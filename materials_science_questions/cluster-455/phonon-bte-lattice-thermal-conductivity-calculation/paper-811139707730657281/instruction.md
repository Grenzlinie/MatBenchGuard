# Phonon BTE lattice thermal conductivity calculation

## Problem background
Germanane (GeH) is a hydrogen-terminated layered germanium structure, a 2D material with potential electronic and thermoelectric applications. Its basal-plane lattice thermal conductivity is critical for device performance and is strongly influenced by microstructure such as grain boundaries and point defects. In this task, you will compute the thermal conductivity of GeH from first principles for several physically distinct scattering scenarios, covering the intrinsic crystalline limit, nanograined samples with specified length scales, and the fully amorphous state.

## Approach
The computational pipeline comprises two stages. First, density functional theory (DFT) calculations are performed to obtain the harmonic and anharmonic interatomic force constants of GeH, from which the full phonon dispersion, group velocities, and three-phonon scattering rates are derived. Second, the phonon Boltzmann transport equation (BTE) is solved within the relaxation time approximation (RTA) to obtain the in-plane lattice thermal conductivity. Four distinct scattering configurations are evaluated: (1) pristine bulk GeH with only intrinsic anharmonic scattering; (2) nanocrystalline GeH with a frequency-independent grain-boundary mean free path of 16 nm plus point-defect scattering (Born approximation, factor F = 0.024, where F = c (Δm/m_host)^2 with c the defect concentration); (3) nanocrystalline GeH with a grain-boundary mean free path of 34 nm and the same point-defect factor F = 0.024; (4) the amorphous limit using the Cahill minimum thermal conductivity model, which takes the phonon lifetime as τ = π/ω. The thermal conductivity is evaluated at three fixed temperatures: 200 K, 300 K, and 400 K.

## Reproduction target
Compute the in-plane lattice thermal conductivity (κ_∥) of GeH for the four scenarios described in the Approach section at T = 200 K, 300 K, and 400 K. Output the results as a plain CSV file named `thermal_conductivity_results.csv` with columns: `temperature_K`, `pristine_bulk`, `nanocrystalline_lb16`, `nanocrystalline_lb34`, `amorphous_limit`. All thermal conductivity values must be reported in units of W/mK. The hidden verifier will compare your submitted values to reference data and check that the temperature dependence of each case follows physically expected trends.

## Assets

- Crystal structure of GeH: 10.1021/nn403308j
- DFT software (Quantum ESPRESSO or VASP): https://www.quantum-espresso.org
- ShengBTE phonon BTE solver: http://www.shengbte.org
- Pseudopotentials for Ge and H: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: First-principles phonon calculation
- Role: process
- Action: Perform DFT calculations to obtain harmonic and anharmonic force constants for GeH. Compute phonon dispersion, group velocities, and three-phonon scattering rates.
- Evidence: `/app/outputs/phonon_calc.log`

### Step 2: Thermal conductivity calculation
- Role: scored (load-bearing)
- Action: Using the phonon data from the previous step, solve the phonon Boltzmann transport equation within the relaxation time approximation. For pristine bulk GeH, include only anharmonic scattering. For nanocrystalline GeH, add grain-boundary scattering (frequency-independent mean free path l_b) and point-defect scattering (factor F=0.024) with l_b values of 16 nm and 34 nm. For the amorphous limit, apply the Cahill minimum thermal conductivity model (τ = π/ω). Compute the in-plane thermal conductivity at temperatures 200 K, 300 K, and 400 K for each case and write the results to a CSV file.
- Output file: `/app/outputs/thermal_conductivity_results.csv`
- Format: csv
- Contract: Columns: temperature_K (float, temperature in kelvin), pristine_bulk (float, thermal conductivity in W/mK), nanocrystalline_lb16 (float, thermal conductivity in W/mK), nanocrystalline_lb34 (float, thermal conductivity in W/mK), amorphous_limit (float, thermal conductivity in W/mK). Each row corresponds to a temperature point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_results.csv
- path: `/app/outputs/thermal_conductivity_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal conductivity of GeH computed via phonon BTE for different scattering scenarios. The hidden checker compares the values at 300 K to paper reference values with tolerance, and also verifies temperature trends (pristine decreasing, nanocrystalline increasing, amorphous flat).
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pristine_bulk`, `nanocrystalline_lb16`, `nanocrystalline_lb34`, `amorphous_limit`
  - `units`:
    - `temperature_K`: K
    - `pristine_bulk`: W/mK
    - `nanocrystalline_lb16`: W/mK
    - `nanocrystalline_lb34`: W/mK
    - `amorphous_limit`: W/mK

Notes: Units are W/mK. The agent must compute the results from first principles; the hidden checker checks consistency with known reference values within physically reasonable tolerances. Temperature trends are also evaluated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pristine_bulk",
          "nanocrystalline_lb16",
          "nanocrystalline_lb34",
          "amorphous_limit"
        ],
        "units": {
          "temperature_K": "K",
          "pristine_bulk": "W/mK",
          "nanocrystalline_lb16": "W/mK",
          "nanocrystalline_lb34": "W/mK",
          "amorphous_limit": "W/mK"
        }
      },
      "description": "Lattice thermal conductivity of GeH computed via phonon BTE for different scattering scenarios. The hidden checker compares the values at 300 K to paper reference values with tolerance, and also verifies temperature trends (pristine decreasing, nanocrystalline increasing, amorphous flat)."
    }
  ],
  "notes": "Units are W/mK. The agent must compute the results from first principles; the hidden checker checks consistency with known reference values within physically reasonable tolerances. Temperature trends are also evaluated."
}
```

## How you are scored
A hidden verifier reads your `thermal_conductivity_results.csv` and compares the thermal conductivity you report at each temperature for each case against hidden reference values, using tolerances appropriate for a correct independent re-implementation. The verifier also checks that the temperature trends in your data are physically consistent across the different scattering regimes (a crystalline solid governed by anharmonic scattering, grain-boundary-dominated transport, and the thermal-conductivity floor of an amorphous material). The final reward is a weighted combination of how closely your computed values agree with the references and whether your results exhibit the correct temperature trends.
