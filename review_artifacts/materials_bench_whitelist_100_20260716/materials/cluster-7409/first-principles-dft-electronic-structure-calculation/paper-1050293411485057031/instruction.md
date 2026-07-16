# DFT Band Structure of Ti-doped SrNbO3: Fermi-level shift and indirect gap

## Problem background
SrNbO3 is a correlated perovskite with potential as a transparent conductor. Its electronic structure features a metallic ground state with a conduction band dominated by Nb 3d states and a valence band of O 2p character. Ti doping has been proposed to modify the electronic structure by shifting the Fermi level and altering the band gap, but the exact nature of the Fermi-level shift, the indirect/direct character of the fundamental gap, and the orbital composition of the band edges across different Ti concentrations must be quantified by first-principles density-functional theory (DFT) calculations.

## Approach
Use plane-wave DFT with the Perdew-Burke-Ernzerhof (PBE) functional and PAW pseudopotentials to model SrNb1-xTixO3 compositions (x = 0, 0.25, 0.5). Construct a 2×2×2 perovskite supercell of SrNbO3, substitute Nb by Ti to achieve the target compositions, and relax the structures until forces are below 1e-3 eV/Å and total energy converges to 1e-6 eV. Then compute the Kohn-Sham band structure along a suitable high-symmetry k-path (e.g., Γ–X–M–Γ–R–X–M) and unfold the supercell bands to the primitive Brillouin zone. Calculate projected density of states (pDOS) with orbital projections onto O 2p, Nb 3d, and Ti 3d states. For each composition, extract the conduction-band minimum (CBM) energy relative to the Fermi level, the k-points of the valence-band maximum (VBM) and CBM, the nature of the fundamental gap, and the dominant orbital character of VBM and CBM. Report the extracted parameters in a structured summary file.

## Reproduction target
For the three Ti-doped compositions x = 0, 0.25, 0.5, determine from the computed band structures and pDOS: the energy of the conduction-band minimum (CBM) in eV relative to the Fermi level (EF = 0), the k-point coordinates (in units of the reciprocal lattice vectors) of the valence-band maximum (VBM) and CBM, whether the fundamental gap is indirect or direct (based on the k-point locations of VBM and CBM), and the dominant orbital character of the VBM and CBM (identified from the pDOS as O 2p, Nb 3d, or Ti 3d). Write the results in a JSON array as specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency v1.3): https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of SrNbO3 (mp-1087999): https://materialsproject.org/materials/mp-1087999
- Crystal structure of SrTiO3 (mp-2652): https://materialsproject.org/materials/mp-2652
- fold2Bloch: https://github.com/band-unfolding/fold2Bloch

## Workflow steps

### Step 1: Construct supercells and relax structures
- Role: process
- Action: Build 2×2×2 supercells of SrNb1-xTixO3 for x=0, 0.25, 0.5 by substituting Nb with Ti in the SrNbO3 perovskite structure, then relax atomic positions and lattice parameters using PBE functional and PAW pseudopotentials until forces < 1e-3 eV/Å and total energy convergence 1e-6 eV.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Compute electronic structure, band unfolding and pDOS
- Role: process
- Action: For each relaxed supercell, compute Kohn-Sham band structure on a high-symmetry k-path (e.g., Γ–X–M–Γ–R–X–M) using PBE functional and PAW pseudopotentials. Perform band unfolding to the primitive cell (using fold2Bloch or similar). Compute projected density of states (pDOS) with O 2p, Nb 3d, and Ti 3d components. Save intermediate files for the next step.
- Evidence: `/app/outputs/band_unfolded_x0.csv, band_unfolded_x0.25.csv, band_unfolded_x0.5.csv, pdos_total.csv`

### Step 3: Extract key electronic structure parameters
- Role: scored (load-bearing)
- Action: From the computed band structure and pDOS, determine for each composition x=0, 0.25, 0.5: the conduction-band minimum (CBM) energy relative to the Fermi level (E_F=0), the k-point coordinates of the valence-band maximum (VBM) and CBM, the nature of the fundamental gap (indirect or direct), and the dominant orbital characters of VBM and CBM. Write these results to summary.json exactly as per the output contract.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: Array of objects. Each object: { composition: string, cbm_energy: number (eV, float), vbm_kpoint: [number, number, number], cbm_kpoint: [number, number, number], gap_type: string, vbm_orbital: string, cbm_orbital: string }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Extracted electronic and optical parameters for each composition: CBM energy shift, indirect gap character, and plasma frequency.
- schema:
  - `type`: array
  - `items`:
    - `composition`: string
    - `cbm_energy`: number
    - `vbm_kpoint`: `number`, `number`, `number`
    - `cbm_kpoint`: `number`, `number`, `number`
    - `gap_type`: string
    - `vbm_orbital`: string
    - `cbm_orbital`: string
    - `plasma_frequency`: number
  - `required`: `composition`, `cbm_energy`, `vbm_kpoint`, `cbm_kpoint`, `gap_type`, `vbm_orbital`, `cbm_orbital`, `plasma_frequency`

Notes: The checker compares cbm_energy values for x=0 and x=0.5 against paper-reported shifts (≈ -1.3 eV and -0.8 eV) with tolerance ±0.2 eV, verifies gap_type is 'indirect', and checks orbital assignments. For plasma frequency, the checker verifies x=0 around 2.4 eV (±0.3 eV) and x=0.5 ≤ 1.75 eV (shift below visible range).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "composition": "string",
          "cbm_energy": "number",
          "vbm_kpoint": [
            "number",
            "number",
            "number"
          ],
          "cbm_kpoint": [
            "number",
            "number",
            "number"
          ],
          "gap_type": "string",
          "vbm_orbital": "string",
          "cbm_orbital": "string",
          "plasma_frequency": "number"
        },
        "required": [
          "composition",
          "cbm_energy",
          "vbm_kpoint",
          "cbm_kpoint",
          "gap_type",
          "vbm_orbital",
          "cbm_orbital",
          "plasma_frequency"
        ]
      },
      "description": "Extracted electronic and optical parameters for each composition: CBM energy shift, indirect gap character, and plasma frequency."
    }
  ],
  "notes": "The checker compares cbm_energy values for x=0 and x=0.5 against paper-reported shifts (≈ -1.3 eV and -0.8 eV) with tolerance ±0.2 eV, verifies gap_type is 'indirect', and checks orbital assignments. For plasma frequency, the checker verifies x=0 around 2.4 eV (±0.3 eV) and x=0.5 ≤ 1.75 eV (shift below visible range)."
}
```

## How you are scored
A hidden verifier independently inspects each scored artifact produced by the workflow stages. For the final summary.json, the verifier compares the CBM energies and gap-type against reference criteria derived from the underlying physical expectations, and checks the orbital assignments for consistency. Scores from individual stages are combined according to their assigned weights to produce a final reward between 0 and 1. Merely reporting plausible numbers without performing the actual DFT computations is not sufficient; the verifier evaluates the artifacts as evidence of a genuine reproduction workflow.
