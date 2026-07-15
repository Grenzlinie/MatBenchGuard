# Thermodynamic function derivation from experimental enthalpy data

## Problem background
Rare-earth germanides are candidate materials for semiconductor and optical applications; their thermodynamic stability and phase-transition behavior are critical for processing and performance. The central quantity of interest is the temperature dependence of their enthalpy, heat capacity, entropy, and reduced Gibbs free energy. These functions can be derived from experimental enthalpy-increment measurements by fitting compact empirical equations and then computing phase-transformation enthalpies and entropies.

## Approach
The workflow uses published experimental enthalpy-increment data (H(T)−H(298.15 K)) for three gadolinium germanide compounds, measured over a wide temperature range spanning solid and liquid phases. For each solid phase, the data are fitted to the Mayer–Kelly form H(T) = A T² + B T + C/T + D by a constrained least-squares procedure that enforces H(298.15)=0 and the known standard heat capacity at 298.15 K (Cp298). For each liquid phase, a linear equation H(T) = a T + b is fitted with H(298.15)=0. Once the coefficients are obtained, the entropy integration constant E for solid phases is determined so that S(298.15) matches the known standard entropy (S298). The necessary Cp298 and S298 values are given as fixed constants in this instruction.

- Gd5Ge3: Cp298 = 213.50 J·K⁻¹·mol⁻¹, S298 = 443.8 J·K⁻¹·mol⁻¹
- GdGe: Cp298 = 48.87 J·K⁻¹·mol⁻¹, S298 = 89.9 J·K⁻¹·mol⁻¹
- GdGe1.5: Cp298 = 61.90 J·K⁻¹·mol⁻¹, S298 = 98.3 J·K⁻¹·mol⁻¹ Phase transformation temperatures are identified from the experimental data as the midpoints of the temperature intervals where the enthalpy exhibits jumps. The fitted solid and liquid equations are then extrapolated to these temperatures to compute the transformation enthalpy (ΔH) and the corresponding entropy (ΔS = ΔH/T).

## Reproduction target
Produce two comma-separated files:
1. fitted_coefficients.csv: contains the fitted coefficients (A, B, C, D, E for solid phases and a, b for liquid phases) for each compound and phase as specified in the output contract.
2. phase_transformations.csv: contains the melting temperature, enthalpy, and entropy for Gd5Ge3 and GdGe, and both polymorphic transformations (near 1114 K and 1442 K) and the melting transformation for GdGe1.5. All transformation properties must be computed from the fitted equations; the values are compared against independently derived reference results.

## Assets

- Experimental enthalpy data CSV
- Python scientific libraries (numpy, scipy, pandas): numpy, scipy, pandas

## Workflow steps

### Step 1: Fit enthalpy functions and derive thermodynamic coefficients
- Role: scored (load-bearing)
- Action: Load the provided experimental enthalpy data CSV. Using the specified standard heat capacities at 298.15 K (Cp298) and standard entropies at 298.15 K (S298) for each compound (given in the instruction), perform constrained least-squares fitting: for each solid phase, fit the Mayer-Kelly equation H(T)-H(298.15) = A T^2 + B T + C/T + D with constraints H(298.15)=0 and dH/dT(298.15)=Cp298. For each liquid phase, fit a linear equation H = a T + b with H(298.15)=0 constraint. For solid phases, compute the entropy integration constant E such that S(298.15)=S298. Output all coefficients (A, B, C, D, E, a, b) for each compound and phase as specified in the output schema.
- Output file: `/app/outputs/fitted_coefficients.csv`
- Format: csv
- Contract: CSV with columns: phase (string, e.g., 'Gd5Ge3_solid', 'Gd5Ge3_liquid', 'GdGe_solid', 'GdGe_liquid', 'alpha_GdGe1.5', 'beta_GdGe1.5', 'gamma_GdGe1.5', 'GdGe1.5_liquid'), A (float), B (float), C (float), D (float), E (float), a (float), b (float). For liquid phases, A, B, C, D, E may be empty or NaN; for solid phases, a, b may be empty or NaN.
- Scoring: scored by hidden verifier

### Step 2: Compute phase transformation temperatures, enthalpies, and entropies
- Role: scored
- Action: From the experimental enthalpy data, identify the temperature intervals where jumps (discontinuities) indicate phase transformations (melting and the two polymorphic transformations in GdGe1.5). Determine the transformation temperature as the midpoint of each jump interval. Then, using the fitted solid and liquid enthalpy equations from the previous step, compute the enthalpy change of each transformation by evaluating the enthalpy difference of the two phases at the transformation temperature. Compute the entropy change as ΔH/T. For Gd5Ge3 and GdGe, compute only the melting transformation. For GdGe1.5, compute the two polymorphic transformations (at ~1114 K and ~1442 K) and the melting transformation. Output all transformation properties as specified.
- Output file: `/app/outputs/phase_transformations.csv`
- Format: csv
- Contract: CSV with columns: compound (string, one of 'Gd5Ge3', 'GdGe', 'GdGe1.5'), transformation_type (string, 'melting' or 'polymorphic'), temperature_K (float), deltaH_kJ_per_mol (float), deltaS_J_per_K_per_mol (float). For GdGe1.5, include two polymorphic rows (at ~1114 K and ~1442 K) and one melting row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_coefficients.csv`
- `/app/outputs/phase_transformations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_coefficients.csv
- path: `/app/outputs/fitted_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted coefficients of the Mayer-Kelly equation for solid phases and linear equation for liquid phases, and the entropy integration constant E.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `A`, `B`, `C`, `D`, `E`, `a`, `b`
  - `units`: object

### phase_transformations.csv
- path: `/app/outputs/phase_transformations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase transformation properties (melting and polymorphic) for the three compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `transformation_type`, `temperature_K`, `deltaH_kJ_per_mol`, `deltaS_J_per_K_per_mol`
  - `units`:
    - `temperature_K`: K
    - `deltaH_kJ_per_mol`: kJ/mol
    - `deltaS_J_per_K_per_mol`: J/(K·mol)

Notes: The task reproduces the computational derivation of thermodynamic coefficients and phase transformation properties from published experimental enthalpy data. All required numerical constants (Cp298, S298) are provided in the instruction. The scored artifacts correspond to Tables 3 and 4 of the source, but the agent must compute them from the provided experimental data and boundary conditions, not extract them from the paper text.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "A",
          "B",
          "C",
          "D",
          "E",
          "a",
          "b"
        ],
        "units": {}
      },
      "description": "Fitted coefficients of the Mayer-Kelly equation for solid phases and linear equation for liquid phases, and the entropy integration constant E."
    },
    {
      "file": "phase_transformations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "transformation_type",
          "temperature_K",
          "deltaH_kJ_per_mol",
          "deltaS_J_per_K_per_mol"
        ],
        "units": {
          "temperature_K": "K",
          "deltaH_kJ_per_mol": "kJ/mol",
          "deltaS_J_per_K_per_mol": "J/(K·mol)"
        }
      },
      "description": "Phase transformation properties (melting and polymorphic) for the three compounds."
    }
  ],
  "notes": "The task reproduces the computational derivation of thermodynamic coefficients and phase transformation properties from published experimental enthalpy data. All required numerical constants (Cp298, S298) are provided in the instruction. The scored artifacts correspond to Tables 3 and 4 of the source, but the agent must compute them from the provided experimental data and boundary conditions, not extract them from the paper text."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact. For fitted_coefficients.csv, the verifier compares your reported coefficients against reference coefficients obtained by the same fitting procedure; the comparison accounts for legitimate numerical differences due to implementation choices. For phase_transformations.csv, the verifier compares your transformation temperatures, enthalpies, and entropies against reference values derived from the enthalpy data. Each stage contributes a weighted component to the final reward. A submission that merely reports expected numbers without executing the required fitting and evaluation will not receive full credit.
