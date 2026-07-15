# Cluster-Model Multiplet Calculation of Magnetic Moment from XAS and XMCD Spectra

## Problem background
Cobalt-doped anatase TiO₂ is a diluted magnetic semiconductor exhibiting carrier-mediated ferromagnetism at room temperature. Soft X-ray magnetic circular dichroism (XMCD) at the Co L₂,₃ edges provides element-specific magnetic probing. Cluster-model multiplet calculations can simulate the Co L₂,₃ X-ray absorption and XMCD spectra and, when combined with XMCD sum rules, yield the magnetic moment per Co ion. This task reproduces the cluster-model part of such an analysis to determine the magnetic moment of Co ions in the bulk.

## Approach
Perform cluster-model multiplet calculations for Co L₂,₃ XAS and XMCD spectra under three crystal-field symmetry contributions (D₂h low-spin, O_h low-spin, O_h high-spin) using a publicly available multiplet code such as CTM4XAS. The electronic parameters (charge-transfer energy Δ, on-site d-d Coulomb energy U_dd, d-p Coulomb energy U_dc, hopping V_Eg, and crystal-field splitting 10Dq) and spin-state weights are listed in the table below. The three spectra are weighted (35%, 35%, 30%) and summed to produce the final XAS and XMCD spectra. Then, apply the XMCD sum rules to the weighted spectra to extract spin and orbital magnetic moments per Co ion, using the spin-sum-rule correction factor of 0.92. The total magnetic moment is the sum of spin and orbital moments.

## Reproduction target
Compute the Co L₂,₃ XAS and XMCD spectra via cluster-model multiplet calculations with the provided parameters and weights. From these spectra, apply the XMCD sum rules (with the 0.92 correction factor) to obtain spin and orbital magnetic moments per Co ion, and report the total magnetic moment in μB/Co. The result must be written to `/app/outputs/magnetic_moment.json` with the exact schema described in the workflow steps.

## Assets

- CTM4XAS: https://www.esrf.fr/computing/scientific/ctm4xas/

## Workflow steps

### Step 1: Cluster-model multiplet calculation
- Role: process
- Action: Using an open-source cluster-model code (CTM4XAS or equivalent), compute the Co L2,3 XAS and XMCD spectra for the weighted mixture of crystal-field symmetries (D2h low-spin 35%, Oh low-spin 35%, Oh high-spin 30%) with the provided electronic parameters (Δ, Udd, Udc, V_Eg, 10Dq). Produce the final weighted spectra files.
- Evidence: `/app/outputs/xas.csv,xmcd.csv`

### Step 2: XMCD sum-rule analysis
- Role: scored (load-bearing)
- Action: From the XAS and XMCD spectra, apply XMCD sum rules to compute spin and orbital magnetic moments per Co ion, using the spin-sum-rule correction factor 0.92. Report the total magnetic moment as the sum of spin and orbital moments.
- Output file: `/app/outputs/magnetic_moment.json`
- Format: json
- Contract: JSON object with fields: total_magnetic_moment (float, μB/Co), spin_moment (float, μB/Co), orbital_moment (float, μB/Co).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moment.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moment.json
- path: `/app/outputs/magnetic_moment.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Co magnetic moment per ion computed from XMCD sum rules. The hidden verifier compares the submitted total_magnetic_moment against a hidden reference value with a tolerance of ±0.2 μB/Co and checks structural sanity: spin_moment > 0 and orbital_moment < spin_moment.
- schema:
  - `type`: object
  - `required`:
    - `total_magnetic_moment`: float (μB/Co)
    - `spin_moment`: float (μB/Co)
    - `orbital_moment`: float (μB/Co)

Notes: Only magnetic_moment.json is directly scored by the verifier; raw XAS and XMCD spectra are not inspected.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "total_magnetic_moment": "float (μB/Co)",
          "spin_moment": "float (μB/Co)",
          "orbital_moment": "float (μB/Co)"
        }
      },
      "description": "Co magnetic moment per ion computed from XMCD sum rules. The hidden verifier compares the submitted total_magnetic_moment against a hidden reference value with a tolerance of ±0.2 μB/Co and checks structural sanity: spin_moment > 0 and orbital_moment < spin_moment."
    }
  ],
  "notes": "Only magnetic_moment.json is directly scored by the verifier; raw XAS and XMCD spectra are not inspected."
}
```

## How you are scored
A hidden verifier will compare your submitted `magnetic_moment.json` against a hidden reference value for the total magnetic moment (μB/Co). Additionally, structural sanity checks will verify that the spin moment is positive and the orbital moment is smaller than the spin moment. The final reward is based on a tolerance‑based match of the total moment and these sanity checks. The verifier does not process any raw spectra; only the JSON output is scored.
