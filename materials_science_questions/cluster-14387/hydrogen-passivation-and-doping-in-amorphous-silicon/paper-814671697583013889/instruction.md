# Density functional theory study of hydrogen in diamond: surface and subsurface configurations

## Problem background
Diamond films that are hydrogen-terminated exhibit high surface electrical conductivity while the bulk remains insulating. The origin of this conductivity is controversial: some studies attribute it to surface-chemisorbed hydrogen atoms, whereas others suggest that hydrogen atoms that have diffused into the subsurface region play the dominant role. Density functional theory (DFT) can be used to calculate the electronic density of states (DOS) of various hydrogen-in-diamond configurations, to assess which structures produce gap states capable of supporting surface transport.

## Approach
A set of atomic models are constructed and their electronic structure is computed with plane-wave DFT. The exchange-correlation functional GGA-PW91 and ultrasoft pseudopotentials are used, as implemented in the open-source Quantum ESPRESSO code. Four kinds of system are compared: (i) a monohydrogenated C(100) 2×1 surface slab, (ii) a 64-atom diamond supercell containing a single hydrogen atom placed at a C–C bond-centre site, (iii) the most stable supercell with two subsurface hydrogen atoms (determined by comparing total energies of candidate placements), and (iv) the most stable supercell with three subsurface hydrogen atoms (similarly determined). For each system, geometry relaxation is performed first, then the total DOS is computed. The resulting DOS curves show whether the electronic gap contains states and, if so, at which energies relative to the Fermi level. The comparison across these four regimes directly addresses the role of surface-only and subsurface hydrogen.

## Reproduction target
Produce four DOS curves as comma-separated value files (energy in eV with the Fermi level at 0, total DOS in arbitrary units, no header):
- dos_slab.csv: monohydrogenated C(100) 2×1 surface slab.
- dos_isolated_H.csv: 64-atom supercell with one bond-centre hydrogen.
- dos_two_H.csv: 64-atom supercell with the most stable two‑hydrogen subsurface configuration.
- dos_three_H.csv: 64-atom supercell with the most stable three‑hydrogen subsurface configuration.
Additionally, summarize the electronic properties in a JSON file (summary.json) containing, for each system, the band gap width (distance from valence band maximum to conduction band minimum), a boolean indicating whether gap states are present, and a list of gap‑state peak energies (relative to the Fermi level).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PW91 ultrasoft pseudopotentials for C and H: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Build atomic models
- Role: process
- Action: Construct the four required atomic models: (i) a monohydrogenated C(100) 2x1 surface slab with 10 layers of carbon atoms, hydrogen termination on both top and bottom, and 15 Å vacuum; (ii) a 64-atom diamond supercell with one hydrogen at a C-C bond centre (C-Hbc-C); (iii) two supercells for the two-hydrogen configurations: C-2Hbc-C (both H at bond-centre sites) and C-Hbc-C-Hab (one at bond-centre, one at antibonding site); (iv) three supercells for the three-hydrogen configurations: C-3Hbc-C, C-2Hbc-C-Hab, and C-Hbc-C-2Hab. Record each structure in a standard format suitable for DFT input.
- Evidence: `/app/outputs/model_structures.txt`

### Step 2: DFT for monohydrogenated C(100) surface
- Role: scored
- Action: Perform DFT geometry relaxation and total density of states (DOS) calculation for the slab model using Quantum ESPRESSO, the GGA-PW91 exchange-correlation functional, and ultrasoft pseudopotentials. Save the total DOS as a comma-separated file with energy (eV, Fermi level at 0) and total DOS (arbitrary units).
- Output file: `/app/outputs/dos_slab.csv`
- Format: csv
- Contract: Two columns: energy (eV, Fermi level at 0) and total_dos (arbitrary units). No header.
- Scoring: scored by hidden verifier

### Step 3: DFT for isolated subsurface hydrogen
- Role: scored
- Action: Perform DFT geometry relaxation and total DOS for the 64-atom supercell with one hydrogen at the C-C bond centre (C-Hbc-C) using the same functional and pseudopotentials as the slab calculation. Output the total DOS as a CSV with energy (eV) and total DOS (arbitrary units).
- Output file: `/app/outputs/dos_isolated_H.csv`
- Format: csv
- Contract: Two columns: energy (eV, Fermi level at 0) and total_dos (arbitrary units). No header.
- Scoring: scored by hidden verifier

### Step 4: Determine most stable two-hydrogen subsurface configuration
- Role: process
- Action: For each of the two-hydrogen configurations (C-2Hbc-C and C-Hbc-C-Hab), perform a DFT geometry optimization using the same functional, pseudopotentials, and supercell parameters. Compare the final total energies and identify the lower-energy structure. Record the energies and the selected configuration.
- Evidence: `/app/outputs/two_H_stability.json`

### Step 5: DFT for the stable two-hydrogen subsurface configuration
- Role: scored
- Action: Using the most stable configuration identified in the previous step (expected to be C-Hbc-C-Hab), perform a DFT geometry relaxation and total DOS calculation. Save the DOS as a CSV with energy (eV) and total DOS (arbitrary units).
- Output file: `/app/outputs/dos_two_H.csv`
- Format: csv
- Contract: Two columns: energy (eV, Fermi level at 0) and total_dos (arbitrary units). No header.
- Scoring: scored by hidden verifier

### Step 6: Determine most stable three-hydrogen subsurface configuration
- Role: process
- Action: For each of the three-hydrogen configurations (C-3Hbc-C, C-2Hbc-C-Hab, C-Hbc-C-2Hab), run DFT geometry optimization with the same supercell parameters. Compare the total energies and select the lowest-energy structure. Record the energies and chosen structure.
- Evidence: `/app/outputs/three_H_stability.json`

### Step 7: DFT for the stable three-hydrogen subsurface configuration
- Role: scored (load-bearing)
- Action: For the most stable three-hydrogen configuration (expected to be C-3Hbc-C), perform geometry relaxation and total DOS calculation with the same supercell parameters. Save the DOS as a CSV. This step is load-bearing because its surface states near the Fermi level are the central result and can only be obtained by genuinely running the DFT calculation.
- Output file: `/app/outputs/dos_three_H.csv`
- Format: csv
- Contract: Two columns: energy (eV, Fermi level at 0) and total_dos (arbitrary units). No header.
- Scoring: scored by hidden verifier

### Step 8: Summarize band gap and gap states from all DOS
- Role: scored
- Action: Analyze each of the four DOS CSV files to extract: band gap width (distance from valence band maximum to conduction band minimum), whether any states exist inside the gap, and if so their peak energies (relative to Fermi level). Output a JSON file with the extracted features for all four systems.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: JSON object with keys 'slab', 'isolated_H', 'two_H', 'three_H'. Each value is an object containing: 'band_gap_width_eV' (float, distance from VBM to CBM edges), 'has_gap_states' (bool), 'gap_states_energies_eV' (array of floats, energies relative to Fermi level if present).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_slab.csv`
- `/app/outputs/dos_isolated_H.csv`
- `/app/outputs/dos_two_H.csv`
- `/app/outputs/dos_three_H.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_slab.csv
- path: `/app/outputs/dos_slab.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for the hydrogen-terminated diamond(100) slab. Two columns (energy in eV with Fermi level at 0, total DOS) without header.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_dos`
  - `units`:
    - `energy_eV`: eV
    - `total_dos`: arbitrary units

### dos_isolated_H.csv
- path: `/app/outputs/dos_isolated_H.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for the supercell with one bond-centre hydrogen atom.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_dos`
  - `units`:
    - `energy_eV`: eV
    - `total_dos`: arbitrary units

### dos_two_H.csv
- path: `/app/outputs/dos_two_H.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for the most stable two-hydrogen subsurface structure.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_dos`
  - `units`:
    - `energy_eV`: eV
    - `total_dos`: arbitrary units

### dos_three_H.csv
- path: `/app/outputs/dos_three_H.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for the most stable three-hydrogen subsurface structure (C-3Hbc-C).
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_dos`
  - `units`:
    - `energy_eV`: eV
    - `total_dos`: arbitrary units

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON summary of band-gap properties (band gap width, presence/absence of gap states, peak energies relative to Fermi level) for all four systems, derived from the DOS files.
- schema:
  - `type`: object
  - `required`: `slab`, `isolated_H`, `two_H`, `three_H`
  - `properties`:
    - `slab`:
      - `type`: object
      - `required`: `band_gap_width_eV`, `has_gap_states`, `gap_states_energies_eV`
      - `properties`:
        - `band_gap_width_eV`:
          - `type`: number
        - `has_gap_states`:
          - `type`: boolean
        - `gap_states_energies_eV`:
          - `type`: array
          - `items`:
            - `type`: number
    - `isolated_H`:
      - `type`: object
      - `required`: `band_gap_width_eV`, `has_gap_states`, `gap_states_energies_eV`
      - `properties`:
        - `band_gap_width_eV`:
          - `type`: number
        - `has_gap_states`:
          - `type`: boolean
        - `gap_states_energies_eV`:
          - `type`: array
          - `items`:
            - `type`: number
    - `two_H`:
      - `type`: object
      - `required`: `band_gap_width_eV`, `has_gap_states`, `gap_states_energies_eV`
      - `properties`:
        - `band_gap_width_eV`:
          - `type`: number
        - `has_gap_states`:
          - `type`: boolean
        - `gap_states_energies_eV`:
          - `type`: array
          - `items`:
            - `type`: number
    - `three_H`:
      - `type`: object
      - `required`: `band_gap_width_eV`, `has_gap_states`, `gap_states_energies_eV`
      - `properties`:
        - `band_gap_width_eV`:
          - `type`: number
        - `has_gap_states`:
          - `type`: boolean
        - `gap_states_energies_eV`:
          - `type`: array
          - `items`:
            - `type`: number

Notes: The checker will recompute band gap features from the DOS CSV files and verify consistency with the summary.json. Peak energies will be compared against expected values within tolerances; full credit requires correct presence/absence of gap states and peak locations within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_slab.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_dos"
        ],
        "units": {
          "energy_eV": "eV",
          "total_dos": "arbitrary units"
        }
      },
      "description": "Total density of states for the hydrogen-terminated diamond(100) slab. Two columns (energy in eV with Fermi level at 0, total DOS) without header."
    },
    {
      "file": "dos_isolated_H.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_dos"
        ],
        "units": {
          "energy_eV": "eV",
          "total_dos": "arbitrary units"
        }
      },
      "description": "Total density of states for the supercell with one bond-centre hydrogen atom."
    },
    {
      "file": "dos_two_H.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_dos"
        ],
        "units": {
          "energy_eV": "eV",
          "total_dos": "arbitrary units"
        }
      },
      "description": "Total density of states for the most stable two-hydrogen subsurface structure."
    },
    {
      "file": "dos_three_H.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_dos"
        ],
        "units": {
          "energy_eV": "eV",
          "total_dos": "arbitrary units"
        }
      },
      "description": "Total density of states for the most stable three-hydrogen subsurface structure (C-3Hbc-C)."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "slab",
          "isolated_H",
          "two_H",
          "three_H"
        ],
        "properties": {
          "slab": {
            "type": "object",
            "required": [
              "band_gap_width_eV",
              "has_gap_states",
              "gap_states_energies_eV"
            ],
            "properties": {
              "band_gap_width_eV": {
                "type": "number"
              },
              "has_gap_states": {
                "type": "boolean"
              },
              "gap_states_energies_eV": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "isolated_H": {
            "type": "object",
            "required": [
              "band_gap_width_eV",
              "has_gap_states",
              "gap_states_energies_eV"
            ],
            "properties": {
              "band_gap_width_eV": {
                "type": "number"
              },
              "has_gap_states": {
                "type": "boolean"
              },
              "gap_states_energies_eV": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "two_H": {
            "type": "object",
            "required": [
              "band_gap_width_eV",
              "has_gap_states",
              "gap_states_energies_eV"
            ],
            "properties": {
              "band_gap_width_eV": {
                "type": "number"
              },
              "has_gap_states": {
                "type": "boolean"
              },
              "gap_states_energies_eV": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "three_H": {
            "type": "object",
            "required": [
              "band_gap_width_eV",
              "has_gap_states",
              "gap_states_energies_eV"
            ],
            "properties": {
              "band_gap_width_eV": {
                "type": "number"
              },
              "has_gap_states": {
                "type": "boolean"
              },
              "gap_states_energies_eV": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "JSON summary of band-gap properties (band gap width, presence/absence of gap states, peak energies relative to Fermi level) for all four systems, derived from the DOS files."
    }
  ],
  "notes": "The checker will recompute band gap features from the DOS CSV files and verify consistency with the summary.json. Peak energies will be compared against expected values within tolerances; full credit requires correct presence/absence of gap states and peak locations within tolerance."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files and summary JSON. It independently locates the Fermi level in each DOS curve, identifies peaks inside the band gap, and compares the presence/absence of gap states and their energies against reference expectations. The consistency of the summary with the DOS data is also checked. Your reward is a weighted combination of these checks: correctness of the gap‑state findings carries substantial weight, while the summary consistency adds a minor share. The verifier recomputes properties from your raw data; simply reporting expected numbers is not sufficient.
