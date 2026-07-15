# First‑Principles Band Gap Calculations of Lead Halide Perovskites Using a Novel mBJ Parameterization

## Problem background
Lead halide perovskites have emerged as promising materials for photovoltaic applications. A major challenge in computational modelling is that standard density functional theory (GGA) severely underestimates electronic band gaps, especially when spin-orbit coupling is included. Accurate yet affordable predictions are needed to guide material design. This task addresses the problem by evaluating a specific parameterization of the modified Becke-Johnson (mBJ) exchange potential for six lead halide perovskite semiconductors. The goal is to determine whether this parameterization can produce band gaps that match experimental measurements, thereby offering a practical DFT protocol for these systems.

## Approach
The computational approach is based on density functional theory (DFT) with the modified Becke-Johnson exchange potential. A novel set of parameters (A=0.4, B=1.0, e=0.5) is used to define the exchange potential, and spin-orbit coupling is included. Self-consistent calculations are performed using the experimental crystal structures of the seven compounds (lattice constants and atomic positions from the published literature). Non-self-consistent band structure calculations then yield the electronic eigenvalues from which direct band gaps are extracted at specific high-symmetry k-points determined by each crystal's symmetry. The method can be implemented with any DFT code that supports the mBJ functional and SOC, such as Quantum ESPRESSO.

## Reproduction target
Produce a JSON file `/app/outputs/band_gaps.json` containing the direct band gap (in eV, rounded to three decimal places) for each of the following seven lead halide perovskites, computed with the mBJ parameterization (A=0.4, B=1.0, e=0.5) and spin-orbit coupling: tetragonal CH₃NH₃PbI₃, cubic CH₃NH₃PbBr₃, cubic CsPbCl₃, orthorhombic CsPbBr₃, orthorhombic RbPbI₃, orthorhombic CsPbI₃, and cubic CsPbI₃.

## Assets

- Crystal structures for the seven lead halide perovskites
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Perform DFT calculations with the new mBJ parameterization
- Role: process
- Action: For each of the seven target perovskites (CH₃NH₃PbI₃, CH₃NH₃PbBr₃, CsPbCl₃, CsPbBr₃, RbPbI₃, orthorhombic CsPbI₃, and cubic CsPbI₃), set up and run a self‑consistent density functional theory calculation using the modified Becke‑Johnson exchange potential with parameters A=0.4, B=1.0, e=0.5, and including spin‑orbit coupling. Use the experimental crystal structures (lattice constants from Table I and atomic positions from the cited references). Converge total energy and charge density to high accuracy, and perform a non‑self‑consistent band structure calculation at the end to obtain the electronic eigenvalues.
- Evidence: `/app/outputs/dft_convergence.log`

### Step 2: Extract and report the band gaps
- Role: scored (load-bearing)
- Action: From the completed DFT calculations, extract the electronic band gaps. For CH₃NH₃PbI₃ (tetragonal) the gap is at Γ; for cubic phases (CH₃NH₃PbBr₃, CsPbCl₃, cubic CsPbI₃) at R; for orthorhombic structures (CsPbBr₃, RbPbI₃, orthorhombic CsPbI₃) at the appropriate high‑symmetry point determined by the band structure. Compile the band gap value (in eV, rounded to three decimal places) for each compound into a JSON object, and write it to `/app/outputs/band_gaps.json`.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: object with exactly seven keys: "CH3NH3PbI3", "CH3NH3PbBr3", "CsPbCl3", "CsPbBr3", "RbPbI3", "CsPbI3_ortho", "CsPbI3_cubic"; each value is a float ≥ 0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The computed band gaps (eV) for the seven lead halide perovskites, produced by the present‐method mBJ parameterization (A=0.4, B=1.0, e=0.5) with spin‐orbit coupling. All values are rounded to three decimal places.
- schema:
  - `type`: object
  - `required`: `CH3NH3PbI3`, `CH3NH3PbBr3`, `CsPbCl3`, `CsPbBr3`, `RbPbI3`, `CsPbI3_ortho`, `CsPbI3_cubic`
  - `properties`:
    - `CH3NH3PbI3`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 10
    - `CH3NH3PbBr3`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 10
    - `CsPbCl3`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 10
    - `CsPbBr3`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 10
    - `RbPbI3`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 10
    - `CsPbI3_ortho`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 10
    - `CsPbI3_cubic`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 10
  - `additionalProperties`: False

Notes: The band gaps are compared to hidden reference values derived from the paper's reported present‑method results, using an appropriate tolerance to account for implementation differences.

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
        "required": [
          "CH3NH3PbI3",
          "CH3NH3PbBr3",
          "CsPbCl3",
          "CsPbBr3",
          "RbPbI3",
          "CsPbI3_ortho",
          "CsPbI3_cubic"
        ],
        "properties": {
          "CH3NH3PbI3": {
            "type": "number",
            "minimum": 0,
            "maximum": 10
          },
          "CH3NH3PbBr3": {
            "type": "number",
            "minimum": 0,
            "maximum": 10
          },
          "CsPbCl3": {
            "type": "number",
            "minimum": 0,
            "maximum": 10
          },
          "CsPbBr3": {
            "type": "number",
            "minimum": 0,
            "maximum": 10
          },
          "RbPbI3": {
            "type": "number",
            "minimum": 0,
            "maximum": 10
          },
          "CsPbI3_ortho": {
            "type": "number",
            "minimum": 0,
            "maximum": 10
          },
          "CsPbI3_cubic": {
            "type": "number",
            "minimum": 0,
            "maximum": 10
          }
        },
        "additionalProperties": false
      },
      "description": "The computed band gaps (eV) for the seven lead halide perovskites, produced by the present‐method mBJ parameterization (A=0.4, B=1.0, e=0.5) with spin‐orbit coupling. All values are rounded to three decimal places."
    }
  ],
  "notes": "The band gaps are compared to hidden reference values derived from the paper's reported present‑method results, using an appropriate tolerance to account for implementation differences."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/band_gaps.json`. For each compound, it compares your reported band gap to the paper's reported value using an absolute tolerance that accounts for implementation differences (e.g., pseudopotential vs. all-electron, basis set, convergence). If every band gap falls within that tolerance, you receive full credit; otherwise, zero credit. The verifier only checks the final band gaps; you must genuinely perform the DFT calculations to produce them. Reporting the paper's numbers without running the simulations will not satisfy the tolerance and will be detected.
