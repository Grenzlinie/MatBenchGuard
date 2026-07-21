# Eccentricity Valley Hall Angle from Drude Model

## Problem background
Valleytronics exploits the valley degree of freedom for information processing. A central effect is the valley Hall effect (VHE), where a longitudinal charge current generates a transverse valley current. In conventional VHE, the valley Hall angle depends sensitively on scattering time and carrier density. This work investigates a new type of VHE in systems with time-reversal-invariant valleys (TRIVs), where each valley sits at a time-reversal-invariant momentum point. The valley Hall angle in such systems can be determined solely by the geometry of the valley Fermi surface. In particular, for two TRIVs connected by fourfold rotational symmetry, the valley Hall angle is predicted to depend only on the eccentricity of the Fermi ellipse and the orientation of the driving electric field, making it robust against temperature and doping variations. Your task is to reproduce this eccentricity VHE from a Drude transport model.

## Approach
You will implement the Drude model for a pair of TRIVs connected by C4z symmetry. Start by writing an effective Hamiltonian for a single valley: an anisotropic quadratic band with principal axes along x and y, characterized by the ratio of semi-axes λ = ay/ax. From the band velocities, compute the diagonal Drude conductivities for that valley. Then apply the symmetry operation linking the two valleys to obtain the conductivity tensor of the second valley. For a given in‑plane electric field direction φ, compute the longitudinal charge current (parallel to the field) and the transverse valley current (perpendicular to the field), both in arbitrary units (the common drift prefactor μτ/2π can be omitted). From these, calculate the magnitude of the valley Hall angle and the Fermi‑ellipse eccentricity e. The computation should be implemented as a self‑contained script that accepts λ and φ as inputs and writes the four quantities to a JSON file.

## Reproduction target
Produce a file named step_02_results.json containing the input parameters (λ, φ) and the computed values: longitudinal_current, transverse_valley_current, valley_hall_angle, and derived_eccentricity. The valley Hall angle is the absolute ratio of transverse valley current to longitudinal charge current. The eccentricity is derived from λ as e = sqrt(1 − λ⁻²). All quantities are in arbitrary units. The parameter λ should be greater than 1, and φ in radians. You may use any open‑source numerical environment (Python with numpy is recommended). The file must strictly follow the supplied JSON schema.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute eccentricity valley Hall angle
- Role: scored (load-bearing)
- Action: Implement the Drude model for a pair of time-reversal-invariant valleys (TRIVs) connected by C4z symmetry, using an effective elliptic Hamiltonian. For a given ratio of semi-axes λ and in-plane electric field angle φ, compute the longitudinal charge current, transverse valley current, and the resulting valley Hall angle (magnitude). Also compute the Fermi-ellipse eccentricity. Write the results to step_02_results.json.
- Output file: `/app/outputs/step_02_results.json`
- Format: json
- Contract: {
  "parameters": {
    "lambda": "float",
    "phi": "float"
  },
  "longitudinal_current": "float",
  "transverse_valley_current": "float",
  "valley_hall_angle": "float",
  "derived_eccentricity": "float"
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_results.json
- path: `/app/outputs/step_02_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The checker recomputes the expected valley Hall angle from the reported lambda and phi, compares it to the reported valley_hall_angle within a tolerance, and verifies consistency of the other quantities.
- schema:
  - `type`: object
  - `required`:
    - `parameters`:
      - `lambda`: number
      - `phi`: number
    - `longitudinal_current`: number
    - `transverse_valley_current`: number
    - `valley_hall_angle`: number
    - `derived_eccentricity`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "parameters": {
            "lambda": "number",
            "phi": "number"
          },
          "longitudinal_current": "number",
          "transverse_valley_current": "number",
          "valley_hall_angle": "number",
          "derived_eccentricity": "number"
        }
      },
      "description": "The checker recomputes the expected valley Hall angle from the reported lambda and phi, compares it to the reported valley_hall_angle within a tolerance, and verifies consistency of the other quantities."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is assessed by a hidden verifier that reads your step_02_results.json. The verifier extracts the parameters λ and φ, then independently computes the expected valley Hall angle from a known geometric formula. It compares this expected value to your reported valley_hall_angle, assigning high reward for close agreement. It also verifies that your derived_eccentricity is consistent with λ and that the longitudinal and transverse currents follow the Drude relations up to a common factor. Each scored quantity contributes to a final reward between 0 and 1; the valley Hall angle carries the largest weight. Simply reporting numbers without actually running the computation will not yield a passing score, because the verifier's check is based on internal consistency and the hidden formula.
