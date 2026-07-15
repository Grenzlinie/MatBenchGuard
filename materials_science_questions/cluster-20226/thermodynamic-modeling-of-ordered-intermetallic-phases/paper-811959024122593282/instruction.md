# Configurational Entropy Model for Solid Solution Electrode Materials

## Problem background
Solid solution electrodes used in batteries exhibit composition-dependent voltage (emf) determined by the chemical potential of the mobile ionic species. In superionic conductors with large carrier concentrations, configurational entropy often dominates the variation of partial thermodynamic properties (partial molar entropy, enthalpy, chemical potential) with composition. Computing these quantities from a simple site-occupancy model provides insight into the electrochemical behavior of the material. This task implements a lattice-site statistical model in which mobile Cu+ ions occupy two types of crystallographic sites with single-occupancy constraints, leading to a Fermi-Dirac distribution of occupancies, and computes the resulting configurational entropy, internal energy, chemical potential, and partial molar quantities as functions of composition.

## Approach
The thermodynamic model treats a unit cell containing two types of crystallographic sites for the mobile ions: type A with g_A equivalent sites at energy u_A, and type B with g_B equivalent sites at energy u_B, each site accommodating at most one ion. Given a total number of ions per unit cell x, the site occupancies follow a Fermi-Dirac distribution: n_j = g_j / [exp((u_j − μ)/kT) + 1], where μ is the ionic chemical potential. For a desired x, μ is determined by numerically solving the equation Σ n_j = x. From the occupancies one computes the configurational entropy S = k Σ [g_j ln g_j − n_j ln n_j − (g_j − n_j) ln(g_j − n_j)] and the configurational internal energy U = Σ n_j u_j. Partial molar entropy S̄ = dS/dx and partial molar enthalpy H̄ ≈ dU/dx are obtained by finite differences between closely spaced compositions.

Apply this model to the specific two-site system representing Cu_xMo6S8-y: g_A = 2 (Cu(A) sites), g_B = 4 (Cu(B) sites), and an energy gap u_B − u_A = 5RT at temperature T = 400 K. Use the gas constant R = 8.314 J/(mol·K) and compute the quantities for compositions x from 0.0 to 4.0 in steps of 0.1.

## Reproduction target
Implement the ionic configurational entropy model for a two-site system with site multiplicities g_A = 2, g_B = 4, energy gap u_B − u_A = 5RT, and temperature T = 400 K. For each target total Cu content x from 0.0 to 4.0 in steps of 0.1, numerically solve for the chemical potential μ such that the sum of the Fermi-Dirac occupancies equals x. Compute the site occupancies n_A and n_B, the configurational entropy S, configurational internal energy U, the ionic chemical potential μ, and the partial molar quantities S̄ = dS/dx and H̄ = dU/dx via finite differences. Output the results as a CSV file with columns: x, n_A, n_B, S, U, mu, S_bar, H_bar. Ensure S and U are reported per unit cell and mu, S_bar, H_bar are per mole of Cu (using R = 8.314 J/(mol·K)).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute configurational entropy model for Cu_xMo6S8-y
- Role: scored (load-bearing)
- Action: Implement the configurational entropy model for mobile ions in a solid solution electrode using the Fermi-Dirac site occupancy formalism. Given site multiplicities g_j and site energies u_j, for a target total ion content x, numerically solve for the chemical potential μ such that the sum of occupancies matches the target. Compute site occupancies, configurational entropy S, and configurational internal energy U using the standard combinatorial expressions. Obtain partial molar quantities S̄ and H̄ via finite differences. Apply the model to a two-site system with g1=2, g2=4, energy gap u2 - u1 = 5RT, and temperature T=400 K. Compute results for total ion content x from 0.0 to 4.0 in steps of 0.1. Use R=8.314 J/(mol·K). Output the computed quantities to a CSV file.
- Output file: `/app/outputs/step_01_cu_model.csv`
- Format: csv
- Contract: CSV with columns: x (float), n_A (float), n_B (float), S (float, J per unit cell), U (float, J per unit cell), mu (float, J/mol), S_bar (float, J/(mol·K)), H_bar (float, J/mol). 41 rows covering x from 0.0 to 4.0 in steps of 0.1. Values formatted with standard floating-point precision (e.g., 6 decimal places).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_cu_model.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_cu_model.csv
- path: `/app/outputs/step_01_cu_model.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing computed thermodynamic quantities of the ionic configurational model as a function of composition x. The checker will re-implement the same model and compare each field against its own reference values within a numerical tolerance.
- schema:
  - `type`: table
  - `required_columns`: `x`, `n_A`, `n_B`, `S`, `U`, `mu`, `S_bar`, `H_bar`
  - `units`:
    - `S`: J per unit cell
    - `U`: J per unit cell
    - `mu`: J/mol
    - `S_bar`: J/(mol*K)
    - `H_bar`: J/mol

Notes: The model includes only ionic configurational contributions. Electronic contributions are not included. The computed chemical potential μ is the ionic chemical potential.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_cu_model.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "n_A",
          "n_B",
          "S",
          "U",
          "mu",
          "S_bar",
          "H_bar"
        ],
        "units": {
          "S": "J per unit cell",
          "U": "J per unit cell",
          "mu": "J/mol",
          "S_bar": "J/(mol*K)",
          "H_bar": "J/mol"
        }
      },
      "description": "CSV file containing computed thermodynamic quantities of the ionic configurational model as a function of composition x. The checker will re-implement the same model and compare each field against its own reference values within a numerical tolerance."
    }
  ],
  "notes": "The model includes only ionic configurational contributions. Electronic contributions are not included. The computed chemical potential μ is the ionic chemical potential."
}
```

## How you are scored
A hidden verifier independently re-implements the same configurational entropy model with identical parameters to compute reference values for every field in the output CSV. It compares your submitted CSV row by row and column by column against the reference using a pre-determined numerical tolerance. Your overall score is the fraction of fields that fall within that tolerance. The verifier may also check that the partial molar quantities exhibit the expected qualitative behavior (e.g., the partial molar entropy peaks near a certain composition). You do not need to reproduce any external table; only the self-consistent output of the model defined by the given parameters is evaluated.
