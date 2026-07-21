# Site percolation threshold of spin-1/2 and spin-1 Ising models via effective-field theory

## Problem background
Site dilution in magnetic systems, where a fraction of magnetic atoms are replaced by non-magnetic impurities, influences the existence of long-range ferromagnetic order. A key quantity is the site percolation threshold c*, the minimum concentration of magnetic atoms needed for the system to sustain order at zero temperature. Accurate theoretical estimates of c* require accounting for multi-site spin correlations beyond simple mean-field or single-site decoupling approximations. This task reproduces the critical site concentration for three cases: spin-1/2 Ising model on honeycomb and square lattices, and spin-1 Blume-Capel model on honeycomb lattice at zero crystal field and zero transverse field.

## Approach
The method constructs a finite cluster of a central spin and its q nearest neighbors, then writes the exact thermal averages using differential-operator techniques without decoupling higher-order correlation functions. The resulting linear systems relate site correlation functions and involve coefficient functions that depend on temperature, coordination number, and an effective field parameter. By solving a self-consistency condition on the magnetizations of central and perimeter sites in the limit of vanishing effective field, the critical temperature Tc as a function of magnetic site concentration c is obtained. Scanning over c, the percolation threshold c* is determined as the concentration at which Tc drops to zero.

## Reproduction target
Produce a JSON file 'percolation_thresholds.json' containing the three computed critical site concentrations c* for the following cases: spin-1/2 Ising model on a honeycomb lattice (coordination q=3), spin-1/2 Ising model on a square lattice (q=4), and spin-1 Blume-Capel model on a honeycomb lattice (q=3) with crystal field D/J=0 and transverse field Ω/J=0. The intermediate Tc(c) curves must be saved as CSV files, but only the final JSON is scored.

## Assets

- numpy: https://pypi.org/project/numpy
- scipy: https://pypi.org/project/scipy

## Equations

### Spin-1/2 honeycomb (q=3)
The differential-operator coefficients are:
K₁ = sinh(J∇) tanh(βx) |_{x=0}
K₂ = cosh(J∇) sinh(J∇) tanh(βx) |_{x=0}
K₃ = cosh²(J∇) sinh(J∇) tanh(βx) |_{x=0}
K₄ = sinh³(J∇) tanh(βx) |_{x=0}
A₁ = tanh(β(x+γ)) |_{x=0}
A₂ = cosh(J∇) tanh(β(x+γ)) |_{x=0}
A₃ = sinh(J∇) tanh(β(x+γ)) |_{x=0}
where γ = (q−1)A is the effective field.  Use e^{α∇}f(x)=f(x+α) to evaluate, e.g. sinh(J∇)tanh(βx)|_{x=0} = ½[tanh(βJ)−tanh(−βJ)].

The linear system (A2):
x₁ = (3c−6c²+3c³)x₄K₁ + (6c²−6c³)x₄K₂ + 3c³x₄K₃ + c x₆K₄
x₂ = (3c²−6c³+3c⁴)K₁ + (6c³−6c⁴)K₂ + 3c⁴K₃ + c²x₅K₄
x₃ = (−3c²+3c³)x₄K₁ + (6c²−6c³)x₄K₂ + 3c³x₄K₃ + c³x₄K₄
x₄ = (c−c²)A₁ + c²A₂ + c x₁A₃
x₅ = c x₂A₃
x₆ = c x₃A₃
Critical condition: x₁ = x₄ in the limit γ→0 (A→0).

### Spin-1/2 square (q=4)
Coefficients:
L₁ = sinh(J∇)tanh(βx)|_{x=0}   L₂ = cosh(J∇)sinh(J∇)tanh(βx)|_{x=0}
L₃ = cosh²(J∇)sinh(J∇)tanh(βx)|_{x=0}   L₄ = cosh³(J∇)sinh(J∇)tanh(βx)|_{x=0}
L₅ = sinh³(J∇)tanh(βx)|_{x=0}   L₆ = cosh(J∇)sinh³(J∇)tanh(βx)|_{x=0}
B₁ = tanh(β(x+γ))|_{x=0}   B₂ = cosh(J∇)tanh(β(x+γ))|_{x=0}   B₃ = sinh(J∇)tanh(β(x+γ))|_{x=0}
Linear system (A4):
x₁ = (4c−12c²+12c³−4c⁴)x₅L₁ + (12c²−24c³+12c⁴)x₅L₂ + (12c³−12c⁴)x₅L₃ + 4c⁴x₅L₄ + (4c−4c²)x₇L₅ + 4c²x₇L₆
x₂ = (4c²−12c³+12c⁴−4c⁵)L₁ + (12c³−24c⁴+12c⁵)L₂ + (12c⁴−12c⁵)L₃ + 4c⁵L₄ + (4c²−4c³)x₆L₅ + 4c³x₆L₆
x₃ = (−8c²+12c³−4c⁴)x₅L₁ + (12c²−24c³+12c⁴)x₅L₂ + (12c³−12c⁴)x₅L₃ + 4c⁴x₅L₄ + (4c³−4c⁴)x₅L₅ + 4c⁴x₅L₆
x₄ = (4c²−4c³)x₆L₁ + (−12c²+12c³)x₆L₂ + (12c²−12c³)x₆L₃ + 4c³x₆L₄ + (4c²−4c³)x₆L₅ + 4c³x₆L₆
x₅ = (c−c²)B₁ + c²B₂ + c x₁B₃
x₆ = (c−c²)x₅B₁ + c²x₅B₂ + c x₂B₃
x₇ = (c−c²)x₆B₁ + c²x₆B₂ + c x₃B₃
x₈ = (c−c²)x₇B₁ + c²x₇B₂ + c x₄B₃
Critical condition: x₁ = x₅ in the limit γ→0.

### Spin-1 Blume‑Capel honeycomb (q=3), D/J=0, Ω/J=0
Effective‑field functions:
F(x) = 2 sinh(βx) / (2 cosh(βx) + 1)
G(x) = 2 cosh(βx) / (2 cosh(βx) + 1)

Coefficients:
k₁ = sinh(J∇) F(x)|_{x=0}   k₂ = cosh(J∇) sinh(J∇) F(x)|_{x=0}
k₃ = sinh³(J∇) F(x)|_{x=0}   k₄ = cosh²(J∇) sinh(J∇) F(x)|_{x=0}
r₀ = G(0)   r₁ = cosh(J∇) G(x)|_{x=0}   r₂ = sinh²(J∇) G(x)|_{x=0}
r₃ = cosh²(J∇) G(x)|_{x=0}   r₄ = cosh(J∇) sinh²(J∇) G(x)|_{x=0}   r₅ = cosh³(J∇) G(x)|_{x=0}
a₁ = F(γ)   a₂ = sinh(J∇)F(x+γ)|_{x=0}   a₃ = cosh(J∇)F(x+γ)|_{x=0}
b₁ = G(γ)   b₂ = sinh(J∇)G(x+γ)|_{x=0}   b₃ = cosh(J∇)G(x+γ)|_{x=0}
γ = 2A (q−1 = 2)

Linear system (B2) – 21 equations:
x₁ = 3c x₄ k₁ + c x₆ k₃ + (−6k₁+6k₂)c x₈ + (3k₁−6k₂+3k₄)c x₁₄
x₂ = 3c k₁ x₇ + (−6k₁+6k₂)c x₉ + c k₃ x₁₃ + (3k₁−6k₂+3k₄)c x₁₅
x₃ = (−3k₁+6k₂)c x₈ + (3k₁−6k₂+k₃+3k₄)c x₁₄
x₄ = a₁c + a₂c x₁ + (a₃−a₁)c x₁₆
x₅ = a₁c x₄ + a₂c x₂ + (a₃−a₁)c x₁₇
x₆ = a₁c x₅ + a₂c x₃ + (a₃−a₁)c x₁₉
x₇ = b₁c + b₂c x₁ + (b₃−b₁)c x₁₆
x₈ = b₁c x₄ + b₂c x₂ + (b₃−b₁)c x₁₇
x₉ = b₁c x₇ + b₂c x₁₀ + (b₃−b₁)c x₁₈
x₁₀ = b₂c x₁₆ + b₃c x₁
x₁₁ = b₂c x₁₇ + b₃c x₂
x₁₂ = b₂c x₁₈ + b₃c x₁₀
x₁₃ = b₁c x₅ + b₂c x₃ + (b₃−b₁)c x₁₉
x₁₄ = b₁c x₈ + b₂c x₁₁ + (b₃−b₁)c x₂₀
x₁₅ = b₁c x₉ + b₂c x₁₂ + (b₃−b₁)c x₂₁
x₁₆ = c r₀ + 3c r₂ x₅ + (−3r₀+3r₁)c x₇ + (3r₀−6r₁+3r₃)c x₉ + (−3r₂+3r₄)c x₁₃ + (−r₀+3r₁−3r₃+r₅)c x₁₅
x₁₇ = (−2r₀+3r₁)c x₄ + (3r₀+3r₂+3r₃−6r₁)c x₈ + (−r₀+3r₁−3r₂−3r₃+3r₄+r₅)c x₁₄
x₁₈ = (−2r₀+3r₁)c x₇ + (3r₀−6r₁+3r₂+3r₃)c x₉ + (−r₀+3r₁−3r₂−3r₃+3r₄+r₅)c x₁₅
x₁₉ = (r₀−3r₁+3r₂+3r₃)c x₅ + (−r₀+3r₁−3r₂−3r₃+3r₄+r₅)c x₁₃
x₂₀ = (r₀−3r₁+3r₂+3r₃)c x₈ + (−r₀+3r₁−3r₂−3r₃+3r₄+r₅)c x₁₄
x₂₁ = (r₀−3r₁+3r₂+3r₃)c x₉ + (−r₀+3r₁−3r₂−3r₃+3r₄+r₅)c x₁₅
Critical condition: x₁ = x₄ in the limit γ→0 (A→0).

All coefficients can be evaluated numerically by applying the shift identity e^{α∇}f(x)=f(x+α) to the base functions tanh(βx), F(x), G(x).

## Workflow steps

### Step 1: Evaluate differential-operator coefficients
- Role: process
- Action: Implement the differential-operator coefficients (K1-K4, A1-A3, L1-L6, B1-B3, k1-k4, a1-a3, b1-b3, r0-r5) and the linear systems (A2, A4, B2) as defined in the Equations section. Use the shift identity e^{α∇}f(x)=f(x+α) to evaluate the coefficients numerically.
- Evidence: none

### Step 2: Compute Tc(c) curves
- Role: process
- Action: For the three cases (spin-1/2 on honeycomb q=3, spin-1/2 on square q=4, spin-1 on honeycomb q=3 at D/J=0, Ω/J=0), construct the linear systems of site correlation functions derived from the restricted-decoupling effective-field approximation. For each site concentration c in a suitable range, solve the self-consistency condition (x1=x4 for q=3, x1=x5 for q=4) in the limit of vanishing effective field to obtain the critical temperature Tc(c). Save the resulting (c, Tc/J) pairs as CSV files: 'tc_vs_c_spin_half_q3.csv', 'tc_vs_c_spin_half_q4.csv', 'tc_vs_c_spin1_q3.csv'.
- Evidence: `/app/outputs/tc_vs_c_spin_half_q3.csv,tc_vs_c_spin_half_q4.csv,tc_vs_c_spin1_q3.csv`

### Step 3: Extract percolation thresholds c*
- Role: scored (load-bearing)
- Action: From the Tc(c) curves produced in step_02, locate the site concentration c* where Tc extrapolates to zero for each case. Compute the three values: c_star_spin_half_q3, c_star_spin_half_q4, c_star_spin1_q3. Write a JSON file percolation_thresholds.json containing these values.
- Output file: `/app/outputs/percolation_thresholds.json`
- Format: json
- Contract: {"c_star_spin_half_q3": <float>, "c_star_spin_half_q4": <float>, "c_star_spin1_q3": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/percolation_thresholds.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### percolation_thresholds.json
- path: `/app/outputs/percolation_thresholds.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the three computed critical site concentration values c* for spin-1/2 honeycomb (q=3), spin-1/2 square (q=4), and spin-1 honeycomb (q=3) at D/J=0, Ω/J=0.
- schema:
  - `type`: object
  - `required`:
    - `c_star_spin_half_q3`: number
    - `c_star_spin_half_q4`: number
    - `c_star_spin1_q3`: number

Notes: Only the percolation thresholds are scored. The intermediate Tc(c) CSV files are for evidence only and not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "percolation_thresholds.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "c_star_spin_half_q3": "number",
          "c_star_spin_half_q4": "number",
          "c_star_spin1_q3": "number"
        }
      },
      "description": "JSON file containing the three computed critical site concentration values c* for spin-1/2 honeycomb (q=3), spin-1/2 square (q=4), and spin-1 honeycomb (q=3) at D/J=0, Ω/J=0."
    }
  ],
  "notes": "Only the percolation thresholds are scored. The intermediate Tc(c) CSV files are for evidence only and not directly scored."
}
```

## How you are scored
A hidden verifier reads your 'percolation_thresholds.json'. It compares each c* value to the corresponding hidden reference value (the paper-reported result) within an absolute tolerance. If all three values fall within tolerance, you receive full credit. Partial credit is awarded proportionally. The intermediate Tc(c) CSV files are not scored but their production is required to obtain the final result.
