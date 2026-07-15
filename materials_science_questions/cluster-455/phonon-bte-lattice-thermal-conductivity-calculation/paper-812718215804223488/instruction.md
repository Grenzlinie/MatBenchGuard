# Lattice thermal conductivity of type-I Si/Ge clathrates from DFT phonon calculations and Debye-Callaway model

## Problem background
Intermetallic type-I clathrates, built from a host framework of tetrahedrally bonded Si or Ge atoms that encapsulates guest atoms (alkali or alkaline earth metals), exhibit promising thermoelectric properties due to their expected “phonon glass electron crystal” (PGEC) behaviour. The low lattice thermal conductivity is thought to originate from guest rattling modes and increased anharmonicity, but the detailed phonon dynamics — especially the interplay between guests, host, and spontaneous framework vacancies — remain incompletely understood. This task investigates how guest filling modifies the vibrational properties and lattice thermal conductivity of binary Si and Ge clathrates by performing first-principles phonon calculations and applying the Debye–Callaway model.

## Approach
The computational approach combines density functional theory (DFT) with quasi-harmonic phonon calculations and the Debye–Callaway thermal conductivity model. For each clathrate composition — empty Si46 and Ge46, and their Na-, K-, and Ba-filled stable phases (Na8Si46, K8Si46, Ba8Si46, K8Ge44□2, and Ba8Ge43□3) — the workflow proceeds as follows:

1. **DFT relaxation**: fully relax the atomic positions and lattice parameters to obtain the equilibrium crystal structure.
2. **Harmonic phonon dispersion**: compute the phonon band structure on a fine k-point grid and along high-symmetry paths to obtain mode frequencies ω_i(K).
3. **Group velocity extraction**: from the harmonic dispersions, numerically differentiate to obtain mode-resolved group velocities v_i = dω_i/dK, and then average to get branch velocities v_TA, v_LA and the average sound velocity v_s.
4. **Quasi-harmonic calculations**: generate isotropically strained volumes (±5%) and re-compute the harmonic phonon dispersions at each volume to capture the volume dependence of frequencies.
5. **Grüneisen parameter extraction**: calculate mode Grüneisen parameters γ_i = −(1/ω_i) dω_i/dV using central differences; compute branch-averaged γ for the TA and LA branches and the average Grüneisen parameter γ̄ at 300 K from a frequency-window average.
6. **Debye temperature determination**: identify the zone-boundary frequencies of the acoustic branches and compute mode Debye temperatures θ_i = ℏ ω_max / k_B, and also derive the average Debye temperature θ_D from the sound velocity.
7. **Scattering lifetime modeling**: for each acoustic mode (TA, TA′, LA), compute the normal (τ_N) and Umklapp (τ_U) phonon scattering lifetimes as functions of the reduced frequency x = ℏω/k_B T using the analytical expressions from the Debye–Callaway formalism. The required inputs are the group velocities, Grüneisen parameters, Debye temperatures, average atomic mass, and unit-cell volume.
8. **Lattice thermal conductivity**: evaluate the Asen–Palmer modified Debye–Callaway formula that combines the normal and Umklapp scattering lifetimes to obtain the per-branch thermal conductivity κ_l^i(T) and sum them to obtain the total κ_l(T). The calculation is performed at T = 300 K. For Ba8Ge43□3 the model predicts diverging Grüneisen parameters, making the κ_l integral ill-defined; therefore that composition should be reported as “N/A” or left empty.

## Reproduction target
Compute the lattice thermal conductivity at 300 K for the seven clathrate systems: Si46, Na8Si46, K8Si46, Ba8Si46, Ge46, K8Ge44□2, and Ba8Ge43□3, by executing the DFT+phonon+Debye–Callaway pipeline described above. Write the results to `/app/outputs/thermal_conductivity.csv` with columns `system` and `kappa_300` (in W/m/K). The rows must appear in exactly the order listed above. For the Ba8Ge43□3 system the Debye–Callaway integral diverges; the `kappa_300` entry for that row must be left empty or contain the string “N/A”.

## Assets

- DFT code (e.g. FHI-aims, Quantum ESPRESSO): https://aimsclub.fhi-berlin.mpg.de/
- phonopy: https://phonopy.github.io/phonopy/
- Python scientific libraries (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: Perform DFT structural relaxation for each clathrate composition (Si46, Na8Si46, K8Si46, Ba8Si46, Ge46, K8Ge44□2, Ba8Ge43□3) using an appropriate DFT code. Relax atomic positions and lattice vectors until forces are below a chosen convergence threshold. Save the relaxed structures (atomic positions and lattice vectors).
- Evidence: none

### Step 2: Harmonic phonon dispersion calculation
- Role: process
- Action: For each relaxed structure, compute harmonic phonon band structures using a DFT code and the phonopy post-processor. Obtain phonon eigenfrequencies ω_i(K) on a fine k-point grid and along high-symmetry paths.
- Evidence: none

### Step 3: Phonon group velocity extraction
- Role: process
- Action: From the harmonic phonon dispersions, compute mode-resolved phonon group velocities v_i = dω_i/dK using a finite-difference method along the chosen high-symmetry path. Average to obtain branch velocities v_TA, v_LA, and compute the average sound velocity v_s. Save the computed group velocities to group_velocity.csv.
- Evidence: `/app/outputs/group_velocity.csv`

### Step 4: Quasi-harmonic phonon calculations on strained volumes
- Role: process
- Action: For each composition, generate structures with isotropic volume strains (e.g., ±5%). Relax internal coordinates at fixed strained volumes and compute harmonic phonon dispersions at each volume.
- Evidence: none

### Step 5: Grüneisen parameter extraction
- Role: process
- Action: From the frequency shift with volume, calculate mode-resolved Grüneisen parameters γ_i = −(1/ω_i)·dω_i/dV using central differences. Compute branch-averaged γ for TA and LA modes, and the average Grüneisen parameter γ̄ at 300 K. Save the Grüneisen parameters to gruneisen_parameters.csv.
- Evidence: `/app/outputs/gruneisen_parameters.csv`

### Step 6: Acoustic-mode Debye temperature calculation
- Role: process
- Action: Identify the zone-boundary termination frequencies of the TA and LA branches from harmonic dispersions, compute mode Debye temperatures θ_i = ℏ·ω_max/k_B, and derive the average Debye temperature θ_D from the sound velocity. Save the Debye temperatures to debye_temperatures.csv.
- Evidence: `/app/outputs/debye_temperatures.csv`

### Step 7: Phonon scattering lifetime modeling
- Role: process
- Action: For each acoustic mode (TA, TA′, LA), compute the normal scattering lifetime τ_N and Umklapp scattering lifetime τ_U as functions of reduced frequency x = ℏω/k_BT using the Debye-Callaway formulas with the group velocities, Grüneisen parameters, Debye temperatures, atomic masses, and unit-cell volume. Save computed lifetimes or array data as scattering_lifetimes.csv (.npy) for inspection.
- Evidence: `/app/outputs/scattering_lifetimes.csv`

### Step 8: Lattice thermal conductivity calculation (scored output)
- Role: scored (load-bearing)
- Action: For each system, calculate the per-branch lattice thermal conductivity κ_l^i(T) using the Asen-Palmer modified Debye-Callaway equation and sum to obtain the total κ_l(T) at 300 K. The model fails for Ba8Ge43□3; report that system with an empty or 'N/A' value. Write the results to thermal_conductivity.csv.
- Output file: `/app/outputs/thermal_conductivity.csv`
- Format: csv
- Contract: CSV with columns: system (string), kappa_300 (float, in W/m/K). Rows in exact order: Si46, Na8Si46, K8Si46, Ba8Si46, Ge46, K8Ge44□2, Ba8Ge43□3. For Ba8Ge43□3 the kappa_300 entry must be empty or the string 'N/A'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.csv
- path: `/app/outputs/thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Lattice thermal conductivity at 300K computed from DFT phonon properties and Debye-Callaway model.
- schema:
  - `type`: table
  - `required_columns`: `system`, `kappa_300`
  - `units`:
    - `kappa_300`: W/m/K
  - `description`: CSV file with two columns: system (string) and kappa_300 (float, W/m/K). Rows in exact order: Si46, Na8Si46, K8Si46, Ba8Si46, Ge46, K8Ge44□2, Ba8Ge43□3. For Ba8Ge43□3 the entry must be empty or the string 'N/A'.

Notes: The thermal conductivity for Ba8Ge43□3 is not computable with this model (divergent Grüneisen parameters); the agent should report an empty/N/A entry for that system.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "kappa_300"
        ],
        "units": {
          "kappa_300": "W/m/K"
        },
        "description": "CSV file with two columns: system (string) and kappa_300 (float, W/m/K). Rows in exact order: Si46, Na8Si46, K8Si46, Ba8Si46, Ge46, K8Ge44□2, Ba8Ge43□3. For Ba8Ge43□3 the entry must be empty or the string 'N/A'."
      },
      "description": "Lattice thermal conductivity at 300K computed from DFT phonon properties and Debye-Callaway model."
    }
  ],
  "notes": "The thermal conductivity for Ba8Ge43□3 is not computable with this model (divergent Grüneisen parameters); the agent should report an empty/N/A entry for that system."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/thermal_conductivity.csv`. It checks that the file is well-formed CSV with the correct columns and row order, and then compares the numeric `kappa_300` values for the six computable systems (all except Ba8Ge43□3) against the expected values using a relative tolerance. Each system contributes equally to the total score (1/6 per system). The Ba8Ge43□3 row is evaluated only for the format requirement (empty or “N/A”). The verifier does not inspect the intermediate evidence files — only the final thermal conductivity CSV is scored. The exact tolerance is not disclosed. To obtain full credit you must execute the complete computational pipeline; reporting a pre‑known number without rerunning the calculations will not satisfy the tolerance.
