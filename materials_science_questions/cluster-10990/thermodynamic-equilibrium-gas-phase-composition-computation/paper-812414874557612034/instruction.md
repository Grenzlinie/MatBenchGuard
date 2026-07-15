# Thermochemistry of gaseous LiO and Li₂O from equilibrium vapor pressure data

## Problem background
Lithium oxide (Li₂O) is a candidate tritium breeder material for fusion reactors, and understanding the vaporization behavior and thermochemical stability of its gaseous species (LiO, Li₂O, …) is essential for modelling high-temperature material transport and containment compatibility. Accurate heats of formation and atomization energies of these molecules provide fundamental thermodynamic data used in reactor design and safety analysis. This task aims to derive these quantities for gaseous LiO and Li₂O from equilibrium vapor pressure measurements over solid Li₂O.

## Approach
The derivation employs the third‑law thermodynamic method. From the provided partial pressures of Li, Li₂, LiO, and Li₂O over Li₂O(s) at several temperatures, equilibrium constants are calculated for two key reactions: Li₂O(s) ⇌ Li(g) + LiO(g) and Li₂O(g) ⇌ Li(g) + LiO(g). Free‑energy functions (Δ(G_T–H₀)/T) for Li₂O(s), Li₂O(g), Li(g), and LiO(g) are obtained from the publicly available JANAF Thermochemical Tables. Combining these functions with the equilibrium constants yields per‑temperature third‑law enthalpies (ΔH⁰₀) for each reaction; averaging them gives the reaction enthalpy at 0 K. Standard reference heats of formation (ΔHf⁰ for Li₂O(s), Li(g), O(g)) from JANAF are then used to derive the heats of formation of LiO(g) and Li₂O(g) and their atomization energies (D⁰). No measured or reported final values are used within the computation; all quantities are recomputed from the inputs.

## Reproduction target
Using the provided vapor pressure data (vapor_pressures.csv), the experimental calibration constants (constants.json), and free‑energy functions from the JANAF tables, perform a third‑law analysis to compute the following and write them to a structured JSON file:
- Per‑temperature third‑law enthalpies (ΔH⁰₀) and their averages for the reactions Li₂O(s) → Li(g) + LiO(g) and Li₂O(g) → Li(g) + LiO(g).
- The heats of formation ΔHf⁰(LiO,g) and ΔHf⁰(Li₂O,g).
- The atomization energies D⁰(LiO) and D⁰(Li₂O).
All energies must be reported in kcal/mol.

## Assets

- Vapor pressure data of Li, Li₂, LiO, Li₂O over Li₂O(s)
- Experimental parameters and calibration constants
- JANAF Thermochemical Tables, 2nd ed.

## Workflow steps

### Step 1: Derive thermochemistry of LiO and Li₂O
- Role: scored (load-bearing)
- Action: Using the provided vapor pressure data (vapor_pressures.csv) and experimental constants (constants.json), together with free‑energy functions (Δ(G_T–H_0)/T) for Li₂O(s), Li₂O(g), Li(g), and LiO(g) retrieved from the JANAF tables, compute equilibrium constants for the reactions Li₂O(s) → Li(g)+LiO(g) and Li₂O(g) → Li(g)+LiO(g) at each temperature. Perform a third‑law analysis to obtain the per‑temperature enthalpies ΔH⁰₀ and their averages for both reactions. Combine these with standard heats of formation (ΔHf⁰(Li₂O,s), ΔHf⁰(Li,g), ΔHf⁰(O,g) from JANAF) to derive the heat of formation ΔHf⁰(LiO,g) and ΔHf⁰(Li₂O,g) and the atomization energies D⁰(LiO) and D⁰(Li₂O). Write the complete results to a JSON file.
- Output file: `/app/outputs/thermochemistry_results.json`
- Format: json
- Contract: A JSON object with keys 'reaction_enthalpies' (object with keys 'Li2O(s)->Li+LiO' and 'Li2O(g)->Li+LiO', each containing 'average_DeltaH0' (kcal/mol, float), 'standard_deviation' (float), and 'values' (array of floats, per‑temperature ΔH⁰₀ in kcal/mol)), 'heat_of_formation' (object with keys 'LiO_g' and 'Li2O_g', each containing 'DeltaH0_0' (kcal/mol, float) and 'uncertainty' (float)), and 'atomization_energy' (object with keys 'LiO' and 'Li2O', each containing 'D0_0' (kcal/mol, float) and 'uncertainty' (float)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermochemistry_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermochemistry_results.json
- path: `/app/outputs/thermochemistry_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Structured thermochemistry results: third‑law reaction enthalpies, heats of formation, and atomization energies for LiO(g) and Li₂O(g).
- schema:
  - `type`: object
  - `required`:
    - `reaction_enthalpies`:
      - `type`: object
      - `required_keys`: `Li2O(s)->Li+LiO`, `Li2O(g)->Li+LiO`
      - `value_schema`:
        - `average_DeltaH0`: float (kcal/mol)
        - `standard_deviation`: float
        - `values`: array of floats (kcal/mol)
    - `heat_of_formation`:
      - `type`: object
      - `required_keys`: `LiO_g`, `Li2O_g`
      - `value_schema`:
        - `DeltaH0_0`: float (kcal/mol)
        - `uncertainty`: float
    - `atomization_energy`:
      - `type`: object
      - `required_keys`: `LiO`, `Li2O`
      - `value_schema`:
        - `D0_0`: float (kcal/mol)
        - `uncertainty`: float

Notes: The agent must retrieve free‑energy functions from the publicly available JANAF tables. The number of temperature points in the 'values' arrays should match the provided vapor pressures (16 entries). All energies are in kcal/mol.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermochemistry_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "reaction_enthalpies": {
            "type": "object",
            "required_keys": [
              "Li2O(s)->Li+LiO",
              "Li2O(g)->Li+LiO"
            ],
            "value_schema": {
              "average_DeltaH0": "float (kcal/mol)",
              "standard_deviation": "float",
              "values": "array of floats (kcal/mol)"
            }
          },
          "heat_of_formation": {
            "type": "object",
            "required_keys": [
              "LiO_g",
              "Li2O_g"
            ],
            "value_schema": {
              "DeltaH0_0": "float (kcal/mol)",
              "uncertainty": "float"
            }
          },
          "atomization_energy": {
            "type": "object",
            "required_keys": [
              "LiO",
              "Li2O"
            ],
            "value_schema": {
              "D0_0": "float (kcal/mol)",
              "uncertainty": "float"
            }
          }
        }
      },
      "description": "Structured thermochemistry results: third‑law reaction enthalpies, heats of formation, and atomization energies for LiO(g) and Li₂O(g)."
    }
  ],
  "notes": "The agent must retrieve free‑energy functions from the publicly available JANAF tables. The number of temperature points in the 'values' arrays should match the provided vapor pressures (16 entries). All energies are in kcal/mol."
}
```

## How you are scored
A hidden verifier independently recomputes the same thermodynamic quantities from your submitted JSON artifact and compares them to a hidden reference derived from the same input data and JANAF functions. The reward reflects agreement of the per‑temperature enthalpies, the averages, and the final heats of formation and atomization energies, with higher weight on the headline quantities. Structural consistency (correct keys, array lengths) is also checked. You are not required to hit any pre‑known numeric value; the evaluation only depends on whether your computation correctly follows the third‑law procedure with the given inputs.
