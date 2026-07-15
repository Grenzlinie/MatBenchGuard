# Point-charge Coulomb model for deep-level divacancy luminescence in CdSe

## Problem background
CdSe nanocrystals and bulk crystals consistently exhibit two broad deep-level luminescence bands (commonly labelled E1 and E2) separated by a few tenths of an electron volt. A simple divacancy model has been proposed in which these emissions arise from electron–hole recombination at two different orientations of a V_Cd–V_Se divacancy in the wurtzite lattice. In the model the hole is strongly localized at one selenium neighbour around the cadmium vacancy, while the electron can be trapped at two geometrically distinct cadmium sites near the selenium vacancy, leading to two different electron–hole distances and thus two Coulomb energies. The predicted luminescence peak energies are then obtained by subtracting a Stokes shift from the Coulomb energies. This task asks you to compute the Coulomb energies and the resulting luminescence peak energies for the sp² hole-localisation geometry from the point-charge model, testing whether the divacancy picture yields consistent predictions.

## Approach
The approach is a point-charge Coulomb model. The hole is assumed to be localized on one Se ligand in a trigonal Jahn–Teller distorted configuration with sp² hybrid character. The electron is trapped at a Cd ligand around the selenium vacancy. For the two divacancy configurations E1 (axial) and E2 (basal), the electron–hole separation distances differ. The Coulomb attraction energy is computed as U = e²/d, using the Coulomb constant e²/(4πε₀) = 1.44 eV·nm. The Cd–Se bond length b = 0.263 nm defines the length scale, and the two distances are given as multiples of b. Strong electron–phonon coupling, characterised by a Huang–Rhys factor S = 18 and an LO-phonon energy ħω_LO = 26 meV, introduces a Stokes shift that reduces the zero‑phonon line to the luminescence maximum. The predicted luminescence energy for each configuration is therefore hν = U – Sħω_LO, where Sħω_LO is computed from the given parameters. Implement this model for the sp² geometry to obtain the numerical predictions.

## Reproduction target
Implement the point-charge Coulomb model for the sp² hole-localisation geometry. Using the Cd–Se bond length b = 0.263 nm, the electron–hole distances d(E1) = 1.805 b and d(E2) = 2.108 b, and the Coulomb constant e²/(4πε₀) = 1.44 eV·nm, compute the Coulomb energies U(E1) and U(E2). Then calculate the Stokes shift Sħω_LO (with S = 18 and ħω_LO = 26 meV) and subtract it from each Coulomb energy to obtain the predicted luminescence peak energies hν(E1) and hν(E2). Write all results to `/app/outputs/predictions.json` with keys: `geometry` (string "sp2"), `E1_U_eV` (float), `E2_U_eV` (float), `E1_hnu_eV` (float), `E2_hnu_eV` (float), `stokes_shift_eV` (float).

## Assets
No external datasets, models, or specialised software are required. All necessary parameters are provided in the instruction. The computation can be performed with any standard programming environment (e.g., Python with its built‑in json module). No additional downloads are needed.

## Workflow steps

### Step 1: Point‑charge Coulomb model luminescence energies
- Role: scored
- Action: Implement the point-charge Coulomb model for the sp² hole localisation geometry. Use the Cd–Se bond length b = 0.263 nm and the electron–hole separation distances d(E1)=1.805b, d(E2)=2.108b to compute the Coulomb attraction energies U = e²/d, using e²/(4πε₀) = 1.44 eV·nm. Subtract the Stokes shift Sħω_LO = 18 × 0.026 eV = 0.468 eV to obtain the predicted luminescence maxima hν(E1) = U(E1) – 0.468 eV and hν(E2) = U(E2) – 0.468 eV.
- Output file: `/app/outputs/predictions.json`
- Format: json
- Contract: JSON object with keys: 'geometry' (string 'sp2'), 'E1_U_eV' (float), 'E2_U_eV' (float), 'E1_hnu_eV' (float), 'E2_hnu_eV' (float), 'stokes_shift_eV' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.json
- path: `/app/outputs/predictions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Predicted luminescence energies from the point-charge Coulomb model using sp² hole localisation.
- schema:
  - `type`: object
  - `required`:
    - `geometry`: string
    - `E1_U_eV`: number (eV)
    - `E2_U_eV`: number (eV)
    - `E1_hnu_eV`: number (eV)
    - `E2_hnu_eV`: number (eV)
    - `stokes_shift_eV`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: All numerical inputs are fixed physical constants. The expected values are those given by the model; the agent must compute them from the stated parameters. Floating‑point precision within reasonable tolerance is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "geometry": "string",
          "E1_U_eV": "number (eV)",
          "E2_U_eV": "number (eV)",
          "E1_hnu_eV": "number (eV)",
          "E2_hnu_eV": "number (eV)",
          "stokes_shift_eV": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Predicted luminescence energies from the point-charge Coulomb model using sp² hole localisation."
    }
  ],
  "notes": "All numerical inputs are fixed physical constants. The expected values are those given by the model; the agent must compute them from the stated parameters. Floating‑point precision within reasonable tolerance is required."
}
```

## How you are scored
A hidden verifier independently reads your `predictions.json`. It first checks that `stokes_shift_eV` equals the value computed from the given S and ħω_LO within a narrow tolerance. It then recomputes the expected Coulomb energies from the prescribed distances and the Coulomb constant, comparing them to your `E1_U_eV` and `E2_U_eV` values. Using those recomputed Coulomb energies, it computes the expected luminescence energies hν = U – stokes_shift and compares them to your `E1_hnu_eV` and `E2_hnu_eV`. Each check contributes to the overall reward. Reporting the correct numbers is essential, but the verifier derives its references from the same model inputs – you must carry out the actual calculation to produce consistent results.
