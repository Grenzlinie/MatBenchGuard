# Water Clusters on Graphite: Global Minimum Energy Search

## Problem background
Water–graphite interactions underlie technologies from lubrication and corrosion-resistant materials to environmental and astrophysical processes. Understanding how small water clusters adsorb and arrange on graphite at the nanoscale is key to predicting wetting behavior and cluster growth. Computational studies can provide structural and energetic details that are difficult to access experimentally, but they face challenges from finite-size artifacts, incomplete global optimization, and the need to accurately capture both van der Waals dispersion and electrostatic polarization of the graphite substrate. This task reproduces a search for the likely global potential energy minima of (H2O)n clusters on the (0001) surface of graphite, using a physically motivated empirical potential energy surface (PES) that combines a standard water model with an analytic treatment of water–graphite interactions.

## Approach
The PES consists of two parts: the water–water interaction is described by the rigid four‑site TIP4P model (Coulomb plus Lennard‑Jones), and the water–graphite interaction is a sum of a dispersion‑repulsion term and an electrostatic polarization term. The dispersion‑repulsion is obtained by analytically summing Lennard‑Jones oxygen–carbon interactions over the graphite lattice using the Steele method. Polarization is treated with explicit image charges (to represent the metallic in‑plane response) and image dipoles (with a perpendicular polarizability density derived from the graphite dielectric constant). Global optimization is performed with basin‑hopping to locate the lowest‑energy structure of (H2O)n on graphite for n = 1…21. To obtain the binding energy, the same basin‑hopping protocol is applied to free TIP4P water clusters to determine their global minimum energies. From the optimized minima, association energies, binding energies, and per‑molecule energy decompositions are computed, along with the equilibrium monomer orientation (tilt angle and oxygen–surface distance).

## Reproduction target
Produce, for cluster sizes n = 1 through 21, the association energy per water molecule ΔEa/n (kJ/mol) and the binding energy ΔEb (kJ/mol). Also report the per‑molecule contributions of the water–graphite dispersion‑repulsion (V_dr/n) and polarization (V_pol/n). For the monomer (n = 1), determine the equilibrium geometry: the angle (in degrees) between the water C2 symmetry axis and the surface normal, and the distance (in Å) between the oxygen atom and the topmost graphite plane. All results must be derived from the basin‑hopping global minima obtained with the specified TIP4P‑based PES; the free water cluster energies serve as the reference for binding energies.

## Assets

- TIP4P water model parameters
- Graphite lattice and dielectric parameters

## Workflow steps

### Step 1: Implement Water-Graphite PES
- Role: process
- Action: Implement the potential energy surface V = V_ww + V_wg. V_ww: TIP4P water–water pairwise interaction (Coulomb + Lennard-Jones). V_wg: dispersion-repulsion via Steele summation (LJ O–C interactions, parameters ε_CO=0.389 kJ/mol, σ_CO=3.28 Å) and electrostatic polarization via image charges (perfect-conductor limit) and image dipoles (α⊥=0.220 Å).
- Evidence: `/app/outputs/pes_module.py`

### Step 2: Compute Free Water Cluster Minima
- Role: process
- Action: Using only the TIP4P water model (no graphite), perform basin-hopping global optimization to find the global potential energy minimum of (H2O)n clusters for n=1..21. Record the minimum energy E_free_n for each cluster size.
- Evidence: `/app/outputs/free_water_energies.csv`

### Step 3: Global Optimization on Graphite
- Role: process
- Action: Using the full PES from step 1, perform basin-hopping global optimization for graphite-(H2O)n clusters with n=1..21. Store the global minimum structure (atomic coordinates) for each n.
- Evidence: `/app/outputs/graphite_minima_structures.json`

### Step 4: Compute Energies and Output CSV
- Role: scored (load-bearing)
- Action: For each n, from the global minimum structure, compute: total potential energy V, dispersion-repulsion V_dr, polarization V_pol. Derive association energy ΔEa = -V (reference: isolated graphite + n isolated water molecules). Compute binding energy ΔEb = ΔEa - E_free_n. Report per water molecule: ΔEa/n, ΔEb, V_dr/n, V_pol/n. Write to global_minimum_energies.csv with columns: n, association_energy_kJ_per_mol, binding_energy_kJ_per_mol, V_dr_kJ_per_mol, V_pol_kJ_per_mol.
- Output file: `/app/outputs/global_minimum_energies.csv`
- Format: csv
- Contract: Columns: n (integer), association_energy_kJ_per_mol (float), binding_energy_kJ_per_mol (float), V_dr_kJ_per_mol (float), V_pol_kJ_per_mol (float).
- Scoring: scored by hidden verifier

### Step 5: Compute Monomer Orientation
- Role: scored
- Action: From the n=1 global minimum structure, compute the angle between the water C2 symmetry axis and the surface normal (z-axis) in degrees, and the distance between the oxygen atom and the topmost graphite surface plane in Å. Write to monomer_orientation.txt with line 1: 'angle_C2_to_z = <value>', line 2: 'O_distance = <value>'.
- Output file: `/app/outputs/monomer_orientation.txt`
- Format: txt
- Contract: Line 1: 'angle_C2_to_z = <value in degrees>'. Line 2: 'O_distance = <value in Angstroms>'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/global_minimum_energies.csv`
- `/app/outputs/monomer_orientation.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### global_minimum_energies.csv
- path: `/app/outputs/global_minimum_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Per-water-molecule association energy, binding energy, and their components for each cluster size n=1..21.
- schema:
  - `type`: table
  - `required_columns`: `n`, `association_energy_kJ_per_mol`, `binding_energy_kJ_per_mol`, `V_dr_kJ_per_mol`, `V_pol_kJ_per_mol`
  - `units`:
    - `association_energy_kJ_per_mol`: kJ/mol
    - `binding_energy_kJ_per_mol`: kJ/mol
    - `V_dr_kJ_per_mol`: kJ/mol
    - `V_pol_kJ_per_mol`: kJ/mol

### monomer_orientation.txt
- path: `/app/outputs/monomer_orientation.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Two lines giving the angle between water C2 axis and surface normal, and the oxygen-surface distance.
- schema:
  - `type`: text
  - `required_lines`: `angle_C2_to_z = <float>`, `O_distance = <float>`

Notes: The scored artifacts are derived from the global minima obtained via basin-hopping; the checker compares the agent's computed values to the paper's hidden reference values within acceptable tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "global_minimum_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "association_energy_kJ_per_mol",
          "binding_energy_kJ_per_mol",
          "V_dr_kJ_per_mol",
          "V_pol_kJ_per_mol"
        ],
        "units": {
          "association_energy_kJ_per_mol": "kJ/mol",
          "binding_energy_kJ_per_mol": "kJ/mol",
          "V_dr_kJ_per_mol": "kJ/mol",
          "V_pol_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Per-water-molecule association energy, binding energy, and their components for each cluster size n=1..21."
    },
    {
      "file": "monomer_orientation.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required_lines": [
          "angle_C2_to_z = <float>",
          "O_distance = <float>"
        ]
      },
      "description": "Two lines giving the angle between water C2 axis and surface normal, and the oxygen-surface distance."
    }
  ],
  "notes": "The scored artifacts are derived from the global minima obtained via basin-hopping; the checker compares the agent's computed values to the paper's hidden reference values within acceptable tolerances."
}
```

## How you are scored
A hidden verifier independently examines each scored artifact. For global_minimum_energies.csv it reads the reported per‑water energies and compares them to reference values; for monomer_orientation.txt it compares the angle and distance to reference quantities. The comparison uses tolerances that account for legitimate numerical differences from basin‑hopping convergence and independent implementations. Each artifact carries a fraction of the total reward, and the scores are combined into a final score between 0 and 1. Simply reporting numbers from the literature is not sufficient — the artifacts must be genuine computational results from the required workflow.
