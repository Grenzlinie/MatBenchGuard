# Thermodynamic Calculation of Ellingham Diagram for RuO2 Reductions

## Problem background
In the synthesis of intermetallic RuIn<sub>3</sub> and its substitution derivatives, commercially available starting metals often contain trace amounts of oxide impurities, particularly RuO<sub>2</sub>. At the elevated temperatures used during liquid–solid reaction synthesis, these oxides can participate in redox side reactions. A key question is which metallic components present in the reaction mixture (In, Zn, and potential substituents such as Rh, Ir, and Re) are most likely to reduce the ruthenium oxide, thereby consuming that element and altering the final composition and lattice parameters of the product. A thermodynamic analysis of the relevant reduction reactions provides a basis for predicting and interpreting these effects.

## Approach
The thermodynamic favorability of each possible reduction is assessed by computing the standard Gibbs free energy change (ΔG) for the general reaction RuO<sub>2</sub> + (a/b) M → Ru + (y/b) M<sub>a</sub>O<sub>b</sub>, where M represents the reducing metal (In, Zn, Rh, Ir, Re). Standard enthalpies of formation, entropies, and temperature-dependent heat capacity corrections for all solid and liquid species are obtained from public thermochemical databases. Because indium melts at 430 K and zinc melts at 693 K, the calculations must use the appropriate thermodynamic data for the condensed phase present at each temperature (solid below the melting point, liquid above). By evaluating ΔG for each reaction across a wide temperature range (300–1000 K) and normalizing all values to one mole of RuO<sub>2</sub>, the relative reductant strength of the different metals can be compared in an Ellingham-type diagram, revealing which oxides are most stable and which reductions are thermodynamically preferred.

## Reproduction target
Compute the standard Gibbs free energy change ΔG for the reduction of RuO<sub>2</sub> by each metal M = In, Zn, Rh, Ir, Re according to the reaction RuO<sub>2</sub> + (a/b) M → Ru + (y/b) M<sub>a</sub>O<sub>b</sub>, normalized to one mole of RuO<sub>2</sub>. Perform the calculation at temperatures from 300 K to 1000 K, at a minimum of 10 equally spaced points, taking into account the phase changes of indium and zinc (liquid above 430 K and 693 K, respectively). Record the results in a CSV file with columns: the balanced reduction reaction string, the temperature in Kelvin, and the computed ΔG in kJ per mole of RuO<sub>2</sub>. From this dataset, determine which reduction reactions are thermodynamically favorable over the temperature range by comparing the relative magnitudes of ΔG.

## Assets

- Standard Thermochemical Data: https://janaf.nist.gov/

## Workflow steps

### Step 1: Define reactions and gather thermochemical data
- Role: process
- Action: Define the balanced reduction reactions (RuO2 + (a/b)M → Ru + (y/b)M_aO_b for M = In, Zn, Rh, Ir, Re, normalized to one mole of RuO2). Gather temperature-dependent Gibbs free energy data for all solid and liquid species from public thermochemical databases, accounting for the phase transitions of In (m.p. 430 K) and Zn (m.p. 693 K).
- Evidence: `/app/outputs/reactions_and_data.json`

### Step 2: Compute Ellingham diagram data
- Role: scored
- Action: Compute the Gibbs free energy change ΔG for each reduction reaction at temperatures from 300 to 1000 K (at least 10 equally spaced points). Normalize all values to one mole of RuO2. Account for liquid-phase corrections for In and Zn above their melting points. Output the results in a CSV file.
- Output file: `/app/outputs/thermo_results.csv`
- Format: csv
- Contract: CSV with columns: reduction_reaction (string, e.g., 'RuO2 + 4/3 In -> Ru + 2/3 In2O3'), temperature_K (float), delta_G_kJ_per_mol (float). One row per reaction per temperature point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_results.csv
- path: `/app/outputs/thermo_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing the computed Gibbs free energy change for each reduction reaction at multiple temperatures. The checker will verify the relative ordering of the reactions to confirm thermodynamic favorability.
- schema:
  - `type`: table
  - `required_columns`: `reduction_reaction`, `temperature_K`, `delta_G_kJ_per_mol`
  - `units`:
    - `temperature_K`: K
    - `delta_G_kJ_per_mol`: kJ/mol

Notes: The relative ordering of the ΔG values for the different reduction reactions is a key structural property that will be assessed by the verifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduction_reaction",
          "temperature_K",
          "delta_G_kJ_per_mol"
        ],
        "units": {
          "temperature_K": "K",
          "delta_G_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "CSV file containing the computed Gibbs free energy change for each reduction reaction at multiple temperatures. The checker will verify the relative ordering of the reactions to confirm thermodynamic favorability."
    }
  ],
  "notes": "The relative ordering of the ΔG values for the different reduction reactions is a key structural property that will be assessed by the verifier."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage. The main scored artifact (thermo_results.csv) is evaluated structurally: the verifier groups the ΔG values by temperature and checks the relative ordering among the different reduction reactions to verify that the computed thermodynamic favorability is physically consistent across the entire temperature range. The process evidence (reactions_and_data.json) may also be inspected to confirm that the correct reactions and data sources were used. The final reward is a weighted combination of these stage scores; reporting a single number is not sufficient—the structural relationships in the data must be correct.
