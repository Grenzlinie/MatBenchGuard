# Constrained carbon equilibrium calculation for alloy design

## Problem background
During the quench-and-partition (Q&P) heat treatment of steels, carbon can partition from martensite (usually modeled as ferrite) into retained austenite while substitutional alloying elements remain frozen in place. This carbon enrichment stabilizes the austenite, allowing high strength combined with good ductility. Predicting how much carbon ends up in the austenite is essential for alloy design, but the full thermodynamic equilibrium is often not achieved because the interface between ferrite and austenite is immobile. The constrained carbon equilibrium (CCE) model was introduced to describe this situation, and it has been extended to general multicomponent steels. The present task computes the CCE carbon concentration in austenite for a series of ternary Fe–X–C alloys and for several transformation‑induced plasticity (TRIP) steel compositions under given processing conditions, to evaluate how substitutional solutes and processing temperatures influence the final carbon enrichment. The resulting carbon concentrations are open quantities to be computed from the thermodynamic model.

## Approach
The CCE model fixes the amounts and substitutional composition of ferrite and austenite (derived from a known retained‑austenite fraction), then finds the carbon distribution that gives equal carbon chemical potential in both phases, without allowing substitutional elements to redistribute. This requires evaluating the carbon chemical potential as a function of carbon content for each phase using a CALPHAD thermodynamic database, and locating the point where the two curves intersect. The workflow: (1) Implement a CCE solver using pycalphad and a publicly available Fe‑alloy database. (2) Apply the solver to eight ternary Fe–1 wt% X –0.5 wt% C alloys (X = Al, Cr, Cu, Mn, Mo, Ni, Si, P) at a partitioning temperature of 400 °C with 10 vol% retained austenite, recording the austenite carbon concentration. (3) For a set of TRIP steels, first perform an unconstrained equilibrium calculation at the intercritical temperature to obtain the equilibrium austenite volume fraction; then run the CCE solver at the austempering temperature with that fraction to compute the carbon concentration in retained austenite. The final outputs are two CSV tables summarizing these computed quantities.

## Reproduction target
Produce two CSV files under `/app/outputs`:  
`cce_alloying_elements.csv` – for each of the eight ternary Fe–1%X–0.5%C alloys, give the CCE carbon concentration in austenite (wt%) at 400 °C with 0.10 volume fraction retained austenite. The table must include columns for the alloy element, temperature, austenite volume fraction, and the computed carbon concentration.  
`cce_trip_steels.csv` – for each of the eight TRIP steel conditions, after first computing the unconstrained equilibrium austenite volume fraction at the given intercritical temperature, give the CCE carbon concentration in retained austenite at the given austempering temperature. The table must include the steel label, nominal composition, intercritical temperature, austempering temperature, the calculated austenite volume fraction, and the CCE carbon concentration.  
The goal is to produce these computed concentrations from the thermodynamic model; the values themselves are not prescribed.

## Assets

- Python 3: python3
- pycalphad: https://pypi.org/project/pycalphad/
- Fe‑alloy CALPHAD database
- Scientific Python stack: numpy, scipy, pandas

## Workflow steps

### Step 1: Implement CCE solver
- Role: process
- Action: Implement a constrained carbon equilibrium (CCE) solver using pycalphad and a publicly available Fe‑alloy thermodynamic database. The solver must accept an alloy composition (wt%), a retained‑austenite volume fraction, a partitioning temperature, and the database. It models martensite as ferrite, fixes substitutional composition in each phase, computes carbon chemical potential curves as a function of moles of carbon, and finds the CCE state as the intersection of the two curves (equal carbon chemical potential). Verify the solver on a simple Fe‑0.5 wt% C alloy at several austenite fractions and save a short test log.
- Evidence: `/app/outputs/evidence_CCE_solver_test.log`

### Step 2: CCE for ternary Fe‑X‑C alloys
- Role: scored
- Action: For each substitutional solute X in (Al, Cr, Cu, Mn, Mo, Ni, Si, P), prepare a bulk alloy composition Fe–1 wt% X –0.5 wt% C. Run the CCE solver at a partitioning temperature of 400°C with a retained‑austenite volume fraction of 0.10 (10%). Record the resulting carbon concentration in austenite (wt%) in a CSV file.
- Output file: `/app/outputs/cce_alloying_elements.csv`
- Format: csv
- Contract: CSV with header: Alloy_element,Temperature_C,Austenite_vol_fraction,C_austenite_wt. Eight rows (one per alloy element). Temperature in °C, carbon concentration in wt%.
- Scoring: scored by hidden verifier

### Step 3: Unconstrained equilibrium for TRIP steels
- Role: process
- Action: For each of the eight TRIP steel compositions and intercritical temperatures given in the task description, compute the thermodynamic equilibrium (unconstrained, no carbide precipitation) using pycalphad and the Fe‑alloy database. Determine the equilibrium volume fraction of austenite at the intercritical temperature. Save the computed austenite fractions for use in the next step, and optionally output a log.
- Evidence: `/app/outputs/evidence_unconstrained_TRIP.log`

### Step 4: CCE for TRIP steels
- Role: scored (load-bearing)
- Action: Using the austenite volume fraction obtained in step 03 for each TRIP steel, run the CCE solver at the given austempering temperature to compute the carbon concentration in retained austenite (wt%). Output the results as a CSV file.
- Output file: `/app/outputs/cce_trip_steels.csv`
- Format: csv
- Contract: CSV with header: Steel_label,Composition,Intercritical_T_C,Austempering_T_C,V_gamma_calc,C_austenite_CCE_wt. Eight rows. Temperature in °C, volume fraction dimensionless, carbon concentration in wt%.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cce_alloying_elements.csv`
- `/app/outputs/cce_trip_steels.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cce_alloying_elements.csv
- path: `/app/outputs/cce_alloying_elements.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CCE carbon concentration in austenite for eight ternary Fe‑1%X‑0.5%C alloys, used to verify the solver and reproduce the alloying effect trends.
- schema:
  - `type`: table
  - `required_columns`: `Alloy_element`, `Temperature_C`, `Austenite_vol_fraction`, `C_austenite_wt`
  - `units`:
    - `Temperature_C`: °C
    - `Austenite_vol_fraction`: dimensionless
    - `C_austenite_wt`: wt%

### cce_trip_steels.csv
- path: `/app/outputs/cce_trip_steels.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CCE carbon concentration in retained austenite for eight TRIP steels, compared against paper‑reported values and trend checks (T0 and paraequilibrium).
- schema:
  - `type`: table
  - `required_columns`: `Steel_label`, `Composition`, `Intercritical_T_C`, `Austempering_T_C`, `V_gamma_calc`, `C_austenite_CCE_wt`
  - `units`:
    - `Intercritical_T_C`: °C
    - `Austempering_T_C`: °C
    - `V_gamma_calc`: dimensionless
    - `C_austenite_CCE_wt`: wt%

Notes: The checker compares the submitted carbon concentrations to the expected thermodynamic values and evaluates required relative trends among alloying elements. Scoring tolerates legitimate differences arising from the choice of thermodynamic database, while still enforcing the reported qualitative orderings and approximate magnitudes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cce_alloying_elements.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Alloy_element",
          "Temperature_C",
          "Austenite_vol_fraction",
          "C_austenite_wt"
        ],
        "units": {
          "Temperature_C": "°C",
          "Austenite_vol_fraction": "dimensionless",
          "C_austenite_wt": "wt%"
        }
      },
      "description": "CCE carbon concentration in austenite for eight ternary Fe‑1%X‑0.5%C alloys, used to verify the solver and reproduce the alloying effect trends."
    },
    {
      "file": "cce_trip_steels.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Steel_label",
          "Composition",
          "Intercritical_T_C",
          "Austempering_T_C",
          "V_gamma_calc",
          "C_austenite_CCE_wt"
        ],
        "units": {
          "Intercritical_T_C": "°C",
          "Austempering_T_C": "°C",
          "V_gamma_calc": "dimensionless",
          "C_austenite_CCE_wt": "wt%"
        }
      },
      "description": "CCE carbon concentration in retained austenite for eight TRIP steels, compared against paper‑reported values and trend checks (T0 and paraequilibrium)."
    }
  ],
  "notes": "The checker compares the submitted carbon concentrations to the expected thermodynamic values and evaluates required relative trends among alloying elements. Scoring tolerates legitimate differences arising from the choice of thermodynamic database, while still enforcing the reported qualitative orderings and approximate magnitudes."
}
```

## How you are scored
A hidden verifier will independently evaluate the artifacts from each scored workflow stage and combine the stage‑level rewards into an overall score (weighted, total 1.0). The verifier checks the computed carbon concentrations against thermodynamic expectations and validates qualitative consistency (for example, relative trends among different alloying elements). It does not require exact agreement with any single reported number, as numerical values depend on the specific thermodynamic database employed. The primary checks are whether the submitted values fall within plausible ranges and whether the relative ordering of elements respects known thermodynamic behavior. Both `cce_alloying_elements.csv` and `cce_trip_steels.csv` contribute to the final score; merely reporting values without proper execution of the CCE solver will not earn full credit.
