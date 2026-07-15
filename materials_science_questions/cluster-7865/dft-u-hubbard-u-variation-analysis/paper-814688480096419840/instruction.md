# DFT+U Hubbard U Variation Analysis for BaFeO3

## Problem background
Perovskite oxide BaFeO3 exhibits a range of structural, electronic, and magnetic behaviors that are sensitive to the treatment of electron correlation. Density functional theory with a Hubbard U correction (DFT+U) can account for strong on-site Coulomb interactions in the Fe 3d states, potentially altering the predicted equilibrium lattice parameters, bulk modulus, and magnetic moments. This task investigates the influence of the U-Hubbard term on the ground-state properties of cubic BaFeO3 across different magnetic orderings. The goal is to compute these properties and determine how they vary with the choice of exchange-correlation functional and magnetic configuration.

## Approach
The method follows a computational workflow based on plane-wave density functional theory. The cubic perovskite BaFeO3 is constructed in four magnetic states: non-magnetic (NF), ferromagnetic (FM), A-type antiferromagnetic (A-AFM), and G-type antiferromagnetic (G-AFM). For each configuration, total-energy calculations are performed as a function of volume using three different treatments of exchange and correlation: the generalized gradient approximation (GGA), the local spin density approximation with an added Hubbard U (LSDA+U), and the generalized gradient approximation with a Hubbard U (GGA+U). The Hubbard parameters are fixed to U = 0.49 Ryd and J = 0.07 Ryd for the +U functionals. By fitting the Murnaghan equation of state to the energy-volume data, the equilibrium lattice constants (a, and c where applicable), bulk modulus B, and its pressure derivative B' are obtained. At the optimized geometry, the Fe magnetic moments are extracted from the self-consistent spin density. The comparison across functionals and magnetic configurations reveals the effect of the Hubbard correction on the structural and magnetic predictions.

## Reproduction target
The objective is to produce a single CSV file containing, for each of the four magnetic configurations (NF, FM, A-AFM, G-AFM) and each of the three methods (GGA, LSDA+U, GGA+U), the equilibrium lattice constant a (in Å), the lattice constant c (in Å, for the tetragonal A-AFM case; null for cubic cells), the bulk modulus B (in GPa), its pressure derivative B' (dimensionless), and the Fe magnetic moment (in μ_B). The file must follow the specified schema (columns: configuration, method, a, c, B, B_prime, magnetic_moment_Fe). No other outputs are scored.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/pbe

## Workflow steps

### Step 1: Structure and input generation
- Role: process
- Action: Generate DFT input files (crystal structure, k-point sets, magnetic ordering) for each required configuration: non-magnetic (NF), ferromagnetic (FM), A-type antiferromagnetic (A-AFM), and G-type antiferromagnetic (G-AFM) of cubic BaFeO3, using the perovskite atomic positions and appropriate supercells to realize the spin arrangements.
- Evidence: `/app/outputs/input_files.zip`

### Step 2: Self-consistent field calculations over volumes
- Role: process
- Action: For every (configuration, functional) pair (GGA, LSDA+U, GGA+U), run SCF total-energy calculations at several lattice parameters to generate energy-volume data. Use Hubbard U=0.49 Ryd and J=0.07 Ryd for the +U functionals.
- Evidence: `/app/outputs/energy_volume.csv`

### Step 3: Extract structural properties and magnetic moments
- Role: scored (load-bearing)
- Action: Fit the Murnaghan equation of state to the energy-volume data to obtain equilibrium lattice constants (a, and c for the tetragonal A-AFM case), bulk modulus B, and pressure derivative B'. At the optimized lattice parameters, compute the Fe magnetic moments from the self-consistent spin density. Write all results to the CSV file.
- Output file: `/app/outputs/output_table_2_and_3.csv`
- Format: csv
- Contract: Columns: configuration (NF, FM, A-AFM, G-AFM), method (GGA, LSDA+U, GGA+U), a (float, Å), c (float, Å, null for cubic cells), B (float, GPa), B_prime (float, dimensionless), magnetic_moment_Fe (float, μ_B).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/output_table_2_and_3.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### output_table_2_and_3.csv
- path: `/app/outputs/output_table_2_and_3.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Reproduced structural parameters (lattice constants, bulk modulus) and Fe magnetic moments from DFT+U calculations, to be compared against paper-reported values with tolerances (±0.05 Å for lattice constants, ±5 GPa for bulk modulus, ±0.2 for B', ±0.2 μ_B for magnetic moments) by the hidden checker.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `method`, `a`, `c`, `B`, `B_prime`, `magnetic_moment_Fe`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `B`: GPa
    - `B_prime`: dimensionless
    - `magnetic_moment_Fe`: μ_B

Notes: The exact_match policy is used because the outputs are deterministic quantities with tolerances applied by the hidden checker; no 'better' direction exists.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "output_table_2_and_3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "method",
          "a",
          "c",
          "B",
          "B_prime",
          "magnetic_moment_Fe"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "B": "GPa",
          "B_prime": "dimensionless",
          "magnetic_moment_Fe": "μ_B"
        }
      },
      "description": "Reproduced structural parameters (lattice constants, bulk modulus) and Fe magnetic moments from DFT+U calculations, to be compared against paper-reported values with tolerances (±0.05 Å for lattice constants, ±5 GPa for bulk modulus, ±0.2 for B', ±0.2 μ_B for magnetic moments) by the hidden checker."
    }
  ],
  "notes": "The exact_match policy is used because the outputs are deterministic quantities with tolerances applied by the hidden checker; no 'better' direction exists."
}
```

## How you are scored
A hidden verifier reads the output_table_2_and_3.csv file and compares each reported numerical value against an independent hidden reference (the expected value for that property under identical conditions). The verifier checks that all required columns are present and correctly typed, then computes a reward based on the fraction of entries that fall within specified tolerances. The magnetic moment entries for the GGA+U G-AFM configuration carry extra weight. The final score is a value between 0 and 1. Simply reporting numbers that match the reference is not sufficient; they must result from genuine DFT calculations as described in the workflow steps. The verifier does not re-run the DFT calculations, so it trusts the submitted values but penalizes missing or malformed data.
