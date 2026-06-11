# Medium-Review Dossier: A171502

## Status

- Finding status: triage lead only; not a fraud finding, title opinion, or identity determination.
- Medium-review rank: 2
- Fraud-confidence score: 61.8
- Risk signal score: 77.0
- Linkage confidence score: 37.0
- Confidence band: medium_review

## Court Case Context

- Case number: A171502
- Filing date: 1994-01-05
- Case type: GUARDIANSHIP OF PERSON ONLY
- Related party/caption: SHELDON-MINOR
- Search lead term: SHELDON
- Vulnerability flags: guardianship

## Recorder-Window Signals

- Local recorder matches: 73
- Transfer-like matches: 48
- Exact-name matches: 0
- Distress/lien/default rows: 13
- Distinct matched documents: 73
- Full match CSV: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A171502__rank_002__SHELDON_matches.csv
- Transfer document sample: 19930683468 | 19930698669 | 19930729819 | 19930742048 | 19930758031 | 19930760783 | 19930760933 | 19930760934 | 19930764757 | 19930768689 | 19930781443 | 19930795737 | 19930817236 | 19930850861 | 19930865616 | 19930903807 | 19930914351 | 19930914352 | 19940009510 | 19940032513 | 19940032514 | 19940051936 | 19940067669 | 19940094163 | 19940094164 | 19940108007 | 19940156521 | 19940189568 | 19940195273 | 19940200036 | ... (18 more)
- Distress document sample: 19930688453 | 19930697322 | 19930700572 | 19930743019 | 19930771016 | 19930796008 | 19930848403 | 19940089312 | 19940101661 | 19940108715 | 19940134510 | 19940174148 | 19940208728

## Risk Factors

- vulnerable_population_case
- nearby_transfer_like_activity
- nearby_distress_lien_default_activity
- dense_recorder_activity
- guardianship_or_minor_context
- case_specific_surname_context

## Cautions

- surname_or_caption_only_linkage

## User-Provided Context

These notes are user-provided context for investigation routing; they are not independently verified by the local public-record corpus.

- Actor/name: SHELDON
- Role/description: Tustin psychologist
- Related matter: User psych ward release context
- Note: User states Sheldon was the Tustin psychologist who was scared when the user was released from the psych ward.
- Verification status: user_provided_unverified


## Document-Type Mix

- ASGT TRUST DEED: 20
- TRUST DEED: 10
- RECONVEYANCE: 9
- ABSTRACT JUDGMT: 6
- GRANT DEED: 5
- POWER ATTORNEY: 4
- NOTICE FED LIEN: 3
- ASSIGNMENT RNT: 3
- DELINQUENT CTF: 2
- NOTICE: 2
- NOTICE DEFAULT: 1
- TRUSTEES DEED: 1

## Matched Recorder Rows

Full match table: /Users/ALISTAIRE/housing-fraud-intel-api/exports/medium_review_dossiers/matches/A171502__rank_002__SHELDON_matches.csv

Sample rows are shown below for readability.

| document_number | recording_date | document_type | party_names | match_rules | transfer |
|---|---:|---|---|---|---|
| 19930676570 | 10/5/1993 | POWER ATTORNEY | SHELDON ANNE | surname_only_low_confidence | no |
| 19930683468 | 10/7/1993 | RECONVEYANCE | SHELDON GARY W SHELDON VIOLET S | surname_only_low_confidence | yes |
| 19930688453 | 10/8/1993 | NOTICE DEFAULT | SHELDON FREDERICK A 93-0527091 9-6-93 SHELDON SUSAN B 93-0527091 9-6-93 | surname_only_low_confidence | no |
| 19930697322 | 10/14/1993 | ABSTRACT JUDGMT | SHELDON HARVEY | surname_only_low_confidence | no |
| 19930698669 | 10/14/1993 | TRUSTEES DEED | SHELDON FREDERICK A SHELDON SUSAN B | surname_only_low_confidence | yes |
| 19930700572 | 10/15/1993 | ABSTRACT JUDGMT | SHELDON NEIL | surname_only_low_confidence | no |
| 19930729819 | 10/26/1993 | RECONVEYANCE | SHELDON ANITA C SHELDON CHERI R SHELDON MICHAEL A SHELDON MICHAEL D | surname_only_low_confidence | yes |
| 19930742048 | 10/29/1993 | TRUST DEED | SHELDON MICHAEL B | surname_only_low_confidence | yes |
| 19930743019 | 10/29/1993 | NOTICE FED LIEN | SHELDON DEBBIE K SHELDON DENNIS L | surname_only_low_confidence | no |
| 19930758031 | 11/4/1993 | GRANT DEED | SHELDON DENISE L SHELDON ROBERT G | surname_only_low_confidence | yes |
| 19930760783 | 11/5/1993 | RECONVEYANCE | SHELDON MICHAEL J SHELDON RENEE I | surname_only_low_confidence | yes |
| 19930760933 | 11/5/1993 | GRANT DEED | SHELDON DENISE L SHELDON ROBERT G | surname_only_low_confidence | yes |
| 19930760934 | 11/5/1993 | TRUST DEED | SHELDON DENISE L SHELDON ROBERT G | surname_only_low_confidence | yes |
| 19930764757 | 11/5/1993 | RECONVEYANCE | SHELDON PHYLLIS SHELDON TERRY | surname_only_low_confidence | yes |
| 19930768689 | 11/8/1993 | RECONVEYANCE | SHELDON MICHAEL K TR | surname_only_low_confidence | yes |

## Recommended Verification

- Pull document images for the sampled transfer-like and distress/lien/default instruments.
- Confirm whether the matched party is the same person/entity as the court-caption subject.
- Check whether court orders, conservatorship/guardianship authority, or estate authority existed before each transfer-like document.
- Separate institutional parties from individual actors before drawing any inference.
- If document images show APNs, join them to the OC parcel layer and build parcel-specific chronology.
