# Multilevel Elasto-Damage Modeling of Porous Bioceramics

## Problem background
Porous bioceramics are used as bone substitutes. Their mechanical performance—stiffness, strength, and damage evolution—depends critically on the internal pore structure: large pores and interconnecting channels. Predicting these properties directly from the microstructure requires a computational framework that links the explicit pore geometry to macroscopic behavior. This task implements a multilevel numerical approach for a two‑phase composite consisting of a ceramic matrix filled with cortical bone, aiming to compute the effective elastic stiffness, ultimate deformation, and damage accumulation for given porous microstructures.

## Approach
The work adopts a multiscale modeling strategy. First, two‑dimensional random geometric models of the porous biocomposite are created: circular inclusions represent pores and channels, with prescribed diameters and total porosity. Then, for each geometry, a set of local finite‑element meso‑volumes is built around randomly sampled points, using linear elastic material properties for the ceramic matrix and the bone filler obtained from the cited literature. Uniaxial tensile loading is applied, and local effective elastic moduli are computed. Damage is introduced through a per‑element criterion; as loading increases, damaged elements are tracked. A percolation‑based clustering rule identifies the formation of a spanning, connected damage cluster, which defines macroscopic fracture. The workflow yields for each structure type the macroscopic effective elastic modulus (GPa), the ultimate strain (%) at fracture, and for the channel‑bearing structure the fractions of damaged volume in bone and matrix. The two structure types are compared to isolate the influence of interconnecting channels: Type 1 contains only large pores (porosity 32%), while Type 2 contains both large pores and smaller connecting channels (total porosity 40%).

## Reproduction target
Produce a single JSON file `results.json` that contains six numeric fields computed from the multilevel simulation pipeline described in the Workflow steps:

- For the pores‑only structure (Type 1): `type1_effective_modulus_GPa` (GPa) and `type1_ultimate_strain_percent` (%).
- For the pores+channels structure (Type 2): `type2_effective_modulus_GPa` (GPa), `type2_ultimate_strain_percent` (%), `type2_damage_bone_fraction` (fraction, 0‑1), and `type2_damage_matrix_fraction` (fraction, 0‑1).

The values must be derived by running the full pipeline: generating random geometries, constructing meso‑models, solving finite‑element problems with progressive loading, and applying the percolation‑based fracture criterion. The results should reflect the physical effects of the different pore structures; no further dataset or external download is needed beyond the elastic constants cited in the Assets.

## Assets

- Barinov 2010 – mechanical properties of zirconia ceramics
- Matveeva et al. 1997 – mechanical properties of cortical bone
- Open-source finite element library (e.g., FEniCS, deal.II): https://fenicsproject.org/

## Workflow steps

### Step 1: Generate 2D geometric representative volume models
- Role: process
- Action: Generate two 2D geometric representative volume models of porous biocomposite: Type 1 (pores only, porosity 32%) and Type 2 (pores + channels, total porosity 40%, channel ratio k=1/5). Domain side length 50× pore diameter (200 µm). Randomly place circular inclusions.
- Evidence: `/app/outputs/geometry_models.json`

### Step 2: Construct meso‑level finite element models
- Role: process
- Action: For each geometry, sample a representative set of random points and for each point build a finite element meso‑model of the local neighbourhood with boundary conditions for uniaxial tensile loading. Include material properties (ceramic matrix and cortical bone) from Barinov 2010 and Matveeva et al. 1997.
- Evidence: `/app/outputs/mesomodels_config.json`

### Step 3: Solve FE problems and track damage accumulation
- Role: process
- Action: Solve linear elasticity finite element problems for each meso‑model under progressive loading to obtain local effective elastic moduli and per‑element damage states. Apply damage initiation criteria and a percolation‑based clustering rule to detect formation of a spanning connective damage cluster (macroscopic fracture).
- Evidence: `/app/outputs/simulation_log.json`

### Step 4: Compute headline quantities and write results.json
- Role: scored (load-bearing)
- Action: From the FEM results, compute the macroscopic effective elastic modulus (GPa) for each structure type (as the average of local effective moduli), the ultimate strain (εu, %) when a spanning damage cluster forms, and for Type 2, the fraction of damaged volume in bone tissue and ceramic matrix at the point of macroscopic fracture. Write results.json with the six fields.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: { type1_effective_modulus_GPa: float, type1_ultimate_strain_percent: float, type2_effective_modulus_GPa: float, type2_ultimate_strain_percent: float, type2_damage_bone_fraction: float, type2_damage_matrix_fraction: float }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed effective elastic properties, ultimate strains, and damage fractions at failure for the two porous structure types. The checker compares each value to the paper's reference with prescribed tolerances and validates the relative ordering of moduli.
- schema:
  - `type`: object
  - `required`:
    - `type1_effective_modulus_GPa`: number (GPa)
    - `type1_ultimate_strain_percent`: number (%)
    - `type2_effective_modulus_GPa`: number (GPa)
    - `type2_ultimate_strain_percent`: number (%)
    - `type2_damage_bone_fraction`: number (fraction 0-1)
    - `type2_damage_matrix_fraction`: number (fraction 0-1)

Notes: The solving agent must implement the full multiscale FEM pipeline, not merely interpolate reported numbers. The geometric randomness introduces run‑to‑run spread; tolerances accommodate legitimate re‑implementation variation while distinguishing a genuine solution from a guess.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "type1_effective_modulus_GPa": "number (GPa)",
          "type1_ultimate_strain_percent": "number (%)",
          "type2_effective_modulus_GPa": "number (GPa)",
          "type2_ultimate_strain_percent": "number (%)",
          "type2_damage_bone_fraction": "number (fraction 0-1)",
          "type2_damage_matrix_fraction": "number (fraction 0-1)"
        }
      },
      "description": "Computed effective elastic properties, ultimate strains, and damage fractions at failure for the two porous structure types. The checker compares each value to the paper's reference with prescribed tolerances and validates the relative ordering of moduli."
    }
  ],
  "notes": "The solving agent must implement the full multiscale FEM pipeline, not merely interpolate reported numbers. The geometric randomness introduces run‑to‑run spread; tolerances accommodate legitimate re‑implementation variation while distinguishing a genuine solution from a guess."
}
```

## How you are scored
An automated hidden verifier reads your `results.json`, extracts the six numeric scalars, and compares them against reference values obtained from the original computational study. The verifier also checks a required structural relationship between the effective moduli of the two structure types to ensure the physical trend is captured. Each of the six fields carries equal weight. Tolerances are set to accommodate legitimate run‑to‑run variability caused by different implementations, meshing, and random seeds, while still distinguishing a genuine multi‑scale simulation from a guess. The verifier runs offline; you are not shown the reference values or tolerances. Only the final scored file `results.json` is evaluated; intermediate evidence files are auditable but not scored.
