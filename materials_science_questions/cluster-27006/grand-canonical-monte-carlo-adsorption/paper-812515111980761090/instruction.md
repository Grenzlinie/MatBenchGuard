# Adsorption Selectivity Prediction for Near-Azeotropic Mixtures using GCMC and IAST

## Problem background
Near-azeotropic mixtures, where components have very similar boiling points, are notoriously difficult to separate by conventional distillation. Adsorption-based gas separations offer an alternative, but predicting mixture adsorption in porous materials such as metal-organic frameworks (MOFs) is challenging due to the vast number of possible adsorbent–adsorbate combinations. Ideal adsorbed solution theory (IAST) is a popular mixing theory that can predict mixture adsorption from single-component isotherms, but its accuracy for near-azeotropic molecules in MOFs needs to be tested. Grand canonical Monte Carlo (GCMC) simulations can provide direct binary mixture adsorption data against which IAST can be compared. This task focuses on computing whether IAST can reproduce the binary mixture behavior for a set of near-azeotropic molecules in a selected MOF, using GCMC simulations as the ground truth.

## Approach
The approach consists of two streams: (1) direct GCMC simulations of binary adsorption for selected molecular pairs in a MOF, and (2) IAST predictions using single-component isotherms simulated under identical conditions. First, a set of 12 molecules with near-azeotropic boiling points and compatible with the TraPPE force field is selected. For a chosen MOF (QATHOK from the CoRE MOF 2019 database), force field parameters are assigned: UFF for the framework and TraPPE (united-atom or explicit-hydrogen as appropriate) for adsorbates. Single-component adsorption isotherms at 300 K are generated via GCMC in RASPA for pressures spanning the Henry’s law region up to high loadings. Then equimolar binary GCMC simulations are run for four specific molecular pairs at a total pressure defined as the average of the vapor pressures. Using pyIAST, the single-component isotherms are used to predict the adsorbed loadings and selectivity for each binary mixture. Finally, the relative error of each prediction with respect to the direct GCMC result is computed as the absolute difference divided by the simulated value.

## Reproduction target
Generate a CSV file named iast_vs_simulation_errors.csv under /app/outputs containing the relative errors between IAST predictions and direct GCMC simulations for the following four binary mixtures in MOF QATHOK at 300 K and total pressure P_total = 0.5×(P_vp_A + P_vp_B): (i) 3-butenal / tert-butanol, (ii) 3-butenal / 4-methyl-1-hexene, (iii) 4-methyl-1-hexene / 2,2-dimethylpentane, (iv) 4-methyl-1-hexene / 2,4-dimethylpentane. For each system, report the relative error in the loading of component A, the loading of component B, and the adsorption selectivity, defined as |prediction − simulation| / simulation. The hidden verifier will compare each reported relative error to reference values derived from the paper’s own simulation data for these exact systems.

## Assets

- RASPA 2.0: https://github.com/numat/RASPA2
- pyIAST: https://github.com/CorySimon/pyIAST
- CoRE MOF 2019 database: https://doi.org/10.1021/acs.jced.9b00835
- TraPPE force field parameters
- Universal Force Field (UFF): https://doi.org/10.1002/jcc.540110211

## Workflow steps

### Step 1: Prepare molecular models and MOF structure
- Role: process
- Action: Obtain the crystal structure of MOF QATHOK from the CoRE MOF 2019 database (CIF file). Assign UFF force field parameters and atomic point charges. Build flexible molecular models for the 12 molecules (3-butenal, butylamine, tert-butanol, 4-methyl-1-hexene, 4,4-dimethyl-1-pentene, 2,2-dimethylpentane, 2,4-dimethylpentane, 3,3-dimethylpentane, methylethylpropylamine, dimethylbutylamine, ethyl tert-butyl ether, diisopropyl ether) using the TraPPE force field (UA or EH as appropriate) with standard functional forms from the literature. Assign each molecule an integer ID according to this ordering: 1) 3-butenal, 2) butylamine, 3) tert-butanol, 4) 4-methyl-1-hexene, 5) 4,4-dimethyl-1-pentene, 6) 2,2-dimethylpentane, 7) 2,4-dimethylpentane, 8) 3,3-dimethylpentane, 9) methylethylpropylamine, 10) dimethylbutylamine, 11) ethyl tert-butyl ether, 12) diisopropyl ether.
- Evidence: `/app/outputs/preparation.log`

### Step 2: Simulate single-component adsorption isotherms
- Role: process
- Action: For each of the 12 molecules in MOF QATHOK, perform GCMC simulations with RASPA 2.0 at 300 K. Use pressures ranging from a low value (chosen to give loading < 1e-4 of the saturation loading) up to 50× the vapor pressure. Simulation parameters: 1e5 equilibration cycles, 1e6 production cycles, LJ cutoff 14 Å with tail correction, Ewald summation for Coulomb interactions. Save the equilibrium loading (molecules/unit cell) as a function of pressure.
- Evidence: `/app/outputs/single_component_isotherms.csv`

### Step 3: Simulate binary mixture adsorption
- Role: process
- Action: Run equimolar binary GCMC simulations for the four selected pairs (3-butenal/tert-butanol, 3-butenal/4-methyl-1-hexene, 4-methyl-1-hexene/2,2-dimethylpentane, 4-methyl-1-hexene/2,4-dimethylpentane) in QATHOK at 300 K and total pressure P_total = 0.5*(Pvp_A + Pvp_B). Use the same simulation settings as the single-component runs. Save the adsorbed loading of each component and the selectivity S_ads.
- Evidence: `/app/outputs/binary_mixture_results.csv`

### Step 4: Compute IAST predictions and relative errors
- Role: scored (load-bearing)
- Action: For each binary mixture system, use pyIAST to predict the adsorbed loadings and selectivity from the single-component isotherm data. Compute the relative error for each component's loading and for the selectivity as |prediction - simulation| / simulation. Export the results.
- Output file: `/app/outputs/iast_vs_simulation_errors.csv`
- Format: csv
- Contract: Columns: system_id (str, must be one of 'pair_1_3', 'pair_1_4', 'pair_4_6', 'pair_4_7'), component_A (str), component_B (str), MOF_ID (str), relative_error_loading_A (float), relative_error_loading_B (float), relative_error_selectivity (float). One row per binary system. The molecule IDs 1,3,4,6,7 correspond to 3-butenal, tert-butanol, 4-methyl-1-hexene, 2,2-dimethylpentane, and 2,4-dimethylpentane respectively.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/iast_vs_simulation_errors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### iast_vs_simulation_errors.csv
- path: `/app/outputs/iast_vs_simulation_errors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative errors between IAST predictions and direct GCMC simulations for the four test binary systems. The hidden checker compares each reported error to a gold reference derived from the paper's reported simulation data, using per-column tolerances.
- schema:
  - `type`: table
  - `required_columns`: `system_id`, `component_A`, `component_B`, `MOF_ID`, `relative_error_loading_A`, `relative_error_loading_B`, `relative_error_selectivity`
  - `columns`:
    - `system_id`:
      - `type`: string
      - `allowed`: `pair_1_3`, `pair_1_4`, `pair_4_6`, `pair_4_7`
      - `description`: Formed as 'pair_<ID_A>_<ID_B>' using the molecule IDs from Step 1. For the required mixtures: pair_1_3 (3-butenal/tert-butanol), pair_1_4 (3-butenal/4-methyl-1-hexene), pair_4_6 (4-methyl-1-hexene/2,2-dimethylpentane), pair_4_7 (4-methyl-1-hexene/2,4-dimethylpentane).
    - `component_A`:
      - `type`: string
    - `component_B`:
      - `type`: string
    - `MOF_ID`:
      - `type`: string
    - `relative_error_loading_A`:
      - `type`: number
      - `units`: dimensionless
    - `relative_error_loading_B`:
      - `type`: number
      - `units`: dimensionless
    - `relative_error_selectivity`:
      - `type`: number
      - `units`: dimensionless

Notes: Only the four specified binary pairs in MOF QATHOK are required. The hidden reference corresponds to the paper's reported relative errors for these exact systems. The agent must re-produce the full GCMC pipeline; pre-computed isotherm data is not provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "iast_vs_simulation_errors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system_id",
          "component_A",
          "component_B",
          "MOF_ID",
          "relative_error_loading_A",
          "relative_error_loading_B",
          "relative_error_selectivity"
        ],
        "columns": {
          "system_id": {
            "type": "string",
            "allowed": [
              "pair_1_3",
              "pair_1_4",
              "pair_4_6",
              "pair_4_7"
            ],
            "description": "Formed as 'pair_<ID_A>_<ID_B>' using the molecule IDs from Step 1. For the required mixtures: pair_1_3 (3-butenal/tert-butanol), pair_1_4 (3-butenal/4-methyl-1-hexene), pair_4_6 (4-methyl-1-hexene/2,2-dimethylpentane), pair_4_7 (4-methyl-1-hexene/2,4-dimethylpentane)."
          },
          "component_A": {
            "type": "string"
          },
          "component_B": {
            "type": "string"
          },
          "MOF_ID": {
            "type": "string"
          },
          "relative_error_loading_A": {
            "type": "number",
            "units": "dimensionless"
          },
          "relative_error_loading_B": {
            "type": "number",
            "units": "dimensionless"
          },
          "relative_error_selectivity": {
            "type": "number",
            "units": "dimensionless"
          }
        }
      },
      "description": "Relative errors between IAST predictions and direct GCMC simulations for the four test binary systems. The hidden checker compares each reported error to a gold reference derived from the paper's reported simulation data, using per-column tolerances."
    }
  ],
  "notes": "Only the four specified binary pairs in MOF QATHOK are required. The hidden reference corresponds to the paper's reported relative errors for these exact systems. The agent must re-produce the full GCMC pipeline; pre-computed isotherm data is not provided."
}
```

## How you are scored
A hidden verifier checks that the required output file iast_vs_simulation_errors.csv exists and conforms to the specified schema. It then compares each reported relative error (loading of component A, loading of component B, and selectivity) to the corresponding hidden reference value for that system. For each comparison, if the reported error falls within a pre-defined tolerance (which accounts for Monte Carlo noise), that entry is marked correct. The final reward is the fraction of correct entries out of the total number of comparisons (4 systems × 3 metrics = 12 entries). Full credit (1.0) is awarded only if all entries meet the tolerance; partial credit decreases linearly with the number of out-of-tolerance entries. The tolerances are not disclosed in advance, but they are set to be achievable by a faithful re-run of the GCMC pipeline.
