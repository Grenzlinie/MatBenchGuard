# Gaussian Chain Coil-to-Flower Binodal Determination

## Problem background
A flexible polymer chain pinned near a penetrable interface between two media can undergo a conformation transition from a random coil to a "flower" state with a stretched stem and a coiled crown. The interface is modeled as a Heaviside step potential u. For a Gaussian chain, an exact Landau free-energy functional NΦ[φ] is derived as a function of the order parameter φ (the fraction of segments in the favorable region), predicting a first-order coil-to-flower transition. The binodal line in the (u, grafting distance) plane describes the conditions where the two phases coexist. This task reproduces the binodal distance for a given chain length and potential strength by implementing the analytic expressions and locating the point of equal free-energy minima.

## Approach
The Landau free-energy functional NΦ[φ] for an ideal Gaussian chain of N segments, with one end fixed at distance z0 from a step potential of strength u, has exact piecewise analytic forms. Define a = z0/(2Rg) with Rg = sqrt(N/6) and U = u N. Then:

When z0 ≤ 0 (grafting in the favorable half-space):
- For φ = 1 (all segments in favorable region): NΦ = -ln[erf(-a)].
- For φ < 1: NΦ = ln(Nπ/2) + 1/2 ln(1-φ^2) + 2a^2/(1+φ) + U (1-φ)/2.

When z0 > 0 (grafting in the unfavorable half-space):
- For φ = -1 (all segments in unfavorable region): NΦ = -ln[erf(a)] + U.
- For φ > -1: NΦ = ln(Nπ/2) + 1/2 ln(1-φ^2) + 2a^2/(1-φ) + U (1-φ)/2.

The order parameter φ = 2(m/N) - 1, where m is the number of segments that reside in the zero-potential side.

For a given chain length N and potential u, the coil state is the global minimum at φ=-1, while the flower state corresponds to a second minimum at φ>0. The binodal distance z0* is the grafting distance such that NΦ(φ_coil) = NΦ(φ_flower).

## Reproduction target
For N=1000 and u=0.1, compute the Landau free energy NΦ[φ] on a dense grid of φ ∈ [-1,1]. For a range of grafting distances z0, locate the global minima, and numerically solve for the binodal distance z0* at which the two minima have equal depth (to within a small tolerance). Record the binodal distance and the corresponding minima details (φ and NΦ) in a JSON file binodal_result.json with the structure specified in the output contract.

## Assets

- Python with numpy and scipy: numpy, scipy

## Workflow steps

### Step 1: Compute Landau free energy and binodal distance
- Role: scored (load-bearing)
- Action: Implement the analytic Landau free energy NΦ[φ] for a Gaussian chain pinned at distance z0 near a step potential of strength u, using the exact piecewise expressions. For a dense grid of φ in [-1,1] and a range of grafting distances z0, evaluate NΦ[φ], locate the global minima corresponding to coil and flower states, and solve for the binodal distance z0* where the two minima have equal depth. Output the binodal distance and the two minima details.
- Output file: `/app/outputs/binodal_result.json`
- Format: json
- Contract: {"N": int, "u": float, "z0_star": float, "coil_minimum": {"phi": float, "NPhi": float}, "flower_minimum": {"phi": float, "NPhi": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binodal_result.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binodal_result.json
- path: `/app/outputs/binodal_result.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed binodal distance (z0_star) and the free-energy minima for the coil and flower states (φ and NΦ values) for a Gaussian chain with chain length N and segment potential u.
- schema:
  - `type`: object
  - `required`:
    - `N`: int
    - `u`: float
    - `z0_star`: float
    - `coil_minimum`:
      - `phi`: float
      - `NPhi`: float
    - `flower_minimum`:
      - `phi`: float
      - `NPhi`: float

Notes: The checker compares z0_star to the exact binodal distance from the paper's analytic solution with a relative tolerance of 1e-3. The minima values are cross-checked for internal consistency with the Landau function but carry lower weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binodal_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "N": "int",
          "u": "float",
          "z0_star": "float",
          "coil_minimum": {
            "phi": "float",
            "NPhi": "float"
          },
          "flower_minimum": {
            "phi": "float",
            "NPhi": "float"
          }
        }
      },
      "description": "Computed binodal distance (z0_star) and the free-energy minima for the coil and flower states (φ and NΦ values) for a Gaussian chain with chain length N and segment potential u."
    }
  ],
  "notes": "The checker compares z0_star to the exact binodal distance from the paper's analytic solution with a relative tolerance of 1e-3. The minima values are cross-checked for internal consistency with the Landau function but carry lower weight."
}
```

## How you are scored
The hidden verifier reads your binodal_result.json. It compares your reported z0_star against the exact binodal distance for the same parameters, computed from the analytic theory, with an appropriate tolerance. It also verifies that the coil minimum corresponds to φ=-1 and the flower minimum to φ>0, and that the two minima depths are approximately equal. The final score is a weighted combination of these checks. Simply reporting the paper's published numbers is insufficient; the verifier scores the actual computations.
