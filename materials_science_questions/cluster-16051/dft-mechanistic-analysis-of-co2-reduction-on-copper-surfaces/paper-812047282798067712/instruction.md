# DFT and AIMD Study of CO2 Reduction on Cu Nanoparticles: Static Free Energies and Dynamic C-C Coupling Barrier

## Problem background
Electrochemical reduction of CO2 on Cu-based catalysts can produce multicarbon (C2+) fuels such as ethylene and ethanol, but the selectivity remains poor and the product distribution is highly sensitive to catalyst structure. Experiments show that carbon-supported Cu nanoparticles can exhibit enhanced C2+ selectivity compared to flat Cu electrodes, yet the underlying mechanisms—particularly the roles of particle size, low-coordinated sites, and support interactions—are not fully understood. Computational studies using density functional theory (DFT) and ab initio molecular dynamics (AIMD) can provide atomistic insight by computing free-energy profiles and activation barriers for key elementary steps, including C–C coupling. The aim of this task is to computationally investigate whether dynamic structure change of Cu clusters on a graphene support leads to surface roughening that significantly alters the C–C coupling barrier relative to static isolated clusters and a flat Cu(100) surface.

## Approach
The investigation combines static DFT calculations with AIMD simulations. First, models of five isolated Cu clusters (Cu8, Cu13, Cu20, Cu38, Cu55) and a Cu(100) surface slab are constructed and optimized using DFT with the PBE functional and D3 dispersion correction. For each system, free-energy changes for the elementary reduction steps *CO2→*COOH and *CO→*COH are computed within the computational hydrogen electrode (CHE) model, with implicit solvation. The activation barrier for the key C–C coupling step (*CO + *CHO) is then obtained via the nudged elastic band (NEB) method. These static results establish the baseline reactivity of isolated clusters and the Cu(100) reference. In parallel, an AIMD simulation of a Cu55 cluster supported on pristine graphene is performed at 300 K with implicit solvation to capture the dynamic motion of the cluster on the support. From the time-resolved trajectory, the surface roughness of the cluster is quantified as the standard deviation of the vertical positions of surface Cu atoms. A snapshot exhibiting large roughness is then selected, and the C–C coupling barrier is recalculated on that dynamically generated rough surface using the same static DFT/NEB protocol. The key comparison is between the C–C coupling barrier on the dynamic rough surface and the barrier on the static Cu(100) surface.

## Reproduction target
The task objective is to compute and output the following three scored artifacts:

1. `static_results.json` – A JSON array containing, for each system (Cu8, Cu13, Cu20, Cu38, Cu55, and Cu(100)), the computed free-energy changes for *CO→*COOH and *CO→*COH, and the activation barrier for *CO–*CHO coupling, all in electronvolts (eV).
2. `roughness_data.csv` – A CSV file with columns `time_ps` and `roughness_au`, recording the surface roughness factor at regular time intervals over at least 5 ps of AIMD simulation of Cu55 on graphene.
3. `barrier_rough.json` – A JSON object containing the activation barrier for *CO–*CHO coupling (in eV) computed on a dynamically roughened Cu surface obtained from the AIMD snapshot.



## Assets

- Quantum ESPRESSO (or open-source planewave DFT code with PBE+D3, implicit solvation, NEB): https://www.quantum-espresso.org/
- CP2K: https://www.cp2k.org/
- Python 3 with numpy, scipy, matplotlib: numpy, scipy, matplotlib
- Atomic structures of Cu clusters, Cu(100) surface, and graphene

## Workflow steps

### Step 1: Model construction and geometry optimization
- Role: process
- Action: Build and optimize atomic models for the five isolated Cu clusters (n=8,13,20,38,55), a Cu(100) surface slab, and the Cu55-on-graphene adsorption complex. Use DFT (PBE+D3) to relax all geometries to stable minima.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Static DFT free energy profiles and C-C coupling barriers
- Role: process
- Action: Using the optimized models, perform static DFT calculations (PBE+D3, implicit solvation, CHE model) to compute free energy changes for the *CO2→*COOH and *CO→*COH steps on each isolated cluster and Cu(100). For each system, compute the activation barrier for *CO-*CHO coupling using the NEB method. Save all raw energy and barrier data.
- Evidence: `/app/outputs/static_calculations.log`

### Step 3: Write static free energy and barrier summary
- Role: scored
- Action: Extract the key results from step 1 and write static_results.json: for each system (Cu8, Cu13, Cu20, Cu38, Cu55, and Cu(100)), provide the free energy change for *CO→*COOH, the free energy change for *CO→*COH, and the activation barrier for *CO-*CHO coupling. All values in electronvolts (eV).
- Output file: `/app/outputs/static_results.json`
- Format: json
- Contract: [{"system": "Cu8", "free_energy_COOH": 0.12, "free_energy_COH": 0.70, "barrier_CC": 0.73, "unit": "eV"}, ...]
- Scoring: scored by hidden verifier

### Step 4: AIMD simulation of Cu55 on pristine graphene
- Role: process
- Action: Run an ab initio molecular dynamics simulation of the Cu55-on-graphene system in aqueous solution (implicit solvation) at 300 K using CP2K (PBE+D3, SCCS). Use a time step of 0.5 fs and run for at least 5 ps. Record atomic trajectories and compute the surface roughness factor at each saved frame.
- Evidence: `/app/outputs/aimd_trajectory.xyz`

### Step 5: Record surface roughness time series
- Role: scored
- Action: From the AIMD trajectory, compute the surface roughness factor (as defined by the standard deviation of vertical positions of surface Cu atoms) at each recorded frame and write roughness_data.csv with columns time_ps (time in picoseconds) and roughness_au (roughness in arbitrary units). The file should cover the full simulation time and contain at least 500 rows.
- Output file: `/app/outputs/roughness_data.csv`
- Format: csv
- Contract: time_ps,roughness_au (header row, numeric values)
- Scoring: scored by hidden verifier

### Step 6: Compute C-C coupling barrier on dynamic rough surface
- Role: scored (load-bearing)
- Action: Select a snapshot from the AIMD trajectory where the surface roughness is large. Place *CO and *CHO on the roughly irregular surface and compute the minimum-energy path for their coupling using the NEB method (static DFT, same settings as step1). Extract the activation energy barrier (eV) and write barrier_rough.json.
- Output file: `/app/outputs/barrier_rough.json`
- Format: json
- Contract: {"barrier": 0.25, "unit": "eV"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_results.json`
- `/app/outputs/roughness_data.csv`
- `/app/outputs/barrier_rough.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_results.json
- path: `/app/outputs/static_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed free energy changes and C-C coupling barrier for each isolated cluster and Cu(100). Compared against the paper's reported average values with absolute and trend tolerances.
- schema:
  - `type`: array
  - `required`:
    - `system`: string (e.g., Cu8)
    - `free_energy_COOH`: number (eV)
    - `free_energy_COH`: number (eV)
    - `barrier_CC`: number (eV)
    - `unit`: string (always 'eV')
  - `items`: object

### roughness_data.csv
- path: `/app/outputs/roughness_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of surface roughness during AIMD. Must contain at least 500 rows and show measurable fluctuations (standard deviation > 0.1).
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `roughness_au`
  - `units`:
    - `time_ps`: picoseconds
    - `roughness_au`: arbitrary units (standard deviation of surface Cu z-coordinates)
  - `items`: object

### barrier_rough.json
- path: `/app/outputs/barrier_rough.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Activation barrier for C-C coupling on a dynamically roughened Cu surface. Compared against a hidden threshold (direction and exact value are not disclosed).
- schema:
  - `type`: object
  - `required`:
    - `barrier`: number (eV)
    - `unit`: string (always 'eV')
  - `items`: object

Notes: Scoring of static_results.json uses paper-reported averages (0.70 eV for *CO→*COH on clusters, 0.76 eV on Cu(100); 0.73 eV for *CO-*CHO on clusters, 0.77 eV on Cu(100)) with hidden tolerances. Roughness is audited structurally. The dynamic barrier is load-bearing: computing it requires genuinely running the AIMD and NEB steps, preventing bypass.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": {
          "system": "string (e.g., Cu8)",
          "free_energy_COOH": "number (eV)",
          "free_energy_COH": "number (eV)",
          "barrier_CC": "number (eV)",
          "unit": "string (always 'eV')"
        },
        "items": {}
      },
      "description": "Computed free energy changes and C-C coupling barrier for each isolated cluster and Cu(100). Compared against the paper's reported average values with absolute and trend tolerances."
    },
    {
      "file": "roughness_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "roughness_au"
        ],
        "units": {
          "time_ps": "picoseconds",
          "roughness_au": "arbitrary units (standard deviation of surface Cu z-coordinates)"
        },
        "items": {}
      },
      "description": "Time series of surface roughness during AIMD. Must contain at least 500 rows and show measurable fluctuations (standard deviation > 0.1)."
    },
    {
      "file": "barrier_rough.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "barrier": "number (eV)",
          "unit": "string (always 'eV')"
        },
        "items": {}
      },
      "description": "Activation barrier for C-C coupling on a dynamically roughened Cu surface. Compared against a hidden threshold (direction and exact value are not disclosed)."
    }
  ],
  "notes": "Scoring of static_results.json uses paper-reported averages (0.70 eV for *CO→*COH on clusters, 0.76 eV on Cu(100); 0.73 eV for *CO-*CHO on clusters, 0.77 eV on Cu(100)) with hidden tolerances. Roughness is audited structurally. The dynamic barrier is load-bearing: computing it requires genuinely running the AIMD and NEB steps, preventing bypass."
}
```

## How you are scored
A hidden verifier checks each output file independently. The checkers perform the following assessments:
- `static_results.json`: The reported free energies and barriers are compared against expected reference ranges with tolerances; both the absolute values and the relative trends among systems are evaluated.
- `roughness_data.csv`: The file is audited for structural validity (required columns, sufficient number of rows covering the simulation time) and for the presence of measurable roughness fluctuations.
- `barrier_rough.json`: The barrier value is compared against a hidden threshold. Meeting the threshold criterion earns full credit.

The final score is a weighted combination of the scores from all three checks. Simply reporting numbers that match the paper is not sufficient; the verifier penalizes artifacts that fail structural or threshold requirements.
