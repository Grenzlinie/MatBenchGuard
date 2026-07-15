# NEMD simulations of thermal conductivity in DNTT organic semiconductor

## Problem background
The thermal transport properties of the high-mobility organic semiconductor DNTT (dinaphtho[2,3-b:2',3'-f]thieno[3,2-b]thiophene) are critical for the thermal management and reliability of organic electronic devices, yet remain poorly characterized. Polycrystalline thin films of DNTT contain grain boundaries and defects that strongly influence phonon transport. Understanding the anisotropic bulk thermal conductivity of perfect single crystals, the thermal boundary resistance (TBR) across representative crystal interfaces, and the impact of molecular vacancies on thermal conductivity is essential for predicting device performance and guiding materials design. These quantities have not been systematically established for DNTT, and their determination through non-equilibrium molecular dynamics (NEMD) provides a quantitative foundation for thermal engineering of organic electronics.

## Approach
All simulations use the LAMMPS package with the General AMBER Force Field (GAFF) to model intra- and intermolecular interactions in DNTT. The monoclinic unit cell is taken from the published crystal structure, and the heat transport directions are along the orthogonalized principal axes designated a*, b*, and c*. For the perfect-crystal studies, periodic simulation boxes are constructed with varying lengths along each transport direction. Non-equilibrium MD is performed by adding kinetic energy to a central heat source and removing the same amount at heat sinks at the ends, creating a steady-state temperature gradient and constant heat flux. Thermal conductivity is obtained from Fourier's law (k = -J/∇T) by fitting the linear region of the temperature profile. The size-dependent conductivities (k(L)) are then used to extrapolate the bulk thermal conductivity via a 1/k versus 1/L linear regression based on Matthiessen's rule. For the interface studies, bi-crystal simulation boxes are built with free boundary conditions; temperature drop ΔT at the interface is extracted from the temperature profile and the TBR is computed as R_K = ΔT / heat flux. For the vacancy study, a fraction of molecules is randomly removed from perfect crystals, and NEMD is run to obtain the reduced thermal conductivities, which are compared to the perfect-crystal values to compute the percentage reduction. All simulations are carried out at 300 K.

## Reproduction target
Produce the following four quantitative artifacts by running the described NEMD workflow:

1. A CSV file containing size-dependent thermal conductivities (k) for at least three different crystal lengths along each of the a*, b*, and c* directions, obtained from steady-state temperature profiles.
2. A JSON file with the extrapolated bulk thermal conductivities for each direction, derived from the size-dependent data by fitting 1/k vs 1/L.
3. A JSON file with the thermal boundary resistance for the a*-b*, a*-c*, and b*-c* interfaces. For each interface, report the simulated lengths, the TBR per length, and the mean TBR with standard deviation.
4. A JSON file with the thermal conductivity values for perfect crystals and for systems with a 6% vacancy concentration along each direction, along with the corresponding reduction percentage.

The target is to compute these quantities without referencing any hidden reference values; the method and conditions described here define the required computations.

## Assets

- LAMMPS: https://lammps.sandia.gov
- AmberTools / GAFF force field: http://ambermd.org
- DNTT crystal structure: 10.1021/ja068214e

## Workflow steps

### Step 1: Build perfect DNTT crystal simulation systems
- Role: process
- Action: Construct LAMMPS simulation boxes for perfect DNTT crystals along a*, b*, c* at multiple lengths using the GAFF force field and the published crystal structure.
- Evidence: none

### Step 2: Compute size-dependent thermal conductivity
- Role: scored
- Action: Run NEMD simulations at 300 K for each direction and length. From steady-state temperature profiles and imposed heat flux, compute thermal conductivity via Fourier's law and record the values with standard deviations.
- Output file: `/app/outputs/size_dependent_k.csv`
- Format: csv
- Contract: CSV with columns: direction (string: a*, b*, c*), length_nm (float), k_W_per_mK (float), k_std_W_per_mK (float). One row per simulation length; include at least three lengths per direction as specified in the paper.
- Scoring: scored by hidden verifier

### Step 3: Extrapolate bulk thermal conductivity
- Role: scored
- Action: Using the size-dependent k data, perform a linear regression of 1/k vs 1/L (Matthiessen's rule) to obtain the bulk thermal conductivity (k_bulk) for each direction. Report the extrapolated values.
- Output file: `/app/outputs/bulk_k.json`
- Format: json
- Contract: JSON object with keys "a*", "b*", "c*" mapping to float values (k_bulk in W/m-K).
- Scoring: scored by hidden verifier

### Step 4: Build interface simulation boxes
- Role: process
- Action: Construct simulation systems with two crystal orientations to represent a*-b*, a*-c*, b*-c* interfaces at various lengths as specified.
- Evidence: none

### Step 5: Calculate thermal boundary resistance
- Role: scored (load-bearing)
- Action: Run NEMD with free boundaries and heat source/sink at 300 K for each interface configuration and length. Extract temperature drop ΔT and heat flux q for each length. Compute TBR R_K = ΔT/q, then report the mean TBR and standard deviation averaged over the lengths for each interface.
- Output file: `/app/outputs/tbr_results.json`
- Format: json
- Contract: JSON object with keys "a*-b*", "a*-c*", "b*-c*". Each key maps to an object containing: "lengths" (list of simulated lengths in nm), "TBR_per_length" (list of R_K values in m^2·K/W), "mean_TBR" (float), "std_TBR" (float).
- Scoring: scored by hidden verifier

### Step 6: Generate vacancy configurations
- Role: process
- Action: Randomly remove molecules from perfect crystal boxes to create samples with vacancy concentration of 6%.
- Evidence: none

### Step 7: Determine thermal conductivity reduction from vacancies
- Role: scored
- Action: Run NEMD at 300 K for perfect crystal and 6% vacancy systems along a*, b*, c* directions. Compute thermal conductivity from temperature profiles. Report the perfect-crystal k, the 6%-vacancy k, and the percentage reduction for each direction.
- Output file: `/app/outputs/vacancy_effect.json`
- Format: json
- Contract: JSON object with keys "a*", "b*", "c*". Each key maps to an object with fields: "perfect_k" (W/m-K), "vacancy_k_6pct" (W/m-K), "reduction_percent" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/size_dependent_k.csv`
- `/app/outputs/bulk_k.json`
- `/app/outputs/tbr_results.json`
- `/app/outputs/vacancy_effect.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### size_dependent_k.csv
- path: `/app/outputs/size_dependent_k.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Raw thermal conductivity vs. crystal length data for each direction from NEMD simulations.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `length_nm`, `k_W_per_mK`
  - `optional_columns`: `k_std_W_per_mK`
  - `units`:
    - `direction`: string (a*, b*, c*)
    - `length_nm`: nanometre
    - `k_W_per_mK`: W/m·K
    - `k_std_W_per_mK`: W/m·K

### bulk_k.json
- path: `/app/outputs/bulk_k.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extrapolated bulk thermal conductivities for the three crystallographic directions.
- schema:
  - `type`: object
  - `required`:
    - `a*`: number (W/m·K)
    - `b*`: number (W/m·K)
    - `c*`: number (W/m·K)
  - `items`: 
  - `required_columns`:
  - `units`:
    - `a*`: W/m·K
    - `b*`: W/m·K
    - `c*`: W/m·K

### tbr_results.json
- path: `/app/outputs/tbr_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Thermal boundary resistance for the three representative interfaces, including per-length data and averaged values.
- schema:
  - `type`: object
  - `required`:
    - `a*-b*`: object
    - `a*-c*`: object
    - `b*-c*`: object
  - `items`:
    - `lengths`: list of numbers (nm)
    - `TBR_per_length`: list of numbers (m^2·K/W)
    - `mean_TBR`: number (m^2·K/W)
    - `std_TBR`: number (m^2·K/W)
  - `required_columns`:
  - `units`:
    - `mean_TBR`: m^2·K/W
    - `std_TBR`: m^2·K/W
    - `lengths`: nm
    - `TBR_per_length`: m^2·K/W

### vacancy_effect.json
- path: `/app/outputs/vacancy_effect.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Thermal conductivity reduction due to 6% molecular vacancies for each direction.
- schema:
  - `type`: object
  - `required`:
    - `a*`: object
    - `b*`: object
    - `c*`: object
  - `items`:
    - `perfect_k`: number (W/m·K)
    - `vacancy_k_6pct`: number (W/m·K)
    - `reduction_percent`: number (percent)
  - `required_columns`:
  - `units`:
    - `perfect_k`: W/m·K
    - `vacancy_k_6pct`: W/m·K
    - `reduction_percent`: percent

Notes: The checker will recompute bulk thermal conductivity from size_dependent_k.csv where appropriate. Tolerances accommodate stochastic NEMD variation; exact values are compared to hidden reference quantities.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "size_dependent_k.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "length_nm",
          "k_W_per_mK"
        ],
        "optional_columns": [
          "k_std_W_per_mK"
        ],
        "units": {
          "direction": "string (a*, b*, c*)",
          "length_nm": "nanometre",
          "k_W_per_mK": "W/m·K",
          "k_std_W_per_mK": "W/m·K"
        }
      },
      "description": "Raw thermal conductivity vs. crystal length data for each direction from NEMD simulations."
    },
    {
      "file": "bulk_k.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a*": "number (W/m·K)",
          "b*": "number (W/m·K)",
          "c*": "number (W/m·K)"
        },
        "items": "",
        "required_columns": [],
        "units": {
          "a*": "W/m·K",
          "b*": "W/m·K",
          "c*": "W/m·K"
        }
      },
      "description": "Extrapolated bulk thermal conductivities for the three crystallographic directions."
    },
    {
      "file": "tbr_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a*-b*": "object",
          "a*-c*": "object",
          "b*-c*": "object"
        },
        "items": {
          "lengths": "list of numbers (nm)",
          "TBR_per_length": "list of numbers (m^2·K/W)",
          "mean_TBR": "number (m^2·K/W)",
          "std_TBR": "number (m^2·K/W)"
        },
        "required_columns": [],
        "units": {
          "mean_TBR": "m^2·K/W",
          "std_TBR": "m^2·K/W",
          "lengths": "nm",
          "TBR_per_length": "m^2·K/W"
        }
      },
      "description": "Thermal boundary resistance for the three representative interfaces, including per-length data and averaged values."
    },
    {
      "file": "vacancy_effect.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a*": "object",
          "b*": "object",
          "c*": "object"
        },
        "items": {
          "perfect_k": "number (W/m·K)",
          "vacancy_k_6pct": "number (W/m·K)",
          "reduction_percent": "number (percent)"
        },
        "required_columns": [],
        "units": {
          "perfect_k": "W/m·K",
          "vacancy_k_6pct": "W/m·K",
          "reduction_percent": "percent"
        }
      },
      "description": "Thermal conductivity reduction due to 6% molecular vacancies for each direction."
    }
  ],
  "notes": "The checker will recompute bulk thermal conductivity from size_dependent_k.csv where appropriate. Tolerances accommodate stochastic NEMD variation; exact values are compared to hidden reference quantities."
}
```

## How you are scored
A hidden verifier will independently inspect each of the four output files. For each artifact, the verifier compares your reported quantities to hidden reference values that are derived from the original study, using tolerances that account for stochastic variations inherent in molecular dynamics (e.g., different random seeds, implementation details). The final reward is a weighted combination of the scores from all scored artifacts. Simply reporting numbers that match the paper's published results is not sufficient; you must execute the full simulation pipeline and write the corresponding output files as specified in the workflow steps. The verifier may also recompute derived quantities from your raw data (e.g., refit the bulk thermal conductivity from your size-dependent k values) and check consistency. The tolerances are set such that a genuine re-implementation of the method under the stated simulation conditions will succeed, while substantially incorrect or fabricated results will not.
