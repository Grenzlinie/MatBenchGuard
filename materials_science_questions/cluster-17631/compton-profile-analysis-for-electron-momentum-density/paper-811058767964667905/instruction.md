# Pauli-exclusion corrected Compton scattering intensity in Al and Si

## Problem background
The Compton scattered X-ray intensity from a crystal often deviates from the intensity calculated for an isolated free atom, especially at low scattering angles. In aluminium and silicon, the outer valence electrons form a band; according to the Pauli exclusion principle, electrons in the band cannot make transitions into already occupied states. This reduces the effective number of scatterers and causes a suppression of the Compton intensity compared to the free‑atom expectation. The magnitude of this reduction depends on the modulus s of the scattering vector and on the band‑electron parameters. This work computes the band‑occupation‑corrected Compton scattering intensity for Al and Si by applying theoretical correction factors to the free‑atom analytical intensity. The resulting intensities can be compared with experimental measurements to assess the validity of the correction model.

## Approach
The free‑atom Compton scattering intensity for each element is obtained from the analytical representation of Smith, Thakkar & Chapman (1975) – see the Assets section; the agent retrieves the appropriate expression using the provided DOI.

For aluminium, the electron gas is treated as a free‑electron metal. The correction factor N_eff/N for 0 ≤ s ≤ 2k_F is

N_eff/N = (3/4) (s/k_F) − (1/16) (s/k_F)^3,

and N_eff/N = 1 for s > 2k_F. The Fermi wave‑vector is k_F = 2.8 nm⁻¹.

For silicon, the intrinsic semiconductor is modelled by filled valence and empty conduction bands in the free‑electron approximation, with a band gap E_G. The valence‑band radius k_V = 2.9 nm⁻¹ and E_G = 1.17 eV. The boundary of the empty conduction band is defined by k_C² = k_V² + 2mE_G/ħ²; the agent uses standard physical constants (Planck constant, electron mass, electron‑volt conversion). The correction factor N_eff/N is piecewise:
- for 0 ≤ s ≤ k_C − k_V: N_eff/N = 0,
- for s ≥ k_C + k_V: N_eff/N = 1,
- for k_C − k_V < s < k_C + k_V:

N_eff/N = 1 − γ(s),

where

γ(s) = (k_C³/(2 k_V³)) (1 − (3/2) cos φ + (1/2) cos³ φ) + (1/2) (1 − (3/2) cos ψ + (1/2) cos³ ψ),

cos φ = (k_C² − k_V² + s²)/(2 k_C s),
cos ψ = (k_V² − k_C² + s²)/(2 k_V s).

The corrected Compton intensity is then the free‑atom analytical intensity multiplied by the appropriate N_eff/N factor.

## Reproduction target
For aluminium and silicon, compute the corrected Compton scattering intensity at the following scattering‑vector moduli s (nm⁻¹): 0.1, 0.5, 1.0, 2.0, 3.0, 4.0.

Use the free‑atom Compton intensity as given by Smith et al. (1975) and the correction formulas described above. The required material parameters are:
- Al: k_F = 2.8 nm⁻¹,
- Si: k_V = 2.9 nm⁻¹, E_G = 1.17 eV (and k_C determined from k_C² = k_V² + 2mE_G/ħ² using standard physical constants).

For each (material, s) combination, record the free‑atom intensity, the correction factor, and the corrected intensity (free‑atom × correction factor) in electron units per atom. Output the results as the JSON file specified in the workflow steps.

## Assets

- Analytical representation of free-atom Compton scattering intensities (Smith et al., 1975): 10.1107/S0567739475001264
- CODATA physical constants: https://physics.nist.gov/cuu/Constants/

## Workflow steps

### Step 1: Compute Pauli-exclusion corrected Compton intensities for Al and Si
- Role: scored (load-bearing)
- Action: Implement the analytical free-atom Compton intensity from Smith et al. (1975) for Al and Si. Compute the correction factor N_eff/N using the metal formula for Al with k_F = 2.8 nm⁻¹, and the intrinsic semiconductor formula for Si with k_V = 2.9 nm⁻¹, E_G = 1.17 eV, and k_C from k_C² = k_V² + 2mE_G/ħ². Multiply the free-atom intensity by the correction factor to obtain the corrected Compton intensity. Compute for s = [0.1, 0.5, 1.0, 2.0, 3.0, 4.0] nm⁻¹ and write the results to corrected_compton_intensities.json.
- Output file: `/app/outputs/corrected_compton_intensities.json`
- Format: json
- Contract: A JSON array of 12 objects. Each object has keys: material (string, 'Al' or 'Si'), s (float, nm⁻¹), free_atom_intensity (float, eua), correction_factor (float, dimensionless), corrected_intensity (float, eua). The array covers s = [0.1, 0.5, 1.0, 2.0, 3.0, 4.0] for Al first, then the same s values for Si.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/corrected_compton_intensities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### corrected_compton_intensities.json
- path: `/app/outputs/corrected_compton_intensities.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Band-occupation-corrected Compton scattering intensity for Al and Si computed from the free-atom intensity and the Pauli-exclusion correction factor.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `s`, `free_atom_intensity`, `correction_factor`, `corrected_intensity`
    - `properties`:
      - `material`:
        - `type`: string
        - `description`: Either 'Al' or 'Si'
      - `s`:
        - `type`: number
        - `unit`: nm⁻¹
      - `free_atom_intensity`:
        - `type`: number
        - `unit`: eua
      - `correction_factor`:
        - `type`: number
        - `unit`: dimensionless
      - `corrected_intensity`:
        - `type`: number
        - `unit`: eua
  - `length`: 12
  - `order`: Al entries in increasing s, then Si entries in increasing s

Notes: The checker independently implements the same free-atom formula and correction formulas, recomputes corrected_intensity for each entry, and compares with the agent's value within a hidden tolerance. No self-reported metric is trusted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "corrected_compton_intensities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "s",
            "free_atom_intensity",
            "correction_factor",
            "corrected_intensity"
          ],
          "properties": {
            "material": {
              "type": "string",
              "description": "Either 'Al' or 'Si'"
            },
            "s": {
              "type": "number",
              "unit": "nm⁻¹"
            },
            "free_atom_intensity": {
              "type": "number",
              "unit": "eua"
            },
            "correction_factor": {
              "type": "number",
              "unit": "dimensionless"
            },
            "corrected_intensity": {
              "type": "number",
              "unit": "eua"
            }
          }
        },
        "length": 12,
        "order": "Al entries in increasing s, then Si entries in increasing s"
      },
      "description": "Band-occupation-corrected Compton scattering intensity for Al and Si computed from the free-atom intensity and the Pauli-exclusion correction factor."
    }
  ],
  "notes": "The checker independently implements the same free-atom formula and correction formulas, recomputes corrected_intensity for each entry, and compares with the agent's value within a hidden tolerance. No self-reported metric is trusted."
}
```

## How you are scored
A hidden verifier independently computes the corrected Compton intensities using the same analytical free‑atom expression and the same correction formulas with the same parameters. For every data point in your submission, the verifier recomputes the corrected_intensity and compares it with your value. The absolute difference is measured; if the difference lies within a hidden tolerance, the point is considered correct. Your final score is the fraction of points that meet this tolerance criterion, mapped to a reward between 0 and 1. You do not need to guess the tolerance; simply compute the intensity according to the method described.
