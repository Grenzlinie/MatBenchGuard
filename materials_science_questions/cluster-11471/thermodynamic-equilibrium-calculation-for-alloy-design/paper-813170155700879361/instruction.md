# Compute equilibrium phase intervals for two tool alloy compositions

## Problem background
Tool alloys of ledeburite type are multicomponent materials whose microstructure and properties depend on the phase constitution and the temperatures at which phase transformations occur. Computational thermodynamics based on the CALPHAD (CALculation of PHAse Diagrams) method can predict equilibrium phase assemblages, phase fractions, and transformation boundaries as functions of composition and temperature. This information is essential for alloy design and for interpreting experimental data. The present task concerns the equilibrium phase regions in two specific tool steel compositions belonging to the Fe-Cr-V-C and Fe-Cr-V-Mo-C systems.

## Approach
The CALPHAD approach models the Gibbs energy of each phase using thermodynamic descriptions parameterized from published data. The phases considered are liquid, ferrite (bcc), austenite (fcc), and the carbides MC and M7C3. The two alloy compositions are Ch3F12 (Fe-bal., 3.00 wt% Cr, 12.00 wt% V, 3.00 wt% C) and Ch12MF4 (Fe-bal., 12.06 wt% Cr, 1.20 wt% Mo, 4.00 wt% V, 2.37 wt% C). Using a provided thermodynamic database file that encodes the Gibbs energy expressions, perform equilibrium calculations with the open-source pycalphad package. For each alloy, step through temperatures from 750 K to 1700 K, computing the stable phase assemblage at each temperature. Determine the temperature intervals (start and end) over which each distinct equilibrium region exists. The expected equilibrium regions are those that involve combinations of ferrite, austenite, liquid, M7C3, and MC. The result is a set of temperature ranges for each region, which can be compared with prior theoretical predictions.

## Reproduction target
Produce a TSV file, phase_equilibrium_intervals.tsv, containing the temperature intervals for the equilibrium phase regions of both alloys. For Ch3F12, the required regions are: ferrite+MC+M7C3, ferrite+MC+M7C3+austenite, ferrite+MC+austenite, austenite+MC, austenite+MC+liquid, MC+liquid, liquid. For Ch12MF4: ferrite+MC+M7C3, ferrite+MC+M7C3+austenite, austenite+MC+M7C3, austenite+MC+M7C3+liquid, austenite+MC+liquid, austenite+liquid, liquid. Each row reports the alloy name, the region label, and the start and end temperatures in Kelvin (as integers).

## Assets

- Fe-Cr-V-C-Mo thermodynamic database (TDB file)
- pycalphad: pycalphad

## Workflow steps

### Step 1: Compute equilibrium phase intervals for Ch3F12 and Ch12MF4
- Role: scored (load-bearing)
- Action: Using pycalphad, read the bundled TDB file and define two alloy compositions: Ch3F12 (Fe-bal., 3.00 wt% Cr, 12.00 wt% V, 3.00 wt% C) and Ch12MF4 (Fe-bal., 12.06 wt% Cr, 1.20 wt% Mo, 4.00 wt% V, 2.37 wt% C). For each alloy, perform equilibrium calculations from 750 K to 1700 K with a step size of no more than 10 K. Determine the temperature intervals (start and end temperatures in K) where each phase assemblage listed in Table I is stable. Write the intervals to phase_equilibrium_intervals.tsv.
- Output file: `/app/outputs/phase_equilibrium_intervals.tsv`
- Format: tsv
- Contract: Columns: alloy (string), equilibrium_label (string), start_temperature_K (int), end_temperature_K (int). Each row corresponds to one equilibrium region. For Ch3F12: ferrite+MC+M7C3, ferrite+MC+M7C3+austenite, ferrite+MC+austenite, austenite+MC, austenite+MC+liquid, MC+liquid, liquid. For Ch12MF4: ferrite+MC+M7C3, ferrite+MC+M7C3+austenite, austenite+MC+M7C3, austenite+MC+M7C3+liquid, austenite+MC+liquid, austenite+liquid, liquid.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_equilibrium_intervals.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_equilibrium_intervals.tsv
- path: `/app/outputs/phase_equilibrium_intervals.tsv`
- format: tsv
- purpose: scored
- target_policy: reference_match
- description: Temperature intervals of equilibrium phase assemblages for Ch3F12 and Ch12MF4 alloys as computed by pycalphad. The checker will compare these intervals against hidden gold values from Table I of the paper with an allowed tolerance (not disclosed to the agent).
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `equilibrium_label`, `start_temperature_K`, `end_temperature_K`
  - `units`:
    - `start_temperature_K`: K
    - `end_temperature_K`: K

Notes: The thermodynamic database (TDB file) is provided as a bundled resource. The agent must use pycalphad to perform the calculations. No gold values or tolerances are revealed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_equilibrium_intervals.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "equilibrium_label",
          "start_temperature_K",
          "end_temperature_K"
        ],
        "units": {
          "start_temperature_K": "K",
          "end_temperature_K": "K"
        }
      },
      "description": "Temperature intervals of equilibrium phase assemblages for Ch3F12 and Ch12MF4 alloys as computed by pycalphad. The checker will compare these intervals against hidden gold values from Table I of the paper with an allowed tolerance (not disclosed to the agent)."
    }
  ],
  "notes": "The thermodynamic database (TDB file) is provided as a bundled resource. The agent must use pycalphad to perform the calculations. No gold values or tolerances are revealed."
}
```

## How you are scored
Your output file is evaluated by an automated verifier that reads the TSV and compares each reported start and end temperature to reference values. The reward is proportional to the number of intervals correctly matched across both alloys; full credit is awarded when all regions fall within an acceptable tolerance. The verifier does not expect exact agreement with any specific published table but assesses correctness based on a consistent thermodynamic model. The final score is a weighted combination of the per-stage rewards, with this scored step carrying all the weight.
