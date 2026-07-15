# DFT Electronic Structure of Intermediate-Band Photovoltaic Compounds

## Problem background
Intermediate-band (IB) solar cells can surpass the single-junction Shockley–Queisser limit by splitting the main band gap into two sub-gaps with an intermediate band. Finding bulk materials that naturally host such an isolated, partially filled IB is an active area of computational materials discovery. This task addresses the electronic structure analysis of a set of candidate IB compounds: using density functional theory (DFT) to compute band structures, density of states, and carrier effective masses is central to evaluating their potential as photovoltaic absorbers.

## Approach
The workflow uses plane-wave DFT with a generalized-gradient approximation (GGA) exchange-correlation functional (e.g., PBE). The crystal structures are obtained from public databases, and high-symmetry k-point paths are determined via the Bilbao Crystallographic Server. Structural relaxation is performed to obtain ground-state geometries, followed by non-self-consistent band structure calculations and both total and site-projected density-of-states (DOS) computations. From the resulting electronic structure the band gap parameters that characterise the intermediate band (Evi, Eci, ΔEi, total Eg, and band gap type) are extracted. The DOS data are analysed to identify the energy window of the intermediate band and the dominant atomic-orbital contributions. Finally, effective masses (light hole, heavy hole, electron) are calculated at the relevant band extrema using a finite-difference method applied to the band dispersion.

## Reproduction target
Using the open-source Quantum ESPRESSO package (or an equivalent plane-wave DFT code) and the PBE functional, compute the electronic structure for the three compounds Au2Cs2I6, Ag2GeBaS4, Ag2ZnSnS4. For each compound, produce the following as structured JSON files:

1. Band gap parameters: Evi (energy gap from valence band maximum to intermediate band minimum), Eci (intermediate band maximum to conduction band minimum), ΔEi (width of the intermediate band), the total band gap Eg, and whether the gap is direct or indirect.
2. DOS data: the energy grid, total DOS, and site-projected DOS (per element and orbital). Additionally, report the energy window of the intermediate band and list the dominant atomic orbitals that constitute that band.
3. Effective masses: the light-hole, heavy-hole, and electron effective masses (in units of electron mass) at the relevant band extrema, along a specified plane direction (e.g., [110]).

The outputs must be obtained by executing the DFT pipeline; the final JSON files should reflect the computed results, not literature values.

## Assets

- Crystal structures of Au2Cs2I6, Ag2GeBaS4, Ag2ZnSnS4: Public databases: DFTBD (https://dftbd.org) or Materials Project (https://materialsproject.org)
- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Bilbao Crystallographic Server: https://www.cryst.ehu.es
- Effective Mass Calculator (EMC): https://github.com/afonari/emc
- PBE pseudopotentials library: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare DFT input files
- Role: process
- Action: Obtain the crystal structures of Au2Cs2I6, Ag2GeBaS4, and Ag2ZnSnS4 from a public database. Determine the high-symmetry k-point path using the Bilbao Crystallographic Server. Generate Quantum ESPRESSO input files for structural relaxation and band structure/DOS calculations.
- Evidence: `/app/outputs/input_files_generated.txt`

### Step 2: Run DFT calculations
- Role: process
- Action: For each compound, perform DFT structural relaxation using a PBE functional. Then compute the electronic band structure along the high-symmetry path, total density of states (DOS), and site-projected DOS (PDOS). Store the raw DFT output files for post-processing.
- Evidence: `/app/outputs/dft_completed.json`

### Step 3: Extract band gap parameters
- Role: scored
- Action: From the calculated band structures, determine for each compound: Evi (VB to IB minimum), Eci (IB maximum to CB minimum), ΔEi (width of IB), total Eg, and band gap type (direct/indirect). Output structured JSON.
- Output file: `/app/outputs/band_structure_data.json`
- Format: json
- Contract: Array of objects; each object has keys: compound (string), Evi (number, eV), Eci (number, eV), delta_Ei (number, eV), total_Eg (number, eV), gap_type (string 'direct' or 'indirect').
- Scoring: scored by hidden verifier

### Step 4: Extract DOS and orbital character
- Role: scored
- Action: From the DFT output, extract total DOS and site-projected DOS for each compound. Identify the energy window of the intermediate band and the dominant orbital contributions (e.g., I 2p, S 2p, Sn 5s). Output structured JSON.
- Output file: `/app/outputs/dos_data.json`
- Format: json
- Contract: Array of objects; each object has keys: compound (string), energy_grid (array of numbers, eV), total_dos (array of numbers, states/eV), projected_dos (object: element -> orbital -> array of numbers, states/eV), ib_energy_window (array of two numbers, eV), dominant_orbitals (array of strings).
- Scoring: scored by hidden verifier

### Step 5: Calculate effective masses
- Role: scored (load-bearing)
- Action: Using the band structure data and the finite difference method (e.g., Effective Mass Calculator tool or equivalent), compute the effective masses of light hole, heavy hole, and electron for each compound at the relevant band extrema. Output structured JSON.
- Output file: `/app/outputs/effective_masses.json`
- Format: json
- Contract: Array of objects; each object has keys: compound (string), plane_direction (string), light_hole_effective_mass (number, me), heavy_hole_effective_mass (number, me), electron_effective_mass (number, me).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure_data.json`
- `/app/outputs/dos_data.json`
- `/app/outputs/effective_masses.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure_data.json
- path: `/app/outputs/band_structure_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap values Evi, Eci, delta_Ei, total Eg, and gap type for each compound.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `Evi`, `Eci`, `delta_Ei`, `total_Eg`, `gap_type`
    - `properties`:
      - `compound`:
        - `type`: string
      - `Evi`:
        - `type`: number
        - `units`: eV
      - `Eci`:
        - `type`: number
        - `units`: eV
      - `delta_Ei`:
        - `type`: number
        - `units`: eV
      - `total_Eg`:
        - `type`: number
        - `units`: eV
      - `gap_type`:
        - `type`: string
        - `enum`: `direct`, `indirect`

### dos_data.json
- path: `/app/outputs/dos_data.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Total DOS, site-projected DOS, IB window, and dominant orbital character for each compound.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `energy_grid`, `total_dos`, `projected_dos`, `ib_energy_window`, `dominant_orbitals`
    - `properties`:
      - `compound`:
        - `type`: string
      - `energy_grid`:
        - `type`: array
        - `items`:
          - `type`: number
        - `units`: eV
      - `total_dos`:
        - `type`: array
        - `items`:
          - `type`: number
        - `units`: states/eV
      - `projected_dos`:
        - `type`: object
        - `additionalProperties`:
          - `type`: object
          - `additionalProperties`:
            - `type`: array
            - `items`:
              - `type`: number
            - `units`: states/eV
      - `ib_energy_window`:
        - `type`: array
        - `items`:
          - `type`: number
        - `minItems`: 2
        - `maxItems`: 2
        - `units`: eV
      - `dominant_orbitals`:
        - `type`: array
        - `items`:
          - `type`: string

### effective_masses.json
- path: `/app/outputs/effective_masses.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Effective masses (light hole, heavy hole, electron) for each compound.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `plane_direction`, `light_hole_effective_mass`, `heavy_hole_effective_mass`, `electron_effective_mass`
    - `properties`:
      - `compound`:
        - `type`: string
      - `plane_direction`:
        - `type`: string
      - `light_hole_effective_mass`:
        - `type`: number
        - `units`: me
      - `heavy_hole_effective_mass`:
        - `type`: number
        - `units`: me
      - `electron_effective_mass`:
        - `type`: number
        - `units`: me

Notes: All energy values in eV, effective masses in units of electron mass (me). GGA-PBE is the assumed exchange-correlation functional.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "Evi",
            "Eci",
            "delta_Ei",
            "total_Eg",
            "gap_type"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "Evi": {
              "type": "number",
              "units": "eV"
            },
            "Eci": {
              "type": "number",
              "units": "eV"
            },
            "delta_Ei": {
              "type": "number",
              "units": "eV"
            },
            "total_Eg": {
              "type": "number",
              "units": "eV"
            },
            "gap_type": {
              "type": "string",
              "enum": [
                "direct",
                "indirect"
              ]
            }
          }
        }
      },
      "description": "Band gap values Evi, Eci, delta_Ei, total Eg, and gap type for each compound."
    },
    {
      "file": "dos_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "energy_grid",
            "total_dos",
            "projected_dos",
            "ib_energy_window",
            "dominant_orbitals"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "energy_grid": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "units": "eV"
            },
            "total_dos": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "units": "states/eV"
            },
            "projected_dos": {
              "type": "object",
              "additionalProperties": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "units": "states/eV"
                }
              }
            },
            "ib_energy_window": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 2,
              "maxItems": 2,
              "units": "eV"
            },
            "dominant_orbitals": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      },
      "description": "Total DOS, site-projected DOS, IB window, and dominant orbital character for each compound."
    },
    {
      "file": "effective_masses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "plane_direction",
            "light_hole_effective_mass",
            "heavy_hole_effective_mass",
            "electron_effective_mass"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "plane_direction": {
              "type": "string"
            },
            "light_hole_effective_mass": {
              "type": "number",
              "units": "me"
            },
            "heavy_hole_effective_mass": {
              "type": "number",
              "units": "me"
            },
            "electron_effective_mass": {
              "type": "number",
              "units": "me"
            }
          }
        }
      },
      "description": "Effective masses (light hole, heavy hole, electron) for each compound."
    }
  ],
  "notes": "All energy values in eV, effective masses in units of electron mass (me). GGA-PBE is the assumed exchange-correlation functional."
}
```

## How you are scored
Each output file is scored independently by a hidden verifier. For band parameters and effective masses, the verifier compares your reported values against reference targets derived from the original study, applying tolerances that reflect the expected spread of a PBE calculation with different software. The DOS output is audited for structural consistency: the intermediate band energy window must be plausible given the band structure, and the dominant orbital character must match the expected chemical species. The final reward is a weighted combination of the scores from each output artifact. Simply writing down the reference numbers without performing the DFT calculations will not satisfy these checks.
