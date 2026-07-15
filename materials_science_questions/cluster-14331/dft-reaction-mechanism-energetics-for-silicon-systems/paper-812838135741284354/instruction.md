# DFT and Kinetic Study of Beta-Elimination of 2,2-Difluoroethylsilane Derivatives

## Problem background
The gas-phase β‑elimination of 2,2‑difluoroethylsilane derivatives (CHF₂CH₂SiFₙMe₃₋ₙ, n = 0–3) is believed to proceed via a four‑center cyclic transition state. Computational studies using density functional theory (M06‑2x) and a high‑level composite electronic structure method (CBS‑QB3) have been performed to compute activation barriers, reaction thermochemistry, and pressure‑dependent unimolecular rate constants with transition‑state theory (TST) and RRKM theory. The task is to reproduce the key computational predictions: how the barrier and rate constants change when fluorine atoms on silicon are replaced by methyl groups, and at what pressure the TST approximation breaks down for the most reactive pathway.

## Approach
The reproduction follows a computational workflow: build initial 3D structures for the reactants, a four‑center cyclic transition state guess, and the products for each of the four compounds (n = 0, 1, 2, 3); optimize all geometries at the M06‑2x/aug‑cc‑pVTZ level and confirm that every transition state has exactly one imaginary frequency; refine the electronic energies with a composite method of CBS‑QB3 quality (e.g., DLPNO‑CCSD(T)/CBS) and add zero‑point and thermal corrections to obtain the activation and reaction energies. The energies and vibrational frequencies are then fed into the KiSThelP program to compute TST and RRKM unimolecular rate constants across the experimental temperature range (151–246 °C) and a broad pressure range (10⁻¹² to 10² bar), including Wigner tunneling and Lennard‑Jones collision parameters appropriate for each species with argon bath gas. The final outputs are structured data files that allow independent verification of the computed energetics and the fall‑off behavior of the rate constants.

## Reproduction target
Produce three output artifacts:

1. `energies.json` – activation energies (ΔE₀K‡, ΔH₂₉₈‡, ΔG₂₉₈‡) and reaction energies (ΔE₀K, ΔH₂₉₈, ΔG₂₉₈) in kcal/mol for each of the four pathways.
2. `rate_constants.csv` – TST and RRKM unimolecular rate constants (s⁻¹) at every experimental temperature and at a pressure grid that spans 10⁻¹² to 10² bar, for all four pathways.
3. `falloff_summary.json` – a boolean indicating whether the TST approximation for pathway 1 deviates significantly from RRKM at low pressures, and the highest pressure (in bar) at which the TST/RRKM ratio falls below 0.9.

## Assets

- Quantum chemistry software (ORCA or open-source equivalent like Psi4 or PySCF): https://orcaforum.kofo.mpg.de/ (ORCA) or https://psicode.org/ (Psi4)
- KiSThelP: https://kisthelp.lct.jussieu.fr/

## Workflow steps

### Step 1: Geometry optimization and TS verification
- Role: process
- Action: Build initial 3D structures for reactants, transition states (4-center cyclic guesses), and products of compounds 1–4. Optimize geometries at M06-2x/aug-cc-pVTZ level and compute harmonic vibrational frequencies. Confirm each TS has exactly one imaginary frequency.
- Evidence: `/app/outputs/optimization_output.log`

### Step 2: High-level energy calculation
- Role: scored (load-bearing)
- Action: Using the optimized geometries, perform single-point energy calculations with a high-level composite method equivalent to CBS-QB3 (e.g., DLPNO-CCSD(T)/CBS) to obtain electronic energies. Compute zero-point vibrational energies and thermal corrections to derive activation energies (ΔE0K‡, ΔH298‡, ΔG298‡) and reaction energies (ΔE0K, ΔH298, ΔG298) for all four pathways. Write the results to energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: Object with keys "R1->P1", "R2->P2", "R3->P3", "R4->P4". Each key maps to an object with two sub-objects: "activation" (fields: delta_E0_dagger, delta_H298_dagger, delta_G298_dagger in kcal/mol) and "reaction" (fields: delta_E0, delta_H298, delta_G298 in kcal/mol).
- Scoring: scored by hidden verifier

### Step 3: TST and RRKM kinetics calculation
- Role: process
- Action: Using KiSThelP, compute TST and RRKM unimolecular rate constants for all pathways over the temperature range 151–246 °C and pressures from 10⁻¹² to 10² bar. Use the activation barriers and vibrational frequencies from previous steps, include Wigner tunneling correction, and apply Lennard-Jones collision parameters (σ ≈ 4.8 Å, ε/kB appropriate for each compound, with Ar bath gas).
- Evidence: `/app/outputs/kisthelp_full_output.log`

### Step 4: Rate constants table
- Role: scored
- Action: From the KiSThelP output, extract TST and RRKM rate constants at the experimental temperatures and pressures. Write a CSV file rate_constants.csv with columns: pathway, temperature_C, pressure_bar, TST_rate, RRKM_rate. Include all temperatures from 151 to 246 °C (in °C) and a sufficient pressure grid covering the fall-off (e.g., 10⁻¹², 10⁻¹¹, …, 10² bar).
- Output file: `/app/outputs/rate_constants.csv`
- Format: csv
- Contract: Columns: pathway (str), temperature_C (float), pressure_bar (float, scientific notation), TST_rate (float, s^-1), RRKM_rate (float, s^-1).
- Scoring: scored by hidden verifier

### Step 5: Fall-off analysis
- Role: scored
- Action: Analyze the pressure dependence for pathway 1 (R1->P1). Determine the highest pressure (in bar) at which the TST rate constant deviates by more than 10% from the RRKM rate (i.e., TST/RRKM < 0.9) at any temperature in the experimental range. Write this analysis to falloff_summary.json with a boolean 'pathway1_falloff' (true if TST breaks down at P < 10⁻⁴ bar) and the numeric 'breakdown_pressure_bar'.
- Output file: `/app/outputs/falloff_summary.json`
- Format: json
- Contract: Object with keys "pathway1_falloff" (bool) and "breakdown_pressure_bar" (float, in bar).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`
- `/app/outputs/rate_constants.csv`
- `/app/outputs/falloff_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Activation and reaction energies for all four pathways at an equivalent CBS-QB3 composite level.
- schema:
  - `type`: object
  - `required`:
    - `R1->P1`:
      - `activation`:
        - `delta_E0_dagger`: kcal/mol
        - `delta_H298_dagger`: kcal/mol
        - `delta_G298_dagger`: kcal/mol
      - `reaction`:
        - `delta_E0`: kcal/mol
        - `delta_H298`: kcal/mol
        - `delta_G298`: kcal/mol
    - `R2->P2`: same structure
    - `R3->P3`: same structure
    - `R4->P4`: same structure

### rate_constants.csv
- path: `/app/outputs/rate_constants.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: TST and RRKM unimolecular rate constants for all four pathways over the experimental temperature range and a pressure grid covering 10⁻¹² to 10² bar.
- schema:
  - `type`: table
  - `required_columns`: `pathway`, `temperature_C`, `pressure_bar`, `TST_rate`, `RRKM_rate`
  - `units`:
    - `temperature_C`: degrees Celsius
    - `pressure_bar`: bar
    - `TST_rate`: s^-1
    - `RRKM_rate`: s^-1

### falloff_summary.json
- path: `/app/outputs/falloff_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Boolean and pressure threshold where TST/RRKM ratio drops below 0.9 for pathway 1.
- schema:
  - `type`: object
  - `required`:
    - `pathway1_falloff`: bool
    - `breakdown_pressure_bar`: float (bar)

Notes: The energies should be computed using an open-source composite method of CBS-QB3 quality. Lennard-Jones parameters for RRKM can be taken from the paper's Table 1 or standard sources; they are not separately scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R1->P1": {
            "activation": {
              "delta_E0_dagger": "kcal/mol",
              "delta_H298_dagger": "kcal/mol",
              "delta_G298_dagger": "kcal/mol"
            },
            "reaction": {
              "delta_E0": "kcal/mol",
              "delta_H298": "kcal/mol",
              "delta_G298": "kcal/mol"
            }
          },
          "R2->P2": "same structure",
          "R3->P3": "same structure",
          "R4->P4": "same structure"
        }
      },
      "description": "Activation and reaction energies for all four pathways at an equivalent CBS-QB3 composite level."
    },
    {
      "file": "rate_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pathway",
          "temperature_C",
          "pressure_bar",
          "TST_rate",
          "RRKM_rate"
        ],
        "units": {
          "temperature_C": "degrees Celsius",
          "pressure_bar": "bar",
          "TST_rate": "s^-1",
          "RRKM_rate": "s^-1"
        }
      },
      "description": "TST and RRKM unimolecular rate constants for all four pathways over the experimental temperature range and a pressure grid covering 10⁻¹² to 10² bar."
    },
    {
      "file": "falloff_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "pathway1_falloff": "bool",
          "breakdown_pressure_bar": "float (bar)"
        }
      },
      "description": "Boolean and pressure threshold where TST/RRKM ratio drops below 0.9 for pathway 1."
    }
  ],
  "notes": "The energies should be computed using an open-source composite method of CBS-QB3 quality. Lennard-Jones parameters for RRKM can be taken from the paper's Table 1 or standard sources; they are not separately scored."
}
```

## How you are scored
A hidden verifier independently scores each of the three artifacts. The activation and reaction energies are compared to reference values within an allowed tolerance that reflects the use of an open‑source composite method. The rate constant file is used to recompute the TST/RRKM ratio for pathway 1 and to confirm the fall‑off behavior; the verifier checks that the ratio drops below 0.9 at the breakdown pressure reported in `falloff_summary.json`. The fall‑off summary is also cross‑checked for consistency with the recomputed ratios. The final score is a weighted combination of these checks, with the largest weights assigned to the energies and to the fall‑off verification. No single numerical target from the source literature is required; the scoring rewards a physically correct reproduction and internally consistent data.
