# Heat Exchanger Γ Factor Evaluation for Thermoelectric Module Microchannels

## Problem background
Waste heat recovery from industrial exhaust streams, such as those in glass manufacturing, can generate usable electrical power through thermoelectric generator (TEG) systems. These systems require compact, high-performance heat exchangers on both the hot and cold sides to maintain large temperature differentials across the thermoelectric modules while dissipating unconverted heat. Microchannel heat exchangers are a promising technology because they provide high heat transfer coefficients in a small volume. A critical figure of merit for these heat exchangers is the ratio of heat transfer to pumping power (Γ); a high Γ indicates efficient use of pumping energy. This task evaluates Γ for two baseline designs—a water-cooled copper cold‑side microchannel heat exchanger and an exhaust‑gas hot‑side heat exchanger—using standard heat transfer and pressure drop correlations.

## Approach
The computation follows the ε‑NTU heat exchanger analysis method. Two independent analyses are performed, one for each heat exchanger. For the cold‑side, we assume fully developed laminar flow in the microchannels; the heat transfer is described by a constant‑heat‑rate Nusselt number correlation for rectangular ducts. For the hot‑side, the flow is turbulent and the Nusselt number is obtained from the Gnielinski correlation, with the friction factor given by a standard turbulent‑flow correlation. In each case, the geometric parameters (channel height, width, overall dimensions) and the mass flow rate are combined with fluid properties (water or exhaust gas properties approximated as air) to compute the hydraulic diameter, the heat transfer coefficient, and then the UA product. Using the effectiveness relation for a heat exchanger with a nearly isothermal interface (C_min/C_max → 0), the actual heat transfer rate is determined, accounting for heat loss factors and interface thermal resistances. The pressure drop is calculated from the friction factor and entrance/exit loss coefficients; the pumping power follows from the mass flow rate and pressure drop. Finally, Γ is the ratio of total heat transfer to pumping power. All required input parameters (geometry, mass flow rates, temperature differences, heat‑loss factors, interface resistances) are provided in the workflow steps; standard fluid and material properties may be taken from engineering references.

## Reproduction target
Compute the heat‑transfer‑to‑pumping‑power factor Γ for two specific heat exchanger designs:
1. A water‑cooled copper microchannel cold‑side design with channel height 0.25 cm, channel width 82 µm, and water mass flow rate 0.18 kg/s.
2. A hot‑side exhaust‑gas copper microchannel design with channel width 1750 µm, channel height 6.35 cm, and exhaust mass flow rate 0.3 kg/s.
Use the published geometry, temperature boundary conditions, heat‑loss factors, and interface resistances. Report the two Γ values by writing them into `/app/outputs/cold_side_gamma.txt` and `/app/outputs/hot_side_gamma.txt` (one line per file, a single floating‑point number).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Cold‑side microchannel Γ computation
- Role: scored
- Action: Using the specified water‑cooled copper microchannel geometry (overall size 12.4 cm × 12.4 cm × 0.6 cm, channel height 0.25 cm, channel width 82 μm), cold‑side mass flow rate 0.18 kg/s, cold‑side temperature difference (T_c − T_amb) = 90 K, cold‑side heat‑loss factors 0.075, interface thermal resistance 0.0004 K/W, and standard water/copper properties at approximately 300 K: compute hydraulic diameter, apply a fully‑developed laminar Nusselt number correlation for a rectangular duct with constant heat rate, calculate heat transfer coefficient and UA_c, effectiveness ε, cold‑side heat transfer rate Q_c, pressure drop ΔP using laminar friction factor and abrupt contraction/expansion loss coefficients, pumping power P_pump, and finally Γ = Q_c / P_pump. Write the single Γ value to cold_side_gamma.txt.
- Output file: `/app/outputs/cold_side_gamma.txt`
- Format: txt
- Contract: single float number without unit, e.g. 3500.0
- Scoring: scored by hidden verifier

### Step 2: Hot‑side exhaust gas Γ computation
- Role: scored
- Action: Using the specified hot‑side copper heat exchanger geometry (overall size 17.8 cm × 11.1 cm × 7.3 cm, channel height 6.35 cm, channel width 1750 μm), exhaust mass flow rate 0.3 kg/s, hot‑side temperature difference (T_ex − T_h) = 353.2 K, hot‑side heat‑loss factors 0.025, interface thermal resistance 0.00035 K/W, and standard exhaust‑gas (air) and copper properties at ~1000 K: compute hydraulic diameter, apply the Gnielinski turbulent‑flow Nusselt number correlation with friction factor f = (1.82 log10 Re_D − 1.64)^(−2), calculate heat transfer coefficient and UA_h, effectiveness ε, hot‑side heat transfer rate Q_h, pressure drop ΔP using the same friction factor and abrupt loss coefficients, pumping power P_pump, and finally Γ = Q_h / P_pump. Write the single Γ value to hot_side_gamma.txt.
- Output file: `/app/outputs/hot_side_gamma.txt`
- Format: txt
- Contract: single float number without unit, e.g. 18.5
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cold_side_gamma.txt`
- `/app/outputs/hot_side_gamma.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cold_side_gamma.txt
- path: `/app/outputs/cold_side_gamma.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Cold‑side microchannel heat transfer to pumping power factor Γ (heat transfer divided by pumping power)
- schema:
  - `type`: text
  - `content`: single float value (Γ factor, dimensionless)

### hot_side_gamma.txt
- path: `/app/outputs/hot_side_gamma.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Hot‑side exhaust gas microchannel heat transfer to pumping power factor Γ
- schema:
  - `type`: text
  - `content`: single float value (Γ factor, dimensionless)

Notes: The hidden checker compares each Γ value against an acceptable interval derived from the paper. Each file must contain exactly one floating‑point number (no units, no extra text).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cold_side_gamma.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content": "single float value (Γ factor, dimensionless)"
      },
      "description": "Cold‑side microchannel heat transfer to pumping power factor Γ (heat transfer divided by pumping power)"
    },
    {
      "file": "hot_side_gamma.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content": "single float value (Γ factor, dimensionless)"
      },
      "description": "Hot‑side exhaust gas microchannel heat transfer to pumping power factor Γ"
    }
  ],
  "notes": "The hidden checker compares each Γ value against an acceptable interval derived from the paper. Each file must contain exactly one floating‑point number (no units, no extra text)."
}
```

## How you are scored
A hidden verifier reads the two output files and extracts each Γ value. It checks that the cold‑side Γ and the hot‑side Γ fall within pre‑defined acceptable intervals that reflect the reference results. If both values lie inside their respective intervals, you receive full credit (1.0); otherwise the score is 0.0. The intervals are wide enough to accommodate legitimate implementation choices in fluid properties and correlation forms. The verifier does not re‑compute your intermediate steps; it only examines the final numbers you write to the files. Therefore, you must faithfully implement the complete heat exchanger analysis—simply guessing or copying a number will not guarantee a correct result.
