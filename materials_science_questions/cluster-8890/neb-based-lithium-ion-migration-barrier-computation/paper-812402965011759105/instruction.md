# Structure and Vibrational Properties of Lithium Borate Glasses from Molecular Dynamics

## Problem background
Lithium borate glasses are ion-conducting materials whose ionic transport properties are intimately linked to their atomic-scale structure and dynamics. Understanding the glass network connectivity and the characteristic vibrational modes of boron–oxygen bonds is essential to explain the mechanisms of ionic conductivity. In this task, you will investigate the structure and vibrational properties of lithium borate glasses using classical molecular dynamics simulations.

## Approach
You will model three glass compositions (B2O3)_{1-x}(Li2O)_x with x=0, 0.1, 0.2 by molecular dynamics using the Born–Mayer–Huggins (BMH) pair potential, which accounts for repulsive overlap and Coulombic interactions. The glass is prepared by equilibrating the system at high temperature and then rapidly quenching to room temperature via velocity scaling. From the resulting atomic configurations, you extract structural properties: nearest-neighbour distances (B–O, O–O) from radial distribution functions, average coordination numbers for boron and oxygen, bond angles (BOB and OBO), and the fraction of four-coordinated boron (NBO4). Additionally, you analyse the vibrational dynamics by tracking the B–O nearest-neighbour distance over time at room temperature and computing its Fourier spectrum to identify the main B–O stretching frequency band. The goal is to produce a consistent set of structural parameters and vibrational peak positions across the three compositions.

## Reproduction target
Produce two output files as described in the workflow steps:
- structural_properties.json: for each of the three compositions, report the B–O nearest-neighbour distance, O–O nearest-neighbour distance, average boron coordination number, average oxygen coordination number, average BOB angle, average OBO angle, and the fraction of four-coordinated boron (NBO4).
- vibrational_peak.json: for each composition, report the frequency of the strongest vibrational peak in the B–O stretching region (800–1600 cm^{-1}).
All quantities must be derived from the MD simulations you run, not taken from external sources.

## Assets

- Molecular dynamics simulation software: any MD package supporting Born-Mayer-Huggins potential (e.g., LAMMPS, GROMACS)

## Workflow steps

### Step 1: MD Simulations
- Role: process
- Action: Run classical molecular dynamics simulations for three lithium borate glass compositions: (B2O3)_{1-x}(Li2O)_x with x=0, 0.1, 0.2. Initialize systems according to ion counts and box sizes given in the paper. Use the Born-Mayer-Huggins potential with parameters from the paper. Start at 6000 K for 1 ps, then quench to 300 K by velocity scaling. Save atomic trajectories or final configuration snapshots for subsequent analysis.
- Evidence: `/app/outputs/md_simulation.log`

### Step 2: Structural Properties Extraction
- Role: scored (load-bearing)
- Action: From the MD-generated structures, compute and report structural properties for each composition: B-O nearest-neighbor distance (first peak), O-O nearest-neighbor distance, boron average coordination number, oxygen average coordination number, average BOB angle, average OBO angle, and fraction of four-coordinated boron (NBO4).
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: array of objects with composition value restricted to exactly "x0", "x0.1", or "x0.2". Other keys: B_O_distance (float, Angstrom), O_O_distance (float, Angstrom), B_coordination (float), O_coordination (float), BOB_angle (float, degrees), OBO_angle (float, degrees), NBO4_fraction (float)
- Scoring: scored by hidden verifier

### Step 3: B-O Vibrational Frequency Analysis
- Role: scored
- Action: Extract the time series of B-O nearest-neighbor distances from the MD trajectories at 300 K, compute the Fourier spectrum of these distance oscillations for each composition, and identify the main vibrational peak frequency (frequency of the strongest peak in the range 800-1600 cm^{-1}). Report the peak frequency for each composition.
- Output file: `/app/outputs/vibrational_peak.json`
- Format: json
- Contract: array of objects with composition value restricted to exactly "x0", "x0.1", or "x0.2". Other key: peak_frequency (float, cm^{-1})
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.json`
- `/app/outputs/vibrational_peak.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Agent-reported structural properties for three glass compositions. Composition must be exactly 'x0', 'x0.1', or 'x0.2'. Hidden checker compares each value to paper-reported references with predefined tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `composition`:
        - `type`: string
        - `enum`: `x0`, `x0.1`, `x0.2`
      - `B_O_distance`:
        - `type`: number
      - `O_O_distance`:
        - `type`: number
      - `B_coordination`:
        - `type`: number
      - `O_coordination`:
        - `type`: number
      - `BOB_angle`:
        - `type`: number
      - `OBO_angle`:
        - `type`: number
      - `NBO4_fraction`:
        - `type`: number
    - `required`: `composition`, `B_O_distance`, `O_O_distance`, `B_coordination`, `O_coordination`, `BOB_angle`, `OBO_angle`, `NBO4_fraction`
    - `additionalProperties`: False
  - `units`:
    - `B_O_distance`: Angstrom
    - `O_O_distance`: Angstrom
    - `B_coordination`: unitless
    - `O_coordination`: unitless
    - `BOB_angle`: degrees
    - `OBO_angle`: degrees
    - `NBO4_fraction`: unitless

### vibrational_peak.json
- path: `/app/outputs/vibrational_peak.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Agent-reported B-O vibrational peak frequencies for each composition. Composition must be exactly 'x0', 'x0.1', or 'x0.2'. Hidden checker compares to paper-reported peak positions with a tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `composition`:
        - `type`: string
        - `enum`: `x0`, `x0.1`, `x0.2`
      - `peak_frequency`:
        - `type`: number
    - `required`: `composition`, `peak_frequency`
    - `additionalProperties`: False
  - `units`:
    - `peak_frequency`: cm^{-1}

Notes: All quantities are derived from MD simulations that are sensitive to implementation details. The hidden checker uses tolerances informed by expected method spread. The composition keys are mandated to match hidden gold table.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "composition": {
              "type": "string",
              "enum": [
                "x0",
                "x0.1",
                "x0.2"
              ]
            },
            "B_O_distance": {
              "type": "number"
            },
            "O_O_distance": {
              "type": "number"
            },
            "B_coordination": {
              "type": "number"
            },
            "O_coordination": {
              "type": "number"
            },
            "BOB_angle": {
              "type": "number"
            },
            "OBO_angle": {
              "type": "number"
            },
            "NBO4_fraction": {
              "type": "number"
            }
          },
          "required": [
            "composition",
            "B_O_distance",
            "O_O_distance",
            "B_coordination",
            "O_coordination",
            "BOB_angle",
            "OBO_angle",
            "NBO4_fraction"
          ],
          "additionalProperties": false
        },
        "units": {
          "B_O_distance": "Angstrom",
          "O_O_distance": "Angstrom",
          "B_coordination": "unitless",
          "O_coordination": "unitless",
          "BOB_angle": "degrees",
          "OBO_angle": "degrees",
          "NBO4_fraction": "unitless"
        }
      },
      "description": "Agent-reported structural properties for three glass compositions. Composition must be exactly 'x0', 'x0.1', or 'x0.2'. Hidden checker compares each value to paper-reported references with predefined tolerances."
    },
    {
      "file": "vibrational_peak.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "composition": {
              "type": "string",
              "enum": [
                "x0",
                "x0.1",
                "x0.2"
              ]
            },
            "peak_frequency": {
              "type": "number"
            }
          },
          "required": [
            "composition",
            "peak_frequency"
          ],
          "additionalProperties": false
        },
        "units": {
          "peak_frequency": "cm^{-1}"
        }
      },
      "description": "Agent-reported B-O vibrational peak frequencies for each composition. Composition must be exactly 'x0', 'x0.1', or 'x0.2'. Hidden checker compares to paper-reported peak positions with a tolerance."
    }
  ],
  "notes": "All quantities are derived from MD simulations that are sensitive to implementation details. The hidden checker uses tolerances informed by expected method spread. The composition keys are mandated to match hidden gold table."
}
```

## How you are scored
After you complete all steps, a hidden verifier will independently score each scored artifact (structural_properties.json and vibrational_peak.json) by comparing your reported values to independently determined reference values. Each artifact contributes a weighted share toward the final reward (a float between 0 and 1). The verifier does not depend on any external network access. Simply reporting values that match literature does not guarantee a high score; the verifier checks that the quantities are physically plausible and consistent with the simulation protocol you executed. The exact tolerances and scoring details are hidden.
