# DFT prediction of Seebeck coefficients for 3d-metal-alloyed RuO2

## Problem background
Ruthenium dioxide (RuO2) is a promising thermoelectric oxide because its electrical conductivity is exceptionally high for an oxide, but its Seebeck coefficient is modest. Early quantum-mechanical calculations suggest that partially replacing Ru with 3d transition metals could substantially increase the Seebeck coefficient through a quantum-confinement mechanism, but the systematic picture—which elements among Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, and Zn produce the largest enhancement—remains an open computation-driven question. This task reproduces the computational screening that predicts the Seebeck coefficient at 300 K for RuO2 alloyed at low concentration with each of these 3d metals, enabling a comparison of their relative effectiveness.

## Approach
The core idea is to use density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional to compute the electronic density of states (DOS) of alloyed RuO2, and then estimate the Seebeck coefficient from the DOS shape near the Fermi level via the Mott equation. Each alloying element is introduced by substituting one Ru atom in a 2×2×2 supercell of the rutile RuO2 lattice, resulting in 2.1 at.% alloying. After full structural relaxation, the total and atom-projected DOS are calculated. The Seebeck coefficient is proportional to the energy derivative of the DOS at the Fermi level; by applying the Mott formula at 300 K, a numerical prediction is obtained for each element. The workflow compares the predicted Seebeck coefficients across the full 3d series to gauge which dopants yield the largest increase relative to the host oxide. No experimental synthesis or measurement is required; this is a purely computational task.

## Reproduction target
For all ten 3d transition metals (Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn), compute the Seebeck coefficient at 300 K for RuO2 alloyed at 2.1 at.% and record each value in a CSV file with columns `element` and `Seebeck_coefficient_muV_per_K`. The complete set of predictions, spanning the entire 3d series, constitutes the primary reproducible result. The submission will be evaluated by a hidden automatic verifier that checks these computed coefficients against a reference set of expected values and physical trends derived from the original study; you are not required to know those reference values, only to produce a physically sound, consistent DFT+Mott estimate for each element.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- SSSP PBE pseudopotential library (efficiency-tested PAW pseudopotentials for Ru, O, and 3d elements): https://www.materialscloud.org/discover/sssp/table/efficiency
- RuO2 rutile crystal structure reference (lattice parameters for P4_2/mnm): https://materialsproject.org/materials/mp-1128

## Workflow steps

### Step 1: DFT structural relaxation of alloyed supercells
- Role: process
- Action: For each 3d transition metal (Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn), build a 2x2x2 rutile RuO2 supercell (48 atoms), substitute one Ru atom with the alloying element, and perform full structural relaxation using an open-source DFT code with GGA-PBE functional and appropriate pseudopotentials.
- Evidence: `/app/outputs/relaxation_summary.txt`

### Step 2: DFT density of states calculation
- Role: process
- Action: For each relaxed alloy supercell, compute total and atom-projected density of states (DOS) using the same functional and pseudopotentials, with a k-point mesh adequate to resolve the Fermi slope.
- Evidence: `/app/outputs/dos_data.tar.gz`

### Step 3: Estimate Seebeck coefficients and compile predictions
- Role: scored (load-bearing)
- Action: From the total DOS of each alloy, extract the value and slope at the Fermi level, estimate the Seebeck coefficient at 300 K via the Mott equation, and write a CSV file with columns 'element' and 'Seebeck_coefficient_muV_per_K'.
- Output file: `/app/outputs/dd_seebeck_predictions.csv`
- Format: csv
- Contract: element: string, Seebeck_coefficient_muV_per_K: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dd_seebeck_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dd_seebeck_predictions.csv
- path: `/app/outputs/dd_seebeck_predictions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Predicted Seebeck coefficients at 300 K for RuO2 alloyed with 2.1 at.% of each 3d transition metal (Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn).
- schema:
  - `type`: table
  - `required_columns`: `element`, `Seebeck_coefficient_muV_per_K`
  - `units`:
    - `Seebeck_coefficient_muV_per_K`: µV/K

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dd_seebeck_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "Seebeck_coefficient_muV_per_K"
        ],
        "units": {
          "Seebeck_coefficient_muV_per_K": "µV/K"
        }
      },
      "description": "Predicted Seebeck coefficients at 300 K for RuO2 alloyed with 2.1 at.% of each 3d transition metal (Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your output CSV and compares the predicted Seebeck coefficients to a set of gold expectations that capture both the absolute magnitudes and the relative trends among the 3d metal series. The verifier uses deterministic rules, checking for specific ordering relations and threshold groupings derived from the underlying computational study. Partial credit is awarded if the relative trends among elements are correct even if the absolute values deviate due to implementation differences. Each scored step contributes to a final reward in the range [0, 1]; only the final CSV is directly scored, but the earlier process steps are required to produce it. The verifier does not disclose the gold values or tolerances; your job is to run the full DFT pipeline and submit the resulting Seebeck coefficients.
