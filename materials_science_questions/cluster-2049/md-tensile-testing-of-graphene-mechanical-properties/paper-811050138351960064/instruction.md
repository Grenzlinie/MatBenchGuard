# MD and DFT investigation of Stone-Thrower-Wales defect effects on graphene-polymer interfacial properties

## Problem background
Stone-Thrower-Wales (STW) defects in graphene are topological defects formed by a 90° rotation of a C–C bond, converting four hexagons into two pentagons and two heptagons. These defects degrade the in-plane mechanical properties of graphene but can also alter the local surface geometry and electronic structure, potentially enhancing interfacial adhesion with polymer matrices. This work investigates the role of STW defects in polypropylene (PP)–graphene nanocomposites, examining their effect on mechanical properties and interfacial load transfer. The open computational task is to quantify adsorption energies, stress–strain responses, and surface roughness as a function of STW defect density using first-principles and molecular dynamics simulations.

## Approach
The reproduction uses a two-level computational approach. First, density functional theory (DFT) with a van der Waals correction is applied to periodic supercells of pristine and STW-defective graphene to compute the adsorption energy of a propylene monomer on specific sites (Hole for pristine, Bridge-3 for defective). The plane-wave DFT calculations are performed with an open-source code such as Quantum ESPRESSO, using the projector augmented wave method and the DFT-D2 dispersion correction. Second, molecular dynamics (MD) simulations with LAMMPS model transversely isotropic nanocomposite unit cells: an amorphous PP matrix (64 chains, 20 monomers each) and single-layer graphene sheets containing 0, 5, and 10 STW defects. Interactions are described by the PCFF force field for the polymer and by the AIREBO reactive potential for graphene. After NPT equilibration at 200 K and 1 atm, uniaxial tension of freestanding graphene in the armchair direction and longitudinal shear of the nanocomposites are performed at a constant true strain rate. The mean arithmetic surface roughness of the embedded graphene sheets is calculated from the equilibrated structures.

## Reproduction target
The objective is to produce the following quantitative results:
1. Adsorption energy (eV) of propylene monomer on pristine graphene (Hole site) and on STW-defective graphene (Bridge-3 site) computed with DFT-D2.
2. Stress–strain curves of freestanding single-layer graphene (0, 5, and 10 STW defects) under uniaxial tension in the armchair direction, reporting true strain and virial stress (GPa) up to 15% strain.
3. Stress–strain curves of the nanocomposite unit cells under longitudinal shear (xz and yz), averaged over three independent runs per defect density, reporting shear strain and shear stress (MPa).
4. Mean arithmetic surface roughness (Å) and maximum out-of-plane displacement (Å) of the graphene sheets in the equilibrated composites for each defect density.
All artifacts must be saved in the /app/outputs directory with the specified formats and column schemas.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LAMMPS: https://www.lammps.org/
- PCFF force field: pair_style pcff (included in LAMMPS)
- AIREBO potential: pair_style airebo (included in LAMMPS)

## Workflow steps

### Step 1: Build DFT supercells and relax structures
- Role: process
- Action: Generate periodic supercells of pristine graphene and STW‑defective graphene (32 carbon atoms, 20 Å vacuum). Build and optimize a propylene monomer. Relax all structures using DFT with a van der Waals functional.
- Evidence: `/app/outputs/dft_relaxation.log`

### Step 2: Compute DFT adsorption energies
- Role: scored
- Action: Place the propylene monomer above the Hole site of pristine graphene and above the Bridge 3 site of STW‑defective graphene. Calculate the adsorption energy using the same DFT‑vdW setup.
- Output file: `/app/outputs/dft_adsorption_energies.json`
- Format: json
- Contract: type=object; required={'pristine_graphene': 'float (eV)', 'stw_graphene': 'float (eV)'}
- Scoring: scored by hidden verifier

### Step 3: Construct MD nanocomposite unit cells
- Role: process
- Action: Build an amorphous polypropylene matrix (64 chains of 20 monomers each) and graphene sheets containing 0, 5, and 10 STW defects. Assemble transversely isotropic unit cells with graphene embedded in PP. Assign PCFF and AIREBO force fields.
- Evidence: `/app/outputs/md_model_construction.log`

### Step 4: Equilibrate systems via NPT MD
- Role: process
- Action: Equilibrate each nanocomposite unit cell and corresponding freestanding graphene unit cell at 200 K and 1 atm for 3 ns in the NPT ensemble using LAMMPS.
- Evidence: `/app/outputs/md_equilibration.log`

### Step 5: Tensile test of freestanding graphene
- Role: scored (load-bearing)
- Action: Perform uniaxial tension on the freestanding graphene sheets (0, 5, 10 defects) in the armchair direction at a constant true strain rate of 0.0002 /ps up to 15% strain. Record strain and corresponding virial stress.
- Output file: `/app/outputs/graphene_tensile_stress_strain.csv`
- Format: csv
- Contract: type=table; required_columns=['strain', 'stress_0defects', 'stress_5defects', 'stress_10defects']; units={'strain': 'dimensionless (true strain)', 'stress_0defects': 'GPa', 'stress_5defects': 'GPa', 'stress_10defects': 'GPa'}
- Scoring: scored by hidden verifier

### Step 6: Longitudinal shear test of nanocomposites
- Role: scored (load-bearing)
- Action: Apply a longitudinal shear deformation (xz and yz) to the equilibrated nanocomposite unit cells at 200 K with a strain rate of 0.0002 /ps. Average three independent runs per defect density. Output shear strain and averaged shear stress.
- Output file: `/app/outputs/composite_longitudinal_shear.csv`
- Format: csv
- Contract: type=table; required_columns=['shear_strain', 'stress_0defects', 'stress_5defects', 'stress_10defects']; units={'shear_strain': 'dimensionless (true shear strain)', 'stress_0defects': 'MPa', 'stress_5defects': 'MPa', 'stress_10defects': 'MPa'}
- Scoring: scored by hidden verifier

### Step 7: Analyze surface roughness
- Role: scored
- Action: From the equilibrated nanocomposite configurations, compute the mean arithmetic surface roughness and maximum out‑of‑plane displacement for each graphene sheet.
- Output file: `/app/outputs/surface_roughness.csv`
- Format: csv
- Contract: type=table; required_columns=['defect_count', 'roughness_angstrom', 'max_displacement_angstrom']; units={'defect_count': 'integer', 'roughness_angstrom': 'ångström', 'max_displacement_angstrom': 'ångström'}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_adsorption_energies.json`
- `/app/outputs/graphene_tensile_stress_strain.csv`
- `/app/outputs/composite_longitudinal_shear.csv`
- `/app/outputs/surface_roughness.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_adsorption_energies.json
- path: `/app/outputs/dft_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adsorption energy of propylene monomer on pristine graphene (Hole site) and on STW‑defective graphene (Bridge 3 site) computed with DFT‑vdW. Compare to paper‑reported values.
- schema:
  - `type`: object
  - `required`:
    - `pristine_graphene`: float (eV)
    - `stw_graphene`: float (eV)

### graphene_tensile_stress_strain.csv
- path: `/app/outputs/graphene_tensile_stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress‑strain curves of single‑layer graphene under uniaxial tension in the armchair direction. Verify that stress decreases with defect density and that modulus and strength magnitudes are within an acceptable range.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_0defects`, `stress_5defects`, `stress_10defects`
  - `units`:
    - `strain`: dimensionless (true strain)
    - `stress_0defects`: GPa
    - `stress_5defects`: GPa
    - `stress_10defects`: GPa

### composite_longitudinal_shear.csv
- path: `/app/outputs/composite_longitudinal_shear.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress‑strain curves of nanocomposites under longitudinal shear. Verify increasing shear stress with defect density and approximate magnitudes.
- schema:
  - `type`: table
  - `required_columns`: `shear_strain`, `stress_0defects`, `stress_5defects`, `stress_10defects`
  - `units`:
    - `shear_strain`: dimensionless (true shear strain)
    - `stress_0defects`: MPa
    - `stress_5defects`: MPa
    - `stress_10defects`: MPa

### surface_roughness.csv
- path: `/app/outputs/surface_roughness.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean arithmetic surface roughness and maximum out‑of‑plane displacement of graphene sheets. Compare with paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `defect_count`, `roughness_angstrom`, `max_displacement_angstrom`
  - `units`:
    - `defect_count`: integer
    - `roughness_angstrom`: ångström
    - `max_displacement_angstrom`: ångström

Notes: The verification uses absolute tolerances for adsorption energies and roughness, and structural trend/magnitude checks for stress-strain curves. The load-bearing steps require actual execution of the MD equilibration and deformation simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine_graphene": "float (eV)",
          "stw_graphene": "float (eV)"
        }
      },
      "description": "Adsorption energy of propylene monomer on pristine graphene (Hole site) and on STW‑defective graphene (Bridge 3 site) computed with DFT‑vdW. Compare to paper‑reported values."
    },
    {
      "file": "graphene_tensile_stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_0defects",
          "stress_5defects",
          "stress_10defects"
        ],
        "units": {
          "strain": "dimensionless (true strain)",
          "stress_0defects": "GPa",
          "stress_5defects": "GPa",
          "stress_10defects": "GPa"
        }
      },
      "description": "Stress‑strain curves of single‑layer graphene under uniaxial tension in the armchair direction. Verify that stress decreases with defect density and that modulus and strength magnitudes are within an acceptable range."
    },
    {
      "file": "composite_longitudinal_shear.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "shear_strain",
          "stress_0defects",
          "stress_5defects",
          "stress_10defects"
        ],
        "units": {
          "shear_strain": "dimensionless (true shear strain)",
          "stress_0defects": "MPa",
          "stress_5defects": "MPa",
          "stress_10defects": "MPa"
        }
      },
      "description": "Stress‑strain curves of nanocomposites under longitudinal shear. Verify increasing shear stress with defect density and approximate magnitudes."
    },
    {
      "file": "surface_roughness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_count",
          "roughness_angstrom",
          "max_displacement_angstrom"
        ],
        "units": {
          "defect_count": "integer",
          "roughness_angstrom": "ångström",
          "max_displacement_angstrom": "ångström"
        }
      },
      "description": "Mean arithmetic surface roughness and maximum out‑of‑plane displacement of graphene sheets. Compare with paper‑reported values."
    }
  ],
  "notes": "The verification uses absolute tolerances for adsorption energies and roughness, and structural trend/magnitude checks for stress-strain curves. The load-bearing steps require actual execution of the MD equilibration and deformation simulations."
}
```

## How you are scored
A hidden verifier will independently score each of the four output artifacts. 
- The DFT adsorption energies are compared to expected reference values using an absolute tolerance.
- The graphene tensile stress–strain curves are checked for the correct structural trend (stress decreases with increasing defect density) and for approximate magnitudes.
- The nanocomposite longitudinal shear curves are checked for the correct trend (shear stress increases with defect density) and approximate magnitudes.
- The surface roughness values are compared to expected reference values within a tolerance.
The verifier combines the scores from all stages into a single reward in the range [0, 1]. Reproducing the exact numerical values is not required; the evaluation rewards correct physical trends and agreement within method-dependent uncertainties.
