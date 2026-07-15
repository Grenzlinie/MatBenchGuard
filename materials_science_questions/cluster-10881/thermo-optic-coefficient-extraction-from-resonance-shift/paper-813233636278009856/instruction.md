# Thermal Wavelength Shift Calculation for HgGa2S4 Optical Parametric Oscillator

## Problem background
HgGa2S4 (mercury thiogallate) is a defect chalcopyrite nonlinear optical crystal used in mid-infrared optical parametric oscillators (OPOs) pumped near 1 μm. Accurate prediction of phase-matched wavelengths under varying thermal conditions is essential for high-power OPO design. The crystal's refractive indices are described by Sellmeier equations, and their temperature dependence is given by thermo-optic coefficients dn/dT. During operation, residual absorption heats the crystal, causing a temperature rise that shifts the phase-matched signal wavelength. This task requires computing that thermally induced shift from the published material data for a specific measured temperature rise.

## Approach
Implement the Sellmeier equations for HgGa2S4 (ordinary and extraordinary indices) as reported by Badikov et al. (2004). Use the thermo-optic coefficients dn/dT from Umemura et al. (2012) and/or Mangin et al. (2009) to describe the refractive-index change with temperature. For type-I (oo-e) phase matching at normal incidence (internal angle θ ≈ 52.7°), solve the energy- and momentum-conservation equations to find the signal wavelength near 1446 nm that satisfies the phase-matching condition at two temperatures: the ambient temperature of 22 °C and an elevated temperature of 30 °C (a rise of 8 °C). The shift is the difference between the two signal wavelengths. No other operating condition or extra baseline is required; the calculation is purely numerical with analytic inputs.

## Reproduction target
Produce a JSON file at `/app/outputs/step_01_shift.json` containing a single key `calculated_signal_wavelength_shift_nm` whose value is the computed shift (in nanometers). The shift equals the signal wavelength at 30 °C minus the signal wavelength at 22 °C (both obtained from the phase-matched condition for type-I oo-e interaction at the given cut angle). The expected result is a deterministic numerical value derived solely from the published Sellmeier equations and thermo-optic coefficients.

## Assets

- Badikov et al. (2004) Sellmeier equations for HgGa2S4: 10.1070/QE2004v034n05ABEH002734
- Umemura et al. (2012) thermo-optic coefficients for HgGa2S4: 10.1016/j.optcom.2011.12.058
- Mangin et al. (2009) thermo-optic coefficients for HgGa2S4: 10.1364/JOSAB.26.001702

## Workflow steps

### Step 1: Compute temperature-induced signal wavelength shift
- Role: scored (load-bearing)
- Action: Implement the Sellmeier equations for HgGa2S4 (ordinary and extraordinary) from Badikov et al. (2004) and the thermo-optic coefficients dn/dT from Umemura et al. (2012) and/or Mangin et al. (2009). Using the reported crystal temperature rise of 8°C (from ambient 22°C), compute the type-I (oo-e) phase-matched signal wavelength for normal incidence near 1446 nm at 22°C and 30°C. Calculate the wavelength shift as the difference. Write the shift (in nanometers) to the output file.
- Output file: `/app/outputs/step_01_shift.json`
- Format: json
- Contract: {"calculated_signal_wavelength_shift_nm": "number (float, in nanometers)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_shift.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_shift.json
- path: `/app/outputs/step_01_shift.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed signal wavelength shift in nanometers due to a temperature rise from 22°C to 30°C.
- schema:
  - `type`: object
  - `required`:
    - `calculated_signal_wavelength_shift_nm`: float
  - `units`:
    - `calculated_signal_wavelength_shift_nm`: nm

Notes: The shift is computed from the Sellmeier equations and thermo-optic coefficients. The measured shift reported in the literature is used only as hidden gold for scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_shift.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "calculated_signal_wavelength_shift_nm": "float"
        },
        "units": {
          "calculated_signal_wavelength_shift_nm": "nm"
        }
      },
      "description": "Computed signal wavelength shift in nanometers due to a temperature rise from 22°C to 30°C."
    }
  ],
  "notes": "The shift is computed from the Sellmeier equations and thermo-optic coefficients. The measured shift reported in the literature is used only as hidden gold for scoring."
}
```

## How you are scored
Only the artifact from the workflow step `step_01` is scored (weight 1.0). A hidden verifier will compare your reported shift against a reference value – a high-accuracy calculation based on the same material parameters – and accept an answer that lies within a prescribed tolerance. The tolerance is not disclosed. The verifier does not inspect intermediate workings; it only reads the JSON file. No other artifacts contribute to the score. Your task is to implement the published method faithfully so that the computed shift falls within the acceptance window.
