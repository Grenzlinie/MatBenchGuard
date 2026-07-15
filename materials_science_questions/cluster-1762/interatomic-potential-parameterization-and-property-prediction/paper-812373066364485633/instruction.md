# Prediction of Oxygen Positional Parameters in Rare-Earth Orthovanadates by Lattice Energy Minimization

## Problem background
The rare-earth orthovanadates RVO₄ (R = lanthanide or Y) crystallize in a tetragonal zircon-type structure with space group I4₁/amd. In this structure, the oxygen atoms occupy the 16(h) Wyckoff site, whose positions are described by two fractional coordinates (u, v) within the unit cell. Precise knowledge of these oxygen parameters is important for understanding the structural, optical, and luminescent properties of these materials. While X‑ray diffraction refinements can determine (u, v) for individual compounds, carrying out such measurements for all members of the series is time‑consuming. A practical alternative is to predict the oxygen coordinates for the entire family from a lattice‑energy model using only the experimentally determined lattice parameters and a small number of calibration structures. The present task implements this approach: given the lattice constants of each vanadate and a minimal set of short‑range repulsion constants, you will compute the (u, v) values that minimise the lattice energy for every member of the series.

## Approach
The method is a point‑charge lattice‑energy model combined with short‑range metal–oxygen repulsion. All calculations assume the space group I4₁/amd and the experimentally determined lattice parameters a₀, c₀ for each compound (Table 1). The total energy E(u, v) consists of:

1. **Electrostatic Madelung term** – a point‑charge sum over the lattice using formal charges M³⁺, V⁵⁺, O²⁻, evaluated by the Bertaut method with a Templeton convergence correction.
2. **Short‑range repulsion** – an inverse‑power term C/rᵐ for each M–O pair and another term C_V/rⁿ for each V–O pair. The exponents follow Pauling’s rules: m = 9.5 for lanthanides, m = 8.5 for yttrium, n = 8 for vanadium–oxygen.

The repulsion constants C_Y, C_Nd, C_Er, and C_V are not pre‑given; you must determine them from the experimental oxygen positions of the three compounds whose structures have been refined by X‑ray diffraction (YVO₄, NdVO₄, ErVO₄). The fitting procedure minimises, with respect to the constants, the weighted sum of squared energy derivatives evaluated at the experimental (u,v) for the three calibration compounds:

\[
\sum \frac{1}{(\Delta p_i)^2} \left( \frac{\partial E(MVO_4)}{\partial p_i} \right)^2 = \text{minimum},
\]

where M runs over Y, Nd, Er, p₁ = u, p₂ = v, and Δp_i is the experimental uncertainty in the corresponding coordinate. Because the lattice energy is linear in the repulsion constants, the minimum condition yields a set of linear equations; solving them gives the optimum C_Y, C_Nd, C_Er, and C_V.

The experimental oxygen coordinates and uncertainties to use in the fit are:

| Compound | u_exp   | Δu     | v_exp   | Δv     |
|----------|---------|--------|---------|--------|
| YVO₄     | 0.1846  | 0.0012 | 0.3273  | 0.0013 |
| NdVO₄    | 0.1801  | 0.0006 | 0.3284  | 0.0009 |
| ErVO₄    | 0.187   | 0.002  | 0.325   | 0.003  |

For the remaining lanthanides (Ce–Lu, except Nd and Er) the metal‑oxygen constant C_R is obtained by drawing a straight line through the (Z, C_R) points for Nd and Er:

\[
C_R = C_{Nd} + \frac{C_{Er} - C_{Nd}}{Z_{Er} - Z_{Nd}} (Z - Z_{Nd}).
\]

Yttrium is treated separately with its own fitted C_Y.

Once the constants are determined, the oxygen fractional coordinates (u, v) in the 16(h) site are the only variables; for each compound the energy is numerically minimised with respect to (u, v) to yield the predicted oxygen parameters.

**Table 1: Lattice parameters (Å)**

| Compound | a₀     | c₀     |
|----------|--------|--------|
| CeVO₄   | 7.3990 | 6.4960 |
| PrVO₄   | 7.3633 | 6.4652 |
| NdVO₄   | 7.3290 | 6.4356 |
| SmVO₄   | 7.2652 | 6.3894 |
| EuVO₄   | 7.2365 | 6.3675 |
| GdVO₄   | 7.2126 | 6.3483 |
| TbVO₄   | 7.1772 | 6.3289 |
| DyVO₄   | 7.1434 | 6.3130 |
| HoVO₄   | 7.1214 | 6.2926 |
| ErVO₄   | 7.0975 | 6.2723 |
| TmVO₄   | 7.0712 | 6.2606 |
| YbVO₄   | 7.0435 | 6.2470 |
| LuVO₄   | 7.0243 | 6.2316 |
| YVO₄    | 7.1230 | 6.2920 |

Exponents: M–O m = 9.5 for R (lanthanides), m = 8.5 for Y; V–O n = 8.

## Reproduction target
Implement the lattice energy model described above for the 14 tetragonal vanadates: CeVO₄, PrVO₄, NdVO₄, SmVO₄, EuVO₄, GdVO₄, TbVO₄, DyVO₄, HoVO₄, ErVO₄, TmVO₄, YbVO₄, LuVO₄, and YVO₄ (LaVO₄ is monoclinic and excluded). For each compound, use the provided lattice parameters and the repulsion constants obtained from the fitting step. Numerically minimise the total energy E(u, v) with respect to the oxygen fractional coordinates u and v. Output the predicted (u, v) for every compound as a CSV file `predicted_positions.csv` with columns `compound`, `Z` (atomic number of the rare‑earth or 39 for Y), `u`, and `v`.

## Assets

- Lattice parameters and experimental oxygen positions for calibration (provided inline)
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 0: Fit repulsion constants from experimental structures
- Role: process
- Action: Using the experimental oxygen positions and uncertainties for YVO₄, NdVO₄, and ErVO₄ provided above, construct the linear system that minimises the weighted sum of squared energy derivatives (Eq. 2). Compute the required Madelung and repulsion energy contributions at the experimental (u,v) for each calibration compound. Solve the linear system to obtain the optimum repulsion constants C_Y, C_Nd, C_Er, and C_V. From these, determine the metal‑oxygen constant for each remaining lanthanide by linear interpolation between Nd and Er (C_R = C_Nd + (C_Er − C_Nd)/(Z_Er − Z_Nd) × (Z − Z_Nd)). Yttrium uses its own fitted C_Y. Output a file `fitted_constants.csv` containing the fitted C_R and C_V for every compound (Ce–Lu + Y) for documentation; this file is not scored but may be used in the next step.
- Evidence: fitted_constants.csv (optional)

### Step 1: Compute u,v via lattice energy minimization
- Role: scored
- Action: Implement the lattice energy model: point-charge Madelung sum (Bertaut method with Templeton convergence correction) plus short-range repulsion terms using the repulsion constants you determined in Step 0. For each vanadate compound (YVO₄, NdVO₄, ErVO₄, and the lanthanide series CeVO₄ through LuVO₄), numerically minimise the total energy with respect to the oxygen fractional coordinates u,v in Wyckoff site 16(h) (space group I4₁/amd). Write the minimising u,v for every compound to predicted_positions.csv.
- Output file: `/app/outputs/predicted_positions.csv`
- Format: csv
- Contract: compound (string), Z (integer), u (float), v (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_positions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_positions.csv
- path: `/app/outputs/predicted_positions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted oxygen positional parameters (u,v) from lattice energy minimization using Model II repulsion constants.
- schema:
  - `type`: table
  - `required_columns`:
    - `name`: compound
    - `type`: string
    - `description`: Compound identifier, e.g., YVO4, NdVO4, CeVO4
    - `name`: Z
    - `type`: integer
    - `description`: Atomic number of the rare-earth (or Y) cation
    - `name`: u
    - `type`: float
    - `description`: Oxygen fractional coordinate u in Wyckoff site 16h
    - `name`: v
    - `type`: float
    - `description`: Oxygen fractional coordinate v in Wyckoff site 16h

Notes: The CSV must include all 14 tetragonal vanadates: CeVO4, PrVO4, NdVO4, SmVO4, EuVO4, GdVO4, TbVO4, DyVO4, HoVO4, ErVO4, TmVO4, YbVO4, LuVO4, and YVO4. LaVO4 is excluded because it is monoclinic. The checker will compare the u,v values for the three calibration compounds (YVO4, NdVO4, ErVO4) against hidden reference values within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_positions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          {
            "name": "compound",
            "type": "string",
            "description": "Compound identifier, e.g., YVO4, NdVO4, CeVO4"
          },
          {
            "name": "Z",
            "type": "integer",
            "description": "Atomic number of the rare-earth (or Y) cation"
          },
          {
            "name": "u",
            "type": "float",
            "description": "Oxygen fractional coordinate u in Wyckoff site 16h"
          },
          {
            "name": "v",
            "type": "float",
            "description": "Oxygen fractional coordinate v in Wyckoff site 16h"
          }
        ]
      },
      "description": "Predicted oxygen positional parameters (u,v) from lattice energy minimization using Model II repulsion constants."
    }
  ],
  "notes": "The CSV must include all 14 tetragonal vanadates: CeVO4, PrVO4, NdVO4, SmVO4, EuVO4, GdVO4, TbVO4, DyVO4, HoVO4, ErVO4, TmVO4, YbVO4, LuVO4, and YVO4. LaVO4 is excluded because it is monoclinic. The checker will compare the u,v values for the three calibration compounds (YVO4, NdVO4, ErVO4) against hidden reference values within tolerance."
}
```

## How you are scored
A hidden verifier reads your `predicted_positions.csv` and independently scores it. The verifier checks that the file contains all required compounds with the correct schema. It compares the predicted (u, v) coordinates for certain key compounds against reference values that are consistent with the model; those comparisons are made with a small absolute tolerance. The full lanthanide series is also examined for physical plausibility, such as smooth monotonic trends in u and v with atomic number. Your overall reward is a weighted combination of the per‑compound match quality and the global structural consistency. Reporting numbers that cannot be obtained from a genuine lattice energy minimization will not satisfy the verifier.
