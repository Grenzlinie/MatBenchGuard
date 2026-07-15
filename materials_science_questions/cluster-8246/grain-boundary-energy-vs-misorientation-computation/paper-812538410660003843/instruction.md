# Oxygen segregation energies in Σ3{111} silicon grain boundary under strain and vacancies

## Problem background
Multi-crystalline silicon used in solar cells contains grain boundaries (GBs) that can act as segregation sites for impurities such as oxygen. The segregation of oxygen atoms at GBs modifies the electronic properties and can influence solar cell efficiency. The present task investigates the energetics of oxygen segregation at the Σ3{111} Si grain boundary under different conditions: pristine unstrained, under local and global tensile/compressive strain, and in the presence of silicon vacancies. The goal is to compute the segregation energy of oxygen interstitials in these various GB environments and to understand how strain and vacancies affect the segregation propensity.

## Approach
Density functional theory (DFT) calculations using the PBE exchange-correlation functional are performed to obtain total energies of the Σ3{111} Si GB supercell and bulk Si reference systems. The GB formation energy is computed from the total energy per atom of bulk Si and the GB cell. Oxygen atoms are then introduced as interstitials in the GB in several configurations and the system is relaxed. The segregation energy is defined as the difference between the impurity energy in the GB and that in bulk Si, which itself is computed from the bulk total energies with O impurities and the chemical potential of oxygen (derived from the O2 molecule). To probe the role of strain, two types of strain are applied starting from the lowest-energy pristine configurations: (i) local strain, where specific bond lengths close to the O atoms are elongated or compressed; (ii) global strain, where the in-plane lattice parameters are uniformly scaled while keeping the GB separation fixed. For strained structures, only a self-consistent electronic calculation is performed (no ionic relaxation) to preserve the imposed strain. The effect of Si vacancies is studied by creating two distinct vacancy positions in the GB, relaxing the resulting structures, and then inserting O atoms in various configurations. For each condition (pristine, local/global strain, V1/V2 vacancy) and each number of oxygen atoms n=1–4, the segregation energies of the lowest-energy (LE) and highest-energy (HE) configurations are recorded.

## Reproduction target
The reproduction target is to compute and provide two scored artifacts:

1. A text file containing the formation energy of the pristine Σ3{111} Si grain boundary (in J/m²).
2. A CSV file containing the computed oxygen segregation energies (in eV) for the following conditions: pristine unstrained, local strain (+3.7% and +5.7% bond elongation near O), global strain (+3.0%, +0.5%, -0.5%, -3.0% uniform scaling of a and b lattice parameters), and with a V1 or V2 silicon vacancy. Each row of the CSV must specify the condition, number of oxygen atoms n_O (1–4), configuration type (LE or HE), and the segregation energy. The CSV must include both LE and HE configurations for every condition and n_O.

These artifacts will be checked against hidden physical consistency criteria.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE PAW pseudopotentials for Si and O: https://www.materialscloud.org/discover/sssp/table
- GB Studio: https://github.com/ryokbys/gbstudio
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Bulk Si reference DFT calculation
- Role: process
- Action: Using an open-source DFT code (e.g., Quantum ESPRESSO) with GGA-PBE exchange-correlation functional, compute the total energy of a cubic Si bulk supercell containing 64 atoms with a lattice constant of 10.86 Å. Obtain the energy per Si atom (e_B) for subsequent formation and segregation energy evaluations.
- Evidence: `/app/outputs/si_bulk_energy.log`

### Step 2: Bulk Si + O impurity reference DFT calculation
- Role: process
- Action: Compute the total energy of an O2 molecule in vacuum and the total energies of bulk Si supercells containing 1, 2, 3, and 4 interstitial O atoms in various configurations using the same DFT functional. Derive the oxygen chemical potential μ_O (energy per O atom) and record the bulk impurity total energies E_{nO+B} for n=1–4.
- Evidence: `/app/outputs/oxygen_reference.log`

### Step 3: Pristine Σ3{111} Si GB formation energy
- Role: scored
- Action: Construct the orthorhombic Σ3{111} Si GB supercell (96 Si atoms, lattice parameters a=13.30 Å, b=7.68 Å, c=18.81 Å). Relax the structure with DFT. Compute the total energy E_GB and the GB formation energy E_GB^f = (E_GB - 96 * e_B) / (2 * A), where A is the GB cross-sectional area and e_B is from step 1. Write the formation energy in J/m² to the output file.
- Output file: `/app/outputs/pristine_GB_formation_energy.txt`
- Format: txt
- Contract: Plain text file with one floating-point number (unit: J/m²).
- Scoring: scored by hidden verifier

### Step 4: Interstitial O segregation energy in pristine Σ3{111} GB
- Role: process
- Action: For n=1,2,3,4 oxygen atoms, insert O atoms in many distinct starting configurations into the pristine GB supercell. Fully relax each structure with DFT. Identify the lowest-energy (LE) and highest-energy (HE) configurations for each n. Compute the impurity energy E^{nOGB} = E_{nO+GB} - E_GB - n*μ_O and the bulk impurity energy E^{nOB} = E_{nO+B} - E_B - n*μ_O using references from steps 1–2. Calculate the segregation energy Δ = E^{nOGB} - E^{nOB}. Retain these values for later aggregation.
- Evidence: `/app/outputs/pristine_seg.log`

### Step 5: Strained GB segregation energies
- Role: process
- Action: Starting from the LE pristine GB+nO structures, apply two types of strain: (i) local strain (LS): modify bond lengths near the O atoms (e.g., +3.7%, +5.7% elongation); (ii) global strain (GS): change the a and b lattice parameters while keeping c fixed (e.g., +3.0%, +0.5%, -0.5%, -3.0%). For each strained configuration, perform a self-consistent DFT calculation (no full relaxation) to obtain the total energy. Compute the impurity energy E^{nOSGB} = E_{nO+SGB} - E_SGB - n*μ_O and the segregation energy Δ = E^{nOSGB} - E^{nOGB}. Record the results.
- Evidence: `/app/outputs/strained_seg.log`

### Step 6: Vacancy formation energy in Σ3{111} GB
- Role: process
- Action: Introduce the two distinct Si vacancies V1 and V2 into the pristine GB supercell. Relax the structures with DFT. Compute the vacancy formation energy E_VGB^f = E_VGB - (95/96) * E_GB. Also record the total energies of the relaxed V1 and V2 structures for use in step 7.
- Evidence: `/app/outputs/vacancy_formation.log`

### Step 7: Oxygen segregation in GB with a Si vacancy
- Role: process
- Action: For each vacancy (V1, V2), insert n=1,2,3,4 oxygen atoms in various configurations, including both bond‑centered positions and sites adjacent to the dangling bonds. Relax the structures with DFT. Identify LE (lowest total energy) and HE (highest total energy) configurations. Compute the impurity energy E^{nOVGB} = E_{nO+VGB} - E_VGB - n*μ_O and the segregation energy Δ = E^{nOVGB} - E^{nOGB}. Record these values.
- Evidence: `/app/outputs/vacancy_o_seg.log`

### Step 8: Compile segregation energies into scored CSV
- Role: scored (load-bearing)
- Action: Collect all segregation energy results from steps 4, 5, and 7. Write a CSV file containing one row per combination of condition, n_O, config_type, and the computed segregation energy in eV. Conditions include: 'pristine', 'LS_+3.7%', 'LS_+5.7%', 'GS_+3.0%', 'GS_+0.5%', 'GS_-0.5%', 'GS_-3.0%', 'V1', 'V2'. For each condition and n_O, include rows for the lowest-energy (LE) and highest-energy (HE) configuration types.
- Output file: `/app/outputs/segregation_energies.csv`
- Format: csv
- Contract: Columns: condition (string), n_O (integer), config_type (string: 'LE' or 'HE'), seg_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_GB_formation_energy.txt`
- `/app/outputs/segregation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_GB_formation_energy.txt
- path: `/app/outputs/pristine_GB_formation_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed formation energy of the pristine Σ3{111} Si grain boundary, compared to the paper's reported low-distortion value.
- schema:
  - `type`: text
  - `units`: J/m²

### segregation_energies.csv
- path: `/app/outputs/segregation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Compiled oxygen segregation energies for pristine, strained, and vacancy-containing GB configurations. Checked for correct sign and monotonic trends.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `n_O`, `config_type`, `seg_energy_eV`
  - `units`:
    - `seg_energy_eV`: eV

Notes: The exact numerical values are not expected to match the paper's VASP results; the scoring verifies that the segregation energy signs and trends (more negative with increasing n for tensile strain and vacancies, positive for compressive strain) are correctly reproduced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_GB_formation_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "J/m²"
      },
      "description": "Computed formation energy of the pristine Σ3{111} Si grain boundary, compared to the paper's reported low-distortion value."
    },
    {
      "file": "segregation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "n_O",
          "config_type",
          "seg_energy_eV"
        ],
        "units": {
          "seg_energy_eV": "eV"
        }
      },
      "description": "Compiled oxygen segregation energies for pristine, strained, and vacancy-containing GB configurations. Checked for correct sign and monotonic trends."
    }
  ],
  "notes": "The exact numerical values are not expected to match the paper's VASP results; the scoring verifies that the segregation energy signs and trends (more negative with increasing n for tensile strain and vacancies, positive for compressive strain) are correctly reproduced."
}
```

## How you are scored
A hidden verifier independently scores each output file.

- For `pristine_GB_formation_energy.txt`, the verifier compares the computed value to an expected reference within a tolerance.
- For `segregation_energies.csv`, the verifier performs a structural audit: it groups the data by condition and checks that the segregation energies exhibit the correct sign and monotonic trends (e.g., how the energy changes with increasing n_O) for each condition type. Because the exact numerical values can differ between DFT codes (the task may be run with Quantum ESPRESSO, CP2K, or ABINIT), the tolerances are generous for absolute values, and the primary scoring is based on the reproduction of expected physical trends.

The two scored artifacts are weighted: the formation energy carries a small weight, and the CSV of segregation energies carries the majority weight. The verifier combines the scores into a final reward between 0 and 1, with higher reward for solutions that reproduce the correct trends and approximate energy scales.
