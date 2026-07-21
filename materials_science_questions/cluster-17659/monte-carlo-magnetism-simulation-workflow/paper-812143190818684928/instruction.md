# Compute Vortex Lattice Melting Temperature from Langevin Molecular Dynamics Simulation

## Problem background
High-temperature superconductors such as BSCCO host a lattice of magnetic flux lines (vortices). At low temperatures the repulsive interactions between vortices order them into a triangular Abrikosov lattice. As temperature increases, thermal fluctuations cause the lattice to melt, destroying crystalline order. Understanding the melting temperature is central to mapping the phase diagram of these materials. In highly anisotropic layered superconductors, each flux line can be described as a stack of "pancake vortices" residing in the superconducting layers. Molecular dynamics simulations that track the overdamped Langevin motion of these pancakes, including realistic electromagnetic and Josephson interactions, can capture the melting transition. This task re‑implements such a simulation and extracts the melting temperature via the Lindemann criterion.

## Approach
The simulation follows the overdamped Langevin equation of motion for pancake vortices interacting through in‑plane and out‑of‑plane electromagnetic forces and through a nearest‑neighbor Josephson coupling. Periodic boundary conditions are applied in all three spatial directions. The electromagnetic pair potential is a long‑range in‑plane repulsion and an inter‑plane attraction; the Josephson interaction is an attractive force between adjacent planes that grows approximately quadratically with transverse displacement for small separations and linearly for larger ones. The simulation cell contains 36 flux lines and 36 layers. The magnetic field is set to B = 100 G and the anisotropy to γ = 400, with material parameters for BSCCO: zero‑temperature penetration depth λ₀ = 1700 Å, interlayer spacing d = 15 Å, and critical temperature T_c = 90 K. The penetration depth follows the two‑fluid temperature dependence λ(T) = λ₀ / √(1 − T/T_c). The lattice constant a₀ = √(2ϕ₀ / B√3) determines the transverse cell dimensions, which are chosen to accommodate a perfect triangular lattice. Interaction tables (periodic Green’s functions, their gradients, and the Josephson potential with its gradient) are pre‑computed on a fine mesh and used for force evaluation during the simulation. The system is equilibrated and then production runs are performed at a series of temperatures (e.g., 60 K to 80 K in 2 K steps). For each temperature, the mean‑square transverse deviation of flux lines from their centre of mass, ⟨R_f²⟩, is measured. The melting temperature is identified as the temperature where the Lindemann parameter c_L = √(⟨R_f²⟩) / a₀ first reaches or exceeds 0.25.

## Reproduction target
Compute the vortex lattice melting temperature for magnetic field B = 100 G and anisotropy γ = 400. Use the Lindemann criterion: the melting point is the lowest temperature at which the dimensionless parameter c_L = √(⟨R_f²⟩) / a₀ is ≥ 0.25. Report the temperature in Kelvin in the output file.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Langevin Molecular Dynamics Simulation
- Role: process
- Action: Implement the overdamped Langevin dynamics for 36 flux lines and 36 layers at B=100 G, gamma=400, using the electromagnetic and Josephson interaction potentials with periodic boundary conditions in all directions. Precompute interaction lookup tables (periodic Green's functions, their gradients, Josephson potential and gradient). Equilibrate and run production simulations at a range of temperatures (e.g., 60 K to 80 K in 2 K steps), recording pancake trajectories for each temperature.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Melting Temperature Determination
- Role: scored (load-bearing)
- Action: For each simulated temperature, compute the mean square transverse deviation R_f^2 of flux lines from their center of mass, then the Lindemann parameter cL = sqrt(R_f^2)/a0. Determine the melting temperature as the temperature where cL first reaches or exceeds 0.25. Output this temperature in Kelvin.
- Output file: `/app/outputs/melting_temperature.json`
- Format: json
- Contract: {"melting_temperature_K": <number>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/melting_temperature.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### melting_temperature.json
- path: `/app/outputs/melting_temperature.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The melting temperature in Kelvin, determined from the Langevin simulation via the Lindemann criterion (cL >= 0.25).
- schema:
  - `type`: object
  - `required`:
    - `melting_temperature_K`: number
  - `units`:
    - `melting_temperature_K`: Kelvin

Notes: The checker compares the reported melting_temperature_K against the paper's reference value for B=100 G, gamma=400, with a tolerance that accounts for stochastic variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "melting_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "melting_temperature_K": "number"
        },
        "units": {
          "melting_temperature_K": "Kelvin"
        }
      },
      "description": "The melting temperature in Kelvin, determined from the Langevin simulation via the Lindemann criterion (cL >= 0.25)."
    }
  ],
  "notes": "The checker compares the reported melting_temperature_K against the paper's reference value for B=100 G, gamma=400, with a tolerance that accounts for stochastic variation."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects every stage of your workflow. The primary scored artifact is the melting temperature you write to **melting_temperature.json**. The verifier compares your computed temperature to a hidden reference derived from the original study, using an appropriate tolerance that accounts for legitimate run‑to‑run and implementation variation. The **simulation_log.txt** produced by the process step may be checked for consistency and evidence that the simulation was genuinely executed. Reporting a number without having run the full simulation pipeline will not pass. Each stage’s evidence is weighted; the melting temperature is the dominant scored quantity.
