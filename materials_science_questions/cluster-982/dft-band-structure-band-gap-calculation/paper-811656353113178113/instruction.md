# TlGaSe2 DFT Band Structure and Effective Mass Ordering

## Problem background
TlGaSe₂ is a wide-band-gap semiconductor that has drawn interest for room‑temperature X‑ray and γ‑ray detection. First‑principles electronic structure calculations are a key tool for predicting its band gap and the effective masses of charge carriers, quantities that directly influence detector performance. This task reproduces the density functional theory (DFT) band structure calculation to assess these properties.

## Approach
The approach is a DFT band‑structure calculation for monoclinic TlGaSe₂ (space group C2/c, experimental lattice parameters: a = 10.77 Å, b = 10.77 Å, c = 15.63 Å, β = 100.06°). We use a hybrid exchange–correlation functional (e.g., HSE06 or an equivalent screened hybrid) together with spin–orbit coupling to capture the heavy‑element relativistic effects and obtain a band gap close to experiment. A self‑consistent field calculation is followed by a non‑self‑consistent band structure run along a high‑symmetry k‑path that includes Γ, Y, and other Brillouin zone points. From the raw band energies we locate the valence band maximum (expected at Γ) and the conduction band minimum (expected along Γ–Y), then compute the indirect gap, the direct gap at Γ, and the effective masses near the band edges. The raw energies are saved as band_structure.csv, and the extracted quantities are written to results.json.

## Reproduction target
Using the published crystal structure of TlGaSe₂ (monoclinic C2/c, lattice parameters above, atomic coordinates obtainable from public crystallographic databases or the supplementary information of the original study), perform a DFT band‑structure calculation with an open‑source code that supports hybrid functionals and spin–orbit coupling (Quantum ESPRESSO is a suitable choice).

1. Compute the electronic band energies along a high‑symmetry k‑path that includes Γ and Y (e.g., Γ–Y, Γ–X, Y–Z, etc.) and save them to `/app/outputs/band_structure.csv` with columns: kx, ky, kz (reciprocal lattice units), band_index (int, 0 for lowest conduction band, ‑1 for highest valence band, …), energy (eV, referenced to Fermi level at 0 eV).

2. From that CSV, extract the indirect band gap (VBM at Γ, CBM along Γ–Y) and the direct band gap at Γ, and evaluate the effective masses near the band edges to decide which carrier (hole or electron) has the lighter effective mass. Write these three results to `/app/outputs/results.json` as a JSON object with keys: indirect_gap (float, eV), direct_gap_at_Gamma (float, eV), effective_mass_ordering (string: 'hole_lighter_than_electron', 'electron_lighter_than_hole', or 'comparable').

## Assets

- TlGaSe2 crystal structure: 10.1021/cm200946y
- Open-source DFT code with hybrid functional and spin–orbit coupling: https://www.quantum-espresso.org
- Pseudopotentials for Tl, Ga, Se with spin–orbit coupling: http://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Prepare crystal structure input
- Role: process
- Action: Download the TlGaSe2 crystal structure from the paper's supplementary CIF or a public database and create an input file for the chosen DFT code with the correct symmetry and an initial set of k-points.
- Evidence: none

### Step 2: Compute DFT band structure
- Role: scored (load-bearing)
- Action: Run a self-consistent field calculation followed by a non-self-consistent band structure calculation for TlGaSe2 along a high-symmetry k-path that includes Γ, Y, and other directions of the Brillouin zone. Use spin–orbit coupling and a screened-exchange hybrid functional (or an equivalent hybrid functional that yields a similar band gap). Write the band energies along the path to band_structure.csv.
- Output file: `/app/outputs/band_structure.csv`
- Format: csv
- Contract: CSV with columns: kx (float), ky (float), kz (float) in reciprocal lattice units; band_index (int, 0 for lowest conduction band, -1 for highest valence band, etc.); energy (float, eV, referenced to the Fermi level at 0 eV).
- Scoring: scored by hidden verifier

### Step 3: Extract band gaps and effective mass ordering
- Role: scored
- Action: From the computed band structure in band_structure.csv, determine the indirect band gap as the energy difference between the conduction band minimum and valence band maximum (VBM at Γ, CBM along Γ-Y). Compute the direct band gap at the Γ point. Evaluate the effective masses of electrons and holes near the respective band edges and decide which carrier has the lighter effective mass. Output the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: indirect_gap (float, eV), direct_gap_at_Gamma (float, eV), effective_mass_ordering (string: 'hole_lighter_than_electron', 'electron_lighter_than_hole', or 'comparable').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure.csv
- path: `/app/outputs/band_structure.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw band energies along high-symmetry k-point paths. The hidden checker recomputes the indirect and direct band gaps from these data.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `kz`, `band_index`, `energy`
  - `units`:
    - `kx`: reciprocal lattice unit
    - `ky`: reciprocal lattice unit
    - `kz`: reciprocal lattice unit
    - `energy`: eV

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent-reported band gaps and effective mass ordering. The checker verifies the gaps by recomputing from band_structure.csv and checks the ordering claim against band curvature analysis.
- schema:
  - `type`: object
  - `required`: `indirect_gap`, `direct_gap_at_Gamma`, `effective_mass_ordering`
  - `items`:
    - `indirect_gap`: float (eV)
    - `direct_gap_at_Gamma`: float (eV)
    - `effective_mass_ordering`: string ('hole_lighter_than_electron', 'electron_lighter_than_hole', or 'comparable')

Notes: Scoring is based on recomputation of the band gaps from the raw band_structure.csv and on verification of the effective mass ordering via band curvature. No gold values are provided in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "kz",
          "band_index",
          "energy"
        ],
        "units": {
          "kx": "reciprocal lattice unit",
          "ky": "reciprocal lattice unit",
          "kz": "reciprocal lattice unit",
          "energy": "eV"
        }
      },
      "description": "Raw band energies along high-symmetry k-point paths. The hidden checker recomputes the indirect and direct band gaps from these data."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "indirect_gap",
          "direct_gap_at_Gamma",
          "effective_mass_ordering"
        ],
        "items": {
          "indirect_gap": "float (eV)",
          "direct_gap_at_Gamma": "float (eV)",
          "effective_mass_ordering": "string ('hole_lighter_than_electron', 'electron_lighter_than_hole', or 'comparable')"
        }
      },
      "description": "Agent-reported band gaps and effective mass ordering. The checker verifies the gaps by recomputing from band_structure.csv and checks the ordering claim against band curvature analysis."
    }
  ],
  "notes": "Scoring is based on recomputation of the band gaps from the raw band_structure.csv and on verification of the effective mass ordering via band curvature. No gold values are provided in this contract."
}
```

## How you are scored
A hidden verifier inspects your two output files. From `band_structure.csv`, the verifier recomputes the indirect and direct band gaps using the same k‑point definitions described in the workflow and compares them to reference expectations; it also checks that the conduction band minimum is not at Γ (consistent with the indirect‑gap character). For effective mass ordering, the verifier performs its own curvature analysis on the CSV band edges and cross‑checks the result with your `results.json` ordering claim. Each component (indirect gap, direct gap at Γ, effective mass ordering, structural correctness) carries a share of the total reward. Merely quoting published numbers without the required computed artifacts will not pass.
