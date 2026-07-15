# Thermodynamic Quantities of Impurities in GaP via Bond‑Energy/Strain Method

## Problem background
Control of doping during epitaxial growth of A³B⁵ semiconductors requires knowledge of the thermodynamic properties of substitutional solid solutions. This task computes the key quantities that govern impurity incorporation: the strain energy introduced by a size-mismatched impurity atom, the impurity–host bond energy, the resulting heat of dissolution, and the overall enthalpy change, entropy change, and equilibrium constant for the doping reaction. For tellurium (substituting phosphorus) and zinc (substituting gallium) in gallium phosphide, these quantities have been predicted by a bond‑energy/strain method; the goal is to reproduce those predictions by implementing the same method and using the given material constants.

## Approach
The method treats the host crystal outside the first shell of neighbours as a continuous elastic medium. The strain energy depends on the squared difference between the tetrahedral radii of the impurity and the substituted host atom, with a strain constant C specific to the host compound. The impurity–host bond energy is estimated as one‑quarter of the sum of the sublimation enthalpies of the impurity and the nearest‑neighbour host atom that is being replaced. The heat of dissolution then follows from balancing the four impurity–host bonds against the strain energy. From the known host bond energy, the enthalpy change of the dissolution reaction is obtained. The entropy change is taken as the difference between the gas‑phase entropies of the substituted host atom and the impurity. Finally, the equilibrium constant is found from the relation −RT ln K = ΔH − TΔS evaluated at T = 1200 K. All required input values (host bond energy, strain constant, tetrahedral radii, sublimation enthalpies, and gas entropies) are supplied; the task is to implement these formulas and compute the six thermodynamic quantities for each impurity.

## Reproduction target
Using the supplied material constants, compute the following six thermodynamic quantities for both Te (substituting P) and Zn (substituting Ga) in GaP: strain energy W_strain (kJ/mol), impurity–host bond energy W_A‑I (kJ/mol), heat of dissolution Q_I (kJ/mol), enthalpy change ΔH_I (kJ/mol), entropy change ΔS_I (J/(K mol)), and equilibrium constant K_I. Output the results as a JSON file with the specified schema and save it at `/app/outputs/thermodynamic_quantities.json`. The objective is to produce correct numerical values that match the predictions of the bond‑energy/strain model; the checker will compare your output to reference values.

## Assets

- Tetrahedral radii of elements
- Bond energy of GaP
- Sublimation enthalpies of impurity and host elements
- Monoatomic vapour entropies
- Strain constant C for GaP

## Workflow steps

### Step 1: Compute thermodynamic quantities for Te and Zn in GaP
- Role: scored (load-bearing)
- Action: Using the provided material constants (host bond energy W_A-B, strain constant C, tetrahedral radii, sublimation enthalpies, gas entropies, temperature T = 1200 K), compute the following thermodynamic quantities for both Te (substituting P) and Zn (substituting Ga) impurities in GaP: strain energy W_strain (kJ/mol), impurity‑host bond energy W_A‑I (kJ/mol), heat of dissolution Q_I (kJ/mol), enthalpy change ΔH_I (kJ/mol), entropy change ΔS_I (J/(K mol)), and equilibrium constant K_I. Apply the bond‑energy/strain formulas: W_strain = C·(Δr)² (with Δr = |r_impurity − r_host|, convert to kJ/mol dividing by 1000); W_A‑I = ¼(ΔH_subl.impurity + ΔH_subl.host) where the host atom is the nearest neighbour being replaced; Q_I = 4·W_A‑I − W_strain; ΔH_I = 4·W_A‑B (converted to kJ/mol) − Q_I; ΔS_I = S_B(gas) − S_I(gas) (B = P for Te, B = Ga for Zn); solve −RT ln(K_I) = ΔH_I − T·ΔS_I with R = 8.314 J/(K mol), T = 1200 K. Output the six quantities for each impurity into a JSON file with the specified schema.
- Output file: `/app/outputs/thermodynamic_quantities.json`
- Format: json
- Contract: {"impurities": [{"name": "Te", "W_strain_kJ_per_mol": <float>, "W_A-I_kJ_per_mol": <float>, "Q_I_kJ_per_mol": <float>, "Delta_H_I_kJ_per_mol": <float>, "Delta_S_I_J_per_K_per_mol": <float>, "K_I": <float>}, {"name": "Zn", "W_strain_kJ_per_mol": <float>, "W_A-I_kJ_per_mol": <float>, "Q_I_kJ_per_mol": <float>, "Delta_H_I_kJ_per_mol": <float>, "Delta_S_I_J_per_K_per_mol": <float>, "K_I": <float>}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_quantities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_quantities.json
- path: `/app/outputs/thermodynamic_quantities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed W_strain, W_A‑I, Q_I, ΔH_I, ΔS_I, and K_I for Te and Zn substitutional impurities in GaP via the bond‑energy/strain method.
- schema:
  - `type`: object
  - `required`:
    - `impurities`: array of objects
  - `items`:
    - `name`: string
    - `W_strain_kJ_per_mol`: number (kJ/mol)
    - `W_A-I_kJ_per_mol`: number (kJ/mol)
    - `Q_I_kJ_per_mol`: number (kJ/mol)
    - `Delta_H_I_kJ_per_mol`: number (kJ/mol)
    - `Delta_S_I_J_per_K_per_mol`: number (J/(K mol))
    - `K_I`: number (dimensionless)

Notes: All inputs are provided as explicit constants; the task does not require downloading external datasets or training models. The output is deterministic given the inputs, and scoring uses tolerance‑based comparison against the paper‑reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_quantities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "impurities": "array of objects"
        },
        "items": {
          "name": "string",
          "W_strain_kJ_per_mol": "number (kJ/mol)",
          "W_A-I_kJ_per_mol": "number (kJ/mol)",
          "Q_I_kJ_per_mol": "number (kJ/mol)",
          "Delta_H_I_kJ_per_mol": "number (kJ/mol)",
          "Delta_S_I_J_per_K_per_mol": "number (J/(K mol))",
          "K_I": "number (dimensionless)"
        }
      },
      "description": "Computed W_strain, W_A‑I, Q_I, ΔH_I, ΔS_I, and K_I for Te and Zn substitutional impurities in GaP via the bond‑energy/strain method."
    }
  ],
  "notes": "All inputs are provided as explicit constants; the task does not require downloading external datasets or training models. The output is deterministic given the inputs, and scoring uses tolerance‑based comparison against the paper‑reported values."
}
```

## How you are scored
After you submit your output, a hidden verifier will read your `thermodynamic_quantities.json` and compare each numeric field (W_strain, W_A‑I, Q_I, ΔH_I, ΔS_I, K_I for each impurity) against the corresponding reference values. Fields that fall within tolerances earn credit; the final reward is the weighted sum of the passes. The verifier does not require your code or intermediate files — only the final JSON artifact matters. Reporting the paper's numbers without performing the correct calculation will not succeed, because the verifier checks the values obtained from the defined formulas and inputs, not a copy of a pre‑known answer. Your task is to implement the method faithfully so that every computed quantity is correct.
