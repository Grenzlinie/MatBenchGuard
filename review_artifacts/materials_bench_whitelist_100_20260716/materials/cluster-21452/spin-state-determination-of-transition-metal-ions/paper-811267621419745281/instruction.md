# Ligand Field Multiplet Calculation of Co K Pre-edge Spectra for Four Symmetries

## Problem background
Transition metal ions in crystalline materials exhibit characteristic X-ray absorption near-edge structure (XANES) at the K edge, including pre-edge features that are sensitive to the local site symmetry. For Co²⁺, the intensity and shape of the K pre-edge arise from electric quadrupole (1s → 3d) transitions, and in non-centrosymmetric geometries, electric dipole transitions (1s → 4p) are allowed through p-d hybridization. Ligand Field Multiplet (LFM) theory can model both contributions and quantify the fraction of electric dipole intensity, providing a spectroscopic fingerprint of the local coordination environment. This task focuses on computing the Co K pre-edge spectra for four idealized Co²⁺ site symmetries (O_h, C_4v, D_3h, T_d) using LFM calculations, and extracting from them the electric dipole contribution fraction and ground state symmetry, which serve as signatures of the local geometry.

## Approach
The core method is Ligand Field Multiplet (LFM) theory implemented in the Quanty code. For each symmetry, the Co²⁺ ion is modeled as an isolated ion with crystal-field and p-d hybridization Hamiltonians. The calculation includes all 3d-3d and 1s-3d Coulomb interactions, spin-orbit coupling on the open shells, and the mixing between the 3d⁷4p⁰ and 3d⁶4p¹ configurations that gives rise to electric dipole intensity. Slater integrals are reduced by a factor β=0.6, spin-orbit coupling is set to 80% of the free-ion value, and the average energy difference between the 3d and 4p configurations is Δ=13.5 eV. The crystal-field and hybridization parameters for each symmetry are given below:

- O_h: Dq = 0.11 eV (crystal field only; no hybridization).
- C_4v: Dq = 0.148 eV, Ds = -0.087 eV, Dt = 0.055 eV; hybridization parameters V_{p-d}(a₁) = 0.25 eV, V_{p-d}(e) = 0.84 eV.
- D_3h: Dμ = 0.0 eV, Dν = -0.096 eV; hybridization parameter V_{p-d} = 5.5 eV.
- T_d: Dq = -0.055 eV; hybridization parameter V_{p-d} = 8.5 eV.

The free-ion Slater integrals are F²_{3d3d} = 11.60483 eV, F⁴_{3d3d} = 7.20942 eV, and the spin-orbit coupling ζ_{3d} = 0.066 eV. With the reduction factor β=0.6, the effective Slater integrals become F²_{3d3d} = 6.962898 eV, F⁴_{3d3d} = 4.325652 eV; the spin-orbit coupling is set to 80% of the free-ion value: 0.0528 eV. The pre-edge spectra are obtained by convolving the transition intensities with a Lorentzian (FWHM 1.33 eV, accounting for the 1s core-hole lifetime) and a Gaussian (FWHM 0.4 eV, for instrumental resolution), and normalized by the Co K-edge jump (3.0×10⁻⁴ Å²). Temperature is 300 K with Boltzmann population of initial state levels. For each symmetry, the computation yields an energy-resolved spectrum with separate total, electric dipole, and electric quadrupole contributions, from which the ground state symmetry and the dipole fraction can be derived.

## Reproduction target
The goal is to produce, for each of the four Co²⁺ site symmetries (O_h, C_4v, D_3h, T_d), the pre-edge spectrum in the energy region near the Co K edge (approx. 7700–7715 eV). For each symmetry, output the arrays of energy and corresponding total, electric dipole, and electric quadrupole intensities, and report the ground state symmetry label. The output must be saved as /app/outputs/pre_edge_spectra.json with the structure described in Step 1. From these spectra one can compute the fraction of electric dipole contribution to the total pre-edge integrated intensity for each symmetry, and determine the relative ordering of total pre-edge intensities across the four site symmetries. The automatic evaluation will check these derived quantities against reference values.

## Assets

- Quanty: http://www.quanty.org/

## Workflow steps

### Step 1: LFM calculation of Co K pre-edge spectra
- Role: scored (load-bearing)
- Action: Perform Ligand Field Multiplet calculations using Quanty for Co²⁺ in four site symmetries: O_h, C_4v, D_3h, T_d. Use the crystal-field and p-d hybridization parameters as listed in the Approach, Slater integrals reduced by β=0.6, spin-orbit coupling at 80% of free-ion value, Δ=13.5 eV, Lorentzian broadening FWHM 1.33 eV, Gaussian broadening FWHM 0.4 eV, temperature 300 K with Boltzmann population, and normalization by Co K-edge jump 3.0×10⁻⁴ Å². For each symmetry, compute the pre-edge spectrum covering the energy region ~7700–7715 eV, outputting separate total, electric dipole, and electric quadrupole intensities. Report the ground state symmetry.
- Output file: `/app/outputs/pre_edge_spectra.json`
- Format: json
- Contract: A JSON object with top-level keys "O_h", "C_4v", "D_3h", "T_d". Each value is an object containing: "energy" (array of floats, eV), "total_intensity" (array of floats), "dipole_intensity" (array of floats), "quadrupole_intensity" (array of floats), and "ground_state_symmetry" (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pre_edge_spectra.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pre_edge_spectra.json
- path: `/app/outputs/pre_edge_spectra.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw LFM pre-edge spectra with separate dipole and quadrupole components for the four symmetries. The checker will integrate the intensities to compute dipole contribution fractions, verify ground state symmetries, and confirm total intensity ordering.
- schema:
  - `type`: object
  - `required`:
    - `O_h`: object containing energy, total_intensity, dipole_intensity, quadrupole_intensity (arrays of floats) and ground_state_symmetry (string)
    - `C_4v`: same structure
    - `D_3h`: same structure
    - `T_d`: same structure

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pre_edge_spectra.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "O_h": "object containing energy, total_intensity, dipole_intensity, quadrupole_intensity (arrays of floats) and ground_state_symmetry (string)",
          "C_4v": "same structure",
          "D_3h": "same structure",
          "T_d": "same structure"
        }
      },
      "description": "Raw LFM pre-edge spectra with separate dipole and quadrupole components for the four symmetries. The checker will integrate the intensities to compute dipole contribution fractions, verify ground state symmetries, and confirm total intensity ordering."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your submitted pre_edge_spectra.json. For each symmetry, it will integrate the dipole and quadrupole intensity arrays over the pre-edge energy range to obtain the total dipole and total quadrupole contributions, then compute the electric dipole fraction. These fractions will be compared to the expected (hidden) values within a tolerance. The verifier will also check the reported ground state symmetry labels against the expected labels (exact match). Additionally, it will evaluate whether the total pre-edge intensity ordering (the sequence from weakest to strongest total intensity across symmetries) matches the expected relative pattern. Each check contributes a weight to the final reward score, which is the sum of weighted partial credits. You do not need to know the target values; the verifier performs the comparison automatically. To succeed, you must execute the LFM calculations accurately and produce the spectrum arrays and symmetry labels that, when re‑processed, yield dipole fractions and an intensity ordering that agree with the hidden reference.
