# Defect and Solution Energies for Xe in UO2 using Mott-Littleton Method

## Problem background
Fission xenon (Xe) produced during reactor operation becomes trapped in the UO₂ fuel lattice, affecting fuel swelling and fission-gas release. Predicting this behavior requires reliable energies for Xe atoms interacting with lattice defects — single vacancies, vacancy aggregates, and their complexes — under relevant temperature and stoichiometry conditions. This task addresses the computation of single Xe atom defect energies, trap formation energies, solution energies, and a proposed migration mechanism in UO₂ using an ionic model with shell polarisation and first-principles-derived interatomic potentials.

## Approach
We use a static lattice defect simulation within the Mott-Littleton method: the crystal around a defect is divided into an inner region treated atomistically and an outer continuum. The UO₂ lattice is described by a fully ionic shell model with short-range Born-Mayer (U–O) and Buckingham/spline (O–O) potentials; the Xe–lattice interactions use a Born-Mayer (Xe–U) and a cubic spline (Xe–O) potentials. Temperature is introduced via the lattice constant at 298, 1773, 2273, and 2773 K. For each trap type (anion vacancy, cation vacancy, divacancy, neutral trivacancy, charged trivacancy, tetravacancy) we compute two energies: the defect energy (Xe present) and the unoccupied trap energy (no Xe). From these, together with an additional anion interstitial simulation, we derive the Schottky trio energy, Frenkel pair energy, and binding energies of vacancy aggregates. Using the expressions for trap formation energies in different stoichiometry regimes (anion-deficient, stoichiometric, anion-excess), we then calculate solution energies for pre-existing traps (defect − unoccupied) and for full thermodynamic equilibrium (adding the trap formation energy). Finally, we simulate the trivacancy migration mechanism: the energy to create a second adjacent trivacancy plus the barrier for Xe to move to the midway position.

## Reproduction target
Produce a single JSON file containing all computed energies for Xe in UO₂ at the four temperatures, organized as: defect energies per trap (Table 3), unoccupied trap energies per trap (Table 4), trap formation energies for the three stoichiometries per trap (Table 5), solution energies for pre-existing traps per trap (Table 6), solution energies for full thermodynamic equilibrium per trap under each stoichiometry (Table 7), migration activation energies for the trivacancy mechanism (Table 8), and the derived basic energies (Schottky trio, Frenkel pair, and binding energies for divacancy, neutral trivacancy, charged trivacancy, tetravacancy). All values must be in electronvolts (eV).

## Assets

- UO2 lattice potential parameters
- Xe gas-lattice potentials
- Temperature-dependent lattice constants
- Mott-Littleton simulation code (GULP or equivalent): https://gulp.curtin.edu.au/

## Workflow steps

### Step 1: Compute raw defect and unoccupied trap energies
- Role: process
- Action: Using the provided lattice and gas-lattice potentials and the temperature-dependent lattice constants, perform static Mott-Littleton defect calculations for each trap type (anion vacancy, cation vacancy, divacancy, neutral trivacancy, charged trivacancy, tetravacancy) at each of the four temperatures (298 K, 1773 K, 2273 K, 2773 K). For every configuration, compute the defect energy (with Xe atom present) and the unoccupied trap energy (without Xe). Store the raw energies in a temporary file for the next step.
- Evidence: `/app/outputs/raw_energies.json`

### Step 2: Derive Schottky trio, Frenkel pair, and binding energies
- Role: process
- Action: From the raw unoccupied trap energies and an additional simulation of an isolated anion interstitial, compute the Frenkel pair formation energy E_f = E(anion vacancy) + E(anion interstitial). Calculate the binding energies of vacancy aggregates (B_dv, B_nt, B_ct, B_tv) using the relation: binding energy = (sum of isolated component formation energies) - (energy of the complex). Derive the Schottky trio formation energy E_s using the stoichiometry-independent neutral trivacancy trap formation relation E_t = E_s - B_nt, referencing the computed unoccupied neutral trivacancy energy. Store the derived E_s, E_f, and binding energies.
- Evidence: `/app/outputs/derived_basic_energies.json`

### Step 3: Compute final target energies
- Role: scored
- Action: Using the raw energies from Step s1 and the derived basic energies from Step s2, compute: (a) defect energies (Table 3); (b) unoccupied trap energies (Table 4); (c) trap formation energies for anion-deficient, stoichiometric, and anion-excess UO₂ using the expressions in the paper’s Appendix; (d) solution energies for pre-existing traps (defect energy minus unoccupied trap energy); (e) solution energies for full thermodynamic equilibrium (add the appropriate trap formation energy to the pre-existing solution energy); (f) migration activation energies for the trivacancy mechanism by simulating the energy cost to create a second trivacancy adjacent to the trapped Xe and the energy to move the Xe to a midway position. Output all quantities in a single structured JSON file.
- Output file: `/app/outputs/computed_energies.json`
- Format: json
- Contract: Object with keys: defect_energies (object mapping trap name to list of 4 floats), unoccupied_trap_energies (same structure), trap_formation_energies (object with sub-keys 'anion_deficient', 'stoichiometric', 'anion_excess', each mapping trap name to list of 4 floats), solution_energies_pre_existent (object mapping trap name to list of 4 floats), solution_energies_equilibrium (object with stoichiometry sub-keys each mapping trap name to list of 4 floats), migration_activation_energies (list of 4 floats), basic_energies (object with keys 'schottky_trio_energy', 'frenkel_pair_energy', and binding energies for each aggregate, each a list of 4 floats). All values in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_energies.json
- path: `/app/outputs/computed_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Complete set of computed defect, trap, solution, and migration activation energies for Xe in UO2 at four temperatures and three stoichiometries, together with derived basic energy parameters. All values in eV.
- schema:
  - `type`: object
  - `required`: `defect_energies`, `unoccupied_trap_energies`, `trap_formation_energies`, `solution_energies_pre_existent`, `solution_energies_equilibrium`, `migration_activation_energies`, `basic_energies`
  - `properties`:
    - `defect_energies`:
      - `type`: object
      - `additionalProperties`:
        - `type`: array
        - `items`:
          - `type`: number
        - `minItems`: 4
        - `maxItems`: 4
      - `description`: Trap name (string) -> list of 4 float energies in eV for T=298,1773,2273,2773 K
    - `unoccupied_trap_energies`:
      - `type`: object
      - `additionalProperties`:
        - `type`: array
        - `items`:
          - `type`: number
        - `minItems`: 4
        - `maxItems`: 4
    - `trap_formation_energies`:
      - `type`: object
      - `required`: `anion_deficient`, `stoichiometric`, `anion_excess`
      - `properties`:
        - `anion_deficient`:
          - `type`: object
          - `additionalProperties`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
        - `stoichiometric`:
          - `type`: object
          - `additionalProperties`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
        - `anion_excess`:
          - `type`: object
          - `additionalProperties`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
    - `solution_energies_pre_existent`:
      - `type`: object
      - `additionalProperties`:
        - `type`: array
        - `items`:
          - `type`: number
        - `minItems`: 4
        - `maxItems`: 4
    - `solution_energies_equilibrium`:
      - `type`: object
      - `required`: `anion_deficient`, `stoichiometric`, `anion_excess`
      - `properties`:
        - `anion_deficient`:
          - `type`: object
          - `additionalProperties`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
        - `stoichiometric`:
          - `type`: object
          - `additionalProperties`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
        - `anion_excess`:
          - `type`: object
          - `additionalProperties`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
    - `migration_activation_energies`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 4
      - `maxItems`: 4
    - `basic_energies`:
      - `type`: object
      - `required`: `schottky_trio_energy`, `frenkel_pair_energy`, `binding_energy_divacancy`, `binding_energy_neutral_trivacancy`, `binding_energy_charged_trivacancy`, `binding_energy_tetravacancy`
      - `properties`:
        - `schottky_trio_energy`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4
        - `frenkel_pair_energy`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4
        - `binding_energy_divacancy`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4
        - `binding_energy_neutral_trivacancy`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4
        - `binding_energy_charged_trivacancy`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4
        - `binding_energy_tetravacancy`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4

Notes: Internal consistency between solution_energies_pre_existent, defect_energies, and unoccupied_trap_energies is expected. The checker will also recompute trap formation energies from basic_energies using the Appendix relations and verify neutrality and stoichiometry-independence of the neutral trivacancy trap formation energy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "defect_energies",
          "unoccupied_trap_energies",
          "trap_formation_energies",
          "solution_energies_pre_existent",
          "solution_energies_equilibrium",
          "migration_activation_energies",
          "basic_energies"
        ],
        "properties": {
          "defect_energies": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 4,
              "maxItems": 4
            },
            "description": "Trap name (string) -> list of 4 float energies in eV for T=298,1773,2273,2773 K"
          },
          "unoccupied_trap_energies": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 4,
              "maxItems": 4
            }
          },
          "trap_formation_energies": {
            "type": "object",
            "required": [
              "anion_deficient",
              "stoichiometric",
              "anion_excess"
            ],
            "properties": {
              "anion_deficient": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                }
              },
              "stoichiometric": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                }
              },
              "anion_excess": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                }
              }
            }
          },
          "solution_energies_pre_existent": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 4,
              "maxItems": 4
            }
          },
          "solution_energies_equilibrium": {
            "type": "object",
            "required": [
              "anion_deficient",
              "stoichiometric",
              "anion_excess"
            ],
            "properties": {
              "anion_deficient": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                }
              },
              "stoichiometric": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                }
              },
              "anion_excess": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4
                }
              }
            }
          },
          "migration_activation_energies": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 4,
            "maxItems": 4
          },
          "basic_energies": {
            "type": "object",
            "required": [
              "schottky_trio_energy",
              "frenkel_pair_energy",
              "binding_energy_divacancy",
              "binding_energy_neutral_trivacancy",
              "binding_energy_charged_trivacancy",
              "binding_energy_tetravacancy"
            ],
            "properties": {
              "schottky_trio_energy": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "maxItems": 4
              },
              "frenkel_pair_energy": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "maxItems": 4
              },
              "binding_energy_divacancy": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "maxItems": 4
              },
              "binding_energy_neutral_trivacancy": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "maxItems": 4
              },
              "binding_energy_charged_trivacancy": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "maxItems": 4
              },
              "binding_energy_tetravacancy": {
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
      },
      "description": "Complete set of computed defect, trap, solution, and migration activation energies for Xe in UO2 at four temperatures and three stoichiometries, together with derived basic energy parameters. All values in eV."
    }
  ],
  "notes": "Internal consistency between solution_energies_pre_existent, defect_energies, and unoccupied_trap_energies is expected. The checker will also recompute trap formation energies from basic_energies using the Appendix relations and verify neutrality and stoichiometry-independence of the neutral trivacancy trap formation energy."
}
```

## How you are scored
A hidden verifier reads your computed_energies.json. It performs internal consistency checks (e.g., solution_energies_pre_existent must equal defect_energies minus unoccupied_trap_energies; trap formation energies must satisfy the stoichiometry-dependent formulas using the supplied basic energies; the neutral trivacancy trap formation energy must be identical across all three stoichiometries). It then compares your computed values against hidden reference values derived from the original study, with appropriate tolerances. Reward is based on the fraction of quantities that pass both the consistency tests and the reference comparisons. Reporting numbers that satisfy the internal relations but do not match the hidden reference will score lower; the highest reward goes to faithful re‑computation that reproduces the target energies within tolerance.
