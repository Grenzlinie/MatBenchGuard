# Sigma-Model Correlation Lengths and Gaps for Quantum Spin Ladders

## Problem background
Quantum spin ladders are systems of parallel spin chains coupled by inter-chain interactions. They exhibit a crossover between one-dimensional and two-dimensional quantum magnetism. The nonlinear sigma model is an effective continuum theory that captures the long-wavelength, low-energy properties of such systems. Using a one-loop reduction, one can derive analytic expressions for the spin correlation length and the spin gap as functions of the ladder width and temperature. This task validates the sigma-model description by computing these quantities for isotropic spin-1/2 Heisenberg ladders with periodic boundary conditions, using published macroscopic parameters.

## Approach
The sigma-model approach treats the ladder as a finite-width two-dimensional antiferromagnet. By integrating out fluctuations with momenta larger than the inverse width or inverse thermal length, one obtains effective lower-dimensional sigma models in different temperature regimes. At zero temperature, the effective coupling of a two-dimensional classical sigma model is computed from an integral over momentum and frequency. This yields a closed-form expression for the correlation length that depends on the ladder width and on the macroscopic spin stiffness and spin-wave velocity. The spin gap is then obtained from the correlation length via the relation expected from Lorentz invariance. At finite but low temperatures, the effective coupling acquires a temperature-dependent correction, and the gap is determined by numerically solving a self-consistent equation. All calculations use the input parameters (spin stiffness and spin-wave velocity) provided below; no external training or databases are needed beyond the specified numerical constants.

## Reproduction target
Compute the correlation length (in units of the lattice spacing a) and the spin gap (in units of J) for isotropic spin-1/2 Heisenberg ladders with periodic boundary conditions, using the macroscopic parameters ρ_s = 0.1800 J and ħc = 1.657 J a. At zero temperature, evaluate results for ladder leg numbers L_y = 4a and 6a. At finite temperatures T = 0.1, 0.2, 0.3 (in units of J), compute the correlation length for L_y = 2a, 4a, 6a and the gap where defined. Assemble all results into a single CSV file at '/app/outputs/correlation_gap_results.csv' with columns: legs (integer), temperature (float, in units of J), correlation_length (float, in units of a), gap (float, in units of J). Include rows for T=0 legs 4 and 6, and rows for T=0.1,0.2,0.3 legs 2,4,6. The gap column may be left empty (NaN) for rows where the gap is not defined; the correlation_length must be present for all rows.

## Assets

- Macroscopic sigma-model parameters from Beard et al.: 10.1103/PhysRevLett.80.1742
- Python scientific computing libraries: numpy, scipy

## Workflow steps

### Step 1: Compute correlation lengths and spin gaps
- Role: scored (load-bearing)
- Action: Implement the nonlinear sigma-model reduction using the provided macroscopic parameters (spin stiffness and spin-wave velocity). At zero temperature, evaluate the appropriate integral to obtain the effective coupling, then compute the correlation length and the spin gap for ladder leg numbers 4 and 6 (periodic boundary conditions). For finite temperatures T = 0.1, 0.2, 0.3 (in units of the intrachain coupling J), compute the temperature-dependent effective coupling and numerically solve the self-consistent gap equation to find the spin gap and correlation length for leg numbers 2, 4, and 6. Assemble all results into a single CSV file.
- Output file: `/app/outputs/correlation_gap_results.csv`
- Format: csv
- Contract: Columns: legs (integer, number of legs), temperature (float, in units of J), correlation_length (float, in units of lattice spacing a), gap (float, in units of J). Rows for T=0 legs 4,6; T=0.1,0.2,0.3 legs 2,4,6. Gap may be omitted (NaN or empty) for rows where it is not defined; correlation_length must be present for all rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlation_gap_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlation_gap_results.csv
- path: `/app/outputs/correlation_gap_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed correlation lengths and spin gaps. The checker compares the values against hidden reference values derived from the paper (Table 1 for T=0, Fig. 3 for finite T) within predefined tolerances, and also checks that the computed quantities are physically consistent with the sigma-model predictions (e.g., trends with leg number and temperature).
- schema:
  - `type`: table
  - `required_columns`: `legs`, `temperature`, `correlation_length`, `gap`
  - `units`:
    - `temperature`: J
    - `correlation_length`: lattice spacing a
    - `gap`: J

Notes: Only the even-legged isotropic cases are required. The gap column may contain NaN for rows where the gap is not defined (e.g., certain finite-temperature 2-leg cases).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlation_gap_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "legs",
          "temperature",
          "correlation_length",
          "gap"
        ],
        "units": {
          "temperature": "J",
          "correlation_length": "lattice spacing a",
          "gap": "J"
        }
      },
      "description": "Computed correlation lengths and spin gaps. The checker compares the values against hidden reference values derived from the paper (Table 1 for T=0, Fig. 3 for finite T) within predefined tolerances, and also checks that the computed quantities are physically consistent with the sigma-model predictions (e.g., trends with leg number and temperature)."
    }
  ],
  "notes": "Only the even-legged isotropic cases are required. The gap column may contain NaN for rows where the gap is not defined (e.g., certain finite-temperature 2-leg cases)."
}
```

## How you are scored
A hidden verifier will read your submitted CSV file and compare the computed correlation lengths and gaps against reference values derived from the paper's sigma-model predictions. The verifier does not require you to match a particular table or figure; it checks that your computed quantities are physically consistent with the sigma-model approach. Full credit is assigned when all values lie within tolerance and the required trends are satisfied.
