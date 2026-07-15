# Band Gap Calculation of 1D and 2D Terpyridine-Based Lead Iodide Perovskites

## Problem background
Hybrid organic–inorganic perovskites are promising for high-efficiency solar cells, but their long-term stability, especially against moisture, limits commercial deployment. To address this, researchers have explored multidimensional coupled perovskites that incorporate low-dimensional phases to improve both stability and carrier transport. This task focuses on two novel low-dimensional lead iodide perovskites — 1D‑Tpy₂Pb₃I₆ and 2D‑TpyPb₃I₆ — that feature terpyridine (Tpy) as the organic cation. Density functional theory (DFT) calculations are used to understand the electronic structure of these materials, in particular their fundamental band gaps, which are key to explaining the observed device performance and the staggered band alignment in the heterojunction.

## Approach
The work employs first‑principles periodic DFT to compute the electronic band structures of 1D‑Tpy₂Pb₃I₆ and 2D‑TpyPb₃I₆ using their experimental crystal structures (CIF files). An open‑source plane‑wave DFT code is used with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and spin‑orbit coupling, as these settings are standard for lead halide perovskites. For each material, the band structure is calculated, and the direct band gap (the minimum separation between the valence band maximum and conduction band minimum at a specific high‑symmetry point) is extracted. The final output is a JSON file reporting the two gap values in electronvolts.

## Reproduction target
Compute the direct electronic band gaps (in eV) of 1D‑Tpy₂Pb₃I₆ and 2D‑TpyPb₃I₆ and write them to /app/outputs/band_gaps.json as a JSON object with keys `gap_1D` and `gap_2D`. The reported band gap of the 1D material must be smaller than that of the 2D material, consistent with the staggered band alignment required for efficient carrier transport in the multidimensional heterojunction.

## Assets

- Crystal structure of 1D-Tpy₂Pb₃I₆ (CIF file): 10.1002/smll.202100888
- Crystal structure of 2D-TpyPb₃I₆ (CIF file): 10.1002/smll.202100888
- Open-source DFT code (Quantum ESPRESSO, GPAW, or CP2K): https://www.quantum-espresso.org
- Pseudopotential library (e.g., PSEUDODOJO or GBRV for PBE): http://www.pseudo-dojo.org

## Workflow steps

### Step 1: DFT calculation for 1D‑Tpy₂Pb₃I₆
- Role: process
- Action: Using the crystal structure from the 1D‑Tpy₂Pb₃I₆ CIF file, perform a density functional theory (DFT) calculation to compute the electronic band structure. Use a suitable exchange‑correlation functional (e.g., PBE) and include spin‑orbit coupling.
- Evidence: `/app/outputs/1D_dft.log`

### Step 2: DFT calculation for 2D‑TpyPb₃I₆
- Role: process
- Action: Using the crystal structure from the 2D‑TpyPb₃I₆ CIF file, perform a DFT calculation with the same settings (PBE, spin‑orbit coupling) to compute the electronic band structure.
- Evidence: `/app/outputs/2D_dft.log`

### Step 3: Report band gaps
- Role: scored (load-bearing)
- Action: Extract the direct band gap values from the DFT calculations performed in step_01 and step_02 and write them to /app/outputs/band_gaps.json as floating‑point numbers in electronvolts (eV).
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"gap_1D": "number (eV)", "gap_2D": "number (eV)"}
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
- description: Band gap values of the 1D-Tpy₂Pb₃I₆ and 2D-TpyPb₃I₆ perovskites obtained from DFT calculations.
- schema:
  - `type`: object
  - `required`:
    - `gap_1D`: number (eV)
    - `gap_2D`: number (eV)
  - `units`:
    - `gap_1D`: eV
    - `gap_2D`: eV

Notes: The checker expects the band gap of the 1D material to be smaller than that of the 2D material. Absolute values are compared within a tolerance to account for differences in DFT implementations.

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
          "gap_1D": "number (eV)",
          "gap_2D": "number (eV)"
        },
        "units": {
          "gap_1D": "eV",
          "gap_2D": "eV"
        }
      },
      "description": "Band gap values of the 1D-Tpy₂Pb₃I₆ and 2D-TpyPb₃I₆ perovskites obtained from DFT calculations."
    }
  ],
  "notes": "The checker expects the band gap of the 1D material to be smaller than that of the 2D material. Absolute values are compared within a tolerance to account for differences in DFT implementations."
}
```

## How you are scored
A hidden verifier checks the contents of /app/outputs/band_gaps.json. It compares your computed `gap_1D` and `gap_2D` against expected reference values and verifies that the 1D band gap is lower than the 2D band gap (i.e., `gap_1D` < `gap_2D`). The total reward (0.0–1.0) is a weighted combination of the accuracy of the individual band gap values and the correctness of the relative ordering. Reporting numbers without executing the required DFT calculations will not yield a passing score.
