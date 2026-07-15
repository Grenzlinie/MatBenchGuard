# Magnetic moments of V and Ti impurities in MoTe₂ from DFT

## Problem background
2H‑MoTe₂ is a layered transition‑metal dichalcogenide with potential for dilute magnetic semiconductor applications. Introducing transition‑metal impurities can induce magnetic ordering, but the magnetic activity depends strongly on both the impurity element and its atomic configuration. Understanding which impurity sites carry a magnetic moment – and which do not – is essential to explain whether doping can produce ferromagnetism and to assign the atomic‑scale defect structures.

## Approach
Use spin‑polarised density functional theory (DFT) within the plane‑wave framework and the PBE exchange‑correlation functional. Construct a supercell of bulk 2H‑MoTe₂ and embed a single impurity atom – vanadium or titanium – in each of four distinct charge‑neutral configurations: an adatom on the surface, an interstitial in the van der Waals gap, a substitutional at a tellurium site, or a substitutional at a molybdenum site. Relax the atomic positions (keeping the supercell fixed) and record the total magnetic moment of the supercell. By computing the moments for all eight configurations, you can compare the magnetic fingerprints of vanadium and titanium impurities and determine which configurations lead to a non‑zero net moment.

## Reproduction target
Compute, using the approach above, the total magnetic moment (in µB per supercell) for each of the following impurity configurations in a 2H‑MoTe₂ supercell:

- V adatom
- V interstitial
- V substitutional at Te site
- V substitutional at Mo site
- Ti adatom
- Ti interstitial
- Ti substitutional at Te site
- Ti substitutional at Mo site

Write the results to `/app/outputs/magnetic_moments.csv`, a CSV file with header `element,configuration,magnetic_moment` and one row per configuration (8 rows). The `magnetic_moment` column holds a positive floating‑point value (unit µB).

## Assets

- Quantum ESPRESSO (plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE, Mo, Te, V, Ti): https://www.materialscloud.org/discover/sssp/table/efficiency
- Bulk 2H-MoTe₂ crystal structure: https://materialsproject.org/materials/mp-602/

## Workflow steps

### Step 1: Build MoTe₂ supercells with V and Ti impurity configurations
- Role: process
- Action: Construct a supercell of 2H-MoTe₂ (e.g., 4×4×1) and generate atomic structures for eight charge-neutral defect configurations: V adatom on the surface, V in an interstitial van der Waals site, V substitutional at a Te site, V substitutional at a Mo site, and the same four configurations with Ti. Use reasonable starting coordinates based on the relaxed bulk lattice.
- Evidence: none

### Step 2: Spin-polarized DFT calculation of magnetic moments
- Role: scored (load-bearing)
- Action: For each of the eight defect supercells, perform a spin-polarized DFT calculation using a plane-wave code (e.g., Quantum ESPRESSO) with the PBE functional and standard pseudopotentials. Relax the atomic positions (cell fixed) and obtain the total magnetic moment of the supercell (in μB/cell). Collect the results into a single CSV file at /app/outputs/magnetic_moments.csv with columns: element (V or Ti), configuration (adatom, interstitial, Te_site, Mo_site), magnetic_moment (float, unit μB).
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: CSV with header: element,configuration,magnetic_moment. One row per defect (8 rows). Values are floats in μB.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Magnetic moments of V and Ti impurities; the hidden checker compares each row’s value against the paper’s reference using threshold_or_better scoring.
- schema:
  - `type`: table
  - `required_columns`: `element`, `configuration`, `magnetic_moment`
  - `units`:
    - `magnetic_moment`: muB

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "configuration",
          "magnetic_moment"
        ],
        "units": {
          "magnetic_moment": "muB"
        }
      },
      "description": "Magnetic moments of V and Ti impurities; the hidden checker compares each row’s value against the paper’s reference using threshold_or_better scoring."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `magnetic_moments.csv` and scores each row independently against reference values using a threshold‑or‑better policy. Configurations that are expected to be magnetic are rewarded when the reported moment meets or exceeds a threshold, while non‑magnetic configurations are rewarded when the reported moment stays below a tolerance. Deviations beyond those tolerances reduce the per‑row score linearly to zero, and sign violations (non‑zero on a non‑magnetic configuration, or zero on a magnetic configuration) are penalised. The overall reward is the average over all eight configurations. The exact tolerances and reference values are not disclosed; the task is to produce a faithful reproduction of the physical moments.
