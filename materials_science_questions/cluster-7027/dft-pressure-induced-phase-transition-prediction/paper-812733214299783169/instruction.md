# Pressure-induced B3→B1 phase transition prediction in ZnSeₓTe₁₋ₓ using an empirical potential

## Problem background
Semiconducting compounds ZnSe and ZnTe both crystallize in the zinc blende (B3) structure at ambient conditions and transform to a rock-salt (B1) structure under applied pressure. The alloys ZnSeₓTe₁₋ₓ exhibit composition‑dependent structural phase transitions and elastic behaviour that are important for device applications. Direct experimental measurement of these high‑pressure properties is challenging, so a predictive computational model is valuable. A phenomenological approach based on an effective interionic interaction potential (EIoIP) has been proposed to describe the pressure‑induced B3→B1 transition and the associated zero‑pressure elastic constants for the full alloy series. The model expresses the total crystal energy as a sum of long‑range Coulomb, short‑range overlap repulsion, and van der Waals interactions, and uses only a small number of material‑dependent parameters that are fitted from equilibrium properties of the end members. This task asks you to implement the EIoIP model and use it to compute the transition pressure, volume collapse, and elastic moduli for six compositions ranging from pure ZnTe to pure ZnSe.

## Approach
You will implement an effective interionic interaction potential (EIoIP) of the form
U(r) = Coulomb + overlap repulsion + van der Waals,
where the Coulomb part uses a modified ionic charge Zₘ, the overlap repulsion is of Hafemeister–Flygare type with a hardness parameter ρ and a range parameter b, and the van der Waals part includes dipole‑dipole and dipole‑quadrupole terms with provided coefficients cᵢⱼ and dᵢⱼ.
The model has three free parameters (Zₘ, b, ρ). For the end members ZnTe and ZnSe you will determine these parameters by imposing the equilibrium condition dU/dr = 0 at the experimental equilibrium nearest‑neighbour distance and matching the experimental bulk modulus through the second derivative d²U/dr². For alloy compositions ZnSeₓTe₁₋ₓ, interpolate Zₘ, b, ρ using Vegard’s law.

For each composition you will compute the internal energies U_B3(r) and U_B1(r') for the zinc blende (B3) and rock-salt (B1) structures, using the appropriate Madelung constants and the first‑ and second‑neighbour short‑range summations. The volume relations are V_B3 = 3.08 r³ and V_B1 = 2 r'³. At zero temperature the Gibbs free energy is the enthalpy H = U + PV. By minimising H with respect to the structural parameter (r or r') at a sequence of pressures, you obtain the pressure‑dependent Gibbs free energies G_B3(P) and G_B1(P). The transition pressure P_t is the pressure at which ΔG = G_B3 − G_B1 crosses zero. At P_t you extract the equilibrium volumes of the two phases and compute the relative volume collapse ΔV/V(0) in percent.

At zero pressure, for the B3 phase you will compute the second‑order elastic constants C₁₁, C₁₂, C₄₄ from the standard formulas that involve the first and second derivatives of the short‑range potentials at the equilibrium interionic distances. From these, derive the bulk modulus B_T = (C₁₁+2C₁₂)/3, the shear modulus C₄₄, and the tetragonal modulus C_s = (C₁₁−C₁₂)/2.

The model is fully specified by the provided crystal data (equilibrium distance, bulk modulus, ionic radii) and the tables of van der Waals coefficients. You are expected to implement the energy expressions, the fitting procedure, and the enthalpy minimisation from scratch using standard numerical tools.

## Reproduction target
You must produce a single JSON file `transition_and_elastic_properties.json` that contains the computed properties for the six ordered compositions: ZnTe, ZnSe₀.₂Te₀.₈, ZnSe₀.₅₅Te₀.₄₅, ZnSe₀.₈₁Te₀.₁₉, ZnSe₀.₉₃Te₀.₀₇, ZnSe. For each compound, report:
- P_t_GPa : the B3→B1 transition pressure in GPa,
- volume_collapse_percent : the relative volume drop ΔV/V(0) at the transition, in percent,
- B_T_GPa : the zero‑pressure bulk modulus in GPa,
- C44_GPa : the shear modulus C₄₄ in GPa,
- C_s_GPa : the tetragonal modulus (C₁₁−C₁₂)/2 in GPa.

## Assets

### Crystal data
| Composition | a (Å) | B_T (GPa) | r_i (Zn²⁺, Å) | r_j (anion, Å) |
|-------------|-------|-----------|---------------|----------------|
| ZnTe        | 6.089 | 52.80     | 0.74          | 1.83           |
| ZnSe        | 5.667 | 62.67     | 0.73          | 1.71           |

For alloy compositions ZnSeₓTe₁₋ₓ, the lattice constant and bulk modulus must be obtained from the end members using Vegard's law (linear interpolation in composition). The ionic radii for the mixed anion site are also interpolated linearly.

### Van der Waals coefficients (cᵢⱼ in 10⁻⁶⁰ erg·cm⁶, dᵢⱼ in 10⁻⁷⁶ erg·cm⁸)
| Composition       | c11 | c12   | c22   | C      | d11  | d12  | d22   | D     |
|-------------------|-----|-------|-------|--------|------|------|-------|-------|
| ZnTe              | 38.0| 149.1 |1087.3 |1078.1  |12.07 |197.0 |1812.4 |1100.3 |
| ZnSe0.2Te0.8      | 38.0| 141.8 | 976.6 |1004.4  |12.07 |180.6 |1590.0 | 997.5 |
| ZnSe0.55Te0.45    | 38.0| 129.1 | 782.9 | 875.26 |12.07 |152.0 |1201.8 | 817.4 |
| ZnSe0.81Te0.19    | 38.0| 119.7 | 639.1 | 779.34 |12.07 |130.7 | 913.1 | 683.9 |
| ZnSe0.93Te0.07    | 38.0| 115.3 | 572.7 | 735.06 |12.07 |120.9 | 779.9 | 622.3 |
| ZnSe              | 38.0| 112.8 | 533.9 | 709.24 |12.07 |115.2 | 702.2 | 586.3 |

Note: c11 = c(Zn,Zn) (same for all compositions), c12 = c(Zn,anion), c22 = c(anion,anion); C and D are overall vdW coefficients computed from the pair-wise cᵢⱼ and dᵢⱼ. You must use the pair-wise coefficients in the energy summation as in Eq. (1).

- Python numerical packages: numpy scipy

## Workflow steps

### Step 1: Fit interionic potential parameters
- Role: process
- Action: For ZnTe and ZnSe, use the provided equilibrium distance r0 and bulk modulus B_T to fit the three model parameters (modified ionic charge Z_m, hardness ρ, range b) by enforcing dU/dr=0 and matching B_T via d²U/dr². For ZnSe_xTe_{1-x} alloy compositions, interpolate Z_m, ρ, b using Vegard's law.
- Evidence: `/app/outputs/fitted_parameters.json`

### Step 2: Compute transition pressures and elastic constants
- Role: scored (load-bearing)
- Action: For each composition, using the fitted potential, minimize the enthalpy H = U + PV for B3 and B1 phases at varying pressure. Find the pressure P_t where ΔG = G_B3 − G_B1 = 0. Determine the equilibrium volumes at P_t to compute the relative volume collapse ΔV/V0. At zero pressure, compute the second-order elastic constants C11, C12, C44 for the B3 phase and derive B_T, C44, C_s. Write all results to 'transition_and_elastic_properties.json'.
- Output file: `/app/outputs/transition_and_elastic_properties.json`
- Format: json
- Contract: {"type": "object", "properties": {"compounds": {"type": "array", "items": {"type": "object", "properties": {"name": {"type": "string"}, "P_t_GPa": {"type": "number"}, "volume_collapse_percent": {"type": "number"}, "B_T_GPa": {"type": "number"}, "C44_GPa": {"type": "number"}, "C_s_GPa": {"type": "number"}}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_and_elastic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_and_elastic_properties.json
- path: `/app/outputs/transition_and_elastic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: the computed transition pressure (P_t in GPa), volume collapse (in %), zero-pressure bulk modulus B_T (GPa), shear modulus C44 (GPa), and tetragonal modulus C_s (GPa) for each of the six compositions, ordered from ZnTe to ZnSe. The checker compares against the paper's reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `compounds`
  - `properties`:
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `name`:
            - `type`: string
          - `P_t_GPa`:
            - `type`: number
          - `volume_collapse_percent`:
            - `type`: number
          - `B_T_GPa`:
            - `type`: number
          - `C44_GPa`:
            - `type`: number
          - `C_s_GPa`:
            - `type`: number

Notes: The hidden checker uses the paper's Table 3 and Table 4 values as the reference. Tolerances are not disclosed; the agent should produce a faithful re-implementation of the described model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_and_elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "compounds"
        ],
        "properties": {
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "P_t_GPa": {
                  "type": "number"
                },
                "volume_collapse_percent": {
                  "type": "number"
                },
                "B_T_GPa": {
                  "type": "number"
                },
                "C44_GPa": {
                  "type": "number"
                },
                "C_s_GPa": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Scored artifact: the computed transition pressure (P_t in GPa), volume collapse (in %), zero-pressure bulk modulus B_T (GPa), shear modulus C44 (GPa), and tetragonal modulus C_s (GPa) for each of the six compositions, ordered from ZnTe to ZnSe. The checker compares against the paper's reported values with appropriate tolerances."
    }
  ],
  "notes": "The hidden checker uses the paper's Table 3 and Table 4 values as the reference. Tolerances are not disclosed; the agent should produce a faithful re-implementation of the described model."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/transition_and_elastic_properties.json` and performs a compound‑wise metric‑pair comparison against independently established reference values. Each pair (P_t, volume collapse, B_T, C₄₄, C_s for each of the six compounds) is compared within tolerances that reflect the expected spread of independent re‑implementations. The reward is the fraction of individual compound‑metric pairs that meet the tolerance criteria. Your task is to faithfully implement the described EIoIP model and the physics‑based computation; reporting values that are inconsistent with a genuine model implementation will not receive full credit.
