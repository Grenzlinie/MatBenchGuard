# DFT Reproduction of Ti2SC Equilibrium Lattice Constants and Bulk Modulus

## Problem background
Ti2SC is a layered ternary carbide belonging to the MAX phase family, which exhibits an unusual combination of metallic and ceramic properties. First-principles density functional theory (DFT) can predict its ground-state structural parameters and elastic response, providing insight into the mechanical stability and compressibility of the material. This task focuses on computing the equilibrium lattice constants and the bulk modulus using DFT, and comparing the results to the experimental findings reported for Ti2SC.

## Approach
Use plane-wave DFT with the generalised gradient approximation (GGA-PBE functional) to model Ti2SC in its hexagonal P63/mmc crystal structure. First, perform a full geometry optimisation—relaxing both atomic positions and cell parameters—to obtain the zero-pressure equilibrium lattice constants a and c. Then, generate a set of total-energy calculations at several volumes around the equilibrium by uniformly scaling the cell. Fit the resulting energy-volume data to the Birch-Murnaghan equation of state to extract the equilibrium volume V0, the bulk modulus K0, and its pressure derivative K0'. The calculations are to be carried out with an open-source DFT code, using publicly available pseudopotentials.

## Reproduction target
Reproduce the DFT-predicted zero-pressure lattice parameters a and c (in ångströms) and the Birch-Murnaghan equation-of-state parameters V0, K0, and K0' for Ti2SC. The lattice parameters must be reported after the geometry optimisation; the EOS parameters must be obtained from a fit to the volume-energy data produced by a series of DFT total-energy calculations around the equilibrium volume.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- Ti2SC crystal structure (hexagonal, P6_3/mmc)
- GGA-PBE pseudopotentials for Ti, S, C: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Run a DFT geometry optimization for Ti2SC using an open-source plane-wave code with GGA-PBE functional. Relax both atomic positions and cell parameters to obtain the equilibrium lattice constants a and c. Retain the output log as evidence.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Extract optimized lattice parameters
- Role: scored (load-bearing)
- Action: From the relaxed structure, extract the equilibrium lattice parameters a and c and write them to a CSV file.
- Output file: `/app/outputs/step_01_optimized_lattice.csv`
- Format: csv
- Contract: columns: a, c
- Scoring: scored by hidden verifier

### Step 3: Equation-of-state volume scan
- Role: process
- Action: Perform a series of DFT total-energy calculations on Ti2SC structures with uniformly scaled cell volumes around the equilibrium volume. Save the resulting (volume, energy) pairs to a CSV file.
- Evidence: `/app/outputs/eos_data.csv`

### Step 4: Fit Birch-Murnaghan equation of state
- Role: scored (load-bearing)
- Action: Fit the volume-energy dataset to the Birch-Murnaghan equation of state using least-squares regression. Output the fitted parameters in a JSON file.
- Output file: `/app/outputs/step_02_eos_fit.json`
- Format: json
- Contract: keys: V0 (float, Angstrom^3), K0 (float, GPa), K0_prime (float, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_optimized_lattice.csv`
- `/app/outputs/step_02_eos_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_optimized_lattice.csv
- path: `/app/outputs/step_01_optimized_lattice.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file with one header row and one data row giving the DFT-optimized lattice parameters a and c of Ti2SC at zero pressure. Checked against the paper's hidden ab initio values within tolerances appropriate for code/pseudopotential differences.
- schema:
  - `type`: table
  - `required_columns`: `a`, `c`
  - `units`:
    - `a`: Angstrom
    - `c`: Angstrom

### step_02_eos_fit.json
- path: `/app/outputs/step_02_eos_fit.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON object containing the agent's Birch-Murnaghan EOS fit from volume-energy data. The hidden checker recomputes the fit from the raw eos_data.csv evidence file and compares the resulting V0, K0, K0' to the paper's ab initio values; this reported JSON is used as a redundant cross-check.
- schema:
  - `type`: object
  - `required`:
    - `V0`: float
    - `K0`: float
    - `K0_prime`: float
  - `units`:
    - `V0`: Angstrom^3
    - `K0`: GPa
    - `K0_prime`: dimensionless

Notes: The process step eos_calc must output a CSV with columns 'Volume' and 'Energy' as evidence. The checker uses that file for independent recomputation of the EOS parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_optimized_lattice.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a",
          "c"
        ],
        "units": {
          "a": "Angstrom",
          "c": "Angstrom"
        }
      },
      "description": "CSV file with one header row and one data row giving the DFT-optimized lattice parameters a and c of Ti2SC at zero pressure. Checked against the paper's hidden ab initio values within tolerances appropriate for code/pseudopotential differences."
    },
    {
      "file": "step_02_eos_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "V0": "float",
          "K0": "float",
          "K0_prime": "float"
        },
        "units": {
          "V0": "Angstrom^3",
          "K0": "GPa",
          "K0_prime": "dimensionless"
        }
      },
      "description": "JSON object containing the agent's Birch-Murnaghan EOS fit from volume-energy data. The hidden checker recomputes the fit from the raw eos_data.csv evidence file and compares the resulting V0, K0, K0' to the paper's ab initio values; this reported JSON is used as a redundant cross-check."
    }
  ],
  "notes": "The process step eos_calc must output a CSV with columns 'Volume' and 'Energy' as evidence. The checker uses that file for independent recomputation of the EOS parameters."
}
```

## How you are scored
A hidden verifier scores each of the two load-bearing artifacts independently. The lattice parameters in `step_01_optimized_lattice.csv` are compared to hidden reference values within tolerances that account for differences in DFT code, pseudopotentials, and convergence settings. The EOS parameters in `step_02_eos_fit.json` are verified by recomputing the Birch-Murnaghan fit from your raw `eos_data.csv` and comparing the resulting V0, K0, and K0' to hidden reference values. The two scored stages carry equal weight; the final reward is the sum of their partial scores. The verifier does not accept the paper's published numbers as a substitute—the required artifacts must be produced by your own DFT workflow.
