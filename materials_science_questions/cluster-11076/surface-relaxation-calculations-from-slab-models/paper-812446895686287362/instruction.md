# Surface energies and multilayer relaxation of diamond low-index planes by Tersoff and Brenner potentials

## Problem background
Diamond surfaces are central to coatings, thin-film technology, and semiconductor applications. The low-index (100), (110), and (111) planes exhibit distinct stability and growth behavior, but reliable quantitative data on their surface energies and atomic-scale relaxations remain scarce and vary widely across studies. A detailed understanding of these properties is essential for predicting and controlling diamond film formation. This task aims to compute surface energies and interlayer relaxations for these three diamond surfaces using classical molecular dynamics simulations with two widely used bond-order potentials, providing a reproducible benchmark for comparing the performance of the Tersoff and Brenner models.

## Approach
The approach employs classical molecular dynamics (MD) to simulate the diamond surfaces. Two empirical bond-order potentials for carbon—the Tersoff and Brenner functions—are implemented to capture both two-body repulsive/attractive forces and three-body angular bonding terms. For each potential, a perfect bulk diamond crystal is first relaxed to obtain the equilibrium lattice constant. Slab supercells are then constructed for the (100), (110), and (111) orientations with a vacuum region, exposing a single surface while maintaining periodic boundaries in the in-plane directions. Surface energy is computed as the difference between the total energy of the slab and that of an equivalent bulk system, normalized by the exposed surface area. Two regimes are considered: an unrelaxed setup where all atoms are fixed at ideal bulk positions, and a relaxed setup where the slab is allowed to equilibrate under MD at a controlled low temperature, permitting surface atoms to rearrange. After equilibration, interlayer spacings (δ12, δ23, δ34) parallel to the surface are measured and compared with their unrelaxed values to obtain multilayer relaxation percentages. The workflow is executed identically for both potentials, enabling a direct comparison of the predictions of the Tersoff and Brenner models for the same physical system.

## Reproduction target
The goal is to compute the following quantities for diamond (100), (110), and (111) surfaces using the Tersoff and Brenner potentials, and to record them in a single JSON file:

- Unrelaxed surface energy γ (erg/cm²).
- Relaxed surface energy γ (erg/cm²), after MD equilibration.
- Interlayer spacings δ12, δ23, δ34 (Å) before relaxation.
- Interlayer spacings δ12, δ23, δ34 (Å) after relaxation.
- Percentage change in each interlayer spacing upon relaxation.

The required output structure is specified in the output contract.

## Assets

- LAMMPS molecular dynamics package: https://lammps.sandia.gov/

## Workflow steps

### Step 1: Generate slab models
- Role: process
- Action: Construct diamond slab supercells for the (100), (110), and (111) planes with atom counts 64, 96, and 128 respectively. Determine the equilibrium lattice constants for the Tersoff and Brenner potentials. Compute the exposed surface area A for each orientation.
- Evidence: `/app/outputs/slab_info.txt`

### Step 2: Compute unrelaxed surface energies
- Role: process
- Action: For each surface and potential, run MD with fixed atomic positions (bulk-like distances) at 100 K. Use a time step of 0.5e-17 s, equilibration for 10,000 steps with temperature rescaling for the first 5,000 steps. Average the total energy over the last 1,000-step windows to obtain stable mean energies for the slab (E_s) and the bulk (E_b). Calculate unrelaxed gamma = (E_s - E_b) / A.
- Evidence: none

### Step 3: Compute relaxed surface energies
- Role: process
- Action: Starting from the unrelaxed slab configurations, allow all atoms to move and equilibrate under MD at 100 K with the same protocol. Average the final total energies to obtain relaxed E_s and E_b. Compute relaxed gamma.
- Evidence: none

### Step 4: Analyze multilayer relaxation
- Role: process
- Action: From the relaxed slab trajectories, extract the interlayer spacings (delta12, delta23, delta34) parallel to the surface for each orientation and potential. Compare with the unrelaxed spacings and compute the percentage changes.
- Evidence: none

### Step 5: Output final results
- Role: scored (load-bearing)
- Action: Write a JSON file containing all computed surface energies and interlayer relaxation data for the Tersoff and Brenner potentials, covering the (100), (110), and (111) surfaces.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys 'tersoff' and 'brenner'. Each value is an object with keys '(100)', '(110)', '(111)'. Each surface entry contains the following numeric fields: unrelaxed_gamma (float, erg/cm^2), relaxed_gamma (float, erg/cm^2), delta12_before (float, Å), delta12_after (float, Å), delta23_before (float, Å), delta23_after (float, Å), delta34_before (float, Å), delta34_after (float, Å), percent_change_delta12 (float, %), percent_change_delta23 (float, %), percent_change_delta34 (float, %).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Consolidated results of surface energies and interlayer spacings for both Tersoff and Brenner potentials.
- schema:
  - `type`: object
  - `required`: `tersoff`, `brenner`
  - `properties`:
    - `tersoff`:
      - `type`: object
      - `required`: `(100)`, `(110)`, `(111)`
      - `properties`:
        - `(100)`:
          - `type`: object
          - `required`: `unrelaxed_gamma`, `relaxed_gamma`, `delta12_before`, `delta12_after`, `delta23_before`, `delta23_after`, `delta34_before`, `delta34_after`, `percent_change_delta12`, `percent_change_delta23`, `percent_change_delta34`
        - `(110)`:
          - `type`: object
          - `required`: `unrelaxed_gamma`, `relaxed_gamma`, `delta12_before`, `delta12_after`, `delta23_before`, `delta23_after`, `delta34_before`, `delta34_after`, `percent_change_delta12`, `percent_change_delta23`, `percent_change_delta34`
        - `(111)`:
          - `type`: object
          - `required`: `unrelaxed_gamma`, `relaxed_gamma`, `delta12_before`, `delta12_after`, `delta23_before`, `delta23_after`, `delta34_before`, `delta34_after`, `percent_change_delta12`, `percent_change_delta23`, `percent_change_delta34`
    - `brenner`:
      - `type`: object
      - `required`: `(100)`, `(110)`, `(111)`
      - `properties`:
        - `(100)`:
          - `type`: object
          - `required`: `unrelaxed_gamma`, `relaxed_gamma`, `delta12_before`, `delta12_after`, `delta23_before`, `delta23_after`, `delta34_before`, `delta34_after`, `percent_change_delta12`, `percent_change_delta23`, `percent_change_delta34`
        - `(110)`:
          - `type`: object
          - `required`: `unrelaxed_gamma`, `relaxed_gamma`, `delta12_before`, `delta12_after`, `delta23_before`, `delta23_after`, `delta34_before`, `delta34_after`, `percent_change_delta12`, `percent_change_delta23`, `percent_change_delta34`
        - `(111)`:
          - `type`: object
          - `required`: `unrelaxed_gamma`, `relaxed_gamma`, `delta12_before`, `delta12_after`, `delta23_before`, `delta23_after`, `delta34_before`, `delta34_after`, `percent_change_delta12`, `percent_change_delta23`, `percent_change_delta34`
  - `definitions`:
    - `surface_entry`:
      - `type`: object
      - `properties`:
        - `unrelaxed_gamma`:
          - `type`: number
          - `units`: erg/cm^2
        - `relaxed_gamma`:
          - `type`: number
          - `units`: erg/cm^2
        - `delta12_before`:
          - `type`: number
          - `units`: Å
        - `delta12_after`:
          - `type`: number
          - `units`: Å
        - `delta23_before`:
          - `type`: number
          - `units`: Å
        - `delta23_after`:
          - `type`: number
          - `units`: Å
        - `delta34_before`:
          - `type`: number
          - `units`: Å
        - `delta34_after`:
          - `type`: number
          - `units`: Å
        - `percent_change_delta12`:
          - `type`: number
          - `units`: %
        - `percent_change_delta23`:
          - `type`: number
          - `units`: %
        - `percent_change_delta34`:
          - `type`: number
          - `units`: %

Notes: The checker compares each numerical value to the paper's reported values (Tables 1 and 2) with absolute tolerances appropriate for the computational method. The agent must implement the Tersoff and Brenner potentials explicitly using the parameters given in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "tersoff",
          "brenner"
        ],
        "properties": {
          "tersoff": {
            "type": "object",
            "required": [
              "(100)",
              "(110)",
              "(111)"
            ],
            "properties": {
              "(100)": {
                "type": "object",
                "required": [
                  "unrelaxed_gamma",
                  "relaxed_gamma",
                  "delta12_before",
                  "delta12_after",
                  "delta23_before",
                  "delta23_after",
                  "delta34_before",
                  "delta34_after",
                  "percent_change_delta12",
                  "percent_change_delta23",
                  "percent_change_delta34"
                ]
              },
              "(110)": {
                "type": "object",
                "required": [
                  "unrelaxed_gamma",
                  "relaxed_gamma",
                  "delta12_before",
                  "delta12_after",
                  "delta23_before",
                  "delta23_after",
                  "delta34_before",
                  "delta34_after",
                  "percent_change_delta12",
                  "percent_change_delta23",
                  "percent_change_delta34"
                ]
              },
              "(111)": {
                "type": "object",
                "required": [
                  "unrelaxed_gamma",
                  "relaxed_gamma",
                  "delta12_before",
                  "delta12_after",
                  "delta23_before",
                  "delta23_after",
                  "delta34_before",
                  "delta34_after",
                  "percent_change_delta12",
                  "percent_change_delta23",
                  "percent_change_delta34"
                ]
              }
            }
          },
          "brenner": {
            "type": "object",
            "required": [
              "(100)",
              "(110)",
              "(111)"
            ],
            "properties": {
              "(100)": {
                "type": "object",
                "required": [
                  "unrelaxed_gamma",
                  "relaxed_gamma",
                  "delta12_before",
                  "delta12_after",
                  "delta23_before",
                  "delta23_after",
                  "delta34_before",
                  "delta34_after",
                  "percent_change_delta12",
                  "percent_change_delta23",
                  "percent_change_delta34"
                ]
              },
              "(110)": {
                "type": "object",
                "required": [
                  "unrelaxed_gamma",
                  "relaxed_gamma",
                  "delta12_before",
                  "delta12_after",
                  "delta23_before",
                  "delta23_after",
                  "delta34_before",
                  "delta34_after",
                  "percent_change_delta12",
                  "percent_change_delta23",
                  "percent_change_delta34"
                ]
              },
              "(111)": {
                "type": "object",
                "required": [
                  "unrelaxed_gamma",
                  "relaxed_gamma",
                  "delta12_before",
                  "delta12_after",
                  "delta23_before",
                  "delta23_after",
                  "delta34_before",
                  "delta34_after",
                  "percent_change_delta12",
                  "percent_change_delta23",
                  "percent_change_delta34"
                ]
              }
            }
          }
        },
        "definitions": {
          "surface_entry": {
            "type": "object",
            "properties": {
              "unrelaxed_gamma": {
                "type": "number",
                "units": "erg/cm^2"
              },
              "relaxed_gamma": {
                "type": "number",
                "units": "erg/cm^2"
              },
              "delta12_before": {
                "type": "number",
                "units": "Å"
              },
              "delta12_after": {
                "type": "number",
                "units": "Å"
              },
              "delta23_before": {
                "type": "number",
                "units": "Å"
              },
              "delta23_after": {
                "type": "number",
                "units": "Å"
              },
              "delta34_before": {
                "type": "number",
                "units": "Å"
              },
              "delta34_after": {
                "type": "number",
                "units": "Å"
              },
              "percent_change_delta12": {
                "type": "number",
                "units": "%"
              },
              "percent_change_delta23": {
                "type": "number",
                "units": "%"
              },
              "percent_change_delta34": {
                "type": "number",
                "units": "%"
              }
            }
          }
        }
      },
      "description": "Consolidated results of surface energies and interlayer spacings for both Tersoff and Brenner potentials."
    }
  ],
  "notes": "The checker compares each numerical value to the paper's reported values (Tables 1 and 2) with absolute tolerances appropriate for the computational method. The agent must implement the Tersoff and Brenner potentials explicitly using the parameters given in the instruction."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact you produce. For the main results file (results.json), the verifier compares your computed surface energies, interlayer spacings, and percentage changes against a hidden reference derived from the original study. Each numerical entry is checked for consistency with the reference; correct values contribute to the score according to a predefined weighting scheme that reflects the relative importance of the surface energy and relaxation data. The final reward is a weighted sum over all scored components. Simply reporting numbers without genuinely running the MD simulations and analysis will not yield the correct values and will not pass the verifier. There is no need to reproduce the paper's exact absolute numbers to a specific tolerance—your job is to faithfully implement the described protocol, and the hidden verifier will judge the result.
