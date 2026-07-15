# Molecular-Dynamics Simulations of Defect Formation in a-Si:H

## Problem background
Hydrogenated amorphous silicon (a-Si:H) is a key material for thin-film photovoltaics, but its efficiency degrades under prolonged illumination (the Staebler-Wronski effect). The microscopic mechanism is debated; one prominent proposal is that nonradiative recombination of photoexcited carriers breaks weak Si-Si bonds, generating metastable dangling-bond defects. The stability of such defects may depend on the local hydrogen bonding — monohydride (SiH) versus dihydride (SiH₂) configurations. Understanding which network type is more susceptible to light-induced defect formation is critical for designing better materials.

This task investigates, via classical molecular-dynamics simulations, whether a monohydride-only a-Si:H network remains defect-free under localized energy excitations while a network containing both monohydride and dihydride species can develop metastable dangling-bond defects, and quantifies the associated energy differences, annealing barriers, and electronic signatures.

## Approach
The work employs classical molecular dynamics with empirical interatomic potentials to describe Si-Si, Si-H, and H-H interactions. The strategy is:
- Implement the potentials: a two- and three-body Si-H potential that captures bond-breaking and re-bonding, the Biswas-Hamann Si-Si potential, and a repulsive H-H term.
- Construct two defect-free a-Si:H networks: Model1 (54 Si + 6 H, monohydride only) and Model2 (54 Si + 14 H, mixed monohydride and dihydride species) via bond saturation and steepest-descent relaxation.
- Simulate nonradiative recombination events as localized kinetic-energy excitations (velocity boosts) applied to specific atom pairs at temperatures around 300 K, with energies ranging up to 7.0 eV.
- Monitor structural evolution: track bond distances, detect dangling bonds, and, for configurations that produce defects, compute energy differences between initial and final relaxed states plus thermal annealing barriers.
- Compute the electronic density of states using an empirical tight-binding model with established Si-Si and Si-H parameters, comparing the initial defect-free configuration with a defect configuration to check for mid-gap states.

By contrasting Model1 and Model2 under identical excitation protocols, the task examines how hydrogen bonding influences network stability and defect formation.

## Reproduction target
Produce a set of scored artifacts that quantify the structural properties and defect behavior of the two a-Si:H network models:
- Structural properties (pair-correlation functions, rms bond-angle deviation, average Si-H bond length, mass density) for both relaxed models (Model1 and Model2).
- A stability verdict for Model1: determine whether any localized excitation (1.7–7.0 eV) creates dangling bonds or lasting structural changes.
- Defect formation metrics for two specific bond‑breaking events in Model2 (atoms 49‑50 and 32‑54): energy difference between initial and defect configurations, annealing barrier, and number of dangling bonds created.
- Electronic density of states for Model2: compute the band gap of the initial defect‑free configuration and verify whether mid‑gap states emerge in a defect configuration.

## Assets

- Biswas-Hamann Si-Si interatomic potential: 10.1103/PhysRevB.36.6434
- Guttman-Fong a-Si:H network coordinates: 10.1103/PhysRevB.26.6756
- Min et al. Si-H tight-binding parameters
- Chadi Si-Si tight-binding parameters: 10.1103/PhysRevLett.41.1062

## Workflow steps

### Step 1: Implement interatomic potentials
- Role: process
- Action: Implement the Si-H two-body potential with exponential terms and smooth cutoff, the three-body potential with Keating angular form and radial cutoffs, the repulsive H-H two-body potential, and the Biswas-Hamann Si-Si two- and three-body potentials. The agent may use any programming language or open-source MD engine.
- Evidence: `/app/outputs/potential_implementation_test.log`

### Step 2: Construct and relax a-Si:H network models
- Role: process
- Action: From the Guttman-Fong initial configurations (or by following the saturation procedure) build Model1 (54 Si + 6 H, monohydride only) and Model2 (54 Si + 14 H, mixed mono/dihydride). Perform steepest-descent relaxation to find minimum-energy defect-free configurations, allowing density to vary, using the implemented potentials.
- Evidence: `/app/outputs/model_relaxation.log`

### Step 3: Structural properties of Model1
- Role: scored
- Action: From the relaxed Model1, compute Si-Si and Si-H pair-correlation functions g(r), RMS bond-angle deviation, average Si-H bond length, and mass density relative to crystalline Si. Write the computed properties to model1_structural_properties.json.
- Output file: `/app/outputs/model1_structural_properties.json`
- Format: json
- Contract: {"Si-Si_pair_corr": [[r, g], ...], "Si-H_pair_corr": [[r, g], ...], "rms_bond_angle_deviation_degrees": float, "average_Si-H_bond_length_A": float, "mass_density_relative_to_cSi": float}
- Scoring: scored by hidden verifier

### Step 4: Structural properties of Model2
- Role: scored
- Action: From the relaxed Model2, compute Si-Si and Si-H pair-correlation functions g(r), RMS bond-angle deviation, average Si-H bond length, and mass density relative to crystalline Si. Write the computed properties to model2_structural_properties.json.
- Output file: `/app/outputs/model2_structural_properties.json`
- Format: json
- Contract: {"Si-Si_pair_corr": [[r, g], ...], "Si-H_pair_corr": [[r, g], ...], "rms_bond_angle_deviation_degrees": float, "average_Si-H_bond_length_A": float, "mass_density_relative_to_cSi": float}
- Scoring: scored by hidden verifier

### Step 5: MD excitations on Model1
- Role: process
- Action: Run molecular dynamics simulations at ~300 K on Model1. Apply localized kinetic-energy excitations (1.7–7.0 eV) to several Si-Si bonds (including bonds 40-41, 42-48, 42-43, 42-7). Evolve each excitation for at least 9 ps and monitor bond distances and structural changes.
- Evidence: `/app/outputs/model1_excitation.log`

### Step 6: Model1 defect-stability summary
- Role: scored (load-bearing)
- Action: Examine the final configurations from all Model1 excitations. Determine whether any excitation created dangling bonds or lasting structural changes. Write the outcome to model1_defect_outcome.json, stating that the monohydride model is stable under excitations up to 7.0 eV.
- Output file: `/app/outputs/model1_defect_outcome.json`
- Format: json
- Contract: {"excitation_energies_eV": [float], "dangling_bonds_created": false, "structural_changes": "none"}
- Scoring: scored by hidden verifier

### Step 7: MD excitations on Model2
- Role: process
- Action: Run MD simulations at ~300 K on Model2. Apply a 1.7 eV excitation along the bond direction to atom pairs 49-50 and 32-54 separately. Evolve each for at least 12–13 ps, monitor bond distances, and obtain the excited final configurations.
- Evidence: `/app/outputs/model2_excitation.log`

### Step 8: Defect analysis: excitation 49-50
- Role: scored (load-bearing)
- Action: From the final configuration after exciting atoms 49-50, perform steepest-descent relaxation and compute the energy difference ΔE relative to the initial configuration. Count the number of dangling bonds created. Perform thermal annealing at temperatures ~270–560 K to estimate the annealing energy barrier E_b. Write results to model2_excitation_49_50_defect.json.
- Output file: `/app/outputs/model2_excitation_49_50_defect.json`
- Format: json
- Contract: {"final_49_50_distance_A": float, "energy_difference_eV": float, "annealing_barrier_eV": float, "number_of_dangling_bonds": int}
- Scoring: scored by hidden verifier

### Step 9: Defect analysis: excitation 32-54
- Role: scored (load-bearing)
- Action: From the final configuration after exciting atoms 32-54, perform steepest-descent relaxation and compute ΔE, count dangling bonds, and perform thermal annealing at room temperature to obtain the annealing barrier. Write results to model2_excitation_32_54_defect.json.
- Output file: `/app/outputs/model2_excitation_32_54_defect.json`
- Format: json
- Contract: {"energy_difference_eV": float, "annealing_barrier_eV": float, "number_of_dangling_bonds": int}
- Scoring: scored by hidden verifier

### Step 10: Electronic density of states for Model2 defect configuration
- Role: scored
- Action: Using empirical tight-binding with Si-H parameters from Min et al. and Si-Si parameters from Chadi, compute the electronic density of states (DOS) for the initial defect-free Model2 configuration and for a defect configuration (e.g., after 49-50 excitation). Determine the band gap of the initial configuration and whether mid-gap states appear in the defect configuration. Write the DOS arrays and diagnostic flags to model2_defect_dos.json.
- Output file: `/app/outputs/model2_defect_dos.json`
- Format: json
- Contract: {"initial_gap_eV": float, "defect_gap_states_present": bool, "DOS_energy_values": [float], "DOS_initial": [float], "DOS_defect": [float]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model1_structural_properties.json`
- `/app/outputs/model2_structural_properties.json`
- `/app/outputs/model1_defect_outcome.json`
- `/app/outputs/model2_excitation_49_50_defect.json`
- `/app/outputs/model2_excitation_32_54_defect.json`
- `/app/outputs/model2_defect_dos.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model1_structural_properties.json
- path: `/app/outputs/model1_structural_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural properties of the monohydride-only a-Si:H network model.
- schema:
  - `type`: object
  - `required`: `Si-Si_pair_corr`, `Si-H_pair_corr`, `rms_bond_angle_deviation_degrees`, `average_Si-H_bond_length_A`, `mass_density_relative_to_cSi`
  - `properties`:
    - `Si-Si_pair_corr`:
      - `type`: array
      - `items`:
        - `type`: array
        - `items`:
          - `type`: number
    - `Si-H_pair_corr`:
      - `type`: array
      - `items`:
        - `type`: array
        - `items`:
          - `type`: number
    - `rms_bond_angle_deviation_degrees`:
      - `type`: number
      - `unit`: degree
    - `average_Si-H_bond_length_A`:
      - `type`: number
      - `unit`: angstrom
    - `mass_density_relative_to_cSi`:
      - `type`: number
      - `unit`: ratio

### model2_structural_properties.json
- path: `/app/outputs/model2_structural_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural properties of the a-Si:H network model containing both monohydride and dihydride species.
- schema:
  - `type`: object
  - `required`: `Si-Si_pair_corr`, `Si-H_pair_corr`, `rms_bond_angle_deviation_degrees`, `average_Si-H_bond_length_A`, `mass_density_relative_to_cSi`
  - `properties`:
    - `Si-Si_pair_corr`:
      - `type`: array
      - `items`:
        - `type`: array
        - `items`:
          - `type`: number
    - `Si-H_pair_corr`:
      - `type`: array
      - `items`:
        - `type`: array
        - `items`:
          - `type`: number
    - `rms_bond_angle_deviation_degrees`:
      - `type`: number
      - `unit`: degree
    - `average_Si-H_bond_length_A`:
      - `type`: number
      - `unit`: angstrom
    - `mass_density_relative_to_cSi`:
      - `type`: number
      - `unit`: ratio

### model1_defect_outcome.json
- path: `/app/outputs/model1_defect_outcome.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Stability verdict for the monohydride model under localized excitations up to 7.0 eV.
- schema:
  - `type`: object
  - `required`: `excitation_energies_eV`, `dangling_bonds_created`, `structural_changes`
  - `properties`:
    - `excitation_energies_eV`:
      - `type`: array
      - `items`:
        - `type`: number
    - `dangling_bonds_created`:
      - `type`: boolean
    - `structural_changes`:
      - `type`: string

### model2_excitation_49_50_defect.json
- path: `/app/outputs/model2_excitation_49_50_defect.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Defect formation metrics for the 49-50 bond-breaking event in the dihydride-containing model.
- schema:
  - `type`: object
  - `required`: `final_49_50_distance_A`, `energy_difference_eV`, `annealing_barrier_eV`, `number_of_dangling_bonds`
  - `properties`:
    - `final_49_50_distance_A`:
      - `type`: number
      - `unit`: angstrom
    - `energy_difference_eV`:
      - `type`: number
      - `unit`: eV
    - `annealing_barrier_eV`:
      - `type`: number
      - `unit`: eV
    - `number_of_dangling_bonds`:
      - `type`: integer

### model2_excitation_32_54_defect.json
- path: `/app/outputs/model2_excitation_32_54_defect.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Defect formation metrics for the 32-54 bond-breaking event in the dihydride-containing model.
- schema:
  - `type`: object
  - `required`: `energy_difference_eV`, `annealing_barrier_eV`, `number_of_dangling_bonds`
  - `properties`:
    - `energy_difference_eV`:
      - `type`: number
      - `unit`: eV
    - `annealing_barrier_eV`:
      - `type`: number
      - `unit`: eV
    - `number_of_dangling_bonds`:
      - `type`: integer

### model2_defect_dos.json
- path: `/app/outputs/model2_defect_dos.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic density of states for initial and defect configurations of the dihydride-containing model, showing mid-gap states.
- schema:
  - `type`: object
  - `required`: `initial_gap_eV`, `defect_gap_states_present`, `DOS_energy_values`, `DOS_initial`, `DOS_defect`
  - `properties`:
    - `initial_gap_eV`:
      - `type`: number
      - `unit`: eV
    - `defect_gap_states_present`:
      - `type`: boolean
    - `DOS_energy_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `DOS_initial`:
      - `type`: array
      - `items`:
        - `type`: number
    - `DOS_defect`:
      - `type`: array
      - `items`:
        - `type`: number

Notes: All outputs are JSON files. The structural properties and defect metrics are compared to paper values with appropriate tolerances. The DOS arrays are audited for the presence of mid-gap states and approximate gap magnitude.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model1_structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Si-Si_pair_corr",
          "Si-H_pair_corr",
          "rms_bond_angle_deviation_degrees",
          "average_Si-H_bond_length_A",
          "mass_density_relative_to_cSi"
        ],
        "properties": {
          "Si-Si_pair_corr": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          },
          "Si-H_pair_corr": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          },
          "rms_bond_angle_deviation_degrees": {
            "type": "number",
            "unit": "degree"
          },
          "average_Si-H_bond_length_A": {
            "type": "number",
            "unit": "angstrom"
          },
          "mass_density_relative_to_cSi": {
            "type": "number",
            "unit": "ratio"
          }
        }
      },
      "description": "Structural properties of the monohydride-only a-Si:H network model."
    },
    {
      "file": "model2_structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Si-Si_pair_corr",
          "Si-H_pair_corr",
          "rms_bond_angle_deviation_degrees",
          "average_Si-H_bond_length_A",
          "mass_density_relative_to_cSi"
        ],
        "properties": {
          "Si-Si_pair_corr": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          },
          "Si-H_pair_corr": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          },
          "rms_bond_angle_deviation_degrees": {
            "type": "number",
            "unit": "degree"
          },
          "average_Si-H_bond_length_A": {
            "type": "number",
            "unit": "angstrom"
          },
          "mass_density_relative_to_cSi": {
            "type": "number",
            "unit": "ratio"
          }
        }
      },
      "description": "Structural properties of the a-Si:H network model containing both monohydride and dihydride species."
    },
    {
      "file": "model1_defect_outcome.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "excitation_energies_eV",
          "dangling_bonds_created",
          "structural_changes"
        ],
        "properties": {
          "excitation_energies_eV": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "dangling_bonds_created": {
            "type": "boolean"
          },
          "structural_changes": {
            "type": "string"
          }
        }
      },
      "description": "Stability verdict for the monohydride model under localized excitations up to 7.0 eV."
    },
    {
      "file": "model2_excitation_49_50_defect.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "final_49_50_distance_A",
          "energy_difference_eV",
          "annealing_barrier_eV",
          "number_of_dangling_bonds"
        ],
        "properties": {
          "final_49_50_distance_A": {
            "type": "number",
            "unit": "angstrom"
          },
          "energy_difference_eV": {
            "type": "number",
            "unit": "eV"
          },
          "annealing_barrier_eV": {
            "type": "number",
            "unit": "eV"
          },
          "number_of_dangling_bonds": {
            "type": "integer"
          }
        }
      },
      "description": "Defect formation metrics for the 49-50 bond-breaking event in the dihydride-containing model."
    },
    {
      "file": "model2_excitation_32_54_defect.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "energy_difference_eV",
          "annealing_barrier_eV",
          "number_of_dangling_bonds"
        ],
        "properties": {
          "energy_difference_eV": {
            "type": "number",
            "unit": "eV"
          },
          "annealing_barrier_eV": {
            "type": "number",
            "unit": "eV"
          },
          "number_of_dangling_bonds": {
            "type": "integer"
          }
        }
      },
      "description": "Defect formation metrics for the 32-54 bond-breaking event in the dihydride-containing model."
    },
    {
      "file": "model2_defect_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "initial_gap_eV",
          "defect_gap_states_present",
          "DOS_energy_values",
          "DOS_initial",
          "DOS_defect"
        ],
        "properties": {
          "initial_gap_eV": {
            "type": "number",
            "unit": "eV"
          },
          "defect_gap_states_present": {
            "type": "boolean"
          },
          "DOS_energy_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "DOS_initial": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "DOS_defect": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "Electronic density of states for initial and defect configurations of the dihydride-containing model, showing mid-gap states."
    }
  ],
  "notes": "All outputs are JSON files. The structural properties and defect metrics are compared to paper values with appropriate tolerances. The DOS arrays are audited for the presence of mid-gap states and approximate gap magnitude."
}
```

## How you are scored
A hidden verifier compares the contents of each output file (model1_structural_properties.json, model2_structural_properties.json, model1_defect_outcome.json, model2_excitation_49_50_defect.json, model2_excitation_32_54_defect.json, model2_defect_dos.json) against reference values derived from the original study, using tolerances that allow for legitimate implementation differences. The overall reward is a weighted combination of stage-specific scores, with the defect analysis and electronic DOS stages carrying the largest weight. Merely reporting numbers without executing the molecular-dynamics pipeline will fail the structural checks applied by the verifier. The verifier does not run the heavy MD or tight‑binding computations; it audits the submitted artifacts.
