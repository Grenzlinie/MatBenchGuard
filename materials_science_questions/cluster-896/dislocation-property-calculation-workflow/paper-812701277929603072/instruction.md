# Solute-strengthening in fcc alloys using isotropic elasticity theory

## Problem background
In random fcc alloys, the motion of dislocations is impeded by their interactions with the compositional fluctuations inherent to the alloy, leading to solute strengthening. A recent theory models this process by considering an edge dislocation that spontaneously becomes wavy to lower its energy, with the balance between elastic line energy and solute potential energy determining the characteristic waviness amplitude and the energy barrier for motion. This framework predicts the temperature- and strain-rate-dependent flow stress in terms of fundamental solute / dislocation interaction energies and the dislocation line tension. The present task is to implement an isotropic elasticity model for solute strengthening, which approximates the full anisotropic results using Voigt-averaged elastic constants. The model is demonstrated on the equiatomic CoCrFeMnNi Cantor alloy, for which key strengthening quantities are computed from the model.

## Approach
The isotropic model describes the dislocation core as a dissociated edge dislocation with a bimodal Gaussian Burgers vector distribution parameterized by the partial separation d/b and the core width σ/b. The first stage is to construct the dimensionless energy-fluctuation function g^iso(w) from the core structure and to find the optimal dislocation waviness amplitude w_c that minimizes the total energy, which reduces to solving dg^iso/dw = g^iso/(2w). This yields the dimensionless coefficients w_c and g^iso(w_c). In the second stage, these core coefficients are combined with the material's elastic properties. The Voigt-averaged shear modulus and Poisson's ratio are obtained from the single-crystal elastic constants C11, C12, C44, while the line tension is computed from the shear modulus in the relevant slip system. Prefactors that scale with the solute misfit-volume combination and the elastic constants are then formed. From these, the zero-temperature energy barrier ΔE_b and zero-temperature yield stress τ_y0 are calculated. Finally, the temperature- and strain-rate-dependent tensile yield stress σ_y is obtained through the thermal-activation relation, using the given temperature, strain rate, and a Taylor factor.

## Reproduction target
Implement the complete isotropic solute-strengthening model for the Cantor alloy using the prescribed material parameters: C11=195.9 GPa, C12=117.7 GPa, C44=129.3 GPa; lattice constant a=3.6 Å (giving Burgers vector b = a/√2 ≈ 2.5456 Å); dislocation core parameters d/b=7 and σ/b=1.5; misfit-volume combination Σc_nΔV_n² = 0.43 Å⁶. First compute the dimensionless core coefficients w_c and g^iso(w_c) by energy minimization. Then compute the Voigt-averaged elastic moduli, the line tension Γ = (1/8)·μ_{111/110}·b² with μ_{111/110} = (C11−C12+C44)/3, and the relevant prefactors. From these, compute the energy barrier ΔE_b (eV) and the zero-temperature yield stress τ_y0 (MPa). Finally, compute the tensile yield stress σ_y (MPa) at temperature T=293 K, strain rate ε̇=10⁻³ s⁻¹, and Taylor factor M=3.06 using the thermal activation formula. Save the three quantities as a JSON object with keys 'delta_E_b', 'tau_y0', 'sigma_y' in /app/outputs/results.json.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute isotropic dislocation core coefficients
- Role: process
- Action: Implement the isotropic elasticity solute-strengthening model for a dissociated edge dislocation with a bimodal Gaussian Burgers vector distribution. Using the given core parameters d/b=7 and σ/b=1.5, compute the dimensionless energy-fluctuation function g^iso(w) as a function of amplitude w. Numerically minimize the total energy of the wavy dislocation to find the optimal amplitude w_c that satisfies dg^iso/dw = g^iso/(2w). Obtain the dimensionless coefficients w_c and g^iso(w_c) needed in the subsequent strength calculation.
- Evidence: none

### Step 2: Compute Cantor alloy strengthening and output results
- Role: scored (load-bearing)
- Action: Using the dimensionless coefficients from step 1 and the following material parameters: C11=195.9 GPa, C12=117.7 GPa, C44=129.3 GPa; lattice constant a=3.6 Å giving Burgers vector b = a/√2 ≈ 2.5456 Å; line tension Γ = (1/8)·μ_{111/110}·b² with μ_{111/110} = (C11−C12+C44)/3; Voigt-averaged shear modulus μ_Voigt = (C11−C12+3C44)/5; Poisson's ratio ν_Voigt computed from bulk and shear moduli; misfit-volume combination Σc_nΔV_n² = 0.43 Å⁶; temperature T = 293 K, strain rate ε̇ = 10⁻³ s⁻¹, reference strain rate ε̇₀ = 10⁴ s⁻¹, Taylor factor M = 3.06. Compute the prefactors from the isotropic model, then compute the energy barrier ΔE_b (eV), zero-temperature yield stress τ_y0 (MPa), and the tensile yield stress σ_y (MPa) using the thermal activation formula. Save the results as a JSON object with keys 'delta_E_b', 'tau_y0', 'sigma_y' to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"delta_E_b": float, "tau_y0": float, "sigma_y": float}
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
- target_policy: threshold_or_better
- description: Predicted solute strengthening parameters for the CoCrFeMnNi Cantor alloy.
- schema:
  - `type`: object
  - `required`:
    - `delta_E_b`: float
    - `tau_y0`: float
    - `sigma_y`: float

Notes: The agent must produce the three quantities as specified using the described isotropic Voigt model. The checker will compare each quantity to a reference value recomputed from the same model and inputs, scoring by tolerance on relative error.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "delta_E_b": "float",
          "tau_y0": "float",
          "sigma_y": "float"
        }
      },
      "description": "Predicted solute strengthening parameters for the CoCrFeMnNi Cantor alloy."
    }
  ],
  "notes": "The agent must produce the three quantities as specified using the described isotropic Voigt model. The checker will compare each quantity to a reference value recomputed from the same model and inputs, scoring by tolerance on relative error."
}
```

## How you are scored
A hidden verifier will independently re-implement the identical isotropic model using the same numerical inputs. It will extract the values of delta_E_b, tau_y0, and sigma_y from your /app/outputs/results.json and compare each against its own recomputed reference value. The reward is determined by the relative errors of the three quantities. Meeting the verifier's accuracy threshold for all three yields full credit; partial credit may be given if only some pass or if errors exceed the thresholds. Your job is to faithfully implement the described computational procedure and produce the three outputs.
