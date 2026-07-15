# DFT Analysis of Si-doped HA-TiO2 Interface Bonding

## Problem background
Hydroxyapatite (HA) coatings on titanium implants are widely used to enhance biocompatibility. Introducing silicon as a dopant is known to influence the bioactivity of the coating, but its effect on the fundamental adhesion mechanism at the atomic scale between the HA coating and the titanium oxide substrate is not fully understood. This task focuses on determining how silicon substitution in amorphous HA alters the interfacial bonding with amorphous TiO2 by computing key properties such as the work of adhesion, the integral charge transfer, and the interfacial bond lengths using density functional theory (DFT).

## Approach
The workflow uses classical molecular dynamics (ReaxFF) to generate amorphous HA and TiO2 slabs, which are then combined to form an HA/TiO2 interface. A Si-doped variant is created by replacing one phosphorus atom with silicon in a phosphate group and introducing a charge-compensating OH vacancy. Both undoped and Si-doped interfaces are then relaxed using plane-wave DFT (PBE exchange-correlation) within an open-source code such as Quantum ESPRESSO. From the optimized geometries and total energies, the work of adhesion is computed as the energy required to separate the interface, divided by the interfacial area. Subsequent Bader charge analysis yields the integral charge transfer between coating and substrate. Finally, interfacial Ti–O and Ca–O bond distances are extracted from the relaxed structures to characterize the chemical bonding pattern.

## Reproduction target
Produce three scored artifacts:
1) step_02_work_of_adhesion.csv containing the work of adhesion (in J/m²) for both the undoped and Si-doped interfaces, along with the total energies and interface area used in the calculation.
2) step_03_charge_transfer.csv reporting the integral charge transfer (in electrons) for each interface from Bader analysis.
3) step_04_bond_lengths.txt listing the identified interfacial Ti–O and Ca–O bond lengths (in Å) for both interfaces, with bond type and distance information.
The task requires executing the full pipeline from slab generation to DFT relaxation and analysis, and reporting the computed values for both interfaces. The objective is to provide a complete set of computed interfacial properties that can be compared between the undoped and doped cases.

## Assets

- Crystal structure of hydroxyapatite (ICSD 26204): https://www.crystallography.net/cod/
- Crystal structure of rutile TiO2 (ICSD 9163): https://www.crystallography.net/cod/
- ReaxFF force field for Ca/P/O/H/Ti systems: https://www.lammps.org
- LAMMPS molecular dynamics simulator: https://www.lammps.org
- Quantum ESPRESSO open-source DFT code: https://www.quantum-espresso.org
- Bader charge analysis code (Henkelman group): http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Generate interface models and perform DFT relaxation
- Role: process
- Action: Using the ReaxFF force field with LAMMPS, amorphize a hydroxyapatite (001) slab and a rutile TiO2 (110) slab, each about 1 nm thick. Build an a-HA/a-TiO2 interface model. Create a Si-doped variant by substituting one P with Si and adding an OH vacancy. Optimize both interface models with DFT using Quantum ESPRESSO (PBE functional, plane-wave cutoff equivalent to 500 eV, 6×6×1 k-point grid). Compute total energies of the isolated slabs (frozen at the interface geometry). Save all optimized coordinates, total energies, and charge densities.
- Evidence: `/app/outputs/step_01_interface_models.tar.gz`

### Step 2: Work of adhesion
- Role: scored (load-bearing)
- Action: From the total energies produced in step 1, compute the work of adhesion W_ad = (E_total - E_HA - E_TiO2) / A, where A is the interface surface area. Output a CSV with columns: interface (undoped or sidoped), w_ad (J/m²), area (Å²), total_energy_interface (Ry), total_energy_slab1 (Ry), total_energy_slab2 (Ry).
- Output file: `/app/outputs/step_02_work_of_adhesion.csv`
- Format: csv
- Contract: CSV with columns: interface (string), w_ad (float, J/m²), area (float, Å²), total_energy_interface (float, Ry), total_energy_slab1 (float, Ry), total_energy_slab2 (float, Ry).
- Scoring: scored by hidden verifier

### Step 3: Integral charge transfer
- Role: scored
- Action: Perform Bader charge analysis on the charge density of the optimized interfaces to obtain the integral charge transfer between the coating and substrate. Output a CSV with columns: interface (undoped or sidoped), ict (electrons).
- Output file: `/app/outputs/step_03_charge_transfer.csv`
- Format: csv
- Contract: CSV with columns: interface (string), ict (float, electrons).
- Scoring: scored by hidden verifier

### Step 4: Interfacial bond lengths
- Role: scored
- Action: Extract interfacial Ti–O and Ca–O bond lengths from the optimized geometries of step 1. Identify bonds with distances <2.5 Å for Ca–O and <2.3 Å for Ti–O. Output a plain text file listing bond types and lengths for each interface.
- Output file: `/app/outputs/step_04_bond_lengths.txt`
- Format: txt
- Contract: Plain text containing bond descriptions. Example format: 'Undoped: Ti–O 1.83 Å, Ca–O 2.43 Å (3 bonds: 2.36, 2.43, 2.50 Å). Si-doped: Ti–O 1.90 Å and 2.22 Å, Ca–O 2.34, 2.44, 2.46 Å (3 bonds).'
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_work_of_adhesion.csv`
- `/app/outputs/step_03_charge_transfer.csv`
- `/app/outputs/step_04_bond_lengths.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_work_of_adhesion.csv
- path: `/app/outputs/step_02_work_of_adhesion.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Work of adhesion (w_ad) computed from DFT total energies. Scored by verifying that the absolute work of adhesion for the Si-doped interface is at least 10% higher than that of the undoped interface.
- schema:
  - `type`: table
  - `required_columns`: `interface`, `w_ad`, `area`, `total_energy_interface`, `total_energy_slab1`, `total_energy_slab2`
  - `units`:
    - `w_ad`: J/m²
    - `area`: Å²
    - `total_energy_interface`: Ry
    - `total_energy_slab1`: Ry
    - `total_energy_slab2`: Ry

### step_03_charge_transfer.csv
- path: `/app/outputs/step_03_charge_transfer.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Integral charge transfer (ICT) computed via Bader analysis. Scored by verifying that the magnitude of ICT for the Si-doped interface is smaller (closer to zero) than that of the undoped interface.
- schema:
  - `type`: table
  - `required_columns`: `interface`, `ict`
  - `units`:
    - `ict`: electrons

### step_04_bond_lengths.txt
- path: `/app/outputs/step_04_bond_lengths.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Plain text file listing interfacial Ti–O and Ca–O bond lengths for each interface. Scored by checking the bonding pattern: undoped interface should have one Ti–O bond and three Ca–O bonds; Si-doped interface should have two Ti–O bonds and three Ca–O bonds, with distances consistent with the described ranges.
- schema:
  - `type`: text

Notes: Trend-based scoring: the Si-doped interface must show a higher absolute work of adhesion (≥10% relative) and a lower magnitude of integral charge transfer compared to the undoped interface. Bond lengths must adhere to the structural pattern described in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_work_of_adhesion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "interface",
          "w_ad",
          "area",
          "total_energy_interface",
          "total_energy_slab1",
          "total_energy_slab2"
        ],
        "units": {
          "w_ad": "J/m²",
          "area": "Å²",
          "total_energy_interface": "Ry",
          "total_energy_slab1": "Ry",
          "total_energy_slab2": "Ry"
        }
      },
      "description": "Work of adhesion (w_ad) computed from DFT total energies. Scored by verifying that the absolute work of adhesion for the Si-doped interface is at least 10% higher than that of the undoped interface."
    },
    {
      "file": "step_03_charge_transfer.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "interface",
          "ict"
        ],
        "units": {
          "ict": "electrons"
        }
      },
      "description": "Integral charge transfer (ICT) computed via Bader analysis. Scored by verifying that the magnitude of ICT for the Si-doped interface is smaller (closer to zero) than that of the undoped interface."
    },
    {
      "file": "step_04_bond_lengths.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Plain text file listing interfacial Ti–O and Ca–O bond lengths for each interface. Scored by checking the bonding pattern: undoped interface should have one Ti–O bond and three Ca–O bonds; Si-doped interface should have two Ti–O bonds and three Ca–O bonds, with distances consistent with the described ranges."
    }
  ],
  "notes": "Trend-based scoring: the Si-doped interface must show a higher absolute work of adhesion (≥10% relative) and a lower magnitude of integral charge transfer compared to the undoped interface. Bond lengths must adhere to the structural pattern described in the paper."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three output artifacts. For the work of adhesion (step_02), the verifier checks whether the relationship between the two computed values meets a predefined criterion. For the integral charge transfer (step_03), the verifier similarly compares the two values against an expected relationship. For the bond length file (step_04), the verifier validates the bonding pattern by examining the types and distances of reported bonds. Each artifact is assigned a weight, and your total score is the weighted sum. Simply reporting the paper's numbers is not enough; the artifacts must be the result of executing the described computational workflow.
