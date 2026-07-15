# Ionization energy and electron‑phonon coupling analysis from optical spectra of ZnS

## Problem background
In II-VI compound semiconductors, low-temperature photoluminescence spectra reveal sharp bound-exciton lines and broad edge-emission bands that serve as fingerprints of donor and acceptor impurities. For iodine-doped cubic ZnS single crystals, resolving and analyzing these spectral features allows determination of the ionization energies of unknown donors and acceptors and characterization of the electron–LO-phonon coupling and recombination kinetics. The target of this reproduction is to compute several key quantities from the reported peak energies and physical constants, using the effective-mass bound-exciton model and the donor-acceptor pair reaction formalism.

## Approach
The analysis rests on the effective-mass approximation for excitons bound to neutral donors and acceptors. From the measured free-exciton emission line and the band gap, one derives the free‑exciton binding energy and the reduced exciton mass. The bound‑exciton peak energies are then used to estimate donor and acceptor ionization energies via linear relations that connect the localization energy of the bound exciton to the impurity binding energy, with proportionality constants determined by the electron-to-hole effective‑mass ratio.

The edge‑emission spectra are analyzed by identifying zero‑phonon lines and considering the time‑dependent peak shift of the donor‑acceptor pair band to extract the donor and acceptor depths and the bound‑to‑bound transition probability W0. Additionally, the Huang–Rhys factor S is extracted from the intensity ratio of phonon replicas; it provides an independent estimate of the acceptor depth via a polar coupling model. The fidelity of the extracted S is checked by simulating the LO‑phonon sideband intensities with a Poisson distribution.

## Reproduction target
Produce a JSON file `results.json` containing six computed quantities:

- E_D: donor ionization energy (eV)
- E_A1: acceptor ionization energy from the I_a bound‑exciton line (eV)
- E_A2: acceptor ionization energy from the I_β bound‑exciton line (eV)
- acceptor_depth_A0: acceptor depth from the A0 zero‑phonon line (eV)
- donor_depth_AB: donor depth from the energy difference between the A0 and B0 zero‑phonon lines (eV)
- W0: donor‑acceptor pair reaction constant (1/s)

All input data (peak energies, material constants, time‑resolved Coulomb energy) are provided in the step descriptions below. The task also requires intermediate calculations (free‑exciton binding energy, reduced exciton mass, Huang–Rhys factor, Poisson phonon intensities) as process steps, but only the six headline quantities in `results.json` are scored.

## Assets

- Python 3 (stdlib, math, json): Python standard library

## Workflow steps

### Step 1: Compute free-exciton binding energy and exciton effective masses
- Role: process
- Action: Using the given free-exciton peak energy I_ex = 3.801 eV and band gap E_g = 3.84 eV at 4.2 K, compute the free-exciton binding energy E_ex = E_g - I_ex. Using E_ex and the static dielectric constant ε0 = 8.3, compute the reduced exciton mass μ0 via the hydrogenic model G = e² μ0 / (2 ħ² ε0² n²) with n=1. Then, with the electron effective mass m_e* = 0.39 m_e, deduce the average hole effective mass m_h* = 1 / (1/μ0 - 1/m_e*) and the mass ratio a = m_e*/m_h*. Save the results to exciton_params.json.
- Evidence: `/app/outputs/exciton_params.json`

### Step 2: Extract Huang-Rhys factor and estimate acceptor depth from electron‑LO‑phonon coupling
- Role: process
- Action: Given the intensity ratio I1/I0 ≈ 1.3, set the Huang‑Rhys factor S = 1.3. Using the relation S = (5/(16 a_h)) (e²/ħω_LO)(1/ε∞ - 1/ε0) with E_A = e²/(ε0 a_h), and the known values ε∞ ≈ 5.7, ε0 = 8.3, ħω_LO = 42 meV, compute the acceptor binding energy E_A(S). Save S and E_A(S) to huang_rhys.json.
- Evidence: `/app/outputs/huang_rhys.json`

### Step 3: Compute ionization energies, edge‑emission depths, and reaction constant
- Role: scored
- Action: Using the bound‑exciton line energies I_D = 3.792 eV, I_a = 3.729 eV, I_β = 3.701 eV, zero‑phonon line energies A0 = 3.659 eV, B0 = 3.543 eV, band‑gap energy E_g = 3.84 eV, free‑exciton binding energy E_ex = 40 meV, time‑resolved Coulomb energy E_cmax = 0.06 eV at t = 5 μs, and the edge‑emission donor depth E_D(edge) = A0 - B0, apply the neutral‑donor bound‑exciton relation E_D = (E_g - E_ex - I_D) / 0.1, the neutral‑acceptor bound‑exciton relation E_A = (E_g - E_ex - (A^0,X)) / 0.12 for each of I_a and I_β, compute acceptor depth from A0 as E_g - A0, donor depth from edge emission as A0 - B0, and bound‑to‑bound reaction constant W0 from ln(W0) = 4 E_D(edge) / E_cmax + ln(1 - E_cmax / E_D(edge)) - ln(t). Write the six computed values to results.json with keys E_D, E_A1, E_A2, acceptor_depth_A0, donor_depth_AB, W0.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": ["E_D", "E_A1", "E_A2", "acceptor_depth_A0", "donor_depth_AB", "W0"], "properties": {"E_D": {"type": "number", "units": "eV"}, "E_A1": {"type": "number", "units": "eV"}, "E_A2": {"type": "number", "units": "eV"}, "acceptor_depth_A0": {"type": "number", "units": "eV"}, "donor_depth_AB": {"type": "number", "units": "eV"}, "W0": {"type": "number", "units": "1/s"}}}
- Scoring: scored by hidden verifier

### Step 4: Simulate LO‑phonon sideband intensities with Poisson distribution
- Role: process
- Action: Using the Huang‑Rhys factor S = 1.3, compute the theoretical relative intensities I_n = exp(-S) * S^n / n! for phonon orders n = 0, 1, ..., 5. Save the results as a CSV file phonon_intensity.csv with columns n and I_n.
- Evidence: `/app/outputs/phonon_intensity.csv`

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
- description: The six headline quantities recomputed from the spectral data and physical constants: donor ionization energy E_D, acceptor ionization energies E_A1 and E_A2 from bound‑exciton lines, acceptor depth from the A0 zero‑phonon line, donor depth from the A0–B0 energy difference, and bound‑to‑bound reaction constant W0 from the time‑resolved peak shift.
- schema:
  - `type`: object
  - `required`: `E_D`, `E_A1`, `E_A2`, `acceptor_depth_A0`, `donor_depth_AB`, `W0`
  - `properties`:
    - `E_D`:
      - `type`: number
      - `units`: eV
    - `E_A1`:
      - `type`: number
      - `units`: eV
    - `E_A2`:
      - `type`: number
      - `units`: eV
    - `acceptor_depth_A0`:
      - `type`: number
      - `units`: eV
    - `donor_depth_AB`:
      - `type`: number
      - `units`: eV
    - `W0`:
      - `type`: number
      - `units`: 1/s

Notes: All six quantities are computed directly from the provided peak energies and material constants using the neutral‑donor/neutral‑acceptor bound‑exciton relations and the donor‑acceptor pair reaction formula. No experimental data retrieval or fitting is required. The scoring checks each value against the hidden paper‑reported reference within a per‑quantity tolerance.

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
        "required": [
          "E_D",
          "E_A1",
          "E_A2",
          "acceptor_depth_A0",
          "donor_depth_AB",
          "W0"
        ],
        "properties": {
          "E_D": {
            "type": "number",
            "units": "eV"
          },
          "E_A1": {
            "type": "number",
            "units": "eV"
          },
          "E_A2": {
            "type": "number",
            "units": "eV"
          },
          "acceptor_depth_A0": {
            "type": "number",
            "units": "eV"
          },
          "donor_depth_AB": {
            "type": "number",
            "units": "eV"
          },
          "W0": {
            "type": "number",
            "units": "1/s"
          }
        }
      },
      "description": "The six headline quantities recomputed from the spectral data and physical constants: donor ionization energy E_D, acceptor ionization energies E_A1 and E_A2 from bound‑exciton lines, acceptor depth from the A0 zero‑phonon line, donor depth from the A0–B0 energy difference, and bound‑to‑bound reaction constant W0 from the time‑resolved peak shift."
    }
  ],
  "notes": "All six quantities are computed directly from the provided peak energies and material constants using the neutral‑donor/neutral‑acceptor bound‑exciton relations and the donor‑acceptor pair reaction formula. No experimental data retrieval or fitting is required. The scoring checks each value against the hidden paper‑reported reference within a per‑quantity tolerance."
}
```

## How you are scored
A hidden verifier reads `results.json` and compares each of the six numeric values against the paper’s reported reference values, using appropriate tolerances. Each entry that falls within its tolerance earns its share of the total reward. The final score is the fraction of entries that pass, weighted equally across all six quantities.

The intermediate process artifacts (`exciton_params.json`, `huang_rhys.json`, `phonon_intensity.csv`) are required for execution but are not directly scored; only `results.json` contributes to the reward. Reporting the correct numbers is not enough — the verifier expects the values to be computed via the prescribed workflow, but it does not inspect your code; it only checks the final numeric output.
