# Piezoelectric Bending Actuator Modeling for Tunable Gratings

## Problem background
Strain-tuning of periodic optical devices such as diffractive gratings can be achieved by integrating thin‑film piezoelectric actuators on a deformable double‑anchored membrane. This task focuses on the analytical modeling of such a system. The model treats the membrane as a piezoelectric bimorph, where an applied voltage across a lead zirconate titanate (PZT) layer induces an in‑plane displacement that uniformly stretches a superimposed grating, thereby altering its period and the angle of diffracted light. The key quantities of interest are the membrane displacement along the grating axis, the resulting change in grating period, the membrane strain, and the corresponding change in the first‑order diffraction angle. You will implement this model and compute these quantities for two specific device designs using the provided geometry, material constants, and voltages.

## Approach
The core of the model is an analytical piezoelectric bimorph formula for the in‑plane displacement δ_x of a double‑anchored multilayer membrane. The displacement is computed as
δ_x = (d31 * E_pzt * A_pzt * V) / (t_pzt * k_x),
where d31 is the piezoelectric coupling coefficient, E_pzt the Young’s modulus of PZT, A_pzt the cross‑sectional area of the PZT layer, V the applied voltage, t_pzt the PZT thickness, and k_x the effective axial stiffness of the composite beam. For an isotropic wide membrane, a correction is applied: replace E_i with E_i/(1‑ν_i²) and d31 with d31(1+ν_pzt), where ν_i are Poisson’s ratios. The effective axial stiffness is k_x = Σ (E_i,corrected * A_i) / L, with the sum running over all layers in the membrane stack and L the beam length along the grating axis.

Once the displacement is obtained, the membrane strain is ε = δ_x / L. The grating period change is Δd = ε * d0, where the nominal grating period d0 = 4 µm. The change in the first‑order diffraction angle (m = 1) for illumination with a HeNe laser at λ = 632.8 nm is given by Δθ ≈ (λ Δd) / d0² (small‑angle approximation).

Perform the calculation for the two device configurations below, using the following parameters:

- PZT layer: thickness 0.5 µm, Young’s modulus 90 GPa, Poisson’s ratio 0.30, piezoelectric coefficient d31 = −100 pC/N.
- Bottom electrode (Pt/Ti): thickness 0.22 µm, effective Young’s modulus 168 GPa, Poisson’s ratio 0.39.
- Top electrode (Pt/Ti): same as bottom electrode.
- SiO₂ diffusion barrier: thickness 0.30 µm, Young’s modulus 70 GPa, Poisson’s ratio 0.17.
- SiN hardmask: thickness 0.20 µm, Young’s modulus 250 GPa, Poisson’s ratio 0.27.
- All layers have the same width; the absolute width cancels out, so you may assume a unit width.
- Beam length L (actuator length) and applied voltage V:
    * Device 1: L = 450 µm, V = 9 V.
    * Device 2: L = 200 µm, V = 10 V.
- Nominal grating period: d0 = 4 µm.
- Incident laser wavelength: λ = 632.8 nm.
- Diffraction order: m = 1.

Compute the displacement, period change, strain, and angular change for each device and report them in the output CSV file.

## Reproduction target
Implement the analytical model described in the Approach section and compute, for each of the two device configurations (Device 1: L = 450 µm, 9 V; Device 2: L = 200 µm, 10 V), the following quantities: membrane displacement (in nm), grating period change (in nm), membrane strain (in percent), and first‑order diffracted angular change (in microradians). Write one row per device into a CSV file named model_predictions.csv placed at `/app/outputs/model_predictions.csv`. The CSV must have the columns:
device_id, voltage_V, membrane_displacement_nm, period_change_nm, strain_percent, angular_change_urad.

## Assets
No external datasets, pretrained models, or proprietary tools are required. All necessary device geometry and material constants are provided in the Approach section. You may implement the calculations using any programming language and standard mathematical libraries (e.g., NumPy, SciPy).

## Workflow steps

### Step 1: Compute bimorph model predictions
- Role: scored
- Action: Implement the double-anchored piezoelectric bimorph model with isotropic wide-membrane corrections. Compute membrane displacement (from the applied voltage, PZT coupling coefficient, layer materials and dimensions, and effective axial stiffness), then derive the grating period change (from membrane strain), membrane strain, and first-order diffracted angular change (using the small-angle grating equation). Perform the calculation for the two device designs reported in the paper: Device 1 (PZT length 450 μm, applied voltage 9 V) and Device 2 (PZT length 200 μm, applied voltage 10 V). Use the published material constants and the fitted piezoelectric coefficient d₃₁ = -100 pC/N. Save one row per device in the output CSV file.
- Output file: `/app/outputs/model_predictions.csv`
- Format: csv
- Contract: Columns: device_id (string), voltage_V (float), membrane_displacement_nm (float), period_change_nm (float), strain_percent (float), angular_change_urad (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_predictions.csv
- path: `/app/outputs/model_predictions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Analytical bimorph model predictions for the two grating devices. The checker will recompute period change, strain, and angular change from the agent's reported membrane displacement and compare them to hidden gold values derived from the paper's own model predictions.
- schema:
  - `type`: table
  - `required_columns`: `device_id`, `voltage_V`, `membrane_displacement_nm`, `period_change_nm`, `strain_percent`, `angular_change_urad`
  - `units`:
    - `voltage_V`: V
    - `membrane_displacement_nm`: nm
    - `period_change_nm`: nm
    - `strain_percent`: %
    - `angular_change_urad`: µrad

Notes: The predicted quantities are derived from the bimorph model using the device geometry and material constants published in the paper. The checker performs a T1 recompute: it extracts the membrane displacement from the CSV, recomputes the period change, strain, and angular change using the same analytical relations, and compares each recomputed quantity against hidden gold values with tolerances appropriate for a deterministic analytical computation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "device_id",
          "voltage_V",
          "membrane_displacement_nm",
          "period_change_nm",
          "strain_percent",
          "angular_change_urad"
        ],
        "units": {
          "voltage_V": "V",
          "membrane_displacement_nm": "nm",
          "period_change_nm": "nm",
          "strain_percent": "%",
          "angular_change_urad": "µrad"
        }
      },
      "description": "Analytical bimorph model predictions for the two grating devices. The checker will recompute period change, strain, and angular change from the agent's reported membrane displacement and compare them to hidden gold values derived from the paper's own model predictions."
    }
  ],
  "notes": "The predicted quantities are derived from the bimorph model using the device geometry and material constants published in the paper. The checker performs a T1 recompute: it extracts the membrane displacement from the CSV, recomputes the period change, strain, and angular change using the same analytical relations, and compares each recomputed quantity against hidden gold values with tolerances appropriate for a deterministic analytical computation."
}
```

## How you are scored
A hidden verifier will evaluate your submission after the task ends. It reads your output CSV, verifies the schema, then recomputes the period change, strain, and angular change from the membrane displacement you reported, using the same analytical relations. These recomputed values are compared against reference values derived from the paper’s model predictions. Your final score reflects the accuracy of your computed quantities; simply reporting numbers you obtained elsewhere will not match the hidden reference. This is the only scored artifact, so the entire reward weight rests on this CSV.
