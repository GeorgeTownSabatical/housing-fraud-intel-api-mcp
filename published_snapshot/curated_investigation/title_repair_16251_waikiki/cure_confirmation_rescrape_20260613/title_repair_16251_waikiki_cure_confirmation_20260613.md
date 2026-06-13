# Cure-Confirmation Rescrape: 16251 Waikiki Ln

Generated UTC: `2026-06-13T14:24:00Z`

## Bottom Line

The refreshed data supports opening a title-cure / corrective-chain review for `16251 Waikiki Ln, Huntington Beach, CA 92649`.

This is not yet proof of a void transfer. It is a high-confidence record-chain target because the current RecorderWorks index and detail scrape confirm a grant deed and same-day deed of trust, the deed detail exposes transfer-tax and tract/lot fields, and the county GIS parcel endpoint confirms the APN/address identity.

## Cure Review Confidence

Score: `0.86 / 1.00` for need-to-cure investigation.

Basis:

- `+0.30` fresh RecorderWorks exact-document rescrape matched `2024000290531`.
- `+0.20` fresh RecorderWorks exact-document rescrape matched same-day financing companion `2024000290532`.
- `+0.20` deed detail exposed `Transfer Tax Amount: 1295.2500`, which computes to `$1,177,500`.
- `+0.15` deed detail exposed `City: Huntington Beach`, `Lot #: 90`, and `Tract #: 3750`.
- `+0.10` county GIS confirms APN `178-083-15` maps to `16251 WAIKIKI LN HUNTINGTON BEACH`.
- `-0.09` certified deed images and the 1994/2003/2005 chain documents are still needed before claiming a void transfer or naming who must disclaim.

## Fresh RecorderWorks Rescrape

Source: `https://cr.occlerkrecorder.gov/RecorderWorksInternet/`

Run artifact:

- `/Users/ALISTAIRE/housing-fraud-intel-api/exports/title_repair_16251_waikiki_rescrape_20260613_recorder_docnum_pull.csv`
- `/Users/ALISTAIRE/housing-fraud-intel-api/exports/title_repair_16251_waikiki_rescrape_20260613_recorder_docnum_pull_summary.json`
- `/Users/ALISTAIRE/housing-fraud-intel-api/exports/title_repair_16251_waikiki_rescrape_20260613_document_views/`

Fresh matched rows:

| Document | Type | Date | Grantor | Grantee | Portal doc id | Pages |
|---|---|---:|---|---|---:|---:|
| `2024000290531` | GRANT DEED | 11/6/2024 | BARTMAN GREGORY GEORGE TR | REDMOND ROBERT GODFREY RUTH | `31159554` | 3 |
| `2024000290532` | TRUST DEED | 11/6/2024 | REDMOND ROBERT GODFREY RUTH | V I P INDEPENDENT MORTGAGE; MORTGAGE ELECTRONIC REGISTRATION SYSTEMS INC | `31159532` | 37 |

Fresh details recovered from `2024000290531`:

| Field | Value |
|---|---|
| City | Huntington Beach |
| Transfer Tax Amount | `1295.2500` |
| Non Disc Tax Amount | `0.0000` |
| Lot # | `90` |
| Tract # | `3750` |
| Number of Pages | `3` |
| Recording Date | `11/6/2024` |

Computed consideration:

`1295.2500 / 1.10 * 1000 = 1,177,500`

Interpretation: the refreshed RecorderWorks detail independently supports the exact `$1,177,500` consideration figure already aligned with public listing-source sale history.

## County GIS Parcel Confirmation

Source:

`https://www.ocgis.com/arcpub/rest/services/Map_Layers/Parcels/MapServer/0/query?where=ASSESSMENT_NO%3D%27178-083-15%27&outFields=ASSESSMENT_NO,SITE_ADDRESS,YEAR_BUILT,NBR_BEDROOMS&returnGeometry=false&f=json`

Refreshed response:

| Field | Value |
|---|---|
| ASSESSMENT_NO | `178-083-15` |
| SITE_ADDRESS | `16251 WAIKIKI LN HUNTINGTON BEACH` |
| YEAR_BUILT | `1963` |
| NBR_BEDROOMS | `3` |

Interpretation: OC GIS confirms the APN/address identity. The deed itself still needs certified image/legal-description confirmation to prove that document `2024000290531` conveys this exact parcel.

## Public Sale-History Checkpoints

Current public listing-source checkpoints to verify against official chain documents:

| Public sale date | Public sale price | Status |
|---|---:|---|
| 11/6/2024 | `$1,177,500` | Matched exactly by RecorderWorks transfer-tax computation for `2024000290531`. |
| 12/2/2005 | `$729,000` | Public-history checkpoint only; official recorder instrument number still needed. |
| 9/3/2003 | `$483,000` | Public-history checkpoint only; official recorder instrument number still needed. |
| 3/15/1994 | `$206,000` | Public-history checkpoint only; official recorder instrument number still needed. |

Listing-source URLs:

- Redfin: `https://www.redfin.com/CA/Huntington-Beach/16251-Waikiki-Ln-92649/home/3868041`
- Zillow: `https://www.zillow.com/homedetails/16251-Waikiki-Ln-Huntington-Beach-CA-92649/25298849_zpid/`

Note: direct command-line archive capture for Redfin/Zillow returned empty responses in this environment, likely anti-bot blocking. Use the public pages as corroborative lead sources only; the official cure record should rely on RecorderWorks certified copies and assessor/parcel records.

## Why This Supports Cure Work

The cure need is supported by a record-chain gap, not by a completed fraud conclusion:

- Current deed target is identified: `2024000290531`.
- Current encumbrance/financing companion is identified: `2024000290532`.
- Current deed consideration has an exact transfer-tax-derived value match.
- Parcel identity has independent county GIS support through APN/address.
- The older public sale checkpoints identify the exact chain intervals that must be certified before determining the first defective or voidable conveyance.

## Next Pulls Required Before Demanding Cure

1. Pull certified/official copy of `2024000290531`.
2. Pull certified/official copy of `2024000290532`.
3. Extract APN, legal description, vesting, preparer, title/escrow, notary, and all signature authority language.
4. Run official chain search by APN/address for the 2005, 2003, and 1994 public sale checkpoints.
5. Pull companion trust deeds, reconveyances, substitutions, assignments, PCOR/DTT material if available, and any same-day adjacent documents.
6. Identify the first allegedly void or voidable transfer only after the certified chain confirms the grantor/grantee sequence.
7. Draft quitclaim/corrective deed demand only after confirming current holder, encumbrancers, and necessary disclaiming parties.
8. If refused, evaluate quiet title / cancellation of instrument as the more complete procedural vehicle.

## Evidence Boundary

This packet confirms a strong need for title-chain cure review. It does not independently prove fraud, void title, forged authority, or entitlement to relief. Certified official copies and legal review remain required.
