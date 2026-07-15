# Point defect formation and binding energies in dilute tungsten alloys via DFT

## Problem background
Tungsten alloys are candidate materials for plasma-facing components in fusion reactors. During operation, neutron exposure can transmute pure tungsten into alloys, and ion irradiation produces self‑interstitial atoms (SIAs) and other point defects. The interaction between SIAs and alloying elements (solutes) can affect defect mobility and radiation damage evolution. Quantifying the formation energies of substitutional and interstitial defects, as well as the binding energies between SIAs and solute atoms, is therefore essential for modelling the behaviour of tungsten‑based alloys under fusion‑relevant conditions.

## Approach
First‑principles density functional theory (DFT) calculations using the PBE exchange‑correlation functional and projector augmented wave (PAW) pseudopotentials are used to compute total energies of bcc tungsten supercells containing point defects. The supercell method is employed, with multiple cell sizes (e.g., 54, 128, and 250 atoms) to extrapolate raw formation energies to the infinite‑size (dilute) limit via finite‑size scaling. A correction for the influence of tungsten 5p semicore states is obtained from selected calculations and added to the extrapolated energies. For each solute (Ti, V, Zr, Nb, Hf, Ta, Re) and for the self‑interstitial, the following defect configurations are considered: a substitutional defect (solute replacing a W atom) and mixed‑interstitial configurations in bridge, ⟨111⟩ dumbbell, and ⟨110⟩ dumbbell geometries. Formation energies are computed as the difference between the total energy of the defective supercell and that of the perfect reference cell, adjusted by chemical potentials. Binding energies between a self‑interstitial and a solute atom are then calculated from the final formation energies as the energy of the most stable mixed‑interstitial minus the sum of the most stable self‑interstitial and the substitutional formation energy. All calculations can be carried out with an open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO or GPAW) using publicly available pseudopotentials. The computed results are organized in two CSV files for scoring.

## Reproduction target
The objective is to compute, using open‑source DFT, the formation energies of substitutional (sub) and interstitial (bridge, ⟨111⟩ dumbbell, ⟨110⟩ dumbbell) point defects in tungsten for seven solute elements (Ti, V, Zr, Nb, Hf, Ta, Re) and for the self‑interstitial (W). Additionally, compute the binding energy between a self‑interstitial atom and each solute atom using the most stable mixed‑interstitial configuration. Results are to be produced as two CSV files:

- `formation_energies.csv`: columns `element` (str), `defect_type` (one of `sub`, `bridge`, `111`, `110`), `formation_energy_eV` (float, in eV).
- `binding_energies.csv`: columns `element` (str), `binding_energy_eV` (float, in eV; negative values indicate attraction).

The primary focus is on the solutes Ti, V, and Re: for these elements, determine whether the bridge interstitial is the most stable configuration (i.e., has the lowest formation energy among the three interstitial geometries) and whether their binding energies are attractive (negative). The other solutes provide a secondary check; however, the scoring concentrates on Ti, V, and Re.

## Assets

- Quantum ESPRESSO (open-source DFT code) or equivalent: https://www.quantum-espresso.org/download
- PBE PAW pseudopotentials for W, Ti, V, Zr, Nb, Hf, Ta, Re: https://www.quantum-espresso.org/pseudopotentials
- Atomic Simulation Environment (ASE): ase
- Pymatgen: pymatgen
- numpy, pandas: numpy pandas

## Workflow steps

### Step 1: DFT structure relaxation and total energy calculations
- Role: process
- Action: Construct bcc tungsten supercells for perfect and defect configurations (substitutional and interstitial: bridge, ⟨111⟩ dumbbell, ⟨110⟩ dumbbell) for solutes Ti, V, Zr, Nb, Hf, Ta, Re and the self-interstitial, using multiple supercell sizes. Run DFT geometry relaxations with PBE-GGA, PAW pseudopotentials, and an open-source code (e.g. Quantum ESPRESSO or GPAW), saving relaxed total energies and lattice vectors.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 2: Finite-size scaling and semicore correction
- Role: process
- Action: Compute raw formation energies from the DFT total energies using the formation energy formula with chemical potentials from cohesive energies. Extrapolate to the infinite-size limit by fitting formation energies versus inverse system size. Determine the semicore correction shift by comparing calculations with and without W 5p semicore states on selected configurations, and add this shift to the extrapolated energies to yield final formation energies for all substitutional and interstitial defects.
- Evidence: `/app/outputs/scaling_analysis.log`

### Step 3: Write final formation energies CSV
- Role: scored (load-bearing)
- Action: Compile the final corrected formation energies for all substitutional and interstitial defects (bridge, ⟨111⟩, ⟨110⟩) for solutes Ti, V, Zr, Nb, Hf, Ta, Re and for the self-interstitial W into a CSV file. Each row corresponds to one defect, with columns: element (str), defect_type (str), formation_energy_eV (float).
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: element (str), defect_type (str, one of: sub, bridge, 111, 110), formation_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 4: Compute and write binding energies CSV
- Role: scored
- Action: Using the final formation energies, compute the binding energy between a self-interstitial atom and a solute atom for each solute as E_b = E_f([X-W]_lowest) - E_f([W-W]_lowest) - E_f(X_sub), where 'lowest' denotes the most stable interstitial configuration. Output the results to a CSV file with columns: element (str) and binding_energy_eV (float, negative indicates attraction).
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: CSV with columns: element (str), binding_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Final corrected formation energies for all substitutional and interstitial defects. Checker compares values within tolerance and verifies ordering for Ti, V, Re.
- schema:
  - `type`: table
  - `required_columns`: `element`, `defect_type`, `formation_energy_eV`
  - `description`: element: W, Ti, V, Zr, Nb, Hf, Ta, Re; defect_type: sub, bridge, 111, 110; formation_energy_eV: float in eV.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Binding energies between self-interstitial atoms and substitutional solutes. Checker verifies that binding is negative for Ti, V, Re.
- schema:
  - `type`: table
  - `required_columns`: `element`, `binding_energy_eV`
  - `description`: element: Ti, V, Zr, Nb, Hf, Ta, Re; binding_energy_eV: float, negative indicates attraction.

Notes: Formation volumes and anisotropy analysis are excluded as they are not in the scored scope.

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
          "element",
          "defect_type",
          "formation_energy_eV"
        ],
        "description": "element: W, Ti, V, Zr, Nb, Hf, Ta, Re; defect_type: sub, bridge, 111, 110; formation_energy_eV: float in eV."
      },
      "description": "Final corrected formation energies for all substitutional and interstitial defects. Checker compares values within tolerance and verifies ordering for Ti, V, Re."
    },
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "binding_energy_eV"
        ],
        "description": "element: Ti, V, Zr, Nb, Hf, Ta, Re; binding_energy_eV: float, negative indicates attraction."
      },
      "description": "Binding energies between self-interstitial atoms and substitutional solutes. Checker verifies that binding is negative for Ti, V, Re."
    }
  ],
  "notes": "Formation volumes and anisotropy analysis are excluded as they are not in the scored scope."
}
```

## How you are scored
Your work is evaluated by a hidden verifier that reads only the two CSV files you write to `/app/outputs`. The verifier compares your computed formation energies and binding energies to independently determined reference values with appropriate tolerances, and checks structural relationships:

- **Formation energy accuracy**: each submitted formation energy is compared to a hidden reference; values within a prescribed tolerance receive credit.
- **Interstitial ordering for Ti, V, Re**: the verifier checks that the `bridge` formation energy is lower than both `111` and `110` energies for each of these three elements.
- **Binding sign for Ti, V, Re**: the verifier checks that the binding energy for Ti, V, and Re is negative (attractive).

The final reward is a weighted combination of these checks. Missing rows or unparseable values result in zero credit for the affected element. To earn full credit, your computed formation energies must satisfy the numerical and structural criteria simultaneously.
