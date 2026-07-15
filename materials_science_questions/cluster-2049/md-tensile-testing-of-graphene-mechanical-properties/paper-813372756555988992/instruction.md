# Reaction energy and curvature correlation for rippled graphene hydrogenation

## Problem background
Graphene sheets naturally exhibit ripples. First‑principles calculations show that one‑dimensional periodic ripples can be used to direct the chemical reactivity of graphene towards hydrogenation. The key quantities of interest are the reaction energy for hydrogenation of rippled graphene sheets with different amplitude‑to‑wavelength ratios (A/λ), the local atomic curvatures at the addition sites, and the band gaps of pristine and hydrogenated rippled graphene. This task requires you to compute these quantities using density functional theory (DFT).

## Approach
The reproduction follows a computational DFT workflow. Rippled graphene sheets are constructed from a sinusoidal function y = a sin(0.2x) with several amplitudes a and a fixed wavelength, spanning a range of A/λ ratios. The geometries of the pristine sheets are optimized at the PBE/DZP level. Hydrogenation is modelled by attaching two H atoms at the most reactive sites (crest and trough, on different sublattices) and optimizing the adduct. The reaction energy is obtained as E(adduct) − E(graphene) − E(H₂). Local atomic curvatures are computed by sphere‑fitting around each addition carbon. The relationship between the reaction energy and the average local curvature is then characterized by a linear regression. Band structure calculations are performed for the most highly rippled system to determine band gaps before and after hydrogenation.

## Reproduction target
Re‑implement the DFT procedure to produce:
- A CSV table containing reaction energies Er(H) and local curvatures for hydrogenation of rippled graphene sheets with four amplitude‑to‑wavelength ratios (corresponding to amplitudes a = 5, 10, 15, 20 Å).
- A CSV table with the band gaps of the pristine and hydrogenated sheet having the largest ripple (a = 20 Å).
- A JSON object with the slope, intercept, and R² of the linear fit of Er(H) vs. average local curvature.
The three artefacts will be compared against hidden reference values derived from the original study. Your submission must contain exactly the three files specified in the output contract.

## Assets

- DFT code with PBE functional and DZP basis (e.g., SIESTA, Quantum ESPRESSO, CP2K): https://departments.icmab.es/leem/siesta/
- PBE pseudopotentials and DZP basis sets for C and H: https://www.icmab.es/siesta/Pseudopotentials/

## Workflow steps

### Step 1: Generate initial ripple geometries
- Role: process
- Action: Generate atomic coordinates for flat graphene and rippled graphene sheets b–e using the sinusoidal function y = a sin(0.2x) with a = 5, 10, 15, 20 Å (wavelength fixed at 10π Å). Output coordinate files in a format suitable for DFT input.
- Evidence: `/app/outputs/ripple_geometries.xyz`

### Step 2: DFT geometry optimization of pristine rippled graphene
- Role: process
- Action: For each rippled sheet b–e, perform spin-unpolarized PBE/DZP geometry optimization with periodic boundary conditions. Fix the unit cell length along the ripple direction to the wavelength, fix the perpendicular vacuum gap to 100 Å, and relax the out-of-plane cell dimension. Output total energies and optimized atomic coordinates.
- Evidence: `/app/outputs/opt_pristine.energies`

### Step 3: DFT hydrogenation of rippled graphene
- Role: process
- Action: For each optimized rippled sheet b–e, place two H atoms at the most reactive sites (crest/trough, on different sublattices, labeled C1 and C2). Perform spin-polarized PBE/DZP geometry optimization using the same cell constraints as the pristine optimization. Also compute the total energy of an isolated H₂ molecule at the same level of theory. Output optimized geometries and total energies for all species.
- Evidence: `/app/outputs/hydrogenation.energies`

### Step 4: Compute reaction energies and local curvatures
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute reaction energies Er(H) = E(adduct) - E(graphene) - E(H2) for b–e. For the addition sites C1 and C2 in each optimized pristine rippled sheet, fit a sphere to the carbon and its three bonded neighbors, compute curvature = 1/radius. Calculate average curvature k̄ = (k_C1 + k_C2)/2. Save the data as CSV.
- Output file: `/app/outputs/reaction_energies_curvatures.csv`
- Format: csv
- Contract: species (str), A_lambda (float), curvature_C1 (float, 1/Å), curvature_C2 (float, 1/Å), avg_curvature (float, 1/Å), Er_H (float, eV)
- Scoring: scored by hidden verifier

### Step 5: Band structure calculation of pristine and hydrogenated e
- Role: scored
- Action: Using the optimized geometries of pristine e and hydrogenated e (C1–C2 adduct), perform band structure DFT calculations at the PBE/DZP level with a dense k-path. Determine the band gaps in eV. Save as CSV.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: species (str), hydrogenated (bool), band_gap_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Linear regression of reaction energy vs average curvature
- Role: scored
- Action: Using the data from reaction_energies_curvatures.csv, perform linear regression of Er_H vs avg_curvature for b–e. Compute slope, intercept, and coefficient of determination (R²). Output as JSON.
- Output file: `/app/outputs/curvature_energy_linear_fit.json`
- Format: json
- Contract: {slope: float (eV·Å), intercept: float (eV), r_squared: float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reaction_energies_curvatures.csv`
- `/app/outputs/band_gaps.csv`
- `/app/outputs/curvature_energy_linear_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_energies_curvatures.csv
- path: `/app/outputs/reaction_energies_curvatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed reaction energies and local curvatures for hydrogenation of rippled graphene species b–e. Checker compares to paper's Table 2 within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `species`, `A_lambda`, `curvature_C1`, `curvature_C2`, `avg_curvature`, `Er_H`
  - `units`:
    - `curvature_C1`: 1/Å
    - `curvature_C2`: 1/Å
    - `avg_curvature`: 1/Å
    - `Er_H`: eV

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Band gaps of pristine rippled graphene (species e) and its C1-C2 hydride, verifying absence of gap in pristine and opening upon hydrogenation.
- schema:
  - `type`: table
  - `required_columns`: `species`, `hydrogenated`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

### curvature_energy_linear_fit.json
- path: `/app/outputs/curvature_energy_linear_fit.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Linear fit of reaction energy vs average curvature, verifying approximate linear dependence (negative slope, high R²).
- schema:
  - `type`: object
  - `required`: `slope`, `intercept`, `r_squared`
  - `items`:
    - `slope`: eV·Å
    - `intercept`: eV
    - `r_squared`: dimensionless

Notes: Tolerances are hidden. The linear fit is checked for negative slope and R² > 0.9, plus a consistency check on predicted Er_H at a given curvature. All DFT calculations are run by the agent; no precomputed data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_energies_curvatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "A_lambda",
          "curvature_C1",
          "curvature_C2",
          "avg_curvature",
          "Er_H"
        ],
        "units": {
          "curvature_C1": "1/Å",
          "curvature_C2": "1/Å",
          "avg_curvature": "1/Å",
          "Er_H": "eV"
        }
      },
      "description": "Computed reaction energies and local curvatures for hydrogenation of rippled graphene species b–e. Checker compares to paper's Table 2 within tolerance."
    },
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "hydrogenated",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Band gaps of pristine rippled graphene (species e) and its C1-C2 hydride, verifying absence of gap in pristine and opening upon hydrogenation."
    },
    {
      "file": "curvature_energy_linear_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "slope",
          "intercept",
          "r_squared"
        ],
        "items": {
          "slope": "eV·Å",
          "intercept": "eV",
          "r_squared": "dimensionless"
        }
      },
      "description": "Linear fit of reaction energy vs average curvature, verifying approximate linear dependence (negative slope, high R²)."
    }
  ],
  "notes": "Tolerances are hidden. The linear fit is checked for negative slope and R² > 0.9, plus a consistency check on predicted Er_H at a given curvature. All DFT calculations are run by the agent; no precomputed data is provided."
}
```

## How you are scored
A hidden verifier reads your output files and compares each scored artefact against reference values or structural constraints, using tolerances suitable for DFT reproduction. Each artefact contributes to a total reward in the range [0, 1]; the final score is the weighted sum. Expected trends (negative slope, high R², correct band‑gap magnitudes) are rewarded. The verifier does not re‑run any DFT calculation; it only checks the numbers you report. Missing or incorrectly formatted files will reduce the score.
