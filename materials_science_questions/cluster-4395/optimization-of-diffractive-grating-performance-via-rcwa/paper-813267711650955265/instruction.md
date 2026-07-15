# Thin-Profile Solar Concentrator Design Optimization by Rigorous Coupled-Wave Analysis

## Problem background
A thin‑profile solar concentrator is designed to capture a broad solar spectrum (400–900 nm) and direct it onto a photovoltaic cell with high angular tolerance, enabling a compact, stationary panel. The design couples light into a wedge prism using two blazed diffraction gratings — a transmission grating on the top surface for shorter wavelengths and a reflection grating on the bottom surface for longer wavelengths — and guides the light via total internal reflection to a smaller exit face. The design challenge is to optimize six geometric parameters to maximize the collection efficiency, concentration ratio, and angular acceptance of the structure.

## Approach
The concentrator’s performance is evaluated by computing the collection efficiency (fraction of incident power that reaches the exit face) across the full spectrum and over a range of incident angles. This requires two computational components:
- Rigorous Coupled‑Wave Analysis (RCWA) to compute the diffraction efficiencies of the blazed gratings for both TE and TM polarizations at each wavelength.
- Geometric ray tracing that propagates each incident ray through the prism, accounting for grating diffraction orders, Fresnel reflections at all surfaces, and the total‑internal‑reflection (TIR) condition. Rays are traced until they exit the prism or drop below a negligible power threshold.

The optimization proceeds sequentially, as detailed in the workflow steps below: first fix the wedge refractive index and estimate feasible grating periods from TIR constraints; then sweep the wedge apex angle, the reflection grating period, the transmission grating period, and finally the blaze angles, each time maximizing the polarization‑averaged collection efficiency averaged over 400–900 nm. With the optimal design fixed, a dense wavelength scan produces a spectral collection‑efficiency curve, and a two‑dimensional incident‑angle scan provides the angular‑tolerance map. The final output is a JSON file containing the six optimal parameters (wedge apex angle, refractive index, grating periods and blaze angles) and the derived headline metrics: the broadband collection efficiency, concentration ratio (CE × surface ratio, where surface ratio A_I/A_II is computed from the final wedge apex angle based on the wedge prism geometry), and the full widths at 90% and 50% of the maximum collection efficiency along the two incident‑angle axes.

## Reproduction target
Optimize the six design parameters (wedge apex angle θ_w, wedge refractive index n_w, transmission grating period Λ_t and blaze angle α_t, reflection grating period Λ_r and blaze angle α_r) using RCWA and ray tracing. From the optimized design, compute the broadband (400–900 nm) average collection efficiency (polarization‑averaged), the concentration ratio (CE × surface ratio, where the surface ratio A_I/A_II is derived from the final wedge apex angle), and the angular‑tolerance widths at 90% and 50% of the maximum collection efficiency along the two incident‑angle axes (θ_inc in the x‑z plane and φ_inc in the y‑z plane). Report all six optimal parameters and these performance metrics in a JSON file following the schema specified in the output contract.

## Assets

- Python 3 with numpy and scipy: numpy
- Open-source RCWA solver

## Workflow steps

### Step 1: Simulation configuration
- Role: process
- Action: Fix all constant simulation parameters: wedge material refractive index n_w=1.48, uniform solar spectrum 400–900 nm, illuminated area A_I = 10 cm², polarization averaging (TE and TM), Fresnel reflections on all prism surfaces, and neglect material absorption.
- Evidence: `/app/outputs/simulation_config.txt`

### Step 2: Estimate feasible grating period ranges using TIR conditions
- Role: process
- Action: Apply the total-internal-reflection (TIR) conditions (paper equations 3–4) to compute wavelength bands that satisfy TIR for the transmission grating and reflection grating. Derive initial feasible ranges for the grating periods.
- Evidence: `/app/outputs/tir_range_estimation.txt`

### Step 3: Wedge apex angle optimization
- Role: process
- Action: Using fixed initial grating parameters (transmission blaze angle = 62°, transmission period = 610 nm; reflection period = 1140 nm, reflection blaze angles 10°,13°,15°,17°), sweep the wedge apex angle θ_w. For each θ_w, compute the polarization‑averaged collection efficiency across the 400‑900 nm spectrum via RCWA and ray tracing. Identify the θ_w that maximizes average CE.
- Evidence: `/app/outputs/wedge_angle_optimization.csv`

### Step 4: Reflection grating period optimization
- Role: process
- Action: With optimal θ_w from step_03 fixed, and transmission grating parameters unchanged, sweep the reflection grating period Λ_r (≈1000–1400 nm) for each blaze angle α_r (10°,13°,15°,17°). Compute average CE; find the Λ_r that maximizes CE.
- Evidence: `/app/outputs/reflection_period_optimization.csv`

### Step 5: Transmission grating period optimization
- Role: process
- Action: With optimal θ_w and optimal Λ_r fixed, sweep the transmission grating period Λ_t (≈500–700 nm) for each blaze angle α_t (58°,62°,66°,70°). Compute average CE; find the optimal Λ_t.
- Evidence: `/app/outputs/transmission_period_optimization.csv`

### Step 6: Grating blaze angles optimization
- Role: process
- Action: With optimized periods (Λ_t = 610 nm, Λ_r = 1140 nm) and θ_w = 8.1°, jointly sweep the blaze angles α_t and α_r. Compute the polarization‑averaged CE across the spectrum. Identify the pair (α_t, α_r) that yields the highest CE. Record TE and TM components separately.
- Evidence: `/app/outputs/blaze_angle_optimization.csv`

### Step 7: Spectral collection efficiency computation
- Role: process
- Action: For the fully optimized design, compute the collection efficiency at a dense sampling of wavelengths from 400 to 900 nm, separately for TE and TM polarizations. Average them to obtain CE(λ).
- Evidence: `/app/outputs/spectral_CE.csv`

### Step 8: Angular tolerance scan
- Role: process
- Action: For the optimized design, scan the incident angles θ_inc (x‑z plane) and φ_inc (y‑z plane) over a sufficient range. For each combination, compute the collection efficiency (TE and TM separately, then average).
- Evidence: `/app/outputs/angular_tolerance_scan.csv`

### Step 9: Final optimal design results
- Role: scored (load-bearing)
- Action: From the optimization results and the spectral and angular data, assemble the headline outputs: the six optimal design parameters, the maximum average collection efficiency (computed from the spectral CE scan), the concentration ratio (CE × surface ratio, where the surface ratio A_I/A_II is derived from the optimized wedge apex angle using the geometric relationship of the prism), and the angular tolerance widths at 90% and 50% of the maximum CE (extracted from the angular tolerance scan). Write all values into optimal_design_results.json.
- Output file: `/app/outputs/optimal_design_results.json`
- Format: json
- Contract: Keys: wedge_apex_angle_deg (float), wedge_refractive_index (float), transmission_grating_period_nm (float), transmission_grating_blaze_angle_deg (float), reflection_grating_period_nm (float), reflection_grating_blaze_angle_deg (float), collection_efficiency (float), concentration_ratio (float), angular_tolerance_phi_deg_90percent (float), angular_tolerance_theta_deg_90percent (float), angular_tolerance_phi_deg_50percent (float), angular_tolerance_theta_deg_50percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimal_design_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimal_design_results.json
- path: `/app/outputs/optimal_design_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The final optimal design parameters and headline performance metrics (collection efficiency, concentration ratio, angular tolerances). Compared against hidden paper‑reported values with appropriate tolerances and threshold‑or‑better logic.
- schema:
  - `type`: object
  - `required`:
    - `wedge_apex_angle_deg`: float
    - `wedge_refractive_index`: float
    - `transmission_grating_period_nm`: float
    - `transmission_grating_blaze_angle_deg`: float
    - `reflection_grating_period_nm`: float
    - `reflection_grating_blaze_angle_deg`: float
    - `collection_efficiency`: float
    - `concentration_ratio`: float
    - `angular_tolerance_phi_deg_90percent`: float
    - `angular_tolerance_theta_deg_90percent`: float
    - `angular_tolerance_phi_deg_50percent`: float
    - `angular_tolerance_theta_deg_50percent`: float

Notes: The checker will also read the intermediate evidence files (spectral_CE.csv and angular_tolerance_scan.csv) to recompute the average collection efficiency and angular tolerance widths, ensuring the reported aggregates are consistent with the raw simulation data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimal_design_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "wedge_apex_angle_deg": "float",
          "wedge_refractive_index": "float",
          "transmission_grating_period_nm": "float",
          "transmission_grating_blaze_angle_deg": "float",
          "reflection_grating_period_nm": "float",
          "reflection_grating_blaze_angle_deg": "float",
          "collection_efficiency": "float",
          "concentration_ratio": "float",
          "angular_tolerance_phi_deg_90percent": "float",
          "angular_tolerance_theta_deg_90percent": "float",
          "angular_tolerance_phi_deg_50percent": "float",
          "angular_tolerance_theta_deg_50percent": "float"
        }
      },
      "description": "The final optimal design parameters and headline performance metrics (collection efficiency, concentration ratio, angular tolerances). Compared against hidden paper‑reported values with appropriate tolerances and threshold‑or‑better logic."
    }
  ],
  "notes": "The checker will also read the intermediate evidence files (spectral_CE.csv and angular_tolerance_scan.csv) to recompute the average collection efficiency and angular tolerance widths, ensuring the reported aggregates are consistent with the raw simulation data."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects all intermediate evidence files (CSV tables from the optimization sweeps, spectral CE curve, angular‑tolerance map) and the final JSON. The verifier recomputes the average collection efficiency from the spectral‑CE data and extracts the angular‑tolerance widths from the angular‑tolerance map, then compares these recomputed values against hidden reference targets. The verifier also compares your reported optimal design parameters against hidden expected values within appropriate tolerances, and checks that the concentration ratio is consistent with the collection efficiency and the given area ratio. Each workflow stage’s artifact contributes to the overall score, with the final JSON carrying the largest weight. Simply reporting the paper’s numbers without genuine simulation will not be rewarded because the raw evidence files must be internally consistent with the final reported aggregates.
