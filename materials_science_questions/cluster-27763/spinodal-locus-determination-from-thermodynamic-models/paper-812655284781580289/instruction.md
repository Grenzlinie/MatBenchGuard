# Lattice Cluster Theory Spinodal Computation for a Polyolefin Blend

## Problem background
Binary polymer blends exhibit miscibility that depends on monomer architecture and the degree of short-chain branching. The lattice cluster theory (LCT) provides a compressible thermodynamic framework to compute phase stability limits (spinodals) and related properties. This task reproduces an LCT computation for a specific polyolefin blend to produce its spinodal curve, critical temperature, excess volume, effective interaction parameter, and a branching parameter, which together characterise the blend's miscibility.

## Approach
The LCT treates a binary polymer blend as a compressible lattice system with coordination number z = 6. A fraction of lattice sites are left empty (voids) to account for excess free volume. Each united-atom group occupies a single site; whole polymer chains are built by connecting these groups according to the monomer architectures. All united-atom groups interact with the same microscopic energy ε. The Helmholtz free energy per lattice site is expanded in 1/z and the dimensionless interaction energy ε/(k_B T), truncated at orders 1/z² and (ε/(k_B T))². The non-combinatorial part is a polynomial in the actual volume fractions φ₁ and φ₂ with coefficients that depend on chain architecture via combinatorial factors.

For the two polymer species, PEP and PP, the combinatorial coefficients are obtained from the chain backbone bond count N and the formulas:

**PEP**:
N₁ = (5N−1)/4,
N₂ = 3/2 (N−1),
N₃ = (3N−7)/2,
N⊥ = (N−1)/4,
N₁,₁ = (N−1)(25N−53)/32,
N₁,₂ = (15/8)N² − 9N + 89/8.

**PP**:
N₁ = (3/2)N,
N₂ = 2N−1,
N₃ = 2(N−2),
N⊥ = N/2,
N₁,₁ = (N−2)(9N−4)/8,
N₁,₂ = (N−2)(3N−5).

The site occupancy index M (the total number of sites per chain) equals N₁ + 1.

From the Helmholtz free energy, the Gibbs free energy G = F + P V is formed, and the pressure equation of state P = −∂F/∂V determines the equilibrium void fraction φ_v for given temperature, pressure, and nominal composition Φ₁. The spinodal condition ∂μ₁/∂Φ₁|_P,T = 0 defines the stability limit. Solving this condition on a grid of Φ₁ yields the spinodal curve T(Φ₁). The critical temperature T_c is the maximum of this curve. The relative excess volume and the effective SANS interaction parameter χ_eff are evaluated from their respective definitions (excess volume: ΔV/(V₁+V₂) using the void fractions of the blend and pure components; χ_eff from the zero-angle scattering function and chemical potential derivative). The branching parameter r is |N₂^(1)/M₁ − N₂^(2)/M₂|.

## Reproduction target
For the PEP/PP binary blend with site occupancy indices M₁ = M₂ = 4342, coordination number z = 6, microscopic interaction energy ε = 0.5 k_B T₀ (T₀ = 415.15 K), lattice cell volume v_cell = 2.5477³ Å³, and constant pressure P = 1 atm, perform the following using the LCT framework described above:
1. Compute the spinodal curve T(Φ₁) on a grid of nominal volume fractions Φ₁ ∈ [0.05, 0.95] (at least 10 evenly spaced points).
2. Extract the critical temperature T_c as the maximum of that curve.
3. Evaluate the relative excess volume V^e/(V₁+V₂) at Φ₁ = 0.5 and T = 500 K.
4. Evaluate the effective interaction parameter χ_eff at Φ₁ = 0.5 and T = 500 K.
5. Compute the branching parameter r = |N₂^(1)/M₁ − N₂^(2)/M₂|.
Write all results to a JSON file named results.json.

## Assets

- Python scientific computing stack (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Compute LCT combinatorial factors for PEP and PP
- Role: process
- Action: Using the formulas from Table 3 of the paper (provided in the instruction) and the site occupancy index M=4342, determine the backbone bond number N and compute the combinatorial coefficients N₁, N₂, N₃, N⊥, N₁,₁, N₁,₂ for both PEP and PP united-atom chain architectures. Save the computed coefficients to a file for later use.
- Evidence: `/app/outputs/combinatorial_factors.json`

### Step 2: Implement LCT free energy, equation of state, and spinodal solver
- Role: process
- Action: Implement the LCT Helmholtz free energy truncated to orders 1/z² and (ε/k_BT)², the pressure equation of state (determine equilibrium void fraction φ_v), the spinodal condition ∂μ₁/∂Φ₁|_P,T=0, the excess volume formula, and the effective interaction parameter χ_eff formula. Use the combinatorial coefficients from step_01 and the fixed parameter values z=6, ε=0.5 k_B T₀, T₀=415.15 K, v_cell=2.5477³ Å³, P=1 atm.
- Evidence: `/app/outputs/lct_solver.py`

### Step 3: Compute spinodal curve, critical temperature, excess volume, χ_eff, and branching parameter
- Role: scored (load-bearing)
- Action: For the PEP/PP binary blend with M₁=M₂=4342, solve the spinodal condition on a grid of nominal volume fractions Φ₁ from 0.05 to 0.95 to obtain the spinodal curve T(Φ₁). Extract the critical temperature T_c as the maximum temperature on the curve. Evaluate the relative excess volume V^e/(V₁+V₂) and the effective interaction parameter χ_eff at Φ₁=0.5 and T=500 K. Compute the branching parameter r = |N₂^(1)/M₁ - N₂^(2)/M₂|. Format all results as a JSON object and write to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"blend": "PEP/PP", "M": 4342, "compositions": [array of floats], "spinodal_temperatures_K": [array of floats], "Tc_K": float, "excess_volume_at_phi05": float, "chi_eff_at_phi05": float, "branching_parameter_r": float}
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
- target_policy: structural_audit
- description: Scored artifact. The spinodal curve temperatures are checked for correct shape (UCST maximum near Φ₁=0.5, monotonic decrease toward edges); the scalars Tc, excess volume, chi_eff, and r are compared against hidden paper references with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `blend`: string
    - `M`: integer
    - `compositions`: array of floats
    - `spinodal_temperatures_K`: array of floats
    - `Tc_K`: float
    - `excess_volume_at_phi05`: float
    - `chi_eff_at_phi05`: float
    - `branching_parameter_r`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Tc_K`: Kelvin
    - `spinodal_temperatures_K`: Kelvin
    - `excess_volume_at_phi05`: dimensionless
    - `chi_eff_at_phi05`: dimensionless
    - `branching_parameter_r`: dimensionless

Notes: Scoring combines structural audit of the spinodal curve and exact-match-with-tolerance comparison of the scalars Tc, excess volume, chi_eff, and r. All values must be physically reasonable (e.g., positive temperatures).

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
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "blend": "string",
          "M": "integer",
          "compositions": "array of floats",
          "spinodal_temperatures_K": "array of floats",
          "Tc_K": "float",
          "excess_volume_at_phi05": "float",
          "chi_eff_at_phi05": "float",
          "branching_parameter_r": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Tc_K": "Kelvin",
          "spinodal_temperatures_K": "Kelvin",
          "excess_volume_at_phi05": "dimensionless",
          "chi_eff_at_phi05": "dimensionless",
          "branching_parameter_r": "dimensionless"
        }
      },
      "description": "Scored artifact. The spinodal curve temperatures are checked for correct shape (UCST maximum near Φ₁=0.5, monotonic decrease toward edges); the scalars Tc, excess volume, chi_eff, and r are compared against hidden paper references with tolerances."
    }
  ],
  "notes": "Scoring combines structural audit of the spinodal curve and exact-match-with-tolerance comparison of the scalars Tc, excess volume, chi_eff, and r. All values must be physically reasonable (e.g., positive temperatures)."
}
```

## How you are scored
A hidden verifier inspects your results.json. The spinodal temperatures are audited for correct shape: the curve must have a maximum near Φ₁ = 0.5 and decrease monotonically toward both composition extremes (upper-critical-solution-temperature, UCST, behaviour). The critical temperature Tc, excess volume, χ_eff, and branching parameter r are compared to hidden reference values within appropriate tolerances. A faithful implementation of the LCT equations will satisfy these checks; supplying plausible numbers without a correct computation will fail the structural tests. Each quantity contributes to a weighted score; the total reward is a combination of these weighted checks.
