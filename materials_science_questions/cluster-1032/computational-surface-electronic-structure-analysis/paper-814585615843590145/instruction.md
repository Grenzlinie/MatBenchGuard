# Relaxation geometry prediction of CdSe(1010) surface using sp3 tight-binding model

## Problem background
The (10-10) cleavage face of wurtzite-structure II-VI semiconductors is of fundamental interest because of a long-standing controversy about whether a surface state exists near the valence-band maximum. Resolving this question requires a reliable prediction of the surface atomic relaxation, which is a prerequisite for any electronic surface state calculation. This task focuses on predicting the equilibrium atomic geometry of the relaxed CdSe(10-10) surface using an empirical tight-binding model. The goal is to compute, from the physical ingredients of the model, the six independent parameters that fully characterize the surface relaxation of the top two atomic layers.

## Approach
We use an empirical nearest-neighbor sp<sup>3</sup> tight-binding model with Slater–Koster two-center interaction integrals. The bulk total energy is supplemented by an elastic strain energy term, with coefficients derived from the bulk modulus, to penalize large atomic displacements from the ideal bulk positions. The total energy (electronic band energy plus elastic energy) is minimized with respect to the positions of the atoms in the surface region. The influence of bond-length changes on the overlap integrals is taken into account by a d<sup>−2</sup> scaling law. The model is applied to a slab geometry that represents the CdSe(10-10) surface, using the experimental bulk lattice constants. From the relaxed geometry we extract the six independent structural parameters that define the bond-rotation relaxation: the perpendicular and in-plane displacements of the top-layer Se relative to Cd, the interlayer spacings between the first and second layers, the perpendicular displacement of the second layer, and the bond-rotation angle.

## Reproduction target
Compute the six structural parameters that describe the relaxed surface geometry and write them to a JSON file with the following keys (all values are floats):
- `delta1_perp` (Å): perpendicular displacement of top-layer Se relative to Cd,
- `delta1_y` (Å): in-plane displacement of top-layer Se relative to Cd,
- `d12_y` (Å): in-plane distance between first and second layers,
- `d12_perp` (Å): perpendicular distance between first and second layers,
- `delta2_perp` (Å): perpendicular displacement of the second layer,
- `omega1` (degrees): bond-rotation angle.
All parameters must be derived from the fully relaxed atomic positions obtained by energy minimization.

## Assets
No external datasets, code libraries, or trained models are required beyond a standard numerical computing environment (e.g., Python with numpy/scipy). All necessary physical parameters are listed below; no additional downloads are needed.
- Lattice constants: a_x = 4.30 Å, a_y = 7.02 Å
- Tight-binding on-site energies (eV): Se 4s = -10.960, Cd 5s = 1.360, Se 4p = 1.640, Cd 5p = 4.560
- Slater–Koster interaction integrals (eV): V_ssσ = -0.659, V_spσ(Se→Cd) = 0.342, V_spσ(Cd→Se) = 2.814, V_ppσ = 3.361, V_ppπ = -0.655
- Elastic parameters: U₁ = -14.953 eV/atom, U₂ = 66.872 eV/atom (derived from bulk modulus B = 5.50×10¹¹ dyn/cm²)
- Bond-length scaling: all interaction integrals scale as d⁻² with bond length.

## Workflow steps

### Step 1: Surface relaxation simulation
- Role: process
- Action: Implement a nearest-neighbor sp3 tight-binding model for CdSe with on-site and Slater-Koster interaction parameters as specified. Construct a slab model of the wurtzite CdSe(10-10) cleavage face using lattice constants a_x=4.30 Å and a_y=7.02 Å. Apply the d^{-2} scaling law to interaction integrals with bond length. Perform energy minimization of the total energy (electronic energy from tight-binding plus elastic strain energy with parameters U1=−14.953 eV/atom and U2=66.872 eV/atom, the latter derived from bulk modulus B=5.50×10^11 dyn/cm²) to find the relaxed atomic positions of the top two layers. Save the final relaxed geometry as a text file 'relaxed_geometry.xyz'.
- Evidence: `/app/outputs/relaxed_geometry.xyz`

### Step 2: Extract relaxation structural parameters
- Role: scored (load-bearing)
- Action: From the relaxed surface geometry produced in the previous step, compute the six independent structural parameters that characterize the bond-rotation relaxation: delta1_perp (perpendicular displacement of top-layer Se relative to Cd, in Å), delta1_y (in-plane displacement, in Å), d12_y, d12_perp (interlayer distances, in Å), delta2_perp (second layer perpendicular displacement, in Å), and omega1 (bond-rotation angle, in degrees). Write these values to a JSON file.
- Output file: `/app/outputs/relaxation_parameters.json`
- Format: json
- Contract: JSON object with keys: delta1_perp, delta1_y, d12_y, d12_perp, delta2_perp, omega1 (all floats; distances in Å, angle in degrees).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxation_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxation_parameters.json
- path: `/app/outputs/relaxation_parameters.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Relaxed surface structural parameters: perpendicular/in-plane displacements and bond-rotation angle, as defined in the paper.
- schema:
  - `type`: object
  - `required`:
    - `delta1_perp`: float
    - `delta1_y`: float
    - `d12_y`: float
    - `d12_perp`: float
    - `delta2_perp`: float
    - `omega1`: float
  - `units`:
    - `delta1_perp`: Å
    - `delta1_y`: Å
    - `d12_y`: Å
    - `d12_perp`: Å
    - `delta2_perp`: Å
    - `omega1`: degrees

Notes: The hidden checker compares each parameter to the paper’s theory prediction using relative tolerances. All six must be within tolerance for full credit; partial credit is proportional to the number of passing parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxation_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "delta1_perp": "float",
          "delta1_y": "float",
          "d12_y": "float",
          "d12_perp": "float",
          "delta2_perp": "float",
          "omega1": "float"
        },
        "units": {
          "delta1_perp": "Å",
          "delta1_y": "Å",
          "d12_y": "Å",
          "d12_perp": "Å",
          "delta2_perp": "Å",
          "omega1": "degrees"
        }
      },
      "description": "Relaxed surface structural parameters: perpendicular/in-plane displacements and bond-rotation angle, as defined in the paper."
    }
  ],
  "notes": "The hidden checker compares each parameter to the paper’s theory prediction using relative tolerances. All six must be within tolerance for full credit; partial credit is proportional to the number of passing parameters."
}
```

## How you are scored
Your submission will be scored by a hidden automated verifier. The verifier reads the file `relaxation_parameters.json` and compares each of the six numerical values against a reference that is hidden from you. For each parameter, the verifier checks whether its value falls within a pre-defined relative tolerance. The reward is proportional to the number of parameters that satisfy the tolerance; full credit (reward 1.0) is awarded only when all six parameters pass. Reporting values without actually performing the energy-minimization relaxation will likely not satisfy the tolerances.
