# Compute 50 kbar Fe-Ni γ/(α+γ) boundary and eutectoid assessment

## Problem background
Iron meteorites consist primarily of Fe-Ni alloys and display a variety of microstructures (kamacite, taenite, plessite) whose formation and compositions are governed by the Fe-Ni phase diagram. The observed mineralogy and compositions are difficult to explain using the phase diagram at ambient pressure, because some phases would require quench conditions incompatible with the slow cooling expected in asteroid-sized parent bodies. A hypothesis proposes that the meteorites crystallized under high confining pressure, which shifts the phase boundaries and may resolve the discrepancies. Testing this hypothesis requires accurate Fe-Ni phase diagrams at elevated pressures. This task focuses on the 50 kilobar isobar, which is within the pressure range thought relevant. Two aspects are critical: the temperatures of the γ/(α+γ) boundary at selected Ni contents, and the presence or absence of a eutectoid (γ1+γ2 miscibility gap intersecting the boundary) at that pressure.

## Approach
The CALPHAD method provides a way to compute phase equilibria from thermodynamic models. For the Fe-Ni system, the free energies of the body-centred cubic (α) and face-centred cubic (γ) phases are expressed as functions of temperature, composition, and pressure. At atmospheric pressure, published thermodynamic assessments describe the system accurately. Pressure effects are incorporated by adding a PV term derived from molar volume data as a function of composition and temperature. The equilibrium phase boundaries are then obtained by applying the common tangent construction to the free energy curves at the desired pressure. An open-source implementation using pycalphad and a compatible thermodynamic database enables fully reproducible computation. The workflow first computes the full γ/(α+γ) boundary at 50 kbars, then extracts the transformation temperatures at the specified Ni compositions and analyzes the diagram for the presence of a eutectoid.

## Reproduction target
Using the CALPHAD approach, compute the temperature of the γ/(α+γ) phase boundary at 50 kilobars for nickel compositions of 0, 10, 20, 30, 40, 50, 55, and 60 weight percent Ni. Additionally, determine whether a miscibility gap in the γ phase (γ1+γ2) intersects the γ/(α+γ) boundary at this pressure, i.e., whether a eutectoid is present. The results must be written to the specified output files.

## Assets

- pycalphad (open-source CALPHAD Python library): pycalphad
- Fe-Ni thermodynamic database (SGTE-compatible TDB or FEDEMO): pycalphad (bundled FEDEMO database or downloadable SGTE sources)

## Workflow steps

### Step 1: Compute 50-kbar Fe-Ni phase boundaries
- Role: process
- Action: Set up the Fe-Ni system in pycalphad with an appropriate public thermodynamic database, incorporating molar volume data to account for the 50 kbar pressure effect. Compute the equilibrium phase boundaries (specifically the γ/(α+γ) transus) as a function of temperature and composition across the full Fe-Ni range. Save the raw phase boundary data for audit.
- Evidence: `/app/outputs/phase_boundaries_50kbar.csv`

### Step 2: Extract boundary temperatures at specified Ni contents
- Role: scored (load-bearing)
- Action: From the computed 50-kbar phase boundaries, extract the γ/(α+γ) transformation temperature at Ni compositions of 0, 10, 20, 30, 40, 50, 55, and 60 wt% Ni. Write the results to table1_depressions.csv.
- Output file: `/app/outputs/table1_depressions.csv`
- Format: csv
- Contract: CSV with header row: Ni_wtPct, T_50kbar_C. Eight data rows, one per composition; both columns float.
- Scoring: scored by hidden verifier

### Step 3: Determine eutectoid presence at 50 kbars
- Role: scored (load-bearing)
- Action: Analyze the full 50-kbar phase diagram to verify whether a γ1+γ2 miscibility gap intersects the γ/(α+γ) phase boundary (i.e., whether a eutectoid is present). Write the conclusion to eutectoid_check.txt.
- Output file: `/app/outputs/eutectoid_check.txt`
- Format: txt
- Contract: A single line of text, exactly one of: 'Eutectoid present at 50 kbars: YES' or 'Eutectoid present at 50 kbars: NO'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1_depressions.csv`
- `/app/outputs/eutectoid_check.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1_depressions.csv
- path: `/app/outputs/table1_depressions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The γ/(α+γ) phase boundary temperature at 50 kbars for each of the eight Ni compositions specified in the paper. The checker compares each T_50kbar_C value to a hidden reference derived from the paper, with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Ni_wtPct`, `T_50kbar_C`
  - `items`:
    - `Ni_wtPct`: float
    - `T_50kbar_C`: float

### eutectoid_check.txt
- path: `/app/outputs/eutectoid_check.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Boolean verdict stating whether a eutectoid (γ1+γ2 field intersecting the γ/(α+γ) boundary) appears in the 50 kbar phase diagram. The checker compares the line to a hidden gold reference.
- schema:
  - `type`: text
  - `required`: line_text

Notes: The agent must compute the Fe-Ni phase diagram at 50 kbars from a public thermodynamic database, then extract the required data. The checker reads the agent's numeric values and string verdict and compares them to hidden gold values derived from the paper. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1_depressions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ni_wtPct",
          "T_50kbar_C"
        ],
        "items": {
          "Ni_wtPct": "float",
          "T_50kbar_C": "float"
        }
      },
      "description": "The γ/(α+γ) phase boundary temperature at 50 kbars for each of the eight Ni compositions specified in the paper. The checker compares each T_50kbar_C value to a hidden reference derived from the paper, with an appropriate tolerance."
    },
    {
      "file": "eutectoid_check.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": "line_text"
      },
      "description": "Boolean verdict stating whether a eutectoid (γ1+γ2 field intersecting the γ/(α+γ) boundary) appears in the 50 kbar phase diagram. The checker compares the line to a hidden gold reference."
    }
  ],
  "notes": "The agent must compute the Fe-Ni phase diagram at 50 kbars from a public thermodynamic database, then extract the required data. The checker reads the agent's numeric values and string verdict and compares them to hidden gold values derived from the paper. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your submission is evaluated automatically against hidden reference data. The verifier reads table1_depressions.csv and compares each T_50kbar_C value to the corresponding expected value; credit for that part scales with the accuracy of your computed temperatures. The eutectoid_check.txt file is checked for agreement with the hidden verdict. The overall reward is the weighted sum of the scores from both checks. The tolerances and the exact weighting are not disclosed. Note that reporting arbitrary numbers will not succeed; only a genuine thermodynamic calculation produces the required values.
