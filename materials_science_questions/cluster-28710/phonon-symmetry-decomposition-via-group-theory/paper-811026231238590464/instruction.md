# Phonon Symmetry Decomposition via Group Theory

## Problem background
The ternary chalcopyrite semiconductor ZnSnP₂ is a candidate for photovoltaic applications because of its direct band gap of about 1.68 eV. Understanding its vibrational and dielectric properties—in particular the zone‑center optical phonon frequencies, Born effective charge tensors, and the high‑frequency and static dielectric constants—is essential for modelling lattice heat transport and carrier scattering. This task aims to compute these quantities from first principles, providing a self‑contained reference data set that can be compared with experiment and used as input for higher‑level simulations.

## Approach
The calculation uses density‑functional perturbation theory (DFPT) within the local‑density approximation (LDA) with norm‑conserving Troullier‑Martins pseudopotentials. The workflow consists of four stages. First, the crystal structure of tetragonal ZnSnP₂ (space group I‑42d, point group D₂d) is relaxed to its equilibrium geometry. Second, a DFPT calculation on a uniform q‑point grid yields the dynamical matrices, the Born effective charge tensors for each atom, and the high‑frequency (electronic) dielectric tensor. Third, the dynamical matrices are Fourier‑interpolated to the zone centre to obtain the Γ‑point phonon modes; the acoustic sum rule is enforced; irreducible representations (A₁, A₂, B₁, B₂, E) are assigned to the optical modes using the D₂d character table; and longitudinal‑optical / transverse‑optical (LO/TO) splitting is computed for all polar modes from the Born charges and electronic dielectric tensor. Fourth, the static dielectric tensor is obtained from the LO/TO frequencies via the generalised Lyddane–Sachs–Teller relation.

## Reproduction target
Execute the four‑stage protocol and write a single JSON file, `results.json`, containing three sections: (1) zone‑center optical phonon modes, each with a label, a symmetry assignment (A₁, A₂, B₁, B₂, E), the transverse‑optical frequency (in cm⁻¹), and for IR‑active modes the longitudinal‑optical frequency (set to `null` for non‑polar modes); (2) for each symmetry‑inequivalent atom species (Zn, Sn, P), the eigenvalues and the average eigenvalue of the Born effective charge tensor; (3) the electronic (ε∞) and static (ε₀) dielectric tensor components, both perpendicular to and parallel to the tetragonal c axis. The exact JSON schema is given in the output contract below.

## Assets

- ABINIT software: https://www.abinit.org/
- Troullier-Martins LDA pseudopotentials for Zn, Sn, P: https://www.abinit.org/downloads/psp-links/psp-links/lda_tm

## Workflow steps

### Step 1: Structural optimization
- Role: process
- Action: Perform DFT structural optimization of ZnSnP2 in the chalcopyrite structure (space group I-42d) using ABINIT and the provided LDA pseudopotentials, relaxing lattice constants a, c and internal parameter u until forces are converged.
- Evidence: `/app/outputs/opt_structure.log`

### Step 2: DFPT calculation
- Role: process
- Action: Using the optimized structure, run a DFPT calculation in ABINIT on a chosen q-point grid to compute dynamical matrices, Born effective charge tensors, and the electronic (high-frequency) dielectric tensor.
- Evidence: `/app/outputs/dfpt_output.log`

### Step 3: Phonon postprocessing and symmetry assignment
- Role: process
- Action: From the DFPT outputs, Fourier-interpolate to obtain zone-center phonon frequencies and eigenvectors. Apply the acoustic sum rule. Assign irreducible representations (A1, A2, B1, B2, E) to the optical modes using the D2d point group. Compute LO/TO splitting for IR-active modes using the Born effective charges and electronic dielectric tensor. Calculate the static dielectric constants via the generalized Lyddane-Sachs-Teller relation.
- Evidence: none

### Step 4: Collect scored results
- Role: scored (load-bearing)
- Action: Write all computed headline quantities into a JSON file: zone-center phonon frequencies with symmetry labels and LO/TO values, Born effective charge eigenvalues and averages, and dielectric tensor components (electronic and static).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys: 'zone_center_phonons' (list of {mode: string, symmetry: string, frequency_TO: number, frequency_LO: number|null}), 'born_effective_charges' (list of {atom: string, eigenvalues: [number, number, number], average: number}), 'dielectric_constants' ({epsilon_inf_perp: number, epsilon_inf_par: number, epsilon_0_perp: number, epsilon_0_par: number}).
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
- description: Scored artifact containing all headline quantities: zone-center phonon frequencies with symmetry assignments and LO/TO splitting, Born effective charge eigenvalues and averages, and electronic and static dielectric tensor components.
- schema:
  - `type`: object
  - `required`: `zone_center_phonons`, `born_effective_charges`, `dielectric_constants`
  - `properties`:
    - `zone_center_phonons`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `mode`, `symmetry`, `frequency_TO`
        - `properties`:
          - `mode`:
            - `type`: string
          - `symmetry`:
            - `type`: string
          - `frequency_TO`:
            - `type`: number
          - `frequency_LO`:
            - `type`: `number`, `null`
    - `born_effective_charges`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `atom`, `eigenvalues`, `average`
        - `properties`:
          - `atom`:
            - `type`: string
          - `eigenvalues`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 3
            - `maxItems`: 3
          - `average`:
            - `type`: number
    - `dielectric_constants`:
      - `type`: object
      - `required`: `epsilon_inf_perp`, `epsilon_inf_par`, `epsilon_0_perp`, `epsilon_0_par`
      - `properties`:
        - `epsilon_inf_perp`:
          - `type`: number
        - `epsilon_inf_par`:
          - `type`: number
        - `epsilon_0_perp`:
          - `type`: number
        - `epsilon_0_par`:
          - `type`: number

Notes: Verification compares the agent's reported values in this file against the paper's published reference values for the same quantities, with tolerances appropriate for a DFPT re-run using a different code version or pseudopotential generation. The phonon frequencies, Born charges, and dielectric constants must be derived from the preceding DFT/DFPT calculations; the output file is load-bearing.

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
          "zone_center_phonons",
          "born_effective_charges",
          "dielectric_constants"
        ],
        "properties": {
          "zone_center_phonons": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "mode",
                "symmetry",
                "frequency_TO"
              ],
              "properties": {
                "mode": {
                  "type": "string"
                },
                "symmetry": {
                  "type": "string"
                },
                "frequency_TO": {
                  "type": "number"
                },
                "frequency_LO": {
                  "type": [
                    "number",
                    "null"
                  ]
                }
              }
            }
          },
          "born_effective_charges": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "atom",
                "eigenvalues",
                "average"
              ],
              "properties": {
                "atom": {
                  "type": "string"
                },
                "eigenvalues": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 3,
                  "maxItems": 3
                },
                "average": {
                  "type": "number"
                }
              }
            }
          },
          "dielectric_constants": {
            "type": "object",
            "required": [
              "epsilon_inf_perp",
              "epsilon_inf_par",
              "epsilon_0_perp",
              "epsilon_0_par"
            ],
            "properties": {
              "epsilon_inf_perp": {
                "type": "number"
              },
              "epsilon_inf_par": {
                "type": "number"
              },
              "epsilon_0_perp": {
                "type": "number"
              },
              "epsilon_0_par": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Scored artifact containing all headline quantities: zone-center phonon frequencies with symmetry assignments and LO/TO splitting, Born effective charge eigenvalues and averages, and electronic and static dielectric tensor components."
    }
  ],
  "notes": "Verification compares the agent's reported values in this file against the paper's published reference values for the same quantities, with tolerances appropriate for a DFPT re-run using a different code version or pseudopotential generation. The phonon frequencies, Born charges, and dielectric constants must be derived from the preceding DFT/DFPT calculations; the output file is load-bearing."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares each quantity to reference values obtained from an independent first‑principles calculation and, where available, experimental measurements. For every phonon frequency, Born charge eigenvalue and average, and dielectric constant, the verifier checks whether the absolute difference from the reference falls within a tolerance that accounts for the systematic spread expected between different DFT engines and pseudopotential libraries. The final reward is a weighted average of the per‑quantity accuracies, with the highest weight placed on the phonon frequencies and dielectric constants. Note that the output file must be the genuine result of running the workflow; simply reporting plausible numbers is not sufficient.
