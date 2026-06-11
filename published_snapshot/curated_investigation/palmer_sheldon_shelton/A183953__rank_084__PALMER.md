# Medium-Review Dossier: A183953

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 84
- Fraud-confidence score: 55.72
- Risk signal score: 77.0
- Linkage confidence score: 21.0
- Confidence band: medium_review

## Court Case Context

- Case number: A183953
- Filing date: 1996-08-14
- Case type: LPS CONSERVATORSHIP (WI 5350)
- Related party/caption: PALMER-C
- Search lead term: PALMER
- Vulnerability flags: conservatorship | mental_health

## Recorder-Window Signals

- Local recorder matches: 194
- Transfer-like matches: 132
- Exact-name matches: 0
- Distress/lien/default rows: 31
- Distinct matched documents: 194
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A183953__rank_084__PALMER_matches.csv
- Transfer document sample: 19960242509 | 19960242510 | 19960242527 | 19960250219 | 19960250220 | 19960250221 | 19960250781 | 19960257185 | 19960257186 | 19960257187 | 19960262524 | 19960263846 | 19960267252 | 19960267302 | 19960269522 | 19960272322 | 19960274500 | 19960275020 | 19960275021 | 19960276128 | 19960279766 | 19960280606 | 19960284570 | 19960291252 | 19960292401 | 19960296050 | 19960298538 | 19960298635 | 19960301289 | 19960306280 | ... (102 more)
- Distress document sample: 19960242573 | 19960251340 | 19960258357 | 19960276033 | 19960285615 | 19960289845 | 19960294477 | 19960302778 | 19960303564 | 19960332755 | 19960341997 | 19960357787 | 19960358413 | 19960362804 | 19960385230 | 19960408321 | 19960409674 | 19960410872 | 19960424702 | 19960448671 | 19960477076 | 19960489398 | 19960499025 | 19960504743 | 19960515388 | 19960516988 | 19960547961 | 19960548123 | 19960564182 | 19960566654 | ... (1 more)

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

- RECONVEYANCE: 30
- GRANT DEED: 29
- ASGT TRUST DEED: 23
- TRUST DEED: 23
- RELEASE: 12
- LIEN STATE: 11
- QUITCLAIM DEED: 9
- ASSIGNMENT RNT: 9
- ABSTRACT JUDGMT: 7
- NOTICE FED LIEN: 7
- TRUSTEES DEED: 6
- POWER ATTORNEY: 3

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A183953__rank_084__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 19960242509 | 5/15/1996 | ASGT TRUST DEED | PALMER CAROL L | surname_only_low_confidence | yes |
| 19960242510 | 5/15/1996 | ASGT TRUST DEED | PALMER JOHN DONOHUE PALMER PATRICIA DIANE | surname_only_low_confidence | yes |
| 19960242527 | 5/15/1996 | RECONVEYANCE | PALMER JUDY A PALMER KENNETH LLOYD | surname_only_low_confidence | yes |
| 19960242573 | 5/15/1996 | LIEN STATE | PALMER PAMELA | surname_only_low_confidence | no |
| 19960245961 | 5/16/1996 | RELEASE | PALMER RICHARD | surname_only_low_confidence | no |
| 19960250219 | 5/17/1996 | QUITCLAIM DEED | PALMER PEGGY / PALMER SAMUEL | surname_only_low_confidence | yes |
| 19960250220 | 5/17/1996 | GRANT DEED | PALMER PEGGY | surname_only_low_confidence | yes |
| 19960250221 | 5/17/1996 | TRUST DEED | PALMER PEGGY | surname_only_low_confidence | yes |
| 19960250781 | 5/20/1996 | RECONVEYANCE | PALMER ESTHER L PALMER LAWRENCE L | surname_only_low_confidence | yes |
| 19960251299 | 5/20/1996 | POWER ATTORNEY | PALMER BARBARA A | surname_only_low_confidence | no |
| 19960251340 | 5/20/1996 | ABSTRACT JUDGMT | PALMER JERRY W | surname_only_low_confidence | no |
| 19960257185 | 5/22/1996 | GRANT DEED | PALMER A JOYCE | surname_only_low_confidence | yes |
| 19960257186 | 5/22/1996 | GRANT DEED | PALMER A JOYCE | surname_only_low_confidence | yes |
| 19960257187 | 5/22/1996 | ASSIGNMENT RNT | PALMER A JOYCE BFC | surname_only_low_confidence | yes |
| 19960258357 | 5/23/1996 | NOTICE FED LIEN | PALMER NANCY J | surname_only_low_confidence | no |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
