# Compute bulk and surface spin-wave energies and intensity ratio for semi-infinite Heisenberg antiferromagnet

## Problem background
Light scattering from magnetic surfaces can probe surface spin-wave excitations. For a Heisenberg antiferromagnet with a (001) surface, the broken sublattice symmetry gives rise to a localized surface spin-wave mode whose energy differs from the bulk spin-wave continuum. This task reproduces the theoretical calculation of the bulk spin-wave energy at zero wavevector, the surface spin-wave energy at zero wavevector, and the ratio of integrated Stokes peak intensities for surface-to-bulk scattering, using given material parameters. These quantities are essential for understanding surface magnetic excitations and their optical signatures.

## Approach
The method is based on analysing the spin-spin Green functions of a semi-infinite Heisenberg antiferromagnet with a body-centred tetragonal structure and a (001) surface, using nearest-neighbour exchange interactions. From the poles of the Green functions, analytic expressions are obtained for the spin-wave energies. The bulk spin-wave energy at zero wavevector is given by E_B(0) = sqrt(gμ_B H_A (gμ_B H_A + 16 S J)). The localized surface spin-wave energy at zero wavevector is E_S^+(0) = sqrt(gμ_B H_A (gμ_B H_A + 8 S J)). The one-magnon light scattering cross-section is computed from these Green functions, and in the absorptive case the ratio of integrated Stokes intensities for surface-to-bulk scattering simplifies to I_S/I_B = 4π c|k''| sqrt(S J/(gμ_B H_A)) for weak anisotropy (gμ_B H_A ≪ 8 S J). Here S is the spin quantum number, J is the exchange constant (taken as energy unit, J=1), gμ_B H_A is the product of the g-factor, Bohr magneton, and anisotropy field, and c|k''| = c|k_{2i}^{z''} + k_{2s}^{z''}| is the optical absorption parameter describing the imaginary part of the wavevectors for incident and scattered light. The task is to compute these three quantities for the supplied parameter values.

## Reproduction target
Given specific values for the parameters S, gμ_B H_A, and c|k''| (with J=1), compute the bulk_energy (E_B(0)), surface_energy (E_S^+(0)), and intensity_ratio (I_S/I_B). Write these three numbers into /app/outputs/results.json in JSON format with keys 'bulk_energy', 'surface_energy', 'intensity_ratio'.

## Assets
No external datasets, pre-trained models, or specialized software are required. The computation can be performed with any programming language, e.g., Python 3 using the standard math library. No additional package installations are needed beyond what the base environment provides.

## Workflow steps

### Step 1: Compute bulk and surface spin-wave energies and intensity ratio
- Role: scored
- Action: Implement the analytic formulas for the bulk spin-wave energy at zero wavevector (E_B(0)), the surface spin-wave energy at zero wavevector (E_S^+(0)), and the ratio of integrated Stokes peak intensities for surface-to-bulk scattering in the absorptive case (I_S/I_B). Compute these three quantities from the given material parameters: spin S, exchange J (units are chosen such that J=1), anisotropy field parameter gμ_B H_A, and optical absorption parameter c|k_{2i}^{z''}+k_{2s}^{z''}|. All energies are in units of J; the ratio is dimensionless.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"bulk_energy": <float>, "surface_energy": <float>, "intensity_ratio": <float>}
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
- description: The JSON object must contain the three computed quantities: bulk spin-wave energy at zero wavevector (E_B(0)), surface spin-wave energy at zero wavevector (E_S^+(0)), and the ratio of integrated Stokes peak intensities for surface-to-bulk scattering in the absorptive case (I_S/I_B).
- schema:
  - `type`: object
  - `required`:
    - `bulk_energy`: float (units of J)
    - `surface_energy`: float (units of J)
    - `intensity_ratio`: float (dimensionless)

Notes: The material parameters (S, gμ_B H_A, and the optical absorption parameter) are provided in the instruction. The agent must compute the quantities using the paper's analytic formulas.

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
          "bulk_energy": "float (units of J)",
          "surface_energy": "float (units of J)",
          "intensity_ratio": "float (dimensionless)"
        }
      },
      "description": "The JSON object must contain the three computed quantities: bulk spin-wave energy at zero wavevector (E_B(0)), surface spin-wave energy at zero wavevector (E_S^+(0)), and the ratio of integrated Stokes peak intensities for surface-to-bulk scattering in the absorptive case (I_S/I_B)."
    }
  ],
  "notes": "The material parameters (S, gμ_B H_A, and the optical absorption parameter) are provided in the instruction. The agent must compute the quantities using the paper's analytic formulas."
}
```

## How you are scored
Your results.json file will be evaluated by a hidden verifier. It will compare your submitted bulk_energy, surface_energy, and intensity_ratio against the correct reference values (the analytic results from the theory) using appropriate error tolerances. The verifier will compute a reward score between 0 and 1 based on the accuracy of the three numbers; higher accuracy yields a higher reward. You must produce the output in exactly the specified format. No other outputs are scored.
