# Symbolic expressions for mutual information and correlation partitions in an Ising-like dipolar spin system

## Problem background
In solid-state NMR, dipolar-coupled quantum spin systems exhibit a free induction decay (FID) whose shape coincides for classical and quantum systems when each spin has many equivalent neighbours. This task investigates the underlying correlations by focusing on a pair of spins in a lattice governed by an Ising-like (zz-only) secular dipolar Hamiltonian at high temperature. The aim is to derive exact analytic expressions for the mutual information and its decomposition into classical and quantum contributions, thereby quantifying the share of quantum correlations in such a system.

## Approach
The derivation follows a stepwise reduction: starting from the high-temperature equilibrium density matrix after a resonant π/2 pulse, the time evolution under the zz-only Hamiltonian H_d = Σ b_ij S_{zi} S_{zj} (flip-flop terms neglected) is computed exactly to first order in the inverse temperature β. Tracing out all but a chosen spin pair yields the two-spin reduced density matrix, expressed in terms of lattice embedding factors G_ij(t). The mutual information is obtained by expanding the von Neumann entropy to order β². For spin‑1/2, classical and quantum correlations are separated using von Neumann orthogonal measurement projectors. For general spin S, the analogue of classical correlations is extracted via a positive‑operator‑valued measure (POVM) using spin coherent states, leaving a quantum discord‑like remainder. Finally, a small‑time expansion reveals the asymptotic fraction of quantum correlations in the limit of many equivalent neighbours.

## Reproduction target
Produce a single JSON file derivation_output.json containing the sympy‑parseable strings for the following quantities, all expressed in terms of the symbols beta (β), G (G_ij(t)), b (b_ij), t, S, and d = 2S+1:
- mutual_information: I_ij
- classical_correlation_S_half: C_ij (S = 1/2)
- quantum_correlation_S_half: D_ij (S = 1/2)
- classical_correlation_S_general: J_ij (S ≥ 1/2)
- quantum_correlation_S_general: Q_ij (S ≥ 1/2)
- quantum_fraction: simplified expression for Q_ij / I_ij in the asymptotic regime (|b t| ≪ 1).

## Assets

- sympy: sympy
- numpy: numpy

## Workflow steps

### Step 1: Derive time-evolved multi-spin density matrix
- Role: process
- Action: Define the high-temperature equilibrium density matrix (polarization β = ħω₀/kT ≪ 1) and the initial state after a resonant π/2 pulse about the y-axis: ρ(0) = (1 + β Ŝₓ)/Z. Using the Ising-like (zz-only) secular dipolar Hamiltonian H_d = Σ_i≠j b_ij Ŝ_{zi} Ŝ_{zj} (flip-flop terms a_ij=0), derive the exact time-evolved many-spin density matrix ρ(t) = exp(-i H_d t/ħ) ρ(0) exp(i H_d t/ħ) to first order in β. Obtain the explicit many-spin expression and the free-induction-decay factor F_zz(t).
- Evidence: none

### Step 2: Reduce to two-spin reduced density matrix
- Role: process
- Action: Perform a partial trace over all lattice spins except a chosen pair at sites i, j on the full density matrix from step 01. Obtain the exact two-spin reduced density matrix ρ_{ij}(t). Define the lattice embedding factor G_{ij}(t) and the local factor g_{ij}(t). Assume the two sites are equivalent so that G_{i(j)}(t)=G_{j(i)}(t)=G_{ij}(t). The result will be of the form ρ_{ij}(t) = (1 + β Δρ_{ij}(t)) / d².
- Evidence: none

### Step 3: Compute correlation formulas and output the final expressions
- Role: scored (load-bearing)
- Action: From the two-spin density matrix ρ_{ij}(t), expand the von Neumann entropy to order β² and derive the mutual information I_{ij}. For S=1/2, apply von Neumann orthogonal measurement projectors to split I_{ij} into classical correlation C_{ij} and quantum discord D_{ij}. For general spin S≥1/2, use the POVM measurement basis of spin coherent states to obtain the classical part J_{ij} and quantum part Q_{ij}. Simplify the expressions, and expand for small time (|b_{ij}t|≪1) to extract the asymptotic quantum fraction Q_{ij}/I_{ij}. Collect all final symbolic expressions into a JSON file with the keys: mutual_information, classical_correlation_S_half, quantum_correlation_S_half, classical_correlation_S_general, quantum_correlation_S_general, quantum_fraction. Each value must be a string parseable by sympy using the symbols beta (β), G (G_{ij}(t)), b (b_{ij}), t, S, and d=2*S+1. Use sympy to derive and simplify the expressions; do not merely hardcode the answer.
- Output file: `/app/outputs/derivation_output.json`
- Format: json
- Contract: Object with required keys: mutual_information (string), classical_correlation_S_half (string), quantum_correlation_S_half (string), classical_correlation_S_general (string), quantum_correlation_S_general (string), quantum_fraction (string). Each value is a sympy-parseable expression string involving the symbols beta, G, b, t, S, and d=2*S+1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/derivation_output.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### derivation_output.json
- path: `/app/outputs/derivation_output.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON file containing the sympy-parseable symbolic expressions for mutual information, classical and quantum correlations (for S=1/2 and general S), and the asymptotic quantum fraction.
- schema:
  - `type`: object
  - `properties`:
    - `mutual_information`:
      - `type`: string
    - `classical_correlation_S_half`:
      - `type`: string
    - `quantum_correlation_S_half`:
      - `type`: string
    - `classical_correlation_S_general`:
      - `type`: string
    - `quantum_correlation_S_general`:
      - `type`: string
    - `quantum_fraction`:
      - `type`: string
  - `required`: `mutual_information`, `classical_correlation_S_half`, `quantum_correlation_S_half`, `classical_correlation_S_general`, `quantum_correlation_S_general`, `quantum_fraction`
  - `additionalProperties`: False

Notes: All expressions are strings that can be parsed by sympy using symbols beta, G, b, t, S, and d=2*S+1.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "derivation_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "mutual_information": {
            "type": "string"
          },
          "classical_correlation_S_half": {
            "type": "string"
          },
          "quantum_correlation_S_half": {
            "type": "string"
          },
          "classical_correlation_S_general": {
            "type": "string"
          },
          "quantum_correlation_S_general": {
            "type": "string"
          },
          "quantum_fraction": {
            "type": "string"
          }
        },
        "required": [
          "mutual_information",
          "classical_correlation_S_half",
          "quantum_correlation_S_half",
          "classical_correlation_S_general",
          "quantum_correlation_S_general",
          "quantum_fraction"
        ],
        "additionalProperties": false
      },
      "description": "JSON file containing the sympy-parseable symbolic expressions for mutual information, classical and quantum correlations (for S=1/2 and general S), and the asymptotic quantum fraction."
    }
  ],
  "notes": "All expressions are strings that can be parsed by sympy using symbols beta, G, b, t, S, and d=2*S+1."
}
```

## How you are scored
A hidden verifier reads your derivation_output.json, parses each expression string into a sympy expression and compares it symbolically against the correct analytic formula. For each quantity, it simplifies the difference between the reference expression and yours. If a difference simplifies to zero, that quantity is correct. The final reward is a weighted sum over all scored entries: full credit requires all expressions to be symbolically equivalent; partial credit is awarded proportionally to the number of matching expressions. The verifier does not inspect intermediate derivation steps; only the final expressions are evaluated.
