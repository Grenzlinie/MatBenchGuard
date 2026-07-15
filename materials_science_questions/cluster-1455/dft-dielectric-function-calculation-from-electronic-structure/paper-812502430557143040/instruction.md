# DFT-based predictions of structural, electronic, and optical properties of ternary Zintl phases

## Problem background
Ternary Zintl phases AE₃GaAs₃ (AE = Sr, Ba) are potential candidates for optoelectronic and thermoelectric applications, but experimental measurements of their fundamental physical properties—equilibrium lattice parameters, elastic stiffness, electronic band gap, charge‑carrier effective masses, and static dielectric constants—remain scarce. This task uses first‑principles density‑functional theory (DFT) to compute these quantities for both Sr₃GaAs₃ and Ba₃GaAs₃, supplying quantitative reference data that can help assess their technological potential.

## Approach
The predictions are built from DFT‑based calculations that start from the publicly available experimental crystal structures (orthorhombic, space group Pnma). The workflow proceeds in three stages:

1. **Full geometry optimization** – relax the lattice vectors and atomic positions with the GGA‑PBEsol exchange‑correlation functional to obtain the equilibrium lattice constants and cell volume.
2. **Elastic‑constant calculation** – apply the stress‑strain method on the optimized cells to compute the nine independent single‑crystal elastic constants Cᵢⱼ.
3. **Electronic‑structure and optical post‑processing** – perform a self‑consistent field calculation using a functional that yields accurate band gaps (e.g., TB‑mBJ or a hybrid) on the optimized structures; from the resulting eigenvalues and wavefunctions (a) identify the direct band gap at the Γ point, (b) fit the band‑edge dispersions along [100], [010], and [001] to obtain electron and hole effective masses, and (c) evaluate the real part of the frequency‑dependent dielectric function at ω→0 for the three principal polarization directions.

All calculations are reproducible with open‑source codes (Quantum ESPRESSO for geometry and elastic constants; GPAW or Elk for the electronic‑structure steps) and standard pseudopotential libraries. The detailed step‑by‑step instructions below describe the required input files, output artifacts, and data formats.

## Reproduction target
Your goal is to produce three CSV files for the two compounds Sr₃GaAs₃ and Ba₃GaAs₃, following the workflow defined in the steps and respecting the exact schemas listed in the Output contract:

- `optimized_lattice.csv` – equilibrium lattice constants a, b, c (Å) and unit‑cell volume V (Å³).
- `elastic_constants.csv` – the nine independent single‑crystal elastic constants C₁₁, C₁₂, C₁₃, C₂₂, C₂₃, C₃₃, C₄₄, C₅₅, C₆₆ (all in GPa).
- `electronic_and_optical.csv` – the direct band gap at Γ (eV), electron and hole effective masses (in units of the free‑electron mass m₀) along the three principal crystallographic directions, and the static real dielectric constants for polarization along the a, b, c axes.

The numbers must be obtained from genuine DFT calculations executed through the prescribed workflow; using pre‑computed or guessed values is not an acceptable substitute.

## Assets

- Experimental crystal structures of Sr3GaAs3 and Ba3GaAs3: 10.3390/cryst5040433
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GPAW or Elk: https://wiki.fysik.dtu.dk/gpaw/
- Pseudopotential datasets (SSSP or PSLibrary): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Obtain initial crystal structures
- Role: process
- Action: Retrieve the published experimental crystal structures of Sr3GaAs3 and Ba3GaAs3 (lattice parameters and fractional coordinates) from the literature (DOI: 10.3390/cryst5040433) and prepare input files for DFT calculations.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: Structural optimization
- Role: scored
- Action: Perform full DFT geometry optimization (lattice parameters and atomic positions) of both compounds using the GGA-PBEsol exchange-correlation functional, starting from the experimental structures obtained in step 1. Save the optimized lattice constants a, b, c (in Å) and unit-cell volume V (in Å³) to the output file.
- Output file: `/app/outputs/optimized_lattice.csv`
- Format: csv
- Contract: CSV with columns: compound (string), a (float, Angstrom), b (float, Angstrom), c (float, Angstrom), V (float, Angstrom^3).
- Scoring: scored by hidden verifier

### Step 3: Elastic constants calculation
- Role: scored
- Action: Using the optimized structures from step 2, compute the nine independent single-crystal elastic constants (C11, C12, C13, C22, C23, C33, C44, C55, C66) for the orthorhombic phases via the stress-strain method with the same DFT functional. Write the results to the output file.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: CSV with columns: compound (string), C11, C12, C13, C22, C23, C33, C44, C55, C66 (all float, GPa).
- Scoring: scored by hidden verifier

### Step 4: Electronic structure SCF calculation
- Role: process
- Action: Perform a self-consistent field DFT calculation on the optimized structures using a method that yields accurate band gaps (e.g., a hybrid functional or the TB-mBJ potential). Compute Kohn-Sham eigenvalues on a fine k-point mesh covering the Brillouin zone and along the high-symmetry path needed to analyze band edges.
- Evidence: `/app/outputs/electronic_scf_output.txt`

### Step 5: Post-processing: band gap, effective masses, and dielectric constants
- Role: scored (load-bearing)
- Action: From the SCF results of step 4, (i) identify the direct band gap at the Γ point; (ii) along the [100], [010], [001] directions, fit the energy dispersion near the valence band maximum and conduction band minimum to extract electron and hole effective masses; (iii) compute the frequency-dependent dielectric function (real part) from the momentum matrix elements and Kramers-Kronig transformation, then extract the static (ω→0) values for polarization along the a, b, c axes. Write all these quantities to the output file.
- Output file: `/app/outputs/electronic_and_optical.csv`
- Format: csv
- Contract: CSV with columns: compound (string), bandgap (float, eV), me_100, me_010, me_001, mh_100, mh_010, mh_001 (float, dimensionless, in units of m0), epsilon1_100, epsilon1_010, epsilon1_001 (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_lattice.csv`
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/electronic_and_optical.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_lattice.csv
- path: `/app/outputs/optimized_lattice.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized equilibrium lattice parameters and unit-cell volume for both compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a`, `b`, `c`, `V`
  - `units`:
    - `a`: Angstrom
    - `b`: Angstrom
    - `c`: Angstrom
    - `V`: Angstrom^3

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Single-crystal elastic constants Cij for the two orthorhombic compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `C11`, `C12`, `C13`, `C22`, `C23`, `C33`, `C44`, `C55`, `C66`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C22`: GPa
    - `C23`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C55`: GPa
    - `C66`: GPa

### electronic_and_optical.csv
- path: `/app/outputs/electronic_and_optical.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Direct band gap, electron and hole effective masses along three principal directions, and static dielectric constants for three polarization directions.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `bandgap`, `me_100`, `me_010`, `me_001`, `mh_100`, `mh_010`, `mh_001`, `epsilon1_100`, `epsilon1_010`, `epsilon1_001`
  - `units`:
    - `bandgap`: eV
    - `me_100`: dimensionless (m0)
    - `me_010`: dimensionless (m0)
    - `me_001`: dimensionless (m0)
    - `mh_100`: dimensionless (m0)
    - `mh_010`: dimensionless (m0)
    - `mh_001`: dimensionless (m0)
    - `epsilon1_100`: dimensionless
    - `epsilon1_010`: dimensionless
    - `epsilon1_001`: dimensionless

Notes: The checker compares each submitted value against the paper-reported reference value with an appropriate hidden tolerance that accounts for legitimate toolchain spread. All quantities are fixed physical properties; meeting the reference within tolerance earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_lattice.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a",
          "b",
          "c",
          "V"
        ],
        "units": {
          "a": "Angstrom",
          "b": "Angstrom",
          "c": "Angstrom",
          "V": "Angstrom^3"
        }
      },
      "description": "Optimized equilibrium lattice parameters and unit-cell volume for both compounds."
    },
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "C11",
          "C12",
          "C13",
          "C22",
          "C23",
          "C33",
          "C44",
          "C55",
          "C66"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C22": "GPa",
          "C23": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C55": "GPa",
          "C66": "GPa"
        }
      },
      "description": "Single-crystal elastic constants Cij for the two orthorhombic compounds."
    },
    {
      "file": "electronic_and_optical.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "bandgap",
          "me_100",
          "me_010",
          "me_001",
          "mh_100",
          "mh_010",
          "mh_001",
          "epsilon1_100",
          "epsilon1_010",
          "epsilon1_001"
        ],
        "units": {
          "bandgap": "eV",
          "me_100": "dimensionless (m0)",
          "me_010": "dimensionless (m0)",
          "me_001": "dimensionless (m0)",
          "mh_100": "dimensionless (m0)",
          "mh_010": "dimensionless (m0)",
          "mh_001": "dimensionless (m0)",
          "epsilon1_100": "dimensionless",
          "epsilon1_010": "dimensionless",
          "epsilon1_001": "dimensionless"
        }
      },
      "description": "Direct band gap, electron and hole effective masses along three principal directions, and static dielectric constants for three polarization directions."
    }
  ],
  "notes": "The checker compares each submitted value against the paper-reported reference value with an appropriate hidden tolerance that accounts for legitimate toolchain spread. All quantities are fixed physical properties; meeting the reference within tolerance earns full credit."
}
```

## How you are scored
A hidden automatic verifier will independently compare the numerical values in each of your three scored CSV files against carefully vetted reference data. The overall reward is a weighted sum over the three files, normalized to the interval [0, 1]; a perfect agreement with the references yields a reward of 1.0. The verifier uses tolerances that are chosen to distinguish physically correct DFT results from guesses or copied values—reporting numbers found in a publication or inventing data that are not obtained from actual calculations will result in a very low or zero reward. The exact tolerances and reference values are not disclosed; to earn a high score you must faithfully execute the DFT workflow described in the steps, because only genuinely computed quantities can fall within the expected agreement range.
