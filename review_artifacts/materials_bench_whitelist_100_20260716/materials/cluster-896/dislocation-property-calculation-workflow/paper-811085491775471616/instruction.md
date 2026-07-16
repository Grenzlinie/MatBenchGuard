# MD Simulation of Repulsive Dislocation Intersection in Copper

## Problem background
Short-range dislocation interactions are inherently atomistic and cannot be fully described by continuum linear elasticity. The intersection of dislocations in metals involves complex core-scale processes such as junction and jog formation, which govern the strength of obstacles and the mobility of dislocations. Accurately characterizing these reaction products—whether a junction forms, its length and direction, the jog line orientation, and the critical angle at which one dislocation passes through another—is central to building realistic models of plastic deformation. This task reproduces the repulsive intersection of a dissociated 60° dislocation and a screw dislocation in copper using large-scale molecular dynamics (MD) to quantify these short-range interactions.

## Approach
The method employs molecular dynamics (MD) with an embedded-atom method (EAM) potential for copper. Two pre-dissociated dislocations—a 60° mixed dislocation (DB) on glide plane a and a screw dislocation (BA) on glide plane d—are embedded in a simulation cell using linear isotropic continuum elastic displacements. After a brief low-temperature relaxation to allow the partials to reach near-equilibrium separations, a homogeneous compressive strain is applied to drive the intersection. The subsequent MD simulation captures the partial dislocation reactions, the bending and alignment of dislocation segments, and the final configuration after the crossing. Post-simulation analysis extracts geometric and energetic measures: formation and length of any junction line, crystallographic direction of the jog, the critical breaking angle, and the b² energy comparison for the involved partial reactions.

## Reproduction target
Set up and run an MD simulation of the repulsive intersection between the dissociated 60° dislocation (DB) and the dissociated screw dislocation (BA) in fcc Cu using the EAM potential. From the simulation, determine the following and report them in /app/outputs/results.json: (1) whether a junction line forms along the [10-1] direction; (2) its length in units of the nearest-neighbor distance r0; (3) the crystallographic direction of the resulting jog line; (4) the critical breaking angle (in degrees) at which the bowing αB partial segments meet and pass the obstacle; (5) the b² sums (in units of b²) for the reactants and product of the two partial reactions αB+δA and αB+Bδ, to assess the Frank energy criterion.

## Assets

- Cu EAM potential (Voter 1994): lammps
- LAMMPS: https://lammps.org/

## Workflow steps

### Step 1: Generate initial dislocation configuration
- Role: process
- Action: Set up the simulation cell for repulsive dislocation intersection in f.c.c. Cu. Embed a 60° mixed dislocation (DB) dissociated into partials αB and Dα on glide plane a, and a screw dislocation (BA) dissociated into partials δA and Bδ on glide plane d, using atomic displacements from linear isotropic continuum elasticity. Write the atomic configuration to a LAMMPS data file.
- Evidence: `/app/outputs/initial.data`

### Step 2: Relax initial configuration
- Role: process
- Action: Run a short MD relaxation at near 0 K under free boundary conditions to allow the embedded dislocations to dissociate into equilibrium partials.
- Evidence: `/app/outputs/relaxed.data`

### Step 3: Apply compressive loading
- Role: process
- Action: Impose a homogeneous compressive elastic strain ε_zz at a constant strain rate until a target value is reached, then fix the positions of atoms in a few top and bottom layers to maintain the strain while all other atoms remain mobile.
- Evidence: `/app/outputs/strained.data`

### Step 4: Run MD intersection simulation
- Role: process
- Action: Run MD using the Cu EAM potential, evolving the system from the strained configuration to capture the partial reactions, junction formation, jog formation, and passing of the intersecting dislocations. Generate a trajectory file recording atomic positions over time.
- Evidence: `/app/outputs/trajectory.dump`

### Step 5: Analyze junction, jog, and critical angle
- Role: scored (load-bearing)
- Action: From the MD trajectory, identify the partial dislocation reactions and determine: (1) whether a junction line forms along [10-1]; (2) its length in units of r0; (3) the crystallographic direction of the jog line; (4) the critical breaking angle at which the bowing partial segments meet and pass the obstacle. Also compute the b² criterion for the two reactions αB+δA and αB+Bδ, reporting reactant and product squared Burgers‑vector sums. Compile all findings into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: junction_formed (bool), junction_length_r0 (float), jog_direction (string, e.g., '[0-1-1]'), critical_breaking_angle_degrees (float), partial_reaction_b2_analysis (object: for each reaction 'alphaB_deltaA' and 'alphaB_Bdelta', keys 'reactants' [list of strings], 'product' [string], 'reactant_b2_sum' [string/number], 'product_b2' [string/number]).
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
- target_policy: reference_match
- description: Contains the determined junction formation (boolean), junction length in units of r0, jog direction as crystallographic string, critical breaking angle in degrees, and a nested object with b² analysis for the two partial reactions.
- schema:
  - `type`: object
  - `required`:
    - `junction_formed`: boolean
    - `junction_length_r0`: number
    - `jog_direction`: string
    - `critical_breaking_angle_degrees`: number
    - `partial_reaction_b2_analysis`: object
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: Only the repulsive intersection case is required. The hidden checker compares the reported values against reference values from the paper within tolerances.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "junction_formed": "boolean",
          "junction_length_r0": "number",
          "jog_direction": "string",
          "critical_breaking_angle_degrees": "number",
          "partial_reaction_b2_analysis": "object"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Contains the determined junction formation (boolean), junction length in units of r0, jog direction as crystallographic string, critical breaking angle in degrees, and a nested object with b² analysis for the two partial reactions."
    }
  ],
  "notes": "Only the repulsive intersection case is required. The hidden checker compares the reported values against reference values from the paper within tolerances."
}
```

## How you are scored
A hidden verifier evaluates your final artifact (results.json) by comparing the reported junction length, jog direction, critical breaking angle, and b² sums against reference values derived from the original study, using appropriate tolerances. Each quantity contributes a portion of the total reward; the verifier also checks that the junction formation answer is consistent with the directional and b² findings. The evaluation does not rely on you self-reporting a single aggregate metric—every field is independently checked. Correct reproduction of the dislocation intersection process through MD is necessary to obtain values that fall within the expected ranges; fabrication or guesswork will not pass all hidden checks.
