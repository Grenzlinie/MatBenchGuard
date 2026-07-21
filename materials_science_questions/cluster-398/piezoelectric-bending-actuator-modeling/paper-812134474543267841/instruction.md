# Shear-mode PZT actuator poling voltage simulation

## Problem background
A shear-mode PZT actuator requires a lateral (in-plane) poling process to align ferroelectric domains perpendicular to the later actuating electric field. The poling field must exceed the material's coercive field (4 MV/m) in most of the intended poled region. Two electrode arrangements are possible: placing the poling electrodes on only one surface of the piezoelectric plate (single-surface design) or on both surfaces (dual-surface design). The poling voltage needed to achieve a given extent of polarization depends on the electrode layout and the plate thickness. This task asks you to compute, via electrostatic finite-element simulation, the poling voltage that yields 85% of the expected poled region above the coercive field for both designs and for three plate thicknesses (220 µm, 250 µm, 280 µm).

## Approach
Construct a 2D electrostatic finite-element model of the plate cross-section around the poling electrodes. The material is assigned a uniform relative permittivity of 2000. Use an open-source FEM solver (e.g., FEniCS, deal.II, Elmer). For the single-surface design, define the electrode geometry on one surface only; for the dual-surface design, define electrodes on opposite surfaces. Apply known potentials to the electrodes and ground the appropriate boundaries. Solve the Laplace equation for the electric potential and extract the lateral electric field component, Ex.

For each design and each thickness (220, 250, 280 µm), sweep the applied poling voltage over a range that allows the fraction of the poled region where |Ex| ≥ 4×10⁶ V/m to pass through 85%. From the simulated Ex distributions, compute the spatial fraction of the expected poled region that exceeds the coercive field. Interpolate to find the voltage that yields exactly 85% coverage. This procedure yields six voltages (two designs × three thicknesses).

## Reproduction target
Produce a CSV file named poling_voltages.csv with exactly three columns: design (string, either 'single' or 'dual'), thickness_um (integer, 220, 250, or 280), and voltage_V (float, the applied poling voltage in volts). The file must contain exactly six rows, one for each combination of design and thickness. The voltages you report are the primary quantity to be evaluated.

## Assets

- Open-source 2D electrostatic FEM solver: https://fenicsproject.org/

## Workflow steps

### Step 1: Set up 2D electrostatic FEM model
- Role: process
- Action: Define the 2D cross-sectional geometry of the plate around the expected poled region for both the single-surface and dual-surface electrode designs. Assign uniform relative permittivity εr = 2000 and coercive field threshold Ec = 4×10^6 V/m. Generate a mesh and apply appropriate electrostatic boundary conditions (voltage on electrodes, ground on relevant surfaces).
- Evidence: `/app/outputs/model_setup.log`

### Step 2: Run electrostatic field simulations
- Role: process
- Action: For each combination of poling design (single-surface, dual-surface) and plate thickness (220 µm, 250 µm, 280 µm), run the finite-element simulation for a range of applied poling voltages. For each run, extract the lateral electric field component Ex within the intended poled region.
- Evidence: `/app/outputs/simulation_output.log`

### Step 3: Determine poling voltages for 85% poled-region coverage
- Role: scored (load-bearing)
- Action: For each design and thickness, from the simulated Ex distributions compute the fraction of the expected poled region where |Ex| ≥ Ec. Determine the poling voltage at which this fraction reaches exactly 85% (interpolate if needed). Record the resulting six voltages.
- Output file: `/app/outputs/poling_voltages.csv`
- Format: csv
- Contract: Columns: design (string: 'single' or 'dual'), thickness_um (integer: 220, 250, 280), voltage_V (float). Exactly 6 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/poling_voltages.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### poling_voltages.csv
- path: `/app/outputs/poling_voltages.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed poling voltages for 85% poled-region coverage. The hidden checker compares these values to the paper's reported targets within a tolerance and enforces the ordering dual-surface < single-surface for each thickness.
- schema:
  - `type`: table
  - `required_columns`: `design`, `thickness_um`, `voltage_V`
  - `units`:
    - `thickness_um`: µm
    - `voltage_V`: V

Notes: Only the dry electrostatic simulation is reproduced; the experimental poling, crack observations, and d15 measurements are excluded. The agent must use an open-source FEM solver; the proprietary ANSYS tool used in the paper is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "poling_voltages.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "design",
          "thickness_um",
          "voltage_V"
        ],
        "units": {
          "thickness_um": "µm",
          "voltage_V": "V"
        }
      },
      "description": "Computed poling voltages for 85% poled-region coverage. The hidden checker compares these values to the paper's reported targets within a tolerance and enforces the ordering dual-surface < single-surface for each thickness."
    }
  ],
  "notes": "Only the dry electrostatic simulation is reproduced; the experimental poling, crack observations, and d15 measurements are excluded. The agent must use an open-source FEM solver; the proprietary ANSYS tool used in the paper is not required."
}
```

## How you are scored
The file poling_voltages.csv is the sole scored artifact. A hidden verifier will compare each of the six voltages against reference values (derived from the same simulation protocol) and will also check the internal consistency among designs and thicknesses. Each correct row earns equal credit; the final score is the average of the six row-level scores.
