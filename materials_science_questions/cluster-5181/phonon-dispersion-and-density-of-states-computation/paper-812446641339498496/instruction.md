# Phonon dispersion and density of states for Lennard-Jones f.c.c. crystal

## Problem background
For a monatomic face-centered-cubic (f.c.c.) crystal with atoms interacting via a Lennard-Jones potential, the harmonic phonon spectrum depends strongly on the lattice constant. This task computes the phonon dispersion curves and the phonon density of states (DOS) for two representative densities (σ/a = 1.30 and σ/a = 1.24) to reveal how the spectrum changes with density. The resulting frequency distributions and dispersion relations are fundamental for understanding thermodynamic properties of noble-gas solids and serve as a benchmark for anharmonic calculations.

## Approach
The phonon frequencies are obtained by constructing the dynamical matrix of the f.c.c. Lennard-Jones crystal in the harmonic approximation. The dynamical matrix is built from lattice sums over neighbour shells using the pair potential φ(r)=4ε[(σ/r)^12 – (σ/r)^6]. The lattice sums S_n^{αβ}(q) (Eq. (3) of the original work) and S_n(q) (Eq. (4)) are computed for every required wave vector q and for a converged set of neighbour shells. The 3×3 dynamical matrix D_{αβ}(q) (Eq. (2)) is then assembled and diagonalised to yield the three phonon frequencies at each q. All calculations are performed in reduced units (ε=1, σ=1, M=1); the lattice constant a is determined by the prescribed ratio σ/a. The workflow consists of three phases: (i) generating the f.c.c. neighbour shells and the required q‑point grids (one‑dimensional path from Γ to X for the dispersion curves and a dense irreducible Brillouin zone grid for the DOS); (ii) evaluating the lattice sums and the dynamical matrix for σ/a = 1.30 and 1.24, and diagonalising to obtain the frequencies; (iii) extracting the longitudinal and transverse branches along [100] for each density and binning the frequencies from the dense grid to produce the DOS histogram. The approach uses standard numerical linear algebra (NumPy/SciPy) and does not rely on any external datasets; all inputs are the lattice geometry and the known potential.

## Reproduction target
The goal is to compute and deliver three scored artifacts:

1. A CSV file (`step_02_dispersion_curves_sigma_a_1.30.csv`) containing the phonon dispersion curves along the [100] direction for σ/a = 1.30, reporting the reduced wave-vector coordinate q, the longitudinal frequency ω_L, and the transverse frequency ω_T (all in reduced units).

2. A CSV file (`step_03_dispersion_curves_sigma_a_1.24.csv`) with the same structure for σ/a = 1.24.

3. A CSV file (`step_04_frequency_distribution_sigma_a_1.30.csv`) containing the phonon density‑of‑states histogram for σ/a = 1.30, with columns `bin_start`, `bin_end`, and `count`.

The underlying requirement is that the phonon frequencies are correctly obtained from the Lennard‑Jones force‑constant model. The hidden verification will check that the dispersion curves follow the expected physical behaviour and that the DOS histogram exhibits the characteristic double‑peak structure, with the high‑frequency peak (longitudinal modes) at a higher frequency than the low‑frequency peak (transverse modes).

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Prepare f.c.c. lattice neighbor list and wave vector grid
- Role: process
- Action: Construct the f.c.c. lattice vectors, generate neighbor shells up to sufficient convergence, and create the set of wave vectors q along the [100] high-symmetry line from Γ to X (reduced coordinates from 0 to 1) as well as a dense sampling of the irreducible Brillouin zone for the density-of-states calculation.
- Evidence: none

### Step 2: Compute phonon frequencies for σ/a=1.30 and σ/a=1.24
- Role: process
- Action: For each target σ/a value (1.30 and 1.24), use the generated neighbor list and q-points to compute the lattice sums S_n^{αβ}(q) and S_n(q) as defined in the paper, assemble the 3×3 dynamical matrix D_{αβ}(q) using the Lennard-Jones force-constant formula, diagonalize the matrix for every q, and store the resulting phonon frequencies and wave vectors.
- Evidence: none

### Step 3: Extract dispersion curves along [100] for σ/a=1.30
- Role: scored
- Action: Extract the longitudinal and transverse phonon frequencies along the [100] direction for σ/a=1.30 and write the dispersion data to a CSV file.
- Output file: `/app/outputs/step_02_dispersion_curves_sigma_a_1.30.csv`
- Format: csv
- Contract: q (reduced coordinate, float), omega_L (longitudinal frequency in reduced units, float), omega_T (transverse frequency in reduced units, float)
- Scoring: scored by hidden verifier

### Step 4: Extract dispersion curves along [100] for σ/a=1.24
- Role: scored
- Action: Extract the longitudinal and transverse phonon frequencies along the [100] direction for σ/a=1.24 and write the dispersion data to a CSV file.
- Output file: `/app/outputs/step_03_dispersion_curves_sigma_a_1.24.csv`
- Format: csv
- Contract: q (reduced coordinate, float), omega_L (longitudinal frequency in reduced units, float), omega_T (transverse frequency in reduced units, float)
- Scoring: scored by hidden verifier

### Step 5: Compute phonon density of states for σ/a=1.30
- Role: scored (load-bearing)
- Action: Using the phonon frequencies computed for σ/a=1.30 over the dense irreducible Brillouin zone grid, bin the frequencies into a histogram representing the phonon density of states and write the histogram to a CSV file.
- Output file: `/app/outputs/step_04_frequency_distribution_sigma_a_1.30.csv`
- Format: csv
- Contract: bin_start (float, lower edge of frequency bin), bin_end (float, upper edge of frequency bin), count (int, number of states in that bin)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_dispersion_curves_sigma_a_1.30.csv`
- `/app/outputs/step_03_dispersion_curves_sigma_a_1.24.csv`
- `/app/outputs/step_04_frequency_distribution_sigma_a_1.30.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_dispersion_curves_sigma_a_1.30.csv
- path: `/app/outputs/step_02_dispersion_curves_sigma_a_1.30.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon dispersion curves for σ/a=1.30 along the [100] direction, used for comparison with hidden reference digitized from the paper's figure.
- schema:
  - `type`: table
  - `required_columns`: `q`, `omega_L`, `omega_T`

### step_03_dispersion_curves_sigma_a_1.24.csv
- path: `/app/outputs/step_03_dispersion_curves_sigma_a_1.24.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon dispersion curves for σ/a=1.24 along the [100] direction, used for comparison with hidden reference digitized from the paper's figure.
- schema:
  - `type`: table
  - `required_columns`: `q`, `omega_L`, `omega_T`

### step_04_frequency_distribution_sigma_a_1.30.csv
- path: `/app/outputs/step_04_frequency_distribution_sigma_a_1.30.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon density of states histogram for σ/a=1.30; auditor checks for a double-peak structure and that the longitudinal peak appears at higher frequency than the transverse peak.
- schema:
  - `type`: table
  - `required_columns`: `bin_start`, `bin_end`, `count`

Notes: All computed frequencies are in reduced units (Lennard-Jones parameters ε=1, σ=1, M=1). The agent must implement lattice sums and dynamical matrix assembly as described in the task instructions; no pre-computed data are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_dispersion_curves_sigma_a_1.30.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q",
          "omega_L",
          "omega_T"
        ]
      },
      "description": "Phonon dispersion curves for σ/a=1.30 along the [100] direction, used for comparison with hidden reference digitized from the paper's figure."
    },
    {
      "file": "step_03_dispersion_curves_sigma_a_1.24.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q",
          "omega_L",
          "omega_T"
        ]
      },
      "description": "Phonon dispersion curves for σ/a=1.24 along the [100] direction, used for comparison with hidden reference digitized from the paper's figure."
    },
    {
      "file": "step_04_frequency_distribution_sigma_a_1.30.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bin_start",
          "bin_end",
          "count"
        ]
      },
      "description": "Phonon density of states histogram for σ/a=1.30; auditor checks for a double-peak structure and that the longitudinal peak appears at higher frequency than the transverse peak."
    }
  ],
  "notes": "All computed frequencies are in reduced units (Lennard-Jones parameters ε=1, σ=1, M=1). The agent must implement lattice sums and dynamical matrix assembly as described in the task instructions; no pre-computed data are provided."
}
```

## How you are scored
A hidden verifier scores the three artifacts independently and combines them by weight into a final reward between 0 and 1.

- For the two dispersion‑curve CSVs, the verifier compares the reported frequencies (ω_L and ω_T at each q) to a hidden reference computed from a correct implementation of the same model. Small numerical differences (e.g., from lattice‑sum convergence threshold) are tolerated; large deviations, unphysical discontinuities, or wrong branch assignments reduce the score.

- For each DOS histogram, the verifier performs a structural audit that assesses the histogram's shape and spectral features against a hidden reference. A histogram whose spectral shape deviates significantly from the expected one receives a low score.

You must carry out the full computation yourself; reporting numbers that merely look plausible or copying values from an external source will not match the hidden reference and will be penalised.
