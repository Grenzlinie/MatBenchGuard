# Grain boundary expansion detection via bicrystal diffraction intensity asymmetry

## Problem background
Large-angle grain boundaries can exhibit local changes in interplanar spacing (expansion or contraction), which influence material properties. Lamarre and Sass (LS) proposed that such dilations produce a separate 'grain-boundary relrod' in electron diffraction patterns — a distinct streak of intensity away from the main lattice reflection — that could be used to detect and quantify the dilation. However, when the boundary diffraction lies very close to strong lattice reflections, it is unclear whether the simple LS model applies; a more complete calculation that includes the coherent scattering from both the grain-boundary region and the two adjoining perfect-crystal halves may be necessary. This task examines the bicrystal diffraction problem for a model with a four-plane grain boundary. The goal is to compute the locally averaged diffracted intensity Ī(f) along the [002] direction for two cases — expansion and contraction — and to determine whether a separate relrod appears or only an asymmetric modification of the main lattice peak.

## Approach
The scattering geometry is a bicrystal: two half-cylinders of radius R, each containing N (002) planes of spacing d₀ = 1. A grain-boundary region of four planes (two dilation parameters ε₁, ε₂) separates them. The total scattered amplitude per unit grain-boundary area, Y, is a coherent sum over all planes, each weighted by a cylindrical geometry factor (to account for the finite half-cylinder shape) and a phase factor exp(i 2π kz·z). For the four-plane boundary, the sum splits into the left half-cylinder, the boundary planes with dilations, and the right half-cylinder. The intensity I = Y Y* oscillates rapidly as a function of the normalized coordinate f = kz / k(002) because of interference from the large number of planes. To reveal the gross behaviour, the fine oscillations are removed by local averaging over several subsidiary maxima, giving a smooth Ī(f). You will implement this model and compute Ī(f) for f from 0.9 to 1.1 with a step of 0.001, for two distinct parameter sets: (i) expansion — ε₁ = 0.1, ε₂ = 0.05; (ii) contraction — ε₁ = −0.1, ε₂ = −0.05. All calculations use N = 1000 planes per half-cylinder.

## Reproduction target
Produce a CSV file called intensity_curves.csv under /app/outputs with three columns: f (float, range 0.9 to 1.1 inclusive, step 0.001), I_bar_expansion (float), I_bar_contraction (float). The file must contain the locally averaged intensity curves for both the expansion and contraction cases calculated as described. The absolute units of Ī are arbitrary; only the relative shape matters.

## Assets

- Python: python
- NumPy: numpy

## Workflow steps

### Step 1: Compute locally averaged intensity curves
- Role: scored (load-bearing)
- Action: Implement the bicrystal scattering model using a four‑plane grain‑boundary geometry with N=1000 half‑cylinder (002) planes per lattice. Use the cylindrical geometry factor. For the expansion case set ε₁=0.1, ε₂=0.05; for the contraction case set ε₁=−0.1, ε₂=−0.05. Compute the scattered amplitude Y per unit grain‑boundary area, then I = YY*. Apply local averaging over subsidiary oscillations to obtain a smooth Ī(f). Evaluate f from 0.9 to 1.1 with a step of 0.001. Output a CSV with columns f, I_bar_expansion, I_bar_contraction.
- Output file: `/app/outputs/intensity_curves.csv`
- Format: csv
- Contract: Columns: f (float, range 0.9 to 1.1 inclusive, step 0.001), I_bar_expansion (float), I_bar_contraction (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/intensity_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### intensity_curves.csv
- path: `/app/outputs/intensity_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Locally averaged diffraction intensity curves along [002] for the expansion case (ε₁=0.1, ε₂=0.05) and contraction case (ε₁=−0.1, ε₂=−0.05), evaluated at f values from 0.9 to 1.1 with step 0.001.
- schema:
  - `type`: table
  - `required_columns`: `f`, `I_bar_expansion`, `I_bar_contraction`
  - `units`:
    - `f`: dimensionless
    - `I_bar_expansion`: arbitrary intensity units
    - `I_bar_contraction`: arbitrary intensity units

Notes: The checker will perform structural checks on the submitted curves without using a pre‑computed numeric reference: (1) maximum intensity for each curve at f=1 within one step, (2) monotonic increase as f approaches 1 from below and monotonic decrease above, (3) low‑f side average higher than high‑f side average for expansion, and opposite for contraction, (4) no local maximum in (0.9,0.999) other than at f=1. Passing all checks yields full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "intensity_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "I_bar_expansion",
          "I_bar_contraction"
        ],
        "units": {
          "f": "dimensionless",
          "I_bar_expansion": "arbitrary intensity units",
          "I_bar_contraction": "arbitrary intensity units"
        }
      },
      "description": "Locally averaged diffraction intensity curves along [002] for the expansion case (ε₁=0.1, ε₂=0.05) and contraction case (ε₁=−0.1, ε₂=−0.05), evaluated at f values from 0.9 to 1.1 with step 0.001."
    }
  ],
  "notes": "The checker will perform structural checks on the submitted curves without using a pre‑computed numeric reference: (1) maximum intensity for each curve at f=1 within one step, (2) monotonic increase as f approaches 1 from below and monotonic decrease above, (3) low‑f side average higher than high‑f side average for expansion, and opposite for contraction, (4) no local maximum in (0.9,0.999) other than at f=1. Passing all checks yields full credit."
}
```

## How you are scored
A hidden verifier will read your intensity_curves.csv and perform four structural checks that do not rely on matching any pre-specified numeric values. (1) For each curve, the maximum value of Ī must occur at f = 1 (within the f‑grid resolution). (2) Ī must increase monotonically as f approaches 1 from below and decrease monotonically as f moves above 1, with a small tolerance for numerical noise. (3) The expansion and contraction curves must show opposite intensity asymmetry around the main peak: one curve must have a higher average intensity on the low‑f side (f < 1) than on the high‑f side (f > 1), while the other curve shows the reverse. (4) No local maximum (i.e., no separate relrod) may appear in the f range (0.9, 0.999) other than the main peak at f = 1. If all four checks pass, you receive a reward of 1.0; otherwise the reward is 0.0.
