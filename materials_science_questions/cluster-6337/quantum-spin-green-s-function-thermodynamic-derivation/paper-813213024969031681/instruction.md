# Dynamic Phase Transitions in the Spin-2 Ising Model under Oscillating Field: EFT Simulation

## Problem background
This task investigates dynamic (nonequilibrium) phase transitions in a spin-2 Ising model subjected to a time-dependent oscillating magnetic field. The model includes a ferromagnetic exchange interaction, a single-ion crystal-field anisotropy, and a sinusoidal external field. Understanding dynamic transitions in such higher-spin systems is important because magnetic materials often involve ions with spin greater than 1/2, and the interplay of crystal fields, oscillating perturbations, and thermal fluctuations leads to rich phase behavior. The goal is to compute the dynamic order parameter, hysteresis loop area, and dynamic correlation as functions of temperature and field amplitude, and to construct dynamic phase diagrams in the temperature–field plane, classifying transition orders and locating special points where the nature of the transition changes.

## Approach
We use the effective-field theory (EFT) with correlations, which partially accounts for nearest-neighbor spin correlations beyond the ordinary mean-field approximation. Starting from the Glauber stochastic dynamics of the spin-2 Ising model and employing the exact Van der Waerden identity for spin-2, a decoupling approximation is applied to obtain a closed dynamical equation for the average magnetization m(t). The resulting ordinary differential equation (ODE) has the form dm/dt = -m + a0 + a1*m1 + a2*m2 + a3*m3 + a4*m4, where the coefficients a_i depend on temperature, the crystal field D, the coordination number z (taken as 4 for a square lattice), and the instantaneous magnetic field h(t) = h0 sin(wt). The coefficients are derived using the differential-operator shift identity exp(α∇) f(x) = f(x+α). The ODE is numerically integrated over multiple periods of the oscillating field until a steady-state periodic solution is reached. From the steady-state magnetization time series we then compute: (i) the time-averaged dynamic magnetization (the dynamic order parameter), (ii) the hysteresis loop area (energy loss per cycle), and (iii) the dynamic correlation between magnetization and field. To locate dynamic phase transitions, we vary the temperature and the field amplitude h0. A second-order (continuous) transition is signaled by the dynamic magnetization continuously vanishing, while a first-order (discontinuous) transition shows a jump or hysteresis in the temperature dependence. The parameter regimes that produce the two types of transitions are mapped onto a phase diagram in the (T/zJ, h0/zJ) plane. Special points where the transition order changes (tricritical points) are identified from these boundaries.

## Reproduction target
Reproduce the following quantitative results from the EFT dynamic equation on a square lattice (z=4):

1. For crystal field D/|J| = 1.0, field amplitude h0/|J| = 0.1, and frequency w = 2π, compute the dynamic magnetization M, hysteresis loop area A, and dynamic correlation C over a temperature range from low temperature to above the transition. Output these as a table with columns T (temperature in units of |J|), M, A, and C (at least 100 points covering 0 to 12 T/|J|). Determine the second-order transition temperature where M vanishes continuously.

2. For D/|J| = −1.5 and w = 2π, systematically scan temperature T/zJ and field amplitude h0/zJ to locate dynamic transition points. Record each transition point with its classification: 'second' if the magnetization vanishes continuously, 'first' if it exhibits a discontinuity or jump. Output the transition points as a table with columns T_over_zJ, h_over_zJ, and transition_type (at least 50 points covering both first- and second-order boundary segments).

3. From the phase-boundary data, extract the coordinates of the two tricritical points where the transition changes order. Output a table with columns T_over_zJ and h_over_zJ, two rows, one for each tricritical point.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement EFT dynamic equation and numerical solver
- Role: process
- Action: Derive and implement the coefficients a_i (i=0..4) of the effective-field dynamic equation for the spin-2 Ising model using the Van der Waerden identity for spin-2, the decoupling approximation, and the differential-operator shift identity. Implement a numerical ODE solver (e.g., Adams–Moulton predictor-corrector with Romberg integration) to integrate dm/dt = -m + a0 + a1*m1 + a2*m2 + a3*m3 + a4*m4 under the oscillating field h(t)=h0 sin(wt). Use z=4 (square lattice).
- Evidence: none

### Step 2: Compute thermal behavior of dynamic quantities
- Role: scored (load-bearing)
- Action: For D/|J|=1.0, h0/|J|=0.1, w=2π, run the solver over a range of temperatures covering 0 to 12 T/|J| to obtain steady-state magnetization time series m(t). At each temperature, compute the time-averaged dynamic magnetization M, hysteresis loop area A, and dynamic correlation C. Output the results as a CSV table. Also determine the second-order transition temperature Tc where M vanishes continuously.
- Output file: `/app/outputs/thermal_curves.csv`
- Format: csv
- Contract: Temperature dependence of dynamic magnetization M, hysteresis loop area A, and dynamic correlation C for the specified parameters.
- Scoring: scored by hidden verifier

### Step 3: Construct dynamic phase boundaries
- Role: scored
- Action: For D/|J|=-1.5, w=2π, systematically scan temperature T/zJ and field amplitude h0/zJ. At each point, run the solver and classify the dynamic transition order (first-order if M exhibits a discontinuity/jump; second-order if continuous). Compile a table of transition points with their classification.
- Output file: `/app/outputs/phase_boundaries.csv`
- Format: csv
- Contract: Dynamic phase transition lines for D/|J|=-1.5, w=2π, with classification of transition order.
- Scoring: scored by hidden verifier

### Step 4: Identify tricritical points
- Role: scored
- Action: From the phase boundary data obtained in step 3, determine the coordinates of the two dynamic tricritical points where the transition order changes. Output their (T/zJ, h0/zJ).
- Output file: `/app/outputs/tricritical_points.csv`
- Format: csv
- Contract: Coordinates of the two dynamic tricritical points in the phase diagram.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_curves.csv`
- `/app/outputs/phase_boundaries.csv`
- `/app/outputs/tricritical_points.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_curves.csv
- path: `/app/outputs/thermal_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature variation of dynamic magnetization M, hysteresis loop area A, and dynamic correlation C for D/|J|=1.0, h0/|J|=0.1, w=2π. Temperature T is in units of |J|. M is the time-averaged magnetization (Eq. 8). A is the hysteresis loop area (Eq. 9). C is the dynamic correlation (Eq. 10).
- schema:
  - `type`: table
  - `required_columns`: `T`, `M`, `A`, `C`

### phase_boundaries.csv
- path: `/app/outputs/phase_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dynamic phase transition points for D/|J|=-1.5, w=2π. T_over_zJ = T/(zJ), h_over_zJ = h0/(zJ). transition_type is either 'first' or 'second'.
- schema:
  - `type`: table
  - `required_columns`: `T_over_zJ`, `h_over_zJ`, `transition_type`

### tricritical_points.csv
- path: `/app/outputs/tricritical_points.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Coordinates of the two dynamic tricritical points for D/|J|=-1.5, w=2π, in the (T/zJ, h0/zJ) plane.
- schema:
  - `type`: table
  - `required_columns`: `T_over_zJ`, `h_over_zJ`

Notes: All scored outputs are compared against the paper's reported numerical results with appropriate tolerances. The agent must re-implement the EFT dynamic equation from the described method and run the full ODE scanning; no pre-computed lookup tables are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "M",
          "A",
          "C"
        ]
      },
      "description": "Temperature variation of dynamic magnetization M, hysteresis loop area A, and dynamic correlation C for D/|J|=1.0, h0/|J|=0.1, w=2π. Temperature T is in units of |J|. M is the time-averaged magnetization (Eq. 8). A is the hysteresis loop area (Eq. 9). C is the dynamic correlation (Eq. 10)."
    },
    {
      "file": "phase_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_over_zJ",
          "h_over_zJ",
          "transition_type"
        ]
      },
      "description": "Dynamic phase transition points for D/|J|=-1.5, w=2π. T_over_zJ = T/(zJ), h_over_zJ = h0/(zJ). transition_type is either 'first' or 'second'."
    },
    {
      "file": "tricritical_points.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_over_zJ",
          "h_over_zJ"
        ]
      },
      "description": "Coordinates of the two dynamic tricritical points for D/|J|=-1.5, w=2π, in the (T/zJ, h0/zJ) plane."
    }
  ],
  "notes": "All scored outputs are compared against the paper's reported numerical results with appropriate tolerances. The agent must re-implement the EFT dynamic equation from the described method and run the full ODE scanning; no pre-computed lookup tables are provided."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage's output artifact. The final reward is a weighted sum over the scored stages. For thermal_curves.csv, the verifier checks that the temperature range is appropriate, that the dynamic magnetization M decreases from a high value near zero temperature to approximately zero at a critical temperature, that the hysteresis area A shows a peak near the transition, and that the dynamic correlation C exhibits a dip; the exact shapes and the transition temperature are compared against reference values derived from the underlying method within allowed tolerances. For phase_boundaries.csv, the verifier compares the reported transition points and their order classification to reference phase boundaries; a point is considered correct if its coordinates lie within an acceptable fractional deviation from the expected location. For tricritical_points.csv, the verifier checks that two points are present and that their coordinates agree with the expected tricritical locations to within tolerance. Reporting the paper's numbers without actually running the required numerical computations is not sufficient to achieve a high score.
