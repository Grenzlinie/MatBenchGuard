# Microkinetic Modeling of Dimethyl Ether Synthesis over H-Zeolite Catalyst

## Problem background
Dimethyl ether (DME) is a clean alternative fuel that can be produced by dehydration of methanol over solid-acid catalysts such as H-zeolites. The reaction mechanism involves two competing pathways: an associative (direct) route in which two methanol molecules react simultaneously to form DME and water, and a dissociative (sequential) route in which one methanol first dissociates into a surface CH3 group and water, followed by reaction with a second methanol to produce DME. Resolving which pathway dominates and identifying the rate‑determining step is essential for designing improved catalysts and processes.

## Approach
A quantum‑chemical and microkinetic modelling approach is used. First, a 4T cluster model of the H‑zeolite is built and used in MP2 calculations with the 6‑311+G(2df,2p) basis set to optimise the geometries and transition states of all gas‑phase species and adsorbed intermediates. From the resulting ZPE‑corrected energies, reaction energies (ΔE) and activation barriers (Ef, Eb) are computed for the nine elementary steps. These activation energies are then used in a microkinetic model where the pre‑exponential factors are estimated by fitting the model to experimental conversion/selectivity data from the literature (Hassanpour et al. 2010, H‑MFI90 catalyst, P=17 bar, LHSV=3.8 h⁻¹, T=240–330 °C). The fitted model is run at three temperatures (450, 475, 500 K) to compare the forward and backward rates of the two pathways, identify the dominant route, and determine the rate‑determining step.

## Reproduction target
Produce the following four deliverables from a self‑contained computational workflow:

1. A JSON file (`step_01_reaction_energies.json`) containing the reaction energy ΔE and forward/backward activation energies Ef, Eb for each of the nine elementary steps R1–R9.
2. A JSON file (`step_02_pre_exponential_factors.json`) containing the fitted forward and backward pre‑exponential factors for all nine steps.
3. A text file (`step_03_dominant_pathway.txt`) that states whether the dissociative or associative pathway is dominant and which elementary step is the rate‑determining step, with supporting reasoning based on the simulated reaction rates.
4. A CSV file (`step_04_reaction_rates.csv`) listing forward and backward reaction rates for R1–R9 at T = 450, 475, and 500 K.

All artifacts must be produced by executing the computational pipeline, not by copying numbers from the literature.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Python scientific computing stack (numpy, scipy, matplotlib, pandas): numpy scipy matplotlib pandas
- Experimental data from Hassanpour et al. (2010): 10.1016/j.fuproc.2010.07.003
- 6-311+G(2df,2p) basis set
- 4T H-zeolite cluster model description

## Workflow steps

### Step 1: Build 4T H-zeolite cluster model
- Role: process
- Action: Construct the 4T cluster model (H3Si–O–AlH2–(OH)–SiH2–O–SiH3) with appropriate initial geometry. Save the coordinates in a format suitable for subsequent quantum chemistry input.
- Evidence: `/app/outputs/cluster.xyz`

### Step 2: MP2 geometry optimizations and transition‑state searches
- Role: process
- Action: Using an open-source quantum chemistry package (e.g., ORCA) with the MP2 method and 6-311+G(2df,2p) basis set, optimize geometries for all gas‑phase species (CH3OH, CH3OCH3, H2O) and all adsorbed intermediates (CH3OH‑H‑Z, H2O‑CH3‑Z, CH3‑Z, CH3OH‑CH3‑Z, CH3OCH3‑H‑Z, CH3OH‑CH3OH‑H‑Z, CH3OCH3‑H2O‑H‑Z). Locate transition states for reactions R2, R5, and R8. Verify minima (no imaginary frequency) and transition states (exactly one imaginary frequency). Compute ZPE‑corrected total energies for each species.
- Evidence: `/app/outputs/mp2_energies.json`

### Step 3: Compute reaction and activation energies
- Role: scored
- Action: From the MP2 total energies, calculate reaction energies (ΔE) and forward/backward activation energies (Ef, Eb) for all nine elementary steps R1–R9. Write the values to step_01_reaction_energies.json.
- Output file: `/app/outputs/step_01_reaction_energies.json`
- Format: json
- Contract: {"type":"object","properties":{"R1":{"ΔE":"float (eV)","Ef":"float (eV)","Eb":"float (eV)"},"R2":{...},"R3":{...},"R4":{...},"R5":{...},"R6":{...},"R7":{...},"R8":{...},"R9":{...}}}
- Scoring: scored by hidden verifier

### Step 4: Estimate pre‑exponential factors by fitting experimental data
- Role: process
- Action: Implement the microkinetic model (ODE system describing site fractions). Using the activation energies from the previous step as fixed, estimate the 16 pre‑exponential factors (A) by fitting the molar flow rates of DME and methanol at the reactor outlet to the digitized experimental data from Hassanpour et al. (2010) for the H‑MFI90 catalyst (P=17 bar, LHSV=3.8 h⁻¹, T=240–330°C). Use appropriate optimization (e.g., genetic algorithm) to minimize a relative error objective function.
- Evidence: `/app/outputs/fitting_log.txt`

### Step 5: Output estimated pre‑exponential factors
- Role: scored
- Action: Extract the fitted pre‑exponential factors and save to step_02_pre_exponential_factors.json.
- Output file: `/app/outputs/step_02_pre_exponential_factors.json`
- Format: json
- Contract: {"type":"object","properties":{"R1":{"Af":"float","Ab":"float"},"R2":{...},"R3":{...},"R4":{...},"R5":{...},"R6":{...},"R7":{...},"R8":{...},"R9":{...}}}
- Scoring: scored by hidden verifier

### Step 6: Run microkinetic simulations
- Role: process
- Action: Using the estimated pre‑exponential factors and MP2 activation energies, solve the microkinetic model under the experimental conditions (P=17 bar, LHSV=3.8 h⁻¹) at temperatures T = 450, 475, 500 K. Compute site fractions, forward and backward reaction rates for all nine steps, and DME desorption rates for R6 and R9. Save intermediate simulation output (e.g., arrays) for subsequent analysis.
- Evidence: `/app/outputs/simulation_output.npz`

### Step 7: Determine dominant pathway and rate‑determining step
- Role: scored (load-bearing)
- Action: Analyze the simulated reaction rates: compare DME desorption rates from R6 (dissociative) and R9 (associative) to see which pathway produces DME; examine relative forward rates to identify the slowest step. Write the conclusion (dominant pathway and RDS) to step_03_dominant_pathway.txt.
- Output file: `/app/outputs/step_03_dominant_pathway.txt`
- Format: txt
- Contract: Text file containing a clear statement, e.g., 'Dominant pathway: dissociative. Rate‑determining step: R5 (CH3OH‑CH3‑Z → CH3OCH3‑H‑Z).'
- Scoring: scored by hidden verifier

### Step 8: Output reaction rates at selected temperatures
- Role: scored
- Action: From the simulation results, extract forward reaction rates (r_f) and backward reaction rates (r_b) for reactions R1–R9 at T = 450, 475, 500 K. For reactions R3 and R9 that have no backward rate, record the backward rate as 0 or null. Write the data to step_04_reaction_rates.csv.
- Output file: `/app/outputs/step_04_reaction_rates.csv`
- Format: csv
- Contract: CSV with columns: Temperature (K), Reaction_number (R1..R9), r_f (s⁻¹), r_b (s⁻¹). R3 and R9 have backward rate 0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_reaction_energies.json`
- `/app/outputs/step_02_pre_exponential_factors.json`
- `/app/outputs/step_03_dominant_pathway.txt`
- `/app/outputs/step_04_reaction_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_reaction_energies.json
- path: `/app/outputs/step_01_reaction_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reaction energies and activation barriers for all nine elementary steps, to be compared with the paper's reported values within hidden tolerances (±0.1 eV for barriers, ±0.05 eV for ΔE).
- schema:
  - `type`: object
  - `required`:
    - `R1`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R2`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R3`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R4`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R5`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R6`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R7`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R8`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)
    - `R9`:
      - `ΔE`: float (eV)
      - `Ef`: float (eV)
      - `Eb`: float (eV)

### step_02_pre_exponential_factors.json
- path: `/app/outputs/step_02_pre_exponential_factors.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted pre‑exponential factors for all forward and backward reactions, compared in log-scale order of magnitude.
- schema:
  - `type`: object
  - `required`:
    - `R1`:
      - `Af`: float
      - `Ab`: float
    - `R2`:
      - `Af`: float
      - `Ab`: float
    - `R3`:
      - `Af`: float
      - `Ab`: float
    - `R4`:
      - `Af`: float
      - `Ab`: float
    - `R5`:
      - `Af`: float
      - `Ab`: float
    - `R6`:
      - `Af`: float
      - `Ab`: float
    - `R7`:
      - `Af`: float
      - `Ab`: float
    - `R8`:
      - `Af`: float
      - `Ab`: float
    - `R9`:
      - `Af`: float
      - `Ab`: float

### step_03_dominant_pathway.txt
- path: `/app/outputs/step_03_dominant_pathway.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Text file containing the conclusion about the dominant reaction pathway and the rate-determining step, to be checked for internal consistency and correct identification.
- schema:
  - `type`: text
  - `required`: `statement identifying the dominant pathway (dissociative or associative) and the rate-determining step with supporting reason`

### step_04_reaction_rates.csv
- path: `/app/outputs/step_04_reaction_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elementary forward and backward reaction rates for R1–R9 at T=450, 475, 500 K, to be compared with reference rates and relative ordering.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `Reaction_number`, `r_f (s⁻¹)`, `r_b (s⁻¹)`

Notes: All scored artifacts are derived from the computational pipeline. The hidden checker compares the computed energies, pre-exponential factors, and reaction rates against the paper's reported values with appropriate tolerances, and verifies the pathway conclusion through structural content checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_reaction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R1": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R2": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R3": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R4": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R5": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R6": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R7": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R8": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          },
          "R9": {
            "ΔE": "float (eV)",
            "Ef": "float (eV)",
            "Eb": "float (eV)"
          }
        }
      },
      "description": "Reaction energies and activation barriers for all nine elementary steps, to be compared with the paper's reported values within hidden tolerances (±0.1 eV for barriers, ±0.05 eV for ΔE)."
    },
    {
      "file": "step_02_pre_exponential_factors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R1": {
            "Af": "float",
            "Ab": "float"
          },
          "R2": {
            "Af": "float",
            "Ab": "float"
          },
          "R3": {
            "Af": "float",
            "Ab": "float"
          },
          "R4": {
            "Af": "float",
            "Ab": "float"
          },
          "R5": {
            "Af": "float",
            "Ab": "float"
          },
          "R6": {
            "Af": "float",
            "Ab": "float"
          },
          "R7": {
            "Af": "float",
            "Ab": "float"
          },
          "R8": {
            "Af": "float",
            "Ab": "float"
          },
          "R9": {
            "Af": "float",
            "Ab": "float"
          }
        }
      },
      "description": "Fitted pre‑exponential factors for all forward and backward reactions, compared in log-scale order of magnitude."
    },
    {
      "file": "step_03_dominant_pathway.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": [
          "statement identifying the dominant pathway (dissociative or associative) and the rate-determining step with supporting reason"
        ]
      },
      "description": "Text file containing the conclusion about the dominant reaction pathway and the rate-determining step, to be checked for internal consistency and correct identification."
    },
    {
      "file": "step_04_reaction_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "Reaction_number",
          "r_f (s⁻¹)",
          "r_b (s⁻¹)"
        ]
      },
      "description": "Elementary forward and backward reaction rates for R1–R9 at T=450, 475, 500 K, to be compared with reference rates and relative ordering."
    }
  ],
  "notes": "All scored artifacts are derived from the computational pipeline. The hidden checker compares the computed energies, pre-exponential factors, and reaction rates against the paper's reported values with appropriate tolerances, and verifies the pathway conclusion through structural content checks."
}
```

## How you are scored
A hidden verifier independently scores each of the four output artifacts. The reaction energies and pre‑exponential factors are compared against reference values (with appropriate tolerances), the dominant pathway statement is checked for logical consistency with the submitted rates, and the reaction rate table is compared to expected values and relative ordering. Artifacts that merely quote a known number without a genuine execution of the pipeline will receive little or no credit. The per‑artifact scores are combined into a final reward, with the pathway and rate‑determining‑step conclusion carrying the largest weight.
