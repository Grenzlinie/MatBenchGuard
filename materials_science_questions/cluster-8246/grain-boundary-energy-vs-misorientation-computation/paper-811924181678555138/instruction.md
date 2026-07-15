# Molecular dynamics simulation of tilt grain boundaries in Ni3Al

## Problem background
Grain boundaries strongly influence the mechanical and physical properties of polycrystalline materials, yet the dependence of grain-boundary energy on misorientation angle remains an active topic of investigation. The intermetallic compound Ni₃Al (L1₂ structure) serves as a model system for such studies. This task aims to compute the specific grain-boundary energy for {111} and {100} tilt boundaries in Ni₃Al as a function of misorientation angle using molecular dynamics simulations, in order to understand the energy behavior of these two important boundary families.

## Approach
The simulation uses classical molecular dynamics with pairwise Morse potentials to describe interatomic forces, including interactions up to the fifth coordination shell. For each tilt axis ({111} and {100}), a bicrystal block is constructed by rotating the upper and lower halves of a perfect L1₂ Ni₃Al block by ±θ/2, creating a planar tilt grain boundary at the block center. Overlapping atoms are removed. Fixed boundary conditions are applied normal to the grain boundary plane, and periodic conditions along the tilt axis. A perfect crystal block of identical dimensions serves as an energy reference. Both blocks are relaxed at a low temperature (50–150 K) for 100 ps after initializing velocities from a Maxwell distribution with zero total momentum. The specific grain-boundary energy is obtained from the difference in total potential energy between the bicrystal and the perfect crystal, divided by the boundary area. This process is repeated for a set of misorientation angles θ to produce energy-versus-angle curves for the two tilt boundary families.

## Reproduction target
Produce a CSV file, gb_energy_data.csv, with columns: tilt_axis, angle_deg, energy_Jm2. The tilt_axis must be either '111' or '100', and angle_deg is the misorientation angle in degrees. Provide data for at least 6 distinct angles per tilt axis, covering both low and high angles. The energy_Jm2 values should be positive and computed from the MD relaxations using the Morse potential parameters for Ni₃Al described in the resources.

## Assets

- Morse potential parameters for Ni₃Al (Tsaregorodtsev et al., 1984)
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Crystal structure of Ni₃Al (L1₂)

## Workflow steps

### Step 1: Construct bicrystal with tilt grain boundary
- Role: process
- Action: For a given tilt axis ({111} or {100}) and misorientation angle θ, build a parallelepiped bicrystal block containing 2×10⁵ – 5×10⁵ atoms using the L1₂ Ni₃Al structure. Rotate the two halves by ±θ/2 to create a planar tilt grain boundary at the block center; remove overlapping atoms beyond the boundary plane. Apply fixed boundary conditions on faces perpendicular to the GB and periodic conditions along the tilt axis. Record the GB area S.
- Evidence: `/app/outputs/initial_bicrystal.data`

### Step 2: Construct perfect crystal reference
- Role: process
- Action: Build a perfect crystal block with the same dimensions and total number of atoms as the bicrystal from step 1, using the same L1₂ Ni₃Al structure.
- Evidence: none

### Step 3: MD relaxation of bicrystal
- Role: process
- Action: Assign Morse pair potentials (parameters from Tsaregorodtsev et al., 1984, five coordination spheres) to the bicrystal. Initialize atomic velocities from a Maxwell distribution corresponding to a temperature in the 50–150 K range, zero total momentum. Run molecular dynamics for 100 ps with the boundary conditions from step 1. Extract the total potential energy U₁ of the final relaxed configuration.
- Evidence: `/app/outputs/relaxation_bicrystal.log`

### Step 4: MD relaxation of perfect crystal
- Role: process
- Action: Repeat the MD relaxation protocol of step 3 on the perfect crystal block from step 2. Use identical potential, temperature range, and simulation time. Extract the total potential energy U₀.
- Evidence: none

### Step 5: Compute GB energies and compile data
- Role: scored (load-bearing)
- Action: For every combination of tilt axis ({111}, {100}) and a set of misorientation angles θ (at least 6 per axis, covering low and high angles), compute the specific grain-boundary energy E = (U₁ - U₀) / S and write a CSV file with the results.
- Output file: `/app/outputs/gb_energy_data.csv`
- Format: csv
- Contract: CSV with header: tilt_axis,angle_deg,energy_Jm2. tilt_axis is either '111' or '100'; angle_deg is a float (degrees); energy_Jm2 is a positive float (J/m²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gb_energy_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gb_energy_data.csv
- path: `/app/outputs/gb_energy_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of computed grain-boundary energies. The scoring verifies the structural trend: for each angle present in both families, E for '111' must exceed that for '100', and all energies must lie in a plausible positive range.
- schema:
  - `type`: table
  - `columns`:
    - `tilt_axis`: string, either '111' or '100'
    - `angle_deg`: float (degrees)
    - `energy_Jm2`: float (J/m², positive)

Notes: The verification targets the paper's central claim that {111} tilt boundaries have higher energy than {100} tilt boundaries. The absolute value of energy is not compared to a specific paper number, only the relative ordering and physical sanity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gb_energy_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "columns": {
          "tilt_axis": "string, either '111' or '100'",
          "angle_deg": "float (degrees)",
          "energy_Jm2": "float (J/m², positive)"
        }
      },
      "description": "Table of computed grain-boundary energies. The scoring verifies the structural trend: for each angle present in both families, E for '111' must exceed that for '100', and all energies must lie in a plausible positive range."
    }
  ],
  "notes": "The verification targets the paper's central claim that {111} tilt boundaries have higher energy than {100} tilt boundaries. The absolute value of energy is not compared to a specific paper number, only the relative ordering and physical sanity."
}
```

## How you are scored
A hidden verifier will inspect your gb_energy_data.csv. It checks that the file is correctly formatted and that all energy values are positive and lie within a physically plausible range. The verifier then compares the energies for the '111' and '100' tilt axes at each common misorientation angle and evaluates whether the data satisfy the expected physical relationship between these two boundary families. Your final score is the fraction of angles where the relationship holds, with all energy values also required to pass the physical reasonableness check. The verifier does not depend on any particular absolute reference value; it scores the structural trend of the data you produce.
