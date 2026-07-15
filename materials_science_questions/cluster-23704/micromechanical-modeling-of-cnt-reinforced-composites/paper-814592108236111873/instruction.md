# Percolation and Electrical Conductivity of CNT-Polymer Nanocomposites from Monte Carlo Microstructure Simulations

## Problem background
Carbon nanotube (CNT) reinforced polymer nanocomposites can become electrically conductive when the CNTs form a percolating network. The onset and magnitude of this conduction depend on CNT concentration, geometry (length, diameter, waviness), quantum tunneling through the polymer matrix, and contact resistance at CNT junctions. Predicting the percolation probability and the macroscopic electrical conductivity as functions of CNT volume fraction is essential for designing conductive lightweight materials. This task implements a Monte Carlo methodology that generates stochastic 2D CNT microstructures, models all relevant conduction mechanisms as an equivalent resistor network, and computes both percolation probability and electrical conductivity.

## Approach
The core idea is to treat a representative volume element (RVE) of the composite as a random 2D network of CNT segments, then solve the resulting resistor network. Each fiber is built from straight segments whose lengths follow a Weibull distribution and diameters a log-normal distribution; the waviness of the fiber depends on its total length. The simulation places fibers until a target volume fraction is reached, detects crossings between segments, splits them at crossing points, and adds tunnelling connections when the polymer gap is below a material‑dependent cut‑off. Every network element receives a resistance: intrinsic CNT conductivity is drawn from a metallic/semiconducting mixture, crossing segments get an increased resistance to account for contact resistance, and tunnelling gaps are assigned a resistance that depends exponentially on the gap distance. The resulting conductance matrix is assembled, the nodal voltages are solved by Gauss‑Jordan elimination, and the solution is used to detect percolation (a continuous path from the voltage source to ground) and to compute the RVE’s total current and effective conductivity. Many independent realizations are run at each volume fraction, and the averages yield the percolation probability and mean conductivity curves.

## Reproduction target
Implement the full Monte Carlo pipeline to produce two curves as CSV files:

1. **Percolation probability curve** – use aspect ratio 240, segment‑length parameter g=0.3, with Weibull fiber‑length distribution and log‑normal diameter distribution, and include waviness. Run Monte Carlo realizations at volume fractions covering at least 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04, and 0.05. Report the percolation probability (fraction of realizations that percolate) at each volume fraction.

2. **Conductivity curve** – use a constant intrinsic CNT conductivity of 1×10⁴ S/m for all CNTs, no contact resistance, aspect ratio 100, and a fixed fiber length of 500 nm. Run Monte Carlo realizations at the same volume fractions and report the mean RVE electrical conductivity (S/m) at each volume fraction.

The computational protocol (microstructure generation, interaction detection, resistance assignment, network solving, and Monte Carlo averaging) must be genuinely executed; the final CSVs must be written to the paths specified under “Output files”.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/
- matplotlib: https://pypi.org/project/matplotlib/

## Workflow steps

### Step 1: Generate CNT microstructure
- Role: process
- Action: Generate a 2D CNT network within a square representative volume element (RVE). Use a Weibull distribution for fiber lengths (α=2.4, β=161.74) and a log-normal distribution for diameters (μ=0.02847, σ=0.3363). The maximum angular deviation of each segment is determined from the fiber length by the linear relation y = 0.375x - 7.5 (x in nm, y in degrees). Each fiber is composed of a specified number of straight segments; the orientation of the first segment is random, and subsequent segments deviate randomly within the computed maximum angle.
- Evidence: none

### Step 2: Identify fiber interactions and tunneling paths
- Role: process
- Action: Detect crossing points between segments: if two segment midpoints are closer than the sum of their radii, check signed distances; for crossed segments, split them at the crossing point into sub-segments. Identify tunneling paths: for segment pairs whose nearest distance is below the matrix-dependent cut-off (PE: 2.0 nm, PI: 2.5 nm, PVA: 2.27 nm), insert a tunneling segment between the closest nodes or segment ends.
- Evidence: none

### Step 3: Assign electrical resistances to network elements
- Role: process
- Action: Assign each sub-segment an intrinsic conductivity according to the metallic/semiconducting distribution: 1/3 metallic (10^5 S/m) and 2/3 semiconducting (10 S/m). Compute segment resistance from resistivity, length, and cross-sectional area (solid circular rod). Compute tunneling resistance for each tunneling segment using the tunneling resistance formula with polymer barrier heights (PE: 4.43 eV, PI: 4.56 eV, PVA: 2.58 eV) and a fixed tunnel cross-sectional area. Increase the resistance of crossed segments by 200% to account for contact resistance.
- Evidence: none

### Step 4: Solve resistor network and determine percolation
- Role: process
- Action: Assemble the conductance matrix and current source vector (voltage source at left boundary, ground at right). Apply nodal voltage analysis and solve the linear system using Gauss-Jordan elimination. For each connected component, compute nodal voltages. Determine percolation: the network percolates if there exists a continuous electrical path from the left to the right boundary.
- Evidence: none

### Step 5: Calculate single-run RVE properties
- Role: process
- Action: From the solved network, compute the total current entering the left boundary, the RVE equivalent resistance, and the RVE electrical conductivity using the RVE dimensions (side length, thickness).
- Evidence: none

### Step 6: Monte Carlo loop and aggregation
- Role: process
- Action: Repeat steps 1-5 for a sufficient number of realizations at each volume fraction (at least [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05]) to achieve convergence. For percolation curves, record the percolation outcome (1/0) per realization; for conductivity curves, record the conductivity value per realization. Average over realizations to obtain percolation probability and mean conductivity at each volume fraction.
- Evidence: none

### Step 7: Produce percolation probability curve
- Role: scored (load-bearing)
- Action: Write a CSV file containing two columns: volume_fraction and percolation_probability. Each row corresponds to one volume fraction from the Monte Carlo simulations. Use the parameter set: aspect ratio 240, g=0.3, with fiber length and diameter distributions and waviness.
- Output file: `/app/outputs/percolation_curve.csv`
- Format: csv
- Contract: volume_fraction (float), percolation_probability (float between 0 and 1)
- Scoring: scored by hidden verifier

### Step 8: Produce conductivity curve
- Role: scored (load-bearing)
- Action: Write a CSV file containing two columns: volume_fraction and conductivity. Each row corresponds to one volume fraction from the Monte Carlo simulations. Use the parameter set: constant intrinsic conductivity 1e4 S/m for all CNTs, no contact resistance, aspect ratio 100, fiber length 500 nm.
- Output file: `/app/outputs/conductivity_curve.csv`
- Format: csv
- Contract: volume_fraction (float), conductivity (float, S/m)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/percolation_curve.csv`
- `/app/outputs/conductivity_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### percolation_curve.csv
- path: `/app/outputs/percolation_curve.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Percolation probability vs. CNT volume fraction for AR=240, g=0.3 with length/diameter distributions and waviness. Checker will interpolate at hidden gold volume fractions, compute MAE, and compare to a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `volume_fraction`, `percolation_probability`
  - `units`:
    - `volume_fraction`: dimensionless
    - `percolation_probability`: dimensionless

### conductivity_curve.csv
- path: `/app/outputs/conductivity_curve.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Electrical conductivity vs. CNT volume fraction for constant intrinsic conductivity 1e4 S/m, no contact resistance, AR=100, fiber length 500 nm. Checker will interpolate at hidden gold volume fractions, compute mean absolute log error (MALE), and compare to a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `volume_fraction`, `conductivity`
  - `units`:
    - `volume_fraction`: dimensionless
    - `conductivity`: S/m

Notes: The two scored artifacts require the full pipeline to be genuinely executed; the numerical values cannot be guessed without running the simulations. Both curves use the same MC framework but different parameter sets as specified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "percolation_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume_fraction",
          "percolation_probability"
        ],
        "units": {
          "volume_fraction": "dimensionless",
          "percolation_probability": "dimensionless"
        }
      },
      "description": "Percolation probability vs. CNT volume fraction for AR=240, g=0.3 with length/diameter distributions and waviness. Checker will interpolate at hidden gold volume fractions, compute MAE, and compare to a tolerance."
    },
    {
      "file": "conductivity_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume_fraction",
          "conductivity"
        ],
        "units": {
          "volume_fraction": "dimensionless",
          "conductivity": "S/m"
        }
      },
      "description": "Electrical conductivity vs. CNT volume fraction for constant intrinsic conductivity 1e4 S/m, no contact resistance, AR=100, fiber length 500 nm. Checker will interpolate at hidden gold volume fractions, compute mean absolute log error (MALE), and compare to a tolerance."
    }
  ],
  "notes": "The two scored artifacts require the full pipeline to be genuinely executed; the numerical values cannot be guessed without running the simulations. Both curves use the same MC framework but different parameter sets as specified."
}
```

## How you are scored
A hidden verifier independently reads your two CSV files. For the percolation curve, it interpolates your reported probabilities at reference volume fractions (which are not disclosed) and computes the mean absolute error against hidden reference values. For the conductivity curve, it similarly interpolates your conductivities and computes the mean absolute logarithmic error against hidden reference values. The scores from the two artifacts are combined into an overall reward between 0 and 1 according to predetermined weights. The verifier uses tolerances that account for the stochastic nature of the simulations; you must therefore run enough realizations for convergence. The hidden reference values, weights, and tolerances are never revealed to the solving agent.
