# DFT study of di-Frenkel pair magnetism in anatase TiO2

## Problem background
Low-energy ion irradiation of anatase TiO₂ can induce a ferromagnetic surface layer with perpendicular magnetic anisotropy. Density functional theory (DFT) calculations are used to investigate whether di-Frenkel pair (di‑FP) defect configurations — pairs of titanium vacancies and interstitials — can produce a stable net magnetic moment and magnetocrystalline anisotropy in anatase. The goal is to compute the magnetic and energetic properties of two specific defect geometries, di‑FP1 and di‑FP2, embedded in a 3×3×1 anatase supercell.

## Approach
Spin‑polarised DFT within the PBE+U framework (U = 4 eV on Ti 3d) is employed to relax the atomic structures of the di‑FP1 and di‑FP2 supercells and obtain their ground‑state spin densities. From the relaxed di‑FP1 structure, non‑collinear spin‑orbit coupling calculations are performed to determine the magnetocrystalline anisotropy energy. All calculations use an open‑source DFT code (Quantum ESPRESSO) and publicly available pseudopotentials. The workflow proceeds in four stages: (1) generate the initial defect supercells with prescribed interatomic distances; (2) relax both supercells with spin‑polarised DFT; (3) compute total energies for magnetisation along the x, y, and z axes for di‑FP1; and (4) extract and report the key magnetic properties — total magnetic moment per supercell, local atomic moments on the inequivalent Ti and O sites, the total energy difference between the two defect configurations, and the magnetocrystalline anisotropy energy differences.

## Reproduction target
The task is to compute the following quantities for the di‑FP1 and di‑FP2 defect configurations using the DFT protocol described: (a) the integrated total magnetic moment per supercell in μ_B; (b) the local atomic magnetic moments on the Ti interstitials I1 and I2 in di‑FP1, and on Ti interstitial I1 and the spin‑polarised O atom in di‑FP2; (c) the total energy of each defect supercell and the energy difference ΔE(di‑FP2 − di‑FP1) per formula unit in meV; and (d) the magnetocrystalline anisotropy energy differences ΔE(z−x) and ΔE(z−y) for di‑FP1 in meV. Report all results in a single JSON file, `/app/outputs/summary_results.json`, conforming to the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (Ti and O): https://www.materialscloud.org/discover/sssp/table/pseudopotentials
- Anatase TiO2 crystal structure: https://www.crystallography.net/cod/5000224.html

## Workflow steps

### Step 1: Generate di‑FP1 and di‑FP2 supercells
- Role: process
- Action: Construct 3×3×1 anatase supercells containing the di‑Frenkel pair configurations di‑FP1 and di‑FP2 with the exact interatomic distances specified in the paper: for di‑FP1 d_V1‑V2 = 3.03 Å, d_V1‑I1 = d_V2‑I2 = 5.97 Å, d_I1‑I2 = 6.52 Å; for di‑FP2 d_V1‑V2 = 4.96 Å, d_V1‑I1 = 5.75 Å, d_V2‑I2 = 5.95 Å, d_I1‑I2 = 3.81 Å. Define the atomic positions accordingly as initial structures for DFT calculations.
- Evidence: none

### Step 2: Relax di‑FP1 and di‑FP2 with spin‑polarized DFT
- Role: process
- Action: Perform spin‑polarized DFT structural relaxation for both di‑FP1 and di‑FP2 supercells using PBE+U (U=4 eV on Ti 3d), a plane‑wave energy cutoff of 600 eV, a Γ‑centered 2×2×3 k‑point mesh, and force convergence below 10 meV/Å. Keep the cell volume fixed. The relaxation must produce the final relaxed geometries and the converged spin density.
- Evidence: none

### Step 3: Magnetocrystalline anisotropy for di‑FP1
- Role: process
- Action: Using the relaxed di‑FP1 geometry, perform non‑collinear spin‑orbit coupling DFT calculations to obtain total energies for magnetization directions along the crystallographic x, y, and z axes. Use the same PBE+U functional and comparable cutoff/k‑mesh as in the relaxation step.
- Evidence: none

### Step 4: Extract magnetic and energetic properties
- Role: scored (load-bearing)
- Action: From the DFT outputs of steps 2 and 3, compute: (a) the total magnetic moment per supercell by integrating the spin density; (b) the local atomic magnetic moments on the specified atoms (Ti interstitials I1 and I2 in di‑FP1, I1 and the polarized O atom in di‑FP2); (c) the total energy difference per formula unit between di‑FP1 and di‑FP2; (d) the magnetocrystalline anisotropy energies ΔE_z‑x and ΔE_z‑y of di‑FP1. Write all results into summary_results.json.
- Output file: `/app/outputs/summary_results.json`
- Format: json
- Contract: Object with keys: total_moment_muB (float), local_moments (object with keys 'di_fp1' and 'di_fp2', each containing a list of {atom_site_description: string, moment_muB: float}), di_fp1_energy_eV (float), di_fp2_energy_eV (float), energy_diff_meV_per_fu (float), anisotropy_meV_z_x (float), anisotropy_meV_z_y (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/summary_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### summary_results.json
- path: `/app/outputs/summary_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed magnetic moments, energies, and magnetocrystalline anisotropy energy differences for di‑FP1 and di‑FP2 defect configurations in anatase TiO2.
- schema:
  - `type`: object
  - `required`:
    - `total_moment_muB`: float (Bohr magnetons)
    - `local_moments`: object with keys di_fp1 and di_fp2, each an array of objects with keys atom_site_description (string) and moment_muB (float)
    - `di_fp1_energy_eV`: float (eV)
    - `di_fp2_energy_eV`: float (eV)
    - `energy_diff_meV_per_fu`: float (meV per formula unit)
    - `anisotropy_meV_z_x`: float (meV)
    - `anisotropy_meV_z_y`: float (meV)

Notes: The hidden checker compares each reported value to the paper‑reported reference with tolerances appropriate for typical DFT code/functional differences (±0.2 μB for moments, ±10 meV for energy difference, ±0.02 meV for anisotropy energies). Only the summary_results.json is scored; the evidence directories are for process transparency and are not graded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "summary_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "total_moment_muB": "float (Bohr magnetons)",
          "local_moments": "object with keys di_fp1 and di_fp2, each an array of objects with keys atom_site_description (string) and moment_muB (float)",
          "di_fp1_energy_eV": "float (eV)",
          "di_fp2_energy_eV": "float (eV)",
          "energy_diff_meV_per_fu": "float (meV per formula unit)",
          "anisotropy_meV_z_x": "float (meV)",
          "anisotropy_meV_z_y": "float (meV)"
        }
      },
      "description": "Computed magnetic moments, energies, and magnetocrystalline anisotropy energy differences for di‑FP1 and di‑FP2 defect configurations in anatase TiO2."
    }
  ],
  "notes": "The hidden checker compares each reported value to the paper‑reported reference with tolerances appropriate for typical DFT code/functional differences (±0.2 μB for moments, ±10 meV for energy difference, ±0.02 meV for anisotropy energies). Only the summary_results.json is scored; the evidence directories are for process transparency and are not graded."
}
```

## How you are scored
A hidden verifier evaluates your submission by reading the scored artifact, `/app/outputs/summary_results.json`, and comparing each reported value to a hidden reference set that is derived from the original DFT study. The comparison uses tolerances that account for typical variability when the same protocol is executed with a different DFT code and pseudopotentials. Full credit is awarded when your computed total magnetic moment, local moments, energy difference, and anisotropy energies fall within the acceptable windows. The intermediate evidence (relaxed structures, spin‑orbit calculation outputs) is expected as proof that the workflow was executed, but only the summary_results.json is scored. The verifier combines the scores for each field into a single overall reward; you must genuinely run the DFT calculations to obtain values that lie within the tolerated range.
