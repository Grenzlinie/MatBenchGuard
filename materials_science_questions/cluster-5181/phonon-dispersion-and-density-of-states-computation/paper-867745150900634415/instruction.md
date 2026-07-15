# Phonon frequencies and pNN convergence for L1₀ AuCu

## Problem background
Ordered metallic alloys can exhibit complex lattice dynamics when subjected to intense laser excitation, where the electron temperature rises to several electron volts, creating a warm dense matter (WDM) regime. Under these conditions, the interatomic forces are modified, potentially leading to phonon hardening or softening depending on crystal structure and interaction range. Understanding the stability of Au-Cu alloy phases in this regime is important for predicting laser-driven structural transformations. This task focuses on computing the phonon dispersion of the L1₀ AuCu phase and analyzing how the lowest-frequency mode at the Brillouin-zone R point is influenced by electron temperature and the range of interatomic interactions.

## Approach
The study uses density-functional perturbation theory (DFPT) to compute phonon frequencies and real-space force constants. The overall idea is:
1. Optimize the geometry of L1₀ AuCu using DFT with the PBE functional.
2. Perform DFPT calculations at two electron temperatures: ground state (Te=0 eV) and the WDM condition (Te=4 eV, using Fermi-Dirac smearing) to obtain the full dynamical matrix at the R point.
3. From the DFPT force constants, construct truncated dynamical matrices that include interactions only up to a given nearest-neighbor shell p (p=1 to 5). By diagonalizing these matrices, we can observe how the lowest phonon frequency ω_I converges toward the full DFPT result as longer-range interactions are included. The comparison between Te=0 and Te=4 reveals the impact of electron temperature on the interaction range.
The agent will use Quantum ESPRESSO (pw.x, ph.x, q2r.x) and the provided pseudopotentials. The computational steps are described in the workflow below.

## Reproduction target
The objective is to produce the following artifacts based on first-principles calculations:
- Optimized lattice parameters a and c for L1₀ AuCu at Te=0 eV.
- Six phonon frequencies at the R point (q=(0, π/a, π/c)) for both Te=0 eV and Te=4 eV, labeled by mode (I through VI) in ascending order of energy.
- A table showing the convergence of the lowest phonon frequency ω_I with interaction range p (p=1..5 and the full DFPT result) at both temperatures.
The physical significance is to establish whether ω_I becomes stable or remains unstable as a function of p, and to quantify the effect of electron temperature on the required interaction range for stability. The results should be reported as per the output contract.

## Assets

- Quantum ESPRESSO (v6.7 or later): https://www.quantum-espresso.org/
- Au PBE ultrasoft pseudopotential (pslibrary 1.0.0): https://www.quantum-espresso.org/pseudopotentials
- Cu PBE ultrasoft pseudopotential (pslibrary 1.0.0): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Geometry optimization of L1₀ AuCu
- Role: scored
- Action: Perform a variable-cell DFT relaxation of L1₀ AuCu (2 atom basis) using the PBE exchange-correlation functional. Optimize lattice parameters a and c, then write the optimized values.
- Output file: `/app/outputs/optimized_lattice_params.json`
- Format: json
- Contract: JSON object: { "a": <float>, "c": <float>, "Te": <float> } with units Å and eV.
- Scoring: scored by hidden verifier

### Step 2: DFPT phonon calculation (Te=0 eV) and force constant extraction
- Role: process
- Action: Using the optimized structure from step_01, perform a ground-state self-consistent field calculation followed by a phonon calculation on a q-grid that includes the R point (q=(0, π/a, π/c)). Then convert the dynamical matrices to real-space force constants.
- Evidence: `/app/outputs/force_constants_Te0.dat`

### Step 3: Phonon frequencies at R point (Te=0 eV)
- Role: scored
- Action: From the dynamical matrix at q=(0, π/a, π/c) obtained in step_02, diagonalize the 6×6 matrix to obtain the squared phonon frequencies, convert to meV, and report the six phonon energies in ascending order.
- Output file: `/app/outputs/phonon_frequencies_Rpoint_Te0.csv`
- Format: csv
- Contract: CSV with columns: mode (str), omega_meV (float). Modes labelled I, II, III, IV, V, VI.
- Scoring: scored by hidden verifier

### Step 4: DFPT phonon calculation (Te=4 eV) and force constant extraction
- Role: process
- Action: Using the optimized structure from step_01, repeat the DFT+DFPT calculation with electron temperature Te=4 eV (Fermi-Dirac smearing) to obtain real-space force constants.
- Evidence: `/app/outputs/force_constants_Te4.dat`

### Step 5: Phonon frequencies at R point (Te=4 eV)
- Role: scored
- Action: From the dynamical matrix at q=(0, π/a, π/c) obtained in step_04, diagonalize to get the six phonon energies at Te=4 eV.
- Output file: `/app/outputs/phonon_frequencies_Rpoint_Te4.csv`
- Format: csv
- Contract: CSV with columns: mode (str), omega_meV (float). Modes labelled I, II, III, IV, V, VI.
- Scoring: scored by hidden verifier

### Step 6: pNN convergence analysis of ω_I
- Role: scored (load-bearing)
- Action: Using the real-space force constants from steps 02 and 04, construct the dynamical matrix at point R truncated to each p-th nearest-neighbour shell (p=1..5) as defined in the paper's approach. Diagonalize each 6×6 matrix and record the lowest squared frequency ω_I². Convert to meV and include the full DFPT ω_I from steps 03 and 05 as reference (pNN=0). Output a table.
- Output file: `/app/outputs/pNN_convergence_table.csv`
- Format: csv
- Contract: CSV with columns: pNN (int, 0 for full DFPT, 1..5), Te0_omega_I_meV (float), Te4_omega_I_meV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_lattice_params.json`
- `/app/outputs/phonon_frequencies_Rpoint_Te0.csv`
- `/app/outputs/phonon_frequencies_Rpoint_Te4.csv`
- `/app/outputs/pNN_convergence_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_lattice_params.json
- path: `/app/outputs/optimized_lattice_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice parameters of L1₀ AuCu at Te=0 eV.
- schema:
  - `type`: object
  - `required`: `a`, `c`, `Te`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `Te`: eV

### phonon_frequencies_Rpoint_Te0.csv
- path: `/app/outputs/phonon_frequencies_Rpoint_Te0.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Six phonon frequencies at point R for Te=0 eV.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `omega_meV`
  - `units`:
    - `omega_meV`: meV

### phonon_frequencies_Rpoint_Te4.csv
- path: `/app/outputs/phonon_frequencies_Rpoint_Te4.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Six phonon frequencies at point R for Te=4 eV.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `omega_meV`
  - `units`:
    - `omega_meV`: meV

### pNN_convergence_table.csv
- path: `/app/outputs/pNN_convergence_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lowest phonon frequency ω_I for p=1..5 and full DFPT (pNN=0) at both Te=0 and Te=4 eV.
- schema:
  - `type`: table
  - `required_columns`: `pNN`, `Te0_omega_I_meV`, `Te4_omega_I_meV`
  - `units`:
    - `Te0_omega_I_meV`: meV
    - `Te4_omega_I_meV`: meV

Notes: Checker compares reported values to hidden gold with tolerances (±0.02 Å for lattice constants, ±2 meV for phonon energies, and verifies pNN convergence trend).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_lattice_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "c",
          "Te"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "Te": "eV"
        }
      },
      "description": "Optimized lattice parameters of L1₀ AuCu at Te=0 eV."
    },
    {
      "file": "phonon_frequencies_Rpoint_Te0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "omega_meV"
        ],
        "units": {
          "omega_meV": "meV"
        }
      },
      "description": "Six phonon frequencies at point R for Te=0 eV."
    },
    {
      "file": "phonon_frequencies_Rpoint_Te4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "omega_meV"
        ],
        "units": {
          "omega_meV": "meV"
        }
      },
      "description": "Six phonon frequencies at point R for Te=4 eV."
    },
    {
      "file": "pNN_convergence_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pNN",
          "Te0_omega_I_meV",
          "Te4_omega_I_meV"
        ],
        "units": {
          "Te0_omega_I_meV": "meV",
          "Te4_omega_I_meV": "meV"
        }
      },
      "description": "Lowest phonon frequency ω_I for p=1..5 and full DFPT (pNN=0) at both Te=0 and Te=4 eV."
    }
  ],
  "notes": "Checker compares reported values to hidden gold with tolerances (±0.02 Å for lattice constants, ±2 meV for phonon energies, and verifies pNN convergence trend)."
}
```

## How you are scored
After you submit the output files, an automated verifier will inspect them. Each scored artifact (lattice parameters, phonon frequencies at Te=0, phonon frequencies at Te=4, and the pNN convergence table) is checked independently against reference criteria. For numerical values, the verifier allows reasonable tolerances that account for typical variations from different computational setups (e.g., pseudopotential choice, k‑point sampling). For the pNN analysis, the verifier also assesses whether the convergence trend (how ω_I changes with p and temperature) is physically plausible and consistent with the expected short‑range vs. long‑range force picture. The partial scores from each artifact are combined to yield a final reward between 0 and 1. Simply reporting a number without having performed the underlying DFPT runs is unlikely to produce the correct trend in the pNN table, so the verifier's checks emphasize internal consistency and expected physical behavior.
