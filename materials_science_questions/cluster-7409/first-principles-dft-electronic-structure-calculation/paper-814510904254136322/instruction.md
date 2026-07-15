# DFT Electronic Structure of C- and P-Doped ZnO

## Problem background
ZnO is a promising material for photoelectrochemical water splitting due to its high electron mobility and favorable band-edge positions. However, its wide band gap (3.2 eV) limits light absorption to the ultraviolet region. Substitutional doping with non-metal elements such as carbon or phosphorus can introduce isolated impurity states in the band gap, potentially extending absorption into the visible range and enhancing photocatalytic activity. Density functional theory (DFT) calculations can predict the electronic structure of such doped systems and quantify the positions of dopant-induced states. The task is to compute the energies of these impurity states, the resulting band gaps, and whether the materials retain a direct gap at the Gamma point, providing a quantitative understanding of the doping effects.

## Approach
Use first-principles spin-polarized DFT with the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation (GGA). To improve the description of Zn 3d states, apply a Hubbard U correction of U = 4 eV on the Zn d orbitals (GGA+U). Build 2×2×2 supercells of wurtzite ZnO containing 32 atoms. For the doped cases, replace one O atom with C (C-doped) or P (P-doped), corresponding to a doping concentration of 6.25 at.%. After constructing the initial geometries, perform a full geometry relaxation for each supercell until forces and stresses are converged. Then, run a self-consistent field (SCF) calculation to obtain the charge density, compute the band structure along a high-symmetry path that includes the Gamma point, and calculate the partial density of states (PDOS). From these results, extract the energy positions of the impurity states relative to the O 2p valence band maximum (VBM), the band gaps, and the character of the band gap (direct or indirect) at the Gamma point for pure, C-doped, and P-doped ZnO.

## Reproduction target
Compute the electronic structure of pure wurtzite ZnO as well as C‑doped and P‑doped ZnO (both at 6.25 at.%). Specifically, determine: (i) for pure ZnO, the band gap and whether the valence band maximum and conduction band minimum are both at the Gamma point (direct gap); (ii) for C‑doped ZnO, the energy of the isolated C 2p‑derived impurity state above the O 2p VBM, the band gap, and whether the gap is direct at Gamma; (iii) for P‑doped ZnO, the energy of the P 3p‑derived impurity state above the O 2p VBM, its band gap, and direct gap character. Report all results in the JSON file `electronic_properties.json` following the specified schema.

## Assets

- Quantum ESPRESSO (or any DFT code with GGA+U capability): https://www.quantum-espresso.org/
- Wurtzite ZnO crystal structure

## Workflow steps

### Step 1: Build initial supercell models
- Role: process
- Action: Construct 32-atom (2×2×2) supercells of wurtzite ZnO (pure), and substitutional doped variants: replace one O atom with C (C-doped) and one O with P (P-doped), yielding 6.25 at.% doping concentration.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Geometry optimization
- Role: process
- Action: Perform DFT geometry relaxation for the pure, C-doped, and P-doped supercells. Use GGA+U with U=4 eV on Zn d orbitals. Converge forces and stresses.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Electronic structure calculation
- Role: process
- Action: For each relaxed structure (pure, C-doped, P-doped), run SCF calculation, compute band structure along a high-symmetry path including the Gamma point, and compute partial density of states (PDOS).
- Evidence: `/app/outputs/electronic_output.log`

### Step 4: Extract and report electronic properties
- Role: scored (load-bearing)
- Action: From the obtained band structures and PDOS: (i) for pure ZnO, determine the band gap and whether VBM and CBM are at the Gamma point; (ii) for C-doped ZnO, find the energy of the isolated C 2p-derived state relative to the host O 2p valence band maximum (VBM), the band gap, and whether the gap remains direct at Gamma; (iii) for P-doped ZnO, similarly extract the P 3p impurity state energy, band gap, and direct gap character. Write all results to electronic_properties.json.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: {"C_impurity_energy_above_vbm": float, "P_impurity_energy_above_vbm": float, "pure_bandgap": float, "C_bandgap": float, "P_bandgap": float, "direct_gap_pure": bool, "direct_gap_C": bool, "direct_gap_P": bool}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted electronic properties: impurity state energies relative to O 2p VBM, band gaps, and direct gap character for pure, C-doped, and P-doped ZnO.
- schema:
  - `type`: object
  - `required`:
    - `C_impurity_energy_above_vbm`: float (eV)
    - `P_impurity_energy_above_vbm`: float (eV)
    - `pure_bandgap`: float (eV)
    - `C_bandgap`: float (eV)
    - `P_bandgap`: float (eV)
    - `direct_gap_pure`: bool
    - `direct_gap_C`: bool
    - `direct_gap_P`: bool

Notes: Checkers will compare each numeric quantity to hidden paper-reported gold values with appropriate tolerances (impurity energies ±0.1 eV, band gaps ±0.05 eV) and exact boolean match for direct gap flags. Charge density plots are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C_impurity_energy_above_vbm": "float (eV)",
          "P_impurity_energy_above_vbm": "float (eV)",
          "pure_bandgap": "float (eV)",
          "C_bandgap": "float (eV)",
          "P_bandgap": "float (eV)",
          "direct_gap_pure": "bool",
          "direct_gap_C": "bool",
          "direct_gap_P": "bool"
        }
      },
      "description": "Extracted electronic properties: impurity state energies relative to O 2p VBM, band gaps, and direct gap character for pure, C-doped, and P-doped ZnO."
    }
  ],
  "notes": "Checkers will compare each numeric quantity to hidden paper-reported gold values with appropriate tolerances (impurity energies ±0.1 eV, band gaps ±0.05 eV) and exact boolean match for direct gap flags. Charge density plots are not required."
}
```

## How you are scored
A hidden verifier reads your `electronic_properties.json` output file. It compares each numeric quantity (impurity state energies and band gaps) to a hidden reference value with an appropriate tolerance, and checks each boolean direct‑gap flag exactly. Your final reward is a weighted combination of these comparisons. Simply reporting textbook or paper values without running the required DFT workflow will not yield the correct numbers; you must execute the full pipeline to produce the results.
