"""Parser for Icelandic English-translation PDFs where each article starts on its own line ("Art. 12", "Art. 6 b"),
paragraphs are blank-line separated and footnotes are lines such as "1) Act 98/2009, Art. 20". Used by statutes.py."""
import re

ITEM = re.compile(r'^(\d{1,2}\.|[a-z]\)) ')
FOOT = re.compile(r'^\d{1,2}\) (Acts?\b|Regulation|Act\.)')


def clean_para(q, norm):
    q = re.sub(r'(?<=\]) ?\d{1,2}\)', '', q)           # marker after an amended passage
    q = q.replace('[', '').replace(']', '')
    q = re.sub(r'(?<=[A-Za-z.,;´"]) ?\d{1,2}\)(?=\s|$)', lambda m: m.group(0) if re.search(r'(Art|para|clause)', m.string[max(0, m.start() - 6):m.start()]) else '', q) if not ITEM.match(q) else q
    return norm(q)


def parse_blocks(a, here, norm):
    raw = (here / '.cache' / a['txt']).read_text(encoding='utf8')
    lines = [norm(l.replace('\f', '')) for l in raw.split('\n')]
    s0 = next(i for i, l in enumerate(lines) if l == 'SECTION I')
    units = {}
    state = {'key': None, 'buf': [], 'temp': False}

    def flush():
        key = state['key']
        if key is None:
            return
        paras, cur = [], []
        for l in state['buf'] + ['']:
            if not l:
                if cur:
                    paras.append(' '.join(cur)); cur = []
            elif cur and ITEM.match(l):
                paras.append(' '.join(cur)); cur = [l]
            else:
                cur.append(l)
        for q in paras:
            if FOOT.match(q):
                continue
            q = clean_para(q, norm)
            if q:
                units[key]['lines'].append(q)

    for l in lines[s0:]:
        m = re.fullmatch(r'Art\. (\d+)(?: ?([a-z]))?', l)
        t = re.fullmatch(r'(I{1,3}|IV|V|VI{0,3}|IX|X)\.', l) if state['temp'] else None
        if m or t:
            flush(); state['buf'] = []
            if m:
                n, suf = int(m.group(1)), m.group(2)
                k = 'art-%03d%s' % (n, '-' + suf if suf else ''); lab = 'Art. %d%s' % (n, suf or '')
            else:
                k = 'temp-%s' % t.group(1).lower(); lab = 'Temporary provision ' + t.group(1)
            while k in units:
                k += 'x'
            units[k] = {'label': lab, 'kind': 'art' if m else 'transitional', 'lines': ['# ' + lab.replace('Art.', 'Article')]}
            state['key'] = k
            continue
        if l == 'Temporary Provisions':
            flush(); state['buf'] = []; state['key'] = None; state['temp'] = True
            continue
        if re.fullmatch(r'SECTION [IVXL]+', l):
            flush(); state['buf'] = []; state['key'] = None
            continue
        if state['key'] is None:
            continue
        state['buf'].append(l)
    flush()
    for k, u in units.items():
        u['text'] = '\n'.join(u.pop('lines')) + '\n'
    return a, units
