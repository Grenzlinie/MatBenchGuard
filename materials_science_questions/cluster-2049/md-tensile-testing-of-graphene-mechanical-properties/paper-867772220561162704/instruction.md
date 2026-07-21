# MD Simulation of Knotting Effect on Graphene Buckling and Unknotting Mechanism

## Problem background
Monolayer graphene exhibits buckling under compression due to its extreme thinness. When free edges are present, they warp out of plane due to compressive edge stress. In narrow nanoribbons, the penetration depth of this edge warping can be comparable to the ribbon width, causing the two free edges to interact. This task investigates how the interaction between a pair of free edges, specifically when they warp in opposite directions, affects the buckling response. In that configuration, the collision of buckling waves from the two edges during compression can create a knot structure, which may lead to a gradual buckling mode, enhanced mechanical stiffness, and a stable post-buckling regime. The goal is to compute the stress-strain curves for both opposite-warping and same-warping edge configurations, determine the critical strain at which the knot unknits, and quantify the energy barrier that stabilizes the knot.

## Approach
The buckling of an armchair graphene nanoribbon (30 Å along the compression direction x, 80 Å along the free-edge direction y) is studied by classical molecular dynamics using the Brenner reactive empirical bond-order (REBO) potential. The workflow proceeds as follows. First, a flat ribbon is thermalized at 1 K and zero pressure within the NPT ensemble for 200 ps to obtain two distinct warped-edge configurations: one where the two free edges warp in opposite directions (configuration FBC‑1) and one where they warp in the same direction (configuration FBC+1). Each configuration is then compressed uniaxially in the x‑direction at 1 K by deforming the simulation box while allowing lateral relaxation; the virial stress σ_xx is recorded as a function of strain. The FBC+1 curve serves as a baseline representing the typical abrupt buckling, while the FBC‑1 curve captures the gradual, knot-mediated buckling. For the FBC‑1 compression, the atomic configuration is saved at an engineering strain of 0.02 (the knotted state R_minus). Compression is continued past the unknotting point, and the unknotted structure is saved as R_plus. To analyze the knot energetics, a reaction coordinate η linearly interpolates the atomic fractional coordinates between R_minus (η=−1) and R_plus (η=+1). At each η, a static energy minimization at 0 K is performed, yielding a potential energy profile. The barrier for unknotting is derived from this profile.

## Reproduction target
1. Produce the compression stress‑strain curve (strain 0 – 0.04) for the FBC‑1 configuration at 1 K and save it as `step_01_stress_strain_fbc1.csv`.
2. Produce the compression stress‑strain curve over the same strain range for the FBC+1 configuration and save it as `step_02_stress_strain_fbc+1.csv`.
3. From the FBC‑1 curve, determine the critical unknotting strain εu (the strain at which the stress first falls substantially after the plateau) and write the dimensionless value to `step_03_critical_unknotting_strain.txt`.
4. Using the saved knotted (ε=0.02) and unknotted configurations, perform an η‑interpolation scan (η = –1 to +1, at least 21 points) with static energy minimizations and save the η vs. potential‑energy data to `step_04_eta_scan_energy.csv`.
5. From the η‑scan, compute the barrier ΔV = V(η=0) − V(η=–1), convert to meV, and write the value to `step_05_barrier_mev.txt`.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/downloads

## Workflow steps

### Step 1: Generate initial graphene nanoribbon structure
- Role: process
- Action: Create atomic coordinates for an armchair graphene nanoribbon of dimensions 30 Å (armchair along x) by 80 Å (along y). Fix the two ends in the x‑direction, keep the two y‑edges free.
- Evidence: none

### Step 2: Thermalize to obtain warped edge configurations
- Role: process
- Action: Using LAMMPS with the Brenner potential (AIREBO or REBO), thermalize the flat nanoribbon at 1 K and zero pressure within the NPT ensemble (Nosé‑Hoover) for 200 ps. After equilibration, classify the warping direction of each free edge and produce one stable configuration of FBC‑1 (opposite warping) and one of FBC+1 (same warping). Multiple random velocity seeds may be needed.
- Evidence: none

### Step 3: Compress FBC‑1 configuration and record stress‑strain curve
- Role: scored (load-bearing)
- Action: Using the thermalized FBC‑1 configuration, apply uniaxial compressive strain in the x‑direction at 1 K by uniformly deforming the simulation box while maintaining lateral relaxation. Record the virial stress σ_xx at each strain. Sample at least 100 points from strain 0 to 0.04. At an engineering strain of 0.02, save the atomic configuration (R_minus). Continue compression until the stress drops to the level of the FBC+1 curve (post‑unknotting); save that configuration as R_plus for later use.
- Output file: `/app/outputs/step_01_stress_strain_fbc1.csv`
- Format: csv
- Contract: CSV with columns: strain (dimensionless), stress_xx (GPa). At least 100 rows covering strain from 0 to 0.04.
- Scoring: scored by hidden verifier

### Step 4: Compress FBC+1 configuration and record stress‑strain curve
- Role: scored
- Action: Compress the thermalized FBC+1 configuration under identical conditions (1 K, uniform box deformation, lateral relaxation). Record virial stress σ_xx at each strain over the same range 0‑0.04 with at least 100 points.
- Output file: `/app/outputs/step_02_stress_strain_fbc+1.csv`
- Format: csv
- Contract: CSV with columns: strain (dimensionless), stress_xx (GPa). At least 100 rows covering strain from 0 to 0.04.
- Scoring: scored by hidden verifier

### Step 5: Extract critical unknotting strain
- Role: scored
- Action: From the FBC‑1 stress‑strain curve (step_01), determine the critical unknotting strain εu. A practical definition is the strain at which the stress first falls below 90% of the peak stress after the initial plateau. Write the numeric value.
- Output file: `/app/outputs/step_03_critical_unknotting_strain.txt`
- Format: txt
- Contract: A single floating‑point number (e.g., 0.0336).
- Scoring: scored by hidden verifier

### Step 6: Perform η‑interpolation potential energy scan
- Role: scored (load-bearing)
- Action: Using the saved atomic configurations R_minus (at ε=0.02) and R_plus (unknotted), generate a family of configurations by linear interpolation in fractional coordinates: R(η) = (1‑η)/2 * R_minus + (1+η)/2 * R_plus for η ranging from ‑1 to +1 in at least 21 uniform steps. For each η, perform a static 0 K energy minimization with the Brenner potential to obtain the potential energy. Record η and energy.
- Output file: `/app/outputs/step_04_eta_scan_energy.csv`
- Format: csv
- Contract: CSV with columns: eta (dimensionless, range -1 to 1), potential_energy (eV). At least 21 rows uniformly spaced in eta.
- Scoring: scored by hidden verifier

### Step 7: Compute potential energy barrier ΔV
- Role: scored
- Action: From the eta‑scan data (step_04), compute ΔV = V(η=0) − V(η=‑1) and convert to meV (1 eV = 1000 meV). Write the value.
- Output file: `/app/outputs/step_05_barrier_mev.txt`
- Format: txt
- Contract: A single floating‑point number (e.g., 600 for 0.6 eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stress_strain_fbc1.csv`
- `/app/outputs/step_02_stress_strain_fbc+1.csv`
- `/app/outputs/step_03_critical_unknotting_strain.txt`
- `/app/outputs/step_04_eta_scan_energy.csv`
- `/app/outputs/step_05_barrier_mev.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stress_strain_fbc1.csv
- path: `/app/outputs/step_01_stress_strain_fbc1.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress‑strain data for FBC‑1 compression. The checker uses this file to extract εu and verify gradual buckling.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_xx`
  - `units`:
    - `strain`: dimensionless
    - `stress_xx`: GPa

### step_02_stress_strain_fbc+1.csv
- path: `/app/outputs/step_02_stress_strain_fbc+1.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress‑strain data for FBC+1 compression. The checker verifies abrupt buckling and consistency with PBC.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_xx`
  - `units`:
    - `strain`: dimensionless
    - `stress_xx`: GPa

### step_03_critical_unknotting_strain.txt
- path: `/app/outputs/step_03_critical_unknotting_strain.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Agent‑reported critical unknotting strain εu extracted from step_01.
- schema:
  - `type`: number
  - `unit`: dimensionless

### step_04_eta_scan_energy.csv
- path: `/app/outputs/step_04_eta_scan_energy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: η‑scan energy data. The checker recomputes the potential energy barrier ΔV from this raw data.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `potential_energy`
  - `units`:
    - `eta`: dimensionless
    - `potential_energy`: eV

### step_05_barrier_mev.txt
- path: `/app/outputs/step_05_barrier_mev.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Agent‑reported potential energy barrier ΔV (difference V(η=0)‑V(η=‑1)) derived from step_04, in meV.
- schema:
  - `type`: number
  - `unit`: meV

Notes: The hidden checker recomputes εu from step_01 (using the 90%‑of‑peak rule) and ΔV from step_04 (as V(η=0)‑V(η=‑1)), comparing them to the paper’s reported values with appropriate tolerances. The stress‑strain curves are also audited for qualitative features. Step_05 is provided for completeness but the primary scoring uses recomputation from raw data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stress_strain_fbc1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_xx"
        ],
        "units": {
          "strain": "dimensionless",
          "stress_xx": "GPa"
        }
      },
      "description": "Stress‑strain data for FBC‑1 compression. The checker uses this file to extract εu and verify gradual buckling."
    },
    {
      "file": "step_02_stress_strain_fbc+1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_xx"
        ],
        "units": {
          "strain": "dimensionless",
          "stress_xx": "GPa"
        }
      },
      "description": "Stress‑strain data for FBC+1 compression. The checker verifies abrupt buckling and consistency with PBC."
    },
    {
      "file": "step_03_critical_unknotting_strain.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "number",
        "unit": "dimensionless"
      },
      "description": "Agent‑reported critical unknotting strain εu extracted from step_01."
    },
    {
      "file": "step_04_eta_scan_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "potential_energy"
        ],
        "units": {
          "eta": "dimensionless",
          "potential_energy": "eV"
        }
      },
      "description": "η‑scan energy data. The checker recomputes the potential energy barrier ΔV from this raw data."
    },
    {
      "file": "step_05_barrier_mev.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "number",
        "unit": "meV"
      },
      "description": "Agent‑reported potential energy barrier ΔV (difference V(η=0)‑V(η=‑1)) derived from step_04, in meV."
    }
  ],
  "notes": "The hidden checker recomputes εu from step_01 (using the 90%‑of‑peak rule) and ΔV from step_04 (as V(η=0)‑V(η=‑1)), comparing them to the paper’s reported values with appropriate tolerances. The stress‑strain curves are also audited for qualitative features. Step_05 is provided for completeness but the primary scoring uses recomputation from raw data."
}
```

## How you are scored
A hidden verifier independently inspects each output file and combines the results into a final reward (0 – 1). The stress‑strain curves (Steps 3 and 4) are checked for structural features: the FBC‑1 curve should show a gradual stress decline while the FBC+1 curve should exhibit an abrupt drop. The verifier recomputes the critical unknotting strain from your submitted FBC‑1 CSV using a prescribed rule (e.g., the strain where stress first falls below 90 % of the peak after the plateau) and compares it to a hidden reference tolerance. The potential energy barrier is recomputed from `step_04_eta_scan_energy.csv` as V(η=0)−V(η=–1) and compared to a hidden reference tolerance; your self-reported εu and ΔV values are also checked against the same tolerances. Satisfying only the self-reported numbers without consistent raw CSV evidence will not yield full credit. Each stage is weighted, and the final score is the weighted sum of these stage scores.
