# Pressure-Induced Phase Transition in Alumina: Corundum to Rh₂O₃-II

## Problem background
Alumina (Al₂O₃) undergoes a pressure-induced phase transition from the ground-state corundum (α-Al₂O₃) structure to the Rh₂O₃-II structure. The transition pressure is debated experimentally, with estimates spanning a wide range. This task investigates this transition using a transferable ionic potential model that includes both spherical anion relaxation (‘breathing’) and induced dipole/quadrupole polarization on the oxide ions. The goal is to understand whether including anion quadrupoles stabilizes the corundum structure and how the transition pressure shifts compared to a model without polarization.

## Approach
We implement two variants of the compressible ion model (CIM) for Al₂O₃, using parameters from a published potential model. The first variant, CIM with no polarization, includes only spherical anion relaxation. The second, CIM‑DQ, adds induced dipoles and quadrupoles on the oxide ions. For both models and for the corundum and Rh₂O₃‑II crystal structures, we perform static lattice energy minimisations at a series of fixed volumes to obtain energy–volume curves. Each curve is fitted to the Birch‑Murnaghan equation of state to extract equilibrium energy and volume. The Gibbs free energy G = U + PV is then computed from the fitted EOS. The transition pressure is determined as the pressure at which G(corundum) = G(Rh₂O₃‑II), and the relative volume change at that pressure is calculated. The procedure is repeated for both model variants, and the results are reported as a structured JSON file.

## Reproduction target
Produce the static (0 K) corundum→Rh₂O₃‑II phase transition pressure (Pt, in GPa) and the relative volume change (ΔV, in percent) for the CIM with no polarization and for the full CIM‑DQ model. Write the results to `/app/outputs/transition_results.json` as a JSON array containing one object per model variant, each with keys `"model"` (string), `"Pt_GPa"` (number), and `"delta_V_percent"` (number).

## Assets

- Corundum crystal structure (α-Al₂O₃, R-3c): ICSD or Wyckoff Crystal Structures
- Rh₂O₃-II crystal structure (Pbcn): ICSD or Shannon & Prewitt (1970)
- CIM and CIM-DQ interatomic potential model parameters: 10.1103/PhysRevB.54.15683

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Obtain the crystal structures of corundum (α-Al₂O₃, R-3c) and Rh₂O₃-II (Pbcn) from public crystallographic references and store them in a suitable format for subsequent energy calculations.
- Evidence: none

### Step 2: Implement interatomic potentials
- Role: process
- Action: Implement the compressible ion model (CIM) without any polarization and the CIM-DQ variant that includes induced dipoles and quadrupoles, using the parameters published in Wilson et al., Phys. Rev. B 54, 15683 (1996). Ensure correct functional forms for spherical relaxation, short-range overlap, Coulombic interactions, and (for CIM-DQ) the polarization response up to quadrupole level.
- Evidence: none

### Step 3: Generate energy-volume curves
- Role: process
- Action: For each model variant (CIM no polarization and CIM-DQ) and each of the two structures (corundum, Rh₂O₃-II), perform static lattice energy minimisations at a series of fixed volumes spanning the equilibrium range. Record the final energy and volume to build U–V data sets.
- Evidence: `/app/outputs/uv_curves.csv`

### Step 4: Extract transition pressure and volume change
- Role: scored (load-bearing)
- Action: Fit each U–V curve to the Birch-Murnaghan equation of state to obtain equilibrium energy and volume. Compute the Gibbs free energy G = U + PV from the fitted EOS and determine the pressure at which G(corundum) = G(Rh₂O₃-II) for each model. Calculate the relative volume change ΔV = (V_Rh2O3-II − V_corundum)/V_corundum at the transition pressure. Report Pt in GPa and ΔV in percent for both model variants in a structured JSON file.
- Output file: `/app/outputs/transition_results.json`
- Format: json
- Contract: JSON array of two objects. Each object has keys: "model" (string, one of "CIM-DQ" or "CIM no polarization"), "Pt_GPa" (number, transition pressure in GPa), "delta_V_percent" (number, relative volume change in percent, e.g. -1.68 means -1.68% decrease).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_results.json
- path: `/app/outputs/transition_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: A JSON array with two entries, one for each model variant ("CIM-DQ" and "CIM no polarization"). Each entry reports the calculated corundum→Rh₂O₃-II transition pressure (Pt_GPa) and relative volume change (delta_V_percent). The checker will apply threshold_or_better tolerances on Pt and delta_V, as well as a secondary structural ordering check.
- schema:
  - `type`: array
  - `required`:
    - `model`: string
    - `Pt_GPa`: number
    - `delta_V_percent`: number
  - `items`:
    - `model`: string
    - `Pt_GPa`: number
    - `delta_V_percent`: number
  - `required_columns`:
  - `units`:
    - `Pt_GPa`: GPa
    - `delta_V_percent`: percent

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "required": {
          "model": "string",
          "Pt_GPa": "number",
          "delta_V_percent": "number"
        },
        "items": {
          "model": "string",
          "Pt_GPa": "number",
          "delta_V_percent": "number"
        },
        "required_columns": [],
        "units": {
          "Pt_GPa": "GPa",
          "delta_V_percent": "percent"
        }
      },
      "description": "A JSON array with two entries, one for each model variant (\"CIM-DQ\" and \"CIM no polarization\"). Each entry reports the calculated corundum→Rh₂O₃-II transition pressure (Pt_GPa) and relative volume change (delta_V_percent). The checker will apply threshold_or_better tolerances on Pt and delta_V, as well as a secondary structural ordering check."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `transition_results.json` and independently scores the transition pressure and volume change for each model. The verifier compares your computed values to a hidden gold result, applying tolerances that allow for legitimate numerical differences from different implementations while penalising solutions far from the expected physics. It also checks that the transition pressure is larger for the CIM‑DQ model than for the model without polarization, and that the magnitude of the volume change is smaller for CIM‑DQ. Reporting the paper's numbers without performing the required calculations will not pass, because the verifier rewards intermediate evidence and internal consistency, not a pre‑filled answer. The final reward is a weighted combination of the scores on each required condition.
