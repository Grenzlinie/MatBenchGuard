# DFT+U Prediction of Weyl Nodes in EuCd2As2

## Problem background
The layered intermetallic compound EuCd2As2 has been proposed as a candidate for a magnetic Weyl semimetal—a material in which topologically protected band crossings (Weyl nodes) appear when time-reversal symmetry is broken by a magnetic field. In the ferromagnetic state with Eu spins fully aligned along the c axis, ab initio electronic structure calculations predict that a band inversion creates non-degenerate bands crossing linearly near the Fermi level. This work investigates whether such Weyl nodes indeed form along the Γ-A high-symmetry line and determines their precise location, number, and chirality through first-principles computation.

## Approach
The computational approach is to perform a spin-polarised DFT+U calculation for EuCd2As2 in the fully spin-aligned ferromagnetic state (Eu spins parallel to the c axis). Using the experimentally known crystal structure, the GGA-PBE exchange-correlation functional, and a Hubbard U correction on the Eu 4f states to account for strong correlations, the band structure is computed along the Γ-A high-symmetry direction. Linear band crossings where singly degenerate conduction and valence bands meet are identified as Weyl nodes. For each crossing, the kz position (in units of 2π/c), the energy relative to the Fermi level, and the chirality (+1 or −1) are extracted. The chirality assignment follows from the sign of the Berry curvature flux through a small sphere surrounding the node. The resulting data—the list of Weyl nodes and the full raw band structure along Γ-A—are saved as scored artifacts.

## Reproduction target
Run a spin-polarised DFT+U calculation for EuCd2As2 with Eu spins fully aligned along the c axis, and extract the Weyl nodes from the computed band structure along the Γ-A path. The task is to determine (1) the kz positions (in units of 2π/c) of each Weyl node, (2) their energies relative to the Fermi level, and (3) their chirality. The primary scored artifact is the list of identified Weyl nodes, each described by its kz, energy, and chirality. The secondary artifact is the underlying band structure data along Γ-A, which must contain all bands and a fine kz grid covering the full segment from 0 to 0.5 r.l.u. The scoring will assess the correctness of the identified Weyl nodes.

## Assets

- Crystal structure of EuCd2As2: 10.1103/PhysRevB.97.214422
- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, ABINIT): https://www.quantum-espresso.org
- Pseudopotentials for Eu, Cd, As (e.g., SSSP or GBRV library): SSSP efficiency library

## Workflow steps

### Step 1: Run spin-polarized DFT+U calculation
- Role: process
- Action: Perform a spin-polarized DFT+U calculation for EuCd2As2 with Eu spins fully aligned along the c axis (ferromagnetic state). Use the provided crystal structure, the GGA-PBE functional, and a Hubbard U of 5 eV on Eu 4f states. Choose appropriate k-point mesh and energy cutoff. Compute the band structure along the Γ-A high-symmetry line with fine k-point sampling.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: Extract Weyl nodes
- Role: scored (load-bearing)
- Action: From the computed band structure along Γ-A, identify linear band crossings where singly degenerate conduction and valence bands touch. Extract the kz positions (in units of 2π/c), energies (eV relative to the Fermi level), and chirality (±1) of each Weyl node. Report exactly two nodes symmetric in kz, with opposite chirality.
- Output file: `/app/outputs/step_01_weyl_nodes.json`
- Format: json
- Contract: Array of objects, each with keys: "kz" (float, units 2π/c), "energy" (float, eV relative to EF), "chirality" (int, 1 or -1).
- Scoring: scored by hidden verifier

### Step 3: Save band structure along Γ-A
- Role: scored
- Action: Save the full computed band structure along the Γ-A line for all bands. Cover kz from 0 to 0.5 in units of 2π/c with at least 100 evenly spaced points. Include band index and energy for each k-point.
- Output file: `/app/outputs/step_02_band_structure.csv`
- Format: csv
- Contract: CSV with columns: "kz" (float, in units of 2π/c), "band_index" (int), "energy" (float, eV). Must contain all bands, with kz values covering the full segment from 0 to 0.5, at least 100 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_weyl_nodes.json`
- `/app/outputs/step_02_band_structure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_weyl_nodes.json
- path: `/app/outputs/step_01_weyl_nodes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The primary scored artifact: a list of Weyl nodes (kz, energy, chirality) extracted from the DFT+U band structure. Checked against expected positions within tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `kz`, `energy`, `chirality`
    - `properties`:
      - `kz`:
        - `type`: number
        - `description`: k_z position in units of 2π/c
      - `energy`:
        - `type`: number
        - `description`: energy in eV relative to the Fermi level (positive above EF)
      - `chirality`:
        - `type`: integer
        - `enum`: `1`, `-1`
        - `description`: chirality of the node (1 for source, -1 for sink)

### step_02_band_structure.csv
- path: `/app/outputs/step_02_band_structure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Supporting raw band structure data along Γ-A. Audited for format, column completeness, and kz range; may be used to recompute Weyl node positions for consistency.
- schema:
  - `type`: table
  - `required_columns`: `kz`, `band_index`, `energy`
  - `units`:
    - `kz`: units of 2π/c
    - `energy`: eV

Notes: This task reproduces the DFT+U computation of Weyl nodes in EuCd2As2. The agent must perform a spin-polarized DFT+U calculation using an open-source code, then identify Weyl nodes along Γ-A. The primary scored artifact is the list of nodes, verified against the paper's predicted positions. The band structure CSV enables recomputation of nodes for cross-check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_weyl_nodes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "kz",
            "energy",
            "chirality"
          ],
          "properties": {
            "kz": {
              "type": "number",
              "description": "k_z position in units of 2π/c"
            },
            "energy": {
              "type": "number",
              "description": "energy in eV relative to the Fermi level (positive above EF)"
            },
            "chirality": {
              "type": "integer",
              "enum": [
                1,
                -1
              ],
              "description": "chirality of the node (1 for source, -1 for sink)"
            }
          }
        }
      },
      "description": "The primary scored artifact: a list of Weyl nodes (kz, energy, chirality) extracted from the DFT+U band structure. Checked against expected positions within tolerances."
    },
    {
      "file": "step_02_band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kz",
          "band_index",
          "energy"
        ],
        "units": {
          "kz": "units of 2π/c",
          "energy": "eV"
        }
      },
      "description": "Supporting raw band structure data along Γ-A. Audited for format, column completeness, and kz range; may be used to recompute Weyl node positions for consistency."
    }
  ],
  "notes": "This task reproduces the DFT+U computation of Weyl nodes in EuCd2As2. The agent must perform a spin-polarized DFT+U calculation using an open-source code, then identify Weyl nodes along Γ-A. The primary scored artifact is the list of nodes, verified against the paper's predicted positions. The band structure CSV enables recomputation of nodes for cross-check."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each scored artifact. The Weyl node list (step_01_weyl_nodes.json) is checked for the correct number of nodes, their symmetry, chirality signs, and that their kz positions and energies fall within acceptable ranges—these ranges are set to accommodate the natural spread that occurs when re-running DFT+U calculations with different open-source codes. The band structure CSV (step_02_band_structure.csv) is audited for format, completeness (at least 100 k-points, correct columns), and the verifier may recompute band crossings from it to cross-check consistency with the reported nodes. Both artifacts contribute to the final reward, which is a weighted sum; correctly identifying the Weyl nodes (number, positions, energies, chirality) earns full credit, while significant deviations reduce the score proportionally.
