# First-principles DFT calculation of electronic band structure and band gap of La2GeO5

## Problem background
The electronic band structure of crystalline solids determines key optical properties such as absorption and emission. For the oxide host La2GeO5, understanding the band gap and the character of the valence and conduction bands is essential for designing phosphors and optoelectronic materials. This task reproduces the density functional theory (DFT) calculation of the electronic band structure and the associated direct band gap of monoclinic La2GeO5 (space group P21/c). The calculation provides a reference electronic-structure description that informs the interpretation of experimental optical spectra and interband transitions.

## Approach
The calculation is performed with first-principles DFT using the generalized gradient approximation (GGA) in the Perdew–Burke–Ernzerhof (PBE) formulation. The crystal structure is taken from refined X-ray diffraction data (Table 1 in the instruction). The unit cell contains 52 atoms with two inequivalent La sites, GeO4 tetrahedra, and several oxygen positions. The self-consistent field (SCF) calculation is followed by a non-self-consistent band structure calculation along a standard high-symmetry k-path and a total density of states calculation using the tetrahedron method. The open-source Quantum ESPRESSO package (pw.x, bands.x, dos.x) serves as the DFT engine, with PBE pseudopotentials from a public library (e.g., SSSP efficiency).

## Reproduction target
Compute the electronic band structure, total density of states, and direct band gap of monoclinic La2GeO5 using DFT-PBE. From the calculation, produce a band structure file (band_structure.dat) containing k-point distances and eigenvalues along the high-symmetry path, a total DOS file (dos.dat) with energy and DOS values, and extract the direct band gap at the Γ point into band_gap.txt. The direct band gap is defined as the energy difference between the lowest unoccupied conduction band and the highest occupied valence band at the same k-point where they coincide.

## Assets

- La2GeO5 crystal structure (Table 1)
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT self-consistent field and band structure calculation
- Role: process
- Action: Construct the La2GeO5 unit cell using the provided monoclinic lattice parameters (a=7.10975 Å, b=7.46333 Å, c=9.60172 Å, β=107.5466°, space group P21/c) and atomic fractional coordinates (Table 1). Perform a self-consistent DFT calculation with the PBE functional, then compute the band structure along a standard high-symmetry path (e.g., Γ–X–S–Y–Γ–Z) and the total density of states using the tetrahedron method. Use Quantum ESPRESSO (pw.x, bands.x, dos.x). Write raw output files for later extraction.
- Evidence: `/app/outputs/qe_output.log`

### Step 2: Extract band structure data
- Role: scored (load-bearing)
- Action: Export the computed electronic band structure as a text file. Each row corresponds to one k-point and one band. Columns: k-point distance along the path (1/Å) and eigenvalue (eV). Include all bands. Write to band_structure.dat.
- Output file: `/app/outputs/band_structure.dat`
- Format: txt
- Contract: Columns: k_distance (float, units 1/Å), eigenvalue (float, eV). Space-separated, one line per (k-point, band). Optional header line.
- Scoring: scored by hidden verifier

### Step 3: Extract density of states
- Role: scored
- Action: Output the total density of states as a two-column file: energy (eV) and total DOS (states/eV). Write to dos.dat.
- Output file: `/app/outputs/dos.dat`
- Format: txt
- Contract: Columns: energy (eV), total_DOS (states/eV). Space-separated, optional header.
- Scoring: scored by hidden verifier

### Step 4: Extract direct band gap
- Role: scored
- Action: From the band structure data, identify the highest occupied valence state and the lowest unoccupied conduction state that occur at the same k-point (the band gap is direct). Compute the direct band gap as E_cbm - E_vbm and write the value in eV to band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: Single line containing a floating-point number (eV). No extra text.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure.dat`
- `/app/outputs/dos.dat`
- `/app/outputs/band_gap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure.dat
- path: `/app/outputs/band_structure.dat`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Electronic band structure eigenvalues along a high-symmetry path. The checker will recompute the direct band gap from this file.
- schema:
  - `type`: table
  - `required_columns`: `k_distance`, `eigenvalue`
  - `units`:
    - `k_distance`: 1/Å
    - `eigenvalue`: eV

### dos.dat
- path: `/app/outputs/dos.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total density of states. The checker will audit the presence of a band gap region (zero DOS between valence and conduction bands).
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_DOS`
  - `units`:
    - `energy`: eV
    - `total_DOS`: states/eV

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Agent-reported direct band gap value. The checker will compare this value against the hidden gold value with tolerance.
- schema:
  - `type`: text
  - `unit`: eV

Notes: The primary scoring weight is on the direct band gap recomputed from band_structure.dat. The DOS file carries a small structural audit weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_distance",
          "eigenvalue"
        ],
        "units": {
          "k_distance": "1/Å",
          "eigenvalue": "eV"
        }
      },
      "description": "Electronic band structure eigenvalues along a high-symmetry path. The checker will recompute the direct band gap from this file."
    },
    {
      "file": "dos.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_DOS"
        ],
        "units": {
          "energy": "eV",
          "total_DOS": "states/eV"
        }
      },
      "description": "Total density of states. The checker will audit the presence of a band gap region (zero DOS between valence and conduction bands)."
    },
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "unit": "eV"
      },
      "description": "Agent-reported direct band gap value. The checker will compare this value against the hidden gold value with tolerance."
    }
  ],
  "notes": "The primary scoring weight is on the direct band gap recomputed from band_structure.dat. The DOS file carries a small structural audit weight."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that evaluates each output artifact separately. The verifier recomputes the direct band gap from your band_structure.dat file and compares it against a reference value using an appropriate tolerance. It also checks the structural integrity of your density of states (presence of a band gap region) and the format of all output files. Each scored artifact contributes a weighted portion to the final reward (total 1.0). The reward is monotonic in quality: the closer your computed gap is to the expected range, the higher the score, with full credit for meeting or exceeding the quality threshold. Simply reporting a plausible number without performing the DFT calculation will not yield the full reward, as the verifier examines the detailed raw data.
