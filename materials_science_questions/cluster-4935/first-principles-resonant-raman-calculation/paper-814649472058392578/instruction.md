# Computation of Resonant Raman Spectra for a Chromophore Molecule in Liquid 3He Droplets

## Problem background
Resonant Raman scattering from a chromophore molecule embedded in a liquid helium-3 nanodroplet can directly probe the local excitations of the Fermi liquid. Unlike ordinary liquids, the low-energy excitations of ³He consist of both collective phonon modes and a continuum of single particle-hole (PH) excitations across the Fermi level. The PH density of states remains finite at zero energy, so the response function of the droplet, which determines the vibronic spectrum, is dominated by PH excitations at low energies. When the incident light is tuned to the anti‑Stokes (red) side of the molecule’s absorption, the first‑order Raman spectrum directly reflects this total response function. The goal of this task is to compute the first‑order resonant Raman spectra of a glyoxal molecule in ³He droplets and to demonstrate that the spectral shape follows the response function on the red side, while on the blue (Stokes) side distinct peaks appear at the expected Raman shifts.

## Approach
The calculation proceeds in three stages. First, compute the total response function φ(E) by summing two contributions: the PH part, derived from Fermi‑liquid theory using the coupling constant α, the Fermi energy EF, temperature T, and a continuous cut‑off function that encapsulates the k‑space dependence; and the phonon part, which includes a localized phonon peak and a Debye‑like bulk continuum. Second, from φ(E) compute the absorption spectrum I(ω) via a Fourier transform that involves the electronic excitation energy E₀ and a radiative linewidth γ, then derive the complex refractive index Φ(ω) as the principal‑value integral of I(ω). Third, combine φ and Φ to evaluate the first‑order resonant Raman intensity W1(ω₀,Ω) for the four excitation frequencies ω₀ = E₀ + 30 cm⁻¹, E₀ + 50 cm⁻¹, E₀ − 30 cm⁻¹, and E₀ − 50 cm⁻¹. The entire pipeline uses standard physical parameters (α=1, EF=4.21 K, T=0.15 K, localized phonon energy 8.05 cm⁻¹, effective mass m* = 2.8 m, etc.) and a reasonable energy grid (at least −80 to 80 cm⁻¹ with sufficient resolution for FFTs).

## Reproduction target
Compute the first‑order resonant Raman scattering intensity W1(ω₀,Ω) for the four excitation conditions ω₀ = E₀ ± 30 cm⁻¹ and ω₀ = E₀ ± 50 cm⁻¹. Also compute the total response function φ(E) on the same energy grid. Package the four Raman spectra, the response function, and the common energy grid into `rrs_results.json`. The computed spectra should exhibit two key features: for red‑side excitation (ω₀ = E₀ − 30 cm⁻¹, E₀ − 50 cm⁻¹) the Raman line‑shape should closely correlate with the total response function φ(E); for blue‑side excitation (ω₀ = E₀ + 30 cm⁻¹, E₀ + 50 cm⁻¹) the spectra should display strong peaks at the incident Raman shifts of approximately 30 cm⁻¹ and 50 cm⁻¹, respectively.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute total response function φ(E)
- Role: process
- Action: Implement the particle-hole and phonon contributions to the response function using the Fermi-liquid model described in the paper with the given parameters (coupling constant α=1, Fermi energy EF=4.21 K, temperature T=0.15 K, localized phonon energy ~8.05 cm⁻¹, effective mass m* = 2.8 m, etc.). Compute the total response function φ(E) as the sum of both contributions.
- Evidence: `/app/outputs/response_function_evidence.json`

### Step 2: Compute absorption spectrum I(ω) and complex refractive index Φ(ω)
- Role: process
- Action: From the total response function, compute the absorption spectrum I(ω) via Fourier transform using a reasonable radiative linewidth γ (e.g., 0.5 cm⁻¹) and the electronic excitation energy E0. Then derive the complex refractive index Φ(ω) from I(ω) using the principal-value integral.
- Evidence: `/app/outputs/optical_data.json`

### Step 3: Compute first-order resonant Raman spectra
- Role: scored (load-bearing)
- Action: Using the total response function φ and complex refractive index Φ, calculate the first-order resonant Raman scattering spectrum W1(ω0,Ω) for four incident frequencies: ω0 = E0 + 30 cm⁻¹, E0 + 50 cm⁻¹, E0 − 30 cm⁻¹, E0 − 50 cm⁻¹. Package the spectra, the response function, and the common energy grid into rrs_results.json.
- Output file: `/app/outputs/rrs_results.json`
- Format: json
- Contract: {"Raman_spectra": {"E0_plus_30": [float], "E0_plus_50": [float], "E0_minus_30": [float], "E0_minus_50": [float]}, "response_function": [float], "energy_grid": [float]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rrs_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rrs_results.json
- path: `/app/outputs/rrs_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Contains the first-order Raman spectra for four excitation frequencies, the total response function φ(E), and the common energy grid. The checker will verify internal consistency between the Raman spectra and the submitted φ and Φ, check shape correlation between red-side spectra and φ, and validate peak positions for blue-side spectra.
- schema:
  - `type`: object
  - `required`: `Raman_spectra`, `response_function`, `energy_grid`
  - `properties`:
    - `Raman_spectra`:
      - `type`: object
      - `required`: `E0_plus_30`, `E0_plus_50`, `E0_minus_30`, `E0_minus_50`
      - `properties`:
        - `E0_plus_30`:
          - `type`: array
          - `items`:
            - `type`: number
        - `E0_plus_50`:
          - `type`: array
          - `items`:
            - `type`: number
        - `E0_minus_30`:
          - `type`: array
          - `items`:
            - `type`: number
        - `E0_minus_50`:
          - `type`: array
          - `items`:
            - `type`: number
    - `response_function`:
      - `type`: array
      - `items`:
        - `type`: number
    - `energy_grid`:
      - `type`: array
      - `items`:
        - `type`: number

Notes: The agent must implement the formulas using the stated parameters and a reasonable approximation for the cut-off function. All required inputs are parametric; no external data download is needed. The hidden checker will perform structural audits on the submitted artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rrs_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "Raman_spectra",
          "response_function",
          "energy_grid"
        ],
        "properties": {
          "Raman_spectra": {
            "type": "object",
            "required": [
              "E0_plus_30",
              "E0_plus_50",
              "E0_minus_30",
              "E0_minus_50"
            ],
            "properties": {
              "E0_plus_30": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "E0_plus_50": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "E0_minus_30": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "E0_minus_50": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "response_function": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "energy_grid": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "Contains the first-order Raman spectra for four excitation frequencies, the total response function φ(E), and the common energy grid. The checker will verify internal consistency between the Raman spectra and the submitted φ and Φ, check shape correlation between red-side spectra and φ, and validate peak positions for blue-side spectra."
    }
  ],
  "notes": "The agent must implement the formulas using the stated parameters and a reasonable approximation for the cut-off function. All required inputs are parametric; no external data download is needed. The hidden checker will perform structural audits on the submitted artifact."
}
```

## How you are scored
A hidden verifier will independently score your submission by examining the artifacts written to `/app/outputs`. The verifier will first recompute the Raman spectra from your submitted response function and complex refractive index to check internal consistency. It will then compute the Pearson correlation between each red‑side Raman spectrum and the response function over the same energy range, requiring a high correlation. For the blue‑side spectra, the verifier will locate the strongest peak in each and verify that its position is close to the expected Raman shift. A qualitative intensity ratio check will also be performed. These individual checks are combined with weights into a single reward in [0,1]. Simply reporting a target number without a correct computational pipeline will not pass the consistency and correlation audits.
