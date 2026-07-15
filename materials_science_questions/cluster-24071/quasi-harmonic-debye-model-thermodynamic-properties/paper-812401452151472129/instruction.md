# Supercooled metallic liquid specific heat trend calculation

## Problem background
Supercooled metallic liquids can exhibit very different specific heat behaviour between the melting temperature Tm and the glass-transition temperature Tg. For systems with high glass-forming ability, measurements and extrapolations suggest that the constant-pressure specific heat Cp may increase monotonically as the temperature drops. For liquids that form glasses only with difficulty, a more complex dependence — an initial decrease followed by a rise near Tg — has been proposed. Because direct experimental access to the entire supercooled range is blocked by crystallisation, this problem is addressed here by first-principles thermodynamic calculations. The task is to compute Cp as a function of normalised temperature T/Tm for two model metals, Al and Rb, and to determine the resulting trend.

## Approach
The reproduction uses the Gibbs–Bogoliubov variational method with a hard-sphere reference system. The interionic pair potential is modelled by the Ashcroft empty-core pseudopotential, with core radii taken from standard literature (Al: 1.12 a.u., Rb: 1.31 a.u.). For each metal, the Helmholtz free energy F(T,Ω) is minimised with respect to the hard-sphere packing fraction to obtain the equilibrium atomic volume Ω(T) and internal energy E(T) across a grid of temperatures covering roughly 0.3Tm to Tm. From these results, the constant-volume specific heat CΩ, isothermal bulk modulus BT, and thermal expansion coefficient αp are computed numerically. Finally, the constant-pressure specific heat is obtained via Cp = CΩ + T Ω BT αp².

## Reproduction target
Compute the specific heat at constant pressure Cp (in units of Boltzmann constant per atom) for both supercooled Al and supercooled Rb at a set of normalised temperatures T/Tm spanning approximately 0.3 to 1.0. Write the results to a CSV file with columns system, T_Tm, and Cp_kB. The values for the two metals must be obtained from the same variational thermodynamic pipeline described in the workflow steps.

## Assets

- numpy: numpy
- scipy: scipy
- Ashcroft empty-core pseudopotential parameters for Al and Rb

## Workflow steps

### Step 1: Variational thermodynamic calculation
- Role: process
- Action: Implement the Gibbs–Bogoliubov variational method using a hard‑sphere reference system and Ashcroft empty‑core pseudopotentials. For each metal (Al, Rb), compute the Helmholtz free energy F(T,Ω) and internal energy E(T,Ω) by minimizing the variational bound to obtain equilibrium volume Ω(T) and internal energy E(T) at a grid of temperatures covering T/Tm from approximately 0.3 to 1.0.
- Evidence: none

### Step 2: Compute specific heat Cp and write trend data
- Role: scored (load-bearing)
- Action: From the variational results E(T) and Omega(T), numerically compute C_Omega = (dE/dT)_Omega, isothermal bulk modulus B_T, thermal expansion coefficient alpha_p, and finally Cp = C_Omega + T * Omega * B_T * alpha_p^2. Write a CSV file cp_trend.csv with columns: system (string, either 'Al' or 'Rb'), T_Tm (float, dimensionless ratio T/Tm), Cp_kB (float, Cp in units of Boltzmann constant). Include all computed temperature points.
- Output file: `/app/outputs/cp_trend.csv`
- Format: csv
- Contract: system (string), T_Tm (float), Cp_kB (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cp_trend.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cp_trend.csv
- path: `/app/outputs/cp_trend.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Specific heat at constant pressure as a function of normalized temperature for supercooled metallic liquids. The hidden verifier will inspect structural properties of the Cp data for each metal; exact trend criteria are not disclosed.
- schema:
  - `type`: table
  - `required_columns`: `system`, `T_Tm`, `Cp_kB`
  - `units`:
    - `Cp_kB`: kB per atom
    - `T_Tm`: dimensionless

Notes: Structural trends are checked with small tolerance intervals as documented in the hidden checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cp_trend.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "T_Tm",
          "Cp_kB"
        ],
        "units": {
          "Cp_kB": "kB per atom",
          "T_Tm": "dimensionless"
        }
      },
      "description": "Specific heat at constant pressure as a function of normalized temperature for supercooled metallic liquids. The hidden verifier will inspect structural properties of the Cp data for each metal; exact trend criteria are not disclosed."
    }
  ],
  "notes": "Structural trends are checked with small tolerance intervals as documented in the hidden checker."
}
```

## How you are scored
The hidden verifier inspects the structural properties of the Cp values in cp_trend.csv. It checks whether the data for each metal exhibits certain qualitative trends; the precise criteria are not disclosed. The raw Cp values are not compared to a specific paper‑reported number; the check is purely structural. Both metals carry equal weight in the final reward.
