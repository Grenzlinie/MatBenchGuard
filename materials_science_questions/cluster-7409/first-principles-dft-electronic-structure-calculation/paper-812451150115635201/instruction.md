# First-principles DFT investigation of structural and electronic properties of TiO2 polymorphs

## Problem background
Titanium dioxide (TiO2) exists in several polymorphs, among which rutile (space group P4_2/mnm) and anatase (I4_1/amd) are the most studied for photocatalytic and photoelectrochemical applications. Accurate knowledge of their structural, mechanical, and electronic properties is fundamental for understanding their performance. First-principles density functional theory (DFT) is a powerful tool to compute such properties from the atomic constituents. This task is to compute the equilibrium lattice parameters, internal atomic coordinates, density, bulk modulus, electronic band gaps, and the relative thermodynamic stability of rutile and anatase within the local density approximation (LDA) using two different norm-conserving pseudopotentials.

## Approach
The computational approach is an ab initio pseudopotential plane-wave method within LDA. Two types of norm-conserving pseudopotentials are employed: Troullier-Martins (TM) type and Teter-type extended norm-conserving potentials. For titanium the 3s, 3p, 4s, and 3d electrons are included as valence, and for oxygen the 2s and 2p electrons. First, convergence tests determine suitable plane-wave energy cutoffs and k-point grids. Then, full structural optimizations of both rutile and anatase are performed under symmetry constraints, allowing lattice parameters and internal coordinates to relax until forces are small. Bulk moduli are obtained by computing total energies over a range of unit-cell volumes with internal relaxation at each volume, fitting the energy-volume data to Murnaghan's equation of state. Electronic band structures are calculated along high-symmetry paths for the optimized structures to determine the band gap type (direct or indirect) and its magnitude. Finally, the total energy difference per formula unit between anatase and rutile is evaluated to identify the more stable phase. The whole workflow is carried out with an open-source DFT code (e.g., ABINIT) and publicly available pseudopotential generation tools.

## Reproduction target
Compute the following quantities for both rutile and anatase, using both the TM-type and the Teter-type pseudopotentials:

1. Optimized lattice constants a and c (in Å), the c/a ratio, the internal oxygen coordinate u (unitless), and the density d (in g/cm³).
2. Bulk modulus B (in GPa) from a Murnaghan equation-of-state fit.
3. Electronic band gap type (direct or indirect) and its value (in eV).
4. Total energy difference ΔE = E(anatase) – E(rutile) per TiO₂ formula unit (in kcal/mol), together with the thermodynamically more stable phase.

All numerical results must be written to CSV files with the exact headers and units specified in the workflow steps and output contract.

## Assets

- ABINIT DFT code: https://www.abinit.org/download
- Pseudopotential generation software (e.g., FHI98PP or oncvpsp): https://www.fhi-berlin.mpg.de/th/fhi98pp/
- Initial crystal structures of rutile and anatase from literature

## Workflow steps

### Step 1: Generate pseudopotentials for Ti and O
- Role: process
- Action: Generate Troullier-Martins (TM) and Teter-type norm-conserving pseudopotentials for titanium (valence: 3s, 3p, 4s, 3d) and oxygen (valence: 2s, 2p) using a pseudopotential generator. Alternatively, obtain pre-generated potentials from a public repository that match the specifications.
- Evidence: `/app/outputs/pseudopotential_manifest.txt`

### Step 2: Determine convergence parameters for DFT calculations
- Role: process
- Action: Perform convergence tests to identify sufficient plane-wave energy cutoffs and Monkhorst-Pack k-point grids for rutile and anatase with each pseudopotential. Document the chosen converged parameters.
- Evidence: `/app/outputs/convergence_params.json`

### Step 3: Optimize rutile structure
- Role: scored
- Action: Perform DFT structural optimization of the rutile unit cell (space group P4_2/mnm) using both TM and Teter pseudopotentials under imposed symmetry. Minimize total energy with respect to atomic positions and lattice parameters until forces are below an appropriate threshold.
- Output file: `/app/outputs/optimized_structures_rutile.csv`
- Format: csv
- Contract: CSV with header: pseudopotential,a,c,c/a,u,d. pseudopotential is 'TM' or 'Teter'; a,c (Å); c/a (unitless); u (unitless); d (g/cm³).
- Scoring: scored by hidden verifier

### Step 4: Optimize anatase structure
- Role: scored
- Action: Perform DFT structural optimization of the anatase unit cell (space group I4_1/amd) using both TM and Teter pseudopotentials under imposed symmetry.
- Output file: `/app/outputs/optimized_structures_anatase.csv`
- Format: csv
- Contract: CSV with header: pseudopotential,a,c,c/a,u,d. pseudopotential is 'TM' or 'Teter'; a,c (Å); c/a (unitless); u (unitless); d (g/cm³).
- Scoring: scored by hidden verifier

### Step 5: Compute bulk moduli of rutile and anatase
- Role: scored (load-bearing)
- Action: For each pseudopotential type, compute total energies of rutile and anatase over a range of cell volumes with internal relaxation at each fixed volume. Fit the energy-volume points to Murnaghan’s equation of state to extract the bulk modulus B.
- Output file: `/app/outputs/bulk_moduli.csv`
- Format: csv
- Contract: CSV with header: pseudopotential,phase,B. pseudopotential 'TM' or 'Teter'; phase 'rutile' or 'anatase'; B in GPa.
- Scoring: scored by hidden verifier

### Step 6: Compute band structures and band gaps
- Role: scored
- Action: Calculate the electronic band structures along high-symmetry paths for the optimized rutile and anatase structures with each pseudopotential. Identify the valence band maximum, conduction band minimum, and determine whether the band gap is direct or indirect, and its magnitude.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with header: pseudopotential,phase,gap_type,gap_value. pseudopotential 'TM' or 'Teter'; phase 'rutile' or 'anatase'; gap_type 'direct' or 'indirect'; gap_value in eV.
- Scoring: scored by hidden verifier

### Step 7: Compute total energy difference between phases
- Role: scored
- Action: From the fully optimized total energies, compute the energy difference ΔE = E(anatase) - E(rutile) per TiO2 formula unit for each pseudopotential, and indicate which phase is thermodynamically more stable.
- Output file: `/app/outputs/total_energy_difference.csv`
- Format: csv
- Contract: CSV with header: pseudopotential,delta_E,stable_phase. pseudopotential 'TM' or 'Teter'; delta_E in kcal/mol per TiO2; stable_phase 'rutile' or 'anatase'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structures_rutile.csv`
- `/app/outputs/optimized_structures_anatase.csv`
- `/app/outputs/bulk_moduli.csv`
- `/app/outputs/band_gaps.csv`
- `/app/outputs/total_energy_difference.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structures_rutile.csv
- path: `/app/outputs/optimized_structures_rutile.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice constants, internal oxygen coordinate, c/a ratio, and density of rutile for TM and Teter pseudopotentials.
- schema:
  - `type`: table
  - `required_columns`: `pseudopotential`, `a`, `c`, `c/a`, `u`, `d`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `c/a`: unitless
    - `u`: unitless
    - `d`: g/cm³

### optimized_structures_anatase.csv
- path: `/app/outputs/optimized_structures_anatase.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice constants, internal oxygen coordinate, c/a ratio, and density of anatase for TM and Teter pseudopotentials.
- schema:
  - `type`: table
  - `required_columns`: `pseudopotential`, `a`, `c`, `c/a`, `u`, `d`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `c/a`: unitless
    - `u`: unitless
    - `d`: g/cm³

### bulk_moduli.csv
- path: `/app/outputs/bulk_moduli.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Bulk modulus B for rutile and anatase obtained from Murnaghan equation-of-state fits for each pseudopotential.
- schema:
  - `type`: table
  - `required_columns`: `pseudopotential`, `phase`, `B`
  - `units`:
    - `B`: GPa

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Band gap type (direct/indirect) and magnitude for rutile and anatase with each pseudopotential.
- schema:
  - `type`: table
  - `required_columns`: `pseudopotential`, `phase`, `gap_type`, `gap_value`
  - `units`:
    - `gap_value`: eV

### total_energy_difference.csv
- path: `/app/outputs/total_energy_difference.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total energy difference per TiO2 between anatase and rutile, and the thermodynamically more stable phase.
- schema:
  - `type`: table
  - `required_columns`: `pseudopotential`, `delta_E`, `stable_phase`
  - `units`:
    - `delta_E`: kcal/mol per TiO2

Notes: All outputs are numerical results from first-principles DFT calculations. The checker compares them against hidden reference values within appropriate tolerances to assess reproduction accuracy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structures_rutile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pseudopotential",
          "a",
          "c",
          "c/a",
          "u",
          "d"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "c/a": "unitless",
          "u": "unitless",
          "d": "g/cm³"
        }
      },
      "description": "Optimized lattice constants, internal oxygen coordinate, c/a ratio, and density of rutile for TM and Teter pseudopotentials."
    },
    {
      "file": "optimized_structures_anatase.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pseudopotential",
          "a",
          "c",
          "c/a",
          "u",
          "d"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "c/a": "unitless",
          "u": "unitless",
          "d": "g/cm³"
        }
      },
      "description": "Optimized lattice constants, internal oxygen coordinate, c/a ratio, and density of anatase for TM and Teter pseudopotentials."
    },
    {
      "file": "bulk_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pseudopotential",
          "phase",
          "B"
        ],
        "units": {
          "B": "GPa"
        }
      },
      "description": "Bulk modulus B for rutile and anatase obtained from Murnaghan equation-of-state fits for each pseudopotential."
    },
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pseudopotential",
          "phase",
          "gap_type",
          "gap_value"
        ],
        "units": {
          "gap_value": "eV"
        }
      },
      "description": "Band gap type (direct/indirect) and magnitude for rutile and anatase with each pseudopotential."
    },
    {
      "file": "total_energy_difference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pseudopotential",
          "delta_E",
          "stable_phase"
        ],
        "units": {
          "delta_E": "kcal/mol per TiO2"
        }
      },
      "description": "Total energy difference per TiO2 between anatase and rutile, and the thermodynamically more stable phase."
    }
  ],
  "notes": "All outputs are numerical results from first-principles DFT calculations. The checker compares them against hidden reference values within appropriate tolerances to assess reproduction accuracy."
}
```

## How you are scored
A hidden verifier reads each of the five CSV output files and independently compares your reported values against hidden reference data using appropriate numeric tolerances. It also checks that certain physical trends hold (e.g., the ordering of bulk moduli between the two phases). Each scored artifact carries a weight, and the final reward is the weighted sum of the per-artifact scores. Reporting accurate results for both pseudopotential types will earn full credit; results for only one type may earn partial credit. The verifier does not re-run DFT calculations.
