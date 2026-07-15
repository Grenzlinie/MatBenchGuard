# Anisotropic Debye temperatures, compressibilities, and Grüneisen constants from crystal structure data

## Problem background
MnSb₂O₄ is a tetragonal antimonite that exhibits anisotropic thermal expansion and magnetostrictive effects below its Néel temperature. Understanding its anisotropic thermoelastic properties – Debye temperatures, compressibilities, elastic constants, and Grüneisen constants – is essential for modeling the vibrational anisotropy and anharmonicity of the crystal and for interpreting the interplay between lattice vibrations and magnetic order. These quantities can be determined from low‑temperature neutron diffraction data and a macroscopic Debye–Grüneisen model, providing a route to characterize the elastic and anharmonic behaviour without requiring single‑crystal measurements.

## Approach
The approach uses a macroscopic Debye model and Grüneisen relations, applied separately along the basal plane (direction a) and the c‑axis. Average atomic displacement parameters from neutron diffraction at two temperatures (2 K and 300 K) are converted into anisotropic Debye temperatures via the mean‑squared‑displacement formula of the Debye model. From these Debye temperatures, anisotropic force constants are obtained. A structural model then relates force constants, lattice parameters, and the number of effective bonds in each crystallographic direction to yield anisotropic compressibilities. Experimental thermal expansion data at 200 K and 250 K together with the computed specific heats (from the Debye model) give the mean Grüneisen parameter via the thermodynamic definition. Finally, a system of equations that couples thermal expansion, compressibilities, specific heats, and the mean Grüneisen parameter is solved to extract the elastic compliance factors and the two anisotropic Grüneisen constants. The entire calculation is a self‑contained pipeline that uses only the published crystallographic parameters and thermal expansion coefficients supplied in the instruction.

## Reproduction target
Reproduce the following quantities for MnSb₂O₄:

- Anisotropic Debye temperatures Θₐ (basal plane) and Θ꜀ (c‑axis), in K.
- Anisotropic compressibility coefficients χₐ and χ꜀, in Pa⁻¹.
- Elastic compliance factors Sₐ = s₁₁ + s₁₂, Sₐ꜀ = s₁₃, and S꜀ = s₃₃, in Pa⁻¹.
- Anisotropic Grüneisen constants γₐ and γ꜀, dimensionless.

## Input constants
All numeric constants needed for the computation are listed here. The anisotropic specific heats are computed from the Debye temperatures by the solver (Step 4) – they are not input. The following values must be used as given:

### Lattice parameters (300 K)
a = 8.7145 Å
c = 6.0011 Å
V = 455.74 Å³

### Average anisotropic displacement parameters (in Å²)
At 2 K: ⟨B₁₁⟩ = 0.487, ⟨B₃₃⟩ = 0.184
At 300 K: ⟨B₁₁⟩ = 1.089, ⟨B₃₃⟩ = 0.800

### Experimental thermal expansion coefficients (K⁻¹)
αₐ(200 K) = 7.21 × 10⁻⁶
αₐ(250 K) = 7.57 × 10⁻⁶
α꜀(200 K) = 6.32 × 10⁻⁶
α꜀(250 K) = 6.37 × 10⁻⁶

### Other constants
- Reduced molar mass M* = 24.595 g
- (Cv)∞ = 25 J mol⁻¹ K⁻¹   (high‑temperature limit of the molar specific heat)
- Structural indices: N₁ = 3.486, N₃ = 2.828, N_{l,a} = 20, N_{l,c} = 32

The six‑step workflow converts these data into the nine final numbers; the final step writes them to a JSON artifact.

## Assets

- Python

## Workflow steps

### Step 1: Compute anisotropic Debye temperatures
- Role: process
- Action: Using the average displacement parameters ⟨B11⟩ and ⟨B33⟩ at 2 K and 300 K together with the reduced molar mass M*, calculate the anisotropic Debye temperatures Θ_a (basal plane) and Θ_c (c‑axis) via the Debye model relation that connects mean‑squared displacements to the Debye temperature.
- Evidence: `/app/outputs/debye_temperatures.json`

### Step 2: Compute anisotropic force constants
- Role: process
- Action: From Θ_a and Θ_c, compute the average force constants F_a and F_c using the relationship F = 5.9×10⁻⁷ × M*(g) × (Cv)∞ × Θ² (the macroscopic Debye‑model expression for the force constant).
- Evidence: `/app/outputs/force_constants.json`

### Step 3: Compute anisotropic compressibilities
- Role: process
- Action: Using the lattice parameters a, c, cell volume V, the structural numbers N₁, N₃, N_{l,a}, N_{l,c}, and the force constants F_a, F_c, calculate the anisotropic compressibility coefficients χ_a and χ_c from the macroscopic model (χ relates force constants, cell dimensions, and structural indices).
- Evidence: `/app/outputs/compressibilities.json`

### Step 4: Compute Debye specific heat contributions
- Role: process
- Action: Evaluate the anisotropic specific heat functions 3C_a(T) and 3C_c(T) at the temperatures 200 K and 250 K using the Debye model and the previously obtained Θ_a, Θ_c.
- Evidence: `/app/outputs/specific_heats.json`

### Step 5: Compute mean Grüneisen parameter
- Role: process
- Action: Calculate the volume thermal expansion coefficient from the experimental α_a and α_c at 250 K, then determine the mean Grüneisen parameter γ̄ from the thermodynamic relation γ̄ = α_v V / (C_v χ̄) using the mean compressibility and the total specific heat.
- Evidence: `/app/outputs/mean_gruneisen.json`

### Step 6: Solve for elastic constants and anisotropic Grüneisen constants
- Role: scored (load-bearing)
- Action: Solve the system of equations that relate thermal expansion, compressibilities, specific heats, and the mean Grüneisen parameter to obtain the elastic compliance factors S_A (= s₁₁ + s₁₂), S_AC (= s₁₃), S_C (= s₃₃) and the anisotropic Grüneisen constants γ_a, γ_c. Store all final quantities in the output JSON.
- Output file: `/app/outputs/final_results.json`
- Format: json
- Contract: Object with keys: "Theta_a" (float, K), "Theta_c" (float, K), "chi_a" (float, Pa⁻¹), "chi_c" (float, Pa⁻¹), "S_A" (float, Pa⁻¹), "S_AC" (float, Pa⁻¹), "S_C" (float, Pa⁻¹), "gamma_a" (float, dimensionless), "gamma_c" (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_results.json
- path: `/app/outputs/final_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduced anisotropic thermoelastic quantities: Debye temperatures (Θ_a, Θ_c), compressibilities (χ_a, χ_c), elastic compliance factors (S_A, S_AC, S_C), and Grüneisen constants (γ_a, γ_c).
- schema:
  - `type`: object
  - `required`:
    - `Theta_a`: number (K)
    - `Theta_c`: number (K)
    - `chi_a`: number (Pa⁻¹)
    - `chi_c`: number (Pa⁻¹)
    - `S_A`: number (Pa⁻¹)
    - `S_AC`: number (Pa⁻¹)
    - `S_C`: number (Pa⁻¹)
    - `gamma_a`: number (dimensionless)
    - `gamma_c`: number (dimensionless)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Theta_a": "number (K)",
          "Theta_c": "number (K)",
          "chi_a": "number (Pa⁻¹)",
          "chi_c": "number (Pa⁻¹)",
          "S_A": "number (Pa⁻¹)",
          "S_AC": "number (Pa⁻¹)",
          "S_C": "number (Pa⁻¹)",
          "gamma_a": "number (dimensionless)",
          "gamma_c": "number (dimensionless)"
        }
      },
      "description": "Reproduced anisotropic thermoelastic quantities: Debye temperatures (Θ_a, Θ_c), compressibilities (χ_a, χ_c), elastic compliance factors (S_A, S_AC, S_C), and Grüneisen constants (γ_a, γ_c)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your output file `/app/outputs/final_results.json`, extracts each of the nine required quantities, and compares them to independently determined reference values. The comparison uses tolerances that account for the expected spread from a correct re‑implementation of the macroscopic model. A weighted score is computed as the fraction of quantities that fall within the acceptable range. Only the final JSON contributes to the reward; the intermediate process artifacts are required to be executed but are not directly scored. The verifier's reference values and tolerances are not disclosed, so you must compute each quantity faithfully through the pipeline described above.
