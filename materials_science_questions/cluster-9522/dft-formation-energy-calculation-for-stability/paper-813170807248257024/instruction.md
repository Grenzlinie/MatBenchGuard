# DFT Bandgap Bowing of Mo1-xWxSe2 Monolayer Alloys

## Problem background
Two-dimensional (2D) transition metal dichalcogenides (TMDs) such as MoSe₂ and WSe₂ are direct-gap semiconductors with potential for optoelectronics. Alloying them, e.g., Mo₁₋ₓWₓSe₂, offers a route to continuously tune the bandgap. However, the bandgap of an alloy often deviates from a simple linear interpolation (Vegard’s law), exhibiting a “bowing” effect that can be important for device design. First-principles density functional theory (DFT) can predict the band structure of these alloys and quantify whether bowing occurs. This task asks you to compute, using DFT, the direct band gap at the K point of monolayer Mo₁₋ₓWₓSe₂ random alloys at several compositions, and then determine whether the bandgap follows a linear trend or exhibits bowing, by fitting a bowing model to the computed gaps.

## Approach
DFT calculations are performed with the PBE functional for monolayer Mo₁₋ₓWₓSe₂. The workflow consists of: (1) relaxing the primitive cells of MoSe₂ and WSe₂ to obtain equilibrium lattice constants; (2) constructing special quasirandom structure (SQS) supercells (e.g., 5x5 or 6x6) at compositions x=0.14 and 0.75, as well as the pure endpoints x=0 and 1, to approximate random alloy configurations; (3) calculating the band structure of each supercell and extracting the direct bandgap at the K point; (4) fitting the four bandgap values to the bowing equation E_g(x) = x·E_g(1) + (1−x)·E_g(0) − b·x·(1−x) to obtain the bowing parameter b. Any open-source DFT code implementing PBE (e.g., Quantum ESPRESSO, GPAW, ABINIT) may be used, together with standard pseudopotentials from the SSSP library or an equivalent set. The SQS supercells can be generated with available tools (ATAT, icet) or an equivalent random substitution algorithm that matches correlation functions close to a truly random alloy.

## Reproduction target
Produce two scored artifacts:
1. A CSV file `step_01_bandgaps.csv` containing the computed direct bandgap (in eV) for each composition x=0, 0.14, 0.75, and 1. Columns: `composition_x` (float), `calculated_bandgap_eV` (float).
2. A text file `step_02_bowing_parameter.txt` containing a single number: the fitted bowing parameter b (in eV), derived by least-squares fitting of the bandgap values to the bowing equation.
The four bandgap values must be obtained from the DFT calculations as described, and the fitted b must come from them.

## Assets

- Quantum ESPRESSO or other PBE-capable DFT code: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Monolayer MoSe2 reference crystal structure: https://materialsproject.org/materials/mp-1634
- Monolayer WSe2 reference crystal structure: https://materialsproject.org/materials/mp-1821
- Special Quasirandom Structure generator

## Workflow steps

### Step 1: Relax monolayer primitive cells
- Role: process
- Action: Obtain the initial monolayer MoSe2 and WSe2 primitive cell structures from public databases. Perform DFT geometry relaxation (cell vectors and atomic positions) using PBE to obtain equilibrium lattice constants.
- Evidence: `/app/outputs/relaxed_structures.log`

### Step 2: Generate random alloy supercells
- Role: process
- Action: Construct monolayer supercells (e.g., 5x5 or 6x6) for compositions x=0.14, 0.75 and the pure endpoints x=0,1 by substituting Mo with W, using a special quasirandom structure (SQS) approach or a random substitution strategy such that the correlation functions approximate a random alloy.
- Evidence: `/app/outputs/alloy_supercells_structures.json`

### Step 3: Compute band gaps for alloy supercells
- Role: scored (load-bearing)
- Action: For each composition (x=0, 0.14, 0.75, 1), perform a DFT self-consistent field calculation and band structure evaluation using the PBE functional. Extract the direct band gap at the K point.
- Output file: `/app/outputs/step_01_bandgaps.csv`
- Format: csv
- Contract: columns: composition_x (float), calculated_bandgap_eV (float). Rows for x=0, 0.14, 0.75, 1.
- Scoring: scored by hidden verifier

### Step 4: Fit bowing parameter
- Role: scored
- Action: Using the bandgap values from step_01_bandgaps.csv, fit the bowing equation E_g(x) = x*E_g(1)+(1-x)*E_g(0) - b*x*(1-x) to obtain the bowing parameter b.
- Output file: `/app/outputs/step_02_bowing_parameter.txt`
- Format: txt
- Contract: single floating-point number representing the fitted bowing parameter b (in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bandgaps.csv`
- `/app/outputs/step_02_bowing_parameter.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bandgaps.csv
- path: `/app/outputs/step_01_bandgaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed direct bandgap (eV) for each composition (x=0, 0.14, 0.75, 1) of monolayer Mo1-xWxSe2.
- schema:
  - `type`: table
  - `required_columns`: `composition_x`, `calculated_bandgap_eV`
  - `units`:
    - `calculated_bandgap_eV`: eV

### step_02_bowing_parameter.txt
- path: `/app/outputs/step_02_bowing_parameter.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Fitted bowing parameter b (in eV) derived from the bandgap bowing equation.
- schema:
  - `type`: text

Notes: Only the DFT bandgaps and derived bowing parameter are scored; experimental synthesis/characterization are excluded. The checker will also verify monotonic bandgap increase with x and a positive bowing parameter.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bandgaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_x",
          "calculated_bandgap_eV"
        ],
        "units": {
          "calculated_bandgap_eV": "eV"
        }
      },
      "description": "Computed direct bandgap (eV) for each composition (x=0, 0.14, 0.75, 1) of monolayer Mo1-xWxSe2."
    },
    {
      "file": "step_02_bowing_parameter.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Fitted bowing parameter b (in eV) derived from the bandgap bowing equation."
    }
  ],
  "notes": "Only the DFT bandgaps and derived bowing parameter are scored; experimental synthesis/characterization are excluded. The checker will also verify monotonic bandgap increase with x and a positive bowing parameter."
}
```

## How you are scored
A hidden verifier will independently read your submitted `step_01_bandgaps.csv` and `step_02_bowing_parameter.txt`. For the bandgap file, it compares each of your four bandgap values to reference values; for the bowing parameter file, it compares your b to a reference b. It also checks that your bandgap values increase monotonically with increasing x (the pure endpoints have known bandgaps). Scoring is based on how closely your numbers match the expected values within allowed tolerances; passing all checks yields the full reward, while large deviations or a violation of the monotonic trend reduces the score. The reference values are not disclosed; simply compute the quantities as accurately as possible following the prescribed protocol.
