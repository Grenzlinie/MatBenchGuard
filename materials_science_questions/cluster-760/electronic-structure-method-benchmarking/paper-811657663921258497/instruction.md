# Computation of transition-state geometries and reaction energetics for hydrogen-abstraction by chlorine using DFT methods

## Problem background
The hydrogen-atom abstraction by chlorine and related radicals is a fundamental reaction in organic chemistry and atmospheric science. Accurate computational prediction of transition-state geometries and reaction energetics is essential for understanding reactivity and kinetics, but standard electronic structure methods can be expensive. There is a need for reliable yet cost-effective density functional theory (DFT) protocols that can reproduce high-level benchmark results for these systems. This task reproduces the key quantum-chemical computations that benchmark various DFT procedures for hydrogen-abstraction reactions.

## Approach
The study evaluates the performance of several hybrid and double-hybrid DFT functionals by computing transition-state geometries and vibrationless barriers and reaction energies for a set of hydrogen-abstraction reactions. The theoretical approach involves:
- Geometry optimization of transition structures (first-order saddle points) and harmonic frequency analysis to confirm the nature of stationary points and extract imaginary frequencies.
- Single-point energy calculations on optimized geometries to obtain barriers and reaction energies.
Two hybrid functionals (BH&H-LYP and M05-2X) with the 6-31+G(d,p) basis set are used for the geometry optimization and harmonic frequency calculations. For energies, three method/basis combinations are used: M05-2X/6-31+G(d,p), M05-2X/aug-cc-pVTZ, and the double-hybrid functional DSD-B-LYP-D3/aug-cc-pVTZ. The computed quantities are compared against high-level coupled-cluster benchmarks to assess functional accuracy.

## Reproduction target
The goal is to produce two CSV files documenting the computed geometric and energetic results:
- `step_01_geometries.csv`: For reactions (1)–(5) (Cl• + CH₄, Cl• + CH₃NH₃⁺, Cl• + CH₃CHO, Cl• + CH₃CO₂H, Cl• + CH₃CO₂⁻), optimize transition structures with BH&H-LYP/6-31+G(d,p) and M05-2X/6-31+G(d,p) and compute harmonic frequencies. Record the interatomic distances Cl–H, H–C, Cl–C (in Å) and the imaginary frequency (in cm⁻¹) for each reaction and functional, yielding 10 rows.
- `step_03_energies.csv`: For reactions (1) and (6)–(10), where the abstracting radical is Cl•, F•, Br•, HO•, HOO•, and again Cl• from CH₃CHO, use BH&H-LYP/6-31+G(d,p) optimized geometries as reference and perform single-point energy calculations at the three method/basis combinations. Compute the vibrationless barrier (E_TS – sum(E_reactants)) and reaction energy (sum(E_products) – sum(E_reactants)) for each, providing 18 rows with reaction, method, basis, barrier (kJ/mol), and reaction_energy (kJ/mol).

## Assets

- Quantum chemistry software (ORCA, Psi4, or PySCF): https://www.orcasoftware.com/tutorials/ (ORCA); https://psicode.org/ (Psi4)

## Workflow steps

### Step 1: Transition structure optimization and frequency analysis for reactions (1)–(5)
- Role: scored
- Action: For reactions (1) Cl• + CH4 → ClH + •CH3, (2) Cl• + CH3NH3+ → ClH + •CH2NH3+, (3) Cl• + CH3CHO → ClH + •CH2CHO, (4) Cl• + CH3CO2H → ClH + •CH2CO2H, (5) Cl• + CH3CO2- → ClH + •CH2CO2-, construct initial transition-state guesses and perform geometry optimizations to locate the first-order saddle point using the BH&H-LYP and M05-2X functionals with the 6-31+G(d,p) basis set. After each optimization, run a harmonic frequency calculation at the same level to confirm the nature of the stationary point and extract the single imaginary frequency. Collect the key interatomic distances (Cl–H, H–C, Cl–C) and the imaginary frequency for each reaction/functional combination. Write the results to step_01_geometries.csv.
- Output file: `/app/outputs/step_01_geometries.csv`
- Format: csv
- Contract: columns: reaction (string), functional (string), Cl_H (float, Å), H_C (float, Å), Cl_C (float, Å), imag_freq (float, cm⁻¹). One row per (reaction, functional) combination (10 rows).
- Scoring: scored by hidden verifier

### Step 2: Geometry optimization of full reaction set (1),(6)–(10) with BH&H-LYP/6-31+G(d,p)
- Role: process
- Action: For reactions (1) and (6) F• + CH4 → FH + •CH3, (7) Br• + CH4 → BrH + •CH3, (8) HO• + CH4 → H2O + •CH3, (9) HOO• + CH4 → H2O2 + •CH3, (10) Cl• + CH3CHO → ClH + •CH2CHO, optimize the geometries of all reactants, products, and transition states using BH&H-LYP/6-31+G(d,p). Perform harmonic frequency analyses to confirm minima (all real frequencies) and transition states (exactly one imaginary frequency). Save the optimized geometries in a structured format (e.g., XYZ files) for use in the next step.
- Evidence: `/app/outputs/bhhlp_opt_geometries`

### Step 3: Single-point energy calculations for barriers and reaction energies
- Role: scored (load-bearing)
- Action: Using the BH&H-LYP/6-31+G(d,p) optimized geometries from step_02, compute single-point energies for all species involved in reactions (1) and (6)–(10) at three levels: M05-2X/6-31+G(d,p), M05-2X/aug-cc-pVTZ, and DSD-B-LYP-D3/aug-cc-pVTZ. Calculate the vibrationless barrier as E_TS - sum(E_reactants) and the vibrationless reaction energy as sum(E_products) - sum(E_reactants) for each reaction and level. Write the results to step_03_energies.csv.
- Output file: `/app/outputs/step_03_energies.csv`
- Format: csv
- Contract: columns: reaction (string), method (string), basis (string), barrier (float, kJ/mol), reaction_energy (float, kJ/mol). One row per (reaction, method, basis) combination (6 reactions × 3 combos = 18 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_geometries.csv`
- `/app/outputs/step_03_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_geometries.csv
- path: `/app/outputs/step_01_geometries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized transition-structure bond lengths and imaginary vibrational frequencies for reactions (1)–(5) computed with BH&H-LYP and M05-2X using the 6-31+G(d,p) basis set.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `functional`, `Cl_H`, `H_C`, `Cl_C`, `imag_freq`
  - `units`:
    - `Cl_H`: Å
    - `H_C`: Å
    - `Cl_C`: Å
    - `imag_freq`: cm⁻¹

### step_03_energies.csv
- path: `/app/outputs/step_03_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Vibrationless barriers and reaction energies for reactions (1) and (6)–(10) computed at three method/basis combinations on BH&H-LYP/6-31+G(d,p) optimized geometries.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `method`, `basis`, `barrier`, `reaction_energy`
  - `units`:
    - `barrier`: kJ/mol
    - `reaction_energy`: kJ/mol

Notes: The hidden checker compares the reported bond lengths and imaginary frequencies to the paper's DFT values for the same functionals, and the energies to the paper's benchmark URCCSD(T)/aug-cc-pVQZ values, using tolerances appropriate for computational chemistry re-runs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "functional",
          "Cl_H",
          "H_C",
          "Cl_C",
          "imag_freq"
        ],
        "units": {
          "Cl_H": "Å",
          "H_C": "Å",
          "Cl_C": "Å",
          "imag_freq": "cm⁻¹"
        }
      },
      "description": "Optimized transition-structure bond lengths and imaginary vibrational frequencies for reactions (1)–(5) computed with BH&H-LYP and M05-2X using the 6-31+G(d,p) basis set."
    },
    {
      "file": "step_03_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "method",
          "basis",
          "barrier",
          "reaction_energy"
        ],
        "units": {
          "barrier": "kJ/mol",
          "reaction_energy": "kJ/mol"
        }
      },
      "description": "Vibrationless barriers and reaction energies for reactions (1) and (6)–(10) computed at three method/basis combinations on BH&H-LYP/6-31+G(d,p) optimized geometries."
    }
  ],
  "notes": "The hidden checker compares the reported bond lengths and imaginary frequencies to the paper's DFT values for the same functionals, and the energies to the paper's benchmark URCCSD(T)/aug-cc-pVQZ values, using tolerances appropriate for computational chemistry re-runs."
}
```

## How you are scored
Your output will be evaluated by a hidden automated verifier that independently inspects each required CSV artifact. The verifier allocates a weight to each scored stage and checks:
- Existence, format, and schema compliance (correct columns, data types, and row count).
- For each reported numeric value, the verifier compares it against a hidden reference value with a tolerance that accounts for legitimate computational differences. The reward is computed as the fraction of values within the tolerance thresholds across all scored stages. Reporting the paper's own numbers without actual computation will not suffice, because the verifier checks the computed values. You must run the quantum chemistry simulations as described to obtain your own results.
