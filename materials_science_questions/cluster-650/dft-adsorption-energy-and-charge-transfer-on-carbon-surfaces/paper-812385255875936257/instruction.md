# DFT Rotational Barrier of H2 on Coronene

## Problem background
Determining the strength of hydrogen–carbon interactions is essential for evaluating carbon nanomaterials as potential hydrogen storage media. One way to probe this interaction strength is through the rotational dynamics of a hydrogen molecule adsorbed on a carbon surface. When the interaction is weak (physisorption), the molecule rotates almost freely, experiencing only a very small energetic barrier. When the interaction is stronger, the rotation becomes hindered and the barrier increases. In this task, you will compute the rotational barrier for a hydrogen molecule on a model graphite surface — a coronene (C₂₄H₁₂) cluster — using density functional theory. The magnitude of this barrier provides a direct measure of the interaction strength.

## Approach
You will use an open-source DFT code (e.g., Quantum ESPRESSO, CP2K) with a GGA functional (such as PBE or PW91). The target system is an H₂ molecule interacting with a coronene cluster, which serves as a finite-sized model of a graphite surface. The computational procedure consists of three main stages: 1) geometry optimization of the H₂ molecule above the coronene, starting with the molecule placed above the central C–C bond with its bond axis parallel to the surface; 2) a potential energy scan by rotating the optimized H₂ molecule stepwise about an axis perpendicular to the surface; 3) extraction of the rotational barrier from the energy vs. angle data. The results will allow you to quantify how freely the hydrogen molecule rotates on the surface.

## Reproduction target
Your goal is to generate three scored artifacts:
- The equilibrium distance (in Å) between the H₂ center of mass and the coronene plane from the geometry optimization.
- A CSV file containing the energy (in eV) at each rotation angle (in degrees) from the scan.
- The rotational barrier (in meV), defined as the difference between the maximum and minimum total energy from the scan.
The barrier should be very small, consistent with nearly free rotation and weak physisorption.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Optimize H₂ geometry above coronene
- Role: scored
- Action: Perform DFT geometry optimization of a hydrogen molecule above the central C–C bond of a coronene (C₂₄H₁₂) cluster. Initially place the H₂ molecule with its bond axis parallel to the surface at a vertical distance of ~3.0 Å. After optimization, extract the perpendicular distance between the H₂ center of mass and the mean plane of the coronene carbon atoms.
- Output file: `/app/outputs/equilibrium_distance.txt`
- Format: txt
- Contract: single numeric value (float) in Å
- Scoring: scored by hidden verifier

### Step 2: Rotational potential energy scan
- Role: scored (load-bearing)
- Action: Using the optimized geometry from the previous step, rotate the H₂ molecule around the axis perpendicular to the surface (passing through its center of mass) in increments of 10–20° from 0° to 180°. Perform single-point energy calculations at each angle. Save the results as a CSV file with columns angle_deg and energy_eV.
- Output file: `/app/outputs/energy_vs_angle.csv`
- Format: csv
- Contract: two columns: angle_deg (float), energy_eV (float)
- Scoring: scored by hidden verifier

### Step 3: Compute rotational barrier
- Role: scored
- Action: From the energy vs angle data, compute the rotational barrier as the difference between the maximum and minimum total energy. Write the barrier value in meV to a text file.
- Output file: `/app/outputs/rotational_barrier.txt`
- Format: txt
- Contract: single numeric value (float) in meV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_distance.txt`
- `/app/outputs/energy_vs_angle.csv`
- `/app/outputs/rotational_barrier.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_distance.txt
- path: `/app/outputs/equilibrium_distance.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimized equilibrium distance (H₂ center-of-mass to coronene plane) from DFT geometry optimization.
- schema:
  - `type`: text
  - `units`:
    - `value`: Å

### energy_vs_angle.csv
- path: `/app/outputs/energy_vs_angle.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw potential energy scan over rotation angle. The verifier recomputes the rotational barrier from this data.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `energy_eV`

### rotational_barrier.txt
- path: `/app/outputs/rotational_barrier.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Agent-computed rotational barrier. Verified for consistency with the barrier recomputed from energy_vs_angle.csv.
- schema:
  - `type`: text
  - `units`:
    - `value`: meV

Notes: The task reproduces the DFT calculation of the H₂ rotational barrier on a graphite model (coronene). The barrier must be very small (≤0.1 eV) to support the paper's conclusion of weak physisorption. The verifier recomputes the barrier from the CSV and checks the reported distance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_distance.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "Å"
        }
      },
      "description": "Optimized equilibrium distance (H₂ center-of-mass to coronene plane) from DFT geometry optimization."
    },
    {
      "file": "energy_vs_angle.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "energy_eV"
        ]
      },
      "description": "Raw potential energy scan over rotation angle. The verifier recomputes the rotational barrier from this data."
    },
    {
      "file": "rotational_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "units": {
          "value": "meV"
        }
      },
      "description": "Agent-computed rotational barrier. Verified for consistency with the barrier recomputed from energy_vs_angle.csv."
    }
  ],
  "notes": "The task reproduces the DFT calculation of the H₂ rotational barrier on a graphite model (coronene). The barrier must be very small (≤0.1 eV) to support the paper's conclusion of weak physisorption. The verifier recomputes the barrier from the CSV and checks the reported distance."
}
```

## How you are scored
A hidden verifier will independently evaluate each of your three output files. The verifier recomputes the rotational barrier from your `energy_vs_angle.csv` and checks that the value you report in `rotational_barrier.txt` is self-consistent. The barrier magnitude is the primary scoring criterion: a very small barrier (indicating weak physisorption) yields full credit. The equilibrium distance in `equilibrium_distance.txt` is checked for physical reasonableness (it should lie within a plausible range for a van der Waals complex). The different checks are weighted and combined into a single reward between 0 and 1. Reporting a paper's numbers is not enough; you must perform the actual DFT calculations and produce the data as described in the workflow steps.
