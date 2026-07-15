# DFT Study of MBSi2 Structural, Electronic, and Mechanical Properties

## Problem background
Diamond-like covalent networks hosting guest alkali-metal atoms exhibit diverse structural and electronic properties, and have been explored for applications such as thermoelectrics and superconductors. A recently reported compound, LiBSi₂, features a three-dimensional BSi₂ framework with channels occupied by Li atoms. Replacing the guest atom with larger alkalis (Na, K, Rb) or removing it altogether may distort the covalent network and alter the electronic structure. The open question is how the choice of guest species affects the crystal structure, electronic band gap, metallicity, and mechanical stability, and whether a semiconductor-to-metal transition occurs across the series MBSi₂ (M = Li, Na, K, Rb) and the guest-free BSi₂ phase.

## Approach
The study uses first-principles density-functional theory (DFT) with the GGA-PBE exchange–correlation functional. The structures of all five tetragonal phases (space group P4₂/nmc) are fully relaxed, and the resulting lattice parameters, cell volumes, and atomic coordinates are collected. A phonon dispersion calculation (finite-displacement method) is performed for BSi₂ to check for imaginary frequencies. Electronic band structures and density-of-states (DOS) are computed for each compound, from which the band gap, metallic/semiconducting character, and the dominant orbital character at the Fermi level are extracted. Finally, elastic constants are obtained from stress–strain calculations; the bulk modulus, shear modulus, and Pugh’s ratio B/G are derived, and the mechanical stability criteria for tetragonal symmetry are verified. By comparing the results across the five systems, one can infer the structural and electronic trends induced by the guest atoms.

## Reproduction target
Compute and report the following quantities for the five compounds BSi₂, LiBSi₂, NaBSi₂, KBSi₂, and RbBSi₂:
- optimized lattice parameters (a, c) and cell volume per formula unit (V), along with the relaxed fractional atomic coordinates and Wyckoff labels.
- for BSi₂ only, a phonon-stability verdict (stable or unstable) based on the absence or presence of imaginary frequencies.
- the electronic band gap (null if metallic), a metallic/semiconducting flag, and a qualitative description of the dominant orbital character of the density of states at the Fermi level.
- the elastic constants C₁₁, C₃₃, C₄₄, C₆₆, C₁₂, C₁₃, and the derived bulk modulus B, shear modulus G, and Pugh’s ratio B/G.
Use these results to determine whether each phase is a semiconductor or a metal, whether BSi₂ is dynamically stable, and whether the mechanical stability criteria for tetragonal crystals are satisfied. The analysis should also examine how the lattice parameters and volumes change across the series, and whether the B/G ratio suggests ductile or brittle behavior.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for B, Si, Li, Na, K, Rb: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Geometry optimization of all compounds
- Role: process
- Action: Perform full DFT geometry optimizations for BSi2, LiBSi2, NaBSi2, KBSi2, and RbBSi2 in the tetragonal P4_2/nmc space group. Use initial atomic positions from the paper and a GGA-PBE functional with a 450 eV cutoff and a 5×5×4 k-point mesh. The optimizations must converge forces and total energies to tight criteria.
- Evidence: `/app/outputs/geometry_optimizations.log`

### Step 2: Extract structural summary
- Role: scored (load-bearing)
- Action: From the optimized structures, extract the relaxed lattice parameters a, c, cell volume per formula unit V, and fractional atomic coordinates with Wyckoff labels for all five compounds. Write the data to structures_summary.json.
- Output file: `/app/outputs/structures_summary.json`
- Format: json
- Contract: A JSON object with top-level keys 'BSi2', 'LiBSi2', 'NaBSi2', 'KBSi2', 'RbBSi2'. Each value is an object with: 'a' (float, Å), 'c' (float, Å), 'V_per_fu' (float, Å³), 'atoms' (list of objects, each with 'element' (string), 'x' (float), 'y' (float), 'z' (float), 'wyckoff' (string)).
- Scoring: scored by hidden verifier

### Step 3: Phonon stability of BSi2
- Role: scored
- Action: Using the optimized BSi2 structure, perform a phonon dispersion calculation (finite displacement method). Determine whether imaginary frequencies are present and write a single-line text verdict.
- Output file: `/app/outputs/bsi2_phonon_stability.txt`
- Format: txt
- Contract: A single line: either 'Stable: no imaginary frequencies' or 'Unstable: imaginary frequencies found'.
- Scoring: scored by hidden verifier

### Step 4: Electronic band structure and DOS analysis
- Role: scored
- Action: Using the optimized structures, compute the electronic band structure and density of states (DOS) for all five compounds with the same DFT settings. Determine the band gap (in eV) and metallic/semiconducting character. Extract the dominant orbital character of the DOS at the Fermi level. Write the results to electronic_summary.json.
- Output file: `/app/outputs/electronic_summary.json`
- Format: json
- Contract: A JSON object with top-level keys 'BSi2', 'LiBSi2', 'NaBSi2', 'KBSi2', 'RbBSi2'. Each value is an object: {'band_gap_eV': float or null if metallic, 'is_metal': boolean, 'dos_fermi_character': string (e.g., 'Si pz dominated')}.
- Scoring: scored by hidden verifier

### Step 5: Elastic constants and mechanical properties
- Role: scored
- Action: Compute the elastic constants C11, C33, C44, C66, C12, C13 for each compound using a stress-strain method. Derive the bulk modulus B, shear modulus G, and Pugh's ratio B/G. Verify the mechanical stability criteria for tetragonal systems. Write all values to elastic_constants_summary.json.
- Output file: `/app/outputs/elastic_constants_summary.json`
- Format: json
- Contract: A JSON object with top-level keys 'BSi2', 'LiBSi2', 'NaBSi2', 'KBSi2', 'RbBSi2'. Each value is an object: {'C11': float, 'C33': float, 'C44': float, 'C66': float, 'C12': float, 'C13': float, 'B': float, 'G': float, 'B/G': float}. All units GPa except B/G (unitless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structures_summary.json`
- `/app/outputs/bsi2_phonon_stability.txt`
- `/app/outputs/electronic_summary.json`
- `/app/outputs/elastic_constants_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structures_summary.json
- path: `/app/outputs/structures_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameters, volumes, and atomic positions for all five compounds.
- schema:
  - `type`: object
  - `required`:
    - `BSi2`: object
    - `LiBSi2`: object
    - `NaBSi2`: object
    - `KBSi2`: object
    - `RbBSi2`: object
  - `items`:
    - `a`: float (Å)
    - `c`: float (Å)
    - `V_per_fu`: float (Å³)
    - `atoms`: array of objects (element:string, x:float, y:float, z:float, wyckoff:string)

### bsi2_phonon_stability.txt
- path: `/app/outputs/bsi2_phonon_stability.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Phonon stability verdict for BSi2.
- schema:
  - `type`: text
  - `required`:
    - `line`: string (one of: 'Stable: no imaginary frequencies' or 'Unstable: imaginary frequencies found')

### electronic_summary.json
- path: `/app/outputs/electronic_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gaps, metallic flags, and DOS character near the Fermi level for all compounds.
- schema:
  - `type`: object
  - `required`:
    - `BSi2`: object
    - `LiBSi2`: object
    - `NaBSi2`: object
    - `KBSi2`: object
    - `RbBSi2`: object
  - `items`:
    - `band_gap_eV`: float or null
    - `is_metal`: boolean
    - `dos_fermi_character`: string (e.g., 'Si_pz dominated')

### elastic_constants_summary.json
- path: `/app/outputs/elastic_constants_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic constants and derived moduli for all compounds.
- schema:
  - `type`: object
  - `required`:
    - `BSi2`: object
    - `LiBSi2`: object
    - `NaBSi2`: object
    - `KBSi2`: object
    - `RbBSi2`: object
  - `items`:
    - `C11`: float (GPa)
    - `C33`: float (GPa)
    - `C44`: float (GPa)
    - `C66`: float (GPa)
    - `C12`: float (GPa)
    - `C13`: float (GPa)
    - `B`: float (GPa)
    - `G`: float (GPa)
    - `B/G`: float (unitless)

Notes: All reference comparisons use hidden tolerances that absorb systematic differences due to DFT code and pseudopotential choice. The checker verifies structural trends (monotonic volume expansion, abrupt c‑axis increase), band gap values and metallic/semiconducting classification, phonon stability phrase, and elastic constants including mechanical stability criteria and B/G ductility trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structures_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BSi2": "object",
          "LiBSi2": "object",
          "NaBSi2": "object",
          "KBSi2": "object",
          "RbBSi2": "object"
        },
        "items": {
          "a": "float (Å)",
          "c": "float (Å)",
          "V_per_fu": "float (Å³)",
          "atoms": "array of objects (element:string, x:float, y:float, z:float, wyckoff:string)"
        }
      },
      "description": "Optimized lattice parameters, volumes, and atomic positions for all five compounds."
    },
    {
      "file": "bsi2_phonon_stability.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "line": "string (one of: 'Stable: no imaginary frequencies' or 'Unstable: imaginary frequencies found')"
        }
      },
      "description": "Phonon stability verdict for BSi2."
    },
    {
      "file": "electronic_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BSi2": "object",
          "LiBSi2": "object",
          "NaBSi2": "object",
          "KBSi2": "object",
          "RbBSi2": "object"
        },
        "items": {
          "band_gap_eV": "float or null",
          "is_metal": "boolean",
          "dos_fermi_character": "string (e.g., 'Si_pz dominated')"
        }
      },
      "description": "Band gaps, metallic flags, and DOS character near the Fermi level for all compounds."
    },
    {
      "file": "elastic_constants_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BSi2": "object",
          "LiBSi2": "object",
          "NaBSi2": "object",
          "KBSi2": "object",
          "RbBSi2": "object"
        },
        "items": {
          "C11": "float (GPa)",
          "C33": "float (GPa)",
          "C44": "float (GPa)",
          "C66": "float (GPa)",
          "C12": "float (GPa)",
          "C13": "float (GPa)",
          "B": "float (GPa)",
          "G": "float (GPa)",
          "B/G": "float (unitless)"
        }
      },
      "description": "Elastic constants and derived moduli for all compounds."
    }
  ],
  "notes": "All reference comparisons use hidden tolerances that absorb systematic differences due to DFT code and pseudopotential choice. The checker verifies structural trends (monotonic volume expansion, abrupt c‑axis increase), band gap values and metallic/semiconducting classification, phonon stability phrase, and elastic constants including mechanical stability criteria and B/G ductility trend."
}
```

## How you are scored
A hidden verifier will independently check each of the four output files. It will compare your computed lattice parameters, band gaps, stability verdict, and elastic constants against reference values with appropriate tolerances that account for systematic differences due to the choice of DFT code and pseudopotentials. It will also verify that the reported structural trends (e.g., evolution of a, c, V), the metallic/semiconducting classification, the phonon-stability statement, the mechanical stability criteria, and the B/G ductility indicator are correctly reported. Each artifact contributes a share of the final reward, which is a continuous score between 0 and 1. Submitting values merely copied from the literature will not pass; you must obtain them by running the described DFT workflow.
