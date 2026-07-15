# Thermochemical stability and thermodynamic functions of the HO₂–HClO₄ complex

## Problem background
The HO₂–HClO₄ complex may influence peroxy radical partitioning in atmospheric chemistry. This work aims to determine its thermochemical stability by computing the dissociation binding energies, and to provide fitted thermodynamic functions (heat capacity, entropy, enthalpy content) for the dissociation reaction. The target quantities are derived from first‑principles quantum chemical calculations.

## Approach
Geometry optimizations and harmonic frequency calculations are performed for the isolated monomers HO₂ and HClO₄, and for the HO₂–HClO₄ complex, using density functional theory (B3LYP) and second‑order Møller‑Plesset perturbation theory (MP2), both with the 6‑311++G(3df,3pd) basis set. From these calculations, total electronic energies and zero‑point energies (ZPE) are extracted. Binding energies (Dₑ without ZPE and D₀ with ZPE) are then computed for the dissociation reaction HO₂–HClO₄ → HO₂ + HClO₄. Using the harmonic vibrational frequencies from the B3LYP calculation, the isobaric heat capacity (Cₚ), entropy (S), and enthalpy content (H⁰ − H₂₉₈.₁₅⁰) are obtained for the same reaction at three temperatures (100 K, 298.15 K, 1000 K) via standard statistical thermodynamics (translational, rotational, and vibrational contributions).

## Reproduction target
Compute the dissociation binding energies Dₑ and D₀ (kcal mol⁻¹) for HO₂–HClO₄ → HO₂ + HClO₄ at the B3LYP/6‑311++G(3df,3pd) and MP2/6‑311++G(3df,3pd) levels. Compute the isobaric heat capacity Cₚ (kJ mol⁻¹ K⁻¹), entropy S (J mol⁻¹ K⁻¹), and enthalpy content H⁰ − H₂₉₈.₁₅⁰ (kJ mol⁻¹) for the same reaction at T = 100 K, 298.15 K, and 1000 K, using harmonic vibrational frequencies from the B3LYP calculation and standard thermodynamic formulas. Report the binding energies in `binding_energies.csv` and the thermodynamic functions in `thermodynamic_functions.csv`, with the exact formats specified in the workflow steps and output contract.

## Assets

- Psi4: https://psicode.org/

## Workflow steps

### Step 1: Quantum chemical calculations
- Role: process
- Action: Using Psi4, perform geometry optimizations and harmonic frequency calculations for the isolated monomers HO₂ and HClO₄, and for the HO₂–HClO₄ complex, at the B3LYP/6‑311++G(3df,3pd) and MP2/6‑311++G(3df,3pd) levels of theory. Extract total electronic energies, zero‑point energies (ZPE), and harmonic vibrational frequencies. Save the results in a JSON file for use by subsequent steps.
- Evidence: `/app/outputs/computed_energies.json`

### Step 2: Compute binding energies
- Role: scored (load-bearing)
- Action: From the total electronic energies and ZPE obtained in step_01, compute the binding energy without ZPE (D_e) and with ZPE (D₀) in kcal/mol for the dissociation reaction HO₂–HClO₄ → HO₂ + HClO₄ at both B3LYP/6‑311++G(3df,3pd) and MP2/6‑311++G(3df,3pd) levels. Write the results to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: Columns: method (string), de (float, kcal/mol), d0 (float, kcal/mol). Rows for B3LYP/6‑311++G(3df,3pd) and MP2/6‑311++G(3df,3pd).
- Scoring: scored by hidden verifier

### Step 3: Compute thermodynamic functions
- Role: scored (load-bearing)
- Action: Using the harmonic vibrational frequencies from the B3LYP/6‑311++G(3df,3pd) calculation in step_01, compute the isobaric heat capacity (Cₚ, kJ mol⁻¹ K⁻¹), entropy (S, J mol⁻¹ K⁻¹), and enthalpy content (H⁰ − H₂₉₈.₁₅⁰, kJ mol⁻¹) for the dissociation reaction at T = 100 K, 298.15 K, and 1000 K. Use the standard statistical thermodynamics expressions (translational, rotational, vibrational contributions) and report the results in thermodynamic_functions.csv.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: Columns: property (string), T100 (float), T298 (float), T1000 (float). Properties: Cp (kJ/mol/K), S (J/mol/K), H_minus_H298 (kJ/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/thermodynamic_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies (D_e and D₀) for HO₂–HClO₄ → HO₂ + HClO₄ at two levels of theory.
- schema:
  - `type`: table
  - `required_columns`: `method`, `de`, `d0`
  - `units`:
    - `de`: kcal/mol
    - `d0`: kcal/mol

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic functions (Cₚ, S, H⁰−H₂₉₈.₁₅⁰) at 100 K, 298.15 K, and 1000 K.
- schema:
  - `type`: table
  - `required_columns`: `property`, `T100`, `T298`, `T1000`
  - `units`:
    - `T100`: varies by property row
    - `T298`: varies by property row
    - `T1000`: varies by property row

Notes: The hidden checker compares the agent’s reported values against the paper’s originally reported numbers with per‑property tolerances; no gold values are exposed in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "de",
          "d0"
        ],
        "units": {
          "de": "kcal/mol",
          "d0": "kcal/mol"
        }
      },
      "description": "Binding energies (D_e and D₀) for HO₂–HClO₄ → HO₂ + HClO₄ at two levels of theory."
    },
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "T100",
          "T298",
          "T1000"
        ],
        "units": {
          "T100": "varies by property row",
          "T298": "varies by property row",
          "T1000": "varies by property row"
        }
      },
      "description": "Computed thermodynamic functions (Cₚ, S, H⁰−H₂₉₈.₁₅⁰) at 100 K, 298.15 K, and 1000 K."
    }
  ],
  "notes": "The hidden checker compares the agent’s reported values against the paper’s originally reported numbers with per‑property tolerances; no gold values are exposed in this contract."
}
```

## How you are scored
A hidden verifier independently scores each load‑bearing artifact (`binding_energies.csv` and `thermodynamic_functions.csv`). The verifier compares the values you report against hidden reference values using per‑property tolerances. Both artifacts carry substantial weight, and genuine execution of all workflow steps is required; simply reporting numbers without performing the calculations will not yield the correct results. Deviation from the expected values reduces the reward.
