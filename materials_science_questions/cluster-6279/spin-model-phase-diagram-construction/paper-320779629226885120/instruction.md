# Monte Carlo Study of Phase Transitions in the Antiferromagnetic Ising Model with Next-Nearest-Neighbor Interactions

## Problem background
The antiferromagnetic Ising model on a square lattice with competing nearest‑neighbour (J1<0) and next‑nearest‑neighbour (J2<0) interactions exhibits frustration and is a cornerstone system for studying order‑disorder phase transitions. Whether the low‑temperature ordered phase is reached by a first‑order or a continuous (second‑order) transition for different coupling ratios r = J2/J1 remains a debated question. Determining the transition order is important for understanding universality classes and the role of frustration in spin models. This task targets a quantitative Monte Carlo investigation of the transition signatures for two representative coupling ratios.

## Approach
The system is described by the Hamiltonian H = -J1 Σ_{⟨ij⟩} S_i S_j - J2 Σ_{⟨il⟩} S_i S_l on a square lattice with periodic boundary conditions and Ising spins S_i = ±1 (J1<0, J2<0). Reproduce the experiment by implementing a replica‑exchange Monte Carlo (parallel tempering) algorithm that swaps configurations between adjacent temperature replicas using a Metropolis acceptance criterion based on the energy difference. For each run, track the total energy and the sublattice magnetizations; the order parameter is derived from the four sublattice magnetizations. After equilibration, collect a long production chain for lattice sizes L = 20, 40, 80, 120, 150 at coupling ratios r = 0.2 and 0.7. From the trajectories, compute the temperature-dependent fourth‑order Binder cumulants: U_L = 1 - ⟨m⁴⟩/(3⟨m²⟩²) for the order parameter and V_L = 1 - ⟨E⁴⟩/(3⟨E²⟩²) for the energy. Determine the critical temperature T_N as the average intersection point of the U_L(T) curves for different system sizes. Additionally, at T_N for L = 150, construct the energy histogram by binning the sampled energies. The whole workflow produces a single scored JSON artifact containing T_N, the cumulant curves, and the histogram.

## Reproduction target
For coupling ratios r = 0.2 and r = 0.7, compute the critical temperature T_N and the following quantitative indicators: (i) the fourth-order Binder cumulant U_L(T) curves for lattice sizes L = 20, 80, 150 and determine T_N from their intersection; (ii) the energy cumulant V_L(T) for L = 150 and note its value at the lowest simulated temperature; (iii) the energy histogram at T_N for L = 150 and count the number of peaks. Package all results in a single JSON file `results.json` under `/app/outputs` as specified in the output contract.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Replica Exchange Monte Carlo Simulation
- Role: process
- Action: Implement the antiferromagnetic Ising model on a square lattice with periodic boundary conditions (J1<0, J2<0). Use replica exchange Monte Carlo. Run simulations for lattice sizes L ∈ {20, 40, 80, 120, 150} and coupling ratios r ∈ {0.2, 0.7}. For each (L,r) collect trajectories of total energy and sublattice magnetizations. Retain raw data for post-processing.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Thermodynamic Analysis and Phase Transition Determination
- Role: scored (load-bearing)
- Action: From the raw simulation data, compute the order parameter m from sublattice magnetizations, the Binder cumulants U_L = 1 - <m^4>/(3<m^2>^2) and V_L = 1 - <E^4>/(3<E^2>^2) as functions of temperature for every L (at least L=20,80,150) and r. Determine the critical temperature T_N for each r as the average intersection temperature of U_L(T) curves for different L. Compute the energy histogram at T_N for L=150. Write all results to results.json according to the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON file containing the critical temperature, Binder cumulant data (U and V), and energy histogram for r=0.2 and r=0.7. The checker recomputes T_N from U_data, checks V_data low-T limit, and verifies the histogram shows a single peak.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact containing the critical temperature, Binder cumulant curves, and energy histogram for two coupling ratios. The checker will recompute T_N from U_data intersection, verify V_L(T) trend, and count histogram peaks.
- schema:
  - `type`: object
  - `required`:
    - `r0.2`:
      - `type`: object
      - `required`: `T_N`, `U_data`, `V_data`, `histogram`
    - `r0.7`:
      - `type`: object
      - `required`: `T_N`, `U_data`, `V_data`, `histogram`
  - `items`:
    - `T_N`: float
    - `U_data`:
      - `type`: object
      - `required_keys`: `L20`, `L80`, `L150`
      - `L20`:
        - `T`: array<float>
        - `U`: array<float>
      - `L80`:
        - `T`: array<float>
        - `U`: array<float>
      - `L150`:
        - `T`: array<float>
        - `U`: array<float>
    - `V_data`:
      - `type`: object
      - `required_keys`: `L20`, `L80`, `L150`
      - `L20`:
        - `T`: array<float>
        - `V`: array<float>
      - `L80`:
        - `T`: array<float>
        - `V`: array<float>
      - `L150`:
        - `T`: array<float>
        - `V`: array<float>
    - `histogram`:
      - `bins`: array<float>
      - `counts`: array<int>
  - `units`: T_N: unitless (k_B T / |J|); U and V: dimensionless; histogram for L=150 at T_N

Notes: The task requires reproducing the simulation and analysis for r=0.2 and r=0.7 only. The full phase diagram over all r is not required. The simulation must produce statistically converged data; the exact number of MC steps is not mandated. All temperatures and cumulants use reduced units k_B T / |J|.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "r0.2": {
            "type": "object",
            "required": [
              "T_N",
              "U_data",
              "V_data",
              "histogram"
            ]
          },
          "r0.7": {
            "type": "object",
            "required": [
              "T_N",
              "U_data",
              "V_data",
              "histogram"
            ]
          }
        },
        "items": {
          "T_N": "float",
          "U_data": {
            "type": "object",
            "required_keys": [
              "L20",
              "L80",
              "L150"
            ],
            "L20": {
              "T": "array<float>",
              "U": "array<float>"
            },
            "L80": {
              "T": "array<float>",
              "U": "array<float>"
            },
            "L150": {
              "T": "array<float>",
              "U": "array<float>"
            }
          },
          "V_data": {
            "type": "object",
            "required_keys": [
              "L20",
              "L80",
              "L150"
            ],
            "L20": {
              "T": "array<float>",
              "V": "array<float>"
            },
            "L80": {
              "T": "array<float>",
              "V": "array<float>"
            },
            "L150": {
              "T": "array<float>",
              "V": "array<float>"
            }
          },
          "histogram": {
            "bins": "array<float>",
            "counts": "array<int>"
          }
        },
        "units": "T_N: unitless (k_B T / |J|); U and V: dimensionless; histogram for L=150 at T_N"
      },
      "description": "Scored artifact containing the critical temperature, Binder cumulant curves, and energy histogram for two coupling ratios. The checker will recompute T_N from U_data intersection, verify V_L(T) trend, and count histogram peaks."
    }
  ],
  "notes": "The task requires reproducing the simulation and analysis for r=0.2 and r=0.7 only. The full phase diagram over all r is not required. The simulation must produce statistically converged data; the exact number of MC steps is not mandated. All temperatures and cumulants use reduced units k_B T / |J|."
}
```

## How you are scored
A hidden verifier independently processes your `results.json`. It recomputes the critical temperature from the intersection of the U_L curves for L = 20, 80, 150, checks the low‑temperature behaviour of V_L for L = 150, verifies the structure of the energy histogram for L = 150 (e.g., peak count), and evaluates the relative trend of T_N between different r values. The reward is a weighted combination of these checks, with the intersection‑based recomputed T_N carrying the highest weight. Simply reporting numbers is insufficient; the verifier recomputes the key quantities from your raw data.
