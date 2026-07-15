# Germanium Thin Film Thermal Conductivity from NEMD and Phonon Boltzmann Transport

## Problem background
Germanium thin films are central to modern semiconductor and microelectronic devices, where efficient heat removal is often limited by the thermal conductivity of the film itself. In bulk germanium crystals, thermal conductivity is isotropic and reasonably well-known. However, when film thickness drops to the nanoscale, phonon boundary scattering can drastically reduce the effective conductivity and introduce directional anisotropy. Understanding how thermal conductivity depends on film thickness and heat-flow direction is critical for thermal design at the nanoscale. This task computes the thermal conductivity of germanium thin films as a function of thickness using two independent computational strategies, providing quantitative insight into these size and directional effects.

## Approach
Two complementary approaches are used to assess the thermal transport.

**1. Non‑Equilibrium Molecular Dynamics (NEMD)**  
A diamond-structure germanium thin film is simulated with the Stillinger–Weber interatomic potential, using the following parameters (units as in the original work): A = 7.049556, B = 0.602224, η = 21.0, γ = 1.20, r_cut = 1.80 (reduced units), σ = 0.20951 nm.  
The simulation domain is heated by a hot reservoir at 330 K and cooled by a cold reservoir at 270 K. Separate runs apply the temperature gradient in the through‑thickness (normal) and in‑plane (tangential) directions. Periodic boundary conditions are used in the film plane, and fixed walls in the thickness direction.  
From the steady‑state heat flux and temperature gradient, thermal conductivity is obtained via Fourier’s law, yielding both the normal and tangential conductivities for each of the nine specified film thicknesses.

**2. Phonon Boltzmann Transport (Dubey Model)**  
A theoretical estimate is obtained from the Dubey phonon Boltzmann transport framework, which resolves the phonon dispersion into transverse and longitudinal branches and incorporates boundary scattering via a thickness‑dependent relaxation time. The key material parameters are:  
- Transverse phonon velocities: v_T1 = 3.55×10³ m/s (0<ω<ω1), v_T2 = 1.30×10³ m/s (ω1<ω<ω2);  
- Longitudinal phonon velocities: v_L1 = 4.92×10³ m/s (0<ω<ω4), v_L2 = 2.46×10³ m/s (ω4<ω<ω3);  
- Dispersion coefficients: R1 = 2.95×10⁻²⁷, R2 = 8.28×10⁻²⁷, R3 = 0, R4 = 1.13×10⁻²⁷;  
- Cutoff temperatures: θ1 = 90 K, θ2 = 108 K, θ4 = 208 K, θ3 = 319 K.  
The relaxation time is built from the Casimir length and a boundary‑scattering reduction function F that depends on the film thickness and a wall‑scattering transmission coefficient α. Numerically integrating the transverse and longitudinal contributions (the integrals contain factors (1+R_i x² T²)²/(1+3R_i x² T²)) yields the total theoretical thermal conductivity for each thickness.  

Together, the NEMD and Boltzmann‑transport results provide an independent cross‑check of the size effect and anisotropy in thin‑film germanium.

## Reproduction target
For germanium thin films with the following nine thicknesses – 5.67, 10.21, 17.00, 22.67, 28.34, 34.01, 39.68, 45.35, and 50.92 nm – produce:

*   From NEMD simulations: the normal (through‑thickness) and tangential (in‑plane) thermal conductivity values, written to `step_01_md_results.csv`.
*   From the Dubey Boltzmann transport model: the total theoretical thermal conductivity, written to `step_02_theory_results.csv`.

The data must allow verification that (a) the conductivity decreases with decreasing film thickness (a monotonic overall trend), and (b) for every thickness, the in‑plane (tangential) conductivity is clearly larger than the through‑thickness (normal) conductivity.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/download.html
- Python with SciPy (and NumPy): scipy, numpy
- Stillinger-Weber potential parameters for germanium
- Dubey model parameters for germanium (phonon velocities, cutoff temperatures, dispersion parameters)
- Germanium diamond crystal structure

## Workflow steps

### Step 1: NEMD simulation of germanium thin film thermal conductivity
- Role: scored
- Action: Set up a germanium thin film simulation system with the Stillinger–Weber potential (parameters provided in the instruction) and perform non-equilibrium molecular dynamics for nine film thicknesses (5.67, 10.21, 17.00, 22.67, 28.34, 34.01, 39.68, 45.35, 50.92 nm). Use hot reservoir at 330 K, cold reservoir at 270 K, periodic boundary conditions in the film plane, and fixed walls in the thickness direction. Compute normal thermal conductivity (through thickness) and tangential thermal conductivity (in-plane) from the heat flux and temperature gradient using Fourier's law.
- Output file: `/app/outputs/step_01_md_results.csv`
- Format: csv
- Contract: Columns: thickness_nm (float, nm), k_normal_WmK (float, W/m·K), k_tangential_WmK (float, W/m·K). Nine rows, one per thickness.
- Scoring: scored by hidden verifier

### Step 2: Dubey Boltzmann transport theory calculation
- Role: scored
- Action: Implement the Dubey phonon Boltzmann transport model for germanium thin films using the provided dispersion parameters (phonon velocities, cutoff temperatures, R_i) and the boundary scattering model with the decrement function F. Numerically integrate the transverse and longitudinal phonon conductivity contributions (integrals over x with factors (1+R_i x^2 T^2)^2/(1+3 R_i x^2 T^2)) and sum them to obtain the total theoretical thermal conductivity for each of the nine film thicknesses.
- Output file: `/app/outputs/step_02_theory_results.csv`
- Format: csv
- Contract: Columns: thickness_nm (float, nm), k_theory_WmK (float, W/m·K). Nine rows, one per thickness.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_md_results.csv`
- `/app/outputs/step_02_theory_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_md_results.csv
- path: `/app/outputs/step_01_md_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: MD thermal conductivity values for the nine thicknesses. Scoring verifies structural properties: (a) thermal conductivity decreases with decreasing thickness (monotonic overall trend), and (b) for each thickness, tangential conductivity exceeds normal conductivity.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `k_normal_WmK`, `k_tangential_WmK`
  - `units`:
    - `thickness_nm`: nm
    - `k_normal_WmK`: W/(m·K)
    - `k_tangential_WmK`: W/(m·K)

### step_02_theory_results.csv
- path: `/app/outputs/step_02_theory_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Theoretical thermal conductivity values from the Dubey Boltzmann transport model. The checker recomputes the values using the same parameters and integrals, then compares the agent-reported values against the recomputed reference within a tight relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `k_theory_WmK`
  - `units`:
    - `thickness_nm`: nm
    - `k_theory_WmK`: W/(m·K)

Notes: MD results are scored by structural audit because absolute values can vary with simulation parameters; the theory results are deterministic given the same model implementation, so an exact-match tolerance check is appropriate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_md_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "k_normal_WmK",
          "k_tangential_WmK"
        ],
        "units": {
          "thickness_nm": "nm",
          "k_normal_WmK": "W/(m·K)",
          "k_tangential_WmK": "W/(m·K)"
        }
      },
      "description": "MD thermal conductivity values for the nine thicknesses. Scoring verifies structural properties: (a) thermal conductivity decreases with decreasing thickness (monotonic overall trend), and (b) for each thickness, tangential conductivity exceeds normal conductivity."
    },
    {
      "file": "step_02_theory_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "k_theory_WmK"
        ],
        "units": {
          "thickness_nm": "nm",
          "k_theory_WmK": "W/(m·K)"
        }
      },
      "description": "Theoretical thermal conductivity values from the Dubey Boltzmann transport model. The checker recomputes the values using the same parameters and integrals, then compares the agent-reported values against the recomputed reference within a tight relative tolerance."
    }
  ],
  "notes": "MD results are scored by structural audit because absolute values can vary with simulation parameters; the theory results are deterministic given the same model implementation, so an exact-match tolerance check is appropriate."
}
```

## How you are scored
A hidden verifier independently evaluates each of the two output files.

*For the MD results (`step_01_md_results.csv`):* a structural audit checks that (a) the conductivity exhibits a monotonic decreasing trend as the film becomes thinner, and (b) for each thickness, the tangential conductivity exceeds the normal conductivity by a clear margin. The audit does not require matching precise published numbers, only that these physically expected trends emerge from your simulation.

*For the theory results (`step_02_theory_results.csv`):* the verifier recomputes the theoretical conductivity using the same Dubey model and parameters stated in this instruction. Your reported values are compared against the recomputed reference; a close match (allowing for reasonable numerical integration differences) is required.

The final reward is a weighted combination of the scores from the two stages. Simply reproducing numbers from the literature will not satisfy these checks — only a genuine execution of the required computations can produce the correct trends and values.
