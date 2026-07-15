# Linear Model for Molecular Adsorption Binding Energy Prediction

## Problem background
Predicting the dissociative adsorption energy of molecules on metal surfaces is essential for catalyst design, corrosion inhibition, and coatings. A reliable predictive model that uses easily accessible descriptors would drastically reduce the computational cost of screening candidate molecules and substrates. This task addresses the construction of a linear model that estimates the binding energy from a small set of physically motivated descriptors computed from density functional theory (DFT) and standard reference data.

## Approach
The predictive model expresses the dissociative adsorption binding energy (BE) as a linear function of three descriptors:

- **Cohesive bulk energy** (CE_B) – a property of the metal substrate.
- **Work‑function / gap alignment** (WF − E_gap/2) – the mismatch between the substrate work function and the midpoint of the adsorbate molecule's HOMO–LUMO gap.
- **Molecule‑Bulk Energy** (MBE) – a cluster‑based estimate of the substrate–adsorbate interaction, pre‑computed from DFT for each molecule–substrate pair.

The coefficients of this linear relationship are fitted via ordinary least‑squares (OLS) regression on a training set of 80 adsorbate–substrate pairs. As a benchmark, the Sure Independence Screening and Sparsifying Operator (SISSO) algorithm is applied to an extended descriptor pool that includes additional tabulated metal and molecular properties (e.g., number of valence electrons, surface energy, ionization potential, atomic volume, electronegativity, molecular HOMO, LUMO, molar mass) to identify the best three‑descriptor linear model. The comparison reveals whether the physically chosen descriptors are close to the mathematically optimal ones.

## Reproduction target
1. Using the training dataset provided in the task's input files (80 data points with BE, CE_B, WF, E_gap, MBE), perform OLS linear regression to fit the coefficients of the model BE = a + b·CE_B + c·(WF − E_gap/2) + d·MBE. Report the fitted coefficients and the training‑set metrics: R², mean absolute error (MAE, in eV), and root‑mean‑square error (RMSE, in eV).

2. Assemble an extended descriptor matrix that augments the above descriptors with the following properties for each pair: number of valence electrons of the metal (N_ve), metal surface energy (γ_met), first ionisation potential of the metal (I₁), atomic volume of the metal (V_met), metal electronegativity (χ_met), molecular HOMO (HOMO_mol) and LUMO (LUMO_mol), and molar mass of the molecule (M_mol). Run the SISSO algorithm to discover the best linear model with exactly three descriptors. Record the chosen descriptors, their fitted coefficients (intercept and three slopes), and the training RMSE (in eV).

## Assets

- Training dataset (80 data points with descriptors and binding energies) - supplied in the task's input files.
- Materials Project database: https://materialsproject.org/
- Cohesive bulk energies from C. Kittel, Introduction to Solid State Physics: https://www.wiley.com/en-us/Introduction+to+Solid+State+Physics%2C+8th+Edition-p-9780471415268
- statsmodels Python library: statsmodels
- SISSO algorithm implementation: https://github.com/rouyang2017/SISSO
- Extended tabulated properties for metals and molecules
- Python 3 with numpy, scipy, pandas, scikit-learn: numpy scipy pandas scikit-learn

## Workflow steps

### Step 1: OLS regression of the linear adsorption model
- Role: scored
- Action: Load the training dataset (80 data points with BE, CE_B, WF, E_gap, MBE), perform ordinary least‑squares linear regression to fit the coefficients a, b, c, d of BE = a + b·CE_B + c·(WF − E_gap/2) + d·MBE. Compute the model’s R², MAE, and RMSE on the training set.
- Output file: `/app/outputs/step_01_regression_coefficients.json`
- Format: json
- Contract: JSON object with keys: a (float), b (float), c (float), d (float), R2 (float), MAE (float, unit: eV), RMSE (float, unit: eV).
- Scoring: scored by hidden verifier

### Step 2: SISSO benchmark and descriptor identification
- Role: scored
- Action: Assemble an extended descriptor matrix for the training set: in addition to CE_B, WF, E_gap, MBE, collect the following properties for each molecule‑substrate pair: number of valence electrons (N_ve), surface energy (γ_met), first ionisation potential (I₁), atomic volume (V_met), metal electronegativity (χ_met), molecular HOMO (HOMO_mol), LUMO (LUMO_mol), and molecular molar mass (M_mol). Run the SISSO algorithm to find the best linear model with three descriptors. Record the identified descriptors, the fitted coefficients (intercept and slopes), and the training RMSE.
- Output file: `/app/outputs/step_02_sisso_results.json`
- Format: json
- Contract: JSON object with keys: intercept (float), coeff_1 (float), coeff_2 (float), coeff_3 (float), descriptor_1 (string), descriptor_2 (string), descriptor_3 (string), RMSE (float, unit: eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_regression_coefficients.json`
- `/app/outputs/step_02_sisso_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_regression_coefficients.json
- path: `/app/outputs/step_01_regression_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Coefficients of the linear adsorption model (Eq. 3) and training set performance metrics.
- schema:
  - `type`: object
  - `required`:
    - `a`: float
    - `b`: float
    - `c`: float
    - `d`: float
    - `R2`: float
    - `MAE`: float
    - `RMSE`: float
  - `units`:
    - `MAE`: eV
    - `RMSE`: eV

### step_02_sisso_results.json
- path: `/app/outputs/step_02_sisso_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Best 3‑descriptor linear model found by SISSO, its coefficients and training RMSE.
- schema:
  - `type`: object
  - `required`:
    - `intercept`: float
    - `coeff_1`: float
    - `coeff_2`: float
    - `coeff_3`: float
    - `descriptor_1`: string
    - `descriptor_2`: string
    - `descriptor_3`: string
    - `RMSE`: float
  - `units`:
    - `RMSE`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_regression_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float",
          "b": "float",
          "c": "float",
          "d": "float",
          "R2": "float",
          "MAE": "float",
          "RMSE": "float"
        },
        "units": {
          "MAE": "eV",
          "RMSE": "eV"
        }
      },
      "description": "Coefficients of the linear adsorption model (Eq. 3) and training set performance metrics."
    },
    {
      "file": "step_02_sisso_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "intercept": "float",
          "coeff_1": "float",
          "coeff_2": "float",
          "coeff_3": "float",
          "descriptor_1": "string",
          "descriptor_2": "string",
          "descriptor_3": "string",
          "RMSE": "float"
        },
        "units": {
          "RMSE": "eV"
        }
      },
      "description": "Best 3‑descriptor linear model found by SISSO, its coefficients and training RMSE."
    }
  ],
  "notes": ""
}
```

## How you are scored
Each workflow step produces one scored artifact. A hidden verifier independently recomputes the OLS model metrics and the SISSO model RMSE from your submitted coefficients and the same training data it holds privately. The verifier also compares your coefficients against hidden reference values. Every scored artifact contributes a separate score; the final overall reward is the weighted sum of these step‑level scores. Submitting the expected numbers without genuinely running the required computations will not yield correct artifacts.
