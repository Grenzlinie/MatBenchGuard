# Compute Uniaxial Stress Dependence of Al Fermi Surface Orbits via Four‑OPW Model

## Problem background
The uniaxial stress dependence of Fermi‑surface orbits in aluminium provides a sensitive test of pseudopotential models for simple metals. This task focuses on the theoretical determination of the quantity (1/A)(∂A/∂σ) — the relative change of an extremal orbit area A with uniaxial stress σ applied along the [001] direction. Six distinct orbits (γ1, γ2, α1, α2, β1, β2) of the third‑band Fermi surface are to be characterised. The result is a benchmark for the four‑OPW pseudopotential description of the metal.

## Approach
Implement the four‑OPW (orthogonalised‑plane‑wave) pseudopotential model for aluminium. The secular determinant is formed in terms of the axial ratio ρ = a/c, where a and c are the transverse and longitudinal lattice spacings. Zero‑pressure parameters are taken from Ashcroft: pseudopotential matrix elements V1=0.00855 a.u., V2=V3=0.0281 a.u., and Fermi energy EF=0.4280 a.u. The stress‑dependence of the form factor is modelled using the Heine‑Animalu slopes (∂V/∂q at q1=0.13, at q2=0.07 a.u.). For each of the six orbits, obtain the extremal cross‑sectional area A(ρ) by solving the secular equation in the vicinity of ρ=1, taking into account the Fermi‑energy correction and the ρ‑dependence of the reciprocal‑lattice vectors. Numerically compute (1/A)(dA/dρ) and convert to (1/A)(∂A/∂σ) using the elastic‑constants conversion dρ/dσ = –1.927×10⁻⁶ bar⁻¹. The final values are reported in units of 10⁻⁵ bar⁻¹.

## Reproduction target
Compute, from the four‑OPW model with Heine‑Animalu slopes, the uniaxial stress dependence (1/A)(∂A/∂σ) for the six Fermi‑surface orbits γ1, γ2, α1, α2, β1, β2. Write the results as a JSON array of objects, each with the orbit name and the stress_dependence value in units of 10⁻⁵ bar⁻¹.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute theoretical stress dependence for six orbits
- Role: scored (load-bearing)
- Action: Implement the four‑OPW pseudopotential model for aluminum: define the secular determinant with ρ‑dependent reciprocal‑lattice vectors and the Fermi‑energy correction, using the zero‑pressure parameters V1=0.00855 a.u., V2=V3=0.0281 a.u., EF=0.4280 a.u. For each of the six orbits (γ1, γ2, α1, α2, β1, β2) determine the extremal cross‑sectional area A(ρ) as a function of the axial ratio ρ near ρ=1 by solving the secular equation. Use the Heine‑Animalu form factor slopes (∂V/∂q at q1=0.13, at q2=0.07 a.u.) to compute ∂V_i/∂ρ and thereby (1/A)(dA/dρ). Convert to (1/A)(∂A/∂σ) using dρ/dσ = −1.927×10⁻⁶ bar⁻¹. Write a JSON array containing six objects, each with fields 'orbit' and 'stress_dependence' (value in units 10⁻⁵ bar⁻¹).
- Output file: `/app/outputs/stress_dependence_values.json`
- Format: json
- Contract: An array of six objects: [{"orbit": "gamma1", "stress_dependence": <float>}, {"orbit": "gamma2", ...}, {"orbit": "alpha1", ...}, {"orbit": "alpha2", ...}, {"orbit": "beta1", ...}, {"orbit": "beta2", ...}]. stress_dependence is a floating‑point number in units of 10⁻⁵ bar⁻¹.
- Scoring: scored by hidden verifier


## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_dependence_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_dependence_values.json
- path: `/app/outputs/stress_dependence_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed uniaxial stress dependence for the six Fermi‑surface orbits. The checker compares each stress_dependence value to the paper‑reported theoretical value with an absolute tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `orbit`:
        - `type`: string
        - `enum`: `gamma1`, `gamma2`, `alpha1`, `alpha2`, `beta1`, `beta2`
      - `stress_dependence`:
        - `type`: number
        - `unit`: 10^{-5} bar^{-1}

Notes: Only the theoretical four‑OPW calculation with Heine‑Animalu slopes is scored. The subsequent fitting of pseudopotential slopes from experimental data is omitted because it requires the experimental stress‑dependence values as input and falls outside the scoped reproduction task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_dependence_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "orbit": {
              "type": "string",
              "enum": [
                "gamma1",
                "gamma2",
                "alpha1",
                "alpha2",
                "beta1",
                "beta2"
              ]
            },
            "stress_dependence": {
              "type": "number",
              "unit": "10^{-5} bar^{-1}"
            }
          }
        }
      },
      "description": "Computed uniaxial stress dependence for the six Fermi‑surface orbits. The checker compares each stress_dependence value to the paper‑reported theoretical value with an absolute tolerance."
    }
  ],
  "notes": "Only the theoretical four‑OPW calculation with Heine‑Animalu slopes is scored. The subsequent fitting of pseudopotential slopes from experimental data is omitted because it requires the experimental stress‑dependence values as input and falls outside the scoped reproduction task."
}
```

## How you are scored
A hidden verifier reads your output file stress_dependence_values.json and compares each orbit's stress_dependence value to a hidden theoretical reference. Each of the six orbits contributes an equal share to the final reward; the closer your computed values are to the expected results, the higher your score.
