# Atomistic simulation of edge dislocation motion in aluminum and lattice-dynamics limiting velocity prediction

## Problem background
The motion of dislocations governs plastic deformation in crystalline materials. Understanding the intrinsic resistance to dislocation motion — arising from the crystal lattice itself, rather than obstacles — is key for predicting mechanical behavior under high strain rates. Molecular dynamics simulations can probe the velocity of an edge dislocation as a function of applied shear stress and temperature, revealing distinct regimes: a Peierls barrier at low stress, a phonon‑drag regime where velocity decreases with temperature, a subsonic limiting velocity plateau, and potentially a transonic jump at very high stress. A separate lattice‑dynamics analysis, using the same interatomic potential and the Celli‑Flytzanis criterion, can predict a limiting velocity for the defect from phonon dispersion relations. This task reproduces the MD mobility curve and the lattice‑dynamics prediction for aluminum, quantifying the plateau velocity and the drag coefficient.

## Approach
We use the Ercolessi‑Adams embedded‑atom method (EAM) potential for aluminum. First, a simulation cell containing an edge dislocation is built and relaxed. Molecular dynamics simulations are then run at a fixed temperature (e.g., 100 K) for a range of applied shear stresses, tracking the dislocation position over time to extract steady‑state velocities; from these, the subsonic plateau velocity is identified and an effective drag coefficient B is estimated via a tangent‑line construction. Independently, the phonon dispersion relation ω(k) of aluminum is computed using the same EAM potential. The dispersion curve along a specific high‑symmetry direction is analyzed, and the Celli‑Flytzanis tangent condition is applied to predict a limiting dislocation velocity v₁. The workflow integrates MD simulation, velocity–stress analysis, and lattice‑dynamics calculation.

## Reproduction target
Run a series of MD simulations of an edge dislocation in aluminum at a chosen fixed temperature (suggested 100 K) for at least five applied shear stresses (e.g., 50–2000 MPa). For each stress, determine the steady‑state dislocation velocity. From the velocity–stress data, identify the subsonic plateau velocity and estimate the dislocation drag coefficient B. Separately, compute the phonon dispersion ω(k) along kₓ at fixed k_y = 2√2/(a₀√3), k_z = 2π/(a₀√3) using the same potential. From this curve, find the wavevector where a radial line is tangent to the branch and report the corresponding limiting velocity v₁. Document the results in the specified CSV output files.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/downloads.html
- Ercolessi-Adams EAM potential for aluminum: https://www.ctcms.nist.gov/potentials/
- Phonon analysis tool (Phonopy or LAMMPS fix phonon): https://phonopy.github.io/phonopy/
- Python with numpy, pandas, scipy: numpy, pandas, scipy

## Workflow steps

### Step 1: Build relaxed edge dislocation configuration
- Role: process
- Action: Construct a simulation cell oriented slip ⟨110⟩, line ⟨112⟩, normal ⟨111⟩ with dimensions 226.66 Å × 4.59 Å × 137 Å. Remove two atomic half‑layers, apply Volterra displacements for an edge dislocation, and energy‑minimize using the Ercolessi‑Adams EAM potential to obtain the dissociated initial configuration.
- Evidence: `/app/outputs/dislocation_initial.lmp`

### Step 2: Run MD simulations of dislocation motion
- Role: process
- Action: Using LAMMPS and the Ercolessi‑Adams EAM potential, run a series of MD simulations at a fixed temperature (e.g., 100 K) for a range of applied shear stresses (e.g., 50 MPa to 2000 MPa). For each stress, equilibrate the configuration under Nose‑Hoover thermostat, apply equal‑and‑opposite shear forces on top/bottom atomic layers, and simulate for at least 100 ps. Record the dislocation position as a function of time (e.g., from the peak of the slip distribution).
- Evidence: `/app/outputs/dislocation_positions.json`

### Step 3: Extract velocity–stress curve and plateau
- Role: scored (load-bearing)
- Action: From the MD dislocation‑position histories, compute the steady‑state velocity for each applied stress. Tabulate stress (MPa) and velocity (nm/ps) and output to 'md_velocity_stress.csv'. Also identify the subsonic plateau velocity (the average velocity for stresses above ~500 MPa where velocity saturates).
- Output file: `/app/outputs/md_velocity_stress.csv`
- Format: csv
- Contract: stress_MPa (float), velocity_nm_ps (float)
- Scoring: scored by hidden verifier

### Step 4: Estimate dislocation drag coefficient
- Role: scored
- Action: Using the velocity‑stress data from step_03, draw a tangent line from the origin to the curve (avoiding the Peierls and plateau extremes) to estimate the drag coefficient B from the slope B = τ b / v, where b is the Burgers vector magnitude (0.286 nm for Al). Report the result in 'drag_coefficient_B.csv'.
- Output file: `/app/outputs/drag_coefficient_B.csv`
- Format: csv
- Contract: temperature_K (float), B_Pa_s (float)
- Scoring: scored by hidden verifier

### Step 5: Compute phonon dispersion relations
- Role: scored
- Action: Using the Ercolessi‑Adams EAM potential and a phonon analysis tool (Phonopy or LAMMPS fix phonon), compute the phonon dispersion ω(k) for aluminum. Extract the dispersion curve along kx for fixed ky = 2√2/(a₀√3) and kz = 2π/(a₀√3), corresponding to the dislocation geometry. Save the curve as 'ld_dispersion_curve.csv'.
- Output file: `/app/outputs/ld_dispersion_curve.csv`
- Format: csv
- Contract: kx_angstrom_inv (float), omega_THz (float)
- Scoring: scored by hidden verifier

### Step 6: Predict limiting velocity from dispersion tangent
- Role: scored
- Action: Apply the Celli‑Flytzanis criterion: find the wavevector kx (in the dispersion curve from step_05) where a radial line from the origin is tangent to a branch, satisfying ∂ω/∂kx = v1 and ∂ω/∂ky = 0, ∂ω/∂kz = 0. Record the tangent point kx and the corresponding limiting velocity v1 in 'ld_limiting_velocity.csv'.
- Output file: `/app/outputs/ld_limiting_velocity.csv`
- Format: csv
- Contract: v1_nm_ps (float), kx_angstrom_inv (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/md_velocity_stress.csv`
- `/app/outputs/drag_coefficient_B.csv`
- `/app/outputs/ld_dispersion_curve.csv`
- `/app/outputs/ld_limiting_velocity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### md_velocity_stress.csv
- path: `/app/outputs/md_velocity_stress.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Tabulated steady‑state dislocation velocity versus applied shear stress from MD simulations. The checker derives the subsonic plateau velocity and compares to the paper‑reported value within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `stress_MPa`, `velocity_nm_ps`
  - `units`:
    - `stress_MPa`: MPa
    - `velocity_nm_ps`: nm/ps

### drag_coefficient_B.csv
- path: `/app/outputs/drag_coefficient_B.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Dislocation drag coefficient B estimated from the tangent‑line slope of the velocity‑stress curve. Checker compares to the paper‑derived reference at the selected temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `B_Pa_s`
  - `units`:
    - `temperature_K`: K
    - `B_Pa_s`: Pa·s

### ld_dispersion_curve.csv
- path: `/app/outputs/ld_dispersion_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion curve ω(kx) at fixed ky, kz. The checker performs a structural audit (e.g., verifies existence of a valid branch and checks that the tangent point yields a consistent limiting velocity).
- schema:
  - `type`: table
  - `required_columns`: `kx_angstrom_inv`, `omega_THz`
  - `units`:
    - `kx_angstrom_inv`: 1/Å
    - `omega_THz`: THz

### ld_limiting_velocity.csv
- path: `/app/outputs/ld_limiting_velocity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Lattice‑dynamics predicted limiting dislocation velocity v1 and the corresponding tangent wavevector kx, obtained from the dispersion curve via the Celli‑Flytzanis criterion. Checker compares to the paper‑reported value within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `v1_nm_ps`, `kx_angstrom_inv`
  - `units`:
    - `v1_nm_ps`: nm/ps
    - `kx_angstrom_inv`: 1/Å

Notes: All scored artifacts correspond to the paper's headline quantities: subsonic limiting velocity, drag coefficient, and lattice‑dynamics prediction. The finite‑size scaling analysis (stages 5‑7 of the full paper workflow) is omitted as a supporting check; its essence is captured by the comparison between MD plateau and v1. The proprietary 'vibra' code is replaced by open‑source phonon tools. The transonic velocity regime is excluded per scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "md_velocity_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stress_MPa",
          "velocity_nm_ps"
        ],
        "units": {
          "stress_MPa": "MPa",
          "velocity_nm_ps": "nm/ps"
        }
      },
      "description": "Tabulated steady‑state dislocation velocity versus applied shear stress from MD simulations. The checker derives the subsonic plateau velocity and compares to the paper‑reported value within a tolerance."
    },
    {
      "file": "drag_coefficient_B.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "B_Pa_s"
        ],
        "units": {
          "temperature_K": "K",
          "B_Pa_s": "Pa·s"
        }
      },
      "description": "Dislocation drag coefficient B estimated from the tangent‑line slope of the velocity‑stress curve. Checker compares to the paper‑derived reference at the selected temperature."
    },
    {
      "file": "ld_dispersion_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx_angstrom_inv",
          "omega_THz"
        ],
        "units": {
          "kx_angstrom_inv": "1/Å",
          "omega_THz": "THz"
        }
      },
      "description": "Phonon dispersion curve ω(kx) at fixed ky, kz. The checker performs a structural audit (e.g., verifies existence of a valid branch and checks that the tangent point yields a consistent limiting velocity)."
    },
    {
      "file": "ld_limiting_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "v1_nm_ps",
          "kx_angstrom_inv"
        ],
        "units": {
          "v1_nm_ps": "nm/ps",
          "kx_angstrom_inv": "1/Å"
        }
      },
      "description": "Lattice‑dynamics predicted limiting dislocation velocity v1 and the corresponding tangent wavevector kx, obtained from the dispersion curve via the Celli‑Flytzanis criterion. Checker compares to the paper‑reported value within a tolerance."
    }
  ],
  "notes": "All scored artifacts correspond to the paper's headline quantities: subsonic limiting velocity, drag coefficient, and lattice‑dynamics prediction. The finite‑size scaling analysis (stages 5‑7 of the full paper workflow) is omitted as a supporting check; its essence is captured by the comparison between MD plateau and v1. The proprietary 'vibra' code is replaced by open‑source phonon tools. The transonic velocity regime is excluded per scope."
}
```

## How you are scored
A hidden verifier reads your output artifacts and recomputes derived quantities. For the MD velocity‑stress curve, it extracts the plateau velocity and compares it to the paper’s reported value with an appropriate tolerance. For the drag coefficient, it checks B against the paper‑derived reference. The phonon dispersion curve is audited for structural validity, and the lattice‑dynamics predicted velocity v₁ is compared to the paper’s result. Each artifact’s score is weighted, with the plateau velocity and v₁ carrying the most weight. The final reward (0–1) is the weighted average. Simply copying reference numbers without genuine computation will not satisfy the verifier; the checks compare your actual computed outputs.
