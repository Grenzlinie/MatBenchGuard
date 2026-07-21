# Compute BiCuSeO vacancy formation energies under pressure using DFT

## Problem background
BiCuSeO oxyselenides are promising candidates for high-temperature thermoelectric energy conversion. Their electrical conductivity is strongly influenced by native point defects, especially bismuth and copper vacancies. First-principles density functional theory (DFT) calculations can quantify the formation energies of these vacancies and reveal how they respond to applied hydrostatic pressure. Understanding the pressure dependence helps elucidate the microscopic origin of improved thermoelectric performance observed after high-pressure sintering.

## Approach
Use an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with standard projector-augmented-wave pseudopotentials to perform total energy calculations. Build a supercell of tetragonal BiCuSeO (space group P4/nmm, No. 129) and create three configurations: a pristine supercell, a supercell with a single bismuth vacancy, and a supercell with a single copper vacancy. Additionally, compute the chemical potentials of metallic bismuth and copper from bulk elemental calculations. For each of the four hydrostatic pressures (0, 3, 6, and 9 GPa), obtain the total energies of the pristine and defective supercells by compressing the lattice accordingly. Then calculate the vacancy formation energy for each species as the energy of the defective supercell minus the energy of the pristine supercell, plus the chemical potential of the removed atom.

## Reproduction target
Compute the vacancy formation energies of Bi and Cu in BiCuSeO at pressures of 0, 3, 6, and 9 GPa. Output the results into a CSV file at `/app/outputs/vacancy_formation_energies.csv` with three columns: `pressure` (in GPa), `formation_energy_Bi` (in eV), and `formation_energy_Cu` (in eV). One row should be present for each of the four pressures. The data will be used to evaluate whether the formation energies depend on pressure and how they compare between the two vacancy types.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Pseudopotentials (SSSP efficiency library or equivalent): https://www.materialscloud.org/discover/sssp/table/efficiency
- BiCuSeO crystal structure reference

## Workflow steps

### Step 1: Compute Bi and Cu vacancy formation energies in BiCuSeO as a function of pressure
- Role: scored (load-bearing)
- Action: Perform density functional theory (DFT) calculations to compute total energies of a pristine BiCuSeO supercell and supercells with a single Bi vacancy and a single Cu vacancy, as well as the chemical potentials of metallic Bi and Cu from bulk elemental calculations. Calculate the formation energies via E_f = E_defect − E_pristine + μ_atom at pressures 0, 3, 6, and 9 GPa. Report the formation energies for Bi and Cu at each pressure.
- Output file: `/app/outputs/vacancy_formation_energies.csv`
- Format: csv
- Contract: Columns: pressure (float, unit: GPa), formation_energy_Bi (float, unit: eV), formation_energy_Cu (float, unit: eV). One row per pressure (0, 3, 6, 9 GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_formation_energies.csv
- path: `/app/outputs/vacancy_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Vacancy formation energies for Bi and Cu in BiCuSeO at different hydrostatic pressures. The checker verifies that ambient-pressure values are within tolerance of hidden reference values and that both formation energies increase monotonically with pressure.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `formation_energy_Bi`, `formation_energy_Cu`
  - `units`:
    - `pressure`: GPa
    - `formation_energy_Bi`: eV
    - `formation_energy_Cu`: eV

Notes: Only the DFT-calculated vacancy formation energies are scored. Wet-lab synthesis and transport property measurements are outside the scope of this task as they require non-public experimental data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "formation_energy_Bi",
          "formation_energy_Cu"
        ],
        "units": {
          "pressure": "GPa",
          "formation_energy_Bi": "eV",
          "formation_energy_Cu": "eV"
        }
      },
      "description": "Vacancy formation energies for Bi and Cu in BiCuSeO at different hydrostatic pressures. The checker verifies that ambient-pressure values are within tolerance of hidden reference values and that both formation energies increase monotonically with pressure."
    }
  ],
  "notes": "Only the DFT-calculated vacancy formation energies are scored. Wet-lab synthesis and transport property measurements are outside the scope of this task as they require non-public experimental data."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/vacancy_formation_energies.csv`. It first confirms that the file is well-formed and contains the required columns and rows. It then assesses the numerical values against predefined correctness criteria. The reward depends on physical consistency: the magnitude and relative ordering of the formation energies at ambient pressure, and whether the computed energies exhibit a plausible trend with pressure (e.g., monotonic behavior). You do not need to match any specific published number; the verifier uses its own hidden reference. Your task is to perform the DFT calculations faithfully and report the energies you extract.
