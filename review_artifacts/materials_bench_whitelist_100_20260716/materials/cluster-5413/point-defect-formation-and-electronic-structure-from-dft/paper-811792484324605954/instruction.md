# Defect cluster binding energies in Ni-doped ceria: atomistic simulations

## Problem background
Solid oxide fuel cells (SOFCs) operating at intermediate temperatures (∼500 °C) require thin, dense electrolyte films to minimize ohmic losses. Gd-doped ceria (GDC) is a candidate electrolyte material, but its performance can be degraded by microstructural inhomogeneities (nano-sized domains, superstructures, and local oxygen‑vacancy ordering) that appear when dopant concentration exceeds 10–15 at.%. In anode‑supported thin‑film cells fabricated by co‑sintering and reduction, nickel from the Ni‑GDC cermet anode can diffuse into the GDC film near the interface. The central open question is whether and how this Ni incorporation alters the stability of defect clusters containing dopant cations and oxygen vacancies, thereby influencing the formation of inhomogeneous microstructures and the resulting ionic conductivity.

## Approach
The investigation uses classical atomistic simulation based on the Born model of ionic solids, implemented in the open‑source lattice simulation code GULP. Short‑range interactions are described by Buckingham pair potentials with shell‑model polarizability for Ce⁴⁺ and O²⁻ ions. CeO₂ is modeled as a fluorite unit cell with lattice constant 5.411 Å. Defect configurations are relaxed using the Mott–Littleton two‑region approach, with region I radius 3.0 a₀ and region IIa radius 6.0 a₀.

First, the defect energies of isolated point defects (an oxygen vacancy V_O^··, substitutional Ni²⁺ and Gd³⁺ on Ce sites, and an interstitial Ni²⁺) together with the lattice energies of CeO₂ and NiO are obtained. Reaction energies for incorporating Ni into CeO₂ are then computed for two possible charge‑compensation routes: (i) vacancy compensation, where the substitution of Ni²⁺ for Ce⁴⁺ is accompanied by creation of an oxygen vacancy, and (ii) an interstitial route where a second Ni²⁺ occupies an interstitial site. These reaction energies are derived from sums of lattice and defect energies.

Next, the total energies of defect clusters containing Ni²⁺ or Gd³⁺ and oxygen vacancies are calculated. The binding energy of a cluster is defined as the sum of the isolated defect energies of its constituents minus the relaxed cluster energy. For (Ni_Ce'' V_O^··)× clusters the binding energy is evaluated for three vacancy positions (first, second, and third neighbour with respect to the Ni dopant). For the larger (2 Ni_Ce'' 2 V_O^··)× cluster, four different vacancy arrangements are examined to find the most stable configuration. Analogous clusters containing Gd³⁺ are computed for comparison.

Finally, a comparative table is prepared that contrasts the binding energies and per‑vacancy binding energies of the most stable Ni‑containing and Gd‑containing clusters for n = 1 and n = 2 oxygen vacancies, together with the increments observed when going from n = 1 to n = 2.

## Reproduction target
Produce the following quantities:
1. Reaction energies for Ni incorporation into CeO₂ via the vacancy‑compensation and interstitial routes.
2. Binding energies ΔE for (Ni_Ce'' V_O^··)× clusters with the oxygen vacancy at the first, second, and third neighbour positions, for the most stable (2 Ni_Ce'' 2 V_O^··)× cluster, and for the corresponding most stable Gd‑containing clusters with n = 1 and n = 2 oxygen vacancies.
3. A structured comparison table containing ΔE and ΔE/n (binding energy per oxygen vacancy) for the most stable Ni‑containing cluster and the most stable Gd‑containing cluster at n = 1 and n = 2, and the increase in ΔE and ΔE/n when the cluster size doubles. All energies are reported in electronvolts (eV).

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/
- Interatomic potential parameters (Buckingham and shell model)

## Workflow steps

### Step 1: Run atomistic simulations with GULP
- Role: process
- Action: Install GULP, prepare input files with the specified Buckingham and shell-model parameters, set up the fluorite unit cell (a0=5.411 A), define all required defect configurations (isolated point defects and clusters), run GULP with the Mott-Littleton two-region approach (region I radius 3.0 a0, region IIa 6.0 a0), and collect the total energies.
- Evidence: `/app/outputs/gulp_output.log`

### Step 2: Extract isolated defect and lattice energies
- Role: scored
- Action: From the GULP output, extract the lattice energies of CeO2 and NiO, and the defect energies of V_O, Ni_Ce'', Ni_i, and Gd_Ce. Write them to step_00_isolated_energies.json.
- Output file: `/app/outputs/step_00_isolated_energies.json`
- Format: json
- Contract: JSON object with keys: lattice_energy_CeO2 (float, eV), lattice_energy_NiO (float, eV), defect_energies (object with keys VO, NiCe, Ni_i, Gd_Ce, each a float in eV)
- Scoring: scored by hidden verifier

### Step 3: Calculate reaction energies and cluster binding energies
- Role: scored (load-bearing)
- Action: Using the isolated defect energies, lattice energies, and cluster total energies from the simulation, compute reaction energies for Ni incorporation via vacancy compensation and interstitial route, and binding energies for (Ni_Ce'' V_O) clusters at three neighbour positions, the most stable (2Ni_Ce'' 2V_O) cluster, and corresponding Gd-containing clusters. Write the results to step_01_binding_energies.json.
- Output file: `/app/outputs/step_01_binding_energies.json`
- Format: json
- Contract: JSON object with: reaction_energies (object with vacancy_compensation and interstitial_route, each float in eV), clusters (array of objects each with label (string) and delta_E (float in eV))
- Scoring: scored by hidden verifier

### Step 4: Compile Ni vs Gd cluster binding energy comparison
- Role: scored
- Action: From the binding energies computed in the previous step, assemble the comparative table: for n=1 and n=2 oxygen vacancies, report delta_E and delta_E/n for the most stable Ni- and Gd-containing clusters, and the increases in delta_E and delta_E/n with cluster size. Write to step_02_comparison_table.json.
- Output file: `/app/outputs/step_02_comparison_table.json`
- Format: json
- Contract: JSON object with: Ni_clusters (array of objects with n_vacancies (int), delta_E (float, eV), delta_E_per_vac (float, eV)), Gd_clusters (same structure), increase_Ni (object with delta_E and delta_E_per_vac, floats in eV), increase_Gd (same structure)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_00_isolated_energies.json`
- `/app/outputs/step_01_binding_energies.json`
- `/app/outputs/step_02_comparison_table.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_00_isolated_energies.json
- path: `/app/outputs/step_00_isolated_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Isolated defect and lattice energies in eV from GULP simulation.
- schema:
  - `type`: object
  - `required`: `lattice_energy_CeO2`, `lattice_energy_NiO`, `defect_energies`
  - `properties`:
    - `lattice_energy_CeO2`:
      - `type`: number
    - `lattice_energy_NiO`:
      - `type`: number
    - `defect_energies`:
      - `type`: object
      - `required`: `VO`, `NiCe`, `Ni_i`, `Gd_Ce`
      - `properties`:
        - `VO`:
          - `type`: number
        - `NiCe`:
          - `type`: number
        - `Ni_i`:
          - `type`: number
        - `Gd_Ce`:
          - `type`: number

### step_01_binding_energies.json
- path: `/app/outputs/step_01_binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reaction energies and cluster binding energies in eV.
- schema:
  - `type`: object
  - `required`: `reaction_energies`, `clusters`
  - `properties`:
    - `reaction_energies`:
      - `type`: object
      - `required`: `vacancy_compensation`, `interstitial_route`
      - `properties`:
        - `vacancy_compensation`:
          - `type`: number
        - `interstitial_route`:
          - `type`: number
    - `clusters`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `label`, `delta_E`
        - `properties`:
          - `label`:
            - `type`: string
          - `delta_E`:
            - `type`: number

### step_02_comparison_table.json
- path: `/app/outputs/step_02_comparison_table.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Comparative binding energy analysis for Ni vs Gd clusters.
- schema:
  - `type`: object
  - `required`: `Ni_clusters`, `Gd_clusters`, `increase_Ni`, `increase_Gd`
  - `properties`:
    - `Ni_clusters`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `n_vacancies`, `delta_E`, `delta_E_per_vac`
        - `properties`:
          - `n_vacancies`:
            - `type`: integer
          - `delta_E`:
            - `type`: number
          - `delta_E_per_vac`:
            - `type`: number
    - `Gd_clusters`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `n_vacancies`, `delta_E`, `delta_E_per_vac`
        - `properties`:
          - `n_vacancies`:
            - `type`: integer
          - `delta_E`:
            - `type`: number
          - `delta_E_per_vac`:
            - `type`: number
    - `increase_Ni`:
      - `type`: object
      - `required`: `delta_E`, `delta_E_per_vac`
      - `properties`:
        - `delta_E`:
          - `type`: number
        - `delta_E_per_vac`:
          - `type`: number
    - `increase_Gd`:
      - `type`: object
      - `required`: `delta_E`, `delta_E_per_vac`
      - `properties`:
        - `delta_E`:
          - `type`: number
        - `delta_E_per_vac`:
          - `type`: number

Notes: All energies in eV. The checker compares the numerical values against the hidden paper-reported values with tolerances and verifies the ordering (Ni cluster binding energies > Gd, larger increase for Ni) as an additional structural check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_00_isolated_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lattice_energy_CeO2",
          "lattice_energy_NiO",
          "defect_energies"
        ],
        "properties": {
          "lattice_energy_CeO2": {
            "type": "number"
          },
          "lattice_energy_NiO": {
            "type": "number"
          },
          "defect_energies": {
            "type": "object",
            "required": [
              "VO",
              "NiCe",
              "Ni_i",
              "Gd_Ce"
            ],
            "properties": {
              "VO": {
                "type": "number"
              },
              "NiCe": {
                "type": "number"
              },
              "Ni_i": {
                "type": "number"
              },
              "Gd_Ce": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Isolated defect and lattice energies in eV from GULP simulation."
    },
    {
      "file": "step_01_binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "reaction_energies",
          "clusters"
        ],
        "properties": {
          "reaction_energies": {
            "type": "object",
            "required": [
              "vacancy_compensation",
              "interstitial_route"
            ],
            "properties": {
              "vacancy_compensation": {
                "type": "number"
              },
              "interstitial_route": {
                "type": "number"
              }
            }
          },
          "clusters": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "label",
                "delta_E"
              ],
              "properties": {
                "label": {
                  "type": "string"
                },
                "delta_E": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Reaction energies and cluster binding energies in eV."
    },
    {
      "file": "step_02_comparison_table.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ni_clusters",
          "Gd_clusters",
          "increase_Ni",
          "increase_Gd"
        ],
        "properties": {
          "Ni_clusters": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "n_vacancies",
                "delta_E",
                "delta_E_per_vac"
              ],
              "properties": {
                "n_vacancies": {
                  "type": "integer"
                },
                "delta_E": {
                  "type": "number"
                },
                "delta_E_per_vac": {
                  "type": "number"
                }
              }
            }
          },
          "Gd_clusters": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "n_vacancies",
                "delta_E",
                "delta_E_per_vac"
              ],
              "properties": {
                "n_vacancies": {
                  "type": "integer"
                },
                "delta_E": {
                  "type": "number"
                },
                "delta_E_per_vac": {
                  "type": "number"
                }
              }
            }
          },
          "increase_Ni": {
            "type": "object",
            "required": [
              "delta_E",
              "delta_E_per_vac"
            ],
            "properties": {
              "delta_E": {
                "type": "number"
              },
              "delta_E_per_vac": {
                "type": "number"
              }
            }
          },
          "increase_Gd": {
            "type": "object",
            "required": [
              "delta_E",
              "delta_E_per_vac"
            ],
            "properties": {
              "delta_E": {
                "type": "number"
              },
              "delta_E_per_vac": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Comparative binding energy analysis for Ni vs Gd clusters."
    }
  ],
  "notes": "All energies in eV. The checker compares the numerical values against the hidden paper-reported values with tolerances and verifies the ordering (Ni cluster binding energies > Gd, larger increase for Ni) as an additional structural check."
}
```

## How you are scored
A hidden verifier will independently score each of the three output artifacts (step_00_isolated_energies.json, step_01_binding_energies.json, and step_02_comparison_table.json). The verifier compares your reported numerical values against a hidden set of reference values using appropriate tolerances, and verifies the relative trends (e.g., the ordering of binding energies between Ni‑ and Gd‑containing clusters and the magnitude of their increase with cluster size). Each artifact carries a weight, and the final reward (a float between 0 and 1) is the weighted sum of the per‑artifact scores. Reporting the correct paper values without honest simulation is not sufficient; the hidden checks are designed to reflect genuine computational reproduction.
