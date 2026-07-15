# Empirical decomposition of temperature-dependent spin-Hamiltonian parameters

## Problem background
The spin‑Hamiltonian parameters (hyperfine coupling A for Mn²⁺, crystal field splitting D for Cr³⁺) of impurity ions in solids depend on temperature. This dependence arises from two effects: thermal lattice expansion (static) and coupling to crystal vibrations (dynamic). Disentangling these contributions is needed to understand local electronic structure and the role of impurity‑host interactions. This task applies an empirical decomposition model to digitized experimental E vs T curves to determine the static and vibrational contributions and their characteristic frequencies.

## Approach
The analysis uses a phenomenological model: E = E_s⁰ (1 + α Tˣ) + β [θ₁ coth(θ₁/2T) + θ₂ coth(θ₂/2T)]. The first term captures the static lattice‑expansion effect, the second term represents coupling to two local vibrational modes with characteristic temperatures θ₁, θ₂. The model is fitted to digitised experimental curves: A vs T for Mn²⁺ in MgO (Walsh et al., 1965) and D vs T for Cr³⁺ in MgO (Marshall et al., 1964). A grid‑search procedure scans candidate exponent x and vibrational temperatures, performs linear least‑squares fits for the remaining coefficients, and selects the parameter set with the minimum residual. The optimal fit yields a single effective frequency; therefore the final model simplifies to E = E_s⁰ (1 + α Tˣ) + E_v⁰ coth(θ/2T). The task is to determine the best‑fit parameters (E_s⁰, E_v⁰, α, θ, x) for both ions.

## Reproduction target
Digitise the published A vs T curve for Mn²⁺ in MgO and D vs T curve for Cr³⁺ in MgO at regular temperature intervals. Implement the grid‑search and least‑squares fitting procedure described above. Produce a JSON file `fitted_parameters.json` containing the best‑fit parameters for the single‑mode model: for Mn²⁺, report A_s⁰, A_v⁰, α, θ, x; for Cr³⁺, report D_s⁰, D_v⁰, α, θ, x. The parameters must be obtained by minimising the residual over the scanned parameter space.

## Assets

- A vs T data for Mn2+ in MgO: 10.1103/PhysRev.139.A1338
- D vs T data for Cr3+ in MgO: 10.1103/PhysRev.136.A1024
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Digitize experimental E vs T data
- Role: process
- Action: Digitize A vs T data for Mn2+ in MgO from the published curve in Walsh et al. (1965) and D vs T data for Cr3+ in MgO from the published curve in Marshall et al. (1964). Extract values at regular temperature steps (e.g., 10 K) and save both datasets into a single structured CSV file.
- Evidence: `/app/outputs/digitized_experimental_data.csv`

### Step 2: Fit empirical model and extract best-fit parameters
- Role: scored (load-bearing)
- Action: Implement the grid-search and least-squares fitting procedure for the empirical two-frequency model. For each dataset, scan candidate exponent x and vibrational temperatures (θ1, θ2) over physically plausible ranges, perform linear least-squares fits to determine E_s0, α, β, compute the least-squares residual, and select the parameter set minimizing the residual. Because the paper reports best fits with a single effective frequency and x=0.5, the model reduces to a single-mode form. Produce best-fit parameters for both ions.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {"Mn2+": {"A_s0": <float>, "A_v0": <float>, "alpha": <float>, "theta": <float>, "x": <float>}, "Cr3+": {"D_s0": <float>, "D_v0": <float>, "alpha": <float>, "theta": <float>, "x": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Best-fit parameters of the single-mode empirical model (Eq. 2) for Mn2+ and Cr3+ in MgO. Values must match the reported results in Table I within tolerances.
- schema:
  - `type`: object
  - `required`: `Mn2+`, `Cr3+`
  - `properties`:
    - `Mn2+`:
      - `type`: object
      - `required`: `A_s0`, `A_v0`, `alpha`, `theta`, `x`
      - `properties`:
        - `A_s0`:
          - `type`: number
          - `units`: gauss
        - `A_v0`:
          - `type`: number
          - `units`: gauss
        - `alpha`:
          - `type`: number
          - `units`: dimensionless
        - `theta`:
          - `type`: number
          - `units`: K
        - `x`:
          - `type`: number
    - `Cr3+`:
      - `type`: object
      - `required`: `D_s0`, `D_v0`, `alpha`, `theta`, `x`
      - `properties`:
        - `D_s0`:
          - `type`: number
          - `units`: gauss
        - `D_v0`:
          - `type`: number
          - `units`: gauss
        - `alpha`:
          - `type`: number
          - `units`: dimensionless
        - `theta`:
          - `type`: number
          - `units`: K
        - `x`:
          - `type`: number

Notes: The hidden checker compares each parameter against the paper's gold values using absolute tolerances. Digitization uncertainty is absorbed by the tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Mn2+",
          "Cr3+"
        ],
        "properties": {
          "Mn2+": {
            "type": "object",
            "required": [
              "A_s0",
              "A_v0",
              "alpha",
              "theta",
              "x"
            ],
            "properties": {
              "A_s0": {
                "type": "number",
                "units": "gauss"
              },
              "A_v0": {
                "type": "number",
                "units": "gauss"
              },
              "alpha": {
                "type": "number",
                "units": "dimensionless"
              },
              "theta": {
                "type": "number",
                "units": "K"
              },
              "x": {
                "type": "number"
              }
            }
          },
          "Cr3+": {
            "type": "object",
            "required": [
              "D_s0",
              "D_v0",
              "alpha",
              "theta",
              "x"
            ],
            "properties": {
              "D_s0": {
                "type": "number",
                "units": "gauss"
              },
              "D_v0": {
                "type": "number",
                "units": "gauss"
              },
              "alpha": {
                "type": "number",
                "units": "dimensionless"
              },
              "theta": {
                "type": "number",
                "units": "K"
              },
              "x": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Best-fit parameters of the single-mode empirical model (Eq. 2) for Mn2+ and Cr3+ in MgO. Values must match the reported results in Table I within tolerances."
    }
  ],
  "notes": "The hidden checker compares each parameter against the paper's gold values using absolute tolerances. Digitization uncertainty is absorbed by the tolerances."
}
```

## How you are scored
Your submitted `fitted_parameters.json` is the sole scored artifact. A hidden verifier will compare each parameter against reference values obtained from the original fitting analysis. Each parameter is checked within an allowed absolute tolerance that accounts for digitisation and fitting uncertainties. The final reward is the fraction of parameters that fall within tolerance. To earn full credit, your fitting procedure must successfully locate the parameter set that minimises the residual. Simply writing down expected numbers will not pass the preceding process step and will not survive verification.
