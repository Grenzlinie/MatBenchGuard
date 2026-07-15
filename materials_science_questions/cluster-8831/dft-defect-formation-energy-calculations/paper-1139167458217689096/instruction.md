# High-throughput conventional Pourbaix diagram screening of 2D materials

## Problem background
Two-dimensional (2D) materials are promising for electrochemical applications, but their stability in aqueous environments under applied potential is a critical concern. The conventional Pourbaix diagram (CPD) provides a rapid thermodynamic screening method by evaluating the free energy of decomposition reactions. This task applies a large-scale CPD analysis to a set of thermodynamically stable monolayer candidates from the Computational 2D Materials Database (C2DB) to quantify their electrochemical stability at six pH–potential points relevant for the hydrogen evolution (HER) and oxygen evolution (OER) reactions. The goal is to determine the distribution of Pourbaix energies and how the fraction of stable materials varies across these conditions.

## Approach
The workflow uses the Atomic Simulation Environment (ASE) Pourbaix module together with solid-phase reference formation energies from the Open Quantum Materials Database (OQMD). First, all monolayer materials with a hull energy ΔH_hull < 50 meV/atom are retrieved from C2DB. For each material, ASE considers all possible electrochemical decomposition reactions, calculates the corresponding reaction free energy as a function of pH and applied potential (accounting for ionic activities set to 10⁻⁶ mol/L for all ions except H⁺), and extracts the Pourbaix energy ΔG_pbx as the negative of the minimum reaction free energy. This evaluation is performed at six preset pH–potential conditions (HER acidic, neutral, alkaline; OER acidic, neutral, alkaline). The per-material ΔG_pbx values are collected into a CSV file. From these values, aggregated statistics—the percentage of materials with ΔG_pbx < 0, the mean ΔG_pbx, and histogram distributions—are computed for each condition and stored in a JSON summary.

## Reproduction target
Compute the Pourbaix energy ΔG_pbx (eV/atom) for the 3376 C2DB monolayer materials with ΔH_hull < 50 meV/atom at the six specified pH–potential points using the ASE Pourbaix implementation with OQMD references. Output a per-material CSV file and a summary JSON file reporting, for each of the six electrochemical conditions, the fraction of materials with ΔG_pbx < 0, the mean ΔG_pbx, and histogram bin edges/counts (HER bins: 0–2 eV/atom, width 0.1; OER bins: 0–8 eV/atom, width 0.5). The output files must conform exactly to the contracts described in the output files section.

## Assets

- Computational 2D Materials Database (C2DB): https://www.c2db.dtu.dk
- Open Quantum Materials Database (OQMD): https://oqmd.org
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- surfpbx (Pourbaix diagram code from the paper): https://github.com/surfpbx/surfpbx

## Workflow steps

### Step 1: Extract stable 2D material candidates from C2DB
- Role: scored
- Action: Query the Computational 2D Materials Database (C2DB) and select all monolayer materials with hull energy ΔE_hull < 50 meV/atom. Write the resulting list of material identifiers (one per line) to the output file.
- Output file: `/app/outputs/step_01_materials_list.txt`
- Format: txt
- Contract: Plain text file, no header. One material identifier per line. Exactly 3376 non‑empty lines.
- Scoring: scored by hidden verifier

### Step 2: Compute Pourbaix energies for all materials at six electrochemical conditions
- Role: scored (load-bearing)
- Action: For each material ID from step_01, use the Atomic Simulation Environment (ASE) Pourbaix implementation with solid-phase references fetched from the Open Quantum Materials Database (OQMD). Set ionic activities (except H⁺) to 10⁻⁶ mol/L when evaluating the activity product. Compute the Pourbaix energy ΔG_pbx (eV/atom) at the six prescribed pH–potential points: HER acidic (pH=0, U=0 V), HER neutral (pH=7, U=-0.41 V), HER alkaline (pH=14, U=-0.83 V); OER acidic (pH=0, U=1.23 V), OER neutral (pH=7, U=0.82 V), OER alkaline (pH=14, U=0.40 V). Write a CSV file with the results.
- Output file: `/app/outputs/step_02_delta_G_pbx.csv`
- Format: csv
- Contract: CSV file with columns: material_id (string), delta_G_pbx_HER_acidic (float), delta_G_pbx_HER_neutral (float), delta_G_pbx_HER_alkaline (float), delta_G_pbx_OER_acidic (float), delta_G_pbx_OER_neutral (float), delta_G_pbx_OER_alkaline (float). One row per material (3376 rows). No missing values.
- Scoring: scored by hidden verifier

### Step 3: Calculate stability summary and histograms
- Role: scored
- Action: From the per‑material ΔG_pbx values in step_02, compute for each of the six conditions: the percentage of materials with ΔG_pbx < 0, the mean ΔG_pbx (eV/atom), and histogram bin edges/counts. For HER conditions, use bins from 0 to 2 eV/atom with a width of 0.1. For OER conditions, use bins from 0 to 8 eV/atom with a width of 0.5. Write a JSON summary file.
- Output file: `/app/outputs/step_03_stability_summary.json`
- Format: json
- Contract: JSON object with keys 'HER_acidic', 'HER_neutral', 'HER_alkaline', 'OER_acidic', 'OER_neutral', 'OER_alkaline'. Each value is an object containing: 'stable_percentage' (float, 0–100), 'mean_delta_G' (float, eV/atom), 'histogram_bin_edges' (array of floats), 'histogram_counts' (array of integers). Bin edges for HER span 0 to 2 with step 0.1; OER span 0 to 8 with step 0.5.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_materials_list.txt`
- `/app/outputs/step_02_delta_G_pbx.csv`
- `/app/outputs/step_03_stability_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_materials_list.txt
- path: `/app/outputs/step_01_materials_list.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: List of stable 2D material identifiers from C2DB. Checked for correct count and format.
- schema:
  - `type`: text
  - `required`:
    - `line_count`: 3376
  - `description`: One material identifier per line. No header. Exactly 3376 non‑empty lines.

### step_02_delta_G_pbx.csv
- path: `/app/outputs/step_02_delta_G_pbx.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑material Pourbaix energies. The checker recomputes the fraction of materials with ΔG_pbx < 0 for each condition and compares to the paper's hidden percentages.
- schema:
  - `type`: table
  - `required_columns`: `material_id`, `delta_G_pbx_HER_acidic`, `delta_G_pbx_HER_neutral`, `delta_G_pbx_HER_alkaline`, `delta_G_pbx_OER_acidic`, `delta_G_pbx_OER_neutral`, `delta_G_pbx_OER_alkaline`
  - `units`:
    - `delta_G_pbx_*`: eV/atom
  - `description`: Each row corresponds to one material. All delta_G_pbx values are numeric floats in eV/atom. Missing values not allowed.

### step_03_stability_summary.json
- path: `/app/outputs/step_03_stability_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Summary statistics and histogram data derived from step_02. Checked for structural consistency and histogram range/bin steps.
- schema:
  - `type`: object
  - `required`:
    - `HER_acidic`: object
    - `HER_neutral`: object
    - `HER_alkaline`: object
    - `OER_acidic`: object
    - `OER_neutral`: object
    - `OER_alkaline`: object
  - `description`: Each condition value is an object containing: stable_percentage (float 0-100), mean_delta_G (float eV/atom), histogram_bin_edges (array of floats), histogram_counts (array of ints). The checker verifies internal consistency with step_02 and correct histogram bounds.

Notes: All outputs are scored; step_01 ensures the correct material set is used, step_02 carries the main computational burden and is load_bearing, step_03 provides aggregated views used for structural audits.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_materials_list.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "line_count": "3376"
        },
        "description": "One material identifier per line. No header. Exactly 3376 non‑empty lines."
      },
      "description": "List of stable 2D material identifiers from C2DB. Checked for correct count and format."
    },
    {
      "file": "step_02_delta_G_pbx.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material_id",
          "delta_G_pbx_HER_acidic",
          "delta_G_pbx_HER_neutral",
          "delta_G_pbx_HER_alkaline",
          "delta_G_pbx_OER_acidic",
          "delta_G_pbx_OER_neutral",
          "delta_G_pbx_OER_alkaline"
        ],
        "units": {
          "delta_G_pbx_*": "eV/atom"
        },
        "description": "Each row corresponds to one material. All delta_G_pbx values are numeric floats in eV/atom. Missing values not allowed."
      },
      "description": "Per‑material Pourbaix energies. The checker recomputes the fraction of materials with ΔG_pbx < 0 for each condition and compares to the paper's hidden percentages."
    },
    {
      "file": "step_03_stability_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "HER_acidic": "object",
          "HER_neutral": "object",
          "HER_alkaline": "object",
          "OER_acidic": "object",
          "OER_neutral": "object",
          "OER_alkaline": "object"
        },
        "description": "Each condition value is an object containing: stable_percentage (float 0-100), mean_delta_G (float eV/atom), histogram_bin_edges (array of floats), histogram_counts (array of ints). The checker verifies internal consistency with step_02 and correct histogram bounds."
      },
      "description": "Summary statistics and histogram data derived from step_02. Checked for structural consistency and histogram range/bin steps."
    }
  ],
  "notes": "All outputs are scored; step_01 ensures the correct material set is used, step_02 carries the main computational burden and is load_bearing, step_03 provides aggregated views used for structural audits."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s output artifact and combines the stage scores into a final reward. The verifier performs a structural audit on the material list (line count, format), recomputes the stable-material fractions directly from your CSV and compares them to the paper’s reported values with an appropriate tolerance, and checks the JSON summary for internal consistency with the CSV and correct histogram bounds. Reporting numbers that are not the result of a genuine ASE computation is unlikely to yield a high reward, because the tolerance is calibrated to accept real re-run variability while excluding generic guesses. The final reward is a weighted combination, with the CSV (step_02) carrying the largest weight.
