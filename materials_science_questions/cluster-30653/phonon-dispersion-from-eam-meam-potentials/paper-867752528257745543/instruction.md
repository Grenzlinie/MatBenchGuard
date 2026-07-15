# Dislocation Core Structure and Energy from Deep Potential Simulations in FCC Copper

## Problem background
The core structure of dislocations in face-centered cubic (FCC) metals governs plasticity mechanisms such as cross‑slip and climb. In copper, the 1/2⟨110⟩{111} dislocation dissociates into two Shockley partial dislocations separated by a stacking‑fault ribbon. The splitting width and core energy are key parameters but are challenging to obtain from first‑principles DFT because of the large length scales. Machine‑learned interatomic potentials, like the Deep Potential (DP) trained on DFT data, promise DFT-level accuracy on the scales needed to resolve dislocation cores. This task asks you to compute the equilibrium splitting widths (in units of the Burgers vector b) of the 0° (screw), 60° (mixed), and 90° (edge) dislocation in FCC copper, and the core energy per unit length of the screw dislocation, using the DP potential and molecular statics.

## Approach
A DP potential for copper, available from the Deep Potential Library, is used with the open‑source codes LAMMPS and deepmd‑kit. Dislocation dipole supercells of ~10⁵ atoms are constructed for the three dislocation orientations according to the paper’s geometry. Initial atomic positions are set using the analytical displacement field of the Peierls‑Nabarro model, then the structures are relaxed to their minimum energy via molecular statics. From the relaxed configurations, the slip displacement profile along the glide plane is extracted and differentiated to obtain the discrete dislocation density; the splitting width is the distance between the two density peaks. For the core energy, a series of quadrupole supercells with varying cell sizes are relaxed, and the total dislocation energy (total energy minus the perfect‑crystal reference) is recorded as a function of the dipole separation. The core energy is obtained by fitting the energy to the elastic continuum picture where the energy scales linearly with the logarithm of the dipole separation, and subtracting the elastic part.

## Reproduction target
Produce two scored artifacts: (1) a CSV file containing the splitting widths d (in units of b, where b = 2.57 Å) for the 0° (screw), 60° (mixed), and 90° (edge) dislocation; (2) a text file reporting the core energy per unit length (eV/Å) of the screw dislocation. Both quantities are to be obtained by executing the DP molecular statics workflow described in the steps below, using the specified Cu DP potential and supercell geometries.

## Assets

- Cu DP potential (Zhang et al.): http://dplibrary.deepmd.net/
- LAMMPS: https://lammps.sandia.gov/
- deepmd-kit: https://github.com/deepmodeling/deepmd-kit

## Workflow steps

### Step 1: DP molecular statics of dislocation cores
- Role: process
- Action: Construct dipole supercells containing approximately 10^5 atoms for 0° screw, 60° mixed, and 90° edge dislocations in FCC Cu. Use the supercell geometry from the paper: basis vectors a1=1/2[011], a2=1/2[2-1-1], a3=[11-1]; parameters (l1,l2,l3)=(1,480,70) for screw/60°, (480,1,70) for edge. Insert initial dislocation displacement fields according to the P‑N model solution, then perform energy minimization (molecular statics) with the Cu DP potential using LAMMPS and the deepmd-kit interface. Save relaxed atomic configurations.
- Evidence: `/app/outputs/core_sim_summary.txt`

### Step 2: Extract splitting widths
- Role: scored (load-bearing)
- Action: From the relaxed configurations, extract the slip displacement field s(l) along the glide plane. Compute discrete dislocation densities ρ(l) = s(l+1)-s(l). For each dislocation type (0°, 60°, 90°), determine the splitting width d as the distance between the two peaks of the appropriate density component (ρ_x for screw and edge, ρ_y for 60° mixed), expressed in units of the Burgers vector b (b = 2.57 Å). Write the results to splitting_widths.csv with columns 'dislocation_angle' and 'splitting_width_b'.
- Output file: `/app/outputs/splitting_widths.csv`
- Format: csv
- Contract: CSV with header: dislocation_angle (string: '0deg','60deg','90deg'), splitting_width_b (float). Three rows.
- Scoring: scored by hidden verifier

### Step 3: DP simulations of screw dislocation arrays
- Role: process
- Action: Construct quadrupole supercells for screw dislocation arrays with varying cell sizes. Fix l1=1 and vary l2 (e.g., 40,80,120,160) while for each l2 vary l3 from 5 to 90, or fix l3=60 and vary l2 from 30 to 120 as described in the paper. For each supercell, perform DP molecular statics to obtain the total energy of the dislocation array. Subtract the perfect-crystal energy (N_a * E_a, where N_a=6*l1*l2*l3, E_a=−3.728 eV) to get the dislocation contribution. Record the total dislocation energy per unit dislocation length as a function of the dipole separation distance L_d.
- Evidence: `/app/outputs/array_energies.json`

### Step 4: Derive core energy
- Role: scored (load-bearing)
- Action: Using the total dislocation energies of the screw arrays as a function of dipole separation L_d, fit the data to the elastic continuum picture where the total energy per unit length of the dislocation dipole is linear in log(L_d). Extract the core energy per unit length E_core by subtracting the elastic contribution. Write the obtained value to core_energy.txt as a single line: 'core_energy_eV_per_Angstrom: <value>' (value in eV/Å).
- Output file: `/app/outputs/core_energy.txt`
- Format: txt
- Contract: Single line: 'core_energy_eV_per_Angstrom: <float>'
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/splitting_widths.csv`
- `/app/outputs/core_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### splitting_widths.csv
- path: `/app/outputs/splitting_widths.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Splitting widths d (in units of b) for 0° screw, 60° mixed, and 90° edge dislocations, extracted from DP relaxed configurations.
- schema:
  - `type`: table
  - `required_columns`: `dislocation_angle`, `splitting_width_b`
  - `units`:
    - `splitting_width_b`: b (Burgers vector, b=2.57 Å)

### core_energy.txt
- path: `/app/outputs/core_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Core energy per unit length of a screw dislocation in FCC Cu, derived from DP array simulations.
- schema:
  - `type`: text
  - `format`: Single line: 'core_energy_eV_per_Angstrom: <float>'
  - `units`: eV/Å

Notes: The scored quantities are obtained from the same DP potential and are deterministic. Tolerances will be applied by the hidden checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "splitting_widths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dislocation_angle",
          "splitting_width_b"
        ],
        "units": {
          "splitting_width_b": "b (Burgers vector, b=2.57 Å)"
        }
      },
      "description": "Splitting widths d (in units of b) for 0° screw, 60° mixed, and 90° edge dislocations, extracted from DP relaxed configurations."
    },
    {
      "file": "core_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "Single line: 'core_energy_eV_per_Angstrom: <float>'",
        "units": "eV/Å"
      },
      "description": "Core energy per unit length of a screw dislocation in FCC Cu, derived from DP array simulations."
    }
  ],
  "notes": "The scored quantities are obtained from the same DP potential and are deterministic. Tolerances will be applied by the hidden checker."
}
```

## How you are scored
A hidden automated verifier independently reads your submitted `splitting_widths.csv` and `core_energy.txt`. It compares the splitting widths and the core energy against reference values from the original study, using hidden tolerance windows. Each scored artifact is weighted, and the final reward is the weighted sum of the per‑artifact scores. Simply reporting the paper’s numbers is not sufficient; you must produce the required output files through the specified simulation and analysis pipeline.
