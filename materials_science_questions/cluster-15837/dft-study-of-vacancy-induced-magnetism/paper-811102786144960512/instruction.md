# Hydrogen divacancy diffusion in MgH2: DFT calculation of formation energies and barriers

## Problem background
Magnesium hydride (MgH₂) is a promising solid-state hydrogen storage material due to its high gravimetric capacity, but its practical use is limited by slow hydrogen absorption and desorption kinetics. Hydrogen diffusion is a key rate-limiting step. Recent computational studies have suggested that hydrogen divacancies — pairs of adjacent hydrogen vacancies — may play an important role in the diffusion process. This task investigates the formation energy and diffusion barriers of hydrogen divacancies in bulk MgH₂ using density functional theory (DFT).

## Approach
The computational approach employs plane-wave DFT using the Quantum ESPRESSO suite with the PW91 exchange-correlation functional and ultrasoft pseudopotentials. The material is modeled in a 162-atom supercell (Mg₅₄H₁₀₈) with the rutile-type tetragonal structure (a = 4.501 Å, c/a = 0.6674, u = 3.22 Å). Divacancy configurations are created by removing specified pairs of H atoms from the pristine supercell.

Geometry optimizations are performed for the pristine cell and each defective configuration to obtain total energies and relaxed coordinates. Formation energies of divacancies are computed as FE = E(defective supercell) + E(H₂ molecule) − E(pristine supercell), where the H₂ molecule energy is obtained in a separate calculation.

For diffusion studies, the nudged elastic band (NEB) method with climbing image is used to determine minimum energy paths between initial and final divacancy states. Activation energies (the energy of the highest saddle point along the path) and the path length (the distance between vacancy positions at the rate-determining step) are extracted for the most favorable mechanisms along each Cartesian direction. The initial state is always the V2V3 divacancy; the final states and intermediate states are given in the workflow steps.

## Reproduction target
The goal is to compute two quantitative results:

1. Formation energies (in eV) and vacancy-vacancy distances (in Å) for the divacancy configurations V2V3, V1V2, and V2V6, reported in `/app/outputs/step_01_formation.json`.
2. Activation energies (in eV) and path lengths (in Å) for the most favorable diffusion mechanisms along the x, y, and z axes, reported in `/app/outputs/step_02_diffusion.json`.

The required initial and final states and the specific mechanisms to evaluate are defined in the workflow steps below. The reported numbers must result from your own DFT computations; they are not to be copied or guessed.

## Assets

- Quantum ESPRESSO v5.1: https://www.quantum-espresso.org
- H.pw91-van_ak.UPF: https://www.quantum-espresso.org/pseudopotentials
- Mg.pw91-np-van.UPF: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Supercell generation
- Role: process
- Action: Construct the MgH2 supercell (54 Mg, 108 H) with rutile structure (a=4.501 Å, c/a=0.6674, u=3.22 Å). Generate input files for pristine and required divacancy configurations (V2V3, V1V2, V2V6, V11V12, V8V9, V5V6, V2V1, V7V1, V11V1, V1V10, V5V3) by removing the specified hydrogen atom pairs.
- Evidence: `/app/outputs/supercell_inputs.txt`

### Step 2: Geometry relaxations
- Role: process
- Action: Relax pristine Mg54H108 and each divacancy supercell using spin-unrestricted DFT (PW91 functional, ultrasoft pseudopotentials, plane-wave cutoff 35 Ry, charge density cutoff 350 Ry, 2x2x2 Monkhorst-Pack k-point grid). Save total energies and relaxed coordinates.
- Evidence: `/app/outputs/relaxation_summary.txt`

### Step 3: Divacancy formation energies
- Role: scored
- Action: Compute formation energy for divacancies V2V3, V1V2, V2V6 using the total energies from relaxation and the H2 molecule energy, using the formula FE = E(defective) + E(H2) - E(pristine). Write results as JSON with an array of objects (label, FEVH2_eV, V_V_distance_ang) to /app/outputs/step_01_formation.json.
- Output file: `/app/outputs/step_01_formation.json`
- Format: json
- Contract: {"divacancies": [{"label": "string", "FEVH2_eV": "float", "V_V_distance_ang": "float"}]}
- Scoring: scored by hidden verifier

### Step 4: Diffusion barrier computation
- Role: scored (load-bearing)
- Action: Using the relaxed divacancy structures as initial and final states, run nudged elastic band (NEB) calculations with 7 images, climbing image algorithm, force convergence below 0.05 eV/Å, to determine the minimum energy paths and activation energies for the following processes: x-axis sequential intermediate mechanism (V2V3 → V2V1 → V7V1 → V11V1 → V11V12); y-axis simultaneous intermediate mechanism (V2V3 → V1V10 → V8V9); z-axis sequential direct mechanism (V2V3 → V5V3 → V5V6). Extract the activation energy (in eV) and path length (in Å) for the rate-determining step of each mechanism. Write the results to /app/outputs/step_02_diffusion.json.
- Output file: `/app/outputs/step_02_diffusion.json`
- Format: json
- Contract: {"x_axis": {"most_favorable_mechanism": "sequential intermediate", "rate_determining_step_energy_eV": "number", "path_length_ang": "number"}, "y_axis": {"most_favorable_mechanism": "simultaneous intermediate", "rate_determining_step_energy_eV": "number", "path_length_ang": "number"}, "z_axis": {"most_favorable_mechanism": "sequential direct", "rate_determining_step_energy_eV": "number", "path_length_ang": "number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation.json`
- `/app/outputs/step_02_diffusion.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation.json
- path: `/app/outputs/step_01_formation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies (eV) and vacancy-vacancy distances (Å) for divacancies V2V3, V1V2, V2V6.
- schema:
  - `type`: object
  - `required`: `divacancies`
  - `properties`:
    - `divacancies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `label`, `FEVH2_eV`, `V_V_distance_ang`
        - `properties`:
          - `label`:
            - `type`: string
          - `FEVH2_eV`:
            - `type`: number
            - `unit`: eV
          - `V_V_distance_ang`:
            - `type`: number
            - `unit`: Å

### step_02_diffusion.json
- path: `/app/outputs/step_02_diffusion.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Activation energies and path lengths for the most favorable divacancy diffusion mechanisms along the x, y, and z axes.
- schema:
  - `type`: object
  - `required`: `x_axis`, `y_axis`, `z_axis`
  - `properties`:
    - `x_axis`:
      - `type`: object
      - `required`: `most_favorable_mechanism`, `rate_determining_step_energy_eV`, `path_length_ang`
      - `properties`:
        - `most_favorable_mechanism`:
          - `type`: string
        - `rate_determining_step_energy_eV`:
          - `type`: number
          - `unit`: eV
        - `path_length_ang`:
          - `type`: number
          - `unit`: Å
    - `y_axis`:
      - `type`: object
      - `required`: `most_favorable_mechanism`, `rate_determining_step_energy_eV`, `path_length_ang`
      - `properties`:
        - `most_favorable_mechanism`:
          - `type`: string
        - `rate_determining_step_energy_eV`:
          - `type`: number
          - `unit`: eV
        - `path_length_ang`:
          - `type`: number
          - `unit`: Å
    - `z_axis`:
      - `type`: object
      - `required`: `most_favorable_mechanism`, `rate_determining_step_energy_eV`, `path_length_ang`
      - `properties`:
        - `most_favorable_mechanism`:
          - `type`: string
        - `rate_determining_step_energy_eV`:
          - `type`: number
          - `unit`: eV
        - `path_length_ang`:
          - `type`: number
          - `unit`: Å

Notes: The agent must execute full DFT relaxations and NEB calculations. Only the three specified divacancies for formation energies and the one most favorable mechanism per axis for diffusion barriers are required. The checker compares reported energies and distances to hidden reference values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "divacancies"
        ],
        "properties": {
          "divacancies": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "label",
                "FEVH2_eV",
                "V_V_distance_ang"
              ],
              "properties": {
                "label": {
                  "type": "string"
                },
                "FEVH2_eV": {
                  "type": "number",
                  "unit": "eV"
                },
                "V_V_distance_ang": {
                  "type": "number",
                  "unit": "Å"
                }
              }
            }
          }
        }
      },
      "description": "Formation energies (eV) and vacancy-vacancy distances (Å) for divacancies V2V3, V1V2, V2V6."
    },
    {
      "file": "step_02_diffusion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "x_axis",
          "y_axis",
          "z_axis"
        ],
        "properties": {
          "x_axis": {
            "type": "object",
            "required": [
              "most_favorable_mechanism",
              "rate_determining_step_energy_eV",
              "path_length_ang"
            ],
            "properties": {
              "most_favorable_mechanism": {
                "type": "string"
              },
              "rate_determining_step_energy_eV": {
                "type": "number",
                "unit": "eV"
              },
              "path_length_ang": {
                "type": "number",
                "unit": "Å"
              }
            }
          },
          "y_axis": {
            "type": "object",
            "required": [
              "most_favorable_mechanism",
              "rate_determining_step_energy_eV",
              "path_length_ang"
            ],
            "properties": {
              "most_favorable_mechanism": {
                "type": "string"
              },
              "rate_determining_step_energy_eV": {
                "type": "number",
                "unit": "eV"
              },
              "path_length_ang": {
                "type": "number",
                "unit": "Å"
              }
            }
          },
          "z_axis": {
            "type": "object",
            "required": [
              "most_favorable_mechanism",
              "rate_determining_step_energy_eV",
              "path_length_ang"
            ],
            "properties": {
              "most_favorable_mechanism": {
                "type": "string"
              },
              "rate_determining_step_energy_eV": {
                "type": "number",
                "unit": "eV"
              },
              "path_length_ang": {
                "type": "number",
                "unit": "Å"
              }
            }
          }
        }
      },
      "description": "Activation energies and path lengths for the most favorable divacancy diffusion mechanisms along the x, y, and z axes."
    }
  ],
  "notes": "The agent must execute full DFT relaxations and NEB calculations. Only the three specified divacancies for formation energies and the one most favorable mechanism per axis for diffusion barriers are required. The checker compares reported energies and distances to hidden reference values with tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each scored output file against reference values derived from the original publication. The verifier compares the formation energies and distances, as well as the diffusion barriers and path lengths, using appropriate tolerances. The final reward (a number between 0 and 1) is a weighted combination of the scores for `step_01_formation.json` and `step_02_diffusion.json`. The verifier does not merely check for existence or correct format; it requires numerically accurate results that could only be obtained by properly executing the DFT and NEB workflow. Reporting arbitrary numbers or reusing published values without performing the calculations will not pass the scoring.
