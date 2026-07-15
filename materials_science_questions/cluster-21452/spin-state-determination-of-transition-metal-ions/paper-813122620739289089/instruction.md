# Probabilistic Spin-Canting Model in Zn-Diluted Ferrite Nanoparticles

## Problem background
In spinel ferrite nanoparticles such as cobalt–zinc ferrite, the magnetic order can deviate from simple ferrimagnetism when nonmagnetic Zn²⁺ ions occupy tetrahedral sites. An octahedral Fe³⁺ ion that has few or no magnetic (Fe³⁺ or Co²⁺) neighbours on adjacent tetrahedral sites experiences weakened intersublattice coupling. This can lead to strong spin canting or even reversal of its magnetic moment, reducing the magnetic contribution from the octahedral sublattice without changing the number of Fe³⁺ ions. Quantifying the probability of such magnetic disorder under given Zn dilution levels is essential to understand the magnetic structure of these nanoparticles.

## Approach
We implement a probabilistic model inspired by Gilleo's approach. The fraction of tetrahedral sites occupied by Zn is denoted x. For an octahedral Fe³⁺ ion in the particle core, the number of adjacent tetrahedral neighbours is 6; at the surface, where half the neighbours are missing, this number is 3. The probability p(0) that an octahedral ion has zero magnetic tetrahedral neighbours is x to the power of the number of neighbours: p_c(0) = x⁶ for the core and p_s(0) = x³ for the surface. The probability p(1) that it has exactly one magnetic neighbour is given by the binomial term: p_c(1) = 6(1−x)x⁵ and p_s(1) = 3(1−x)x². From these we obtain the probability that an octahedral ion has at most one magnetic tetrahedral neighbour: p(≤1) = p(0) + p(1).

The model is evaluated for two Zn fractions: x = 0.73 (Zn exclusively on tetrahedral sites) and x = 0.65 (10% inversion to octahedral sites). To estimate the overall fractions of inverted and canted octahedral moments, the core and surface probabilities are weighted by the surface atom fraction w_s = 0.25, corresponding to particles with an average diameter of 3.7 nm. The overall inverted fraction is w_s·p_s(0) + (1−w_s)·p_c(0); the overall canted fraction is w_s·p_s(≤1) + (1−w_s)·p_c(≤1). Finally, the model quantifies the consequence for X‑ray magnetic circular dichroism: if 20% of the octahedral moments were inverted, the effective octahedral contribution would reduce to 1 − 2×0.20 = 0.60 times the collinear value. All quantities are computed using only standard arithmetic operations.

## Reproduction target
Produce a single JSON output file that contains all computed quantities of the probabilistic spin‑canting model:
- For each Zn fraction (x = 0.73 and x = 0.65), the core and surface probabilities p(0) and p(≤1).
- The overall inverted fraction and overall canted fraction for each x, computed using the surface fraction w_s = 0.25.
- The XMCD reduction factor when 20% of octahedral moments are inverted, i.e. the numerical factor by which the octahedral contribution is multiplied.
The file must follow the exact structure and field names specified in the output contract. All values must be computed from the given parameters; the goal is to reproduce the underlying probabilistic calculation, not to guess a pre‑existing number.

## Assets
This task uses only Python's standard library. No external datasets, models, or tools need to be downloaded or installed. The computation can be performed entirely with built‑in arithmetic functions.

## Workflow steps

### Step 1: Compute probabilistic spin-canting model
- Role: scored
- Action: Given Zn tetrahedral fractions x=0.73 and x=0.65, coordination numbers (core: 6 tetrahedral neighbours, surface: 3), and a surface atom fraction w_s=0.25, compute p_c(0)=x^6, p_s(0)=x^3, p_c(1)=6(1-x)x^5, p_s(1)=3(1-x)x^2. Then compute p_c(≤1)=p_c(0)+p_c(1) and p_s(≤1)=p_s(0)+p_s(1). Calculate the overall inverted fraction = w_s * p_s(0) + (1-w_s) * p_c(0) and canted fraction = w_s * p_s(≤1) + (1-w_s) * p_c(≤1). Finally, compute the effective octahedral contribution to XMCD when 20% of octahedral moments are inverted (i.e., 1 – 2*0.20 = 0.60). Output all quantities in a JSON file.
- Output file: `/app/outputs/model_results.json`
- Format: json
- Contract: {"type":"object","required":["x_0_73","x_0_65","overall_inverted_fraction","overall_canted_fraction","reduction_if_20_percent_inverted"],"properties":{"x_0_73":{"type":"object","properties":{"core":{"type":"object","properties":{"p0":"number","p_leq1":"number"}},"surface":{"type":"object","properties":{"p0":"number","p_leq1":"number"}}}},"x_0_65":{"type":"object","properties":{"core":{"type":"object","properties":{"p0":"number","p_leq1":"number"}},"surface":{"type":"object","properties":{"p0":"number","p_leq1":"number"}}}},"overall_inverted_fraction":{"type":"object","properties":{"x_0_73":"number","x_0_65":"number"}},"overall_canted_fraction":{"type":"object","properties":{"x_0_73":"number","x_0_65":"number"}},"reduction_if_20_percent_inverted":"number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_results.json
- path: `/app/outputs/model_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Probabilistic model results for spin canting/inversion in Zn-diluted cobalt-zinc ferrite nanoparticles, comparing against hidden paper-reported values.
- schema:
  - `type`: object
  - `required`: `x_0_73`, `x_0_65`, `overall_inverted_fraction`, `overall_canted_fraction`, `reduction_if_20_percent_inverted`
  - `properties`:
    - `x_0_73`:
      - `type`: object
      - `properties`:
        - `core`:
          - `type`: object
          - `properties`:
            - `p0`: number
            - `p_leq1`: number
        - `surface`:
          - `type`: object
          - `properties`:
            - `p0`: number
            - `p_leq1`: number
    - `x_0_65`:
      - `type`: object
      - `properties`:
        - `core`:
          - `type`: object
          - `properties`:
            - `p0`: number
            - `p_leq1`: number
        - `surface`:
          - `type`: object
          - `properties`:
            - `p0`: number
            - `p_leq1`: number
    - `overall_inverted_fraction`:
      - `type`: object
      - `properties`:
        - `x_0_73`: number
        - `x_0_65`: number
    - `overall_canted_fraction`:
      - `type`: object
      - `properties`:
        - `x_0_73`: number
        - `x_0_65`: number
    - `reduction_if_20_percent_inverted`: number

Notes: The model uses only public inputs described in the paper; no external datasets or tools are required. The checker compares the submitted probabilities and fractions against the paper's published Table 1 values and derived statements within prescribed tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "x_0_73",
          "x_0_65",
          "overall_inverted_fraction",
          "overall_canted_fraction",
          "reduction_if_20_percent_inverted"
        ],
        "properties": {
          "x_0_73": {
            "type": "object",
            "properties": {
              "core": {
                "type": "object",
                "properties": {
                  "p0": "number",
                  "p_leq1": "number"
                }
              },
              "surface": {
                "type": "object",
                "properties": {
                  "p0": "number",
                  "p_leq1": "number"
                }
              }
            }
          },
          "x_0_65": {
            "type": "object",
            "properties": {
              "core": {
                "type": "object",
                "properties": {
                  "p0": "number",
                  "p_leq1": "number"
                }
              },
              "surface": {
                "type": "object",
                "properties": {
                  "p0": "number",
                  "p_leq1": "number"
                }
              }
            }
          },
          "overall_inverted_fraction": {
            "type": "object",
            "properties": {
              "x_0_73": "number",
              "x_0_65": "number"
            }
          },
          "overall_canted_fraction": {
            "type": "object",
            "properties": {
              "x_0_73": "number",
              "x_0_65": "number"
            }
          },
          "reduction_if_20_percent_inverted": "number"
        }
      },
      "description": "Probabilistic model results for spin canting/inversion in Zn-diluted cobalt-zinc ferrite nanoparticles, comparing against hidden paper-reported values."
    }
  ],
  "notes": "The model uses only public inputs described in the paper; no external datasets or tools are required. The checker compares the submitted probabilities and fractions against the paper's published Table 1 values and derived statements within prescribed tolerances."
}
```

## How you are scored
A hidden verifier reads your `model_results.json` and compares every numerical field to reference values that correspond to the paper's reported results. Scoring is per‑field: each quantity is compared to its reference via absolute difference. If the difference is within a prescribed tolerance, that field earns full credit; otherwise, credit decays linearly with increasing deviation up to a maximum tolerance. All tolerances are fixed internally and are not visible to you. The final reward is the average of the per‑field scores, scaled to the range [0, 1] and written to the verifier output. The task therefore rewards accurate computation of the model, not merely returning a plausible number.
