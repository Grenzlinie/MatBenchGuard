# C60 Nanocluster Adsorption and Diffusion

## Problem background
Clusters of C60 molecules can adopt different structural motifs—truncated octahedra, icosahedra, and truncated decahedra—whose growth and stability are influenced by the adsorption of additional molecules and the ease with which they diffuse across the surface. Understanding the adsorption energetics and the energy barriers for the elementary diffusion steps is crucial for explaining kinetic trapping and solid–solid transformations observed in these systems. This task computes the adsorption energies of single C60 molecules on the facets of three representative nanoclusters and the energy barriers for the main diffusion processes, providing a map of sites and pathways that control the cluster’s morphological evolution.

## Approach
The interaction between C60 molecules is described by the Girifalco pair potential, which treats each molecule as a sphere with a uniform distribution of Lennard-Jones sites. The adsorption energetics are obtained by placing an extra molecule at each distinct surface site and performing quenched molecular dynamics minimizations; adsorption energies are reported relative to the most favourable site on each cluster. Energy barriers for diffusion are calculated using the nudged elastic band (NEB) method. The clusters studied are a truncated octahedron of 38 molecules (TO₃₈), an icosahedron of 55 molecules (Ih₅₅), and a truncated Marks decahedron of 75 molecules (Dh₇₅). Their geometries are constructed from known crystallographic descriptions. The workflow first sets up the potential and the cluster coordinates, then computes site‑resolved adsorption energies, and finally computes energy barriers for intrafacet jumps, interfacet jumps, and exchange processes.

## Reproduction target
Produce two tables. First, compute the adsorption energy for every distinct adsorption site on the three clusters, each cluster’s energies being expressed relative to its own most stable site. Second, compute the minimum‑energy barriers for the listed diffusion processes (intrafacet jumps on (111) facets, interfacet jumps between (111)/(111), (111)/(100), (111)/reentrance, and exchange processes). The computed energies and barriers should be physically consistent with a simple nearest‑neighbour bond‑counting picture: sites with higher coordination should be more favourable, intrafacet barriers should be a fraction of a single‑bond energy, and exchange processes should be high compared to jumps. The quantitative results are the reported energies and barriers themselves; they will be checked against the original paper’s reference values.

## Assets

- LAMMPS: https://lammps.sandia.gov

## Workflow steps

### Step 1: Model and cluster preparation
- Role: process
- Action: Implement the Girifalco pair potential (functional form and parameters) and construct atomic coordinates for the three clusters: truncated octahedron of 38 molecules (TO38), icosahedron of 55 molecules (Ih55), truncated decahedron of 75 molecules (Dh75).
- Evidence: `/app/outputs/cluster_geometries.xyz`

### Step 2: Compute adsorption energies
- Role: scored (load-bearing)
- Action: Identify all distinct adsorption sites on each cluster (e.g., (100) facet, (111) fcc and hcp sites), place an ad-molecule at each site, perform quenched molecular dynamics minimizations to obtain adsorption energies relative to the most favourable site within each cluster. Output a CSV with columns: cluster, facet, site, energy_eV.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: CSV with columns: cluster (string), facet (string), site (string), energy_eV (float, eV, relative to most stable site per cluster).
- Scoring: scored by hidden verifier

### Step 3: Compute diffusion barriers
- Role: scored
- Action: For listed diffusion processes (intrafacet jumps on (111) facets, interfacet jumps between (111)/(111), (111)/(100), (111)/reentrance, and exchange processes), perform nudged elastic band (NEB) calculations to obtain energy barriers. Output a CSV with columns: cluster, process, barrier_eV.
- Output file: `/app/outputs/diffusion_barriers.csv`
- Format: csv
- Contract: CSV with columns: cluster (string), process (string), barrier_eV (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/diffusion_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of all distinct adsorption sites with their computed adsorption energies.
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `facet`, `site`, `energy_eV`
  - `units`:
    - `energy_eV`: eV, relative to most stable site per cluster

### diffusion_barriers.csv
- path: `/app/outputs/diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of energy barriers for the most important diffusion processes.
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `process`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

Notes: The checker compares each row's energy value to hidden reference values from the original paper with an absolute tolerance of ±0.03 eV, and also verifies the relative ordering of site energies within each cluster (e.g., (100) sites more stable than (111) sites).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "facet",
          "site",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV, relative to most stable site per cluster"
        }
      },
      "description": "Table of all distinct adsorption sites with their computed adsorption energies."
    },
    {
      "file": "diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "process",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Table of energy barriers for the most important diffusion processes."
    }
  ],
  "notes": "The checker compares each row's energy value to hidden reference values from the original paper with an absolute tolerance of ±0.03 eV, and also verifies the relative ordering of site energies within each cluster (e.g., (100) sites more stable than (111) sites)."
}
```

## How you are scored
A hidden verifier reads your output files and compares each adsorption energy and each diffusion barrier row to independently determined reference values. Credit is awarded for values that fall within appropriate numerical tolerances; the relative ordering of site energies within each cluster is also verified. The final reward is a weighted combination of the scores from the two output tables. Reporting numbers that are close to the reference, together with the correct qualitative ordering, yields a high score. Merely formatting the files correctly gives virtually no credit.
