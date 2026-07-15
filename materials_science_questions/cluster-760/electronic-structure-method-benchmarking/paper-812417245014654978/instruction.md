# ICN Adsorption and Decomposition on Si(100)-(2×1): DFT Potential Energy Profile Reproduction

## Problem background
This work addresses the adsorption and surface reaction pathways of ICN on the Si(100)-(2×1) surface, studied using density functional theory on a Si9H12 single-dimer cluster. The aim is to understand the stability and interconversion of molecularly and dissociatively adsorbed species, and to map the potential-energy profile that controls surface reactivity. The computed energetics are particularly relevant for interpreting experimental observations and for contrasting the ICN system with the analogous HCN surface chemistry. The key open question is what relative energies and reaction barriers emerge for the various adsorption minima and transition states.

## Approach
The investigation employs hybrid density functional theory with the B3LYP functional. A mixed basis set is used: the LanL2DZ effective core potential and basis for iodine atoms, and the 6-31G* basis for silicon, carbon, and nitrogen. The Si(100)-(2×1) surface is modeled by a single-dimer Si9H12 cluster, whose geometry is constructed from standard surface models. Geometry optimizations and vibrational frequency calculations are carried out for each stationary point (minima and transition states). The computed total electronic energies are then used to evaluate relative energies, taking the separated cluster and gas-phase molecule (ICN or INC) as the energy reference. This approach yields the potential-energy profile for the ICN adsorption and decomposition pathways.

## Reproduction target
Compute relative energies (in kJ/mol) for all ICN- and INC-derived stationary points on the Si9H12 single-dimer cluster at the B3LYP/LanL2DZ+6-31G* level. The required structures are: ICN1, ICN2, SiNC, SiCN, TS1, TS2, TS3, TS4, INC2, TS5, and the constrained INC1 (INC angle fixed at 180°). For each structure, report both the total electronic energy in hartree and the relative energy with respect to the appropriate separated reference: Si9H12 + ICN for the ICN-derived species, and Si9H12 + INC for the INC-derived species. The final result must be written as a CSV file.

## Assets

- Quantum chemistry package (Psi4, ORCA, or PySCF): https://psicode.org/
- Basis set definitions (LanL2DZ effective core potential and 6-31G*): https://www.basissetexchange.org/

## Workflow steps

### Step 1: Build and optimize reference systems
- Role: process
- Action: Construct the Si9H12 single-dimer cluster model from standard Si(100)-(2×1) surface geometry (as used in prior HCN literature). Optimize the bare cluster geometry at B3LYP/LanL2DZ+6-31G*. Compute total electronic energies of isolated ICN and INC molecules at the same level to serve as reference energies.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 2: Optimize ICN adsorption minima and transition states
- Role: process
- Action: Build starting geometries for the four minima (ICN1, ICN2, SiNC, SiCN) and the four transition states (TS1, TS2, TS3, TS4) on the Si9H12 cluster. Run full geometry optimizations and frequency calculations at B3LYP/LanL2DZ+6-31G*. Confirm that every transition state has exactly one imaginary frequency. For INC1, apply a collinear INC angle constraint (180°) to obtain the constrained-structure energy.
- Evidence: `/app/outputs/icn_stationary_points.log`

### Step 3: Optimize INC side-on structure and TS5
- Role: process
- Action: Build and optimize the side-on INC2 minimum and the transition state TS5 connecting INC2 to SiCN on the Si9H12 cluster. Perform frequency calculations; verify TS5 has exactly one imaginary frequency.
- Evidence: `/app/outputs/inc_stationary_points.log`

### Step 4: Compile energy table
- Role: scored
- Action: Extract total electronic energies (Hartree) from all completed calculations. Compute relative energies (kJ/mol) using the appropriate separated-system reference: Si9H12 + ICN for ICN-derived species, Si9H12 + INC for INC-derived species. Write a CSV file containing one row per structure with columns: structure (string), total_energy_hartree (float), relative_energy_kJmol (float). Structures to include: ICN1, ICN2, SiNC, SiCN, TS1, TS2, TS3, TS4, INC2, TS5, and the constrained INC1.
- Output file: `/app/outputs/step_01_energies.csv`
- Format: csv
- Contract: structure:string,total_energy_hartree:float,relative_energy_kJmol:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energies.csv
- path: `/app/outputs/step_01_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stationary-point energies for ICN and INC adsorption on the Si(100)-(2x1) single-dimer cluster at B3LYP/LanL2DZ+6-31G*. Contains 11 rows covering all minima and transition states from the paper's potential-energy diagram.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `total_energy_hartree`, `relative_energy_kJmol`
  - `units`:
    - `total_energy_hartree`: hartree
    - `relative_energy_kJmol`: kJ/mol

Notes: The checker compares each reported relative_energy_kJmol to gold reference values (derived from the original paper) and also verifies that the SiNC→SiCN barrier computed as TS4_relative minus SiNC_relative matches the paper's value within an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "total_energy_hartree",
          "relative_energy_kJmol"
        ],
        "units": {
          "total_energy_hartree": "hartree",
          "relative_energy_kJmol": "kJ/mol"
        }
      },
      "description": "Stationary-point energies for ICN and INC adsorption on the Si(100)-(2x1) single-dimer cluster at B3LYP/LanL2DZ+6-31G*. Contains 11 rows covering all minima and transition states from the paper's potential-energy diagram."
    }
  ],
  "notes": "The checker compares each reported relative_energy_kJmol to gold reference values (derived from the original paper) and also verifies that the SiNC→SiCN barrier computed as TS4_relative minus SiNC_relative matches the paper's value within an appropriate tolerance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks the relative energies you report. The verifier compares each relative energy to reference values derived from the original study, using a tolerance that accounts for legitimate differences in quantum chemistry implementations. In addition, the barrier between SiNC and SiCN (computed as the relative energy of TS4 minus the relative energy of SiNC) is checked against the expected barrier height. You must perform the full DFT workflow; simply copying known numbers will not satisfy the scoring protocol, because the hidden comparison tolerances require genuine computational results.
