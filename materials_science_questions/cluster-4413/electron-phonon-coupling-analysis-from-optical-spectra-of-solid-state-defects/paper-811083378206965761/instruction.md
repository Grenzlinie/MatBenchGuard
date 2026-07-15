# Configuration-coordinate diagram construction and crossover activation barrier extraction for Pr³⁺-doped YAGG garnets

## Problem background
Praseodymium (Pr³⁺) exhibits broad 5d–4f luminescence in garnet hosts, but this luminescence is quenched at elevated temperatures by non-radiative processes. Two competing mechanisms are possible: thermally activated crossover from the excited 5d state to high-lying 4f² states, and thermal ionization to the conduction band. In Y₃Al₅₋ₓGaₓO₁₂:Pr³⁺, varying the Ga content x tunes the relative energies of the 5d₁, 4f²(³P₂), and conduction-band states, which is expected to change the dominant quenching mechanism. A central quantity for analysing this transition is the crossover activation barrier ΔE_{5d₁–CP} — the vertical energy difference between the bottom of the lowest 5d₁ parabola and its intersection point with the ³P₂ parabola, as obtained from harmonic configuration coordinate diagrams. Computing this barrier for the whole composition series (x = 0,1,2,3,4,5) tests the ability to construct the CC diagrams and extract the barrier that predicts thermal quenching via crossover.

## Approach
The configuration coordinate model describes the 5d₁ and ³P₂ states as harmonic potential curves (parabolas) with equal force constants. The displacement of the 5d₁ parabola from the 4f ground state is characterised by the Huang–Rhys parameter S and the dominant phonon energy ℏω; together they define the phonon relaxation energy Sℏω = (Stokes shift)/2. The zero-phonon line energy for the 5d₁ ↔ 4f transition is E_zpl = E_{5d₁Ex} − SS/2. For each Ga composition, two parabolas are constructed:
- E_{5d₁}(x) = E_zpl + Sℏω·(x/a − 1)²  (minimum at x = a)
- E_{³P₂}(x) = E_{³P₂Ex} + Sℏω·(x/a)²
where x is the configuration coordinate and a is the horizontal offset. The crossing point x_c is found as the smallest x > a where the curves intersect. The vertical activation barrier is then ΔE = E_{5d₁}(x_c) − E_{5d₁}(a). Numerical root‑finding (e.g., solving E_{5d₁}(x) = E_{³P₂}(x) for x > a) yields the barrier for each composition. The required spectroscopic parameters (E_{5d₁Ex}, E_{5d₁Em}, SS, and E_{³P₂Ex}) are provided in the workflow step; S = 5.5 and ℏω = 196 cm⁻¹ are fixed constants.

## Reproduction target
Using the harmonic configuration coordinate model described above and the input parameters for each Ga content (x = 0,1,2,3,4,5), compute the vertical activation barrier ΔE_{5d₁–CP} (in cm⁻¹) for every composition. Report all six values in a single JSON file `step_01_deltaE_CP.json` with keys x0 through x5.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute crossover activation barriers from configuration coordinate model
- Role: scored
- Action: The input spectroscopic parameters for each Ga content x are listed below (taken from Table I and Supplemental Table S1 of the paper). Additional constants: S = 5.5, ℏω = 196 cm⁻¹.

  | x | E5d1Em (cm⁻¹) | E5d1Ex (cm⁻¹) | SS (cm⁻¹) | E³P₂Ex (cm⁻¹) |
  |---|----------------|----------------|-----------|-----------------|
  | 0 | 31646          | 34542          | 2896      | 21618           |
  | 1 | 32154          | 34843          | 2689      | 22186           |
  | 2 | 32600          | 35335          | 2735      | 22185           |
  | 3 | 32949          | 35747          | 2798      | 22181           |
  | 4 | 33195          | 35939          | 2744      | 22183           |
  | 5 | 33384          | 36331          | 2947      | 22295           |

  Using these values, construct the harmonic configuration coordinate parabolas for the 5d₁ and ³P₂ states with equal force constants. The parabola equations are:

  E_{5d₁}(x) = E_zpl + Sℏω (x/a − 1)²  
  E_{³P₂}(x) = E³P₂Ex + Sℏω (x/a)²

  where E_zpl = E5d1Ex − SS/2 and Sℏω = SS/2. Determine the lowest crossing point x_c > a by solving E_{5d₁}(x) = E_{³P₂}(x), then compute the vertical energy barrier ΔE_{5d1–CP} = E_{5d₁}(x_c) − E_{5d₁}(a) (in cm⁻¹) for each composition x=0..5. Report the six barrier values in JSON format.
- Output file: `/app/outputs/step_01_deltaE_CP.json`
- Format: json
- Contract: {"x0": <float (cm⁻¹)>, "x1": <float (cm⁻¹)>, "x2": <float (cm⁻¹)>, "x3": <float (cm⁻¹)>, "x4": <float (cm⁻¹)>, "x5": <float (cm⁻¹)>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_deltaE_CP.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_deltaE_CP.json
- path: `/app/outputs/step_01_deltaE_CP.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Crossover activation barriers ΔE_{5d1–CP} computed by constructing harmonic configuration coordinate parabolas with equal force constants and finding their crossing point. The checker recomputes the barriers from the same input parameters and scores based on absolute tolerance and monotonic trend.
- schema:
  - `type`: object
  - `required`:
    - `x0`: float
    - `x1`: float
    - `x2`: float
    - `x3`: float
    - `x4`: float
    - `x5`: float
  - `units`:
    - `x0..x5`: cm⁻¹

Notes: The checker will recompute the six barrier values using the provided harmonic model and compare each against the agent's report with a tolerance. The trend (monotonically increasing up to x=4) is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_deltaE_CP.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "x0": "float",
          "x1": "float",
          "x2": "float",
          "x3": "float",
          "x4": "float",
          "x5": "float"
        },
        "units": {
          "x0..x5": "cm⁻¹"
        }
      },
      "description": "Crossover activation barriers ΔE_{5d1–CP} computed by constructing harmonic configuration coordinate parabolas with equal force constants and finding their crossing point. The checker recomputes the barriers from the same input parameters and scores based on absolute tolerance and monotonic trend."
    }
  ],
  "notes": "The checker will recompute the six barrier values using the provided harmonic model and compare each against the agent's report with a tolerance. The trend (monotonically increasing up to x=4) is also verified."
}
```

## How you are scored
A hidden verifier will independently implement the same harmonic CC model, recompute the six ΔE_{5d₁–CP} values from the same input parameters, and compare them to your reported numbers using a tolerance. In addition, the verifier checks that the six barrier values obey a specific monotonic ordering among the Ga compositions that is expected from the model; you do not need to enforce this ordering yourself — the check is part of the automatic scoring. The final reward is a weighted combination of the per‑composition correctness and the structural trend check; reporting the paper’s numbers without performing the computation is not sufficient.
