# Phase-field simulation of block copolymer coarsening on curved cylindrical surfaces

## Problem background
Block copolymer thin films deposited on curved substrates can exhibit ordered textures whose orientation couples to the substrate geometry. In cylinder-forming systems, understanding how the curvature influences the alignment of cylindrical microdomains is both a fundamental challenge and relevant for nanofabrication. Phase-field simulations based on the Ohta–Kawasaki / Cahn–Hilliard model provide a computational tool to study microphase separation and coarsening on non-planar surfaces, allowing investigation of the preferred orientation of cylindrical domains relative to geometric features. This task asks you to compute the average orientation angle that emerges from such a simulation on a cylindrical surface, a quantity that reveals the coupling between texture and curvature.

## Approach
The dynamics of microphase separation are described by a conserved order parameter undergoing Cahn–Hilliard evolution governed by an Ohta–Kawasaki free energy functional. The free energy consists of a short‑range Landau term (with parameters for the as‑spun blend) and a long‑range non‑local term that accounts for chain connectivity, producing a wavelength selection. The order parameter represents the local composition contrast between the two blocks. The system is simulated on a two‑dimensional cylindrical surface (a ring cross‑section extruded along the cylinder axis) with periodic boundary conditions along the axis. Starting from a disordered initial state, the order parameter coarsens over time via defect annihilation. After sufficient coarsening, the orientation of the cylindrical microdomains relative to the cylinder long axis is analyzed: the average orientation angle (in degrees, where 0° is parallel and 90° is perpendicular) is computed from the final configuration.

## Reproduction target
Implement the Ohta–Kawasaki / Cahn–Hilliard conserved-order-parameter dynamics on a cylindrical surface with either a circular or pseudo-elliptical cross-section. Use the fixed parameters f=0.4, A=1.5, σ=0.38, λ=0.23, D=0.3, β=0.03, and enforce periodic boundary conditions along the cylinder axis. After allowing the system to coarsen adequately, compute the average orientation angle (in degrees) of the cylindrical domains with respect to the cylinder long axis. Save this result as a JSON file `/app/outputs/orientation.json` with the key `average_orientation`.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Phase-field simulation and orientation analysis
- Role: scored (load-bearing)
- Action: Implement the Ohta-Kawasaki / Cahn-Hilliard conserved-order-parameter dynamics on a cylindrical surface with either circular or pseudo-elliptical cross-section, using the parameters f=0.4, A=1.5, σ=0.38, λ=0.23, D=0.3, β=0.03, and periodic boundary conditions along the cylinder axis. After sufficient coarsening time, compute the average orientation angle (in degrees) of the cylindrical domains relative to the cylinder long axis. Save the result to orientation.json.
- Output file: `/app/outputs/orientation.json`
- Format: json
- Contract: {"average_orientation": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/orientation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### orientation.json
- path: `/app/outputs/orientation.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Average orientation angle of the simulated cylindrical domains relative to the cylinder long axis. The checker compares this to a hidden threshold based on the expected physical behavior.
- schema:
  - `type`: object
  - `required`:
    - `average_orientation`: float (degrees)

Notes: The geometry parameters (cylinder dimensions, cross-section shape, mesh resolution) and numerical solver settings are left to the agent's discretion; the result must reflect the physics captured by the given free-energy parameters and periodic boundary conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "orientation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "average_orientation": "float (degrees)"
        }
      },
      "description": "Average orientation angle of the simulated cylindrical domains relative to the cylinder long axis. The checker compares this to a hidden threshold based on the expected physical behavior."
    }
  ],
  "notes": "The geometry parameters (cylinder dimensions, cross-section shape, mesh resolution) and numerical solver settings are left to the agent's discretion; the result must reflect the physics captured by the given free-energy parameters and periodic boundary conditions."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the `average_orientation` value from `/app/outputs/orientation.json`. The verifier compares your reported angle to a hidden threshold. Full credit is earned if the angle satisfies a predetermined criterion; the exact scoring function is hidden. The verifier does not require an exact match to any particular published number; it rewards results that correctly capture the physics of orientation on curved substrates.
