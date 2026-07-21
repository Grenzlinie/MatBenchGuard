# Size-Dependent Nonlinear Static Analysis of a Piezoelectric Cantilever Microbeam

## Problem background
Microelectromechanical systems (MEMS) often employ electrostatically actuated cantilever microbeams as sensors and actuators. When a voltage is applied between a movable beam and a fixed electrode, the electrostatic force pulls the beam downwards, and at a critical voltage – the pull-in voltage – the beam collapses. Accurate prediction of the static deflection and pull-in voltage is essential for design. When a piezoelectric layer is bonded to the beam, an additional voltage applied to that layer can influence the beam’s deformation and stability. Moreover, at micron scale the mechanical response can differ from classical continuum predictions due to size effects, and damage accumulated during fabrication or use can further alter the behaviour. This task reproduces a computational study that combines modified couple stress theory (to capture size effects), von Kármán geometric nonlinearity, and isotropic damage to model the static bending of a piezoelectric cantilever microbeam and to compute its tip displacement versus applied voltage and its pull-in voltage.

## Approach
The beam is modelled as a cantilever with a piezoelectric layer bonded to its top surface, separated from a fixed ground electrode by a gap. The governing equation is derived from Hamilton’s principle using Bernoulli–Euler beam theory, the modified couple stress theory, and the von Kármán nonlinear strain–displacement relation. A damage parameter D reduces the beam’s Young’s modulus, and the equivalent electric field from the piezoelectric layer enters as an axial force and a boundary bending moment. The resulting fourth-order nonlinear ordinary differential equation is nondimensionalized and solved numerically by the differential quadrature method (DQM) for cantilever boundary conditions. The solution gives the dimensionless transverse deflection W(ξ) along the beam length; the tip displacement W(ξ=1) is recorded as a function of the electrode voltage. The pull-in voltage is identified as the voltage where the solution diverges (or the slope becomes infinite). The task compares two models: a classical model with no length scale effect (l_eq = 0) and the present size-dependent model (l_eq = 0.7 µm), and examines three piezoelectric voltages. Additional sweeps explore the effect of varying the piezoelectric voltage, beam damage, initial gap, and inclusion/exclusion of geometric nonlinearity.

## Reproduction target
Implement the DQM numerical solver and compute the following:
- Tip displacement curves: For the classical model and the present model, at piezoelectric voltages V̄_p = -1, 0, and 1, sweep the electrode voltage V̄ from zero up to pull-in and record the dimensionless tip displacement. Save all (case, V̄, W_tip) points in tip_displacement.csv.
- Pull-in voltages: For the present model, determine the pull-in voltage for V̄_p values from -1.5 to 1.5; for the present and classical models with damage D=0.2; for different initial gaps; and for the geometrically linear versus nonlinear cases. Save each case identifier and its V̄_pl in pull_in_voltage.csv.
The computed curves and pull-in voltages should be physically plausible and consistent with the model physics; the hidden verifier will assess them against reference values and expected structural trends.

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute equivalent stiffnesses and nondimensional parameters
- Role: process
- Action: Using the geometric and material properties given in Table 1 (L=100 µm, b=15 µm, hb=3 µm, hp=0.5 µm, Eb=169 GPa, Ep=78.6 GPa, νb=0.06, νp=0.3, ρb=2331 kg/m³, ρp=7500 kg/m³, e31=-9.29 C/m², εv=8.854e-12 F/m, d=1 µm, and damage D when applicable), compute the neutral-axis position zc, the effective bending stiffness (EI)eq, axial stiffness (EA)eq, couple-stress contribution (μA l²)eq, and the nondimensional coefficients α, ē₃₁, β, as well as any other required intermediate constants. Store all parameters for use by the DQM solver.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Solve static deflection and produce tip displacement curves
- Role: scored (load-bearing)
- Action: Implement the differential quadrature method (DQM) to solve the nondimensional static governing equation with cantilever boundary conditions. Using the parameters from the previous step, compute the nondimensional tip displacement W(ξ=1) for a sweep of electrode voltages V̄ from 0 up to pull-in. Run the DQM solver for the classical model (l_eq=0, i.e., (μA l²)eq = 0) and the present model (l_eq=0.7 µm) at piezoelectric voltages V̄_p = -1, 0, 1. For each combination, record the nondimensional applied voltage V_bar and the corresponding nondimensional tip displacement W_tip. Save all computed points to the output CSV. The required case identifiers are:
  - 'classic_Vp_neg1' (classical model, V̄_p = -1)
  - 'classic_Vp_0'   (classical model, V̄_p = 0)
  - 'classic_Vp_1'   (classical model, V̄_p = 1)
  - 'present_Vp_neg1' (present model, V̄_p = -1)
  - 'present_Vp_0'   (present model, V̄_p = 0)
  - 'present_Vp_1'   (present model, V̄_p = 1)
- Output file: `/app/outputs/tip_displacement.csv`
- Format: csv
- Contract: The CSV must contain exactly the columns case, V_bar, W_tip. The case column must use the exact strings listed above.
- Scoring: scored by hidden verifier

### Step 3: Extract pull-in voltages
- Role: scored (load-bearing)
- Action: For each parameter combination below, compute the nondimensional pull‑in voltage V̄_pl using the DQM solver (direct voltage sweep until divergence). The pull‑in voltage is the voltage where the solution diverges or the slope becomes infinite. Write one row per combination to the output CSV using the exact case identifier strings specified.
  Combinations to compute (present model means l_eq=0.7 µm; classic model means l_eq=0):
  (a) V̄_p sweep (Fig. 3): For V̄_p in [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5], compute V̄_pl for both classic and present models. Use default damage D=0, d=1 µm, and include geometric nonlinearity.
    Case strings: 'classic_Vp_neg1.5', 'classic_Vp_neg1.0', 'classic_Vp_neg0.5', 'classic_Vp_0', 'classic_Vp_0.5', 'classic_Vp_1.0', 'classic_Vp_1.5', 'present_Vp_neg1.5', 'present_Vp_neg1.0', 'present_Vp_neg0.5', 'present_Vp_0', 'present_Vp_0.5', 'present_Vp_1.0', 'present_Vp_1.5'.
  (b) Damage D=0.2 (Fig. 6): For V̄_p in the same set [-1.5..1.5], compute V̄_pl for the present model with damage D=0.2 (l_eq=0.7 µm, d=1 µm, geometric nonlinear).
    Case strings: 'present_D0.2_Vp_neg1.5', 'present_D0.2_Vp_neg1.0', 'present_D0.2_Vp_neg0.5', 'present_D0.2_Vp_0', 'present_D0.2_Vp_0.5', 'present_D0.2_Vp_1.0', 'present_D0.2_Vp_1.5'.
  (c) Initial gap sweep (Fig. 7): For default conditions (V̄_p=1, D=0, geometric nonlinear), compute V̄_pl for initial gaps d = 1, 2, 3, 4 µm for both classic and present models.
    Case strings: 'present_nonlinear_d1', 'present_nonlinear_d2', 'present_nonlinear_d3', 'present_nonlinear_d4', 'classic_nonlinear_d1', 'classic_nonlinear_d2', 'classic_nonlinear_d3', 'classic_nonlinear_d4'.
  (d) Geometric nonlinear vs. linear comparison (Fig. 9): With default configuration (present model, l_eq=0.7 µm, V̄_p=1, D=0, d=1 µm), compute V̄_pl for the full nonlinear model and for the geometric linear model (set α=0).
    Case strings: 'present_nonlinear_default', 'present_linear_default'.
- Output file: `/app/outputs/pull_in_voltage.csv`
- Format: csv
- Contract: The CSV must contain exactly the columns case and V_pl. The case column must use the exact strings listed above.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tip_displacement.csv`
- `/app/outputs/pull_in_voltage.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tip_displacement.csv
- path: `/app/outputs/tip_displacement.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of nondimensional tip displacement points for each model and V_p. The case column must be one of the listed values.
- schema:
  - `type`: table
  - `required_columns`: `case`, `V_bar`, `W_tip`
  - `case_values`: `classic_Vp_neg1`, `classic_Vp_0`, `classic_Vp_1`, `present_Vp_neg1`, `present_Vp_0`, `present_Vp_1`

### pull_in_voltage.csv
- path: `/app/outputs/pull_in_voltage.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of nondimensional pull-in voltages for all specified parameter combinations. The case column must be one of the listed values.
- schema:
  - `type`: table
  - `required_columns`: `case`, `V_pl`
  - `case_values`: `classic_Vp_neg1.5`, `classic_Vp_neg1.0`, `classic_Vp_neg0.5`, `classic_Vp_0`, `classic_Vp_0.5`, `classic_Vp_1.0`, `classic_Vp_1.5`, `present_Vp_neg1.5`, `present_Vp_neg1.0`, `present_Vp_neg0.5`, `present_Vp_0`, `present_Vp_0.5`, `present_Vp_1.0`, `present_Vp_1.5`, `present_D0.2_Vp_neg1.5`, `present_D0.2_Vp_neg1.0`, `present_D0.2_Vp_neg0.5`, `present_D0.2_Vp_0`, `present_D0.2_Vp_0.5`, `present_D0.2_Vp_1.0`, `present_D0.2_Vp_1.5`, `present_nonlinear_d1`, `present_nonlinear_d2`, `present_nonlinear_d3`, `present_nonlinear_d4`, `classic_nonlinear_d1`, `classic_nonlinear_d2`, `classic_nonlinear_d3`, `classic_nonlinear_d4`, `present_nonlinear_default`, `present_linear_default`

Notes: All inputs are public constants from Table 1. DQM implementation is the agent's responsibility. The verifier matches submitted values to hidden gold numbers and trends; exact case strings are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tip_displacement.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "V_bar",
          "W_tip"
        ],
        "case_values": [
          "classic_Vp_neg1",
          "classic_Vp_0",
          "classic_Vp_1",
          "present_Vp_neg1",
          "present_Vp_0",
          "present_Vp_1"
        ]
      },
      "description": "Table of nondimensional tip displacement points for each model and V_p. The case column must be one of the listed values."
    },
    {
      "file": "pull_in_voltage.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "V_pl"
        ],
        "case_values": [
          "classic_Vp_neg1.5",
          "classic_Vp_neg1.0",
          "classic_Vp_neg0.5",
          "classic_Vp_0",
          "classic_Vp_0.5",
          "classic_Vp_1.0",
          "classic_Vp_1.5",
          "present_Vp_neg1.5",
          "present_Vp_neg1.0",
          "present_Vp_neg0.5",
          "present_Vp_0",
          "present_Vp_0.5",
          "present_Vp_1.0",
          "present_Vp_1.5",
          "present_D0.2_Vp_neg1.5",
          "present_D0.2_Vp_neg1.0",
          "present_D0.2_Vp_neg0.5",
          "present_D0.2_Vp_0",
          "present_D0.2_Vp_0.5",
          "present_D0.2_Vp_1.0",
          "present_D0.2_Vp_1.5",
          "present_nonlinear_d1",
          "present_nonlinear_d2",
          "present_nonlinear_d3",
          "present_nonlinear_d4",
          "classic_nonlinear_d1",
          "classic_nonlinear_d2",
          "classic_nonlinear_d3",
          "classic_nonlinear_d4",
          "present_nonlinear_default",
          "present_linear_default"
        ]
      },
      "description": "Table of nondimensional pull-in voltages for all specified parameter combinations. The case column must be one of the listed values."
    }
  ],
  "notes": "All inputs are public constants from Table 1. DQM implementation is the agent's responsibility. The verifier matches submitted values to hidden gold numbers and trends; exact case strings are required."
}
```

## How you are scored
A hidden verifier independently evaluates each of the two scored artifacts (tip_displacement.csv and pull_in_voltage.csv). For tip displacement, it compares your submitted curves to a reference set of points digitised from the study’s own numerical results; acceptable agreement earns partial credit, with tighter agreement required near pull-in. For pull-in voltages, the verifier checks whether your computed values match reference pull-in numbers within a tolerance and whether the qualitative variation with parameters follows the predictions of the physical model (e.g., the direction of change with a certain parameter must be correct). The two stages carry weights; the final reward is the weighted sum. Simply reporting a number from the paper is not sufficient – the verifier scores the actual output files you produce.
