# Determining tilt angles and gauche defect fractions of alkanethiol monolayers on zinc from infrared band intensities

## Problem background
Self-assembled monolayers (SAMs) of alkanethiols on metal substrates are used for surface modification and corrosion protection. Understanding the molecular conformation—specifically the tilt angle, twist angle, and the fraction of gauche defects—is essential for predicting barrier properties and designing subsequent coatings. This work uses infrared reflection-absorption spectroscopy (IRRAS) to determine these structural parameters. The objective is to compute the tilt angles and gauche defect fractions from measured integrated intensities of the C–H stretching bands, applying a well-established orientation analysis.

## Approach
The analysis relies on the surface selection rule for metallic substrates: only the normal component of a vibrational transition dipole moment contributes to the IRRAS intensity. For each vibrational mode i, the integrated monolayer intensity I_i is proportional to the square of the dipole projection F_i(α,β)·|M_i|, where α is the molecular tilt angle from the surface normal and β is the twist angle. By normalizing with the corresponding bulk isotropic intensity A_i, one obtains I_i / I_j = [F_i(α,β) / F_j(α,β)]² · (A_i / A_j). The angular functions F_i(α,β) are determined by the dipole orientations (see below).

First, the twist angle β is determined directly from the ratio of the asymmetric (νₐCH₂) and symmetric (νₛCH₂) methylene stretches, using the relation β = arctan √[(I_νaCH₂·A_νsCH₂) / (I_νsCH₂·A_νaCH₂)], independent of α.

Next, two independent vibrational couples are used to solve for α:
Couple 1: νₐCH₃ in-plane / νₛCH₂
Couple 2: νₛCH₃ / νₛCH₂
For each couple, the equation yields two possible tilt-angle solutions (α₁⁺, α₁⁻) and (α₂⁺, α₂⁻).

The presence of gauche defects causes a discrepancy between the α values obtained from different couples. A sensitivity model relates this discrepancy to the fraction of gauche defects at the chain terminus. The pair that gives a defect fraction below a physically meaningful threshold (typically <5%) corresponds to the positive α branch and is taken as the true solution; the negative branch would imply an unphysically high defect fraction (>50%) and is rejected.

The required integrated intensities I (monolayer) and A (bulk) for the relevant C–H stretching modes—νₐCH₂, νₛCH₂, νₐCH₃ in‑plane, νₐCH₃ out‑of‑plane, νₛCH₃—must be extracted from the Supporting Information PDF listed in Assets. The angular projection functions F_i(α,β) are defined as follows:
- νₐCH₃ in‑plane (⊥ to C–CH₃ bond, in the C–C–C plane): cos α sin δ + sin α cos β cos δ, with δ = (180° − 109°)/2
- νₐCH₃ out‑of‑plane (⊥ to both the C–C–C plane and the C–CH₃ bond): sin α sin β
- νₛCH₂ (dipole bisecting the H–C–H angle): sin α cos β
- νₛCH₃ (∥ to C–CH₃ bond): cos α cos δ − sin α cos β sin δ
- νₐCH₂ (⊥ to C–C–C plane): sin α sin β

Using these, compute the orientation for both CH₃(CH₂)₉–SH (DT) and CH₃(CH₂)₁₇–SH (ODT) monolayers on Zn.

## Reproduction target
Compute the twist angle β, the physically correct positive tilt angle α⁺, and the corresponding gauche defect percentage for decanethiol (DT) and octadecanethiol (ODT) monolayers on zinc, using the integrated intensities from the provided Supporting Information. Write the results to `structure_results.json` with keys: `DT_alpha` (degrees), `ODT_alpha` (degrees), `DT_gauche_pct` (percentage), `ODT_gauche_pct` (percentage), `beta_DT` (degrees), `beta_ODT` (degrees).

## Assets

- Supporting Information: Integrated CH stretching band intensities: https://pubs.acs.org/doi/suppl/10.1021/la0701879

## Workflow steps

### Step 1: Extract intensities and define angular functions
- Role: process
- Action: Obtain the integrated intensities I (monolayer) and A (bulk) for the C–H stretching modes (νaCH2, νsCH2, νaCH3 ip, νaCH3 op, νsCH3) from the Supporting Information. Define the angular projection functions Fi(α,β) for each vibrational mode as described in the paper's orientation analysis.
- Evidence: none

### Step 2: Compute orientation results (β, α, gauche defect %)
- Role: scored (load-bearing)
- Action: Using the extracted intensities and angular functions, compute twist angles β for DT and ODT from the ratio of νaCH2 and νsCH2 intensities. Then, for each thiol, solve the intensity-ratio equation for two vibrational couples: (νaCH3 in-plane / νsCH2) and (νsCH3 / νsCH2) to obtain tilt angle candidates α1+, α1-, α2+, α2-. Evaluate gauche defect fraction from the difference between α1 and α2 on both branches. Select the positive α solution that yields a physically small defect fraction. Write the final twist angles, positive tilt angles (α+), and corresponding gauche defect percentages to structure_results.json.
- Output file: `/app/outputs/structure_results.json`
- Format: json
- Contract: JSON object with keys: DT_alpha (float, degrees), ODT_alpha (float, degrees), DT_gauche_pct (float, percentage), ODT_gauche_pct (float, percentage), beta_DT (float, degrees), beta_ODT (float, degrees)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structure_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structure_results.json
- path: `/app/outputs/structure_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed orientation parameters (tilt angles, gauche defect percentages, twist angles) for decanethiol and octadecanethiol monolayers on zinc.
- schema:
  - `type`: object
  - `required`:
    - `DT_alpha`: float (degrees)
    - `ODT_alpha`: float (degrees)
    - `DT_gauche_pct`: float (percentage)
    - `ODT_gauche_pct`: float (percentage)
    - `beta_DT`: float (degrees)
    - `beta_ODT`: float (degrees)
  - `units`:
    - `DT_alpha`: degrees
    - `ODT_alpha`: degrees
    - `DT_gauche_pct`: percent
    - `ODT_gauche_pct`: percent
    - `beta_DT`: degrees
    - `beta_ODT`: degrees

Notes: The checker will compare the reported values against reference data within specified tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "DT_alpha": "float (degrees)",
          "ODT_alpha": "float (degrees)",
          "DT_gauche_pct": "float (percentage)",
          "ODT_gauche_pct": "float (percentage)",
          "beta_DT": "float (degrees)",
          "beta_ODT": "float (degrees)"
        },
        "units": {
          "DT_alpha": "degrees",
          "ODT_alpha": "degrees",
          "DT_gauche_pct": "percent",
          "ODT_gauche_pct": "percent",
          "beta_DT": "degrees",
          "beta_ODT": "degrees"
        }
      },
      "description": "Computed orientation parameters (tilt angles, gauche defect percentages, twist angles) for decanethiol and octadecanethiol monolayers on zinc."
    }
  ],
  "notes": "The checker will compare the reported values against reference data within specified tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks the contents of each scored artifact file. The verifier compares your computed values for the twist angles, tilt angles, and gauche defect percentages against reference data. Each quantity is assessed with a suitable tolerance, and the final score is a weighted combination of these comparisons. To receive full credit, you must faithfully implement the orientation analysis procedure described in the workflow steps and produce the required output; simply reporting plausible numbers without executing the computation is not sufficient.
