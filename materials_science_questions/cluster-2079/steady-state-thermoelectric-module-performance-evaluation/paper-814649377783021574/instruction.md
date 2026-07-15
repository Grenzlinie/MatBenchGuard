# TEG temperature difference simulation for marine gearbox energy harvesting

## Problem background
Wireless sensor nodes for condition monitoring of marine gearboxes require a continuous 2 mW power supply. Thermoelectric generators (TEGs) can harvest frictional heat from the gearbox by exploiting the temperature difference between a hot source (oil/gearbox surface) and a cold sink (cooling water/ambient air). This work evaluates several design variants through steady‑state thermal simulations: an actively cooled TEG placed between the oil line and the cooling water line (variants A‑1 and A‑2), and passively cooled TEGs mounted on the gearbox housing with different heat sinks (variants B‑1 to B‑6). The simulations predict the temperature difference ΔT across the TEG module, which directly determines the electrical power. Your task is to reproduce these ΔT values for two representative conditions using the provided material properties and geometries.

## Approach
Use a steady‑state thermal simulation (finite‑element or lumped‑parameter model) to compute the temperature distribution in the TEG assembly. Model the TEG 127‑200‑28 (30 × 30 × 4.8 mm) as a stack of ceramic plates, p‑ and n‑type bismuth‑telluride thermolegs, and copper interconnects, surrounded by the structural components described below.

For variant A‑1 (active cooling): the hot side is an oil‑line adapter at 70 °C; the cold side is a cooling‑water adapter (punch) held at 35 °C. The TEG is sandwiched between them with thermal contact.

For variant B‑5 (passive cooling): the hot side is a steel gearbox surface at 50 °C. The cold side is the base of the heat sink SK507‑75 (extruded aluminium, dimensions 75 × 90 × 100 mm). The heat sink exchanges heat with ambient air at 25 °C through free convection, characterised by a heat transfer coefficient of 10 W/m²K. The TEG is pressed between the gearbox surface and the heat sink.

Include the relevant material properties (thermal conductivity, specific heat) for aluminium oxide, bismuth‑telluride, copper, extruded aluminium, structural steel, and the insulation/interface materials. The steady‑state temperature difference ΔT is the difference between the temperature of the hot ceramic plate and the cold ceramic plate of the TEG.

## Reproduction target
Implement a thermal simulation to compute the steady‑state temperature difference across the TEG (hot ceramic surface minus cold ceramic surface) for two boundary conditions:
- Variant A‑1: hot side oil‑line adapter at 70 °C, cold side cooling‑water adapter at 35 °C.
- Variant B‑5: hot side gearbox surface at 50 °C, ambient air 25 °C, heat sink SK507‑75, heat transfer coefficient 10 W/m²K.

Output the results as a JSON file with keys "A1_deltaT" and "B5_deltaT", both in degrees Celsius. The hidden verifier will compare your computed values against reference results derived from the paper's simulations.

## Assets

- Open-source thermal simulation solver: any open-source steady-state thermal simulation framework, e.g., FEniCS, SfePy, or custom Python thermal circuit model with numpy

## Workflow steps

### Step 1: Thermal simulation for two design variants
- Role: scored (load-bearing)
- Action: Implement a steady-state thermal simulation (e.g., finite element or lumped-parameter model) of the thermoelectric module cooling system for two design variants: (1) active-cooled variant A-1 with TEG between oil line at 70°C and cooling water line at 35°C; (2) passive-cooled variant B-5 with TEG on 50°C gearbox surface, SK507-75 heat sink in 25°C ambient, heat transfer coefficient 10 W/m²K. Use the material properties and geometries provided in the instruction. Compute the temperature difference across the TEG's ceramic plates (hot side minus cold side) for each variant. Output the two ΔT values in a JSON file.
- Output file: `/app/outputs/step_01_temperature_differences.json`
- Format: json
- Contract: {"type": "object", "required": ["A1_deltaT", "B5_deltaT"], "properties": {"A1_deltaT": {"type": "number", "description": "Temperature difference in °C"}, "B5_deltaT": {"type": "number", "description": "Temperature difference in °C"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_temperature_differences.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_temperature_differences.json
- path: `/app/outputs/step_01_temperature_differences.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed temperature difference across the TEG surfaces for the two representative design variants. The checker verifies these values against hidden references and threshold conditions to confirm the power requirement fulfillment.
- schema:
  - `type`: object
  - `required`: `A1_deltaT`, `B5_deltaT`
  - `properties`:
    - `A1_deltaT`:
      - `type`: number
      - `description`: ΔT in °C for variant A-1
    - `B5_deltaT`:
      - `type`: number
      - `description`: ΔT in °C for variant B-5
  - `units`:
    - `A1_deltaT`: °C
    - `B5_deltaT`: °C

Notes: The ΔT values directly support the paper's central claim: variant A-1 meets the 2 mW power requirement, while B-5 does not reliably meet it. The checker uses tolerance and threshold checks on ΔT, not direct power comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_temperature_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "A1_deltaT",
          "B5_deltaT"
        ],
        "properties": {
          "A1_deltaT": {
            "type": "number",
            "description": "ΔT in °C for variant A-1"
          },
          "B5_deltaT": {
            "type": "number",
            "description": "ΔT in °C for variant B-5"
          }
        },
        "units": {
          "A1_deltaT": "°C",
          "B5_deltaT": "°C"
        }
      },
      "description": "Computed temperature difference across the TEG surfaces for the two representative design variants. The checker verifies these values against hidden references and threshold conditions to confirm the power requirement fulfillment."
    }
  ],
  "notes": "The ΔT values directly support the paper's central claim: variant A-1 meets the 2 mW power requirement, while B-5 does not reliably meet it. The checker uses tolerance and threshold checks on ΔT, not direct power comparison."
}
```

## How you are scored
An automated verifier reads your submitted `step_01_temperature_differences.json` and compares the two values against hidden reference standards (the paper's reported ΔT for the same conditions). The reward for this step is computed from how close each ΔT is to its reference: full credit is awarded when the values lie within a physics‑motivated tolerance (defined by the verifier), and credit decays smoothly as the deviation grows. Additionally, the verifier checks that `A1_deltaT` meets a hidden threshold required for the TEG to supply sufficient continuous power; failure to meet this threshold reduces the reward. The overall final score is the weighted result of this scored step (weight 1.0). A faithful re‑implementation of the thermal simulation is required; guessing a value or reproducing a memorised number without executing the proper procedure is unlikely to satisfy the tolerance and threshold checks.
