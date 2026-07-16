# Superabundant vacancy thermodynamics in palladium-hydrogen: two- and eight-sublattice models

## Problem background
When palladium absorbs hydrogen under high pressure and high temperature, metal-sublattice vacancy concentrations far above the thermal equilibrium value of the pure metal have been observed. A thermodynamic model rationalises this effect by treating the Pd–H system as a two‑sublattice alloy in which the metal and interstitial sublattices are coupled through a Schottky equilibrium. As hydrogen fills the interstitial sublattice, the interstitial vacancy concentration drops, forcing a compensating rise in the metal‑sublattice vacancy concentration to preserve the Schottky condition. At sufficiently high hydrogen/metal ratios, vacancy fractions of order 0.1–0.2 can appear on the metal sublattice. Upon cooling, these “superabundant” vacancies may order, a process that can be captured by dividing the metal and interstitial sublattices further into eight sublattices. This task investigates both the formation and the ordering of superabundant vacancies by implementing the two‑sublattice and eight‑sublattice thermodynamic models with prescribed parameter sets and numerically computing the equilibrium vacancy fractions, the required hydrogen pressure, and the long‑range order parameter.

## Approach
A sublattice model is used where the system is described by (M,□)⁽α⁾(H,□)⁽β⁾ (M = Pd, □ = vacancy). The molar free energy is written in terms of site fractions on the two sublattices and contains three energetic contributions: (i) nearest-neighbour bond-energy mixing ΔU_m(1) with inter-sublattice exchange energies W_MH, W_MV, W_VH; (ii) configuration‑independent terms ΔU_m(2) expressed as a polynomial in the hydrogen/metal ratio r=y_H^β / y_M^α, with coefficients A₁ and A₂; and (iii) a vacancy‑formation term ΔU_m(3) that depends on the metal‑sublattice composition, containing a parameter A₃. Equilibrium at a given overall composition r is found by solving simultaneously the species‑balance constraint and the Schottky relation μ_□⁽α⁾ + μ_□⁽β⁾ = 0. The resulting site fractions give the metal‑sublattice vacancy fraction y_□⁽α⁾.

To capture vacancy ordering, the metal sublattice is split into four sub‑lattices (α1…α4) and the interstitial sublattice into four (β1…β4), yielding an eight‑sublattice model. The bond‑energy mixing ΔU_m(1) is extended by a metal‑sublattice ordering interaction term L_MV, and the parameter A₃ is adjusted by an amount that keeps the vacancy‑formation energy unchanged. Starting from the fully equilibrated two‑sublattice state at 800°C (uniform vacancy distribution), the system is closed (no exchange of hydrogen or vacancies with the surroundings) and cooled. At each temperature, the vacancy distribution among the four metal sublattices is recomputed subject to fixed total vacancy concentrations, and a long‑range order parameter is calculated from the differences between sublattice occupancies. All parameters needed for both models are specified in the steps below.

## Reproduction target
From the described models, compute and output three data sets:

1. **Metal‑sublattice vacancy fraction vs. H/Pd ratio** at 800°C (1073 K) for r = 0 → 1.5. Output y_□⁽α⁾ as a function of r.
2. **Required H₂ pressure vs. metal‑sublattice vacancy fraction** at 800°C. Use the hydrogen chemical potential obtained from the two‑sublattice model and the μ_H₂(p) relation digitised or fitted from Sugimoto & Fukai (1992, Fig. 1) to convert μ_H to H₂ pressure in GPa. Cover vacancy fractions from about 0.01 to 0.20.
3. **Long‑range order parameter vs. temperature** during closed‑system cooling from 800°C. Starting from the two‑sublattice equilibrium state at 800°C (total metal‑vacancy fraction ≈0.17, uniform distribution), compute the order parameter (y_□⁽α1⁾ − y_□⁽α2⁾)/(y_□⁽α1⁾ + y_□⁽α2⁾) at temperatures between 550 K and 1073 K.

## Assets

- NumPy: numpy
- SciPy: scipy
- Hydrogen chemical potential vs pressure relation (Sugimoto & Fukai 1992): 10.1016/0956-7151(92)90102-K

## Workflow steps

### Step 1: Two-sublattice equilibrium: vacancy fraction vs H/Pd ratio
- Role: scored
- Action: Implement the two-sublattice thermodynamic model with energy contributions ΔU_m(1) (nearest-neighbour bond-energy mixing), ΔU_m(2) (configuration-independent terms as a function of hydrogen/metal ratio r), and ΔU_m(3) (metal-sublattice vacancy formation term). Use the specified parameter values: W_MH/RT=0.808, W_MV=W_VH=0, A1/RT=-2.0, A2/RT=+2.0, A3/RT=13.816. For each r in a range from 0 to at least 1.5, solve the coupled equilibrium equations (composition constraint and Schottky relation) numerically to obtain site fractions, then extract the metal-sublattice vacancy fraction y_□^α. Write a CSV file with columns r and y_square_alpha, containing at least 50 evenly spaced data points.
- Output file: `/app/outputs/two_sublattice_vacancy_vs_r.csv`
- Format: csv
- Contract: Two columns: r (float, dimensionless H/Pd ratio), y_square_alpha (float, vacancy fraction on metal sublattice).
- Scoring: scored by hidden verifier

### Step 2: Required H2 pressure as function of vacancy fraction
- Role: scored
- Action: Using the hydrogen chemical potential obtained from the two-sublattice model (or the species chemical potentials) and the relation between μ_H2 and H2 pressure digitised or fitted from the published curve of Sugimoto & Fukai (1992, Fig. 1), convert the equilibrium hydrogen chemical potential to H2 gas pressure at 800°C. For a range of metal-sublattice vacancy fractions y_□^α (covering at least 0.01 to 0.20), compute the corresponding required H2 pressure in GPa. Write a CSV file with columns y_square_alpha and p_H2_GPa, containing at least 20 points.
- Output file: `/app/outputs/two_sublattice_pressure_vs_vacancy.csv`
- Format: csv
- Contract: Two columns: y_square_alpha (float, vacancy fraction), p_H2_GPa (float, H2 pressure in GPa).
- Scoring: scored by hidden verifier

### Step 3: Eight-sublattice ordering: long-range order parameter vs temperature
- Role: scored (load-bearing)
- Action: Implement the eight-sublattice model (four metal sublattices α1…α4, four interstitial sublattices β1…β4) with the modified ΔU_m(1) expression where the bond-energy mixing is summed over nearest-neighbor sublattice pairs and includes an additional metal-sublattice ordering interaction term L_MV, whose contribution to ΔU_m(1) is 2 L_MV y_M^αi y_□^αj for each pair of metal sublattices. Use the ordering interaction parameter L_MV/RT = -0.6, and with A3/RT increased by 12·L_MV/RT to maintain the vacancy formation energy. Starting from the equilibrium state at 800°C obtained from the two-sublattice model (total metal vacancy fraction ≈0.17, vacancies uniformly distributed), close the system (no exchange with external reservoirs) and allow redistribution of vacancies among sublattices during cooling. At each temperature in a range from 550 to 1073 K (at least 20 points), compute the equilibrium distribution subject to fixed total vacancy concentrations and calculate the long-range order parameter as (y_□^α1 − y_□^α2) / (y_□^α1 + y_□^α2), where α1 and α2 are two non-equivalent metal sublattices. Write a CSV file with columns temperature_K and long_range_order_parameter.
- Output file: `/app/outputs/eight_sublattice_order_vs_temperature.csv`
- Format: csv
- Contract: Two columns: temperature_K (float, in Kelvin), long_range_order_parameter (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/two_sublattice_vacancy_vs_r.csv`
- `/app/outputs/two_sublattice_pressure_vs_vacancy.csv`
- `/app/outputs/eight_sublattice_order_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### two_sublattice_vacancy_vs_r.csv
- path: `/app/outputs/two_sublattice_vacancy_vs_r.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Metal-sublattice vacancy fraction as a function of H/Pd ratio r at 800°C, computed from the two-sublattice model with specified parameters.
- schema:
  - `type`: table
  - `required_columns`: `r`, `y_square_alpha`
  - `columns`:
    - `r`:
      - `type`: float
      - `description`: Hydrogen/metal ratio r = y_H^β / y_M^α
    - `y_square_alpha`:
      - `type`: float
      - `description`: Metal-sublattice vacancy fraction y_□^α

### two_sublattice_pressure_vs_vacancy.csv
- path: `/app/outputs/two_sublattice_pressure_vs_vacancy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: H2 pressure required to achieve a given metal-sublattice vacancy concentration at 800°C, derived using the hydrogen chemical potential vs pressure relation from Sugimoto & Fukai (1992).
- schema:
  - `type`: table
  - `required_columns`: `y_square_alpha`, `p_H2_GPa`
  - `columns`:
    - `y_square_alpha`:
      - `type`: float
      - `description`: Metal-sublattice vacancy fraction
    - `p_H2_GPa`:
      - `type`: float
      - `description`: Required H2 gas pressure in GPa

### eight_sublattice_order_vs_temperature.csv
- path: `/app/outputs/eight_sublattice_order_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Long-range order parameter for vacancy ordering on the metal sublattice as a function of temperature during closed‑system cooling, computed from the eight-sublattice model.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `long_range_order_parameter`
  - `columns`:
    - `temperature_K`:
      - `type`: float
      - `description`: Temperature in Kelvin
    - `long_range_order_parameter`:
      - `type`: float
      - `description`: Long-range order parameter (y_□^α1 − y_□^α2) / (y_□^α1 + y_□^α2)

Notes: The agent must implement the thermodynamic models and numerical solvers using the given parameter values. The hydrogen chemical potential vs pressure relation is needed from the published figure; digitization or a fitted function is acceptable. The scored artifacts are compared to reference curves derived from the same models with the same parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "two_sublattice_vacancy_vs_r.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "y_square_alpha"
        ],
        "columns": {
          "r": {
            "type": "float",
            "description": "Hydrogen/metal ratio r = y_H^β / y_M^α"
          },
          "y_square_alpha": {
            "type": "float",
            "description": "Metal-sublattice vacancy fraction y_□^α"
          }
        }
      },
      "description": "Metal-sublattice vacancy fraction as a function of H/Pd ratio r at 800°C, computed from the two-sublattice model with specified parameters."
    },
    {
      "file": "two_sublattice_pressure_vs_vacancy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "y_square_alpha",
          "p_H2_GPa"
        ],
        "columns": {
          "y_square_alpha": {
            "type": "float",
            "description": "Metal-sublattice vacancy fraction"
          },
          "p_H2_GPa": {
            "type": "float",
            "description": "Required H2 gas pressure in GPa"
          }
        }
      },
      "description": "H2 pressure required to achieve a given metal-sublattice vacancy concentration at 800°C, derived using the hydrogen chemical potential vs pressure relation from Sugimoto & Fukai (1992)."
    },
    {
      "file": "eight_sublattice_order_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "long_range_order_parameter"
        ],
        "columns": {
          "temperature_K": {
            "type": "float",
            "description": "Temperature in Kelvin"
          },
          "long_range_order_parameter": {
            "type": "float",
            "description": "Long-range order parameter (y_□^α1 − y_□^α2) / (y_□^α1 + y_□^α2)"
          }
        }
      },
      "description": "Long-range order parameter for vacancy ordering on the metal sublattice as a function of temperature during closed‑system cooling, computed from the eight-sublattice model."
    }
  ],
  "notes": "The agent must implement the thermodynamic models and numerical solvers using the given parameter values. The hydrogen chemical potential vs pressure relation is needed from the published figure; digitization or a fitted function is acceptable. The scored artifacts are compared to reference curves derived from the same models with the same parameters."
}
```

## How you are scored
A hidden verifier independently implements the same two‑sublattice and eight‑sublattice models with the identical parameter values and the same hydrogen chemical potential–pressure relationship. For each of the three scored output files, the verifier reads your submitted data points, computes the corresponding reference curve at the exact same (r, y_□⁽α⁾, T) coordinates, and compares your values point‑by‑point against those reference values within a numerical tolerance that accounts for minor implementation or digitisation differences. The reward is proportional to the fraction of points that agree within tolerance, and the final score is a weighted combination of the three stages. Running the model and writing the computed data to the specified CSV files is mandatory; simply reporting a known or expected value will not pass because the verifier performs its own full recomputation based solely on the model definition.
