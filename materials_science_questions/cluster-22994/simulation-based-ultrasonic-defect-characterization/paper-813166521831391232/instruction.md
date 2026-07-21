# Phase-velocity dispersion curves for guided waves in a thin spherical shell

## Problem background
Thin segmental spherical shell components (e.g., pressure vessels, aircraft fuselage sections) can develop defects that threaten structural integrity. Ultrasonic guided waves are an attractive tool for nondestructive inspection of such curved plates because they can propagate long distances and interrogate the entire thickness. However, guided wave propagation in spherical shells is dispersive: the phase velocity of each wave mode depends on frequency. An accurate understanding of the dispersion characteristics — specifically, the set of phase-velocity curves as a function of frequency — is essential for choosing excitation frequencies and modes that exhibit low dispersion and are therefore well suited for defect detection. This task requires computing the phase velocity dispersion curves for guided waves in a thin spherical shell with prescribed material properties and dimensions, enabling the analysis and selection of suitable inspection modes.

## Approach
The problem is formulated using the equations of motion for an isotropic elastic medium in spherical coordinates. The shell is treated as a medium with position-dependent elastic constants and density, multiplied by a rectangular window function that enforces stress-free boundaries at the inner and outer radii: the material exists only between those radii, and outside the window the acoustic impedance is zero. The wave front on the shell surface is assumed to be toroidal, allowing a separation of variables with harmonic time dependence and a single propagation direction. Substituting the toroidal-wave ansatz and the windowed material description into the stress-equilibrium equations yields a system of coupled ordinary differential equations for the radial dependence of the displacement amplitudes. The boundary conditions require zero traction on the inner and outer surfaces. To solve this differential eigenvalue problem, the radial displacement amplitude functions are expanded in a series of Legendre orthogonal polynomials, turning the problem into an algebraic eigenvalue problem. The eigenvalues correspond to permissible wavenumbers at each frequency, from which the phase velocity for each guided wave mode is obtained. This procedure is carried out for a frequency range covering 0 to 1 MHz.

## Reproduction target
Compute the phase velocity dispersion curves for guided waves in a thin segmental spherical shell with the following properties: density ρ = 2800 kg/m³, outer radius b = 400 mm, and thickness h = 1 mm (inner radius a = 399 mm). Using the Legendre polynomial expansion technique described above, solve the governing equations and boundary conditions to obtain the phase velocity for each guided wave mode as a function of frequency. Produce a CSV file named `dispersion_curves.csv` in the `/app/outputs` directory with columns: `frequency_Hz` (float), `mode_number` (int), `phase_velocity_m_per_s` (float). The file must contain data for at least the first three guided wave modes over the frequency range 0 to 1 MHz.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute dispersion curves
- Role: scored (load-bearing)
- Action: Implement the governing equations (stress-equilibrium with windowed material and toroidal-wave ansatz) and stress-free boundary conditions for a thin segmental spherical shell. Expand radial displacement amplitudes in Legendre orthogonal polynomials to convert the differential eigenvalue problem to an algebraic one. Solve for phase velocities for frequencies from 0 to 1 MHz. Produce dispersion_curves.csv with columns frequency_Hz, mode_number, phase_velocity_m_per_s for at least the first three guided wave modes.
- Output file: `/app/outputs/dispersion_curves.csv`
- Format: csv
- Contract: CSV with columns: frequency_Hz (float), mode_number (int), phase_velocity_m_per_s (float). At least the first three modes over 0-1 MHz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_curves.csv
- path: `/app/outputs/dispersion_curves.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phase velocity dispersion curves for guided waves in a thin segmental spherical shell (density 2800 kg/m³, outer radius 400 mm, thickness 1 mm).
- schema:
  - `type`: table
  - `required_columns`: `frequency_Hz`, `mode_number`, `phase_velocity_m_per_s`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_Hz",
          "mode_number",
          "phase_velocity_m_per_s"
        ]
      },
      "description": "Phase velocity dispersion curves for guided waves in a thin segmental spherical shell (density 2800 kg/m³, outer radius 400 mm, thickness 1 mm)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently read your `dispersion_curves.csv` and extract the phase velocities at a set of selected frequency points. It will match the modes and compare your computed phase velocities to reference values using a relative tolerance. The verifier combines the scores of all workflow stages into a final reward. Simply reporting a value from a known source is not enough; the verifier checks whether your computation genuinely reproduces the expected dispersion behavior. The exact reference data and tolerances are hidden, so you must compute the dispersion curves from the given physics and geometry.
