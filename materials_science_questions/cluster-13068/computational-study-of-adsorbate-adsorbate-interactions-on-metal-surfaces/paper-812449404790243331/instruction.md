# Field adsorption binding energy calculation using array model

## Problem background
In field-ion microscopy, imaging gas atoms can become field-adsorbed onto the emitter surface. The binding energy of these atoms has a short-range part that arises from the locally enhanced electric field and from dispersion/repulsion interactions with the substrate. An array model represents the emitter surface as an infinite periodic lattice of superimposed monopoles and dipoles, together with a layer of adsorbate atoms. The model accounts for mutual depolarisation within each layer and mutual induction between the two layers. The goal of this task is to compute the field enhancement factor at the adsorbate site and the resulting conventional and differential short-range binding energies for helium on a hexagonally-packed tungsten (111) surface, at an external field of 56 V nm⁻¹, considering two plausible values for the emitter-atom polarisability.

## Approach
Implement the array model for a two-layer system: an emitter-atom layer (E) and an adsorbate-atom layer (A), both with hexagonal lattice structure (lattice spacing a = 0.4476 nm, interlayer separation s = 0.259 nm). Use the known structure factors for the hexagonal lattice: K₁ = 11.034 for the intra-layer depolarising sum, and S = 5.297 for the interlayer coupling sum. The adsorbate (helium) polarisability is b_A = 0.143 meV V⁻² nm²; the emitter polarisability b_E takes the two values 2.00 and 7.00 meV V⁻² nm². All calculations should be performed in consistent SI units.

First, compute the layer relative permittivities M_A = 1 + b_A·K₁/(4πε₀ a³) and M_E = 1 + b_E·K₁/(4πε₀ a³), and the coupling coefficients γ_A^E = S·b_E/(4πε₀ a³) and γ_E^A = S·b_A/(4πε₀ a³). The monopole-induced field ratios are β_A^m = 1.048 and β_E^m = 0.5. With these, compute the field enhancement factor β_A for each b_E value from the self-consistent formula:

β_A = (M_A⁻¹ β_A^m + M_A⁻¹ γ_A^E M_E⁻¹ β_E^m) / (1 − M_A⁻¹ γ_A^E M_E⁻¹ γ_E^A).

Next, calculate the conventional short‑range binding energy ΔB(conv.) = 0.5·b_A·(β_A² − 1)·(F_ext)² with F_ext = 56 V nm⁻¹. Then obtain the differential short‑range binding energy ΔB(diff.) = (1−η)·ΔB(conv.) + 0.5·ΔB_disp, using η = 0.51 for b_E = 2.00 meV V⁻² nm², η = 0.48 for b_E = 7.00 meV V⁻² nm², and ΔB_disp = 10 meV.

All numerical work can be done in a standard Python environment with NumPy.

## Reproduction target
Compute the following quantities for both values of the emitter polarisability (b_E = 2.00 and 7.00 meV V⁻² nm²) on the hexagonal W(111) lattice at an external field of 56 V nm⁻¹:

- the field enhancement factor β_A,
- the conventional short‑range binding energy ΔB(conv.) (in eV),
- the differential short‑range binding energy ΔB(diff.) (in eV).

Write the results to two CSV files as specified in the workflow steps.

## Assets

- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Compute intermediate parameters M and γ
- Role: process
- Action: Compute the layer relative permittivities M_A and M_E and coupling coefficients γ_A^E and γ_E^A using the hexagonal lattice model. Use the given lattice spacing a=0.4476 nm, structure factor K1=11.034, adsorbate polarisability b_A=0.143 meV V^-2 nm^2, emitter polarisabilities b_E=2.00 and 7.00 meV V^-2 nm^2, and structure factor S=5.297. Carry out in consistent SI units.
- Evidence: `/app/outputs/step_01_intermediates_log.txt`

### Step 2: Compute field enhancement factor β_A
- Role: scored (load-bearing)
- Action: Using the computed M_A, M_E, γ_A^E, γ_E^A and the given monopole field ratios β_A^m=1.048, β_E^m=0.5, calculate the field enhancement factor β_A for the two emitter polarisability values via the full array model formula. Write the results to the output CSV.
- Output file: `/app/outputs/step_01_field_enhancement_factors.csv`
- Format: csv
- Contract: CSV with columns: b_E_value (float, meV V^-2 nm^2), lattice_type (str, 'hexagonal'), beta_A (float, dimensionless). Two rows.
- Scoring: scored by hidden verifier

### Step 3: Compute short-range binding energies
- Role: scored
- Action: For each emitter polarisability case, compute the conventional short-range binding energy ΔB(conv.) (eV) from the field enhancement factor via ΔB(conv.) = 0.5 * b_A * (β_A^2 - 1) * (F_ext)^2, with F_ext = 56 V/nm. Then compute the differential binding energy ΔB(diff.) (eV) using ΔB(diff.) = (1-η) * ΔB(conv.) + 0.5 * ΔB_disp, with η = 0.51 for b_E=2.00, η = 0.48 for b_E=7.00, and ΔB_disp = 10 meV. Write the results to the output CSV.
- Output file: `/app/outputs/step_02_binding_energies.csv`
- Format: csv
- Contract: CSV with columns: b_E_value (float, meV V^-2 nm^2), lattice_type (str, 'hexagonal'), Delta_B_conv (float, eV), Delta_B_diff (float, eV). Two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_field_enhancement_factors.csv`
- `/app/outputs/step_02_binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_field_enhancement_factors.csv
- path: `/app/outputs/step_01_field_enhancement_factors.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Field enhancement factor β_A computed for the two emitter polarisability values using the hexagonal array model.
- schema:
  - `type`: table
  - `required_columns`: `b_E_value`, `lattice_type`, `beta_A`
  - `units`:
    - `b_E_value`: meV V^{-2} nm^2
    - `beta_A`: dimensionless

### step_02_binding_energies.csv
- path: `/app/outputs/step_02_binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Conventional and differential short-range binding energies derived from the field enhancement factor for both emitter polarisability values.
- schema:
  - `type`: table
  - `required_columns`: `b_E_value`, `lattice_type`, `Delta_B_conv`, `Delta_B_diff`
  - `units`:
    - `b_E_value`: meV V^{-2} nm^2
    - `Delta_B_conv`: eV
    - `Delta_B_diff`: eV

Notes: The hidden checker recomputes intermediate quantities as needed and compares the submitted values to expected numerical ranges with tolerance, ensuring internal consistency and correct physical derivation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_field_enhancement_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "b_E_value",
          "lattice_type",
          "beta_A"
        ],
        "units": {
          "b_E_value": "meV V^{-2} nm^2",
          "beta_A": "dimensionless"
        }
      },
      "description": "Field enhancement factor β_A computed for the two emitter polarisability values using the hexagonal array model."
    },
    {
      "file": "step_02_binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "b_E_value",
          "lattice_type",
          "Delta_B_conv",
          "Delta_B_diff"
        ],
        "units": {
          "b_E_value": "meV V^{-2} nm^2",
          "Delta_B_conv": "eV",
          "Delta_B_diff": "eV"
        }
      },
      "description": "Conventional and differential short-range binding energies derived from the field enhancement factor for both emitter polarisability values."
    }
  ],
  "notes": "The hidden checker recomputes intermediate quantities as needed and compares the submitted values to expected numerical ranges with tolerance, ensuring internal consistency and correct physical derivation."
}
```

## How you are scored
A hidden verifier will independently score each of the two output artifacts (field enhancement factors and binding energies). It will compare your submitted β_A values against the expected physical ranges, recompute ΔB(conv.) from your β_A, and recompute ΔB(diff.) using the given formulas and parameters. The verifier checks internal consistency and the required physical trends between the two b_E cases. The final reward is a weighted combination of the per-stage scores. Simply reporting the paper's published numbers is not sufficient; the workflow must be executed correctly to produce the required outputs.
