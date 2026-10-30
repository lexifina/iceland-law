# Iceland: law history in git

The law of Iceland as a git history: one file per provision, and the law that made each change as the commit's author, so `git blame` names the law behind every line.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `is/`.

**What is in it now (first build, retrieved 2026-10-29)**

| Folder | Law | Versions | Language |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Republic of Iceland (No. 33, 17 June 1944) | 1 | English translation published by the Prime Minister's Office, as amended to 24 June 1999 (later amendments are not in the translation) |
| `general-penal-code/` | The General Penal Code, No. 19/1940 | 1 | English translation published by the Ministry of Justice (hosted on ministryoffinance.is), as amended up to Act 141/2018 (in force 1 January 2019); retrieved 2026-10-30 |
| `contracts-act/` | Act on contracts, agency and void legal instruments, No. 7/1936 | 1 | English translation published on stjornarradid.is (Government of Iceland), as amended up to Act 108/2006 (in force 1 November 2006); retrieved 2026-10-30 |
| `public-limited-companies-act/` | Act respecting Public Limited Companies, No. 2/1995 | 1 | English translation published on government.is, as amended up to 1 May 2011; retrieved 2026-10-30 |

**Icelandic texts with dated history (added 2026-10-30)**

| Folder | Law | History |
| --- | --- | --- |
| `stjornarskra/` | Stjórnarskrá lýðveldisins Íslands, nr. 33/1944 | Every Lagasafn edition read, from 1995 on |
| `almenn-hegningarlog/` | Almenn hegningarlög, nr. 19/1940 (General Penal Code) | Every Lagasafn edition read, from 1995 on |
| `log-um-medferd-sakamala/` | Lög um meðferð sakamála, nr. 88/2008 (Criminal Procedure Act) | From its first edition (in force 1 January 2009) |
| `log-um-medferd-einkamala/` | Lög um meðferð einkamála, nr. 91/1991 (Civil Procedure Act) | Every Lagasafn edition read, from 1995 on |
| `samningalog/` | Lög um samningsgerð, umboð og ógilda löggerninga, nr. 7/1936 (Contracts Act) | Every Lagasafn edition read, from 1995 on |
| `log-um-stettarfelog-og-vinnudeilur/` | Lög um stéttarfélög og vinnudeilur, nr. 80/1938 (Trade Unions and Industrial Disputes Act) | Every Lagasafn edition read, from 1995 on |

These are the authentic Icelandic texts, from the editions of Lagasafn, the Althingi's consolidated law collection, which republishes every act in force two or three times a year. The oldest edition read is the act's first commit ("oldest version available", credited to the Althingi as publisher). After that, each change to an article is credited to the amending law(s) that the article's footnotes name for the first time in that edition, and dated to the day the act's own list of amending laws says they took effect ("tóku gildi"). A change with no new footnote law is committed as unexplained, dated to the edition's consolidation date. Square brackets marking amended passages and footnote markers are removed, "…" marks a passage the source shows as repealed, and chapter headings and the temporary provisions (ákvæði til bráðabirgða) are left out. Iceland has no civil code or labour code: the Contracts Act and the Trade Unions and Industrial Disputes Act are the nearest equivalents.

This is a first, small build, not the whole statute book. The Constitution, the Penal Code, the Contracts Act and the Public Limited Companies Act (the nearest commercial-law equivalent; Iceland has no commercial code) are in. Iceland has no civil code either; its nearest equivalent, the Contracts Act No. 7/1936, is in, from the English translation the Government of Iceland publishes as a Word file. Notes on the three statute translations: the translation's square brackets (which mark amended passages), footnote markers and footnotes citing amending acts are removed, `...` marks a passage the source shows as repealed, and chapter headings are left out. The English translations have no dated history: each is one "oldest version available" commit, dated from the source's own date and credited to the publisher. Texts are in the official language shown above; the English is a translation where marked, and the original governs.

Sources and terms are in `LICENSE`; how it was built is in `REPRODUCE.md`. Not legal advice; for anything that matters, read the original.
