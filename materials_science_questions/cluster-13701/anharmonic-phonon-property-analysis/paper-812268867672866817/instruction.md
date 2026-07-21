# Anharmonic Phonon Frequency Decomposition

## Problem background
In crystalline solids, the temperature dependence of phonon frequencies arises from two separate effects: a pure-volume contribution due to thermal expansion, and a pure-temperature contribution due to anharmonic phonon‑phonon interactions (self-energy). Separating these contributions helps to understand the underlying anharmonicities. A common experimental approach is to measure the isobaric temperature derivative of a phonon frequency, the isothermal pressure derivative, and to combine them with independent measurements of the volume thermal expansion coefficient β and the isothermal compressibility κ. At a given temperature, the pure-volume and pure-temperature contributions can then be obtained from these quantities. This task applies that decomposition to four Raman‑active modes of anatase TiO₂ at room temperature (293 K), using published derivative and bulk‑property data. The resulting pure-volume and pure-temperature terms quantify how much of the total temperature‑induced frequency change is caused by thermal expansion versus anharmonicity.

## Approach
The isobaric temperature derivative (∂lnω/∂T)_P can be written as the sum of a pure-volume term −(β/κ)(∂lnω/∂P)_T and a pure-temperature term (∂lnω/∂T)_V. Therefore, given the numerically tabulated values of β, κ, and for each Raman mode its frequency, isobaric temperature derivative, and isothermal pressure derivative, one can compute the pure-volume contribution and then obtain the pure-temperature contribution by subtraction. The inputs are all provided in the workflow step; no additional data retrieval or preprocessing is required. The computation is straightforward arithmetic, and the results are written directly to a CSV file with one row per mode.

## Reproduction target
For the four Raman modes v1 (639 cm⁻¹), v4 (399 cm⁻¹), v5 (197 cm⁻¹), and v6 (144 cm⁻¹) of anatase TiO₂ at 293 K, compute the pure-volume contribution (in units of 10⁻⁵ K⁻¹) and the pure-temperature contribution (in the same units) using the provided β, κ, and mode-specific derivative values. Write the results as a CSV file with columns: mode (string), frequency (float, cm⁻¹), pure_volume_contribution (float, 10⁻⁵ K⁻¹), pure_temperature_contribution (float, 10⁻⁵ K⁻¹).

**Unit conversion**: The formulas directly yield values in units of K⁻¹. To obtain the required output units of 10⁻⁵ K⁻¹, divide each computed value (in K⁻¹) by 10⁻⁵ (equivalently, multiply by 10⁵).

## Assets
No external datasets, files, or tools are needed. All required numerical inputs (β, κ, and the per‑mode frequency and derivative values) are provided directly in the workflow step. Only standard Python libraries (e.g., csv or pandas) are needed to read the inputs and write the CSV output.

## Workflow steps

### Step 1: Compute the 293 K decomposition
- Role: scored (load-bearing)
- Action: Using the following input values: volume thermal expansion coefficient β = 14.7 × 10⁻⁶ K⁻¹, isothermal compressibility κ = 6.09 × 10⁻⁴ kbar⁻¹, and the per‑mode frequency, isobaric temperature derivative (∂lnω/∂T)ₚ, and isothermal pressure derivative (∂lnω/∂P)ₜ listed below:
  • v1: ω=639 cm⁻¹, (∂lnω/∂T)ₚ = −2.68×10⁻⁵ K⁻¹, (∂lnω/∂P)ₜ = 0.62×10⁻³ kbar⁻¹
  • v4: ω=399 cm⁻¹, (∂lnω/∂T)ₚ = −0.25×10⁻⁵ K⁻¹, (∂lnω/∂P)ₜ = 0.68×10⁻³ kbar⁻¹
  • v5: ω=197 cm⁻¹, (∂lnω/∂T)ₚ = 4.78×10⁻⁵ K⁻¹, (∂lnω/∂P)ₜ = −0.12×10⁻³ kbar⁻¹
  • v6: ω=144 cm⁻¹, (∂lnω/∂T)ₚ = 21.96×10⁻⁵ K⁻¹, (∂lnω/∂P)ₜ = 2.17×10⁻³ kbar⁻¹
Compute, for each mode, the raw pure‑volume contribution = −(β/κ) × (∂lnω/∂P)ₜ (unit K⁻¹) and the raw pure‑temperature contribution = (∂lnω/∂T)ₚ − (raw pure‑volume contribution) (unit K⁻¹). Then convert each to the required units of 10⁻⁵ K⁻¹ by dividing by 10⁻⁵ (multiplying by 10⁵). Write the results to decomposition_293K.csv.
- Output file: `/app/outputs/decomposition_293K.csv`
- Format: csv
- Contract: CSV with columns: mode (string), frequency (float, cm⁻¹), pure_volume_contribution (float, 10⁻⁵ K⁻¹), pure_temperature_contribution (float, 10⁻⁵ K⁻¹). All values in the output columns must be expressed after the unit conversion.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/decomposition_293K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### decomposition_293K.csv
- path: `/app/outputs/decomposition_293K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed pure-volume and pure-temperature contributions for each mode, reported in units of 10⁻⁵ K⁻¹ (i.e., the raw K⁻¹ values divided by 10⁻⁵).
- schema:
  - `type`: table
  - `required_columns`: `mode`, `frequency`, `pure_volume_contribution`, `pure_temperature_contribution`
  - `units`:
    - `frequency`: cm⁻¹
    - `pure_volume_contribution`: 10⁻⁵ K⁻¹
    - `pure_temperature_contribution`: 10⁻⁵ K⁻¹

Notes: All required numerical inputs are provided explicitly in the task instruction and workflow step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "decomposition_293K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "frequency",
          "pure_volume_contribution",
          "pure_temperature_contribution"
        ],
        "units": {
          "frequency": "cm⁻¹",
          "pure_volume_contribution": "10⁻⁵ K⁻¹",
          "pure_temperature_contribution": "10⁻⁵ K⁻¹"
        }
      },
      "description": "Computed pure-volume and pure-temperature contributions for each mode, reported in units of 10⁻⁵ K⁻¹ (i.e., the raw K⁻¹ values divided by 10⁻⁵)."
    }
  ],
  "notes": "All required numerical inputs are provided explicitly in the task instruction and workflow step."
}
```

## How you are scored
A hidden verifier reads your output file `/app/outputs/decomposition_293K.csv` and compares each reported `pure_volume_contribution` and `pure_temperature_contribution` value against the independently known correct values for those modes. The comparison uses a fixed tolerance appropriate for deterministic arithmetic. You receive a score between 0 and 1 based on the fraction of the eight values (2 contributions × 4 modes) that fall within the tolerance. The CSV must have exactly the columns described in the output contract; format errors may reduce the score. You must produce the file at the exact path; no other files are scored.