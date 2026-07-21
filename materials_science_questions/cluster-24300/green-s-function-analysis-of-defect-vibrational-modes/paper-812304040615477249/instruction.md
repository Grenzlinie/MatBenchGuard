# Mean-Square Displacement Computation for an F⁻ Interstitial in CaF₂ via Lattice Green's Functions

## Problem background
The mean-square displacements of atoms in a crystal are fundamental to understanding thermal vibrations, diffusion, and phase stability. In fluorite-structured CaF₂, F⁻ interstitials are crucial for ionic transport and the anomalous increase of mean-square displacements observed at high temperatures. This task computes the mean-square displacement B‑values (B = 8π²/3 ⟨u²⟩) for an F⁻ interstitial and its nearest neighbour host ions using lattice Green's functions and scattering‑matrix theory. The results are to be compared with the corresponding values for host ions in a perfect CaF₂ lattice, providing insight into how the defect environment modifies vibrational amplitudes.

## Approach
The harmonic lattice dynamics of CaF₂ are described by a shell‑model phonon dispersion (Elcombe and Pryor 1970). The dynamical matrix yields the host Green's function g(ω) restricted to a defect space containing the interstitial and 14 nearest neighbours (8 F⁻ and 6 Ca²⁺). Interatomic forces are taken from the Catlow–Norgett potential (1973), which allows relaxation of the host ions and construction of the deformation matrix δl and the coupling matrix a that connect the lattice displacements to the interstitial.

The interstitial is treated as an added degree of freedom with mass mI and a frozen‑lattice frequency ωI, defining its Green's function γ(ω). The combined perturbation δl′ = δl + a γ aᵀ is introduced, and the scattering matrix t = δl′ (I − g δl′)^(-1) is computed. For each normal‑mode frequency, incident plane‑wave displacements u₁⁰ are scattered to give the host‑atom displacement vector u₁ = (I + g t) u₁⁰ and the interstitial displacement ξ = −γ aᵀ u₁.

Squared displacement amplitudes u₁²(k,ω) and ξ²(ω) are integrated over frequency with the thermal occupation factor coth(ħω/2kT) to obtain mean‑square displacements ⟨u²⟩ and the conventional B‑values. The harmonic approximation (HA) is applied from 50 K to 500 K. For higher temperatures (300, 1000, 1500 K), the quasiharmonic approximation (QHA) is implemented: the lattice constant is scaled using the thermal expansion coefficient, and mode Grüneisen parameters are used to shift phonon frequencies. The Green's functions are rescaled appropriately for consistency.

## Reproduction target
Produce a CSV file at `/app/outputs/b_values.csv` with the following columns:

- `temperature` (K)
- `approximation` (HA or QHA)
- `B_interstitial` (Å²)
- `B_F_D` (Å²) – B‑value of a first‑neighbour F⁻ ion in the defect region
- `B_Ca_D` (Å²) – B‑value of a second‑neighbour Ca²⁺ ion in the defect region
- `B_F_H` (Å²) – B‑value of a host F⁻ ion in a perfect CaF₂ lattice
- `B_Ca_H` (Å²) – B‑value of a host Ca²⁺ ion in a perfect CaF₂ lattice

The file must contain rows for temperatures 50 K, 100 K, …, 500 K (step 50 K) under HA; rows for 300 K, 1000 K, 1500 K under HA; and rows for the same three temperatures under QHA. All B‑values must be positive and physically reasonable. The hidden verifier will additionally check that the interstitial B‑value is substantially larger than the host fluorine B‑value (a ratio condition that reflects the enhanced motion of the interstitial).

## Assets

- Catlow-Norgett interatomic potential for CaF₂: https://doi.org/10.1088/0022-3719/6/8/001
- Shell-model phonon data for CaF₂ (Elcombe and Pryor 1970): https://doi.org/10.1088/0022-3719/3/3/015
- Crystal structure of CaF₂ (fluorite, Fm-3m, a≈5.463 Å)
- Mode Grüneisen parameters for CaF₂ (Govindarajan et al. 1979)
- Thermal expansion coefficient β for CaF₂

## Workflow steps

### Step 1: Lattice relaxation around F⁻ interstitial
- Role: process
- Action: Using the Catlow–Norgett interatomic potential, relax the positions of the 14 host ions (8 F⁻ first neighbours and 6 Ca²⁺ second neighbours) surrounding an F⁻ interstitial in CaF₂. The relaxation may be performed with an open-source lattice-statics code (e.g., GULP, LAMMPS).
- Evidence: `/app/outputs/relaxed_coords.txt`

### Step 2: Compute host Green's functions and defect perturbation matrices
- Role: process
- Action: From the shell-model phonon data of Elcombe–Pryor, compute the perfect-crystal phonon frequencies and eigenvectors for CaF₂. Construct the real-space Green’s function submatrix g(ω) for the defect space (42×42). Using the relaxed coordinates from step 1 and the Catlow–Norgett potential, compute the deformation matrix δl and coupling matrix a.
- Evidence: `/app/outputs/green_perturbation_data.npz`

### Step 3: Build scattering operators and compute displacement amplitudes
- Role: process
- Action: For a dense grid of reduced frequencies (approximately x = 0.01–0.99), compute the interstitial Green’s function γ(ω) using the interstitial mass and a frozen-lattice frequency estimate. Form the combined perturbation δl + a γ aᵀ, invert [I − g(δl + a γ aᵀ)], and obtain the scattered displacement vectors u₁(ω) and interstitial displacement ξ(ω). Evaluate and store the squared amplitudes u₁²(1,ω) and ξ²(ω).
- Evidence: `/app/outputs/displacement_amplitudes.npz`

### Step 4: Compute B-values and output final CSV
- Role: scored (load-bearing)
- Action: Integrate the displacement amplitudes using ⟨u²⟩ = (ħ/2) ∫ (u²(ω)/ω) coth(ħω/(2kT)) dω. Compute B = (8π²/3)⟨u²⟩ for temperatures 50 K to 500 K at 50 K intervals (harmonic approximation). For the quasiharmonic approximation, incorporate thermal expansion and mode-Grüneisen-parameter frequency shifts, scale the Green's functions accordingly, and recompute B-values at 300, 1000, 1500 K. Write all results to b_values.csv.
- Output file: `/app/outputs/b_values.csv`
- Format: csv
- Contract: CSV with columns: temperature (K), approximation (HA or QHA), B_interstitial (Å²), B_F_D (Å²), B_Ca_D (Å²), B_F_H (Å²), B_Ca_H (Å²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/b_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### b_values.csv
- path: `/app/outputs/b_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed B-values (B = 8π²/3 ⟨u²⟩) for the F⁻ interstitial, its host neighbours, and perfect lattice hosts under harmonic and quasiharmonic approximations. The checker compares each value to a hidden gold from the paper with a suitable tolerance and verifies the interstitial/ host C B ratio.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `approximation`, `B_interstitial`, `B_F_D`, `B_Ca_D`, `B_F_H`, `B_Ca_H`
  - `units`:
    - `temperature`: K
    - `B_interstitial`: Å²
    - `B_F_D`: Å²
    - `B_Ca_D`: Å²
    - `B_F_H`: Å²
    - `B_Ca_H`: Å²

Notes: The file must contain rows for temperatures 50, 100, 150, …, 500 K (approximation = HA) and for 300, 1000, 1500 K (approximation = HA and QHA). All B values are in Å².

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "b_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "approximation",
          "B_interstitial",
          "B_F_D",
          "B_Ca_D",
          "B_F_H",
          "B_Ca_H"
        ],
        "units": {
          "temperature": "K",
          "B_interstitial": "Å²",
          "B_F_D": "Å²",
          "B_Ca_D": "Å²",
          "B_F_H": "Å²",
          "B_Ca_H": "Å²"
        }
      },
      "description": "Computed B-values (B = 8π²/3 ⟨u²⟩) for the F⁻ interstitial, its host neighbours, and perfect lattice hosts under harmonic and quasiharmonic approximations. The checker compares each value to a hidden gold from the paper with a suitable tolerance and verifies the interstitial/ host C B ratio."
    }
  ],
  "notes": "The file must contain rows for temperatures 50, 100, 150, …, 500 K (approximation = HA) and for 300, 1000, 1500 K (approximation = HA and QHA). All B values are in Å²."
}
```

## How you are scored
A hidden verifier reads your `b_values.csv` and scores your submission. It compares each B‑value entry to reference benchmarks (derived from high‑quality independent calculations) with an appropriate tolerance. Your reward depends on how closely your computed values match these references. Additionally, the verifier checks the ratio between the interstitial B‑value and the host fluorine B‑value; the interstitial must exceed the host value by a substantial margin indicative of the interstitial’s enhanced dynamics. This ratio condition also contributes a portion of your score. The final reward is a weighted combination of these checks. You do not need to guess the reference values; a correct implementation of the physical model and numerical integration will naturally approach the reference numbers.
