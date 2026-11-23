# Search, verification and disposition log

## 24 October 2026 — initial purposive pass

**Purpose:** establish a balanced starting corpus and repository, not complete a systematic review. Sources were selected for their roles in the debate, methods or economics/finance applications. Identity checks used retrieved material independent of model recall. This does not mean every record received two independent checks or that reported findings were replicated.

Four parallel research streams covered the original exchange; inference reform and power; decision theory and finance; and intervals/equivalence/design. Searches used exact titles and author combinations, then publisher, author and institutional records. Consulted URLs, document versions, locators and limitations are retained per source in [registry.json](registry.json). No local copies of paywalled books or articles were acquired.

**Discovery limitation:** an OpenAlex API query for `statistical economic significance` was attempted through the web tool and returned “not accessible”. A local Python request failed at DNS resolution in the restricted network environment. Other research streams reported the same web-tool access barrier. Verification therefore used web retrieval of publisher/author/institution records and bibliographic repositories. No OpenAlex verification, citation counts, successful API result or quota exhaustion is claimed. No AJG grades were used.

### Recorded query examples actually used in the root stream

- `Lakens 2017 Equivalence Tests A Practical Primer t tests correlations meta analyses DOI`
- `Schuirmann 1987 comparison two one-sided tests procedure power approach equivalence average bioavailability DOI`
- `Lakens Scheel Isager 2018 Equivalence Testing for Psychological Research tutorial DOI`
- `Neyman 1937 Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability confidence intervals 333 380`
- `Morey Hoekstra Rouder Lee Wagenmakers 2016 fallacy placing confidence confidence intervals DOI`
- `Hoenig Heisey 2001 Abuse of Power pervasive fallacy data analysis DOI`
- `Lakens 2022 Sample Size Justification Collabra Psychology DOI`

This is a provenance summary, not a full search-engine hit log. Parallel streams used targeted title/author lookups; their consulted records are preserved, but an exhaustive list of every query and rejected search hit was not reconstructed.

## Metadata corrections and version decisions

| Item | Decision / basis |
|---|---|
| *The Standard Error of Regressions* | Published in JEL; AER is the surveyed journal. No DOI inferred from the JSTOR identifier. |
| *Size matters* | Use final Journal of Socio-Economics version. Econ Journal Watch version is not counted separately. |
| *The Cult of Statistical Significance* | Cite Ziliak then McCloskey, supported by JSTOR and author institutional page; current publisher webpage reverses displayed order. Record print year 2008 rather than ebook availability date. Book unread. |
| *Signifying nothing* | Published PDF establishes pp. 39–55; author HTML gives 39–57. Preserve discrepancy, use published pagination. |
| Hoover–Siegler | Prefer 2008 published versions over the separately hosted 2005 draft. Their rejoinder's parenthetical p-value/Type I error wording is flagged for technical checking, not adopted. |
| ASA status | 2016 statement is official; 2019 Wasserstein–Schirm–Lazar editorial explicitly disclaims ASA endorsement. |
| Benjamin et al. | Online 2017, issue year 2018. Author list explicitly abbreviated in this scaffold; complete author import remains due. |
| Amrhein et al. | Online bibliographic title differs from the publisher PDF's display heading; record the online title with that caveat. |
| Manski 2021 | Final title is *Econometrics for Decision Making: Building Foundations Sketched by Haavelmo and Wald*. Publisher note supersedes the 2019 draft *Statistical Inference for Statistical Decisions*. Do not count both. |
| Wald | 1950 book metadata checked; the Nature review DOI is not the book DOI. Book unread. |
| Issue years | Morey et al. 2016, Deaton–Cartwright 2018, Harvey–Liu–Zhu 2016 use issue years; different online dates remain in notes. Hoenig–Heisey is 2001, not the later online archive date. |
| Lakens 2022 | 33267 is an article identifier, not a page range. |

## Selection and exclusions

32 distinct works retained. The selection includes methodological articles, academic books, editorials and commentary; it is not described as 32 empirical studies or 32 completely read papers. No selected reference is retained solely from memory. Drafts and duplicate versions listed above were not counted. A possible Gelman–Loken science-crisis overview was not pursued once more directly relevant methods and finance sources filled the scope; no unverified citation for it was added.

Publisher pages or PDFs that were blocked were sometimes available as actual abstracts or extended source text through indexed retrieval. Records disclose this. Brief snippets were used for discovery or metadata only. Full-text availability is not labelled full-text reading. Metadata-only sources cannot support detailed source claims.

## Coverage still to complete

The latest selected work is from 2023. Conduct a focused 2024–2026 update and forward/backward citation tracing before calling the corpus contemporary through the search date. Review at least one additional economics candidate on partial identification, policy learning or robust welfare decisions; consider replacing overlapping reform commentary to remain within 25–35. Prioritise accessible primary treatments of any historical arguments that become central.

Acquire and read the book and classical foundations as needed, then deepen source notes. The original AER coding debate and later finance findings have not been independently reproduced. The [review gate](../reviews/review-gate.md) remains open.

## 24 October 2026 — close-reading and contemporary-update milestone

The earlier “coverage still to complete” section records the scaffold state; the latest core work is now 2026. See the [targeted update and actual queries](update-2024-2026.md) for additions, candidate dispositions, primary links, access failures and date/version checks. The core now has 35 distinct works: three 2008 exchange articles are fully read, while other depths remain explicit. The 2025 equivalence contribution is a working paper, and the 2026 robust-Bayes contribution is FirstView. Drafts and finals are not counted twice.

The published exchange was read in full using temporary author-hosted PDFs. Complete reading is not an independent audit of cited AER articles or historical claims. The rejoinder confirms that the book was unavailable when the exchange was written; the book remains separately unread. No full copyrighted text or temporary extracted source text is committed.

OpenAlex was not used successfully and was not retried in this update; primary publisher/author/institutional retrieval was used. The targeted search is not exhaustive, and no citation-count coverage claim is made. The review gate is **NOT PASSED / closed**, as instructed by the user.

## 24 October 2026 — direct-book, supplied-file and AER audit

The earlier unread/unaudited statements above describe their respective milestones. Current coverage is in the [book ledger](../wiki/evidence/cult-2008-reading.md), [coding audit](../wiki/evidence/aer-coding-audit.md) and [supporting registry](aer-audit/supporting-registry.json). The core remains 35 works. Supporting application papers, draft/final versions, the EJW version, lecture and court sources are recorded separately; they are not silently counted as new core contributions.

Public access checks covered the publisher, JSTOR, DOI/Fulcrum, Open Library, the author's prepublication preface, and Google Books. The authorised preview for ISBN9780472050079 exposed image-only pages; printed pp. 57–61 and 74–85 were read visually. The publisher's Look Inside yielded only annotated contents. Full-book access was not obtained. Third-party full-text hits of uncertain provenance were not used. The attempted Google Drive search returned a tool-interface error, not zero search results. A narrow local filename search near the project found no copy. The user then supplied `Downloads/Ziliak_Week2.cleaned.pdf`, verified as a31-slide 2012 lecture rather than the 2008 book.

The public author-hosted 1980s/1990s worksheets and omissions list were retrieved from Hoover's Duke site. Exact URLs, hashes, source coverage and access failures are preserved in the [coding manifest](aer-audit/coding-manifest.json) and [access log](aer-audit/coding-access-log.json). The audit distinguishes the original 137-row matrix from the book's expanded 187-paper results, and 281 author-paper rows from independent papers. It records article-identity checks and contradictions instead of inventing replacement scores.

The case streams searched titles, authors and institutional sources for the five disputed articles. Actual queries, selected-page coverage and access failures are preserved in supporting records and case ledgers. Published primary sections were obtained for Bernanke–Blinder, Becker et al. and Woodbury–Spiegelman; the latter was readable author-uploaded published text, without visual verification of its tables. Final Darby remained metadata-only and final Bernheim–Wantz abstract-level; earlier NBER drafts supply explicitly bounded evidence. Successful HTTP responses that contained challenge HTML were not treated as downloaded PDFs.

The supplied lecture prompted the exact root query `site.supremecourt.gov opinions 2010 Matrixx Siracusano 09-1156 pdf`, followed by an agent reading of the official United States Reports text and an official *Basic* PDF. The [court audit](../wiki/evidence/matrixx-2011-lecture-audit.md) separates holdings, allegations, oral-argument quotations and interpretation. This was a targeted historical verification, not a current legal review or an exhaustive literature search.

No complete copyrighted source, extracted source text or preview image is committed. The repository retains original notes, factual coding transcriptions, bibliography, checksums and reproducible diagnostics. Remaining source access is documented rather than inferred from snippets or earlier drafts. The slide gate remains closed.

## 24 October 2026 — remaining sources and final-paper reading

A renewed targeted pass searched final Darby and Bernheim–Wantz routes through author/institutional pages, JSTOR, reprint and course-list leads, bibliographic APIs and public archive indexes. The [permanent final-paper log](aer-audit/final-paper-access-log.json) preserves 27 Darby queries and 19 Bernheim–Wantz queries, exact attempted routes, responses, version checks and later user-supply events. The public routes initially did not yield final text. Ordinary JSTOR browser interfaces offered library login; this was a session access boundary, not evidence that the user lacked entitlement. A further Drive attempt failed at the tool interface, not with an empty search result.

The user then downloaded both final PDFs into Downloads. Their title pages, journal headers, pagination, stable identifiers and hashes were checked against the independently verified identities. Darby printed pp. 301–322 were read, with selected visual checks; Bernheim–Wantz printed pp. 532–533, 538–549 and the conclusion continuation on p. 550 were read, with selected visuals. The [reading ledgers](aer-audit/README.md) disclose what was and was not reviewed. Earlier failed URLs remain failed attempts; later local access resolves the source gap rather than retrospectively changing those outcomes.

OpenAlex **did succeed in this pass**, unlike the earlier scaffold attempt. Its retrieved records combine draft and final locations, often under the working-paper DOI; those machine records were not used to relabel a draft as the final article. The supplied final files demonstrate substantive version changes, including Darby's estimates/horizon and Bernheim–Wantz's added magnitude panel. The latter's NBER DOI was corroborated only for the draft. Final AER DOIs remain unverified and blank.

The [expanded-matrix log](aer-audit/expanded-search-log.json) records 27 routes and 15 discovery queries, including actual archived author pages from 2008, 2010 and 2011. No 187-paper matrix, list of the 50 additions or versioned article crosswalk was recovered. This is not a global absence claim. The author articles index did yield the final JSE 2004 scan: pp. 527–535 and 540–542 were visually read. [Version checks](../wiki/evidence/jse-2004-version-check.md) establish which table discrepancies persist and which do not; the article still concerns the earlier 137-paper survey.

The synthesis and current case/claim notes now use the final text while preserving unresolved selection, non-rejection, identification and coding-validity questions. No empirical replication, invented matrix, new core work, external correspondence or slide generation is claimed. The [latest review](../reviews/2026-10-24-final-source-review.md) records independent checks and revisions.
