# 1-3 Piezoelectric Composite Electroelastic Homogenization

## Problem background
1‑3 piezoelectric composites — continuous piezoelectric fibers embedded in a piezoelectric or passive matrix — combine the high coupling of ceramics with the flexibility of polymers, making them attractive for sensors, actuators, and transducers. Accurate prediction of their full anisotropic electroelastic behavior is essential for composite design. An analytical model that captures the complete set of effective elastic, piezoelectric, and dielectric constants for such composites, without resorting to full finite‑element simulations, would provide a fast and insightful design tool. This task reproduces the core computation of that model for the case where both fiber and matrix are transversely isotropic and poled longitudinally.

## Approach
The analytical model is built on the assumptions of perfect bonding and a series‑parallel representation of the fiber–matrix microstructure. Longitudinal (along‑fiber) strains and electric fields are considered uniform in both phases, while transverse stresses and electric displacements are required to be continuous across the composite. By combining these compatibility and equilibrium conditions with the linear constitutive equations of each phase, closed‑form algebraic expressions for all 81 independent electroelastic moduli emerge. For the relevant transversely isotropic, longitudinally poled case these formulas reduce to a compact set of auxiliary coefficients and mixing rules. You will implement those expressions using the supplied constituent constants for BaTiO₃ (matrix) and PZT‑7A (fiber) and a fiber volume fraction of 0.5, outputting the resulting 9×9 matrix in the prescribed order.

## Reproduction target
Compute the full 9×9 electroelastic constitutive matrix for a longitudinal 1‑3 composite with BaTiO₃ matrix and PZT‑7A fiber at 50 % fiber volume fraction. The matrix maps the vector of composite strains and electric fields (ε₁,…,ε₆, E₁,E₂,E₃) to the vector of composite stresses and electric displacements (σ₁,…,σ₆, D₁,D₂,D₃). Use the provided constituent material constants and assemble the 81 entries in the standard order. Output the matrix as a CSV file at `/app/outputs/composite_matrix.csv`.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Constituent material constants

Both BaTiO₃ (matrix) and PZT‑7A (fiber) are transversely isotropic and poled in the longitudinal (3) direction. The required independent constants from the paper's Table 3 are:

| Constant | Symbol | BaTiO₃ (matrix) | PZT‑7A (fiber) | Units |
|----------|--------|-------------------|-----------------|
| Elastic stiffness | C₁₁ᴱ | 1.504e11 | 1.480e11 | Pa |
| Elastic stiffness | C₁₂ᴱ | 6.563e10 | 7.620e10 | Pa |
| Elastic stiffness | C₁₃ᴱ | 6.594e10 | 7.420e10 | Pa |
| Elastic stiffness | C₃₃ᴱ | 1.455e11 | 1.310e11 | Pa |
| Elastic stiffness | C₄₄ᴱ | 4.386e10 | 2.530e10 | Pa |
| Elastic stiffness | C₆₆ᴱ | 4.237e10 | 3.590e10 | Pa |
| Piezoelectric coupling | e₁₅ | 1.140e01 | 9.310e01 | C/m² |
| Piezoelectric coupling | e₃₁ | -4.322e00 | -2.324e00 | C/m² |
| Piezoelectric coupling | e₃₃ | 1.736e01 | 1.099e01 | C/m² |
| Dielectric permittivity | κ₁₁ᵋ | 1.280e-08 | 3.984e-09 | C/(V·m) |
| Dielectric permittivity | κ₃₃ᵋ | 1.510e-08 | 2.081e-09 | C/(V·m) |

All constants are given at constant electric field (E) or constant strain (ε) as indicated. The matrix and fiber densities are 5700 kg/m³ and 7700 kg/m³ respectively (used for acoustic impedance).

## Workflow steps

### Step 1: Compute composite electroelastic matrix
- Role: scored (load-bearing)
- Action: Implement the analytical homogenization model for a 1‑3 composite where both fiber and matrix are transversely isotropic and poled in the longitudinal direction. Use the series‑parallel mixing rules and the constituent constitutive relations to assemble the effective composite electroelastic matrix. The elastic, piezoelectric, and dielectric constants for BaTiO₃ matrix and PZT‑7A fiber are provided in the instruction. Compute for fiber volume fraction v_f = 0.5. Output the full 9×9 matrix that maps composite strains and electric fields to composite stresses and electric displacements.
- Output file: `/app/outputs/composite_matrix.csv`
- Format: csv
- Contract: 9 rows × 9 columns of floating‑point numbers, no header. Rows correspond to the output quantities in order: σ₁, σ₂, σ₃, σ₄, σ₅, σ₆, D₁, D₂, D₃. Columns correspond to the input quantities in order: ε₁, ε₂, ε₃, ε₄, ε₅, ε₆, E₁, E₂, E₃.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/composite_matrix.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### composite_matrix.csv
- path: `/app/outputs/composite_matrix.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Full 9×9 composite electroelastic constitutive matrix (C, –e, e, κ) as a dense float CSV.
- schema:
  - `type`: table
  - `note`: 9 rows of 9 float columns; row order σ₁–σ₆ then D₁–D₃; column order ε₁–ε₆ then E₁–E₃; no header.

Notes: The constituents are both transversely isotropic and poled longitudinally. Material constants are provided directly in the instruction; no external data retrieval is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "composite_matrix.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "note": "9 rows of 9 float columns; row order σ₁–σ₆ then D₁–D₃; column order ε₁–ε₆ then E₁–E₃; no header."
      },
      "description": "Full 9×9 composite electroelastic constitutive matrix (C, –e, e, κ) as a dense float CSV."
    }
  ],
  "notes": "The constituents are both transversely isotropic and poled longitudinally. Material constants are provided directly in the instruction; no external data retrieval is required."
}
```

## How you are scored
A hidden verifier reads your `composite_matrix.csv` and compares each of its 81 entries to a gold‑standard matrix for the same composite. The gold matrix is derived independently from the same analytical model and has been validated. Each entry is checked with an absolute tolerance; mismatched entries reduce the reward proportionally. The output format must conform exactly to the contract: 9 rows (ordered σ₁–σ₆, D₁–D₃) and 9 columns (ordered ε₁–ε₆, E₁–E₃) of plain floating‑point numbers, no header. The verifier does not recalculate the model, so achieving the correct values requires faithful implementation of the homogenisation formulas.
