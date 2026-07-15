# Magnetic Semiconductor CrGaS3 Electronic and Magnetic Properties Reproduction

## Problem background
Two-dimensional magnetic semiconductors are attractive for spintronic devices because they combine long-range magnetic order with tunable electronic properties. A major challenge is raising the Curie temperature above room temperature to enable practical devices. Recent first-principles predictions suggest that a monolayer of CrGaS₃ may host intrinsic ferromagnetism with a high Curie temperature and a semiconducting bandgap, and that its magnetic anisotropy can be controlled by applying biaxial strain. This task reproduces the key first-principles results for CrGaS₃: we compute its electronic band structure and bandgap, magnetic anisotropy energy and easy axis, exchange coupling parameters, Curie temperature, and the effect of biaxial strain on the magnetic anisotropy. Successfully reproducing these quantities will verify the computational predictions and provide a benchmark for further studies.

## Approach
The reproduction follows a workflow that combines density functional theory (DFT) calculations with Monte Carlo simulations. All DFT calculations use an open-source plane-wave code (Quantum ESPRESSO or equivalent) with PBE pseudopotentials. We first construct the CrGaS₃ monolayer in the CBCAC stacking (space group P3m1) by substituting atoms in the α-In₂Se₃ parent structure. Geometry relaxation uses spin-polarized GGA+U with a Hubbard U correction on Cr and a van der Waals dispersion correction. From the relaxed structure, we compute the spin-polarized band structure and density of states with both GGA+U (DFT-D3) and the HSE06 hybrid functional to obtain the indirect bandgap and the locations of the valence band maximum (VBM) and conduction band minimum (CBM). To determine the magnetic anisotropy, we perform non-collinear DFT with spin-orbit coupling (SOC) for the ferromagnetic configuration, evaluating total energies for magnetization directions in the principal planes; the easy axis and MAE are derived from these energies. Extract exchange parameters by computing collinear and SOC total energies for ferromagnetic (FM) and two antiferromagnetic (AFM1, AFM2) configurations, then solving the anisotropic Heisenberg model with spin S=3/2 to obtain the isotropic exchanges J₁ and J₂, single-ion anisotropy D, and anisotropic exchanges λ₁ and λ₂. Using these parameters, we run Monte Carlo simulations of the anisotropic Heisenberg model on a 30×30 supercell to estimate the Curie temperature from the peak of the specific heat. Finally, we apply biaxial strains of −2%, 0%, 2%, 4%, 6% to the monolayer; for each strain, the structure is relaxed at the fixed in-plane lattice constant, and the MAE and easy axis are computed with SOC-DFT. All results are written to JSON artifacts for verification.

## Reproduction target
Produce the following quantities for the CrGaS₃ monolayer in the CBCAC configuration, all written to JSON files under `/app/outputs`:

1. **Electronic band structure and bandgap** (`band_structure_results.json`): The indirect bandgap from GGA+U and HSE06, the k-point locations of the VBM and CBM, whether the bandgap is spin-polarized, and whether it is indirect.

2. **Magnetic anisotropy energy and easy axis** (`mae_results.json`): The MAE (in µeV) defined as the energy of the hardest direction minus the easy-axis energy, the easy magnetization axis as a unit vector, and a flag indicating whether the easy axis is out-of-plane.

3. **Exchange coupling parameters** (`exchange_parameters.json`): The isotropic exchanges J₁, J₂ (meV), the single-ion anisotropy D (meV), and the anisotropic exchanges λ₁, λ₂ (meV), extracted from total energy differences of FM, AFM1, and AFM2 configurations.

4. **Curie temperature** (`curie_temperature.json`): The Curie temperature (in K) from Monte Carlo simulation, together with a string indicating the overall temperature range of the simulated transition.

5. **Strain-dependent magnetic anisotropy** (`strain_mae.json`): For each biaxial strain (−2%, 0%, 2%, 4%, 6%), the MAE value, the easy axis vector, and the strain threshold at which the easy axis flips (if any).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials for Cr, Ga, S: https://www.materialscloud.org/discover/sssp/
- α-In2Se3 monolayer crystal structure: 10.1021/acs.inorgchem.8b01742

## Workflow steps

### Step 1: Construct the CBCAC monolayer CrGaS3 structure
- Role: process
- Action: Generate the atomic model of CrGaS3 monolayer in the CBCAC stacking (S-Cr-S-Ga-S) with space group P3m1 by substituting In and Se in the α-In2Se3 monolayer with Ga/Cr and S. Save the initial structure.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: Geometry optimization of the CBCAC structure
- Role: process
- Action: Perform spin-polarized DFT relaxation of atomic positions and lattice vectors using PBE functional with DFT-D3 vdW correction, Hubbard U correction on Cr 3d with Ueff=3 eV, and a plane-wave cutoff of at least 550 eV, until forces are converged. Save the relaxed structure.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 3: Electronic band structure and bandgap
- Role: scored
- Action: Compute spin-polarized band structure and DOS for the relaxed CBCAC structure using PBE+U (with DFT-D3) and also with the HSE06 hybrid functional. Determine the indirect bandgap, VBM and CBM locations, and note the spin-polarized character. Write results to band_structure_results.json.
- Output file: `/app/outputs/band_structure_results.json`
- Format: json
- Contract: {"bandgap_GGA_U_eV": number, "bandgap_HSE06_eV": number, "VBM_location": string, "CBM_location": string, "spin_polarized": boolean, "is_indirect": boolean}
- Scoring: scored by hidden verifier

### Step 4: Magnetic anisotropy energy and easy axis
- Role: scored
- Action: For the FM configuration, perform non-collinear DFT+SOC calculations and evaluate total energies for magnetization directions spanning the principal planes. Compute MAE = E([uvw]) - E([001]) and determine the easy axis. Write results to mae_results.json.
- Output file: `/app/outputs/mae_results.json`
- Format: json
- Contract: {"MAE_microeV": number, "easy_axis": array of 3 numbers, "is_out_of_plane": boolean}
- Scoring: scored by hidden verifier

### Step 5: Exchange coupling parameters extraction
- Role: scored (load-bearing)
- Action: Compute total energies of FM, AFM1, AFM2 configurations with spin aligned in-plane (collinear DFT) and also with spin aligned out-of-plane (with SOC). Using the energy expressions for an anisotropic Heisenberg model with spin S=3/2, solve for the isotropic exchange J1, J2, single-ion anisotropy D, and anisotropic exchange λ1, λ2. Write results to exchange_parameters.json.
- Output file: `/app/outputs/exchange_parameters.json`
- Format: json
- Contract: {"J1_meV": number, "J2_meV": number, "D_meV": number, "lambda1_meV": number, "lambda2_meV": number}
- Scoring: scored by hidden verifier

### Step 6: Curie temperature from Monte Carlo simulation
- Role: scored (load-bearing)
- Action: Using the extracted exchange parameters, run Monte Carlo simulations on a 30×30 supercell with the anisotropic Heisenberg model for at least 1e5 steps per temperature. Determine the Curie temperature Tc from the peak of the specific heat. Write results to curie_temperature.json.
- Output file: `/app/outputs/curie_temperature.json`
- Format: json
- Contract: {"Tc_K": number, "Tc_range_K": string}
- Scoring: scored by hidden verifier

### Step 7: Strain-dependent magnetic anisotropy
- Role: scored (load-bearing)
- Action: For biaxial strains of -2%, 0%, 2%, 4%, 6%, perform geometry relaxation with fixed in-plane lattice constant. For each strained relaxed structure, compute SOC-DFT total energies for different magnetization directions to obtain MAE and easy axis. Write all strain-dependent results to strain_mae.json.
- Output file: `/app/outputs/strain_mae.json`
- Format: json
- Contract: {"strain_percent": array, "MAE_microeV": array, "easy_axis": array of arrays, "strain_switch_threshold": number or null}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure_results.json`
- `/app/outputs/mae_results.json`
- `/app/outputs/exchange_parameters.json`
- `/app/outputs/curie_temperature.json`
- `/app/outputs/strain_mae.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure_results.json
- path: `/app/outputs/band_structure_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Key electronic structure properties: bandgaps from GGA+U and HSE06, VBM/CBM locations, spin-polarized character, and indirect gap flag.
- schema:
  - `type`: object
  - `required`:
    - `bandgap_GGA_U_eV`: number (eV)
    - `bandgap_HSE06_eV`: number (eV)
    - `VBM_location`: string
    - `CBM_location`: string
    - `spin_polarized`: boolean
    - `is_indirect`: boolean

### mae_results.json
- path: `/app/outputs/mae_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Magnetic anisotropy energy and easy magnetization axis.
- schema:
  - `type`: object
  - `required`:
    - `MAE_microeV`: number (µeV)
    - `easy_axis`: array of 3 numbers
    - `is_out_of_plane`: boolean

### exchange_parameters.json
- path: `/app/outputs/exchange_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Magnetic exchange coupling parameters: isotropic J1, J2, single-ion anisotropy D, and anisotropic λ1, λ2.
- schema:
  - `type`: object
  - `required`:
    - `J1_meV`: number (meV)
    - `J2_meV`: number (meV)
    - `D_meV`: number (meV)
    - `lambda1_meV`: number (meV)
    - `lambda2_meV`: number (meV)

### curie_temperature.json
- path: `/app/outputs/curie_temperature.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Estimated Curie temperature from Monte Carlo simulation.
- schema:
  - `type`: object
  - `required`:
    - `Tc_K`: number (K)
    - `Tc_range_K`: string

### strain_mae.json
- path: `/app/outputs/strain_mae.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Magnetic anisotropy and easy axis under biaxial strain, including the strain threshold for easy-axis switching.
- schema:
  - `type`: object
  - `required`:
    - `strain_percent`: array of numbers
    - `MAE_microeV`: array of numbers
    - `easy_axis`: array of arrays of 3 numbers
    - `strain_switch_threshold`: number or null

Notes: All outputs will be compared against paper-reported values with appropriate tolerances (bandgap ±0.1 eV, MAE ±2 µeV, Tc ±50 K, exchange parameters ±25%, strain MAE ±2 µeV and correct easy-axis flip).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bandgap_GGA_U_eV": "number (eV)",
          "bandgap_HSE06_eV": "number (eV)",
          "VBM_location": "string",
          "CBM_location": "string",
          "spin_polarized": "boolean",
          "is_indirect": "boolean"
        }
      },
      "description": "Key electronic structure properties: bandgaps from GGA+U and HSE06, VBM/CBM locations, spin-polarized character, and indirect gap flag."
    },
    {
      "file": "mae_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "MAE_microeV": "number (µeV)",
          "easy_axis": "array of 3 numbers",
          "is_out_of_plane": "boolean"
        }
      },
      "description": "Magnetic anisotropy energy and easy magnetization axis."
    },
    {
      "file": "exchange_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "J1_meV": "number (meV)",
          "J2_meV": "number (meV)",
          "D_meV": "number (meV)",
          "lambda1_meV": "number (meV)",
          "lambda2_meV": "number (meV)"
        }
      },
      "description": "Magnetic exchange coupling parameters: isotropic J1, J2, single-ion anisotropy D, and anisotropic λ1, λ2."
    },
    {
      "file": "curie_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc_K": "number (K)",
          "Tc_range_K": "string"
        }
      },
      "description": "Estimated Curie temperature from Monte Carlo simulation."
    },
    {
      "file": "strain_mae.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "strain_percent": "array of numbers",
          "MAE_microeV": "array of numbers",
          "easy_axis": "array of arrays of 3 numbers",
          "strain_switch_threshold": "number or null"
        }
      },
      "description": "Magnetic anisotropy and easy axis under biaxial strain, including the strain threshold for easy-axis switching."
    }
  ],
  "notes": "All outputs will be compared against paper-reported values with appropriate tolerances (bandgap ±0.1 eV, MAE ±2 µeV, Tc ±50 K, exchange parameters ±25%, strain MAE ±2 µeV and correct easy-axis flip)."
}
```

## How you are scored
A hidden verifier reads the five required JSON artifacts from `/app/outputs` and independently scores each one. For each scored quantity, the verifier compares the agent's reported value to the paper's computed value (or to the expected trend for strain) using a tolerance that accounts for the legitimate spread of different DFT toolchains and simulation implementations. A result that matches or improves upon the reference earns full credit for that component; credit degrades only as the result deviates in the wrong direction. The overall reward is a weighted sum of the individual step scores, normalized to [0, 1]. Merely reporting numbers is not sufficient — the agent must perform the computational workflow and produce the specified output files.
