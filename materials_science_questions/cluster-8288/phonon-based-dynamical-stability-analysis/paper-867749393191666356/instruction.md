# Phonon-based dynamical stability analysis of Ti₂NiCu and dislocation-kinetic model fitting

## Problem background
Shape memory alloys such as Ti₂NiCu undergo a thermoelastic martensitic transformation from a cubic austenite (B2) to an orthorhombic martensite (B19). At the nanoscale, the transformation temperature can depend strongly on sample dimensions, and wedge-shaped plates provide a geometry where the thickness varies smoothly, allowing a systematic study of this size effect. Understanding the fundamental physics that determines whether the martensitic transformation remains possible at very small scales is crucial for designing nano‑mechanical devices based on shape memory effects. The key open question is how the transformation temperature changes with plate thickness and whether a critical thickness exists below which the transformation is fully blocked.

## Approach
This reproduction combines first‑principles density‑functional theory (DFT) calculations with a dislocation‑kinetic model. First, bulk B2 and B19 phases are relaxed and their total energy difference is computed to estimate the transformation enthalpy. Then, surface energies are obtained from slab calculations for the two terminations of B2(001) and four terminations of B19(001). Separately, phonon frequencies of the B2 phase are calculated using density‑functional perturbation theory (DFPT) to detect dynamical instabilities that drive the transformation. Finally, the dislocation‑kinetic model, which describes the movement of transformation dislocations confined by the plate boundaries, is fitted to experimental temperature‑thickness data to extract the model parameters and to infer the critical thickness where the transformation ceases. The DFT workflow uses an open‑source plane‑wave code (Quantum Espresso) with standard pseudopotentials and the virtual crystal approximation for the alloy; the fitting step uses nonlinear least‑squares optimization.

## Reproduction target
Produce the following artifacts by executing the workflow steps:

1. Compute the total energy difference between relaxed B2 and B19 bulk phases (in eV per formula unit) and write it to `enthalpy_difference.json`.
2. Compute the surface energies (in J/m²) for all six (001) terminations (B2_NiCu, B2_Ti, B19_NiCu1, B19_NiCu2, B19_Ti1, B19_Ti2) and write them to `surface_energies.json`.
3. Compute phonon frequencies (in cm⁻¹) at the high‑symmetry points Γ, M, R, X for the B2 phase, reporting soft modes as negative numbers, and write them to `phonon_frequencies.json`.
4. Fit the dislocation‑kinetic model T(h) formula (using the provided experimental CSV data) to obtain the parameters *T*_c, *k*_a, *k*₀, the mean free path λ, the nucleus volume ω, the transformation heat *q*, and the minimum blocking thickness *h*_min, and write them to `fitted_parameters.json`.

Each output must follow the declared JSON schema. The target is to reproduce the physical trends and quantitative predictions that underpin the paper’s main claim, not to match any particular table or figure.

## Assets

- Quantum Espresso (or equivalent DFT code): https://www.quantum-espresso.org/
- Pseudopotentials for Ti, Ni, Cu (PBE): https://www.quantum-espresso.org/pseudopotentials
- Experimental T(h) data for Ti₂NiCu wedge
- Crystal structure information for Ti₂NiCu B2 and B19
- Python scientific stack (SciPy, NumPy): scipy

## Workflow steps

### Step 1: DFT geometry optimization for B2 and B19 bulk phases
- Role: process
- Action: Perform full geometry optimization (variable-cell relaxation) of B2 (cubic, Pm‑3m) and B19 (orthorhombic, Pmmb) Ti₂NiCu using DFT (Quantum Espresso or equivalent). Obtain optimized lattice constants and ground-state structures required for subsequent energy and phonon calculations.
- Evidence: `/app/outputs/bulk_relax.log`

### Step 2: B2–B19 total energy difference
- Role: scored (load-bearing)
- Action: Compute the total energy of the relaxed B2 and B19 bulk structures. Report the difference E(B2) – E(B19) in eV per formula unit (four atoms).
- Output file: `/app/outputs/enthalpy_difference.json`
- Format: json
- Contract: {"delta_E_B2_to_B19_ev_per_fu": number}
- Scoring: scored by hidden verifier

### Step 3: Surface energy DFT calculations
- Role: process
- Action: Build slab models for B2 (001) with NiCu and Ti terminations, and for B19 (001) with NiCu-1, NiCu-2, Ti-1, Ti-2 terminations. Use a vacuum gap of at least 10 Å. Perform relaxations allowing the top few layers to move. Compute surface energies using the standard formula referencing the bulk total energies from step_01.
- Evidence: `/app/outputs/surface.log`

### Step 4: Surface energies report
- Role: scored (load-bearing)
- Action: Collect the computed surface energies into a structured JSON file for all six terminations.
- Output file: `/app/outputs/surface_energies.json`
- Format: json
- Contract: {"B2_NiCu": number, "B2_Ti": number, "B19_NiCu1": number, "B19_NiCu2": number, "B19_Ti1": number, "B19_Ti2": number}
- Scoring: scored by hidden verifier

### Step 5: DFPT phonon dispersion of B2
- Role: process
- Action: Using density-functional perturbation theory (DFPT), compute the phonon frequencies of the relaxed B2 structure along a high-symmetry path including Gamma, M, R, X points. Use the virtual crystal approximation (VCA) to model the alloy.
- Evidence: `/app/outputs/phonon.log`

### Step 6: Phonon frequencies at high-symmetry points
- Role: scored (load-bearing)
- Action: Extract phonon frequencies (in cm⁻¹) at the Gamma, M, R, and X points from the DFPT calculation. Report soft (imaginary) modes as negative values.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: {"Gamma": [number,...], "M": [number,...], "R": [number,...], "X": [number,...]}
- Scoring: scored by hidden verifier

### Step 7: Fit dislocation-kinetic model to T(h) data
- Role: scored
- Action: Using the provided experimental T(h) data (CSV file), fit the dislocation‑kinetic model formula T(h) = T_c / [1 − B ln( 2 k₀ / ((1 − kₐ/3) + λ/h) − 1 ) ] with B = ω q / (k_B T_c) and k_B = 1.38×10⁻²³ J/K to determine the best‑fit parameters T_c, kₐ, k₀, ω, q, and the mean free path λ. From the fitted model, compute the minimum thickness h_min at which T(h) = 0 (or the smallest value defined by the model). Report all parameters and h_min in SI/nanometer units.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {"Tc_K": number, "ka": number, "k0": number, "lambda_nm": number, "omega_nm3": number, "q_J_per_kg": number, "h_min_nm": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/enthalpy_difference.json`
- `/app/outputs/surface_energies.json`
- `/app/outputs/phonon_frequencies.json`
- `/app/outputs/fitted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### enthalpy_difference.json
- path: `/app/outputs/enthalpy_difference.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total energy difference per formula unit (eV) between austenite B2 and martensite B19. Expected to be positive if B19 is more stable.
- schema:
  - `type`: object
  - `required`: `delta_E_B2_to_B19_ev_per_fu`
  - `properties`:
    - `delta_E_B2_to_B19_ev_per_fu`:
      - `type`: number

### surface_energies.json
- path: `/app/outputs/surface_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Surface energies (J/m²) for the six (001) terminations of Ti₂NiCu.
- schema:
  - `type`: object
  - `required`: `B2_NiCu`, `B2_Ti`, `B19_NiCu1`, `B19_NiCu2`, `B19_Ti1`, `B19_Ti2`
  - `properties`:
    - `B2_NiCu`:
      - `type`: number
    - `B2_Ti`:
      - `type`: number
    - `B19_NiCu1`:
      - `type`: number
    - `B19_NiCu2`:
      - `type`: number
    - `B19_Ti1`:
      - `type`: number
    - `B19_Ti2`:
      - `type`: number

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phonon frequencies (cm⁻¹) at high-symmetry k-points for B2 Ti₂NiCu. Imaginary modes appear as negative numbers.
- schema:
  - `type`: object
  - `required`: `Gamma`, `M`, `R`, `X`
  - `properties`:
    - `Gamma`:
      - `type`: array
      - `items`:
        - `type`: number
    - `M`:
      - `type`: array
      - `items`:
        - `type`: number
    - `R`:
      - `type`: array
      - `items`:
        - `type`: number
    - `X`:
      - `type`: array
      - `items`:
        - `type`: number

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted parameters of the dislocation-kinetic model (Eq. 9) and the predicted critical blocking thickness h_min (nm). λ is the dislocation mean free path.
- schema:
  - `type`: object
  - `required`: `Tc_K`, `ka`, `k0`, `lambda_nm`, `omega_nm3`, `q_J_per_kg`, `h_min_nm`
  - `properties`:
    - `Tc_K`:
      - `type`: number
    - `ka`:
      - `type`: number
    - `k0`:
      - `type`: number
    - `lambda_nm`:
      - `type`: number
    - `omega_nm3`:
      - `type`: number
    - `q_J_per_kg`:
      - `type`: number
    - `h_min_nm`:
      - `type`: number

Notes: All outputs are compared to the paper's reported values with realistic tolerances that account for methodological differences in DFT codes/pseudopotentials and numerical fitting. The agent must execute the ordered steps to compute these quantities.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "enthalpy_difference.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_E_B2_to_B19_ev_per_fu"
        ],
        "properties": {
          "delta_E_B2_to_B19_ev_per_fu": {
            "type": "number"
          }
        }
      },
      "description": "Total energy difference per formula unit (eV) between austenite B2 and martensite B19. Expected to be positive if B19 is more stable."
    },
    {
      "file": "surface_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "B2_NiCu",
          "B2_Ti",
          "B19_NiCu1",
          "B19_NiCu2",
          "B19_Ti1",
          "B19_Ti2"
        ],
        "properties": {
          "B2_NiCu": {
            "type": "number"
          },
          "B2_Ti": {
            "type": "number"
          },
          "B19_NiCu1": {
            "type": "number"
          },
          "B19_NiCu2": {
            "type": "number"
          },
          "B19_Ti1": {
            "type": "number"
          },
          "B19_Ti2": {
            "type": "number"
          }
        }
      },
      "description": "Surface energies (J/m²) for the six (001) terminations of Ti₂NiCu."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Gamma",
          "M",
          "R",
          "X"
        ],
        "properties": {
          "Gamma": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "M": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "R": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "X": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "Phonon frequencies (cm⁻¹) at high-symmetry k-points for B2 Ti₂NiCu. Imaginary modes appear as negative numbers."
    },
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Tc_K",
          "ka",
          "k0",
          "lambda_nm",
          "omega_nm3",
          "q_J_per_kg",
          "h_min_nm"
        ],
        "properties": {
          "Tc_K": {
            "type": "number"
          },
          "ka": {
            "type": "number"
          },
          "k0": {
            "type": "number"
          },
          "lambda_nm": {
            "type": "number"
          },
          "omega_nm3": {
            "type": "number"
          },
          "q_J_per_kg": {
            "type": "number"
          },
          "h_min_nm": {
            "type": "number"
          }
        }
      },
      "description": "Fitted parameters of the dislocation-kinetic model (Eq. 9) and the predicted critical blocking thickness h_min (nm). λ is the dislocation mean free path."
    }
  ],
  "notes": "All outputs are compared to the paper's reported values with realistic tolerances that account for methodological differences in DFT codes/pseudopotentials and numerical fitting. The agent must execute the ordered steps to compute these quantities."
}
```

## How you are scored
A hidden verifier independently scores each of the four output artifacts. The verifier compares your submitted values to reference values (derived from the original study) with realistic tolerances that account for legitimate tool‑ and implementation‑dependent differences. For each artifact, the score reflects how close your result is to the reference; meeting or exceeding the reference for directional metrics earns full credit, and only larger deviations reduce the score. The final reward is a weighted sum of the per‑artifact scores. Simply reporting the paper’s published numbers without executing the workflow will not satisfy the scoring criteria — the verifier checks that the submitted values are consistent with the output of a correct execution of the required computations.
