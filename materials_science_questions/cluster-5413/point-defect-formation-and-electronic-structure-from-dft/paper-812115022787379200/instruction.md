# DFT Calculation of Vacancy Formation Energies and Midgap States in Orthorhombic LaInO3

## Problem background
Bulk single crystals of lanthanum indate (LaInO3) exhibit a weak optical absorption band between 2.8 and 4 eV, below the fundamental bandgap, which is suspected to arise from point defects. To identify the defect type responsible, density-functional-theory (DFT) calculations are performed on supercells of orthorhombic LaInO3 containing various vacancies (La, In, and oxygen in two distinct planes). The key quantities are the formation energies of these vacancies and whether they introduce occupied electronic states inside the band gap (midgap states) that could explain the sub-bandgap absorption.

## Approach
The method employs all-electron DFT with the PBEsol exchange-correlation functional, using the FHI-aims code. Starting from the experimental orthorhombic crystal structure (space group Pnma, lattice constants a=5.9380 Å, b=8.2143 Å, c=5.7227 Å), a 2×1×2 supercell containing 80 atoms is constructed. Four defect supercells are created by removing one atom: an oxygen atom from the LaO plane (denoted O^{La}), an oxygen atom from the InO2 plane (O^{In}), one In atom, and one La atom, each yielding a vacancy concentration of approximately 6.25%. The internal coordinates of each supercell are relaxed while keeping the lattice constants fixed to the experimental values. For each relaxed structure, the total energy and the Kohn-Sham band structure are computed. The formation energy per atom, Ef = (1/N)[E_tot^defect – Σ E_tot^bulk], is evaluated using N=79 and the bulk reference total energies per atom of fcc La, face-centered tetragonal In, and the O2 molecule, all calculated with the same functional and settings. The relative stability of the vacancies is then compared by their formation energies, and the band structures are inspected for the presence of occupied midgap states. The combination of stability and electronic structure allows the identification of the most likely defect type responsible for the observed weak absorption.

## Reproduction target
Compute the formation energy per atom (eV/atom) for each vacancy type (O^{In}, O^{La}, In, La) in orthorhombic LaInO3 following the DFT protocol described above. Write the results to a CSV file. Additionally, for each vacancy type, determine whether an occupied midgap state exists inside the band gap and report the presence as 'yes' or 'no' in a text file. The outcome should enable a comparison of the relative stability of the vacancies and identify which type(s) could cause the experimentally observed weak optical absorption between 2.8 and 4 eV.

## Assets

- FHI-aims DFT code: https://fhi-aims.org/
- LaInO3 crystal structure: ICSD 01-083-6124
- NOMAD repository (Figure 14 data): 10.17172/NOMAD/2021.03.16-1

## Workflow steps

### Step 1: DFT defect supercell calculations
- Role: process
- Action: Set up pristine and defect 2x1x2 supercells (80 atoms) of orthorhombic LaInO3 (Pnma). Create four defect supercells by removing one O atom from the LaO plane (O^{La}), one O atom from the InO2 plane (O^{In}), one In atom, and one La atom (yielding ~6.25% vacancy each). Perform structural relaxation (optimize internal coordinates) keeping lattice constants fixed at experimental values a=5.9380 Å, b=8.2143 Å, c=5.7227 Å. Compute total energies and Kohn-Sham band structures for the relaxed supercells using PBEsol functional in FHI-aims with tight settings. Document key convergence details and total energies in a log file.
- Evidence: `/app/outputs/defect_dft.log`

### Step 2: Formation energies
- Role: scored (load-bearing)
- Action: Compute the formation energy per atom (eV/atom) for each vacancy type (O^{In}, O^{La}, In, La) using Ef = (1/N)[E_tot^defect - Σ E_tot^bulk], where N=79 and E_tot^bulk are total energies per atom of fcc La, face-centered tetragonal In, and O₂ molecule computed at the same level of theory. Write the results to formation_energies.csv with columns: vacancy_type, formation_energy.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: vacancy_type (string), formation_energy (float)
- Scoring: scored by hidden verifier

### Step 3: Midgap state identification
- Role: scored
- Action: Examine the Kohn-Sham band structures of the four defect supercells. Determine whether an occupied state exists inside the band gap (midgap state) for each defect type. Report the result in midgap_state_report.txt as lines like '<vacancy_type>: midgap=yes' or '<vacancy_type>: midgap=no'.
- Output file: `/app/outputs/midgap_state_report.txt`
- Format: txt
- Contract: Each line: '<vacancy_type>: midgap=<yes/no>'. Example: 'La: midgap=no'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/midgap_state_report.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation energies per atom for O^{In}, O^{La}, In, and La vacancies in LaInO3.
- schema:
  - `type`: table
  - `required_columns`: `vacancy_type`, `formation_energy`
  - `units`:
    - `formation_energy`: eV/atom

### midgap_state_report.txt
- path: `/app/outputs/midgap_state_report.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Presence of midgap states for each vacancy type.
- schema:
  - `type`: text
  - `format`: Each line: '<vacancy_type>: midgap=<yes/no>'

Notes: Only the DFT defect supercell workflow is reproduced; the experimental crystal growth, characterization, and thermodynamic (FactSage) calculations are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "vacancy_type",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "eV/atom"
        }
      },
      "description": "Formation energies per atom for O^{In}, O^{La}, In, and La vacancies in LaInO3."
    },
    {
      "file": "midgap_state_report.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "Each line: '<vacancy_type>: midgap=<yes/no>'"
      },
      "description": "Presence of midgap states for each vacancy type."
    }
  ],
  "notes": "Only the DFT defect supercell workflow is reproduced; the experimental crystal growth, characterization, and thermodynamic (FactSage) calculations are excluded."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently assesses each required output artifact. The verifier compares your reported formation energies to hidden reference values with a tolerance that accounts for legitimate variation in DFT implementations, and checks both the numerical values and the qualitative midgap-state assignments (yes/no) against expected results. The scores from each artifact are combined (with appropriate weights) into a single reward between 0 and 1. Producing accurate results according to the specified DFT workflow is essential; the verifier does not simply read back the submitted numbers but cross-checks them against the required properties.
