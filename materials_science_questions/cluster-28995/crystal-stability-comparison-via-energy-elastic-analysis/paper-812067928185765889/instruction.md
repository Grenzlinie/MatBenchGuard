# Crystal Stability Comparison via Energy/Elastic Analysis

## Problem background
The ground-state crystal structure of a material—whether it prefers face-centered cubic (f.c.c.) or body-centered cubic (b.c.c.) order—is set by its free energy. Computing the Helmholtz free-energy difference between these two structures at finite temperature is a central challenge in statistical mechanics, because the difference is often tiny compared with the total energy per particle and requires precision methods that go beyond harmonic approximations. Solving this problem for a given interatomic potential yields a quantitative prediction of the stable phase and its dependence on thermodynamic conditions. The present task computes this free-energy difference for two model systems: a Lennard-Jones crystal and a rubidium crystal described by an effective pair potential.

## Approach
Free-energy differences are computed with the method of overlapping distributions and Bennett's acceptance-ratio estimator, using multistage sampling. For each system a linear combination Hamiltonian H(λ)=λ H_fcc + (1−λ) H_bcc is introduced, with intermediate values of λ between 0 and 1 to connect the two end structures. Monte Carlo or molecular dynamics simulations in the canonical or microcanonical ensemble are run at each λ, recording time series of the potential energy of each structure and of the energy difference Δ = V_fcc − V_bcc. The two-sided Bennett formula, which involves a Fermi-function average with an optimized shift constant, is applied to each adjacent λ pair to extract the per-particle free-energy difference δF(λ_i→λ_{i+1}) and its statistical error. The total ΔF is the sum of these interval contributions. For the Lennard-Jones system the temperature and density are chosen so that the entropy difference ΔS = (ΔV − ΔF)/T can also be obtained from the average potential-energy difference ΔV of the end ensembles. The calculation is repeated for a rubidium effective pair potential at standard temperature and pressure, requiring that the volume dependence of that potential be included.

## Reproduction target
Produce the per-particle Helmholtz free-energy difference ΔF between f.c.c. and b.c.c. crystals under the following conditions:
- Lennard-Jones system: T = 0.5, number density ρ = 1.0054, N = 320 particles, interaction cut-off radius Rc = 2.35 (all in reduced Lennard‑Jones units). Use 11 equally spaced λ stages from 0 to 1. For each interval report the per‑particle free‑energy contribution and its statistical error in a CSV file. From the end‑ensemble potential‑energy averages compute ΔV and the entropy difference ΔS = (ΔV − ΔF)/T, and write a summary JSON with the total ΔF, ΔS, and their errors.
- Rubidium system: ρ = 0.92237, T = 0.728 (reduced Rubidium units), N = 144 particles, with the Price et al. effective pair potential. Use 5 equally spaced λ stages. Output the per‑interval ΔF values and a summary JSON containing the total ΔF and its error.
The required output files are: lj_multistage_results.csv, lj_summary.json, rb_multistage_results.csv, rb_summary.json. All energies are per particle.

## Assets

- Lennard-Jones 12-6 pair potential
- Rubidium effective pair potential (Price et al., 1971): 10.1103/PhysRevA.4.358

## Workflow steps

### Step 1: Multistage sampling for LJ and Rb crystals
- Role: process
- Action: Generate perfect f.c.c. and b.c.c. configurations for a 320-particle Lennard-Jones system at T=0.5, rho=1.0054 (reduced units) with cut-off radius Rc=2.35, and for a 144-particle Rubidium system at STP conditions (rho=0.92237, T=0.728) using the Price et al. effective pair potential. Define intermediate Hamiltonians H(lambda)=lambda*H_fcc + (1-lambda)*H_bcc with equally spaced lambda in [0,1] (LJ: 11 stages; Rb: 5 stages). Perform molecular dynamics or Monte Carlo sampling in the canonical or microcanonical ensemble for each lambda, collecting time series of the potential energy of each structure and the energy difference Delta = V_fcc - V_bcc. Record also the total potential energy for the end ensembles to enable Delta_V computation.
- Evidence: `/app/outputs/sampling_log.json`

### Step 2: Compute LJ free-energy differences per stage
- Role: scored (load-bearing)
- Action: Using the recorded energy difference time series for the LJ system, apply Bennett's acceptance-ratio estimator (the two-sided formula with optimized shift constant) to compute the per-particle Helmholtz free-energy difference delta_F for each adjacent lambda pair, together with its statistical error. Output the per-stage results to a CSV file.
- Output file: `/app/outputs/lj_multistage_results.csv`
- Format: csv
- Contract: lambda_start, lambda_end, delta_F_per_particle, error
- Scoring: scored by hidden verifier

### Step 3: LJ free-energy and entropy summary
- Role: scored
- Action: Compute the total free-energy difference per particle (sum of the per-stage values), its statistical error, the potential energy difference DeltaV from the end-ensemble averages, and the entropy difference DeltaS = (DeltaV - DeltaF)/T. Write the results to a JSON file.
- Output file: `/app/outputs/lj_summary.json`
- Format: json
- Contract: {"delta_F": float, "delta_F_error": float, "delta_S": float, "delta_S_error": float}
- Scoring: scored by hidden verifier

### Step 4: Compute Rb free-energy differences per stage
- Role: scored
- Action: Using the recorded energy difference time series for the Rubidium system, apply Bennett's acceptance-ratio estimator to compute the per-particle delta_F for each lambda interval and its error. Output the per-stage results to a CSV file.
- Output file: `/app/outputs/rb_multistage_results.csv`
- Format: csv
- Contract: lambda_start, lambda_end, delta_F_per_particle, error
- Scoring: scored by hidden verifier

### Step 5: Rb free-energy difference summary
- Role: scored
- Action: Compute the total free-energy difference per particle and its statistical error for the Rubidium system. Write the results to a JSON file.
- Output file: `/app/outputs/rb_summary.json`
- Format: json
- Contract: {"delta_F": float, "delta_F_error": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lj_multistage_results.csv`
- `/app/outputs/lj_summary.json`
- `/app/outputs/rb_multistage_results.csv`
- `/app/outputs/rb_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lj_multistage_results.csv
- path: `/app/outputs/lj_multistage_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-interval free-energy contributions for the LJ system. The hidden checker will sum delta_F_per_particle and compare the total to a hidden gold value with an absolute tolerance, and will also verify that column values are numeric and errors are positive.
- schema:
  - `type`: table
  - `required_columns`: `lambda_start`, `lambda_end`, `delta_F_per_particle`, `error`
  - `units`:
    - `delta_F_per_particle`: reduced Lennard-Jones energy unit
    - `error`: reduced Lennard-Jones energy unit

### lj_summary.json
- path: `/app/outputs/lj_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate free-energy and entropy difference for the LJ system. The hidden checker will compare delta_F and delta_S to hidden gold values (paper-reported) with absolute tolerance 0.02 each, and will verify that errors are positive and that the sum of per-stage contributions from the CSV matches the summary delta_F.
- schema:
  - `type`: object
  - `required`:
    - `delta_F`: number
    - `delta_F_error`: number
    - `delta_S`: number
    - `delta_S_error`: number
  - `units`:
    - `delta_F`: reduced Lennard-Jones energy unit
    - `delta_F_error`: reduced Lennard-Jones energy unit
    - `delta_S`: reduced Lennard-Jones unit (k_B)
    - `delta_S_error`: reduced Lennard-Jones unit (k_B)

### rb_multistage_results.csv
- path: `/app/outputs/rb_multistage_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-interval free-energy contributions for the Rb system. The hidden checker will sum delta_F_per_particle and compare the total to a hidden gold value with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `lambda_start`, `lambda_end`, `delta_F_per_particle`, `error`
  - `units`:
    - `delta_F_per_particle`: reduced Rubidium energy unit
    - `error`: reduced Rubidium energy unit

### rb_summary.json
- path: `/app/outputs/rb_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate free-energy difference for the Rb system. The hidden checker will compare delta_F to a hidden gold value (paper-reported) with absolute tolerance 0.02, and will verify that the sum of per-stage contributions from the CSV matches the summary delta_F.
- schema:
  - `type`: object
  - `required`:
    - `delta_F`: number
    - `delta_F_error`: number
  - `units`:
    - `delta_F`: reduced Rubidium energy unit
    - `delta_F_error`: reduced Rubidium energy unit

Notes: All energies are per-particle. The hidden checker also enforces internal consistency: the per-stage delta_F sums must equal the values in the summary JSON files. Scoring weights: LJ delta_F 40%, LJ delta_S 30%, Rb delta_F 30%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lj_multistage_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda_start",
          "lambda_end",
          "delta_F_per_particle",
          "error"
        ],
        "units": {
          "delta_F_per_particle": "reduced Lennard-Jones energy unit",
          "error": "reduced Lennard-Jones energy unit"
        }
      },
      "description": "Per-interval free-energy contributions for the LJ system. The hidden checker will sum delta_F_per_particle and compare the total to a hidden gold value with an absolute tolerance, and will also verify that column values are numeric and errors are positive."
    },
    {
      "file": "lj_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_F": "number",
          "delta_F_error": "number",
          "delta_S": "number",
          "delta_S_error": "number"
        },
        "units": {
          "delta_F": "reduced Lennard-Jones energy unit",
          "delta_F_error": "reduced Lennard-Jones energy unit",
          "delta_S": "reduced Lennard-Jones unit (k_B)",
          "delta_S_error": "reduced Lennard-Jones unit (k_B)"
        }
      },
      "description": "Aggregate free-energy and entropy difference for the LJ system. The hidden checker will compare delta_F and delta_S to hidden gold values (paper-reported) with absolute tolerance 0.02 each, and will verify that errors are positive and that the sum of per-stage contributions from the CSV matches the summary delta_F."
    },
    {
      "file": "rb_multistage_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda_start",
          "lambda_end",
          "delta_F_per_particle",
          "error"
        ],
        "units": {
          "delta_F_per_particle": "reduced Rubidium energy unit",
          "error": "reduced Rubidium energy unit"
        }
      },
      "description": "Per-interval free-energy contributions for the Rb system. The hidden checker will sum delta_F_per_particle and compare the total to a hidden gold value with an absolute tolerance."
    },
    {
      "file": "rb_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_F": "number",
          "delta_F_error": "number"
        },
        "units": {
          "delta_F": "reduced Rubidium energy unit",
          "delta_F_error": "reduced Rubidium energy unit"
        }
      },
      "description": "Aggregate free-energy difference for the Rb system. The hidden checker will compare delta_F to a hidden gold value (paper-reported) with absolute tolerance 0.02, and will verify that the sum of per-stage contributions from the CSV matches the summary delta_F."
    }
  ],
  "notes": "All energies are per-particle. The hidden checker also enforces internal consistency: the per-stage delta_F sums must equal the values in the summary JSON files. Scoring weights: LJ delta_F 40%, LJ delta_S 30%, Rb delta_F 30%."
}
```

## How you are scored
A hidden verifier independently reads each of the four output artifacts. For each system the per‑stage CSV values are summed to obtain a total ΔF, which is compared against a hidden reference; the summary JSON entries are likewise compared. Internal consistency checks verify that the sum of the interval contributions matches the summary value and that all reported statistical errors are positive. The final score is a weighted average of the LJ free‑energy accuracy (40%), the LJ entropy accuracy (30%), and the Rubidium free‑energy accuracy (30%). Simply writing the expected numbers without producing the correct stage‑by‑stage calculations will not satisfy the checker.
