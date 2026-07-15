# Bragg-Williams-Gorsky thermodynamic model for ordering-induced martensitic transformation temperature shift

## Problem background
Some alloys exhibit a martensitic transformation temperature that depends on the degree of long-range order in the parent phase. This work computes the theoretical relationship between the shift of the equilibrium transformation temperature and the order parameter for a Ag-Zn-Al type alloy, using the Bragg-Williams-Gorsky (BWG) thermodynamic approximation. The parent phase has a C11b ordered structure, and the martensitic phase is approximated as fcc-based. The goal is to derive the coefficient of the quadratic law relating the temperature shift to an experimentally defined order parameter, thereby quantifying the ordering effect on the relative stability of the two phases.

## Approach
The approach is a thermodynamic free energy analysis under the Bragg-Williams-Gorsky (BWG) approximation. The free energies of the ordered parent β phase (C11b structure) and the martensitic α phase (approximated as fcc-based) are expressed in terms of exchange interaction energies between atomic neighbours (first and second neighbour for the parent, first neighbour for the martensite) and the temperature-dependent free energy differences of the pure metals between bcc and fcc structures. All necessary energy parameters and concentration values are provided as given inputs.

The free energy difference ΔG = G^α – G^β is written as a function of temperature T and the BWG order parameter η, for an effective solute concentration c_eff=0.4. The expression is reduced to the form ΔG = A + B η^2 + C T (J/mol). Setting ΔG = 0 yields the equilibrium transformation temperature T0(η). The shift ΔT0 = T0(η) – T0(0) is then expressed as a quadratic in η, and its coefficient is extracted. Finally, the BWG order parameter η is converted to the experimentally defined normalized long-range order parameter φ via the relation η = 2c φ, where c is a given solute concentration. Substituting this conversion yields the final quadratic law ΔT0 = C φ^2, whose coefficient C is the primary reproduction target.

## Reproduction target
Implement the BWG thermodynamic model using the provided exchange interaction energies (W^(1), W^(2), W) and pure-metal free energy differences (ΔG_Ag(T), ΔG_Zn(T)). For effective solute concentration c_eff=0.4, compute the three coefficients A, B, C of the free energy difference expression ΔG = A + B η^2 + C T in J/mol. Solve ΔG = 0 to obtain the equilibrium transformation temperature T0(η) and derive the coefficient D in ΔT0 = D η^2 (K). Then, using the conversion η = 2c φ with c=0.312, obtain the final coefficient C in the quadratic law ΔT0 = C φ^2 (K). Report the results in the three JSON output files exactly as specified in the workflow steps and output contract.

## Assets

- Python scientific computing stack (numpy): numpy

## Workflow steps

### Step 1: Assemble ΔG coefficients
- Role: scored
- Action: Using the Bragg-Williams-Gorsky (BWG) approximation for the parent β (C11b) and martensitic α (approximated as fcc-based) phases of Ag-Zn-Al. Accept given exchange energies: W^(1)=5.61 kJ/mol, W^(2)=3.15 kJ/mol, W=3.43 kJ/mol. Compute enthalpy coefficients for parent: E^β = -(4W^(1)+3W^(2)), F^β = -(4W^(1)-3W^(2))/4; for martensitic: E^α = -6W, F^α = -W/2. Accept given pure-metal free energy differences (bcc vs fcc): ΔG_Ag(T) = -4.58 + 0.00154·T kJ/mol, ΔG_Zn(T) = -1.23 - 0.000556·T kJ/mol. Build the free energy difference ΔG = G^α – G^β for effective solute concentration c_eff=0.4: ΔG = (1-c_eff)ΔG_Ag(T) + c_eff ΔG_Zn(T) + (E^α - E^β) c_eff (1-c_eff) + (F^α - F^β) η^2. Simplify to ΔG = A + B·η^2 + C·T in J/mol. Write the coefficients A, B, C to the output file.
- Output file: `/app/outputs/delta_g_coefficients.json`
- Format: json
- Contract: {"A": number, "B": number, "C": number}
- Scoring: scored by hidden verifier

### Step 2: Derive ΔT0 coefficient in η
- Role: scored
- Action: Set ΔG = 0 using the assembled expression to solve for the equilibrium transformation temperature T0(η). Compute the shift ΔT0 = T0(η) – T0(0) as a function of η^2, and extract the coefficient D in ΔT0 = D·η^2 [K]. Write D to the output file.
- Output file: `/app/outputs/delta_T0_eta_coefficient.json`
- Format: json
- Contract: {"coefficient_eta2": number}
- Scoring: scored by hidden verifier

### Step 3: Convert to φ and report final law
- Role: scored (load-bearing)
- Action: Convert the BWG order parameter η to the experimentally defined normalized long-range order parameter φ using η = 2c·φ with c = 0.312 (Zn+Al concentration). Substitute into ΔT0 = D·η^2 to obtain ΔT0 = C·φ^2, and compute C. Write C to the output file.
- Output file: `/app/outputs/final_coefficient.json`
- Format: json
- Contract: {"coefficient_phi2": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_g_coefficients.json`
- `/app/outputs/delta_T0_eta_coefficient.json`
- `/app/outputs/final_coefficient.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_g_coefficients.json
- path: `/app/outputs/delta_g_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Coefficients A, B, C in ΔG = A + B·η² + C·T [J/mol] for c_eff=0.4. Scored by reference_match against paper-derived values with tolerances.
- schema:
  - `type`: object
  - `required`: `A`, `B`, `C`
  - `properties`:
    - `A`:
      - `type`: number
      - `units`: J/mol
    - `B`:
      - `type`: number
      - `units`: J/mol
    - `C`:
      - `type`: number
      - `units`: J/(mol·K)

### delta_T0_eta_coefficient.json
- path: `/app/outputs/delta_T0_eta_coefficient.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Coefficient D in ΔT₀ = D·η² [K], derived by solving ΔG=0. Scored by recomputation: verifier independently computes D from the provided ΔG coefficients and checks consistency.
- schema:
  - `type`: object
  - `required`: `coefficient_eta2`
  - `properties`:
    - `coefficient_eta2`:
      - `type`: number
      - `units`: K

### final_coefficient.json
- path: `/app/outputs/final_coefficient.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final coefficient C in ΔT₀ = C·φ² [K] after conversion. Scored by recomputation from ΔG coefficients and conversion formula.
- schema:
  - `type`: object
  - `required`: `coefficient_phi2`
  - `properties`:
    - `coefficient_phi2`:
      - `type`: number
      - `units`: K

Notes: Step 1 uses reference_match with tolerances; steps 2 and 3 are consistency checks where the verifier recomputes the coefficient from previous outputs, equivalent to metric_recompute.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_g_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "A",
          "B",
          "C"
        ],
        "properties": {
          "A": {
            "type": "number",
            "units": "J/mol"
          },
          "B": {
            "type": "number",
            "units": "J/mol"
          },
          "C": {
            "type": "number",
            "units": "J/(mol·K)"
          }
        }
      },
      "description": "Coefficients A, B, C in ΔG = A + B·η² + C·T [J/mol] for c_eff=0.4. Scored by reference_match against paper-derived values with tolerances."
    },
    {
      "file": "delta_T0_eta_coefficient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "coefficient_eta2"
        ],
        "properties": {
          "coefficient_eta2": {
            "type": "number",
            "units": "K"
          }
        }
      },
      "description": "Coefficient D in ΔT₀ = D·η² [K], derived by solving ΔG=0. Scored by recomputation: verifier independently computes D from the provided ΔG coefficients and checks consistency."
    },
    {
      "file": "final_coefficient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "coefficient_phi2"
        ],
        "properties": {
          "coefficient_phi2": {
            "type": "number",
            "units": "K"
          }
        }
      },
      "description": "Final coefficient C in ΔT₀ = C·φ² [K] after conversion. Scored by recomputation from ΔG coefficients and conversion formula."
    }
  ],
  "notes": "Step 1 uses reference_match with tolerances; steps 2 and 3 are consistency checks where the verifier recomputes the coefficient from previous outputs, equivalent to metric_recompute."
}
```

## How you are scored
A hidden verifier reads the three JSON output files and independently compares each reported coefficient to the values derived from the theoretical model in the source paper, using appropriate numerical tolerances to account for minor implementation differences. Each workflow stage carries a weight, and the final reward is the weighted sum of the stage scores. Simply reporting numbers without executing the full thermodynamic derivation is not sufficient; the verifier may check consistency across stages to ensure the reported values follow from the given inputs and the BWG treatment.
