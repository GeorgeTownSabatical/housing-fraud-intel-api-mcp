# Full Current Investigation Packet

Orange County probate / RecorderWorks / criminal-attorney / identity-graph triage exports

Generated UTC: 2026-06-11T06:35:41Z
Boundary: this packet is investigative triage only. It is not a fraud finding, not an identity determination, not a title opinion, not legal advice, and not a claim that any named person committed misconduct.
Purpose: provide a single uploadable PDF snapshot of the current local evidence state, high/medium leads, known coverage gaps, and next verification steps.

## Executive Metrics

- Scored fraud-risk leads: 1074
- Band counts: {'high_review': 1, 'medium_review': 178, 'low_review': 895}
- High/medium review leads: 179
- Court/probate rows processed in recorder-window packet: 127885
- Cases with local recorder matches: 1187
- Vulnerable cases in case universe: 38128
- Vulnerable cases with local recorder matches: 391
- Local match rows: 56220
- Identity graph: 32239 nodes, 113268 edges
- Connection paths: 4322 ranked paths; 1695 focus multi-hop paths

## Current Coverage Caveat

The 171 PDF is dominated by 1993/1994 because local recorder correlation signals are populated almost entirely for 1994-2001, with no 2002+ local recorder signal rows in the current packet.
Populate/merge RecorderWorks name cross-reference results for 2002+ years, then rebuild fraud_confidence_scores and regenerate a year-balanced dossier packet.

### Year Counts In Current Scores

- 1994: 799 scored rows
- 1995: 44 scored rows
- 1996: 21 scored rows
- 1997: 25 scored rows
- 1998: 25 scored rows
- 1999: 8 scored rows
- 2000: 16 scored rows
- 2001: 17 scored rows
- 2002: 119 scored rows

### Backfill State

- Backfill target years: 2002 to 2010
- Completed batches: 3
- Missing batches: 3081
- Next batches: [2205, 2206, 2207, 2208, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217]
- Clean completed batches observed in this run: 2209, 2204, 2203.
- Batch 2205 was interrupted/slow and should be checked before retrying.

## Scoring Method

0-100 triage score, not a fraud finding
0.62 * risk_signal_score + 0.38 * linkage_confidence_score, with caps for collision-prone surname-only matches

### Positive Factors

- vulnerable population case type
- transfer-like recorder activity near filing
- distress/lien/default-like recorder activity near filing
- exact-name overlap
- low-collision transfer window
- case-specific surname context

### Penalties / Cautions

- high or very high surname/name collision, retained as a caution rather than a hard suppressor because surnames are case-specific
- surname-only linkage where no vulnerable context is present
- no transfer or distress signal

### Observed Risk Factor Counts

- nearby_transfer_like_activity: 1043
- case_specific_surname_context: 1043
- low_collision_transfer_window: 794
- nearby_distress_lien_default_activity: 418
- vulnerable_population_case: 373
- conservatorship_context: 282
- dense_recorder_activity: 119
- guardianship_or_minor_context: 91
- exact_name_overlap: 5

### Observed Caution Counts

- surname_or_caption_only_linkage: 1039
- high_name_collision: 84
- very_high_name_collision: 25
- no_transfer_or_distress_signal: 1

## Top Leads

**001. A171585 | 79.9 | high_review | 1994-01-11 | LPS CONSERVATORSHIP (WI 5350) | HARRIS-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | exact_name_overlap | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: very_high_name_collision
**002. A172078 | 62.05 | medium_review | 1994-02-24 | GUARDIANSHIP OF PERSON ONLY | FELTON-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**003. A171502 | 61.8 | medium_review | 1994-01-05 | GUARDIANSHIP OF PERSON ONLY | SHELDON-MINOR**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**004. A171711 | 61.8 | medium_review | 1994-01-21 | CONSERVATORSHIP OF PERSON ONLY | CUEVAS-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**005. A172023 | 61.8 | medium_review | 1994-02-18 | LPS CONSERVATORSHIP (WI 5350) | RHEE-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**006. A172377 | 61.8 | medium_review | 1994-03-16 | LIMITED CONSERVATORSHIP OF PERSON ONLY | CARLTON-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**007. A172659 | 61.8 | medium_review | 1994-04-01 | GUARDIANSHIP OF PERSON ONLY | MICHEL-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**008. A172675 | 61.8 | medium_review | 1994-04-01 | CONSERVATORSHIP OF PERSON AND ESTATE | MATTSON-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**009. A172761 | 61.8 | medium_review | 1994-04-07 | LPS CONSERVATORSHIP (WI 5350) | RHODES-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**010. A173379 | 61.8 | medium_review | 1994-05-20 | GUARDIANSHIP OF PERSON ONLY | BOYD-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**011. A171523 | 61.62 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | LEE-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**012. A171869 | 61.62 | medium_review | 1994-02-07 | GUARDIANSHIP OF PERSON AND ESTATE | JEWETT-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**013. A171610 | 61.55 | medium_review | 1994-01-12 | CONSERVATORSHIP OF PERSON AND ESTATE | MADDOX-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**014. A172308 | 61.55 | medium_review | 1994-03-10 | CONSERVATORSHIP OF PERSON AND ESTATE | PRATT-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**015. A172370 | 60.87 | medium_review | 1994-03-15 | GUARDIANSHIP OF ESTATE ONLY | WEST-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**016. A172539 | 60.87 | medium_review | 1994-03-25 | LPS CONSERVATORSHIP (WI 5350) | LEE-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**017. A172671 | 60.87 | medium_review | 1994-04-01 | LPS CONSERVATORSHIP (WI 5350) | BURKHARDT-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**018. A172979 | 60.87 | medium_review | 1994-04-21 | CONSERVATORSHIP OF ESTATE ONLY | HURD-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**019. A171857 | 60.81 | medium_review | 1994-02-03 | LPS CONSERVATORSHIP (WI 5350) | ASHLEY-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**020. A172631 | 60.81 | medium_review | 1994-03-31 | LPS CONSERVATORSHIP (WI 5350) | CARRANZA-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**021. A173520 | 60.81 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | NORRIS-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**022. A172509 | 60.13 | medium_review | 1994-03-23 | LIMITED CONSERVATORSHIP OF PERSON ONLY | NIEVES-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**023. A172552 | 60.13 | medium_review | 1994-03-25 | GUARDIANSHIP OF PERSON ONLY | SABO-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**024. A172678 | 60.13 | medium_review | 1994-04-04 | GUARDIANSHIP OF ESTATE ONLY | HERNDON-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**025. A174101 | 60.13 | medium_review | 1994-07-15 | GUARDIANSHIP OF ESTATE ONLY | SMITH-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**026. A172567 | 60.06 | medium_review | 1994-03-28 | LPS CONSERVATORSHIP (WI 5350) | JOHNS-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**027. A172582 | 60.06 | medium_review | 1994-03-29 | GUARDIANSHIP OF PERSON AND ESTATE | JOHNS-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
**028. A182843 | 59.72 | medium_review | 1996-05-28 | PROBATE OF WILL - LETTERS TESTAMENTARY | PALMER-D**
Risk: nearby_transfer_like_activity | nearby_distress_lien_default_activity | exact_name_overlap | case_specific_surname_context
Cautions: high_name_collision
**029. A171803 | 59.38 | medium_review | 1994-01-31 | LIMITED CONSERVATORSHIP OF PERSON ONLY | WILLIAMS-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**030. A172483 | 59.38 | medium_review | 1994-03-22 | CONSERVATORSHIP OF PERSON AND ESTATE | VAN DYKE-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**031. A173074 | 59.38 | medium_review | 1994-04-27 | LPS CONSERVATORSHIP (WI 5350) | KIM-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**032. A173504 | 59.38 | medium_review | 1994-06-02 | CONSERVATORSHIP OF PERSON AND ESTATE | DE SOTO-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**033. A173916 | 59.38 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | MC VICAR-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**034. A175806 | 59.38 | medium_review | 1994-11-29 | CONSERVATORSHIP OF PERSON AND ESTATE | O'DELL-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**035. A175904 | 59.38 | medium_review | 1994-12-06 | LIMITED CONSERVATORSHIP OF PERSON ONLY | O'BITZ-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage

## Palmer Focus

PALMER rows in current scored export: 13. Current Palmer cases: A182843, A183184, A183953, A186883, A194892, A202011, A204953, A205071, A213042, A179959, A189182, A207103, A214089.
**A182843 | score 59.72 | medium_review | 1996-05-28 | PROBATE OF WILL - LETTERS TESTAMENTARY | PALMER-D**
Risk: nearby_transfer_like_activity | nearby_distress_lien_default_activity | exact_name_overlap | case_specific_surname_context
Cautions: high_name_collision
**A183184 | score 55.72 | medium_review | 1996-06-21 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A183953 | score 55.72 | medium_review | 1996-08-14 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A186883 | score 55.72 | medium_review | 1997-04-02 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A194892 | score 55.72 | medium_review | 1998-11-20 | GUARDIANSHIP OF PERSON AND ESTATE | PALMER-M**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A202011 | score 55.72 | medium_review | 2000-04-19 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A204953 | score 55.72 | medium_review | 2000-11-08 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A205071 | score 55.72 | medium_review | 2000-11-20 | CONSERVATORSHIP OF PERSON AND ESTATE | PALMER-C**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | conservatorship_context | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A213042 | score 42.21 | low_review | 2002-04-19 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS**
Risk: vulnerable_population_case | nearby_transfer_like_activity | conservatorship_context | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage
**A179959 | score 34.02 | low_review | 1995-10-13 | DETERMINE SUCCESSION TO PRIMARY RESIDENCE IN CALIFORNIA | PALMER-D**
Risk: nearby_transfer_like_activity | nearby_distress_lien_default_activity | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A189182 | score 34.02 | low_review | 1997-09-19 | PROBATE OF WILL - LETTERS TESTAMENTARY | PALMER-D**
Risk: nearby_transfer_like_activity | nearby_distress_lien_default_activity | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A207103 | score 34.02 | low_review | 2001-04-04 | PROBATE OF WILL - LETTERS TESTAMENTARY | PALMER-D**
Risk: nearby_transfer_like_activity | nearby_distress_lien_default_activity | case_specific_surname_context
Cautions: high_name_collision | surname_or_caption_only_linkage
**A214089 | score 25.47 | low_review | 2002-06-26 | PROBATE OF WILL - LETTERS TESTAMENTARY | PALMER-D**
Risk: nearby_transfer_like_activity | case_specific_surname_context | low_collision_transfer_window
Cautions: surname_or_caption_only_linkage

### Palmer Recorder / Property Anchors

`19970343965 | 7/21/1997 | GRANT DEED | ASTOR CYNTHIA S ASTOR JAMES W -> PALMER JAMES E III PALMER MICHELLE L`
`19970410943 | 8/25/1997 | GRANT DEED | ASTOR CYNTHIA S ASTOR JAMES W -> PALMER JAMES E III PALMER MICHELLE L`
`19960410872 | 8/12/1996 | NOTICE FED LIEN | PALMER JAMES E -> U S A INT REV`
`19970254357 | 6/3/1997 | QUITCLAIM DEED | PALMER JAMES E III -> CLARK ELIZABETH N / MANUEL W`
Public-context Jim Palmer / OCRM / Hurtt links are retained as public-context anchors only, not allegations and not proof of a case connection.

## Sheldon / Shelton Focus

SHELDON rows in current scored export: 1. SHELTON rows found in targeted score export: 0.
**A171502 | score 61.8 | medium_review | 1994-01-05 | GUARDIANSHIP OF PERSON ONLY | SHELDON-MINOR**
Risk: vulnerable_population_case | nearby_transfer_like_activity | nearby_distress_lien_default_activity | dense_recorder_activity | guardianship_or_minor_context | case_specific_surname_context
Cautions: surname_or_caption_only_linkage
User-provided context identifies Sheldon as a Tustin psychologist connected to a psych-ward release context. That is preserved as routing context only and is not independently verified by this public-record corpus.
`19940019918 | 1/10/1994 | POWER ATTORNEY | SHELDON-window row`
`19940032513 | 1/14/1994 | GRANT DEED | SHELDON-window row`
`19940032514 | 1/14/1994 | TRUST DEED | SHELDON-window row`
`19940051936 | 1/21/1994 | ASGT TRUST DEED | SHELDON-window row`
`19940067669 | 1/28/1994 | ASSIGNMENT RNT | SHELDON-window row`

## OCRM / Hurtt Bridge

- OCRM rows: 2
- OCRM docnums: ['2008000012688', '2008000360614']
- Bridge rows: 318
- Hurtt local recorder rows: 3
- Exact overlaps to base identity graph: 0
- Augmented graph: 32830 nodes, 113915 edges
Public sources captured locally include OCRM/Hurtt/Jim Palmer pages. These are context bridges only; they do not establish fraud or personal liability.

## Anomaly And Exploitation-Risk Themes

- Vulnerable-population context is a priority signal: guardianship, conservatorship, LPS/mental-health, minor, and patient cases are weighted for review.
- Recorder-window signals include transfer-like documents, distress/lien/default-like documents, exact-name overlap, low-collision windows, and dense recorder activity.
- Highest-risk leads still need official court docket/minute orders and official recorder images before any external claim is made.
- Surname-only linkage is intentionally retained as a lead because names are case-specific, but it must not be treated as identity resolution.

### Prior All-8 Exploitation Report Excerpt

# Vulnerable-Population Exploitation Risk Report
This report identifies investigative risk patterns. It does not conclude that fraud occurred.
## Statistical Summary
- Cases reviewed: 171
- Mean exploitation-risk score: 69.5
- Median exploitation-risk score: 70.77
- P0 document-pull lanes: 1
- P1 chronology/APN lanes: 122
- APN-resolved recorder documents: 0
- Actor surnames with criminal-attorney hits: 13
- Actor surnames with lawsuit hits: 169
## Key Pattern Clusters
- vulnerable_court_control: 168 cases; Court process involves vulnerable-population context; prioritize court-order chronology and fiduciary/professional actor identification.
- distress_lien_default_cluster: 50 cases; Lien/default/foreclosure-style records cluster near court filing window; prioritize distress chronology and party role review.
- dense_transfer_activity: 48 cases; Large volume of transfer-like recorder hits near case filing; prioritize APN/document image pulls to separate true asset movement from surname collision.
- high_name_collision_density: 14 cases; Very dense surname activity; useful for pattern detection but weak for identity without document/APN corroboration.
- exact_name_overlap: 4 cases; At least one exact-name recorder overlap; stronger linkage candidate requiring identity disambiguation.
- user_actor_context: 2 cases; User-provided actor context intersects a scored lead; preserve as unverified context until independently corroborated.
## Highest-Priority Cases
- A171585 / HARRIS: score 100.0; lane P0 document-pull and identity-resolution; signals {'vulnerable_population': True, 'transfers': 502, 'distress': 102, 'exact': 1, 'user_context': False}
- A171910 / SMITH: score 88.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': False, 'transfers': 1938, 'distress': 424, 'exact': 1, 'user_context': False}
- A174196 / NGUYEN: score 88.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': False, 'transfers': 829, 'distress': 126, 'exact': 1, 'user_context': False}
- A171522 / JONES: score 88.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 1098, 'distress': 219, 'exact': 0, 'user_context': False}
- A173044 / JOHNSON: score 88.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 1299, 'distress': 291, 'exact': 0, 'user_context': False}
- A173917 / NGUYEN: score 88.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 1235, 'distress': 169, 'exact': 0, 'user_context': False}
- A174235 / NGUYEN: score 88.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 786, 'distress': 123, 'exact': 0, 'user_context': False}
- A174409 / NGUYEN: score 88.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 542, 'distress': 97, 'exact': 0, 'user_context': False}
- A173359 / DAVIS: score 86.08; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 474, 'distress': 79, 'exact': 0, 'user_context': False}
- A173527 / DAVIS: score 84.7; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 385, 'distress': 68, 'exact': 0, 'user_context': False}
- A173609 / DAVIS: score 84.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 360, 'distress': 64, 'exact': 0, 'user_context': False}
- A173610 / DAVIS: score 84.2; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 360, 'distress': 64, 'exact': 0, 'user_context': False}
- A171502 / SHELDON: score 82.15; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 48, 'distress': 14, 'exact': 0, 'user_context': True}
- A171508 / VU: score 81.95; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 587, 'distress': 46, 'exact': 0, 'user_context': False}
- A172078 / FELTON: score 80.47; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 5, 'distress': 10, 'exact': 0, 'user_context': True}
- A172793 / WALLACE: score 80.05; lane P1 chronology and parcel/APN confirmation; signals {'vulnerable_population': True, 'transfers': 216, 'distress': 41, 'exact': 0, 'user_context': False}

### Filled Database Statistical Report Excerpt

# Filled Database Statistical and Anomaly Report
## Scope and Guardrail
This report summarizes restored court records, imported RecorderWorks index rows, and the Orange County public parcel layer. It identifies risk indicators and leads only; it does not establish fraud, ownership, title status, or identity equivalence without doc
## Database Fill
- court_cases: 171,429
- instruments: 888,523
- instrument_parties: 1,543,809
- parcels: 688,023
- addresses: 633,209
- source_documents: 8
- Court filing dates: 1994-01-03 to 2026-05-20
- Recorder dates: 1982-01-04 to 2026-04-29
## Vulnerable-Population Court Surface
- conservatorship: 26,863
- guardianship: 11,265
- mental_health: 28,335
- minor_related: 13,567
## Probate-to-Recorder Window Overlay
- Probate-family cases processed: 127,885
- Cases with local recorder matches: 1,036
- Cases with transfer matches: 929
- Cases with exact-name matches: 5
- Vulnerable cases with local matches: 332
- Vulnerable cases with transfer matches: 301
- Exploitation-watch flagged cases: 38,128
- Priority case leads generated: 38,757
- Exact-name case leads generated: 5
- Vulnerable-transfer case leads generated: 301
## Recorder Risk Signals
- Transfer-like instruments: 557,843 (62.783%)
- Distress/lien/default-like instruments: 112,045 (12.61%)
Top recorder document types:
- TRUST DEED: 173,994
- RECONVEYANCE: 156,731
- GRANT DEED: 117,220

## Other Correlation Surfaces


### Criminal Attorney / Probate Sale Match Summary

- comparison_summary: {"criminal_attorney_rows": 13, "criminal_unique_surnames": 13, "probate_rows_with_surnames": 0, "probate_sale_rows": 0, "surname_matches": 0}
- criminal_summary: {"attorney_rows_extracted": 13, "detail_files_scanned": 20, "detail_page_kind_counts": {"search_results_help": 20}, "manual_attorney_rows_loaded": 13, "unique_attorney_surnames": ["armendariz", "brown", "chally", "gawad", "glass", "hernandez", "lagun
- probate_summary: {"housing_probate_cases_last_decade": 0, "notes": ["probate_tracker contained no sold-status or sold-activity probate listings dated 2016-01-01 or later.", "housing_fraud_intel.db court_cases table currently stops before 2016, so it cannot supply pas

### Criminal Attorney / Probate Anomaly Ranked Summary

- rows_ranked: 30
- severity_counts: {"high": 2, "medium": 10, "low": 18}
- top_high: [{"severity": "high", "score": 11, "surname": "brown", "related_party_name": "BROWN-D", "row_count": 37, "direct_count": 37, "expanded_count": 0, "distinct_case_types": 7, "distinct_case_numbers": 37, "first_filing_date": "1994-02-15", "last_filing_d

### Sale-Date Cross Reference Summary

- case_count: 171
- document_pull_queue_rows: 18897
- generated_at: 2026-06-08T09:47:10.058306+00:00
- key_finding: Current public parcel/UrbanKit data verifies APN/address, but does not provide sale dates. Sale-date corroboration must start from RecorderWorks transfer recording dates and document-image extraction.
- outputs: {"case_summary": "/Users/ALISTAIRE/housing-fraud-intel-api/exports/sale_date_cross_reference/case_sale_date_candidate_summary.csv", "document_pull_queue": "/Users/ALISTAIRE/housing-fraud-intel-api/exports/sale_date_cross_reference/sale_date_document_
- probate_sales_rows: 0
- source_stats: {"instrument_transfer_rows": 569185, "instrument_transfer_rows_with_apn": 0, "parcels_total": 688023, "parcels_with_last_sale_date": 0, "parcels_with_last_sale_price": 0}
- urbankit_mcp: {"endpoint": "https://urbankitstudio.com/api/mcp", "ocgis_endpoint": "https://www.ocgis.com/arcpub/rest/services/Map_Layers/Parcels/MapServer/0", "orange_county_fips": "06059", "sale_date_fields_available": false, "searchable_fields": ["ASSESSMENT_NO

## All High And Medium Review Leads

`001 | A171585 | 79.9 | high_review | 1994-01-11 | LPS CONSERVATORSHIP (WI 5350) | HARRIS-C`
`002 | A172078 | 62.05 | medium_review | 1994-02-24 | GUARDIANSHIP OF PERSON ONLY | FELTON-M`
`003 | A171502 | 61.8 | medium_review | 1994-01-05 | GUARDIANSHIP OF PERSON ONLY | SHELDON-MINOR`
`004 | A171711 | 61.8 | medium_review | 1994-01-21 | CONSERVATORSHIP OF PERSON ONLY | CUEVAS-C`
`005 | A172023 | 61.8 | medium_review | 1994-02-18 | LPS CONSERVATORSHIP (WI 5350) | RHEE-C`
`006 | A172377 | 61.8 | medium_review | 1994-03-16 | LIMITED CONSERVATORSHIP OF PERSON ONLY | CARLTON-C`
`007 | A172659 | 61.8 | medium_review | 1994-04-01 | GUARDIANSHIP OF PERSON ONLY | MICHEL-M`
`008 | A172675 | 61.8 | medium_review | 1994-04-01 | CONSERVATORSHIP OF PERSON AND ESTATE | MATTSON-C`
`009 | A172761 | 61.8 | medium_review | 1994-04-07 | LPS CONSERVATORSHIP (WI 5350) | RHODES-C`
`010 | A173379 | 61.8 | medium_review | 1994-05-20 | GUARDIANSHIP OF PERSON ONLY | BOYD-M`
`011 | A171523 | 61.62 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | LEE-C`
`012 | A171869 | 61.62 | medium_review | 1994-02-07 | GUARDIANSHIP OF PERSON AND ESTATE | JEWETT-M`
`013 | A171610 | 61.55 | medium_review | 1994-01-12 | CONSERVATORSHIP OF PERSON AND ESTATE | MADDOX-C`
`014 | A172308 | 61.55 | medium_review | 1994-03-10 | CONSERVATORSHIP OF PERSON AND ESTATE | PRATT-C`
`015 | A172370 | 60.87 | medium_review | 1994-03-15 | GUARDIANSHIP OF ESTATE ONLY | WEST-M`
`016 | A172539 | 60.87 | medium_review | 1994-03-25 | LPS CONSERVATORSHIP (WI 5350) | LEE-C`
`017 | A172671 | 60.87 | medium_review | 1994-04-01 | LPS CONSERVATORSHIP (WI 5350) | BURKHARDT-C`
`018 | A172979 | 60.87 | medium_review | 1994-04-21 | CONSERVATORSHIP OF ESTATE ONLY | HURD-C`
`019 | A171857 | 60.81 | medium_review | 1994-02-03 | LPS CONSERVATORSHIP (WI 5350) | ASHLEY-C`
`020 | A172631 | 60.81 | medium_review | 1994-03-31 | LPS CONSERVATORSHIP (WI 5350) | CARRANZA-C`
`021 | A173520 | 60.81 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | NORRIS-C`
`022 | A172509 | 60.13 | medium_review | 1994-03-23 | LIMITED CONSERVATORSHIP OF PERSON ONLY | NIEVES-C`
`023 | A172552 | 60.13 | medium_review | 1994-03-25 | GUARDIANSHIP OF PERSON ONLY | SABO-M`
`024 | A172678 | 60.13 | medium_review | 1994-04-04 | GUARDIANSHIP OF ESTATE ONLY | HERNDON-M`
`025 | A174101 | 60.13 | medium_review | 1994-07-15 | GUARDIANSHIP OF ESTATE ONLY | SMITH-M`
`026 | A172567 | 60.06 | medium_review | 1994-03-28 | LPS CONSERVATORSHIP (WI 5350) | JOHNS-C`
`027 | A172582 | 60.06 | medium_review | 1994-03-29 | GUARDIANSHIP OF PERSON AND ESTATE | JOHNS-M`
`028 | A182843 | 59.72 | medium_review | 1996-05-28 | PROBATE OF WILL - LETTERS TESTAMENTARY | PALMER-D`
`029 | A171803 | 59.38 | medium_review | 1994-01-31 | LIMITED CONSERVATORSHIP OF PERSON ONLY | WILLIAMS-C`
`030 | A172483 | 59.38 | medium_review | 1994-03-22 | CONSERVATORSHIP OF PERSON AND ESTATE | VAN DYKE-C`
`031 | A173074 | 59.38 | medium_review | 1994-04-27 | LPS CONSERVATORSHIP (WI 5350) | KIM-C`
`032 | A173504 | 59.38 | medium_review | 1994-06-02 | CONSERVATORSHIP OF PERSON AND ESTATE | DE SOTO-C`
`033 | A173916 | 59.38 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | MC VICAR-C`
`034 | A175806 | 59.38 | medium_review | 1994-11-29 | CONSERVATORSHIP OF PERSON AND ESTATE | O'DELL-C`
`035 | A175904 | 59.38 | medium_review | 1994-12-06 | LIMITED CONSERVATORSHIP OF PERSON ONLY | O'BITZ-C`
`036 | A212735 | 59.38 | medium_review | 2002-04-03 | GUARDIANSHIP OF PERSON AND ESTATE | BOURNE-M`
`037 | A171493 | 59.32 | medium_review | 1994-01-04 | CONSERVATORSHIP OF PERSON AND ESTATE | GOLDSTEIN-C`
`038 | A171494 | 59.32 | medium_review | 1994-01-04 | CONSERVATORSHIP OF PERSON AND ESTATE | GOLDSTEIN-C`
`039 | A171557 | 59.32 | medium_review | 1994-01-07 | GUARDIANSHIP OF PERSON AND ESTATE | VELA-M`
`040 | A171712 | 59.32 | medium_review | 1994-01-21 | LPS CONSERVATORSHIP (WI 5350) | LUTZ-C`
`041 | A172975 | 59.32 | medium_review | 1994-04-20 | CONSERVATORSHIP OF PERSON AND ESTATE | COCHRAN-C`
`042 | A172281 | 59.2 | medium_review | 1994-03-09 | LPS CONSERVATORSHIP (WI 5350) | CATLETT-C`
`043 | A171594 | 58.58 | medium_review | 1994-01-11 | CONSERVATORSHIP OF PERSON AND ESTATE | DILL-C`
`044 | A172571 | 58.58 | medium_review | 1994-03-28 | CONSERVATORSHIP OF PERSON AND ESTATE | COY-C`
`045 | A173831 | 58.58 | medium_review | 1994-06-27 | CONSERVATORSHIP OF PERSON AND ESTATE | RICHTER-C`
`046 | A212707 | 58.58 | medium_review | 2002-04-03 | CONSERVATORSHIP OF PERSON AND ESTATE | VALENTINE-C`
`047 | A175050 | 58.27 | medium_review | 1994-09-26 | GUARDIANSHIP OF PERSON ONLY | BAILEY-M`
`048 | A171910 | 58.2 | medium_review | 1994-02-09 | PROBATE OF WILL - LETTERS TESTAMENTARY | SMITH-D`
`049 | A174196 | 58.2 | medium_review | 1994-07-22 | PROBATE OF WILL  - LETTERS OF ADMINISTRATI | NGUYEN-D`
`050 | A172578 | 57.83 | medium_review | 1994-03-28 | CONSERVATORSHIP OF PERSON AND ESTATE | REIMER-C`
`051 | A173522 | 57.83 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | MC CARTY-C`
`052 | A212689 | 57.83 | medium_review | 2002-04-02 | CONSERVATORSHIP OF PERSON AND ESTATE | YODER-C`
`053 | A171558 | 57.52 | medium_review | 1994-01-10 | CONSERVATORSHIP OF PERSON AND ESTATE | MARTIN-C`
`054 | A171671 | 57.52 | medium_review | 1994-01-19 | LPS CONSERVATORSHIP (WI 5350) | BUSHMAN-C`
`055 | A171787 | 57.09 | medium_review | 1994-01-28 | GUARDIANSHIP OF PERSON ONLY | MASUDA-M`
`056 | A172260 | 57.09 | medium_review | 1994-03-07 | LPS CONSERVATORSHIP (WI 5350) | CURRIE-C`
`057 | A172822 | 57.09 | medium_review | 1994-04-11 | CONSERVATORSHIP OF PERSON AND ESTATE | MCCONNELL-C`
`058 | A173175 | 57.09 | medium_review | 1994-05-06 | GUARDIANSHIP OF PERSON AND ESTATE | DOWNEY-M`
`059 | A174080 | 57.09 | medium_review | 1994-07-14 | CONSERVATORSHIP OF PERSON AND ESTATE | SMITH-C`
`060 | A174129 | 57.09 | medium_review | 1994-07-19 | GUARDIANSHIP OF ESTATE ONLY | GABRIEL JR-M`
`061 | A171526 | 56.34 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | WINSTON-C`
`062 | A171576 | 56.34 | medium_review | 1994-01-10 | LPS CONSERVATORSHIP (WI 5350) | GLEASON-C`
`063 | A171866 | 56.34 | medium_review | 1994-02-04 | GUARDIANSHIP OF PERSON ONLY | THURSTON-M`
`064 | A172422 | 56.34 | medium_review | 1994-03-17 | LPS CONSERVATORSHIP (WI 5350) | KIM-C`
`065 | A172497 | 56.34 | medium_review | 1994-03-22 | LPS CONSERVATORSHIP (WI 5350) | TOOKER-C`
`066 | A173097 | 56.34 | medium_review | 1994-04-29 | LPS CONSERVATORSHIP (WI 5350) | DE NEUI-C`
`067 | A171533 | 55.72 | medium_review | 1994-01-06 | CONSERVATORSHIP OF PERSON AND ESTATE | DUNN-C`
`068 | A171583 | 55.72 | medium_review | 1994-01-11 | LPS CONSERVATORSHIP (WI 5350) | NICHOLS-C`
`069 | A171584 | 55.72 | medium_review | 1994-01-11 | LPS CONSERVATORSHIP (WI 5350) | KNIGHT-C`
`070 | A171690 | 55.72 | medium_review | 1994-01-20 | LPS CONSERVATORSHIP (WI 5350) | GATES-C`
`071 | A171743 | 55.72 | medium_review | 1994-01-25 | LPS CONSERVATORSHIP (WI 5350) | WHEELER-C`
`072 | A171778 | 55.72 | medium_review | 1994-01-27 | GUARDIANSHIP OF PERSON AND ESTATE | CASTILLO-M`
`073 | A171837 | 55.72 | medium_review | 1994-02-03 | GUARDIANSHIP OF PERSON ONLY | HARRISON-M`
`074 | A171862 | 55.72 | medium_review | 1994-02-04 | GUARDIANSHIP OF PERSON ONLY | NORRIS-M`
`075 | A171960 | 55.72 | medium_review | 1994-02-15 | CONSERVATORSHIP OF PERSON AND ESTATE | HARRISON-C`
`076 | A171975 | 55.72 | medium_review | 1994-02-15 | GUARDIANSHIP OF PERSON ONLY | GUERRERO-M`
`077 | A171996 | 55.72 | medium_review | 1994-02-16 | CONSERVATORSHIP OF PERSON AND ESTATE | AVILA-C`
`078 | A172071 | 55.72 | medium_review | 1994-02-23 | CONSERVATORSHIP OF PERSON AND ESTATE | RILEY-C`
`079 | A172083 | 55.72 | medium_review | 1994-02-24 | LPS CONSERVATORSHIP (WI 5350) | ALLISON-C`
`080 | A172267 | 55.72 | medium_review | 1994-03-08 | GUARDIANSHIP OF ESTATE ONLY | ARNOLD-M`
`081 | A172510 | 55.72 | medium_review | 1994-03-23 | CONSERVATORSHIP OF PERSON AND ESTATE | STEIN-C`
`082 | A172568 | 55.72 | medium_review | 1994-03-28 | LPS CONSERVATORSHIP (WI 5350) | MATTHEWS-C`
`083 | A172783 | 55.72 | medium_review | 1994-04-08 | GUARDIANSHIP OF PERSON ONLY | BAILEY-M`
`084 | A172793 | 55.72 | medium_review | 1994-04-08 | CONSERVATORSHIP OF PERSON AND ESTATE | WALLACE-C`
`085 | A173467 | 55.72 | medium_review | 1994-05-27 | LPS CONSERVATORSHIP (WI 5350) | RILEY-C`
`086 | A174364 | 55.72 | medium_review | 1994-08-04 | GUARDIANSHIP OF ESTATE ONLY | DAVIS-M`
`087 | A183184 | 55.72 | medium_review | 1996-06-21 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C`
`088 | A183953 | 55.72 | medium_review | 1996-08-14 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C`
`089 | A186883 | 55.72 | medium_review | 1997-04-02 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C`
`090 | A194892 | 55.72 | medium_review | 1998-11-20 | GUARDIANSHIP OF PERSON AND ESTATE | PALMER-M`
`091 | A202011 | 55.72 | medium_review | 2000-04-19 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS`
`092 | A204953 | 55.72 | medium_review | 2000-11-08 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS`
`093 | A205071 | 55.72 | medium_review | 2000-11-20 | CONSERVATORSHIP OF PERSON AND ESTATE | PALMER-C`
`094 | A172496 | 55.29 | medium_review | 1994-03-22 | LPS CONSERVATORSHIP (WI 5350) | HIXSON-C`
`095 | A171522 | 54.2 | medium_review | 1994-01-05 | GUARDIANSHIP OF ESTATE ONLY | JONES-M`
`096 | A171508 | 54.2 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | VU-C`
`097 | A173044 | 54.2 | medium_review | 1994-04-25 | LPS CONSERVATORSHIP (WI 5350) | JOHNSON-C`
`098 | A173359 | 54.2 | medium_review | 1994-05-18 | LPS CONSERVATORSHIP (WI 5350) | DAVIS-C`
`099 | A173527 | 54.2 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | DAVIS-C`
`100 | A173609 | 54.2 | medium_review | 1994-06-09 | CONSERVATORSHIP OF PERSON AND ESTATE | DAVIS-C`
`101 | A173610 | 54.2 | medium_review | 1994-06-09 | GUARDIANSHIP OF PERSON AND ESTATE | DAVIS-M`
`102 | A173917 | 54.2 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | NGUYEN-C`
`103 | A174235 | 54.2 | medium_review | 1994-07-25 | LPS CONSERVATORSHIP (WI 5350) | NGUYEN-C`
`104 | A174409 | 54.2 | medium_review | 1994-08-08 | LPS CONSERVATORSHIP (WI 5350) | NGUYEN-C`
`105 | A171802 | 53.98 | medium_review | 1994-01-31 | CONSERVATORSHIP OF PERSON AND ESTATE | STEIN-C`
`106 | A171524 | 53.68 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | REEDY-C`
`107 | A171592 | 53.68 | medium_review | 1994-01-11 | GUARDIANSHIP OF PERSON ONLY | TYNER-M`
`108 | A171810 | 53.68 | medium_review | 1994-02-01 | CONSERVATORSHIP OF PERSON AND ESTATE | SOUTH-C`
`109 | A172211 | 53.68 | medium_review | 1994-03-07 | CONSERVATORSHIP OF PERSON AND ESTATE | MARTIN-C`
`110 | A172920 | 53.68 | medium_review | 1994-04-18 | LPS CONSERVATORSHIP (WI 5350) | MILLER-C`
`111 | A173523 | 53.68 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | MILLER-C`
`112 | A212708 | 53.68 | medium_review | 2002-04-03 | CONSERVATORSHIP OF PERSON AND ESTATE | BONFIGLIO-C`
`113 | A172643 | 52.75 | medium_review | 1994-03-31 | CONSERVATORSHIP OF PERSON AND ESTATE | WILLIAMS-C`
`114 | A172644 | 52.75 | medium_review | 1994-03-31 | CONSERVATORSHIP OF PERSON AND ESTATE | **WILLIAMS- CONSOLIDATED INTO A172643`
`115 | A172738 | 52.75 | medium_review | 1994-04-06 | CONSERVATORSHIP OF PERSON AND ESTATE | GARCIA-C`
`116 | A171632 | 52.56 | medium_review | 1994-01-14 | LPS CONSERVATORSHIP (WI 5350) | ROGERS-C`
`117 | A173195 | 52.56 | medium_review | 1994-05-06 | GUARDIANSHIP OF PERSON ONLY | SABO-M`
`118 | A171906 | 50.7 | medium_review | 1994-02-09 | LPS CONSERVATORSHIP (WI 5350) | ADAMS-C`
`119 | A172201 | 50.7 | medium_review | 1994-03-03 | GUARDIANSHIP OF PERSON AND ESTATE | PEREZ-M`
`120 | A172365 | 50.7 | medium_review | 1994-03-15 | LPS CONSERVATORSHIP (WI 5350) | MUKAI-C`
`121 | A171631 | 50.64 | medium_review | 1994-01-14 | LPS CONSERVATORSHIP (WI 5350) | PHAM-C`
`122 | A172259 | 50.64 | medium_review | 1994-03-07 | LPS CONSERVATORSHIP (WI 5350) | WINSTON-C`
`123 | A172721 | 50.64 | medium_review | 1994-04-06 | CONSERVATORSHIP OF PERSON AND ESTATE | FAWCETT-C`
`124 | A173466 | 50.64 | medium_review | 1994-05-27 | LPS CONSERVATORSHIP (WI 5350) | LE-C`
`125 | A212951 | 50.64 | medium_review | 2002-04-16 | CONSERVATORSHIP OF PERSON AND ESTATE | CHASE-C`
`126 | A172458 | 50.52 | medium_review | 1994-03-21 | GUARDIANSHIP OF PERSON ONLY | WAMPLER-M`
`127 | A172739 | 50.33 | medium_review | 1994-04-07 | GUARDIANSHIP OF ESTATE ONLY | BENAVIDEZ-M`
`128 | A172081 | 49.77 | medium_review | 1994-02-24 | LPS CONSERVATORSHIP (WI 5350) | COLLINS-C`
`129 | A172633 | 49.77 | medium_review | 1994-03-31 | GUARDIANSHIP OF PERSON AND ESTATE | KORDICH-M`
`130 | A172710 | 49.77 | medium_review | 1994-04-05 | CONSERVATORSHIP OF PERSON AND ESTATE | SANDHOFF-C`
`131 | A173043 | 49.77 | medium_review | 1994-04-25 | CONSERVATORSHIP OF PERSON AND ESTATE | SANDHOFF-C`
`132 | A174425 | 49.77 | medium_review | 1994-08-09 | GUARDIANSHIP OF PERSON ONLY | DE LA O-M`
`133 | A171714 | 49.59 | medium_review | 1994-01-21 | LPS CONSERVATORSHIP (WI 5350) | KAMINSKY-C`
`134 | A173267 | 49.59 | medium_review | 1994-05-11 | GUARDIANSHIP OF PERSON AND ESTATE | FOGLER-M`
`135 | A172432 | 48.84 | medium_review | 1994-03-17 | LPS CONSERVATORSHIP (WI 5350) | LEV-C`
`136 | A172699 | 48.84 | medium_review | 1994-04-04 | CONSERVATORSHIP OF PERSON AND ESTATE | SCHLUETER-C`
`137 | A173296 | 48.84 | medium_review | 1994-05-13 | GUARDIANSHIP OF PERSON AND ESTATE | CLARK-M`
`138 | A174600 | 48.84 | medium_review | 1994-08-22 | LPS CONSERVATORSHIP (WI 5350) | SMITH-C`
`139 | A214204 | 48.84 | medium_review | 2002-07-01 | LPS CONSERVATORSHIP (WI 5350) | ALVARADO-LPS`
`140 | A172534 | 48.72 | medium_review | 1994-03-24 | CONSERVATORSHIP OF PERSON AND ESTATE | RUSSELL-C`
`141 | A172827 | 48.72 | medium_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | DINH-C`
`142 | A212419 | 48.72 | medium_review | 2002-03-13 | GUARDIANSHIP OF PERSON AND ESTATE | GOLDEN-M`
`143 | A172837 | 47.91 | medium_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | FRANK-C`
`144 | A172838 | 47.91 | medium_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | AYALA-C`
`145 | A173268 | 47.91 | medium_review | 1994-05-11 | LPS CONSERVATORSHIP (WI 5350) | HODGE-C`
`146 | A173613 | 47.91 | medium_review | 1994-06-09 | GUARDIANSHIP OF PERSON ONLY | CLARK-M`
`147 | A171765 | 46.86 | medium_review | 1994-01-26 | LPS CONSERVATORSHIP (WI 5350) | LOPEZ-C`
`148 | A172017 | 46.86 | medium_review | 1994-02-18 | GUARDIANSHIP OF PERSON ONLY | THOMAS JR-M`
`149 | A172035 | 46.86 | medium_review | 1994-02-22 | GUARDIANSHIP OF PERSON ONLY | MARTINEZ-M`
`150 | A172878 | 46.86 | medium_review | 1994-04-14 | CONSERVATORSHIP OF ESTATE ONLY | BENNETT-C`
`151 | A173173 | 46.86 | medium_review | 1994-05-05 | CONSERVATORSHIP OF PERSON AND ESTATE | BENNETT-C`
`152 | A173525 | 46.86 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | LEWIS-C`
`153 | A171769 | 45.93 | medium_review | 1994-01-27 | LPS CONSERVATORSHIP (WI 5350) | JACKSON-C`
`154 | A172022 | 45.93 | medium_review | 1994-02-18 | LPS CONSERVATORSHIP (WI 5350) | WILSON-C`
`155 | A173159 | 45.93 | medium_review | 1994-05-04 | LPS CONSERVATORSHIP (WI 5350) | JACKSON-C`
`156 | A173168 | 45.93 | medium_review | 1994-05-05 | GUARDIANSHIP OF PERSON ONLY | HERNANDEZ-M`
`157 | A173266 | 45.93 | medium_review | 1994-05-11 | LPS CONSERVATORSHIP (WI 5350) | HA-C`
`158 | A173524 | 45.93 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | DINH-C`
`159 | A173666 | 45.93 | medium_review | 1994-06-13 | GUARDIANSHIP OF PERSON ONLY | GARCIA-M`
`160 | A171636 | 45.0 | medium_review | 1994-01-14 | LPS CONSERVATORSHIP (WI 5350) | RICHARDSON-C`
`161 | A172066 | 45.0 | medium_review | 1994-02-23 | GUARDIANSHIP OF ESTATE ONLY | RAMIREZ-M`
`162 | A172430 | 45.0 | medium_review | 1994-03-17 | LPS CONSERVATORSHIP (WI 5350) | FOX-C`
`163 | A172926 | 45.0 | medium_review | 1994-04-18 | LPS CONSERVATORSHIP (WI 5350) | WHITE-C`
`164 | A172961 | 45.0 | medium_review | 1994-04-20 | LPS CONSERVATORSHIP (WI 5350) | HUGHES-C`
`165 | A173073 | 45.0 | medium_review | 1994-04-27 | CONSERVATORSHIP OF PERSON ONLY | RUSSELL-C`
`166 | A173129 | 45.0 | medium_review | 1994-05-03 | GUARDIANSHIP OF PERSON ONLY | MARTINEZ-M`
`167 | A173130 | 45.0 | medium_review | 1994-05-03 | LPS CONSERVATORSHIP (WI 5350) | RODRIGUEZ-C`
`168 | A173274 | 45.0 | medium_review | 1994-05-12 | LPS CONSERVATORSHIP (WI 5350) | MARTINEZ-C`
`169 | A173473 | 45.0 | medium_review | 1994-05-31 | CONSERVATORSHIP OF PERSON AND ESTATE | MORGAN-C`
`170 | A173750 | 45.0 | medium_review | 1994-06-21 | GUARDIANSHIP OF ESTATE ONLY | WILSON-M`
`171 | A173915 | 45.0 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | BROWN-C`
`172 | A173930 | 45.0 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | TAYLOR-C`
`173 | A173999 | 45.0 | medium_review | 1994-07-08 | LPS CONSERVATORSHIP (WI 5350) | BROWN-C`
`174 | A174070 | 45.0 | medium_review | 1994-07-13 | LPS CONSERVATORSHIP (WI 5350) | HOANG-C`
`175 | A174130 | 45.0 | medium_review | 1994-07-19 | CONSERVATORSHIP OF PERSON AND ESTATE | MILLER-C`
`176 | A174500 | 45.0 | medium_review | 1994-08-15 | LPS CONSERVATORSHIP (WI 5350) | LEVESQUE-C`
`177 | A200435 | 45.0 | medium_review | 2000-01-03 | LPS CONSERVATORSHIP (WI 5350) | WASHINGTON-LPS`
`178 | A208278 | 45.0 | medium_review | 2001-06-13 | GUARDIANSHIP OF ESTATE ONLY | NORTH-M`
`179 | A212787 | 45.0 | medium_review | 2002-04-04 | CONSERVATORSHIP OF PERSON ONLY | AMESCUA-C`

## All Scored Rows Compact Appendix

`0001 | A171585 | 79.9 | high_review | 1994-01-11 | LPS CONSERVATORSHIP (WI 5350) | HARRIS-C | LM=721 TR=498 EX=1`
`0002 | A172078 | 62.05 | medium_review | 1994-02-24 | GUARDIANSHIP OF PERSON ONLY | FELTON-M | LM=17 TR=5 EX=0`
`0003 | A171502 | 61.8 | medium_review | 1994-01-05 | GUARDIANSHIP OF PERSON ONLY | SHELDON-MINOR | LM=73 TR=48 EX=0`
`0004 | A171711 | 61.8 | medium_review | 1994-01-21 | CONSERVATORSHIP OF PERSON ONLY | CUEVAS-C | LM=86 TR=49 EX=0`
`0005 | A172023 | 61.8 | medium_review | 1994-02-18 | LPS CONSERVATORSHIP (WI 5350) | RHEE-C | LM=32 TR=15 EX=0`
`0006 | A172377 | 61.8 | medium_review | 1994-03-16 | LIMITED CONSERVATORSHIP OF PERSON O | CARLTON-C | LM=23 TR=10 EX=0`
`0007 | A172659 | 61.8 | medium_review | 1994-04-01 | GUARDIANSHIP OF PERSON ONLY | MICHEL-M | LM=63 TR=43 EX=0`
`0008 | A172675 | 61.8 | medium_review | 1994-04-01 | CONSERVATORSHIP OF PERSON AND ESTAT | MATTSON-C | LM=42 TR=27 EX=0`
`0009 | A172761 | 61.8 | medium_review | 1994-04-07 | LPS CONSERVATORSHIP (WI 5350) | RHODES-C | LM=91 TR=62 EX=0`
`0010 | A173379 | 61.8 | medium_review | 1994-05-20 | GUARDIANSHIP OF PERSON ONLY | BOYD-M | LM=85 TR=61 EX=0`
`0011 | A171523 | 61.62 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | LEE-C | LM=16 TR=11 EX=0`
`0012 | A171869 | 61.62 | medium_review | 1994-02-07 | GUARDIANSHIP OF PERSON AND ESTATE | JEWETT-M | LM=15 TR=11 EX=0`
`0013 | A171610 | 61.55 | medium_review | 1994-01-12 | CONSERVATORSHIP OF PERSON AND ESTAT | MADDOX-C | LM=44 TR=26 EX=0`
`0014 | A172308 | 61.55 | medium_review | 1994-03-10 | CONSERVATORSHIP OF PERSON AND ESTAT | PRATT-C | LM=80 TR=60 EX=0`
`0015 | A172370 | 60.87 | medium_review | 1994-03-15 | GUARDIANSHIP OF ESTATE ONLY | WEST-M | LM=16 TR=11 EX=0`
`0016 | A172539 | 60.87 | medium_review | 1994-03-25 | LPS CONSERVATORSHIP (WI 5350) | LEE-C | LM=17 TR=13 EX=0`
`0017 | A172671 | 60.87 | medium_review | 1994-04-01 | LPS CONSERVATORSHIP (WI 5350) | BURKHARDT-C | LM=15 TR=9 EX=0`
`0018 | A172979 | 60.87 | medium_review | 1994-04-21 | CONSERVATORSHIP OF ESTATE ONLY | HURD-C | LM=14 TR=8 EX=0`
`0019 | A171857 | 60.81 | medium_review | 1994-02-03 | LPS CONSERVATORSHIP (WI 5350) | ASHLEY-C | LM=38 TR=25 EX=0`
`0020 | A172631 | 60.81 | medium_review | 1994-03-31 | LPS CONSERVATORSHIP (WI 5350) | CARRANZA-C | LM=44 TR=32 EX=0`
`0021 | A173520 | 60.81 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | NORRIS-C | LM=44 TR=24 EX=0`
`0022 | A172509 | 60.13 | medium_review | 1994-03-23 | LIMITED CONSERVATORSHIP OF PERSON O | NIEVES-C | LM=14 TR=12 EX=0`
`0023 | A172552 | 60.13 | medium_review | 1994-03-25 | GUARDIANSHIP OF PERSON ONLY | SABO-M | LM=11 TR=8 EX=0`
`0024 | A172678 | 60.13 | medium_review | 1994-04-04 | GUARDIANSHIP OF ESTATE ONLY | HERNDON-M | LM=14 TR=8 EX=0`
`0025 | A174101 | 60.13 | medium_review | 1994-07-15 | GUARDIANSHIP OF ESTATE ONLY | SMITH-M | LM=13 TR=8 EX=0`
`0026 | A172567 | 60.06 | medium_review | 1994-03-28 | LPS CONSERVATORSHIP (WI 5350) | JOHNS-C | LM=53 TR=34 EX=0`
`0027 | A172582 | 60.06 | medium_review | 1994-03-29 | GUARDIANSHIP OF PERSON AND ESTATE | JOHNS-M | LM=54 TR=34 EX=0`
`0028 | A182843 | 59.72 | medium_review | 1996-05-28 | PROBATE OF WILL - LETTERS TESTAMENT | PALMER-D | LM=211 TR=135 EX=1`
`0029 | A171803 | 59.38 | medium_review | 1994-01-31 | LIMITED CONSERVATORSHIP OF PERSON O | WILLIAMS-C | LM=12 TR=8 EX=0`
`0030 | A172483 | 59.38 | medium_review | 1994-03-22 | CONSERVATORSHIP OF PERSON AND ESTAT | VAN DYKE-C | LM=14 TR=8 EX=0`
`0031 | A173074 | 59.38 | medium_review | 1994-04-27 | LPS CONSERVATORSHIP (WI 5350) | KIM-C | LM=20 TR=17 EX=0`
`0032 | A173504 | 59.38 | medium_review | 1994-06-02 | CONSERVATORSHIP OF PERSON AND ESTAT | DE SOTO-C | LM=15 TR=12 EX=0`
`0033 | A173916 | 59.38 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | MC VICAR-C | LM=17 TR=12 EX=0`
`0034 | A175806 | 59.38 | medium_review | 1994-11-29 | CONSERVATORSHIP OF PERSON AND ESTAT | O'DELL-C | LM=15 TR=14 EX=0`
`0035 | A175904 | 59.38 | medium_review | 1994-12-06 | LIMITED CONSERVATORSHIP OF PERSON O | O'BITZ-C | LM=15 TR=14 EX=0`
`0036 | A212735 | 59.38 | medium_review | 2002-04-03 | GUARDIANSHIP OF PERSON AND ESTATE | BOURNE-M | LM=15 TR=10 EX=0`
`0037 | A171493 | 59.32 | medium_review | 1994-01-04 | CONSERVATORSHIP OF PERSON AND ESTAT | GOLDSTEIN-C | LM=97 TR=74 EX=0`
`0038 | A171494 | 59.32 | medium_review | 1994-01-04 | CONSERVATORSHIP OF PERSON AND ESTAT | GOLDSTEIN-C | LM=97 TR=74 EX=0`
`0039 | A171557 | 59.32 | medium_review | 1994-01-07 | GUARDIANSHIP OF PERSON AND ESTATE | VELA-M | LM=28 TR=20 EX=0`
`0040 | A171712 | 59.32 | medium_review | 1994-01-21 | LPS CONSERVATORSHIP (WI 5350) | LUTZ-C | LM=59 TR=46 EX=0`
`0041 | A172975 | 59.32 | medium_review | 1994-04-20 | CONSERVATORSHIP OF PERSON AND ESTAT | COCHRAN-C | LM=58 TR=38 EX=0`
`0042 | A172281 | 59.2 | medium_review | 1994-03-09 | LPS CONSERVATORSHIP (WI 5350) | CATLETT-C | LM=10 TR=7 EX=0`
`0043 | A171594 | 58.58 | medium_review | 1994-01-11 | CONSERVATORSHIP OF PERSON AND ESTAT | DILL-C | LM=44 TR=31 EX=0`
`0044 | A172571 | 58.58 | medium_review | 1994-03-28 | CONSERVATORSHIP OF PERSON AND ESTAT | COY-C | LM=24 TR=17 EX=0`
`0045 | A173831 | 58.58 | medium_review | 1994-06-27 | CONSERVATORSHIP OF PERSON AND ESTAT | RICHTER-C | LM=39 TR=27 EX=0`
`0046 | A212707 | 58.58 | medium_review | 2002-04-03 | CONSERVATORSHIP OF PERSON AND ESTAT | VALENTINE-C | LM=96 TR=75 EX=0`
`0047 | A175050 | 58.27 | medium_review | 1994-09-26 | GUARDIANSHIP OF PERSON ONLY | BAILEY-M | LM=13 TR=6 EX=0`
`0048 | A171910 | 58.2 | medium_review | 1994-02-09 | PROBATE OF WILL - LETTERS TESTAMENT | SMITH-D | LM=2865 TR=1910 EX=1`
`0049 | A174196 | 58.2 | medium_review | 1994-07-22 | PROBATE OF WILL  - LETTERS OF ADMIN | NGUYEN-D | LM=1149 TR=809 EX=1`
`0050 | A172578 | 57.83 | medium_review | 1994-03-28 | CONSERVATORSHIP OF PERSON AND ESTAT | REIMER-C | LM=24 TR=19 EX=0`
`0051 | A173522 | 57.83 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | MC CARTY-C | LM=26 TR=17 EX=0`
`0052 | A212689 | 57.83 | medium_review | 2002-04-02 | CONSERVATORSHIP OF PERSON AND ESTAT | YODER-C | LM=43 TR=35 EX=0`
`0053 | A171558 | 57.52 | medium_review | 1994-01-10 | CONSERVATORSHIP OF PERSON AND ESTAT | MARTIN-C | LM=10 TR=6 EX=0`
`0054 | A171671 | 57.52 | medium_review | 1994-01-19 | LPS CONSERVATORSHIP (WI 5350) | BUSHMAN-C | LM=10 TR=6 EX=0`
`0055 | A171787 | 57.09 | medium_review | 1994-01-28 | GUARDIANSHIP OF PERSON ONLY | MASUDA-M | LM=36 TR=28 EX=0`
`0056 | A172260 | 57.09 | medium_review | 1994-03-07 | LPS CONSERVATORSHIP (WI 5350) | CURRIE-C | LM=32 TR=25 EX=0`
`0057 | A172822 | 57.09 | medium_review | 1994-04-11 | CONSERVATORSHIP OF PERSON AND ESTAT | MCCONNELL-C | LM=22 TR=15 EX=0`
`0058 | A173175 | 57.09 | medium_review | 1994-05-06 | GUARDIANSHIP OF PERSON AND ESTATE | DOWNEY-M | LM=41 TR=37 EX=0`
`0059 | A174080 | 57.09 | medium_review | 1994-07-14 | CONSERVATORSHIP OF PERSON AND ESTAT | SMITH-C | LM=36 TR=28 EX=0`
`0060 | A174129 | 57.09 | medium_review | 1994-07-19 | GUARDIANSHIP OF ESTATE ONLY | GABRIEL JR-M | LM=26 TR=15 EX=0`
`0061 | A171526 | 56.34 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | WINSTON-C | LM=54 TR=48 EX=0`
`0062 | A171576 | 56.34 | medium_review | 1994-01-10 | LPS CONSERVATORSHIP (WI 5350) | GLEASON-C | LM=30 TR=24 EX=0`
`0063 | A171866 | 56.34 | medium_review | 1994-02-04 | GUARDIANSHIP OF PERSON ONLY | THURSTON-M | LM=33 TR=18 EX=0`
`0064 | A172422 | 56.34 | medium_review | 1994-03-17 | LPS CONSERVATORSHIP (WI 5350) | KIM-C | LM=23 TR=20 EX=0`
`0065 | A172497 | 56.34 | medium_review | 1994-03-22 | LPS CONSERVATORSHIP (WI 5350) | TOOKER-C | LM=35 TR=31 EX=0`
`0066 | A173097 | 56.34 | medium_review | 1994-04-29 | LPS CONSERVATORSHIP (WI 5350) | DE NEUI-C | LM=21 TR=17 EX=0`
`0067 | A171533 | 55.72 | medium_review | 1994-01-06 | CONSERVATORSHIP OF PERSON AND ESTAT | DUNN-C | LM=295 TR=213 EX=0`
`0068 | A171583 | 55.72 | medium_review | 1994-01-11 | LPS CONSERVATORSHIP (WI 5350) | NICHOLS-C | LM=233 TR=166 EX=0`
`0069 | A171584 | 55.72 | medium_review | 1994-01-11 | LPS CONSERVATORSHIP (WI 5350) | KNIGHT-C | LM=199 TR=142 EX=0`
`0070 | A171690 | 55.72 | medium_review | 1994-01-20 | LPS CONSERVATORSHIP (WI 5350) | GATES-C | LM=118 TR=76 EX=0`
`0071 | A171743 | 55.72 | medium_review | 1994-01-25 | LPS CONSERVATORSHIP (WI 5350) | WHEELER-C | LM=201 TR=126 EX=0`
`0072 | A171778 | 55.72 | medium_review | 1994-01-27 | GUARDIANSHIP OF PERSON AND ESTATE | CASTILLO-M | LM=265 TR=184 EX=0`
`0073 | A171837 | 55.72 | medium_review | 1994-02-03 | GUARDIANSHIP OF PERSON ONLY | HARRISON-M | LM=245 TR=155 EX=0`
`0074 | A171862 | 55.72 | medium_review | 1994-02-04 | GUARDIANSHIP OF PERSON ONLY | NORRIS-M | LM=117 TR=76 EX=0`
`0075 | A171960 | 55.72 | medium_review | 1994-02-15 | CONSERVATORSHIP OF PERSON AND ESTAT | HARRISON-C | LM=227 TR=140 EX=0`
`0076 | A171975 | 55.72 | medium_review | 1994-02-15 | GUARDIANSHIP OF PERSON ONLY | GUERRERO-M | LM=179 TR=118 EX=0`
`0077 | A171996 | 55.72 | medium_review | 1994-02-16 | CONSERVATORSHIP OF PERSON AND ESTAT | AVILA-C | LM=187 TR=128 EX=0`
`0078 | A172071 | 55.72 | medium_review | 1994-02-23 | CONSERVATORSHIP OF PERSON AND ESTAT | RILEY-C | LM=212 TR=145 EX=0`
`0079 | A172083 | 55.72 | medium_review | 1994-02-24 | LPS CONSERVATORSHIP (WI 5350) | ALLISON-C | LM=185 TR=57 EX=0`
`0080 | A172267 | 55.72 | medium_review | 1994-03-08 | GUARDIANSHIP OF ESTATE ONLY | ARNOLD-M | LM=241 TR=169 EX=0`
`0081 | A172510 | 55.72 | medium_review | 1994-03-23 | CONSERVATORSHIP OF PERSON AND ESTAT | STEIN-C | LM=196 TR=142 EX=0`
`0082 | A172568 | 55.72 | medium_review | 1994-03-28 | LPS CONSERVATORSHIP (WI 5350) | MATTHEWS-C | LM=170 TR=113 EX=0`
`0083 | A172783 | 55.72 | medium_review | 1994-04-08 | GUARDIANSHIP OF PERSON ONLY | BAILEY-M | LM=284 TR=201 EX=0`
`0084 | A172793 | 55.72 | medium_review | 1994-04-08 | CONSERVATORSHIP OF PERSON AND ESTAT | WALLACE-C | LM=312 TR=214 EX=0`
`0085 | A173467 | 55.72 | medium_review | 1994-05-27 | LPS CONSERVATORSHIP (WI 5350) | RILEY-C | LM=114 TR=80 EX=0`
`0086 | A174364 | 55.72 | medium_review | 1994-08-04 | GUARDIANSHIP OF ESTATE ONLY | DAVIS-M | LM=126 TR=84 EX=0`
`0087 | A183184 | 55.72 | medium_review | 1996-06-21 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C | LM=207 TR=144 EX=0`
`0088 | A183953 | 55.72 | medium_review | 1996-08-14 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C | LM=194 TR=132 EX=0`
`0089 | A186883 | 55.72 | medium_review | 1997-04-02 | LPS CONSERVATORSHIP (WI 5350) | PALMER-C | LM=178 TR=118 EX=0`
`0090 | A194892 | 55.72 | medium_review | 1998-11-20 | GUARDIANSHIP OF PERSON AND ESTATE | PALMER-M | LM=241 TR=158 EX=0`
`0091 | A202011 | 55.72 | medium_review | 2000-04-19 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS | LM=204 TR=144 EX=0`
`0092 | A204953 | 55.72 | medium_review | 2000-11-08 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS | LM=211 TR=153 EX=0`
`0093 | A205071 | 55.72 | medium_review | 2000-11-20 | CONSERVATORSHIP OF PERSON AND ESTAT | PALMER-C | LM=215 TR=157 EX=0`
`0094 | A172496 | 55.29 | medium_review | 1994-03-22 | LPS CONSERVATORSHIP (WI 5350) | HIXSON-C | LM=11 TR=2 EX=0`
`0095 | A171522 | 54.2 | medium_review | 1994-01-05 | GUARDIANSHIP OF ESTATE ONLY | JONES-M | LM=1591 TR=1086 EX=0`
`0096 | A171508 | 54.2 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | VU-C | LM=731 TR=580 EX=0`
`0097 | A173044 | 54.2 | medium_review | 1994-04-25 | LPS CONSERVATORSHIP (WI 5350) | JOHNSON-C | LM=1922 TR=1277 EX=0`
`0098 | A173359 | 54.2 | medium_review | 1994-05-18 | LPS CONSERVATORSHIP (WI 5350) | DAVIS-C | LM=664 TR=465 EX=0`
`0099 | A173527 | 54.2 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | DAVIS-C | LM=556 TR=378 EX=0`
`0100 | A173609 | 54.2 | medium_review | 1994-06-09 | CONSERVATORSHIP OF PERSON AND ESTAT | DAVIS-C | LM=518 TR=354 EX=0`
`0101 | A173610 | 54.2 | medium_review | 1994-06-09 | GUARDIANSHIP OF PERSON AND ESTATE | DAVIS-M | LM=518 TR=354 EX=0`
`0102 | A173917 | 54.2 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | NGUYEN-C | LM=1668 TR=1210 EX=0`
`0103 | A174235 | 54.2 | medium_review | 1994-07-25 | LPS CONSERVATORSHIP (WI 5350) | NGUYEN-C | LM=1091 TR=767 EX=0`
`0104 | A174409 | 54.2 | medium_review | 1994-08-08 | LPS CONSERVATORSHIP (WI 5350) | NGUYEN-C | LM=759 TR=527 EX=0`
`0105 | A171802 | 53.98 | medium_review | 1994-01-31 | CONSERVATORSHIP OF PERSON AND ESTAT | STEIN-C | LM=149 TR=121 EX=0`
`0106 | A171524 | 53.68 | medium_review | 1994-01-06 | LPS CONSERVATORSHIP (WI 5350) | REEDY-C | LM=13 TR=11 EX=0`
`0107 | A171592 | 53.68 | medium_review | 1994-01-11 | GUARDIANSHIP OF PERSON ONLY | TYNER-M | LM=10 TR=9 EX=0`
`0108 | A171810 | 53.68 | medium_review | 1994-02-01 | CONSERVATORSHIP OF PERSON AND ESTAT | SOUTH-C | LM=20 TR=11 EX=0`
`0109 | A172211 | 53.68 | medium_review | 1994-03-07 | CONSERVATORSHIP OF PERSON AND ESTAT | MARTIN-C | LM=13 TR=10 EX=0`
`0110 | A172920 | 53.68 | medium_review | 1994-04-18 | LPS CONSERVATORSHIP (WI 5350) | MILLER-C | LM=13 TR=12 EX=0`
`0111 | A173523 | 53.68 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | MILLER-C | LM=11 TR=11 EX=0`
`0112 | A212708 | 53.68 | medium_review | 2002-04-03 | CONSERVATORSHIP OF PERSON AND ESTAT | BONFIGLIO-C | LM=10 TR=9 EX=0`
`0113 | A172643 | 52.75 | medium_review | 1994-03-31 | CONSERVATORSHIP OF PERSON AND ESTAT | WILLIAMS-C | LM=10 TR=7 EX=0`
`0114 | A172644 | 52.75 | medium_review | 1994-03-31 | CONSERVATORSHIP OF PERSON AND ESTAT | **WILLIAMS- CONSOLIDATED INTO A172643 | LM=10 TR=7 EX=0`
`0115 | A172738 | 52.75 | medium_review | 1994-04-06 | CONSERVATORSHIP OF PERSON AND ESTAT | GARCIA-C | LM=10 TR=7 EX=0`
`0116 | A171632 | 52.56 | medium_review | 1994-01-14 | LPS CONSERVATORSHIP (WI 5350) | ROGERS-C | LM=8 TR=6 EX=0`
`0117 | A173195 | 52.56 | medium_review | 1994-05-06 | GUARDIANSHIP OF PERSON ONLY | SABO-M | LM=7 TR=6 EX=0`
`0118 | A171906 | 50.7 | medium_review | 1994-02-09 | LPS CONSERVATORSHIP (WI 5350) | ADAMS-C | LM=6 TR=4 EX=0`
`0119 | A172201 | 50.7 | medium_review | 1994-03-03 | GUARDIANSHIP OF PERSON AND ESTATE | PEREZ-M | LM=5 TR=4 EX=0`
`0120 | A172365 | 50.7 | medium_review | 1994-03-15 | LPS CONSERVATORSHIP (WI 5350) | MUKAI-C | LM=7 TR=4 EX=0`
`0121 | A171631 | 50.64 | medium_review | 1994-01-14 | LPS CONSERVATORSHIP (WI 5350) | PHAM-C | LM=21 TR=21 EX=0`
`0122 | A172259 | 50.64 | medium_review | 1994-03-07 | LPS CONSERVATORSHIP (WI 5350) | WINSTON-C | LM=42 TR=41 EX=0`
`0123 | A172721 | 50.64 | medium_review | 1994-04-06 | CONSERVATORSHIP OF PERSON AND ESTAT | FAWCETT-C | LM=21 TR=13 EX=0`
`0124 | A173466 | 50.64 | medium_review | 1994-05-27 | LPS CONSERVATORSHIP (WI 5350) | LE-C | LM=31 TR=30 EX=0`
`0125 | A212951 | 50.64 | medium_review | 2002-04-16 | CONSERVATORSHIP OF PERSON AND ESTAT | CHASE-C | LM=46 TR=45 EX=0`
`0126 | A172458 | 50.52 | medium_review | 1994-03-21 | GUARDIANSHIP OF PERSON ONLY | WAMPLER-M | LM=6 TR=3 EX=0`
`0127 | A172739 | 50.33 | medium_review | 1994-04-07 | GUARDIANSHIP OF ESTATE ONLY | BENAVIDEZ-M | LM=6 TR=2 EX=0`
`0128 | A172081 | 49.77 | medium_review | 1994-02-24 | LPS CONSERVATORSHIP (WI 5350) | COLLINS-C | LM=5 TR=3 EX=0`
`0129 | A172633 | 49.77 | medium_review | 1994-03-31 | GUARDIANSHIP OF PERSON AND ESTATE | KORDICH-M | LM=5 TR=3 EX=0`
`0130 | A172710 | 49.77 | medium_review | 1994-04-05 | CONSERVATORSHIP OF PERSON AND ESTAT | SANDHOFF-C | LM=4 TR=3 EX=0`
`0131 | A173043 | 49.77 | medium_review | 1994-04-25 | CONSERVATORSHIP OF PERSON AND ESTAT | SANDHOFF-C | LM=4 TR=3 EX=0`
`0132 | A174425 | 49.77 | medium_review | 1994-08-09 | GUARDIANSHIP OF PERSON ONLY | DE LA O-M | LM=6 TR=3 EX=0`
`0133 | A171714 | 49.59 | medium_review | 1994-01-21 | LPS CONSERVATORSHIP (WI 5350) | KAMINSKY-C | LM=5 TR=2 EX=0`
`0134 | A173267 | 49.59 | medium_review | 1994-05-11 | GUARDIANSHIP OF PERSON AND ESTATE | FOGLER-M | LM=7 TR=2 EX=0`
`0135 | A172432 | 48.84 | medium_review | 1994-03-17 | LPS CONSERVATORSHIP (WI 5350) | LEV-C | LM=3 TR=2 EX=0`
`0136 | A172699 | 48.84 | medium_review | 1994-04-04 | CONSERVATORSHIP OF PERSON AND ESTAT | SCHLUETER-C | LM=5 TR=2 EX=0`
`0137 | A173296 | 48.84 | medium_review | 1994-05-13 | GUARDIANSHIP OF PERSON AND ESTATE | CLARK-M | LM=4 TR=2 EX=0`
`0138 | A174600 | 48.84 | medium_review | 1994-08-22 | LPS CONSERVATORSHIP (WI 5350) | SMITH-C | LM=6 TR=2 EX=0`
`0139 | A214204 | 48.84 | medium_review | 2002-07-01 | LPS CONSERVATORSHIP (WI 5350) | ALVARADO-LPS | LM=3 TR=2 EX=0`
`0140 | A172534 | 48.72 | medium_review | 1994-03-24 | CONSERVATORSHIP OF PERSON AND ESTAT | RUSSELL-C | LM=9 TR=9 EX=0`
`0141 | A172827 | 48.72 | medium_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | DINH-C | LM=8 TR=8 EX=0`
`0142 | A212419 | 48.72 | medium_review | 2002-03-13 | GUARDIANSHIP OF PERSON AND ESTATE | GOLDEN-M | LM=8 TR=8 EX=0`
`0143 | A172837 | 47.91 | medium_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | FRANK-C | LM=2 TR=1 EX=0`
`0144 | A172838 | 47.91 | medium_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | AYALA-C | LM=2 TR=1 EX=0`
`0145 | A173268 | 47.91 | medium_review | 1994-05-11 | LPS CONSERVATORSHIP (WI 5350) | HODGE-C | LM=2 TR=1 EX=0`
`0146 | A173613 | 47.91 | medium_review | 1994-06-09 | GUARDIANSHIP OF PERSON ONLY | CLARK-M | LM=3 TR=1 EX=0`
`0147 | A171765 | 46.86 | medium_review | 1994-01-26 | LPS CONSERVATORSHIP (WI 5350) | LOPEZ-C | LM=8 TR=6 EX=0`
`0148 | A172017 | 46.86 | medium_review | 1994-02-18 | GUARDIANSHIP OF PERSON ONLY | THOMAS JR-M | LM=8 TR=6 EX=0`
`0149 | A172035 | 46.86 | medium_review | 1994-02-22 | GUARDIANSHIP OF PERSON ONLY | MARTINEZ-M | LM=7 TR=6 EX=0`
`0150 | A172878 | 46.86 | medium_review | 1994-04-14 | CONSERVATORSHIP OF ESTATE ONLY | BENNETT-C | LM=7 TR=6 EX=0`
`0151 | A173173 | 46.86 | medium_review | 1994-05-05 | CONSERVATORSHIP OF PERSON AND ESTAT | BENNETT-C | LM=7 TR=6 EX=0`
`0152 | A173525 | 46.86 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | LEWIS-C | LM=6 TR=6 EX=0`
`0153 | A171769 | 45.93 | medium_review | 1994-01-27 | LPS CONSERVATORSHIP (WI 5350) | JACKSON-C | LM=6 TR=5 EX=0`
`0154 | A172022 | 45.93 | medium_review | 1994-02-18 | LPS CONSERVATORSHIP (WI 5350) | WILSON-C | LM=5 TR=5 EX=0`
`0155 | A173159 | 45.93 | medium_review | 1994-05-04 | LPS CONSERVATORSHIP (WI 5350) | JACKSON-C | LM=6 TR=5 EX=0`
`0156 | A173168 | 45.93 | medium_review | 1994-05-05 | GUARDIANSHIP OF PERSON ONLY | HERNANDEZ-M | LM=7 TR=5 EX=0`
`0157 | A173266 | 45.93 | medium_review | 1994-05-11 | LPS CONSERVATORSHIP (WI 5350) | HA-C | LM=5 TR=5 EX=0`
`0158 | A173524 | 45.93 | medium_review | 1994-06-03 | LPS CONSERVATORSHIP (WI 5350) | DINH-C | LM=5 TR=5 EX=0`
`0159 | A173666 | 45.93 | medium_review | 1994-06-13 | GUARDIANSHIP OF PERSON ONLY | GARCIA-M | LM=5 TR=5 EX=0`
`0160 | A171636 | 45.0 | medium_review | 1994-01-14 | LPS CONSERVATORSHIP (WI 5350) | RICHARDSON-C | LM=4 TR=4 EX=0`
`0161 | A172066 | 45.0 | medium_review | 1994-02-23 | GUARDIANSHIP OF ESTATE ONLY | RAMIREZ-M | LM=5 TR=4 EX=0`
`0162 | A172430 | 45.0 | medium_review | 1994-03-17 | LPS CONSERVATORSHIP (WI 5350) | FOX-C | LM=5 TR=4 EX=0`
`0163 | A172926 | 45.0 | medium_review | 1994-04-18 | LPS CONSERVATORSHIP (WI 5350) | WHITE-C | LM=5 TR=4 EX=0`
`0164 | A172961 | 45.0 | medium_review | 1994-04-20 | LPS CONSERVATORSHIP (WI 5350) | HUGHES-C | LM=4 TR=4 EX=0`
`0165 | A173073 | 45.0 | medium_review | 1994-04-27 | CONSERVATORSHIP OF PERSON ONLY | RUSSELL-C | LM=4 TR=4 EX=0`
`0166 | A173129 | 45.0 | medium_review | 1994-05-03 | GUARDIANSHIP OF PERSON ONLY | MARTINEZ-M | LM=4 TR=4 EX=0`
`0167 | A173130 | 45.0 | medium_review | 1994-05-03 | LPS CONSERVATORSHIP (WI 5350) | RODRIGUEZ-C | LM=4 TR=4 EX=0`
`0168 | A173274 | 45.0 | medium_review | 1994-05-12 | LPS CONSERVATORSHIP (WI 5350) | MARTINEZ-C | LM=4 TR=4 EX=0`
`0169 | A173473 | 45.0 | medium_review | 1994-05-31 | CONSERVATORSHIP OF PERSON AND ESTAT | MORGAN-C | LM=4 TR=4 EX=0`
`0170 | A173750 | 45.0 | medium_review | 1994-06-21 | GUARDIANSHIP OF ESTATE ONLY | WILSON-M | LM=4 TR=4 EX=0`
`0171 | A173915 | 45.0 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | BROWN-C | LM=4 TR=4 EX=0`
`0172 | A173930 | 45.0 | medium_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | TAYLOR-C | LM=4 TR=4 EX=0`
`0173 | A173999 | 45.0 | medium_review | 1994-07-08 | LPS CONSERVATORSHIP (WI 5350) | BROWN-C | LM=4 TR=4 EX=0`
`0174 | A174070 | 45.0 | medium_review | 1994-07-13 | LPS CONSERVATORSHIP (WI 5350) | HOANG-C | LM=4 TR=4 EX=0`
`0175 | A174130 | 45.0 | medium_review | 1994-07-19 | CONSERVATORSHIP OF PERSON AND ESTAT | MILLER-C | LM=4 TR=4 EX=0`
`0176 | A174500 | 45.0 | medium_review | 1994-08-15 | LPS CONSERVATORSHIP (WI 5350) | LEVESQUE-C | LM=4 TR=4 EX=0`
`0177 | A200435 | 45.0 | medium_review | 2000-01-03 | LPS CONSERVATORSHIP (WI 5350) | WASHINGTON-LPS | LM=4 TR=4 EX=0`
`0178 | A208278 | 45.0 | medium_review | 2001-06-13 | GUARDIANSHIP OF ESTATE ONLY | NORTH-M | LM=4 TR=4 EX=0`
`0179 | A212787 | 45.0 | medium_review | 2002-04-04 | CONSERVATORSHIP OF PERSON ONLY | AMESCUA-C | LM=5 TR=4 EX=0`
`0180 | A171831 | 44.07 | low_review | 1994-02-02 | CONSERVATORSHIP OF PERSON AND ESTAT | BROOKS-C | LM=3 TR=3 EX=0`
`0181 | A171843 | 44.07 | low_review | 1994-02-03 | CONSERVATORSHIP OF PERSON ONLY | BLACK-C | LM=4 TR=3 EX=0`
`0182 | A171901 | 44.07 | low_review | 1994-02-09 | LPS CONSERVATORSHIP (WI 5350) | WARD-C | LM=3 TR=3 EX=0`
`0183 | A172438 | 44.07 | low_review | 1994-03-18 | LPS CONSERVATORSHIP (WI 5350) | ALVAREZ-C | LM=4 TR=3 EX=0`
`0184 | A172601 | 44.07 | low_review | 1994-03-29 | LPS CONSERVATORSHIP (WI 5350) | BUTLER-C | LM=4 TR=3 EX=0`
`0185 | A172782 | 44.07 | low_review | 1994-04-08 | LPS CONSERVATORSHIP (WI 5350) | WRIGHT-C | LM=3 TR=3 EX=0`
`0186 | A172870 | 44.07 | low_review | 1994-04-14 | CONSERVATORSHIP OF PERSON AND ESTAT | REYNOLDS-C | LM=3 TR=3 EX=0`
`0187 | A172928 | 44.07 | low_review | 1994-04-18 | LPS CONSERVATORSHIP (WI 5350) | GARDNER-C | LM=3 TR=3 EX=0`
`0188 | A173077 | 44.07 | low_review | 1994-04-27 | LIMITED CONSERVATORSHIP OF PERSON O | GARDNER-LIMITED CONSERVATORSHIP | LM=3 TR=3 EX=0`
`0189 | A173335 | 44.07 | low_review | 1994-05-17 | GUARDIANSHIP OF ESTATE ONLY | ROBERTS-M | LM=4 TR=3 EX=0`
`0190 | A173877 | 44.07 | low_review | 1994-06-29 | CONSERVATORSHIP OF PERSON AND ESTAT | HUGHES-C | LM=3 TR=3 EX=0`
`0191 | A174307 | 44.07 | low_review | 1994-08-01 | LPS CONSERVATORSHIP (WI 5350) | SAMUELSON-C | LM=3 TR=3 EX=0`
`0192 | A174331 | 44.07 | low_review | 1994-08-02 | GUARDIANSHIP OF PERSON ONLY | BROWN-M | LM=3 TR=3 EX=0`
`0193 | A212278 | 44.07 | low_review | 2002-03-04 | LPS CONSERVATORSHIP (WI 5350) | DUONG-LPS | LM=4 TR=3 EX=0`
`0194 | A213127 | 44.07 | low_review | 2002-04-25 | CONSERVATORSHIP OF PERSON AND ESTAT | ELLIS-C | LM=3 TR=3 EX=0`
`0195 | A171738 | 43.14 | low_review | 1994-01-25 | LPS CONSERVATORSHIP (WI 5350) | HOLLADAY-C | LM=4 TR=2 EX=0`
`0196 | A172019 | 43.14 | low_review | 1994-02-18 | CONSERVATORSHIP OF PERSON AND ESTAT | OLSON-C | LM=4 TR=2 EX=0`
`0197 | A172079 | 43.14 | low_review | 1994-02-24 | LPS CONSERVATORSHIP (WI 5350) | PETERSON-C | LM=2 TR=2 EX=0`
`0198 | A172082 | 43.14 | low_review | 1994-02-24 | LPS CONSERVATORSHIP (WI 5350) | MORENO-C | LM=4 TR=2 EX=0`
`0199 | A172105 | 43.14 | low_review | 1994-02-25 | GUARDIANSHIP OF PERSON ONLY | ZRINSKI-M | LM=3 TR=2 EX=0`
`0200 | A172144 | 43.14 | low_review | 1994-03-01 | CONSERVATORSHIP OF PERSON AND ESTAT | WALSH-C | LM=4 TR=2 EX=0`
`0201 | A172270 | 43.14 | low_review | 1994-03-08 | CONSERVATORSHIP OF PERSON AND ESTAT | PLAVAN-C | LM=2 TR=2 EX=0`
`0202 | A172448 | 43.14 | low_review | 1994-03-18 | GUARDIANSHIP OF PERSON AND ESTATE | DI SALVO-M | LM=4 TR=2 EX=0`
`0203 | A172488 | 43.14 | low_review | 1994-03-22 | LPS CONSERVATORSHIP (WI 5350) | MENDOZA-C | LM=2 TR=2 EX=0`
`0204 | A172495 | 43.14 | low_review | 1994-03-22 | LPS CONSERVATORSHIP (WI 5350) | CAMPOS-C | LM=2 TR=2 EX=0`
`0205 | A172736 | 43.14 | low_review | 1994-04-06 | CONSERVATORSHIP OF ESTATE ONLY | HASBROUCK-C | LM=2 TR=2 EX=0`
`0206 | A172849 | 43.14 | low_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | DAHM-C | LM=2 TR=2 EX=0`
`0207 | A172921 | 43.14 | low_review | 1994-04-18 | LPS CONSERVATORSHIP (WI 5350) | CARTER-C | LM=3 TR=2 EX=0`
`0208 | A173024 | 43.14 | low_review | 1994-04-22 | LPS CONSERVATORSHIP (WI 5350) | PERKINS-C | LM=2 TR=2 EX=0`
`0209 | A173204 | 43.14 | low_review | 1994-05-09 | CONSERVATORSHIP OF PERSON AND ESTAT | REYNOLDS-C | LM=2 TR=2 EX=0`
`0210 | A173422 | 43.14 | low_review | 1994-05-24 | CONSERVATORSHIP OF PERSON AND ESTAT | TUCKER-D | LM=2 TR=2 EX=0`
`0211 | A173782 | 43.14 | low_review | 1994-06-22 | CONSERVATORSHIP OF PERSON AND ESTAT | PENROD-C | LM=2 TR=2 EX=0`
`0212 | A173798 | 43.14 | low_review | 1994-06-23 | CONSERVATORSHIP OF PERSON AND ESTAT | DOAN-C | LM=2 TR=2 EX=0`
`0213 | A173811 | 43.14 | low_review | 1994-06-24 | LPS CONSERVATORSHIP (WI 5350) | RAMOS-C | LM=2 TR=2 EX=0`
`0214 | A174031 | 43.14 | low_review | 1994-07-11 | LPS CONSERVATORSHIP (WI 5350) | ROCHE-C | LM=2 TR=2 EX=0`
`0215 | A174158 | 43.14 | low_review | 1994-07-20 | LPS CONSERVATORSHIP (WI 5350) | SCOTT-C | LM=2 TR=2 EX=0`
`0216 | A174303 | 43.14 | low_review | 1994-07-29 | LIMITED CONSERVATORSHIP OF PERSON O | LEE-C | LM=3 TR=2 EX=0`
`0217 | A174654 | 43.14 | low_review | 1994-08-25 | GUARDIANSHIP OF ESTATE ONLY | WILSON-M | LM=2 TR=2 EX=0`
`0218 | A174958 | 43.14 | low_review | 1994-09-19 | LPS CONSERVATORSHIP (WI 5350) | THOMPSON-C | LM=2 TR=2 EX=0`
`0219 | A175132 | 43.14 | low_review | 1994-09-30 | GUARDIANSHIP OF PERSON ONLY | JOHNSON-M | LM=2 TR=2 EX=0`
`0220 | A176148 | 43.14 | low_review | 1994-12-28 | LPS CONSERVATORSHIP (WI 5350) | ROBINSON-C | LM=2 TR=2 EX=0`
`0221 | A177439 | 43.14 | low_review | 1995-04-06 | GUARDIANSHIP OF PERSON ONLY | WELLS/JORDAN-M | LM=2 TR=2 EX=0`
`0222 | A177677 | 43.14 | low_review | 1995-04-25 | LPS CONSERVATORSHIP (WI 5350) | WELLS-C | LM=2 TR=2 EX=0`
`0223 | A184051 | 43.14 | low_review | 1996-08-21 | LPS CONSERVATORSHIP (WI 5350) | MC CONNELL-C | LM=2 TR=2 EX=0`
`0224 | A184446 | 43.14 | low_review | 1996-09-20 | CONSERVATORSHIP OF PERSON AND ESTAT | WELLS-C | LM=2 TR=2 EX=0`
`0225 | A185939 | 43.14 | low_review | 1997-01-24 | LPS CONSERVATORSHIP (WI 5350) | KRAMER-C | LM=2 TR=2 EX=0`
`0226 | A189240 | 43.14 | low_review | 1997-09-24 | LPS CONSERVATORSHIP (WI 5350) | DOWNEY-C | LM=2 TR=2 EX=0`
`0227 | A191736 | 43.14 | low_review | 1998-04-02 | LPS CONSERVATORSHIP (WI 5350) | FRANKLIN-C | LM=2 TR=2 EX=0`
`0228 | A192179 | 43.14 | low_review | 1998-05-05 | CONSERVATORSHIP OF PERSON ONLY | FRANKLIN-C | LM=2 TR=2 EX=0`
`0229 | A192336 | 43.14 | low_review | 1998-05-14 | GUARDIANSHIP OF PERSON AND ESTATE | CHASE-M | LM=2 TR=2 EX=0`
`0230 | A193905 | 43.14 | low_review | 1998-09-02 | LPS CONSERVATORSHIP (WI 5350) | WELLS-C | LM=2 TR=2 EX=0`
`0231 | A204076 | 43.14 | low_review | 2000-09-08 | GUARDIANSHIP OF PERSON ONLY | STONE-M | LM=2 TR=2 EX=0`
`0232 | A208007 | 43.14 | low_review | 2001-05-30 | CONSERVATORSHIP OF PERSON AND ESTAT | JOHN-C | LM=2 TR=2 EX=0`
`0233 | A211230 | 43.14 | low_review | 2001-12-24 | LPS CONSERVATORSHIP (WI 5350) | GATES-LPS | LM=2 TR=2 EX=0`
`0234 | A212019 | 43.14 | low_review | 2002-02-15 | LPS CONSERVATORSHIP (WI 5350) | PARK-LPS | LM=2 TR=2 EX=0`
`0235 | A212750 | 43.14 | low_review | 2002-04-02 | GUARDIANSHIP OF PERSON ONLY | CARR-M | LM=2 TR=2 EX=0`
`0236 | A212924 | 43.14 | low_review | 2002-04-12 | LPS CONSERVATORSHIP (WI 5350) | TRUONG-LPS | LM=2 TR=2 EX=0`
`0237 | A172218 | 42.89 | low_review | 1994-03-04 | DETERMINE SUCCESSION TO PRIMARY RES | MCLEOD-D | LM=16 TR=8 EX=0`
`0238 | A171535 | 42.21 | low_review | 1994-01-06 | GUARDIANSHIP OF PERSON ONLY | CONTRERAS-M | LM=1 TR=1 EX=0`
`0239 | A171713 | 42.21 | low_review | 1994-01-21 | LPS CONSERVATORSHIP (WI 5350) | NEEDHAM-C | LM=1 TR=1 EX=0`
`0240 | A171796 | 42.21 | low_review | 1994-01-31 | LPS CONSERVATORSHIP (WI 5350) | MEYER-C | LM=1 TR=1 EX=0`
`0241 | A171894 | 42.21 | low_review | 1994-02-08 | CONSERVATORSHIP OF PERSON AND ESTAT | HUNT-C | LM=1 TR=1 EX=0`
`0242 | A171943 | 42.21 | low_review | 1994-02-14 | CONSERVATORSHIP OF ESTATE ONLY | NOVAK-C | LM=1 TR=1 EX=0`
`0243 | A171950 | 42.21 | low_review | 1994-02-15 | CONSERVATORSHIP OF ESTATE ONLY | MEYERS-C | LM=1 TR=1 EX=0`
`0244 | A171952 | 42.21 | low_review | 1994-02-15 | LPS CONSERVATORSHIP (WI 5350) | RAVELLETTE-C | LM=1 TR=1 EX=0`
`0245 | A172151 | 42.21 | low_review | 1994-03-01 | CONSERVATORSHIP OF PERSON AND ESTAT | DODGE-C | LM=1 TR=1 EX=0`
`0246 | A172193 | 42.21 | low_review | 1994-03-03 | GUARDIANSHIP OF PERSON AND ESTATE | YOUNG-T | LM=1 TR=1 EX=0`
`0247 | A172244 | 42.21 | low_review | 1994-03-07 | LIMITED CONSERVATORSHIP OF PERSON O | PIERCE-C | LM=1 TR=1 EX=0`
`0248 | A172246 | 42.21 | low_review | 1994-03-07 | LIMITED CONSERVATORSHIP OF PERSON O | SUMNER-C | LM=1 TR=1 EX=0`
`0249 | A172331 | 42.21 | low_review | 1994-03-11 | CONSERVATORSHIP OF PERSON AND ESTAT | CABALFIN-C | LM=1 TR=1 EX=0`
`0250 | A172421 | 42.21 | low_review | 1994-03-17 | CONSERVATORSHIP OF ESTATE ONLY | LITTLE-C | LM=1 TR=1 EX=0`
`0251 | A172446 | 42.21 | low_review | 1994-03-18 | CONSERVATORSHIP OF ESTATE ONLY | BLOOM-C | LM=1 TR=1 EX=0`
`0252 | A172600 | 42.21 | low_review | 1994-03-29 | LPS CONSERVATORSHIP (WI 5350) | SPEAR-C | LM=1 TR=1 EX=0`
`0253 | A172649 | 42.21 | low_review | 1994-04-01 | CONSERVATORSHIP OF PERSON ONLY | HUNT-C | LM=1 TR=1 EX=0`
`0254 | A172763 | 42.21 | low_review | 1994-04-07 | LPS CONSERVATORSHIP (WI 5350) | STOCKER-C | LM=1 TR=1 EX=0`
`0255 | A172836 | 42.21 | low_review | 1994-04-12 | LPS CONSERVATORSHIP (WI 5350) | WATERS-C | LM=1 TR=1 EX=0`
`0256 | A172945 | 42.21 | low_review | 1994-04-19 | CONSERVATORSHIP OF PERSON ONLY | ORR-C | LM=1 TR=1 EX=0`
`0257 | A173132 | 42.21 | low_review | 1994-05-03 | LPS CONSERVATORSHIP (WI 5350) | SOTO-C | LM=1 TR=1 EX=0`
`0258 | A173273 | 42.21 | low_review | 1994-05-11 | CONSERVATORSHIP OF PERSON AND ESTAT | GOMEZ-C | LM=2 TR=1 EX=0`
`0259 | A173322 | 42.21 | low_review | 1994-05-16 | CONSERVATORSHIP OF PERSON AND ESTAT | DAWSON-C | LM=2 TR=1 EX=0`
`0260 | A173356 | 42.21 | low_review | 1994-05-18 | LPS CONSERVATORSHIP (WI 5350) | RYAN-C | LM=1 TR=1 EX=0`
`0261 | A173358 | 42.21 | low_review | 1994-05-18 | LPS CONSERVATORSHIP (WI 5350) | YI-C | LM=1 TR=1 EX=0`
`0262 | A173445 | 42.21 | low_review | 1994-05-26 | LPS CONSERVATORSHIP (WI 5350) | LLOYD-C | LM=1 TR=1 EX=0`
`0263 | A173447 | 42.21 | low_review | 1994-05-27 | GUARDIANSHIP OF PERSON ONLY | VON WEIGERT-M | LM=1 TR=1 EX=0`
`0264 | A173644 | 42.21 | low_review | 1994-06-10 | GUARDIANSHIP OF PERSON AND ESTATE | RICHARDSON-M | LM=2 TR=1 EX=0`
`0265 | A173648 | 42.21 | low_review | 1994-06-13 | LPS CONSERVATORSHIP (WI 5350) | THOMAS-C | LM=2 TR=1 EX=0`
`0266 | A173759 | 42.21 | low_review | 1994-06-22 | LPS CONSERVATORSHIP (WI 5350) | LOPEZ-C | LM=1 TR=1 EX=0`
`0267 | A173818 | 42.21 | low_review | 1994-06-24 | LPS CONSERVATORSHIP (WI 5350) | ALVARADO-C | LM=1 TR=1 EX=0`
`0268 | A173920 | 42.21 | low_review | 1994-07-01 | LPS CONSERVATORSHIP (WI 5350) | DIEHL-C | LM=1 TR=1 EX=0`
`0269 | A174193 | 42.21 | low_review | 1994-07-21 | CONSERVATORSHIP OF PERSON AND ESTAT | VAN NESS-C | LM=2 TR=1 EX=0`
`0270 | A174194 | 42.21 | low_review | 1994-07-21 | CONSERVATORSHIP OF PERSON AND ESTAT | VAN NESS-C | LM=2 TR=1 EX=0`
`0271 | A174216 | 42.21 | low_review | 1994-07-22 | GUARDIANSHIP OF PERSON ONLY | JACKSON-M | LM=1 TR=1 EX=0`
`0272 | A174238 | 42.21 | low_review | 1994-07-26 | GUARDIANSHIP OF PERSON ONLY | CARR-M | LM=2 TR=1 EX=0`
`0273 | A174267 | 42.21 | low_review | 1994-07-28 | LPS CONSERVATORSHIP (WI 5350) | HA-C | LM=1 TR=1 EX=0`
`0274 | A174302 | 42.21 | low_review | 1994-07-29 | LIMITED CONSERVATORSHIP OF PERSON O | HUFF-C | LM=1 TR=1 EX=0`
`0275 | A174311 | 42.21 | low_review | 1994-08-01 | LPS CONSERVATORSHIP (WI 5350) | ROSENAST-C | LM=2 TR=1 EX=0`
`0276 | A174646 | 42.21 | low_review | 1994-08-24 | LPS CONSERVATORSHIP (WI 5350) | LOPEZ-C | LM=1 TR=1 EX=0`
`0277 | A174705 | 42.21 | low_review | 1994-08-30 | CONSERVATORSHIP OF PERSON AND ESTAT | LONG-C | LM=1 TR=1 EX=0`
`0278 | A174823 | 42.21 | low_review | 1994-09-08 | CONSERVATORSHIP OF PERSON ONLY | BROWN-C | LM=1 TR=1 EX=0`
`0279 | A174837 | 42.21 | low_review | 1994-09-09 | GUARDIANSHIP OF PERSON AND ESTATE | FRENCH-M | LM=1 TR=1 EX=0`
`0280 | A174859 | 42.21 | low_review | 1994-09-12 | LPS CONSERVATORSHIP (WI 5350) | MITCHELL-C | LM=1 TR=1 EX=0`
`0281 | A175608 | 42.21 | low_review | 1994-11-09 | LPS CONSERVATORSHIP (WI 5350) | GARCIA-C | LM=1 TR=1 EX=0`
`0282 | A175701 | 42.21 | low_review | 1994-11-18 | LPS CONSERVATORSHIP (WI 5350) | FRENCH-C | LM=1 TR=1 EX=0`
`0283 | A175771 | 42.21 | low_review | 1994-11-23 | LPS CONSERVATORSHIP (WI 5350) | FRENCH-C | LM=1 TR=1 EX=0`
`0284 | A175894 | 42.21 | low_review | 1994-12-06 | GUARDIANSHIP OF PERSON AND ESTATE | FLORES-M | LM=1 TR=1 EX=0`
`0285 | A175908 | 42.21 | low_review | 1994-12-07 | CONSERVATORSHIP OF PERSON AND ESTAT | DE LEON-C | LM=1 TR=1 EX=0`
`0286 | A175982 | 42.21 | low_review | 1994-12-12 | LPS CONSERVATORSHIP (WI 5350) | MARTINEZ-C | LM=1 TR=1 EX=0`
`0287 | A176400 | 42.21 | low_review | 1995-01-18 | CONSERVATORSHIP OF PERSON AND ESTAT | HAMILTON-C | LM=1 TR=1 EX=0`
`0288 | A177122 | 42.21 | low_review | 1995-03-15 | LPS CONSERVATORSHIP (WI 5350) | GONZALES-C | LM=1 TR=1 EX=0`
`0289 | A177513 | 42.21 | low_review | 1995-04-11 | GUARDIANSHIP OF PERSON AND ESTATE | GONZALES-M | LM=1 TR=1 EX=0`
`0290 | A177567 | 42.21 | low_review | 1995-04-14 | GUARDIANSHIP OF PERSON AND ESTATE | GONZALES-M | LM=1 TR=1 EX=0`
`0291 | A177741 | 42.21 | low_review | 1995-04-28 | LPS CONSERVATORSHIP (WI 5350) | PHAM-C | LM=1 TR=1 EX=0`
`0292 | A177934 | 42.21 | low_review | 1995-05-11 | CONSERVATORSHIP OF PERSON AND ESTAT | DE LA ROCHA-C | LM=1 TR=1 EX=0`
`0293 | A178114 | 42.21 | low_review | 1995-05-23 | GUARDIANSHIP OF ESTATE ONLY | SANCHEZ-M | LM=1 TR=1 EX=0`
`0294 | A178246 | 42.21 | low_review | 1995-06-02 | LPS CONSERVATORSHIP (WI 5350) | WILSON-C | LM=1 TR=1 EX=0`
`0295 | A178745 | 42.21 | low_review | 1995-07-13 | LPS CONSERVATORSHIP (WI 5350) | IRVINE-C | LM=1 TR=1 EX=0`
`0296 | A178927 | 42.21 | low_review | 1995-07-26 | CONSERVATORSHIP OF PERSON ONLY | PHAM-C | LM=1 TR=1 EX=0`
`0297 | A180372 | 42.21 | low_review | 1995-11-15 | LPS CONSERVATORSHIP (WI 5350) | DOLAN-C | LM=1 TR=1 EX=0`
`0298 | A180505 | 42.21 | low_review | 1995-11-28 | LPS CONSERVATORSHIP (WI 5350) | BROWN-C | LM=1 TR=1 EX=0`
`0299 | A183299 | 42.21 | low_review | 1996-07-01 | LPS CONSERVATORSHIP (WI 5350) | BARRETT-C | LM=1 TR=1 EX=0`
`0300 | A183543 | 42.21 | low_review | 1996-07-19 | LPS CONSERVATORSHIP (WI 5350) | PHILLIPS-C | LM=2 TR=1 EX=0`
`0301 | A184398 | 42.21 | low_review | 1996-09-18 | LPS CONSERVATORSHIP (WI 5350) | KING-C | LM=1 TR=1 EX=0`
`0302 | A185046 | 42.21 | low_review | 1996-11-06 | LPS CONSERVATORSHIP (WI 5350) | REED-C | LM=1 TR=1 EX=0`
`0303 | A185911 | 42.21 | low_review | 1997-01-23 | LPS CONSERVATORSHIP (WI 5350) | SCHULTZ-C | LM=1 TR=1 EX=0`
`0304 | A187153 | 42.21 | low_review | 1997-04-22 | CONSERVATORSHIP OF ESTATE ONLY | DOMINGUEZ-C | LM=1 TR=1 EX=0`
`0305 | A187483 | 42.21 | low_review | 1997-05-15 | GUARDIANSHIP OF PERSON ONLY | OROZCO-M | LM=1 TR=1 EX=0`
`0306 | A188301 | 42.21 | low_review | 1997-07-16 | LPS CONSERVATORSHIP (WI 5350) | BURNS-C | LM=1 TR=1 EX=0`
`0307 | A189104 | 42.21 | low_review | 1997-09-15 | GUARDIANSHIP OF PERSON AND ESTATE | FISHER-M | LM=1 TR=1 EX=0`
`0308 | A190314 | 42.21 | low_review | 1997-12-11 | LPS CONSERVATORSHIP (WI 5350) | JAMES-C | LM=1 TR=1 EX=0`
`0309 | A190476 | 42.21 | low_review | 1997-12-30 | GUARDIANSHIP OF PERSON AND ESTATE | ARNOLD-M | LM=1 TR=1 EX=0`
`0310 | A190980 | 42.21 | low_review | 1998-02-05 | GUARDIANSHIP OF PERSON ONLY | PARKER-M | LM=1 TR=1 EX=0`
`0311 | A192201 | 42.21 | low_review | 1998-05-06 | GUARDIANSHIP OF PERSON ONLY | WATSON-M | LM=1 TR=1 EX=0`
`0312 | A192633 | 42.21 | low_review | 1998-06-02 | LPS CONSERVATORSHIP (WI 5350) | JACOBS-C | LM=1 TR=1 EX=0`
`0313 | A192766 | 42.21 | low_review | 1998-06-12 | LPS CONSERVATORSHIP (WI 5350) | ROSS-C | LM=1 TR=1 EX=0`
`0314 | A196140 | 42.21 | low_review | 1999-03-02 | GUARDIANSHIP OF PERSON ONLY | ROSE-M | LM=1 TR=1 EX=0`
`0315 | A198624 | 42.21 | low_review | 1999-08-24 | GUARDIANSHIP OF PERSON AND ESTATE | LAWSON-M | LM=1 TR=1 EX=0`
`0316 | A199754 | 42.21 | low_review | 1999-11-12 | LPS CONSERVATORSHIP (WI 5350) | MORGAN-LPS | LM=1 TR=1 EX=0`
`0317 | A201222 | 42.21 | low_review | 2000-02-24 | GUARDIANSHIP OF ESTATE ONLY | STANSFIELD-M | LM=1 TR=1 EX=0`
`0318 | A206460 | 42.21 | low_review | 2001-02-26 | LPS CONSERVATORSHIP (WI 5350) | LASALLE-LPS | LM=1 TR=1 EX=0`
`0319 | A210357 | 42.21 | low_review | 2001-10-19 | GUARDIANSHIP OF PERSON ONLY | JENSEN-M | LM=1 TR=1 EX=0`
`0320 | 30-2009-00272352-PR-CP-CMC | 42.21 | low_review | 2001-11-21 | CONSERVATORSHIP OF PERSON AND ESTAT | TODD-CONSERVATORSHIP | LM=1 TR=1 EX=0`
`0321 | A210862 | 42.21 | low_review | 2001-11-27 | LIMITED CONSERVATORSHIP OF PERSON O | GREENE-LIMITED CONSERVATORSHIP | LM=1 TR=1 EX=0`
`0322 | A246039 | 42.21 | low_review | 2001-12-07 | CONSERVATORSHIP OF PERSON ONLY | HAYES-C | LM=1 TR=1 EX=0`
`0323 | A211343 | 42.21 | low_review | 2002-01-03 | GUARDIANSHIP OF PERSON AND ESTATE | DEAN-M | LM=1 TR=1 EX=0`
`0324 | A211493 | 42.21 | low_review | 2002-01-14 | LPS CONSERVATORSHIP (WI 5350) | RHOADES-LPS | LM=1 TR=1 EX=0`
`0325 | A211810 | 42.21 | low_review | 2002-01-31 | LPS CONSERVATORSHIP (WI 5350) | HAMPTON-LPS | LM=1 TR=1 EX=0`
`0326 | A211899 | 42.21 | low_review | 2002-02-08 | LPS CONSERVATORSHIP (WI 5350) | LY-LPS | LM=1 TR=1 EX=0`
`0327 | A212018 | 42.21 | low_review | 2002-02-13 | LPS CONSERVATORSHIP (WI 5350) | HARRINGTON-LPS | LM=1 TR=1 EX=0`
`0328 | A212026 | 42.21 | low_review | 2002-02-15 | LPS CONSERVATORSHIP (WI 5350) | PIERCE-LPS | LM=1 TR=1 EX=0`
`0329 | A212244 | 42.21 | low_review | 2002-03-01 | LPS CONSERVATORSHIP (WI 5350) | KELLEY-LPS | LM=1 TR=1 EX=0`
`0330 | A212656 | 42.21 | low_review | 2002-03-28 | GUARDIANSHIP OF PERSON ONLY | TA-M | LM=1 TR=1 EX=0`
`0331 | A212925 | 42.21 | low_review | 2002-04-12 | LPS CONSERVATORSHIP (WI 5350) | HARRINGTON-LPS | LM=1 TR=1 EX=0`
`0332 | A212918 | 42.21 | low_review | 2002-04-15 | GUARDIANSHIP OF PERSON ONLY | FARMER-M | LM=1 TR=1 EX=0`
`0333 | A212966 | 42.21 | low_review | 2002-04-17 | LPS CONSERVATORSHIP (WI 5350) | WEAVER-LPS | LM=1 TR=1 EX=0`
`0334 | A213042 | 42.21 | low_review | 2002-04-19 | LPS CONSERVATORSHIP (WI 5350) | PALMER-LPS | LM=1 TR=1 EX=0`
`0335 | A213134 | 42.21 | low_review | 2002-04-26 | CONSERVATORSHIP OF PERSON AND ESTAT | BLASINGAME-C | LM=1 TR=1 EX=0`
`0336 | A213161 | 42.21 | low_review | 2002-04-26 | LPS CONSERVATORSHIP (WI 5350) | KEYS-LPS | LM=1 TR=1 EX=0`
`0337 | A213191 | 42.21 | low_review | 2002-04-30 | CONSERVATORSHIP OF PERSON AND ESTAT | SNYDER-C | LM=1 TR=1 EX=0`
`0338 | A213298 | 42.21 | low_review | 2002-05-06 | LPS CONSERVATORSHIP (WI 5350) | LYNCH-LPS | LM=1 TR=1 EX=0`
`0339 | A213496 | 42.21 | low_review | 2002-05-20 | GUARDIANSHIP OF PERSON ONLY | BUCHANAN-MINOR | LM=1 TR=1 EX=0`
`0340 | A213822 | 42.21 | low_review | 2002-06-11 | GUARDIANSHIP OF PERSON ONLY | ROBERTO-MINOR | LM=1 TR=1 EX=0`
`0341 | A214271 | 42.21 | low_review | 2002-07-05 | LPS CONSERVATORSHIP (WI 5350) | MEREDITH-LPS | LM=1 TR=1 EX=0`
`0342 | A214273 | 42.21 | low_review | 2002-07-09 | GUARDIANSHIP OF PERSON ONLY | KELLEY-M | LM=1 TR=1 EX=0`
`0343 | A214485 | 42.21 | low_review | 2002-07-19 | GUARDIANSHIP OF ESTATE ONLY | LIND-MINORS | LM=1 TR=1 EX=0`
`0344 | A214498 | 42.21 | low_review | 2002-07-19 | LPS CONSERVATORSHIP (WI 5350) | RIVAS-LPS | LM=1 TR=1 EX=0`
`0345 | A214564 | 42.21 | low_review | 2002-07-25 | GUARDIANSHIP OF PERSON ONLY | DALE-M | LM=1 TR=1 EX=0`
`0346 | A215397 | 42.21 | low_review | 2002-09-12 | LPS CONSERVATORSHIP (WI 5350) | RIVAS-LPS | LM=1 TR=1 EX=0`
`0347 | A172540 | 41.4 | low_review | 1994-03-25 | PROBATE OF WILL - LETTERS TESTAMENT | HAMLIN-D | LM=16 TR=9 EX=0`
`0348 | A172147 | 40.84 | low_review | 1994-03-01 | LPS CONSERVATORSHIP (WI 5350) | STEWART-C | LM=196 TR=4 EX=0`
`0349 | A171589 | 40.1 | low_review | 1994-01-11 | DETERMINE SUCCESSION TO PRIMARY RES | MCDONALD-D | LM=83 TR=57 EX=0`
`0350 | A171609 | 40.1 | low_review | 1994-01-12 | DETERMINE SUCCESSION TO PRIMARY RES | STOUT-D | LM=62 TR=42 EX=0`
`0351 | A171623 | 40.1 | low_review | 1994-01-13 | PROBATE OF WILL - LETTERS TESTAMENT | MCKINNEY-D | LM=26 TR=13 EX=0`
`0352 | A171624 | 40.1 | low_review | 1994-01-13 | PROBATE OF WILL - LETTERS TESTAMENT | BUCHANAN-D | LM=87 TR=57 EX=0`
`0353 | A171709 | 40.1 | low_review | 1994-01-21 | PROBATE OF WILL - LETTERS TESTAMENT | GUILLEN-D | LM=86 TR=62 EX=0`
`0354 | A171892 | 40.1 | low_review | 1994-02-08 | PROBATE OF WILL - LETTERS TESTAMENT | MURILLO-D | LM=82 TR=54 EX=0`
`0355 | A172016 | 40.1 | low_review | 1994-02-18 | PROBATE OF WILL - LETTERS TESTAMENT | BRANSON-D | LM=42 TR=28 EX=0`
`0356 | A172204 | 40.1 | low_review | 1994-03-03 | PROBATE OF WILL - LETTERS TESTAMENT | JUNG-D | LM=95 TR=65 EX=0`
`0357 | A172307 | 40.1 | low_review | 1994-03-10 | DETERMINE SUCCESSION TO PRIMARY RES | MADRID-D | LM=80 TR=49 EX=0`
`0358 | A172479 | 40.1 | low_review | 1994-03-22 | LETTERS OF ADMINISTRATION | SHAPIRO-D | LM=83 TR=52 EX=0`
`0359 | A172576 | 40.1 | low_review | 1994-03-28 | LETTERS OF ADMINISTRATION | BLANCO-D | LM=39 TR=26 EX=0`
`0360 | A172587 | 40.1 | low_review | 1994-03-29 | LETTERS OF ADMINISTRATION | RICHTER-D | LM=74 TR=46 EX=0`
`0361 | A172774 | 40.1 | low_review | 1994-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | RAYMOND-D | LM=62 TR=40 EX=0`
`0362 | A172834 | 40.1 | low_review | 1994-04-12 | PROBATE OF WILL  - LETTERS OF ADMIN | FELDMAN-D | LM=71 TR=45 EX=0`
`0363 | A174169 | 40.1 | low_review | 1994-07-21 | PROBATE OF WILL - LETTERS TESTAMENT | JOHNSTON-D | LM=97 TR=68 EX=0`
`0364 | A171741 | 39.92 | low_review | 1994-01-25 | OTHER PROBATE MATTER | HAROLD-M | LM=20 TR=9 EX=0`
`0365 | A172107 | 39.85 | low_review | 1994-02-25 | LETTERS OF ADMINISTRATION | PRATT-D | LM=79 TR=59 EX=0`
`0366 | A172537 | 39.85 | low_review | 1994-03-24 | TRUST PROCEEDINGS | STARK-T | LM=66 TR=42 EX=0`
`0367 | A173416 | 39.85 | low_review | 1994-05-24 | PROBATE OF WILL - LETTERS TESTAMENT | NORRIS-D | LM=50 TR=28 EX=0`
`0368 | A173591 | 39.85 | low_review | 1994-06-08 | PROBATE OF WILL - LETTERS TESTAMENT | WADE-D | LM=58 TR=37 EX=0`
`0369 | A171784 | 39.17 | low_review | 1994-01-28 | PROBATE OF WILL - LETTERS TESTAMENT | MOORE-D | LM=14 TR=10 EX=0`
`0370 | A172202 | 39.17 | low_review | 1994-03-03 | PROBATE OF WILL - LETTERS TESTAMENT | LEE-D | LM=16 TR=12 EX=0`
`0371 | A172358 | 39.17 | low_review | 1994-03-15 | SPOUSAL PROPERTY | **LEE-D CONSOL INTO A170041 | LM=16 TR=12 EX=0`
`0372 | A172819 | 39.17 | low_review | 1994-04-11 | LETTERS OF ADMINISTRATION | GURNEY-D | LM=16 TR=11 EX=0`
`0373 | A172028 | 39.11 | low_review | 1994-02-18 | PROBATE OF WILL - LETTERS TESTAMENT | GRACE-D | LM=80 TR=54 EX=0`
`0374 | A172566 | 39.11 | low_review | 1994-03-28 | LETTERS OF ADMINISTRATION | GABRIEL-D | LM=62 TR=35 EX=0`
`0375 | A172570 | 39.11 | low_review | 1994-03-28 | PROBATE OF WILL - LETTERS TESTAMENT | MARVIN-D | LM=23 TR=10 EX=0`
`0376 | A172743 | 39.11 | low_review | 1994-04-07 | PROBATE OF WILL - LETTERS TESTAMENT | MCDONALD-D | LM=46 TR=33 EX=0`
`0377 | A171797 | 38.43 | low_review | 1994-01-31 | PROBATE OF WILL - LETTERS TESTAMENT | LYON-D | LM=10 TR=8 EX=0`
`0378 | A172041 | 38.43 | low_review | 1994-02-22 | PROBATE OF WILL - LETTERS TESTAMENT | ANDERSON-D | LM=17 TR=13 EX=0`
`0379 | A172291 | 38.43 | low_review | 1994-03-09 | LETTERS OF ADMINISTRATION | BEAVERS-D | LM=16 TR=9 EX=0`
`0380 | A172447 | 38.43 | low_review | 1994-03-18 | PROBATE OF WILL - LETTERS TESTAMENT | DEXTER-D | LM=16 TR=12 EX=0`
`0381 | A172759 | 38.43 | low_review | 1994-04-07 | PROBATE OF WILL - LETTERS TESTAMENT | ZINN-D | LM=16 TR=9 EX=0`
`0382 | A172989 | 38.43 | low_review | 1994-04-21 | PROBATE OF WILL - LETTERS TESTAMENT | LEE-D | LM=15 TR=12 EX=0`
`0383 | A173417 | 38.43 | low_review | 1994-05-24 | LETTERS OF ADMINISTRATION | REIMER-D | LM=17 TR=13 EX=0`
`0384 | A174530 | 38.43 | low_review | 1994-08-16 | SPOUSAL PROPERTY | WELLS-D | LM=16 TR=11 EX=0`
`0385 | A171726 | 38.36 | low_review | 1994-01-24 | OTHER PROBATE MATTER | CORRALES-M | LM=23 TR=14 EX=0`
`0386 | A171775 | 38.36 | low_review | 1994-01-27 | PROBATE OF WILL - LETTERS TESTAMENT | HAGEN-D | LM=59 TR=38 EX=0`
`0387 | A172131 | 38.36 | low_review | 1994-02-28 | PROBATE OF WILL - LETTERS TESTAMENT | HERRICK-D | LM=30 TR=20 EX=0`
`0388 | A173165 | 38.36 | low_review | 1994-05-05 | LETTERS OF ADMINISTRATION | JUNG-D | LM=61 TR=42 EX=0`
`0389 | A211243 | 38.36 | low_review | 2001-12-24 | TRUST PROCEEDINGS | REEVES-T | LM=64 TR=47 EX=0`
`0390 | A171597 | 37.68 | low_review | 1994-01-11 | PROBATE OF WILL - LETTERS TESTAMENT | FOSTER-D | LM=20 TR=19 EX=0`
`0391 | A171605 | 37.68 | low_review | 1994-01-12 | PROBATE OF WILL - LETTERS TESTAMENT | CHRISTIANSON-D | LM=17 TR=13 EX=0`
`0392 | A171818 | 37.68 | low_review | 1994-02-01 | PROBATE OF WILL - LETTERS TESTAMENT | FREDERICKS-D | LM=13 TR=9 EX=0`
`0393 | A171821 | 37.68 | low_review | 1994-02-02 | PROBATE OF WILL - LETTERS TESTAMENT | MARTIN-D | LM=14 TR=10 EX=0`
`0394 | A171948 | 37.68 | low_review | 1994-02-15 | PROBATE OF WILL - LETTERS TESTAMENT | BROWN-D | LM=15 TR=12 EX=0`
`0395 | A172159 | 37.68 | low_review | 1994-03-01 | TRUST PROCEEDINGS | BALLANTYNE-T | LM=13 TR=8 EX=0`
`0396 | A172184 | 37.68 | low_review | 1994-03-02 | LETTERS OF ADMINISTRATION | PARGA-D | LM=15 TR=13 EX=0`
`0397 | A172635 | 37.68 | low_review | 1994-03-31 | PROBATE OF WILL - LETTERS TESTAMENT | RIPPE-D | LM=19 TR=13 EX=0`
`0398 | A172673 | 37.68 | low_review | 1994-04-01 | PROBATE OF WILL - LETTERS TESTAMENT | HILLIARD-D | LM=12 TR=9 EX=0`
`0399 | A172812 | 37.68 | low_review | 1994-04-11 | PROBATE OF WILL - LETTERS TESTAMENT | SAMUELSON-D | LM=13 TR=11 EX=0`
`0400 | A173147 | 37.68 | low_review | 1994-05-04 | PROBATE OF WILL - LETTERS TESTAMENT | MADDOX-D | LM=16 TR=10 EX=0`
`0401 | A175211 | 37.68 | low_review | 1994-10-07 | PROBATE OF WILL - LETTERS TESTAMENT | O'DONNELL-D | LM=12 TR=10 EX=0`
`0402 | A175229 | 37.68 | low_review | 1994-10-11 | PROBATE OF WILL - LETTERS TESTAMENT | O'CONNOR-D | LM=12 TR=10 EX=0`
`0403 | A175898 | 37.68 | low_review | 1994-12-06 | PROBATE OF WILL - LETTERS TESTAMENT | O'DONNELL-D | LM=15 TR=14 EX=0`
`0404 | A176019 | 37.68 | low_review | 1994-12-15 | SPOUSAL PROPERTY | O'CONNELL-D | LM=18 TR=16 EX=0`
`0405 | A179849 | 37.68 | low_review | 1995-10-05 | PROBATE OF WILL  - LETTERS OF ADMIN | O'TOOLE-D | LM=18 TR=14 EX=0`
`0406 | A171770 | 37.62 | low_review | 1994-01-27 | PROBATE OF WILL  - LETTERS OF ADMIN | KRIEGER-D | LM=30 TR=19 EX=0`
`0407 | A171883 | 37.62 | low_review | 1994-02-08 | PROBATE OF WILL - LETTERS TESTAMENT | SCHUMACHER-D | LM=69 TR=45 EX=0`
`0408 | A171941 | 37.62 | low_review | 1994-02-14 | PROBATE OF WILL - LETTERS TESTAMENT | MCKENZIE-D | LM=39 TR=30 EX=0`
`0409 | A172128 | 37.62 | low_review | 1994-02-28 | PROBATE OF WILL - LETTERS TESTAMENT | TIERNEY-D | LM=38 TR=24 EX=0`
`0410 | A172129 | 37.62 | low_review | 1994-02-28 | SPOUSAL PROPERTY | CORREA-D | LM=55 TR=46 EX=0`
`0411 | A172737 | 37.62 | low_review | 1994-04-06 | LETTERS OF ADMINISTRATION | GALLOWAY-D | LM=58 TR=45 EX=0`
`0412 | A172879 | 37.62 | low_review | 1994-04-14 | LETTERS OF ADMINISTRATION | MASSEY-D | LM=65 TR=48 EX=0`
`0413 | A172885 | 37.62 | low_review | 1994-04-14 | PROBATE OF WILL - LETTERS TESTAMENT | ASH-D | LM=26 TR=15 EX=0`
`0414 | A173493 | 37.62 | low_review | 1994-06-01 | PROBATE OF WILL - LETTERS TESTAMENT | CARRANZA-D | LM=30 TR=21 EX=0`
`0415 | A173941 | 37.62 | low_review | 1994-07-05 | LETTERS OF ADMINISTRATION | MICHEL-D | LM=28 TR=18 EX=0`
`0416 | A174410 | 37.62 | low_review | 1994-08-08 | LETTERS OF ADMINISTRATION | MATTHEWS-D | LM=37 TR=25 EX=0`
`0417 | A174412 | 37.62 | low_review | 1994-08-08 | LETTERS OF ADMINISTRATION | MATTHEWS-D | LM=37 TR=25 EX=0`
`0418 | A171628 | 37.5 | low_review | 1994-01-13 | PROBATE OF WILL - LETTERS TESTAMENT | SANDIN-D | LM=11 TR=7 EX=0`
`0419 | A171777 | 37.5 | low_review | 1994-01-27 | TRUST PROCEEDINGS | STANSBURY-T | LM=13 TR=7 EX=0`
`0420 | A171868 | 37.5 | low_review | 1994-02-07 | PROBATE OF WILL - LETTERS TESTAMENT | VAN WINKLE-D | LM=13 TR=7 EX=0`
`0421 | A172742 | 37.5 | low_review | 1994-04-07 | LETTERS OF ADMINISTRATION | DOBBINS-D | LM=13 TR=7 EX=0`
`0422 | A171590 | 37.1 | low_review | 1994-01-11 | PROBATE OF WILL - LETTERS TESTAMENT | SMITH-D | LM=1 TR=0 EX=1`
`0423 | A171487 | 36.88 | low_review | 1994-01-03 | PROBATE OF WILL - LETTERS TESTAMENT | NANCE-D | LM=30 TR=19 EX=0`
`0424 | A171556 | 36.88 | low_review | 1994-01-07 | SPOUSAL PROPERTY | GOSSETT-D | LM=23 TR=10 EX=0`
`0425 | A171720 | 36.88 | low_review | 1994-01-21 | PROBATE OF WILL - LETTERS TESTAMENT | PETTIT-D | LM=43 TR=35 EX=0`
`0426 | A171855 | 36.88 | low_review | 1994-02-03 | PROBATE OF WILL - LETTERS TESTAMENT | HAYDEN-D | LM=81 TR=55 EX=0`
`0427 | A171878 | 36.88 | low_review | 1994-02-07 | REAL PROPERTY OF SMALL VALUE (PROB  | ROSENTHAL-D | LM=38 TR=29 EX=0`
`0428 | A171882 | 36.88 | low_review | 1994-02-08 | PROBATE OF WILL - LETTERS TESTAMENT | PURDY-D | LM=33 TR=26 EX=0`
`0429 | A171978 | 36.88 | low_review | 1994-02-15 | LETTERS OF ADMINISTRATION | HURD-D | LM=24 TR=16 EX=0`
`0430 | A172241 | 36.88 | low_review | 1994-03-07 | PROBATE OF WILL - LETTERS TESTAMENT | ERWIN-D | LM=57 TR=43 EX=0`
`0431 | A172755 | 36.88 | low_review | 1994-04-07 | PROBATE OF WILL - LETTERS TESTAMENT | TIERNEY-D | LM=31 TR=18 EX=0`
`0432 | A172817 | 36.88 | low_review | 1994-04-11 | PROBATE OF WILL  - LETTERS OF ADMIN | WEEKS-D | LM=26 TR=16 EX=0`
`0433 | A172868 | 36.88 | low_review | 1994-04-14 | DETERMINE SUCCESSION TO PRIMARY RES | COMSTOCK-D | LM=25 TR=14 EX=0`
`0434 | A173162 | 36.88 | low_review | 1994-05-05 | PROBATE OF WILL - LETTERS TESTAMENT | MC GRATH-D | LM=33 TR=24 EX=0`
`0435 | A173892 | 36.88 | low_review | 1994-06-30 | PROBATE OF WILL - LETTERS TESTAMENT | RAYMOND-D | LM=26 TR=15 EX=0`
`0436 | A174133 | 36.88 | low_review | 1994-07-19 | PROBATE OF WILL - LETTERS TESTAMENT | LANE-D | LM=35 TR=26 EX=0`
`0437 | A171552 | 36.75 | low_review | 1994-01-07 | LETTERS OF ADMINISTRATION | BLEECKER-D | LM=13 TR=7 EX=0`
`0438 | A172298 | 36.75 | low_review | 1994-03-09 | PROBATE OF WILL - LETTERS TESTAMENT | WILLIAMS-D | LM=11 TR=7 EX=0`
`0439 | A172424 | 36.75 | low_review | 1994-03-18 | LETTERS OF ADMINISTRATION | WILLIAMS-D | LM=11 TR=7 EX=0`
`0440 | A171845 | 36.57 | low_review | 1994-02-03 | PROBATE OF WILL - LETTERS TESTAMENT | HENNINGER-D | LM=10 TR=6 EX=0`
`0441 | A174211 | 36.57 | low_review | 1994-07-22 | LETTERS OF ADMINISTRATION | SMITH-D | LM=11 TR=6 EX=0`
`0442 | A174212 | 36.57 | low_review | 1994-07-22 | LETTERS OF ADMINISTRATION | SMITH-D | LM=11 TR=6 EX=0`
`0443 | A171489 | 36.13 | low_review | 1994-01-03 | PROBATE OF WILL - LETTERS TESTAMENT | O'BARR-D | LM=30 TR=23 EX=0`
`0444 | A171551 | 36.13 | low_review | 1994-01-07 | PROBATE OF WILL - LETTERS TESTAMENT | BEATTY-D | LM=45 TR=33 EX=0`
`0445 | A171620 | 36.13 | low_review | 1994-01-13 | PROBATE OF WILL - LETTERS TESTAMENT | CHANEY-D | LM=40 TR=28 EX=0`
`0446 | A171958 | 36.13 | low_review | 1994-02-15 | PROBATE OF WILL - LETTERS TESTAMENT | LARKIN-D | LM=46 TR=37 EX=0`
`0447 | A172257 | 36.13 | low_review | 1994-03-07 | SPOUSAL PROPERTY | O'FLYNN-D | LM=39 TR=31 EX=0`
`0448 | A172355 | 36.13 | low_review | 1994-03-15 | LETTERS OF SPECIAL ADMINISTRATION | THACKER-D | LM=31 TR=24 EX=0`
`0449 | A172402 | 36.13 | low_review | 1994-03-16 | SPOUSAL PROPERTY | O'NEILL-D | LM=40 TR=32 EX=0`
`0450 | A172518 | 36.13 | low_review | 1994-03-24 | TRUST PROCEEDINGS | HACKER-T | LM=22 TR=14 EX=0`
`0451 | A213225 | 36.13 | low_review | 2002-05-02 | PROBATE OF WILL - LETTERS TESTAMENT | VALENTINE-D | LM=82 TR=65 EX=0`
`0452 | A171816 | 36.01 | low_review | 1994-02-01 | PROBATE OF WILL - LETTERS TESTAMENT | TOW-D | LM=11 TR=3 EX=0`
`0453 | A172139 | 36.01 | low_review | 1994-02-28 | LETTERS OF SPECIAL ADMINISTRATION | BENAVIDEZ-D | LM=9 TR=3 EX=0`
`0454 | A171606 | 35.82 | low_review | 1994-01-12 | PROBATE OF WILL - LETTERS TESTAMENT | HELLMAN-D | LM=10 TR=6 EX=0`
`0455 | A171980 | 35.82 | low_review | 1994-02-15 | PROBATE OF WILL - LETTERS TESTAMENT | ROGERS-D | LM=8 TR=6 EX=0`
`0456 | A172234 | 35.82 | low_review | 1994-03-07 | REAL PROPERTY OF SMALL VALUE (PROB  | DICE-D | LM=9 TR=6 EX=0`
`0457 | A172596 | 35.82 | low_review | 1994-03-29 | LETTERS OF ADMINISTRATION | WILLOUGHBY-D | LM=7 TR=6 EX=0`
`0458 | A172646 | 35.82 | low_review | 1994-04-01 | LETTERS OF ADMINISTRATION | FLORES-D | LM=7 TR=6 EX=0`
`0459 | A172884 | 35.82 | low_review | 1994-04-14 | PROBATE OF WILL - LETTERS TESTAMENT | MAC DONALD-D | LM=11 TR=6 EX=0`
`0460 | A171627 | 35.64 | low_review | 1994-01-13 | PROBATE OF WILL - LETTERS TESTAMENT | POND-D | LM=7 TR=5 EX=0`
`0461 | A171957 | 35.64 | low_review | 1994-02-15 | DETERMINE SUCCESSION TO PRIMARY RES | GORSKI-D | LM=7 TR=5 EX=0`
`0462 | A172224 | 35.64 | low_review | 1994-03-04 | REAL PROPERTY OF SMALL VALUE (PROB  | GORSKI-D | LM=7 TR=5 EX=0`
`0463 | A172186 | 35.45 | low_review | 1994-03-03 | LETTERS OF ADMINISTRATION | DUFFEY-D | LM=7 TR=4 EX=0`
`0464 | A171613 | 35.39 | low_review | 1994-01-13 | PROBATE OF WILL - LETTERS TESTAMENT | GRISWOLD-D | LM=37 TR=28 EX=0`
`0465 | A171767 | 35.39 | low_review | 1994-01-27 | LETTERS OF ADMINISTRATION | WAKEFIELD-D | LM=50 TR=40 EX=0`
`0466 | A171893 | 35.39 | low_review | 1994-02-08 | PROBATE OF WILL - LETTERS TESTAMENT | RAINEY-D | LM=35 TR=26 EX=0`
`0467 | A172481 | 35.39 | low_review | 1994-03-22 | PROBATE OF WILL - LETTERS TESTAMENT | LYMAN-D | LM=24 TR=18 EX=0`
`0468 | A173015 | 35.39 | low_review | 1994-04-22 | PROBATE OF WILL - LETTERS TESTAMENT | LARKIN-D | LM=32 TR=25 EX=0`
`0469 | A174401 | 35.39 | low_review | 1994-08-08 | SPOUSAL PROPERTY | ROSEN-D | LM=29 TR=21 EX=0`
`0470 | A177952 | 35.39 | low_review | 1995-05-12 | PROBATE OF WILL - LETTERS TESTAMENT | O'LEARY-D | LM=23 TR=15 EX=0`
`0471 | A179327 | 35.39 | low_review | 1995-08-24 | LETTERS OF ADMINISTRATION | O'KEEFFE-D | LM=26 TR=20 EX=0`
`0472 | A107217 | 35.39 | low_review | 1995-10-24 | OTHER PROBATE MATTER | O'SCHAUGHNESSEY - DECEDENT | LM=21 TR=16 EX=0`
`0473 | A180637 | 35.39 | low_review | 1995-12-08 | LETTERS OF ADMINISTRATION | O'NEIL-D | LM=22 TR=19 EX=0`
`0474 | A171812 | 34.89 | low_review | 1994-02-01 | PROBATE OF WILL - LETTERS TESTAMENT | GREEN-D | LM=8 TR=5 EX=0`
`0475 | A171835 | 34.89 | low_review | 1994-02-02 | PROBATE OF WILL - LETTERS TESTAMENT | GREEN-D | LM=8 TR=5 EX=0`
`0476 | A171852 | 34.89 | low_review | 1994-02-03 | PROBATE OF WILL - LETTERS TESTAMENT | SLONE-D | LM=7 TR=5 EX=0`
`0477 | A171934 | 34.89 | low_review | 1994-02-14 | PROBATE OF WILL - LETTERS TESTAMENT | COUNCIL-D | LM=6 TR=5 EX=0`
`0478 | A172359 | 34.89 | low_review | 1994-03-15 | LETTERS OF ADMINISTRATION | SINDELAR-D | LM=9 TR=5 EX=0`
`0479 | A173260 | 34.89 | low_review | 1994-05-11 | PROBATE OF WILL  - LETTERS OF ADMIN | BAKER-D | LM=8 TR=5 EX=0`
`0480 | A173282 | 34.89 | low_review | 1994-05-12 | PROBATE OF WILL - LETTERS TESTAMENT | VAN HOOREBEKE-D | LM=9 TR=5 EX=0`
`0481 | A173628 | 34.89 | low_review | 1994-06-10 | PROBATE OF WILL - LETTERS TESTAMENT | BAKER-D | LM=8 TR=5 EX=0`
`0482 | A173847 | 34.89 | low_review | 1994-06-28 | LETTERS OF ADMINISTRATION | LA COMMARE-D | LM=16 TR=5 EX=0`
`0483 | A172166 | 34.71 | low_review | 1994-03-01 | PROBATE OF WILL - LETTERS TESTAMENT | KING-D | LM=6 TR=4 EX=0`
`0484 | A172372 | 34.71 | low_review | 1994-03-15 | PROBATE OF WILL - LETTERS TESTAMENT | KING-D | LM=6 TR=4 EX=0`
`0485 | A172704 | 34.71 | low_review | 1994-04-04 | PROBATE OF WILL - LETTERS TESTAMENT | HEINLEIN-D | LM=7 TR=4 EX=0`
`0486 | A172862 | 34.71 | low_review | 1994-04-13 | OTHER PROBATE MATTER | KEPFORD-M | LM=7 TR=4 EX=0`
`0487 | A171499 | 34.64 | low_review | 1994-01-04 | LETTERS OF SPECIAL ADMINISTRATION | DE SANTIAGO-D | LM=35 TR=29 EX=0`
`0488 | A172207 | 34.64 | low_review | 1994-03-04 | PROBATE OF WILL - LETTERS TESTAMENT | TEMPLETON-D | LM=23 TR=15 EX=0`
`0489 | A172215 | 34.64 | low_review | 1994-03-04 | PROBATE OF WILL - LETTERS TESTAMENT | NYE-D | LM=23 TR=20 EX=0`
`0490 | A172292 | 34.64 | low_review | 1994-03-09 | LETTERS OF ADMINISTRATION | CLIFTON-D | LM=22 TR=15 EX=0`
`0491 | A172612 | 34.64 | low_review | 1994-03-30 | LETTERS OF ADMINISTRATION | GLEASON-D | LM=46 TR=33 EX=0`
`0492 | A172632 | 34.64 | low_review | 1994-03-31 | PROBATE OF WILL - LETTERS TESTAMENT | HAND-D | LM=38 TR=33 EX=0`
`0493 | A172821 | 34.64 | low_review | 1994-04-11 | PROBATE OF WILL - LETTERS TESTAMENT | DE SILVIA-D | LM=25 TR=21 EX=0`
`0494 | A173316 | 34.64 | low_review | 1994-05-16 | SPOUSAL PROPERTY | NICHOLSON-D | LM=32 TR=19 EX=0`
`0495 | A177609 | 34.64 | low_review | 1995-04-18 | PROBATE OF WILL - LETTERS TESTAMENT | O'HALLORAN-D | LM=23 TR=18 EX=0`
`0496 | A177740 | 34.64 | low_review | 1995-04-28 | TRUST PROCEEDINGS | O'NEAL-T | LM=23 TR=17 EX=0`
`0497 | A172096 | 34.52 | low_review | 1994-02-24 | PROBATE OF WILL - LETTERS TESTAMENT | CURTIS-D | LM=43 TR=2 EX=0`
`0498 | A171488 | 34.02 | low_review | 1994-01-03 | PROBATE OF WILL - LETTERS TESTAMENT | ROBERTSON-D | LM=310 TR=222 EX=0`
`0499 | A171495 | 34.02 | low_review | 1994-01-04 | PROBATE OF WILL - LETTERS TESTAMENT | DUNCAN-D | LM=216 TR=149 EX=0`
`0500 | A171511 | 34.02 | low_review | 1994-01-05 | PROBATE OF WILL - LETTERS TESTAMENT | MURRAY-D | LM=325 TR=242 EX=0`
`0501 | A171518 | 34.02 | low_review | 1994-01-05 | LETTERS OF ADMINISTRATION | VEGA-D | LM=189 TR=133 EX=0`
`0502 | A171530 | 34.02 | low_review | 1994-01-06 | TRUST PROCEEDINGS | EWING-T | LM=113 TR=77 EX=0`
`0503 | A171554 | 34.02 | low_review | 1994-01-07 | PROBATE OF WILL - LETTERS TESTAMENT | WHEELER-D | LM=185 TR=117 EX=0`
`0504 | A171593 | 34.02 | low_review | 1994-01-11 | PROBATE OF WILL - LETTERS TESTAMENT | GREENE-D | LM=207 TR=136 EX=0`
`0505 | A171601 | 34.02 | low_review | 1994-01-12 | PROBATE OF WILL - LETTERS TESTAMENT | HART-D | LM=291 TR=195 EX=0`
`0506 | A171607 | 34.02 | low_review | 1994-01-12 | PROBATE OF WILL - LETTERS TESTAMENT | WEBB-D | LM=268 TR=183 EX=0`
`0507 | A171616 | 34.02 | low_review | 1994-01-13 | PROBATE OF WILL  - LETTERS OF ADMIN | COCHRAN-D | LM=104 TR=71 EX=0`
`0508 | A171718 | 34.02 | low_review | 1994-01-21 | PROBATE OF WILL - LETTERS TESTAMENT | SNYDER-D | LM=274 TR=182 EX=0`
`0509 | A171783 | 34.02 | low_review | 1994-01-28 | PROBATE OF WILL - LETTERS TESTAMENT | KNIGHT-D | LM=173 TR=128 EX=0`
`0510 | A171790 | 34.02 | low_review | 1994-01-31 | PROBATE OF WILL - LETTERS TESTAMENT | LYNCH-D | LM=166 TR=105 EX=0`
`0511 | A171801 | 34.02 | low_review | 1994-01-31 | PROBATE OF WILL - LETTERS TESTAMENT | BOYD-D | LM=216 TR=147 EX=0`
`0512 | A171826 | 34.02 | low_review | 1994-02-02 | PROBATE OF WILL - LETTERS TESTAMENT | HESS-D | LM=135 TR=88 EX=0`
`0513 | A171854 | 34.02 | low_review | 1994-02-03 | PROBATE OF WILL  - LETTERS OF ADMIN | NICHOLS-D | LM=206 TR=142 EX=0`
`0514 | A171897 | 34.02 | low_review | 1994-02-09 | PROBATE OF WILL - LETTERS TESTAMENT | WADE-D | LM=132 TR=85 EX=0`
`0515 | A171908 | 34.02 | low_review | 1994-02-09 | SPOUSAL PROPERTY | HARRISON-D | LM=234 TR=147 EX=0`
`0516 | A171921 | 34.02 | low_review | 1994-02-10 | PROBATE OF WILL - LETTERS TESTAMENT | LANE-D | LM=184 TR=125 EX=0`
`0517 | A171965 | 34.02 | low_review | 1994-02-15 | LETTERS OF ADMINISTRATION | BATES-D | LM=132 TR=103 EX=0`
`0518 | A171981 | 34.02 | low_review | 1994-02-15 | PROBATE OF WILL - LETTERS TESTAMENT | PETERSEN-D | LM=192 TR=133 EX=0`
`0519 | A171990 | 34.02 | low_review | 1994-02-16 | PROBATE OF WILL - LETTERS TESTAMENT | GOODMAN-D | LM=211 TR=156 EX=0`
`0520 | A172008 | 34.02 | low_review | 1994-02-17 | PROBATE OF WILL - LETTERS TESTAMENT | REED-D | LM=467 TR=294 EX=0`
`0521 | A172074 | 34.02 | low_review | 1994-02-23 | LETTERS OF ADMINISTRATION | ROSE JR-D | LM=196 TR=131 EX=0`
`0522 | A172134 | 34.02 | low_review | 1994-02-28 | LETTERS OF ADMINISTRATION | MURRAY-D | LM=219 TR=156 EX=0`
`0523 | A172221 | 34.02 | low_review | 1994-03-04 | PROBATE OF WILL - LETTERS TESTAMENT | **LYNCH-CONSOLIDATED INTO A171790 | LM=190 TR=121 EX=0`
`0524 | A172236 | 34.02 | low_review | 1994-03-07 | LETTERS OF ADMINISTRATION | MURRAY-D | LM=207 TR=146 EX=0`
`0525 | A172301 | 34.02 | low_review | 1994-03-10 | LETTERS OF ADMINISTRATION | BATES-D | LM=150 TR=117 EX=0`
`0526 | A172360 | 34.02 | low_review | 1994-03-15 | PROBATE OF WILL - LETTERS TESTAMENT | LYNCH-D | LM=202 TR=125 EX=0`
`0527 | A172390 | 34.02 | low_review | 1994-03-16 | TRUST PROCEEDINGS | JOHNSTON-T | LM=268 TR=189 EX=0`
`0528 | A172420 | 34.02 | low_review | 1994-03-17 | LETTERS OF ADMINISTRATION | CHOI-D | LM=308 TR=195 EX=0`
`0529 | A172513 | 34.02 | low_review | 1994-03-23 | PROBATE OF WILL - LETTERS TESTAMENT | GUERRERO-D | LM=131 TR=94 EX=0`
`0530 | A172517 | 34.02 | low_review | 1994-03-24 | PROBATE OF WILL - LETTERS TESTAMENT | ROSE-D | LM=219 TR=146 EX=0`
`0531 | A172554 | 34.02 | low_review | 1994-03-25 | TRUST PROCEEDINGS | HICKS-M | LM=148 TR=88 EX=0`
`0532 | A172639 | 34.02 | low_review | 1994-03-31 | PROBATE OF WILL - LETTERS TESTAMENT | WALLACE-D | LM=326 TR=219 EX=0`
`0533 | A172711 | 34.02 | low_review | 1994-04-05 | PROBATE OF WILL  - LETTERS OF ADMIN | SHERMAN-D | LM=160 TR=114 EX=0`
`0534 | A172751 | 34.02 | low_review | 1994-04-07 | PROBATE OF WILL - LETTERS TESTAMENT | HICKS-D | LM=155 TR=91 EX=0`
`0535 | A172880 | 34.02 | low_review | 1994-04-14 | SPOUSAL PROPERTY | GORDON-D | LM=313 TR=199 EX=0`
`0536 | A172881 | 34.02 | low_review | 1994-04-14 | PROBATE OF WILL - LETTERS TESTAMENT | RILEY-D | LM=164 TR=108 EX=0`
`0537 | A172897 | 34.02 | low_review | 1994-04-15 | PROBATE OF WILL  - LETTERS OF ADMIN | JOHNSTON-D | LM=246 TR=171 EX=0`
`0538 | A173020 | 34.02 | low_review | 1994-04-22 | PROBATE OF WILL - LETTERS TESTAMENT | BAILEY-D | LM=269 TR=192 EX=0`
`0539 | A173152 | 34.02 | low_review | 1994-05-04 | TRUST PROCEEDINGS | BAILEY-T | LM=245 TR=174 EX=0`
`0540 | A173153 | 34.02 | low_review | 1994-05-04 | PROBATE OF WILL - LETTERS TESTAMENT | JOHNSTON-D | LM=228 TR=164 EX=0`
`0541 | A173214 | 34.02 | low_review | 1994-05-09 | SPOUSAL PROPERTY | AVILA-D | LM=103 TR=68 EX=0`
`0542 | A173342 | 34.02 | low_review | 1994-05-18 | PROBATE OF WILL - LETTERS TESTAMENT | JONES-D | LM=457 TR=318 EX=0`
`0543 | A173542 | 34.02 | low_review | 1994-06-03 | LETTERS OF ADMINISTRATION | WALLACE-D | LM=195 TR=132 EX=0`
`0544 | A173748 | 34.02 | low_review | 1994-06-21 | PROBATE OF WILL - LETTERS TESTAMENT | GORDON-D | LM=161 TR=104 EX=0`
`0545 | A173865 | 34.02 | low_review | 1994-06-29 | PROBATE OF WILL - LETTERS TESTAMENT | SMITH-D | LM=307 TR=219 EX=0`
`0546 | A174596 | 34.02 | low_review | 1994-08-22 | PROBATE OF WILL - LETTERS TESTAMENT | JOHNSON-D | LM=398 TR=258 EX=0`
`0547 | A179959 | 34.02 | low_review | 1995-10-13 | DETERMINE SUCCESSION TO PRIMARY RES | PALMER-D | LM=198 TR=120 EX=0`
`0548 | A189182 | 34.02 | low_review | 1997-09-19 | PROBATE OF WILL - LETTERS TESTAMENT | PALMER-D | LM=210 TR=132 EX=0`
`0549 | A207103 | 34.02 | low_review | 2001-04-04 | PROBATE OF WILL - LETTERS TESTAMENT | PALMER-D | LM=247 TR=192 EX=0`
`0550 | A171644 | 33.96 | low_review | 1994-01-14 | PROBATE OF WILL - LETTERS TESTAMENT | WILSON-D | LM=6 TR=4 EX=0`
`0551 | A171728 | 33.96 | low_review | 1994-01-24 | PROBATE OF WILL - LETTERS TESTAMENT | AGUILAR-D | LM=5 TR=4 EX=0`
`0552 | A172766 | 33.96 | low_review | 1994-04-08 | TRUST PROCEEDINGS | DENIO-T | LM=6 TR=4 EX=0`
`0553 | A172109 | 33.78 | low_review | 1994-02-25 | OTHER PROBATE MATTER | MITCHELL-M | LM=5 TR=3 EX=0`
`0554 | A172110 | 33.78 | low_review | 1994-02-25 | OTHER PROBATE MATTER | MITCHELL-M | LM=5 TR=3 EX=0`
`0555 | A172300 | 33.78 | low_review | 1994-03-10 | PROBATE OF WILL - LETTERS TESTAMENT | MCCALL-D | LM=16 TR=3 EX=0`
`0556 | A172830 | 33.78 | low_review | 1994-04-12 | TRUST PROCEEDINGS | LYON-T | LM=5 TR=3 EX=0`
`0557 | A172249 | 33.77 | low_review | 1994-03-07 | PROBATE OF WILL  - LETTERS OF ADMIN | BOYER-D | LM=111 TR=83 EX=0`
`0558 | A171500 | 33.03 | low_review | 1994-01-04 | LETTERS OF ADMINISTRATION | AOKI-D | LM=7 TR=3 EX=0`
`0559 | A173036 | 33.03 | low_review | 1994-04-25 | PROBATE OF WILL - LETTERS TESTAMENT | ADAMS-D | LM=5 TR=3 EX=0`
`0560 | A173060 | 33.03 | low_review | 1994-04-27 | LETTERS OF ADMINISTRATION | CLARK-D | LM=5 TR=3 EX=0`
`0561 | A173312 | 33.03 | low_review | 1994-05-16 | PROBATE OF WILL - LETTERS TESTAMENT | BALDWIN-D | LM=4 TR=3 EX=0`
`0562 | A193186 | 33.03 | low_review | 1998-07-16 | OTHER PROBATE MATTER | UNION HISPANA-ADJUDICATION OF NEWSPAPER | LM=4 TR=3 EX=0`
`0563 | A171545 | 32.85 | low_review | 1994-01-07 | OTHER PROBATE MATTER | MITCHELL-M | LM=4 TR=2 EX=0`
`0564 | A172797 | 32.85 | low_review | 1994-04-08 | LETTERS OF ADMINISTRATION | FOGLER-D | LM=8 TR=2 EX=0`
`0565 | A171555 | 32.5 | low_review | 1994-01-07 | PROBATE OF WILL - LETTERS TESTAMENT | JONES-D | LM=1604 TR=1094 EX=0`
`0566 | A171947 | 32.5 | low_review | 1994-02-14 | PROBATE OF WILL - LETTERS TESTAMENT | JOHNSON-D | LM=2306 TR=1549 EX=0`
`0567 | A172054 | 32.5 | low_review | 1994-02-22 | LETTERS OF ADMINISTRATION | HARRIS-D | LM=526 TR=357 EX=0`
`0568 | A172223 | 32.5 | low_review | 1994-03-04 | PROBATE OF WILL - LETTERS TESTAMENT | ALLEN-D | LM=752 TR=484 EX=0`
`0569 | A172275 | 32.5 | low_review | 1994-03-09 | PROBATE OF WILL - LETTERS TESTAMENT | ALLEN-D | LM=784 TR=502 EX=0`
`0570 | A172413 | 32.5 | low_review | 1994-03-17 | PROBATE OF WILL  - LETTERS OF ADMIN | ALLEN-D | LM=760 TR=491 EX=0`
`0571 | A172480 | 32.5 | low_review | 1994-03-22 | PROBATE OF WILL - LETTERS TESTAMENT | DAVIS-D | LM=1059 TR=729 EX=0`
`0572 | A172608 | 32.5 | low_review | 1994-03-30 | PROBATE OF WILL - LETTERS TESTAMENT | SMITH-D | LM=1974 TR=1316 EX=0`
`0573 | A173133 | 32.5 | low_review | 1994-05-03 | PROBATE OF WILL - LETTERS TESTAMENT | DAVIS-D | LM=753 TR=508 EX=0`
`0574 | A173308 | 32.5 | low_review | 1994-05-16 | LETTERS OF ADMINISTRATION | SMITH-D | LM=1085 TR=732 EX=0`
`0575 | A173543 | 32.5 | low_review | 1994-06-03 | PROBATE OF WILL - LETTERS TESTAMENT | JOHNSON-D | LM=1445 TR=956 EX=0`
`0576 | A173684 | 32.5 | low_review | 1994-06-14 | PROBATE OF WILL - LETTERS TESTAMENT | SMITH-D | LM=586 TR=404 EX=0`
`0577 | A171550 | 32.1 | low_review | 1994-01-07 | PROBATE OF WILL  - LETTERS OF ADMIN | FRATER-D | LM=3 TR=2 EX=0`
`0578 | A171789 | 32.1 | low_review | 1994-01-31 | PROBATE OF WILL  - LETTERS OF ADMIN | GILBERT-D | LM=4 TR=2 EX=0`
`0579 | A171808 | 32.1 | low_review | 1994-02-01 | PROBATE OF WILL - LETTERS TESTAMENT | KELLEY-D | LM=3 TR=2 EX=0`
`0580 | A171911 | 32.1 | low_review | 1994-02-09 | PROBATE OF WILL - LETTERS TESTAMENT | LAMPEL-D | LM=6 TR=2 EX=0`
`0581 | A172200 | 32.1 | low_review | 1994-03-03 | PROBATE OF WILL - LETTERS TESTAMENT | LEATHERS-D | LM=5 TR=2 EX=0`
`0582 | A172764 | 32.1 | low_review | 1994-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | GOTHAM-D | LM=3 TR=2 EX=0`
`0583 | A172846 | 32.1 | low_review | 1994-04-13 | SPOUSAL PROPERTY | MORENO-D | LM=5 TR=2 EX=0`
`0584 | A173154 | 32.1 | low_review | 1994-05-04 | LETTERS OF ADMINISTRATION | CLARK-D | LM=4 TR=2 EX=0`
`0585 | A173323 | 32.1 | low_review | 1994-05-16 | OTHER PROBATE MATTER | EATON-M | LM=3 TR=2 EX=0`
`0586 | A212726 | 32.1 | low_review | 2002-04-03 | PROBATE OF WILL - LETTERS TESTAMENT | DEROSA-D | LM=3 TR=2 EX=0`
`0587 | A171591 | 31.98 | low_review | 1994-01-11 | PROBATE OF WILL - LETTERS TESTAMENT | MILLER-D | LM=15 TR=12 EX=0`
`0588 | A171622 | 31.98 | low_review | 1994-01-13 | PROBATE OF WILL - LETTERS TESTAMENT | HEUER-D | LM=8 TR=8 EX=0`
`0589 | A171675 | 31.98 | low_review | 1994-01-19 | PROBATE OF WILL - LETTERS TESTAMENT | HINSHAW-D | LM=20 TR=17 EX=0`
`0590 | A171710 | 31.98 | low_review | 1994-01-21 | PROBATE OF WILL - LETTERS TESTAMENT | SCHREINER-D | LM=18 TR=16 EX=0`
`0591 | A171780 | 31.98 | low_review | 1994-01-28 | PROBATE OF WILL - LETTERS TESTAMENT | STEVENS-D | LM=13 TR=12 EX=0`
`0592 | A171815 | 31.98 | low_review | 1994-02-01 | PROBATE OF WILL  - LETTERS OF ADMIN | POORE-D | LM=18 TR=13 EX=0`
`0593 | A171955 | 31.98 | low_review | 1994-02-15 | PROBATE OF WILL - LETTERS TESTAMENT | RATZLAFF-D | LM=8 TR=8 EX=0`
`0594 | A171979 | 31.98 | low_review | 1994-02-15 | LETTERS OF ADMINISTRATION | MILLER-D | LM=16 TR=14 EX=0`
`0595 | A171999 | 31.98 | low_review | 1994-02-17 | TRUST PROCEEDINGS | ILLIONS-T | LM=15 TR=15 EX=0`
`0596 | A172219 | 31.98 | low_review | 1994-03-04 | OTHER PROBATE MATTER | TAYLOR-D | LM=10 TR=9 EX=0`
`0597 | A172255 | 31.98 | low_review | 1994-03-07 | LETTERS OF ADMINISTRATION | WINCHELL-D | LM=14 TR=12 EX=0`
`0598 | A172395 | 31.98 | low_review | 1994-03-16 | TRUST PROCEEDINGS | BURKART-T | LM=18 TR=13 EX=0`
`0599 | A172437 | 31.98 | low_review | 1994-03-18 | PROBATE OF WILL - LETTERS TESTAMENT | MILLER-D | LM=16 TR=14 EX=0`
`0600 | A172466 | 31.98 | low_review | 1994-03-21 | PROBATE OF WILL - LETTERS TESTAMENT | BENNETT-D | LM=9 TR=8 EX=0`
`0601 | A172616 | 31.98 | low_review | 1994-03-30 | PROBATE OF WILL - LETTERS TESTAMENT | MILLER-D | LM=15 TR=14 EX=0`
`0602 | A172625 | 31.98 | low_review | 1994-03-30 | PROBATE OF WILL - LETTERS TESTAMENT | CLEGG-D | LM=12 TR=9 EX=0`
`0603 | A172712 | 31.98 | low_review | 1994-04-05 | SPOUSAL PROPERTY | MILLER-D | LM=15 TR=14 EX=0`
`0604 | A172796 | 31.98 | low_review | 1994-04-08 | SPOUSAL PROPERTY | STRENGTH-D | LM=12 TR=10 EX=0`
`0605 | A172800 | 31.98 | low_review | 1994-04-11 | OTHER PROBATE MATTER | BROMLEY-M | LM=15 TR=10 EX=0`
`0606 | A172842 | 31.98 | low_review | 1994-04-12 | PROBATE OF WILL - LETTERS TESTAMENT | PALMQUIST-D | LM=15 TR=12 EX=0`
`0607 | A173050 | 31.98 | low_review | 1994-04-25 | LETTERS OF ADMINISTRATION | MILLER-D | LM=13 TR=12 EX=0`
`0608 | A173283 | 31.98 | low_review | 1994-05-12 | SPOUSAL PROPERTY | BURKART-D | LM=12 TR=9 EX=0`
`0609 | A173452 | 31.98 | low_review | 1994-05-27 | PROBATE OF WILL  - LETTERS OF ADMIN | DILL-D | LM=12 TR=11 EX=0`
`0610 | A174074 | 31.98 | low_review | 1994-07-14 | DETERMINE SUCCESSION TO PRIMARY RES | O'RYAN-D | LM=17 TR=15 EX=0`
`0611 | A174187 | 31.98 | low_review | 1994-07-21 | PROBATE OF WILL - LETTERS TESTAMENT | SNYDER-D | LM=10 TR=10 EX=0`
`0612 | A201526 | 31.98 | low_review | 2000-03-16 | OTHER PROBATE MATTER | FIRST PRESBYTERIAN CHURCH-OT | LM=9 TR=8 EX=0`
`0613 | A212730 | 31.98 | low_review | 2002-04-03 | PROBATE OF WILL - LETTERS TESTAMENT | REEVE-D | LM=11 TR=9 EX=0`
`0614 | A172748 | 31.92 | low_review | 1994-04-07 | PROBATE OF WILL - LETTERS TESTAMENT | MCNAIR-D | LM=5 TR=1 EX=0`
`0615 | A172784 | 31.92 | low_review | 1994-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | PIFER-D | LM=5 TR=1 EX=0`
`0616 | A171571 | 31.17 | low_review | 1994-01-10 | DETERMINE SUCCESSION TO PRIMARY RES | GOMEZ-D | LM=3 TR=1 EX=0`
`0617 | A171827 | 31.17 | low_review | 1994-02-02 | PROBATE OF WILL - LETTERS TESTAMENT | SULLIVAN-D | LM=2 TR=1 EX=0`
`0618 | A171844 | 31.17 | low_review | 1994-02-03 | SPOUSAL PROPERTY | GRAY-D | LM=3 TR=1 EX=0`
`0619 | A171944 | 31.17 | low_review | 1994-02-14 | PROBATE OF WILL  - LETTERS OF ADMIN | COCHEMS-D | LM=3 TR=1 EX=0`
`0620 | A171987 | 31.17 | low_review | 1994-02-16 | PROBATE OF WILL - LETTERS TESTAMENT | SULLIVAN-D | LM=2 TR=1 EX=0`
`0621 | A172318 | 31.17 | low_review | 1994-03-11 | SPOUSAL PROPERTY | ROSENLOF-D | LM=2 TR=1 EX=0`
`0622 | A172329 | 31.17 | low_review | 1994-03-11 | PROBATE OF WILL  - LETTERS OF ADMIN | COLLINS-D | LM=3 TR=1 EX=0`
`0623 | A172338 | 31.17 | low_review | 1994-03-14 | PROBATE OF WILL - LETTERS TESTAMENT | SULLIVAN-D | LM=2 TR=1 EX=0`
`0624 | A172428 | 31.17 | low_review | 1994-03-17 | LETTERS OF ADMINISTRATION | LEIFHEIT-D | LM=3 TR=1 EX=0`
`0625 | A172531 | 31.17 | low_review | 1994-03-24 | LETTERS OF ADMINISTRATION | EILAND-D | LM=4 TR=1 EX=0`
`0626 | A172674 | 31.17 | low_review | 1994-04-01 | PROBATE OF WILL - LETTERS TESTAMENT | HUGHEY-D | LM=2 TR=1 EX=0`
`0627 | A172752 | 31.17 | low_review | 1994-04-07 | PROBATE OF WILL - LETTERS TESTAMENT | GULINO-D | LM=3 TR=1 EX=0`
`0628 | A172815 | 31.17 | low_review | 1994-04-11 | PROBATE OF WILL - LETTERS TESTAMENT | ABELA-D | LM=2 TR=1 EX=0`
`0629 | A173615 | 31.17 | low_review | 1994-06-09 | PROBATE OF WILL  - LETTERS OF ADMIN | PEREZ-D | LM=2 TR=1 EX=0`
`0630 | A173952 | 31.17 | low_review | 1994-07-06 | PROBATE OF WILL - LETTERS TESTAMENT | BALDWIN-D | LM=2 TR=1 EX=0`
`0631 | A175052 | 31.17 | low_review | 1994-09-27 | PROBATE OF WILL - LETTERS TESTAMENT | MARTINEZ-D | LM=2 TR=1 EX=0`
`0632 | A213200 | 31.17 | low_review | 2002-05-01 | LETTERS OF ADMINISTRATION | KLEIN-D | LM=2 TR=1 EX=0`
`0633 | A213584 | 31.17 | low_review | 2002-05-24 | TRUST PROCEEDINGS | KLEIN-T | LM=2 TR=1 EX=0`
`0634 | A171684 | 31.05 | low_review | 1994-01-19 | PROBATE OF WILL - LETTERS TESTAMENT | MODLIN-D | LM=8 TR=7 EX=0`
`0635 | A171785 | 31.05 | low_review | 1994-01-28 | LETTERS OF ADMINISTRATION | THOMAS-D | LM=9 TR=7 EX=0`
`0636 | A171874 | 31.05 | low_review | 1994-02-07 | PROBATE OF WILL - LETTERS TESTAMENT | GLAZE-D | LM=9 TR=7 EX=0`
`0637 | A172583 | 31.05 | low_review | 1994-03-29 | LETTERS OF ADMINISTRATION | STONE-D | LM=8 TR=7 EX=0`
`0638 | A172609 | 31.05 | low_review | 1994-03-30 | PROBATE OF WILL - LETTERS TESTAMENT | STONE-D | LM=8 TR=7 EX=0`
`0639 | A172785 | 31.05 | low_review | 1994-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | WILLIAMS-D | LM=10 TR=7 EX=0`
`0640 | A172820 | 31.05 | low_review | 1994-04-11 | PROBATE OF WILL - LETTERS TESTAMENT | ANDERSON-D | LM=9 TR=7 EX=0`
`0641 | A173136 | 31.05 | low_review | 1994-05-03 | PROBATE OF WILL - LETTERS TESTAMENT | WILSON-D | LM=7 TR=7 EX=0`
`0642 | A173348 | 31.05 | low_review | 1994-05-18 | LETTERS OF ADMINISTRATION | WILSON-D | LM=7 TR=7 EX=0`
`0643 | A174066 | 31.05 | low_review | 1994-07-13 | TRUST PROCEEDINGS | ASH-T | LM=9 TR=7 EX=0`
`0644 | A171798 | 30.12 | low_review | 1994-01-31 | PROBATE OF WILL - LETTERS TESTAMENT | CAMPBELL-D | LM=6 TR=6 EX=0`
`0645 | A172310 | 30.12 | low_review | 1994-03-10 | PROBATE OF WILL - LETTERS TESTAMENT | NELSON-D | LM=10 TR=6 EX=0`
`0646 | A173841 | 30.12 | low_review | 1994-06-27 | PROBATE OF WILL - LETTERS TESTAMENT | IRVINE-D | LM=8 TR=6 EX=0`
`0647 | A215471 | 30.12 | low_review | 2002-09-19 | PROBATE OF WILL - LETTERS TESTAMENT | VOGEL-D | LM=11 TR=6 EX=0`
`0648 | A172409 | 30.05 | low_review | 1994-03-17 | TRUST PROCEEDINGS | EMERSON-T | LM=115 TR=51 EX=0`
`0649 | A172910 | 29.63 | low_review | 1994-04-15 | LPS CONSERVATORSHIP (WI 5350) | DIAMOND-C | LM=3 TR=0 EX=0`
`0650 | A171724 | 29.19 | low_review | 1994-01-21 | SPOUSAL PROPERTY | PETERSON-D | LM=5 TR=5 EX=0`
`0651 | A171772 | 29.19 | low_review | 1994-01-27 | PROBATE OF WILL - LETTERS TESTAMENT | JACKSON-D | LM=6 TR=5 EX=0`
`0652 | A171871 | 29.19 | low_review | 1994-02-07 | PROBATE OF WILL  - LETTERS OF ADMIN | BLEWETT-D | LM=6 TR=5 EX=0`
`0653 | A172075 | 29.19 | low_review | 1994-02-23 | LETTERS OF ADMINISTRATION | THOMAS-D | LM=7 TR=5 EX=0`
`0654 | A172172 | 29.19 | low_review | 1994-03-02 | PROBATE OF WILL - LETTERS TESTAMENT | SAXTON-D | LM=5 TR=5 EX=0`
`0655 | A172191 | 29.19 | low_review | 1994-03-03 | PROBATE OF WILL - LETTERS TESTAMENT | WILSON-D | LM=5 TR=5 EX=0`
`0656 | A172198 | 29.19 | low_review | 1994-03-03 | PROBATE OF WILL - LETTERS TESTAMENT | JACKSON-D | LM=6 TR=5 EX=0`
`0657 | A172391 | 29.19 | low_review | 1994-03-16 | PROBATE OF WILL  - LETTERS OF ADMIN | GARRETT-D | LM=5 TR=5 EX=0`
`0658 | A172586 | 29.19 | low_review | 1994-03-29 | PROBATE OF WILL - LETTERS TESTAMENT | BORCHARDT-D | LM=6 TR=5 EX=0`
`0659 | A172647 | 29.19 | low_review | 1994-04-01 | PROBATE OF WILL  - LETTERS OF ADMIN | RUSSELL-D | LM=5 TR=5 EX=0`
`0660 | A172828 | 29.19 | low_review | 1994-04-12 | LETTERS OF ADMINISTRATION | TAYLOR-D | LM=6 TR=5 EX=0`
`0661 | A173113 | 29.19 | low_review | 1994-04-29 | TRUST PROCEEDINGS | FROST-T | LM=5 TR=5 EX=0`
`0662 | A173355 | 29.19 | low_review | 1994-05-18 | TRUST PROCEEDINGS | ANDERSON-T | LM=7 TR=5 EX=0`
`0663 | A173544 | 29.19 | low_review | 1994-06-03 | PROBATE OF WILL - LETTERS TESTAMENT | WILSON-D | LM=5 TR=5 EX=0`
`0664 | A173777 | 29.19 | low_review | 1994-06-22 | PROBATE OF WILL - LETTERS TESTAMENT | LEWIS-D | LM=5 TR=5 EX=0`
`0665 | A110627 | 28.94 | low_review | 1994-01-07 | OTHER PROBATE MATTER | HAMILTON - DECEDENT | LM=48 TR=46 EX=0`
`0666 | A171683 | 28.94 | low_review | 1994-01-19 | PROBATE OF WILL - LETTERS TESTAMENT | HAMMOND-D | LM=53 TR=53 EX=0`
`0667 | A172101 | 28.94 | low_review | 1994-02-24 | PROBATE OF WILL - LETTERS TESTAMENT | HAMILTON-D | LM=54 TR=53 EX=0`
`0668 | A172226 | 28.94 | low_review | 1994-03-04 | PROBATE OF WILL - LETTERS TESTAMENT | FORD-D | LM=21 TR=19 EX=0`
`0669 | A172584 | 28.94 | low_review | 1994-03-29 | PROBATE OF WILL - LETTERS TESTAMENT | PARK-D | LM=22 TR=11 EX=0`
`0670 | A172700 | 28.94 | low_review | 1994-04-04 | PROBATE OF WILL - LETTERS TESTAMENT | MAIN-D | LM=50 TR=50 EX=0`
`0671 | A172824 | 28.94 | low_review | 1994-04-11 | PROBATE OF WILL - LETTERS TESTAMENT | HALLIDAY-D | LM=23 TR=21 EX=0`
`0672 | A173000 | 28.94 | low_review | 1994-04-22 | LETTERS OF ADMINISTRATION | LE PIERRES-D | LM=37 TR=36 EX=0`
`0673 | A173139 | 28.94 | low_review | 1994-05-04 | PROBATE OF WILL - LETTERS TESTAMENT | LE CHASSEUR-D | LM=36 TR=35 EX=0`
`0674 | A173382 | 28.94 | low_review | 1994-05-20 | SPOUSAL PROPERTY | LE-D | LM=35 TR=34 EX=0`
`0675 | A211866 | 28.94 | low_review | 2002-02-07 | PROBATE OF WILL - LETTERS TESTAMENT | CHASE-D | LM=40 TR=39 EX=0`
`0676 | A212161 | 28.94 | low_review | 2002-02-26 | DETERMINE SUCCESSION TO PRIMARY RES | CHASE-D | LM=45 TR=44 EX=0`
`0677 | A172939 | 28.89 | low_review | 1994-04-18 | LPS CONSERVATORSHIP (WI 5350) | HALL-C | LM=4 TR=0 EX=0`
`0678 | A213203 | 28.89 | low_review | 2002-04-30 | LPS CONSERVATORSHIP (WI 5350) | PHELPS-LPS | LM=2 TR=0 EX=0`
`0679 | A213258 | 28.89 | low_review | 2002-05-03 | CONSERVATORSHIP OF PERSON ONLY | PHELPS-C | LM=2 TR=0 EX=0`
`0680 | A214239 | 28.89 | low_review | 2002-07-03 | LPS CONSERVATORSHIP (WI 5350) | PHELPS-LPS | LM=2 TR=0 EX=0`
`0681 | A171663 | 28.26 | low_review | 1994-01-18 | TRUST PROCEEDINGS | COOPER-T | LM=5 TR=4 EX=0`
`0682 | A171701 | 28.26 | low_review | 1994-01-20 | PROBATE OF WILL  - LETTERS OF ADMIN | FISHER JR-D | LM=4 TR=4 EX=0`
`0683 | A171735 | 28.26 | low_review | 1994-01-24 | PROBATE OF WILL - LETTERS TESTAMENT | BERKSON-D | LM=4 TR=4 EX=0`
`0684 | A171924 | 28.26 | low_review | 1994-02-10 | PROBATE OF WILL - LETTERS TESTAMENT | RYAN-D | LM=4 TR=4 EX=0`
`0685 | A172058 | 28.26 | low_review | 1994-02-23 | PROBATE OF WILL - LETTERS TESTAMENT | ROISMAN-D | LM=4 TR=4 EX=0`
`0686 | A172065 | 28.26 | low_review | 1994-02-23 | PROBATE OF WILL - LETTERS TESTAMENT | HOFFMAN-D | LM=4 TR=4 EX=0`
`0687 | A172160 | 28.26 | low_review | 1994-03-01 | TRUST PROCEEDINGS | WENTZEL-T | LM=4 TR=4 EX=0`
`0688 | A172185 | 28.26 | low_review | 1994-03-02 | PROBATE OF WILL - LETTERS TESTAMENT | LEWIS-D | LM=4 TR=4 EX=0`
`0689 | A172415 | 28.26 | low_review | 1994-03-17 | PROBATE OF WILL  - LETTERS OF ADMIN | BERRY-D | LM=4 TR=4 EX=0`
`0690 | A172477 | 28.26 | low_review | 1994-03-22 | LETTERS OF ADMINISTRATION | KRAIGE-D | LM=5 TR=4 EX=0`
`0691 | A172501 | 28.26 | low_review | 1994-03-23 | TRUST PROCEEDINGS | BRACAMONTES-T | LM=4 TR=4 EX=0`
`0692 | A172577 | 28.26 | low_review | 1994-03-28 | TRUST PROCEEDINGS | HAIN-T | LM=4 TR=4 EX=0`
`0693 | A172787 | 28.26 | low_review | 1994-04-08 | PROBATE OF WILL  - LETTERS OF ADMIN | LETCHER-D | LM=5 TR=4 EX=0`
`0694 | A172799 | 28.26 | low_review | 1994-04-11 | PROBATE OF WILL - LETTERS TESTAMENT | THOMPSON-D | LM=5 TR=4 EX=0`
`0695 | A172841 | 28.26 | low_review | 1994-04-12 | PROBATE OF WILL - LETTERS TESTAMENT | HUGHES-D | LM=4 TR=4 EX=0`
`0696 | A173156 | 28.26 | low_review | 1994-05-04 | SPOUSAL PROPERTY | WHITE-D | LM=5 TR=4 EX=0`
`0697 | A173237 | 28.26 | low_review | 1994-05-10 | PROBATE OF WILL - LETTERS TESTAMENT | WILLIAMS-D | LM=7 TR=4 EX=0`
`0698 | A173634 | 28.26 | low_review | 1994-06-10 | TRUST PROCEEDINGS | STEVENS JR-T | LM=5 TR=4 EX=0`
`0699 | A173660 | 28.26 | low_review | 1994-06-13 | PROBATE OF WILL - LETTERS TESTAMENT | ANDERSON-D | LM=6 TR=4 EX=0`
`0700 | A173699 | 28.26 | low_review | 1994-06-15 | PROBATE OF WILL  - LETTERS OF ADMIN | WILSON-D | LM=4 TR=4 EX=0`
`0701 | A173914 | 28.26 | low_review | 1994-07-01 | PROBATE OF WILL - LETTERS TESTAMENT | BROWN-D | LM=4 TR=4 EX=0`
`0702 | A174145 | 28.26 | low_review | 1994-07-20 | PROBATE OF WILL - LETTERS TESTAMENT | BROWN-D | LM=4 TR=4 EX=0`
`0703 | A213230 | 28.26 | low_review | 2002-05-02 | OTHER PROBATE MATTER | SOUTH-MISC | LM=4 TR=4 EX=0`
`0704 | A171577 | 28.14 | low_review | 1994-01-10 | LPS CONSERVATORSHIP (WI 5350) | LAWRENCE-C | LM=1 TR=0 EX=0`
`0705 | A171781 | 28.14 | low_review | 1994-01-28 | CONSERVATORSHIP OF PERSON AND ESTAT | HEGELE-C | LM=1 TR=0 EX=0`
`0706 | A173572 | 28.14 | low_review | 1994-06-08 | LPS CONSERVATORSHIP (WI 5350) | SIMPSON-C | LM=1 TR=0 EX=0`
`0707 | A173658 | 28.14 | low_review | 1994-06-13 | CONSERVATORSHIP OF PERSON AND ESTAT | BAIRD-C | LM=1 TR=0 EX=0`
`0708 | A173812 | 28.14 | low_review | 1994-06-24 | LPS CONSERVATORSHIP (WI 5350) | KING-C | LM=2 TR=0 EX=0`
`0709 | A178142 | 28.14 | low_review | 1995-05-25 | LPS CONSERVATORSHIP (WI 5350) | SAN MIGUEL-C | LM=2 TR=0 EX=0`
`0710 | A182219 | 28.14 | low_review | 1996-04-12 | GUARDIANSHIP OF PERSON ONLY | COLLINS-M | LM=2 TR=0 EX=0`
`0711 | A182972 | 28.14 | low_review | 1996-06-06 | CONSERVATORSHIP OF PERSON ONLY | COLLINS-CONSERVATORSHIP | LM=2 TR=0 EX=0`
`0712 | A183079 | 28.14 | low_review | 1996-06-13 | CONSERVATORSHIP OF PERSON AND ESTAT | COLLINS-C | LM=2 TR=0 EX=0`
`0713 | A187815 | 28.14 | low_review | 1997-06-10 | GUARDIANSHIP OF PERSON AND ESTATE | CRAIG-M | LM=1 TR=0 EX=0`
`0714 | A191391 | 28.14 | low_review | 1998-03-10 | LPS CONSERVATORSHIP (WI 5350) | SEPULVEDA-C | LM=1 TR=0 EX=0`
`0715 | A201006 | 28.14 | low_review | 2000-02-10 | LPS CONSERVATORSHIP (WI 5350) | OROZCO-LPS | LM=1 TR=0 EX=0`
`0716 | A211914 | 28.14 | low_review | 2002-02-11 | CONSERVATORSHIP OF PERSON AND ESTAT | KHAN-C | LM=1 TR=0 EX=0`
`0717 | A211980 | 28.14 | low_review | 2002-02-13 | LPS CONSERVATORSHIP (WI 5350) | SEBASTIAN-LPS | LM=1 TR=0 EX=0`
`0718 | A212017 | 28.14 | low_review | 2002-02-13 | LPS CONSERVATORSHIP (WI 5350) | JENKINS-LPS | LM=1 TR=0 EX=0`
`0719 | A212035 | 28.14 | low_review | 2002-02-19 | GUARDIANSHIP OF PERSON AND ESTATE | DIAZ-M | LM=1 TR=0 EX=0`
`0720 | A212270 | 28.14 | low_review | 2002-03-05 | GUARDIANSHIP OF PERSON ONLY | DIAZ-MINOR | LM=1 TR=0 EX=0`
`0721 | A212866 | 28.14 | low_review | 2002-04-10 | LPS CONSERVATORSHIP (WI 5350) | OLIVER-LPS | LM=2 TR=0 EX=0`
`0722 | A213377 | 28.14 | low_review | 2002-05-10 | LPS CONSERVATORSHIP (WI 5350) | DOWNS-LPS | LM=1 TR=0 EX=0`
`0723 | A213581 | 28.14 | low_review | 2002-05-24 | GUARDIANSHIP OF ESTATE ONLY | BISHOP-M | LM=1 TR=0 EX=0`
`0724 | A214145 | 28.14 | low_review | 2002-06-26 | LPS CONSERVATORSHIP (WI 5350) | FERNANDEZ-LPS | LM=1 TR=0 EX=0`
`0725 | A214120 | 28.14 | low_review | 2002-06-28 | GUARDIANSHIP OF PERSON ONLY | OLIVER-M | LM=2 TR=0 EX=0`
`0726 | A214283 | 28.14 | low_review | 2002-07-09 | GUARDIANSHIP OF PERSON AND ESTATE | GALLO-MINOR | LM=1 TR=0 EX=0`
`0727 | A214325 | 28.14 | low_review | 2002-07-10 | LPS CONSERVATORSHIP (WI 5350) | WOLFE-LPS | LM=1 TR=0 EX=0`
`0728 | A174636 | 27.4 | low_review | 1994-08-24 | LPS CONSERVATORSHIP (WI 5350) | STEWART-C | LM=19 TR=0 EX=0`
`0729 | A171658 | 27.33 | low_review | 1994-01-18 | LETTERS OF ADMINISTRATION | COLLINS-D | LM=5 TR=3 EX=0`
`0730 | A171708 | 27.33 | low_review | 1994-01-20 | PROBATE OF WILL - LETTERS TESTAMENT | BLACK-D | LM=4 TR=3 EX=0`
`0731 | A171725 | 27.33 | low_review | 1994-01-21 | LETTERS OF ADMINISTRATION | BULLOCK-D | LM=3 TR=3 EX=0`
`0732 | A171740 | 27.33 | low_review | 1994-01-25 | PROBATE OF WILL - LETTERS TESTAMENT | LEWIS-D | LM=3 TR=3 EX=0`
`0733 | A171846 | 27.33 | low_review | 1994-02-03 | LETTERS OF ADMINISTRATION | GOLD-D | LM=5 TR=3 EX=0`
`0734 | A171896 | 27.33 | low_review | 1994-02-08 | PROBATE OF WILL - LETTERS TESTAMENT | RUNDLE-D | LM=3 TR=3 EX=0`
`0735 | A171919 | 27.33 | low_review | 1994-02-10 | PROBATE OF WILL - LETTERS TESTAMENT | KRAMER-D | LM=3 TR=3 EX=0`
`0736 | A171923 | 27.33 | low_review | 1994-02-10 | PROBATE OF WILL  - LETTERS OF ADMIN | LABELLE-D | LM=3 TR=3 EX=0`
`0737 | A171959 | 27.33 | low_review | 1994-02-15 | SPOUSAL PROPERTY | WARD-D | LM=3 TR=3 EX=0`
`0738 | A172061 | 27.33 | low_review | 1994-02-23 | PROBATE OF WILL - LETTERS TESTAMENT | WOOD-D | LM=3 TR=3 EX=0`
`0739 | A172089 | 27.33 | low_review | 1994-02-24 | PROBATE OF WILL - LETTERS TESTAMENT | HOWDEN-D | LM=3 TR=3 EX=0`
`0740 | A172097 | 27.33 | low_review | 1994-02-24 | PROBATE OF WILL - LETTERS TESTAMENT | GUTTILLA-D | LM=3 TR=3 EX=0`
`0741 | A172103 | 27.33 | low_review | 1994-02-24 | PROBATE OF WILL - LETTERS TESTAMENT | KATZ-D | LM=3 TR=3 EX=0`
`0742 | A172111 | 27.33 | low_review | 1994-02-25 | PROBATE OF WILL - LETTERS TESTAMENT | EDWARDS-D | LM=3 TR=3 EX=0`
`0743 | A172117 | 27.33 | low_review | 1994-02-25 | PROBATE OF WILL - LETTERS TESTAMENT | SHLEPPEY-D | LM=6 TR=3 EX=0`
`0744 | A172314 | 27.33 | low_review | 1994-03-11 | TRUST PROCEEDINGS | MORRISON-T | LM=3 TR=3 EX=0`
`0745 | A172335 | 27.33 | low_review | 1994-03-11 | PROBATE OF WILL - LETTERS TESTAMENT | LACKNER-D | LM=4 TR=3 EX=0`
`0746 | A172363 | 27.33 | low_review | 1994-03-15 | PROBATE OF WILL - LETTERS TESTAMENT | RIQUELME-D | LM=3 TR=3 EX=0`
`0747 | A172532 | 27.33 | low_review | 1994-03-24 | PROBATE OF WILL - LETTERS TESTAMENT | ISHIHARA-D | LM=4 TR=3 EX=0`
`0748 | A172557 | 27.33 | low_review | 1994-03-25 | PROBATE OF WILL - LETTERS TESTAMENT | NERNEY-D | LM=4 TR=3 EX=0`
`0749 | A172569 | 27.33 | low_review | 1994-03-28 | PROBATE OF WILL - LETTERS TESTAMENT | MORRISON-D | LM=3 TR=3 EX=0`
`0750 | A172603 | 27.33 | low_review | 1994-03-29 | SPOUSAL PROPERTY | LECLAIR-D | LM=5 TR=3 EX=0`
`0751 | A172621 | 27.33 | low_review | 1994-03-30 | PROBATE OF WILL - LETTERS TESTAMENT | KINZIE-D | LM=3 TR=3 EX=0`
`0752 | A172662 | 27.33 | low_review | 1994-04-01 | LETTERS OF ADMINISTRATION | SEIBEL-D | LM=3 TR=3 EX=0`
`0753 | A172753 | 27.33 | low_review | 1994-04-07 | LETTERS OF ADMINISTRATION | KOIZUMI-D | LM=5 TR=3 EX=0`
`0754 | A172769 | 27.33 | low_review | 1994-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | HOSE-D | LM=4 TR=3 EX=0`
`0755 | A172900 | 27.33 | low_review | 1994-04-15 | PROBATE OF WILL - LETTERS TESTAMENT | BURNS-D | LM=3 TR=3 EX=0`
`0756 | A173039 | 27.33 | low_review | 1994-04-25 | PROBATE OF WILL - LETTERS TESTAMENT | WALKER-D | LM=3 TR=3 EX=0`
`0757 | A173048 | 27.33 | low_review | 1994-04-25 | PROBATE OF WILL - LETTERS TESTAMENT | BERRY-D | LM=3 TR=3 EX=0`
`0758 | A173095 | 27.33 | low_review | 1994-04-28 | DETERMINE SUCCESSION TO PRIMARY RES | HILL-D | LM=3 TR=3 EX=0`
`0759 | A173112 | 27.33 | low_review | 1994-04-29 | PROBATE OF WILL  - LETTERS OF ADMIN | WARD-D | LM=3 TR=3 EX=0`
`0760 | A173197 | 27.33 | low_review | 1994-05-06 | OTHER PROBATE MATTER | HILL-M | LM=3 TR=3 EX=0`
`0761 | A173198 | 27.33 | low_review | 1994-05-06 | OTHER PROBATE MATTER | HILL-M | LM=3 TR=3 EX=0`
`0762 | A173381 | 27.33 | low_review | 1994-05-20 | PROBATE OF WILL - LETTERS TESTAMENT | LANG-D | LM=3 TR=3 EX=0`
`0763 | A173745 | 27.33 | low_review | 1994-06-20 | PROBATE OF WILL - LETTERS TESTAMENT | MORGAN-D | LM=3 TR=3 EX=0`
`0764 | A174099 | 27.33 | low_review | 1994-07-15 | LETTERS OF ADMINISTRATION | RODRIGUEZ-D | LM=3 TR=3 EX=0`
`0765 | A174273 | 27.33 | low_review | 1994-07-28 | PROBATE OF WILL - LETTERS TESTAMENT | LA BAR-D | LM=8 TR=3 EX=0`
`0766 | A174305 | 27.33 | low_review | 1994-08-01 | PROBATE OF WILL - LETTERS TESTAMENT | BROWN-D | LM=3 TR=3 EX=0`
`0767 | A174552 | 27.33 | low_review | 1994-08-17 | PROBATE OF WILL - LETTERS TESTAMENT | BROWN JR-D | LM=3 TR=3 EX=0`
`0768 | A187717 | 27.33 | low_review | 1997-06-04 | LETTERS OF ADMINISTRATION | LA MARRE-D | LM=3 TR=3 EX=0`
`0769 | A188387 | 27.33 | low_review | 1997-08-20 | LETTERS OF ADMINISTRATION | BENNETT-D | LM=3 TR=3 EX=0`
`0770 | A189294 | 27.33 | low_review | 1997-09-29 | DETERMINE SUCCESSION TO PRIMARY RES | BENNETT-D | LM=3 TR=3 EX=0`
`0771 | A195726 | 27.33 | low_review | 1999-01-29 | OTHER PROBATE MATTER | FRANKLIN-M | LM=3 TR=3 EX=0`
`0772 | A205576 | 27.33 | low_review | 2000-12-29 | TRUST PROCEEDINGS | STONE/VAN WAGONER-TRUST | LM=3 TR=3 EX=0`
`0773 | A212202 | 27.33 | low_review | 2002-02-28 | LETTERS OF ADMINISTRATION | DUONG-D | LM=4 TR=3 EX=0`
`0774 | A212701 | 27.33 | low_review | 2002-04-03 | PROBATE OF WILL - LETTERS TESTAMENT | RICE-D | LM=3 TR=3 EX=0`
`0775 | A213027 | 27.33 | low_review | 2002-04-19 | TRUST PROCEEDINGS | ELLIS-T | LM=3 TR=3 EX=0`
`0776 | A171521 | 26.4 | low_review | 1994-01-05 | PROBATE OF WILL - LETTERS TESTAMENT | RINDER-D | LM=2 TR=2 EX=0`
`0777 | A171579 | 26.4 | low_review | 1994-01-10 | LETTERS OF ADMINISTRATION | ESQUIVEL-D | LM=3 TR=2 EX=0`
`0778 | A171581 | 26.4 | low_review | 1994-01-10 | PROBATE OF WILL - LETTERS TESTAMENT | COOK-D | LM=2 TR=2 EX=0`
`0779 | A171617 | 26.4 | low_review | 1994-01-13 | TRUST PROCEEDINGS | INGLIS-D | LM=2 TR=2 EX=0`
`0780 | A171661 | 26.4 | low_review | 1994-01-18 | LETTERS OF ADMINISTRATION | KOCH-D | LM=2 TR=2 EX=0`
`0781 | A171681 | 26.4 | low_review | 1994-01-19 | SPOUSAL PROPERTY | MAIZLAND-D | LM=4 TR=2 EX=0`
`0782 | A171686 | 26.4 | low_review | 1994-01-20 | PROBATE OF WILL - LETTERS TESTAMENT | DIXON-D | LM=2 TR=2 EX=0`
`0783 | A171753 | 26.4 | low_review | 1994-01-25 | PROBATE OF WILL - LETTERS TESTAMENT | EATON-D | LM=2 TR=2 EX=0`
`0784 | A171766 | 26.4 | low_review | 1994-01-26 | LETTERS OF ADMINISTRATION | DRACHMAN-D | LM=2 TR=2 EX=0`
`0785 | A171786 | 26.4 | low_review | 1994-01-28 | PROBATE OF WILL - LETTERS TESTAMENT | CRUZ-D | LM=2 TR=2 EX=0`
`0786 | A171840 | 26.4 | low_review | 1994-02-03 | PROBATE OF WILL - LETTERS TESTAMENT | MCIVER-D | LM=2 TR=2 EX=0`
`0787 | A171954 | 26.4 | low_review | 1994-02-15 | PROBATE OF WILL - LETTERS TESTAMENT | SAMPSEL-D | LM=2 TR=2 EX=0`
`0788 | A171994 | 26.4 | low_review | 1994-02-16 | TRUST PROCEEDINGS | EDWARDS-T | LM=2 TR=2 EX=0`
`0789 | A172003 | 26.4 | low_review | 1994-02-17 | PROBATE OF WILL  - LETTERS OF ADMIN | OLSON-D | LM=4 TR=2 EX=0`
`0790 | A172007 | 26.4 | low_review | 1994-02-17 | PROBATE OF WILL - LETTERS TESTAMENT | COOK-D | LM=2 TR=2 EX=0`
`0791 | A172062 | 26.4 | low_review | 1994-02-23 | PROBATE OF WILL  - LETTERS OF ADMIN | UNGUREANU-D | LM=4 TR=2 EX=0`
`0792 | A172072 | 26.4 | low_review | 1994-02-23 | SPOUSAL PROPERTY | CARLSON-D | LM=4 TR=2 EX=0`
`0793 | A172127 | 26.4 | low_review | 1994-02-28 | PROBATE OF WILL - LETTERS TESTAMENT | WALSH-D | LM=4 TR=2 EX=0`
`0794 | A172146 | 26.4 | low_review | 1994-03-01 | LETTERS OF ADMINISTRATION | WOLF-D | LM=2 TR=2 EX=0`
`0795 | A172167 | 26.4 | low_review | 1994-03-02 | PROBATE OF WILL - LETTERS TESTAMENT | LUNNY-D | LM=2 TR=2 EX=0`
`0796 | A172199 | 26.4 | low_review | 1994-03-03 | PROBATE OF WILL - LETTERS TESTAMENT | PETERSON-D | LM=2 TR=2 EX=0`
`0797 | A172217 | 26.4 | low_review | 1994-03-04 | PROBATE OF WILL - LETTERS TESTAMENT | SENERCHIA-D | LM=2 TR=2 EX=0`
`0798 | A172250 | 26.4 | low_review | 1994-03-07 | PROBATE OF WILL  - LETTERS OF ADMIN | CONSTANCE-D | LM=3 TR=2 EX=0`
`0799 | A172299 | 26.4 | low_review | 1994-03-09 | OTHER PROBATE MATTER | WALSH-M | LM=4 TR=2 EX=0`
`0800 | A172349 | 26.4 | low_review | 1994-03-14 | PROBATE OF WILL - LETTERS TESTAMENT | HANSEN-D | LM=3 TR=2 EX=0`
`0801 | A172354 | 26.4 | low_review | 1994-03-15 | PROBATE OF WILL - LETTERS TESTAMENT | OLSON-D | LM=4 TR=2 EX=0`
`0802 | A172406 | 26.4 | low_review | 1994-03-17 | PROBATE OF WILL - LETTERS TESTAMENT | MATTOCKS-D | LM=2 TR=2 EX=0`
`0803 | A172478 | 26.4 | low_review | 1994-03-22 | TRUST PROCEEDINGS | GUGGENHEIM-T | LM=2 TR=2 EX=0`
`0804 | A172506 | 26.4 | low_review | 1994-03-23 | PROBATE OF WILL - LETTERS TESTAMENT | RANZAN-D | LM=3 TR=2 EX=0`
`0805 | A172519 | 26.4 | low_review | 1994-03-24 | PROBATE OF WILL - LETTERS TESTAMENT | DREBLOW-D | LM=3 TR=2 EX=0`
`0806 | A172538 | 26.4 | low_review | 1994-03-24 | SPOUSAL PROPERTY | ANDREWS-D | LM=2 TR=2 EX=0`
`0807 | A172585 | 26.4 | low_review | 1994-03-29 | SPOUSAL PROPERTY | CARLSON-D | LM=4 TR=2 EX=0`
`0808 | A172597 | 26.4 | low_review | 1994-03-29 | PROBATE OF WILL - LETTERS TESTAMENT | ENGELMANN-D | LM=3 TR=2 EX=0`
`0809 | A172620 | 26.4 | low_review | 1994-03-30 | PROBATE OF WILL - LETTERS TESTAMENT | NELSON-D | LM=5 TR=2 EX=0`
`0810 | A172634 | 26.4 | low_review | 1994-03-31 | LETTERS OF ADMINISTRATION | ESQUIVEL-D | LM=3 TR=2 EX=0`
`0811 | A172636 | 26.4 | low_review | 1994-03-31 | PROBATE OF WILL  - LETTERS OF ADMIN | CAREY-D | LM=2 TR=2 EX=0`
`0812 | A172661 | 26.4 | low_review | 1994-04-01 | PROBATE OF WILL - LETTERS TESTAMENT | OLSON-D | LM=3 TR=2 EX=0`
`0813 | A172664 | 26.4 | low_review | 1994-04-01 | PROBATE OF WILL - LETTERS TESTAMENT | GRISE-D | LM=2 TR=2 EX=0`
`0814 | A172665 | 26.4 | low_review | 1994-04-01 | REAL PROPERTY OF SMALL VALUE (PROB  | MOSCA-D | LM=2 TR=2 EX=0`
`0815 | A172666 | 26.4 | low_review | 1994-04-01 | PROBATE OF WILL - LETTERS TESTAMENT | COPPOLA-D | LM=2 TR=2 EX=0`
`0816 | A172677 | 26.4 | low_review | 1994-04-04 | LETTERS OF ADMINISTRATION | **DOYLE-D CONSOLIDATE INTO A173418 | LM=2 TR=2 EX=0`
`0817 | A173418 | 26.4 | low_review | 1994-04-04 | PROBATE OF WILL - LETTERS TESTAMENT | DOYLE-D | LM=2 TR=2 EX=0`
`0818 | A172794 | 26.4 | low_review | 1994-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | JAFFE-D | LM=2 TR=2 EX=0`
`0819 | A172831 | 26.4 | low_review | 1994-04-12 | PROBATE OF WILL - LETTERS TESTAMENT | AGUILERA-D | LM=2 TR=2 EX=0`
`0820 | A172858 | 26.4 | low_review | 1994-04-13 | PROBATE OF WILL - LETTERS TESTAMENT | MENER-D | LM=2 TR=2 EX=0`
`0821 | A172946 | 26.4 | low_review | 1994-04-19 | PROBATE OF WILL  - LETTERS OF ADMIN | PHILLIPS-D | LM=2 TR=2 EX=0`
`0822 | A172967 | 26.4 | low_review | 1994-04-20 | REAL PROPERTY OF SMALL VALUE (PROB  | MOSCA-D | LM=2 TR=2 EX=0`
`0823 | A172983 | 26.4 | low_review | 1994-04-21 | PROBATE OF WILL - LETTERS TESTAMENT | WOOD-D | LM=2 TR=2 EX=0`
`0824 | A172986 | 26.4 | low_review | 1994-04-21 | LETTERS OF ADMINISTRATION | SCOTT-D | LM=2 TR=2 EX=0`
`0825 | A173057 | 26.4 | low_review | 1994-04-26 | SPOUSAL PROPERTY | HARTONG-D | LM=2 TR=2 EX=0`
`0826 | A173155 | 26.4 | low_review | 1994-05-04 | PROBATE OF WILL - LETTERS TESTAMENT | CARTER-D | LM=3 TR=2 EX=0`
`0827 | A173180 | 26.4 | low_review | 1994-05-06 | PROBATE OF WILL - LETTERS TESTAMENT | FISHER-D | LM=2 TR=2 EX=0`
`0828 | A173248 | 26.4 | low_review | 1994-05-11 | PROBATE OF WILL - LETTERS TESTAMENT | GREEN-D | LM=3 TR=2 EX=0`
`0829 | A173380 | 26.4 | low_review | 1994-05-20 | PROBATE OF WILL - LETTERS TESTAMENT | PERKINS-D | LM=2 TR=2 EX=0`
`0830 | A173386 | 26.4 | low_review | 1994-05-20 | TRUST PROCEEDINGS | WEISS-T | LM=2 TR=2 EX=0`
`0831 | A173407 | 26.4 | low_review | 1994-05-24 | REAL PROPERTY OF SMALL VALUE (PROB  | MORRISON-D | LM=2 TR=2 EX=0`
`0832 | A173462 | 26.4 | low_review | 1994-05-27 | PROBATE OF WILL - LETTERS TESTAMENT | BLAKE-D | LM=2 TR=2 EX=0`
`0833 | A173614 | 26.4 | low_review | 1994-06-09 | TRUST PROCEEDINGS | WOOD-T | LM=2 TR=2 EX=0`
`0834 | A173632 | 26.4 | low_review | 1994-06-10 | PROBATE OF WILL - LETTERS TESTAMENT | WALKER-D | LM=2 TR=2 EX=0`
`0835 | A173649 | 26.4 | low_review | 1994-06-10 | SPOUSAL PROPERTY | DI GIULIO-D | LM=3 TR=2 EX=0`
`0836 | A173722 | 26.4 | low_review | 1994-06-17 | TRUST PROCEEDINGS | FOX-T | LM=2 TR=2 EX=0`
`0837 | A173743 | 26.4 | low_review | 1994-06-20 | PROBATE OF WILL - LETTERS TESTAMENT | WOOD-D | LM=2 TR=2 EX=0`
`0838 | A174044 | 26.4 | low_review | 1994-07-13 | SPOUSAL PROPERTY | GARCIA-D | LM=2 TR=2 EX=0`
`0839 | A174138 | 26.4 | low_review | 1994-07-19 | PROBATE OF WILL - LETTERS TESTAMENT | WEISS-D | LM=2 TR=2 EX=0`
`0840 | A174242 | 26.4 | low_review | 1994-07-26 | PROBATE OF WILL - LETTERS TESTAMENT | TAYLOR-D | LM=2 TR=2 EX=0`
`0841 | A174373 | 26.4 | low_review | 1994-08-04 | PROBATE OF WILL - LETTERS TESTAMENT | WILSON-D | LM=2 TR=2 EX=0`
`0842 | A174939 | 26.4 | low_review | 1994-08-16 | PROBATE OF WILL - LETTERS TESTAMENT | CARY-D | LM=2 TR=2 EX=0`
`0843 | A109287 | 26.4 | low_review | 1994-09-07 | OTHER PROBATE MATTER | THOMPSON-T | LM=3 TR=2 EX=0`
`0844 | A175972 | 26.4 | low_review | 1994-12-12 | PROBATE OF WILL - LETTERS TESTAMENT | ROBINSON-D | LM=2 TR=2 EX=0`
`0845 | A176690 | 26.4 | low_review | 1995-02-09 | LETTERS OF ADMINISTRATION | WELLS-D | LM=2 TR=2 EX=0`
`0846 | A176855 | 26.4 | low_review | 1995-02-22 | PROBATE OF WILL - LETTERS TESTAMENT | ROBINSON-D | LM=2 TR=2 EX=0`
`0847 | A176875 | 26.4 | low_review | 1995-02-23 | SPOUSAL PROPERTY | ROBINSON-D | LM=2 TR=2 EX=0`
`0848 | A178027 | 26.4 | low_review | 1995-05-14 | PROBATE OF WILL - LETTERS TESTAMENT | WELLS-D | LM=2 TR=2 EX=0`
`0849 | A178207 | 26.4 | low_review | 1995-05-31 | LETTERS OF ADMINISTRATION | ROMAN-D | LM=2 TR=2 EX=0`
`0850 | A184025 | 26.4 | low_review | 1996-08-19 | PROBATE OF WILL - LETTERS TESTAMENT | MC COLM-D | LM=2 TR=2 EX=0`
`0851 | A188110 | 26.4 | low_review | 1997-07-01 | LETTERS OF ADMINISTRATION | BENNETT-D | LM=2 TR=2 EX=0`
`0852 | A189925 | 26.4 | low_review | 1997-11-14 | PROBATE OF WILL  - LETTERS OF ADMIN | LAWSON JR-D | LM=2 TR=2 EX=0`
`0853 | A190614 | 26.4 | low_review | 1998-01-14 | PROBATE OF WILL - LETTERS TESTAMENT | LAWSON-D | LM=2 TR=2 EX=0`
`0854 | A194096 | 26.4 | low_review | 1998-09-18 | PROBATE OF WILL - LETTERS TESTAMENT | WASHINGTON-D | LM=2 TR=2 EX=0`
`0855 | A204805 | 26.4 | low_review | 2000-10-31 | PROBATE OF WILL - LETTERS TESTAMENT | BARRINGTON-D | LM=2 TR=2 EX=0`
`0856 | A205235 | 26.4 | low_review | 2000-12-05 | LETTERS OF ADMINISTRATION | CHASE-D | LM=3 TR=2 EX=0`
`0857 | A210200 | 26.4 | low_review | 2001-10-10 | LETTERS OF ADMINISTRATION | GIBSON-D | LM=2 TR=2 EX=0`
`0858 | A211707 | 26.4 | low_review | 2002-01-29 | TRUST PROCEEDINGS | ST GEORGE-T | LM=2 TR=2 EX=0`
`0859 | A212037 | 26.4 | low_review | 2002-02-19 | LETTERS OF ADMINISTRATION | ELLIS-D | LM=2 TR=2 EX=0`
`0860 | A212158 | 26.4 | low_review | 2002-02-26 | PROBATE OF WILL - LETTERS TESTAMENT | ELLIS-D | LM=2 TR=2 EX=0`
`0861 | A212272 | 26.4 | low_review | 2002-03-05 | TRUST PROCEEDINGS | HAYES-T | LM=2 TR=2 EX=0`
`0862 | A212888 | 26.4 | low_review | 2002-04-11 | DETERMINE SUCCESSION TO PRIMARY RES | BURTON,SR-D | LM=2 TR=2 EX=0`
`0863 | A213649 | 26.4 | low_review | 2002-05-30 | PROBATE OF WILL  - LETTERS OF ADMIN | VOURNAZOS-D | LM=4 TR=2 EX=0`
`0864 | A213834 | 26.4 | low_review | 2002-06-11 | DETERMINE SUCCESSION TO PRIMARY RES | STEELE-D | LM=2 TR=2 EX=0`
`0865 | A213964 | 26.4 | low_review | 2002-06-19 | TRUST PROCEEDINGS | STEELE-T | LM=2 TR=2 EX=0`
`0866 | A171490 | 25.47 | low_review | 1994-01-03 | PROBATE OF WILL - LETTERS TESTAMENT | HARDING-SAUNDERS-D | LM=1 TR=1 EX=0`
`0867 | A171491 | 25.47 | low_review | 1994-01-03 | PROBATE OF WILL - LETTERS TESTAMENT | REDERSCHEID-D | LM=2 TR=1 EX=0`
`0868 | A171543 | 25.47 | low_review | 1994-01-07 | LETTERS OF ADMINISTRATION | BRUSHITIS-D | LM=1 TR=1 EX=0`
`0869 | A171604 | 25.47 | low_review | 1994-01-12 | TRUST PROCEEDINGS | BENCE-T | LM=2 TR=1 EX=0`
`0870 | A171612 | 25.47 | low_review | 1994-01-13 | OTHER PROBATE MATTER | PEW-M | LM=1 TR=1 EX=0`
`0871 | A171685 | 25.47 | low_review | 1994-01-20 | PROBATE OF WILL  - LETTERS OF ADMIN | LUKENBILL-D | LM=2 TR=1 EX=0`
`0872 | A171719 | 25.47 | low_review | 1994-01-21 | PROBATE OF WILL - LETTERS TESTAMENT | BAUER-D | LM=1 TR=1 EX=0`
`0873 | A171755 | 25.47 | low_review | 1994-01-26 | TRUST PROCEEDINGS | TUCKER-D | LM=1 TR=1 EX=0`
`0874 | A171811 | 25.47 | low_review | 1994-02-01 | PROBATE OF WILL - LETTERS TESTAMENT | KINGHORN-D | LM=1 TR=1 EX=0`
`0875 | A171813 | 25.47 | low_review | 1994-02-01 | PROBATE OF WILL - LETTERS TESTAMENT | ORNER-D | LM=3 TR=1 EX=0`
`0876 | A171820 | 25.47 | low_review | 1994-02-02 | REAL PROPERTY OF SMALL VALUE (PROB  | WILCOX-D | LM=1 TR=1 EX=0`
`0877 | A171833 | 25.47 | low_review | 1994-02-02 | PROBATE OF WILL - LETTERS TESTAMENT | SCHILLER-D | LM=1 TR=1 EX=0`
`0878 | A171888 | 25.47 | low_review | 1994-02-08 | PROBATE OF WILL - LETTERS TESTAMENT | WINNER-D | LM=2 TR=1 EX=0`
`0879 | A171918 | 25.47 | low_review | 1994-02-09 | REAL PROPERTY OF SMALL VALUE (PROB  | ROBBINS-D | LM=1 TR=1 EX=0`
`0880 | A171927 | 25.47 | low_review | 1994-02-10 | PROBATE OF WILL - LETTERS TESTAMENT | OSBORNE-D | LM=1 TR=1 EX=0`
`0881 | A171964 | 25.47 | low_review | 1994-02-15 | PROBATE OF WILL - LETTERS TESTAMENT | PETERS-D | LM=1 TR=1 EX=0`
`0882 | A172012 | 25.47 | low_review | 1994-02-17 | PROBATE OF WILL - LETTERS TESTAMENT | FORREST-D | LM=1 TR=1 EX=0`
`0883 | A172029 | 25.47 | low_review | 1994-02-18 | PROBATE OF WILL - LETTERS TESTAMENT | BROADDUS-D | LM=1 TR=1 EX=0`
`0884 | A172033 | 25.47 | low_review | 1994-02-22 | PROBATE OF WILL - LETTERS TESTAMENT | HARKEY-D | LM=1 TR=1 EX=0`
`0885 | A172040 | 25.47 | low_review | 1994-02-22 | PROBATE OF WILL - LETTERS TESTAMENT | HALEY-D | LM=1 TR=1 EX=0`
`0886 | A172130 | 25.47 | low_review | 1994-02-28 | PROBATE OF WILL - LETTERS TESTAMENT | NAGELE-D | LM=1 TR=1 EX=0`
`0887 | A172138 | 25.47 | low_review | 1994-02-28 | PROBATE OF WILL - LETTERS TESTAMENT | ROCKEY-D | LM=2 TR=1 EX=0`
`0888 | A172192 | 25.47 | low_review | 1994-03-03 | TRUST PROCEEDINGS | YOUNG-T | LM=1 TR=1 EX=0`
`0889 | A172197 | 25.47 | low_review | 1994-03-03 | PROBATE OF WILL - LETTERS TESTAMENT | STEELE-D | LM=2 TR=1 EX=0`
`0890 | A172252 | 25.47 | low_review | 1994-03-07 | SPOUSAL PROPERTY | KENNEY-D | LM=1 TR=1 EX=0`
`0891 | A172264 | 25.47 | low_review | 1994-03-08 | PROBATE OF WILL - LETTERS TESTAMENT | TYLER-D | LM=1 TR=1 EX=0`
`0892 | A172273 | 25.47 | low_review | 1994-03-08 | SPOUSAL PROPERTY | SCHNEIDER-D | LM=2 TR=1 EX=0`
`0893 | A172290 | 25.47 | low_review | 1994-03-09 | PROBATE OF WILL - LETTERS TESTAMENT | HOLMES-D | LM=1 TR=1 EX=0`
`0894 | A172305 | 25.47 | low_review | 1994-03-10 | PROBATE OF WILL - LETTERS TESTAMENT | PASTUSHIN-D | LM=1 TR=1 EX=0`
`0895 | A172332 | 25.47 | low_review | 1994-03-11 | PROBATE OF WILL - LETTERS TESTAMENT | KINWORTHY-D | LM=1 TR=1 EX=0`
`0896 | A172367 | 25.47 | low_review | 1994-03-15 | PROBATE OF WILL - LETTERS TESTAMENT | CAMERON-D | LM=1 TR=1 EX=0`
`0897 | A172449 | 25.47 | low_review | 1994-03-18 | PROBATE OF WILL - LETTERS TESTAMENT | BOWERS-D | LM=1 TR=1 EX=0`
`0898 | A172450 | 25.47 | low_review | 1994-03-21 | SPOUSAL PROPERTY | TORONTO-D | LM=4 TR=1 EX=0`
`0899 | A172476 | 25.47 | low_review | 1994-03-22 | PROBATE OF WILL - LETTERS TESTAMENT | JANSEN-D | LM=1 TR=1 EX=0`
`0900 | A172505 | 25.47 | low_review | 1994-03-23 | SPOUSAL PROPERTY | LUIRETTE-D | LM=3 TR=1 EX=0`
`0901 | A172536 | 25.47 | low_review | 1994-03-24 | PROBATE OF WILL - LETTERS TESTAMENT | ROBBINS-D | LM=1 TR=1 EX=0`
`0902 | A172543 | 25.47 | low_review | 1994-03-25 | PROBATE OF WILL - LETTERS TESTAMENT | HARDY-D | LM=1 TR=1 EX=0`
`0903 | A172560 | 25.47 | low_review | 1994-03-25 | OTHER PROBATE MATTER | BAUMAN-M | LM=1 TR=1 EX=0`
`0904 | A172561 | 25.47 | low_review | 1994-03-25 | OTHER PROBATE MATTER | BAUMAN-M | LM=1 TR=1 EX=0`
`0905 | A172627 | 25.47 | low_review | 1994-03-30 | PROBATE OF WILL - LETTERS TESTAMENT | WILLIAMSON-D | LM=5 TR=1 EX=0`
`0906 | A172706 | 25.47 | low_review | 1994-04-04 | PROBATE OF WILL - LETTERS TESTAMENT | VON GRUENIGEN-D | LM=1 TR=1 EX=0`
`0907 | A172719 | 25.47 | low_review | 1994-04-05 | SPOUSAL PROPERTY | CATLING-D | LM=2 TR=1 EX=0`
`0908 | A172746 | 25.47 | low_review | 1994-04-07 | PROBATE OF WILL - LETTERS TESTAMENT | ERHART-D | LM=1 TR=1 EX=0`
`0909 | A172786 | 25.47 | low_review | 1994-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | NOBLE-D | LM=1 TR=1 EX=0`
`0910 | A172808 | 25.47 | low_review | 1994-04-11 | PROBATE OF WILL  - LETTERS OF ADMIN | MORENCY-D | LM=2 TR=1 EX=0`
`0911 | A172818 | 25.47 | low_review | 1994-04-11 | PROBATE OF WILL - LETTERS TESTAMENT | MURAVEZ-D | LM=1 TR=1 EX=0`
`0912 | A172835 | 25.47 | low_review | 1994-04-12 | PROBATE OF WILL - LETTERS TESTAMENT | MCFARLIN-D | LM=1 TR=1 EX=0`
`0913 | A172875 | 25.47 | low_review | 1994-04-14 | SPOUSAL PROPERTY | MCKELVIE-D | LM=1 TR=1 EX=0`
`0914 | A172947 | 25.47 | low_review | 1994-04-19 | PROBATE OF WILL - LETTERS TESTAMENT | GRIFFIN-D | LM=1 TR=1 EX=0`
`0915 | A172948 | 25.47 | low_review | 1994-04-19 | OTHER PROBATE MATTER | SPENCER-D | LM=2 TR=1 EX=0`
`0916 | A172950 | 25.47 | low_review | 1994-04-20 | REAL PROPERTY OF SMALL VALUE (PROB  | WILLIS-D | LM=1 TR=1 EX=0`
`0917 | A172968 | 25.47 | low_review | 1994-04-20 | LETTERS OF ADMINISTRATION | CORBIN-D | LM=1 TR=1 EX=0`
`0918 | A172974 | 25.47 | low_review | 1994-04-20 | PROBATE OF WILL - LETTERS TESTAMENT | BOWEN-T | LM=1 TR=1 EX=0`
`0919 | A172978 | 25.47 | low_review | 1994-04-21 | PROBATE OF WILL - LETTERS TESTAMENT | MOSES-D | LM=1 TR=1 EX=0`
`0920 | A172993 | 25.47 | low_review | 1994-04-22 | PROBATE OF WILL - LETTERS TESTAMENT | MEDINA-D | LM=1 TR=1 EX=0`
`0921 | A173010 | 25.47 | low_review | 1994-04-22 | PROBATE OF WILL - LETTERS TESTAMENT | TOMLINSON-D | LM=1 TR=1 EX=0`
`0922 | A173058 | 25.47 | low_review | 1994-04-26 | TRUST PROCEEDINGS | NELSON-T | LM=3 TR=1 EX=0`
`0923 | A173081 | 25.47 | low_review | 1994-04-27 | PROBATE OF WILL - LETTERS TESTAMENT | FALCONE-D | LM=1 TR=1 EX=0`
`0924 | A173118 | 25.47 | low_review | 1994-05-02 | LETTERS OF ADMINISTRATION | BARBER-D | LM=1 TR=1 EX=0`
`0925 | A173194 | 25.47 | low_review | 1994-05-06 | PROBATE OF WILL - LETTERS TESTAMENT | FAIRFIELD-D | LM=1 TR=1 EX=0`
`0926 | A173261 | 25.47 | low_review | 1994-05-11 | PROBATE OF WILL  - LETTERS OF ADMIN | ELDER-D | LM=1 TR=1 EX=0`
`0927 | A173326 | 25.47 | low_review | 1994-05-17 | LETTERS OF ADMINISTRATION | SIMMONS-D | LM=1 TR=1 EX=0`
`0928 | A173329 | 25.47 | low_review | 1994-05-17 | PROBATE OF WILL - LETTERS TESTAMENT | MEYER-D | LM=1 TR=1 EX=0`
`0929 | A173334 | 25.47 | low_review | 1994-05-17 | PROBATE OF WILL - LETTERS TESTAMENT | PETERSON-D | LM=1 TR=1 EX=0`
`0930 | A173397 | 25.47 | low_review | 1994-05-23 | LETTERS OF ADMINISTRATION | FERGUSON-D | LM=1 TR=1 EX=0`
`0931 | A173492 | 25.47 | low_review | 1994-06-01 | PROBATE OF WILL - LETTERS TESTAMENT | CUMMINGS-D | LM=1 TR=1 EX=0`
`0932 | A173495 | 25.47 | low_review | 1994-06-01 | SPOUSAL PROPERTY | HUTCHISON-D | LM=2 TR=1 EX=0`
`0933 | A173505 | 25.47 | low_review | 1994-06-02 | PROBATE OF WILL - LETTERS TESTAMENT | BERG-D | LM=1 TR=1 EX=0`
`0934 | A173537 | 25.47 | low_review | 1994-06-03 | PROBATE OF WILL - LETTERS TESTAMENT | CUMMINGS-D | LM=1 TR=1 EX=0`
`0935 | A173560 | 25.47 | low_review | 1994-06-07 | PROBATE OF WILL - LETTERS TESTAMENT | MEYERS-D | LM=2 TR=1 EX=0`
`0936 | A173597 | 25.47 | low_review | 1994-06-08 | PROBATE OF WILL - LETTERS TESTAMENT | HILLS-D | LM=1 TR=1 EX=0`
`0937 | A173618 | 25.47 | low_review | 1994-06-10 | PROBATE OF WILL - LETTERS TESTAMENT | ARMSTRONG-D | LM=1 TR=1 EX=0`
`0938 | A173674 | 25.47 | low_review | 1994-06-14 | LETTERS OF ADMINISTRATION | MACLEAN-D | LM=1 TR=1 EX=0`
`0939 | A173686 | 25.47 | low_review | 1994-06-15 | PROBATE OF WILL - LETTERS TESTAMENT | FREEMAN-D | LM=1 TR=1 EX=0`
`0940 | A173692 | 25.47 | low_review | 1994-06-15 | LETTERS OF ADMINISTRATION | CABALFIN-D | LM=1 TR=1 EX=0`
`0941 | A173712 | 25.47 | low_review | 1994-06-16 | LETTERS OF ADMINISTRATION | JENNINGS-D | LM=1 TR=1 EX=0`
`0942 | A173726 | 25.47 | low_review | 1994-06-17 | PROBATE OF WILL - LETTERS TESTAMENT | FLETCHER-D | LM=1 TR=1 EX=0`
`0943 | A173797 | 25.47 | low_review | 1994-06-23 | SPOUSAL PROPERTY | LOPEZ-D | LM=1 TR=1 EX=0`
`0944 | A173938 | 25.47 | low_review | 1994-07-05 | PROBATE OF WILL - LETTERS TESTAMENT | WILCOX-D | LM=1 TR=1 EX=0`
`0945 | A173940 | 25.47 | low_review | 1994-07-05 | PROBATE OF WILL - LETTERS TESTAMENT | KROEKER-D | LM=1 TR=1 EX=0`
`0946 | A174035 | 25.47 | low_review | 1994-07-12 | PROBATE OF WILL - LETTERS TESTAMENT | WALTER-D | LM=1 TR=1 EX=0`
`0947 | A174036 | 25.47 | low_review | 1994-07-12 | PROBATE OF WILL - LETTERS TESTAMENT | MYERS-D | LM=2 TR=1 EX=0`
`0948 | A174041 | 25.47 | low_review | 1994-07-12 | PROBATE OF WILL - LETTERS TESTAMENT | ARMSTRONG-D | LM=1 TR=1 EX=0`
`0949 | A174062 | 25.47 | low_review | 1994-07-13 | TRUST PROCEEDINGS | WARD-T | LM=1 TR=1 EX=0`
`0950 | A174112 | 25.47 | low_review | 1994-07-18 | PROBATE OF WILL  - LETTERS OF ADMIN | BARRETT-D | LM=1 TR=1 EX=0`
`0951 | A174124 | 25.47 | low_review | 1994-07-18 | SPOUSAL PROPERTY | VAN DRUTEN-D | LM=2 TR=1 EX=0`
`0952 | A174294 | 25.47 | low_review | 1994-07-29 | PROBATE OF WILL - LETTERS TESTAMENT | WALKER-D | LM=1 TR=1 EX=0`
`0953 | A174357 | 25.47 | low_review | 1994-08-03 | PROBATE OF WILL - LETTERS TESTAMENT | CATLING-D | LM=2 TR=1 EX=0`
`0954 | A174376 | 25.47 | low_review | 1994-08-05 | PROBATE OF WILL  - LETTERS OF ADMIN | TAYLOR-D | LM=1 TR=1 EX=0`
`0955 | A174394 | 25.47 | low_review | 1994-08-08 | OTHER PROBATE MATTER | WALKER-D | LM=1 TR=1 EX=0`
`0956 | A174411 | 25.47 | low_review | 1994-08-08 | LETTERS OF ADMINISTRATION | TAYLOR-D | LM=1 TR=1 EX=0`
`0957 | A174415 | 25.47 | low_review | 1994-08-08 | OTHER PROBATE MATTER | ROWE-D | LM=1 TR=1 EX=0`
`0958 | A174463 | 25.47 | low_review | 1994-08-11 | LETTERS OF ADMINISTRATION | MILLER-D | LM=1 TR=1 EX=0`
`0959 | A174474 | 25.47 | low_review | 1994-08-11 | LETTERS OF ADMINISTRATION | MILLER-D | LM=1 TR=1 EX=0`
`0960 | A174490 | 25.47 | low_review | 1994-08-12 | PROBATE OF WILL  - LETTERS OF ADMIN | MILLER-D | LM=1 TR=1 EX=0`
`0961 | A174776 | 25.47 | low_review | 1994-09-02 | PROBATE OF WILL - LETTERS TESTAMENT | ROSENQUIST-D | LM=1 TR=1 EX=0`
`0962 | A174777 | 25.47 | low_review | 1994-09-02 | PROBATE OF WILL - LETTERS TESTAMENT | BRADLEY-D | LM=1 TR=1 EX=0`
`0963 | A174803 | 25.47 | low_review | 1994-09-07 | REAL PROPERTY OF SMALL VALUE (PROB  | STEINLE-D | LM=1 TR=1 EX=0`
`0964 | A174865 | 25.47 | low_review | 1994-09-12 | PROBATE OF WILL - LETTERS TESTAMENT | MITCHELL-D | LM=1 TR=1 EX=0`
`0965 | A174932 | 25.47 | low_review | 1994-09-16 | PROBATE OF WILL - LETTERS TESTAMENT | WADE-D | LM=1 TR=1 EX=0`
`0966 | A175204 | 25.47 | low_review | 1994-10-07 | PROBATE OF WILL  - LETTERS OF ADMIN | REYNOLDS-D | LM=1 TR=1 EX=0`
`0967 | A175274 | 25.47 | low_review | 1994-10-13 | PROBATE OF WILL - LETTERS TESTAMENT | REYNOLDS-T | LM=1 TR=1 EX=0`
`0968 | A176106 | 25.47 | low_review | 1994-12-22 | SPOUSAL PROPERTY | HOFFMAN-D | LM=1 TR=1 EX=0`
`0969 | A176429 | 25.47 | low_review | 1995-01-20 | PROBATE OF WILL - LETTERS TESTAMENT | HOFFMAN-D | LM=1 TR=1 EX=0`
`0970 | A176540 | 25.47 | low_review | 1995-01-27 | REAL PROPERTY OF SMALL VALUE (PROB  | GIBBS-D | LM=1 TR=1 EX=0`
`0971 | A176803 | 25.47 | low_review | 1995-02-17 | PROBATE OF WILL - LETTERS TESTAMENT | MARSHALL-D | LM=1 TR=1 EX=0`
`0972 | A176847 | 25.47 | low_review | 1995-02-22 | PROBATE OF WILL - LETTERS TESTAMENT | DAWSON-D | LM=1 TR=1 EX=0`
`0973 | A176869 | 25.47 | low_review | 1995-02-23 | LETTERS OF ADMINISTRATION | HOFFMAN-D | LM=1 TR=1 EX=0`
`0974 | A177114 | 25.47 | low_review | 1995-03-14 | PROBATE OF WILL - LETTERS TESTAMENT | FLORES-D | LM=1 TR=1 EX=0`
`0975 | A177278 | 25.47 | low_review | 1995-03-27 | LETTERS OF ADMINISTRATION | LOPEZ-D | LM=1 TR=1 EX=0`
`0976 | A177886 | 25.47 | low_review | 1995-05-09 | SPOUSAL PROPERTY | CHAPMAN-D | LM=1 TR=1 EX=0`
`0977 | A177971 | 25.47 | low_review | 1995-05-15 | PROBATE OF WILL - LETTERS TESTAMENT | CHAPMAN-D | LM=1 TR=1 EX=0`
`0978 | A178328 | 25.47 | low_review | 1995-06-12 | PROBATE OF WILL - LETTERS TESTAMENT | GONZALES-D | LM=1 TR=1 EX=0`
`0979 | A178333 | 25.47 | low_review | 1995-06-12 | PROBATE OF WILL - LETTERS TESTAMENT | HOFFMAN-D | LM=1 TR=1 EX=0`
`0980 | A178369 | 25.47 | low_review | 1995-06-14 | DETERMINE SUCCESSION TO PRIMARY RES | GONZALES-D | LM=1 TR=1 EX=0`
`0981 | A178739 | 25.47 | low_review | 1995-07-12 | PROBATE OF WILL - LETTERS TESTAMENT | WILSON-D | LM=1 TR=1 EX=0`
`0982 | A179092 | 25.47 | low_review | 1995-08-07 | PROBATE OF WILL - LETTERS TESTAMENT | ROGERS-D | LM=1 TR=1 EX=0`
`0983 | A179438 | 25.47 | low_review | 1995-09-01 | LETTERS OF ADMINISTRATION | SANCHEZ-D | LM=1 TR=1 EX=0`
`0984 | A180732 | 25.47 | low_review | 1995-12-15 | PROBATE OF WILL - LETTERS TESTAMENT | ROGERS-D | LM=1 TR=1 EX=0`
`0985 | A181259 | 25.47 | low_review | 1996-01-31 | PROBATE OF WILL - LETTERS TESTAMENT | WALLACE-D | LM=1 TR=1 EX=0`
`0986 | A181924 | 25.47 | low_review | 1996-03-20 | LETTERS OF ADMINISTRATION | WALLACE JR-D | LM=1 TR=1 EX=0`
`0987 | A182014 | 25.47 | low_review | 1996-03-27 | PROBATE OF WILL - LETTERS TESTAMENT | PARKER-D | LM=1 TR=1 EX=0`
`0988 | A182080 | 25.47 | low_review | 1996-04-02 | SPOUSAL PROPERTY | WALLACE-D | LM=1 TR=1 EX=0`
`0989 | A182149 | 25.47 | low_review | 1996-04-08 | PROBATE OF WILL - LETTERS TESTAMENT | CHAPMAN-D | LM=1 TR=1 EX=0`
`0990 | A182558 | 25.47 | low_review | 1996-05-07 | LETTERS OF ADMINISTRATION | PARKER-D | LM=1 TR=1 EX=0`
`0991 | A183338 | 25.47 | low_review | 1996-07-03 | TRUST PROCEEDINGS | WELLS-T | LM=1 TR=1 EX=0`
`0992 | A185155 | 25.47 | low_review | 1996-11-15 | PROBATE OF WILL  - LETTERS OF ADMIN | REED-D | LM=1 TR=1 EX=0`
`0993 | A186705 | 25.47 | low_review | 1997-03-20 | PROBATE OF WILL - LETTERS TESTAMENT | FISHER-D | LM=1 TR=1 EX=0`
`0994 | A187243 | 25.47 | low_review | 1997-04-28 | OTHER PROBATE MATTER | CARDILLO-ADULT WARD | LM=1 TR=1 EX=0`
`0995 | A187396 | 25.47 | low_review | 1997-05-08 | DETERMINE SUCCESSION TO PRIMARY RES | PLOTKIN-D | LM=1 TR=1 EX=0`
`0996 | A189825 | 25.47 | low_review | 1997-11-05 | PROBATE OF WILL - LETTERS TESTAMENT | QUINTERO-D | LM=1 TR=1 EX=0`
`0997 | A190033 | 25.47 | low_review | 1997-11-20 | SPOUSAL PROPERTY | JAMES-D | LM=1 TR=1 EX=0`
`0998 | A190095 | 25.47 | low_review | 1997-11-25 | PROBATE OF WILL - LETTERS TESTAMENT | COLOMBO-D | LM=1 TR=1 EX=0`
`0999 | A190112 | 25.47 | low_review | 1997-11-26 | PROBATE OF WILL - LETTERS TESTAMENT | JAMES-D | LM=1 TR=1 EX=0`
`1000 | A190202 | 25.47 | low_review | 1997-12-05 | PROBATE OF WILL  - LETTERS OF ADMIN | ARNOLD-D | LM=1 TR=1 EX=0`
`1001 | A190956 | 25.47 | low_review | 1998-02-04 | TRUST PROCEEDINGS | JACOBS-T | LM=1 TR=1 EX=0`
`1002 | A191223 | 25.47 | low_review | 1998-02-26 | TRUST PROCEEDINGS | ROSS-T | LM=1 TR=1 EX=0`
`1003 | A191353 | 25.47 | low_review | 1998-03-06 | PROBATE OF WILL - LETTERS TESTAMENT | FLEET-D | LM=1 TR=1 EX=0`
`1004 | A192416 | 25.47 | low_review | 1998-05-19 | LETTERS OF ADMINISTRATION | SANDERS-D | LM=1 TR=1 EX=0`
`1005 | A193208 | 25.47 | low_review | 1998-07-17 | PROBATE OF WILL - LETTERS TESTAMENT | BOOTH-D | LM=1 TR=1 EX=0`
`1006 | A194160 | 25.47 | low_review | 1998-09-24 | PROBATE OF WILL - LETTERS TESTAMENT | CONNELL-D | LM=1 TR=1 EX=0`
`1007 | A194410 | 25.47 | low_review | 1998-10-14 | LETTERS OF ADMINISTRATION | JENSEN JR-D | LM=1 TR=1 EX=0`
`1008 | A194475 | 25.47 | low_review | 1998-10-19 | PROBATE OF WILL - LETTERS TESTAMENT | CONNELL-D | LM=1 TR=1 EX=0`
`1009 | A194641 | 25.47 | low_review | 1998-10-30 | TRUST PROCEEDINGS | STEWARD-T | LM=1 TR=1 EX=0`
`1010 | A194928 | 25.47 | low_review | 1998-11-24 | PROBATE OF WILL - LETTERS TESTAMENT | GREEN-D | LM=1 TR=1 EX=0`
`1011 | A194969 | 25.47 | low_review | 1998-11-30 | PROBATE OF WILL - LETTERS TESTAMENT | JENSEN-D | LM=1 TR=1 EX=0`
`1012 | A195011 | 25.47 | low_review | 1998-12-02 | PROBATE OF WILL - LETTERS TESTAMENT | **JENSEN-D CONSOLIDATED INTO A194969 | LM=1 TR=1 EX=0`
`1013 | A195671 | 25.47 | low_review | 1999-01-27 | OTHER PROBATE MATTER | JENSEN-M | LM=1 TR=1 EX=0`
`1014 | A196367 | 25.47 | low_review | 1999-03-17 | LETTERS OF ADMINISTRATION | MACALUSO-D | LM=1 TR=1 EX=0`
`1015 | A198989 | 25.47 | low_review | 1999-09-17 | PROBATE OF WILL - LETTERS TESTAMENT | DOUGHERTY-D | LM=1 TR=1 EX=0`
`1016 | A200198 | 25.47 | low_review | 1999-12-13 | SPOUSAL PROPERTY | FRANKLIN-D | LM=1 TR=1 EX=0`
`1017 | A202199 | 25.47 | low_review | 2000-05-02 | TRUST PROCEEDINGS | SIMPSON-T | LM=1 TR=1 EX=0`
`1018 | A202317 | 25.47 | low_review | 2000-05-11 | PROBATE OF WILL - LETTERS TESTAMENT | PEARSON-D | LM=1 TR=1 EX=0`
`1019 | A203261 | 25.47 | low_review | 2000-07-14 | PROBATE OF WILL - LETTERS TESTAMENT | WINN-D | LM=1 TR=1 EX=0`
`1020 | A203326 | 25.47 | low_review | 2000-07-19 | LETTERS OF ADMINISTRATION | HANSON-D | LM=1 TR=1 EX=0`
`1021 | A205463 | 25.47 | low_review | 2000-12-20 | PROBATE OF WILL - LETTERS TESTAMENT | BLACK-D | LM=1 TR=1 EX=0`
`1022 | A210047 | 25.47 | low_review | 2001-09-28 | TRUST PROCEEDINGS | DIXON-T | LM=1 TR=1 EX=0`
`1023 | A210709 | 25.47 | low_review | 2001-11-15 | TRUST PROCEEDINGS | PETERSEN-T | LM=1 TR=1 EX=0`
`1024 | A211048 | 25.47 | low_review | 2001-12-11 | PROBATE OF WILL - LETTERS TESTAMENT | BAY-D | LM=1 TR=1 EX=0`
`1025 | A211071 | 25.47 | low_review | 2001-12-12 | SPOUSAL PROPERTY | MADRIGAL-D | LM=1 TR=1 EX=0`
`1026 | A211121 | 25.47 | low_review | 2001-12-14 | PROBATE OF WILL  - LETTERS OF ADMIN | RICHTER-D | LM=1 TR=1 EX=0`
`1027 | A211216 | 25.47 | low_review | 2001-12-21 | PROBATE OF WILL - LETTERS TESTAMENT | BOYD-D` | LM=1 TR=1 EX=0`
`1028 | A211621 | 25.47 | low_review | 2002-01-24 | LETTERS OF ADMINISTRATION | RICHARDS-D | LM=1 TR=1 EX=0`
`1029 | A211632 | 25.47 | low_review | 2002-01-24 | LETTERS OF ADMINISTRATION | MEYER-D | LM=1 TR=1 EX=0`
`1030 | A211660 | 25.47 | low_review | 2002-01-25 | LETTERS OF ADMINISTRATION | QUINTERO-D | LM=1 TR=1 EX=0`
`1031 | A211662 | 25.47 | low_review | 2002-01-25 | OTHER PROBATE MATTER | DRAKE-M | LM=1 TR=1 EX=0`
`1032 | A211719 | 25.47 | low_review | 2002-01-29 | PROBATE OF WILL - LETTERS TESTAMENT | WEAVER-D | LM=1 TR=1 EX=0`
`1033 | A211742 | 25.47 | low_review | 2002-01-31 | TRUST PROCEEDINGS | FRENCH-T | LM=1 TR=1 EX=0`
`1034 | A211770 | 25.47 | low_review | 2002-02-01 | LETTERS OF ADMINISTRATION | SONG-D | LM=1 TR=1 EX=0`
`1035 | A211785 | 25.47 | low_review | 2002-02-01 | REAL PROPERTY OF SMALL VALUE (PROB  | LIM-D | LM=1 TR=1 EX=0`
`1036 | A211822 | 25.47 | low_review | 2002-02-05 | PROBATE OF WILL  - LETTERS OF ADMIN | FABER-D | LM=1 TR=1 EX=0`
`1037 | A211873 | 25.47 | low_review | 2002-02-07 | TRUST PROCEEDINGS | MELTON-T | LM=1 TR=1 EX=0`
`1038 | A212100 | 25.47 | low_review | 2002-02-21 | PROBATE OF WILL - LETTERS TESTAMENT | AITKEN-D | LM=1 TR=1 EX=0`
`1039 | A212114 | 25.47 | low_review | 2002-02-22 | LETTERS OF ADMINISTRATION | SPENCER-D | LM=1 TR=1 EX=0`
`1040 | A212151 | 25.47 | low_review | 2002-02-25 | TRUST PROCEEDINGS | BOYD-T | LM=1 TR=1 EX=0`
`1041 | A212281 | 25.47 | low_review | 2002-03-05 | LETTERS OF ADMINISTRATION | PIERCE-D | LM=1 TR=1 EX=0`
`1042 | A212348 | 25.47 | low_review | 2002-03-08 | TRUST PROCEEDINGS | SHAFFER-T | LM=1 TR=1 EX=0`
`1043 | A212498 | 25.47 | low_review | 2002-03-19 | TRUST PROCEEDINGS | JENSEN-T | LM=1 TR=1 EX=0`
`1044 | A212586 | 25.47 | low_review | 2002-03-25 | PROBATE OF WILL  - LETTERS OF ADMIN | PETERSEN-D | LM=1 TR=1 EX=0`
`1045 | A212640 | 25.47 | low_review | 2002-03-27 | PROBATE OF WILL - LETTERS TESTAMENT | MILLAR-D | LM=1 TR=1 EX=0`
`1046 | A212682 | 25.47 | low_review | 2002-04-02 | LETTERS OF ADMINISTRATION | JENSEN-D | LM=1 TR=1 EX=0`
`1047 | A212783 | 25.47 | low_review | 2002-04-04 | PROBATE OF WILL - LETTERS TESTAMENT | GLEAVES-D | LM=1 TR=1 EX=0`
`1048 | A212784 | 25.47 | low_review | 2002-04-04 | LETTERS OF ADMINISTRATION | PRATT-D | LM=1 TR=1 EX=0`
`1049 | A212827 | 25.47 | low_review | 2002-04-09 | PROBATE OF WILL - LETTERS TESTAMENT | FRANKLIN-D | LM=1 TR=1 EX=0`
`1050 | A212874 | 25.47 | low_review | 2002-04-10 | OTHER PROBATE MATTER | WALL-MISC | LM=1 TR=1 EX=0`
`1051 | A213040 | 25.47 | low_review | 2002-04-22 | TRUST PROCEEDINGS | MASON-T | LM=1 TR=1 EX=0`
`1052 | A213062 | 25.47 | low_review | 2002-04-22 | PROBATE OF WILL - LETTERS TESTAMENT | HANSON-D | LM=1 TR=1 EX=0`
`1053 | A213146 | 25.47 | low_review | 2002-04-26 | PROBATE OF WILL - LETTERS TESTAMENT | BOYD-D | LM=1 TR=1 EX=0`
`1054 | A213147 | 25.47 | low_review | 2002-04-26 | LETTERS OF ADMINISTRATION | MASON-D | LM=1 TR=1 EX=0`
`1055 | A213177 | 25.47 | low_review | 2002-04-29 | PROBATE OF WILL - LETTERS TESTAMENT | RIVAS-D | LM=1 TR=1 EX=0`
`1056 | A213218 | 25.47 | low_review | 2002-05-01 | PROBATE OF WILL - LETTERS TESTAMENT | MARQUEZ-D | LM=1 TR=1 EX=0`
`1057 | A213335 | 25.47 | low_review | 2002-05-08 | PROBATE OF WILL - LETTERS TESTAMENT | HITT-D | LM=1 TR=1 EX=0`
`1058 | A213380 | 25.47 | low_review | 2002-05-13 | LETTERS OF ADMINISTRATION | WEBER-D | LM=1 TR=1 EX=0`
`1059 | A213568 | 25.47 | low_review | 2002-05-23 | PROBATE OF WILL - LETTERS TESTAMENT | WEBER-D | LM=1 TR=1 EX=0`
`1060 | A213571 | 25.47 | low_review | 2002-05-24 | LETTERS OF ADMINISTRATION | PAGE-D | LM=1 TR=1 EX=0`
`1061 | A213775 | 25.47 | low_review | 2002-06-07 | DETERMINE SUCCESSION TO PRIMARY RES | ABBOTT-D | LM=1 TR=1 EX=0`
`1062 | 01C15995 | 25.47 | low_review | 2002-06-10 | OTHER PROBATE MATTER | FULLER VS GLENN | LM=1 TR=1 EX=0`
`1063 | A214089 | 25.47 | low_review | 2002-06-26 | PROBATE OF WILL - LETTERS TESTAMENT | PALMER-D | LM=1 TR=1 EX=0`
`1064 | A214193 | 25.47 | low_review | 2002-07-02 | PROBATE OF WILL - LETTERS TESTAMENT | WEBB-D | LM=1 TR=1 EX=0`
`1065 | A214195 | 25.47 | low_review | 2002-07-02 | SPOUSAL PROPERTY | WEBB-D | LM=1 TR=1 EX=0`
`1066 | A214197 | 25.47 | low_review | 2002-07-02 | PROBATE OF WILL - LETTERS TESTAMENT | HARRINGTON-D | LM=1 TR=1 EX=0`
`1067 | A214360 | 25.47 | low_review | 2002-07-15 | TRUST PROCEEDINGS | HENRY-T | LM=1 TR=1 EX=0`
`1068 | A214376 | 25.47 | low_review | 2002-07-15 | PROBATE OF WILL - LETTERS TESTAMENT | BARRINGTON-D | LM=1 TR=1 EX=0`
`1069 | A214445 | 25.47 | low_review | 2002-07-18 | TRUST PROCEEDINGS | SNYDER-T | LM=1 TR=1 EX=0`
`1070 | A214493 | 25.47 | low_review | 2002-07-22 | TRUST PROCEEDINGS | FITZPATRICK-T | LM=1 TR=1 EX=0`
`1071 | A214631 | 25.47 | low_review | 2002-07-30 | TRUST PROCEEDINGS | BEAVER-T | LM=1 TR=1 EX=0`
`1072 | A214782 | 25.47 | low_review | 2002-08-08 | TRUST PROCEEDINGS | BUSBY-T | LM=1 TR=1 EX=0`
`1073 | A214823 | 25.47 | low_review | 2002-08-12 | PROBATE OF WILL - LETTERS TESTAMENT | REID-D | LM=1 TR=1 EX=0`
`1074 | A215305 | 25.47 | low_review | 2002-09-09 | TRUST PROCEEDINGS | FITZPATRICK-T | LM=1 TR=1 EX=0`

## Verification Plan

- Pull official court dockets/minute orders for high and medium leads, especially vulnerable-population cases.
- Pull official RecorderWorks document images for sampled transfer/distress instruments; index rows alone are not enough.
- Extract APNs from official document images and join to OC GIS/assessor sources for parcel-specific chronology.
- Separate institutional parties, family members, attorneys, clinicians, nonprofits, utilities, and title/finance parties before inference.
- Treat common surnames as lead terms only until full-name, APN, signature, address, or official-record corroboration is found.
- Continue 2002-2010 backfill using compact compressed batch mode, starting with 2205 only after confirming no stale collector process.

## Source Artifact Hash Appendix

exports/fraud_confidence_scores.csv | size=326584
`sha256=99f8b2a4953cc9b6a8fb053d165d3bc421be7fc30ece365c9d1ecdaf72165b41`
exports/fraud_confidence_scores_top250.csv | size=92654
`sha256=4eb5c19df120311ebbdac1652621f2fdf2d2ae485055e2a1fddaef5911d47bdb`
exports/fraud_confidence_score_summary.json | size=2194
`sha256=8390affcbdc812817f602d5e2e2733584c0def2f61d02e113a8a869c47b1c9d2`
exports/fraud_confidence_score_methodology.md | size=1415
`sha256=07562805c9ceb138c578f1f03a8623bf971f99cda56b07ba0de3184b887c6f12`
exports/fraud_packet_year_coverage_audit/summary.json | size=10714
`sha256=cd4cc201754258d2e356daac6be2b3b21a5518552d01cc3e212679aa020086c3`
exports/fraud_packet_year_coverage_audit/report.md | size=2595
`sha256=366227f9b5cac7b6066c6294ed54fb67dea401f250924dbc78d93d348ebad2a9`
exports/probate_case_recorder_window_summary.json | size=924
`sha256=f1a94919c7dfcca971e5edc239dcf3db86220014bdceeda54a8e380f8efbdb6e`
exports/recorder_backfill_plan/summary.json | size=774
`sha256=95d4717d0c89759cc90417aecae42a42119cd94fd5ea5fabe794fdcc9446722c`
exports/identity_weighted_actor_connections/identity_weighted_actor_connections_summary.json | size=47264
`sha256=870a6ab287f1ca64a5ea9eb1838bdadafd6201fd95b2d8bf712c5b579e79cf8c`
exports/identity_weighted_actor_connections/palmer_identity_drilldown.csv | size=529873
`sha256=86ca9326a29e2bd30b83f5934f80570df4221ae127e9c30be0bfd6c3f5b21638`
exports/identity_connection_paths/connection_path_summary.json | size=16544
`sha256=fe664ff23a8842a0ef108cbe2100610206afd116439cfa543958b37c0e02cf7c`
exports/oc_rescue_mission_bridge_graph/oc_rescue_mission_bridge_summary.json | size=2157
`sha256=7d6910a2dfc9430d6858e734b6eb6432801c63ef8fd51a891036067919af04da`
exports/oc_rescue_mission_bridge_graph/oc_rescue_mission_bridge_report.md | size=1507
`sha256=b32eb25d36993fc4853d10a2a706a6680573bee07bc07affddef3c9607d85b3d`
exports/medium_review_dossiers_summary.json | size=606
`sha256=a4042270b6d71166ce0d4c2a1a5e99692e5743de96e99d7b3f9eca260a569f71`
exports/medium_review_dossiers_index.md | size=39616
`sha256=da38b0709c7d2bc384f031ff9ef1effe646d2713d666d96f51565b572224cd49`
exports/medium_review_dossiers/A171502__rank_002__SHELDON.md | size=5018
`sha256=a3b586e7ceab9c463feffb51d3d4c7bd479f60edfbf09f5558574ec0ef94d06c`
exports/medium_review_dossiers/A182843__rank_027__PALMER.md | size=4881
`sha256=4a9747a66d486f8e64a29caf1daeabe8cf54911e7b849051ab9a49d79d31cc86`
exports/newsdesk_palmer_sheldon_packet.pdf | size=2363067
`sha256=77d4eeef41f584f9a32cb7f492a61526754645f24c320229bac4ebf815b5c95c`
exports/backup_fold_manifest_primary_writable_20260610T2345Z.json | size=1035
`sha256=8ca55a084bd1de116df09cfa26320a258cfc13ef52bb6ee3b173cf30f4ccbf6f`
