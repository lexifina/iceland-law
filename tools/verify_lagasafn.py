"""Checks the Lagasafn parts against the editions they were read from (reads .cache and corpus.d only).

1. Latest edition, independently of the parser's paragraph logic: every unit line occurs in the page's whole visible
   text (tags, footnotes, footnote markers and amendment brackets removed), and the units hold nearly all of the
   page's article text (letters only, footnotes and the act's header excluded).
2. History: replaying the versions, the text on each edition's consolidation date equals that edition's text for
   every article, except articles whose change was dated to an amending law's later in-force date.

Usage: python -X utf8 verify_lagasafn.py [act-number ...]
"""
import html, json, re, sys
from pathlib import Path
import parse_lagasafn as P

here = Path(__file__).parent


def visible(t):
    t = P.FOOT.sub(' ', t)
    t = P.SUP.sub('', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    return P.norm(t)


def letters(s):
    return re.sub(r'[^a-záéíóúýþæöð]', '', s.lower())


def main(only):
    eds = P.editions()
    ok = True
    for num in only:
        meta = P.ACTS[num]
        part = json.loads((here / 'corpus.d' / f"{meta['part']}.json").read_text(encoding='utf-8'))
        act = part['acts'][0]
        rows = [(ed, a[num][0]) for ed, a in eds.items() if num in a]
        parsed = []
        for ed, raw in rows:
            u, l, d, e, _ = P.parse_act(raw)
            if u and d:
                parsed.append((d, ed, raw, u))
        parsed.sort(key=lambda r: (r[0], P.edition_sort(r[1])))
        d, ed, raw, units = parsed[-1]
        t = P.decode(raw)
        body = t[t.find('</small><br>'):] if '</small><br>' in t else t
        vis = visible(body)
        state = {}
        for v in act['versions']:
            if 'units' in v:
                state = dict(v['units'])
            for k, x in v.get('changes', {}).items():
                if x is None:
                    state.pop(k, None)
                else:
                    state[k] = x
        missing = [(k, line) for k, x in state.items() for line in x['text'].split('\n')[1:] if line and line not in vis]
        cover = len(letters(''.join(x['text'] for x in state.values()))) / max(1, len(letters(vis)))
        same_as_latest = state == units
        # history replay
        def state_on(day):
            s = {}
            for v in act['versions']:
                if v['from'] > day:
                    break
                if 'units' in v:
                    s = dict(v['units'])
                for k, x in v.get('changes', {}).items():
                    if x is None:
                        s.pop(k, None)
                    else:
                        s[k] = x
            return s
        diffs = 0
        for d2, ed2, raw2, u2 in parsed:
            s = state_on(d2)
            diffs += sum(1 for k in set(s) | set(u2) if s.get(k) != u2.get(k))
        print(f"{meta['slug']}: latest edition {ed} ({d}); units {len(state)}; equals latest edition: {same_as_latest}; "
              f"unit lines not in the page text: {len(missing)}; unit/page letters {cover:.3f}; "
              f"article-states differing from their edition across {len(parsed)} editions: {diffs}")
        for k, line in missing[:5]:
            print('   MISSING', k, line[:120])
        ok = ok and same_as_latest and not missing
    return ok


if __name__ == '__main__':
    sys.exit(0 if main(sys.argv[1:] or list(P.ACTS)) else 1)
