# Steady-state thermoelectric generator performance evaluation with finned heat exchangers

## Problem background
Thermoelectric generators convert heat directly to electricity through the Seebeck effect. Real devices are subject to multiple internal and external irreversibilities—Joule heating, Thomson effect, thermal conduction, air-gap leakage, contact resistances, and finite-rate heat transfer through finned heat exchangers. A complete numerical model that accounts for all these effects is needed to predict and optimise the performance of a practical thermoelectric generator. The task is to simulate the steady-state behaviour of a commercial thermoelectric module with finned heat exchangers, supplied with hot and cold water flows, and to extract its key performance metrics: open-circuit voltage, short-circuit current, maximum power output, and maximum efficiency.

## Approach
The model represents a multielement thermoelectric module (Ferrotec 8001/127/040B) paired with finned aluminium heat exchangers. Temperature-dependent thermoelectric properties of the semiconductor legs (Seebeck coefficient, electrical resistivity, thermal conductivity) are used; these are taken from published Melcor data. A thermal resistance network is built that connects the hot and cold water streams to the thermoelectric junctions through the heat exchanger bases, ceramic plates, copper conducting strips, semiconductor legs, and the air gap between the ceramic plates. The coupled heat balance equations for the thermoelectric elements are derived from the one-dimensional energy conservation, incorporating Peltier, Fourier, Joule, and Thomson effects. For a given electrical current, the hot and cold junction temperatures are found by iteratively solving the algebraic energy balances that link the thermoelectric elements and the thermal resistances. Once the junction temperatures are converged, the output voltage, power, and efficiency are computed. The simulation sweeps a range of electrical currents to generate the characteristic performance curves.

## Reproduction target
Simulate the thermoelectric generator with hot water at 100 °C and cold water at 27 °C. For at least 20 equidistant current values between 0 A and 0.3 A, compute the steady-state output voltage V, power output P, efficiency η, hot junction temperature T_h, and cold junction temperature T_c. Write the sweep results to a CSV file (`step_01_simulation_results.csv`). From the CSV, determine the open-circuit voltage V_oc (voltage at zero current), short-circuit current I_sc (current at zero voltage), maximum power P_max, and maximum efficiency η_max, and save them as a JSON file (`step_02_summary.json`). All required parameters are listed in the Constants and parameters section below; no external data download is required.

## Assets

- numpy: numpy
- scipy: scipy

## Constants and parameters

**General constants**
- Stefan–Boltzmann constant: σ_b = 5.670367 × 10⁻⁸ W·m⁻²·K⁻⁴
- Gravitational acceleration: g = 9.81 m·s⁻²

**Thermoelectric module geometry (Ferrotec 8001/127/040B)**
- Number of leg pairs: N = 127
- Leg cross‑sectional area: A = 1 mm² (each leg)
- Leg height: L = 1.9 mm  (also the spacing between ceramic plates for the air gap)
- Copper strip thickness: δ_cu = 0.2 mm
- Ceramic plate thickness: δ_cp = 0.9 mm
- Ceramic plate side length: 29.7 mm  →  A_cp = 29.7 × 29.7 mm² = 882.09 mm²
- Air‑gap packed density: θ = (2 A N) / A_cp  (values above give θ ≈ 0.288)

**Material properties of module components**
- Copper electrical resistivity: ρ_cu = 1.7×10⁻⁸ Ω·m
- Copper thermal conductivity: k_cu = 386 W·m⁻¹·K⁻¹
- Ceramic plate thermal conductivity: k_cp = 35.3 W·m⁻¹·K⁻¹
- Ceramic plate emissivity (blackness): ε_cp = 0.9
- Aluminium heat‑exchanger thermal conductivity: k_Al = 204 W·m⁻¹·K⁻¹

**Finned heat‑exchanger geometry (identical hot and cold sides)**
- Base area: A_b = 29.7 × 29.7 mm²  (same footprint as ceramic plate)
- Base thickness: δ_b = 4 mm
- Fin thickness: δ_f = 2.7 mm
- Channel width: δ_c = 2.7 mm
- Fin height: H_f = 20 mm
- Number of fins: N_f = 6

**Fluid properties (air)**
- Thermal conductivity: k_air = 2.57×10⁻² W·m⁻¹·K⁻¹
- Prandtl number: Pr_air = 0.713
- Coefficient of cubical expansion: β_air = 3.43×10⁻³ K⁻¹
- Kinetic viscosity: ν_air = 1.52×10⁻⁵ m²·s⁻¹
- Thermal diffusivity (computed): a_air = ν_air / Pr_air ≈ 2.13×10⁻⁵ m²·s⁻¹

**Fluid properties (water)**
- Thermal conductivity: k_w = 5.99×10⁻² W·m⁻¹·K⁻¹
- Prandtl number: Pr_w = 7.02
- Flow velocity: v_w = 0.5 m·s⁻¹
- Kinematic viscosity (representative value for water near room temperature): ν_w ≈ 1.0×10⁻⁶ m²·s⁻¹

**Temperature‑dependent semiconductor properties (T in K, mean temperature T_avg = (T_h+T_c)/2)**
- Seebeck coefficient of p‑type leg (α_n = –α_p):  
  α_p(T_avg) = (22224.0 + 930.6·T_avg – 0.9905·T_avg²) × 10⁻⁹  V·K⁻¹
- Electrical resistivity (ρ):  
  ρ(T_avg) = (5112.0 + 163.4·T_avg + 0.6279·T_avg²) × 10⁻¹⁰  Ω·m
  (electrical conductivity σ = 1/ρ)
- Thermal conductivity (k):  
  k(T_avg) = (62605.0 – 277.7·T_avg + 0.4131·T_avg²) × 10⁻⁴  W·m⁻¹·K⁻¹

## Workflow steps

### Step 1: Simulate irreversible thermoelectric generator model
- Role: scored
- Action: Implement the full numerical model of the thermoelectric generator with finned heat exchangers, including temperature-dependent Seebeck coefficient, electrical resistivity, and thermal conductivity of the semiconductor legs, thermal resistance network (conducting strips, ceramic plates, heat exchangers, air gap), and the coupled heat balance equations. Solve iteratively for hot and cold junction temperatures at a given electrical current I. Compute output voltage V, power output P, and thermal efficiency η for at least 20 equidistant current values in the range 0 to 0.3 A. Use hot water temperature TH=100°C and cold water temperature TL=27°C. Write the sweep results to a CSV file.
- Output file: `/app/outputs/step_01_simulation_results.csv`
- Format: csv
- Contract: CSV with header row: I (float, A), V (float, V), P (float, W), eta (float, dimensionless), T_h (float, K), T_c (float, K). At least 20 rows.
- Scoring: scored by hidden verifier

### Step 2: Extract headline performance metrics
- Role: scored (load-bearing)
- Action: Read the simulation CSV from step_01. Locate the open-circuit voltage V_oc as the voltage at I=0 (or interpolate from the smallest current values). Locate the short-circuit current I_sc as the current at V=0 (interpolate if needed). Determine the maximum power P_max as the largest value in the P column, and the maximum efficiency η_max as the largest value in the eta column. Write these four extracted values to a JSON summary file.
- Output file: `/app/outputs/step_02_summary.json`
- Format: json
- Contract: JSON object with keys: {"V_oc": <float, V>, "I_sc": <float, A>, "P_max": <float, W>, "eta_max": <float, dimensionless>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_simulation_results.csv`
- `/app/outputs/step_02_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_simulation_results.csv
- path: `/app/outputs/step_01_simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing the performance sweep of the TEG module. Columns: I (A), V (V), P (W), eta (dimensionless), T_h (K), T_c (K). At least 20 data rows. The checker will verify column existence, data types, and structural consistency (e.g. V monotonically decreasing with I).
- schema:
  - `type`: table
  - `required_columns`: `I`, `V`, `P`, `eta`, `T_h`, `T_c`
  - `units`:
    - `I`: A
    - `V`: V
    - `P`: W
    - `eta`: dimensionless
    - `T_h`: K
    - `T_c`: K

### step_02_summary.json
- path: `/app/outputs/step_02_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: JSON object containing the extracted headline performance metrics from the simulation. The checker will compare these values to hidden reference values with appropriate tolerances (meeting or exceeding the reference for power and efficiency).
- schema:
  - `type`: object
  - `required`:
    - `V_oc`: float (V)
    - `I_sc`: float (A)
    - `P_max`: float (W)
    - `eta_max`: float (dimensionless)

Notes: The simulation must reproduce the performance of the Ferrotec 8001/127/040B module with the specified heat exchanger and water temperatures. The checker will validate the CSV structure, recompute V_oc, I_sc, P_max, eta_max from the CSV, and compare both the self-consistency between the CSV and JSON and the JSON values against hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "I",
          "V",
          "P",
          "eta",
          "T_h",
          "T_c"
        ],
        "units": {
          "I": "A",
          "V": "V",
          "P": "W",
          "eta": "dimensionless",
          "T_h": "K",
          "T_c": "K"
        }
      },
      "description": "CSV file containing the performance sweep of the TEG module. Columns: I (A), V (V), P (W), eta (dimensionless), T_h (K), T_c (K). At least 20 data rows. The checker will verify column existence, data types, and structural consistency (e.g. V monotonically decreasing with I)."
    },
    {
      "file": "step_02_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "V_oc": "float (V)",
          "I_sc": "float (A)",
          "P_max": "float (W)",
          "eta_max": "float (dimensionless)"
        }
      },
      "description": "JSON object containing the extracted headline performance metrics from the simulation. The checker will compare these values to hidden reference values with appropriate tolerances (meeting or exceeding the reference for power and efficiency)."
    }
  ],
  "notes": "The simulation must reproduce the performance of the Ferrotec 8001/127/040B module with the specified heat exchanger and water temperatures. The checker will validate the CSV structure, recompute V_oc, I_sc, P_max, eta_max from the CSV, and compare both the self-consistency between the CSV and JSON and the JSON values against hidden reference values."
}
```

## How you are scored
A hidden verifier checks the two output artifacts. For the CSV, it validates that the required columns are present, data types are correct, and the curves exhibit the expected structural properties (e.g., voltage decreases monotonically with current). It recomputes V_oc, I_sc, P_max, and η_max from the CSV and compares them to hidden reference values. It also verifies that the JSON file is consistent with the CSV. The total reward is a weighted combination: the accuracy of the four headline metrics provides the bulk of the reward, while structural validation contributes a smaller share. You must produce both files exactly as specified; the verifier scores the artifacts, not the code that generated them.
