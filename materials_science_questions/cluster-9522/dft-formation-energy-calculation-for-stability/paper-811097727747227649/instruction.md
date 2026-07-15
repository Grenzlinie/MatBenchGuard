# DFT Formation Energy and Magnetic Moment Calculation for Cr-V-Sb Phase Stability

## Problem background
Antimonides in the pseudoternary system (Cr,V)–Sb can adopt several different crystal structures, including the cubic A15 type (Cr₃Si-type, space group Pm-3n), the hexagonal Ni₂In type (P6₃/mmc), and the cubic Heusler type (Ni₂MnAl-type, Fm-3m). Which structure is thermodynamically preferred depends on both the Cr:V ratio and the overall metal-to-antimony stoichiometry. Thin-film synthesis experiments often compete between these phases, so predicting the ground-state structure for a given composition is important for understanding phase formation. Additionally, some of these structures may exhibit local magnetic moments on the transition-metal sites. This task computes the spin-polarized DFT total energy per formula unit for all candidate phases across a range of Cr concentrations for both M:Sb = 3:1 and M:Sb = 2:1, and extracts the magnetic moments in the hexagonal phase. The results will reveal the relative phase stability ordering and the magnetic behavior.

## Approach
Spin-polarised first-principles calculations based on density functional theory (DFT) will be performed using the local spin-density approximation (LSDA, Vosko-Wilk-Nusair) and the open-source plane-wave code Quantum ESPRESSO. Pseudopotentials are taken from the SSSP efficiency library (v1.3). For each discrete Cr concentration x = 0, 0.25, 0.5, 0.75, 1.0 in the alloy (CrₓV₁₋ₓ), supercells are constructed to represent the desired stoichiometry for the A15, Ni₂In, and Heusler structures (the Heusler structure only for the M:Sb = 2:1 stoichiometry). Each structure is then fully relaxed — both atomic positions and lattice parameters — to obtain its ground-state geometry. From the relaxed outputs the total energy per formula unit is extracted for every system, and for the hexagonal Ni₂In-type phase the local spin magnetic moments on the two crystallographically distinct transition-metal sites are recorded. By comparing the total energies of the competing structures at each composition, the relative phase stability can be evaluated.

## Reproduction target
Produce two comma-separated-value (CSV) tables. (1) `total_energies.csv`: one row per composition and structure covering all (Cr,V)₃Sb (M:Sb = 3:1) and (Cr,V)₂Sb (M:Sb = 2:1) systems and all candidate structures; columns are `composition_label` (e.g. 'x0.25_3to1'), `structure` (one of 'A15', 'Ni2In', 'Heusler'), and `total_energy_per_fu_eV` (eV per formula unit). (2) `magnetic_moments.csv`: one row per crystallographically distinct Cr site in the hexagonal Ni₂In-type phase for both stoichiometries; columns are `composition_label` (e.g. 'x0.25_3to1_hex'), `site_index` (1 or 2), and `magnetic_moment_muB` (μB). The energy data should allow a verifier to infer the lowest-energy structure at each composition, and the magnetic moments should be physically plausible for Cr in such an environment.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency v1.3): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: For each (Cr,V)xSb composition with Cr concentration x = 0, 0.25, 0.5, 0.75, 1.0 for stoichiometries M:Sb=3:1 and 2:1, construct supercells for the A15 (space group Pm-3n), hexagonal Ni2In-type (P63/mmc), and Heusler Ni2MnAl-type (Fm-3m, only for M:Sb=2:1) structures. Run spin-polarized DFT calculations using Quantum ESPRESSO with the LSDA functional (Vosko-Wilk-Nusair) and SSSP pseudopotentials. Perform variable-cell relaxation (vc-relax) to optimize lattice parameters and atomic positions. Save the relaxation output files for each system.
- Evidence: `/app/outputs/relaxation_outputs`

### Step 2: Total energy extraction
- Role: scored (load-bearing)
- Action: Parse the relaxation output files from step s1. For each composition and structure, extract the converged total energy per formula unit (eV). Write a CSV file containing one row per (composition, structure) pair covering both M:Sb=3:1 and 2:1 stoichiometries and all required structures.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: columns: composition_label (str, e.g. 'x0.25_3to1'), structure (str, one of 'A15','Ni2In','Heusler'), total_energy_per_fu_eV (float, eV)
- Scoring: scored by hidden verifier

### Step 3: Magnetic moment extraction
- Role: scored
- Action: From the relaxation output files of step s1, extract the local spin magnetic moments (μB) of Cr atoms in the hexagonal Ni2In-type phase for both stoichiometries (M:Sb=3:1 and 2:1). The hexagonal phase contains two non-equivalent transition-metal sites; report the magnetic moment on each site. Write a CSV with one row per site per composition.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: columns: composition_label (str, e.g. 'x0.25_3to1_hex'), site_index (int, 1 or 2), magnetic_moment_muB (float, μB)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.csv`
- `/app/outputs/magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total energy per formula unit for all calculated (Cr,V)Sb compositions and candidate structures. The hidden checker verifies that the energy ordering matches the phase stability trends predicted by the paper.
- schema:
  - `type`: table
  - `required_columns`: `composition_label`, `structure`, `total_energy_per_fu_eV`
  - `units`:
    - `total_energy_per_fu_eV`: eV per formula unit

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Local Cr magnetic moments for the hexagonal Ni2In-type phase for both stoichiometries. The hidden checker verifies that the moments fall within the expected range.
- schema:
  - `type`: table
  - `required_columns`: `composition_label`, `site_index`, `magnetic_moment_muB`
  - `units`:
    - `magnetic_moment_muB`: μB

Notes: Scoring is based on relative energy ordering (A15 vs Ni2In etc.) and magnetic moment ranges, with tolerances that absorb code-to-code differences. The solver must run all DFT relaxations; no pre-computed total energies or moments are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_label",
          "structure",
          "total_energy_per_fu_eV"
        ],
        "units": {
          "total_energy_per_fu_eV": "eV per formula unit"
        }
      },
      "description": "Total energy per formula unit for all calculated (Cr,V)Sb compositions and candidate structures. The hidden checker verifies that the energy ordering matches the phase stability trends predicted by the paper."
    },
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_label",
          "site_index",
          "magnetic_moment_muB"
        ],
        "units": {
          "magnetic_moment_muB": "μB"
        }
      },
      "description": "Local Cr magnetic moments for the hexagonal Ni2In-type phase for both stoichiometries. The hidden checker verifies that the moments fall within the expected range."
    }
  ],
  "notes": "Scoring is based on relative energy ordering (A15 vs Ni2In etc.) and magnetic moment ranges, with tolerances that absorb code-to-code differences. The solver must run all DFT relaxations; no pre-computed total energies or moments are provided."
}
```

## How you are scored
Your submission is evaluated by a hidden automated checker that reads your CSV files and independently verifies the results. The checker checks whether the total energy ordering among the candidate structures follows the physical phase‑stability pattern (i.e., which structure has the lowest energy at each composition) and whether the Cr magnetic moments in the hexagonal phase lie within a plausible range. The overall score is a weighted combination: energy‑ordering correctness accounts for 70 %, and magnetic‑moment compliance for 30 %. Because the checker compares trends and ranges, rather than exact numerical matches, moderate code‑to‑code variations are tolerated — what matters is that the relative stabilities and magnetic moments are internally consistent and physically sound. Simply reporting numbers that resemble reference values is not sufficient; the verifier recomputes the ordering and moment compliance from your data, so the calculations must reflect a genuine DFT relaxation.
