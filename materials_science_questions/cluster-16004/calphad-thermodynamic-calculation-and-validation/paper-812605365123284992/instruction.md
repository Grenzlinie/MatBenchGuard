# CALPHAD Phase Equilibrium Calculation for a Ni-Al-Cr-Mo-Pt-Re Coating Alloy

## Problem background
Superalloys with high Mo content face a significant challenge during high‑temperature service: Mo can diffuse outward from the substrate into the protective coating, where it forms volatile oxides that disrupt the thermally grown oxide scale and degrade oxidation resistance. One proposed mitigation is the addition of Re to a PtAl coating, which may act as a diffusion barrier by reacting with Mo to form a stable intermetallic phase (the σ‑MoRe phase). To assess whether such a phase is thermodynamically stable under the relevant operating conditions, phase equilibrium calculations using the CALPHAD (CALculation of PHAse Diagrams) methodology are performed on the coating composition of interest.

## Approach
The core approach is a CALPHAD‑based thermodynamic equilibrium calculation. Given the fixed coating composition (Al 23.2 at.%, Ni balance, Cr 1.0 at.%, Mo 3.8 at.%, Pt 3.2 at.%, Re 0.5 at.%), the Gibbs free energy of the system is minimized at each temperature using an open‑source CALPHAD software package and a public thermodynamic database that covers Ni, Al, Cr, Mo, Pt, and Re. The procedure yields the set of stable phases and their mole fractions at each temperature, without any fitting or training steps. The calculation is repeated for a series of temperatures spanning 900 °C to 1200 °C to capture the phase evolution, with the oxidation temperature of 1100 °C being of particular interest.

## Reproduction target
You must run the CALPHAD equilibrium calculation described above and produce a single CSV file at `/app/outputs/step_01_phase_fractions.csv` containing the results. The file must list, for each temperature (900, 950, 1000, 1050, 1100, 1150, 1200 °C), every stable phase with a mole fraction greater than 0.0001. The expected columns are `Temperature` (float, °C), `Phase` (string), and `MoleFraction` (float). A hidden verifier will evaluate the file based on whether the phase assembly at 1100 °C agrees with physically expected behaviour for this alloy system, not on a single exact numerical value.

## Assets

- pycalphad: pycalphad
- Public Ni-Al-Cr-Mo-Pt-Re thermodynamic database (TDB file): https://github.com/pycalphad/pycalphad/blob/main/pycalphad/examples/data/NiAlCrMoRe.tdb

## Workflow steps

### Step 1: CALPHAD equilibrium phase calculation
- Role: scored
- Action: Using the coating composition Al 23.2 at.%, Ni balance, Cr 1.0 at.%, Mo 3.8 at.%, Pt 3.2 at.%, Re 0.5 at.%, perform equilibrium phase calculations with pycalphad and a suitable public thermodynamic database covering Ni-Al-Cr-Mo-Pt-Re. Compute the stable phases and their mole fractions at temperatures 900, 950, 1000, 1050, 1100, 1150, and 1200 °C. Write the results to a CSV file; each row lists a phase with mole fraction > 0.0001 at a given temperature.
- Output file: `/app/outputs/step_01_phase_fractions.csv`
- Format: csv
- Contract: Columns: Temperature (float, °C), Phase (string), MoleFraction (float). Required temperatures: 900, 950, 1000, 1050, 1100, 1150, 1200. Each temperature has one row per stable phase with MoleFraction > 0.0001.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phase_fractions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phase_fractions.csv
- path: `/app/outputs/step_01_phase_fractions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Equilibrium phase fractions at each temperature from 900 to 1200 °C. Each row lists a phase with mole fraction > 0.0001 at a given temperature.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Phase`, `MoleFraction`
  - `units`:
    - `Temperature`: °C

Notes: Scoring is structural: the checker will verify that certain phase labels exist at 1100 °C with mole fraction > 0.001 (e.g., a B2 phase, an L1₂ phase, a sigma/Mo(Re) phase) and that a Re(Cr) or HCP phase label, if present, has mole fraction < 0.01. Exact fractions are not compared.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phase_fractions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Phase",
          "MoleFraction"
        ],
        "units": {
          "Temperature": "°C"
        }
      },
      "description": "Equilibrium phase fractions at each temperature from 900 to 1200 °C. Each row lists a phase with mole fraction > 0.0001 at a given temperature."
    }
  ],
  "notes": "Scoring is structural: the checker will verify that certain phase labels exist at 1100 °C with mole fraction > 0.001 (e.g., a B2 phase, an L1₂ phase, a sigma/Mo(Re) phase) and that a Re(Cr) or HCP phase label, if present, has mole fraction < 0.01. Exact fractions are not compared."
}
```

## How you are scored
A hidden verifier will read your submitted `step_01_phase_fractions.csv` and evaluate it in two stages. First, it will confirm that the file is well‑formed and contains rows for all required temperatures. Second, it will perform a structural audit of the phase composition at 1100 °C: it will check that certain expected phases are present (with a mole fraction above a threshold) and that any phase that would indicate a physically unlikely equilibrium has a negligible fraction. The verifier may also examine the temperature‑dependent trends of key phases for monotonicity. No single mole‑fraction value is compared against a fixed gold number; the scoring rewards a physically sound equilibrium calculation.
