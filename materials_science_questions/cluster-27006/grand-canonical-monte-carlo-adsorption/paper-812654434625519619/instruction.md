# Grand Canonical Monte Carlo Adsorption of Branched Alkanes in Silicalite

## Problem background
Zeolites are microporous catalysts whose shape selectivity depends on the adsorption and diffusion of molecules in their pores. Understanding how linear and branched alkanes adsorb and move in the channels of the zeolite silicalite is important for catalytic dewaxing and alkane isomerisation. Computer simulations can provide detailed molecular-level information about the energetics and siting of these hydrocarbons that is difficult to obtain experimentally.

## Approach
This task uses configurational-bias Monte Carlo (CBMC) simulations with a united-atom force field to study alkanes in silicalite. The silicalite framework is treated as rigid, and interactions are described by Lennard-Jones potentials and intramolecular bond, angle, and torsion terms. The workflow involves: (1) obtaining the silicalite crystal structure and setting up the force field; (2) computing heats of adsorption for a series of singly branched alkanes at 398 K; (3) computing the spatial distribution (fraction occupancy in straight channels, zig-zag channels, and intersections) for 2-methylbutane and n-pentane at 298 K; and (4) for 2-methylhexane at 398 K, computing free energy profiles along the straight and zig-zag channels, then deriving hopping rates via transition-state theory and anisotropic diffusion coefficients from lattice random-walk formulas. The agent must implement these CBMC simulations using an open-source code such as RASPA2.

## Reproduction target
The goal is to produce three output files from CBMC simulations:
- `heats_of_adsorption.csv`: heats of adsorption for singly branched alkanes (CH3)2CH(CH2)nCH3 with n=0–3 (total carbon numbers Nc=5–8) at T=398 K.
- `siting_distribution.json`: occupancy fractions in straight channels, zig‑zag channels, and intersections for 2-methylbutane and n‑pentane at T=298 K.
- `diffusion_results.json`: free energy profiles as a function of head-group position along the straight and zig‑zag channels, the associated hopping rates, and the anisotropic diffusion coefficients (Dxx, Dyy, Dzz, D) for 2-methylhexane at T=398 K.
The task is satisfied if these quantities are computed from the specified simulations using the given force field and zeolite structure, and written to the required file formats and schemas.

## Assets

- Silicalite MFI zeolite framework: https://www.iza-structure.org/databases/
- United-atom force field for alkanes (Wang et al.) and zeolite-alkane interactions (Kiselev et al.)
- CBMC simulation code (e.g., RASPA2): https://github.com/iraspa/RASPA2

## Workflow steps

### Step 1: System preparation
- Role: process
- Action: Obtain the silicalite MFI crystal structure from the IZA structure database and set up the united-atom force field parameters for alkanes from Wang et al. and zeolite-alkane interactions from Kiselev et al. as specified in the paper. Generate simulation input files for silicalite and alkane molecules at the required temperatures.
- Evidence: none

### Step 2: Heats of adsorption for branched alkanes
- Role: scored
- Action: Run configurational-bias Monte Carlo (CBMC) simulations for the adsorption of singly branched alkanes (CH3)2-CH-(CH2)n-CH3 with n=0,1,2,3 (total carbon numbers 5-8) in silicalite at T=398 K. Compute the heat of adsorption from the average potential energy. Write the results to heats_of_adsorption.csv.
- Output file: `/app/outputs/heats_of_adsorption.csv`
- Format: csv
- Contract: columns: Nc (integer), heat_of_adsorption_kJ_per_mol (float)
- Scoring: scored by hidden verifier

### Step 3: Siting distribution for 2-methylbutane and n-pentane
- Role: scored
- Action: Run CBMC simulations for 2-methylbutane and n-pentane in silicalite at T=298 K. Record the positions of the CH head group (for 2-methylbutane) and the middle CH2 segment (for n-pentane). Compute the fraction of time the designated pseudo-atom spends in straight channels, zig-zag channels, and intersections. Write the fractions to siting_distribution.json.
- Output file: `/app/outputs/siting_distribution.json`
- Format: json
- Contract: {"2-methylbutane": {"straight": float, "zigzag": float, "intersection": float}, "pentane": {"straight": float, "zigzag": float, "intersection": float}}
- Scoring: scored by hidden verifier

### Step 4: Diffusion barriers and coefficients for 2-methylhexane
- Role: scored (load-bearing)
- Action: For 2-methylhexane in silicalite at T=398 K, compute the free energy profile as a function of the head group position along the straight and zig-zag channels using CBMC with Rosenbluth weighting. From the free energy barriers, compute hopping rates via transition-state theory. Then compute the anisotropic diffusion coefficients using the lattice random-walk formulas. Write the free energy arrays, hopping rates, and diffusion coefficients to diffusion_results.json.
- Output file: `/app/outputs/diffusion_results.json`
- Format: json
- Contract: {"straight_channel": {"q": [float], "free_energy": [float]}, "zigzag_channel": {"q": [float], "free_energy": [float]}, "hopping_rates": {"str_1_to_2": float, "str_2_to_3": float, "str_3_to_1": float, "zz_1_to_2": float, "zz_2_to_3": float, "zz_3_to_4": float, "zz_4_to_1": float}, "diffusion_coefficients": {"Dxx": float, "Dyy": float, "Dzz": float, "D": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heats_of_adsorption.csv`
- `/app/outputs/siting_distribution.json`
- `/app/outputs/diffusion_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heats_of_adsorption.csv
- path: `/app/outputs/heats_of_adsorption.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Heats of adsorption for singly branched alkanes (Nc=5-8) in silicalite at 398 K.
- schema:
  - `type`: table
  - `required_columns`: `Nc`, `heat_of_adsorption_kJ_per_mol`
  - `units`:
    - `Nc`: integer
    - `heat_of_adsorption_kJ_per_mol`: kJ/mol

### siting_distribution.json
- path: `/app/outputs/siting_distribution.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Occupancy fractions in straight channels, zig-zag channels, and intersections for 2-methylbutane and pentane at 298 K.
- schema:
  - `type`: object
  - `required`: `2-methylbutane`, `pentane`
  - `properties`:
    - `2-methylbutane`:
      - `type`: object
      - `required`: `straight`, `zigzag`, `intersection`
      - `properties`:
        - `straight`: float
        - `zigzag`: float
        - `intersection`: float
    - `pentane`:
      - `type`: object
      - `required`: `straight`, `zigzag`, `intersection`
      - `properties`:
        - `straight`: float
        - `zigzag`: float
        - `intersection`: float

### diffusion_results.json
- path: `/app/outputs/diffusion_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Free energy profiles, hopping rates, and anisotropic diffusion coefficients for 2-methylhexane in silicalite at 398 K.
- schema:
  - `type`: object
  - `required`: `straight_channel`, `zigzag_channel`, `hopping_rates`, `diffusion_coefficients`
  - `properties`:
    - `straight_channel`:
      - `type`: object
      - `required`: `q`, `free_energy`
      - `properties`:
        - `q`: array of float
        - `free_energy`: array of float
    - `zigzag_channel`:
      - `type`: object
      - `required`: `q`, `free_energy`
      - `properties`:
        - `q`: array of float
        - `free_energy`: array of float
    - `hopping_rates`:
      - `type`: object
      - `required`: `str_1_to_2`, `str_2_to_3`, `str_3_to_1`, `zz_1_to_2`, `zz_2_to_3`, `zz_3_to_4`, `zz_4_to_1`
      - `properties`:
        - `str_1_to_2`: float (events/s)
        - `str_2_to_3`: float
        - `str_3_to_1`: float
        - `zz_1_to_2`: float
        - `zz_2_to_3`: float
        - `zz_3_to_4`: float
        - `zz_4_to_1`: float
    - `diffusion_coefficients`:
      - `type`: object
      - `required`: `Dxx`, `Dyy`, `Dzz`, `D`
      - `properties`:
        - `Dxx`: float (cm^2/s)
        - `Dyy`: float
        - `Dzz`: float
        - `D`: float

Notes: All three outputs are compared to hidden gold values extracted from the paper with appropriate tolerances (see grading_spec, not public).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heats_of_adsorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Nc",
          "heat_of_adsorption_kJ_per_mol"
        ],
        "units": {
          "Nc": "integer",
          "heat_of_adsorption_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Heats of adsorption for singly branched alkanes (Nc=5-8) in silicalite at 398 K."
    },
    {
      "file": "siting_distribution.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "2-methylbutane",
          "pentane"
        ],
        "properties": {
          "2-methylbutane": {
            "type": "object",
            "required": [
              "straight",
              "zigzag",
              "intersection"
            ],
            "properties": {
              "straight": "float",
              "zigzag": "float",
              "intersection": "float"
            }
          },
          "pentane": {
            "type": "object",
            "required": [
              "straight",
              "zigzag",
              "intersection"
            ],
            "properties": {
              "straight": "float",
              "zigzag": "float",
              "intersection": "float"
            }
          }
        }
      },
      "description": "Occupancy fractions in straight channels, zig-zag channels, and intersections for 2-methylbutane and pentane at 298 K."
    },
    {
      "file": "diffusion_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "straight_channel",
          "zigzag_channel",
          "hopping_rates",
          "diffusion_coefficients"
        ],
        "properties": {
          "straight_channel": {
            "type": "object",
            "required": [
              "q",
              "free_energy"
            ],
            "properties": {
              "q": "array of float",
              "free_energy": "array of float"
            }
          },
          "zigzag_channel": {
            "type": "object",
            "required": [
              "q",
              "free_energy"
            ],
            "properties": {
              "q": "array of float",
              "free_energy": "array of float"
            }
          },
          "hopping_rates": {
            "type": "object",
            "required": [
              "str_1_to_2",
              "str_2_to_3",
              "str_3_to_1",
              "zz_1_to_2",
              "zz_2_to_3",
              "zz_3_to_4",
              "zz_4_to_1"
            ],
            "properties": {
              "str_1_to_2": "float (events/s)",
              "str_2_to_3": "float",
              "str_3_to_1": "float",
              "zz_1_to_2": "float",
              "zz_2_to_3": "float",
              "zz_3_to_4": "float",
              "zz_4_to_1": "float"
            }
          },
          "diffusion_coefficients": {
            "type": "object",
            "required": [
              "Dxx",
              "Dyy",
              "Dzz",
              "D"
            ],
            "properties": {
              "Dxx": "float (cm^2/s)",
              "Dyy": "float",
              "Dzz": "float",
              "D": "float"
            }
          }
        }
      },
      "description": "Free energy profiles, hopping rates, and anisotropic diffusion coefficients for 2-methylhexane in silicalite at 398 K."
    }
  ],
  "notes": "All three outputs are compared to hidden gold values extracted from the paper with appropriate tolerances (see grading_spec, not public)."
}
```

## How you are scored
A hidden verifier will read each scored artifact, check that it conforms to the required schema, and compare selected quantities against reference values derived from the published literature. Each artifact contributes a weighted portion of the total reward. Deviations within a reasonable margin for the simulation method are acceptable, but the numbers must be obtained by running the actual simulations, not by guessing or external look‑up. Evidence that you faithfully executed the required workflow will be more valuable than matching any specific pre‑known number.
