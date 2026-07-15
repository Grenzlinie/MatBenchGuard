# Ni-based superconductor pairing symmetry overlap analysis

## Problem background
This task investigates a potential family of Ni-based high-temperature superconductors. The material La₂Ni₂Se₂O₃ contains [Ni₂Se₂O]²⁻ layers with an antiperovskite structure. In these compounds, the low-energy electronic physics is controlled by two e_g d-orbitals on each Ni site, and superconductivity is assumed to be mediated by short-range antiferromagnetic superexchange interactions. The key question is which pairing symmetry—extended s-wave or d-wave—is more favourable under different doping conditions. The Hu-Ding overlap principle predicts that the symmetry whose gap form factor has the larger average magnitude on the Fermi surface dominates. This task evaluates the competition by computing the average superconducting gap magnitudes for both symmetries on the Fermi surfaces of a tight-binding model at three doping levels.

## Approach
The approach is built around a minimal effective four-orbital tight-binding model H₀ that captures the two-dimensional electronic structure of a single Ni₂Se₂O layer. The basis consists of the e_g orbitals on two inequivalent Ni sites: Ni3 d_{x²−y²}, Ni3 d_{yz}, Ni4 d_{x²−y²}, and Ni4 d_{xz}. The model is specified by the following 4×4 matrix elements (in eV, k in units of 1/a where a is the in-plane lattice constant):

H₁₁ = ε₁ + 2 tₓₓ¹¹ cos(kₓ) + 2 tₓₓ¹¹ cos(kᵧ)
H₁₃ = 4 tₓᵧ¹³ cos(kₓ/2) cos(kᵧ/2)
H₂₂ = ε₂ + 2 tₓₓ²² cos(kᵧ) + 2 tₓₓₓₓ²² cos(2kᵧ) + 4 tₓₓᵧᵧ²² cos(kₓ) cos(kᵧ) + 4 tₓₓₓₓₓₓ²² cos(kₓ) cos(2kᵧ)
H₂₄ = −4 tₓᵧ²⁴ sin(kᵧ/2) sin(kₓ/2)
H₃₃(kₓ,kᵧ) = H₁₁(kᵧ,kₓ)
H₄₄(kₓ,kᵧ) = H₂₂(kᵧ,kₓ)

with parameters: ε₁ = 7.2218, ε₂ = 7.0804, tₓₓ¹¹ = −0.3995, tₓᵧ¹³ = −0.2014, tₓₓ²² = 0.1573, tₓᵧ²⁴ = −0.2705, tₓₓᵧᵧ²² = −0.0113, tₓₓₓₓ²² = 0.0656, tₓₓₓₓₓₓ²² = 0.0668, and tₓₓ¹¹ (the yy hopping in H₁₁) = −0.1264. All other elements are zero.

The Fermi surfaces are obtained by adjusting the chemical potential μ so that the total electron count per Ni (spin included) matches the target doping level. At half filling each Ni contributes 8 electrons; at 0.2 electron doping the count is 8.2, at 0.28 hole doping it is 7.72.

Superconducting gap functions are defined from the short-range AFM exchange with an overall scale Δ₀ = 0.03 eV. On each orbital the gap functions for the two pairing symmetries differ by an overall sign. For the d_{x²−y²} orbital on Ni3 the gap is ±Δ₀(cos kₓ + (1/3) cos kᵧ); for d_{yz} on Ni3 it is ±(1/3)Δ₀ cos kᵧ; for d_{x²−y²} on Ni4 it is ±Δ₀(cos kᵧ + (1/3) cos kₓ); for d_{xz} on Ni4 it is ±(1/3)Δ₀ cos kₓ. The '+' sign corresponds to extended s‑wave and the '−' sign to d‑wave. The average gap magnitude for each symmetry is the arithmetic mean of |Δ(k)| evaluated at all Fermi-surface k‑points (weighted equally). The ratio extended‑s average / d‑wave average is then computed at each doping level.

## Reproduction target
Implement the tight-binding model described above. For each doping level (0.2 electron doping, half filling, and 0.28 hole doping), determine the chemical potential that gives the correct electron count per Ni, generate a dense grid of k‑points covering the Brillouin zone, locate the Fermi surface points (|E(k) − μ| ≤ a small threshold), evaluate the extended‑s and d‑wave gap functions at every Fermi‑surface point, compute the average of |Δ(k)| for each symmetry, and report the three ratios (extended‑s average / d‑wave average) in the output JSON file. The result is the set of three ratios showing the competition between the two pairing symmetries at the three distinct doping conditions.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Tight-binding model and pairing symmetry overlap analysis
- Role: scored
- Action: Implement the 4-orbital tight-binding model H0 using the given hopping parameters that describe the two-dimensional electronic structure. For each of the three doping levels (0.2 electron doping, half filling, and 0.28 hole doping relative to half filling), determine the chemical potential that achieves the target electron count per Ni. Generate a sufficient k-point mesh, locate the Fermi surface k-points, and evaluate the extended s-wave and d-wave gap functions at every Fermi surface point using the explicit gap forms derived from short-range antiferromagnetic exchange. Compute the Fermi-surface-weighted average absolute gap magnitude for each pairing symmetry at every doping. Report the three ratios (extended s-wave average magnitude divided by d-wave average magnitude) in the output JSON.
- Output file: `/app/outputs/step_01_overlap_results.json`
- Format: json
- Contract: A JSON object with top-level keys 'electron_0.2', 'half_filling', 'hole_0.28'. Each key maps to an object with numeric fields 'extended_s' (average gap magnitude for extended s-wave), 'd_wave' (average gap magnitude for d-wave), and 'ratio' (extended_s / d_wave).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_overlap_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_overlap_results.json
- path: `/app/outputs/step_01_overlap_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The three doping-level overlap ratios computed from the tight-binding model and gap functions; the checker compares these ratios to hidden reference values.
- schema:
  - `type`: object
  - `required`: `electron_0.2`, `half_filling`, `hole_0.28`
  - `properties`:
    - `electron_0.2`:
      - `type`: object
      - `required`: `extended_s`, `d_wave`, `ratio`
      - `properties`:
        - `extended_s`:
          - `type`: number
        - `d_wave`:
          - `type`: number
        - `ratio`:
          - `type`: number
    - `half_filling`:
      - `type`: object
      - `required`: `extended_s`, `d_wave`, `ratio`
      - `properties`:
        - `extended_s`:
          - `type`: number
        - `d_wave`:
          - `type`: number
        - `ratio`:
          - `type`: number
    - `hole_0.28`:
      - `type`: object
      - `required`: `extended_s`, `d_wave`, `ratio`
      - `properties`:
        - `extended_s`:
          - `type`: number
        - `d_wave`:
          - `type`: number
        - `ratio`:
          - `type`: number

Notes: The solver must implement the H0 model, chemical potential adjustment, and Fermi surface sampling; the checker only validates the reported ratios against pre‑established thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_overlap_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "electron_0.2",
          "half_filling",
          "hole_0.28"
        ],
        "properties": {
          "electron_0.2": {
            "type": "object",
            "required": [
              "extended_s",
              "d_wave",
              "ratio"
            ],
            "properties": {
              "extended_s": {
                "type": "number"
              },
              "d_wave": {
                "type": "number"
              },
              "ratio": {
                "type": "number"
              }
            }
          },
          "half_filling": {
            "type": "object",
            "required": [
              "extended_s",
              "d_wave",
              "ratio"
            ],
            "properties": {
              "extended_s": {
                "type": "number"
              },
              "d_wave": {
                "type": "number"
              },
              "ratio": {
                "type": "number"
              }
            }
          },
          "hole_0.28": {
            "type": "object",
            "required": [
              "extended_s",
              "d_wave",
              "ratio"
            ],
            "properties": {
              "extended_s": {
                "type": "number"
              },
              "d_wave": {
                "type": "number"
              },
              "ratio": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "The three doping-level overlap ratios computed from the tight-binding model and gap functions; the checker compares these ratios to hidden reference values."
    }
  ],
  "notes": "The solver must implement the H0 model, chemical potential adjustment, and Fermi surface sampling; the checker only validates the reported ratios against pre‑established thresholds."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/step_01_overlap_results.json file. It extracts the three reported ratios and compares each to a reference value with an appropriate tolerance. For each doping level that falls within the tolerance you earn one point. The final score is the fraction of the three doping levels that pass, reported as a number between 0 and 1. The verifier does not inspect your code; only the submitted JSON file is evaluated.
