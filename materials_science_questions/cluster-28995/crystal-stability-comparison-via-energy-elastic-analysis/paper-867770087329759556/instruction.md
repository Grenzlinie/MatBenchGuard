# Closed-form elastic constants of fcc argon from an environment-dependent overlap potential

## Problem background
Interatomic forces in solid argon at high pressures deviate significantly from any two-body, central-force model. A central diagnostic is the Cauchy violation, which is a measure of the many-body nature of interactions: it vanishes if the total energy is purely pairwise, yet experiments show a large deviation. Understanding and modelling this effect requires an environment-dependent interatomic potential that captures the quantum-mechanical origin of the overlap repulsion. The goal is to compute the pressure, Cauchy violation, bulk modulus, and cubic elastic constants of fcc argon as a function of lattice constant using an analytic environment-dependent potential that incorporates the necessary many-atom character.

## Approach
The repulsive energy between atoms i and j is modelled as Φ_{ij}(R_{ij};λ_i+λ_j) = exp(-λ_i) exp(-λ_j) V_R(R_{ij}), where λ_i = Σ_{k≠i} ρ(R_{ik}) is an environment-dependent contraction factor built from a pairwise function ρ(R). The pairwise functions V_R(R) and ρ(R) are chosen as:

V_R(R) = A (1 + a_1 R + a_2 R^2) exp(-μ_1 R - μ_2 R^2)
ρ(R) = g exp(-ν R)

with the following parameter set:
A = 2.10×10⁻¹⁵ J

a₁ = -0.5819 Å⁻¹

a₂ = 0.09309 Å⁻²

μ₁ = 3.000 Å⁻¹

μ₂ = -0.03996 Å⁻²

g = 80.0

ν = 3.60 Å⁻¹

For an fcc crystal one first generates the ideal lattice and computes, for each lattice constant, the lattice sums u, v, w, uˢ, vˢ, wˢ (energy densities that involve the potential and its first and second derivatives) and the environment parameters α₀, α₀ˢ, β₀, β₀ˢ (defined from derivatives of ρ weighted by lattice vectors). These quantities are then inserted into closed-form expressions to yield the pressure P (GPa), Cauchy violation δ (GPa), adiabatic bulk modulus B (GPa), and the cubic elastic constants C₁₁, C₁₂, C₄₄ (GPa). No external datasets are required; the entire computation follows from the fcc geometry and the parameterised potential.

## Reproduction target
Implement the environment-dependent potential described in the Approach, generate the fcc lattice, compute the necessary neighbour sums and environment parameters, and evaluate the analytic expressions for pressure P, Cauchy violation δ, bulk modulus B, and elastic constants C₁₁, C₁₂, C₄₄ over a range of lattice constants from 3.8 Å to 5.2 Å in steps of 0.1 Å. Write the results to `/app/outputs/step_01_elastic_properties.csv` as a comma-separated table with the columns: lattice_constant_A, pressure_GPa, delta_GPa, B_GPa, C11_GPa, C12_GPa, C44_GPa (one row per lattice constant).

## Assets
No external datasets or pre-trained models are required. The fcc crystal geometry, the analytic forms of V_R(R) and ρ(R), and the numerical parameters are all given in the Approach section. The implementation may rely on standard numerical Python libraries (e.g., NumPy, SciPy) for lattice sums and array operations.

## Workflow steps

### Step 1: Generate fcc lattice and compute neighbour sums and environment parameters
- Role: process
- Action: For each targeted lattice constant, construct the fcc lattice and compute the per-site auxiliary sums u, v, w, u^s, v^s, w^s, and the environment parameters α₀, α₀^s, β₀, β₀^s using the separable potential, the radial functions V_R(R) and ρ(R), and the parameters given in the paper’s Table 1.
- Evidence: none

### Step 2: Compute pressure, Cauchy violation, bulk modulus, and elastic constants
- Role: scored (load-bearing)
- Action: From the computed neighbour sums and environment parameters, evaluate the closed-form expressions for pressure P (GPa), Cauchy violation δ (GPa), adiabatic bulk modulus B (GPa), and cubic elastic constants C11, C12, C44 (GPa) at a range of fcc lattice constants (3.8 Å to 5.2 Å in steps of 0.1 Å). Write the results to step_01_elastic_properties.csv.
- Output file: `/app/outputs/step_01_elastic_properties.csv`
- Format: csv
- Contract: lattice_constant_A,pressure_GPa,delta_GPa,B_GPa,C11_GPa,C12_GPa,C44_GPa (one row per lattice constant, comma-separated values)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_elastic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_elastic_properties.csv
- path: `/app/outputs/step_01_elastic_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Elastic properties of fcc solid argon predicted by the environment-dependent model as a function of lattice constant.
- schema:
  - `type`: table
  - `required_columns`: `lattice_constant_A`, `pressure_GPa`, `delta_GPa`, `B_GPa`, `C11_GPa`, `C12_GPa`, `C44_GPa`
  - `units`:
    - `lattice_constant_A`: angstrom
    - `pressure_GPa`: GPa
    - `delta_GPa`: GPa
    - `B_GPa`: GPa
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C44_GPa`: GPa

Notes: The checker recomputes the expected P, δ, B, C11, C12, C44 for each row using the same analytic formulas and fitted parameters (Table 1) and compares them within tolerances. Additionally, a structural check verifies that δ is negative for all reported rows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_elastic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice_constant_A",
          "pressure_GPa",
          "delta_GPa",
          "B_GPa",
          "C11_GPa",
          "C12_GPa",
          "C44_GPa"
        ],
        "units": {
          "lattice_constant_A": "angstrom",
          "pressure_GPa": "GPa",
          "delta_GPa": "GPa",
          "B_GPa": "GPa",
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C44_GPa": "GPa"
        }
      },
      "description": "Elastic properties of fcc solid argon predicted by the environment-dependent model as a function of lattice constant."
    }
  ],
  "notes": "The checker recomputes the expected P, δ, B, C11, C12, C44 for each row using the same analytic formulas and fitted parameters (Table 1) and compares them within tolerances. Additionally, a structural check verifies that δ is negative for all reported rows."
}
```

## How you are scored
Your submitted CSV file will be evaluated by a hidden verifier. The verifier internally recomputes the expected pressure, Cauchy violation, bulk modulus, and elastic constants from the same analytic model using your reported lattice constants as input, and compares them to the values you provide. A higher score is awarded for closer agreement, with appropriate tolerances. The verifier also performs structural sanity checks on the computed quantities to ensure that the relations among elastic constants are physically consistent. The final reward is a weighted combination of these checks that reflects both numerical accuracy and physical soundness.
