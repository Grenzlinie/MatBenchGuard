# DFT calculation of ground and excited singlet states in CaWO4

## Problem background
Calcium tungstate (CaWO4) is a scheelite-type phosphor that exhibits broad photoluminescence (PL) centered in the blue or green region, depending on synthesis conditions. The PL mechanism is believed to be related to structural distortions of the constituent WO4 tetrahedra and CaO8 polyhedra, and to the presence of stable electronic excited states. Understanding the relationship between local structural distortions, excited electronic states, and PL emission is important for designing optical materials. This work uses first-principles density functional theory (DFT) calculations to characterize the geometry and electronic structure of the ground singlet state (s) and a putative excited singlet state (s*) of crystalline CaWO4, and to investigate whether such an excited state can be a local minimum on the potential energy surface.

## Approach
The computational approach employs periodic DFT with the B3LYP hybrid functional. The CaWO4 scheelite crystal structure (space group I41/a) is taken as the starting point. For the ground singlet state, full geometry optimization (atomic positions and lattice parameters) is performed, followed by a single-point calculation to extract the direct Kohn–Sham band gap. An excited singlet state (s*) is constructed by modifying the electronic occupation: an electron is promoted from the highest occupied Kohn–Sham state to the lowest unoccupied one, and the geometry is then fully relaxed under that constrained occupation. Finally, Gamma-point vibrational frequencies are computed at the optimized excited-state geometry to verify that s* is a true local minimum (no imaginary modes). The energy difference ΔE = E(s*) – E(s) is then obtained by comparing the total energies of the two optimized structures.

## Reproduction target
Using an open-source periodic DFT code (e.g., CP2K) with the B3LYP functional and appropriate basis sets/pseudopotentials (Ca: 86‑511d21 or equivalent, W: pseudopotential with double‑zeta valence, O: 6‑31G* with d‑orbital exponent 0.8), you must produce three output files:

- step_01_ground_state_summary.csv: after ground‑state geometry optimization, report the lattice parameters a and c, the W–O bond distance, the O–W–O angles (α and β as defined in the scheelite tetrahedron), the total energy per simulation cell, and the direct Kohn–Sham band gap.
- step_02_excited_state_summary.csv: after excited‑state geometry optimization, report the same set of quantities.
- step_03_energy_comparison.txt: compute ΔE = E(s*) − E(s) and state whether the excited‑state structure is a local minimum (i.e., the optimization yielded no imaginary vibrational frequencies at the Γ‑point).

The results must be reported in the specified CSV format and text format; the exact column layout and required rows are given in the workflow steps below.

## Assets

- CaWO4 scheelite crystal structure (ICSD #18135): ICSD 18135
- Open-source DFT code (e.g., CP2K): https://www.cp2k.org/
- Basis sets / pseudopotentials: https://www.crystal.unito.it/basis_sets.html

## Workflow steps

### Step 1: Ground-state geometry optimization and band gap
- Role: scored
- Action: Retrieve the CaWO4 scheelite crystal structure from ICSD #18135 or literature. Set up a periodic DFT calculation with a hybrid functional (e.g., B3LYP) to optimize the atomic positions and cell parameters of the ground singlet state (s). After convergence, perform a single-point calculation to obtain the direct Kohn-Sham band gap. Report the optimized lattice parameters, W-O bond length, O-W-O angles, total energy per cell, and band gap in the output CSV.
- Output file: `/app/outputs/step_01_ground_state_summary.csv`
- Format: csv
- Contract: CSV with columns: parameter (string), unit (string), value (float). Rows: a, c, W-O distance, angle_alpha, angle_beta, total_energy, band_gap.
- Scoring: scored by hidden verifier

### Step 2: Excited-state geometry optimization and band gap
- Role: scored
- Action: Starting from the optimized ground-state geometry, set up an excited singlet state calculation by promoting an electron from the highest occupied to the lowest unoccupied Kohn-Sham state (or using another state-specific approach) and fully relax the geometry. After convergence, compute the direct band gap. Report the optimized lattice parameters, bond lengths, angles, total energy, and band gap in the output CSV.
- Output file: `/app/outputs/step_02_excited_state_summary.csv`
- Format: csv
- Contract: CSV with same columns as step_01.
- Scoring: scored by hidden verifier

### Step 3: Vibrational analysis and energy comparison
- Role: scored (load-bearing)
- Action: At the optimized excited-state geometry, compute the gamma-point vibrational frequencies to verify that s* is a local minimum (no imaginary modes). Read the total energies from the previous summaries and compute ΔE = E(s*) − E(s). Write the energy difference and the minimum verification result to the output text file.
- Output file: `/app/outputs/step_03_energy_comparison.txt`
- Format: txt
- Contract: Text file with two lines: 'Delta_E (eV): <value>' and 's_star_is_minimum: <true/false>'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_ground_state_summary.csv`
- `/app/outputs/step_02_excited_state_summary.csv`
- `/app/outputs/step_03_energy_comparison.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_ground_state_summary.csv
- path: `/app/outputs/step_01_ground_state_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ground singlet state (s) optimized lattice parameters, bond lengths, angles, total energy, and band gap.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `unit`, `value`
  - `columns`:
    - `parameter`: string
    - `unit`: string
    - `value`: float

### step_02_excited_state_summary.csv
- path: `/app/outputs/step_02_excited_state_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Excited singlet state (s*) optimized geometry and electronic structure.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `unit`, `value`
  - `columns`:
    - `parameter`: string
    - `unit`: string
    - `value`: float

### step_03_energy_comparison.txt
- path: `/app/outputs/step_03_energy_comparison.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Energy difference between s* and s, and verification that the excited state is a local minimum.
- schema:
  - `type`: text
  - `required`:
    - `lines`: `Delta_E (eV):`, `s_star_is_minimum:`

Notes: All outputs are compared to hidden paper-reported values with tolerances (lattice ±0.01 Å, bonds ±0.005 Å, angles ±0.5°, total energy ±0.05 eV, band gap ±0.1 eV). ΔE must be positive and the minimum index true. The checker uses reference_match policy to validate each artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_ground_state_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "unit",
          "value"
        ],
        "columns": {
          "parameter": "string",
          "unit": "string",
          "value": "float"
        }
      },
      "description": "Ground singlet state (s) optimized lattice parameters, bond lengths, angles, total energy, and band gap."
    },
    {
      "file": "step_02_excited_state_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "unit",
          "value"
        ],
        "columns": {
          "parameter": "string",
          "unit": "string",
          "value": "float"
        }
      },
      "description": "Excited singlet state (s*) optimized geometry and electronic structure."
    },
    {
      "file": "step_03_energy_comparison.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": {
          "lines": [
            "Delta_E (eV):",
            "s_star_is_minimum:"
          ]
        }
      },
      "description": "Energy difference between s* and s, and verification that the excited state is a local minimum."
    }
  ],
  "notes": "All outputs are compared to hidden paper-reported values with tolerances (lattice ±0.01 Å, bonds ±0.005 Å, angles ±0.5°, total energy ±0.05 eV, band gap ±0.1 eV). ΔE must be positive and the minimum index true. The checker uses reference_match policy to validate each artifact."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. For each scored workflow step, the verifier reads your output file and compares every numerical entry against independently established reference values. The comparison uses appropriate tolerances that account for differences in DFT implementations and basis sets. Each step contributes a weighted score, and the final reward is the weighted sum. Merely reporting numbers that "look plausible" or copying expected values is not sufficient; the verifier requires that your computed quantities are physically consistent and fall within the accepted ranges. The exact weighting and tolerance thresholds are hidden, so focus on faithfully executing the workflow and obtaining physically meaningful results.
