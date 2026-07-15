# Compute dielectric properties of NaCl0.5Br0.5 using extended three-body force shell model

## Problem background
Mixed alkali halide crystals exhibit interesting dielectric and vibrational properties due to the mixing of anions on the halide sublattice. For the equimolar crystal $\mathrm{NaCl_{0.5}Br_{0.5}}$, the static and high-frequency dielectric constants, their volume dependence, and the optical-mode Gruneisen parameters are important quantities that reflect the lattice dynamics and ion polarizabilities. A classical ionic model—the extended three-body force shell model—has been applied to this system to compute these dielectric properties and to understand the role of three-body charge-transfer interactions.

## Approach
The extended three-body force shell model describes the crystal as polarizable ions (cores and shells) coupled by short-range repulsive interactions, long-range Coulomb forces, and three-body terms that account for charge-transfer effects during lattice deformations. Given the input data (elastic constants, long-wavelength phonon frequencies, lattice parameter, and the polarizabilities $\alpha_1$, $\alpha_2$) and a set of model parameters (repulsive parameters $A$, $B$, three-body function $f(r)$ and its derivative, distortion parameters $d_1$, $d_2$, and shell charges $Y_1$, $Y_2$) that have been fitted for the mixed crystal, the model can be solved to obtain the static and high-frequency dielectric constants, their volume-scaled logarithmic derivatives, and the TO and LO Gruneisen parameters. The implementation must compute these six quantities from the supplied data without requiring any external experimental reference values.

## Reproduction target
Implement the extended three-body force shell model using the numeric input data and model parameters provided below to calculate the static dielectric constant $\varepsilon_0$, the high-frequency dielectric constant $\varepsilon_\infty$, the volume-scaled derivatives $V\partial\varepsilon_0/\partial V$ and $V\partial\varepsilon_\infty/\partial V$, and the TO and LO Gruneisen parameters $\gamma_{\mathrm{TO}}$ and $\gamma_{\mathrm{LO}}$ for $\mathrm{NaCl_{0.5}Br_{0.5}}$. All six results must be written to the output file as specified in the contract.

## Assets

- Extended three-body force shell model
- NumPy: numpy

## Workflow steps

### Step 1: Compute dielectric parameters
- Role: scored (load-bearing)
- Action: Implement the extended three-body force shell model using the given input data (C11, C12, C44, ωLO, ωTO, α1, α2, r from Table 1) and model parameters (A, B, f(r), r∂f/∂r, d1, d2, Y1, Y2 from Table 2) to calculate the static dielectric constant ε0, high-frequency dielectric constant ε∞, volume-scaled derivatives V∂ε0/∂V and V∂ε∞/∂V, and TO/LO Gruneisen parameters γ_TO and γ_LO. Write the six numerical results to dielectric_parameters.json.
- Output file: `/app/outputs/dielectric_parameters.json`
- Format: json
- Contract: {
  "ε0": number,
  "ε∞": number,
  "Vdε0_dV": number,
  "Vdε∞_dV": number,
  "γ_TO": number,
  "γ_LO": number
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dielectric_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dielectric_parameters.json
- path: `/app/outputs/dielectric_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed dielectric constants, volume derivatives, and Gruneisen parameters for NaCl0.5Br0.5.
- schema:
  - `type`: object
  - `required`: `ε0`, `ε∞`, `Vdε0_dV`, `Vdε∞_dV`, `γ_TO`, `γ_LO`
  - `properties`:
    - `ε0`:
      - `type`: number
    - `ε∞`:
      - `type`: number
    - `Vdε0_dV`:
      - `type`: number
    - `Vdε∞_dV`:
      - `type`: number
    - `γ_TO`:
      - `type`: number
    - `γ_LO`:
      - `type`: number

Notes: The agent must implement the extended three-body force shell model from the cited references. All necessary numerical input data and model parameters are provided in the task instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dielectric_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "ε0",
          "ε∞",
          "Vdε0_dV",
          "Vdε∞_dV",
          "γ_TO",
          "γ_LO"
        ],
        "properties": {
          "ε0": {
            "type": "number"
          },
          "ε∞": {
            "type": "number"
          },
          "Vdε0_dV": {
            "type": "number"
          },
          "Vdε∞_dV": {
            "type": "number"
          },
          "γ_TO": {
            "type": "number"
          },
          "γ_LO": {
            "type": "number"
          }
        }
      },
      "description": "Computed dielectric constants, volume derivatives, and Gruneisen parameters for NaCl0.5Br0.5."
    }
  ],
  "notes": "The agent must implement the extended three-body force shell model from the cited references. All necessary numerical input data and model parameters are provided in the task instruction."
}
```

## How you are scored
A hidden verifier will read your output file and compare each of the six reported quantities to a set of reference values derived from the paper. For each quantity, the verifier checks whether your computed value is sufficiently close to the reference; a successful match earns a fraction of the total score. The final reward is the sum of the fractions for all six quantities. Reporting the correct numbers without running the actual model computation is not sufficient—the verifier uses numerical tolerances, and a genuine implementation of the shell model is required to achieve full credit.
