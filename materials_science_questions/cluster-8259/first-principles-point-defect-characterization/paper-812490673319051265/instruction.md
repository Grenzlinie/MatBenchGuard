# First-principles defect characterization of CsPbBr3

## Problem background
Metal halide perovskites such as CsPbBr3 exhibit defect tolerance despite significant defect densities. A hypothesised explanation is that all favourable native defects are shallow, i.e., they do not introduce deep levels in the band gap. This task uses first-principles DFT to inventory native point defects and hydrogen impurities in orthorhombic CsPbBr3 and to compute defect formation energies and thermodynamic charge-state transition levels. The goal is to determine the presence and nature of deep levels in the band gap.

## Approach
The computational workflow for defect characterization follows the standard defect formation energy formalism. Using the hybrid functional HSE (with 35% exact exchange and 0.1 Å⁻¹ screening) and spin–orbit coupling, total energies are computed for a pristine supercell and for supercells containing each native defect (vacancies, interstitials, antisites) and hydrogen impurities in multiple charge states. Chemical potentials of the atomic species are determined from elemental and competing binary phases to define the Pb-rich and Br-rich limits. Defect formation energies E^f[X^q] are then computed as E[X^q] − E[bulk] − Σ n_i μ_i + q E_F + Δ^q, where E_F is the Fermi level referenced to the valence-band maximum (VBM) and Δ^q corrects for finite-size effects. Transition levels ε(q/q′) are calculated as (E^f[q; E_F=0] − E^f[q′; E_F=0])/(q′ − q). Finally, the convex hull of defect formation energies is constructed for both chemical potential regimes, and the charge-neutrality Fermi level is determined by balancing the concentrations of positive and negative defects.

## Reproduction target
Using DFT with the specified hybrid functional (HSE, 35% exact exchange, 0.1 Å⁻¹ screening) and spin–orbit coupling, compute defect formation energies E^f[X^q] for all relevant charge states of native vacancies, interstitials, antisites, and hydrogen impurities in orthorhombic CsPbBr3. From these, derive the thermodynamic charge-state transition levels ε(q/q′) that lie within the band gap (0 to 2.3 eV) and construct the defect hull under both Pb-rich and Br-rich chemical potential conditions. Report the total energies in step_01_total_energies.json, formation energies in step_02_formation_energies.json (evaluated at the VBM and at the charge-neutrality Fermi levels for each condition), transition levels in step_03_transition_levels.json, and defect hull data in step_04_defect_hull.json.

## Assets

- Orthorhombic CsPbBr3 crystal structure: 10.1021/cg400645x
- Elemental and binary phase structures for chemical potential: https://materialsproject.org/
- Quantum ESPRESSO DFT software: https://www.quantum-espresso.org/
- Pseudopotentials for Cs, Pb, Br: https://www.materialscloud.org/discover/sssp/table/psml
- Python post-processing packages: numpy scipy pymatgen

## Workflow steps

### Step 1: Supercell generation
- Role: process
- Action: Generate supercells for orthorhombic CsPbBr3: a pristine bulk supercell, and supercells for each native point defect (vacancies, interstitials, antisites) and hydrogen impurities in all relevant charge states.
- Evidence: `/app/outputs/structures.log`

### Step 2: Chemical potential determination
- Role: process
- Action: Compute total energies of elemental Cs, Pb, Br and competing binary phases (CsBr, PbBr2) using the same HSE+SOC setup. Derive the allowed chemical potential ranges and determine the Pb-rich and Br-rich limits.
- Evidence: `/app/outputs/chemical_potentials.json`

### Step 3: DFT total energy calculation
- Role: scored
- Action: Perform DFT calculations with HSE (35% exact exchange, 0.1 Å⁻¹ screening) and spin-orbit coupling for every generated supercell (pristine bulk and all defect/charge combinations). Relax atomic positions, obtain total energies E[X^q] and VBM alignment. Write total energies to step_01_total_energies.json.
- Output file: `/app/outputs/step_01_total_energies.json`
- Format: json
- Contract: Array of objects with keys: defect (string), charge (int), total_energy_eV (float), supercell_size (int). Bulk entry with defect='bulk', charge=0.
- Scoring: scored by hidden verifier

### Step 4: Defect formation energy calculation
- Role: scored (load-bearing)
- Action: Using total energies from step_01_total_energies.json, chemical potentials from chemical_potentials.json, and applying finite-size corrections (Freysoldt et al.) for charged defects, compute defect formation energies E^f[X^q] as a function of Fermi level. Report formation energies at VBM (E_F=0) and at the charge-neutrality Fermi levels for Pb-rich and Br-rich conditions. Write step_02_formation_energies.json.
- Output file: `/app/outputs/step_02_formation_energies.json`
- Format: json
- Contract: Array of objects with keys: defect (string), charge (int), Ef_at_VBM_eV (float), Ef_at_neutral_Pbrich_eV (float), Ef_at_neutral_Brrich_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Thermodynamic transition level calculation
- Role: scored
- Action: From formation energies at E_F=0, compute transition levels ε(q/q') = (E^f[q;E_F=0] - E^f[q';E_F=0])/(q' - q). Filter and report only those within the band gap (0 – 2.3 eV). Write step_03_transition_levels.json.
- Output file: `/app/outputs/step_03_transition_levels.json`
- Format: json
- Contract: Array of objects with keys: defect (string), charge_transition (string, e.g. '-/+'), energy_eV (float).
- Scoring: scored by hidden verifier

### Step 6: Defect hull and charge-neutrality analysis
- Role: scored
- Action: Identify the convex hull of defect formation energies vs Fermi level for both Pb-rich and Br-rich conditions. Determine the charge-neutrality Fermi level by solving for the point where the positive and negative defect concentrations balance. Write step_04_defect_hull.json.
- Output file: `/app/outputs/step_04_defect_hull.json`
- Format: json
- Contract: Object with keys 'Pb_rich' and 'Br_rich', each an object with keys: hull_defects (array of strings), crossing_fermi_level_eV (float), dominant_charged_defects (object with keys positive (string) and negative (string)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_total_energies.json`
- `/app/outputs/step_02_formation_energies.json`
- `/app/outputs/step_03_transition_levels.json`
- `/app/outputs/step_04_defect_hull.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_total_energies.json
- path: `/app/outputs/step_01_total_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT total energies for bulk and defect supercells.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect`, `charge`, `total_energy_eV`, `supercell_size`
    - `properties`:
      - `defect`:
        - `type`: string
      - `charge`:
        - `type`: integer
      - `total_energy_eV`:
        - `type`: number
      - `supercell_size`:
        - `type`: integer
  - `description`: Array of total energy objects for each supercell. Bulk entry uses defect='bulk' and charge=0.

### step_02_formation_energies.json
- path: `/app/outputs/step_02_formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Defect formation energies computed from total energies and chemical potentials.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect`, `charge`, `Ef_at_VBM_eV`, `Ef_at_neutral_Pbrich_eV`, `Ef_at_neutral_Brrich_eV`
    - `properties`:
      - `defect`:
        - `type`: string
      - `charge`:
        - `type`: integer
      - `Ef_at_VBM_eV`:
        - `type`: number
      - `Ef_at_neutral_Pbrich_eV`:
        - `type`: number
      - `Ef_at_neutral_Brrich_eV`:
        - `type`: number
  - `description`: Array of formation energy objects for every defect and charge state.

### step_03_transition_levels.json
- path: `/app/outputs/step_03_transition_levels.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic charge-state transition levels ε(q/q') in eV.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect`, `charge_transition`, `energy_eV`
    - `properties`:
      - `defect`:
        - `type`: string
      - `charge_transition`:
        - `type`: string
      - `energy_eV`:
        - `type`: number
  - `description`: Array of transition level objects for levels within the band gap.

### step_04_defect_hull.json
- path: `/app/outputs/step_04_defect_hull.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Convex hull of defect formation energies and charge-neutrality analysis.
- schema:
  - `type`: object
  - `required`: `Pb_rich`, `Br_rich`
  - `properties`:
    - `Pb_rich`:
      - `type`: object
      - `required`: `hull_defects`, `crossing_fermi_level_eV`, `dominant_charged_defects`
      - `properties`:
        - `hull_defects`:
          - `type`: array
          - `items`:
            - `type`: string
        - `crossing_fermi_level_eV`:
          - `type`: number
        - `dominant_charged_defects`:
          - `type`: object
          - `required`: `positive`, `negative`
          - `properties`:
            - `positive`:
              - `type`: string
            - `negative`:
              - `type`: string
    - `Br_rich`:
      - `type`: object
      - `required`: `hull_defects`, `crossing_fermi_level_eV`, `dominant_charged_defects`
      - `properties`:
        - `hull_defects`:
          - `type`: array
          - `items`:
            - `type`: string
        - `crossing_fermi_level_eV`:
          - `type`: number
        - `dominant_charged_defects`:
          - `type`: object
          - `required`: `positive`, `negative`
          - `properties`:
            - `positive`:
              - `type`: string
            - `negative`:
              - `type`: string
  - `description`: Defect hull data for Pb-rich and Br-rich chemical potential conditions.

Notes: All output files are JSON and adhere to the declared schemas. The checker compares reported values to hidden gold values within tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect",
            "charge",
            "total_energy_eV",
            "supercell_size"
          ],
          "properties": {
            "defect": {
              "type": "string"
            },
            "charge": {
              "type": "integer"
            },
            "total_energy_eV": {
              "type": "number"
            },
            "supercell_size": {
              "type": "integer"
            }
          }
        },
        "description": "Array of total energy objects for each supercell. Bulk entry uses defect='bulk' and charge=0."
      },
      "description": "DFT total energies for bulk and defect supercells."
    },
    {
      "file": "step_02_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect",
            "charge",
            "Ef_at_VBM_eV",
            "Ef_at_neutral_Pbrich_eV",
            "Ef_at_neutral_Brrich_eV"
          ],
          "properties": {
            "defect": {
              "type": "string"
            },
            "charge": {
              "type": "integer"
            },
            "Ef_at_VBM_eV": {
              "type": "number"
            },
            "Ef_at_neutral_Pbrich_eV": {
              "type": "number"
            },
            "Ef_at_neutral_Brrich_eV": {
              "type": "number"
            }
          }
        },
        "description": "Array of formation energy objects for every defect and charge state."
      },
      "description": "Defect formation energies computed from total energies and chemical potentials."
    },
    {
      "file": "step_03_transition_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect",
            "charge_transition",
            "energy_eV"
          ],
          "properties": {
            "defect": {
              "type": "string"
            },
            "charge_transition": {
              "type": "string"
            },
            "energy_eV": {
              "type": "number"
            }
          }
        },
        "description": "Array of transition level objects for levels within the band gap."
      },
      "description": "Thermodynamic charge-state transition levels ε(q/q') in eV."
    },
    {
      "file": "step_04_defect_hull.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Pb_rich",
          "Br_rich"
        ],
        "properties": {
          "Pb_rich": {
            "type": "object",
            "required": [
              "hull_defects",
              "crossing_fermi_level_eV",
              "dominant_charged_defects"
            ],
            "properties": {
              "hull_defects": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "crossing_fermi_level_eV": {
                "type": "number"
              },
              "dominant_charged_defects": {
                "type": "object",
                "required": [
                  "positive",
                  "negative"
                ],
                "properties": {
                  "positive": {
                    "type": "string"
                  },
                  "negative": {
                    "type": "string"
                  }
                }
              }
            }
          },
          "Br_rich": {
            "type": "object",
            "required": [
              "hull_defects",
              "crossing_fermi_level_eV",
              "dominant_charged_defects"
            ],
            "properties": {
              "hull_defects": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "crossing_fermi_level_eV": {
                "type": "number"
              },
              "dominant_charged_defects": {
                "type": "object",
                "required": [
                  "positive",
                  "negative"
                ],
                "properties": {
                  "positive": {
                    "type": "string"
                  },
                  "negative": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "description": "Defect hull data for Pb-rich and Br-rich chemical potential conditions."
      },
      "description": "Convex hull of defect formation energies and charge-neutrality analysis."
    }
  ],
  "notes": "All output files are JSON and adhere to the declared schemas. The checker compares reported values to hidden gold values within tolerances."
}
```

## How you are scored
A hidden verifier independently scores the JSON artifacts you produce for each workflow stage. For the scored steps, the verifier compares your reported defect formation energies, transition levels, and defect hull composition to hidden reference data extracted from the original study, using appropriate tolerances. Each correctly matched defect/charge combination earns credit. The final reward is the weighted fraction of matches across all scored outputs. Simply reporting a number without executing the underlying computation will not yield a passing score.
