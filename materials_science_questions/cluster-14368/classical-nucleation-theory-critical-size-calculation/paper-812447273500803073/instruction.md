# Contact Angle Computation for Heterogeneous Nucleation via Atomistic-Capillarity Algorithm

## Problem background
During vapor deposition of metals onto crystalline substrates, the initial nuclei form isolated clusters on the surface. Understanding the contact angle that these clusters make with the substrate is crucial for predicting film morphology and growth mode. Classical capillarity theory relates the contact angle to the balance of interfacial energies, but when the critical nucleus consists of only a few atoms, bulk thermodynamic concepts must be reconciled with atomistic nucleation kinetics. This task asks you to implement a computational method that combines the atomistic single‑atom critical nucleus concept with the cap‑shaped cluster geometry of capillarity theory to compute the contact angle for a specific, well‑characterized material system.

## Approach
The algorithm works in two stages. First, steady‑state nucleation kinetics for the single‑atom critical nucleus are used to determine the critical adatom concentration on the substrate. The incident flux, substrate temperature, and energetic parameters (adsorption energy, diffusion barrier) enter an expression for the nucleation rate, from which the critical incidence rate and the critical adatom population are derived. Second, the equilibrium vapor pressure of the condensate material is used together with the gas‑kinetic formula to obtain the equilibrium adatom density, which then yields the supersaturation and the volume Gibbs free energy of condensation. The critical nucleus radius is taken as the atomic radius of the depositing element. From these quantities, the effective cluster‑vapor surface energy and the Gibbs free energy barrier for nucleation are computed, assuming a cap‑shaped nucleus with a currently unknown contact angle. Solving the geometric factor linking the barrier, the surface energy, and the volume free energy gives the contact angle. The entire chain is a deterministic algebraic derivation that requires only standard mathematical operations and the physical constants specified in the workflow.

## Reproduction target
Your goal is to execute the full algorithmic chain for the deposition of gold onto a vacuum‑cleaved NaCl substrate under the following fixed conditions: substrate temperature T = 150 °C (423.15 K), incident flux R = 1.4 × 10¹⁵ cm⁻² s⁻¹, with the material parameters Eₐ = 0.69 eV, E_d = 0.31 eV, N₀ = 4 × 10¹⁴ cm⁻², vibrational frequency ν = 1.1 × 10¹² s⁻¹, atomic radius r* = 1.4 Å, atomic volume Ω = 17.0 × 10⁻²⁴ cm³, substrate lattice parameter a₀ = 5.64 × 10⁻⁸ cm, and molecular mass M = 196.97 g mol⁻¹. Use the appropriate empirical vapor‑pressure constants for gold (C₁, C₂ when log P_c is in dyn cm⁻²) to compute the equilibrium vapor density. Implement the sequence described in the Approach, computing all intermediate quantities (R_crit, T_s, n_0star, n_c, supersaturation S, ΔG_v, γ_cv, ΔG*, and the geometric factor φ) and finally solve φ = (2 − cos θ + cos³ θ) / 4 for the contact angle θ in degrees. Write the complete set of results as a JSON object into /app/outputs/computed_values.json. The verifier will check the internal consistency of your intermediates and evaluate your reported contact angle against an undisclosed reference value for this system.

## Assets

- Python 3 standard environment: python3

## Workflow steps

### Step 1: Compute contact angle and intermediate quantities
- Role: scored (load-bearing)
- Action: Implement the algorithmic chain for the gold/NaCl deposition system using the specified physical parameters: incident flux R = 1.4e15 cm^-2 s^-1, substrate temperature T = 150°C, adsorption energy Ea = 0.69 eV, surface diffusion activation energy Ed = 0.31 eV, vibrational frequency v = 1.1e12 s^-1, substrate site density N0 = 4e14 cm^-2, atomic radius r* = 1.4 Å, atomic condensate volume Ω = 17.0e-24 cm^3, substrate lattice parameter a0 = 5.64e-8 cm, molecular mass M = 196.97 g/mol, and the standard empirical vapor‑pressure constants for gold. Compute the following quantities in sequence: critical incidence rate R_crit from the kinetic nucleation‑rate expression with I=1; mean stay time T_s and critical adatom concentration n_0star = R_crit * T_s; equilibrium vapor adatom density n_c using the empirical vapor pressure and gas‑kinetic formula; supersaturation S = n_0star / n_c; volume Gibbs free energy ΔG_v = - (k T / Ω) ln S; effective cluster‑vapor surface energy γ_cv = - r* ΔG_v / 2; Gibbs free energy barrier ΔG* from the capillarity nucleation‑rate expression with I=1, single‑atom radius, and n_1* = R * T_s; geometric factor φ from ΔG* and γ_cv; and finally the contact angle θ (in degrees) by solving φ = (2 - cos θ + cos³ θ) / 4. Write all computed values into /app/outputs/computed_values.json.
- Output file: `/app/outputs/computed_values.json`
- Format: json
- Contract: JSON object with numeric keys: R_crit (cm^-2 s^-1), T_s (s), n_0star (cm^-2), n_c (cm^-2), S (dimensionless), Delta_Gv (eV·cm^-3), r_star (cm), gamma_cv (eV·cm^-2), Delta_Gstar (eV), phi (dimensionless), theta (degrees).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_values.json
- path: `/app/outputs/computed_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the computed contact angle (theta) and all intermediate quantities for the gold deposition on NaCl system. The contact angle is the primary scored result, validated against a hidden reference value.
- schema:
  - `type`: object
  - `required`: `R_crit`, `T_s`, `n_0star`, `n_c`, `S`, `Delta_Gv`, `r_star`, `gamma_cv`, `Delta_Gstar`, `phi`, `theta`
  - `properties`:
    - `R_crit`:
      - `type`: number
      - `unit`: cm^-2 s^-1
    - `T_s`:
      - `type`: number
      - `unit`: s
    - `n_0star`:
      - `type`: number
      - `unit`: cm^-2
    - `n_c`:
      - `type`: number
      - `unit`: cm^-2
    - `S`:
      - `type`: number
      - `unit`: dimensionless
    - `Delta_Gv`:
      - `type`: number
      - `unit`: eV cm^-3
    - `r_star`:
      - `type`: number
      - `unit`: cm
    - `gamma_cv`:
      - `type`: number
      - `unit`: eV cm^-2
    - `Delta_Gstar`:
      - `type`: number
      - `unit`: eV
    - `phi`:
      - `type`: number
      - `unit`: dimensionless
    - `theta`:
      - `type`: number
      - `unit`: degrees

Notes: The hidden checker recomputes the contact angle from the reported intermediates to verify internal consistency, then compares the reported theta to the paper‑reported reference value within an absolute tolerance. Intermediate values ensure the pipeline was genuinely executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "R_crit",
          "T_s",
          "n_0star",
          "n_c",
          "S",
          "Delta_Gv",
          "r_star",
          "gamma_cv",
          "Delta_Gstar",
          "phi",
          "theta"
        ],
        "properties": {
          "R_crit": {
            "type": "number",
            "unit": "cm^-2 s^-1"
          },
          "T_s": {
            "type": "number",
            "unit": "s"
          },
          "n_0star": {
            "type": "number",
            "unit": "cm^-2"
          },
          "n_c": {
            "type": "number",
            "unit": "cm^-2"
          },
          "S": {
            "type": "number",
            "unit": "dimensionless"
          },
          "Delta_Gv": {
            "type": "number",
            "unit": "eV cm^-3"
          },
          "r_star": {
            "type": "number",
            "unit": "cm"
          },
          "gamma_cv": {
            "type": "number",
            "unit": "eV cm^-2"
          },
          "Delta_Gstar": {
            "type": "number",
            "unit": "eV"
          },
          "phi": {
            "type": "number",
            "unit": "dimensionless"
          },
          "theta": {
            "type": "number",
            "unit": "degrees"
          }
        }
      },
      "description": "JSON file containing the computed contact angle (theta) and all intermediate quantities for the gold deposition on NaCl system. The contact angle is the primary scored result, validated against a hidden reference value."
    }
  ],
  "notes": "The hidden checker recomputes the contact angle from the reported intermediates to verify internal consistency, then compares the reported theta to the paper‑reported reference value within an absolute tolerance. Intermediate values ensure the pipeline was genuinely executed."
}
```

## How you are scored
A hidden verifier reads your submitted computed_values.json. It first recomputes the contact angle from your reported intermediates (γ_cv, ΔG_v, ΔG*) using the geometric factor equation, verifying that the data is internally coherent. It then compares your reported θ to a hidden reference contact angle for the gold/NaCl system. The final reward is determined primarily by how close your θ is to that reference, with better (smaller) absolute deviations earning higher reward; extreme deviations receive zero. Internal consistency contributes a modest additional weight. Merely reporting the paper’s published numbers without genuinely executing the chain will not satisfy the verifier’s recomputation check.
