# Ísland: lagasaga í git

**Íslenska** · **[Or read it in English](README.en.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/is/effort-dark.svg">
<img alt="Íslensk lög í þessari geymslu: innihald, breytingar eftir gildistökuári, heildstæðni miðað við opinberar heimildir og réttmæti innihaldsins" src="data/is/effort-light.svg" width="880">
</picture>

Lög Íslands sem git-saga: ein skrá fyrir hverja grein, ein færsla (commit) fyrir hver breytingalög á þeim degi sem þau tóku gildi, og þau lög skráð sem höfundur færslunnar. `git blame` nefnir lögin að baki hverri línu; `git log` sýnir hverja breytingu á grein; með því að velja dagsetningu fæst textinn sem var í gildi þann dag.

Hluti af [lexifina/global-law](https://github.com/lexifina/global-law), einni git-sögu fyrir lög allra landa: þetta eru landslög Íslands, sem global-law les í `iceland/national/acts/`.

**Innihald nú:** sex lög úr Lagasafni, safni Alþingis yfir gildandi lög, með 163 útgáfum frá 1995 (stjórnarskráin, almenn hegningarlög, lög um meðferð sakamála, lög um meðferð einkamála, samningalög og lög um stéttarfélög og vinnudeilur); og enskar þýðingar Stjórnarráðs Íslands á fernum lögum (stjórnarskránni, almennum hegningarlögum, samningalögum og lögum um hlutafélög), ein útgáfa af hverri. Í möppu hverra laga er `README.md` sem telur upp hverja grein, hve oft henni var breytt og hvenær ([`log-um-stettarfelog-og-vinnudeilur/README.md`](log-um-stettarfelog-og-vinnudeilur/README.md)); [`REPRODUCE.md`](REPRODUCE.md) telur upp öll lögin með útgáfum þeirra.

Hver lög eru í möppu sem heitir eftir titli þeirra (`log-um-stettarfelog-og-vinnudeilur/` eru lög um stéttarfélög og vinnudeilur, nr. 80/1938, það sem næst kemst vinnulögbók á Íslandi); hver grein er ein skrá (`gr-020.md` er 20. gr.). Ensku þýðingarnar eru í möppum og skrám með enskum heitum (`constitution/`, `art-001.md`).

Íslensku textarnir eru eins og Lagasafn birtir þá. Ensku textarnir eru þýðingar sem Stjórnarráð Íslands birtir; íslenski textinn gildir.

## Spurningar sem git-skipanir

| Spurning | Skipun |
| --- | --- |
| Allar breytingar á 20. gr. laga um stéttarfélög og vinnudeilur | `git log -p --word-diff -- log-um-stettarfelog-og-vinnudeilur/gr-020.md` |
| Hvaða lög skrifuðu hverja línu 20. gr.? | `git blame log-um-stettarfelog-og-vinnudeilur/gr-020.md` |
| Allar útgáfur laga um stéttarfélög og vinnudeilur, með þeim degi sem hver tók gildi | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- log-um-stettarfelog-og-vinnudeilur` |
| 20. gr. eins og hún var í gildi 1. janúar 2015 | `python tools/on.py 2015-01-01 log-um-stettarfelog-og-vinnudeilur 20` |

**Utan git** hýsum við þessi gögn einnig opinberlega og án endurgjalds:

- **[Spyrjið Claude um íslensk lög](https://global-law.lexifina.com/v1/try_claude?country=iceland)**: opnar Claude með fyrstu spurningu tilbúna.
- **[Spyrjið ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=iceland)**: sama spurning í ChatGPT.
- **[Kallið á API-ið í vafranum](https://global-law.lexifina.com/v1/search_law?query=kjarasamning&jurisdictions=iceland)**: leit í íslenskum lögum að „kjarasamning“, svar á JSON-sniði. Skjölunin er [hér](https://lexifina.com/api/global-law).

Báðir aðstoðarmennirnir lesa gögnin í gegnum ókeypis tengið Global law (MCP, `https://global-law.lexifina.com/mcp`); í fyrsta sinn gefur spjallið ykkur hlekkinn sem bætir því við. Spyrjið á íslensku eða ensku.

**Auðvelt er að hýsa það sjálf.** Allt sem þarf er git og Python, og verkfærin keyra á ykkar eigin tölvu:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add iceland/national/acts
python3 tools/law.py show 2026-01-01 iceland/national/acts/log-um-stettarfelog-og-vinnudeilur/gr-020.md
```

Sé afritið opnað í Claude Code, Cursor, VS Code eða Codex ræsir það einnig staðbundinn MCP-þjón með sömu verkfærum ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dagsetningar

Hver færsla er dagsett á hádegi að íslenskum tíma (Atlantic/Reykjavik) þann dag sem breytingin tók gildi, og sá dagur stendur einnig í `In-force:`-eftirvagni (trailer) hennar:

- fyrir breytingu á grein, sá dagur sem skrá laganna sjálfra yfir breytingalög segir að lögin sem neðanmálsgreinar greinarinnar nefna í fyrsta sinn hafi tekið gildi („tóku gildi“), sá síðasti ef lögin eru fleiri en ein;
- fyrir breytingu sem engin ný neðanmálsgrein skýrir (21 færsla), sá dagur sem útgáfa Lagasafns er uppfærð til;
- fyrir fyrstu útgáfu laga, sá dagur sem elsta útgáfa Lagasafns sem lesin var er uppfærð til (1. október 1995; 1. október 2008 fyrir lög um meðferð sakamála); fyrir enska þýðingu, dagur síðustu breytingar sem hún nær til.

Hver breyting er eignuð þeim breytingalögum sem neðanmálsgreinarnar nefna, eins og Lagasafn ritar þau (`Lög nr. 42/2022`); breytingar sem engin neðanmálsgrein skýrir eru eignaðar `Alþingi (Lagasafn)`. Fyrsta útgáfa laga er „oldest version available“ (elsta tiltæka útgáfa), eignuð Alþingi sem útgefanda; hver ensk þýðing er eignuð útgefanda sínum.

## Hvernig það er yfirfarið

- `tools/verify_lagasafn.py` ber íslensku textana saman við þær útgáfur Lagasafns sem þeir voru lesnir úr: hver lína nýjasta textans kemur fyrir á síðu útgáfunnar, og þegar útgáfur laganna eru raktar í tímaröð fæst texti hverrar útgáfu Lagasafns á þeim degi sem hún er uppfærð til, nema þar sem breyting er dagsett á síðari gildistökudegi.
- `tools/check_repo.py` les hverja útgáfu aftur úr git á þeim degi sem hún tók gildi og deginum áður og ber hana saman við gagnasafnið (167 útgáfur af 10 lögum, 0 frávik); það kannar einnig að eftirvagnar hverrar færslu séu læsilegir, að engar sameiningarfærslur (merge commits) séu til og að engin dagsetning færslu fari aftur á bak eða sé í framtíðinni.
- Önnur smíð úr sama gagnasafni gaf sömu tætigildi (hash) fyrir allar 153 færslurnar og 286 merkin (tags). Niðurstöðurnar eru í [`REPRODUCE.md`](REPRODUCE.md).
- Sagan er aðeins aukin: `tools/append.py` bætir nýrri útgáfum ofan á og endurritar aldrei birta færslu.

## Það sem hún sýnir ekki

- **Flest íslensk lög.** Sex lög úr Lagasafni eru hér; önnur gildandi lög, reglugerðir og samþykktir sveitarfélaga eru það ekki.
- **Útgáfur fyrir 1995.** Fyrsta færsla hverra laga er elsta útgáfa Lagasafns sem lesin var (útgáfa 119, uppfærð til 1. október 1995), ekki lögin eins og þau voru fyrst birt í Stjórnartíðindum.
- **Kaflafyrirsagnir og ákvæði til bráðabirgða** eru ekki með; „…“ merkir textahluta sem heimildin sýnir sem felldan brott.
- **Hvaða lög gerðu sumar breytingar.** Sú 21 færsla sem engin ný neðanmálsgrein skýrir er eignuð útgefandanum.
- **Uppfærðar enskar þýðingar.** Hver þeirra nær aðeins til síðustu breytingar sem útgefandinn tók með: stjórnarskráin til 24. júní 1999, almenn hegningarlög til laga nr. 141/2018, samningalög til laga nr. 108/2006 og lög um hlutafélög til 1. maí 2011.
- **Dómar, þjóðréttarsamningar og EES-réttur.** Ekkert af því er hér.

## Heimildir

| Heimild | Tegund | Fyrri útgáfur | Athugasemdir |
| --- | --- | --- | --- |
| [Lagasafn](https://www.althingi.is/lagasafn/) (Alþingi) | Safn gildandi laga með áorðnum breytingum | já, allt að 67 útgáfur Lagasafns fyrir hver lög frá 1995 | Lesið úr afritum í Internet Archive; textinn eins og hann er birtur í Stjórnartíðindum gildir |
| [Stjórnarráð Íslands](https://www.government.is) (forsætisráðuneytið, dómsmálaráðuneytið) | Enskar þýðingar | ein útgáfa af hverri | Ekki frumtextinn |

## Leyfi

Sjá [`LICENSE`](LICENSE). Íslensk lög njóta ekki verndar höfundalaga (höfundalög nr. 73/1972, 9. gr.); á vefjum Stjórnarráðs Íslands er öllum frjálst að nota ensku þýðingarnar, gegn því að heimildar sé getið. Uppröðun Lexifina, textar færslna og verkfæri eru undir CC BY 4.0.

Ekkert gervigreindarlíkan skrifaði, þýddi eða leiðrétti lagatexta og ekkert slíkt keyrir þegar sagan er smíðuð; forskriftirnar skrifaði gervigreindarlíkan (sjá [`REPRODUCE.md`](REPRODUCE.md)).

Þetta er þýðing á ensku útgáfunni ([README.en.md](README.en.md)); ef þær stangast á gildir enska útgáfan.

## Meira

Úr geymslunni [lexifina/global-law](https://github.com/lexifina/global-law) (á ensku):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): allir eiginleikar og það sem hvert safn þarf að styðja (`git blame`, `law.py`, MCP-verkfæri)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): spurningar og svör · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): tillögur að breytingum · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): MCP-þjónn · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): hvernig það var smíðað · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): hversu nýlegt hvert safn er · [Vöktun](https://github.com/lexifina/global-law/tree/main/monitoring): hvort uppfærslur virka · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): hvernig hver opinber heimild er vöktuð vegna breytinga
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): hversu hröð verkfærin eru, mælt
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): gröf og tengsl þvert á lög alls heimsins
- [Veikleikar](https://github.com/lexifina/global-law/tree/main/vulnerabilities): villur í lögum eins og þau voru birt
