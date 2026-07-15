# Molecular Statics Study of Wrinklon Metastable States in Graphene

## Problem background
Graphene is the thinnest known membrane, with extremely high in-plane stiffness but very low bending rigidity, making it prone to forming wrinkles under compressive in-plane strain. When a graphene nanoribbon is clamped at its edges and subjected to biaxial strain, the boundary conditions impose a specific wrinkle wavelength near the clamped edge, while farther away, longer wavelengths become energetically favorable. The transition regions where the wrinkle wavelength changes are called wrinklons. Understanding how different initial wrinkle-wavelength transitions lead to different metastable equilibrium configurations and affect the transition-region energy is crucial for strain engineering of graphene's mechanical and electronic properties. This work computationally explores the equilibrium configurations that arise from two distinct initial wrinklon patterns and examines their transition-region energies and spatial displacement profiles.

## Approach
Construct a rectangular computational cell for a graphene nanoribbon with zigzag edges in the x-direction and armchair edges in the y-direction. The nanoribbon is modeled with M unit cells in width and N cells in length, using the equilibrium carbon–carbon bond length ρ₀=1.418 Å. The system is subjected to biaxial in‑plane strain εxx⁰ and εyy⁰, which update the cell dimensions. Periodic boundary conditions are applied along the y‑direction; displacements are clamped to zero at the far end (n=N) and mirror symmetry is imposed at the opposite end (n=0), effectively simulating a half-ribbon with two clamped ends. The interatomic interactions are described by the AIREBO potential (or an equivalent that yields ρ₀=1.418 Å). Two initial out‑of‑plane displacement patterns are introduced as sinusoidal waves: a long‑wavelength region near the unclamped end (λ₁ equal to the ribbon width) and a shorter‑wavelength region near the clamped end (λ₂ = λ₁/2 for the first configuration and λ₁/3 for the second). Starting from these initial displacements, damped molecular statics (energy minimization) is performed until each system reaches a local potential‑energy minimum. The relaxed configurations are then analyzed to obtain the transition‑region energy E, the maximum out‑of‑plane displacement, and the number of sign changes (zero‑crossings) of the displacement profile within a distance from the clamped edge. The transition energy is computed as (4M/W) Σₙ [e(n) − e(0)], where e(n) is the mean potential energy per atom at slice n and e(0) is the reference energy far from the clamped edge. The two configurations are compared to determine which yields a lower transition energy and to characterize their distinct wrinklon spatial patterns.

## Reproduction target
For a graphene nanoribbon with M=104, N=700 unit cells, strained to εxx⁰=−0.08 and εyy⁰=0.10, run the complete workflow using LAMMPS with the AIREBO potential (or an equivalent that reproduces ρ₀=1.418 Å). From the two equilibrium configurations obtained after relaxation, compute and submit the following:

- Transition‑region energy E (eV/Å) for each initial condition (λ₁→λ₁/2 and λ₁→λ₁/3) in results.json.
- The out‑of‑plane displacement ΔZ (nm) for atom k=1 as a function of unit‑cell indices (m,n) for both configurations, saved as CSV files with columns m,n,deltaZ.
- The number of zero‑crossings of the ΔZ profile along n within a distance W/2 from the clamped edge for each configuration, also reported in results.json.

The objective is to correctly reproduce these quantities from the simulated equilibrium states. No other external data or pretrained models are required; all necessary inputs are fully specified above and in the workflow steps.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- AIREBO interatomic potential for graphene: lammps

## Workflow steps

### Step 1: Build graphene nanoribbon and apply strain
- Role: process
- Action: Construct a rectangular computational cell for a graphene nanoribbon with M=104 unit cells in the zigzag (x) direction and N=700 in the armchair (y) direction, using equilibrium bond length ρ₀=1.418 Å and unit cell dimensions a₀=√3 ρ₀, b₀=3 ρ₀. Apply biaxial strain εxx⁰=−0.08, εyy⁰=0.10, updating cell dimensions a = a₀(1+εxx⁰), b = b₀(1+εyy⁰). Set periodic boundary conditions along y, clamp atomic displacements to zero at n=700, and impose mirror symmetry on displacements relative to the (xz)-plane at n=0. Define the interatomic potential (AIREBO) in LAMMPS.
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Impose initial wrinklon pattern
- Role: process
- Action: For all atoms, set out-of-plane displacement Δz: for unit cells 0≤n≤550, Δz = 0.1 Å·sin(2π x / λ₁) with λ₁ = W (the strained ribbon width); for 551≤n≤699, Δz = 0.1 Å·sin(2π x / λ₂) with λ₂ = λ₁/2 for the first configuration and λ₁/3 for the second. Initial in-plane displacements and velocities are zero. Create two separate LAMMPS input files, one per initial condition.
- Evidence: `/app/outputs/initial_structure_lambda1_to_lambda1_2.data, initial_structure_lambda1_to_lambda1_3.data`

### Step 3: Molecular statics relaxation
- Role: process
- Action: Using LAMMPS, run damped molecular statics (energy minimization) on each initial configuration until the system reaches a local potential energy minimum. Save the relaxed atomic coordinates and per-atom potential energies.
- Evidence: `/app/outputs/relaxed_config_lambda1_to_lambda1_2.log, relaxed_config_lambda1_to_lambda1_3.log`

### Step 4: Compute transition energy, max displacement, and zero-crossing counts
- Role: scored (load-bearing)
- Action: From the relaxed configurations, for each initial condition compute: (1) the transition-region energy E = (4M/W) Σₙ [e(n)−e(0)], where e(n) is the mean potential energy per atom at slice n and e(0) is the reference energy far from the clamped edge; (2) the maximum absolute out-of-plane displacement ΔZ (nm); (3) for atom k=1, count the number of sign changes (zero-crossings) of ΔZ along n within a distance W/2 from the clamped edge. Write these results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "systems": [
    {
      "initial_condition": "lambda1_to_lambda1_2",
      "energy_E": <float>,
      "max_deltaZ": <float>,
      "num_zero_crossings_within_W": <int>
    },
    {
      "initial_condition": "lambda1_to_lambda1_3",
      "energy_E": <float>,
      "max_deltaZ": <float>,
      "num_zero_crossings_within_W": <int>
    }
  ]
}
- Scoring: scored by hidden verifier

### Step 5: Export ΔZ map for λ₁→λ₁/2
- Role: scored
- Action: From the relaxed configuration for the λ₁→λ₁/2 initial condition, extract the out-of-plane displacement ΔZ (nm) for atom k=1 at every unit cell (m,n) and write a CSV file with columns m, n, deltaZ.
- Output file: `/app/outputs/deltaZ_lambda1_to_lambda1_2.csv`
- Format: csv
- Contract: Columns: m (int), n (int), deltaZ (nm)
- Scoring: scored by hidden verifier

### Step 6: Export ΔZ map for λ₁→λ₁/3
- Role: scored
- Action: Same as previous, but for the λ₁→λ₁/3 configuration.
- Output file: `/app/outputs/deltaZ_lambda1_to_lambda1_3.csv`
- Format: csv
- Contract: Columns: m (int), n (int), deltaZ (nm)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/deltaZ_lambda1_to_lambda1_2.csv`
- `/app/outputs/deltaZ_lambda1_to_lambda1_3.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent-reported transition-region energies, maximum out-of-plane displacement, and zero-crossing counts for both initial conditions. The hidden checker recomputes these quantities from the displacement CSV files and verifies the reported values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `systems`: array of objects, each with fields initial_condition (string), energy_E (number), max_deltaZ (number), num_zero_crossings_within_W (integer)
  - `items`:
    - `systems`:
      - `type`: object
      - `properties`:
        - `initial_condition`:
          - `type`: string
        - `energy_E`:
          - `type`: number
        - `max_deltaZ`:
          - `type`: number
        - `num_zero_crossings_within_W`:
          - `type`: integer

### deltaZ_lambda1_to_lambda1_2.csv
- path: `/app/outputs/deltaZ_lambda1_to_lambda1_2.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Out-of-plane displacement ΔZ for atom k=1 (in nm) at every unit cell index (m,n) for the λ₁→λ₁/2 initial condition. The checker uses this file to recompute zero-crossings and transition energy.
- schema:
  - `type`: table
  - `required_columns`: `m`, `n`, `deltaZ`
  - `units`:
    - `deltaZ`: nm

### deltaZ_lambda1_to_lambda1_3.csv
- path: `/app/outputs/deltaZ_lambda1_to_lambda1_3.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Out-of-plane displacement ΔZ for atom k=1 (in nm) at every unit cell index (m,n) for the λ₁→λ₁/3 initial condition. The checker uses this file to recompute zero-crossings and transition energy.
- schema:
  - `type`: table
  - `required_columns`: `m`, `n`, `deltaZ`
  - `units`:
    - `deltaZ`: nm

Notes: The three scored outputs together capture the paper's main result: distinct metastable wrinklon configurations with similar transition-region energies but different zero-crossing counts. The checker recomputes energies and zero-crossings from the raw CSV data, ensuring fidelity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "systems": "array of objects, each with fields initial_condition (string), energy_E (number), max_deltaZ (number), num_zero_crossings_within_W (integer)"
        },
        "items": {
          "systems": {
            "type": "object",
            "properties": {
              "initial_condition": {
                "type": "string"
              },
              "energy_E": {
                "type": "number"
              },
              "max_deltaZ": {
                "type": "number"
              },
              "num_zero_crossings_within_W": {
                "type": "integer"
              }
            }
          }
        }
      },
      "description": "Agent-reported transition-region energies, maximum out-of-plane displacement, and zero-crossing counts for both initial conditions. The hidden checker recomputes these quantities from the displacement CSV files and verifies the reported values within tolerances."
    },
    {
      "file": "deltaZ_lambda1_to_lambda1_2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "n",
          "deltaZ"
        ],
        "units": {
          "deltaZ": "nm"
        }
      },
      "description": "Out-of-plane displacement ΔZ for atom k=1 (in nm) at every unit cell index (m,n) for the λ₁→λ₁/2 initial condition. The checker uses this file to recompute zero-crossings and transition energy."
    },
    {
      "file": "deltaZ_lambda1_to_lambda1_3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "n",
          "deltaZ"
        ],
        "units": {
          "deltaZ": "nm"
        }
      },
      "description": "Out-of-plane displacement ΔZ for atom k=1 (in nm) at every unit cell index (m,n) for the λ₁→λ₁/3 initial condition. The checker uses this file to recompute zero-crossings and transition energy."
    }
  ],
  "notes": "The three scored outputs together capture the paper's main result: distinct metastable wrinklon configurations with similar transition-region energies but different zero-crossing counts. The checker recomputes energies and zero-crossings from the raw CSV data, ensuring fidelity."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently recomputes the key quantities from your raw ΔZ CSV files and the per‑atom energy data and compares them to expected reference values derived from the paper’s reported experimental conditions. The verifier will:

- Parse deltaZ_lambda1_to_lambda1_2.csv and deltaZ_lambda1_to_lambda1_3.csv, compute the number of zero‑crossings of ΔZ along n within the specified distance from the clamped edge, and verify agreement.
- Recompute the transition‑region energy E from the displacement‑derived energy profile and compare with your reported E values.
- Check that the reported maximum out‑of‑plane displacement is within a physically plausible range.

Each scored artifact (results.json and the two CSV files) carries a weight; the verifier combines the checks into a final reward between 0 and 1. Simply reporting literature numbers is not sufficient—the verifier’s recomputation must confirm that the artifacts reflect a genuine relaxation of the two initial wrinklon configurations as described in the workflow.
