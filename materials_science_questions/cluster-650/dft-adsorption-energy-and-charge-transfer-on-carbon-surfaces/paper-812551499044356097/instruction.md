# DFT Adsorption Energies and Distances on Mg-decorated C3B Monolayer for Gas Sensing

## Problem background
Two-dimensional materials such as the C3B monolayer are promising for gas sensing because of their large surface-to-volume ratio and tunable electronic properties. Pristine C3B often interacts only weakly with gas molecules, limiting sensitivity. Decorating the surface with metal atoms (e.g., Mg) has been proposed to enhance adsorption strength and sensitivity towards nitrogen-based pollutants. This task investigates the adsorption behaviour of NO, N2O, NO2 and NH3 on an Mg‑adsorbed C3B monolayer by computing adsorption energies and equilibrium distances, and compares them with adsorption on pristine C3B. Obtaining these quantitative properties is essential for evaluating the material's potential as a gas sensor.

## Approach
The adsorption properties are studied with density functional theory (DFT) using the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and the Grimme D2 semi‑empirical dispersion correction (DFT‑D2) to account for van der Waals interactions. First, the geometries of a pristine C3B monolayer and of an Mg atom placed at a hollow site on the C3B surface are optimized. Separately, the geometries of the isolated gas molecules (NO, N2O, NO2, NH3) are optimized in a periodic box. For each gas molecule, total energies are computed for the adsorption complex formed on the Mg site of the Mg‑C3B system (for NO and NO2 both N‑end and O‑end binding orientations are considered) and on the pristine C3B surface. From these energies the adsorption energy E_ad is derived as E(complex) ‑ E(substrate) ‑ E(gas). For each adsorption configuration on Mg‑C3B the equilibrium distance d (shortest atom‑to‑substrate distance) is extracted from the relaxed geometry. The set of computed E_ad and d values quantifies the effect of Mg decoration on gas uptake.

## Reproduction target
Produce a CSV file step_01_results.csv containing the adsorption energy E_ad (eV) and equilibrium distance d (Å) for every combination of substrate (Mg‑C3B and pristine C3B) and gas molecule (NO, N2O, NO2, NH3). For Mg‑C3B report both N‑end (configuration `I`) and O‑end (configuration `II`) orientations for NO and NO2, and the N‑end orientation for N2O and NH3. For pristine C3B report one entry per gas (leave the configuration field empty) and either set d to 0 or leave it blank. The required columns are: `system`, `gas`, `configuration`, `E_ad`, `d`. Achieve these values by following the DFT workflow steps; a hidden verifier will later compare them against established reference values. The reference numbers are not disclosed at this stage.

## Assets

- Open-source DFT package with PBE functional and Grimme D2 dispersion correction (e.g., SIESTA or Quantum ESPRESSO): https://departments.icmab.es/leem/siesta/CodeAccess/

## Workflow steps

### Step 1: Geometry optimization of pristine C3B monolayer
- Role: process
- Action: Perform DFT geometry relaxation of a C3B monolayer in a suitable supercell using the PBE functional with Grimme D2 dispersion correction. Record the total energy and optimized atomic positions.
- Evidence: `/app/outputs/pristine_C3B_energy.json`

### Step 2: Mg atom adsorption on C3B monolayer
- Role: process
- Action: Place a Mg atom at the hollow site of the optimized C3B monolayer and perform spin-polarized DFT relaxation (PBE+DFT-D2). Record total energy and optimized geometry.
- Evidence: `/app/outputs/Mg_C3B_energy.json`

### Step 3: Geometry optimization of isolated gas molecules
- Role: process
- Action: Perform DFT optimization of each isolated gas molecule (NO, N2O, NO2, NH3) in a sufficiently large periodic box. Record their total energies.
- Evidence: `/app/outputs/gas_energies.json`

### Step 4: Calculate adsorption energies and equilibrium distances for all gas/substrate combinations
- Role: scored (load-bearing)
- Action: For each gas molecule, perform geometry optimization of the gas adsorbed on the Mg site of the Mg-C3B system (including two orientations for NO and NO2: N-end and O-end) and on the pristine C3B surface. Using the total energies from previous steps, compute adsorption energies E_ad = E(complex) - E(substrate) - E(gas) and equilibrium distances d from the relaxed geometries. Output all results to step_01_results.csv.
- Output file: `/app/outputs/step_01_results.csv`
- Format: csv
- Contract: Columns: system (str, one of 'Mg-C3B' or 'pristine_C3B'), gas (str, one of 'NO','N2O','NO2','NH3'), configuration (str, for Mg-C3B: 'I' (N-end) or 'II' (O-end) for NO and NO2, 'N-end' for others; for pristine_C3B: single entry per gas with empty configuration), E_ad (float, eV), d (float, Å; leave empty or 0 for pristine entries).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.csv
- path: `/app/outputs/step_01_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies (E_ad in eV) and equilibrium adsorption distances (d in Å) for NO, N2O, NO2, and NH3 on Mg-C3B and pristine C3B surfaces. Configurations for NO and NO2 on Mg-C3B must include both N-end (I) and O-end (II) orientations.
- schema:
  - `type`: table
  - `required_columns`: `system`, `gas`, `configuration`, `E_ad`, `d`
  - `units`:
    - `E_ad`: eV
    - `d`: Å

Notes: The hidden checker compares the reported E_ad and d values against the paper's published gold values with appropriate tolerances. Only the CSV is evaluated; no intermediate files are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "gas",
          "configuration",
          "E_ad",
          "d"
        ],
        "units": {
          "E_ad": "eV",
          "d": "Å"
        }
      },
      "description": "Adsorption energies (E_ad in eV) and equilibrium adsorption distances (d in Å) for NO, N2O, NO2, and NH3 on Mg-C3B and pristine C3B surfaces. Configurations for NO and NO2 on Mg-C3B must include both N-end (I) and O-end (II) orientations."
    }
  ],
  "notes": "The hidden checker compares the reported E_ad and d values against the paper's published gold values with appropriate tolerances. Only the CSV is evaluated; no intermediate files are scored."
}
```

## How you are scored
A hidden verifier reads your step_01_results.csv and compares each row’s E_ad and d to a set of gold reference values (derived from the original study) using a pre‑defined small tolerance. Each row where both E_ad and (if applicable) d fall within tolerance earns full credit. Partial credit is awarded proportionally to the number of correct rows. The total score is a weighted sum of the per‑row scores, normalised to a float between 0.0 and 1.0. The verifier also checks that all expected rows are present. No other output files are scored. Copying numbers from external sources or guessing will produce inaccurate results; only a genuine DFT execution of the described protocol can reliably meet the required precision.
