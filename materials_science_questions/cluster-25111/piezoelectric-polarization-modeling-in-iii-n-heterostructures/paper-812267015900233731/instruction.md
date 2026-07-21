# Strain-induced Polarization Screening Simulation in III-Nitride Heterostructures

## Problem background
Wurtzite III-nitride heterostructures used in blue/violet light-emitting diodes and laser diodes possess large spontaneous and piezoelectric polarization-induced electric fields (PIEFs) along the growth direction. In InGaN quantum wells (QWs) these fields separate injected electrons and holes to opposite sides of the well, which reduces the radiative recombination efficiency. Screening of PIEFs can be achieved by ionized donors from intentional Si doping of the quantum barriers or by the accumulation of injected charge at high current densities. The interplay between fixed donor charge and mobile injected charge determines how the pressure derivative of the electroluminescence peak energy (dE_E/dp) evolves with current. Understanding this dependence is important for predicting the conditions under which full screening is reached.

## Approach
Use a simple constant-field model for InGaN QWs: assume a spatially constant electric field in the wells. Compute the overlap integral of the electron and hole envelope wavefunctions as a function of the sheet charge density σ. Convert σ to an equivalent current density J via J = q σ / τ, taking a carrier lifetime τ = 1 ns and 100 % injection efficiency. For each J, determine the corresponding dE_E/dp by interpolating between the fully unscreened value (determined by the PIEF pressure derivative from Vaschenko et al., Appl. Phys. Lett. 78, 640 (2001)) and the fully screened value of 34 meV/GPa, using the wavefunction overlap as the screening weight. Perform the calculation for four background ionized donor concentrations N_D: 0, 1×10^16, 1×10^17, and 1×10^18 cm⁻³, on a dense logarithmic grid of current densities spanning approximately 1×10⁻⁶ to 1×10³ A/cm².

## Reproduction target
Produce a single CSV file `simulation_dE_E_dp.csv` inside `/app/outputs`. The file must contain columns: `N_D` (cm⁻³, numeric), `current_density` (A/cm², numeric), and `dE_E_dp` (meV/GPa, numeric). At least 20 current-density points per N_D value must be present, covering the interval from about 1×10⁻⁶ to 1×10³ A/cm² in a monotonically increasing sequence. All four N_D values (0, 1×10¹⁶, 1×10¹⁷, 1×10¹⁸) must appear. The output should reflect the expected steplike dependence of dE_E/dp on current, with a systematic shift of the step with N_D.

## Assets

- Pressure derivative of PIEF in InGaN/GaN QWs (Vaschenko et al., Appl. Phys. Lett. 78, 640 (2001)): https://doi.org/10.1063/1.1344225

## Workflow steps

### Step 1: Simulate dE_E/dp vs. current density for different background doping concentrations
- Role: scored (load-bearing)
- Action: Implement the constant-field screening model: assume a spatially constant electric field in InGaN quantum wells, compute the electron-hole wavefunction overlap as a function of sheet charge density σ, convert σ to current density J via J = qσ/τ with carrier lifetime τ = 1 ns and 100% injection efficiency, then calculate dE_E/dp for each J using the fully screened value 34 meV/GPa and the pressure derivative of the polarization-induced electric field (PIEF) from Vaschenko et al. (2001). Perform the calculation for background ionized donor concentrations N_D = 0, 1e16, 1e17, 1e18 cm⁻³ on a dense logarithmic grid of current densities from approximately 1e-6 to 1e3 A/cm². Output a single CSV with the results.
- Output file: `/app/outputs/simulation_dE_E_dp.csv`
- Format: csv
- Contract: Columns: N_D (cm⁻³, numeric), current_density (A/cm², numeric), dE_E_dp (meV/GPa, numeric). At least 20 current points per N_D, monotonically increasing. All N_D values 0, 1e16, 1e17, 1e18 must be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_dE_E_dp.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_dE_E_dp.csv
- path: `/app/outputs/simulation_dE_E_dp.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulation results from the constant-field screening model; used to verify structural trends of dE_E/dp with current density and background doping.
- schema:
  - `type`: table
  - `required_columns`: `N_D`, `current_density`, `dE_E_dp`
  - `units`:
    - `N_D`: cm⁻³
    - `current_density`: A/cm²
    - `dE_E_dp`: meV/GPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_dE_E_dp.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N_D",
          "current_density",
          "dE_E_dp"
        ],
        "units": {
          "N_D": "cm⁻³",
          "current_density": "A/cm²",
          "dE_E_dp": "meV/GPa"
        }
      },
      "description": "Simulation results from the constant-field screening model; used to verify structural trends of dE_E/dp with current density and background doping."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier loads the submitted CSV and checks several structural properties of the dE_E/dp curves: (1) at the lowest current, dE_E/dp increases monotonically with N_D; (2) at the highest current, all curves approach a common saturation value within a hidden tolerance; (3) the current at which dE_E/dp reaches a fixed high fraction of saturation decreases strictly as N_D increases; (4) each dE_E/dp vs. log(current) curve exhibits a distinct steplike shape (the first derivative shows a well-defined peak). Full credit is awarded if all conditions are met; partial credit is given for each condition that holds.
