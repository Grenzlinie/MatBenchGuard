# DFPT lattice dynamics and dielectric properties of anatase TiO₂

## Problem background
Titanium dioxide (TiO₂) in the anatase phase is a wide-bandgap semiconductor used in photocatalysis, solar cells, and batteries. Understanding its lattice vibrations and dielectric response is important for interpreting spectroscopic measurements and for predicting material performance. First-principles density-functional perturbation theory (DFPT) can directly compute these properties – including Born effective charge tensors, zone‑center phonon frequencies, and dielectric permittivity tensors – from the crystal structure and exchange‑correlation functional. This task reproduces such a DFPT study for anatase TiO₂.

## Approach
The calculation uses the public ABINIT code with the local density approximation (LDA) and norm‑conserving Teter‑type pseudopotentials for titanium and oxygen. Starting from the known anatase crystal structure (space group I4₁/amd, two formula units in the primitive cell), a ground‑state density is obtained, followed by DFPT linear‑response computations that yield dynamical matrices, Born effective charge tensors, and the electronic dielectric permittivity tensor. From these, one can diagonalize the Born tensors to obtain principal values, compute Gamma‑point phonon frequencies including LO‑TO splitting with irreducible‑representation labels, and evaluate the static dielectric tensor by summing mode oscillator strengths. A scissor correction of 1.15 eV is applied to the electronic tensor to account for the LDA band‑gap underestimation.

## Reproduction target
Produce three machine‑readable JSON files:
- The principal (diagonal) components of the Born effective charge tensors for Ti and O.
- The zone‑center optical phonon frequencies (cm⁻¹) with symmetry labels for all Raman‑active, infrared‑active (TO and LO), and silent modes.
- The xx and zz components of the electronic (uncorrected and scissor‑corrected) and static dielectric permittivity tensors.
The outputs must follow the exact schemas described in the workflow steps and output contract. The target is to compute these quantities using the specified DFPT protocol; the computed numbers are then evaluated by a hidden verifier.

## Assets

- ABINIT code: https://www.abinit.org/
- Norm-conserving Teter-type pseudopotentials for Ti and O: https://www.abinit.org/pseudos
- Anatase TiO2 crystal structure (space group I41/amd)

## Workflow steps

### Step 1: Structure setup
- Role: process
- Action: Set up the anatase TiO₂ crystal structure using lattice parameters a=3.747 Å, c=9.334 Å, space group I4₁/amd. Build the primitive unit cell with 2 formula units (6 atoms). Obtain internal coordinates from the literature or a public crystallographic database. Write the geometry input file for the subsequent DFPT calculation.
- Evidence: `/app/outputs/geometry.in`

### Step 2: DFPT linear-response calculation
- Role: process
- Action: Run a density-functional perturbation theory (DFPT) calculation using the ABINIT code. Use the LDA exchange-correlation, Teter-type norm-conserving pseudopotentials for Ti and O, a plane-wave cutoff of 100 Ry, and a Monkhorst-Pack (4,4,4) k-point grid. Compute the ground-state charge density, dynamical matrices on the (4,4,4) q-grid, Born effective charge tensors, and the electronic dielectric permittivity tensor. Save all required outputs for later analysis.
- Evidence: `/app/outputs/abinit.log`

### Step 3: Extract Born effective charges
- Role: scored (load-bearing)
- Action: Extract the Born effective charge tensors for Ti and O from the DFPT output. Diagonalize them in the conventional-cell axes (i=1,2,3 along a,b,c) to obtain the principal (diagonal) values. Write the principal values to /app/outputs/born_effective_charges.json.
- Output file: `/app/outputs/born_effective_charges.json`
- Format: json
- Contract: JSON object with keys 'Ti_principal' (array of three floats) and 'O_principal' (array of three floats).
- Scoring: scored by hidden verifier

### Step 4: Compute zone‑center phonon frequencies
- Role: scored
- Action: Using the dynamical matrices and Born effective charges from the DFPT run, compute the zone‑center (Γ) phonon frequencies including LO‑TO splitting for infrared-active modes. Assign each mode to its irreducible representation (Raman: E_g, B_1g, A_1g; IR: E_u, A_2u; silent: B_2u). Write the mode labels and frequencies (cm⁻¹) to /app/outputs/phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object where each key is the mode label (e.g., 'Eg(1)', 'Eu(1)_TO', 'Eu(1)_LO', 'A2u(1)_TO', 'A2u(1)_LO', 'Eu(2)_TO', 'Eu(2)_LO', 'B2u') and each value is a float (cm⁻¹).
- Scoring: scored by hidden verifier

### Step 5: Compute dielectric permittivity tensors
- Role: scored
- Action: From the DFPT results, compute the electronic dielectric permittivity tensor ε^∞ (uncorrected), the static dielectric tensor ε^0 by summing mode oscillator strengths, and the electronic tensor after applying a scissor correction of 1.15 eV. Write the relevant components to /app/outputs/dielectric_tensors.json.
- Output file: `/app/outputs/dielectric_tensors.json`
- Format: json
- Contract: JSON object with keys: 'electronic_xx_noscissor', 'electronic_zz_noscissor', 'electronic_xx_scissor', 'electronic_zz_scissor', 'static_xx', 'static_zz'. All values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/born_effective_charges.json`
- `/app/outputs/phonon_frequencies.json`
- `/app/outputs/dielectric_tensors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### born_effective_charges.json
- path: `/app/outputs/born_effective_charges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Principal Born effective charge tensor components for Ti and O in anatase TiO2.
- schema:
  - `type`: object
  - `required`: `Ti_principal`, `O_principal`
  - `properties`:
    - `Ti_principal`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `O_principal`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zone‑center optical phonon frequencies with symmetry assignments for anatase TiO2.
- schema:
  - `type`: object
  - `additionalProperties`:
    - `type`: number
  - `description`: Keys are mode labels (e.g., 'Eg(1)', 'Eu(1)_TO', 'Eu(1)_LO', 'A2u(1)_TO', 'A2u(1)_LO', 'Eu(2)_TO', 'Eu(2)_LO', 'B2u'); values are frequencies in cm⁻¹.

### dielectric_tensors.json
- path: `/app/outputs/dielectric_tensors.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dielectric permittivity tensor components (uncorrected, scissor-corrected, and static) for anatase TiO2.
- schema:
  - `type`: object
  - `required`: `electronic_xx_noscissor`, `electronic_zz_noscissor`, `electronic_xx_scissor`, `electronic_zz_scissor`, `static_xx`, `static_zz`
  - `properties`:
    - `electronic_xx_noscissor`:
      - `type`: number
    - `electronic_zz_noscissor`:
      - `type`: number
    - `electronic_xx_scissor`:
      - `type`: number
    - `electronic_zz_scissor`:
      - `type`: number
    - `static_xx`:
      - `type`: number
    - `static_zz`:
      - `type`: number

Notes: All values must be in the same units as the paper. The hidden checker compares these files to the paper's reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "born_effective_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Ti_principal",
          "O_principal"
        ],
        "properties": {
          "Ti_principal": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "O_principal": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          }
        }
      },
      "description": "Principal Born effective charge tensor components for Ti and O in anatase TiO2."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "additionalProperties": {
          "type": "number"
        },
        "description": "Keys are mode labels (e.g., 'Eg(1)', 'Eu(1)_TO', 'Eu(1)_LO', 'A2u(1)_TO', 'A2u(1)_LO', 'Eu(2)_TO', 'Eu(2)_LO', 'B2u'); values are frequencies in cm⁻¹."
      },
      "description": "Zone‑center optical phonon frequencies with symmetry assignments for anatase TiO2."
    },
    {
      "file": "dielectric_tensors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "electronic_xx_noscissor",
          "electronic_zz_noscissor",
          "electronic_xx_scissor",
          "electronic_zz_scissor",
          "static_xx",
          "static_zz"
        ],
        "properties": {
          "electronic_xx_noscissor": {
            "type": "number"
          },
          "electronic_zz_noscissor": {
            "type": "number"
          },
          "electronic_xx_scissor": {
            "type": "number"
          },
          "electronic_zz_scissor": {
            "type": "number"
          },
          "static_xx": {
            "type": "number"
          },
          "static_zz": {
            "type": "number"
          }
        }
      },
      "description": "Dielectric permittivity tensor components (uncorrected, scissor-corrected, and static) for anatase TiO2."
    }
  ],
  "notes": "All values must be in the same units as the paper. The hidden checker compares these files to the paper's reported values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads each of the three output JSON files and compares every reported numerical value to an independently established reference. Because different re‑implementations may yield slightly different results, each comparison uses a tolerance that absorbs legitimate numerical spread. The reward is monotonic: if your value lies within the tolerance (or is better than the reference when “better” is well‑defined), you receive full credit for that component; larger deviations reduce the credit proportionally. The three files carry roughly equal weight, and the final reward is a weighted combination of all component scores. Reporting numbers without performing the actual workflow is not sufficient; the verifier only rewards artefacts that are consistent with a genuine DFPT calculation.
