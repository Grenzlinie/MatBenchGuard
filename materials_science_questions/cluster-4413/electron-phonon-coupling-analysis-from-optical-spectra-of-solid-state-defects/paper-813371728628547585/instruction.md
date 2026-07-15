# Exciton–phonon sidebands and spectral weight transfer in carbon nanotubes

## Problem background
Low-temperature optical spectra of carbon nanotubes often display vibronic sidebands that arise from the coupling between excitons and phonons. Understanding how the spectral weight is transferred from the zero‑phonon line to these sidebands as a function of temperature and nanotube chirality/diameter is essential for interpreting experimental data and for quantifying the exciton–phonon coupling strength. This task computes the integrated spectral weights of the zero‑phonon line and of the higher‑ and lower‑energy phonon sidebands for three nanotubes covering a wide temperature range, enabling a detailed study of sideband formation and weight redistribution.

## Approach
The theoretical framework is based on the many‑body density matrix formalism. The electronic band structure of each carbon nanotube is computed within the tight‑binding approximation combined with zone‑folding using standard graphene parameters. Coulomb and optical matrix elements are obtained from the tight‑binding Bloch functions. Excitonic effects are included by transforming the microscopic polarization into an excitonic basis: the stationary Bloch equation is solved in the one‑exciton limit to obtain the excitonic wave function of the first excitonic transition. The coupling to longitudinal optical (Γ‑LO) phonons is described by effective exciton–phonon matrix elements constructed from the excitonic wave function and from DFT‑derived electron‑phonon matrix elements. The absorption coefficient α(ω) is obtained by solving the coupled exciton‑phonon equations in the frequency domain at different temperatures, yielding spectra that contain the zero‑phonon line and phonon sidebands. Finally, the integrated intensity of each feature is extracted to quantify the spectral weight transfer.

## Reproduction target
Compute the temperature‑dependent absorption spectra for three carbon nanotubes with different chirality and diameter: metallic (21,0) and semiconducting (19,0) and (20,0), covering the temperature range 0 K to 2500 K. From each spectrum, integrate the intensity of the zero‑phonon line, the higher‑energy phonon sideband (at roughly the exciton energy plus 200 meV), and the lower‑energy sideband (at roughly the exciton energy minus 200 meV). Report the integrated weights – in the same arbitrary intensity units for all features – in a CSV file. The resulting table should allow a complete analysis of how the spectral weight shifts from the zero‑phonon line to the sidebands as a function of temperature and nanotube diameter.

## Assets

- DFT electron-phonon matrix elements for Γ-LO phonon in carbon nanotubes: 10.1103/PhysRevB.75.035427

## Workflow steps

### Step 1: Compute electronic structure and Coulomb/optical matrix elements
- Role: process
- Action: For each carbon nanotube (19,0), (20,0), (21,0), compute the electronic band structure ε_k using tight-binding with zone-folding (standard graphene parameters: nearest-neighbor hopping t≈3.0 eV, onsite energy ε=0). Derive the screened Coulomb matrix elements V_ren, V_exc and the optical matrix elements M_k^cv from tight-binding Bloch functions. Save all intermediate data for the next step.
- Evidence: `/app/outputs/matrix_elements.npz`

### Step 2: Compute excitonic wave function for the first exciton
- Role: process
- Action: Solve the stationary Bloch equation for the microscopic polarization in the one-exciton limit to obtain the excitonic wave function Ψ_{1k} of the first excitonic transition E11. Use the matrix elements from step0. Save the wave function for later use.
- Evidence: `/app/outputs/exciton_wavefunction.npz`

### Step 3: Solve exciton–phonon equations and compute absorption spectra
- Role: process
- Action: Using the excitonic wave function and the effective exciton–phonon matrix elements g_{11}(q) (constructed with |g_q| from the DFT reference and ℏω_LO ≈ 200 meV), solve the coupled exciton–phonon equations (Eqs. (3), (5), (6) of the model) in the frequency domain to compute the absorption coefficient α(ω) for the three nanotubes at temperatures ranging from 0 K to 2500 K. Choose phenomenological dephasing constants that yield reasonable linewidths. Save the full absorption spectra for each (tube, temperature).
- Evidence: `/app/outputs/absorption_spectra.npz`

### Step 4: Extract spectral weight transfer and sideband weights
- Role: scored (load-bearing)
- Action: For each tube and temperature, integrate the intensity of the zero-phonon line and the phonon sidebands at ω_n ± ω_LO from the absorption spectra. Compute the integrated weights (ZPL, higher-energy sideband, lower-energy sideband) and write them to a CSV file.
- Output file: `/app/outputs/spectral_weight_transfer.csv`
- Format: csv
- Contract: tube_index (string): tube label ('19,0', '20,0', '21,0'); temperature_K (float): temperature in kelvin; zpl_weight (float): integrated weight of the zero-phonon line; higher_sideband_weight (float): integrated weight of the sideband at ω_n + ω_LO; lower_sideband_weight (float): integrated weight of the sideband at ω_n - ω_LO. All weights are in the same arbitrary intensity units and should sum to the total spectral weight of the absorption feature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spectral_weight_transfer.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spectral_weight_transfer.csv
- path: `/app/outputs/spectral_weight_transfer.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Integrated spectral weights for the zero-phonon line and sidebands. The checker recomputes sideband percentages and verifies monotonic trends, ordering, crossing, and matches within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `tube_index`, `temperature_K`, `zpl_weight`, `higher_sideband_weight`, `lower_sideband_weight`
  - `description`: tube_index: one of '19,0','20,0','21,0'; temperature_K: float; other columns: float weights. Units are arbitrary but consistent across all rows.

Notes: The agent must compute the absorption coefficient α(ω) (not ωα(ω)) to obtain weights consistent with the crossing and ordering checks. The integrated weights should be extracted from a fixed energy window around each feature to ensure consistency across temperatures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spectral_weight_transfer.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tube_index",
          "temperature_K",
          "zpl_weight",
          "higher_sideband_weight",
          "lower_sideband_weight"
        ],
        "description": "tube_index: one of '19,0','20,0','21,0'; temperature_K: float; other columns: float weights. Units are arbitrary but consistent across all rows."
      },
      "description": "Integrated spectral weights for the zero-phonon line and sidebands. The checker recomputes sideband percentages and verifies monotonic trends, ordering, crossing, and matches within tolerance."
    }
  ],
  "notes": "The agent must compute the absorption coefficient α(ω) (not ωα(ω)) to obtain weights consistent with the crossing and ordering checks. The integrated weights should be extracted from a fixed energy window around each feature to ensure consistency across temperatures."
}
```

## How you are scored
A hidden verifier reads your CSV output and independently computes the relative sideband weights (sideband / zero‑phonon line). It inspects the temperature‑ and diameter‑dependent trends that the exciton‑phonon model predicts (monotonicity, ordering among the nanotubes, temperature threshold for the lower‑energy sideband, and the crossing behavior of the sideband intensities). It also compares your extracted weights against a reference dataset with appropriate tolerances. The combined score from all these checks, weighted by their importance, determines your final reward. Simply reporting the paper's numbers is not enough; the result must arise from the computational workflow described in the steps.
