# Radiation Defect Accumulation Modeling in Silicon Detectors

## Problem background
Silicon detectors used in associated particle imaging (API) suffer performance degradation from radiation-induced defects. Predicting defect accumulation and the resulting leakage current under alpha particle irradiation is crucial for assessing detector lifetime. This task reproduces a multiscale computational model that simulates the formation and evolution of radiation defects in silicon detectors irradiated by 3.5 MeV alpha particles. The model computes primary defect yields, tracks defect concentrations over time via stochastic cluster dynamics, and calculates the detector leakage current at several fluences.

## Approach
The multiscale approach combines three stages. (1) Primary defect production: the number of surviving primary defects (vacancies, interstitials, divacancies, diinterstitials) per alpha particle is estimated using analytical survival coefficients from Huhtinen (2002) applied to a given SRIM vacancy count. (2) Secondary defect evolution: a stochastic cluster dynamics simulation (using SPPARKS or an equivalent solver) tracks the time‑ and fluence‑dependent concentrations of defect‑impurity complexes. The simulation includes a reaction network with specified capture radii and initial concentrations of phosphorus, carbon, and oxygen impurities, assuming uniform irradiation within the Bragg peak. (3) Leakage current: the concentration of the electrically active V₂O defect is used to compute the detector leakage current via the carrier emission model. The results are compared across three alpha fluence levels.

## Reproduction target
Your task is to compute and report the following quantities:

(i) The mean numbers of primary defects per alpha particle: V, I, V₂, I₂, using the Huhtinen method and the provided SRIM vacancy count.

(ii) The saturation fluences and maximum concentrations of the VO, V₂O, and V₃O defects as determined from the cluster dynamics simulation.

(iii) The detector leakage current (in μA) at alpha fluences of 0, 1×10¹², and 1×10¹⁴ cm⁻², normalized to 1 cm², using the simulated V₂O concentration and the given emissivity.

Store these results in the specified JSON output files. The verifier will compare your computed values to reference values with appropriate tolerances.

## Assets

- SRIM software: http://www.srim.org
- SPPARKS stochastic kinetic Monte Carlo code: http://spparks.sandia.gov
- Defect reaction list and parameters from Huhtinen (2002): 10.1016/S0168-9002(02)00853-4
- Python environment with numpy: numpy

## Workflow steps

### Step 1: Compute primary defect numbers
- Role: scored
- Action: Using the given SRIM vacancy count per alpha particle (170 vacancies) and the survival coefficients for low-energy cascades from Huhtinen (2002) (the same coefficients as for 10 MeV protons), calculate the mean numbers of primary defects that survive after the displacement cascade: vacancies (V), interstitials (I), divacancies (V2), and diinterstitials (I2) per alpha particle.
- Output file: `/app/outputs/primary_defects_table.json`
- Format: json
- Contract: JSON object with keys 'V', 'I', 'V2', 'I2' mapping to floating-point numbers (defects per alpha particle).
- Scoring: scored by hidden verifier

### Step 2: Run stochastic cluster dynamics simulation
- Role: process
- Action: Set up and execute a stochastic cluster dynamics simulation using SPPARKS (or an equivalent solver) with a reaction network for defect-impurity interactions in silicon. Include the reaction list and parameters from Huhtinen (2002) and the defect-impurity complex add-on. Use initial impurity concentrations: phosphorus 1e12 cm⁻³, carbon 1e15 cm⁻³, oxygen 5e15 cm⁻³. Use alpha flux 1.1e5 cm⁻² s⁻¹ and primary defect generation rates from step1. Assume a uniform defect distribution within a 2 μm thick Bragg peak region. Run until defect concentrations saturate (fluence ≥ 1e14 cm⁻²). Output the full time/fluence evolution of all defect species concentrations as a CSV file.
- Evidence: `/app/outputs/concentration_evolution.csv`

### Step 3: Extract defect saturation concentrations
- Role: scored (load-bearing)
- Action: From the concentration evolution produced in step2, determine the saturation fluences (the approximate fluence at which concentrations stop changing significantly) for VO, V2O, and V3O, and extract the maximum (saturation) concentrations of V2O and V3O. Write these values to the output file.
- Output file: `/app/outputs/defect_saturation.json`
- Format: json
- Contract: JSON object with keys 'VO_saturation_fluence', 'V2O_saturation_fluence', 'V3O_saturation_fluence' (each a string representing fluence in cm⁻²), and 'V2O_max', 'V3O_max' (floating-point numbers, concentrations in cm⁻³).
- Scoring: scored by hidden verifier

### Step 4: Calculate leakage current
- Role: scored (load-bearing)
- Action: Using the V2O concentration from the simulation at the alpha fluences of 0, 1e12, and 1e14 cm⁻², compute the detector leakage current. Use the formula I = q * η * [V2O] * V, with q = 1.602e-19 C, η = 480 s⁻¹ (emissivity of V2O at 300 K), and V = 2e-4 cm³ (active volume of the Bragg peak region for a 1 cm² detector area). For fluence 0, use the background generation current of 0.010 μA. Neglect contributions from other defects. Report each current in μA.
- Output file: `/app/outputs/leakage_current.json`
- Format: json
- Contract: JSON object with keys '0', '1e12', '1e14' (as strings), each mapping to a floating-point leakage current in μA.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/primary_defects_table.json`
- `/app/outputs/defect_saturation.json`
- `/app/outputs/leakage_current.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### primary_defects_table.json
- path: `/app/outputs/primary_defects_table.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Primary defect counts per alpha particle using the Huhtinen method.
- schema:
  - `type`: object
  - `required`:
    - `V`: float
    - `I`: float
    - `V2`: float
    - `I2`: float
  - `units`: defects per alpha particle

### defect_saturation.json
- path: `/app/outputs/defect_saturation.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Saturation fluences and maximum concentrations of VO, V2O, V3O.
- schema:
  - `type`: object
  - `required`:
    - `VO_saturation_fluence`: string
    - `V2O_saturation_fluence`: string
    - `V3O_saturation_fluence`: string
    - `V2O_max`: float
    - `V3O_max`: float
  - `units`: fluence: cm⁻², concentration: cm⁻³

### leakage_current.json
- path: `/app/outputs/leakage_current.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Leakage current at three alpha fluences computed from V2O concentration.
- schema:
  - `type`: object
  - `required`:
    - `0`: float
    - `1e12`: float
    - `1e14`: float
  - `units`: μA

Notes: All scored outputs are compared to hidden reference values with appropriate tolerances. The primary defect coefficients from Huhtinen (2002) are the same as for 10 MeV protons; SRIM vacancy count is 170 per alpha. The simulation evidence file (concentration_evolution.csv) is not scored but documents that the cluster dynamics step was executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "primary_defects_table.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "V": "float",
          "I": "float",
          "V2": "float",
          "I2": "float"
        },
        "units": "defects per alpha particle"
      },
      "description": "Primary defect counts per alpha particle using the Huhtinen method."
    },
    {
      "file": "defect_saturation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "VO_saturation_fluence": "string",
          "V2O_saturation_fluence": "string",
          "V3O_saturation_fluence": "string",
          "V2O_max": "float",
          "V3O_max": "float"
        },
        "units": "fluence: cm⁻², concentration: cm⁻³"
      },
      "description": "Saturation fluences and maximum concentrations of VO, V2O, V3O."
    },
    {
      "file": "leakage_current.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "0": "float",
          "1e12": "float",
          "1e14": "float"
        },
        "units": "μA"
      },
      "description": "Leakage current at three alpha fluences computed from V2O concentration."
    }
  ],
  "notes": "All scored outputs are compared to hidden reference values with appropriate tolerances. The primary defect coefficients from Huhtinen (2002) are the same as for 10 MeV protons; SRIM vacancy count is 170 per alpha. The simulation evidence file (concentration_evolution.csv) is not scored but documents that the cluster dynamics step was executed."
}
```

## How you are scored
Each scored artifact (primary_defects_table.json, defect_saturation.json, leakage_current.json) is checked independently by a hidden verifier. For each file, the verifier compares your reported numbers to hidden reference values using tolerances that account for legitimate implementation and discretization differences. The overall reward is a weighted combination of the scores from these three artifacts. Simply reporting a set of numbers is not sufficient; the artifacts must be produced by the described workflow steps.
