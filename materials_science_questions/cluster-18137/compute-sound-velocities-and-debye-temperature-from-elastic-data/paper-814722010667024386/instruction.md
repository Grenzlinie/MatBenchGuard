# First-principles calculation of elastic properties and Debye temperatures for Pb-Ba intermetallic compounds

## Problem background
Pb-Ba intermetallic compounds are potential materials for thermoelectric and optoelectronic applications. Density functional theory (DFT) can predict their ground-state physical properties such as phase stability, elastic moduli, Debye temperatures, and electronic structure, yet systematic first-principles investigations for the five experimentally known compounds – BaPb₃, Ba₃Pb₅, BaPb, Ba₅Pb₃, and Ba₂Pb – are incomplete. This task aims to compute these fundamental properties using DFT with the LDA CA-PZ exchange-correlation functional and ultrasoft pseudopotentials, providing quantitative insights into their stability and mechanical/electronic behaviour.

## Approach
Use density functional theory within the local-density approximation (CA-PZ functional) together with ultrasoft pseudopotentials for Pb and Ba. First, perform geometry optimizations of the five Pb-Ba intermetallic compounds as well as the elemental bulk phases fcc Pb (experimental structure) and bcc Ba (experimental structure), starting from the crystal structures provided in the task (lattice parameters and Wyckoff positions from the literature).

From the optimized total energies compute the formation enthalpies per atom for each compound using the formula ΔH(BaₓPbᵧ) = [E_total(BaₓPbᵧ) − x·E(Ba_bulk) − y·E(Pb_bulk)] / (x+y).

Apply strain perturbations to the optimized cells according to the patterns appropriate for each crystal system (trigonal, orthorhombic, tetragonal) and fit the resulting energy vs strain data to obtain the full set of independent elastic constants Cᵢⱼ.

Derive the isotropic polycrystalline elastic moduli – bulk modulus B, shear modulus G, Young's modulus E, and Poisson's ratio ν – by Voigt-Reuss-Hill averaging. Using the optimized cell volume and composition, calculate the density ρ; then compute the longitudinal (vₗ) and transverse (vₜ) sound velocities, the average sound velocity v_m, and finally the Debye temperature Θ_D via the standard relations Θ_D = (h/k) · (3n N_A ρ / (4π M))^(1/3) · v_m, where h and k are Planck and Boltzmann constants, N_A is Avogadro's number, n the number of atoms per formula unit, and M the molecular weight.

Calculate the electronic band structure and the total and partial density of states (DOS) for each compound. For Ba₂Pb, identify the direct band gap from the band structure. Integrate the total DOS in the energy window from −4 eV to the Fermi level to obtain the bonding electron number per atom for each compound.

Assemble all computed quantities into a single JSON file, and order the compounds from most negative to least negative formation enthalpy.

## Reproduction target
For each of the five Pb-Ba intermetallic compounds (BaPb₃, Ba₃Pb₅, BaPb, Ba₅Pb₃, Ba₂Pb) compute and report:
- formation enthalpy (kJ/mol)
- isotropic polycrystalline elastic moduli: bulk modulus, shear modulus, Young's modulus, Poisson's ratio
- Debye temperature (K)
- bonding electron number per atom

Additionally, report the direct band gap (eV) of Ba₂Pb, and list the compounds in order of most negative to least negative formation enthalpy (stability ordering). All values must be written to the scored JSON artifact `results.json` following the specified schema.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code with LDA CA-PZ functional and ultrasoft pseudopotentials): https://www.quantum-espresso.org/
- LDA ultrasoft pseudopotentials for Pb and Ba: https://www.materialscloud.org/discover/sssp/table/efficiency
- Experimental crystal structures of Pb-Ba intermetallic compounds

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for all five Pb-Ba intermetallic compounds (BaPb3, Ba3Pb5, BaPb, Ba5Pb3, Ba2Pb) and for pure Pb and Ba, using the LDA CA-PZ functional and ultrasoft pseudopotentials. Start from the experimental crystal structures provided in the task instructions. Obtain optimized lattice parameters and total energies.
- Evidence: `/app/outputs/step_01_geometry_opt.log`

### Step 2: Elastic constant calculation
- Role: process
- Action: Apply strain perturbations to the optimized structures of each compound and perform DFT total-energy calculations. Extract the elastic constants C_ij from the energy versus strain data, using the strain patterns appropriate for each crystal system (trigonal, orthorhombic, tetragonal).
- Evidence: `/app/outputs/step_02_elastic_constants.log`

### Step 3: Electronic structure calculation
- Role: process
- Action: Calculate the band structure and total and partial density of states (DOS) for each compound. For Ba2Pb, determine the direct band gap from the band structure. Integrate the total DOS below the Fermi level over the energy range -4 eV to 0 eV to obtain the bonding electron numbers per atom.
- Evidence: `/app/outputs/step_03_electronic_structure.log`

### Step 4: Compute final properties
- Role: scored (load-bearing)
- Action: From the total energies of optimized compounds and elements, compute formation enthalpies per atom. Using the elastic constants, derive isotropic polycrystalline moduli (bulk B, shear G, Young's E, Poisson's ν) via Voigt-Reuss-Hill averaging. Compute the density from the optimized volume and composition; then calculate sound velocities and the Debye temperature. Assemble all results, together with bonding electron numbers and the Ba2Pb band gap, into a JSON file. List the compounds in order of most negative to least negative formation enthalpy.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys for each compound ('BaPb3', 'Ba3Pb5', 'BaPb', 'Ba5Pb3', 'Ba2Pb'). Each key maps to an object containing numeric fields: 'formation_enthalpy' (kJ/mol), 'bulk_modulus' (GPa), 'shear_modulus' (GPa), 'youngs_modulus' (GPa), 'poissons_ratio' (dimensionless), 'debye_temperature' (K), 'bonding_electron_number' (dimensionless). Top-level field 'Ba2Pb_band_gap' (eV) giving the band gap. Top-level list 'stability_order' with compound names from most negative formation enthalpy to least negative.
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
- description: The main checkable artifact containing the reproduced formation enthalpies, polycrystalline elastic moduli, Debye temperatures, bonding electron numbers, Vickers hardness, elastic anisotropy indexes, Ba2Pb band gap, and stability ordering.
- schema:
  - `type`: object
  - `properties`:
    - `BaPb3`:
      - `type`: object
      - `required`: `formation_enthalpy`, `bulk_modulus`, `shear_modulus`, `youngs_modulus`, `poissons_ratio`, `debye_temperature`, `bonding_electron_number`, `hardness`, `anisotropy`
      - `properties`:
        - `formation_enthalpy`:
          - `type`: number
          - `unit`: kJ/mol
        - `bulk_modulus`:
          - `type`: number
          - `unit`: GPa
        - `shear_modulus`:
          - `type`: number
          - `unit`: GPa
        - `youngs_modulus`:
          - `type`: number
          - `unit`: GPa
        - `poissons_ratio`:
          - `type`: number
          - `unit`: dimensionless
        - `debye_temperature`:
          - `type`: number
          - `unit`: K
        - `bonding_electron_number`:
          - `type`: number
          - `unit`: dimensionless
        - `hardness`:
          - `type`: number
          - `unit`: GPa
        - `anisotropy`:
          - `type`: object
          - `required`: `A_U`, `A_B`, `A_G`, `A1`, `A2`, `A3`
          - `properties`:
            - `A_U`:
              - `type`: number
              - `unit`: dimensionless
            - `A_B`:
              - `type`: number
              - `unit`: dimensionless
            - `A_G`:
              - `type`: number
              - `unit`: dimensionless
            - `A1`:
              - `type`: number
              - `unit`: dimensionless
            - `A2`:
              - `type`: number
              - `unit`: dimensionless
            - `A3`:
              - `type`: number
              - `unit`: dimensionless
    - `Ba3Pb5`:
      - `type`: object
      - `required`: `formation_enthalpy`, `bulk_modulus`, `shear_modulus`, `youngs_modulus`, `poissons_ratio`, `debye_temperature`, `bonding_electron_number`, `hardness`, `anisotropy`
      - `properties`:
        - `formation_enthalpy`:
          - `type`: number
          - `unit`: kJ/mol
        - `bulk_modulus`:
          - `type`: number
          - `unit`: GPa
        - `shear_modulus`:
          - `type`: number
          - `unit`: GPa
        - `youngs_modulus`:
          - `type`: number
          - `unit`: GPa
        - `poissons_ratio`:
          - `type`: number
          - `unit`: dimensionless
        - `debye_temperature`:
          - `type`: number
          - `unit`: K
        - `bonding_electron_number`:
          - `type`: number
          - `unit`: dimensionless
        - `hardness`:
          - `type`: number
          - `unit`: GPa
        - `anisotropy`:
          - `type`: object
          - `required`: `A_U`, `A_B`, `A_G`, `A1`, `A2`, `A3`
          - `properties`:
            - `A_U`:
              - `type`: number
              - `unit`: dimensionless
            - `A_B`:
              - `type`: number
              - `unit`: dimensionless
            - `A_G`:
              - `type`: number
              - `unit`: dimensionless
            - `A1`:
              - `type`: number
              - `unit`: dimensionless
            - `A2`:
              - `type`: number
              - `unit`: dimensionless
            - `A3`:
              - `type`: number
              - `unit`: dimensionless
    - `BaPb`:
      - `type`: object
      - `required`: `formation_enthalpy`, `bulk_modulus`, `shear_modulus`, `youngs_modulus`, `poissons_ratio`, `debye_temperature`, `bonding_electron_number`, `hardness`, `anisotropy`
      - `properties`:
        - `formation_enthalpy`:
          - `type`: number
          - `unit`: kJ/mol
        - `bulk_modulus`:
          - `type`: number
          - `unit`: GPa
        - `shear_modulus`:
          - `type`: number
          - `unit`: GPa
        - `youngs_modulus`:
          - `type`: number
          - `unit`: GPa
        - `poissons_ratio`:
          - `type`: number
          - `unit`: dimensionless
        - `debye_temperature`:
          - `type`: number
          - `unit`: K
        - `bonding_electron_number`:
          - `type`: number
          - `unit`: dimensionless
        - `hardness`:
          - `type`: number
          - `unit`: GPa
        - `anisotropy`:
          - `type`: object
          - `required`: `A_U`, `A_B`, `A_G`, `A1`, `A2`, `A3`
          - `properties`:
            - `A_U`:
              - `type`: number
              - `unit`: dimensionless
            - `A_B`:
              - `type`: number
              - `unit`: dimensionless
            - `A_G`:
              - `type`: number
              - `unit`: dimensionless
            - `A1`:
              - `type`: number
              - `unit`: dimensionless
            - `A2`:
              - `type`: number
              - `unit`: dimensionless
            - `A3`:
              - `type`: number
              - `unit`: dimensionless
    - `Ba5Pb3`:
      - `type`: object
      - `required`: `formation_enthalpy`, `bulk_modulus`, `shear_modulus`, `youngs_modulus`, `poissons_ratio`, `debye_temperature`, `bonding_electron_number`, `hardness`, `anisotropy`
      - `properties`:
        - `formation_enthalpy`:
          - `type`: number
          - `unit`: kJ/mol
        - `bulk_modulus`:
          - `type`: number
          - `unit`: GPa
        - `shear_modulus`:
          - `type`: number
          - `unit`: GPa
        - `youngs_modulus`:
          - `type`: number
          - `unit`: GPa
        - `poissons_ratio`:
          - `type`: number
          - `unit`: dimensionless
        - `debye_temperature`:
          - `type`: number
          - `unit`: K
        - `bonding_electron_number`:
          - `type`: number
          - `unit`: dimensionless
        - `hardness`:
          - `type`: number
          - `unit`: GPa
        - `anisotropy`:
          - `type`: object
          - `required`: `A_U`, `A_B`, `A_G`, `A1`, `A2`, `A3`
          - `properties`:
            - `A_U`:
              - `type`: number
              - `unit`: dimensionless
            - `A_B`:
              - `type`: number
              - `unit`: dimensionless
            - `A_G`:
              - `type`: number
              - `unit`: dimensionless
            - `A1`:
              - `type`: number
              - `unit`: dimensionless
            - `A2`:
              - `type`: number
              - `unit`: dimensionless
            - `A3`:
              - `type`: number
              - `unit`: dimensionless
    - `Ba2Pb`:
      - `type`: object
      - `required`: `formation_enthalpy`, `bulk_modulus`, `shear_modulus`, `youngs_modulus`, `poissons_ratio`, `debye_temperature`, `bonding_electron_number`, `hardness`, `anisotropy`
      - `properties`:
        - `formation_enthalpy`:
          - `type`: number
          - `unit`: kJ/mol
        - `bulk_modulus`:
          - `type`: number
          - `unit`: GPa
        - `shear_modulus`:
          - `type`: number
          - `unit`: GPa
        - `youngs_modulus`:
          - `type`: number
          - `unit`: GPa
        - `poissons_ratio`:
          - `type`: number
          - `unit`: dimensionless
        - `debye_temperature`:
          - `type`: number
          - `unit`: K
        - `bonding_electron_number`:
          - `type`: number
          - `unit`: dimensionless
        - `hardness`:
          - `type`: number
          - `unit`: GPa
        - `anisotropy`:
          - `type`: object
          - `required`: `A_U`, `A_B`, `A_G`, `A1`, `A2`, `A3`
          - `properties`:
            - `A_U`:
              - `type`: number
              - `unit`: dimensionless
            - `A_B`:
              - `type`: number
              - `unit`: dimensionless
            - `A_G`:
              - `type`: number
              - `unit`: dimensionless
            - `A1`:
              - `type`: number
              - `unit`: dimensionless
            - `A2`:
              - `type`: number
              - `unit`: dimensionless
            - `A3`:
              - `type`: number
              - `unit`: dimensionless
    - `Ba2Pb_band_gap`:
      - `type`: number
      - `unit`: eV
    - `stability_order`:
      - `type`: array
      - `items`:
        - `type`: string
  - `required`: `BaPb3`, `Ba3Pb5`, `BaPb`, `Ba5Pb3`, `Ba2Pb`, `Ba2Pb_band_gap`, `stability_order`

Notes: All numerical values are referenced against paper-reported values with tolerances that account for method-dependent variations in DFT implementations. Hardness and anisotropy fields are now embedded within each compound's object, keeping a single scored file.

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
          "BaPb3": {
            "type": "object",
            "required": [
              "formation_enthalpy",
              "bulk_modulus",
              "shear_modulus",
              "youngs_modulus",
              "poissons_ratio",
              "debye_temperature",
              "bonding_electron_number",
              "hardness",
              "anisotropy"
            ],
            "properties": {
              "formation_enthalpy": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "bulk_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "shear_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "youngs_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "poissons_ratio": {
                "type": "number",
                "unit": "dimensionless"
              },
              "debye_temperature": {
                "type": "number",
                "unit": "K"
              },
              "bonding_electron_number": {
                "type": "number",
                "unit": "dimensionless"
              },
              "hardness": {
                "type": "number",
                "unit": "GPa"
              },
              "anisotropy": {
                "type": "object",
                "required": [
                  "A_U",
                  "A_B",
                  "A_G",
                  "A1",
                  "A2",
                  "A3"
                ],
                "properties": {
                  "A_U": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_B": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_G": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A1": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A2": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A3": {
                    "type": "number",
                    "unit": "dimensionless"
                  }
                }
              }
            }
          },
          "Ba3Pb5": {
            "type": "object",
            "required": [
              "formation_enthalpy",
              "bulk_modulus",
              "shear_modulus",
              "youngs_modulus",
              "poissons_ratio",
              "debye_temperature",
              "bonding_electron_number",
              "hardness",
              "anisotropy"
            ],
            "properties": {
              "formation_enthalpy": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "bulk_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "shear_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "youngs_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "poissons_ratio": {
                "type": "number",
                "unit": "dimensionless"
              },
              "debye_temperature": {
                "type": "number",
                "unit": "K"
              },
              "bonding_electron_number": {
                "type": "number",
                "unit": "dimensionless"
              },
              "hardness": {
                "type": "number",
                "unit": "GPa"
              },
              "anisotropy": {
                "type": "object",
                "required": [
                  "A_U",
                  "A_B",
                  "A_G",
                  "A1",
                  "A2",
                  "A3"
                ],
                "properties": {
                  "A_U": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_B": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_G": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A1": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A2": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A3": {
                    "type": "number",
                    "unit": "dimensionless"
                  }
                }
              }
            }
          },
          "BaPb": {
            "type": "object",
            "required": [
              "formation_enthalpy",
              "bulk_modulus",
              "shear_modulus",
              "youngs_modulus",
              "poissons_ratio",
              "debye_temperature",
              "bonding_electron_number",
              "hardness",
              "anisotropy"
            ],
            "properties": {
              "formation_enthalpy": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "bulk_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "shear_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "youngs_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "poissons_ratio": {
                "type": "number",
                "unit": "dimensionless"
              },
              "debye_temperature": {
                "type": "number",
                "unit": "K"
              },
              "bonding_electron_number": {
                "type": "number",
                "unit": "dimensionless"
              },
              "hardness": {
                "type": "number",
                "unit": "GPa"
              },
              "anisotropy": {
                "type": "object",
                "required": [
                  "A_U",
                  "A_B",
                  "A_G",
                  "A1",
                  "A2",
                  "A3"
                ],
                "properties": {
                  "A_U": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_B": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_G": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A1": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A2": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A3": {
                    "type": "number",
                    "unit": "dimensionless"
                  }
                }
              }
            }
          },
          "Ba5Pb3": {
            "type": "object",
            "required": [
              "formation_enthalpy",
              "bulk_modulus",
              "shear_modulus",
              "youngs_modulus",
              "poissons_ratio",
              "debye_temperature",
              "bonding_electron_number",
              "hardness",
              "anisotropy"
            ],
            "properties": {
              "formation_enthalpy": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "bulk_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "shear_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "youngs_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "poissons_ratio": {
                "type": "number",
                "unit": "dimensionless"
              },
              "debye_temperature": {
                "type": "number",
                "unit": "K"
              },
              "bonding_electron_number": {
                "type": "number",
                "unit": "dimensionless"
              },
              "hardness": {
                "type": "number",
                "unit": "GPa"
              },
              "anisotropy": {
                "type": "object",
                "required": [
                  "A_U",
                  "A_B",
                  "A_G",
                  "A1",
                  "A2",
                  "A3"
                ],
                "properties": {
                  "A_U": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_B": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_G": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A1": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A2": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A3": {
                    "type": "number",
                    "unit": "dimensionless"
                  }
                }
              }
            }
          },
          "Ba2Pb": {
            "type": "object",
            "required": [
              "formation_enthalpy",
              "bulk_modulus",
              "shear_modulus",
              "youngs_modulus",
              "poissons_ratio",
              "debye_temperature",
              "bonding_electron_number",
              "hardness",
              "anisotropy"
            ],
            "properties": {
              "formation_enthalpy": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "bulk_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "shear_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "youngs_modulus": {
                "type": "number",
                "unit": "GPa"
              },
              "poissons_ratio": {
                "type": "number",
                "unit": "dimensionless"
              },
              "debye_temperature": {
                "type": "number",
                "unit": "K"
              },
              "bonding_electron_number": {
                "type": "number",
                "unit": "dimensionless"
              },
              "hardness": {
                "type": "number",
                "unit": "GPa"
              },
              "anisotropy": {
                "type": "object",
                "required": [
                  "A_U",
                  "A_B",
                  "A_G",
                  "A1",
                  "A2",
                  "A3"
                ],
                "properties": {
                  "A_U": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_B": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A_G": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A1": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A2": {
                    "type": "number",
                    "unit": "dimensionless"
                  },
                  "A3": {
                    "type": "number",
                    "unit": "dimensionless"
                  }
                }
              }
            }
          },
          "Ba2Pb_band_gap": {
            "type": "number",
            "unit": "eV"
          },
          "stability_order": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "BaPb3",
          "Ba3Pb5",
          "BaPb",
          "Ba5Pb3",
          "Ba2Pb",
          "Ba2Pb_band_gap",
          "stability_order"
        ]
      },
      "description": "The main checkable artifact containing the reproduced formation enthalpies, polycrystalline elastic moduli, Debye temperatures, bonding electron numbers, Vickers hardness, elastic anisotropy indexes, Ba2Pb band gap, and stability ordering."
    }
  ],
  "notes": "All numerical values are referenced against paper-reported values with tolerances that account for method-dependent variations in DFT implementations. Hardness and anisotropy fields are now embedded within each compound's object, keeping a single scored file."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares each reported numeric quantity to independently determined reference values using appropriate tolerances that account for legitimate between-code variations. The verifier also checks that the `stability_order` array lists the compounds from most negative to least negative formation enthalpy. The reward is based on the fraction of quantities within the allowed tolerances and on the correctness of the ordering; meeting or exceeding the reference performance (e.g., a more negative formation enthalpy) never reduces your score. The final reward is a weighted combination of the individual checks, with the main result fields carrying most of the weight.
