# Computational Mechanical Properties of Amorphous Cellulose via Reactive Molecular Dynamics

## Problem background
Amorphous cellulose constitutes the disordered regions of wood microfibrils and strongly influences flexibility and plasticity in cellulosic materials. Predicting its mechanical response is important for designing cellulose‑based composites. Experimental characterization is time‑intensive, so molecular dynamics (MD) simulations are used to compute elastic constants and stress‑strain behavior at the atomic level. This task uses the ReaxFF reactive force field, which can model bond breaking and formation, to estimate the equilibrium density, Young’s modulus, shear modulus, and Poisson’s ratio of an amorphous cellulose model.

## Approach
Build a periodic amorphous cellulose simulation cell containing many glucose chains. The system is relaxed via energy minimization, then equilibrated at room temperature and atmospheric pressure using isothermal‑isobaric (NPT) MD with the ReaxFF force field. The equilibrated configuration is subsequently subjected to uniaxial tensile deformation at a constant strain rate, while stress and strain are recorded. From the resulting stress‑strain curve, the linear‑elastic response is analyzed to extract the Young’s modulus, Poisson’s ratio, and shear modulus. The equilibrium density is obtained from the final frame of the NPT equilibration. The computed properties are compared with previously reported experimental and simulation benchmarks to assess the model’s realism.

## Reproduction target
Compute the equilibrium density and the three elastic constants (Young’s modulus, shear modulus, Poisson’s ratio) of an amorphous cellulose model at 298 K and atmospheric pressure, following the model‑building, equilibration, and deformation workflow described below. Write the four scalar values into a JSON file. The hidden verifier will compare your submitted values against reference data for amorphous cellulose (derived from published experiments and simulations) to evaluate how accurately the simulation reproduces the target material behavior.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- ReaxFF force field parameters for cellulose / C-H-O: https://www.engr.psu.edu/adri/
- Packmol (optional): https://m3g.github.io/packmol/
- Cellulose chain molecular structure (glucose/cellobiose)

## Workflow steps

### Step 1: Generate initial amorphous cellulose structure
- Role: process
- Action: Build a periodic amorphous cellulose simulation cell containing 27 chains of 50-glucose-unit cellulose (using cellobiose as the building block) at an initial density of ~0.8 g/cm³. Use a chain packing protocol (e.g., Amorphous Cell method, Packmol, or a custom script) and replicate the unit cell to a 3×3×3 supercell to obtain a system of approximately 28,404 atoms (C:8100, H:13554, O:6750).
- Evidence: `/app/outputs/init_structure.data`

### Step 2: Energy minimization
- Role: process
- Action: Perform energy minimization on the initial structure using the ReaxFF force field to relax high-energy contacts.
- Evidence: `/app/outputs/minimized.lammpstrj`

### Step 3: NPT equilibration at 298 K and atmospheric pressure
- Role: process
- Action: Run an NPT (isothermal-isobaric) MD simulation with timestep 0.5 fs for 250 ps at T=298 K and P=0.0001 GPa using the ReaxFF force field, to achieve equilibrium density and remove internal stresses.
- Evidence: `/app/outputs/equilibrated.lammpstrj`

### Step 4: Uniaxial tensile deformation
- Role: process
- Action: From the equilibrated structure, apply a constant strain rate (e.g., 10^10 s⁻¹) uniaxial tensile strain in the x-direction while maintaining zero pressure in y and z. Run the simulation at 298 K until sufficient strain to capture elastic and yielding regimes, recording stress in all three directions.
- Evidence: `/app/outputs/deformation.lammpstrj`

### Step 5: Extract mechanical properties
- Role: scored (load-bearing)
- Action: From the stress–strain data obtained in the deformation step, extract the equilibrium density, Young's modulus (initial linear slope of stress–strain in loading direction), Poisson's ratio (negative ratio of lateral to axial strain in elastic region), and shear modulus (computed from Young's modulus and Poisson's ratio using isotropic relation). Write the four scalar values into a JSON file.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: {"density": "float (g/cm^3)", "youngs_modulus": "float (GPa)", "shear_modulus": "float (GPa)", "poissons_ratio": "float (dimensionless)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed mechanical properties of amorphous cellulose: density, Young's modulus, shear modulus, and Poisson's ratio.
- schema:
  - `type`: object
  - `required`: `density`, `youngs_modulus`, `shear_modulus`, `poissons_ratio`
  - `properties`:
    - `density`:
      - `type`: number
      - `unit`: g/cm^3
    - `youngs_modulus`:
      - `type`: number
      - `unit`: GPa
    - `shear_modulus`:
      - `type`: number
      - `unit`: GPa
    - `poissons_ratio`:
      - `type`: number
      - `unit`: dimensionless

Notes: The values in the JSON are compared against hidden reference values (the paper's reported results) using tolerances appropriate for DFT/MD re-runs. Scoring is based on agreement with these references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "density",
          "youngs_modulus",
          "shear_modulus",
          "poissons_ratio"
        ],
        "properties": {
          "density": {
            "type": "number",
            "unit": "g/cm^3"
          },
          "youngs_modulus": {
            "type": "number",
            "unit": "GPa"
          },
          "shear_modulus": {
            "type": "number",
            "unit": "GPa"
          },
          "poissons_ratio": {
            "type": "number",
            "unit": "dimensionless"
          }
        }
      },
      "description": "Computed mechanical properties of amorphous cellulose: density, Young's modulus, shear modulus, and Poisson's ratio."
    }
  ],
  "notes": "The values in the JSON are compared against hidden reference values (the paper's reported results) using tolerances appropriate for DFT/MD re-runs. Scoring is based on agreement with these references."
}
```

## How you are scored
Your submission is scored by a hidden verifier. The verifier reads `mechanical_properties.json` and compares each of the four properties—density, Young’s modulus, shear modulus, and Poisson’s ratio—against hidden reference values. Each property that falls within the verifier’s predetermined tolerance earns a quarter of the total reward; the overall score is the sum of these quarter‑point checks, ranging from 0 to 1. The tolerances account for the normal variability of a re‑run with a different implementation environment, so a faithful reproduction of the described workflow will yield a high score even if the numbers are not identical to any single published dataset.
