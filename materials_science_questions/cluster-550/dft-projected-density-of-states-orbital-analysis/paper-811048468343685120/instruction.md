# CdTe(110)-Metal Interface Adsorption Classification and Electronic Properties from DFT

## Problem background
CdTe is a key p-type absorber in thin-film solar cells. The physical and electronic properties of the interface between CdTe and the metal back electrode directly govern carrier extraction efficiency through Schottky barriers and possible tunneling barriers. Understanding the adsorption strength, equilibrium geometry, Schottky contact type and barrier heights for commonly used electrode metals (Al, Ag, Au, Cu, Ni) is essential for designing high-performance contacts.

## Approach
First-principles density functional theory (DFT) is used to model CdTe(110) slabs adsorbed on six-layer metal slabs and the corresponding isolated systems. The PBE+optB88‑vdW exchange-correlation functional captures van-der-Waals interactions. Geometry optimizations provide total energies and atomic coordinates, from which interfacial binding energies and average vertical distances are computed. Adsorption strength is classified based on these quantities. Static electronic structure calculations give band structures, electrostatic potentials, and work functions. The Schottky barrier type and height are determined from band alignment using a GW-corrected CdTe band gap (applied by scaling the DFT band edges). Additionally, average effective potential profiles across the interface are analysed to extract tunneling barrier heights, widths, and probabilities using a square-barrier model.

## Reproduction target
For each metal (Al, Ag, Au, Cu, Ni) compute:
(i) interfacial binding energy per Cd atom (E_b, eV) and average vertical distance between CdTe and the metal (d_CdTe-M, Å);
(ii) adsorption classification (weak chemisorption, medium chemisorption, or strong chemisorption) based on the binding strength and distance;
(iii) Schottky contact type (n-type or p-type) and the corresponding Schottky barrier height (SBH, eV) after GW correction;
(iv) tunneling barrier height (ΔV, eV), full-width at half-maximum (w_B, Å), and tunneling probability (T_B, %).
Write the four scored artifacts as described in the workflow steps.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE efficiency set) or equivalent: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Build supercell models for CdTe(110) on each metal (Al, Ag, Au, Cu, Ni) using lattice matching, as well as isolated CdTe(110) slab and isolated metal slabs. Use six-layer metal and six-layer CdTe, appropriate lattice orientation, and a vacuum layer.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: For each system (isolated CdTe slab, isolated metal slabs, and the five CdTe-metal interfaces), perform DFT structural optimization using PBE+optB88-vdW functional and PAW pseudopotentials. Relax until force and energy convergence criteria are met. Save final total energies and relaxed atomic positions.
- Evidence: none

### Step 3: Binding energy and equilibrium distance
- Role: scored (load-bearing)
- Action: From the optimized total energies and coordinates, compute the interfacial binding energy per Cd atom using the formula E_b = (E_CdTe + E_metal - E_CdTe_metal)/N_Cd, and the average vertical distance d_CdTe-M between the bottom-layer Cd/Te atoms and the topmost metal-layer atoms. Write results to binding_energies_distances.json.
- Output file: `/app/outputs/binding_energies_distances.json`
- Format: json
- Contract: Array of objects, each with keys: metal (string), E_b (float, eV), d_CdTe_M (float, Å).
- Scoring: scored by hidden verifier

### Step 4: Adsorption classification
- Role: scored
- Action: Based on the computed binding energies and equilibrium distances from step3, classify each interface as 'weak chemisorption', 'medium chemisorption', or 'strong chemisorption' following the trend that higher E_b and shorter distance indicate stronger adsorption. Write to adsorption_classification.json.
- Output file: `/app/outputs/adsorption_classification.json`
- Format: json
- Contract: Array of objects, each with keys: metal (string), category (one of 'weak chemisorption', 'medium chemisorption', 'strong chemisorption').
- Scoring: scored by hidden verifier

### Step 5: Static DFT and bulk band gap
- Role: process
- Action: Using the optimized geometries from step2, run static DFT calculations with denser k-points for each interfacial system. Additionally, compute the band structure of bulk CdTe to obtain its DFT band gap. Extract electrostatic potential profiles and band eigenvalues.
- Evidence: none

### Step 6: Work function extraction
- Role: process
- Action: From the electrostatic potentials of the clean metal surface and the CdTe-adsorbed metal surface (extracted from the static DFT runs), compute the work functions W_M and W. Save these values for later use.
- Evidence: none

### Step 7: Schottky barrier calculation
- Role: scored
- Action: Using the DFT band edges (CBM, VBM) and Fermi level of bulk CdTe, together with the work functions and band alignment from the interfacial systems, determine the Schottky contact type (n-type or p-type) for each metal and the corresponding Schottky barrier height (SBH). Apply a GW correction by scaling the DFT band gap to a corrected band gap, keeping the Fermi level unchanged. Write results to schottky_barriers.json.
- Output file: `/app/outputs/schottky_barriers.json`
- Format: json
- Contract: Array of objects, each with keys: metal (string), SBH (float, eV), contact_type (string, 'n-type' or 'p-type').
- Scoring: scored by hidden verifier

### Step 8: Tunneling barrier analysis
- Role: scored
- Action: From the average effective potentials along the direction normal to the interface (obtained from static DFT), extract the tunneling barrier height ΔV and full-width at half-maximum w_B. Compute the tunneling probability T_B using the square barrier formula. Write results to tunneling_barriers.json.
- Output file: `/app/outputs/tunneling_barriers.json`
- Format: json
- Contract: Array of objects, each with keys: metal (string), Delta_V (float, eV), w_B (float, Å), T_B (float, %). For interfaces with no tunneling barrier, Delta_V and w_B should be 0 and T_B 100.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies_distances.json`
- `/app/outputs/adsorption_classification.json`
- `/app/outputs/schottky_barriers.json`
- `/app/outputs/tunneling_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies_distances.json
- path: `/app/outputs/binding_energies_distances.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Interfacial binding energies per Cd atom and equilibrium vertical distances for Al, Ag, Au, Cu, Ni.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `metal`, `E_b`, `d_CdTe_M`
    - `properties`:
      - `metal`:
        - `type`: string
      - `E_b`:
        - `type`: number
        - `unit`: eV
      - `d_CdTe_M`:
        - `type`: number
        - `unit`: Å

### adsorption_classification.json
- path: `/app/outputs/adsorption_classification.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Adsorption strength classification for each metal interface.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `metal`, `category`
    - `properties`:
      - `metal`:
        - `type`: string
      - `category`:
        - `type`: string
        - `enum`: `weak chemisorption`, `medium chemisorption`, `strong chemisorption`

### schottky_barriers.json
- path: `/app/outputs/schottky_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Schottky barrier heights (with GW correction) and contact types for each metal.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `metal`, `SBH`, `contact_type`
    - `properties`:
      - `metal`:
        - `type`: string
      - `SBH`:
        - `type`: number
        - `unit`: eV
      - `contact_type`:
        - `type`: string
        - `enum`: `n-type`, `p-type`

### tunneling_barriers.json
- path: `/app/outputs/tunneling_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Tunneling barrier height, width, and probability for each metal interface.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `metal`, `Delta_V`, `w_B`, `T_B`
    - `properties`:
      - `metal`:
        - `type`: string
      - `Delta_V`:
        - `type`: number
        - `unit`: eV
      - `w_B`:
        - `type`: number
        - `unit`: Å
      - `T_B`:
        - `type`: number
        - `unit`: %

Notes: All values should be reported for the five metals: Al, Ag, Au, Cu, Ni. GW correction uses a scaling factor applied to DFT band edges; the exact GW gap is not required to be computed from scratch. The check can compare values with appropriate tolerances accounting for DFT code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "metal",
            "E_b",
            "d_CdTe_M"
          ],
          "properties": {
            "metal": {
              "type": "string"
            },
            "E_b": {
              "type": "number",
              "unit": "eV"
            },
            "d_CdTe_M": {
              "type": "number",
              "unit": "Å"
            }
          }
        }
      },
      "description": "Interfacial binding energies per Cd atom and equilibrium vertical distances for Al, Ag, Au, Cu, Ni."
    },
    {
      "file": "adsorption_classification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "metal",
            "category"
          ],
          "properties": {
            "metal": {
              "type": "string"
            },
            "category": {
              "type": "string",
              "enum": [
                "weak chemisorption",
                "medium chemisorption",
                "strong chemisorption"
              ]
            }
          }
        }
      },
      "description": "Adsorption strength classification for each metal interface."
    },
    {
      "file": "schottky_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "metal",
            "SBH",
            "contact_type"
          ],
          "properties": {
            "metal": {
              "type": "string"
            },
            "SBH": {
              "type": "number",
              "unit": "eV"
            },
            "contact_type": {
              "type": "string",
              "enum": [
                "n-type",
                "p-type"
              ]
            }
          }
        }
      },
      "description": "Schottky barrier heights (with GW correction) and contact types for each metal."
    },
    {
      "file": "tunneling_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "metal",
            "Delta_V",
            "w_B",
            "T_B"
          ],
          "properties": {
            "metal": {
              "type": "string"
            },
            "Delta_V": {
              "type": "number",
              "unit": "eV"
            },
            "w_B": {
              "type": "number",
              "unit": "Å"
            },
            "T_B": {
              "type": "number",
              "unit": "%"
            }
          }
        }
      },
      "description": "Tunneling barrier height, width, and probability for each metal interface."
    }
  ],
  "notes": "All values should be reported for the five metals: Al, Ag, Au, Cu, Ni. GW correction uses a scaling factor applied to DFT band edges; the exact GW gap is not required to be computed from scratch. The check can compare values with appropriate tolerances accounting for DFT code differences."
}
```

## How you are scored
A hidden verifier reads each of the four scored output files and compares the values, classifications, and contact types against expected results. The verifier checks both the quantitative values (binding energies, distances, barrier heights, etc.) and the correct structural assignments (adsorption classes, contact types). The final score is a weighted combination of the per‑stage scores. Simply reporting known numbers from outside sources is not sufficient; the results must be produced by executing the described workflow.
