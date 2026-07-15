# 1D Two-Bar Impact via Acoustic Riemann Solver

## Problem background
When two elastic bodies collide, shock waves propagate from the contact point, creating discontinuities in velocity and stress. Accurately capturing the transition between contact and separation is a long-standing challenge in computational contact dynamics, where standard methods often introduce numerically motivated dissipation or require ad‑hoc parameters. An alternative approach uses a system of first‑order conservation laws written in terms of linear momentum and geometric deformation measures, together with the associated Rankine‑Hugoniot jump conditions across moving shocks. By assuming the shock speeds after contact equal the material sound speeds (the acoustic approximation), these jump conditions yield closed‑form expressions for the common contact velocity and traction and, later, for the release velocities when the bodies separate. In this task you will implement this acoustic Riemann solver for the simplest frictionless one‑dimensional case: two identical elastic bars impacting and then separating, and compute the key contact and final‑state quantities.

## Approach
The solver is built on the one‑dimensional forms of the jump conditions that link velocity and traction before and after a discontinuity. At impact, a Riemann problem arises at the contact interface; enforcing the jump conditions for both bars together with traction‑free conditions before contact gives the common (contact‑stick) velocity and the normal traction that persists during contact. The same jump conditions, applied again when the tensile reflected waves return to the contact point, determine the release velocities of each bar after separation. The calculation is deterministic for the given geometry, material properties, and initial conditions. You will implement a time‑domain simulation that tracks the wave propagation until separation is complete and extract the needed quantities at the appropriate instants. The simulation uses linear elasticity with the prescribed one‑dimensional sound speed, and the contact logic follows the algorithm of contact‑stick while the bars are pushed together and separation when the traction becomes tensile. No external data or pre‑trained models are required; you will write all code from scratch within the environment.

## Reproduction target
Implement the acoustic Riemann solver for the one‑dimensional two‑bar impact problem described above. Use the following fixed parameters:

* Young's modulus \(E = 100\ \text{N/m}^2\)
* Reference density \(\rho_R = 0.01\ \text{kg/m}^3\)
* Poisson's ratio \(\nu = 0.0\) (reduces the sound speed to \(c_p = \sqrt{E/\rho_R}\))
* Bar length \(L = 20\ \text{m}\)
* Initial gap between the bars \(\delta = 0.01\ \text{m}\)
* Left bar initial velocity \(v_0 = 0.1\ \text{m/s}\) (moving to the right)
* Right bar initially at rest.

Simulate from \(t = 0\) until after separation (i.e., until a time greater than \(0.3\ \text{s}\)). From the simulation, extract four scalar quantities and write them as a single JSON file at the path specified in the workflow step. The quantities are:

1. **contact_velocity** — the common velocity \(v_x^C\) of the two bars at the instant of impact.
2. **contact_traction** — the traction \(t_x^C\) acting across the contact interface at that same instant.
3. **left_release_velocity** — the final velocity of the left bar after separation.
4. **right_release_velocity** — the final velocity of the right bar after separation.

All quantities should be reported in SI units (velocity in \(\text{m/s}\), traction in \(\text{N/m}^2\)). The output file must conform to the JSON schema shown in the output contract.

## Assets
No external datasets, models, or special tools are required. The workflow uses only standard numerical computing libraries available in Python (e.g., NumPy, SciPy) or any other language you choose. You may install any needed packages at runtime using the Tsinghua PyPI mirror:
```bash
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple <packages>
```

## Workflow steps

### Step 1: 1D two-bar impact simulation and result output
- Role: scored (load-bearing)
- Action: Implement the acoustic Riemann solver for the one-dimensional two-bar impact problem using the given material parameters (E=100 N/m^2, ρ_R=0.01 kg/m^3, ν=0.0, bar length L=20 m, initial gap δ=0.01 m, left bar initial velocity v0=0.1 m/s, right bar at rest). Simulate from t=0 until after separation (t > 0.3 s). Output a JSON file containing the common contact velocity v_x^C and traction t_x^C at impact, and the final velocities of the left and right bars after separation.
- Output file: `/app/outputs/contact_analytical_check.json`
- Format: json
- Contract: {"type": "object", "required": {"contact_velocity": "float", "contact_traction": "float", "left_release_velocity": "float", "right_release_velocity": "float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contact_analytical_check.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contact_analytical_check.json
- path: `/app/outputs/contact_analytical_check.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file with four floating-point fields: contact velocity and traction at impact, and post-separation velocities of left and right bars. The checker compares each value to the paper's analytical solutions with predefined tolerances.
- schema:
  - `type`: object
  - `required`:
    - `contact_velocity`: float (m/s)
    - `contact_traction`: float (N/m^2)
    - `left_release_velocity`: float (m/s)
    - `right_release_velocity`: float (m/s)

Notes: The quantities are deterministic for the given inputs. Tolerances account for numerical discretization errors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contact_analytical_check.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "contact_velocity": "float (m/s)",
          "contact_traction": "float (N/m^2)",
          "left_release_velocity": "float (m/s)",
          "right_release_velocity": "float (m/s)"
        }
      },
      "description": "JSON file with four floating-point fields: contact velocity and traction at impact, and post-separation velocities of left and right bars. The checker compares each value to the paper's analytical solutions with predefined tolerances."
    }
  ],
  "notes": "The quantities are deterministic for the given inputs. Tolerances account for numerical discretization errors."
}
```

## How you are scored
After you submit your output, a hidden verifier reads only the file `contact_analytical_check.json` from `/app/outputs`. It validates that the JSON matches the required schema, extracts the four numerical fields, and compares them to the exact analytical solutions derived from the jump conditions with the given parameters. Each field is checked with an appropriate absolute tolerance that accounts for typical numerical discretisation effects. The four toleranced comparisons are then combined (with equal weight) into a final reward between 0 and 1. Reporting numerical values that are close to the analytical references yields high reward; the verifier does **not** look at any internal simulation data, logs, or code.
