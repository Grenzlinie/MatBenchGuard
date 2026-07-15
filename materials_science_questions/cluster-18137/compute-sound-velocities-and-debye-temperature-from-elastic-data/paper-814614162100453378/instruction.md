# Compute dispersion curves for copper along principal directions using Born–Begbie noncentral force theory

## Problem background
Understanding the vibrational properties of crystals is essential for predicting their thermal and elastic behaviour. The dispersion relations—angular frequency ω as a function of wave vector k—describe the phonon spectrum. This task focuses on face-centred cubic copper (Cu). Using the Born–Begbie noncentral force theory with only nearest-neighbour interactions (α=β=0), you will compute the theoretical dispersion curves along the three high-symmetry directions: (100), (110), and (111). The results are obtained from the room-temperature elastic constants, density, and lattice parameter of copper, all of which are provided below. This computation reproduces a key prediction of the lattice-dynamical model and serves as a reference for comparison with other theoretical and experimental results.

## Approach
The Born–Begbie noncentral force model extends the central-force picture by including terms that depend on the relative orientations of ion pairs. When only nearest-neighbour interactions are retained, the three force constants are fully determined by the three independent elastic constants c11, c12, and c44. The secular equation can be solved in closed form along the principal symmetry directions, yielding explicit expressions for ω² as a function of the wave-vector magnitude k. For each direction and each polarisation (longitudinal L and transverse T1, T2), you will discretise k from 0 to the Brillouin‑zone boundary, evaluate the corresponding analytical formula, and compute the angular frequency ω. The task requires implementing these formulas and writing the resulting (k, ω) pairs to a CSV file. No external data or model training is needed—only a straightforward numerical evaluation of the given expressions and input constants.

## Reproduction target
You must compute the angular frequency ω (in 10¹³ rad/s) for longitudinal (L) and transverse (T1, T2) modes in copper along the (100), (110), and (111) directions using the Born–Begbie theory with nearest-neighbour interactions only (α=β=0). The required inputs are: c11 = 1.68×10¹² dynes/cm², c12 = 1.21×10¹² dynes/cm², c44 = 0.75×10¹² dynes/cm², density ρ = 8.96 g/cm³, lattice constant a = 3.61 Å. Define ε = c11 − c12 − 2c44. For each direction, sample at least 20 equally spaced k values from 0 to the Brillouin‑zone boundary (k_max = √2 π/a for (100), √5 π/a for (110), √(3/2) π/a for (111); express k in 1/Å). Evaluate the following formulas at each k value:

**100 direction**
- L mode: ω² = (8/(ρ a²)) sin²(a k/(2√2)) [c11]
- T1, T2 modes: ω² = (8/(ρ a²)) sin²(a k/(2√2)) [c44]

**110 direction**
- L mode: ω² = (8/(ρ a²)) sin²(a k/4) [2c11 − ε − (2c11 − c44 − ε) sin²(a k/4)]
- T1 mode: ω² = (8/(ρ a²)) sin²(a k/4) [ε + 2c44 − (c44 + ε) sin²(a k/4)]
- T2 mode: ω² = (8/(ρ a²)) sin²(a k/4) [2c44 − (2c44 − c11) sin²(a k/4)]

**111 direction**
- L mode: ω² = (2/(ρ a²)) (3c11 − 2ε) sin²(a k/√6)
- T1, T2 modes: ω² = (2/(ρ a²)) (3c44 + ε) sin²(a k/√6)

Take the positive square root to obtain ω. Write the results to `/app/outputs/dispersion_curves.csv` with columns: direction (string: 100, 110, 111), mode (string: L, T1, T2), k (float, 1/Å), frequency (float, 10¹³ rad/s). Each curve must contain at least 20 equally spaced k points.

**Note on the low-temperature Debye temperature expansion:** The paper's headline results also include the low-temperature Debye temperature expansion coefficient and the critical elastic-constant parameter σ. However, the computational derivation of the expansion coefficient depends on formulas and integrals detailed only in earlier publications not provided here and cannot be fully specified within this self-contained task. Consequently, this reproduction is scoped to the dispersion curves, which are the primary quantitative prediction that can be independently computed from the given formulas and constants. The critical σ can be directly evaluated as (c11−c12−2c44)/c44 from the provided elastic constants and is not included as a separate scored artifact.

## Assets

- Elastic constants, density, and lattice parameter of Cu

## Workflow steps

### Step 1: Compute dispersion curves for Cu (Born–Begbie, nearest‑neighbor)
- Role: scored (load-bearing)
- Action: Using the Born–Begbie noncentral force theory with only nearest‑neighbor interactions (α=β=0) and the provided elastic constants (c11, c12, c44), density ρ, and lattice constant a, compute the angular frequency ω (in 10¹³ rad/s) for longitudinal (L) and transverse (T1, T2) modes in the (100), (110), and (111) directions. For each direction, generate at least 20 equally spaced k values from 0 to the Brillouin‑zone boundary. Write the results to /app/outputs/dispersion_curves.csv with columns: direction, mode, k (in 1/Å), frequency.
- Output file: `/app/outputs/dispersion_curves.csv`
- Format: csv
- Contract: Columns: direction (str), mode (str), k (float), frequency (float). Each row represents one (direction, mode, k) point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_curves.csv
- path: `/app/outputs/dispersion_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact: the computed dispersion curves. The checker independently recomputes the expected frequencies at each k point from the known formulas and inputs, then scores the agent's frequencies by the recomputed RMS error, with full credit for excellent agreement.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `mode`, `k`, `frequency`
  - `units`:
    - `k`: 1/Å
    - `frequency`: 10^13 rad/s

Notes: The agent must ensure at least 20 equally spaced k points per curve, spanning from 0 to the appropriate Brillouin‑zone boundary for each direction. Frequencies must be reported in 10¹³ rad/s.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "mode",
          "k",
          "frequency"
        ],
        "units": {
          "k": "1/Å",
          "frequency": "10^13 rad/s"
        }
      },
      "description": "Scored artifact: the computed dispersion curves. The checker independently recomputes the expected frequencies at each k point from the known formulas and inputs, then scores the agent's frequencies by the recomputed RMS error, with full credit for excellent agreement."
    }
  ],
  "notes": "The agent must ensure at least 20 equally spaced k points per curve, spanning from 0 to the appropriate Brillouin‑zone boundary for each direction. Frequencies must be reported in 10¹³ rad/s."
}
```

## How you are scored
A hidden verifier will independently recompute the expected dispersion curves using the same formulas and input constants. It will read your CSV file, align the rows by (direction, mode, k), and compare your reported frequencies against its own recomputed values. The verifier computes an error metric (e.g. root-mean-square error) and converts it to a reward between 0 and 1: excellent agreement yields a high reward, while larger errors reduce the reward. Your final score is the weighted combination of this reward (the dispersion curves stage accounts for the full task). Reporting correct frequencies that match the known physics is essential; no further inputs are needed.
