# Lattice Energy of Orthorhombic Acetylene with Ellipsoidal Core Potential

## Problem background
The low-temperature orthorhombic phase of solid acetylene is held together by van der Waals forces and electrostatic quadrupolar interactions. The acetylene molecule is elongated, so its intermolecular interactions depend sensitively on molecular shape. A physically accurate description of the lattice energy must account for the ellipsoidal shape of the molecules in both the repulsive core and the long-range electrostatic terms. This task asks you to compute the lattice energy of the orthorhombic acetylene crystal using a shape-dependent pair potential that combines a Kihara core term extended to prolate ellipsoids and a spheroidal quadrupole-quadrupole interaction.

## Approach
The method models each acetylene molecule as a prolate ellipsoid with a quadrupole moment. The intermolecular pair potential U is the sum of two terms: (i) the Kihara core potential U_K(ρ) = U₀[(ρ₀/ρ)¹² − 2(ρ₀/ρ)⁶], evaluated at the shortest distance ρ between the ellipsoidal cores, and (ii) the electrostatic quadrupolar interaction U_ΘΘ expressed in prolate spheroidal coordinates. The core geometry is defined by the major semi-axis a, the focal distance d, and the derived minor semi-axes b = c. The potential parameters U₀, ρ₀, and the quadrupole moment Θ are taken from independent experiments and are provided in the workflow steps. Using the published crystal structure (unit cell parameters, space group, molecular positions and orientations), you will generate the positions of all molecules in the unit cell, identify all neighbor pairs within a 0.7 nm cutoff from a reference molecule, compute the pair interactions, and sum them to obtain the lattice energy.

## Reproduction target
Reproduce the lattice energy of the orthorhombic acetylene crystal by implementing the ellipsoidal-core pair potential and the spheroidal quadrupolar interaction. Compute the pair energy for each of the 19 nearest neighbor pairs (within 0.7 nm) and take half the sum. Output the resulting lattice energy as a single decimal number (in kJ mol⁻¹) to the file lattice_energy.txt.

## Assets

- Orthorhombic acetylene (C2D2) crystal structure from Koski & Sandor (1975)

## Workflow steps

### Step 1: Define prolate ellipsoid core geometry for acetylene
- Role: process
- Action: Define acetylene as a prolate ellipsoid with major semi-axis a = 0.17 nm and focal distance d = 0.33 nm (the distance between the two hydrogen foci). Compute the minor semi-axes b = c from the ellipsoid focal relation d = 2√(a² - b²). Record the resulting geometry parameters for use in subsequent steps.
- Evidence: none

### Step 2: Set up orthorhombic crystal structure and neighbor list
- Role: process
- Action: Using the orthorhombic cell parameters (a_X = 0.6193 nm, b_Y = 0.6005 nm, c_Z = 0.5551 nm, space group Acam) and the following explicit molecular data (from Tables 4 and 5):
- Direction cosines matrix (angle θ = 0.6894 rad) from crystal XYZ to molecule-fixed xyz:
  |     | x       | y | z        |
  | X   | -cosθ   | 0 | -sinθ    |
  | Y   | -sinθ   | 0 |  cosθ    |
  | Z   | 0       | 1 | 0       |
- Fractional positions and orientation sign vectors (x,y,z) for the four molecules:
  Molecule 1: position (0, 0, 0), orientation (1, 1, 1)
  Molecule 2: position (1/2, 1/2, 0), orientation (1, -1, -1)
  Molecule 3: position (0, 1/2, 1/2), orientation (1, 1, 1)
  Molecule 4: position (1/2, 0, 1/2), orientation (1, -1, -1)
  The orientation signs indicate whether the molecular axis aligns (+) or anti-aligns (-) with the direction-cosine matrix. Generate the Cartesian coordinates of all molecules in the unit cell by converting fractional coordinates to Cartesian using the cell vectors (a along X, b along Y, c along Z) and apply the orientation matrix with the sign adjustments. From a reference molecule at the origin, identify all neighbors whose center-to-center distance ≤ 0.7 nm (the set of 19 molecules used in the paper).
- Evidence: none

### Step 3: Compute pair interactions and lattice energy
- Role: scored (load-bearing)
- Action: For each of the 19 neighbor pairs, compute: (i) center-to-center distance R, (ii) the shortest distance ρ between the prolate ellipsoidal cores using the ellipsoid geometry, (iii) the prolate spheroidal coordinates (λ, μ, φ) of the second molecule's center in the first molecule's coordinate system. Evaluate the Kihara core potential U_K(ρ) = U₀[(ρ₀/ρ)¹² - 2(ρ₀/ρ)⁶] with U₀ = 3.32 kJ mol⁻¹ and ρ₀ = 0.268 nm, and the spheroidal quadrupolar interaction U_ΘΘ using the formula involving the quadrupole moment Θ = 2.4×10⁻³⁹ C m². Sum U = U_K + U_ΘΘ for all pairs, take half the sum to obtain the lattice energy, and write that single decimal number (in kJ mol⁻¹) to lattice_energy.txt.
- Output file: `/app/outputs/lattice_energy.txt`
- Format: txt
- Contract: Single floating-point number, e.g. -25.10, representing the lattice energy in kJ mol⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energy.txt
- path: `/app/outputs/lattice_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Reproduced lattice energy of orthorhombic acetylene crystal using the ellipsoidal Kihara core plus spheroidal quadrupolar interaction model.
- schema:
  - `type`: text
  - `format`: single_number
  - `units`: kJ mol⁻¹
  - `description`: A single decimal number representing the half-sum of pair potentials over the 19 neighbors.

Notes: The exact tolerance is hidden. The agent must compute the energy from first principles; the hidden gold is the paper-reported value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single_number",
        "units": "kJ mol⁻¹",
        "description": "A single decimal number representing the half-sum of pair potentials over the 19 neighbors."
      },
      "description": "Reproduced lattice energy of orthorhombic acetylene crystal using the ellipsoidal Kihara core plus spheroidal quadrupolar interaction model."
    }
  ],
  "notes": "The exact tolerance is hidden. The agent must compute the energy from first principles; the hidden gold is the paper-reported value."
}
```

## How you are scored
A hidden verifier will read the contents of lattice_energy.txt and compare your computed lattice energy to a hidden reference value obtained from an independent evaluation of the same model. The verifier assigns a reward between 0 and 1 based on how close your computed value is to the reference; the value must be produced through genuine computation, not by simply reporting a known number. The reward is the sole score for this task.
