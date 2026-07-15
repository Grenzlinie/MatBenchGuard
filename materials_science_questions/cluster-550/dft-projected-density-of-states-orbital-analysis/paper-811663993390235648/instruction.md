# DFT structural and elastic properties of cubic Zr3N4 and Hf3N4

## Problem background
Transition metal nitrides such as Zr3N4 and Hf3N4 are promising for hard coatings and electronic applications due to their high hardness, thermal stability, and interesting electronic properties. First-principles density functional theory (DFT) calculations can predict their ground-state equilibrium structural parameters, equation-of-state behavior, and mechanical stiffness. This task challenges you to compute the equilibrium lattice constant, bulk modulus, its pressure derivative, and the three independent single-crystal elastic constants of the cubic Th3P4-type phases of Zr3N4 and Hf3N4 using DFT with the GGA-PBE exchange-correlation functional. The results will be compared to independently established reference values, providing a rigorous test of your DFT workflow.

## Approach
The computational method is plane-wave pseudopotential DFT within the generalized gradient approximation (GGA-PBE). You will model both compounds in the cubic Th3P4 structure (space group I-43d) with the metal atoms occupying Wyckoff position (3/8, 0, 1/4) and nitrogen at (0.063, 0.063, 0.063). The workflow proceeds in stages: (1) construct initial crystal structure input files, (2) perform zero-pressure structural relaxation to obtain equilibrium lattice constants and volumes, (3) carry out a series of cell optimizations at hydrostatic pressures from 0 to 30 GPa to generate pressure-volume data, (4) fit these data to the third-order Birch-Murnaghan equation of state with the zero-pressure volume fixed to extract the bulk modulus and its pressure derivative, (5) compute the three independent elastic stiffness constants at zero pressure using the static finite strain method, and (6) compile the final set of properties into a single JSON output file. An open-source plane-wave code such as Quantum ESPRESSO and public SSSP efficiency pseudopotentials for Zr, Hf, and N are suitable substitutes for the proprietary CASTEP code originally used.

## Reproduction target
Your objective is to produce a single JSON file containing the equilibrium lattice constant a0 (in Å), zero-pressure bulk modulus B0 (in GPa), pressure derivative B0′, and the three elastic constants C11, C12, C44 (in GPa) for both Zr3N4 and Hf3N4. The file must be written to `/app/outputs/computed_properties.json` and follow the exact structure specified in the output contract. The values you report should be the direct result of your DFT computations using GGA-PBE; no additional corrections or empirical adjustments are required.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (Zr, Hf, N): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate initial crystal structures
- Role: process
- Action: Build the cubic Th3P4-type (space group I-43d) unit cells for Zr3N4 and Hf3N4 with correct Wyckoff positions (Zr/Hf at (3/8,0,1/4); N at (0.063,0.063,0.063)) and prepare input files suitable for DFT calculations.
- Evidence: `/app/outputs/structures_input.txt`

### Step 2: Zero-pressure structural relaxation
- Role: process
- Action: Perform full cell and ionic relaxation at zero pressure using GGA-PBE exchange-correlation, appropriate plane-wave cutoff and k-point sampling, converging forces and stresses below standard thresholds to obtain the equilibrium lattice constant and volume.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 3: Pressure-dependent cell optimizations
- Role: process
- Action: Run DFT cell optimizations at a set of hydrostatic pressures from 0 to 30 GPa for each compound, recording the converged unit-cell volume at each pressure to generate P(V) data.
- Evidence: `/app/outputs/PV_data.csv`

### Step 4: Birch-Murnaghan equation of state fitting
- Role: process
- Action: Fit the P(V) data to the third-order Birch-Murnaghan equation using least-squares regression, with the equilibrium volume V0 fixed at the zero-pressure optimized value. Extract the bulk modulus B0 and pressure derivative B0'.
- Evidence: `/app/outputs/eos_fit_results.txt`

### Step 5: Elastic constants calculation
- Role: process
- Action: Compute the single-crystal elastic stiffness constants C11, C12, C44 at zero pressure for both compounds using the static finite strain method within DFT.
- Evidence: `/app/outputs/elastic_constants_log.txt`

### Step 6: Compile final structural and elastic properties
- Role: scored (load-bearing)
- Action: Gather the equilibrium lattice constant a0 (in Å), zero-pressure bulk modulus B0 (in GPa), pressure derivative B0', and elastic constants C11, C12, C44 (in GPa) for both Zr3N4 and Hf3N4 into a single JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {"Zr3N4":{"lattice_constant_a0":"number (Å)","bulk_modulus_B0":"number (GPa)","pressure_derivative_B0p":"number","elastic_constant_C11":"number (GPa)","elastic_constant_C12":"number (GPa)","elastic_constant_C44":"number (GPa)"},"Hf3N4":{"lattice_constant_a0":"number (Å)","bulk_modulus_B0":"number (GPa)","pressure_derivative_B0p":"number","elastic_constant_C11":"number (GPa)","elastic_constant_C12":"number (GPa)","elastic_constant_C44":"number (GPa)"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the computed equilibrium lattice constant, bulk modulus, pressure derivative, and three elastic constants for both Zr3N4 and Hf3N4.
- schema:
  - `type`: object
  - `required`: `Zr3N4`, `Hf3N4`
  - `properties`:
    - `Zr3N4`:
      - `type`: object
      - `required`: `lattice_constant_a0`, `bulk_modulus_B0`, `pressure_derivative_B0p`, `elastic_constant_C11`, `elastic_constant_C12`, `elastic_constant_C44`
      - `properties`:
        - `lattice_constant_a0`:
          - `type`: number
          - `units`: Å
        - `bulk_modulus_B0`:
          - `type`: number
          - `units`: GPa
        - `pressure_derivative_B0p`:
          - `type`: number
        - `elastic_constant_C11`:
          - `type`: number
          - `units`: GPa
        - `elastic_constant_C12`:
          - `type`: number
          - `units`: GPa
        - `elastic_constant_C44`:
          - `type`: number
          - `units`: GPa
    - `Hf3N4`:
      - `type`: object
      - `required`: `lattice_constant_a0`, `bulk_modulus_B0`, `pressure_derivative_B0p`, `elastic_constant_C11`, `elastic_constant_C12`, `elastic_constant_C44`
      - `properties`:
        - `lattice_constant_a0`:
          - `type`: number
          - `units`: Å
        - `bulk_modulus_B0`:
          - `type`: number
          - `units`: GPa
        - `pressure_derivative_B0p`:
          - `type`: number
        - `elastic_constant_C11`:
          - `type`: number
          - `units`: GPa
        - `elastic_constant_C12`:
          - `type`: number
          - `units`: GPa
        - `elastic_constant_C44`:
          - `type`: number
          - `units`: GPa

Notes: The output contract declares a single scored artifact. The hidden checker compares the reported values to reference (paper-reported) values using appropriate tolerances; only the shape and fields are specified here. The target policy is reference_match because the quantities are method-dependent computational results, not universally fixed constants.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Zr3N4",
          "Hf3N4"
        ],
        "properties": {
          "Zr3N4": {
            "type": "object",
            "required": [
              "lattice_constant_a0",
              "bulk_modulus_B0",
              "pressure_derivative_B0p",
              "elastic_constant_C11",
              "elastic_constant_C12",
              "elastic_constant_C44"
            ],
            "properties": {
              "lattice_constant_a0": {
                "type": "number",
                "units": "Å"
              },
              "bulk_modulus_B0": {
                "type": "number",
                "units": "GPa"
              },
              "pressure_derivative_B0p": {
                "type": "number"
              },
              "elastic_constant_C11": {
                "type": "number",
                "units": "GPa"
              },
              "elastic_constant_C12": {
                "type": "number",
                "units": "GPa"
              },
              "elastic_constant_C44": {
                "type": "number",
                "units": "GPa"
              }
            }
          },
          "Hf3N4": {
            "type": "object",
            "required": [
              "lattice_constant_a0",
              "bulk_modulus_B0",
              "pressure_derivative_B0p",
              "elastic_constant_C11",
              "elastic_constant_C12",
              "elastic_constant_C44"
            ],
            "properties": {
              "lattice_constant_a0": {
                "type": "number",
                "units": "Å"
              },
              "bulk_modulus_B0": {
                "type": "number",
                "units": "GPa"
              },
              "pressure_derivative_B0p": {
                "type": "number"
              },
              "elastic_constant_C11": {
                "type": "number",
                "units": "GPa"
              },
              "elastic_constant_C12": {
                "type": "number",
                "units": "GPa"
              },
              "elastic_constant_C44": {
                "type": "number",
                "units": "GPa"
              }
            }
          }
        }
      },
      "description": "JSON file containing the computed equilibrium lattice constant, bulk modulus, pressure derivative, and three elastic constants for both Zr3N4 and Hf3N4."
    }
  ],
  "notes": "The output contract declares a single scored artifact. The hidden checker compares the reported values to reference (paper-reported) values using appropriate tolerances; only the shape and fields are specified here. The target policy is reference_match because the quantities are method-dependent computational results, not universally fixed constants."
}
```

## How you are scored
A hidden verifier reads your final output file and validates that all required fields are present and contain appropriate numeric values. The verifier then compares each computed value against independently established reference values using tolerances that account for normal computational variability (different DFT codes, pseudopotentials, convergence settings). Each value that falls within its tolerance earns partial credit, and the total reward is the weighted sum across all values for both compounds. No credit is given for simply reporting expected numbers; only computed results consistent with the procedure outlined in the workflow earn points. Intermediate evidence files (e.g., PV_data.csv, elastic_constants_log.txt) are not directly scored but may be inspected to confirm that the required steps were executed.
