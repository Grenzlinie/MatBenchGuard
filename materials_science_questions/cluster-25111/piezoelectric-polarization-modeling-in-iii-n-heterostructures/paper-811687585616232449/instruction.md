# Corrected Valence-Band Offsets for InAlN/GaN Heterostructures via Polarization-Induced Band-Bending Correction

## Problem background
Valence-band offsets (ΔE_V) at InAlN/GaN heterostructures are a key parameter for designing high-frequency, high-power electronic devices. When measured by X-ray photoelectron spectroscopy (XPS), ultrathin InAlN layers can exhibit sharp band bending due to the strong polarization-induced electric field combined with surface Fermi-level pinning. This band bending causes apparent shifts and broadening of the core-level spectra, leading to erroneous ΔE_V if not corrected. The challenge is to accurately recover the true ΔE_V for In_{0.17}Al_{0.83}N/GaN, In_{0.25}Al_{0.75}N/GaN, and In_{0.30}Al_{0.70}N/GaN interfaces by implementing a numerical correction procedure that accounts for the band bending.

## Approach
The core idea is to model the band bending and its effect on XPS lineshapes. Assume a uniform internal electric field across the InAlN layer. Using the measured surface Fermi-level position as a boundary condition, solve Poisson’s equation to obtain the depth-dependent potential throughout the heterostructure. For each depth, construct a pseudo-Voigt lineshape for the Al 2p and Ga 3d core levels and integrate these spectra with an exponential escape-depth weighting that depends on the exit angle and the inelastic mean free path. This yields predicted apparent peak positions and full widths at half maximum (FWHM) at the three measured exit angles. Iteratively adjust the internal electric field in the InAlN layer until the modeled angle-dependent apparent energies and FWHM match the provided experimental data. Once the electric field is determined, subtract the modeled apparent increases from the measured core-level energies to obtain corrected values. Finally, compute ΔE_V using the standard relation with the given bulk core-level-to-VBM constants for each composition.

## Reproduction target
Reproduce the corrected valence-band offsets for the three InAlN/GaN interfaces. Use the provided experimental data file (containing apparent Al 2p energies, FWHM, ΔE_CL, IMFP values, bulk material constants, and surface Fermi-level positions) to implement the numerical correction procedure described above. Your implementation must output a CSV file, `/app/outputs/corrected_delta_EV.csv`, with two columns: In_molar_fraction (0.17, 0.25, 0.30) and delta_EV (the corrected offset in eV). The task is to produce these three numbers by computation, not by copying a reported result.

## Assets

- Experimental XPS data and material constants for InAlN/GaN correction
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Numerical correction of ΔE_V
- Role: scored (load-bearing)
- Action: Implement the numerical correction procedure: load the provided experimental data, assume a uniform internal electric field in the InAlN layer, solve Poisson's equation with the surface Fermi-level pinning to obtain the depth-dependent potential, model depth-local pseudo-Voigt Al 2p and Ga 3d spectra, numerically integrate with escape-depth weighting to predict apparent peak positions and FWHM at each exit angle, iteratively adjust the electric field to reproduce the measured angle-dependent apparent values, then subtract the modeled apparent increases to obtain corrected core-level energies, and compute ΔE_V via the standard relation using the given bulk constants. Output the corrected ΔE_V for each In molar fraction to corrected_delta_EV.csv.
- Output file: `/app/outputs/corrected_delta_EV.csv`
- Format: csv
- Contract: CSV with columns: In_molar_fraction (float), delta_EV (float). Three rows for molar fractions 0.17, 0.25, 0.30. delta_EV in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/corrected_delta_EV.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### corrected_delta_EV.csv
- path: `/app/outputs/corrected_delta_EV.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Corrected valence-band offsets for three InAlN/GaN interfaces.
- schema:
  - `type`: table
  - `required_columns`: `In_molar_fraction`, `delta_EV`
  - `units`:
    - `delta_EV`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "corrected_delta_EV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "In_molar_fraction",
          "delta_EV"
        ],
        "units": {
          "delta_EV": "eV"
        }
      },
      "description": "Corrected valence-band offsets for three InAlN/GaN interfaces."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/corrected_delta_EV.csv` and compare the reported ΔE_V for each In molar fraction against a hidden reference value. The final reward is the fraction of the three samples that lie within an appropriate hidden tolerance of the expected value. Simply reporting the paper's numbers without performing the correction procedure correctly will not earn credit; the verifier checks the values you produce.
