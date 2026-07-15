# Polymorph Control in Lennard-Jones Crystallization via MD Simulations

## Problem background
Crystallization of atomic fluids can result in different polymorphs (face-centered cubic, hexagonal close-packed, body-centered cubic). Controlling which polymorph forms is crucial for applications ranging from pharmaceuticals to functional materials. This study uses molecular dynamics simulations of Lennard-Jones particles to investigate how the conditions of crystallization—specifically, the applied pressure and the degree of supercooling—influence the composition of the resulting crystallites. The aim is to understand whether we can steer polymorph selection by changing these external parameters.

## Approach
The workflow mirrors the full crystallization process: nucleation followed by growth. First, umbrella sampling MD simulations with a harmonic bias on the global bond-order parameter Q6 are performed to generate critical nuclei. For pressure-varied studies, simulations are run at 25% supercooling and several reduced pressures (notably P=10 and P=50). For temperature-varied studies, the pressure is fixed at P=5.68 and supercoolings of 22% and 10% relative to the melting temperature are used. Each critical nucleus is then embedded in a much larger liquid system. After a short equilibration with the bias retained on the central region, the bias is removed and multiple unbiased growth trajectories are launched. The evolving crystallites are analyzed using local bond-order analysis (e.g., the pyscal package) to classify every particle as fcc, hcp, or bcc. This yields, for each set of conditions, the polymorph composition as a function of crystallite size, from which the final core composition and the extent of cross-nucleation between polymorphs can be quantified.

## Reproduction target
The goal is to reproduce two key quantitative findings by executing the full nucleation–growth–analysis pipeline.

1. **Pressure-driven polymorph control**: Compute the final core composition (percentages of fcc, hcp, and bcc particles) at the end of growth for crystallization at 25% supercooling and pressures P=10 and P=50. The results must be reported in `pressure_composition.json`.

2. **Temperature-driven control of cross-nucleation**: Compute the average number of hcp particles as a function of total crystallite size for supercoolings of 22% and 10% at a fixed pressure of P=5.68. The results must be reported in `temperature_hcp_counts.csv` for crystallite sizes from 1000 to 5000 particles. Together these outputs allow one to assess how pressure changes the stable/metastable polymorph fractions and how temperature influences the growth of the hcp phase via cross-nucleation.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- pyscal: pyscal
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib
- MDAnalysis: MDAnalysis

## Workflow steps

### Step 1: Umbrella-sampling MD for pressure-varied critical nuclei
- Role: process
- Action: Perform umbrella-sampling MD simulations for Lennard-Jones fluid at 25% supercooling with pressures P=10 and P=50, using harmonic bias on Q6 order parameter, system size 4000 particles. Generate critical nucleus configurations for each pressure.
- Evidence: `/app/outputs/umbrella_pressure_log.txt`

### Step 2: Pressure-varied growth MD simulations
- Role: process
- Action: For each pressure, embed the critical nucleus from step1_pressure_umbrella into a larger liquid phase (32000 particles). Equilibrate for 10 time units with umbrella bias retained on central 4000 particles, then switch off bias and run 10 independent unbiased trajectories. Collect trajectory data.
- Evidence: `/app/outputs/growth_pressure_log.txt`

### Step 3: Polymorph fraction analysis for pressure variation
- Role: scored (load-bearing)
- Action: Using local bond-order analysis (e.g., via pyscal), identify fcc, hcp, and bcc particles in all growth trajectories from step2_pressure_growth. For each pressure, compute the number of each polymorph as a function of crystallite size, average over trajectories, and determine the final core composition percentages (fcc, hcp, bcc) at the end of growth. Output results for P=10 and P=50 only.
- Output file: `/app/outputs/pressure_composition.json`
- Format: json
- Contract: JSON object with keys 'P10' and 'P50'. Each value is an object with keys 'fcc_percent' (float), 'hcp_percent' (float), 'bcc_percent' (float).
- Scoring: scored by hidden verifier

### Step 4: Umbrella-sampling MD for temperature-varied critical nuclei
- Role: process
- Action: Perform umbrella-sampling MD simulations for Lennard-Jones fluid at fixed pressure P=5.68, for supercoolings 22% and 10% below the melting temperature. Use harmonic bias on Q6, system size 4000 particles. Generate critical nucleus configurations for each supercooling.
- Evidence: `/app/outputs/umbrella_temp_log.txt`

### Step 5: Temperature-varied growth MD simulations
- Role: process
- Action: For each supercooling from step4_temp_umbrella, embed the critical nucleus into a larger liquid of 32000 particles. Equilibrate with bias (10 time units), then release and run 10 independent unbiased trajectories. Record crystallite size and coordinates.
- Evidence: `/app/outputs/growth_temp_log.txt`

### Step 6: HCP cross-nucleation analysis for temperature variation
- Role: scored (load-bearing)
- Action: Analyze the trajectories from step5_temp_growth using local bond-order analysis to identify hcp particles. Compute the average number of hcp particles as a function of total crystallite size for supercoolings 22% and 10%. Output a CSV with columns: crystallite_size, hcp_22pct, hcp_10pct for sizes from 1000 to 5000 (or as obtainable).
- Output file: `/app/outputs/temperature_hcp_counts.csv`
- Format: csv
- Contract: CSV with columns: 'crystallite_size' (int), 'hcp_22pct' (int), 'hcp_10pct' (int). Rows for sizes 1000, 2000, 3000, 4000, 5000 (or closest available).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pressure_composition.json`
- `/app/outputs/temperature_hcp_counts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pressure_composition.json
- path: `/app/outputs/pressure_composition.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final polymorph composition percentages for P=10 and P=50, plus the bcc-liquid coexistence line from thermodynamic integration, enabling verification of the occurrence domain of the metastable bcc polymorph.
- schema:
  - `type`: object
  - `required`:
    - `P10`: object
    - `P50`: object
    - `bcc_coexistence_line`: array
  - `properties`:
    - `P10`:
      - `type`: object
      - `required`: `fcc_percent`, `hcp_percent`, `bcc_percent`
      - `properties`:
        - `fcc_percent`:
          - `type`: number
        - `hcp_percent`:
          - `type`: number
        - `bcc_percent`:
          - `type`: number
    - `P50`:
      - `type`: object
      - `required`: `fcc_percent`, `hcp_percent`, `bcc_percent`
      - `properties`:
        - `fcc_percent`:
          - `type`: number
        - `hcp_percent`:
          - `type`: number
        - `bcc_percent`:
          - `type`: number
    - `bcc_coexistence_line`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `pressure`, `T_bcc_liquid`
        - `properties`:
          - `pressure`:
            - `type`: number
          - `T_bcc_liquid`:
            - `type`: number

### temperature_hcp_counts.csv
- path: `/app/outputs/temperature_hcp_counts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average number of hcp particles versus crystallite size for supercoolings 22% and 10% at fixed pressure P=5.68, demonstrating cross-nucleation control.
- schema:
  - `type`: table
  - `required_columns`: `crystallite_size`, `hcp_22pct`, `hcp_10pct`

Notes: The scored quantities are compared against paper-reported reference values with appropriate tolerances and trend checks. The bcc-liquid coexistence line is additionally checked to confirm that the state points P=10 (outside domain) and P=50 (inside domain) lie on the correct sides of the line.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pressure_composition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "P10": "object",
          "P50": "object",
          "bcc_coexistence_line": "array"
        },
        "properties": {
          "P10": {
            "type": "object",
            "required": [
              "fcc_percent",
              "hcp_percent",
              "bcc_percent"
            ],
            "properties": {
              "fcc_percent": {
                "type": "number"
              },
              "hcp_percent": {
                "type": "number"
              },
              "bcc_percent": {
                "type": "number"
              }
            }
          },
          "P50": {
            "type": "object",
            "required": [
              "fcc_percent",
              "hcp_percent",
              "bcc_percent"
            ],
            "properties": {
              "fcc_percent": {
                "type": "number"
              },
              "hcp_percent": {
                "type": "number"
              },
              "bcc_percent": {
                "type": "number"
              }
            }
          },
          "bcc_coexistence_line": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "pressure",
                "T_bcc_liquid"
              ],
              "properties": {
                "pressure": {
                  "type": "number"
                },
                "T_bcc_liquid": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Final polymorph composition percentages for P=10 and P=50, plus the bcc-liquid coexistence line from thermodynamic integration, enabling verification of the occurrence domain of the metastable bcc polymorph."
    },
    {
      "file": "temperature_hcp_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystallite_size",
          "hcp_22pct",
          "hcp_10pct"
        ]
      },
      "description": "Average number of hcp particles versus crystallite size for supercoolings 22% and 10% at fixed pressure P=5.68, demonstrating cross-nucleation control."
    }
  ],
  "notes": "The scored quantities are compared against paper-reported reference values with appropriate tolerances and trend checks. The bcc-liquid coexistence line is additionally checked to confirm that the state points P=10 (outside domain) and P=50 (inside domain) lie on the correct sides of the line."
}
```

## How you are scored
A hidden verifier will independently examine each of your scored output files. For `pressure_composition.json`, the verifier compares your reported fcc/hcp/bcc percentages at P=10 and P=50 against reference values derived from the original study. It also checks that the compositional trends are physically consistent (e.g., the bcc fraction increases and the fcc fraction decreases as pressure is raised). For `temperature_hcp_counts.csv`, the verifier compares the hcp counts at the largest crystallite size across the two supercoolings and inspects the slope of hcp accumulation versus size. Credit is awarded when the numbers and trends agree with the hidden reference within defined tolerances; a simple restatement of published values is not sufficient—your reported numbers must arise from the full simulation pipeline. The final reward is a weighted combination of the scores from these two artifacts.
