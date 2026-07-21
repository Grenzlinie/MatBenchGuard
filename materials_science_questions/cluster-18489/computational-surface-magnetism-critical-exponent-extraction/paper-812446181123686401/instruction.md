# Surface Phase Diagram Computation for a Spin-1 Monolayer on a Semi-infinite Spin-1/2 Ferromagnet

## Problem background
The system is a spin-1 Blume-Emery-Griffiths (BEG) monolayer on a semi-infinite spin-1/2 Ising ferromagnet. The surface layer has bilinear and biquadratic exchange interactions and a single-ion anisotropy. The goal is to compute the surface phase diagram and examine how the surface biquadratic interaction influences the width of the surface ferromagnetic phase region.

## Approach
Use effective-field theory (EFT) with a decoupling approximation to derive coupled equations for the surface magnetization, quadrupolar moment, and bulk-layer magnetizations. The second-order surface phase boundary is determined by the condition a=1, where a depends on the model parameters through the EFT equations. Numerically solve this condition to obtain the reduced surface transition temperature T_c^s / T_c^b as a function of the surface bilinear coupling Δ_s = (J_s / J) - 1, for fixed values of the surface biquadratic interaction J_s'/J, with single-ion anisotropy D_s = 0 and interlayer coupling J_1 = J. The bulk transition temperature T_c^b is first obtained from the bulk EFT equation and used to normalize all surface transition temperatures.

## Reproduction target
Compute the reduced surface transition temperature T_c^s / T_c^b as a function of Δ_s for each of the four values J_s'/J ∈ {2.0, 1.0, 0.0, -1.0}, with D_s = 0, J_1 = J, and Δ_s ranging from 0 to 2 in sufficiently fine steps to locate the critical Δ_s (where T_c^s = T_c^b) to within 0.01. Output the results as a CSV file with columns J_s_prime_over_J (float), delta_s (float), T_c_over_T_cb (float), sorted by J_s_prime_over_J then delta_s.

## Assets

- Python: python
- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute bulk transition temperature
- Role: process
- Action: Derive the bulk magnetization equation for the semi-infinite spin-1/2 Ising ferromagnet within the effective-field theory (EFT) and solve for the bulk transition temperature T_c^b. The obtained value in units of k_B T_c^b / J = 5.073 will be used to normalise all surface transition temperatures. Record the computed value in a process evidence artifact.
- Evidence: `/app/outputs/bulk_tc.json`

### Step 2: Compute surface phase boundaries
- Role: scored (load-bearing)
- Action: Implement the effective-field theory (EFT) equations for the spin-1 BEG monolayer on a semi-infinite spin-1/2 Ising ferromagnet, with parameters D_s=0, J_1=J, and J_s = J(1+Δ_s). For each value of the surface biquadratic coupling J_s'/J in {2.0, 1.0, 0.0, -1.0}, solve the second-order phase boundary condition numerically as a function of Δ_s (0 ≤ Δ_s ≤ 2) to obtain the reduced surface transition temperature T_c^s / T_c^b. Save the results to a CSV file with columns: J_s_prime_over_J, delta_s, T_c_over_T_cb. Ensure a sufficient density of Δ_s points so that the critical Δ_s at which T_c^s equals T_c^b can be located to within 0.01.
- Output file: `/app/outputs/phase_boundary_data.csv`
- Format: csv
- Contract: Columns: J_s_prime_over_J (float), delta_s (float), T_c_over_T_cb (float). Rows sorted by J_s_prime_over_J, then delta_s.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundary_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundary_data.csv
- path: `/app/outputs/phase_boundary_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase boundary curves of reduced surface transition temperature vs surface bilinear coupling for four values of the biquadratic interaction. The hidden verifier will perform structural checks on the curves, such as assessing monotonicity and comparing against hidden reference criteria. No expected numerical trends are disclosed.
- schema:
  - `type`: table
  - `required_columns`: `J_s_prime_over_J`, `delta_s`, `T_c_over_T_cb`
  - `units`:
    - `J_s_prime_over_J`: dimensionless
    - `delta_s`: dimensionless
    - `T_c_over_T_cb`: dimensionless

Notes: All other artifacts (bulk_tc.json) are process evidence and not scored. The task reproduces only the main result (Fig. 2) of the paper; tricritical and reentrant behaviours are omitted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundary_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "J_s_prime_over_J",
          "delta_s",
          "T_c_over_T_cb"
        ],
        "units": {
          "J_s_prime_over_J": "dimensionless",
          "delta_s": "dimensionless",
          "T_c_over_T_cb": "dimensionless"
        }
      },
      "description": "Phase boundary curves of reduced surface transition temperature vs surface bilinear coupling for four values of the biquadratic interaction. The hidden verifier will perform structural checks on the curves, such as assessing monotonicity and comparing against hidden reference criteria. No expected numerical trends are disclosed."
    }
  ],
  "notes": "All other artifacts (bulk_tc.json) are process evidence and not scored. The task reproduces only the main result (Fig. 2) of the paper; tricritical and reentrant behaviours are omitted."
}
```

## How you are scored
A hidden verifier will read your phase_boundary_data.csv and perform structural checks on the curves. For each J_s'/J value, it will determine the critical Δ_s at which T_c_over_T_cb ≈ 1.0 and will verify that T_c_over_T_cb increases monotonically with Δ_s. The exact tolerances and target relationships are hidden, but a correct re-implementation of the effective-field theory as described in the workflow steps will satisfy them. Your submission will receive a score between 0 and 1 based on how well the computed curves reproduce the expected structural properties.
