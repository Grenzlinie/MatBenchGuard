# Critical microcrack density and effective moduli in percolation-based damage model

## Problem background
In many polycrystalline materials subjected to cyclic loading, a large fraction of the fatigue life is consumed by the accumulation of randomly distributed microcracks at grain or phase boundaries before a few major macrocracks form. Predicting when this microcrack-governed stage ends is important for safe design. This task deals with a percolation-based damage model: the microstructure is idealized as a lattice whose links correspond to intact boundaries, microcracks are missing links, and the percolation threshold yields a critical microcrack density beyond which conductivity percolation occurs — interpreted as the onset of macrocrack growth. Combining this threshold with a self-consistent effective-modulus model and a self-similar microcrack nucleation law enables the prediction of both the degraded elastic constants at the critical state and a power-law fatigue life relation.

## Approach
The work proceeds in three conceptual stages.

1. **Critical microcrack density via percolation.** Model a simple cubic lattice with coordination number z=6 and bond percolation threshold p_c^b=0.247. Each lattice link has length l, and a microcrack corresponds to a broken link. By counting broken links at the percolation threshold and assuming penny-shaped microcracks of radius a=l/2, derive the critical microcrack density ω_c (the number density of cracks times the cube of their radius).

2. **Effective elastic moduli at the critical density.** With ω_c known, use Budiansky and O'Connell's self-consistent model for a solid containing a random array of flat circular cracks. The undamaged Poisson's ratio is ν=0.37. First solve an implicit equation for the effective Poisson's ratio ν̄ as a function of ω, then compute the ratios Ē/E (effective vs. undamaged Young's modulus) and μ̄/μ (effective vs. undamaged shear modulus) at ω=ω_c.

3. **Fatigue lifetime constant.** Assume a self-similar microcrack nucleation process where the microcrack density increment per cycle follows a power law in the local shear strain range, with exponent χ. The paper's authors fitted the continuous-loading coefficient A_c=132.86 and χ=3.0 from experimental data. Using these constants and ω_c, compute C=ω_c/A_c, which gives the fatigue life N_f = C / Δε^3 for continuous cycling.

## Reproduction target
The task is to implement the three computational steps above and produce the following numerical results under `/app/outputs`:
- `critical_density.json`: the critical microcrack density ω_c for non‑overlapping penny‑shaped cracks on a simple cubic lattice.
- `effective_moduli.json`: at that ω_c, the ratios Ē/E and μ̄/μ, and the effective Poisson's ratio ν̄.
- `lifetime_constant.json`: the lifetime constant C = ω_c/A_c, using χ=3.0 and A_c=132.86.

All quantities are deterministic and derived from the specified parameters. No experimental data fitting is required; use the paper's reported fitted constants directly.

## Assets

- Python scientific computing environment (numpy, scipy): pip

## Workflow steps

### Step 1: Calculate critical microcrack density
- Role: scored
- Action: Compute the critical microcrack density ω_c for non‑overlapping penny‑shaped cracks in a simple cubic lattice. Use the lattice coordination number z = 6, bond percolation threshold p_c^b = 0.247, and the relationship that links ω_c to p_c^b and z derived from counting broken links at the percolation threshold.
- Output file: `/app/outputs/critical_density.json`
- Format: json
- Contract: {"omega_c": number}
- Scoring: scored by hidden verifier

### Step 2: Calculate effective elastic moduli at critical density
- Role: scored
- Action: Using the undamaged Poisson's ratio ν = 0.37 and the critical microcrack density ω_c obtained in the previous step, numerically solve the implicit Budiansky‑O'Connell self‑consistent relation between effective Poisson's ratio ν̄ and ω. Then compute the effective elastic modulus ratio Ē/E and shear modulus ratio μ̄/μ from the self‑consistent expressions that relate them to ν̄ and ω.
- Output file: `/app/outputs/effective_moduli.json`
- Format: json
- Contract: {"E_ratio": number, "mu_ratio": number, "nu_bar": number}
- Scoring: scored by hidden verifier

### Step 3: Compute fatigue lifetime constant C
- Role: scored
- Action: Using the material exponent χ = 3.0 and the continuous‑loading coefficient A_c = 132.86 reported by the paper's authors from their fitting, compute the lifetime constant C = ω_c / A_c, where ω_c is the critical microcrack density from the first step.
- Output file: `/app/outputs/lifetime_constant.json`
- Format: json
- Contract: {"C": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_density.json`
- `/app/outputs/effective_moduli.json`
- `/app/outputs/lifetime_constant.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_density.json
- path: `/app/outputs/critical_density.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed critical microcrack density ω_c for non‑overlapping penny‑shaped cracks in a simple cubic lattice.
- schema:
  - `type`: object
  - `required`:
    - `omega_c`: number

### effective_moduli.json
- path: `/app/outputs/effective_moduli.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Effective elastic modulus ratio Ē/E, shear modulus ratio μ̄/μ, and effective Poisson's ratio ν̄ at ω_c.
- schema:
  - `type`: object
  - `required`:
    - `E_ratio`: number
    - `mu_ratio`: number
    - `nu_bar`: number

### lifetime_constant.json
- path: `/app/outputs/lifetime_constant.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fatigue lifetime constant C = ω_c / A_c for continuous cycling.
- schema:
  - `type`: object
  - `required`:
    - `C`: number

Notes: The hidden checker compares the reported numeric values against the paper's reported gold values with appropriate absolute tolerances. The effective moduli computation requires solving an implicit equation; different numerical implementations may yield slightly different values, but the tolerances absorb that spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_density.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "omega_c": "number"
        }
      },
      "description": "Computed critical microcrack density ω_c for non‑overlapping penny‑shaped cracks in a simple cubic lattice."
    },
    {
      "file": "effective_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_ratio": "number",
          "mu_ratio": "number",
          "nu_bar": "number"
        }
      },
      "description": "Effective elastic modulus ratio Ē/E, shear modulus ratio μ̄/μ, and effective Poisson's ratio ν̄ at ω_c."
    },
    {
      "file": "lifetime_constant.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C": "number"
        }
      },
      "description": "Fatigue lifetime constant C = ω_c / A_c for continuous cycling."
    }
  ],
  "notes": "The hidden checker compares the reported numeric values against the paper's reported gold values with appropriate absolute tolerances. The effective moduli computation requires solving an implicit equation; different numerical implementations may yield slightly different values, but the tolerances absorb that spread."
}
```

## How you are scored
A hidden verifier inspects the three JSON artifacts you produce. For each artifact it compares the submitted value(s) against the expected (gold) value(s) with an appropriate allowed tolerance that accounts for minor numerical differences. Each of the three stages carries a fraction of the total reward. The three scores are combined into a single final reward using predetermined weights. You must actually perform the calculations and write the results to the specified files; simply reporting a number without genuine computation will not satisfy the verifier because the comparison tolerances are set tight enough that arbitrary guesses are unlikely to succeed, but wide enough that any correct implementation from the given parameters will pass.
