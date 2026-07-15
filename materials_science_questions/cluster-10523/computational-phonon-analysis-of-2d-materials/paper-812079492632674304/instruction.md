# DFT Calculation of Phonon Frequencies and Projected Density of States for a Layered Transition-Metal Dichalcogenide

## Problem background
Layered transition-metal dichalcogenide 1T'-TaTe2 exhibits a structural phase transition upon cooling: from a room-temperature (3×1) stripe-like order to a low-temperature (3×3) superstructure of Ta trimer clusters. Ultrafast optical excitation can melt this trimer superstructure on a picosecond timescale. Density-functional theory (DFT) calculations are essential to identify the electronic states and phonon modes involved in the photo-induced transformation. The projected density of states reveals the intra-trimer charge transfer character in the Ta d and Te p orbitals, while a particular phonon mode is proposed to couple to the structural dynamics.

## Approach
Use density-functional theory (DFT) with a standard exchange-correlation functional (e.g., PBE) and plane-wave/pseudopotential implementation. First, obtain the low-temperature crystal structure (space group C2/m) and fully relax the atomic positions and lattice parameters via geometry optimization. From the relaxed structure, compute the phonon frequencies at the Gamma point via density-functional perturbation theory (DFPT). Separately, compute the self-consistent electronic ground state and project the density of states onto Ta d orbitals and Te p orbitals to assess the orbital character of the valence and conduction bands.

## Reproduction target
Starting from the low-temperature (3×3) superstructure of 1T'-TaTe2, relax the geometry with DFT, then compute all Gamma-point phonon frequencies (in THz) and report them in step_01_phonon_frequencies.csv. Additionally, compute the projected density of states (PDOS) onto Ta d and Te p orbitals as a function of energy relative to the Fermi level, and write it to step_02_projected_dos.csv. The PDOS should faithfully represent the orbital-resolved electronic structure across an energy range that covers the bonding and non-bonding features.

## Assets

- Crystal structure of low-temperature 1T'-TaTe2 (C2/m)
- Quantum ESPRESSO (or compatible DFT code): https://www.quantum-espresso.org
- PBE pseudopotentials for Ta and Te: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: Obtain the publicly available low-temperature crystal structure of 1T'-TaTe2 (space group C2/m) and perform a density functional theory geometry optimization using a standard exchange-correlation functional (e.g., PBE) to obtain relaxed atomic positions and lattice parameters.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Phonon frequency calculation
- Role: scored (load-bearing)
- Action: Using the relaxed structure, perform density functional perturbation theory (DFPT) phonon calculation at the Gamma point. Extract all Gamma-point phonon frequencies (in THz) and write to step_01_phonon_frequencies.csv.
- Output file: `/app/outputs/step_01_phonon_frequencies.csv`
- Format: csv
- Contract: Two columns: mode_index (integer), frequency_THz (float).
- Scoring: scored by hidden verifier

### Step 3: Projected density of states
- Role: scored
- Action: Using the relaxed structure, perform a self-consistent field calculation and compute the projected density of states (PDOS) onto Ta d and Te p orbitals. Write the PDOS as a function of energy (eV) relative to the Fermi level to step_02_projected_dos.csv.
- Output file: `/app/outputs/step_02_projected_dos.csv`
- Format: csv
- Contract: Three columns: energy_eV (float), pdos_Ta_d (float), pdos_Te_p (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_frequencies.csv`
- `/app/outputs/step_02_projected_dos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_frequencies.csv
- path: `/app/outputs/step_01_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Gamma-point phonon frequencies computed by DFPT. The mode closest to 2.7 THz is scored by exact match within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `mode_index`, `frequency_THz`
  - `units`:
    - `frequency_THz`: THz

### step_02_projected_dos.csv
- path: `/app/outputs/step_02_projected_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Projected density of states onto Ta d and Te p orbitals. The shape is audited: Ta d states should dominate above -2 eV and Te p states below -4 eV.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `pdos_Ta_d`, `pdos_Te_p`
  - `units`:
    - `energy_eV`: eV

Notes: The relaxation log (relaxation_log.txt) produced by the process step is not scored but documents that the required geometry relaxation was executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_index",
          "frequency_THz"
        ],
        "units": {
          "frequency_THz": "THz"
        }
      },
      "description": "Gamma-point phonon frequencies computed by DFPT. The mode closest to 2.7 THz is scored by exact match within a tolerance."
    },
    {
      "file": "step_02_projected_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "pdos_Ta_d",
          "pdos_Te_p"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Projected density of states onto Ta d and Te p orbitals. The shape is audited: Ta d states should dominate above -2 eV and Te p states below -4 eV."
    }
  ],
  "notes": "The relaxation log (relaxation_log.txt) produced by the process step is not scored but documents that the required geometry relaxation was executed."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact. For step_01_phonon_frequencies.csv, the verifier identifies the phonon mode of interest (the one closest to the experimentally relevant frequency) and compares its computed frequency to a hidden reference value; full credit is awarded when the deviation is within a tolerance, and partial credit decays for larger deviations. For step_02_projected_dos.csv, the verifier performs a structural audit: it checks that the Ta d contribution dominates the upper valence region near the Fermi level while the Te p contribution dominates the deeper valence region. The relaxation evidence (relaxation_log.txt) is not directly scored but is required as a prerequisite for the subsequent steps. The final reward is a weighted combination of the two scored outputs, with the phonon frequency carrying the primary weight.
