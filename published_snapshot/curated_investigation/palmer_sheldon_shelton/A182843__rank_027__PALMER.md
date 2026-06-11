# Medium-Review Dossier: A182843

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 27
- Fraud-confidence score: 59.72
- Risk signal score: 62.0
- Linkage confidence score: 56.0
- Confidence band: medium_review

## Court Case Context

- Case number: A182843
- Filing date: 1996-05-28
- Case type: PROBATE OF WILL - LETTERS TESTAMENTARY
- Related party/caption: PALMER-D
- Search lead term: PALMER
- Vulnerability flags: none

## Recorder-Window Signals

- Local recorder matches: 211
- Transfer-like matches: 135
- Exact-name matches: 1
- Distress/lien/default rows: 36
- Distinct matched documents: 211
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A182843__rank_027__PALMER_matches.csv
- Transfer document sample: 19960089363 | 19960103920 | 19960104274 | 19960105701 | 19960106335 | 19960115236 | 19960117878 | 19960130526 | 19960135832 | 19960138451 | 19960138452 | 19960138463 | 19960138621 | 19960138624 | 19960142114 | 19960144670 | 19960149188 | 19960149189 | 19960155446 | 19960155447 | 19960159541 | 19960169078 | 19960170933 | 19960172107 | 19960179157 | 19960183240 | 19960183324 | 19960188755 | 19960193900 | 19960194638 | ... (105 more)
- Distress document sample: 19960089791 | 19960090581 | 19960102154 | 19960109413 | 19960110431 | 19960122252 | 19960125636 | 19960131677 | 19960132561 | 19960133471 | 19960161396 | 19960206970 | 19960209384 | 19960210120 | 19960233888 | 19960233889 | 19960233890 | 19960242573 | 19960251340 | 19960258357 | 19960276033 | 19960285615 | 19960289845 | 19960294477 | 19960302778 | 19960303564 | 19960332755 | 19960341997 | 19960357787 | 19960358413 | ... (6 more)

## Risk Factors

- nearby_transfer_like_activity
- nearby_distress_lien_default_activity
- exact_name_overlap
- case_specific_surname_context

## Cautions

- high_name_collision

## User-Provided Context

- No user-provided actor context matched this lead.

## Document-Type Mix

- GRANT DEED: 36
- ASGT TRUST DEED: 27
- RECONVEYANCE: 23
- TRUST DEED: 23
- RELEASE: 16
- QUITCLAIM DEED: 13
- LIEN STATE: 10
- ASSIGNMENT RNT: 9
- NOTICE FED LIEN: 7
- ABSTRACT JUDGMT: 6
- NT TRUSTEE SALE: 5
- NOTICE DEFAULT: 4

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A182843__rank_027__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 19960088542 | 2/26/1996 | REQUEST NOTICE | PALMER VICKIE L 89-464056 8-30-89 PALMER WILLIAM M 89-464056 8-30-89 | surname_only_low_confidence | no |
| 19960089363 | 2/26/1996 | QUITCLAIM DEED | PALMER ESTHER L / PALMER LAWRENCE L | surname_only_low_confidence | yes |
| 19960089791 | 2/26/1996 | NOTICE FED LIEN | PALMER LILLIAN | surname_only_low_confidence | no |
| 19960090581 | 2/26/1996 | NOTICE DEFAULT | PALMER MARY SHANNON 93-202409 3-26-93 | surname_only_low_confidence | no |
| 19960092185 | 2/27/1996 | NOTICE | PALMER MARSHALL REASSESSMENT DIST 95-1 BOOK 72 PAGES 1-21 ASSMT MAPS PALMER SUSAN J REASSESSMENT DIST 95-1 BOOK 72 PAGES | surname_only_low_confidence | no |
| 19960102154 | 3/1/1996 | LIEN STATE | PALMER SHARON | surname_only_low_confidence | no |
| 19960103920 | 3/4/1996 | ASGT TRUST DEED | PALMER KATIE J | surname_only_low_confidence | yes |
| 19960104274 | 3/4/1996 | RECONVEYANCE | PALMER KENNETH L PALMER PATRICIA A | surname_only_low_confidence | yes |
| 19960105701 | 3/5/1996 | GRANT DEED | PALMER CAROLYN R | surname_only_low_confidence | yes |
| 19960106335 | 3/5/1996 | RECONVEYANCE | PALMER SHATZ BRENDA L | surname_only_low_confidence | yes |
| 19960109413 | 3/6/1996 | ABSTRACT JUDGMT | PALMER SHIRLEY A | surname_only_low_confidence | no |
| 19960110431 | 3/7/1996 | NOTICE DEFAULT | PALMER CLEVELAND 86-629104 12-19-86 PALMER JOYCE 86-629104 12-19-86 | surname_only_low_confidence | no |
| 19960110803 | 3/7/1996 | NT DELQNT ASSMT | PALMER CRAIG B PALMER LYNN M | surname_only_low_confidence | no |
| 19960115236 | 3/8/1996 | ASGT TRUST DEED | PALMER ROSEANN MARIE PALMER SHARON M | surname_only_low_confidence | yes |
| 19960117878 | 3/11/1996 | GRANT DEED | PALMER HOWARD M | surname_only_low_confidence | yes |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
