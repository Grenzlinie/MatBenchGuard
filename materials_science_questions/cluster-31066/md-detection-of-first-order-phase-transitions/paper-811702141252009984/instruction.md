# Structural order parameter and crossover pressure from MD of SPC/E water

## Problem background
Liquid water exhibits many anomalous properties that are thought to arise from a closely interwoven mixture of two structural motifs: an open tetrahedral (low-density) arrangement and a more compact hexagonal (high-density) arrangement. Temperature and pressure shift the balance between these two components, gradually erasing water's 'anomalous' behavior as one structure comes to dominate over the other. Quantifying this competition requires an order parameter that is sensitive to structural features beyond the first coordination shell and that can be extracted directly from the oxygen-oxygen radial distribution function, g(r). This task focuses on computing such an order parameter from molecular dynamics simulations of the SPC/E water model and determining the pressure at which the structural dominance crosses over at ambient temperature.

## Approach
The approach rests on a two-state model that decomposes the g(r) into separate tetrahedral and hexagonal contributions. For each simulated pressure, the full g(r) is fitted with a G‑function that explicitly accounts for the first three coordination spheres of each contribution. The first sphere is modeled by an asymmetric Freundlich distribution, the second and third spheres by symmetric Gaussian functions, and all higher-order coordination is treated implicitly via a sigmoidal tail. The same functional form is applied consistently at every pressure. Once the G‑function parameters are obtained, a dimensionless order parameter P_r is computed as P_r = (C^t − C^h)/(C^t + C^h), where C^t and C^h are scalar measures of the tetrahedral and hexagonal contributions, respectively, derived from the second- and third-sphere Gaussian components. Positive P_r indicates tetrahedral dominance, negative P_r indicates hexagonal dominance. The analysis is carried out using molecular dynamics simulations of SPC/E water at 300 K over a range of pressures spanning from ambient up to 10 kbar, yielding the dependence of the order parameter on pressure.

## Reproduction target
Perform molecular dynamics simulations of SPC/E water at 300 K for at least the following pressures: 1 bar, 1 kbar, 2 kbar, 3 kbar, 5 kbar, and 10 kbar. From each production trajectory, compute the oxygen‑oxygen radial distribution function g(r). Fit the two-state G‑function model to each g(r) and record all fitted parameters. From the fitted parameters, calculate the order parameter P_r for every pressure and save the pressure–P_r pairs in pr_vs_pressure.csv. Finally, use the tabulated P_r data to interpolate the pressure at which P_r = 0 (the crossover point where tetrahedral and hexagonal contributions are equal). Report this crossover pressure in kbar in crossover_pressure.txt. The full pipeline must demonstrate that P_r changes monotonically with increasing pressure and that a crossover exists within the examined pressure range.

## Assets

- GROMACS: https://www.gromacs.org
- SPC/E water model
- Python scientific stack: numpy, scipy, matplotlib

## Workflow steps

### Step 1: MD simulation and g(r) calculation
- Role: process
- Action: Run MD simulations of SPC/E water at 300 K and at least the pressures: 1 bar, 1 kbar, 2 kbar, 3 kbar, 5 kbar, 10 kbar. For each pressure, equilibrate and collect a production run of at least 1 ns. Compute the oxygen-oxygen radial distribution function g(r) from the production trajectory.
- Evidence: `/app/outputs/g_r_log.txt`

### Step 2: Fit G function to g(r) data
- Role: scored
- Action: For each simulated pressure, fit the G function (a two-state decomposition with tetrahedral and hexagonal contributions, explicitly treating the first three coordination spheres via asymmetric Freundlich distributions for the first sphere and symmetric Gaussians for the second and third spheres, plus an implicit sigmoidal tail) to the computed g(r). Save all fitted parameters to fitted_parameters.csv.
- Output file: `/app/outputs/fitted_parameters.csv`
- Format: csv
- Contract: CSV with header: pressure,parameter_name,value. pressure is in bar (float), parameter_name is string identifying the parameter (e.g., A2_t, omega2_t, ...), value is float. One row per parameter per pressure.
- Scoring: scored by hidden verifier

### Step 3: Compute order parameter P_r
- Role: scored (load-bearing)
- Action: From the fitted parameters, compute the dimensionless order parameter P_r = (C^t - C^h)/(C^t + C^h) where C^t and C^h are sums of A_i^j / omega_i^j for tetrahedral and hexagonal second- and third-sphere Gaussians. Save pressure (bar) and P_r to pr_vs_pressure.csv.
- Output file: `/app/outputs/pr_vs_pressure.csv`
- Format: csv
- Contract: CSV with header: pressure,Pr. pressure in bar (float), Pr dimensionless (float). One row per simulated pressure.
- Scoring: scored by hidden verifier

### Step 4: Determine crossover pressure
- Role: scored (load-bearing)
- Action: From the pr_vs_pressure data, interpolate to find the pressure at which P_r = 0 (crossover from tetrahedral to hexagonal dominance). Write the crossover pressure in kbar to crossover_pressure.txt.
- Output file: `/app/outputs/crossover_pressure.txt`
- Format: txt
- Contract: A single line containing the crossover pressure as a floating-point number (kbar).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.csv`
- `/app/outputs/pr_vs_pressure.csv`
- `/app/outputs/crossover_pressure.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.csv
- path: `/app/outputs/fitted_parameters.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: All fitted G-function parameters for each pressure. Checker recomputes P_r from these parameters and scores against hidden gold P_r values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `parameter_name`, `value`
  - `units`:
    - `pressure`: bar
    - `value`: float (mixed units per parameter)

### pr_vs_pressure.csv
- path: `/app/outputs/pr_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Order parameter P_r at each pressure. Checker compares the reported P_r values directly to hidden paper gold values (from Fig. 3) with tolerance, and enforces monotonic decrease.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `Pr`
  - `units`:
    - `pressure`: bar
    - `Pr`: dimensionless

### crossover_pressure.txt
- path: `/app/outputs/crossover_pressure.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Pressure where P_r=0 (crossover from tetrahedral to hexagonal dominance). Checker compares to paper-reported value within tolerance.
- schema:
  - `type`: text
  - `units`: kbar

Notes: The task covers only the 300 K pressure sweep using SPC/E water; the temperature-dependent curve and argon reference are omitted per scope. The checker recomputes P_r from fitted_parameters.csv as a consistency check and compares pr_vs_pressure.csv and crossover_pressure.txt to hidden gold derived from the paper's Fig. 3. All scored artifacts must be present; missing files score zero.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "parameter_name",
          "value"
        ],
        "units": {
          "pressure": "bar",
          "value": "float (mixed units per parameter)"
        }
      },
      "description": "All fitted G-function parameters for each pressure. Checker recomputes P_r from these parameters and scores against hidden gold P_r values from the paper."
    },
    {
      "file": "pr_vs_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "Pr"
        ],
        "units": {
          "pressure": "bar",
          "Pr": "dimensionless"
        }
      },
      "description": "Order parameter P_r at each pressure. Checker compares the reported P_r values directly to hidden paper gold values (from Fig. 3) with tolerance, and enforces monotonic decrease."
    },
    {
      "file": "crossover_pressure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "kbar"
      },
      "description": "Pressure where P_r=0 (crossover from tetrahedral to hexagonal dominance). Checker compares to paper-reported value within tolerance."
    }
  ],
  "notes": "The task covers only the 300 K pressure sweep using SPC/E water; the temperature-dependent curve and argon reference are omitted per scope. The checker recomputes P_r from fitted_parameters.csv as a consistency check and compares pr_vs_pressure.csv and crossover_pressure.txt to hidden gold derived from the paper's Fig. 3. All scored artifacts must be present; missing files score zero."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently inspects each scored output and combines the results by weight. The verifier recomputes the order parameter P_r from the parameters you provide in fitted_parameters.csv and checks internal consistency with the values in pr_vs_pressure.csv. It then compares your reported P_r values (and the implied trend) against reference quantities derived from the paper's published results, which are kept hidden. It also verifies that P_r decreases monotonically with increasing pressure. The crossover pressure in crossover_pressure.txt is compared directly to the published reference. Meeting or exceeding the expected accuracy earns full credit; partial credit is awarded if the results deviate but remain within a tolerance band. The final reward is a weighted sum: pr_vs_pressure.csv and crossover_pressure.txt carry the largest weight, while fitted_parameters.csv contributes with a moderate weight. The process evidence log g_r_log.txt is not scored but may be used to support a reproducibility audit.
