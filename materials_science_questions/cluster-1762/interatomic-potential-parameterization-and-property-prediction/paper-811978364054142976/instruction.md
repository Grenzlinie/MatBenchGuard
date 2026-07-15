# Model Pseudopotential Parameterization and Band Structure Prediction for Si, Ge, and α-Sn

## Problem background
Understanding and predicting the electronic band structure of elementary semiconductors (Si, Ge, and α-Sn) is essential for their electronic and optical properties. Empirical pseudopotential methods offer a practical route to obtain band structures from a small number of form factors, but general model pseudopotentials that depend only on atomic number often fail to reproduce key transition energies, particularly those near the band gap. This work introduces a phenomenological correction to the VS pseudopotential: a sum of higher-order spherical Bessel functions with three adjustable coefficients (C1, C2, C3). When these coefficients are properly fitted, the resulting modified VS (mVS) pseudopotential is intended to yield band structures and transition energies in close agreement with experiment. The task is to determine the optimal C1, C2, and C3 for Si, Ge, and α-Sn and to verify that the computed transition energies for a set of high-symmetry interband transitions match the established experimental benchmarks.

## Approach
The mVS pseudopotential form factor is a sum of the original VS term (parametrized by β1 and β2 from Veljković and Slavić (1972) Table 1) and a correction comprising the first three spherical Bessel functions j1, j2, j3 weighted by the unknown coefficients C1, C2, and C3. The electronic band structure is obtained by solving the secular equation for the diamond/zincblende lattice. We employ Brust’s modification of Löwdin perturbation theory with parameters N=50 and Γ=89, which ensures convergence of the eigenvalues to well within the experimental uncertainty of the transition energies.

The fitting procedure starts from the Cohen–Bergstresser empirical pseudopotential form factors, w(111), w(220), and w(311). The form factor w(220) is chosen as the adjustable parameter; its value is refined iteratively while the other two form factors remain fixed at their Cohen–Bergstresser values. At each iteration, the coefficients C1, C2, C3 are recomputed so that the mVS form factor passes through the current set of three form factors. The iteration aims to bring the computed transition energies near the band gap into agreement with the experimental reference values provided below. The fit targets the following experimental energies (in eV), which are extracted from optical and photoemission measurements. For α-Sn the centre of gravity of spin–orbit split levels is used for comparison, and missing values are marked “—”.

**Experimental reference transition energies (eV)**

| Transition | Si | Ge | α-Sn |
|------------|----|----|------|
| Γ2′–Γ25′ | 4.15 | 0.99 | −0.16 |
| Γ15–Γ25′ | 3.41 | 3.23 | 2.9 |
| L1–Γ25′ | — | 0.84 | 0.32 |
| X1(Δ1)–Γ25′ | — | 1.26 | — |
| L1–L3′ | 3.40 | 2.34 | 1.4 |
| L3–L3′ | 5.1 | 5.80 | 4.4 |
| X1–X4 | 4.3 | 4.50 | 3.5 |

Once the coefficients are finalised, the secular equation is solved at the same high-symmetry points to obtain the computed transition energies. No spin–orbit splitting is included. The complete fitting algorithm consists of: (1) computing initial C1, C2, C3 from the starting form factors, (2) identifying w(220) as the optimum adjustable form factor, (3–5) iterating by changing w(220) in small steps and recalculating the coefficients until the computed near‑gap energies agree with the experimental targets within a prescribed reliability window, finally recording the converged C1, C2, C3.

## Reproduction target
Produce the fitted mVS pseudopotential coefficients C1, C2, C3 (in Rydbergs) for Si, Ge, and α-Sn, and compute the transition energies (in eV) for the high‑symmetry interband transitions listed in the workflow steps, using the fitted pseudopotential. The coefficients should yield near‑gap transition energies that agree with the experimental reference values to within the fitting tolerance used in the procedure. The final computed transition energies must be consistent with the same experimental benchmarks.

## Assets

- β1, β2 parameters for Si, Ge, α-Sn (Veljković and Slavić, 1972, Table 1): 10.1103/PhysRevLett.29.105
- Cohen-Bergstresser pseudopotential form factors w(111), w(220), w(311) for Si, Ge, α-Sn (Cohen and Bergstresser, 1966): 10.1103/PhysRev.141.789

## Workflow steps

### Step 1: Gather reference data
- Role: process
- Action: Obtain the β1, β2 parameters for Si, Ge, α‑Sn from Veljković and Slavić (1972) Table 1, the Cohen‑Bergstresser initial form factors w(111), w(220), w(311) from Cohen and Bergstresser (1966), and note the experimental target transition energies provided in the problem description. Save a summary file `reference_data.json` containing these inputs.
- Evidence: `/app/outputs/reference_data.json`

### Step 2: Fit mVS pseudopotential coefficients
- Role: scored
- Action: Implement the mVS pseudopotential form factor (Equation 2 of the source paper), the secular equation solver using Brust's modification of Löwdin perturbation theory (with N=50, Γ=89), and the five‑step iterative fitting algorithm. Starting from the three Cohen‑Bergstresser form factors, determine the optimal w(220) and fit the coefficients C1, C2, C3 for Si, Ge, and α‑Sn so that the computed near‑gap transition energies fall within ±0.05 eV of the experimental targets. Output the final fitted coefficients.
- Output file: `/app/outputs/step_01_fitted_coefficients.json`
- Format: json
- Contract: JSON object with keys "Si", "Ge", "alphaSn"; each value an object with numeric fields "C1", "C2", "C3".
- Scoring: scored by hidden verifier

### Step 3: Compute transition energies
- Role: scored
- Action: Using the fitted mVS pseudopotential from step_01, solve the secular equation to calculate the transition energies (in eV) at the high‑symmetry points listed in the paper's Table 2: Γ2'‑Γ25', Γ15‑Γ25', L1‑Γ25' (for Ge), X1(Δ1)‑Γ25' (for Ge), L1‑L3', L3‑L3', X1‑X4. For α‑Sn, use the center of gravity of spin‑orbit split levels for comparison with experiment. Include all transitions for which a computed mVS value is reported (excluding those marked as unavailable).
- Output file: `/app/outputs/step_02_transition_energies.csv`
- Format: csv
- Contract: CSV with columns: material (one of Si, Ge, alphaSn), transition (string, e.g. Gamma2'_Gamma25'), energy (numeric, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_fitted_coefficients.json`
- `/app/outputs/step_02_transition_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_fitted_coefficients.json
- path: `/app/outputs/step_01_fitted_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted mVS pseudopotential coefficients C1, C2, C3 in Rydberg for Si, Ge, and α-Sn.
- schema:
  - `type`: object
  - `required`:
    - `Si`:
      - `type`: object
      - `required`: `C1`, `C2`, `C3`
    - `Ge`:
      - `type`: object
      - `required`: `C1`, `C2`, `C3`
    - `alphaSn`:
      - `type`: object
      - `required`: `C1`, `C2`, `C3`

### step_02_transition_energies.csv
- path: `/app/outputs/step_02_transition_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed transition energies (eV) for all transitions reported in the reference paper's Table 2.
- schema:
  - `type`: table
  - `required_columns`: `material`, `transition`, `energy`
  - `units`:
    - `energy`: eV

Notes: The experimental target transition energies are provided within the problem statement and are not a separate downloadable resource.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_fitted_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Si": {
            "type": "object",
            "required": [
              "C1",
              "C2",
              "C3"
            ]
          },
          "Ge": {
            "type": "object",
            "required": [
              "C1",
              "C2",
              "C3"
            ]
          },
          "alphaSn": {
            "type": "object",
            "required": [
              "C1",
              "C2",
              "C3"
            ]
          }
        }
      },
      "description": "Fitted mVS pseudopotential coefficients C1, C2, C3 in Rydberg for Si, Ge, and α-Sn."
    },
    {
      "file": "step_02_transition_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "transition",
          "energy"
        ],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Computed transition energies (eV) for all transitions reported in the reference paper's Table 2."
    }
  ],
  "notes": "The experimental target transition energies are provided within the problem statement and are not a separate downloadable resource."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier in two parts. The fitted coefficients (step_01) are compared to a hidden reference on a per-coefficient basis; a small absolute tolerance is allowed. The computed transition energies (step_02) are compared to a hidden reference; each transition energy must fall within a prescribed absolute tolerance. Transition energies carry approximately 70% of the total reward, and the coefficients carry the remaining 30%. For each entry, agreement within tolerance earns full credit; larger deviations lead to a linearly decreasing score down to zero. The verifier aggregates the scores across all entries into a final reward between 0 and 1. The primary evaluation criterion is the accuracy of the band‑gap transition energies, as they are the main drivers of the fitting procedure.
