# Fe-Cu-Ni fcc/liquid Phase Equilibria Calculation

## Problem background
The Fe-Cu-Ni ternary system is of great importance for alloy solidification and processing, because the stability of the liquid and fcc solid-solution phases determines the microstructural evolution and mechanical properties. The CALPHAD (CALculation of PHAse Diagrams) methodology constructs thermodynamic models for the Gibbs energy of each phase and uses them to compute phase equilibria. The excess Gibbs energy of mixing is described by Redlich-Kister polynomials, whose temperature-dependent coefficients are evaluated from experimental data and phase boundary measurements. This task addresses the computation of the fcc/liquid phase boundaries in Fe-Cu-Ni alloys using a self-consistent set of Redlich-Kister coefficients and lattice stabilities. The aim is to determine, as a function of temperature, the compositions at which the liquid and the fcc solid phase coexist in equilibrium.

## Approach
The molar Gibbs energy of a phase φ (φ = fcc or liquid) in the Fe-Cu-Ni ternary is written as:

G^φ = Σ_i x_i °G_i^φ + RT Σ_i x_i ln x_i + exG^φ

where x_i (i = Cu, Fe, Ni) are mole fractions, °G_i^φ is the Gibbs energy of pure element i in the φ structure, and exG^φ is the excess Gibbs energy of mixing. The difference between the liquid and fcc structures of a pure element is its lattice stability:

ΔG_i(fcc→liq) = °G_i^liq − °G_i^fcc

which is expressed as a polynomial in temperature (given below).

The excess Gibbs energy is expanded in Redlich-Kister polynomials:

exG^φ = Σ_{i<j} Σ_{v=0}^{n_ij} g_ij^{v,φ} x_i x_j (x_i − x_j)^v + x_Cu x_Fe x_Ni (A^φ + B^φ T)

with temperature-dependent coefficients g_ij^{v,φ} = a + b T. The following evaluated coefficients are provided (units J/mol, T in K):

**Cu-Ni system**
- fcc: v=0 → a=9534.49, b=2.83903; v=1 → a=424.255, b=−0.62595; v=2 → a=−1812.93, b=2.12233
- liq: v=0 → a=32238.7, b=−11.1093; v=1 → a=−619.65, b=−1.08812; v=2 → a=−213.489, b=0.97309

**Fe-Ni system**
- fcc: v=0 → a=−18298.8, b=5.14894; v=1 → a=14313.6, b=−7.65979
- liq: v=0 → a=−20292.4, b=5.14137; v=1 → a=11924.4, b=−6.16329

**Cu-Fe system**
- fcc: v=0 → a=48206.0, b=−8.44645; v=1 → a=−5918.0, b=5.01725
- liq: v=0 → a=34321.3, b=−1.8577; v=1 → a=−1811.6, b=1.6401; v=2 → a=7564.6, b=−2.5857; v=3 → a=−2418.3, b=2.3472

**Ternary interaction** exG^φ = x_Cu x_Fe x_Ni (A^φ + B^φ T)
- fcc: A = −35982, B = −12.0
- liq: A = −45000, B = 0

**Lattice stabilities** ΔG(fcc→liq) = a + b T + c T² + d T ln T (J/mol, T in K)

| Element | a       | b        | c          | d     |
|---------|---------|----------|------------|-------|
| Cu      | 13054.1 | −9.6232  | 4.1756e-3  | 22.03 |
| Fe      | −11274.0| 163.878  | 4.1756e-3  | 22.03 |
| Ni      | 17614.6 | −10.209  | 4.1756e-3  | 22.03 |

At each temperature, phase equilibrium is found by the condition of minimum total Gibbs energy, which requires equality of the chemical potentials of each element in the two phases:

μ_i^fcc(x^fcc) = μ_i^liq(x^liq)   (i = Cu, Fe, Ni)

subject to the mass balance constraints Σ_i x_i^fcc = 1 and Σ_i x_i^liq = 1. Solving this system yields the compositions of the coexisting fcc and liquid phases at equilibrium — the phase boundary points. To map the entire fcc/liquid coexistence region, the problem is solved for a range of overall compositions and/or tie-lines at each temperature from 1373 K to 1673 K in 50 K steps.

## Reproduction target
Compute the fcc/liquid phase boundary coordinates for the Fe-Cu-Ni system at the following seven temperatures: 1373 K, 1423 K, 1473 K, 1523 K, 1573 K, 1623 K, and 1673 K. For each temperature, determine the equilibrium mole fractions of Cu, Fe, and Ni for both the fcc solid phase and the liquid phase along the phase boundary. Collect all results in a single CSV file with columns: temperature (K, float), phase (string: 'fcc' or 'liq'), x_Cu (float, 0–1), x_Fe (float, 0–1), x_Ni (float, 0–1). Each row represents one point on the boundary; the set of rows for a temperature should describe the entire liquidus and solidus surfaces. The file must be written to `/app/outputs/phase_boundaries.csv`.

## Assets

- NumPy: numpy
- SciPy: scipy
- pycalphad: pycalphad

## Workflow steps

### Step 1: Compute fcc/liquid phase equilibria in Fe-Cu-Ni
- Role: scored (load-bearing)
- Action: Implement the excess Gibbs energy model for the fcc and liquid phases of the Fe-Cu-Ni system using Redlich-Kister polynomials with the provided coefficients (binary Cu-Ni, Fe-Ni, Cu-Fe; ternary interaction) and the lattice stabilities. For each temperature from 1373 K to 1673 K at 50 K intervals, perform a Gibbs energy minimization to find the equilibrium compositions of the coexisting fcc and liquid phases. Collect the resulting phase boundary coordinates (mole fractions of Cu, Fe, Ni) for both phases at each temperature.
- Output file: `/app/outputs/phase_boundaries.csv`
- Format: csv
- Contract: temperature (column: temperature, unit: K, float), phase (column: phase, string: 'fcc' or 'liq'), x_Cu (column: x_Cu, float between 0 and 1), x_Fe (column: x_Fe, float between 0 and 1), x_Ni (column: x_Ni, float between 0 and 1). Each row is one point along the phase boundary.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundaries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundaries.csv
- path: `/app/outputs/phase_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed fcc/liquid phase boundary coordinates for the Fe-Cu-Ni system at temperatures from 1373 K to 1673 K. Each row gives the mole fractions of Cu, Fe, Ni and the phase (fcc or liq) for a point along the boundary.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `phase`, `x_Cu`, `x_Fe`, `x_Ni`
  - `units`:
    - `temperature`: K
    - `x_Cu`: mole fraction (0–1)
    - `x_Fe`: mole fraction (0–1)
    - `x_Ni`: mole fraction (0–1)

Notes: The solver may produce multiple tie-line endpoints; all are valid as long as they satisfy the equilibrium conditions. The checker compares against hidden reference coordinates using a spatial tolerance in composition space.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "phase",
          "x_Cu",
          "x_Fe",
          "x_Ni"
        ],
        "units": {
          "temperature": "K",
          "x_Cu": "mole fraction (0–1)",
          "x_Fe": "mole fraction (0–1)",
          "x_Ni": "mole fraction (0–1)"
        }
      },
      "description": "Computed fcc/liquid phase boundary coordinates for the Fe-Cu-Ni system at temperatures from 1373 K to 1673 K. Each row gives the mole fractions of Cu, Fe, Ni and the phase (fcc or liq) for a point along the boundary."
    }
  ],
  "notes": "The solver may produce multiple tie-line endpoints; all are valid as long as they satisfy the equilibrium conditions. The checker compares against hidden reference coordinates using a spatial tolerance in composition space."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares your phase boundary coordinates to a set of reference coordinates (not disclosed to you). For each reference point at a given temperature, the verifier checks whether any of your submitted points falls within a spatial tolerance in composition space (e.g., Euclidean distance in the three‑component triangle). The final reward is computed as the fraction of reference points that are matched, or as a continuous monotonic function of the average deviation, so that higher accuracy — smaller deviations or more matched points — yields a strictly higher score. The scoring is fully automatic; there is no human review. Reporting numbers that do not correspond to a correct thermodynamic solution will not produce a high reward.
