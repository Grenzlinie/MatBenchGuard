# Structural, Electronic, and Thermal Properties of C15 Laves Alloys via DFT and Quasi-harmonic Debye Model

## Problem background
C15 Laves phases such as Cr₂Zr and Cr₂Nb are candidate intermetallic compounds for high‑temperature structural applications because of their high melting points and good oxidation resistance. The pseudo‑binary series Cr₂Zr₁₋ₓNbₓ with the cubic C15 structure offers a way to tune mechanical and thermal stability. Detailed knowledge of structural parameters, electronic structure, and thermodynamic properties between 0 K and 1500 K is often scarce experimentally. Density functional theory (DFT) can provide these properties at 0 K, and the quasi‑harmonic Debye model extends them to finite temperatures using the computed total‑energy vs volume relationship. The task is to compute and report these quantities for the complete solid‑solution series.

## Approach
The work uses periodic DFT with the GGA‑PBE exchange‑correlation functional to calculate the total energy as a function of unit‑cell volume for the C15 Laves structures of Cr₂Zr, Cr₂Nb, and three ordered ternary compositions (Cr₂Zr₀.₇₅Nb₀.₂₅, Cr₂Zr₀.₅Nb₀.₅, Cr₂Zr₀.₂₅Nb₀.₇₅). Equilibrium lattice constants and bulk moduli are extracted by fitting the Murnaghan equation of state to the E(V) data. Heats of formation are obtained from the total‑energy differences between the alloy and the elemental ground‑state structures (bcc‑Cr, hcp‑Zr, bcc‑Nb). At the equilibrium geometries, self‑consistent electronic structure calculations yield the total density of states; the value at the Fermi level N(E_F) is read off for the pure endpoints and the equimolar composition. With the E(V) curves as input, the quasi‑harmonic Debye model is implemented: the Debye temperature is determined from the isotropic expression (Debye temperature θ_D ∝ (B_S / M)^{1/2} with the scaling function f(σ) depending on the Poisson ratio) using the isothermal bulk modulus derived from E(V). The non‑equilibrium Gibbs function G*(V;T,p) is minimized at each (T, p=0) to obtain the temperature‑dependent equilibrium volume and derived properties: lattice parameter a(T), bulk modulus B(T), volumetric thermal expansion coefficient α(T), heat capacity at constant volume C_V(T), Grüneisen parameter γ(T), and Debye temperature θ_D(T). The model is applied from 0 to 1500 K. All calculations are carried out using an open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) with standard PBE pseudopotentials, and the Debye model is implemented as a post‑processing script.

## Reproduction target
Produce three scored JSON artifacts containing the following computed quantities:
- **Structural and energetic properties** (`step_01_structural_results.json`): For each of the five compositions (x = 0, 0.25, 0.5, 0.75, 1.0), report the equilibrium lattice constant a₀ (Å), the bulk modulus B₀ (GPa), and the heat of formation ΔH_f (eV per formula unit).
- **Electronic property** (`step_02_electronic_results.json`): For the three compositions x = 0, 0.5, 1.0, report the total density of states at the Fermi level N(E_F) in units of states/Ry.
- **Thermal properties** (`step_03_thermal_results.json`): For each of the five compositions, report the temperature‑dependent quantities at the fixed temperature points T = {0, 300, 600, 900, 1200, 1500} K: lattice parameter a(T) (Å), bulk modulus B(T) (GPa), thermal expansion coefficient α(T) (×10⁻⁵ K⁻¹), Grüneisen parameter γ(T), heat capacity C_V(T) (J mol⁻¹ K⁻¹), and Debye temperature θ_D(T) (K). These must be obtained from the quasi‑harmonic Debye model at zero pressure using the DFT‑calculated E(V) curves and the appropriate Poisson ratios (0.32 for Cr₂Zr, 0.34 for Cr₂Nb, 0.33 for ternaries).

## Assets

- Quantum ESPRESSO (GGA-PBE): https://www.quantum-espresso.org/
- PBE pseudopotentials for Cr, Zr, Nb: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT total-energy calculations
- Role: process
- Action: Perform DFT total-energy calculations for C15 Laves phases Cr2Zr1-xNbx (x=0,0.25,0.5,0.75,1.0) and for pure elements Cr (bcc), Zr (hcp), Nb (bcc) using GGA-PBE. Vary the unit cell volume to obtain total energy E(V) data for each system. Store the computed total energy vs volume data for later use.
- Evidence: `/app/outputs/ev_curves.json`

### Step 2: Extract equilibrium structural properties and heats of formation
- Role: scored
- Action: Fit the Murnaghan equation of state to the E(V) data from the DFT calculations to determine equilibrium lattice constants a0 and bulk moduli B0 for each composition. Compute heats of formation from the total energies of alloys and pure elements. Report the results for all x.
- Output file: `/app/outputs/step_01_structural_results.json`
- Format: json
- Contract: array of objects with fields: composition_x (number), a0_A (number), B0_GPa (number), heat_of_formation_eV (number)
- Scoring: scored by hidden verifier

### Step 3: Compute electronic density of states and Fermi-level DOS
- Role: scored
- Action: Using the equilibrium geometries, perform self-consistent field calculations and compute the total density of states (DOS). Extract the DOS at the Fermi level N(E_F) in states/Ry for the three endpoint compositions: x=0, 0.5, 1.0.
- Output file: `/app/outputs/step_02_electronic_results.json`
- Format: json
- Contract: array of objects with fields: composition_x (number), N_EF_states_per_Ry (number)
- Scoring: scored by hidden verifier

### Step 4: Quasi-harmonic Debye model thermal properties
- Role: scored (load-bearing)
- Action: Implement the quasi-harmonic Debye model using the E(V) data and Poisson's ratios (0.32 for Cr2Zr, 0.34 for Cr2Nb, 0.33 for ternaries). Compute the temperature-dependent lattice parameter, bulk modulus, thermal expansion coefficient, heat capacity, Grüneisen parameter, and Debye temperature for all compositions (x=0,0.25,0.5,0.75,1.0) from 0 to 1500 K at zero pressure. Output the thermal data for each composition at specified temperature points.
- Output file: `/app/outputs/step_03_thermal_results.json`
- Format: json
- Contract: object with key 'compositions' (array of objects, each with 'x' (number) and 'thermal_data' (object containing arrays: T_K, lattice_param_A, bulk_modulus_GPa, thermal_expansion_1e-5_per_K, gruneisen_param, heat_capacity_J_molK, debye_temp_K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_results.json`
- `/app/outputs/step_02_electronic_results.json`
- `/app/outputs/step_03_thermal_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_results.json
- path: `/app/outputs/step_01_structural_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium structural parameters and heats of formation for each composition (x=0,0.25,0.5,0.75,1.0).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `composition_x`:
        - `type`: number
      - `a0_A`:
        - `type`: number
      - `B0_GPa`:
        - `type`: number
      - `heat_of_formation_eV`:
        - `type`: number
    - `required`: `composition_x`, `a0_A`, `B0_GPa`, `heat_of_formation_eV`

### step_02_electronic_results.json
- path: `/app/outputs/step_02_electronic_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fermi-level density of states (states/Ry) for Cr2Zr, Cr2Zr0.5Nb0.5, and Cr2Nb.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `composition_x`:
        - `type`: number
      - `N_EF_states_per_Ry`:
        - `type`: number
    - `required`: `composition_x`, `N_EF_states_per_Ry`

### step_03_thermal_results.json
- path: `/app/outputs/step_03_thermal_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent lattice parameter, bulk modulus, thermal expansion, heat capacity, Grüneisen parameter, and Debye temperature from the quasi-harmonic Debye model for 0–1500 K at p=0, for all compositions (x=0,0.25,0.5,0.75,1.0).
- schema:
  - `type`: object
  - `properties`:
    - `compositions`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `x`:
            - `type`: number
          - `thermal_data`:
            - `type`: object
            - `properties`:
              - `T_K`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `lattice_param_A`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `bulk_modulus_GPa`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `thermal_expansion_1e-5_per_K`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `gruneisen_param`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `heat_capacity_J_molK`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `debye_temp_K`:
                - `type`: array
                - `items`:
                  - `type`: number
            - `required`: `T_K`, `lattice_param_A`, `bulk_modulus_GPa`, `thermal_expansion_1e-5_per_K`, `gruneisen_param`, `heat_capacity_J_molK`, `debye_temp_K`
        - `required`: `x`, `thermal_data`
  - `required`: `compositions`

Notes: All scored artifacts are compared against paper-reported reference values with domain‑appropriate tolerances. The thermal step also implicitly verifies expected physical trends (monotonicity, ordering) as part of the scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "composition_x": {
              "type": "number"
            },
            "a0_A": {
              "type": "number"
            },
            "B0_GPa": {
              "type": "number"
            },
            "heat_of_formation_eV": {
              "type": "number"
            }
          },
          "required": [
            "composition_x",
            "a0_A",
            "B0_GPa",
            "heat_of_formation_eV"
          ]
        }
      },
      "description": "Equilibrium structural parameters and heats of formation for each composition (x=0,0.25,0.5,0.75,1.0)."
    },
    {
      "file": "step_02_electronic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "composition_x": {
              "type": "number"
            },
            "N_EF_states_per_Ry": {
              "type": "number"
            }
          },
          "required": [
            "composition_x",
            "N_EF_states_per_Ry"
          ]
        }
      },
      "description": "Fermi-level density of states (states/Ry) for Cr2Zr, Cr2Zr0.5Nb0.5, and Cr2Nb."
    },
    {
      "file": "step_03_thermal_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "compositions": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "x": {
                  "type": "number"
                },
                "thermal_data": {
                  "type": "object",
                  "properties": {
                    "T_K": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "lattice_param_A": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "bulk_modulus_GPa": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "thermal_expansion_1e-5_per_K": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "gruneisen_param": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "heat_capacity_J_molK": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "debye_temp_K": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    }
                  },
                  "required": [
                    "T_K",
                    "lattice_param_A",
                    "bulk_modulus_GPa",
                    "thermal_expansion_1e-5_per_K",
                    "gruneisen_param",
                    "heat_capacity_J_molK",
                    "debye_temp_K"
                  ]
                }
              },
              "required": [
                "x",
                "thermal_data"
              ]
            }
          }
        },
        "required": [
          "compositions"
        ]
      },
      "description": "Temperature-dependent lattice parameter, bulk modulus, thermal expansion, heat capacity, Grüneisen parameter, and Debye temperature from the quasi-harmonic Debye model for 0–1500 K at p=0, for all compositions (x=0,0.25,0.5,0.75,1.0)."
    }
  ],
  "notes": "All scored artifacts are compared against paper-reported reference values with domain‑appropriate tolerances. The thermal step also implicitly verifies expected physical trends (monotonicity, ordering) as part of the scoring."
}
```

## How you are scored
A hidden automated verifier will inspect the three output JSON files. Each scored artifact is compared against a reference (the paper’s own DFT + Debye model results) using domain‑appropriate tolerances and structural checks. For the structural and electronic steps, the verifier evaluates agreement with the reference values. For the thermal step, it additionally checks that the data obey physically required trends: for each composition, a(T) increases with T, B(T) decreases with T, thermal expansion increases with T, heat capacity approaches the Dulong–Petit limit, and Debye temperature decreases with T. The orderings a(Cr₂Zr) > a(Cr₂Nb) and B(Cr₂Nb) > B(Cr₂Zr) at 0 K are also verified. The three steps are assigned weights, and the overall reward is the weighted sum of the individual scores, ranging from 0 (poor agreement) to 1 (excellent agreement). Simply reporting the paper’s numbers without running the workflow will not pass; the verifier cross‑checks multiple independent quantities and trends that can only be correctly reproduced by genuine calculations.
