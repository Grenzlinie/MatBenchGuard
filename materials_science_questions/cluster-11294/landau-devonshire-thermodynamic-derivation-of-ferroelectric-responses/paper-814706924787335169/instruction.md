# BT/PZT Bimorph Permittivity Response Calculation

## Problem background
Ferroelectric materials such as BaTiO₃ (BT) exhibit a tunable permittivity under external stress or electric field. This task reproduces a strain‑mediated approach in which the permittivity of a BT ceramic layer is manipulated by a Pb(Zr,Ti)O₃ (PZT) bimorph actuator. In the reported BT/PZT heterostructure, the PZT bimorph bends under an applied electric field and transfers mechanical strain to the BT layer, thereby altering its dielectric response. The goal is to quantify the relationship between the BT relative permittivity ε₃ and the electric field E₃,PZT applied to the PZT bimorph, using an electrostrictive‑based analytical model.

## Approach
In the BT/PZT heterostructure, a thin unpolarized BT layer is bonded to the top surface of a PZT bimorph composed of two thickness‑polarized piezoelectric plates. A control voltage applied to the PZT bimorph produces a longitudinal strain that is transferred to the BT layer. The strain in BT changes its dielectric stiffness χ = 1/(ε₀(ε−1)) through the electrostrictive coupling, and for small stress the dielectric stiffness varies linearly with stress. The relationship between BT permittivity and the stress delivered by the PZT bimorph is combined with the piezoelectric strain of the bimorph to yield an analytical expression for ε₃ as a function of the applied electric field E₃,PZT. The model uses publicly known material constants: electrostrictive coefficient Q₁₃, elastic compliance s₁₁ᴱ, PZT piezoelectric coefficient d₃₁,PZT, vacuum permittivity ε₀, and the zero‑field BT permittivity ε₃(0). The task is to evaluate this expression for electric fields from −4 kV/cm to +4 kV/cm and record the resulting permittivity values.

## Reproduction target
Compute the relative permittivity ε₃ of the BT layer as a function of the applied electric field E₃,PZT over the range −4 kV/cm to +4 kV/cm inclusive, in steps of 0.5 kV/cm, using the electrostrictive‑based model and the material parameters described in the workflow step. Output the results as a CSV file with two columns: E_kV_per_cm (the electric field in kV/cm) and epsilon_3 (the dimensionless relative permittivity).

## Assets
No external datasets, pre‑trained models, or downloadable files are required. All needed material parameters are provided in the workflow step. A standard Python 3 environment with basic mathematical libraries (e.g., math, csv) is sufficient to perform the calculation.

## Workflow steps

### Step 1: Compute BT relative permittivity vs. PZT electric field
- Role: scored (load-bearing)
- Action: Implement the electrostrictive-based analytical relation derived for the BT/PZT heterostructure. Using the material constants: electrostrictive coefficient Q₁₃ = -0.0431 m⁴/C², elastic compliance s₁₁ᴱ = 8.33×10⁻¹² m²/N, PZT piezoelectric coefficient d₃₁,PZT = -274×10⁻¹² C/N, vacuum permittivity ε₀ = 8.85×10⁻¹² F/m, and zero-field BT permittivity ε₃(0) = 5554, compute the BT relative permittivity ε₃ from the formula ε₃(E) = 1 / ( -3 ε₀ Q₁₃ d₃₁,PZT E / s₁₁ᴱ + 1/(ε₃(0)-1) ) + 1. Evaluate ε₃ for electric fields E₃,PZT from -4 kV/cm to +4 kV/cm inclusive, in steps of 0.5 kV/cm. Output the results as a two-column CSV file.
- Output file: `/app/outputs/epsilon_vs_field.csv`
- Format: csv
- Contract: Two columns: E_kV_per_cm (float, the electric field in kV/cm), epsilon_3 (float, the relative permittivity, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/epsilon_vs_field.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### epsilon_vs_field.csv
- path: `/app/outputs/epsilon_vs_field.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file with the computed BT relative permittivity ε₃ for each electric field grid point. The checker recomputes ε₃ from the reported E_kV_per_cm using the same analytical expression and compares epsilon_3 values element-wise with a relative error tolerance.
- schema:
  - `type`: table
  - `required_columns`: `E_kV_per_cm`, `epsilon_3`
  - `units`:
    - `E_kV_per_cm`: kV/cm
    - `epsilon_3`: dimensionless

Notes: The analytical expression and all material constants are public and taken from the paper's Table I. The experimental validation against measured capacitance is not included because the raw measurement data are not publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "epsilon_vs_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "E_kV_per_cm",
          "epsilon_3"
        ],
        "units": {
          "E_kV_per_cm": "kV/cm",
          "epsilon_3": "dimensionless"
        }
      },
      "description": "CSV file with the computed BT relative permittivity epsilon_3 for each electric field grid point. The checker recomputes epsilon_3 from the reported E_kV_per_cm using the same analytical expression and compares epsilon_3 values element-wise with a relative error tolerance."
    }
  ],
  "notes": "The analytical expression and all material constants are public and taken from the paper's Table I. The experimental validation against measured capacitance is not included because the raw measurement data are not publicly available."
}
```

## output_contract declaration

```json
[
  {
    "file": "epsilon_vs_field.csv",
    "format": "csv",
    "purpose": "scored",
    "target_policy": "metric_recompute",
    "schema": {
      "type": "table",
      "required_columns": [
        "E_kV_per_cm",
        "epsilon_3"
      ],
      "units": {
        "E_kV_per_cm": "kV/cm",
        "epsilon_3": "dimensionless"
      }
    },
    "description": "CSV file with the computed BT relative permittivity epsilon_3 for each electric field grid point. The checker recomputes epsilon_3 from the reported E_kV_per_cm using the same analytical expression and compares epsilon_3 values element-wise with a relative error tolerance."
  }
]
```

## How you are scored
A hidden verifier will independently recompute ε₃ using the same analytical expression and the same material constants for each grid point. It reads your submitted CSV file and compares the epsilon_3 values element‑wise. A grid point is considered correct if the agreement satisfies a tight, pre‑defined tolerance. Your final score is the fraction of grid points that are correct, weighted to 100% of the total reward. To receive credit, your output must faithfully implement the described model; simply reporting numbers copied from a publication is not sufficient and will not pass the verification.