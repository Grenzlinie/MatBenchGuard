# FEM Hc2(T) Curves and WHHM Indistinguishability in Disordered Superconductors

## Problem background
In disordered superconductors, weak-localization corrections are predicted to modify the temperature dependence of the upper critical field Hc2(T). The Fukuyama-Ebisawa-Maekawa (FEM) theory describes these effects through an equation that includes a field-induced delocalization term. For moderate levels of disorder, the resulting reduced-field curves h(t) can have a shape that closely resembles the standard Werthamer-Helfand-Hohenberg-Maki (WHHM) form, raising the question of whether localization effects may go unnoticed when experimental Hc2 data are fitted to the WHHM model alone. The task computes FEM and WHHM curves for representative metallic-glass parameters to quantify the level of similarity and to derive the field-gradient ratio and Tc suppression as functions of the disorder parameter εFτ.

## Approach
The FEM equation for the upper critical field in reduced units is derived from Eq. (1a) of the paper. Using the reduced temperature `t = T/T_{c0}` and reduced field `h = π e D_0 H_{c2} / (4 c T_{c0})`, the equation becomes:

```
ln(t / r) = ψ(1/2) - ψ(1/2 + (2/π^2) * (h/t) * A) + (√3/π^2) * (h/t) / (ε_Fτ)^2 * ψ'(1/2 + (2/π^2) * (h/t))
```

where ψ is the digamma function, ψ' its derivative, and

```
A = 1 - (3√3/(4π)) / (ε_Fτ)^2,
r = T_c / T_{c0} is the critical-temperature ratio given by:

ln(r) = - (3√3) / (8π (ε_Fτ)^2) { (1/g*)^2 + 2π [ 1/g - (μ*/g)^2 ln(Θ_D τ) ] }

with g = λ_{e-ph} - μ*, μ* = 0.13, μ = 0.5,
g*/g = [1 + μ ln(ε_F/Θ_D)] / [1 + μ ln(ε_Fτ)],
and the relaxation time τ is obtained from ε_Fτ via τ = (ε_Fτ)/ε_F, so Θ_D τ = Θ_D * ε_Fτ / ε_F.
```

For the disorder-free limit (ε_Fτ → ∞), the correction term vanishes and A = 1, r = 1, reducing to the WHHM Maki orbital curve:

```
ln(t) = ψ(1/2) - ψ(1/2 + (2/π^2) * h_{Maki} / t).
```

This defines a universal reference curve h_{Maki}(t). For a given ε_Fτ, the FEM curve h_FEM(t) is obtained by solving the full implicit equation for h at each t with the corresponding r computed from the above expression.

To obtain the WHHM best-fit curves, we fit each FEM dataset (t_i, h_FEM_i) to the scaled Maki form h_{WHHM}(t) = b * h_{Maki}(t) by minimizing the sum of squared residuals ∑_i (h_FEM_i - b * h_{Maki,i})^2. The best-fit scaling factor b is used to compute h_{WHHM}(t) = b * h_{Maki}(t). For ε_Fτ = ∞ (represented as 1e6), b = 1 exactly.

From these results we compute:
- The ratio α_H/α_{H=0} = b (since it directly gives the field-gradient ratio).
- The Tc suppression ΔT_c/T_{c0} = 1 - r.
- The maximum absolute relative difference between h_FEM and h_{WHHM_fit} over the temperature grid: max |h_FEM - h_{WHHM_fit}| / h_FEM.

## Reproduction target
Using the input parameters λ = 1, ΘD = 0.017 eV, εF = 5 eV, and disorder parameters εFτ ∈ {1e6 (representing ∞), 2.0, 1.5, 1.3, 1.0}, complete the following: numerically solve the FEM equation to generate reduced field h versus reduced temperature t (t = 0.1 to 1.0 in steps of 0.05) for each εFτ; fit each resulting FEM curve to the WHHM Maki form via least squares to obtain the corresponding h_WHHM(t); compute the field-gradient ratio αH/αH=0, the Tc suppression ΔTc/Tc0, and the maximum absolute relative difference between h_FEM and h_WHHM_fit over the temperature grid. Write the raw curves to h_vs_t.csv and the derived quantities to ratios.csv with the columns specified in the output contract.

## Assets

- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Generate reduced-field FEM curves and WHHM fits
- Role: scored (load-bearing)
- Action: Implement the FEM equation and WHHM Maki fitting as described in the Approach section. Using the representative metallic-glass parameters (λ ≈ 1, Θ_D ≈ 0.017 eV, ε_F ≈ 5 eV), compute the reduced field h for reduced temperature t from 0.1 to 1.0 in steps of 0.05, for each disorder parameter ε_Fτ from {∞ (use 1e6), 2.0, 1.5, 1.3, 1.0}. Perform least‑squares fitting of the FEM data to the scaled Maki form to obtain best‑fit reduced‑field values h_WHHM(t). Write all data to `/app/outputs/h_vs_t.csv`.
- Output file: `/app/outputs/h_vs_t.csv`
- Format: csv
- Contract: Columns: t (float, reduced temperature), epsilonFtau (float, disorder parameter; 1e6 represents ∞), h_FEM (float, FEM reduced field), h_WHHM_fit (float, best‑fit WHHM reduced field). One row per (t, ε_Fτ) combination; all ε_Fτ values are included in the same file.
- Scoring: scored by hidden verifier

### Step 2: Compute α_H/α_H=0 ratio, T_c suppression, and indistinguishability check
- Role: scored
- Action: From the FEM and WHHM data, compute the ratio α_H/α_{H=0} as the best‑fit scaling factor b (see Approach). Compute the reduced T_c suppression ΔT_c/T_{c0} = 1 - r using r from the FEM equation. For each ε_Fτ, compute the maximum absolute relative difference between h_FEM and h_WHHM_fit across the temperature grid. Write the results to `/app/outputs/ratios.csv`.
- Output file: `/app/outputs/ratios.csv`
- Format: csv
- Contract: Columns: epsilonFtau (float), alpha_H_over_alpha_0 (float), dTc_over_Tc0 (float), max_rel_diff_h_vs_WHHM_fit (float). One row per ε_Fτ value; ε_Fτ=∞ (1e6) produces the Maki limit with α_H/α_0 = 1 and zero suppression.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/h_vs_t.csv`
- `/app/outputs/ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### h_vs_t.csv
- path: `/app/outputs/h_vs_t.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: FEM computed reduced‑field curves and WHHM fits for a grid of reduced temperatures and disorder parameters.
- schema:
  - `type`: table
  - `required_columns`: `t`, `epsilonFtau`, `h_FEM`, `h_WHHM_fit`

### ratios.csv
- path: `/app/outputs/ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Derived ratios and Tc suppression verifying indistinguishability of FEM and WHHM curves for ε_Fτ > 1.5.
- schema:
  - `type`: table
  - `required_columns`: `epsilonFtau`, `alpha_H_over_alpha_0`, `dTc_over_Tc0`, `max_rel_diff_h_vs_WHHM_fit`

Notes: The experimental re‑analysis of Zr–Cu Hc2 data (Table I in the paper) is omitted because the raw Hc2(T) data from Ref. 11 are not publicly available in machine‑readable form. The task focuses on the reproducible numerical core: FEM Hc2 curves, WHHM fitting, and the derived parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "h_vs_t.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "epsilonFtau",
          "h_FEM",
          "h_WHHM_fit"
        ]
      },
      "description": "FEM computed reduced‑field curves and WHHM fits for a grid of reduced temperatures and disorder parameters."
    },
    {
      "file": "ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilonFtau",
          "alpha_H_over_alpha_0",
          "dTc_over_Tc0",
          "max_rel_diff_h_vs_WHHM_fit"
        ]
      },
      "description": "Derived ratios and Tc suppression verifying indistinguishability of FEM and WHHM curves for ε_Fτ > 1.5."
    }
  ],
  "notes": "The experimental re‑analysis of Zr–Cu Hc2 data (Table I in the paper) is omitted because the raw Hc2(T) data from Ref. 11 are not publicly available in machine‑readable form. The task focuses on the reproducible numerical core: FEM Hc2 curves, WHHM fitting, and the derived parameters."
}
```

## How you are scored
A hidden verifier independently recomputes the FEM curves and WHHM fits using the same input parameters, then compares your submitted h_vs_t.csv and ratios.csv. Each scored stage is weighted, and the final reward is the weighted sum of stage-level scores. The verifier also checks that the output files conform to the required column schema and that the derived quantities are self-consistent. Simply reporting numbers from the literature is not sufficient; the artifacts must be generated by executing the described workflow.
