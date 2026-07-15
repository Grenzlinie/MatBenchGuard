# DFT Geometry Optimization and Band Gap of Ag-doped Anatase TiO2

## Problem background
Anatase TiO₂ is a wide-bandgap semiconductor widely studied for photocatalysis. Substitutional doping with noble metals such as Ag can introduce acceptor levels and localized gap states, tuning the electronic structure and potentially improving visible-light harvesting. Understanding how Ag incorporation modifies lattice parameters and the electronic band gap is essential for designing better photocatalysts. In this task you will compute, using first-principles density functional theory (DFT), the relaxed lattice constants of pristine anatase TiO₂ and several Ag-doped configurations, as well as the pristine band gap at a hybrid-functional level. The target quantities reveal whether Ag doping expands the lattice and creates gap states that could shift the optical absorption edge.

## Approach
You will perform first-principles DFT calculations using an open-source DFT code such as Quantum ESPRESSO or CP2K. Starting from the publicly known anatase crystal structure (space group I4₁/amd), you will construct a 2×2×1 supercell and prepare three substitutionally Ag‑doped configurations by replacing one, two, and three Ti atoms with Ag, corresponding to nominal concentrations of 6.25%, 12.5%, and 18.75%. For each of the four systems (pristine + three doped) you will relax both atomic positions and cell parameters at the PBE‑GGA level using norm‑conserving pseudopotentials. From these relaxations you will extract the lattice parameters a, c, and volume. Finally, using the relaxed pristine structure, you will compute the electronic band structure with the HSE06 hybrid functional and determine the indirect band gap. This workflow mirrors the computational strategy of the original study; you are free to choose pseudopotential sets and numerical convergence settings that yield physically reasonable results.

## Reproduction target
Your goal is to compute and report the following quantities, which will be compared against hidden reference values:
- Relaxed lattice parameters a (Å), c (Å), and volume (Å³) for the pristine anatase TiO₂ supercell and for the three Ag‑doped supercells (6.25%, 12.5%, 18.75% Ag).
- The HSE06 indirect band gap (in eV) of pristine anatase TiO₂.

All values must be written to the designated output files in the formats specified in the workflow steps. No external experimental data sets need to be fetched; the only required input is the publicly available anatase crystal structure.

## Assets

- Anatase TiO2 crystal structure (space group I41/amd): https://materialsproject.org/materials/mp-390
- Open-source DFT code (Quantum ESPRESSO or CP2K): https://www.quantum-espresso.org/ or https://www.cp2k.org/
- Norm-conserving pseudopotentials (PseudoDojo): http://www.pseudo-dojo.org/

## Workflow steps

### Step 1: Build supercell structures
- Role: process
- Action: Construct a 2×2×1 supercell of anatase TiO2 using the public crystal structure. Create three substitutional Ag‑doped configurations by replacing one, two, and three Ti atoms with Ag (6.25%, 12.5%, 18.75% concentrations). Save the initial structures for subsequent relaxation.
- Evidence: none

### Step 2: Geometry optimization and lattice parameters
- Role: scored (load-bearing)
- Action: Perform DFT geometry optimization (PBE-GGA functional, norm-conserving pseudopotentials) for the pristine and three Ag-doped supercells, relaxing both atomic positions and cell parameters. Extract the relaxed lattice parameters a (Å), c (Å), and volume (Å³) for each composition and write them to /app/outputs/lattice_parameters.json.
- Output file: `/app/outputs/lattice_parameters.json`
- Format: json
- Contract: {"pristine": {"a": float, "c": float, "volume": float}, "Ag_6.25": {"a": float, "c": float, "volume": float}, "Ag_12.5": {"a": float, "c": float, "volume": float}, "Ag_18.75": {"a": float, "c": float, "volume": float}}
- Scoring: scored by hidden verifier

### Step 3: HSE06 band gap calculation
- Role: scored (load-bearing)
- Action: Using the relaxed pristine anatase TiO2 structure from step2, perform an HSE06 hybrid functional band-structure calculation. Determine the indirect band gap (eV) and write the value to /app/outputs/pristine_band_gap.txt.
- Output file: `/app/outputs/pristine_band_gap.txt`
- Format: txt
- Contract: A single floating-point number (e.g., 3.16) in units of eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.json`
- `/app/outputs/pristine_band_gap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.json
- path: `/app/outputs/lattice_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice parameters for pristine and three Ag-doped anatase TiO2 supercells. Units: a and c in Å, volume in Å³.
- schema:
  - `type`: object
  - `required`: `pristine`, `Ag_6.25`, `Ag_12.5`, `Ag_18.75`
  - `properties`:
    - `pristine`:
      - `type`: object
      - `required`: `a`, `c`, `volume`
      - `properties`:
        - `a`:
          - `type`: number
        - `c`:
          - `type`: number
        - `volume`:
          - `type`: number
    - `Ag_6.25`:
      - `type`: object
      - `required`: `a`, `c`, `volume`
      - `properties`:
        - `a`:
          - `type`: number
        - `c`:
          - `type`: number
        - `volume`:
          - `type`: number
    - `Ag_12.5`:
      - `type`: object
      - `required`: `a`, `c`, `volume`
      - `properties`:
        - `a`:
          - `type`: number
        - `c`:
          - `type`: number
        - `volume`:
          - `type`: number
    - `Ag_18.75`:
      - `type`: object
      - `required`: `a`, `c`, `volume`
      - `properties`:
        - `a`:
          - `type`: number
        - `c`:
          - `type`: number
        - `volume`:
          - `type`: number

### pristine_band_gap.txt
- path: `/app/outputs/pristine_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: HSE06 indirect band gap of pristine anatase TiO2, in eV.
- schema:
  - `type`: text
  - `description`: Single line containing a floating-point number representing the HSE06 indirect band gap of pristine anatase TiO2 in eV.

Notes: Temporarily restoring original output contract to pass static checks; missing headline claims (Ag-doping band gap reduction and absorption edge shift) will be addressed in subsequent cross‑cutting edits.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "pristine",
          "Ag_6.25",
          "Ag_12.5",
          "Ag_18.75"
        ],
        "properties": {
          "pristine": {
            "type": "object",
            "required": [
              "a",
              "c",
              "volume"
            ],
            "properties": {
              "a": {
                "type": "number"
              },
              "c": {
                "type": "number"
              },
              "volume": {
                "type": "number"
              }
            }
          },
          "Ag_6.25": {
            "type": "object",
            "required": [
              "a",
              "c",
              "volume"
            ],
            "properties": {
              "a": {
                "type": "number"
              },
              "c": {
                "type": "number"
              },
              "volume": {
                "type": "number"
              }
            }
          },
          "Ag_12.5": {
            "type": "object",
            "required": [
              "a",
              "c",
              "volume"
            ],
            "properties": {
              "a": {
                "type": "number"
              },
              "c": {
                "type": "number"
              },
              "volume": {
                "type": "number"
              }
            }
          },
          "Ag_18.75": {
            "type": "object",
            "required": [
              "a",
              "c",
              "volume"
            ],
            "properties": {
              "a": {
                "type": "number"
              },
              "c": {
                "type": "number"
              },
              "volume": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Relaxed lattice parameters for pristine and three Ag-doped anatase TiO2 supercells. Units: a and c in Å, volume in Å³."
    },
    {
      "file": "pristine_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line containing a floating-point number representing the HSE06 indirect band gap of pristine anatase TiO2 in eV."
      },
      "description": "HSE06 indirect band gap of pristine anatase TiO2, in eV."
    }
  ],
  "notes": "Temporarily restoring original output contract to pass static checks; missing headline claims (Ag-doping band gap reduction and absorption edge shift) will be addressed in subsequent cross‑cutting edits."
}
```

## How you are scored
A hidden verifier will read your output files and score each artifact independently against reference values that are consistent with the protocol you are asked to follow. The lattice parameters for each composition are checked with tolerances that account for the spread introduced by different DFT codes, pseudopotentials, and numerical choices; the band gap is similarly evaluated with a tolerance suitable for hybrid‑functional calculations. The scores from the two scored steps are combined by weight to produce your final reward. Simply reporting a plausible number is not sufficient — your workflow must actually be executed and produce the required values from a genuine DFT simulation.
