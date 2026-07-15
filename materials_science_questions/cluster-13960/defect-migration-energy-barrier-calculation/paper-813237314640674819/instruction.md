# He, Kr, Xe diffusion barriers in ZrN

## Problem background
Zirconium nitride (ZrN) is a candidate inert matrix fuel component for Generation-IV nuclear reactors. Understanding the atomic-scale diffusion behavior of fission gases—helium (He), krypton (Kr), and xenon (Xe)—in ZrN is essential for predicting fuel swelling and gas release. The mechanisms by which these inert gases migrate, whether interstitially or with the aid of vacancies, and the strength with which they bind to lattice vacancies, are not fully established. First-principles calculations can provide the defect formation energies, binding energies, and migration barriers that govern gas mobility and retention, helping to explain experimental observations of selective He release and Kr/Xe retention in irradiated nitride fuels.

## Approach
The work uses density functional theory (DFT) with the generalized gradient approximation and plane-wave pseudopotentials to model rocksalt ZrN. The equilibrium lattice constant is obtained from energy-volume calculations fitted to the Birch-Murnaghan equation of state. All defect calculations are performed in a 3×3×3 supercell containing 216 atomic sites. Vacancy formation energies of nitrogen and zirconium vacancies are computed by comparing total energies of defective and perfect supercells, with chemical potentials referenced to bulk ZrN and elemental Zr metal. Binding energies of an inert gas atom (He, Kr, Xe) to a pre-existing N or Zr vacancy are determined from total-energy differences of supercells containing the gas atom, the vacancy, and both defects together. Migration barriers for interstitial diffusion are evaluated using the nudged elastic band (NEB) method along a path between adjacent tetrahedral sites passing through an octahedral saddle point. Vacancy-aided diffusion barriers are obtained by NEB calculations for the gas atom moving between two adjacent N vacancies on the nitrogen sublattice. All computed quantities—lattice constant, vacancy formation energies at zero chemical potential offset, binding energies, and migration barriers—are collected into a single scored artifact.

## Reproduction target
Using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials, perform the following calculations and write the results into `/app/outputs/results.json`:

1. Determine the equilibrium lattice constant of rocksalt ZrN.
2. Compute the formation energies of a nitrogen vacancy and a zirconium vacancy at Δμ = 0.
3. Compute the binding energies of He, Kr, and Xe atoms to a N vacancy and to a Zr vacancy.
4. Compute the interstitial migration barriers of He, Kr, and Xe.
5. Compute the vacancy-aided migration barriers of He, Kr, and Xe on the N sublattice.

The goal is to obtain the set of fundamental diffusion-related quantities that govern the mobility and trapping of inert gases in ZrN.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- SSSP pseudopotential library (or equivalent): https://www.materialscloud.org/discover/sssp
- Rocksalt ZrN crystal structure
- Hexagonal Zr metal crystal structure

## Workflow steps

### Step 1: Determine equilibrium lattice parameter of ZrN
- Role: process
- Action: Perform DFT energy-volume calculations on the rocksalt ZrN unit cell and fit the Birch-Murnaghan equation of state to obtain the equilibrium lattice constant a0.
- Evidence: `/app/outputs/lattice_parameter.txt`

### Step 2: Compute reference energies for bulk ZrN and Zr metal
- Role: process
- Action: Calculate the total energy per ZrN formula unit in the bulk rocksalt structure and the energy per atom of hexagonal Zr metal using DFT. These set the chemical potential bounds for vacancy formation energy calculations.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Compute total energies of vacancy supercells
- Role: process
- Action: Construct a 3×3×3 supercell (216 atoms) of ZrN using the equilibrium lattice constant from step_01. Perform DFT relaxations to obtain total energies of the perfect supercell, the supercell with one N vacancy, and the supercell with one Zr vacancy.
- Evidence: `/app/outputs/vacancy_total_energies.json`

### Step 4: Compute binding energies of He, Kr, Xe to vacancies
- Role: process
- Action: Perform DFT calculations for supercells containing: (i) an interstitial inert gas atom (He, Kr, or Xe) in a vacancy-free cell, (ii) a single N or Zr vacancy, and (iii) both the interstitial gas and the vacancy simultaneously. From the total energies, compute the binding energy E_b for each gas to an N vacancy and to a Zr vacancy using the method described in the paper.
- Evidence: `/app/outputs/binding_raw_energies.json`

### Step 5: Run NEB for interstitial diffusion barriers
- Role: process
- Action: Set up a diffusion path from one tetrahedral interstitial site to an adjacent one via an octahedral saddle point. Run nudged elastic band (NEB) calculations for He, Kr, and Xe as interstitial defects and extract the maximum energy along each path as the migration barrier.
- Evidence: `/app/outputs/interstitial_neb_paths.json`

### Step 6: Run NEB for vacancy-aided diffusion barriers
- Role: process
- Action: Create a configuration with a substitutional inert gas atom on the N sublattice and an adjacent N vacancy (two‑vacancy cluster). Run NEB calculations for the gas atom moving from one vacancy to the neighboring vacancy along the (1 1 0) direction. Extract the migration barrier (global maximum minus initial energy) for He, Kr, and Xe.
- Evidence: `/app/outputs/vacancy_aided_neb_paths.json`

### Step 7: Compile all key results into scored artifact
- Role: scored (load-bearing)
- Action: Collect the lattice constant, vacancy formation energies (N and Zr at Δμ=0), binding energies to N and Zr vacancies, interstitial migration barriers, and vacancy‑aided migration barriers from the preceding steps and write them into the JSON file results.json according to the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {\n  \"lattice_parameter_A\": <float, lattice constant in Angstrom>,\
  \"vacancy_formation_N_eV\": <float, formation energy of N vacancy at Δμ=0>,\
  \"vacancy_formation_Zr_eV\": <float, formation energy of Zr vacancy at Δμ=0>,\
  \"binding_energies_to_N_vac_eV\": {\n    \"He\": <float>,\\n    \"Kr\": <float>,\\n    \"Xe\": <float>\
  },\
  \"binding_energies_to_Zr_vac_eV\": {\n    \"He\": <float>,\\n    \"Kr\": <float>,\\n    \"Xe\": <float>\
  },\
  \"interstitial_migration_barriers_eV\": {\n    \"He\": <float>,\\n    \"Kr\": <float>,\\n    \"Xe\": <float>\
  },\
  \"vacancy_aided_migration_barriers_eV\": {\n    \"He\": <float>,\\n    \"Kr\": <float>,\\n    \"Xe\": <float>\
  }\
}
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
- description: Aggregate result containing lattice constant, vacancy formation energies at Δμ=0, binding energies of He/Kr/Xe to N and Zr vacancies, and migration barriers for interstitial and vacancy‑aided diffusion. All values in eV except lattice_parameter (Angstrom).
- schema:
  - `type`: object
  - `required`: `lattice_parameter_A`, `vacancy_formation_N_eV`, `vacancy_formation_Zr_eV`, `binding_energies_to_N_vac_eV`, `binding_energies_to_Zr_vac_eV`, `interstitial_migration_barriers_eV`, `vacancy_aided_migration_barriers_eV`
  - `properties`:
    - `lattice_parameter_A`:
      - `type`: number
    - `vacancy_formation_N_eV`:
      - `type`: number
    - `vacancy_formation_Zr_eV`:
      - `type`: number
    - `binding_energies_to_N_vac_eV`:
      - `type`: object
      - `required`: `He`, `Kr`, `Xe`
      - `properties`:
        - `He`:
          - `type`: number
        - `Kr`:
          - `type`: number
        - `Xe`:
          - `type`: number
    - `binding_energies_to_Zr_vac_eV`:
      - `type`: object
      - `required`: `He`, `Kr`, `Xe`
      - `properties`:
        - `He`:
          - `type`: number
        - `Kr`:
          - `type`: number
        - `Xe`:
          - `type`: number
    - `interstitial_migration_barriers_eV`:
      - `type`: object
      - `required`: `He`, `Kr`, `Xe`
      - `properties`:
        - `He`:
          - `type`: number
        - `Kr`:
          - `type`: number
        - `Xe`:
          - `type`: number
    - `vacancy_aided_migration_barriers_eV`:
      - `type`: object
      - `required`: `He`, `Kr`, `Xe`
      - `properties`:
        - `He`:
          - `type`: number
        - `Kr`:
          - `type`: number
        - `Xe`:
          - `type`: number

Notes: The scoring includes numeric comparisons with absolute tolerances and verification of relative ordering trends (interstitial barrier He lowest, vacancy‑aided barrier He negligible, binding energies He less negative than Kr/Xe). Additional paper quantities such as anti‑site defects, di‑vacancy binding, and self‑diffusion barriers are not required for this core reproduction.

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
          "lattice_parameter_A",
          "vacancy_formation_N_eV",
          "vacancy_formation_Zr_eV",
          "binding_energies_to_N_vac_eV",
          "binding_energies_to_Zr_vac_eV",
          "interstitial_migration_barriers_eV",
          "vacancy_aided_migration_barriers_eV"
        ],
        "properties": {
          "lattice_parameter_A": {
            "type": "number"
          },
          "vacancy_formation_N_eV": {
            "type": "number"
          },
          "vacancy_formation_Zr_eV": {
            "type": "number"
          },
          "binding_energies_to_N_vac_eV": {
            "type": "object",
            "required": [
              "He",
              "Kr",
              "Xe"
            ],
            "properties": {
              "He": {
                "type": "number"
              },
              "Kr": {
                "type": "number"
              },
              "Xe": {
                "type": "number"
              }
            }
          },
          "binding_energies_to_Zr_vac_eV": {
            "type": "object",
            "required": [
              "He",
              "Kr",
              "Xe"
            ],
            "properties": {
              "He": {
                "type": "number"
              },
              "Kr": {
                "type": "number"
              },
              "Xe": {
                "type": "number"
              }
            }
          },
          "interstitial_migration_barriers_eV": {
            "type": "object",
            "required": [
              "He",
              "Kr",
              "Xe"
            ],
            "properties": {
              "He": {
                "type": "number"
              },
              "Kr": {
                "type": "number"
              },
              "Xe": {
                "type": "number"
              }
            }
          },
          "vacancy_aided_migration_barriers_eV": {
            "type": "object",
            "required": [
              "He",
              "Kr",
              "Xe"
            ],
            "properties": {
              "He": {
                "type": "number"
              },
              "Kr": {
                "type": "number"
              },
              "Xe": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Aggregate result containing lattice constant, vacancy formation energies at Δμ=0, binding energies of He/Kr/Xe to N and Zr vacancies, and migration barriers for interstitial and vacancy‑aided diffusion. All values in eV except lattice_parameter (Angstrom)."
    }
  ],
  "notes": "The scoring includes numeric comparisons with absolute tolerances and verification of relative ordering trends (interstitial barrier He lowest, vacancy‑aided barrier He negligible, binding energies He less negative than Kr/Xe). Additional paper quantities such as anti‑site defects, di‑vacancy binding, and self‑diffusion barriers are not required for this core reproduction."
}
```

## How you are scored
A hidden verifier reads your `results.json` file. It compares each reported numeric value (lattice parameter, vacancy formation energies, binding energies, and migration barriers) against expected reference values within predefined tolerances. In addition, the verifier checks that the migration barriers of He, Kr, and Xe obey a specific relative ordering (for both interstitial and vacancy-aided diffusion) and that the binding energies of the three gases to vacancies exhibit a consistent structural trend. Each quantity and each trend check contributes a weighted portion of the final reward. Reproducing the correct absolute numbers AND the correct relative ordering among the gas species is required for full credit.
