# Electronic Structure of La2CuO4: LSDA vs LSDA+U

## Problem background
The parent compound La2CuO4 of the high‑temperature superconductors is a Mott insulator with antiferromagnetic order. Standard density‑functional theory within the local spin‑density approximation (LSDA) often struggles to describe the ground state of such materials. The LSDA+U method attempts to improve the description by introducing an on‑site Coulomb interaction (U) and exchange (J) for the correlated Cu 3d electrons. The aim of this reproduction is to compute the electronic ground state of La2CuO4 with both the plain LSDA and the LSDA+U approach and to extract the band gap and the Cu local magnetic moment from each calculation.

## Approach
The reproduction uses density‑functional theory with plane‑wave basis sets as implemented in the open‑source code Quantum ESPRESSO. The tetragonal crystal structure of La2CuO4 (space group I4/mmm) is built from known lattice parameters and atomic positions. Two separate self‑consistent calculations are performed: (i) a standard spin‑polarized LSDA calculation, and (ii) an LSDA+U calculation in which a Hubbard correction is applied to the Cu 3d orbitals following the Dudarev rotationally‑invariant scheme. After reaching electronic convergence, the band gap is obtained as the energy difference between the conduction‑band minimum and the valence‑band maximum, and the Cu local magnetic moment is extracted by integrating the spin density within the Cu atomic sphere. The two sets of results—one from LSDA and one from LSDA+U—are then compared to verify the predicted metal‑to‑insulator transition and the formation of a local magnetic moment.

## Reproduction target
Set up the tetragonal La2CuO4 crystal, run spin‑polarized LSDA and LSDA+U plane‑wave DFT calculations, and produce a single JSON file (`results.json`) that contains, for each method, the band gap (in eV) and the Cu local magnetic moment (in μB).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotentials for La, Cu, O: https://www.materialscloud.org/discover/sssp/table
- La2CuO4 tetragonal crystal structure (I4/mmm)

## Workflow steps

### Step 1: Prepare La2CuO4 crystal structure and DFT input files
- Role: process
- Action: Define the tetragonal cell (a=3.80 Å, c=13.20 Å, I4/mmm) with atomic positions as given. Generate Quantum ESPRESSO input files for LSDA and LSDA+U calculations, specifying pseudopotentials, a plane-wave cutoff, and a k-point mesh. For LSDA+U, apply Hubbard correction to Cu 3d orbitals using the Dudarev approach with U_eff = U - J = 7.42 - 1.35 = 6.07 eV.
- Evidence: `/app/outputs/input_files.tar.gz`

### Step 2: Run LSDA calculation
- Role: process
- Action: Execute the self-consistent LSDA calculation for La2CuO4 using a spin-polarized calculation. Record the final total energy, eigenvalues, and charge density. Extract the band gap as the smallest energy between the top of the valence band and the bottom of the conduction band. Extract the Cu magnetic moment as the integrated spin density difference in the Cu pseudopotential sphere.
- Evidence: `/app/outputs/lsda_run.log`

### Step 3: Run LSDA+U calculation
- Role: process
- Action: Execute the self-consistent LSDA+U calculation for La2CuO4, applying the Hubbard U and J parameters to Cu 3d orbitals. Use the same structural and computational settings as the LSDA calculation. Extract band gap and Cu magnetic moment analogously.
- Evidence: `/app/outputs/lsdau_run.log`

### Step 4: Compile results into scored JSON
- Role: scored (load-bearing)
- Action: From the outputs of the two previous steps, collect the band gap and Cu magnetic moment for LSDA and LSDA+U and write them to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"LSDA": {"band_gap_eV": <float>, "Cu_moment_muB": <float>}, "LSDA_plus_U": {"band_gap_eV": <float>, "Cu_moment_muB": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed charge-transfer gap (eV) and local Cu magnetic moment (μB) for La2CuO4 from both LSDA (reference) and LSDA+U calculations. The checker compares against hidden paper reference values.
- schema:
  - `type`: object
  - `required_keys`: `LSDA`, `LSDA_plus_U`
  - `properties`:
    - `LSDA`:
      - `band_gap_eV`: number (eV)
      - `Cu_moment_muB`: number (μB)
    - `LSDA_plus_U`:
      - `band_gap_eV`: number (eV)
      - `Cu_moment_muB`: number (μB)

Notes: Only the main La2CuO4 result (gap and moment for LSDA and LSDA+U) is covered; AMF, LaCuO3, and spectral simulations are out of scope per taskability. The LSDA+U scored step is load-bearing: it requires the preceding process calculations to have been run.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "LSDA",
          "LSDA_plus_U"
        ],
        "properties": {
          "LSDA": {
            "band_gap_eV": "number (eV)",
            "Cu_moment_muB": "number (μB)"
          },
          "LSDA_plus_U": {
            "band_gap_eV": "number (eV)",
            "Cu_moment_muB": "number (μB)"
          }
        }
      },
      "description": "Computed charge-transfer gap (eV) and local Cu magnetic moment (μB) for La2CuO4 from both LSDA (reference) and LSDA+U calculations. The checker compares against hidden paper reference values."
    }
  ],
  "notes": "Only the main La2CuO4 result (gap and moment for LSDA and LSDA+U) is covered; AMF, LaCuO3, and spectral simulations are out of scope per taskability. The LSDA+U scored step is load-bearing: it requires the preceding process calculations to have been run."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares the LSDA and LSDA+U band gaps and Cu magnetic moments to reference values. The verifier checks that the LSDA+U values correspond to an insulating antiferromagnetic state and that the LSDA values correspond to a metallic nonmagnetic state. It also evaluates how closely your computed quantities match the published results, using tolerances that account for differences in implementation, pseudopotentials, and numerical settings. Each workflow stage is inspected, and the final score is a weighted combination across the stages; reporting the correct numbers without having run the calculations is not sufficient to obtain a high score.
