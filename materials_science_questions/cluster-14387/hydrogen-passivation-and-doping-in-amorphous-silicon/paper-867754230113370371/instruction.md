# DFT study of Pb adsorption on a high-index silicon surface: relative energies and electronic band structure

## Problem background
High-index silicon surfaces decorated with noble metals can template self-organized arrays of one-dimensional atomic chains. The Si(335)-Au surface is a well-known example: Au atoms substitute into the middle of terraces, leaving step-edge Si dangling bonds that form metallic chains. Adding Pb atoms at a coverage of 0.28 ML (one Pb per surface unit cell) creates new one-dimensional structures on top of the Au-reconstructed surface. Understanding the atomic arrangement and electronic character of the Pb chains is the open challenge: multiple structural models are plausible, and it needs to be determined which one is most stable, and whether the resulting band structure retains the one-dimensional metallic nature of the clean surface.

## Approach
The study employs density-functional theory (DFT) within the local density approximation (LDA), using a linear combination of numerical atomic orbitals as implemented in the SIESTA code. Troullier–Martins norm-conserving pseudopotentials (with semicore 5d states for Au and Pb) and a double-ζ polarized basis set are used. The surface is modelled as a four-silicon-double-layer slab with a vacuum region of 18 Å; the bottom Si layer is fixed and saturated with hydrogen. From this, slab models are built for the clean Si(335)-Au surface and for five candidate Pb adsorption/substitution configurations (Si3-Au-Au, Si1(subst), Si5-Si6-Si1, Au-Si1-Si1, Si4-Au). A bulk fcc Pb reference cell is also prepared. For each model, total-energy relaxations are performed, and relative surface energies are calculated by referencing to the clean surface and bulk Pb. After identifying the most stable Pb geometry from the relaxed energies, the electronic band structure of that lowest-energy model is computed along two high-symmetry paths: one parallel to the step direction (Γ–K–Mʹ) and one perpendicular to it (Γ–M), yielding the Kohn–Sham eigenvalues for all bands near the Fermi level.

## Reproduction target
As a standalone computational task, you must produce the following:

1. A CSV file (`relative_energies.csv`) with columns `model` (string) and `relative_energy_eV` (float), containing the relative surface energy for each of the five Pb structural models. The relative energy is defined as E_model − E_clean − E_bulk_Pb (per unit cell). The file must include all five model names.

2. Two CSV files containing the electronic band structure of the lowest-energy Pb model (whichever model you find to have the smallest relative energy after relaxation). The files are `band_structure_gamma_K.csv` (along the chain direction, path Γ–K–Mʹ) and `band_structure_gamma_M.csv` (perpendicular to the steps, path Γ–M). Each must have columns `kx` (reciprocal coordinate), `energy_eV` (band energy with Fermi level set to zero), and `band_index` (integer). Use at least 100 k‑points along each path and include all bands within ±2 eV of the Fermi level.

The correct solution is the one that emerges from an honest, converged DFT calculation with the specified functional, pseudopotentials, basis, and structural models. The checker will verify that the relative energies follow the expected ordering (with one model clearly lowest) and that the band structure exhibits one-dimensional metallic character (a dispersive band crossing the Fermi level along the chain and flat bands perpendicular to it).

## Assets

- SIESTA DFT code: https://siesta-project.org/siesta/
- Troullier-Martins norm-conserving pseudopotentials for Si, Au, Pb, H (with semicore 5d for Au and Pb): https://siesta-project.org/siesta/Pseudopotentials/

## Workflow steps

### Step 1: Build atomic structures
- Role: process
- Action: Construct slab models for the clean Si(335)-Au surface and for the five Pb adsorption/substitution candidate structures (Si3-Au-Au, Si1(subst), Si5-Si6-Si1, Au-Si1-Si1, Si4-Au) at 0.28 ML coverage. Use a four‑Si‑double‑layer slab with 18 Å vacuum, bottom Si atoms fixed at bulk positions and saturated with hydrogen. Prepare a bulk fcc Pb cell for the reference calculation. Follow the atomic arrangements and bonding information from the paper.
- Evidence: `/app/outputs/models_manifest.json`

### Step 2: Compute relative surface energies
- Role: scored
- Action: Run DFT relaxations using SIESTA with LDA functional, DZP basis, and Troullier‑Martins pseudopotentials for the clean Si(335)-Au surface, bulk fcc Pb, and each of the five Pb models. For each relaxed configuration extract the total energy and compute the relative surface energy as E_model − E_clean − E_Pb_bulk (per unit cell). Save the result as relative_energies.csv. Also save the relaxed atomic coordinates of the Si3‑Au‑Au model in a file relaxed_si3_au_au.xyz for later band‑structure steps.
- Output file: `/app/outputs/relative_energies.csv`
- Format: csv
- Contract: columns: model (string), relative_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 3: Compute band structure along chain direction (Gamma‑K‑M')
- Role: scored (load-bearing)
- Action: Using the relaxed Si3‑Au‑Au geometry from relaxed_si3_au_au.xyz, run a SIESTA band‑structure calculation along the high‑symmetry path Gamma‑K‑M' (parallel to the step direction). Output the Kohn‑Sham eigenvalues for all bands in the energy range of interest (e.g., −2 to +2 eV relative to Fermi level) as band_structure_gamma_K.csv.
- Output file: `/app/outputs/band_structure_gamma_K.csv`
- Format: csv
- Contract: columns: kx (float, reciprocal lattice coordinate), energy_eV (float, Fermi level at 0), band_index (int)
- Scoring: scored by hidden verifier

### Step 4: Compute band structure perpendicular to chain (Gamma‑M)
- Role: scored (load-bearing)
- Action: Using the same relaxed Si3‑Au‑Au geometry, compute the band structure along the Gamma‑M direction (perpendicular to the steps) and write the eigenvalues to band_structure_gamma_M.csv.
- Output file: `/app/outputs/band_structure_gamma_M.csv`
- Format: csv
- Contract: columns: kx (float), energy_eV (float, Fermi level at 0), band_index (int)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.csv`
- `/app/outputs/band_structure_gamma_K.csv`
- `/app/outputs/band_structure_gamma_M.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.csv
- path: `/app/outputs/relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative surface energies of the five stable Pb structural models referenced to the clean Si(335)-Au surface and bulk Pb.
- schema:
  - `type`: table
  - `required_columns`: `model`, `relative_energy_eV`
  - `units`:
    - `relative_energy_eV`: eV

### band_structure_gamma_K.csv
- path: `/app/outputs/band_structure_gamma_K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electronic band structure along direction parallel to the atomic chain. The checker will verify that at least one band crosses the Fermi level and that the dispersive band shows a peaked shape near the K point.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `energy_eV`, `band_index`
  - `units`:
    - `energy_eV`: eV
    - `kx`: reciprocal lattice coordinate

### band_structure_gamma_M.csv
- path: `/app/outputs/band_structure_gamma_M.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electronic band structure along direction perpendicular to the steps. The checker will verify that all bands are essentially flat (dispersion within ±0.2 eV) confirming the one-dimensional nature.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `energy_eV`, `band_index`
  - `units`:
    - `energy_eV`: eV
    - `kx`: reciprocal lattice coordinate

Notes: The agent must produce the three CSV artifacts. The hidden checker will compare relative energies to the paper's Table I and analyze the band eigenvalues for metallicity and dispersion.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "relative_energy_eV"
        ],
        "units": {
          "relative_energy_eV": "eV"
        }
      },
      "description": "Relative surface energies of the five stable Pb structural models referenced to the clean Si(335)-Au surface and bulk Pb."
    },
    {
      "file": "band_structure_gamma_K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "energy_eV",
          "band_index"
        ],
        "units": {
          "energy_eV": "eV",
          "kx": "reciprocal lattice coordinate"
        }
      },
      "description": "Electronic band structure along direction parallel to the atomic chain. The checker will verify that at least one band crosses the Fermi level and that the dispersive band shows a peaked shape near the K point."
    },
    {
      "file": "band_structure_gamma_M.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "energy_eV",
          "band_index"
        ],
        "units": {
          "energy_eV": "eV",
          "kx": "reciprocal lattice coordinate"
        }
      },
      "description": "Electronic band structure along direction perpendicular to the steps. The checker will verify that all bands are essentially flat (dispersion within ±0.2 eV) confirming the one-dimensional nature."
    }
  ],
  "notes": "The agent must produce the three CSV artifacts. The hidden checker will compare relative energies to the paper's Table I and analyze the band eigenvalues for metallicity and dispersion."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier. The verifier reads the three CSV artifacts from `/app/outputs` and independently scores them:

- The relative energies stage checks that all five models are present, that the energies are physically reasonable, and that the ordering identifies the correct most-stable model (the verifier compares against the expected ordering derived from the published study). The reward for this stage is proportional to how well your computed energies reproduce the correct relative stability.

- The band structure stages are evaluated for structural properties: the verifier examines the eigenvalues to confirm that at least one band crosses the Fermi level, that the dispersive band near the Fermi level shows a peaked shape along the Γ–K–Mʹ path (strong dispersion), and that all bands are essentially flat (dispersion within a tight band) along the Γ–M path. The reward for each band artifact reflects whether these one-dimensional metallic signatures are present.

The verifier combines the stage rewards into a final reward in [0, 1]. It does not compare against a single `correct` number but against the structural characteristics of a successful DFT reproduction. Reporting a set of numbers without running the DFT workflow cannot satisfy these checks. The verifier’s exact criteria and tolerances are hidden, but they account for the expected run-to-run variability of DFT calculations.
