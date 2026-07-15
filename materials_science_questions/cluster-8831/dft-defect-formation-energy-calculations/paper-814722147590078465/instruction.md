# Magnetic Properties of Cu-Doped ZnO Nanotubes from Density Functional Theory

## Problem background
Diluted magnetic semiconductors based on ZnO nanostructures are candidates for spintronic devices because they may combine semiconducting and magnetic behavior. Recent work has focused on doping ZnO nanotubes with transition metals to tailor their electronic and magnetic properties. In particular, single-walled ZnO nanotubes (SWZnONTs) with Cu substituents have been studied using first-principles density functional theory to probe whether the system can exhibit half-metallic ferromagnetism and how the magnetic ground state depends on the arrangement of the Cu dopants. The task is to reproduce the computational investigation of the structural, electronic, and magnetic properties of Cu-doped SWZnONTs for two chiralities, (10,0) and (5,0), and for three doping configurations: a single Cu atom, a close Cu pair, and a far Cu pair.

## Approach
The approach is a first-principles density functional theory (DFT) supercell study. Pristine ZnO nanotube supercells (Zn40O40 for (10,0) and Zn20O20 for (5,0)) are built and relaxed with the generalized-gradient approximation (GGA-PBE) using a plane-wave DFT code. The site preference for Cu substitution is verified by comparing substitution energies on Zn and O sites. Then, three doping scenarios are investigated:
- Single Cu doping: one Zn atom replaced by Cu. Total energies of ferromagnetic (FM) and nonmagnetic (NM) spin configurations are compared to identify the ground state. The electronic density of states (DOS) gives the spin polarization at the Fermi level and magnetic moments.
- Close Cu pair: two Cu atoms occupy nearest-neighbor Zn sites. FM and antiferromagnetic (AFM) configurations are evaluated; the ground-state energy difference and the band gap from the DOS are extracted.
- Far Cu pair: three configurations with increasing Cu–Cu separation in the (10,0) nanotube. The same FM/AFM energy comparison is performed, and total and Cu-partial magnetic moments together with spin polarization are computed.
All calculations use open-source plane-wave DFT (e.g., Quantum ESPRESSO) with GGA-PBE pseudopotentials. The evaluation focuses on comparing computed magnetic ground states and derived quantities against reference expectations.

## Reproduction target
Perform DFT supercell calculations to determine the following properties for Cu-doped SWZnONTs:
- From single Cu doping (10,0 and 5,0 nanotubes): the stable magnetic state (FM or NM), total magnetic moment, partial magnetic moment on Cu, Cu–O bond length after relaxation, spin polarization at the Fermi level, and whether the system is half-metallic.
- From close Cu pair co-doping (10,0 and 5,0): the stable magnetic state (AFM or FM), the energy difference ΔE = E_AFM – E_FM, and the band gap from DOS.
- From far Cu pair co-doping in the (10,0) nanotube (three configurations a, b, c with increasing distance): the stable magnetic state (FM or AFM), total magnetic moment, Cu partial magnetic moment, and spin polarization.
All results must be written to the specified JSON output files under `/app/outputs`, following the defined schemas.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build pristine ZnO nanotube supercells
- Role: process
- Action: Construct Zn40O40 and Zn20O20 zigzag supercells for (10,0) and (5,0) single-walled ZnO nanotubes using literature ZnO nanotube geometry and lattice parameters.
- Evidence: none

### Step 2: Relax pristine supercells and compute reference properties
- Role: process
- Action: Perform DFT relaxation of the pristine supercells within the generalized-gradient approximation (GGA-PBE) using a plane-wave code. Converge forces to a strict threshold analogous to the paper (< 1 mRy/a.u.). Compute Zn-O bond lengths and band gaps for reference. Save energies to pristine_energies.json.
- Evidence: `/app/outputs/pristine_energies.json`

### Step 3: Determine Cu substitution site preference
- Role: process
- Action: Calculate formation energies for Cu substituting on Zn and O sites in the relaxed supercells to verify the Zn site preference. Use chemical potentials of Cu, Zn, and O from standard elemental phases.
- Evidence: none

### Step 4: Single Cu doping: magnetic and electronic properties
- Role: scored (load-bearing)
- Action: For each supercell with one Cu substituting a Zn atom (single Cu doping), perform DFT calculations for both ferromagnetic (FM) and nonmagnetic (NM) spin configurations. Determine the stable magnetic ground state (lower total energy). Compute total magnetic moment, partial Cu magnetic moment, Cu-O bond length after relaxation, and spin polarization at the Fermi level from the density of states. Report these in step_04_single_cu_results.json.
- Output file: `/app/outputs/step_04_single_cu_results.json`
- Format: json
- Contract: A JSON object with keys '10-0' and '5-0'. Each value is an object with fields: stable_magnetic_state (string 'FM' or 'NM'), total_magnetic_moment (float μB), Cu_partial_magnetic_moment (float μB), Cu_O_bond_length (float Å), spin_polarization (float 0-1), half_metallic (boolean).
- Scoring: scored by hidden verifier

### Step 5: Close Cu pair co-doping: magnetic and electronic properties
- Role: scored
- Action: For each supercell with two Cu atoms substituting two nearest-neighbor Zn sites (close Cu pair), perform DFT calculations for FM and antiferromagnetic (AFM) spin configurations. Determine the stable magnetic ground state. Compute the energy difference ΔE = E_AFM - E_FM and the semiconducting band gap from the density of states. Report in step_05_close_cu_results.json.
- Output file: `/app/outputs/step_05_close_cu_results.json`
- Format: json
- Contract: A JSON object with keys '10-0' and '5-0'. Each value is an object with fields: stable_magnetic_state (string 'AFM' or 'FM'), band_gap (float eV), energy_difference_deltaE (float eV, negative if AFM stable), semiconducting (boolean).
- Scoring: scored by hidden verifier

### Step 6: Far Cu pair co-doping: magnetic and electronic properties
- Role: scored
- Action: For the (10,0) supercell, set up three configurations with Cu atoms at increasing separation distances (far-apart pair configurations a, b, c). For each configuration, perform DFT calculations for FM and AFM spin configurations, determine the stable FM ground state, and compute total magnetic moment, partial Cu magnetic moment, and spin polarization. Report as an array in step_06_far_cu_results.json.
- Output file: `/app/outputs/step_06_far_cu_results.json`
- Format: json
- Contract: A JSON array of three objects. Each object has fields: configuration_id (string 'a','b','c'), stable_magnetic_state (string 'FM' or 'AFM'), total_magnetic_moment (float μB), Cu_partial_magnetic_moment (float μB), spin_polarization (float 0-1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_single_cu_results.json`
- `/app/outputs/step_05_close_cu_results.json`
- `/app/outputs/step_06_far_cu_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_single_cu_results.json
- path: `/app/outputs/step_04_single_cu_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single Cu doping results for both (10,0) and (5,0) supercells: magnetic ground state, moments, bond length, spin polarization, and half-metallicity.
- schema:
  - `type`: object
  - `required`: `10-0`, `5-0`
  - `items`:
    - `type`: object
    - `required`: `stable_magnetic_state`, `total_magnetic_moment`, `Cu_partial_magnetic_moment`, `Cu_O_bond_length`, `spin_polarization`, `half_metallic`
    - `properties`:
      - `stable_magnetic_state`:
        - `type`: string
        - `enum`: `FM`, `NM`
      - `total_magnetic_moment`:
        - `type`: number
        - `unit`: μB
      - `Cu_partial_magnetic_moment`:
        - `type`: number
        - `unit`: μB
      - `Cu_O_bond_length`:
        - `type`: number
        - `unit`: Å
      - `spin_polarization`:
        - `type`: number
        - `minimum`: 0
        - `maximum`: 1
      - `half_metallic`:
        - `type`: boolean

### step_05_close_cu_results.json
- path: `/app/outputs/step_05_close_cu_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Close Cu pair co-doping results for both supercells: magnetic state, band gap, AFM-FM energy difference, and semiconducting character.
- schema:
  - `type`: object
  - `required`: `10-0`, `5-0`
  - `items`:
    - `type`: object
    - `required`: `stable_magnetic_state`, `band_gap`, `energy_difference_deltaE`, `semiconducting`
    - `properties`:
      - `stable_magnetic_state`:
        - `type`: string
        - `enum`: `AFM`, `FM`
      - `band_gap`:
        - `type`: number
        - `unit`: eV
      - `energy_difference_deltaE`:
        - `type`: number
        - `unit`: eV
      - `semiconducting`:
        - `type`: boolean

### step_06_far_cu_results.json
- path: `/app/outputs/step_06_far_cu_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Far Cu pair co-doping results for three separation distances in the (10,0) supercell: magnetic state, total/partial moments, and spin polarization.
- schema:
  - `type`: array
  - `minItems`: 3
  - `maxItems`: 3
  - `items`:
    - `type`: object
    - `required`: `configuration_id`, `stable_magnetic_state`, `total_magnetic_moment`, `Cu_partial_magnetic_moment`, `spin_polarization`
    - `properties`:
      - `configuration_id`:
        - `type`: string
        - `enum`: `a`, `b`, `c`
      - `stable_magnetic_state`:
        - `type`: string
        - `enum`: `FM`, `AFM`
      - `total_magnetic_moment`:
        - `type`: number
        - `unit`: μB
      - `Cu_partial_magnetic_moment`:
        - `type`: number
        - `unit`: μB
      - `spin_polarization`:
        - `type`: number
        - `minimum`: 0
        - `maximum`: 1

Notes: The hidden checker will compare the agent's reported values against paper-derived reference values using appropriate tolerances for a re-run with a different DFT code. All numerical values must be in the indicated units.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_single_cu_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "10-0",
          "5-0"
        ],
        "items": {
          "type": "object",
          "required": [
            "stable_magnetic_state",
            "total_magnetic_moment",
            "Cu_partial_magnetic_moment",
            "Cu_O_bond_length",
            "spin_polarization",
            "half_metallic"
          ],
          "properties": {
            "stable_magnetic_state": {
              "type": "string",
              "enum": [
                "FM",
                "NM"
              ]
            },
            "total_magnetic_moment": {
              "type": "number",
              "unit": "μB"
            },
            "Cu_partial_magnetic_moment": {
              "type": "number",
              "unit": "μB"
            },
            "Cu_O_bond_length": {
              "type": "number",
              "unit": "Å"
            },
            "spin_polarization": {
              "type": "number",
              "minimum": 0,
              "maximum": 1
            },
            "half_metallic": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Single Cu doping results for both (10,0) and (5,0) supercells: magnetic ground state, moments, bond length, spin polarization, and half-metallicity."
    },
    {
      "file": "step_05_close_cu_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "10-0",
          "5-0"
        ],
        "items": {
          "type": "object",
          "required": [
            "stable_magnetic_state",
            "band_gap",
            "energy_difference_deltaE",
            "semiconducting"
          ],
          "properties": {
            "stable_magnetic_state": {
              "type": "string",
              "enum": [
                "AFM",
                "FM"
              ]
            },
            "band_gap": {
              "type": "number",
              "unit": "eV"
            },
            "energy_difference_deltaE": {
              "type": "number",
              "unit": "eV"
            },
            "semiconducting": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Close Cu pair co-doping results for both supercells: magnetic state, band gap, AFM-FM energy difference, and semiconducting character."
    },
    {
      "file": "step_06_far_cu_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "minItems": 3,
        "maxItems": 3,
        "items": {
          "type": "object",
          "required": [
            "configuration_id",
            "stable_magnetic_state",
            "total_magnetic_moment",
            "Cu_partial_magnetic_moment",
            "spin_polarization"
          ],
          "properties": {
            "configuration_id": {
              "type": "string",
              "enum": [
                "a",
                "b",
                "c"
              ]
            },
            "stable_magnetic_state": {
              "type": "string",
              "enum": [
                "FM",
                "AFM"
              ]
            },
            "total_magnetic_moment": {
              "type": "number",
              "unit": "μB"
            },
            "Cu_partial_magnetic_moment": {
              "type": "number",
              "unit": "μB"
            },
            "spin_polarization": {
              "type": "number",
              "minimum": 0,
              "maximum": 1
            }
          }
        }
      },
      "description": "Far Cu pair co-doping results for three separation distances in the (10,0) supercell: magnetic state, total/partial moments, and spin polarization."
    }
  ],
  "notes": "The hidden checker will compare the agent's reported values against paper-derived reference values using appropriate tolerances for a re-run with a different DFT code. All numerical values must be in the indicated units."
}
```

## How you are scored
A hidden verifier will inspect each of the three scored output files (`step_04_single_cu_results.json`, `step_05_close_cu_results.json`, `step_06_far_cu_results.json`). For every quantity in these files, the verifier compares your reported value to an internal reference. Each scored step contributes a weighted fraction to the final reward, which is a number between 0.0 and 1.0. Meeting the required accuracy for a quantity yields full credit for that portion; larger deviations reduce the reward. The reference values are derived from the expected outcome of the DFT procedure and are not disclosed. The verifier does not re-run DFT; it only reads your submitted JSON artifacts and compares the reported numbers against the hidden targets. Producing the required output files with plausible, non-trivial values is necessary to obtain a non-zero score.
