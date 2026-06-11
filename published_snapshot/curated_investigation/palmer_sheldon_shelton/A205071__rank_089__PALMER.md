# Medium-Review Dossier: A205071

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 89
- Fraud-confidence score: 55.72
- Risk signal score: 77.0
- Linkage confidence score: 21.0
- Confidence band: medium_review

## Court Case Context

- Case number: A205071
- Filing date: 2000-11-20
- Case type: CONSERVATORSHIP OF PERSON AND ESTATE
- Related party/caption: PALMER-C
- Search lead term: PALMER
- Vulnerability flags: conservatorship

## Recorder-Window Signals

- Local recorder matches: 215
- Transfer-like matches: 157
- Exact-name matches: 0
- Distress/lien/default rows: 27
- Distinct matched documents: 215
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A205071__rank_089__PALMER_matches.csv
- Transfer document sample: 20000440278 | 20000441512 | 20000445185 | 20000446285 | 20000449402 | 20000451171 | 20000451522 | 20000452650 | 20000454193 | 20000462684 | 20000463432 | 20000463583 | 20000463716 | 20000465237 | 20000467805 | 20000468842 | 20000471031 | 20000476537 | 20000476611 | 20000476612 | 20000476845 | 20000480226 | 20000480227 | 20000481503 | 20000483954 | 20000484944 | 20000490771 | 20000490772 | 20000490920 | 20000497524 | ... (127 more)
- Distress document sample: 20000434584 | 20000448082 | 20000466620 | 20000466725 | 20000523338 | 20000528287 | 20000534308 | 20000534309 | 20000535190 | 20000549053 | 20000559221 | 20000566140 | 20000578288 | 20000578437 | 20000601268 | 20000602971 | 20000603477 | 20000665619 | 20000686954 | 20000686956 | 20010005071 | 20010006214 | 20010009898 | 20010023878 | 20010024879 | 20010035865 | 20010059766

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

- GRANT DEED: 45
- TRUST DEED: 43
- RECONVEYANCE: 32
- ASGT TRUST DEED: 26
- ABSTRACT JUDGMT: 14
- RELEASE: 10
- ASSIGNMENT RNT: 6
- NOTICE OF LIENS: 6
- REQUEST NOTICE: 3
- NOTICE FED LIEN: 3
- QUITCLAIM DEED: 3
- NOTICE REMOVAL: 2

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A205071__rank_089__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 20000434584 | 8/21/2000 | ABSTRACT JUDGMT | PALMER DAVID KEITH | surname_only_low_confidence | no |
| 20000440278 | 8/23/2000 | RECONVEYANCE | PALMER VICKIE L | surname_only_low_confidence | yes |
| 20000441512 | 8/24/2000 | ASGT TRUST DEED | PALMER CHRISTINE ANN | surname_only_low_confidence | yes |
| 20000445185 | 8/25/2000 | ASGT TRUST DEED | PALMER DAVID PALMER DEBBIE | surname_only_low_confidence | yes |
| 20000446285 | 8/25/2000 | GRANT DEED | PALMER DONALD W JR PALMER YVONNE S | surname_only_low_confidence | yes |
| 20000448082 | 8/28/2000 | ABSTRACT JUDGMT | PALMER-LANDE JENE | surname_only_low_confidence | no |
| 20000449402 | 8/29/2000 | TRUST DEED | PALMER MATTHEW | surname_only_low_confidence | yes |
| 20000449403 | 8/29/2000 | REQUEST NOTICE | PALMER MATTHEW | surname_only_low_confidence | no |
| 20000451171 | 8/29/2000 | ASSIGNMENT RNT | PALMER FRANK TR PALMER MARIA E TR | surname_only_low_confidence | yes |
| 20000451522 | 8/29/2000 | GRANT DEED | PALMER DAVID E TR PALMER PATRICIA A TR | surname_only_low_confidence | yes |
| 20000452650 | 8/30/2000 | GRANT DEED | PALMER DOUGLAS L PALMER RITA L | surname_only_low_confidence | yes |
| 20000454193 | 8/30/2000 | ASGT TRUST DEED | PALMER SHERI P | surname_only_low_confidence | yes |
| 20000462151 | 9/5/2000 | RELEASE | PALMER KARLYN A PALMER VAL M | surname_only_low_confidence | no |
| 20000462684 | 9/5/2000 | RECONVEYANCE | PALMER JOHN | surname_only_low_confidence | yes |
| 20000463432 | 9/5/2000 | ASGT TRUST DEED | PALMER JAMES R | surname_only_low_confidence | yes |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
