# Magnetic Phase Diagram of Double Exchange Model on Triangular Lattice

## Problem background
The double-exchange model describes itinerant electrons that interact with localized classical spins through a Hund coupling, along with antiferromagnetic superexchange between spins. On a two-dimensional triangular lattice, geometric frustration competes with the tendency of electrons to align spins, leading to a variety of possible magnetic orderings. Understanding the low-temperature magnetic phase diagram of this model for different electron fillings and superexchange strengths is important for explaining the properties of layered manganites and related strongly correlated materials. This task computes the spin structure factor and spin‑spin correlations from Monte Carlo simulations to characterize the stable magnetic phases.

## Approach
We use the truncated polynomial expansion method (TPEM) combined with Monte Carlo simulation. The procedure consists of (1) precomputing Chebyshev expansion coefficients for the effective action and electron density at given chemical potentials and inverse temperature, (2) implementing the double-exchange Hamiltonian on a 6×6 triangular lattice with periodic boundary conditions, (3) performing Metropolis spin-flip updates where the change in effective action is evaluated via recursive Chebyshev moments and truncated matrix-vector products, and (4) accumulating spin‑spin correlations during the simulation. After equilibration, the spin structure factor S(q) is computed from the correlation data for each parameter set, and the peak positions and magnitudes are identified.

## Reproduction target
Perform TPEM Monte Carlo simulations for the double-exchange model with the following fixed parameters: inverse temperature β=75, Hund coupling J_H=8, hopping t=1, Chebyshev cutoff M=30, and truncation thresholds ε_p=10^{-5}, ε_tr=10^{-3}. Run simulations for four distinct conditions: (i) half‑filling (chemical potential μ=−6) with superexchange J_AF=0, (ii) half‑filling with J_AF=0.1, (iii) quarter‑filling (μ=−8) with J_AF=0, and (iv) quarter‑filling with J_AF=0.1. For each condition, compute the spin‑spin correlation ⟨S_1·S_j⟩ for all sites j on the 6×6 lattice and the spin structure factor S(q) over the first Brillouin zone. Output the full correlation array, the S(q) map, and the list of peak positions and magnitudes into four JSON files. The goal is to produce accurate results that can be compared against reference values for the peak locations and nearest-neighbor correlation.

## Assets
No external datasets or pre-trained models are required. A Python 3 environment with standard numerical libraries (numpy, scipy) is sufficient; all simulation code is implemented within the workflow. The TPEM algorithm is described in the literature and must be coded from scratch.

## Workflow steps

### Step 1: Precompute Chebyshev expansion coefficients
- Role: process
- Action: Compute the Chebyshev expansion coefficients f_m for the effective action S(x) = -ln[1+exp(beta*(x-mu))] and electron occupation n(x)=1/(1+exp(beta*(x-mu))) for chemical potentials mu=-6 and mu=-8 at inverse temperature beta=75, up to polynomial cutoff M=30.
- Evidence: none

### Step 2: Implement TPEM core and Hamiltonian
- Role: process
- Action: Implement the double-exchange Hamiltonian H = -t sum_{<ij>,alpha} c^+_{i,alpha}c_{j,alpha} + h.c. - J_H sum_{i,alpha,beta} c^+_{i,alpha} sigma_{alpha,beta} c_{i,beta} . S_i + J_AF sum_{<ij>} S_i . S_j on a 6x6 triangular lattice with periodic boundary conditions. Implement the recursive Chebyshev moment calculation, truncated matrix-vector products, and the effective action update for spin-flip trials using thresholds epsilon_p=10^{-5} and epsilon_tr=10^{-3} (TPEM).
- Evidence: none

### Step 3: Run Monte Carlo simulations for four parameter sets
- Role: process
- Action: Using the precomputed coefficients and TPEM engine, perform Monte Carlo simulations for each of the four parameter sets: (mu=-6, J_AF=0), (mu=-6, J_AF=0.1), (mu=-8, J_AF=0), (mu=-8, J_AF=0.1) on a 6x6 triangular lattice with beta=75, J_H=8, t=1, M=30, epsilon_p=10^{-5}, epsilon_tr=10^{-3}. Run 10000 MC steps with 2000 warmup, measuring every 20 steps. Save the resulting spin-spin correlations as evidence files: correlations_half_JAF0.npy, correlations_half_JAF01.npy, correlations_quarter_JAF0.npy, correlations_quarter_JAF01.npy.
- Evidence: `/app/outputs/correlations_half_JAF0.npy, correlations_half_JAF01.npy, correlations_quarter_JAF0.npy, correlations_quarter_JAF01.npy`

### Step 4: Compute S(q) for half-filling J_AF=0
- Role: scored (load-bearing)
- Action: From the spin-spin correlation file correlations_half_JAF0.npy, compute the spin structure factor S(q) for all q in the first Brillouin zone, extract peak positions and values, and write the results to the output JSON file.
- Output file: `/app/outputs/results_half_filling_JAF0.json`
- Format: json
- Contract: JSON object with fields: lattice_size (list of ints), parameters (object with mu, J_AF, beta, JH, M, epsilon_p, epsilon_tr), spin_spin_correlations (list of floats, length N), structure_factor (object with keys 'q1_q2' and S(q) float values), peak_positions (list of [q1,q2] arrays).
- Scoring: scored by hidden verifier

### Step 5: Compute S(q) for half-filling J_AF=0.1
- Role: scored (load-bearing)
- Action: From the spin-spin correlation file correlations_half_JAF01.npy, compute S(q), extract peaks, and write to the output JSON file.
- Output file: `/app/outputs/results_half_filling_JAF01.json`
- Format: json
- Contract: JSON object with fields: lattice_size, parameters, spin_spin_correlations, structure_factor, peak_positions.
- Scoring: scored by hidden verifier

### Step 6: Compute S(q) for quarter-filling J_AF=0
- Role: scored (load-bearing)
- Action: From the spin-spin correlation file correlations_quarter_JAF0.npy, compute S(q), extract peaks, and write to the output JSON file.
- Output file: `/app/outputs/results_quarter_filling_JAF0.json`
- Format: json
- Contract: JSON object with fields: lattice_size, parameters, spin_spin_correlations, structure_factor, peak_positions.
- Scoring: scored by hidden verifier

### Step 7: Compute S(q) for quarter-filling J_AF=0.1
- Role: scored (load-bearing)
- Action: From the spin-spin correlation file correlations_quarter_JAF01.npy, compute S(q), extract peaks, and write to the output JSON file.
- Output file: `/app/outputs/results_quarter_filling_JAF01.json`
- Format: json
- Contract: JSON object with fields: lattice_size, parameters, spin_spin_correlations, structure_factor, peak_positions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_half_filling_JAF0.json`
- `/app/outputs/results_half_filling_JAF01.json`
- `/app/outputs/results_quarter_filling_JAF0.json`
- `/app/outputs/results_quarter_filling_JAF01.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_half_filling_JAF0.json
- path: `/app/outputs/results_half_filling_JAF0.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin structure factor results for half-filling (mu=-6) without AF superexchange.
- schema:
  - `type`: object
  - `required`:
    - `lattice_size`: list of ints
    - `parameters`: object
    - `spin_spin_correlations`: list of floats
    - `structure_factor`: object
    - `peak_positions`: list of arrays
  - `items`: object
  - `units`: object

### results_half_filling_JAF01.json
- path: `/app/outputs/results_half_filling_JAF01.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin structure factor results for half-filling with J_AF=0.1.
- schema:
  - `type`: object
  - `required`:
    - `lattice_size`: list of ints
    - `parameters`: object
    - `spin_spin_correlations`: list of floats
    - `structure_factor`: object
    - `peak_positions`: list of arrays
  - `items`: object
  - `units`: object

### results_quarter_filling_JAF0.json
- path: `/app/outputs/results_quarter_filling_JAF0.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin structure factor results for quarter-filling (mu=-8) without AF superexchange.
- schema:
  - `type`: object
  - `required`:
    - `lattice_size`: list of ints
    - `parameters`: object
    - `spin_spin_correlations`: list of floats
    - `structure_factor`: object
    - `peak_positions`: list of arrays
  - `items`: object
  - `units`: object

### results_quarter_filling_JAF01.json
- path: `/app/outputs/results_quarter_filling_JAF01.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin structure factor results for quarter-filling with J_AF=0.1.
- schema:
  - `type`: object
  - `required`:
    - `lattice_size`: list of ints
    - `parameters`: object
    - `spin_spin_correlations`: list of floats
    - `structure_factor`: object
    - `peak_positions`: list of arrays
  - `items`: object
  - `units`: object

Notes: The hidden checker will verify that the reported spin structure factor peak positions and magnitudes match expected reference values within tolerances. No gold values or tolerances are provided to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_half_filling_JAF0.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_size": "list of ints",
          "parameters": "object",
          "spin_spin_correlations": "list of floats",
          "structure_factor": "object",
          "peak_positions": "list of arrays"
        },
        "items": {},
        "units": {}
      },
      "description": "Spin structure factor results for half-filling (mu=-6) without AF superexchange."
    },
    {
      "file": "results_half_filling_JAF01.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_size": "list of ints",
          "parameters": "object",
          "spin_spin_correlations": "list of floats",
          "structure_factor": "object",
          "peak_positions": "list of arrays"
        },
        "items": {},
        "units": {}
      },
      "description": "Spin structure factor results for half-filling with J_AF=0.1."
    },
    {
      "file": "results_quarter_filling_JAF0.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_size": "list of ints",
          "parameters": "object",
          "spin_spin_correlations": "list of floats",
          "structure_factor": "object",
          "peak_positions": "list of arrays"
        },
        "items": {},
        "units": {}
      },
      "description": "Spin structure factor results for quarter-filling (mu=-8) without AF superexchange."
    },
    {
      "file": "results_quarter_filling_JAF01.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_size": "list of ints",
          "parameters": "object",
          "spin_spin_correlations": "list of floats",
          "structure_factor": "object",
          "peak_positions": "list of arrays"
        },
        "items": {},
        "units": {}
      },
      "description": "Spin structure factor results for quarter-filling with J_AF=0.1."
    }
  ],
  "notes": "The hidden checker will verify that the reported spin structure factor peak positions and magnitudes match expected reference values within tolerances. No gold values or tolerances are provided to the agent."
}
```

## How you are scored
A hidden verifier will examine the four output JSON files. For each case, it will compare the reported peak positions and magnitudes of S(q) against expected reference values, and it will check the value of the spin‑spin correlation between nearest neighbors. Tolerance windows are applied but are not disclosed to you. The final reward is a weighted combination of the scores for the four parameter sets; each contributes equally. Reporting plausible numbers that merely look correct is not enough — they must match the reference data within the hidden tolerances.
