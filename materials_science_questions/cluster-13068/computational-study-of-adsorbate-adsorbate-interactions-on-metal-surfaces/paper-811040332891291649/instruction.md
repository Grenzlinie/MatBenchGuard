# Molecular Dynamics Study of Ar Scattering on Ag(111) — Angular Width and Sticking Probability

## Problem background
Understanding the scattering of atoms from metal surfaces is fundamental to gas‑surface dynamics. For systems like Ar on Ag(111), the interaction potential governs energy transfer, angular distributions, and trapping/sticking. A pairwise‑additive potential energy surface (PES) derived from first‑principles calculations can, in principle, describe scattering across a wide range of incidence energies and surface temperatures without fitting to experimental data. The challenge is to implement this PES and a realistic crystal model in a molecular dynamics simulation, and then compute two key observables: the angular width of the scattered flux (which probes corrugation and energy transfer) and the sticking probability (which captures trapping and penetration). The results for a static lattice and a surface thermalized at 600 K are to be obtained as a function of incidence energy, from thermal energies up to the penetration regime.

## Approach
The core idea is to model the Ar–Ag(111) interaction as a sum of repulsive pair potentials and a surface‑localised attractive correction. The repulsion is described by a Born–Mayer exponential, while the attractive well is given by a Z‑dependent term attached to individual surface atoms to permit energy exchange. The Ag(111) crystal is built as a large slab with nearest‑neighbour anharmonic interactions; force constants are computed from tabulated Debye temperatures. Classical molecular dynamics is then used to propagate an Ar atom approaching the surface at a fixed incidence angle and azimuth. Two surface preparations are examined: a static lattice (atoms initially at equilibrium, allowed to recoil) and a thermalised 600 K lattice (displaced and moving with Boltzmann statistics). For each incidence energy, many independent trajectories are run with varying impact parameters. From the final velocities and exit angles of atoms that leave the surface, the angular width is computed via the moment definition (two standard deviations of the in‑plane angular distribution). Sticking probability is estimated as the fraction of atoms that do not escape within the simulation time window. The required output files summarise these quantities across the requested energy range.

## Reproduction target
Produce three CSV files that list the angular width and sticking probability as functions of incidence energy. For a static Ag(111) surface, compute the angular width 2Δθ<sub>f</sub> (in degrees) for incidence energies of 0.03, 0.1, 0.5, 1, 10, and 100 eV. Repeat the width calculation for a surface thermalised at 600 K. Additionally, for the 600 K surface, compute the sticking probability (a dimensionless fraction between 0 and 1) at the same six energies. All simulations use an incidence angle of 40° from the surface normal along the [10‑1] azimuth, and only in‑plane scattered atoms are considered. The columns of the CSVs are `incidence_energy_eV` and `angular_width_deg` (for the two width files) or `incidence_energy_eV` and `sticking_probability` (for the sticking file).

## Assets

- LAMMPS: https://www.lammps.org/
- Python scientific stack: numpy, pandas, matplotlib, scipy

## Workflow steps

### Step 1: Calculate crystal force constants
- Role: process
- Action: Compute the harmonic and anharmonic force constants k1, k2, k3 for bulk and surface Ag atoms. Use the Debye temperatures (225 K bulk, 104 K surface), Ag atomic mass, equilibrium nearest-neighbor distance d = a/√2 with a = 4.09 Å, and the relations: ⟨u²⟩ = 3ħ²T/(M_Ag k_B Θ²), k1 = (3/8) M_Ag (k_B Θ/ħ)², k2 = -(21/(2d)) k1, k3 = (371/(6d²)) k1. These define the anharmonic nearest-neighbor potential.

### Step 2: Implement Ar-Ag(111) potential energy surface
- Role: process
- Action: Implement the total Ar-Ag(111) PES V_tot(R) as a sum over all crystal atoms of a Born-Mayer repulsive pair term V_BM(ρ_i) = A exp(−α ρ_i) with A = 10608.0 eV, α = 4.2487 Å⁻¹, plus an atom-linked Z-dependent attractive correction. The correction for each surface atom i is V_Z(R_i) = W(Z_i) * exp(−σ (X_i²+Y_i²)) / Σ_k exp(−σ (X_k²+Y_k²)), where W(Z) = −B (Z−z₀) exp(−γ Z⁴) with B = 1.28 eV·Å⁻¹, z₀ = 2.6 Å, γ = 0.0183 Å⁻⁴, and lateral weighting parameter σ = 0.149 Å⁻². Attach the attractive contribution to individual surface atoms to allow energy transfer during dynamics.

### Step 3: Run molecular dynamics simulations
- Role: process
- Action: Set up a 25×25×5 Ag(111) crystal with nearest-neighbor anharmonic interactions and fixed edge atoms. For each of the incidence energies 0.03, 0.1, 0.5, 1, 10, 100 eV, run classical MD trajectories of Ar atoms impinging at 40° from the surface normal along the [10-1] azimuth. Run separate ensembles for a static surface (crystal atoms initially at equilibrium positions, no initial velocities but allowed to recoil) and a surface thermalized at 600 K (Boltzmann-distributed displacements and velocities after equilibration). Use approximately 10,000 trajectories per energy for the static case and 30,000 for the 600 K case, terminating when the Ar atom reaches 5.25 Å above the surface, approaches within 5 atoms of the crystal edge, or undergoes more than 10 collisions. Record for each scattered atom its final velocity, exit angle, and number of turning points.

### Step 4: Compute angular width and sticking probability
- Role: scored (load-bearing)
- Action: From the MD trajectory data, compute for each incidence energy the angular width 2Δθ_f using the moment definition (2√(⟨θ_f²⟩ − ⟨θ_f⟩²) over all in-plane scattered atoms that exited the surface), separately for the static and 600 K cases. Also compute the sticking probability as the fraction of launched atoms that did not escape the surface within the simulation time (i.e., those that reached the crystal edge or exceeded 10 collisions), for the 600 K case. Write the results to the three CSV files.
- Output file: `/app/outputs/angular_width_static.csv, angular_width_600K.csv, sticking_probability_600K.csv`
- Format: csv
- Contract: angular_width_static.csv: columns incidence_energy_eV (float), angular_width_deg (float). angular_width_600K.csv: same schema. sticking_probability_600K.csv: columns incidence_energy_eV (float), sticking_probability (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/angular_width_static.csv`
- `/app/outputs/angular_width_600K.csv`
- `/app/outputs/sticking_probability_600K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### angular_width_static.csv
- path: `/app/outputs/angular_width_static.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Angular width 2Δθ_f (in degrees) for in-plane scattering from a static Ag(111) surface at each incidence energy.
- schema:
  - `required_columns`: `incidence_energy_eV`, `angular_width_deg`
  - `units`:
    - `incidence_energy_eV`: eV
    - `angular_width_deg`: degree

### angular_width_600K.csv
- path: `/app/outputs/angular_width_600K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Angular width 2Δθ_f (in degrees) for in-plane scattering from a Ag(111) surface at 600 K at each incidence energy.
- schema:
  - `required_columns`: `incidence_energy_eV`, `angular_width_deg`
  - `units`:
    - `incidence_energy_eV`: eV
    - `angular_width_deg`: degree

### sticking_probability_600K.csv
- path: `/app/outputs/sticking_probability_600K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sticking probability (fraction of atoms that do not escape the surface) for a 600 K surface at each incidence energy.
- schema:
  - `required_columns`: `incidence_energy_eV`, `sticking_probability`
  - `units`:
    - `incidence_energy_eV`: eV
    - `sticking_probability`: dimensionless (fraction)

Notes: The hidden checker compares the agent’s reported angular widths and sticking probabilities to paper-derived reference values with tolerances that absorb implementation spread and resist guessing. Trends (e.g., minimum near 1 eV, sticking decrease below 1 eV then rise above 10 eV) are also checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "angular_width_static.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "incidence_energy_eV",
          "angular_width_deg"
        ],
        "units": {
          "incidence_energy_eV": "eV",
          "angular_width_deg": "degree"
        }
      },
      "description": "Angular width 2*Delta*theta_f (in degrees) for in-plane scattering from a static Ag(111) surface at each incidence energy."
    },
    {
      "file": "angular_width_600K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "incidence_energy_eV",
          "angular_width_deg"
        ],
        "units": {
          "incidence_energy_eV": "eV",
          "angular_width_deg": "degree"
        }
      },
      "description": "Angular width 2*Delta*theta_f (in degrees) for in-plane scattering from a Ag(111) surface at 600 K at each incidence energy."
    },
    {
      "file": "sticking_probability_600K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "incidence_energy_eV",
          "sticking_probability"
        ],
        "units": {
          "incidence_energy_eV": "eV",
          "sticking_probability": "dimensionless (fraction)"
        }
      },
      "description": "Sticking probability (fraction of atoms that do not escape the surface) for a 600 K surface at each incidence energy."
    }
  ],
  "notes": "The hidden checker compares the agent’s reported angular widths and sticking probabilities to paper-derived reference values with tolerances that absorb implementation spread and resist guessing. Trends (e.g., minimum near 1 eV, sticking decrease below 1 eV then rise above 10 eV) are also checked."
}
```

## How you are scored
After your run completes, a hidden verifier reads the three CSV files and independently evaluates each one. The verifier checks your reported angular widths and sticking probabilities against reference values and expected physical trends (e.g. the dependence of the width on incidence energy, the relative changes between a static and a thermalised surface). Each scored output carries a weight, and the final reward (between 0 and 1) is the weighted sum. To earn full credit, your results must be consistent with the physics of the system as captured by the implemented potential and simulation protocol described in this instruction. It is not sufficient to merely report numbers that happen to match a target; the pipeline steps must be genuinely executed and the evidence artifacts must be present under `/app/outputs`. The verifier does **not** reveal its tolerances or reference values, so you must trust the simulation workflow rather than attempting to guess the answer.