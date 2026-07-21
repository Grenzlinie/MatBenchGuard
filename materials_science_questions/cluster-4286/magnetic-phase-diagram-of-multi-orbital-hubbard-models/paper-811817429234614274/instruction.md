# Superconductivity in a Two-Orbital Hubbard Model: Exact Diagonalization, Luttinger Parameter, and Pairing Correlations

## Problem background
Iron-based superconductors feature a multi-orbital electronic structure with electron and hole Fermi pockets. A minimal model capturing this physics is the one-dimensional two-orbital Hubbard model, where two orbitals with a crystal-field splitting Δ produce upper and lower bands. The model includes intra-orbital and inter-orbital Coulomb repulsions, Hund's rule coupling, and pair-hopping. Theoretical work suggests that superconducting (SC) phases can emerge as a function of the interaction parameters. The challenge is to compute the ground-state properties—specifically, the renormalized Luttinger liquid parameter K_ρ and various pairing correlation functions—and thereby determine the conditions under which SC order dominates and identify the pairing symmetries involved. The results are expected to show whether sign-reversing s-wave pairing, analogous to proposals for iron pnictides, can be stabilized in this minimal model.

## Approach
The task employs exact diagonalization (Lanczos) of the two-orbital Hubbard Hamiltonian on a finite cluster (6 sites, 12 orbitals) with appropriate boundary conditions to minimize finite-size effects. The model parameters are set as: hopping t=1, Hund coupling J=U'/4, intra-orbital repulsion U=U'+2J, and a fixed orbital splitting Δ=1.9. Two series of calculations are performed: (i) a sweep of inter-orbital repulsion U' from 0 to 4 (in steps of 0.5) at electron density n=5/3; for each value, the ground-state energy is used to extract the raw Luttinger parameter K_ρ^{raw} from the curvature of the energy versus flux, which is then normalized by the non-interacting result K_ρ^0. The ground-state total spin S is also recorded. (ii) For two specific parameter combinations—{U'=1.0, J=0.25, U=2.4} and {U'=1.0, J=0.25, U=-0.4}—the ground-state wavefunction is obtained, and a set of pairing correlation functions (spin-singlet on-site and nearest-neighbor, spin-triplet, and inter-orbital) is computed for distances r=0,…,3. No external dataset is required; the Hamiltonian is fully defined and the simulation is self-contained. The computed K_ρ and pairing correlations serve as the primary deliverables that characterize the superconducting tendencies.

## Reproduction target
Produce two JSON artifacts:

1. **`k_rho_data.json`** – an array of objects, each containing `U_prime` (float), `K_rho` (float, renormalized Luttinger parameter), and `ground_state_spin` (integer) for `U_prime` = 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, all at Δ=1.9 and electron filling 5/3 (10 electrons on a 6‑site chain).

2. **`pairing_correlations.json`** – an array of two objects, each with fields `parameters` (object with keys `U_prime`, `J`, `U`, `Delta`, `filling`) and `correlations` (object with ten 4‑element float arrays keyed by the correlation function labels). The two objects correspond to the two parameter sets:
   - `U_prime=1.0, J=0.25, U=2.4, Delta=1.9, filling="5/3"`
   - `U_prime=1.0, J=0.25, U=-0.4, Delta=1.9, filling="5/3"`
The arrays must contain absolute values of the correlation functions, except for the inter-orbital singlet and triplet correlations (`S_nn_l-u` and `T_nn_l-u`) where the sign must be retained. The ground-state spin for the K_ρ sweep must be reported as 0 (singlet) or 1 (triplet).

## Assets
No external datasets or pre-trained models are required. The two-orbital Hubbard Hamiltonian is fully specified by the parameters given above. The agent must implement the exact diagonalization and correlation calculation in a numerical computing environment, such as Python with standard scientific libraries (numpy, scipy). Libraries for sparse linear algebra and eigenvalue computation (e.g., scipy.sparse.linalg) are sufficient to run the Lanczos algorithm on the required system size. No GPU or specialized hardware is needed.

## Workflow steps

### Step 1: Exact diagonalization of the two-orbital Hubbard model on a 6-site chain
- Role: process
- Action: Implement the two-orbital Hubbard model Hamiltonian (with t=1, J=J') on a 6-site chain (12 orbitals) with periodic/antiperiodic boundary conditions chosen to minimize |K_rho^0-1| for filling n=5/3. Use the Lanczos algorithm to compute ground-state energies, total spins, and wavefunctions for a range of interaction parameters: U' from 0.0 to 4.0 in steps of 0.5 (with J=U'/4, U=U'+2J) at Δ=1.9, and for the two specific parameter sets (U'=1.0, J=0.25, U=2.4) and (U'=1.0, J=0.25, U=-0.4). Also compute the ground-state energy for the noninteracting case (U=U'=J=0) with the same boundary conditions to obtain K_rho^0. Save intermediate results internally; an evidence log (ed_log.txt) documents successful completion.
- Evidence: `/app/outputs/ed_log.txt`

### Step 2: Compute renormalized K_rho and ground-state spin for U' sweep
- Role: scored (load-bearing)
- Action: From the ED results, extract the raw Luttinger parameter K_rho_raw for each interacting case from the ground-state energy curvature. Compute the noninteracting K_rho^0 from the finite-size noninteracting result. Calculate renormalized K_rho = K_rho_raw / K_rho^0. For each U' value (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0), record U', the renormalized K_rho, and the ground-state total spin S (0 for singlet, 1 for triplet, etc.). Save the data as a JSON array.
- Output file: `/app/outputs/k_rho_data.json`
- Format: json
- Contract: JSON array of objects, each with fields: U_prime (float), K_rho (float), ground_state_spin (int).
- Scoring: scored by hidden verifier

### Step 3: Compute pairing correlation functions for two representative parameter points
- Role: scored (load-bearing)
- Action: For the two parameter sets (U'=1.0, J=0.25, U=2.4) and (U'=1.0, J=0.25, U=-0.4) at Δ=1.9, n=5/3, use the ground-state wavefunctions from ED to calculate the absolute values of the spin-singlet pairing correlation functions S_on^u, S_nn^u, S_on^l, S_nn^l, S_on^lu and the spin-triplet functions T_nn^u, T_nn^l, T_on^lu for distances r=0,1,2,3. Also compute the inter-orbital correlation functions S_nn^{l-u} and T_nn^{l-u} as defined in the paper. Save all results for both parameter sets as a JSON array of two objects.
- Output file: `/app/outputs/pairing_correlations.json`
- Format: json
- Contract: JSON array of two objects. Each object has: parameters (object with keys U_prime, J, U, Delta, filling) and correlations (object with keys S_on_u, S_nn_u, S_on_l, S_nn_l, S_on_lu, T_nn_u, T_nn_l, T_on_lu, S_nn_l-u, T_nn_l-u, each a list of 4 floats for distances r=0,1,2,3).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/k_rho_data.json`
- `/app/outputs/pairing_correlations.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### k_rho_data.json
- path: `/app/outputs/k_rho_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Renormalized K_rho and ground-state spin for a sweep of U' values at Δ=1.9 and n=5/3; compared against digitized reference values with absolute tolerance to verify the SC phase diagram.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `U_prime`, `K_rho`, `ground_state_spin`
    - `properties`:
      - `U_prime`:
        - `type`: number
      - `K_rho`:
        - `type`: number
      - `ground_state_spin`:
        - `type`: integer

### pairing_correlations.json
- path: `/app/outputs/pairing_correlations.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Pairing correlation functions for two parameter sets (U'=1.0, J=0.25 with U=2.4 and U=-0.4). The structural audit verifies the dominant pairing channel and inter-orbital sign reversal without exact numerical tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `parameters`, `correlations`
    - `properties`:
      - `parameters`:
        - `type`: object
        - `required`: `U_prime`, `J`, `U`, `Delta`, `filling`
        - `properties`:
          - `U_prime`:
            - `type`: number
          - `J`:
            - `type`: number
          - `U`:
            - `type`: number
          - `Delta`:
            - `type`: number
          - `filling`:
            - `type`: string
      - `correlations`:
        - `type`: object
        - `required`: `S_on_u`, `S_nn_u`, `S_on_l`, `S_nn_l`, `S_on_lu`, `T_nn_u`, `T_nn_l`, `T_on_lu`, `S_nn_l-u`, `T_nn_l-u`
        - `properties`:
          - `S_on_u`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `S_nn_u`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `S_on_l`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `S_nn_l`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `S_on_lu`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `T_nn_u`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `T_nn_l`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `T_on_lu`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `S_nn_l-u`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
          - `T_nn_l-u`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4

Notes: The task reproduces the main numerical results of the paper: the renormalized K_rho as a function of U' (detecting the SC phase and ferromagnetic transition) and the pairing correlation functions that identify the dominant pairing symmetry. The noninteracting band structure determination and the anomalous flux quantization check are not required as separate artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "k_rho_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "U_prime",
            "K_rho",
            "ground_state_spin"
          ],
          "properties": {
            "U_prime": {
              "type": "number"
            },
            "K_rho": {
              "type": "number"
            },
            "ground_state_spin": {
              "type": "integer"
            }
          }
        }
      },
      "description": "Renormalized K_rho and ground-state spin for a sweep of U' values at Δ=1.9 and n=5/3; compared against digitized reference values with absolute tolerance to verify the SC phase diagram."
    },
    {
      "file": "pairing_correlations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "parameters",
            "correlations"
          ],
          "properties": {
            "parameters": {
              "type": "object",
              "required": [
                "U_prime",
                "J",
                "U",
                "Delta",
                "filling"
              ],
              "properties": {
                "U_prime": {
                  "type": "number"
                },
                "J": {
                  "type": "number"
                },
                "U": {
                  "type": "number"
                },
                "Delta": {
                  "type": "number"
                },
                "filling": {
                  "type": "string"
                }
              }
            },
            "correlations": {
              "type": "object",
              "required": [
                "S_on_u",
                "S_nn_u",
                "S_on_l",
                "S_nn_l",
                "S_on_lu",
                "T_nn_u",
                "T_nn_l",
                "T_on_lu",
                "S_nn_l-u",
                "T_nn_l-u"
              ],
              "properties": {
                "S_on_u": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "S_nn_u": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "S_on_l": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "S_nn_l": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "S_on_lu": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "T_nn_u": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "T_nn_l": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "T_on_lu": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "S_nn_l-u": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                },
                "T_nn_l-u": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                }
              }
            }
          }
        }
      },
      "description": "Pairing correlation functions for two parameter sets (U'=1.0, J=0.25 with U=2.4 and U=-0.4). The structural audit verifies the dominant pairing channel and inter-orbital sign reversal without exact numerical tolerance."
    }
  ],
  "notes": "The task reproduces the main numerical results of the paper: the renormalized K_rho as a function of U' (detecting the SC phase and ferromagnetic transition) and the pairing correlation functions that identify the dominant pairing symmetry. The noninteracting band structure determination and the anomalous flux quantization check are not required as separate artifacts."
}
```

## How you are scored
A hidden verifier reads the two JSON files and independently scores each artifact. For **`k_rho_data.json`**, the renormalized K_ρ values are compared against expected physical results within an appropriate tolerance, and the ground-state spin is checked against the predicted phase (singlet vs. triplet) as a function of U′. For **`pairing_correlations.json`**, the verifier inspects the relative magnitudes among the spin‑singlet channels and the sign of specific inter‑orbital correlations to verify that the dominant pairing symmetry and inter‑orbital sign structure match the physical expectations for each parameter regime. Each artifact contributes a weight to the overall score, and the final reward is the combined weighted fraction in [0,1]. Meeting the required structural and numerical thresholds yields full credit; a missing or trivial artifact yields zero.
