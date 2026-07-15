# Ab initio structural, magnetic, and transport properties of Co3Sn2S2 thin films

## Problem background
Co3Sn2S2 is a quasi-two-dimensional kagome-lattice ferromagnet that hosts Weyl nodes and exhibits a large intrinsic anomalous Hall effect (AHE) and anomalous Nernst effect (ANE). Thin films of this material may realize the quantum anomalous Hall effect, but how the structural, magnetic, and topological transport properties evolve with film thickness and surface termination (Sn-end vs S-end) is not well understood. This task investigates these properties by performing first-principles density functional theory (DFT) calculations on thin films with one, two, and three Co kagome layers, using both Sn and S surface terminations, and comparing with the bulk reference.

## Approach
The workflow follows a multi-stage computational protocol. First, slab models are built from the bulk experimental lattice constants and relaxed using nonrelativistic DFT with the PBE functional and norm-conserving pseudopotentials, optimizing atomic positions and in-plane lattice vectors. For each relaxed geometry, relativistic DFT calculations including spin-orbit coupling are performed for several candidate magnetic configurations (ferromagnetic, noncollinear, interlayer antiferromagnetic/ferrimagnetic) to identify the lowest-energy magnetic ground state and to extract Co local magnetic moments via Mulliken population analysis. From the ground-state electronic structure, maximally-localized Wannier functions (Co d, Sn s/p, S p orbitals) are constructed to obtain tight-binding Hamiltonians. Finally, the anomalous Hall conductivity (σH) at the Fermi level and the anomalous Nernst conductivity (αN) at a temperature of kBT = 5 meV are computed via the Kubo formula on dense k-point grids. The calculations are carried out with the open‑source DFT code OpenMX.

## Reproduction target
Produce a JSON file containing, for each of the following systems, the optimized in‑plane lattice constant (Å), the Co layer distance (Å, null for monolayers), the magnetic ground state (a descriptive string), the Co local magnetic moment(s) per ion (µB, either a single number or an array of layer‑resolved values), the anomalous Hall conductivity σH at the Fermi level (units of e²/h), and the anomalous Nernst conductivity αN at kBT = 5 meV (units of (e/ħ)·(kB/e)):
sn_end_monolayer, sn_end_bilayer, sn_end_trilayer,
s_end_monolayer, s_end_bilayer, s_end_trilayer, and bulk.

## Assets

- OpenMX: http://www.openmx-square.org

## Workflow steps

### Step 1: Build initial slab models
- Role: process
- Action: Construct initial slab geometries for monolayer, bilayer, and trilayer Co3Sn2S2 films with Sn and S surface terminations using bulk experimental lattice constants (a=5.358 Å, c=13.123 Å) and a vacuum spacing >15 Å. Prepare input files for structural relaxation.
- Evidence: none

### Step 2: DFT structural optimization (nonrelativistic)
- Role: process
- Action: Perform nonrelativistic DFT structural optimization with PBE functional, norm-conserving pseudopotentials, and quasi-Newton algorithm until forces < 0.01 eV/Å. Relax atomic positions and in-plane lattice vectors for each thin film system. Use ferromagnetic initial state for all except S-end bilayer (interlayer AFM) and S-end trilayer (interlayer ferrimagnetic).
- Evidence: none

### Step 3: Determine magnetic ground state (relativistic)
- Role: process
- Action: For each optimized geometry, run fully relativistic DFT calculations including spin-orbit coupling for multiple candidate magnetic configurations (FM along c, a, b'; 120-degree noncollinear; interlayer arrangements). Identify the lowest-energy magnetic state and compute Co local magnetic moments via Mulliken population analysis.
- Evidence: none

### Step 4: Construct Wannier tight-binding models
- Role: process
- Action: Project relativistic DFT Bloch states onto maximally-localized Wannier functions (Co d, Sn s/p, S p orbitals) for the ground-state magnetic configuration. Construct tight-binding Hamiltonians that reproduce the DFT band structure within chosen inner windows.
- Evidence: none

### Step 5: Compute anomalous Hall and Nernst conductivities
- Role: process
- Action: Using the tight-binding models, compute the anomalous Hall conductivity σH and anomalous Nernst conductivity αN via the Kubo formula on dense k-point grids. Evaluate σH at zero temperature (Fermi level) and αN at temperature k_B T = 5 meV for each system.
- Evidence: none

### Step 6: Compile final reproduction results
- Role: scored (load-bearing)
- Action: Compile the optimized in-plane lattice constant, Co layer distance, magnetic ground state, Co magnetic moment(s), anomalous Hall conductivity at Fermi level, and anomalous Nernst conductivity at 5 meV for each of the six thin film systems and the bulk reference. Write the results to /app/outputs/reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: {"type":"object","required":["bulk","sn_end_monolayer","sn_end_bilayer","sn_end_trilayer","s_end_monolayer","s_end_bilayer","s_end_trilayer"],"additionalProperties":false,"properties":{"bulk":{"$ref":"#/definitions/system_entry"},"sn_end_monolayer":{"$ref":"#/definitions/system_entry"},"sn_end_bilayer":{"$ref":"#/definitions/system_entry"},"sn_end_trilayer":{"$ref":"#/definitions/system_entry"},"s_end_monolayer":{"$ref":"#/definitions/system_entry"},"s_end_bilayer":{"$ref":"#/definitions/system_entry"},"s_end_trilayer":{"$ref":"#/definitions/system_entry"}},"definitions":{"system_entry":{"type":"object","required":["in_plane_lattice_const_A","co_layer_distance_A","magnetic_state","co_moment_muB","anomalous_hall_conductivity_e2_per_h","anomalous_nernst_conductivity_kB_T_5meV"],"additionalProperties":false,"properties":{"in_plane_lattice_const_A":{"type":"number","description":"Optimized in-plane lattice constant (\u00c5)"},"co_layer_distance_A":{"type":["number","null"],"description":"Co layer distance (\u00c5); null for monolayer"},"magnetic_state":{"type":"string","description":"Magnetic ground state description, e.g. 'FM \u2225 c', 'interlayer AFM \u2225 b''', 'interlayer ferri \u2225 c'"},"co_moment_muB":{"type":["number","array"],"description":"Co local magnetic moment per ion in \u00ce\u00bcB. For multi-layer systems an array of layer-resolved values.","items":{"type":"number"}},"anomalous_hall_conductivity_e2_per_h":{"type":"number","description":"Anomalous Hall conductivity \u03c3H at Fermi level in units of e\u00b2/h"},"anomalous_nernst_conductivity_kB_T_5meV":{"type":"number","description":"Anomalous Nernst conductivity \u03b1N at k_B T = 5 meV in units of (e/\u0127)*(kB/e)"}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final scored artifact containing all target quantities: optimized structural parameters, magnetic ground state, magnetic moments, and transport conductivities for the six thin-film systems and the bulk reference.
- schema:
  - `type`: object
  - `required`: `bulk`, `sn_end_monolayer`, `sn_end_bilayer`, `sn_end_trilayer`, `s_end_monolayer`, `s_end_bilayer`, `s_end_trilayer`
  - `additionalProperties`: False
  - `properties`:
    - `bulk`:
      - `$ref`: #/definitions/system_entry
    - `sn_end_monolayer`:
      - `$ref`: #/definitions/system_entry
    - `sn_end_bilayer`:
      - `$ref`: #/definitions/system_entry
    - `sn_end_trilayer`:
      - `$ref`: #/definitions/system_entry
    - `s_end_monolayer`:
      - `$ref`: #/definitions/system_entry
    - `s_end_bilayer`:
      - `$ref`: #/definitions/system_entry
    - `s_end_trilayer`:
      - `$ref`: #/definitions/system_entry
  - `definitions`:
    - `system_entry`:
      - `type`: object
      - `required`: `in_plane_lattice_const_A`, `co_layer_distance_A`, `magnetic_state`, `co_moment_muB`, `anomalous_hall_conductivity_e2_per_h`, `anomalous_nernst_conductivity_kB_T_5meV`
      - `additionalProperties`: False
      - `properties`:
        - `in_plane_lattice_const_A`:
          - `type`: number
          - `description`: Optimized in-plane lattice constant (Å)
        - `co_layer_distance_A`:
          - `type`: `number`, `null`
          - `description`: Co layer distance (Å); null for monolayer
        - `magnetic_state`:
          - `type`: string
          - `description`: Magnetic ground state description, e.g. 'FM ∥ c', 'interlayer AFM ∥ b''', 'interlayer ferri ∥ c'
        - `co_moment_muB`:
          - `type`: `number`, `array`
          - `description`: Co local magnetic moment per ion in μB. For multi-layer systems an array of layer-resolved values.
          - `items`:
            - `type`: number
        - `anomalous_hall_conductivity_e2_per_h`:
          - `type`: number
          - `description`: Anomalous Hall conductivity σH at Fermi level in units of e²/h
        - `anomalous_nernst_conductivity_kB_T_5meV`:
          - `type`: number
          - `description`: Anomalous Nernst conductivity αN at k_B T = 5 meV in units of (e/ħ)*(kB/e)

Notes: The checker compares each numerical field to the hidden paper-reported values with predetermined tolerances. The magnetic_state field is compared by exact case-insensitive string match. The co_moment_muB field may be a single number or an array of layer-resolved values; the checker compares each value individually.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bulk",
          "sn_end_monolayer",
          "sn_end_bilayer",
          "sn_end_trilayer",
          "s_end_monolayer",
          "s_end_bilayer",
          "s_end_trilayer"
        ],
        "additionalProperties": false,
        "properties": {
          "bulk": {
            "$ref": "#/definitions/system_entry"
          },
          "sn_end_monolayer": {
            "$ref": "#/definitions/system_entry"
          },
          "sn_end_bilayer": {
            "$ref": "#/definitions/system_entry"
          },
          "sn_end_trilayer": {
            "$ref": "#/definitions/system_entry"
          },
          "s_end_monolayer": {
            "$ref": "#/definitions/system_entry"
          },
          "s_end_bilayer": {
            "$ref": "#/definitions/system_entry"
          },
          "s_end_trilayer": {
            "$ref": "#/definitions/system_entry"
          }
        },
        "definitions": {
          "system_entry": {
            "type": "object",
            "required": [
              "in_plane_lattice_const_A",
              "co_layer_distance_A",
              "magnetic_state",
              "co_moment_muB",
              "anomalous_hall_conductivity_e2_per_h",
              "anomalous_nernst_conductivity_kB_T_5meV"
            ],
            "additionalProperties": false,
            "properties": {
              "in_plane_lattice_const_A": {
                "type": "number",
                "description": "Optimized in-plane lattice constant (Å)"
              },
              "co_layer_distance_A": {
                "type": [
                  "number",
                  "null"
                ],
                "description": "Co layer distance (Å); null for monolayer"
              },
              "magnetic_state": {
                "type": "string",
                "description": "Magnetic ground state description, e.g. 'FM ∥ c', 'interlayer AFM ∥ b''', 'interlayer ferri ∥ c'"
              },
              "co_moment_muB": {
                "type": [
                  "number",
                  "array"
                ],
                "description": "Co local magnetic moment per ion in μB. For multi-layer systems an array of layer-resolved values.",
                "items": {
                  "type": "number"
                }
              },
              "anomalous_hall_conductivity_e2_per_h": {
                "type": "number",
                "description": "Anomalous Hall conductivity σH at Fermi level in units of e²/h"
              },
              "anomalous_nernst_conductivity_kB_T_5meV": {
                "type": "number",
                "description": "Anomalous Nernst conductivity αN at k_B T = 5 meV in units of (e/ħ)*(kB/e)"
              }
            }
          }
        }
      },
      "description": "Final scored artifact containing all target quantities: optimized structural parameters, magnetic ground state, magnetic moments, and transport conductivities for the six thin-film systems and the bulk reference."
    }
  ],
  "notes": "The checker compares each numerical field to the hidden paper-reported values with predetermined tolerances. The magnetic_state field is compared by exact case-insensitive string match. The co_moment_muB field may be a single number or an array of layer-resolved values; the checker compares each value individually."
}
```

## How you are scored
A hidden verifier compares each numerical field in your submitted reproduction_results.json to reference values (hidden tolerances). The magnetic_state field is compared by exact case‑insensitive string match. For multi‑layer systems, each layer’s moment is compared individually. The reward is the fraction of systems for which all fields meet the required accuracy. You must genuinely execute the DFT workflow; reporting paper‑reported numbers without performing the computations will not satisfy the scoring criteria.
