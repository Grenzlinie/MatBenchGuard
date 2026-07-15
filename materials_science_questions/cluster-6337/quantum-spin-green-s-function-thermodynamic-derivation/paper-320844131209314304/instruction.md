# Ising Model Thermodynamics via Static Fluctuation Approximation

## Problem background
The Ising model is a canonical model of ferromagnetism in statistical mechanics. The static fluctuation approximation (SFA) provides a self-consistent closed system of equations for the magnetization, pair correlations, and thermodynamic properties. You will implement the SFA for the spin‑1/2 Ising model with nearest‑neighbour ferromagnetic exchange and zero external field, for the 2D square lattice and the 3D simple cubic lattice. By solving these equations numerically, you will obtain physical quantities that probe the accuracy of the SFA method against known exact (2D) and numerical (3D) results. This capability is valuable for applying SFA to more complex magnetic systems.

## Approach
The SFA method replaces the dynamic fluctuations of the local field with their static expectation values, yielding a closed set of non‑linear equations that involve a lattice Green function G(p). The lattice structure enters through G(p): for the 2D square lattice it can be expressed analytically via the complete elliptic integral of the first kind, while for the 3D simple cubic lattice it requires numerical integration over the Brillouin zone. For each lattice you will solve the self‑consistent equations (magnetization, local‑field dispersion, and a relation linking them) using root‑finding. The solution is parametrised by a variable p; scanning p gives the reduced temperature X = T/J and magnetization μ over the full temperature range, including the critical region where μ→0. The critical temperature is obtained in the limit p→1. You will then extract the magnetization curve at prescribed X points and determine the critical temperatures for both lattices.

## Reproduction target
Produce the magnetization curve μ(X) for the 2D square‑lattice Ising model at reduced temperatures X = T/J from 0.5 to 4.0 in steps of 0.1, and determine the critical temperature X_c = T_c/J for the 2D square lattice and for the 3D simple cubic lattice. Write the magnetization curve as a CSV file and the two critical temperatures as a plain text file, as detailed in the workflow steps below.

## Assets

- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute lattice Green functions
- Role: process
- Action: Implement and evaluate the lattice Green function G(p) for the 2D square lattice (z=4, λ=1, γ(k)=(cos kx + cos ky)/2) using the complete elliptic integral of the first kind, and for the 3D simple cubic lattice (z=6, λ=1/6, γ(k)=(cos kx+cos ky+cos kz)/3) using numerical integration over the Brillouin zone. Produce callable functions or arrays that return G(p) for any p in [0,1].
- Evidence: none

### Step 2: Solve SFA self-consistent equations
- Role: process
- Action: Numerically solve the SFA closed system of equations (22a–22c) with zero external field for both lattices. For each lattice, treat p as an independent parameter, compute B(p) and X(p) via root-finding, and determine the magnetization μ(p). Generate dense arrays of (p, X, μ) covering the full temperature range, including the critical region where μ→0.
- Evidence: none

### Step 3: Write 2D magnetization curve
- Role: scored (load-bearing)
- Action: From the 2D solution arrays, output a CSV file with columns X (reduced temperature T/J) and μ (magnetization) for X from 0.5 to 4.0 in steps of 0.1. Use linear interpolation if necessary to obtain μ at the requested X points. Write the file to '2d_magnetization.csv'.
- Output file: `/app/outputs/2d_magnetization.csv`
- Format: csv
- Contract: CSV with header: X, mu. X values from 0.5 to 4.0 in steps of 0.1. mu is a float between 0 and 1.
- Scoring: scored by hidden verifier

### Step 4: Determine critical temperatures
- Role: scored (load-bearing)
- Action: Extract the critical temperature X_c = T_c/J for each lattice. This can be obtained as the X value where μ becomes zero, or by solving the system at p=1 using the lattice Green function value G(p=1). Write a text file with two lines: first line X_c for the 2D square lattice, second line X_c for the 3D simple cubic lattice. Write to 'critical_temperatures.txt'.
- Output file: `/app/outputs/critical_temperatures.txt`
- Format: txt
- Contract: Two lines, each containing a float. First line: X_c_2d, second line: X_c_3d.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/2d_magnetization.csv`
- `/app/outputs/critical_temperatures.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### 2d_magnetization.csv
- path: `/app/outputs/2d_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Magnetization μ as a function of reduced temperature X=T/J for the 2D square-lattice Ising model in SFA.
- schema:
  - `type`: table
  - `required_columns`: `X`, `mu`

### critical_temperatures.txt
- path: `/app/outputs/critical_temperatures.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical temperatures X_c = T_c/J for the 2D and 3D Ising models in the SFA.
- schema:
  - `type`: text
  - `description`: First line: critical temperature for 2D square lattice (float), second line: critical temperature for 3D simple cubic lattice (float).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "2d_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "X",
          "mu"
        ]
      },
      "description": "Magnetization μ as a function of reduced temperature X=T/J for the 2D square-lattice Ising model in SFA."
    },
    {
      "file": "critical_temperatures.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "First line: critical temperature for 2D square lattice (float), second line: critical temperature for 3D simple cubic lattice (float)."
      },
      "description": "Critical temperatures X_c = T_c/J for the 2D and 3D Ising models in the SFA."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently evaluates each of your scored artifacts. For the magnetization curve, the verifier computes the mean absolute error between your submitted μ values and a reference curve (the exact Onsager solution) at the same X points. For the critical temperatures, the verifier compares your submitted values to hidden gold values representing the SFA predictions. Full credit is awarded when your values fall within generous but finite tolerance windows, and partial credit may be given for larger but still reasonable deviations. The stage weights are: magnetization curve 40%, 2D critical temperature 30%, 3D critical temperature 30%. Simply reporting the expected numbers without genuinely executing the SFA workflow will not produce the correct computed artifacts that the verifier expects.
