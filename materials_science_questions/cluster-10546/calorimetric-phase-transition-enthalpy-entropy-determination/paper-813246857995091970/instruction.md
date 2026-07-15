# Structural Metrics of an Iron(II) Spin Crossover Complex from Crystallographic Data

## Problem background
Spin crossover (SCO) compounds can switch between low-spin (LS) and high-spin (HS) electronic states, a transition accompanied by measurable changes in metal–ligand bond distances and coordination geometry. The compound trans-[Fe(tzpy)₂(NCSe)₂] (tzpy = 3-(2-pyridyl)-[1,2,3]triazolo[1,5-a]pyridine) has been crystallographically characterized at 120 K, where the iron(II) centre is in the LS state, and at 325 K, where it is essentially in the HS state. The deposited crystal structures (CCDC 915013 and 915014) provide atomic coordinates that allow direct calculation of the structural metrics that correlate with the spin-state change. This task asks you to compute those metrics from the public crystallographic data to quantify the structural signature of the SCO behaviour.

## Approach
Obtain the CIF files for the two temperatures from the Cambridge Structural Database. For each structure, parse the unit cell, space group, and atomic coordinates. Identify the iron atom and its six coordinating nitrogen atoms (using the atom labels Fe, N(1), N(2), N(3) and their symmetry equivalents). From these coordinates, calculate:
- the six individual Fe–N bond lengths and their average (Fe–Nav);
- the trigonal distortion parameter Φ, defined as the average of |60° − θᵢ| over the 24 face superposition angles of the octahedron;
- the octahedral distortion parameter Σ, defined as the sum of absolute deviations from 90° of the twelve cis N–Fe–N angles;
- the Fe–N(3)–C(12) angle;
- all intermolecular C···C contact distances listed in Table 3 of the source work, using the specified symmetry operations (i: x+1, y, z; ii: −x+2, −y−1, −z+1; iii: −x, −y, −z+2) and the atom labels given in that table.
Perform this analysis for both the 120 K and 325 K structures independently. Collect all results into a single JSON file as described in the workflow steps.

## Reproduction target
Produce the file `step_01_structural_metrics.json` containing, for each temperature (120 K and 325 K):
- `Fe_N_bonds`: an array of the six Fe–N bond lengths (Å),
- `Fe_N_av`: the average Fe–N bond length (Å),
- `trigonal_distortion_Phi`: the trigonal distortion Φ (degrees),
- `octahedral_distortion_Sigma`: the octahedral distortion Σ (degrees),
- `Fe_N3_C12_angle`: the Fe–N(3)–C(12) angle (degrees),
- `intermolecular_contacts`: an object whose keys are contact labels (e.g., "C1…C10_i") and whose values are the corresponding C···C distances (Å) exactly as defined in Table 3 of the source paper.
Also include a top‑level key `Delta_Fe_N_av` with the difference Fe_N_av(325 K) − Fe_N_av(120 K) (Å).

## Assets

- CCDC 915013 – Crystal structure of trans-[Fe(tzpy)₂(NCSe)₂] at 120 K: https://www.ccdc.cam.ac.uk/structures/search?identifier=915013
- CCDC 915014 – Crystal structure of trans-[Fe(tzpy)₂(NCSe)₂] at 325 K: https://www.ccdc.cam.ac.uk/structures/search?identifier=915014

## Workflow steps

### Step 1: Compute structural metrics from CIF files
- Role: scored (load-bearing)
- Action: Download the CIF files for CCDC 915013 (120 K) and 915014 (325 K) from the Cambridge Structural Database. Parse each CIF to extract atomic coordinates, unit cell parameters, and space group. Identify the Fe atom and its six coordinating N atoms (using atom labels consistent with the paper: Fe, N(1), N(2), N(3) and their symmetry equivalents). Compute: (i) the six Fe–N bond lengths and their average Fe–N_av, and the difference Δ(Fe–N_av); (ii) the trigonal distortion parameter Φ (average of |60° – θ_i| over the 24 face superposition angles); (iii) the octahedral distortion parameter Σ (sum of absolute deviations from 90° of the twelve cis N–Fe–N angles); (iv) the Fe–N(3)–C(12) angle; (v) all intermolecular C···C contact distances listed in Table 3 of the paper, using the specified symmetry operations (i: x+1, y, z; ii: -x+2, -y-1, -z+1; iii: -x, -y, -z+2) and atom labels. Write all results to step_01_structural_metrics.json.
- Output file: `/app/outputs/step_01_structural_metrics.json`
- Format: json
- Contract: JSON object with top-level keys 'temp_120_K' and 'temp_325_K'. Each value is an object containing: 'Fe_N_bonds' (list of 6 floats, individual Fe–N bond lengths in Å), 'Fe_N_av' (float, average bond length), 'trigonal_distortion_Phi' (float, degrees), 'octahedral_distortion_Sigma' (float, degrees), 'Fe_N3_C12_angle' (float, degrees), 'intermolecular_contacts' (object where each key is a contact label string, e.g. 'C1...C10_i', and the value is the distance in Å). Optionally include top-level 'Delta_Fe_N_av' (float, difference Fe_N_av(325 K) - Fe_N_av(120 K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_metrics.json
- path: `/app/outputs/step_01_structural_metrics.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Structural metrics (bond lengths, angles, distortion parameters, intermolecular contacts) computed from the deposited crystallographic data at 120 K and 325 K.
- schema:
  - `type`: object
  - `required`: `temp_120_K`, `temp_325_K`
  - `properties`:
    - `temp_120_K`:
      - `type`: object
      - `required`: `Fe_N_bonds`, `Fe_N_av`, `trigonal_distortion_Phi`, `octahedral_distortion_Sigma`, `Fe_N3_C12_angle`, `intermolecular_contacts`
      - `properties`:
        - `Fe_N_bonds`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 6
          - `maxItems`: 6
          - `unit`: angstrom
        - `Fe_N_av`:
          - `type`: number
          - `unit`: angstrom
        - `trigonal_distortion_Phi`:
          - `type`: number
          - `unit`: degrees
        - `octahedral_distortion_Sigma`:
          - `type`: number
          - `unit`: degrees
        - `Fe_N3_C12_angle`:
          - `type`: number
          - `unit`: degrees
        - `intermolecular_contacts`:
          - `type`: object
          - `additionalProperties`:
            - `type`: number
            - `unit`: angstrom
    - `temp_325_K`:
      - `type`: object
      - `required`: `Fe_N_bonds`, `Fe_N_av`, `trigonal_distortion_Phi`, `octahedral_distortion_Sigma`, `Fe_N3_C12_angle`, `intermolecular_contacts`
      - `properties`:
        - `Fe_N_bonds`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 6
          - `maxItems`: 6
          - `unit`: angstrom
        - `Fe_N_av`:
          - `type`: number
          - `unit`: angstrom
        - `trigonal_distortion_Phi`:
          - `type`: number
          - `unit`: degrees
        - `octahedral_distortion_Sigma`:
          - `type`: number
          - `unit`: degrees
        - `Fe_N3_C12_angle`:
          - `type`: number
          - `unit`: degrees
        - `intermolecular_contacts`:
          - `type`: object
          - `additionalProperties`:
            - `type`: number
            - `unit`: angstrom
    - `Delta_Fe_N_av`:
      - `type`: number
      - `unit`: angstrom
      - `description`: Fe_N_av(325 K) - Fe_N_av(120 K)
  - `additionalProperties`: False

Notes: All values are fixed by the crystal structure and must match the paper's reported values within prescribed tolerances (exact match policy).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "temp_120_K",
          "temp_325_K"
        ],
        "properties": {
          "temp_120_K": {
            "type": "object",
            "required": [
              "Fe_N_bonds",
              "Fe_N_av",
              "trigonal_distortion_Phi",
              "octahedral_distortion_Sigma",
              "Fe_N3_C12_angle",
              "intermolecular_contacts"
            ],
            "properties": {
              "Fe_N_bonds": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 6,
                "maxItems": 6,
                "unit": "angstrom"
              },
              "Fe_N_av": {
                "type": "number",
                "unit": "angstrom"
              },
              "trigonal_distortion_Phi": {
                "type": "number",
                "unit": "degrees"
              },
              "octahedral_distortion_Sigma": {
                "type": "number",
                "unit": "degrees"
              },
              "Fe_N3_C12_angle": {
                "type": "number",
                "unit": "degrees"
              },
              "intermolecular_contacts": {
                "type": "object",
                "additionalProperties": {
                  "type": "number",
                  "unit": "angstrom"
                }
              }
            }
          },
          "temp_325_K": {
            "type": "object",
            "required": [
              "Fe_N_bonds",
              "Fe_N_av",
              "trigonal_distortion_Phi",
              "octahedral_distortion_Sigma",
              "Fe_N3_C12_angle",
              "intermolecular_contacts"
            ],
            "properties": {
              "Fe_N_bonds": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 6,
                "maxItems": 6,
                "unit": "angstrom"
              },
              "Fe_N_av": {
                "type": "number",
                "unit": "angstrom"
              },
              "trigonal_distortion_Phi": {
                "type": "number",
                "unit": "degrees"
              },
              "octahedral_distortion_Sigma": {
                "type": "number",
                "unit": "degrees"
              },
              "Fe_N3_C12_angle": {
                "type": "number",
                "unit": "degrees"
              },
              "intermolecular_contacts": {
                "type": "object",
                "additionalProperties": {
                  "type": "number",
                  "unit": "angstrom"
                }
              }
            }
          },
          "Delta_Fe_N_av": {
            "type": "number",
            "unit": "angstrom",
            "description": "Fe_N_av(325 K) - Fe_N_av(120 K)"
          }
        },
        "additionalProperties": false
      },
      "description": "Structural metrics (bond lengths, angles, distortion parameters, intermolecular contacts) computed from the deposited crystallographic data at 120 K and 325 K."
    }
  ],
  "notes": "All values are fixed by the crystal structure and must match the paper's reported values within prescribed tolerances (exact match policy)."
}
```

## How you are scored
A hidden verifier independently downloads the same CIF files (CCDC 915013, 915014) and recomputes every metric using a reference crystallographic toolchain. It compares your submitted values for each quantity (bond lengths, angles, distortion parameters, contact distances) against the recomputed values. The reward is based on the agreement between your computed numbers and the verifier's recomputation. Simply reporting literature values without performing the actual computation will not satisfy the verifier.
