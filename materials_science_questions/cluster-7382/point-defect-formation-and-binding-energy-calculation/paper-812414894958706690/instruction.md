# Carbon activity isotherms for ThC_x using a two-site lattice-gas model

## Problem background
Thorium carbide (ThC_x) is a candidate fertile material for breeder reactor fuels. The chemical activity of carbon in non-stoichiometric ThC_x strongly influences fuel chemistry, fission-product behavior, and compatibility with cladding. Direct measurements of carbon activity over the full composition range are lacking, and existing indirect data are limited and contradictory. This task uses a statistical-mechanical lattice-gas model to predict the carbon activity as a function of composition and temperature, providing a theoretical baseline for the Th–C system. You will compute the activity isotherms numerically.

## Approach
The model treats carbon dissolution in thorium as a lattice gas on two kinds of sites: type-1 sites (octahedral interstices that can host single carbon atoms) and type-2 sites (additional sites that become available only next to an occupied type-1 site, allowing C₂ groups to form). Configurational entropy and interaction energies are evaluated within the Bragg–Williams (mean-field) approximation assuming random mixing. This yields coupled expressions for the carbon chemical potential, which—after absorbing vibrational contributions—give the carbon activity as a function of the site occupancies θ₁ and θ₂/θ₁. The equilibrium condition a_c(θ₁) = a_c(θ₂/θ₁), together with the total carbon content x = θ₁ + θ₂, is solved numerically for each (x, T) pair to obtain the equilibrium occupancies and the corresponding activity a_c. The required model parameters (pair interactions and thermodynamic constants) are fixed and are listed in the workflow step.

## Reproduction target
Compute the carbon activity a_c on a grid of total carbon content x ∈ {0.90, 0.95, 1.00, …, 1.95} (step 0.05) and temperature T ∈ {1173, 1473, 1773, 2073, 2373} K. For each (x, T) point, find the equilibrium site occupancies by solving the activity-equality condition numerically and evaluate a_c. Write all results to a CSV file at `/app/outputs/activity_isotherms.csv` with columns: x (composition), T (temperature in K), a_c (carbon activity). The file must contain exactly one row per (x, T) combination.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute carbon activity isotherms
- Role: scored (load-bearing)
- Action: Implement the two-site lattice-gas model with Bragg-Williams approximation for carbon activity in nonstoichiometric ThC_x. Use the parameter values (E11 = -3.918 kJ/mol, E22 = 5.887 kJ/mol, S_c^0 - S_{c,1}^M(vib) = 6.13 J/K·mol, E1 - H_c^0 = 154.3 kJ/mol, S_c^0 - S_{c,2}^M(vib) = 44.17 J/K·mol, E2 - H_c^0 = 78.30 kJ/mol) and coordination number c=12. For each temperature T in [1173, 1473, 1773, 2073, 2373] K and each total carbon content x from 0.90 to 1.95 (step 0.05), solve the equilibrium condition a_c(θ₁) = a_c(θ₂/θ₁) together with x = θ₁ + θ₂ using numerical root-finding. Compute the corresponding carbon activity a_c and write a CSV file with columns x, T, a_c.
- Output file: `/app/outputs/activity_isotherms.csv`
- Format: csv
- Contract: CSV table with columns: x (float, composition), T (float, temperature in K), a_c (float, carbon activity). Contains rows for all combinations of x ∈ {0.90, 0.95, …, 1.95} and T ∈ {1173, 1473, 1773, 2073, 2373}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activity_isotherms.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activity_isotherms.csv
- path: `/app/outputs/activity_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed carbon activity values for ThC_x at the specified grid of composition and temperature.
- schema:
  - `type`: table
  - `required_columns`: `x`, `T`, `a_c`
  - `description`: columns: x (float), T (float in K), a_c (float)

Notes: The hidden gold values are digitized from the paper's Figure 1. The checker compares each reported a_c against the corresponding gold using an absolute tolerance of 0.1 and relative tolerance of 15% (whichever is larger).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activity_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "T",
          "a_c"
        ],
        "description": "columns: x (float), T (float in K), a_c (float)"
      },
      "description": "Computed carbon activity values for ThC_x at the specified grid of composition and temperature."
    }
  ],
  "notes": "The hidden gold values are digitized from the paper's Figure 1. The checker compares each reported a_c against the corresponding gold using an absolute tolerance of 0.1 and relative tolerance of 15% (whichever is larger)."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/activity_isotherms.csv` and compares your reported a_c values against a reference dataset obtained by accurately solving the same model equations. For each (x, T) point the verifier checks whether your value agrees with the reference to within a pre-defined tolerance. Your final score is the fraction of points that pass this check. No other files or output are considered. The reference and tolerance are hidden and are not disclosed in this instruction.
