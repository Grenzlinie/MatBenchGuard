# Compute Incommensurate Susceptibility Peaks for Mixed Quasiperiodic Ising Models

## Problem background
Quasiperiodic Ising models on regular square lattices exhibit wavevector-dependent susceptibility χ(q) that reveals whether the magnetic peaks are commensurate or incommensurate with the lattice. In a purely ferromagnetic case the peaks remain at the usual positions, but when the interactions mix ferromagnetic and antiferromagnetic bonds, the susceptibility may develop incommensurate peaks whose positions depend on the chosen aperiodic sequence of couplings. This task focuses on the mixed-case model for two aperiodic sequences: the golden-ratio sequence and the silver-mean sequence. The goal is to compute the principal peak position of the longitudinal susceptibility along the q_x axis at a temperature above the critical point.

## Approach
The starting point is the uniform, symmetric square-lattice Ising model at a fixed temperature (with an elliptic-modulus parameter that gives a correlation length ≈ 16). First, we compute the connected spin–spin correlation function C₀(l, m) for all needed separations using a standard numerical method (e.g. transfer‑matrix diagonalisation or exact determinants). For each aperiodic sequence (j = 0 for golden ratio, j = 1 for silver mean), we define a quasiperiodic gauge function φ^{(j)}(m) that depends on the fractional parts of m/αⱼ (αⱼ = (1+√5)/2 for j=0, αⱼ = 1+√2 for j=1). The mixed-model pair correlation is then obtained by modulating the uniform correlation: C(l, m) = φ(l+m)·φ(l−m)·C₀(l, m). Finally, the susceptibility χ(q, 0) is computed by summing the modulated correlation over the lattice (or, equivalently, by a convolution with the uniform susceptibility). The location of the highest peak (the principal peak) in χ(q, 0) is then extracted for each j. The task therefore requires implementing a reliable method to evaluate the uniform Ising correlations, constructing the quasiperiodic factor, performing the double sum or convolution, and locating the maximum of the resulting curve.

## Reproduction target
Produce a JSON file `/app/outputs/peak_positions.json` that contains the principal peak positions of χ(q, 0) for the mixed quasiperiodic Ising model at the temperature defined by k = 0.915398728… (correlation length ≈ 16). The file must have the structure `{"q_j0": <float>, "q_j1": <float>}`, where `q_j0` is the peak location for the golden-ratio sequence (j=0) and `q_j1` is the peak location for the silver-mean sequence (j=1), both in radians and measured along the q_x axis (q_y = 0).

## Assets

- Python scientific computing stack: numpy, scipy, mpmath

## Workflow steps

### Step 1: Compute uniform Ising spin correlations
- Role: process
- Action: For the square-lattice Ising model at temperature k=0.915398728… (correlation length ξ≈16), compute the connected spin correlation function C0(l,m) for all needed separations. Use a standard numerical method (e.g., transfer matrix diagonalization or finite-lattice summation). Store the results in a NumPy archive for later use.
- Evidence: `/app/outputs/uniform_c0.npz`

### Step 2: Compute principal peak positions for mixed quasiperiodic models
- Role: scored (load-bearing)
- Action: For j=0 (golden ratio α₀=(1+√5)/2) and j=1 (silver mean α₁=1+√2), compute the gauge function φ^{(j)}(m) using Eq. (5.53) (floor and fractional part, without referring to the paper), construct the mixed-model pair correlation C^{(c)}(l,m)=φ^{(j)}(l+m)φ^{(j)}(l-m)C0(l,m). Then compute the susceptibility χ(q,0) by summing over l,m (or using the convolution formula) on a fine q-grid. Locate the principal peak (maximum) for each j and write its q value to peak_positions.json.
- Output file: `/app/outputs/peak_positions.json`
- Format: json
- Contract: {"q_j0": <float>, "q_j1": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/peak_positions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### peak_positions.json
- path: `/app/outputs/peak_positions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The two principal peak positions of the wavevector-dependent susceptibility along q_x for the mixed quasiperiodic Ising model, computed at k=0.915398728… . The hidden checker compares each against the paper's exact analytic value within an absolute tolerance.
- schema:
  - `type`: object
  - `required`: `q_j0`, `q_j1`
  - `properties`:
    - `q_j0`:
      - `type`: number
      - `description`: Principal peak q-value for j=0 (golden ratio) in radians
    - `q_j1`:
      - `type`: number
      - `description`: Principal peak q-value for j=1 (silver mean) in radians

Notes: The output contract contains only the scored artifact. The intermediate C0 correlation file is not scored but its execution is forced because the load-bearing scored step requires it.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "peak_positions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "q_j0",
          "q_j1"
        ],
        "properties": {
          "q_j0": {
            "type": "number",
            "description": "Principal peak q-value for j=0 (golden ratio) in radians"
          },
          "q_j1": {
            "type": "number",
            "description": "Principal peak q-value for j=1 (silver mean) in radians"
          }
        }
      },
      "description": "The two principal peak positions of the wavevector-dependent susceptibility along q_x for the mixed quasiperiodic Ising model, computed at k=0.915398728… . The hidden checker compares each against the paper's exact analytic value within an absolute tolerance."
    }
  ],
  "notes": "The output contract contains only the scored artifact. The intermediate C0 correlation file is not scored but its execution is forced because the load-bearing scored step requires it."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that reads `/app/outputs/peak_positions.json`. The verifier compares the two reported peak positions against the correct reference values for this model, allowing for the small numerical spread that arises from different grid discretisations and summation truncations. The final score reflects how close your computed peaks are to the reference; a grossly inaccurate or missing value yields a very low score. Do not include any extra outputs—only the prescribed JSON file is inspected.
