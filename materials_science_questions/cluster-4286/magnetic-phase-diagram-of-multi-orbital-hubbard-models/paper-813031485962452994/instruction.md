# Reentrant Fulde-Ferrell-Larkin-Ovchinnikov superfluidity on the honeycomb lattice

## Problem background
We study the ground-state phase diagram of the attractive Hubbard model on the honeycomb lattice, motivated by experiments with ultracold fermionic atoms in artificial hexagonal optical lattices. The model features nearest-neighbor hopping, an on-site attraction U (negative), a chemical potential μ, and a Zeeman magnetic field h that induces a population imbalance between the two spin components. At half filling (average particle number per site n=1) and zero field, the non-interacting density of states vanishes linearly at the Fermi level, leading to a semimetal phase. A finite pairing interaction |U| exceeding a critical value |U_c| is required to stabilize a homogeneous BCS superfluid. In the presence of a Zeeman field, one can ask whether an inhomogeneous superfluid with a nonzero total momentum Q of Cooper pairs — the Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) phase — can appear even when |U| < |U_c|, and how the optimal Q evolves with the magnetic field. The task is to determine these ground-state properties within a mean-field theory that allows an arbitrary Cooper-pair momentum.

## Approach
The system is described by a two-sublattice tight-binding Hamiltonian on the honeycomb lattice. Superconductivity is introduced by a mean-field decoupling of the on-site attraction, yielding a spatially modulated order parameter ansatz that respects the two sublattices: the order parameter on sublattice A is Δ₀ exp(i Q·R_j) and on sublattice B is Δ₀ exp[i Q·(R_j + w)], where w is the vector connecting the two basis atoms. The mean-field Hamiltonian is written in a Nambu-like 4×4 Bogoliubov–de Gennes form in reciprocal space, depending on the order-parameter amplitude Δ₀ and the Cooper-pair momentum Q. The ground state is found by evaluating the zero-temperature grand potential Ω(Δ₀, Q) on a discrete grid of k-points in the first Brillouin zone and minimizing it globally with respect to both Δ₀ ≥ 0 and all allowed Q vectors. Three computations are performed: (1) At h=0, U is varied to locate the smallest |U| for which Δ₀ > 0, giving the critical interaction |U_c|. (2) With U fixed at −2.0t, the global minimum of Ω is found at the three representative fields h/t = 0.5, 1.0, 1.5, assigning a phase label (normal if Δ₀ is negligible, BCS if Δ₀ > 0 and |Q|=0, FFLO if Δ₀ > 0 and |Q|>0) and recording the optimal Δ₀ and Q. (3) For the same U = −2.0t, a fine sweep of h across the relevant field window is carried out; at each h the optimal Q is recorded to map the evolution of the Cooper-pair momentum vector.

## Reproduction target
Produce three artifacts: (a) The critical interaction |U_c| (positive, in units of the hopping t) that separates the normal semimetal from the BCS superfluid at half filling and zero magnetic field. (b) For a fixed attraction U = −2.0t (which is below the reported critical interaction), the ground-state phase and order parameter at three Zeeman fields, h/t = 0.5, 1.0, and 1.5: report the order-parameter amplitude Δ₀, the optimal Cooper-pair momentum Q = (Qx, Qy), and the phase label. (c) The evolution of the optimal momentum vector Q as a function of h across the field range where the inhomogeneous phase might occur (e.g., from h/t ≈ 0.5 to 1.5), capturing any non‑monotonic changes in both magnitude and direction of Q. All results must be computed from the mean-field theory described above and saved in the specified output files.

## Assets

- Python 3.x: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Critical interaction for BCS
- Role: scored
- Action: At half filling (chemical potential = 0) and zero Zeeman field (h = 0), implement the mean-field decoupling of the attractive Hubbard model on the honeycomb lattice. Systematically vary the attractive interaction U (negative) and self-consistently determine the superconducting order parameter via the grand potential minimization on a discrete k‑mesh in the first Brillouin zone. Report the critical value |U_c| (in units of t) as the smallest |U| for which the order parameter is non-zero.
- Output file: `/app/outputs/uc_output.json`
- Format: json
- Contract: {"U_c": float (positive, units of t)}
- Scoring: scored by hidden verifier

### Step 2: Phase points at fixed U
- Role: scored (load-bearing)
- Action: Fix U = −2.0t and μ = 0. For each of the three Zeeman fields h/t = 0.5, 1.0, 1.5, perform an unrestricted global minimization of the grand potential over the order parameter amplitude and Cooper‑pair momentum. Determine the optimal order parameter Δ₀, momentum Q = (Qx, Qy) and the ground‑state phase label ("NO" for negligible Δ₀, "FFLO" for Δ₀>0 and |Q|>0, "BCS" for Δ₀>0 and |Q|=0).
- Output file: `/app/outputs/phase_points.json`
- Format: json
- Contract: [{"U": float, "h": float, "delta0": float, "Qx": float, "Qy": float, "phase": string}]  // U, h in units of t; phase one of "NO", "FFLO", "BCS"
- Scoring: scored by hidden verifier

### Step 3: Q-vector evolution across FFLO window
- Role: scored (load-bearing)
- Action: Fix U = −2.0t and μ = 0. Sweep h/t over a dense range covering the FFLO window (e.g., from 0.5 to 1.5). At each h, compute the optimal Cooper‑pair momentum Q and the phase using the same global minimization. Output a table that captures the non‑monotonic evolution of Q, including changes in magnitude and direction.
- Output file: `/app/outputs/q_evolution.csv`
- Format: csv
- Contract: columns: h/t, Qx, Qy, phase (header row required; h/t, Qx, Qy are floats; phase is string)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/uc_output.json`
- `/app/outputs/phase_points.json`
- `/app/outputs/q_evolution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### uc_output.json
- path: `/app/outputs/uc_output.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical interaction |U_c|/t. The checker compares the reported value to the paper’s reference within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `U_c`: float (positive, units of t)

### phase_points.json
- path: `/app/outputs/phase_points.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Ground-state phase and order parameter at three magnetic fields. The checker verifies that at the expected fields the phase labels and threshold amplitudes match the paper’s predictions.
- schema:
  - `type`: array
  - `items`:
    - `U`: float (units of t)
    - `h`: float (units of t)
    - `delta0`: float (order parameter amplitude)
    - `Qx`: float
    - `Qy`: float
    - `phase`: string (one of 'NO', 'FFLO', 'BCS')

### q_evolution.csv
- path: `/app/outputs/q_evolution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Evolution of Q vector with magnetic field. The checker inspects the non-monotonic trend (change of direction, presence of three distinct regimes).
- schema:
  - `type`: table
  - `required_columns`: `h/t`, `Qx`, `Qy`, `phase`
  - `units`:
    - `h/t`: unitless
    - `Qx`: units of reciprocal lattice
    - `Qy`: units of reciprocal lattice
    - `phase`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "uc_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "U_c": "float (positive, units of t)"
        }
      },
      "description": "Critical interaction |U_c|/t. The checker compares the reported value to the paper’s reference within a tolerance."
    },
    {
      "file": "phase_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "U": "float (units of t)",
          "h": "float (units of t)",
          "delta0": "float (order parameter amplitude)",
          "Qx": "float",
          "Qy": "float",
          "phase": "string (one of 'NO', 'FFLO', 'BCS')"
        }
      },
      "description": "Ground-state phase and order parameter at three magnetic fields. The checker verifies that at the expected fields the phase labels and threshold amplitudes match the paper’s predictions."
    },
    {
      "file": "q_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "h/t",
          "Qx",
          "Qy",
          "phase"
        ],
        "units": {
          "h/t": "unitless",
          "Qx": "units of reciprocal lattice",
          "Qy": "units of reciprocal lattice",
          "phase": "string"
        }
      },
      "description": "Evolution of Q vector with magnetic field. The checker inspects the non-monotonic trend (change of direction, presence of three distinct regimes)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will inspect the three output files. The critical interaction |U_c| will be compared to the paper’s reference value with an appropriate tolerance; the phase-point entries at the three nominated h values will be checked for consistency with expected phase labels and for realistic threshold behaviour of the order parameter; the Q-evolution table will be examined for a non‑monotonic pattern — specifically, the presence of distinct directional regimes as the field increases, consistent with a genuine mean-field solution on the honeycomb lattice. Each stage contributes a weight to the overall score; the verifier does not require the numbers to match the paper exactly, but the physics they embody (where and how the order appears and how the pair momentum evolves) must be reproduced within the natural spread of an independent mean-field implementation.
