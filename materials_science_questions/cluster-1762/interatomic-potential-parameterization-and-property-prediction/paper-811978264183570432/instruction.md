## Problem background

The isothermal bulk modulus is a key input for interatomic potential parameterization of ionic materials. For mixed crystals (solid solutions), a simple linear interpolation of the end-member bulk moduli with composition does not capture the physical dependence on molar volume changes. A physically motivated formula that uses the end-member moduli and molar volume ratios yields more realistic bulk modulus values for mixed crystals. This task computes the bulk modulus of the CaF2–SrF2 mixed crystal series using such a formula.

## Approach

The bulk modulus B of the mixed crystal is given by:

$$B = \frac{1 + x\left(\frac{v_2}{v_1} - 1\right)}{1 + x\left(\frac{B_1}{B_2}\frac{v_2}{v_1} - 1\right)} B_1$$

where x is the mole fraction of SrF2 (the second end-member), B1 = 814 kbar and B2 = 693 kbar are the isothermal bulk moduli of pure CaF2 and SrF2, respectively, and the molar volume ratio v2/v1 is obtained from the nearest-neighbor distances r0 of the end members in the cubic fluorite structure:

$$v_2/v_1 = (r_{0,\mathrm{SrF}_2} / r_{0,\mathrm{CaF}_2})^3$$

with r0(CaF2) = 0.23655 nm and r0(SrF2) = 0.25096 nm.

Evaluate this formula for the nine compositions listed below; the mole fraction x of SrF2 is shown in parentheses. The computed bulk modulus must be expressed in kbar.

Compositions:
- CaF2 (0.0)
- Ca90Sr10F2 (0.1)
- Ca80Sr20F2 (0.2)
- Ca70Sr30F2 (0.3)
- Ca50Sr50F2 (0.5)
- Ca40Sr60F2 (0.6)
- Ca30Sr70F2 (0.7)
- Ca10Sr90F2 (0.9)
- SrF2 (1.0)

## Reproduction target

Compute the isothermal bulk modulus B (in kbar) for each of the nine compositions using the formula and constants above. Write the result to a CSV file with columns `composition` and `B_kbar`. The order of rows must follow the composition list above (pure CaF2 first, increasing Sr content, pure SrF2 last).

## Assets

- **End-member parameters**: B1 = 814 kbar, B2 = 693 kbar, r0(CaF2) = 0.23655 nm, r0(SrF2) = 0.25096 nm, and the nine mole fractions (provided in the instruction).
- **Python 3**: standard environment with basic math support; no external libraries are required.

## Workflow steps

### Step 1: Prepare input data
- Role: process
- Action: Gather the given end-member bulk moduli (B1, B2), nearest-neighbor distances (r0 values), and the target compositions with their mole fractions x.
- Evidence: none

### Step 2: Compute isothermal bulk moduli
- Role: scored (load-bearing)
- Action: For each composition, calculate the bulk modulus B using the formula  B = (1 + x*(v2/v1 - 1)) / (1 + x*((B1/B2)*(v2/v1) - 1)) * B1, with v2/v1 = (r0,SrF2 / r0,CaF2)^3. Use the mole fraction x as given. Write a CSV file containing the composition name and the computed B_kbar value.
- Output file: `/app/outputs/computed_bulk_moduli.csv`
- Format: csv
- Contract: Exactly 9 rows, columns: `composition` (string), `B_kbar` (float). Row order must match the composition list (CaF2, Ca90Sr10F2, ..., SrF2).
- Scoring: scored by hidden verifier

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_bulk_moduli.csv
- path: `/app/outputs/computed_bulk_moduli.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed isothermal bulk modulus for each of the nine CaF2–SrF2 compositions. The row order must match CaF2 (0% Sr) to SrF2 (100% Sr).
- schema:
  - `type`: table
  - `required_columns`: `composition`, `B_kbar`
  - `units`:
    - `B_kbar`: kbar

Notes: The verifier recomputes the expected bulk modulus for each composition using the same formula and constants; each value is compared with an absolute tolerance. The reward is the fraction of values within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_bulk_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "B_kbar"
        ],
        "units": {
          "B_kbar": "kbar"
        }
      },
      "description": "Computed isothermal bulk modulus for each of the nine CaF2–SrF2 compositions. The row order must match CaF2 (0% Sr) to SrF2 (100% Sr)."
    }
  ],
  "notes": "The verifier recomputes the expected bulk modulus for each composition using the same formula and constants; each value is compared with an absolute tolerance. The reward is the fraction of values within tolerance."
}
```

## How you are scored

A hidden verifier computes the expected bulk modulus for each composition independently using the same formula and constants. It compares each `B_kbar` value in your CSV against the expected value with an absolute tolerance. The reward is the fraction of values within tolerance. The CSV must contain exactly the nine rows in the specified order; missing or extra rows lead to a score of zero for that stage. Reporting paper numbers without correct computation will fail the comparison.
