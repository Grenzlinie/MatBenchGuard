# Reproduction of Vegard's Law Deviation in InAsSb Alloys via DFT

## Problem background
III-V semiconductor alloys, such as InAs_xSb_{1-x}, are studied for their tunable structural and electronic properties. A common reference model for the composition dependence of the lattice constant is Vegard's law, a linear interpolation between the end-member binary compounds. This task investigates the structural optimization of zinc-blende InAs_xSb_{1-x} alloys using density functional theory (DFT) within the local density approximation (LDA), employing the virtual crystal approximation (VCA) to represent the alloy. The objective is to compute the equilibrium lattice parameters for several compositions and then to quantify how closely they follow Vegard's law.

## Approach
The calculations are performed with the open-source plane-wave pseudopotential DFT code ABINIT. Two distinct norm-conserving pseudopotential sets are used: the Hartwigsen–Goedecker–Hutter (HGH) pseudopotentials and the Troullier–Martins (FHI) pseudopotentials (the FHI set for indium includes the 4d semicore electrons). For each composition x = 0, 0.25, 0.5, 0.75, 1, the ternary alloy is modeled within the VCA by constructing an ionic pseudopotential as a linear combination of the As and Sb pseudopotentials. LDA exchange-correlation is employed. The crystal structure is relaxed until the forces on the atoms are converged, yielding the equilibrium cubic lattice constant for each condition. From these lattice constants, the maximum percent deviation from Vegard's law is derived for each pseudopotential set, using the computed x = 0 and x = 1 endpoints as the Vegard reference.

## Reproduction target
Produce the equilibrium cubic lattice parameters (in Å) for InAs_xSb_{1-x} at compositions x = 0, 0.25, 0.5, 0.75, 1 using DFT-LDA with both HGH and FHI pseudopotentials. From these results, compute the maximum percent deviation from Vegard's law (a_ideal(x) = x·a_InAs + (1−x)·a_InSb) for each pseudopotential scheme, taken over the intermediate compositions x = 0.25, 0.5, 0.75.

## Assets

- ABINIT software: https://www.abinit.org/downloads
- HGH LDA pseudopotentials for In, As, Sb: https://www.abinit.org/downloads/pseudopotentials
- FHI (Troullier-Martins) LDA pseudopotentials for In, As, Sb (with In 4d): https://www.abinit.org/downloads/pseudopotentials

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: For each composition x in {0, 0.25, 0.5, 0.75, 1} and for each pseudopotential scheme (HGH.LDA and FHI.LDA), construct the virtual crystal approximation (VCA) ionic pseudopotential as a linear combination of As and Sb pseudopotentials, set up ABINIT calculations within LDA exchange-correlation, and perform structural relaxation until forces are converged. Store the final optimized crystal structures and convergence logs.
- Evidence: `/app/outputs/optimization_logs.json`

### Step 2: Extract lattice parameters
- Role: scored (load-bearing)
- Action: From the final optimized geometries of each DFT run, extract the equilibrium cubic lattice parameter a (in Å) and compile them into a CSV file.
- Output file: `/app/outputs/lattice_parameters.csv`
- Format: csv
- Contract: composition (float), pseudopotential (string), lattice_parameter_angstrom (float)
- Scoring: scored by hidden verifier

### Step 3: Compute Vegard's law deviation
- Role: scored
- Action: Using the lattice parameters from step_2, compute the maximum percent deviation from Vegard's law for each pseudopotential scheme. Vegard's law: a_ideal(x) = x*a_InAs + (1-x)*a_InSb. Calculate percent deviation = 100*|a(x) - a_ideal(x)| / a_ideal(x) for intermediate compositions and find the maximum over x=0.25, 0.5, 0.75. Write the result to a CSV file.
- Output file: `/app/outputs/vegard_deviation.csv`
- Format: csv
- Contract: pseudopotential (string), max_deviation_percent (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.csv`
- `/app/outputs/vegard_deviation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.csv
- path: `/app/outputs/lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice constants for each composition and pseudopotential scheme.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `pseudopotential`, `lattice_parameter_angstrom`
  - `units`:
    - `lattice_parameter_angstrom`: Å

### vegard_deviation.csv
- path: `/app/outputs/vegard_deviation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Maximum deviation from Vegard's law computed from the lattice parameters.
- schema:
  - `type`: table
  - `required_columns`: `pseudopotential`, `max_deviation_percent`
  - `units`:
    - `max_deviation_percent`: %

Notes: The checker recomputes the maximum percent deviation from the submitted lattice parameters and compares it to the hidden reference. The lattice parameters themselves are compared against hidden gold values with an absolute tolerance of ±0.05 Å.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "pseudopotential",
          "lattice_parameter_angstrom"
        ],
        "units": {
          "lattice_parameter_angstrom": "Å"
        }
      },
      "description": "Optimized lattice constants for each composition and pseudopotential scheme."
    },
    {
      "file": "vegard_deviation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pseudopotential",
          "max_deviation_percent"
        ],
        "units": {
          "max_deviation_percent": "%"
        }
      },
      "description": "Maximum deviation from Vegard's law computed from the lattice parameters."
    }
  ],
  "notes": "The checker recomputes the maximum percent deviation from the submitted lattice parameters and compares it to the hidden reference. The lattice parameters themselves are compared against hidden gold values with an absolute tolerance of ±0.05 Å."
}
```

## How you are scored
A hidden automated verifier independently checks each workflow stage's artifact. The lattice constants in lattice_parameters.csv are compared to reference values using an absolute tolerance. The Vegard deviation is recomputed by the verifier from the lattice constants you provide and compared to a hidden reference. The final score is a weighted combination: lattice parameter match contributes 0.7, and the correct maximum Vegard deviation contributes 0.3. Simply reporting the paper's numbers without executing the workflow will not satisfy these checks.
