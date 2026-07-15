# DFT Stability Analysis of Cr2O3 Surface Terminations

## Problem background
Understanding the surface termination of α‑Cr₂O₃(0001) under different gas environments is crucial for applications in catalysis, corrosion protection, and nuclear reactor safety. The (0001) surface can adopt various oxygen, hydrogen, and water terminations depending on temperature and partial pressure, but which terminations are stable under given conditions is not fully resolved. This task aims to determine, from first‑principles density‑functional theory calculations, the relative stabilities of a set of well‑defined terminations and the chemical‑potential boundaries that separate them.

## Approach
Use plane‑wave DFT+U (on‑site Coulomb U and exchange J for Cr) with the PBE functional to compute total energies. Construct symmetric slab models of α‑Cr₂O₃(0001) with the experimental in‑plane lattice parameter (a = 4.951 Å), 12 Cr layers, ∼21 Å vacuum gap, and the ground‑state CCC spin configuration. A double hexagonal cell is employed to accommodate all terminations. For the oxygen series, consider terminations I (Cr‑O₃‑Cr), II (Cr‑O₃‑Cr‑O), III (Cr‑O₃‑Cr‑O₂), IV (Cr‑O₃‑Cr‑O₃), VI (Cr‑Cr‑O₃/₂), and X (Cr‑Cr‑O₃). For the hydrogen series, treat bare‑H1, bare‑H2, bare‑H3 adsorbed on the Cr‑terminated surface, as well as chromyl‑OH and chromyl‑H₂O derived from the chromyl (II) surface. For the water series, model dissociative and associative adsorption on the Cr‑terminated surface (Cr‑O₃‑H‑Cr‑OH, Cr‑O₃‑H‑Cr‑OH·H₂O, Cr‑O₃‑H‑Cr‑OH·(H₂O)₂) and on the O‑terminated surface (Cr‑Cr‑O₂‑H, Cr‑Cr‑O₃‑H₃). Also compute total energies of isolated O₂, H₂, and H₂O molecules in the same computational setup. From the total energies, calculate the 0 K relative surface energy ΔE of each termination with respect to termination I, using ΔE = (E_slab − E_Cr₁₂O₁₈ − N·E_ref) / (2A), where A is the slab surface area and N is the number of reference molecules (O₂, H₂, or H₂O) added or extracted. For the oxygen series, use the thermodynamic formalism at 0 K to express ΔE as a linear function of the oxygen chemical potential μ−μ₀ and find the crossing points where the ΔE of two terminations become equal. Specifically, determine the μ−μ₀ values at which I ↔ II and II ↔ IV have equal energy.

## Reproduction target
Produce four scored artifacts based solely on your DFT calculations:
1. `/app/outputs/oxygen_relative_energies.csv` – columns `termination` (I, II, III, IV, VI, X) and `de` (meV/Å²).
2. `/app/outputs/hydrogen_relative_energies.csv` – columns `termination` (bare_H1, bare_H2, bare_H3, chromyl_OH, chromyl_H₂O) and `de` (meV/Å²).
3. `/app/outputs/water_relative_energies.csv` – columns `termination` (Cr‑O₃‑H‑Cr‑OH, Cr‑O₃‑H‑Cr‑OH(H₂O), Cr‑O₃‑H‑Cr‑OH(H₂O)₂, Cr‑Cr‑O₂‑H, Cr‑Cr‑O₃‑H₃) and `de` (meV/Å²).
4. `/app/outputs/chemical_potential_crossings.json` – a JSON object with keys `"I_II_crossing"` and `"II_IV_crossing"`, each mapping to the oxygen chemical‑potential value μ−μ₀ (in eV) where the two indicated terminations have the same relative energy.
All energies must be computed from your DFT total energies; no external datasets or pre‑computed values are allowed.

## Assets

- Quantum ESPRESSO (or other open-source DFT plane-wave code): https://www.quantum-espresso.org/
- Cr PAW pseudopotential: https://www.quantum-espresso.org/pseudopotentials
- O PAW pseudopotential: https://www.quantum-espresso.org/pseudopotentials
- H PAW pseudopotential: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT total energy calculations for all slabs and gas molecules
- Role: process
- Action: Construct symmetric slab models of α-Cr2O3(0001) for the required oxygen, hydrogen, and water terminations and compute total DFT+U energies using an open-source plane-wave code (e.g., Quantum ESPRESSO) with provided pseudopotentials. Also compute isolated-molecule total energies for O2, H2, and H2O in the same computational setup. Record all relevant total energies in a log file.
- Evidence: `/app/outputs/dft_energies.txt`

### Step 2: Oxygen series relative surface energies
- Role: scored
- Action: From the DFT total energies, compute the 0 K relative surface energy ΔE (meV/Å²) for each oxygen-series termination (I, II, III, IV, VI, X) with respect to termination I using the standard reaction formula involving the slab energies, O2 reference energy, and surface area. Write the results to a CSV file.
- Output file: `/app/outputs/oxygen_relative_energies.csv`
- Format: csv
- Contract: termination: string; de: float, meV/Å²
- Scoring: scored by hidden verifier

### Step 3: Hydrogen series relative surface energies
- Role: scored
- Action: From the DFT total energies, compute the 0 K relative surface energy ΔE (meV/Å²) for each hydrogen-series termination (bare_H1, bare_H2, bare_H3, chromyl_OH, chromyl_H2O) with respect to termination I using the appropriate reaction formula involving slab energies, H2 reference, and surface area. Write the results to a CSV file.
- Output file: `/app/outputs/hydrogen_relative_energies.csv`
- Format: csv
- Contract: termination: string; de: float, meV/Å²
- Scoring: scored by hidden verifier

### Step 4: Water series relative surface energies
- Role: scored
- Action: From the DFT total energies, compute the 0 K relative surface energy ΔE (meV/Å²) for each water-series termination (Cr-O3-H-Cr-OH, Cr-O3-H-Cr-OH(H2O), Cr-O3-H-Cr-OH(H2O)2, Cr-Cr-O2-H, Cr-Cr-O3-H3) with respect to termination I using the appropriate reaction formula involving slab energies, H2O reference, and surface area. Write the results to a CSV file.
- Output file: `/app/outputs/water_relative_energies.csv`
- Format: csv
- Contract: termination: string; de: float, meV/Å²
- Scoring: scored by hidden verifier

### Step 5: Oxygen chemical potential crossings
- Role: scored (load-bearing)
- Action: Using the oxygen relative surface energies, determine the oxygen chemical-potential values (μ−μ₀ in eV) at which the relative energies of terminations I and II, and II and IV, become equal at 0 K. Solve the linear equations derived from the standard thermodynamic formalism. Write the two crossing points to a JSON file.
- Output file: `/app/outputs/chemical_potential_crossings.json`
- Format: json
- Contract: I_II_crossing: float, eV; II_IV_crossing: float, eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/oxygen_relative_energies.csv`
- `/app/outputs/hydrogen_relative_energies.csv`
- `/app/outputs/water_relative_energies.csv`
- `/app/outputs/chemical_potential_crossings.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### oxygen_relative_energies.csv
- path: `/app/outputs/oxygen_relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: 0 K relative surface energies for the oxygen series terminations. Values are compared to hidden gold with tolerance; lower absolute deviations earn full credit.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `de`
  - `units`:
    - `de`: meV/Å²

### hydrogen_relative_energies.csv
- path: `/app/outputs/hydrogen_relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: 0 K relative surface energies for the hydrogen series terminations. Scored similarly to oxygen series.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `de`
  - `units`:
    - `de`: meV/Å²

### water_relative_energies.csv
- path: `/app/outputs/water_relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: 0 K relative surface energies for the water series terminations. Scored similarly to oxygen series.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `de`
  - `units`:
    - `de`: meV/Å²

### chemical_potential_crossings.json
- path: `/app/outputs/chemical_potential_crossings.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Chemical-potential crossing points between terminations I↔II and II↔IV. Compared to hidden gold with tolerance.
- schema:
  - `type`: object
  - `required`: `I_II_crossing`, `II_IV_crossing`
  - `units`:
    - `I_II_crossing`: eV
    - `II_IV_crossing`: eV

Notes: All relative energies are with respect to the bare Cr-terminated surface (I) and use the slab double-cell construction. The chemical-potential crossings are derived from the oxygen relative energies at 0 K. The agent must perform the full DFT calculations; no pre-computed energies are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "oxygen_relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "de"
        ],
        "units": {
          "de": "meV/Å²"
        }
      },
      "description": "0 K relative surface energies for the oxygen series terminations. Values are compared to hidden gold with tolerance; lower absolute deviations earn full credit."
    },
    {
      "file": "hydrogen_relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "de"
        ],
        "units": {
          "de": "meV/Å²"
        }
      },
      "description": "0 K relative surface energies for the hydrogen series terminations. Scored similarly to oxygen series."
    },
    {
      "file": "water_relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "de"
        ],
        "units": {
          "de": "meV/Å²"
        }
      },
      "description": "0 K relative surface energies for the water series terminations. Scored similarly to oxygen series."
    },
    {
      "file": "chemical_potential_crossings.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "I_II_crossing",
          "II_IV_crossing"
        ],
        "units": {
          "I_II_crossing": "eV",
          "II_IV_crossing": "eV"
        }
      },
      "description": "Chemical-potential crossing points between terminations I↔II and II↔IV. Compared to hidden gold with tolerance."
    }
  ],
  "notes": "All relative energies are with respect to the bare Cr-terminated surface (I) and use the slab double-cell construction. The chemical-potential crossings are derived from the oxygen relative energies at 0 K. The agent must perform the full DFT calculations; no pre-computed energies are provided."
}
```

## How you are scored
Each of the four scored artifacts is independently verified by a hidden checker that compares your reported values against hidden reference values (derived from the original paper’s results). For the three CSV files, the checker uses a threshold‑or‑better policy: the closer your computed ΔE values are to the hidden reference, the higher your score, with full credit awarded when the deviation is within a tolerance that accounts for legitimate DFT‑implementation differences. For the chemical‑potential crossings, the reported μ−μ₀ values are compared to the hidden reference values with a similar tolerance‑based scoring. The final reward is a weighted average of the scores from the four artifacts; the chemical‑potential crossings carry a higher weight because they depend on the correct execution of all prior calculations. Missing or malformed artifacts receive zero credit for that stage.
