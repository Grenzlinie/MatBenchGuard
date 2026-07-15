# Net electronic charge descriptor for oxygen vacancy formation energy and migration barrier correlations

## Problem background
Perovskite oxides are attractive as oxygen sorbents for chemical looping air separation (CLAS) due to their tunable redox properties, but the vast compositional space makes rational optimization challenging. The oxygen release capacity and transport kinetics are governed by the oxygen vacancy formation energy and the vacancy migration barrier, both of which depend sensitively on cation substitutions. An effective, computationally inexpensive descriptor that correlates with these properties would greatly accelerate material screening. Previous work has suggested that the net electronic charge on oxygen anions computed from a single-point electronic structure calculation may reflect the ease of oxygen release and migration, but this hypothesis requires systematic verification across different doping types and vacancy concentrations.

## Approach
The approach is to compute oxygen vacancy formation energies and migration barriers for three representative SrFeO₃‑based perovskites—pristine (SF), A‑site Y‑doped (A.Y), and B‑site Cu‑doped (B.Cu)—using first‑principles DFT+U calculations within 2×2×2 supercells. For each system, the ferromagnetic ground state is determined first. Oxygen vacancies are introduced sequentially to reach nonstoichiometries δ up to 0.375, and at each δ the most favourable vacancy configuration is identified from unrelaxed static energies. The chosen defect structures are then relaxed to obtain incremental vacancy formation energies ΔEv. A single‑point DFT+U calculation on each relaxed structure yields Bader charges, from which the net electronic charge Δe per oxygen atom is extracted. In a separate set of calculations, the climbing‑image nudged elastic band (CI‑NEB) method is used to determine the lowest oxygen vacancy migration barrier at each δ. The collected data allow a direct examination of whether a simple linear relationship exists between Δe and ΔEv, and between Δe and the migration barriers, without requiring large‑scale trial‑and‑error searches.

## Reproduction target
Produce two CSV files that contain the raw computed data:
- `dE_vs_de.csv` with columns `system, delta, de_per_O, dE_V` for δ = 0.0, 0.125, 0.25, 0.375 (rows for SF, A.Y, B.Cu).
- `barriers_vs_de.csv` with columns `system, delta, barrier_eV, de_per_O` for δ = 0.125, 0.25, 0.375 (rows for SF, A.Y, B.Cu).
The hidden verifier will independently analyze these raw data and quantify the strength and direction of the correlations between Δe and ΔEv, and between Δe and the migration barriers, confirming whether they reproduce the trends reported in the literature.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader Charge Analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/
- PAW pseudopotentials: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Magnetic ordering selection
- Role: process
- Action: Determine the most stable magnetic ordering (FM, A‑AFM, C‑AFM, G‑AFM) for a 2×2×2 SrFeO₃ supercell using DFT+U; select the FM phase for subsequent doping models.
- Evidence: `/app/outputs/mag_order.log`

### Step 2: Construction of doped supercell models
- Role: process
- Action: Build 2×2×2 supercells for pristine SrFeO₃ (SF), A‑site Y‑doped Sr₇YFe₈O₂₄ (A.Y), and B‑site Cu‑doped Sr₈Fe₇CuO₂₄ (B.Cu) with FM magnetic ordering.
- Evidence: none

### Step 3: Oxygen vacancy site selection
- Role: process
- Action: For each system, sequentially screen all single‑oxygen‑vacancy sites at δ = 0.125, 0.25, 0.375 using unrelaxed static DFT energies; select the most energetically favourable configurations.
- Evidence: none

### Step 4: Geometry relaxation and vacancy formation energy
- Role: process
- Action: Perform DFT+U ionic relaxation on the chosen defect supercells; compute incremental vacancy formation energies ΔEv(δ→δ+0.125) using total energies and an O₂ binding energy correction (open‑source equivalent).
- Evidence: none

### Step 5: Single‑point electronic structure and charge analysis
- Role: process
- Action: Perform single‑point DFT+U calculations on the relaxed structures; compute Bader charges and extract the net electronic charge Δe per oxygen atom (Δe = N(ion) − N(atom)).
- Evidence: none

### Step 6: Nudged elastic band migration barriers
- Role: process
- Action: Using the CI‑NEB method, compute oxygen vacancy migration barriers for SF, A.Y, and B.Cu at δ = 0.125, 0.25, 0.375; identify the lowest‑energy migration pathway at each δ.
- Evidence: none

### Step 7: Collect Δe and ΔEv
- Role: scored (load-bearing)
- Action: Collect Δe per O atom and incremental vacancy formation energy ΔEv for SF, A.Y, and B.Cu at δ = 0, 0.125, 0.25, 0.375 and save to dE_vs_de.csv.
- Output file: `/app/outputs/dE_vs_de.csv`
- Format: csv
- Contract: columns: system, delta, de_per_O, dE_V
- Scoring: scored by hidden verifier

### Step 8: Collect barriers and Δe
- Role: scored (load-bearing)
- Action: Collect the lowest oxygen vacancy migration barrier and the corresponding Δe per O atom for SF, A.Y, and B.Cu at δ = 0.125, 0.25, 0.375 and save to barriers_vs_de.csv.
- Output file: `/app/outputs/barriers_vs_de.csv`
- Format: csv
- Contract: columns: system, delta, barrier_eV, de_per_O
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dE_vs_de.csv`
- `/app/outputs/barriers_vs_de.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dE_vs_de.csv
- path: `/app/outputs/dE_vs_de.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw data for recomputing Pearson correlation between Δe and ΔEv.
- schema:
  - `type`: table
  - `required_columns`: `system`, `delta`, `de_per_O`, `dE_V`

### barriers_vs_de.csv
- path: `/app/outputs/barriers_vs_de.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw data for recomputing Pearson correlation between oxygen vacancy migration barrier and Δe.
- schema:
  - `type`: table
  - `required_columns`: `system`, `delta`, `barrier_eV`, `de_per_O`

Notes: The checker recomputes Pearson correlation coefficients from the submitted raw values and checks for strong positive correlation (Δe vs ΔEv) and strong negative correlation (barrier vs Δe) consistent with the paper's claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dE_vs_de.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "delta",
          "de_per_O",
          "dE_V"
        ]
      },
      "description": "Raw data for recomputing Pearson correlation between Δe and ΔEv."
    },
    {
      "file": "barriers_vs_de.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "delta",
          "barrier_eV",
          "de_per_O"
        ]
      },
      "description": "Raw data for recomputing Pearson correlation between oxygen vacancy migration barrier and Δe."
    }
  ],
  "notes": "The checker recomputes Pearson correlation coefficients from the submitted raw values and checks for strong positive correlation (Δe vs ΔEv) and strong negative correlation (barrier vs Δe) consistent with the paper's claims."
}
```

## How you are scored
A hidden checker reads your submitted CSV files and recomputes Pearson correlation coefficients for the two relationships: (1) Δe vs ΔEv for each system, and (2) barrier vs Δe for each system. It then compares the computed correlations against the expected direction and strength. The score reflects how well your results demonstrate the predicted linear trends; stronger, direction‑consistent correlations earn higher reward. The final reward is a weighted average across these checks, with the primary weight on the two correlation analyses. Simply producing the output files is not enough—the computed correlations must be meaningful.
