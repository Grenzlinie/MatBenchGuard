# Dynamic Magnetization Grid Computation for a Mean-Field Spin-3/2 Model

## Problem background
The kinetic spin-3/2 Blume–Capel model under a time-dependent oscillating magnetic field can show dynamic phase transitions. The stationary states and the resulting phase diagrams in the temperature–crystal-field plane are determined by the interplay between reduced temperature, crystal-field interaction, and the amplitude of the driving field. Understanding how the magnetization evolves and what types of ordered and disordered phases appear—and where the transitions among them occur—is the core task.

## Approach
Use a mean-field Glauber-type stochastic dynamics to describe the time evolution of the spin-3/2 system. The local spin can take values ±3/2, ±1/2. The master equation with transition probabilities given by detailed balance leads to a single ordinary differential equation for the time-dependent magnetisation m, which depends on the reduced temperature T, the crystal-field parameter d, and a sinusoidal external field of amplitude h and angular frequency ω. After rescaling time (ξ = ω t) and fixing the coordination number z = 4 and the product Ω = τ ω = 2π, the equation reads:

Ω dm/dξ = -m + [3 exp(d/T) sinh(3 (m + h cos ξ)/(2T)) + exp(-d/T) sinh((m + h cos ξ)/(2T))] / [2 exp(d/T) cosh(3 (m + h cos ξ)/(2T)) + 2 exp(-d/T) cosh((m + h cos ξ)/(2T))].

The periodic stationary solution m(ξ) must be found numerically. From it, the dynamic (period-averaged) magnetisation M is computed as M = (1/(2π)) ∫₀²π m(ξ) dξ. By repeating this calculation for many pairs (T, d) at a fixed field amplitude h, one obtains a grid of M(T,d) values that captures the phase structure. This procedure is to be carried out for five different reduced field amplitudes h that probe qualitatively different phase diagram topologies.

## Reproduction target
For each of the five reduced field amplitudes h = 0.125, 0.35, 0.375, 1.3, 1.5, solve the mean-field dynamic equation, compute the dynamic magnetisation M, and produce a CSV file containing rows (T, d, M). The grids must cover a sufficient range of T and d with a resolution that allows reliable identification of phase transitions, different ordered/disordered phases, and special points. The five output files are phase_data_h0p125.csv, phase_data_h0p35.csv, phase_data_h0p375.csv, phase_data_h1p3.csv, and phase_data_h1p5.csv.

## Assets

- Python scientific stack (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Compute dynamic magnetization for h=0.125
- Role: scored (load-bearing)
- Action: Solve the mean-field Glauber dynamic ODE for the spin-3/2 Blume-Capel model with fixed parameters z=4, Ω=2π, and reduced field amplitude h=0.125. Obtain the stationary 2π-periodic magnetization m(ξ) and compute the period-averaged dynamic magnetization M = (1/2π)∫₀²π m(ξ) dξ. Scan a grid of reduced temperature T and crystal-field interaction d, and save the resulting (T, d, M) table.
- Output file: `/app/outputs/phase_data_h0p125.csv`
- Format: csv
- Contract: CSV file with header T,d,M. T (float), d (float), M (float).
- Scoring: scored by hidden verifier

### Step 2: Compute dynamic magnetization for h=0.35
- Role: scored (load-bearing)
- Action: Solve the same ODE with h=0.35, compute M(T,d), and write the CSV.
- Output file: `/app/outputs/phase_data_h0p35.csv`
- Format: csv
- Contract: CSV file with header T,d,M. T (float), d (float), M (float).
- Scoring: scored by hidden verifier

### Step 3: Compute dynamic magnetization for h=0.375
- Role: scored (load-bearing)
- Action: Solve the ODE with h=0.375, compute M(T,d), and write the CSV.
- Output file: `/app/outputs/phase_data_h0p375.csv`
- Format: csv
- Contract: CSV file with header T,d,M. T (float), d (float), M (float).
- Scoring: scored by hidden verifier

### Step 4: Compute dynamic magnetization for h=1.3
- Role: scored (load-bearing)
- Action: Solve the ODE with h=1.3, compute M(T,d), and write the CSV.
- Output file: `/app/outputs/phase_data_h1p3.csv`
- Format: csv
- Contract: CSV file with header T,d,M. T (float), d (float), M (float).
- Scoring: scored by hidden verifier

### Step 5: Compute dynamic magnetization for h=1.5
- Role: scored (load-bearing)
- Action: Solve the ODE with h=1.5, compute M(T,d), and write the CSV.
- Output file: `/app/outputs/phase_data_h1p5.csv`
- Format: csv
- Contract: CSV file with header T,d,M. T (float), d (float), M (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_data_h0p125.csv`
- `/app/outputs/phase_data_h0p35.csv`
- `/app/outputs/phase_data_h0p375.csv`
- `/app/outputs/phase_data_h1p3.csv`
- `/app/outputs/phase_data_h1p5.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_data_h0p125.csv
- path: `/app/outputs/phase_data_h0p125.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dynamic magnetization grid for h=0.125; the checker will reconstruct the phase diagram topology, identify phases and special points, and validate structural correctness.
- schema:
  - `type`: table
  - `required_columns`: `T`, `d`, `M`

### phase_data_h0p35.csv
- path: `/app/outputs/phase_data_h0p35.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dynamic magnetization grid for h=0.35; structural audit of expected phases and transition lines.
- schema:
  - `type`: table
  - `required_columns`: `T`, `d`, `M`

### phase_data_h0p375.csv
- path: `/app/outputs/phase_data_h0p375.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dynamic magnetization grid for h=0.375; structural audit of expected phases and transition lines.
- schema:
  - `type`: table
  - `required_columns`: `T`, `d`, `M`

### phase_data_h1p3.csv
- path: `/app/outputs/phase_data_h1p3.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dynamic magnetization grid for h=1.3; structural audit of expected phases and transition lines.
- schema:
  - `type`: table
  - `required_columns`: `T`, `d`, `M`

### phase_data_h1p5.csv
- path: `/app/outputs/phase_data_h1p5.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dynamic magnetization grid for h=1.5; structural audit of expected phases and transition lines.
- schema:
  - `type`: table
  - `required_columns`: `T`, `d`, `M`

Notes: The checker will perform a T3 structural audit, analyzing the M(T,d) data to classify phases, locate first- and second-order transition lines, and identify tricritical points and the double critical end point. Basic consistency checks (e.g., |M| ≤ 1.5) contribute minor weight. The target is to reproduce the phase diagram topologies described in the source paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_data_h0p125.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "d",
          "M"
        ]
      },
      "description": "Dynamic magnetization grid for h=0.125; the checker will reconstruct the phase diagram topology, identify phases and special points, and validate structural correctness."
    },
    {
      "file": "phase_data_h0p35.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "d",
          "M"
        ]
      },
      "description": "Dynamic magnetization grid for h=0.35; structural audit of expected phases and transition lines."
    },
    {
      "file": "phase_data_h0p375.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "d",
          "M"
        ]
      },
      "description": "Dynamic magnetization grid for h=0.375; structural audit of expected phases and transition lines."
    },
    {
      "file": "phase_data_h1p3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "d",
          "M"
        ]
      },
      "description": "Dynamic magnetization grid for h=1.3; structural audit of expected phases and transition lines."
    },
    {
      "file": "phase_data_h1p5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "d",
          "M"
        ]
      },
      "description": "Dynamic magnetization grid for h=1.5; structural audit of expected phases and transition lines."
    }
  ],
  "notes": "The checker will perform a T3 structural audit, analyzing the M(T,d) data to classify phases, locate first- and second-order transition lines, and identify tricritical points and the double critical end point. Basic consistency checks (e.g., |M| ≤ 1.5) contribute minor weight. The target is to reproduce the phase diagram topologies described in the source paper."
}
```

## How you are scored
Your uploaded CSV files are evaluated by a hidden verifier that independently reconstructs the phase diagram from each (T, d, M) grid. It classifies the phases (paramagnetic, ferromagnetic-3/2, ferromagnetic-1/2, and coexistence regions), determines whether the phase boundaries are first-order or second-order, and locates any multicritical or special points (e.g., tricritical points, double critical end point). The extracted topological structure—presence of required phases, correct nature of transition lines, and occurrence of special points—is compared against reference expectations. The verifier also performs basic consistency checks (for example, that the magnetization magnitude never exceeds 1.5). The combined reward weighs the correctness of the phase diagram topologies across all five field amplitudes; merely reporting a number that happens to match the paper’s published values without a correct underlying grid yields no credit.
