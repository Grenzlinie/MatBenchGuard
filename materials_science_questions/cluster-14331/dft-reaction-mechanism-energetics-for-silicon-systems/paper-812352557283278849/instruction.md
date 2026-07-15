# G3 Enthalpy Profile for Silylene + Hydrogen Chloride Reaction

## Problem background
The reaction of silylene (SiH2) with hydrogen chloride (HCl) is an important prototype for understanding insertion and elimination pathways in silicon-hydride chemistry and chemical vapor deposition. Experimental kinetic studies observe a weakly pressure-dependent reaction, pointing to a potential energy surface (PES) with several intermediates and transition states. A reliable ab initio energy profile is essential to interpret the kinetics and determine which pathways are accessible. This task asks you to compute that energy profile using the G3 composite method.

## Approach
The energy landscape is explored with ab initio electronic structure theory. Starting from initial guesses for all relevant species (reactants, donor–acceptor complexes, transition states, products), geometries are optimized at the MP2/6-31G(d) level and harmonic vibrational frequencies are computed to confirm stationary points and obtain thermal corrections. Then a G3 composite energy calculation is performed: single-point energies at QCISD(T)/6-31G(d), MP4/6-31+G(d), MP4/6-31G(2df,p), and MP2/GTlarge levels are combined according to the G3 additive scheme to yield accurate enthalpies at 298.15 K. The resulting enthalpies are reported relative to the infinitely separated reactants SiH2 + HCl.

## Reproduction target
Compute the relative enthalpies (kJ/mol) at the G3 level for all stationary points on the SiH2 + HCl potential energy surface, with respect to the separated reactants, and save them in a JSON file. The required species are: SiH2 + HCl (reactants), H2Si···ClH in syn and anti conformers (donor–acceptor complexes), TS1 (chlorine-to-silicon H-shift), TS2 (direct H2 elimination from the complex), SiH3Cl (chlorosilane), TS3 (H2 elimination from SiH3Cl), and the products HSiCl + H2. Optionally, the SiH2Cl radical + H atom can be included.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Basis sets 6-31G(d), 6-31+G(d), 6-31G(2df,p), GTlarge: Included with ORCA; GTlarge basis available via Basis Set Exchange

## Workflow steps

### Step 1: Geometry optimization and frequency analysis
- Role: process
- Action: Perform MP2/6-31G(d) geometry optimization for all species on the SiH2+HCl potential energy surface: SiH2, HCl, H2Si···ClH (syn and anti conformers), TS1 (Cl→Si H-shift), TS2 (direct H2 elimination from complex), SiH3Cl, TS3 (H2 elimination from SiH3Cl), HSiCl, H2, and optionally the SiH2Cl radical. Compute harmonic vibrational frequencies at the same level to confirm stationary points (minima have no imaginary frequencies, transition states exactly one). Scale frequencies by 0.893.
- Evidence: `/app/outputs/geom_opt.log`

### Step 2: G3 energy calculation and relative enthalpy output
- Role: scored (load-bearing)
- Action: Using the optimized geometries and scaled frequencies from the previous step, perform G3 composite energy calculations: QCISD(T)/6-31G(d), MP4/6-31+G(d), MP4/6-31G(2df,p), and MP2/GTlarge single-point energies. Combine them according to the G3 procedure to obtain enthalpies at 298.15 K. Compute relative enthalpies (kJ/mol) with respect to SiH2 + HCl. Save the results to relative_enthalpies.json.
- Output file: `/app/outputs/relative_enthalpies.json`
- Format: json
- Contract: A JSON object with keys: "SiH2+HCl", "ylid_anti", "ylid_syn", "TS1", "TS2", "SiH3Cl", "TS3", "SiHCl+H2". Each value is a float representing relative enthalpy in kJ/mol. Optional key: "SiH2Cl_radical+H".
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_enthalpies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_enthalpies.json
- path: `/app/outputs/relative_enthalpies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative G3 enthalpies (kJ/mol) of all stationary points on the SiH3Cl potential energy surface with respect to the reactants SiH2 + HCl.
- schema:
  - `type`: object
  - `required`: `SiH2+HCl`, `ylid_anti`, `ylid_syn`, `TS1`, `TS2`, `SiH3Cl`, `TS3`, `SiHCl+H2`
  - `properties`:
    - `SiH2+HCl`:
      - `type`: number
      - `unit`: kJ/mol
    - `ylid_anti`:
      - `type`: number
      - `unit`: kJ/mol
    - `ylid_syn`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS1`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS2`:
      - `type`: number
      - `unit`: kJ/mol
    - `SiH3Cl`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS3`:
      - `type`: number
      - `unit`: kJ/mol
    - `SiHCl+H2`:
      - `type`: number
      - `unit`: kJ/mol
  - `additionalProperties`: False

Notes: The optional key 'SiH2Cl_radical+H' may be present; it is not required for scoring. Scoring tolerances (hidden) are 5 kJ/mol for minima and 10 kJ/mol for transition states, applied against the paper-reported G3 values. Structural ordering checks also contribute.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_enthalpies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "SiH2+HCl",
          "ylid_anti",
          "ylid_syn",
          "TS1",
          "TS2",
          "SiH3Cl",
          "TS3",
          "SiHCl+H2"
        ],
        "properties": {
          "SiH2+HCl": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "ylid_anti": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "ylid_syn": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS1": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS2": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "SiH3Cl": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS3": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "SiHCl+H2": {
            "type": "number",
            "unit": "kJ/mol"
          }
        },
        "additionalProperties": false
      },
      "description": "Relative G3 enthalpies (kJ/mol) of all stationary points on the SiH3Cl potential energy surface with respect to the reactants SiH2 + HCl."
    }
  ],
  "notes": "The optional key 'SiH2Cl_radical+H' may be present; it is not required for scoring. Scoring tolerances (hidden) are 5 kJ/mol for minima and 10 kJ/mol for transition states, applied against the paper-reported G3 values. Structural ordering checks also contribute."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier. It reads the JSON output and compares your relative-enthalpy values to a hidden reference derived from the published G3 calculation, using tolerances that account for typical variations between honest re-runs. Each required species is checked; the reward is proportional to the number of values that fall within the tolerance. Additional checks verify that the enthalpies respect plausible chemical ordering, but these carry only small weight. Producing the proper computational workflow (geometry optimizations and G3 energy evaluations) is essential — fabricating numbers without running the calculations is unlikely to pass the scoring.
