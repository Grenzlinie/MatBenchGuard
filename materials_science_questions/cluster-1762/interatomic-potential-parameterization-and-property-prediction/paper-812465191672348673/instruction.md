# Ab Initio–Fitted Interatomic Potential for AlN and Thermal Conductivity from Molecular Dynamics

## Problem background
Aluminum nitride (AlN) is a promising substrate material for electronics because of its extremely high theoretical thermal conductivity (~320 W m⁻¹ K⁻¹), but in practical ceramics the conductivity is often much lower due to crystalline imperfections such as lattice defects and the possible coexistence of a metastable zincblende phase. Developing a reliable interatomic potential and using it in molecular dynamics simulations can help understand and predict how these imperfections affect heat transport, and guide materials design. This task reproduces such a potential from first-principles quantum chemistry calculations and uses it to compute thermal conductivities of wurtzite and zincblende AlN, as well as the influence of an aluminum vacancy.

## Approach
The interatomic potential combines a two-body term (Coulomb interaction, Born–Mayer–type repulsion, and dipole–dipole dispersion) and a short-range three-body term that penalizes deviations from the ideal tetrahedral bond angle via a smooth cut-off function. The potential parameters are determined by fitting to a potential energy surface obtained from an ab initio molecular orbital calculation on an Al₄N₄H₁₈ cluster (using an STO-3G basis set and an open-source quantum chemistry code such as NWChem). Once the potential is fitted, equilibrium lattice constants and bulk modulus of wurtzite AlN are computed with Ewald summation for the long-range electrostatics. Molecular dynamics simulations are then carried out for perfect wurtzite (72 atoms) and for wurtzite with one Al vacancy (71 atoms) at specified temperatures, as well as for zincblende AlN. The thermal conductivity along the c-axis is obtained from the Green–Kubo formula by integrating the heat flux autocorrelation function. The main comparison involves the thermal conductivity values of wurtzite at two different temperatures, the effect of an Al vacancy, and the difference between the wurtzite and zincblende phases.

## Reproduction target
You must produce the following artifacts:
- Equilibrium lattice constants a and c and bulk modulus B of wurtzite AlN (lattice_constants.json).
- Thermal conductivity of perfect wurtzite AlN at 282 K and 1130 K (thermal_conductivity_wurtzite.csv).
- Thermal conductivity of wurtzite AlN with one Al vacancy at a temperature near 300 K (thermal_conductivity_vacancy.csv).
- Thermal conductivity of zincblende AlN at 268 K (thermal_conductivity_zincblende.csv).

In addition to the numerical values, the verifier will assess whether the thermal conductivity of zincblende is higher or lower than that of wurtzite, whether the Al vacancy increases or decreases the conductivity relative to perfect wurtzite, and whether wurtzite conductivity increases or decreases with temperature.

## Assets

- NWChem: https://github.com/nwchemgit/nwchem
- LAMMPS: https://www.lammps.org/
- Python scientific stack: numpy scipy

## Workflow steps

### Step 1: Ab initio MO calculation on Al4N4H18 cluster
- Role: process
- Action: Perform an ab initio molecular orbital calculation on a model cluster consisting of four Al and four N atoms arranged as a fragment of the wurtzite structure, with three H atoms attached to each outer Al and N atom at a fixed Al–H and N–H distance of 1.0 Å to saturate dangling bonds. Use an open-source quantum chemistry code (e.g., NWChem) with the STO-3G basis set. Vary the nearest Al–N bond length and the bond angle to generate a potential energy surface (energy as a function of bond length and angle) that will serve as reference data for fitting the interatomic potential.
- Evidence: `/app/outputs/mo_energy_surface.txt`

### Step 2: Fit interatomic potential parameters
- Role: process
- Action: Fit the parameters of the two-body (Born–Mayer–Higgins with Coulomb and dispersion) and three-body (angular term with a smooth cut-off) potential functions to the energy surface obtained from the MO calculation. The two-body term includes effective point charges, Born–Mayer–type repulsion, and dipole–dipole dispersion; the three-body term penalizes deviations from the preferred bond angle and is short-ranged via a piecewise cut-off function. Perform a non-linear least-squares optimization to obtain numerical values for all potential parameters.
- Evidence: `/app/outputs/fitted_parameters.json`

### Step 3: Compute wurtzite lattice constants and bulk modulus
- Role: scored (load-bearing)
- Action: Using the fitted interatomic potential and Ewald summation for long-range electrostatics, compute the equilibrium lattice constants a and c and the bulk modulus B of wurtzite AlN. The c/a ratio should be kept at the experimental ratio during energy–volume scans.
- Output file: `/app/outputs/lattice_constants.json`
- Format: json
- Contract: JSON object with keys: a (Angstrom, float), c (Angstrom, float), bulk_modulus (N/m^2, float).
- Scoring: scored by hidden verifier

### Step 4: Thermal conductivity of perfect wurtzite
- Role: scored
- Action: Run equilibrium molecular dynamics simulation of perfect wurtzite AlN (72 atoms in the simulation cell, periodic boundaries) with a time step of 0.5 fs in the NVT ensemble at temperatures 282 K and 1130 K. Use the fitted potential and the Green–Kubo formula to compute the thermal conductivity along the c-axis from the decay of the heat flux autocorrelation function. Equilibrate the system and collect the heat flux time correlation until convergence.
- Output file: `/app/outputs/thermal_conductivity_wurtzite.csv`
- Format: csv
- Contract: CSV with columns: Temperature (K, float), Lambda_c (W/mK, float). Two rows for 282 K and 1130 K.
- Scoring: scored by hidden verifier

### Step 5: Thermal conductivity with an Al vacancy
- Role: scored
- Action: Run equilibrium MD simulation of wurtzite AlN with one Al atom removed from the simulation cell (71 atoms) at a temperature near 300 K, using the same MD protocol and Green–Kubo analysis as the perfect crystal. Compute the thermal conductivity along the c-axis.
- Output file: `/app/outputs/thermal_conductivity_vacancy.csv`
- Format: csv
- Contract: CSV with columns: Defect (string, e.g., 'Al'), Temperature (K, float), Lambda_c (W/mK, float). One row for the Al vacancy.
- Scoring: scored by hidden verifier

### Step 6: Thermal conductivity of zincblende AlN
- Role: scored
- Action: Run equilibrium MD simulation of zincblende AlN at 268 K, using the same MD protocol and Green–Kubo analysis. Compute the thermal conductivity along the c-axis.
- Output file: `/app/outputs/thermal_conductivity_zincblende.csv`
- Format: csv
- Contract: CSV with columns: Temperature (K, float), Lambda_c (W/mK, float). One row for 268 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.json`
- `/app/outputs/thermal_conductivity_wurtzite.csv`
- `/app/outputs/thermal_conductivity_vacancy.csv`
- `/app/outputs/thermal_conductivity_zincblende.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.json
- path: `/app/outputs/lattice_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice parameters and bulk modulus of wurtzite AlN. The values will be compared to reference data with a tolerance appropriate for code differences.
- schema:
  - `type`: object
  - `required`:
    - `a`: float (Angstrom)
    - `c`: float (Angstrom)
    - `bulk_modulus`: float (N/m^2)

### thermal_conductivity_wurtzite.csv
- path: `/app/outputs/thermal_conductivity_wurtzite.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermal conductivity of perfect wurtzite AlN at 282 K and 1130 K. The checker compares each value to hidden reference data within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Lambda_c`
  - `units`:
    - `Temperature`: K
    - `Lambda_c`: W/mK

### thermal_conductivity_vacancy.csv
- path: `/app/outputs/thermal_conductivity_vacancy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermal conductivity of wurtzite AlN with an Al vacancy at a temperature near 300 K. The checker compares the conductivity to a hidden reference value.
- schema:
  - `type`: table
  - `required_columns`: `Defect`, `Temperature`, `Lambda_c`
  - `units`:
    - `Temperature`: K
    - `Lambda_c`: W/mK

### thermal_conductivity_zincblende.csv
- path: `/app/outputs/thermal_conductivity_zincblende.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermal conductivity of zincblende AlN at 268 K. The checker compares the value to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Lambda_c`
  - `units`:
    - `Temperature`: K
    - `Lambda_c`: W/mK

Notes: Agent must reproduce the full interatomic potential fitting pipeline from ab initio MO data; no pre-fitted potential is provided. Scoring includes both numerical comparison of the submitted quantities and additional hidden checks on relative ordering (e.g., zincblende conductivity < wurtzite, and conductivity with Al vacancy < perfect wurtzite).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float (Angstrom)",
          "c": "float (Angstrom)",
          "bulk_modulus": "float (N/m^2)"
        }
      },
      "description": "Equilibrium lattice parameters and bulk modulus of wurtzite AlN. The values will be compared to reference data with a tolerance appropriate for code differences."
    },
    {
      "file": "thermal_conductivity_wurtzite.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Lambda_c"
        ],
        "units": {
          "Temperature": "K",
          "Lambda_c": "W/mK"
        }
      },
      "description": "Thermal conductivity of perfect wurtzite AlN at 282 K and 1130 K. The checker compares each value to hidden reference data within a relative tolerance."
    },
    {
      "file": "thermal_conductivity_vacancy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Defect",
          "Temperature",
          "Lambda_c"
        ],
        "units": {
          "Temperature": "K",
          "Lambda_c": "W/mK"
        }
      },
      "description": "Thermal conductivity of wurtzite AlN with an Al vacancy at a temperature near 300 K. The checker compares the conductivity to a hidden reference value."
    },
    {
      "file": "thermal_conductivity_zincblende.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Lambda_c"
        ],
        "units": {
          "Temperature": "K",
          "Lambda_c": "W/mK"
        }
      },
      "description": "Thermal conductivity of zincblende AlN at 268 K. The checker compares the value to a hidden reference."
    }
  ],
  "notes": "Agent must reproduce the full interatomic potential fitting pipeline from ab initio MO data; no pre-fitted potential is provided. Scoring includes both numerical comparison of the submitted quantities and additional hidden checks on relative ordering (e.g., zincblende conductivity < wurtzite, and conductivity with Al vacancy < perfect wurtzite)."
}
```

## How you are scored
Each scored output file is validated by a hidden verifier. The lattice constants and bulk modulus are compared against reference values within a prescribed tolerance. The thermal conductivity values from the CSV files are compared to reference data, also with a suitable tolerance. The verifier further checks the relative ordering between the conditions: zincblende vs. wurtzite, perfect wurtzite vs. vacancy-containing wurtzite, and low vs. high temperature. Each stage carries a weight, and the final reward is a weighted sum of the individual scores. You do not need to match any specific published number exactly; a physically sound reproduction that lands within the tolerance and respects the expected trends will earn full credit.
