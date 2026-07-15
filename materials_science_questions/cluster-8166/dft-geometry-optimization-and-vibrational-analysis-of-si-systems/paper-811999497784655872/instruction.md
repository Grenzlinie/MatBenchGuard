# DFT Crystal Structure and Charge Analysis of a Li-Si Alloy

## Problem background
Lithium-ion batteries use silicon as a promising anode material because of its large theoretical specific capacity. LiSi is the Li-poorest crystalline compound that forms during the initial lithiation of silicon. Understanding its crystal structure, bonding geometry, charge distribution, and average intercalation voltage is essential for characterizing the electrochemical Li–Si alloying mechanism. This task reproduces a density functional theory (DFT) study that determines these properties by performing first-principles calculations on LiSi, metallic lithium, and crystalline silicon.

## Approach
The work uses DFT calculations with the generalized gradient approximation (GGA) in the Perdew–Burke–Ernzerhof (PBE) formulation and an open-source plane-wave pseudopotential code. Three crystal structures are set up: a conventional tetragonal cell of LiSi (space group I4₁/a, 16 Li and 16 Si atoms), body-centred cubic (bcc) metallic lithium (2 Li atoms), and diamond silicon (8 Si atoms). The LiSi structure is relaxed (geometry optimization) to minimize total energy, while total-energy calculations are performed for the Li and Si references. From the relaxed LiSi cell, lattice constants, unit-cell volume and fractional atomic coordinates are extracted. Interatomic distances and bond angles are computed to characterize the bonding geometry. Total energies per formula unit for LiSi and per atom for Li and Si are obtained, and the average intercalation voltage for the reaction Li + Si → LiSi is calculated by approximating the Gibbs free energy change with the internal energy difference. Finally, the charge density from the LiSi calculation is integrated within Wigner–Seitz spheres (radii taken from the corresponding pure reference calculations) to obtain valence electron counts resolved by orbital angular momentum (s, p, d, and total), revealing the charge transfer between Li and Si.

## Reproduction target
Compute and report:
- The DFT-relaxed lattice constants a and c, unit-cell volume V, and fractional atomic coordinates of Li and Si in LiSi.
- The distinct Si–Si bond lengths, Li–Li bond lengths within and between the triangular pyramids, Li–Si bond distances, and Si–Si–Si bond angles derived from the relaxed structure.
- The total energies per formula unit for LiSi and per atom for metallic Li and crystalline Si.
- The average intercalation voltage V̄ = –(E[LiSi_per_fu] – E[Li_per_atom] – E[Si_per_atom]) / F, where F is the Faraday constant (assume 1 eV per electron so V̄ is in volts).
- The valence electron counts (s, p, d orbital contributions and total) within Wigner–Seitz spheres of radius 1.814 Å for Li and 1.5765 Å for Si, averaged over all symmetry-equivalent atoms in LiSi.

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO, CP2K) with PBE-GGA: https://www.quantum-espresso.org/
- PBE pseudopotentials for Li and Si (ultrasoft or PAW version, e.g., from SSSP library): https://github.com/SSSP/SSSP/tree/main/PBE

## Workflow steps

### Step 1: DFT geometry optimization of LiSi
- Role: process
- Action: Set up a conventional tetragonal cell of LiSi (space group I4_1/a, 16 Li and 16 Si atoms) and perform a PBE-GGA DFT geometry optimization using an open-source plane-wave code. Converge atomic positions and cell vectors; save the relaxed structure and charge density.
- Evidence: `/app/outputs/lisi_opt.log`

### Step 2: DFT reference calculation for metallic Li
- Role: process
- Action: Set up a bcc Li unit cell (2 Li atoms) and perform a PBE-GGA DFT static calculation to obtain the total energy and charge density.
- Evidence: `/app/outputs/li_ref.log`

### Step 3: DFT reference calculation for crystalline Si
- Role: process
- Action: Set up a diamond Si unit cell (8 Si atoms) and perform a PBE-GGA DFT static calculation to obtain the total energy and charge density.
- Evidence: `/app/outputs/si_ref.log`

### Step 4: Extract LiSi relaxed structure
- Role: scored
- Action: From the LiSi relaxation output, extract the lattice constants a (Å), c (Å), unit-cell volume V (Å³), and the fractional atomic coordinates of one Li atom and one Si atom. Write relaxed_structure.json.
- Output file: `/app/outputs/relaxed_structure.json`
- Format: json
- Contract: {"a": number (Å), "c": number (Å), "volume": number (Å³), "Li": {"x": number, "y": number, "z": number}, "Si": {"x": number, "y": number, "z": number}}
- Scoring: scored by hidden verifier

### Step 5: Compute bond lengths and angles
- Role: scored
- Action: Using the relaxed LiSi structure, compute the distinct Si–Si bond lengths (Å), Li–Li bond lengths (Å) within and between the triangular pyramids, Li–Si bond distances (Å), and Si–Si–Si bond angles (°). Write bond_data.json.
- Output file: `/app/outputs/bond_data.json`
- Format: json
- Contract: {"Si_Si_bonds": [number, number], "Li_Li_bonds": [number, number, number], "Li_Si_bonds": [number, ...], "Si_Si_Si_angles": [number, number, number]}
- Scoring: scored by hidden verifier

### Step 6: Report total energies
- Role: scored
- Action: Extract the total energy of the LiSi DFT calculation and divide by 16 to obtain energy per formula unit (eV). Similarly extract energies per atom for Li and Si from their reference calculations. Write total_energies.json.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: {"LiSi_per_fu": number (eV), "Li_per_atom": number (eV), "Si_per_atom": number (eV)}
- Scoring: scored by hidden verifier

### Step 7: Compute average intercalation voltage
- Role: scored
- Action: From the total energies per formula unit, calculate the average intercalation voltage V̄ = -(E[LiSi_per_fu] – E[Li_per_atom] – E[Si_per_atom]) / 1 (eV per electron, so V̄ is in volts). Write the number to intercalation_voltage.txt.
- Output file: `/app/outputs/intercalation_voltage.txt`
- Format: txt
- Contract: A single number (float) in volts.
- Scoring: scored by hidden verifier

### Step 8: Compute valence electron counts in Wigner–Seitz spheres
- Role: scored (load-bearing)
- Action: Integrate the charge density from the LiSi DFT calculation within Wigner–Seitz spheres of radius 1.814 Å for Li and 1.5765 Å for Si. Average over all symmetry-equivalent atoms. Report total and orbital (s, p, d) counts. Write electron_counts.json.
- Output file: `/app/outputs/electron_counts.json`
- Format: json
- Contract: {"Li_in_LiSi": {"s": number, "p": number, "d": number, "total": number}, "Si_in_LiSi": {"s": number, "p": number, "d": number, "total": number}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_structure.json`
- `/app/outputs/bond_data.json`
- `/app/outputs/total_energies.json`
- `/app/outputs/intercalation_voltage.txt`
- `/app/outputs/electron_counts.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_structure.json
- path: `/app/outputs/relaxed_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-relaxed lattice constants, unit-cell volume, and fractional coordinates of Li and Si in LiSi.
- schema:
  - `type`: object
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
    - `c`:
      - `type`: number
      - `unit`: Å
    - `volume`:
      - `type`: number
      - `unit`: Å³
    - `Li`:
      - `type`: object
      - `properties`:
        - `x`:
          - `type`: number
        - `y`:
          - `type`: number
        - `z`:
          - `type`: number
    - `Si`:
      - `type`: object
      - `properties`:
        - `x`:
          - `type`: number
        - `y`:
          - `type`: number
        - `z`:
          - `type`: number
  - `required`: `a`, `c`, `volume`, `Li`, `Si`

### bond_data.json
- path: `/app/outputs/bond_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Interatomic distances and bond angles computed from the relaxed LiSi structure.
- schema:
  - `type`: object
  - `properties`:
    - `Si_Si_bonds`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Si–Si bond lengths (Å)
    - `Li_Li_bonds`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Li–Li bond lengths (Å)
    - `Li_Si_bonds`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Li–Si bond distances (Å)
    - `Si_Si_Si_angles`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Si–Si–Si bond angles (°)
  - `required`: `Si_Si_bonds`, `Li_Li_bonds`, `Li_Si_bonds`, `Si_Si_Si_angles`

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energies per formula unit (LiSi) and per atom (Li, Si) from DFT calculations.
- schema:
  - `type`: object
  - `properties`:
    - `LiSi_per_fu`:
      - `type`: number
      - `unit`: eV
    - `Li_per_atom`:
      - `type`: number
      - `unit`: eV
    - `Si_per_atom`:
      - `type`: number
      - `unit`: eV
  - `required`: `LiSi_per_fu`, `Li_per_atom`, `Si_per_atom`

### intercalation_voltage.txt
- path: `/app/outputs/intercalation_voltage.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Average intercalation voltage V̄ for Li + Si → LiSi.
- schema:
  - `type`: text
  - `content`: A single number (float) in volts.

### electron_counts.json
- path: `/app/outputs/electron_counts.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Valence electron counts (s, p, d, total) within Wigner–Seitz spheres for Li and Si in LiSi.
- schema:
  - `type`: object
  - `properties`:
    - `Li_in_LiSi`:
      - `type`: object
      - `properties`:
        - `s`:
          - `type`: number
        - `p`:
          - `type`: number
        - `d`:
          - `type`: number
        - `total`:
          - `type`: number
      - `required`: `s`, `p`, `d`, `total`
    - `Si_in_LiSi`:
      - `type`: object
      - `properties`:
        - `s`:
          - `type`: number
        - `p`:
          - `type`: number
        - `d`:
          - `type`: number
        - `total`:
          - `type`: number
      - `required`: `s`, `p`, `d`, `total`
  - `required`: `Li_in_LiSi`, `Si_in_LiSi`

Notes: Outputs are compared against hidden reference values from the source paper with appropriate tolerances. The checker also recomputes the intercalation voltage from total_energies.json to ensure self-consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å"
          },
          "c": {
            "type": "number",
            "unit": "Å"
          },
          "volume": {
            "type": "number",
            "unit": "Å³"
          },
          "Li": {
            "type": "object",
            "properties": {
              "x": {
                "type": "number"
              },
              "y": {
                "type": "number"
              },
              "z": {
                "type": "number"
              }
            }
          },
          "Si": {
            "type": "object",
            "properties": {
              "x": {
                "type": "number"
              },
              "y": {
                "type": "number"
              },
              "z": {
                "type": "number"
              }
            }
          }
        },
        "required": [
          "a",
          "c",
          "volume",
          "Li",
          "Si"
        ]
      },
      "description": "DFT-relaxed lattice constants, unit-cell volume, and fractional coordinates of Li and Si in LiSi."
    },
    {
      "file": "bond_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "Si_Si_bonds": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Si–Si bond lengths (Å)"
          },
          "Li_Li_bonds": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Li–Li bond lengths (Å)"
          },
          "Li_Si_bonds": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Li–Si bond distances (Å)"
          },
          "Si_Si_Si_angles": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Si–Si–Si bond angles (°)"
          }
        },
        "required": [
          "Si_Si_bonds",
          "Li_Li_bonds",
          "Li_Si_bonds",
          "Si_Si_Si_angles"
        ]
      },
      "description": "Interatomic distances and bond angles computed from the relaxed LiSi structure."
    },
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "LiSi_per_fu": {
            "type": "number",
            "unit": "eV"
          },
          "Li_per_atom": {
            "type": "number",
            "unit": "eV"
          },
          "Si_per_atom": {
            "type": "number",
            "unit": "eV"
          }
        },
        "required": [
          "LiSi_per_fu",
          "Li_per_atom",
          "Si_per_atom"
        ]
      },
      "description": "Total energies per formula unit (LiSi) and per atom (Li, Si) from DFT calculations."
    },
    {
      "file": "intercalation_voltage.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content": "A single number (float) in volts."
      },
      "description": "Average intercalation voltage V̄ for Li + Si → LiSi."
    },
    {
      "file": "electron_counts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "Li_in_LiSi": {
            "type": "object",
            "properties": {
              "s": {
                "type": "number"
              },
              "p": {
                "type": "number"
              },
              "d": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "s",
              "p",
              "d",
              "total"
            ]
          },
          "Si_in_LiSi": {
            "type": "object",
            "properties": {
              "s": {
                "type": "number"
              },
              "p": {
                "type": "number"
              },
              "d": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "s",
              "p",
              "d",
              "total"
            ]
          }
        },
        "required": [
          "Li_in_LiSi",
          "Si_in_LiSi"
        ]
      },
      "description": "Valence electron counts (s, p, d, total) within Wigner–Seitz spheres for Li and Si in LiSi."
    }
  ],
  "notes": "Outputs are compared against hidden reference values from the source paper with appropriate tolerances. The checker also recomputes the intercalation voltage from total_energies.json to ensure self-consistency."
}
```

## How you are scored
A hidden verifier independently scores each of your submitted artifacts. It compares your reported values to reference values using tolerances that account for legitimate differences between DFT implementations and pseudopotentials. The verifier also performs internal consistency checks (for example, recomputing the intercalation voltage from your total energies to confirm self-consistency). The final reward is a weighted combination of the scores across all scored artifacts; reporting the paper's numbers alone is not sufficient—you must execute the DFT calculations and produce the required outputs.
