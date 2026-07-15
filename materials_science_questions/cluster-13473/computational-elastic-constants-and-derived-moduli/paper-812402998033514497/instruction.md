# Molecular Dynamics Simulation of Irradiation-Induced Amorphization in Cu-Ti Intermetallics

## Problem background
Irradiation can induce a crystalline-to-amorphous transition in many ordered intermetallic compounds, with consequences for the structural and mechanical stability of materials. Among alloy systems, the Cu-Ti series is particularly well studied experimentally, and molecular dynamics (MD) simulations offer a way to separate the effects of chemical disordering and point-defect production and to predict critical amorphization doses. This task investigates the radiation response of four Cu-Ti intermetallics (Cu4Ti, Cu4Ti3, CuTi, CuTi2) using embedded-atom method (EAM) MD simulations. The goal is to determine which compounds become amorphous under Frenkel-pair irradiation, the critical doses at which amorphization occurs, and how the average shear modulus softens relative to the perfect crystal.

## Approach
The method uses classical MD with EAM potentials to simulate irradiation damage in perfect crystals of each compound at 160 K. Three types of runs are performed: (1) equilibration of ordered crystals to obtain reference ground-state properties, (2) melt-quench simulations to create amorphous reference states, and (3) defect-accumulation runs where chemical disorder (atom exchanges) and Frenkel pairs are introduced at controlled rates. After each defect event the system is relaxed and its potential energy, volume, pair-correlation function, and elastic constants (C44, C', and their average Cavg) are computed. The onset of amorphization is detected by the condition C44 = C' (structural isotropy) combined with energy/volume reaching the quenched-liquid values. The core scientific question is to compare the dose needed to trigger amorphization under different defect-introduction modes (single vs. grouped Frenkel pairs) and to quantify the softening of the average shear modulus.

## Reproduction target
Reproduce MD simulations to determine the critical amorphization doses (in dpa) for Cu4Ti3, CuTi, CuTi2 under single Frenkel pair introduction, and for Cu4Ti under grouped Frenkel pair introduction; determine whether Cu4Ti becomes amorphous under single Frenkel pairs; and compute the average shear modulus ratio (C_avg_d / C_avg_c) evaluated at the amorphization point for the affected compounds. The target is to produce a single JSON artifact (results.json) containing boolean amorphization flags, numerical critical doses, and the shear modulus reduction factor, all computed from the MD pipeline described in the workflow steps.

## Assets

- Cu-Ti EAM interatomic potential (Sabochick and Lam, Phys. Rev. B 43, 1991): 10.1103/PhysRevB.43.5243
- Crystallographic structures of Cu-Ti intermetallics
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov

## Workflow steps

### Step 1: Build initial crystal structures
- Role: process
- Action: Construct perfect lattice supercells for Cu4Ti (D1a), Cu4Ti3 (Frank-Kasper), CuTi (B11), and CuTi2 (C15b) using their known crystallographic structures and the EAM-potential-predicted lattice constants.
- Evidence: none

### Step 2: Equilibrate perfect crystals and compute reference properties
- Role: process
- Action: Perform MD equilibration of each perfect crystal at 160 K for 5000 time steps using the EAM potential. Compute ground-state potential energy per atom, equilibrium volume, and shear elastic constants (C44, C', Cavg) using the fluctuation formula over 20000 time steps.
- Evidence: none

### Step 3: Generate quenched amorphous reference states
- Role: process
- Action: Produce amorphous references for each compound by melt-quench MD simulations: heat to a melt temperature then quench to 160 K. Record quenched-liquid potential energy, volume, and pair-correlation functions.
- Evidence: none

### Step 4: Irradiation simulations with defect introduction
- Role: process
- Action: For each compound, introduce chemical disorder via atom exchanges (one Cu-Ti pair per event) and point defects via Frenkel pair creation at controlled rates: single Frenkel pairs (one per event) for Cu4Ti3, CuTi, CuTi2; single and grouped Frenkel pairs (groups of ten per event) for Cu4Ti. After each defect event, perform energy minimization (Fletcher-Powell) and MD equilibration at 160 K. Save configurations periodically for analysis.
- Evidence: none

### Step 5: Property analysis of irradiated configurations
- Role: process
- Action: For each saved configuration, compute potential energy, volume expansion (ΔV/V), pair-correlation function g(r), and elastic constants (C44, C', Cavg) using the fluctuation formula. Collect these as functions of dose (dpa or epa).
- Evidence: none

### Step 6: Determine amorphization outcomes and critical doses
- Role: scored (load-bearing)
- Action: Analyze the dose-dependent property curves to determine for each compound and irradiation mode whether amorphization occurs and at what critical dose (where C44 equals C' and energy/volume reach quenched-liquid levels). Report boolean amorphization flags for Cu4Ti under single and grouped Frenkel pairs, critical doses for Cu4Ti3, CuTi, CuTi2 under single Frenkel pairs, critical dose for Cu4Ti under grouped Frenkel pairs, and the average shear modulus ratio (C_avg_d / C_avg_c) at amorphization. Output a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with required keys: Cu4Ti_single_FP_amorphized (boolean), Cu4Ti_grouped_FP_amorphized (boolean), Cu4Ti3_critical_dose (float), CuTi_critical_dose (float), CuTi2_critical_dose (float), Cu4Ti_grouped_critical_dose (float), C_avg_ratio_at_amorphization (float). The ratio is the average shear modulus of the amorphized compound divided by that of the perfect crystal.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored JSON file containing the amorphization outcomes, critical doses, and shear modulus reduction factor.
- schema:
  - `type`: object
  - `required`: `Cu4Ti_single_FP_amorphized`, `Cu4Ti_grouped_FP_amorphized`, `Cu4Ti3_critical_dose`, `CuTi_critical_dose`, `CuTi2_critical_dose`, `Cu4Ti_grouped_critical_dose`, `C_avg_ratio_at_amorphization`
  - `properties`:
    - `Cu4Ti_single_FP_amorphized`:
      - `type`: boolean
      - `description`: whether Cu4Ti becomes amorphous under single Frenkel pair introduction
    - `Cu4Ti_grouped_FP_amorphized`:
      - `type`: boolean
      - `description`: whether Cu4Ti becomes amorphous under grouped Frenkel pair introduction
    - `Cu4Ti3_critical_dose`:
      - `type`: number
      - `description`: critical dose for amorphization of Cu4Ti3 under single Frenkel pairs, in dpa
    - `CuTi_critical_dose`:
      - `type`: number
      - `description`: critical dose for amorphization of CuTi under single Frenkel pairs, in dpa
    - `CuTi2_critical_dose`:
      - `type`: number
      - `description`: critical dose for amorphization of CuTi2 under single Frenkel pairs, in dpa
    - `Cu4Ti_grouped_critical_dose`:
      - `type`: number
      - `description`: critical dose for amorphization of Cu4Ti under grouped Frenkel pairs, in dpa
    - `C_avg_ratio_at_amorphization`:
      - `type`: number
      - `description`: ratio of average shear modulus at amorphization to that of the perfect crystal

Notes: The hidden checker compares the reported boolean flags, critical doses, and ratio to paper-derived gold values with tolerances: ±20% relative on critical doses, exact match for boolean outcomes, and ratio within 0.5 ± 0.1.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Cu4Ti_single_FP_amorphized",
          "Cu4Ti_grouped_FP_amorphized",
          "Cu4Ti3_critical_dose",
          "CuTi_critical_dose",
          "CuTi2_critical_dose",
          "Cu4Ti_grouped_critical_dose",
          "C_avg_ratio_at_amorphization"
        ],
        "properties": {
          "Cu4Ti_single_FP_amorphized": {
            "type": "boolean",
            "description": "whether Cu4Ti becomes amorphous under single Frenkel pair introduction"
          },
          "Cu4Ti_grouped_FP_amorphized": {
            "type": "boolean",
            "description": "whether Cu4Ti becomes amorphous under grouped Frenkel pair introduction"
          },
          "Cu4Ti3_critical_dose": {
            "type": "number",
            "description": "critical dose for amorphization of Cu4Ti3 under single Frenkel pairs, in dpa"
          },
          "CuTi_critical_dose": {
            "type": "number",
            "description": "critical dose for amorphization of CuTi under single Frenkel pairs, in dpa"
          },
          "CuTi2_critical_dose": {
            "type": "number",
            "description": "critical dose for amorphization of CuTi2 under single Frenkel pairs, in dpa"
          },
          "Cu4Ti_grouped_critical_dose": {
            "type": "number",
            "description": "critical dose for amorphization of Cu4Ti under grouped Frenkel pairs, in dpa"
          },
          "C_avg_ratio_at_amorphization": {
            "type": "number",
            "description": "ratio of average shear modulus at amorphization to that of the perfect crystal"
          }
        }
      },
      "description": "Scored JSON file containing the amorphization outcomes, critical doses, and shear modulus reduction factor."
    }
  ],
  "notes": "The hidden checker compares the reported boolean flags, critical doses, and ratio to paper-derived gold values with tolerances: ±20% relative on critical doses, exact match for boolean outcomes, and ratio within 0.5 ± 0.1."
}
```

## How you are scored
A hidden verifier will compare the values in your results.json (the amorphization flags, critical doses, and shear modulus ratio) to independently determined reference values using appropriate tolerances. The amorphization flags are checked for exact match; the critical doses are compared with tolerance; the shear modulus ratio is checked within a tolerance band. Each scored output carries a weight that contributes to the final reward in [0,1]. In addition, the verifier may audit the presence and format of the JSON artifact and the correctness of its keys. The checker does not re-run your simulations; it judges only the reported results. To earn full credit, your reported values must be within the acceptable ranges of the (hidden) reference values, which are derived from rigorous MD simulations under the same protocol.
