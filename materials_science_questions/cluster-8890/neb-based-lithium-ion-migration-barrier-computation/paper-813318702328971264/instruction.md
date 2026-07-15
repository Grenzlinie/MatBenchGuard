# LiCoO2 Near-Σ2 Twin Boundary Energy and Li Ion Migration Barriers

## Problem background
The capacity and stability of LiCoO₂ cathodes in lithium-ion batteries are influenced by microstructural features such as grain boundaries. In thin-film and nano-scale materials, interfaces can alter Li-ion transport and thermodynamic stability. This work addresses a high-coincidence twin boundary observed in LiCoO₂ films. Atomistic simulations are used to determine the boundary's structure, its excess energy, and its impact on Li-ion migration barriers. Understanding these interfacial properties is important for optimizing cathode materials.

## Approach
Classical atomistic simulations are performed using the open-source GULP code and the Hart‑Bates two-body potential for LiCoO₂. The R‑3m crystal structure is used as the starting point. A bicrystal model of the near‑Σ2 (1̄104)/[44̄01] twist boundary is built by bisecting a perfect crystal and rotating one half by 180° about the interface normal. A systematic rigid‑body translation search (over 200 configurations) with energy minimization identifies the minimum‑energy grain boundary structure. From the relaxed boundary and a corresponding free‑surface slab, the grain boundary excess energy, the (1̄104) surface energy, and the work of cohesion are computed. Li‑ion migration energy barriers are then evaluated for two vacancy‑mediated mechanisms — octahedral‑octahedral (O‑O) and octahedral‑tetrahedral‑octahedral (O‑T‑O) — at increasing distances from the interface, covering both oblique and parallel trajectories. The Mott‑Littleton method is used to determine saddle‑point energies.

## Reproduction target
Compute the following quantities for the near‑Σ2 (1̄104)/[44̄01] twist boundary in LiCoO₂ using the Hart‑Bates potential and the GULP code:

* Grain boundary excess energy (J/m²).
* Surface energy of the free (1̄104) termination (J/m²).
* Work of cohesion derived from the boundary and surface energies (J/m²).
* Li‑ion migration activation energies (eV) for the O‑O and O‑T‑O mechanisms at distances of 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, and 1.2 nm from the interface, for trajectories oblique and parallel to the boundary. For the O‑T‑O mechanism, consider both sub‑cases where the extra vacancy lies on the boundary side or on the bulk side.

Report the energies in the specified output files: `step_01_boundary_energy.json` (for the three energies) and `step_02_migration_barriers.csv` (for the migration barriers).

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/
- Hart-Bates two-body potential parameters for LiCoO2: 10.1063/1.367672
- LiCoO2 crystal structure (R-3m)

## Workflow steps

### Step 1: Validate the potential against bulk lattice parameters
- Role: process
- Action: Using GULP and the Hart-Bates potential, perform an energy minimization of the R-3m LiCoO2 structure and compute the optimized lattice parameters. Confirm that the error relative to the experimental reference (a=2.815 Å, c=14.05 Å, c/a=4.99) is acceptably small.
- Evidence: `/app/outputs/potential_validation.log`

### Step 2: Validate bulk Li-ion migration barriers
- Role: process
- Action: Using the validated potential, calculate the Li-ion migration energy barriers in bulk LiCoO2 for the O-O (octahedral-to-octahedral) and O-T-O (octahedral-tetrahedral-octahedral) mechanisms using the Mott-Littleton method in GULP. Verify that the computed barriers are consistent with published DFT reference values (O-O ~0.74 eV, O-T-O ~0.23 eV).
- Evidence: `/app/outputs/bulk_migration.log`

### Step 3: Construct the near-Σ2 twist boundary bicrystal model
- Role: process
- Action: Build an initial bicrystal model (576 atoms) by bisecting the bulk LiCoO2 crystal and rotating one half by 180° about the [44̄01] axis, with the (1̄104) plane as the interface. This creates the near-Σ2 coincident site lattice (CSL) configuration.
- Evidence: `/app/outputs/initial_model.gin`

### Step 4: Find the minimum-energy grain boundary structure via rigid-body translation search
- Role: process
- Action: Systematically translate one crystal relative to the other in increments of about 0.5 Å in two orthogonal directions parallel to the interface. For each translation (at least 200 configurations), perform an energy minimization using GULP with fixed in-plane dimensions and 3D periodic boundary conditions. Identify the lowest-energy symmetrical configuration as the relaxed grain boundary structure.
- Evidence: `/app/outputs/gb_minimization.log`

### Step 5: Compute grain boundary energy, surface energy, and work of cohesion
- Role: scored (load-bearing)
- Action: From the relaxed grain boundary structure, compute the grain boundary excess energy (J/m²). Construct a slab model for the free (1̄104) surface and calculate its energy (J/m²) using the same potential. Combine the two values to obtain the work of cohesion (J/m²). Save the three energies to step_01_boundary_energy.json.
- Output file: `/app/outputs/step_01_boundary_energy.json`
- Format: json
- Contract: { "grain_boundary_energy": <float, J/m²>, "surface_energy": <float, J/m²>, "work_of_cohesion": <float, J/m²> }
- Scoring: scored by hidden verifier

### Step 6: Compute Li ion migration barriers near the grain boundary
- Role: scored (load-bearing)
- Action: Using the relaxed grain boundary structure, calculate Li ion migration energy barriers for both the O-O and O-T-O mechanisms at increasing distances from the interface plane. For the O-T-O mechanism, consider both sub-cases where the extra vacancy is on the boundary side or the bulk side. Cover distances of 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2 nm for trajectories oblique and parallel to the boundary. Save the results to step_02_migration_barriers.csv.
- Output file: `/app/outputs/step_02_migration_barriers.csv`
- Format: csv
- Contract: CSV with columns: distance_from_interface (float, nm), mechanism (string, one of 'O-O' or 'O-T-O_boundary_vac' or 'O-T-O_bulk_vac'), activation_energy (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_boundary_energy.json`
- `/app/outputs/step_02_migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_boundary_energy.json
- path: `/app/outputs/step_01_boundary_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed grain boundary excess energy, free (1̄104) surface energy, and work of cohesion for the near-Σ2 twist boundary.
- schema:
  - `type`: object
  - `required`:
    - `grain_boundary_energy`: float (J/m²)
    - `surface_energy`: float (J/m²)
    - `work_of_cohesion`: float (J/m²)
  - `units`:
    - `grain_boundary_energy`: J/m²
    - `surface_energy`: J/m²
    - `work_of_cohesion`: J/m²

### step_02_migration_barriers.csv
- path: `/app/outputs/step_02_migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Li ion migration activation energies for O-O and O-T-O mechanisms at various distances from the grain boundary interface.
- schema:
  - `type`: table
  - `required_columns`: `distance_from_interface`, `mechanism`, `activation_energy`
  - `items`:
    - `distance_from_interface`: float (nm)
    - `mechanism`: string (one of O-O, O-T-O_boundary_vac, O-T-O_bulk_vac)
    - `activation_energy`: float (eV)
  - `units`:
    - `distance_from_interface`: nm
    - `activation_energy`: eV

Notes: The d-spacing profile analysis is qualitative and not included in scoring. The scoring scheme compares computed energies and barriers to hidden gold values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_boundary_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "grain_boundary_energy": "float (J/m²)",
          "surface_energy": "float (J/m²)",
          "work_of_cohesion": "float (J/m²)"
        },
        "units": {
          "grain_boundary_energy": "J/m²",
          "surface_energy": "J/m²",
          "work_of_cohesion": "J/m²"
        }
      },
      "description": "Computed grain boundary excess energy, free (1̄104) surface energy, and work of cohesion for the near-Σ2 twist boundary."
    },
    {
      "file": "step_02_migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_from_interface",
          "mechanism",
          "activation_energy"
        ],
        "items": {
          "distance_from_interface": "float (nm)",
          "mechanism": "string (one of O-O, O-T-O_boundary_vac, O-T-O_bulk_vac)",
          "activation_energy": "float (eV)"
        },
        "units": {
          "distance_from_interface": "nm",
          "activation_energy": "eV"
        }
      },
      "description": "Li ion migration activation energies for O-O and O-T-O mechanisms at various distances from the grain boundary interface."
    }
  ],
  "notes": "The d-spacing profile analysis is qualitative and not included in scoring. The scoring scheme compares computed energies and barriers to hidden gold values with appropriate tolerances."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads your output files. The verifier compares your computed grain boundary energy, surface energy, and work of cohesion to reference values obtained from a correct reproduction run, using appropriate tolerances. For the migration barriers, the verifier checks the reported activation energies at each distance and mechanism against reference values, and verifies that the barriers exhibit a monotonic trend as a function of distance from the interface. Each scored artifact (step 5 and step 6) contributes a weighted fraction to the final reward, which is a single number between 0 and 1. Simply writing down the paper's numbers without executing the required simulation workflow will not satisfy the consistency checks, because the verifier expects values that genuinely result from the described procedure.
