# Jahn-Teller coupling and vibronic spectra of Cr²⁺ in ZnS and ZnSe

## Problem background
Substitutional Cr²⁺ impurities in ZnS and ZnSe exhibit a zero‑phonon doublet in their infrared emission and absorption spectra that cannot be explained by a simple crystal‑field model. The observed doublet consists of two closely spaced peaks with characteristic relative intensities: in emission the lower‑energy peak is stronger, while in absorption the higher‑energy peak dominates. The goal of this task is to compute the vibronic spectra including Jahn‑Teller coupling to τ₂ phonon modes, and to determine the zero‑phonon peak positions and the Huang‑Rhys factor for both compounds.

## Approach
The electronic Hamiltonian is built from crystal‑field splitting, spin‑orbit coupling (λ = 57 cm⁻¹) and spin‑spin interaction (ρ = 0.39 cm⁻¹). The total Hamiltonian adds a harmonic lattice contribution for τ₂ phonons and a linear Jahn‑Teller coupling to those phonons, with electronic coupling matrices D_i as derived for the ⁵T₂ and ⁵E multiplets in tetrahedral symmetry. The crystal‑field splitting 10Dq is set to match the observed threshold line (5218 cm⁻¹ for ZnS, 4971 cm⁻¹ for ZnSe). The phonon energy ℏω_τ and the Jahn‑Teller energies for the lower and upper multiplets are taken from the paper’s best‑fit values (provided in the workflow steps).

For each compound and each multiplet, the vibronic Hamiltonian is diagonalised by the Lanczos recursion method, yielding the lowest eigenenergies and eigenstates. Electric‑dipole transition matrix elements are then computed between the lower and upper multiplet eigenstates to obtain oscillator strengths. Emission and absorption spectra are synthesised by summing Lorentzian‑broadened lines: for transitions dominated by zero‑phonon components a narrow half‑width is used, while for transitions involving higher phonon overtones a broader width is employed. Absorption spectra additionally include Boltzmann population factors at liquid helium temperature (≈ 4.2 K). The spectra are sampled at fine energy resolution over the range that covers the zero‑phonon doublet.

The final step locates the two most intense peaks in each spectrum within a window around the expected doublet energies and records the peak energies and the relative intensity ordering. The Huang‑Rhys factor S_τ = E_JT^(τ)/ℏω_τ is evaluated directly from the input parameters.

## Reproduction target
For ZnS:Cr²⁺ and ZnSe:Cr²⁺, produce the following scored artifacts:
  - `znS_emission.csv` and `znS_absorption.csv` (energy in cm⁻¹, intensity in arbitrary units).
  - `znSe_emission.csv` and `znSe_absorption.csv` (same format).
  - `zero_phonon_params.json` containing, for each spectrum, the two zero‑phonon peak energies (ascending order, lower energy listed second) and the Huang‑Rhys factors S_τ for ZnS and ZnSe.
The expected result is that the zero‑phonon doublet is correctly resolved with the characteristic intensity reversal between emission and absorption (lower‑energy peak stronger in emission, higher‑energy peak stronger in absorption). The Huang‑Rhys factors should be consistent with the coupling parameters used in the Hamiltonian.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Assemble vibronic Hamiltonian
- Role: process
- Action: Construct the total Hamiltonian H = H_e + H_so + H_ss + H_L + H_e-L for the lower ⁵T₂ and upper ⁵E multiplets of Cr²⁺ in a tetrahedral crystal field, for ZnS and ZnSe. Use the atomic parameters λ=57 cm⁻¹, ρ=0.39 cm⁻¹, the crystal‑field splitting 10Dq set to 5218 cm⁻¹ (ZnS) and 4971 cm⁻¹ (ZnSe), the τ₂ phonon energy ℏω_τ = 100 cm⁻¹ (ZnS) and 70 cm⁻¹ (ZnSe), and the Jahn‑Teller energies E_JT^(τ)=260 cm⁻¹ (ZnS), 180 cm⁻¹ (ZnSe) for the lower multiplet and E_JT' = 370 cm⁻¹ (ZnS), 270 cm⁻¹ (ZnSe) for the upper multiplet. Build the electronic coupling matrices D_i as specified in the paper. Truncate the phonon Fock space with a suitable maximum phonon number to keep the Hamiltonian finite.
- Evidence: none

### Step 2: Lanczos diagonalization
- Role: process
- Action: For each compound (ZnS, ZnSe) and each multiplet (⁵T₂, ⁵E), use the Lanczos recursion method with a proper choice of initial state and over‑recursions to compute the lowest vibronic eigenstates and eigenenergies.
- Evidence: none

### Step 3: Compute transition oscillator strengths
- Role: process
- Action: From the vibronic eigenvectors, compute electric‑dipole transition matrix elements between the lower (⁵T₂) and upper (⁵E) multiplets for each compound. Evaluate the corresponding oscillator strengths and save a list of transition energies (cm⁻¹) together with their strengths.
- Evidence: none

### Step 4: ZnS emission spectrum
- Role: scored (load-bearing)
- Action: For ZnS:Cr²⁺, construct the emission spectrum by summing Lorentzian lines for every allowed transition. Use a half‑width of 1 cm⁻¹ for transitions predominantly involving zero‑phonon components (those near 5218 cm⁻¹) and 2 cm⁻¹ for the other lines. The spectrum should be a function of energy (cm⁻¹) and intensity; sample it at fine resolution over the range that covers the zero‑phonon doublet (e.g., 5100–5300 cm⁻¹). Do not apply Boltzmann factors. Output a CSV file with columns: energy (float), intensity (float).
- Output file: `/app/outputs/znS_emission.csv`
- Format: csv
- Contract: energy: float (cm⁻¹), intensity: float (arbitrary units)
- Scoring: scored by hidden verifier

### Step 5: ZnS absorption spectrum
- Role: scored
- Action: For ZnS:Cr²⁺, construct the absorption spectrum using the same Lorentzian widths as for emission. For each transition, multiply the oscillator strength by the Boltzmann factor exp(-E_i/kT) where E_i is the energy of the initial vibronic level of the lower (⁵T₂) multiplet and T ≈ 4.2 K. Sum over all initial and final states. Output a CSV with columns: energy (float), intensity (float) covering the same energy range.
- Output file: `/app/outputs/znS_absorption.csv`
- Format: csv
- Contract: energy: float (cm⁻¹), intensity: float (arbitrary units)
- Scoring: scored by hidden verifier

### Step 6: ZnSe emission spectrum
- Role: scored
- Action: For ZnSe:Cr²⁺, construct the emission spectrum analogously to ZnS, with Lorentzian widths of 1 cm⁻¹ for the zero‑phonon region near 4971 cm⁻¹ and 2 cm⁻¹ for the others. Output CSV with columns energy and intensity over the range covering the doublet (e.g., 4900–5100 cm⁻¹).
- Output file: `/app/outputs/znSe_emission.csv`
- Format: csv
- Contract: energy: float (cm⁻¹), intensity: float (arbitrary units)
- Scoring: scored by hidden verifier

### Step 7: ZnSe absorption spectrum
- Role: scored
- Action: For ZnSe:Cr²⁺, construct the absorption spectrum with Boltzmann weighting (T ≈ 4.2 K) and Lorentzian widths (1 cm⁻¹ / 2 cm⁻¹). Output a CSV with columns energy and intensity covering the relevant range.
- Output file: `/app/outputs/znSe_absorption.csv`
- Format: csv
- Contract: energy: float (cm⁻¹), intensity: float (arbitrary units)
- Scoring: scored by hidden verifier

### Step 8: Extract zero‑phonon peak parameters and Huang‑Rhys factor
- Role: scored
- Action: For each of the four CSV spectra, locate the two most intense peaks in the zero‑phonon region (ZnS: around 5218/5212 cm⁻¹, ZnSe: around 4971/4964 cm⁻¹) within a search window of ±10 cm⁻¹. Record their energies (cm⁻¹) and indicate which peak is stronger. Also compute the Huang‑Rhys factor S_τ = E_JT^(τ)/ℏω_τ for each compound using the input Jahn‑Teller energy and phonon frequency. Output a JSON file with structure: "znS_emission_peaks": [energy1, energy2], "znS_absorption_peaks": [energy1, energy2], "znSe_emission_peaks": [energy1, energy2], "znSe_absorption_peaks": [energy1, energy2], "S_tau_ZnS": float, "S_tau_ZnSe": float. The peak energies should be in ascending order (lower energy second).
- Output file: `/app/outputs/zero_phonon_params.json`
- Format: json
- Contract: JSON object with keys: znS_emission_peaks (list of two floats), znS_absorption_peaks (list of two floats), znSe_emission_peaks (list of two floats), znSe_absorption_peaks (list of two floats), S_tau_ZnS (float), S_tau_ZnSe (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/znS_emission.csv`
- `/app/outputs/znS_absorption.csv`
- `/app/outputs/znSe_emission.csv`
- `/app/outputs/znSe_absorption.csv`
- `/app/outputs/zero_phonon_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### znS_emission.csv
- path: `/app/outputs/znS_emission.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: ZnS:Cr²⁺ emission spectrum; checker recomputes zero-phonon doublet peak positions and relative intensities.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `intensity`
  - `units`:
    - `energy`: cm⁻¹
    - `intensity`: arbitrary

### znS_absorption.csv
- path: `/app/outputs/znS_absorption.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: ZnS:Cr²⁺ absorption spectrum; checker recomputes peak positions and ordering.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `intensity`
  - `units`:
    - `energy`: cm⁻¹
    - `intensity`: arbitrary

### znSe_emission.csv
- path: `/app/outputs/znSe_emission.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: ZnSe:Cr²⁺ emission spectrum; checker recomputes zero-phonon doublet peak positions and relative intensities.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `intensity`
  - `units`:
    - `energy`: cm⁻¹
    - `intensity`: arbitrary

### znSe_absorption.csv
- path: `/app/outputs/znSe_absorption.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: ZnSe:Cr²⁺ absorption spectrum; checker recomputes peak positions and ordering.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `intensity`
  - `units`:
    - `energy`: cm⁻¹
    - `intensity`: arbitrary

### zero_phonon_params.json
- path: `/app/outputs/zero_phonon_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zero-phonon doublet peak energies and Huang-Rhys factors for both compounds; compared to paper reference values.
- schema:
  - `type`: object
  - `required`: `znS_emission_peaks`, `znS_absorption_peaks`, `znSe_emission_peaks`, `znSe_absorption_peaks`, `S_tau_ZnS`, `S_tau_ZnSe`
  - `properties`:
    - `znS_emission_peaks`:
      - `type`: array
      - `items`: number
      - `minItems`: 2
      - `maxItems`: 2
    - `znS_absorption_peaks`:
      - `type`: array
      - `items`: number
      - `minItems`: 2
      - `maxItems`: 2
    - `znSe_emission_peaks`:
      - `type`: array
      - `items`: number
      - `minItems`: 2
      - `maxItems`: 2
    - `znSe_absorption_peaks`:
      - `type`: array
      - `items`: number
      - `minItems`: 2
      - `maxItems`: 2
    - `S_tau_ZnS`:
      - `type`: number
    - `S_tau_ZnSe`:
      - `type`: number

Notes: All output artifacts must be written under /app/outputs. The Huang-Rhys factor S_tau is defined as E_JT^(τ)/ℏω_τ, evaluated directly from the given Jahn-Teller energies and phonon frequencies used in the Hamiltonian. The peak lists must be in ascending order (lower cm⁻¹ value second).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "znS_emission.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "intensity"
        ],
        "units": {
          "energy": "cm⁻¹",
          "intensity": "arbitrary"
        }
      },
      "description": "ZnS:Cr²⁺ emission spectrum; checker recomputes zero-phonon doublet peak positions and relative intensities."
    },
    {
      "file": "znS_absorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "intensity"
        ],
        "units": {
          "energy": "cm⁻¹",
          "intensity": "arbitrary"
        }
      },
      "description": "ZnS:Cr²⁺ absorption spectrum; checker recomputes peak positions and ordering."
    },
    {
      "file": "znSe_emission.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "intensity"
        ],
        "units": {
          "energy": "cm⁻¹",
          "intensity": "arbitrary"
        }
      },
      "description": "ZnSe:Cr²⁺ emission spectrum; checker recomputes zero-phonon doublet peak positions and relative intensities."
    },
    {
      "file": "znSe_absorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "intensity"
        ],
        "units": {
          "energy": "cm⁻¹",
          "intensity": "arbitrary"
        }
      },
      "description": "ZnSe:Cr²⁺ absorption spectrum; checker recomputes peak positions and ordering."
    },
    {
      "file": "zero_phonon_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "znS_emission_peaks",
          "znS_absorption_peaks",
          "znSe_emission_peaks",
          "znSe_absorption_peaks",
          "S_tau_ZnS",
          "S_tau_ZnSe"
        ],
        "properties": {
          "znS_emission_peaks": {
            "type": "array",
            "items": "number",
            "minItems": 2,
            "maxItems": 2
          },
          "znS_absorption_peaks": {
            "type": "array",
            "items": "number",
            "minItems": 2,
            "maxItems": 2
          },
          "znSe_emission_peaks": {
            "type": "array",
            "items": "number",
            "minItems": 2,
            "maxItems": 2
          },
          "znSe_absorption_peaks": {
            "type": "array",
            "items": "number",
            "minItems": 2,
            "maxItems": 2
          },
          "S_tau_ZnS": {
            "type": "number"
          },
          "S_tau_ZnSe": {
            "type": "number"
          }
        }
      },
      "description": "Zero-phonon doublet peak energies and Huang-Rhys factors for both compounds; compared to paper reference values."
    }
  ],
  "notes": "All output artifacts must be written under /app/outputs. The Huang-Rhys factor S_tau is defined as E_JT^(τ)/ℏω_τ, evaluated directly from the given Jahn-Teller energies and phonon frequencies used in the Hamiltonian. The peak lists must be in ascending order (lower cm⁻¹ value second)."
}
```

## How you are scored
A hidden verifier independently scores each artifact. For the four CSV spectra, it identifies the two highest peaks in a window near the zero‑phonon region and checks whether their energies and their relative intensity ordering match the paper’s reference. For the JSON file, it compares the listed peak energies and the Huang‑Rhys factors against the reference values. Each artifact contributes a weighted share to the total reward (maximum 1.0). Simply reporting numbers without computing the full vibronic model and spectra will not satisfy the scoring criteria.
