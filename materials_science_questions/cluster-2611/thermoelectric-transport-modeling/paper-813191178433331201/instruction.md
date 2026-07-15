# Thermoelectric Transport Modeling under Biaxial Strain

## Problem background
Thermoelectric materials convert heat to electricity, and their efficiency is governed by the dimensionless figure of merit ZT = S²σT/κ, where S is the Seebeck coefficient, σ the electrical conductivity, T the temperature, and κ the thermal conductivity. Magnesium silicide (Mg₂Si) is a promising candidate for waste-heat recovery in the 500–800 K range because it is non-toxic, earth-abundant, and exhibits competitive thermoelectric performance. One strategy to enhance ZT is to tune the electronic band structure through mechanical strain, which can dramatically alter the transport properties. This work investigates how in-plane biaxial strain — ranging from compressive to tensile — affects the electronic band structure and the resulting thermoelectric transport coefficients of bulk Mg₂Si, focusing on electrical conductivity, Seebeck coefficient, and power factor. The key open question is: how do these quantities change with strain, and what benefit or penalty arises for the thermoelectric performance?

## Approach
The reproduction adopts the same two-step computational approach described in the literature. First, first-principles density-functional theory (DFT) calculations are performed within the generalized gradient approximation (GGA-PBE) using the plane‑wave pseudopotential method. The electronic band structure of Mg₂Si is computed for the unstrained equilibrium crystal and for a series of in‑plane biaxial strains applied at constant volume, which changes the c/a ratio. The band energies on a dense k‑mesh are saved as the input for transport calculations. Second, the constant‑relaxation‑time approximation to the semiclassical Boltzmann transport equation is applied to compute the electrical conductivity tensor (σ/τ, where τ is the relaxation time), the Seebeck coefficient tensor, and the power factor tensor as functions of temperature and chemical potential (doping level). The simulation spans both electron (n‑type) and hole (p‑type) doping across a wide range of carrier concentrations and temperatures. The workflow results in a structured set of tensor components and total values for each strain, temperature, doping type, and doping level, from which the effect of strain on the transport properties can be assessed.

## Reproduction target
Produce a JSON file, `transport_properties.json`, containing the computed transport coefficients for Mg₂Si under in‑plane biaxial strains from −2% to +2% (in steps of 0.5% or 1%), including the unstrained (0%) case. For each strain, report results at two temperatures (300 K and 900 K), for both electron (n‑type) and hole (p‑type) doping, and at two doping concentrations: 1×10¹⁸ cm⁻³ and 1.2×10²⁰ cm⁻³. For every condition, provide the following tensor components and derived total values: electrical conductivity σₓₓ/τ and σ_zz/τ, Seebeck coefficient Sₓₓ and S_zz, power factor PFₓₓ and PF_zz, as well as the total sums σ_total = σₓₓ + σ_zz, S_total = (σₓₓ·Sₓₓ + σ_zz·S_zz) / σ_total, and PF_total = S_total²·σ_total. All quantities must be expressed in consistent units (σ in arbitrary units of (Ω·m·s)⁻¹, S in μV/K, PF in arbitrary or SI‑based units). The exact structure is specified in the output contract. The goal is to obtain a physically reasonable dataset that captures how these properties vary with strain, temperature, and doping.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- BoltzTraP: https://www.boltztrap.org
- Mg2Si crystal structure
- Ultrasoft pseudopotentials for Mg and Si: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT band structure calculations
- Role: process
- Action: Perform first-principles DFT calculations for Mg2Si using Quantum ESPRESSO to obtain electronic band structures for unstrained and biaxially strained (-2% to +2% in-plane strain) Mg2Si.
- Evidence: `/app/outputs/dft_band_energies.dat`

### Step 2: Boltzmann transport calculations
- Role: process
- Action: Run BoltzTraP using the constant-relaxation-time approximation on the band structures from step 1 to compute electrical conductivity (σ/τ), Seebeck coefficient, and power factor tensors over a temperature range up to 1200 K.
- Evidence: `/app/outputs/sigma.trace`

### Step 3: Extract transport properties at specified conditions
- Role: scored
- Action: Parse BoltzTraP outputs to extract tensor components and totals for temperatures 300 K and 900 K, electron and hole doping at 1e18 cm^-3 and 1.2e20 cm^-3, for each strain. Compute total values (sum of xx and zz). Save to transport_properties.json.
- Output file: `/app/outputs/transport_properties.json`
- Format: json
- Contract: Nested JSON object: strain (string e.g. '0.0','0.5','1.0','1.5','2.0','-0.5','-1.0','-1.5','-2.0') -> temperature (string '300','900') -> doping_type (string 'electron','hole') -> doping_level (string '1e18','1.2e20') -> object with float keys: sigma_xx, sigma_zz, sigma_total, S_xx, S_zz, S_total, PF_xx, PF_zz, PF_total. Units: sigma in arbitrary units (σ/τ), S in μV/K, PF in W/(m·K^2) or consistent units.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transport_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transport_properties.json
- path: `/app/outputs/transport_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The complete set of transport property tensor components and totals at two temperatures and two doping levels for electron and hole carriers across all strain values. The checker will compare these computed values to the paper's reported enhancement ratios and trends.
- schema:
  - `type`: object
  - `description`: Nested object with keys: strain -> temperature -> doping_type -> doping_level -> {sigma_xx, sigma_zz, sigma_total, S_xx, S_zz, S_total, PF_xx, PF_zz, PF_total} all floats.

Notes: The scorer will verify electrical conductivity enhancement ratios, Seebeck reduction, and power factor trends against the paper's reference data with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transport_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Nested object with keys: strain -> temperature -> doping_type -> doping_level -> {sigma_xx, sigma_zz, sigma_total, S_xx, S_zz, S_total, PF_xx, PF_zz, PF_total} all floats."
      },
      "description": "The complete set of transport property tensor components and totals at two temperatures and two doping levels for electron and hole carriers across all strain values. The checker will compare these computed values to the paper's reported enhancement ratios and trends."
    }
  ],
  "notes": "The scorer will verify electrical conductivity enhancement ratios, Seebeck reduction, and power factor trends against the paper's reference data with appropriate tolerances."
}
```

## How you are scored
Your work is scored by a hidden verifier that reads your `transport_properties.json` and compares the computed values to expected physical trends and reference data, without revealing the exact reference numbers or tolerances. The verifier evaluates the three workflow stages collectively: the DFT band structure (step 1), the Boltzmann transport calculation (step 2), and the extracted properties (step 3). The reward is based on how well the extracted transport coefficients capture the known strain-dependent behavior of Mg₂Si. In particular, the verifier checks that the important ratios and trends (such as conductivity enhancement under strain, Seebeck coefficient variation, and power factor changes) are consistent with the underlying physics and with published benchmark calculations. The overall reward is a weighted combination of the checks across the different conditions (temperature, doping type, concentration). To obtain a high score, you must carry out a careful DFT calculation on a fine k‑mesh and perform the Boltzmann transport analysis accurately; simply reporting numbers without a meaningful simulation will not pass the hidden checks.
