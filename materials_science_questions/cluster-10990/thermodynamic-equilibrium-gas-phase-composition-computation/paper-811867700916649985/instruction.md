# Thermodynamic Equilibrium Gas-Phase C/Si Ratio Computation for SiC Sublimation

## Problem background
During silicon carbide (SiC) crystal growth by sublimation (Physical Vapor Transport, PVT) and related techniques, the gas-phase carbon-to-silicon (C/Si) ratio is a key parameter that influences doping, crystal quality, and growth stoichiometry. The composition of the vapor above solid SiC is determined by thermodynamic equilibrium; it can be modified by the choice of ambient atmosphere (e.g., inert argon, hydrogen, or chlorine) and by the total pressure. Understanding how the equilibrium C/Si ratio varies with temperature, pressure, and atmospheric additives is important for designing and controlling SiC crystal growth processes. In this task you will compute this equilibrium gas-phase C/Si ratio as a function of these parameters by performing thermodynamic calculations.

## Approach
You will perform Gibbs free energy minimisation for a system containing solid SiC(s) and an excess of the chosen atmosphere gas (Ar, H₂, or Cl₂). The equilibrium composition of the gas phase will be computed over a range of temperatures (1900–2500 °C) at two total pressures (4 mbar and 25 mbar) using the open-source chemical kinetics and thermodynamics solver Cantera, together with a suitable public thermochemical database that includes NASA polynomial coefficients for the relevant gas-phase species (e.g., Si, Si₂C, SiC₂, SiH, SiCl, SiCl₂, C₂H₂, C, Ar, H₂, Cl₂) and solid SiC. From the equilibrium mole fractions you will calculate the total gas-phase C/Si ratio, defined as the sum of carbon atoms in all gas species divided by the sum of silicon atoms in all gas species. The computation will cover 7 temperatures (every 100 °C), 2 pressures, and 3 atmospheres, producing a single table of results.

## Reproduction target
Produce a CSV file named c_si_ratio_vs_T.csv containing the computed C/Si ratio for each combination of temperature, pressure, and atmosphere. The file must include columns: Temperature_K (float, K), Pressure_mbar (float, mbar), Atmosphere (string, one of Ar, H2, Cl2), and C_Si_ratio (float, dimensionless). The hidden checker will verify that the ratio values are physically reasonable and that the relationships between different atmospheres and pressures follow expected qualitative trends (e.g., ordering between different gases, pressure effect).

## Assets

- Cantera: cantera
- Burcat Thermodynamic Database (or equivalent): ftp://ftp.technion.ac.il/pub/tsnissan/thermo/

## Workflow steps

### Step 1: Thermodynamic equilibrium computation of C/Si ratio
- Role: scored
- Action: Using Cantera (or an equivalent open-source Gibbs minimisation solver) and a public thermodynamic database that includes the species Si, Si2C, SiC2, SiH, SiCl, SiCl2, C2H2, C, Ar, H2, Cl2 and solid SiC, compute the equilibrium gas-phase composition for the system solid SiC(s) + excess atmosphere (Ar, H2 or Cl2) at total pressures 4 mbar and 25 mbar, over temperatures 1900–2500 °C in steps of ≤ 100 °C. For each condition, calculate the total C/Si ratio = (sum of C atoms in all gas-phase species) / (sum of Si atoms in all gas-phase species). Write the results to /app/outputs/c_si_ratio_vs_T.csv.
- Output file: `/app/outputs/c_si_ratio_vs_T.csv`
- Format: csv
- Contract: temperature_K (float), pressure_mbar (float), atmosphere (string, one of Ar, H2, Cl2), C_Si_ratio (float, dimensionless). One row per computed condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/c_si_ratio_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### c_si_ratio_vs_T.csv
- path: `/app/outputs/c_si_ratio_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the computed gas-phase C/Si ratio as a function of temperature, pressure, and atmosphere.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Pressure_mbar`, `Atmosphere`, `C_Si_ratio`
  - `units`:
    - `Temperature_K`: K
    - `Pressure_mbar`: mbar
    - `C_Si_ratio`: dimensionless

Notes: The checker will compare values and orderings against hidden reference data derived from the paper's Fig. 3; exact tolerances are not public.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "c_si_ratio_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Pressure_mbar",
          "Atmosphere",
          "C_Si_ratio"
        ],
        "units": {
          "Temperature_K": "K",
          "Pressure_mbar": "mbar",
          "C_Si_ratio": "dimensionless"
        }
      },
      "description": "Scored artifact containing the computed gas-phase C/Si ratio as a function of temperature, pressure, and atmosphere."
    }
  ],
  "notes": "The checker will compare values and orderings against hidden reference data derived from the paper's Fig. 3; exact tolerances are not public."
}
```

## How you are scored
A hidden verifier will read your c_si_ratio_vs_T.csv and compare the C_Si_ratio entries for all required conditions against a set of reference values derived from known thermodynamic data. It will also check that the computed values obey specific ordering relationships between atmospheres and pressures. The reward is binary: you receive full credit if all entries agree with the reference within a hidden tolerance and all required orderings are satisfied; otherwise zero. Your task is to correctly implement the equilibrium computation with the specified parameters; reporting the paper's numbers without genuine calculation will not pass the hidden checks.
