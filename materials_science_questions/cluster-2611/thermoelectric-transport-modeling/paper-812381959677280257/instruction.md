# Modeling In-Plane Thermoelectric Transport in Si/Ge Superlattices with Quantum-Classical Boltzmann Theory

## Problem background
Thermoelectric energy conversion in Si/Ge superlattices is influenced by both quantum confinement (subband formation) and classical interface scattering. A quantitative model that combines these effects is needed to predict the Seebeck coefficient, electrical conductivity, and power factor as functions of temperature and doping. This task implements the Boltzmann transport description that treats specularly reflected electrons as two-dimensional carriers with subband energies from a Kronig-Penney model and diffusely scattered electrons as three-dimensional carriers with parabolic dispersion, including multi-valley and strain effects. The computed transport properties are to be evaluated against measured data for three Si/Ge superlattice samples with different period thicknesses and doping levels.

## Approach
The modeling proceeds in several stages: (1) Compute the strain tensor and band-edge shifts for each superlattice sample using the lattice constants, compliance constants, and deformation potentials of Si and Ge, assuming the superlattice is grown on a substrate with composition Si₀.₂Ge₀.₈ (as used in the original study). The conduction band offsets between Si and Ge layers are obtained from the unstrained offset (ΔE_c⁰ = 0.22 eV) plus the strain-induced shifts from deformation potential theory. (2) For each sample, solve the Kronig-Penney model for the one-dimensional superlattice potential (determined by the strained band offsets) to obtain the quantized subband energies at the zone centre (k_∥ = 0) for the specularly scattered electrons. The relevant conduction band valleys are the Δ valleys of Si, with effective masses m_∥ = 0.916 m₀ and m_⊥ = 0.19 m₀. (3) Construct the transport integrals ℓ^(α) (α = 0, 1, 2) that combine contributions from both specular and diffuse scattering. For specular electrons, use a two-dimensional density of states derived from the subband energies and the in-plane effective masses; for diffuse electrons, use the three-dimensional parabolic density of states of bulk Si. The diffuse fraction is determined by the electron specularity parameter p_e = 0.7. A Fuchs-Sondheimer boundary scattering function g(η, μ) weights the diffuse contribution. The relaxation time is approximated via a constant mobility μ = 100 cm²/Vs, and the carrier concentration is used to compute the Fermi level at each temperature. (4) From the transport integrals, compute the electrical conductivity σ = ℓ^(0), the Seebeck coefficient S = –(1/eT)(ℓ^(0))⁻¹ℓ^(1), and the power factor PF = S²σ. Evaluate these quantities for the three samples (JL254, JL255, JL256) under two regimes: (a) power factor as a function of carrier concentration from 1×10¹⁷ to 1×10²¹ cm⁻³ at T = 300 K; (b) Seebeck coefficient and electrical conductivity as functions of temperature from 80 K to 300 K, using the nominal donor concentrations of each sample (0.8×10¹⁹, 1.0×10¹⁹, and 1.2×10¹⁹ cm⁻³, respectively). The specularity p_e = 0.7 and constant mobility μ = 100 cm²/Vs are used throughout.

Material constants (from the literature):
- Si: lattice constant a_Si = 5.4309 Å, Ge: a_Ge = 5.6461 Å.
- Deformation potentials (eV): E_c^Δ,Si = 4.18, E_c^Δ,Ge = 2.55; E_c^L,Si = –0.66, E_c^L,Ge = –1.54; Ξ_u^Δ,Si = 9.16, Ξ_u^Δ,Ge = 9.42; Ξ_u^L,Si = 16.14, Ξ_u^L,Ge = 15.13.
- Compliance constants (10¹² dyn/cm²): Si: c₁₁ = 1.675, c₁₂ = 0.650; Ge: c₁₁ = 1.315, c₁₂ = 0.494.
- Band offsets at unstrained Si/Ge: ΔE_v⁰ = 0.68 eV, ΔE_c⁰ = 0.22 eV.
- Substrate composition: Si₀.₂Ge₀.₈ (Vegard’s law for lattice constant a_s = 0.2 a_Si + 0.8 a_Ge).

Superlattice sample structures:
- JL254: 91 periods, Si layer 88 Å, Ge layer 22 Å, doping 0.8×10¹⁹ cm⁻³.
- JL255: 133 periods, Si layer 60 Å, Ge layer 15 Å, doping 1.0×10¹⁹ cm⁻³.
- JL256: 250 periods, Si layer 32 Å, Ge layer 8 Å, doping 1.2×10¹⁹ cm⁻³.

All doping is n-type (Sb). The electron specularity is p_e = 0.7, and the constant electron mobility is μ = 100 cm²/Vs.

## Reproduction target
Produce three comma-separated value (CSV) files, each containing the results of the combined Boltzmann transport model for the three Si/Ge superlattice samples under the specified conditions. The files and their required columns are:
- power_factor_vs_concentration.csv: columns = sample, carrier_concentration_cm3, power_factor_WmK2. Rows for each sample (JL254, JL255, JL256) at a set of carrier concentrations spanning 1×10¹⁷ to 1×10²¹ cm⁻³ (logarithmically spaced is recommended) at T = 300 K.
- seebeck_vs_temperature.csv: columns = sample, temperature_K, seebeck_uVK. For each sample at its nominal doping concentration, rows covering temperatures from 80 K to 300 K (e.g., at intervals of 10 K or 20 K).
- conductivity_vs_temperature.csv: columns = sample, temperature_K, conductivity_Sm. Same temperature set, same fixed doping as for the Seebeck file.
The submission is scored by comparing the computed curves against hidden reference data derived from experimental measurements. The evaluation checks that the power factor decreases with decreasing superlattice period at a given doping, that the magnitude of the Seebeck coefficient increases with decreasing temperature, and that the electrical conductivity decreases with decreasing temperature for the constant‑mobility case.

## Assets
None. All constants, material parameters, and sample geometries needed for the calculation are explicitly listed in the instruction. No external data files, model weights, or packages beyond a standard Python numerical computing environment are required.

## Workflow steps

### Step 1: Parameter and geometry assembly
- Role: process
- Action: Assemble all material constants (effective masses, deformation potentials, lattice constants, compliance constants, band offsets) and the three sample layer thicknesses and nominal doping levels as given in the problem statement. Compute strain tensor components and conduction/valence band-edge shifts for each superlattice sample using deformation potential theory.
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Subband energy calculation
- Role: process
- Action: Using the Kronig-Penney model with the superlattice potential derived from the band offsets, compute the quantized subband energies for specularly scattered electrons in each relevant valley for the given sample structures.
- Evidence: `/app/outputs/subband_log.txt`

### Step 3: Power factor vs carrier concentration
- Role: scored (load-bearing)
- Action: For each of the three samples (JL254, JL255, JL256), evaluate the combined Boltzmann transport model at T=300 K over a range of carrier concentrations (e.g., 1e17–1e21 cm⁻³). Use constant mobility μ=100 cm²/Vs and electron specularity p_e=0.7. Compute electrical conductivity σ, Seebeck coefficient S, and power factor PF = S²σ. Write results to CSV.
- Output file: `/app/outputs/power_factor_vs_concentration.csv`
- Format: csv
- Contract: Columns: sample (str), carrier_concentration_cm3 (float), power_factor_WmK2 (float).
- Scoring: scored by hidden verifier

### Step 4: Seebeck coefficient vs temperature
- Role: scored (load-bearing)
- Action: For each sample at its nominal doping level from the structure table, compute the Seebeck coefficient S over temperatures 80–300 K using the combined model with constant mobility and specularity 0.7. Write results to CSV.
- Output file: `/app/outputs/seebeck_vs_temperature.csv`
- Format: csv
- Contract: Columns: sample (str), temperature_K (float), seebeck_uVK (float).
- Scoring: scored by hidden verifier

### Step 5: Electrical conductivity vs temperature
- Role: scored (load-bearing)
- Action: For each sample at its nominal doping, compute the electrical conductivity σ over temperatures 80–300 K using the combined model with constant mobility (μ=100 cm²/Vs) and specularity 0.7. Write results to CSV.
- Output file: `/app/outputs/conductivity_vs_temperature.csv`
- Format: csv
- Contract: Columns: sample (str), temperature_K (float), conductivity_Sm (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/power_factor_vs_concentration.csv`
- `/app/outputs/seebeck_vs_temperature.csv`
- `/app/outputs/conductivity_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### power_factor_vs_concentration.csv
- path: `/app/outputs/power_factor_vs_concentration.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Power factor (S²σ) as a function of carrier concentration at 300 K for the three Si/Ge superlattice samples, computed with the combined model at constant mobility and specularity 0.7.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `carrier_concentration_cm3`, `power_factor_WmK2`

### seebeck_vs_temperature.csv
- path: `/app/outputs/seebeck_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Seebeck coefficient as a function of temperature (80–300 K) for the three Si/Ge superlattice samples at their nominal doping, from the combined model with constant mobility.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `temperature_K`, `seebeck_uVK`

### conductivity_vs_temperature.csv
- path: `/app/outputs/conductivity_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Electrical conductivity as a function of temperature (80–300 K) for the three Si/Ge superlattice samples at nominal doping, from the combined model with constant mobility (μ=100 cm²/Vs).
- schema:
  - `type`: table
  - `required_columns`: `sample`, `temperature_K`, `conductivity_Sm`

Notes: All required material constants and sample geometries are provided in the task statement; no external data download is needed. The checker will compute mean absolute percentage error (MAPE) against hidden digitised reference curves and verify relative ordering among samples/conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "power_factor_vs_concentration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "carrier_concentration_cm3",
          "power_factor_WmK2"
        ]
      },
      "description": "Power factor (S²σ) as a function of carrier concentration at 300 K for the three Si/Ge superlattice samples, computed with the combined model at constant mobility and specularity 0.7."
    },
    {
      "file": "seebeck_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "temperature_K",
          "seebeck_uVK"
        ]
      },
      "description": "Seebeck coefficient as a function of temperature (80–300 K) for the three Si/Ge superlattice samples at their nominal doping, from the combined model with constant mobility."
    },
    {
      "file": "conductivity_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "temperature_K",
          "conductivity_Sm"
        ]
      },
      "description": "Electrical conductivity as a function of temperature (80–300 K) for the three Si/Ge superlattice samples at nominal doping, from the combined model with constant mobility (μ=100 cm²/Vs)."
    }
  ],
  "notes": "All required material constants and sample geometries are provided in the task statement; no external data download is needed. The checker will compute mean absolute percentage error (MAPE) against hidden digitised reference curves and verify relative ordering among samples/conditions."
}
```

## How you are scored
After you submit your output files, a hidden verifier script inspects each of the three scored CSV artifacts. For each file, the verifier numerically compares your computed values against a set of hidden reference data (derived from published experimental curves) using mean absolute percentage error (MAPE) and verifies qualitative trends (relative ordering among samples and temperature dependence). Each scored stage carries a weight, and the overall reward is the weighted sum of the per‑stage scores. The verifier does not simply check whether you reported a particular number; it evaluates the actual data points you wrote in the output files. Therefore, merely guessing or copying a known value is insufficient — you must run the model correctly to produce the required curves.
