# FLAPW dHvA Frequency Calculation for LaNi₂Al₅

## Problem background
LaNi₂Al₅ crystallizes in an orthorhombic body-centred structure (space group Immm) and serves as a non-magnetic reference material for the isostructural dense-Kondo system CeNi₂Al₅. Understanding its Fermi surface topology and the associated de Haas–van Alphen (dHvA) frequencies through first-principles FLAPW band-structure calculations is essential for interpreting the electronic structure and for later comparison with the 4f-electron compound. This task requires you to compute the extremal cross-sectional areas of the Fermi surface, expressed as dHvA frequencies (in 10⁶ Oe), and the corresponding cyclotron effective masses (in units of the free-electron mass m₀) for specific magnetic-field directions. The computed quantities can then be compared with experimental measurements.

## Approach
The reproduction uses an all-electron full-potential linearized augmented plane-wave (FLAPW) method as implemented in the Elk code (an equivalent open-source FLAPW implementation may be used). The conceptual workflow is:

1. Construct the DFT input for LaNi₂Al₅ from the reported crystal structure (lattice constants, space group, atomic positions) and set standard FLAPW parameters, including muffin-tin radii and the local-density approximation (LDA) exchange-correlation functional.

2. Perform a self-consistent field (SCF) calculation on a moderate k-point mesh to obtain a converged ground-state charge density and Kohn–Sham potential.

3. Perform a non-self-consistent band-structure calculation on a denser k-point mesh, using the converged potential, to obtain the Kohn–Sham eigenvalues on a grid suitable for Fermi surface analysis. Identify which bands cross the Fermi level.

4. Using an extremal-orbit finder (e.g., SKEAF, or an equivalent tool), extract the extremal cross-sectional areas from the eigenvalues. Convert these areas to dHvA frequencies (10⁶ Oe) and compute the cyclotron effective masses (m₀) for the following six orbits:
   - Field direction H ∥ b: branches δ, ε, ζ.
   - Field direction H ∥ 15° from b to a in the (100) plane: branches α, β, δ.

Write the six computed entries to the output CSV file. The mass-enhancement effects are implicitly included in the computed effective masses.

## Reproduction target
Produce a CSV file named `dHvA_frequencies.csv` with the header `branch,direction,frequency_calc,mass_calc` and exactly six data rows. The required entries are:

- For direction `'H∥b'`: branches `'δ'`, `'ε'`, `'ζ'`.
- For direction `'H∥15° from b to a'`: branches `'α'`, `'β'`, `'δ'`.

Within each direction the rows must appear in strictly increasing order of `frequency_calc`. Units: frequencies in 10⁶ Oe, masses in m₀ (free-electron mass). These six entries constitute the reproduction target and will be evaluated by the hidden checker.

## Assets

- Elk FLAPW code: https://elk.sourceforge.net
- SKEAF extremal orbit finder: skeaf
- Crystal structure of LaNi₂Al₅

## Workflow steps

### Step 1: Crystal structure and DFT parameter setup
- Role: process
- Action: Create input files for the Elk FLAPW code using the crystal structure of LaNi₂Al₅. Set space group Immm, lattice constants, atomic positions, muffin-tin radii (0.2870a for La, 0.1534a for Ni and Al), LDA exchange-correlation (Gunnarsson-Lundqvist), and k-point grids for self-consistency (equivalent to 61 irreducible k-points) and final band structure (353 irreducible k-points).
- Evidence: none

### Step 2: Self‑consistent field calculation
- Role: process
- Action: Run the Elk self-consistent field calculation to obtain a converged ground‑state charge density and Kohn–Sham potential. Ensure convergence sufficient for accurate Fermi surface analysis.
- Evidence: `/app/outputs/scf.log`

### Step 3: Fine k‑mesh non‑self‑consistent band calculation
- Role: process
- Action: Perform a non‑self‑consistent calculation on the fine k‑mesh (353 irreducible k‑points) using the converged potential from step02. Output the Kohn–Sham eigenvalues on the k‑mesh for subsequent Fermi surface analysis. Identify which bands cross the Fermi level.
- Evidence: `/app/outputs/eigenvalues.dat`

### Step 4: Extract dHvA frequencies and cyclotron masses
- Role: scored (load-bearing)
- Action: Using the eigenvalues from step03, run a tool (e.g., SKEAF) to compute extremal cross-sectional areas (dHvA frequencies) and cyclotron effective masses. Determine frequencies (unit: 10⁶ Oe) and masses (unit: m₀) for these six orbits: field direction H∥b → branches δ, ε, ζ; field direction H∥15° from b to a in the (100) plane → branches α, β, δ. Write the results to a CSV file with columns: branch, direction, frequency_calc, mass_calc. Rows for each direction must be ordered by increasing frequency.
- Output file: `/app/outputs/dHvA_frequencies.csv`
- Format: csv
- Contract: CSV file with header row: branch (string), direction (string), frequency_calc (float, 10⁶ Oe), mass_calc (float, m₀). Six rows corresponding to the required branches and directions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dHvA_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dHvA_frequencies.csv
- path: `/app/outputs/dHvA_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the six required dHvA frequency and mass entries, compared against the paper's Table I experimental values.
- schema:
  - `type`: table
  - `required_columns`: `branch`, `direction`, `frequency_calc`, `mass_calc`
  - `units`:
    - `frequency_calc`: 10^6 Oe
    - `mass_calc`: m0

Notes: The checker compares each frequency_calc and mass_calc to hidden gold values with tolerances and verifies ordering within each direction group. Only these six entries are scored; other measured branches are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dHvA_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "branch",
          "direction",
          "frequency_calc",
          "mass_calc"
        ],
        "units": {
          "frequency_calc": "10^6 Oe",
          "mass_calc": "m0"
        }
      },
      "description": "CSV containing the six required dHvA frequency and mass entries, compared against the paper's Table I experimental values."
    }
  ],
  "notes": "The checker compares each frequency_calc and mass_calc to hidden gold values with tolerances and verifies ordering within each direction group. Only these six entries are scored; other measured branches are not required."
}
```

## How you are scored
A hidden verifier reads your `dHvA_frequencies.csv` and compares each entry to a set of reference values (derived from the paper's experimental dHvA data) that are not disclosed to you. The verifier checks two aspects:

1. **Numeric accuracy** of the computed frequencies and masses relative to the hidden references.
2. **Ordering correctness**: within each field direction, the branches must appear in strictly increasing order of frequency.

The final reward is a weighted combination: frequency accuracy carries most of the weight, mass accuracy a smaller share, and an ordering-correctness factor multiplies the score. To obtain a high score you must genuinely execute the described DFT workflow and extract the quantities; simply reporting numbers that "look plausible" will not pass the ordering and accuracy checks.
