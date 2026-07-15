# Ising impurity spin ratio and distortion

## Problem background
Hyperfine field techniques are widely used to measure critical exponents in magnetic systems, but the probe nucleus itself acts as an impurity in the host lattice. Whether this probe significantly disturbs the measurement of the bulk critical exponent β is an open physical question. This task models the host as a spin-½ Ising ferromagnet on a simple cubic lattice and introduces a single non-magnetic impurity at one site. The quantity of interest is the ratio ⟨σ₁⟩/σ: the average spin on a nearest-neighbour host site to the impurity relative to the bulk magnetisation σ, evaluated as a function of reduced temperature τ = 1 − T/Tc along the coexistence curve. Computing this ratio and the associated probe-induced distortion Δβ/β over a range of τ allows a quantitative assessment of probe disturbance effects.

## Approach
The calculation uses an exact expression that relates the impurity-neighbour spin ⟨σ₁⟩ to a set of perfect‑lattice correlation functions: the bulk magnetisation σ, the two‑point functions Γ₁₀₀ (nearest‑neighbour), Γ₁₁₀, Γ₂₀₀, and two higher‑point functions. The higher‑point functions are approximated as simple fractions of lower‑order ones. The expression’s coefficients are temperature‑dependent constants that vary slowly near Tc; their critical‑point values are taken from the literature.

To evaluate the ratio across the full temperature range, Padé approximants are constructed for σ, Γ₁₀₀, Γ₁₁₀, and Γ₂₀₀. The procedure uses known low‑temperature series expansions for these functions (extracted from published sources) together with accepted critical exponents, critical amplitudes, and the critical coupling uc. The singular critical behaviour is subtracted, near‑diagonal Padé approximants are formed to match the remaining series coefficients, and the correct critical values are restored. The resulting analytic forms can be evaluated for any τ in [0,1].

With the correlation functions in hand, ⟨σ₁⟩ is computed from the exact formula, and the ratio R = ⟨σ₁⟩ / σ is formed. The probe‑induced distortion Δβ/β is defined as −(log R₂ − log R₁)/(log τ₂ − log τ₁) and is evaluated over three specified τ intervals. A CSV file records τ, the perfect‑lattice functions, the ratio, and the distortion.

## Reproduction target
For a simple cubic spin‑½ Ising model with a single non‑magnetic impurity, compute the ratio ⟨σ₁⟩/σ for reduced temperatures τ ranging from 10⁻⁵ to 1 (along the coexistence curve, H→0⁺). Compute the probe‑induced distortion Δβ/β for the three intervals:

- [10⁻⁴, 10⁻³]
- [10⁻³, 10⁻²]
- [10⁻², 10⁻¹]

Write a CSV file containing columns:
- tau (float): reduced temperature τ
- sigma (float): bulk magnetisation σ(τ)
- Gamma100 (float): nearest-neighbour correlation Γ₁₀₀(τ)
- Gamma110 (float): correlation Γ₁₁₀(τ)
- Gamma200 (float): correlation Γ₂₀₀(τ)
- ratio (float): the ratio ⟨σ₁⟩/σ at τ
- dbeta_beta (float or empty): the distortion Δβ/β for the interval that contains τ (e.g., at the interval centre), empty for other rows.

## Assets

- Domb 1974 – Phase Transitions and Critical Phenomena, Vol. 4
- Tarko & Fisher 1975 – Phys. Rev. B 11 1217: https://doi.org/10.1103/PhysRevB.11.1217

## Workflow steps

### Step 1: Obtain low-temperature series expansion coefficients
- Role: process
- Action: Retrieve the low-temperature series expansions for the bulk magnetisation σ and the two-point correlation functions Γ₁₀₀ (nearest-neighbour), Γ₁₁₀, and Γ₂₀₀ from the references Domb (1974) and Tarko & Fisher (1975). Extract the expansion coefficients up to the required orders: σ to u²⁰, Γ₁₀₀ to u¹⁷, Γ₁₁₀ and Γ₂₀₀ to u¹².
- Evidence: none

### Step 2: Build Padé approximants for perfect-lattice correlation functions
- Role: process
- Action: Implement the Padé approximant construction method from the paper (subtract critical singular behaviour, build near-diagonal approximants, enforce critical values). Use the collected series coefficients and the following parameters: critical exponents β=0.325, α′=0.11, critical coupling u_c=0.411985, critical values Γ₁₀₀ᶜ=0.332, Γ₁₁₀ᶜ=0.208, Γ₂₀₀ᶜ=0.162, and amplitudes E⁻ as given in the paper. Form approximants for σ(T) (order [10/10]), Γ₁₀₀(T) ([8/9]), Γ₁₁₀(T) ([5/7]), Γ₂₀₀(T) ([5/7]), and approximate Γ₁₂₃₄₅₆ = 0.5 Γ₁₀₀ and Γ_c₁₂₃₄₅₆ = 0.5 σ. Produce a set of temperature-dependent functions that can be evaluated for 0 ≤ T ≤ Tc.
- Evidence: none

### Step 3: Compute ratio ⟨σ₁⟩/σ and distortion Δβ/β
- Role: scored (load-bearing)
- Action: For reduced temperatures τ ranging from 1e-5 to 1, evaluate σ(τ), Γ₁₀₀(τ), Γ₁₁₀(τ), Γ₂₀₀(τ) from the Padé approximants. Compute the ratio R = ⟨σ₁⟩/σ using the exact expression: ⟨σ₁⟩ = (A₁σ + A₂ Γ_c123456) / (B₁ + B₂ Γ_c1 + B₃ Γ_12 + B₄ Γ_14 + B₅ Γ_123456) with A₁=0.63549, A₂=0.00150, B₁=1.03397, B₂=−0.81664, B₃=0.13626, B₄=0.03406, B₅=−0.00009, Γ_c1=Γ₁₀₀, Γ_12=Γ₁₁₀, Γ_14=Γ₂₀₀, and the higher-point approximations given above. For the three τ intervals [1e-4,1e-3], [1e-3,1e-2], [1e-2,1e-1], calculate Δβ/β = −(log R₂ − log R₁)/(log τ₂ − log τ₁) using the endpoints of each interval and report the resulting value. Write a CSV file with columns: tau, sigma, Gamma100, Gamma110, Gamma200, ratio, dbeta_beta.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: tau (float), sigma (float), Gamma100 (float), Gamma110 (float), Gamma200 (float), ratio (float), dbeta_beta (float or empty)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The ratio ⟨σ₁⟩/σ as a function of reduced temperature and the probe-induced distortion Δβ/β over the three τ intervals. The checker compares the ratio at τ=0 and the distortion values to hidden reference values derived from the paper, within absolute tolerances.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `sigma`, `Gamma100`, `Gamma110`, `Gamma200`, `ratio`, `dbeta_beta`

Notes: The hidden verifier uses reference values derived from the paper; the exact reference values are not disclosed in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "sigma",
          "Gamma100",
          "Gamma110",
          "Gamma200",
          "ratio",
          "dbeta_beta"
        ]
      },
      "description": "The ratio ⟨σ₁⟩/σ as a function of reduced temperature and the probe-induced distortion Δβ/β over the three τ intervals. The checker compares the ratio at τ=0 and the distortion values to hidden reference values derived from the paper, within absolute tolerances."
    }
  ],
  "notes": "The hidden verifier uses reference values derived from the paper; the exact reference values are not disclosed in the public contract."
}
```

## How you are scored
A hidden verifier independently inspects the submitted artifacts. It reads the CSV file, checks that the required columns exist, and compares the computed ratio and distortion values to hidden reference values. Reward is awarded based on how close the computed numbers are to the references; reporting the paper’s numbers without executing the prescribed workflow is not sufficient. The verifier may also audit the internal consistency of the correlation functions. The final score is a weighted combination of all scored stages.
