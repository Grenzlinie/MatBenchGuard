# DFT-based calculation of formation energies and bulk moduli for Mg-Pd intermetallics

## Problem background
The Mg–Pd system is of interest for hydrogen storage applications. A reliable thermodynamic model of this system is not yet available, partly because consistent data for formation energies, relaxed lattice constants, and bulk moduli of all reported intermetallic phases is missing. This task aims to provide such a consistent set of first‑principles data for every known Mg–Pd intermetallic phase, including the phases Mg6Pd and Mg9Pd11 for which these quantities have not been previously computed. The computed properties will serve as a basis for future phase‑equilibrium modelling of this promising hydrogen‑storage material.

## Approach
The calculations are performed with density functional theory (DFT) within the generalized gradient approximation (GGA), using a functional revised for solids (PBESol) as implemented in the open‑source Quantum ESPRESSO suite. Crystal structures of all phases are taken from the Crystallography Open Database and are fully relaxed. For the two phases that exhibit mixed atomic occupation at crystallographic sites (Mg6Pd and Mg9Pd11), special quasirandom structures (SQS) are generated to represent the disordered arrangement; any publicly available tool for SQS generation (such as the Supercell code or pymatgen) may be used. Total energies are computed for the pure elements Mg and Pd and for every intermetallic phase. Formation energies per atom are then derived from the total energies using the standard formula, and bulk moduli are obtained from the pressure–volume data via the definition K = −V dP/dV. The final step assembles all results—formation energies, relaxed lattice constants, and bulk moduli—into a single table for all phases.

## Reproduction target
Using the described DFT workflow, compute the formation energy per atom (eV/atom), the relaxed lattice constants a, b, c (Å), and the bulk modulus (GPa) for each of the following phases: Mg, Pd, Mg6Pd, Mg3Pd, Mg5Pd2, MgPd, Mg9Pd11, Mg3Pd5, MgPd2, and MgPd3. Report the results in the CSV file `/app/outputs/phase_properties.csv` according to the output contract below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Crystallography Open Database: http://www.crystallography.net/cod/
- Supercell code (SQS generation): 10.1186/s13321-016-0128-6
- GULP: https://www.materials.manchester.ac.uk/research/themes/chemistry/
- pymatgen: pymatgen

## Workflow steps

### Step 1: Retrieve initial crystal structures from COD
- Role: process
- Action: Obtain crystallographic structures for all Mg-Pd intermetallic phases and pure elements Mg and Pd from the Crystallography Open Database (COD).
- Evidence: none

### Step 2: Generate SQS structures for mixed-occupancy phases
- Role: process
- Action: For Mg6Pd and Mg9Pd11 (phases with mixed Wyckoff occupancy), generate special quasirandom structures (SQS) to determine the most probable atomic arrangements using an appropriate tool (pymatgen or Supercell code).
- Evidence: none

### Step 3: DFT calculations on pure Mg and Pd
- Role: process
- Action: Run DFT calculations with Quantum ESPRESSO on Mg (R-3m structure) and Pd (Fm-3m structure) to obtain total energies, relaxed lattice constants, and pressure-volume data for bulk modulus computation.
- Evidence: none

### Step 4: DFT calculations on all Mg-Pd intermetallic phases
- Role: process
- Action: Perform DFT calculations with the same settings as for pure elements on all intermetallic phases: Mg6Pd, Mg3Pd, Mg5Pd2, MgPd, Mg9Pd11, Mg3Pd5, MgPd2, MgPd3. Use the retrieved structures (SQS for Mg6Pd and Mg9Pd11). Obtain total energies, relaxed lattice constants, and pressure-volume data.
- Evidence: none

### Step 5: Compile phase properties table
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute per-atom formation energies using the standard formation energy formula (ΔE = (E_compound − m·E_Pd − n·E_Mg) / (m+n)). Extract relaxed lattice constants from the geometry optimizations. Compute bulk moduli from pressure-volume data (K = −V dP/dV). Assemble all results into a CSV file with columns: phase, structure, formation_energy_eV_atom, a_A, b_A, c_A, bulk_modulus_GPa. Include all phases from the paper’s Table 1 (Mg, Pd, Mg6Pd, Mg3Pd, Mg5Pd2, MgPd, Mg9Pd11, Mg3Pd5, MgPd2, MgPd3).
- Output file: `/app/outputs/phase_properties.csv`
- Format: csv
- Contract: CSV with columns: phase (string), structure (string space group), formation_energy_eV_atom (float, eV/atom), a_A (float, Å), b_A (float, Å), c_A (float, Å), bulk_modulus_GPa (float, GPa). One row per phase.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_properties.csv
- path: `/app/outputs/phase_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of computed formation energies, relaxed lattice constants, and bulk moduli for all Mg-Pd intermetallic phases and pure elements. The checker compares each value against the paper-reported reference values with appropriate tolerances and also verifies that all formation energies lie on the convex hull at 0 K.
- schema:
  - `type`: table
  - `columns`:
    - `phase`: string
    - `structure`: string (space group)
    - `formation_energy_eV_atom`: float
    - `a_A`: float
    - `b_A`: float
    - `c_A`: float
    - `bulk_modulus_GPa`: float

Notes: The hidden checker will additionally perform a structural audit: it computes the convex hull from the Pd mole fraction and formation energies, and verifies that no reported point lies above the hull.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": {
          "phase": "string",
          "structure": "string (space group)",
          "formation_energy_eV_atom": "float",
          "a_A": "float",
          "b_A": "float",
          "c_A": "float",
          "bulk_modulus_GPa": "float"
        }
      },
      "description": "Table of computed formation energies, relaxed lattice constants, and bulk moduli for all Mg-Pd intermetallic phases and pure elements. The checker compares each value against the paper-reported reference values with appropriate tolerances and also verifies that all formation energies lie on the convex hull at 0 K."
    }
  ],
  "notes": "The hidden checker will additionally perform a structural audit: it computes the convex hull from the Pd mole fraction and formation energies, and verifies that no reported point lies above the hull."
}
```

## How you are scored
A hidden verifier will read your `phase_properties.csv` and compare every reported value—formation energy, lattice constant, and bulk modulus—against reference values that were obtained by following the same computational protocol. The comparison uses appropriate tolerances; meeting or exceeding the reference quality (e.g., getting a formation energy that is as low as or lower than the reference) is considered successful. In addition, the verifier checks that the set of formation energies satisfies the convex‑hull stability condition at 0 K (no formation energy lies above the convex hull). The final reward is a weighted combination of these checks; simply reporting numbers without executing the full DFT pipeline will not produce a valid result.
