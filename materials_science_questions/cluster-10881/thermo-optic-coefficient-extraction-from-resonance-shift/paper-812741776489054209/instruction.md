# Thermo-Optic Coefficients and Electronic Polarizability of Molybdenum Bronze Thin Films

## Problem background
Molybdenum trioxide (MoO₃) thin films and their hydrogen- and lithium-inserted bronze forms (HₓMoO₃, LiₓMoO₃) are important materials for electrochromic devices, optical switching coatings, and solid‑state microbatteries. Their performance depends sensitively on how the optical constants—refractive index n and extinction coefficient k—vary with temperature. This work addresses the extraction of thermo‑optic coefficients (dn/dT and dk/dT) and the calculation of film density and electronic polarizability from ellipsometric n and k data measured over a wide temperature range (100–373 K). The experiments provide tabulated n and k values at different temperatures for MoO₃ and two bronze compositions during heating and cooling cycles. The core challenge is to process these tables into the derived physical quantities that govern the films' thermal‑optical behaviour.

## Approach
The reproduction uses a two‑stage computation on the provided ellipsometric data (a CSV containing material, temperature_K, cycle, n, and k).  

1. **Thermo‑optic coefficients.** For each material, restrict attention to the high‑temperature heating cycle (295–373 K). Between every pair of consecutive rows compute the finite‑difference slopes dn/dT and dk/dT. Collect all these slope values and report the minimum and maximum for each material, separately for dn/dT and dk/dT.  

2. **Film density and electronic polarizability.** For every row (all temperatures, all materials, all cycles), compute the film density ρ_f (g/cm³) from the refractive index n using the Lorentz‑Lorenz relation that connects refractive index to density via known bulk properties. Using that density, compute the electronic polarizability α_e (cm³) through the standard Lorentz‑Lorenz formula that relates refractive index, density, molecular weight, and Avogadro's number.  

The required formulas are specified in the workflow steps below and must be applied exactly as given.

## Reproduction target
From the provided ellipsometric CSV, produce two JSON artifacts:  

* `thermo_optic_coefficients.json`: an array of objects, one per material (MoO₃, H₀.₁₃₄MoO₃, Li₀.₄₂MoO₃), each giving the material name, the fixed `temperature_range` "high" and `cycle` "heating", and the minimum and maximum values of dn/dT and dk/dT observed within the 295–373 K heating cycle.  

* `density_polarizability.json`: an array of objects, one per every row in the CSV, each giving the material name, the temperature in Kelvin, the computed film density (g/cm³), and the computed electronic polarizability (cm³).  

All outputs must be written to `/app/outputs/` with the exact filenames and JSON schemas described in the workflow steps.

## Assets

- Ellipsometric data for MoO3, H0.134MoO3, Li0.42MoO3 thin films: 10.1007/s11664-019-07548-1

## Workflow steps

### Step 1: Compute Thermo-Optic Coefficients
- Role: scored (load-bearing)
- Action: Read the ellipsometric data CSV. For each material (MoO3, H0.134MoO3, Li0.42MoO3) and for the high-temperature heating cycle (295–373 K), compute successive finite differences dn/dT and dk/dT using consecutive rows. Determine the minimum and maximum of dn/dT and dk/dT over that range. Output a JSON array.
- Output file: `/app/outputs/thermo_optic_coefficients.json`
- Format: json
- Contract: [{"material": "string", "temperature_range": "high", "cycle": "heating", "dn_dT_min": float, "dn_dT_max": float, "dk_dT_min": float, "dk_dT_max": float}]
- Scoring: scored by hidden verifier

### Step 2: Compute Film Density and Electronic Polarizability
- Role: scored
- Action: Using the same ellipsometric data, for every row compute film density (g/cm³) via ρ_f = 6.96 * (n²−1)/(n²+2) and electronic polarizability (cm³) via α_e = 5.711 × (n²−1)/(n²+2) / ρ_f. Output a JSON array.
- Output file: `/app/outputs/density_polarizability.json`
- Format: json
- Contract: [{"material": "string", "temperature_K": float, "density_g_per_cm3": float, "polarizability_cm3": float}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_optic_coefficients.json`
- `/app/outputs/density_polarizability.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_optic_coefficients.json
- path: `/app/outputs/thermo_optic_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Minimum and maximum thermo-optic coefficients dn/dT and dk/dT for MoO3, H0.134MoO3, and Li0.42MoO3 during the high-temperature heating cycle (295–373 K).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `temperature_range`, `cycle`, `dn_dT_min`, `dn_dT_max`, `dk_dT_min`, `dk_dT_max`
    - `properties`:
      - `material`:
        - `type`: string
      - `temperature_range`:
        - `type`: string
        - `enum`: `high`
      - `cycle`:
        - `type`: string
        - `enum`: `heating`
      - `dn_dT_min`:
        - `type`: number
        - `description`: minimum dn/dT (K⁻¹) over the range
      - `dn_dT_max`:
        - `type`: number
        - `description`: maximum dn/dT (K⁻¹) over the range
      - `dk_dT_min`:
        - `type`: number
        - `description`: minimum dk/dT (K⁻¹) over the range
      - `dk_dT_max`:
        - `type`: number
        - `description`: maximum dk/dT (K⁻¹) over the range

### density_polarizability.json
- path: `/app/outputs/density_polarizability.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Film density and electronic polarizability at each temperature point for all materials, computed from refractive index n using Lorentz-Lorenz relations.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `temperature_K`, `density_g_per_cm3`, `polarizability_cm3`
    - `properties`:
      - `material`:
        - `type`: string
      - `temperature_K`:
        - `type`: number
        - `description`: temperature in Kelvin
      - `density_g_per_cm3`:
        - `type`: number
        - `description`: film density in g/cm³
      - `polarizability_cm3`:
        - `type`: number
        - `description`: electronic polarizability in cm³

Notes: Both artifacts are re-derivable from the provided ellipsometric data. The checker will recompute the values independently and compare them to paper-reported references with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_optic_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "temperature_range",
            "cycle",
            "dn_dT_min",
            "dn_dT_max",
            "dk_dT_min",
            "dk_dT_max"
          ],
          "properties": {
            "material": {
              "type": "string"
            },
            "temperature_range": {
              "type": "string",
              "enum": [
                "high"
              ]
            },
            "cycle": {
              "type": "string",
              "enum": [
                "heating"
              ]
            },
            "dn_dT_min": {
              "type": "number",
              "description": "minimum dn/dT (K⁻¹) over the range"
            },
            "dn_dT_max": {
              "type": "number",
              "description": "maximum dn/dT (K⁻¹) over the range"
            },
            "dk_dT_min": {
              "type": "number",
              "description": "minimum dk/dT (K⁻¹) over the range"
            },
            "dk_dT_max": {
              "type": "number",
              "description": "maximum dk/dT (K⁻¹) over the range"
            }
          }
        }
      },
      "description": "Minimum and maximum thermo-optic coefficients dn/dT and dk/dT for MoO3, H0.134MoO3, and Li0.42MoO3 during the high-temperature heating cycle (295–373 K)."
    },
    {
      "file": "density_polarizability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "temperature_K",
            "density_g_per_cm3",
            "polarizability_cm3"
          ],
          "properties": {
            "material": {
              "type": "string"
            },
            "temperature_K": {
              "type": "number",
              "description": "temperature in Kelvin"
            },
            "density_g_per_cm3": {
              "type": "number",
              "description": "film density in g/cm³"
            },
            "polarizability_cm3": {
              "type": "number",
              "description": "electronic polarizability in cm³"
            }
          }
        }
      },
      "description": "Film density and electronic polarizability at each temperature point for all materials, computed from refractive index n using Lorentz-Lorenz relations."
    }
  ],
  "notes": "Both artifacts are re-derivable from the provided ellipsometric data. The checker will recompute the values independently and compare them to paper-reported references with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores both output files. For each file, the verifier recomputes the expected quantities from the same dataset and formulas, then compares your reported values to the correct references within appropriate tolerances. The two files contribute to the final reward with predefined weights; the total reward is a number between 0 and 1. Simply writing numbers that match the paper's reported results is not enough—the verifier checks that your outputs are consistent with the provided data and the computation described in the workflow. You must therefore faithfully implement the finite‑difference and Lorentz‑Lorenz calculations on the supplied CSV.
