# Repulsive Potential Parameterization and Property Prediction for Alkali Halides

## Problem background
Ionic compounds such as alkali halides exhibit strong Coulombic, polarization, dispersion, and short-range repulsive interactions. A fundamental challenge is to design an interatomic potential that captures both molecular and crystalline properties with a single consistent repulsive form. This work investigates a short-range overlap repulsive interaction ψ(r) = (P'/r^2) exp(-b' r^N) embedded in a modified Rittner-model potential. The goal is to compute molecular spectroscopic constants (binding energy, rotation-vibration coupling constant, vibrational anharmonicity constant) and crystal properties (cohesive energy, bulk modulus) for twenty alkali halide molecules and crystals and to assess how well the model reproduces experimental measurements.

## Approach
The interaction potential for a diatomic molecule is built from four contributions: (i) Coulomb attraction, (ii) polarization energy depending on distance-dependent ionic polarizabilities, (iii) van der Waals dipole-dipole energy, and (iv) a short-range repulsive term ψ(r) = (P'/r^2) exp(-b' r^N). Ionic polarizabilities are obtained via Ruffa's theory from published free-ion polarizabilities; the van der Waals coefficient is evaluated with the Slater-Kirkwood formula. The repulsive parameters P' and b' are fitted molecule-by-molecule by solving the equilibrium conditions at the experimental bond length and force constant. The exponent N is set by a correlation rule that depends on the valence electrons of the constituent atoms. With the fitted potential, the binding energy, rotation-vibration coupling constant, and vibrational anharmonicity constant are calculated from the potential and its derivatives at equilibrium. For the crystalline state, the same repulsive form is extended to all ion pairs. Hardness parameters for cation-anion, cation-cation, and anion-anion interactions are derived from empirical schemes that use the molecular hardness b' and a structure constant. The repulsive strength parameter P is then determined from the crystal equilibrium condition at the experimental interionic distance. Cohesive energy and bulk modulus are computed both with nearest-neighbor repulsion only and including next-nearest-neighbor interactions.

## Reproduction target
For each of the twenty alkali halides (LiF, LiCl, LiBr, LiI, NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI, RbF, RbCl, RbBr, RbI, CsF, CsCl, CsBr, CsI), compute the molecular binding energy (kcal/mol), rotation-vibration coupling constant (10^-4 cm^-1), and vibrational anharmonicity constant (cm^-1) from the fitted potential, and compute the crystalline repulsive hardness parameter b_+- (10^12 cm^-1), cohesive energy (kcal/mol) and bulk modulus (10^12 dyne/cm^2) both without and with next-nearest-neighbor repulsion. Report all results in two CSV files: molecular_properties.csv and crystal_properties.csv with columns as specified in the workflow steps.

## Assets

- Experimental equilibrium distances r_e and force constants k_e for 20 alkali halides
- Free-ion polarizabilities for alkali and halogen ions
- Effective numbers of electrons N1, N2 for van der Waals coefficient calculation
- Van der Waals coefficients C and D for crystalline state
- Experimental crystal interionic distances r0 for alkali halide crystals
- Madelung constant A for NaCl- and CsCl-type structures

## Workflow steps

### Step 1: Compute electronic polarizabilities and van der Waals coefficient
- Role: process
- Action: Using free-ion polarizabilities from Tessmann et al. and effective electron numbers from Shanker et al., compute the cation and anion polarizabilities α1, α2 as functions of interionic distance r via Ruffa's theory, and compute the van der Waals dipole-dipole coefficient c via the Slater-Kirkwood formula. These are needed later to construct the total potential.
- Evidence: none

### Step 2: Fit repulsive potential parameters P' and b' from molecular data
- Role: process
- Action: For each of the 20 alkali halide molecules, using experimental equilibrium distance r_e and force constant k_e, solve the equilibrium condition (dU/dr=0) and force constant condition (d²U/dr² = k_e) simultaneously for the parameters P' and b'. The exponent N is determined from valence electron correlation rules. The total potential U(r) includes electrostatic, polarization, van der Waals, and repulsive terms. This yields fitted P' and b' for each molecule.
- Evidence: none

### Step 3: Compute molecular state properties
- Role: scored (load-bearing)
- Action: Using the total potential with the fitted parameters from step_02, compute the molecular binding energy D_i = -U(r_e), rotation-vibration coupling constant α_e, and vibrational anharmonicity constant ω_e x_e for all 20 alkali halide molecules. Required additional inputs: experimental rotational constant B_e and vibrational frequency ω_e.
- Output file: `/app/outputs/molecular_properties.csv`
- Format: csv
- Contract: Columns: Molecule (string), Di_calc (float, kcal/mol), alpha_e_calc (float, 10^-4 cm^-1), wexe_calc (float, cm^-1).
- Scoring: scored by hidden verifier

### Step 4: Compute crystalline state properties
- Role: scored
- Action: Extend the model to crystals: using the molecular repulsive hardness parameter b' from step_02 and empirical relations (cation-cation and anion-anion hardness), determine repulsive hardness parameters for all ion pairs. Fix the repulsive strength parameter P from the crystal equilibrium condition (dW/dr=0) using experimental interionic distance r0. Compute cohesive energy W and bulk modulus B_T for each crystal, both without next-nearest-neighbor (NNN) interactions (using only ψ_+-) and with NNN interactions (including ψ_++ and ψ_--). Use Madelung constant and van der Waals coefficients C, D.
- Output file: `/app/outputs/crystal_properties.csv`
- Format: csv
- Contract: Columns: Crystal (string), b_plus_minus (float, 10^12 cm^-1), W_calc_NN (float, kcal/mol), W_calc_NNN (float, kcal/mol), BT_calc_NN (float, 10^12 dyne/cm^2), BT_calc_NNN (float, 10^12 dyne/cm^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/molecular_properties.csv`
- `/app/outputs/crystal_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### molecular_properties.csv
- path: `/app/outputs/molecular_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed molecular binding energy, rotation-vibration coupling constant, and vibrational anharmonicity constant for each of the 20 alkali halide molecules. The checker will compare against hidden experimental references.
- schema:
  - `type`: table
  - `required_columns`: `Molecule`, `Di_calc`, `alpha_e_calc`, `wexe_calc`
  - `units`:
    - `Di_calc`: kcal/mol
    - `alpha_e_calc`: 10^-4 cm^-1
    - `wexe_calc`: cm^-1

### crystal_properties.csv
- path: `/app/outputs/crystal_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed repulsive hardness parameter, cohesive energy (without and with NNN), and bulk modulus (without and with NNN) for each alkali halide crystal. The checker will compare against hidden experimental references.
- schema:
  - `type`: table
  - `required_columns`: `Crystal`, `b_plus_minus`, `W_calc_NN`, `W_calc_NNN`, `BT_calc_NN`, `BT_calc_NNN`
  - `units`:
    - `b_plus_minus`: 10^12 cm^-1
    - `W_calc_NN`: kcal/mol
    - `W_calc_NNN`: kcal/mol
    - `BT_calc_NN`: 10^12 dyne/cm^2
    - `BT_calc_NNN`: 10^12 dyne/cm^2

Notes: The checker will compute average percentage deviations for each property across all molecules/crystals and compare them to hidden tolerances derived from the paper's reported deviations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "molecular_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Molecule",
          "Di_calc",
          "alpha_e_calc",
          "wexe_calc"
        ],
        "units": {
          "Di_calc": "kcal/mol",
          "alpha_e_calc": "10^-4 cm^-1",
          "wexe_calc": "cm^-1"
        }
      },
      "description": "Computed molecular binding energy, rotation-vibration coupling constant, and vibrational anharmonicity constant for each of the 20 alkali halide molecules. The checker will compare against hidden experimental references."
    },
    {
      "file": "crystal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Crystal",
          "b_plus_minus",
          "W_calc_NN",
          "W_calc_NNN",
          "BT_calc_NN",
          "BT_calc_NNN"
        ],
        "units": {
          "b_plus_minus": "10^12 cm^-1",
          "W_calc_NN": "kcal/mol",
          "W_calc_NNN": "kcal/mol",
          "BT_calc_NN": "10^12 dyne/cm^2",
          "BT_calc_NNN": "10^12 dyne/cm^2"
        }
      },
      "description": "Computed repulsive hardness parameter, cohesive energy (without and with NNN), and bulk modulus (without and with NNN) for each alkali halide crystal. The checker will compare against hidden experimental references."
    }
  ],
  "notes": "The checker will compute average percentage deviations for each property across all molecules/crystals and compare them to hidden tolerances derived from the paper's reported deviations."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores the two output artifacts. The verifier compares the computed molecular properties (binding energy, α_e, ω_e x_e) in molecular_properties.csv and the computed crystal properties (cohesive energy, bulk modulus with and without NNN) in crystal_properties.csv to experimentally derived reference values that are kept hidden. The scoring combines weighted average deviations across all molecules and crystals into a final reward in [0,1]. Simply reporting the paper's published values or guessing will not pass; you must genuinely implement the computational pipeline described above. The exact tolerances and weighting are hidden.
