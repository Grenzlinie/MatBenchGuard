# Monte Carlo Simulation of a Triangular Lattice Gas Model with Competing Interactions

## Problem background
The adsorbate system S/Ru(0001) forms ordered overlayer structures on a triangular lattice, exhibiting a rich phase diagram with multiple coexistence regions and critical points in the coverage range 0<Θ<1/3. A minimal lattice-gas model with repulsive first- and second-neighbour interactions supplemented by a weak attractive third-neighbour interaction is a candidate to explain this behaviour. Reproducing the phase diagram and the temperature dependence of thermodynamic quantities from Monte Carlo simulations of this model is a key step in validating whether such a simple pairwise interaction picture captures the experimental observations.

## Approach
Implement the lattice-gas Hamiltonian H = φ1 Σ_nn c_i c_j + φ2 Σ_nnn c_i c_j + φ3 Σ_nnnn c_i c_j on a triangular lattice with periodic boundary conditions, setting φ1=1, φ2=0.1, φ3=-0.02. Use Glauber dynamics Monte Carlo in the canonical ensemble to sample configurations across a range of chemical potentials μ that cover coverages from near zero up to 1/3, including the μ values that yield the ideal ordered coverages Θ=1/4 and Θ=1/3. For linear system sizes N = 24, 36, 48, 60, 72, 84, 96, accumulate time series of energy and the relevant order parameters (Ψ_p(2×2) and Ψ_√3×√3). From these trajectories compute the specific heat c_N(T) and susceptibility χ_N(T) using the fluctuation-dissipation relations. For each N,μ pair, locate the temperature T_c of the maximum of each observable and its peak value. Perform a finite-size scaling analysis: for the two ideal coverages, fit log(c_max) and log(χ_max) against log(N) to extract the critical exponent ratios α/ν and γ/ν. Using the largest system (N=96) construct the T-Θ phase diagram by tracing the locus of specific-heat maxima and identifying first-order coexistence boundaries through the detection of double-peak structures in the energy probability distribution or through sharp jumps in coverage vs. temperature. Label the resulting boundaries and special points (tricritical points, eutectic point, critical point) accordingly.

## Reproduction target
Produce three CSV files:
- specific_heat_maxima.csv: for each simulated system size N and chemical potential μ, the temperature T_c and maximum specific heat value c_max.
- susceptibility_maxima.csv: for each (N, μ), the temperature T_c and maximum susceptibility value χ_max.
- phase_diagram_points.csv: for the N=96 system, a list of phase boundary points giving temperature T, coverage Θ, chemical potential μ, and a boundary_type label (critical, coexistence_left, coexistence_right, tricritical, eutectic). The file should cover the entire phase diagram in the coverage interval 0<Θ<1/3, including the boundaries of the island phase (region A), the p(2×2) ordered phase, the √3×√3 ordered phase, and the coexistence regions among them.

## Assets

- Python scientific computing stack (numpy, scipy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Monte Carlo simulations of the lattice gas model
- Role: process
- Action: Implement the lattice gas Hamiltonian H = φ1 Σ_nn c_i c_j + φ2 Σ_nnn c_i c_j + φ3 Σ_nnnn c_i c_j on a triangular lattice with periodic boundary conditions using φ1=1, φ2=0.1, φ3=-0.02. Perform Glauber dynamics Monte Carlo simulations for linear system sizes N ∈ {24,36,48,60,72,84,96} and for a range of chemical potentials μ that span the coverage region 0<Θ<1/3, including the μ values that produce the ideal coverages Θ=1/4 and Θ=1/3. For each (N, μ) run long enough to reach equilibrium and collect time series of energy per site and the relevant order parameters (Ψ_{p(2×2)}, Ψ_{√3×√3}) at multiple temperatures.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute thermodynamic observables
- Role: process
- Action: From the saved MC trajectories compute the specific heat c_N(T) and susceptibility χ_N(T) using the fluctuation formulas for each (N, μ). Additionally compute the coverage Θ(T,μ), coverage fluctuations ΔΘ(T), and energy probability distributions P(E) for the N=96 system.
- Evidence: none

### Step 3: Output specific heat maxima
- Role: scored (load-bearing)
- Action: For every simulated (N, μ) pair locate the maximum specific heat value c_max and the temperature T_c at which it occurs. Write the results to a CSV file.
- Output file: `/app/outputs/specific_heat_maxima.csv`
- Format: csv
- Contract: Columns: N (integer), mu (float), T_c (float), c_max (float)
- Scoring: scored by hidden verifier

### Step 4: Output susceptibility maxima
- Role: scored (load-bearing)
- Action: For every simulated (N, μ) pair locate the maximum susceptibility value χ_max and the temperature T_c at which it occurs. Write the results to a CSV file.
- Output file: `/app/outputs/susceptibility_maxima.csv`
- Format: csv
- Contract: Columns: N (integer), mu (float), T_c (float), chi_max (float)
- Scoring: scored by hidden verifier

### Step 5: Output phase diagram points
- Role: scored (load-bearing)
- Action: From the N=96 simulation results construct the T–Θ phase diagram. Identify critical lines (second-order transitions) by connecting specific-heat maxima, first-order coexistence boundaries by detecting double-peak structures in energy histograms or coverage discontinuities, and locate the special points: tricritical points P_tr^A, P_tr^B, P_tr^D, eutectic point P_eut, and critical point P_c^D. Write a CSV file enumerating points that lie on phase boundaries, each labeled with an appropriate boundary_type.
- Output file: `/app/outputs/phase_diagram_points.csv`
- Format: csv
- Contract: Columns: T (float), Theta (float), mu (float), boundary_type (string, one of: critical, coexistence_left, coexistence_right, tricritical, eutectic)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/specific_heat_maxima.csv`
- `/app/outputs/susceptibility_maxima.csv`
- `/app/outputs/phase_diagram_points.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### specific_heat_maxima.csv
- path: `/app/outputs/specific_heat_maxima.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Maximum specific heat values and the temperatures at which they occur for every simulated (N, μ) pair. The checker will recompute critical exponent ratio α/ν from these maxima using finite-size scaling.
- schema:
  - `type`: table
  - `required_columns`: `N`, `mu`, `T_c`, `c_max`

### susceptibility_maxima.csv
- path: `/app/outputs/susceptibility_maxima.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Maximum susceptibility values and the temperatures at which they occur for every simulated (N, μ) pair. The checker will recompute critical exponent ratio γ/ν from these maxima using finite-size scaling.
- schema:
  - `type`: table
  - `required_columns`: `N`, `mu`, `T_c`, `chi_max`

### phase_diagram_points.csv
- path: `/app/outputs/phase_diagram_points.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Points on the T–Θ phase diagram boundaries (critical lines, coexistence boundaries, and special points) determined from the N=96 simulations. The checker will compare the coordinates of the labeled tricritical, eutectic, and critical points to the paper-reported values within a tolerance, and verify the presence of required coexistence regions.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Theta`, `mu`, `boundary_type`

Notes: All three scored files are essential to verify the paper's main claim that the minimal lattice-gas model reproduces the experimental phase diagram. The checker does not rely on any self-reported metrics; it recomputes exponent ratios from the raw maxima and directly compares boundary-point coordinates.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "specific_heat_maxima.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "mu",
          "T_c",
          "c_max"
        ]
      },
      "description": "Maximum specific heat values and the temperatures at which they occur for every simulated (N, μ) pair. The checker will recompute critical exponent ratio α/ν from these maxima using finite-size scaling."
    },
    {
      "file": "susceptibility_maxima.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "mu",
          "T_c",
          "chi_max"
        ]
      },
      "description": "Maximum susceptibility values and the temperatures at which they occur for every simulated (N, μ) pair. The checker will recompute critical exponent ratio γ/ν from these maxima using finite-size scaling."
    },
    {
      "file": "phase_diagram_points.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Theta",
          "mu",
          "boundary_type"
        ]
      },
      "description": "Points on the T–Θ phase diagram boundaries (critical lines, coexistence boundaries, and special points) determined from the N=96 simulations. The checker will compare the coordinates of the labeled tricritical, eutectic, and critical points to the paper-reported values within a tolerance, and verify the presence of required coexistence regions."
    }
  ],
  "notes": "All three scored files are essential to verify the paper's main claim that the minimal lattice-gas model reproduces the experimental phase diagram. The checker does not rely on any self-reported metrics; it recomputes exponent ratios from the raw maxima and directly compares boundary-point coordinates."
}
```

## How you are scored
A hidden verifier will independently assess each scored artifact. For the specific heat and susceptibility maxima, it will perform finite-size scaling on the data to calculate the critical exponent ratios α/ν and γ/ν at the two ideal coverages and judge how closely they match the values expected from the underlying lattice-gas model. For the phase diagram points, it will verify the overall topology—including the presence and correct ordering of the expected phase regions and coexistence boundaries—and compare the coordinates of the labeled special points (tricritical points, eutectic point, critical point) to reference coordinates. The final score is a weighted sum of these assessments, with higher weight given to the accuracy of the critical exponents and the location of the special points.
