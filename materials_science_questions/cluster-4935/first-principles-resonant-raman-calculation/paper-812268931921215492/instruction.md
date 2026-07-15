# Non-local Raman Scattering from Coupled LO Phonon-Plasmon Mode in n-GaAs

## Problem background
In polar semiconductors such as n-type gallium arsenide (n-GaAs), free electrons can couple with longitudinal optical (LO) phonons to form coupled LO phonon-plasmon (LO-PL) modes. Raman scattering is a powerful probe of these modes, but when the laser light is in the absorption region of the crystal, the momentum transfer to the mode is no longer negligible and light attenuation becomes important. Early local theories (assuming zero wavevector) fail to explain the observed broad, asymmetric line shapes and the dependence of peak positions on laser wavelength. This work addresses the need for a non-local theory of Raman scattering from coupled LO-PL modes in an absorptive medium, which accounts for finite wavevector, light attenuation, and the interference between two scattering mechanisms (atomic displacement and electro-optic). The target is to compute the Raman line shape, the integrated scattering efficiency, and the dispersion of the lower branch (L-) of the coupled mode, and to compare with measurements on n-GaAs.

## Approach
The non-local theory describes Raman scattering from an opaque semiconductor using correlation functions of the atomic displacement and the induced electric field. The coupled system of carriers, LO phonons, and plasmons is treated within the random-phase approximation (RPA) for the electron gas and the Fröhlich interaction for electron-LO phonon coupling. The Raman line shape g(ω) is expressed as a convolution of a phonon spectral density J(q,ω) with a Lorentzian momentum distribution that reflects the mean wavevector and spread of the incident laser light, modulated by an interference factor. The phonon spectral density is derived from the LO-phonon Green function, which includes screening via the Lindhard dielectric function and the Landau damping width. The integrated scattering efficiency is obtained by frequency integration and multiplication by a prefactor that includes incident and scattered light frequencies, Raman tensor elements, and a reduction factor for the experimental incidence angle. The lower-branch (L-) peak positions are extracted from J(q,ω) or g(ω) at the mean wavevector for each laser wavelength. The implementation requires computing the Lindhard dielectric function on a grid of q and ω, evaluating the phonon spectral density, performing numerical convolution and integration, and outputting the integrated efficiencies and peak positions.

## Reproduction target
Compute the integrated Raman scattering efficiencies (in units of 10^{-11}) for n-GaAs at three carrier densities (8.4×10^17, 2×10^18, 4.5×10^18 cm^{-3}) and three laser wavelengths (5145, 4880, 4765 Å), using the material parameters and experimental conditions specified in the provided resources. Additionally, determine the peak frequencies (in cm^{-1}) of the lower branch (L-) of the coupled mode for the lowest carrier density at the same three wavelengths. The results must be output as the files integrated_efficiencies.json and peak_positions.csv with the exact formats given in the workflow steps.

## Assets

- GaAs material parameters (effective mass, dielectric constants, phonon frequencies)
- Complex refractive index of GaAs (N, K) at 5145, 4880, 4765 Å: 10.1103/PhysRev.129.1550
- Raman tensor magnitudes a, b and interference factor D: 10.1103/PhysRevLett.19.849
- Experimental parameters (carrier densities, wavelengths, incident angle, reduction factors)

## Workflow steps

### Step 1: Collect input parameters
- Role: process
- Action: Gather all necessary physical constants for GaAs: effective masses m* for each carrier density, static and optical dielectric constants ε0, ε∞, LO and TO phonon frequencies ωℓ, ωt, reduced mass density M̄, Raman tensor magnitudes |a|, |b|, interference factor D, complex refractive index data (N, K) at each laser wavelength (5145, 4880, 4765 Å), and experimental parameters (carrier densities, incident angle θ0=80°, mean wavevectors <q> and spreads Δq from Table I, reduction factors I(θ0) from Table II). Record these in a machine-readable format for later use.
- Evidence: `/app/outputs/input_parameters.json`

### Step 2: Compute RPA dielectric function and screening
- Role: process
- Action: Implement the random-phase approximation (RPA) dielectric function for a 3D free electron gas at T=0 K using the Lindhard formula. Discretize wavevectors q and frequencies ω on a grid covering the experimental range (q up to ~2×10^6 cm^{-1}, ω up to ~500 cm^{-1}). For each carrier density, compute ε(q,ω), the screening function χ(q,ω) = (q²ε∞/(4πe²))(1/ε - 1), and the Landau damping width Γ(q,ω). Store the results.
- Evidence: `/app/outputs/rpa_results.npz`

### Step 3: Compute phonon spectral density J(q,ω)
- Role: process
- Action: For each carrier density, compute the Fröhlich electron–LO phonon coupling vertex V(q) using ε∞, ε0, ωℓ, and the polarization vector. Evaluate the phonon spectral density J(q,ω) using the phonon Green function formula (neglecting anharmonicity, Γ_A=0) and the previously computed χ(q,ω) and Γ(q,ω). Store the J(q,ω) arrays.
- Evidence: `/app/outputs/J_q_omega.npz`

### Step 4: Compute Raman line shape g(ω)
- Role: process
- Action: For each (carrier density, laser wavelength) combination, compute the line shape function g(ω) by convolving J(q,ω) with a Lorentzian momentum distribution 1/[(q - <q>)² + (Δq)²] (using the <q> and Δq values from Table I), multiplying by the interference factor (1 + D (ω_t² - ω²)/ω_t²)², and including the Bose factor (n_q+1, equal to 1 at T=0 K). Store the (ω, g(ω)) arrays.
- Evidence: `/app/outputs/g_omega.npz`

### Step 5: Compute integrated Raman efficiencies
- Role: scored (load-bearing)
- Action: Numerically integrate g(ω) over frequency and multiply by the prefactor (4ħ a² ω0³ ωs / (M̄ ωℓ c^4)) * (2 vF / (π ωℓ²)) * I(θ0) to obtain the integrated Raman scattering efficiency S (in units of 10^{-11}) for each of the 9 (density, wavelength) combinations. Output the results as integrated_efficiencies.json.
- Output file: `/app/outputs/integrated_efficiencies.json`
- Format: json
- Contract: object with keys 'density_8.4e17', 'density_2e18', 'density_4.5e18', each mapping to an object with keys '5145', '4880', '4765' (strings) and values of type number (float).
- Scoring: scored by hidden verifier

### Step 6: Extract L- branch peak positions
- Role: scored
- Action: For the carrier density n=8.4×10^17 cm^{-3}, identify the frequency ω at which the phonon spectral density J(q=⟨q⟩, ω) (or g(ω)) is maximum for the lower branch (L-) at each of the three wavelengths (5145, 4880, 4765 Å). Convert to Raman shift in cm^{-1}. Output a CSV file peak_positions.csv with three rows.
- Output file: `/app/outputs/peak_positions.csv`
- Format: csv
- Contract: CSV with columns 'wavelength' (string, e.g. '5145') and 'peak_frequency' (number, in cm^{-1}). Three rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/integrated_efficiencies.json`
- `/app/outputs/peak_positions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### integrated_efficiencies.json
- path: `/app/outputs/integrated_efficiencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Integrated Raman scattering efficiencies for three carrier densities and three laser wavelengths, compared to paper Table II values with a relative tolerance.
- schema:
  - `type`: object
  - `required`: `density_8.4e17`, `density_2e18`, `density_4.5e18`
  - `items`:
    - `density_8.4e17`:
      - `type`: object
      - `required`: `5145`, `4880`, `4765`
      - `values`: float (efficiency in 10^{-11})
    - `density_2e18`:
      - `type`: object
      - `required`: `5145`, `4880`, `4765`
      - `values`: float (efficiency in 10^{-11})
    - `density_4.5e18`:
      - `type`: object
      - `required`: `5145`, `4880`, `4765`
      - `values`: float (efficiency in 10^{-11})
  - `unit`: 10^{-11}

### peak_positions.csv
- path: `/app/outputs/peak_positions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Peak positions of the L- mode for n=8.4×10^17 cm^{-3} at three wavelengths, compared to paper Fig. 2 values with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `wavelength`, `peak_frequency`
  - `columns`:
    - `wavelength`: string (e.g. '5145')
    - `peak_frequency`: number (cm^{-1})
  - `num_rows`: 3

Notes: The computed efficiencies and peak positions are verified against corresponding reference values from the literature. Tolerances are chosen to accommodate legitimate computational spread while rejecting trivial guesses.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "integrated_efficiencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "density_8.4e17",
          "density_2e18",
          "density_4.5e18"
        ],
        "items": {
          "density_8.4e17": {
            "type": "object",
            "required": [
              "5145",
              "4880",
              "4765"
            ],
            "values": "float (efficiency in 10^{-11})"
          },
          "density_2e18": {
            "type": "object",
            "required": [
              "5145",
              "4880",
              "4765"
            ],
            "values": "float (efficiency in 10^{-11})"
          },
          "density_4.5e18": {
            "type": "object",
            "required": [
              "5145",
              "4880",
              "4765"
            ],
            "values": "float (efficiency in 10^{-11})"
          }
        },
        "unit": "10^{-11}"
      },
      "description": "Integrated Raman scattering efficiencies for three carrier densities and three laser wavelengths, compared to paper Table II values with a relative tolerance."
    },
    {
      "file": "peak_positions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength",
          "peak_frequency"
        ],
        "columns": {
          "wavelength": "string (e.g. '5145')",
          "peak_frequency": "number (cm^{-1})"
        },
        "num_rows": 3
      },
      "description": "Peak positions of the L- mode for n=8.4×10^17 cm^{-3} at three wavelengths, compared to paper Fig. 2 values with an absolute tolerance."
    }
  ],
  "notes": "The computed efficiencies and peak positions are verified against corresponding reference values from the literature. Tolerances are chosen to accommodate legitimate computational spread while rejecting trivial guesses."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that implements the same theoretical framework and compares your computed integrated efficiencies and peak positions against reference values obtained independently from the same method. Each scored artifact (integrated efficiencies and peak positions) contributes to the total reward according to the weights assigned by the verifier. Merely reporting numbers without executing the full computational pipeline will result in a zero score, because the verifier checks the internal consistency and plausibility of the results. The verifier does not reveal the reference values or tolerances; your job is to faithfully implement the theory and produce the required outputs.
