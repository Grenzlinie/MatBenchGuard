# Numerical Simulation of Surface-Directed Spinodal Decomposition in Thin Films

## Problem background
Surface‑directed spinodal decomposition occurs when a homogeneous binary mixture confined in a thin film is quenched below its critical point. The presence of surfaces breaks translational symmetry and produces oscillatory concentration profiles across the film. This task studies the phenomenon using two theoretical descriptions: a discrete lattice molecular field theory for the Kawasaki spin‑exchange kinetic Ising model, and a continuum time‑dependent Ginzburg–Landau (TDGL) theory with derived surface boundary conditions. The key quantity is the laterally averaged order parameter profile as a function of distance from the walls at different times after the quench. The goal is to compute these profiles and to compare the lattice and continuum approaches under conditions where the bulk correlation length is small (deep quench) and where it approaches a few lattice spacings (near‑critical quench).

## Approach
Two numerical solvers are implemented. The lattice solver integrates the full set of coupled nonlinear kinetic equations for the local magnetization on a simple cubic lattice representing a thin film with 30 layers and periodic lateral dimensions 128×128. It uses the Kawasaki spin‑exchange dynamics with Glauber transition probabilities and treats interactions via nearest‑neighbour couplings, a surface coupling, and a surface field. The TDGL solver solves the conserved order‑parameter equation (model B) on a grid representing the same film geometry, augmented with boundary conditions that are derived by a continuum approximation of the lattice equations. The deep‑quench scenario (reduced temperature k_B T / J = 4, surface field H₁ = J, surface coupling J_s = J) yields rapid concentration variations that the lattice method resolves. The near‑critical scenario (k_B T / J = 5.875) compares the profiles obtained from both methods.

## Reproduction target
Compute and output two sets of laterally averaged order parameter profiles Ψ_av(n) for a film with D+1 = 30 layers, indexed by layer n = 1 … 30.

1. **Deep quench** – from the lattice model at temperature k_B T / J = 4, produce Ψ_av(n) at times t = 50, 500, 2000, 10000.
2. **Near‑critical comparison** – from the lattice model and from the TDGL model at k_B T / J = 5.875, produce Ψ_av(n) at times t = 50, 500, 10000 and list them together, labelling the method.

All profiles must be obtained by averaging over the lateral directions and, for the lattice results, over five independent random initial conditions.

## Assets
No external datasets, pre‑trained models, or proprietary files are required. The necessary simulation code can be written in standard scientific Python (NumPy, SciPy, etc.). All model parameters, equations, and boundary conditions are fully specified in this document.

## Workflow steps

### Step 1: Lattice simulation (deep quench)
- Role: process
- Action: Implement the coupled kinetic equations for local magnetization m_n(ρ,t) on a simple cubic lattice film with D+1=30 layers and periodic lateral dimensions L=128. Use parameters J=1, J_s=1, H_1=1, H=0, k_BT=4. Initialize m_n(ρ,0) uniformly random in [-1,1] with zero total magnetization. Evolve with time step δt=0.1, storing the full magnetization field at times t=50, 500, 2000, 10000.
- Evidence: `/app/outputs/magnetization_fields_deep.npz`

### Step 2: Lattice simulation (near-critical)
- Role: process
- Action: Run the same lattice solver with temperature k_BT=5.875 (near-critical). Save the magnetization field at t=50, 500, 10000.
- Evidence: `/app/outputs/magnetization_fields_near.npz`

### Step 3: TDGL simulation (near-critical)
- Role: process
- Action: Implement the time-dependent Ginzburg-Landau equation with the derived surface boundary conditions on a grid representing the same film geometry (D=29 layers, L=128). Use the near-critical temperature (k_BT=5.875). Initialize with random fluctuations and evolve to t=10000, storing the order parameter field at t=50, 500, 10000.
- Evidence: `/app/outputs/tdgl_fields.npz`

### Step 4: Deep quench averaged profiles
- Role: scored (load-bearing)
- Action: From the raw magnetization fields produced in the deep-quench lattice simulation, compute laterally (over ρ) and ensemble (over 5 independent runs) averaged order parameter Ψ_av(n) for each layer n at times t=50,500,2000,10000. Save as CSV.
- Output file: `/app/outputs/deep_quench_profiles.csv`
- Format: csv
- Contract: CSV with columns: time (int), layer_index (int from 1 to 30), psi_av (float). One row per layer per time.
- Scoring: scored by hidden verifier

### Step 5: Lattice vs TDGL comparison profiles
- Role: scored
- Action: From the raw fields of the near-critical lattice simulation and the TDGL simulation, compute laterally averaged order parameter profiles Ψ_av(n) for each method separately at times t=50,500,10000. Combine into one CSV with a 'method' column.
- Output file: `/app/outputs/comparison_profiles.csv`
- Format: csv
- Contract: CSV with columns: time (int), layer_index (int from 1 to 30), method (string, either 'lattice' or 'tdgl'), psi_av (float). One row per method per layer per time.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deep_quench_profiles.csv`
- `/app/outputs/comparison_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deep_quench_profiles.csv
- path: `/app/outputs/deep_quench_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Laterally averaged order parameter profiles for the deep quench (k_BT/J=4) at four times.
- schema:
  - `type`: table
  - `required_columns`: `time`, `layer_index`, `psi_av`
  - `units`:
    - `psi_av`: dimensionless

### comparison_profiles.csv
- path: `/app/outputs/comparison_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Comparison of laterally averaged order parameter profiles from the lattice model and TDGL theory at near-critical conditions.
- schema:
  - `type`: table
  - `required_columns`: `time`, `layer_index`, `method`, `psi_av`
  - `units`:
    - `psi_av`: dimensionless

Notes: All model parameters and protocol are defined; no external datasets are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deep_quench_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "layer_index",
          "psi_av"
        ],
        "units": {
          "psi_av": "dimensionless"
        }
      },
      "description": "Laterally averaged order parameter profiles for the deep quench (k_BT/J=4) at four times."
    },
    {
      "file": "comparison_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "layer_index",
          "method",
          "psi_av"
        ],
        "units": {
          "psi_av": "dimensionless"
        }
      },
      "description": "Comparison of laterally averaged order parameter profiles from the lattice model and TDGL theory at near-critical conditions."
    }
  ],
  "notes": "All model parameters and protocol are defined; no external datasets are required."
}
```

## How you are scored
A hidden verifier reads the two output CSV files. For the deep‑quench profiles it compares the reported Ψ_av(n) values against a hidden reference at the specified times and layers, using a tolerance that accounts for implementation‑dependent spread. For the comparison profiles it separately checks the lattice and TDGL profiles against its reference and also verifies that the two methods produce internally consistent profiles. Reporting approximate values is not enough – the verifier expects a faithful numerical solution of the required equations under the required conditions. The final reward is a weighted combination of the scores from the two artifacts.
