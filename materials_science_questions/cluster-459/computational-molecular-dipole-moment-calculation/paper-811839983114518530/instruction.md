# Optical Absorption Spectra of Silver Nanoclusters via Atomistic Electrodynamics Model

## Problem background
Silver nanoclusters in the size range 1–5 nm exhibit strong, size- and shape-dependent optical absorption due to localized surface plasmons. Classical electrodynamics methods that rely on bulk dielectric functions fail for particles below ~10 nm because they lack atomic-scale structural detail, while full time-dependent density functional theory (TDDFT) calculations are computationally prohibitive for intermediate cluster sizes. An atomistic electrodynamics model that assigns each atom a frequency-dependent capacitance and polarizability can bridge this gap, providing a physically motivated description of the optical response that connects first‑principles theory with classical electrodynamics.

## Approach
The model used in this work is the Frequency-Dependent Capacitance–Polarizability Interaction Model (FD-CPIM). It treats a silver nanocluster as a collection of interacting atoms, each characterized by a static capacitance and a static polarizability whose frequency dispersion is described by Lorentzian oscillators. The total energy includes charge–charge, dipole–dipole, and charge–dipole interactions, with Gaussian‑damped interaction tensors to prevent divergences at short distances. Minimizing the total energy with respect to the induced atomic charges, induced atomic dipoles, and a Lagrange multiplier that enforces the total cluster charge leads to a complex linear system of size (4N+1)×(4N+1) that is solved at each photon energy of interest. From the solution one obtains the complex molecular polarizability tensor; the isotropic average of its imaginary part yields the absorption cross section per atom σ(ω)/N. The static and dynamic atomic parameters have been determined from TDDFT reference data for small silver clusters and are provided in the workflow steps. The model is applied to five quasi-spherical structural motifs: icosahedral, Ino decahedral, Marks decahedral, regular truncated octahedral, and cuboctahedral clusters, constructed from silver atoms with a fixed bond length and magic‑number formulas. No further training or parameter optimization is required—the task is to implement the model solver, apply it across a range of cluster sizes and photon energies, and extract the resulting plasmon resonance properties.

## Reproduction target
Build silver clusters for all five structural motifs (icosahedral, Ino decahedral, Marks decahedral, truncated octahedral, cuboctahedral) spanning a size range from approximately Ag₅₅ to Ag₄₀₀₀. Using the FD-CPIM model with the provided static and dynamic atomic parameters, compute the normalized absorption cross section per atom σ(ω)/N at a sequence of photon energies covering 2.4–4.8 eV for every cluster, and write the spectra to `/app/outputs/absorption_spectra.csv`. From each spectrum identify the main absorption peak: record its energy as the plasmon frequency and measure the full width at half maximum (FWHM) of that peak. Output these extracted quantities to `/app/outputs/plasmon_summary.csv`. Both CSV files must follow the column schemas described in the Workflow steps.

## Assets

- NumPy: https://numpy.org/
- SciPy: https://scipy.org/

## Workflow steps

### Step 1: Construct cluster geometries
- Role: process
- Action: Generate atomic coordinates for silver clusters of the five structural motifs (icosahedral, Ino decahedral, Marks decahedral, truncated octahedral, cuboctahedral) using the published magic-number formulas and the Ag–Ag bond length of 2.889 Å. Cover a representative size range for each motif (e.g., approximately Ag<sub>55</sub> to Ag<sub>4000</sub>). Record the generated cluster labels and atom counts in a log file.
- Evidence: `/app/outputs/geometries.log`

### Step 2: Compute normalized absorption spectra
- Role: scored (load-bearing)
- Action: Implement the frequency-dependent capacitance-polarizability interaction model (FD-CPIM). Use the published atomic parameters: static atomic polarizability α_s = 49.9843 au, static capacitance c_s = 3.4502 au, Lorentzian oscillator frequencies ω_i1 = 0.0747 au, ω_i2 = 0.0545 au, widths γ_i1 = 0.0604 au, γ_i2 = 0.0261 au, and size-correction A = 2.7759 au. For each cluster generated in Step 1, assemble the (4N+1)×(4N+1) complex relay matrix (using Gaussian-damped interaction tensors to avoid divergences) for a sequence of photon energies ranging from 2.4 eV to 4.8 eV. Solve for the induced charges and dipoles, compute the complex molecular polarizability tensor and its isotropic average, and then the normalized absorption cross section per atom σ(ω)/N = (4πω/c) Im[ꕯ(ω)]. Write the results for every cluster and frequency to a single CSV file.
- Output file: `/app/outputs/absorption_spectra.csv`
- Format: csv
- Contract: Columns: motif (string), cluster_label (string), energy_eV (float), sigma_per_atom (float).
- Scoring: scored by hidden verifier

### Step 3: Extract plasmon frequencies and widths
- Role: scored
- Action: From the computed spectra in absorption_spectra.csv, identify the main absorption peak for each cluster. Record the peak energy as the plasmon frequency and measure the full width at half maximum (FWHM) of that peak. Output a summary table with one row per cluster.
- Output file: `/app/outputs/plasmon_summary.csv`
- Format: csv
- Contract: Columns: motif (string), cluster_label (string), plasmon_freq_eV (float), FWHM_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_spectra.csv`
- `/app/outputs/plasmon_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_spectra.csv
- path: `/app/outputs/absorption_spectra.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw simulated absorption spectra; the checker will verify structural plausibility (e.g., peak location near expected plasmon energies).
- schema:
  - `type`: table
  - `required_columns`: `motif`, `cluster_label`, `energy_eV`, `sigma_per_atom`
  - `columns`:
    - `motif`: string
    - `cluster_label`: string
    - `energy_eV`: number
    - `sigma_per_atom`: number
  - `description`: Each row gives the normalized absorption cross section per atom for a specific cluster and photon energy.

### plasmon_summary.csv
- path: `/app/outputs/plasmon_summary.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Extracted plasmon properties; the checker compares plasmon_freq_eV and FWHM_eV against published reference values with tolerances (±0.15 eV for frequency, ±0.2 eV for width).
- schema:
  - `type`: table
  - `required_columns`: `motif`, `cluster_label`, `plasmon_freq_eV`, `FWHM_eV`
  - `columns`:
    - `motif`: string
    - `cluster_label`: string
    - `plasmon_freq_eV`: number
    - `FWHM_eV`: number
  - `description`: Each row contains the plasmon resonance frequency and full width at half maximum for one cluster.

Notes: The checker uses the plasmon_summary.csv as the primary scored artifact, comparing frequencies and widths to paper-reported values using a threshold-or-better policy. The absorption_spectra.csv is audited for structural consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "motif",
          "cluster_label",
          "energy_eV",
          "sigma_per_atom"
        ],
        "columns": {
          "motif": "string",
          "cluster_label": "string",
          "energy_eV": "number",
          "sigma_per_atom": "number"
        },
        "description": "Each row gives the normalized absorption cross section per atom for a specific cluster and photon energy."
      },
      "description": "Raw simulated absorption spectra; the checker will verify structural plausibility (e.g., peak location near expected plasmon energies)."
    },
    {
      "file": "plasmon_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "motif",
          "cluster_label",
          "plasmon_freq_eV",
          "FWHM_eV"
        ],
        "columns": {
          "motif": "string",
          "cluster_label": "string",
          "plasmon_freq_eV": "number",
          "FWHM_eV": "number"
        },
        "description": "Each row contains the plasmon resonance frequency and full width at half maximum for one cluster."
      },
      "description": "Extracted plasmon properties; the checker compares plasmon_freq_eV and FWHM_eV against published reference values with tolerances (±0.15 eV for frequency, ±0.2 eV for width)."
    }
  ],
  "notes": "The checker uses the plasmon_summary.csv as the primary scored artifact, comparing frequencies and widths to paper-reported values using a threshold-or-better policy. The absorption_spectra.csv is audited for structural consistency."
}
```

## How you are scored
A hidden verifier will independently evaluate your two scored artifacts. The primary reward comes from the plasmon_summary.csv: the verifier compares your extracted plasmon frequencies and peak widths for each cluster against reference values derived from high‑accuracy electronic‑structure calculations. It uses a threshold‑based policy—you do not need to hit exact numbers, but your values must lie within a physically justified margin of the reference. As a secondary check, the verifier performs a structural audit of the absorption_spectra.csv to ensure the spectra are plausible (e.g., the main peak is located in the expected energy region). The final score is a weighted combination of these evaluations; the plasmon summary carries the largest weight. Simply reporting the paper’s numbers without performing the computation will not pass the structural audit and will not receive full credit.
