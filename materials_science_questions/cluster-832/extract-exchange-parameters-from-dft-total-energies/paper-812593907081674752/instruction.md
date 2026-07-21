# Spin-wave spectrum from Heisenberg model with exchange, anisotropy, and dipolar interactions

## Problem background
Ferromagnetic/nonmagnetic multilayers exhibit thickness-dependent magnetic properties influenced by interface quality and exchange interactions. A central theoretical tool is the computation of spin-wave (magnon) excitation spectra from a Heisenberg Hamiltonian. The target of this task is the magnon dispersion for a single ferromagnetic film of eight atomic planes, which shows acoustic and optical mode branches governed by exchange, anisotropy, and dipolar contributions. Reproducing this spectrum verifies the numerical implementation of the spin-wave model.

## Approach
The system is modeled by a Heisenberg Hamiltonian that includes three types of exchange interactions (bulk, surface, and interlayer) and a single-ion interface anisotropy. Dipolar interactions are neglected in this model (set ω_M = 0). The magnetic film has n = 8 atomic layers with a hexagonal (001) structure; the nearest-neighbor counts are n_parallel = 6 within a layer, n_perp = 3 to the adjacent layer in the same film, and n_up = 3 to the neighboring film. Using the Holstein-Primakoff transformation, the spin operators are mapped to boson ladder operators and the Hamiltonian is expanded to quadratic order. For each in-plane wave vector k (k_x, with k_y = 0, k_z = 0), one constructs a 2n × 2n linear system of motion equations for the creation and annihilation operators. Diagonalizing this system yields the magnon eigen-energies. The n positive eigenvalues form the magnon branches; their dependence on k_x reveals the dispersion. The calculation uses the specified spin S = 0.78 and the coupling/anisotropy constants in Kelvin: J_b = 120, J_s = 70, J_I = 0.01, D^∥ = 0.6, D^⊥ = 0. No external data is needed; all parameters are given here.

## Reproduction target
Implement the Holstein-Primakoff linearisation described above and solve the eigenvalue problem for the given parameters. Choose at least 20 k_x points evenly spaced between 0 and π/a (where a is the in-plane lattice constant). For each k_x, compute the 8 positive magnon eigen-energies in Kelvin. Write the results to a JSON file with an array of objects, each containing the keys 'k_x' (float), 'branch_index' (integer from 1 to 8), and 'energy' (float). The goal is to reproduce the correct dispersion branches, including the acoustic modes (low energy near k_x = 0) and higher optical modes.

## Assets
- Python 3.9+ (available via standard package managers)
- NumPy and SciPy (install via pip: `python3 -m pip install numpy scipy`)

No external datasets, pretrained models, or proprietary tools are required. All physical parameters are provided in the Approach section.

## Workflow steps

### Step 1: Compute spin-wave eigenvalues
- Role: scored (load-bearing)
- Action: Implement the Heisenberg Hamiltonian with exchange and interface anisotropy, neglecting dipolar interactions (set ω_M = 0), using the Holstein-Primakoff linear approximation for a single ferromagnetic film of n=8 atomic planes. Assemble the 2n x 2n system for each k_x value (with k_y=0, k_z=0) using the given parameters: S=0.78, J_b=120 K, J_s=70 K, J_I=0.01 K, D_parallel=0.6 K, D_perp=0 K, and hexagonal (001) structure with neighbor counts n_parallel=6, n_perp=3, n_up=3. Solve the eigenvalue problem to obtain the positive magnon energies. Output the eigenvalues for a set of at least 20 k_x points evenly spaced from 0 to π/a.
- Output file: `/app/outputs/spin_wave_eigenvalues.json`
- Format: json
- Contract: array of objects, each with: 'k_x' (float, in units of inverse lattice constant), 'branch_index' (integer, 1 to 8), 'energy' (float, eigenvalue in Kelvin)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_wave_eigenvalues.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_wave_eigenvalues.json
- path: `/app/outputs/spin_wave_eigenvalues.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: List of all positive magnon eigenvalues for each k-point and branch index. At least 20 k-points must be included. The recomputation ignores dipolar interactions (ω_M=0).
- schema:
  - `type`: array
  - `items`:
    - `k_x`: float, inverse lattice constant
    - `branch_index`: integer, 1..8
    - `energy`: float, Kelvin
  - `required`: `k_x`, `branch_index`, `energy`

Notes: The checker implements the same spin-wave model (exchange + anisotropy, no dipolar) and recomputes eigenvalues on the same k-grid, then compares the agent's values via RMS deviation and branch structure checks. No external hidden holdout is needed, only the derived numerical reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_wave_eigenvalues.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "k_x": "float, inverse lattice constant",
          "branch_index": "integer, 1..8",
          "energy": "float, Kelvin"
        },
        "required": [
          "k_x",
          "branch_index",
          "energy"
        ]
      },
      "description": "List of all positive magnon eigenvalues for each k-point and branch index. At least 20 k-points must be included. The recomputation ignores dipolar interactions (ω_M=0)."
    }
  ],
  "notes": "The checker implements the same spin-wave model (exchange + anisotropy, no dipolar) and recomputes eigenvalues on the same k-grid, then compares the agent's values via RMS deviation and branch structure checks. No external hidden holdout is needed, only the derived numerical reference."
}
```

## How you are scored
A hidden verifier will independently re-implement the same spin-wave model using the parameters given in the Approach. It recomputes the eigenvalues for every k_x point you report and compares them with your submitted values. The verifier checks structural properties (exactly 8 positive branches, the lowest branch approaching zero at k_x = 0, correct separation into acoustic and optical groups) and numeric agreement within a tolerance. Your final reward is based on how well your computed eigenvalues match the recomputed reference across all k-points and branches. Reporting numbers without computation is not sufficient; the verifier recomputes from scratch.
