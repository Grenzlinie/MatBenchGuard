# Hole Binding Energy in Coupled Spin-Fermion Model via Exact Diagonalization

## Problem background
High-temperature superconductivity in oxide materials remains a major puzzle in condensed matter physics, with a possible origin in purely electronic mechanisms driven by magnetic correlations. A candidate framework is a coupled spin-fermion Hamiltonian that describes holes moving on a lattice of interacting quantum spins. In the limit of zero hole hopping, the formation of a bound state between two holes provides direct evidence that magnetic interactions alone can generate an attractive effective interaction—a necessary ingredient for superconductivity. Numerical exact diagonalization on small clusters allows a quantitative test of this idea by computing the binding energy of two holes. The challenge is to compute this binding energy accurately in the thermodynamic limit through finite-size extrapolation, without any dependence on the holes' kinetic energy.

## Approach
The investigation focuses on a square lattice where each spin-1/2 Heisenberg site also hosts a fermionic site (z_K=1 geometry). The Hamiltonian consists of an antiferromagnetic Heisenberg exchange J_S among the spins and an on-site or nearest-neighbor Kondo coupling J_K between the fermion spin and the local spin. The holes are fully localized (transfer t=0, on-site U=0). The central computation is to exactly diagonalize the many-body Hamiltonian for 0, 1, and 2 fermions on a series of finite clusters (up to about 24 sites) with free boundary conditions in the y-direction and periodic in the x-direction. Two extreme coupling limits are considered: infinite antiferromagnetic Kondo coupling (J_K → –∞), where each fermion forms a spin singlet with the underlying spin, and infinite ferromagnetic coupling (J_K → +∞), where the fermion aligns with the spin. For each lattice size, the ground-state energies E0 (no hole), E1 (one hole), and E2 (two holes) are computed, and the raw binding energy Δ = 2E1 – E0 – E2 is extracted. A double extrapolation removes finite-size effects: for each fixed Lx, Δ is plotted against 1/Ly and extrapolated to Ly → ∞ via a linear fit, and then the resulting Lx-dependent values are extrapolated to Lx → ∞ using a linear fit in 1/Lx. The final extrapolated scaled binding energy is obtained by dividing by |J_S| (set to 1).

## Reproduction target
Compute the extrapolated scaled binding energy |E_B|/|J_S| for the coupled spin-fermion model on the square lattice (z_K=1) with t=0, U=0, J_S = –1. Perform the calculation for the two limiting Kondo couplings: J_K = –∞ and J_K = +∞. Output the raw ground-state energies used for each (Lx, Ly) combination, together with the final extrapolated binding energies after double extrapolation (Ly → ∞ then Lx → ∞).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Exact diagonalization and binding energy computation
- Role: scored
- Action: Implement the coupled spin-fermion Hamiltonian H = -J_S/2 Σ S_k·S_l - J_K/2 Σ σ_i·S_k on a square lattice with one fermion site per spin site (z_K=1). Fix t=0, U=0, J_S=-1. Use free boundary condition in the y-direction and periodic in the x-direction. Build and diagonalize the many-body Hamiltonian in the 0-, 1-, and 2-fermion sectors for a set of lattice sizes up to ~24 sites. For J_K = -∞, enforce infinite antiferromagnetic Kondo coupling by projecting onto spin-singlet states on each fermion site; for J_K = +∞, enforce ferromagnetic alignment. For each lattice, compute ground-state energies E0, E1, E2 and the raw binding energy Δ = 2E1 - E0 - E2. Perform double extrapolation: for each Lx, extrapolate Δ to Ly→∞ by linear fit vs 1/Ly; then extrapolate the Ly-extrapolated values to Lx→∞ by linear fit vs 1/Lx. Scale the final result by |J_S| (=1) to obtain the extrapolated binding energy. Write all raw energies and the extrapolated scaled binding energies for J_K = -∞ and J_K = +∞ to binding_energy_data.json.
- Output file: `/app/outputs/binding_energy_data.json`
- Format: json
- Contract: A JSON object with top-level keys 'JK_neg_inf' and 'JK_pos_inf'. Each is an object with: 'z_K' (integer, 1), 'J_S' (float, -1.0), 'lattices' (array of objects, each with 'Lx' (int), 'Ly' (int), 'E0' (float), 'E1' (float), 'E2' (float)), and 'extrapolated_E_B_scaled' (float) giving the final binding energy scaled by |J_S|.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energy_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energy_data.json
- path: `/app/outputs/binding_energy_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Raw ground-state energies and extrapolated binding energies for two limiting Kondo couplings from exact diagonalization of the coupled spin-fermion model.
- schema:
  - `type`: object
  - `required`: `JK_neg_inf`, `JK_pos_inf`
  - `JK_neg_inf`:
    - `type`: object
    - `required`: `z_K`, `J_S`, `lattices`, `extrapolated_E_B_scaled`
    - `z_K`:
      - `type`: integer
    - `J_S`:
      - `type`: float
    - `lattices`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `Lx`, `Ly`, `E0`, `E1`, `E2`
        - `Lx`:
          - `type`: integer
        - `Ly`:
          - `type`: integer
        - `E0`:
          - `type`: float
        - `E1`:
          - `type`: float
        - `E2`:
          - `type`: float
    - `extrapolated_E_B_scaled`:
      - `type`: float
  - `JK_pos_inf`:
    - `type`: object
    - `required`: `z_K`, `J_S`, `lattices`, `extrapolated_E_B_scaled`
    - `z_K`:
      - `type`: integer
    - `J_S`:
      - `type`: float
    - `lattices`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `Lx`, `Ly`, `E0`, `E1`, `E2`
        - `Lx`:
          - `type`: integer
        - `Ly`:
          - `type`: integer
        - `E0`:
          - `type`: float
        - `E1`:
          - `type`: float
        - `E2`:
          - `type`: float
    - `extrapolated_E_B_scaled`:
      - `type`: float

Notes: The checker will recompute the final extrapolated binding energy from the raw energies to verify against the paper's reported values. No external datasets are required; all inputs are parameters specified in the task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energy_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "JK_neg_inf",
          "JK_pos_inf"
        ],
        "JK_neg_inf": {
          "type": "object",
          "required": [
            "z_K",
            "J_S",
            "lattices",
            "extrapolated_E_B_scaled"
          ],
          "z_K": {
            "type": "integer"
          },
          "J_S": {
            "type": "float"
          },
          "lattices": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "Lx",
                "Ly",
                "E0",
                "E1",
                "E2"
              ],
              "Lx": {
                "type": "integer"
              },
              "Ly": {
                "type": "integer"
              },
              "E0": {
                "type": "float"
              },
              "E1": {
                "type": "float"
              },
              "E2": {
                "type": "float"
              }
            }
          },
          "extrapolated_E_B_scaled": {
            "type": "float"
          }
        },
        "JK_pos_inf": {
          "type": "object",
          "required": [
            "z_K",
            "J_S",
            "lattices",
            "extrapolated_E_B_scaled"
          ],
          "z_K": {
            "type": "integer"
          },
          "J_S": {
            "type": "float"
          },
          "lattices": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "Lx",
                "Ly",
                "E0",
                "E1",
                "E2"
              ],
              "Lx": {
                "type": "integer"
              },
              "Ly": {
                "type": "integer"
              },
              "E0": {
                "type": "float"
              },
              "E1": {
                "type": "float"
              },
              "E2": {
                "type": "float"
              }
            }
          },
          "extrapolated_E_B_scaled": {
            "type": "float"
          }
        }
      },
      "description": "Raw ground-state energies and extrapolated binding energies for two limiting Kondo couplings from exact diagonalization of the coupled spin-fermion model."
    }
  ],
  "notes": "The checker will recompute the final extrapolated binding energy from the raw energies to verify against the paper's reported values. No external datasets are required; all inputs are parameters specified in the task."
}
```

## How you are scored
A hidden verifier independently scores each workflow step's artifact and combines them into the final reward. For the exact diagonalization step, the verifier reads the raw energies from the submitted JSON file, recomputes the per-lattice binding energies, and performs the same double extrapolation to obtain a binding energy for each Kondo coupling. That recomputed value is compared against a hidden reference. The verifier also checks that the self-reported extrapolated values in the file are consistent with the recomputed values. Meeting the required accuracy on the extrapolated binding energy yields full credit for this step; larger deviations incur partial or zero credit. Additional checks verify that all required lattice data are present and that the binding energies are positive. No external datasets or pretrained models are used; all results must be generated from the specified Hamiltonian and parameters.
