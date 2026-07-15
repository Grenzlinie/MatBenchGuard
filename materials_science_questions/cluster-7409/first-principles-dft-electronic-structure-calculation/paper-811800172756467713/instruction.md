# First-Principles Study of Optical Properties of Transition-Metal Doped Silicon Clusters

## Problem background
Transition-metal doped silicon clusters (MSi₁₂) exhibit tunable optical properties due to strong hybridization between 3d orbitals of the metal and the 3s,3p states of silicon. This task investigates the linear and nonlinear optical response of such clusters by computing dipole polarizabilities, second-order hyperpolarizabilities, and optical absorption spectra for a series of 3d metals using first-principles density functional theory (DFT) and time-dependent DFT. The goal is to determine how these properties vary with the dopant metal and to evaluate the role of the exchange-correlation functional.

## Approach
Employ spin‑unrestricted DFT with the B3LYP functional and the 6‑311+G(2d) basis set, using an open‑source code (NWChem or an equivalent). Work with five MSi₁₂ clusters (M = Sc, Ti, Fe, Cu, Zn) in hexagonal‑prism geometries that respect the symmetries and spin states indicated below. After full geometry optimizations and harmonic frequency checks, compute static dipole polarizabilities and second‑order hyperpolarizabilities via the finite‑field method with an external field of 0.002 a.u. For the FeSi₁₂ cluster, additionally run a TD‑DFT calculation to obtain the first 30 electronic excitation energies and oscillator strengths. The entire pipeline is self‑contained: the agent must construct initial geometries, perform all electronic‑structure steps, and produce the two scored CSV files described in the workflow below.

## Reproduction target
Compute the mean dipole polarizability ⟨α⟩, the polarizability anisotropy Δα, and the mean second‑order hyperpolarizability ⟨γ⟩ for the clusters ScSi₁₂, TiSi₁₂, FeSi₁₂, CuSi₁₂, and ZnSi₁₂ at the B3LYP/6‑311+G(2d) level and write the results to `/app/outputs/polarizability_results.csv`. For FeSi₁₂, simulate the optical absorption spectrum with TD‑DFT (same functional and basis) and write the excitation index, wavelength (nm), and oscillator strength for the first 30 excitations to `/app/outputs/absorption_spectrum.csv`. The outputs must follow the column schemes and units specified in the output contract. A hidden verifier will later check that the computed properties capture the expected metal‑dependence and that the major absorption bands appear in the correct spectral region and order.

## Assets

- NWChem: https://github.com/nwchemgit/nwchem

## Workflow steps

### Step 1: Geometry optimization of MSi12 clusters
- Role: process
- Action: Construct initial hexagonal-prism (HP) structures for MSi12 (M=Sc, Ti, Fe, Cu, Zn) with the symmetries and spin states described: Sc (encapsulated HP, ^4A state), Ti (distorted HP with C_s symmetry, ^1A' state), Fe (D_{3d} HP, ^1A_{1g} state), Cu (regular C_{2h} HP, ^2A_g state), Zn (D_{3d} HP, ^1A_{1g} state). Perform spin-unrestricted B3LYP/6-311+G(2d) geometry optimizations followed by harmonic frequency calculations to confirm each structure is a local minimum. Produce the optimized coordinates for each cluster.
- Evidence: `/app/outputs/optimized_geometries.log`

### Step 2: Finite-field (hyper)polarizability computation
- Role: scored
- Action: Using the optimized geometries from s1, perform static finite-field calculations at B3LYP/6-311+G(2d) with an external electric field of 0.002 a.u. Compute the mean dipole polarizability ⟨α⟩, polarizability anisotropy Δα, and mean second-order hyperpolarizability ⟨γ⟩ for each of the five clusters (Sc, Ti, Fe, Cu, Zn) using the Cartesian components and the formulas given in the literature. Write the results into a CSV file.
- Output file: `/app/outputs/polarizability_results.csv`
- Format: csv
- Contract: CSV with columns: cluster (string), method (string, always 'B3LYP'), basis (string, always '6-311+G(2d)'), mean_polarizability (float, a.u.), polarizability_anisotropy (float, a.u.), mean_hyperpolarizability (float, 10^3 a.u.).
- Scoring: scored by hidden verifier

### Step 3: TD-DFT absorption spectrum of FeSi12
- Role: scored (load-bearing)
- Action: For the FeSi12 cluster, run a TD-DFT calculation at B3LYP/6-311+G(2d) to obtain the first 30 electronic excitation energies (nm) and oscillator strengths. Write the excitation index, wavelength, and oscillator strength to a CSV file.
- Output file: `/app/outputs/absorption_spectrum.csv`
- Format: csv
- Contract: CSV with columns: excitation_index (int), wavelength_nm (float), oscillator_strength (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polarizability_results.csv`
- `/app/outputs/absorption_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polarizability_results.csv
- path: `/app/outputs/polarizability_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean dipole polarizability, polarizability anisotropy, and mean second-order hyperpolarizability for MSi12 clusters (M=Sc, Ti, Fe, Cu, Zn) at B3LYP/6-311+G(2d).
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `method`, `basis`, `mean_polarizability`, `polarizability_anisotropy`, `mean_hyperpolarizability`
  - `units`:
    - `mean_polarizability`: a.u.
    - `polarizability_anisotropy`: a.u.
    - `mean_hyperpolarizability`: 10^3 a.u.

### absorption_spectrum.csv
- path: `/app/outputs/absorption_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: TD-DFT electronic excitation list for FeSi12 (B3LYP/6-311+G(2d)) containing the first 30 excitations; from this the checker recomputes the four major absorption bands and their ordering.
- schema:
  - `type`: table
  - `required_columns`: `excitation_index`, `wavelength_nm`, `oscillator_strength`

Notes: The agent is required to re-run the complete DFT pipeline (geometry optimizations, finite-field calculations, TD-DFT) and output the above artifacts. Only the B3LYP/6-311+G(2d) level is required for the scored outputs. The scoring uses paper-reported results as hidden reference for polarizabilities, and recomputes absorption bands from the raw excitation list for FeSi12.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polarizability_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "method",
          "basis",
          "mean_polarizability",
          "polarizability_anisotropy",
          "mean_hyperpolarizability"
        ],
        "units": {
          "mean_polarizability": "a.u.",
          "polarizability_anisotropy": "a.u.",
          "mean_hyperpolarizability": "10^3 a.u."
        }
      },
      "description": "Mean dipole polarizability, polarizability anisotropy, and mean second-order hyperpolarizability for MSi12 clusters (M=Sc, Ti, Fe, Cu, Zn) at B3LYP/6-311+G(2d)."
    },
    {
      "file": "absorption_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "excitation_index",
          "wavelength_nm",
          "oscillator_strength"
        ]
      },
      "description": "TD-DFT electronic excitation list for FeSi12 (B3LYP/6-311+G(2d)) containing the first 30 excitations; from this the checker recomputes the four major absorption bands and their ordering."
    }
  ],
  "notes": "The agent is required to re-run the complete DFT pipeline (geometry optimizations, finite-field calculations, TD-DFT) and output the above artifacts. Only the B3LYP/6-311+G(2d) level is required for the scored outputs. The scoring uses paper-reported results as hidden reference for polarizabilities, and recomputes absorption bands from the raw excitation list for FeSi12."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that examines the two scored artifacts (`polarizability_results.csv` and `absorption_spectrum.csv`). Each artifact contributes to the final reward according to its weight. The verifier compares your computed polarizabilities and hyperpolarizabilities against hidden reference criteria that capture the expected trends and magnitudes without penalising improvements over the original study. For the absorption spectrum, the verifier reconstructs the major absorption bands from your raw excitation list and checks that the band positions and their ordering agree with the expected pattern. You must genuinely run the DFT pipeline; the verifier may cross‑check consistency between the geometry optimisations and the scored properties. Do not embed hard‑coded numbers from external sources — the scoring is based on the results of your own calculations.
