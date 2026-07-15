# Correlation Exponents of Fully Frustrated Ising Models

## Problem background
Fully frustrated two-dimensional Ising models (such as the Villain model and the triangular antiferromagnet) are known to exhibit long-range spin-spin correlations at zero temperature, but the value of the correlation exponent has historically been obtained through calculations specific to each model. A unified theoretical framework that directly connects the frustrated-model correlation functions to the well-studied unfrustrated square-lattice ferromagnet at its critical temperature has been of considerable interest. This task reproduces a general propagator expansion that expresses the spin-spin correlation function of frustrated Ising systems in terms of the ferromagnetic result. The goal is to implement the expansion and compute, from first principles, the correlation exponents for both the ferromagnetic reference system and the fully frustrated models, and to verify the scaling relation between them.

## Approach
The correlation function can be written as a determinant and expanded in a series of terms Π_n involving products of asymptotic Green's functions. For the square-lattice ferromagnet at the critical temperature, the asymptotic Green's function is g_{ij} ∼ 1/(π(i−j)). The Dotsenko–Dotsenko propagator expansion evaluates the leading logarithmic contributions of even-n Π_n terms to extract the correlation exponent η.

For fully frustrated models, a sublattice-dependent factor Q modifies the asymptotic Green's function to g_{ij} ∼ Q_{ij}/(π(i−j)). By organising the sites into sublattices (d sublattices), the nth term of the frustrated model, Π_n, can be expressed in terms of the ferromagnetic term Π̄_n as Π_n = d^{-n} Tr(Q^n) Π̄_n. The matrix Q is model-specific: for the Villain model (d=2) it is [[0,2],[2,0]]; for the triangular antiferromagnet (d=3) it is [[0,√3,−√3],[−√3,0,√3],[√3,−√3,0]].

The reproduction proceeds in two conceptual stages: first, implement the propagator expansion for the ferromagnetic square lattice to obtain the series Π̄_n and the ferromagnetic exponent. Second, for each frustrated model, compute the factor d^{-n} Tr(Q^n) for even n, combine it with the ferromagnetic Π̄_n, and extract the frustrated correlation exponent. The relationship between Π_n and Π̄_n, which follows from the sublattice factor d^{-n} Tr(Q^n), should be verified by computing the ratios Π_n/Π̄_n.

## Reproduction target
Implement the propagator expansion and compute the correlation function exponents for the following three systems:
1. The square Ising ferromagnet at the critical temperature.
2. The Villain model (horizontal/vertical correlations) at zero temperature.
3. The triangular antiferromagnet at zero temperature.

The exponent for each model must be extracted from the leading logarithmic contributions in the series expansion. In addition, for even values of the order n, compute the ratio Π_n (frustrated) / Π̄_n (ferromagnetic) for both the Villain model and the triangular antiferromagnet, and report these ratios as lists of numbers (one ratio per even n).

Write all results to the file specified by the output contract (`/app/outputs/reproduction_results.json`), containing the keys `ferromagnetic_exponent`, `villian_model_exponent`, `triangular_exponent`, and `ratio_for_even_n` (an object with keys `Villain` and `Triangular` each holding a list of ratios).

## Assets

- Python 3 with numpy and sympy: numpy sympy

## Workflow steps

### Step 1: Compute ferromagnetic correlation exponent baseline
- Role: process
- Action: Implement the Dotsenko-Dotsenko propagator expansion for the square Ising ferromagnet at Tc: use the asymptotic Green's function g_{ij} ~ 1/(π(i-j)) to construct the matrix M = I + g, compute the series Π̄_n and extract the correlation exponent η from the leading logarithmic contributions. Save the series and derived exponent.
- Evidence: `/app/outputs/ferromagnetic_baseline.json`

### Step 2: Derive frustrated model exponents and verify ratio
- Role: scored (load-bearing)
- Action: For the Villain model (d=2, Q=[[0,2],[2,0]]) and the triangular antiferromagnet (d=3, Q=[[0,√3,-√3],[-√3,0,√3],[√3,-√3,0]]), compute the factor d^{-n} Tr Q^n for even n. Using the ferromagnetic Π̄_n from the previous step, verify the relationship between Π_n and Π̄_n implied by the sublattice factor. Calculate the correlation exponent η for each frustrated model and compile the ratios for even n. Output all results to reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: {"ferromagnetic_exponent": number, "villian_model_exponent": number, "triangular_exponent": number, "ratio_for_even_n": {"Villain": [number, ...], "Triangular": [number, ...]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Main reproduction artifact with correlation exponents for ferromagnetic, Villain, and triangular antiferromagnet models, and the ratio Π_n/Π̄_n for even n.
- schema:
  - `type`: object
  - `required`: `ferromagnetic_exponent`, `villian_model_exponent`, `triangular_exponent`, `ratio_for_even_n`
  - `properties`:
    - `ferromagnetic_exponent`:
      - `type`: number
      - `description`: dimensionless
    - `villian_model_exponent`:
      - `type`: number
      - `description`: dimensionless
    - `triangular_exponent`:
      - `type`: number
      - `description`: dimensionless
    - `ratio_for_even_n`:
      - `type`: object
      - `description`: object containing lists of floats for Villain and Triangular
      - `properties`:
        - `Villain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `Triangular`:
          - `type`: array
          - `items`:
            - `type`: number

Notes: All outputs are dimensionless numerical values derived from the propagator expansion. The hidden verifier checks the reported exponents and ratio consistency against the analytic derivation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "ferromagnetic_exponent",
          "villian_model_exponent",
          "triangular_exponent",
          "ratio_for_even_n"
        ],
        "properties": {
          "ferromagnetic_exponent": {
            "type": "number",
            "description": "dimensionless"
          },
          "villian_model_exponent": {
            "type": "number",
            "description": "dimensionless"
          },
          "triangular_exponent": {
            "type": "number",
            "description": "dimensionless"
          },
          "ratio_for_even_n": {
            "type": "object",
            "description": "object containing lists of floats for Villain and Triangular",
            "properties": {
              "Villain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "Triangular": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Main reproduction artifact with correlation exponents for ferromagnetic, Villain, and triangular antiferromagnet models, and the ratio Π_n/Π̄_n for even n."
    }
  ],
  "notes": "All outputs are dimensionless numerical values derived from the propagator expansion. The hidden verifier checks the reported exponents and ratio consistency against the analytic derivation."
}
```

## How you are scored
A hidden verifier independently checks the artifacts produced by each workflow stage. It compares your reported exponents and ratio lists against reference values derived from the analytic derivation, using tolerances that absorb numerical rounding. Credits are awarded based on the agreement of the exponents and the consistency of the ratio relation; a higher weight is placed on the final scored artifact (`reproduction_results.json`). The final reward is a weighted combination of per-stage scores. Reporting a known result without executing the required computation will not suffice, because the verifier checks both the numeric values and their consistency with the derived scaling relationship.
