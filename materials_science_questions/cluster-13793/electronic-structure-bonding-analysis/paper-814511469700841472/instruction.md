# Reproducing the pressure–composition phase diagram and structural transitions of Li-Si binary compounds

## Problem background
Lithium-silicon binary compounds under high pressure are of interest for discovering new silicon-rich phases that may serve as precursors for novel silicon allotropes with desirable electronic properties. A computational study has predicted a series of lithium silicides stabilized under pressure, including Si-rich compositions that exhibit covalent silicon frameworks. Evaluating their thermodynamic stability via formation enthalpy convex hulls, verifying dynamical stability through phonon dispersions, and pinpointing pressure-induced structural phase boundaries are essential to assess their viability and recovery potential.

## Approach
First-principles density functional theory (DFT) calculations are used to compute the total energies of elemental lithium and silicon reference phases and of candidate Li-Si compound structures across a range of pressures. From these, the formation enthalpies are derived and the convex hull is constructed at each pressure to identify the thermodynamically stable stoichiometries. For the candidate LiSi₄ compound in the Cmmm structure, the phonon dispersion is computed at ambient pressure using the finite-displacement method to assess dynamical stability (presence or absence of imaginary phonon modes). Additionally, the total enthalpies of the Cmmm phase and the competing I4/m phase are compared as a function of pressure to locate the pressure at which the structural phase transition occurs. The calculations employ the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional, with all simulations performed using open-source tools (Quantum ESPRESSO for DFT and Phonopy for phonons).

## Reproduction target
Produce the following three scored artifacts:

- `/app/outputs/formation_enthalpies.csv`: a CSV table containing the formation enthalpy (in eV/atom) for every considered Li-Si compound at each required pressure (25, 50, 100 GPa), along with composition and space group identifiers.
- `/app/outputs/LiSi4_phonon_dispersion.txt`: a text file containing the phonon dispersion of LiSi₄ (Cmmm) at ambient pressure, with a header line `# MIN_FREQ <value> IMAGINARY_yes/no` that reports the minimum phonon frequency and whether any imaginary (negative) modes exist.
- `/app/outputs/LiSi4_transition_pressure.txt`: a plain text file containing a single positive floating-point number that is the estimated Cmmm → I4/m structural transition pressure (in GPa) for LiSi₄.

## Assets

- Crystal structure parameters of Li–Si compounds (Table S1 from Supporting Information): https://pubs.acs.org/doi/suppl/10.1021/acsami.6b04308
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials for Li and Si: https://www.quantum-espresso.org/pseudopotentials
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Download the Supporting Information PDF from the ACS URL and extract the crystal structure parameters (space groups, atomic positions, lattice parameters) from Table S1 for all stable Li-Si compounds (LiSi4, LiSi3, LiSi2, Li2Si3, LiSi, Li2Si, Li3Si, Li4Si) and for elemental Li (Fm-3m, I-43d, Cmca-24) and Si (P6/mmm, P63/mmc, Fm-3m) reference phases. Convert the structures into input files for Quantum ESPRESSO at the required pressures.
- Evidence: none

### Step 2: Reference total energies of elemental Li and Si
- Role: process
- Action: Using Quantum ESPRESSO with PBE pseudopotentials, perform DFT calculations for each elemental phase (Li: Fm-3m, I-43d, Cmca-24; Si: P6/mmm, P63/mmc, Fm-3m) at pressures 0, 25, 50, and 100 GPa. For each phase at each pressure, relax the structure and record the total energy per atom. These energies are needed to compute formation enthalpies later.
- Evidence: none

### Step 3: Total energies of Li-Si compounds
- Role: process
- Action: For every Li-Si compound from step_01, perform DFT geometry relaxation with Quantum ESPRESSO at the pressures needed for enthalpy construction (at least 25, 50, 100 GPa, and additionally a series of pressures for the LiSi4 transition pressure determination). Record the final total energy for each relaxed structure.
- Evidence: none

### Step 4: Formation enthalpies and convex hull
- Role: scored (load-bearing)
- Action: From the energies obtained in steps 2 and 3, compute the formation enthalpy per atom: ΔH_f = [H(Li_xSi_y) - x·H(Li) - y·H(Si)] / (x+y), using the elemental phase with the lowest total energy at each pressure. Assemble a CSV file containing composition, pressure (GPa), space group, and formation enthalpy (in eV/atom) for every Li-Si compound that was relaxed. Write to formation_enthalpies.csv.
- Output file: `/app/outputs/formation_enthalpies.csv`
- Format: csv
- Contract: CSV with header: composition,pressure,space_group,formation_enthalpy. composition is a string like 'LiSi4'; pressure is numeric (GPa); space_group is string; formation_enthalpy is numeric in eV/atom.
- Scoring: scored by hidden verifier

### Step 5: Phonon dispersion of LiSi4 (Cmmm) at ambient pressure
- Role: scored
- Action: Relax the Cmmm LiSi4 structure from step_01 at 0 GPa using Quantum ESPRESSO. Then obtain the phonon dispersion via finite-displacement calculations with Phonopy. Write the phonon frequencies along the high-symmetry path to LiSi4_phonon_dispersion.txt, and include a line '# MIN_FREQ <value> IMAGINARY_yes/no' that reports the minimum frequency and whether any imaginary modes exist.
- Output file: `/app/outputs/LiSi4_phonon_dispersion.txt`
- Format: txt
- Contract: Text file containing phonon frequencies along k-point path. Must contain at least one line starting with '# MIN_FREQ' followed by a floating-point frequency in THz and the string 'IMAGINARY_yes' or 'IMAGINARY_no'.
- Scoring: scored by hidden verifier

### Step 6: Cmmm → I4/m transition pressure of LiSi4
- Role: scored
- Action: Calculate the total enthalpy (H = E + PV) of LiSi4 in the Cmmm and I4/m structures at a series of pressures spanning 0–50 GPa using Quantum ESPRESSO. Determine the pressure at which the enthalpy curves intersect (the transition pressure). Write that single pressure value in GPa (as a floating point) to LiSi4_transition_pressure.txt.
- Output file: `/app/outputs/LiSi4_transition_pressure.txt`
- Format: txt
- Contract: A plain text file containing a single positive floating-point number representing the transition pressure in GPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_enthalpies.csv`
- `/app/outputs/LiSi4_phonon_dispersion.txt`
- `/app/outputs/LiSi4_transition_pressure.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_enthalpies.csv
- path: `/app/outputs/formation_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Formation enthalpies of Li-Si compounds used to recompute the convex hull and identify stable stoichiometries.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `pressure`, `space_group`, `formation_enthalpy`
  - `units`:
    - `pressure`: GPa
    - `formation_enthalpy`: eV/atom

### LiSi4_phonon_dispersion.txt
- path: `/app/outputs/LiSi4_phonon_dispersion.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion data and a header line reporting minimum frequency and presence/absence of imaginary modes.
- schema:
  - `type`: text

### LiSi4_transition_pressure.txt
- path: `/app/outputs/LiSi4_transition_pressure.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Single transition pressure value (in GPa) for the Cmmm→I4/m phase transition of LiSi4.
- schema:
  - `type`: text

Notes: No additional public notes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "pressure",
          "space_group",
          "formation_enthalpy"
        ],
        "units": {
          "pressure": "GPa",
          "formation_enthalpy": "eV/atom"
        }
      },
      "description": "Formation enthalpies of Li-Si compounds used to recompute the convex hull and identify stable stoichiometries."
    },
    {
      "file": "LiSi4_phonon_dispersion.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Phonon dispersion data and a header line reporting minimum frequency and presence/absence of imaginary modes."
    },
    {
      "file": "LiSi4_transition_pressure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Single transition pressure value (in GPa) for the Cmmm→I4/m phase transition of LiSi4."
    }
  ],
  "notes": "No additional public notes."
}
```

## How you are scored
A hidden verifier independently scores each submitted artifact and combines them by weight into a final reward between 0 and 1.
- For `formation_enthalpies.csv`, the verifier recomputes the convex hull from the submitted formation enthalpies and checks whether the set of compositions on the hull at the designated pressures matches the expected stable stoichiometries, allowing for a small energy tolerance.
- For `LiSi4_phonon_dispersion.txt`, the verifier parses the `# MIN_FREQ` line and confirms that the minimum frequency is above a defined threshold and that the `IMAGINARY` flag is `no`.
- For `LiSi4_transition_pressure.txt`, the verifier compares the submitted value to a hidden reference within an acceptable pressure window.
Only a correctly executed computational workflow will produce artifacts that pass the verification; reporting the paper’s numbers without performing the calculations is insufficient to earn credit.
