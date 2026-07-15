# MD simulation of graphene adhesion on pseudo-random rough iron substrates

## Problem background
Graphene's exceptional mechanical and electronic properties make it a promising material for surface passivation, lubrication, and flexible electronics. When placed on a metal substrate, the quality of the graphene–substrate interface critically depends on the surface roughness of the metal. Atomically thin graphene can partially conform to rough features, resulting in local strain, deformation, and varying adhesion energy. Understanding how the root-mean-square roughness of an iron substrate influences the conformability, adhesion energy, and atomic strain distribution of monolayer graphene is essential for designing graphene-based devices. Molecular dynamics simulations provide a direct way to probe these relationships by modeling realistic rough surfaces and quantifying the resulting graphene state.

## Approach
This task uses molecular dynamics (MD) simulations with the open-source LAMMPS code to study monolayer graphene adhering to pseudo-random rough iron substrates. The iron surfaces are constructed using a multi-scale sub-surface method: a target roughness is built by summing three independent Gaussian sub-surfaces with prescribed characteristic asperity distances and weights, then scaling the combined surface to achieve desired root-mean-square heights (Sq_Fe). Graphene is modeled as a perfect monolayer sheet initially suspended above the substrate. MD simulations use a Finnis-Sinclair potential for Fe-Fe interactions, an AIREBO potential for C-C bonds, and a Lennard-Jones potential for Fe-C interactions. The system is equilibrated at 300 K with periodic boundary conditions, allowing the graphene to adhere to the substrate until the energy stabilizes. Post-processing of the final configurations yields the root-mean-square height of the adhered graphene (Sq_Gr), the adhesion energy per carbon atom (E_ad), and the distribution of per-atom strain. Special attention is given to the extreme strains by computing the mean of the top 10% of per-atom absolute strains (epsilon_mean_top10). The analysis is performed on three substrate roughness values (Sq_Fe = 2 Å, 4 Å, 6 Å) to extract the quantitative dependence of these quantities on substrate roughness and to examine the shape of the strain distribution.

## Reproduction target
For monolayer graphene on pseudo-random rough iron substrates with Sq_Fe = 2, 4, and 6 Å, reproduce the relationship between substrate roughness and the following quantities: (1) the root-mean-square height of the graphene (Sq_Gr, in Å), (2) the adhesion energy (E_ad, in meV per C atom), and (3) the mean of the top 10% per-atom absolute strain (epsilon_mean_top10). Additionally, for the substrate with Sq_Fe = 6 Å, extract the full list of per-atom strains to characterize the tail of the strain distribution. The goal is to determine how these properties scale with Sq_Fe and whether the strain distribution deviates from Gaussian behavior.

## Assets

- LAMMPS: https://lammps.sandia.gov

## Workflow steps

### Step 1: Generate graphene sheet coordinates
- Role: process
- Action: Generate atomic coordinates for a monolayer graphene sheet with dimensions 48.5 nm × 48.5 nm, zigzag direction parallel to the x-axis, using the standard graphene lattice constant.
- Evidence: none

### Step 2: Generate pseudo-random rough iron substrates
- Role: process
- Action: Using the multi-scale sub-surface method: sum three independent Gaussian sub-surfaces generated from control-point grids. Sub-surface weights are k1=0.6 (d1=50 Å), k2=0.3 (d2=25 Å), k3=0.1 (d3=12.5 Å). Apply periodic boundary padding (2, 4, 8 rows for S1, S2, S3). Scale the master template's z-coordinates to obtain three iron substrates (50 nm × 50 nm, bcc lattice) with root-mean-square heights Sq_Fe = 2, 4, and 6 Å. Output the atomic coordinate files for simulation.
- Evidence: none

### Step 3: Run LAMMPS MD adhesion simulations for each substrate
- Role: process
- Action: For each of the three iron substrates (Sq_Fe = 2, 4, 6 Å), set up a LAMMPS simulation with the generated 1L graphene sheet initially suspended above the substrate. Use Finnis-Sinclair potential for Fe-Fe, AIREBO for C-C, Lennard-Jones for Fe-C (ε=0.043 eV, σ=2.221 Å). Apply periodic boundary conditions in x and y, Nosé-Hoover thermostat at 300 K, 1 fs timestep. Equilibrate and allow adhesion until energy stabilizes. Save final trajectories or configurations for post-processing.
- Evidence: none

### Step 4: Compute graphene roughness, adhesion energy, and top-10% strain statistics
- Role: scored
- Action: From the final MD configurations for each substrate, compute the root-mean-square height of the graphene atoms (Sq_Gr, in Å), the adhesion energy E_ad (in meV per C atom, as the difference between total system energy and sum of isolated graphene and substrate energies), and the mean of the top 10% of per-atom absolute strain values (epsilon_mean_top10, dimensionless). Output one row per substrate condition.
- Output file: `/app/outputs/graphene_roughness_data.csv`
- Format: csv
- Contract: Columns: Sq_Fe (float, Å), Sq_Gr (float, Å), E_ad (float, meV/C atom), epsilon_mean_top10 (float).
- Scoring: scored by hidden verifier

### Step 5: Extract per-atom strains for the Sq_Fe=6 Å substrate
- Role: scored (load-bearing)
- Action: From the final MD configuration of the graphene sheet on the iron substrate with Sq_Fe = 6 Å, extract the absolute atomic strain for every carbon atom. Write the list of strain values as a JSON file.
- Output file: `/app/outputs/per_atom_strains_sq6.json`
- Format: json
- Contract: A JSON object with a single key 'strains' whose value is a list of floating-point numbers (per-atom absolute strain).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/graphene_roughness_data.csv`
- `/app/outputs/per_atom_strains_sq6.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### graphene_roughness_data.csv
- path: `/app/outputs/graphene_roughness_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Aggregate statistics for three substrate conditions. Structural audit checks monotonic trends (Sq_Gr increases with Sq_Fe, E_ad decreases, epsilon_mean_top10 increases) and a numeric bound (epsilon_mean_top10 < 0.02 for Sq_Fe=2 Å).
- schema:
  - `type`: table
  - `required_columns`: `Sq_Fe`, `Sq_Gr`, `E_ad`, `epsilon_mean_top10`
  - `units`:
    - `Sq_Fe`: Å
    - `Sq_Gr`: Å
    - `E_ad`: meV/C atom
    - `epsilon_mean_top10`: dimensionless

### per_atom_strains_sq6.json
- path: `/app/outputs/per_atom_strains_sq6.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Per-atom strain list for the Sq_Fe=6 Å condition. Structural audit computes kurtosis of the distribution and verifies it is > 3.
- schema:
  - `type`: object
  - `required`:
    - `strains`: list of float
  - `items`:
    - `strains`: float

Notes: The verification checks structural properties (monotonic trends, threshold, distribution kurtosis) without requiring re-simulation. No hidden gold values are exposed in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "graphene_roughness_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Sq_Fe",
          "Sq_Gr",
          "E_ad",
          "epsilon_mean_top10"
        ],
        "units": {
          "Sq_Fe": "Å",
          "Sq_Gr": "Å",
          "E_ad": "meV/C atom",
          "epsilon_mean_top10": "dimensionless"
        }
      },
      "description": "Aggregate statistics for three substrate conditions. Structural audit checks monotonic trends (Sq_Gr increases with Sq_Fe, E_ad decreases, epsilon_mean_top10 increases) and a numeric bound (epsilon_mean_top10 < 0.02 for Sq_Fe=2 Å)."
    },
    {
      "file": "per_atom_strains_sq6.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "strains": "list of float"
        },
        "items": {
          "strains": "float"
        }
      },
      "description": "Per-atom strain list for the Sq_Fe=6 Å condition. Structural audit computes kurtosis of the distribution and verifies it is > 3."
    }
  ],
  "notes": "The verification checks structural properties (monotonic trends, threshold, distribution kurtosis) without requiring re-simulation. No hidden gold values are exposed in the public contract."
}
```

## How you are scored
A hidden verifier independently scores your two output files. For graphene_roughness_data.csv, the verifier checks that the three quantities (Sq_Gr, E_ad, epsilon_mean_top10) exhibit the correct monotonic trend across the three Sq_Fe values (each must consistently increase, consistently decrease, or remain constant) and that epsilon_mean_top10 for Sq_Fe=2 Å lies below a physical upper bound. For per_atom_strains_sq6.json, the verifier computes the kurtosis of the strain distribution and verifies that it exceeds a threshold consistent with a heavy-tailed, non-Gaussian distribution. The overall reward is a weighted combination of these checks, and no external information is provided to you. Your submitted artifacts must be fully self-contained and placed at the specified output paths.
