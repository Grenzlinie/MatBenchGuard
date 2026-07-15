# Effective Shear Properties of Porous Ceramics with Bimodal Pore Distribution

## Problem background
Brittle porous ceramics, such as nanocrystalline yttria-stabilized zirconia, often exhibit a bimodal pore size distribution. The effective shear strength and shear modulus of these materials depend not only on the total porosity but also on how porosity is partitioned between the two pore-size classes. Understanding this dependence is important for tailoring ceramics for specific mechanical applications. This task reproduces a movable cellular automata (MCA) mesoscale model that simulates simple shear of 2D ceramic specimens with explicit bimodal pores and computes the resulting effective shear properties τ and G as functions of total porosity Ct and the partial porosity ratio C2/Ct.

## Approach
The approach uses a two-dimensional plane-strain movable cellular automata (MCA) method. A square specimen of side 60 μm is discretised into automata of size 1.2 μm. Bimodal pores are modelled by removing automata: a single automaton for a small pore (diameter 1.2μm) and a central automaton plus its six nearest neighbours for a large pore (diameter 3.6μm). For each combination of total porosity Ct and the fraction of porosity due to large pores (C2/Ct), multiple stochastic realizations are generated with random but non-overlapping pore placements that satisfy C1 + C2 = Ct. Each specimen is subjected to simple shear: the bottom automaton layer is fixed, the top layer is driven with a sinusoidal velocity ramp up to 0.5 m/s, and periodic boundary conditions are applied laterally. Automata respond elastically with shear modulus 32 GPa, Poisson ratio 0.3, and compressive strength 1750 MPa. Bond rupture occurs when a local shear-stress intensity exceeds a calibrated threshold. From the resulting shear-stress versus shear-angle diagram of each realization, the effective shear strength τ_i (peak stress) and effective shear modulus G_i (initial linear slope) are extracted. Ensemble averages over nine realizations yield the properties τ and G for each (Ct, C2/Ct) combination.

## Reproduction target
Produce a CSV file containing the ensemble-averaged effective shear strength τ (in GPa) and shear modulus G (in GPa) for total porosities Ct = 0.075, 0.15, and 0.223. For each Ct, evaluate the properties for a set of C2/Ct values that covers the full range from 0 to 1 (for example, 0, 0.25, 0.5, 0.75, 1). For every (Ct, C2/Ct) combination, generate nine independent stochastic pore-structure realizations, run the MCA shear simulation on each, extract the per-specimen τ_i and G_i, and compute the arithmetic mean τ and G. The final output must be written to `/app/outputs/effective_properties.csv` with columns: Ct, C2_over_Ct, tau_mean (GPa), G_mean (GPa).

## Assets

- Python scientific stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Generate stochastic pore structures
- Role: process
- Action: For each combination of total porosity Ct (0.075, 0.15, 0.223) and a set of C2/Ct values (e.g., 0, 0.25, 0.5, 0.75, 1), generate nine independent stochastic realizations of a 60 μm square specimen discretized into 1.2 μm automata. Create small pores (diameter 1.2 μm) by removing single automata; large pores (diameter 3.6 μm) by removing an automaton and its six nearest neighbors. Ensure C1 = Ct - C2 and random spatial distributions.
- Evidence: `/app/outputs/specimen_log.txt`

### Step 2: Run MCA shear simulations
- Role: process
- Action: For each generated specimen, run a 2D plane strain movable cellular automata simulation of simple shear. Use the following: automata shear modulus G=32 GPa, Poisson ratio ν=0.3, compressive strength 1750 MPa; shear loading: top layer velocity sinusoidally ramped to 0.5 m/s, bottom layer fixed; periodic lateral boundaries; inter-automaton bond rupture governed by shear stress intensity threshold calibrated to the compressive strength. Record the shear stress–shear angle response.
- Evidence: `/app/outputs/simulation_diagrams.csv`

### Step 3: Extract per-specimen τ_i and G_i
- Role: process
- Action: From each simulated shear stress–shear angle diagram, extract the effective shear strength τ_i as the maximum specific resistance (peak stress) and the effective shear modulus G_i as the slope of the linear part of the curve.
- Evidence: `/app/outputs/per_specimen_properties.csv`

### Step 4: Compute ensemble-averaged effective properties
- Role: scored (load-bearing)
- Action: For each (Ct, C2/Ct) combination, compute τ_mean = arithmetic mean of the nine τ_i values, and G_mean = arithmetic mean of the nine G_i values. Write the results to effective_properties.csv with columns: Ct, C2_over_Ct, tau_mean (GPa), G_mean (GPa).
- Output file: `/app/outputs/effective_properties.csv`
- Format: csv
- Contract: CSV with columns: Ct (float), C2_over_Ct (float), tau_mean (float, units: GPa), G_mean (float, units: GPa). Each row corresponds to one porosity combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_properties.csv
- path: `/app/outputs/effective_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Averaged effective shear strength τ and shear modulus G for each (Ct, C2/Ct) combination. The checker recomputes accuracy by comparing these values to the paper's analytical predictions and checking monotonicity trends.
- schema:
  - `type`: table
  - `required_columns`: `Ct`, `C2_over_Ct`, `tau_mean`, `G_mean`
  - `units`:
    - `tau_mean`: GPa
    - `G_mean`: GPa

Notes: The agent must run the full MCA pipeline; the analytical fitting stage is not required. The hidden checker uses the paper's analytical expressions (Eqs. 1-2) as reference curves and scores based on relative tolerance of the simulated values plus trend consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ct",
          "C2_over_Ct",
          "tau_mean",
          "G_mean"
        ],
        "units": {
          "tau_mean": "GPa",
          "G_mean": "GPa"
        }
      },
      "description": "Averaged effective shear strength τ and shear modulus G for each (Ct, C2/Ct) combination. The checker recomputes accuracy by comparing these values to the paper's analytical predictions and checking monotonicity trends."
    }
  ],
  "notes": "The agent must run the full MCA pipeline; the analytical fitting stage is not required. The hidden checker uses the paper's analytical expressions (Eqs. 1-2) as reference curves and scores based on relative tolerance of the simulated values plus trend consistency."
}
```

## How you are scored
A hidden verifier inspects your submitted `/app/outputs/effective_properties.csv`. It checks that the file contains the required columns and that you covered the specified Ct values and a sufficient spread of C2/Ct ratios. The verifier then independently assesses the consistency of your reported τ and G values. This assessment may compare your ensemble-averaged properties to expected physical trends (for example, monotonicity with respect to Ct and C2/Ct) and may compute derived reference quantities. You are rewarded when your simulated properties faithfully reflect the underlying physics. Reporting numbers without actually running the full MCA pipeline will not pass, because the verifier examines the entire parameter sweep and expects physically reasonable values and trends that emerge only from a correct implementation of the mesoscale model.
