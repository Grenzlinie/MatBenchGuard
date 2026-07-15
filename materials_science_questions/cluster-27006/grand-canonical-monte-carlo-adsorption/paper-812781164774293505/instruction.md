# Correction of Gibbs Free Energy and Monte Carlo Water Adsorption for γ‑CaSO₄

## Problem background
The mineral gypsum (CaSO₄·2H₂O) can undergo dehydration to various calcium sulfate phases depending on temperature and ambient water vapor pressure. The soluble anhydrite γ‑CaSO₄ is known to rehydrate by absorbing water vapor even from extremely dry atmospheres, making it a candidate for atmospheric water capture. However, the standard Gibbs free energy of formation of γ‑CaSO₄ is difficult to determine accurately because the pure phase is rarely obtained without a trace of crystal water. A corrected thermodynamic model is needed to correctly predict phase stability boundaries. Grand canonical Monte Carlo (GCMC) simulations can complement thermodynamic models by predicting water adsorption isotherms in the γ‑CaSO₄ framework, enabling a quantitative understanding of its adsorption capacity under a range of relative humidity and temperature conditions, including conditions akin to the Martian surface.

## Approach
The reproduction employs two complementary lines of attack. First, the standard Gibbs free energy of formation of γ‑CaSO₄ is corrected using thermodynamic equilibrium relations and experimentally known hygroscopic constraints. The approach makes use of published polynomial expressions for the Gibbs free energies of β‑CaSO₄·0.5H₂O and H₂O(g) as functions of temperature:

β‑CaSO₄·0.5H₂O: ΔfG°/(kJ·mol⁻¹) = -1566 + 0.44029·T + 1.4600×10⁻⁴·T² – 1.0480×10⁻⁷·T³

H₂O(g): ΔfG°/(kJ·mol⁻¹) = -241.1 + 0.03874·T – 1.0580×10⁻⁵·T²

The equilibrium relation for the rehydration of γ‑CaSO₄ to β‑CaSO₄·0.5H₂O,
γ‑CaSO₄ + 0.5 H₂O(g) ↔ β‑CaSO₄·0.5H₂O,
is combined with these polynomials to express the unknown Gibbs free energy of γ‑CaSO₄ at two calibration points — 298 K under 0.1 % relative humidity and 459 K under 1 atm water vapor pressure. It is assumed that the Gibbs free energy of γ‑CaSO₄ follows a cubic polynomial of the form
ΔfG°(γ‑CaSO₄)/(kJ·mol⁻¹) = a + b·T + 1.1620×10⁻⁴·T² – 7.0810×10⁻⁸·T³,
where the quadratic and cubic terms are fixed from analogy with the known anhydrite form, leaving the two coefficients a and b to be determined from the two calibration points. Solving the resulting 2×2 linear system yields the corrected polynomial.

With the corrected γ‑CaSO₄ polynomial and the same base polynomials for the other phases, the equilibrium water vapour pressures for the three principal dehydration reactions (gypsum↔hemihydrate, gypsum↔anhydrite, hemihydrate↔anhydrite) are derived and evaluated over 300–600 K.

Second, water adsorption in γ‑CaSO₄ is simulated using grand canonical Monte Carlo (GCMC) in a periodic 3×3×3 supercell built from the published crystal structure (ICSD 22371). Non‑bonded interactions are described by the DREIDING force field, with rigid water molecules. The simulations are run at two conditions: a relative humidity sweep at 298 K from 0 % to 100 % RH, and a low‑pressure sweep at 215 K from 0 to 0.07 kPa, covering conditions from terrestrial ambient to Martian surface. The resulting cumulative water occupancy (number of H₂O molecules per CaSO₄ formula unit) is recorded as the isotherm output.

## Reproduction target
The goal is to compute and produce four output files:

1. Corrected γ‑CaSO₄ Gibbs free energy polynomial coefficients (a and b) that satisfy the thermodynamic constraints at 298 K (0.1 % RH) and 459 K (1 atm H₂O vapour).
2. Equilibrium water vapour pressure curves (in Pa) for the gypsum‑hemihydrate, gypsum‑anhydrite, and hemihydrate‑anhydrite reactions over the temperature range 300–600 K.
3. Water adsorption isotherm at 298 K: cumulative H₂O occupancy vs. relative humidity (0–100 %).
4. Water adsorption isotherm at 215 K: cumulative H₂O occupancy vs. water vapour pressure (0–0.07 kPa).

These artifacts together verify the thermodynamic correction and the simulated adsorption behaviour across the described experimental regimes.

## Assets

- γ‑CaSO₄ crystal structure: ICSD 22371
- DREIDING force field parameters: 10.1021/j100389a010
- Standard Gibbs free energy polynomials for β‑CaSO₄·0.5H₂O and H₂O(g)
- Hygroscopic constraints for gypsum dehydration
- GCMC simulation software (RASPA 2 or equivalent): https://github.com/snurr-group/raspa2

## Workflow steps

### Step 1: Correct γ‑CaSO₄ Gibbs free energy polynomial
- Role: scored
- Action: Using the provided polynomial expressions for β‑CaSO₄·0.5H₂O and H₂O(g) together with the equilibrium relation ΔfG°(γ‑CaSO₄) = ΔfG°(β‑CaSO₄·0.5H₂O) – 0.5·ΔfG°(H₂O) – 0.5·R·T·ln(P_H₂O/P°), compute the standard molar Gibbs free energy of formation of γ‑CaSO₄ at 298 K and 459 K under the given experimental conditions (298 K, relative humidity 0.1%, i.e., water vapour partial pressure = 0.1% of saturation pressure; 459 K, water vapour partial pressure = 1 atm). Assume the cubic polynomial form ΔfG°(γ‑CaSO₄)/(kJ·mol⁻¹) = a + b·T + 1.1620×10⁻⁴·T² – 7.0810×10⁻⁸·T³. Set up and solve the 2×2 linear system for the coefficients a and b using the two computed ΔfG° values. Save the coefficients to a JSON file.
- Output file: `/app/outputs/gamma_caso4_gibbs_polynomial.json`
- Format: json
- Contract: JSON object with keys 'a' (float) and 'b' (float).
- Scoring: scored by hidden verifier

### Step 2: Compute equilibrium water vapour pressure curves
- Role: scored
- Action: Using the corrected γ‑CaSO₄ polynomial from Step 1 and the provided polynomials for CaSO₄·2H₂O, β‑CaSO₄·0.5H₂O, and H₂O(g), derive the equilibrium water vapour pressure expressions for the three dehydration reactions: gypsum ↔ hemihydrate, gypsum ↔ anhydrite, and hemihydrate ↔ anhydrite. Evaluate the pressures at a set of temperatures over the range 300‑600 K and save the results to a CSV file.
- Output file: `/app/outputs/phase_boundary_curves.csv`
- Format: csv
- Contract: Columns: T_K, P_gypsum_hemihydrate_Pa, P_gypsum_anhydrite_Pa, P_hemihydrate_anhydrite_Pa. All pressure values in Pa.
- Scoring: scored by hidden verifier

### Step 3: Prepare GCMC simulation system
- Role: process
- Action: Obtain the γ‑CaSO₄ crystal structure (ICSD 22371 or equivalent). Build a periodic 3×3×3 supercell. Assign DREIDING force field parameters for all atom types and rigid water molecules. Generate the input files required for grand canonical Monte Carlo simulations of water adsorption at 298 K and 215 K.
- Evidence: `/app/outputs/gcmc_setup.log`

### Step 4: GCMC water adsorption isotherm at 298 K
- Role: scored (load-bearing)
- Action: Run grand canonical Monte Carlo simulations of water adsorption in the γ‑CaSO₄ framework at 298 K over a range of relative humidities (0% to 100%). For each humidity condition, record the average cumulative water occupancy (number of H₂O molecules per CaSO₄ formula unit). Output the isotherm as a CSV file.
- Output file: `/app/outputs/mc_isotherm_298K.csv`
- Format: csv
- Contract: Columns: relative_humidity_pct (percent, 0‑100), occupancy (dimensionless).
- Scoring: scored by hidden verifier

### Step 5: GCMC water adsorption isotherm at 215 K
- Role: scored
- Action: Run grand canonical Monte Carlo simulations at 215 K over a water vapour pressure range of 0 to 0.07 kPa. Record the average occupancy and output the isotherm as a CSV file.
- Output file: `/app/outputs/mc_isotherm_215K.csv`
- Format: csv
- Contract: Columns: pressure_Pa (Pa), occupancy (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_caso4_gibbs_polynomial.json`
- `/app/outputs/phase_boundary_curves.csv`
- `/app/outputs/mc_isotherm_298K.csv`
- `/app/outputs/mc_isotherm_215K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_caso4_gibbs_polynomial.json
- path: `/app/outputs/gamma_caso4_gibbs_polynomial.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Corrected coefficients for the cubic polynomial ΔfG°(γ‑CaSO₄)/(kJ·mol⁻¹) = a + b·T + 1.1620×10⁻⁴·T² – 7.0810×10⁻⁸·T³. Scoring compares a and b against hidden gold values with absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `a`: float
    - `b`: float

### phase_boundary_curves.csv
- path: `/app/outputs/phase_boundary_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium water vapour pressures for the three dehydration reactions over 300‑600 K. The checker recomputes log10(P) at selected temperatures and compares against hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `P_gypsum_hemihydrate_Pa`, `P_gypsum_anhydrite_Pa`, `P_hemihydrate_anhydrite_Pa`
  - `units`:
    - `T_K`: K
    - `P_gypsum_hemihydrate_Pa`: Pa
    - `P_gypsum_anhydrite_Pa`: Pa
    - `P_hemihydrate_anhydrite_Pa`: Pa

### mc_isotherm_298K.csv
- path: `/app/outputs/mc_isotherm_298K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Water occupancy per CaSO₄ formula unit vs. relative humidity at 298 K. Scoring verifies monotonic increase and checks occupancy at key humidity points against hidden thresholds.
- schema:
  - `type`: table
  - `required_columns`: `relative_humidity_pct`, `occupancy`
  - `units`:
    - `relative_humidity_pct`: percent
    - `occupancy`: dimensionless

### mc_isotherm_215K.csv
- path: `/app/outputs/mc_isotherm_215K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Water occupancy per CaSO₄ formula unit vs. water vapour pressure at 215 K. Scoring verifies monotonic increase and checks occupancy at key pressure points against hidden thresholds.
- schema:
  - `type`: table
  - `required_columns`: `pressure_Pa`, `occupancy`
  - `units`:
    - `pressure_Pa`: Pa
    - `occupancy`: dimensionless

Notes: The corrected polynomial coefficients are treated as fixed deterministic values (exact_match); the equilibrium curves are scored by recomputing log10(P) and comparing to a hidden reference; the isotherms are scored by structural checks (monotonic trend) and threshold comparisons at selected points.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_caso4_gibbs_polynomial.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float",
          "b": "float"
        }
      },
      "description": "Corrected coefficients for the cubic polynomial ΔfG°(γ‑CaSO₄)/(kJ·mol⁻¹) = a + b·T + 1.1620×10⁻⁴·T² – 7.0810×10⁻⁸·T³. Scoring compares a and b against hidden gold values with absolute tolerance."
    },
    {
      "file": "phase_boundary_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "P_gypsum_hemihydrate_Pa",
          "P_gypsum_anhydrite_Pa",
          "P_hemihydrate_anhydrite_Pa"
        ],
        "units": {
          "T_K": "K",
          "P_gypsum_hemihydrate_Pa": "Pa",
          "P_gypsum_anhydrite_Pa": "Pa",
          "P_hemihydrate_anhydrite_Pa": "Pa"
        }
      },
      "description": "Equilibrium water vapour pressures for the three dehydration reactions over 300‑600 K. The checker recomputes log10(P) at selected temperatures and compares against hidden reference values."
    },
    {
      "file": "mc_isotherm_298K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "relative_humidity_pct",
          "occupancy"
        ],
        "units": {
          "relative_humidity_pct": "percent",
          "occupancy": "dimensionless"
        }
      },
      "description": "Water occupancy per CaSO₄ formula unit vs. relative humidity at 298 K. Scoring verifies monotonic increase and checks occupancy at key humidity points against hidden thresholds."
    },
    {
      "file": "mc_isotherm_215K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_Pa",
          "occupancy"
        ],
        "units": {
          "pressure_Pa": "Pa",
          "occupancy": "dimensionless"
        }
      },
      "description": "Water occupancy per CaSO₄ formula unit vs. water vapour pressure at 215 K. Scoring verifies monotonic increase and checks occupancy at key pressure points against hidden thresholds."
    }
  ],
  "notes": "The corrected polynomial coefficients are treated as fixed deterministic values (exact_match); the equilibrium curves are scored by recomputing log10(P) and comparing to a hidden reference; the isotherms are scored by structural checks (monotonic trend) and threshold comparisons at selected points."
}
```

## How you are scored
A hidden verifier will independently inspect each of the four scored output files. For each file, the verifier checks the computed values against independently derived reference data (for example, recomputing key derived quantities from the submitted polynomials, comparing occupancy at critical humidity/pressure points against expected trends, and verifying the overall shape and monotonicity of the isotherms). Each stage contributes a weighted portion to the total reward (the main isotherm carries the highest weight); a perfect score requires all stages to be correctly executed. Simply reporting the expected numbers without running the prescribed computational workflow will not satisfy the verifier.
