# Adsorption Phase Sequence on M=3 Square Terraces via Transfer Matrix

## Problem background
The study addresses adsorption of gas particles onto a surface consisting of long, finite-width square terraces where adjacent edge-sites are second‑neighbors. The adsorbate‑adsorbate interactions are limited to first‑ (V) and second‑neighbor (W) lateral energies, and the binding energy at edge‑sites differs from that in the bulk by an edge‑interaction energy U. At low temperature, as the chemical potential μ is varied, the system can adopt a sequence of ordered or partially ordered adsorbate phases, each characterized by a distinct set of occupational numbers: coverage θ₀, first‑neighbor pairs per site θ, second‑neighbor pairs per site β, and edge occupancy per site γ. Transitions between phases occur at specific μ where the entropy peaks. The goal is to determine the phase sequence and the transition chemical potentials, coverages, and entropies for a width‑M=3 terrace for a given set of interaction parameters, using a transfer‑matrix formalism.

## Approach
The transfer‑matrix method constructs an 8×8 matrix T₁³ for a terrace of width M=3 from the Boltzmann activities x=exp(μ/kT), y=exp(V/kT), z=exp(W/kT), u=exp(U/kT). The entries are products of powers of these activities; u‑factors appear on even‑numbered columns and an additional u‑factor is applied to even‑numbered columns in the lower half of the matrix. The leading (largest real positive) eigenvalue R₁ₑ of this matrix yields the partition function in the thermodynamic limit. The occupational characteristics are obtained as logarithmic derivatives: θ₀ = (x/(M R₁ₑ)) ∂R₁ₑ/∂x, and similarly for θ, β, γ. The energy per site E_site is built from these characteristics and the interaction energies, and the entropy per site is S_ent = (1/M) ln R₁ₑ – E_site/(k_B T). By sweeping μ over a range and monitoring S_ent and the occupational set, one identifies phases as intervals where these quantities are constant (entropy plateaus) and transitions as local entropy maxima. The ordered phase names and the corresponding transition μ, coverage θ₀, and entropy S_ent are recorded. The computation uses standard numerical linear algebra (eigenvalue solver) and finite‑difference differentiation.

## Reproduction target
Implement the procedure described in the Approach for a terrace of width M=3. Use the following fixed model parameters: V = −1, W = −1.5, U = 0.3, and temperature T = 1 (k_B = 1). Sweep the chemical potential μ over a sufficiently broad range (e.g., from negative to positive values) to encounter the full sequence from empty (E) to full coverage (F). Produce two output files under /app/outputs: (1) phase_sequence.txt containing the ordered phase names (e.g., "E -> S3 -> S4 -> \bar{S}_3 -> F") and (2) transitions.csv with columns transition_name, mu, coverage, entropy for each observed phase transition. The required computation is self‑contained; no external dataset is needed.

## Assets

- Python: https://python.org
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Boltzmann activities
- Role: process
- Action: Given fixed interaction energies V, W, U, temperature T (k_B=1), and a range of shifted chemical potentials μ, compute the absolute activities x = exp(μ/T), y = exp(V/T), z = exp(W/T), u = exp(U/T). Keep y, z, u constant while sweeping x values corresponding to each μ.
- Evidence: none

### Step 2: Build transfer matrix for M=3
- Role: process
- Action: For each set of activities (x, y, z, u), construct the 8×8 transfer matrix T_3^1 using the explicit form given in the model description. The matrix entries are products of powers of x, y, z, u, with u-factors on even-numbered columns and an additional u-factor on even-numbered columns in the second half of the matrix.
- Evidence: none

### Step 3: Compute leading eigenvalue and partial derivatives
- Role: process
- Action: For each transfer matrix, compute all eigenvalues and identify the largest real positive eigenvalue R_le. Estimate the partial derivatives ∂R_le/∂x, ∂R_le/∂y, ∂R_le/∂z, ∂R_le/∂u using central finite differences (e.g., perturb each activity by a small amount).
- Evidence: none

### Step 4: Calculate occupational characteristics and entropy
- Role: process
- Action: Compute coverage θ0, first-neighbor pairs per site θ, second-neighbor pairs per site β, and edge occupancy per site γ using the logarithmic derivative formulas: θ0=(x/(M R_le))∂R_le/∂x, etc. Compute energy per site E_site from the occupational characteristics and input energies, and entropy per site S_ent = (1/M) ln R_le - E_site/(k_B T). Store these quantities for each μ.
- Evidence: none

### Step 5: Identify phases and transitions
- Role: process
- Action: Scan the entropy S_ent vs μ curve. Identify phases as intervals where the occupational set {θ0, θ, β, γ} is constant (entropy plateaus). Locate phase transitions at local maxima of entropy. Determine the ordered list of phase names (E, S1, S2, ..., F) and for each transition record the chemical potential μ, coverage θ0, and entropy S_ent at the peak. Verify the energy-balance condition as a consistency check.
- Evidence: none

### Step 6: Write phase sequence
- Role: scored (load-bearing)
- Action: Write the ordered sequence of phases separated by ' -> ' to phase_sequence.txt.
- Output file: `/app/outputs/phase_sequence.txt`
- Format: txt
- Contract: Single line, e.g., "E -> S3 -> S4 -> \bar{S}_3 -> F".
- Scoring: scored by hidden verifier

### Step 7: Write transition data
- Role: scored (load-bearing)
- Action: Write a CSV file with columns transition_name, mu, coverage, entropy, one row per observed transition.
- Output file: `/app/outputs/transitions.csv`
- Format: csv
- Contract: CSV with columns: transition_name (string), mu (float), coverage (float), entropy (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_sequence.txt`
- `/app/outputs/transitions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_sequence.txt
- path: `/app/outputs/phase_sequence.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Ordered sequence of adsorption phases encountered as chemical potential increases for a given parameter set.
- schema:
  - `type`: text
  - `description`: A single line with phase names separated by ' -> '.

### transitions.csv
- path: `/app/outputs/transitions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Transition data: name, chemical potential, coverage, entropy for each phase transition.
- schema:
  - `type`: table
  - `required_columns`: `transition_name`, `mu`, `coverage`, `entropy`
  - `units`:
    - `mu`: in units of k_B T
    - `coverage`: fraction of sites occupied
    - `entropy`: per site divided by k_B

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_sequence.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line with phase names separated by ' -> '."
      },
      "description": "Ordered sequence of adsorption phases encountered as chemical potential increases for a given parameter set."
    },
    {
      "file": "transitions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "transition_name",
          "mu",
          "coverage",
          "entropy"
        ],
        "units": {
          "mu": "in units of k_B T",
          "coverage": "fraction of sites occupied",
          "entropy": "per site divided by k_B"
        }
      },
      "description": "Transition data: name, chemical potential, coverage, entropy for each phase transition."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks both output files. For phase_sequence.txt it checks that the sequence of phase names, the number of phases, and the transition ordering agree with the correct physical outcome for the given parameters. For transitions.csv it compares each reported μ, coverage, and entropy against a set of hidden reference values obtained from the exact theoretical computation for these parameters. Tolerances are chosen to accommodate slight numerical differences inevitably arising from finite‑difference derivatives and eigenvalue calculations, while still penalising incorrect results. The final reward, a number between 0 and 1, is a weighted combination of the phase‑sequence correctness and the accuracy of the transition data. Simply guessing numbers or copying a reported value without executing the full transfer‑matrix computation and μ‑sweep will not match the hidden checker’s expectations and will receive a low score.
