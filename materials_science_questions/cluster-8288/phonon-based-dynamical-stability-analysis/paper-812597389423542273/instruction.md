# Phonon, Electronic, and Thermoelectric Properties of TiMoCO2 MXene Alloy

## Problem background
MXenes are a large family of two-dimensional (2D) transition metal carbides, nitrides, and carbonitrides with extensive compositional tunability for energy applications. This task focuses on a novel asymmetrically ordered Janus-like MXene alloy, TiMoCO₂, which features O(fcc)-Ti-C-Mo-O(hcp) stacking and space group P3m1. The alloy is theoretically predicted to be a promising high-performance water-splitting photocatalyst and thermoelectric material. The goal is to computationally determine its key physical properties that underpin these claims: electronic band gap, dynamical stability, carrier mobilities, thermoelectric power factors and optimal doping, and solar absorption-driven short-circuit current.

## Approach
The workflow uses first-principles calculations to reproduce these quantities from scratch. The electronic structure of the relaxed monolayer is computed with a hybrid functional (HSE06) to obtain the band gap and the frequency-dependent dielectric function. Phonon dispersion is calculated via density functional perturbation theory (DFPT) to assess dynamical stability. Electron-phonon coupling is treated within the Wannier function (EPW) framework, and transport properties (carrier mobilities, Seebeck coefficient, electrical conductivity) are evaluated using the self-energy relaxation time approximation (SERTA). Doping effects are simulated under a rigid-band approximation, and power factors are extracted from the Boltzmann transport equation assuming an effective monolayer thickness. The optical absorption coefficient is derived from the HSE06 dielectric function and integrated with the AM1.5G solar spectrum to estimate the maximum short-circuit current for water-splitting. All calculations use publicly available open-source codes (Quantum ESPRESSO, EPW) and norm-conserving pseudopotentials (PseudoDojo).

## Reproduction target
Produce a file `results.json` at `/app/outputs/` containing the following computed properties for the TiMoCO₂ monolayer, with the indicated fields and units:
- `band_gap` (float, eV): the electronic band gap from HSE06.
- `phonon_stable` (bool): true if the phonon dispersion exhibits no imaginary frequencies within a small numerical tolerance.
- `hole_mobility` (float, cm²/V/s): room-temperature hole mobility.
- `electron_mobility` (float, cm²/V/s): room-temperature electron mobility.
- `n_type_power_factor` (float, µW/cm/K²): peak room-temperature n-type power factor.
- `p_type_power_factor` (float, µW/cm/K²): peak room-temperature p-type power factor.
- `n_opt_doping` (float, cm⁻³): carrier concentration at which the n-type power factor peaks.
- `p_opt_doping` (float, cm⁻³): carrier concentration at which the p-type power factor peaks.
- `max_short_circuit_current` (float, mA/cm²): maximum short-circuit current for water splitting.
All fields are mandatory.

## Assets

- TiMoCO2 crystal structure (Supporting Information): 10.1039/d0ma00391c
- Quantum ESPRESSO (electronic structure and phonon code): https://www.quantum-espresso.org/
- EPW (electron-phonon transport code): https://epw-code.org/
- PseudoDojo norm-conserving pseudopotentials: http://www.pseudo-dojo.org/
- AM1.5G solar spectrum

## Workflow steps

### Step 1: Construct TiMoCO2 structure
- Role: process
- Action: Build the TiMoCO2 crystal structure (O(fcc)-Ti-C-Mo-O(hcp), space group P3m1) using atomic coordinates and lattice constants from the paper's Supporting Information (DOI: 10.1039/d0ma00391c).
- Evidence: `/app/outputs/structure_constructed.txt`

### Step 2: DFT structural relaxation (PBE)
- Role: process
- Action: Relax the TiMoCO2 structure using DFT-PBE as implemented in Quantum ESPRESSO, with PseudoDojo norm-conserving pseudopotentials, plane-wave cutoff 100 Ry, sufficient k-point density, dipole correction, and ~15 Å vacuum. Converge forces below 1e-3 eV/Å.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 3: Phonon dispersion (DFPT)
- Role: process
- Action: Compute the phonon dispersion of the relaxed structure using DFPT in Quantum ESPRESSO with the same pseudopotentials and cutoff. Use a k/q-point mesh consistent with convergence requirements.
- Evidence: `/app/outputs/phonon_frequencies.txt`

### Step 4: PBE band structure for Wannierization
- Role: process
- Action: Perform a PBE band structure calculation on a dense k-point mesh (suitable for Wannierization and electron-phonon coupling) using Quantum ESPRESSO.
- Evidence: `/app/outputs/pbe_bands.dat`

### Step 5: Wannierization and EPW transport
- Role: process
- Action: Generate maximally localized Wannier functions and compute electron-phonon matrix elements using EPW. Within EPW, evaluate relaxation times and band velocities using the SERTA method to produce transport spectral quantities required for mobility and thermoelectric properties.
- Evidence: none

### Step 6: HSE06 electronic structure and optics
- Role: process
- Action: Using the relaxed structure, perform a HSE06 hybrid functional calculation to obtain the electronic band structure (band gap) and the frequency-dependent dielectric function. Use sufficient k-point sampling and include dipole correction.
- Evidence: `/app/outputs/hse06_epsilon.dat`

### Step 7: Extract and report all key properties
- Role: scored (load-bearing)
- Action: From the raw outputs of previous steps, compute: (1) band gap (eV) from HSE06 band structure; (2) phonon stability (boolean, true if no imaginary frequencies beyond a small tolerance) from phonon frequencies; (3) room-temperature hole and electron mobilities (cm²/V/s) from EPW SERTA results; (4) peak n-type and p-type power factors (μW/cm/K²) and optimal doping concentrations (cm⁻³) by applying rigid-band approximation and solving Boltzmann transport using EPW data, assuming an effective monolayer thickness of 7.2 Å; (5) maximum short-circuit current (mA/cm²) by integrating the optical absorption coefficient (derived from HSE06 dielectric function) with the AM1.5G solar spectrum. Write all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "band_gap": float (eV),
  "phonon_stable": bool,
  "hole_mobility": float (cm2/V/s),
  "electron_mobility": float (cm2/V/s),
  "n_type_power_factor": float (muW/cm/K2),
  "p_type_power_factor": float (muW/cm/K2),
  "n_opt_doping": float (cm-3),
  "p_opt_doping": float (cm-3),
  "max_short_circuit_current": float (mA/cm2)
}
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
- target_policy: reference_match
- description: JSON file containing the key reproduced quantities: electronic band gap, phonon stability, carrier mobilities, peak thermoelectric power factors, optimal doping concentrations, and maximum short-circuit current.
- schema:
  - `type`: object
  - `required`:
    - `band_gap`: float (eV)
    - `phonon_stable`: bool
    - `hole_mobility`: float (cm2/V/s)
    - `electron_mobility`: float (cm2/V/s)
    - `n_type_power_factor`: float (muW/cm/K2)
    - `p_type_power_factor`: float (muW/cm/K2)
    - `n_opt_doping`: float (cm-3)
    - `p_opt_doping`: float (cm-3)
    - `max_short_circuit_current`: float (mA/cm2)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `band_gap`: eV
    - `hole_mobility`: cm2/V/s
    - `electron_mobility`: cm2/V/s
    - `n_type_power_factor`: muW/cm/K2
    - `p_type_power_factor`: muW/cm/K2
    - `n_opt_doping`: cm-3
    - `p_opt_doping`: cm-3
    - `max_short_circuit_current`: mA/cm2

Notes: The hidden checker compares each field to paper-reported gold values with appropriate tolerances (band_gap: ±0.05 eV, phonon_stable must be True, mobilities: ±20% of midpoint of reported range, power factors: threshold_or_better, doping concentrations: ±50%, short-circuit current: ±20%). Gold values are hardcoded in the checker.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap": "float (eV)",
          "phonon_stable": "bool",
          "hole_mobility": "float (cm2/V/s)",
          "electron_mobility": "float (cm2/V/s)",
          "n_type_power_factor": "float (muW/cm/K2)",
          "p_type_power_factor": "float (muW/cm/K2)",
          "n_opt_doping": "float (cm-3)",
          "p_opt_doping": "float (cm-3)",
          "max_short_circuit_current": "float (mA/cm2)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "band_gap": "eV",
          "hole_mobility": "cm2/V/s",
          "electron_mobility": "cm2/V/s",
          "n_type_power_factor": "muW/cm/K2",
          "p_type_power_factor": "muW/cm/K2",
          "n_opt_doping": "cm-3",
          "p_opt_doping": "cm-3",
          "max_short_circuit_current": "mA/cm2"
        }
      },
      "description": "JSON file containing the key reproduced quantities: electronic band gap, phonon stability, carrier mobilities, peak thermoelectric power factors, optimal doping concentrations, and maximum short-circuit current."
    }
  ],
  "notes": "The hidden checker compares each field to paper-reported gold values with appropriate tolerances (band_gap: ±0.05 eV, phonon_stable must be True, mobilities: ±20% of midpoint of reported range, power factors: threshold_or_better, doping concentrations: ±50%, short-circuit current: ±20%). Gold values are hardcoded in the checker."
}
```

## How you are scored
A hidden verifier reads `results.json` and compares each field to hidden reference values derived from the original publication. Each field is scored according to its own criteria: numerical fields are checked within tolerances that accommodate legitimate toolchain spread; `phonon_stable` must be true; directional metrics (e.g., power factors) are evaluated on a “meet or exceed” basis. The verifier combines the per-field scores using a fixed weighting to produce a final score between 0 and 1. You must faithfully execute the computational pipeline; simply guessing or fabricating numbers without performing the calculations will not meet the verifier’s checks.
