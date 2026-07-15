# DFT study of Ge3N4 polymorphs: structure, equation of state, and phase transition

## Problem background
Germanium nitride (Ge3N4) crystallizes in several polymorphs. The hexagonal β phase (phenacite structure, space group P63/m) is the ground-state phase at ambient conditions, while the cubic spinel γ phase (space group Fd3̅m) is a high‑pressure phase synthesized in diamond‑anvil cells. Both phases are wide‑band‑gap semiconductors and are of interest for potential optoelectronic applications. Understanding their structural parameters, equations of state, electronic band gaps, vibrational properties, and the pressure‑induced β→γ phase transition is essential for assessing their stability and functionality. This task is a first‑principles investigation of these properties using density‑functional theory (DFT).

## Approach
The reproduction uses plane‑wave DFT within the local‑density approximation (LDA, Ceperley–Alder functional) and ultrasoft pseudopotentials, with an open‑source code (Quantum ESPRESSO). For each phase, the crystal structure is relaxed at multiple fixed unit‑cell volumes, keeping the space‑group symmetry, to generate total‑energy vs. volume (E vs. V) data. These data are fitted to the Birch–Murnaghan equation of state to extract the equilibrium binding energy, equilibrium volume, bulk modulus, and its pressure derivative. The optimized equilibrium structure is taken as the relaxed geometry at the volume closest to the fitted V₀, and its lattice constants and fractional internal coordinates are recorded. Using that equilibrium structure, the electronic band structure is computed and the direct LDA band gap at the Γ point is obtained. Γ‑point phonon frequencies are calculated via the finite‑displacement method (or with the help of Phonopy), and each mode is labeled with its irreducible representation and Raman/IR activity. Finally, the enthalpy H = E + pV is evaluated for both phases as a function of pressure, and the β→γ transition pressure is identified as the crossing point of the two enthalpy curves.

## Reproduction target
Produce the following five scored artifacts for the β (P63/m) and γ (spinel, Fd3̅m) phases of Ge3N4:

1. **eos_data.json** – Birch–Murnaghan equation‑of‑state parameters: equilibrium binding energy E₀ (eV/atom), equilibrium volume V₀ (Å³/atom), bulk modulus K (GPa), and its pressure derivative K′ (dimensionless) for each phase.
2. **structural_data.json** – Zero‑pressure optimized lattice constants (a, c for β; a for γ) and all fractional internal coordinates (atom type, Wyckoff label, x, y, z).
3. **band_gap.json** – LDA direct band gap at the Γ point (in eV) for each phase.
4. **phonon_frequencies.json** – All Γ‑point phonon frequencies (in cm⁻¹), each with its symmetry label and boolean flags indicating IR and Raman activity, for both phases.
5. **transition_pressure.txt** – A single line containing the β→γ equilibrium transition pressure in GPa.

All output files must be placed in `/app/outputs`. The required formats and schemas are detailed in the workflow steps below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Ge and N: https://www.materialscloud.org/discover/sssp/table
- Phonopy: phonopy

## Workflow steps

### Step 1: Prepare initial crystal structures
- Role: process
- Action: Define the hexagonal beta (P6_3/m) and cubic spinel gamma (Fd-3m) structures of Ge3N4 using published lattice parameters and atomic positions as initial guesses. Write these structures to input files for the DFT code.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: DFT geometry optimization at multiple volumes
- Role: process
- Action: For each phase, perform LDA plane-wave DFT structural relaxations at a set of at least seven fixed unit-cell volumes spanning the equilibrium region. At each volume, relax internal coordinates and lattice shape while preserving space-group symmetry. Record the total energy (E) and volume (V) for each relaxed structure.
- Evidence: `/app/outputs/ev_data.json`

### Step 3: Birch-Murnaghan EOS fitting
- Role: scored
- Action: Fit the computed E(V) data to the Birch-Murnaghan equation of state to extract the equilibrium binding energy (E0), equilibrium volume (V0), bulk modulus (K), and pressure derivative (K′). Report these four parameters for both phases in JSON.
- Output file: `/app/outputs/eos_data.json`
- Format: json
- Contract: JSON object with keys 'beta' and 'gamma', each containing E0 (eV/atom), V0 (Å³/atom), K (GPa), K_prime (dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Extract optimized equilibrium structure
- Role: scored (load-bearing)
- Action: From the relaxed geometry at the volume closest to the fitted V0, collect the lattice constants and all fractional internal coordinates (including the Wyckoff positions as given in the paper). Report them as structured JSON.
- Output file: `/app/outputs/structural_data.json`
- Format: json
- Contract: JSON object with keys 'beta' and 'gamma', each containing 'lattice_constants' (object: a, c for beta; a for gamma) and 'internal_coordinates' (list of objects with atom, site_label, fractional_coordinates x,y,z).
- Scoring: scored by hidden verifier

### Step 5: LDA band gap calculation
- Role: scored
- Action: Using the optimized equilibrium structure, compute the electronic band structure along high-symmetry paths. Extract the LDA band gap at the Gamma point. Report the direct band gap for each phase in a JSON file.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: JSON object with keys 'beta' and 'gamma', each containing 'LDA_gap' (float in eV).
- Scoring: scored by hidden verifier

### Step 6: Gamma-point phonon calculation
- Role: scored
- Action: At the equilibrium geometry, compute the Gamma-point phonon frequencies using finite-displacement method (or phonopy). List all modes with their irreducible representation labels, and indicate Raman/IR activity. Report in JSON.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object with keys 'beta' and 'gamma'. Each value is an array of objects with keys 'frequency_cm-1' (number), 'symmetry_label' (string), 'ir_active' (boolean), 'raman_active' (boolean).
- Scoring: scored by hidden verifier

### Step 7: Beta→gamma phase transition pressure
- Role: scored
- Action: Using the fitted EOS or directly from the E(V) data, compute the enthalpy H = E + pV as a function of pressure for both phases. Determine the pressure at which the enthalpies cross, i.e., the equilibrium beta→gamma transition pressure. Report this value in a text file.
- Output file: `/app/outputs/transition_pressure.txt`
- Format: txt
- Contract: A single line containing the transition pressure in GPa (e.g., '5.2').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_data.json`
- `/app/outputs/structural_data.json`
- `/app/outputs/band_gap.json`
- `/app/outputs/phonon_frequencies.json`
- `/app/outputs/transition_pressure.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_data.json
- path: `/app/outputs/eos_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Birch-Murnaghan EOS parameters (E0, V0, K, K') for beta and gamma phases.
- schema:
  - `type`: object
  - `required_keys`: `beta`, `gamma`
  - `beta`:
    - `type`: object
    - `properties`:
      - `E0`: number (eV/atom)
      - `V0`: number (Å³/atom)
      - `K`: number (GPa)
      - `K_prime`: number (dimensionless)
  - `gamma`:
    - `type`: object
    - `properties`:
      - `E0`: number (eV/atom)
      - `V0`: number (Å³/atom)
      - `K`: number (GPa)
      - `K_prime`: number (dimensionless)

### structural_data.json
- path: `/app/outputs/structural_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized zero-pressure crystal structures (lattice constants and fractional internal coordinates).
- schema:
  - `type`: object
  - `required_keys`: `beta`, `gamma`
  - `beta`:
    - `type`: object
    - `properties`:
      - `lattice_constants`:
        - `type`: object
        - `properties`:
          - `a`: number (Å)
          - `c`: number (Å)
      - `internal_coordinates`:
        - `type`: array
        - `items`:
          - `atom`: string
          - `site_label`: string
          - `x`: number
          - `y`: number
          - `z`: number
  - `gamma`:
    - `type`: object
    - `properties`:
      - `lattice_constants`:
        - `type`: object
        - `properties`:
          - `a`: number (Å)
      - `internal_coordinates`:
        - `type`: array
        - `items`:
          - `atom`: string
          - `site_label`: string
          - `x`: number
          - `y`: number
          - `z`: number

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: LDA direct band gap at Gamma for beta and gamma phases.
- schema:
  - `type`: object
  - `required_keys`: `beta`, `gamma`
  - `beta`:
    - `LDA_gap`: number (eV)
  - `gamma`:
    - `LDA_gap`: number (eV)

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Gamma-point phonon frequencies and symmetries for beta and gamma phases.
- schema:
  - `type`: object
  - `required_keys`: `beta`, `gamma`
  - `beta`:
    - `type`: array
    - `items`:
      - `frequency_cm-1`: number
      - `symmetry_label`: string
      - `ir_active`: boolean
      - `raman_active`: boolean
  - `gamma`:
    - `type`: array
    - `items`:
      - `frequency_cm-1`: number
      - `symmetry_label`: string
      - `ir_active`: boolean
      - `raman_active`: boolean

### transition_pressure.txt
- path: `/app/outputs/transition_pressure.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Beta→gamma equilibrium phase transition pressure in GPa.
- schema:
  - `type`: text
  - `content`: single GPa value

Notes: All scored artifacts are compared to the paper’s LDA results with appropriate hidden tolerances. The structural_data step is marked load-bearing to ensure actual DFT geometry optimizations are performed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "beta",
          "gamma"
        ],
        "beta": {
          "type": "object",
          "properties": {
            "E0": "number (eV/atom)",
            "V0": "number (Å³/atom)",
            "K": "number (GPa)",
            "K_prime": "number (dimensionless)"
          }
        },
        "gamma": {
          "type": "object",
          "properties": {
            "E0": "number (eV/atom)",
            "V0": "number (Å³/atom)",
            "K": "number (GPa)",
            "K_prime": "number (dimensionless)"
          }
        }
      },
      "description": "Birch-Murnaghan EOS parameters (E0, V0, K, K') for beta and gamma phases."
    },
    {
      "file": "structural_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "beta",
          "gamma"
        ],
        "beta": {
          "type": "object",
          "properties": {
            "lattice_constants": {
              "type": "object",
              "properties": {
                "a": "number (Å)",
                "c": "number (Å)"
              }
            },
            "internal_coordinates": {
              "type": "array",
              "items": {
                "atom": "string",
                "site_label": "string",
                "x": "number",
                "y": "number",
                "z": "number"
              }
            }
          }
        },
        "gamma": {
          "type": "object",
          "properties": {
            "lattice_constants": {
              "type": "object",
              "properties": {
                "a": "number (Å)"
              }
            },
            "internal_coordinates": {
              "type": "array",
              "items": {
                "atom": "string",
                "site_label": "string",
                "x": "number",
                "y": "number",
                "z": "number"
              }
            }
          }
        }
      },
      "description": "Optimized zero-pressure crystal structures (lattice constants and fractional internal coordinates)."
    },
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "beta",
          "gamma"
        ],
        "beta": {
          "LDA_gap": "number (eV)"
        },
        "gamma": {
          "LDA_gap": "number (eV)"
        }
      },
      "description": "LDA direct band gap at Gamma for beta and gamma phases."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "beta",
          "gamma"
        ],
        "beta": {
          "type": "array",
          "items": {
            "frequency_cm-1": "number",
            "symmetry_label": "string",
            "ir_active": "boolean",
            "raman_active": "boolean"
          }
        },
        "gamma": {
          "type": "array",
          "items": {
            "frequency_cm-1": "number",
            "symmetry_label": "string",
            "ir_active": "boolean",
            "raman_active": "boolean"
          }
        }
      },
      "description": "Gamma-point phonon frequencies and symmetries for beta and gamma phases."
    },
    {
      "file": "transition_pressure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single GPa value"
      },
      "description": "Beta→gamma equilibrium phase transition pressure in GPa."
    }
  ],
  "notes": "All scored artifacts are compared to the paper’s LDA results with appropriate hidden tolerances. The structural_data step is marked load-bearing to ensure actual DFT geometry optimizations are performed."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the five scored artifacts. For every artifact, the verifier reads your file, extracts the reported numbers, and compares them to reference values using appropriate tolerances and comparison policies. Each artifact contributes a predefined weight toward the final score (total = 1.0). Simply reporting numbers that happen to match is not sufficient; you must genuinely execute the DFT pipeline. The verifier does not access the network – all ground truth is pre‑bundled in the evaluation environment. Your total reward is the weighted sum of the per‑artifact scores, recorded in `/logs/verifier/reward.txt`.
