# DFT Activation Barriers and Free Energies for Acrolein Hydrodeoxygenation Pathways on a Mo3O9 Cluster Model

## Problem background
Hydrodeoxygenation (HDO) of bio‑oil oxygenates is a key step in upgrading pyrolysis products to transportation fuels. Acrolein, the simplest unsaturated aldehyde, serves as a model molecule to study the competition between C=C hydrogenation and C=O hydrogenation on reducible metal oxide catalysts. MoO3‑based catalysts have demonstrated activity for selective HDO, but the underlying kinetic factors that control product distribution among propene, allyl alcohol, and 1‑propanol are not fully established. This task addresses that question by computing the full potential energy surface for acrolein conversion on a Mo3O9 cluster model of the MoO3 surface. The objective is to determine which of the three competing pathways is kinetically favored by evaluating the activation barriers and overall reaction free energies through first‑principles calculations.

## Approach
The reaction network is mapped using density functional theory (DFT) with the unrestricted B3LYP functional. The Mo atoms are described by the LANL2DZ effective core potential and basis set, while the 6‑31G(d,p) and 6‑311+G(d,p) basis sets are used for light atoms (H, C, O). A Mo3O9 cluster (three Mo atoms arranged in a ring with terminal and bridging oxygens) models the catalyst. The hydrogen‑rich defective state Mo3O8H (terminal oxygen vacancy with one surface hydroxyl) serves as the active site. Starting from Mo3O8H + acrolein + 2 H2, the mechanisms leading to propene, allyl alcohol, and 1‑propanol are explored by locating all stable intermediates and transition states. Geometry optimizations and frequency calculations are performed at the double‑ζ basis level, followed by single‑point energy refinements with the larger 6‑311+G(d,p) basis. Thermal corrections at 323 K and 1 atm are obtained from scaled harmonic frequencies to compute free energy barriers (ΔG‡323) and reaction free energies (ΔrG323). The entire workflow is executed with the open‑source ORCA quantum chemistry package and Python for data extraction.

## Reproduction target
Produce a JSON file containing the following nine quantities, all in kJ/mol and referenced to the Mo3O8H + acrolein + 2 H2 initial state:
- Classical activation energy (ΔE) and free energy barrier at 323 K (ΔG‡323) for TS2′ (propene pathway)
- Classical activation energy (ΔE) and free energy barrier at 323 K (ΔG‡323) for TS6 (allyl alcohol pathway)
- Classical activation energy (ΔE) and free energy barrier at 323 K (ΔG‡323) for TS8 (1‑propanol pathway)
- Overall reaction free energy at 323 K (ΔrG323) for the formation of propene, allyl alcohol, and 1‑propanol.
The file must be named computed_energies.json and placed at /app/outputs/computed_energies.json. The required keys are: TS2_prime_Delta_E, TS2_prime_Delta_G_323, TS6_Delta_E, TS6_Delta_G_323, TS8_Delta_E, TS8_Delta_G_323, Delta_r_G_propene, Delta_r_G_allyl_alcohol, Delta_r_G_1_propanol. All values are floating‑point numbers.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Python 3: python3

## Workflow steps

### Step 1: Build cluster models and optimize geometries
- Role: process
- Action: Construct the Mo3O9 cluster model and the defective Mo3O8H cluster (terminal oxygen vacancy with H at a terminal site). Optimize geometries at the UB3LYP/6-31G(d,p)/LANL2DZ level using ORCA.
- Evidence: `/app/outputs/cluster_geometries.xyz`

### Step 2: Optimise reaction intermediates and transition states
- Role: process
- Action: For the complete reaction scheme from Mo3O8H+acrolein+2H2 to propene, allyl alcohol and 1-propanol, optimise all stable intermediates and locate all transition states (TS4, TS2', TS5, TS6, TS7, TS8, TS9, TS10) at UB3LYP/6-31G(d,p)/LANL2DZ. Verify each transition state with a frequency calculation (one imaginary mode) and intrinsic reaction coordinate (IRC) calculations.
- Evidence: `/app/outputs/ts_irc_verification.log`

### Step 3: Single‑point energies and free energy corrections
- Role: process
- Action: Perform single point energy calculations at the UB3LYP/6-311+G(d,p)/LANL2DZ level for all optimised geometries. Compute zero‑point energy corrections and thermal corrections to the free energy at 323 K and 1 atm using scaled harmonic frequencies. Compile total energies and free energies relative to the Mo3O8H+acrolein+2H2 reference.
- Evidence: `/app/outputs/energy_table.csv`

### Step 4: Report activation barriers and reaction free energies
- Role: scored (load-bearing)
- Action: From the computed energy/free-energy data, extract the classical activation energies (ΔE) and free energy barriers at 323 K (ΔG‡323) for TS2', TS6 and TS8 relative to intermediate 10. Compute the overall reaction free energies (ΔrG323) for propene, allyl alcohol and 1-propanol formation relative to the Mo3O8H+acrolein+2H2 reference state. Write these values to computed_energies.json.
- Output file: `/app/outputs/computed_energies.json`
- Format: json
- Contract: JSON object with float keys: TS2_prime_Delta_E, TS2_prime_Delta_G_323, TS6_Delta_E, TS6_Delta_G_323, TS8_Delta_E, TS8_Delta_G_323, Delta_r_G_propene, Delta_r_G_allyl_alcohol, Delta_r_G_1_propanol. All values in kJ/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_energies.json
- path: `/app/outputs/computed_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The file contains the classical activation energies and free energy barriers for the three competing proton-transfer steps, as well as the overall reaction free energies for the three products.
- schema:
  - `type`: object
  - `required`: `TS2_prime_Delta_E`, `TS2_prime_Delta_G_323`, `TS6_Delta_E`, `TS6_Delta_G_323`, `TS8_Delta_E`, `TS8_Delta_G_323`, `Delta_r_G_propene`, `Delta_r_G_allyl_alcohol`, `Delta_r_G_1_propanol`
  - `properties`:
    - `TS2_prime_Delta_E`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS2_prime_Delta_G_323`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS6_Delta_E`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS6_Delta_G_323`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS8_Delta_E`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS8_Delta_G_323`:
      - `type`: number
      - `unit`: kJ/mol
    - `Delta_r_G_propene`:
      - `type`: number
      - `unit`: kJ/mol
    - `Delta_r_G_allyl_alcohol`:
      - `type`: number
      - `unit`: kJ/mol
    - `Delta_r_G_1_propanol`:
      - `type`: number
      - `unit`: kJ/mol

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "TS2_prime_Delta_E",
          "TS2_prime_Delta_G_323",
          "TS6_Delta_E",
          "TS6_Delta_G_323",
          "TS8_Delta_E",
          "TS8_Delta_G_323",
          "Delta_r_G_propene",
          "Delta_r_G_allyl_alcohol",
          "Delta_r_G_1_propanol"
        ],
        "properties": {
          "TS2_prime_Delta_E": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS2_prime_Delta_G_323": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS6_Delta_E": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS6_Delta_G_323": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS8_Delta_E": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS8_Delta_G_323": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "Delta_r_G_propene": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "Delta_r_G_allyl_alcohol": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "Delta_r_G_1_propanol": {
            "type": "number",
            "unit": "kJ/mol"
          }
        }
      },
      "description": "The file contains the classical activation energies and free energy barriers for the three competing proton-transfer steps, as well as the overall reaction free energies for the three products."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your computed_energies.json. It compares each reported barrier and free energy against reference values obtained from a complete DFT calculation at the specified level of theory. The comparison includes both quantitative agreement (within tolerances that account for differences between DFT codes and numerical settings) and a qualitative check: the allyl alcohol barrier (TS6) must be the lowest among the three competing steps, and the 1‑propanol barrier (TS8) must be the highest. The verifier does not require bit‑exact reproduction, but significant deviations from the reference values will lower the reward. Your final score is the fraction of the evaluated criteria that are satisfied.
