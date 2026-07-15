# Thermoelectric Power Factor of Nanocrystalline Si via Two-Phase Transport

## Problem background
Heavily boron‑doped nanocrystalline silicon is a promising thermoelectric material. A theoretical two‑phase transport model describes how grain interiors and grain boundary barriers jointly determine the electrical conductivity and Seebeck coefficient. Understanding this interplay can explain whether a large thermoelectric power factor is achievable at specific carrier concentrations. This task asks you to compute the power factor predicted by the model at a given doping level and temperature, using the provided structural and scattering parameters.

## Approach
The approach is based on the semiclassical Boltzmann transport theory in a three‑dimensional hole band. You will implement the transport integrals for electrical conductivity and Seebeck coefficient, incorporating energy‑dependent scattering from acoustic and optical phonons, ionised impurities (using Brooks–Herring and strongly screened limits), and quantum reflections at grain boundaries via the WKB approximation. The material is treated as a series of grains and grain‑boundary barriers. The composite electrical conductivity follows a series volume‑fraction rule. The composite Seebeck coefficient is obtained by interpolating between a ballistic limit (where the grain‑boundary Seebeck coefficient dominates) and a diffusive limit (where the Seebeck coefficients of the grain and grain‑boundary phases are weighted by their respective thermal conductivities). The interpolation weight corresponds to the fraction of carrier energy relaxation within a grain. You will use the geometric and material parameters listed in the workflow step to calculate the electrical conductivity σ, Seebeck coefficient S, and the power factor σS² at the specified conditions.

## Reproduction target
Compute the thermoelectric power factor σS² at a hole concentration p = 5.6×10¹⁹ cm⁻³ and temperature T = 300 K, using the parameters given in the workflow step. Output the results as a JSON file `/app/outputs/computed_results.json` with three fields: `electrical_conductivity` (in Ω⁻¹ cm⁻¹), `seebeck_coefficient` (in μV K⁻¹), and `power_factor` (in mW m⁻¹ K⁻²).

## Assets
No external datasets or pre‑trained models are required. All necessary physical constants and material parameters are provided in the workflow step. The computation can be performed with standard open‑source Python libraries. Install `numpy` and `scipy` using the Tsinghua mirror:

```bash
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
```

## Workflow steps

### Step 1: Compute two-phase transport properties
- Role: scored (load-bearing)
- Action: Implement the semiclassical Boltzmann transport model for hole transport in nanocrystalline Si, including the transport integrals for electrical conductivity and Seebeck coefficient, the energy-dependent grain-boundary conductivity with WKB transmission, the series conductivity relation, and the ballistic‑diffusive Seebeck interpolation. The energy relaxation fraction (interpolation weight) is C = 0.5 for the given grain size of 30 nm. Use the provided geometric and material parameters (grain length 30 nm, grain-boundary width 2 nm, barrier height 0.165 eV, grain thermal conductivity 12 W m⁻¹ K⁻¹, grain-boundary thermal conductivity 2 W m⁻¹ K⁻¹, 55% grain non‑depleted, phonon MFP λ₀=7.4 nm, scattering exponent r=0, and standard Si band parameters) to compute the electrical conductivity, Seebeck coefficient, and power factor at a hole concentration p=5.6×10¹⁹ cm⁻³ and temperature 300 K.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: A JSON object with exactly three numeric keys: electrical_conductivity (in Ω⁻¹ cm⁻¹), seebeck_coefficient (in μV K⁻¹), power_factor (in mW m⁻¹ K⁻²). All values must be positive numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the three key thermoelectric coefficients computed from the two‑phase transport model at the specified carrier concentration and temperature.
- schema:
  - `type`: object
  - `required`:
    - `electrical_conductivity`: number (Ω⁻¹ cm⁻¹)
    - `seebeck_coefficient`: number (μV K⁻¹)
    - `power_factor`: number (mW m⁻¹ K⁻²)
  - `units`:
    - `electrical_conductivity`: Ω⁻¹ cm⁻¹
    - `seebeck_coefficient`: μV K⁻¹
    - `power_factor`: mW m⁻¹ K⁻²

Notes: The checker recomputes the power factor from the agent’s σ and S for internal consistency and then compares the power factor to a hidden reference value using a relative tolerance. Full credit if the error falls within an acceptable range.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "electrical_conductivity": "number (Ω⁻¹ cm⁻¹)",
          "seebeck_coefficient": "number (μV K⁻¹)",
          "power_factor": "number (mW m⁻¹ K⁻²)"
        },
        "units": {
          "electrical_conductivity": "Ω⁻¹ cm⁻¹",
          "seebeck_coefficient": "μV K⁻¹",
          "power_factor": "mW m⁻¹ K⁻²"
        }
      },
      "description": "Contains the three key thermoelectric coefficients computed from the two‑phase transport model at the specified carrier concentration and temperature."
    }
  ],
  "notes": "The checker recomputes the power factor from the agent’s σ and S for internal consistency and then compares the power factor to a hidden reference value using a relative tolerance. Full credit if the error falls within an acceptable range."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier reads `/app/outputs/computed_results.json` and checks that the three numeric fields are present and positive. It recomputes the power factor from your reported σ and S to verify internal consistency. Then the verifier compares your computed power factor to a reference value using a relative error tolerance. Credit is awarded based on how close your result falls within the acceptable range; the closer, the higher the score. To achieve the best score you must implement the physical model correctly – simply reporting a number without genuine computation will not pass.
