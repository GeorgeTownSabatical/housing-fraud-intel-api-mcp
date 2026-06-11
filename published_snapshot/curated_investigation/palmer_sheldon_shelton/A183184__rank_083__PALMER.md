# Medium-Review Dossier: A183184

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 83
- Fraud-confidence score: 55.72
- Risk signal score: 77.0
- Linkage confidence score: 21.0
- Confidence band: medium_review

## Court Case Context

- Case number: A183184
- Filing date: 1996-06-21
- Case type: LPS CONSERVATORSHIP (WI 5350)
- Related party/caption: PALMER-C
- Search lead term: PALMER
- Vulnerability flags: conservatorship | mental_health

## Recorder-Window Signals

- Local recorder matches: 207
- Transfer-like matches: 144
- Exact-name matches: 0
- Distress/lien/default rows: 28
- Distinct matched documents: 207
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A183184__rank_083__PALMER_matches.csv
- Transfer document sample: 19960138451 | 19960138452 | 19960138463 | 19960138621 | 19960138624 | 19960142114 | 19960144670 | 19960149188 | 19960149189 | 19960155446 | 19960155447 | 19960159541 | 19960169078 | 19960170933 | 19960172107 | 19960179157 | 19960183240 | 19960183324 | 19960188755 | 19960193900 | 19960194638 | 19960197305 | 19960212988 | 19960212991 | 19960216729 | 19960221704 | 19960221705 | 19960221785 | 19960222552 | 19960222553 | ... (114 more)
- Distress document sample: 19960161396 | 19960206970 | 19960209384 | 19960210120 | 19960233888 | 19960233889 | 19960233890 | 19960242573 | 19960251340 | 19960258357 | 19960276033 | 19960285615 | 19960289845 | 19960294477 | 19960302778 | 19960303564 | 19960332755 | 19960341997 | 19960357787 | 19960358413 | 19960362804 | 19960385230 | 19960408321 | 19960409674 | 19960410872 | 19960424702 | 19960448671 | 19960477076

## Risk Factors

- vulnerable_population_case
- nearby_transfer_like_activity
- nearby_distress_lien_default_activity
- dense_recorder_activity
- conservatorship_context
- case_specific_surname_context

## Cautions

- high_name_collision
- surname_or_caption_only_linkage

## User-Provided Context

- No user-provided actor context matched this lead.

## Document-Type Mix

- GRANT DEED: 37
- TRUST DEED: 27
- ASGT TRUST DEED: 25
- RECONVEYANCE: 25
- RELEASE: 13
- QUITCLAIM DEED: 12
- ASSIGNMENT RNT: 10
- LIEN STATE: 10
- NT TRUSTEE SALE: 5
- ABSTRACT JUDGMT: 5
- TRUSTEES DEED: 5
- POWER ATTORNEY: 4

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A183184__rank_083__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 19960138451 | 3/21/1996 | GRANT DEED | PALMER MARY H PALMER WILLIAM SCOTT | surname_only_low_confidence | yes |
| 19960138452 | 3/21/1996 | TRUST DEED | PALMER MARY H PALMER WILLIAM SCOTT | surname_only_low_confidence | yes |
| 19960138463 | 3/21/1996 | ASSIGNMENT RNT | PALMER CHRIS PALMER TAMMALEE TAHNI KING | surname_only_low_confidence | yes |
| 19960138621 | 3/21/1996 | GRANT DEED | PALMER HOWARD M | surname_only_low_confidence | yes |
| 19960138624 | 3/21/1996 | GRANT DEED | PALMER HOWARD M | surname_only_low_confidence | yes |
| 19960142114 | 3/22/1996 | GRANT DEED | PALMER MARK S PALMER SUZANNE C | surname_only_low_confidence | yes |
| 19960144670 | 3/26/1996 | GRANT DEED | PALMER MARY HELEN PALMER RAY WM | surname_only_low_confidence | yes |
| 19960147701 | 3/27/1996 | NOTARY BOND | PALMER PATRICIA MARY | surname_only_low_confidence | no |
| 19960149188 | 3/27/1996 | TRUST DEED | PALMER BEVERLY B TR PALMER RICHARD C TR | surname_only_low_confidence | yes |
| 19960149189 | 3/27/1996 | ASGT TRUST DEED | PALMER BEVERLY B TR PALMER RICHARD C TR | surname_only_low_confidence | yes |
| 19960150557 | 3/28/1996 | RELEASE | PALMER VALERIE A | surname_only_low_confidence | no |
| 19960150559 | 3/28/1996 | RELEASE | PALMER VALERIE A | surname_only_low_confidence | no |
| 19960155446 | 3/29/1996 | GRANT DEED | PALMER HOLLY PALMER P WAYNE | surname_only_low_confidence | yes |
| 19960155447 | 3/29/1996 | TRUST DEED | PALMER HOLLY PALMER P WAYNE | surname_only_low_confidence | yes |
| 19960159541 | 4/2/1996 | ASGT TRUST DEED | PALMER RICHARD A | surname_only_low_confidence | yes |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
