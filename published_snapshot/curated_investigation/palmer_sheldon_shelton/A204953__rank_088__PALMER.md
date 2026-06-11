# Medium-Review Dossier: A204953

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 88
- Fraud-confidence score: 55.72
- Risk signal score: 77.0
- Linkage confidence score: 21.0
- Confidence band: medium_review

## Court Case Context

- Case number: A204953
- Filing date: 2000-11-08
- Case type: LPS CONSERVATORSHIP (WI 5350)
- Related party/caption: PALMER-LPS
- Search lead term: PALMER
- Vulnerability flags: conservatorship | mental_health

## Recorder-Window Signals

- Local recorder matches: 211
- Transfer-like matches: 153
- Exact-name matches: 0
- Distress/lien/default rows: 28
- Distinct matched documents: 211
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A204953__rank_088__PALMER_matches.csv
- Transfer document sample: 20000421564 | 20000427052 | 20000429608 | 20000431671 | 20000431672 | 20000432062 | 20000440278 | 20000441512 | 20000445185 | 20000446285 | 20000449402 | 20000451171 | 20000451522 | 20000452650 | 20000454193 | 20000462684 | 20000463432 | 20000463583 | 20000463716 | 20000465237 | 20000467805 | 20000468842 | 20000471031 | 20000476537 | 20000476611 | 20000476612 | 20000476845 | 20000480226 | 20000480227 | 20000481503 | ... (123 more)
- Distress document sample: 20000415507 | 20000434584 | 20000448082 | 20000466620 | 20000466725 | 20000523338 | 20000528287 | 20000534308 | 20000534309 | 20000535190 | 20000549053 | 20000559221 | 20000566140 | 20000578288 | 20000578437 | 20000601268 | 20000602971 | 20000603477 | 20000665619 | 20000686954 | 20000686956 | 20010005071 | 20010006214 | 20010009898 | 20010023878 | 20010024879 | 20010035865 | 20010059766

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

- GRANT DEED: 44
- TRUST DEED: 42
- RECONVEYANCE: 33
- ASGT TRUST DEED: 24
- ABSTRACT JUDGMT: 14
- RELEASE: 10
- NOTICE OF LIENS: 7
- ASSIGNMENT RNT: 6
- NT DELQNT ASSMT: 3
- REQUEST NOTICE: 3
- NOTICE FED LIEN: 3
- NOTARY BOND: 2

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A204953__rank_088__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 20000415507 | 8/8/2000 | NOTICE OF LIENS | PALMER GARY S | surname_only_low_confidence | no |
| 20000416686 | 8/9/2000 | NOTARY BOND | PALMER GABRIELLA | surname_only_low_confidence | no |
| 20000421564 | 8/11/2000 | GRANT DEED | PALMER BARBARA / PALMER GERALD B | surname_only_low_confidence | yes |
| 20000426004 | 8/15/2000 | NT DELQNT ASSMT | PALMER JAMES RICHARD | surname_only_low_confidence | no |
| 20000427052 | 8/15/2000 | TRUST DEED | PALMER JOHN W A | surname_only_low_confidence | yes |
| 20000429608 | 8/17/2000 | RECONVEYANCE | PALMER MICHAEL | surname_only_low_confidence | yes |
| 20000431671 | 8/18/2000 | GRANT DEED | PALMER DONALD W PALMER YVONNE S | surname_only_low_confidence | yes |
| 20000431672 | 8/18/2000 | TRUST DEED | PALMER DONALD W PALMER YVONNE S | surname_only_low_confidence | yes |
| 20000432062 | 8/18/2000 | RECONVEYANCE | PALMER-SHATZ BRENDA L | surname_only_low_confidence | yes |
| 20000434584 | 8/21/2000 | ABSTRACT JUDGMT | PALMER DAVID KEITH | surname_only_low_confidence | no |
| 20000440278 | 8/23/2000 | RECONVEYANCE | PALMER VICKIE L | surname_only_low_confidence | yes |
| 20000441512 | 8/24/2000 | ASGT TRUST DEED | PALMER CHRISTINE ANN | surname_only_low_confidence | yes |
| 20000445185 | 8/25/2000 | ASGT TRUST DEED | PALMER DAVID PALMER DEBBIE | surname_only_low_confidence | yes |
| 20000446285 | 8/25/2000 | GRANT DEED | PALMER DONALD W JR PALMER YVONNE S | surname_only_low_confidence | yes |
| 20000448082 | 8/28/2000 | ABSTRACT JUDGMT | PALMER-LANDE JENE | surname_only_low_confidence | no |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
