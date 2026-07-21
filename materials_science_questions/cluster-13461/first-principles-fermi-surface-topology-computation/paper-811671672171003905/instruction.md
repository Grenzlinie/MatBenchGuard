# Extract calculated dHvA frequencies and masses from provided paper

## Problem background
Certain layered molecular conductors that incorporate transition metal ions can exhibit a rich electronic structure, with low‑dimensional bands arising from organic π‑orbitals and additional bands originating from metal d‑orbitals. In the system studied in the accompanying paper, tight‑binding band‑structure calculations are reported for (DMe‑DCNQI)₂Cu. Table I of the paper lists calculated de Haas–van Alphen frequencies (`F_cal`) and band cyclotron masses (`m_b_cal`) for a number of cyclotron orbits.

## Task
From the provided paper (see Table I in the paper content above), extract the `F_cal` and `m_b_cal` values for the six specific cyclotron orbits listed below and write them to a CSV file.

## Required orbits
- α (field parallel to the c axis, θ = 0°)
- β (field direction: θ = 60°)   ← **only this orientation; the ω = 0° entry in Table I is not needed**
- γ (ω = 0°)
- δ2 (ω = 25°)
- ε5 (ω = 25°)
- ε8 (ω = 33°)

**Note about ε5 and ε8 masses:** For the high‑frequency orbits ε5 and ε8 the paper does not provide reliable band cyclotron masses (the numbers printed in the `m_b_cal` column of Table I are replicates of the frequencies and are not physically meaningful). You may therefore fill the `mass_ratio_m0` column for ε5 and ε8 with any placeholder (e.g., 0); these two entries will be judged solely on the `frequency_T` value.

## Output file
- Path: `/app/outputs/step_03_cyclotron_orbit_freq.csv`
- Format: CSV
- Columns: `orbit_label`, `frequency_T`, `mass_ratio_m0`
- The `orbit_label` values must match **exactly**: `α`, `β`, `γ`, `δ2`, `ε5`, `ε8`

## Workflow
1. Locate Table I in the paper (the table is reproduced in the problem statement).
2. For each required orbit, read the value in the `F_cal` column (frequency in tesla) and the value in the `m_b_cal` column (cyclotron mass in units of the free electron mass `m₀`). Use the above clarification for ε5/ε8.
3. Write a CSV file with one row per orbit using the extracted numbers.

## Output contract (for your reference)
```json
{
  "outputs": [
    {
      "file": "step_03_cyclotron_orbit_freq.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "orbit_label",
          "frequency_T",
          "mass_ratio_m0"
        ],
        "units": {
          "frequency_T": "tesla",
          "mass_ratio_m0": "dimensionless (in units of m_0)"
        }
      },
      "description": "Computed dHvA frequencies and band cyclotron masses for the selected cyclotron orbits. The values will be compared against independent reference data within prescribed tolerances (not disclosed here)."
    }
  ],
  "notes": "Orbit labels must match exactly: α, β, γ, δ2, ε5, ε8. The checker expects one row for each of the six named orbits."
}
```

## How you are scored
Your submission will be evaluated by comparing your reported frequencies and masses against independent reference values. The exact tolerances are not disclosed; extract the numbers as accurately as possible from Table I.