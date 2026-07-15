# Attributing Strengthening Mechanisms in Al/n-TiB2 Metal Matrix Composites

## Problem background
This task investigates the strengthening mechanisms that govern the high compressive strength of a nanostructured Al 5083 metal matrix composite reinforced with nano‑TiB₂ particles. By quantifying the contributions from grain boundaries, Orowan looping, and geometrically necessary dislocations (GNDs) induced by thermal and elastic modulus mismatch, one can understand which factors dominate the material's performance. The goal is to compute these three individual strengthening contributions (in MPa) and their sum using the classical models and the provided microstructural parameters, and to assess how well the sum accounts for the experimentally measured yield strength.

## Approach
The strengthening can be decoupled into three additive mechanisms that are computed from the composite's microstructure and well‑established physical constants. The exact equations are as follows:

**Grain boundary strengthening (Hall‑Petch):**
Δσ_GB = k_HP / √d, where d is the grain size.

**Orowan strengthening (Redsten equation):**
First compute inter‑particle spacing L = √(2/3)·D_p·(√(π/(4f)) − 1).
Then σ_or = (0.4·M)/(π·√(1−ν)) · (G·b/L) · ln(√(2/3)·D_p/b).

**Geometrically necessary dislocations (GND) strengthening:**
Strain due to CTE mismatch: ε_CTE = Δα·ΔT.
Density of CTE‑mismatch dislocations: ρ_CTE = 12·f·ε_CTE/(b·D_p).
Density of elastic modulus mismatch dislocations: ρ_EM = 6·f·ε_CTE/(b·D_p).
Strengthening contribution: Δσ_GND = √3·η·G·b·√ρ_EM + √3·β·G·b·√ρ_CTE.

The three contributions are calculated independently and then summed to yield the total predicted strengthening.

## Reproduction target
Compute the following three contributions using the models described above and the explicit parameters listed in the workflow step: grain boundary strengthening, Orowan strengthening, and GND strengthening. Then calculate the sum of these three contributions. Output the four values (all in MPa) to a JSON file. The correctness of each contribution and the total sum will be verified by comparing them against values recomputed independently from the same formulas and constants.

## Assets
No external datasets, models, or pre‑trained files are required. All necessary physical constants and microstructural parameters are given in the workflow. A standard Python environment with built‑in `math` and `json` libraries is sufficient to perform the calculations.

## Workflow steps

### Step 1: Compute strengthening contributions and write to JSON
- Role: scored (load-bearing)
- Action: Compute grain boundary strengthening via Hall-Petch (k_HP/sqrt(d)), Orowan strengthening via the Redsten equation (inter-particle spacing L, orientation factor M, shear modulus G, Burgers vector b, Poisson’s ratio ν), and geometrically necessary dislocation (GND) strengthening from CTE and elastic modulus mismatch (ρ_CTE, ρ_EM, Δσ_GND). Use the following parameters: Al grain size d=74 nm, TiB₂ particle diameter D_p=38 nm, volume fraction f=0.03, Hall-Petch constant k_HP=0.09 MPa·m^(1/2), mean orientation factor M=3.06, shear modulus G=25.6 GPa, Burgers vector b=0.286 nm, Poisson’s ratio ν=0.33, CTE mismatch Δα=15×10⁻⁶ K⁻¹, ΔT=420 K, geometric constants η=0.5, β=0.7. Write the results (grain_boundary_strengthening, orowan_strengthening, gnd_strengthening, total_calculated, all in MPa) to a JSON file.
- Output file: `/app/outputs/strengthening_contributions.json`
- Format: json
- Contract: Object with keys: grain_boundary_strengthening (float, MPa), orowan_strengthening (float, MPa), gnd_strengthening (float, MPa), total_calculated (float, MPa).
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
- target_policy: reference_match
- description: The computed strengthening contributions from Hall-Petch, Orowan, and GND mechanisms, and their sum.
- schema:
  - `type`: object
  - `required`:
    - `grain_boundary_strengthening`: float, MPa
    - `orowan_strengthening`: float, MPa
    - `gnd_strengthening`: float, MPa
    - `total_calculated`: float, MPa

Notes: The checker independently recomputes each contribution using the same formulas and parameters, then compares the agent's values with a tolerance.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "grain_boundary_strengthening": "float, MPa",
          "orowan_strengthening": "float, MPa",
          "gnd_strengthening": "float, MPa",
          "total_calculated": "float, MPa"
        }
      },
      "description": "The computed strengthening contributions from Hall-Petch, Orowan, and GND mechanisms, and their sum."
    }
  ],
  "notes": "The checker independently recomputes each contribution using the same formulas and parameters, then compares the agent's values with a tolerance."
}
```

## How you are scored
A hidden verifier will independently recompute the three strengthening contributions and their sum using the same formulas and parameters. It will compare your submitted `grain_boundary_strengthening`, `orowan_strengthening`, `gnd_strengthening`, and `total_calculated` (all in MPa) to its own recomputed values. Each field is scored based on how close it is to the correct value, with the total sum carrying the largest weight. The final reward is a weighted combination of these accuracies. Producing the correct numbers by implementing the formulas accurately is essential; simply reporting arbitrary values will not earn high scores.
