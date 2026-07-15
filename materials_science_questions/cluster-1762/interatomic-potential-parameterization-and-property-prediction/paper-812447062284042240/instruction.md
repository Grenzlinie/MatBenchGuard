# Multiple Ionization Thresholds and X-ray Energy per F-Centre in Alkali Halides

## Problem background
Alkali halide crystals develop colour centres (F-centres) when irradiated by X-rays. A key question is how many electrons must be temporarily removed from a halogen ion to allow it to be displaced interstitially, leaving a negative-ion vacancy that can trap an electron to form an F-centre. This number, p, depends on the balance between the electrostatic energy gained as the multiply-charged ion moves toward an interstitial site and the closed-shell repulsion it must overcome, modified by the polarisation energy of the surrounding lattice. Once p is found, one can estimate the average X-ray energy absorbed per F-centre formed by modelling the multiple-ionisation cross-sections of the halogen ions. At room temperature, the process becomes more complex: displaced halogen atoms migrate, interact with pre‑existing vacancies, and contribute to a slow volume expansion and continued F‑centre production over hours of irradiation. The goal is to compute these fundamental quantities—the ionisation threshold and the energy per centre—for seven common alkali halides, and to evaluate a simple room‑temperature model that predicts the linear dilatation and the concentration of negative‑ion vacancies after one hour of X‑irradiation.

## Approach
The computation proceeds in four stages. First, collect all required empirical constants: Born–Mayer exchange constants and ionic radii, the range parameter ρ, the Madelung constant, lattice distances, polarizabilities, ionisation energies, cross‑section ratios for double and triple ionisation, and the fixed parameters of the room‑temperature model. These are extracted from standard published compilations and are provided inline.

Second, for each halide, numerically solve an energy‑balance equation that equates the electrostatic energy gained by a multiply‑ionised anion as it passes through the first shell of neighbours (given by Madelung and geometry terms) to the closed‑shell repulsion energy from four neighbouring ions (using the Born–Mayer form, modified for incomplete shells) plus the change in lattice polarisation energy. The solution gives a non‑integral effective charge n; the integer threshold p is then taken as floor(n) + 1.

Third, the average X‑ray energy E_F (eV) absorbed per F‑centre is obtained from a multiple‑ionisation cross‑section model. The model expresses cross‑sections for p‑fold ionisation relative to single ionisation using known ratios s_p, and relates these to the atomic numbers, ionisation energies, and the mean energy of secondary electrons. The final expression for E_F depends on the halide composition, its first ionisation energy, the cross‑section ratio for the required p, and a factor accounting for secondary ionisations.

Fourth, a simple room‑temperature model for a typical NaCl‑like crystal is used. Displaced halogen atoms reach sub‑grain boundaries and cause dislocation climb, generating new vacancy pairs. The model yields the linear dilatation Δl/l and the negative‑ion vacancy concentration N_v after one hour, using fixed values for the initial vacancy concentration, dislocation spacing, and interstitial creation rate.

## Reproduction target
For the seven alkali halides LiF, NaF, KCl, NaCl, KBr, NaBr, and KI:

- Solve the energy‑balance equation to obtain the non‑integral charge n and the integer threshold p = floor(n) + 1. Save the results to `multiple_ionization_threshold.csv`.

- Using the cross‑section model and the appropriate p value for each halide, compute the average X‑ray energy E_F (eV) absorbed per F‑centre formed. Save the results to `energy_per_f_centre.csv`.

Additionally, for a generic NaCl‑like case, compute the linear dilatation Δl/l (dimensionless) and the negative‑ion vacancy concentration N_v (cm⁻³) after one hour of X‑irradiation, using the following room‑temperature model parameters: a0 = 3×10⁻⁸ cm, N0 = 2×10²² cm⁻³, a = 1×10⁻⁴ cm, c0 = 5×10⁻⁶, q = 4, β_i = 2×10¹⁶ cm⁻³ hr⁻¹, and t = 1 hr. Save the results to `room_temperature_model.csv`.

## Assets

- Python with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compile empirical parameters
- Role: process
- Action: Collect all required empirical parameters for the calculations: Born-Mayer exchange constants, ionic radii, range parameter ρ, Madelung constant, lattice distances, polarizabilities, ionization energies, cross-section ratios, and room-temperature model parameters. Write them to a structured JSON file for downstream steps.
- Evidence: `/app/outputs/prepared_parameters.json`

### Step 2: Solve energy-balance equation for multiple ionization threshold
- Role: scored
- Action: For each of the seven alkali halides LiF, NaF, KCl, NaCl, KBr, NaBr, KI, numerically solve the energy-balance equation (which balances electrostatic, polarization, and Born-Mayer repulsion terms) to find the non-integral positive charge n on the multiply-ionized anion, then determine the integer threshold p = floor(n)+1. Use the compiled parameters. Save the results to multiple_ionization_threshold.csv.
- Output file: `/app/outputs/multiple_ionization_threshold.csv`
- Format: csv
- Contract: CSV with columns: alkali_halide (string), n (float), p (integer). One row per halide: LiF, NaF, KCl, NaCl, KBr, NaBr, KI.
- Scoring: scored by hidden verifier

### Step 3: Compute X-ray energy per F-centre
- Role: scored (load-bearing)
- Action: Using a multiple-ionisation cross-section model (relating cross-section ratios to ionization energies and atomic numbers) and the compiled parameters, compute the average X-ray energy E_F (in eV) absorbed per F-centre formed for each of the seven alkali halides. Use the appropriate p value from the previous step. Save the results to energy_per_f_centre.csv.
- Output file: `/app/outputs/energy_per_f_centre.csv`
- Format: csv
- Contract: CSV with columns: alkali_halide (string), E_F (float, units eV). One row per halide.
- Scoring: scored by hidden verifier

### Step 4: Compute room-temperature linear dilatation and vacancy concentration
- Role: scored
- Action: For a typical NaCl-like case, compute the linear dilatation Δl/l and the negative-ion vacancy concentration N_v after one hour of X-irradiation using the room-temperature model. Use the following fixed parameters: a0 = 3e-8 cm, N0 = 2e22 cm⁻³, a = 1e-4 cm, c0 = 5e-6, q = 4, β_i = 2e16 cm⁻³ hr⁻¹, and t = 1 hr. Save the results to room_temperature_model.csv.
- Output file: `/app/outputs/room_temperature_model.csv`
- Format: csv
- Contract: CSV with columns: delta_l_over_l (float, dimensionless), N_v (float, units cm⁻³). Single row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/multiple_ionization_threshold.csv`
- `/app/outputs/energy_per_f_centre.csv`
- `/app/outputs/room_temperature_model.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### multiple_ionization_threshold.csv
- path: `/app/outputs/multiple_ionization_threshold.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Multiple ionization thresholds for seven alkali halides, computed from the energy-balance equation.
- schema:
  - `type`: table
  - `required_columns`: `alkali_halide`, `n`, `p`
  - `columns`:
    - `alkali_halide`: string
    - `n`: float
    - `p`: int
  - `notes`: n dimensionless; p integer threshold.

### energy_per_f_centre.csv
- path: `/app/outputs/energy_per_f_centre.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: X-ray energy per F-centre formed for each alkali halide.
- schema:
  - `type`: table
  - `required_columns`: `alkali_halide`, `E_F`
  - `columns`:
    - `alkali_halide`: string
    - `E_F`: float
  - `notes`: E_F in eV.

### room_temperature_model.csv
- path: `/app/outputs/room_temperature_model.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Linear dilatation and vacancy concentration from the room-temperature model.
- schema:
  - `type`: table
  - `required_columns`: `delta_l_over_l`, `N_v`
  - `columns`:
    - `delta_l_over_l`: float
    - `N_v`: float
  - `notes`: delta_l_over_l dimensionless; N_v in cm⁻³. Single row.

Notes: All empirical constants used are from published literature and will be provided inline in the instruction; no external datasets are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "multiple_ionization_threshold.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alkali_halide",
          "n",
          "p"
        ],
        "columns": {
          "alkali_halide": "string",
          "n": "float",
          "p": "int"
        },
        "notes": "n dimensionless; p integer threshold."
      },
      "description": "Multiple ionization thresholds for seven alkali halides, computed from the energy-balance equation."
    },
    {
      "file": "energy_per_f_centre.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alkali_halide",
          "E_F"
        ],
        "columns": {
          "alkali_halide": "string",
          "E_F": "float"
        },
        "notes": "E_F in eV."
      },
      "description": "X-ray energy per F-centre formed for each alkali halide."
    },
    {
      "file": "room_temperature_model.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_l_over_l",
          "N_v"
        ],
        "columns": {
          "delta_l_over_l": "float",
          "N_v": "float"
        },
        "notes": "delta_l_over_l dimensionless; N_v in cm⁻³. Single row."
      },
      "description": "Linear dilatation and vacancy concentration from the room-temperature model."
    }
  ],
  "notes": "All empirical constants used are from published literature and will be provided inline in the instruction; no external datasets are required."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently recomputes the results for each workflow stage. The verifier solves the energy‑balance equation numerically using the same embedded constants and checks the reported n (to within a tolerance) and p (must be exact). It recomputes E_F from the cross‑section model and compares values within a tolerance. For the room‑temperature model, it calculates Δl/l and N_v from the same fixed parameters and checks against your submitted numbers. Each scored artifact contributes a fraction of the total reward; the final score is a weighted combination. The verifier does not reveal its tolerances or reference values; simply reporting numbers without genuine computation will not succeed.
