# Predict Density and Detonation Performance of SF5- and CF3-1,2,3-Triazoles

## Problem background
Pentafluorosulfanyl (SF5)-substituted heterocycles are promising candidates for high-density energetic materials. Because the SF5 group has a higher intrinsic density than the CF3 group and can enhance the exothermicity of reactions with metals, it is hypothesized that replacing CF3 with SF5 in nitrogen-rich heterocycles will increase crystal density and improve detonation performance. This task tests that hypothesis computationally for two model 1,2,3-triazoles: 4-SF5-1,2,3-triazole (compound 5) and its CF3 analogue 4-CF3-1,2,3-triazole (compound 8). The goal is to compute their crystal density, condensed-phase heat of formation, detonation pressure, and detonation velocity using quantum chemistry, group additivity, and semi-empirical detonation models.

## Approach
The computational workflow has four stages. First, gas-phase thermochemistry is obtained by density functional theory (DFT) at the B3LYP/6-311G(d,p) level: geometry optimization and harmonic frequency calculation for each compound yield the electronic energy and thermal corrections needed for the atomization energy method. Standard experimental heats of formation for atoms (C, H, N, F, S) are used to convert the total energy to a gas-phase heat of formation. Second, the gaseous heat of formation is converted to a condensed-phase value by subtracting a constant enthalpy of sublimation (20 kcal mol⁻¹ = 83.68 kJ mol⁻¹). Third, crystal density is predicted by an atom/group additivity scheme. The molecular volume is estimated by summing group volumes: C 6.3 Å³, H 3.5 Å³, N 7.0 Å³, F 10.5 Å³, and SF5 82 Å³ (from Ye & Shreeve, J. Phys. Chem. A 2007). Density is then density = molecular_weight / (total_volume × 0.6022), giving units of g cm⁻³. Fourth, the condensed-phase heat of formation and predicted density are fed into the Kamlet–Jacobs semi-empirical equations to compute detonation pressure (P) and detonation velocity (D). The required parameters N (moles of gas per gram), M (average molecular weight of gaseous products), and Q (detonation heat release, kcal g⁻¹) are derived from the molecular formula and the standard decomposition products (CO₂, H₂O, N₂, HF, SF₄, etc.) following the Kamlet–Jacobs rules. The entire pipeline is rerun independently for each compound, and the final computed values are reported in the scored output files.

## Reproduction target
Compute the crystal density (g cm⁻³), condensed-phase heat of formation (ΔfH°298, kJ mol⁻¹), detonation pressure (P, GPa), and detonation velocity (D, m s⁻¹) for compound 5 (4‑SF5‑1,2,3‑triazole) and compound 8 (4‑CF3‑1,2,3‑triazole). The structural relationship between their properties will be verified by the scorer.

## Assets

- Quantum chemistry software (e.g., ORCA, NWChem, Psi4): https://orcaforum.kofo.mpg.de/
- Group volume additivity parameters: 10.1021/jp0684402
- Molecular structures of compounds 5 and 8

## Workflow steps

### Step 1: DFT geometry optimization and frequency calculation
- Role: process
- Action: Perform geometry optimization and harmonic frequency calculation at the B3LYP/6-311G(d,p) level for compounds 5 and 8. Save the optimized Cartesian coordinates and raw thermochemistry output (total energy, zero-point energy, thermal correction to enthalpy).
- Evidence: none

### Step 2: Compute gas-phase heat of formation
- Role: process
- Action: Using the total energies and thermal corrections from step 1, compute the gas-phase heat of formation for compounds 5 and 8 using the atomization energy method with standard experimental heats of formation for atoms (C, H, N, F, S). Save the computed gas-phase ΔfH°298 (kJ/mol) for each compound.
- Evidence: `/app/outputs/gas_hof.json`

### Step 3: Convert to condensed-phase heat of formation
- Role: process
- Action: For each compound, subtract the constant enthalpy of sublimation (20 kcal/mol = 83.68 kJ/mol) from the gas-phase heat of formation to obtain the condensed-phase heat of formation. Save the values in JSON.
- Evidence: `/app/outputs/condensed_hof.json`

### Step 4: Predict crystal density by group additivity
- Role: process
- Action: Calculate the crystal density (g/cm³) for compounds 5 and 8 using the atom/group additivity method. Sum the group volumes from the provided parameters (SF5 = 82 Å³; other atom volumes given in instruction), compute molecular weight from the formula, and apply density = molecular_weight / (total_volume * 0.6022). Save the predicted density for each compound.
- Evidence: `/app/outputs/predicted_density.json`

### Step 5: Compute detonation performance via Kamlet-Jacobs
- Role: process
- Action: Using the condensed-phase heat of formation and predicted density, compute detonation pressure (P, GPa) and detonation velocity (D, m/s) for each compound using the Kamlet-Jacobs semiempirical equations. Derive N (moles of gas per gram), M (average molecular weight of gas), and Q (detonation heat release, kcal/g) from the compound's molecular formula and decomposition products following standard Kamlet-Jacobs rules. Save the computed P and D.
- Evidence: `/app/outputs/detonation_raw.json`

### Step 6: Scored output for compound 5
- Role: scored (load-bearing)
- Action: Write the final computed values for compound 5 (density, condensed heat of formation, detonation pressure, detonation velocity) into compound_5_results.json according to the schema.
- Output file: `/app/outputs/compound_5_results.json`
- Format: json
- Contract: {"compound": "5", "density": <float g/cm³>, "delta_H_condensed": <float kJ/mol>, "detonation_P": <float GPa>, "detonation_D": <float m/s>}
- Scoring: scored by hidden verifier

### Step 7: Scored output for compound 8
- Role: scored (load-bearing)
- Action: Write the final computed values for compound 8 (density, condensed heat of formation, detonation pressure, detonation velocity) into compound_8_results.json according to the schema.
- Output file: `/app/outputs/compound_8_results.json`
- Format: json
- Contract: {"compound": "8", "density": <float g/cm³>, "delta_H_condensed": <float kJ/mol>, "detonation_P": <float GPa>, "detonation_D": <float m/s>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/compound_5_results.json`
- `/app/outputs/compound_8_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### compound_5_results.json
- path: `/app/outputs/compound_5_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed density, condensed-phase heat of formation, detonation pressure, and detonation velocity for 4-SF5-1,2,3-triazole (compound 5). The checker will compare density and heat of formation to hidden reference values and recompute detonation from the submitted density/heat of formation to verify internal consistency.
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `density`: number
    - `delta_H_condensed`: number
    - `detonation_P`: number
    - `detonation_D`: number
  - `units`:
    - `density`: g/cm³
    - `delta_H_condensed`: kJ/mol
    - `detonation_P`: GPa
    - `detonation_D`: m/s

### compound_8_results.json
- path: `/app/outputs/compound_8_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed density, condensed-phase heat of formation, detonation pressure, and detonation velocity for 4-CF3-1,2,3-triazole (compound 8). The checker will compare density and heat of formation to hidden reference values and recompute detonation from the submitted density/heat of formation to verify internal consistency.
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `density`: number
    - `delta_H_condensed`: number
    - `detonation_P`: number
    - `detonation_D`: number
  - `units`:
    - `density`: g/cm³
    - `delta_H_condensed`: kJ/mol
    - `detonation_P`: GPa
    - `detonation_D`: m/s

Notes: The detonation values are computed using the Kamlet-Jacobs equations, not the paper's proprietary Cheetah 4.0. The checker will recompute detonation pressure and velocity from the submitted density and heat of formation and verify that compound 5 exhibits higher density and detonation velocity than compound 8 (trend).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "compound_5_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "density": "number",
          "delta_H_condensed": "number",
          "detonation_P": "number",
          "detonation_D": "number"
        },
        "units": {
          "density": "g/cm³",
          "delta_H_condensed": "kJ/mol",
          "detonation_P": "GPa",
          "detonation_D": "m/s"
        }
      },
      "description": "Computed density, condensed-phase heat of formation, detonation pressure, and detonation velocity for 4-SF5-1,2,3-triazole (compound 5). The checker will compare density and heat of formation to hidden reference values and recompute detonation from the submitted density/heat of formation to verify internal consistency."
    },
    {
      "file": "compound_8_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "density": "number",
          "delta_H_condensed": "number",
          "detonation_P": "number",
          "detonation_D": "number"
        },
        "units": {
          "density": "g/cm³",
          "delta_H_condensed": "kJ/mol",
          "detonation_P": "GPa",
          "detonation_D": "m/s"
        }
      },
      "description": "Computed density, condensed-phase heat of formation, detonation pressure, and detonation velocity for 4-CF3-1,2,3-triazole (compound 8). The checker will compare density and heat of formation to hidden reference values and recompute detonation from the submitted density/heat of formation to verify internal consistency."
    }
  ],
  "notes": "The detonation values are computed using the Kamlet-Jacobs equations, not the paper's proprietary Cheetah 4.0. The checker will recompute detonation pressure and velocity from the submitted density and heat of formation and verify that compound 5 exhibits higher density and detonation velocity than compound 8 (trend)."
}
```

## How you are scored
Your work is scored by a hidden verifier that inspects the two required output files: `compound_5_results.json` and `compound_8_results.json`. For each compound, the verifier compares your reported density and condensed‑phase heat of formation to hidden reference values (generous tolerances). It then independently recomputes the detonation pressure and velocity from your reported density and heat of formation using the Kamlet–Jacobs equations; your reported detonation values must match the recomputed values within a tight tolerance (internal consistency check). In addition, the verifier checks the structural relationship between the two compounds' properties (trend). Each compound’s internal consistency accounts for 40 % of the total reward, and the correct trend accounts for the remaining 20 %.
