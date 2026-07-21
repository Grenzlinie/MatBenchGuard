# Reduction in Heterogeneous Nucleation Work by Nickel-Plating for Al₂O₃/Al Composites

## Problem background
When solidification nuclei form on a foreign substrate, the energy barrier is lower than for homogeneous nucleation. The ratio of heterogeneous to homogeneous nucleation work for a spherical cap nucleus on a flat substrate is given by the classical wetting function

```
f(θ) = (2 - 3 cos θ + cos³ θ) / 4
```

where **θ** is the contact angle between the solidifying metal and the substrate.

Aluminium‑based composites reinforced with Al₂O₃ nanoparticles suffer from poor wettability: the wetting angle of molten aluminium on bare Al₂O₃ is **94°**. Electroless nickel‑plating of the nanoparticles replaces the Al/Al₂O₃ interface with an Al/Ni interface, whose wetting angle is **45°**. This change drastically reduces the nucleation work and promotes a fine, uniform microstructure.

In this task you will compute the nucleation work ratios for the two substrate conditions and the **percentage reduction** in heterogeneous nucleation work achieved by the nickel coating.

## Task
Using the two fixed wetting angles and the formula above, compute three quantities:

1. Nucleation work ratio for **uncoated Al₂O₃** (θ = 94°)
2. Nucleation work ratio for **Ni‑coated Al₂O₃** (θ = 45°)
3. Percentage reduction in nucleation work, defined as

```
reduction_percent = (ratio_Al2O3 - ratio_NiAl2O3) / ratio_Al2O3 × 100
```

Write the results to a single JSON file at `/app/outputs/nucleation_work_results.json`.

## Output file
- **Path:** `/app/outputs/nucleation_work_results.json`
- **Format:** JSON object with the following keys and numeric values:
  - `wetting_angle_Al2O3`         (degrees)
  - `nucleation_work_ratio_Al2O3` (dimensionless)
  - `wetting_angle_NiAl2O3`       (degrees)
  - `nucleation_work_ratio_NiAl2O3` (dimensionless)
  - `reduction_percent`           (%)

The computation is deterministic; use the standard math library (e.g., `math.radians`, `math.cos`) to evaluate the cosine terms. All numeric values must be written with the number type—no strings, no extra commentary.

## Scoring
Your output file will first be checked for correct format and required fields. The hidden verifier will then recompute the nucleation work ratios and the reduction percentage directly from the wetting angles you report, using the same formula given above. Your reported values must be consistent with those re‑computed values. No paper‑reported target values are used in scoring; only internal consistency with the formula and your own angles matters.

**Important:** Do **not** include any identifying information (author names, DOIs, journal titles) in your outputs. The submission must contain only the JSON file described above.