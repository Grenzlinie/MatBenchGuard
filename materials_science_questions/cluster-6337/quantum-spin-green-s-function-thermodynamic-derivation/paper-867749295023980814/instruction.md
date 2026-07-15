# Spin-wave Spectrum and Thermodynamics of Layered Heisenberg- Compass Model in RPA

## Problem background
The layered spin-1/2 Heisenberg antiferromagnet with in-plane compass-model interactions arises in the context of spin-orbit-coupled transition-metal oxides such as iridates. In these compounds, strong relativistic coupling generates bond-directional exchange anisotropies that can stabilize long-range antiferromagnetic order and modify the spin-wave excitation spectrum. Understanding the magnetic excitation spectrum, the temperature dependence of the sublattice magnetization, and the Néel temperature is important for linking model predictions to experimental measurements. This task reproduces the random phase approximation (RPA) Green’s function calculation of the spin-wave spectrum, sublattice magnetization, and Néel temperature for the two-sublattice model, covering symmetric and anisotropic compass interactions, as well as an extension with next-nearest-neighbor exchange, allowing a study of how the compass anisotropy affects the magnetic properties.

## Approach
The calculation employs a two-sublattice representation of the antiferromagnetic order, with the order parameter direction fixed by the compass-model anisotropy. The retarded two-time commutator Green’s functions for spin operators are evaluated using the equations of motion, and the RPA is applied to decouple the hierarchy of Green’s functions by replacing higher-order correlation functions with products of sublattice magnetizations and lower-order Green’s functions. This leads to a closed 4×4 matrix system in sublattice and spin-± space. After Fourier transformation, the interaction matrix yields the spin-wave dispersion branches ω_±(q) from the pole condition. The sublattice magnetization σ is obtained by self-consistently solving the kinematic relation for spin-1/2, in which the correlation function is expressed through the spectral representation of the Green’s function and integrated numerically over the Brillouin zone. The Néel temperature TN is determined either from the linearized self-consistency equation in the limit σ→0 or by tracking the temperature at which σ(T) vanishes.

## Reproduction target
Compute and output the following quantities using the RPA Green’s function method for the two-sublattice model:

1. **Spin-wave dispersion** for the symmetric compass model **only** (Fig. 1 of the reference study): parameters J = 65 meV, J_z = 0, Γ_x = Γ_y = 3.4 meV (Γ/J = 0.0522). Use the zero-temperature sublattice magnetization σ = 0.37 as fixed input (do not recalculate σ dynamically for the dispersion). Provide ω_±(q) along the high-symmetry path in the square-lattice Brillouin zone: Γ(0,0,0) → X(π,0,0) → M(π,π,0) → Γ(0,0,0) with q_z = 0. Use at least 50 points per segment. The output array must be ordered along this path.

2. **Sublattice magnetization σ(T)** for the symmetric Ba₂IrO₄ case: J = 65 meV, J_z = 5×10⁻⁵ J, Γ_x = Γ_y = 3.4 meV. Temperatures T must be given in dimensionless units (T/J). Compute σ on a temperature grid from T/J = 0.05 up to above T_N (at least to T/J = 0.5) with a step no larger than 0.01.

3. **Néel temperatures T_N** for two required cases, using the case names exactly as specified:
   - Case key `"symmetric_Ba2IrO4"`: J = 65 meV, J_z = 5×10⁻⁵ J, Γ_x = Γ_y = 3.4 meV.
   - Case key `"NNN_model"`: J = 65 meV, J_z = 0, Γ_x = Γ_y = 3.4 meV, next-nearest-neighbor couplings J′ = −(1/3)J, J′′ = (1/4)J.
   For each case, report Tc_meV and Tc_K (Tc_K = Tc_meV × 11.6045 K/meV). The checker will compare the Tc_meV values against hidden reference results; keys must match exactly.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute RPA spin-wave spectrum, sublattice magnetization, and Néel temperatures
- Role: scored (load-bearing)
- Action: Implement the RPA Green’s function method for the two-sublattice layered Heisenberg antiferromagnet with compass-model interactions. For the dispersion, evaluate the following explicit formulas. Define J(q) = 2J(cos q_x + cos q_y) + 2J_z cos q_z. For the symmetric compass model (J_z=0, Γ_x=Γ_y=Γ=3.4 meV, fixed σ=0.37) set A = σ[J(0)+2Γ], B(q)=σ Γ cos q_y, C(q)=σ[J(q)+Γ cos q_y]. The two branches are ω_-(q)=σ sqrt[J(0)^2 - J(q)^2 + 4Γ J(0) + 4Γ^2 - 2Γ(J(0)+J(q)+2Γ) cos q_y], ω_+(q)=σ sqrt[J(0)^2 - J(q)^2 + 4Γ J(0) + 4Γ^2 + 2Γ(J(0)-J(q)+2Γ) cos q_y]. Evaluate them on the q-path Γ(0,0,0)→X(π,0,0)→M(π,π,0)→Γ(0,0,0) with q_z=0, ≥50 points/segment. For the sublattice magnetization σ(T) of the symmetric Ba₂IrO₄ case (J=65 meV, J_z=5e-5J, Γ_x=Γ_y=Γ=3.4 meV) solve σ = 0.5 - (2/N) Σ_q ⟨S⁻_q S⁺_q⟩ iteratively, where the correlation function is ⟨S⁻_q S⁺_q⟩=2σ Σ_{μ,ν=±} I_{μν}(q) / (exp(μ ω_ν(q)/T)-1), with I_{μν}(q)=a_q(μ ω_ν) / [8 μ ν ω_ν A B(q)], a_q(ω)=ω^3 + A ω^2 - [A^2+B^2-C^2] ω - A^3 + A[B^2+C^2]. Grid T/J from 0.05 to 0.5, step ≤0.01. Compute Néel temperature for both cases via the linearized equation T_N = 1/(4C), C = (1/(N/2)) Σ_q Σ_{μ,ν} I_{μν}(q)/(μ ε_ν(q)), with ε_ν(q)=ω_ν(q)/σ. For symmetric_Ba2IrO4 use the same parameters as magnetization. For NNN_model (J=65 meV, J_z=0, Γ_x=Γ_y=Γ=3.4 meV, J'=-J/3, J''=J/4) incorporate NNN by replacing J(0) in the dispersion with J_eff(q) = J(0) - J_nn(0) + J_nn(q), where J_nn(q) = 4J' cos q_x cos q_y + 2J''(cos 2q_x + cos 2q_y), so that ε_-(q)=sqrt[J_eff(q)^2 - J(q)^2 + 4Γ J_eff(q) + 4Γ^2 - 2Γ(J_eff(q)+J(q)+2Γ) cos q_y], ε_+(q)=sqrt[J_eff(q)^2 - J(q)^2 + 4Γ J_eff(q) + 4Γ^2 + 2Γ(J_eff(q)-J(q)+2Γ) cos q_y]; use these ε_ν in C. Convert T_N to Tc_meV and Tc_K = Tc_meV × 11.6045. Package all results into `results.json` as per the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"dispersion": [{"q_point": [float, float, float], "omega_minus": float, "omega_plus": float}], "magnetization_curve": [{"T": float, "sigma": float}], "neel_temperatures": {"case_name": {"Tc_meV": float, "Tc_K": float}}}
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
- target_policy: metric_recompute
- description: JSON file containing the RPA spin-wave dispersion for the symmetric compass model (J=65 meV, Jz=0, Γx=Γy=3.4 meV, σ=0.37), the sublattice magnetization σ(T) for the symmetric Ba₂IrO₄ case (J=65 meV, Jz=5e-5 J, Γx=Γy=3.4 meV) with T in units of J, and the Néel temperatures for two required cases: symmetric_Ba2IrO4 and NNN_model. The checker recomputes dispersion at the provided q-points, compares magnetization at selected temperatures, and verifies TN against hidden paper values.
- schema:
  - `dispersion`:
    - `q_point`: `float`, `float`, `float`
    - `omega_minus`: float
    - `omega_plus`: float
  - `magnetization_curve`:
    - `T`: float
    - `sigma`: float
  - `neel_temperatures`:
    - `symmetric_Ba2IrO4`:
      - `Tc_meV`: float
      - `Tc_K`: float
    - `NNN_model`:
      - `Tc_meV`: float
      - `Tc_K`: float

Notes: All quantities must be computed from the given model parameters using the RPA Green's function formalism. The q-point path must follow Γ→X→M→Γ in the square lattice with qz=0. Temperatures in magnetization_curve must be dimensionless T/J. The keys in neel_temperatures are exact: 'symmetric_Ba2IrO4' and 'NNN_model'. Other keys may be present but will not be scored.

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
      "target_policy": "metric_recompute",
      "schema": {
        "dispersion": [
          {
            "q_point": [
              "float",
              "float",
              "float"
            ],
            "omega_minus": "float",
            "omega_plus": "float"
          }
        ],
        "magnetization_curve": [
          {
            "T": "float",
            "sigma": "float"
          }
        ],
        "neel_temperatures": {
          "symmetric_Ba2IrO4": {
            "Tc_meV": "float",
            "Tc_K": "float"
          },
          "NNN_model": {
            "Tc_meV": "float",
            "Tc_K": "float"
          }
        }
      },
      "description": "JSON file containing the RPA spin-wave dispersion for the symmetric compass model (J=65 meV, Jz=0, Γx=Γy=3.4 meV, σ=0.37), the sublattice magnetization σ(T) for the symmetric Ba₂IrO₄ case (J=65 meV, Jz=5e-5 J, Γx=Γy=3.4 meV) with T in units of J, and the Néel temperatures for two required cases: symmetric_Ba2IrO4 and NNN_model. The checker recomputes dispersion at the provided q-points, compares magnetization at selected temperatures, and verifies TN against hidden paper values."
    }
  ],
  "notes": "All quantities must be computed from the given model parameters using the RPA Green's function formalism. The q-point path must follow Γ→X→M→Γ in the square lattice with qz=0. Temperatures in magnetization_curve must be dimensionless T/J. The keys in neel_temperatures are exact: 'symmetric_Ba2IrO4' and 'NNN_model'. Other keys may be present but will not be scored."
}
```

## How you are scored
A hidden verifier will independently recompute selected quantities from your output and compare them against reference values derived from the original study. For the dispersion, it recomputes ω±(q) at the exact q-points you report using the analytical expressions and checks agreement within a narrow tolerance. For the magnetization curve, it compares σ at several temperature points against reference values. For the Néel temperature, your reported Tc_meV is compared to the expected value within a tolerance. Additional structural checks verify that the dispersion exhibits the correct qualitative features (e.g., presence of gaps, symmetry between branches). Each component is weighted, and the final reward is a single float in [0,1] reflecting overall agreement.
