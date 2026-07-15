# SCC-DFTB Modeling of 3D BN Polymorphs: Structural and Electronic Properties

## Problem background
Boron nitride (BN) is an inorganic compound analogous to carbon that can crystallize in many polymorphous forms. Beyond the familiar layered (graphite-like) and cubic (diamond-like) phases, a variety of three-dimensional structures with sp³-hybridized atoms are possible, each with distinct structural motifs and potentially different physical properties. Understanding how the arrangement of B and N atoms into units like tetragonal B₂N₂ rings or B₄N₄ cubes affects the stability, density, elastic response, and electronic band structure is important for the rational design of BN-based materials with tailored characteristics. The self-consistent charge density functional tight binding (SCC-DFTB) method offers a computationally efficient means to perform systematic comparative simulations across multiple candidate polymorphs, making it possible to explore the full structural family and extract reliable trends.

## Approach
The computational approach is to model six specific 3D sp³ BN polymorphs using SCC-DFTB: the well-known cubic phase c-BN, and five hypothetical structures identified by their crystal lattice types—body-centered tetragonal (bct), body-centered cubic (bcc), face-centered cubic (fcc), simple cubic (sc), and a more complex tetragonal (t) arrangement. For each polymorph, initial unit-cell models are constructed from the described structural motifs (alternating B–N bonds, tetragonal B₂N₂ rings, B₄N₄ cubes, and isolated sp³ B/N atoms) ensuring that every boron is surrounded only by nitrogen and vice versa. The workflow then performs a full geometry optimization with DFTB+ using the publicly available Slater–Koster parameter set for B–N (pbc-0-3). From the relaxed structures, the lattice parameters, unit-cell volume, total energy, theoretical density, and bulk modulus are extracted; the bulk modulus is estimated by fitting an equation of state to total energies computed at varied volumes. Electronic-structure calculations yield the band structure and density of states (DOS), from which the band gap and the dominant orbital character at the valence band maximum and conduction band minimum are obtained. All results are compared across the polymorph series to reveal how the lattice architecture influences the physical properties.

## Reproduction target
Produce a quantitative reproduction of the SCC-DFTB simulation results for the six BN polymorphs. The task is to compute, for each of the six structures, the following quantities and store them in the prescribed JSON files:

- In `properties.json`: for each polymorph, report the number of atoms in the unit cell Z, the lattice constants a and c (where applicable), the volume per atom V_uc (in Å³/atom), the total energy per atom relative to c-BN ΔE_tot (eV/atom), the theoretical density ρ (g/cm³), the compression modulus B (GPa), and the change in band gap ΔE_g (eV) relative to the c-BN gap.
- In `dos_character.json`: for each polymorph, assign the dominant orbital character at the valence band maximum (VBM) and conduction band minimum (CBM) and provide a boolean judgment of whether the overall pattern of orbital character across the series matches the expectation that the VBM is primarily derived from N 2p states and the CBM from B 2p states.

The reproduction is considered successful if the computed values, when checked against reference data, fall within predefined tolerances and the qualitative trends (e.g., the ordering of volumes and energies among the polymorphs) align with the original study.

## Assets

- DFTB+: https://www.dftbplus.org
- Slater-Koster parameter set for B-N (pbc-0-3): https://www.dftb.org/parameters/pbc-0-3/

## Workflow steps

### Step 1: Construct initial structures
- Role: process
- Action: Construct unit-cell models for six 3D sp³ BN polymorphs: c-BN, bct-B₂N₂, bcc-B₄N₄, fcc-B₅N₅, sc-B₆N₆, t-B₈N₈. Use the described structural motifs (alternating B-N bonds, tetragonal B₂N₂ rings, B₄N₄ cubes, single sp³ B/N atoms) and the given lattice types (cubic, body-centered tetragonal, body-centered cubic, face-centered cubic, simple cubic, tetragonal). Generate input files in a format readable by DFTB+.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: SCC-DFTB geometry optimization
- Role: process
- Action: Run SCC-DFTB geometry optimization (relaxation of lattice parameters and atomic positions) for each polymorph using DFTB+ with the pbc-0-3 Slater-Koster parameters for B-N. Run until convergence. Save the final optimized structures and total energies.
- Evidence: `/app/outputs/optimization_results.json`

### Step 3: Compute structural and electronic properties
- Role: scored (load-bearing)
- Action: From the optimized geometries and electronic structure outputs of the six BN polymorphs, compute: number of atoms per unit cell Z, lattice parameters a and c (where applicable), unit-cell volume per atom V_uc (Å³/atom), total energy per atom relative to c-BN ΔE_tot (eV/atom), theoretical density ρ (g/cm³), compression modulus B (GPa) estimated via an equation of state, and change of forbidden band gap ΔE_g (eV) relative to c-BN. Write the results to properties.json.
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: JSON object with key 'polymorphs' (array of objects). Each object: polymorph_id (int), polymorph_name (string), Z (int), a (float, Å), c (float or null), V_uc (float, Å³/atom), ΔE_tot (float, eV/atom), ρ (float, g/cm³), B (float, GPa), ΔE_g (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Orbital character analysis of band edges
- Role: scored
- Action: Compute the projected (partial) density of states for each polymorph. Identify the dominant orbital character at the valence band maximum (VBM) and conduction band minimum (CBM). Write the assignments to dos_character.json. Also include a verification boolean indicating whether the character matches the expected trend: VBM dominated by N2p, CBM dominated by B2p for all polymorphs.
- Output file: `/app/outputs/dos_character.json`
- Format: json
- Contract: JSON object with keys: 'polymorphs' (array of objects, each with polymorph_id (int), polymorph_name (string), VBM_orbital (string), CBM_orbital (string)) and 'orbital_character_matches_paper' (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.json`
- `/app/outputs/dos_character.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed structural and electronic properties of six BN polymorphs.
- schema:
  - `type`: object
  - `required`:
    - `polymorphs`: array of objects
  - `items`:
    - `polymorph_id`: int
    - `polymorph_name`: string
    - `Z`: int
    - `a`: float (Å)
    - `c`: float or null
    - `V_uc`: float (Å³/atom)
    - `ΔE_tot`: float (eV/atom)
    - `ρ`: float (g/cm³)
    - `B`: float (GPa)
    - `ΔE_g`: float (eV)
  - `required_columns`:
  - `units`: object

### dos_character.json
- path: `/app/outputs/dos_character.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dominant orbital character of valence and conduction band edges and whether it matches the expected N2p/B2p pattern.
- schema:
  - `type`: object
  - `required`:
    - `polymorphs`: array of objects
    - `orbital_character_matches_paper`: boolean
  - `items`:
    - `polymorph_id`: int
    - `polymorph_name`: string
    - `VBM_orbital`: string
    - `CBM_orbital`: string
  - `required_columns`:
  - `units`: object

Notes: All values are compared to the paper's reported numbers within hidden tolerances that account for method/implementation differences. Structural trends (e.g., V_uc ordering) are also checked implicitly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "polymorphs": "array of objects"
        },
        "items": {
          "polymorph_id": "int",
          "polymorph_name": "string",
          "Z": "int",
          "a": "float (Å)",
          "c": "float or null",
          "V_uc": "float (Å³/atom)",
          "ΔE_tot": "float (eV/atom)",
          "ρ": "float (g/cm³)",
          "B": "float (GPa)",
          "ΔE_g": "float (eV)"
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Computed structural and electronic properties of six BN polymorphs."
    },
    {
      "file": "dos_character.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "polymorphs": "array of objects",
          "orbital_character_matches_paper": "boolean"
        },
        "items": {
          "polymorph_id": "int",
          "polymorph_name": "string",
          "VBM_orbital": "string",
          "CBM_orbital": "string"
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Dominant orbital character of valence and conduction band edges and whether it matches the expected N2p/B2p pattern."
    }
  ],
  "notes": "All values are compared to the paper's reported numbers within hidden tolerances that account for method/implementation differences. Structural trends (e.g., V_uc ordering) are also checked implicitly."
}
```

## How you are scored
Your outputs will be evaluated by a hidden automated verifier that independently compares each scored artifact against reference values derived from the original work. Each of the two scored files (properties.json and dos_character.json) contributes to the final score, with the properties file carrying the larger weight because it is the primary quantitative result. The verifier checks the numerical entries in properties.json for agreement within allowed tolerances (lattice parameters, volumes, densities, bulk moduli, and band gaps are compared with relative or absolute tolerances that account for method and implementation differences) and also verifies that the relative ordering of unit-cell volumes and energies across the six polymorphs matches the expected trend. The dos_character.json is checked for correct orbital assignments and the boolean verification flag. A perfect score is awarded when all computed quantities fall within the acceptable ranges and all structural trends are correctly reproduced; partial credit is given for partial matches. The process steps (structure construction and geometry optimization) are mandatory but are not themselves scored; they are required to reach the scored outputs.
