# Calculation of Lattice Energies and Densities for α- and β-SrNCN Polymorphs

## Problem background
Strontium cyanamide (SrNCN) exists in two polymorphs, α and β, obtained under different temperature conditions. Establishing their thermochemical stability ordering and density is important for solid-state chemistry and materials design. Experimental ranking is challenging, so first-principles calculations are used to compute lattice energies and densities, answering which phase is more stable and which is denser.

## Approach
Periodic density functional theory (DFT) calculations will be performed on the crystal structures of both polymorphs obtained from public crystallographic databases. Geometry optimizations relax the unit cell parameters and atomic positions, after which the total energy is computed. The lattice energy per formula unit is derived by dividing the total energy by the number of formula units per cell, and the density is obtained from the relaxed unit cell volume and the formula mass. The procedure is implemented using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO). The calculations adopt standard solid-state settings (exchange-correlation functional, pseudopotentials, k-point sampling, and energy cutoffs) appropriate to the system. The resulting energies and densities are then compared to rank the polymorphs.

## Reproduction target
Use an open-source periodic DFT code to compute total energies and densities for α- and β-SrNCN. For each polymorph, report the total energy per formula unit in eV and Ry, the density in g/cm³, unit cell volume, and the formula units per cell. Determine which polymorph is thermochemically more stable (i.e., has the lower total energy per formula unit) and which is denser. Output the results in the two JSON files `/app/outputs/densities.json` and `/app/outputs/lattice_energies.json` exactly as described in the workflow steps.

## Assets

- Crystal structures of α- and β-SrNCN: CCDC deposition numbers from the original publication (e.g., CCDC 763561, 763562); also retrievable via ICSD.
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare crystal structure input files
- Role: process
- Action: Retrieve the published crystal structures of α- and β-SrNCN from a public crystallographic database (CSD/ICSD) using the provided accession numbers. Convert them to input files suitable for periodic DFT (e.g., PWscf input).
- Evidence: none

### Step 2: DFT geometry optimization and total energy calculation
- Role: process
- Action: For each polymorph, perform a periodic DFT geometry relaxation and a subsequent total energy calculation using an open-source code (Quantum ESPRESSO). Retain the optimized structure and the final total energy.
- Evidence: `/app/outputs/dft_output_logs`

### Step 3: Compute and report densities
- Role: scored
- Action: From the relaxed unit cell volumes and formula units per cell, compute the density of each polymorph in g/cm³. Output a JSON file with the densities, volumes, and formula-unit counts.
- Output file: `/app/outputs/densities.json`
- Format: json
- Contract: {
  "alpha_SrNCN": {
    "density_g_per_cm3": float,
    "unit_cell_volume_A3": float,
    "formula_units_per_cell": int
  },
  "beta_SrNCN": {
    "density_g_per_cm3": float,
    "unit_cell_volume_A3": float,
    "formula_units_per_cell": int
  }
}
- Scoring: scored by hidden verifier

### Step 4: Compute and report lattice energies
- Role: scored (load-bearing)
- Action: Extract the total energy per formula unit (in eV and Ry) for each polymorph from the DFT output, compute the energy difference, and report in lattice_energies.json. Explicitly state which polymorph is more stable.
- Output file: `/app/outputs/lattice_energies.json`
- Format: json
- Contract: {
  "alpha_SrNCN": {
    "total_energy_per_fu_eV": float,
    "total_energy_per_fu_Ry": float
  },
  "beta_SrNCN": {
    "total_energy_per_fu_eV": float,
    "total_energy_per_fu_Ry": float
  },
  "energy_difference_beta_minus_alpha_eV_per_fu": float,
  "more_stable_polymorph": "alpha or beta"
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/densities.json`
- `/app/outputs/lattice_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### densities.json
- path: `/app/outputs/densities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed densities (g/cm³), unit cell volumes (Å³), and formula units per cell from the relaxed DFT structures.
- schema:
  - `type`: object
  - `properties`:
    - `alpha_SrNCN`:
      - `type`: object
      - `properties`:
        - `density_g_per_cm3`:
          - `type`: number
        - `unit_cell_volume_A3`:
          - `type`: number
        - `formula_units_per_cell`:
          - `type`: integer
      - `required`: `density_g_per_cm3`, `unit_cell_volume_A3`, `formula_units_per_cell`
    - `beta_SrNCN`:
      - `type`: object
      - `properties`:
        - `density_g_per_cm3`:
          - `type`: number
        - `unit_cell_volume_A3`:
          - `type`: number
        - `formula_units_per_cell`:
          - `type`: integer
      - `required`: `density_g_per_cm3`, `unit_cell_volume_A3`, `formula_units_per_cell`
  - `required`: `alpha_SrNCN`, `beta_SrNCN`

### lattice_energies.json
- path: `/app/outputs/lattice_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energy per formula unit (eV and Ry) for each polymorph, the energy difference (beta minus alpha), and which polymorph is more stable.
- schema:
  - `type`: object
  - `properties`:
    - `alpha_SrNCN`:
      - `type`: object
      - `properties`:
        - `total_energy_per_fu_eV`:
          - `type`: number
        - `total_energy_per_fu_Ry`:
          - `type`: number
      - `required`: `total_energy_per_fu_eV`, `total_energy_per_fu_Ry`
    - `beta_SrNCN`:
      - `type`: object
      - `properties`:
        - `total_energy_per_fu_eV`:
          - `type`: number
        - `total_energy_per_fu_Ry`:
          - `type`: number
      - `required`: `total_energy_per_fu_eV`, `total_energy_per_fu_Ry`
    - `energy_difference_beta_minus_alpha_eV_per_fu`:
      - `type`: number
    - `more_stable_polymorph`:
      - `type`: string
      - `enum`: `alpha`, `beta`
  - `required`: `alpha_SrNCN`, `beta_SrNCN`, `energy_difference_beta_minus_alpha_eV_per_fu`, `more_stable_polymorph`

Notes: The densities and lattice energies will be compared to hidden paper-reported values within appropriate tolerances. The primary check for lattice energies is that the correct polymorph is identified as more stable (lower energy).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "densities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "alpha_SrNCN": {
            "type": "object",
            "properties": {
              "density_g_per_cm3": {
                "type": "number"
              },
              "unit_cell_volume_A3": {
                "type": "number"
              },
              "formula_units_per_cell": {
                "type": "integer"
              }
            },
            "required": [
              "density_g_per_cm3",
              "unit_cell_volume_A3",
              "formula_units_per_cell"
            ]
          },
          "beta_SrNCN": {
            "type": "object",
            "properties": {
              "density_g_per_cm3": {
                "type": "number"
              },
              "unit_cell_volume_A3": {
                "type": "number"
              },
              "formula_units_per_cell": {
                "type": "integer"
              }
            },
            "required": [
              "density_g_per_cm3",
              "unit_cell_volume_A3",
              "formula_units_per_cell"
            ]
          }
        },
        "required": [
          "alpha_SrNCN",
          "beta_SrNCN"
        ]
      },
      "description": "Computed densities (g/cm³), unit cell volumes (Å³), and formula units per cell from the relaxed DFT structures."
    },
    {
      "file": "lattice_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "alpha_SrNCN": {
            "type": "object",
            "properties": {
              "total_energy_per_fu_eV": {
                "type": "number"
              },
              "total_energy_per_fu_Ry": {
                "type": "number"
              }
            },
            "required": [
              "total_energy_per_fu_eV",
              "total_energy_per_fu_Ry"
            ]
          },
          "beta_SrNCN": {
            "type": "object",
            "properties": {
              "total_energy_per_fu_eV": {
                "type": "number"
              },
              "total_energy_per_fu_Ry": {
                "type": "number"
              }
            },
            "required": [
              "total_energy_per_fu_eV",
              "total_energy_per_fu_Ry"
            ]
          },
          "energy_difference_beta_minus_alpha_eV_per_fu": {
            "type": "number"
          },
          "more_stable_polymorph": {
            "type": "string",
            "enum": [
              "alpha",
              "beta"
            ]
          }
        },
        "required": [
          "alpha_SrNCN",
          "beta_SrNCN",
          "energy_difference_beta_minus_alpha_eV_per_fu",
          "more_stable_polymorph"
        ]
      },
      "description": "Total energy per formula unit (eV and Ry) for each polymorph, the energy difference (beta minus alpha), and which polymorph is more stable."
    }
  ],
  "notes": "The densities and lattice energies will be compared to hidden paper-reported values within appropriate tolerances. The primary check for lattice energies is that the correct polymorph is identified as more stable (lower energy)."
}
```

## How you are scored
A hidden automated verifier will examine your two output JSON files. It compares your reported densities and volumes against reference values with a generous tolerance. For the lattice energies, the primary check is that the computed energies correctly identify β-SrNCN as more stable (lower energy per formula unit); the sign of the energy difference (beta minus alpha) must be negative. In addition, the verifier will compare your absolute energies and the energy difference to hidden reference numbers with a tolerance that accounts for differences in DFT settings. Finally, the field `more_stable_polymorph` must match the expected result. Each scored artifact is weighted, and the combined reward (0–1) is written to `/logs/verifier/reward.txt`.
