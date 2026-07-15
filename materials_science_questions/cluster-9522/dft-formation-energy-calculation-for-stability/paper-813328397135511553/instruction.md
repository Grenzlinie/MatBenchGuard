# DFT study of structure, mechanics, hardness and thermal properties of orthorhombic A2N2O compounds

## Problem background
Silicon oxynitride (Si2N2O) and germanium oxynitride (Ge2N2O) are important ceramic materials with high thermal and chemical stability, and they adopt an orthorhombic structure (space group Cmc2_1). The analogous orthorhombic carbon oxynitride (C2N2O) has not been synthesized, and its stability, mechanical properties, and potential hardness are of great interest. First-principles density functional theory (DFT) can predict the thermodynamic stability, elastic constants, mechanical moduli, Vickers hardness, Debye temperature, and minimum thermal conductivity of these three compounds. This task aims to compute these properties for orthorhombic A2N2O (A = C, Si, Ge) using plane-wave DFT with the PBEsol exchange-correlation functional and to assess whether C2N2O might exhibit superhard behaviour.

## Approach
The approach uses an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with the PBEsol functional and appropriate pseudopotentials for C, Si, Ge, N, O. Crystal structures for the three compounds are built in the orthorhombic space group Cmc2_1. Full structural optimization (lattice vectors and atomic positions) is performed for each compound. Electronic structure calculations yield band gaps, and Mulliken population analysis provides bond overlap populations and bond lengths. Elastic constants Cij are obtained via the stress-strain method by applying small deformations to the optimized cells. From the elastic constants, the Voigt-Reuss-Hill averaged bulk, shear, and Young's moduli are computed, along with Poisson's ratio, anisotropy indices, and linear compressibilities. Vickers hardness is estimated using Gao's semi-empirical method that combines bond lengths, cell volume, and Mulliken overlap populations; an alternative estimate from the Jiang relation (Hv = G/6.78) is also provided if computed. Finally, sound velocities, Debye temperature, and minimum thermal conductivities (Clarke and Cahill models) are derived from the density and elastic moduli. All results are organised in JSON files as specified in the output contract.

## Reproduction target
For each of the three compounds C2N2O, Si2N2O, and Ge2N2O, run the DFT workflow and produce the following scored artifacts: (i) optimized lattice parameters, cohesive energy, formation enthalpy, and band gap (lattice_properties.json); (ii) full set of orthorhombic elastic constants Cij (elastic_constants.json); (iii) Voigt-Reuss-Hill mechanical moduli, anisotropy indices, Poisson's ratio, B/G ratio, and linear compressibilities (mechanical_properties.json); (iv) bond-level hardness contributions and the geometrically averaged Vickers hardness via Gao's method, plus the Jiang estimate if computed (vickers_hardness.json); (v) sound velocities, Debye temperature, and minimum thermal conductivities from the Clarke and Cahill models (thermal_properties.json). All files must adhere to the exact JSON schemas described in the output contract and must be written to /app/outputs.

## Assets

- Open-source plane-wave DFT code: https://www.quantum-espresso.org
- PBEsol pseudopotentials for C, Si, Ge, N, O
- Orthorhombic crystal structures of A2N2O (space group Cmc2_1, No. 36)

## Workflow steps

### Step 1: Prepare initial crystal structures
- Role: process
- Action: Build initial orthorhombic structures for C2N2O, Si2N2O, and Ge2N2O in space group Cmc2_1 (No. 36) using publicly available lattice parameters and atomic positions. Write the input files required by the chosen DFT code.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: DFT structural optimization and electronic structure calculation
- Role: process
- Action: For each compound, perform full structural relaxation (lattice vectors and atomic positions) using plane-wave DFT with the PBEsol functional and the chosen pseudopotentials. Compute total energies, band gaps, and perform a Mulliken population analysis to obtain bond overlap populations and bond lengths. Achieve convergence in total energy and forces.
- Evidence: `/app/outputs/dft_optimization.log`

### Step 3: Elastic constants via stress-strain method
- Role: process
- Action: Using the optimized structures from step 2, apply small strains and compute the resulting stress tensors with DFT to obtain the full set of orthorhombic elastic constants C11, C22, C33, C44, C55, C66, C12, C13, C23.
- Evidence: `/app/outputs/elastic_constants_calc.log`

### Step 4: Extract lattice properties
- Role: scored (load-bearing)
- Action: Extract the optimized lattice parameters, cell volume, cohesive energy, formation enthalpy, and band gap for each compound. Write a JSON file with the schema described in the output contract.
- Output file: `/app/outputs/lattice_properties.json`
- Format: json
- Contract: Object with keys 'C2N2O', 'Si2N2O', 'Ge2N2O'. Each value is an object containing: a (Å), b (Å), c (Å), cell_volume (Å³), cohesive_energy (eV/f.u.), formation_enthalpy (eV/f.u.), band_gap (eV), band_gap_type (string, one of 'direct' or 'indirect').
- Scoring: scored by hidden verifier

### Step 5: Report elastic constants
- Role: scored
- Action: Assemble the elastic constants Cij for each compound and write a JSON file.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: Object with keys 'C2N2O', 'Si2N2O', 'Ge2N2O'. Each value is an object with keys: C11, C22, C33, C44, C55, C66, C12, C13, C23 (all numbers, units GPa).
- Scoring: scored by hidden verifier

### Step 6: Compute mechanical moduli and anisotropy
- Role: scored
- Action: From the elastic constants, derive the compliance matrix and compute bulk modulus B (GPa), shear modulus G (GPa), Young's modulus E (GPa), Poisson's ratio v, B/G ratio, universal anisotropic index A_U, percent anisotropy A_B and A_G (%), shear anisotropic factors A1, A2, A3, and linear compressibilities k_a, k_b, k_c (10⁻³ GPa⁻¹). Write a JSON file.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: Object with keys 'C2N2O', 'Si2N2O', 'Ge2N2O'. Each value is an object containing: B (GPa), G (GPa), E (GPa), v (dimensionless), BG_ratio, A_U, A_B (%), A_G (%), A1, A2, A3, k_a (1e-3 GPa-1), k_b, k_c.
- Scoring: scored by hidden verifier

### Step 7: Vickers hardness from Mulliken population
- Role: scored (load-bearing)
- Action: Using the cell volume, bond lengths, and Mulliken overlap populations from step 2, compute the bond volumes, bond hardnesses, and the geometrically averaged Vickers hardness H_v (GPa) for each compound using Gao's semi-empirical method. Also provide the alternative hardness from Jiang's empirical relation H_v = G/6.78, if computed. Write a JSON file.
- Output file: `/app/outputs/vickers_hardness.json`
- Format: json
- Contract: Object with keys 'C2N2O', 'Si2N2O', 'Ge2N2O'. Each value contains: bonds (an array of objects, each with: bond_type (string), bond_length (Å), overlap_population (e), bond_volume (Å³), bond_hardness (GPa), number_of_bonds (integer)), H_v_Gao (GPa), H_v_Jiang (GPa, nullable).
- Scoring: scored by hidden verifier

### Step 8: Debye temperature and minimum thermal conductivity
- Role: scored
- Action: From the density, bulk modulus, and shear modulus, compute the longitudinal, transverse, and mean sound velocities (m/s), the Debye temperature Θ_D (K), and the minimum thermal conductivities κ_min (W/mK) using the Clarke and Cahill models. Write a JSON file.
- Output file: `/app/outputs/thermal_properties.json`
- Format: json
- Contract: Object with keys 'C2N2O', 'Si2N2O', 'Ge2N2O'. Each value contains: longitudinal_velocity (m/s), transverse_velocity (m/s), mean_velocity (m/s), Debye_temperature (K), k_min_Clarke (W/mK), k_min_Cahill (W/mK).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_properties.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/mechanical_properties.json`
- `/app/outputs/vickers_hardness.json`
- `/app/outputs/thermal_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_properties.json
- path: `/app/outputs/lattice_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice parameters and thermodynamic stability data for the three compounds.
- schema:
  - `type`: object
  - `required`:
    - `C2N2O`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `cell_volume`: number
      - `cohesive_energy`: number
      - `formation_enthalpy`: number
      - `band_gap`: number
      - `band_gap_type`: string
    - `Si2N2O`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `cell_volume`: number
      - `cohesive_energy`: number
      - `formation_enthalpy`: number
      - `band_gap`: number
      - `band_gap_type`: string
    - `Ge2N2O`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `cell_volume`: number
      - `cohesive_energy`: number
      - `formation_enthalpy`: number
      - `band_gap`: number
      - `band_gap_type`: string

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Full set of elastic constants Cij (GPa) for the three compounds.
- schema:
  - `type`: object
  - `required`:
    - `C2N2O`:
      - `C11`: number
      - `C22`: number
      - `C33`: number
      - `C44`: number
      - `C55`: number
      - `C66`: number
      - `C12`: number
      - `C13`: number
      - `C23`: number
    - `Si2N2O`:
      - `C11`: number
      - `C22`: number
      - `C33`: number
      - `C44`: number
      - `C55`: number
      - `C66`: number
      - `C12`: number
      - `C13`: number
      - `C23`: number
    - `Ge2N2O`:
      - `C11`: number
      - `C22`: number
      - `C33`: number
      - `C44`: number
      - `C55`: number
      - `C66`: number
      - `C12`: number
      - `C13`: number
      - `C23`: number

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Mechanical moduli (Voigt–Reuss–Hill), anisotropy indices, and linear compressibilities. The checker will recompute these from the elastic constants and compare with paper values.
- schema:
  - `type`: object
  - `required`:
    - `C2N2O`:
      - `B`: number
      - `G`: number
      - `E`: number
      - `v`: number
      - `BG_ratio`: number
      - `A_U`: number
      - `A_B`: number
      - `A_G`: number
      - `A1`: number
      - `A2`: number
      - `A3`: number
      - `k_a`: number
      - `k_b`: number
      - `k_c`: number
    - `Si2N2O`:
      - `B`: number
      - `G`: number
      - `E`: number
      - `v`: number
      - `BG_ratio`: number
      - `A_U`: number
      - `A_B`: number
      - `A_G`: number
      - `A1`: number
      - `A2`: number
      - `A3`: number
      - `k_a`: number
      - `k_b`: number
      - `k_c`: number
    - `Ge2N2O`:
      - `B`: number
      - `G`: number
      - `E`: number
      - `v`: number
      - `BG_ratio`: number
      - `A_U`: number
      - `A_B`: number
      - `A_G`: number
      - `A1`: number
      - `A2`: number
      - `A3`: number
      - `k_a`: number
      - `k_b`: number
      - `k_c`: number

### vickers_hardness.json
- path: `/app/outputs/vickers_hardness.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bond-level hardness contributions and averaged Vickers hardness via Gao and Jiang methods.
- schema:
  - `type`: object
  - `required`:
    - `C2N2O`:
      - `bonds`: array
      - `H_v_Gao`: number
      - `H_v_Jiang`: number|null
    - `Si2N2O`:
      - `bonds`: array
      - `H_v_Gao`: number
      - `H_v_Jiang`: number|null
    - `Ge2N2O`:
      - `bonds`: array
      - `H_v_Gao`: number
      - `H_v_Jiang`: number|null
  - `items`:
    - `bonds`:
      - `bond_type`: string
      - `bond_length`: number
      - `overlap_population`: number
      - `bond_volume`: number
      - `bond_hardness`: number
      - `number_of_bonds`: integer

### thermal_properties.json
- path: `/app/outputs/thermal_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Sound velocities, Debye temperature, and minimum thermal conductivities (Clarke and Cahill models).
- schema:
  - `type`: object
  - `required`:
    - `C2N2O`:
      - `longitudinal_velocity`: number
      - `transverse_velocity`: number
      - `mean_velocity`: number
      - `Debye_temperature`: number
      - `k_min_Clarke`: number
      - `k_min_Cahill`: number
    - `Si2N2O`:
      - `longitudinal_velocity`: number
      - `transverse_velocity`: number
      - `mean_velocity`: number
      - `Debye_temperature`: number
      - `k_min_Clarke`: number
      - `k_min_Cahill`: number
    - `Ge2N2O`:
      - `longitudinal_velocity`: number
      - `transverse_velocity`: number
      - `mean_velocity`: number
      - `Debye_temperature`: number
      - `k_min_Clarke`: number
      - `k_min_Cahill`: number

Notes: All values must be extracted from the DFT calculations. The checker compares the submitted values to the paper-reported reference data with appropriate tolerances, and recomputes mechanical moduli from the elastic constants for internal consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C2N2O": {
            "a": "number",
            "b": "number",
            "c": "number",
            "cell_volume": "number",
            "cohesive_energy": "number",
            "formation_enthalpy": "number",
            "band_gap": "number",
            "band_gap_type": "string"
          },
          "Si2N2O": {
            "a": "number",
            "b": "number",
            "c": "number",
            "cell_volume": "number",
            "cohesive_energy": "number",
            "formation_enthalpy": "number",
            "band_gap": "number",
            "band_gap_type": "string"
          },
          "Ge2N2O": {
            "a": "number",
            "b": "number",
            "c": "number",
            "cell_volume": "number",
            "cohesive_energy": "number",
            "formation_enthalpy": "number",
            "band_gap": "number",
            "band_gap_type": "string"
          }
        }
      },
      "description": "Lattice parameters and thermodynamic stability data for the three compounds."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C2N2O": {
            "C11": "number",
            "C22": "number",
            "C33": "number",
            "C44": "number",
            "C55": "number",
            "C66": "number",
            "C12": "number",
            "C13": "number",
            "C23": "number"
          },
          "Si2N2O": {
            "C11": "number",
            "C22": "number",
            "C33": "number",
            "C44": "number",
            "C55": "number",
            "C66": "number",
            "C12": "number",
            "C13": "number",
            "C23": "number"
          },
          "Ge2N2O": {
            "C11": "number",
            "C22": "number",
            "C33": "number",
            "C44": "number",
            "C55": "number",
            "C66": "number",
            "C12": "number",
            "C13": "number",
            "C23": "number"
          }
        }
      },
      "description": "Full set of elastic constants Cij (GPa) for the three compounds."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "C2N2O": {
            "B": "number",
            "G": "number",
            "E": "number",
            "v": "number",
            "BG_ratio": "number",
            "A_U": "number",
            "A_B": "number",
            "A_G": "number",
            "A1": "number",
            "A2": "number",
            "A3": "number",
            "k_a": "number",
            "k_b": "number",
            "k_c": "number"
          },
          "Si2N2O": {
            "B": "number",
            "G": "number",
            "E": "number",
            "v": "number",
            "BG_ratio": "number",
            "A_U": "number",
            "A_B": "number",
            "A_G": "number",
            "A1": "number",
            "A2": "number",
            "A3": "number",
            "k_a": "number",
            "k_b": "number",
            "k_c": "number"
          },
          "Ge2N2O": {
            "B": "number",
            "G": "number",
            "E": "number",
            "v": "number",
            "BG_ratio": "number",
            "A_U": "number",
            "A_B": "number",
            "A_G": "number",
            "A1": "number",
            "A2": "number",
            "A3": "number",
            "k_a": "number",
            "k_b": "number",
            "k_c": "number"
          }
        }
      },
      "description": "Mechanical moduli (Voigt–Reuss–Hill), anisotropy indices, and linear compressibilities. The checker will recompute these from the elastic constants and compare with paper values."
    },
    {
      "file": "vickers_hardness.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C2N2O": {
            "bonds": "array",
            "H_v_Gao": "number",
            "H_v_Jiang": "number|null"
          },
          "Si2N2O": {
            "bonds": "array",
            "H_v_Gao": "number",
            "H_v_Jiang": "number|null"
          },
          "Ge2N2O": {
            "bonds": "array",
            "H_v_Gao": "number",
            "H_v_Jiang": "number|null"
          }
        },
        "items": {
          "bonds": {
            "bond_type": "string",
            "bond_length": "number",
            "overlap_population": "number",
            "bond_volume": "number",
            "bond_hardness": "number",
            "number_of_bonds": "integer"
          }
        }
      },
      "description": "Bond-level hardness contributions and averaged Vickers hardness via Gao and Jiang methods."
    },
    {
      "file": "thermal_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C2N2O": {
            "longitudinal_velocity": "number",
            "transverse_velocity": "number",
            "mean_velocity": "number",
            "Debye_temperature": "number",
            "k_min_Clarke": "number",
            "k_min_Cahill": "number"
          },
          "Si2N2O": {
            "longitudinal_velocity": "number",
            "transverse_velocity": "number",
            "mean_velocity": "number",
            "Debye_temperature": "number",
            "k_min_Clarke": "number",
            "k_min_Cahill": "number"
          },
          "Ge2N2O": {
            "longitudinal_velocity": "number",
            "transverse_velocity": "number",
            "mean_velocity": "number",
            "Debye_temperature": "number",
            "k_min_Clarke": "number",
            "k_min_Cahill": "number"
          }
        }
      },
      "description": "Sound velocities, Debye temperature, and minimum thermal conductivities (Clarke and Cahill models)."
    }
  ],
  "notes": "All values must be extracted from the DFT calculations. The checker compares the submitted values to the paper-reported reference data with appropriate tolerances, and recomputes mechanical moduli from the elastic constants for internal consistency."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact by comparing your submitted values against the reference results from the original study, using appropriate tolerances that account for differences in DFT codes and pseudopotentials. The verifier also recomputes the mechanical moduli and hardness from your reported elastic constants and bond data to check internal consistency. Each of the five scored stages carries a weight, and the final reward is the weighted sum. You are not required to match any particular published number exactly; the verifier expects physically reasonable values that are consistent with the PBEsol treatment of these compounds.
