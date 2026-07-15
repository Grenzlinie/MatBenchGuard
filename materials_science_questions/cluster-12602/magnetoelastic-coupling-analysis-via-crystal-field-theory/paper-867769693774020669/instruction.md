# Ginzburg-Landau analysis of antiferromagnetic order in an FFLO superconductor

## Problem background
In the heavy-fermion superconductor CeCoIn5, an incommensurate antiferromagnetic (AFM) order coexists with a Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) superconducting state in high magnetic fields. Neutron scattering reveals two degenerate AFM wave vectors, and the FFLO state breaks translation symmetry, leading to a complex interplay between magnetism and superconductivity. Understanding which magnetic phase is realized and how it manifests in measurable quantities is an open question.

## Approach
The problem is analyzed with a two-component Ginzburg-Landau free energy functional. The order parameters η1 and η2 describe amplitudes of two degenerate incommensurate AFM states; the free energy includes quadratic terms with nearest-neighbor stiffness (parameterized by ξAF), quartic terms stabilizing a single-q or double-q ground state, and a commensurate coupling term that models the pinning effect of FFLO nodal planes on the magnetic moment. The functional is minimized numerically with respect to η1, η2 and the wave vectors q1, q2 at the given condition T/T_N^0 = 0.5, ξAF q0 = 0, using parameters b = 0.1, c2(N) = 0.01, and ξAF = 3. From the minimized state, three derived quantities are computed: (1) the phase (single-q or double-q) and the ratio η2/η1; (2) an analytic bound on the Bragg peak shift |q1 − q_inc|; (3) the NMR internal field distribution P(h) at In(2b) sites, obtained by evaluating the dipolar field on a representative spatial lattice and building a normalized histogram.

## Reproduction target
From the Ginzburg-Landau functional described above, compute at T/T_N^0 = 0.5 and ξAF q0 = 0: (1) the phase classification (single-q or double-q) and the order parameter ratio η2/η1; (2) the analytic bound on the main Bragg peak shift |q1 − q_inc|, expressed in units of π; (3) the NMR internal field distribution P(h) for the single-q phase at In(2b) sites, showing a double-peak structure. All results are written as output files under /app/outputs.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Free energy minimization and magnetization computation
- Role: process
- Action: Implement the Ginzburg-Landau free energy functional and numerically minimize with respect to η1, η2, q1, q2 for the condition T/T_N^0 = 0.5, ξAF q0 = 0, using parameters b = 0.1, c2(N) = 0.01, ξAF = 3. Compute the equilibrium magnetization profile M(r) using the minimized order parameters.
- Evidence: `/app/outputs/minimization_output.json`

### Step 2: Phase classification and order parameter ratio
- Role: scored
- Action: From the minimization results, determine the phase (single‑q or double‑q) and compute the ratio η2/η1 at T/T_N^0 = 0.5, ξAF q0 = 0. Write one row to phase_analysis.csv.
- Output file: `/app/outputs/phase_analysis.csv`
- Format: csv
- Contract: Columns: temperature_ratio (float), xiAF_q0 (float), phase (string: single‑q or double‑q), eta2_eta1_ratio (float). One row.
- Scoring: scored by hidden verifier

### Step 3: Bragg peak shift bound
- Role: scored
- Action: Compute the analytic bound on |q1 - q_inc| using the formula |Δq| ≤ ξ_AF^{-1} √(c2(N))/8 and the equilibrium q1 from the minimization. Express the result in units of π and write the single float to bragg_shift_bound.txt.
- Output file: `/app/outputs/bragg_shift_bound.txt`
- Format: txt
- Contract: Single float value.
- Scoring: scored by hidden verifier

### Step 4: NMR internal field distribution
- Role: scored (load-bearing)
- Action: For the single‑q phase (order parameters from stage1), compute the dipolar field H_x at In(2b) sites on a representative spatial lattice, build the normalized histogram P(h), and output a two‑column CSV.
- Output file: `/app/outputs/nmr_distribution.csv`
- Format: csv
- Contract: Two columns: field_value (float), probability_density (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_analysis.csv`
- `/app/outputs/bragg_shift_bound.txt`
- `/app/outputs/nmr_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_analysis.csv
- path: `/app/outputs/phase_analysis.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase and order parameter ratio at T/T_N^0=0.5, ξAF q0=0. Reports the phase label and the ratio η2/η1.
- schema:
  - `type`: table
  - `required_columns`: `temperature_ratio`, `xiAF_q0`, `phase`, `eta2_eta1_ratio`
  - `units`:
    - `temperature_ratio`: dimensionless
    - `xiAF_q0`: dimensionless
    - `eta2_eta1_ratio`: dimensionless

### bragg_shift_bound.txt
- path: `/app/outputs/bragg_shift_bound.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Analytic bound on the Bragg peak shift |q1 - q_inc|, compared to the paper‑derived value with tolerance.
- schema:
  - `type`: text
  - `units`: units of π

### nmr_distribution.csv
- path: `/app/outputs/nmr_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: NMR internal field distribution P(h) for the single‑q phase.
- schema:
  - `type`: table
  - `required_columns`: `field_value`, `probability_density`
  - `units`:
    - `field_value`: arbitrary
    - `probability_density`: arbitrary

Notes: The process step (minimization) is required to compute the order parameters but is not scored. The scored artifacts are derived from the minimized state at T/T_N^0=0.5 and ξAF q0=0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_analysis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_ratio",
          "xiAF_q0",
          "phase",
          "eta2_eta1_ratio"
        ],
        "units": {
          "temperature_ratio": "dimensionless",
          "xiAF_q0": "dimensionless",
          "eta2_eta1_ratio": "dimensionless"
        }
      },
      "description": "Phase and order parameter ratio at T/T_N^0=0.5, ξAF q0=0. Reports the phase label and the ratio η2/η1."
    },
    {
      "file": "bragg_shift_bound.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "units of π"
      },
      "description": "Analytic bound on the Bragg peak shift |q1 - q_inc|, compared to the paper‑derived value with tolerance."
    },
    {
      "file": "nmr_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_value",
          "probability_density"
        ],
        "units": {
          "field_value": "arbitrary",
          "probability_density": "arbitrary"
        }
      },
      "description": "NMR internal field distribution P(h) for the single‑q phase."
    }
  ],
  "notes": "The process step (minimization) is required to compute the order parameters but is not scored. The scored artifacts are derived from the minimized state at T/T_N^0=0.5 and ξAF q0=0."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact. The verifier checks structural properties (e.g., phase label and order-parameter ratio are consistent with the single-q phase; the NMR distribution exhibits two well-separated peaks), and compares the reported Bragg shift bound to a hidden reference. Each stage contributes a weighted portion to a total reward between 0 and 1. Reporting a number is not sufficient; the artifacts must be produced by actually executing the workflow.
