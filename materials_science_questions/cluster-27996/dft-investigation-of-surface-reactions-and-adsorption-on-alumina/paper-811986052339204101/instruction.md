# DFT Simulation of Polymer–Al₂O₃ Interfacial Interactions

## Problem background
Polymer-alumina nanocomposites have demonstrated enhanced dielectric properties, which could enable further miniaturization of electronic devices. The dielectric enhancement is thought to originate from interfacial interactions between the polymer matrix and the alumina nano-particles. To understand the mechanism, this work models the molecular interactions in the interfacial region by computing stabilization energies and dipole moments for polymer–Al₂O₃ complexes using quantum chemical calculations.

## Approach
The approach uses ab initio molecular orbital calculations at both Hartree–Fock (HF) and density functional theory (DFT) levels. Molecular models are built for the polymer repeat unit, truncated fragments that represent the three distinct oxygen sites (labelled a, b, c) where Al₂O₃ can adsorb, and complexes of Al₂O₃ with these sites. Geometry optimizations are performed with ORCA, an open-source quantum chemistry package, to obtain total energies and dipole moments. Stabilization energies are then computed as the difference between the complex energy and the sum of the isolated fragment and Al₂O₃ energies. The calculations are repeated for two theory levels: HF/3-21G and B3LYP/6-31+G(d). For the full repeat unit, complexes with one or two Al₂O₃ molecules are considered.

## Reproduction target
Reproduce stabilization energies (in kJ mol⁻¹) for a single Al₂O₃ molecule adsorbed on each of the three oxygen sites (a, b, c) using both truncated models at HF/3-21G and B3LYP/6-31+G(d), and for the full polymer repeat unit with one Al₂O₃ on site a, one on site b, and two Al₂O₃ on sites a and b at HF/3-21G. Additionally, compute the total dipole moment (in Debye) for the isolated repeat unit and the same full-repeat-unit complexes at HF/3-21G. All results must be written to the specified CSV files.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de

## Workflow steps

### Step 1: Perform DFT geometry optimizations
- Role: process
- Action: Build molecular models and run geometry optimizations at HF/3-21G and B3LYP/6-31+G(d) levels for the following species: isolated Al₂O₃ molecule, isolated polymer repeat unit, truncated models for oxygen sites a, b, c and their complexes with one Al₂O₃, and full repeat unit complexes with one Al₂O₃ on site a, one on site b, and two Al₂O₃ on sites a and b. Store total energies and dipole moments (HF/3-21G) for subsequent calculation.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: Report single-site stabilization energies (truncated models)
- Role: scored (load-bearing)
- Action: From the optimized total energies, compute stabilization energy as ΔE = E(complex) – E(fragment) – E(Al₂O₃) and convert to kJ/mol. Report for each oxygen site (a, b, c) and both theory levels.
- Output file: `/app/outputs/stabilization_energies_single.csv`
- Format: csv
- Contract: CSV with columns: model (a, b, c), level (HF-3-21G, B3LYP-6-31+G-d), stabilization_energy_kJ_mol (float)
- Scoring: scored by hidden verifier

### Step 3: Report additive stabilization energies (full repeat unit)
- Role: scored (load-bearing)
- Action: From the optimized total energies, compute stabilization energy as ΔE = E(complex) – E(repeat_unit) – n × E(Al₂O₃) (n=1 or 2) and convert to kJ/mol. Report for complexes R+Al₂O₃ on a, R+Al₂O₃ on b, R+2Al₂O₃ on a and b at HF/3-21G.
- Output file: `/app/outputs/stabilization_energies_additive.csv`
- Format: csv
- Contract: CSV with columns: complex (R+Al2O3_on_a, R+Al2O3_on_b, R+2Al2O3_on_a_and_b), level (HF-3-21G), stabilization_energy_kJ_mol (float)
- Scoring: scored by hidden verifier

### Step 4: Report dipole moments (full repeat unit)
- Role: scored (load-bearing)
- Action: From the HF/3-21G optimized structures, extract the total dipole moment in Debye for the isolated repeat unit and each full-repeat-unit complex (R+Al₂O₃ on a, R+Al₂O₃ on b, R+2Al₂O₃ on a and b) and report.
- Output file: `/app/outputs/dipole_moments.csv`
- Format: csv
- Contract: CSV with columns: model (isolated_R, R+Al2O3_on_a, R+Al2O3_on_b, R+2Al2O3_on_a_and_b), level (HF-3-21G), dipole_total_Debye (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stabilization_energies_single.csv`
- `/app/outputs/stabilization_energies_additive.csv`
- `/app/outputs/dipole_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stabilization_energies_single.csv
- path: `/app/outputs/stabilization_energies_single.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stabilization energies for Al₂O₃ adsorbed on oxygen sites a, b, c using truncated polymer models at HF/3-21G and B3LYP/6-31+G(d).
- schema:
  - `type`: table
  - `required_columns`: `model`, `level`, `stabilization_energy_kJ_mol`
  - `units`:
    - `stabilization_energy_kJ_mol`: kJ mol⁻¹

### stabilization_energies_additive.csv
- path: `/app/outputs/stabilization_energies_additive.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stabilization energies for full polymer repeat unit with one or two Al₂O₃ molecules at HF/3-21G.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `level`, `stabilization_energy_kJ_mol`
  - `units`:
    - `stabilization_energy_kJ_mol`: kJ mol⁻¹

### dipole_moments.csv
- path: `/app/outputs/dipole_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dipole moments for the isolated polymer repeat unit and its complexes with Al₂O₃ at HF/3-21G.
- schema:
  - `type`: table
  - `required_columns`: `model`, `level`, `dipole_total_Debye`
  - `units`:
    - `dipole_total_Debye`: Debye

Notes: The molecular structures must be built from the paper's description; no pre-made coordinate files are provided. The agent may use remote or high-performance computing for the DFT optimizations. Scoring compares reported values to reference values with tolerances appropriate for the level of theory. Structural consistency checks (site ordering and additivity) are applied by the checker but not declared as separate output files.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stabilization_energies_single.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "level",
          "stabilization_energy_kJ_mol"
        ],
        "units": {
          "stabilization_energy_kJ_mol": "kJ mol⁻¹"
        }
      },
      "description": "Stabilization energies for Al₂O₃ adsorbed on oxygen sites a, b, c using truncated polymer models at HF/3-21G and B3LYP/6-31+G(d)."
    },
    {
      "file": "stabilization_energies_additive.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "level",
          "stabilization_energy_kJ_mol"
        ],
        "units": {
          "stabilization_energy_kJ_mol": "kJ mol⁻¹"
        }
      },
      "description": "Stabilization energies for full polymer repeat unit with one or two Al₂O₃ molecules at HF/3-21G."
    },
    {
      "file": "dipole_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "level",
          "dipole_total_Debye"
        ],
        "units": {
          "dipole_total_Debye": "Debye"
        }
      },
      "description": "Dipole moments for the isolated polymer repeat unit and its complexes with Al₂O₃ at HF/3-21G."
    }
  ],
  "notes": "The molecular structures must be built from the paper's description; no pre-made coordinate files are provided. The agent may use remote or high-performance computing for the DFT optimizations. Scoring compares reported values to reference values with tolerances appropriate for the level of theory. Structural consistency checks (site ordering and additivity) are applied by the checker but not declared as separate output files."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. Each scored output file (stabilization energies and dipole moments) is independently checked against hidden reference values derived from the published work. The verifier compares the reported numbers with tolerances appropriate for the computational method, and it also verifies internal consistency (e.g., the ordering of site energies and approximate additivity of multiple adsorption). The final score is a weighted combination of these checks. Simply copying the published numbers is not sufficient — you must execute the simulations and report the actual computed results from your DFT/HF calculations.
