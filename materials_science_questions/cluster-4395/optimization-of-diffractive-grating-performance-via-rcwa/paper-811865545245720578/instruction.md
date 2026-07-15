# Evaluation of Homogeneous-Layer Models for High-Spatial-Frequency Grating Diffraction

## Problem background
Dielectric surface-relief gratings with periods small enough to cut off all nonzero diffracted orders can behave like uniaxial slabs, enabling applications as antireflection surfaces and wave plates. For a rectangular-groove grating, the equivalent ordinary and extraordinary refractive indices of the homogenized layer depend on the filling factor, the material indices, and the wavelength-to-period ratio. Several approximations exist: first-order indices (simple averaging, no wavelength dependence), second-order indices (Rytov's approximation), and higher-order indices (exact solutions of transcendental equations). This task investigates the accuracy of these homogeneous-layer models for predicting the zero-order diffraction properties of a silicon grating in air, under both nonconical and conical incidence, by comparing their predictions against rigorous coupled-wave analysis (RCWA). You will compute the zero-order backward diffraction efficiencies and relative phases and determine the conditions under which each model provides a trustworthy description of the grating's electromagnetic response.

## Approach
The grating region is replaced by a homogeneous uniaxial slab whose ordinary index n_O and extraordinary index n_E are computed from one of three formulas. First-order indices are simple root-mean-square (TE) and inverse parallel-plate (TM) averages. Second-order indices are given by Rytov's series expansion retaining terms to second order in Λ/λ0. Higher-order indices are obtained by solving the full transcendental equations numerically. With these indices, the reflection and transmission of the slab are calculated using standard anisotropic layer matrix methods. As the rigorous reference, implement RCWA with sufficient Fourier harmonics to accurately represent the rectangular-groove profile. For nonconical incidence (φ=0°, θ1=30°), the TE and TM polarizations are decoupled; compute the zero-order backward diffraction efficiency DE0 using each index model and also directly with RCWA. For conical incidence (φ=45°, θ1=45°), the homogeneous layer model and RCWA both produce coupled TE and TM reflected components; compute the TE-component DE0, TM-component DE0, total DE0, and their relative phase as a function of λ0/Λ. The detailed parameter sets and output schemas are given in the workflow steps.

## Reproduction target
Produce two scored CSV files according to the specifications in the workflow steps. First, for the nonconical incidence case with the specified grating parameters, compute the zero-order backward diffraction efficiency DE0 for TE and TM polarizations using the first-order, second-order, and higher-order index models, and optionally RCWA. Report all values in `/app/outputs/step_01_nonconical_results.csv`. Second, for the antireflection grating design under TE-polarized conical incidence, sweep the wavelength-to-period ratio through the listed values (4,5,6,7,8,9,10) and for each ratio compute the TE-component, TM-component, total DE0, and relative phase using both the higher-order homogeneous-layer model and RCWA. Write the full set of results to `/app/outputs/step_02_conical_results.csv`. The contents of both files must be self-consistent and physically reasonable; the conical-diffraction model outputs should agree closely with the corresponding RCWA outputs where all nonzero orders are cut off.

## Assets

- gratingrcwa (Python RCWA library): https://pypi.org/project/gratingrcwa/
- S4 (Stanford Stratified Structure Solver): https://github.com/victorpoughon/s4
- NumPy/SciPy: numpy, scipy

## Workflow steps

### Step 1: Compute nonconical diffraction efficiencies
- Role: scored
- Action: Implement rigorous coupled-wave analysis (RCWA) and the homogeneous-layer indices (first-order, second-order, higher-order) for rectangular-groove gratings in air (n1=1) on a silicon substrate (n3=3.5) at λ0/Λ=5. For TE polarization, design parameters (F, d/λ0) are: first-order (0.2000, 0.1443), second-order (0.1704, 0.1443), higher-order (0.1679, 0.1443). For TM polarization: first-order (0.8155, 0.1268), second-order (0.7178, 0.1270), higher-order (0.6633, 0.1272). The angle of incidence is θ1=30°, φ=0°. Compute zero-order backward diffraction efficiency DE0 for TE and TM polarizations using each index model; if you also compute RCWA results, use the same design parameters (RCWA rows are optional but encouraged). Report all computed values in a CSV.
- Output file: `/app/outputs/step_01_nonconical_results.csv`
- Format: csv
- Contract: Columns: polarization (str), model_type (str), de0 (float, percent). Example: TE,first_order,1.1958
- Scoring: scored by hidden verifier

### Step 2: Compute conical diffraction and model-RCWA comparison
- Role: scored (load-bearing)
- Action: For the grating designed to be antireflecting at normal incidence (TE, F=0.222, d/λ0=0.4010) and under TE-polarized conical incidence at φ=45°, θ1=45°, compute using RCWA and the higher-order homogeneous-layer model (HLM) the TE-component DE0, TM-component DE0, total DE0, and relative phase (degrees) as functions of λ0/Λ for λ0/Λ = 4,5,6,7,8,9,10. Output a CSV with columns for both HLM and RCWA results.
- Output file: `/app/outputs/step_02_conical_results.csv`
- Format: csv
- Contract: Columns: lambda_over_period (float), de0_TE_HLM (float), de0_TM_HLM (float), de0_total_HLM (float), phase_HLM (float, degrees), de0_TE_RCWA (float), de0_TM_RCWA (float), de0_total_RCWA (float), phase_RCWA (float, degrees). Rows for λ0/Λ = 4,5,6,7,8,9,10.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_nonconical_results.csv`
- `/app/outputs/step_02_conical_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_nonconical_results.csv
- path: `/app/outputs/step_01_nonconical_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nonconical zero-order backward diffraction efficiency DE0 for TE and TM polarizations computed with first-order, second-order, and higher-order indices. Checked against hidden reference values extracted from Table 1 of the paper within a tolerance.
- schema:
  - `required_columns`: `polarization`, `model_type`, `de0`
  - `description`: CSV with columns polarization (TE or TM), model_type (first_order, second_order, higher_order, RCWA), de0 (float, percent).

### step_02_conical_results.csv
- path: `/app/outputs/step_02_conical_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Conical diffraction results: self-consistency between HLM and RCWA for TE-component, TM-component, total DE0, and relative phase at multiple λ/Λ values. The checker recomputes the maximum absolute difference between HLM and RCWA values across reported points and scores against a tolerance (<0.02 absolute for DE0, <10° for phase).
- schema:
  - `required_columns`: `lambda_over_period`, `de0_TE_HLM`, `de0_TM_HLM`, `de0_total_HLM`, `phase_HLM`, `de0_TE_RCWA`, `de0_TM_RCWA`, `de0_total_RCWA`, `phase_RCWA`
  - `description`: CSV with columns for λ/Λ and the HLM and RCWA results for TE component, TM component, total DE0, and relative phase (degrees).

Notes: The agent must implement the homogeneous-layer model (first-order, second-order, higher-order index formulas) and rigorous coupled-wave analysis (RCWA) with at least 19 Fourier orders. The RCWA may be implemented from scratch or by using an open-source library. The output contract defines only the scored artifacts; no gold tolerances are revealed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_nonconical_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "polarization",
          "model_type",
          "de0"
        ],
        "description": "CSV with columns polarization (TE or TM), model_type (first_order, second_order, higher_order, RCWA), de0 (float, percent)."
      },
      "description": "Nonconical zero-order backward diffraction efficiency DE0 for TE and TM polarizations computed with first-order, second-order, and higher-order indices. Checked against hidden reference values extracted from Table 1 of the paper within a tolerance."
    },
    {
      "file": "step_02_conical_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "lambda_over_period",
          "de0_TE_HLM",
          "de0_TM_HLM",
          "de0_total_HLM",
          "phase_HLM",
          "de0_TE_RCWA",
          "de0_TM_RCWA",
          "de0_total_RCWA",
          "phase_RCWA"
        ],
        "description": "CSV with columns for λ/Λ and the HLM and RCWA results for TE component, TM component, total DE0, and relative phase (degrees)."
      },
      "description": "Conical diffraction results: self-consistency between HLM and RCWA for TE-component, TM-component, total DE0, and relative phase at multiple λ/Λ values. The checker recomputes the maximum absolute difference between HLM and RCWA values across reported points and scores against a tolerance (<0.02 absolute for DE0, <10° for phase)."
    }
  ],
  "notes": "The agent must implement the homogeneous-layer model (first-order, second-order, higher-order index formulas) and rigorous coupled-wave analysis (RCWA) with at least 19 Fourier orders. The RCWA may be implemented from scratch or by using an open-source library. The output contract defines only the scored artifacts; no gold tolerances are revealed."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier. The verifier examines each required output file independently. For the nonconical results, your reported DE0 values are compared against hidden reference values using a tolerance-based pass/fail criterion. For the conical results, the verifier computes the differences between your homogeneous-layer model values and your RCWA values and scores based on how closely they match, particularly in the wavelength-to-period range where higher diffracted orders are suppressed. Each step contributes a fraction to the final reward: step 1 (nonconical) carries 60% weight, and step 2 (conical) carries 40% weight. The overall reward is a continuous score from 0 to 1, with a score of 1 indicating an excellent reproduction. Simply reporting the paper's numbers without actually performing the required computations will not pass the verifier.
