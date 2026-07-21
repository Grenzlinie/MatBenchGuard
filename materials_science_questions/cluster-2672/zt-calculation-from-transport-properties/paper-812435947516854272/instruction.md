# Thermoelectric figure of merit and band gap in Bi nanowires from quantum confinement model

## Problem background
Bulk bismuth is a semimetal with overlapping electron and hole bands, which limits its thermoelectric figure of merit because the Seebeck coefficients of electrons and holes nearly cancel. When bismuth is formed into nanowires with diameters small enough that quantum confinement becomes significant, the electron and hole subband energies shift and a band gap can open, turning the material into a semiconductor. This confinement-induced semimetal-to-semiconductor transition offers a route to high thermoelectric performance. The present task reproduces the theoretical model that predicts how the effective band gap and the thermoelectric figure of merit depend on wire diameter and crystallographic orientation.

## Approach
The nanowire is modeled as a quasi-one-dimensional electron gas confined inside an infinitely deep cylindrical potential well. The subband energies are obtained from the bulk bismuth effective mass tensors by quantizing the transverse motion: the energy of a subband with quantum numbers i, j is given by the sum of the free-electron kinetic energy along the wire axis and the transverse confinement energy, which depends on the roots of the Bessel functions J_i, the dynamic effective mass in the plane perpendicular to the wire, and the wire radius. The effective band gap is computed as the energy difference between the lowest electron subband and the highest hole subband, taking into account the bulk band overlap of 38 meV. For the thermoelectric figure of merit ZT, a semiclassical transport model is used. The electrical conductivity, Seebeck coefficient, and electronic thermal conductivity are calculated from the subband structure and the carrier distribution. Lattice thermal conductivity is approximated with a suitable phonon transport model. The carrier concentration is optimized to maximize ZT. The model is applied to three primary crystal directions (binary, trigonal, bisectrix) and, for ZT, to n-type doping along the trigonal axis at 300 K.

## Model parameters
The following numerical values are used as fixed constants:
- Band overlap between conduction and valence bands: Δ = 38 meV.
- Electron effective masses (lowest subband) for each wire orientation:
  - Binary: wire-axis mass m_e∥ = 0.00113 m0, in-plane dynamic mass m_e⊥ = 0.034 m0
  - Trigonal: m_e∥ = 0.00443 m0, m_e⊥ = 0.017 m0
  - Bisectrix: m_e∥ = 0.26 m0, m_e⊥ = 0.0038 m0
- Hole effective mass: isotropic, m_h = 0.06 m0 (both wire-axis and in-plane).
- Use infinite cylindrical well with first root of J0: χ = 2.4048.

## Reproduction target
Produce two scored CSV files:
1. The effective band gap (in meV) between the lowest electron and highest hole subbands as a function of wire diameter (in nm) for the binary, trigonal, and bisectrix orientations. The file should cover diameters from at least 10 nm to 200 nm.
2. The thermoelectric figure of merit ZT for n-type Bi nanowires oriented along the trigonal axis at 300 K with optimal carrier concentration, as a function of wire diameter (in nm). The file should cover diameters from at least 20 nm to 200 nm.
The required column schemas are detailed in the workflow steps and output contract.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute 1D subband energies
- Role: process
- Action: Compute electron and hole subband edge energies for Bi nanowires as functions of wire diameter and crystallographic orientation using the infinite cylindrical potential well approximation and bulk Bi effective mass tensors (electron masses along wire axis and in-plane, hole mass). Include the bulk band overlap of 38 meV.
- Evidence: `/app/outputs/subband_energies.npz`

### Step 2: Determine band gap vs wire diameter
- Role: scored (load-bearing)
- Action: From the subband energies, determine the effective band gap (energy difference between lowest electron subband and highest hole subband) for the binary, trigonal, and bisectrix orientations. Report the gap as a function of wire diameter.
- Output file: `/app/outputs/band_gap_vs_diameter.csv`
- Format: csv
- Contract: diameter_nm: numeric (nm); binary_gap_meV: numeric (meV); trigonal_gap_meV: numeric (meV); bisectrix_gap_meV: numeric (meV). Positive values indicate a semiconductor-like gap.
- Scoring: scored by hidden verifier

### Step 3: Compute ZT vs wire diameter
- Role: scored
- Action: Using the subband structure and a semiclassical transport model, compute the thermoelectric figure of merit ZT for n-type Bi nanowires oriented along the trigonal axis at 300 K with optimal carrier concentration. Report ZT as a function of wire diameter.
- Output file: `/app/outputs/ZT_vs_diameter.csv`
- Format: csv
- Contract: diameter_nm: numeric (nm); ZT: numeric (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_vs_diameter.csv`
- `/app/outputs/ZT_vs_diameter.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_vs_diameter.csv
- path: `/app/outputs/band_gap_vs_diameter.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective band gap between the lowest electron and highest hole subbands for the three primary crystal directions as a function of wire diameter.
- schema:
  - `type`: table
  - `required_columns`: `diameter_nm`, `binary_gap_meV`, `trigonal_gap_meV`, `bisectrix_gap_meV`
  - `units`:
    - `diameter_nm`: nm
    - `binary_gap_meV`: meV
    - `trigonal_gap_meV`: meV
    - `bisectrix_gap_meV`: meV

### ZT_vs_diameter.csv
- path: `/app/outputs/ZT_vs_diameter.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Figure of merit ZT for n‑type Bi nanowires oriented along the trigonal axis at 300 K with optimal carrier concentration, as a function of wire diameter.
- schema:
  - `type`: table
  - `required_columns`: `diameter_nm`, `ZT`
  - `units`:
    - `diameter_nm`: nm
    - `ZT`: dimensionless

Notes: The hidden checker compares the computed band gap curves and ZT values to the reference results from the paper using tolerances and monotonicity checks. The agent is required to implement the full 1D quantum confinement model, not merely report numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_vs_diameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diameter_nm",
          "binary_gap_meV",
          "trigonal_gap_meV",
          "bisectrix_gap_meV"
        ],
        "units": {
          "diameter_nm": "nm",
          "binary_gap_meV": "meV",
          "trigonal_gap_meV": "meV",
          "bisectrix_gap_meV": "meV"
        }
      },
      "description": "Effective band gap between the lowest electron and highest hole subbands for the three primary crystal directions as a function of wire diameter."
    },
    {
      "file": "ZT_vs_diameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diameter_nm",
          "ZT"
        ],
        "units": {
          "diameter_nm": "nm",
          "ZT": "dimensionless"
        }
      },
      "description": "Figure of merit ZT for n‑type Bi nanowires oriented along the trigonal axis at 300 K with optimal carrier concentration, as a function of wire diameter."
    }
  ],
  "notes": "The hidden checker compares the computed band gap curves and ZT values to the reference results from the paper using tolerances and monotonicity checks. The agent is required to implement the full 1D quantum confinement model, not merely report numbers."
}
```

## How you are scored
A hidden verifier will independently read the submitted CSV files and compare them to reference data. For the band gap file, it will verify that the gap crosses zero (indicating a semimetal-to-semiconductor transition) at wire diameters consistent with the theoretical framework, and that the gap increases monotonically as diameter decreases below the transition point. For the ZT file, it will check that ZT increases monotonically as diameter decreases below the transition diameter and will compare ZT values at several selected diameters against hidden reference numbers. Each artifact carries a share of the total reward; the final score is a weighted combination. The tolerances used by the verifier are not disclosed, so simply reporting the paper’s numbers without running the full quantum confinement and transport calculation will not succeed.
