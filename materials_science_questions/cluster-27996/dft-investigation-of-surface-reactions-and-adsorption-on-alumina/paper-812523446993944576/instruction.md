# Reproduce CH₃O Radical Binding Energies on Hexagonal and Amorphous Water Ice

## Problem background
Interstellar chemistry models depend on accurate binding energies of radicals to icy grain surfaces. The methoxy (CH₃O) radical is a key intermediate in the formation of methanol and larger organic molecules on interstellar ices. However, binding energies vary with the local surface structure of ice — both hexagonal (Ih) and amorphous solid water (ASW). This task aims to compute the binding energies of CH₃O on a range of surface sites of Ih and ASW ice cluster models, using hybrid quantum-mechanics/molecular-mechanics (QM/MM) calculations, to capture the distribution of binding strengths expected under astrophysical conditions.

## Approach
The computation uses a two-layer ONIOM approach. The binding site and nearby water molecules are treated with density functional theory (DFT) at the wB97X-D/def2-TZVP level, while the surrounding ice is described by the AMBER molecular mechanics force field (mechanical embedding). Ice cluster models for Ih (sites A1–A16) and ASW (B1–B10) are built from published structural coordinates. The workflow involves geometry optimizations and harmonic vibrational frequency analysis for each isolated ice cluster, the isolated CH₃O radical, and each radical–ice complex. Binding energies are then derived from the total electronic energies and zero-point vibrational corrections. The calculations quantify how the binding energy varies across different surface structures (A1–A16 on Ih, B1–B10 on ASW).

## Reproduction target
Produce a CSV file named binding_energies.csv containing, for each of the 26 binding sites (A1–A16 and B1–B10), the computed binding energy without zero-point energy (ZPE) and the binding energy with harmonic ZPE, both in eV. The binding energies are to be derived from geometry-optimized structures and vibrational frequency analyses performed with an ONIOM(wB97X-D/def2-TZVP:AMBER) mechanical embedding protocol. The final CSV must include exactly 26 data rows and a header row with columns `site`, `binding_energy_without_zpe`, `binding_energy_with_zpe`.

## Assets

- Ice cluster model coordinates from Andersson et al. (2006): https://doi.org/10.1063/1.2162530
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- AMBER force field parameters: AmberTools

## Workflow steps

### Step 1: Prepare ice cluster models
- Role: process
- Action: Using the published ice cluster coordinates from Andersson et al. (JCP 2006), build the 26 QM/MM cluster models for I_h (A1-A16) and ASW (B1-B10). For I_h A1–A5 use 48 QM water molecules and 114 MM water molecules; A6–A8 use 44 QM, 112 MM; A9–A16 use the same QM/MM counts as A1 but with a vacancy obtained by removing one H₂O molecule from the top layer; for ASW B1–B10 use 49 QM and 113 MM water molecules. During all optimizations, freeze all atoms in the MM region. Create input files for isolated ice clusters, the isolated CH₃O radical, and each CH₃O-adsorbed complex.
- Evidence: none

### Step 2: Run ONIOM geometry optimizations and frequency calculations
- Role: process
- Action: For each of the 26 ice clusters, the isolated CH₃O radical, and the 26 radical-ice complexes, perform a two-layer ONIOM(wB97X-D/def2-TZVP:AMBER) geometry optimization with mechanical embedding, followed by harmonic vibrational frequency analysis. Save total energies and harmonic zero-point energies (ZPE) for every system.
- Evidence: none

### Step 3: Compute and output binding energies
- Role: scored (load-bearing)
- Action: For each binding site (A1-A16, B1-B10), compute the binding energy without ZPE as |E_complex - E_ice - E_radical| and the binding energy with ZPE as |(E_complex+ZPE_complex) - (E_ice+ZPE_ice) - (E_radical+ZPE_radical)|. Write the results to a CSV file.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: CSV with header: site, binding_energy_without_zpe (eV), binding_energy_with_zpe (eV). 26 rows for sites A1-A16 and B1-B10.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Per-site CH₃O radical binding energies computed from ONIOM(wB97X-D/def2-TZVP:AMBER) calculations. The checker recomputes the average and range and compares each site's energies against hidden reference values within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `site`, `binding_energy_without_zpe`, `binding_energy_with_zpe`
  - `units`:
    - `binding_energy_without_zpe`: eV
    - `binding_energy_with_zpe`: eV

Notes: The CSV must contain exactly 26 rows (sites A1–A16 and B1–B10). The checker will recompute the overall average binding energy (with ZPE) and range from the submitted values, in addition to per-site comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "binding_energy_without_zpe",
          "binding_energy_with_zpe"
        ],
        "units": {
          "binding_energy_without_zpe": "eV",
          "binding_energy_with_zpe": "eV"
        }
      },
      "description": "Per-site CH₃O radical binding energies computed from ONIOM(wB97X-D/def2-TZVP:AMBER) calculations. The checker recomputes the average and range and compares each site's energies against hidden reference values within a tolerance."
    }
  ],
  "notes": "The CSV must contain exactly 26 rows (sites A1–A16 and B1–B10). The checker will recompute the overall average binding energy (with ZPE) and range from the submitted values, in addition to per-site comparison."
}
```

## How you are scored
A hidden verifier reads your submitted binding_energies.csv. For each site, it compares your reported binding energies (with and without ZPE) to hidden reference values within specified tolerances. It also recomputes the overall average and range of your with-ZPE binding energies and checks them against hidden expected values. The verifier aggregates these per-site and aggregate scores into a single reward between 0 and 1. To succeed, your workflow must genuinely execute the ONIOM calculations; simply guessing or reporting values from another source will not pass the verifier's checks.
