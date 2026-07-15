# Electrocaloric temperature change simulation in BaTiO3 with FERAM

## Problem background
The electrocaloric (EC) effect is a change in the temperature of a material upon adiabatic application or removal of an electric field. Ferroelectric materials near phase transitions are particularly promising for solid-state cooling applications. BaTiO3 exhibits three successive ferroelectric transitions—from cubic to tetragonal (C-T), tetragonal to orthorhombic (T-O), and orthorhombic to rhombohedral (O-R)—making it an ideal model system to explore EC effects at ferroelectric-ferroelectric transitions. First-principles-based effective Hamiltonian molecular dynamics (MD) simulations can predict the EC response under various field directions and temperatures. Understanding the EC temperature change and the associated structural evolution at these transitions is essential for evaluating their potential in caloric devices.

## Approach
We use the FERAM code, an open-source implementation of the effective Hamiltonian method for ferroelectrics. The model captures the essential degrees of freedom (soft-mode displacements and homogeneous/inhomogeneous strain) responsible for the phase transitions in BaTiO3. A 96×96×96 supercell (about 900 000 perovskite unit cells) is employed. The simulation protocol consists of:

- Thermalization in the isothermal-isobaric (NPT) ensemble at the target temperature and applied electric field.
- Switching to the microcanonical (NPE) ensemble and linearly ramping the electric field to zero while recording the instantaneous kinetic energy.
- Computing the adiabatic temperature change ΔT from the change in average kinetic energy using the equipartition theorem: ΔT = 2 ΔE_kin / (N_f k_B), where N_f is the number of dynamical degrees of freedom.
- Because the effective Hamiltonian treats only the soft-mode vectors as dynamical (3 variables per unit cell, rather than the 15 in the real material), the computed ΔT must be scaled by the factor 3/15 = 1/5 to account for the reduced specific heat. This scaling is applied to obtain the comparable physical temperature change.

Additionally, polarization components are averaged over the simulation cell and tracked throughout the entire process. The field direction and initial condition studied here correspond to the regime where a field-induced phase transition between the tetragonal and orthorhombic phases may occur.

## Reproduction target
Perform the MD simulation at an initial temperature of 125 K with an electric field of 200 kV/cm applied along the [001] pseudocubic direction, then linearly ramp the field to zero. Record the full time evolution of the system temperature (determined from the kinetic energy) and the three Cartesian polarization components (Px, Py, Pz) at 1 ps intervals. From this trajectory, compute the scaled adiabatic EC temperature change as follows:

- Identify the last 40 ps of the equilibration period before the field ramp as the initial equilibrium region; compute its average temperature T_i.
- Identify the last 40 ps after the field ramp as the final equilibrium region; compute its average temperature T_f.
- Compute raw ΔT = T_f − T_i.
- Scale: scaled ΔT = raw ΔT / 5.

Output the scaled ΔT as a single floating-point number in Kelvin, and provide the complete time series (time, temperature, Px, Py, Pz) as a CSV file.

## Assets

- FERAM (ferroelectric molecular dynamics code): http://loto.sourceforge.net/feram/
- BaTiO3 effective Hamiltonian parameters: 10.1103/PhysRevB.82.134106

## Workflow steps

### Step 1: Microcanonical MD simulation of EC temperature change
- Role: scored (load-bearing)
- Action: Using FERAM with the bulk BaTiO3 effective Hamiltonian, set up a 96×96×96 supercell. Perform a microcanonical (NPE) molecular dynamics simulation: thermalize at 125 K with an applied electric field of 200 kV/cm along [001], then linearly ramp the field to zero, and continue the simulation. Record the system temperature and Cartesian polarization components (Px, Py, Pz) at intervals of 1 ps throughout the entire simulation.
- Output file: `/app/outputs/time_evolution.csv`
- Format: csv
- Contract: Columns: time_ps (float), temperature_K (float), Px (float), Py (float), Pz (float)
- Scoring: scored by hidden verifier

### Step 2: Compute scaled adiabatic EC temperature change
- Role: scored
- Action: From time_evolution.csv, identify the initial equilibrium period (the last 40 ps before the field ramp begins) and the final equilibrium period (the last 40 ps after the ramp ends). Compute the average temperature T_i of the initial period and T_f of the final period. Compute raw ΔT = T_f - T_i, then the scaled ΔT = raw_ΔT / 5. Write this single floating-point number to a text file.
- Output file: `/app/outputs/scaled_delta_T.txt`
- Format: txt
- Contract: A single floating-point number (in Kelvin).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/time_evolution.csv`
- `/app/outputs/scaled_delta_T.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### time_evolution.csv
- path: `/app/outputs/time_evolution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of temperature and polarization components throughout the EC field-ramp simulation; used to verify the occurrence of the phase transition and the inverse caloric effect.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `temperature_K`, `Px`, `Py`, `Pz`

### scaled_delta_T.txt
- path: `/app/outputs/scaled_delta_T.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The scaled adiabatic electrocaloric temperature change (ΔT) computed from the simulation trajectory.
- schema:
  - `type`: text

Notes: The agent must run the full MD simulation; the time_evolution.csv output is the raw artifact that enables both the structural audit of the phase transition and the recomputation of the scaled ΔT.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "time_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "temperature_K",
          "Px",
          "Py",
          "Pz"
        ]
      },
      "description": "Time series of temperature and polarization components throughout the EC field-ramp simulation; used to verify the occurrence of the phase transition and the inverse caloric effect."
    },
    {
      "file": "scaled_delta_T.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "The scaled adiabatic electrocaloric temperature change (ΔT) computed from the simulation trajectory."
    }
  ],
  "notes": "The agent must run the full MD simulation; the time_evolution.csv output is the raw artifact that enables both the structural audit of the phase transition and the recomputation of the scaled ΔT."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that independently inspects both output files. The checks are:

- **Scaled ΔT (heavy weight):** The verifier will recompute the scaled ΔT from your `time_evolution.csv` using the same protocol (averaging the specified last 40-ps windows before and after the ramp) and compare the resulting value against a hidden reference value derived from the underlying physics model. Your reported ΔT will be accepted only if it lies within an expected range consistent with correct execution of the simulation.
- **Phase transition signature (complementary weight):** The verifier will examine the polarization time series in `time_evolution.csv` to confirm that the system undergoes a structural phase transition during the field ramp, as evidenced by a change in the pattern of nonzero polarization components (e.g., from one dominant nonzero component to two). It will also verify that the temperature evolves monotonically during the ramp and that the simulation ran for a sufficient duration.

Meeting the specification of the output contract (correct columns, data range, etc.) is a prerequisite for scoring. You do not need to guess the reference value; run the simulation as described and the result will fall into the accepted range.
