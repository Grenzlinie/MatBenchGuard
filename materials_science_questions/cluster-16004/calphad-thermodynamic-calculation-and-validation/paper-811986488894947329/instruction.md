# Viscosity Calculation for Fe‑Metalloid Liquids from Heat of Vaporization and Ionic Radii

## Problem background
Liquid viscosity governs reaction and crystallisation kinetics in molten alloys, but it is challenging to measure experimentally, especially at high temperatures and for multi‑component systems. A practical semi‑empirical calculation method has been proposed that combines the Eyring hole‑theory of viscosity with an empirical ionic‑size correction. The apparent activation energy of viscosity Ev is linked to the heat of vaporization and to the ratio of ionic to atomic radii, making it possible to estimate Ev from readily available elemental properties. When extended to alloys, the method incorporates thermodynamic mixing data, allowing prediction of temperature‑dependent liquid viscosities for iron‑metalloid systems. This task focuses on the Fe–17 at.% B alloy: from published physical constants and two hypothetical mixing‑energy assumptions, you will compute the alloy activation energy and derive viscosity equations that cover both the stable liquid range and the deeply supercooled region, producing quantitative predictions that can be compared with reference values.

## Approach
The calculation rests on two building blocks.  (1) For each pure element, the apparent activation energy of viscosity Ev is obtained from the heat of vaporization Evap, the ionic radius r*i, and the atomic radius r*a through empirical relational equations that distinguish metallic and covalent bond types.  (2) For an alloy, Ev is modelled as a weighted sum of the elemental Ev values plus a free energy of mixing Fm, whose magnitude is taken here from analogy with the Fe–C system under two extreme assumptions (half or twice the Fe–C mixing energy).

Once the alloy Ev is known, the pre‑exponential factor η0 of the Arrhenius viscosity equation is estimated from a log‑log correlation between η0 and Ev derived from literature data on liquid alloys. The Arrhenius coefficients a = log10(η0) and b = Ev/(R·ln10) then define the viscosity as η(T) = η0·exp(Ev/(RT)). Liquid viscosities at two reference temperatures (the melting point and a higher temperature) are computed with this equation.

To describe the supercooled liquid viscosity, the three‑parameter Fulcher equation log10(η) = A + B/(T − T0) is fitted to three points: the two liquid viscosities from the previous step plus the conventional assumption that the viscosity at the glass transition temperature Tg = 760 K equals 10¹⁵ mPa·s. Solving the resulting system of three equations yields A, B, and T0 for each mixing‑energy case. All required elemental properties (radii, heats of vaporization) are provided in the task assets, and the computational workflow proceeds through the ordered steps listed below.

## Reproduction target
For the Fe–17 at.% B alloy, perform the following:
- Compute the apparent activation energy of viscosity Ev for two free‑energy‑of‑mixing assumptions: Fm = −5.31 kJ mol⁻¹ (case 1) and Fm = −21.24 kJ mol⁻¹ (case 2).
- Derive the Arrhenius viscosity equation coefficients a and b (log η = a + b/T) for each case.
- Fit the Fulcher supercooled‑liquid viscosity equation coefficients A, B, T0 (log η = A + B/(T − T0)) for each case, using the viscosities at T = 1462 K, T = 1562 K, and the condition that η(Tg=760 K) = 10¹⁵ mPa·s.
- Report the liquid viscosity (mPa·s) at 1462 K and at 1562 K for both mixing‑energy assumptions.

All outputs must be written to the specified files under /app/outputs as detailed in the workflow steps below.

## Assets

- Properties of Elemental Materials (Tata McGraw‑Hill, 1972): The required heat of vaporization, ionic radii, and atomic radii are as follows (units: kJ mol⁻¹ for heat of vaporization, Å for radii):
  * Fe: heat of vaporization = 354.1 kJ mol⁻¹, ionic radius r*i = 0.78 Å, atomic radius r*a = 1.26 Å
  * C: heat of vaporization = 711 kJ mol⁻¹, ionic radius r*i = 0.16 Å, atomic radius r*a = 0.77 Å
  * P: heat of vaporization = 78.65 kJ mol⁻¹, ionic radius r*i = 0.38 Å, atomic radius r*a = 1.10 Å
  * B: heat of vaporization = 565 kJ mol⁻¹, ionic radius r*i = 0.23 Å, atomic radius r*a = 0.88 Å

## Workflow steps

### Step 1: Compute elemental activation energies Ev
- Role: process
- Action: Using the provided ionic radii (r*i), atomic radii (r*a), and heats of vaporization (Evap) for Fe, C, P, and B, compute the apparent activation energy of viscosity Ev for each element from the empirical size‑dependence relations. For Fe (metallic bond) apply log[(Evap/Ev)(r*i/r*a)^3] = 4.98 log(r*i/r*a) + 2.35. For C, P, B (covalent bond) apply log[(Evap/Ev)(r*i/r*a)^3] = 3.44 log(r*i/r*a) + 1.15. Store the four computed Ev values (kJ/mol).
- Evidence: `/app/outputs/elemental_Ev.json`

### Step 2: Calculate alloy activation energy Ev for Fe‑17 at.% B
- Role: scored (load-bearing)
- Action: Using the elemental Ev from step‑01, compute the alloy activation energy Ev for Fe‑17 at.% B under two mixing‑energy assumptions: case1 Fm = ‑5.31 kJ/mol (half of the Fe‑C mixing energy), case2 Fm = ‑21.24 kJ/mol (twice of the Fe‑C mixing energy). Apply Ev_alloy = X(Fe)·Ev(Fe) + X(B)·Ev(B) + Fm with mole fractions X(Fe)=0.83, X(B)=0.17. Write the two Ev values (in kJ/mol) to the output CSV.
- Output file: `/app/outputs/step_01_Ev_results.csv`
- Format: csv
- Contract: columns: case (string: case1, case2), Ev_kJ_per_mol (float)
- Scoring: scored by hidden verifier

### Step 3: Derive viscosity equation coefficients and supercooled‑liquid parameters
- Role: scored
- Action: For each case, transform Ev to J/mol and compute the pre‑exponential factor η0 (mPa·s) from log10(η0) = -3.30·log10(Ev) + 14.6. Obtain the Arrhenius coefficients: a = log10(η0), b = Ev/(R·ln(10)) with R=8.314 J/(mol·K). Use the Arrhenius equation η(T)=η0·exp(Ev/(RT)) to evaluate the liquid viscosity at T=1462 K and T=1562 K. Then fit the Fulcher equation log10(η) = A + B/(T‑T0) to the three points (1462 K, 1562 K, Tg=760 K) under the conventional assumption that the viscosity at the glass transition is 1e15 mPa·s. Solve for A, B, T0 for each case and write all coefficients as JSON.
- Output file: `/app/outputs/step_02_viscosity_eq_coefficients.json`
- Format: json
- Contract: object with keys Arrhenius_case1 {a: float, b: float}, Arrhenius_case2 {a: float, b: float}, Fulcher_case1 {A: float, B: float, T0: float}, Fulcher_case2 {A: float, B: float, T0: float}
- Scoring: scored by hidden verifier

### Step 4: Compute liquid viscosity at reference temperatures
- Role: scored
- Action: Using the Arrhenius coefficients from step_03 (or recomputing directly from Ev), calculate the liquid viscosity η (mPa·s) for each case at T = 1462 K and T = 1562 K. Write the four values as JSON.
- Output file: `/app/outputs/step_03_viscosity_at_temps.json`
- Format: json
- Contract: object with keys viscosity_case1_1462K (float, mPa·s), viscosity_case1_1562K (float), viscosity_case2_1462K (float), viscosity_case2_1562K (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_Ev_results.csv`
- `/app/outputs/step_02_viscosity_eq_coefficients.json`
- `/app/outputs/step_03_viscosity_at_temps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_Ev_results.csv
- path: `/app/outputs/step_01_Ev_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Alloy activation energy Ev for Fe‑17 at.% B under two mixing assumptions. The checker recomputes Ev from the elemental Ev values (computed from the given property constants) and the stated Fm assumptions, and compares with a tolerance of 0.1 kJ/mol.
- schema:
  - `type`: table
  - `required_columns`: `case`, `Ev_kJ_per_mol`
  - `units`:
    - `Ev_kJ_per_mol`: kJ/mol

### step_02_viscosity_eq_coefficients.json
- path: `/app/outputs/step_02_viscosity_eq_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Arrhenius and Fulcher viscosity equation coefficients for Fe‑17 at.% B alloy. The checker re‑computes the coefficients from the same Ev values and the same fitting procedure (using η(Tg)=1e15 mPa·s) and compares with tolerances of ±0.001 for A/a, ±1 for b/B/T0.
- schema:
  - `type`: object
  - `required`:
    - `Arrhenius_case1`:
      - `a`: float (log10 mPa·s)
      - `b`: float (K)
    - `Arrhenius_case2`:
      - `a`: float
      - `b`: float
    - `Fulcher_case1`:
      - `A`: float
      - `B`: float (K)
      - `T0`: float (K)
    - `Fulcher_case2`:
      - `A`: float
      - `B`: float
      - `T0`: float

### step_03_viscosity_at_temps.json
- path: `/app/outputs/step_03_viscosity_at_temps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Liquid viscosity at 1462 K and 1562 K for Fe‑17 at.% B alloy. The checker recomputes from the Arrhenius coefficients and compares with relative tolerance 2%.
- schema:
  - `type`: object
  - `required`:
    - `viscosity_case1_1462K`: float (mPa·s)
    - `viscosity_case1_1562K`: float
    - `viscosity_case2_1462K`: float
    - `viscosity_case2_1562K`: float

Notes: The task reproduces the viscosity calculation method for Fe‑17 at.% B. The critical cooling rate stage is omitted. The provided elemental constants now appear explicitly in the instruction, and the hidden verifier uses the same constants to recompute all scored artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_Ev_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "Ev_kJ_per_mol"
        ],
        "units": {
          "Ev_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Alloy activation energy Ev for Fe‑17 at.% B under two mixing assumptions. The checker recomputes Ev from the elemental Ev values (computed from the given property constants) and the stated Fm assumptions, and compares with a tolerance of 0.1 kJ/mol."
    },
    {
      "file": "step_02_viscosity_eq_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Arrhenius_case1": {
            "a": "float (log10 mPa·s)",
            "b": "float (K)"
          },
          "Arrhenius_case2": {
            "a": "float",
            "b": "float"
          },
          "Fulcher_case1": {
            "A": "float",
            "B": "float (K)",
            "T0": "float (K)"
          },
          "Fulcher_case2": {
            "A": "float",
            "B": "float",
            "T0": "float"
          }
        }
      },
      "description": "Arrhenius and Fulcher viscosity equation coefficients for Fe‑17 at.% B alloy. The checker re‑computes the coefficients from the same Ev values and the same fitting procedure (using η(Tg)=1e15 mPa·s) and compares with tolerances of ±0.001 for A/a, ±1 for b/B/T0."
    },
    {
      "file": "step_03_viscosity_at_temps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "viscosity_case1_1462K": "float (mPa·s)",
          "viscosity_case1_1562K": "float",
          "viscosity_case2_1462K": "float",
          "viscosity_case2_1562K": "float"
        }
      },
      "description": "Liquid viscosity at 1462 K and 1562 K for Fe‑17 at.% B alloy. The checker recomputes from the Arrhenius coefficients and compares with relative tolerance 2%."
    }
  ],
  "notes": "The task reproduces the viscosity calculation method for Fe‑17 at.% B. The critical cooling rate stage is omitted. The provided elemental constants now appear explicitly in the instruction, and the hidden verifier uses the same constants to recompute all scored artifacts."
}
```

## How you are scored
A hidden verifier independently recomputes every scored artifact using the same public constants and the same computational procedure. It compares your reported values against its own recomputed results, not against hardcoded targets from the task description. The verifier checks each output file — the alloy Ev values, the Arrhenius and Fulcher coefficients, and the viscosities at the two temperatures — using tolerances appropriate for an independent recalculation, and combines the per‑stage scores (weighted as specified by the hidden rubric) into a final reward between 0 and 1. Simply writing known literature numbers without performing the computation will not pass, because the verifier’s recomputation follows precisely the equations and constants listed in the public instruction.
