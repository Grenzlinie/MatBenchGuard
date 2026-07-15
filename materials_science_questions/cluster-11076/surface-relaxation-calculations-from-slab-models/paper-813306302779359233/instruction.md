# Surface relaxation calculations from slab models

## Problem background
Tungsten (W) surfaces are central to thin-film growth and interface engineering. First-principles calculations can quantify surface stability through interlayer relaxation, surface energy, and electronic density of states (DOS). This task requires a computational reproduction that determines the relative stability of the three low-index W surfaces — (001), (110), and (111) — by computing these quantities from scratch using density functional theory (DFT).

## Approach
The workflow employs plane-wave pseudopotential DFT within the generalized gradient approximation (GGA-PBE). First, the bulk bcc W crystal is fully optimized to obtain the equilibrium lattice constant and the energy per atom. Using this lattice constant, 7-layer slab supercells are built for the (001), (110), and (111) surfaces, each with a vacuum width of 16 Å. The atomic positions in every slab are relaxed until convergence. From the relaxed geometries, interlayer spacing changes are converted into percentage relaxations Δ12, Δ23, Δ34, and their sum Δ14, using the unrelaxed bulk-derived spacings as reference. Surface energies are obtained from E_surf = (E_slab − n·E_bulk) / (2A), where E_slab is the relaxed slab total energy, n is the number of W atoms, and A is the surface area. Finally, the total density of states is computed for each relaxed surface, and the DOS value at the Fermi level, n(E_F), is extracted. Comparing these properties across the three surfaces reveals the stability ordering.

## Reproduction target
Produce a single JSON file, /app/outputs/surface_results.json, containing for each surface — W(001), W(110), W(111) — the interlayer relaxation percentages delta_12, delta_23, delta_34, delta_14, the surface_energy (in eV/Å²), and the dos_at_fermi (in states/eV). A hidden verifier will check that the file has the required structure and that the computed values respect a specific stability ordering among the three surfaces: the magnitudes of Δ14, the surface energies, and the Fermi-level DOS must follow a consistent trend. Meeting this structural audit condition earns full credit.

## Assets

- Quantum ESPRESSO (or equivalent plane-wave DFT code): https://www.quantum-espresso.org
- W pseudopotential (GGA-PBE ultrasoft or PAW): http://pseudopotentials.quantum-espresso.org

## Workflow steps

### Step 1: Bulk W optimization
- Role: process
- Action: Perform DFT optimization of bulk bcc W using a plane-wave pseudopotential code with GGA-PBE exchange-correlation. Obtain the equilibrium lattice constant and bulk energy per atom.
- Evidence: `/app/outputs/bulk_result.json`

### Step 2: Slab model construction
- Role: process
- Action: Using the optimized lattice constant, construct 7-layer slab supercells for W(001), W(110), and W(111) surfaces with a vacuum width of 16 Å. Generate the crystal structures in a format readable by the DFT code.
- Evidence: `/app/outputs/slab_structures.cif`

### Step 3: DFT slab relaxation
- Role: process
- Action: Perform full ionic relaxation of each slab (atomic positions only, cell fixed) using GGA-PBE. Continue until force and energy convergence criteria are met. Record relaxed total energies and final atomic coordinates.
- Evidence: `/app/outputs/relaxed_energies.json`

### Step 4: Electronic DOS calculation
- Role: process
- Action: Using the relaxed structures, perform a DFT calculation to compute the total density of states (DOS) for each surface. Extract the DOS value at the Fermi level.
- Evidence: `/app/outputs/dos_results.json`

### Step 5: Aggregate surface properties and report
- Role: scored (load-bearing)
- Action: From the bulk reference, relaxed geometries, slab total energies, and DOS outputs, compute: (a) interlayer relaxation percentages Δ12, Δ23, Δ34, Δ14 for each surface using the unrelaxed bulk interlayer spacings; (b) surface energies E_surf = (E_slab - n·E_bulk)/(2A); (c) Fermi‑level DOS values. Write all quantities to surface_results.json.
- Output file: `/app/outputs/surface_results.json`
- Format: json
- Contract: {"type":"object","properties":{"W(001)":{"type":"object","properties":{"delta_12":{"type":"number","unit":"%"},"delta_23":{"type":"number","unit":"%"},"delta_34":{"type":"number","unit":"%"},"delta_14":{"type":"number","unit":"%"},"surface_energy":{"type":"number","unit":"eV/Å²"},"dos_at_fermi":{"type":"number","unit":"states/eV"}},"required":["delta_12","delta_23","delta_34","delta_14","surface_energy","dos_at_fermi"]},"W(110)":{"$ref":"#/properties/W(001)"},"W(111)":{"$ref":"#/properties/W(001)"}},"required":["W(001)","W(110)","W(111)"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_results.json
- path: `/app/outputs/surface_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed interlayer relaxations, surface energies, and Fermi-level DOS for the three surfaces. The checker verifies the stability orderings: |Δ14(110)| < |Δ14(111)| < |Δ14(001)|, E_surf(110) < E_surf(111) < E_surf(001), and n(E_F,110) < n(E_F,111) < n(E_F,001).
- schema:
  - `type`: object
  - `properties`:
    - `W(001)`:
      - `type`: object
      - `properties`:
        - `delta_12`:
          - `type`: number
          - `unit`: %
        - `delta_23`:
          - `type`: number
          - `unit`: %
        - `delta_34`:
          - `type`: number
          - `unit`: %
        - `delta_14`:
          - `type`: number
          - `unit`: %
        - `surface_energy`:
          - `type`: number
          - `unit`: eV/Å²
        - `dos_at_fermi`:
          - `type`: number
          - `unit`: states/eV
      - `required`: `delta_12`, `delta_23`, `delta_34`, `delta_14`, `surface_energy`, `dos_at_fermi`
    - `W(110)`:
      - `$ref`: #/properties/W(001)
    - `W(111)`:
      - `$ref`: #/properties/W(001)
  - `required`: `W(001)`, `W(110)`, `W(111)`

Notes: Only the aggregate file is scored; intermediate outputs listed in the steps (bulk_result.json, slab_structures.cif, relaxed_energies.json, dos_results.json) are evidence of process execution but are not part of the scored output contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "W(001)": {
            "type": "object",
            "properties": {
              "delta_12": {
                "type": "number",
                "unit": "%"
              },
              "delta_23": {
                "type": "number",
                "unit": "%"
              },
              "delta_34": {
                "type": "number",
                "unit": "%"
              },
              "delta_14": {
                "type": "number",
                "unit": "%"
              },
              "surface_energy": {
                "type": "number",
                "unit": "eV/Å²"
              },
              "dos_at_fermi": {
                "type": "number",
                "unit": "states/eV"
              }
            },
            "required": [
              "delta_12",
              "delta_23",
              "delta_34",
              "delta_14",
              "surface_energy",
              "dos_at_fermi"
            ]
          },
          "W(110)": {
            "$ref": "#/properties/W(001)"
          },
          "W(111)": {
            "$ref": "#/properties/W(001)"
          }
        },
        "required": [
          "W(001)",
          "W(110)",
          "W(111)"
        ]
      },
      "description": "Computed interlayer relaxations, surface energies, and Fermi-level DOS for the three surfaces. The checker verifies the stability orderings: |Δ14(110)| < |Δ14(111)| < |Δ14(001)|, E_surf(110) < E_surf(111) < E_surf(001), and n(E_F,110) < n(E_F,111) < n(E_F,001)."
    }
  ],
  "notes": "Only the aggregate file is scored; intermediate outputs listed in the steps (bulk_result.json, slab_structures.cif, relaxed_energies.json, dos_results.json) are evidence of process execution but are not part of the scored output contract."
}
```

## How you are scored
A hidden verifier inspects the output artifacts. The primary scored artifact is surface_results.json. The verifier confirms that it is a well-formed JSON with all mandatory fields and that, for each surface, every numeric quantity is present. It then evaluates whether the computed |Δ14| values, surface energies, and Fermi-level DOS satisfy a predetermined ordering across W(001), W(110), and W(111). Correctly fulfilling all three orderings gives the maximum score; partial credit may be awarded if only some are correct. Intermediate evidence files (bulk_result.json, slab_structures.cif, relaxed_energies.json, dos_results.json) are recorded for completeness but are not directly weighted in the final reward. The final score is a real number between 0 (failure) and 1 (perfect reproduction) that combines these checks.
