# Multi-Scale Modeling of Elastic Properties of Nanoparticle/Polymer Composites

## Problem background
Nanoparticle-reinforced polyimide composites are candidates for lightweight structural materials. Their bulk elastic stiffness depends on nanoscale features, particularly the molecular structure and density of the polymer region adjacent to the nanoparticle surface. Capturing how interfacial treatments and particle size influence the overall mechanical response, and whether a continuum model with an effective interface can bridge molecular simulations and macroscopic predictions, is a challenging multiscale problem. The work develops a quantitative pipeline that combines molecular modeling and continuum micromechanics to investigate this size- and interface-dependent behaviour of silica nanoparticle/polyimide composites.

## Approach
A multiscale computational procedure is employed. First, atomistic representative volume elements are prepared via a coarse-grained linked-vector model of the BPDA/APB polyimide, Monte Carlo equilibration with a hard-sphere nanoparticle, and reverse mapping to atomistic detail. Constant-pressure NPT molecular dynamics (300 K, 1 atm, 200 ps) using the CVFF force field provides equilibrated configurations for pure silica, pure polyimide, and four composite variants that differ by nanoparticle surface treatment: untreated, hydroxylated, phenoxybenzene, and covalently functionalized. From each equilibrated RVE, elastic stiffness constants C11 and C12 are computed via the static-deformation energy-difference approach; isotropic Young's modulus E and shear modulus G are then derived. Next, two micromechanics models are applied. The classical Mori–Tanaka two-phase model (spherical inclusions, Eshelby tensor) uses the pure phase properties and an effective particle volume fraction of 1.7 % to produce a baseline prediction. An effective-interface three-phase model introduces a spherical interface of fixed thickness (12 Å) between the particle and the matrix; its elastic properties are solved for by requiring the model to reproduce the MD composite moduli, given the geometry (particle inner radius 6 Å, interface outer radius 18 Å, volume fractions 1.7 % particle / 45.2 % interface / 53.1 % matrix) and an assumed interface Poisson's ratio of 0.4. Finally, using the extracted interface properties and the pure phase constants, the composite E and G are predicted for both models across a wide range of effective particle radii (10–10,000 Å) at a fixed particle volume fraction of 5 %. This yields radius-dependent curves that reveal how the interface influence decays with particle size.

## Reproduction target
Produce the following quantitative results through the full computational pipeline described in the Workflow steps:

- MD-derived Young's modulus (E) and shear modulus (G) for the six material systems: silica, polyimide, silica_composite, hydroxylated_composite, phenoxybenzene_composite, functionalized_composite.
- Mori–Tanaka two-phase micromechanics predictions (E_MT, G_MT) at the RVE volume fraction (1.7 %) for the four composite types, using the pure phase E and G from MD.
- Effective interface Young's modulus (E_interface) and shear modulus (G_interface) for each of the four composites, obtained by solving the effective-interface model with the geometry and volume fractions stated above and the MD and Mori–Tanaka results.
- Radius-dependent composite moduli (E, G) for both the effective-interface and Mori–Tanaka models at a particle volume fraction of 5 %, for at least 10 logarithmically spaced radii between 10 Å and 10,000 Å. Include all four composite types and distinguish the model type with a column.

All moduli are reported in GPa; radii in Å. The expected outputs are the CSV files listed under "Output files" with the exact column schemas described in each step. The elastic constants must be physically admissible (E > 0, G > 0) and the effective-interface predictions should exhibit monotonic behaviour with radius and approach the Mori–Tanaka predictions as the radius increases.

## Assets

- LAMMPS (open-source MD engine): https://lammps.sandia.gov
- CVFF force field parameters: ffcvff2.cff (from LAMMPS distribution or Discover force field library)
- Python with NumPy/SciPy: numpy scipy

## Workflow steps

### Step 1: Atomistic RVE preparation via coarse-grained modeling and MD equilibration
- Role: process
- Action: Construct coarse-grained linked-vector model of BPDA/APB polyimide chains; perform Monte Carlo equilibration with a hard-sphere nanoparticle (diameter ∼15 Å) in a cubic simulation box (∼42 Å side); reverse-map to atomistic detail; apply energy minimization; run constant-pressure NPT MD at 300 K and 1 atm for 200 ps using LAMMPS with the CVFF force field to obtain equilibrated atomistic configurations for pure silica, pure polyimide, and the four composite variants (untreated, hydroxylated, phenoxybenzene, functionalized).
- Evidence: `/app/outputs/md_equilibration.log`

### Step 2: Compute elastic constants from MD
- Role: scored
- Action: For each of the six equilibrated systems, apply small static deformations and energy minimizations according to the static-deformation energy-difference approach. Use the resulting energy differences to calculate the isotropic elastic stiffness components C11 and C12, then derive Young's modulus (E) and shear modulus (G). Write the results to a CSV file.
- Output file: `/app/outputs/elastic_constants_systems.csv`
- Format: csv
- Contract: columns: system (string: 'silica','polyimide','silica_composite','hydroxylated_composite','phenoxybenzene_composite','functionalized_composite'), E (float, GPa), G (float, GPa). One row per system.
- Scoring: scored by hidden verifier

### Step 3: Mori–Tanaka predictions at RVE volume fraction
- Role: scored
- Action: Using the pure silica and polyimide elastic constants from Step 2, apply the Mori–Tanaka two-phase model with an effective particle volume fraction of 1.7% and the Eshelby tensor for spherical inclusions to predict composite Young's and shear moduli for the four composite systems. Save the results to a CSV.
- Output file: `/app/outputs/mori_tanaka_rve.csv`
- Format: csv
- Contract: columns: composite (string: 'silica_composite','hydroxylated_composite','phenoxybenzene_composite','functionalized_composite'), E_MT (float, GPa), G_MT (float, GPa). Four rows.
- Scoring: scored by hidden verifier

### Step 4: Determine effective interface elastic properties
- Role: scored
- Action: For each composite, take the MD composite elastic constants (Step 2) together with the pure silica and polyimide constants. Using the effective interface geometry (inner radius 6 Å, outer radius 18 Å, thickness 12 Å, corresponding volume fractions: particle 1.7%, interface 45.2%, matrix 53.1%) and an assumed interface Poisson's ratio of 0.4, solve the effective-interface micromechanics equations to extract the isotropic interface Young's modulus (E_i) and shear modulus (G_i). Write the interface properties to a CSV.
- Output file: `/app/outputs/effective_interface_properties.csv`
- Format: csv
- Contract: columns: composite_type (string: 'silica_composite','hydroxylated_composite','phenoxybenzene_composite','functionalized_composite'), E_interface (float, GPa), G_interface (float, GPa). Four rows.
- Scoring: scored by hidden verifier

### Step 5: Radius-dependent composite moduli (effective-interface and Mori–Tanaka)
- Role: scored (load-bearing)
- Action: For each composite type, compute the composite Young's modulus (E) and shear modulus (G) at a particle volume fraction of 5% for a set of effective particle radii (logarithmically spaced from 10 Å to 10,000 Å, at least 10 points). Use the effective-interface model with interface thickness 12 Å and the interface properties from Step 4; also compute the constant Mori–Tanaka predictions at each radius using the pure phase constants from Step 2. Combine both sets into one file, distinguishing them with a model_type column. Save as CSV.
- Output file: `/app/outputs/moduli_vs_radius.csv`
- Format: csv
- Contract: columns: composite_type (string: 'silica_composite','hydroxylated_composite','phenoxybenzene_composite','functionalized_composite'), radius_A (float, angstrom), model_type (string: 'Mori-Tanaka' or 'Effective-Interface'), E (float, GPa), G (float, GPa). At least 10 radius values per composite.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants_systems.csv`
- `/app/outputs/mori_tanaka_rve.csv`
- `/app/outputs/effective_interface_properties.csv`
- `/app/outputs/moduli_vs_radius.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants_systems.csv
- path: `/app/outputs/elastic_constants_systems.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: MD-derived Young's (E) and shear (G) moduli for the six material systems.
- schema:
  - `type`: table
  - `required_columns`: `system`, `E`, `G`
  - `units`:
    - `E`: GPa
    - `G`: GPa

### mori_tanaka_rve.csv
- path: `/app/outputs/mori_tanaka_rve.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mori–Tanaka predicted composite moduli at the RVE volume fraction.
- schema:
  - `type`: table
  - `required_columns`: `composite`, `E_MT`, `G_MT`
  - `units`:
    - `E_MT`: GPa
    - `G_MT`: GPa

### effective_interface_properties.csv
- path: `/app/outputs/effective_interface_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective interface Young's and shear moduli for each composite.
- schema:
  - `type`: table
  - `required_columns`: `composite_type`, `E_interface`, `G_interface`
  - `units`:
    - `E_interface`: GPa
    - `G_interface`: GPa

### moduli_vs_radius.csv
- path: `/app/outputs/moduli_vs_radius.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Radius-dependent composite moduli from both effective-interface and Mori–Tanaka models; checker recomputes effective-interface curves for consistency.
- schema:
  - `type`: table
  - `required_columns`: `composite_type`, `radius_A`, `model_type`, `E`, `G`
  - `units`:
    - `radius_A`: Å
    - `E`: GPa
    - `G`: GPa

Notes: All moduli are in GPa. Radii in Å. The effective-interface model curves will be recomputed from the submitted interface properties and pure phase constants; internal consistency (within 1%) is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants_systems.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "E",
          "G"
        ],
        "units": {
          "E": "GPa",
          "G": "GPa"
        }
      },
      "description": "MD-derived Young's (E) and shear (G) moduli for the six material systems."
    },
    {
      "file": "mori_tanaka_rve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composite",
          "E_MT",
          "G_MT"
        ],
        "units": {
          "E_MT": "GPa",
          "G_MT": "GPa"
        }
      },
      "description": "Mori–Tanaka predicted composite moduli at the RVE volume fraction."
    },
    {
      "file": "effective_interface_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composite_type",
          "E_interface",
          "G_interface"
        ],
        "units": {
          "E_interface": "GPa",
          "G_interface": "GPa"
        }
      },
      "description": "Effective interface Young's and shear moduli for each composite."
    },
    {
      "file": "moduli_vs_radius.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composite_type",
          "radius_A",
          "model_type",
          "E",
          "G"
        ],
        "units": {
          "radius_A": "Å",
          "E": "GPa",
          "G": "GPa"
        }
      },
      "description": "Radius-dependent composite moduli from both effective-interface and Mori–Tanaka models; checker recomputes effective-interface curves for consistency."
    }
  ],
  "notes": "All moduli are in GPa. Radii in Å. The effective-interface model curves will be recomputed from the submitted interface properties and pure phase constants; internal consistency (within 1%) is required."
}
```

## How you are scored
A hidden verifier independently examines each scored output file. It checks that the reported numerical values are consistent with the physics of the problem and with the internal relationships among the different models. Specifically, the verifier will verify that all moduli are positive, that the relative ordering among the different composite surface treatments follows a physically expected pattern, that the effective-interface moduli increase monotonically with increasing particle radius, and that they asymptotically approach the Mori–Tanaka baseline at large radii. The verifier also recomputes the effective-interface radius-dependent curves from the interface properties and pure phase constants you report, requiring internal consistency. Each scored artifact contributes a predefined weight to the overall reward (a single float between 0 and 1). Simply writing down values that match the paper's published numbers is not sufficient; the workflow must be executed genuinely to produce the required artifacts.
