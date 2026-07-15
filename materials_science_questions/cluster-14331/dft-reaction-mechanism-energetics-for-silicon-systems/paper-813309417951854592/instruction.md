# Catalytic Hydrosilylation Activation Barriers via Quantum Chemistry

## Problem background
Hydrosilylation of carbonyl compounds using silanes is an important catalytic transformation for the synthesis of protected alcohols. Transition-metal complexes can catalyze this reaction under mild conditions, but the relative reactivity of different carbonyl substrates (aldehydes, ketones, esters) varies significantly. Understanding why some substrates react faster than others is crucial for catalyst design and synthetic planning. Computational quantum chemistry provides a route to rationalize these reactivity trends by calculating the activation barriers for the rate-determining step of the catalytic cycle, thus giving a quantitative link between electronic structure and observed kinetics.

## Approach
The catalytic cycle proposed in this work involves activation of a rhenium-silyl complex, coordination of the carbonyl, a silyl-transfer step that forms a new carbon‑oxygen bond, and subsequent silane-assisted product release. The silyl‑transfer step is thought to be rate‑determining. To study its energetics, the entire catalytic cycle is first optimized using model substrates silane (SiH4) and formaldehyde (CH2O) at the MP2 level with the LANL2DZ basis set. This yields the key intermediate (the rhenium silyl species) and confirms the thermodynamic feasibility of the cycle. Next, for a set of four representative carbonyls—formaldehyde, benzaldehyde, acetone, and methyl formate—transition state searches are performed for the silyl‑transfer step. Each transition state is located, validated by a single imaginary frequency, and the activation energy Ea is computed as the difference between the transition state energy and the separated reactants (Re(CO)4SiH3 + carbonyl). The resulting barriers can then be compared across substrates to rationalize the observed relative rates.

## Reproduction target
Compute the activation energies (Ea, in kJ/mol) for the silyl‑transfer transition state TS1 for the four carbonyl substrates: formaldehyde, benzaldehyde, acetone, and methyl formate. Write the results to `/app/outputs/activation_energies.json` as a JSON object with keys `formaldehyde`, `benzaldehyde`, `acetone`, and `methyl_formate`, each a numeric value in kJ/mol.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- LANL2DZ basis set

## Workflow steps

### Step 1: Full catalytic cycle optimization (SiH4+CH2O)
- Role: process
- Action: Perform MP2/LANL2DZ geometry optimization and frequency calculation for all intermediates and transition states of the catalytic cycle using SiH4 and CH2O as model substrates. Compute energies and vibrational frequencies to establish the structure of the key intermediate Re(CO)4SiH3 and to confirm thermodynamic feasibility.
- Evidence: `/app/outputs/cycle_results.log`

### Step 2: Activation barrier calculations for TS1
- Role: scored (load-bearing)
- Action: Using the optimized Re(CO)4SiH3 structure and the carbonyl substrates formaldehyde, benzaldehyde, acetone, and methyl formate, perform MP2/LANL2DZ transition state searches for the silyl-transfer step (TS1). Compute the activation energy Ea as the energy difference between the transition state and the separated reactants (Re(CO)4SiH3 + carbonyl). Write the computed barriers in kJ/mol to a JSON file.
- Output file: `/app/outputs/activation_energies.json`
- Format: json
- Contract: JSON object with keys 'formaldehyde', 'benzaldehyde', 'acetone', 'methyl_formate', each a numeric value in kJ/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.json
- path: `/app/outputs/activation_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Activation energies (Ea) for the silyl-transfer transition state TS1 for formaldehyde, benzaldehyde, acetone, and methyl formate. Values are in kJ/mol and are compared to hidden reference values with a relative tolerance and an ordering check (aldehydes < ketone < ester).
- schema:
  - `type`: object
  - `required`:
    - `formaldehyde`: number
    - `benzaldehyde`: number
    - `acetone`: number
    - `methyl_formate`: number
  - `units`:
    - `formaldehyde`: kJ/mol
    - `benzaldehyde`: kJ/mol
    - `acetone`: kJ/mol
    - `methyl_formate`: kJ/mol

Notes: The task reproduces only the computational part of the paper. The solving agent must use an open-source quantum chemistry package (ORCA or Psi4) with the MP2/LANL2DZ level of theory. No experimental synthesis or photolysis is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "formaldehyde": "number",
          "benzaldehyde": "number",
          "acetone": "number",
          "methyl_formate": "number"
        },
        "units": {
          "formaldehyde": "kJ/mol",
          "benzaldehyde": "kJ/mol",
          "acetone": "kJ/mol",
          "methyl_formate": "kJ/mol"
        }
      },
      "description": "Activation energies (Ea) for the silyl-transfer transition state TS1 for formaldehyde, benzaldehyde, acetone, and methyl formate. Values are in kJ/mol and are compared to hidden reference values with a relative tolerance and an ordering check (aldehydes < ketone < ester)."
    }
  ],
  "notes": "The task reproduces only the computational part of the paper. The solving agent must use an open-source quantum chemistry package (ORCA or Psi4) with the MP2/LANL2DZ level of theory. No experimental synthesis or photolysis is required."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. For the activation energies, your computed values are compared to reference values using appropriate tolerances to account for differences between quantum chemistry implementations. In addition, the verifier checks that the relative ordering of the four barriers (which substrates have higher or lower barriers) is consistent with the experimentally observed trend in hydrosilylation rates. The final reward combines these checks, with the largest weight given to the accuracy of the computed activation energies.
