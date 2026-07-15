# Reproducing HSE06 band gaps and Z₂ invariants of fluoride-terminated MXene topological insulators

## Problem background
Two-dimensional topological insulators (TIs) are materials with insulating bulk and conducting edge states, promising for quantum spin-Hall effects. MXenes are a family of 2D transition metal carbides/nitrides that can be functionalized with various surface terminations. First-principles density-functional theory (DFT) studies have predicted that certain ordered double-transition-metal carbide MXenes may host topological phases. Determining whether specific fluoride-terminated compounds exhibit a band gap and a non-trivial topological invariant is essential for assessing their viability as 2D TIs. This task reproduces the computational evaluation of the topological properties of nine such compounds.

## Approach
The workflow uses first-principles DFT with the Perdew-Burke-Ernzerhof (PBE) functional and the hybrid Heyd-Scuseria-Ernzerhof (HSE06) functional, both including spin-orbit coupling (SOC). Starting from the known hexagonal crystal structure (space group P-3m1) of ordered double-transition-metal MXenes with fluorine terminations, each structure is relaxed to its equilibrium geometry. Electronic band structures are then computed with PBE+SOC to determine the Z2 topological invariant via parity analysis of wavefunctions at time-reversal-invariant momenta, and to obtain the PBE band gaps. Finally, HSE06+SOC calculations provide more accurate band gaps. The nine compounds are all combinations of M' = V, Nb, Ta with M'' = Ti, Zr, Hf in the formula M'2M''C2F2.

## Reproduction target
For each of the nine fluoride-terminated compounds (V2TiC2F2, V2ZrC2F2, V2HfC2F2, Nb2TiC2F2, Nb2ZrC2F2, Nb2HfC2F2, Ta2TiC2F2, Ta2ZrC2F2, Ta2HfC2F2), compute the optimized lattice constant (Å), Z2 topological invariant (0 or 1), PBE system band gap (meV), HSE06 system band gap (meV), and HSE06 band gap at the Γ point (meV). Assemble these results into a JSON array of objects, one per compound, with the fields: compound, lattice_constant, Z2, pbe_system_gap, hse06_system_gap, hse06_gamma_gap. The output must be saved as /app/outputs/hse06_results.json.

## Assets

- DFT code (Quantum ESPRESSO or VASP): https://www.quantum-espresso.org/
- Pseudopotential library for PBE and HSE06: https://www.materialscloud.org/discover/sssp/
- MXene crystal structure prototype

## Workflow steps

### Step 1: Structure generation and relaxation
- Role: process
- Action: Generate the atomic structures for the nine M'₂M''C₂F₂ compounds (M' = V, Nb, Ta; M'' = Ti, Zr, Hf) in the hexagonal P‑3m1 space group, with F atoms at the preferred adsorption site (site B or C as identified in the literature). Relax each structure using DFT with the PBE functional until forces are < 1e‑3 eV/Å. Document the relaxed geometries.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: PBE band structure and Z₂ invariant computation
- Role: process
- Action: Using the relaxed structures, compute electronic band structures with spin‑orbit coupling and the PBE functional. Determine the Z₂ topological invariant via parity analysis of wavefunctions at the time‑reversal‑invariant momenta (Γ, M, K). Record the PBE system band gap and Γ‑point gap for each compound.
- Evidence: `/app/outputs/pbe_z2.log`

### Step 3: HSE06 calculation and final results assembly
- Role: scored (load-bearing)
- Action: For each relaxed structure, perform a hybrid‑functional HSE06+SOC band structure calculation. Compile the results into a JSON file containing, for each compound, the compound name, optimized lattice constant (Å), Z₂ invariant (0 or 1), PBE system band gap (meV), HSE06 system band gap (meV), and HSE06 Γ‑point band gap (meV). Save as /app/outputs/hse06_results.json.
- Output file: `/app/outputs/hse06_results.json`
- Format: json
- Contract: Array of objects: [ { compound: string, lattice_constant: float, Z2: integer, pbe_system_gap: float, hse06_system_gap: float, hse06_gamma_gap: float } ] with exactly nine entries.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hse06_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hse06_results.json
- path: `/app/outputs/hse06_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled HSE06 band gaps and Z₂ topological invariants for the nine M'₂M''C₂F₂ compounds; the checker compares hse06_system_gap and Z2 against hidden reference data.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `lattice_constant`, `Z2`, `pbe_system_gap`, `hse06_system_gap`, `hse06_gamma_gap`
    - `properties`:
      - `compound`:
        - `type`: string
      - `lattice_constant`:
        - `type`: float
        - `units`: Å
      - `Z2`:
        - `type`: integer
        - `enum`: `0`, `1`
      - `pbe_system_gap`:
        - `type`: float
        - `units`: meV
      - `hse06_system_gap`:
        - `type`: float
        - `units`: meV
      - `hse06_gamma_gap`:
        - `type`: float
        - `units`: meV
  - `required`: object
  - `required_columns`:

Notes: The nine expected compound names are: V2TiC2F2, V2ZrC2F2, V2HfC2F2, Nb2TiC2F2, Nb2ZrC2F2, Nb2HfC2F2, Ta2TiC2F2, Ta2ZrC2F2, Ta2HfC2F2. Lattice constants and PBE gaps are checked for basic plausibility but not strictly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hse06_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "lattice_constant",
            "Z2",
            "pbe_system_gap",
            "hse06_system_gap",
            "hse06_gamma_gap"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "lattice_constant": {
              "type": "float",
              "units": "Å"
            },
            "Z2": {
              "type": "integer",
              "enum": [
                0,
                1
              ]
            },
            "pbe_system_gap": {
              "type": "float",
              "units": "meV"
            },
            "hse06_system_gap": {
              "type": "float",
              "units": "meV"
            },
            "hse06_gamma_gap": {
              "type": "float",
              "units": "meV"
            }
          }
        },
        "required": {},
        "required_columns": []
      },
      "description": "Compiled HSE06 band gaps and Z₂ topological invariants for the nine M'₂M''C₂F₂ compounds; the checker compares hse06_system_gap and Z2 against hidden reference data."
    }
  ],
  "notes": "The nine expected compound names are: V2TiC2F2, V2ZrC2F2, V2HfC2F2, Nb2TiC2F2, Nb2ZrC2F2, Nb2HfC2F2, Ta2TiC2F2, Ta2ZrC2F2, Ta2HfC2F2. Lattice constants and PBE gaps are checked for basic plausibility but not strictly scored."
}
```

## How you are scored
A hidden verifier reads the JSON file and independently evaluates each compound’s reported values. The primary check compares the HSE06 system band gaps against reference values with an appropriate tolerance that accounts for legitimate differences between DFT implementations. The Z2 invariants are verified to match the expected topological classification (0 or 1) for each compound. Additional plausibility checks are applied to the lattice constants and PBE gaps. The verifier combines these checks into a single reward score; reporting numbers without genuine computation will not pass the tolerance criteria and will yield a low score. The exact tolerances and reference values are not disclosed.
