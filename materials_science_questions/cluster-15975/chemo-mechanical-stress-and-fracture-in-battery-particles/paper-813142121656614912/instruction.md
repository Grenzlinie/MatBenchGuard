# Compute stress contributions to lithiation free energy for planar and perturbed reaction fronts

## Problem background
During lithiation of crystalline silicon, large volume expansion generates stress that can affect the shape of the reaction front. A thermodynamic–kinetic model predicts whether the front remains planar or develops perturbations. This analysis computes the hydrostatic-stress contribution to the free-energy change for two scenarios: (a) a planar reaction front and (b) a small spherical perturbation (approximated as a misfitting inclusion).

## Approach
The free-energy change for lithiation (excluding the ΔG_r and applied voltage terms) contains a stress term (1/x)(σ_h^Si Ω^Si − σ_h^{Li_xSi} Ω^{Li_xSi}) that captures the effect of hydrostatic stress on the driving force. For a planar reaction front, the lithiated phase is under equal biaxial compression at the yield stress, giving σ_h^{Li_xSi} = −2σ_Y/3 and σ_h^Si = 0. For a small spherical perturbation, the stress state near the perturbation is approximated by the elastic solution for a misfitting inclusion. The pressure inside the inclusion is determined by the elastic constants and the misfit strain; at the interface the hydrostatic stresses are σ_h^{Li_xSi} = −p and σ_h^Si = 0. Evaluate both stress contributions using the material parameters provided (σ_Y = 500 MPa, x = 3.75, Ω^{Li_xSi} = 7.6×10⁻²⁹ m³, E^Si = 160 GPa, E^{Li_xSi} = 12 GPa, ν^Si = 0.22, ν^{Li_xSi} = 0.26, ε_mf = 0.55) and report the results in electronvolts.

## Reproduction target
Compute the stress contribution term (1/x)(σ_h^Si Ω^Si − σ_h^{Li_xSi} Ω^{Li_xSi}) for two scenarios: (a) planar reaction front growth and (b) a spherical perturbation, using the elastic misfitting sphere approximation. Report both contributions in electronvolts (eV).

## Assets
No external datasets, pretrained models, or proprietary tools are required. You may use standard scientific computing libraries (e.g., NumPy) to perform the calculations.

## Workflow steps

### Step 1: Compute lithiation stress contributions
- Role: scored (load-bearing)
- Action: Implement the lithiation free-energy change expression (omitting ΔG_r and eΦ terms) and the elastic misfitting sphere stress solution. Using the provided material parameters (σ_Y=500 MPa, x=3.75, Ω^{Li_xSi}=7.6e-29 m³, E^Si=160 GPa, E^{Li_xSi}=12 GPa, ν^Si=0.22, ν^{Li_xSi}=0.26, ε_mf=0.55), compute the stress contribution term (1/x)*(σ_h^Si*Ω^Si − σ_h^{Li_xSi}*Ω^{Li_xSi}) for (a) planar reaction front growth (σ_h^{Li_xSi} = −2σ_Y/3, σ_h^Si=0) and (b) a spherical perturbation using the elastic misfitting sphere solution. Report both results in eV.
- Output file: `/app/outputs/stress_contributions.json`
- Format: json
- Contract: {"planar_contribution_eV": float, "perturbation_elastic_contribution_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_contributions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_contributions.json
- path: `/app/outputs/stress_contributions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The stress contributions to the free energy for planar reaction front growth and for a spherical perturbation (elastic estimate), both in electronvolts. These quantities verify the thermodynamic stabilization of the planar front.
- schema:
  - `type`: object
  - `required`: `planar_contribution_eV`, `perturbation_elastic_contribution_eV`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `planar_contribution_eV`: eV
    - `perturbation_elastic_contribution_eV`: eV

Notes: The paper also reports an elastic-plastic finite-element simulation result (0.92 eV) using ABAQUS, which is excluded from this scope due to proprietary software and complexity. The task covers the core analytic elastic estimate only.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "planar_contribution_eV",
          "perturbation_elastic_contribution_eV"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "planar_contribution_eV": "eV",
          "perturbation_elastic_contribution_eV": "eV"
        }
      },
      "description": "The stress contributions to the free energy for planar reaction front growth and for a spherical perturbation (elastic estimate), both in electronvolts. These quantities verify the thermodynamic stabilization of the planar front."
    }
  ],
  "notes": "The paper also reports an elastic-plastic finite-element simulation result (0.92 eV) using ABAQUS, which is excluded from this scope due to proprietary software and complexity. The task covers the core analytic elastic estimate only."
}
```

## How you are scored
A hidden verifier reads your scored artifact (stress_contributions.json). It compares your reported planar_contribution_eV and perturbation_elastic_contribution_eV to hidden reference values (derived from the paper’s model) within predefined tolerances, and it verifies that the perturbation contribution is larger than the planar contribution. The final reward is a weighted combination of these checks. Simply reporting the paper’s numbers is not sufficient; you must implement the computation to produce these values.
