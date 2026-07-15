# DFT Calculation and Superconducting Parameter Derivation for KBi2

## Problem background
KBi2 is a binary intermetallic compound that crystallizes in the MgCu2-type Laves phase (space group Fd-3m) and becomes superconducting at low temperatures. Determining whether KBi2 belongs to the type-I or type-II class of superconductors, and understanding its microscopic superconducting properties, requires a combination of electronic-structure calculations and thermodynamic/transport data. In particular, the effective mass, penetration depths, coherence lengths, and Ginzburg-Landau (GL) parameter κ_GL must be derived from first-principles density functional theory (DFT) and experimental constants. The key open task is to perform an independent DFT calculation to obtain the carrier density n and Fermi wave vector k_F, and then, using published experimental inputs (specific-heat coefficient γ=1.3 mJ mol⁻¹ K⁻², residual resistivity ρ₀=5.76 μΩ cm, and T_c=3.573 K), compute the derived superconducting parameters and evaluate whether they satisfy the criteria for type-I superconductivity in the dirty limit.

## Approach
The approach is two-stage, combining a DFT electronic-structure calculation with analytic post-processing. In the first stage, the crystal structure of KBi2 (experimental lattice constant a = 0.95233 nm, atoms at the 8a and 16d sites of Fd-3m) is used as input to a DFT code. A Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional with spin-orbit coupling is employed to compute the total electronic density of states at the Fermi level. From the DOS, the free-electron model yields the carrier density n and the Fermi wave vector k_F. In the second stage, these two quantities are combined with the measured specific-heat coefficient γ, residual resistivity ρ₀, and superconducting transition temperature T_c to evaluate, using the standard formulas of Orlando et al. (1979), the effective mass m*, London penetration depth λ_L(0), electronic mean free path l_tr, BCS coherence length ξ(0), dirty-limit GL coherence length ξ_GL(0), GL penetration depth λ_GL(0), and the GL parameter κ_GL. The question to be answered computationally is whether the resulting κ_GL lies below the critical value 1/√2 and whether the ratio l_tr/ξ(0) is much less than unity, as expected for a type-I dirty-limit superconductor.

## Reproduction target
Produce a JSON file (derived_quantities.json) containing the following quantities, all expressed in the specified units:
- m_star: effective mass in units of free-electron mass m_e
- lambda_L_0: London penetration depth in nm
- l_tr: electronic mean free path in nm
- xi_0: BCS coherence length in nm
- xi_GL_0: dirty-limit GL coherence length in nm
- lambda_GL_0: GL penetration depth in nm
- kappa_GL: GL parameter (dimensionless).
The target is to compute these values using an independent DFT run and the given experimental constants, and to assess whether the computed κ_GL is less than 1/√2 (criterion for type-I) and whether l_tr is much smaller than ξ(0) (criterion for the dirty limit).

## Assets

- DFT software (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- KBi2 crystal structure

## Workflow steps

### Step 1: DFT calculation of KBi2 electronic structure
- Role: process
- Action: Perform first-principles density functional theory (DFT) calculation for KBi2 using the experimental crystal structure (space group Fd-3m, a=0.95233 nm, K at 8a (1/8,1/8,1/8), Bi at 16d (1/2,1/2,1/2)). Use the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional with spin-orbit coupling. Compute the total electronic density of states (DOS) at the Fermi level. From the DOS, derive the carrier density n and Fermi wave vector k_F using the free-electron model. Save n and k_F to dft_intermediate.json.
- Evidence: `/app/outputs/dft_intermediate.json`

### Step 2: Compute superconducting parameters
- Role: scored (load-bearing)
- Action: Using the carrier density n and Fermi wave vector k_F from dft_intermediate.json and the following experimental constants: specific heat coefficient γ = 1.3 mJ mol^{-1} K^{-2}, residual resistivity ρ₀ = 5.76 μΩ cm, and superconducting transition temperature T_c = 3.573 K, compute the derived quantities using the formulas from Orlando et al. (Phys. Rev. B 19, 4545, 1979). Compute: effective mass m* (in units of free-electron mass m_e), London penetration depth λ_L(0) (nm), mean free path l_tr (nm), BCS coherence length ξ(0) (nm), dirty-limit GL coherence length ξ_GL(0) (nm), GL penetration depth λ_GL(0) (nm), and GL parameter κ_GL. Write the results to /app/outputs/derived_quantities.json.
- Output file: `/app/outputs/derived_quantities.json`
- Format: json
- Contract: {"type":"object","required":["m_star","lambda_L_0","l_tr","xi_0","xi_GL_0","lambda_GL_0","kappa_GL"],"properties":{"m_star":{"type":"number","unit":"m_e"},"lambda_L_0":{"type":"number","unit":"nm"},"l_tr":{"type":"number","unit":"nm"},"xi_0":{"type":"number","unit":"nm"},"xi_GL_0":{"type":"number","unit":"nm"},"lambda_GL_0":{"type":"number","unit":"nm"},"kappa_GL":{"type":"number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/derived_quantities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### derived_quantities.json
- path: `/app/outputs/derived_quantities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Derived superconducting parameters for KBi2.
- schema:
  - `type`: object
  - `required`: `m_star`, `lambda_L_0`, `l_tr`, `xi_0`, `xi_GL_0`, `lambda_GL_0`, `kappa_GL`
  - `properties`:
    - `m_star`:
      - `type`: number
      - `unit`: m_e
    - `lambda_L_0`:
      - `type`: number
      - `unit`: nm
    - `l_tr`:
      - `type`: number
      - `unit`: nm
    - `xi_0`:
      - `type`: number
      - `unit`: nm
    - `xi_GL_0`:
      - `type`: number
      - `unit`: nm
    - `lambda_GL_0`:
      - `type`: number
      - `unit`: nm
    - `kappa_GL`:
      - `type`: number

Notes: The hidden checker compares the agent-computed values to the paper's reported quantities with tolerances (~15% for DFT-derived values, ~10% for algebraically computed values) and checks structural conditions (kappa_GL < 1/sqrt(2), l_tr/xi(0) << 1). The agent must not guess; the DFT run produces the necessary inputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "derived_quantities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "m_star",
          "lambda_L_0",
          "l_tr",
          "xi_0",
          "xi_GL_0",
          "lambda_GL_0",
          "kappa_GL"
        ],
        "properties": {
          "m_star": {
            "type": "number",
            "unit": "m_e"
          },
          "lambda_L_0": {
            "type": "number",
            "unit": "nm"
          },
          "l_tr": {
            "type": "number",
            "unit": "nm"
          },
          "xi_0": {
            "type": "number",
            "unit": "nm"
          },
          "xi_GL_0": {
            "type": "number",
            "unit": "nm"
          },
          "lambda_GL_0": {
            "type": "number",
            "unit": "nm"
          },
          "kappa_GL": {
            "type": "number"
          }
        }
      },
      "description": "Derived superconducting parameters for KBi2."
    }
  ],
  "notes": "The hidden checker compares the agent-computed values to the paper's reported quantities with tolerances (~15% for DFT-derived values, ~10% for algebraically computed values) and checks structural conditions (kappa_GL < 1/sqrt(2), l_tr/xi(0) << 1). The agent must not guess; the DFT run produces the necessary inputs."
}
```

## How you are scored
A hidden verifier reads your derived_quantities.json and compares each reported quantity against reference values using pre-set tolerances. In addition, the verifier checks that the computed GL parameter satisfies the type-I condition (κ_GL < 1/√2) and that the dirty-limit condition (l_tr/ξ(0) is small). The verifier then combines these comparisons into an overall reward between 0 and 1. Reporting the paper’s published numbers without performing the required DFT calculation will not succeed, because the tolerances and structural checks require physically consistent intermediate quantities (n and k_F) that can only be obtained from a genuine electronic-structure computation. No gold values or tolerances are provided in this instruction.
