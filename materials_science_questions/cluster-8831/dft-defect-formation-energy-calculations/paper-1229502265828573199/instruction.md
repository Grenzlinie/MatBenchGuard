# Prediction of Point Defect Concentrations and Arrhenius Parameters in Refractory Carbides using DFT and Statistical Mechanics

## Problem background
The refractory carbides TaC and HfC are ultra‑high temperature ceramics with the highest melting points among all known materials. Their processing and high‑temperature performance, including sintering and creep, are controlled by atomic diffusion, which in turn depends on the concentrations of point defects — vacancies, interstitials, antisite atoms, and their clusters. This task predicts the equilibrium populations of these defects by combining first‑principles raw defect energies with a statistical‑mechanical model. The result is a set of effective formation energies and Arrhenius prefactors that compactly describe how each defect type’s concentration depends on temperature and off‑stoichiometry.

## Approach
The reproduction implements a quasi‑chemical statistical‑mechanical model that treats point defects as an ideal gas mixture. The six elementary defects are:

- Metal vacancy V_α (vacancy on the metal sublattice)
- Carbon vacancy V_β (vacancy on the carbon sublattice)
- Antisite on carbon sublattice A_β (metal atom occupying a carbon site)
- Antisite on metal sublattice B_α (carbon atom occupying a metal site)
- Metal interstitial I_A (metal atom in a tetrahedral interstitial site)
- Carbon interstitial I_B (carbon atom in a tetrahedral interstitial site)

Several defect clusters are also considered: the divacancy V_α V_β, the antisite pair A_β B_α, the vacancy‑antisite pairs V_α B_α, V_β A_β, V_β B_α (stable only in HfC), the carbon Frenkel pair V_β I_B (stable only in HfC), and the series of vacancy clusters V_α V_β^n with n = 2,…,6. The vacancy clusters exist in different symmetric configurations (triangular T, linear L, in‑plane IP, off‑plane OP) as indicated below.

Each defect d is assigned a raw energy ε_d (obtained from DFT), a symmetry factor σ_d that counts the number of orientationally equivalent micro‑states, and L‑numbers L_{d_i}^d that give the count of each elementary defect i in the cluster. The chemical potential of defect d is μ_d = ε_d + k_B T ln(X_d / σ_d), where X_d is the centre fraction of the sublattice sites occupied by the defect centres.

The equilibrium concentrations are found by solving the following system:

1. Mass‑action equations for the independent composition‑conserving reactions among the elementary defects:
   - V_α + V_β = –AB  →  X_{V_α} X_{V_β} = exp[–(ε_{V_α} + ε_{V_β} + 2ε_0) / (k_B T)]
   - B_α + A_β = 0  →  X_{B_α} X_{A_β} = exp[–(ε_{B_α} + ε_{A_β}) / (k_B T)]
   - V_α = B_α + V_β  →  X_{V_α} / (X_{B_α} X_{V_β}) = exp[–(ε_{V_α} – ε_{B_α} – ε_{V_β}) / (k_B T)]
   - V_α + I_A = 0  →  X_{V_α} X_{I_A} = exp[–(ε_{V_α} + ε_{I_A}) / (k_B T)]
   - V_β + I_B = 0  →  X_{V_β} X_{I_B} = exp[–(ε_{V_β} + ε_{I_B}) / (k_B T)]
2. For each cluster d composed of elementary defects d_i, the dissociation‑recombination reaction gives
   X_d / (∏_i X_{d_i}) = σ_d exp[–(ε_d – Σ_i ε_{d_i}) / (k_B T)].
3. The linearised material‑balance equation that enforces the given off‑stoichiometry x (deviation from 1:1 stoichiometry):
   x = (1/4)(X_{V_β} – X_{V_α}) + (1/2)(X_{A_β} – X_{B_α}) – (1/2)ν (X_{I_B} – X_{I_A})
       + (1/4) Σ_d X_d [L_{V_β}^d – L_{V_α}^d + 2(L_{A_β}^d – L_{B_α}^d) + (L_{I_B}^d – L_{I_A}^d)],
   where ν = 8 is the number of tetrahedral interstitial positions per lattice site.

The defect concentrations at any temperature and composition can be obtained by solving the full set of equations numerically. In the two limiting cases — off‑stoichiometric metal‑rich (x > 0) where carbon vacancies dominate, and stoichiometric (x = 0) where thermal disorder is controlled by either V_α + V_β (TaC) or V_β + I_B (HfC) — simple analytical Arrhenius expressions for the effective formation energy and prefactor can be derived. The scored artifacts are the effective parameters for all defects; they may be obtained either by fitting the numerical concentrations or directly from the analytical formulas.

The required input data — raw defect energies, cohesive energy ε_0 of the perfect crystal, symmetry factors σ_d, and L‑numbers — are listed below.

### Input data

**Cohesive energy ε_0 (potential energy per atom relative to ideal gas)**

| Carbide | ε_0 (eV) |
|---------|----------|
| TaC     | –11.10   |
| HfC     | –10.53   |

**ν = 8** (tetrahedral interstitial sites per lattice site).

**Raw defect energies ε_d (eV)**

| Defect symbol            | TaC    | HfC    |
|--------------------------|--------|--------|
| V_α                      | 15.30  | 19.30  |
| V_β                      | 9.45   | 10.20  |
| A_β                      | 7.59   | 9.13   |
| B_α                      | 11.78  | 13.80  |
| I_A                      | –0.27  | –0.31  |
| I_B                      | –2.71  | –3.99  |
| V_α V_β                  | 24.61  | 27.90  |
| A_β B_α                  | 5.45   | 5.00   |
| V_α B_α                  | 22.63  | 25.86  |
| V_β A_β                  | 15.62  | 18.27  |
| V_β B_α                  | unstable | 20.46  |
| V_β I_B                  | unstable | 4.30   |
| V_α V_β^2 (T)            | 34.08  | 36.80  |
| V_α V_β^2 (L)            | 33.94  | 37.03  |
| V_α V_β^3 (IP)           | 43.60  | 46.01  |
| V_α V_β^3 (OP)           | 43.62  | 46.17  |
| V_α V_β^4 (IP)           | 53.16  | 55.39  |
| V_α V_β^4 (OP)           | 53.13  | 55.75  |
| V_α V_β^5                | 62.60  | 65.19  |
| V_α V_β^6                | 72.13  | 75.01  |

**Symmetry factors σ_d for clusters**

| Cluster | TaC σ | HfC σ |
|---------|-------|-------|
| V_α V_β                  | 6  | 6  |
| A_β B_α                  | 6  | 6  |
| V_α B_α                  | 6  | 6  |
| V_β A_β                  | 6  | 12 |
| V_β B_α                  | –  | 6  |
| V_β I_B                  | –  | 8  |
| V_α V_β^2 (T)            | 12 | 12 |
| V_α V_β^2 (L)            | 3  | 3  |
| V_α V_β^3 (IP)           | 12 | 12 |
| V_α V_β^3 (OP)           | 8  | 8  |
| V_α V_β^4 (IP)           | 3  | 3  |
| V_α V_β^4 (OP)           | 12 | 12 |
| V_α V_β^5                | 6  | 6  |
| V_α V_β^6                | 1  | 1  |

**L‑numbers (counts of elementary defects in each cluster)**

| Cluster | L_{V_α} | L_{V_β} | L_{A_β} | L_{B_α} | L_{I_A} | L_{I_B} |
|---------|---------|---------|---------|---------|---------|---------|
| V_α V_β                  | 1 | 1 | 0 | 0 | 0 | 0 |
| A_β B_α                  | 0 | 0 | 1 | 1 | 0 | 0 |
| V_α B_α                  | 1 | 0 | 0 | 1 | 0 | 0 |
| V_β A_β                  | 0 | 1 | 1 | 0 | 0 | 0 |
| V_β B_α                  | 0 | 1 | 0 | 1 | 0 | 0 |
| V_β I_B                  | 0 | 1 | 0 | 0 | 0 | 1 |
| V_α V_β^2 (T/L)          | 1 | 2 | 0 | 0 | 0 | 0 |
| V_α V_β^3 (IP/OP)        | 1 | 3 | 0 | 0 | 0 | 0 |
| V_α V_β^4 (IP/OP)        | 1 | 4 | 0 | 0 | 0 | 0 |
| V_α V_β^5                | 1 | 5 | 0 | 0 | 0 | 0 |
| V_α V_β^6                | 1 | 6 | 0 | 0 | 0 | 0 |

*Note:* The divacancy V_α V_β, the antisite pair A_β B_α, and the Frenkel‑like pairs V_β I_B, V_α I_A are composition‑conserving (do not affect the material balance). Their concentrations can be calculated directly from the formula X_d = σ_d exp[ –(ε_d + 2m ε₀)/(k_B T)], where m = 1 for divacancies, m = 0 for antisite pairs and Frenkel pairs, without solving the coupled system.

## Reproduction target
Produce a single JSON file, `/app/outputs/arrhenius_parameters.json`, that reports the effective formation energy (in eV) and Arrhenius prefactor for every stable point defect in TaC and HfC under two conditions: stoichiometric (x = 0) and metal‑rich (x = 0.02). The file structure must be:

- Top‑level keys: `TaC`, `HfC`.
- Each carbide object contains the sub‑keys `x=0` and `x=0.02`.
- For each composition, provide an object mapping from defect symbols to a parameter object with keys `prefactor` (float) and `formation_energy_eV` (float).

The defect symbols follow the naming in the tables above: `V_alpha`, `V_beta`, `A_beta`, `B_alpha`, `I_A`, `I_B`, `A_beta_B_alpha`, `V_alpha_B_alpha`, `V_beta_A_beta`, `V_beta_B_alpha`, `V_beta_I_B`, `V_alpha_V_beta`, `V_alpha_V_beta^2_T`, `V_alpha_V_beta^2_L`, `V_alpha_V_beta^3_IP`, `V_alpha_V_beta^3_OP`, `V_alpha_V_beta^4_IP`, `V_alpha_V_beta^4_OP`, `V_alpha_V_beta^5`, `V_alpha_V_beta^6`.

For defects that are unstable or do not exist for a particular carbide/composition (e.g., `V_beta_B_alpha` and `V_beta_I_B` in TaC), you may either omit the key or set its value to `null`. The prefactor and formation energy must be the values that best describe the concentration X_d in the Arrhenius form X_d = X_d^0 exp(–̅ε_d/(k_B T)) over the temperature range 2500–3500 K.

## Assets

- Python 3 with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute equilibrium defect concentrations
- Role: process
- Action: Implement the quasi‑chemical statistical‑mechanical model using the provided raw defect energies, cohesive energy, symmetry factors σ, and L‑numbers. Solve the set of mass‑action equations and the material‑balance equation to compute equilibrium defect centre‑fractions X_d as a function of temperature and off‑stoichiometry. Save the resulting concentration data to defect_concentrations.json.
- Evidence: `/app/outputs/defect_concentrations.json`

### Step 2: Effective formation energies and Arrhenius prefactors
- Role: scored (load-bearing)
- Action: From the computed defect concentrations (or via the analytical limiting‑case expressions) derive the effective formation energy ε̅_d and Arrhenius prefactor X_d^0 for each point defect type in TaC and HfC under stoichiometric (x=0) and metal‑rich (x=0.02) conditions. Write the results to arrhenius_parameters.json.
- Output file: `/app/outputs/arrhenius_parameters.json`
- Format: json
- Contract: A JSON object with keys 'TaC' and 'HfC'. Each carbide object contains keys 'x=0' and 'x=0.02'. For each composition, an object mapping defect symbol (e.g., 'V_alpha', 'V_beta', 'A_beta', 'B_alpha', 'I_A', 'I_B', 'A_beta_B_alpha', 'V_alpha_B_alpha', 'V_beta_A_beta', 'V_beta_B_alpha', 'V_beta_I_B', 'V_alpha_V_beta', 'V_alpha_V_beta^2_T', 'V_alpha_V_beta^2_L', 'V_alpha_V_beta^3_IP', 'V_alpha_V_beta^3_OP', 'V_alpha_V_beta^4_IP', 'V_alpha_V_beta^4_OP', 'V_alpha_V_beta^5', 'V_alpha_V_beta^6') to an object with keys 'prefactor' (float) and 'formation_energy_eV' (float). Defects that are unstable or not applicable for a particular carbide/composition may be omitted or set to null.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/arrhenius_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### arrhenius_parameters.json
- path: `/app/outputs/arrhenius_parameters.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored artifact: effective formation energies and Arrhenius prefactors for all point defect types in TaC and HfC under stoichiometric and metal-rich compositions, corresponding to Table 7 of the source paper.
- schema:
  - `type`: object
  - `required`: `TaC`, `HfC`
  - `properties`:
    - `TaC`:
      - `type`: object
      - `required`: `x=0`, `x=0.02`
      - `properties`:
        - `x=0`:
          - `type`: object
          - `additionalProperties`:
            - `type`: object
            - `properties`:
              - `prefactor`:
                - `type`: number
              - `formation_energy_eV`:
                - `type`: number
        - `x=0.02`:
          - `type`: object
          - `additionalProperties`:
            - `type`: object
            - `properties`:
              - `prefactor`:
                - `type`: number
              - `formation_energy_eV`:
                - `type`: number
    - `HfC`:
      - `type`: object
      - `required`: `x=0`, `x=0.02`
      - `properties`:
        - `x=0`:
          - `type`: object
          - `additionalProperties`:
            - `type`: object
            - `properties`:
              - `prefactor`:
                - `type`: number
              - `formation_energy_eV`:
                - `type`: number
        - `x=0.02`:
          - `type`: object
          - `additionalProperties`:
            - `type`: object
            - `properties`:
              - `prefactor`:
                - `type`: number
              - `formation_energy_eV`:
                - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "arrhenius_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "TaC",
          "HfC"
        ],
        "properties": {
          "TaC": {
            "type": "object",
            "required": [
              "x=0",
              "x=0.02"
            ],
            "properties": {
              "x=0": {
                "type": "object",
                "additionalProperties": {
                  "type": "object",
                  "properties": {
                    "prefactor": {
                      "type": "number"
                    },
                    "formation_energy_eV": {
                      "type": "number"
                    }
                  }
                }
              },
              "x=0.02": {
                "type": "object",
                "additionalProperties": {
                  "type": "object",
                  "properties": {
                    "prefactor": {
                      "type": "number"
                    },
                    "formation_energy_eV": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "HfC": {
            "type": "object",
            "required": [
              "x=0",
              "x=0.02"
            ],
            "properties": {
              "x=0": {
                "type": "object",
                "additionalProperties": {
                  "type": "object",
                  "properties": {
                    "prefactor": {
                      "type": "number"
                    },
                    "formation_energy_eV": {
                      "type": "number"
                    }
                  }
                }
              },
              "x=0.02": {
                "type": "object",
                "additionalProperties": {
                  "type": "object",
                  "properties": {
                    "prefactor": {
                      "type": "number"
                    },
                    "formation_energy_eV": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "Scored artifact: effective formation energies and Arrhenius prefactors for all point defect types in TaC and HfC under stoichiometric and metal-rich compositions, corresponding to Table 7 of the source paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your solution is evaluated by a hidden verifier. The verifier reads `/app/outputs/arrhenius_parameters.json` and compares each reported prefactor and formation energy to reference values that correspond to the paper’s published results. The comparison uses a tolerance band: each parameter must lie within an acceptable range around the reference. Parameters that fall within the tolerance earn full credit; those outside receive proportionally less. Only the final output file is scored, but it must be produced by genuinely executing the statistical‑mechanical model as described in the workflow steps. The reward is a single number between 0 and 1 that reflects the fraction of parameters that satisfy the tolerance.
