# First-Principles Structure, Stability, and Band Gaps of Silicon Allotropes

## Problem background
Silicon is the dominant material for photovoltaic energy production, but its ordinary diamond form suffers from an indirect electronic band gap, which limits light absorption and requires thick absorber layers. Searching for silicon allotropes with direct or quasi-direct band gaps in the visible range is therefore a long-standing goal. This work explores whether five known sp³ carbon crystal topologies can be transplanted to silicon, yielding metastable allotropes that are dynamically and thermodynamically stable and possess electronic properties suitable for thin‑film solar cells. The reproduction task is to compute their optimized structures, phonon stability, and band gaps by first‑principles methods.

## Approach
The approach transplants five previously reported sp³ carbon crystal topologies (M585, S, Z‑CACB, H, Z‑ACA) to silicon. Starting structures are obtained by substituting silicon atoms for carbon and scaling the lattice to reasonable Si–Si bond lengths. These structures are then fully relaxed using density‑functional theory (DFT) within the local‑density approximation (LDA) and a plane‑wave projector‑augmented‑wave (PAW) method. Diamond silicon is relaxed alongside the five allotropes to serve as the energy reference. For each optimized system, the dynamical stability is evaluated by computing the phonon band structure via the finite‑displacement method; the absence of imaginary frequencies is taken as evidence of stability. Electronic band structures are then computed with the HSE06 hybrid functional to extract both the indirect and the direct band gaps. All calculations use open‑source or publicly available tools equivalent to those in the original study. The comparison of structural properties, relative energies, and band gaps against diamond silicon provides a self‑contained check of the predicted allotropes' promise for solar applications.

## Reproduction target
1.  Produce `/app/outputs/optimized_structures.json`: a JSON object reporting, for each of the five allotropes (M585, S, Z‑CACB, H, Z‑ACA), the space group, lattice constants (a, b, c in Å), mass density (Mg/m³), and relative energy with respect to diamond silicon (meV/atom), all obtained from the LDA‑PAW geometry optimization.
2.  Produce `/app/outputs/phonon_stability.json`: a JSON object that records, for each allotrope, whether the phonon calculation reveals any imaginary frequencies (stable = true/false) and optionally the maximum negative frequency (THz).
3.  Produce `/app/outputs/band_gaps.json`: a JSON object that reports, for each allotrope, the indirect band gap (eV) and the direct band gap (eV) computed with the HSE06 hybrid functional.

All results must be derived from the same public carbon topologies and open‑source or publicly documented DFT tools; no external experimental data are required.

## Assets

- Five sp³ carbon crystal topologies (M585, S, Z-CACB, H, Z-ACA) from He et al. 2012: doi:10.1039/c2cp24196c; Solid State Commun. 152, 1560 (2012). Atomic positions must be extracted to build initial Si cells.
- Plane-wave DFT code with LDA+PAW capability (e.g., Quantum ESPRESSO, ABINIT, VASP): Open-source alternatives (Quantum ESPRESSO, ABINIT) can substitute for proprietary VASP.
- Phonon calculation package (Phonopy or equivalent): https://phonopy.github.io/phonopy/
- HSE06 hybrid functional implementation: Available in most DFT codes (VASP, Quantum ESPRESSO, etc.).

## Workflow steps

### Step 1: Generate initial Si structures
- Role: process
- Action: Obtain the five sp³ carbon crystal topologies (M585, S, Z-CACB, H, Z-ACA) from the literature. Substitute silicon atoms for carbon and scale lattice parameters to appropriate Si–Si bond lengths to create starting Si structures. Prepare input files for DFT optimization.
- Evidence: `/app/outputs/initial_structures.cif`

### Step 2: DFT geometry optimization and structural properties
- Role: scored (load-bearing)
- Action: Perform density-functional theory (DFT) geometry optimization of diamond silicon and the five Si allotropes using the local-density approximation (LDA) and a plane-wave PAW method. Relax both ionic positions and lattice parameters. For each system, extract the space group, lattice constants (a, b, c in Å), mass density (Mg/m³), and total energy. Compute the relative energy per atom with respect to diamond silicon. Save all results to optimized_structures.json.
- Output file: `/app/outputs/optimized_structures.json`
- Format: json
- Contract: A JSON object with top-level keys per allotrope (M585, S, Z-CACB, H, Z-ACA). Each value is an object containing: space_group (string), lattice_a, lattice_b, lattice_c (Å, numbers), mass_density (Mg/m³, number), relative_energy (meV/atom, number).
- Scoring: scored by hidden verifier

### Step 3: Phonon dynamical stability
- Role: scored
- Action: For each optimized structure from step 1, compute the phonon band structure using the finite-displacement method (e.g., Phonopy). Determine whether any imaginary phonon frequencies exist. Record whether each allotrope is dynamically stable (no imaginary modes) and optionally the maximum negative frequency. Write results to phonon_stability.json.
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: A JSON object with top-level keys per allotrope. Each value is an object containing: stable (boolean, true if no imaginary frequencies), max_negative_frequency (THz, number, optional).
- Scoring: scored by hidden verifier

### Step 4: HSE06 electronic band gaps
- Role: scored
- Action: For each optimized structure, compute the electronic band structure using the HSE06 hybrid functional. Extract the indirect band gap (minimum conduction band minus maximum valence band across the Brillouin zone) and the direct band gap (smallest direct transition at the same k-point). Save results to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: A JSON object with top-level keys per allotrope. Each value is an object containing: indirect_band_gap (eV, number), direct_band_gap (eV, number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structures.json`
- `/app/outputs/phonon_stability.json`
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structures.json
- path: `/app/outputs/optimized_structures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized structural data: lattice constants, mass density, and relative energy per atom for diamond silicon and the five allotropes, as computed from LDA-PAW geometry optimization.
- schema:
  - `type`: object
  - `required`: `M585`, `S`, `Z-CACB`, `H`, `Z-ACA`
  - `item_structure`:
    - `space_group`: string
    - `lattice_a`:
      - `type`: number
      - `unit`: Å
    - `lattice_b`:
      - `type`: number
      - `unit`: Å
    - `lattice_c`:
      - `type`: number
      - `unit`: Å
    - `mass_density`:
      - `type`: number
      - `unit`: Mg/m³
    - `relative_energy`:
      - `type`: number
      - `unit`: meV/atom

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dynamical stability verdict: indicates whether each allotrope has no imaginary phonon modes, based on finite-displacement phonon calculations.
- schema:
  - `type`: object
  - `required`: `M585`, `S`, `Z-CACB`, `H`, `Z-ACA`
  - `item_structure`:
    - `stable`: boolean
    - `max_negative_frequency`:
      - `type`: number
      - `unit`: THz
      - `optional`: True

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: HSE06 electronic band gaps: indirect and direct band gaps for the five Si allotropes.
- schema:
  - `type`: object
  - `required`: `M585`, `S`, `Z-CACB`, `H`, `Z-ACA`
  - `item_structure`:
    - `indirect_band_gap`:
      - `type`: number
      - `unit`: eV
    - `direct_band_gap`:
      - `type`: number
      - `unit`: eV

Notes: The checker compares the agent's reported numbers in these JSON files to the paper's reference values within hidden tolerances. All output files must be placed under /app/outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "M585",
          "S",
          "Z-CACB",
          "H",
          "Z-ACA"
        ],
        "item_structure": {
          "space_group": "string",
          "lattice_a": {
            "type": "number",
            "unit": "Å"
          },
          "lattice_b": {
            "type": "number",
            "unit": "Å"
          },
          "lattice_c": {
            "type": "number",
            "unit": "Å"
          },
          "mass_density": {
            "type": "number",
            "unit": "Mg/m³"
          },
          "relative_energy": {
            "type": "number",
            "unit": "meV/atom"
          }
        }
      },
      "description": "Optimized structural data: lattice constants, mass density, and relative energy per atom for diamond silicon and the five allotropes, as computed from LDA-PAW geometry optimization."
    },
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "M585",
          "S",
          "Z-CACB",
          "H",
          "Z-ACA"
        ],
        "item_structure": {
          "stable": "boolean",
          "max_negative_frequency": {
            "type": "number",
            "unit": "THz",
            "optional": true
          }
        }
      },
      "description": "Dynamical stability verdict: indicates whether each allotrope has no imaginary phonon modes, based on finite-displacement phonon calculations."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "M585",
          "S",
          "Z-CACB",
          "H",
          "Z-ACA"
        ],
        "item_structure": {
          "indirect_band_gap": {
            "type": "number",
            "unit": "eV"
          },
          "direct_band_gap": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "HSE06 electronic band gaps: indirect and direct band gaps for the five Si allotropes."
    }
  ],
  "notes": "The checker compares the agent's reported numbers in these JSON files to the paper's reference values within hidden tolerances. All output files must be placed under /app/outputs."
}
```

## How you are scored
A hidden verifier independently scores each of the three output artifacts (`optimized_structures.json`, `phonon_stability.json`, `band_gaps.json`). Your submitted numbers are compared to reference values derived from standard first‑principles calculations following the same protocol. Each artifact carries a weight, and the final reward (0–1) is a weighted combination of the stage scores. Simply quoting the paper's figures is not sufficient; the verifier checks that the reported values are consistent with a correct execution of the full workflow. The precise tolerances and comparison logic are hidden, but a faithful reproduction that delivers internally consistent and physically sensible results will earn a high score.
