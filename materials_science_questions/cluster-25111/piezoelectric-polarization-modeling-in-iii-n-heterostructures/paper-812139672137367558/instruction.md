# Polarization and Ionization Effects on UV Photodiode Responsivity

## Problem background
AlGaN-based p‑i‑n photodiodes are attractive for solar‑blind UV detection because their cutoff wavelength can be tuned by the Al composition. A typical front‑illuminated device uses a thin p‑GaN cap, an intrinsic Al₀.₃₃Ga₀.₆₇N absorption layer, and an n‑GaN substrate. In such heterostructures, spontaneous and piezoelectric polarisation create fixed sheet charges at the interfaces, modifying the energy‑band profile and carrier transport. At the same time, the large ionisation energies of dopants in III‑N materials lead to incomplete ionisation at room temperature. This task investigates how polarisation‑induced charges and incomplete ionisation affect the spectral responsivity of the photodiode, and whether they can improve its solar‑blindness — the ability to suppress photocurrent from longer‑wavelength background radiation.

## Approach
Build a one‑dimensional drift‑diffusion model that solves Poisson’s equation and the electron/hole continuity equations with optical generation, Shockley‑Read‑Hall recombination, radiative recombination, and incomplete‑ionisation statistics. Fixed sheet charges representing the total polarisation (spontaneous + piezoelectric) are introduced at the top surface, the p/i interface, and the i/n interface. The device structure is p‑GaN (20 nm, N_A as specified) / i‑Al₀.₃₃Ga₀.₆₇N (60 nm, N_D = 1×10¹⁴ cm⁻³) / n‑GaN (300 nm, N_D = 5×10¹⁸ cm⁻³). Four distinct configurations are simulated:

1. Full ionisation of all dopants + full polarisation charges.
2. Incomplete ionisation of the p‑GaN acceptor with N_A = 1×10¹⁸ cm⁻³.
3. Incomplete ionisation with N_A = 1×10²⁰ cm⁻³.
4. Full ionisation but with all polarisation charges at the p/i interface compensated (set to zero).

For each configuration, compute the short‑circuit current responsivity (A/W) for wavelengths from 250 nm to 400 nm under a constant incident photon flux of 5×10¹⁴ photons cm⁻² s⁻¹. The required material parameters (band offsets, effective masses, dielectric constants, elastic constants, piezoelectric constants, spontaneous polarisation, ionisation energies) are taken from standard III‑N literature references.

## Reproduction target
Produce the spectral responsivity (A/W) of the p‑GaN/i‑AlGaN/n‑GaN photodiode for the four conditions listed above and compile the results into a single CSV file covering at least 250–400 nm in steps no larger than 5 nm, including the exact wavelengths 280, 310, 340, and 365 nm. The verifier will derive from your spectra the solar‑blindness ratio (responsivity at 310 nm divided by responsivity at 365 nm) for each condition and the fractional change in responsivity between the full‑ionisation reference and each incomplete‑ionisation case. These derived quantities are checked against hidden reference criteria; you only need to supply the raw responsivity CSV.

## Assets

- III-N material parameters
- Python scientific computing stack: scipy,numpy

## Workflow steps

### Step 1: Input Preparation
- Role: process
- Action: Define the p-GaN(20nm)/i-Al0.33Ga0.67N(60nm)/n-GaN(300nm) photodiode structure and doping profiles. Assemble all material parameters (elastic constants, piezoelectric constants, spontaneous polarization, band offsets, ionization energies) from standard III-N references. Compute polarization-induced sheet charges at the top surface, p/i interface, and i/n interface using linear interpolation of binary compounds. Set up simulation inputs for the four target conditions: (1) full ionization + full polarization, (2) incomplete ionization with N_A=1e18 cm⁻³, (3) incomplete ionization with N_A=1e20 cm⁻³, (4) full ionization with compensated p/i interface charges.
- Evidence: `/app/outputs/input_parameters.json`

### Step 2: Device Simulation
- Role: process
- Action: Implement a one-dimensional drift-diffusion solver (Poisson and continuity equations with optical generation, SRH recombination, and incomplete-ionization statistics). Run the simulation for each of the four conditions over wavelengths 250–400 nm with a constant incident photon flux of 5×10¹⁴ cm⁻²s⁻¹. Record convergence logs and intermediate data.
- Evidence: `/app/outputs/simulation_logs.txt`

### Step 3: Responsivity Extraction
- Role: scored (load-bearing)
- Action: Extract short-circuit spectral responsivity (A/W) from the simulation results for each of the four conditions and compile them into a single CSV file. The file must cover at least 250–400 nm in steps no larger than 5 nm, including the exact wavelengths 280, 310, 340, and 365 nm.
- Output file: `/app/outputs/responsivity_spectra.csv`
- Format: csv
- Contract: Columns: condition (string, one of 'full_ion_polar','II_NA1e18','II_NA1e20','compensated'), wavelength_nm (int), responsivity_A_per_W (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/responsivity_spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### responsivity_spectra.csv
- path: `/app/outputs/responsivity_spectra.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw responsivity values used to recompute the solar-blindness ratio R(310nm)/R(365nm) and fractional change due to incomplete ionization.
- schema:
  - `type`: table
  - `required`:
    - `columns`: `condition`, `wavelength_nm`, `responsivity_A_per_W`
  - `required_columns`: `condition`, `wavelength_nm`, `responsivity_A_per_W`
  - `units`:
    - `wavelength_nm`: nm
    - `responsivity_A_per_W`: A/W

Notes: The checker recomputes the ratios and fractional changes directly from this CSV; absolute responsivity is also compared to hidden reference values digitised from the paper with a 15% relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "responsivity_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {
          "columns": [
            "condition",
            "wavelength_nm",
            "responsivity_A_per_W"
          ]
        },
        "required_columns": [
          "condition",
          "wavelength_nm",
          "responsivity_A_per_W"
        ],
        "units": {
          "wavelength_nm": "nm",
          "responsivity_A_per_W": "A/W"
        }
      },
      "description": "Raw responsivity values used to recompute the solar-blindness ratio R(310nm)/R(365nm) and fractional change due to incomplete ionization."
    }
  ],
  "notes": "The checker recomputes the ratios and fractional changes directly from this CSV; absolute responsivity is also compared to hidden reference values digitised from the paper with a 15% relative tolerance."
}
```

## How you are scored
A hidden verifier independently assesses your submitted artifacts. The primary scored product is `/app/outputs/responsivity_spectra.csv`. The verifier reads that CSV, computes for each condition the ratio `R(310 nm)/R(365 nm)` and the fractional change in responsivity at selected wavelengths between the full‑ionisation baseline and each incomplete‑ionisation case, and compares these computed values against reference expectations derived from the original study. The comparison uses appropriate tolerances to account for differences in numerical implementation. The process‑evidence files (`input_parameters.json`, `simulation_logs.txt`) are checked for structural completeness but carry little weight. Simply reporting the expected numbers without a genuine simulation run will not satisfy the verifier.
