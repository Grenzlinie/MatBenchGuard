# MD simulation of strain-induced pseudomagnetic fields in supported graphene

## Problem background
Graphene deposited on a nanostructured substrate experiences nonuniform strain that can generate a pseudomagnetic field affecting its electronic behavior. This task investigates this effect for a step-shaped substrate using atomic-scale molecular dynamics simulations. The goal is to compute the y-averaged pseudomagnetic field profile B_avg(x) that arises when a graphene sheet is placed over a 1 nm tall step, following the approach described below.

## Approach
The workflow consists of two major stages: first, molecular dynamics (MD) simulations are performed to obtain equilibrium atomic configurations of graphene on a flat substrate (reference) and on a step substrate (height h0 = 1 nm, defined by a Heaviside step function). The simulations model carbon–carbon interactions with the second-generation Brenner bond-order potential and graphene–substrate adhesion with a Lennard-Jones (LJ) potential. The LJ parameters for carbon and the substrate are combined using standard mixing rules. The simulation is run at 300 K with armchair-oriented graphene of dimensions roughly 19.2 nm × 19.7 nm and supported longitudinal boundary conditions. After equilibration, the equilibrium atomic coordinates are saved for both configurations.

Second, the two atomic configurations are compared to compute the displacement field, from which the strain tensor u_{αβ} (including out-of-plane displacements) is obtained. The strain tensor is then used to calculate the strain-induced gauge field A = (2βħ/(3a₀e))(u_{xx} - u_{yy}, -2u_{xy}), using β = 2.5 and the carbon bond length a₀ = 1.42 Å. The pseudomagnetic field B is obtained by numerical differentiation: B = ∂_y A_x - ∂_x A_y. Finally, B is averaged over the y-direction using 60 equally spaced bins along x to yield the one-dimensional profile B_avg(x). The result is written to a CSV file.

## Reproduction target
The scored artifact is the file `/app/outputs/step_Bavg.csv`. This CSV must contain the y-averaged pseudomagnetic field B_avg for the step substrate case. It should have two columns with header `x (nm),B_avg (T)`. The x-coordinate ranges from approximately -9.5 nm to 9.5 nm with about 60 equally spaced bins covering the graphene sheet. B_avg is the pseudomagnetic field in tesla averaged across the y-direction within each x-bin. The profile should be computed from the full MD + strain-analysis pipeline described above.

## Assets

- LAMMPS: https://lammps.sandia.gov/download.html

## Workflow steps

### Step 1: MD simulations for reference and step configurations
- Role: process
- Action: Set up and run molecular dynamics simulations using LAMMPS to obtain equilibrium atomic configurations of graphene on a flat substrate (reference) and on a step substrate (height h0=1 nm). Use armchair orientation, sheet dimensions 19.17 nm x 19.67 nm, second-generation Brenner potential for C–C interactions, and Lennard-Jones potential for graphene–substrate adhesion (σ_C=3.369 Å, ε_C=2.63 meV, σ=3.5 Å, ε=10.0 meV, mixing rules). Simulations at T=300 K with supported longitudinal boundary conditions.
- Evidence: `/app/outputs/md_configurations.txt`

### Step 2: Compute y-averaged pseudomagnetic field B_avg(x)
- Role: scored (load-bearing)
- Action: From the two atomic configurations, compute the displacement field, strain tensor u_αβ including out-of-plane contributions, gauge field A = (2βħ/(3a0 e))(u_xx-u_yy, -2u_xy) with β=2.5, a0=1.42 Å, and pseudomagnetic field B = ∂_y A_x - ∂_x A_y by numerical differencing. Average B over the y-direction using a histogram of 60 equal bins along x. Output the result as a CSV file.
- Output file: `/app/outputs/step_Bavg.csv`
- Format: csv
- Contract: Two-column CSV with header 'x (nm),B_avg (T)'. x runs from approximately -9.5 nm to 9.5 nm with about 60 equally spaced bins. B_avg is the y-averaged pseudomagnetic field in tesla.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_Bavg.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_Bavg.csv
- path: `/app/outputs/step_Bavg.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: y-averaged pseudomagnetic field profile for graphene on a step substrate. The curve is compared to a hidden reference to verify the MD simulation and strain analysis pipeline.
- schema:
  - `type`: table
  - `required_columns`: `x (nm)`, `B_avg (T)`

Notes: Only the step substrate case is scored. The checker compares the B_avg(x) curve to a hidden reference from the paper, using tolerance on peak positions and magnitudes, or overall correlation. The agent must execute the full MD simulation pipeline; the scored artifact cannot be bypassed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_Bavg.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x (nm)",
          "B_avg (T)"
        ]
      },
      "description": "y-averaged pseudomagnetic field profile for graphene on a step substrate. The curve is compared to a hidden reference to verify the MD simulation and strain analysis pipeline."
    }
  ],
  "notes": "Only the step substrate case is scored. The checker compares the B_avg(x) curve to a hidden reference from the paper, using tolerance on peak positions and magnitudes, or overall correlation. The agent must execute the full MD simulation pipeline; the scored artifact cannot be bypassed."
}
```

## How you are scored
A hidden verifier compares your submitted `/app/outputs/step_Bavg.csv` to a reference profile. The comparison checks whether the profile exhibits the expected structural features—in particular, the location and magnitude of the key peaks. Tolerances on peak positions and on peak values, as well as overall correlation with the reference, are used to compute a score. Simply reporting approximate numbers or a flat line will not earn credit; the profile must result from faithfully executing the molecular dynamics and post-processing pipeline. In addition, the verifier confirms that the preceding MD simulation step produced the required evidence artifact, and the final reward is a weighted combination of all scored stages.
