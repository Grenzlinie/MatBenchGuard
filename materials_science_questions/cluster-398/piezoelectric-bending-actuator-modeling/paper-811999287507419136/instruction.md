# Piezoelectric Hybrid Actuator Displacement Calculation

## Problem background
A hybrid actuation system (HYBAS) combines a negative‑strain component that contracts under an electric field with a positive‑strain component that elongates, aiming to amplify displacement. An analytical model describes the buckled beam profile of the positive‑strain element and its maximum displacement, both governed by a parameter c that satisfies an integral equation involving the arc length of the buckled beam and the effective strains of the active components. This parameter c must be computed numerically; from it, the displacement profile and its maximum are predicted for any chosen geometry and material pair. The objective of this task is to implement the numerical solver that finds c and to use it to predict actuator displacement for the original HYBAS configuration and for a set of candidate material combinations, thereby enabling systematic material selection for enhanced performance.

## Approach
The HYBAS actuator is modeled as a beam fixed at both ends, with the negative‑strain component setting the dynamic length Ld = L0 (1 + s_neg) where s_neg is the effective strain (free piezoelectric strain d31 × V / t). The positive‑strain component buckles and its displacement profile follows w(x) = c [ (Ld/2)² – x² ]², leading to maximum displacement w_max = c Ld⁴ / 16.

The core challenge is finding c. This is done by equating two expressions for the total arc length of the buckled positive‑strain beam:
  (1) the integral ∫_{-Ld/2}^{Ld/2} sqrt( (dw/dx)² + 1 ) dx, which depends on c, and
  (2) the elongated length L0 (1 + s_pos_eff), where s_pos_eff = (d31 × V / t) / (1 + k) is the effective strain reduced by the clamping stiffness k.

The clamping ratio k is computed as the sum of the stiffness (E × thickness × width) of all inactive layers (inactive EAP layer, epoxy layer, gold electrodes, unelectroded margins) divided by the stiffness of the active EAP layer, using the dimensions and Young’s moduli of the original HYBAS (listed below).

The left‑hand integral is evaluated numerically with a left‑hand Riemann sum using 1000 subintervals. Starting from an initial guess for c, the solver iteratively adjusts c until the percent difference between the left‑side integral and the right‑side length falls below 0.001%. The resulting c and the achieved percent error are recorded. The same solver is later applied to the trade‑study material combinations.

**Required dimensional and material constants**

*Original HYBAS geometry (effective length 5.5 mm for all components)*
- ESC component: thickness 470 µm, total width 3 mm, effective width 3 mm, Young’s modulus 20 GPa.
- Active EAP layer: thickness 16 µm, total width 4.5 mm, effective width 3 mm, Young’s modulus 1 GPa.
- Inactive EAP layer: thickness 15 µm, total width 4.5 mm, effective width 4.5 mm, Young’s modulus 1 GPa.
- Epoxy layer: thickness 1 µm, total width 4.5 mm, effective width 4.5 mm, Young’s modulus 5 GPa.
- Gold electrodes on EAP: thickness 0.1 µm, total width 3 mm, effective width 3 mm, Young’s modulus 74 GPa.
- Unelectroded margins: thickness 16 µm, total width 0.75 mm, effective width 0.75 mm, Young’s modulus 1 GPa.

*Piezoelectric constants for the original configuration*
- Negative‑strain (ESC) d31 = –970 pC/N.
- Positive‑strain (EAP) d31 = 20 pC/N.

*Trade‑study materials (use same geometric dimensions as the original ESC and EAP layers respectively)*
Negative‑strain components:
- Hard PZT (TRS100HD): d31 = –150 pC/N, Young’s modulus 79 GPa.
- Soft PZT (TRSHK1HD): d31 = –360 pC/N, Young’s modulus 67 GPa.
- PZN‑4.5%PT single crystal: d31 = –970 pC/N, Young’s modulus 12 GPa.

Positive‑strain components:
- Uni‑axial PVDF: d31 = 20 pC/N, Young’s modulus 2 GPa.
- Bi‑axial PVDF: d31 = 8 pC/N, Young’s modulus 2 GPa.

## Reproduction target
1. Compute, for the original HYBAS configuration at applied RMS voltages 200, 400, 800, 1600 V and for each activation mode (EAP only, ESC only, HYBAS), the parameter c (in units of 10⁶ m⁻³) and the percent error of the arc‑length equality. Save these results to `/app/outputs/c_values.json`.
2. Compute, for every combination of the three negative‑strain materials and the two positive‑strain materials at RMS voltages 100 V and 650 V with both components active, the maximum displacement w_max = c Ld⁴ / 16 (in micrometers). Save these results to `/app/outputs/max_displacements.json`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute c values for original HYBAS configuration
- Role: scored
- Action: Implement the iterative solver based on the HYBAS model. Using the geometry and material properties of the original HYBAS (Table 1 dimensions, L0=5.5 mm, d31 ESC = -970 pC/N, d31 EAP = 20 pC/N), compute the parameter c (in 10^6/m^3) and the percent error between left- and right-hand sides of the arc-length equality for applied RMS voltages 200, 400, 800, 1600 V and for each activation mode: EAP only, ESC only, HYBAS. Solve by numerically integrating the left-hand side with a Riemann sum using 1000 subintervals, iteratively adjusting c until the percent error is below 0.001%. Output the c value and achieved percent error for each case.
- Output file: `/app/outputs/c_values.json`
- Format: json
- Contract: Array of objects, each having numeric 'voltage' (V), string 'active_elements' (one of "EAP","ESC","HYBAS"), numeric 'c' (10^6/m^3), and numeric 'percent_error' (%).
- Scoring: scored by hidden verifier

### Step 2: Compute max displacements for trade study
- Role: scored (load-bearing)
- Action: Using the same solver, for every combination of three negative strain materials (Hard PZT (TRS100HD), Soft PZT (TRSHK1HD), PZN-4.5%PT single crystal) and two positive strain materials (Uni-axial PVDF, Bi-axial PVDF) at RMS voltages of 100 V and 650 V with both components active, compute the maximum displacement w_max = c L_d^4 / 16. Use the geometric dimensions from Table 1 and the material properties from Table 3 (d31 and Young's moduli). Output the maximum displacement in micrometers for each configuration.
- Output file: `/app/outputs/max_displacements.json`
- Format: json
- Contract: Array of objects, each having string 'negative_strain_material', string 'positive_strain_material', numeric 'voltage' (V), and numeric 'max_displacement' (micrometers).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/c_values.json`
- `/app/outputs/max_displacements.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### c_values.json
- path: `/app/outputs/c_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Parameter c and solver accuracy for original HYBAS configuration under different voltages and activation modes.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `voltage`:
        - `type`: number
        - `unit`: V
      - `active_elements`:
        - `type`: string
        - `enum`: `EAP`, `ESC`, `HYBAS`
      - `c`:
        - `type`: number
        - `unit`: 10^6/m^3
      - `percent_error`:
        - `type`: number
        - `unit`: %
    - `required`: `voltage`, `active_elements`, `c`, `percent_error`

### max_displacements.json
- path: `/app/outputs/max_displacements.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Maximum displacement for all six material combinations at two voltages with both components active.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `negative_strain_material`:
        - `type`: string
        - `enum`: `Hard PZT (TRS100HD)`, `Soft PZT (TRSHK1HD)`, `PZN-4.5%PT single crystal`
      - `positive_strain_material`:
        - `type`: string
        - `enum`: `Uni-axial PVDF`, `Bi-axial PVDF`
      - `voltage`:
        - `type`: number
        - `unit`: V
      - `max_displacement`:
        - `type`: number
        - `unit`: micrometers
    - `required`: `negative_strain_material`, `positive_strain_material`, `voltage`, `max_displacement`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "c_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "voltage": {
              "type": "number",
              "unit": "V"
            },
            "active_elements": {
              "type": "string",
              "enum": [
                "EAP",
                "ESC",
                "HYBAS"
              ]
            },
            "c": {
              "type": "number",
              "unit": "10^6/m^3"
            },
            "percent_error": {
              "type": "number",
              "unit": "%"
            }
          },
          "required": [
            "voltage",
            "active_elements",
            "c",
            "percent_error"
          ]
        }
      },
      "description": "Parameter c and solver accuracy for original HYBAS configuration under different voltages and activation modes."
    },
    {
      "file": "max_displacements.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "negative_strain_material": {
              "type": "string",
              "enum": [
                "Hard PZT (TRS100HD)",
                "Soft PZT (TRSHK1HD)",
                "PZN-4.5%PT single crystal"
              ]
            },
            "positive_strain_material": {
              "type": "string",
              "enum": [
                "Uni-axial PVDF",
                "Bi-axial PVDF"
              ]
            },
            "voltage": {
              "type": "number",
              "unit": "V"
            },
            "max_displacement": {
              "type": "number",
              "unit": "micrometers"
            }
          },
          "required": [
            "negative_strain_material",
            "positive_strain_material",
            "voltage",
            "max_displacement"
          ]
        }
      },
      "description": "Maximum displacement for all six material combinations at two voltages with both components active."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each of the two output files. For `c_values.json`, your computed c and percent error values are compared against the expected results derived from a reference implementation of the described algorithm. For `max_displacements.json`, your computed maximum displacements are compared against expected values for each material‑voltage combination. The final reward is a weighted combination of the scores from both artifacts. Simply reporting the paper’s published numbers is not sufficient; you must implement the iterative numerical solver to produce the results.
