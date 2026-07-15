# DFT+U effective mass calculation of a 2DEG at an oxide interface

## Problem background
A two-dimensional electron gas (2DEG) forms at the interface between the band insulator SrTiO3 (STO) and the Mott insulator LaTiO3 (LTO) despite each individual material having low native conductivity. When a STO/LTO heterostructure is grown on Si(001), the interface hosts charge carriers with moderate density and mobility, making it a candidate for oxide electronic devices. Density functional theory (DFT) with a Hubbard U correction is used to characterize the electronic bands that give rise to the 2DEG. A critical quantity for modeling carrier dynamics, such as the THz response, is the effective mass of the Ti 3d_{xy} conduction bands at the interface. The objective is to compute these effective masses from first‑principles band structure calculations.

## Approach
Spin‑polarized DFT+U calculations are performed on a slab model of the STO/LTO/STO heterostructure on a reconstructed Si(001) substrate. The slab includes a few monolayers of each oxide, a vacuum region, and hydrogen passivation of the bottom Si surface. The exchange‑correlation functional is PBE (generalized gradient approximation) with an on‑site Hubbard U correction on the Ti 3d states (U_eff = 5 eV) to account for strong correlation effects; antiferromagnetic ordering is imposed on the LTO layers. After relaxing the atomic positions, a non‑self‑consistent band structure calculation is carried out along the high‑symmetry paths Γ–M and Γ–X. The conduction bands with dominant Ti d_{xy} character at the LTO/STO interface are identified, and their energy eigenvalues are extracted. The effective mass in each direction is then obtained by fitting a parabola to the band dispersion near the Γ point. The workflow uses an open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) with standard PAW pseudopotentials.

## Reproduction target
Run the DFT+U slab calculation as described. From the completed calculation, extract the raw band energies along Γ–M and Γ–X for the Ti d_{xy} conduction band (or bands) that form the 2DEG at the LTO/STO interface. Save these energies, together with the corresponding k‑point distances, to the file `band_structure.json` (energies in eV relative to the Fermi level, k‑point distances in 1/Å). Do not report the effective masses directly; the verifier will recompute them from the band structure data you provide. The task is to produce the physical band dispersion that yields the correct effective masses upon parabolic fitting.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP precision PAW pseudopotentials: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: DFT+U slab calculation and band structure
- Role: process
- Action: Build the STO/LTO/STO/Si(001) slab model as described (p(2×2) lateral cell, 1 ML STO cap, 2 ML LTO, 3 ML STO on 9 ML reconstructed Si(001) with SrO termination and H passivation, 30 Å vacuum, in-plane lattice constant 5.43 Å). Perform spin-polarized DFT+U calculation using an open-source code (e.g., Quantum ESPRESSO) with PBE functional, Hubbard U on Ti (U_eff=5 eV), plane-wave basis, antiferromagnetic ordering for LTO layers. Include ionic relaxation and a subsequent non-self-consistent band structure calculation along Γ-M and Γ-X high-symmetry paths. Record a brief completion log.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 2: Extract Ti d_{xy} conduction band energies
- Role: scored (load-bearing)
- Action: From the completed DFT calculation, identify the conduction bands with Ti d_{xy} character that cross the Fermi level at the LTO/STO interface. Extract the band eigenvalues for the lowest such band (or an appropriately averaged band) along Γ-M and Γ-X. Write the band structure data to band_structure.json with k-point distances in 1/Å and energies in eV relative to the Fermi level.
- Output file: `/app/outputs/band_structure.json`
- Format: json
- Contract: {
  "Gamma_M": {
    "kpoints": [number, ...],         // distances along Γ-M in 1/Å
    "energies_ev": [number, ...]     // band energies in eV (E_F = 0)
  },
  "Gamma_X": {
    "kpoints": [number, ...],         // distances along Γ-X in 1/Å
    "energies_ev": [number, ...]
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure.json
- path: `/app/outputs/band_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band energies along Γ-M and Γ-X for the Ti d_{xy} conduction band(s). The checker fits a parabola around Γ to recompute effective masses and compares them to the paper-reported reference within tolerance.
- schema:
  - `type`: object
  - `required`: `Gamma_M`, `Gamma_X`
  - `properties`:
    - `Gamma_M`:
      - `kpoints`: array of float (unit: 1/Å)
      - `energies_ev`: array of float (unit: eV)
    - `Gamma_X`:
      - `kpoints`: array of float (unit: 1/Å)
      - `energies_ev`: array of float (unit: eV)

Notes: The agent must perform a full DFT+U relaxation and band structure calculation. The scored file must contain the band energies; the effective masses are not to be reported directly. The checker will recompute them from this raw data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Gamma_M",
          "Gamma_X"
        ],
        "properties": {
          "Gamma_M": {
            "kpoints": "array of float (unit: 1/Å)",
            "energies_ev": "array of float (unit: eV)"
          },
          "Gamma_X": {
            "kpoints": "array of float (unit: 1/Å)",
            "energies_ev": "array of float (unit: eV)"
          }
        }
      },
      "description": "Band energies along Γ-M and Γ-X for the Ti d_{xy} conduction band(s). The checker fits a parabola around Γ to recompute effective masses and compares them to the paper-reported reference within tolerance."
    }
  ],
  "notes": "The agent must perform a full DFT+U relaxation and band structure calculation. The scored file must contain the band energies; the effective masses are not to be reported directly. The checker will recompute them from this raw data."
}
```

## How you are scored
A hidden verifier reads your `band_structure.json` and recomputes the effective masses along Γ–M and Γ–X by fitting a parabola E(k) = ħ²k²/(2m*) to the band data near the Γ point. These recomputed masses are compared to a trusted reference with an appropriate tolerance that accounts for differences arising from the choice of DFT code, pseudopotentials, and convergence settings. The reward increases as the agreement improves, up to a maximum when the recomputed values fall within the tolerance. You are not required to output the effective masses yourself; the scoring depends solely on the raw band energies you provide. Therefore, reporting the paper’s numbers without actually performing the calculation will not earn credit.
