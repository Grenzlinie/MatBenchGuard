# Kink-pair activation enthalpy and Peierls stress for a Lomer dislocation from static NEB and dynamic MD with flexible boundary conditions

## Problem background
Kink-pair nucleation on dislocations determines the thermally activated glide in high-Peierls-stress crystals. Accurately computing the activation enthalpy as a function of stress is difficult due to configurational forces that arise in small simulation cells with rigid boundary conditions. This task studies a Lomer edge dislocation in aluminum (a high-Peierls-stress fcc case with a planar core) to investigate how activation enthalpies extracted from static nudged-elastic-band (NEB) and dynamic constant-strain-rate molecular dynamics (MD) simulations compare, and to validate a flexible boundary condition protocol that eliminates spurious stress oscillations.

## Approach
The computational approach employs two complementary methods. (1) Static NEB: For the dislocation cell, a chain of replicas between adjacent Peierls valleys is relaxed to find the minimum-energy path. The activation enthalpy is taken as the energy difference between the saddle point and the initial valley. This is repeated at several applied shear stresses from 0 to 1000 MPa. (2) Dynamic MD with flexible boundary conditions: The simulation cell is sheared at a constant strain rate while the atoms in the outer layers are allowed to relax in the shear direction, removing the average force. The stress is recorded as a function of strain and time. The dislocation undergoes jump events between valleys. The effective activation enthalpy is extracted from the average jump stress using the statistical relation H* = kT ln(ν* Δτ / τ̇₀), with attempt frequency ν = 5×10¹³ s⁻¹, dislocation segment length L_Y = 14.4 nm, critical kink size ℓ_c = b = 0.2851 nm, and stress drop Δτ = μ ρ b². To verify the flexible BC, a short test simulation is run, and the stress oscillation amplitude is measured. Additionally, the athermal Peierls stress for rigid motion is determined by statically pushing a short straight dislocation.

## Reproduction target
The final output consists of four scored artifacts: (i) a stress-strain curve from a short flexible-BC test at 200 K, used to check that stress oscillations are small; (ii) a table of static NEB enthalpy values at stresses including 0, 200, 400, 600, 800, and 1000 MPa; (iii) the Peierls stress for rigid motion (a single scalar in MPa); (iv) a table of dynamic effective activation enthalpies extracted from MD runs at 150, 200, and 250 K, along with the corresponding average jump stresses. The primary scientific goal is the comparison between the static and dynamic enthalpy-stress relations.

## Assets

- Ercolessi-Adams EAM potential for Al: https://www.ctcms.nist.gov/potentials/Download/Al-1.eam.alloy
- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- Python 3 with numpy, scipy: python3

## Workflow steps

### Step 1: Prepare Lomer dislocation simulation cell
- Role: process
- Action: Construct a simulation cell containing a single Lomer edge dislocation in Al, orient axes X=[110], Y=[-110], Z=[001], and relax the atomic configuration using the provided Ercolessi-Adams EAM potential. Save the relaxed atom positions and cell dimensions in a format suitable for subsequent MD and NEB runs.
- Evidence: `/app/outputs/relaxed_dislocation_cell.data`

### Step 2: Validate flexible boundary conditions
- Role: scored
- Action: Run a short constant strain-rate molecular dynamics simulation (L_Y=2 nm, T=200 K, strain rate 5e-5 ps^-1) using the flexible boundary condition protocol. Save stress (MPa) vs strain (dimensionless).
- Output file: `/app/outputs/flexible_bc_stress_strain.csv`
- Format: csv
- Contract: strain (dimensionless), stress_MPa (MPa)
- Scoring: scored by hidden verifier

### Step 3: Static NEB activation enthalpy vs stress
- Role: scored (load-bearing)
- Action: Perform nudged elastic band (NEB) calculations on the full dislocation cell (L_Y=14.4 nm) at several applied shear stresses covering 0 to 1000 MPa. Extract the activation enthalpy H(τ) as the energy difference between the saddle point and the initial Peierls valley, and save the (stress, enthalpy) pairs.
- Output file: `/app/outputs/static_enthalpy.csv`
- Format: csv
- Contract: stress_MPa (MPa), enthalpy_eV (eV)
- Scoring: scored by hidden verifier

### Step 4: Peierls stress for rigid motion
- Role: scored
- Action: On a short dislocation configuration, incrementally increase the applied shear stress in a series of static simulations until the straight dislocation moves athermally by at least one Peierls valley. Report the critical stress as the Peierls stress for rigid motion.
- Output file: `/app/outputs/peierls_rigid_motion.json`
- Format: json
- Contract: {'peierls_stress_MPa': <float>}
- Scoring: scored by hidden verifier

### Step 5: Run constant strain-rate MD simulations
- Role: process
- Action: Perform constant strain-rate molecular dynamics simulations on the full dislocation cell at strain rate 1.5e-5 ps^-1 using flexible boundary conditions at temperatures 150 K, 200 K, and 250 K. For each temperature save the time evolution of stress and dislocation position, which will be used to extract the dynamic activation enthalpy.
- Evidence: `/app/outputs/md_stress_time_series_150K.csv, md_stress_time_series_200K.csv, md_stress_time_series_250K.csv`

### Step 6: Extract dynamic activation enthalpy
- Role: scored (load-bearing)
- Action: From the stress time series at each temperature, identify dislocation jump events and compute the average jump stress τ. Calculate the effective activation enthalpy H*(T) using the statistical model relation H* = kT ln(ν* Δτ / τ̇₀) with ν = 5×10¹³ s⁻¹ and critical kink size ℓ_c = b = 0.2851 nm. Save temperature (K), average jump stress (MPa), and enthalpy (eV).
- Output file: `/app/outputs/dynamic_enthalpy.csv`
- Format: csv
- Contract: temperature_K (K), avg_jump_stress_MPa (MPa), enthalpy_eV (eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/flexible_bc_stress_strain.csv`
- `/app/outputs/static_enthalpy.csv`
- `/app/outputs/peierls_rigid_motion.json`
- `/app/outputs/dynamic_enthalpy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### flexible_bc_stress_strain.csv
- path: `/app/outputs/flexible_bc_stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Stress-strain data from a short MD simulation with flexible BC. The checker verifies that the stress oscillation amplitude (standard deviation over strain 0.0025–0.007) is below 50 MPa.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_MPa`
  - `units`:
    - `strain`: dimensionless
    - `stress_MPa`: MPa

### static_enthalpy.csv
- path: `/app/outputs/static_enthalpy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Kink-pair activation enthalpy from static NEB as a function of stress. The checker compares enthalpy values at selected stresses (0, 200, 400, 600, 800, 1000 MPa) to a hidden reference within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `stress_MPa`, `enthalpy_eV`
  - `units`:
    - `stress_MPa`: MPa
    - `enthalpy_eV`: eV

### peierls_rigid_motion.json
- path: `/app/outputs/peierls_rigid_motion.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Peierls stress for rigid motion determined from static push tests on a short dislocation. The checker compares the reported value to a hidden reference within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `peierls_stress_MPa`: number
  - `units`:
    - `peierls_stress_MPa`: MPa

### dynamic_enthalpy.csv
- path: `/app/outputs/dynamic_enthalpy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective kink-pair activation enthalpy extracted from constant strain-rate MD simulations at three temperatures. The checker compares the enthalpy values to a hidden reference within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `avg_jump_stress_MPa`, `enthalpy_eV`
  - `units`:
    - `temperature_K`: K
    - `avg_jump_stress_MPa`: MPa
    - `enthalpy_eV`: eV

Notes: All scored artifacts are re-derivable from raw simulation outputs. The checker applies tolerance-based comparisons against paper-reported values. The dynamic enthalpy extraction uses a fixed attempt frequency ν=5×10¹³ s⁻¹ and critical kink size ℓ_c=b=0.2851 nm as stated in the workflow; the checker verifies consistency with the given relation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "flexible_bc_stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_MPa"
        ],
        "units": {
          "strain": "dimensionless",
          "stress_MPa": "MPa"
        }
      },
      "description": "Stress-strain data from a short MD simulation with flexible BC. The checker verifies that the stress oscillation amplitude (standard deviation over strain 0.0025–0.007) is below 50 MPa."
    },
    {
      "file": "static_enthalpy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stress_MPa",
          "enthalpy_eV"
        ],
        "units": {
          "stress_MPa": "MPa",
          "enthalpy_eV": "eV"
        }
      },
      "description": "Kink-pair activation enthalpy from static NEB as a function of stress. The checker compares enthalpy values at selected stresses (0, 200, 400, 600, 800, 1000 MPa) to a hidden reference within a tolerance."
    },
    {
      "file": "peierls_rigid_motion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "peierls_stress_MPa": "number"
        },
        "units": {
          "peierls_stress_MPa": "MPa"
        }
      },
      "description": "Peierls stress for rigid motion determined from static push tests on a short dislocation. The checker compares the reported value to a hidden reference within a tolerance."
    },
    {
      "file": "dynamic_enthalpy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "avg_jump_stress_MPa",
          "enthalpy_eV"
        ],
        "units": {
          "temperature_K": "K",
          "avg_jump_stress_MPa": "MPa",
          "enthalpy_eV": "eV"
        }
      },
      "description": "Effective kink-pair activation enthalpy extracted from constant strain-rate MD simulations at three temperatures. The checker compares the enthalpy values to a hidden reference within a tolerance."
    }
  ],
  "notes": "All scored artifacts are re-derivable from raw simulation outputs. The checker applies tolerance-based comparisons against paper-reported values. The dynamic enthalpy extraction uses a fixed attempt frequency ν=5×10¹³ s⁻¹ and critical kink size ℓ_c=b=0.2851 nm as stated in the workflow; the checker verifies consistency with the given relation."
}
```

## How you are scored
Each scored output file is evaluated by a hidden verifier that recomputes derived quantities or compares your reported values to a hidden reference. The verifier checks: (i) that the stress standard deviation in the flexible‑BC test is below a predetermined threshold; (ii) that the static enthalpy values at specified stresses are within an acceptable tolerance of the reference; (iii) that the dynamic enthalpies at the three temperatures match the reference; (iv) that the Peierls stress for rigid motion is within a tolerance. The overall reward is a weighted sum of these per‑artifact checks. Meeting or exceeding the hidden thresholds (i.e., coming closer to the correct answer) yields higher reward. Your job is to perform the simulations and analysis correctly; simply reporting numbers that look plausible is not sufficient because the verifier recomputes metrics from your raw data where possible.
