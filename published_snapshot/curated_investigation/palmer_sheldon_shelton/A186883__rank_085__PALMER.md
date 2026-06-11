# Medium-Review Dossier: A186883

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 85
- Fraud-confidence score: 55.72
- Risk signal score: 77.0
- Linkage confidence score: 21.0
- Confidence band: medium_review

## Court Case Context

- Case number: A186883
- Filing date: 1997-04-02
- Case type: LPS CONSERVATORSHIP (WI 5350)
- Related party/caption: PALMER-C
- Search lead term: PALMER
- Vulnerability flags: conservatorship | mental_health

## Recorder-Window Signals

- Local recorder matches: 178
- Transfer-like matches: 118
- Exact-name matches: 0
- Distress/lien/default rows: 29
- Distinct matched documents: 178
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A186883__rank_085__PALMER_matches.csv
- Transfer document sample: 19960657597 | 19970003061 | 19970004897 | 19970010607 | 19970020387 | 19970025166 | 19970027189 | 19970030113 | 19970031928 | 19970033830 | 19970033850 | 19970035896 | 19970037244 | 19970044461 | 19970047443 | 19970053178 | 19970055336 | 19970060421 | 19970064113 | 19970065775 | 19970070430 | 19970070829 | 19970070830 | 19970072853 | 19970080997 | 19970080998 | 19970082907 | 19970082908 | 19970089652 | 19970089653 | ... (88 more)
- Distress document sample: 19970011291 | 19970040819 | 19970071597 | 19970099441 | 19970101541 | 19970103964 | 19970120337 | 19970126224 | 19970129884 | 19970129885 | 19970133894 | 19970158066 | 19970161414 | 19970164400 | 19970164962 | 19970178691 | 19970179585 | 19970209134 | 19970211660 | 19970211661 | 19970212411 | 19970219340 | 19970233246 | 19970263598 | 19970266155 | 19970277018 | 19970281138 | 19970292507 | 19970302412

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

- GRANT DEED: 31
- ASGT TRUST DEED: 28
- TRUST DEED: 25
- RECONVEYANCE: 21
- RELEASE: 15
- ABSTRACT JUDGMT: 9
- LIEN STATE: 7
- NOTICE FED LIEN: 6
- QUITCLAIM DEED: 5
- ASSIGNMENT RNT: 5
- REQUEST NOTICE: 4
- NT DELQNT ASSMT: 3

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A186883__rank_085__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 19960657597 | 12/31/1996 | GRANT DEED | PALMER CAROLE J PALMER WILLIAM D | surname_only_low_confidence | yes |
| 19960657750 | 12/31/1996 | DECLN HOMESTEAD | PALMER KARLYN A PALMER VAL W | surname_only_low_confidence | no |
| 19970003061 | 1/3/1997 | ASGT TRUST DEED | PALMER ROBERT A PALMER SHERRY D | surname_only_low_confidence | yes |
| 19970004878 | 1/6/1997 | RELEASE | PALMER GLEN C | surname_only_low_confidence | no |
| 19970004897 | 1/6/1997 | ASGT TRUST DEED | PALMER DAVID C | surname_only_low_confidence | yes |
| 19970010607 | 1/8/1997 | RECONVEYANCE | PALMER KENNETH M PALMER MARY M | surname_only_low_confidence | yes |
| 19970011291 | 1/8/1997 | DELINQUENT CTF | PALMER THOM | surname_only_low_confidence | no |
| 19970012385 | 1/9/1997 | DECLN HOMESTEAD | PALMER LISA PALMER MICHAEL P | surname_only_low_confidence | no |
| 19970012386 | 1/9/1997 | NT COMPLETION | PALMER LISA PALMER MICHAEL | surname_only_low_confidence | no |
| 19970020387 | 1/14/1997 | GRANT DEED | PALMER SHAWNA | surname_only_low_confidence | yes |
| 19970025166 | 1/16/1997 | ASGT TRUST DEED | PALMER BERTRAND PALMER JUDITH | surname_only_low_confidence | yes |
| 19970027189 | 1/17/1997 | TRUST DEED | PALMER MARIETTA S PALMER RONALD L | surname_only_low_confidence | yes |
| 19970027549 | 1/17/1997 | RELEASE | PALMER CRAIG B PALMER LYNN M | surname_only_low_confidence | no |
| 19970030113 | 1/21/1997 | GRANT DEED | PALMER JAMES | surname_only_low_confidence | yes |
| 19970031652 | 1/22/1997 | RELEASE | PALMER JEFFREY PALMER JUDITH | surname_only_low_confidence | no |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
