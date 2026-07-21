# Effective exchange coupling sign in triangular cluster with vacancy for two multi-spin exchange models

## Problem background
Monolayer ³He adsorbed on a graphite surface forms a triangular lattice of spin-1/2 fermions, where multiple‑spin‑exchange (MSE) interactions are important due to hard‑core repulsion. At the 4/7 commensurate phase, introducing zero‑point vacancies (doping) is known experimentally to make the system less ferromagnetic. Two theoretical models describe the magnetic exchange in the presence of vacancies: the triangular‑lattice t‑J‑K model, which absorbs three‑spin exchange into an effective two‑spin coupling, and the t‑J₂‑J₃‑J₄ model, which treats the three‑spin ring‑exchange term independently and accounts for the truncation of ring‑exchange paths around a vacancy. The physical picture is that when a vacancy is introduced into a triangular plaquette, the residual magnetic interaction between the remaining two spins depends on how the three‑spin processes are cut. Computing the effective exchange coupling between those two spins is therefore a direct test of the two models. Your task is to compute this coupling by exact diagonalization of a minimal three‑site cluster.

## Approach
You will implement and diagonalise the Hamiltonians for a triangular three‑site cluster with one fixed vacant site and two spin‑1/2 particles, respecting the hard‑core constraint (no double occupancy). Hopping is set to zero (t = 0) to isolate the pure magnetic exchange. You will implement two models:

1. **t‑J‑K model** – the three‑spin exchange is absorbed into an effective two‑spin interaction. Use the relation J = J₂ + 4 J₃ and fix the effective exchange to J = −0.3 (in the paper’s energy units). The J₃ term is considered to be already included in this J; no separate three‑spin operator is applied.
2. **t‑J₂‑J₃‑J₄ model** – the two‑, three‑, and four‑spin exchanges are treated independently: J₂ = 0.3, J₃ = −0.15, J₄ = 0. The three‑spin permutation term J₃ is only active when all three sites of the triangle are occupied; in the presence of a vacancy it is absent. This is the key structural difference between the models.

For each model, construct the Hamiltonian in the singlet and triplet total‑spin sectors of the two‑particle basis, then diagonalise each block to obtain the lowest eigenvalues E_singlet and E_triplet. The effective exchange coupling is defined as J_eff = E_triplet − E_singlet.

## Reproduction target
Produce a CSV file containing the singlet and triplet ground‑state energies for the two models:
- `t-J-K`
- `t-J2-J3-J4`
The effective exchange coupling J_eff = E_triplet − E_singlet will be computed from these raw energies, and its sign (ferromagnetic J_eff < 0 or antiferromagnetic J_eff > 0) is the quantity of interest. The CSV must have columns: `model`, `E_singlet`, `E_triplet`.

## Assets
No external datasets or model weights are required. All necessary numerical parameters are specified in the Approach above. The workflow requires standard linear‑algebra and scientific‑computing libraries, which can be installed from PyPI, e.g. `numpy` and `scipy` (Tsinghua mirror recommended).

## Workflow steps

### Step 1: Construct triangle cluster Hamiltonians
- Role: process
- Action: Define the Hilbert space for two spin-1/2 particles on a three-site triangular lattice with one fixed vacancy. Implement the t-J-K Hamiltonian (effective J = J2+4J3) and the t-J2-J3-J4 Hamiltonian (with independent J2, J3, J4 terms, where J3 term only active when all three sites are occupied). Set hopping t=0 to isolate magnetic exchange. Construct the singlet and triplet Hamiltonian blocks for each model.
- Evidence: none

### Step 2: Compute singlet and triplet energies
- Role: scored (load-bearing)
- Action: Diagonalize the singlet and triplet Hamiltonian blocks for both models. Extract the lowest eigenvalues as E_singlet and E_triplet. Write the four energies to a CSV file.
- Output file: `/app/outputs/step_01_energies.csv`
- Format: csv
- Contract: columns: model (string), E_singlet (float), E_triplet (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energies.csv
- path: `/app/outputs/step_01_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The singlet and triplet energies for both models, used to compute effective exchange J_eff = E_triplet - E_singlet.
- schema:
  - `type`: table
  - `required_columns`: `model`, `E_singlet`, `E_triplet`
  - `units`: object

Notes: The checker will recompute J_eff from the raw energies and verify that for the t-J-K model J_eff < 0 (ferromagnetic) and for the t-J2-J3-J4 model J_eff > 0 (antiferromagnetic) within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "E_singlet",
          "E_triplet"
        ],
        "units": {}
      },
      "description": "The singlet and triplet energies for both models, used to compute effective exchange J_eff = E_triplet - E_singlet."
    }
  ],
  "notes": "The checker will recompute J_eff from the raw energies and verify that for the t-J-K model J_eff < 0 (ferromagnetic) and for the t-J2-J3-J4 model J_eff > 0 (antiferromagnetic) within a tolerance."
}
```

## How you are scored
A hidden verifier will read your `step_01_energies.csv`, recompute J_eff for each model, and check that the sign of J_eff is physically consistent with the expected behaviour of each model and that the energy values are numerically plausible (within a tolerance appropriate for an independent implementation). The reward is monotonic in the correctness of the sign and in the quality of the computed energies; a better (more accurate) result is never penalised. You are scored on the output artifact alone; reporting a number without honestly performing the computation is detectable and will not yield a valid artifact.
