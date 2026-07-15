# Modeling Raman 2D Band Shift and Broadening in Wrinkled CVD Graphene

## Problem background
Monolayer graphene produced by chemical vapor deposition (CVD) and transferred onto a polymer substrate such as PET typically contains a network of flat, micron‑sized islands separated by out‑of‑plane wrinkles. Under tensile deformation, the wrinkles are thought to mechanically decouple the islands from each other, leading to non‑uniform strain distributions within each island as stress transfers from the substrate. A coupled mechanical–optical model has been developed to simulate the resulting Raman 2D band response under uniaxial strain, taking into account both the island‑scale strain distribution via shear‑lag theory and the intensity profile of the probing laser spot. Your task is to implement this model numerically.

## Approach
You will model a single graphene island as a circular disk of diameter ~1.2 µm, discretised into a grid of elementary units. For each elementary unit you will compute the local axial strain ε_r using a shear‑lag formulation adapted to a network of parallel graphene nanoribbons of varying length, where the stress‑transfer efficiency is parameterised by a single dimensionless quantity ns. The laser excitation is described as a Gaussian beam with a specified effective radius; its local intensity weights each unit’s contribution. The 2D Raman band contributed by each strained unit is modelled as a Lorentzian whose centre and width shift linearly with the local strain relative to known reference rates for ideal flat graphene. Summing these weighted Lorentzians across all units gives the total collected Raman spectrum for a given applied matrix strain. Fitting that total spectrum with a single Lorentzian yields the effective band centre ω₂D and width FWHM₂D that a spectrometer would report. Repeating the procedure for a range of matrix strains provides the strain‑dependent peak properties.

## Reproduction target
Implement the coupled model for a 1.2 µm diameter circular island with stress‑transfer parameter ns = 2 and a concentric Gaussian laser spot of effective radius r₀ = 0.7 µm. Use the following literature reference values for ideal flat monolayer graphene on a PET substrate: the strain‑free 2D FWHM is 27 cm⁻¹, the intrinsic Raman band shift rate (dω₂D/dε)ᵣₑ is −60 cm⁻¹ per % strain, and the intrinsic broadening rate (dFWHM₂D/dε)ᵣₑ is 12 cm⁻¹ per % strain. Compute the effective ω₂D and FWHM₂D for a set of applied matrix strains ε_m evenly spaced from 0 % to 0.4 % (inclusive), with at least five strain values. Output your results as a CSV file `/app/outputs/predicted_peak_properties.csv` containing the columns `strain_percent`, `omega_2D` (cm⁻¹), and `FWHM_2D` (cm⁻¹). Your results will be evaluated by extracting the slopes dω₂D/dε and dFWHM₂D/dε from this table and comparing them against hidden reference slopes computed from an independent correct implementation of the same model.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute spatial strain distribution within the graphene island
- Role: process
- Action: Discretize a 1.2 µm diameter circular island into a 12×12 grid of 0.1 µm square units. For each unit (L,T) compute the local axial strain ε_r(L,T) using shear-lag theory for nanoribbons, with stress-transfer parameter ns=2, applied matrix strain ε_m from 0% to 0.4% in at least 5 evenly spaced steps. Use the discrete adaptation where nanoribbon length and ns vary with transverse position T. Store strain maps for each ε_m.
- Evidence: `/app/outputs/strain_maps.npy`

### Step 2: Simulate total Raman 2D band spectrum and extract peak properties per strain
- Role: process
- Action: For each ε_m, build the total collected Raman 2D band by summing Lorentzian contributions from every unit, with unit centre = ε_r(L,T)·(dω₂D/dε)_ref and width = FWHM₂D + ε_r(L,T)·(dFWHM₂D/dε)_ref, using (dω₂D/dε)_ref = −60 cm⁻¹/%, (dFWHM₂D/dε)_ref = 12 cm⁻¹/%, FWHM₂D = 27 cm⁻¹. Weight each unit by a Gaussian laser intensity (r₀=0.7 µm). From the summed spectrum, fit a single Lorentzian to extract effective ω₂D and FWHM₂D.
- Evidence: `/app/outputs/fitted_peaks.npy`

### Step 3: Export predicted peak properties for scoring
- Role: scored (load-bearing)
- Action: Collect the extracted ω₂D and FWHM₂D for each strain into a CSV. Write to predicted_peak_properties.csv with columns: strain_percent (float), omega_2D (float, cm⁻¹), FWHM_2D (float, cm⁻¹). At least 5 rows covering evenly spaced strains from 0 to 0.4% (inclusive).
- Output file: `/app/outputs/predicted_peak_properties.csv`
- Format: csv
- Contract: Three columns: strain_percent (float), omega_2D (float, cm⁻¹), FWHM_2D (float, cm⁻¹). At least 5 evenly spaced strain values between 0 and 0.4 (inclusive).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_peak_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_peak_properties.csv
- path: `/app/outputs/predicted_peak_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV with model-predicted Raman 2D band peak position and width at varying applied matrix strains.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `omega_2D`, `FWHM_2D`
  - `units`:
    - `omega_2D`: cm⁻¹
    - `FWHM_2D`: cm⁻¹

Notes: The verifier fits linear slopes ω₂D vs. strain and FWHM₂D vs. strain from the submitted table and compares them to hidden reference slopes derived from an independent correct implementation of the same model with ns=2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_peak_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "omega_2D",
          "FWHM_2D"
        ],
        "units": {
          "omega_2D": "cm⁻¹",
          "FWHM_2D": "cm⁻¹"
        }
      },
      "description": "CSV with model-predicted Raman 2D band peak position and width at varying applied matrix strains."
    }
  ],
  "notes": "The verifier fits linear slopes ω₂D vs. strain and FWHM₂D vs. strain from the submitted table and compares them to hidden reference slopes derived from an independent correct implementation of the same model with ns=2."
}
```

## How you are scored
A hidden verifier reads your `predicted_peak_properties.csv`, performs a linear regression of ω₂D against strain_percent and of FWHM_2D against strain_percent to obtain the mean slopes dω₂D/dε and dFWHM₂D/dε. Both slopes are required; missing data or an absent column results in zero credit. Each slope is compared against a hidden reference value derived from an independent correct model implementation using the same ns = 2. The reward is full when both slopes match their references to within a hidden tolerance and decreases monotonically as the deviation grows. Note that the checker does not directly compare your raw ω₂D and FWHM₂D numbers to any paper values; it works exclusively with the slopes it computes from your CSV, so accurate implementation of the strain‑distribution and spectral‑summation steps is essential to obtain the correct slopes.
