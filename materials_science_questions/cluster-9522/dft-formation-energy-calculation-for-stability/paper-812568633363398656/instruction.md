# Formation Energies and Bulk Moduli of Mg-Pd Intermetallic Phases from First-Principles DFT

## Problem background
Thermodynamic modelling of the Mg-Pd system has been hindered by missing ab initio data for the intermetallic phases that appear in the equilibrium phase diagram. In particular, formation energies, relaxed lattice constants, and bulk moduli for several Mg-Pd intermetallic compounds were either unknown or not consistently published. Obtaining these quantities from first-principles calculations is essential for building a reliable thermodynamic model and for understanding phase stability, hydrogen storage applications, and alloy design in this binary system.

## Approach
The reproduction uses density functional theory (DFT) as implemented in Quantum ESPRESSO with the General Gradient Approximation functional PBEsol, which is revised for solids. Standard PBEsol pseudopotentials for Mg and Pd (e.g., from the SSSP library) are employed. The initial crystal structures for all required phases are obtained from the Crystallography Open Database (COD). For phases with mixed Wyckoff site occupancy (Mg₆Pd and Mg₉Pd₁₁), special quasirandom structures (SQS) are generated to model the random occupation (using the Supercell code to enumerate permutations and GULP, or an equivalent approach, to select the most probable SQS configuration). All structures are then fully relaxed with Quantum ESPRESSO using the BFGS algorithm. The computation uses a plane-wave cutoff of 680 eV and a k-point spacing of 0.20 Å⁻¹; the relaxation stops when the residual stress falls below 0.5 kbar. The self-consistent field (SCF) total energies of the pure elemental reference states (Mg in R-3m and Pd in Fm-3m) and of each intermetallic compound are recorded. Formation energies per atom are calculated from the total energies, and bulk moduli are derived from the pressure–volume response obtained in the SCF runs. Finally, the relaxed lattice constants, formation energies, and bulk moduli are tabulated for all phases.

## Reproduction target
Produce a CSV file, `results.csv`, with one row for each of the following ten phases: Mg, Pd, Mg₆Pd, Mg₃Pd, Mg₅Pd₂, MgPd, Mg₉Pd₁₁, Mg₃Pd₅, MgPd₂, MgPd₃. For each phase, the file must report the formation energy per atom (eV/atom), the relaxed lattice constants a, b, c (in Å), and the bulk modulus (GPa). The formation energy of the pure elements is defined as 0.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Crystallography Open Database (COD): http://www.crystallography.net/cod/
- GGA-PBESol pseudopotentials for Mg and Pd: https://www.materialscloud.org/discover/sssp/
- Supercell code: https://github.com/okhotnikov/supercell
- GULP (General Utility Lattice Program): https://www.chemguide.org/gulp/

## Workflow steps

### Step 1: Obtain initial crystal structures from COD
- Role: process
- Action: Retrieve crystallographic data for all required phases (Mg in R-3m, Pd in Fm-3m, and intermetallics Mg6Pd, Mg3Pd, Mg5Pd2, MgPd, Mg9Pd11, Mg3Pd5, MgPd2, MgPd3) from the Crystallography Open Database. Save the geometry files.
- Evidence: none

### Step 2: Generate SQS structures for mixed-occupancy phases
- Role: process
- Action: For Mg6Pd and Mg9Pd11, which have mixed Wyckoff site occupancy, use an SQS method (e.g., Supercell code to enumerate permutations and GULP to select the optimal SQS, or an equivalent approach) to generate special quasirandom structure supercells that model the random occupancy. Produce the SQS supercell structure files.
- Evidence: `/app/outputs/sqs_generation.log`

### Step 3: Run DFT calculations for all structures
- Role: process
- Action: Using Quantum ESPRESSO with the GGA-PBESol pseudopotentials, plane-wave cut-off 680 eV, k-point spacing 0.20 1/Å, and BFGS relaxation with stress threshold 0.5 kbar, perform a full structural relaxation and a self-consistent field (SCF) calculation for each of the pure elements (Mg in R-3m, Pd in Fm-3m) and for every intermetallic compound (using the structures from step1 and the SQS supercells from step2). Record the total energies, final relaxed lattice parameters, cell volumes, and pressure for each run.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 4: Compute formation energies and bulk moduli
- Role: scored (load-bearing)
- Action: From the DFT outputs, calculate for each intermetallic phase: (1) formation energy per atom using ΔE⁰ = (E_compound – m·E_Pd – n·E_Mg) / (m+n), where E_Mg and E_Pd are the total energies of the pure Mg (R-3m) and Pd (Fm-3m) references, and n, m are the atom counts; (2) bulk modulus from the pressure–volume data using K = –V·dP/dV. Include the pure elements with formation energy 0 and their calculated bulk moduli. Report the relaxed lattice constants a, b, c (in Å) for every phase. Write all results to a CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: phase (string), formation_energy_eV_per_atom (float, eV/atom), a_angstrom (float, Å), b_angstrom (float, Å), c_angstrom (float, Å), bulk_modulus_GPa (float, GPa). One row for each of: Mg, Pd, Mg6Pd, Mg3Pd, Mg5Pd2, MgPd, Mg9Pd11, Mg3Pd5, MgPd2, MgPd3 (10 rows total).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the computed formation energies per atom, relaxed lattice constants, and bulk moduli for the pure elements and all Mg-Pd intermetallic phases listed in the output schema.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `formation_energy_eV_per_atom`, `a_angstrom`, `b_angstrom`, `c_angstrom`, `bulk_modulus_GPa`
  - `units`:
    - `formation_energy_eV_per_atom`: eV/atom
    - `a_angstrom`: Å
    - `b_angstrom`: Å
    - `c_angstrom`: Å
    - `bulk_modulus_GPa`: GPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "formation_energy_eV_per_atom",
          "a_angstrom",
          "b_angstrom",
          "c_angstrom",
          "bulk_modulus_GPa"
        ],
        "units": {
          "formation_energy_eV_per_atom": "eV/atom",
          "a_angstrom": "Å",
          "b_angstrom": "Å",
          "c_angstrom": "Å",
          "bulk_modulus_GPa": "GPa"
        }
      },
      "description": "CSV file containing the computed formation energies per atom, relaxed lattice constants, and bulk moduli for the pure elements and all Mg-Pd intermetallic phases listed in the output schema."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your results are evaluated by a hidden verifier. For each scored workflow stage the verifier independently checks the content of the corresponding output artifact against a reference. The final reward is a weighted combination of these stage-level checks. Submitting only the expected table of numbers without genuinely running the computational pipeline will not suffice to meet the verification criteria.
