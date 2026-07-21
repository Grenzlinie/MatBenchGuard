# Microscopic profiles of polarization and refractive indices across a 180° domain wall in tetragonal KNbO3

## Problem background
Ferroelectric materials exhibit spontaneous polarization that can be reversed by an external field. Inside a domain wall, the polarization changes gradually between opposite domains, and the microscopic behaviour of polarization and optical properties in this region is of both fundamental and practical interest. This task investigates a 180° ferroelectric domain wall in tetragonal KNbO₃ using a microscopic model that couples electronic polarizabilities (treated with a quantum orbital approximation) and dipole‑dipole interactions. The model predicts unit‑cell resolved profiles of spontaneous polarization and refractive indices across the wall, and how those profiles depend on the domain wall thickness.

## Approach
We treat the crystal as a slab of unit cells containing a 180° domain wall, with the wall plane centred at the Nb–O₂ (100) plane. Each ion carries an effective charge. Its ionic displacement across the wall follows a hyperbolic tangent profile characterised by a thickness parameter rc. The electronic response is described by a field‑dependent polarizability tensor derived from an orbital approximation; the required ionic polarizability parameters, effective charges, lattice constants, and spontaneous ionic shifts at 270 °C are taken from published work and are supplied inline.

The core computational procedure is:
- For each ion pair, compute interatomic vectors and the point‑dipole interaction tensors, including the macroscopic volume term.
- Set up the linear system that relates the local electric field at each ion site to the external field (zero for the spontaneous case) and to the dipole moments of all other ions.
- Solve the system self‑consistently, including the fluctuation term that accounts for variations of the relative ionic dipole moment between different unit cells.
- From the converged local fields, derive the electronic and ionic dipole moments per unit cell, and hence the unit‑cell polarization component parallel to the polar axis (P₃).
- For the optical properties, solve a coupled linear system for the derivatives of the local field with respect to an optical field, construct the optical dielectric tensor, invert it, and obtain the three principal refractive indices as functions of position.

This workflow is repeated for each of four domain wall thicknesses (rc = 5, 10, 15, 20 Å). The final output files contain the position‑resolved P₃ and refractive index profiles for all thicknesses.

## Reproduction target
Produce two CSV files under `/app/outputs`:
1. `step_01_polarization_profile.csv`: unit‑cell resolved spontaneous polarization component P₃ (C/m²) as a function of position x (Å) across the domain wall, for each of the four thicknesses rc ∈ {5, 10, 15, 20} Å.
2. `step_02_refractive_index_profile.csv`: position‑resolved principal refractive indices n₁, n₂, n₃ (dimensionless) for the same four thicknesses.

In both files, x is measured relative to the wall centre (the Nb–O₂ plane), and the profiles must span far enough on either side that the bulk behaviour is clearly captured. The model parameters (lattice constants, ionic polarizabilities, effective charges, spontaneous shifts) are fixed at the values for tetragonal KNbO₃ at 270 °C, as provided in the instruction. No external bias field is applied.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy
- Chaib et al. 1999 - Ionic polarizability parameters for KNbO3: 10.1002/(SICI)1521-3951(199908)214:2<453::AID-PSSB453>3.0.CO;2-7
- Chaib et al. 2000 - Effective charges and lattice parameters for tetragonal KNbO3: 10.1088/0953-8984/12/10/311

## Workflow steps

### Step 1: Construct domain wall geometry
- Role: process
- Action: Build a slab of tetragonal KNbO3 unit cells containing a 180° domain wall with the wall plane centered at the Nb-O2 (100) plane. Use the tetragonal lattice parameters, spontaneous ionic shifts at 270°C from the literature (provided in the task instruction), and the hyperbolic tangent profile for ionic shifts as a function of x-position to define the domain wall. Compute interionic vectors for all ion pairs within a sufficiently large supercell that captures the domain wall profile for each of the four domain wall thicknesses rc = 5, 10, 15, 20 Å.
- Evidence: none

### Step 2: Compute dipole-dipole interaction tensors
- Role: process
- Action: For each of the four domain wall thicknesses, evaluate the point-dipole interaction tensors T_{kk'} including the macroscopic volume term, using the unit cell volume computed from the lattice parameters. Store the tensors for later use in solving the local-field linear system.
- Evidence: none

### Step 3: Self-consistent local field solution
- Role: process
- Action: Solve the linear system for the local electric fields at every ion site across the domain wall for each rc. Use the field-dependent electronic polarizability tensor with the provided ionic polarizability parameters and effective charges. Iterate to self-consistency, including the fluctuation term. No external field is applied for the spontaneous polarization case.
- Evidence: none

### Step 4: Compute spontaneous polarization profile
- Role: scored (load-bearing)
- Action: From the converged local fields and ionic shifts, compute the electronic and ionic dipole moments and derive the unit-cell polarization component P3 as a function of position x across the domain wall. Output the profile as a CSV file containing x (in Å relative to wall center), rc (domain wall thickness), and P3 (spontaneous polarization in C/m²). Include results for all four rc values.
- Output file: `/app/outputs/step_01_polarization_profile.csv`
- Format: csv
- Contract: CSV with columns: x (float, position in Å), rc (float, domain wall thickness in Å, one of 5,10,15,20), P3 (float, spontaneous polarization in C/m²).
- Scoring: scored by hidden verifier

### Step 5: Compute refractive index profiles
- Role: scored
- Action: Using the same converged local fields and polarizabilities, solve the coupled linear systems for the optical field derivatives, compute the optical dielectric tensor and its inverse, and derive the three principal refractive indices n1, n2, n3 as functions of x. Output the profiles as a CSV file with columns: x, rc, n1, n2, n3. Include all four rc values.
- Output file: `/app/outputs/step_02_refractive_index_profile.csv`
- Format: csv
- Contract: CSV with columns: x (float, position in Å), rc (float, domain wall thickness in Å, one of 5,10,15,20), n1 (float), n2 (float), n3 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_polarization_profile.csv`
- `/app/outputs/step_02_refractive_index_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_polarization_profile.csv
- path: `/app/outputs/step_01_polarization_profile.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Unit-cell resolved spontaneous polarization component P3 across the 180° domain wall in tetragonal KNbO3 at 270°C for four domain wall thicknesses. The checker verifies far-field magnitude and profile shape against reference values.
- schema:
  - `type`: table
  - `required_columns`: `x`, `rc`, `P3`
  - `units`:
    - `x`: Å
    - `rc`: Å
    - `P3`: C/m²

### step_02_refractive_index_profile.csv
- path: `/app/outputs/step_02_refractive_index_profile.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Unit-cell resolved principal refractive indices n1, n2, n3 across the 180° domain wall for four domain wall thicknesses. The checker verifies far-field values and profile shape against reference values derived from the literature.
- schema:
  - `type`: table
  - `required_columns`: `x`, `rc`, `n1`, `n2`, `n3`
  - `units`:
    - `x`: Å
    - `rc`: Å
    - `n1`: dimensionless
    - `n2`: dimensionless
    - `n3`: dimensionless

Notes: The profiles should be computed with the domain wall centered at the Nb-O2 (100) plane. The checker verifies far-field magnitude and profile shape against reference values derived from the literature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_polarization_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "rc",
          "P3"
        ],
        "units": {
          "x": "Å",
          "rc": "Å",
          "P3": "C/m²"
        }
      },
      "description": "Unit-cell resolved spontaneous polarization component P3 across the 180° domain wall in tetragonal KNbO3 at 270°C for four domain wall thicknesses. The checker verifies far-field magnitude and profile shape against reference values."
    },
    {
      "file": "step_02_refractive_index_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "rc",
          "n1",
          "n2",
          "n3"
        ],
        "units": {
          "x": "Å",
          "rc": "Å",
          "n1": "dimensionless",
          "n2": "dimensionless",
          "n3": "dimensionless"
        }
      },
      "description": "Unit-cell resolved principal refractive indices n1, n2, n3 across the 180° domain wall for four domain wall thicknesses. The checker verifies far-field values and profile shape against reference values derived from the literature."
    }
  ],
  "notes": "The profiles should be computed with the domain wall centered at the Nb-O2 (100) plane. The checker verifies far-field magnitude and profile shape against reference values derived from the literature."
}
```

## How you are scored
A hidden verifier will read your CSV output files and perform automated checks. It will verify that far from the domain wall the polarization and refractive indices approach consistent bulk magnitudes, that the polarization vanishes at the wall centre, and that the refractive index profiles show the expected symmetry and qualitative shape (e.g., peaks at the centre for some indices, monotonically returning to the bulk away from the wall). It will also check that the changes with wall thickness are physically plausible. The verifier combines these individual checks into an overall score between 0 and 1. Reporting a single number is insufficient; you must produce the full profiles as specified.
