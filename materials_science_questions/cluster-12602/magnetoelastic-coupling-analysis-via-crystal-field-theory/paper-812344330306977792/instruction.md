# Exchange-Striction Landau Model: Tricritical and Wing Critical Points Calculation

## Problem background
The itinerant ferromagnet CoS₂ undergoes a pressure-induced change in the order of its magnetic phase transition: the second-order transition at ambient pressure becomes first-order under moderate hydrostatic pressure. An exchange-striction model that incorporates both first- and second-order magnetoelastic interactions describes this behaviour by coupling the volume strain to the exchange integral. After expanding the magnetic equation of state in powers of the reduced magnetization, one obtains a Landau-like equation whose coefficients govern the location of a tricritical point and the critical points of phase-diagram wings in the temperature–pressure–magnetic-field space. This task computes those features from the model with a prescribed set of material parameters.

## Approach
The model starts from a Heisenberg ferromagnet in mean-field theory, with an exchange integral that depends on the volume strain ω via the first-order magnetoelastic constant γ and the second-order constant ε. Minimising the free energy with respect to ω and expanding the Brillouin function for spin s = 1/2 up to fifth order in the reduced magnetization m yields an equation of state

A m + B m³ + C m⁵ = h,  h = μ H / (k T),

where μ is the Bohr magneton and k is Boltzmann’s constant. The coefficients are:

A = (T − T_c(P))/T,
T_c(P) = T_c⁰ − (γ / (2 k B₀)) P + (ε / (12 k B₀²)) P²,

B = 1/3 (T_c(P)/T)³ − (n / (8 k T B₀)) (γ − ε P/(3 B₀))²,

C = 1/8 (n / (k T B₀)) (T_c(P)/T)² (γ − ε P/(3 B₀))²
    − 1/64 (n² ε / (k T B₀²)) (γ − ε P/(3 B₀))²
    − 2/15 (T_c(P)/T)⁵.

The given numerical parameters are T_c⁰ = 121 K, B₀ = 1.5×10¹² erg/cm³, n = 2.4×10²² cm⁻³, γ = 2×10⁻¹³ erg, ε = −5×10⁻¹⁰ erg (s = 1/2). Pressures must be expressed in erg/cm³ (1 GPa = 10¹⁰ erg/cm³).

At zero field (h = 0) the transition is second-order when B > 0 and first-order when B < 0. The tricritical point is found by solving A = 0 (i.e., T = T_c(P)) together with B(T_c(P), P) = 0.

For a pressure where B becomes negative, a first-order line appears when a magnetic field is applied. The critical point of the phase-diagram wing (where the first-order line terminates) satisfies B < 0, C > 0 and

A_cr = (9/20) (B² / C),
m_cr² = −(3/10) (B / C),
h_cr = (6/25) (B² / C) m_cr.

The physical critical magnetic field is H_cr = (k T_cr / μ) h_cr, with μ = 9.274×10⁻²¹ erg/G and k = 1.380649×10⁻¹⁶ erg/K.

## Reproduction target
Using the material parameters listed above, implement the expressions for T_c(P), B, and C. Then:

1. Compute T_c(P) and B at T = T_c(P) for pressures P = 0, 0.5, 1.0, 1.5 GPa. Output the results as a CSV showing pressure (in GPa) and the corresponding B value.
2. Find the tricritical point by solving T = T_c(P) and B(T_c(P), P) = 0 simultaneously. Report the pressure P_t (in GPa) and temperature T_t (in K) in a JSON file.
3. At P = 1.4 GPa, compute T_c(P), B, and C. Determine the wing critical point (T_cr, H_cr in Tesla, and m_cr) from the critical-point equations and the conversion h_cr → H_cr. Save the result as JSON, including the fixed pressure value.

## Assets

- Python 3
- numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute cubic coefficient B at selected pressures
- Role: scored
- Action: Implement the formula for pressure-dependent Curie temperature and cubic coefficient B from the exchange-striction model using the given material parameters (Tc0=121 K, B0=1.5e12 erg/cm^3, n=2.4e22 cm^-3, gamma=2e-13 erg, epsilon=-5e-10 erg, spin s=1/2). For pressures P = 0, 0.5, 1.0, 1.5 GPa, compute Tc(P) and then evaluate B at T = Tc(P). Save results as a CSV.
- Output file: `/app/outputs/B_coefficient.csv`
- Format: csv
- Contract: pressure_GPa (float), B_value (float)
- Scoring: scored by hidden verifier

### Step 2: Find tricritical point
- Role: scored (load-bearing)
- Action: Using the expressions for A (linear coefficient) and B, solve the equations A=0 (i.e., T=Tc(P)) and B(Tc(P),P)=0 simultaneously to find the pressure P_t and temperature T_t where the second-order transition changes to first-order. Output coordinates.
- Output file: `/app/outputs/tricritical_point.json`
- Format: json
- Contract: {"P_t_GPa": float, "T_t_K": float}
- Scoring: scored by hidden verifier

### Step 3: Compute wing critical point at P=1.4 GPa
- Role: scored (load-bearing)
- Action: At fixed pressure P=1.4 GPa, compute Tc(P), then B and C coefficients. Determine the critical point (T_cr, H_cr, m_cr) of the phase-diagram wing using the condition that A = (9/20) B^2/C with B<0, C>0, and the relations m_cr^2 = -(3/10) B/C and h_cr = (6/25)(B^2/C) m_cr. Convert reduced field h_cr to magnetic field H_cr in Tesla using h = mu H / (k T) with Bohr magneton mu = 9.274e-21 erg/G and Boltzmann constant k = 1.380649e-16 erg/K. Output the critical point values.
- Output file: `/app/outputs/wing_critical_point.json`
- Format: json
- Contract: {"pressure_GPa": 1.4, "T_cr_K": float, "H_cr_T": float, "m_cr": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/B_coefficient.csv`
- `/app/outputs/tricritical_point.json`
- `/app/outputs/wing_critical_point.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### B_coefficient.csv
- path: `/app/outputs/B_coefficient.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cubic coefficient B at four pressures (P=0, 0.5, 1.0, 1.5 GPa) evaluated at T=Tc(P).
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `B_value`
  - `units`:
    - `pressure_GPa`: GPa
    - `B_value`: dimensionless

### tricritical_point.json
- path: `/app/outputs/tricritical_point.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Tricritical point coordinates (pressure, temperature) where A=0 and B=0 simultaneously.
- schema:
  - `type`: object
  - `required`: `P_t_GPa`, `T_t_K`
  - `items`:
    - `P_t_GPa`: float
    - `T_t_K`: float

### wing_critical_point.json
- path: `/app/outputs/wing_critical_point.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Wing critical point at P=1.4 GPa (temperature, magnetic field, reduced magnetization).
- schema:
  - `type`: object
  - `required`: `pressure_GPa`, `T_cr_K`, `H_cr_T`, `m_cr`
  - `items`:
    - `pressure_GPa`: float
    - `T_cr_K`: float
    - `H_cr_T`: float
    - `m_cr`: float

Notes: All outputs are derived from the exchange-striction Landau model with given material parameters. The agent must implement the formulas for Tc(P), B, and C as described in the steps. The checker will compare against independently computed reference values and the paper's reported gold (with tolerance).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "B_coefficient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "B_value"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "B_value": "dimensionless"
        }
      },
      "description": "Cubic coefficient B at four pressures (P=0, 0.5, 1.0, 1.5 GPa) evaluated at T=Tc(P)."
    },
    {
      "file": "tricritical_point.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "P_t_GPa",
          "T_t_K"
        ],
        "items": {
          "P_t_GPa": "float",
          "T_t_K": "float"
        }
      },
      "description": "Tricritical point coordinates (pressure, temperature) where A=0 and B=0 simultaneously."
    },
    {
      "file": "wing_critical_point.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "pressure_GPa",
          "T_cr_K",
          "H_cr_T",
          "m_cr"
        ],
        "items": {
          "pressure_GPa": "float",
          "T_cr_K": "float",
          "H_cr_T": "float",
          "m_cr": "float"
        }
      },
      "description": "Wing critical point at P=1.4 GPa (temperature, magnetic field, reduced magnetization)."
    }
  ],
  "notes": "All outputs are derived from the exchange-striction Landau model with given material parameters. The agent must implement the formulas for Tc(P), B, and C as described in the steps. The checker will compare against independently computed reference values and the paper's reported gold (with tolerance)."
}
```

## How you are scored
A hidden verifier evaluates each scored artifact independently and combines the stage scores into a final reward.

- **B_coefficient.csv**: The verifier recomputes B from the same formulas and checks correctness. It also verifies that the sign of B is positive at the lowest pressure and becomes negative by the highest pressure, consistent with a change in transition order.
- **tricritical_point.json**: The verifier solves the tricritical equations and compares the submitted (P_t, T_t) against its own solution. Credit is awarded based on agreement within a hidden tolerance.
- **wing_critical_point.json**: The verifier first extracts the agent’s own B and C values for P = 1.4 GPa and checks that T_cr, H_cr, and m_cr satisfy the wing critical-point relations (self-consistency). It also compares H_cr against a hidden reference value.

The final score is a weighted combination of these checks; simply writing numbers that are known to appear in the literature is not sufficient to pass.
