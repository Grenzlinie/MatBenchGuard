# High-pressure phase transition and elastic properties of LaS and PrS using a realistic interaction potential model

## Problem background
Rare earth sulfides exhibit pressure-induced structural phase transitions from the NaCl-type (B1) to the CsCl-type (B2) crystal structure. Understanding the transition pressures, associated volume changes, and the elastic and thermo-mechanical properties of these compounds under extreme conditions is important for their potential applications in electro-optics, grinding alloys, and electronic devices. This task reproduces a computational study that uses a Realistic Interaction Potential (RIP) model to predict these properties for the pure compounds LaS and PrS at both zero temperature and room temperature (300 K).

## Approach
The RIP model describes the total lattice energy of an ionic crystal as a sum of several contributions: long-range Coulomb attraction, a three-body interaction that accounts for charge-transfer effects, van der Waals dipole–dipole and dipole–quadrupole interactions, short-range overlap repulsion up to second neighbours (Born–Mayer form), and a zero-point energy term. Finite-temperature effects are included by working with the Gibbs free energy G = U + PV − TS, where the entropy S is obtained from the vibrational specific heat via the Grüneisen parameter.

The workflow proceeds in three stages:
1. **Model calibration:** The model contains three adjustable parameters – the range parameter ρ, the hardness parameter b, and the three-body force parameter f(r). These are determined for each compound by solving the equilibrium conditions (dU/dr = 0 and the curvature condition linking the second derivative to the bulk modulus) at the known zero-pressure equilibrium nearest-neighbor separation r0 and bulk modulus BT. The required input data are extracted from the literature:
   - LaS: r0 = 2.946 Å, BT = 89 GPa; ionic radii r(La) = 1.27 Å, r(S) = 1.84 Å.
   - PrS: r0 = 2.880 Å, BT = 107 GPa; r(Pr) = 1.00 Å, r(S) = 1.84 Å.
   Madelung constants for the B1 (α_m ≈ 1.7476) and B2 (α'_m ≈ 1.7627) structures are standard; van der Waals coefficients C and D are computed from ionic polarizabilities using the Slater–Kirkwood approximation, and Pauling coefficients quantify the ionic overlap repulsion.

2. **Phase transition calculation:** Using the calibrated parameters, the Gibbs free energies G(r) for the B1 and B2 phases are constructed as functions of the nearest-neighbour distance r (or r'). For each temperature (0 K and 300 K), a pressure scan is performed; at each pressure the free energy of each phase is minimized with respect to its nearest-neighbor separation. The transition pressure Pt is located at the pressure where ΔG = G(B2) − G(B1) = 0. The volume drop is computed as the relative change (V_B1/V0 − V_B2/V0) × 100 evaluated at Pt.

3. **Elastic and thermo‑mechanical properties:** For the B1 phase at zero pressure, the second-order elastic constants C11, C12, and C44 are obtained from the second derivatives of the lattice energy with respect to appropriate deformations. From these, the full set of derived properties is calculated using standard relations from linear elasticity: Young’s modulus Y, bulk modulus BT, shear modulus G, tetragonal shear moduli CS and CL, anisotropy A, Kleinman parameter ζ, Poisson’s ratio σ, longitudinal, transverse, and mean elastic wave velocities (ν_l, ν_t, ν_m), pressure derivatives of BT, CS, and C44, the Cauchy parameter C12 − C44, the ratio BT/G, and the Every/Blackman parameters s1, s2, s3, F12, F44. All properties are evaluated at both 0 K and 300 K.

## Reproduction target
You must compute and output the following two tables as CSV files:

1. **transition_pressures_volume_drops.csv** – Columns: `compound` (string), `temperature_K` (integer), `transition_pressure_GPa` (float), `volume_drop_percent` (float). Provide one row for each combination of LaS/PrS and 0 K/300 K, giving the B1→B2 transition pressure and the associated volume drop.

2. **elastic_properties.csv** – Columns: `compound` (string), `temperature_K` (integer), `property` (string), `value` (float). For each compound (LaS, PrS) and each temperature (0 K, 300 K), output a row for every property listed below, using exactly these property names: C11, C12, C44, Y, BT, G, CS, CL, A, zeta, sigma, nu_l, nu_t, nu_m, dBT_dP, dCS_dP, dC44_dP, C12_minus_C44, BT_over_G, s1, s2, s3, F12, F44. Elastic moduli are in GPa, velocities in m/s, and dimensionless quantities as pure numbers.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Calibrate RIP model parameters
- Role: process
- Action: Using the input data (equilibrium nearest‑neighbor separation r0 and bulk modulus BT for LaS and PrS from the paper’s Table 1, together with ionic radii), solve the equilibrium conditions (first and second derivative of lattice energy) to determine the three model parameters: range parameter ρ, hardness parameter b, and three‑body force parameter f(r). These parameters will be used in all subsequent calculations.
- Evidence: `/app/outputs/calibration_parameters.json`

### Step 2: Compute phase transition pressures and volume drops
- Role: scored (load-bearing)
- Action: For LaS and PrS at T=0K and T=300K: build the Gibbs free energy expressions for the B1 and B2 phases using the calibrated RIP model. For each temperature, scan pressure values, minimize the Gibbs free energy with respect to the nearest‑neighbor separation for each phase, and locate the transition pressure Pt where ΔG=0. Calculate the volume drop as (V_B1(Pt)/V0 – V_B2(Pt)/V0)×100. Write results to CSV.
- Output file: `/app/outputs/transition_pressures_volume_drops.csv`
- Format: csv
- Contract: Columns: compound (string: LaS, PrS), temperature_K (int: 0, 300), transition_pressure_GPa (float), volume_drop_percent (float). One row per (compound, temperature) combination.
- Scoring: scored by hidden verifier

### Step 3: Compute elastic and thermo‑mechanical properties
- Role: scored (load-bearing)
- Action: For LaS and PrS at T=0K and T=300K: using the calibrated RIP model and the equilibrium nearest‑neighbor separation of the B1 phase at zero pressure, calculate the second‑order elastic constants (C11, C12, C44) and all derived quantities (Young’s modulus Y, bulk modulus BT, shear modulus G, tetragonal shear moduli CS and CL, anisotropy A, Kleinman parameter ζ, Poisson’s ratio σ, elastic wave velocities ν_l, ν_t, ν_m, pressure derivatives dBT/dP, dCS/dP, dC44/dP, Cauchy parameter C12-C44, ratio BT/G, and the Every/Blackman parameters s1, s2, s3, F12, F44). Write each property as a row in CSV file.
- Output file: `/app/outputs/elastic_properties.csv`
- Format: csv
- Contract: Columns: compound (string: LaS, PrS), temperature_K (int: 0, 300), property (string: C11, C12, C44, Y, BT, G, CS, CL, A, zeta, sigma, nu_l, nu_t, nu_m, dBT_dP, dCS_dP, dC44_dP, C12_minus_C44, BT_over_G, s1, s2, s3, F12, F44), value (float). One row per property per compound per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_pressures_volume_drops.csv`
- `/app/outputs/elastic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_pressures_volume_drops.csv
- path: `/app/outputs/transition_pressures_volume_drops.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed structural phase transition pressures (GPa) and volume drops (%) for LaS and PrS at T=0K and T=300K.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature_K`, `transition_pressure_GPa`, `volume_drop_percent`
  - `columns`:
    - `compound`: string
    - `temperature_K`: int
    - `transition_pressure_GPa`: float
    - `volume_drop_percent`: float

### elastic_properties.csv
- path: `/app/outputs/elastic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed second‑order elastic constants and derived mechanical properties. Possible property names: C11, C12, C44, Y, BT, G, CS, CL, A, zeta, sigma, nu_l, nu_t, nu_m, dBT_dP, dCS_dP, dC44_dP, C12_minus_C44, BT_over_G, s1, s2, s3, F12, F44. Units: elastic moduli in GPa, velocities in m/s, others dimensionless.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature_K`, `property`, `value`
  - `columns`:
    - `compound`: string
    - `temperature_K`: int
    - `property`: string
    - `value`: float

Notes: The agent must implement the full RIP model from scratch. Input constants (lattice constants, bulk moduli, ionic radii) are listed in the paper’s Table 1 and should be hard‑coded. Only pure LaS and PrS are required; mixed‑concentration alloys are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_pressures_volume_drops.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature_K",
          "transition_pressure_GPa",
          "volume_drop_percent"
        ],
        "columns": {
          "compound": "string",
          "temperature_K": "int",
          "transition_pressure_GPa": "float",
          "volume_drop_percent": "float"
        }
      },
      "description": "Computed structural phase transition pressures (GPa) and volume drops (%) for LaS and PrS at T=0K and T=300K."
    },
    {
      "file": "elastic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature_K",
          "property",
          "value"
        ],
        "columns": {
          "compound": "string",
          "temperature_K": "int",
          "property": "string",
          "value": "float"
        }
      },
      "description": "Computed second‑order elastic constants and derived mechanical properties. Possible property names: C11, C12, C44, Y, BT, G, CS, CL, A, zeta, sigma, nu_l, nu_t, nu_m, dBT_dP, dCS_dP, dC44_dP, C12_minus_C44, BT_over_G, s1, s2, s3, F12, F44. Units: elastic moduli in GPa, velocities in m/s, others dimensionless."
    }
  ],
  "notes": "The agent must implement the full RIP model from scratch. Input constants (lattice constants, bulk moduli, ionic radii) are listed in the paper’s Table 1 and should be hard‑coded. Only pure LaS and PrS are required; mixed‑concentration alloys are excluded."
}
```

## How you are scored
A hidden verifier independently evaluates each scored CSV file. The verifier compares your computed transition pressures, volume drops, and elastic properties to the expected reference values using appropriate absolute and relative tolerances, and checks that qualitative trends (e.g., the transition pressure decreasing with temperature) are correctly reproduced. The final score is a weighted combination of the partial scores from the two output files; correctly implementing the full RIP model and obtaining numbers within tolerance will earn full credit, while large deviations or missing properties will reduce the score.
