# Phonon Mode Classification of Graphene Nanoribbons from DFT Calculations

## Problem background
Graphene nanoribbons (GNRs) are quasi-one-dimensional nanostructures formed by cutting strips from a graphene sheet. Their confinement perpendicular to the ribbon axis leads to quantised phonon wavevectors, and the resulting vibrational modes can be interpreted as six fundamental oscillations (matching graphene’s Γ‑point phonons) plus a series of overtones that arise from transverse quantisation. The task is to compute these Γ‑point phonon modes for representative armchair and zigzag nanoribbons, classify them into fundamentals, overtones, and edge‑termination (C–H) modes, and map the ribbon overtones onto the phonon dispersion of graphene by “unfolding” the ribbon Brillouin zone. The outcome characterises width‑dependent phonon behaviour and provides a numerical dataset that allows verification of the zone‑folding relationship.

## Approach
The reproduction uses density‑functional theory (DFT) with the open‑source SIESTA code. Troullier‑Martins pseudopotentials are generated for carbon and hydrogen, and a double‑ζ plus polarisation (DZP) basis set is employed. The pipeline is: (i) relax the atomic positions and lattice constants for selected nanoribbons (7‑AGNR, 15‑AGNR, 4‑ZGNR, 12‑ZGNR); (ii) compute the full phonon dispersion of a periodic graphene sheet along Γ–M and Γ–K, scaling all frequencies so that the experimental E₂g mode lies at 1580 cm⁻¹; (iii) perform finite‑displacement phonon calculations at the Γ point for each relaxed ribbon, applying the same frequency scaling; and (iv) for every ribbon mode, classify the displacement pattern as a fundamental (k_perp = 0), an overtone (assign order n and compute k_perp = n π / w_ribbon), or a C–H mode, and assemble a single CSV table that also includes the graphene dispersion points. The internal consistency between the ribbon overtones and the self‑computed graphene dispersion provides the main quantitative check.

## Reproduction target
Produce the scored file `phonon_data.csv`. This CSV must contain: (a) rows for the graphene phonon dispersion along Γ–M and Γ–K, and (b) rows for every Γ‑point phonon mode of the four ribbons (7‑AGNR, 15‑AGNR, 4‑ZGNR, 12‑ZGNR), classified into fundamentals (k_perp = 0), overtones (with order n and k_perp = n π / w_ribbon), and C–H modes. The columns are `system`, `k_perp` (1/Å), `mode_label`, and `frequency` (cm⁻¹). The verifier will independently recompute the LO‑TO splitting for armchair ribbons and the root‑mean‑square deviation between overtone frequencies and your graphene dispersion at the corresponding k_perp, and will check that C–H modes fall in plausible frequency windows.

## Assets

- SIESTA DFT code: https://departments.icmab.es/leem/siesta/

## Workflow steps

### Step 1: DFT geometry relaxation of selected GNRs
- Role: process
- Action: Relax the atomic positions and lattice constants for hydrogen‑passivated 7‑AGNR, 15‑AGNR, 4‑ZGNR, and 12‑ZGNR nanoribbons using SIESTA with Troullier‑Martins pseudopotentials (core radii: C 2s²(1.49), 2p²(1.50); H 1s¹(1.25)), a DZP basis set, and standard converged parameters. Ensure residual forces on each atom are <0.01 eV/Å. Save the relaxed lattice constants and atomic coordinates.
- Evidence: `/app/outputs/relaxation_details.txt`

### Step 2: Compute graphene reference phonon dispersion
- Role: process
- Action: Using DFPT or finite‑displacement method with a supercell (e.g., 9×9×1) in SIESTA, compute the phonon dispersion of a periodic graphene sheet along the Γ–M and Γ–K high‑symmetry directions. Scale all computed frequencies by a constant factor such that the E₂g Raman‑active mode at Γ equals 1580 cm⁻¹ (the known experimental value).
- Evidence: `/app/outputs/graphene_dispersion.txt`

### Step 3: Compute Γ‑point phonon frequencies for ribbons
- Role: process
- Action: For each relaxed nanoribbon (7‑AGNR, 15‑AGNR, 4‑ZGNR, 12‑ZGNR) run a finite‑displacement phonon calculation at the Γ point using SIESTA in non‑spin‑polarized mode. Apply the same frequency‑scaling factor derived from the graphene E₂g mode.
- Evidence: `/app/outputs/ribbon_phonon_raw.txt`

### Step 4: Classify modes and assemble phonon‑data table
- Role: scored (load-bearing)
- Action: From the graphene dispersion and the ribbon Γ‑point phonon eigenvectors, classify each ribbon mode as a fundamental oscillation (k_perp=0), an overtone (assign order n and compute k_perp = nπ/w_ribbon), or a C–H mode. Assemble a single CSV file `phonon_data.csv` that contains: (i) for graphene, the dispersion points along Γ–M and Γ–K, and (ii) for every ribbon, all Γ‑point modes with their classification. Columns: system (e.g., 'graphene','7‑AGNR','4‑ZGNR'), k_perp (float, 1/Å, set to 0 for fundamentals), mode_label (string, e.g., 'LO','TO','ZO','LA','TA','ZA','C‑H', with overtone prefix like '1‑LO'), frequency (float, cm⁻¹). At least six rows for graphene and all 3m rows for each ribbon must be present; overtones must go up to order n=N‑1 for each fundamental of the largest ribbon studied.
- Output file: `/app/outputs/phonon_data.csv`
- Format: csv
- Contract: Columns: system (string), k_perp (float, 1/Å; 0 for fundamentals), mode_label (string), frequency (float, cm⁻¹). Include graphene rows along Γ–M and Γ–K; ribbon rows must have all fundamentals and overtones up to order N−1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_data.csv
- path: `/app/outputs/phonon_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Phonon frequencies for graphene reference dispersion and for Γ‑point modes of armchair and zigzag graphene nanoribbons, classified into fundamentals (k_perp=0), overtones (order n with k_perp = n·π/w_ribbon), and C–H modes. The checker will extract fundamental frequencies to compute LO‑TO splitting, map overtones onto the agent‑supplied graphene dispersion and compute RMSE, and verify that C–H modes lie in expected frequency windows.
- schema:
  - `type`: table
  - `required_columns`: `system`, `k_perp`, `mode_label`, `frequency`
  - `units`:
    - `k_perp`: 1/Å
    - `frequency`: cm⁻¹

Notes: The agent must use the same Troullier‑Martins pseudopotential core radii and DZP basis as the paper, but does not need to reproduce the full set of 30+ nanoribbon widths; a representative subset (7‑AGNR, 15‑AGNR, 4‑ZGNR, 12‑ZGNR) suffices. Spin‑polarised calculations are not required as their effect on phonon frequencies is negligible. The checker will compare recomputed LO‑TO splitting and overtone RMSE against paper‑reported values with generous tolerances that account for toolchain variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "k_perp",
          "mode_label",
          "frequency"
        ],
        "units": {
          "k_perp": "1/Å",
          "frequency": "cm⁻¹"
        }
      },
      "description": "Phonon frequencies for graphene reference dispersion and for Γ‑point modes of armchair and zigzag graphene nanoribbons, classified into fundamentals (k_perp=0), overtones (order n with k_perp = n·π/w_ribbon), and C–H modes. The checker will extract fundamental frequencies to compute LO‑TO splitting, map overtones onto the agent‑supplied graphene dispersion and compute RMSE, and verify that C–H modes lie in expected frequency windows."
    }
  ],
  "notes": "The agent must use the same Troullier‑Martins pseudopotential core radii and DZP basis as the paper, but does not need to reproduce the full set of 30+ nanoribbon widths; a representative subset (7‑AGNR, 15‑AGNR, 4‑ZGNR, 12‑ZGNR) suffices. Spin‑polarised calculations are not required as their effect on phonon frequencies is negligible. The checker will compare recomputed LO‑TO splitting and overtone RMSE against paper‑reported values with generous tolerances that account for toolchain variations."
}
```

## How you are scored
A hidden verifier inspects your submitted artifacts. For the scored artifact `phonon_data.csv`, it extracts fundamental modes, computes the LO‑TO splitting for each armchair ribbon, maps each ribbon’s overtones onto the graphene dispersion points you supplied, and computes the root‑mean‑square deviation (RMSE) between overtone frequencies and the graphene phonon branches at the assigned k_perp values. These derived quantities are compared against reference values from the original study. Additional structural checks verify that C–H modes lie in expected frequency intervals and that the correct number of modes is present. The overall reward is a weighted combination of these checks, with the largest weight on the LO‑TO splitting and the overtone‑to‑graphene RMSE. Simply reporting numbers without performing the DFT calculations will not produce a meaningful score because the verifier recomputes metrics from your CSV and cross‑checks internal consistency with your own graphene dispersion.
