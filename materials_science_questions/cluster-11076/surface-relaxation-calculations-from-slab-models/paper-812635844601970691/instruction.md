# Surface relaxation calculations for Al(001) and Al(110) using DFT slab models

## Problem background
The atomic layers at a crystal surface often adjust their spacing relative to the bulk — a phenomenon known as interlayer relaxation. Density functional theory (DFT) can predict these relaxations by computing total energies and forces for different surface geometries. This task focuses on two low‑index surfaces of aluminum, Al(001) and Al(110), for which experimental relaxation values exist. The goal is to determine, from first principles, the equilibrium surface relaxation and, for Al(001), the work function.

## Approach
The reproduction uses plane‑wave DFT slab calculations within the local‑density approximation (LDA). For each surface, a symmetric slab model is constructed with vacuum separating periodic images. Self‑consistent DFT calculations are performed at many different interlayer spacings of the surface layer, spanning both contraction and expansion of the bulk spacing. The total energy and Hellmann‑Feynman forces are recorded for each displacement. For Al(001) the work function is also computed. The equilibrium spacing is identified by fitting the total energy vs. displacement curve to a high‑order polynomial; the relaxation percentage is then the percentage change of that equilibrium spacing relative to the bulk interlayer distance. The approach does not require any specific proprietary code — an open‑source DFT code capable of LDA slab calculations provides equivalent results.

## Reproduction target
Produce, from DFT slab calculations, the surface relaxation percentages for Al(001) and Al(110) (the contraction or expansion of the outermost interlayer spacing as a percentage of the bulk spacing). For Al(001), also extract the work function at the equilibrium geometry. Your outputs must include the raw computed data for each surface (energy, forces, work function at each displacement) and a summary file reporting the final relaxation percentages and work function. The required files and formats are detailed in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Al LDA pseudopotential: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Al(001) surface DFT and curve generation
- Role: scored (load-bearing)
- Action: Construct a symmetric slab model for Al(001), perform DFT calculations using LDA for at least 20 different surface-layer spacings around the bulk interlayer separation (step ~0.02 a.u.), and compute total energy, work function, Hellmann-Feynman forces, and force from a polynomial fit to the energy curve. Output all results in a CSV file.
- Output file: `/app/outputs/al001_relaxation.csv`
- Format: csv
- Contract: columns: spacing_change (float, in a.u.), total_energy (float, in hartree), work_function (float, in eV), force_direct (float, in hartree/bohr), force_from_derivative (float, in hartree/bohr). At least 20 rows covering -0.5 to +0.5 a.u. from bulk spacing.
- Scoring: scored by hidden verifier

### Step 2: Al(110) surface DFT and curve generation
- Role: scored
- Action: Construct a symmetric slab model for Al(110), perform DFT calculations using LDA for at least 15 different surface-layer spacings, and compute total energy and Hellmann-Feynman forces. Output the data.
- Output file: `/app/outputs/al110_relaxation.csv`
- Format: csv
- Contract: columns: spacing_change (float, in a.u.), total_energy (float, in hartree), force (float, in hartree/bohr). At least 15 rows.
- Scoring: scored by hidden verifier

### Step 3: Extract relaxation percentages and work function
- Role: scored
- Action: From the two CSV files, determine the equilibrium interlayer spacing for each surface by fitting the total energy curve to a polynomial and finding the minimum. Compute the relaxation percentage relative to the bulk spacing. For Al(001), extract the work function at the equilibrium spacing. Write a JSON file with the three headline quantities.
- Output file: `/app/outputs/results_summary.json`
- Format: json
- Contract: JSON object with keys: al001_relaxation_percent (float), al001_work_function_eV (float), al110_relaxation_percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/al001_relaxation.csv`
- `/app/outputs/al110_relaxation.csv`
- `/app/outputs/results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### al001_relaxation.csv
- path: `/app/outputs/al001_relaxation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw DFT data for Al(001) surface at various interlayer spacings. Checker will fit energy curve to obtain relaxation and work function.
- schema:
  - `type`: table
  - `required_columns`: `spacing_change`, `total_energy`, `work_function`, `force_direct`, `force_from_derivative`
  - `units`:
    - `spacing_change`: a.u.
    - `total_energy`: hartree
    - `work_function`: eV
    - `force_direct`: hartree/bohr
    - `force_from_derivative`: hartree/bohr

### al110_relaxation.csv
- path: `/app/outputs/al110_relaxation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw DFT data for Al(110) surface at various interlayer spacings. Checker will fit energy curve to obtain relaxation.
- schema:
  - `type`: table
  - `required_columns`: `spacing_change`, `total_energy`, `force`
  - `units`:
    - `spacing_change`: a.u.
    - `total_energy`: hartree
    - `force`: hartree/bohr

### results_summary.json
- path: `/app/outputs/results_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent's self-reported relaxation percentages and work function. Checker will validate consistency with its own recomputed values from the CSVs.
- schema:
  - `type`: object
  - `required`:
    - `al001_relaxation_percent`: float
    - `al001_work_function_eV`: float
    - `al110_relaxation_percent`: float

Notes: The primary scoring is based on recomputed relaxation percentages and work function from the CSV files; the summary JSON is a secondary consistency check. Tolerances and exact gold values are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "al001_relaxation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "spacing_change",
          "total_energy",
          "work_function",
          "force_direct",
          "force_from_derivative"
        ],
        "units": {
          "spacing_change": "a.u.",
          "total_energy": "hartree",
          "work_function": "eV",
          "force_direct": "hartree/bohr",
          "force_from_derivative": "hartree/bohr"
        }
      },
      "description": "Raw DFT data for Al(001) surface at various interlayer spacings. Checker will fit energy curve to obtain relaxation and work function."
    },
    {
      "file": "al110_relaxation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "spacing_change",
          "total_energy",
          "force"
        ],
        "units": {
          "spacing_change": "a.u.",
          "total_energy": "hartree",
          "force": "hartree/bohr"
        }
      },
      "description": "Raw DFT data for Al(110) surface at various interlayer spacings. Checker will fit energy curve to obtain relaxation."
    },
    {
      "file": "results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "al001_relaxation_percent": "float",
          "al001_work_function_eV": "float",
          "al110_relaxation_percent": "float"
        }
      },
      "description": "Agent's self-reported relaxation percentages and work function. Checker will validate consistency with its own recomputed values from the CSVs."
    }
  ],
  "notes": "The primary scoring is based on recomputed relaxation percentages and work function from the CSV files; the summary JSON is a secondary consistency check. Tolerances and exact gold values are hidden."
}
```

## How you are scored
A hidden verifier will read your submitted artifact files and independently score them. For each surface, the verifier will fit a polynomial to the total energy vs. displacement curve in your CSV, locate the equilibrium spacing, and compute the relaxation percentage. For Al(001) it will also note the work function at that spacing. The derived values are compared to hidden reference benchmarks with tolerances appropriate for the toolchain differences expected in plane‑wave DFT LDA slab calculations. The verifier may also check that the force derived from the energy curve and the directly computed Hellmann‑Feynman force agree within a prescribed margin at equilibrium. Each scored step contributes a share of the final reward; the summary JSON is validated for consistency with the recomputed results. Simply reporting a number without the underlying data or without a valid computation will not pass the checks.
