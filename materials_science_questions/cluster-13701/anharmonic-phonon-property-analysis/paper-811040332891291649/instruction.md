# Ar–Ag(111) Scattering Molecular Dynamics Reproduction

## Problem background
Gas–surface scattering involves a wide range of collision regimes, from thermal scattering where the surface appears smooth to structure scattering where the atomic corrugation produces rainbow features.  Accurately reproducing the angular distributions, energy transfer, and sticking probabilities across incidence energies spanning several orders of magnitude requires a realistic potential energy surface (PES) and a dynamics model that includes the collective motion of many surface atoms.  The Ar–Ag(111) system is a prototypical test case:  a pairwise‑additive PES derived from local‑density‑approximation calculations, augmented with a position‑dependent attractive correction, can be evaluated by classical molecular dynamics (MD) simulations.  This task implements such a simulation to compute the angular width of the in‑plane scattering distribution and the sticking probability for an Ar beam impinging on Ag(111) at a fixed incidence angle, covering both a static (0 K) surface and a 600 K surface over a wide range of incidence energies.  The results probe the transition between thermal and structure scattering, the role of surface temperature, and the occurrence of multiple collisions and trapping.

## Approach
The approach uses a large‑scale classical molecular dynamics simulation with a realistic crystal model and a physically motivated Ar–Ag(111) interaction potential.  The Ag(111) crystal is represented as a 3125‑atom slab with nearest‑neighbour anharmonic interactions; harmonic and anharmonic force constants are derived from the Debye temperatures of the surface and the bulk.  The Ar–surface interaction is a pairwise additive potential that consists of a Born–Mayer repulsive pair potential summed over all crystal atoms and an atom‑linked Z‑dependent attractive correction summed over the surface atoms.  The correction accounts for the delocalized surface electrons and introduces a shallow attractive well.  All parameters of the interaction potential are fixed by published first‑principles fits, with no adjustable parameters tuned to experimental data.

Trajectories are propagated with the velocity Verlet integrator.  For each chosen incidence energy and surface temperature, many independent trajectories are launched with the Ar atom starting far above the surface at a fixed incidence angle.  A trajectory is considered ‘scattered’ when the Ar atom returns to a detection height above the surface; otherwise it is classified as non‑escaping (trapped or implanted).  From the final kinetic energies and in‑plane exit angles of all scattered trajectories, the angular intensity distribution is constructed and its width is computed using the second central moment.  The sticking probability is taken as the fraction of trajectories that do not escape within the simulation time.  The same procedure is applied to a static (0 K) surface and to a surface thermalised at 600 K.

## Reproduction target
The target is to produce three scored artifacts located under `/app/outputs`:

1. `relative_energy_data.csv` – raw trajectory data.  For each incidence energy (0.1, 0.5, 1.0, 2.6, 10.0, 100.0 eV) and surface temperature (0 K and 600 K), list every scattered trajectory with its final kinetic energy (eV) and in‑plane exit angle (degrees).

2. `angular_widths.csv` – the angular width (2 √(⟨θ_f²⟩−⟨θ_f⟩²)) computed from the scattered exit‑angle distribution for every combination of incidence energy and surface temperature.

3. `sticking_probability.csv` – the sticking probability (fraction of non‑escaping trajectories) as a function of incidence energy for the 600 K surface.

The raw trajectory file must be sufficiently rich that an independent checker can recompute the angular widths and inspect the angular distributions for structural signatures of the scattering regime.  The computed angular widths and sticking probabilities should reflect the physical behaviour expected from the implemented potential and crystal model.

## Assets

- Python scientific computing libraries (NumPy, SciPy, h5py): numpy scipy h5py

## Workflow steps

### Step 1: Crystal model and force-constant preparation
- Role: process
- Action: Calculate harmonic and anharmonic force constants (k1, k2, k3) for surface and bulk atoms using the Debye temperatures (surface 104 K, bulk 225 K) and Lennard-Jones expansion coefficients. Build a 3125-atom fcc(111) slab with 25×25 surface atoms, 5 layers, fixed edge atoms, and nearest-neighbour interactions. Write the computed force constants as evidence.
- Evidence: `/app/outputs/force_constants.txt`

### Step 2: Ar–Ag(111) potential energy surface implementation
- Role: process
- Action: Implement the total potential V_tot(R) as a sum of Born-Mayer repulsive pair terms over all crystal atoms and an atom-linked Z-dependent attractive correction over all surface atoms, using the published parameters (A=10608.0 eV, α=4.2487 Å⁻¹, B=1.28 eV Å⁻¹, z₀=2.6 Å, γ=0.0183 Å⁻⁴, σ=0.149 Å⁻²) and functional forms. The routine must accept arbitrary crystal atom positions.
- Evidence: none

### Step 3: Molecular dynamics trajectory generation
- Role: scored (load-bearing)
- Action: Run classical MD simulations with velocity Verlet integration for Ar atoms impinging on the Ag(111) surface at incidence energies [0.1, 0.5, 1.0, 2.6, 10.0, 100.0] eV, a fixed 40° incidence angle along the [10-1] azimuth, for a static surface and a surface at 600 K. For the static surface run at least 10 000 trajectories per energy; for the 600 K surface run at least 30 000 trajectories per energy. Thermalise the 600 K crystal before impact. For every scattered trajectory that escapes (Ar returns to 5.25 Å above the surface), record the final kinetic energy and the in-plane exit angle. Output all collected raw trajectory data.
- Output file: `/app/outputs/relative_energy_data.csv`
- Format: csv
- Contract: columns: incidence_energy_eV (float), surface_temperature_K (int), trajectory_id (int), final_energy_eV (float), exit_angle_deg (float)
- Scoring: scored by hidden verifier

### Step 4: Angular width calculation
- Role: scored
- Action: From the raw trajectory data, compute the angular width 2√(⟨θ_f²⟩−⟨θ_f⟩²) for each incidence energy and both surface temperatures (static and 600 K). Use all scattered trajectories within the in-plane detector acceptance. Write the computed angular widths.
- Output file: `/app/outputs/angular_widths.csv`
- Format: csv
- Contract: columns: incidence_energy_eV (float), surface_temperature_K (int), angular_width_deg (float)
- Scoring: scored by hidden verifier

### Step 5: Sticking probability calculation
- Role: scored
- Action: For the 600 K surface, determine the sticking probability as the fraction of trajectories that did not escape (reached the crystal edge, exceeded 10 turning points, or never returned to 5.25 Å) for each incidence energy. Write the per-energy probabilities.
- Output file: `/app/outputs/sticking_probability.csv`
- Format: csv
- Contract: columns: incidence_energy_eV (float), sticking_probability (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energy_data.csv`
- `/app/outputs/angular_widths.csv`
- `/app/outputs/sticking_probability.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energy_data.csv
- path: `/app/outputs/relative_energy_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw trajectory data from the MD simulation. Each row records the final energy and exit angle of one scattered trajectory for a given incidence energy and surface temperature. The checker uses this file to verify the presence of surface rainbows (multiple peaks in the angular distribution for static surface at 0.1 eV) and as the basis for recomputing the angular width.
- schema:
  - `type`: table
  - `required_columns`: `incidence_energy_eV`, `surface_temperature_K`, `trajectory_id`, `final_energy_eV`, `exit_angle_deg`
  - `units`:
    - `incidence_energy_eV`: eV
    - `surface_temperature_K`: K
    - `final_energy_eV`: eV
    - `exit_angle_deg`: degree

### angular_widths.csv
- path: `/app/outputs/angular_widths.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed angular width (2Δθ_f) for each combination of incidence energy and surface temperature (static=0 K, finite=600 K). The checker recomputes the angular width from the raw trajectory data and compares it to a hidden reference within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `incidence_energy_eV`, `surface_temperature_K`, `angular_width_deg`
  - `units`:
    - `incidence_energy_eV`: eV
    - `surface_temperature_K`: K
    - `angular_width_deg`: degree

### sticking_probability.csv
- path: `/app/outputs/sticking_probability.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sticking probability as a function of incidence energy for the 600 K surface. The checker compares these values to a hidden reference (paper‑reported trend) with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `incidence_energy_eV`, `sticking_probability`
  - `units`:
    - `incidence_energy_eV`: eV
    - `sticking_probability`: fraction

Notes: The raw trajectory file is load‑bearing: a correct angular width and the structural rainbow audit cannot be reproduced without a physically meaningful simulation. The agent must execute the full MD workflow; no pre‑computed trajectory data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energy_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "incidence_energy_eV",
          "surface_temperature_K",
          "trajectory_id",
          "final_energy_eV",
          "exit_angle_deg"
        ],
        "units": {
          "incidence_energy_eV": "eV",
          "surface_temperature_K": "K",
          "final_energy_eV": "eV",
          "exit_angle_deg": "degree"
        }
      },
      "description": "Raw trajectory data from the MD simulation. Each row records the final energy and exit angle of one scattered trajectory for a given incidence energy and surface temperature. The checker uses this file to verify the presence of surface rainbows (multiple peaks in the angular distribution for static surface at 0.1 eV) and as the basis for recomputing the angular width."
    },
    {
      "file": "angular_widths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "incidence_energy_eV",
          "surface_temperature_K",
          "angular_width_deg"
        ],
        "units": {
          "incidence_energy_eV": "eV",
          "surface_temperature_K": "K",
          "angular_width_deg": "degree"
        }
      },
      "description": "Computed angular width (2Δθ_f) for each combination of incidence energy and surface temperature (static=0 K, finite=600 K). The checker recomputes the angular width from the raw trajectory data and compares it to a hidden reference within a tolerance."
    },
    {
      "file": "sticking_probability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "incidence_energy_eV",
          "sticking_probability"
        ],
        "units": {
          "incidence_energy_eV": "eV",
          "sticking_probability": "fraction"
        }
      },
      "description": "Sticking probability as a function of incidence energy for the 600 K surface. The checker compares these values to a hidden reference (paper‑reported trend) with a tolerance."
    }
  ],
  "notes": "The raw trajectory file is load‑bearing: a correct angular width and the structural rainbow audit cannot be reproduced without a physically meaningful simulation. The agent must execute the full MD workflow; no pre‑computed trajectory data is provided."
}
```

## How you are scored
Your submission is scored by a hidden verifier that processes the artifacts in `/app/outputs`.  Each scored output is checked independently, and the final reward is a weighted combination of the stage scores.

- **Angular width** (`angular_widths.csv`):  the verifier recomputes the angular width from the raw trajectory data and compares the values to a hidden reference.  The check rewards angular widths that meet or exceed a reference trend; the comparison uses a tolerance that accommodates the natural variance of independent implementations.

- **Sticking probability** (`sticking_probability.csv`):  the reported probabilities are compared to a hidden reference.  The check rewards values that agree with the reference within an appropriate tolerance.

- **Raw trajectory data** (`relative_energy_data.csv`):  the verifier performs a structural audit on the angular distributions.  For the static surface at the lowest incidence energy, the distribution must show at least two distinct peaks (surface rainbows).  For the 600 K case at the same energy, a single broad peak is expected.  The angular width recomputation also cross‑checks the consistency of this file.

Meeting or exceeding the paper‑reported quality level (lower angular width error, correct trend) is never penalised.  The scoring rewards implementations that faithfully capture the scattering physics; fabricating numbers will not pass the structural checks and the recomputation from raw data.
