# DFT Calculation of the Split Antisite Complex in GaAs

## Problem background
Low-temperature-grown GaAs contains high concentrations of point defects such as As interstitials and As antisites. Understanding the lowest-energy complexes formed by these defects is crucial for explaining the electrical and optical properties of the material. This task focuses on computing the properties of the split antisite complex—a configuration where two As atoms share a Ga site—using first-principles density functional theory (DFT). The goal is to determine the atomic geometry, the electronic donor level relative to the conduction-band edge, and the binding energies of the complex relative to the isolated constituent defects.

## Approach
Use plane-wave DFT within the local-density approximation (LDA) and norm-conserving pseudopotentials. Build a 65-atom cubic supercell of GaAs and first compute band-edge energies for pristine GaAs. Then model isolated defects: a neutral (110) As split interstitial, a neutral As antisite (As on a Ga site), and their singly charged counterparts ($q=-1$ for the interstitial, $q=+1$ for the antisite). Search for the lowest-energy complex by relaxing supercells containing one As interstitial and one As antisite starting from several initial configurations (split interstitial adjacent to antisite, tetrahedral, hexagonal, bridge-bond, and displaced variants). Identify the split antisite as the relaxed configuration with two As atoms occupying a Ga site. From the relaxed complex, extract atomic coordinates of the two central As atoms and their four nearest neighbors, expressed in units of the GaAs lattice constant with origin at the midpoint between the central atoms. Compute the donor-like electronic level by aligning the highest occupied defect-related Kohn-Sham eigenvalue against the conduction band minimum from the pristine calculation. Compute three binding energies using total energy differences: neutral binding (complex minus neutral isolated constituents), charged binding (complex minus charged isolated constituents), and scissors-corrected binding (charged binding recalculated after applying a 0.2 eV upward shift to conduction-derived states of the isolated As antisite).

## Reproduction target
Produce three scored artifacts:

1. `split_antisite_coordinates.json`: an array of six objects, each containing the atom symbol (`atom`) and coordinates `x`, `y`, `z` in units of the GaAs lattice constant, origin at the midpoint between the two central As atoms. The array must list exactly the two central As atoms and their four nearest neighbors.

2. `donor_level.json`: an object with a single key `donor_level_below_cb` giving the donor level in eV (positive below the conduction band edge).

3. `binding_energies.json`: an object with keys `neutral`, `charged`, and `scissors_corrected`, each a binding energy in eV computed as described in the approach.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Pseudopotentials for Ga and As: https://www.pseudo-dojo.org

## Workflow steps

### Step 1: Pristine GaAs supercell calculation
- Role: process
- Action: Construct a 65-atom cubic GaAs supercell and perform DFT calculation to obtain valence band maximum (VBM), conduction band minimum (CBM), and bulk total energy per formula unit for band-edge alignment.
- Evidence: `/app/outputs/pristine_band_edges.json`

### Step 2: Isolated neutral As (110) split interstitial
- Role: process
- Action: Insert an As interstitial in the (110) split configuration into the supercell, relax the structure, and compute total energy and Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/split_interstitial_total_energy.json`

### Step 3: Isolated neutral As antisite
- Role: process
- Action: Replace a Ga atom with an As atom to create an As antisite, relax the structure, and compute total energy and Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/antisite_total_energy.json`

### Step 4: Charged As split interstitial (acceptor)
- Role: process
- Action: Compute total energy of the singly negatively charged (110) As split interstitial (q=-1) using the same supercell and DFT with appropriate charge handling.
- Evidence: `/app/outputs/charged_split_interstitial_energy.json`

### Step 5: Charged As antisite (donor)
- Role: process
- Action: Compute total energy of the singly positively charged As antisite (q=+1) using the same DFT approach.
- Evidence: `/app/outputs/charged_antisite_energy.json`

### Step 6: Search for split antisite complex
- Role: process
- Action: Starting from a supercell containing one As antisite and one As interstitial placed in several initial configurations (split interstitial adjacent to antisite, tetrahedral, hexagonal, bridge-bond, and slightly displaced variants), perform DFT relaxation to find the lowest-energy complex. Identify the split antisite (two As atoms sharing a Ga site) and record its total energy and relaxed atomic positions.
- Evidence: `/app/outputs/complex_structure.json`

### Step 7: Atomic coordinates of the split antisite
- Role: scored
- Action: From the relaxed complex structure, extract the atomic positions of the two central As atoms and their four nearest neighbors. Express coordinates in units of the GaAs lattice constant, with origin at the midpoint between the two central As atoms.
- Output file: `/app/outputs/split_antisite_coordinates.json`
- Format: json
- Contract: Array of objects with fields: atom (string), x (float), y (float), z (float). The array must contain exactly 6 atoms (two As and four nearest neighbors).
- Scoring: scored by hidden verifier

### Step 8: Donor level of the split antisite
- Role: scored
- Action: From the Kohn-Sham eigenvalues of the relaxed split antisite complex, identify the highest occupied defect-related state and determine its energy relative to the conduction band minimum (CBM) obtained from the pristine supercell. Output the donor level below the CBM in eV.
- Output file: `/app/outputs/donor_level.json`
- Format: json
- Contract: {"donor_level_below_cb": float}
- Scoring: scored by hidden verifier

### Step 9: Binding energies of the split antisite
- Role: scored (load-bearing)
- Action: Compute three binding energies using the collected total energies and electronic levels: (a) neutral: E(complex) - [E(neutral split interstitial) + E(neutral As antisite)]; (b) charged: E(complex) - [E(charged split interstitial, -1) + E(charged As antisite, +1)]; (c) scissors-corrected: apply a 0.2 eV upward shift to conduction-derived states of the isolated As antisite donor level and recalculate the charged binding energy using the formation-energy formalism with the corrected level.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"neutral": float, "charged": float, "scissors_corrected": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/split_antisite_coordinates.json`
- `/app/outputs/donor_level.json`
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### split_antisite_coordinates.json
- path: `/app/outputs/split_antisite_coordinates.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Atomic coordinates of the two central As atoms and their four nearest neighbors in the split antisite complex, expressed in units of the GaAs lattice constant with origin at the midpoint between the central atoms.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `atom`, `x`, `y`, `z`
    - `properties`:
      - `atom`:
        - `type`: string
      - `x`:
        - `type`: number
        - `unit`: lattice constant
      - `y`:
        - `type`: number
        - `unit`: lattice constant
      - `z`:
        - `type`: number
        - `unit`: lattice constant

### donor_level.json
- path: `/app/outputs/donor_level.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Donor-like electronic level of the split antisite complex relative to the conduction band edge, in eV.
- schema:
  - `type`: object
  - `required`: `donor_level_below_cb`
  - `properties`:
    - `donor_level_below_cb`:
      - `type`: number
      - `unit`: eV

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Binding energies of the split antisite complex: neutral, charged, and scissors-corrected (shift of conduction-derived states by 0.2 eV).
- schema:
  - `type`: object
  - `required`: `neutral`, `charged`, `scissors_corrected`
  - `properties`:
    - `neutral`:
      - `type`: number
      - `unit`: eV
    - `charged`:
      - `type`: number
      - `unit`: eV
    - `scissors_corrected`:
      - `type`: number
      - `unit`: eV

Notes: Coordinates are to be compared to the reference geometry with a tolerance; donor level and binding energies are compared to the paper-reported values with appropriate tolerances. The scissors-corrected binding energy must use the protocol of shifting conduction-derived states by 0.2 eV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "split_antisite_coordinates.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "atom",
            "x",
            "y",
            "z"
          ],
          "properties": {
            "atom": {
              "type": "string"
            },
            "x": {
              "type": "number",
              "unit": "lattice constant"
            },
            "y": {
              "type": "number",
              "unit": "lattice constant"
            },
            "z": {
              "type": "number",
              "unit": "lattice constant"
            }
          }
        }
      },
      "description": "Atomic coordinates of the two central As atoms and their four nearest neighbors in the split antisite complex, expressed in units of the GaAs lattice constant with origin at the midpoint between the central atoms."
    },
    {
      "file": "donor_level.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "donor_level_below_cb"
        ],
        "properties": {
          "donor_level_below_cb": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Donor-like electronic level of the split antisite complex relative to the conduction band edge, in eV."
    },
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "neutral",
          "charged",
          "scissors_corrected"
        ],
        "properties": {
          "neutral": {
            "type": "number",
            "unit": "eV"
          },
          "charged": {
            "type": "number",
            "unit": "eV"
          },
          "scissors_corrected": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Binding energies of the split antisite complex: neutral, charged, and scissors-corrected (shift of conduction-derived states by 0.2 eV)."
    }
  ],
  "notes": "Coordinates are to be compared to the reference geometry with a tolerance; donor level and binding energies are compared to the paper-reported values with appropriate tolerances. The scissors-corrected binding energy must use the protocol of shifting conduction-derived states by 0.2 eV."
}
```

## How you are scored
Each of the three scored artifacts is checked independently by an automated verifier. The verifier compares the reported coordinates, donor level, and binding energies against reference values with appropriate tolerances, and assigns a score per artifact. The final reward is the weighted combination of these scores. To receive full credit, you must execute all process steps honestly and produce the artifacts from genuine DFT calculations—simply guessing or fabricating numbers will not yield correct results.
