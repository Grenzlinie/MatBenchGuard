# Phase Diagrams and Magnetization of a Hexagonal Transverse Ising Nanoisland

## Problem background
This work studies the magnetic properties of a hexagonal transverse Ising nanoisland. The nanoisland consists of two layers, each with seven spin‑1/2 atoms: six surface atoms and one core atom (Figure 1A of the source). The Hamiltonian includes surface exchange J_s, surface‑core exchange J, interlayer exchange J_r, and transverse fields Ω_s (surface) and Ω_b (core). The objective is to understand how the reduced Curie temperature t_c = k_B T_c / J varies with the surface coupling enhancement Δs (where J_s = J (1 + Δs)), the interlayer coupling ratio r = J_r / J, and the ratio q = Ω_s / Ω_b of the transverse fields, as well as how the total magnetization m_T depends on the reduced temperature t = k_B T / J for selected interlayer couplings r.

## Approach
The effective‑field theory (EFT) with correlations is employed. Starting from the spin‑1/2 Hamiltonian with transverse fields, the differential operator technique is used to derive coupled equations for the surface magnetization m_s and the core magnetization m_c. When the temperature approaches the Curie temperature, the magnetizations become small and the equations can be linearized, leading to a homogeneous linear system whose nontrivial solution condition determines t_c for a given set of parameters. For the full temperature dependence of the magnetization, the nonlinear coupled equations are solved numerically, and the total magnetization is computed as m_T = (6 m_s + m_c) / 7. The task is to implement these equations and solve them for the parameter sweeps specified in the workflow steps.

## Reproduction target
Implement the effective‑field theory for the hexagonal nanoisland and numerically solve the transition‑temperature condition to compute t_c for three parameter sweeps: (i) Δs from 0.0 to 5.0 in steps of 0.5, for r = 0.0 and 1.5 with zero transverse fields; (ii) r from 0.0 to 10.0 in steps of 1.0, for Δs = 0.0 and 1.5; (iii) q = Ω_s / Ω_b from 0.0 to 10.0 in steps of 0.5, for r = 1.0, 3.0, 7.5, with Ω_b / J = 1.0 and Δs = 0.0. Also solve the full nonlinear magnetization equations to obtain m_T as a function of t from 0.0 to 10.0 in steps of 0.1 for r = 1.0, 4.0, 7.0, 10.0, with Δs = 0.0, Ω_b / J = 1.0, and q = 1.0. Write the results into CSV files as detailed in the workflow steps.

## Assets
No external datasets, pre‑trained models, or specialized tools are required. The computation can be performed with standard numerical libraries (e.g., numpy, scipy) in any programming language. All necessary equations and system specifications are contained in this instruction.

## Workflow steps

### Step 1: Phase diagram t_c vs Δs
- Role: scored (load-bearing)
- Action: Solve the linearized transition temperature equation derived from effective-field theory for the hexagonal nanoisland to obtain the reduced Curie temperature t_c as a function of the surface coupling enhancement Δs from 0.0 to 5.0 in steps of 0.5, for two fixed interlayer coupling ratios r=0.0 and 1.5, with zero transverse fields (Ω_s = Ω_b = 0). Write the numeric results to a CSV file.
- Output file: `/app/outputs/t_c_vs_delta_s.csv`
- Format: csv
- Contract: Columns: delta_s (float), r (float), t_c (float). Rows for each Δs from 0.0 to 5.0 in steps of 0.5, with one block for r=0.0 and one for r=1.5.
- Scoring: scored by hidden verifier

### Step 2: Phase diagram t_c vs r
- Role: scored
- Action: Solve the transition temperature equation to obtain t_c as a function of the interlayer coupling ratio r from 0.0 to 10.0 in steps of 1.0, for two fixed surface coupling enhancements Δs=0.0 and Δs=1.5, with zero transverse fields. Write the results to a CSV file.
- Output file: `/app/outputs/t_c_vs_r.csv`
- Format: csv
- Contract: Columns: r (float), delta_s (float), t_c (float). Rows for each r from 0.0 to 10.0 in steps of 1.0, with one block for Δs=0.0 and one for Δs=1.5.
- Scoring: scored by hidden verifier

### Step 3: Phase diagram t_c vs q
- Role: scored
- Action: Solve the transition temperature equation for the hexagonal nanoisland with non-zero transverse fields: set Ω_b/J = 1.0, Δs = 0.0, and for each of the three interlayer coupling ratios r = 1.0, 3.0, 7.5, compute t_c as a function of the transverse field ratio q = Ω_s/Ω_b from 0.0 to 10.0 in steps of 0.5. Write the results to a CSV file.
- Output file: `/app/outputs/t_c_vs_q.csv`
- Format: csv
- Contract: Columns: r (float), q (float), t_c (float). Rows for each q from 0.0 to 10.0 in steps of 0.5, with one block per r value (1.0, 3.0, 7.5).
- Scoring: scored by hidden verifier

### Step 4: Magnetization curves m_T vs T
- Role: scored (load-bearing)
- Action: Solve the full coupled effective-field magnetization equations numerically for the hexagonal nanoisland with Δs=0.0, Ω_b/J=1.0, Ω_s/Ω_b=1.0, for four interlayer coupling ratios r = 1.0, 4.0, 7.0, 10.0. Compute the total magnetization m_T = (6m_s + m_c)/7 as a function of reduced temperature t = k_B T/J from 0.0 to 10.0 in steps of 0.1 (or until magnetization vanishes). Write the results to a CSV file.
- Output file: `/app/outputs/m_T_vs_T.csv`
- Format: csv
- Contract: Columns: r (float), t (float), m_T (float). Rows for each t from 0.0 to 10.0 in steps of 0.1, with one block per r value (1.0, 4.0, 7.0, 10.0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/t_c_vs_delta_s.csv`
- `/app/outputs/t_c_vs_r.csv`
- `/app/outputs/t_c_vs_q.csv`
- `/app/outputs/m_T_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### t_c_vs_delta_s.csv
- path: `/app/outputs/t_c_vs_delta_s.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Reduced Curie temperature t_c vs surface coupling enhancement Δs for r=0.0 and 1.5.
- schema:
  - `columns`:
    - `delta_s`: float
    - `r`: float
    - `t_c`: float

### t_c_vs_r.csv
- path: `/app/outputs/t_c_vs_r.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Reduced Curie temperature t_c vs interlayer coupling r for Δs=0.0 and 1.5.
- schema:
  - `columns`:
    - `r`: float
    - `delta_s`: float
    - `t_c`: float

### t_c_vs_q.csv
- path: `/app/outputs/t_c_vs_q.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Reduced Curie temperature t_c vs transverse field ratio q for r=1.0, 3.0, 7.5.
- schema:
  - `columns`:
    - `r`: float
    - `q`: float
    - `t_c`: float

### m_T_vs_T.csv
- path: `/app/outputs/m_T_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total magnetization m_T vs reduced temperature t for r=1.0, 4.0, 7.0, 10.0.
- schema:
  - `columns`:
    - `r`: float
    - `t`: float
    - `m_T`: float

Notes: The task covers only the hexagonal nanoisland (Figure 1A). Comparison with other nanostructures is excluded. The agent must implement the effective-field theory equations from the geometry and Hamiltonian described in the instruction; no external datasets are required. All values are dimensionless.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "t_c_vs_delta_s.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "columns": {
          "delta_s": "float",
          "r": "float",
          "t_c": "float"
        }
      },
      "description": "Reduced Curie temperature t_c vs surface coupling enhancement Δs for r=0.0 and 1.5."
    },
    {
      "file": "t_c_vs_r.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "columns": {
          "r": "float",
          "delta_s": "float",
          "t_c": "float"
        }
      },
      "description": "Reduced Curie temperature t_c vs interlayer coupling r for Δs=0.0 and 1.5."
    },
    {
      "file": "t_c_vs_q.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "columns": {
          "r": "float",
          "q": "float",
          "t_c": "float"
        }
      },
      "description": "Reduced Curie temperature t_c vs transverse field ratio q for r=1.0, 3.0, 7.5."
    },
    {
      "file": "m_T_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "columns": {
          "r": "float",
          "t": "float",
          "m_T": "float"
        }
      },
      "description": "Total magnetization m_T vs reduced temperature t for r=1.0, 4.0, 7.0, 10.0."
    }
  ],
  "notes": "The task covers only the hexagonal nanoisland (Figure 1A). Comparison with other nanostructures is excluded. The agent must implement the effective-field theory equations from the geometry and Hamiltonian described in the instruction; no external datasets are required. All values are dimensionless."
}
```

## How you are scored
A hidden verifier independently scores each output file. It compares your computed t_c and m_T values to reference values derived from the paper's reported results, using appropriate tolerances. It also applies low‑weight structural checks (e.g., monotonic trends and expected qualitative features such as reentrant behavior) to verify that the computed curves exhibit physically consistent characteristics. The overall reward is a weighted sum of the per‑file scores.
