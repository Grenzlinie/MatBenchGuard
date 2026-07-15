# Ice Nucleation Free-Energy Barrier Scaling via Classical Nucleation Theory

## Problem background
Water freezing requires the nucleation of an ice phase, which is kinetically hindered by a free-energy barrier. Understanding how this barrier depends on supercooling is crucial for explaining why bulk water can remain liquid well below 0 °C and why ice eventually forms on surfaces or impurities. Classical nucleation theory provides a framework to compute the activation free energy for homogeneous (bulk) and heterogeneous (surface) ice nucleation.

## Approach
Implement the free-energy model of classical nucleation theory. For a d-dimensional compact nucleus of n particles (d = 3 for homogeneous bulk nucleation; d = 2 for heterogeneous surface nucleation), the free energy change is:

G(n) = n Δμ + α_d n^{(d-1)/d} B_d

where Δμ < 0 is the chemical potential difference per molecule between ice and liquid water, B_d > 0 is the free-energy penalty per molecule on the surface (d=3) or perimeter (d=2), and α_d is a geometric prefactor.

For homogeneous (3D) nucleation, assume a spherical nucleus: α₃ = (36π)^{1/3}. For heterogeneous nucleation on a smooth surface (2D), use a square nucleus: α₂ = 4.

The activation free energy G^# is the maximum of G(n) along the nucleation pathway. Compute it analytically from the condition dG/dn = 0. The dimensionless activation free energy is G_dimensionless = G^# / (k_B T_0), where T_0 ≈ 273 K is the equilibrium freezing temperature.

Use the following fixed parameter values:
- B₃ = 0.85 k_B T₀
- B₂ = 0.85 k_B T₀
- The chemical potential difference obeys the linear relation Δμ/(k_B T₀) = –ΔT/100, with ΔT (supercooling) in degrees Celsius.

From these, compute G_dimensionless as a function of ΔT for both the 3D and 2D cases.

## Reproduction target
For each supercooling value ΔT in the set {1, 2, 5, 10, 20, 30, 40, 50} °C:
- Compute the dimensionless activation free energy for homogeneous 3D nucleation (G_dimensionless = G_3D^# / (k_B T_0)).
- Compute the dimensionless activation free energy for heterogeneous 2D nucleation on a smooth surface (G_dimensionless = G_2D_smooth^# / (k_B T_0)).
Write the results to the two scored CSV files specified under Workflow steps.

## Assets
No external datasets, pretrained models, or proprietary tools are needed. All inputs are physical constants given in the task description. The computation can be performed using standard scientific Python libraries (e.g., numpy, scipy).

## Workflow steps

### Step 1: Compute homogeneous 3D nucleation barrier
- Role: scored (load-bearing)
- Action: Using the classical nucleation free-energy expression for a 3D spherical nucleus (geometric prefactor α₃ = (36π)^(1/3)) with B₃ = 0.85 k_B T_0 and the linear relation Δμ/(k_B T_0) = -ΔT/100 (ΔT in degrees Celsius), compute the dimensionless activation free energy G_dimensionless = G_3D^# / (k_B T_0) for each supercooling value ΔT in [1, 2, 5, 10, 20, 30, 40, 50] °C. Write the results to homogeneous_3d_barrier.csv.
- Output file: `/app/outputs/homogeneous_3d_barrier.csv`
- Format: csv
- Contract: CSV file with two columns: delta_T (float, degrees Celsius) and G_dimensionless (float, dimensionless free energy).
- Scoring: scored by hidden verifier

### Step 2: Compute heterogeneous 2D nucleation barrier on smooth surface
- Role: scored
- Action: Using the classical nucleation free-energy expression for a 2D square nucleus (geometric prefactor α₂ = 4) with B₂ = B₃ = 0.85 k_B T_0 and the same Δμ relation, compute the dimensionless activation free energy G_dimensionless = G_2D_smooth^# / (k_B T_0) for each supercooling value ΔT in [1, 2, 5, 10, 20, 30, 40, 50] °C. Write the results to heterogeneous_2d_smooth_barrier.csv.
- Output file: `/app/outputs/heterogeneous_2d_smooth_barrier.csv`
- Format: csv
- Contract: CSV file with two columns: delta_T (float, degrees Celsius) and G_dimensionless (float, dimensionless free energy).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homogeneous_3d_barrier.csv`
- `/app/outputs/heterogeneous_2d_smooth_barrier.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homogeneous_3d_barrier.csv
- path: `/app/outputs/homogeneous_3d_barrier.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Dimensionless activation free energy for homogeneous ice nucleation in bulk water. The agent must compute the barrier from given parameters and classical nucleation theory; the checker compares using the classical nucleation formulas with a per-row relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `delta_T`, `G_dimensionless`
  - `units`:
    - `delta_T`: degrees Celsius
    - `G_dimensionless`: dimensionless (k_B T_0)

### heterogeneous_2d_smooth_barrier.csv
- path: `/app/outputs/heterogeneous_2d_smooth_barrier.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Dimensionless activation free energy for heterogeneous ice nucleation on a smooth surface. The agent computes the barrier from given parameters and classical nucleation theory; the checker compares using the classical nucleation formulas with a per-row relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `delta_T`, `G_dimensionless`
  - `units`:
    - `delta_T`: degrees Celsius
    - `G_dimensionless`: dimensionless (k_B T_0)

Notes: The dimensionless activation free energy G_dimensionless = G^#/(k_B T_0) must be computed using the classical nucleation theory formulas with the provided parameters: B3=0.85 k_B T_0, B2=0.85 k_B T_0, Δμ/(k_B T_0) = -ΔT/100 (ΔT in °C), and appropriate geometric prefactors (α3 = (36π)^(1/3) for 3D spherical nucleus, α2 = 4 for 2D square nucleus).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homogeneous_3d_barrier.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_T",
          "G_dimensionless"
        ],
        "units": {
          "delta_T": "degrees Celsius",
          "G_dimensionless": "dimensionless (k_B T_0)"
        }
      },
      "description": "Dimensionless activation free energy for homogeneous ice nucleation in bulk water. The agent must compute the barrier from given parameters and classical nucleation theory; the checker compares using the classical nucleation formulas with a per-row relative tolerance."
    },
    {
      "file": "heterogeneous_2d_smooth_barrier.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_T",
          "G_dimensionless"
        ],
        "units": {
          "delta_T": "degrees Celsius",
          "G_dimensionless": "dimensionless (k_B T_0)"
        }
      },
      "description": "Dimensionless activation free energy for heterogeneous ice nucleation on a smooth surface. The agent computes the barrier from given parameters and classical nucleation theory; the checker compares using the classical nucleation formulas with a per-row relative tolerance."
    }
  ],
  "notes": "The dimensionless activation free energy G_dimensionless = G^#/(k_B T_0) must be computed using the classical nucleation theory formulas with the provided parameters: B3=0.85 k_B T_0, B2=0.85 k_B T_0, Δμ/(k_B T_0) = -ΔT/100 (ΔT in °C), and appropriate geometric prefactors (α3 = (36π)^(1/3) for 3D spherical nucleus, α2 = 4 for 2D square nucleus)."
}
```

## How you are scored
Each scored CSV file is evaluated independently by a hidden verifier. The verifier recomputes the expected G_dimensionless values from the classical nucleation theory formulas using the provided parameters and tolerances and compares your submitted values pointwise using a relative tolerance. The reward for each file is proportional to the fraction of supercooling points whose relative error is within the tolerance. The total reward is a weighted combination of the per-file scores.
