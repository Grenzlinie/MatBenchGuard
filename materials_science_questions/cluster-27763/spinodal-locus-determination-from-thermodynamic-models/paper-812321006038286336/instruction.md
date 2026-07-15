# Phase Behavior and Spinodal Stability of Oppositely Charged Polyelectrolyte Complexes with Ion Pairing

## Problem background
Complexation in symmetric mixtures of oppositely charged polyelectrolytes is governed by three competing physical mechanisms: long-range electrostatic charge fluctuations, short-range thermoreversible ion pairing (cross-linking), and non‑specific van der Waals interactions between monomer backbones. Understanding how these mechanisms set the polymer density inside the precipitated complex and control its dissolution upon salt addition is critical for designing polymeric carriers, coatings, and flocculants. This reproduction task asks you to compute, from a self‑consistent theoretical model, the equilibrium properties of such polyelectrolyte complexes — specifically the polymer volume fraction in the precipitate, the fraction of cross‑linked monomers, and the stability boundaries — and to determine how those properties respond to salt concentration and to the strengths of ion binding and backbone hydrophobicity.

## Approach
You will implement a free‑energy model for a symmetric polyelectrolyte solution. The model consists of a Flory–Huggins reference free energy that includes ideal mixing of chains, salt ions, and cross‑links, plus a hard‑core repulsion term and a van der Waals interaction controlled by the Flory–Huggins parameter χ. Long‑range electrostatics are treated at the random phase approximation (RPA) level using a modified Coulomb potential that incorporates the finite size of the ions. The RPA correlators account for the structure of thermoreversibly cross‑linked chains through an interpolation form that correctly respects the Gaussian chain statistics and the point‑ion limit at large wave vectors.

The fraction of monomers forming ionic pairs (conversion, denoted Γ) is not a free parameter but is determined self‑consistently: you must solve the modified law of mass action together with the electrostatic chemical potential contribution that arises from the RPA free energy. Once the self‑consistent free energy density is obtained, phase coexistence in the limit of infinite chain length N is found by balancing the pressure and the salt chemical potential between the polymer‑precipitate phase and a salt‑only supernatant phase. Finally, for a finite chain length you will compute a spinodal point by solving the determinant condition corresponding to the stability limit of the homogeneous solution.

## Reproduction target
Your task is to write a Python implementation of the model and use it to produce a structured JSON file (`/app/outputs/results.json`) that contains the following quantities:

1. For N = ∞, Bjerrum length l = 3, charge fraction f = 0.1, monomer size b = 1, and no van der Waals attraction (χ = 0):
   - at each salt volume fraction φ_s ∈ {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3} and for binding energies ε = 0, 3, 5, 7, report the polymer volume fraction in the precipitate φ, the conversion Γ, the salt volume fraction difference between precipitate and supernatant, and the electrostatic binding energy μ_RPA.

2. For ε = 0 and the same l, f, b, N = ∞:
   - at each φ_s as above, compute φ for χ = 0, 0.4, 0.5, 0.6 to examine the effect of backbone hydrophobicity.

3. In the salt‑free case (φ_s = 0):
   - for ε = 0, 1, …, 10 and for each of the four χ values, compute the precipitate polymer volume fraction φ.

4. For a finite chain N = 200, with ε = 5, χ = 0.5, at φ_s = 0.1:
   - determine the polymer volume fraction at the spinodal point (the solution of J(φ, φ_s) = 0).

All results must be written in the JSON structure specified in the Workflow steps and Output contract sections. Include every required key and array length; the verifier will parse this file automatically.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Free Energy Module and Self‑Consistent Solver
- Role: process
- Action: Implement the free energy model: Flory–Huggins reference (Eq. 6), RPA electrostatic free energy (Eq. 24) including the modified Coulomb potential (Eq. 23) and the interpolation form for g(q) (Eq. 25). Write a solver that, for given (φ, φ_s, N, f, l, ε, χ), solves the modified law of mass action (Eq. 28) together with the electrostatic chemical potential (Eq. 30) self-consistently to obtain equilibrium conversion Γ and total free energy density ℱ(φ,φ_s). Support both N→∞ (polymer entropy term zero) and finite N.
- Evidence: `/app/outputs/free_energy_module.py`

### Step 2: Compute Phase Coexistence and Spinodal Results
- Role: scored (load-bearing)
- Action: Using the free energy module, compute the following and write the aggregated results to /app/outputs/results.json:
- For N=∞, l=3, f=0.1, b=1, χ=0: compute polymer volume fraction in precipitate φ, conversion Γ, salt volume fraction difference φ_s^(p)−φ_s, and electrostatic binding energy μ_RPA for salt volume fractions φ_s = 0,0.05,0.1,0.15,0.2,0.25,0.3 at ε = 0,3,5,7.
- For ε=0: compute φ vs φ_s for the same grid at χ = 0,0.4,0.5,0.6.
- For salt-free (φ_s=0) and χ = 0,0.4,0.5,0.6: compute φ for ε from 0 to 10 in steps of 1.
- For N=200, ε=5, χ=0.5, φ_s=0.1: determine the spinodal polymer volume fraction φ by solving the spinodal determinant condition J(φ,φ_s)=0 (Eq. 37).
Structure results.json with top-level keys as described in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys for each parameter set. For ε=0,3,5,7: 'fig1_epsilon_{e}' → { 'phi_s': [0.0,0.05,...], 'phi': [...], 'Gamma': [...], 'phi_s_diff': [...], 'mu_RPA': [...] }. For χ scans: 'fig2_chi_{chi}' → { 'phi_s': [...], 'phi': [...] }. 'fig3' → { 'epsilon': [0,1,...,10], 'phi_chi_0': [...], 'phi_chi_0.4': [...], 'phi_chi_0.5': [...], 'phi_chi_0.6': [...] }. 'fig5_spinodal' → { 'phi': float, 'phi_s': 0.1, 'N': 200, 'epsilon': 5, 'chi': 0.5 }. All numeric values as standard JSON floats.
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
- target_policy: exact_match
- description: Aggregated quantitative results from the phase coexistence and spinodal calculations. The checker compares selected numeric values and trends to hidden gold digitized from the paper's figures using absolute tolerances.
- schema:
  - `type`: object
  - `required`: `fig1_epsilon_0`, `fig1_epsilon_3`, `fig1_epsilon_5`, `fig1_epsilon_7`, `fig2_chi_0`, `fig2_chi_0.4`, `fig2_chi_0.5`, `fig2_chi_0.6`, `fig3`, `fig5_spinodal`
  - `properties`:
    - `fig1_epsilon_0`:
      - `type`: object
      - `required`: `phi_s`, `phi`, `Gamma`, `phi_s_diff`, `mu_RPA`
      - `properties`:
        - `phi_s`:
          - `type`: array
          - `items`:
            - `type`: number
        - `phi`:
          - `type`: array
          - `items`:
            - `type`: number
        - `Gamma`:
          - `type`: array
          - `items`:
            - `type`: number
        - `phi_s_diff`:
          - `type`: array
          - `items`:
            - `type`: number
        - `mu_RPA`:
          - `type`: array
          - `items`:
            - `type`: number
    - `fig1_epsilon_3`:
      - `$ref`: #/properties/fig1_epsilon_0
    - `fig1_epsilon_5`:
      - `$ref`: #/properties/fig1_epsilon_0
    - `fig1_epsilon_7`:
      - `$ref`: #/properties/fig1_epsilon_0
    - `fig2_chi_0`:
      - `type`: object
      - `required`: `phi_s`, `phi`
      - `properties`:
        - `phi_s`:
          - `type`: array
          - `items`:
            - `type`: number
        - `phi`:
          - `type`: array
          - `items`:
            - `type`: number
    - `fig2_chi_0.4`:
      - `$ref`: #/properties/fig2_chi_0
    - `fig2_chi_0.5`:
      - `$ref`: #/properties/fig2_chi_0
    - `fig2_chi_0.6`:
      - `$ref`: #/properties/fig2_chi_0
    - `fig3`:
      - `type`: object
      - `required`: `epsilon`, `phi_chi_0`, `phi_chi_0.4`, `phi_chi_0.5`, `phi_chi_0.6`
      - `properties`:
        - `epsilon`:
          - `type`: array
          - `items`:
            - `type`: number
        - `phi_chi_0`:
          - `type`: array
          - `items`:
            - `type`: number
        - `phi_chi_0.4`:
          - `type`: array
          - `items`:
            - `type`: number
        - `phi_chi_0.5`:
          - `type`: array
          - `items`:
            - `type`: number
        - `phi_chi_0.6`:
          - `type`: array
          - `items`:
            - `type`: number
    - `fig5_spinodal`:
      - `type`: object
      - `required`: `phi`, `phi_s`, `N`, `epsilon`, `chi`
      - `properties`:
        - `phi`:
          - `type`: number
        - `phi_s`:
          - `type`: number
        - `N`:
          - `type`: number
        - `epsilon`:
          - `type`: number
        - `chi`:
          - `type`: number

Notes: The output contract declares the exact structure of results.json. The hidden checker verifies shape, required keys, array lengths, and numeric values against paper‑reported references within tolerances that absorb legitimate implementation differences. Trends (e.g., monotonicity) are also checked as part of structural validation.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "fig1_epsilon_0",
          "fig1_epsilon_3",
          "fig1_epsilon_5",
          "fig1_epsilon_7",
          "fig2_chi_0",
          "fig2_chi_0.4",
          "fig2_chi_0.5",
          "fig2_chi_0.6",
          "fig3",
          "fig5_spinodal"
        ],
        "properties": {
          "fig1_epsilon_0": {
            "type": "object",
            "required": [
              "phi_s",
              "phi",
              "Gamma",
              "phi_s_diff",
              "mu_RPA"
            ],
            "properties": {
              "phi_s": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "phi": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "Gamma": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "phi_s_diff": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "mu_RPA": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "fig1_epsilon_3": {
            "$ref": "#/properties/fig1_epsilon_0"
          },
          "fig1_epsilon_5": {
            "$ref": "#/properties/fig1_epsilon_0"
          },
          "fig1_epsilon_7": {
            "$ref": "#/properties/fig1_epsilon_0"
          },
          "fig2_chi_0": {
            "type": "object",
            "required": [
              "phi_s",
              "phi"
            ],
            "properties": {
              "phi_s": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "phi": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "fig2_chi_0.4": {
            "$ref": "#/properties/fig2_chi_0"
          },
          "fig2_chi_0.5": {
            "$ref": "#/properties/fig2_chi_0"
          },
          "fig2_chi_0.6": {
            "$ref": "#/properties/fig2_chi_0"
          },
          "fig3": {
            "type": "object",
            "required": [
              "epsilon",
              "phi_chi_0",
              "phi_chi_0.4",
              "phi_chi_0.5",
              "phi_chi_0.6"
            ],
            "properties": {
              "epsilon": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "phi_chi_0": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "phi_chi_0.4": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "phi_chi_0.5": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "phi_chi_0.6": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "fig5_spinodal": {
            "type": "object",
            "required": [
              "phi",
              "phi_s",
              "N",
              "epsilon",
              "chi"
            ],
            "properties": {
              "phi": {
                "type": "number"
              },
              "phi_s": {
                "type": "number"
              },
              "N": {
                "type": "number"
              },
              "epsilon": {
                "type": "number"
              },
              "chi": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Aggregated quantitative results from the phase coexistence and spinodal calculations. The checker compares selected numeric values and trends to hidden gold digitized from the paper's figures using absolute tolerances."
    }
  ],
  "notes": "The output contract declares the exact structure of results.json. The hidden checker verifies shape, required keys, array lengths, and numeric values against paper‑reported references within tolerances that absorb legitimate implementation differences. Trends (e.g., monotonicity) are also checked as part of structural validation."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/results.json` and compares your computed values for the polymer volume fraction, conversion, salt volume‑fraction difference, electrostatic binding energy, and the spinodal polymer volume fraction against reference values extracted from the original study. Comparisons use absolute tolerances that are large enough to absorb legitimate numerical differences that arise from independently re‑implementing the model (different integration routines, root‑finding algorithms, or discretizations), but tight enough that only a faithful computation of the full self‑consistent model can pass. The verifier distributes credit across all required conditions and aggregates it into a final score between 0 and 1. Simply reporting a number without running the correct model will not satisfy the checks.
