# Critical Radius and Nucleation Energy for Superheated Freon-12 and Freon-22

## Problem background
Superheated drop detectors use superheated liquids suspended in a gel to detect neutrons. When a neutron interacts with the liquid, it can trigger nucleation of a vapor bubble. The theory of bubble formation, based on classical nucleation theory (CNT), describes the free energy of a spherical bubble. The critical bubble radius, at which the bubble becomes thermodynamically unstable, and the minimum energy required to form a bubble of that size, are key parameters that govern the sensitivity of a liquid to neutrons. This task computes these quantities for two common refrigerants, Freon-12 and Freon-22, at a temperature of 30 °C and atmospheric pressure, as required for evaluating their relative performance as detection media.

## Approach
Use classical nucleation theory for a spherical vapor bubble. The free energy of a bubble of radius r is G = 4πr²γ − (4/3)πr³(p_v − p_o), where γ is the liquid-vapor interfacial tension, p_v is the vapor pressure, and p_o is the ambient pressure. The critical radius r_c is found by maximizing G, giving r_c = 2γ/(p_v − p_o). The minimum reversible work (nucleation energy) is W = 16πγ³ / [3(p_v − p_o)²]. Given the surface tension and vapor pressure for each liquid at 30 °C, and ambient pressure p_o = 1.013×10⁶ dyn/cm² (1 atm), compute r_c in cm and W in ergs, then convert W to keV using 1 erg = 6.2415×10⁵ keV. All inputs are in CGS units, so intermediate values will be in erg (dyne·cm).

## Reproduction target
Compute the critical radius r_c (in cm) and minimum nucleation energy W (in keV) for Freon-12 and Freon-22 at 30 °C and atmospheric pressure, using the formulas and conversion factor described above. Output the four numeric results to a JSON file with the keys: "freon12_rc_cm", "freon12_W_keV", "freon22_rc_cm", "freon22_W_keV".

## Assets
No external assets are required. All needed physical parameters (surface tension, vapor pressure, ambient pressure) are listed in the workflow step below.

## Workflow steps

### Step 1: Calculate critical radius and nucleation energy
- Role: scored (load-bearing)
- Action: Using the classical nucleation theory formulas for a spherical vapor bubble: r_c = 2γ/(p_v - p_0) and W = 16πγ³/[3(p_v - p_0)²]. Use the following physical parameters at 30 °C and atmospheric pressure: For Freon-12: surface tension γ=9 dyn/cm, vapor pressure p_v=7.4556×10⁶ dyn/cm²; For Freon-22: γ=8 dyn/cm, p_v=1.1478×10⁷ dyn/cm². Ambient pressure p_0 = 1.013×10⁶ dyn/cm² (1 atm). Compute the critical radius r_c in cm for each substance, and the minimum nucleation energy W in keV (use conversion factor: 1 erg = 6.2415×10⁵ keV; note that dyne·cm = erg). Write the four results to /app/outputs/computed_values.json with keys "freon12_rc_cm", "freon12_W_keV", "freon22_rc_cm", "freon22_W_keV".
- Output file: `/app/outputs/computed_values.json`
- Format: json
- Contract: {"type":"object","required":["freon12_rc_cm","freon12_W_keV","freon22_rc_cm","freon22_W_keV"],"properties":{"freon12_rc_cm":{"type":"number","description":"Critical radius for Freon-12 in cm"},"freon12_W_keV":{"type":"number","description":"Minimum nucleation energy for Freon-12 in keV"},"freon22_rc_cm":{"type":"number","description":"Critical radius for Freon-22 in cm"},"freon22_W_keV":{"type":"number","description":"Minimum nucleation energy for Freon-22 in keV"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_values.json
- path: `/app/outputs/computed_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The four computed critical radii and nucleation energies. The checker will compare these to hidden reference values with a relative tolerance.
- schema:
  - `type`: object
  - `required`: `freon12_rc_cm`, `freon12_W_keV`, `freon22_rc_cm`, `freon22_W_keV`
  - `properties`:
    - `freon12_rc_cm`:
      - `type`: number
      - `description`: Critical radius for Freon-12 in cm
    - `freon12_W_keV`:
      - `type`: number
      - `description`: Minimum nucleation energy for Freon-12 in keV
    - `freon22_rc_cm`:
      - `type`: number
      - `description`: Critical radius for Freon-22 in cm
    - `freon22_W_keV`:
      - `type`: number
      - `description`: Minimum nucleation energy for Freon-22 in keV

Notes: The task is a closed-form classical nucleation theory computation. All inputs are from the paper's own physical parameters; no external datasets or experimental fitting required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "freon12_rc_cm",
          "freon12_W_keV",
          "freon22_rc_cm",
          "freon22_W_keV"
        ],
        "properties": {
          "freon12_rc_cm": {
            "type": "number",
            "description": "Critical radius for Freon-12 in cm"
          },
          "freon12_W_keV": {
            "type": "number",
            "description": "Minimum nucleation energy for Freon-12 in keV"
          },
          "freon22_rc_cm": {
            "type": "number",
            "description": "Critical radius for Freon-22 in cm"
          },
          "freon22_W_keV": {
            "type": "number",
            "description": "Minimum nucleation energy for Freon-22 in keV"
          }
        }
      },
      "description": "The four computed critical radii and nucleation energies. The checker will compare these to hidden reference values with a relative tolerance."
    }
  ],
  "notes": "The task is a closed-form classical nucleation theory computation. All inputs are from the paper's own physical parameters; no external datasets or experimental fitting required."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the computed values from computed_values.json and compares them to independently derived reference values. The verifier checks each of the four quantities and awards a reward based on the agreement. The comparison uses a relative tolerance to account for minor numerical differences arising from unit conversions and floating-point arithmetic. Simply reporting some numbers is not enough; you must correctly apply the formulas and conversion to the given inputs. The final reward is a single score between 0 and 1, where 1 indicates close agreement and lower scores indicate larger deviations. Do not attempt to guess the values or copy them from any external source.
