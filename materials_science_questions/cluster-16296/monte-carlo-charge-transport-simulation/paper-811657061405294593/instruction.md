# GaAs Fermi-Kinetics Transport Model: Drift Velocity and Device I-V Simulation

## Problem background
Simulating hot‑electron transport in semiconductors such as GaAs is essential for understanding device behaviour, but the most faithful method—full‑band ensemble Monte Carlo—is computationally extremely expensive. A much faster deterministic alternative is to describe the electron population with a small set of Fermi‑Dirac distributions assigned to different regions of the conduction band. This Fermi‑kinetics model treats heat flow between the electron ensembles through the thermodynamic identity for an ideal gas, avoiding the closure issues that arise in traditional energy‑transport models that rely on an electron thermal conductivity. By incorporating the full band structure via energy‑isosurface integrals, the model aims to reproduce the main hot‑electron effects—notably the drift‑velocity overshoot and the current–voltage characteristic of a realistic n⁺nn⁺ diode—at a fraction of the computational cost. The task is to compute from public inputs the two key output curves that test this capacity.

## Approach
The model assigns separate Fermi‑Dirac distribution functions to multiple valleys (Γ, L, X) in the GaAs conduction band, and further sub‑divides them according to phonon‑accessible energy intervals. The band energies are obtained by the empirical pseudopotential method on a tetrahedral mesh filling the irreducible wedge of the Brillouin zone. Energy isosurfaces are then extracted and used to evaluate numerical spectra: density‑of‑states, phonon‑scattering integrals (optical deformation‑potential and polar‑optical), and flux‑isosurface integrals that include momentum‑relaxation‑time estimates. These spectra are approximated by piecewise power‑law fits, which become the transport coefficients. In a spatially homogeneous setting the drift‑velocity curve is obtained from the drift‑only flux with six Fermi gases; for the 1‑D device the full real‑space equations (particle flux, kinetic‑energy flux, heat flow via the thermodynamic identity) are coupled to Gauss’s law and solved by Newton iteration. This workflow yields the two headline quantities without requiring any pre‑computed data from the paper.

## Reproduction target
Compute and output as CSV files:

- Bulk electron drift velocity vs. electric field for undoped GaAs at 300 K, with a background electron density of 1 × 10¹³ cm⁻³. The electric field should span a range from approximately 0.5 kV/cm to 30 kV/cm, with at least 10 data points distributed across the range, including the region where velocity overshoot occurs.
- Current density vs. applied voltage for an n⁺nn⁺ GaAs structure (doping: n⁺ 2 × 10¹⁶ cm⁻³, n 1 × 10¹⁵ cm⁻³; lengths 0.5 µm / 7.5 µm / 0.5 µm) with ohmic contacts. The applied bias should span a range from 0 V to approximately 2.5 V, with at least 10 data points distributed across the range.

## Assets

- GaAs empirical pseudopotential form factors: 10.1103/PhysRev.141.789
- GaAs material parameters
- Goano incomplete Fermi‑Dirac integral algorithm: https://netlib.org/toms/745
- Standard numerical libraries (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Generate GaAs conduction band structure
- Role: process
- Action: Construct a tetrahedral mesh of the irreducible wedge of the fcc Brillouin zone; assign conduction‑band eigenenergies using the empirical pseudopotential method with GaAs form factors. Identify and label the Γ, L, and X valley regions. The resulting eigenenergies on the mesh serve as the basis for all subsequent isosurface and transport calculations.
- Evidence: `/app/outputs/band_structure_mesh.npy`

### Step 2: Compute raw isosurface‑integral spectra
- Role: process
- Action: From the mesh eigenenergies, extract constant‑energy isosurfaces for each valley (Γ, L, X). Numerically evaluate: (a) density‑of‑states spectra ρ_i(E), (b) phonon‑scattering isosurface integrals W_E^{YZ}(E) for optical deformation‑potential and polar‑optical mechanisms (using public material parameters and a single phonon energy of 36 meV), and (c) flux‑isosurface integrals μ_ij(E) = ∫ τ_k v²/3 ρ_k(E) dk, where τ_k is estimated from the scattering rates. Output raw numerical spectra as a CSV table.
- Evidence: `/app/outputs/isosurface_spectra_raw.csv`

### Step 3: Fit piecewise power‑laws to isosurface spectra
- Role: process
- Action: For each spectral function from step 2, partition the energy range into segments and fit power‑law parameters that reproduce the numerical spectra adequately: density‑of‑states (A, α, E_ρ), scattering (G, γ, E_s), and flux‑isosurface integrals (D, β, E_J). Write the fitted parameter tables as a structured JSON file.
- Evidence: `/app/outputs/powerlaw_parameters.json`

### Step 4: Simulate bulk electron drift velocity
- Role: scored (load-bearing)
- Action: Using the fitted power‑law parameters from step 3, set up the spatially homogeneous, constant‑field case for GaAs at 300 K (undoped, 1e13 cm⁻³ electron density). Assign six Fermi distributions (Γ₁, Γ₂, Γ₃, L₁, L₂, X) and solve the coupled continuity and energy conservation equations with only the drift component of the electron flux (zero divergences). For at least a set of electric field values spanning ~0.5–30 kV/cm, compute the total electron flux and derive the average drift velocity. Write the resulting (field, velocity) pairs.
- Output file: `/app/outputs/bulk_drift_velocity.csv`
- Format: csv
- Contract: Columns: electric_field_kV_cm (float), drift_velocity_cm_s (float). Rows for simulated field points spanning the range ~0.5–30 kV/cm.
- Scoring: scored by hidden verifier

### Step 5: Simulate n⁺nn⁺ device current‑voltage characteristics
- Role: scored
- Action: Set up a 1‑D mesh representing the n⁺nn⁺ GaAs structure (doping: n⁺ 2×10¹⁶ cm⁻³, n 10¹⁵ cm⁻³; lengths 0.5/7.5/0.5 µm) with ohmic contacts. Using the power‑law parameters from step 3, couple Gauss's law and the full transport equations (real‑space particle flux and kinetic‑energy flux, heat flow via the thermodynamic identity, and momentum‑space collision operators). Solve the nonlinear system with Newton iteration for a range of applied biases (e.g., 0–2.5 V). Compute the terminal current density for each bias and write the (voltage, current density) pairs.
- Output file: `/app/outputs/device_iv_curve.csv`
- Format: csv
- Contract: Columns: bias_voltage_V (float), current_density_A_cm2 (float). Rows for simulated bias points spanning the range ~0–2.5 V.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_drift_velocity.csv`
- `/app/outputs/device_iv_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_drift_velocity.csv
- path: `/app/outputs/bulk_drift_velocity.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Electron drift velocity vs. electric field for bulk GaAs at 300 K, simulated with the Fermi‑kinetics model. The hidden checker compares the reported pairs against expected reference values; a result that meets or improves upon the expected accuracy earns full credit.
- schema:
  - `type`: table
  - `required_columns`: `electric_field_kV_cm`, `drift_velocity_cm_s`
  - `units`:
    - `electric_field_kV_cm`: kV/cm
    - `drift_velocity_cm_s`: cm/s

### device_iv_curve.csv
- path: `/app/outputs/device_iv_curve.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Current density vs. applied voltage for the n⁺nn⁺ GaAs structure, simulated with the fully coupled Fermi‑kinetics device solver. The hidden checker compares the reported pairs against expected reference values; a result that meets or improves upon the expected accuracy earns full credit.
- schema:
  - `type`: table
  - `required_columns`: `bias_voltage_V`, `current_density_A_cm2`
  - `units`:
    - `bias_voltage_V`: V
    - `current_density_A_cm2`: A/cm²

Notes: All outputs are deterministic computational results from public inputs. The solver must implement the full pipeline (band structure → isosurfaces → power‑law fits → transport simulations) without relying on pre‑computed data. The tolerance policies are threshold_or_better, meaning the hidden checker will verify that each data point lies within an acceptable margin of the expected reference values; exceeding that margin reduces the score proportionally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_drift_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_kV_cm",
          "drift_velocity_cm_s"
        ],
        "units": {
          "electric_field_kV_cm": "kV/cm",
          "drift_velocity_cm_s": "cm/s"
        }
      },
      "description": "Electron drift velocity vs. electric field for bulk GaAs at 300 K, simulated with the Fermi‑kinetics model. The hidden checker compares the reported pairs against expected reference values; a result that meets or improves upon the expected accuracy earns full credit."
    },
    {
      "file": "device_iv_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "bias_voltage_V",
          "current_density_A_cm2"
        ],
        "units": {
          "bias_voltage_V": "V",
          "current_density_A_cm2": "A/cm²"
        }
      },
      "description": "Current density vs. applied voltage for the n⁺nn⁺ GaAs structure, simulated with the fully coupled Fermi‑kinetics device solver. The hidden checker compares the reported pairs against expected reference values; a result that meets or improves upon the expected accuracy earns full credit."
    }
  ],
  "notes": "All outputs are deterministic computational results from public inputs. The solver must implement the full pipeline (band structure → isosurfaces → power‑law fits → transport simulations) without relying on pre‑computed data. The tolerance policies are threshold_or_better, meaning the hidden checker will verify that each data point lies within an acceptable margin of the expected reference values; exceeding that margin reduces the score proportionally."
}
```

## How you are scored
A hidden verifier reads your two CSV files. For the drift‑velocity curve it checks that an overshoot peak appears in the correct field region and that the velocity at the provided field points lies within expected ranges consistent with the physics of GaAs hot‑electron transport. For the device I‑V it checks that the current density increases monotonically and that the values at the specified bias voltages lie within expected ranges. Each CSV is scored independently, and the two scores are combined to produce the final reward. You do not need to hit any exact reference numbers—an independent re‑implementation will differ slightly, so the tolerances are generous enough to accommodate legitimate tool‑chain spread. Presenting a physically implausible curve (e.g., no velocity overshoot, non‑monotonic I‑V) will be penalised.
