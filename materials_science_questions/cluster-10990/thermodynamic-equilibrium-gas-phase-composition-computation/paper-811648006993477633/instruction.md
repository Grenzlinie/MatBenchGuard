# Equilibrium Composition of Ar-H-N-Si-Cl System from Thermochemical Data

## Problem background
Plasma synthesis of ultrafine Si3N4 powders uses reactive quenching to suppress the formation of liquid silicon and to obtain high-nitrogen amorphous particles. Thermodynamic equilibrium analysis of the Ar-H-N-Si-Cl system clarifies why Si(l) can appear during cooling and how the NH3 injection rate influences the temperature range over which silicon condenses and the degree of Si(g) supersaturation. This task computes those equilibrium compositions from public thermochemical data, providing a quantitative basis for the experimental findings.

## Approach
Use a thermodynamic equilibrium solver (e.g., one based on Gibbs free energy minimization) together with publicly available JANAF thermochemical data for all species in the Ar-H-N-Si-Cl system. The system is treated at a constant total pressure of 1 atm. The inlet flows of Ar, H2, and SiCl4 are fixed, while the NH3 injection rate is varied across a set of values. For each NH3 flow, compute the equilibrium absolute mole numbers of every chemical species (gas and condensed phases) over a temperature grid from 300 K to 3500 K. Perform two calculation cases: (1) allowing the condensed phases Si(l) and Si3N4(s) to form; (2) assuming Si(l) does not appear (only Si3N4(s) is allowed). The results are collected into a single CSV table that provides the mole numbers at every temperature and condition. This table can then be used to derive the Si(l) existence temperature window and the maximum supersaturation ratio of Si(g) (P_Si(g)/P_sat_Si(g)), which characterize the thermodynamic barriers to pure Si3N4 formation.

## Reproduction target
Produce a CSV file, equilibrium_compositions.csv, containing the equilibrium absolute mole numbers of all relevant species in the Ar-H-N-Si-Cl system at 1 atm across the temperature range 300–3500 K. The file must cover all specified NH3 flow rates and both condensed-phase cases (with and without Si(l)). From this CSV the following derived quantities are expected to agree with known reference values: (a) the temperature interval where liquid Si is stable when Si(l) is allowed, and (b) the maximum Si(g) supersaturation ratio when Si(l) is suppressed. The task is considered successful if these derived quantities match the reference values within reasonable tolerances, with the strongest weight placed on the cases corresponding to the highest NH3 flow rate, and the correct qualitative trend of the Si(l) stability window as the NH3 flow changes.

## Assets

- JANAF Thermochemical Tables, 2nd Edition
- Open-source thermodynamics library (e.g., Cantera): cantera

## Workflow steps

### Step 1: Compute equilibrium compositions
- Role: scored (load-bearing)
- Action: Using publicly available JANAF thermochemical data and an equilibrium solver (e.g., Cantera), compute the equilibrium mole numbers of all species in the Ar-H-N-Si-Cl system at a total pressure of 1 atm, for temperatures from 300 K to 3500 K. Fix the inlet flows at Ar=40 L/min, H2=0.5 L/min, SiCl4=1 g/min, and vary the NH3 injection rate across the set {2.5, 5, 10, 15, 20} L/min. Perform two calculation cases for each flow: (1) allowing Si(l) and Si3N4(s) as possible condensed phases; (2) suppressing Si(l) and allowing only Si3N4(s). Write the resulting absolute mole numbers (not mole fractions) for every species at every temperature and condition into a single CSV file.
- Output file: `/app/outputs/equilibrium_compositions.csv`
- Format: csv
- Contract: CSV with columns: Q_NH3 (float, L/min), case (string, one of 'with_Si_liquid' or 'without_Si_liquid'), T_K (float, K), and one column per chemical species giving the absolute mole number at that equilibrium state. Expected species columns: Ar_mol, H2_mol, H_mol, N2_mol, N_mol, NH3_mol, NH4Cl_mol, HCl_mol, Cl2_mol, SiCl4_mol, SiCl2_mol, SiCl_mol, Si_g_mol, Si_l_mol (present only in rows with case='with_Si_liquid'), Si3N4_s_mol. All mole values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_compositions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_compositions.csv
- path: `/app/outputs/equilibrium_compositions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium mole numbers for the Ar-H-N-Si-Cl system at 1 atm, covering five NH3 injection rates, two condensed-phase cases, and a temperature grid from 300 K to 3500 K. The checker recomputes the Si(l) existence temperature window and the maximum Si(g) supersaturation ratio from this table, scoring against the paper's reported values.
- schema:
  - `type`: table
  - `required_columns`: `Q_NH3`, `case`, `T_K`, `Ar_mol`, `H2_mol`, `H_mol`, `N2_mol`, `N_mol`, `NH3_mol`, `NH4Cl_mol`, `HCl_mol`, `Cl2_mol`, `SiCl4_mol`, `SiCl2_mol`, `SiCl_mol`, `Si_g_mol`, `Si3N4_s_mol`
  - `units`:
    - `Q_NH3`: L/min
    - `T_K`: K
    - `all mole columns`: absolute moles

Notes: The checker recomputes derived quantities from the raw mole numbers; the agent does not need to supply the final metrics. Only the CSV is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_compositions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Q_NH3",
          "case",
          "T_K",
          "Ar_mol",
          "H2_mol",
          "H_mol",
          "N2_mol",
          "N_mol",
          "NH3_mol",
          "NH4Cl_mol",
          "HCl_mol",
          "Cl2_mol",
          "SiCl4_mol",
          "SiCl2_mol",
          "SiCl_mol",
          "Si_g_mol",
          "Si3N4_s_mol"
        ],
        "units": {
          "Q_NH3": "L/min",
          "T_K": "K",
          "all mole columns": "absolute moles"
        }
      },
      "description": "Equilibrium mole numbers for the Ar-H-N-Si-Cl system at 1 atm, covering five NH3 injection rates, two condensed-phase cases, and a temperature grid from 300 K to 3500 K. The checker recomputes the Si(l) existence temperature window and the maximum Si(g) supersaturation ratio from this table, scoring against the paper's reported values."
    }
  ],
  "notes": "The checker recomputes derived quantities from the raw mole numbers; the agent does not need to supply the final metrics. Only the CSV is scored."
}
```

## How you are scored
A hidden verifier reads your equilibrium_compositions.csv. It recomputes the Si(l) existence temperature range (for the case including Si(l)) and the maximum Si(g) supersaturation ratio (for the case excluding Si(l)) at each NH3 flow rate. These recomputed quantities are compared against reference targets using appropriate tolerances. The verifier also checks that the qualitative trend of the Si(l) stability window across different NH3 flow rates is correct. Your reward is a weighted combination of these comparisons; accurate reproduction of the derived quantities for the critical flow rates contributes most to the score. You do not need to supply the final metrics yourself—only the raw CSV is required, and the verifier evaluates it independently.
