# Transfer-Matrix Finite-Size Scaling Phase Diagram of the Spin-1 Baxter-Wu Model

## Problem background
The spin‑1 Baxter–Wu model on a triangular lattice with a crystal‑field anisotropy arises from adding a single‑ion term Δ Σ s_i^2 to the three‑spin interaction −J Σ s_i s_j s_k, where s_i ∈ {−1,0,1}. In the pure (Δ → −∞) limit the model reduces to the well‑studied Baxter–Wu model, which belongs to the four‑state Potts universality class. The presence of a crystal field creates a competition between the ordered and disordered phases, and it is of considerable interest to understand whether the model exhibits a line of second‑order phase transitions for finite values of the crystal field and whether a multicritical point (where the second‑order line meets a first‑order transition) exists at finite temperature and crystal field. Earlier finite‑size work conjectured that second‑order transitions occur only in the Δ → −∞ limit, but a later renormalization‑group and conformal‑invariance study indicated a richer phase diagram. This task reproduces the core finite‑size scaling analysis of the transfer‑matrix spectrum to determine the second‑order transition line, the location of the multicritical point, and the associated conformal anomaly and scaling dimensions.

## Approach
The method is a transfer‑matrix finite‑size scaling (FSS) analysis augmented by conformal‑invariance relations. The row‑to‑row transfer matrix T is built for a triangular‑lattice strip of width N with periodic boundary conditions; its entries are Boltzmann weights determined by the reduced temperature t = k_B T / J and the reduced crystal field δ = Δ / J. Diagonalizing T yields the largest eigenvalues Λ_0(N) > Λ_1(N) > …. From these, the mass gap G_N(t) = ln(Λ_0/Λ_1) is computed. For a given δ, the critical temperature t_c(δ) is estimated by solving the two‑width crossing condition G_6(t) * 6 = G_9(t) * 9. The multicritical point (δ_t, t_t) is found by solving the three‑width condition G_3(t) * 3 = G_6(t) * 6 = G_9(t) * 9 simultaneously for t and δ. At each critical point, the conformal anomaly c is obtained from the finite‑size behaviour of the ground‑state energy Λ_0(N). Using two sizes (N = 3 and 6) one extrapolates c with a dominant correction exponent w = 4 (the value for the pure Baxter–Wu model). The scaling dimensions x(1,0) and x(2,0) that govern thermal fluctuations are extracted from the gaps between the leading eigenvalues in the momentum‑zero sector, using the relation x^N(n,0) = (N / (π√3)) ln(Λ_0(N)/Λ_n(N)), with N = 9 providing the final estimate. The entire analysis is implemented in Python using numpy and scipy for sparse linear algebra and Lanczos diagonalization.

## Reproduction target
- Build and diagonalize the transfer matrix for strip widths N = 3, 6, 9.
- For δ ∈ {−10, −1, 1, 1.25, 1.3089}, locate t_c(δ) by solving G_6(t) * 6 = G_9(t) * 9; record the eigenvalues Λ_0 and Λ_1 for N = 6 and 9 at the solution.
- Solve G_3(t) * 3 = G_6(t) * 6 = G_9(t) * 9 to find the multicritical point (δ_t, t_t); record Λ_0 and Λ_1 for N = 3, 6, 9 at that point.
- For each δ and at the multicritical point, compute the conformal anomaly c from the N = 3 and 6 ground‑state energies (using the two‑size extrapolation with w = 4) and the scaling dimensions x(1,0) and x(2,0) from the N = 9 eigenvalue spectrum.
- Write all derived quantities together with the raw eigenvalues to `/app/outputs/results.json` in the exact schema described under "Output contract".

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Implement and diagonalize the transfer matrix
- Role: process
- Action: Implement the row-to-row transfer matrix for the spin-1 Baxter–Wu model with a crystal field on a triangular-lattice strip of width N with periodic boundary conditions, using the Boltzmann weight expression with reduced temperature t and reduced crystal field δ. Diagonalize the matrix using the Lanczos method for non-Hermitian matrices, exploiting translational symmetry, to obtain the largest eigenvalues Λ0, Λ1, Λ2, ...
- Evidence: `/app/outputs/diagonalization.log`

### Step 2: Compute finite-size scaling results
- Role: scored (load-bearing)
- Action: Using the diagonalization routine, perform finite-size scaling analysis for δ in {-10, -1, 1, 1.25, 1.3089}: (a) For each δ, solve the two-width crossing condition G_6(t)*6 = G_9(t)*9 to find critical temperature t_c(δ), where G_N = ln(Λ0/Λ1). Record eigenvalues for N=6,9 at the solution. (b) For the multicritical point, solve G_3(t)*3 = G_6(t)*6 = G_9(t)*9 simultaneously for t and δ, and record eigenvalues for N=3,6,9. (c) At each critical temperature, compute the conformal anomaly c from the ground-state energy scaling using the two-size extrapolation with a dominant correction exponent w=4. (d) Compute scaling dimensions x(1,0) and x(2,0) from the excitation spectrum using N=9. Store all results and the relevant raw eigenvalue data in results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: An object with keys: 'critical_line' (array of objects each with delta (number), t_c (number), eigenvalues_N6 (object with Lambda0, Lambda1), eigenvalues_N9 (object), eigenvalues_N3 (object, only for delta=1.3089), c (number), x1_0 (number), x2_0 (number)), 'multicritical_point' (object with delta_t, t_t, eigenvalues_N3, eigenvalues_N6, eigenvalues_N9). All numeric values as floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains raw eigenvalue data and derived quantities (critical line, multicritical point, conformal anomaly, scaling dimensions). The checker will recompute mass gaps, solve crossing conditions, recompute c and scaling dimensions from the provided eigenvalues, and compare derived quantities to hidden references.
- schema:
  - `type`: object
  - `required`: `critical_line`, `multicritical_point`
  - `properties`:
    - `critical_line`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `delta`, `t_c`, `eigenvalues_N6`, `eigenvalues_N9`, `c`, `x1_0`, `x2_0`
        - `properties`:
          - `delta`:
            - `type`: number
          - `t_c`:
            - `type`: number
          - `eigenvalues_N6`:
            - `type`: object
            - `required`: `Lambda0`, `Lambda1`
            - `properties`:
              - `Lambda0`:
                - `type`: number
              - `Lambda1`:
                - `type`: number
          - `eigenvalues_N9`:
            - `type`: object
            - `required`: `Lambda0`, `Lambda1`
            - `properties`:
              - `Lambda0`:
                - `type`: number
              - `Lambda1`:
                - `type`: number
          - `eigenvalues_N3`:
            - `type`: object
            - `required`: `Lambda0`, `Lambda1`
            - `properties`:
              - `Lambda0`:
                - `type`: number
              - `Lambda1`:
                - `type`: number
          - `c`:
            - `type`: number
          - `x1_0`:
            - `type`: number
          - `x2_0`:
            - `type`: number
    - `multicritical_point`:
      - `type`: object
      - `required`: `delta_t`, `t_t`, `eigenvalues_N3`, `eigenvalues_N6`, `eigenvalues_N9`
      - `properties`:
        - `delta_t`:
          - `type`: number
        - `t_t`:
          - `type`: number
        - `eigenvalues_N3`:
          - `type`: object
          - `required`: `Lambda0`, `Lambda1`
          - `properties`:
            - `Lambda0`:
              - `type`: number
            - `Lambda1`:
              - `type`: number
        - `eigenvalues_N6`:
          - `type`: object
          - `required`: `Lambda0`, `Lambda1`
          - `properties`:
            - `Lambda0`:
              - `type`: number
            - `Lambda1`:
              - `type`: number
        - `eigenvalues_N9`:
          - `type`: object
          - `required`: `Lambda0`, `Lambda1`
          - `properties`:
            - `Lambda0`:
              - `type`: number
            - `Lambda1`:
              - `type`: number

Notes: The checker will use the eigenvalues to recompute gap equations and derived quantities; the agent must include the raw eigenvalues for the relevant N and the computed values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "critical_line",
          "multicritical_point"
        ],
        "properties": {
          "critical_line": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "delta",
                "t_c",
                "eigenvalues_N6",
                "eigenvalues_N9",
                "c",
                "x1_0",
                "x2_0"
              ],
              "properties": {
                "delta": {
                  "type": "number"
                },
                "t_c": {
                  "type": "number"
                },
                "eigenvalues_N6": {
                  "type": "object",
                  "required": [
                    "Lambda0",
                    "Lambda1"
                  ],
                  "properties": {
                    "Lambda0": {
                      "type": "number"
                    },
                    "Lambda1": {
                      "type": "number"
                    }
                  }
                },
                "eigenvalues_N9": {
                  "type": "object",
                  "required": [
                    "Lambda0",
                    "Lambda1"
                  ],
                  "properties": {
                    "Lambda0": {
                      "type": "number"
                    },
                    "Lambda1": {
                      "type": "number"
                    }
                  }
                },
                "eigenvalues_N3": {
                  "type": "object",
                  "required": [
                    "Lambda0",
                    "Lambda1"
                  ],
                  "properties": {
                    "Lambda0": {
                      "type": "number"
                    },
                    "Lambda1": {
                      "type": "number"
                    }
                  }
                },
                "c": {
                  "type": "number"
                },
                "x1_0": {
                  "type": "number"
                },
                "x2_0": {
                  "type": "number"
                }
              }
            }
          },
          "multicritical_point": {
            "type": "object",
            "required": [
              "delta_t",
              "t_t",
              "eigenvalues_N3",
              "eigenvalues_N6",
              "eigenvalues_N9"
            ],
            "properties": {
              "delta_t": {
                "type": "number"
              },
              "t_t": {
                "type": "number"
              },
              "eigenvalues_N3": {
                "type": "object",
                "required": [
                  "Lambda0",
                  "Lambda1"
                ],
                "properties": {
                  "Lambda0": {
                    "type": "number"
                  },
                  "Lambda1": {
                    "type": "number"
                  }
                }
              },
              "eigenvalues_N6": {
                "type": "object",
                "required": [
                  "Lambda0",
                  "Lambda1"
                ],
                "properties": {
                  "Lambda0": {
                    "type": "number"
                  },
                  "Lambda1": {
                    "type": "number"
                  }
                }
              },
              "eigenvalues_N9": {
                "type": "object",
                "required": [
                  "Lambda0",
                  "Lambda1"
                ],
                "properties": {
                  "Lambda0": {
                    "type": "number"
                  },
                  "Lambda1": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Contains raw eigenvalue data and derived quantities (critical line, multicritical point, conformal anomaly, scaling dimensions). The checker will recompute mass gaps, solve crossing conditions, recompute c and scaling dimensions from the provided eigenvalues, and compare derived quantities to hidden references."
    }
  ],
  "notes": "The checker will use the eigenvalues to recompute gap equations and derived quantities; the agent must include the raw eigenvalues for the relevant N and the computed values."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json`. It extracts the raw eigenvalues, recomputes the mass gaps and the crossing conditions, recalculates the conformal anomaly c and the scaling dimensions x(1,0), x(2,0), and then compares your derived critical temperatures t_c(δ), multicritical point coordinates (δ_t, t_t), c, and x values to reference values with appropriate tolerances. Each component carries a weight, and the final score is a weighted sum of the per‑component credits. Meeting or exceeding the reference thresholds yields full points for that component; larger deviations reduce the score. Including the raw eigenvalues is necessary for verification; a submission that omits them or contains only self‑reported final numbers will not receive credit for the affected parts.
