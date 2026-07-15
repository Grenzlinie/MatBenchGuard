# CALPHAD Thermodynamic Calculation of Ti‑Ni B2 Phase and Martensitic Properties

## Problem background
The Ti‑Ni system is the basis for the most widely used shape memory alloys (SMAs), whose unique properties originate from a thermoelastic martensitic transformation of the B2 (CsCl‑type) parent phase to the monoclinic B19′ martensite. The composition range of the B2 phase and the thermodynamic properties of the transformation are critical for predicting transformation temperatures, enthalpies, and stress‑temperature behavior. In this work, a symmetric two‑sublattice model (Ni,Ti,Va)₀.₅(Ni,Ti,Va)₀.₅ is applied to describe the ordered B2 phase and to couple it with the disordered b.c.c. A2 phase, while a two‑sublattice model (Ni,Va)₀.₅(Ni,Ti)₀.₅ is used for the B19′ phase. The objective is to compute, from the provided model parameters, the phase diagram of the Ti‑Ni system with an emphasis on the B2 phase boundaries, and several thermodynamic quantities that characterize the B2→B19′ martensitic transformation: the T₀ temperature (where the Gibbs energies of the two phases are equal), the martensitic start temperature Mₛ, the transformation enthalpy ΔH, and the Clausius–Clapeyron stress rate dσ/dT.

## Approach
Implement the Gibbs energy models using the open‑source CALPHAD library pycalphad together with the SGTE pure‑element database for the reference states of Ni and Ti. The B2 phase is treated as an ordered counterpart of the A2 phase via a single Gibbs energy function that consists of a disordered contribution plus an ordering contribution; a magnetic contribution to the Gibbs energy is included. The B19′ phase is described with a two‑sublattice model using the parameters given in the Appendix. With these models, compute the equilibrium Ti–Ni phase diagram over the full composition range and a wide temperature interval using the pycalphad equilibrium solver. Then, for a fine composition grid on both sides of the equiatomic composition, compute the following quantities: (a) the T₀ temperature by solving G_B2 = G_B19′ at each composition; (b) the Mₛ temperature by solving G_B2 − G_B19′ = 150 J/mol; (c) the absolute transformation enthalpy ΔH = H_B2 − H_B19′ evaluated at the T₀ temperature; and (d) the stress rate dσ/dT using the Clausius–Clapeyron relation dσ/dT = −ΔH/(T₀ · ε) for two assumed transformation strains (6% and 8%). The computed curves are saved as CSV files for downstream scoring.

## Reproduction target
Produce the following files under `/app/outputs`:

1. `phase_diagram_data.csv`: phase‑boundary data for the Ti–Ni system (temperature 300–2000 K, Ni mole fraction 0–1; columns: T (K), x_Ni, phase). Sample the boundaries densely enough to identify the congruent melting point of B2 and its solubility limits.
2. `T0_vs_Ni.csv`: T₀ temperature for Ni mole fractions 0.48–0.55 (step ≤ 0.001); columns: x_Ni, T0 (K).
3. `Ms_vs_Ni.csv`: Mₛ temperature for Ni mole fractions 0.48–0.515 (step ≤ 0.001); columns: x_Ni, Ms (K).
4. `enthalpy_vs_Ni.csv`: absolute transformation enthalpy (J/mol) for the same composition range as Mₛ; columns: x_Ni, dH (J/mol).
5. `stress_rate_vs_Ni.csv`: stress rate dσ/dT (MPa/K) for transformation strains 6% and 8%, same composition range; columns: x_Ni, dsigma_dT_6pct, dsigma_dT_8pct.

All calculations must use the Gibbs energy parameters provided in the Appendix of this instruction and the SGTE unary database.

## Assets

- pycalphad (CALPHAD calculation library): pycalphad
- SGTE pure‑element database (unary data)

## Workflow steps

### Step 1: Set up thermodynamic models
- Role: process
- Action: Implement the Gibbs energy functions for the disordered BCC (A2) phase, the ordered B2 phase (symmetric two‑sublattice with ordering contribution), and the B19' phase (two‑sublattice) using pycalphad. Create a pycalphad Database object containing pure‑element reference states from SGTE and the model parameters exactly as provided in the Appendix (given in the prompt). Prepare the system for subsequent equilibrium and property calculations.
- Evidence: none

### Step 2: Compute Ti‑Ni phase diagram
- Role: scored (load-bearing)
- Action: Calculate the equilibrium phase diagram of the Ti‑Ni system over temperature 300–2000 K and composition 0–100 at.% Ni using pycalphad's equilibrium solver. For each equilibrium point, record temperature (K), mole fraction Ni (x_Ni), and the stable phases present. Sample densely enough to identify the B2 phase boundaries, congruent melting point, and Ti‑rich solubility limit.
- Output file: `/app/outputs/phase_diagram_data.csv`
- Format: csv
- Contract: Columns: T (float, K), x_Ni (float), phase (string).
- Scoring: scored by hidden verifier

### Step 3: Compute T0 temperature
- Role: scored (load-bearing)
- Action: For a series of Ni mole fractions in 0.48–0.55 (step ≤ 0.001), compute the T0 temperature where the molar Gibbs energy of B2 equals that of B19' (the thermodynamic equilibrium between B2 parent and B19' martensite). Use the Gibbs energy functions from step 0. For each composition, find T in 200–600 K where G_B2 = G_B19'. Write composition–T0 pairs.
- Output file: `/app/outputs/T0_vs_Ni.csv`
- Format: csv
- Contract: Columns: x_Ni (float), T0 (float, K).
- Scoring: scored by hidden verifier

### Step 4: Compute Ms temperature
- Role: scored
- Action: For Ni mole fractions in 0.48–0.515 (step ≤ 0.001), compute the martensitic start temperature Ms assuming a constant chemical driving force of 150 J/mol: find T such that G_B2(T,x) − G_B19'(T,x) = 150 J/mol. Use the models from step 0. Write composition–Ms pairs.
- Output file: `/app/outputs/Ms_vs_Ni.csv`
- Format: csv
- Contract: Columns: x_Ni (float), Ms (float, K).
- Scoring: scored by hidden verifier

### Step 5: Compute transformation enthalpy
- Role: scored
- Action: For Ni mole fractions in 0.48–0.515 (step ≤ 0.001), compute the absolute transformation enthalpy ΔH (J/mol) for B2→B19' at the T0 temperature corresponding to each composition: ΔH = H_B2(T0,x) − H_B19'(T0,x). Write composition–enthalpy pairs.
- Output file: `/app/outputs/enthalpy_vs_Ni.csv`
- Format: csv
- Contract: Columns: x_Ni (float), dH (float, J/mol).
- Scoring: scored by hidden verifier

### Step 6: Compute stress rate dσ/dT
- Role: scored
- Action: For Ni mole fractions in 0.48–0.515 (step ≤ 0.001), compute the Clausius‑Clapeyron stress rate dσ/dT for two transformation strains (6% and 8%) using dσ/dT = −ΔH / (T0 · ε). Use ΔH and T0 from previous steps. Write composition and both stress‑rate values.
- Output file: `/app/outputs/stress_rate_vs_Ni.csv`
- Format: csv
- Contract: Columns: x_Ni (float), dsigma_dT_6pct (float, MPa/K), dsigma_dT_8pct (float, MPa/K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_data.csv`
- `/app/outputs/T0_vs_Ni.csv`
- `/app/outputs/Ms_vs_Ni.csv`
- `/app/outputs/enthalpy_vs_Ni.csv`
- `/app/outputs/stress_rate_vs_Ni.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_data.csv
- path: `/app/outputs/phase_diagram_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Phase boundary coordinates of the Ti‑Ni system. The checker extracts key features (congruent melting point, solubility limits) and compares them to the paper's reported values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `x_Ni`, `phase`
  - `units`:
    - `T`: K
    - `x_Ni`: mole fraction
    - `phase`: string

### T0_vs_Ni.csv
- path: `/app/outputs/T0_vs_Ni.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: T0 temperature vs. Ni content. The checker extracts T0 at specific compositions and compares to paper values.
- schema:
  - `type`: table
  - `required_columns`: `x_Ni`, `T0`
  - `units`:
    - `x_Ni`: mole fraction
    - `T0`: K

### Ms_vs_Ni.csv
- path: `/app/outputs/Ms_vs_Ni.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Martensite start temperature vs. Ni content. The checker extracts Ms at key compositions and compares to paper values.
- schema:
  - `type`: table
  - `required_columns`: `x_Ni`, `Ms`
  - `units`:
    - `x_Ni`: mole fraction
    - `Ms`: K

### enthalpy_vs_Ni.csv
- path: `/app/outputs/enthalpy_vs_Ni.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Transformation enthalpy vs. Ni content. The checker reads the value at equiatomic composition and compares to the paper.
- schema:
  - `type`: table
  - `required_columns`: `x_Ni`, `dH`
  - `units`:
    - `x_Ni`: mole fraction
    - `dH`: J/mol

### stress_rate_vs_Ni.csv
- path: `/app/outputs/stress_rate_vs_Ni.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress rate vs. Ni content for 6% and 8% strain. The checker extracts a value at a specific composition and compares to the paper.
- schema:
  - `type`: table
  - `required_columns`: `x_Ni`, `dsigma_dT_6pct`, `dsigma_dT_8pct`
  - `units`:
    - `x_Ni`: mole fraction
    - `dsigma_dT_6pct`: MPa/K
    - `dsigma_dT_8pct`: MPa/K

Notes: All outputs are computed using the model parameters given in the Appendix. The checker extracts key scalar values from these CSV files and compares them against the paper's reported numbers with per‑quantity tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "x_Ni",
          "phase"
        ],
        "units": {
          "T": "K",
          "x_Ni": "mole fraction",
          "phase": "string"
        }
      },
      "description": "Phase boundary coordinates of the Ti‑Ni system. The checker extracts key features (congruent melting point, solubility limits) and compares them to the paper's reported values."
    },
    {
      "file": "T0_vs_Ni.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Ni",
          "T0"
        ],
        "units": {
          "x_Ni": "mole fraction",
          "T0": "K"
        }
      },
      "description": "T0 temperature vs. Ni content. The checker extracts T0 at specific compositions and compares to paper values."
    },
    {
      "file": "Ms_vs_Ni.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Ni",
          "Ms"
        ],
        "units": {
          "x_Ni": "mole fraction",
          "Ms": "K"
        }
      },
      "description": "Martensite start temperature vs. Ni content. The checker extracts Ms at key compositions and compares to paper values."
    },
    {
      "file": "enthalpy_vs_Ni.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Ni",
          "dH"
        ],
        "units": {
          "x_Ni": "mole fraction",
          "dH": "J/mol"
        }
      },
      "description": "Transformation enthalpy vs. Ni content. The checker reads the value at equiatomic composition and compares to the paper."
    },
    {
      "file": "stress_rate_vs_Ni.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Ni",
          "dsigma_dT_6pct",
          "dsigma_dT_8pct"
        ],
        "units": {
          "x_Ni": "mole fraction",
          "dsigma_dT_6pct": "MPa/K",
          "dsigma_dT_8pct": "MPa/K"
        }
      },
      "description": "Stress rate vs. Ni content for 6% and 8% strain. The checker extracts a value at a specific composition and compares to the paper."
    }
  ],
  "notes": "All outputs are computed using the model parameters given in the Appendix. The checker extracts key scalar values from these CSV files and compares them against the paper's reported numbers with per‑quantity tolerances."
}
```

## How you are scored
After the deadline, a hidden verifier reads each output CSV. It extracts key scalar quantities from the files:
- From `phase_diagram_data.csv`: the congruent melting point of B2 and the B2 Ti‑rich solubility limit at 1400 K.
- From `T0_vs_Ni.csv`: T₀ at two specific Ni fractions.
- From `Ms_vs_Ni.csv`: Mₛ at two specific compositions.
- From `enthalpy_vs_Ni.csv`: ΔH at the equiatomic composition.
- From `stress_rate_vs_Ni.csv`: dσ/dT for the 6% strain case at a given composition.

Each extracted value is compared to a hidden reference using a per‑quantity tolerance: full credit is awarded when the absolute difference is within the tolerance; outside that, the score decreases linearly to zero at 2 × the tolerance. The total reward is the weighted sum:
- phase diagram: 0.3
- T₀: 0.2
- Mₛ: 0.2
- enthalpy: 0.15
- stress rate: 0.15

Only artifacts that conform to the specified schemas (columns, units) will be scored; missing or malformed files receive zero credit for that artifact.
