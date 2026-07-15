# Ab Initio Calculation of Defect Formation Energies and Lattice Distortions in Doped PbTiO3

## Problem background
Donor doping in lead-based ferroelectric perovskites can induce piezoelectric softening, yet at very low dopant concentrations anomalous behaviour such as reduced densification and deteriorated properties has been observed. The origin of these effects is linked to point defects, in particular lead-oxygen divacancies (V_Pb–V_O). This computational study uses density-functional theory (DFT) on the model perovskite PbTiO₃ to evaluate how the formation energy of the V_Pb–V_O divacancy depends on doping (acceptor Fe, donors Nb and La) and how different defect configurations affect the crystal's lattice parameters. Quantifying these defect energetics and structural distortions is essential for interpreting sintering behaviour and the hardening-to-softening transition in Pb-based ceramics.

## Approach
First-principles calculations are performed with the PBEsol exchange-correlation functional and ultrasoft pseudopotentials using the Quantum ESPRESSO code. The approach uses 3×3×3 supercells of PbTiO₃ to model: perfect PbTiO₃, a single Nb substituent on a Ti site (Nb_Ti), Nb on a Pb site, one Pb vacancy (V_Pb), the V_Pb–V_O divacancy together with a Nb_Ti substituent (multiple configurations to find the lowest energy arrangement), Fe substituting Ti, La substituting Pb, and a reference tetragonal PbO cell. For charged defects, a compensating jellium background is added. After relaxing each system, total energies and optimised cell parameters are recorded.

The formation enthalpy of the V_Pb–V_O divacancy for a given doping case is computed as:
  H = E(PbO) + E(supercell containing V_Pb–V_O and dopant) − E(supercell with dopant alone)
For the undoped case, the dopant energy is that of the pure PbTiO₃ supercell, and the divacancy-containing cell has only the V_Pb–V_O defect.

Separately, from the relaxed supercells of pure PbTiO₃, Nb on Pb site, Nb on Ti site, and one Pb vacancy, the perovskite unit-cell parameters (a, c) are obtained by dividing the supercell edge lengths by 3, and the unit-cell volume is calculated. These values quantify the lattice distortion induced by each defect type.

## Reproduction target
The task requires two scored CSV files under /app/outputs:
1. table1_formation_energies.csv – Formation energy of the V_Pb–V_O divacancy in undoped, Fe-doped, Nb-doped, and La-doped PbTiO₃, computed according to the formulation described above.
2. table2_lattice_parameters.csv – Relaxed perovskite unit-cell parameters (a, c, volume) for pure PbTiO₃, for a supercell with Nb occupying a Pb site, for Nb occupying a Ti site, and for a supercell containing one lead vacancy.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Pb, Ti, O, Nb, Fe, La: https://pseudopotentials.quantum-espresso.org/ (PBEsol, ultrasoft, from the QE pseudopotential library)

## Workflow steps

### Step 1: DFT total energy and geometry calculations
- Role: process
- Action: Set up and run DFT calculations using Quantum ESPRESSO (pw.x) for PbO (tetragonal), pure PbTiO3 3×3×3 supercell, PbTiO3 supercell with one Nb substituting Ti (Nb_Ti), PbTiO3 with Nb substituting Pb, PbTiO3 with one Pb vacancy (V_Pb), PbTiO3 with V_Pb–V_O divacancy and a Nb_Ti substituent (multiple configurations, select lowest total energy), PbTiO3 with one Fe substituting Ti (acceptor), and PbTiO3 with one La substituting Pb (donor). Use PBEsol functional, ultrasoft pseudopotentials, appropriate cutoffs, a shifted 2×2×2 Monkhorst-Pack k-point mesh, and force convergence threshold of 10⁻⁴ Ry/bohr. For charged defects, insert a compensating jellium background. Record the final total energy, relaxed atomic positions, and optimized cell parameters for each system.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 2: Formation energy analysis of V_Pb–V_O divacancy
- Role: scored (load-bearing)
- Action: Using the total energies from Step 1, compute the formation enthalpy H of the V_Pb–V_O divacancy for each doping case as described in the paper: H = E(PbO) + E(supercell with V_Pb–V_O and dopant) – E(supercell with dopant). For the undoped case, use the pure supercell energy and the energy of a supercell containing only the V_Pb–V_O divacancy (no dopant). Write the results to a CSV file.
- Output file: `/app/outputs/table1_formation_energies.csv`
- Format: csv
- Contract: CSV with columns: dopant (string, one of 'undoped', 'Fe', 'Nb', 'La'), formation_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 3: Lattice parameter extraction for defect configurations
- Role: scored
- Action: From the relaxed cell parameters obtained in Step 1 for the pure PbTiO3 supercell, the supercell with Nb on Pb site, the supercell with Nb on Ti site, and the supercell with one Pb vacancy, extract the lattice parameters of the perovskite unit cell. For the 3×3×3 supercells, divide the supercell lengths by 3 to obtain a and c (assuming a ≈ b). Compute the unit cell volume. Write the values to a CSV file.
- Output file: `/app/outputs/table2_lattice_parameters.csv`
- Format: csv
- Contract: CSV with columns: system (string, one of 'pure', 'Nb_on_Pb', 'Nb_on_Ti', 'Pb_vacancy'), a_angstrom (float), c_angstrom (float), volume_ang3 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1_formation_energies.csv`
- `/app/outputs/table2_lattice_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1_formation_energies.csv
- path: `/app/outputs/table1_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation energy of the V_Pb–V_O divacancy in undoped, Fe-doped, Nb-doped, and La-doped PbTiO3. The checker compares each formation_energy_eV to the paper-reported values with a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `dopant`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

### table2_lattice_parameters.csv
- path: `/app/outputs/table2_lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Relaxed lattice parameters a, c and cell volume for pure PbTiO3, Nb on Pb site, Nb on Ti site, and Pb vacancy. The checker compares each value to the paper-reported values with hidden tolerances.
- schema:
  - `type`: table
  - `required_columns`: `system`, `a_angstrom`, `c_angstrom`, `volume_ang3`
  - `units`:
    - `a_angstrom`: Å
    - `c_angstrom`: Å
    - `volume_ang3`: Å³

Notes: Both artifacts are scored by the hidden checker against the paper's reported values (T0 result-level comparison). The checker reads the CSVs and counts how many values are within the hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dopant",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Formation energy of the V_Pb–V_O divacancy in undoped, Fe-doped, Nb-doped, and La-doped PbTiO3. The checker compares each formation_energy_eV to the paper-reported values with a hidden tolerance."
    },
    {
      "file": "table2_lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "a_angstrom",
          "c_angstrom",
          "volume_ang3"
        ],
        "units": {
          "a_angstrom": "Å",
          "c_angstrom": "Å",
          "volume_ang3": "Å³"
        }
      },
      "description": "Relaxed lattice parameters a, c and cell volume for pure PbTiO3, Nb on Pb site, Nb on Ti site, and Pb vacancy. The checker compares each value to the paper-reported values with hidden tolerances."
    }
  ],
  "notes": "Both artifacts are scored by the hidden checker against the paper's reported values (T0 result-level comparison). The checker reads the CSVs and counts how many values are within the hidden tolerances."
}
```

## How you are scored
A hidden verifier reads your table1_formation_energies.csv and table2_lattice_parameters.csv. It compares each numeric value (formation energies, lattice parameters, volumes) to independently determined reference values derived from the original publication. Tolerances are applied to account for the natural variation among correct DFT implementations (different pseudopotential versions, float precision, convergence details). The final reward is the fraction of individual values that fall within the accepted tolerance ranges; the two outputs contribute to the overall score based on the number of checked quantities. Reporting the paper's numbers without actually performing the DFT calculations will not pass the verifier's tolerance checks, as the hidden tolerances are set to differentiate genuine re-computation from approximate guesses.
