# Semiempirical Determination of Static Effective Charges and Short-Range Potentials for Cubic Perovskites from Elastic Moduli

## Problem background
Perovskite ABO3 crystals such as SrTiO3 and BaTiO3 exhibit mixed ionic-covalent bonding, and their macroscopic elastic properties (c11, c12) in the cubic paraelectric phase are intimately linked to the effective charges on the ions and the short-range repulsive forces between them. Determining these microscopic parameters—static effective charges, Born-Mayer repulsive potentials, and the effective Madelung constant—from the measured elastic moduli yields insight into the ionicity of the bonds and the stiffness of the cation-oxygen interactions, which in turn govern ferroelectric instability. The challenge is to solve the coupled nonlinear system that connects the known lattice constants and elastic constants to the unknown charges and force constants, under the constraints of electroneutrality and mechanical equilibrium.

## Approach
The total potential energy of one ABO3 unit cell is expressed as the sum of an effective Madelung (Coulomb) term and a short-range repulsive part. The Coulomb energy is written with an effective Madelung constant α_M* = s·α_M, where α_M is the ideal constant and s is a mean ionicity. The short-range interactions between the nearest A–O, B–O, and O–O pairs are modeled by Born-Mayer potentials U_ij = b_ij exp(−r/ρ), using a common hardness ρ for all interactions. The A–O and O–O parameters (ρ and the sum b1+b3) are taken from the experimentally determined values for the corresponding binary AO crystals (NaCl structure). This leaves b2 (the B–O repulsion), the three effective charges Z1, Z2, Z3, and α_M* as unknowns. The system is closed by four relations: (i) electroneutrality Z1+Z2+3Z3=0; (ii) the equilibrium condition, i.e., the derivative of the cell energy with respect to the lattice constant set to zero at the experimental lattice parameter; (iii) the Cowley relations that link the elastic stiffnesses c11 and c12 to the effective charges and to the short-range force constants derived from the second derivatives of the Born-Mayer potentials. Solving these equations numerically yields the complete parameter set. For BaTiO3, the ρ value from BaO alone does not reproduce the literature sum b1+b3; an averaging over two nearby ρ values is performed, as in the original treatment. Once the parameters are found, the dimensionless Kellermann force constants A_i, B_i (i=1,2,3) are computed from the second derivatives of the repulsive potentials, and the quasielastic constants k1 and k2 for the A and B cations are obtained from approximate expressions involving the lattice constant, ρ, and the b parameters.

## Reproduction target
Compute the full set of quantities for both SrTiO3 and BaTiO3 using the given experimental inputs: lattice constants (a=3.905 Å for SrTiO3, a=4.01 Å for BaTiO3), elastic moduli (c11=317.6 GPa, c12=102.5 GPa for SrTiO3; c11=173 GPa, c12=82 GPa for BaTiO3), and the binary-oxide Born-Mayer parameters.
For SrO: ρ=0.270 Å, b1=8.66×10⁻¹⁶ J, b3=2.08×10⁻¹⁶ J (so b1+b3=10.74×10⁻¹⁶ J).
For BaO: ρ=0.298 Å, b1=4.68×10⁻¹⁶ J, b3=2.02×10⁻¹⁶ J (so b1+b3=6.70×10⁻¹⁶ J; the literature sum is 7.275×10⁻¹⁶ J but the paper uses the BaO parameters as these individual values).
The ideal Madelung constant α_M for the perovskite structure is taken as 35.833 for SrTiO3 and 30.0 for BaTiO3 (these are the values used in the paper to compute the mean ionicity s=α_M*/α_M).

For SrTiO3, use the SrO parameters directly (b1 and b3 are fixed from SrO). Solve the system to determine the effective charges Z1/e, Z2/e, Z3/e, the effective Madelung constant α_M*, the Born-Mayer parameter b2, and the unit-cell energy W. From these compute the mean ionicity s=α_M*/α_M, the dimensionless Kellermann force constants A1, B1, A2, B2, A3, B3, and the quasielastic constants k1, k2.

For BaTiO3, apply an averaging procedure because using ρ=0.298 Å directly does not reproduce the literature sum. Perform the calculation twice:
1) With ρ=0.298 Å, using the BaO parameters b1=4.68×10⁻¹⁶ J, b3=2.02×10⁻¹⁶ J, and fixing Z1/e=2. Solve for Z2, Z3, α_M*, b2, W.
2) With ρ=0.294 Å, using the same BaO parameters b1=4.68×10⁻¹⁶ J, b3=2.02×10⁻¹⁶ J, and Z1/e=2. Solve for the same unknowns.
Then take the arithmetic mean of the obtained Z2, Z3, α_M*, b2, and W to obtain the final BaTiO3 parameters. (b1 and b3 remain unchanged as 4.68 and 2.02.) From these averaged quantities compute s, the force constants A_i, B_i, and the quasielastic constants k1, k2.

Write all results into /app/outputs/results.json exactly adhering to the schema described in the Output contract section.

## Assets

- Python scientific computing libraries: numpy scipy

## Workflow steps

### Step 1: Compute effective charges, potentials, force constants, and quasielastic constants for SrTiO3 and BaTiO3
- Role: scored (load-bearing)
- Action: Using the given experimental lattice constants and elastic moduli for SrTiO3 (a=3.905 Å, c11=317.6 GPa, c12=102.5 GPa) and BaTiO3 (a=4.01 Å, c11=173 GPa, c12=82 GPa), together with the binary-oxide Born-Mayer parameters specified in Reproduction target (individual b1, b3, and ρ for SrO and BaO; ideal Madelung constants α_M=35.833 for SrTiO3 and 30.0 for BaTiO3; for BaTiO3 perform the averaging over ρ=0.298 Å and ρ=0.294 Å as described), implement the semiempirical scheme: set up the unit-cell energy expression, equilibrium derivative, electroneutrality constraint, and the Cowley relations linking elastic moduli to effective charges and short-range force constants. Solve the system to obtain the effective static charges Z1/e, Z2/e, Z3/e, effective Madelung constant α_M*, Born-Mayer parameters b1, b2, b3, unit-cell energy W, and the mean ionicity s. From these, compute the dimensionless Kellermann force constants A_i, B_i (i=1,2,3) and the quasielastic constants k1, k2. Write all quantities for both crystals into /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Top-level keys 'SrTiO3' and 'BaTiO3'. Each value is an object with keys: 'Z1', 'Z2', 'Z3', 'alpha_M_star', 's', 'b1', 'b2', 'b3', 'W', 'A1', 'B1', 'A2', 'B2', 'A3', 'B3', 'k1', 'k2'. All values are floating-point numbers. Units: charges in elementary charge e, b_i in 10^{-16} J, W in 10^{-16} J, k1 and k2 in J/m^2.
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
- target_policy: reference_match
- description: All computed physical quantities for SrTiO3 and BaTiO3. The checker will compare each value to the hidden paper-reported reference within tolerances and also verify electroneutrality and equilibrium conditions.
- schema:
  - `type`: object
  - `required`:
    - `SrTiO3`: object with keys Z1, Z2, Z3, alpha_M_star, s, b1, b2, b3, W, A1, B1, A2, B2, A3, B3, k1, k2
    - `BaTiO3`: object with same keys
  - `items`:
    - `Z1`: float (elementary charge e)
    - `Z2`: float (elementary charge e)
    - `Z3`: float (elementary charge e)
    - `alpha_M_star`: float (dimensionless)
    - `s`: float (mean ionicity, dimensionless)
    - `b1`: float (10^{-16} J)
    - `b2`: float (10^{-16} J)
    - `b3`: float (10^{-16} J)
    - `W`: float (10^{-16} J)
    - `A1`: float (dimensionless)
    - `B1`: float (dimensionless)
    - `A2`: float (dimensionless)
    - `B2`: float (dimensionless)
    - `A3`: float (dimensionless)
    - `B3`: float (dimensionless)
    - `k1`: float (J/m^2)
    - `k2`: float (J/m^2)

Notes: The hidden checker also validates that the submitted values satisfy Z1+Z2+3Z3=0 and the equilibrium condition within reasonable tolerance, ensuring structural consistency without exposing gold values.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "SrTiO3": "object with keys Z1, Z2, Z3, alpha_M_star, s, b1, b2, b3, W, A1, B1, A2, B2, A3, B3, k1, k2",
          "BaTiO3": "object with same keys"
        },
        "items": {
          "Z1": "float (elementary charge e)",
          "Z2": "float (elementary charge e)",
          "Z3": "float (elementary charge e)",
          "alpha_M_star": "float (dimensionless)",
          "s": "float (mean ionicity, dimensionless)",
          "b1": "float (10^{-16} J)",
          "b2": "float (10^{-16} J)",
          "b3": "float (10^{-16} J)",
          "W": "float (10^{-16} J)",
          "A1": "float (dimensionless)",
          "B1": "float (dimensionless)",
          "A2": "float (dimensionless)",
          "B2": "float (dimensionless)",
          "A3": "float (dimensionless)",
          "B3": "float (dimensionless)",
          "k1": "float (J/m^2)",
          "k2": "float (J/m^2)"
        }
      },
      "description": "All computed physical quantities for SrTiO3 and BaTiO3. The checker will compare each value to the hidden paper-reported reference within tolerances and also verify electroneutrality and equilibrium conditions."
    }
  ],
  "notes": "The hidden checker also validates that the submitted values satisfy Z1+Z2+3Z3=0 and the equilibrium condition within reasonable tolerance, ensuring structural consistency without exposing gold values."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/results.json and compare each quantitative entry against a reference set of correct values obtained from the same scheme. In addition, it checks that the submitted charges satisfy electroneutrality and that the equilibrium condition is met within a tolerance. Your final reward is proportional to the number of quantities that fall within the verifier's acceptable ranges, combined into a single score between 0 and 1. Merely reporting numbers without executing the computation will not pass, because some checks involve internal consistency that only a correct solution can provide.
