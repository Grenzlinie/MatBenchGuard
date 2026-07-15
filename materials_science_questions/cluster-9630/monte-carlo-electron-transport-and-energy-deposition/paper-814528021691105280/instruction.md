# Si p-n and Ni/Si Schottky Betavoltaic Performance Optimization

## Problem background
Betavoltaic batteries use a radioisotope source and a semiconductor junction to convert beta‑particle energy directly into electricity. This work theoretically optimises silicon (Si) parameters for a p‑n junction and a Ni/Si Schottky barrier structure, aiming to maximise conversion efficiency under irradiation from a ⁶³Ni source. The core device physics is described by minority‑carrier diffusion equations, and the required electron‑hole pair generation profiles are taken from prior Monte Carlo simulations whose parameters are supplied.

## Approach
Implement the analytic semiconductor device equations for both the Si p‑n junction and the Ni/Si Schottky barrier betavoltaic cells. For the p‑n junction, the generation rate is modelled as G(x)=G₀ exp(‑αx) with given parameters G₀ and α; for the Schottky barrier, use the number of electron‑hole pairs generated per beta particle and the stopping range Lₐ. Combine these with the optimised device dimensions and doping levels provided in the workflow steps, together with physical constants and established Si material parameters (dielectric constant, intrinsic carrier concentration, effective density of states, minority‑carrier diffusion coefficients, surface recombination velocities, etc.).

For the p‑n structure, compute the minority‑carrier diffusion lengths, the depletion width, the three current‑density contributions (emitter, base, and depletion), and then the short‑circuit current density Jsc, saturation current J₀, open‑circuit voltage Voc, fill factor FF, and conversion efficiency η. For the Schottky structure, compute the depletion and n‑region contributions to Jsc, the saturation current from thermionic emission, and then Voc, FF, and η. All calculations should use the standard semiconductor equations and numerical libraries as required.

## Reproduction target
Compute and output the following performance metrics for both device structures: short‑circuit current density (Jsc) in nA/cm², open‑circuit voltage (Voc) in V, fill factor (FF, dimensionless), and conversion efficiency (η) in %. Additionally, compute the ratio of the p‑n efficiency to the Schottky efficiency. Write all nine values as a JSON object to the file `/app/outputs/betavoltaic_results.json` following the schema defined in the workflow step.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Betavoltaic Performance Metrics
- Role: scored (load-bearing)
- Action: Calculate the short-circuit current density (Jsc), open-circuit voltage (Voc), fill factor (FF), and conversion efficiency (η) for both Si p-n junction and Ni/Si Schottky barrier betavoltaic batteries using the analytic semiconductor device equations. For the p-n junction, use the generation profile G(x)=G0 exp(-αx) with G0=3.7×10¹⁵ cm⁻³ s⁻¹ and α=3697 cm⁻¹. For the Schottky barrier, use the number of generated EHPs per beta particle (≈2200) and the stopping range L_a=9.5 μm. Combine these with the optimised device dimensions and doping levels: p-n: emitter doping N_D=1×10¹⁹ cm⁻³, base doping N_A=1×10¹⁷ cm⁻³, junction depth x_j=0.1 μm, base thickness h≈400 μm; Schottky: epi-layer doping N_D=1×10¹³ cm⁻³, Ni thickness 0.1 μm, epi-layer thickness 11 μm. Use physical constants (k, q, ε0, etc.) and material parameters (Si dielectric constant, intrinsic carrier concentration, effective density of states, minority‑carrier diffusion coefficients, surface recombination velocities, etc.) as required. Compute all current-density components (emitter, base, depletion) for the p-n junction and the corresponding components for the Schottky structure; then derive Jsc, J0, Voc, FF, and η for each. Output all computed values in a single JSON file.
- Output file: `/app/outputs/betavoltaic_results.json`
- Format: json
- Contract: {
  "pn_jsc": <float>,  // nA/cm²
  "pn_voc": <float>,  // V
  "pn_ff": <float>,   // dimensionless
  "pn_eta": <float>,  // %
  "schottky_jsc": <float>,
  "schottky_voc": <float>,
  "schottky_ff": <float>,
  "schottky_eta": <float>,
  "efficiency_ratio": <float>  // pn_eta / schottky_eta
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/betavoltaic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### betavoltaic_results.json
- path: `/app/outputs/betavoltaic_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed betavoltaic performance metrics for Si p-n junction and Ni/Si Schottky barrier structures.
- schema:
  - `type`: object
  - `required`:
    - `pn_jsc`: float
    - `pn_voc`: float
    - `pn_ff`: float
    - `pn_eta`: float
    - `schottky_jsc`: float
    - `schottky_voc`: float
    - `schottky_ff`: float
    - `schottky_eta`: float
    - `efficiency_ratio`: float
  - `units`:
    - `pn_jsc`: nA/cm^2
    - `pn_voc`: V
    - `pn_ff`: dimensionless
    - `pn_eta`: %
    - `schottky_jsc`: nA/cm^2
    - `schottky_voc`: V
    - `schottky_ff`: dimensionless
    - `schottky_eta`: %
    - `efficiency_ratio`: dimensionless

Notes: All metrics are compared against paper-reported optimal values with tolerances; exceeding the target (higher Jsc, Voc, FF, η) is not penalized.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "betavoltaic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "pn_jsc": "float",
          "pn_voc": "float",
          "pn_ff": "float",
          "pn_eta": "float",
          "schottky_jsc": "float",
          "schottky_voc": "float",
          "schottky_ff": "float",
          "schottky_eta": "float",
          "efficiency_ratio": "float"
        },
        "units": {
          "pn_jsc": "nA/cm^2",
          "pn_voc": "V",
          "pn_ff": "dimensionless",
          "pn_eta": "%",
          "schottky_jsc": "nA/cm^2",
          "schottky_voc": "V",
          "schottky_ff": "dimensionless",
          "schottky_eta": "%",
          "efficiency_ratio": "dimensionless"
        }
      },
      "description": "Computed betavoltaic performance metrics for Si p-n junction and Ni/Si Schottky barrier structures."
    }
  ],
  "notes": "All metrics are compared against paper-reported optimal values with tolerances; exceeding the target (higher Jsc, Voc, FF, η) is not penalized."
}
```

## How you are scored
A hidden verifier will read the produced `betavoltaic_results.json`, compare each computed metric to independently stored reference values, and assign a reward between 0 and 1. The reward is 1.0 if all metrics are within the expected agreement range, and it degrades linearly with increasing deviation. The reference values and tolerances are not disclosed; a careful implementation of the analytic equations using the given parameters will yield a high reward.
