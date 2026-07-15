# Acoustic Phonon LA/TA Ratio in GaAs Quantum Wells and Heterostructures

## Problem background
In a hot two-dimensional electron gas (2DEG) formed in GaAs/AlGaAs heterostructures and quantum wells, the dominant energy relaxation at low temperatures occurs via emission of acoustic phonons. Understanding the angular and mode (longitudinal vs. transverse) distribution of these emitted phonons is essential for interpreting heat-pulse experiments and for designing hot-electron devices. Early theoretical models failed to explain the observed suppression of longitudinal acoustic (LA) phonons near the [100] direction, predicting instead a strong LA signal. This discrepancy motivated the development of a comprehensive model that includes the anisotropic electron-phonon matrix elements, dynamical RPA screening, finite 2DEG thickness through wavefunction form factors, and acoustic phonon focusing in the GaAs substrate.

The central quantity of interest is the LA/TA phonon emission ratio detected on the opposite side of the substrate. By computing this ratio for several quantum well widths and for a heterostructure, one can assess the importance of the above physical ingredients and compare with the experimentally observed trend.

## Approach
The reproduction implements the theoretical model described in the literature. The core idea is a linear response formalism for acoustic phonon emission by a quasi-2D electron gas at a hot-electron temperature Te > T_lattice. The model accounts for:

- **Phonon properties**: solving the Christoffel equation with the elastic constants of GaAs to obtain anisotropic phonon frequencies, group velocities, phase velocities, polarization vectors, and phonon focusing factors for the three acoustic branches. This step maps wavevector space to real-space propagation directions.
- **Form factors**: computing the ground-state electron wavefunction in a finite-depth confining potential (square well for quantum wells, triangular-like for the heterostructure) and evaluating the form factors G(q⟂) and g(q∥) that describe the finite extension of the 2DEG perpendicular to the plane.
- **RPA dynamical screening**: evaluating the finite-temperature polarizability of a non-interacting 2DEG and the full RPA dielectric function, including the Coulomb interaction and the form factor g(q∥). The result enters the emission rate as the screened spectral function Im{χ/(1−v g χ)}.
- **Directional emission**: evaluating the emitted power per solid angle for each acoustic mode by combining the electron-phonon matrix element (deformation potential ΞD and piezoelectric coupling h14) with the focusing factors, summing over all wavevector directions whose group velocity points to that real-space direction.
- **Detector geometry**: projecting the flux onto the (001) wafer surface and integrating over a rectangular detector window (100×10 µm) located centrally opposite a 120×50 µm 2DEG on a substrate of thickness 0.4 mm.

The workflow chains these components into four sequential steps that produce the final LA/TA ratios.

## Reproduction target
Compute the LA/TA phonon emission ratio for the following five device structures on a (001) GaAs substrate, all at an electron temperature Te = 50 K:

- Quantum wells of widths 5.1, 6.8, 12, and 15 nm with a finite square confining potential of depth 350 meV, having 2DEG densities 1.8, 2.0, 3.7, and 3.6 ×10^15 m^−2, respectively.
- A GaAs/AlGaAs heterostructure with a conduction band offset of 225 meV and a 2DEG density of 2.8 ×10^15 m^−2.

Use the deformation potential ΞD = 9 eV and the piezoelectric constant h14 = 1.4 ×10^9 eV/m. The phonon emission is recorded by a detector of 100×10 µm placed on the opposite side of a 0.4 mm thick substrate, directly opposite a 120×50 µm 2DEG. For each structure, compute the total LA and TA signals by integrating the directional emitted flux over the detector area, and take the ratio LA/TA.

Output a CSV file `/app/outputs/la_ta_ratios.csv` with columns: structure, well_width_nm, density_10_15_m2, la_ta_ratio. Include exactly one row per structure (for the heterostructure, enter an empty value for well_width_nm).

## Assets

- NumPy: numpy
- SciPy: scipy
- GaAs elastic constants

## Workflow steps

### Step 1: Compute anisotropic phonon properties for GaAs
- Role: process
- Action: Using the GaAs elastic constants (C11=11.88e10 Pa, C12=5.38e10 Pa, C44=5.94e10 Pa), numerically solve the Christoffel equation for a dense grid of wavevector directions to obtain acoustic phonon frequencies, group velocities, phase velocities, polarization vectors, and phonon focusing factors for all three acoustic modes (LA, fast TA, slow TA). This precomputation is required for the emission model to map wavevector directions to real-space group velocity directions.
- Evidence: `/app/outputs/phonon_properties.npy`

### Step 2: Compute electron wavefunction form factors
- Role: process
- Action: For each of the five device structures (quantum well widths 5.1, 6.8, 12, 15 nm with a finite confinement potential of 350 meV, and a heterostructure with a conduction band offset of 225 meV), solve the effective-mass Schrödinger equation to obtain the electron ground-state wavefunction. Then compute the form factors G(q⊥) and g(q||) that account for the finite extension of the 2DEG perpendicular to the plane. Use the GaAs electron effective mass of 0.067 m_e.
- Evidence: `/app/outputs/form_factors.npz`

### Step 3: Compute RPA dynamical screening
- Role: process
- Action: For each structure and electron temperature T_e=50 K, compute the finite-temperature dynamic polarizability function χ_{T_e}(ω, q||) of a non-interacting 2DEG and then the RPA dielectric function. Use the same effective mass and the form factor g(q||) from step_02. Evaluate the screening function Im{χ/(1 - v g χ)} over the frequency and in-plane wavevector ranges needed for the emission rate integral (Eq. 3 of the model).
- Evidence: `/app/outputs/screening_data.npy`

### Step 4: Compute LA/TA phonon ratio for all structures and export CSV
- Role: scored (load-bearing)
- Action: Using the phonon properties from step_01, form factors from step_02, and screening factors from step_03, implement the directional acoustic phonon emission model. For each structure, evaluate the emitted power per solid angle (Eq. 3) for LA and TA modes, accounting for phonon focusing and the electron-phonon matrix element (deformation potential Ξ_D=9 eV, piezoelectric constant h_14=1.4e9 eV/m). Map wavevector directions to real-space group velocity directions using the focusing factors. Project the flux onto the (001) surface and integrate over a detector window of 100×10 µm centrally opposite a 120×50 µm 2DEG on a 0.4 mm thick substrate. Compute the total LA and TA signals and calculate the LA/TA ratio. Output a CSV file with one row for each of the five structures: quantum wells of 5.1 nm (density 1.8e15 m^{-2}), 6.8 nm (2.0e15), 12 nm (3.7e15), 15 nm (3.6e15), and the heterostructure (2.8e15).
- Output file: `/app/outputs/la_ta_ratios.csv`
- Format: csv
- Contract: CSV with header structure,well_width_nm,density_10_15_m2,la_ta_ratio. Five rows, one per structure: e.g., '5.1nm',5.1,1.8,<ratio>; for HET, well_width_nm is empty.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/la_ta_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### la_ta_ratios.csv
- path: `/app/outputs/la_ta_ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: LA/TA phonon emission ratio for five device structures (QW 5.1, 6.8, 12, 15 nm and heterostructure) computed by the theoretical model. The hidden checker compares each ratio against the paper-reported gold value with an appropriate tolerance and verifies the monotonic trend of decreasing ratio with increasing well width.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `well_width_nm`, `density_10_15_m2`, `la_ta_ratio`
  - `units`:
    - `la_ta_ratio`: dimensionless

Notes: Only the LA/TA ratio is scored; the checker will use a hidden tolerance (e.g., relative 25% or absolute 0.1, whichever is larger) and a structural check that the ratio decreases monotonically with well width. The heterostructure row may have a NaN well_width_nm.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "la_ta_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "well_width_nm",
          "density_10_15_m2",
          "la_ta_ratio"
        ],
        "units": {
          "la_ta_ratio": "dimensionless"
        }
      },
      "description": "LA/TA phonon emission ratio for five device structures (QW 5.1, 6.8, 12, 15 nm and heterostructure) computed by the theoretical model. The hidden checker compares each ratio against the paper-reported gold value with an appropriate tolerance and verifies the monotonic trend of decreasing ratio with increasing well width."
    }
  ],
  "notes": "Only the LA/TA ratio is scored; the checker will use a hidden tolerance (e.g., relative 25% or absolute 0.1, whichever is larger) and a structural check that the ratio decreases monotonically with well width. The heterostructure row may have a NaN well_width_nm."
}
```

## How you are scored
Your submission is scored by a hidden verifier that examines the artifacts you write under `/app/outputs`. The primary scored artifact is `la_ta_ratios.csv`. The verifier reads the reported LA/TA ratios for the five structures and compares them against the expected theoretical values using appropriate numerical tolerances. The verifier also checks that the results exhibit self-consistent physical trends (e.g., the dependence on well width) expected from the model.

Merely typing in some numbers without running the full computational workflow will not satisfy the verifier. The scoring rewards correct implementation of the model; each step of the workflow must be executed to obtain the intermediate quantities needed to compute the final ratios. No paper-specific gold values or tolerances are revealed here—the checker's hidden reference is derived from the physical model you are tasked to implement.
