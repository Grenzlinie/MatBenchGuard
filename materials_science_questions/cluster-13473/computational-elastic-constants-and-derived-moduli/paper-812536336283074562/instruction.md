# Penta-graphene Elastic Constants and Fracture Strain Reproduction

## Problem background
Penta-graphene is a two-dimensional carbon allotrope composed of non-coplanar pentagons in a Cairo-tiling lattice. Its unique structure gives rise to unusual mechanical properties and the ability to sustain large tensile strain before fracture. Accurately determining its elastic constants (Young's modulus and Poisson's ratio) from first-principles calculations and its failure strain under uniaxial tension from reactive molecular dynamics is important for understanding its mechanical limits and guiding potential applications. This task computes these key mechanical benchmarks for penta-graphene using density functional theory (DFT) and reactive molecular dynamics (MD).

## Approach
DFT calculations using a generalized gradient approximation (GGA-PBE) functional are performed on the penta-graphene unit cell. The elastic constants C11 and C12 are obtained by fitting the strain-energy per area under uniaxial and equi-biaxial small-strain series. From these, the in-plane Young's modulus and Poisson's ratio are derived using standard formulas for a two-dimensional membrane. Reactive MD simulations employ the ReaxFF force field with the Mueller parameter set. A periodic supercell is first equilibrated at 300 K, then subjected to uniaxial tensile deformation at a constant engineering strain rate. The resulting engineering stress–strain data is recorded until complete fracture. The failure strain is identified from this curve as the strain at which the stress first drops below 10% of the peak stress. Both the DFT-derived mechanical constants and the MD stress–strain curve are saved as structured artifacts for verification.

## Reproduction target
Compute the Young's modulus (in GPa·nm) and Poisson's ratio (dimensionless) of penta-graphene using DFT (GGA-PBE). Compute the uniaxial tensile failure strain (in %) using reactive MD with the Mueller ReaxFF parameter set at 300 K and a strain rate of 10⁻⁶ fs⁻¹. Save the DFT results in `/app/outputs/dft_elastic_constants.json` and the full engineering stress–strain curve in `/app/outputs/md_stress_strain.csv`.

## Assets

- LAMMPS molecular dynamics package: https://www.lammps.org/download.html
- ReaxFF parameter file (Mueller set): https://www.lammps.org/potentials/ffield.reax.CHONO-2019
- DFT code (Quantum ESPRESSO or equivalent GGA-PBE implementation): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Generate penta-graphene atomic models
- Role: process
- Action: Create the penta-graphene unit cell (square lattice a=3.64 Å, 6 carbon atoms in Cairo-tiling) for DFT. Also build a periodic supercell (approx. 80×80 Å) for MD. Save coordinates in standard formats.
- Evidence: `/app/outputs/structure_gen.log`

### Step 2: DFT elastic constants calculation
- Role: scored
- Action: Perform DFT total-energy calculations on the unit cell under uniaxial and equi-biaxial strain series (small strains). Fit strain-energy per area to obtain elastic constants C11 and C12. Compute Young's modulus Y = (C11^2 - C12^2)/C11 and Poisson's ratio ν = C12/C11. Save results to dft_elastic_constants.json.
- Output file: `/app/outputs/dft_elastic_constants.json`
- Format: json
- Contract: {"youngs_modulus_GPa_nm": float, "poissons_ratio": float}
- Scoring: scored by hidden verifier

### Step 3: ReaxFF MD fracture simulation
- Role: scored (load-bearing)
- Action: Equilibrate the supercell at 300 K (NPT), then apply uniaxial tensile deformation at a constant engineering strain rate of 1e-6 fs⁻¹ (NVT) using the Mueller ReaxFF set. Record engineering strain and engineering stress at every timestep up to complete fracture. Write the stress-strain data to md_stress_strain.csv.
- Output file: `/app/outputs/md_stress_strain.csv`
- Format: csv
- Contract: CSV with columns: strain (dimensionless), stress (GPa·nm)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_elastic_constants.json`
- `/app/outputs/md_stress_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_elastic_constants.json
- path: `/app/outputs/dft_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT computed Young's modulus (in GPa·nm) and Poisson's ratio (dimensionless). Both quantities must be present and the Poisson's ratio must be negative. The checker compares them to the paper's DFT reference values.
- schema:
  - `type`: object
  - `required`:
    - `youngs_modulus_GPa_nm`: float
    - `poissons_ratio`: float

### md_stress_strain.csv
- path: `/app/outputs/md_stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Engineering stress-strain curve from ReaxFF tensile simulation. The checker recomputes the engineering failure strain from this data and compares it to the paper's MD failure strain (20%) within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa·nm

Notes: The unit cell coordinates are provided in the instruction.md. The agent may use any GGA-PBE DFT code. The Mueller ReaxFF parameter file is a public resource listed above. No other outputs are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "youngs_modulus_GPa_nm": "float",
          "poissons_ratio": "float"
        }
      },
      "description": "DFT computed Young's modulus (in GPa·nm) and Poisson's ratio (dimensionless). Both quantities must be present and the Poisson's ratio must be negative. The checker compares them to the paper's DFT reference values."
    },
    {
      "file": "md_stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa·nm"
        }
      },
      "description": "Engineering stress-strain curve from ReaxFF tensile simulation. The checker recomputes the engineering failure strain from this data and compares it to the paper's MD failure strain (20%) within tolerance."
    }
  ],
  "notes": "The unit cell coordinates are provided in the instruction.md. The agent may use any GGA-PBE DFT code. The Mueller ReaxFF parameter file is a public resource listed above. No other outputs are required."
}
```

## How you are scored
A hidden verifier independently scores each required output. It reads `/app/outputs/dft_elastic_constants.json` and compares the reported Young's modulus and Poisson's ratio to reference values within pre-set tolerances. It reads `/app/outputs/md_stress_strain.csv`, recomputes the engineering failure strain as the strain at which the stress drops below 10% of the peak stress, and compares that value to a reference. The final reward is a weighted combination of the stage scores; reporting the paper's numbers without genuine computation will not yield credit because the tolerances are designed to reward only workflows that faithfully execute the described methodology.
