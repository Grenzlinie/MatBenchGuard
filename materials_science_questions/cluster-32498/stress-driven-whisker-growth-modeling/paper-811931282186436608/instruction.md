# Whiskerette-Induced Nanoscale Roughness Estimation

## Problem background
Nanostructured thin-film (NSTF) fuel cell electrocatalysts consist of oriented crystalline organic whiskers coated with a polycrystalline metal film. The whiskers are rectangular lath-shaped particles with sub-micron lengths and nanoscale cross-sections. When metal is sputter-deposited onto these whiskers, it grows as discrete, acicular crystallites — called whiskerettes — that protrude from the whisker side faces. These whiskerettes increase the catalyst's geometric surface area well beyond what a smooth metal coating would provide. Quantifying this surface-area enhancement in terms of a nanoscale roughness factor and an overall total roughness factor is important for understanding and predicting the electrochemical performance of NSTF electrodes.

## Approach
Model a single organic whisker as a rectangular prism whose side faces carry the majority of the deposited metal surface area. The whisker has mean cross-sectional dimensions of approximately 52.5 nm (wide face) by 27.0 nm (narrow face) and an average length of 1 µm. Compute its geometric side-surface area by treating it as a lath with these flat rectangular faces.

Metal whiskerettes are treated as protrusions with a roughly square cross-section of ~6 nm per side. They nucleate at regular intervals along the whisker, with a center-to-center spacing of 6–8 nm both along and around the whisker perimeter. Their length varies from near zero at the whisker base up to approximately 25 nm at the top, and they project from the whisker surface at a fixed angle. To estimate the total metal surface area contributed by whiskerettes, determine the number of whiskerettes per whisker from the whisker geometry and the reported spacing, then sum the exposed side-wall areas of all whiskerettes (the top-facet areas are comparatively small and can be approximated as part of the side-wall envelope).

From these two area quantities — smooth whisker surface area and total whiskerette surface area — one derives the nanoscale roughness factor (the ratio of whiskerette-covered area to smooth area). Multiplying the nanoscale factor by a separately reported mesoscale roughness factor of 5–8 (which accounts for the areal number density of whiskers on the substrate) yields the estimated total roughness factor range for the NSTF electrode.

## Reproduction target
Write a script that takes the geometric parameters given above and computes: (1) the smooth whisker side-surface area in nm², (2) the estimated number of whiskerettes on a single whisker, (3) the total surface area contributed by all whiskerettes on that whisker in nm², (4) the nanoscale roughness factor (dimensionless ratio), and (5) the total roughness factor range [min, max] obtained by multiplying the nanoscale factor by the mesoscale roughness factors of 5 and 8. Output all five quantities as a single JSON file.

## Assets
No external datasets, models, or pre-trained weights are required. All geometric parameters needed for the computation are listed in the Approach section above. You only need a programming environment capable of numerical calculation and JSON output (e.g., Python with its standard library or NumPy).

## Workflow steps

### Step 1: Calculate nanoscale and total roughness factors
- Role: scored
- Action: Implement a script that calculates, from the given geometric parameters (whisker cross‑sections ~50 nm × 25 nm, average length 1 μm; whiskerette cross‑section ~6 nm, spacing ~6–8 nm, length varying 0–25 nm), the smooth whisker surface area, the number of whiskerettes per whisker, the total whiskerette surface area, the nanoscale roughness factor (ratio), and the total roughness factor range (using mesoscale factors 5–8). Output the results as a JSON file.
- Output file: `/app/outputs/whisker_roughness_calculation.json`
- Format: json
- Contract: JSON object with keys: smooth_whisker_surface_area_nm2 (float), whiskerette_count (int), total_whiskerette_surface_area_nm2 (float), nanoscale_roughness_factor (float), total_roughness_factor_range (array of two floats, [min, max])
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/whisker_roughness_calculation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### whisker_roughness_calculation.json
- path: `/app/outputs/whisker_roughness_calculation.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Derived nanoscale and total roughness factors from whisker and whiskerette dimensions, used to verify the geometric roughness enhancement claim.
- schema:
  - `type`: object
  - `required`: `smooth_whisker_surface_area_nm2`, `whiskerette_count`, `total_whiskerette_surface_area_nm2`, `nanoscale_roughness_factor`, `total_roughness_factor_range`
  - `properties`:
    - `smooth_whisker_surface_area_nm2`:
      - `type`: number
      - `unit`: nm2
      - `description`: Surface area of the smooth whisker side faces in square nanometers.
    - `whiskerette_count`:
      - `type`: integer
      - `description`: Estimated number of whiskerettes on a single whisker.
    - `total_whiskerette_surface_area_nm2`:
      - `type`: number
      - `unit`: nm2
      - `description`: Total metal surface area contributed by all whiskerettes on a single whisker.
    - `nanoscale_roughness_factor`:
      - `type`: number
      - `description`: Ratio of total whiskerette surface area to smooth whisker surface area (dimensionless).
    - `total_roughness_factor_range`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 2
      - `maxItems`: 2
      - `description`: Estimated total roughness factor range [min, max] when multiplied by mesoscale roughness factors 5-8 (dimensionless).

Notes: The nanoscale roughness factor is recomputed by the checker as total_whiskerette_surface_area_nm2 / smooth_whisker_surface_area_nm2 and compared to a hidden reference. The total roughness factor range is checked for overlap with the expected range derived from mesoscale factors 5-8.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "whisker_roughness_calculation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "smooth_whisker_surface_area_nm2",
          "whiskerette_count",
          "total_whiskerette_surface_area_nm2",
          "nanoscale_roughness_factor",
          "total_roughness_factor_range"
        ],
        "properties": {
          "smooth_whisker_surface_area_nm2": {
            "type": "number",
            "unit": "nm2",
            "description": "Surface area of the smooth whisker side faces in square nanometers."
          },
          "whiskerette_count": {
            "type": "integer",
            "description": "Estimated number of whiskerettes on a single whisker."
          },
          "total_whiskerette_surface_area_nm2": {
            "type": "number",
            "unit": "nm2",
            "description": "Total metal surface area contributed by all whiskerettes on a single whisker."
          },
          "nanoscale_roughness_factor": {
            "type": "number",
            "description": "Ratio of total whiskerette surface area to smooth whisker surface area (dimensionless)."
          },
          "total_roughness_factor_range": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 2,
            "maxItems": 2,
            "description": "Estimated total roughness factor range [min, max] when multiplied by mesoscale roughness factors 5-8 (dimensionless)."
          }
        }
      },
      "description": "Derived nanoscale and total roughness factors from whisker and whiskerette dimensions, used to verify the geometric roughness enhancement claim."
    }
  ],
  "notes": "The nanoscale roughness factor is recomputed by the checker as total_whiskerette_surface_area_nm2 / smooth_whisker_surface_area_nm2 and compared to a hidden reference. The total roughness factor range is checked for overlap with the expected range derived from mesoscale factors 5-8."
}
```

## How you are scored
A hidden verifier reads your output JSON file and independently recomputes the nanoscale roughness factor from your reported smooth whisker surface area and total whiskerette surface area. It compares the recomputed factor to an independently established reference value for the same geometry. It also checks whether your total roughness factor range overlaps with the expected range derived from the combination of nanoscale and mesoscale roughness factors. Your score depends on how closely your computed quantities agree with those references; merely reporting numbers without a correct geometric derivation will not receive full credit.
