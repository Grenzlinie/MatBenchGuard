# Mean-Square Displacements for NH4Cl and ND4Cl from Lattice Dynamics

## Problem background
Mean-square atomic displacements are a key measure of thermal vibrations in crystals and are essential for interpreting charge-density studies. For ammonium chloride (NH4Cl) and its deuterated analogue (ND4Cl), these displacements can be calculated from a lattice-dynamical model instead of relying on diffraction data that may contain systematic errors. The goal of this task is to compute the total mean-square displacements for all atoms in NH4Cl and ND4Cl across several temperatures, as well as the N-H and N-D bond mean-square amplitudes, by implementing a rigid ion-rigid molecule lattice-dynamical model and adding internal vibration contributions.

## Approach
The approach uses a rigid ion-rigid molecule model of lattice dynamics, where the ammonium group is treated as a rigid unit for external vibrations and its internal vibrations are calculated separately. The dynamical matrix is built from short-range forces, Ewald-summed Coulomb interactions, effective charges, and mass/inertia scaling. Phonon eigenfrequencies and eigenvectors are obtained by diagonalizing the matrix on a mesh of wave vectors. Translational and rotational mean-square displacements for the chlorine ion and the ammonium group are then computed from the eigenmodes, handling the acoustic-mode divergence. Separately, internal vibration contributions for the N, H, and D atoms are obtained from symmetry force constants using the method of Cyvin. The external and internal components are combined using the rigid-body libration formalism to yield the total mean-square displacements for each atom at the specified temperatures, along with the N-H and N-D bond amplitudes.

## Reproduction target
Produce a single file, `mean_square_displacements.json`, that contains the total mean-square displacements for all atoms in NH4Cl and ND4Cl at temperatures 85, 105, 125, 145, and 165 K. The file must be a JSON object with the keys `NH4Cl` and `ND4Cl`. Each is an array of objects with fields `T_K` (integer temperature), `Cl_u2`, `N_u2`, `H_perp_u2`, `H_par_u2` (for NH4Cl; for ND4Cl use `D_perp_u2` and `D_par_u2`). The values are total mean-square displacements in units of 10⁻³ Å². The file must also contain the top-level keys `NH_bond_amplitude` and `ND_bond_amplitude`, each a float in the same units, representing the mean-square amplitude of the N-H and N-D bond vibrations. This calculation must be based on the rigid ion-rigid molecule lattice-dynamical model and the internal vibration force constants described above.

## Assets

- Teh (1972) rigid ion-rigid molecule model parameters for NH4Cl: 10.1139/p72-392
- Ramaswamy & Ranganathan (1968) force constants for NH4+ ion
- Crystal structure of NH4Cl (space group Pm-3m, lattice parameters)

## Workflow steps

### Step 1: Compute phonon eigenmodes
- Role: process
- Action: Construct the dynamical matrix D = m^{-1/2}(R+ZCZ)m^{-1/2} using the rigid ion-rigid molecule model parameters from Teh (1972) and Ewald summation for the Coulomb matrix C. Diagonalize D on a regular mesh of wave vectors in the first Brillouin zone, handling the acoustic-mode divergence. Produce eigenfrequencies and eigenvectors.
- Evidence: `/app/outputs/eigenmodes.npy`

### Step 2: Calculate external mean-square displacements
- Role: process
- Action: Using the phonon eigenmodes from step1 and the expression for translational and rotational mean-square displacements, calculate translational <u²> for Cl, NH4 group, and ND4 group, and rotational <θ²> for NH4/ND4 at temperatures 85, 105, 125, 145, 165 K. Convert the acoustic-mode q=0 divergence by integrating over a sphere.
- Evidence: `/app/outputs/external_msd.json`

### Step 3: Calculate internal vibration contributions
- Role: process
- Action: Using force constants from Ramaswamy & Ranganathan (1968) and the method of Cyvin, compute the mean-square displacement contributions from internal vibrations of the NH4/ND4 groups for N, H, and D atoms, including perpendicular and parallel components relative to the N-H or N-D bond.
- Evidence: `/app/outputs/internal_vibration.json`

### Step 4: Combine and report total mean-square displacements
- Role: scored (load-bearing)
- Action: Combine the external translational/rotational MSDs and internal vibration contributions using the rigid-body libration formalism to obtain total mean-square displacements for all atoms in NH4Cl and ND4Cl at each temperature. Also compute the N-H and N-D bond mean-square amplitudes. Write the final numbers into mean_square_displacements.json according to the output contract.
- Output file: `/app/outputs/mean_square_displacements.json`
- Format: json
- Contract: JSON object with keys 'NH4Cl' and 'ND4Cl', each an array of objects with fields T_K (int), Cl_u2 (float), N_u2 (float), H_perp_u2 (float), H_par_u2 (float) for NH4Cl and similarly with D for ND4Cl. Top-level keys 'NH_bond_amplitude' and 'ND_bond_amplitude' (float). All values in units of 10^-3 Å^2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mean_square_displacements.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mean_square_displacements.json
- path: `/app/outputs/mean_square_displacements.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total mean-square displacements of atoms in NH4Cl and ND4Cl at 85, 105, 125, 145, 165 K and N-H/N-D bond amplitudes.
- schema:
  - `type`: object
  - `required_keys`: `NH4Cl`, `ND4Cl`, `NH_bond_amplitude`, `ND_bond_amplitude`
  - `properties`:
    - `NH4Cl`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required_keys`: `T_K`, `Cl_u2`, `N_u2`, `H_perp_u2`, `H_par_u2`
    - `ND4Cl`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required_keys`: `T_K`, `Cl_u2`, `N_u2`, `D_perp_u2`, `D_par_u2`
    - `NH_bond_amplitude`:
      - `type`: number
    - `ND_bond_amplitude`:
      - `type`: number
  - `units`: All numeric values are in 10^-3 Å^2

Notes: The agent must re-implement the lattice dynamics and internal vibration calculations using open-source tools. The scoring compares the agent's computed values to the paper's reported Tables 3 and 4 and bond amplitudes within a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mean_square_displacements.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "NH4Cl",
          "ND4Cl",
          "NH_bond_amplitude",
          "ND_bond_amplitude"
        ],
        "properties": {
          "NH4Cl": {
            "type": "array",
            "items": {
              "type": "object",
              "required_keys": [
                "T_K",
                "Cl_u2",
                "N_u2",
                "H_perp_u2",
                "H_par_u2"
              ]
            }
          },
          "ND4Cl": {
            "type": "array",
            "items": {
              "type": "object",
              "required_keys": [
                "T_K",
                "Cl_u2",
                "N_u2",
                "D_perp_u2",
                "D_par_u2"
              ]
            }
          },
          "NH_bond_amplitude": {
            "type": "number"
          },
          "ND_bond_amplitude": {
            "type": "number"
          }
        },
        "units": "All numeric values are in 10^-3 Å^2"
      },
      "description": "Total mean-square displacements of atoms in NH4Cl and ND4Cl at 85, 105, 125, 145, 165 K and N-H/N-D bond amplitudes."
    }
  ],
  "notes": "The agent must re-implement the lattice dynamics and internal vibration calculations using open-source tools. The scoring compares the agent's computed values to the paper's reported Tables 3 and 4 and bond amplitudes within a hidden tolerance."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the final `mean_square_displacements.json` file. The verifier compares each reported mean-square displacement value and bond amplitude to a set of hidden reference values (derived from the original paper's results). For each entry, the verifier checks whether the computed value agrees with the reference within a tolerance. The overall reward is the proportion of entries (temperature–atom–component combinations) that fall within the allowed deviation. No credit is given for simply formatting the file correctly; the numbers themselves must be physically correct, as obtained from the lattice-dynamical and internal vibration calculations. Intermediate evidence files (eigenmodes, external_msd, internal_vibration) are not directly scored, but they support the reproducible execution of the pipeline.
