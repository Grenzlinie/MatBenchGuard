# Thermodynamic Phase Field Computation for Chemical Vapor Deposition System

## Problem background
In the low-pressure chemical vapor deposition (LPCVD) of siliconboron carbonitride (Si-B-C-N) ceramics from precursors CH3SiCl3 (MTS), BCl3, NH3, H2, and Ar, understanding which solid phases form at equilibrium is crucial for process design. The paper investigates the thermodynamic equilibrium of this multicomponent system; it computes the condensed phases that coexist and their amounts as functions of temperature, total pressure, H2 dilution, and precursor ratios δ and γ. This task re‑implements that equilibrium calculation using an open‑source solver and public thermochemical data to predict the equilibrium phase fields and yield trends.

## Approach
The approach uses Gibbs free energy minimization for a multi‑species gas system. The initial composition is specified as fixed amounts of MTS, BCl3, NH3, H2, and Ar, with n_NH3 + n_BCl3 = 10 mol. The free energy of the system is minimized at each (T, δ) point using Cantera, an open‑source chemical thermodynamics library, with thermochemical data taken from the publicly available Burcat (NASA‑7) database, supplemented as needed for solids. The equilibrium composition yields the molar amounts of the condensed phases SiC, Si3N4, BN, B4C, and graphite. The computation is performed over a grid of temperatures (700–1200 °C) and δ values (0–1) for a baseline condition (γ = 1, P = 0.01 atm, H2 dilution 10:1). Additional runs with a different γ (e.g., 0.6) provide a parameter variation for trend analysis. The equilibrium results are post‑processed to construct phase diagrams (identifying which phases coexist at each point) and yield maps (molar amounts of each phase).

## Reproduction target
The goal is to produce the following artifacts from the equilibrium calculations:
- A phase‑diagram CSV (`phase_diagram.csv`) showing the dominant condensed phases and their molar amounts at each (T, δ) point for the baseline condition.
- Two yield‑map CSVs (`yield_map_BN_Si3N4.csv` and `yield_map_SiC_C_B4C.csv`) giving the molar yields of BN and Si3N4, and of SiC, C, and B4C, respectively, for the same baseline.
- A trend summary (`trend_summary.txt`) describing how the phase field topology changes when γ is varied (e.g., from 0.6 to 1) and stating whether the observed change is consistent with the expected thermodynamic behavior described in the analysis.

## Assets

- Cantera (open-source chemical kinetics and thermodynamics library): https://cantera.org
- Thermochemical database for gas and condensed species: http://garfield.chem.elte.hu/Burcat/burcat.html

## Workflow steps

### Step 1: Define chemical system and process parameter grid
- Role: process
- Action: Define the initial gas-phase species (CH3SiCl3, BCl3, NH3, H2, Ar) and their initial molar amounts: n_NH3 + n_BCl3 = 10 mol. Establish the parameter grid for the baseline condition: temperature range 700–1200 °C, delta (δ = n_NH3/(n_NH3+n_BCl3)) from 0 to 1, with fixed γ = 1, total pressure P = 0.01 atm, H2 dilution ratio = 10:1 (moles H2 per mole of main precursors). Also define a parameter variation condition (e.g., γ = 0.6, same P and H2 ratio) for trend verification.
- Evidence: `/app/outputs/none`

### Step 2: Compute equilibrium compositions with Gibbs free energy minimization
- Role: process
- Action: Using Cantera's equilibrium solver with thermochemical data covering all relevant gas and condensed species (SiC, Si3N4, BN, B4C, C), compute the equilibrium composition by Gibbs free energy minimization for every (T, δ) point in the baseline and variation grids. Save the molar amounts of all condensed phases and the dominant gas species for downstream processing.
- Evidence: `/app/outputs/equilibrium_data.csv`

### Step 3: Generate phase diagram CSV from equilibrium data
- Role: scored (load-bearing)
- Action: From the raw equilibrium data of the baseline condition, extract for each (T, δ) point the dominant condensed phases (phases with non-negligible amounts) and produce a phase diagram CSV listing the co-existing phases and their molar amounts.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: columns: T (float, °C), delta (float), gamma (float), P (float, atm), H2_ratio (float), dominant_phases (string), SiC_mol (float), Si3N4_mol (float), BN_mol (float), B4C_mol (float), C_mol (float)
- Scoring: scored by hidden verifier

### Step 4: Generate yield map for BN and Si3N4
- Role: scored
- Action: From the raw equilibrium data for the baseline condition, extract BN and Si3N4 amounts and produce a yield map CSV.
- Output file: `/app/outputs/yield_map_BN_Si3N4.csv`
- Format: csv
- Contract: columns: T (float, °C), delta (float), BN_mol (float), Si3N4_mol (float)
- Scoring: scored by hidden verifier

### Step 5: Generate yield map for SiC, C, and B4C
- Role: scored
- Action: From the raw equilibrium data for the baseline condition, extract SiC, C, and B4C amounts and produce a yield map CSV.
- Output file: `/app/outputs/yield_map_SiC_C_B4C.csv`
- Format: csv
- Contract: columns: T (float, °C), delta (float), SiC_mol (float), C_mol (float), B4C_mol (float)
- Scoring: scored by hidden verifier

### Step 6: Write trend summary for a parameter variation
- Role: scored
- Action: Using the equilibrium results from the variation condition (e.g., γ=0.6) and the baseline, compute the number of distinct phase fields at different δ values and describe whether the trend (e.g., reduction in the number of phase fields as γ increases from 0.6 to 1) agrees with thermodynamic expectations. Write a plain-text summary stating the observed trend and its consistency.
- Output file: `/app/outputs/trend_summary.txt`
- Format: txt
- Contract: plain text
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/yield_map_BN_Si3N4.csv`
- `/app/outputs/yield_map_SiC_C_B4C.csv`
- `/app/outputs/trend_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase diagram for the baseline condition (γ=1, P=0.01 atm, H2 ratio=10:1) across the temperature and delta grid. Each row gives the co-existing condensed phases and their amounts.
- schema:
  - `type`: table
  - `required_columns`: `T`, `delta`, `gamma`, `P`, `H2_ratio`, `dominant_phases`, `SiC_mol`, `Si3N4_mol`, `BN_mol`, `B4C_mol`, `C_mol`
  - `units`:
    - `T`: °C
    - `delta`: ratio
    - `gamma`: ratio
    - `P`: atm
    - `H2_ratio`: ratio
    - `SiC_mol`: mol
    - `Si3N4_mol`: mol
    - `BN_mol`: mol
    - `B4C_mol`: mol
    - `C_mol`: mol

### yield_map_BN_Si3N4.csv
- path: `/app/outputs/yield_map_BN_Si3N4.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Yield map for BN and Si3N4 for the baseline condition. Shows how the amounts of BN and Si3N4 vary with temperature and delta.
- schema:
  - `type`: table
  - `required_columns`: `T`, `delta`, `BN_mol`, `Si3N4_mol`
  - `units`:
    - `T`: °C
    - `delta`: ratio
    - `BN_mol`: mol
    - `Si3N4_mol`: mol

### yield_map_SiC_C_B4C.csv
- path: `/app/outputs/yield_map_SiC_C_B4C.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Yield map for SiC, C, and B4C for the baseline condition. Shows how the amounts of these carbon and carbide phases vary with temperature and delta.
- schema:
  - `type`: table
  - `required_columns`: `T`, `delta`, `SiC_mol`, `C_mol`, `B4C_mol`
  - `units`:
    - `T`: °C
    - `delta`: ratio
    - `SiC_mol`: mol
    - `C_mol`: mol
    - `B4C_mol`: mol

### trend_summary.txt
- path: `/app/outputs/trend_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: A plain text summary describing the observed trend when a process parameter (e.g., γ or H2 dilution) is varied, and confirming whether that trend matches the expected thermodynamic behavior.
- schema:
  - `type`: text

Notes: The checker will load the CSV phase diagram and yield maps, identify phase regions by dominant phases, and compare the structural pattern (region presence/absence, relative yields) against a reference derived from the paper's reported thermodynamic diagrams, allowing reasonable tolerances in temperature (±50 °C) and delta (±0.1). The trend summary is assessed on whether it correctly states at least one major trend (e.g., fewer phase fields at higher γ) consistent with the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "delta",
          "gamma",
          "P",
          "H2_ratio",
          "dominant_phases",
          "SiC_mol",
          "Si3N4_mol",
          "BN_mol",
          "B4C_mol",
          "C_mol"
        ],
        "units": {
          "T": "°C",
          "delta": "ratio",
          "gamma": "ratio",
          "P": "atm",
          "H2_ratio": "ratio",
          "SiC_mol": "mol",
          "Si3N4_mol": "mol",
          "BN_mol": "mol",
          "B4C_mol": "mol",
          "C_mol": "mol"
        }
      },
      "description": "Phase diagram for the baseline condition (γ=1, P=0.01 atm, H2 ratio=10:1) across the temperature and delta grid. Each row gives the co-existing condensed phases and their amounts."
    },
    {
      "file": "yield_map_BN_Si3N4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "delta",
          "BN_mol",
          "Si3N4_mol"
        ],
        "units": {
          "T": "°C",
          "delta": "ratio",
          "BN_mol": "mol",
          "Si3N4_mol": "mol"
        }
      },
      "description": "Yield map for BN and Si3N4 for the baseline condition. Shows how the amounts of BN and Si3N4 vary with temperature and delta."
    },
    {
      "file": "yield_map_SiC_C_B4C.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "delta",
          "SiC_mol",
          "C_mol",
          "B4C_mol"
        ],
        "units": {
          "T": "°C",
          "delta": "ratio",
          "SiC_mol": "mol",
          "C_mol": "mol",
          "B4C_mol": "mol"
        }
      },
      "description": "Yield map for SiC, C, and B4C for the baseline condition. Shows how the amounts of these carbon and carbide phases vary with temperature and delta."
    },
    {
      "file": "trend_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "A plain text summary describing the observed trend when a process parameter (e.g., γ or H2 dilution) is varied, and confirming whether that trend matches the expected thermodynamic behavior."
    }
  ],
  "notes": "The checker will load the CSV phase diagram and yield maps, identify phase regions by dominant phases, and compare the structural pattern (region presence/absence, relative yields) against a reference derived from the paper's reported thermodynamic diagrams, allowing reasonable tolerances in temperature (±50 °C) and delta (±0.1). The trend summary is assessed on whether it correctly states at least one major trend (e.g., fewer phase fields at higher γ) consistent with the paper."
}
```

## How you are scored
Each output file will be evaluated by a hidden verifier. For the phase diagram, the verifier extracts the phase regions from your CSV and compares their topology (which phases coexist in which (T, δ) regions) to a reference derived from the published analysis; it allows reasonable temperature and δ tolerances. For the yield maps, the verifier checks that the trends (e.g., the peak of BN production around δ = 0.5, the increase of Si3N4 with δ) match the expected patterns. The trend summary is assessed on whether it correctly describes at least one major trend (such as the change in number of phase fields with γ) and whether that trend agrees with the analysis. The scores from all stages are weighted and combined into a final reward in [0, 1]. Simply printing a pre‑recorded value is not sufficient; the artifacts must be the result of a genuine thermodynamic computation.
