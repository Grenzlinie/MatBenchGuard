# DFT Band Gap Calculation for Ba8Si6Sn from First Principles

## Problem background
The ternary Zintl phase Ba8Si6Sn crystallizes in an orthorhombic structure (space group Pbcn) and features isolated Sn anions and Si3 triangles. First-principles electronic-structure calculations can reveal whether this material is metallic or semiconducting and, if a gap exists, predict its magnitude. Density-functional theory (DFT) has been used to address this question; the key quantity of interest is the band gap of Ba8Si6Sn obtained from such calculations.

## Approach
The electronic structure is computed with plane-wave DFT using the generalized gradient approximation (PBE exchange-correlation functional) and pseudopotentials to describe the ions. The starting point is the experimental crystal structure (lattice constants and atomic positions). A self-consistent field (SCF) run yields the ground-state charge density; a subsequent non-self-consistent band-structure calculation along a high-symmetry k-point path gives the band energies. The valence band maximum (VBM) and conduction band minimum (CBM) are located, and the band gap is the energy difference between them. The gap is classified as direct if the VBM and CBM occur at the same k-point, otherwise indirect.

## Reproduction target
Using the crystal structure data below, set up and run a plane-wave DFT calculation with the PBE functional. Determine the band gap of Ba8Si6Sn and report whether it is direct or indirect. Output a single JSON file (`/app/outputs/bandgap.json`) with the gap in eV and the direct/indirect flag.

Crystal structure:
- Space group: Pbcn (No. 60)
- Lattice parameters: a = 8.7739 Å, b = 8.7599 Å, c = 27.162 Å
- Atomic coordinates (fractional):
  Ba(1)  0.0490  0.3207  0.4136
  Ba(2)  0.1854  0.0088  0.1865
  Ba(3)  0.2115  0.0065  0.0218
  Ba(4)  0.3246  0.1305  0.3246
  Sn(1)  0.0     0.3252  0.25
  Si(1)  0.3671  0.2320  0.1080
  Si(2)  0.5603  0.2065  0.0456
  Si(3)  0.5716  0.4248  0.1008

## Assets

- Plane-wave DFT code (e.g. Quantum ESPRESSO): https://www.quantum-espresso.org
- PBE pseudopotentials (e.g. SSSP efficiency library): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Setup DFT inputs from crystal structure
- Role: process
- Action: Using the provided crystal structure of Ba8Si6Sn (space group Pbcn, a=8.7739 Å, b=8.7599 Å, c=27.162 Å, and atomic coordinates of Ba, Si, Sn), create input files for a plane-wave DFT code that define the unit cell, atomic positions, k-point grid, pseudopotentials, and a high-symmetry k-path covering the orthorhombic Brillouin zone.
- Evidence: none

### Step 2: Compute band structure and band gap
- Role: scored (load-bearing)
- Action: Run the DFT band-structure calculation using the inputs from the previous step. Compute the band energies along the chosen high-symmetry path, locate the valence band maximum (VBM) and conduction band minimum (CBM), and extract the band gap (in eV) and direct/indirect character. Write the result to bandgap.json.
- Output file: `/app/outputs/bandgap.json`
- Format: json
- Contract: {"band_gap_eV": number, "is_direct": boolean, "vbm_kpoint": [float, float, float] (optional), "cbm_kpoint": [float, float, float] (optional)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap.json
- path: `/app/outputs/bandgap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gap value, direct/indirect character, and optionally VBM/CBM k-point coordinates for Ba8Si6Sn obtained from DFT.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number (float, eV)
    - `is_direct`: boolean
  - `items`:
    - `vbm_kpoint`: [float, float, float] (optional)
    - `cbm_kpoint`: [float, float, float] (optional)

Notes: The band gap is expected to be small but positive. The reported value will be compared to the paper's reported band gap within a tolerance, and semiconducting behavior (gap > 0.01 eV) checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number (float, eV)",
          "is_direct": "boolean"
        },
        "items": {
          "vbm_kpoint": "[float, float, float] (optional)",
          "cbm_kpoint": "[float, float, float] (optional)"
        }
      },
      "description": "Band gap value, direct/indirect character, and optionally VBM/CBM k-point coordinates for Ba8Si6Sn obtained from DFT."
    }
  ],
  "notes": "The band gap is expected to be small but positive. The reported value will be compared to the paper's reported band gap within a tolerance, and semiconducting behavior (gap > 0.01 eV) checked."
}
```

## How you are scored
A hidden verifier reads your `bandgap.json` and compares the `band_gap_eV` field against a reference value (the reference is not disclosed). The comparison uses an absolute tolerance; if your computed gap is within the tolerance you receive full credit for that check. The verifier also verifies that `band_gap_eV` is positive, confirming semiconducting behavior, and that the JSON file has the correct structure. The `is_direct` flag and k‑point coordinates are validated for syntactic correctness but do not directly contribute to the score. The total reward is a weighted combination of the gap check, the positivity check, and the schema conformance. Simply reporting a plausible number without actually running the DFT workflow will not satisfy the verifier.
