# Critical Nucleus Radius Calculation via Classical Nucleation Theory

## Problem background
Barium sulfate (BaSO₄) and potassium perchlorate (KClO₄) share the same crystal structure but differ widely in solubility. In crystal growth inhibition studies, it is observed that the more soluble salt requires higher additive concentrations to achieve the same level of inhibition. One proposed explanation is a surface-energy argument: the more soluble salt might have a lower surface energy, leading to more nuclei and a greater total surface area, thus requiring more additive. To test this hypothesis, classical nucleation theory can be used to compute the critical nucleus radius for each salt under the experimental conditions, providing a quantitative basis for evaluating the surface-energy argument.

## Approach
We employ classical nucleation theory (CNT) to estimate the critical nucleus radius for each salt. The critical radius R is determined from the balance between volume free energy and surface energy. For a nucleus with a cubic shape, the radius is given by the expression that involves the molecular volume V, interfacial surface tension γ, supersaturation ratio S, temperature T, and Boltzmann constant k_B. The shape factors are k_a = 6 (surface area) and k_v = 1 (volume), and the salt is assumed to dissociate into v = 2 ionic units. The free-energy driving force is φ = v·k_B·T·ln(S). The critical radius is then R = (2·k_a·V·γ²) / (3·k_v·φ). Compute R for both BaSO₄ and KClO₄ using the specific thermodynamic parameters supplied for each salt. The result is a purely deterministic computation with no fitting or stochastic elements.

## Reproduction target
Using the given CNT formulas and thermodynamic parameters, compute the critical nucleus radius (in nanometers) for BaSO₄ and KClO₄. Write the computed radii to the file /app/outputs/results.json as a JSON object with exactly two keys: R_BaSO4_nm and R_KClO4_nm, each holding a numeric value. This output is the sole scored artifact.

## Assets

- Python 3
- NumPy: numpy

## Workflow steps

### Step 1: Compute critical nucleus radii
- Role: scored
- Action: Implement classical nucleation theory to compute the critical nucleus radius (in nm) for BaSO₄ and KClO₄. Use shape factors k_a=6, k_v=1, dissociation number v=2 for both salts, and Boltzmann constant. Compute φ = v·k_B·T·ln(S) for each salt, then radius R = (2·k_a·V·γ²) / (3·k_v·φ). Use the provided thermodynamic values: for BaSO₄ — V=8.6638×10⁻²⁹ m³, γ=0.136 J/m², S=25, T=298 K; for KClO₄ — V=9.1263×10⁻²⁹ m³, γ=0.044 J/m², S=1.2, T=280 K. Output the two radii as a JSON object with keys R_BaSO4_nm and R_KClO4_nm.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"R_BaSO4_nm": "float, radius in nanometers", "R_KClO4_nm": "float, radius in nanometers"}
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
- target_policy: exact_match
- description: Critical nucleus radii for BaSO₄ and KClO₄ computed from classical nucleation theory. The checker recomputes these values independently and compares with a tight tolerance to account for floating-point differences.
- schema:
  - `type`: object
  - `required`:
    - `R_BaSO4_nm`: number
    - `R_KClO4_nm`: number
  - `units`:
    - `R_BaSO4_nm`: nm
    - `R_KClO4_nm`: nm

Notes: The calculation uses fixed deterministic inputs; the target policy is exact_match within a hidden tolerance. The nucleation rate calculation is excluded per feasibility scope.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "R_BaSO4_nm": "number",
          "R_KClO4_nm": "number"
        },
        "units": {
          "R_BaSO4_nm": "nm",
          "R_KClO4_nm": "nm"
        }
      },
      "description": "Critical nucleus radii for BaSO₄ and KClO₄ computed from classical nucleation theory. The checker recomputes these values independently and compares with a tight tolerance to account for floating-point differences."
    }
  ],
  "notes": "The calculation uses fixed deterministic inputs; the target policy is exact_match within a hidden tolerance. The nucleation rate calculation is excluded per feasibility scope."
}
```

## How you are scored
A hidden verifier independently computes the expected critical nucleus radii using the same CNT formulas and input parameters. It reads your /app/outputs/results.json and compares your reported R_BaSO4_nm and R_KClO4_nm against the independently computed values. Scoring is based on the closeness of your numbers to the expected values: a perfect match (within a tolerance that accounts for normal floating‑point differences) earns full credit, and larger deviations reduce the score. The verifier does not look at your code, only at the JSON output.
