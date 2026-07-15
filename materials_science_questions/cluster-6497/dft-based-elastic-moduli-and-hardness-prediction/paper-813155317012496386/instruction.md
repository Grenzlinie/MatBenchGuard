# Group-wise B-n_e linear regression and alkali metal effective masses

## Problem background
The bulk modulus B of a solid reflects its resistance to uniform compression and is closely tied to the density of net-bonding valence electrons. This work explores an empirical linear relationship between B and the bulk electron concentration n_e for 59 elements, grouped by periodic column. From group-wise linear fits one can extract average valence bond strengths (AVBS) and, for the alkali metals, test the free-electron theory of metals by deriving effective electron masses.

## Approach
Compile published experimental data (bulk modulus B and atomic concentrations, Engel's net-bonding valence electrons Z) for 59 elements from the provided Table 1. Within each periodic Group (IA through VIB, excluding the transition metals Ti–Cu), perform ordinary least-squares linear regression of B versus n_e to obtain slope a and intercept b. Convert a to eV using the electron charge. For Group IA, where the fit passes through the origin, use the free-electron relation between B, n_e, and the Fermi energy ε_F^0, together with the theoretical expression ε_F^0 = (ħ²/(2 m_e))(3π² n_e)^(2/3), to compute empirical effective mass ratios m*/m = ε_F^0(theoretical) / ε_F^0(empirical) for Li, Na, K, Rb, Cs.

## Reproduction target
From the provided dataset of 59 elements, produce two CSV files: (i) `step_01_fit_parameters.csv` giving the slope a (in dyne·cm and eV) and intercept b (dyne/cm²) for the eight Groups IA, IIA, IIIA, IIB, IIIB, IVB, VB, VIB; (ii) `step_02_effective_masses.csv` giving the effective mass ratio m*/m for each alkali metal Li, Na, K, Rb, Cs. These numbers are derived solely from the tabulated n_e and B values and the free-electron formula.

## Assets

- Compiled dataset of 59 elements (Table 1)

## Workflow steps

### Step 1: Group-wise linear regression of B on n_e
- Role: scored (load-bearing)
- Action: Load the provided dataset of 59 elements (columns: element, structure, Engel's Z, n_a, BEC n_e in 10^22 cm⁻³, B in 10^12 dyne/cm², AVBS). Group elements by periodic Group as defined in the paper: IA (Li,Na,K,Rb,Cs), IIA (Be,Mg,Ca,Sr,Ba), IIIA (Sc,Y,La), IIB (Zn,Cd,Hg), IIIB (B,Al,Ga,In,Tl), IVB (C,Si,Ge,Sn,Pb), VB (P,As,Sb,Bi), VIB (S,Se,Te,Po). For each group, perform ordinary least-squares linear regression of B vs n_e (convert the reported units: n_e_actual = n_e_column * 1e22 cm⁻³, B_actual = B_column * 1e12 dyne/cm²). Extract slope a (dyne·cm) and intercept b (dyne/cm²). Convert slope a to eV by dividing by 1.602176634e-12 (1 eV in erg; 1 dyne·cm = 1 erg). Write a CSV file with columns: Group, a_dyne_cm, a_eV, b_dyne_cm2. Include all eight groups.
- Output file: `/app/outputs/step_01_fit_parameters.csv`
- Format: csv
- Contract: Columns: Group (string), a_dyne_cm (float), a_eV (float), b_dyne_cm2 (float). One row per Group (IA, IIA, IIIA, IIB, IIIB, IVB, VB, VIB).
- Scoring: scored by hidden verifier

### Step 2: Compute alkali metal effective masses
- Role: scored
- Action: From the Group IA fit in step_01, obtain slope a_eV (in eV). Compute the empirical Fermi energy ε_F^emp = 1.5 * a_eV (eV). For each alkali metal (Li, Na, K, Rb, Cs) extract its BEC n_e (in cm⁻³) from the dataset. Compute the theoretical free-electron Fermi energy ε_F^th = (ħ²/(2 m_e)) (3π² n_e)^(2/3) in eV, using m_e = 9.10956e-28 g, ħ = 1.0545718e-27 erg·s, n_e_actual in cm⁻³, and the conversion 1 eV = 1.602176634e-12 erg (1 erg = 1e-7 J). Then compute the effective mass ratio m*/m = ε_F^th / ε_F^emp. Write a CSV file with columns: Element, m_star_over_m.
- Output file: `/app/outputs/step_02_effective_masses.csv`
- Format: csv
- Contract: Columns: Element (string), m_star_over_m (float). One row per alkali metal: Li, Na, K, Rb, Cs.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_fit_parameters.csv`
- `/app/outputs/step_02_effective_masses.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_fit_parameters.csv
- path: `/app/outputs/step_01_fit_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Group-wise linear regression parameters (slope a in dyne·cm and eV, intercept b in dyne/cm²) for Groups IA through VIB.
- schema:
  - `type`: table
  - `required_columns`: `Group`, `a_dyne_cm`, `a_eV`, `b_dyne_cm2`
  - `units`:
    - `a_dyne_cm`: dyne·cm
    - `a_eV`: eV
    - `b_dyne_cm2`: dyne/cm^2

### step_02_effective_masses.csv
- path: `/app/outputs/step_02_effective_masses.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective mass ratio m*/m for Li, Na, K, Rb, Cs derived from the Group IA free-electron analysis.
- schema:
  - `type`: table
  - `required_columns`: `Element`, `m_star_over_m`
  - `units`:
    - `m_star_over_m`: dimensionless

Notes: The checker will compare the agent's fitted parameters and mass ratios to the paper's reported values within appropriate tolerances. The dataset used for fitting is the exact Table 1 from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_fit_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Group",
          "a_dyne_cm",
          "a_eV",
          "b_dyne_cm2"
        ],
        "units": {
          "a_dyne_cm": "dyne·cm",
          "a_eV": "eV",
          "b_dyne_cm2": "dyne/cm^2"
        }
      },
      "description": "Group-wise linear regression parameters (slope a in dyne·cm and eV, intercept b in dyne/cm²) for Groups IA through VIB."
    },
    {
      "file": "step_02_effective_masses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Element",
          "m_star_over_m"
        ],
        "units": {
          "m_star_over_m": "dimensionless"
        }
      },
      "description": "Effective mass ratio m*/m for Li, Na, K, Rb, Cs derived from the Group IA free-electron analysis."
    }
  ],
  "notes": "The checker will compare the agent's fitted parameters and mass ratios to the paper's reported values within appropriate tolerances. The dataset used for fitting is the exact Table 1 from the paper."
}
```

## How you are scored
A hidden verifier independently reads your output files and compares the fitted regression parameters and effective mass ratios against reference values for each Group and each metal. The two scored artifacts carry weights: the regression parameters (step_01) contribute 0.8 to the final reward, and the effective masses (step_02) contribute 0.2. The verifier checks numeric agreement within pre-set tolerances. Simply reporting correct numbers is not sufficient — your workflow must perform the actual linear regressions and free-electron calculations to produce the artifacts.
