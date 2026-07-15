# Strengthening Contributions in Boron-Modified Titanium Alloy Composite via Load Sharing, Hall-Petch, and Orowan Models

## Problem background
Titanium alloys reinforced with TiB whiskers exhibit improved strength and stiffness compared to the unreinforced base alloy. The strengthening of these composites arises from multiple mechanisms acting across different length scales: load transfer from the soft matrix to stiff micrometer-sized whiskers, grain size refinement of the matrix that increases yield strength (Hall–Petch effect), and dispersion of nanometer-sized particles that obstruct dislocation motion (Orowan strengthening). Quantifying the individual contribution of each mechanism is valuable for understanding the micromechanics of composite strengthening and for guiding alloy and processing design.

## Approach
Compute the strengthening contributions using standard engineering models. For the **load sharing** increment, apply a composite-strengthening model (e.g., shear‑lag theory) that accounts for the whisker volume fraction, aspect ratio, and orientation factor to estimate the extra stress carried by the reinforcement. For the **Hall‑Petch** increment, use the well‑known relation Δσ = k<sub>y</sub> / √d with the matrix grain size; adopt a Hall‑Petch coefficient suitable for Ti‑6Al‑4V. For the **Orowan** increment, calculate the bypass stress required for dislocations to loop around the nanoscale TiB particles based on their size, spacing, and the matrix shear modulus and Burgers vector. Each increment is computed in MPa and the total strength increment is the sum of the three contributions.

## Reproduction target
Using the following microstructural parameters reported for the PA Ti‑64‑1.6B alloy:
- Eutectic TiB whiskers: 8 vol%, width 1–2 µm, aspect ratio 8–12
- Nanoscale TiB particles: 2 vol%, length ≈ 500 nm, diameter ≈ 50 nm
- Matrix grain size: 3 µm

Compute the strength increments contributed by load sharing, Hall‑Petch, and Orowan strengthening (all in MPa). Sum the three increments to obtain the total strength increment. Write the four quantities to `/app/outputs/strengthening_contributions.json` as a JSON object with keys `load_sharing_increment_MPa`, `hall_petch_increment_MPa`, `orowan_increment_MPa`, and `total_increment_MPa` (all float numbers).

## Assets
No external datasets or pre‑trained models are required. The computations can be performed with standard Python numerical libraries (e.g., numpy, scipy).

## Workflow steps

### Step 1: Compute strengthening contributions
- Role: scored (load-bearing)
- Action: Using the microstructural parameters for PA Ti-64-1.6B (eutectic TiB: 8 vol%, width 1-2 µm, aspect ratio 8-12; nanoscale TiB: 2 vol%, length 500 nm, diameter 50 nm; matrix grain size 3 µm) and standard strengthening models (load sharing, Hall-Petch, Orowan), compute the strength increments contributed by each mechanism and write them to the output JSON.
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
- description: JSON object containing the predicted strength increments from load sharing, Hall-Petch, and Orowan mechanisms, plus the sum.
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
