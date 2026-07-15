# Lu‑Grover Isobaric Heat Capacity for β‑Sn at High Pressure

## Problem background
High-pressure Gibbs energy approaches for CALPHAD thermodynamic databases often produce unphysical extrapolations of the heat capacity at elevated pressures, such as negative Cp values. One candidate model to describe the volume contribution is the Lu‑Grover model, which has been applied to various materials. For β‑Sn, it has been suggested that this model may lead to unphysical isobaric heat capacities at high pressure, limiting its applicability. The present task investigates this behavior by computing Cp at 300 K for several pressures using the Lu‑Grover model.

## Approach
The Lu‑Grover volume model expresses the molar volume V(T,p) through an exponential integral function, with a material-dependent parameter c. The pressure‑dependent Gibbs energy is obtained as G(T,p) = G⁰(T) + c K_T⁰ (exp((V⁰−V)/c) − 1), where G⁰(T), V⁰(T), and K_T⁰(T) are atmospheric‑pressure reference properties. The isobaric heat capacity Cp is then derived numerically from the second temperature derivative of G. For β‑Sn, the parameter c = 2.945×10⁻⁶ (in appropriate molar‑volume units) and the atmospheric‑pressure functions V⁰(T), K_T⁰(T), α⁰(T), and G⁰(T) are provided by two public datasets (Deffrennes & Oudot 2021 and Khvan et al. 2019). The agent must implement these functions, compute Cp over a temperature grid (0–600 K) at four fixed pressures (1×10⁵, 5×10⁹, 1×10¹⁰, and 1.5×10¹⁰ Pa), and extract the Cp values at 300 K.

## Reproduction target
Using the Lu‑Grover model with c = 2.945×10⁻⁶ and the atmospheric‑pressure reference functions from the specified datasets, compute the isobaric heat capacity Cp of β‑Sn at 300 K for the following four pressures: 1×10⁵ Pa, 5×10⁹ Pa, 1×10¹⁰ Pa, and 1.5×10¹⁰ Pa. Output these four Cp values in a CSV file. The goal is to determine the model's prediction for Cp at these conditions, and in particular whether Cp becomes negative at the highest pressures.

## Assets

- Deffrennes & Oudot 2021 self-consistent model dataset: 10.17632/xskt8cj82b.1
- Khvan et al. 2019 thermodynamic description of Sn: 10.1016/j.calphad.2019.02.003
- SciPy library: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Obtain atmospheric-pressure reference functions for β-Sn
- Role: process
- Action: Download and parse the Deffrennes & Oudot (2021) dataset (DOI:10.17632/xskt8cj82b.1) to obtain the parameters describing V⁰(T), K_T⁰(T), and α⁰(T) for β-Sn. Retrieve the atmospheric-pressure Gibbs energy G⁰(T) from Khvan et al. (2019) (DOI:10.1016/j.calphad.2019.02.003). Implement functions that return V⁰(T), K_T⁰(T), α⁰(T), and G⁰(T) for a given temperature T.
- Evidence: `/app/outputs/ref_data_loaded.txt`

### Step 2: Compute Cp at 300 K using Lu-Grover model
- Role: scored (load-bearing)
- Action: Using the Lu-Grover volume model (Eq. (3.1)) with c = 2.945e-6 and the reference functions from the previous step, compute the Gibbs energy G(T,p) = G⁰(T) + ΔG where ΔG = c K_T⁰ (exp((V⁰−V)/c) − 1). Numerically obtain the isobaric heat capacity Cp = −T ∂²G/∂T² via finite differences for temperatures 0–600 K at pressures 1×10⁵ Pa, 5 GPa, 10 GPa, and 15 GPa. Output a CSV file with the Cp values at T=300 K for each pressure.
- Output file: `/app/outputs/cp_at_300K.csv`
- Format: csv
- Contract: CSV with columns: pressure_Pa (float), Cp_J_mol_K (float). Four rows, one per pressure (1e5, 5e9, 1e10, 1.5e10).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cp_at_300K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cp_at_300K.csv
- path: `/app/outputs/cp_at_300K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Isobaric heat capacity of β-Sn at 300 K for pressures 1×10⁵, 5×10⁹, 1×10¹⁰, and 1.5×10¹⁰ Pa. Values are compared to reference values within a tolerance to confirm the negative Cp anomaly above ~10 GPa.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `pressure_Pa`, `Cp_J_mol_K`
  - `units`:
    - `pressure_Pa`: Pa
    - `Cp_J_mol_K`: J/(mol·K)

Notes: The hidden checker compares the submitted Cp values at 300 K against the paper-reported reference values (extracted from Fig. 1) and verifies that Cp is negative at 10 GPa and above. The agent must implement the full computation; the c parameter is provided as a constant.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cp_at_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "pressure_Pa",
          "Cp_J_mol_K"
        ],
        "units": {
          "pressure_Pa": "Pa",
          "Cp_J_mol_K": "J/(mol·K)"
        }
      },
      "description": "Isobaric heat capacity of β-Sn at 300 K for pressures 1×10⁵, 5×10⁹, 1×10¹⁰, and 1.5×10¹⁰ Pa. Values are compared to reference values within a tolerance to confirm the negative Cp anomaly above ~10 GPa."
    }
  ],
  "notes": "The hidden checker compares the submitted Cp values at 300 K against the paper-reported reference values (extracted from Fig. 1) and verifies that Cp is negative at 10 GPa and above. The agent must implement the full computation; the c parameter is provided as a constant."
}
```

## How you are scored
A hidden verifier reads your cp_at_300K.csv and compares the four Cp values against reference values obtained from the published study using the same model. Your score depends on how closely your values agree with the reference (within a tolerance that accounts for minor numerical differences). Additionally, the verifier checks that the Cp values at 10 GPa and above are negative. Each workflow step contributes to the final reward; the Cp computation step is the primary scored artifact. Simply reporting the paper's numbers without performing the computation will not succeed, because the verifier expects the result of an honest implementation.
