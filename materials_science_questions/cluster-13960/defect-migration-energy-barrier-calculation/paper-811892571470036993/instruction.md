# DFT-NEB calculation of surface segregation barriers in Pt(111)

## Problem background
Pt-based alloy catalysts used in polymer electrolyte membrane fuel cells exhibit surface segregation, where impurity atoms diffuse to or from the surface, influencing catalytic activity and stability. Understanding the kinetics of this process is crucial. A vacancy-mediated kinetic model provides a mechanistic picture in which an impurity atom migrates through a surface vacancy. The present task focuses on two impurity metals, Au and Co, in a Pt(111) host. The objective is to compute the energy barriers and overall thermodynamic driving force for the vacancy-assisted segregation pathway of each impurity, thereby determining their respective segregation tendencies.

## Approach
The computation employs density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and projector augmented wave (PAW) pseudopotentials. An open-source plane-wave DFT code (Quantum ESPRESSO or equivalent) is used. The model system is a five-layer 3×3 Pt(111) slab with a vacuum gap. A surface vacancy is created in the topmost layer, and the impurity atom (Au or Co) is placed in the second layer. The bottom two layers are fixed at bulk positions, while the top three layers are allowed to relax. The segregation pathway consists of three elementary steps: (i) impurity migration from the second layer to the surface vacancy, (ii) intralayer Pt movement to fill the resulting vacancy in the second layer, and (iii) interlayer Pt migration from the surface to the second layer, regenerating the surface vacancy. The nudged elastic band (NEB) method is used to find minimum-energy paths and extract activation barriers. Separate calculations are performed for Au and Co impurities.

## Reproduction target
For each impurity (Au and Co), compute the activation barrier (in eV) for the impurity migration step (step 1→2), the barrier for the rate-determining Pt interlayer migration step (TS3, step 3→4), and the total energy change ΔE(state 4) − ΔE(state 1) for the complete cycle. Report these six quantities in two JSON files: step_01_au_barriers.json and step_02_co_barriers.json, as specified in the output contract. The results must be obtained from full DFT+NEB calculations on a 3×3 five-layer Pt(111) slab with the described setup and spin-polarized PBE, using a plane-wave cutoff of approximately 350 eV and a 4×4×1 k-point mesh.

## Assets

- Atomic Simulation Environment (ASE): ase
- Quantum ESPRESSO (or equivalent open-source plane-wave DFT code with NEB support): https://www.quantum-espresso.org/
- PBE pseudopotentials for Pt, Au, Co: https://www.quantum-espresso.org/pseudopotentials or SSSP efficiency library (https://www.materialscloud.org/discover/sssp/table/efficiency)

## Workflow steps

### Step 1: Optimize bulk Pt lattice constant
- Role: process
- Action: Perform spin-polarized DFT calculation on bulk fcc Pt to determine the equilibrium lattice constant a. Use the same pseudopotential and functional as later steps. Store the optimized lattice constant.
- Evidence: `/app/outputs/bulk_lattice_optimization.json`

### Step 2: Construct slab supercells and endpoint structures
- Role: process
- Action: Using the optimized lattice constant, build a five-layer 3×3 Pt(111) slab with vacuum. Place a surface vacancy at the topmost layer center and the impurity (Au or Co) in the second layer center. Create all endpoint structures for the segregation cycle: structure 1 (impurity in second layer, vacancy on surface), structure 2 (impurity on surface, vacancy in second layer), structure 3 (intralayer Pt movement, vacancy in second layer), and structure 4 (interlayer Pt movement, vacancy on surface). Bottom two layers are fixed at bulk positions; top three layers are free to relax. Generate configurations for both Au and Co impurities.
- Evidence: `/app/outputs/slab_structures.traj`

### Step 3: DFT geometry relaxation of endpoint structures
- Role: process
- Action: Relax all endpoint structures (1–4 for Au and Co) using spin-polarized DFT with PBE functional, plane-wave cutoff ~350 eV, 4×4×1 k‑points, and force convergence 1×10⁻⁴ eV/Å. Top three layers free, bottom two fixed. Save relaxed coordinates and total energies.
- Evidence: `/app/outputs/relaxed_endpoints.pickle`

### Step 4: NEB calculations for Au segregation pathways
- Role: process
- Action: Run nudged elastic band calculations for three elementary steps (1→2 impurity migration, 2→3 intralayer Pt movement, 3→4 interlayer Pt migration) using the relaxed Au endpoints. Use at least 5 images and the same DFT settings. Save the energy profile (image energies) for each step.
- Evidence: `/app/outputs/au_neb_profiles.json`

### Step 5: Extract Au segregation barriers and total energy change
- Role: scored (load-bearing)
- Action: From the Au NEB profiles, determine the activation barrier for step 1→2 (energy of highest image minus energy of state 1), the barrier for the rate-determining step TS3 (step 3→4, highest image energy minus energy of state 3), and the total energy change ΔE(state 4) − ΔE(state 1). Write these three values (in eV) to step_01_au_barriers.json.
- Output file: `/app/outputs/step_01_au_barriers.json`
- Format: json
- Contract: {"impurity": "string (Au)", "barrier_step1_2_eV": "number (eV)", "barrier_TS3_eV": "number (eV)", "delta_E_total_1_to_4_eV": "number (eV)"}
- Scoring: scored by hidden verifier

### Step 6: NEB calculations for Co segregation pathways
- Role: process
- Action: Run nudged elastic band calculations for the same three elementary steps using the relaxed Co endpoints. Same DFT settings and number of images as for Au. Save the energy profile for each step.
- Evidence: `/app/outputs/co_neb_profiles.json`

### Step 7: Extract Co segregation barriers and total energy change
- Role: scored (load-bearing)
- Action: From the Co NEB profiles, determine the activation barrier for step 1→2, the barrier for the rate-determining step TS3 (step 3→4), and the total energy change ΔE(state 4) − ΔE(state 1). Write these three values (in eV) to step_02_co_barriers.json.
- Output file: `/app/outputs/step_02_co_barriers.json`
- Format: json
- Contract: {"impurity": "string (Co)", "barrier_step1_2_eV": "number (eV)", "barrier_TS3_eV": "number (eV)", "delta_E_total_1_to_4_eV": "number (eV)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_au_barriers.json`
- `/app/outputs/step_02_co_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_au_barriers.json
- path: `/app/outputs/step_01_au_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Au vacancy-mediated segregation barriers and overall energy change. Checked against the paper's reported values within hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `impurity`: string
    - `barrier_step1_2_eV`: number
    - `barrier_TS3_eV`: number
    - `delta_E_total_1_to_4_eV`: number
  - `units`:
    - `barrier_step1_2_eV`: eV
    - `barrier_TS3_eV`: eV
    - `delta_E_total_1_to_4_eV`: eV

### step_02_co_barriers.json
- path: `/app/outputs/step_02_co_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Co vacancy-mediated segregation barriers and overall energy change. Checked against the paper's reported values within hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `impurity`: string
    - `barrier_step1_2_eV`: number
    - `barrier_TS3_eV`: number
    - `delta_E_total_1_to_4_eV`: number
  - `units`:
    - `barrier_step1_2_eV`: eV
    - `barrier_TS3_eV`: eV
    - `delta_E_total_1_to_4_eV`: eV

Notes: The agent must compute the quantities via DFT+NEB as described in the steps. The checker performs result-level comparison (T0) with hidden tolerances to account for different pseudopotentials and code implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_au_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "impurity": "string",
          "barrier_step1_2_eV": "number",
          "barrier_TS3_eV": "number",
          "delta_E_total_1_to_4_eV": "number"
        },
        "units": {
          "barrier_step1_2_eV": "eV",
          "barrier_TS3_eV": "eV",
          "delta_E_total_1_to_4_eV": "eV"
        }
      },
      "description": "Au vacancy-mediated segregation barriers and overall energy change. Checked against the paper's reported values within hidden tolerances."
    },
    {
      "file": "step_02_co_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "impurity": "string",
          "barrier_step1_2_eV": "number",
          "barrier_TS3_eV": "number",
          "delta_E_total_1_to_4_eV": "number"
        },
        "units": {
          "barrier_step1_2_eV": "eV",
          "barrier_TS3_eV": "eV",
          "delta_E_total_1_to_4_eV": "eV"
        }
      },
      "description": "Co vacancy-mediated segregation barriers and overall energy change. Checked against the paper's reported values within hidden tolerances."
    }
  ],
  "notes": "The agent must compute the quantities via DFT+NEB as described in the steps. The checker performs result-level comparison (T0) with hidden tolerances to account for different pseudopotentials and code implementations."
}
```

## How you are scored
After you submit the output files, a hidden verifier will read the JSON files and compare your reported barriers and energy changes to reference values derived from the original study, taking into account expected method-dependent variations. Your score will be based on the accuracy of the quantitative values.
