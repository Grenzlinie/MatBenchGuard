# Effective Mass from Transport Properties using Single Parabolic Band Model

## Problem background
The thermoelectric figure of merit ZT determines how efficiently a material converts heat to electricity. Understanding the electronic transport in skutterudite compounds such as CeFe4As12, CeFe4P12, and CeFe4Sb12 requires estimating the density-of-states effective mass of the charge carriers. A standard way to extract the effective mass from measured transport properties is the single parabolic band (SPB) model with acoustic phonon scattering. This task asks you to compute the effective mass for each compound at room temperature from given Seebeck coefficient and Hall carrier concentration data.

## Approach
Apply the single parabolic band model under the assumption of acoustic phonon scattering (scattering parameter r = -1/2). For a p-type material, the reduced chemical potential η is obtained by solving the Seebeck coefficient equation:
α = (k_B/e) * ( (2 F_1(η) / F_0(η)) - η )
where k_B is Boltzmann's constant, e the elementary charge, and F_j the Fermi-Dirac integral of order j. With η determined, the carrier concentration p in a single parabolic band is:
 p = 4π ( (2 m* k_B T) / h^2 )^(3/2) * F_{1/2}(η)
where h is Planck's constant. Solve for the density-of-states effective mass m* and express it in units of the free electron mass m0. Perform this calculation for CeFe4As12, CeFe4P12, and CeFe4Sb12 using the provided room-temperature input data.

## Reproduction target
Using the given Seebeck coefficients and Hall carrier concentrations at T=300 K, compute the hole effective mass m*/m0 for each compound:
- CeFe4As12: α = 37 μV/K, p = 6.3×10^20 cm^-3
- CeFe4P12: α = 58 μV/K, p = 1.42×10^19 cm^-3
- CeFe4Sb12: α = 59 μV/K, p = 5.5×10^21 cm^-3
Report the three masses in a JSON file named effective_masses.json with keys "CeFe4As12", "CeFe4P12", and "CeFe4Sb12" and numeric values (floating-point).

## Assets

- scipy: scipy

## Workflow steps

### Step 1: Effective Mass Calculation
- Role: scored (load-bearing)
- Action: Implement the single-parabolic-band model under the assumption of acoustic phonon scattering (scattering parameter r = -1/2). Using the provided room-temperature Seebeck coefficients (37 μV/K for CeFe4As12, 58 μV/K for CeFe4P12, 59 μV/K for CeFe4Sb12) and Hall carrier concentrations (6.3×10^20 cm^-3, 1.42×10^19 cm^-3, 5.5×10^21 cm^-3) at T=300 K, first compute the reduced chemical potential η from the Seebeck equation α = (kB/e) * ( (2*F1(η)/F0(η)) - η ), then compute the density-of-states effective mass using the carrier concentration formula p = 4π (2 m* kB T / h^2)^(3/2) * F_{1/2}(η). Express the effective mass in units of free electron mass m0 for each compound. Report the three effective masses in a JSON dictionary.
- Output file: `/app/outputs/effective_masses.json`
- Format: json
- Contract: {"CeFe4As12": <float>, "CeFe4P12": <float>, "CeFe4Sb12": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_masses.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_masses.json
- path: `/app/outputs/effective_masses.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed density-of-states effective masses (in units of m0) for CeFe4As12, CeFe4P12, and CeFe4Sb12 based on the single-parabolic-band model with acoustic phonon scattering.
- schema:
  - `type`: object
  - `required`:
    - `CeFe4As12`: number
    - `CeFe4P12`: number
    - `CeFe4Sb12`: number

Notes: The checker will recompute the effective masses from the same input Seebeck coefficients and carrier concentrations using the SPB model and compare to the agent's reported values. The scoring uses tolerances appropriate for numerical integration and root-finding differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_masses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "CeFe4As12": "number",
          "CeFe4P12": "number",
          "CeFe4Sb12": "number"
        }
      },
      "description": "Computed density-of-states effective masses (in units of m0) for CeFe4As12, CeFe4P12, and CeFe4Sb12 based on the single-parabolic-band model with acoustic phonon scattering."
    }
  ],
  "notes": "The checker will recompute the effective masses from the same input Seebeck coefficients and carrier concentrations using the SPB model and compare to the agent's reported values. The scoring uses tolerances appropriate for numerical integration and root-finding differences."
}
```

## How you are scored
A hidden verifier will take your effective_masses.json, recompute the effective masses independently using the same SPB model and input data, and compare your reported values to the reference results. Your score is based on how closely your computed effective masses agree with the reference; better agreement yields a higher score. This is not a simple pass/fail — small numerical deviations are expected and will be credited proportionally to their accuracy. No further information about the reference values is available to you; your job is to faithfully implement the model described in the Approach section.
