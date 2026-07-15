# Classical Nucleation Theory Critical Size Calculation

## Problem background
Fast moving bed pyrolysis enables the synthesis of ultrasmall, highly dispersed high-entropy alloy nanoparticles (HEA-NPs) on granular supports. A key thermodynamic question is why high‑temperature rapid pyrolysis yields small, homogeneous nuclei without phase separation. Classical nucleation theory (CNT) addresses this by relating the critical nucleus radius and the associated free‑energy barrier to temperature and supersaturation, thus providing a thermodynamic explanation for the observed size and uniformity of the nuclei.

## Approach
Implement the classical nucleation theory (CNT) model for a spherical nucleus. The critical nucleus radius r* is given by the Kelvin equation, and the critical excess free energy ΔG is obtained from the balance of surface and volume contributions. The required formulas are:
r* = 2 γ V_m / (R T ln S)
ΔG = 4 π r*² γ − (4/3) π r*³ (R T ln S / V_m)
All parameters are provided: surface free energy γ = 0.3 J m⁻², solid molar volume V_m = 8.0×10⁻⁶ m³ mol⁻¹, supersaturation ratio S = 10, and the ideal gas constant R = 8.314 J mol⁻¹ K⁻¹. Compute r* (converted to nanometers) and ΔG (in joules) at two nucleation temperatures, T = 673 K and T = 923 K, and write the results to a JSON file.

## Reproduction target
Produce a JSON file containing four computed values: the critical nucleus radius at 673 K (nm), the critical excess free energy at 673 K (J), the critical nucleus radius at 923 K (nm), and the critical excess free energy at 923 K (J). All values must be derived from the CNT equations using the given parameters; no other data sources are needed.

## Assets
None. All required constants (γ, V_m, S, R) and the two temperatures are supplied in the task instructions. No external datasets, models, or tools must be fetched.

## Workflow steps

### Step 1: CNT critical radius and free-energy barrier computation
- Role: scored (load-bearing)
- Action: Using classical nucleation theory (CNT): r* = 2γV_m/(RT ln S) and ΔG = 4πr*²γ - (4/3)πr*³ (RT ln S/V_m). Given parameters: γ = 0.3 J m⁻², V_m = 8.0×10⁻⁶ m³ mol⁻¹, S = 10, R = 8.314 J mol⁻¹ K⁻¹. Compute r* (converted to nm) and ΔG (in J) at T = 673 K and T = 923 K. Write the four numerical values as a JSON object.
- Output file: `/app/outputs/step_01_nucleation_results.json`
- Format: json
- Contract: object with keys: r_star_673K (float, nm), deltaG_star_673K (float, J), r_star_923K (float, nm), deltaG_star_923K (float, J)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_nucleation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_nucleation_results.json
- path: `/app/outputs/step_01_nucleation_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical nucleus radius and free-energy barrier at 673 K and 923 K computed from classical nucleation theory with the provided parameters.
- schema:
  - `type`: object
  - `required`:
    - `r_star_673K`: float (nm)
    - `deltaG_star_673K`: float (J)
    - `r_star_923K`: float (nm)
    - `deltaG_star_923K`: float (J)

Notes: All necessary constants (γ, V_m, S, R) are given in the instruction. The checker will compare these deterministic computed values against the paper's reported results using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_nucleation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "r_star_673K": "float (nm)",
          "deltaG_star_673K": "float (J)",
          "r_star_923K": "float (nm)",
          "deltaG_star_923K": "float (J)"
        }
      },
      "description": "Critical nucleus radius and free-energy barrier at 673 K and 923 K computed from classical nucleation theory with the provided parameters."
    }
  ],
  "notes": "All necessary constants (γ, V_m, S, R) are given in the instruction. The checker will compare these deterministic computed values against the paper's reported results using appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your output JSON file and independently compares the four numerical values against the correct answers derived from the same CNT formulas with the same parameters. Scoring is deterministic: each value must be correct within a strict numeric tolerance; all four values must pass for full credit. Merely reporting numbers without proper computation will not meet the scoring criteria. The verifier does not access the internet and uses only the contents of /app/outputs.
