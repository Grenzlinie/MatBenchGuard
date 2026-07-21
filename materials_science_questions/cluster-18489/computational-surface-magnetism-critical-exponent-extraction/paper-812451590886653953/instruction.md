# Monte Carlo simulation of a modified sine-Gordon SOS model for preroughening scaling analysis

## Problem background
Crystal surfaces can undergo roughening and, in some models, a lower-temperature preroughening (PR) transition where the surface develops a disordered flat (DOF) phase. A modified solid-on-solid (SOS) Hamiltonian with temperature-dependent pinning coefficients can exhibit continuous or first-order PR depending on parameters. When the PR transition is continuous, the interface width (mean-square height fluctuation δh²) is expected to diverge logarithmically with system size L. This task investigates the scaling of δh² at the PR temperature for a specific parameter set (model A) to determine whether the transition is continuous, using Monte Carlo simulations of the SOS model on square lattices of increasing size.

## Approach
The SOS Hamiltonian includes a harmonic nearest-neighbour step-energy term and a site-dependent pinning potential of the form log[1 + β y₂ cos(2πh) + β y₄ cos(4πh)] (normalised by its value at the PR temperature). The temperature-dependent parameters are y₂ = C(T_PR − T) and a constant y₄. For model A, which is expected to yield continuous PR, the parameters are C/k = 0.5, kT_PR/J = 0.5, and y₄/J = 0.1. Monte Carlo simulations are carried out on L×L square lattices with periodic boundary conditions at the reduced PR temperature t = kT/J = 0.5. The simulation uses the Metropolis algorithm with real-valued heights: a random height change is proposed at a site and accepted or rejected based on the energy change. The height-step size is dynamically adjusted to maintain an acceptance ratio near 50%. After equilibration, the mean-square fluctuation δh² = ⟨(h − \bar{h})²⟩ is measured for several system sizes (L = 24, 48, 72). A comparison of δh² against the logarithm of L reveals whether the interface width diverges, thereby confirming continuous PR.

## Reproduction target
Produce a CSV file containing the measured δh² for three square lattice sizes L = 24, 48, 72 at temperature t = 0.5. The file must list each L and its corresponding δh². The hidden verifier will check that δh² increases monotonically with L and will perform a linear regression of δh² against ln(L) to assess whether the scaling is logarithmic. The strength of the logarithmic divergence (the slope) is the primary quantitative outcome that will be compared to the paper's reference value.

## Assets

- Python 3 with numpy: python3, numpy

## Workflow steps

### Step 1: Monte Carlo simulation of SOS model A
- Role: process
- Action: Implement the SOS Hamiltonian (Eq. 3) with parameters C/k=0.5, kT_PR/J=0.5, y4/J=0.1, using the Metropolis algorithm with real-valued heights and periodic boundary conditions. Run simulations on square lattices of sizes L=24,48,72 at reduced temperature t=0.5, adjusting step size for ~50% acceptance, equilibrating and collecting at least 5e5 sweeps. Compute the mean-square height fluctuation δh² for each system size.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Scored artifact: δh² scaling data
- Role: scored (load-bearing)
- Action: Write a CSV file containing the measured δh² for each system size L (24,48,72) at t=0.5.
- Output file: `/app/outputs/delta_h2_scaling.csv`
- Format: csv
- Contract: L (int), delta_h2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_h2_scaling.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_h2_scaling.csv
- path: `/app/outputs/delta_h2_scaling.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV file containing mean-square height fluctuation delta_h2 for system sizes L=24,48,72 at temperature t=0.5.
- schema:
  - `type`: table
  - `required_columns`: `L`, `delta_h2`
  - `notes`: L is integer system size; delta_h2 is float mean-square height fluctuation.

Notes: The checker computes ln(L) and performs ordinary linear regression to extract the slope, then compares it to the hidden paper-reported value using a relative tolerance. The delta_h2 values must increase monotonically with L.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_h2_scaling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "delta_h2"
        ],
        "notes": "L is integer system size; delta_h2 is float mean-square height fluctuation."
      },
      "description": "CSV file containing mean-square height fluctuation delta_h2 for system sizes L=24,48,72 at temperature t=0.5."
    }
  ],
  "notes": "The checker computes ln(L) and performs ordinary linear regression to extract the slope, then compares it to the hidden paper-reported value using a relative tolerance. The delta_h2 values must increase monotonically with L."
}
```

## How you are scored
An automated verifier reads your submitted `delta_h2_scaling.csv`. It first validates the file's presence and format (columns L and delta_h2, at least three rows for L=24,48,72). It then checks that delta_h2 increases with L. Next, it computes ln(L), performs ordinary linear regression of delta_h2 on ln(L), and extracts the slope. This slope is compared to a hidden reference slope derived from the paper, using a tolerance that accounts for implementation differences. Your final score is a weighted combination of the correctness of the monotonic trend and the agreement of the slope with the reference. You are not given the reference slope or the tolerance.

## Omitted components

The original paper also presents a dual Coulomb gas (CG) model and its Monte Carlo simulation results (dielectric constant, charge fractions). These CG stages are omitted because the CG model is an exact mathematical dual of the SOS Hamiltonian; its phase behavior is fully determined by the same temperature-dependent parameters already simulated. The CG observables are not needed to reproduce the primary evidence for continuous preroughening, which is the logarithmic divergence of δh². Including them would duplicate computational effort without adding independent verification, so the task focuses on the SOS model scaling signature.
