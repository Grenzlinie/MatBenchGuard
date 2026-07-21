# DFT Li Adsorption Energies on Curved and N-Doped Carbon Models

## Problem background
Carbon-based materials with curved layers and nitrogen doping have shown promise for high-capacity Li-ion battery anodes, but the atomic-scale mechanism of Li adsorption on such structures needs quantification. First-principles density functional theory (DFT) with dispersion corrections (DFT-D2) can provide adsorption energies that reveal how curvature of sp² carbon layers and the type of nitrogen dopant affect Li binding. Understanding these effects is key to designing better electrode materials. This task measures Li adsorption energies on a set of controlled molecular models to isolate the roles of curvature and pyrrolic/pyridinic nitrogen doping.

## Approach
The reproduction uses an open-source DFT code with Grimme D2 dispersion correction to compute Li adsorption energies. Five molecular models are constructed from the descriptions below:
1. Bowl-shaped C30H10 (half of a fullerene cage, edges saturated with H) – Li adsorbed on the inner concave side.
2. Flat C30H14 (a graphene fragment with H-saturated edges) – Li adsorbed at the center.
3. Pristine C60 – Li adsorbed on the outer and inner sides.
4. Defective C54N4 with four pyrrolic N atoms (all-N5).
5. Defective C54N4 with two pyridinic N (N6) and two pyrrolic N.
For each model, both the bare fragment and the Li-adsorbed complex are geometry-optimized until forces and total energy are converged. The adsorption energy is then obtained as E_ads = E_total(complex) – E_total(bare) – E_isolated_Li, with all energies calculated consistently at the DFT-D2 level. This computational protocol allows quantitative assessment of the effects of curvature and nitrogen doping on Li binding strength.

## Reproduction target
Compute the Li adsorption energy (in eV) for each of the five models described above. Report all values in a single JSON file as specified in Step 2. Your results will be automatically evaluated against a set of expected physical trends and approximate magnitude ranges derived from the computational protocol, without revealing exact target values. The computation must be performed using DFT-D2 with geometry optimization as described.

## Assets

- Open-source DFT code with Grimme D2: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Construct molecular models and perform DFT-D2 geometry optimizations
- Role: process
- Action: Build initial atomic coordinates for the five molecular systems: (i) bowl-like C30H10 (half-C60 with edges saturated with H), (ii) flat C30H14 (graphene fragment with saturated edges), (iii) pristine C60 (outer and inner adsorption), (iv) C54N4 with four pyrrolic N atoms (all-N5), (v) C54N4 with two pyridinic N and two pyrrolic N atoms. For each system, place a single Li atom at the specified adsorption site (inner center for bowl, center for flat, outer/inner for C60, center of defect for doped models). Using an open-source DFT code with Grimme D2 dispersion correction, perform geometry optimization of the bare model and the Li-adsorbed complex until forces and total energy are converged. Save optimized total energies for later use.
- Evidence: none

### Step 2: Compute Li adsorption energies
- Role: scored (load-bearing)
- Action: For each model, calculate the Li adsorption energy as E_ads = E_total(complex) - E_total(bare) - E_isolated_Li using the converged total energies from step_01. Report all values in eV in the specified JSON file.
- Output file: `/app/outputs/li_adsorption_energies.json`
- Format: json
- Contract: JSON object with exactly the following string keys mapped to floats (adsorption energy in eV, negative for favorable binding): 'bowl_C30H10_inner', 'flat_C30H14', 'C60_inner', 'C60_outer', 'C54N4_all_N5', 'C54N4_two_N5_two_N6'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/li_adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### li_adsorption_energies.json
- path: `/app/outputs/li_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lithium adsorption energies computed with DFT-D2 for the five molecular models. The values are compared to the paper-reported values and checked for structural trends (curved > flat, N-doped > undoped, mixed doping > all-N5) using hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `bowl_C30H10_inner`: number
    - `flat_C30H14`: number
    - `C60_inner`: number
    - `C60_outer`: number
    - `C54N4_all_N5`: number
    - `C54N4_two_N5_two_N6`: number

Notes: The hidden checker reads the agent's reported energies and compares each value to the paper's reference within ±0.3 eV, then verifies the following structural relationships: (1) bowl_C30H10_inner < flat_C30H14 (curved binds stronger), (2) both C54N4 entries < C60_inner, (3) C54N4_two_N5_two_N6 < C54N4_all_N5.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "li_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "bowl_C30H10_inner": "number",
          "flat_C30H14": "number",
          "C60_inner": "number",
          "C60_outer": "number",
          "C54N4_all_N5": "number",
          "C54N4_two_N5_two_N6": "number"
        }
      },
      "description": "Lithium adsorption energies computed with DFT-D2 for the five molecular models. The values are compared to the paper-reported values and checked for structural trends (curved > flat, N-doped > undoped, mixed doping > all-N5) using hidden tolerances."
    }
  ],
  "notes": "The hidden checker reads the agent's reported energies and compares each value to the paper's reference within ±0.3 eV, then verifies the following structural relationships: (1) bowl_C30H10_inner < flat_C30H14 (curved binds stronger), (2) both C54N4 entries < C60_inner, (3) C54N4_two_N5_two_N6 < C54N4_all_N5."
}
```

## How you are scored
A hidden verifier reads your submitted JSON file and compares the reported adsorption energies to reference values and checks structural relationships among the models. The reward is a weighted combination of these checks: higher weight is given to correct trends and to values that fall within an acceptable tolerance of the expected range, while large deviations or missing entries reduce the reward. You will not see the reference values or tolerances. The more accurately your DFT-D2 calculations reproduce the expected physical behavior, the higher your score.
