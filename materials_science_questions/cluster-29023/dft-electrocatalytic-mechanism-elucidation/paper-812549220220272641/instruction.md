# DFT Adsorption and TD-DFT Hole-Electron Analysis of PtCl6^2- on Covalent Organic Framework Models

## Problem background
Covalent organic frameworks (COFs) have emerged as promising photocatalysts for hydrogen production, but efficient use of platinum co‑catalysts depends on achieving uniform and well‑dispersed deposition. The initial adsorption of the Pt precursor (PtCl6^2-) onto the COF structure governs the subsequent photodeposition, yet the thermodynamic preference for different binding motifs is not obvious from the chemical structure alone. This task uses density functional theory (DFT) and time‑dependent DFT (TD‑DFT) to compute the adsorption energy of PtCl6^2- on fragment models of three COFs — one containing adjacent hydroxyl and imine groups (PY‑DHBD‑COF), one with a bipyridine linkage (PY‑BPY‑COF), and a control without hydroxyl groups (PY‑BP‑COF) — and to quantify the spatial separation of photogenerated electrons and holes in each fragment's first excited state.

## Approach
The computational strategy has two parts. (I) DFT ground‑state calculations are performed with the B3LYP functional, Grimme's D3 dispersion correction, and the 6‑31G(d) basis set, using the Stuttgart/Dresden (SDD) effective‑core potential for Pt. After geometry optimizations of each bare fragment and of the fragment‑PtCl6^2- complexes at three distinct binding sites in implicit PCM water solvation, single‑point energies yield the adsorption energy ΔEads = E(complex) – E(fragment) – E(PtCl6^2-). (II) For each bare fragment a TD‑DFT calculation with the PBE0‑D3 functional is performed to obtain the S1 excited state, and the wavefunction is analyzed with Multiwfn's hole‑electron module, which returns the overlap integral S (a dimensionless measure of how much the electron and hole distributions coincide) and the centroid distance D (the spatial separation of their centers). The computed values are compared across the three fragments.

## Reproduction target
Produce the following two CSV files under `/app/outputs`:

1. `adsorption_energies.csv` with columns `Fragment`, `Site`, `DeltaE_ads_kcal_mol`. For each fragment (PY_DHBD_COF, PY_BPY_COF, PY_BP_COF), report the adsorption energy of PtCl6^2- at three different binding sites. The most negative (i.e., strongest binding) value for each fragment is the key outcome.

2. `hole_electron_metrics.csv` with columns `Fragment`, `State`, `S`, `D`. For each fragment, report the hole‑electron overlap integral S (dimensionless) and centroid distance D (in Ångströms) for the S1 excited state. All entries must be obtained by applying the computational protocol described in the Approach.

## Assets

- COF fragment coordinates
- ORCA quantum chemistry program: https://orcaforum.kofo.mpg.de/
- Multiwfn: http://sobereva.com/multiwfn/

## Workflow steps

### Step 1: Prepare fragment geometry input files
- Role: process
- Action: Convert the provided XYZ coordinates of PY-DHBD-COF, PY-BPY-COF, and PY-BP-COF into input files suitable for the quantum chemistry program (e.g., ORCA).
- Evidence: none

### Step 2: DFT geometry optimizations
- Role: process
- Action: Perform ground-state geometry optimizations for each fragment alone and for each fragment with PtCl6^2- adsorbed at three different binding sites, using B3LYP-D3/6-31G(d) (SDD for Pt) and PCM water solvation. Converge to tight energy and gradient thresholds.
- Evidence: `/app/outputs/optimizations.log`

### Step 3: Compute adsorption energies
- Role: scored
- Action: From the optimized geometries, perform single-point energy calculations and compute ΔE_ads = E(complex) - E(fragment) - E(PtCl6^2-) for each binding site. Report a CSV with columns Fragment, Site, DeltaE_ads_kcal_mol.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Columns: Fragment (string), Site (int), DeltaE_ads_kcal_mol (float).
- Scoring: scored by hidden verifier

### Step 4: Hole-electron overlap and distance for S1
- Role: scored
- Action: For each COF fragment (without Pt), perform a TD-DFT calculation at the PBE0-D3/6-31G(d) level to obtain the S1 excited state. Use Multiwfn to compute the hole-electron overlap integral S and centroid distance D. Output a CSV with columns Fragment, State, S, D.
- Output file: `/app/outputs/hole_electron_metrics.csv`
- Format: csv
- Contract: Columns: Fragment (string), State (string), S (float), D (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/hole_electron_metrics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Adsorption energies of PtCl6^2- on PY-DHBD-COF, PY-BPY-COF, and PY-BP-COF fragment models at three binding sites each. The row with the most negative DeltaE_ads per Fragment is the best site.
- schema:
  - `type`: table
  - `required_columns`: `Fragment`, `Site`, `DeltaE_ads_kcal_mol`
  - `units`:
    - `DeltaE_ads_kcal_mol`: kcal/mol

### hole_electron_metrics.csv
- path: `/app/outputs/hole_electron_metrics.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Hole-electron overlap integral S and centroid distance D for the S1 excited state of each COF fragment.
- schema:
  - `type`: table
  - `required_columns`: `Fragment`, `State`, `S`, `D`
  - `units`:
    - `S`: dimensionless
    - `D`: Angstrom

Notes: Scoring compares the most negative adsorption energy per fragment and the S/D values against hidden reference values. Meeting or exceeding the reference accuracy (i.e., more negative adsorption or stronger hole-electron separation) earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Fragment",
          "Site",
          "DeltaE_ads_kcal_mol"
        ],
        "units": {
          "DeltaE_ads_kcal_mol": "kcal/mol"
        }
      },
      "description": "Adsorption energies of PtCl6^2- on PY-DHBD-COF, PY-BPY-COF, and PY-BP-COF fragment models at three binding sites each. The row with the most negative DeltaE_ads per Fragment is the best site."
    },
    {
      "file": "hole_electron_metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Fragment",
          "State",
          "S",
          "D"
        ],
        "units": {
          "S": "dimensionless",
          "D": "Angstrom"
        }
      },
      "description": "Hole-electron overlap integral S and centroid distance D for the S1 excited state of each COF fragment."
    }
  ],
  "notes": "Scoring compares the most negative adsorption energy per fragment and the S/D values against hidden reference values. Meeting or exceeding the reference accuracy (i.e., more negative adsorption or stronger hole-electron separation) earns full credit."
}
```

## How you are scored
A hidden verifier evaluates your submission by comparing the values in your CSV files to a reference derived from the original study (the exact reference thresholds are not shown to you). From `adsorption_energies.csv`, the verifier extracts the most negative ΔEads for each fragment and compares it to the reference; if your value is as negative or more negative than the hidden threshold, you obtain full credit for that fragment, and less favorable values receive proportionally less credit. From `hole_electron_metrics.csv`, the verifier compares your S and D values for each fragment's S1 state to the hidden reference; tolerances are chosen to accommodate the spread expected when using different quantum‑chemistry programs (e.g., ORCA instead of the original publication's software). The final reward is a weighted combination of the adsorption‑energy and hole‑electron metric scores. Simply supplying the paper's tabulated numbers without running the prescribed pipeline will not yield a passing score.
