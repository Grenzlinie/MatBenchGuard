# Point defect formation and binding energy calculation: material-specific HSE mixing parameters and vacancy formation enthalpies for Cu, Ag, Au

## Problem background
Standard semilocal density functional theory (DFT) approximations (e.g., PBE) have difficulty accurately predicting vacancy formation enthalpies in the filled d-band noble metals Ag and Au, while Cu is reasonably described. Recent reanalysis of experimental high-temperature vacancy concentration data using a non-Arrhenius local Grüneisen extrapolation has revised the T=0 K vacancy formation enthalpies, revealing that for Ag the discrepancy with PBE remains large, unlike for Cu. Hybrid functionals that include a fraction of exact Hartree-Fock exchange (the HSE functional) can alter the electronic structure and may improve the prediction. The exact-exchange mixing parameter α is material-specific and can be determined by aligning the computed valence-band density of states (DOS) with experimental photoemission spectra. The task is to compute the HSE mixing parameters α and the resulting T=0 K vacancy formation enthalpies for Cu, Ag, and Au, using α values optimized via DOS matching.

## Approach
The computational approach consists of several stages. First, for each metal, build a 64-atom fcc supercell and perform self-consistent HSE calculations for a series of α values (covering a range that includes the semilocal limit). From each calculation, extract the electronic density of states (DOS). Identify the energy positions of the main d-band peaks relative to the Fermi level in the computed DOS and compare them to the d-band peak positions observed in published experimental ultraviolet photoemission spectra. For each metal, select the α that yields the best alignment of the computed and experimental d-band peaks. Then, using the optimal α, fully relax the perfect supercell (lattice constant and atomic positions) to obtain the equilibrium total energy. Create a vacancy by removing one atom from the relaxed cell, relax the atomic positions of the defective supercell at constant volume, and compute its total energy. The vacancy formation enthalpy is obtained as H_vac = E(vacancy) − (63/64)·E(perfect). The derived α and H_vac values are then compared against independently determined reference data (experimentally revised formation enthalpies).

## Reproduction target
Compute the optimal HSE mixing parameter α and the vacancy formation enthalpy H_vac (in eV) for Cu, Ag, and Au. The α for each metal is determined by matching the computed DOS d-band peak positions to those in published experimental valence-band photoemission spectra (Au: Duo et al., J. Phys.: Condens. Matter 3, 989 (1991); Ag: Riley et al., J. Phys. F 6, 293 (1976); Cu: multiple references – see assets). Report the results in a single JSON file with keys 'Cu', 'Ag', 'Au', each containing the fields 'optimized_alpha' and 'H_vac_eV'. The computational workflow (DOS series, α selection, and vacancy energy calculations) must be executed; the intermediate evidence files (dos_curves.tar.gz, alpha_selection.log, vacancy_calculations.log) are required to document the pipeline.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP Pseudopotentials (PBE): https://www.quantum-espresso.org/pseudopotentials/sssp
- Valence-band photoemission spectrum of Au (Duo et al. 1991): 10.1088/0953-8984/3/7/003
- Valence-band photoemission spectrum of Ag (Riley et al. 1976): 10.1088/0305-4608/6/2/016
- Valence-band photoemission spectrum of Cu (Riley et al. 1976; Janak et al. 1975; Dose and Reusing 1982): 10.1088/0305-4608/6/2/016

## Workflow steps

### Step 1: Compute HSE DOS series for Cu, Ag, Au
- Role: process
- Action: For Cu, Ag, and Au, build 64-atom fcc supercells using the experimental lattice constants and perform self-consistent HSE calculations for a series of exact-exchange mixing parameters α (e.g., 0.0, 0.1, 0.2, 0.3, 0.4, 0.6) to obtain the density of states (DOS) curves. Use an appropriate plane-wave cutoff and k-point mesh.
- Evidence: `/app/outputs/dos_curves.tar.gz`

### Step 2: Determine optimal α by matching experimental spectra
- Role: process
- Action: For each metal, identify the main d-band peak positions in the computed DOS series and compare them to the positions in the corresponding published experimental valence-band photoemission spectra. Select the α that gives the best alignment of the d-band peaks relative to the Fermi level.
- Evidence: `/app/outputs/alpha_selection.log`

### Step 3: Compute vacancy formation enthalpies with optimal α
- Role: process
- Action: Using the optimal α for each metal, fully relax the perfect 64-atom supercell (ionic positions and lattice constants) to obtain the equilibrium total energy. Create a vacancy by removing one atom, relax the ionic positions, and compute the total energy of the defective supercell. Compute the vacancy formation enthalpy as H_vac = E(vacancy) − (63/64)·E(perfect).
- Evidence: `/app/outputs/vacancy_calculations.log`

### Step 4: Report optimized α and H_vac for Cu, Ag, Au
- Role: scored
- Action: Compile the optimized α and vacancy formation enthalpies (in eV) for Cu, Ag, and Au into a single JSON file, using the keys 'Cu', 'Ag', 'Au'. Each metal entry contains the fields 'optimized_alpha' and 'H_vac_eV'.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys 'Cu', 'Ag', 'Au'; each value is an object with numeric fields 'optimized_alpha' (float) and 'H_vac_eV' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized HSE mixing parameters α and computed T=0 K vacancy formation enthalpies for Cu, Ag, and Au. Checked against paper-reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `Cu`, `Ag`, `Au`
  - `properties`:
    - `Cu`:
      - `type`: object
      - `required`: `optimized_alpha`, `H_vac_eV`
      - `properties`:
        - `optimized_alpha`:
          - `type`: number
        - `H_vac_eV`:
          - `type`: number
          - `unit`: eV
    - `Ag`:
      - `type`: object
      - `required`: `optimized_alpha`, `H_vac_eV`
      - `properties`:
        - `optimized_alpha`:
          - `type`: number
        - `H_vac_eV`:
          - `type`: number
          - `unit`: eV
    - `Au`:
      - `type`: object
      - `required`: `optimized_alpha`, `H_vac_eV`
      - `properties`:
        - `optimized_alpha`:
          - `type`: number
        - `H_vac_eV`:
          - `type`: number
          - `unit`: eV

Notes: The reported values must be obtained by following the full computational pipeline; fabricating numbers does not guarantee a match to the hidden gold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Cu",
          "Ag",
          "Au"
        ],
        "properties": {
          "Cu": {
            "type": "object",
            "required": [
              "optimized_alpha",
              "H_vac_eV"
            ],
            "properties": {
              "optimized_alpha": {
                "type": "number"
              },
              "H_vac_eV": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "Ag": {
            "type": "object",
            "required": [
              "optimized_alpha",
              "H_vac_eV"
            ],
            "properties": {
              "optimized_alpha": {
                "type": "number"
              },
              "H_vac_eV": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "Au": {
            "type": "object",
            "required": [
              "optimized_alpha",
              "H_vac_eV"
            ],
            "properties": {
              "optimized_alpha": {
                "type": "number"
              },
              "H_vac_eV": {
                "type": "number",
                "unit": "eV"
              }
            }
          }
        }
      },
      "description": "Optimized HSE mixing parameters α and computed T=0 K vacancy formation enthalpies for Cu, Ag, and Au. Checked against paper-reported values with appropriate tolerances."
    }
  ],
  "notes": "The reported values must be obtained by following the full computational pipeline; fabricating numbers does not guarantee a match to the hidden gold."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares the contents of `/app/outputs/results.json` to a hidden set of reference values. These reference values are the optimal mixing parameters α and vacancy formation enthalpies for Cu, Ag, and Au as derived from the experimental photoemission spectra and the corresponding experimentally revised formation enthalpies. The verifier computes the deviation of your reported optimized_alpha and H_vac_eV from the hidden targets, applying appropriate tolerances. Full credit (reward 1.0) requires that all six quantities (α and H_vac for all three metals) are within tolerance; partial credit is awarded proportionally based on the number of metals meeting the tolerance. Intermediate evidence files (dos_curves.tar.gz, alpha_selection.log, vacancy_calculations.log) must be present to demonstrate that the full computational pipeline was executed, but they are not directly scored.
