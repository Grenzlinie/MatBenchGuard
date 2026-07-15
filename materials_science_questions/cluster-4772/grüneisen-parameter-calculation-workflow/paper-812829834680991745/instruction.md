# Calculation of lattice thermal conductivity of transition-metal-substituted TiNiSn via DFT and quasi-harmonic Debye model

## Problem background
TiNiSn half-Heusler alloy is a promising n-type thermoelectric material due to its high power factor, but its high lattice thermal conductivity limits the overall figure of merit. Substituting transition metals (TM) on the Ti-site is predicted to reduce lattice thermal conductivity (κ_lat) through changes in Debye temperature and Grüneisen parameter. This study computationally investigates the effect of TM substitution on the structural and thermal properties of TiNiSn using density functional theory (DFT) combined with a quasi-harmonic Debye model, aiming to identify compositions that can significantly reduce κ_lat and enhance thermoelectric performance.

## Approach
The workflow first performs DFT total-energy calculations using the PBE-GGA exchange-correlation functional to obtain energy–volume curves for the parent TiNiSn and three substituted compositions. These curves are fitted to an equation of state (e.g., Birch-Murnaghan) to extract equilibrium lattice constant, bulk modulus, and equilibrium volume. Using these results as input, a quasi-harmonic Debye model computes temperature-dependent Debye temperature, Grüneisen parameter, volume, and thermal expansion coefficient. Finally, the lattice thermal conductivity is evaluated via the Slack/Berman formula with Julian’s parameterization, which relates κ_lat to Debye temperature, Grüneisen parameter, volume, and average atomic mass. The substituted systems are compared to the baseline TiNiSn to assess the reduction in lattice thermal conductivity at selected temperatures. The detailed step-by-step execution is given in the Workflow steps below.

## Reproduction target
Perform the above computational pipeline to produce: (i) for TiNiSn, Ti0.75Zr0.25NiSn, Ti0.75Hf0.25NiSn, and Ti0.50Mn0.50NiSn, the lattice thermal conductivity κ_lat at 300 K and 1000 K, and the percentage reduction in κ_lat at 300 K relative to TiNiSn; (ii) for TiNiSn, the equilibrium lattice constant a0 (0 K), bulk modulus B0 (0 K), and Debye temperature Θ (300 K). The results shall be written to the specified CSV output files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GIBBS code: https://www.sciencedirect.com/science/article/pii/S0010465504002055
- PBE-GGA pseudopotentials: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate crystal structures
- Role: process
- Action: Create substitutional crystal structures for TiNiSn, Ti0.75Zr0.25NiSn, Ti0.75Hf0.25NiSn, and Ti0.50Mn0.50NiSn using space group 216 and Wyckoff positions. Generate input structures for a range of lattice constants around equilibrium.
- Evidence: `/app/outputs/structures.cif`

### Step 2: DFT total-energy calculations
- Role: process
- Action: Perform self-consistent DFT total-energy calculations with Quantum ESPRESSO for each composition at a series of lattice constants using PBE-GGA functional, kinetic energy cut-off 40 Ry, 6x6x6 k-point mesh, and convergence threshold 1e-8. Obtain total energy vs. lattice constant curves.
- Evidence: `/app/outputs/total_energy_curves.csv`

### Step 3: Equation of state fitting
- Role: process
- Action: Fit the energy-volume data for each composition to an equation of state to extract equilibrium lattice constant a0, bulk modulus B0, and equilibrium volume V0.
- Evidence: `/app/outputs/eos_results.csv`

### Step 4: Quasi-harmonic Debye model simulation
- Role: process
- Action: Run the quasi-harmonic Debye model (GIBBS code or direct implementation) using the DFT energy-volume curves to compute temperature-dependent Debye temperature Θ, Grüneisen parameter γ, volume V, and thermal expansion α over 0–1000 K.
- Evidence: `/app/outputs/thermal_properties.csv`

### Step 5: Slack/Berman lattice thermal conductivity
- Role: process
- Action: For each composition, compute the lattice thermal conductivity κ_lat using the Slack/Berman relation with Julian's parameterization, using Θ, γ, V, average atomic mass, and number of atoms from the Debye model results at 300 K and 1000 K.
- Evidence: `/app/outputs/kappa_lat_raw.csv`

### Step 6: Compile κ_lat summary
- Role: scored (load-bearing)
- Action: Create a CSV file summarizing the computed lattice thermal conductivity at 300 K and 1000 K and the percentage reduction at 300 K for the four compositions.
- Output file: `/app/outputs/kappa_lat_summary.csv`
- Format: csv
- Contract: CSV with columns: composition (string), kappa_lat_300K (float, W/mK), kappa_lat_1000K (float, W/mK), reduction_percentage_300K (float, %). Rows for TiNiSn, Ti0.75Zr0.25NiSn, Ti0.75Hf0.25NiSn, Ti0.50Mn0.50NiSn. For TiNiSn, reduction_percentage_300K=0.
- Scoring: scored by hidden verifier

### Step 7: Compile TiNiSn baseline properties
- Role: scored
- Action: Create a CSV file reporting the equilibrium lattice constant a0 at 0 K, bulk modulus B0 at 0 K, and Debye temperature Θ at 300 K for TiNiSn.
- Output file: `/app/outputs/ti_nisn_properties.csv`
- Format: csv
- Contract: CSV with columns: property (string), value (float), unit (string). Rows: a0_0K (Å), B0_0K (GPa), Debye_temperature_300K (K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kappa_lat_summary.csv`
- `/app/outputs/ti_nisn_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kappa_lat_summary.csv
- path: `/app/outputs/kappa_lat_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal conductivity summary for four compositions.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `kappa_lat_300K`, `kappa_lat_1000K`, `reduction_percentage_300K`
  - `units`:
    - `kappa_lat_300K`: W/mK
    - `kappa_lat_1000K`: W/mK
    - `reduction_percentage_300K`: %

### ti_nisn_properties.csv
- path: `/app/outputs/ti_nisn_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Baseline properties of TiNiSn: lattice constant a0 (0 K), bulk modulus B0 (0 K), Debye temperature (300 K).
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`, `unit`
  - `units`:
    - `value`: float (unit as indicated in unit column)

Notes: All values are numeric. The checker will compare the reported values to the paper's results within pre-defined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kappa_lat_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "kappa_lat_300K",
          "kappa_lat_1000K",
          "reduction_percentage_300K"
        ],
        "units": {
          "kappa_lat_300K": "W/mK",
          "kappa_lat_1000K": "W/mK",
          "reduction_percentage_300K": "%"
        }
      },
      "description": "Lattice thermal conductivity summary for four compositions."
    },
    {
      "file": "ti_nisn_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value",
          "unit"
        ],
        "units": {
          "value": "float (unit as indicated in unit column)"
        }
      },
      "description": "Baseline properties of TiNiSn: lattice constant a0 (0 K), bulk modulus B0 (0 K), Debye temperature (300 K)."
    }
  ],
  "notes": "All values are numeric. The checker will compare the reported values to the paper's results within pre-defined tolerances."
}
```

## How you are scored
The hidden verifier will read your submitted CSV files and independently compare each reported quantity against pre‑defined reference values. For `kappa_lat_summary.csv`, the verifier checks the κ_lat values at 300 K and 1000 K for the four compositions and the percentage reductions at 300 K. For `ti_nisn_properties.csv`, it checks a0, B0, and Θ. Each comparison uses an appropriate hidden tolerance. The final reward is a weighted combination of the per‑artifact scores; simply copying numbers from an external source without correctly executing the workflow will not pass. The verifier may also verify that the percentage reductions are consistent with the reported κ_lat values.
