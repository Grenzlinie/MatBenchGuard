# Electrostatic whisker theory: nucleation, growth and length statistics computation

## Problem background
Metal whiskers are hairlike protrusions that grow spontaneously on metal surfaces, causing short circuits and reliability failures in electronics. Despite decades of research, a quantitative theory of whisker formation and growth has been elusive. This task is grounded in an electrostatic theory: surface imperfections (oxide, contamination, grain boundaries) create local electric fields, and a needle-shaped metal filament can gain electrostatic energy by polarizing in these fields. The balance between this electrostatic energy gain and the surface-energy cost determines whether a whisker nucleates, how fast it grows, and what statistical distribution of whisker lengths emerges. The goal is to compute the key theoretical predictions—nucleation barrier, critical length, incubation time, growth rate, and the peak of the length distribution—using the analytic formulas of the theory with representative physical parameters.

## Approach
We treat whisker nucleation as a field-induced process. The free energy of a metallic needle of length h and fixed diameter d0 in a uniform electric field is modeled as the sum of an electrostatic energy gain (proportional to the cube of the length divided by a logarithmic factor Λ that accounts for the needle's polarizability) and a surface-energy cost (proportional to h). By maximizing this free energy with respect to h, analytic expressions are obtained for the nucleation barrier W and the critical length h0.

Growth after nucleation is described by a deterministic driving force: the whisker length evolves proportionally to the negative gradient of the free energy, with a mobility b = D/(kT) where D is the surface diffusion coefficient. In the short-whisker regime (h ≪ L, with L a characteristic patch size of the surface charge) the growth is extremely slow and leads to an incubation time t0; once the whisker overgrows the patch size L, the growth rate becomes approximately constant, characterized by a time tL and a corresponding growth velocity dh/dt.

Finally, the electrostatic field in the intermediate-to-long whisker regime becomes random (due to uncorrelated charged patches), causing random blocking of growth. The probability density g(h) for whisker lengths is derived from the statistics of the squared potential ξ², resulting in an expression involving a logarithmic function of h/L with parameters β and γ. Numerically locating the maximum of g(h) yields the most probable length (relative to the patch size).

The task is to implement these analytic formulas using the given representative parameters, evaluate each quantity numerically, and output the results as a structured JSON file.

## Reproduction target
Using the representative parameters from the electrostatic theory:
- surface tension σ = 500 dyn/cm
- whisker diameter d0 = 1 nm
- surface electric field E0 = 10⁶ V/cm (1 MV/cm)
- patch size L = 3 μm
- diffusion coefficient D = 10⁻¹⁸ cm²/s
- temperature T = 300 K
- logarithmic factor Λ = 2
- distribution parameters β = 1, γ = 0.15
and treating the surrounding medium as vacuum (ε = 1),

compute the following quantities from the analytic expressions of the theory:
1. Nucleation barrier W (in eV).
2. Critical whisker length h0 (in nm).
3. Incubation time t0 (in seconds).
4. Characteristic growth time tL (in seconds) for the intermediate-length regime.
5. Growth rate (in Å/s) from the constant-velocity regime, computed as dh/dt = L / tL.
6. The position of the maximum of the whisker-length probability density g(h), expressed as the ratio h/L (dimensionless).

All values should be written to a JSON file with the keys: W_eV, h0_nm, t0_s, tL_s, growth_rate_Angstrom_per_s, distribution_peak_h_over_L.

## Assets

- Python standard library (math, json): python3

## Workflow steps

### Step 1: Compute whisker theory predictions
- Role: scored
- Action: Implement the electrostatic whisker theory using the paper's described analytic formulas. (1) Use the needle polarizability logarithmic factor Λ = 2 (typical range). (2) Compute the nucleation barrier W using the formula for the maximum of the free energy F(h) = - (h³ ε E0²) / (3Λ) + π d0 σ, where ε=1, surface tension σ = 500 dyn/cm, whisker diameter d0 = 1 nm, and electric field E0 = 10^6 V/cm. Convert W to electron volts. (3) Compute the critical whisker length h0 as the value that gives the maximum, using the same parameters. (4) Compute the incubation time t0 from the deterministic growth law in the short-whisker regime: t0 = (3Λ) / (b ε E0² h0), where the mobility b = D/(kT) and the diffusion coefficient D = 10^{-18} cm²/s, T=300 K. (5) Compute the characteristic growth time tL in the intermediate-length regime: tL = (3Λ) / (b ε E0² L) with patch size L = 3 μm, and then the growth rate dh/dt = L / tL (in Å/s). (6) Compute the whisker length probability density g(h) using the paper's expression g(h) = β (h/L) exp{ -γ [ (h/L) ln( ((1+√(1+(h/L)²))²) / (4√(1+(h/L)²)) ) ]² } with representative parameters β=1 and γ=0.15. Numerically find the value of h/L that maximizes this function over the positive domain, returning the position of the peak. Output all computed values as a JSON object with keys: W_eV (float, barrier in eV), h0_nm (float, critical length in nm), t0_s (float, incubation time in seconds), tL_s (float, characteristic time in seconds), growth_rate_Angstrom_per_s (float, growth rate in Å/s), distribution_peak_h_over_L (float, h/L at maximum probability).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: W_eV (number), h0_nm (number), t0_s (number), tL_s (number), growth_rate_Angstrom_per_s (number), distribution_peak_h_over_L (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed predictions from the electrostatic whisker nucleation and growth theory.
- schema:
  - `type`: object
  - `required`:
    - `W_eV`: number
    - `h0_nm`: number
    - `t0_s`: number
    - `tL_s`: number
    - `growth_rate_Angstrom_per_s`: number
    - `distribution_peak_h_over_L`: number
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: All values are computed from the stated input parameters; the checker independently recomputes the same formulas and compares each value within generous factor-based tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "W_eV": "number",
          "h0_nm": "number",
          "t0_s": "number",
          "tL_s": "number",
          "growth_rate_Angstrom_per_s": "number",
          "distribution_peak_h_over_L": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Computed predictions from the electrostatic whisker nucleation and growth theory."
    }
  ],
  "notes": "All values are computed from the stated input parameters; the checker independently recomputes the same formulas and compares each value within generous factor-based tolerances."
}
```

## How you are scored
Your submitted results are evaluated by a hidden verifier that independently implements the same analytic formulas using the same input parameters. For each of the six quantities in the output JSON, the verifier recomputes the reference value and compares your reported value against it. The comparison uses generous tolerances that account for legitimate numerical and implementation differences (e.g., handling of the logarithmic factor, convergence of the numerical maximization of g(h)). Each quantity that falls within its tolerance contributes to the total reward; the final reward is the fraction of quantities that pass. Simply copying a known paper value is not sufficient—the scoring is based on a direct recompute from the public formulas and parameters. The verifier also checks that the output file is present, valid JSON, and contains all required keys before scoring.
