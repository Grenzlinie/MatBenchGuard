# Anisotropic dislocation node angles in α-iron

## Problem background
Dislocation interactions govern the shape and stability of dislocation nodes and networks in crystalline materials. When multiple dislocations meet, the balance of elastic forces determines the equilibrium angle between the dislocation rays. In anisotropic media, the elastic field of a dislocation cannot be expressed in closed form, and isotropic approximations lead to both quantitative and qualitative errors. Accurately predicting the equilibrium node angles in a material such as body-centered cubic (bcc) iron requires a full anisotropic treatment. The problem is to compute the equilibrium angle 2α for a symmetric three‑fold dislocation node in α‑iron on the (1̄10) glide plane, using anisotropic elasticity and the energy‑factor formalism.

## Approach
The method is based on the energy‑factor approach to planar dislocation interactions. For a given glide plane and Burgers vector, the energy factor tensor K_ij(θ) and its angular derivative K'_ij(θ) are computed as continuous functions of the orientation angle θ via the Barnett integral representation. This representation avoids solving the sextic secular equation and yields accurate, degenerate‑free values. From these tables, the normalized in‑plane traction components T_i(θ) and their angular derivatives T'_i(θ) are derived. The tractions enter the Peach–Koehler force evaluation for each straight dislocation segment. For a three‑fold node with Burgers vectors ½a[111], ½a[1̄11], and a[001] on the (1̄10) plane, the net moment on each ray is expressed in terms of the tractions, and the equilibrium angle 2α is obtained by requiring zero moment. Two configurations are considered: (i) the isolated node, where the three rays are semi‑infinite, and (ii) the network node, where a finite central segment and its interactions modify the angle. The analysis is confined to the symmetric node, and the required elastic constants of α‑iron are taken from standard literature values (C11, C12, C44).

## Reproduction target
Compute the equilibrium node angle 2α (in degrees) for the symmetric three‑fold node in α‑iron on the (1̄10) plane: the isolated node angle using semi‑infinite dislocation rays, and the network node angle incorporating finite‑segment corrections. Write both angles to `/app/outputs/node_angles.json` in the format specified under the output contract.

## Assets

- Elastic constants of α-iron (C11, C12, C44)

## Workflow steps

### Step 1: Generate energy factor tables for α-iron on (1̄10) plane
- Role: process
- Action: Implement the Barnett integral method to compute the energy factor tensor K_ij(θ) and its angular derivative K'_ij(θ) on the (1̄10) glide plane as functions of orientation angle θ, using the elastic constants of α-iron (C11, C12, C44). Generate tables at 5° intervals over 0–360°.
- Evidence: `/app/outputs/energy_factor_data.json`

### Step 2: Compute traction functions from energy factors
- Role: process
- Action: Transform the energy factor tables into the normalized in-plane traction components T_i(θ) and their angular derivatives T'_i(θ) for the Burgers vector b = ½a[111] in the crystal-axis frame.
- Evidence: `/app/outputs/traction_data.json`

### Step 3: Compute equilibrium node angles
- Role: scored (load-bearing)
- Action: Using the traction functions, solve the moment balance for the three-fold node with Burgers vectors ½a[111], ½a[1̄11], and a[001] on the (1̄10) plane. Compute the equilibrium angle 2α for the isolated node (semi-infinite dislocation rays) and the network node (including finite segment corrections). Write the results as JSON.
- Output file: `/app/outputs/node_angles.json`
- Format: json
- Contract: {"type":"object","properties":{"isolated_angle_2alpha_degrees":{"type":"number"},"network_angle_2alpha_degrees":{"type":"number"}},"required":["isolated_angle_2alpha_degrees","network_angle_2alpha_degrees"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/node_angles.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### node_angles.json
- path: `/app/outputs/node_angles.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium node angles (2α) for the symmetric three-fold node in α-iron. Isolated angle from semi-infinite dislocation rays; network angle including finite segment interactions.
- schema:
  - `type`: object
  - `properties`:
    - `isolated_angle_2alpha_degrees`:
      - `type`: number
    - `network_angle_2alpha_degrees`:
      - `type`: number
  - `required`: `isolated_angle_2alpha_degrees`, `network_angle_2alpha_degrees`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "node_angles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "isolated_angle_2alpha_degrees": {
            "type": "number"
          },
          "network_angle_2alpha_degrees": {
            "type": "number"
          }
        },
        "required": [
          "isolated_angle_2alpha_degrees",
          "network_angle_2alpha_degrees"
        ]
      },
      "description": "Equilibrium node angles (2α) for the symmetric three-fold node in α-iron. Isolated angle from semi-infinite dislocation rays; network angle including finite segment interactions."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently examines the artifacts produced by your workflow. The primary scored artifact is `node_angles.json`: the verifier reads the two angles and compares each against internally stored reference values. Both angles must fall within prescribed tolerances to receive full credit; the score degrades as the mismatch increases. Additional intermediate outputs may be audited for consistency but carry little weight. Reporting the paper’s numbers alone is not sufficient—the reproduction must be reached by running the computational pipeline described above.
