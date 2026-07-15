# ZnO nanostructures elastic properties simulation with Buckingham potential

## Problem background
ZnO nanowires and nanotubes are promising building blocks for nanodevices. Understanding how their elastic properties change with size is critical for applications. This work computes the Young's moduli of ZnO nanowires and nanotubes using classical molecular dynamics. The interaction between atoms is described by an empirical Buckingham-type potential together with corrected Ewald summation for long-range Coulomb forces. The goal is to examine how the Young's modulus depends on the radius of nanowires and the wall thickness of nanotubes, and to compare them with the bulk ZnO value.

## Approach
The interatomic forces are modeled using a Buckingham potential with parameters from Kulkarni et al. 2005. Long-range electrostatic interactions are handled via the corrected Ewald summation method. First, bulk wurtzite ZnO is simulated to obtain equilibrium lattice constants and to compute the surface energies of relaxed nonpolar (10-10) and (11-20) slabs. The axial Young’s modulus of bulk ZnO along [0001] is then determined by applying a series of axial strains and fitting the total energy versus strain curve, as well as from the virial stress. Using the equilibrium lattice parameters, hexagonal cross-section nanowires and nanotubes with specified radii and wall thicknesses are constructed. For each nanostructure, atomic positions and the axial lattice parameter are relaxed, after which a series of axial strains is again applied. Young’s modulus is extracted from both the energy-strain fit and the virial stress. Optionally, the Young’s modulus can be decomposed into contributions from individual atomic layers to study surface stiffening effects.

## Reproduction target
Compute and output the following quantitative results:
- Bulk ZnO: lattice constant a, c/a ratio, internal parameter u, surface energies of (10-10) and (11-20), and the axial Young’s modulus from both energy and virial methods (stored in bulk_ZnO_properties.csv).
- Nanowires NW-1, NW-3, NW-5: for each, report the radius and the Young’s modulus from both the energy and virial methods (NW_young_moduli.csv).
- Nanotubes NT-A-1, NT-A-3, NT-B-1, NT-B-4: for each, report the type, outer radius, inner radius, wall thickness, and Young’s modulus from both methods (NT_young_moduli.csv).
The results should reveal whether the Young’s modulus varies systematically with nanowire radius and with nanotube wall thickness, and how the nanostructure moduli compare to bulk ZnO.

## Assets

- Kulkarni et al. 2005 ZnO Buckingham potential parameters: https://doi.org/10.1088/0957-4484/16/12/001

## Workflow steps

### Step 1: Compute Bulk ZnO Properties
- Role: scored (load-bearing)
- Action: Build wurtzite ZnO unit cell using the Buckingham potential and corrected Ewald summation. Relax lattice parameters (a, c, u) to equilibrium. Compute relaxed surface energies of (10-10) and (11-20) slabs. Apply axial strains from -2.5% to 2.5% in 0.5% steps along [0001] and calculate bulk Young's modulus via the energy-strain curve fitting method and the virial stress method. Record all properties.
- Output file: `/app/outputs/bulk_ZnO_properties.csv`
- Format: csv
- Contract: Columns: Property (string), Value (float), Units (string), Method (string). Rows: lattice constant a (Å), c/a ratio, internal parameter u, surface energy (10-10) (J/m^2), surface energy (11-20) (J/m^2), Young's modulus energy (GPa), Young's modulus virial (GPa).
- Scoring: scored by hidden verifier

### Step 2: Generate Nanowire and Nanotube Structures
- Role: process
- Action: Using the equilibrium lattice parameters from step1, construct hexagonal cross-section wurtzite ZnO nanowires NW-1, NW-3, NW-5 (radii approx. 8.707, 28.297, 47.887 Å) and nanotubes NT-A-1, NT-A-3, NT-B-1, NT-B-4 (dimensions as per the paper's structural tables) with periodic supercells along [0001].
- Evidence: `/app/outputs/structure_details.txt`

### Step 3: Compute Young's Moduli for ZnO Nanowires
- Role: scored (load-bearing)
- Action: For each nanowire (NW-1, NW-3, NW-5), relax atomic positions and axial lattice constant to equilibrium. Then apply axial strains from -2.5% to 2.5% in 0.5% steps, compute total energy and virial stress at each strain, and derive Young's modulus from both the energy-strain curve fitting and the virial stress method. Record results.
- Output file: `/app/outputs/NW_young_moduli.csv`
- Format: csv
- Contract: Columns: Structure (string), Radius (float, Å), Young_modulus_energy (float, GPa), Young_modulus_virial (float, GPa).
- Scoring: scored by hidden verifier

### Step 4: Compute Young's Moduli for ZnO Nanotubes
- Role: scored (load-bearing)
- Action: For each nanotube (NT-A-1, NT-A-3, NT-B-1, NT-B-4), relax atomic positions and axial lattice constant to equilibrium. Apply axial strains and compute Young's modulus using both energy and virial methods. Record results.
- Output file: `/app/outputs/NT_young_moduli.csv`
- Format: csv
- Contract: Columns: Structure (string), Type (string), Outer_radius (float, Å), Inner_radius (float, Å), Wall_thickness (float, Å), Young_modulus_energy (float, GPa), Young_modulus_virial (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_ZnO_properties.csv`
- `/app/outputs/NW_young_moduli.csv`
- `/app/outputs/NT_young_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_ZnO_properties.csv
- path: `/app/outputs/bulk_ZnO_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Bulk ZnO validation properties: lattice constant a, c/a ratio, internal parameter u, surface energies of (10-10) and (11-20), and axial Young's modulus from energy and virial methods.
- schema:
  - `type`: table
  - `required_columns`: `Property`, `Value`, `Units`, `Method`
  - `units`:
    - `Value`: varies (Å for a, dimensionless for c/a and u, J/m^2 for surface energies, GPa for Young's modulus)

### NW_young_moduli.csv
- path: `/app/outputs/NW_young_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Young's modulus of ZnO nanowires NW-1, NW-3, NW-5 computed by energy-strain and virial stress methods.
- schema:
  - `type`: table
  - `required_columns`: `Structure`, `Radius`, `Young_modulus_energy`, `Young_modulus_virial`
  - `units`:
    - `Radius`: Å
    - `Young_modulus_energy`: GPa
    - `Young_modulus_virial`: GPa

### NT_young_moduli.csv
- path: `/app/outputs/NT_young_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Young's modulus of ZnO nanotubes NT-A-1, NT-A-3, NT-B-1, NT-B-4 computed by energy-strain and virial stress methods.
- schema:
  - `type`: table
  - `required_columns`: `Structure`, `Type`, `Outer_radius`, `Inner_radius`, `Wall_thickness`, `Young_modulus_energy`, `Young_modulus_virial`
  - `units`:
    - `Outer_radius`: Å
    - `Inner_radius`: Å
    - `Wall_thickness`: Å
    - `Young_modulus_energy`: GPa
    - `Young_modulus_virial`: GPa

Notes: Per-layer Young's moduli (for NW-1 and NT-A-1) are optional and not scored. The checker verifies numeric values and monotonic trends (NW modulus decreases with increasing radius, NT modulus decreases with increasing wall thickness).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_ZnO_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Property",
          "Value",
          "Units",
          "Method"
        ],
        "units": {
          "Value": "varies (Å for a, dimensionless for c/a and u, J/m^2 for surface energies, GPa for Young's modulus)"
        }
      },
      "description": "Bulk ZnO validation properties: lattice constant a, c/a ratio, internal parameter u, surface energies of (10-10) and (11-20), and axial Young's modulus from energy and virial methods."
    },
    {
      "file": "NW_young_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Structure",
          "Radius",
          "Young_modulus_energy",
          "Young_modulus_virial"
        ],
        "units": {
          "Radius": "Å",
          "Young_modulus_energy": "GPa",
          "Young_modulus_virial": "GPa"
        }
      },
      "description": "Young's modulus of ZnO nanowires NW-1, NW-3, NW-5 computed by energy-strain and virial stress methods."
    },
    {
      "file": "NT_young_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Structure",
          "Type",
          "Outer_radius",
          "Inner_radius",
          "Wall_thickness",
          "Young_modulus_energy",
          "Young_modulus_virial"
        ],
        "units": {
          "Outer_radius": "Å",
          "Inner_radius": "Å",
          "Wall_thickness": "Å",
          "Young_modulus_energy": "GPa",
          "Young_modulus_virial": "GPa"
        }
      },
      "description": "Young's modulus of ZnO nanotubes NT-A-1, NT-A-3, NT-B-1, NT-B-4 computed by energy-strain and virial stress methods."
    }
  ],
  "notes": "Per-layer Young's moduli (for NW-1 and NT-A-1) are optional and not scored. The checker verifies numeric values and monotonic trends (NW modulus decreases with increasing radius, NT modulus decreases with increasing wall thickness)."
}
```

## How you are scored
A hidden verifier program reads your three output CSV files and compares each numerical value against reference values (the hidden gold) with appropriate tolerances. It also checks that any size-dependent trends (e.g., change of Young’s modulus with nanowire radius or nanotube wall thickness) are correctly captured. The overall reward is a weighted combination of the scores for the three artifacts. Simply reporting the paper’s numbers is not enough; the verifier expects values consistent with a correct implementation of the simulation protocol.
