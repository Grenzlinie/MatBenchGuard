# Computational study of transient oxygen displacements at doped ceria surfaces

## Problem background
Ceria (CeO2) is a key component in three-way catalysts for automotive emission control due to its high oxygen storage capacity (OSC). Doping with divalent cations such as Ca2+ introduces oxygen vacancies, and the OSC and catalytic activity are thought to be linked to the formation and motion of these vacancies. Despite extensive research, the atomic-level dynamics at doped ceria surfaces remain largely unexplored. This task investigates the oxygen ion motion at a Ca-doped CeO2(011) surface using classical molecular dynamics (MD) simulations to quantify how doping alters surface ion displacements and their time-dependent behaviour.

## Approach
The study uses constant-stress, constant-temperature MD simulations with a shell model to capture ion polarizability. The interatomic potentials consist of short-range Buckingham terms and long-range Coulomb interactions, with parameters taken from published works for Ce-O, Ca-O, and O-O interactions, plus shell-model parameters for Ce4+, O2- and Ca2+. Three systems are simulated: (i) a three-dimensional periodic bulk of Ca-doped CeO2, (ii) an undoped CeO2(011) slab, and (iii) a Ca-doped CeO2(011) slab where Ca ions and accompanying oxygen vacancies are introduced in every second plane (doping degree 1/8). All simulations are performed at 300 K with a 0.20 fs time step, equilibrated and then run for an 8.0 ps production trajectory. From the trajectories, the mean-square displacement (MSD) of oxygen ions is calculated as a function of depth (slice-averaged over 1.94 Å thick layers), the individual-ion squared displacement (ISD) for topmost surface oxygens is analysed to identify transient large-amplitude events, and the frequency of such events is estimated. Additional kinetic estimates for adsorbate residence times are computed using an Arrhenius expression with a given pre-exponential factor and adsorption enthalpy.

## Reproduction target
Construct and run MD simulations per the workflow steps and compute the following quantities, writing them to `/app/outputs/md_results.json`:
- Doped slab: oxygen MSD averaged over slices of thickness 1.94 Å from the slab center outwards (list of [depth_center_Ang, O_MSD_Ang2]); the maximum ISD among all topmost surface oxygen ions during the production run; the frequency (events/ps) of large-displacement events, defined as an ISD exceeding a threshold of approximately 0.1 Å².
- Undoped slab: oxygen MSD depth profile (same format) and its maximum ISD.
- Ca-doped bulk: overall oxygen MSD.
- Adsorbate residence times at 300 K and 700 K, calculated from τ = τ0 * exp(ΔH_ads/(RT)) with τ0 = 0.1 ps and ΔH_ads = 30 kJ/mol.

## Assets

- Ce-O potential parameters (Butler et al., Solid State Ionics 1983)
- Shell model parameters for Ce4+ and O2- (Sayle et al., J. Phys. Chem. 1994)
- Ca-O potential and Ca shell model (Lewis and Catlow, J. Phys. C 1985)
- O-O potential parameters (Catlow, Proc. R. Soc. A 1977)
- LAMMPS molecular dynamics package: https://lammps.org

## Workflow steps

### Step 1: Simulate Ca-doped CeO2 bulk at 300 K
- Role: process
- Action: Construct a three-dimensional periodic bulk CeO2 supercell with Ca doping (replace Ce with Ca and introduce O vacancies: 3 Ca in every second plane, doping degree 1/8). Perform constant-stress, constant-temperature MD at 300 K using the specified interatomic potentials (Butler Ce-O, Sayle shell, Lewis Ca-O, Catlow O-O) with a time step of 0.20 fs. Equilibrate (1.0 ps with temperature scaling, then 7.5 ps without scaling) and collect a 8.0 ps production trajectory.
- Evidence: `/app/outputs/doped_bulk_traj.log`

### Step 2: Simulate undoped CeO2(011) slab at 300 K
- Role: process
- Action: Construct an undoped CeO2(011) slab system with 12 ion planes, periodic in the xy-plane, free surfaces along z. Run MD under identical conditions (same potentials, temperature, equilibration, production length) as step01 to obtain a trajectory for the undoped surface.
- Evidence: `/app/outputs/undoped_slab_traj.log`

### Step 3: Simulate Ca-doped CeO2(011) slab at 300 K
- Role: process
- Action: Construct the Ca-doped CeO2(011) slab system: 12 ion planes, Ca doping of 1/8 (three Ca ions replace Ce in every second plane, charge-balanced by oxygen vacancies), periodic in xy, free surfaces in z. Run MD with the same protocol as step01.
- Evidence: `/app/outputs/doped_slab_traj.log`

### Step 4: Analyze dynamics and produce md_results.json
- Role: scored (load-bearing)
- Action: From the trajectories of step01–step03, compute and write to /app/outputs/md_results.json:
- Doped slab: oxygen MSD averaged over slices of thickness 1.94 Å from the slab center outwards (list of [depth_center_Ang, O_MSD_Ang2]); the maximum ISD among all topmost surface oxygen ions; the frequency (events/ps) of large-displacement events (ISD exceeds ~0.1 Å²).
- Undoped slab: oxygen MSD depth profile (same format) and its maximum ISD.
- Ca-doped bulk: overall oxygen MSD.
- Adsorbate residence times at 300 K and 700 K using τ = τ0 * exp(ΔH_ads/(RT)) with τ0 = 0.1 ps and ΔH_ads = 30 kJ/mol.
- Output file: `/app/outputs/md_results.json`
- Format: json
- Contract: {"doped": {"msd_vs_depth": [[float, float], ...], "max_isd_ang2": float, "frequency_per_ps": float}, "undoped": {"msd_vs_depth": [[float, float], ...], "max_isd_ang2": float}, "bulk_doped_msd_ang2": float, "residence_times": {"300K": float, "700K": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/md_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### md_results.json
- path: `/app/outputs/md_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled molecular dynamics results to be compared against the paper's reported values for MSD depth profiles, maximum ISD, event frequency, and residence time estimates.
- schema:
  - `type`: object
  - `required`: `doped`, `undoped`, `bulk_doped_msd_ang2`, `residence_times`
  - `properties`:
    - `doped`:
      - `type`: object
      - `required`: `msd_vs_depth`, `max_isd_ang2`, `frequency_per_ps`
      - `description`: Oxygen dynamics in the Ca-doped CeO2(011) slab: msd_vs_depth is an array of [depth_center_A, O_MSD_Ang2]; max_isd_ang2 (float); frequency_per_ps (float).
    - `undoped`:
      - `type`: object
      - `required`: `msd_vs_depth`, `max_isd_ang2`
      - `description`: Oxygen dynamics in the undoped CeO2(011) slab: msd_vs_depth array; max_isd_ang2 (float).
    - `bulk_doped_msd_ang2`:
      - `type`: number
      - `description`: Overall oxygen MSD in the Ca-doped CeO2 bulk at 300 K (Angstrom^2).
    - `residence_times`:
      - `type`: object
      - `required`: `300K`, `700K`
      - `description`: Estimated adsorbate residence times (ps) at 300 K and 700 K.

Notes: All values are at 300 K except where noted. The checker will compare each quantity to the paper's reported reference with appropriate tolerances, giving highest weight to the doped-slab MSD and max ISD.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "md_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "doped",
          "undoped",
          "bulk_doped_msd_ang2",
          "residence_times"
        ],
        "properties": {
          "doped": {
            "type": "object",
            "required": [
              "msd_vs_depth",
              "max_isd_ang2",
              "frequency_per_ps"
            ],
            "description": "Oxygen dynamics in the Ca-doped CeO2(011) slab: msd_vs_depth is an array of [depth_center_A, O_MSD_Ang2]; max_isd_ang2 (float); frequency_per_ps (float)."
          },
          "undoped": {
            "type": "object",
            "required": [
              "msd_vs_depth",
              "max_isd_ang2"
            ],
            "description": "Oxygen dynamics in the undoped CeO2(011) slab: msd_vs_depth array; max_isd_ang2 (float)."
          },
          "bulk_doped_msd_ang2": {
            "type": "number",
            "description": "Overall oxygen MSD in the Ca-doped CeO2 bulk at 300 K (Angstrom^2)."
          },
          "residence_times": {
            "type": "object",
            "required": [
              "300K",
              "700K"
            ],
            "description": "Estimated adsorbate residence times (ps) at 300 K and 700 K."
          }
        }
      },
      "description": "Compiled molecular dynamics results to be compared against the paper's reported values for MSD depth profiles, maximum ISD, event frequency, and residence time estimates."
    }
  ],
  "notes": "All values are at 300 K except where noted. The checker will compare each quantity to the paper's reported reference with appropriate tolerances, giving highest weight to the doped-slab MSD and max ISD."
}
```

## How you are scored
A hidden verifier independently scores each reported quantity in `md_results.json`. The overall reward is a weighted sum over multiple checks: the doped-slab MSD (particularly the outermost slice), the maximum ISD of the doped slab, the event frequency, the undoped slab maximum ISD, the doped bulk MSD, and the residence times. Each check compares your submitted value to an expected reference range with a relative tolerance appropriate for the computational method. The doped-slab MSD and maximum ISD carry the highest weight. Meeting or exceeding the reference thresholds earns full credit for those items; simply reporting numbers from the literature is not sufficient—the verifier expects results derived from a genuine re-execution of the described simulations.
