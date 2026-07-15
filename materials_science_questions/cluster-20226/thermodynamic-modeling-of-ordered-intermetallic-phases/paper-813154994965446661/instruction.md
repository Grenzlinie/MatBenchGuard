# Thermodynamic Modeling of Directional Order and Anisotropy in fcc AB3 Alloys

## Problem background
Directional order induced by magnetic annealing in ferromagnetic face-centered cubic (fcc) binary solid solutions can coexist with an ordinary AB3-type superlattice, and the two types of order influence each other. This task addresses a statistico-thermodynamic model that uses the quasi-chemical method with tetrahedral quadruplet approximation to describe both the directional order and the long-range order. The model introduces anisotropic long-range order parameters and 64 quadruplet-count variables, derives the configurational entropy and internal energy, and obtains equilibrium conditions that determine the atomic arrangement under magnetic annealing. From the equilibrium order parameters, the induced uniaxial ferromagnetic anisotropy constants k1 and k2 are computed. Understanding how short-range and long-range order suppress the directional order and the associated anisotropy is of fundamental interest for magnetic materials such as Ni3Fe.

## Approach
The model is solved in two stages using a successive-approximation method. In the zeroth-order approximation, the ordinary AB3 superlattice (without directional order) is treated. This reduces the problem to solving the nonlinear quasi-chemical equations for the isotropic order parameters — a single long-range order parameter r and eight quadruplet occupation fractions a, b, c, d, e, f, g, h — at a given temperature and interaction energy V. These equations are numerically solved to yield the zeroth-order solutions. In the first-order approximation, directional order corrections are introduced. The equations are linearized around the zeroth-order solution for a specified magnetization direction β. The auxiliary coefficients that appear in the linearized expressions depend on the zeroth-order quadruplet fractions and are evaluated analytically. The first-order corrections for the order parameters are then computed, and from them the induced ferromagnetic anisotropy constants k1 and k2 are obtained using the expression that involves the magnetic interaction parameter L. The calculation is carried out for a fixed set of parameters: V = 1 (interaction energy), k = 1 (Boltzmann constant), L = 0.1 (magnetic interaction), and the magnetization direction along [100], i.e., β = (1, 0, 0). The critical temperature Tc for the order-disorder transition is Tc = 0.8224 V/k. The results are evaluated at two reduced temperatures, T = 0.9 Tc and T = 0.4 Tc, which span the ordered phase.

## Reproduction target
Compute the following quantities for an fcc AB3 alloy under magnetic annealing along [100], using the linearized quasi-chemical solution with V = 1, k = 1, L = 0.1, and Tc = 0.8224 V/k: (i) the induced anisotropy constants k1 and k2 obtained from the first-order corrections, and (ii) the long-range order parameter r from the zeroth-order superlattice solution. Report these results for the two specified temperatures (0.9 Tc and 0.4 Tc) in a single JSON file (results.json) with fields k1_highT, k2_highT, r_highT, k1_lowT, k2_lowT, r_lowT.

## Assets

- NumPy: numpy>=1.20
- SciPy: scipy>=1.7

## Workflow steps

### Step 1: Solve zeroth-order quasi-chemical equations for the AB3 superlattice
- Role: process
- Action: Solve the nonlinear quasi-chemical equations for the ordinary AB3 superlattice (zeroth-order approximation, analogous to McGlashan's theory) to obtain the long-range order parameter r and the 16 quadruplet occupation fractions a, b, c, d, e, f, g, h at the two target temperatures. Use the interaction energy V = 1 and Boltzmann constant k = 1. Compute the critical temperature Tc = 0.8224 V/k, then solve the equations for T = 0.9 * Tc and T = 0.4 * Tc. Record the solved parameters in a JSON evidence file.
- Evidence: `/app/outputs/zeroth_order_solution.json`

### Step 2: Compute directional order corrections and anisotropy constants
- Role: scored (load-bearing)
- Action: Using the zeroth-order solution from step s1, compute the auxiliary coefficients defined in the linearized solution method (first-order corrections). Evaluate the induced corrections for the magnetic field direction β = (1, 0, 0). Compute the induced anisotropy constants k1 and k2 from the expressions involving the zeroth-order quadruplet fractions and the magnetic interaction parameter L = 0.1, and report the long-range order parameter r for the two target temperatures: T = 0.9 * Tc and T = 0.4 * Tc. Write all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": ["k1_highT", "k2_highT", "r_highT", "k1_lowT", "k2_lowT", "r_lowT"], "properties": {"k1_highT": {"type": "number"}, "k2_highT": {"type": "number"}, "r_highT": {"type": "number"}, "k1_lowT": {"type": "number"}, "k2_lowT": {"type": "number"}, "r_lowT": {"type": "number"}}, "additionalProperties": false}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the computed induced anisotropy constants k1, k2 and the long-range order parameter r at the two specified reduced temperatures, computed from the linearized quasi-chemical solution with V=1, k=1, L=0.1, field direction [100].
- schema:
  - `type`: object
  - `required`: `k1_highT`, `k2_highT`, `r_highT`, `k1_lowT`, `k2_lowT`, `r_lowT`
  - `properties`:
    - `k1_highT`:
      - `type`: number
      - `description`: Induced anisotropy constant k1 at T=0.9*Tc
    - `k2_highT`:
      - `type`: number
      - `description`: Induced anisotropy constant k2 at T=0.9*Tc
    - `r_highT`:
      - `type`: number
      - `description`: Long-range order parameter r at T=0.9*Tc
    - `k1_lowT`:
      - `type`: number
      - `description`: Induced anisotropy constant k1 at T=0.4*Tc
    - `k2_lowT`:
      - `type`: number
      - `description`: Induced anisotropy constant k2 at T=0.4*Tc
    - `r_lowT`:
      - `type`: number
      - `description`: Long-range order parameter r at T=0.4*Tc
  - `additionalProperties`: False

Notes: The zeroth-order solution (process step) is required to compute the scored quantities; no paper-specific gold values or tolerances are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "k1_highT",
          "k2_highT",
          "r_highT",
          "k1_lowT",
          "k2_lowT",
          "r_lowT"
        ],
        "properties": {
          "k1_highT": {
            "type": "number",
            "description": "Induced anisotropy constant k1 at T=0.9*Tc"
          },
          "k2_highT": {
            "type": "number",
            "description": "Induced anisotropy constant k2 at T=0.9*Tc"
          },
          "r_highT": {
            "type": "number",
            "description": "Long-range order parameter r at T=0.9*Tc"
          },
          "k1_lowT": {
            "type": "number",
            "description": "Induced anisotropy constant k1 at T=0.4*Tc"
          },
          "k2_lowT": {
            "type": "number",
            "description": "Induced anisotropy constant k2 at T=0.4*Tc"
          },
          "r_lowT": {
            "type": "number",
            "description": "Long-range order parameter r at T=0.4*Tc"
          }
        },
        "additionalProperties": false
      },
      "description": "Contains the computed induced anisotropy constants k1, k2 and the long-range order parameter r at the two specified reduced temperatures, computed from the linearized quasi-chemical solution with V=1, k=1, L=0.1, field direction [100]."
    }
  ],
  "notes": "The zeroth-order solution (process step) is required to compute the scored quantities; no paper-specific gold values or tolerances are exposed."
}
```

## How you are scored
A hidden verifier will independently solve the same system of equations — the zeroth-order quasi-chemical equations and the first-order directional order corrections — using the identical parameter set and obtain reference values for k1, k2, and r at both temperatures. Your output in results.json will be compared to these reference values. Full credit is awarded when your computed numbers match the reference values within a tolerance; larger deviations reduce the score. The verifier’s reference values and exact tolerances are not revealed to you. No gold values are provided in this document.
