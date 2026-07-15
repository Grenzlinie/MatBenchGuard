# DFT-based surface relaxation and interface bonding of graphene on alpha-alumina

## Problem background
The interface between graphene and α‑Al₂O₃ is central to next‑generation electronics and to remote epitaxy of functional thin films. The nature of this interface — whether it is a simple van der Waals interaction or involves chemical bonding — has been controversial. Equally important, the presence of the interface may drastically alter the structural relaxation of the sapphire surface layers. Determining the actual bonding configuration (for example, a possible C‑O‑Al linkage) and quantifying the resulting interatomic distances and surface relaxation are key to understanding and exploiting 2D‑material‑based devices.

## Approach
We perform density functional theory (DFT) calculations using an open‑source periodic code. Two slab models are built: (a) a bare, Al‑terminated α‑Al₂O₃(0001) surface, and (b) a graphene/α‑Al₂O₃ interface in which a bridging oxygen atom is placed between the topmost Al of the sapphire and the graphene layer. The in‑plane lattice constant is fixed to that of α‑Al₂O₃; the graphene sheet is strained to match this lattice. Atomic positions are relaxed until forces are converged. From the relaxed geometries we compute: the distance between the topmost surface Al and the bridging O, the average distance between the bridging O and its nearest carbon neighbours, the adhesion energy of the interface (from total energies of the interface, an isolated graphene sheet, and the bare slab), and the first‑layer contraction of the sapphire — for both the bare surface and the interface. Comparing the bare and interface results reveals how the bridging oxygen and the graphene layer modify the surface relaxation.

## Reproduction target
Produce three scored artifacts:
1. `bare_surface_relaxed.xyz` – the fully relaxed geometry of the Al‑terminated α‑Al₂O₃(0001) slab (same number of layers as in the interface model).
2. `interface_relaxed.xyz` – the fully relaxed geometry of the graphene/α‑Al₂O₃ interface containing one bridging O per surface Al, the graphene sheet, and the sapphire slab.
3. `computed_properties.json` – a JSON file with the computed quantities: the Al–O distance (Å), the average O–C distance (Å), the three total energies (eV), the supercell area (Å²), the adhesion energy (J/m²), and the first‑layer contraction percentages for the interface and the bare surface.

Use the bulk α‑Al₂O₃ crystal structure from a public crystallographic database and the known lattice constant of free‑standing graphene. Perform the relaxations with a standard open‑source DFT code and pseudopotentials. Compute the adhesion energy as E_ad = (E_interface – E_graphene – E_bare_slab) / supercell_area, and the layer contraction relative to the bulk interlayer spacing.

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- α-Al₂O₃ bulk crystal structure
- Graphene lattice constant

## Workflow steps

### Step 1: Construct slab models
- Role: process
- Action: Build periodic slab supercells: (a) a bare Al-terminated α-Al₂O₃(0001) slab with 6–8 O–Al–Al–O triple layers and ≥15 Å vacuum; (b) an interface slab consisting of the same oxide slab plus one bridging O atom placed above each topmost surface Al and a graphene sheet (√3×√3)R30° strained to the sapphire lattice constant, placed above the bridging O layer. Output the initial unrelaxed atomic coordinates in a suitable format.
- Evidence: `/app/outputs/slab_models.txt`

### Step 2: Relax bare α-Al₂O₃(0001) surface
- Role: scored
- Action: Run DFT (pw.x) to relax the atomic positions of the bare Al-terminated slab while keeping the in-plane lattice fixed. Output the final relaxed coordinates.
- Output file: `/app/outputs/bare_surface_relaxed.xyz`
- Format: txt
- Contract: Standard XYZ format: first line = number of atoms, second line = comment, then one line per atom: element symbol, x, y, z (in Angstrom).
- Scoring: scored by hidden verifier

### Step 3: Relax Gr/α-Al₂O₃ interface with bridging O
- Role: scored (load-bearing)
- Action: Run DFT to relax the interface slab model (constructed in step_0) until forces are converged. Output the final relaxed coordinates.
- Output file: `/app/outputs/interface_relaxed.xyz`
- Format: txt
- Contract: Standard XYZ format: first line = number of atoms, second line = comment, then one line per atom: element symbol, x, y, z (in Angstrom).
- Scoring: scored by hidden verifier

### Step 4: Compute interface properties
- Role: scored
- Action: Post‑process the relaxed geometries and DFT total energies to extract: (a) the minimum Al–O distance (topmost surface Al to bridging O); (b) the average O–C distance (bridging O to nearest graphene C atoms); (c) the adhesion energy using the formula E_ad = (E_interface – E_graphene – E_bare_slab) / supercell_area, where the energies are obtained from single-point calculations on the relaxed structures; (d) the first-layer contraction (spacing change relative to bulk) for both the interface and the bare surface. Store all quantities in a JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: Keys: 'Al_O_distance' (float, Å), 'O_C_average_distance' (float, Å), 'interface_total_energy' (float, eV), 'graphene_total_energy' (float, eV), 'al2o3_slab_total_energy' (float, eV), 'supercell_area' (float, Å²), 'adhesion_energy' (float, J/m²), 'first_layer_contraction_interface' (float, %), 'first_layer_contraction_bare' (float, %).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bare_surface_relaxed.xyz`
- `/app/outputs/interface_relaxed.xyz`
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bare_surface_relaxed.xyz
- path: `/app/outputs/bare_surface_relaxed.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed coordinates of the bare α-Al₂O₃(0001) slab; the checker recomputes interlayer distances and first-layer contraction.
- schema:
  - `type`: text
  - `description`: Standard XYZ file: first line number of atoms, second line comment, then element x y z per line (Angstrom).

### interface_relaxed.xyz
- path: `/app/outputs/interface_relaxed.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed coordinates of the Gr/α-Al₂O₃ interface with bridging O; the checker recomputes Al–O distance, average O–C distance, and layer contractions.
- schema:
  - `type`: text
  - `description`: Standard XYZ file: first line number of atoms, second line comment, then element x y z per line (Angstrom).

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed geometric distances, total energies, adhesion energy, and layer contractions. The checker will recompute adhesion energy from the reported total energies and area, and compare distances and contractions to hidden references.
- schema:
  - `type`: object
  - `required`: `Al_O_distance`, `O_C_average_distance`, `interface_total_energy`, `graphene_total_energy`, `al2o3_slab_total_energy`, `supercell_area`, `adhesion_energy`, `first_layer_contraction_interface`, `first_layer_contraction_bare`
  - `properties`:
    - `Al_O_distance`:
      - `type`: number
      - `unit`: Angstrom
    - `O_C_average_distance`:
      - `type`: number
      - `unit`: Angstrom
    - `interface_total_energy`:
      - `type`: number
      - `unit`: eV
    - `graphene_total_energy`:
      - `type`: number
      - `unit`: eV
    - `al2o3_slab_total_energy`:
      - `type`: number
      - `unit`: eV
    - `supercell_area`:
      - `type`: number
      - `unit`: Angstrom^2
    - `adhesion_energy`:
      - `type`: number
      - `unit`: J/m^2
    - `first_layer_contraction_interface`:
      - `type`: number
      - `unit`: percent
    - `first_layer_contraction_bare`:
      - `type`: number
      - `unit`: percent

Notes: All geometric coordinates must be in Angstrom. The adhesion energy must be computed from the three total energies and supercell area, as defined in the workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bare_surface_relaxed.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Standard XYZ file: first line number of atoms, second line comment, then element x y z per line (Angstrom)."
      },
      "description": "Relaxed coordinates of the bare α-Al₂O₃(0001) slab; the checker recomputes interlayer distances and first-layer contraction."
    },
    {
      "file": "interface_relaxed.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Standard XYZ file: first line number of atoms, second line comment, then element x y z per line (Angstrom)."
      },
      "description": "Relaxed coordinates of the Gr/α-Al₂O₃ interface with bridging O; the checker recomputes Al–O distance, average O–C distance, and layer contractions."
    },
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "Al_O_distance",
          "O_C_average_distance",
          "interface_total_energy",
          "graphene_total_energy",
          "al2o3_slab_total_energy",
          "supercell_area",
          "adhesion_energy",
          "first_layer_contraction_interface",
          "first_layer_contraction_bare"
        ],
        "properties": {
          "Al_O_distance": {
            "type": "number",
            "unit": "Angstrom"
          },
          "O_C_average_distance": {
            "type": "number",
            "unit": "Angstrom"
          },
          "interface_total_energy": {
            "type": "number",
            "unit": "eV"
          },
          "graphene_total_energy": {
            "type": "number",
            "unit": "eV"
          },
          "al2o3_slab_total_energy": {
            "type": "number",
            "unit": "eV"
          },
          "supercell_area": {
            "type": "number",
            "unit": "Angstrom^2"
          },
          "adhesion_energy": {
            "type": "number",
            "unit": "J/m^2"
          },
          "first_layer_contraction_interface": {
            "type": "number",
            "unit": "percent"
          },
          "first_layer_contraction_bare": {
            "type": "number",
            "unit": "percent"
          }
        }
      },
      "description": "Computed geometric distances, total energies, adhesion energy, and layer contractions. The checker will recompute adhesion energy from the reported total energies and area, and compare distances and contractions to hidden references."
    }
  ],
  "notes": "All geometric coordinates must be in Angstrom. The adhesion energy must be computed from the three total energies and supercell area, as defined in the workflow."
}
```

## How you are scored
A hidden verifier independently examines each of the three scored files. From `bare_surface_relaxed.xyz` and `interface_relaxed.xyz`, the verifier recomputes the Al–O distance, the average O–C distance, and the first‑layer contractions. From `computed_properties.json`, the verifier recomputes the adhesion energy using the three total energies and the supercell area you supply, and cross‑checks the reported contraction values against the XYZ geometries. Each quantity is compared to a hidden reference value using a tolerance that allows for legitimate differences in implementation (functional, pseudopotential, code version) but excludes a random guess. The reward for each stage is combined by fixed weights to yield the final score. Simply reporting the paper’s values without a genuine DFT workflow will not pass; the verifier computes the metric from your raw artifacts.
