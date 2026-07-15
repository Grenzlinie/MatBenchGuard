# DFT band structure and PDOS analysis of a Cd-based coordination polymer

## Problem background
Coordination polymers (CPs) are hybrid inorganic-organic materials with potential applications in electronic and optoelectronic devices. Understanding their electronic band structure and the atomic-orbital character of the band edges is essential for elucidating charge-transport mechanisms. This task focuses on a cadmium-based CP containing acetylenedicarboxylate (adc) linkers, 4-phenylpyridine (4-phpy) co-ligands, and coordinated water. Using density functional theory (DFT), the electronic properties of this compound — the Kohn–Sham band energies, the band gap (type and magnitude), and the partial density of states (PDOS) — are to be computed to reveal which atoms and which orbitals dominate the valence-band maximum and conduction-band minimum.

## Approach
The reproduction replaces the original proprietary DFT code with the open-source plane-wave code Quantum ESPRESSO, using the same level of theory: the Perdew–Burke–Ernzerhof (PBE) generalized-gradient functional, norm-conserving pseudopotentials, and a Grimme dispersion correction. Starting from the experimental crystal structure, atomic positions are relaxed while the lattice parameters are kept fixed. With the relaxed structure, a self‑consistent ground-state DFT calculation is performed, followed by a non-self‑consistent band structure calculation along the high-symmetry k‑path G → F → Q → Z. The partial density of states is computed and projected onto s, p, and d orbitals of the distinct chemical species (Cd, adc, 4‑phpy, water). From the raw band energies the valence-band maximum (VBM) and conduction-band minimum (CBM) are identified, the raw band gap is extracted, and a scissor shift of +0.45 eV is applied to obtain the adjusted gap. The PDOS data are integrated to quantify the fractional orbital contributions at the band edges, revealing which atoms and orbital types dominate the top of the valence band and the bottom of the conduction band.

## Reproduction target
For the given Cd‑based coordination polymer (compound 1), produce the following two scored artifacts:

1. **Band-structure summary** (`band_structure_results.json`):
   - Kohn–Sham band energies (in eV, relative to the Fermi level) for each k‑point along the path G(0,0,0) → F(0,0.5,0) → Q(0,0.5,0.5) → Z(0,0,0.5).
   - The Fermi energy, VBM energy, CBM energy, and raw band gap (CBM − VBM).
   - After applying a scissor shift of +0.45 eV to the conduction bands, report the adjusted band gap.
   - The k‑point labels and coordinates where the VBM and CBM occur, and the gap type (direct or indirect).

2. **PDOS summary** (`pdos_summary.json`):
   - For the three highest valence bands and the three lowest conduction bands, compute the fractional contributions of s, p, and d orbitals for each atomic species: Cd, the adc linker, the 4‑phpy ligand, and water. Contributions should be normalised so that the total across all species and orbital types sums to 1 for each band.

The raw data come from Quantum ESPRESSO calculations with PBE functional, norm‑conserving pseudopotentials, a plane‑wave cutoff of 600 eV, and a k‑point grid of 3×3×2 (geometry optimization and ground‑state), and a band‑structure calculation along the specified path with the same settings. Geometry optimization keeps lattice parameters fixed; Grimme dispersion corrections are included.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Cd, O, N, C, H (SSSP precision library or equivalent): https://www.materialscloud.org/discover/sssp/
- Experimental crystal structure of compound 1 (CIF file, CCDC deposition from Ref. 47): 10.1039/C7RA00758B

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Using the experimental crystal structure of compound 1, perform DFT geometry optimization of atomic positions while keeping lattice parameters fixed. Use the PBE functional, norm-conserving pseudopotentials, a plane-wave cutoff of 600 eV, and a k-point grid of 3×3×2. Include Grimme dispersion corrections.
- Evidence: `/app/outputs/geom_opt.log`

### Step 2: Raw band structure and PDOS calculation
- Role: process
- Action: On the optimized structure, perform a ground-state DFT calculation with the same settings as step 1. Then carry out a non-self-consistent band structure calculation along the k-path G(0,0,0) → F(0,0.5,0) → Q(0,0.5,0.5) → Z(0,0,0.5). Compute the partial density of states (PDOS) projected onto s, p, and d atomic orbitals for Cd, adc linker, 4-phpy, and water, using a 3×3×2 k-point grid.
- Evidence: `/app/outputs/bands.dat, pdos.dat`

### Step 3: Band gap analysis
- Role: scored (load-bearing)
- Action: From the raw band structure data, locate the valence band maximum (VBM) and conduction band minimum (CBM), compute the raw band gap (CBM – VBM), apply a scissor shift of +0.45 eV to obtain the adjusted band gap, determine whether the gap is direct or indirect, and identify the k-point labels of VBM and CBM. Output the results as band_structure_results.json.
- Output file: `/app/outputs/band_structure_results.json`
- Format: json
- Contract: JSON object with required keys: 'kpath' (array of objects with 'label' and 'coordinates'), 'band_energies' (2D array of float, shape [n_kpoints, n_bands]), 'fermi_energy' (float, eV), 'vbm_energy' (float, eV), 'cbm_energy' (float, eV), 'raw_band_gap' (float, eV), 'scissor_shift_applied' (float, set to 0.45), 'adjusted_band_gap' (float, eV), 'vbm_kpoint' (object with 'label' and 'coordinates'), 'cbm_kpoint' (object with 'label' and 'coordinates'), 'gap_type' (string, 'direct' or 'indirect').
- Scoring: scored by hidden verifier

### Step 4: Partial density of states analysis
- Role: scored
- Action: Using the PDOS data, compute the fractional orbital contributions (s, p, d) of each atomic species (Cd, adc, 4-phpy, water) for the three highest valence bands and the three lowest conduction bands. Output the summary as pdos_summary.json.
- Output file: `/app/outputs/pdos_summary.json`
- Format: json
- Contract: JSON object with required keys: 'valence_band_top_contributions' (array of objects, each with 'band_index', 'energy' (eV), and 'contributions' {Cd:{s,p,d}, adc:{s,p,d}, '4-phpy':{s,p,d}, water:{s,p,d}}), 'conduction_band_bottom_contributions' (similar structure). The fractional contributions for each atom type should sum to 1 for that band.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure_results.json`
- `/app/outputs/pdos_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure_results.json
- path: `/app/outputs/band_structure_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Derived band structure quantities: band energies along the k-path, VBM/CBM locations, raw and scissored band gap, and gap type.
- schema:
  - `type`: object
  - `required`:
    - `kpath`: array of objects with 'label' (string) and 'coordinates' (array of 3 floats)
    - `band_energies`: 2D array of float (eV), shape [n_kpoints, n_bands]
    - `fermi_energy`: float (eV)
    - `vbm_energy`: float (eV)
    - `cbm_energy`: float (eV)
    - `raw_band_gap`: float (eV)
    - `scissor_shift_applied`: float (should be 0.45)
    - `adjusted_band_gap`: float (eV)
    - `vbm_kpoint`: object with 'label' and 'coordinates'
    - `cbm_kpoint`: object with 'label' and 'coordinates'
    - `gap_type`: string ('direct' or 'indirect')

### pdos_summary.json
- path: `/app/outputs/pdos_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fractional orbital contributions (s,p,d) per atom type for the band edges, used to audit dominant electronic states.
- schema:
  - `type`: object
  - `required`:
    - `valence_band_top_contributions`: array of objects for the three highest valence bands
    - `conduction_band_bottom_contributions`: array of objects for the three lowest conduction bands
  - `items`:
    - `band_index`: integer
    - `energy`: float (eV)
    - `contributions`:
      - `Cd`:
        - `s`: float
        - `p`: float
        - `d`: float
      - `adc`:
        - `s`: float
        - `p`: float
        - `d`: float
      - `4-phpy`:
        - `s`: float
        - `p`: float
        - `d`: float
      - `water`:
        - `s`: float
        - `p`: float
        - `d`: float

Notes: The workflow covers only compound 1 as specified by the minimal reproduction task. The proprietary CASTEP code is replaced by Quantum ESPRESSO with the same functional (PBE), pseudopotential type, and dispersion correction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "kpath": "array of objects with 'label' (string) and 'coordinates' (array of 3 floats)",
          "band_energies": "2D array of float (eV), shape [n_kpoints, n_bands]",
          "fermi_energy": "float (eV)",
          "vbm_energy": "float (eV)",
          "cbm_energy": "float (eV)",
          "raw_band_gap": "float (eV)",
          "scissor_shift_applied": "float (should be 0.45)",
          "adjusted_band_gap": "float (eV)",
          "vbm_kpoint": "object with 'label' and 'coordinates'",
          "cbm_kpoint": "object with 'label' and 'coordinates'",
          "gap_type": "string ('direct' or 'indirect')"
        }
      },
      "description": "Derived band structure quantities: band energies along the k-path, VBM/CBM locations, raw and scissored band gap, and gap type."
    },
    {
      "file": "pdos_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "valence_band_top_contributions": "array of objects for the three highest valence bands",
          "conduction_band_bottom_contributions": "array of objects for the three lowest conduction bands"
        },
        "items": {
          "band_index": "integer",
          "energy": "float (eV)",
          "contributions": {
            "Cd": {
              "s": "float",
              "p": "float",
              "d": "float"
            },
            "adc": {
              "s": "float",
              "p": "float",
              "d": "float"
            },
            "4-phpy": {
              "s": "float",
              "p": "float",
              "d": "float"
            },
            "water": {
              "s": "float",
              "p": "float",
              "d": "float"
            }
          }
        }
      },
      "description": "Fractional orbital contributions (s,p,d) per atom type for the band edges, used to audit dominant electronic states."
    }
  ],
  "notes": "The workflow covers only compound 1 as specified by the minimal reproduction task. The proprietary CASTEP code is replaced by Quantum ESPRESSO with the same functional (PBE), pseudopotential type, and dispersion correction."
}
```

## How you are scored
A hidden verifier checks each scored artifact independently.

- **band_structure_results.json**: The verifier recomputes the raw band gap from the submitted band‑energies array (minimum conduction energy − maximum valence energy) and compares it to a reference value obtained from a Quantum ESPRESSO calculation with the same functional and pseudopotential set. It also verifies that the reported VBM and CBM k‑point labels are the ones expected for this system, and that the adjusted gap equals the raw gap plus the declared scissor shift. Your score for this stage is based on how closely the recomputed gap and the k‑point labels match the reference.

- **pdos_summary.json**: The verifier performs a structural audit. It checks that the fractional contributions are internally consistent (they sum to 1 for each band) and that the dominant orbital characters match the physical expectations for this compound: the top valence bands should be dominated by p‑orbitals from the adc linker and water, with negligible Cd‑d contribution, while the bottom conduction bands should be dominated by p‑orbitals from the 4‑phpy ligands. Correct trends within a tolerance yield full credit; partial credit is awarded for partially correct trends.

The overall reward is a weighted combination of the scores from the two stages, with the band‑gap analysis carrying a larger share. The output contract describes the exact JSON schemas that the verifier expects.
