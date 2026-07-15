# Structural properties and phase stability of Sc1-xInxN from first-principles DFT

## Problem background
Scandium indium nitride (Sc₁₋ₓInₓN) is a ternary compound with potential applications in hard coatings and optoelectronics. Its structural properties and phase stability as a function of indium composition are not well established for intermediate compositions. Understanding how the lattice constants, bulk modulus, and relative stability of the rocksalt (NaCl) and wurtzite crystal structures evolve across the full composition range is important for guiding synthesis and device design. This task aims to reproduce first‑principles predictions of these structural properties and the phase stability from a density functional theory (DFT) study.

## Approach
The reproduction uses density functional theory (DFT) with the generalized gradient approximation (GGA‑PBE) to compute total energies of Sc₁₋ₓInₓN for compositions x = 0, 0.25, 0.5, 0.75, 1 in both NaCl and wurtzite crystal structures. For the intermediate compositions, special quasirandom structures (SQS) are employed to model the disordered alloy. The calculations include internal relaxation and c/a optimization for the wurtzite phase. From the total energy vs. volume data, equilibrium lattice constants, bulk moduli, and equilibrium energies are extracted by fitting to the Murnaghan equation of state. The composition dependence is then analyzed to obtain bowing parameters for the lattice constant and bulk modulus in each phase. Finally, the relative total energies of the two phases are used to determine the crossover composition where wurtzite becomes more stable than NaCl.

## Reproduction target
Using an open‑source DFT code (Quantum ESPRESSO) with GGA‑PBE and appropriate pseudopotentials (e.g., GBRV), compute the equilibrium lattice constants (a and, for wurtzite, c), bulk moduli (B₀), and total energies per unit cell for Sc₁₋ₓInₓN at compositions x = 0, 0.25, 0.5, 0.75, 1 in both NaCl and wurtzite structures. Model the alloys with SQS supercells. Fit the energy‑volume data to the Murnaghan equation of state and output the results to results_summary.csv. From these data, determine the bowing parameters (α for lattice constant, β for bulk modulus) by fitting quadratic functions for each phase, and write them to bowing_parameters.json. Compare total energies to identify the crossover composition and stable phase ranges, outputting that to phase_transition_composition.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV pseudopotentials: http://www.physics.rutgers.edu/gbrv/

## Workflow steps

### Step 1: Generate SQS supercells
- Role: process
- Action: Generate special quasirandom structure (SQS) supercells for Sc1-xInxN at compositions x=0.25, 0.5, 0.75 in both NaCl and wurtzite structures, using the cell sizes and geometries described in the original DFT study. Prepare conventional unit cells for pure ScN (x=0) and InN (x=1) endpoints.
- Evidence: none

### Step 2: Perform DFT energy-volume calculations
- Role: process
- Action: For each generated structure, run Quantum ESPRESSO self-consistent field calculations at multiple volumes using GGA-PBE functional and appropriate pseudopotentials. Include internal parameter optimization (u, c/a) for wurtzite phases. Collect total energy vs volume data for each composition and phase.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 3: Murnaghan EOS fitting and property extraction
- Role: scored (load-bearing)
- Action: Fit each total energy vs volume dataset to the Murnaghan equation of state to obtain equilibrium lattice constants (a and c for wurtzite; a0 for NaCl), bulk modulus B0, and equilibrium total energy E0. Write results to results_summary.csv.
- Output file: `/app/outputs/results_summary.csv`
- Format: csv
- Contract: Columns: composition, phase, lattice_constant_a (Angstrom), lattice_constant_c (Angstrom, 0 for cubic), bulk_modulus (GPa), total_energy (eV per unit cell). One row per composition/structure.
- Scoring: scored by hidden verifier

### Step 4: Compute bowing parameters
- Role: scored
- Action: From the equilibrium lattice constants and bulk moduli in results_summary.csv, fit quadratic functions to obtain bowing parameters (alpha for lattice constant, beta for bulk modulus) for both NaCl and wurtzite phases. Write results to bowing_parameters.json.
- Output file: `/app/outputs/bowing_parameters.json`
- Format: json
- Contract: {"NaCl": {"alpha_lattice_bowing_parameter": number (Angstrom), "beta_bulk_modulus_bowing_parameter": number (GPa)}, "wurtzite": {"alpha_lattice_bowing_parameter": number, "beta_bulk_modulus_bowing_parameter": number}}
- Scoring: scored by hidden verifier

### Step 5: Determine phase stability
- Role: scored
- Action: Using the total energies from results_summary.csv, compare NaCl and wurtzite energies for each composition. Identify the crossover composition where wurtzite becomes lower in energy. Write results to phase_transition_composition.json.
- Output file: `/app/outputs/phase_transition_composition.json`
- Format: json
- Contract: {"crossover_x": number, "stable_NaCl_range": string, "stable_wurtzite_range": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_summary.csv`
- `/app/outputs/bowing_parameters.json`
- `/app/outputs/phase_transition_composition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_summary.csv
- path: `/app/outputs/results_summary.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constants, bulk moduli, and total energies for all Sc1-xInxN compositions and phases.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `phase`, `lattice_constant_a`, `lattice_constant_c`, `bulk_modulus`, `total_energy`
  - `units`:
    - `lattice_constant_a`: Angstrom
    - `lattice_constant_c`: Angstrom
    - `bulk_modulus`: GPa
    - `total_energy`: eV per unit cell

### bowing_parameters.json
- path: `/app/outputs/bowing_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bowing parameters alpha (lattice) and beta (bulk) for NaCl and wurtzite phases.
- schema:
  - `type`: object
  - `required`:
    - `NaCl`:
      - `alpha_lattice_bowing_parameter`:
        - `type`: number
        - `unit`: Angstrom
      - `beta_bulk_modulus_bowing_parameter`:
        - `type`: number
        - `unit`: GPa
    - `wurtzite`:
      - `alpha_lattice_bowing_parameter`:
        - `type`: number
        - `unit`: Angstrom
      - `beta_bulk_modulus_bowing_parameter`:
        - `type`: number
        - `unit`: GPa

### phase_transition_composition.json
- path: `/app/outputs/phase_transition_composition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Crossover composition where wurtzite becomes more stable; stable ranges.
- schema:
  - `type`: object
  - `required`:
    - `crossover_x`:
      - `type`: number
    - `stable_NaCl_range`:
      - `type`: string
    - `stable_wurtzite_range`:
      - `type`: string

Notes: All values compared to paper-reported reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "phase",
          "lattice_constant_a",
          "lattice_constant_c",
          "bulk_modulus",
          "total_energy"
        ],
        "units": {
          "lattice_constant_a": "Angstrom",
          "lattice_constant_c": "Angstrom",
          "bulk_modulus": "GPa",
          "total_energy": "eV per unit cell"
        }
      },
      "description": "Equilibrium lattice constants, bulk moduli, and total energies for all Sc1-xInxN compositions and phases."
    },
    {
      "file": "bowing_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "NaCl": {
            "alpha_lattice_bowing_parameter": {
              "type": "number",
              "unit": "Angstrom"
            },
            "beta_bulk_modulus_bowing_parameter": {
              "type": "number",
              "unit": "GPa"
            }
          },
          "wurtzite": {
            "alpha_lattice_bowing_parameter": {
              "type": "number",
              "unit": "Angstrom"
            },
            "beta_bulk_modulus_bowing_parameter": {
              "type": "number",
              "unit": "GPa"
            }
          }
        }
      },
      "description": "Bowing parameters alpha (lattice) and beta (bulk) for NaCl and wurtzite phases."
    },
    {
      "file": "phase_transition_composition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "crossover_x": {
            "type": "number"
          },
          "stable_NaCl_range": {
            "type": "string"
          },
          "stable_wurtzite_range": {
            "type": "string"
          }
        }
      },
      "description": "Crossover composition where wurtzite becomes more stable; stable ranges."
    }
  ],
  "notes": "All values compared to paper-reported reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier scores each of the three output artifacts independently by comparing the submitted values to reference results from the original study. results_summary.csv is checked for accuracy of lattice constants and bulk moduli within appropriate tolerances. bowing_parameters.json is verified for correct sign and magnitude of the bowing parameters. phase_transition_composition.json is checked against the expected crossover behavior and stable ranges. Each artifact carries a weight: results_summary.csv is load‑bearing and receives the largest weight, while the other two artifacts contribute smaller weights. A final combined reward (0 to 1) is written. Reporting the paper’s numbers is not enough; the artifacts must be generated through the prescribed computational workflow.
