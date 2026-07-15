# Ledge excess energy and cluster energy for Si(111) surface from atomistic simulations

## Problem background
Two-dimensional nucleation on the Si(111) surface is strongly influenced by the energetics of atomic-height ledges and the long-range interactions between them. Ledge excess energies depend on ledge orientation and spacing, and they in turn control the free-energy barrier for cluster formation. Reproducing the key ledge energies from atomistic static simulations therefore provides critical input for models of crystal growth and surface processing. In this task, you will compute the excess energies of single-height ⟨2-1-1⟩ ledges on Si(111) as a function of spacing, their large-spacing limiting values, and the excess energy of triangular clusters bounded by these ledges, all using a semi-empirical potential energy function.

## Approach
All simulations employ the Mie (12-6) two-body potential combined with the Axilrod–Teller three-body triple-dipole term. The parameter set for silicon is taken from a prior publication (see Assets). The atomic configurations consist of a slab with seven puckered (111) layers; the bottom three layers are held fixed during static energy minimization, while atoms in the upper four layers are fully relaxed.

Two geometrical setups are studied:
1. **Strip ledges** – periodic slabs containing pairs of ledges of a given type ([2-1-1] upper/lower, [211] upper/lower). Configurations are built at a series of ledge spacings d_T. For each relaxed configuration, the ledge excess energy per unit length γ_ℓ is extracted by subtracting out the bulk cohesive energy and the flat-surface free energy, with the cell divided symmetrically to isolate the contribution of each ledge. The energies are extrapolated to large spacing to obtain the converged value. The directional average ledge energy is also obtained as the mean of the upper and lower values for the same direction.
2. **Triangular clusters** – equilateral triangular clusters bounded exclusively by [2-1-1]U ledges are constructed, with the three corner atoms removed to ensure uniform ledge character. Periodic boundary conditions are applied only to the lower substrate layers, effectively simulating isolated clusters. Clusters of various sizes N_c are relaxed, and the excess energy per cluster atom ΔE_ex and the effective ledge energy γ_ℓ (computed from the total ledge length 3·d_T) are evaluated. The converged large-cluster ledge energy is determined from the size trend.

The inputs required are the bulk cohesive energy per atom (Φ_B = -5.469 eV) and the surface free energy of the flat (111) surface (γ_f = 1019 erg/cm²). All other quantities – total energies, atom numbers, surface areas, and ledge lengths – come from the simulations. You will implement the potential, generate the atomic coordinates, run the static relaxations, and post-process the energies as described.

## Reproduction target
Compute and write the following two files.

**strip_ledge_energies.csv**  
- ledge_type: one of [2-1-1]_U, [2-1-1]_L, [211]_U, [211]_L, [2-1-1]_avg, [211]_avg.  
- gamma_large_spacing: the extrapolated large‑spacing ledge excess energy in eV/Å.

**triangular_cluster_energies.csv**  
- N_c: cluster size (integer number of atoms); use -1 for the row that reports the converged large‑cluster ledge energy.  
- Delta_E_ex: excess energy per cluster atom in eV/atom.  
- total_ledge_length: total perimeter of the cluster (3·d_T) in Å.  
- gamma_l: the effective ledge energy γ_ℓ in eV/Å.

The CSV files must contain the columns exactly as specified; numeric formatting is your choice but must be parseable as floats.

## Assets

- Mie + Axilrod-Teller potential parameters for Si (Takai et al. 1985): 10.1016/0039-6028(85)90706-X

## Workflow steps

### Step 1: Generate strip ledge configurations
- Role: process
- Action: Construct atomic coordinates for strip geometries on the Si(111) surface with periodic boundary conditions. Create configurations for each of the four ledge types ([2-1-1]_U, [2-1-1]_L, [211]_U, [211]_L) at a series of ledge spacings d_T. The simulation cell includes seven puckered layers with the bottom three layers held rigid.
- Evidence: none

### Step 2: Relax strip ledge systems
- Role: process
- Action: Perform static energy minimization for each strip configuration using the Mie + Axilrod–Teller potential. The relaxation allows atoms in the upper four layers to move while the bottom three layers remain fixed. Obtain the total potential energy E_T for each simulation.
- Evidence: `/app/outputs/strip_relaxation.log`

### Step 3: Compute strip ledge excess energies
- Role: scored (load-bearing)
- Action: Using the relaxed total energies, atom counts, surface areas, and the given bulk cohesive energy (Phi_B = -5.469 eV) and surface free energy (gamma_f = 1019 erg/cm^2), compute the ledge excess energy per unit length gamma_l for each ledge type as a function of spacing d_T. Extrapolate to large spacing to obtain the converged values. Also compute the average ledge excess energies for the [2-1-1] and [211] directions.
- Output file: `/app/outputs/strip_ledge_energies.csv`
- Format: csv
- Contract: Columns: ledge_type (string: [2-1-1]_U, [2-1-1]_L, [211]_U, [211]_L, [2-1-1]_avg, [211]_avg), gamma_large_spacing (float, eV/Å)
- Scoring: scored by hidden verifier

### Step 4: Generate triangular cluster configurations
- Role: process
- Action: Construct atomic configurations for equilateral triangular clusters bounded by [2-1-1]U ledges on Si(111). Remove corner atoms as described in the paper. Generate clusters of varying sizes (N_c atoms) with periodic boundary conditions applied only to the lower layers, simulating infinite cluster separation.
- Evidence: none

### Step 5: Relax triangular clusters
- Role: process
- Action: Perform static energy minimization for each triangular cluster configuration using the same potential and relaxation protocol as for the strips. Obtain the total potential energy E_T for each cluster.
- Evidence: `/app/outputs/triangular_relaxation.log`

### Step 6: Compute triangular cluster excess energies
- Role: scored (load-bearing)
- Action: From the relaxed total energies, compute the excess energy per cluster atom (ΔE_ex) and the ledge energy (γ_l) as a function of cluster size (N_c) and total ledge length (3 d_T). Determine the converged ledge energy for large clusters.
- Output file: `/app/outputs/triangular_cluster_energies.csv`
- Format: csv
- Contract: Columns: N_c (int, use -1 for the converged value row), Delta_E_ex (float, eV/atom), total_ledge_length (float, Å), gamma_l (float, eV/Å)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strip_ledge_energies.csv`
- `/app/outputs/triangular_cluster_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strip_ledge_energies.csv
- path: `/app/outputs/strip_ledge_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Large-spacing ledge excess energies for the four ledge types and their directional averages.
- schema:
  - `type`: table
  - `required_columns`: `ledge_type`, `gamma_large_spacing`
  - `units`:
    - `gamma_large_spacing`: eV/Å

### triangular_cluster_energies.csv
- path: `/app/outputs/triangular_cluster_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Excess energy per atom and ledge energy for triangular clusters of various sizes, with a converged row (N_c = -1).
- schema:
  - `type`: table
  - `required_columns`: `N_c`, `Delta_E_ex`, `total_ledge_length`, `gamma_l`
  - `units`:
    - `Delta_E_ex`: eV/atom
    - `total_ledge_length`: Å
    - `gamma_l`: eV/Å

Notes: The task reproduces the atomistic static relaxation simulations and energy analysis for the Si(111) surface ledge systems using a semi-empirical potential.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strip_ledge_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ledge_type",
          "gamma_large_spacing"
        ],
        "units": {
          "gamma_large_spacing": "eV/Å"
        }
      },
      "description": "Large-spacing ledge excess energies for the four ledge types and their directional averages."
    },
    {
      "file": "triangular_cluster_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N_c",
          "Delta_E_ex",
          "total_ledge_length",
          "gamma_l"
        ],
        "units": {
          "Delta_E_ex": "eV/atom",
          "total_ledge_length": "Å",
          "gamma_l": "eV/Å"
        }
      },
      "description": "Excess energy per atom and ledge energy for triangular clusters of various sizes, with a converged row (N_c = -1)."
    }
  ],
  "notes": "The task reproduces the atomistic static relaxation simulations and energy analysis for the Si(111) surface ledge systems using a semi-empirical potential."
}
```

## How you are scored
A hidden verifier will read your two CSV files and compare the numerical values against reference results derived from the original study. Each scored artifact is evaluated independently: the verifier checks that the reported large‑spacing ledge energies and the triangular cluster energies fall within allowed tolerances. The final score is a weighted average of the per-artifact scores (range 0–1). The verifier does not inspect your relaxation logs or intermediate outputs; only the final CSV files count. To obtain a high score you must faithfully implement the potential, relaxation protocol, and energy analysis described in the workflow; simply writing plausible numbers without running the simulations is unlikely to meet the required accuracy.
