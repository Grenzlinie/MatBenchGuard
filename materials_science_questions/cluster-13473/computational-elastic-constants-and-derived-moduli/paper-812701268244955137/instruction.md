# Stability-Dependent Local Elastic Heterogeneity in a Polydisperse Glass Former

## Problem background
Amorphous solids display heterogeneous local elasticity that is thought to influence their anomalous vibrational and thermal properties. The spatial variation of elastic constants can depend on the stability of the glass, which is controlled by the temperature from which the glass is prepared (the parent temperature). This task reproduces computational measurements of local shear and bulk moduli in a model polydisperse glass former. The objective is to compute the distributions of local elastic moduli for several coarse-graining box sizes and a range of parent temperatures, and to examine the dependence of the widths of these distributions on the parent temperature, as well as the spatial correlations among the local moduli. Understanding this behavior sheds light on the origin of sound attenuation and the boson peak in glasses.

## Approach
The investigation is performed with classical molecular dynamics (MD) on a system of polydisperse repulsive particles interacting via a truncated and tapered power-law potential (eqn (1)–(3) from the paper). The protocol involves three main stages:

1. **Preparation of equilibrium configurations**: starting from a random packing of 48 000 particles at number density ρ = 1, configurations are equilibrated at several parent temperatures T<sub>p</sub> ∈ {0.062, 0.085, 0.200} using swap Monte Carlo (an advanced Monte Carlo method that combines conventional translational moves with particle-swap moves to accelerate equilibration in deeply supercooled liquids).

2. **Quenching and low-temperature production**: each equilibrated configuration is quenched to its zero-temperature inherent structure via conjugate-gradient minimization. Subsequently, a long NVT MD simulation is run at a very low temperature (T = 10<sup>−5</sup> ε/k<sub>B</sub>) to sample the energy landscape. Particle positions, forces, and the system stress are recorded at closely spaced time intervals.

3. **Local elastic modulus analysis**: at each saved MD snapshot, the simulation box is subdivided into cubic cells (coarse-graining boxes) of sizes w = 12.114, 6.057, 4.543, and 3.303. For each cell, the fully-local stress tensor is computed using the bond-length-weighted line-sharing scheme, and from it the four-rank local elastic constant tensor C<sub>αβγδ</sub> is evaluated. The local moduli are obtained from the affine (Born + stress + kinetic) and the non-affine (fluctuation) contributions, yielding five shear moduli G<sub>1</sub>…G<sub>5</sub> and the bulk modulus K per cell per snapshot. Global moduli obtained by deforming the system at zero temperature are also computed to validate that the averages of the local moduli equal the global response.

The raw per-cell moduli are collected over all snapshots and all parent temperatures.

## Reproduction target
Produce a CSV file `local_moduli_raw.csv` that contains the local shear and bulk moduli for every coarse-graining box and every analyzed snapshot, covering all four box sizes and the three parent temperatures. The file must have the columns: snapshot (int), w (float), box_id (int), center_x (float), center_y (float), center_z (float), G1, G2, G3, G4, G5, and K (all float). A hidden verifier will use this CSV to compute the standard deviations of the local shear and bulk moduli for each parent temperature and box size, and to compute the nearest-neighbor correlation parameters of the moduli. The verifier checks whether your data exhibits the physically expected dependence on the parent temperature (which controls the glass stability) and whether the spatial correlations are consistent with the known behavior of the polydisperse glass former. You do not need to perform the statistical analysis yourself; only the raw moduli CSV is required.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.org
- Polydisperse repulsive pair potential

## Workflow steps

### Step 1: Generate initial configuration
- Role: process
- Action: Create an initial configuration of N=48000 polydisperse particles with the specified size distribution (P(σ) ∝ 1/σ³, σ∈[0.73,1.63]) and number density ρ=1 in a cubic box with periodic boundaries.
- Evidence: none

### Step 2: Equilibrate at parent temperatures
- Role: process
- Action: Equilibrate the initial configuration at each parent temperature Tp ∈ {0.062, 0.085, 0.200} using swap Monte Carlo to obtain well-equilibrated liquid/glass configurations.
- Evidence: none

### Step 3: Quench to inherent structures
- Role: process
- Action: Quench each equilibrated configuration to its zero-temperature inherent structure via conjugate gradient minimization.
- Evidence: none

### Step 4: Low-temperature NVT MD production
- Role: process
- Action: Run a low-temperature NVT MD simulation (T = 10⁻⁵ ε/k_B) on each inherent structure using a timestep dt=0.02 for a production length of at least 1.5e7 steps. Record particle positions, forces, and stresses over time.
- Evidence: none

### Step 5: Compute local elastic moduli and export raw CSV
- Role: scored (load-bearing)
- Action: From the MD trajectories, for each snapshot and for each coarse-graining box of sizes w = {12.114, 6.057, 4.543, 3.303}, compute the five local shear moduli (G1..G5) and the local bulk modulus K using the fully‑local stress and elastic‑constant expressions (Born and fluctuation contributions). Write a CSV file with one row per box per snapshot, including snapshot index, box size, parent temperature, box center coordinates, and the computed moduli.
- Output file: `/app/outputs/local_moduli_raw.csv`
- Format: csv
- Contract: CSV with columns: snapshot (int), w (float), Tp (float), box_id (int), center_x (float), center_y (float), center_z (float), G1 (float), G2 (float), G3 (float), G4 (float), G5 (float), K (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/local_moduli_raw.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### local_moduli_raw.csv
- path: `/app/outputs/local_moduli_raw.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw local moduli per coarse-graining box and snapshot for all parent temperatures and box sizes. The checker will group by Tp and box size, compute standard deviations of the local moduli and nearest-neighbor correlation parameters, and verify monotonic trends and low correlation.
- schema:
  - `type`: table
  - `required_columns`: `snapshot`, `w`, `Tp`, `box_id`, `center_x`, `center_y`, `center_z`, `G1`, `G2`, `G3`, `G4`, `G5`, `K`
  - `description`: Per-box per-snapshot local shear (five components) and bulk moduli, with parent temperature.

Notes: The scorer performs a structural audit: standard deviation of local moduli should decrease with decreasing parent temperature, and nearest-neighbor correlation parameters should be small (|Ψ| < 0.1).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "local_moduli_raw.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "snapshot",
          "w",
          "Tp",
          "box_id",
          "center_x",
          "center_y",
          "center_z",
          "G1",
          "G2",
          "G3",
          "G4",
          "G5",
          "K"
        ],
        "description": "Per-box per-snapshot local shear (five components) and bulk moduli, with parent temperature."
      },
      "description": "Raw local moduli per coarse-graining box and snapshot for all parent temperatures and box sizes. The checker will group by Tp and box size, compute standard deviations of the local moduli and nearest-neighbor correlation parameters, and verify monotonic trends and low correlation."
    }
  ],
  "notes": "The scorer performs a structural audit: standard deviation of local moduli should decrease with decreasing parent temperature, and nearest-neighbor correlation parameters should be small (|Ψ| < 0.1)."
}
```

## How you are scored
Your submission is scored by a hidden verifier that runs after your agent finishes. The verifier reads your `local_moduli_raw.csv`, groups the data by parent temperature and box size, and computes summary statistics (standard deviations of the five shear moduli and of the bulk modulus, and the nearest-neighbor correlation parameters Ψ<sub>G</sub> and Ψ<sub>K</sub>). The scores are assigned based on how well the trends in these statistics match the physical predictions for the model: the change in standard deviation with decreasing parent temperature, the relative magnitude of the correlations, and the consistency of the global moduli averages with values obtained from deformation simulations (if provided as supporting evidence). Each scored workflow step contributes a weight to the overall reward. The verifier does not compare your numbers to any single “correct” value; instead it evaluates whether your data follows the correct physical trends. No gold values are revealed, and the scoring is designed to reward honest computational reproduction of the described protocol.
