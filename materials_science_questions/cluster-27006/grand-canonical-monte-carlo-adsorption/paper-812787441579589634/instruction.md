# Microphase Separation of Confined Binary Liquid Mixture via Molecular Simulation

## Problem background
When a completely miscible binary liquid mixture is confined within a nanoscale pore, the confinement can strongly alter the liquid structure. Recent experiments have suggested that a mixture of tert-butanol (TBA, an amphiphilic alcohol) and toluene (TOL, an apolar aromatic) inside a cylindrical silica nanopore may adopt a core-shell organisation, with one component preferentially adsorbed at the pore wall and the other located in the core. Atomistic simulations using default force-field mixing rules have typically failed to reproduce this separation, raising the question of whether a carefully refined description of the solid-liquid interactions is necessary to capture the phenomenon. This task investigates whether, given improved cross-interaction parameters between silica and toluene, molecular simulations can yield a spatially segregated core-shell structure, and if so, what its quantitative characteristics are.

## Approach
The approach combines Grand Canonical Monte Carlo (GCMC) and Molecular Dynamics (MD) simulations in a cylindrical silica nanopore of radius 12 Å. The silica pore is constructed using the ClayFF force field and the surface is hydroxylated following the Bródka–Zerda procedure. TBA and TOL are modelled with the OPLS-AA force field. To account for the silica–toluene interactions, refined Lennard-Jones parameters (provided in the Assets section) replace the default Lorentz-Berthelot cross terms; all other cross interactions use the standard Lorentz-Berthelot mixing rules. GCMC simulations at 308 K and saturation vapour pressure are first performed to determine the equilibrium numbers of TBA and TOL molecules inside the pore for two target compositions, x_TBA = 0.49 and 0.71. Those loadings are then used as input for constant-NVT MD simulations at 308 K. From the MD trajectories, radial density profiles of the centres of mass of TBA and TOL are computed. The profiles are analysed to identify any local enrichment (shell) and to extract the thickness of the interfacial TBA layer and the number of TBA molecules it contains.

## Reproduction target
Produce a CSV file, `density_profiles.csv`, containing the radial density profiles of TBA and TOL centres of mass as a function of the distance from the pore centre for compositions x_TBA = 0.49 and 0.71. The file must have columns: `composition` (the TBA mole fraction), `radial_distance_angstrom` (distance in Å), `density_TBA`, and `density_TOL` (in any consistent arbitrary units). Additionally, derive from the profile at x_TBA = 0.71 the thickness of the TBA shell, `e_shell_angstrom` (in Å), and the integrated number of TBA molecules inside that shell, `N_TBA_shell`, and write them to a text file `shell_analysis.txt` with one numeric value per line (prefixed by the label shown in the scaffold). These two artifacts constitute the primary deliverables.

## Assets

- OPLS-AA force field parameters for TOL and TBA: Standard in MD packages (LAMMPS, GROMACS, DL_POLY) or from literature (Jorgensen et al., 1996)
- ClayFF force field for silica: From Cygan et al. (2004) or included in MD software packages
- Cross Lennard-Jones parameters between silica and toluene (Table 1): Provided in instruction.md: Si-CH3: σ=3.6475 Å, ε=46.17061 K; Si-CH: σ=3.6725 Å, ε=47.54915 K; Si-C: σ=3.6725 Å, ε=47.54915 K
- Molecular dynamics simulation package (DL_POLY, LAMMPS, or GROMACS): Open source, e.g., LAMMPS (https://www.lammps.org/), GROMACS (https://www.gromacs.org/)

## Workflow steps

### Step 1: Build silica nanopore model
- Role: process
- Action: Construct a cylindrical silica nanopore of radius 12 Å with hydroxylated surface using the ClayFF force field and the procedure of Bródka & Zerda (1996). Remove atoms within a cylinder and saturate non-bridging oxygens with hydrogen to form surface silanol groups (coverage ~7.5 nm⁻²). Output atomic coordinates and topology suitable for GCMC/MD.
- Evidence: `/app/outputs/silica_pore.pdb`

### Step 2: Prepare force field input files
- Role: process
- Action: Combine OPLS-AA parameters for TBA and TOL, ClayFF parameters for silica, and the refined cross LJ parameters (Si-CH3: σ=3.6475 Å, ε=46.17061 K; Si-CH: σ=3.6725 Å, ε=47.54915 K; Si-C: σ=3.6725 Å, ε=47.54915 K) into input files for the chosen MD software. Assign atomic charges (standard OPLS-AA charges) and apply Lorentz-Berthelot mixing rules for other cross interactions.
- Evidence: `/app/outputs/force_field.dat`

### Step 3: GCMC to determine mixture loadings
- Role: process
- Action: Run Grand Canonical Monte Carlo simulations for the TBA/TOL mixture inside the silica pore at 308 K and saturation pressure vapor to determine equilibrium numbers of TBA and TOL molecules for compositions x_TBA=0.49 and x_TBA=0.71. Use configurational-bias moves.
- Evidence: `/app/outputs/gcmc_loadings.txt`

### Step 4: MD simulation of TBA/TOL mixture (x_TBA=0.49)
- Role: process
- Action: Using the molecular counts from step 3 for x_TBA=0.49, perform NVT molecular dynamics at 308 K in the silica nanopore. Equilibrate and sample trajectory (10 ns production).
- Evidence: `/app/outputs/md_x049.log`

### Step 5: MD simulation of TBA/TOL mixture (x_TBA=0.71)
- Role: process
- Action: Using the molecular counts from step 3 for x_TBA=0.71, perform NVT molecular dynamics at 308 K in the silica nanopore. Equilibrate and sample trajectory (10 ns production).
- Evidence: `/app/outputs/md_x071.log`

### Step 6: Compute radial density profiles
- Role: scored (load-bearing)
- Action: From the MD trajectories of steps 4 and 5, calculate radial density profiles of center of mass of TBA and TOL as a function of distance from the pore center. Produce a CSV file with columns: composition (mole fraction TBA), radial_distance_angstrom (Å), density_TBA (arbitrary units), density_TOL (arbitrary units). Include profiles for x_TBA=0.49 and 0.71.
- Output file: `/app/outputs/density_profiles.csv`
- Format: csv
- Contract: Columns: composition (float), radial_distance_angstrom (float), density_TBA (float), density_TOL (float).
- Scoring: scored by hidden verifier

### Step 7: Determine shell thickness and saturation count
- Role: scored
- Action: From the density profile at x_TBA=0.71, identify the shell region (first adsorbed TBA layer) and compute: (a) e_shell, the radial thickness of the TBA shell, and (b) N_TBA,s, the integrated number of TBA molecules in that shell. Output a text file with two lines: e_shell_angstrom = <value>, N_TBA_shell = <value>.
- Output file: `/app/outputs/shell_analysis.txt`
- Format: txt
- Contract: Two lines: e_shell_angstrom (float, Å) and N_TBA_shell (integer).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/density_profiles.csv`
- `/app/outputs/shell_analysis.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### density_profiles.csv
- path: `/app/outputs/density_profiles.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Radial density profiles of TBA and TOL centers of mass, used to verify the core-shell microphase separation pattern (structural ordering and relative peak heights).
- schema:
  - `type`: table
  - `required_columns`: `composition`, `radial_distance_angstrom`, `density_TBA`, `density_TOL`
  - `units`:
    - `radial_distance_angstrom`: Å
    - `density_TBA`: arbitrary
    - `density_TOL`: arbitrary

### shell_analysis.txt
- path: `/app/outputs/shell_analysis.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Shell thickness and number of interfacial TBA molecules at saturation, compared to reference ranges from the paper.
- schema:
  - `type`: object
  - `required`: `e_shell_angstrom`, `N_TBA_shell`
  - `properties`:
    - `e_shell_angstrom`:
      - `type`: number
      - `unit`: Å
    - `N_TBA_shell`:
      - `type`: integer

Notes: Density units are arbitrary but must be internally consistent. The checker evaluates structural trends (TBA preferential adsorption in first layer, TOL core dominance) for x_TBA=0.49 and x_TBA=0.71. For shell_analysis.txt, e_shell and N_TBA_shell are checked against expected tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "density_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "radial_distance_angstrom",
          "density_TBA",
          "density_TOL"
        ],
        "units": {
          "radial_distance_angstrom": "Å",
          "density_TBA": "arbitrary",
          "density_TOL": "arbitrary"
        }
      },
      "description": "Radial density profiles of TBA and TOL centers of mass, used to verify the core-shell microphase separation pattern (structural ordering and relative peak heights)."
    },
    {
      "file": "shell_analysis.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "e_shell_angstrom",
          "N_TBA_shell"
        ],
        "properties": {
          "e_shell_angstrom": {
            "type": "number",
            "unit": "Å"
          },
          "N_TBA_shell": {
            "type": "integer"
          }
        }
      },
      "description": "Shell thickness and number of interfacial TBA molecules at saturation, compared to reference ranges from the paper."
    }
  ],
  "notes": "Density units are arbitrary but must be internally consistent. The checker evaluates structural trends (TBA preferential adsorption in first layer, TOL core dominance) for x_TBA=0.49 and x_TBA=0.71. For shell_analysis.txt, e_shell and N_TBA_shell are checked against expected tolerances."
}
```

## How you are scored
A hidden verifier evaluates your outputs automatically. For `density_profiles.csv`, it checks whether the radial density distributions exhibit the qualitative ordering expected for a core-shell structure—for example, that one component is enriched near the pore wall while the other dominates the central region for the tested compositions. For `shell_analysis.txt`, the verifier compares your reported shell thickness and the number of interfacial TBA molecules against numerically reasonable ranges that are physically consistent with the 12-Å pore geometry. Both checks are combined into a single reward score. Reporting a value is not sufficient; the verifier independently examines the pattern in the density profiles and the magnitude of the shell parameters.
