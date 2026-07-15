# MD Simulation of Gold Clusters: Identifying Energetic and Structural Magic Sizes

## Problem background
Gold clusters display size-dependent structural and energetic properties, with certain sizes exhibiting enhanced stability — commonly called magic numbers. This task investigates the stable structures and stability trends of gold clusters Au_n for n=2–43 using classical molecular dynamics. By computing the total energies of optimized configurations for each size, one can derive energetic stability functions and structural indicators such as density coefficients to identify which cluster sizes are especially stable and which are close-packed. The aim is to reproduce the computational procedure that generates optimized cluster geometries and energies, and to extract the stability signals that reveal magic-number behaviour.

## Approach
The method employs a rearrangement-collision molecular dynamics (MD) protocol with an empirical effective pair potential. The potential is

$$V(r)=D_{21}\frac{A_1}{r^{\lambda_1}} \mathrm{e}^{-\alpha_1 r^2}+D_{22}\frac{A_2}{r^{\lambda_2}} \mathrm{e}^{-\alpha_2 r^2}$$

with parameters A1=345.923364, A2=-38.9245908, λ1=1.04289230, λ2=1.05974062, α1=0.750775065, α2=0.229377368, D21=0.888911352, D22=0.254280292 (distances in Å, energy in eV).

Starting from the dimer, each new cluster is built by colliding a single gold atom at low kinetic energy with the previously optimized cluster, allowing the system to relax, and then minimizing the energy to 0 K to obtain a low-energy structure. This is repeated up to Au44, recording the total energy (eV) and atomic coordinates (Å) for each size.

After obtaining the complete set of structures and energies, energetic stability is probed by computing the second finite difference of the total energy, Δ₂E(n)=E(n+1)+E(n-1)-2E(n); peaks in Δ₂E correspond to particularly stable (magic) clusters. Structural close-packing is assessed via the density coefficient σ(n)=n/r_n³, where r_n is the maximum distance from the cluster centre of mass; minima in its second finite difference indicate sizes that are especially dense. Radial and pair-distance distributions as functions of cluster size provide additional structural insight.

## Reproduction target
Produce a single extended XYZ file `gold_clusters_structures.xyz` that contains the optimized structures and total energies for Au₂ through Au₄₄ in order of increasing number of atoms. From this file, compute:

- the second finite difference of total energy Δ₂E(n) for n=3–43, and identify its peaks as magic-number candidates;
- the cluster radius r_n (maximum distance from the centre of mass), the density coefficient σ(n)=n/r_n³, and its second finite difference, identifying minima as close-packed size candidates;
- the general trends of cluster radius and pair distances as a function of size.

The sets of magic numbers and close-packed sizes derived from your data will be compared to a hidden reference; the consistency of the radial and pair-distance trends will also be evaluated.

## Assets

- Molecular dynamics simulation engine: ase or lammps

## Workflow steps

### Step 1: MD simulation and structure optimization
- Role: scored (load-bearing)
- Action: Implement the rearrangement-collision MD procedure using the empirical pair potential (Eq. 1) with the provided parameters. Starting from a dimer, sequentially add atoms via low-energy collision, relax, and minimize to obtain putative stable structures for Au2 through Au44. Record optimized atomic coordinates (Angstroms) and total energies (eV) for each cluster size.
- Output file: `/app/outputs/gold_clusters_structures.xyz`
- Format: other
- Contract: Extended XYZ: each frame begins with number of atoms N, comment line 'energy=<value_in_eV>' (total energy of cluster), then N lines 'Au x y z' in angstroms. Frames in order n=2,3,...,44.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gold_clusters_structures.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gold_clusters_structures.xyz
- path: `/app/outputs/gold_clusters_structures.xyz`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: Raw optimized structures and total energies used by the checker to recompute energetic and structural stability functions (second finite differences) and identify magic numbers and close-packed sizes.
- schema:
  - `type`: other
  - `format_description`: Extended XYZ file: each frame starts with atom count N, then a comment line 'energy=<value_in_eV>', then N lines each with atom type 'Au' and x,y,z coordinates in angstroms. The file contains 43 frames in order for n=2 to 44.

Notes: The checker will parse this file, extract per-cluster total energy and atomic coordinates, compute the second finite difference of total energy Δ₂E(n) and identify peaks (magic numbers), compute cluster radii r_n, density coefficients σ(n)=n/r_n³, their second finite differences, and identify minima (close-packed sizes). Results will be compared to paper-reported magic numbers [7,13,19,23,26,29,34,37,40,43] and close-packed sizes [4,6,13,23,26,29,34] within ±1 tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gold_clusters_structures.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "other",
        "format_description": "Extended XYZ file: each frame starts with atom count N, then a comment line 'energy=<value_in_eV>', then N lines each with atom type 'Au' and x,y,z coordinates in angstroms. The file contains 43 frames in order for n=2 to 44."
      },
      "description": "Raw optimized structures and total energies used by the checker to recompute energetic and structural stability functions (second finite differences) and identify magic numbers and close-packed sizes."
    }
  ],
  "notes": "The checker will parse this file, extract per-cluster total energy and atomic coordinates, compute the second finite difference of total energy Δ₂E(n) and identify peaks (magic numbers), compute cluster radii r_n, density coefficients σ(n)=n/r_n³, their second finite differences, and identify minima (close-packed sizes). Results will be compared to paper-reported magic numbers [7,13,19,23,26,29,34,37,40,43] and close-packed sizes [4,6,13,23,26,29,34] within ±1 tolerance."
}
```

## How you are scored
A hidden verifier will read your `gold_clusters_structures.xyz` file and independently recompute the stability analyses described above. It will locate peaks in Δ₂E(n) and minima in Δ₂σ(n), matching them to the paper's reported magic numbers and close-packed sizes within pre-set tolerances. It will also assess the qualitative trends of the cluster radius and pair-distance distributions. The final reward is a weighted combination of the number of correctly identified magic sizes, the number of correctly identified close-packed sizes, and the fidelity of the structural trends. You are not required to match the exact energy values or to reproduce any figure from the literature; only the derived magic-number and close-packed sets and the overall structural behaviour matter. Reporting a table of claimed magic numbers is not sufficient — the verifier recomputes everything from your raw XYZ data.
