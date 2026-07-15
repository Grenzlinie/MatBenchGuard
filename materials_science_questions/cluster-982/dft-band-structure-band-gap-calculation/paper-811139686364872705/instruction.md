# Biaxial Strain Tuning of Si46 Band Gap and Optical Absorption - DFT Reproduction

## Problem background
Silicon clathrates are cage-like allotropes of silicon with potential for optoelectronic and photovoltaic applications. Type-I guest-free Si46 has an indirect band gap, which limits its light absorption efficiency. This task investigates whether applying biaxial strain (compressive or tensile) to Si46 can alter its electronic band structure, potentially converting the indirect gap to a direct one and improving optical absorption in the visible spectrum.

## Approach
First-principles calculations based on Density Functional Theory (DFT) with the GGA-PBE functional will be used to simulate the effect of biaxial strain. The workflow constructs the initial Si46 unit cell, relaxes the unstrained structure to obtain the equilibrium lattice constant, then systematically applies in-plane biaxial strains from -4% to +4%. For each strain, the out-of-plane lattice parameter and internal coordinates are relaxed, and the electronic band structure along a high-symmetry path is computed. The band gap and the position of the valence band maximum (VBM) and conduction band minimum (CBM) are extracted to determine whether the gap is direct or indirect. For selected strains, the optical absorption coefficient is derived from the dielectric function, and the maximum absorption in the 1–4 eV range is identified. The open-source DFT package Quantum ESPRESSO serves as the computational engine.

## Reproduction target
The goal is to produce two scored results:
1. For each biaxial strain from -4% to +4%, report the band gap (in eV) and whether the gap is direct (VBM and CBM at the same k-point) in the file `band_gap_vs_strain.csv`. The strain at which a direct band gap appears (if any) must be determined from these calculations.
2. For strains -4%, 0%, and +4%, report the maximum optical absorption coefficient (in consistent units) in the photon energy window 1–4 eV in `absorption_max.csv`. The result should show whether tensile strain enhances the visible-range absorption compared to the unstrained case.
Both artifacts must be computed from the DFT procedure described in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Si pseudopotential (PBE, efficiency or precision): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Optimize unstrained Si46 structure
- Role: process
- Action: Build the initial Si46 unit cell using literature atomic positions (space group Pm-3n) and lattice parameter 10.055 Å; perform a variable-cell relaxation with GGA-PBE to obtain the equilibrium lattice constant a0 and internal coordinates. Use the open-source DFT code Quantum ESPRESSO and a suitable Si pseudopotential.
- Evidence: `/app/outputs/optimized_cell.txt`

### Step 2: Biaxial strain relaxation and band structure calculations
- Role: process
- Action: For each strain ε = -4, -3, -2, -1, 0, 1, 2, 3, 4 %, build the strained cell (in-plane a = a0*(1+ε), fix a=b), relax out-of-plane c and internal coordinates with BFGS; then perform a self-consistent field (SCF) calculation followed by a non-self-consistent bands calculation along a high-symmetry path (e.g., X–R–M–Γ–R) using GGA-PBE. Collect all eigenvalues and relaxation outputs.
- Evidence: `/app/outputs/band_structure_data.zip`

### Step 3: Extract band gap and directness
- Role: scored (load-bearing)
- Action: From the eigenvalues produced in step2, locate VBM and CBM k‑points, compute the band gap (E_CBM - E_VBM), and determine if the gap is direct (VBM and CBM at the same k‑point). Write the results to band_gap_vs_strain.csv.
- Output file: `/app/outputs/band_gap_vs_strain.csv`
- Format: csv
- Contract: Columns: strain (int, e.g., -4, -3, ..., 4), gap_eV (float), is_direct (boolean). Rows in order of increasing strain.
- Scoring: scored by hidden verifier

### Step 4: Compute optical absorption for selected strains
- Role: process
- Action: For strains -4%, 0%, +4%, using the relaxed cells from step2, compute the imaginary part of the dielectric function using GGA-PBE with dense k‑point sampling, and derive the optical absorption coefficient α(ω). Store raw optical data.
- Evidence: `/app/outputs/optical_raw.zip`

### Step 5: Extract absorption maximum
- Role: scored
- Action: From the optical data, extract the maximum value of the absorption coefficient in the photon energy range 1–4 eV for each strain and write absorption_max.csv.
- Output file: `/app/outputs/absorption_max.csv`
- Format: csv
- Contract: Columns: strain (int, -4, 0, 4), absorption_max (float, consistent arbitrary or cm⁻¹ units).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_vs_strain.csv`
- `/app/outputs/absorption_max.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_vs_strain.csv
- path: `/app/outputs/band_gap_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap magnitude and direct/indirect nature for each biaxial strain from -4% to +4%. Rows in order of increasing strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `gap_eV`, `is_direct`
  - `units`:
    - `strain`: %
    - `gap_eV`: eV

### absorption_max.csv
- path: `/app/outputs/absorption_max.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum optical absorption coefficient in the photon energy window 1–4 eV for strains -4%, 0%, +4%.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `absorption_max`
  - `units`:
    - `strain`: %
    - `absorption_max`: cm⁻¹ or a.u.

Notes: The hidden checker compares band gaps against the paper's reported GGA-PBE values within a tolerance and verifies that the direct-gap transition occurs at strains >= +2%. For absorption, the checker verifies that the maximum at +4% is at least 10% larger than at 0% (unstrained).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "gap_eV",
          "is_direct"
        ],
        "units": {
          "strain": "%",
          "gap_eV": "eV"
        }
      },
      "description": "Band gap magnitude and direct/indirect nature for each biaxial strain from -4% to +4%. Rows in order of increasing strain."
    },
    {
      "file": "absorption_max.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "absorption_max"
        ],
        "units": {
          "strain": "%",
          "absorption_max": "cm⁻¹ or a.u."
        }
      },
      "description": "Maximum optical absorption coefficient in the photon energy window 1–4 eV for strains -4%, 0%, +4%."
    }
  ],
  "notes": "The hidden checker compares band gaps against the paper's reported GGA-PBE values within a tolerance and verifies that the direct-gap transition occurs at strains >= +2%. For absorption, the checker verifies that the maximum at +4% is at least 10% larger than at 0% (unstrained)."
}
```

## How you are scored
A hidden verifier will independently score each output file. For `band_gap_vs_strain.csv`, it compares your computed band gaps to reference values (within an appropriate tolerance) and checks the correctness of the direct/indirect classification. For `absorption_max.csv`, it verifies that the absorption maximum at +4% strain exceeds a required threshold relative to the unstrained value. The verifier combines these scores into a single reward in [0,1], with the band gap trend and direct/indirect transition carrying the dominant weight. Simply reporting numbers without performing the DFT workflow will not earn high rewards, as the checker may also cross-validate against intermediate raw data when provided.
