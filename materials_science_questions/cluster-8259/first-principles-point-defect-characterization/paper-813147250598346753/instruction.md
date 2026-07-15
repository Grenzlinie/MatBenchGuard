# Computation of defect levels and formation energies of VAsVGa complex in GaAs

## Problem background
Semi-insulating GaAs materials owe their properties to deep-level defects that act as traps and recombination centers. The electron trap labeled EL6 (located near Ec-0.38 eV) is one of the primary deep donor levels in GaAs, but its atomic origin is not fully settled. Among the proposed microscopic models, the VAsVGa complex — adjacent arsenic and gallium vacancies — is a leading candidate. This task reproduces the first-principles evidence that links the VAsVGa complex to the EL6 level by computing its defect level energies and formation energies at different depths within the crystal. Understanding whether this complex can generate an EL6-like donor level and how its stability varies from the surface to the interior is essential for interpreting the photoelectronic behavior of SI-GaAs devices.

## Approach
The calculation uses density functional theory with a hybrid exchange-correlation functional to describe the GaAs system accurately. A 64-atom supercell of zincblende GaAs serves as the bulk reference. VAsVGa complex defects are introduced by removing one adjacent Ga and As atom pair at three distinct locations: (1) at the surface of a (001)-oriented slab with vacuum, (2) in the bulk at a depth of 5.65 Å from the boundary, and (3) in the bulk at a depth of 2.83 Å from the boundary. For each model, atomic positions are relaxed while keeping the cell dimensions fixed. After relaxation, the electronic band structure and total density of states are computed. From those outputs, the lowest-lying donor defect level below the conduction band minimum is identified, and the formation energy is evaluated using the total energies together with elemental chemical potentials for Ga and As. Additionally, the k-point location of the conduction band minimum and valence band maximum is determined for each configuration. The goal is to compare the defect level positions and formation energies across the three positions, testing whether a consistent EL6-like donor level appears and how the formation energy changes with depth.

## Reproduction target
Produce a single JSON file, `/app/outputs/defect_results.json`, that contains the extracted defect properties for the three VAsVGa complex models (surface, internal deep at 5.65 Å, internal shallow at 2.83 Å). For each model, report:
- `defect_level`: the energy of the lowest donor defect level relative to the conduction band minimum, in electron volts (eV).
- `formation_energy`: the formation energy of the neutral VAsVGa complex, in eV.
- `cbm_vbm_same_kpoint`: a boolean indicating whether the conduction band minimum and valence band maximum are located at the same k-point (Gamma point).

All calculations must be performed with an open-source DFT code capable of hybrid functionals and using pseudopotentials for Ga and As. The agent may choose the specific code, functional mixing, pseudopotential library, and other computational parameters, as long as the final JSON follows the required schema.

## Assets

- Open-source DFT code with hybrid functional capability (e.g., Quantum ESPRESSO, GPAW, CP2K): https://www.quantum-espresso.org/
- Pseudopotentials for Ga and As (norm-conserving or PAW): https://www.pseudo-dojo.org/

## Workflow steps

### Step 1: Perfect GaAs DFT reference calculation
- Role: process
- Action: Perform a DFT calculation with a hybrid functional for a perfect GaAs bulk supercell containing 64 atoms (zincblende structure). Relax atomic positions and obtain the total energy, Fermi level, and band structure. Save the total energy to perfect_energy.txt.
- Evidence: `/app/outputs/perfect_energy.txt`

### Step 2: Surface VAsVGa defect DFT calculation
- Role: process
- Action: Construct a GaAs(001) slab from the bulk supercell with crystal thickness 8.24 Å and vacuum 20.00 Å, and create a surface VAsVGa complex defect by removing an adjacent As and Ga atom at the surface. Perform DFT relaxation keeping cell dimensions fixed, compute band structure and total DOS. Save the total energy to surface_energy.txt.
- Evidence: `/app/outputs/surface_energy.txt`

### Step 3: Internal deep-layer VAsVGa defect DFT calculation
- Role: process
- Action: In the perfect bulk supercell, introduce a VAsVGa defect such that the center of the defect is 5.65 Å from the upper boundary. Relax atomic positions, compute band structure and DOS. Save the total energy to deep_energy.txt.
- Evidence: `/app/outputs/deep_energy.txt`

### Step 4: Internal shallow-layer VAsVGa defect DFT calculation
- Role: process
- Action: Similarly, introduce a VAsVGa defect at a depth of 2.83 Å from the upper boundary. Relax, compute band structure and DOS. Save the total energy to shallow_energy.txt.
- Evidence: `/app/outputs/shallow_energy.txt`

### Step 5: Extract defect levels and formation energies
- Role: scored (load-bearing)
- Action: Using all DFT outputs, determine the conduction band minimum (CBM) and valence band maximum (VBM). For the surface, internal_deep, and internal_shallow defect models, identify the lowest donor defect level nearest to CBM and compute its energy relative to CBM (in eV). Compute the formation energy using total energies and appropriate chemical potentials for Ga and As. Determine whether the CBM and VBM are at the same k-point (Gamma point) for each model. Compile all results into a JSON file.
- Output file: `/app/outputs/defect_results.json`
- Format: json
- Contract: JSON object with keys 'surface', 'internal_deep', 'internal_shallow'. Each key maps to an object with keys: 'defect_level' (float, eV), 'formation_energy' (float, eV), 'cbm_vbm_same_kpoint' (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_results.json
- path: `/app/outputs/defect_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final defect properties: lowest donor level, formation energy, and CBM/VBM k-point information for surface, deep internal, and shallow internal VAsVGa complex defects.
- schema:
  - `type`: object
  - `required`: `surface`, `internal_deep`, `internal_shallow`
  - `properties`:
    - `surface`:
      - `type`: object
      - `required`: `defect_level`, `formation_energy`, `cbm_vbm_same_kpoint`
      - `properties`:
        - `defect_level`:
          - `type`: number
          - `description`: Energy of lowest donor level below conduction band minimum, in eV
        - `formation_energy`:
          - `type`: number
          - `description`: Formation energy of the defect, in eV
        - `cbm_vbm_same_kpoint`:
          - `type`: boolean
          - `description`: Whether conduction band minimum and valence band maximum are at the same k-point
    - `internal_deep`:
      - `type`: object
      - `required`: `defect_level`, `formation_energy`, `cbm_vbm_same_kpoint`
      - `properties`:
        - `defect_level`:
          - `type`: number
          - `description`: Energy of lowest donor level below conduction band minimum, in eV
        - `formation_energy`:
          - `type`: number
          - `description`: Formation energy of the defect, in eV
        - `cbm_vbm_same_kpoint`:
          - `type`: boolean
          - `description`: Whether conduction band minimum and valence band maximum are at the same k-point
    - `internal_shallow`:
      - `type`: object
      - `required`: `defect_level`, `formation_energy`, `cbm_vbm_same_kpoint`
      - `properties`:
        - `defect_level`:
          - `type`: number
          - `description`: Energy of lowest donor level below conduction band minimum, in eV
        - `formation_energy`:
          - `type`: number
          - `description`: Formation energy of the defect, in eV
        - `cbm_vbm_same_kpoint`:
          - `type`: boolean
          - `description`: Whether conduction band minimum and valence band maximum are at the same k-point

Notes: The formation energy calculation should use standard elemental bulk references for chemical potentials. All values are at zero charge state. The agent is free to choose the hybrid functional mix and exact computational settings, but must report results consistent with the expected physical picture.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "surface",
          "internal_deep",
          "internal_shallow"
        ],
        "properties": {
          "surface": {
            "type": "object",
            "required": [
              "defect_level",
              "formation_energy",
              "cbm_vbm_same_kpoint"
            ],
            "properties": {
              "defect_level": {
                "type": "number",
                "description": "Energy of lowest donor level below conduction band minimum, in eV"
              },
              "formation_energy": {
                "type": "number",
                "description": "Formation energy of the defect, in eV"
              },
              "cbm_vbm_same_kpoint": {
                "type": "boolean",
                "description": "Whether conduction band minimum and valence band maximum are at the same k-point"
              }
            }
          },
          "internal_deep": {
            "type": "object",
            "required": [
              "defect_level",
              "formation_energy",
              "cbm_vbm_same_kpoint"
            ],
            "properties": {
              "defect_level": {
                "type": "number",
                "description": "Energy of lowest donor level below conduction band minimum, in eV"
              },
              "formation_energy": {
                "type": "number",
                "description": "Formation energy of the defect, in eV"
              },
              "cbm_vbm_same_kpoint": {
                "type": "boolean",
                "description": "Whether conduction band minimum and valence band maximum are at the same k-point"
              }
            }
          },
          "internal_shallow": {
            "type": "object",
            "required": [
              "defect_level",
              "formation_energy",
              "cbm_vbm_same_kpoint"
            ],
            "properties": {
              "defect_level": {
                "type": "number",
                "description": "Energy of lowest donor level below conduction band minimum, in eV"
              },
              "formation_energy": {
                "type": "number",
                "description": "Formation energy of the defect, in eV"
              },
              "cbm_vbm_same_kpoint": {
                "type": "boolean",
                "description": "Whether conduction band minimum and valence band maximum are at the same k-point"
              }
            }
          }
        }
      },
      "description": "Final defect properties: lowest donor level, formation energy, and CBM/VBM k-point information for surface, deep internal, and shallow internal VAsVGa complex defects."
    }
  ],
  "notes": "The formation energy calculation should use standard elemental bulk references for chemical potentials. All values are at zero charge state. The agent is free to choose the hybrid functional mix and exact computational settings, but must report results consistent with the expected physical picture."
}
```

## How you are scored
A hidden verifier will independently read your `defect_results.json` and compare each reported value against a hidden reference derived from a peer-reviewed DFT study of the same system. The evaluation consists of two parts:
1. **Numerical match**: The `defect_level` and `formation_energy` values for each model are compared to the reference. Your values must lie within tolerances that account for legitimate differences between DFT codes, pseudopotentials, and hybrid functional settings. Exact agreement with any particular setup is not required; a correct physical result obtained via a different open-source code can still achieve full credit.
2. **Trend verification**: The reported formation energies must satisfy the monotonic trend: `surface` > `internal_shallow` > `internal_deep`. The boolean `cbm_vbm_same_kpoint` fields are checked against the reference as well.

Your reward is a weighted sum of these checks. The greatest weight is given to the numerical agreement of the defect level and formation energy for the surface model, with progressively smaller weights for the internal models, while the trend and k-point checks contribute a smaller but non-zero portion. The total reward is a float between 0.0 and 1.0, with 1.0 indicating all numerical and structural criteria are satisfied. Reporting the paper’s numerical values verbatim without performing the required DFT calculations will not pass the verifier’s spatial and trend checks.
