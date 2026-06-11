# Medium-Review Dossier: A202011

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 87
- Fraud-confidence score: 55.72
- Risk signal score: 77.0
- Linkage confidence score: 21.0
- Confidence band: medium_review

## Court Case Context

- Case number: A202011
- Filing date: 2000-04-19
- Case type: LPS CONSERVATORSHIP (WI 5350)
- Related party/caption: PALMER-LPS
- Search lead term: PALMER
- Vulnerability flags: conservatorship | mental_health

## Recorder-Window Signals

- Local recorder matches: 204
- Transfer-like matches: 144
- Exact-name matches: 0
- Distress/lien/default rows: 20
- Distinct matched documents: 204
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A202011__rank_087__PALMER_matches.csv
- Transfer document sample: 20000030930 | 20000030931 | 20000030932 | 20000030933 | 20000034621 | 20000039013 | 20000042484 | 20000044206 | 20000044734 | 20000044735 | 20000045553 | 20000050735 | 20000053079 | 20000054609 | 20000066358 | 20000066579 | 20000068587 | 20000069321 | 20000069322 | 20000070809 | 20000071087 | 20000071088 | 20000072384 | 20000073043 | 20000076026 | 20000078549 | 20000078579 | 20000078580 | 20000078581 | 20000083550 | ... (114 more)
- Distress document sample: 20000033679 | 20000071780 | 20000092886 | 20000116506 | 20000123549 | 20000156819 | 20000193549 | 20000207276 | 20000238178 | 20000253810 | 20000262454 | 20000272981 | 20000278416 | 20000286391 | 20000286392 | 20000320026 | 20000328193 | 20000356387 | 20000357592 | 20000380242

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

- GRANT DEED: 33
- TRUST DEED: 32
- RECONVEYANCE: 31
- ASGT TRUST DEED: 30
- RELEASE: 26
- ABSTRACT JUDGMT: 17
- QUITCLAIM DEED: 10
- NOTARY BOND: 3
- ASSIGNMENT RNT: 3
- ASSIGNMENT: 2
- NT INTEND TRANS: 2
- NT TO CREDITORS: 2

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A202011__rank_087__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 20000030930 | 1/18/2000 | GRANT DEED | PALMER JAMES M | surname_only_low_confidence | yes |
| 20000030931 | 1/18/2000 | DEED | PALMER JAMES M / PALMER SHANNON | surname_only_low_confidence | yes |
| 20000030932 | 1/18/2000 | TRUST DEED | PALMER JAMES M | surname_only_low_confidence | yes |
| 20000030933 | 1/18/2000 | ASGT TRUST DEED | PALMER JAMES M | surname_only_low_confidence | yes |
| 20000031345 | 1/18/2000 | RELEASE | PALMER GREGORY PAUL PALMER KIMBERLY ANN | surname_only_low_confidence | no |
| 20000033679 | 1/19/2000 | ABSTRACT JUDGMT | PALMER RUSTY RAY | surname_only_low_confidence | no |
| 20000034621 | 1/19/2000 | GRANT DEED | PALMER BETHENE | surname_only_low_confidence | yes |
| 20000039013 | 1/21/2000 | ASSIGNMENT | PALMER PATTI L | surname_only_low_confidence | yes |
| 20000040869 | 1/24/2000 | RELEASE | PALMER NICOLL | surname_only_low_confidence | no |
| 20000041487 | 1/24/2000 | RELEASE | PALMER CHERYL A PALMER PAUL E | surname_only_low_confidence | no |
| 20000042484 | 1/25/2000 | ASGT TRUST DEED | PALMER JANICE L PALMER SCOTT G | surname_only_low_confidence | yes |
| 20000044206 | 1/25/2000 | ASGT TRUST DEED | PALMER DENZIL F PALMER IRENE L | surname_only_low_confidence | yes |
| 20000044734 | 1/26/2000 | GRANT DEED | PALMER DARREN PALMER DEANNA / PALMER DEANNA ZITNIK DEANNA | surname_only_low_confidence | yes |
| 20000044735 | 1/26/2000 | TRUST DEED | PALMER DARREN PALMER DEANNA | surname_only_low_confidence | yes |
| 20000045553 | 1/26/2000 | RECONVEYANCE | PALMER WILLIAM L JR | surname_only_low_confidence | yes |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
