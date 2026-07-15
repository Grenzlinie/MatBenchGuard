# Thermally Activated Dislocation Escape in Metal Whiskers

## Problem background
Metal whiskers are filamentary crystals that grow with an axial dislocation along their length. The elastic interaction between the dislocation and the whisker surface can stabilise the dislocation on the axis, but thermal fluctuations may allow the dislocation to bow out and escape, terminating whisker growth. This task reproduces the kinetic model of thermally activated dislocation escape from an idealised cylindrical whisker. For copper at 700°C and six combinations of whisker radius and dislocation character, we compute the saddle-point configuration of a bowed-out dislocation loop, the corresponding activation energy, the vibration frequency, and the expected escape time. Additionally, we compute the effective driving stresses that act on a dislocation once it intersects the whisker surface for a range of radii.

## Approach
The model treats the whisker as an isotropic elastic cylinder. The dislocation's elastic energy when uniformly displaced from the axis is given by the sum of screw and edge contributions due to Eshelby and Koehler. A critical character angle φ' separates metastable from unstable orientations; only dislocations with edge component less than this critical angle can persist on the axis.

The escape process is modelled by a localised bow-out: the dislocation line adopts a trial displacement profile ξ = h(1-2|z|/c) over a segment of length c. The total energy increase ΔW includes the work against Eshelby's restoring force and the line-tension cost of the longer dislocation. The activation energy ΔW* is the least value of the maximum of ΔW with respect to amplitude h and length c, i.e., the saddle point (h*, c*) where ΔW is maximised in h and minimised in c. The escape time τ from a whisker of length L is estimated as τ = (L/c) ω exp(ΔW*/kT), with the vibration frequency ω computed from the effective mass of the loop.

Once the dislocation reaches the surface, the effective stress driving it further is derived from elasticity and surface energy. Separate expressions apply for the edge and screw components relative to the cylindrical surface; the total stress is a linear combination weighted by the character angle cos φ and sin φ.

All necessary material constants for copper (shear modulus, Poisson's ratio, Burgers vector, density, surface energy, temperature, whisker length) are provided; they are standard literature values. The agent must implement the energy functional, perform a two-parameter numerical saddle-point search for six specified (R, φ) pairs, compute τ, and evaluate the effective stresses for four radii.

## Reproduction target
Produce two numerical tables as CSV files.

1. Escape times and saddle-point parameters for the following six conditions:
   - Whisker axis [110] (character angle φ = 0°): R = 1×10⁻⁷ cm, 3.1×10⁻⁷ cm, 1×10⁻⁶ cm.
   - Whisker axis [111] (φ = 35.25°): R = 1×10⁻⁶ cm, 5.8×10⁻⁶ cm, 1×10⁻⁵ cm.
   For each, compute the saddle-point loop half-length c* (cm), maximum displacement h* (cm), vibration frequency ω (s⁻¹), and the expectation escape time τ (s).
2. Effective driving stresses for copper whiskers of radii R = 1×10⁻⁶, 1×10⁻⁵, 1×10⁻⁴, and 1×10⁻³ cm. Compute the edge-component stress σ_e and screw-component stress σ_s (both in dyne/cm²).

All outputs must be written under /app/outputs with the exact filenames and column schemas specified in the workflow steps and output contract.

## Assets

- NumPy and SciPy: numpy scipy
- Copper material constants

## Workflow steps

### Step 1: Compute critical dislocation character angle
- Role: process
- Action: From the Poisson ratio ν, compute the critical character angle φ' = arctan(sqrt(1-ν)). Verify that the two specified character angles (0° and 35.25°) are below φ', confirming the metastable condition required for the escape model.
- Evidence: none

### Step 2: Compute dislocation escape times and saddle-point parameters
- Role: scored (load-bearing)
- Action: Implement the activation energy functional for a bowed-out dislocation loop using the trial displacement ξ = h(1 - 2|z|/c). For each of the six conditions (φ=0° with R=1e-7, 3.1e-7, 1e-6 cm; φ=35.25° with R=1e-6, 5.8e-6, 1e-5 cm), numerically locate the saddle point (h*, c*) that simultaneously maximizes the energy with respect to h and minimizes it with respect to c. Then compute the vibration frequency ω via the effective mass model and the escape time τ = (L/c) ω exp(ΔW*/kT).
- Output file: `/app/outputs/table1_escape_times.csv`
- Format: csv
- Contract: Columns: Orientation (deg), R (cm), tau (sec), c_star (cm), h_star (cm), omega (sec^-1). Six data rows, with Orientation values 0 and 35.25.
- Scoring: scored by hidden verifier

### Step 3: Compute effective driving stresses
- Role: scored
- Action: For copper whiskers with radii R = 1e-6, 1e-5, 1e-4, 1e-3 cm, compute the effective stresses σ_e and σ_s that act on a dislocation after it intersects the cylindrical surface, using the formulas for edge and screw components with the given material constants and surface energy γ.
- Output file: `/app/outputs/table2_stresses.csv`
- Format: csv
- Contract: Columns: R (cm), sigma_e (dyne/cm^2), sigma_s (dyne/cm^2). Four data rows for the four radii.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1_escape_times.csv`
- `/app/outputs/table2_stresses.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1_escape_times.csv
- path: `/app/outputs/table1_escape_times.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Escape times and saddle-point parameters for the six specified whisker conditions. The checker will recompute τ from the reported c_star, h_star, and omega and compare to a hidden reference; additionally the ratio h_star/R will be checked for consistency.
- schema:
  - `required_columns`: `Orientation`, `R`, `tau`, `c_star`, `h_star`, `omega`
  - `units`:
    - `Orientation`: deg
    - `R`: cm
    - `tau`: sec
    - `c_star`: cm
    - `h_star`: cm
    - `omega`: sec^-1

### table2_stresses.csv
- path: `/app/outputs/table2_stresses.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective stresses for the four whisker radii. The checker will compare the reported values to the paper's published numbers with relative tolerance.
- schema:
  - `required_columns`: `R`, `sigma_e`, `sigma_s`
  - `units`:
    - `R`: cm
    - `sigma_e`: dyne/cm^2
    - `sigma_s`: dyne/cm^2

Notes: All outputs are numerical CSV files produced from a self-contained analytical model using standard material constants. No external datasets are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1_escape_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "Orientation",
          "R",
          "tau",
          "c_star",
          "h_star",
          "omega"
        ],
        "units": {
          "Orientation": "deg",
          "R": "cm",
          "tau": "sec",
          "c_star": "cm",
          "h_star": "cm",
          "omega": "sec^-1"
        }
      },
      "description": "Escape times and saddle-point parameters for the six specified whisker conditions. The checker will recompute τ from the reported c_star, h_star, and omega and compare to a hidden reference; additionally the ratio h_star/R will be checked for consistency."
    },
    {
      "file": "table2_stresses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "R",
          "sigma_e",
          "sigma_s"
        ],
        "units": {
          "R": "cm",
          "sigma_e": "dyne/cm^2",
          "sigma_s": "dyne/cm^2"
        }
      },
      "description": "Effective stresses for the four whisker radii. The checker will compare the reported values to the paper's published numbers with relative tolerance."
    }
  ],
  "notes": "All outputs are numerical CSV files produced from a self-contained analytical model using standard material constants. No external datasets are required."
}
```

## How you are scored
A hidden verifier evaluates each output artifact independently. For the escape-time table, the verifier checks internal consistency (e.g., the ratio h*/R must lie within physically expected bounds) and then recomputes the escape time τ from your reported c*, h*, and ω, comparing the result to a hidden reference with appropriate tolerances. For the stress table, your σ_e and σ_s values are compared directly to hidden reference numbers. The verifier combines the scores of the two artifacts by weight into a final reward in [0, 1]. Reporting pre‑known numbers without producing the correct underlying parameters is not sufficient; the solver must generate the required CSV files that pass these consistency and value checks.
