# Compute Critical Temperatures via Decoration-Iteration Mapping

## Problem background
The mixed spin-1/2 and spin-1 Ising-Heisenberg ferromagnet on a diamond-decorated triangular lattice is a quantum many-body model that captures competition between easy-axis and easy-plane exchange anisotropies and single-ion anisotropy. The model consists of spin-1/2 Ising atoms on original triangular-lattice sites and spin-1 Heisenberg atoms decorating each bond as a diamond spin cluster, with Hamiltonian given by Eq. (1) of the task description. An exact decoration-iteration mapping transformation relates this hybrid model to a spin-1/2 Ising model on a simple triangular lattice, whose critical temperature is known exactly. This mapping allows the critical temperature T_c of the decorated model to be obtained as a function of the exchange anisotropy Δ and the single-ion anisotropy D/J_I, without approximations. This task computes T_c for a range of these anisotropy parameters to investigate the resulting critical behaviour.

## Approach
Use the decoration-iteration mapping described in the provided reference (Strečka and Jaščur, Phys. Stat. Sol. (b) 233, R12, 2002). The mapping expresses the partition function of the decorated lattice in terms of an effective spin-1/2 Ising model on a simple triangular lattice, with mapping parameters A and R determined from self-consistency conditions applied to the eigenvalues of a single diamond cluster (bond Hamiltonian). The explicit formulas for the mapping parameters can be found in that reference. Once the effective Ising interaction R is computed for given Hamiltonian parameters (J_H/J_I = 1.0, Δ, and D/J_I), the critical temperature follows from the known exact critical condition of the triangular Ising model: k_B T_c = R / ln 3. The computation is repeated for the required ranges of Δ and D/J_I to generate a table of critical temperatures, which are written to the output CSV file.

## Reproduction target
Compute the critical temperature T_c (in units of k_B/J_I) for the following parameter sweeps, all with J_H/J_I = 1.0:
- Sweep over Δ from 0 to 3 in steps of 0.25, at fixed D/J_I values of -0.5, 0.0, 0.5, 1.0, 2.0. Label these rows with param='Delta' and param_value as the Δ value.
- Sweep over D/J_I from -0.5 to 2.0 in steps of 0.25, at fixed Δ values of 0.5, 1.0, 1.5, 2.0, 3.0. Label these rows with param='D_J_I' and param_value as the D/J_I value.
Produce a single CSV file (`critical_temperatures.csv`) with three columns: `param` (either 'Delta' or 'D_J_I'), `param_value` (float), and `T_c` (float, critical temperature). Each row corresponds to one computed critical temperature.

## Assets

- Strečka and Jaščur, Phys. Stat. Sol. (b) 233, R12 (2002): 10.1002/pssb.200290014

## Workflow steps

### Step 1: Compute critical temperatures
- Role: scored (load-bearing)
- Action: Implement the exact decoration-iteration mapping for the mixed spin-1/2 and spin-1 Ising-Heisenberg model on the diamond-decorated triangular lattice. For the specified parameter sets (Δ values at constant D/J_I, and D/J_I values at constant Δ, all with J_H/J_I = 1.0), calculate the effective Ising interaction R from the self-consistency conditions using the formulas from the mapping reference, then obtain the critical temperature T_c = R / ln 3. Write the results to critical_temperatures.csv.
- Output file: `/app/outputs/critical_temperatures.csv`
- Format: csv
- Contract: CSV with three columns: 'param', 'param_value', 'T_c'. param is either 'Delta' or 'D_J_I'. param_value is the numeric value. T_c is the computed critical temperature (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_temperatures.csv
- path: `/app/outputs/critical_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Critical temperatures T_c (in units of k_B/J_I) for the specified parameter sets, computed via the exact decoration-iteration mapping. The hidden checker compares each T_c to a gold precomputed from the same mapping within a small absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `param`, `param_value`, `T_c`
  - `units`: object

Notes: Only the scored artifact critical_temperatures.csv is required. The agent must implement the mapping and compute Tc; no intermediate artifacts are handed over. The parameter sweep ranges are exactly those specified in the step description.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "param",
          "param_value",
          "T_c"
        ],
        "units": {}
      },
      "description": "Critical temperatures T_c (in units of k_B/J_I) for the specified parameter sets, computed via the exact decoration-iteration mapping. The hidden checker compares each T_c to a gold precomputed from the same mapping within a small absolute tolerance."
    }
  ],
  "notes": "Only the scored artifact critical_temperatures.csv is required. The agent must implement the mapping and compute Tc; no intermediate artifacts are handed over. The parameter sweep ranges are exactly those specified in the step description."
}
```

## How you are scored
A hidden verifier will inspect your `critical_temperatures.csv`. It will compare each computed `T_c` against a set of gold critical-temperature values precomputed from the same mapping formulas. The verifier checks that all required rows are present (with `param` and `param_value` matching the expected sweep values) and that each `T_c` lies within a small absolute tolerance of the gold value. The total reward is the fraction of compliant rows, scaled appropriately. You do not need to match any specific paper-reported table or figure; you only need to submit a correctly computed CSV that passes the verifier's comparison.
