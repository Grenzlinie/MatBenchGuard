# DFT Band Gaps and Density of States of Hexaazatriphenylene-Based COFs

## Problem background
Gold recovery from electronic waste is economically and environmentally important, as leachates can contain much higher concentrations of gold than natural ores. Covalent organic frameworks (COFs) have emerged as promising adsorbents; however, achieving high capacity and selectivity often requires tuning the electronic character of the pore walls. Hexaazatriphenylene-based COFs (HATP-COF-1 and HATP-COF-2) were designed with electronegative skeletons that place electron‑rich nitrogen atoms at vertex, imine linkages, and (in HATP-COF-2) pyridine linker sites, creating a distribution of electrostatic binding sites. The electronic structure—specifically the band gap and the projected density of states—is used to rationalize the differing gold‑capture performance of the two frameworks. This task reproduces the DFT‑computed electronic structure of both materials.

## Approach
Using the known crystal structures (AA‑stacking, P3 space group) and the reported lattice parameters, build atomistic models of HATP-COF-1 and HATP-COF-2 from their molecular fragments: the hexaazatriphenylene vertex and the respective diamino linkers ([1,1'-biphenyl]-4,4'-diamine for HATP-COF-1, 5,5'-diamino-2,2'-bipyridine for HATP-COF-2). Perform periodic density‑functional theory (DFT) calculations with a plane‑wave code (Quantum ESPRESSO or a compatible open‑source alternative) using a generalized gradient approximation (PBE) functional and a dispersion correction (e.g., D3). First, relax the atomic positions while keeping the lattice parameters fixed, then compute the electronic structure. Band structures are obtained along a standard high‑symmetry path (Γ‑M‑K‑Γ) of the hexagonal Brillouin zone, and the fundamental band gap (eV) is extracted for each COF. Separately, compute the total density of states (DOS) and the projected density of states (PDOS) onto carbon and nitrogen atomic orbitals on a dense k‑mesh. The results are to be written directly into the output files band_gaps.json and dos.json.

## Reproduction target
Produce the following two scored artifacts under /app/outputs.

- band_gaps.json: A JSON object with keys "HATP-COF-1" and "HATP-COF-2", each a float representing the DFT‑computed fundamental band gap in eV. The relative ordering of the two gaps is part of the evaluation.
- dos.json: A JSON object containing the total and projected density of states. The file must have keys "energy" (1D float array, in eV relative to the Fermi level), "total_dos" (1D float array, arbitrary units), "c_dos" (1D float array), and "n_dos" (1D float array). All arrays must be of equal length. You may choose either HATP-COF-1 or HATP-COF-2 for this computation, but you must state which framework the data belong to (e.g., by including a "system" field in the JSON). The energy range should cover a reasonable window around the Fermi level (e.g., at least from −5 eV to +5 eV).

Process‑step evidence (initial_structures.json and optimization.log) is required for pipeline auditing but is not directly scored.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
- SSSP pseudopotential library (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Model construction of HATP-COF-1 and HATP-COF-2 periodic structures
- Role: process
- Action: Construct AA-stacking periodic structures of HATP-COF-1 and HATP-COF-2 using the refined lattice parameters (P3 space group: HATP-COF-1 a=b=33.22473 Å, c=4.70489 Å; HATP-COF-2 a=b=34.71496 Å, c=4.71199 Å) and atomic fragments from the hexaazatriphenylene vertex and the respective linkers. Output initial atomic coordinates in a format suitable for Quantum ESPRESSO.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for both COFs using Quantum ESPRESSO with a generalized gradient approximation (PBE) functional and a dispersion correction (e.g., D3). Relax atomic positions keeping the lattice parameters fixed. Save the optimized structures for subsequent electronic-structure calculations.
- Evidence: `/app/outputs/optimization.log`

### Step 3: Band structure and band gap extraction
- Role: scored (load-bearing)
- Action: From the optimized geometries, perform a self-consistent field (SCF) calculation followed by a non-SCF band structure calculation along a standard high-symmetry path (Γ-M-K-Γ) of the hexagonal Brillouin zone. Extract the fundamental band gap (eV) for both HATP-COF-1 and HATP-COF-2. Write the results to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: A JSON object with exactly two keys: 'HATP-COF-1' (float) and 'HATP-COF-2' (float).
- Scoring: scored by hidden verifier

### Step 4: Total and projected density of states
- Role: scored
- Action: Using the optimized structures, compute the total density of states (DOS) and the projected density of states (PDOS) onto atomic orbitals (C 2p, N 2p) with a dense k-mesh. Output the data as dos.json containing arrays of equal length for energy (eV, relative to Fermi level), total DOS, and PDOS contributions from carbon and nitrogen.
- Output file: `/app/outputs/dos.json`
- Format: json
- Contract: A JSON object with keys: 'energy' (1D float array), 'total_dos' (1D float array), 'c_dos' (1D float array), 'n_dos' (1D float array), all arrays of equal length.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/dos.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gaps of HATP-COF-1 and HATP-COF-2. The verifier compares these values to the paper-reported values with a relative tolerance and also enforces that HATP-COF-2 < HATP-COF-1.
- schema:
  - `type`: object
  - `required`:
    - `HATP-COF-1`: float
    - `HATP-COF-2`: float
  - `description`: A JSON object with exactly two keys: 'HATP-COF-1' (float) and 'HATP-COF-2' (float), the DFT-computed band gap in eV.

### dos.json
- path: `/app/outputs/dos.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Total and projected density of states for one of the COFs (agent may choose either HATP-COF-1 or HATP-COF-2, but must state which). The verifier checks array lengths and the presence of finite C and N PDOS near the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `energy`: array of floats
    - `total_dos`: array of floats
    - `c_dos`: array of floats
    - `n_dos`: array of floats
  - `description`: All arrays must be equal length. Energy values are in eV relative to Fermi level. DOS arrays are in arbitrary units.

Notes: The Au³⁺ binding energy calculations (Fig. 5) are excluded because their geometry is underspecified. All other computational stages (model construction, optimization, band structure, DOS) are included. The agent must use the lattice parameters and building blocks provided in the paper and reconstruct the structures without relying on pre‑built coordinates.

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
          "HATP-COF-1": "float",
          "HATP-COF-2": "float"
        },
        "description": "A JSON object with exactly two keys: 'HATP-COF-1' (float) and 'HATP-COF-2' (float), the DFT-computed band gap in eV."
      },
      "description": "Band gaps of HATP-COF-1 and HATP-COF-2. The verifier compares these values to the paper-reported values with a relative tolerance and also enforces that HATP-COF-2 < HATP-COF-1."
    },
    {
      "file": "dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "energy": "array of floats",
          "total_dos": "array of floats",
          "c_dos": "array of floats",
          "n_dos": "array of floats"
        },
        "description": "All arrays must be equal length. Energy values are in eV relative to Fermi level. DOS arrays are in arbitrary units."
      },
      "description": "Total and projected density of states for one of the COFs (agent may choose either HATP-COF-1 or HATP-COF-2, but must state which). The verifier checks array lengths and the presence of finite C and N PDOS near the Fermi level."
    }
  ],
  "notes": "The Au³⁺ binding energy calculations (Fig. 5) are excluded because their geometry is underspecified. All other computational stages (model construction, optimization, band structure, DOS) are included. The agent must use the lattice parameters and building blocks provided in the paper and reconstruct the structures without relying on pre‑built coordinates."
}
```

## How you are scored
A hidden verifier scores each output file independently and then combines the results into a single reward between 0 and 1.

- band_gaps.json: The two band gaps are compared against a hidden reference with a quantitative tolerance. In addition, the verifier checks that the gap of HATP-COF-2 is strictly less than the gap of HATP-COF-1 (trend verification).
- dos.json: The verifier performs a structural audit: it validates that all four arrays have equal length, that the energy range covers at least [−5, +5] eV, and that the projected DOS shows finite, non‑zero values for both C and N in the vicinity of the Fermi level.
- The non‑scored process evidence (initial_structures.json, optimization.log) may be spot‑checked for completeness but carries no direct weight.

Simply reporting a number is not sufficient; the hidden checker uses the contents of the files you write.
