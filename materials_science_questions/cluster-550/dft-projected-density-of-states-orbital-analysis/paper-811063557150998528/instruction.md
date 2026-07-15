# DFT Band Gap and Orbital Analysis of Double Perovskites A2SmTaO6

## Problem background
Double perovskite oxides of the form A2SmTaO6 (A = Ba, Sr, Ca) are candidate materials for microwave dielectric applications. The electronic structure—specifically the band gap and the orbital character at the band edges—governs important electrical properties. Systematic first‑principles calculations of the density of states and band gaps for these compounds have not been widely reported.

## Approach
Use spin‑polarized density functional theory (DFT) with the GGA+U approximation, applying an on‑site Coulomb U correction on Sm 4f states, to compute the electronic structure from first principles. Start from the experimental crystal structures (provided), perform ionic relaxation to obtain the ground‑state geometries, then compute the total and projected density of states (Sm 4f, Ta 5d, O 2p) and the direct band gap at the Gamma point for the up‑spin channel. Extract the dominant orbital contributions at the valence band maximum and conduction band minimum.

## Reproduction target
Perform spin‑polarized GGA+U calculations (U = 7 eV on Sm 4f) for Ba2SmTaO6 (BST), Sr2SmTaO6 (SST), and Ca2SmTaO6 (CST), starting from the provided crystal structures. Compute the direct band gap (up‑spin channel) at the Γ point for each compound and record the results in band_gaps.json. Also produce a text file (dos_analysis.txt) that describes the orbital character at the valence band maximum (expected to be dominated by O 2p hybridized with Sm 4f and Ta 5d) and at the conduction band minimum (expected to be dominated by Ta 5d).

## Assets

- Crystal structure data for BST, SST, CST from Table I
- DFT code (Quantum ESPRESSO optional or VASP if licensed): https://www.quantum-espresso.org
- PAW pseudopotentials for Ba, Sr, Ca, Sm, Ta, O: bundled with Quantum ESPRESSO

## Workflow steps

### Step 1: Ionic relaxation for BST, SST, CST
- Role: process
- Action: Perform ionic relaxation for each compound using spin-polarized GGA+U (U=7 eV on Sm 4f). Start from experimental lattice parameters and atomic coordinates of Table I. Converge total energy and forces until stable relaxed geometries are obtained.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Calculate DOS and direct band gaps
- Role: scored (load-bearing)
- Action: From the relaxed geometries, compute spin-polarized total and projected density of states (Sm 4f, Ta 5d, O 2p) for BST, SST, CST. Determine the direct band gap at the Gamma point for the up-spin channel.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"BST": float, "SST": float, "CST": float}
- Scoring: scored by hidden verifier

### Step 3: Report orbital character analysis
- Role: scored
- Action: Based on the projected DOS, write a text summary describing the dominant orbital contributions at the valence band maximum (VBM) and conduction band minimum (CBM) for each compound.
- Output file: `/app/outputs/dos_analysis.txt`
- Format: txt
- Contract: Must mention O 2p + Sm 4f + Ta 5d at VBM, and Ta 5d at CBM.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/dos_analysis.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gap values for BST, SST, CST computed from spin-polarized GGA+U DFT.
- schema:
  - `type`: object
  - `required`:
    - `BST`: float (eV)
    - `SST`: float (eV)
    - `CST`: float (eV)
  - `items`: object
  - `units`:
    - `BST`: eV
    - `SST`: eV
    - `CST`: eV

### dos_analysis.txt
- path: `/app/outputs/dos_analysis.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Orbital character analysis at VBM and CBM from projected DOS.
- schema:
  - `type`: text
  - `required`:
    - `presence`: keywords O 2p, Sm 4f, Ta 5d, VBM, CBM

Notes: Band gaps are compared to the paper's reported values within a hidden tolerance. The text file is checked for presence of required orbital character keywords.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BST": "float (eV)",
          "SST": "float (eV)",
          "CST": "float (eV)"
        },
        "items": {},
        "units": {
          "BST": "eV",
          "SST": "eV",
          "CST": "eV"
        }
      },
      "description": "Direct band gap values for BST, SST, CST computed from spin-polarized GGA+U DFT."
    },
    {
      "file": "dos_analysis.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "presence": "keywords O 2p, Sm 4f, Ta 5d, VBM, CBM"
        }
      },
      "description": "Orbital character analysis at VBM and CBM from projected DOS."
    }
  ],
  "notes": "Band gaps are compared to the paper's reported values within a hidden tolerance. The text file is checked for presence of required orbital character keywords."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that evaluates each output file. For band_gaps.json, the verifier checks that the three band gap values are physically reasonable and match expected values (the exact tolerance is hidden). For dos_analysis.txt, it verifies that the required orbital character keywords (O 2p, Sm 4f, Ta 5d at the VBM; Ta 5d at the CBM) are present and correctly assigned. The final reward is a weighted combination of these checks.
