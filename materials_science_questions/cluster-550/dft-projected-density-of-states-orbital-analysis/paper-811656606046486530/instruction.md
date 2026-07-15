# DFT Relaxation and Density-of-States Analysis for a Rare-Earth Chalcogenide

## Problem background
High-temperature thermoelectric materials are sought for waste-heat recovery and power generation. Rare-earth chalcogenides with Th3P4 structure have attracted interest because their partially filled 4f or 5d bands can produce sharp features in the density of states (DOS) near the Fermi level. When a conduction band DOS is concentrated in a nearly delta-function shape, the Mahan–Sofo theory predicts that the thermoelectric figure of merit zT can be greatly enhanced. This task targets the cerium telluride Ce3Te4 primitive cell: using first-principles DFT calculations to determine whether a sharp DOS peak from Ce 4f electrons exists above the Fermi level, and to quantify the resulting ideal zT at 1200 K. The outcome will establish whether Ce3Te4 is a promising high-temperature thermoelectric material according to this simple analytical model.

## Approach
The workflow consists of three stages. First, a DFT structural relaxation of the Ce3Te4 primitive cell (6 Ce, 8 Te, Th3P4 structure) is performed using the GGA-PBE exchange-correlation functional. Starting from the experimental lattice constant 9.553 Å, the cell shape is relaxed until forces are below a chosen threshold; the equilibrium lattice constant a0 is extracted. Second, a self-consistent field (SCF) run on the relaxed structure computes the total density of states (TDOS). From the TDOS, the energy position (relative to the Fermi level) and height of the most prominent conduction-band DOS peak are recorded. Third, the Mahan–Sofo analytical model is applied. This model expresses the electronic thermal conductivity in terms of a transport distribution function; its figure‑of‑merit zT is maximized when the distribution is a delta function located at roughly ±2.4 kBT from the Fermi level. Using the DOS peak energy from step 2 and the fixed parameters lattice thermal conductivity k_l = 1 W m⁻¹ K⁻¹, mean free path = 0.3 nm, b = ±2.4 kBT, and T = 1200 K, the ideal dimensionless zT is computed. All calculations can use open-source plane-wave DFT codes (e.g., Quantum ESPRESSO) with standard GGA-PBE pseudopotentials.

## Reproduction target
Produce the following three artifacts in the output directory:

1. The relaxed equilibrium lattice constant a0 of Ce3Te4 (in Å).
2. The energy and height of the sharpest conduction-band DOS peak above the Fermi level: energy in eV (positive if above), height in states per eV per unit cell.
3. The ideal thermoelectric figure of merit zT at 1200 K obtained from the Mahan–Sofo model using the DOS peak location and the supplied model parameters.

The outputs must be written exactly as described in the workflow steps: a plain text file for the lattice constant, a JSON file for the DOS peak properties, and a plain text file for zT.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for Ce and Te (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/
- Ce3Te4 primitive cell structure description

## Workflow steps

### Step 1: DFT relaxation and equilibrium lattice constant
- Role: scored
- Action: Perform a DFT structural relaxation of the Ce3Te4 primitive cell using the conjugate‑gradient method to minimize atomic forces below a threshold, employing GGA‑PBE pseudopotentials with appropriate plane‑wave basis and k‑point sampling. Start from the experimental lattice constant of 9.553 Å. Output the relaxed equilibrium lattice constant a0 in Å.
- Output file: `/app/outputs/step_01_lattice_constant.txt`
- Format: txt
- Contract: A single line with a floating-point number.
- Scoring: scored by hidden verifier

### Step 2: DFT SCF and density of states analysis
- Role: scored (load-bearing)
- Action: Using the relaxed structure from step 1, run a self‑consistent field (SCF) DFT calculation with the same functional and computational settings. Compute the total density of states (TDOS) and partial density of states (PDOS). From the TDOS, identify the sharp conduction‑band peak above the Fermi level: record its energy position relative to the Fermi level (eV) and its height (states/(eV·unit cell)). Save these two quantities in a JSON file.
- Output file: `/app/outputs/step_02_dos_peak.json`
- Format: json
- Contract: {"peak_energy_eV": <float>, "peak_height_states_per_eV_per_unit_cell": <float>}
- Scoring: scored by hidden verifier

### Step 3: Ideal zT estimation (Mahan–Sofo model)
- Role: scored
- Action: Using the DOS peak energy from step 2, apply the Mahan–Sofo analytical model to compute the ideal dimensionless thermoelectric figure of merit zT at 1200 K. Use fixed model parameters: lattice thermal conductivity k_l = 1 W/(m·K), mean free path = 0.3 nm, and b = ±2.4 k_B T. Output the resulting zT value in a plain text file.
- Output file: `/app/outputs/step_03_zt_value.txt`
- Format: txt
- Contract: A single line with a floating-point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_constant.txt`
- `/app/outputs/step_02_dos_peak.json`
- `/app/outputs/step_03_zt_value.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_constant.txt
- path: `/app/outputs/step_01_lattice_constant.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constant obtained from DFT structural relaxation.
- schema:
  - `type`: text
  - `value_format`: single floating-point number
  - `units`: angstroms

### step_02_dos_peak.json
- path: `/app/outputs/step_02_dos_peak.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Position (eV above Fermi level) and height of the delta‑shaped conduction‑band DOS peak.
- schema:
  - `type`: object
  - `required`: `peak_energy_eV`, `peak_height_states_per_eV_per_unit_cell`
  - `properties`:
    - `peak_energy_eV`:
      - `type`: number
      - `unit`: eV
    - `peak_height_states_per_eV_per_unit_cell`:
      - `type`: number
      - `unit`: states/(eV·unit cell)

### step_03_zt_value.txt
- path: `/app/outputs/step_03_zt_value.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Ideal thermoelectric figure of merit zT at 1200 K computed from the Mahan‑Sofo model.
- schema:
  - `type`: text
  - `value_format`: single floating-point number
  - `units`: dimensionless

Notes: All three outputs are compared to hidden reference values with tolerances appropriate for the chosen DFT implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_constant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "value_format": "single floating-point number",
        "units": "angstroms"
      },
      "description": "Equilibrium lattice constant obtained from DFT structural relaxation."
    },
    {
      "file": "step_02_dos_peak.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "peak_energy_eV",
          "peak_height_states_per_eV_per_unit_cell"
        ],
        "properties": {
          "peak_energy_eV": {
            "type": "number",
            "unit": "eV"
          },
          "peak_height_states_per_eV_per_unit_cell": {
            "type": "number",
            "unit": "states/(eV·unit cell)"
          }
        }
      },
      "description": "Position (eV above Fermi level) and height of the delta‑shaped conduction‑band DOS peak."
    },
    {
      "file": "step_03_zt_value.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "value_format": "single floating-point number",
        "units": "dimensionless"
      },
      "description": "Ideal thermoelectric figure of merit zT at 1200 K computed from the Mahan‑Sofo model."
    }
  ],
  "notes": "All three outputs are compared to hidden reference values with tolerances appropriate for the chosen DFT implementation."
}
```

## How you are scored
Each workflow step produces a single output file. After your run, a hidden verifier will read each file independently and compare your computed numbers against a set of hidden reference values, using tolerances that absorb legitimate differences arising from DFT code versions, pseudopotential choices, and numerical settings. The three stages are scored individually, and a weighted average across the stages gives your final reward (from 0 to 1). Reporting a number without actually performing the required calculations is not sufficient; the tolerances are chosen so that only a correct execution of the described workflow yields full credit.
