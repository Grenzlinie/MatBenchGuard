# Surface Tension and Segregation in Liquid Co-Cr-Ni Ternary Alloys via Butler's Equation

## Problem background
Liquid Co-Cr-Ni based alloys are widely used for high-temperature coatings (e.g., MCrAlY systems) where surface composition and tension critically affect protective oxide formation and adhesion. Because direct high-temperature measurements are difficult, theoretical predictions are essential. This work aims to predict the surface tension and surface composition of liquid Co-Cr-Ni ternary alloys at T=1873 K using Butler's equation, in order to understand which element segregates to the surface and how surface tension changes with composition.

## Approach
The surface properties are computed using Butler's equation, which treats the surface as a separate thermodynamic phase in equilibrium with the bulk. For ternary regular solutions, the partial excess Gibbs energies in bulk and surface are obtained from binary Redlich-Kister polynomials combined via the Muggianu model, with a surface coordination ratio β̃ = 0.75 to relate surface to bulk excess energies. The required pure-component properties (surface tension as linear functions of temperature, liquid densities and molar masses) are fixed constants.

The numerical inputs are provided here:

- Binary Redlich-Kister parameters (excess Gibbs energy in J·mol⁻¹, T in K):
  * Co–Cr: ν=0: −12008.6239 + 2.2019·T;  ν=1: −5836.4696 + 1.1402·T
  * Cr–Ni: ν=0: 318 − 7.33·T;  ν=1: 16941 − 6.37·T
  * Co–Ni: ν=0: 1331 (T‑independent)
- Pure-component surface tensions (mN·m⁻¹):
  * σ_Co(T) = 866.0 − 0.15·(T − 933)
  * σ_Cr(T) = 1672.0 − 0.20·(T − 2178)
  * σ_Ni(T) = 1838.0 − 0.42·(T − 1728)
- Liquid densities at 1873 K (g·cm⁻³): ρ_Co = 7.75, ρ_Cr = 6.3, ρ_Ni = 7.9
- Molar masses (g·mol⁻¹): Co: 58.933, Cr: 51.996, Ni: 58.693
- Avogadro's number: N₀ = 6.02214×10²³ mol⁻¹
- Surface area of component i: S_i = 1.091·N₀·(M_i / ρ_i)^{2/3}
- Surface coordination ratio: β̃ = 0.75

For each point on a grid of bulk compositions (X_Cr and X_Ni varying from 0.0 to 0.9 in steps of 0.1, with X_Co = 1 − X_Cr − X_Ni, discarding points where X_Co < 0), the Butler equations are solved simultaneously for the common surface tension σ and the equilibrium surface mole fractions (X_Co^s, X_Cr^s, X_Ni^s). The solution yields a table of surface tension and surface composition for the scanned bulk compositions.

## Reproduction target
For a grid of bulk compositions of liquid Co–Cr–Ni at T = 1873 K, with X_Cr and X_Ni each ranging from 0.0 to 0.9 in steps of 0.1, and X_Co = 1 − X_Cr − X_Ni (skip compositions where X_Co < 0), compute the common surface tension σ (mN·m⁻¹) and the equilibrium surface mole fractions (X_Co^s, X_Cr^s, X_Ni^s) using Butler's equation. Produce a CSV file `surface_properties.csv` with columns: `bulk_X_Cr`, `bulk_X_Ni`, `bulk_X_Co`, `surface_tension_mN_per_m`, `surface_X_Cr`, `surface_X_Ni`, `surface_X_Co`. The file must contain no missing values and all values must be numeric.

## Assets

- Binary Redlich-Kister excess Gibbs energy parameters for liquid Co-Cr, Cr-Ni, and Co-Ni
- Temperature-dependent surface tension functions for pure liquid Co, Cr, and Ni
- Liquid densities of pure Co, Cr, and Ni at T=1873 K
- Python scientific computing stack (scipy, numpy, pandas): scipy numpy pandas

## Workflow steps

### Step 1: Assemble thermodynamic input parameters
- Role: process
- Action: Collect the binary Redlich-Kister polynomial coefficients (Co-Cr, Cr-Ni, Co-Ni), pure component surface tension functions, liquid densities, and the surface coordination ratio β̃ = 0.75. These are provided as literal constants/equations in the instruction; no external data fetch is necessary.
- Evidence: none

### Step 2: Compute ternary surface properties via Butler's equation
- Role: scored (load-bearing)
- Action: Implement Butler's equation for a ternary regular solution using the Redlich-Kister-Muggianu model for excess Gibbs energies, the given pure-component surface tensions and molar surface areas, and β̃ = 0.75. Solve simultaneously for the common surface tension σ and the surface mole fractions over the specified composition grid at T=1873 K. Write the results to surface_properties.csv.
- Output file: `/app/outputs/surface_properties.csv`
- Format: csv
- Contract: CSV with columns: bulk_X_Cr (float), bulk_X_Ni (float), bulk_X_Co (float), surface_tension_mN_per_m (float), surface_X_Cr (float), surface_X_Ni (float), surface_X_Co (float). No missing values. All numeric units as stated.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_properties.csv
- path: `/app/outputs/surface_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing surface tension (mN/m) and surface composition (mole fractions) for the specified ternary composition grid at T=1873 K, computed via Butler's equation.
- schema:
  - `type`: table
  - `required_columns`: `bulk_X_Cr`, `bulk_X_Ni`, `bulk_X_Co`, `surface_tension_mN_per_m`, `surface_X_Cr`, `surface_X_Ni`, `surface_X_Co`
  - `units`:
    - `surface_tension_mN_per_m`: mN·m⁻¹

Notes: The checker recomputes the expected values at hidden composition points using the same physical model and compares with absolute tolerances; structural checks on Cr segregation and surface tension trends are also applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "bulk_X_Cr",
          "bulk_X_Ni",
          "bulk_X_Co",
          "surface_tension_mN_per_m",
          "surface_X_Cr",
          "surface_X_Ni",
          "surface_X_Co"
        ],
        "units": {
          "surface_tension_mN_per_m": "mN·m⁻¹"
        }
      },
      "description": "CSV containing surface tension (mN/m) and surface composition (mole fractions) for the specified ternary composition grid at T=1873 K, computed via Butler's equation."
    }
  ],
  "notes": "The checker recomputes the expected values at hidden composition points using the same physical model and compares with absolute tolerances; structural checks on Cr segregation and surface tension trends are also applied."
}
```

## How you are scored
Your submitted `surface_properties.csv` will be scored by a hidden verifier. The verifier will independently recompute the surface tension and surface composition at a set of hidden bulk composition points using the same Butler equation and input data, and compare against the values in your file with appropriate tolerances. It will also check that your results satisfy general physical expectations for liquid ternary alloy surfaces, such as surface segregation behavior and surface tension trends. The overall reward is a weighted score from these checks. No gold metric values are disclosed; the task is to correctly implement the physical model.
