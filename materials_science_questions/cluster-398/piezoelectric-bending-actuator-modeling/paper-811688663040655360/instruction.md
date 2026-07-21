# Piezoelectric cylindrical shell transient response analysis

## Problem background
This task addresses the transient analysis of a multilayered piezoelectric cylindrical shell. The shell is composed of two layers of equal thickness: an inner layer made of PVDF and an outer layer made of PZT-5A. It is subjected to a coupled electro-mechanical excitation — a radial circular mechanical line load applied on the outer surface with a time history of one cycle of a sine function, together with an electrode excitation on the inner surface having a Heaviside step time history. The goal is to compute the resulting dynamic displacement and electrostatic potential fields throughout the shell.

## Approach
The method is a hybrid numerical-analytical approach. The cylindrical shell is discretized along the wall thickness using layered annular elements, each described by three annular nodal surfaces (inner, middle, outer) with quadratic shape functions. Hamilton's principle and the coupled electro-elastic constitutive relations are applied to derive element mass, stiffness, piezoelectric coupling, and dielectric matrices. After assembling the global system, the electrostatic degrees of freedom are condensed to obtain a reduced mechanical stiffness matrix and a corresponding mass matrix, both functions of the axial wave number (the problem is axisymmetric and the load is independent of the circumferential coordinate, so Fourier transformation is applied only in the axial direction). For each axial wave number, the reduced eigenvalue problem is solved, and modal superposition combined with a Duhamel integral yields the transient response in the wave-number domain under the given coupled loading (the electrode excitation is handled by a large-value modification of the dielectric stiffness matrix). Finally, an inverse Fourier transform (iFFT) returns the displacement and electrostatic potential to the space-time domain as functions of the dimensionless axial coordinate and time.

The material constants of the two layers are:

PZT-5A:
- Elastic constants C11=99.200, C22=99.200, C33=86.856, C12=54.016, C13=50.778, C23=21.100, C44=21.100, C55=21.100, C66=22.593 (all GPa)
- Piezoelectric coefficients e31=-7.209, e32=-7.209, e33=15.118, e24=12.320, e15=12.322 (C/m²)
- Dielectric constants g11=153.00, g22=153.00, g33=153.00 (×10⁻¹⁰ F/m)
- Density ρ=7.750×10³ kg/m³

PVDF:
- Elastic constants C11=238.240, C22=23.600, C33=10.640, C12=3.980, C13=2.190, C23=1.920, C44=2.150, C55=4.400, C66=6.430 (all GPa)
- Piezoelectric coefficients e31=-0.130, e32=-0.145, e33=-0.276, e24=-0.009, e15=-0.135 (C/m²)
- Dielectric constants g11=1.1068, g22=1.1068, g33=1.1068 (×10⁻¹⁰ F/m)
- Density ρ=7.800×10³ kg/m³

The outer radius is R₂ = 20 (dimensionless, after scaling by the thickness H). The simulation discretizes each lamina into four annular elements, resulting in 54 annular nodal surfaces in total. The mechanical line load is applied as a radial force distributed according to a delta function in the axial coordinate, with time history f(t) = sin(2πt/t_d) for 0 < t < t_d (t_d = 4 dimensionless units) and zero elsewhere. The inner-surface electrode potential is a step of amplitude 10 He_s q_0 δ(z) / (g_s c_{66}) (dimensionless).

## Reproduction target
You must compute and write three CSV files:

1. `radial_displacement_time_history.csv` — time histories of dimensionless radial displacement w̄ at the fixed axial coordinate z̄ = 10, on the inner, middle, and outer nodal surfaces. Columns: time (dimensionless t̄), w_inner, w_middle, w_outer.

2. `axial_displacement_spatial.csv` — spatial distribution of dimensionless axial displacement ū at time t̄ = 10, on the inner, middle, and outer surfaces. Columns: z (dimensionless z̄), u_inner, u_middle, u_outer.

3. `potential_spatial.csv` — spatial distribution of dimensionless electrostatic potential φ̄ at time t̄ = 10, on the inner, middle, and outer surfaces. Columns: z (dimensionless z̄), phi_inner, phi_middle, phi_outer.

The outputs must follow the exact schema and physical conditions described in the workflow steps and output contract.

## Assets

- Python 3.8+: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define geometry, materials, and discretization
- Role: process
- Action: Define the cylindrical shell geometry (inner and outer radii, thickness, equal-thickness layers), the material constants for PZT-5A and PVDF (elastic, piezoelectric, dielectric, density as given in the task description), the discretization into layered annular elements (4 elements per layer, 54 annular nodal surfaces total), and the loading conditions (mechanical radial line load with sine time history of duration t̄d=4, inner-surface electrode excitation with Heaviside step).
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Assemble wave-number-dependent reduced-order matrices
- Role: process
- Action: For a set of axial wave numbers k̄z, compute element stiffness, coupling, dielectric, and mass matrices using quadratic shape functions. Assemble global matrices A_t, C_t, G_t, and M_st. Apply electrostatic condensation to obtain the reduced mechanical stiffness K_st(k̄z) and mass M_st(k̄z).
- Evidence: `/app/outputs/sample_matrices.npz`

### Step 3: Solve eigenvalue problem for each wave number
- Role: process
- Action: For each k̄z, solve the eigenvalue problem K_st d = ω² M_st d to obtain eigenfrequencies and left/right eigenvectors. Retain a sufficient number of modes for modal superposition.
- Evidence: `/app/outputs/eigenvalues.csv`

### Step 4: Compute transient response in wave-number domain
- Role: process
- Action: Using modal superposition and Duhamel integral, compute the transformed displacement vector d_t(k̄z, t̄) and electrostatic potential φ_t(k̄z, t̄) for a dense time grid under the coupled mechanical and electrical loading. Handle electrode excitation via the large-value modification of the dielectric stiffness matrix.
- Evidence: `/app/outputs/transformed_response_sample.npy`

### Step 5: Inverse Fourier transform to space domain
- Role: process
- Action: Apply one-dimensional inverse FFT with respect to k̄z to obtain the axial distribution of displacement components ū, v̄, w̄ and electrostatic potential φ̄ as functions of dimensionless axial coordinate z̄ and time t̄.
- Evidence: `/app/outputs/fields.npz`

### Step 6: Extract radial displacement time histories
- Role: scored (load-bearing)
- Action: From the computed field data, extract dimensionless radial displacement w̄ at axial position z̄=10 on the inner, middle, and outer nodal surfaces as functions of dimensionless time t̄. Write radial_displacement_time_history.csv.
- Output file: `/app/outputs/radial_displacement_time_history.csv`
- Format: csv
- Contract: time (dimensionless t̄), w_inner, w_middle, w_outer
- Scoring: scored by hidden verifier

### Step 7: Extract axial displacement spatial distribution
- Role: scored
- Action: From the computed field data, extract dimensionless axial displacement ū as a function of dimensionless z̄ at time t̄=10 on the inner, middle, and outer surfaces. Write axial_displacement_spatial.csv.
- Output file: `/app/outputs/axial_displacement_spatial.csv`
- Format: csv
- Contract: z (dimensionless z̄), u_inner, u_middle, u_outer
- Scoring: scored by hidden verifier

### Step 8: Extract electrostatic potential spatial distribution
- Role: scored
- Action: From the computed field data, extract dimensionless electrostatic potential φ̄ as a function of dimensionless z̄ at time t̄=10 on the inner, middle, and outer surfaces. Write potential_spatial.csv.
- Output file: `/app/outputs/potential_spatial.csv`
- Format: csv
- Contract: z (dimensionless z̄), phi_inner, phi_middle, phi_outer
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/radial_displacement_time_history.csv`
- `/app/outputs/axial_displacement_spatial.csv`
- `/app/outputs/potential_spatial.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### radial_displacement_time_history.csv
- path: `/app/outputs/radial_displacement_time_history.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time histories of dimensionless radial displacement w̄ at z̄=10 on inner, middle, and outer surfaces.
- schema:
  - `type`: table
  - `required_columns`: `time`, `w_inner`, `w_middle`, `w_outer`

### axial_displacement_spatial.csv
- path: `/app/outputs/axial_displacement_spatial.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spatial distribution of dimensionless axial displacement ū at t̄=10 on inner, middle, and outer surfaces.
- schema:
  - `type`: table
  - `required_columns`: `z`, `u_inner`, `u_middle`, `u_outer`

### potential_spatial.csv
- path: `/app/outputs/potential_spatial.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spatial distribution of dimensionless electrostatic potential φ̄ at t̄=10 on inner, middle, and outer surfaces.
- schema:
  - `type`: table
  - `required_columns`: `z`, `phi_inner`, `phi_middle`, `phi_outer`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "radial_displacement_time_history.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "w_inner",
          "w_middle",
          "w_outer"
        ]
      },
      "description": "Time histories of dimensionless radial displacement w̄ at z̄=10 on inner, middle, and outer surfaces."
    },
    {
      "file": "axial_displacement_spatial.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "u_inner",
          "u_middle",
          "u_outer"
        ]
      },
      "description": "Spatial distribution of dimensionless axial displacement ū at t̄=10 on inner, middle, and outer surfaces."
    },
    {
      "file": "potential_spatial.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "phi_inner",
          "phi_middle",
          "phi_outer"
        ]
      },
      "description": "Spatial distribution of dimensionless electrostatic potential φ̄ at t̄=10 on inner, middle, and outer surfaces."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier checks each scored output file independently. It compares your computed field values to a set of reference data points for the corresponding quantities (the same coordinate/time points and surfaces). Each file is scored as the fraction of sampled points whose difference from the reference falls within an acceptable tolerance. The final reward is the weighted average of the scores for the three output files. Submitting plausible numbers without executing the required computational pipeline will not pass this verification.
