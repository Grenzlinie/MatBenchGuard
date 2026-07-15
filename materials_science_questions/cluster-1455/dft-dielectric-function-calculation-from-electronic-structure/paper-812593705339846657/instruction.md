# DFT optical spectra and dielectric properties of layered tin diiodide

## Problem background
SnI₂ is a layered luminescent semiconductor used in discharge lamps and photorecording. Despite several experimental studies, there is controversy about the nature of its fundamental band gap — whether it is direct or indirect — and about which particular tin atoms are responsible for the lowest-energy optical transition. First-principles calculations of the electronic structure and optical properties can provide a definitive answer by computing the band structure, the dielectric function, reflectivity, and absorption spectra. This task reproduces such a calculation.

## Approach
We use all-electron density-functional theory (DFT) with the local-density approximation (LDA) in the von Barth–Hedin parametrisation. Spin–orbit coupling (SOC) is included fully self-consistently to account for the heavy elements Sn and I. The ground-state calculation for monoclinic SnI₂ is performed with the linearised augmented-plane-wave (LAPW) method, which makes no shape approximation for the potential or charge density. From the converged Kohn–Sham eigenvalues and wavefunctions, the imaginary part of the dielectric tensor ε₂(ω) is computed in the electric-dipole approximation for the three principal polarisations (xx, yy, zz). Lifetime broadening (a Lorentzian with FWHM = 0.005(ℏω)² eV) and a Gaussian broadening (FWHM = 0.01 eV) are applied to mimic experimental resolution. The real part ε₁(ω) is obtained via the Kramers–Kronig relation up to 41 eV. From the complex dielectric function, the reflectivity, absorption coefficient (cm⁻¹), and electron energy-loss function are derived for each polarisation. The band structure and site- and orbital-projected densities of states are used to determine the band-gap type and to identify the atomic character of the first prominent peak in ε₂(ω).

## Reproduction target
Produce a single JSON file, `reproduction_results.json`, containing all computed optical spectra and derived quantities. The file must include: the imaginary and real parts of the dielectric tensor for xx, yy, and zz polarisations (energy vs value arrays); the reflectivity, absorption coefficient, and energy-loss function for each polarisation (energy vs value arrays); the band-gap type (direct or indirect) and its numerical value in eV; the static dielectric constants ε_{xx}(0), ε_{yy}(0), ε_{zz}(0) and their average; and the energy (eV) of the first prominent peak in ε₂(ω) together with a string describing its microscopic assignment (e.g., which atomic orbitals and sites dominate the transition). All energies are in eV; dielectric constants and reflectivity are dimensionless; absorption is in cm⁻¹; EELS is in arbitrary units. The JSON schema is given in the output contract below. The workflow steps describe how to generate these results; the final artifact must be placed at `/app/outputs/reproduction_results.json`.

## Assets

- Elk all-electron full-potential linearised augmented-plane-wave (FP-LAPW) code: https://github.com/dft-code/Elk
- Monoclinic SnI₂ crystal structure parameters

## Workflow steps

### Step 1: DFT ground-state calculation with spin-orbit coupling
- Role: process
- Action: Run a self-consistent field (SCF) calculation for monoclinic SnI₂ using the Elk FP-LAPW code with the von Barth‑Hedin LDA exchange‑correlation functional and full spin‑orbit coupling enabled. Use the experimental crystal structure (Table I lattice parameters and atomic positions). Converge the total energy to 1e-6 Ry. This step produces the Kohn–Sham eigenvalues, wavefunctions, self‑consistent potential, and electron density required for the subsequent optical calculation.
- Evidence: `/app/outputs/elk.log`

### Step 2: Optical spectra computation and property extraction
- Role: scored (load-bearing)
- Action: From the converged ground‑state data, compute the imaginary part of the dielectric tensor ε₂(ω) for xx, yy, and zz polarisations via the electric‑dipole approximation using Kohn–Sham eigenvalues and momentum matrix elements. Apply a lifetime broadening Lorentzian (FWHM = 0.005(ℏω)² eV) and a Gaussian smoothing (FWHM = 0.01 eV). Calculate the real part ε₁(ω) through the Kramers‑Kronig relation up to 41 eV. Derive polarised reflectivity, absorption coefficient, and electron energy‑loss function (EELS) for each direction. Determine the static dielectric constants ε_{xx}(0), ε_{yy}(0), ε_{zz}(0) and their average. Determine the fundamental band‑gap type (indirect) and its value (eV) from the band structure. Identify the first prominent peak (peak A) in ε₂(ω) and assign its microscopic origin using orbital‑projected density of states or band character analysis. Package all results into the structured JSON file reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: JSON object. Top‑level keys: band_gap_type (string), band_gap_value (float, eV), static_dielectric_constants (object with fields xx, yy, zz, average), first_peak_energy (float, eV), first_peak_assignment (string). Spectrum arrays (each a list of [energy (eV), value] pairs): epsilon2_xx, epsilon2_yy, epsilon2_zz, epsilon1_xx, epsilon1_yy, epsilon1_zz, reflectivity_xx, reflectivity_yy, reflectivity_zz, absorption_xx, absorption_yy, absorption_zz (absorption coefficient in cm⁻¹), eels_xx, eels_yy, eels_zz (arbitrary units). Dielectric constants and reflectivity dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Full set of computed optical spectra and derived scalar quantities; the checker verifies band‑gap type/nature, numerical values of gap, static dielectric constants, first‑peak energy and assignment, spectral shape features (peak locations, minima, absorption edge, anisotropy), and cross‑consistency between arrays.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_type`: string
    - `band_gap_value`: number (eV)
    - `static_dielectric_constants`: object with fields xx, yy, zz, average (number, dimensionless)
    - `first_peak_energy`: number (eV)
    - `first_peak_assignment`: string
    - `epsilon2_xx`: list of [energy (eV), value] pairs
    - `epsilon2_yy`: list of [energy (eV), value] pairs
    - `epsilon2_zz`: list of [energy (eV), value] pairs
    - `epsilon1_xx`: list of [energy (eV), value] pairs
    - `epsilon1_yy`: list of [energy (eV), value] pairs
    - `epsilon1_zz`: list of [energy (eV), value] pairs
    - `reflectivity_xx`: list of [energy (eV), value] pairs (dimensionless)
    - `reflectivity_yy`: list of [energy (eV), value] pairs
    - `reflectivity_zz`: list of [energy (eV), value] pairs
    - `absorption_xx`: list of [energy (eV), value] pairs (cm⁻¹)
    - `absorption_yy`: list of [energy (eV), value] pairs
    - `absorption_zz`: list of [energy (eV), value] pairs
    - `eels_xx`: list of [energy (eV), value] pairs (arbitrary units)
    - `eels_yy`: list of [energy (eV), value] pairs
    - `eels_zz`: list of [energy (eV), value] pairs
  - `items`: object

Notes: All spectra and derived quantities must be obtained from the DFT+SOC ground‑state calculation of step 1 using the provided crystal structure. The hidden checker compares against paper‑reported reference values with domain‑appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_type": "string",
          "band_gap_value": "number (eV)",
          "static_dielectric_constants": "object with fields xx, yy, zz, average (number, dimensionless)",
          "first_peak_energy": "number (eV)",
          "first_peak_assignment": "string",
          "epsilon2_xx": "list of [energy (eV), value] pairs",
          "epsilon2_yy": "list of [energy (eV), value] pairs",
          "epsilon2_zz": "list of [energy (eV), value] pairs",
          "epsilon1_xx": "list of [energy (eV), value] pairs",
          "epsilon1_yy": "list of [energy (eV), value] pairs",
          "epsilon1_zz": "list of [energy (eV), value] pairs",
          "reflectivity_xx": "list of [energy (eV), value] pairs (dimensionless)",
          "reflectivity_yy": "list of [energy (eV), value] pairs",
          "reflectivity_zz": "list of [energy (eV), value] pairs",
          "absorption_xx": "list of [energy (eV), value] pairs (cm⁻¹)",
          "absorption_yy": "list of [energy (eV), value] pairs",
          "absorption_zz": "list of [energy (eV), value] pairs",
          "eels_xx": "list of [energy (eV), value] pairs (arbitrary units)",
          "eels_yy": "list of [energy (eV), value] pairs",
          "eels_zz": "list of [energy (eV), value] pairs"
        },
        "items": {}
      },
      "description": "Full set of computed optical spectra and derived scalar quantities; the checker verifies band‑gap type/nature, numerical values of gap, static dielectric constants, first‑peak energy and assignment, spectral shape features (peak locations, minima, absorption edge, anisotropy), and cross‑consistency between arrays."
    }
  ],
  "notes": "All spectra and derived quantities must be obtained from the DFT+SOC ground‑state calculation of step 1 using the provided crystal structure. The hidden checker compares against paper‑reported reference values with domain‑appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that loads `reproduction_results.json`. The verifier first checks that the file has the correct structure and required fields. Then it scores several aspects: (i) it verifies the presence of key spectral features (e.g., a local maximum in ε₂ in a specified energy window, a minimum in reflectivity, and a sharp rise in absorption at the expected edge energy); (ii) it compares your reported derived quantities (band-gap type and value, static dielectric constants, first-peak energy, peak assignment) against reference values obtained from the theoretical literature with tolerances that account for differences between DFT implementations; (iii) it checks the anisotropy of the static dielectric constants. The contributions from these checks are weighted and combined into a single score between 0 and 1. Meeting all the criteria earns a perfect score; structural shape checks carry less weight than numerical accuracy. The scoring details and tolerances are not disclosed; only the final reward is reported.
