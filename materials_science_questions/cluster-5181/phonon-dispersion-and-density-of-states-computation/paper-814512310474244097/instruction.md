# Self-consistent harmonic approximation for solid neon

## Problem background
Accurate computation of phonon properties in quantum crystals requires going beyond the conventional harmonic approximation because of large zero-point motion. The self-consistent harmonic approximation selects an optimal effective harmonic Hamiltonian whose force-constant matrix is the ground-state expectation of the second derivative of the true potential. When applied to solid neon with a Mie–Lennard‑Jones pair potential, this method yields a ground-state energy and force constants that can differ significantly from the conventional harmonic approximation, providing a better variational energy. The present task is to implement this method for a face‑centered cubic crystal of neon atoms and compute the resulting ground-state energy, force constants, and sound velocities.

## Approach
Set up a face‑centered cubic crystal of neon atoms with nearest‑neighbor distance b = 2.74 Å and the Mie–Lennard‑Jones potential parameters ε = 50.0 × 10⁻¹⁶ erg, σ = 2.74 Å. Begin with the conventional harmonic approximation (iteration 0): evaluate the force-constant matrix from the second derivatives of the potential at the equilibrium positions. Then apply the self‑consistent harmonic approximation. At each self‑consistent iteration (n = 1,2,3): use the current force-constant matrix to construct a harmonic Hamiltonian and its ground‑state wavefunction; evaluate the matrix elements of ∂²V/∂rᵢ∂rⱼ; average them with the previous force-constant matrix to obtain the new matrix. At every iteration (including iteration 0) compute the ground‑state energy W₀ (cal/mol), the nearest‑neighbor force constants Φ₀₁^xx and Φ₀₁^zz, the second‑nearest‑neighbor force constants Φ₀₂^xx and Φ₀₂^zz, and the longitudinal (c_l) and transverse (c_t) sound velocities in the [111] direction (10⁵ cm/s). The values at iteration 3 are the primary outcome of the calculation.

## Reproduction target
Implement the self‑consistent harmonic approximation for a face‑centered cubic crystal of neon atoms interacting via the Mie–Lennard‑Jones potential (ε = 50.0 × 10⁻¹⁶ erg, σ = 2.74 Å), with a fixed nearest‑neighbor distance b = 2.74 Å. Start from the conventional harmonic approximation (iteration 0) and perform three self‑consistent iterations (iterations 1, 2, 3). For every iteration, compute the ground‑state energy W₀ (cal/mol), the force‑constant components Φ₀₁^xx, Φ₀₁^zz, Φ₀₂^xx, Φ₀₂^zz, and the longitudinal c_l and transverse c_t sound velocities in the [111] direction (10⁵ cm/s). Write the per‑iteration results into the scored artifact `/app/outputs/iteration_results.json`. The values at iteration 3 constitute the primary reproduction target.

## Assets

- Python scientific computing stack: numpy scipy

## Workflow steps

### Step 1: Conventional harmonic approximation baseline
- Role: process
- Action: Set up a face-centered cubic crystal of neon atoms with nearest-neighbor distance b=2.74 Å. Compute the force-constant matrix in the conventional harmonic approximation (zeroth iteration) using the Mie-Lennard-Jones potential (ε=50.0×10⁻¹⁶ erg, σ=2.74 Å). Store the matrix internally.
- Evidence: none

### Step 2: Self-consistent harmonic approximation iterations
- Role: process
- Action: Starting from the conventional force-constant matrix, iteratively construct the self-consistent force-constant matrix Φ. At each iteration: use the current Φ to define a harmonic Hamiltonian, compute the ground-state wavefunction, evaluate the matrix elements of the second derivative of the potential, and update Φ by averaging with the previous matrix. At each iteration (1, 2, 3, plus the zeroth) compute and store the ground-state energy W₀ (cal/mol), nearest-neighbor force constants Φ₀₁^xx, Φ₀₁^zz, second-nearest-neighbor force constants Φ₀₂^xx, Φ₀₂^zz, and longitudinal and transverse sound velocities in the [111] direction (10⁵ cm/s).
- Evidence: none

### Step 3: Compile per-iteration results into JSON
- Role: scored (load-bearing)
- Action: Write the stored per-iteration data (iterations 0, 1, 2, 3) into a JSON file. Each entry must contain the iteration number, ground-state energy, force constants, and sound velocities.
- Output file: `/app/outputs/iteration_results.json`
- Format: json
- Contract: array of objects with fields: iteration (int), W0 (float, cal/mole), Phi01_xx (float), Phi01_zz (float), Phi02_xx (float), Phi02_zz (float), c_l (float, 10⁵ cm/s), c_t (float, 10⁵ cm/s).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/iteration_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### iteration_results.json
- path: `/app/outputs/iteration_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Per-iteration results of the self-consistent harmonic approximation for solid neon. The iteration 3 values are the primary reproduction target.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `iteration`, `W0`, `Phi01_xx`, `Phi01_zz`, `Phi02_xx`, `Phi02_zz`, `c_l`, `c_t`
    - `properties`:
      - `iteration`:
        - `type`: integer
      - `W0`:
        - `type`: number
        - `unit`: cal/mole
      - `Phi01_xx`:
        - `type`: number
        - `unit`: based on ε and σ
      - `Phi01_zz`:
        - `type`: number
        - `unit`: based on ε and σ
      - `Phi02_xx`:
        - `type`: number
        - `unit`: based on ε and σ
      - `Phi02_zz`:
        - `type`: number
        - `unit`: based on ε and σ
      - `c_l`:
        - `type`: number
        - `unit`: 10^5 cm/s
      - `c_t`:
        - `type`: number
        - `unit`: 10^5 cm/s

Notes: The hidden checker compares the submitted iteration 3 values against the paper's reported Table I within appropriate tolerances. Only iteration 3 is scored; the earlier iterations are present for completeness. Units are as indicated: W₀ in cal/mole, force constants in units derived from ε and σ, and sound velocities in 10⁵ cm/s.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "iteration_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "iteration",
            "W0",
            "Phi01_xx",
            "Phi01_zz",
            "Phi02_xx",
            "Phi02_zz",
            "c_l",
            "c_t"
          ],
          "properties": {
            "iteration": {
              "type": "integer"
            },
            "W0": {
              "type": "number",
              "unit": "cal/mole"
            },
            "Phi01_xx": {
              "type": "number",
              "unit": "based on ε and σ"
            },
            "Phi01_zz": {
              "type": "number",
              "unit": "based on ε and σ"
            },
            "Phi02_xx": {
              "type": "number",
              "unit": "based on ε and σ"
            },
            "Phi02_zz": {
              "type": "number",
              "unit": "based on ε and σ"
            },
            "c_l": {
              "type": "number",
              "unit": "10^5 cm/s"
            },
            "c_t": {
              "type": "number",
              "unit": "10^5 cm/s"
            }
          }
        }
      },
      "description": "Per-iteration results of the self-consistent harmonic approximation for solid neon. The iteration 3 values are the primary reproduction target."
    }
  ],
  "notes": "The hidden checker compares the submitted iteration 3 values against the paper's reported Table I within appropriate tolerances. Only iteration 3 is scored; the earlier iterations are present for completeness. Units are as indicated: W₀ in cal/mole, force constants in units derived from ε and σ, and sound velocities in 10⁵ cm/s."
}
```

## How you are scored
A hidden verifier will read the submitted `iteration_results.json` and compare the iteration 3 values of the ground‑state energy, force constants, and sound velocities against independently determined reference values. The final reward is based on how closely these quantities agree with the reference; simply reporting numbers without a correct implementation does not earn credit. The verifier expects the quantities to be computed from the self‑consistent procedure described in the workflow steps.
