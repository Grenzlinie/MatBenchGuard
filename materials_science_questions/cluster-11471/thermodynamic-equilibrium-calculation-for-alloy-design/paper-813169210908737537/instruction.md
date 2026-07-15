## Problem background

Duplex stainless steel UNS S31803 possesses a two-phase microstructure (ferrite and austenite) whose pitting corrosion resistance is determined by the chemical composition of the individual phases. A widely used quantitative metric is the pitting resistance equivalent number (PREN), defined as:

$$\text{PREN} = \%\text{Cr} + 3.3\,\%\text{Mo} + 16\,\%\text{N}$$

where the compositions are in weight percent. The solution treatment temperature alters the partitioning of Cr, Mo and N between ferrite and austenite, thereby changing the PREN of each phase. Understanding how PREN varies with temperature is key to optimizing heat treatment for maximum corrosion resistance.

## Approach

You will use CALPHAD (Calculation of Phase Diagrams) software to compute the equilibrium phase compositions and then calculate the PREN of ferrite (BCC) and austenite (FCC) at four solution treatment temperatures. The required inputs are:

- Bulk alloy composition of UNS S31803:   
  Cr = 22.46 wt%, Ni = 5.39 wt%, Mo = 3.11 wt%, N = 0.18 wt%.
- Solution treatment temperatures: 1050 °C, 1100 °C, 1150 °C, 1200 °C.

You will run equilibrium calculations with an open‑source CALPHAD engine (OpenCalphad) and a thermodynamic database that covers the Fe–Cr–Ni–Mo–N system. From the equilibrium state you extract the weight percentages of Cr, Mo and N in the ferrite and austenite phases at each temperature. Finally you compute PREN using the formula above for each phase at every temperature and report the results in a structured CSV file.

The evaluation will check whether the obtained PREN values follow certain structural trends, which are expected from the physics of element partitioning and the known effect of temperature on phase stability.

## Reproduction target / evaluation requirement

Produce a CSV file (`pren_results.csv`) containing the computed PREN and the underlying phase compositions. Your submission will be scored by a hidden verifier that inspects the structural properties of the reported values. The verifier will check whether the PREN curves exhibit physically consistent trends that reflect the expected repartitioning of elements between phases as temperature changes. No specific gold values are provided; the task is to demonstrate physically plausible, internally consistent results.

## Assets

- **OpenCalphad** – Open‑source CALPHAD software.  
  Access: https://github.com/OpenCalphad/OpenCalphad
- **Fe‑based thermodynamic database** – A database file covering the Fe–Cr–Ni–Mo–N system, such as TCFE8 or an equivalent available from the OpenCalphad databases page.  
  Access: https://opencalphad.com/databases.html
  The solver must download a suitable database file from this source.

## Workflow steps

### Step 1: Perform CALPHAD equilibrium calculations
- Role: process
- Action: Using OpenCalphad and a Fe‑based thermodynamic database, compute equilibrium phase fractions and compositions for the given bulk alloy at the four specified temperatures. Extract the equilibrium weight percentages of Cr, Mo and N in ferrite (BCC) and austenite (FCC). Save the raw extraction results (temperature, phase, composition data) as a structured file for evidence.
- Evidence: `/app/outputs/phase_eq.json`

### Step 2: Compute PREN values
- Role: scored (load‑bearing)
- Action: From the extracted equilibrium phase compositions, calculate PREN = %Cr + 3.3 × %Mo + 16 × %N for each phase at each temperature. Write the results to a CSV file with one row per phase per temperature.
- Output file: `/app/outputs/pren_results.csv`
- Format: csv
- Contract: Columns: `Temperature` (integer, °C), `Phase` (string, “ferrite” or “austenite”), `Cr_wt` (float, wt%), `Mo_wt` (float, wt%), `N_wt` (float, wt%), `PREN` (float, dimensionless). Exactly eight rows (four temperatures × two phases).
- Scoring: hidden structural audit.

## Output files

- `/app/outputs/phase_eq.json` (process evidence)
- `/app/outputs/pren_results.csv` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pren_results.csv
- path: `/app/outputs/pren_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV containing one row per phase per solution temperature; used to verify the physical consistency of the computed PREN values.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Phase`, `Cr_wt`, `Mo_wt`, `N_wt`, `PREN`
  - `units`:
    - `Temperature`: °C
    - `Phase`: none
    - `Cr_wt`: wt%
    - `Mo_wt`: wt%
    - `N_wt`: wt%
    - `PREN`: dimensionless

Notes: The hidden verifier will check the physical consistency of the PREN trends rather than comparing to a specific gold value. The load‑bearing flag on step 2 links it to the process step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pren_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Phase",
          "Cr_wt",
          "Mo_wt",
          "N_wt",
          "PREN"
        ],
        "units": {
          "Temperature": "°C",
          "Phase": "none",
          "Cr_wt": "wt%",
          "Mo_wt": "wt%",
          "N_wt": "wt%",
          "PREN": "dimensionless"
        }
      },
      "description": "CSV containing one row per phase per solution temperature; used to verify the physical consistency of the computed PREN values."
    }
  ],
  "notes": "The hidden verifier will check the physical consistency of the PREN trends rather than comparing to a specific gold value. The load‑bearing flag on step 2 links it to the process step."
}
```

## How you are scored

A hidden verifier will independently read your `pren_results.csv`. For each scored artifact (step 2) the verifier checks the structural properties described in the evaluation requirement. The final reward is a weighted combination of how well the required trends are satisfied. Self‑reported numbers that happen to match the expected trend only because of a lucky guess are insufficient; you must genuinely run the CALPHAD workflow to obtain physically consistent data.

## Self-check

After writing the output file, run a quick sanity check: confirm that the number of rows is 8, that the `Phase` column contains only the two allowed strings, and that all composition values are positive and reasonable (e.g., weight fractions between 0 and 100).
