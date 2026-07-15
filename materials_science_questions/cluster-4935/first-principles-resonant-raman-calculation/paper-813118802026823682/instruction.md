# Charge Transfer Contribution to Vibrational Polarizability Derivative Estimate

## Problem background
Raman scattering intensities of some molecular complexes involving charge transfer are substantially larger than those of the isolated molecules, even when there is no resonant electronic absorption. This paper proposes that the enhancement arises from the different displaceabilities of the electronic charge transferred between the donor and the acceptor. During a vibrational mode that changes the donor–acceptor distance, the extent of charge transfer is modulated, producing an additional oscillation of the polarizability. The resulting charge‑transfer contribution to the Raman polarizability derivative may be comparable to the intramolecular contribution. This task reproduces the order‑of‑magnitude estimate of that charge‑transfer contribution for an acceptor stretching vibration in a CCl₄–pyridine complex.

## Approach
The total polarizability derivative with respect to an acceptor vibrational coordinate can be split into an intramolecular part and a charge‑transfer part. The charge‑transfer part depends on how much the donor–acceptor distance changes with the vibration, how strongly the transferred charge depends on that distance, and the difference in polarizability displaceabilities of the charge on the acceptor and on the donor. The displaceabilities are approximated from the polarizabilities of the neutral and charged species. For a diatomic acceptor stretch, the distance change with the vibrational coordinate can be obtained from the reduced mass. All required parameters are public constants taken from the literature. The workflow computes the magnitude of the charge‑transfer contribution and writes it, together with the input constants, to a JSON file.

## Reproduction target
Implement the formula for the charge‑transfer contribution to the acceptor‑stretch polarizability derivative: CT = (∂ρ_A/∂x) · (dx/dq_A) · (∂α_A/∂ρ_A − ∂α_D/∂ρ_D). Use the following numerical constants (all in CGS units): dx/dq_A = −2.5×10⁻¹² g^{1/2}, ∂ρ_A/∂x = 4×10⁷ e/cm, ∂α_A/∂ρ_A = 33×10⁻²⁵ cm³/e, ∂α_D/∂ρ_D = 5×10⁻²⁵ cm³/e. Compute the magnitude (absolute value) of the result in cm² g^{1/2}. Write a JSON file containing the four input constants and the computed CT_contribution. This file is the scored artifact.

## Assets

- Python 3

## Workflow steps

### Step 1: Compute CT contribution
- Role: scored (load-bearing)
- Action: Implement the formula for the charge-transfer contribution to the vibrational polarizability derivative: (dα_tot/dq_A)_CT = (∂ρ_A/∂x) · (dx/dq_A) · (∂α_A/∂ρ_A - ∂α_D/∂ρ_D). Use the following constants: dx/dq_A = -2.5e-12 g^{1/2}, ∂ρ_A/∂x = 4e7 e/cm, ∂α_A/∂ρ_A = 33e-25 cm^3/e, ∂α_D/∂ρ_D = 5e-25 cm^3/e. Compute the magnitude (absolute value) of the result. Write the four input constants and the computed CT_contribution to a JSON file.
- Output file: `/app/outputs/ct_contribution.json`
- Format: json
- Contract: JSON object with keys: 'dx_dq' (float, unit g^{1/2}), 'drho_dx' (float, unit e/cm), 'dalpha_A_drhoA' (float, unit cm^3/e), 'dalpha_D_drhoD' (float, unit cm^3/e), 'CT_contribution' (float, unit cm^2 g^{1/2}).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ct_contribution.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ct_contribution.json
- path: `/app/outputs/ct_contribution.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Charge-transfer contribution to the acceptor-stretch polarizability derivative, computed using the formula and constants from the paper.
- schema:
  - `type`: object
  - `required`:
    - `dx_dq`: float
    - `drho_dx`: float
    - `dalpha_A_drhoA`: float
    - `dalpha_D_drhoD`: float
    - `CT_contribution`: float
  - `units`:
    - `dx_dq`: g^{1/2}
    - `drho_dx`: e/cm
    - `dalpha_A_drhoA`: cm^3/e
    - `dalpha_D_drhoD`: cm^3/e
    - `CT_contribution`: cm^2 g^{1/2}

Notes: The checker recomputes the CT contribution from the provided constants and compares the computed value against the expected result using a hidden relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ct_contribution.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "dx_dq": "float",
          "drho_dx": "float",
          "dalpha_A_drhoA": "float",
          "dalpha_D_drhoD": "float",
          "CT_contribution": "float"
        },
        "units": {
          "dx_dq": "g^{1/2}",
          "drho_dx": "e/cm",
          "dalpha_A_drhoA": "cm^3/e",
          "dalpha_D_drhoD": "cm^3/e",
          "CT_contribution": "cm^2 g^{1/2}"
        }
      },
      "description": "Charge-transfer contribution to the acceptor-stretch polarizability derivative, computed using the formula and constants from the paper."
    }
  ],
  "notes": "The checker recomputes the CT contribution from the provided constants and compares the computed value against the expected result using a hidden relative tolerance."
}
```

## How you are scored
A hidden verifier independently checks your `ct_contribution.json`. It first recomputes the charge‑transfer contribution from the constants you reported and verifies self‑consistency. It then compares your computed CT_contribution value against a hidden reference using a tolerance that accounts for the numerical precision expected from this straightforward arithmetic. You must produce the correct numeric result to receive credit. The overall reward for the task is a weighted combination of the scores from each workflow stage; this scored stage carries the full weight.
