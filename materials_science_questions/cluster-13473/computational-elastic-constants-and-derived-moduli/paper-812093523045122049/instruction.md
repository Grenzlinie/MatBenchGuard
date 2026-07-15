# Six Elastic Constants of Dehydrated HEW Lysozyme Crystals via Christoffel Equations

## Problem background
Tetragonal hen egg-white (HEW) lysozyme crystals belong to the 422 point group and have six independent elastic constants: C11, C12, C13, C33, C44, and C66. Determining these constants is essential for understanding defect structures, deformation, and fracture of protein crystals. By measuring ultrasonic sound velocities along specific crystallographic directions and the density of the crystal, the Christoffel equations can be solved to obtain the elastic constants. In the paper, such measurements were performed on HEW lysozyme crystals dehydrated at 42% relative humidity, yielding the set of six constants. The present task is to reproduce this computation: from the given density, sound velocities, and propagation angle, compute the six elastic constants.

## Approach
The Christoffel equations for a tetragonal 422 crystal relate the density ρ, the sound velocities v, and the elastic constants Cij. For pure longitudinal and transverse modes along high-symmetry directions the relations are simple algebraic equations. For a quasilongitudinal mode propagating at an angle θ to the c-axis, the velocity v6 satisfies a more complex equation that couples C11, C33, C44, C13, and θ. The overall scheme is to first compute C44 and C66 directly from the pure transverse velocities, then solve for C11 and C12 using the relations for longitudinal and transverse waves along [110], obtain C33 from the pure [001] longitudinal velocity, and finally determine C13 by numerically solving the quasilongitudinal equation for v6. All required inputs (density ρ=1.29 Mg/m³, seven sound velocities in m/s, and the angle θ=22.8°) are given and are fixed public values. No external data download is necessary. The agent must implement this scheme in a Python script that reads the fixed numeric inputs (or directly use them as constants) and produces the six elastic constants in GPa.

## Reproduction target
Compute the six independent elastic constants C11, C12, C13, C33, C44, and C66 (in GPa, rounded to two decimal places) for tetragonal HEW lysozyme crystals dehydrated at 42% relative humidity. Use the following inputs: density ρ = 1.29 Mg/m³, sound velocities v1=3097, v2=1518, v3=1448, v4=3149, v5=1505, v6=3197, v7=1481 (all in m/s), and angle θ = 22.8°. Solve the Christoffel equations for the 422 crystal class to obtain the six constants and write them to a JSON file named elastic_constants.json under `/app/outputs`.

## Assets

- Python 3: python

## Workflow steps

### Step 1: Compute elastic constants from Christoffel equations
- Role: scored (load-bearing)
- Action: Write a Python script that takes as fixed inputs the density rho=1.29 Mg/m^3, sound velocities v1=3097, v2=1518, v3=1448, v4=3149, v5=1505, v6=3197, v7=1481 m/s, and angle theta=22.8°. Solve the Christoffel equations for a tetragonal 422 crystal to compute the six independent elastic constants. Procedure: 1) Compute C44 = rho * v2^2. 2) Compute C66 from rho*v5^2 = C44*cos^2(theta) + C66*sin^2(theta). 3) Compute C11 - C12 = 2 * rho * v3^2. 4) Compute C11 + C12 from rho*v1^2 = (C11+C12+2*C66)/2. 5) Solve for C11 and C12 individually. 6) Compute C33 = rho * v4^2. 7) Compute C13 by solving the quasilongitudinal Christoffel equation for v6 using the already determined C11, C33, C44 and the known theta, v6 (e.g., via root-finding or algebraic manipulation). Output a JSON file with keys C11, C12, C13, C33, C44, C66 (values in GPa, rounded to two decimal places).
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: A JSON object with keys "C11", "C12", "C13", "C33", "C44", "C66". Each value is a float representing the elastic constant in GPa, rounded to two decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The six independent elastic constants of dehydrated tetragonal HEW lysozyme crystals, computed from given sound velocities, density, and angle.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (GPa)
    - `C12`: float (GPa)
    - `C13`: float (GPa)
    - `C33`: float (GPa)
    - `C44`: float (GPa)
    - `C66`: float (GPa)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The solver must derive the constants purely from the provided public numeric inputs; no external data download is required. The hidden verifier compares the agent's computed values against the paper-reported values using relative and absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float (GPa)",
          "C12": "float (GPa)",
          "C13": "float (GPa)",
          "C33": "float (GPa)",
          "C44": "float (GPa)",
          "C66": "float (GPa)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "The six independent elastic constants of dehydrated tetragonal HEW lysozyme crystals, computed from given sound velocities, density, and angle."
    }
  ],
  "notes": "The solver must derive the constants purely from the provided public numeric inputs; no external data download is required. The hidden verifier compares the agent's computed values against the paper-reported values using relative and absolute tolerances."
}
```

## How you are scored
The hidden verifier will read your `elastic_constants.json`, extract the six elastic constant values, and compare each one to reference values using appropriate relative and absolute tolerances. Each constant (C11, C12, C13, C33, C44, C66) carries equal weight. The total reward is the fraction of constants that fall within the allowed tolerance. The output must be a JSON object with the keys exactly as specified and the values in GPa rounded to two decimal places. There is no other scored artifact; this single stage accounts for the entire reward.
