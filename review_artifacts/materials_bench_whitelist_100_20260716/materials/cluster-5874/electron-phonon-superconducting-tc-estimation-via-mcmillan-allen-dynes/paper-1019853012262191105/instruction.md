# Ab-initio superconducting critical temperature calculation of layered metal borocarbides

## Problem background
This task concerns the first-principles prediction of superconductivity in layered metal borocarbides, specifically hole-doped Mg_xB_2C_2 and Na_xBC phases. These materials feature honeycomb boron‑carbon layers and, when doped with holes, can exhibit conventional phonon-mediated superconductivity akin to MgB₂. Determining their superconducting critical temperature Tc using ab initio methods is of great interest for guiding experimental synthesis of new ambient‑pressure superconductors. Your goal is to compute Tc for five target phases using density functional theory and anisotropic Migdal‑Eliashberg theory.

## Approach
You will follow a multi‑step computational protocol:
(i) Relax the provided crystal structures using density functional theory (DFT) with a van der Waals‑corrected exchange‑correlation functional (optB86b‑vdW or optB88‑vdW) and norm‑conserving pseudopotentials.
(ii) Compute phonon dispersions and dynamical matrices via density functional perturbation theory (DFPT).
(iii) Perform electron‑phonon coupling calculations using the EPW code, which employs Wannier interpolation via Wannier90 with 2p orbital projections for B and C atoms.
(iv) Solve the anisotropic full‑bandwidth Migdal‑Eliashberg equations at a fixed Coulomb pseudopotential μ* = 0.20 to obtain the superconducting critical temperature Tc for each structure.
No further input data or parameters beyond the provided CIF files and the open‑source codes are required.

## Reproduction target
Produce Tc values for all five structures: oS48-Mg₄/₅B₂C₂, hP7-Mg₂/₃B₂C₂, mP23-Na₇/₈BC, oP22-Na₃/₄BC, oS32-Na₂/₃BC. Save the results as a JSON file at /app/outputs/tc_results.json with the format [{"phase": "<identifier>", "Tc_K": <float>}, …]. The phase identifiers must match the provided CIF file names exactly.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- EPW: https://docs.epw-code.org/
- Wannier90: https://wannier.org/
- PseudoDojo pseudopotentials (norm-conserving, PBE relativistic): http://www.pseudo-dojo.org/
- CIF structure files for target phases

## Workflow steps

### Step 1: DFT geometry relaxation
- Role: process
- Action: Using Quantum ESPRESSO with optB86b-vdW or optB88-vdW functional and norm-conserving PBE pseudopotentials from PseudoDojo, relax the provided crystal structures (atomic positions and cell parameters) until forces and total energy are tightly converged for subsequent phonon calculations.
- Evidence: none

### Step 2: Phonon calculations (DFPT)
- Role: process
- Action: Compute dynamical matrices and interatomic force constants using density-functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO (ph.x) on regular q-point grids, generating all required files for EPW.
- Evidence: none

### Step 3: Electron-phonon coupling and Wannier interpolation
- Role: process
- Action: Run EPW to compute electron-phonon matrix elements, interpolate to fine k- and q-point grids, and obtain the Eliashberg spectral function and isotropic coupling constant λ. Use Wannier90 to generate maximally localized Wannier functions with 2p orbital projections for B and C atoms.
- Evidence: none

### Step 4: Superconducting Tc calculation (anisotropic Migdal-Eliashberg)
- Role: scored (load-bearing)
- Action: Solve the anisotropic full-bandwidth Migdal-Eliashberg equations using EPW with Coulomb pseudopotential μ*=0.20 on fine uniform k- and q-grids to obtain the superconducting critical temperature Tc for each of the five target phases. Write the results to tc_results.json.
- Output file: `/app/outputs/tc_results.json`
- Format: json
- Contract: A JSON array of objects: [{"phase": "oS48-Mg4/5B2C2", "Tc_K": 57.0}, ...] for the five phases. Phase identifiers must match the provided CIF file names (oS48-Mg4/5B2C2, hP7-Mg2/3B2C2, mP23-Na7/8BC, oP22-Na3/4BC, oS32-Na2/3BC). Tc_K is a numeric float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_results.json
- path: `/app/outputs/tc_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Superconducting critical temperature Tc (in K) for the five target phases computed with anisotropic Migdal-Eliashberg theory using μ*=0.20.
- schema:
  - `type`: array
  - `items`:
    - `phase`: string
    - `Tc_K`: number
  - `description`: Array of objects each containing the phase identifier and the computed superconducting critical temperature Tc in Kelvin.

Notes: The target phases are oS48-Mg4/5B2C2, hP7-Mg2/3B2C2, mP23-Na7/8BC, oP22-Na3/4BC, and oS32-Na2/3BC. The scoring compares each Tc value to a hidden reference with a fixed absolute tolerance; no directionality is assumed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "phase": "string",
          "Tc_K": "number"
        },
        "description": "Array of objects each containing the phase identifier and the computed superconducting critical temperature Tc in Kelvin."
      },
      "description": "Superconducting critical temperature Tc (in K) for the five target phases computed with anisotropic Migdal-Eliashberg theory using μ*=0.20."
    }
  ],
  "notes": "The target phases are oS48-Mg4/5B2C2, hP7-Mg2/3B2C2, mP23-Na7/8BC, oP22-Na3/4BC, and oS32-Na2/3BC. The scoring compares each Tc value to a hidden reference with a fixed absolute tolerance; no directionality is assumed."
}
```

## How you are scored
A hidden verifier will check your tc_results.json. For each phase, the verifier compares your reported Tc value to a hidden reference using an absolute tolerance; if the difference is within the tolerance, the phase counts as correct. The overall reward is the fraction of the five phases that are correct (a value between 0 and 1). No other output files contribute to the score.
