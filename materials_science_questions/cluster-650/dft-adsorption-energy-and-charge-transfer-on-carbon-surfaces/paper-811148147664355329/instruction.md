# DFT Adsorption Energies and Charge Transfer of CO, NO, and HCN on C54Si6 Heterofullerene Isomers

## Problem background
The detection of toxic gases such as CO, NO, and HCN is important for environmental monitoring, industrial safety, and public health. Nanocluster-based gas sensors offer high surface-area-to-volume ratios and tunable electronic properties. This work investigates the adsorption of CO, NO, and HCN molecules on C54Si6 heterofullerene—a silicon-doped C60 cage that exists in two stable isomers (isomer-1 and isomer-2). Using density functional theory (DFT), the study computes adsorption energies, Hirshfeld charge transfers, and HOMO-LUMO gaps for the most stable molecule–heterofullerene complexes. These quantities determine whether chemisorption occurs and how the electronic properties change upon adsorption, which in turn indicates the potential of each isomer as a gas sensor material. The open scientific question is to compute these properties for all relevant adsorption configurations and assess the sensing behaviour of both isomers.

## Approach
The method uses spin-unrestricted density functional theory with a generalized gradient approximation (GGA) functional of the Becke–Perdew type and a double-zeta plus polarization basis set. For each system (pristine isomer, isolated gas molecule, and molecule–heterofullerene complex), a full geometry optimization is performed without symmetry constraints, followed by vibrational analysis to confirm that the obtained stationary points are true minima. Total energies, Hirshfeld population charges, and HOMO-LUMO gaps are extracted for the optimized structures. The adsorption energy is defined as E_ads = E(complex) – E(isomer) – E(molecule). For each molecule and isomer combination, multiple initial adsorption sites (top of Si, top of C, bridge/bond centres) are explored, and the one or two lowest-energy configurations are retained for final property calculations. The overall workflow therefore requires reference calculations on the clean isomers and isolated molecules, followed by exploration and optimization of the adsorbed complexes, and finally the extraction of the physical quantities of interest.

## Reproduction target
The objective is to compute the adsorption energy (E_ads, in eV), HOMO-LUMO gap (E_g, in eV), and Hirshfeld net charge on the adsorbed molecule (charge_transfer, in e, positive meaning net transfer from molecule to heterofullerene) for the most stable configurations of CO, NO, and HCN on both isomer-1 and isomer-2 of C54Si6. For isomer-1, this includes the two most stable CO configurations, the three most stable NO configurations, and the two most stable HCN configurations. For isomer-2, it includes the most stable CO configuration, the two most stable NO configurations, and the most stable HCN configuration. All computed results must be reported in a single CSV file (`/app/outputs/results_table.csv`) with columns: `system` (string, e.g. isomer1_CO_A), `E_ads` (float, eV), `E_g` (float, eV), `charge_transfer` (float, e). The workflow steps below detail the intermediate calculations and the final property extraction.

## Assets

- C54Si6 isomer-1 initial structure
- C54Si6 isomer-2 initial structure
- Open-source DFT package with GGA and Hirshfeld analysis: https://www.cp2k.org

## Workflow steps

### Step 1: Optimize pristine C54Si6 isomers
- Role: process
- Action: Perform DFT geometry optimization for both isomer-1 and isomer-2 of C54Si6 using the provided XYZ structures. Compute total energies and HOMO-LUMO gaps of the optimized isomers.
- Evidence: `/app/outputs/isomer_energies.json`

### Step 2: Optimize isolated gas molecules
- Role: process
- Action: Perform DFT geometry optimization for CO, NO, and HCN molecules separately. Compute total energies of the isolated optimized molecules.
- Evidence: `/app/outputs/molecule_energies.json`

### Step 3: Adsorption complex geometry optimizations
- Role: process
- Action: For each combination of molecule (CO, NO, HCN) and isomer (1 and 2), place the molecule at representative initial sites (top of Si, top of C, bridge/bond centers). Perform full geometry optimizations with no symmetry constraints, using standard DFT convergence criteria. Perform vibrational analysis to confirm no imaginary frequencies. Retain the one or two most stable configurations per system: for isomer-1, CO-A and CO-B, NO-A, NO-B, NO-C, HCN-A and HCN-B; for isomer-2, CO-A, NO-A and NO-B, HCN-B (or the most stable ones found).
- Evidence: `/app/outputs/complex_structures.log`

### Step 4: Compute adsorption energies, charge transfer, and gaps
- Role: scored (load-bearing)
- Action: For each stable complex from step 3, compute adsorption energy E_ads = E(complex) - E(isomer) - E(molecule) using the total energies from steps 1 and 2. Perform Hirshfeld population analysis to obtain the net charge on the adsorbed molecule (positive means charge transferred from molecule to heterofullerene). Extract the HOMO-LUMO gap of the complex. Write all results to a CSV file.
- Output file: `/app/outputs/results_table.csv`
- Format: csv
- Contract: Columns: system (string, e.g., isomer1_CO_A), E_ads (float, eV), E_g (float, eV), charge_transfer (float, e).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_table.csv
- path: `/app/outputs/results_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies, HOMO-LUMO gaps, and Hirshfeld charge transfers for each stable configuration. Each row corresponds to a specific complex (e.g., isomer1_CO_A, isomer1_NO_A, isomer2_CO_A). Charge transfer sign: positive means net transfer from molecule to heterofullerene.
- schema:
  - `type`: table
  - `required_columns`: `system`, `E_ads`, `E_g`, `charge_transfer`
  - `units`:
    - `E_ads`: eV
    - `E_g`: eV
    - `charge_transfer`: e

Notes: The checker compares the reported values against reference data and checks qualitative trends (relative ordering of adsorption energies among systems).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "E_ads",
          "E_g",
          "charge_transfer"
        ],
        "units": {
          "E_ads": "eV",
          "E_g": "eV",
          "charge_transfer": "e"
        }
      },
      "description": "Adsorption energies, HOMO-LUMO gaps, and Hirshfeld charge transfers for each stable configuration. Each row corresponds to a specific complex (e.g., isomer1_CO_A, isomer1_NO_A, isomer2_CO_A). Charge transfer sign: positive means net transfer from molecule to heterofullerene."
    }
  ],
  "notes": "The checker compares the reported values against reference data and checks qualitative trends (relative ordering of adsorption energies among systems)."
}
```

## How you are scored
A hidden verifier independently scores your submission. The verifier reads the final results table (`results_table.csv`) as well as any required intermediate evidence. It compares your computed adsorption energies, HOMO-LUMO gaps, and charge transfers for each system against reference values with appropriate tolerances. It also checks that the relative ordering of adsorption energies across the different molecules (e.g., which molecule binds most strongly) matches the expected qualitative trend. Additional checks verify that the required process steps (geometry optimizations, reference calculations) have been executed and that the outputs are consistent. Each workflow stage carries a weight, and the final score is a weighted combination of these checks. Producing numerically accurate and self-consistent results across all required systems is essential to obtain a high score.
