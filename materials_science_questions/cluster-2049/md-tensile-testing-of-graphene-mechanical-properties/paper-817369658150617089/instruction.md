# MD simulation of shear modulus and failure of multi-layer graphene

## Problem background
Graphene, a single atomic layer of carbon arranged in a honeycomb lattice, exhibits exceptional mechanical properties such as high stiffness and strength. Understanding the shear behavior of multi-layer graphene is important for applications in nanocomposites and nanoelectromechanical systems. Molecular dynamics (MD) simulations can probe the shear modulus, ultimate stress, and failure strain under different loading conditions, and reveal how these properties depend on the number of layers and the edge chirality (zigzag versus armchair). However, a comprehensive characterization of these shear properties for AB‑stacked multi‑layer graphene sheets across a range of layer numbers is still needed. This task reproduces such MD simulations to compute these mechanical quantities.

## Approach
The method uses classical MD with the Tersoff potential to describe covalent carbon–carbon bonding within each graphene layer and the Lennard‑Jones potential to model the non‑bonded van der Waals interactions between layers. Simulations start from atomistic models of zigzag and armchair graphene sheets with AB stacking, built for layer numbers N = 1, 2, 3, 4, 5, 8. Each monolayer measures 10 nm × 10 nm and contains 3984 carbon atoms; the interlayer spacing is 0.335 nm. After energy minimization and NPT equilibration at 300 K, shear deformation is applied under NVT conditions at a constant strain rate until failure. The resulting shear stress–strain curves are analyzed to extract the elastic shear modulus (from the initial linear region), the ultimate stress (the peak stress), and the failure strain (the strain at the ultimate stress). These properties are obtained for both chiralities and all layer numbers.

## Reproduction target
Produce a CSV file, `results.csv`, containing the computed shear modulus, ultimate stress, and failure strain for each combination of orientation (zigzag, armchair) and number of layers (1, 2, 3, 4, 5, 8). The file must have columns: `orientation` (string), `layers` (integer), `shear_modulus_GPa` (float), `ultimate_stress_GPa` (float), `failure_strain` (float). Properties should be extracted consistently from the simulated stress–strain data: the shear modulus is the slope of the linear elastic region (strain range 0.020–0.045) using least‑square regression; the ultimate stress is the maximum stress on the curve; the failure strain is the strain at which the maximum stress occurs. The results for all twelve configurations (2 chiralities × 6 layer numbers) together form the scored artifact.

## Assets

- LAMMPS: https://lammps.sandia.gov

## Workflow steps

### Step 1: Build multi-layer graphene models
- Role: process
- Action: Construct atomic models of zigzag and armchair graphene sheets with AB stacking for layer numbers N=1,2,3,4,5,8. Each monolayer measures 10 nm × 10 nm and contains 3984 carbon atoms; interlayer distance is 0.335 nm. Generate LAMMPS data files for each configuration.
- Evidence: none

### Step 2: Run MD shear deformation simulations
- Role: process
- Action: For each model, perform energy minimization (conjugate gradient), then NPT equilibration at 300 K for 50 ps (Nosé–Hoover thermostat), followed by NVT shear deformation at a constant strain rate of 1×10⁹ s⁻¹ until failure. Use LAMMPS with Tersoff potential for intralayer bonding and Lennard-Jones potential (ε=0.00284 eV, σ=3.35 Å) for interlayer interactions. Apply periodic boundary conditions and a time step of 1.0 fs.
- Evidence: none

### Step 3: Extract mechanical properties
- Role: scored (load-bearing)
- Action: From the simulation outputs, compute shear stress (F/A) and shear strain (tan θ) to obtain stress–strain curves. Calculate shear modulus as the slope of the linear elastic region over the strain range 0.020–0.045 using least‑square regression. Determine ultimate stress as the maximum stress and failure strain as the strain at ultimate stress. Output these properties for every layer number and chirality.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: orientation (string: zigzag or armchair), layers (integer), shear_modulus_GPa (float), ultimate_stress_GPa (float), failure_strain (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Shear mechanical properties (shear modulus, ultimate stress, failure strain) for zigzag and armchair multi-layer graphene sheets with 1 to 8 layers, extracted from the MD simulations.
- schema:
  - `type`: table
  - `required_columns`: `orientation`, `layers`, `shear_modulus_GPa`, `ultimate_stress_GPa`, `failure_strain`

Notes: The graded comparison uses hidden reference values derived from the paper's reported results and trends; tolerances are set to absorb legitimate toolchain spread while verifying the main claims (modulus in 200–480 GPa, divergence for >5 layers, decreasing ultimate stress and failure strain with layer number).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "orientation",
          "layers",
          "shear_modulus_GPa",
          "ultimate_stress_GPa",
          "failure_strain"
        ]
      },
      "description": "Shear mechanical properties (shear modulus, ultimate stress, failure strain) for zigzag and armchair multi-layer graphene sheets with 1 to 8 layers, extracted from the MD simulations."
    }
  ],
  "notes": "The graded comparison uses hidden reference values derived from the paper's reported results and trends; tolerances are set to absorb legitimate toolchain spread while verifying the main claims (modulus in 200–480 GPa, divergence for >5 layers, decreasing ultimate stress and failure strain with layer number)."
}
```

## How you are scored
A hidden verifier independently judges your submitted `results.csv` against reference values and expected physical trends derived from the literature. It checks that the mechanical properties are physically reasonable and consistent with known behavior of multi‑layer graphene. The verifier evaluates the completeness and correctness of the table, and calculates a reward by combining the outcome of this scored artifact. Simply reporting numbers without genuine simulations will not yield a high score; the checkers are designed to recognize physically inconsistent data. The final reward is a float between 0 and 1, reflecting how well your reproduction matches the hidden criteria.
