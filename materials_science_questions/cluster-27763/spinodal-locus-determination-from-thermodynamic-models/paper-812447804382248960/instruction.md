# Bethe Lattice Percolation: Exact Observables and First-Order Transition

## Problem background
The droplet picture in statistical mechanics identifies clusters ("droplets") that describe phase transitions and nucleation. To unify percolation and droplet theories, a polychromatic Potts-correlated-site/random-bond percolation model was introduced. In this model, sites carry spin states from q colors, and two nearest-neighbor sites of the same color are connected only if the intervening bond is active. The bond activity probability p_b is taken as p_b = 1 − θ (the "droplet dilution"), where θ = e^{-K} is the Potts Boltzmann factor. The Bethe lattice provides an exactly solvable framework: the spin statistics (site occupation probability p_1 and the conditional nearest-neighbor probability p_11) can be computed analytically, and the percolative observables (mean number of finite clusters N, percolation probability P, mean finite-cluster size S) follow from closed-form expressions involving a self-consistent quantity Q. The central prediction is that under droplet dilution, the percolation threshold coincides with the Potts critical point, and for q > 2 the transition may become first-order in the percolation functions. This task recreates the computation for the q=3 Potts model on a Bethe lattice with coordination number 6 (σ=5) and examines the nature of the percolation transition — specifically whether P exhibits a discontinuous jump and S remains finite — as would be expected for a first-order phenomenon.

## Approach
The approach separates into two parts: (i) computing the Potts spin statistics p₁(θ) and p₁₁(θ) on the Bethe lattice, and (ii) using these as input to the percolation formulas with the droplet bond probability p_b = 1 − θ.

For the Potts part, the exact Bethe-lattice solution is used. One writes a recursion for the Cayley tree and takes the infinite‑depth limit, which yields a self-consistent equation for an effective order parameter. In the H→0⁺ limit this provides p₁ and p₁₁ as functions of θ, q, and σ. The agent must implement this solution numerically for the required parameters.

For the percolation part, the self‑consistent quantity Q is determined by the condition σ p_b p₁₁: when σ p_b p₁₁ ≤ 1 (sub‑threshold and at threshold), Q = 1; above threshold, Q is the unique root in [0,1) of Q = 1 − p_b p₁₁ + p_b p₁₁ Q^σ, obtained by standard root-finding. Using Q, p₁, p₁₁, and p_b, the percolative observables N, P, S are computed from closed‑form expressions. No external data are needed; all required formulas are well‑established and can be implemented with standard numerical libraries (numpy, scipy).

## Reproduction target
For the zero‑field q=3 Potts model on a Bethe lattice of coordination number σ+1 = 6 (σ=5) with the droplet bond probability p_b = 1 − θ, compute the percolation observables N, P, S for a dense set of θ values in [0, 1]. Produce a CSV file at `/app/outputs/percolation_functions.csv` with the following columns:
- theta (float): temperature parameter θ
- p1 (float): site occupation probability p₁
- p11 (float): conditional probability p₁₁
- p_b (float): bond probability (equal to 1 − θ)
- Q (float): self‑consistent quantity Q
- N (float): mean number of finite clusters per site
- P (float): percolation probability
- S (float): mean size of finite clusters
- threshold_flag (string): one of 'subcritical', 'critical', or 'supercritical', determined by the value of σ p_b p₁₁ relative to 1 (within numerical precision).

The file must contain at least 20 rows spanning θ ∈ [0,1] and must include points near the expected critical region so that the behavior of P and S around the transition can be assessed.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute Potts spin probabilities
- Role: process
- Action: Implement the exact Bethe-lattice Potts model solution for q=3 states and coordination number 6 (σ=5) in the zero-field H→0⁺ limit. Compute the site occupation probability p₁(θ) that a site is in spin state 1 and the conditional probability p₁₁(θ) that a nearest neighbor is in state 1 given the site is in state 1, for a fine grid of θ in [0,1].
- Evidence: `/app/outputs/potts_probs_data.npy`

### Step 2: Compute percolation observables
- Role: scored (load-bearing)
- Action: Using the probabilities from Step 1 and the droplet bond probability p_b = 1 - θ, determine Q: Q = 1 below and at threshold; above threshold solve Q = 1 - p_b p_11 + p_b p_11 Q^σ for the unique root in [0,1). Then compute the percolative observables N, P, S from the paper's formulas. Save the results as a CSV with columns: theta, p1, p11, p_b, Q, N, P, S, and a threshold flag ('subcritical' / 'critical' / 'supercritical').
- Output file: `/app/outputs/percolation_functions.csv`
- Format: csv
- Contract: Columns: theta (float), p1 (float), p11 (float), p_b (float), Q (float), N (float), P (float), S (float), threshold_flag (string: 'subcritical'/'critical'/'supercritical')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/percolation_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### percolation_functions.csv
- path: `/app/outputs/percolation_functions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing the computed percolation observables (N, P, S) for the q=3, σ=5, p_b=1-θ system. The checker recomputes N, P, S from the provided probabilities and Q to verify internal consistency, checks the percolation threshold condition, and compares P at the critical and other temperatures to hidden reference values to confirm the first-order jump.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `p1`, `p11`, `p_b`, `Q`, `N`, `P`, `S`, `threshold_flag`

Notes: The file covers at least 20 values of θ in [0,1]. The agent must implement the Bethe-lattice Potts solution and the root-finding for Q; no pre-made tables are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "percolation_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "p1",
          "p11",
          "p_b",
          "Q",
          "N",
          "P",
          "S",
          "threshold_flag"
        ]
      },
      "description": "CSV file containing the computed percolation observables (N, P, S) for the q=3, σ=5, p_b=1-θ system. The checker recomputes N, P, S from the provided probabilities and Q to verify internal consistency, checks the percolation threshold condition, and compares P at the critical and other temperatures to hidden reference values to confirm the first-order jump."
    }
  ],
  "notes": "The file covers at least 20 values of θ in [0,1]. The agent must implement the Bethe-lattice Potts solution and the root-finding for Q; no pre-made tables are provided."
}
```

## How you are scored
A hidden verifier reads your CSV and independently recomputes the percolation observables N, P, S from the supplied p1, p11, p_b, and Q using the percolation formulas to verify internal consistency within a tight floating‑point tolerance. It checks the percolation threshold condition σ p_b p₁₁ = 1 at the row marked 'critical' and verifies that the percolation probability P undergoes a jump (approximately zero in the subcritical region, finite in the supercritical region) and that the mean cluster size S remains finite at the transition. The verifier also compares your computed P values at selected temperatures against hidden reference values derived from the exact Bethe‑lattice solution. The final score is a weighted combination of these checks; your CSV must be correctly formatted and contain all required columns. Merely reporting numbers from the literature is not sufficient — the verifier recomputes from your raw data and compares against hidden gold standards.
