# Modified Fermi Integral for Band Tails in Semiconductors

## Problem background
Narrow-gap ternary semiconductors such as HgCdTe are important for infrared detection. In these materials, disorder can introduce an exponential density-of-states tail below the conduction band edge. This tail strongly affects carrier statistics and can mask the conventional Burstein-Moss (band-filling) shift. The central quantity needed to assess these effects is the modified Fermi integral that extends the standard parabolic-band integral to include the exponential tail. The task is to compute this integral for a representative range of reduced Fermi energies and tail strengths.

## Approach
The conduction band density of states is taken to have a conventional √E form above a characteristic tail energy E_t, and an exponential tail below it. The tail part of the density of states is proportional to √E_t exp[(E−E_t)/(2E_t)], so that it matches the value and derivative at E_t. The electron concentration then leads to a modified Fermi integral (dimensionless form):

F_{1/2}^{tail}(η, ε_t) = (1/Γ(3/2)) [ ∫_{-∞}^{ε_t} (√ε_t exp((ε−ε_t)/(2ε_t)) / (1+exp(ε−η))) dε  +  ∫_{ε_t}^{∞} (√ε / (1+exp(ε−η))) dε ]

where η is the reduced Fermi energy (scaled by kT), ε_t = E_t/(kT) is the dimensionless tail strength parameter, and Γ is the gamma function. For ε_t=0 the tail-free limit recovers the standard Fermi-Dirac integral F_1/2(η). This expression is to be evaluated numerically for a grid of η and ε_t values.

## Reproduction target
Compute the modified Fermi integral F_{1/2}^{tail}(η, ε_t) for reduced Fermi energies η = -4, -3.5, …, 4 (step 0.5) and for tail parameters ε_t = 0, 1, 10. Additionally compute the specific cases (η=0, ε_t=0) and (η=0, ε_t=10). Output all computed values as a single JSON file (see output contract). The hidden verifier will check whether the computed integral values exhibit the physically expected relationships among different η and ε_t.

## Assets
No external datasets, models, or proprietary tools are required. The reproduction uses standard Python scientific computing packages (e.g., NumPy, SciPy). Install them via pip if needed.

## Workflow steps

### Step 1: Compute modified Fermi integral
- Role: scored (load-bearing)
- Action: Implement the modified Fermi integral F_1/2^tail(η, ε_t) as defined in the instruction. Compute its value for reduced Fermi energy η from -4 to 4 in steps of 0.5 and for tail parameters ε_t = 0, 1, 10. Additionally compute the specific cases η=0, ε_t=0 and η=0, ε_t=10. Output all computed values as a JSON array.
- Output file: `/app/outputs/fermi_integral_values.json`
- Format: json
- Contract: A JSON array of objects, each with keys 'eta' (number), 'epsilon_t' (number), 'F' (number). Must contain all grid points (η from -4 to 4 step 0.5, ε_t=0,1,10) and the two specified cases.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fermi_integral_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fermi_integral_values.json
- path: `/app/outputs/fermi_integral_values.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed values of the modified Fermi integral. The checker verifies structural properties: approximate values at specific (η,ε_t) points, monotonic trends, and order-of-magnitude ratio between tail-free and large-tail cases.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `eta`, `epsilon_t`, `F`
    - `properties`:
      - `eta`:
        - `type`: number
      - `epsilon_t`:
        - `type`: number
      - `F`:
        - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fermi_integral_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "eta",
            "epsilon_t",
            "F"
          ],
          "properties": {
            "eta": {
              "type": "number"
            },
            "epsilon_t": {
              "type": "number"
            },
            "F": {
              "type": "number"
            }
          }
        }
      },
      "description": "Computed values of the modified Fermi integral. The checker verifies structural properties: approximate values at specific (η,ε_t) points, monotonic trends, and order-of-magnitude ratio between tail-free and large-tail cases."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted JSON file and checks that the computed integral values satisfy the expected physical trends: for any fixed ε_t the integral increases monotonically with η, for any fixed η the integral increases monotonically with ε_t, and the ratio between the large-tail and no-tail cases at a key η is consistent with the order-of-magnitude behaviour implied by the tail model. Reporting the correct structural trends and approximate magnitudes (hidden tolerances) yields full credit; a simple shape check that ignores the physics will not pass. Each part of the check contributes to the total reward.
