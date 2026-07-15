# DFT study of V12 vacancy cluster in Gd-implanted GaN

## Problem background
Gadolinium-implanted gallium nitride is a candidate dilute magnetic semiconductor, but the microscopic origin of its magnetic response is debated. Positron annihilation spectroscopy experiments suggest that post-implantation annealing creates vacancy clusters containing at least 12 vacancies (V12 clusters). First-principles calculations are needed to compute the positron annihilation characteristics of these clusters and to determine whether they can host spin-polarized electrons. This task reproduces the density functional theory (DFT) calculations that model the Doppler broadening of annihilation radiation (DBAR) and magnetic Doppler broadening (MDB) spectra for V12 clusters, and extracts the spontaneous magnetization of a double-V12 configuration.

## Approach
The method uses spin-polarized DFT with a Hubbard U correction (DFT+U) within the generalized gradient approximation, employing the ABINIT code with projector augmented-wave (PAW) pseudopotentials. A Hubbard U and J are applied to the Gd 4f electrons. Three supercells of wurtzite GaN are constructed: a pristine 4×2×2 cell, the same cell with a V12 vacancy cluster (removing 6 Ga and 6 N atoms in a compact void), and a cell containing two separated V12 clusters (double-V12) to induce a net magnetization. Atomic positions are relaxed while the lattice parameters are held fixed at experimental values. After self-consistent electronic structure calculations obtain the ground-state electron and spin densities, two-component DFT is used to compute positron wave functions with the Borónski-Nieminen enhancement factor. One-dimensional angular correlation of annihilation radiation spectra are obtained from the momentum density and convoluted with a Gaussian resolution function to produce DBAR spectra. The ratio spectrum N(p)/N_ref(p) is formed using the pristine cell as reference. For the double-V12 cell, spin-resolved positron annihilation spectra are computed from the spin-polarized electron density to obtain the differential spectrum N+(p)−N−(p). The total magnetization of the double-V12 supercell is extracted from the spin density.

## Reproduction target
Produce three scored artifacts: (1) the DBAR ratio spectrum of the V12 cluster relative to pristine GaN, saved as a two-column CSV (momentum in units of m0c, ratio dimensionless); (2) the MDB differential spectrum N+(p)−N−(p) for the double-V12 supercell, saved as a two-column CSV (momentum, differential intensity); (3) the total magnetization of the double-V12 supercell in units of µ_B, saved as a single float in a text file. The spectra should cover the momentum range from 0 to approximately 20×10^{-3} m0c with sufficient resolution (~0.1×10^{-3} m0c step) so that the shape is well resolved.

## Assets

- ABINIT 8.10.3: https://www.abinit.org/
- PAW pseudopotential for Ga (Ga-d-sp.in): https://www.abinit.org/downloads/PAW2/Ga-d-sp.in
- PAW pseudopotential for N (N-sp.in): https://www.abinit.org/downloads/PAW2/N-sp.in
- PAW pseudopotential for Gd (Gd-f-sp.in): https://www.abinit.org/downloads/PAW2/Gd-f-sp.in
- Clementi-Roetti Slater basis sets: 10.1016/0092-640X(74)90048-9
- Python packages: numpy, scipy, matplotlib: numpy scipy matplotlib

## Workflow steps

### Step 1: Build defect supercells
- Role: process
- Action: Construct the initial atomic structures for: (1) pristine 4×2×2 wurtzite GaN supercell (128 atoms), (2) the same supercell with a V12 vacancy cluster (removing 6 Ga and 6 N atoms according to the compact void geometry shown in the paper), and (3) a supercell containing two separated V12 clusters (double-cluster configuration) to induce spontaneous magnetization. Use the experimental lattice constants a=3.189 Å, c=5.185 Å, space group P6₃mc. Output coordinate files in ABINIT format.
- Evidence: `/app/outputs/step_01_supercells.in`

### Step 2: DFT+U relaxation and electronic structure
- Role: process
- Action: For each of the three supercells (pristine, V12, double-V12), perform spin-polarized DFT+U calculations using ABINIT with GGA functional, PAW pseudopotentials, and for Gd atoms Hubbard U=6.7 eV, J=0.7 eV. Relax atomic positions while keeping cell parameters fixed. After relaxation, perform a self-consistent field calculation to obtain ground-state electron density, spin density, and magnetic moments. Produce the total energy and magnetization for the double-V12 cell. This step is required to obtain the electron density and spin density needed for positron calculations.
- Evidence: `/app/outputs/step_02_dft_output.log`

### Step 3: Positron DBAR spectrum for pristine and V12
- Role: process
- Action: For the pristine supercell and the V12 supercell (from step_02), perform two-component DFT positron calculations as implemented in ABINIT. Compute the positron wave function self-consistently using the Borónski-Nieminen enhancement factor. Obtain the one-dimensional angular correlation of annihilation radiation (ACAR) spectrum. Convolve with a Gaussian resolution function (FWHM=3.92×10⁻³ m₀c) to get the DBAR spectrum. Save the raw spectra (momentum vs. intensity) for both systems.
- Evidence: `/app/outputs/step_03_raw_dbar_pristine.csv, step_03_raw_dbar_v12.csv`

### Step 4: Produce DBAR ratio spectrum
- Role: scored
- Action: Compute the ratio spectrum N(p)/N_ref(p) using the pristine DBAR spectrum as N_ref. Interpolate onto a uniform momentum grid from 0 to ~20×10⁻³ m₀c with step ~0.1×10⁻³ m₀c. Write two columns: momentum (in units of m₀c) and ratio.
- Output file: `/app/outputs/v12_dbar_ratio.csv`
- Format: csv
- Contract: Two columns: 'momentum' (float, unit m₀c) and 'ratio' (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Produce MDB differential spectrum
- Role: scored
- Action: For the double-V12 supercell, using the spin density from step_02, compute the spin-resolved positron annihilation spectra N+(p) and N−(p) corresponding to the majority and minority spin channels. The paper uses spin-polarized positron beam simulation; in practice, treat the positron annihilation with the spin-polarized electron density. Produce the differential spectrum N+(p) − N−(p). Output two columns: momentum (m₀c) and differential intensity.
- Output file: `/app/outputs/v12_mdb_differential.csv`
- Format: csv
- Contract: Two columns: 'momentum' (float, unit m₀c) and 'differential_intensity' (float).
- Scoring: scored by hidden verifier

### Step 6: Extract magnetization
- Role: scored (load-bearing)
- Action: From the DFT calculation of step_02 (double-V12 cell), extract the total magnetization of the cell (in units of µB). Output this value as a single float in a text file.
- Output file: `/app/outputs/v12_magnetization.txt`
- Format: txt
- Contract: A single floating-point number representing total magnetization in µB.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/v12_dbar_ratio.csv`
- `/app/outputs/v12_mdb_differential.csv`
- `/app/outputs/v12_magnetization.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### v12_dbar_ratio.csv
- path: `/app/outputs/v12_dbar_ratio.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: DBAR ratio spectrum N(p)/N_ref(p) of the V12 vacancy cluster. The verifier compares intensity values against hidden reference data using a tolerance‑based metric.
- schema:
  - `type`: table
  - `required_columns`: `momentum`, `ratio`
  - `units`:
    - `momentum`: m₀c
    - `ratio`: dimensionless
  - `description`: One column 'momentum' (float, unit m₀c) and one column 'ratio' (float).

### v12_mdb_differential.csv
- path: `/app/outputs/v12_mdb_differential.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: MDB differential spectrum N+(p) − N−(p) of the V12 cluster. The verifier compares intensity values against hidden reference data using a tolerance‑based metric.
- schema:
  - `type`: table
  - `required_columns`: `momentum`, `differential_intensity`
  - `units`:
    - `momentum`: m₀c
    - `differential_intensity`: arbitrary
  - `description`: One column 'momentum' (float, unit m₀c) and one column 'differential_intensity' (float).

### v12_magnetization.txt
- path: `/app/outputs/v12_magnetization.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Spontaneous magnetization of the double-V12 supercell. The verifier checks the agent’s value against a hidden reference within a small tolerance.
- schema:
  - `type`: text
  - `contents`: single float in µB
  - `description`: A single floating‑point number representing the total magnetization of the double‑V12 supercell.

Notes: All outputs are required. The DBAR and MDB curves must cover the momentum range 0 to ~20×10⁻³ m₀c with sufficient resolution (~0.1×10⁻³ m₀c). Hidden reference values are derived from the published theoretical curves.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "v12_dbar_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "momentum",
          "ratio"
        ],
        "units": {
          "momentum": "m₀c",
          "ratio": "dimensionless"
        },
        "description": "One column 'momentum' (float, unit m₀c) and one column 'ratio' (float)."
      },
      "description": "DBAR ratio spectrum N(p)/N_ref(p) of the V12 vacancy cluster. The verifier compares intensity values against hidden reference data using a tolerance‑based metric."
    },
    {
      "file": "v12_mdb_differential.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "momentum",
          "differential_intensity"
        ],
        "units": {
          "momentum": "m₀c",
          "differential_intensity": "arbitrary"
        },
        "description": "One column 'momentum' (float, unit m₀c) and one column 'differential_intensity' (float)."
      },
      "description": "MDB differential spectrum N+(p) − N−(p) of the V12 cluster. The verifier compares intensity values against hidden reference data using a tolerance‑based metric."
    },
    {
      "file": "v12_magnetization.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "contents": "single float in µB",
        "description": "A single floating‑point number representing the total magnetization of the double‑V12 supercell."
      },
      "description": "Spontaneous magnetization of the double-V12 supercell. The verifier checks the agent’s value against a hidden reference within a small tolerance."
    }
  ],
  "notes": "All outputs are required. The DBAR and MDB curves must cover the momentum range 0 to ~20×10⁻³ m₀c with sufficient resolution (~0.1×10⁻³ m₀c). Hidden reference values are derived from the published theoretical curves."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each scored artifact. For the DBAR ratio and MDB differential spectra, the checker samples your provided momentum grid and compares the reported intensity values against hidden reference data derived from the original theoretical calculations. The scoring metric rewards agreement with those reference spectra. For the magnetization, the checker reads your reported value and compares it to a hidden reference value. You must execute the full computational workflow and write the resulting files under /app/outputs; merely restating the paper's reported numbers will not earn credit.
