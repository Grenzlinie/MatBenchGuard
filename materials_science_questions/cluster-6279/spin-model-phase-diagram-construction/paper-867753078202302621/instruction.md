# Exact diagonalization and finite-size scaling of mixed-spin chain for KT universality

## Problem background
The spin-(1,1/2) Heisenberg ferrimagnetic chain in a magnetic field exhibits a magnetization plateau at one-third of the full magnetization (m=1/2). The stability of this plateau under exchange anisotropy α (where the z-coupling strength is scaled relative to the XY coupling) and bond alternation δ (the relative strength of inter-cell coupling) is an open problem. Using exact diagonalization of finite chains and finite-size scaling, the critical behavior of the plateau-to-gapless-spin-fluid transition can be characterized by the central charge c and the critical exponent η, and the phase boundary α_c can be located.

## Approach
Implement the mixed-spin chain Hamiltonian with anisotropic exchange and bond alternation without the Zeeman term, using periodic boundary conditions. Perform exact diagonalization for finite chains of N unit cells (N=6,8,10,12) in sectors of fixed total magnetization M = N/2 (plateau) and N/2±1. Compute the lowest energy E(N,M) in each sector. Derive the finite-size critical field bounds: H_+(N)=E(N,M+1)−E(N,M) and H_−(N)=E(N,M)−E(N,M−1). Extract the sound velocity v_s from the low-energy excitation dispersion (e.g., the lowest excitation energy as a function of momentum). For each (δ,α), the raw finite-size data are used to obtain the central charge c from the ground-state energy per site scaling E(N,M)/N ≈ ε − π c v_s / N² and the critical exponent η from the plateau width Δ_N = H_+ − H_- ≈ 2π v_s η / N, via linear regression in 1/N² and 1/N, respectively. The transition point α_c is the anisotropy where η reaches 1/4, the value expected at a Kosterlitz–Thouless transition.

## Reproduction target
For bond alternation δ=1.0 and δ=0.6, produce a JSON file containing the raw finite-size data (energies, field bounds, sound velocity) for the following exchange anisotropy values: α = -1.0, -0.8, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0. The hidden verifier will recompute c, η, and α_c from this data.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Exact diagonalization and finite-size data collection
- Role: scored (load-bearing)
- Action: Implement the spin-1/2 mixed-spin chain Hamiltonian without the Zeeman term. The Hamiltonian for N unit cells consists of on-site anisotropic exchange (S_j·s_j)_α = S^x s^x + S^y s^y + α S^z s^z and inter-cell coupling with bond alternation δ: δ (s_j·S_{j+1})_α. Use periodic boundary conditions. For bond alternation parameters δ = 1.0 and δ = 0.6, select a range of exchange anisotropy α values covering the Kosterlitz–Thouless transition region (the exact list will be provided in the instruction). For each (δ,α) and system sizes N = 6, 8, 10, 12, compute the lowest energy E(N,M) in the magnetization sectors M = N/2 (the plateau magnetization) and M = N/2 ± 1 using exact diagonalization with total magnetization conservation. From these derive the finite-size critical field bounds: H_+(N) = E(N, M+1) − E(N, M) and H_−(N) = E(N, M) − E(N, M−1). Compute the sound velocity v_s from the low-energy excitation dispersion (e.g., the lowest excitation energy as a function of momentum). Collect all results into a single JSON file.
- Output file: `/app/outputs/reproduction_data.json`
- Format: json
- Contract: A JSON object with keys 'delta_1.0' and 'delta_0.6'. Each maps to a list of objects, one per sampled α. Each object has fields: 'alpha' (float), 'vs' (float), 'energies' (list of objects with fields N (int), M (int), E (float)), and 'H_plus_minus' (list of objects with fields N (int), H_plus (float), H_minus (float)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_data.json
- path: `/app/outputs/reproduction_data.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Finite-size data from exact diagonalization of the spin-(1,1/2) chain. The hidden checker recomputes the central charge c, critical exponent η, and Kosterlitz–Thouless phase boundary α_c from this data using the scaling formulas.
- schema:
  - `type`: object
  - `required`: `delta_1.0`, `delta_0.6`
  - `properties`:
    - `delta_1.0`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `alpha`, `vs`, `energies`, `H_plus_minus`
        - `properties`:
          - `alpha`:
            - `type`: number
          - `vs`:
            - `type`: number
          - `energies`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `N`, `M`, `E`
              - `properties`:
                - `N`:
                  - `type`: integer
                - `M`:
                  - `type`: integer
                - `E`:
                  - `type`: number
          - `H_plus_minus`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `N`, `H_plus`, `H_minus`
              - `properties`:
                - `N`:
                  - `type`: integer
                - `H_plus`:
                  - `type`: number
                - `H_minus`:
                  - `type`: number
    - `delta_0.6`:
      - `$ref`: #/properties/delta_1.0

Notes: The checker performs linear regressions on the finite-size data to extract c and η, then interpolates η to 1/4 to find α_c. Only the raw data is required here; the derived quantities are verified by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "delta_1.0",
          "delta_0.6"
        ],
        "properties": {
          "delta_1.0": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "alpha",
                "vs",
                "energies",
                "H_plus_minus"
              ],
              "properties": {
                "alpha": {
                  "type": "number"
                },
                "vs": {
                  "type": "number"
                },
                "energies": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "N",
                      "M",
                      "E"
                    ],
                    "properties": {
                      "N": {
                        "type": "integer"
                      },
                      "M": {
                        "type": "integer"
                      },
                      "E": {
                        "type": "number"
                      }
                    }
                  }
                },
                "H_plus_minus": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "N",
                      "H_plus",
                      "H_minus"
                    ],
                    "properties": {
                      "N": {
                        "type": "integer"
                      },
                      "H_plus": {
                        "type": "number"
                      },
                      "H_minus": {
                        "type": "number"
                      }
                    }
                  }
                }
              }
            }
          },
          "delta_0.6": {
            "$ref": "#/properties/delta_1.0"
          }
        }
      },
      "description": "Finite-size data from exact diagonalization of the spin-(1,1/2) chain. The hidden checker recomputes the central charge c, critical exponent η, and Kosterlitz–Thouless phase boundary α_c from this data using the scaling formulas."
    }
  ],
  "notes": "The checker performs linear regressions on the finite-size data to extract c and η, then interpolates η to 1/4 to find α_c. Only the raw data is required here; the derived quantities are verified by the checker."
}
```

## How you are scored
Your submission, reproduction_data.json, is evaluated by a hidden verifier that independently recomputes the central charge c and critical exponent η from the raw finite-size data using linear regressions as described. It then determines the critical anisotropy α_c where η reaches 1/4. The recomputed quantities are compared to hidden reference values, and the final reward is a weighted combination of the absolute deviations for c, η, and α_c. Full credit is awarded when deviations fall within acceptable tolerances. Reporting the paper's numbers without genuine data is insufficient.
