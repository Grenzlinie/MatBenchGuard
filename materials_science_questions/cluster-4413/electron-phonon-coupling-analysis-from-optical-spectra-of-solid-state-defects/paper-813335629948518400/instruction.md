# Computational reproduction of exciton-phonon sidebands in metallic carbon nanotubes using semiconductor Bloch equations

## Problem background
Excitonic effects dominate the optical response of carbon nanotubes. When excitons interact with lattice vibrations (phonons), the absorption spectra develop pronounced phonon sidebands alongside the main excitonic peak. These sidebands carry valuable information about exciton-phonon coupling strengths. The position of the zero-phonon line shifts (polaron shift) and a fraction of the spectral weight is transferred from the main peak to the sidebands. Understanding how these quantities depend on the nanotube's diameter, chiral angle, and temperature is essential for interpreting experimental spectra and for designing nanotube-based optoelectronic devices.

## Approach
We will implement a theoretical framework that combines a tight-binding description of the electronic structure with many-body Coulomb interactions and electron-phonon coupling. The calculation proceeds in several stages. First, the single-particle band structure and optical matrix elements are obtained from a zone-folded nearest-neighbour tight-binding model. The Coulomb interaction on the tube surface is regularised and statically screened using the Lindhard approximation; then the electron-hole interaction is treated by solving the excitonic eigenvalue problem to obtain the lowest-energy exciton wavefunction and its binding energy. Next, the electron-phonon coupling for the two dominant optical phonon modes (Γ‑LO and K) is mapped from graphene to the nanotube geometry and projected onto the excitonic basis, yielding exciton-phonon coupling matrix elements. Finally, the absorption coefficient is computed using an analytic expression in the excitonic basis that incorporates the phonon influence via a self-energy term, accounting for both phonon emission and absorption at finite temperature. By comparing spectra calculated with and without the phonon coupling, we extract the polaronic shift of the zero-phonon line and the percentage of total oscillator strength transferred to the phonon sidebands.

## Reproduction target
Implement the above workflow for the following set of metallic carbon nanotubes, all in their lowest-energy optical transition. For five zigzag tubes – (9,0), (12,0), (15,0), (18,0), and (21,0) – compute the absorption spectrum at 300 K considering the Γ‑LO and K phonon modes separately. For three tubes selected from the Kataura branch 2n₁+n₂=24 with chiral angles near 0°, ~10°, and ~20°, also compute the spectra at 300 K with the two phonon modes. Additionally, for the (18,0) tube, obtain the Γ‑LO phonon-influenced spectrum at 300 K and 1000 K. For every (tube, phonon mode, temperature) combination, also compute the corresponding spectrum without phonon coupling (phonon coupling set to zero) to serve as a reference. From each pair of spectra (with and without phonon coupling) extract three quantities: the zero-phonon line energy, the polaron shift (the energy difference between the zero-phonon line with and without phonon coupling, in meV), and the spectral weight transfer (the integrated absorption in the phonon sidebands expressed as a percentage of the total absorption of the zero-phonon line). Compile all results into the CSV file `/app/outputs/polaron_spectral_weights.csv` with one row per combination and the columns specified in the output contract.

## Assets

- Tight-binding parameters for carbon nanotubes (γ₀, s₀)
- Electron‑phonon deformation potentials for Γ‑LO and K phonons
- Phonon energies for Γ‑LO and K modes
- Phonon lifetime (damping γ_s)
- Phenomenological electronic dephasing γ
- Effective atomic number Z_eff for carbon (used in Coulomb form factor)
- Carbon nanotube geometry rules
- Python scientific computing environment

## Workflow steps

### Step 1: Set up nanotube geometry and compute single‑particle states
- Role: process
- Action: For each required (n,m) carbon nanotube, compute the tube radius, unit-cell vectors, and a suitable k‑point grid. Calculate the tight‑binding band energies E_l(k) and wavefunction coefficients (C_a^l(k), C_b^l(k)) using the zone‑folded nearest‑neighbour tight‑binding model with parameters γ₀ and s₀. Also compute the interband optical matrix elements M_cv(k) using the analytic formula based on tight‑binding coefficients.
- Evidence: none

### Step 2: Construct screened Coulomb interaction and solve excitonic problem
- Role: process
- Action: Build the regularised Coulomb potential on the tube surface, apply static Lindhard screening to obtain screened Coulomb matrix elements, compute renormalisation and exchange contributions, and solve the excitonic eigenvalue problem for the lowest‑energy exciton to obtain its excitation energy ε₀ and wavefunction Φ₀(k).
- Evidence: none

### Step 3: Compute exciton‑phonon coupling matrix elements
- Role: process
- Action: Using the deformation potentials D_LO and D_K, map the graphene electron‑phonon coupling to the nanotube geometry and project onto the excitonic basis to obtain the coupling matrix elements g_{nn}^j(q) for the Γ‑LO and K phonon modes.
- Evidence: none

### Step 4: Compute absorption spectra with phonon sidebands
- Role: process
- Action: For each target nanotube and temperature, evaluate phonon occupancy, form the exciton‑phonon self‑energy, and compute the absorption coefficient α(ω) using the excitonic basis expression (including the required phonon contributions). Compute the spectrum both with the full coupling and with the coupling set to zero to obtain reference spectra.
- Evidence: none

### Step 5: Extract polaron shift and spectral weight transfer for all target nanotubes
- Role: scored (load-bearing)
- Action: Run the full pipeline (steps 1–4) for the five zigzag tubes (9,0), (12,0), (15,0), (18,0), (21,0) at 300 K with both Γ‑LO and K phonons; for three tubes from the 2n₁+n₂=24 Kataura branch with chiral angles close to 0°, ~10°, and ~20° at 300 K (both phonon modes); and for the (18,0) tube at 300 K and 1000 K (Γ‑LO only). For each case, from the spectra with and without phonon coupling determine the zero‑phonon line energy, the polaron shift (difference in peak positions, in meV), and the spectral weight transfer (integrated absorption in the sidebands divided by the total absorption of the zero‑phonon line, in percent). Output all values as a single CSV file.
- Output file: `/app/outputs/polaron_spectral_weights.csv`
- Format: csv
- Contract: CSV with columns: tube_id (string), diameter_nm (float), chiral_angle_deg (float), phonon_mode (string, 'Gamma-LO' or 'K'), temperature_K (float), polaron_shift_meV (float), spectral_weight_transfer_percent (float). One row per unique (tube, phonon_mode, temperature) condition. All numeric columns must be strictly numeric.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polaron_spectral_weights.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polaron_spectral_weights.csv
- path: `/app/outputs/polaron_spectral_weights.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of extracted polaron shifts and spectral weight transfer for the specified set of metallic carbon nanotubes. Checked against hidden reference values with tolerances and trend compliance.
- schema:
  - `type`: table
  - `required_columns`: `tube_id`, `diameter_nm`, `chiral_angle_deg`, `phonon_mode`, `temperature_K`, `polaron_shift_meV`, `spectral_weight_transfer_percent`
  - `units`:
    - `polaron_shift_meV`: meV
    - `spectral_weight_transfer_percent`: percent

Notes: The hidden checker compares the reported values to the paper's reported quantities with tolerances and verifies the expected diameter and chirality trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polaron_spectral_weights.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tube_id",
          "diameter_nm",
          "chiral_angle_deg",
          "phonon_mode",
          "temperature_K",
          "polaron_shift_meV",
          "spectral_weight_transfer_percent"
        ],
        "units": {
          "polaron_shift_meV": "meV",
          "spectral_weight_transfer_percent": "percent"
        }
      },
      "description": "Table of extracted polaron shifts and spectral weight transfer for the specified set of metallic carbon nanotubes. Checked against hidden reference values with tolerances and trend compliance."
    }
  ],
  "notes": "The hidden checker compares the reported values to the paper's reported quantities with tolerances and verifies the expected diameter and chirality trends."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier reads your output CSV and compares each reported polaron shift and spectral weight transfer to independently stored reference values derived from the original study. The comparison is performed with appropriate tolerances that account for the spread expected from different numerical implementations while still rejecting meaningless guesses. In addition, the verifier checks that the reported values follow the physically expected monotonic trends: for a fixed chiral angle, both polaron shift and spectral weight transfer should vary systematically with tube diameter; for tubes of similar diameter but different chiral angles, the quantities should also follow a systematic trend. The final reward is a weighted combination of the scores from the individual CSV entries and the trend checks. Simply reporting a number close to a known constant is not sufficient; the values must be internally consistent across the whole set of tubes, phonon modes, and temperatures.
