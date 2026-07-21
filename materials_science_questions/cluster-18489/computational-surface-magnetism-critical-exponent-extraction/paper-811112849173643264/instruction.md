# Surface Magnetism Critical Exponent Extraction via Mean-Field Ising Model

## Problem background
Surface magnetic properties of semi-infinite ferromagnets can differ markedly from those in the bulk because surface atoms have a different coordination environment and possibly altered exchange couplings. In the mean-field approximation, an Ising spin-1/2 model with several surface exchange constants (different from the bulk J) predicts two qualitatively different types of surface phase transitions: an ordinary transition where the surface orders at the bulk Curie temperature, and an extraordinary transition where the surface has its own higher Curie temperature. For certain parameter regimes the model also produces a compensation point where the surface magnetization changes sign below the bulk Curie temperature, mimicking anomalous surface signals observed in some magnetic materials. The goal of this task is to compute the exact critical coupling conditions that separate ordinary from extraordinary behavior, to determine the surface Curie temperature for given exchange ratios, and to solve the full temperature-dependent layer magnetization profile for a physically motivated set of parameters.

## Approach
The model is a semi-infinite Ising spin-1/2 system on an fcc(111) surface, characterized by in-plane coordination Z0=6 and inter-plane coordination Z1=3 (bulk coordination Z=Z0+2Z1=12). Up to three surface exchange constants are allowed to differ from the bulk J: J00 (surface plane), J01 (between surface and first subsurface plane), and J11 (first subsurface plane). In the single-site mean-field approximation, minimizing the free energy yields a set of coupled nonlinear equations for the layer magnetizations η_i. Near the critical temperature the equations can be linearized, and the condition for a non-trivial surface solution leads to an infinite tridiagonal determinant whose limit gives an exact algebraic relation among the critical ratios J00/J, J01/J, J11/J for the onset of the extraordinary transition. When the surface couplings place the system outside this critical surface, the surface Curie temperature T_CS can be obtained by treating the infinite determinant via a continued fraction, which reduces to a cubic equation in T_CS/T_C. The temperature dependence of the layer magnetizations themselves is obtained by iteratively solving the full nonlinear mean-field equations for a finite stack of layers (here four layers, beyond which the magnetization is indistinguishable from the bulk). Two practical average magnetization signals are defined to mimic experimental observables: a three-layer sum η_0+η_1+η_2, and a surface‑layer‑model η_0+2η_bulk, where η_bulk is the bulk magnetization at the same temperature.

## Reproduction target
You are to reproduce the three main theoretical results of the mean-field analysis:

1. **Critical surface classification**: For a regular grid of the exchange ratios (J00/J, J01/J, J11/J) that spans the region of interest, evaluate the exact critical condition derived from the infinite linearized determinant (with Z0=6, Z1=3, n→∞). Classify each point as extraordinary (1) if it leads to a surface disordering above the bulk Curie temperature, or ordinary (0) otherwise. Save the grid and the binary classification.

2. **Surface Curie temperature computation**: For a set of (a,b,c) parameter points defined from the surface couplings via a = Z0(J00−J)/(Z1 J), b = Z0(J11−J)/(Z1 J), c = J01/J, solve the cubic equation that emerges from the continued‑fraction method to obtain the surface Curie temperature relative to the bulk, T_CS/T_C. Save the parameter triplets and the corresponding T_CS/T_C.

3. **Magnetization profile for the antiferromagnetic coupled system**: Using the specific exchange ratios J00 = 1.645 J, J01 = −1.282 J, J11 = J, solve the nonlinear mean-field layer equations (four layers, i=0,1,2,3) on a dense grid of reduced temperature T/T_C ranging from well below T_C to above T_CS. For each temperature compute the layer magnetizations η_0, η_1, η_2, the three‑layer average η_0+η_1+η_2, and the surface‑layer‑model average η_0+2η_bulk (where η_bulk is obtained from the bulk mean-field equation at the same T/T_C). Save the temperature scan with all magnetization columns.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute bulk Curie temperature
- Role: process
- Action: Compute the bulk Curie temperature T_C = Z J / k_B using the fcc(111) coordination numbers Z0=6, Z1=3 (Z=12) and a chosen energy scale (e.g., J/k_B = 1), providing the temperature scale for all later steps.
- Evidence: `/app/outputs/bulk_Tc.txt`

### Step 2: Determine critical surface coupling grid
- Role: scored
- Action: For a regular grid of (J00/J, J01/J, J11/J) values covering the ranges specified in the instruction, evaluate the critical surface condition derived from the linearized determinant (infinite surface of tridiagonal matrix) to classify each point as extraordinary (surface orders above bulk T_C) or ordinary (surface orders at same T_C). Output a CSV with the grid and the binary classification.
- Output file: `/app/outputs/critical_surface.csv`
- Format: csv
- Contract: J00_div_J: float, J01_div_J: float, J11_div_J: float, is_critical: int (1 = extraordinary, 0 = ordinary)
- Scoring: scored by hidden verifier

### Step 3: Compute surface Curie temperature via continued fraction
- Role: scored
- Action: For a set of (a, b, c) parameter points obtained from the surface exchange ratios J00/J, J01/J, J11/J through the definitions a = Z0(J00-J)/(Z1 J), b = Z0(J11-J)/(Z1 J), c = J01/J, solve the cubic equation derived from the continued‑fraction method to obtain the surface Curie temperature relative to the bulk, T_CS / T_C. Output a CSV of the results.
- Output file: `/app/outputs/T_CS_values.csv`
- Format: csv
- Contract: a: float, b: float, c: float, T_CS_div_T_C: float
- Scoring: scored by hidden verifier

### Step 4: Solve layer magnetization vs temperature for Gd parameters
- Role: scored (load-bearing)
- Action: Solve the nonlinear mean‑field self‑consistent equations for four layers (i=0,1,2,3) with coupling constants J00=1.645J, J01=-1.282J, J11=J, over a dense range of reduced temperature T/T_C from well below T_C to above T_CS. Compute the layer magnetizations η_0, η_1, η_2 and the two average surface signals: seven-layer average η* = η_0+η_1+η_2 and the surface‑layer‑model average η* = η_0+2η_bulk, where η_bulk is the bulk magnetization at the same temperature. Output a CSV with the temperature profile.
- Output file: `/app/outputs/magnetization_profile.csv`
- Format: csv
- Contract: T_div_T_C: float, eta_0: float, eta_1: float, eta_2: float, eta_avg_3layers: float, eta_avg_surface_layer_model: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_surface.csv`
- `/app/outputs/T_CS_values.csv`
- `/app/outputs/magnetization_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_surface.csv
- path: `/app/outputs/critical_surface.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Grid classification of extraordinary vs ordinary surface transition. The checker recomputes the critical condition for hidden points and compares is_critical.
- schema:
  - `type`: table
  - `required_columns`: `J00_div_J`, `J01_div_J`, `J11_div_J`, `is_critical`

### T_CS_values.csv
- path: `/app/outputs/T_CS_values.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface Curie temperature ratio computed from the continued‑fraction cubic equation. The checker solves the same equation for given (a,b,c) and compares T_CS_div_T_C within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `a`, `b`, `c`, `T_CS_div_T_C`

### magnetization_profile.csv
- path: `/app/outputs/magnetization_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature‑dependent magnetizations for the Gd parameter set. The checker solves the nonlinear mean‑field equations for a set of hidden temperatures and compares all magnetizations, also verifying the compensation point.
- schema:
  - `type`: table
  - `required_columns`: `T_div_T_C`, `eta_0`, `eta_1`, `eta_2`, `eta_avg_3layers`, `eta_avg_surface_layer_model`

Notes: The experimental Gd magnetization data are not scored; only the model predictions are verified. All computed quantities are dimensionless ratios based on the stated lattice coordination numbers and exchange ratios.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_surface.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "J00_div_J",
          "J01_div_J",
          "J11_div_J",
          "is_critical"
        ]
      },
      "description": "Grid classification of extraordinary vs ordinary surface transition. The checker recomputes the critical condition for hidden points and compares is_critical."
    },
    {
      "file": "T_CS_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "a",
          "b",
          "c",
          "T_CS_div_T_C"
        ]
      },
      "description": "Surface Curie temperature ratio computed from the continued‑fraction cubic equation. The checker solves the same equation for given (a,b,c) and compares T_CS_div_T_C within tolerance."
    },
    {
      "file": "magnetization_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_T_C",
          "eta_0",
          "eta_1",
          "eta_2",
          "eta_avg_3layers",
          "eta_avg_surface_layer_model"
        ]
      },
      "description": "Temperature‑dependent magnetizations for the Gd parameter set. The checker solves the nonlinear mean‑field equations for a set of hidden temperatures and compares all magnetizations, also verifying the compensation point."
    }
  ],
  "notes": "The experimental Gd magnetization data are not scored; only the model predictions are verified. All computed quantities are dimensionless ratios based on the stated lattice coordination numbers and exchange ratios."
}
```

## How you are scored
A hidden verifier will score each of your three output artifacts independently and combine the scores into a final reward between 0 and 1. The verifier works by recomputing the underlying quantities:

- **critical_surface.csv**: The verifier will evaluate the critical condition on a set of hidden (J00/J, J01/J, J11/J) points and check whether your binary labels match the recomputed classification.
- **T_CS_values.csv**: The verifier will solve the same cubic equation for the given (a,b,c) points and compare your T_CS/T_C values within an appropriate relative tolerance.
- **magnetization_profile.csv**: The verifier will recompute the layer magnetizations for the same exchange parameters at a set of hidden temperatures and compare your reported magnetizations and average signals, also verifying that the compensation behaviour (sign change of η_0 below T_C) is present.

Simply reporting numbers that look like those in a publication is not sufficient; the verifier only rewards results that can be produced by a correct implementation of the mean-field theory described above.
