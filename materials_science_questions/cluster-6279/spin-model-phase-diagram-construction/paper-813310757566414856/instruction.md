# Finite-Temperature Hartree-Fock Spin-1 Bose Gas Phase Boundary Computation

## Problem background
A spin-1 Bose gas, described by a three-component order parameter, can form ferromagnetic, polar, antiferromagnetic, and broken-axisymmetry phases depending on the linear Zeeman energy (p) and quadratic Zeeman energy (q). At finite temperature, thermal fluctuations modify the phase boundaries. A self-consistent Hartree-Fock (HF) mean-field theory that includes the noncondensate atoms and their spin coherence predicts how these boundaries shift. This task investigates the temperature dependence of two key phase boundaries for both antiferromagnetic and ferromagnetic interactions, and quantifies the role of noncondensate spin coherence.

## Approach
Implement a uniform spin-1 Bose gas HF solver that iteratively solves the generalized Gross-Pitaevskii equation for the condensate spinor and evaluates the noncondensate density matrix from the Bose-Einstein distribution of excitation eigenvalues. The solver is run in two modes: full HF (allows off-diagonal noncondensate spin coherence) and truncated HF (off-diagonal elements forced to zero). For antiferromagnetic interactions (c1/c0 = 0.05) with fixed q = -3 c1 n, determine the linear Zeeman energy p_b at which the condensate longitudinal magnetization attains saturation (AFM-FM boundary). For ferromagnetic interactions (c1/c0 = -0.05) with fixed p = 0, determine the quadratic Zeeman energy q_b at which the condensate longitudinal magnetization vanishes (BA-P boundary). Both boundaries are located via root-finding as a function of temperature. Record the boundary value, condensate fraction, and the relevant noncondensate spin density at each temperature for both HF variants.

## Reproduction target
For antiferromagnetic interactions at c1/c0 = 0.05 and q = -3 c1 n, compute the AFM-FM phase boundary p_b as a function of reduced temperature T/T0 in the range [0, 0.5]. For each temperature report p_b/(c1 n), n^c/n, and F_z^{nc}/n for both full HF and truncated HF, gathered in a CSV. For ferromagnetic interactions at c1/c0 = -0.05 and p = 0, compute the BA-P phase boundary q_b as a function of T/T0 in [0, 0.5]. For each temperature report q_b/(|c1| n), n^c/n, and d^{nc}/n for both full and truncated HF. The output files must contain at least ten temperature points. The goal is to produce consistent results that satisfy the analytic relations linking the phase boundary to the condensate fraction and noncondensate spin density.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Build Hartree-Fock solver module
- Role: process
- Action: Implement a Python module that solves the self-consistent Hartree-Fock equations for a uniform spin-1 Bose gas. The solver must accept interaction parameters (c0, c1), Zeeman energies (p, q), temperature T, total density n, and a boolean flag 'include_coherence'. When include_coherence=True, the noncondensate density matrix is allowed to have off-diagonal elements (full HF). When False, off-diagonal elements are explicitly set to zero (truncated HF). The module must iteratively solve the generalized Gross-Pitaevskii equation and the noncondensate density matrix until convergence, outputting the condensate spinor, noncondensate density matrix, chemical potential, and excitation eigenvalues.
- Evidence: `/app/outputs/hf_solver.py`

### Step 2: Compute AFM-FM phase boundary vs temperature
- Role: scored (load-bearing)
- Action: Set antiferromagnetic interaction parameters: c1/c0 = 0.05, quadratic Zeeman energy q = -3 c1 n. For temperatures T/T0 from 0 to 0.5 (at least 10 points), find the linear Zeeman energy p_b at which the condensate longitudinal magnetization satisfies F_z^c / n^c = 1 (within tolerance 1e-4), marking the AFM-FM phase boundary. Perform a binary search over p for each temperature. Run both the full HF solver (include_coherence=True) and the truncated HF solver (include_coherence=False). For each temperature and each solver variant, record the boundary value, the condensate fraction n^c/n, and the noncondensate longitudinal magnetization F_z^{nc}/n. Write a CSV with columns: T_div_T0, p_b_over_c1n, n_c_over_n, Fz_nc_over_n, p_b_over_c1n_truncated, n_c_over_n_truncated, Fz_nc_over_n_truncated.
- Output file: `/app/outputs/step_01_phase_boundary_afm.csv`
- Format: csv
- Contract: Columns: T_div_T0 (float), p_b_over_c1n (float), n_c_over_n (float), Fz_nc_over_n (float), p_b_over_c1n_truncated (float), n_c_over_n_truncated (float), Fz_nc_over_n_truncated (float). Each row corresponds to a temperature in the range [0, 0.5].
- Scoring: scored by hidden verifier

### Step 3: Compute BA-P phase boundary vs temperature
- Role: scored (load-bearing)
- Action: Set ferromagnetic interaction parameters: c1/c0 = -0.05, linear Zeeman energy p = 0. For temperatures T/T0 from 0 to 0.5 (at least 10 points), find the quadratic Zeeman energy q_b at which the condensate transverse magnetization vanishes (F_z^c = 0), marking the BA-P phase boundary. Use root-finding over q. Run both the full HF solver (include_coherence=True) and the truncated HF solver (include_coherence=False). For each temperature and solver variant, record the boundary value q_b/(|c1|n), the condensate fraction n^c/n, and the noncondensate spin coherence parameter d^{nc}/n. Write a CSV with columns: T_div_T0, q_b_over_abs_c1n, n_c_over_n, d_nc_over_n, q_b_over_abs_c1n_truncated, n_c_over_n_truncated, d_nc_over_n_truncated.
- Output file: `/app/outputs/step_02_phase_boundary_ba.csv`
- Format: csv
- Contract: Columns: T_div_T0 (float), q_b_over_abs_c1n (float), n_c_over_n (float), d_nc_over_n (float), q_b_over_abs_c1n_truncated (float), n_c_over_n_truncated (float), d_nc_over_n_truncated (float). Each row corresponds to a temperature in the range [0, 0.5].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phase_boundary_afm.csv`
- `/app/outputs/step_02_phase_boundary_ba.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phase_boundary_afm.csv
- path: `/app/outputs/step_01_phase_boundary_afm.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: AFM-FM phase boundary data as a function of temperature. The checker recomputes the expected boundary from n^c/n and F_z^{nc}/n using the analytic formulas for full and truncated HF and verifies consistency.
- schema:
  - `type`: table
  - `required_columns`: `T_div_T0`, `p_b_over_c1n`, `n_c_over_n`, `Fz_nc_over_n`, `p_b_over_c1n_truncated`, `n_c_over_n_truncated`, `Fz_nc_over_n_truncated`
  - `units`: object

### step_02_phase_boundary_ba.csv
- path: `/app/outputs/step_02_phase_boundary_ba.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: BA-P phase boundary data as a function of temperature. The checker recomputes the expected boundary from n^c/n and d^{nc}/n using the analytic formulas for full and truncated HF and verifies consistency.
- schema:
  - `type`: table
  - `required_columns`: `T_div_T0`, `q_b_over_abs_c1n`, `n_c_over_n`, `d_nc_over_n`, `q_b_over_abs_c1n_truncated`, `n_c_over_n_truncated`, `d_nc_over_n_truncated`
  - `units`: object

Notes: The agent must implement the HF solver from scratch. The analytic consistency check serves as a strong load-bearing mechanism: the reported numbers must satisfy the derived relations. The phase boundary search requires root-finding over p or q.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phase_boundary_afm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_T0",
          "p_b_over_c1n",
          "n_c_over_n",
          "Fz_nc_over_n",
          "p_b_over_c1n_truncated",
          "n_c_over_n_truncated",
          "Fz_nc_over_n_truncated"
        ],
        "units": {}
      },
      "description": "AFM-FM phase boundary data as a function of temperature. The checker recomputes the expected boundary from n^c/n and F_z^{nc}/n using the analytic formulas for full and truncated HF and verifies consistency."
    },
    {
      "file": "step_02_phase_boundary_ba.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_T0",
          "q_b_over_abs_c1n",
          "n_c_over_n",
          "d_nc_over_n",
          "q_b_over_abs_c1n_truncated",
          "n_c_over_n_truncated",
          "d_nc_over_n_truncated"
        ],
        "units": {}
      },
      "description": "BA-P phase boundary data as a function of temperature. The checker recomputes the expected boundary from n^c/n and d^{nc}/n using the analytic formulas for full and truncated HF and verifies consistency."
    }
  ],
  "notes": "The agent must implement the HF solver from scratch. The analytic consistency check serves as a strong load-bearing mechanism: the reported numbers must satisfy the derived relations. The phase boundary search requires root-finding over p or q."
}
```

## How you are scored
A hidden verifier independently inspects each scored CSV. It uses the analytic relations, which express the phase boundary in terms of the condensate fraction and the noncondensate spin density, to recompute the expected boundary from your reported numbers. The verifier compares the recomputed boundary to the boundary value you supplied; a row that agrees within a hidden tolerance earns partial credit. The total reward is the weighted sum of scores over both CSVs. Reporting a known value without performing the self-consistent HF computation will not satisfy the consistency checks.
