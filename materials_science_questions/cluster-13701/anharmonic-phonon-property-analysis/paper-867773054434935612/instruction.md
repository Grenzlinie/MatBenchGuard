# DFT optical and electron-phonon analysis of a layered charge-density-wave material

## Problem background
2H-NbSe₂ is a layered transition metal dichalcogenide that hosts both a charge density wave (CDW) and superconductivity at low temperatures. Understanding the ultrafast carrier and collective mode dynamics is crucial for disentangling the electronic and phononic processes underlying these broken-symmetry phases. Time-resolved pump-probe spectroscopy provides insight into the relaxation pathways after photoexcitation, and first-principles density functional theory (DFT) calculations allow identification of specific interband transitions responsible for the observed spectral signatures and of the electron-phonon coupling that controls thermalization. This task targets the computational component: reproducing the DFT-derived optical properties and the electron-phonon coupling to find the dominant phonon group involved in the electron-phonon relaxation. The results are quantitative electronic-structure descriptors that can be compared against the values established in the literature.

## Approach
The workflow consists of a ground-state DFT calculation for bulk 2H-NbSe₂ using the PBE exchange-correlation functional and optimized norm-conserving Vanderbilt (ONCV) pseudopotentials. From the electronic structure, the frequency-dependent dielectric function and the corresponding reflectivity are computed. A rigid 4% red-shift is applied to the energy axis to account for band-width renormalization effects. The three principal peaks in the shifted optical spectrum are extracted; these correspond to interband transitions that dominate the transient reflectivity response. Independently, the phonon dispersion is obtained via density-functional perturbation theory (DFPT), and the electron-phonon coupling is interpolated using Wannier functions with the EPW code. The isotropic Eliashberg spectral function α²F(ω) is then constructed. The maximum of α²F(ω) yields the energy of the phonon group that governs the electron-phonon relaxation time. All calculations rely on open-source codes and publicly available structural data.

## Reproduction target
Your goal is to perform the DFT and electron-phonon calculations described above and to extract two sets of quantitative results:
1. Optical spectrum: from the reflectivity or absorption spectrum, after applying a rigid 4% red-shift of the energy axis, identify the three most prominent peak energies (in eV). Write them to `/app/outputs/optical_peaks.json` in descending order.
2. Eliashberg spectral function: compute the isotropic α²F(ω) and locate the energy (in meV) at which it attains its global maximum. Write this value to `/app/outputs/eph_peak.json`. Both results will be compared against independent hidden reference values obtained from the original study.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- ONCV pseudopotentials (Nb, Se): http://www.quantum-simulation.org
- Wannier90: http://www.wannier.org
- EPW code: quantum-espresso
- 2H-NbSe₂ crystal structure

## Workflow steps

### Step 1: DFT ground-state and band structure calculation
- Role: process
- Action: Perform a self-consistent field (SCF) calculation for bulk 2H-NbSe₂ using Quantum ESPRESSO with the PBE functional and ONCV pseudopotentials. Follow with a non-SCF band structure calculation to obtain electronic eigenvalues, wavefunctions, and Fermi surface. These are needed for the subsequent optical and phonon calculations.
- Evidence: `/app/outputs/scf_output.log`

### Step 2: Optical absorption and reflectivity with energy scaling
- Role: scored (load-bearing)
- Action: Using the electronic structure from the previous step, compute the frequency-dependent dielectric function and reflectivity. Apply a rigid 4% red-shift to the energy axis. Extract the three most prominent peak positions (in eV) from the scaled optical spectrum.
- Output file: `/app/outputs/optical_peaks.json`
- Format: json
- Contract: {"scaled_peak_energies_eV": [number, number, number]} where the three numbers are the main peak energies in eV after the 4% red-shift, ordered from high to low energy.
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion and electron-phonon coupling
- Role: scored (load-bearing)
- Action: Perform phonon calculations using density-functional perturbation theory (DFPT) on the same ground-state charge density. Then use EPW in conjunction with Wannier90 to interpolate the electron-phonon coupling and compute the isotropic Eliashberg spectral function α²F(ω). Identify the energy (in meV) where α²F(ω) reaches its maximum.
- Output file: `/app/outputs/eph_peak.json`
- Format: json
- Contract: {"dominant_phonon_energy_meV": number} where the number is the energy in meV at which α²F(ω) is maximal.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_peaks.json`
- `/app/outputs/eph_peak.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_peaks.json
- path: `/app/outputs/optical_peaks.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Three main peak energies (eV) extracted from the calculated optical spectrum after a 4% rigid red-shift of the energy axis.
- schema:
  - `type`: object
  - `required`:
    - `scaled_peak_energies_eV`: array of three floats

### eph_peak.json
- path: `/app/outputs/eph_peak.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Energy (meV) at which the Eliashberg spectral function α²F(ω) is maximum, corresponding to the phonon group around 20 meV.
- schema:
  - `type`: object
  - `required`:
    - `dominant_phonon_energy_meV`: float

Notes: The hidden checker compares each submitted peak energy against the paper-reported values with a tolerance of ±0.05 eV, and checks that the submitted phonon energy lies within the hidden range 18–22 meV. The scoring policies are exact_match with allowed deviation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "scaled_peak_energies_eV": "array of three floats"
        }
      },
      "description": "Three main peak energies (eV) extracted from the calculated optical spectrum after a 4% rigid red-shift of the energy axis."
    },
    {
      "file": "eph_peak.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "dominant_phonon_energy_meV": "float"
        }
      },
      "description": "Energy (meV) at which the Eliashberg spectral function α²F(ω) is maximum, corresponding to the phonon group around 20 meV."
    }
  ],
  "notes": "The hidden checker compares each submitted peak energy against the paper-reported values with a tolerance of ±0.05 eV, and checks that the submitted phonon energy lies within the hidden range 18–22 meV. The scoring policies are exact_match with allowed deviation."
}
```

## How you are scored
A hidden verifier will read the two JSON output files. It will check that `optical_peaks.json` contains three energies within a tolerance of the expected peaks and that `eph_peak.json` contains a phonon energy that falls within an allowed range. Each scored artifact contributes to the final reward with a pre-defined weight. The verifier does not inspect intermediate logs nor does it grant credit for reporting numbers without having performed the required calculations; only the content and correctness of the submitted JSON artifacts are assessed.
