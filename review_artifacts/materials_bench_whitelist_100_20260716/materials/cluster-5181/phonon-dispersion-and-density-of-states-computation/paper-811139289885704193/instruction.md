# Phonon Dispersion and Thermodynamics of bcc Tungsten from Density Functional Theory

## Problem background
Tungsten (W) is a body-centered cubic (bcc) refractory metal with an exceptionally high melting point and excellent mechanical strength, making it critical for pressure standards, aerospace, and extreme-environment applications. Accurate knowledge of its elastic constants, phonon dispersion, and thermodynamic properties – including thermal expansion, adiabatic bulk modulus, specific heat, and entropy – under high pressure and temperature is essential for constructing thermodynamic models and understanding material behavior in such conditions. However, experimental data under extreme conditions are scarce. First-principles calculations based on density functional theory (DFT) and density functional perturbation theory (DFPT) provide a reliable route to predict these properties directly from the crystal structure without empirical input beyond the chosen exchange-correlation functional.

## Approach
We employ DFT within the generalized gradient approximation (PBE) with an ultrasoft pseudopotential for tungsten, using Quantum ESPRESSO. The workflow proceeds in four stages. First, static self-consistent field (SCF) calculations are carried out for bcc W over a range of unit-cell volumes; the resulting energy–volume data are fitted to a fourth-order finite-strain equation of state (EOS) to determine the static equilibrium volume, bulk modulus, and its pressure derivative. Second, the three independent zero-pressure elastic constants C11, C12, and C44 are obtained via the energy-strain method using volume-conserving lattice deformations. Third, DFPT is used to compute the phonon frequencies at selected high-symmetry q-points – Γ (0,0,0), H (0.5,0.5,0.5), and P (0.5,0.25,0.25) – at the zero-pressure equilibrium volume. Finally, within the quasiharmonic approximation (QHA), the Helmholtz free energy is built as a function of volume and temperature by combining the static energy with the phonon free energy (neglecting electronic contributions). Fitting the free-energy curves to an EOS at each temperature yields equilibrium volumes, from which we derive the volume thermal expansion coefficient α_V, the adiabatic bulk modulus B_S, the constant-volume specific heat C_V, and the entropy S, all evaluated along isobars at 0 GPa and 50 GPa for temperatures from 300 K to 3000 K.

## Reproduction target
Your task is to execute the above computations and produce three output files containing the results:

1. `elastic_constants.json`: the three independent elastic constants C11, C12, and C44 (in GPa) for bcc W at zero pressure.
2. `phonon_frequencies.csv`: the three acoustic‑phonon frequencies (in THz) at the q-points Γ (0,0,0), H (0.5,0.5,0.5), and P (0.5,0.25,0.25) at zero pressure.
3. `thermal_properties.csv`: the thermal expansion coefficient α_V (in 10⁻⁶ K⁻¹), adiabatic bulk modulus B_S (in GPa), constant‑volume specific heat C_V (in J mol⁻¹ K⁻¹), and entropy S (in J mol⁻¹ K⁻¹) for the temperatures 300 K, 500 K, 1000 K, 1500 K, 2000 K, 2500 K, and 3000 K, at both zero pressure and 50 GPa.

The goal is to obtain values that agree with established reference data for bcc tungsten within typical DFT tolerances and that display physically correct trends (e.g., specific heat approaching the Dulong–Petit limit, thermal expansion decreasing with pressure, entropy increasing with temperature).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- W ultrasoft pseudopotential (PBE): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Static energy-volume calculation and equation of state fitting
- Role: process
- Action: Perform static SCF calculations for bcc W at a series of volumes, then fit the energy-volume data to a fourth-order finite-strain EOS to obtain the equilibrium volume V0, bulk modulus B0, and its pressure derivative B'.
- Evidence: `/app/outputs/static_EOS_fit.json`

### Step 2: Elastic constants at zero pressure
- Role: scored (load-bearing)
- Action: Use the energy-strain method with volume-conserving deformations to compute the three independent elastic constants C11, C12, C44 of bcc W at zero pressure. Write the results to elastic_constants.json.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with keys "C11", "C12", "C44" (values are floats in GPa).
- Scoring: scored by hidden verifier

### Step 3: Phonon frequencies at high-symmetry points
- Role: scored (load-bearing)
- Action: Calculate phonon frequencies at the Γ (0,0,0), H (0.5,0.5,0.5), and P (0.5,0.25,0.25) q-points for bcc W at zero pressure using DFPT as implemented in Quantum ESPRESSO. Collect the three branch frequencies at each point and write phonon_frequencies.csv.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: CSV with columns: q_point (string, one of 'GAMMA','H','P'), freq1, freq2, freq3 (floats, the three branch frequencies in THz).
- Scoring: scored by hidden verifier

### Step 4: Quasiharmonic thermodynamic properties
- Role: scored (load-bearing)
- Action: Combine the static energies and phonon frequencies (at several volumes) to evaluate the Helmholtz free energy within the quasiharmonic approximation for temperatures from 0 to 3000 K. Fit the free-energy curves to an EOS to obtain equilibrium volumes at each temperature, then derive the thermal expansion coefficient α_V, adiabatic bulk modulus B_S, specific heat at constant volume C_V, and entropy S at zero pressure and at P=50 GPa for a set of temperatures (300, 500, 1000, 1500, 2000, 2500, 3000 K). Write the results to thermal_properties.csv.
- Output file: `/app/outputs/thermal_properties.csv`
- Format: csv
- Contract: CSV with columns: T_K (float, temperature in Kelvin), P_GPa (float, pressure in GPa), alpha_V_1e-6 (float, in 10^{-6} K^{-1}), B_S_GPa (float, in GPa), C_V_J_molK (float, in J/mol·K), S_J_molK (float, in J/mol·K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/thermal_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zero-pressure elastic constants C11, C12, C44 of bcc W in GPa.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float, GPa
    - `C12`: float, GPa
    - `C44`: float, GPa
  - `items`: object
  - `required_columns`:
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phonon frequencies at high-symmetry q-points Gamma, H, P at zero pressure. Three branch frequencies per point in THz.
- schema:
  - `type`: table
  - `required_columns`: `q_point`, `freq1`, `freq2`, `freq3`
  - `items`: object
  - `units`:
    - `freq1`: THz
    - `freq2`: THz
    - `freq3`: THz
  - `notes`: q_point is a string: one of 'GAMMA', 'H', 'P'.

### thermal_properties.csv
- path: `/app/outputs/thermal_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic properties: thermal expansion coefficient, adiabatic bulk modulus, specific heat at constant volume, and entropy at zero pressure and at 50 GPa for selected temperatures.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `P_GPa`, `alpha_V_1e-6`, `B_S_GPa`, `C_V_J_molK`, `S_J_molK`
  - `items`: object
  - `units`:
    - `alpha_V_1e-6`: 10^{-6} K^{-1}
    - `B_S_GPa`: GPa
    - `C_V_J_molK`: J/mol·K
    - `S_J_molK`: J/mol·K

Notes: All properties are computed within the quasiharmonic approximation using DFPT. Tolerances and scoring details are hidden; the agent must produce physically reasonable values consistent with the described procedure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float, GPa",
          "C12": "float, GPa",
          "C44": "float, GPa"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa"
        }
      },
      "description": "Zero-pressure elastic constants C11, C12, C44 of bcc W in GPa."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_point",
          "freq1",
          "freq2",
          "freq3"
        ],
        "items": {},
        "units": {
          "freq1": "THz",
          "freq2": "THz",
          "freq3": "THz"
        },
        "notes": "q_point is a string: one of 'GAMMA', 'H', 'P'."
      },
      "description": "Phonon frequencies at high-symmetry q-points Gamma, H, P at zero pressure. Three branch frequencies per point in THz."
    },
    {
      "file": "thermal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "P_GPa",
          "alpha_V_1e-6",
          "B_S_GPa",
          "C_V_J_molK",
          "S_J_molK"
        ],
        "items": {},
        "units": {
          "alpha_V_1e-6": "10^{-6} K^{-1}",
          "B_S_GPa": "GPa",
          "C_V_J_molK": "J/mol·K",
          "S_J_molK": "J/mol·K"
        }
      },
      "description": "Thermodynamic properties: thermal expansion coefficient, adiabatic bulk modulus, specific heat at constant volume, and entropy at zero pressure and at 50 GPa for selected temperatures."
    }
  ],
  "notes": "All properties are computed within the quasiharmonic approximation using DFPT. Tolerances and scoring details are hidden; the agent must produce physically reasonable values consistent with the described procedure."
}
```

## How you are scored
A hidden verifier will read your three scored artifacts and compare them to reference target values that are not shown to you. For elastic constants, a weighted deviation from the reference is computed; for phonon frequencies, the root‑mean‑square error across all nine frequencies is assessed; for thermodynamic properties, the mean absolute relative error over all (T,P) points is measured, supplemented by structural checks (monotonic trends, high‑temperature limit of C_V). These three stages carry weights of 40 % (elastic constants), 30 % (phonon frequencies), and 30 % (thermodynamic properties), combining to a final reward between 0 and 1. Tolerances are generous to absorb differences in pseudopotential, cutoffs, k‑point sampling, and numerical implementation, so an honest DFT re‑run scores high even if it does not match the reference exactly. Simply reporting a number without performing the computation will not succeed, because the agreement must be demonstrated across multiple unrelated quantities and conditions that cannot be guessed.
