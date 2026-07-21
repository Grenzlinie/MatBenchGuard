# Determining Critical Island Size from Kinetic Monte Carlo Simulation of Surface Nucleation

## Problem background
In ultrathin films of para-hexaphenyl (6P) grown on sputter-amorphized mica, a bimodal island size distribution is observed: large dendritic islands form during deposition, while small compact islands appear only after the sample is exposed to air. The small islands arise from adsorbate-induced nucleation of a two-dimensional monomer gas that exists on the surface in vacuum. The critical island size—the minimum number of molecules needed for a stable nucleus—governs the final island density after venting. Determining this critical island size is essential for understanding the nucleation mechanism, and it can be obtained by comparing kinetic Monte Carlo (KMC) simulations of the post-venting nucleation process to experimental atomic force microscopy measurements.

## Approach
Implement a lattice-based KMC simulation to model adsorbate-induced subsequent nucleation. The simulation runs on a square lattice with a fixed monomer coverage taken from the initial random placement of point-like monomers. Monomers diffuse with a hopping rate determined by an attempt frequency, a surface diffusion barrier, and the substrate temperature. The critical island size i is treated as a free parameter; clusters smaller than i can dissociate, while clusters of size i or larger are stable and grow irreversibly. Edge diffusion of attached monomers may be included with a comparable energy barrier or approximated as hit-and-stick (infinitely slow), as its effect on the final island density is marginal. The simulation proceeds until no free monomers remain, and the final island density is recorded. This is repeated for each i in a prescribed integer range. After obtaining densities for all i, the simulated values are compared to the experimental AFM island density of 35.0 µm⁻² (for a coverage of 0.03 ML), and the critical island size that yields the closest match is selected.

## Reproduction target
Produce two scored artifacts. First, run the KMC simulation for each critical island size i from 3 to 8 and write the resulting island densities to island_density_vs_i.json as an array of objects with keys 'critical_island_size' and 'island_density_per_um2'. Second, compare each simulated density to the experimental AFM island density of 35.0 µm⁻² (coverage 0.03 ML), select the i that minimizes the absolute difference (choosing the smallest i in case of a tie), and write that integer to selected_critical_island_size.txt. The goal is a correct determination of the critical island size for adsorbate-induced nucleation on this surface.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: KMC Simulation of Island Density vs Critical Island Size
- Role: scored (load-bearing)
- Action: Implement a kinetic Monte Carlo simulation for adsorbate-induced nucleation on a square lattice of size 1000×1000 with lattice constant 1 nm. Initially place monomers randomly at coverage 0.03 ML. Allow monomers to diffuse with hopping rate h1 = ν exp(-Q/kT) where ν = 1e13 s⁻¹, Q = 0.05 eV, k = 8.617333262145e-5 eV/K, T = 300 K. Use a critical island size i (integer from 3 to 8): islands of size < i can dissociate, while islands of size ≥ i are stable and grow irreversibly. Include edge diffusion with the same energy barrier Q, or effectively infinite for hit-and-stick (the effect on final density is marginal). Run the simulation until no free monomers remain. Record the final number of islands and compute island density in islands/µm². Repeat the simulation for each i from 3 to 8. Write the results as an array of objects to island_density_vs_i.json with keys 'critical_island_size' and 'island_density_per_um2'.
- Output file: `/app/outputs/island_density_vs_i.json`
- Format: json
- Contract: Array of objects: each object has keys 'critical_island_size' (integer 3..8) and 'island_density_per_um2' (float).
- Scoring: scored by hidden verifier

### Step 2: Determine Critical Island Size from Density Comparison
- Role: scored
- Action: From island_density_vs_i.json, read the island densities. Compare each simulated density to the experimental AFM island density of 35.0 µm⁻² (coverage 0.03 ML). Compute the absolute difference. Select the critical island size i that minimizes the difference. If multiple i give equal minimal difference, choose the smallest i. Write the selected integer (3–8) to selected_critical_island_size.txt.
- Output file: `/app/outputs/selected_critical_island_size.txt`
- Format: txt
- Contract: A single integer (3..8) representing the critical island size.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/island_density_vs_i.json`
- `/app/outputs/selected_critical_island_size.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### island_density_vs_i.json
- path: `/app/outputs/island_density_vs_i.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Island densities for each critical island size i, compared against hidden paper reference densities with tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `critical_island_size`, `island_density_per_um2`
    - `properties`:
      - `critical_island_size`:
        - `type`: integer
        - `description`: critical island size, 3..8
      - `island_density_per_um2`:
        - `type`: number
        - `description`: final island density in islands per µm²

### selected_critical_island_size.txt
- path: `/app/outputs/selected_critical_island_size.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The determined critical island size.
- schema:
  - `type`: text
  - `description`: A single integer (3..8) representing the critical island size i that minimizes the difference between simulated and experimental island density.

Notes: The experimental AFM island density is 35.0 µm⁻² (coverage 0.03 ML). The hidden scoring checks both the island density trend (tolerance 25%) and the correctness of the selected critical island size.

## How you are scored
A hidden verifier independently scores both artifacts. The verifier checks that island_density_vs_i.json contains plausible density values for each i, consistent with the trend expected from KMC nucleation theory, and that selected_critical_island_size.txt correctly identifies the i that best matches the experimental reference. The final reward (a number between 0 and 1) combines a high weight for the correctness of the selected critical island size with a lower weight for the consistency of the density‑versus‑i trend. For the trend check, the verifier allows a tolerance of 25% of the maximum density to account for stochastic fluctuations in finite-size simulations. Reproducing the paper's numbers without running the simulation is not sufficient; the checker evaluates the quality of the simulated results and the proper derivation of the chosen i.