# GGA+U Reproduction of Fluorinated Boron Nitride Magnetic Properties

## Problem background
Light-element magnetic systems, which rely solely on sp electrons, are attractive for next-generation technologies but pose a fundamental challenge for density functional theory (DFT). Standard semi‑local approximations such as LDA and GGA suffer from severe delocalization error, often failing to capture the correct magnetic ground state, spin moment, and relative stability of magnetic configurations. Hybrid functionals (e.g., HSE) substantially improve the description but are computationally expensive, especially for extended systems. This task investigates whether a computationally efficient GGA+U approach, where a Hubbard U correction is applied to N‑2p orbitals in fluorinated boron nitride (F‑BN) sheets and nanotubes, can reliably reproduce the electronic and magnetic properties that are otherwise only accessible with hybrid functionals. The goal is to determine the energy difference between ferromagnetic and antiferromagnetic configurations and the local magnetic moments on the nitrogen sites, providing a benchmark for the accuracy of the GGA+U method when compared to the higher‑level hybrid functional reference.

## Approach
The method consists of two stages. First, the atomic structures of the F‑BN sheet and nanotube are built using the experimental h‑BN lattice constant and relaxed with GGA‑PBE in the ferromagnetic state. The relaxed geometries then serve as input for GGA+U calculations, where an effective Hubbard U correction (Ueff = 7 eV) is applied exclusively to the N‑2p orbitals. For each system, single‑point total energies are computed in both the ferromagnetic and antiferromagnetic spin configurations. From these energies the magnetic stabilisation energy ΔE = E_AFM − E_FM is obtained. Local magnetic moments on the non‑equivalent nitrogen atoms are extracted from the spin‑polarised charge density, using Mulliken or projected‑density analysis. The entire workflow is implemented with an open‑source plane‑wave DFT code (Quantum ESPRESSO) and standard PAW pseudopotentials, making the procedure fully reproducible.

## Reproduction target
The task is to compute the energy difference ΔE (in meV) between the antiferromagnetic and ferromagnetic states, and the local magnetic moments (in μB) on the non‑equivalent nitrogen atoms, for two specific systems: (i) the (2√3×√3) F‑BN sheet (monolayer) and (ii) the (8,0) BN nanotube with a single fluorine atom adsorbed per primitive cell. The calculation must be performed with GGA+U, using the prescribed Ueff = 7 eV on N‑2p orbitals, and the structures must be optimised beforehand with GGA‑PBE. The results are to be written to a JSON file at `/app/outputs/results.json` following the exact schema described in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP precision PAW pseudopotentials (PBE) for B, N, F: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build initial structures
- Role: process
- Action: Construct the primitive unit cells of the (2√3×√3) F‑BN sheet and the (8,0) BN nanotube with one F atom adsorbed per primitive cell. Use the experimental h‑BN lattice constant a=2.49 Å, place B and N at ideal h‑BN positions, and add F atoms on top of B sites at a reasonable initial distance (~1.4 Å). Output the structures in Quantum ESPRESSO input format.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: GGA-PBE geometry relaxation
- Role: process
- Action: Relax atomic positions (cell parameters fixed) of both the sheet and the nanotube using Quantum ESPRESSO with the PBE functional and the selected PAW pseudopotentials. Use a plane‑wave cutoff of 400 eV, a k‑point grid of 8×8×1 for the sheet and 1×1×8 for the nanotube, and a force convergence threshold of 0.01 eV/Å. Perform the relaxation in the ferromagnetic spin configuration.
- Evidence: `/app/outputs/relaxation_summary.txt`

### Step 3: GGA+U magnetic property calculations
- Role: scored (load-bearing)
- Action: Using the relaxed structures, run single‑point Quantum ESPRESSO calculations with GGA+U (Ueff=7 eV on N‑2p) for both ferromagnetic and antiferromagnetic spin configurations. Extract total energies, compute ΔE = E_AFM − E_FM (meV), and obtain local magnetic moments (Mulliken or projected) on non‑equivalent N atoms: for the sheet, the N closest to F and two other N atoms (N1, N2, N3); for the nanotube, N1 (closest to F), N2 and N3 (second nearest). Output a JSON file with the exact schema specified in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"sheet": {"delta_E_meV": float, "magnetic_moments": {"N1": float, "N2": float, "N3": float}}, "nanotube": {"delta_E_meV": float, "magnetic_moments": {"N1": float, "N2": float, "N3": float}}}
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
- description: GGA+U computed energy difference between antiferromagnetic and ferromagnetic states (ΔE) and local magnetic moments on non‑equivalent N atoms for the (2√3×√3) F‑BN sheet and the (8,0) F‑BN nanotube with a single F per primitive cell.
- schema:
  - `type`: object
  - `required`: `sheet`, `nanotube`
  - `properties`:
    - `sheet`:
      - `type`: object
      - `required`: `delta_E_meV`, `magnetic_moments`
      - `properties`:
        - `delta_E_meV`:
          - `type`: number
          - `unit`: meV
        - `magnetic_moments`:
          - `type`: object
          - `required`: `N1`, `N2`, `N3`
          - `properties`:
            - `N1`:
              - `type`: number
              - `unit`: μB
            - `N2`:
              - `type`: number
              - `unit`: μB
            - `N3`:
              - `type`: number
              - `unit`: μB
    - `nanotube`:
      - `type`: object
      - `required`: `delta_E_meV`, `magnetic_moments`
      - `properties`:
        - `delta_E_meV`:
          - `type`: number
          - `unit`: meV
        - `magnetic_moments`:
          - `type`: object
          - `required`: `N1`, `N2`, `N3`
          - `properties`:
            - `N1`:
              - `type`: number
              - `unit`: μB
            - `N2`:
              - `type`: number
              - `unit`: μB
            - `N3`:
              - `type`: number
              - `unit`: μB

Notes: The hidden checker compares the reported values to the paper's HSE reference values using tolerances (absolute/relative for ΔE, absolute for magnetic moments). The solving agent is not required to run HSE calculations; it must produce the GGA+U results at Ueff=7 eV.

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
          "sheet",
          "nanotube"
        ],
        "properties": {
          "sheet": {
            "type": "object",
            "required": [
              "delta_E_meV",
              "magnetic_moments"
            ],
            "properties": {
              "delta_E_meV": {
                "type": "number",
                "unit": "meV"
              },
              "magnetic_moments": {
                "type": "object",
                "required": [
                  "N1",
                  "N2",
                  "N3"
                ],
                "properties": {
                  "N1": {
                    "type": "number",
                    "unit": "μB"
                  },
                  "N2": {
                    "type": "number",
                    "unit": "μB"
                  },
                  "N3": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              }
            }
          },
          "nanotube": {
            "type": "object",
            "required": [
              "delta_E_meV",
              "magnetic_moments"
            ],
            "properties": {
              "delta_E_meV": {
                "type": "number",
                "unit": "meV"
              },
              "magnetic_moments": {
                "type": "object",
                "required": [
                  "N1",
                  "N2",
                  "N3"
                ],
                "properties": {
                  "N1": {
                    "type": "number",
                    "unit": "μB"
                  },
                  "N2": {
                    "type": "number",
                    "unit": "μB"
                  },
                  "N3": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              }
            }
          }
        }
      },
      "description": "GGA+U computed energy difference between antiferromagnetic and ferromagnetic states (ΔE) and local magnetic moments on non‑equivalent N atoms for the (2√3×√3) F‑BN sheet and the (8,0) F‑BN nanotube with a single F per primitive cell."
    }
  ],
  "notes": "The hidden checker compares the reported values to the paper's HSE reference values using tolerances (absolute/relative for ΔE, absolute for magnetic moments). The solving agent is not required to run HSE calculations; it must produce the GGA+U results at Ueff=7 eV."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks the reported ΔE and magnetic moments against a set of accurate reference values obtained from hybrid functional calculations. The verifier also confirms that the intermediate relaxation output files are present and well‑formed, although the scoring weight lies primarily on the final `results.json`. Your numbers must fall within predetermined tolerances to receive credit; results that are closer to the reference receive a higher score, but the precise tolerances are not disclosed. No credit is given for simply transcribing published numbers – you must genuinely execute the computational workflow described in the steps above.
