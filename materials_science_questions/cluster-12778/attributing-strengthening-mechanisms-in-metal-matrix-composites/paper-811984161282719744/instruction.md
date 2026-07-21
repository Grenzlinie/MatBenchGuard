# Strengthening Contributions in Boron-Modified Titanium Alloy Composite via Load Sharing, Hall-Petch, and Orowan Models

## Problem background
Titanium alloys reinforced with TiB whiskers exhibit improved strength and stiffness compared to the unreinforced base alloy. The strengthening of these composites arises from multiple mechanisms acting across different length scales: load transfer from the soft matrix to stiff micrometer-sized whiskers, grain size refinement of the matrix that increases yield strength (Hall–Petch effect), and dispersion of nanometer-sized particles that obstruct dislocation motion (Orowan strengthening). Quantifying the individual contribution of each mechanism is valuable for understanding the micromechanics of composite strengthening and for guiding alloy and processing design.

## Approach
Compute the strengthening contributions using the specific models and material constants provided below. All required parameters are given; no further literature search is needed.

- **Load sharing** (shear‑lag based): Δσ_LS = σ_ym · V_f · s · C_eff, where:
  - σ_ym = 1000 MPa (matrix yield strength of Ti‑6Al‑4V)
  - V_f = 0.08 (volume fraction of eutectic TiB whiskers)
  - s = 10 (average whisker aspect ratio)
  - C_eff = 0.315 (effective load‑sharing coefficient accounting for orientation and load‑transfer efficiency)

- **Hall–Petch**: Δσ_HP = k_y / √d, where:
  - k_y = 0.0764 MPa·m^(1/2) (Hall‑Petch coefficient for Ti‑6Al‑4V)
  - d = 3 × 10^(-6) m (matrix grain size)

- **Orowan**: Δσ_Or = (0.13 · G_m · b / λ_p) · ln(r_p / b), where:
  - G_m = 44 GPa = 44 × 10^9 Pa (matrix shear modulus)
  - b = 0.295 × 10^(-9) m (Burgers vector of α‑Ti)
  - r_p = 25 × 10^(-9) m (average radius of nanoscale TiB particles)
  - λ_p = 396 × 10^(-9) m (effective inter‑particle spacing)

Each increment is computed in MPa. The total strength increment is the sum of the three contributions: Δσ_total = Δσ_LS + Δσ_HP + Δσ_Or.

## Reproduction target
Using the microstructural parameters and the models/constants given above, compute the strength increments contributed by load sharing, Hall‑Petch, and Orowan strengthening (all in MPa). Sum the three increments to obtain the total strength increment. Write the four quantities to `/app/outputs/strengthening_contributions.json` as a JSON object with keys `load_sharing_increment_MPa`, `hall_petch_increment_MPa`, `orowan_increment_MPa`, and `total_increment_MPa` (all float numbers).

## Assets
No external datasets or pre‑trained models are required. The computations can be performed with standard Python numerical libraries (e.g., numpy, scipy).

## Workflow steps

### Step 1: Compute strengthening contributions
- Role: scored (load-bearing)
- Action: Using the models and constants provided in the **Approach** section, compute the strength increments contributed by load sharing, Hall‑Petch, and Orowan mechanisms. Write the results to the output JSON.
- Output file: `/app/outputs/strengthening_contributions.json`
- Format: json
- Contract: { "load_sharing_increment_MPa": <float>, "hall_petch_increment_MPa": <float>, "orowan_increment_MPa": <float>, "total_increment_MPa": <float> }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strengthening_contributions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strengthening_contributions.json
- path: `/app/outputs/strengthening_contributions.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON object containing the predicted strength increments from load sharing, Hall‑Petch, and Orowan mechanisms, plus the sum.
- schema:
  - `type`: object
  - `required`:
    - `load_sharing_increment_MPa`: number
    - `hall_petch_increment_MPa`: number
    - `orowan_increment_MPa`: number
    - `total_increment_MPa`: number
  - `units`:
    - `load_sharing_increment_MPa`: MPa
    - `hall_petch_increment_MPa`: MPa
    - `orowan_increment_MPa`: MPa
    - `total_increment_MPa`: MPa

Notes: The checker will compute the percentage contribution of each mechanism (increment / total * 100) and compare each to hidden reference values derived from the paper within a tolerance. The output file must contain the four numeric fields.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strengthening_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "load_sharing_increment_MPa": "number",
          "hall_petch_increment_MPa": "number",
          "orowan_increment_MPa": "number",
          "total_increment_MPa": "number"
        },
        "units": {
          "load_sharing_increment_MPa": "MPa",
          "hall_petch_increment_MPa": "MPa",
          "orowan_increment_MPa": "MPa",
          "total_increment_MPa": "MPa"
        }
      },
      "description": "JSON object containing the predicted strength increments from load sharing, Hall-Petch, and Orowan mechanisms, plus the sum."
    }
  ],
  "notes": "The checker will compute the percentage contribution of each mechanism (increment / total * 100) and compare each to hidden reference values derived from the paper within a tolerance. The output file must contain the four numeric fields."
}
```

## How you are scored
The hidden verifier will read `/app/outputs/strengthening_contributions.json`. It will validate the JSON schema and then, for each strengthening mechanism, compute the percentage contribution (increment divided by the total, multiplied by 100). These percentages are compared to hidden reference values derived from the original study. Your score is the fraction of mechanisms whose computed percentage falls within a pre‑defined tolerance of the reference. The JSON file must contain all required fields; missing or improperly typed fields will yield zero credit for the affected mechanism.