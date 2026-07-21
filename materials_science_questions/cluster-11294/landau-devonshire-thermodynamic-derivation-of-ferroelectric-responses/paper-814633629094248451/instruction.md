# Thermal-expansion mismatch model for in-plane strain of BSTO in oxide nanocomposites

## Problem background
Self-assembled vertical nanocomposite thin films of (Ba₀.₆Sr₀.₄TiO₃)₁₋ₓ–(Sm₂O₃)ₓ (BSTO–SmO) exhibit unusual strain states that strongly influence their functional properties. This task reproduces a simple analytical model that predicts the in-plane strain and lattice parameter of BSTO in these nanocomposites. The model combines the thermal expansion mismatch between the two phases with the effect of SmO on the cubic-to-tetragonal phase transition of BSTO to explain how the in-plane lattice parameter varies with composition x. The computed predictions can be compared against measured values from the literature.

## Approach
The in-plane strain and lattice parameter are computed using a thermal‑expansion mismatch model. The system undergoes a cooling process from the growth temperature (800 °C) to room temperature (25 °C), giving a temperature change ΔT = –775 K. For compositions x = 0.25 and 0.50, the Sm₂O₃ forms stiff nanopillars embedded in the BSTO matrix. The BSTO in-plane strain ε arises from two contributions: (1) the thermal contraction of SmO pillars, which strains the BSTO matrix, yielding ε = –α_SmO·ΔT, and (2) an additional 0.5 % tensile strain because the cubic-to-tetragonal phase transition of BSTO is prevented. Thus ε = –α_SmO·ΔT + 0.005. For x = 0.75, the phases reverse: BSTO forms nanopillars inside the SmO matrix, and the SmO matrix radially compresses the BSTO pillars; only the thermal contraction term applies, so ε = α_SmO·ΔT. The thermal expansion coefficient of SmO is α_SmO = 8.8 × 10⁻⁶ K⁻¹. The strain percent is ε × 100, and the in-plane lattice parameter is a = a₀·(1 + ε) with the bulk cubic BSTO lattice constant a₀ = 0.3965 nm. The model is applied to three compositions, x = 0.25, 0.50, and 0.75.

## Reproduction target
Compute the predicted in-plane strain (in percent) and in-plane lattice parameter (in nm) for BSTO at compositions x = 0.25, 0.50, and 0.75 for 1000‑nm thick films using the thermal‑expansion mismatch model. Output the results as a CSV file with columns: x, predicted_strain_percent, predicted_lattice_parameter_nm.

## Assets
No external datasets, pre-trained models, or proprietary software are required. All necessary physical constants and formulas are provided in the instruction. Standard Python with its csv and math modules is sufficient; no additional packages are mandated.

## Workflow steps

### Step 1: In-plane strain model computation
- Role: scored (load-bearing)
- Action: Apply the thermal-expansion mismatch model: for x=0.25 and 0.50 (SmO nanopillars in BSTO matrix) the in-plane strain ε = −α_SmO·ΔT + 0.005; for x=0.75 (BSTO nanopillars in SmO matrix) ε = α_SmO·ΔT. Use α_SmO = 8.8×10⁻⁶ K⁻¹, ΔT = −775 K. Convert to strain percent = ε×100. Compute lattice parameter a = a₀·(1+ε) with a₀ = 0.3965 nm. Output one row per x for x = 0.25, 0.50, 0.75.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: columns: x (float), predicted_strain_percent (float), predicted_lattice_parameter_nm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted in-plane strain (percent) and lattice parameter (nm) for BSTO at x=0.25, 0.50, 0.75 (1000 nm film thickness), computed from the thermal-expansion mismatch model. The checker compares each row to the paper's measured values within tolerances; correct sign is also required.
- schema:
  - `type`: table
  - `required_columns`: `x`, `predicted_strain_percent`, `predicted_lattice_parameter_nm`

Notes: The only scored artifact is the predictions.csv containing three rows with the computed quantities. The checker will compare each predicted strain and lattice parameter to hidden measured values (from the paper's Table I, 1000 nm films) with a tolerance on strain and lattice parameter, and verify correct sign of strain (positive for x=0.25,0.50; negative for x=0.75). Partial credit is proportional to the number of correct values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "predicted_strain_percent",
          "predicted_lattice_parameter_nm"
        ]
      },
      "description": "Predicted in-plane strain (percent) and lattice parameter (nm) for BSTO at x=0.25, 0.50, 0.75 (1000 nm film thickness), computed from the thermal-expansion mismatch model. The checker compares each row to the paper's measured values within tolerances; correct sign is also required."
    }
  ],
  "notes": "The only scored artifact is the predictions.csv containing three rows with the computed quantities. The checker will compare each predicted strain and lattice parameter to hidden measured values (from the paper's Table I, 1000 nm films) with a tolerance on strain and lattice parameter, and verify correct sign of strain (positive for x=0.25,0.50; negative for x=0.75). Partial credit is proportional to the number of correct values."
}
```

## How you are scored
Your submission consists of the single file `/app/outputs/predictions.csv`. A hidden verifier will read this file and compare each row's predicted strain and lattice parameter to hidden reference measured values. The verifier will check that the strain sign (positive or negative) is correct for each composition and that the values lie within required tolerances. The final reward is a number between 0 and 1, proportional to the number of correct values across all rows (six values total: strain and lattice parameter for each x).
