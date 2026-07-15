# Amorphous Polymer Elastic Moduli from NPT Molecular Dynamics

## Problem background
Molecular reinforcement is the concept of using stiff, linear molecules dispersed in a flexible polymer matrix to significantly increase mechanical stiffness, in analogy to macroscopic fiber reinforcement.  A key challenge is that rigid and flexible chains are often immiscible, making experimental validation difficult.  In this work, force-field-based molecular dynamics is used to compute the elastic stiffness tensor of amorphous polyarylate directly from cell-parameter fluctuations, providing a way to evaluate whether a rigid rod-like molecule can produce a directional stiffening effect.  The system studied consists of polyarylate as the flexible matrix and poly(p-phenylene) as the reinforcing rod, placed along a chosen direction.

## Approach
The procedure uses classical molecular dynamics in the isothermal-isobaric (NPT) ensemble.  An amorphous periodic cell of polyarylate chains is built at the experimental density.  After equilibration, a production NPT run records the time series of the cell vectors.  The strain fluctuation tensor <ε_i ε_j> is computed from the cell-parameter variations, and the isothermal elastic stiffness tensor c_ij^T is obtained via the fluctuation relation:

c = (k_B T / <V>) <ε ε>^{-1}.

Standard continuum formulas then yield isotropic moduli (tensile modulus E, shear modulus G, bulk modulus B, Poisson ratio ν, Lamé constants).  

To assess molecular reinforcement, a second amorphous cell is constructed that contains a single poly(p-phenylene) rod of length 100 Å aligned along the z‑axis, embedded in the same polyarylate matrix.  The same equilibration and production MD protocol is applied.  The stiffness tensor from this cell is computed identically, and directional moduli (longitudinal E33, transverse E11, shear G44) are extracted.  The Dreiding II force field, whose parameters are published, must be implemented within LAMMPS for all simulations.

## Reproduction target
Build an amorphous periodic cell of polyarylate chains (target density ~1.18 g/cm³) using the Dreiding II force field in LAMMPS.  Equilibrate the cell, then perform an NPT molecular dynamics production run at 300 K and 1 atm.  From the recorded cell-parameter fluctuations, compute the isothermal elastic stiffness tensor c_ij^T with the fluctuation formula and derive the isotropic moduli (E, G, B, ν, λ, μ).

Next, construct a second amorphous cell that includes a single poly(p-phenylene) rod of length 100 Å aligned along the z‑axis.  Keep the same matrix chemistry, density, and force field.  Repeat the equilibration and NPT production MD.  From this trajectory compute the stiffness tensor and extract the longitudinal tensile modulus E33, the transverse tensile modulus E11, and the associated shear modulus G44.

Report the pure matrix properties in step_01_pure_matrix_properties.json and the reinforced properties in step_02_reinforced_properties.json, both following the exact schemas given in the workflow steps.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/downloads.html
- Dreiding II force field parameters: 10.1063/1.460063

## Workflow steps

### Step 1: Prepare and equilibrate pure polyarylate amorphous cell
- Role: process
- Action: Build an amorphous periodic cell of polyarylate chains (chemical structure per the paper) at a target density of ~1.18 g/cm³ using the Dreiding II force field. Perform equilibration (energy minimization, short NVT/NPT runs) to relax the structure.
- Evidence: `/app/outputs/pure_matrix_equilibration.log`

### Step 2: NPT MD simulation of pure polyarylate
- Role: process
- Action: Run NPT molecular dynamics on the equilibrated cell at 300 K and 1 atm with Dreiding II, sampling cell-parameter fluctuations and energies. Save trajectory with cell dimensions.
- Evidence: `/app/outputs/pure_matrix_md.log`

### Step 3: Compute pure matrix elastic stiffness tensor and moduli
- Role: scored (load-bearing)
- Action: From the pure polyarylate MD trajectory, extract the cell-parameter fluctuation matrix ⟨ε_i ε_j⟩, compute the isothermal elastic stiffness tensor c_ij^T using c = (k_B T / V) ⟨ε ε⟩^{-1}, and derive isotropic moduli (E, G, B, ν, λ, μ). Write the stiffness tensor and all derived moduli to a JSON file.
- Output file: `/app/outputs/step_01_pure_matrix_properties.json`
- Format: json
- Contract: JSON object with keys: 'stiffness_tensor' (6x6 list of floats, in GPa), 'E' (tensile modulus in GPa), 'G' (shear modulus in GPa), 'B' (bulk modulus in GPa), 'nu' (Poisson ratio, dimensionless), 'lambda' (Lamé constant in GPa), 'mu' (shear modulus, same as G, in GPa).
- Scoring: scored by hidden verifier

### Step 4: Prepare and equilibrate reinforced amorphous cell (100 Å poly(p-phenylene) rod)
- Role: process
- Action: Construct a new amorphous periodic cell containing a single poly(p-phenylene) rod of length 100 Å aligned along the z‑axis (rod atoms placed once, then the flexible polyarylate chains are filled around it). Equilibrate using the same Dreiding II force field.
- Evidence: `/app/outputs/reinforced_equilibration.log`

### Step 5: NPT MD simulation of reinforced cell
- Role: process
- Action: Run NPT MD at 300 K and 1 atm on the reinforced cell, recording cell dimensions to capture the reduced fluctuations along the rod direction.
- Evidence: `/app/outputs/reinforced_md.log`

### Step 6: Compute reinforced matrix elastic stiffness tensor and directional moduli
- Role: scored
- Action: From the reinforced cell trajectory, compute the stiffness tensor c_ij^T using the fluctuation formula. Extract the longitudinal tensile modulus E33 (along the rod, z‑direction) and the transverse modulus E11. Write the stiffness tensor and these moduli to a JSON file.
- Output file: `/app/outputs/step_02_reinforced_properties.json`
- Format: json
- Contract: JSON object with keys: 'stiffness_tensor' (6x6 list of floats, in GPa), 'E33' (tensile modulus along rod direction in GPa), 'E11' (transverse tensile modulus in GPa), 'G44' (shear modulus involving rod direction in GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_pure_matrix_properties.json`
- `/app/outputs/step_02_reinforced_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_pure_matrix_properties.json
- path: `/app/outputs/step_01_pure_matrix_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic stiffness tensor and derived mechanical moduli for pure amorphous polyarylate.
- schema:
  - `type`: object
  - `required`:
    - `stiffness_tensor`: 6x6 list of floats, GPa
    - `E`: float, GPa
    - `G`: float, GPa
    - `B`: float, GPa
    - `nu`: float, dimensionless
    - `lambda`: float, GPa
    - `mu`: float, GPa
  - `description`: Isotropic moduli must be derived from the stiffness tensor using standard continuum formulas.

### step_02_reinforced_properties.json
- path: `/app/outputs/step_02_reinforced_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic stiffness tensor and directional moduli for polyarylate reinforced with a 100 Å poly(p‑phenylene) rod.
- schema:
  - `type`: object
  - `required`:
    - `stiffness_tensor`: 6x6 list of floats, GPa
    - `E33`: float, GPa
    - `E11`: float, GPa
    - `G44`: float, GPa
  - `description`: The checker will also verify the structural relation E33 > E11.

Notes: The checker recomputes derived moduli from the submitted stiffness tensor and compares them to paper‑reported reference values with appropriate tolerances. It also verifies tensor symmetry, positive definiteness, and the required trend E33 > E11. The task uses a reference‑match policy; the gold values are the experimentally valid ranges and trends reported in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_pure_matrix_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "stiffness_tensor": "6x6 list of floats, GPa",
          "E": "float, GPa",
          "G": "float, GPa",
          "B": "float, GPa",
          "nu": "float, dimensionless",
          "lambda": "float, GPa",
          "mu": "float, GPa"
        },
        "description": "Isotropic moduli must be derived from the stiffness tensor using standard continuum formulas."
      },
      "description": "Elastic stiffness tensor and derived mechanical moduli for pure amorphous polyarylate."
    },
    {
      "file": "step_02_reinforced_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "stiffness_tensor": "6x6 list of floats, GPa",
          "E33": "float, GPa",
          "E11": "float, GPa",
          "G44": "float, GPa"
        },
        "description": "The checker will also verify the structural relation E33 > E11."
      },
      "description": "Elastic stiffness tensor and directional moduli for polyarylate reinforced with a 100 Å poly(p‑phenylene) rod."
    }
  ],
  "notes": "The checker recomputes derived moduli from the submitted stiffness tensor and compares them to paper‑reported reference values with appropriate tolerances. It also verifies tensor symmetry, positive definiteness, and the required trend E33 > E11. The task uses a reference‑match policy; the gold values are the experimentally valid ranges and trends reported in the paper."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently inspects each output file.  The reward is a weighted combination of the results from both scored stages.

For the pure matrix, the verifier recomputes isotropic moduli from the stiffness tensor you provide, checks that the stiffness tensor is approximately symmetric and positive definite, and compares the derived moduli to the known physical ranges for this material (the exact tolerances are hidden).  A correct submission must yield moduli that fall within the expected bounds.

For the reinforced system, the verifier again checks tensor symmetry and verifies the structural relation E33 > E11 (the longitudinal modulus must be significantly larger than the transverse modulus).  It also checks that E33 falls within the expected reinforcement range for a 100 Å rod.  

Simply reporting numbers that match published tables is not sufficient; the verifier re-derives key quantities from your raw stiffness tensor and checks both quantitative and structural criteria.
