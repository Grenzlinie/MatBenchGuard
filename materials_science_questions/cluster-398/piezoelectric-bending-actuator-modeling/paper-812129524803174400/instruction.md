# Static Performance of Electromagnetic and Piezoelectric Microactuators

## Problem background
Micro actuators are essential building blocks for miniaturised systems. Electromagnetic actuators generate force via Lorentz interaction of a current-carrying conductor in a magnetic field; piezoelectric actuators exploit the converse piezoelectric effect to produce strain under an electric field. Both principles have been proposed for micro-scale applications, and their static performance – maximum force and achievable driving range – determines suitability for different design scenarios. This task reproduces a quantitative comparison of the static force and range of a representative electromagnetic actuator and a piezoelectric actuator of similar overall volume, using analytical models and published material data.

## Approach
Both actuators are modelled with simple analytical expressions derived from first principles. The electromagnetic actuator is a cubic moving‑coil design with a NdFeB permanent magnet; its force is proportional to the product of the magnetic field in the gap and the coil current, with the current ceiling set by the allowed current density and the coil cross‑section. The usable driving range is a geometrical fraction of the actuator length, bounded by the region of constant magnetic field. The piezoelectric actuator is a rectangular beam fixed at one end, operating in transverse (31) mode. Its maximum blocked force is obtained from the electromechanical coupling coefficient and the maximum applied voltage (limited by the material’s breakdown field). The maximum free displacement follows from the relevant piezoelectric charge constant and the same maximum electric field. The required input dimensions and material constants (including coercive force of the magnet, PZT properties, and current density limit) are fully specified in the workflow step; the agent implements the corresponding equations and writes the four computed results to a JSON file.

## Reproduction target
Compute the four static performance metrics for the electromagnetic and piezoelectric actuators described in the workflow step, using the given dimensions and material constants:
-  Maximum electromagnetic force (in newtons)
-  Electromagnetic driving range (in metres)
-  Maximum piezoelectric force (in newtons)
-  Maximum piezoelectric displacement (in metres)
Write the four numeric values into a single JSON file `/app/outputs/actuator_results.json` with the exact keys specified in the output contract. The reproduction target is to obtain values that are physically correct according to the specified analytical models and inputs; no dynamic operating point is required.

## Assets

- Python: python3
- NumPy: numpy

## Workflow steps

### Step 1: Compute actuator static performance
- Role: scored
- Action: Compute the maximum static force and driving range for both electromagnetic and piezoelectric microactuators using the given dimensions and material constants. The electromagnetic actuator is a 5×5×5 mm³ cube with NdFeB permanent magnet (coercive force 900 kA/m) and a coil current density limit of 6 A/mm² rms (peak 26.4 A). The piezoelectric actuator is a 25×2.5×2 mm³ beam with PZT properties from Table II (d31 = -180×10⁻¹² m/N, s11^E = 15×10⁻¹¹ m²/N, breakdown voltage 200 V/mm). Compute: (i) maximum electromagnetic force, (ii) electromagnetic driving range, (iii) maximum piezoelectric force, and (iv) piezoelectric maximum displacement. Write these four values into a JSON file with keys em_max_force_N, em_driving_range_m, pe_max_force_N, pe_max_displacement_m.
- Output file: `/app/outputs/actuator_results.json`
- Format: json
- Contract: {
  "em_max_force_N": <float>,
  "em_driving_range_m": <float>,
  "pe_max_force_N": <float>,
  "pe_max_displacement_m": <float>
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/actuator_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### actuator_results.json
- path: `/app/outputs/actuator_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static force and displacement metrics for electromagnetic and piezoelectric microactuators.
- schema:
  - `type`: object
  - `required`:
    - `em_max_force_N`: number
    - `em_driving_range_m`: number
    - `pe_max_force_N`: number
    - `pe_max_displacement_m`: number

Notes: The output file contains four numeric fields: electromagnetic maximum force in Newtons, electromagnetic driving range in meters, piezoelectric maximum force in Newtons, and piezoelectric maximum displacement in meters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "actuator_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "em_max_force_N": "number",
          "em_driving_range_m": "number",
          "pe_max_force_N": "number",
          "pe_max_displacement_m": "number"
        }
      },
      "description": "Static force and displacement metrics for electromagnetic and piezoelectric microactuators."
    }
  ],
  "notes": "The output file contains four numeric fields: electromagnetic maximum force in Newtons, electromagnetic driving range in meters, piezoelectric maximum force in Newtons, and piezoelectric maximum displacement in meters."
}
```

## How you are scored
A hidden verifier reads your submitted `/app/outputs/actuator_results.json` and extracts the four numeric fields. Each field is compared against an independently determined correct value, and a partial-credit scalar reward is computed based on the accuracy of the reported quantities. The aggregation across the four fields produces the final score. Reporting a number that appears plausible is not sufficient; the values must be consistent with the analytical models and input parameters given in the workflow step. No paper identity, gold values, or tolerances are revealed to you – you must derive the results from the specification alone.
