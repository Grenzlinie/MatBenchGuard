# Phonon Stability and Birefringence of Cyanate Compounds from DFT

## Problem background
Four novel cyanate compounds BaCNOX (X = Cl, Br, I, CNO) containing linear π‑conjugated (CNO)⁻ anions have been synthesized and their crystal structures determined. Such linear anionic groups are a design motif for large optical anisotropy (birefringence). The present task focuses on the first‑principles computational evaluation of these materials: starting from the published crystal structures, assess whether the compounds are dynamically stable (absence of imaginary phonon modes) and quantify their optical birefringence at 800 nm. The required computations are purely density functional theory based; no experimental synthesis or measurement is needed.

## Approach
Use density functional theory (DFT) with an open‑source code such as Quantum ESPRESSO. The workflow consists of three stages: (1) Structural optimization – fully relax the atomic positions (and optionally lattice parameters) of each compound starting from the experimental crystal structure (CIF files from the Cambridge Structural Database, deposition numbers 1964215‑1964218). (2) Phonon stability analysis – on the optimized structures, compute the phonon dispersion via density functional perturbation theory (DFPT) and determine whether any imaginary (negative) frequencies appear anywhere in the Brillouin zone. (3) Birefringence calculation – compute the frequency‑dependent dielectric tensor and extract the principal refractive indices n_x, n_y, n_z at a wavelength of 800 nm; the birefringence is the maximum difference among these three indices. The approach relies on standard plane‑wave DFT with a suitable exchange‑correlation functional (e.g., GGA‑PBE). The specific computational parameters (cutoff, k‑point mesh, pseudopotentials) are left to your discretion.

## Reproduction target
Produce the following two JSON files in `/app/outputs`:

1. **phonon_stability.json** – for each compound (BaCNOCl, BaCNOBr, BaCNOI, Ba(CNO)₂) a boolean `imaginary_modes_present` and a float `min_phonon_frequency_cm⁻¹` (the smallest phonon frequency in cm⁻¹; negative if imaginary modes exist).
2. **refractive_indices.json** – for each compound the three principal refractive indices `n_x`, `n_y`, `n_z` at 800 nm, and the derived `birefringence` (float) calculated as max(n) − min(n).

Your computed values must be the result of the DFT procedure described in the workflow steps. Simple fabrication or guessing will not match the hidden reference criteria used by the verifier.

## Assets

- Crystal structures of BaCNOCl, BaCNOBr, BaCNOI, Ba(CNO)₂: https://www.ccdc.cam.ac.uk/structures/
- Open‑source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: DFT Structural Optimization
- Role: process
- Action: For each of the four compounds, perform a full DFT structural optimization (atomic positions and, if needed, lattice parameters) starting from the CIF structures. Use a sufficiently high plane‑wave cutoff and k‑point grid to obtain relaxed geometries.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Phonon Stability Analysis
- Role: scored
- Action: Using density functional perturbation theory (DFPT) on the optimized structures, calculate the phonon dispersion of each compound. Identify the minimum phonon frequency across the full Brillouin zone and determine whether any imaginary (negative) modes exist. Write the results to /app/outputs/phonon_stability.json.
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: JSON object with keys 'BaCNOCl', 'BaCNOBr', 'BaCNOI', 'Ba(CNO)2'. Each value is an object with keys 'imaginary_modes_present' (boolean) and 'min_phonon_frequency_cm-1' (float, the smallest phonon frequency in cm⁻¹; negative if imaginary modes exist).
- Scoring: scored by hidden verifier

### Step 3: Birefringence Calculation
- Role: scored (load-bearing)
- Action: Compute the frequency‑dependent dielectric function for each compound using DFT, then derive the principal refractive indices (n_x, n_y, n_z) at a wavelength of 800 nm. Calculate the birefringence as the maximum difference among the three indices. Write the results to /app/outputs/refractive_indices.json.
- Output file: `/app/outputs/refractive_indices.json`
- Format: json
- Contract: JSON object with keys 'BaCNOCl', 'BaCNOBr', 'BaCNOI', 'Ba(CNO)2'. Each value is an object with keys 'n_x' (float), 'n_y' (float), 'n_z' (float) – principal refractive indices at 800 nm – and 'birefringence' (float, max(n)-min(n)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_stability.json`
- `/app/outputs/refractive_indices.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon stability verdict for each compound: imaginarY_modes_present must be false and min_phonon_frequency_cm-1 must be positive (or above a small tolerance).
- schema:
  - `type`: object
  - `required`:
    - `BaCNOCl`:
      - `imaginary_modes_present`: boolean
      - `min_phonon_frequency_cm-1`: float
    - `BaCNOBr`:
      - `imaginary_modes_present`: boolean
      - `min_phonon_frequency_cm-1`: float
    - `BaCNOI`:
      - `imaginary_modes_present`: boolean
      - `min_phonon_frequency_cm-1`: float
    - `Ba(CNO)2`:
      - `imaginary_modes_present`: boolean
      - `min_phonon_frequency_cm-1`: float

### refractive_indices.json
- path: `/app/outputs/refractive_indices.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Principal refractive indices at 800 nm and the derived birefringence Δn = max(n) – min(n). The checker compares the reported birefringence values to the paper‑reported values with an appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `BaCNOCl`:
      - `n_x`: float
      - `n_y`: float
      - `n_z`: float
      - `birefringence`: float
    - `BaCNOBr`:
      - `n_x`: float
      - `n_y`: float
      - `n_z`: float
      - `birefringence`: float
    - `BaCNOI`:
      - `n_x`: float
      - `n_y`: float
      - `n_z`: float
      - `birefringence`: float
    - `Ba(CNO)2`:
      - `n_x`: float
      - `n_y`: float
      - `n_z`: float
      - `birefringence`: float

Notes: The task reproduces the DFT‑computed phonon stability and giant birefringence. The electronic structure step is omitted because bandgap values are not reported numerically. All inputs are public (CCDC structures) and an open‑source DFT code is used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "BaCNOCl": {
            "imaginary_modes_present": "boolean",
            "min_phonon_frequency_cm-1": "float"
          },
          "BaCNOBr": {
            "imaginary_modes_present": "boolean",
            "min_phonon_frequency_cm-1": "float"
          },
          "BaCNOI": {
            "imaginary_modes_present": "boolean",
            "min_phonon_frequency_cm-1": "float"
          },
          "Ba(CNO)2": {
            "imaginary_modes_present": "boolean",
            "min_phonon_frequency_cm-1": "float"
          }
        }
      },
      "description": "Phonon stability verdict for each compound: imaginarY_modes_present must be false and min_phonon_frequency_cm-1 must be positive (or above a small tolerance)."
    },
    {
      "file": "refractive_indices.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BaCNOCl": {
            "n_x": "float",
            "n_y": "float",
            "n_z": "float",
            "birefringence": "float"
          },
          "BaCNOBr": {
            "n_x": "float",
            "n_y": "float",
            "n_z": "float",
            "birefringence": "float"
          },
          "BaCNOI": {
            "n_x": "float",
            "n_y": "float",
            "n_z": "float",
            "birefringence": "float"
          },
          "Ba(CNO)2": {
            "n_x": "float",
            "n_y": "float",
            "n_z": "float",
            "birefringence": "float"
          }
        }
      },
      "description": "Principal refractive indices at 800 nm and the derived birefringence Δn = max(n) – min(n). The checker compares the reported birefringence values to the paper‑reported values with an appropriate tolerance."
    }
  ],
  "notes": "The task reproduces the DFT‑computed phonon stability and giant birefringence. The electronic structure step is omitted because bandgap values are not reported numerically. All inputs are public (CCDC structures) and an open‑source DFT code is used."
}
```

## How you are scored
A hidden verifier reads your submitted `phonon_stability.json` and `refractive_indices.json`. It compares your reported quantities against independently derived reference values for each compound. The final score is a weighted combination:
- Phonon stability evaluation (40% of total reward): whether the imaginary‑modes flag and the minimum frequency match the reference stability criteria.
- Birefringence evaluation (60% of total reward): how closely your computed birefringence values agree with the reference values, within prescribed tolerances.

The verifier does not merely check that the files exist or are well‑formed; it assesses the substantive correctness of the physical results. The reference criteria are not disclosed.
