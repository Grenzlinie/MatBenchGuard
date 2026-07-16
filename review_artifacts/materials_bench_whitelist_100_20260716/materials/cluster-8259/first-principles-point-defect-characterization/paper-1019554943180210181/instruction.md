# Multiscale simulation of Al-implanted defects in 4H-SiC: DFT trap levels, NEB barriers, and quantum transport

## Problem background
Aluminum ion implantation is a critical technique for p-type doping in 4H-SiC power devices, but the implantation and post-annealing processes produce not only the desired Al_Si acceptor configuration but also unintended Al configurations (Al_C, Al_i) and abundant point defects (vacancies, interstitials, antisites). These complexes can introduce mid-gap trap levels and alter the local electronic structure, degrading MOSFET channel transport—increasing leakage, shifting threshold voltage, and reducing carrier mobility. Understanding the quantitative electronic and transport signatures of these Al-defect couplings is essential for improving device reliability. Your task is to compute these signatures using first-principles and quantum transport simulations.

## Approach
A multiscale simulation approach is employed, combining density functional theory (DFT), climbing-image nudged elastic band (CI-NEB) calculations, maximally localized Wannier function (MLWF) transformation, and quantum transport simulation. Starting from a perfect 4H-SiC crystal, you will construct supercells (240 atoms) containing a series of defect complexes as specified. Using DFT with the PBE functional, you will relax the structures, compute band structures, and extract trap-level positions relative to the valence band edge. For key migration reactions, CI-NEB calculations (7 images) will determine the minimum energy path and barrier heights. The electronic wavefunctions of the most critical defect complex will then be transformed into a tight-binding Hamiltonian via Wannier90, which serves as the input for a Poisson-NEGF quantum transport simulation of a 10 nm MOSFET channel. This pipeline yields the trap-level energies, reaction barriers, and the I-V transfer characteristic of the defective channel under a fixed drain bias.

## Reproduction target
Compute and report the following three artifacts under the specified directory:
- Trap-level energies (in eV from the valence band maximum) and Fermi-level character for the perfect 4H-SiC crystal and for six defect supercells: isolated Al_Si, Al_Si+V_C, Al_C, Al_C+Si_C, Al_i, and Al_i+antisite. Store results in bandstructure_trap_levels.json.
- Energy barriers (in eV) for two migration pathways involving Al interstitial and a carbon vacancy, as defined in the workflow step, along with the full image energies. Store results in neb_barriers.json.
- I_d vs. V_g transfer characteristic (V_d=0.3 V) for a 10 nm-channel 4H-SiC MOSFET incorporating the tight-binding model of the Al_Si+V_C defect. Provide at least 50 data points covering V_g 0–6 V. Results in iv_characteristics.csv.
Each output must conform to the schemas and format described in the output contract. All values are to be determined by executing the simulation pipeline.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: https://wannier.org/
- NanoTCAD ViDES: https://nanohub.org/tools/vides/
- 4H-SiC pseudopotentials (Si USPP, C PAW, Al PAW): Standard pseudopotential libraries (PSLIB) available via Quantum ESPRESSO

## Workflow steps

### Step 1: DFT band structure and trap-level extraction
- Role: scored
- Action: Build 4H-SiC 3x5x1 supercells (240 atoms) containing the following defect types: perfect crystal, isolated Al_Si, Al_Si+V_C, Al_C, Al_C+Si_C, Al_i, Al_i+antisite. Relax structures and compute band structures using DFT (PBE functional). Extract band gap and trap-level energies (eV from VBM) for each defect. Write the results to the output file.
- Output file: `/app/outputs/bandstructure_trap_levels.json`
- Format: json
- Contract: JSON object with key 'defects': list of objects, each with 'name' (string), 'band_gap' (float, eV), 'trap_energies' (list of floats, eV from VBM), 'fermi_level_position' (string), 'notes' (string).
- Scoring: scored by hidden verifier

### Step 2: CI-NEB barrier calculation for Al_i + V_C migration
- Role: scored
- Action: Construct initial and final states for two Al_i + V_C reaction paths: (a) Al_i directly occupying V_C to form Al_C, (b) Al displacing Si and Si migrating to V_C (forming Al_Si+Si_C). Run CI-NEB (7 images) using DFT. Extract minimum-energy pathway and barrier heights. Write results.
- Output file: `/app/outputs/neb_barriers.json`
- Format: json
- Contract: JSON object with key 'reactions': list of objects, each with 'pathway' (string), 'initial_energy' (float, eV), 'final_energy' (float, eV), 'barrier_height' (float, eV), 'image_energies' (list of floats).
- Scoring: scored by hidden verifier

### Step 3: Maximally localized Wannier function transformation
- Role: process
- Action: Use Wannier90 to convert DFT wavefunctions from the Al_Si+V_C defect supercell into a tight-binding Hamiltonian. Output the hopping parameters and on-site energies needed for transport.
- Evidence: `/app/outputs/wannier_output.log`

### Step 4: Quantum transport simulation of defective MOSFET channel
- Role: scored (load-bearing)
- Action: Construct a 10 nm-channel 4H-SiC MOSFET (gate oxide 1 nm, gate workfunction equal to perfect crystal) incorporating the tight-binding model of the Al_Si+V_C defect from step s3. Solve Poisson-NEGF for V_g from 0 to 6 V, V_d=0.3 V. Output the I_d vs. V_g transfer characteristic.
- Output file: `/app/outputs/iv_characteristics.csv`
- Format: csv
- Contract: CSV with columns: 'Vg' (float, V), 'Id' (float, A/um). Must contain at least 50 data points covering the range 0-6 V. Row 1 is a header.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandstructure_trap_levels.json`
- `/app/outputs/neb_barriers.json`
- `/app/outputs/iv_characteristics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandstructure_trap_levels.json
- path: `/app/outputs/bandstructure_trap_levels.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Trap-level energies and Fermi-level character for each defect supercell.
- schema:
  - `type`: object
  - `required`:
    - `defects`: array of defect objects
  - `items`:
    - `name`: string
    - `band_gap`: number (eV)
    - `trap_energies`: array of numbers (eV from VBM)
    - `fermi_level_position`: string
    - `notes`: string

### neb_barriers.json
- path: `/app/outputs/neb_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: CI-NEB energy barriers for the two Al_i + V_C migration paths.
- schema:
  - `type`: object
  - `required`:
    - `reactions`: array of reaction objects
  - `items`:
    - `pathway`: string
    - `initial_energy`: number (eV)
    - `final_energy`: number (eV)
    - `barrier_height`: number (eV)
    - `image_energies`: array of numbers (eV)

### iv_characteristics.csv
- path: `/app/outputs/iv_characteristics.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: I_d vs V_g transfer characteristic at V_d=0.3 V for the Al_Si+V_C channel.
- schema:
  - `type`: table
  - `required_columns`: `Vg`, `Id`
  - `units`:
    - `Vg`: V
    - `Id`: A/um

Notes: All outputs will be compared to hidden reference values from the literature; tolerances are not disclosed to the agent. The entire pipeline must be executed; the process step is enforced by the load-bearing scored step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandstructure_trap_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "defects": "array of defect objects"
        },
        "items": {
          "name": "string",
          "band_gap": "number (eV)",
          "trap_energies": "array of numbers (eV from VBM)",
          "fermi_level_position": "string",
          "notes": "string"
        }
      },
      "description": "Trap-level energies and Fermi-level character for each defect supercell."
    },
    {
      "file": "neb_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "reactions": "array of reaction objects"
        },
        "items": {
          "pathway": "string",
          "initial_energy": "number (eV)",
          "final_energy": "number (eV)",
          "barrier_height": "number (eV)",
          "image_energies": "array of numbers (eV)"
        }
      },
      "description": "CI-NEB energy barriers for the two Al_i + V_C migration paths."
    },
    {
      "file": "iv_characteristics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vg",
          "Id"
        ],
        "units": {
          "Vg": "V",
          "Id": "A/um"
        }
      },
      "description": "I_d vs V_g transfer characteristic at V_d=0.3 V for the Al_Si+V_C channel."
    }
  ],
  "notes": "All outputs will be compared to hidden reference values from the literature; tolerances are not disclosed to the agent. The entire pipeline must be executed; the process step is enforced by the load-bearing scored step."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores each artifact. The verifier possesses reference values derived from the same physical systems, and it compares your computed numbers against these references using appropriate, hidden tolerances. For the band-structure and NEB steps, the extracted energies and barrier heights are compared directly. For the I-V curve, the leakage current at V_g=0 V and the threshold voltage (defined as V_g where I_d = 10 nA/µm) are evaluated against the reference. Each scored artifact contributes a weight (with the I-V curve carrying the largest share), and the total reward is the weighted sum. Reporting the correct numbers without having genuinely executed the pipeline is insufficient—your outputs must originate from the workflow steps described. The verifier does not rely on perfect bit-level matches; it accounts for the spread inherent in different computational implementations.
