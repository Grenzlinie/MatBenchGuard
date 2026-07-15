# Lithium-Ion Migration Barrier Computation on Pristine and Iodine-Doped Borophene via NEB

## Problem background
Borophenes, two-dimensional boron sheets, are promising anode materials for lithium-ion batteries owing to their high theoretical capacities. However, the lithium-ion diffusion on several borophene polymorphs, including the χ3 phase, is sluggish, with migration barriers that limit fast-charging applications. Halogen functionalization has been proposed as a strategy to boost lithium-ion mobility by modifying the electronic structure of the borophene surface. This task investigates whether iodine doping affects the lithium-ion migration barriers on χ3 borophene by re-running density functional theory (DFT) and nudged-elastic-band (NEB) calculations to compute the relevant energy landscapes.

## Approach
The reproduction uses first-principles DFT with the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional and a van der Waals correction (DFT-D2). The χ3 borophene is modelled as a 2×3 supercell with a vacuum layer to separate periodic images. After geometry optimization of the pristine borophene, the minimum energy paths for lithium-ion migration are determined using the climbing-image nudged elastic band (NEB) method along two high-symmetry directions (vertical and horizontal). Iodine is then adsorbed at the most favourable site (top of a boron atom at a hexagon corner) and the geometry is re-optimized. Lithium is placed at hollow sites adjacent to the iodine atom, and NEB calculations are performed for migration from one hollow site to two neighbouring hollow sites. The initial-state and transition-state adsorption energies are recorded for each path.

## Reproduction target
Compute the initial-state (IS) and transition-state (TS) adsorption energies for lithium-ion migration on pristine χ3 borophene (vertical path and horizontal path) and on iodine-doped χ3 borophene (paths H1→H7 and H1→H2). Collect all eight energies in a single JSON file (`results.json`). From these values, derive the migration barriers (barrier = TS energy – IS energy). The hidden verifier will compare your computed barriers against reference values for pristine χ3 and evaluate the relative trend between the doped and pristine systems.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, or VASP with NEB module)
- Pseudopotential/PAW datasets for B, Li, I
- χ3 borophene crystal structure parameters

## Workflow steps

### Step 1: Geometry optimization of pristine χ3 borophene
- Role: process
- Action: Construct a 2×3 supercell of χ3 borophene (lattice constants a=8.41 Å, b=2.93 Å, 49 B atoms, hexagon-hole pattern) with a vacuum layer >15 Å. Perform DFT geometry optimization until forces and energy converge. Save the optimized atomic coordinates.
- Evidence: `/app/outputs/pristine_chi3_optimized.xyz`

### Step 2: NEB calculation of Li migration on pristine χ3
- Role: process
- Action: On the optimized pristine supercell, place a Li atom at a hollow center site and compute NEB energy profiles for the vertical (Path I) and horizontal (Path II) migration directions. Record the initial-state (IS) and transition-state (TS) adsorption energies for each path.
- Evidence: none

### Step 3: Iodine adsorption on χ3 borophene
- Role: process
- Action: Place an I atom at the T2 site (top of a B atom at a hexagon corner) on the optimized pristine supercell. Fully relax the atomic positions to obtain the optimized I-χ3 geometry.
- Evidence: `/app/outputs/I_chi3_optimized.xyz`

### Step 4: Lithium adsorption on I-χ3 borophene
- Role: process
- Action: On the optimized I-χ3 supercell, place Li atoms at the H1, H7, and H2 hollow sites (sites close to I) and optimize each configuration to obtain the initial-state (IS) structures and energies for the migration endpoints.
- Evidence: none

### Step 5: NEB for Li migration on I-χ3 and compile final results
- Role: scored (load-bearing)
- Action: Using the optimized I-χ3 supercell and the Li IS structures from step 04, perform NEB calculations for the paths H1→H7 and H1→H2. Record the IS and TS adsorption energies. Combine these with the pristine IS/TS energies obtained in step 02 and write a single JSON file containing all eight values (in eV).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"pristine_pathI_IS_ads": float (eV), "pristine_pathI_TS_ads": float, "pristine_pathII_IS_ads": float, "pristine_pathII_TS_ads": float, "I_H1_H7_IS_ads": float, "I_H1_H7_TS_ads": float, "I_H1_H2_IS_ads": float, "I_H1_H2_TS_ads": float, "units": "eV"}
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
- target_policy: metric_recompute
- description: Initial-state and transition-state adsorption energies for four Li-ion migration paths. The checker recomputes migration barriers (barrier = TS - IS) and evaluates whether the iodine-doped barriers are lower than the pristine barriers and whether the barriers are within physically reasonable bounds.
- schema:
  - `type`: object
  - `required`:
    - `pristine_pathI_IS_ads`: float
    - `pristine_pathI_TS_ads`: float
    - `pristine_pathII_IS_ads`: float
    - `pristine_pathII_TS_ads`: float
    - `I_H1_H7_IS_ads`: float
    - `I_H1_H7_TS_ads`: float
    - `I_H1_H2_IS_ads`: float
    - `I_H1_H2_TS_ads`: float
    - `units`: string
  - `units`:
    - `pristine_pathI_IS_ads`: eV
    - `pristine_pathI_TS_ads`: eV
    - `pristine_pathII_IS_ads`: eV
    - `pristine_pathII_TS_ads`: eV
    - `I_H1_H7_IS_ads`: eV
    - `I_H1_H7_TS_ads`: eV
    - `I_H1_H2_IS_ads`: eV
    - `I_H1_H2_TS_ads`: eV

Notes: Only the I-doped case and pristine reference are reproduced; F, Cl, Br cases and benchmark recalculations omitted.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "pristine_pathI_IS_ads": "float",
          "pristine_pathI_TS_ads": "float",
          "pristine_pathII_IS_ads": "float",
          "pristine_pathII_TS_ads": "float",
          "I_H1_H7_IS_ads": "float",
          "I_H1_H7_TS_ads": "float",
          "I_H1_H2_IS_ads": "float",
          "I_H1_H2_TS_ads": "float",
          "units": "string"
        },
        "units": {
          "pristine_pathI_IS_ads": "eV",
          "pristine_pathI_TS_ads": "eV",
          "pristine_pathII_IS_ads": "eV",
          "pristine_pathII_TS_ads": "eV",
          "I_H1_H7_IS_ads": "eV",
          "I_H1_H7_TS_ads": "eV",
          "I_H1_H2_IS_ads": "eV",
          "I_H1_H2_TS_ads": "eV"
        }
      },
      "description": "Initial-state and transition-state adsorption energies for four Li-ion migration paths. The checker recomputes migration barriers (barrier = TS - IS) and evaluates whether the iodine-doped barriers are lower than the pristine barriers and whether the barriers are within physically reasonable bounds."
    }
  ],
  "notes": "Only the I-doped case and pristine reference are reproduced; F, Cl, Br cases and benchmark recalculations omitted."
}
```

## How you are scored
A hidden verifier reads your `results.json`, recomputes the migration barriers, and compares them to expected values and physical trends. The reward is monotonic: full credit is awarded when all barriers fall within the required tolerances and the predicted trend (how the iodine-doped barriers compare with the pristine barriers) is correctly reproduced. Partial credit is given for near matches. Simply reporting numbers from the literature is not sufficient; your results must come from executing the described DFT+NEB workflow.
