# ThN and UN thermodynamic and magnetic bounds from specific heat

## Problem background
The specific heat of thorium mononitride (ThN) was measured from 7 to 300 K. The data are decomposed into electronic, lattice, and dilatation contributions. The extracted lattice parameters are then used in a corresponding-states scheme to estimate the magnetic and electronic specific heat of uranium mononitride (UN). The goal is to quantify the magnetic enthalpy and entropy bounds at the Néel temperature (52 K).

## Approach
The analysis proceeds in two stages. First, for ThN: the experimental specific heat data are corrected for the dilatation contribution using published thermophysical constants (compressibility, thermal expansion coefficient, atomic volume). The electronic contribution is subtracted using a linear term determined at low temperature. The remaining lattice specific heat is modelled as a sum of a Debye function for acoustic phonons and an Einstein function for optical phonons; the Einstein temperature is determined by fitting to the data, and the acoustic part is isolated. Thermodynamic functions (entropy, enthalpy increment, and Gibbs free energy function) are then obtained by numerical integration of the experimental specific heat from zero to 298.15 K. Second, for UN: the dilatation correction is computed from its own thermophysical constants. The acoustic lattice contribution is obtained by scaling the ThN acoustic part using the ratio of the two compounds’ Debye temperatures, and the optical contribution is computed with an Einstein function using an independently known Einstein temperature. These lattice contributions and the dilatation correction are subtracted from the experimental specific heat of UN to yield a residual C_M(T) + γ(T)T. This residual is integrated under two extreme assumptions about the temperature dependence of the electronic coefficient γ: (lower bound) γ remains constant from 0 to 52 K, and (upper bound) γ is reduced to 40% of its low-temperature value by 50 K. The resulting magnetic enthalpy and entropy at 52 K are reported as bounds.

## Reproduction target
Produce the thermodynamic functions of ThN at 298.15 K: entropy S (J/mol/K), enthalpy increment H-H0 (J/mol), and Gibbs free energy function -(G-H0) (J/mol). Produce lower and upper bounds for the magnetic enthalpy ΔH_M(52) (J/mol) and magnetic entropy ΔS_M(52) (J/mol/K) of UN. The required inputs are the provided ThN experimental specific heat data, the UN experimental specific heat data from Westrum & Barber (1966), and published thermophysical constants for both materials.

## Assets

- ThN experimental Cp data (Table 1)
- UN experimental Cp data: https://doi.org/10.1063/1.1728057
- ThN thermophysical constants (compressibility, thermal expansion coeff, atomic volume)
- UN thermophysical constants
- Python with NumPy and SciPy: numpy scipy

## Workflow steps

### Step 1: Compute ThN dilatation correction
- Role: process
- Action: Compute the temperature-dependent (Cp-Cv)d for ThN using published ThN material constants (compressibility, thermal expansion coefficient, atomic volume) and the approximate relation scaled at 300 K. Save the correction as evidence.
- Evidence: `/app/outputs/thn_dilatation_correction.csv`

### Step 2: Determine ThN Einstein temperature and extract acoustic contribution
- Role: process
- Action: Using the provided ThN experimental Cp data (Table 1), the low-temperature γ=3.12 mJ/mol/K², Debye temperature θD=284 K, and the dilatation correction from s01, subtract the electronic and dilatation contributions to isolate the lattice heat capacity. Fit an Einstein function to the optical part and extract the acoustic (Debye) contribution C_r1^ThN(T). Save the acoustic contribution as evidence.
- Evidence: `/app/outputs/thn_acoustic_contribution.csv`

### Step 3: Calculate ThN thermodynamic functions at 298.15 K
- Role: scored
- Action: Numerically integrate the provided ThN experimental Cp data from 0 to 298.15 K to obtain entropy S, enthalpy increment H-H0, and Gibbs free energy function -(G-H0). Write the results to the output file.
- Output file: `/app/outputs/thn_thermo.json`
- Format: json
- Contract: {"S": float (J/mol/K), "H_minus_H0": float (J/mol), "neg_G_minus_H0": float (J/mol)}
- Scoring: scored by hidden verifier

### Step 4: Compute UN dilatation correction
- Role: process
- Action: Compute the temperature-dependent (Cp-Cv)d for UN using published UN material constants (compressibility, thermal expansion coefficient, atomic volume) and the same approximate relation as in s01. Save the correction as evidence.
- Evidence: `/app/outputs/un_dilatation_correction.csv`

### Step 5: Compute UN lattice contributions
- Role: process
- Action: Take the ThN acoustic contribution from s02, scale it by the ratio of Debye temperatures (θD_UN = 291 K / θD_ThN = 284 K) to obtain the acoustic part for UN. Compute the optical contribution using an Einstein function with θE=547 K. Save the total lattice specific heat as evidence.
- Evidence: `/app/outputs/un_lattice_contributions.csv`

### Step 6: Extract magnetic+electronic residual and bound ΔH_M(52) and ΔS_M(52)
- Role: scored (load-bearing)
- Action: Obtain the experimental Cp data for UN from Westrum & Barber (1966). Subtract the lattice contributions from s05 and the dilatation correction from s04 to obtain the residual C_M(T)+γ(T)T. Under the lower-bound assumption (γ constant from 0–52 K), numerically integrate the residual to compute ΔH_M(52) and ΔS_M(52). Under the upper-bound assumption (γ reduced to 40% of its low-T value by 50 K), compute the upper bounds. Report all four values in the output file.
- Output file: `/app/outputs/un_magnetic_bounds.json`
- Format: json
- Contract: {"delta_H_M_lower": float (J/mol), "delta_H_M_upper": float (J/mol), "delta_S_M_lower": float (J/mol/K), "delta_S_M_upper": float (J/mol/K)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thn_thermo.json`
- `/app/outputs/un_magnetic_bounds.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thn_thermo.json
- path: `/app/outputs/thn_thermo.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic functions of ThN at 298.15 K: entropy, enthalpy increment, and negative Gibbs free energy function. Compared to paper-reported values with a relative tolerance.
- schema:
  - `type`: object
  - `required`: `S`, `H_minus_H0`, `neg_G_minus_H0`
  - `units`:
    - `S`: J/mol/K
    - `H_minus_H0`: J/mol
    - `neg_G_minus_H0`: J/mol

### un_magnetic_bounds.json
- path: `/app/outputs/un_magnetic_bounds.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Lower and upper bounds for magnetic enthalpy and magnetic entropy of UN at 52 K. The checker verifies that each bound falls within the paper's reported range.
- schema:
  - `type`: object
  - `required`: `delta_H_M_lower`, `delta_H_M_upper`, `delta_S_M_lower`, `delta_S_M_upper`
  - `units`:
    - `delta_H_M_lower`: J/mol
    - `delta_H_M_upper`: J/mol
    - `delta_S_M_lower`: J/mol/K
    - `delta_S_M_upper`: J/mol/K

Notes: The Schottky anomaly comparison is qualitative and not scored. All required material constants are obtainable from public literature; the ThN experimental Cp data is provided directly in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thn_thermo.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "S",
          "H_minus_H0",
          "neg_G_minus_H0"
        ],
        "units": {
          "S": "J/mol/K",
          "H_minus_H0": "J/mol",
          "neg_G_minus_H0": "J/mol"
        }
      },
      "description": "Thermodynamic functions of ThN at 298.15 K: entropy, enthalpy increment, and negative Gibbs free energy function. Compared to paper-reported values with a relative tolerance."
    },
    {
      "file": "un_magnetic_bounds.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "delta_H_M_lower",
          "delta_H_M_upper",
          "delta_S_M_lower",
          "delta_S_M_upper"
        ],
        "units": {
          "delta_H_M_lower": "J/mol",
          "delta_H_M_upper": "J/mol",
          "delta_S_M_lower": "J/mol/K",
          "delta_S_M_upper": "J/mol/K"
        }
      },
      "description": "Lower and upper bounds for magnetic enthalpy and magnetic entropy of UN at 52 K. The checker verifies that each bound falls within the paper's reported range."
    }
  ],
  "notes": "The Schottky anomaly comparison is qualitative and not scored. All required material constants are obtainable from public literature; the ThN experimental Cp data is provided directly in the instruction."
}
```

## How you are scored
Your submitted artifacts (thn_thermo.json and un_magnetic_bounds.json) will be evaluated by a hidden verifier. Each output is scored independently against a hidden reference that captures the expected physical result. The scores are combined by weight to produce a final reward in [0, 1]. Producing the correct numeric values within acceptable tolerances earns full credit; larger deviations reduce the score. Reporting numbers that merely match published values without performing the required computations will not suffice, because the verifier checks the outputs against reference values that are derived from a correct execution of the workflow, not from a simple lookup.
