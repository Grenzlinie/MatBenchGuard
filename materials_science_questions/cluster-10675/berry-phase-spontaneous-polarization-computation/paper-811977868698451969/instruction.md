# Spontaneous polarization computation from point-charge model

## Problem background
Ammonium fluoberyllate, (NH4)2BeF4, undergoes a ferroelectric phase transition at around 177 K. In the low-temperature ferroelectric phase, a spontaneous polarization appears along the crystallographic b-axis. The microscopic origin of this polarization has been attributed to distortions and possible ordering of the NH4+ and BeF4^2- tetrahedral ions. Here we investigate this by computing the dipole moments of each distinguishable ion type and the resultant net polarization using a point-charge model applied to the published crystal structures in both the high-temperature paraelectric phase (+80 °C) and the low-temperature ferroelectric phase (−140 °C).

## Approach
The computation employs a point-charge model for AB4^n± tetrahedral ions. For each ion (NH4+(I), NH4+(II), and BeF4^2-), the polar distortion vector δr is defined as the sum over the three crystallographic axes of the differences between the positions of the four surrounding B atoms and the central A atom. The dipole moment p (in Debye) is then calculated as p = ±1.2 n δr, where n is the formal charge magnitude (n=1 for NH4+, n=2 for BeF4^2-).

In the paraelectric phase, the unit cell contains one of each ion; in the ferroelectric phase, the unit cell doubles, giving two of each type (denoted α and α′). Using the provided lattice parameters and fractional atomic coordinates for both phases, the dipole moments and their components along the a, b, and c axes are computed. Finally, the spontaneous polarization P_s along the ferroelectric b-axis is obtained by summing the b-components of all dipole moments and dividing by the volume of the ferroelectric unit cell. The goal is a direct implementation of these equations with the given structural data.

## Reproduction target
Compute the per-ion dipole moments (total magnitude and components p_a, p_b, p_c in Debye) for each distinguishable ion in both the paraelectric and ferroelectric phases, and compute the net spontaneous polarization P_s along the b-axis (in μC/cm²). The input crystal structures are provided in the instruction. Output a single JSON file with the numeric results.

## Assets

- Crystal structure data of (NH4)2BeF4 at +80°C and -140°C: 10.1143/JPSJ.46.157

## Workflow steps

### Step 1: Compute dipole moments and spontaneous polarization
- Role: scored (load-bearing)
- Action: Implement the point-charge model for AB4^n± tetrahedral ions using the provided crystal structure coordinates. For each distinguishable ion (two types of NH4+ and BeF4^2-) in both paraelectric (+80°C) and ferroelectric (-140°C) phases, compute the polar distortion vector δr from the central atom and the four surrounding atoms (formula (1) of the point-charge model: δr = Σ(Σ(B^r_i - A_i))), convert to dipole moment p (in Debye) via p = ±1.2 n δr (formula (2)), and then calculate the net spontaneous polarization along the b-axis using the unit cell volume in the ferroelectric phase (formulas (3)-(4)). Output all per-ion dipole moments (total magnitude and a, b, c components) and the total Ps (in μC/cm²) to dipole_results.json.
- Output file: `/app/outputs/dipole_results.json`
- Format: json
- Contract: {"type": "object", "required": {"paraelectric": "array of objects with string ion_label, float total_dipole_D, float pa_D, float pb_D, float pc_D", "ferroelectric": "array of objects with string ion_label, float total_dipole_D, float pa_D, float pb_D, float pc_D", "total_Ps_muC_per_cm2": "float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_results.json
- path: `/app/outputs/dipole_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON containing per-ion dipole moments and total spontaneous polarization, recomputed by checker from the same crystal structure data.
- schema:
  - `type`: object
  - `required`:
    - `paraelectric`: array of objects with string ion_label, float total_dipole_D, float pa_D, float pb_D, float pc_D
    - `ferroelectric`: array of objects with string ion_label, float total_dipole_D, float pa_D, float pb_D, float pc_D
    - `total_Ps_muC_per_cm2`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "paraelectric": "array of objects with string ion_label, float total_dipole_D, float pa_D, float pb_D, float pc_D",
          "ferroelectric": "array of objects with string ion_label, float total_dipole_D, float pa_D, float pb_D, float pc_D",
          "total_Ps_muC_per_cm2": "float"
        }
      },
      "description": "JSON containing per-ion dipole moments and total spontaneous polarization, recomputed by checker from the same crystal structure data."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier re-implements the point-charge model using the same crystal structure data and compares your submitted dipole_results.json to the expected values. Each workflow stage’s artifact is scored independently and combined into a final reward. Accurate computation of the per-ion dipole components and the total spontaneous polarization is required; merely guessing or copying approximate published numbers without correctly executing the model will not yield a high score.
