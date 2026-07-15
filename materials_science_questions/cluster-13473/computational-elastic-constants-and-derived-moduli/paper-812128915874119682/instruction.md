# Computational reproduction of KT melting transition in flexible membranes

## Problem background
Flexible membranes — tensionless two-dimensional sheets that can buckle out of plane — are predicted to exhibit a hexatic phase with quasi-long-range bond-orientational order. The hexatic-to-fluid melting transition is believed to be driven by disclination unbinding. For sufficiently large bending rigidity, the transition is expected to follow Kosterlitz–Thouless (KT) scaling, while at very low bending rigidity it may become first order. The bond-orientational order parameter ψ₆ and its associated susceptibility χ₆ are central observables. The task is to determine, via Monte Carlo simulation of a planar self-avoiding triangulated membrane model, the character of the hexatic-fluid transition for bending rigidities βλ = 1.5, 2, and 3: whether χ₆ follows KT divergence, whether finite‑size scaled data collapse onto a KT universal curve, and whether order‑parameter histograms at βλ = 1.5 exhibit bimodality consistent with a first‑order transition.

## Approach
The membrane is modelled as a planar triangular network of N hard spheres of diameter σ₀ = 1, connected by tethers of maximum extension l₀ < √3, with periodic boundary conditions. The bending energy is E = λ Σ (1 − nᵢ·nⱼ) summed over neighbouring triangles, where nᵢ are triangle normals; the bending rigidity κ relates to λ via κ = λ/√3. Monte Carlo dynamics consist of random bead displacements and tether cuts/reattachments, maintaining zero spreading pressure through occasional area adjustments. For each combination of bending rigidity βλ = 1.5, 2, 3, system size N = 196, 400, 784, and tether length l₀ near the transition, the bond-orientational order parameter ψ₆ = |(1/N_b) Σ exp(6iθ_b)| (where θ_b is the angle of each projected bond) and its second moment ⟨ψ₆²⟩ are recorded. From the data for βλ = 2 and βλ = 3 at N = 784, the bond-orientational susceptibility χ₆ = N⟨ψ₆²⟩ is computed and fitted to the KT divergence form χ₆ = a_χ exp[ b_χ / (l₀ − l₀*)^{1/2} ] for l₀ > l₀* using non‑linear least squares, yielding a_χ, b_χ, and the critical tether length l₀*. Using the fitted parameters, the correlation length ξ₆ = χ₆^{4/7} is computed and scaled quantities are formed to assess data collapse. For βλ = 1.5, normalized histograms of ψ₆ are constructed at the tether length where χ₆ peaks or the distribution becomes bimodal; bimodality with peaks near ψ₆ = 0 and ψ₆ ≈ 0.55 would indicate a discontinuous transition.

## Reproduction target
Perform Monte Carlo simulations for βλ = 1.5, 2, 3 and N = 196, 400, 784 over a range of l₀ spanning the hexatic‑fluid transition. From the simulation data, produce three scored artifacts:
1. `fitted_KT_params.json` – the best‑fit a_χ, b_χ, and l₀* for βλ = 2 and βλ = 3 (using N = 784) obtained from the KT fit.
2. `scaling_data.csv` – for βλ = 2 and βλ = 3 at N = 784, a table containing the scaled susceptibility χ₆/L^{1.75} and the scaling variable ξ₆/L that, together, should demonstrate collapse onto a common KT universal curve.
3. `order_parameter_histograms_beta1.5.csv` – normalized ψ₆ histograms for βλ = 1.5 at the transition l₀ for each system size N = 196, 400, 784; the histograms should be examined for bimodality.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Monte Carlo simulations and order‑parameter recording
- Role: process
- Action: Implement the planar self-avoiding triangulated membrane model with periodic boundary conditions, discretized bending energy (using the standard pair-of-triangles normals form), and bond‑flipping Monte Carlo under constant zero spreading pressure. Run simulations for bending rigidities βλ = 1.5, 2, 3, system sizes N = 196, 400, 784, and a range of tether lengths l₀ that spans the hexatic‑fluid transition region. Record the bond-orientational order parameter ψ₆ and its second moment ⟨ψ₆²⟩ for each configuration, and also collect sequences of ψ₆ values for histogram construction at the transition l₀ for βλ=1.5. Save the aggregated data (simulation trajectories and order‑parameter time series) as evidence.
- Evidence: `/app/outputs/psi6_data.h5`

### Step 2: Kosterlitz‑Thouless fit of susceptibility
- Role: scored (load-bearing)
- Action: From the simulation data for βλ=2 and βλ=3 at N=784, compute the bond-orientational susceptibility χ₆ = N⟨ψ₆²⟩ for each tether length l₀. Fit χ₆ to the Kosterlitz‑Thouless divergence form χ₆ = a_χ exp[ b_χ / (l₀ − l₀*)^{1/2} ] for l₀ > l₀*, using non‑linear least squares. Extract the best‑fit parameters a_χ, b_χ, l₀* and their uncertainties. Write the results to fitted_KT_params.json.
- Output file: `/app/outputs/fitted_KT_params.json`
- Format: json
- Contract: JSON object with keys 'beta_lambda_3' and 'beta_lambda_2'. Each is an object containing fields 'a_chi' (float), 'b_chi' (float), 'l0_star' (float). Optionally error estimates may be included.
- Scoring: scored by hidden verifier

### Step 3: Finite‑size scaling dataset
- Role: scored (load-bearing)
- Action: Using the fitted KT parameters for βλ=2 and βλ=3, compute the correlation length ξ₆ = χ₆^{4/7} for each (βλ, N=784, l₀) point. Construct a CSV file containing for every data point: beta_lambda, L (√N), xi6, chi6, the scaled susceptibility chi6_scaled = χ₆ / L^{1.75}, and the scaling variable xi6_over_L = ξ₆ / L. The resulting scaled data for both bending rigidities should collapse onto a universal curve close to (ξ₆/L)^{1.75}.
- Output file: `/app/outputs/scaling_data.csv`
- Format: csv
- Contract: CSV with columns: beta_lambda (int), L (int), l0 (float), xi6 (float), chi6 (float), chi6_scaled (float), xi6_over_L (float). One row per data point (βλ, N, l₀).
- Scoring: scored by hidden verifier

### Step 4: Order‑parameter histograms for βλ=1.5
- Role: scored (load-bearing)
- Action: For βλ=1.5, identify the transition tether length from the peak in χ₆ or from the l₀ at which the order‑parameter histogram becomes bimodal. At that l₀ for each system size N=196, 400, 784, construct a normalized histogram of the bond-orientational order parameter ψ₆ using a suitable number of bins. Write the histogram as a CSV file with bin boundaries and counts. The histogram must exhibit bimodality (peaks near ψ₆=0 and ψ₆≈0.55).
- Output file: `/app/outputs/order_parameter_histograms_beta1.5.csv`
- Format: csv
- Contract: CSV with columns: N (int), l0 (float), psi6_bin_low (float), psi6_bin_high (float), count (int). Bin boundaries and counts from the normalized histogram.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_KT_params.json`
- `/app/outputs/scaling_data.csv`
- `/app/outputs/order_parameter_histograms_beta1.5.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_KT_params.json
- path: `/app/outputs/fitted_KT_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted KT divergence parameters (a_χ, b_χ, critical tether length l0*) for the two bending rigidities. The checker compares these against the paper's reported values within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `beta_lambda_3`:
      - `type`: object
      - `required_fields`: `a_chi`, `b_chi`, `l0_star`
      - `fields`:
        - `a_chi`: float
        - `b_chi`: float
        - `l0_star`: float
    - `beta_lambda_2`:
      - `type`: object
      - `required_fields`: `a_chi`, `b_chi`, `l0_star`
      - `fields`:
        - `a_chi`: float
        - `b_chi`: float
        - `l0_star`: float

### scaling_data.csv
- path: `/app/outputs/scaling_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Finite‑size scaling data for N=784; the checker verifies that the points collapse onto a universal curve consistent with KT universality.
- schema:
  - `type`: table
  - `required_columns`: `beta_lambda`, `L`, `l0`, `xi6`, `chi6`, `chi6_scaled`, `xi6_over_L`
  - `units`: object

### order_parameter_histograms_beta1.5.csv
- path: `/app/outputs/order_parameter_histograms_beta1.5.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized order‑parameter histograms for βλ=1.5 at the transition tether length for each system size. The checker detects bimodality (peaks near 0 and ~0.55) consistent with a first‑order transition.
- schema:
  - `type`: table
  - `required_columns`: `N`, `l0`, `psi6_bin_low`, `psi6_bin_high`, `count`
  - `units`: object

Notes: All scored artifacts derive from the Monte Carlo simulation data produced in step_01. The checker does not require perfect numerical agreement for the scaling collapse (structural audit) or exact peak positions for bimodality, only robust evidence of the reported physical behaviour.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_KT_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta_lambda_3": {
            "type": "object",
            "required_fields": [
              "a_chi",
              "b_chi",
              "l0_star"
            ],
            "fields": {
              "a_chi": "float",
              "b_chi": "float",
              "l0_star": "float"
            }
          },
          "beta_lambda_2": {
            "type": "object",
            "required_fields": [
              "a_chi",
              "b_chi",
              "l0_star"
            ],
            "fields": {
              "a_chi": "float",
              "b_chi": "float",
              "l0_star": "float"
            }
          }
        }
      },
      "description": "Fitted KT divergence parameters (a_χ, b_χ, critical tether length l0*) for the two bending rigidities. The checker compares these against the paper's reported values within a hidden tolerance."
    },
    {
      "file": "scaling_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta_lambda",
          "L",
          "l0",
          "xi6",
          "chi6",
          "chi6_scaled",
          "xi6_over_L"
        ],
        "units": {}
      },
      "description": "Finite‑size scaling data for N=784; the checker verifies that the points collapse onto a universal curve consistent with KT universality."
    },
    {
      "file": "order_parameter_histograms_beta1.5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "l0",
          "psi6_bin_low",
          "psi6_bin_high",
          "count"
        ],
        "units": {}
      },
      "description": "Normalized order‑parameter histograms for βλ=1.5 at the transition tether length for each system size. The checker detects bimodality (peaks near 0 and ~0.55) consistent with a first‑order transition."
    }
  ],
  "notes": "All scored artifacts derive from the Monte Carlo simulation data produced in step_01. The checker does not require perfect numerical agreement for the scaling collapse (structural audit) or exact peak positions for bimodality, only robust evidence of the reported physical behaviour."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s output artifact, then combines the scores by weight into a final reward. Simply reporting numbers from the paper is not sufficient — the verifier checks the computed artifacts for consistency with the expected physical behaviour:
- `fitted_KT_params.json` is compared against hidden reference values derived from the paper, within an allowable tolerance.
- `scaling_data.csv` is audited for structural collapse: the verifier confirms that the scaled points lie on a universal curve consistent with KT theory.
- `order_parameter_histograms_beta1.5.csv` is audited for bimodality (two well‑separated peaks).
The reward reflects how well the submitted data agree with the expected KT scaling and the presence/absence of a first‑order signature.
