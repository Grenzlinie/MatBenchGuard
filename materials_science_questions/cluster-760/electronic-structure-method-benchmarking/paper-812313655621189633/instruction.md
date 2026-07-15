# Electrostatic model for homolytic bond dissociation energy substituent effects in bicyclooctane systems

## Problem background
Substituent effects on chemical reactivity and stability are central to physical organic chemistry. While the Hammett relationship has been extensively applied to closed-shell molecules, its extension to radical systems is far less understood. In particular, the role of pure inductive/field effects on radical stabilities remains an open question. This study addresses that gap by systematically investigating how remote substituents influence homolytic bond dissociation energies (BDEs) in a rigid, non-conjugated scaffold: 4‑substituted bicyclo[2.2.2]octanyl systems. By using a scaffold that fully eliminates conjugation and steric interactions, the work isolates the inductive/field contribution. The outcome is a set of quantitative substituent effect descriptors (Hammett ρ values) for bond dissociations involving a diverse set of bonds ($\mathrm{Z\!-\!Y}$, with $\mathrm{Z=CH_2, NH, O, SiH_2, PH, S}$ and $\mathrm{Y=H, F, Li}$), as well as a physically motivated electrostatic model that predicts those ρ values from the charge distribution of the reacting moieties. The central task is to recompute these ρ values and to evaluate the predictive power of the electrostatic model by comparing predicted values to the computed ones.

## Approach
The reproduction follows a computational protocol that combines density functional theory (DFT) and high‑level composite quantum chemistry methods. The key steps are:

1. **Energy calculations**: All species involved – substituted bicyclooctane molecules and their corresponding radicals, as well as smaller model compounds – are built, and their geometries are optimized at the B3LYP/6‑31+G(d) level. Enthalpies are obtained from single‑point B3LYP/6‑311++G(2df,p) calculations with thermal corrections.

2. **Calibration of absolute BDEs**: Systematic errors in DFT BDEs are corrected by referencing high‑accuracy bond dissociation energies (obtained from a composite method such as G3B3 or an open‑source focal‑point approach) for the simpler trimethyl analogs $\mathrm{Me_3C\!-\!Z\!-\!Y}$. The DFT BDEs for the bicyclooctane parent systems are then calibrated using a simple additive scheme.

3. **Substituent effect quantification**: For every combination of substituent X, bridgehead atom Z, and leaving group Y, the relative BDE with respect to the parent (X=H) is computed. These ΔBDE values are correlated against the literature substituent field constants F to extract Hammett reaction constants ρ for each bond type.

4. **Partitioning into molecule and radical effects**: Isodesmic reactions defined in the original work separate the total substituent effect into a molecule effect (ME) and a radical effect (RE). Both are correlated with the F constants, yielding ρ_ME and ρ_RE for each Z–Y and Z• case.

5. **Electrostatic descriptor Φ**: For each Z–Y and Z• moiety, a hydrogen‑capped fragment is built using the geometry from the optimized bicyclo system. A single‑point DFT calculation provides CHelpG atomic charges. From these charges, the electrostatic descriptor Φ is calculated as the Coulomb interaction energy per unit charge with a model dipole placed at the substituent position.

6. **Predictive model**: All ρ_ME and ρ_RE values are regressed against their Φ values to obtain a unified linear relationship. This relationship is then used to predict the BDE ρ values: $\rho_{\text{pred}}(\mathrm{BDE}) = -\text{slope} \times (\Phi_{\mathrm{Z-Y}} - \Phi_{\mathrm{Z}^\bullet})$. The agreement between predicted and originally computed ρ values is summarized by the correlation coefficient $r^2$.

## Reproduction target
The objective is to execute the full pipeline described in the workflow steps and produce a single scored artifact containing all final quantitative results.

Specifically, the following quantities must be computed and written to the output JSON:

- **Computed Hammett ρ values** for each of the 18 $\mathrm{Z\!-\!Y}$ bond dissociations ($\mathrm{Z=CH_2, NH, O, SiH_2, PH, S}$; $\mathrm{Y=H, F, Li}$). These are obtained from linear regressions of ΔBDE (relative to X=H) against the substituent field constants $F$ ($\mathrm{F(H)=0.00, F(Me)=0.01, F(NH_2)=0.08, F(SH)=0.30, F(OH)=0.33, F(F)=0.45, F(CN)=0.51, F(NO_2)=0.65}$).

- **Predicted ρ values** for each of those same 18 bond types, derived from the electrostatic model: $\rho_{\text{pred}} = - \text{slope} \times (\Phi_{\mathrm{Z-Y}} - \Phi_{\mathrm{Z}^\bullet})$, where the slope comes from the unified fit of $\rho_{\mathrm{ME}}$ and $\rho_{\mathrm{RE}}$ against $\Phi$.

- **Model parameters** from the unified linear regression of all molecule‑effect and radical‑effect $\rho$ values versus their electrostatic descriptor $\Phi$: the slope (in kJ mol⁻¹ per Φ unit), intercept (kJ mol⁻¹), and correlation coefficient $r$ of the fit.

- **Overall prediction quality**: the squared correlation coefficient $r^2$ between the predicted $\rho_{\mathrm{pred}}$ and the originally computed $\rho$ values.

All numbers must be reported in the same JSON structure as specified in the output contract, with units of kJ mol⁻¹ for all ρ values and the model slope/intercept.

## Assets

- Quantum chemistry package capable of DFT calculations (e.g., Psi4, PySCF): https://psicode.org/
- Substituent inductive/field F constants

## Workflow steps

### Step 1: DFT geometry optimization and single-point energy calculations
- Role: process
- Action: Build molecular models for all species involved: 4-X-bicyclo[2.2.2]octanyl-Z-Y (X = H, CH3, F, OH, NH2, SH, CN, NO2; Z = CH2, NH, O, SiH2, PH, S; Y = H, F, Li), Me3C-Z-Y reference molecules, X-bicyclooctane, bicyclooctane, bicyclooctanyl-Z-Y parent molecules, and X-bicyclooctanyl-Z• radicals. Perform geometry optimizations and frequency calculations at B3LYP/6-31+G(d) level, then single-point energy calculations at B3LYP/6-311++G(2df,p) level. Collect total energies, zero-point energies, and thermal corrections to obtain enthalpies at 298 K.
- Evidence: `/app/outputs/step_01_energies.csv`

### Step 2: Reference high‑level BDEs for calibration trimethyl analogs
- Role: process
- Action: Compute high-accuracy bond dissociation energies for all Me3C-Z-Y systems (Z=CH2, NH, O, SiH2, PH, S; Y=H, F, Li) using a suitable composite quantum chemistry method (e.g., G3B3 or, as an open-source alternative, a focal-point approach such as DLPNO‑CCSD(T)/CBS). These will serve as the absolute reference for calibrating the DFT BDEs.
- Evidence: `/app/outputs/step_02_ref_bde.csv`

### Step 3: Calibrate absolute BDEs for parent bicyclo[2.2.2]octanyl systems
- Role: process
- Action: Using the B3LYP enthalpies from step_01 and the reference BDEs from step_02, compute B3LYP BDEs for Me3C-Z-Y and bicyclo[2.2.2]octanyl-Z-Y. Apply the calibration equation BDE_calc = BDE_ref + (BDE_B3LYP_bicyclo - BDE_B3LYP_Me3C) to obtain recommended absolute Z-Y BDEs for the parent (X=H) bicyclo systems.
- Evidence: `/app/outputs/step_03_parent_bde.csv`

### Step 4: Substituent ΔBDE and Hammett ρ for Z-Y BDEs
- Role: process
- Action: For each X-substituted bicyclooctanyl-Z-Y system, compute ΔBDE relative to X=H using the B3LYP BDEs. Perform linear regression of ΔBDE against the substituent inductive/field F constants for each Z–Y combination (18 pairs total). Record the resulting Hammett reaction constants ρ_BDE, their correlation coefficients, and the underlying ΔBDE values.
- Evidence: `/app/outputs/step_04_rho_bde.csv`

### Step 5: Molecule and radical effect partitioning (ME/RE) and their ρ values
- Role: process
- Action: Construct the isodesmic reactions that separate the total substituent effect into molecule effect (ME) and radical effect (RE). Using the B3LYP enthalpies of the relevant species, compute ME and RE for every substituent. Then regress ME and RE against the F constants to obtain ρ_ME and ρ_RE for each Z-Y and Z• case.
- Evidence: `/app/outputs/step_05_me_re_rho.csv`

### Step 6: Electrostatic descriptor Φ computation
- Role: process
- Action: For each Z-Y bond and the corresponding Z• radical, build an H‑capped moiety (H‑Z‑Y or H‑Z•) with the geometry taken from the optimized bicyclo system. Perform a single‑point B3LYP/6-311++G(2df,p) calculation to obtain CHelpG atomic charges. Compute the electrostatic descriptor Φ using the Coulomb interaction formula with a dipole of length 1.10 Å placed at the substituent position. The dipole is composed of point charges +Q and –Q; Φ represents the interaction energy per unit charge. Save the resulting Φ values.
- Evidence: `/app/outputs/step_06_phi.csv`

### Step 7: Aggregate all computed and predicted results (scored artifact)
- Role: scored (load-bearing)
- Action: Collect the computed ρ values for Z-Y BDEs from step_04, the ρ_ME and ρ_RE values and their corresponding Φ values from steps_05 and 06. Perform a linear regression of all ρ_ME and ρ_RE values against Φ to obtain the unified model parameters (slope, intercept, and correlation coefficient r). Use the derived slope to predict ρ(BDE) for each Z-Y bond as ρ_pred = -slope × (Φ_Z-Y − Φ_Z•). Compute the correlation coefficient r² between the predicted ρ_pred and the originally computed ρ (from step_04). Write all results into the output JSON file.
- Output file: `/app/outputs/step_07_results.json`
- Format: json
- Contract: JSON object with fields: 'overall_r_squared_pred_vs_computed' (float), 'rho_vs_phi_fit_slope' (float, kJ/mol per Φ unit), 'rho_vs_phi_fit_intercept' (float, kJ/mol), 'rho_vs_phi_fit_r' (float), 'z_y_rho' (array of objects, each with keys: 'z' (string, e.g. 'CH2'), 'y' (string, e.g. 'H'), 'computed_rho' (float, kJ/mol), 'predicted_rho' (float, kJ/mol)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_07_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_07_results.json
- path: `/app/outputs/step_07_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated reproduction results: computed ρ for each Z-Y bond, predicted ρ from the electrostatic model, the unified ρ‑vs‑Φ linear fit parameters (slope, intercept, correlation r), and the overall prediction r² between predicted and computed ρ values. The checker will compare these reported numbers against the paper’s gold values, applying the tolerances and directionality rules specified in the hidden grading specification.
- schema:
  - `type`: object
  - `required`:
    - `overall_r_squared_pred_vs_computed`: float
    - `rho_vs_phi_fit_slope`: float
    - `rho_vs_phi_fit_intercept`: float
    - `rho_vs_phi_fit_r`: float
    - `z_y_rho`: array
  - `items`:
    - `z_y_rho element`: object with keys: z (string), y (string), computed_rho (float, kJ/mol), predicted_rho (float, kJ/mol)

Notes: All numeric arrays and objects follow the declared schema. The computed and predicted ρ values are in units of kJ/mol. The model slope relates ρ (kJ/mol) to Φ, and the fit parameters are derived from the pooled ME/RE data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_07_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "overall_r_squared_pred_vs_computed": "float",
          "rho_vs_phi_fit_slope": "float",
          "rho_vs_phi_fit_intercept": "float",
          "rho_vs_phi_fit_r": "float",
          "z_y_rho": "array"
        },
        "items": {
          "z_y_rho element": "object with keys: z (string), y (string), computed_rho (float, kJ/mol), predicted_rho (float, kJ/mol)"
        }
      },
      "description": "Aggregated reproduction results: computed ρ for each Z-Y bond, predicted ρ from the electrostatic model, the unified ρ‑vs‑Φ linear fit parameters (slope, intercept, correlation r), and the overall prediction r² between predicted and computed ρ values. The checker will compare these reported numbers against the paper’s gold values, applying the tolerances and directionality rules specified in the hidden grading specification."
    }
  ],
  "notes": "All numeric arrays and objects follow the declared schema. The computed and predicted ρ values are in units of kJ/mol. The model slope relates ρ (kJ/mol) to Φ, and the fit parameters are derived from the pooled ME/RE data."
}
```

## How you are scored
A hidden verifier automatically reads your submitted `/app/outputs/step_07_results.json` and compares its contents against a set of hidden reference values. The verifier scores each reported quantity independently:

- **Computed ρ values** and **predicted ρ values** are compared to the corresponding reference values with appropriate tolerances; better‑than‑reference values are accepted as correct.
- **Model slope, intercept, and correlation $r$** are similarly compared to reference targets, with tolerances that account for the expected spread from different quantum‑chemistry implementations and numerical choices.
- **Overall $r^2$** between predicted and computed ρ values is checked against a threshold derived from the original work.

The individual scores are combined with a weighted average (the heaviest weight goes to the computed and predicted ρ values, moderate weight to the overall $r^2$, and lighter weight to the model parameters) to produce a final reward between 0 and 1. Reporting the paper’s published numbers without actually performing the computations will not satisfy the verifier’s tolerances and will receive a low or zero reward. The verifier does **not** require perfect agreement with any particular code version or functional; it allows the range expected from a careful independent implementation.
