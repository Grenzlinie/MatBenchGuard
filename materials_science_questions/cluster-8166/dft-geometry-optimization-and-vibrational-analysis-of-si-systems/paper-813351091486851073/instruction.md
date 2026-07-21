# Total‑energy functional and effective charge in bond‑orbital model of SiO₂ and GeO₂

## Problem background
This task concerns the bond‑orbital model of 4:2-coordinated materials SiO₂ and GeO₂. The fundamental structural unit is a Si–O–Si chain with a variable bond angle at the oxygen. The electronic structure is described by a tight‑binding approach where bonding orbitals combine Si sp³ hybrids with oxygen p states. The total energy per bonding unit depends on the effective charge transferred to the oxygen and on the Si–O–Si angle. By minimizing the total energy with respect to the charge, one obtains the static effective oxygen charge Z₀* and the energy landscape that governs the equilibrium bond angle. This computation reproduces the key quantities that determine the observed Si–O–Si angle and the charge distribution.

## Approach
The bond‑orbital model constructs two superbond states |B_z⟩ and |B_x⟩ from the oxygen p_z and p_x orbitals, respectively, coupled to Si hybrids. The polarities β_{pz} and β_{px} are given by

β_{pz} = W₃ / √(2 W_{2z}² + W₃²), β_{px} = W₃ / √(2 W_{2x}² + W₃²),

where the effective coupling parameters depend on the half‑angle θ = (180°−φ)/2, the Si–O bond length d, and the fundamental parameters W₂, W₃, and overlap S:

W_{2z} = W₂ (1−2S²) / (1−2S² cos²θ) cosθ,
W_{2x} = W₂ (1−2S²) / (1−2S² sin²θ) sinθ.

The covalent energy E₂(z) is obtained by minimising the sum of the bond energies of B_z and B_x with respect to β_{pz} and β_{px} under the constraint β_{pz} + β_{px} = z, yielding

E₂(θ,z) = −2√2 W₂ [ √(1−β_{px}²) sinθ + √(1−β_{pz}²) cosθ ].

A Madelung constant A_M(θ) ≈ 3.1 − 1/(2 cosθ) accounts for the screened electrostatic interaction. The electrostatic term is derived by integrating the work to transfer charge z, starting from neutral atoms, with the bare electrostatic parameter A₀ taken equal to A_M at the equilibrium half‑angle θ₀. This simplifies the electrostatic contribution to

E_els(θ,z) = −2z W₃ + z² e² (1/cosθ − 1/cosθ₀) / (2d),

where W₃ is the polar energy (a given constant). The total energy per bonding unit (one oxygen plus its two Si neighbours) is

E_tot(θ,z) = E_els(θ,z) + E₂(θ,z).

The effective charge Z₀*(θ) is obtained by minimising E_tot with respect to z at each θ.

For SiO₂ use d = 1.61 Å, φ = 144° (θ₀ = 18°), S = 0.3, W₂ = 10.75 eV, W₃ = 4.35 eV.
For GeO₂ use d = 1.74 Å, φ = 130° (θ₀ = 25°), S = 0.3, W₂ = 9.13 eV, W₃ = 4.49 eV.

Vary θ from 0° to 50° to compute the energy landscape E_tot(θ, Z₀*(θ)). First determine the angle that minimises E_tot in the covalent‑electrostatic model (no Si–Si repulsion). Then add a short‑range Si–Si repulsion U(R) = U₀ (R₀/R)¹² with U₀ = 1.68 eV and R₀ = 3.06 Å, where R = 2d sinθ is the Si–Si distance, and find the new angle that minimises E_tot(θ, Z₀*(θ)) + U(R).

Finally, evaluate the derivative ∂Z₀*/∂θ for SiO₂ at the equilibrium angle θ₀ = 18° by numerical differentiation of the z‑minimising function.

## Reproduction target
Compute the static effective oxygen charge Z₀* for SiO₂ and GeO₂, the angle θ (in degrees) that minimises the total energy in the covalent‑electrostatic model (without Si–Si repulsion), the angle θ that minimises the total energy when the Si–Si repulsion is included, and the derivative ∂Z₀*/∂θ (per radian) for SiO₂ at the equilibrium angle. Write these five quantities as a single JSON object with keys Z0_SiO2, Z0_GeO2, angle_min_covalent_only, angle_min_with_repulsion, and dZ_dtheta_SiO2.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute bond‑orbital model results
- Role: scored (load-bearing)
- Action: Implement the bond‑orbital model for the Si–O–Si bonding unit using the provided parameters (structural: d, φ; model: S, W2, W3 for SiO₂ and GeO₂; extrapolation rules for GeO₂). Evaluate the polarities β_px, β_pz, the covalent energy E₂(z), the electrostatic term, and the Madelung constant A_M(θ). Construct the total energy per bonding unit E_tot(θ,z) and minimize with respect to effective charge z at each angle θ to obtain Z0*(θ). For SiO₂, compute Z0* and the total energy landscape vs θ (0°–50°) first without Si–Si repulsion and then including the short‑range repulsion U(R)=U₀(R₀/R)¹² (U₀=1.68 eV, R₀=3.06 Å), and record the angle minimum in each case. For GeO₂, compute Z0* and the derivative ∂Z*/∂θ for SiO₂ evaluated at the equilibrium angle. Write all results to the specified JSON file.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: {"Z0_SiO2": number, "Z0_GeO2": number, "angle_min_covalent_only": number (degrees), "angle_min_with_repulsion": number (degrees), "dZ_dtheta_SiO2": number (per radian)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: All reproduced quantities: static charge, angle minima, dielectric constants, dynamic effective charges.
- schema:
  - `type`: object
  - `required`:
    - `Z0_SiO2`: number
    - `Z0_GeO2`: number
    - `angle_min_covalent_only`: number
    - `angle_min_with_repulsion`: number
    - `dZ_dtheta_SiO2`: number
    - `alpha_quartz`: number
    - `beta_cristobalite`: number
    - `vitreous_silica`: number
    - `GeO2_quartzlike`: number
    - `e_x_SiO2`: number
    - `e_y_SiO2`: number
    - `e_z_SiO2`: number
    - `RoverPx_deriv_SiO2`: number
    - `e_x_GeO2`: number
    - `e_y_GeO2`: number
    - `e_z_GeO2`: number
    - `RoverPx_deriv_GeO2`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Z0_SiO2": "number",
          "Z0_GeO2": "number",
          "angle_min_covalent_only": "number",
          "angle_min_with_repulsion": "number",
          "dZ_dtheta_SiO2": "number",
          "alpha_quartz": "number",
          "beta_cristobalite": "number",
          "vitreous_silica": "number",
          "GeO2_quartzlike": "number",
          "e_x_SiO2": "number",
          "e_y_SiO2": "number",
          "e_z_SiO2": "number",
          "RoverPx_deriv_SiO2": "number",
          "e_x_GeO2": "number",
          "e_y_GeO2": "number",
          "e_z_GeO2": "number",
          "RoverPx_deriv_GeO2": "number"
        }
      },
      "description": "All reproduced quantities: static charge, angle minima, dielectric constants, dynamic effective charges."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects the single output file `step_01_results.json`. It checks that the file is valid JSON containing all five required fields with numerical values. Each field is compared to a hidden reference value within a tolerance; the verifier also confirms a structural trend that must hold between the two angle‑minimum quantities. The total reward is a weighted combination of these checks, written to the scoring logs.
