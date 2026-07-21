# Compute interchain-to-intrachain exchange ratio for TMMC

## Problem background
TMMC ((CH₃)₄NMnCl₃) is a quasi-one-dimensional Heisenberg antiferromagnet. Specific heat measurements show a λ‑shaped peak in the magnetic contribution at a temperature of 0.850 K, interpreted as the onset of three‑dimensional (3D) magnetic ordering. Using this Néel temperature and the known intrachain exchange constant J = 6.6 K, the ratio η = J′/J of the interchain exchange J′ to the intrachain exchange J can be estimated from a Green’s function theory for a tetragonal antiferromagnet. The value of η quantifies how much weaker the interchain coupling is compared to the intrachain coupling and is the central quantity to be determined.

## Approach
Apply Oguchi's Green’s function approximation for a tetragonal Heisenberg antiferromagnet with spin S = 5/2, intrachain exchange J = 6.6 K, and a much smaller interchain exchange J′. In this theory the Néel temperature T_N = 0.85 K satisfies the integral equation

$$
\frac{4 S(S+1) J}{3 k_{\mathrm{B}} T_{N}} = \frac{1}{\pi^{3}} \iiint_{0}^{\pi} \frac{dx\,dy\,dz}{(1-\cos x) + \eta\,[(1-\cos y)+(1-\cos z)]},
$$

where η = J′/J. The approach is to implement the triple integral numerically and to solve this equation for η by root‑finding. Once η is found, the interchain constant is obtained as J′ = η·J.

## Reproduction target
Solve the Green's function integral equation for the interchain‑to‑intrachain exchange ratio η = J′/J of TMMC, using the parameters S = 5/2, J = 6.6 K, and T_N = 0.85 K. Compute the corresponding interchain exchange constant J′ = η·J (in Kelvin). Save both values in a JSON file exchange_ratio.json under /app/outputs with keys "eta" (unitless) and "J_prime" (unit: K).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute exchange constant ratio
- Role: scored (load-bearing)
- Action: Solve Oguchi's Green's function equation for a tetragonal Heisenberg antiferromagnet to determine the interchain-to-intrachain exchange ratio η = J′/J. Use the Néel temperature T_N = 0.85 K, intrachain exchange constant J = 6.6 K, and spin quantum number S = 5/2. Implement the triple integral numerically and find η that satisfies (4 S(S+1) J)/(3 k_B T_N) = (1/π³) ∭_0^π [1 / ((1−cos x) + η[(1−cos y)+(1−cos z)])] dx dy dz. Compute J′ = η·J. Save η and J′ to exchange_ratio.json.
- Output file: `/app/outputs/exchange_ratio.json`
- Format: json
- Contract: A JSON object with keys "eta" (float, unitless) and "J_prime" (float, unit: K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exchange_ratio.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exchange_ratio.json
- path: `/app/outputs/exchange_ratio.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The solved exchange ratio η and interchain constant J′ from Oguchi's Green's function theory. Checked against hidden gold using absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `eta`: float
    - `J_prime`: float
  - `units`:
    - `eta`: unitless
    - `J_prime`: K
  - `description`: Object containing the interchain-to-intrachain exchange ratio eta and the interchain exchange constant J_prime.

Notes: Only stage 2 of the paper is reproduced (theoretical exchange ratio calculation). Experimental specific heat data and peak extraction are excluded as they require wet‑lab measurements.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exchange_ratio.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "eta": "float",
          "J_prime": "float"
        },
        "units": {
          "eta": "unitless",
          "J_prime": "K"
        },
        "description": "Object containing the interchain-to-intrachain exchange ratio eta and the interchain exchange constant J_prime."
      },
      "description": "The solved exchange ratio η and interchain constant J′ from Oguchi's Green's function theory. Checked against hidden gold using absolute tolerance."
    }
  ],
  "notes": "Only stage 2 of the paper is reproduced (theoretical exchange ratio calculation). Experimental specific heat data and peak extraction are excluded as they require wet‑lab measurements."
}
```

## How you are scored
A hidden verifier independently checks each workflow stage's output artifact. For the scored step "Compute exchange constant ratio", the verifier reads your exchange_ratio.json, extracts the numerical values of η and J′, and compares them to hidden reference values derived from the paper’s reported exchange ratio. Full credit is awarded if your computed η falls within a narrow tolerance of the reference; larger deviations receive partial credit, with the reward decreasing linearly to zero as the error increases. The interchain constant J′ is checked in the same way. No other artifacts affect the score.
