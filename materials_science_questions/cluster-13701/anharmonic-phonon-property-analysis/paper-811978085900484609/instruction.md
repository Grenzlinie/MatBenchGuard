# Variational Treatment of Anharmonic Libration in Molecular Crystals

## Problem background
Molecular crystals of linear molecules (N2, CO, N2O, CO2) form orientationally ordered structures at low temperatures, where the molecular axes align along specific directions. The librational motions about the equilibrium orientations are anharmonic, especially near the phase transition, and this anharmonicity strongly affects thermodynamic properties such as the order parameter, the libron excitation energy, and the heat capacity. A self-consistent variational approach based on the Bogolyubov inequality can capture these effects in the molecular-field approximation. The goal is to compute, for each crystal, the temperature dependence of the order parameter η, the libron energy Δ, the librational contribution to the heat capacity C_v/R, and the orientational disordering temperature T_λ in the rigid-lattice approximation.

## Physical model and equations
The variational treatment of anharmonic libration uses the following self-consistent equations (temperatures in K, energies in K; Boltzmann constant k_B = 1).
**Variables**: γ (dimensionless), Δ (K), and ⟨ϱ²⟩₀ = γ coth(βΔ/2) with β = 1/T.
The molecular-field constant U (in K) depends on the intermolecular potential and will be determined self-consistently via the calibration step; for the ordered phase at a given temperature it is taken as constant (the 0 K value).
The equations to satisfy are:

 (I)  θ_rot [ –1/γ² + ⅛ coth²(βΔ/2) ] – U η (∂η/∂⟨ϱ²⟩₀) = 0
 (II) θ_rot [ 2/γ + coth(βΔ/2) + (γ/4) coth²(βΔ/2) ] = Δ
 (III) ⟨ϱ²⟩₀ = γ coth(βΔ/2)
 (IV) η = 1 – 6 ∫₀^∞ ds (1–s) e^{–s} / (1 + (s/4) ⟨ϱ²⟩₀)

The derivative ∂η/∂⟨ϱ²⟩₀ = –6 ∫₀^∞ ds (1–s) e^{–s} * ( –s/4 ) / (1 + (s/4) ⟨ϱ²⟩₀)² can be evaluated numerically or expressed in closed form; for the calibration at T=0 the following expansion is used (valid at low temperature):
 (V) η = 1 – (3/2)γ + (3/2)γ² – (27/16)γ³ + O(γ⁴).
At T = 0 the equations reduce to:
 (VI)  1/γ² – 1/8 = α² (1 – (7/2)γ + (63/8)γ² – (63/4)γ³),
 (VII) Δ₀ = θ_rot (1 + 2/γ + γ/4),
where α = √(3U₀/(2 θ_rot)) and Δ₀ is the experimental low‑temperature libron energy.

The ordered‑phase free energy per molecule (Eq. 10) is
 F_order/N = 2T ln(2 sinh(βΔ/2)) + θ_rot[ (1/γ) coth(βΔ/2) + 1/(2 sinh²(βΔ/2)) + (γ/8) coth³(βΔ/2) ] – (U/2) η² – Δ coth(βΔ/2).

The disordered phase is treated as a system of classical free rotators, whose free energy per molecule is
 F_disorder/N = –T ln(T / θ_rot).

The orientational disordering temperature T_λ (rigid‑lattice) is found by solving
 F_order(T_λ) = F_disorder(T_λ).

The libron contribution to the heat capacity (Eq. 16) is
 C_v / R = ½ (βΔ)² / sinh²(βΔ/2) × [ 1 + (β/Δ) (dΔ/dβ) ],
where dΔ/dβ = –T² (dΔ/dT) is obtained by finite differences of the Δ(T) curve.

**Molecular-field constant U₀** (K) is given by the sum of quadrupole, dispersion and valence‑force contributions:
 U₀ = –21.47 Q² R₀⁻⁵ + 46 k² ε σ⁶ R₀⁻⁶ – (51037 – 7168 ξ) B d⁴ R₀⁻¹⁶,
with ξ = 1 for N₂, CO and ξ = 3/2 for N₂O, CO₂.  
The repulsive constant B (in 10⁻⁸ erg Å¹²) is determined in the calibration step (see Procedure).  
Conversion from erg to K: 1 erg = 7.2429717 × 10¹⁵ K.

**Molecular parameters** (input data)

| Parameter   | Symbol | N₂        | CO        | N₂O       | CO₂       |
|-------------|--------|-----------|-----------|-----------|-----------|
| rotational constant (K) | θ_rot | 2.877 | 2.734 | 0.603 | 0.566 |
| quadrupole moment (10⁻²⁶ e.s.u.) | Q | 1.29 | 1.62 | 3.0 | 4.3 |
| LJ well depth (10⁻¹⁴ erg) | ε | 1.313 | 1.382 | 3.251 | 2.623 |
| LJ size parameter (Å) | σ | 3.708 | 3.769 | 3.802 | 3.996 |
| nuclear half‑separation (Å) | d | 0.549 | 0.564 | 1.156 | 1.160 |
| anisotropy factor | k | 0.189 | 0.168 | 0.310 | 0.257 |
| nearest‑neighbour distance at 0 K (Å) | R₀ | 3.994 | 3.986 | 3.969 | 3.929 |
| low‑T libron energy Δ₀ (K) | Δ₀ | 76.0 | 100.0 | 153.0 | 163.0 |

(Note: The nuclear separation 2d in the original table is given; above d is half of that.)

**Temperature grids for output** (from Table 4)

- N₂  : 0, 10, 15, 20, 25, 30, 35 K
- CO  : 0, 20, 30, 35, 40, 45, 50, 60 K
- N₂O : 0, 50, 75, 100, 120, 140, 160, 180 K
- CO₂ : 0, 50, 75, 100, 120, 140, 160, 180, 200, 215 K

**Procedure overview**
1. **Calibration** (process step): using Δ₀ and the T=0 equations (VI),(VII), solve for α and γ.  
   From α compute U₀ = (2/3) α² θ_rot.  
   Using the expression for U₀ and the known molecular parameters, solve for B.
2. **Temperature‑dependent computation** (scored step): for each crystal and each specified T, solve the system (I)–(IV) for γ, Δ, η (U = U₀ determined above).  
   Compute C_v/R using the Δ(T) curve and the formula above.  
   Find T_λ by root‑finding on F_order(T)–F_disorder(T)=0.
Store all results in `results.json` following the contract.

## Reproduction target
For each of the four crystals (N2, CO, N2O, CO2), compute and write to `results.json` arrays of the order parameter η, the libron energy Δ (in K), and the dimensionless librational heat capacity C_v/R at the temperatures specified in the workflow step. Additionally, compute the rigid-lattice orientational disordering temperature T_λ (in K) for each crystal by equating the free energies of the ordered and disordered phases. All computed quantities must be stored following the exact structure defined in the output contract.

## Assets

- Python environment with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Calibrate repulsive constant B and molecular-field constant U0
- Role: process
- Action: Using the molecular parameters and Δ0 from the table in the Approach section, solve the T=0 equations (VI) and (VII) together with expansion (V) to obtain α and γ. Compute U0 = (2/3) α² θ_rot, then determine B from the U0 expression given in the Approach using the known molecular parameters. Produce the dimensionless parameter α.
- Evidence: `/app/outputs/calibration.json`

### Step 2: Compute temperature-dependent properties and disordering temperature
- Role: scored (load-bearing)
- Action: For each crystal, solve the self-consistent equations (I)-(IV) at each temperature listed in the Approach section to obtain η(T) and Δ(T). Compute C_v/R(T) using the libron heat capacity formula. Find T_λ by solving F_order(T)=F_disorder(T) using the free energy expressions given in the Approach.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "N2": {
    "T": [float],
    "eta": [float],
    "delta": [float],
    "C_v_R": [float],
    "T_lambda": float
  },
  "CO": { ... },
  "N2O": { ... },
  "CO2": { ... }
}
Units: T in K, delta in K, C_v_R dimensionless, T_lambda in K.
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
- target_policy: reference_match
- description: Temperature-dependent order parameter η, libron energy Δ, librational heat capacity C_v/R, and rigid-lattice orientational disordering temperature T_lambda for N2, CO, N2O, and CO2 crystals.
- schema:
  - `type`: object
  - `properties`:
    - `N2`:
      - `type`: object
      - `required`: `T`, `eta`, `delta`, `C_v_R`, `T_lambda`
      - `properties`:
        - `T`:
          - `type`: array
          - `items`:
            - `type`: number
        - `eta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `delta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `C_v_R`:
          - `type`: array
          - `items`:
            - `type`: number
        - `T_lambda`:
          - `type`: number
    - `CO`:
      - `type`: object
      - `required`: `T`, `eta`, `delta`, `C_v_R`, `T_lambda`
      - `properties`:
        - `T`:
          - `type`: array
          - `items`:
            - `type`: number
        - `eta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `delta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `C_v_R`:
          - `type`: array
          - `items`:
            - `type`: number
        - `T_lambda`:
          - `type`: number
    - `N2O`:
      - `type`: object
      - `required`: `T`, `eta`, `delta`, `C_v_R`, `T_lambda`
      - `properties`:
        - `T`:
          - `type`: array
          - `items`:
            - `type`: number
        - `eta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `delta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `C_v_R`:
          - `type`: array
          - `items`:
            - `type`: number
        - `T_lambda`:
          - `type`: number
    - `CO2`:
      - `type`: object
      - `required`: `T`, `eta`, `delta`, `C_v_R`, `T_lambda`
      - `properties`:
        - `T`:
          - `type`: array
          - `items`:
            - `type`: number
        - `eta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `delta`:
          - `type`: array
          - `items`:
            - `type`: number
        - `C_v_R`:
          - `type`: array
          - `items`:
            - `type`: number
        - `T_lambda`:
          - `type`: number
  - `required`: `N2`, `CO`, `N2O`, `CO2`

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "N2": {
            "type": "object",
            "required": [
              "T",
              "eta",
              "delta",
              "C_v_R",
              "T_lambda"
            ],
            "properties": {
              "T": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "eta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "delta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "C_v_R": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "T_lambda": {
                "type": "number"
              }
            }
          },
          "CO": {
            "type": "object",
            "required": [
              "T",
              "eta",
              "delta",
              "C_v_R",
              "T_lambda"
            ],
            "properties": {
              "T": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "eta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "delta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "C_v_R": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "T_lambda": {
                "type": "number"
              }
            }
          },
          "N2O": {
            "type": "object",
            "required": [
              "T",
              "eta",
              "delta",
              "C_v_R",
              "T_lambda"
            ],
            "properties": {
              "T": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "eta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "delta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "C_v_R": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "T_lambda": {
                "type": "number"
              }
            }
          },
          "CO2": {
            "type": "object",
            "required": [
              "T",
              "eta",
              "delta",
              "C_v_R",
              "T_lambda"
            ],
            "properties": {
              "T": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "eta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "delta": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "C_v_R": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "T_lambda": {
                "type": "number"
              }
            }
          }
        },
        "required": [
          "N2",
          "CO",
          "N2O",
          "CO2"
        ]
      },
      "description": "Temperature-dependent order parameter η, libron energy Δ, librational heat capacity C_v/R, and rigid-lattice orientational disordering temperature T_lambda for N2, CO, N2O, and CO2 crystals."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently inspects each scored artifact. For `results.json`, the verifier compares every numeric entry (η, Δ, C_v/R, T_λ) against reference values derived from independent implementation of the same physical model, using tolerances that account for legitimate numerical differences. Full credit is awarded when all entries fall within the tolerant thresholds; partial credit is proportional to the fraction of correct entries. Simply reporting numbers without performing the full computational pipeline will not pass, because the verifier checks structural consistency and the values themselves. The final reward is a float between 0.0 and 1.0.
