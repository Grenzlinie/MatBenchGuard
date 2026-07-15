# First-principles DFT and thermoelectric transport calculations for Ca5M2As6 (M=Sn,Ga)

## Problem background
Zintl phases Ca5M2As6 (M = Sn, Ga) contain infinite one-dimensional chains of corner-shared MAs4 tetrahedra that are separated by Ca cations. In Ca5Ga2As6, adjacent chains are linked by As–As dimers, while Ca5Sn2As6 adopts a structure type with no As–As bonding between the chains. The presence or absence of these inter-chain As–As bonds is believed to modify the electronic density of states, the Seebeck coefficient, the anisotropy of the electrical conductivity, and the lattice thermal conductivity, thereby influencing the thermoelectric performance. This task computes the key quantities that characterise these effects for both compounds.

## Approach
Starting from the crystal structures of Ca5Sn2As6 and Ca5Ga2As6, full geometry optimisation is performed with DFT using the PBE functional and PAW pseudopotentials. The optimised structures are then used for two independent branches. First, accurate electronic band structures are obtained with a DFT method that yields reliable band gaps (e.g., MBJ or a hybrid functional); the band gap value and its direct/indirect character are extracted for each compound. Second, the semiclassical Boltzmann transport theory (BoltzTrap) is applied to the band structure to compute the intrinsic (undoped) Seebeck coefficient as a function of temperature; the maximum p-type Seebeck coefficient and the temperature at which it occurs are identified. Separately, single-crystal elastic constants are computed via stress–strain DFT; using the Voigt–Reuss–Hill average, the sound velocities are derived and fed into the Cahill model to estimate the minimum lattice thermal conductivity.

## Reproduction target
For Ca5Sn2As6 and Ca5Ga2As6, produce the following three scored output files under /app/outputs:
- band_gaps.json: band gap in eV and the direct/indirect character for each compound.
- seebeck_max.json: the maximum intrinsic p-type Seebeck coefficient (µV/K) and the corresponding temperature (K) for each compound.
- kappa_min.json: the minimum lattice thermal conductivity (W/m·K) for each compound, computed via the Cahill model from elastic constants.

## Assets

- Crystal structures of Ca5Sn2As6 and Ca5Ga2As6: 10.1002/zaac.19855300106 (Ca5Sn2As6), 10.1107/S0567740876003981 (Ca5Ga2As6)
- DFT software (e.g., Quantum ESPRESSO, GPAW, ABINIT): https://www.quantum-espresso.org
- BoltzTrap or BoltzTrap2 transport code: https://www.saule.cyfronet.pl/~majewsk/boltz/

## Workflow steps

### Step 1: Prepare initial crystal structures
- Role: process
- Action: Obtain or construct the crystal structures of Ca5Sn2As6 and Ca5Ga2As6 from public ICSD entries or from the published lattice parameters and atomic coordinates. Create input files for DFT calculations.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform full geometry optimization (relaxing lattice parameters and atomic positions) for both Ca5Sn2As6 and Ca5Ga2As6 using DFT with PBE functional and PAW pseudopotentials. Save optimized structures.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 3: Electronic structure and band gap calculation
- Role: scored (load-bearing)
- Action: Using the optimized structures, compute band structures with a DFT method that yields accurate band gaps (e.g., MBJ or a hybrid functional). Extract the band gap value (eV) and classify as direct or indirect for each compound. Write results to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"Ca5Sn2As6": {"band_gap_eV": number, "type": "indirect"}, "Ca5Ga2As6": {"band_gap_eV": number, "type": "direct"}}
- Scoring: scored by hidden verifier

### Step 4: Thermoelectric transport – Seebeck maxima
- Role: scored (load-bearing)
- Action: From the band structure of each compound, compute the intrinsic (undoped) Seebeck coefficient as a function of temperature using the semiclassical Boltzmann theory (BoltzTrap). Identify the maximum p-type Seebeck coefficient (in µV/K) and the temperature (K) at which it occurs for each compound. Write results to seebeck_max.json.
- Output file: `/app/outputs/seebeck_max.json`
- Format: json
- Contract: {"Ca5Sn2As6": {"S_max_microV_per_K": number, "T_K": number}, "Ca5Ga2As6": {"S_max_microV_per_K": number, "T_K": number}}
- Scoring: scored by hidden verifier

### Step 5: Elastic constants and sound velocities
- Role: process
- Action: Compute the single-crystal elastic constants (c_ij) for both compounds via stress–strain DFT. Apply the Voigt–Reuss–Hill approximation to obtain bulk modulus K and shear modulus G, then compute the longitudinal (ν_l) and transverse (ν_s) sound velocities.
- Evidence: `/app/outputs/elastic_properties.json`

### Step 6: Minimum lattice thermal conductivity
- Role: scored (load-bearing)
- Action: Using the sound velocities and unit-cell volume from previous steps, compute the minimum lattice thermal conductivity κ_min (W/m·K) via the Cahill model (κ_min = (1/2)(π/6)^(1/3) k_B V^(−2/3)(2ν_s + ν_l)). Write results to kappa_min.json.
- Output file: `/app/outputs/kappa_min.json`
- Format: json
- Contract: {"Ca5Sn2As6": number, "Ca5Ga2As6": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/seebeck_max.json`
- `/app/outputs/kappa_min.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gap values (eV) and direct/indirect character for Ca5Sn2As6 and Ca5Ga2As6.
- schema:
  - `type`: object
  - `required`: `Ca5Sn2As6`, `Ca5Ga2As6`
  - `properties`:
    - `Ca5Sn2As6`:
      - `type`: object
      - `required`: `band_gap_eV`, `type`
      - `properties`:
        - `band_gap_eV`:
          - `type`: number
        - `type`:
          - `type`: string
          - `enum`: `direct`, `indirect`
    - `Ca5Ga2As6`:
      - `type`: object
      - `required`: `band_gap_eV`, `type`
      - `properties`:
        - `band_gap_eV`:
          - `type`: number
        - `type`:
          - `type`: string
          - `enum`: `direct`, `indirect`

### seebeck_max.json
- path: `/app/outputs/seebeck_max.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Maximum p-type Seebeck coefficient (µV/K) and the corresponding temperature (K) for each compound.
- schema:
  - `type`: object
  - `required`: `Ca5Sn2As6`, `Ca5Ga2As6`
  - `properties`:
    - `Ca5Sn2As6`:
      - `type`: object
      - `required`: `S_max_microV_per_K`, `T_K`
      - `properties`:
        - `S_max_microV_per_K`:
          - `type`: number
        - `T_K`:
          - `type`: number
    - `Ca5Ga2As6`:
      - `type`: object
      - `required`: `S_max_microV_per_K`, `T_K`
      - `properties`:
        - `S_max_microV_per_K`:
          - `type`: number
        - `T_K`:
          - `type`: number

### kappa_min.json
- path: `/app/outputs/kappa_min.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Minimum lattice thermal conductivity (W/m·K) for Ca5Sn2As6 and Ca5Ga2As6.
- schema:
  - `type`: object
  - `required`: `Ca5Sn2As6`, `Ca5Ga2As6`
  - `properties`:
    - `Ca5Sn2As6`:
      - `type`: number
    - `Ca5Ga2As6`:
      - `type`: number

Notes: All values are computed from first-principles DFT and semiclassical Boltzmann transport; no gold values are given.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ca5Sn2As6",
          "Ca5Ga2As6"
        ],
        "properties": {
          "Ca5Sn2As6": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "type"
            ],
            "properties": {
              "band_gap_eV": {
                "type": "number"
              },
              "type": {
                "type": "string",
                "enum": [
                  "direct",
                  "indirect"
                ]
              }
            }
          },
          "Ca5Ga2As6": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "type"
            ],
            "properties": {
              "band_gap_eV": {
                "type": "number"
              },
              "type": {
                "type": "string",
                "enum": [
                  "direct",
                  "indirect"
                ]
              }
            }
          }
        }
      },
      "description": "Band gap values (eV) and direct/indirect character for Ca5Sn2As6 and Ca5Ga2As6."
    },
    {
      "file": "seebeck_max.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ca5Sn2As6",
          "Ca5Ga2As6"
        ],
        "properties": {
          "Ca5Sn2As6": {
            "type": "object",
            "required": [
              "S_max_microV_per_K",
              "T_K"
            ],
            "properties": {
              "S_max_microV_per_K": {
                "type": "number"
              },
              "T_K": {
                "type": "number"
              }
            }
          },
          "Ca5Ga2As6": {
            "type": "object",
            "required": [
              "S_max_microV_per_K",
              "T_K"
            ],
            "properties": {
              "S_max_microV_per_K": {
                "type": "number"
              },
              "T_K": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Maximum p-type Seebeck coefficient (µV/K) and the corresponding temperature (K) for each compound."
    },
    {
      "file": "kappa_min.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ca5Sn2As6",
          "Ca5Ga2As6"
        ],
        "properties": {
          "Ca5Sn2As6": {
            "type": "number"
          },
          "Ca5Ga2As6": {
            "type": "number"
          }
        }
      },
      "description": "Minimum lattice thermal conductivity (W/m·K) for Ca5Sn2As6 and Ca5Ga2As6."
    }
  ],
  "notes": "All values are computed from first-principles DFT and semiclassical Boltzmann transport; no gold values are given."
}
```

## How you are scored
A hidden verifier reads the three JSON files and independently compares each reported quantity to the expected reference values. Band gaps, Seebeck maxima and temperatures, and minimum lattice thermal conductivities are all checked with appropriate hidden tolerances. Each scored artifact contributes a weight to the final combined reward, which is a float between 0 and 1. The verifier scores what you write in the required output files; no separate self-reporting or log files are graded.
