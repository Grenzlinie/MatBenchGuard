# Superconducting Properties from Electron-Phonon Coupling via Eliashberg Equations and Vertex Corrections

## Problem background
Recent experiments have discovered phonon-mediated superconductivity in hydrogen-rich compounds compressed to hundreds of gigapascals, with critical temperatures reaching 178 K for H3S and 81 K for PH3 at 200 GPa. In these strong-coupling systems, the standard Migdal approximation may need refinement, as nonadiabatic effects could alter the electron‑phonon interaction. This task investigates the role of lowest‑order vertex corrections in the Eliashberg description of the superconducting state of cubic Im‾3m H3S and monoclinic C2/m PH3 at 200 GPa. The goal is to quantify how the vertex corrections affect the Coulomb pseudopotential that reproduces the experimental critical temperature, the superconducting energy gap, the electron effective mass, and thermodynamic ratios, thereby testing the validity of the conventional Migdal–Eliashberg theory in these materials.

## Approach
We first perform density‑functional perturbation theory (DFPT) calculations on the given crystal structures using the Quantum ESPRESSO package with Vanderbilt ultrasoft pseudopotentials. This yields the phonon dispersions, the Eliashberg spectral function α²F(ω), and the electron‑phonon coupling constant λ, the maximum phonon energy ω_D, the Fermi energy ε_F, and the logarithmic phonon frequency ω_log. Using this spectrum, we solve the Eliashberg equations on the imaginary axis at 1100 Matsubara frequencies for both the conventional (Migdal) form and the form that includes the lowest‑order vertex correction. The experimental critical temperatures are fixed inputs (178 K for H3S, 81 K for PH3). From the solutions we determine the critical Coulomb pseudopotential µ* (the value that yields vanishing order parameter at Tc). By analytic continuation we obtain the real‑axis superconducting energy gap Δ(T), from which we extract the zero‑temperature gap Δ(0) and the dimensionless ratio 2Δ(0)/Tc, as well as the electron effective mass at Tc. The condensation energy is computed to derive the specific‑heat difference and thermodynamic critical field, yielding the dimensionless ratios RC ≡ ΔC(Tc)/C^N(Tc) and RH ≡ Tc C^N(Tc)/Hc²(0). The entire analysis is performed for both H3S and PH3, and for both the conventional and the vertex‑corrected Eliashberg formalisms.

## Reproduction target
For H3S (critical temperature 178 K) and PH3 (critical temperature 81 K) at 200 GPa, compute using the DFPT + Eliashberg workflow the following quantities and write them to the output file `eliashberg_results.json`:
- the critical Coulomb pseudopotential µ* (conventional and vertex‑corrected)
- the zero‑temperature superconducting energy gap Δ(0) in meV
- the dimensionless ratio 2Δ(0)/Tc
- the electron effective mass ratio m_e*/m_e
- the thermodynamic ratios RC and RH
All values must be reported for each compound and for both the conventional and vertex‑corrected Eliashberg equations, structured as described in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Vanderbilt ultrasoft pseudopotentials for S, P, H: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure data for H3S and PH3

## Workflow steps

### Step 1: DFPT calculations for H3S and PH3
- Role: process
- Action: Perform density-functional perturbation theory (DFPT) calculations using Quantum ESPRESSO to compute phonon dispersions, Eliashberg spectral function α²F(ω), electronic density of states, and extract key parameters: electron-phonon coupling constant λ, maximum phonon frequency ω_D, Fermi energy ε_F, and logarithmic phonon frequency ω_log for cubic Im-3m H3S and monoclinic C2/m PH3 at 200 GPa. Use the provided crystal structures and pseudopotentials.
- Evidence: `/app/outputs/dfpt_parameters.json`

### Step 2: Eliashberg analysis and calculation of superconducting properties
- Role: scored (load-bearing)
- Action: Using the α²F(ω) and parameters from the DFPT step, solve the conventional Migdal-Eliashberg equations on the imaginary axis at the experimental critical temperature (T_C = 178 K for H3S, T_C = 81 K for PH3) to find the critical Coulomb pseudopotential μ_C*. Solve the vertex-corrected Eliashberg equations with the modified kernel to obtain the corrected μ_C*. Use analytic continuation to compute the superconducting energy gap Δ(T), extract the zero-temperature gap Δ(0) and the ratio 2Δ(0)/T_C, and determine the electron effective mass ratio m_e*/m_e. From condensation energy, compute the specific heat difference ΔC and thermodynamic critical field H_C, and derive the dimensionless ratios R_C and R_H. Report all quantities in the output JSON file.
- Output file: `/app/outputs/eliashberg_results.json`
- Format: json
- Contract: JSON object with top-level keys 'H3S' and 'PH3'. Each contains sub-objects 'conventional' and 'vertex_corrected', each having numeric keys: 'mu_star', 'delta_0' (meV), 'ratio_2delta_Tc', 'm_eff_ratio', 'R_C', 'R_H'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eliashberg_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eliashberg_results.json
- path: `/app/outputs/eliashberg_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing all headline superconducting properties (μ*, gap ratio, effective mass, thermodynamic ratios) for H3S and PH3 under conventional and vertex-corrected Eliashberg theory. The hidden checker compares each value to the paper-reported gold using tolerances and verifies that μ*_conventional > μ*_vertex_corrected for each compound.
- schema:
  - `type`: object
  - `required`: `H3S`, `PH3`
  - `properties`:
    - `H3S`:
      - `type`: object
      - `required`: `conventional`, `vertex_corrected`
      - `properties`:
        - `conventional`:
          - `type`: object
          - `required`: `mu_star`, `delta_0`, `ratio_2delta_Tc`, `m_eff_ratio`, `R_C`, `R_H`
          - `properties`:
            - `mu_star`:
              - `type`: number
            - `delta_0`:
              - `type`: number
              - `description`: meV
            - `ratio_2delta_Tc`:
              - `type`: number
            - `m_eff_ratio`:
              - `type`: number
            - `R_C`:
              - `type`: number
            - `R_H`:
              - `type`: number
        - `vertex_corrected`:
          - `type`: object
          - `required`: `mu_star`, `delta_0`, `ratio_2delta_Tc`, `m_eff_ratio`, `R_C`, `R_H`
          - `properties`:
            - `mu_star`:
              - `type`: number
            - `delta_0`:
              - `type`: number
              - `description`: meV
            - `ratio_2delta_Tc`:
              - `type`: number
            - `m_eff_ratio`:
              - `type`: number
            - `R_C`:
              - `type`: number
            - `R_H`:
              - `type`: number
    - `PH3`:
      - `type`: object
      - `required`: `conventional`, `vertex_corrected`
      - `properties`:
        - `conventional`:
          - `type`: object
          - `required`: `mu_star`, `delta_0`, `ratio_2delta_Tc`, `m_eff_ratio`, `R_C`, `R_H`
          - `properties`:
            - `mu_star`:
              - `type`: number
            - `delta_0`:
              - `type`: number
              - `description`: meV
            - `ratio_2delta_Tc`:
              - `type`: number
            - `m_eff_ratio`:
              - `type`: number
            - `R_C`:
              - `type`: number
            - `R_H`:
              - `type`: number
        - `vertex_corrected`:
          - `type`: object
          - `required`: `mu_star`, `delta_0`, `ratio_2delta_Tc`, `m_eff_ratio`, `R_C`, `R_H`
          - `properties`:
            - `mu_star`:
              - `type`: number
            - `delta_0`:
              - `type`: number
              - `description`: meV
            - `ratio_2delta_Tc`:
              - `type`: number
            - `m_eff_ratio`:
              - `type`: number
            - `R_C`:
              - `type`: number
            - `R_H`:
              - `type`: number

Notes: The verifier also checks structural consistency: μ*_conventional > μ*_vertex_corrected for each compound, and within each compound the gap ratio and effective mass are equal between formalisms within a small tolerance. Weight distribution: 50% μ* values, 30% gap and mass, 20% RC and RH.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eliashberg_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "H3S",
          "PH3"
        ],
        "properties": {
          "H3S": {
            "type": "object",
            "required": [
              "conventional",
              "vertex_corrected"
            ],
            "properties": {
              "conventional": {
                "type": "object",
                "required": [
                  "mu_star",
                  "delta_0",
                  "ratio_2delta_Tc",
                  "m_eff_ratio",
                  "R_C",
                  "R_H"
                ],
                "properties": {
                  "mu_star": {
                    "type": "number"
                  },
                  "delta_0": {
                    "type": "number",
                    "description": "meV"
                  },
                  "ratio_2delta_Tc": {
                    "type": "number"
                  },
                  "m_eff_ratio": {
                    "type": "number"
                  },
                  "R_C": {
                    "type": "number"
                  },
                  "R_H": {
                    "type": "number"
                  }
                }
              },
              "vertex_corrected": {
                "type": "object",
                "required": [
                  "mu_star",
                  "delta_0",
                  "ratio_2delta_Tc",
                  "m_eff_ratio",
                  "R_C",
                  "R_H"
                ],
                "properties": {
                  "mu_star": {
                    "type": "number"
                  },
                  "delta_0": {
                    "type": "number",
                    "description": "meV"
                  },
                  "ratio_2delta_Tc": {
                    "type": "number"
                  },
                  "m_eff_ratio": {
                    "type": "number"
                  },
                  "R_C": {
                    "type": "number"
                  },
                  "R_H": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "PH3": {
            "type": "object",
            "required": [
              "conventional",
              "vertex_corrected"
            ],
            "properties": {
              "conventional": {
                "type": "object",
                "required": [
                  "mu_star",
                  "delta_0",
                  "ratio_2delta_Tc",
                  "m_eff_ratio",
                  "R_C",
                  "R_H"
                ],
                "properties": {
                  "mu_star": {
                    "type": "number"
                  },
                  "delta_0": {
                    "type": "number",
                    "description": "meV"
                  },
                  "ratio_2delta_Tc": {
                    "type": "number"
                  },
                  "m_eff_ratio": {
                    "type": "number"
                  },
                  "R_C": {
                    "type": "number"
                  },
                  "R_H": {
                    "type": "number"
                  }
                }
              },
              "vertex_corrected": {
                "type": "object",
                "required": [
                  "mu_star",
                  "delta_0",
                  "ratio_2delta_Tc",
                  "m_eff_ratio",
                  "R_C",
                  "R_H"
                ],
                "properties": {
                  "mu_star": {
                    "type": "number"
                  },
                  "delta_0": {
                    "type": "number",
                    "description": "meV"
                  },
                  "ratio_2delta_Tc": {
                    "type": "number"
                  },
                  "m_eff_ratio": {
                    "type": "number"
                  },
                  "R_C": {
                    "type": "number"
                  },
                  "R_H": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Scored artifact containing all headline superconducting properties (μ*, gap ratio, effective mass, thermodynamic ratios) for H3S and PH3 under conventional and vertex-corrected Eliashberg theory. The hidden checker compares each value to the paper-reported gold using tolerances and verifies that μ*_conventional > μ*_vertex_corrected for each compound."
    }
  ],
  "notes": "The verifier also checks structural consistency: μ*_conventional > μ*_vertex_corrected for each compound, and within each compound the gap ratio and effective mass are equal between formalisms within a small tolerance. Weight distribution: 50% μ* values, 30% gap and mass, 20% RC and RH."
}
```

## How you are scored
A hidden verifier independently scores the submitted `eliashberg_results.json`. For each numerical value, the verifier compares your result against a reference obtained from the original work, applying tolerances appropriate for a re‑run with a different code implementation. The verifier also checks structural consistency: for each compound the conventional µ* must be larger than the vertex‑corrected µ*, and the gap ratio and effective mass must be essentially unchanged between the two formalisms. The final reward is a weighted combination of these checks, with the largest weight (50 %) assigned to the Coulomb pseudopotential values, 30 % to the energy‑gap ratio and the effective mass, and 20 % to the thermodynamic ratios RC and RH. Simply copying numbers from the literature without executing the required calculations will not pass these checks.
