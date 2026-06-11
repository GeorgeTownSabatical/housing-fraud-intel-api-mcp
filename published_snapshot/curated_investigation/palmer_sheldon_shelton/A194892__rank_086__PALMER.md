# Medium-Review Dossier: A194892

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 86
- Fraud-confidence score: 55.72
- Risk signal score: 77.0
- Linkage confidence score: 21.0
- Confidence band: medium_review

## Court Case Context

- Case number: A194892
- Filing date: 1998-11-20
- Case type: GUARDIANSHIP OF PERSON AND ESTATE
- Related party/caption: PALMER-M
- Search lead term: PALMER
- Vulnerability flags: guardianship

## Recorder-Window Signals

- Local recorder matches: 241
- Transfer-like matches: 158
- Exact-name matches: 0
- Distress/lien/default rows: 32
- Distinct matched documents: 241
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A194892__rank_086__PALMER_matches.csv
- Transfer document sample: 19980551286 | 19980558523 | 19980563031 | 19980563356 | 19980568010 | 19980581178 | 19980581179 | 19980585107 | 19980585109 | 19980585110 | 19980585111 | 19980587378 | 19980588035 | 19980589356 | 19980598326 | 19980599077 | 19980600240 | 19980600759 | 19980600761 | 19980600763 | 19980607359 | 19980607696 | 19980607697 | 19980610188 | 19980611666 | 19980612898 | 19980628586 | 19980628587 | 19980629841 | 19980629842 | ... (128 more)
- Distress document sample: 19980555590 | 19980583487 | 19980648336 | 19980657438 | 19980667533 | 19980673157 | 19980673521 | 19980678355 | 19980678666 | 19980692641 | 19980728819 | 19980729846 | 19980746422 | 19980747898 | 19980780912 | 19980788395 | 19980788396 | 19980788397 | 19980797596 | 19980813842 | 19980855782 | 19980862127 | 19980891696 | 19990003157 | 19990035894 | 19990043017 | 19990053886 | 19990074678 | 19990093113 | 19990098049 | ... (2 more)

## Risk Factors

- vulnerable_population_case
- nearby_transfer_like_activity
- nearby_distress_lien_default_activity
- dense_recorder_activity
- guardianship_or_minor_context
- case_specific_surname_context

## Cautions

- high_name_collision
- surname_or_caption_only_linkage

## User-Provided Context

- No user-provided actor context matched this lead.

## Document-Type Mix

- TRUST DEED: 45
- RECONVEYANCE: 44
- RELEASE: 31
- GRANT DEED: 29
- ASGT TRUST DEED: 25
- ABSTRACT JUDGMT: 12
- LIEN STATE: 11
- QUITCLAIM DEED: 8
- SUBDN AGREEMENT: 4
- ASSIGNMENT RNT: 4
- NOTICE DEFAULT: 4
- NT DELQNT ASSMT: 3

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A194892__rank_086__PALMER_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 19980551286 | 8/21/1998 | RECONVEYANCE | PALMER CLARENCE E PALMER JOY I | surname_only_low_confidence | yes |
| 19980555590 | 8/24/1998 | ABSTRACT JUDGMT | PALMER ROSS SHARON | surname_only_low_confidence | no |
| 19980558523 | 8/25/1998 | TRUST DEED | PALMER DEANE S PALMER VICKI A | surname_only_low_confidence | yes |
| 19980563031 | 8/26/1998 | RECONVEYANCE | PALMER EILEEN L PALMER JOSEPH C | surname_only_low_confidence | yes |
| 19980563356 | 8/26/1998 | QUITCLAIM DEED | PALMER PERRY A | surname_only_low_confidence | yes |
| 19980568010 | 8/27/1998 | RECONVEYANCE | PALMER ALVA C TR | surname_only_low_confidence | yes |
| 19980574511 | 8/28/1998 | RELEASE | PALMER WILLIAM W | surname_only_low_confidence | no |
| 19980581178 | 8/31/1998 | QUITCLAIM DEED | PALMER PETER L / PALMER VALERIE M | surname_only_low_confidence | yes |
| 19980581179 | 8/31/1998 | TRUST DEED | PALMER VALERIE M | surname_only_low_confidence | yes |
| 19980583487 | 9/1/1998 | LIEN STATE | PALMER T M | surname_only_low_confidence | no |
| 19980585107 | 9/1/1998 | GRANT DEED | PALMER MATTHEW | surname_only_low_confidence | yes |
| 19980585109 | 9/1/1998 | QUITCLAIM DEED | PALMER MATTHEW / PALMER TAMARA JEAN | surname_only_low_confidence | yes |
| 19980585110 | 9/1/1998 | TRUST DEED | PALMER MATTHEW | surname_only_low_confidence | yes |
| 19980585111 | 9/1/1998 | TRUST DEED | PALMER MATTHEW | surname_only_low_confidence | yes |
| 19980586501 | 9/2/1998 | MODIFICATION | PALMER CARI FRANZEL | surname_only_low_confidence | no |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
