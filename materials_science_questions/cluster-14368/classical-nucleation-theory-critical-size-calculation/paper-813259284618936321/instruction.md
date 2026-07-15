# Classical Nucleation Theory Critical Size Calculation for Xenon Clusters

## Problem background
Free xenon clusters with N≈2000–8000 atoms exhibit a noncrystalline surface shell. The paper argues this shell can be in a pseudocrystalline state — a structurally unstable phase constantly fluctuating between liquid and solid — if a thermodynamic condition holds. The key condition is that, for cluster radii below a critical value Rc, the surface melting temperature Ts must be higher than the size‑dependent cluster melting temperature Tm_cl. Verifying this claim requires calculating Ts, Tm_cl for specific cluster sizes, and Rc from classical nucleation theory using bulk xenon parameters.

## Approach
Apply the finite‑size melting temperature formula from classical nucleation theory: Tm_cl = Tm * (1 − R0 / R), where Tm is the bulk melting temperature and R0 is a material‑dependent length computed from the surface tensions, heat of fusion, and solid density. Use the provided xenon constants (Tm = 161.4 K, σ_s = 61 erg/cm², σ_l = 18.8 erg/cm², q = 3.7×10⁻¹⁴ erg, ρ_s = 1.7×10²² cm⁻³) to obtain R0. Calculate Tm_cl for radii corresponding to N≈3000 atoms (R≈35 Å) and N≈6000 atoms (R≈44 Å). The surface melting temperature is defined as Ts = 0.8·Tm. Determine the critical radius Rc by numerically solving Ts = Tm_cl. Finally, evaluate whether the radii for N≈3000 and N≈6000 are smaller than Rc. Report all quantities in a structured JSON file.

## Reproduction target
Write a single JSON file `/app/outputs/results.json` containing the following computed fields:

- `critical_radius_Rc` (float, in Å) – the critical radius where Ts = Tm_cl.
- `Tm_cl_3000` (float, in K) – the cluster melting temperature for N≈3000 (radius ≈35 Å).
- `Tm_cl_6000` (float, in K) – the cluster melting temperature for N≈6000 (radius ≈44 Å).
- `Ts` (float, in K) – the surface melting temperature.
- `inequality_holds` (bool) – `true` if the surface melting temperature exceeds the cluster melting temperature for radii below Rc, `false` otherwise.

The task is complete when this file is produced with the above structure.

## Assets
No external datasets, models, or tools are required. All necessary numerical constants are provided in the approach section. The computation can be performed using standard Python libraries such as NumPy and SciPy (e.g., for root‑finding).

## Workflow steps

### Step 1: Compute thermodynamic parameters and critical radius
- Role: scored (load-bearing)
- Action: Implement the finite-size melting temperature formula using classical nucleation theory for xenon clusters. Compute the parameter R0 from the given surface tensions, heat of fusion, and solid density. Calculate cluster melting temperatures Tm_cl for conditions corresponding to N ≈ 3000 (radius ≈ 35 Å) and N ≈ 6000 (radius ≈ 44 Å). Compute surface melting temperature Ts = 0.8 * Tm, where Tm = 161.4 K. Determine the critical radius Rc by numerically solving Ts = Tm_cl. Record all computed values in results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: critical_radius_Rc (float, units Å), Tm_cl_3000 (float, K), Tm_cl_6000 (float, K), Ts (float, K), inequality_holds (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic results supporting the pseudocrystalline state: critical radius, cluster melting temperatures, surface melting temperature, and inequality verification.
- schema:
  - `type`: object
  - `required`:
    - `critical_radius_Rc`: float (Å)
    - `Tm_cl_3000`: float (K)
    - `Tm_cl_6000`: float (K)
    - `Ts`: float (K)
    - `inequality_holds`: bool
  - `items`: object
  - `required_columns`:
  - `units`:
    - `critical_radius_Rc`: Å
    - `Tm_cl_3000`: K
    - `Tm_cl_6000`: K
    - `Ts`: K

Notes: The checker compares the reported values against paper-reported reference values within predefined tolerances. The boolean inequality_holds must match exactly (true). No additional process steps are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "critical_radius_Rc": "float (Å)",
          "Tm_cl_3000": "float (K)",
          "Tm_cl_6000": "float (K)",
          "Ts": "float (K)",
          "inequality_holds": "bool"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "critical_radius_Rc": "Å",
          "Tm_cl_3000": "K",
          "Tm_cl_6000": "K",
          "Ts": "K"
        }
      },
      "description": "Thermodynamic results supporting the pseudocrystalline state: critical radius, cluster melting temperatures, surface melting temperature, and inequality verification."
    }
  ],
  "notes": "The checker compares the reported values against paper-reported reference values within predefined tolerances. The boolean inequality_holds must match exactly (true). No additional process steps are required."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares each numeric field (critical_radius_Rc, Tm_cl_3000, Tm_cl_6000, Ts) against reference values within predetermined tolerances. The boolean `inequality_holds` is checked for correctness. Each field is scored independently with a weight that reflects its importance, and the final reward is the weighted sum. You must produce the exact file format and structure described; reporting only the final numbers is not sufficient. The verifier does not run your code – it only inspects the output file.
