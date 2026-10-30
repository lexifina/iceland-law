# How this repository was made (Iceland)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Government of Iceland, Prime Minister's Office: Constitution (English translation) | <https://www.government.is/topics/governance-and-national-symbols/constitution/> | 2026-10-29 | free use with acknowledgement of the source (government.is, Disclaimer and copyright) |
| Ministry of Justice of Iceland: The General Penal Code, No. 19/1940 (English translation) | <https://www.ministryoffinance.is/library/01-Ministries/Ministry-of-Justice/Generlal%20Penal%20Code,%20No.19%201940.pdf> | 2026-10-30 | free use with acknowledgement of the source (Government of Iceland sites) |
| Ministry of Justice of Iceland: Act respecting Public Limited Companies, No. 2/1995 (English translation) | <https://www.government.is/library/04-Legislation/Act%20No%202-1995.pdf> | 2026-10-30 | free use with acknowledgement of the source (Government of Iceland sites) |
| Government of Iceland: Act on contracts, agency and void legal instruments, No. 7/1936 (English translation) | <https://www.stjornarradid.is/media/atvinnuvegaraduneyti-media/media/acrobat/samningalog_tyddaensku.doc> | 2026-10-30 | free use with acknowledgement of the source (Government of Iceland sites) |
| Alþingi, Lagasafn: Stjórnarskrá lýðveldisins Íslands, nr. 33/1944 (67 editions, 119 to 158a) | <https://www.althingi.is/lagas/nuna/1944033.html> | 2026-10-30 | Icelandic statutes are not protected by copyright (Höfundalög nr. 73/1972, 9. gr.) |
| Alþingi, Lagasafn: Almenn hegningarlög, nr. 19/1940 (65 editions, 119 to 157b) | <https://www.althingi.is/lagas/nuna/1940019.html> | 2026-10-30 | Icelandic statutes are not protected by copyright (Höfundalög nr. 73/1972, 9. gr.) |
| Alþingi, Lagasafn: Lög um meðferð sakamála, nr. 88/2008 (43 editions, 135b to 157c) | <https://www.althingi.is/lagas/nuna/2008088.html> | 2026-10-30 | Icelandic statutes are not protected by copyright (Höfundalög nr. 73/1972, 9. gr.) |
| Alþingi, Lagasafn: Lög um meðferð einkamála, nr. 91/1991 (62 editions, 119 to 157c) | <https://www.althingi.is/lagas/nuna/1991091.html> | 2026-10-30 | Icelandic statutes are not protected by copyright (Höfundalög nr. 73/1972, 9. gr.) |
| Alþingi, Lagasafn: Lög um samningsgerð, umboð og ógilda löggerninga, nr. 7/1936 (63 editions, 119 to 157b) | <https://www.althingi.is/lagas/nuna/1936007.html> | 2026-10-30 | Icelandic statutes are not protected by copyright (Höfundalög nr. 73/1972, 9. gr.) |
| Alþingi, Lagasafn: Lög um stéttarfélög og vinnudeilur, nr. 80/1938 (63 editions, 119 to 157b) | <https://www.althingi.is/lagas/nuna/1938080.html> | 2026-10-30 | Icelandic statutes are not protected by copyright (Höfundalög nr. 73/1972, 9. gr.) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Iceland (English translation) | 1 | 1999-06-24 to 1999-06-24 |
| `general-penal-code` | The General Penal Code, No. 19/1940 (English translation) | 1 | 2019-01-01 to 2019-01-01 |
| `public-limited-companies-act` | Act respecting Public Limited Companies, No. 2/1995 (English translation) | 1 | 2011-05-01 to 2011-05-01 |
| `contracts-act` | Act on contracts, agency and void legal instruments, No. 7/1936 (English translation) | 1 | 2006-11-01 to 2006-11-01 |
| `stjornarskra` | Stjórnarskrá lýðveldisins Íslands, nr. 33/1944 | 4 | 1995-10-01 to 2019-05-03 |
| `almenn-hegningarlog` | Almenn hegningarlög, nr. 19/1940 | 70 | 1995-10-01 to 2026-04-20 |
| `log-um-medferd-sakamala` | Lög um meðferð sakamála, nr. 88/2008 | 35 | 2008-10-01 to 2026-06-27 |
| `log-um-medferd-einkamala` | Lög um meðferð einkamála, nr. 91/1991 | 34 | 1995-10-01 to 2024-07-01 |
| `samningalog` | Lög um samningsgerð, umboð og ógilda löggerninga, nr. 7/1936 | 6 | 1995-10-01 to 2011-09-30 |
| `log-um-stettarfelog-og-vinnudeilur` | Lög um stéttarfélög og vinnudeilur, nr. 80/1938 | 14 | 1995-10-01 to 2022-07-07 |

The build made 153 commits:

| Commits | Kind |
| ---: | --- |
| 10 | first version of an act |
| 122 | one law on its in-force day |
| 21 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 126 laws in the record.
- 286 tags.

## Dates

Each commit is dated at noon (Atlantic/Reykjavik) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Constitution is dated by the last amendment its published English text states (24 June 1999). https://www.government.is/topics/governance-and-national-symbols/constitution/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `82f913adb92b79688c22c48f0a4c978ae76d94f883d825ad5eb87904dc205ff7` (2431189 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

167 versions of 10 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 153 history commits and 286 tags (history tip `0b8e5a9b63fdbf3fabdd1261e6c33ccd6f147af6`).

## Decisions made by hand

- English is built: the Prime Minister's Office publishes an English translation.
- One version dated 1999-06-24, the last amendment date the source names; no earlier or later versions are online at the source.
- One version only for general-penal-code, dated 2019-01-01 (the last in-force date among the amendments the translation lists); no earlier or later versions are online at the source. Square brackets that mark amended passages, footnote markers and the footnotes citing amending acts were removed; "..." marks passages the source shows as repealed and is kept as printed. Chapter headings are left out.
- One version only for public-limited-companies-act, dated 2011-05-01 (the last in-force date among the amendments the translation lists); no earlier or later versions are online at the source. Square brackets that mark amended passages, footnote markers and the footnotes citing amending acts were removed; "..." marks passages the source shows as repealed and is kept as printed. Chapter headings are left out.
- One version only for contracts-act, dated 2006-11-01 (the in-force date of the last amendment the translation lists); no earlier or later versions are online at the source. Square brackets that mark amended passages, footnote markers and footnotes citing amending acts were removed. Chapter headings are left out.
- stjornarskra: built from 67 Lagasafn editions (119 to 158a, consolidated 1995-10-01 to 2026-10-01). The first is 'oldest version available'. Each later change to a provision is credited to the amending laws its footnotes name for the first time in that edition, and dated to the latest in-force date the act's header gives for them ('tóku gildi'); a change with no new footnote law (2) is dated to the edition's consolidation date and committed as unexplained; 0 change(s) dated before the provision's previous change were moved to the day after it.
- stjornarskra: square brackets marking amended passages and footnote markers are removed, the footnotes themselves are used only for credits, '…' marks passages the source shows as repealed, and chapter headings and the temporary provisions (ákvæði til bráðabirgða, anchored inconsistently from edition to edition) are left out; each article is one file.
- almenn-hegningarlog: built from 65 Lagasafn editions (119 to 157b, consolidated 1995-10-01 to 2026-04-20). The first is 'oldest version available'. Each later change to a provision is credited to the amending laws its footnotes name for the first time in that edition, and dated to the latest in-force date the act's header gives for them ('tóku gildi'); a change with no new footnote law (16) is dated to the edition's consolidation date and committed as unexplained; 0 change(s) dated before the provision's previous change were moved to the day after it.
- almenn-hegningarlog: square brackets marking amended passages and footnote markers are removed, the footnotes themselves are used only for credits, '…' marks passages the source shows as repealed, and chapter headings and the temporary provisions (ákvæði til bráðabirgða, anchored inconsistently from edition to edition) are left out; each article is one file.
- log-um-medferd-sakamala: built from 43 Lagasafn editions (135b to 157c, consolidated 2008-10-01 to 2026-09-01). The first is 'oldest version available'. Each later change to a provision is credited to the amending laws its footnotes name for the first time in that edition, and dated to the latest in-force date the act's header gives for them ('tóku gildi'); a change with no new footnote law (0) is dated to the edition's consolidation date and committed as unexplained; 0 change(s) dated before the provision's previous change were moved to the day after it.
- log-um-medferd-sakamala: square brackets marking amended passages and footnote markers are removed, the footnotes themselves are used only for credits, '…' marks passages the source shows as repealed, and chapter headings and the temporary provisions (ákvæði til bráðabirgða, anchored inconsistently from edition to edition) are left out; each article is one file.
- log-um-medferd-einkamala: built from 62 Lagasafn editions (119 to 157c, consolidated 1995-10-01 to 2026-09-01). The first is 'oldest version available'. Each later change to a provision is credited to the amending laws its footnotes name for the first time in that edition, and dated to the latest in-force date the act's header gives for them ('tóku gildi'); a change with no new footnote law (12) is dated to the edition's consolidation date and committed as unexplained; 0 change(s) dated before the provision's previous change were moved to the day after it.
- log-um-medferd-einkamala: square brackets marking amended passages and footnote markers are removed, the footnotes themselves are used only for credits, '…' marks passages the source shows as repealed, and chapter headings and the temporary provisions (ákvæði til bráðabirgða, anchored inconsistently from edition to edition) are left out; each article is one file.
- samningalog: built from 63 Lagasafn editions (119 to 157b, consolidated 1995-10-01 to 2026-04-20). The first is 'oldest version available'. Each later change to a provision is credited to the amending laws its footnotes name for the first time in that edition, and dated to the latest in-force date the act's header gives for them ('tóku gildi'); a change with no new footnote law (1) is dated to the edition's consolidation date and committed as unexplained; 0 change(s) dated before the provision's previous change were moved to the day after it.
- samningalog: square brackets marking amended passages and footnote markers are removed, the footnotes themselves are used only for credits, '…' marks passages the source shows as repealed, and chapter headings and the temporary provisions (ákvæði til bráðabirgða, anchored inconsistently from edition to edition) are left out; each article is one file.
- log-um-stettarfelog-og-vinnudeilur: built from 63 Lagasafn editions (119 to 157b, consolidated 1995-10-01 to 2026-04-20). The first is 'oldest version available'. Each later change to a provision is credited to the amending laws its footnotes name for the first time in that edition, and dated to the latest in-force date the act's header gives for them ('tóku gildi'); a change with no new footnote law (3) is dated to the edition's consolidation date and committed as unexplained; 0 change(s) dated before the provision's previous change were moved to the day after it.
- log-um-stettarfelog-og-vinnudeilur: square brackets marking amended passages and footnote markers are removed, the footnotes themselves are used only for credits, '…' marks passages the source shows as repealed, and chapter headings and the temporary provisions (ákvæði til bráðabirgða, anchored inconsistently from edition to edition) are left out; each article is one file.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the parser; it did not write or alter any legal text. 0 model calls at data-build time.
