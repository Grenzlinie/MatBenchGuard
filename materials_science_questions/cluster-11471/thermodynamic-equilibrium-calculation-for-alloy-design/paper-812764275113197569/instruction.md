# CALPHAD Corundum Mass Fraction at 1400°C for Fe-Cr-Co Steel

## Problem background
High-chromium heat-resistant steels can form non-metallic inclusions during solidification, which influence mechanical properties. Aluminum is often added as a deoxidizer, leading to the formation of corundum (Al₂O₃) particles. Thermodynamic models based on the CALPHAD method can predict the equilibrium mass fraction of such inclusion phases at a given temperature. This task focuses on computing how the corundum mass fraction at 1400°C depends on the cobalt content in an Fe-18Cr-2Ni-1Mo-0.2C-0.2Mn-0.1Si steel containing 0.1 wt% Al. Understanding this dependence is important for alloy design, as cobalt is known to affect the phase stability and inclusion formation in these steels.

## Approach
The CALPHAD (CALculation of PHAse Diagrams) approach uses a thermodynamic database to minimise the Gibbs free energy of a multicomponent system and compute equilibrium phase fractions. The workflow employs the open-source pycalphad package with a suitable Fe-based thermodynamic database (e.g., TCFE). The alloy composition is defined, and an equilibrium calculation is performed at a fixed temperature (1400°C). From the resulting phase assemblage, the mass fraction of the corundum (Al₂O₃) phase is extracted. This procedure is repeated for three different cobalt concentrations (3, 6, and 12 wt%) while keeping all other elemental concentrations constant.

## Reproduction target
Using pycalphad and the TCFE thermodynamic database, compute the equilibrium mass fraction of the corundum (Al₂O₃) phase at 1400°C for the alloy Fe-18Cr-2Ni-1Mo-0.2C-0.2Mn-0.1Si with 0.1 wt% Al and cobalt contents of 3%, 6%, and 12% (by weight). Write the results to a CSV file with columns `Co_percent` and `corundum_mass_frac`.

## Assets

- pycalphad Python package: pycalphad
- TCFE thermodynamic database

## Workflow steps

### Step 1: Compute corundum mass fractions at 1400°C
- Role: scored (load-bearing)
- Action: Using pycalphad and a suitable Fe-based thermodynamic database (e.g., TCFE), define the thermodynamic system for the alloy composition Fe-18Cr-2Ni-1Mo-0.2C-0.2Mn-0.1Si with 0.1 wt% Al and cobalt contents of 3, 6, and 12 wt%. For each composition, perform an equilibrium calculation at 1400°C, extract the mass fraction of the corundum (Al₂O₃) phase, and write the results to a CSV file.
- Output file: `/app/outputs/corundum_mass_frac_1400C.csv`
- Format: csv
- Contract: CSV with header row: Co_percent,corundum_mass_frac. Three rows with Co_percent = 3, 6, 12. corundum_mass_frac is a dimensionless float (mass fraction).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/corundum_mass_frac_1400C.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### corundum_mass_frac_1400C.csv
- path: `/app/outputs/corundum_mass_frac_1400C.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV with three rows (Co=3,6,12%) and columns Co_percent, corundum_mass_frac. The checker verifies that corundum_mass_frac is positive and within [1e-6, 0.05].
- schema:
  - `type`: table
  - `required_columns`: `Co_percent`, `corundum_mass_frac`
  - `units`:
    - `Co_percent`: wt%
    - `corundum_mass_frac`: dimensionless

Notes: The checker performs a structural audit: it verifies the presence of rows for Co=3,6,12, checks that all mass fractions are within a plausible range, and verifies a required structural relationship between the three values. No exact numeric gold is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "corundum_mass_frac_1400C.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Co_percent",
          "corundum_mass_frac"
        ],
        "units": {
          "Co_percent": "wt%",
          "corundum_mass_frac": "dimensionless"
        }
      },
      "description": "CSV with three rows (Co=3,6,12%) and columns Co_percent, corundum_mass_frac. The checker verifies that corundum_mass_frac is positive and within [1e-6, 0.05]."
    }
  ],
  "notes": "The checker performs a structural audit: it verifies the presence of rows for Co=3,6,12, checks that all mass fractions are within a plausible range, and verifies a required structural relationship between the three values. No exact numeric gold is required."
}
```

## How you are scored
A hidden verifier reads your CSV file and assigns a score based on whether the file meets the required properties specified in the output contract: correct columns and rows, positive mass fractions within a plausible range, and the required structural relationship among the three compositions. The verifier does not simply compare your numbers to a single target value; it checks for scientific consistency across the results. Reporting values that mimic the literature without actually running the computation will not pass these checks.
