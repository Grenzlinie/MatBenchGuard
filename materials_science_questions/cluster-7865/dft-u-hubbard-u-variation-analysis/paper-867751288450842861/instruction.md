# DFT Calculation of Ferromagnetic Stabilization in Doped Sr2MnGe2S6O

## Problem background
The melilite-type oxysulfide Sr2MnGe2S6O is a weakly antiferromagnetic insulator. Introducing charge carriers by substituting strontium with potassium (p‑type) or lanthanum (n‑type) may alter the magnetic interactions and potentially stabilize a ferromagnetic ground state. The energy differences between antiferromagnetic and ferromagnetic ordering at various doping levels, and the resulting Curie temperatures, are critical quantities that determine whether this compound can serve as a room‑temperature ferromagnetic semiconductor. This task reproduces the first‑principles density functional theory (DFT) calculations used to quantify these energy differences and the estimated Curie temperatures.

## Approach
The task uses spin‑polarized DFT within the generalized gradient approximation (GGA‑PBE) and the projector augmented wave (PAW) method. A 48‑atom supercell of Sr2MnGe2S6O is constructed from the known crystal structure. Substitutional doping is modeled by replacing Sr atoms with K or La at concentrations of 12.5% (one substitution) and 25% (two substitutions). For each doped structure, total energies are computed for two magnetic configurations: a ferromagnetic (FM) order and an intra‑layer checkerboard antiferromagnetic (AFM) order. The energy difference per Mn atom ΔE = E_AFM − E_FM is extracted for each doping condition. From the ΔE at 25% doping, the nearest‑neighbour exchange coupling J1 is derived as J1 = ΔE/4, and the Curie temperature Tc is estimated using the two‑dimensional square‑lattice Ising model: k_B Tc = 2J1 / ln(1+√2). The calculations are carried out with Quantum ESPRESSO, an open‑source plane‑wave DFT code, using standard PAW pseudopotentials.

## Reproduction target
Your objective is to compute and output the following quantities:
- The energy difference per Mn (ΔE in meV/Mn) between the AFM and FM orders for K doping at 12.5% and 25%, and for La doping at 12.5% and 25%.
- The Curie temperature Tc (in K) for the K‑25% and La‑25% doped compounds, estimated from the corresponding ΔE values using the Ising model formula.
Save these results in a JSON file at `/app/outputs/results.json`. The file must contain an object with two keys: "delta_E" (an object with fields "K_12.5", "K_25", "La_12.5", "La_25", each a number in meV/Mn) and "Tc" (an object with fields "K_25" and "La_25", each a number in K).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials (PBE) from SSSP library: https://www.materialscloud.org/discover/sssp/table/pbe
- Crystal structure of Sr2MnGe2S6O: 10.1021/acs.inorgchem.6b02682

## Workflow steps

### Step 1: Generate supercell and substitution structures
- Role: process
- Action: Construct the 48-atom supercell of Sr2MnGe2S6O (space group P-42_1m, a=b=9.5206 Å, c=12.4004 Å) by doubling the primitive cell along c. Then create substitutional models for K doping (replace one Sr by K) and La doping (replace one Sr by La) at concentrations 12.5% (one substitution per supercell) and 25% (two substitutions in different Sr layers).
- Evidence: `/app/outputs/structures.log`

### Step 2: DFT total energy calculations
- Role: process
- Action: For each of the four doped structures and for both ferromagnetic (FM) and intra-layer checkerboard antiferromagnetic (AFM) magnetic orders, perform spin-polarized GGA-PBE DFT calculations using Quantum ESPRESSO with PAW pseudopotentials, a plane-wave cutoff of 520 eV, and a 7×7×6 Monkhorst-Pack k-point mesh. Relax internal atomic positions. Collect total energies.
- Evidence: `/app/outputs/dft_energies.json`

### Step 3: Energy difference and Curie temperature
- Role: scored (load-bearing)
- Action: From the total energies collected in step 2, compute ΔE = E_AFM - E_FM per Mn atom for each doping case. Then, for the 25% doping cases, derive the nearest-neighbor exchange parameter J1 = ΔE/4 and estimate the Curie temperature using the 2D square-lattice Ising model formula k_B T_c = 2J1 / ln(1+√2). Write the results as a JSON file with delta_E and Tc.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"delta_E": {"K_12.5": float (meV/Mn), "K_25": float, "La_12.5": float, "La_25": float}, "Tc": {"K_25": float (K), "La_25": float (K)}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduced energy differences and Curie temperatures. The hidden checker compares delta_E values to the paper's reference values with appropriate tolerances, recomputes Tc from delta_E using J1=ΔE/4 and the 2D Ising relation, and verifies that both Tc exceed 300 K.
- schema:
  - `type`: object
  - `required`: `delta_E`, `Tc`
  - `properties`:
    - `delta_E`:
      - `type`: object
      - `required`: `K_12.5`, `K_25`, `La_12.5`, `La_25`
      - `properties`:
        - `K_12.5`:
          - `type`: number
          - `description`: Energy difference per Mn in meV for K doping at 12.5%
        - `K_25`:
          - `type`: number
          - `description`: ΔE for K doping at 25%
        - `La_12.5`:
          - `type`: number
          - `description`: ΔE for La doping at 12.5%
        - `La_25`:
          - `type`: number
          - `description`: ΔE for La doping at 25%
    - `Tc`:
      - `type`: object
      - `required`: `K_25`, `La_25`
      - `properties`:
        - `K_25`:
          - `type`: number
          - `description`: Curie temperature in K for K doping at 25%
        - `La_25`:
          - `type`: number
          - `description`: Curie temperature in K for La doping at 25%

Notes: The checker combines a reference-match on ΔE with a derived threshold check on Tc. Ensure all ΔE values are in meV/Mn and Tc values in K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_E",
          "Tc"
        ],
        "properties": {
          "delta_E": {
            "type": "object",
            "required": [
              "K_12.5",
              "K_25",
              "La_12.5",
              "La_25"
            ],
            "properties": {
              "K_12.5": {
                "type": "number",
                "description": "Energy difference per Mn in meV for K doping at 12.5%"
              },
              "K_25": {
                "type": "number",
                "description": "ΔE for K doping at 25%"
              },
              "La_12.5": {
                "type": "number",
                "description": "ΔE for La doping at 12.5%"
              },
              "La_25": {
                "type": "number",
                "description": "ΔE for La doping at 25%"
              }
            }
          },
          "Tc": {
            "type": "object",
            "required": [
              "K_25",
              "La_25"
            ],
            "properties": {
              "K_25": {
                "type": "number",
                "description": "Curie temperature in K for K doping at 25%"
              },
              "La_25": {
                "type": "number",
                "description": "Curie temperature in K for La doping at 25%"
              }
            }
          }
        }
      },
      "description": "Reproduced energy differences and Curie temperatures. The hidden checker compares delta_E values to the paper's reference values with appropriate tolerances, recomputes Tc from delta_E using J1=ΔE/4 and the 2D Ising relation, and verifies that both Tc exceed 300 K."
    }
  ],
  "notes": "The checker combines a reference-match on ΔE with a derived threshold check on Tc. Ensure all ΔE values are in meV/Mn and Tc values in K."
}
```

## How you are scored
A hidden verifier will load your `/app/outputs/results.json`. It compares each of the four ΔE values to hidden reference values and awards credit for those within a specified tolerance. The two Tc values are evaluated against a hidden minimum threshold (they must exceed it) and against a hidden percentage margin of the reference values. The final reward is a weighted combination: 50% of the score depends on the accuracy of all four ΔE values, and the remaining 50% on the validity of the two Tc values. To pass, you must genuinely execute the DFT workflow; merely reporting numbers without performing the calculations will not succeed.
