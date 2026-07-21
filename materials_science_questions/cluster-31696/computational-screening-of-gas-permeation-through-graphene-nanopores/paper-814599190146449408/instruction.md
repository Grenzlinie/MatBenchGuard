# Molecular dynamics study of water flux and ion rejection through pyridinic-N-doped graphene nanopores

## Problem background
Reverse osmosis (RO) desalination with semipermeable membranes is a leading technology for producing fresh water. Single-layer graphene membranes with tailored nanopores are promising because they can combine high water permeability with effective salt rejection. The chemistry of the pore rim — in particular, functionalization with pyridinic-like nitrogen — can tune the pore size, charge distribution, and hydrophilicity, all of which affect transport. This task computationally evaluates the desalination performance of five pyridinic‑N‑doped nanoporous graphene membranes using molecular dynamics (MD) simulations. The goal is to predict water flux, salt rejection, and the free energy barriers that govern water and ion passage through these pores, in order to understand how the doping level and functional groups influence membrane performance.

## Approach
Five functionalized graphene membranes are considered: N‑graphene (pure pyridinic N), NH‑graphene, NH₃‑graphene, NOH‑graphene, and H‑graphene. All simulations use classical MD with established force fields (SPC/E water, OPLS‑AA for functional groups, uncharged LJ carbon for graphene) together with atomic partial charges obtained from density functional theory (DFT) Hirshfeld analysis. The workflow proceeds in three stages:

- **Membrane construction and charge assignment:** Build each pore structure and compute its atomic charges via DFT (e.g., PBE‑D/DZP). These charges are used in all subsequent MD runs.
- **Non‑equilibrium MD (NEMD) for permeation:** A two‑chamber cell with 0.6 M NaCl feed and pure water permeate is simulated under NVT conditions at 300 K. A rigid graphene piston applies a known transmembrane pressure (50–530 MPa). From the net number of transferred water molecules vs. time, the water flux is extracted for each membrane and pressure. Salt rejection is computed from the ion counts that pass through the pore when half of the water has permeated.
- **Potentials of mean force (PMF):** Free‑energy profiles for a single water molecule (force integration) and for Na⁺ and Cl⁻ ions (steered MD) are computed along the axis perpendicular to the pore (z from -15 to +15 Å, pore centre at z=0).

The resulting data (flux, rejection, PMF) allow a quantitative comparison across all five membrane types and reveal how pore chemistry controls the trade‑off between water transport and ion exclusion.

## Reproduction target
Produce three comma-separated value (CSV) files that together capture the membrane separation behaviour:

1. **Water flux vs. pressure** (`water_flux_data.csv`): One row per (membrane, pressure) combination containing the membrane name, applied pressure (in MPa), and water flux (in ns⁻¹).
2. **Salt rejection vs. pressure** (`salt_rejection_data.csv`): One row per (membrane, pressure) combination with the membrane name, applied pressure (in MPa), and salt rejection (a dimensionless fraction between 0 and 1).
3. **PMF profiles** (`pmf_profiles.csv`): For each membrane and each species (water, Na⁺, Cl⁻), rows giving the spatial coordinate z (in Å) and the corresponding PMF value (in kcal/mol) along the permeation path from -15 to +15 Å (pore centre at z=0).

The targets are defined by these output files themselves: compute the required quantities for all five membranes under the stated conditions and store them in the specified format. The correctness will be checked against hidden reference values derived from the original study.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/download.html
- DFT package (e.g., CP2K, Quantum ESPRESSO, ADF): https://www.cp2k.org/download
- SPC/E water model parameters: 10.1021/j100308a038
- OPLS-AA force field parameters: 10.1021/ja9621760
- Ion force field parameters (Na+, Cl-): 10.1021/ja00146a022
- Graphene carbon Lennard-Jones parameters: 10.1021/ja00146a022
- Python 3 with numpy, scipy, matplotlib, pandas: numpy scipy matplotlib pandas

## Workflow steps

### Step 1: Construct functionalized graphene membrane models
- Role: process
- Action: Build atomic coordinates for the five pyridinic-N doped nanoporous graphene sheets: N-graphene, NH-graphene, NH3-graphene, NOH-graphene, and H-graphene, with pore diameters in the range 0.75–0.89 nm. Save the structure files.
- Evidence: `/app/outputs/membrane_structures.tar.gz`

### Step 2: Compute Hirshfeld atomic charges via DFT
- Role: process
- Action: For each membrane model, perform DFT geometry optimization and compute Hirshfeld charges at the PBE-D/DZP level using an open-source DFT code. Save the atomic charges for use in MD simulations.
- Evidence: `/app/outputs/hirshfeld_charges.json`

### Step 3: Simulate water flux versus transmembrane pressure
- Role: scored (load-bearing)
- Action: Set up two-chamber simulation cells with each membrane, 0.6 M NaCl feed and pure water permeate, and a rigid graphene piston. Use LAMMPS NVT at 300 K with applied forces on the piston generating pressures in the range 50–530 MPa. Run non-equilibrium MD for each membrane and pressure. Compute net transferred water molecules (N_w) vs time and extract the linear slope to obtain water flux per pressure. Record the data in water_flux_data.csv.
- Output file: `/app/outputs/water_flux_data.csv`
- Format: csv
- Contract: columns: membrane_name (str), applied_pressure_MPa (float), water_flux_ns-1 (float)
- Scoring: scored by hidden verifier

### Step 4: Compute salt rejection versus pressure
- Role: scored
- Action: From the same NEMD simulations, count the ions that pass through the membrane when half of the water has permeated, and compute salt rejection R = 1 - N_{1/2}/N_0. Output the data to salt_rejection_data.csv.
- Output file: `/app/outputs/salt_rejection_data.csv`
- Format: csv
- Contract: columns: membrane_name (str), applied_pressure_MPa (float), salt_rejection (float, 0-1)
- Scoring: scored by hidden verifier

### Step 5: Compute potentials of mean force for water and ions
- Role: scored
- Action: Using the membrane structures and force fields, compute the PMF profiles for a single water molecule (force integration method) and for Na+ and Cl- ions (steered molecular dynamics) traversing each pore along the reaction coordinate z from -15 Å to +15 Å (pore center at z=0). Record the free energy profiles in pmf_profiles.csv.
- Output file: `/app/outputs/pmf_profiles.csv`
- Format: csv
- Contract: columns: membrane_name (str), species (water/Na+/Cl-), z_angstrom (float), pmf_kcal_per_mol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/water_flux_data.csv`
- `/app/outputs/salt_rejection_data.csv`
- `/app/outputs/pmf_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### water_flux_data.csv
- path: `/app/outputs/water_flux_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Water flux across five functionalized graphene membranes at pressures from 50 to 530 MPa. Reference comparison includes quantitative tolerances and checks for linear flux-pressure trend and ordering (N-graphene highest).
- schema:
  - `type`: table
  - `required_columns`: `membrane_name`, `applied_pressure_MPa`, `water_flux_ns-1`
  - `units`:
    - `applied_pressure_MPa`: MPa
    - `water_flux_ns-1`: ns^{-1}

### salt_rejection_data.csv
- path: `/app/outputs/salt_rejection_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Salt rejection (0-1) for each membrane at several pressures. Reference comparison checks near-perfect rejection for NOH-graphene and tolerance for others.
- schema:
  - `type`: table
  - `required_columns`: `membrane_name`, `applied_pressure_MPa`, `salt_rejection`
  - `units`:
    - `applied_pressure_MPa`: MPa
    - `salt_rejection`: dimensionless

### pmf_profiles.csv
- path: `/app/outputs/pmf_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: PMF profiles for water, Na+, and Cl- through each pore. Reference comparison checks barrier heights and relative ordering (lowest barrier for N-graphene, high for ions).
- schema:
  - `type`: table
  - `required_columns`: `membrane_name`, `species`, `z_angstrom`, `pmf_kcal_per_mol`
  - `units`:
    - `z_angstrom`: Å
    - `pmf_kcal_per_mol`: kcal/mol

Notes: The checker compares submitted CSV data against reference values with tolerances appropriate for toolchain differences. It also verifies structural trends: linear increase of flux with pressure, highest flux for N-graphene, salt rejection near 1 for NOH-graphene, and PMF barrier ordering consistent with the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "water_flux_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "membrane_name",
          "applied_pressure_MPa",
          "water_flux_ns-1"
        ],
        "units": {
          "applied_pressure_MPa": "MPa",
          "water_flux_ns-1": "ns^{-1}"
        }
      },
      "description": "Water flux across five functionalized graphene membranes at pressures from 50 to 530 MPa. Reference comparison includes quantitative tolerances and checks for linear flux-pressure trend and ordering (N-graphene highest)."
    },
    {
      "file": "salt_rejection_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "membrane_name",
          "applied_pressure_MPa",
          "salt_rejection"
        ],
        "units": {
          "applied_pressure_MPa": "MPa",
          "salt_rejection": "dimensionless"
        }
      },
      "description": "Salt rejection (0-1) for each membrane at several pressures. Reference comparison checks near-perfect rejection for NOH-graphene and tolerance for others."
    },
    {
      "file": "pmf_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "membrane_name",
          "species",
          "z_angstrom",
          "pmf_kcal_per_mol"
        ],
        "units": {
          "z_angstrom": "Å",
          "pmf_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "PMF profiles for water, Na+, and Cl- through each pore. Reference comparison checks barrier heights and relative ordering (lowest barrier for N-graphene, high for ions)."
    }
  ],
  "notes": "The checker compares submitted CSV data against reference values with tolerances appropriate for toolchain differences. It also verifies structural trends: linear increase of flux with pressure, highest flux for N-graphene, salt rejection near 1 for NOH-graphene, and PMF barrier ordering consistent with the paper."
}
```

## How you are scored
A hidden verifier will score each output file by comparing your submitted data to reference values and structural trends. The scoring criteria include:
- Quantitative agreement with expected water flux values (with appropriate tolerance to account for toolchain differences such as DFT code, force‑field implementation, and MD engine version).
- Faithful reproduction of the salt rejection behaviour across pressures.
- Correct ordering and magnitude of PMF barriers for water and ions across the five membranes.
- Presence of all five membrane types and expected trend information (e.g., flux increases linearly with pressure).

The verifier computes a weighted reward for each stage and returns a single overall score between 0 and 1. The reward is monotonic in solution quality: a more accurate reproduction yields a higher score. Simply reporting a number without the underlying workflow will not satisfy the scoring criteria.
