# Simulation evidence for rotating-rectangles deformation mechanism in α-cristobalite

## Problem background
α-cristobalite is a silicate that exhibits negative Poisson's ratio (auxetic) – it becomes wider when stretched. Previous models explained this by rotations of rigid SiO₄ tetrahedra. This work explores an alternative two‑dimensional “rotating rectangles” mechanism: when viewed along the (100) or (010) planes, the crystal projects as connected rectangles; relative rotation of these rectangles under load would produce the auxetic effect. The question is whether, under uniaxial stress, the deformation is dominated by the rotation of these rectangles, as opposed to changes in the rectangle dimensions themselves. Answering this question requires computing the change of specific geometric parameters with applied stress using molecular mechanics simulations.

## Approach
The approach tests the rotating‑rectangles hypothesis by simulating the mechanical response of α-cristobalite under uniaxial stress with the CVFF force-field and measuring how the rectangle-related geometry evolves.

A simulation cell is built from the α-cristobalite crystal structure (CIF) and oriented so that the [001] direction lies along the Z‑axis and the (100) plane is parallel to the YZ‑plane. Uniaxial tensile stress is applied in the [011] direction, which lies within the (100) plane and corresponds to the direction that would maximize any auxetic effect arising from rectangle rotation. A series of energy minimisations is performed at incrementally increasing stress levels; at each step atomic positions and transverse cell dimensions are relaxed.

For each stress, the energy‑minimised configuration is analysed in the (100) plane. The projections of the following geometric quantities are measured:
- The four side lengths of a representative rectangle (l₁ – l₄, in Å),
- The four internal angles of that rectangle (ω₁ – ω₄, in degrees),
- The two distances between opposite corners of adjacent rectangles (d₁, d₂, in Å),
- The two angles formed between adjacent rectangles (θ₁, θ₂, in degrees).

By plotting these parameters as functions of stress, one can compare the rate of change of the inter‑rectangle angles θ₁, θ₂ and distances d₁, d₂ to that of the rectangle‑internal lengths l and angles ω. A rotating‑rectangles mechanism would manifest as a disproportionally larger change in the inter‑rectangle parameters.

## Reproduction target
Produce a CSV file, `geometric_params.csv`, containing the stress‑dependent geometric parameters measured from a series of uniaxial stress simulations on α-cristobalite. The simulation must apply tensile stress in the [011] direction at a minimum of five levels covering approximately 0 GPa to 2 GPa, and extract the following quantities in the (100) plane:
- stress (GPa)
- l1, l2, l3, l4 (Å)
- w1, w2, w3, w4 (degrees)
- d1, d2 (Å)
- theta1, theta2 (degrees)

The delivered CSV will be the primary input for the verifier, which will quantify the relative sensitivity of the inter‑rectangle and intra‑rectangle parameters to applied stress.

## Assets

- α-cristobalite crystal structure (CIF): https://www.crystallography.net/cod/9008092.cif
- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Uniaxial stress energy minimizations
- Role: process
- Action: Build an α-cristobalite simulation cell from the public CIF, orient it with the [001] direction along Z and the (100) plane parallel to the YZ-plane. Assign the CVFF force-field. Perform a series of energy minimisations under uniaxial tensile stress applied in the [011] direction (within the (100) plane), relaxing atomic positions and transverse cell dimensions at each stress. Use at least 5 stress levels covering a range from 0 to approximately 2 GPa. Save the minimised configurations so that geometric parameters can be measured.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Geometric parameter measurement
- Role: scored (load-bearing)
- Action: For each stress level, from the energy-minimised configuration, measure the projections in the (100) plane of: the four rectangle side lengths (l1–l4, in Å), the four internal angles (ω1–ω4, in degrees), the two distances between opposite corners of adjacent rectangles (d1, d2, in Å), and the two angles between adjacent rectangles (θ1, θ2, in degrees). Write a CSV file `geometric_params.csv` containing the columns stress (GPa), l1, l2, l3, l4, w1, w2, w3, w4, d1, d2, theta1, theta2. Include at least 5 rows spanning the applied stress range.
- Output file: `/app/outputs/geometric_params.csv`
- Format: csv
- Contract: CSV with columns: stress (GPa, float), l1 (Ang, float), l2 (Ang, float), l3 (Ang, float), l4 (Ang, float), w1 (deg, float), w2 (deg, float), w3 (deg, float), w4 (deg, float), d1 (Ang, float), d2 (Ang, float), theta1 (deg, float), theta2 (deg, float). All values numeric. At least 5 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometric_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometric_params.csv
- path: `/app/outputs/geometric_params.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing geometric parameters measured from energy-minimised structures under each applied uniaxial stress. Used to verify that the angles between rectangles (theta1, theta2) change much faster than the rectangle-internal dimensions (l1–l4, w1–w4), confirming the rotating‑rectangles mechanism.
- schema:
  - `type`: table
  - `required_columns`: `stress`, `l1`, `l2`, `l3`, `l4`, `w1`, `w2`, `w3`, `w4`, `d1`, `d2`, `theta1`, `theta2`
  - `units`:
    - `stress`: GPa
    - `l1`: Ang
    - `l2`: Ang
    - `l3`: Ang
    - `l4`: Ang
    - `d1`: Ang
    - `d2`: Ang
    - `w1`: deg
    - `w2`: deg
    - `w3`: deg
    - `w4`: deg
    - `theta1`: deg
    - `theta2`: deg

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometric_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "stress",
          "l1",
          "l2",
          "l3",
          "l4",
          "w1",
          "w2",
          "w3",
          "w4",
          "d1",
          "d2",
          "theta1",
          "theta2"
        ],
        "units": {
          "stress": "GPa",
          "l1": "Ang",
          "l2": "Ang",
          "l3": "Ang",
          "l4": "Ang",
          "d1": "Ang",
          "d2": "Ang",
          "w1": "deg",
          "w2": "deg",
          "w3": "deg",
          "w4": "deg",
          "theta1": "deg",
          "theta2": "deg"
        }
      },
      "description": "CSV file containing geometric parameters measured from energy-minimised structures under each applied uniaxial stress. Used to verify that the angles between rectangles (theta1, theta2) change much faster than the rectangle-internal dimensions (l1–l4, w1–w4), confirming the rotating‑rectangles mechanism."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads `geometric_params.csv` and performs an independent analysis. For each parameter, it fits a linear regression against stress and computes the slope. It then compares the slopes of the angles between rectangles (theta1, theta2) to those of the rectangle side lengths (l1–l4) and internal angles (w1–w4). The reward is monotonic and reflects how much more rapidly the inter‑rectangle angles change relative to the intra‑rectangle dimensions. A solution that shows a clear dominance of the inter‑rectangle angle slopes over the intra‑rectangle slopes earns the highest credit; results where the slopes are comparable or where the intra‑rectangle parameters change faster receive progressively lower rewards. The verifier does not rely on exact numerical agreement with any published value but assesses the trend that the simulations produce.
