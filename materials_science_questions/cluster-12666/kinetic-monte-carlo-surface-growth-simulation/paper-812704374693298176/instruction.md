# Kinetic Monte Carlo Ising Model Simulation and Kolmogorov-Avrami Theory Validation

## Problem background
The Kolmogorov-Avrami (KA) theory describes the kinetics of a phase transformation, where growing nuclei impinge and "geometric interaction" accounts for the overlap. The central relation expresses the transformed area fraction \(X(t)\) in terms of an extended area fraction \(X_{\text{ext}}(t)\) that would be occupied if nuclei grew independently and overlapped without interaction. While the model works at small fractions, its validity at large fractions — where percolation occurs and nuclei physically interact — remains debated. This task examines the KA model using a 2D Ising ferromagnet driven by Metropolis dynamics. The system starts metastable with all spins down; upward-pointing spins nucleate and grow under an applied field. Two scenarios are considered: (1) homogeneous nucleation, where nuclei appear spontaneously in the bulk, and (2) a prenucleated system, where a known density of square seed clusters is placed initially, and spontaneous nucleation is suppressed. The key question is whether the KA description holds for arbitrary large transformed fractions, well beyond the percolation threshold, or whether it breaks down when growing interfaces become kinetically smooth. You will compute the magnetization and percolation area fraction for both scenarios and compare to the KA prediction.

## Approach
You will implement kinetic Monte Carlo (Metropolis) simulations on a 1000×1000 square Ising lattice with periodic boundary conditions. The spin-flip dynamics are governed by an energy function that includes nearest-neighbour ferromagnetic couplings and an external field \(h\) that favours up spins. For each condition, record the magnetization \(M(t) = (N_{\text{up}} - N_{\text{down}})/N_{\text{total}}\) as a function of time, measured in full lattice updates (Monte Carlo steps), until the system is nearly fully transformed (\(M \ge 0.99\)). While running, detect percolation: identify the first moment the largest up-spin cluster spans the lattice in either the horizontal or vertical direction, and capture the transformed area fraction \(X_{\text{perc}}\) at that instant.

The two required conditions are:
- Homogeneous nucleation at temperature \(T=0.8\) and field \(h=0.88\), starting from an all-down state. Use standard Metropolis dynamics that allow spontaneous up-flips.
- Prenucleated (breakdown) case at \(T=0.4\) and \(h=0.6\). Here you must use truncated Metropolis dynamics: a spin may only flip up if it is not surrounded by four down neighbours, effectively suppressing homogeneous nucleation. The initial configuration contains square seeds of side \(m_0=5\) placed randomly at an areal density of \(1.1\times10^{-3}\).

For comparison, you will rely on the KA model of geometric interaction. The model expresses the transformed area \(X(t) = 1 - \exp[-X_{\text{ext}}(t)]\). The extended area \(X_{\text{ext}}(t)\) is built from a phenomenological description of nucleation and growth. The growth of a single nucleus is captured by a function \(m(t)\) that accounts for an initial smooth phase before the interface roughens; the nucleation rate can include a transient induction period. The combined expression for \(X_{\text{ext}}\) involves both the preexisting seeds and homogeneous nucleation. The necessary growth and nucleation parameters (\(a\), \(b\), steady-state nucleation rate \(J_{st}\), induction time \(t_0\), and seed density) are provided in this task description. You do not need to fit these parameters; they will be used by the hidden checker to compute the KA prediction. Your simulations provide the actual magnetization and percolation area fractions.

## Reproduction target
Produce the following artifacts:
- For the homogeneous nucleation condition (\(T=0.8, h=0.88\)): a CSV file containing two columns (time \(t\) and magnetization \(M\)) recording the full time series until the magnetization reaches at least 0.99. Additionally, record the percolation area fraction at the instant the largest up-spin cluster first spans the lattice.
- For the prenucleated breakdown condition (\(T=0.4, h=0.6\)): a CSV file in the same two‑column format, again until \(M \ge 0.99\), together with its percolation area fraction.
- A JSON file summarising both percolation area fractions.

Your simulated magnetization curves will be compared against the KA prediction. The percolation area fractions will also be evaluated against reference values. The objective is to determine whether the KA model holds for the homogeneous nucleation case, and whether it breaks down for the prenucleated low‑temperature case, based on the agreement between simulation and the KA description.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Simulate homogeneous nucleation
- Role: scored
- Action: Implement Metropolis dynamics on a 1000×1000 square Ising lattice with periodic boundary conditions, all spins initially down. Use temperature T=0.8 and field h=0.88. Record magnetization M(t) = (N_up - N_down)/N_total as a function of time (measured in full lattice updates) until M >= 0.99. Detect percolation: identify the time when the largest up-spin cluster first spans the lattice in either direction, and record the transformed area fraction at that instant.
- Output file: `/app/outputs/homogeneous_T0.8_h0.88_simulation.csv`
- Format: csv
- Contract: t (float, time step), M (float, magnetization), no header
- Scoring: scored by hidden verifier

### Step 2: Simulate prenucleated system (breakdown)
- Role: scored
- Action: Implement truncated Metropolis dynamics that forbids the flip of any spin surrounded by four down spins, preventing homogeneous nucleation. Use a 1000×1000 lattice, T=0.4, h=0.6. Initialize with square seeds of side m0=5 randomly placed at an areal density 1.1e-3. Run similarly, record M(t) until M >= 0.99, detect percolation, and record the corresponding area fraction.
- Output file: `/app/outputs/breakdown_T0.4_h0.6_simulation.csv`
- Format: csv
- Contract: t (float, time step), M (float, magnetization), no header
- Scoring: scored by hidden verifier

### Step 3: Compile percolation results
- Role: scored (load-bearing)
- Action: Read the percolation area fractions detected during the two simulations above and write them as a JSON object with keys 'homogeneous_T0.8_h0.88' and 'breakdown_T0.4_h0.6'.
- Output file: `/app/outputs/percolation_results.json`
- Format: json
- Contract: {"homogeneous_T0.8_h0.88": float, "breakdown_T0.4_h0.6": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homogeneous_T0.8_h0.88_simulation.csv`
- `/app/outputs/breakdown_T0.4_h0.6_simulation.csv`
- `/app/outputs/percolation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homogeneous_T0.8_h0.88_simulation.csv
- path: `/app/outputs/homogeneous_T0.8_h0.88_simulation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Magnetization time series for homogeneous nucleation at T=0.8, h=0.88.
- schema:
  - `type`: table
  - `required_columns`: `t`, `M`
  - `header`: False
  - `columns`:
    - `name`: t
    - `type`: float
    - `description`: time in full lattice updates
    - `name`: M
    - `type`: float
    - `description`: magnetization

### breakdown_T0.4_h0.6_simulation.csv
- path: `/app/outputs/breakdown_T0.4_h0.6_simulation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Magnetization time series for prenucleated system at T=0.4, h=0.6.
- schema:
  - `type`: table
  - `required_columns`: `t`, `M`
  - `header`: False
  - `columns`:
    - `name`: t
    - `type`: float
    - `description`: time in full lattice updates
    - `name`: M
    - `type`: float
    - `description`: magnetization

### percolation_results.json
- path: `/app/outputs/percolation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Percolation area fractions for the two simulation conditions.
- schema:
  - `type`: object
  - `required`: `homogeneous_T0.8_h0.88`, `breakdown_T0.4_h0.6`
  - `properties`:
    - `homogeneous_T0.8_h0.88`:
      - `type`: number
    - `breakdown_T0.4_h0.6`:
      - `type`: number
  - `additionalProperties`: False

Notes: The checker recomputes the mean absolute error between the agent's M(t) and the KA-predicted magnetization for each condition. The percolation fractions are compared to hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homogeneous_T0.8_h0.88_simulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "M"
        ],
        "header": false,
        "columns": [
          {
            "name": "t",
            "type": "float",
            "description": "time in full lattice updates"
          },
          {
            "name": "M",
            "type": "float",
            "description": "magnetization"
          }
        ]
      },
      "description": "Magnetization time series for homogeneous nucleation at T=0.8, h=0.88."
    },
    {
      "file": "breakdown_T0.4_h0.6_simulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "M"
        ],
        "header": false,
        "columns": [
          {
            "name": "t",
            "type": "float",
            "description": "time in full lattice updates"
          },
          {
            "name": "M",
            "type": "float",
            "description": "magnetization"
          }
        ]
      },
      "description": "Magnetization time series for prenucleated system at T=0.4, h=0.6."
    },
    {
      "file": "percolation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "homogeneous_T0.8_h0.88",
          "breakdown_T0.4_h0.6"
        ],
        "properties": {
          "homogeneous_T0.8_h0.88": {
            "type": "number"
          },
          "breakdown_T0.4_h0.6": {
            "type": "number"
          }
        },
        "additionalProperties": false
      },
      "description": "Percolation area fractions for the two simulation conditions."
    }
  ],
  "notes": "The checker recomputes the mean absolute error between the agent's M(t) and the KA-predicted magnetization for each condition. The percolation fractions are compared to hidden reference values."
}
```

## How you are scored
A hidden verifier independently processes your submitted CSV files and the JSON file. For each magnetization time series, the verifier computes the KA‑predicted magnetization curve using the provided growth and nucleation parameters, then quantifies the deviation between your simulated \(M(t)\) and the KA prediction across the common time range. The percolation area fractions are compared to reference values. Each scored artifact carries a weight, and the final reward is a weighted combination of these evaluations. A solution that properly runs the Monte Carlo simulations and records the required data will be scored accordingly; simply reporting numbers without executing the simulations is not sufficient. The verifier does not require your code or logs — only the specified output files.
