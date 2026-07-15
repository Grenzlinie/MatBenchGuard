# DFT dielectric function calculation from electronic structure

## Problem background
CsSnX3 (X = Cl, Br, I) perovskites are promising lead-free candidates for photovoltaic cells and energy storage. Their optical constants — the dielectric function, refractive index, energy-loss spectra, and the effective number of electrons involved in optical transitions — are critical for assessing light absorption and device efficiency. This task investigates these optical properties across the cubic, tetragonal, and orthorhombic phases using first-principles density functional theory (DFT) with a functional that yields accurate band gaps.

## Approach
Use density functional theory (DFT) to compute the electronic structure and optical properties of CsSnX3 compounds in the cubic, tetragonal, and orthorhombic crystal phases. For each compound‑phase combination, construct the crystal structure using experimental lattice constants, perform self‑consistent field calculations to obtain Kohn‑Sham eigenstates, and then compute the optical response within the independent‑particle approximation. From the complex dielectric function, derive the zero‑frequency dielectric constant, the static refractive index, the energy‑loss function, and the effective number of electrons. The exchange‑correlation functional must be chosen to reproduce the experimentally observed band gaps (e.g., TB‑mBJ or HSE06), so that the optical constants reflect the correct onset of absorption.

## Reproduction target
For each of the eight compound–phase combinations (CsSnCl3 cubic and orthorhombic; CsSnBr3 cubic, tetragonal, and orthorhombic; CsSnI3 cubic, tetragonal, and orthorhombic), compute the direct band gap, the zero‑frequency dielectric constant ε₁(0), the static refractive index n(0), the plasma‑resonance peak position (eV) of the energy‑loss function, and the effective number of electrons N_eff integrated up to 40 eV. Output all values in a single JSON file at /app/outputs/computed_optical_constants.json according to the format specified in the output contract.

## Assets

- Open-source DFT package with optical properties capability: https://www.quantum-espresso.org/
- Pseudopotentials for Cs, Sn, Cl, Br, I: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Construct the crystal structures for all eight compound-phase combinations (CsSnCl3 cubic/orthorhombic; CsSnBr3 cubic/tetragonal/orthorhombic; CsSnI3 cubic/tetragonal/orthorhombic) using the following experimental lattice constants and standard atomic positions for space groups Pm-3m (cubic), P4/mbm (tetragonal), and Pnma (orthorhombic).

Experimental lattice constants:
- CsSnCl3 cubic: a = 5.56 Å
- CsSnCl3 orthorhombic: a = 10.328 Å, b = 17.677 Å, c = 4.765 Å
- CsSnBr3 cubic: a = 5.795 Å
- CsSnBr3 tetragonal: a = 11.59 Å, c = 11.61 Å
- CsSnBr3 orthorhombic: a = 8.2149 Å, b = 11.6322 Å, c = 8.1844 Å
- CsSnI3 cubic: a = 6.219 Å
- CsSnI3 tetragonal: a = 8.775 Å, c = 6.271 Å
- CsSnI3 orthorhombic: a = 8.688 Å, b = 8.643 Å, c = 12.377 Å

For atomic coordinates, use the conventional perovskite positions for each space group (e.g., cubic Pm-3m: Cs 1a (0,0,0), Sn 1b (½,½,½), X 3d (½,0,0), (0,½,0), (0,0,½); for tetragonal P4/mbm and orthorhombic Pnma, look up standard literature or database entries for the respective perovskite phases). Save the structures in input format suitable for the chosen DFT code.
- Evidence: `/app/outputs/structures_generated.log`

### Step 2: DFT electronic structure calculation
- Role: process
- Action: For each structure, run a self-consistent field (SCF) DFT calculation followed by a non-self-consistent (NSCF) calculation on a dense k-point mesh using a functional that gives accurate band gaps (e.g., TB-mBJ or HSE06). Determine the direct band gap at the appropriate k-point (R for cubic, Γ for tetragonal/orthorhombic). Ensure eigenvalues, wavefunctions, and momentum matrix elements are saved for optical property calculation.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 3: Compute optical properties and export results
- Role: scored (load-bearing)
- Action: Compute the complex dielectric function using the independent-particle approximation from the DFT output. Apply Kramers-Kronig relations to obtain ε₁(ω) and extract the zero-frequency limit ε₁(0). Compute the static refractive index n(0) = √ε₁(0). Calculate the energy-loss function L(ω) and locate its most prominent peak (eV). Integrate the optical sum rule up to 40 eV to obtain Neff. Write all extracted values (band_gap_eV, epsilon1_0, n_0, plasma_peak_eV, Neff_plateau) for every compound-phase combination into /app/outputs/computed_optical_constants.json.
- Output file: `/app/outputs/computed_optical_constants.json`
- Format: json
- Contract: A JSON object whose top-level keys are compound-phase labels (e.g., "CsSnCl3_cubic", "CsSnBr3_tetragonal", "CsSnI3_orthorhombic") and whose values are objects with fields: band_gap_eV (float), epsilon1_0 (float), n_0 (float), plasma_peak_eV (float), Neff_plateau (int).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_optical_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_optical_constants.json
- path: `/app/outputs/computed_optical_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the computed optical constants for each compound-phase combination.
- schema:
  - `type`: object
  - `patternProperties`:
    - `^[A-Za-z0-9_]+\_[a-z]+$`:
      - `type`: object
      - `required`: `band_gap_eV`, `epsilon1_0`, `n_0`, `plasma_peak_eV`, `Neff_plateau`
      - `properties`:
        - `band_gap_eV`:
          - `type`: number
        - `epsilon1_0`:
          - `type`: number
        - `n_0`:
          - `type`: number
        - `plasma_peak_eV`:
          - `type`: number
        - `Neff_plateau`:
          - `type`: integer

Notes: The solver must install and use an open-source DFT code with optical property capabilities. The chosen functional should reliably reproduce band gaps within ~0.3 eV of experiment. The checker will compare the submitted values against paper-reported reference values using absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_optical_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "patternProperties": {
          "^[A-Za-z0-9_]+\\_[a-z]+$": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "epsilon1_0",
              "n_0",
              "plasma_peak_eV",
              "Neff_plateau"
            ],
            "properties": {
              "band_gap_eV": {
                "type": "number"
              },
              "epsilon1_0": {
                "type": "number"
              },
              "n_0": {
                "type": "number"
              },
              "plasma_peak_eV": {
                "type": "number"
              },
              "Neff_plateau": {
                "type": "integer"
              }
            }
          }
        }
      },
      "description": "Contains the computed optical constants for each compound-phase combination."
    }
  ],
  "notes": "The solver must install and use an open-source DFT code with optical property capabilities. The chosen functional should reliably reproduce band gaps within ~0.3 eV of experiment. The checker will compare the submitted values against paper-reported reference values using absolute tolerances."
}
```

## How you are scored
A hidden verifier will independently read your submitted /app/outputs/computed_optical_constants.json and compare each reported quantity against reference values for the same compound‑phase combinations. Your score is based on how closely your computed values match the expected physical quantities, with each quantity contributing to an overall reward between 0 and 1. Simply reporting numbers is not sufficient; the values must result from a correctly executed DFT pipeline as described in the workflow steps.
