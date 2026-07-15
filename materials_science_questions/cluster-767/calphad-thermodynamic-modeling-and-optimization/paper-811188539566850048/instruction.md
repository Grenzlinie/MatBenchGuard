# Thermodynamic Optimization of B2O3-FeO-Fe2O3-Nd2O3 Oxide Slag System

## Problem background
Recycling of NdFeB permanent magnets is hindered by the challenge of recovering neodymium, which readily oxidizes. Designing efficient oxidation-based recycling processes requires reliable phase diagrams and thermochemical data for the B2O3-FeO-Fe2O3-Nd2O3 oxide slag system. The iron-saturated FeO-Nd2O3 subsystem is particularly important, yet its high-temperature phase equilibria were not available before the underlying experimental study. This task reproduces the core thermodynamic modeling: fitting liquid solution parameters to experimental phase diagram data using the Modified Quasichemical Model, and then computing the resulting FeO-Nd2O3 phase diagram. Successfully reproducing the liquid parameters and phase diagram demonstrates the ability to predict key invariant points and the overall topology, which is the foundation for later process design.

## Approach
The approach is a CALPHAD-style thermodynamic optimization. Implement the Modified Quasichemical Model (MQM) for the liquid oxide phase in four binary systems: FeO-Nd2O3, B2O3-Nd2O3, FeO-B2O3, and Fe2O3-Nd2O3. In the MQM, the liquid Gibbs energy is expressed in terms of pair fractions of second-nearest-neighbor cation pairs, with configurational entropy and a composition-dependent pair-exchange energy Δg. Using the provided experimental data (liquidus points, eutectic/melting temperatures, miscibility gaps) and the fixed solid compound thermodynamic properties (ΔH, S, Cp), formulate an objective function that captures the discrepancy between calculated and experimental phase equilibrium boundaries. Perform non-linear optimization to determine the polynomial coefficients of Δg that minimize this discrepancy. Once the liquid parameters are optimized, fix them and compute the iron-saturated FeO-Nd2O3 phase diagram by solving the equilibrium conditions (Gibbs energy minimization) over the full composition range at a set of temperatures, tracing the liquidus and solidus curves.

## Reproduction target
Using the provided experimental phase equilibrium datasets and solid compound thermodynamic properties, optimize the MQM liquid pair-exchange energy parameters for the four binary systems and produce:
1. A JSON file (`optimized_liquid_parameters.json`) containing the optimized Δg coefficients for each binary.
2. A CSV file (`feo_nd2o3_phase_diagram.csv`) that samples the iron-saturated FeO-Nd2O3 phase diagram, recording temperature, FeO composition, and stable phase identifier along the liquidus and solidus.

The computed phase diagram must capture the principal topological features consistent with the experimental observations: the two eutectic reactions (FeO + NdFeO3 → liquid and Nd2O3 + NdFeO3 → liquid) and the melting behavior of the intermediate compound NdFeO3. The optimized liquid parameters should be physically plausible and lead to a phase diagram that faithfully reflects the provided experimental constraints.

## Assets

- FeO-Nd2O3 experimental data (DTA, quenching)
- B2O3-Nd2O3 experimental data
- FeO-B2O3 experimental data
- Fe2O3-Nd2O3 experimental data
- Solid compound thermodynamic properties
- Pure component Gibbs energy data
- Python packages numpy, scipy, matplotlib: https://pypi.tuna.tsinghua.edu.cn/simple

## Workflow steps

### Step 1: Optimize binary liquid solution parameters
- Role: scored
- Action: Implement the Modified Quasichemical Model (MQM) for the liquid phase of the four binary systems: FeO-Nd2O3, B2O3-Nd2O3, FeO-B2O3, and Fe2O3-Nd2O3. Using the provided experimental phase equilibrium data and solid compound thermodynamic properties, formulate an objective function (e.g., least-squares deviation between calculated and experimental liquidus/eutectic temperatures) and perform a non-linear optimization to determine the pair-exchange energy parameters (Δg) that best reproduce the experimental data. Output the optimized parameters as a JSON file.
- Output file: `/app/outputs/optimized_liquid_parameters.json`
- Format: json
- Contract: Top-level JSON object with keys 'FeO-Nd2O3', 'B2O3-Nd2O3', 'FeO-B2O3', 'Fe2O3-Nd2O3'. Each value is an object containing numeric fields for the temperature-independent and temperature-dependent terms of the MQM pair-exchange energy (e.g., 'delta_g0', 'delta_g1', ...).
- Scoring: scored by hidden verifier

### Step 2: Compute FeO-Nd2O3 phase diagram
- Role: scored (load-bearing)
- Action: Using the optimized liquid parameters from the previous step and the provided solid compound thermodynamic properties, compute the iron-saturated FeO-Nd2O3 phase diagram. Solve the thermodynamic equilibrium conditions to determine the stable phase assemblage across the composition range from pure FeO to pure Nd2O3 at multiple temperatures. Output a CSV file with points sampling the liquidus and solidus curves.
- Output file: `/app/outputs/feo_nd2o3_phase_diagram.csv`
- Format: csv
- Contract: Columns: Temperature_K (float, temperature in Kelvin), Composition_mol_pct_FeO (float, FeO composition in mol %), Stable_Phase (string, one of 'liquid', 'FeO', 'NdFeO3', 'Nd2O3').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_liquid_parameters.json`
- `/app/outputs/feo_nd2o3_phase_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_liquid_parameters.json
- path: `/app/outputs/optimized_liquid_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized liquid pair-exchange energy parameters for the four binary oxide systems. The FeO-Nd2O3 delta_g0 value is a key target of the reproduction.
- schema:
  - `type`: object
  - `required`: `FeO-Nd2O3`, `B2O3-Nd2O3`, `FeO-B2O3`, `Fe2O3-Nd2O3`
  - `properties`:
    - `FeO-Nd2O3`:
      - `type`: object
      - `description`: MQM liquid parameters for FeO-Nd2O3
    - `B2O3-Nd2O3`:
      - `type`: object
      - `description`: MQM liquid parameters for B2O3-Nd2O3
    - `FeO-B2O3`:
      - `type`: object
      - `description`: MQM liquid parameters for FeO-B2O3
    - `Fe2O3-Nd2O3`:
      - `type`: object
      - `description`: MQM liquid parameters for Fe2O3-Nd2O3

### feo_nd2o3_phase_diagram.csv
- path: `/app/outputs/feo_nd2o3_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed phase diagram of the iron-saturated FeO-Nd2O3 system. The hidden checker will recompute the eutectic and melting temperatures from these phase boundary points.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Composition_mol_pct_FeO`, `Stable_Phase`
  - `units`:
    - `Temperature_K`: K
    - `Composition_mol_pct_FeO`: mol %

Notes: The checker will extract key quantities from the output files to evaluate agreement with the paper-reported experimental data. The phase diagram must correctly reflect the FeO+NdFeO3→L and Nd2O3+NdFeO3→L eutectics and the melting point of NdFeO3 as measured by DTA.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_liquid_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "FeO-Nd2O3",
          "B2O3-Nd2O3",
          "FeO-B2O3",
          "Fe2O3-Nd2O3"
        ],
        "properties": {
          "FeO-Nd2O3": {
            "type": "object",
            "description": "MQM liquid parameters for FeO-Nd2O3"
          },
          "B2O3-Nd2O3": {
            "type": "object",
            "description": "MQM liquid parameters for B2O3-Nd2O3"
          },
          "FeO-B2O3": {
            "type": "object",
            "description": "MQM liquid parameters for FeO-B2O3"
          },
          "Fe2O3-Nd2O3": {
            "type": "object",
            "description": "MQM liquid parameters for Fe2O3-Nd2O3"
          }
        }
      },
      "description": "Optimized liquid pair-exchange energy parameters for the four binary oxide systems. The FeO-Nd2O3 delta_g0 value is a key target of the reproduction."
    },
    {
      "file": "feo_nd2o3_phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Composition_mol_pct_FeO",
          "Stable_Phase"
        ],
        "units": {
          "Temperature_K": "K",
          "Composition_mol_pct_FeO": "mol %"
        }
      },
      "description": "Computed phase diagram of the iron-saturated FeO-Nd2O3 system. The hidden checker will recompute the eutectic and melting temperatures from these phase boundary points."
    }
  ],
  "notes": "The checker will extract key quantities from the output files to evaluate agreement with the paper-reported experimental data. The phase diagram must correctly reflect the FeO+NdFeO3→L and Nd2O3+NdFeO3→L eutectics and the melting point of NdFeO3 as measured by DTA."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact. For the phase diagram CSV, the verifier may recompute the invariant temperatures from the extracted phase boundaries and compare them to expected values with appropriate tolerances, and may also verify the correct topology (e.g., that certain phase assemblages appear in the expected compositional regions). For the liquid parameters JSON, the verifier will check that key coefficients fall within physically acceptable ranges and, optionally, verify internal consistency with the computed phase diagram. Each stage’s score is weighted and combined into a final reward between 0 and 1. Simply reporting a number similar to a published value is not sufficient; the artifacts must pass structural and recomputation-based checks that confirm the underlying model was correctly implemented and optimized.
