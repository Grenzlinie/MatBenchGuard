# Dipole Moment Calculation for Si–O and Si–O–Si Configurations

## Problem background
Oxygen atoms incorporated on oxidized silicon surfaces form Si–O bonds and Si–O–Si bridge configurations. The dipole moments of these molecular entities govern the ability to trap localized electrons, which is essential for nanoscale memory devices. This work evaluates the dipole moments of Si–O and Si–O–Si configurations using Slater-type atomic orbitals and applies a critical dipole moment criterion to predict which configurations can support a localized bound electron state.

## Approach
The method uses analytical integration of Slater atomic orbital products. For the Si–O bond, the dipole moment is computed by evaluating the overlap integral of the Si 3p and O 2p orbitals over the volume of the oxygen atom (covalent radius), scaled by the Si–O bond length. For the Si–O–Si bridge at zero displacement, the integral involves products of four orbitals (two silicon and two oxygen) with the appropriate geometry. The paper provides explicit Slater-type atomic orbital wavefunctions for Si (3p) and O (2p), as well as the geometry parameters (Si–O bond length 1.6 Å, oxygen covalent radius). After obtaining the dipole moments, the results are compared against the Lakhno critical dipole moment (0.318 D) to determine whether each configuration can localize a bound electron.

## Reproduction target
Compute the dipole moment of the Si–O bond and the dipole moment at zero displacement of the Si–O–Si bridge using the provided Slater orbital expressions and integral formulas. Report both values in Debye. Then apply the Lakhno criterion with the critical dipole moment of 0.318 D to determine whether each configuration supports a localized bound electron state.

## Assets
No external datasets, models, or pre-trained weights are required. The necessary Slater atomic orbital wavefunctions, geometry parameters, and integral formulas are fully described in the problem background and approach sections of this instruction.

## Workflow steps

### Step 1: Compute dipole moments and evaluate Lakhno criterion
- Role: scored (load-bearing)
- Action: Calculate the dipole moments for the Si–O bond and the Si–O–Si bridge. Use the provided Slater-type atomic orbital wavefunctions for Si (3p) and O (2p). For the Si–O bond, evaluate the overlap integral of the product of the 3p_x Si and 2p_x O orbitals integrated over the volume of the oxygen atom (covalent radius), with the integrand scaled by the Si–O bond length (1.6 Å). For the Si–O–Si bridge at zero displacement, evaluate the integral for the product of the two relevant silicon and two oxygen orbitals with the appropriate geometry. Report both dipole moments in Debye. Then compare each computed value to the Lakhno critical dipole moment (0.318 D) to determine whether a localized bound electron state can exist.
- Output file: `/app/outputs/dipole_moments.json`
- Format: json
- Contract: {"mu_Si_O": "number (float, in Debye)", "mu_Si_O_Si_0": "number (float, in Debye)", "mu_critical": 0.318}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_moments.json
- path: `/app/outputs/dipole_moments.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed dipole moments for the Si–O bond and the Si–O–Si bridge, together with the Lakhno critical dipole moment (0.318 D). The hidden checker compares the submitted values to paper-reported reference dipole moments within a tolerance regime and verifies the inequality µ_Si‑O > µ_critical and µ^0_Si‑O‑Si < µ_critical.
- schema:
  - `type`: object
  - `required`: `mu_Si_O`, `mu_Si_O_Si_0`, `mu_critical`
  - `properties`:
    - `mu_Si_O`:
      - `type`: number
      - `units`: Debye
    - `mu_Si_O_Si_0`:
      - `type`: number
      - `units`: Debye
    - `mu_critical`:
      - `const`: 0.318

Notes: The scoring verifier compares the computed dipole moments to hidden reference values and checks the Lakhno criterion inequalities. No external datasets or model files are required; the agent implements the integrals from the publicly available Slater orbital descriptions and geometry parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "mu_Si_O",
          "mu_Si_O_Si_0",
          "mu_critical"
        ],
        "properties": {
          "mu_Si_O": {
            "type": "number",
            "units": "Debye"
          },
          "mu_Si_O_Si_0": {
            "type": "number",
            "units": "Debye"
          },
          "mu_critical": {
            "const": 0.318
          }
        }
      },
      "description": "Computed dipole moments for the Si–O bond and the Si–O–Si bridge, together with the Lakhno critical dipole moment (0.318 D). The hidden checker compares the submitted values to paper-reported reference dipole moments within a tolerance regime and verifies the inequality µ_Si‑O > µ_critical and µ^0_Si‑O‑Si < µ_critical."
    }
  ],
  "notes": "The scoring verifier compares the computed dipole moments to hidden reference values and checks the Lakhno criterion inequalities. No external datasets or model files are required; the agent implements the integrals from the publicly available Slater orbital descriptions and geometry parameters."
}
```

## How you are scored
A hidden verifier reads the submitted `/app/outputs/dipole_moments.json` and compares the computed dipole moments against hidden reference values within a tolerance. The verifier also checks that the inequality conditions (comparing each computed dipole moment to the critical value 0.318 D) hold as expected. The final reward is 1.0 only if both numeric comparisons and the inequality checks pass; otherwise it is 0.0. Simply reporting the paper's numbers without genuine computation will not pass the verifier's checks.
