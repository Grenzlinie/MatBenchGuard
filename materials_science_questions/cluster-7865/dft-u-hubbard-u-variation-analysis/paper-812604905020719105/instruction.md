# DFT+DMFT Mott Insulating Gap and Hubbard Bands of Monolayer CrI2

## Problem background
Two-dimensional materials provide a rich platform for studying quantum phenomena emerging from strong electron–electron correlations. Monolayer chromium di-iodide (CrI₂) is predicted to host a Mott insulating state, where the Coulomb repulsion among Cr 3d electrons opens a band gap that conventional band theory cannot capture. The insulating gap and the orbital composition of the Hubbard bands are central to understanding the electronic structure of this material. Reproducing these quantities from first‑principles calculations quantifies the Mott physics in a single‑layer van der Waals magnet.

## Approach
We use a combined density functional theory (DFT) and dynamical mean‑field theory (DMFT) framework. First, a freestanding monolayer of CrI₂ is constructed from the known bulk crystal structure. A spin‑polarized DFT calculation within the local density approximation (LDA) is performed to obtain the Kohn–Sham wavefunctions. The Cr 3d bands are then projected onto maximally‑localized Wannier functions. These Wannier orbitals serve as the correlated subspace for DMFT. DMFT is solved with a continuous‑time quantum Monte Carlo impurity solver, using an on‑site Coulomb interaction U = 4.0 eV and a Hund’s exchange J/U = 0.2. Analytical continuation yields the real‑frequency self‑energy, from which the density of states and momentum‑resolved spectral function are computed. The calculation is carried out for both a ferromagnetic (FM) and a paramagnetic (PM) state to assess the magnetic dependence of the insulating gap.

## Reproduction target
From the FM DFT+DMFT density of states, determine the electronic band gap (in eV) between the highest valence and lowest conduction features. From the orbitally‑projected density of states and the momentum‑resolved spectral function of the FM phase, identify the orbital character (d_{z²} or d_{x²‑y²}) and spin character of the highest valence band and the lowest conduction band. Using the PM DFT+DMFT density of states, verify whether an insulating gap of similar magnitude persists. The two main outputs are a single floating‑point number written to `band_gap.txt` and a JSON summary written to `orbital_character.json` with keys `highest_valence_band_orbital`, `lowest_conduction_band_orbital`, and `paramagnetic_gap_consistent`.

## Assets

- CrI2 crystal structure (monolayer geometry): 10.1107/S0365110X6200140X
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: http://www.wannier.org/
- iQIST: https://github.com/huanglz/iQIST
- TRIQS: https://triqs.github.io/

## Workflow steps

### Step 1: Build monolayer CrI2 computational cell
- Role: process
- Action: Construct a freestanding monolayer CrI2 slab from the public bulk crystal structure (space group C2/m, a=3.88 Å, b=4.23 Å) with a vacuum layer >15 Å, and prepare the DFT input geometry.
- Evidence: `/app/outputs/crI2_structure.in`

### Step 2: LDA DFT calculation for ferromagnetic monolayer
- Role: process
- Action: Perform a spin-polarized LDA DFT calculation on monolayer CrI2 using Quantum ESPRESSO to obtain the Kohn-Sham eigenvalues and wavefunctions for Wannier projection. Initialize with ferromagnetic spin arrangement.
- Evidence: `/app/outputs/lda_fm.out`

### Step 3: Construct Cr 3d Wannier orbitals
- Role: process
- Action: Use Wannier90 to project the Kohn-Sham states onto maximally-localized Wannier functions for the Cr 3d orbitals, and generate the real-space Hamiltonian and projector files needed for DMFT.
- Evidence: `/app/outputs/wannier90.chk`

### Step 4: DFT+DMFT calculation for ferromagnetic phase
- Role: process
- Action: Run a DFT+DMFT calculation for the ferromagnetic (FM) phase using the Cr 3d Wannier projectors, on-site Coulomb U=4.0 eV, Hund's exchange J/U=0.2, and a hybridization-expansion continuous-time quantum Monte Carlo impurity solver. Compute the total density of states and momentum-resolved spectral function via analytical continuation.
- Evidence: `/app/outputs/dmft_fm_dos.dat, dmft_fm_spectral.dat`

### Step 5: Extract ferromagnetic band gap
- Role: scored (load-bearing)
- Action: From the FM DFT+DMFT density of states, determine the electronic band gap between the highest valence and lowest conduction features. Write a single floating-point number (in eV) to band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: A single floating-point number (e.g., 3.0).
- Scoring: scored by hidden verifier

### Step 6: DFT+DMFT calculation for paramagnetic phase
- Role: process
- Action: Run a DFT+DMFT calculation for the paramagnetic (PM) phase (non-spin-polarized) using the same U=4.0 eV, J/U=0.2, Wannier projectors, and impurity solver. Compute its density of states.
- Evidence: `/app/outputs/dmft_pm_dos.dat`

### Step 7: Identify orbital character of Hubbard bands and PM gap
- Role: scored
- Action: Examine the momentum-resolved spectral function and projected density of states of the FM phase to identify the orbital character (type and spin) of the highest valence band and lowest conduction band. From the PM density of states, determine whether a similar insulating gap persists. Save a JSON object with keys 'highest_valence_band_orbital' (string), 'lowest_conduction_band_orbital' (string), and 'paramagnetic_gap_consistent' (boolean) to orbital_character.json.
- Output file: `/app/outputs/orbital_character.json`
- Format: json
- Contract: {"highest_valence_band_orbital": string, "lowest_conduction_band_orbital": string, "paramagnetic_gap_consistent": bool}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`
- `/app/outputs/orbital_character.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Mott insulating gap from the ferromagnetic DFT+DMFT calculation.
- schema:
  - `type`: text
  - `units`: eV
  - `description`: A single floating-point number representing the DFT+DMFT band gap.

### orbital_character.json
- path: `/app/outputs/orbital_character.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Orbital character of the lower Hubbard bands and insulating nature of the paramagnetic phase.
- schema:
  - `type`: object
  - `required`: `highest_valence_band_orbital`, `lowest_conduction_band_orbital`, `paramagnetic_gap_consistent`
  - `properties`:
    - `highest_valence_band_orbital`:
      - `type`: string
    - `lowest_conduction_band_orbital`:
      - `type`: string
    - `paramagnetic_gap_consistent`:
      - `type`: boolean

Notes: The band gap is compared against the DFT+DMFT reference value with an appropriate tolerance. Orbital labels must match the expected character (e.g., 'Cr d_{z^2} spin-up') and paramagnetic_gap_consistent must be true.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "eV",
        "description": "A single floating-point number representing the DFT+DMFT band gap."
      },
      "description": "Mott insulating gap from the ferromagnetic DFT+DMFT calculation."
    },
    {
      "file": "orbital_character.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "highest_valence_band_orbital",
          "lowest_conduction_band_orbital",
          "paramagnetic_gap_consistent"
        ],
        "properties": {
          "highest_valence_band_orbital": {
            "type": "string"
          },
          "lowest_conduction_band_orbital": {
            "type": "string"
          },
          "paramagnetic_gap_consistent": {
            "type": "boolean"
          }
        }
      },
      "description": "Orbital character of the lower Hubbard bands and insulating nature of the paramagnetic phase."
    }
  ],
  "notes": "The band gap is compared against the DFT+DMFT reference value with an appropriate tolerance. Orbital labels must match the expected character (e.g., 'Cr d_{z^2} spin-up') and paramagnetic_gap_consistent must be true."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s required artifact. Both `band_gap.txt` and `orbital_character.json` are evaluated against reference expectations derived from the original DFT+DMFT study. The verifier checks that the reported band gap falls within a physically reasonable range and that the orbital labels and the paramagnetic‑gap consistency flag match the expected outcomes. The two scored stages carry weights that combine into a single final reward between 0 and 1. Reporting a number without executing the full DFT+DMFT pipeline is not sufficient; the verifier may also cross‑check the provided DOS and spectral evidence for consistency with the reported gap and orbital assignments.
