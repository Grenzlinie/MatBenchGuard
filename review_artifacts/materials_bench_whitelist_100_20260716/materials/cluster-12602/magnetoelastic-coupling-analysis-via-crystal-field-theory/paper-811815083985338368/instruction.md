# Magnetoelastic Spin Textures around Edge Dislocation in Rare-Earth Films

## Problem background
Rare-earth metals exhibit strong magnetoelastic coupling, which can lead to the formation of intricate nanoscale spin textures around structural defects such as dislocations. In Dy(0001) films, edge dislocations with a \([2\overline{1}\overline{1}0]\) Burgers vector are known to pin magnetic domain walls and can give rise to vortex‑like or lobe‑shaped spin structures. The objective of this computational task is to determine the equilibrium in-plane spin configuration around a single edge dislocation in a Dy(0001) film through micromagnetic energy minimization, and to compute the resulting magnetic signal as observable by a spin‑polarized STM tip.

## Approach
A micromagnetic model is constructed for a two‑dimensional hexagonal lattice of Dy ions with the dislocation core at the center. The stress field of the edge dislocation is computed using the anisotropic elasticity formulas for a hexagonal crystal, requiring the hexagonal elastic constants of Dy and the Burgers vector. The total free energy per layer includes basal‑plane magnetocrystalline anisotropy (a six‑fold term \(\propto \cos(6\varphi)\)), magnetoelastic energy that couples the dislocation stress field to the local moment direction via magnetostriction constants, long‑range dipolar interactions, and nearest‑neighbour exchange. A Zeeman term equivalent to an in‑plane field of approximately 1 kOe is added to localise the structure. Periodic boundary conditions are applied with the moment direction fixed at the boundaries. The free energy is minimised numerically with respect to the in‑plane spin angles at each lattice site using a suitable optimiser. From the equilibrium spin configuration, the magnetic signal is computed as the projection of the normalised magnetic moment onto a fixed tip magnetisation direction (oriented at a known angle relative to the domain’s easy axis). This signal is then extracted along counter‑clockwise circular line sections at radii of 7 nm and 3.5 nm from the dislocation core, producing CSV files of angle versus normalised signal.

## Reproduction target
Run the micromagnetic energy minimization to obtain the equilibrium spin angles on a 2D hexagonal lattice containing an edge dislocation. Using the computed equilibrium configuration, generate two CSV files: (i) `line_circle_7nm.csv` containing the normalised magnetic signal along a circular path of radius 7 nm, sampled at regular angular increments; (ii) `line_circle_3p5nm.csv` for a radius of 3.5 nm, with the same structure. The signal must exhibit a smooth angular variation, and its extrema must be captured as a function of the angular coordinate.

## Assets

- SciPy optimization library: scipy
- NumPy: numpy
- Dy hexagonal elastic constants
- Dy exchange constant J
- Basal-plane anisotropy constant K6^6
- Magnetostriction constant λ100
- Edge dislocation stress field formulas
- Burgers vector modulus for edge dislocation
- Tip magnetization direction relative to domain easy axis

## Workflow steps

### Step 1: Micromagnetic energy minimization
- Role: process
- Action: Implement a micromagnetic model on a 2D hexagonal lattice centered on an edge dislocation in a Dy(0001) film. Compute the stress field components at each ionic site using the anisotropic elasticity formulas for a hexagonal crystal, with given elastic constants and Burgers vector. Construct the total free energy per layer as the sum of: basal-plane crystal electric field anisotropy (K6^6 cos(6φ)), magnetoelastic coupling (∑ λ100 σij terms), long-range dipolar interactions, and nearest-neighbor exchange coupling. Add a Zeeman term equivalent to an in-plane magnetic field of approximately 1 kOe. Apply periodic boundary conditions with fixed moment direction at the boundaries. Minimize the free energy with respect to in-plane spin angles using a numerical optimizer (e.g., SciPy). Save the equilibrium spin angles for all lattice sites.
- Evidence: `/app/outputs/equilibrium_angles.npy`

### Step 2: Circular line section at d=7 nm
- Role: scored (load-bearing)
- Action: Using the equilibrium spin configuration, compute the magnetic signal at each site as the projection of the normalized magnetic moment onto a fixed in-plane tip magnetization direction (angle 98° relative to the domain's easy axis). Extract a counterclockwise circular line section at a distance of 7 nm from the dislocation core, sampling evenly in angle (e.g., at 1° increments from 0 to 360°). Normalize the signal such that the far-domain maximum parallel projection corresponds to +1 and antiparallel to -1. Write the result as a CSV file with columns: angle_deg (float), normalized_signal (float).
- Output file: `/app/outputs/line_circle_7nm.csv`
- Format: csv
- Contract: CSV with two columns: angle_deg (float, 0 to 360), normalized_signal (float). Approximately 360 rows.
- Scoring: scored by hidden verifier

### Step 3: Circular line section at d=3.5 nm
- Role: scored (load-bearing)
- Action: Similar to step02_line7nm, extract a counterclockwise circular line section at a distance of 3.5 nm from the dislocation core, using the same tip magnetization projection and normalization. Save as a CSV file with columns: angle_deg (float), normalized_signal (float).
- Output file: `/app/outputs/line_circle_3p5nm.csv`
- Format: csv
- Contract: CSV with two columns: angle_deg (float, 0 to 360), normalized_signal (float). Approximately 360 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/line_circle_7nm.csv`
- `/app/outputs/line_circle_3p5nm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### line_circle_7nm.csv
- path: `/app/outputs/line_circle_7nm.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Circular line section of magnetic signal at 7 nm radius. Checker verifies extremal angle positions within tolerance and smooth angular variation.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `normalized_signal`
  - `columns`:
    - `angle_deg`: float
    - `normalized_signal`: float

### line_circle_3p5nm.csv
- path: `/app/outputs/line_circle_3p5nm.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Circular line section of magnetic signal at 3.5 nm radius. Checker verifies extremal angle positions within tolerance and smooth angular variation.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `normalized_signal`
  - `columns`:
    - `angle_deg`: float
    - `normalized_signal`: float

Notes: Both line sections must be derived from the actual energy minimization, not hardcoded. Scoring uses extremal angle positions (exact_match with tolerance) and smoothness check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "line_circle_7nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "normalized_signal"
        ],
        "columns": {
          "angle_deg": "float",
          "normalized_signal": "float"
        }
      },
      "description": "Circular line section of magnetic signal at 7 nm radius. Checker verifies extremal angle positions within tolerance and smooth angular variation."
    },
    {
      "file": "line_circle_3p5nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "normalized_signal"
        ],
        "columns": {
          "angle_deg": "float",
          "normalized_signal": "float"
        }
      },
      "description": "Circular line section of magnetic signal at 3.5 nm radius. Checker verifies extremal angle positions within tolerance and smooth angular variation."
    }
  ],
  "notes": "Both line sections must be derived from the actual energy minimization, not hardcoded. Scoring uses extremal angle positions (exact_match with tolerance) and smoothness check."
}
```

## How you are scored
A hidden verifier fetches the submitted CSV files and independently evaluates several properties that a correct micromagnetic simulation must satisfy. For each circle, the verifier checks that the signal varies smoothly (no flat regions over angular intervals of 10° within the normalised signal range) and identifies the angular positions of maximum and minimum signal. The reward is determined by how many of these checks pass, with the main weight on the extremal angle positions. The final score is the weighted sum over the two line sections. Note: simply reporting values, including those from the paper, without running the actual minimization will not produce an artifact that passes these structural checks.
