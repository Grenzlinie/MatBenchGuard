# DFT Formation Energies and Lattice Parameters of Ge-Ti Intermetallic Compounds

## Problem background
Intermetallic compounds in the Ge–Ti system are of interest for phase diagram construction and thermodynamic modeling. First‑principles density functional theory (DFT) calculations can provide zero‑temperature formation enthalpies and stability rankings of candidate crystal structures without recourse to experimental calorimetry. This task reduces the computational component of such a study: using DFT to compute total energies, formation enthalpies, relaxed lattice parameters, and the convex hull stability of selected Ge–Ti intermetallic phases. Reproducing these quantities verifies the predictive power of the computational protocol.

## Approach
The approach is a self‑contained computational workflow. Starting from crystal structure prototypes for the target compounds (Ge₃Ti₅, Ge₄Ti₅, Ge₅Ti₆, Ge₂Ti) and the elemental reference phases Ge (diamond A4) and Ti (hcp A3), you will perform DFT total‑energy calculations under the generalized gradient approximation (GGA) with the Perdew–Wang 1991 (PW91) functional and the projector‑augmented‑wave (PAW) method. After full relaxation of cell volume and atomic positions, you will obtain the total energy per cell and the relaxed lattice parameters for each system. Using the composition‑weighted subtraction of the elemental reference energies, you will compute the formation enthalpy (kJ per mol of atoms) for each compound. Finally, from these formation enthalpies you will construct the zero‑temperature convex hull of formation enthalpy vs. Ge atomic fraction and determine which compounds lie on the hull, verifying whether the Ge₄Ti₅ phase (Ge₄Sm₅ prototype) is among them. All computations must use open‑source DFT codes and publicly available pseudopotentials and crystal structures; the workflow does not depend on any proprietary software.

## Reproduction target
Produce two artifacts under `/app/outputs`:
- `formation_enthalpies.json`: For each of the four compounds Ge₃Ti₅ (Mn₅Si₃‑type), Ge₄Ti₅ (Ge₄Sm₅‑type), Ge₅Ti₆ (Si₅V₆‑type), Ge₂Ti (TiSi₂‑type) and the pure elements Ge (diamond A4) and Ti (hcp A3), report the total energy per cell (eV), number of atoms, relaxed lattice parameters (a, b, c in Å), and the formation enthalpy (kJ per mol of atoms).
- `convex_hull_analysis.json`: From the computed formation enthalpies, construct the zero‑K convex hull, list the compounds that lie on the hull, and state whether Ge₄Ti₅ is on the hull (boolean).

All quantities must be derived from the DFT total energies that you compute; the formation enthalpies and the convex hull must be internally consistent.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, ABINIT): https://www.quantum-espresso.org/
- PAW pseudopotential library for PW91 (e.g., PSlibrary): https://github.com/dalcorso/pslibrary
- Crystal structure prototypes for Ge-Ti compounds and pure elements: https://materialsproject.org

## Workflow steps

### Step 1: DFT relaxation and total energy calculation
- Role: process
- Action: Retrieve crystal structures for diamond Ge, hcp Ti, Ge3Ti5 (Mn5Si3-type), Ge4Ti5 (Ge4Sm5-type), Ge5Ti6 (Si5V6-type), and Ge2Ti (TiSi2-type) from public databases. Set up and run DFT calculations using the PW91 GGA functional with PAW pseudopotentials, a plane-wave cutoff of at least 300 eV, and a k-point mesh rule: (number of k-points in irreducible Brillouin zone) × (number of atoms in cell) > 500. Perform full relaxation of cell volume and atomic positions for each system. Record the final total energy per cell, number of atoms, and relaxed lattice parameters for each system.
- Evidence: `/app/outputs/none`

### Step 2: Formation enthalpies and lattice parameters
- Role: scored (load-bearing)
- Action: From the relaxed DFT total energies, compute formation enthalpy per atom for each compound using the standard composition-weighted subtraction: E(compound) − x_Ge * E(Ge_A4) − (1−x_Ge) * E(Ti_A3), with energies per atom. Convert results to kJ per mol of atoms. Assemble a JSON file containing for each system: compound name, prototype designation, total energy per cell in eV, number of atoms, relaxed lattice parameters (a, b, c in Å), and the computed formation enthalpy in kJ/mol-atom. Include pure Ge and Ti as references.
- Output file: `/app/outputs/formation_enthalpies.json`
- Format: json
- Contract: Array of objects with keys: compound (string), prototype (string), total_energy_per_cell_eV (number), natoms (integer), lattice_parameters (object with a, b, c in Å), formation_enthalpy_kJ_mol_atom (number). Must contain entries for 'Ge A4', 'Ti A3', 'Ge3Ti5', 'Ge4Ti5', 'Ge5Ti6', 'Ge2Ti'.
- Scoring: scored by hidden verifier

### Step 3: Convex hull analysis
- Role: scored
- Action: Using the formation enthalpies from step2, construct the zero‑K convex hull of formation enthalpy vs Ge atomic fraction. Determine which compounds lie on the hull. Output a JSON object with the list of stable compound names on the hull and a boolean indicating whether Ge4Ti5 is on the hull.
- Output file: `/app/outputs/convex_hull_analysis.json`
- Format: json
- Contract: Object with keys: on_hull (array of compound name strings that lie on the convex hull), ge4ti5_on_hull (boolean, true if Ge4Ti5 lies on the hull).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_enthalpies.json`
- `/app/outputs/convex_hull_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_enthalpies.json
- path: `/app/outputs/formation_enthalpies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed formation enthalpies and relaxed lattice parameters for Ge–Ti compounds and elemental references.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `prototype`, `total_energy_per_cell_eV`, `natoms`, `lattice_parameters`, `formation_enthalpy_kJ_mol_atom`
    - `properties`:
      - `compound`:
        - `type`: string
      - `prototype`:
        - `type`: string
      - `total_energy_per_cell_eV`:
        - `type`: number
      - `natoms`:
        - `type`: integer
      - `lattice_parameters`:
        - `type`: object
        - `required`: `a`, `b`, `c`
        - `properties`:
          - `a`:
            - `type`: number
            - `unit`: Å
          - `b`:
            - `type`: number
            - `unit`: Å
          - `c`:
            - `type`: number
            - `unit`: Å
      - `formation_enthalpy_kJ_mol_atom`:
        - `type`: number

### convex_hull_analysis.json
- path: `/app/outputs/convex_hull_analysis.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Zero‑K convex hull analysis: hull member compounds and stability of Ge4Ti5.
- schema:
  - `type`: object
  - `required`: `on_hull`, `ge4ti5_on_hull`
  - `properties`:
    - `on_hull`:
      - `type`: array
      - `items`:
        - `type`: string
    - `ge4ti5_on_hull`:
      - `type`: boolean

Notes: All formation enthalpy data must be derived from the submitted total energies; checker will recompute formation enthalpy and convex hull independently.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_enthalpies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "prototype",
            "total_energy_per_cell_eV",
            "natoms",
            "lattice_parameters",
            "formation_enthalpy_kJ_mol_atom"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "prototype": {
              "type": "string"
            },
            "total_energy_per_cell_eV": {
              "type": "number"
            },
            "natoms": {
              "type": "integer"
            },
            "lattice_parameters": {
              "type": "object",
              "required": [
                "a",
                "b",
                "c"
              ],
              "properties": {
                "a": {
                  "type": "number",
                  "unit": "Å"
                },
                "b": {
                  "type": "number",
                  "unit": "Å"
                },
                "c": {
                  "type": "number",
                  "unit": "Å"
                }
              }
            },
            "formation_enthalpy_kJ_mol_atom": {
              "type": "number"
            }
          }
        }
      },
      "description": "Computed formation enthalpies and relaxed lattice parameters for Ge–Ti compounds and elemental references."
    },
    {
      "file": "convex_hull_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "on_hull",
          "ge4ti5_on_hull"
        ],
        "properties": {
          "on_hull": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "ge4ti5_on_hull": {
            "type": "boolean"
          }
        }
      },
      "description": "Zero‑K convex hull analysis: hull member compounds and stability of Ge4Ti5."
    }
  ],
  "notes": "All formation enthalpy data must be derived from the submitted total energies; checker will recompute formation enthalpy and convex hull independently."
}
```

## How you are scored
A hidden verifier program independently scores each required artifact. For `formation_enthalpies.json`, the verifier recomputes the formation enthalpy per atom from your supplied total energies and atom counts and checks internal consistency; it also compares your formation enthalpy values and relaxed lattice parameters against a hidden set of reference results. For `convex_hull_analysis.json`, the verifier reconstructs the convex hull from your own formation enthalpy data and verifies that the `on_hull` list and the `ge4ti5_on_hull` boolean are correct. The final reward is a weighted combination of the checks on both files. The verifier does not require that your results match a specific single number; it evaluates whether they are physically reasonable and consistent with the protocol. The reward is monotonic in quality: more accurate results earn higher scores.
