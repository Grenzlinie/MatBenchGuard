# First-principles formation energy decomposition and dynamical stability of K-intercalated FeSe

## Problem background
Understanding the intercalation of potassium into the FeSe layers of the KxFe2-ySe2 system is key to explaining its structural stability, phase formation, and superconducting properties. When K is intercalated between FeSe layers, the total formation energy can be understood as arising from several competing contributions: the energy required to create K ion layers, the energy cost of electron doping the FeSe layers, the deformation energy of the FeSe layers, and the Coulomb attraction between the positively charged K layers and negatively charged FeSe layers. The formation energy, in turn, determines which compositions and structures are thermodynamically stable. Additionally, dynamical stability concerns, reflected in the phonon spectrum, and the tendency to form Fe vacancies at certain K contents further shape the phase behavior. This task re-examines these factors through first-principles calculations.

## Approach
The computational strategy is to use density functional theory (DFT) to compute the total energies of KxFe2Se2 structures across a range of K contents, as well as the energies of isolated fragments (neutral and charged FeSe layers, K ion layers). From these energies, the total formation energy ΔE_I is decomposed into four physically meaningful components: ΔE_K_ion_layers (formation of isolated K ion layers), ΔE_e_doping (electron doping of FeSe layers), ΔE_FeSe_deformation (structural deformation of FeSe layers), and ΔE_C (Coulomb attraction between the layers). To assess dynamical stability, phonon density-of-states calculations are performed for selected compositions using the finite-displacement or density-functional perturbation theory approach, post-processed with Phonopy. The optimized lattice parameters are extracted from the geometry optimizations. The role of Fe vacancies is investigated by comparing the formation energies of stoichiometric and Fe-deficient structures, yielding a relative vacancy formation energy. All simulations are carried out with open-source codes, using the body-centered tetragonal structure for KxFe2Se2.

## Reproduction target
Produce the following quantities, all obtained from DFT calculations with open-source tools:

1. Formation energy decomposition: For K contents x = 0.25, 0.5, 0.6, compute and report the total formation energy ΔE_I and its four components (ΔE_K_ion_layers, ΔE_e_doping, ΔE_FeSe_deformation, ΔE_C) in eV per unit cell.

2. Lattice constants: For x = 0.25 and 0.5, report the optimized lattice parameters a and c (in Å).

3. Phonon density of states: For the optimized structures at x = 0.20 and x = 0.25, compute the phonon DOS and output the frequency (cm⁻¹) and DOS values. These spectra will be examined for the presence or absence of imaginary modes.

4. Fe vacancy formation energy trend: Compute the relative Fe vacancy formation energy at x = 0.8, defined as the difference in formation energies between the stoichiometric KxFe2Se2 and the Fe-deficient KxFe1.94Se2, with the reference value at x = 0.125 set to zero.

Write all results to the output files specified in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Crystal structure descriptions for KxFe2Se2

## Workflow steps

### Step 1: Generate all input structures
- Role: process
- Action: Construct the crystal structures for KxFe2Se2 (x=0.0, 0.2, 0.25, 0.5, 0.6, 0.8, 1.0), KxFe1.94Se2 (x=0.125, 0.8), isolated K ion layers (charge x+), neutral FeSe layers, and charged FeSe layers (charge x-). Use the known body-centered tetragonal lattice and reasonable atomic positions.
- Evidence: `/app/outputs/structure_generation.log`

### Step 2: DFT total energy and structure optimization for main compositions
- Role: process
- Action: Perform DFT geometry optimization and total energy calculations for all KxFe2Se2 and KxFe1.94Se2 structures, and for elemental K. Record the final total energies and the optimized lattice constants a and c for each composition.
- Evidence: `/app/outputs/dft_energies.log`

### Step 3: DFT fragment energies for energy decomposition
- Role: process
- Action: Perform DFT calculations for isolated K ion layers carrying charge x+, for charged FeSe layers carrying charge x-, and for neutral FeSe layers. Store the total energies.
- Evidence: `/app/outputs/fragment_energies.log`

### Step 4: Compute formation energy decomposition
- Role: scored (load-bearing)
- Action: From the total energies obtained in steps 1 and 2, compute the total formation energy ΔE_I and its four components (ΔE_K_ion_layers, ΔE_e_doping, ΔE_FeSe_deformation, ΔE_C) for K contents x=0.25, 0.5, 0.6. Write the results to step_01_formation_energy.csv.
- Output file: `/app/outputs/step_01_formation_energy.csv`
- Format: csv
- Contract: CSV with columns: x, Delta_E_I, Delta_E_K_ion_layers, Delta_E_e_doping, Delta_E_FeSe_deformation, Delta_E_C. Rows for x=0.25, 0.5, 0.6.
- Scoring: scored by hidden verifier

### Step 5: Phonon DOS for K0.2Fe2Se2
- Role: scored
- Action: Compute the phonon density of states for the fully optimized K0.2Fe2Se2 structure using DFT (e.g., DFPT) and Phonopy. Output the frequencies (cm^{-1}) and DOS.
- Output file: `/app/outputs/step_03_phonon_DOS_x020.json`
- Format: json
- Contract: JSON object with keys: 'frequencies_cm-1' (list of floats) and 'dos' (list of floats, same length).
- Scoring: scored by hidden verifier

### Step 6: Phonon DOS for K0.25Fe2Se2
- Role: scored
- Action: Compute the phonon density of states for the fully optimized K0.25Fe2Se2 structure using DFT and Phonopy. Output the frequencies and DOS.
- Output file: `/app/outputs/step_04_phonon_DOS_x025.json`
- Format: json
- Contract: JSON object with keys: 'frequencies_cm-1' (list of floats) and 'dos' (list of floats, same length).
- Scoring: scored by hidden verifier

### Step 7: Extract lattice constants from optimized structures
- Role: scored
- Action: Obtain the optimized lattice constants a and c (in Å) for K0.25Fe2Se2 and K0.5Fe2Se2 from the output of step 1. Write them to step_02_lattice_constants.csv.
- Output file: `/app/outputs/step_02_lattice_constants.csv`
- Format: csv
- Contract: CSV with columns: x, a_Angstrom, c_Angstrom. Rows for x=0.25, 0.5.
- Scoring: scored by hidden verifier

### Step 8: Compute Fe vacancy formation energy trend
- Role: scored
- Action: Using the total energies of KxFe2Se2 and KxFe1.94Se2 from step 1, compute the relative Fe vacancy formation energy ΔE_Fe_vacancy as a difference, with the zero reference set at x=0.125 according to the paper's convention. Output the value for x=0.8 to step_05_Fe_vacancy_energy.csv.
- Output file: `/app/outputs/step_05_Fe_vacancy_energy.csv`
- Format: csv
- Contract: CSV with columns: x, Delta_E_Fe_vacancy. Only row for x=0.8 (value in eV, relative to x=0.125 zero).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energy.csv`
- `/app/outputs/step_02_lattice_constants.csv`
- `/app/outputs/step_03_phonon_DOS_x020.json`
- `/app/outputs/step_04_phonon_DOS_x025.json`
- `/app/outputs/step_05_Fe_vacancy_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energy.csv
- path: `/app/outputs/step_01_formation_energy.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Formation energy decomposition for K intercalation. Rows for K content x=0.25, 0.5, 0.6.
- schema:
  - `type`: table
  - `required_columns`: `x`, `Delta_E_I`, `Delta_E_K_ion_layers`, `Delta_E_e_doping`, `Delta_E_FeSe_deformation`, `Delta_E_C`
  - `units`:
    - `x`: dimensionless
    - `Delta_E_I`: eV per unit cell
    - `Delta_E_K_ion_layers`: eV per unit cell
    - `Delta_E_e_doping`: eV per unit cell
    - `Delta_E_FeSe_deformation`: eV per unit cell
    - `Delta_E_C`: eV per unit cell

### step_02_lattice_constants.csv
- path: `/app/outputs/step_02_lattice_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice parameters a and c for x=0.25 and 0.5.
- schema:
  - `type`: table
  - `required_columns`: `x`, `a_Angstrom`, `c_Angstrom`
  - `units`:
    - `x`: dimensionless
    - `a_Angstrom`: Å
    - `c_Angstrom`: Å

### step_03_phonon_DOS_x020.json
- path: `/app/outputs/step_03_phonon_DOS_x020.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon density of states for K0.2Fe2Se2. Imaginary modes are indicated by negative frequencies.
- schema:
  - `type`: object
  - `required`:
    - `frequencies_cm-1`: list of floats
    - `dos`: list of floats

### step_04_phonon_DOS_x025.json
- path: `/app/outputs/step_04_phonon_DOS_x025.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon density of states for K0.25Fe2Se2. Should contain no negative frequencies.
- schema:
  - `type`: object
  - `required`:
    - `frequencies_cm-1`: list of floats
    - `dos`: list of floats

### step_05_Fe_vacancy_energy.csv
- path: `/app/outputs/step_05_Fe_vacancy_energy.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Relative Fe vacancy formation energy at x=0.8, referenced to zero at x=0.125.
- schema:
  - `type`: table
  - `required_columns`: `x`, `Delta_E_Fe_vacancy`
  - `units`:
    - `x`: dimensionless
    - `Delta_E_Fe_vacancy`: eV (relative)

Notes: All energies are in eV per unit cell formulation. The phonon DOS files must contain frequency (cm^{-1}) and DOS lists of equal length. The checker will verify presence/absence of imaginary modes and compare numerical values against hidden reference tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "Delta_E_I",
          "Delta_E_K_ion_layers",
          "Delta_E_e_doping",
          "Delta_E_FeSe_deformation",
          "Delta_E_C"
        ],
        "units": {
          "x": "dimensionless",
          "Delta_E_I": "eV per unit cell",
          "Delta_E_K_ion_layers": "eV per unit cell",
          "Delta_E_e_doping": "eV per unit cell",
          "Delta_E_FeSe_deformation": "eV per unit cell",
          "Delta_E_C": "eV per unit cell"
        }
      },
      "description": "Formation energy decomposition for K intercalation. Rows for K content x=0.25, 0.5, 0.6."
    },
    {
      "file": "step_02_lattice_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "a_Angstrom",
          "c_Angstrom"
        ],
        "units": {
          "x": "dimensionless",
          "a_Angstrom": "Å",
          "c_Angstrom": "Å"
        }
      },
      "description": "Optimized lattice parameters a and c for x=0.25 and 0.5."
    },
    {
      "file": "step_03_phonon_DOS_x020.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "frequencies_cm-1": "list of floats",
          "dos": "list of floats"
        }
      },
      "description": "Phonon density of states for K0.2Fe2Se2. Imaginary modes are indicated by negative frequencies."
    },
    {
      "file": "step_04_phonon_DOS_x025.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "frequencies_cm-1": "list of floats",
          "dos": "list of floats"
        }
      },
      "description": "Phonon density of states for K0.25Fe2Se2. Should contain no negative frequencies."
    },
    {
      "file": "step_05_Fe_vacancy_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "Delta_E_Fe_vacancy"
        ],
        "units": {
          "x": "dimensionless",
          "Delta_E_Fe_vacancy": "eV (relative)"
        }
      },
      "description": "Relative Fe vacancy formation energy at x=0.8, referenced to zero at x=0.125."
    }
  ],
  "notes": "All energies are in eV per unit cell formulation. The phonon DOS files must contain frequency (cm^{-1}) and DOS lists of equal length. The checker will verify presence/absence of imaginary modes and compare numerical values against hidden reference tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier that examines each output file independently. The verifier compares your reported numerical values (energies and lattice constants) against reference values derived from the original study, using tolerances that account for the use of different DFT implementations and settings. The phonon DOS files are checked for the correct JSON structure and for the presence or absence of negative frequencies (indicating dynamic instability) as expected for each composition. The Fe vacancy formation energy is assessed for its sign and magnitude relative to the reference. Relative trends, such as the increase of certain energy components with K content, are also verified. The final score is a weighted sum of the scores from the individual stages (formation energy, lattice constants, phonon DOS x=0.20, phonon DOS x=0.25, Fe vacancy energy). Reporting the numbers is not sufficient; you must actually perform the DFT and phonon calculations as outlined in the workflow to generate the artifacts that are scored.
