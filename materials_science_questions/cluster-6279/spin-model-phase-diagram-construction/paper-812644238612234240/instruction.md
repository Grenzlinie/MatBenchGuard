# Monte Carlo Phase Diagram of a Classical XY Antiferromagnet on a Stacked Triangular Lattice

## Problem background
The magnetic phase diagram of a classical XY antiferromagnet on a stacked triangular lattice with weak interplanar coupling (in-plane nearest-neighbor exchange J_∥=1, interplane exchange J_⊥=10) and an in-plane magnetic field H∥x̂ is investigated. At zero field the system orders into a non-collinear helical (120°) spin structure below a Néel temperature T_N. The central question is how an applied in-plane field modifies this phase diagram: whether it separates into distinct magnetically ordered phases near T_N, and what critical behavior governs the zero-field transition. Answering this requires computing the order parameters that distinguish the paramagnetic, linearly polarized (S₁ aligned with the field), and elliptically polarized phases, and extracting the zero-field critical exponent β.

## Approach
The method is Metropolis Monte Carlo simulation of the classical XY Hamiltonian ℋ = J_∥ ∑_{⟨ij⟩} 𝐬_i·𝐬_j + J_⊥ ∑_{⟨lk⟩} 𝐬_l·𝐬_k − ∑_i H s_i^x on an L×L×L stacked triangular (simple hexagonal) lattice with periodic boundary conditions. Lattice sizes L=12 and L=18 are used. For each state point (H,T) the primary Fourier components M_x(Q₁) and M_y(Q₁) of the spin density are computed. Magnetic phases are classified by whether these components are zero or non-zero: paramagnet (M_x≈0, M_y≈0), phase 6 (M_x≠0, M_y=0), phase 7 (M_x≠0, M_y≠0). Second‑order transition boundaries are identified from inflection points in the order‑parameter curves via cubic spline fits. At zero field, finite‑size scaling with the spin‑wave correction M(L)=M(∞)+c/L is applied to the L=12 and L=18 data to obtain the thermodynamic limit order parameter M(∞), from which the critical exponent β is extracted by fitting log M(∞) versus the reduced temperature t = (T_N−T)/T_N. This procedure yields two quantitative outputs: a phase label for each (H,T) test point, and the zero‑field Néel temperature T_N (for L=12) together with β.

## Reproduction target
Reproduce the phase diagram by assigning correct phase labels ('paramagnet', 'phase6', 'phase7') to a supplied set of hidden (H,T) test points covering the region near T_N and small fields. In addition, from the zero‑field simulation data, estimate the Néel temperature T_N for L=12 and the critical exponent β at H=0, reporting them in standard scalar form.

## Assets

- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Monte Carlo simulation and order-parameter measurement
- Role: process
- Action: Run Metropolis Monte Carlo simulations of the classical XY model on a stacked triangular (simple hexagonal) lattice with J_∥=1, J_⊥=10 and in-plane field H∥x̂. The in-plane triangular lattice has nearest‑neighbour distance 1 (distance unit); layers are stacked along z with spacing c = 1. Use periodic boundary conditions on an L×L×L grid with L=12 and L=18. The primary Fourier component wave vector is Q₁ = (4π/(3a)) x̂ + (π/c) ẑ with a=1, c=1 (i.e., Q₁ = (4π/3, 0, π)). Scan temperature and field ranges needed to resolve phase boundaries and the zero-field transition. For each state point (H,T) compute the Fourier components M_x(Q₁) and M_y(Q₁) via Eq. (4) of the paper and record averaged values.
- Evidence: `/app/outputs/simulation_raw_data.json`

### Step 2: Phase‑boundary and TN identification
- Role: process
- Action: From the measured order‑parameter curves, locate second‑order transition points by detecting inflection points using cubic splines. Determine the Néel temperatures T_N(L=12) and T_N(L=18) from the H=0 M(T) curve. Optionally store the identified transition points.
- Evidence: `/app/outputs/transition_points.csv`

### Step 3: Phase classification at hidden test points
- Role: scored (load-bearing)
- Action: The test points are provided in the file /app/inputs/test_points.csv (columns H( float), T(float)). For each row, determine the magnetic phase using your computed primary Fourier components: paramagnet (M_x≈0 and M_y≈0), phase 6 (M_x≠0 and M_y=0), phase 7 (M_x≠0 and M_y≠0). Write the results to /app/outputs/phase_labels.csv with columns H, T, phase_label (one of 'paramagnet', 'phase6', 'phase7') for each test point.
- Output file: `/app/outputs/phase_labels.csv`
- Format: csv
- Contract: Columns: H (float), T (float), phase_label (string, one of 'paramagnet', 'phase6', 'phase7')
- Scoring: scored by hidden verifier

### Step 4: Finite‑size scaling for β and TN
- Role: scored
- Action: Perform finite‑size scaling at H=0 using the L=12 and L=18 order‑parameter data. Apply the spin‑wave correction M(L)=M(∞)+c/L to obtain M(∞) at several reduced temperatures. Fit log M(∞) vs log t to extract the critical exponent β, and also report the zero‑field Néel temperature for L=12. Write critical_params.json with keys T_N and beta.
- Output file: `/app/outputs/critical_params.json`
- Format: json
- Contract: Keys: 'T_N' (float), 'beta' (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_labels.csv`
- `/app/outputs/critical_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_labels.csv
- path: `/app/outputs/phase_labels.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-point phase classification for test points supplied in /app/inputs/test_points.csv; the checker recomputes classification accuracy against hidden gold labels extracted from the paper's Fig. 4.
- schema:
  - `type`: table
  - `required_columns`: `H`, `T`, `phase_label`
  - `items`:
    - `H`: float
    - `T`: float
    - `phase_label`: string (one of 'paramagnet', 'phase6', 'phase7')

### critical_params.json
- path: `/app/outputs/critical_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Estimated zero‑field Néel temperature T_N for L=12 and critical exponent β at H=0, compared to paper‑reported values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `T_N`: float (zero-field Néel temperature, L=12)
    - `beta`: float (critical exponent estimate)
  - `units`:
    - `T_N`: arbitrary units
    - `beta`: dimensionless

Notes: All scored artifacts must be produced by the agent via the simulation and analysis pipeline. The checker will recompute accuracy from phase_labels.csv and compare the critical parameters to paper values. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_labels.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "H",
          "T",
          "phase_label"
        ],
        "items": {
          "H": "float",
          "T": "float",
          "phase_label": "string (one of 'paramagnet', 'phase6', 'phase7')"
        }
      },
      "description": "Per-point phase classification for test points supplied in /app/inputs/test_points.csv; the checker recomputes classification accuracy against hidden gold labels extracted from the paper's Fig. 4."
    },
    {
      "file": "critical_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T_N": "float (zero-field Néel temperature, L=12)",
          "beta": "float (critical exponent estimate)"
        },
        "units": {
          "T_N": "arbitrary units",
          "beta": "dimensionless"
        }
      },
      "description": "Estimated zero‑field Néel temperature T_N for L=12 and critical exponent β at H=0, compared to paper‑reported values with tolerance."
    }
  ],
  "notes": "All scored artifacts must be produced by the agent via the simulation and analysis pipeline. The checker will recompute accuracy from phase_labels.csv and compare the critical parameters to paper values. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your work is evaluated by a hidden verifier that independently scores each scored artifact and combines them into a single reward. The verifier recomputes classification accuracy by comparing your phase_labels.csv entries against the correct phase labels for the hidden test points. It also compares your reported T_N and β against hidden reference values using tolerances. The final reward is a weighted combination of these two components (phase classification accuracy carries the largest weight). Simply reporting numbers is not enough; the verifier recomputes the phase labels from your submitted file and checks the scalar parameters against known reference values, so your simulation and analysis must genuinely reproduce the target quantities. No gold values or tolerances are disclosed here.
