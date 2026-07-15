# Thermodynamic analysis of core-shell carbide formation in Fe-Cr-C alloys

## Problem background
High-chromium cast irons (HCCIs) can form core‑shell structured carbides — an M₇C₃ core surrounded by an M₂₃C₆ shell — that reduce stress concentration at the carbide/matrix interface and thereby improve wear resistance. Understanding the thermodynamic conditions (composition ranges and temperatures) under which such core‑shell structures can appear is critical for alloy design. This computational study investigates, entirely through thermodynamic calculations in the Fe‑Cr‑C ternary system, what composition domains and processing regimes make the core (M₇C₃)–shell (M₂₃C₆) morphology possible.

## Approach
The analysis uses the CALPHAD (CALculation of PHAse Diagrams) method with the open-source Python library pycalphad and the Khvan Fe‑Cr‑C thermodynamic database. Three linked stages are performed:

1. **Stable phase diagrams** – Isopleth sections at fixed Cr levels are computed to locate the three‑phase region where Matrix (FCC/BCC), M₇C₃, and M₂₃C₆ coexist. This region constitutes the compositional prerequisite for core‑shell carbide formation.
2. **Solidification‑path analysis** – Scheil‑Gulliver (no solid‑state diffusion) and Lever‑Rule (equilibrium) solidification simulations are run for nine Fe‑Cr‑C alloys whose compositions sample the three‑phase region. The step‑by‑step phase sequences are recorded; the presence of a eutectic Matrix+M₇C₃ colony — the microstructure that can subsequently develop a shell — is noted.
3. **Nucleation driving force** – For those alloys that form a eutectic colony, the interfacial composition of the matrix in metastable local equilibrium with M₇C₃ is determined at a heat‑treatment temperature of 1000 °C. Using the parallel‑tangent method, the driving force for M₂₃C₆ nucleation at that interface is computed and compared to a benchmark, yielding a yes/no expectation for shell formation.

The workflow thus reproduces the thermodynamic reasoning originally performed with commercial software.

## Reproduction target
Compute, from the Khvan Fe‑Cr‑C database with pycalphad:

- **Three‑phase region boundaries** (Matrix + M₇C₃ + M₂₃C₆) in stable isopleths at Cr = 10, 15, 20, 25, 30, 35, 40, and 45 wt%, over the temperature range ≈800–1600 °C. For each Cr level report the carbon‑composition window (C_min, C_max in wt%) and the temperature window (T_min, T_max in °C) of the three‑phase region.
- **Solidification step sequences** for the nine Fe‑Cr‑C alloys listed in the task instruction, under both Scheil‑Gulliver and Lever‑Rule cooling. For every step, record the alloy label, the cooling model, the step order, start and end temperatures (°C), and the phases involved.
- **Nucleation driving force** for M₂₃C₆ at the M₇C₃/Matrix interface at 1000 °C, for each alloy that exhibited a eutectic Matrix+M₇C₃ colony after Scheil solidification. Report the driving force in J/mol and a boolean assessment of whether shell formation is expected based on that driving force.

The outputs must be written to the files and formats specified in the workflow steps.

## Assets

- Fe-Cr-C thermodynamic database (Khvan 2014): 10.1016/j.calphad.2014.03.001
- pycalphad: pycalphad
- Python scientific stack (numpy, pandas, matplotlib): numpy pandas matplotlib

## Workflow steps

### Step 1: Calculate stable phase diagrams and three-phase region
- Role: scored
- Action: Using pycalphad with the Khvan Fe-Cr-C thermodynamic database, compute stable isopleth phase diagrams for Cr contents 10, 15, 20, 25, 30, 35, 40, 45 wt% over the temperature range approximately 800–1600 °C. For each Cr level, identify the temperature and carbon composition range where Matrix (FCC/BCC) + M7C3 + M23C6 coexist (the three-phase region). Output the boundaries as an array of objects.
- Output file: `/app/outputs/phase_diagrams.json`
- Format: json
- Contract: Array of objects, each with fields: Cr_wt (number, wt%), C_min_wt (number, wt%), C_max_wt (number, wt%), T_min_C (number, °C), T_max_C (number, °C).
- Scoring: scored by hidden verifier

### Step 2: Simulate Scheil-Gulliver and Lever-Rule solidification paths
- Role: scored
- Action: For the nine alloys with nominal compositions (provided in the task instruction), run Scheil-Gulliver solidification (no solid diffusion, infinite liquid diffusion) and Lever-Rule (equilibrium) solidification using pycalphad. For each alloy and each cooling mode, record the sequence of phase transformations with start and end temperatures and the phases involved.
- Output file: `/app/outputs/solidification_steps.csv`
- Format: csv
- Contract: CSV with columns: composition (alloy label), model ('Scheil' or 'Lever'), step_order (integer), start_temp_C (float, °C), end_temp_C (float, °C), phases_sequence (string).
- Scoring: scored by hidden verifier

### Step 3: Calculate nucleation driving force for M23C6 at the M7C3/matrix interface
- Role: scored (load-bearing)
- Action: For each alloy that formed a eutectic colony (Matrix+M7C3) under Scheil solidification, determine the interfacial composition of the matrix in metastable local equilibrium with M7C3 at 1000 °C using pycalphad. Apply the parallel tangent method to compute the driving force for nucleation of M23C6 from that interface. Report the driving force and whether core-shell carbide formation is expected based on the magnitude of the driving force.
- Output file: `/app/outputs/driving_force_interface.csv`
- Format: csv
- Contract: CSV with columns: composition (alloy label), driving_force_J_per_mol (float, J/mol), shell_possible (True/False).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagrams.json`
- `/app/outputs/solidification_steps.csv`
- `/app/outputs/driving_force_interface.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagrams.json
- path: `/app/outputs/phase_diagrams.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Three-phase region boundaries for each chromium content.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `Cr_wt`, `C_min_wt`, `C_max_wt`, `T_min_C`, `T_max_C`
    - `properties`:
      - `Cr_wt`:
        - `type`: number
        - `unit`: wt%
      - `C_min_wt`:
        - `type`: number
        - `unit`: wt%
      - `C_max_wt`:
        - `type`: number
        - `unit`: wt%
      - `T_min_C`:
        - `type`: number
        - `unit`: °C
      - `T_max_C`:
        - `type`: number
        - `unit`: °C

### solidification_steps.csv
- path: `/app/outputs/solidification_steps.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Solidification step sequences for nine alloys under Scheil-Gulliver and Lever-Rule cooling.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `model`, `step_order`, `start_temp_C`, `end_temp_C`, `phases_sequence`
  - `units`:
    - `start_temp_C`: °C
    - `end_temp_C`: °C

### driving_force_interface.csv
- path: `/app/outputs/driving_force_interface.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Driving force for M23C6 nucleation at the M7C3/matrix interface and the resulting shell formation possibility.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `driving_force_J_per_mol`, `shell_possible`
  - `units`:
    - `driving_force_J_per_mol`: J/mol

Notes: The nine alloy compositions are provided in the task instruction. All calculations must use the Khvan Fe-Cr-C thermodynamic database and pycalphad. Tolerances account for implementation differences between pycalphad and the original Pandat software.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagrams.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "Cr_wt",
            "C_min_wt",
            "C_max_wt",
            "T_min_C",
            "T_max_C"
          ],
          "properties": {
            "Cr_wt": {
              "type": "number",
              "unit": "wt%"
            },
            "C_min_wt": {
              "type": "number",
              "unit": "wt%"
            },
            "C_max_wt": {
              "type": "number",
              "unit": "wt%"
            },
            "T_min_C": {
              "type": "number",
              "unit": "°C"
            },
            "T_max_C": {
              "type": "number",
              "unit": "°C"
            }
          }
        }
      },
      "description": "Three-phase region boundaries for each chromium content."
    },
    {
      "file": "solidification_steps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "model",
          "step_order",
          "start_temp_C",
          "end_temp_C",
          "phases_sequence"
        ],
        "units": {
          "start_temp_C": "°C",
          "end_temp_C": "°C"
        }
      },
      "description": "Solidification step sequences for nine alloys under Scheil-Gulliver and Lever-Rule cooling."
    },
    {
      "file": "driving_force_interface.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "driving_force_J_per_mol",
          "shell_possible"
        ],
        "units": {
          "driving_force_J_per_mol": "J/mol"
        }
      },
      "description": "Driving force for M23C6 nucleation at the M7C3/matrix interface and the resulting shell formation possibility."
    }
  ],
  "notes": "The nine alloy compositions are provided in the task instruction. All calculations must use the Khvan Fe-Cr-C thermodynamic database and pycalphad. Tolerances account for implementation differences between pycalphad and the original Pandat software."
}
```

## How you are scored
Each of the three scored artifacts (`phase_diagrams.json`, `solidification_steps.csv`, `driving_force_interface.csv`) is evaluated independently by a hidden verifier. The verifier either recomputes the quantities from the same database and protocol, or checks consistency with expected thermodynamic behavior, and compares your submitted values to a hidden reference. It then assigns a partial score to each artifact; the final reward is a weighted sum of those partial scores, with the driving‑force step (`driving_force_interface.csv`) carrying the largest weight. Reporting numbers that match the original publication is not enough — the verifier tests whether the artifacts genuinely obey the physics encoded in the database and the requested calculations.
