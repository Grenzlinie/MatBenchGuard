# Compute Convex Hull and Stability Descriptors for Ag-Au-Cd using AFLOW-CHULL

## Problem background
Predicting the thermodynamic stability of materials is a central challenge in computational materials science. A key tool is the convex hull construction: given the formation enthalpies of candidate phases, the convex hull identifies which compositions are stable against decomposition into other phases or elemental end-members. Autonomous hull analysis enables high-throughput screening for synthesizable compounds and provides quantitative stability descriptors such as the distance to the hull and the stability criterion. AFLOW-CHULL is an open-source module that automates the full pipeline — from retrieval of DFT-calculated formation enthalpy data through to hull construction and thermodynamic characterization — making phase stability analysis accessible for multi-component systems.

## Approach
AFLOW-CHULL operates by fetching structural and energetic data from the AFLOW.org repository via the AFLUX search API. For a given chemical system, it collects entries for all subsystems (unary, binary, ternary, etc.), performs built-in data validation (outlier detection, duplicate removal, and convergence checks), and constructs the convex hull using an iterative half-space partitioning algorithm adapted for thermodynamic data. The module then computes a suite of descriptors: formation enthalpy, ground‑state classification, stability criterion (the distance of a stable phase from a pseudo‑hull built without it), distance to the hull for unstable phases, decomposition reactions, and phase coexistence. The analysis is executed as a single command‑line invocation that writes the results to a structured JSON file containing `points_data` (per‑compound descriptors) and `facets_data` (hull facet definitions).

## Reproduction target
Compute the convex hull and thermodynamic descriptors for the ternary system Ag–Au–Cd by running AFLOW-CHULL. The output must be written to `aflow_AgAuCd_hull.json`, a JSON object with top‑level keys `points_data` and `facets_data` as described in the step contract. The compound of primary interest is Ag₂AuCd (AUID aflow:b306fb2e8866a640). Your file must include this compound in `points_data` with its `formation_enthalpy_atom` (meV/atom), `stability_criterion` (meV/atom), and `ground_state` flag, all obtained from a genuine AFLOW-CHULL calculation using the standard PAW‑PBE data available through AFLOW.org.

## Assets

- AFLOW (including AFLOW-CHULL): https://aflow.org/src/aflow
- AFLOW.org repository of materials properties: http://aflowlib.duke.edu
- AFLUX Search API: http://aflowlib.duke.edu/search/API/

## Workflow steps

### Step 1: Run AFLOW-CHULL for Ag-Au-Cd and export thermodynamic analysis
- Role: scored (load-bearing)
- Action: Install and run AFLOW-CHULL (the AFLOW convex hull module) to retrieve structural and formation-enthalpy data for the Ag-Au-Cd system from the AFLOW.org repository via the AFLUX API, perform built-in data validation (outlier/duplicate detection), construct the ternary convex hull, compute thermodynamic descriptors (formation enthalpies, stability criterion, distance to hull, decomposition reactions, phase coexistence), and write the complete results to aflow_AgAuCd_hull.json.
- Output file: `/app/outputs/aflow_AgAuCd_hull.json`
- Format: json
- Contract: A JSON object with top-level keys 'points_data' (list of objects) and 'facets_data' (list of objects). Each object in points_data must include fields: compound (string), auid (string), formation_enthalpy_atom (float, meV/atom), stability_criterion (float, meV/atom), ground_state (boolean), and optionally other descriptor fields. facets_data holds hull facet definitions with vertices coordinates and auids.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/aflow_AgAuCd_hull.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### aflow_AgAuCd_hull.json
- path: `/app/outputs/aflow_AgAuCd_hull.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Convex hull results for Ag-Au-Cd; the checker will verify specific entries for formation enthalpy, stability criterion, and ground-state flag against hidden reference values.
- schema:
  - `type`: object
  - `required_top_level_keys`: `points_data`, `facets_data`
  - `points_data`:
    - `type`: array
    - `items`:
      - `required_fields`: `compound`, `auid`, `formation_enthalpy_atom`, `stability_criterion`, `ground_state`
      - `field_types`:
        - `compound`: string
        - `auid`: string
        - `formation_enthalpy_atom`: float (meV/atom)
        - `stability_criterion`: float (meV/atom)
        - `ground_state`: boolean
  - `facets_data`:
    - `type`: array
    - `description`: list of facet objects with vertices positions and identifiers

Notes: The output contract covers the single scored artifact. The checker will locate the entry with compound='Ag2AuCd' and auid='aflow:b306fb2e8866a640' within points_data and compare its formation_enthalpy_atom, stability_criterion, and ground_state to hidden paper-reported values with appropriate tolerances (exact for boolean, tolerance windows for numerics).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "aflow_AgAuCd_hull.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_top_level_keys": [
          "points_data",
          "facets_data"
        ],
        "points_data": {
          "type": "array",
          "items": {
            "required_fields": [
              "compound",
              "auid",
              "formation_enthalpy_atom",
              "stability_criterion",
              "ground_state"
            ],
            "field_types": {
              "compound": "string",
              "auid": "string",
              "formation_enthalpy_atom": "float (meV/atom)",
              "stability_criterion": "float (meV/atom)",
              "ground_state": "boolean"
            }
          }
        },
        "facets_data": {
          "type": "array",
          "description": "list of facet objects with vertices positions and identifiers"
        }
      },
      "description": "Convex hull results for Ag-Au-Cd; the checker will verify specific entries for formation enthalpy, stability criterion, and ground-state flag against hidden reference values."
    }
  ],
  "notes": "The output contract covers the single scored artifact. The checker will locate the entry with compound='Ag2AuCd' and auid='aflow:b306fb2e8866a640' within points_data and compare its formation_enthalpy_atom, stability_criterion, and ground_state to hidden paper-reported values with appropriate tolerances (exact for boolean, tolerance windows for numerics)."
}
```

## How you are scored
The hidden verifier will read your `aflow_AgAuCd_hull.json` file. It will locate the entry for Ag₂AuCd (auid aflow:b306fb2e8866a640) and compare your reported `formation_enthalpy_atom`, `stability_criterion`, and `ground_state` against confidential reference values. The comparison uses tolerances that account for legitimate computational variability. Your final reward is 1.0 if all checks pass, and 0.0 otherwise. The verifier expects numbers that result from an authentic AFLOW-CHULL run; do not attempt to reverse‑engineer or hardcode values.
