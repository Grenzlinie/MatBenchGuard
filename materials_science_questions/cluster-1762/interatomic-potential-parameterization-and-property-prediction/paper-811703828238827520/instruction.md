# Molecular Dynamics and Ab Initio EXAFS Modeling of Perovskite LaCoO₃

## Problem background
Perovskite-structured LaCoO₃ is a promising mixed ionic–electronic conductor for solid-oxide fuel cells, oxygen-permeation membranes, and catalysts. Its functional properties are tightly coupled to local atomic structure and thermal disorder. Co K-edge extended X-ray absorption fine structure (EXAFS) is a powerful probe of the local environment around cobalt, but extracting reliable interatomic distances and disorder parameters is challenging because the spectrum contains strong contributions from multiple-scattering (many-body) events beyond the first coordination shell. A recent computational approach addresses this by combining classical molecular dynamics (MD) simulations with ab initio multiple-scattering EXAFS theory: the MD provides realistic thermal displacements, and the multiple-scattering calculation accounts for all relevant scattering paths. The present task is to implement this combined MD+MS pipeline and compute the temperature-dependent structural parameters (interatomic distances and mean-square relative displacements) for the first six coordination shells around cobalt, together with the configuration-averaged EXAFS Fourier transforms at 180 K, 300 K, and 400 K.

## Approach
The method rests on two sequential computations. First, classical NVT molecular dynamics are performed using a rigid-ion force field that describes La–O, Co–O, and O–O pairwise interactions via a Buckingham potential, plus a three-body harmonic term (Co–O–Co) that captures the rotational stiffness of the CoO₆ octahedra. The simulations use experimentally determined lattice parameters at each temperature and produce atomic trajectories in a 5×5×5 supercell. From these trajectories, radial distribution functions are computed and the mean distances R and mean-square relative displacements σ² are extracted for the six nearest coordination shells (O₁, La₂, Co₃, O₄, O₅, Co₆). Second, each instantaneous atomic configuration from the MD production run is fed into an ab initio multiple-scattering code (FEFF8 or equivalent). The scattering potential is calculated for a cluster of radius 8 Å centered on the absorbing Co atom, and the EXAFS χ(k) is computed including all multiple-scattering paths up to the 6th order with a half-path length limit of 6 Å. The individual spectra are arithmetically averaged to obtain the configuration-averaged χ(k)k², which is then Fourier transformed over the k-range 3–12 Å⁻¹ to yield the magnitude and imaginary parts as functions of distance R. The task also explores the sensitivity of the results to the ion charges by testing different charge assignments, and contrasts the full multiple-scattering result with a single-scattering-only calculation to highlight the importance of many-body effects.

### Force-field parameters

The rigid-ion force field is defined by the following parameters (ion charges Z, Buckingham two-body terms, and a harmonic three-body term).

**Ion charges:**
- La³⁺, Co¹·³⁵⁺, O¹·⁴⁵⁻

**Buckingham two-body potential (cutoff 20 Å):**

| Interaction | A (eV) | ρ (Å) | C (eV·Å⁶) |
|---|---|---|---|
| La³⁺–O¹·⁴⁵⁻ | 1357.85 | 0.3456 | 0.0 |
| Co¹·³⁵⁺–O¹·⁴⁵⁻ | 961.199 | 0.2795 | 0.0 |
| O¹·⁴⁵⁻–O¹·⁴⁵⁻ | 22750.7 | 0.0552 | 37.01 |

**Three-body harmonic potential (Co–O–Co):**
- Force constant k = 347.67 eV/rad²
- Equilibrium angle θ₀ = 163.79°

## Reproduction target
Deliver two sets of data products. (1) A CSV file containing the MD-derived structural parameters for the first six coordination shells around cobalt at all three temperatures: coordination number N, mean distance R (in Å), and mean-square relative displacement σ² (in Å²). (2) Three CSV files, one per temperature (180 K, 300 K, 400 K), each containing the Fourier transform of the configuration-averaged k²-weighted EXAFS: the radial distance R (in Å), the FT magnitude, and the imaginary part (both in arbitrary units). Provide these files under /app/outputs with the exact filenames specified in the output contract.

## Assets

- Molecular dynamics code (GULP or LAMMPS): https://gulp.curtin.edu.au
- Multiple-scattering EXAFS code (FEFF8): https://feff.uw.edu
- Crystal structure reference for rhombohedral LaCoO₃: 10.1103/PhysRevB.66.094408
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: NVT molecular dynamics ensemble generation
- Role: process
- Action: Perform classical NVT molecular dynamics simulations for LaCoO₃ at 180 K, 300 K, and 400 K using the provided force-field parameters and experimental lattice constants from the crystal structure reference. Use a 5a×5a×5a supercell (1250 atoms), time step 0.5 fs, 20 ps equilibration, 20 ps production. Save atomic trajectories for subsequent analysis.
- Evidence: `/app/outputs/md_trajectories.log`

### Step 2: Radial distribution function and structural parameter extraction
- Role: process
- Action: From the MD trajectories, compute total and partial radial distribution functions and extract structural parameters (mean interatomic distances R and mean-square relative displacements σ²) for the first six coordination shells around cobalt (O₁, La₂, Co₃, O₄, O₅, Co₆) at each temperature.
- Evidence: `/app/outputs/rdf_analysis.txt`

### Step 3: Output MD structural parameters
- Role: scored
- Action: Write the extracted structural parameters to a single CSV file covering all three temperatures.
- Output file: `/app/outputs/md_structural_params.csv`
- Format: csv
- Contract: Columns: temperature (float), shell (string), N (int), R (float), sigma2 (float)
- Scoring: scored by hidden verifier

### Step 4: Ab initio multiple-scattering EXAFS calculations
- Role: process
- Action: For each instantaneous configuration in the MD production runs, compute the EXAFS χ(k)k² spectrum using FEFF8 with a scattering cluster radius of 8 Å, multiple-scattering contributions up to 6th order with half-path length up to 6 Å, and Hedin-Lundqvist exchange-correlation potential.
- Evidence: `/app/outputs/feff_log.txt`

### Step 5: Configuration-averaged EXAFS and Fourier transform at 180 K
- Role: scored (load-bearing)
- Action: Arithmetically average χ(k)k² over the MD configurations at 180 K, compute the Fourier transform over the k-range 3–12 Å⁻¹, and write the R-dependent magnitude and imaginary part to a CSV file.
- Output file: `/app/outputs/exafs_ft_180K.csv`
- Format: csv
- Contract: Columns: R (float), FT_magnitude (float), FT_imag (float)
- Scoring: scored by hidden verifier

### Step 6: Configuration-averaged EXAFS and Fourier transform at 300 K
- Role: scored (load-bearing)
- Action: Arithmetically average χ(k)k² over the MD configurations at 300 K, compute the Fourier transform over the k-range 3–12 Å⁻¹, and write the R-dependent magnitude and imaginary part to a CSV file.
- Output file: `/app/outputs/exafs_ft_300K.csv`
- Format: csv
- Contract: Columns: R (float), FT_magnitude (float), FT_imag (float)
- Scoring: scored by hidden verifier

### Step 7: Configuration-averaged EXAFS and Fourier transform at 400 K
- Role: scored (load-bearing)
- Action: Arithmetically average χ(k)k² over the MD configurations at 400 K, compute the Fourier transform over the k-range 3–12 Å⁻¹, and write the R-dependent magnitude and imaginary part to a CSV file.
- Output file: `/app/outputs/exafs_ft_400K.csv`
- Format: csv
- Contract: Columns: R (float), FT_magnitude (float), FT_imag (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/md_structural_params.csv`
- `/app/outputs/exafs_ft_180K.csv`
- `/app/outputs/exafs_ft_300K.csv`
- `/app/outputs/exafs_ft_400K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### md_structural_params.csv
- path: `/app/outputs/md_structural_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Structural parameters (coordination number N, interatomic distance R, mean-square relative displacement sigma2) for the first six coordination shells around Co at each of three temperatures.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `shell`, `N`, `R`, `sigma2`
  - `units`:
    - `temperature`: K
    - `R`: Å
    - `sigma2`: Å²

### exafs_ft_180K.csv
- path: `/app/outputs/exafs_ft_180K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fourier transform of the configuration-averaged EXAFS chi(k)*k^2 at 180 K.
- schema:
  - `type`: table
  - `required_columns`: `R`, `FT_magnitude`, `FT_imag`
  - `units`:
    - `R`: Å
    - `FT_magnitude`: a.u.
    - `FT_imag`: a.u.

### exafs_ft_300K.csv
- path: `/app/outputs/exafs_ft_300K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fourier transform of the configuration-averaged EXAFS chi(k)*k^2 at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `R`, `FT_magnitude`, `FT_imag`
  - `units`:
    - `R`: Å
    - `FT_magnitude`: a.u.
    - `FT_imag`: a.u.

### exafs_ft_400K.csv
- path: `/app/outputs/exafs_ft_400K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fourier transform of the configuration-averaged EXAFS chi(k)*k^2 at 400 K.
- schema:
  - `type`: table
  - `required_columns`: `R`, `FT_magnitude`, `FT_imag`
  - `units`:
    - `R`: Å
    - `FT_magnitude`: a.u.
    - `FT_imag`: a.u.

Notes: All scored outputs are compared against hidden gold values (paper-reported MD structural parameters and digitized reference Fourier transform curves). The agent must execute the full MD+MS pipeline to produce realistic results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "md_structural_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "shell",
          "N",
          "R",
          "sigma2"
        ],
        "units": {
          "temperature": "K",
          "R": "Å",
          "sigma2": "Å²"
        }
      },
      "description": "Structural parameters (coordination number N, interatomic distance R, mean-square relative displacement sigma2) for the first six coordination shells around Co at each of three temperatures."
    },
    {
      "file": "exafs_ft_180K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "FT_magnitude",
          "FT_imag"
        ],
        "units": {
          "R": "Å",
          "FT_magnitude": "a.u.",
          "FT_imag": "a.u."
        }
      },
      "description": "Fourier transform of the configuration-averaged EXAFS chi(k)*k^2 at 180 K."
    },
    {
      "file": "exafs_ft_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "FT_magnitude",
          "FT_imag"
        ],
        "units": {
          "R": "Å",
          "FT_magnitude": "a.u.",
          "FT_imag": "a.u."
        }
      },
      "description": "Fourier transform of the configuration-averaged EXAFS chi(k)*k^2 at 300 K."
    },
    {
      "file": "exafs_ft_400K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "FT_magnitude",
          "FT_imag"
        ],
        "units": {
          "R": "Å",
          "FT_magnitude": "a.u.",
          "FT_imag": "a.u."
        }
      },
      "description": "Fourier transform of the configuration-averaged EXAFS chi(k)*k^2 at 400 K."
    }
  ],
  "notes": "All scored outputs are compared against hidden gold values (paper-reported MD structural parameters and digitized reference Fourier transform curves). The agent must execute the full MD+MS pipeline to produce realistic results."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores the contents of each output file. For the structural parameters (md_structural_params.csv), the verifier compares your reported R and σ² values to reference values derived from the published analysis, rewarding agreement within expected tolerance. For the EXAFS Fourier transforms (exafs_ft_*.csv), the verifier compares the magnitude and imaginary-part curves to reference curves digitized from the published computed spectra; the scoring rewards shape similarity, correct peak positions, and relative amplitudes. The final reward is a weighted combination of these stage scores. Importantly, reproducing the correct curves requires genuinely executing the MD and multiple-scattering pipeline; reporting published numbers without performing the computation will not produce detailed R-space curves that match the reference and will result in a low score.
