# 2D Iron Spontaneous Crystallization MD Simulation

## Problem background
Free-standing two-dimensional (2D) iron — sometimes called ironene — is a material of intense interest, but its thermodynamically preferred atomic structure has been debated. Experimental observations of 2D iron suspended in graphene pores have reported both a square lattice and a triangular (hexagonal‑close‑packed) lattice, and density‑functional calculations suggest different outcomes depending on the substrate and chemical environment. Large‑scale classical molecular dynamics (MD) simulations can address this question by modelling the spontaneous crystallisation of 2D iron directly from the liquid state without any templating surface. This task aims to reproduce the full simulation pipeline and to extract the key structural and thermodynamic properties that characterise the resulting 2D iron crystal, thereby providing a numerical benchmark for the nature of the formed monolayer.

## Approach
Use LAMMPS (a widely available open‑source MD engine) with an embedded‑atom method (EAM) potential for iron, which is a standard classical force field for metals that captures both cohesive energy and directional bonding. The entire simulation is constrained to a strictly two‑dimensional plane (z = 0). The workflow proceeds in four stages: (1) prepare an initial square‑lattice configuration of Fe atoms; (2) heat the system to a high‑temperature liquid state; (3) cool the liquid under conditions that produce a nanoribbon (periodic along one axis, reflecting wall along the other); and (4) analyse the final low‑temperature configuration and the cooling trajectory to compute a set of structural and thermodynamic quantities — crystallisation temperature, coordination statistics, bond‑angle and nearest‑neighbour distance distributions, total energy per atom, and global bond‑orientation order. The method relies solely on public resources and does not require any external data beyond the EAM potential file, which is bundled with LAMMPS or available from the NIST Interatomic Potentials Repository.

## Reproduction target
Run the MD simulation protocol described in the Workflow steps and produce a single JSON file `/app/outputs/ironene_results.json` containing exactly these six numeric fields derived from the cooling trajectory and the final configuration at 300 K:

- `coordination_percentage_Z6` (float): percentage of atoms with coordination number 6.
- `bond_angle_peak_degrees` (float): peak position of the bond‑angle distribution, in degrees.
- `nearest_neighbor_distance_peak_A` (float): peak position of the nearest‑neighbor distance distribution, in ångströms.
- `crystallization_temperature_K` (float): crystallisation temperature (the temperature of the sharp peak in heat capacity or the inflection point in total energy versus temperature).
- `total_energy_per_atom_eV` (float): total energy per atom at 300 K, in eV.
- `global_bond_orientation_order_Psi6` (float): global bond‑orientation order parameter Ψ₆ at 300 K.

All values must be computed from the aforementioned MD trajectories; simply reporting literature numbers without performing the simulation will not satisfy the verifier.

## Assets

- LAMMPS: https://lammps.sandia.gov/
- EAM potential for iron (e.g., Fe.eam.alloy): https://www.ctcms.nist.gov/potentials/

## Workflow steps

### Step 1: Generate initial 2D square-lattice configuration
- Role: process
- Action: Create a strictly 2D (z=0) configuration of 6400 iron atoms on a square lattice with lattice constant 2.35 Å, suitable for input to LAMMPS. The configuration must use periodic boundary conditions in x and y during the subsequent heating stage.
- Evidence: `/app/outputs/initial_config.data`

### Step 2: Heating simulation to produce 2D liquid at 4300 K
- Role: process
- Action: Run MD in LAMMPS to heat the initial configuration from 50 K to 4300 K at a heating rate of 10^11 K/s under NPT zero pressure with periodic boundaries in x and y. Relax at 4300 K for 10^5 MD steps using a time step of 1.0 fs, the Verlet integrator, and simple velocity rescaling thermostat. Keep the z coordinate fixed at zero. Save the final liquid configuration and trajectory (or at least periodic snapshots) for later analysis.
- Evidence: `/app/outputs/liquid_restart.data`

### Step 3: Cooling simulation to 300 K and formation of nanoribbons
- Role: process
- Action: Cool the liquid from 4300 K down to 300 K at a cooling rate of 2×10^10 K/s in the NVT ensemble. Use periodic boundary conditions only along the x direction and a reflecting fixed wall along y (to form nanoribbons). Relax the final configuration at 300 K for 10^5 MD steps. Save the full cooling trajectory (or periodic snapshots of energies and configurations) and the final atomic configuration at 300 K.
- Evidence: `/app/outputs/final_config.data`

### Step 4: Compute structural and thermodynamic properties from simulation
- Role: scored (load-bearing)
- Action: From the cooling trajectory and the final configuration at 300 K, compute the following quantities: 1) the crystallization temperature TX – determined as the temperature of the sharp peak in the heat capacity (or the inflection point in total energy vs temperature) derived from the per-atom energies recorded during cooling; 2) from the final 300 K configuration: calculate the radial distribution function, identify the first minimum after the first peak as the cutoff radius for neighbour analysis (~3.30 Å), then compute the coordination number distribution (percentage of atoms with Z=6), the bond-angle distribution (peak position in degrees), and the nearest-neighbor distance distribution (peak position in Ångströms); 3) the total energy per atom at 300 K; 4) the global bond-orientation order parameter Ψ6 at 300 K, defined as the average of the local bond-orientation order over all atoms. Save all six results in a single JSON file named ironene_results.json.
- Output file: `/app/outputs/ironene_results.json`
- Format: json
- Contract: JSON object with keys: coordination_percentage_Z6 (float), bond_angle_peak_degrees (float), nearest_neighbor_distance_peak_A (float), crystallization_temperature_K (float), total_energy_per_atom_eV (float), global_bond_orientation_order_Psi6 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ironene_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ironene_results.json
- path: `/app/outputs/ironene_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural and thermodynamic properties computed from the cooling simulation and final configuration. All values must be derived from the MD trajectories as described; they are compared to hidden paper-reported reference values.
- schema:
  - `type`: object
  - `required`: `coordination_percentage_Z6`, `bond_angle_peak_degrees`, `nearest_neighbor_distance_peak_A`, `crystallization_temperature_K`, `total_energy_per_atom_eV`, `global_bond_orientation_order_Psi6`

Notes: The hidden checker compares each numerical field against the paper's reported values using tolerances appropriate for molecular dynamics reproducibility. All quantities are obtained from the same simulation protocol; no external data beyond the listed resources is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ironene_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "coordination_percentage_Z6",
          "bond_angle_peak_degrees",
          "nearest_neighbor_distance_peak_A",
          "crystallization_temperature_K",
          "total_energy_per_atom_eV",
          "global_bond_orientation_order_Psi6"
        ]
      },
      "description": "Structural and thermodynamic properties computed from the cooling simulation and final configuration. All values must be derived from the MD trajectories as described; they are compared to hidden paper-reported reference values."
    }
  ],
  "notes": "The hidden checker compares each numerical field against the paper's reported values using tolerances appropriate for molecular dynamics reproducibility. All quantities are obtained from the same simulation protocol; no external data beyond the listed resources is required."
}
```

## How you are scored
Your submitted `ironene_results.json` will be evaluated by a hidden automated checker. The checker compares each of the six required fields against reference values (derived from published results) using pre‑defined, loose‑but‑reasonable tolerances that account for the inherent run‑to‑run variability of molecular dynamics with different build and numerical settings. You receive a score equal to the fraction of fields that fall within the tolerance interval. Reporting numbers that were not genuinely obtained from the described MD workflow will almost certainly fall outside the hidden tolerances and lead to a low score. Therefore, honest execution of all process and analysis steps is essential; partial or manually‑constructed submissions will not achieve a high reward.
