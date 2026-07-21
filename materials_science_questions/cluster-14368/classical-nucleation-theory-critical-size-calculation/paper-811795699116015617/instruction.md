# Adipic Acid Critical and Deliquescence Supersaturation Calculation

## Problem background
Cloud condensation nuclei (CCN) activity determines whether atmospheric aerosol particles grow into cloud droplets. For slightly soluble organic compounds such as adipic acid, two activation thresholds are relevant: the critical supersaturation ($S_c$) predicted by standard Köhler theory, and the deliquescence supersaturation ($S_{\mathrm{del}}$) arising from the Kelvin effect over a saturated solution droplet. The actual CCN activation of a dry particle may be controlled by whichever threshold is larger, and the relative magnitudes depend on particle size. This task computes both supersaturation curves as a function of dry particle diameter and determines the crossover diameter where they intersect, thereby delineating the size regimes where each threshold would dominate.

## Approach
Standard Köhler theory (combining the Kelvin curvature effect and the Raoult solution effect) is used to calculate the critical supersaturation of an aqueous adipic acid droplet. The surface tension of the droplet depends on the **concentration of dissolved carbon (moles of carbon per kg of water)** and is modeled by the Szyszkowski–Langmuir equation with published parameters. The deliquescence supersaturation is obtained from the Kelvin equation for a saturated solution, using a fixed water activity and two limiting surface tension values (0.060 and 0.072 J/m²) that bracket the expected concentration-dependent range. The two curves are evaluated over dry particle diameters from 50 nm to 300 nm. The crossover diameter is the size at which the deliquescence curve (using the midpoint surface tension 0.066 J/m²) equals the Köhler critical supersaturation. **All required physical constants, material properties, and model coefficients are given below in explicit numerical form. You must use exactly these values because the hidden checker uses them to recompute the reference curves.**

## Constants and model parameters
The checker uses the following exact numerical values. To obtain full credit your implementation must use these same numbers.

### Physical constants
- Universal gas constant: **R = 8.314** J/(mol·K)
- Molar mass of water: **M_w = 0.018** kg/mol
- Density of water: **ρ_w = 1000.0** kg/m³
- Surface tension of pure water: **σ_w = 0.072** J/m²
- Temperature: **T = 298.15** K

### Adipic acid material properties
- Molar mass of adipic acid: **M_aa = 0.14614** kg/mol (equivalent to 146.14 g/mol)
- Density of adipic acid: **ρ_aa = 1360.0** kg/m³ (equivalent to 1.36 g/cm³)
- Szyszkowski–Langmuir parameters fitted to surface tension data: **a = 0.0106**, **b = 11.836**

### Model assumptions
- The aqueous droplet is treated as an ideal solution: the water activity coefficient **γ_w = 1**.
- Adipic acid does not dissociate; the van’t Hoff factor is **1**.
- The concentration of dissolved carbon is calculated as **C = (6 × n_aa) / m_water** where n_aa is the moles of adipic acid and m_water is the mass of water (kg). (Adipic acid has 6 carbon atoms.)
- The droplet surface tension is obtained from the Szyszkowski–Langmuir relation:

  **σ(C) = σ_w − a·T·ln(1 + b·C)**.

  If this expression gives a negative value, clamp it to 0.0.

### Deliquescence parameters
- Water activity for deliquescence: **γ_w_del = 0.990**
- Lower bound surface tension: **σ_del_low = 0.060 J/m²**
- Upper bound surface tension: **σ_del_high = 0.072 J/m²**
- Midpoint surface tension for crossover: **σ_del_mid = 0.066 J/m²**

## Reproduction target
Produce arrays of dry particle diameters (50–300 nm), the corresponding critical supersaturation percentages ($S_c$), and the deliquescence supersaturation percentages for the lower and upper surface tension bounds ($S_{\mathrm{del}}$). The deliquescence calculation uses a water activity **γ_w = 0.990**. Additionally, determine the dry diameter at which the deliquescence curve (evaluated with **σ = 0.066 J/m²**) crosses the Köhler critical supersaturation curve. Output the computed quantities as a single JSON file with the fields `dry_diameters_nm`, `Sc_kohler_pct`, `Sdel_lower_pct`, `Sdel_upper_pct`, `gamma_w`, and `crossover_diameter_nm`. **The `gamma_w` field must hold the value 0.990.**

## Assets

- The numerical constants listed above are self‑contained in this instruction; no external download is needed.

## Workflow steps

### Step 1: Compute adipic acid Köhler and deliquescence supersaturation curves
- Role: scored (load-bearing)
- Action: Implement standard Köhler theory (Kelvin effect + Raoult effect) with the concentration-dependent surface tension from the Szyszkowski–Langmuir model (a=0.0106, b=11.836) to compute the critical supersaturation $S_c$ as a function of dry particle diameter. Implement the deliquescence relation (Kelvin equation for a saturated droplet) with water activity $\gamma_w=0.990$ and two surface tension limits (0.060 and 0.072 J/m²) to compute $S_{\mathrm{del}}$. Evaluate both curves for dry diameters from 50 nm to 300 nm. Determine the crossover diameter where $S_{\mathrm{del}}$ (using $\sigma=0.066$ J/m²) equals $S_c$. All constants must be taken from the table above.
- Output file: `/app/outputs/step_01_sc_sdel.json`
- Format: json
- Contract: {"dry_diameters_nm": [float], "Sc_kohler_pct": [float], "Sdel_lower_pct": [float], "Sdel_upper_pct": [float], "gamma_w": 0.990, "crossover_diameter_nm": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_sc_sdel.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_sc_sdel.json
- path: `/app/outputs/step_01_sc_sdel.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The checker independently recomputes the same curves using the same public theory and constants, then compares the submitted arrays elementwise with a tolerance and verifies the crossover diameter.
- schema:
  - `type`: object
  - `required`:
    - `dry_diameters_nm`: array of float, nm
    - `Sc_kohler_pct`: array of float, %
    - `Sdel_lower_pct`: array of float, %
    - `Sdel_upper_pct`: array of float, %
    - `gamma_w`: float, must be exactly 0.990
    - `crossover_diameter_nm`: float, nm

Notes: All physical constants and model parameters are explicitly listed in this instruction. The checker recomputes its own reference using those identical numbers, so no external gold file is needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_sc_sdel.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "dry_diameters_nm": "array of float, nm",
          "Sc_kohler_pct": "array of float, %",
          "Sdel_lower_pct": "array of float, %",
          "Sdel_upper_pct": "array of float, %",
          "gamma_w": "float (must be 0.990)",
          "crossover_diameter_nm": "float, nm"
        }
      },
      "description": "The checker independently recomputes the same curves using the same public theory and constants, then compares the submitted arrays elementwise with a tolerance and verifies the crossover diameter."
    }
  ],
  "notes": "All physical constants and model parameters are explicitly listed in the instruction. The checker recomputes its own reference from identical equations and parameters, so no external gold file is needed."
}
```

## How you are scored
A hidden verifier independently re-computes the Köhler and deliquescence curves using the same publicly known equations and constants that are available to you. It compares your submitted arrays elementwise against its own recomputed reference, and checks the crossover diameter. The reward is based on agreement with that reference: better agreement yields higher credit. Reporting the paper's numbers without producing correct computed arrays will not match the recomputed reference and will receive low reward.