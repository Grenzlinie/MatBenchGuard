# DFT Relative Energies and Diffusion Barriers of Al Trimer on Al(111) Surface

## Problem background
The diffusion of small clusters on metal surfaces is fundamental to understanding nucleation, growth, and catalysis. The Al trimer on Al(111) is the smallest cluster that can adopt both one‑dimensional (linear) and two‑dimensional (triangular) structures, making it an ideal model system for studying structural stability and diffusion mechanisms. A detailed energetic landscape — relative total energies of various trimer configurations and the energy barriers for interconversion pathways — is needed to identify the most relevant configurations and dominant diffusion modes. This task requires you to compute this landscape from first‑principles density‑functional theory (DFT).

## Approach
Use first‑principles plane‑wave DFT with the local‑density approximation (LDA) and an ultrasoft or PAW pseudopotential for aluminium. Model the Al(111) surface as a periodic slab of six atomic layers with a vacuum gap of 9.4 Å. The in‑plane supercell must be a hexagonal (5 × 5) surface unit cell constructed from the LDA bulk lattice constant a₀ = 3.98 Å. Use a plane‑wave kinetic energy cut‑off of 9.5 Ry and a (2 × 2) Monkhorst‑Pack k‑point mesh. Place Al trimer atoms in all known configurations: four compact triangular (FCC‑H, HCP‑H, FCC‑T, HCP‑T), two linear (FCC‑L, HCP‑L), and eight non‑compact triangular configurations (as listed in the workflow steps). For each configuration, relax the trimer atoms and the top three slab layers while keeping the bottom three layers fixed at their bulk LDA positions. Compute converged total energies and then calculate relative energies referenced to the most stable configuration. Next, for the three key diffusion mechanisms — (i) concerted translations of compact triangular trimers, (ii) transformation between compact triangular and linear trimers, and (iii) intercell translation of the linear trimer — locate the minimum‑energy path (using the nudged elastic band method or constrained relaxations) and extract the energy barrier for each. An open‑source DFT code (e.g. Quantum ESPRESSO) may be used; the commercial code originally employed is not required.

## Reproduction target
Your objective is to compute and report two quantities: (1) the relative total energies (in eV) of every trimer configuration listed in Step 1, referenced to the most stable configuration; (2) the energy barriers (in eV) for the three diffusion pathways described in Step 2. Write the results to the specified CSV files in /app/outputs. Your submission will be checked against hidden reference numbers that represent the correct results for this system.

As a scientific sanity check: verify that the relative energies you compute follow physical intuition — compact triangular trimers should be more stable (lower in energy) than linear trimers and non‑compact triangular trimers. Any significant violation of this ordering likely indicates a numerical problem and should be investigated before submission.

## Assets

- Open-source plane-wave DFT code with LDA and ultrasoft/PAW pseudopotentials for Al (e.g. Quantum ESPRESSO): https://www.quantum-espresso.org/
- Aluminium LDA pseudopotential: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: DFT total energy calculations of Al trimer configurations
- Role: scored
- Action: Construct a six-layer Al(111) slab with a (5×5) surface cell, a₀ = 3.98 Å, and a vacuum region of 9.4 Å. Use a (2×2) Monkhorst–Pack k‑point mesh and a plane‑wave cut‑off of 9.5 Ry. Place Al trimers in the following configurations: compact triangular (FCC-H, HCP-H, FCC-T, HCP-T), linear (FCC-L, HCP-L), and eight non-compact triangular (1F2H-120°, 2F1H-150°, 1F2H-150°, 3H-120°, 2F1H-120°, 3F-120°, 2F1H-90°, 1F2H-90°). For each configuration, relax the trimer atoms and the top three slab layers while keeping the bottom three layers fixed at bulk LDA positions. Use LDA exchange-correlation.

  **Important – unstable non‑compact configurations**: The two configurations **2F1H‑90°** and **1F2H‑90°** are not stable structures. If all atoms are allowed to relax freely, these configurations relax back to compact triangular trimers and yield incorrect (lower) energies. To obtain their energies in the sense reported in the literature, you must apply a targeted constraint on one atom in each of these two structures.

  - **2F1H‑90°**: In this configuration, one Al atom (the one that would, upon free relaxation, slide towards the nearest fcc site and convert the trimer into a compact triangular shape) must be prevented from moving. Identify the vector from the initial position of this atom to the centre of the adjacent fcc adsorption site. During ionic relaxation, fix the Cartesian coordinate component of that atom that is **parallel to this vector** (i.e. fix the spatial coordinate that corresponds to the direction of the impending slide).
  - **1F2H‑90°**: Analogously, identify the atom that would move towards the nearest hcp site and fix its Cartesian coordinate component parallel to the vector pointing from the initial position to that hcp site.

  All other configurations can be relaxed without any coordinate constraints.

  Converge total energies, then compute relative energies (eV) referenced to the most stable configuration. Output the relative energies to a CSV file.
- Output file: `/app/outputs/relative_energies.csv`
- Format: csv
- Contract: Columns: configuration (string) – name of the trimer configuration; relative_energy_eV (float) – total energy relative to the most stable configuration in electron-volts. Rows must include all configurations listed in the action.
- Scoring: scored by hidden verifier

### Step 2: DFT energy barrier calculations for selected diffusion paths
- Role: scored
- Action: Using the relaxed structures from Step 1, compute energy barriers for the following three diffusion mechanisms. For each path, locate the minimum‑energy profile (e.g. via nudged elastic band or constrained relaxations) and extract the highest energy barrier encountered along the path.

  1. **Concerted translation of compact triangular trimers**: investigate the path connecting FCC‑H and HCP‑T (the equivalent path between FCC‑T and HCP‑H should give the same barrier; you may compute either or both for validation). Label this result as `concerted FCC-H↔HCP-T translation` in the output file.

  2. **Triangular‑to‑linear transformation**: investigate a path that converts a compact triangular trimer into a linear one and back, e.g. FCC‑H → intermediate (such as 1F2H‑120°) → FCC‑L → intermediate (such as 2F1H‑120°) → HCP‑H. Determine the overall barrier for this transformation. Label this result as `triangular-to-linear transformation`.

  3. **Linear trimer intercell translation**: investigate the translation of the linear trimer from FCC‑L to HCP‑L. Label this result as `linear intercell translation`.

  Report exactly one barrier value per mechanism.
- Output file: `/app/outputs/diffusion_barriers.csv`
- Format: csv
- Contract: Columns: diffusion_path (string) – exactly one of the labels listed above; barrier_eV (float) – computed energy barrier in electron-volts. The file must contain exactly three rows, one for each mechanism.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.csv`
- `/app/outputs/diffusion_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly. All output files are in **CSV format** (comma‑separated values), not JSON.

### relative_energies.csv
- path: `/app/outputs/relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative total energies of all Al trimer configurations referenced to the most stable configuration.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `relative_energy_eV`
  - `units`:
    - `relative_energy_eV`: eV

### diffusion_barriers.csv
- path: `/app/outputs/diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy barriers for three key diffusion mechanisms of Al trimers on Al(111) surface.
- schema:
  - `type`: table
  - `required_columns`: `diffusion_path`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

## Self-check before finishing (optional, not scored)

Before you finish, verify that your output files exist under `/app/outputs` and follow the CSV format described above: each file has the expected columns (`configuration`/`relative_energy_eV` for relative_energies.csv, and `diffusion_path`/`barrier_eV` for diffusion_barriers.csv), all required rows are present, and values are reasonable floats. This checks shape only — it does not judge scientific correctness, and passing it does not mean your answer is correct.

## How you are scored
After your workflow finishes, a hidden verifier script inspects the two output CSV files. For relative energies, it compares each configuration's value to the corresponding hidden gold value, using an appropriate tolerance that absorbs the numerical spread inherent to different DFT implementations. For energy barriers, it similarly compares each reported barrier to its gold reference. The verifier also checks that the configuration you report as the most stable (the one with relative energy 0.0) matches the correct reference minimum, as well as basic physical ordering among configuration families. Each artifact carries a weight; your final score is a weighted combination (0.0–1.0) of the per‑artifact scores. The exact tolerances and weights are predefined and hidden. You do not need to produce an exact match to a particular published table — the tolerances are set to accept a legitimate reproduction.