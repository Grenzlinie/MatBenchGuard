# Monte Carlo Simulation of Diluted Antiferromagnet with Tethered Ensemble and Critical Exponent Extraction

## Problem background
The three-dimensional diluted antiferromagnet in an applied magnetic field (DAFF) is the prime experimental realisation of the random-field Ising model (RFIM). Despite extensive study, the nature of its phase transition and the values of its critical exponents remain controversial. Canonical Monte Carlo simulations are hampered by huge free‑energy barriers and severe self‑averaging violations, which lead to metastable behaviour and systematically biased estimates. Tethered Monte Carlo (TMC) addresses both problems by constraining smooth order parameters, eliminating the need to tunnel over barriers and restoring self‑averaging through a disorder‑averaged effective potential. In this task you will re‑implement the TMC protocol for the three‑dimensional DAFF and compute a comprehensive set of critical properties, including the correlation‑length ratio ξ/L, the free‑energy barrier ΔF, and the critical exponents β/ν, ν<sub>h</sub>, ν<sub>T</sub>, and θ.

## Approach
The method couples the DAFF Hamiltonian to two tethered ‘bath’ fields that fix smoothed magnetisations (m̂, m̂<sub>s</sub>) at every Monte Carlo step, removing the large free‑energy barriers between ordered and disordered phases. For each disorder sample the tethered expectation values ⟨b̂⟩ and ⟨b̂<sub>s</sub>⟩ are collected on a grid of (m̂, m̂<sub>s</sub>) points. These fields are the gradient of the Helmholtz effective potential Ω̂<sub>N</sub>(m̂, m̂<sub>s</sub>), which is then reconstructed by numerical integration. Averaging Ω̂<sub>N</sub> over disorder samples yields the disorder‑averaged effective potential. Saddle‑point equations link m̂ to the applied field h, and the canonical correlation length ξ and the free‑energy barrier ΔF are extracted from the averaged potential. Critical exponents are obtained by the quotients method: intersection points h*(L) of ξ/L curves for pairs (L, 2L) give field‑driven exponents β/ν and ν<sub>h</sub> through derivatives of ξ and the staggered magnetisation; the temperature‑driven exponent ν<sub>T</sub> is obtained from the temperature dependence of ξ at fixed h. The hyperscaling‑violation exponent θ is determined by fitting the barrier ΔF = A L<sup>θ</sup>.

## Reproduction target
Implement the full Tethered Monte Carlo workflow for the three‑dimensional DAFF on cubic lattices of linear size L = 8, 12, 16, 24, 32 with quenched occupation probability p = 0.7 and periodic boundary conditions. For every size generate the required number of disorder samples (1000 for L ≤ 24, 700 for L = 32). At temperature T = 1.6, run independent tethered simulations on a grid of roughly 5 m̂ values and ~30 m̂<sub>s</sub> values per m̂. Reconstruct the disorder‑averaged effective potential, determine the saddle‑point relation m̂(h) for h<sub>s</sub> → 0⁺, and compute the second‑moment correlation length ξ, the free‑energy barrier ΔF, and the critical exponents β/ν, ν<sub>h</sub>, ν<sub>T</sub>, and θ via the quotients method. The output must consist of three files placed under /app/outputs: (1) `xi_over_L_data.csv` with columns L, h, xi_over_L, error_xi_over_L; (2) `barrier_data.json` containing the per‑L barriers ΔF/N and their errors, plus the fitted θ and its error; (3) `critical_exponents.json` providing per‑pair intersection fields and exponent estimates with errors, as well as final combined estimates. The numerical values must originate from the simulations you run—no pre‑trained models or pre‑computed data are provided.

## Assets

- Python scientific computing environment: numpy, scipy (optionally C compiler for performance)

## Workflow steps

### Step 1: Generate quenched disorder samples
- Role: process
- Action: For each linear size L in {8, 12, 16, 24, 32}, generate random occupation configurations ε_x (occupation probability p=0.7) on a cubic lattice with periodic boundary conditions. Produce 1000 samples for L=8,12,16,24 and 700 samples for L=32.
- Evidence: none

### Step 2: Run Tethered Monte Carlo simulations
- Role: process
- Action: For every disorder sample, perform independent Monte Carlo simulations at fixed smoothed magnetizations (m̂, m̂_s) on a grid of approximately 5 m̂ values and ~30 m̂_s values per m̂. Use the tethered ensemble with the Gaussian smoothing kernel defined in the protocol, at temperature T=1.6. Employ temperature parallel tempering for lattice sizes L≥24. Compute and store the tethered expectation values ⟨b̂⟩ and ⟨b̂_s⟩ at each grid point.
- Evidence: none

### Step 3: Average tethered fields and reconstruct effective potential
- Role: process
- Action: Average the tethered field expectations over all disorder realizations. Numerically integrate the averaged fields to obtain the disorder-averaged Helmholtz effective potential Ω̂_N(m̂, m̂_s). Determine the saddle-point relation m̂(h) in the limit h_s→0+ and compute the canonical observables: correlation length ξ and free-energy barrier ΔF.
- Evidence: none

### Step 4: Compute correlation length ξ/L vs h and save data
- Role: scored
- Action: From the reconstructed observables, compute the second-moment correlation length ξ via the staggered propagator for a range of applied fields h at T=1.6 for each L. Output a CSV with columns L (int), h (float), xi_over_L (float), error_xi_over_L (float).
- Output file: `/app/outputs/xi_over_L_data.csv`
- Format: csv
- Contract: Columns: L (int), h (float), xi_over_L (float), error_xi_over_L (float).
- Scoring: scored by hidden verifier

### Step 5: Compute free-energy barrier and output
- Role: scored
- Action: At the critical field h_c, compute the free-energy barrier per spin ΔF/N by line-integrating the tethered fields along a path from the antiferromagnetic saddle point to the disordered saddle point. Fit the barriers to ΔF = A L^θ and obtain the hyperscaling violation exponent θ. Output a JSON with keys: L (array of integers), Delta_F_over_N (array of floats), error_Delta_F (array of floats), theta_estimate (float), theta_error (float), fit_range (string).
- Output file: `/app/outputs/barrier_data.json`
- Format: json
- Contract: JSON object with keys: L (array of integers), Delta_F_over_N (array of floats), error_Delta_F (array of floats), theta_estimate (float), theta_error (float), fit_range (string).
- Scoring: scored by hidden verifier

### Step 6: Extract critical exponents using quotients method
- Role: scored (load-bearing)
- Action: Apply the quotients method to the ξ/L curves at T=1.6: compute the intersection point h*(L) for each pair (L,2L) and extract β/ν and ν_h from derivatives of ξ and the staggered magnetization. Also compute ν_T from the temperature dependence at fixed h=-2.13. Output a JSON with per-size values (with errors) and final estimates of β/ν, ν_h, ν_T, and θ.
- Output file: `/app/outputs/critical_exponents.json`
- Format: json
- Contract: JSON object with arrays: L (int[]), h_star (float[]), h_star_error (float[]), beta_over_nu (float[]), beta_over_nu_error (float[]), nu_h (float[]), nu_h_error (float[]), nu_T (float[]), nu_T_error (float[]); final estimates: final_beta_over_nu (float), final_beta_over_nu_error (float), final_nu_h (float), final_nu_h_error (float), final_nu_T (float), final_nu_T_error (float), final_theta (float), final_theta_error (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/xi_over_L_data.csv`
- `/app/outputs/barrier_data.json`
- `/app/outputs/critical_exponents.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### xi_over_L_data.csv
- path: `/app/outputs/xi_over_L_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV containing ξ/L vs h for each L at T=1.6. Structural audit ensures correct columns and reasonable range; the main scoring is carried out on the derived exponents.

### barrier_data.json
- path: `/app/outputs/barrier_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Free-energy barrier per spin for each L and the fitted θ. Checker compares the barriers and θ to hidden reference values from the paper.

### critical_exponents.json
- path: `/app/outputs/critical_exponents.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical exponents extracted via the quotients method. The checker compares per-size intersection fields and final exponent estimates to hidden paper values within tolerances.

Notes: The three scored artifacts are the final computational outputs of the reproduction. The ξ/L CSV provides raw data for structural checks; the barrier and exponent JSON files carry the main reward through reference comparison to the paper's reported results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "xi_over_L_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {},
      "description": "CSV containing ξ/L vs h for each L at T=1.6. Structural audit ensures correct columns and reasonable range; the main scoring is carried out on the derived exponents."
    },
    {
      "file": "barrier_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {},
      "description": "Free-energy barrier per spin for each L and the fitted θ. Checker compares the barriers and θ to hidden reference values from the paper."
    },
    {
      "file": "critical_exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {},
      "description": "Critical exponents extracted via the quotients method. The checker compares per-size intersection fields and final exponent estimates to hidden paper values within tolerances."
    }
  ],
  "notes": "The three scored artifacts are the final computational outputs of the reproduction. The ξ/L CSV provides raw data for structural checks; the barrier and exponent JSON files carry the main reward through reference comparison to the paper's reported results."
}
```

## How you are scored
A hidden verifier will inspect the three output artifacts you produce. For `xi_over_L_data.csv` it will check the existence of the required columns and examine the crossing behaviour of the ξ/L curves as evidence of a second‑order transition. The contents of `barrier_data.json` and `critical_exponents.json` will be compared against reference values derived from the published work, within tolerances that account for legitimate statistical and implementation differences. The verifier will also check internal consistency (e.g., the barrier ΔF/N should decrease with L, and the intersection fields h*(L) should evolve monotonically). Simply reporting known literature values without running the genuine computation will not satisfy these checks. Each stage contributes to the final score, with the critical‑exponent and barrier stages carrying the largest weight. A correct submission must be produced by faithfully executing the full TMC pipeline, as the hidden tolerances are set to reward genuine simulations rather than guesses.
