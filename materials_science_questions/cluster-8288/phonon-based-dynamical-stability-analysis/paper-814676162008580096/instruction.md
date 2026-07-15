# First-principles calculation of structural, electronic, and vibrational properties of β- and γ-Ge₃N₄

## Problem background
Germanium nitride (Ge₃N₄) is a group‑IV nitride with potential optoelectronic and high‑strength applications. The hexagonal β phase (phenacite structure, space group P6₃/m) and the high‑pressure cubic spinel γ phase (Fd‑3m) are the focus of this first‑principles study. Understanding their optimized geometries, equations of state, electronic band gaps, and vibrational spectra is essential for assessing stability and optical properties.

## Approach
The study uses first‑principles density‑functional theory (DFT) with the local‑density approximation (LDA) for exchange‑correlation. Plane‑wave basis sets and pseudopotentials represent the electrons and ions. For each phase, total energies and forces are computed for a sequence of unit‑cell volumes while relaxing internal coordinates, yielding an energy‑vs‑volume curve. The Birch‑Murnaghan equation of state is fitted to these curves to extract the equilibrium volume per atom, bulk modulus, and pressure derivative. Electronic structure is obtained from a self‑consistent calculation at the Γ point, and the direct band gap is extracted. Γ‑point phonon frequencies and symmetry assignments are computed using the finite‑displacement method, in which individual atoms are displaced and the resulting forces are used to build the force‑constant matrix.

## Reproduction target
Produce the following quantities for both β‑Ge₃N₄ (P6₃/m) and γ‑Ge₃N₄ (Fd‑3m):
1. LDA‑optimized lattice constants and fractional atomic coordinates at the equilibrium volume.
2. Birch‑Murnaghan EOS parameters V₀ (Å³/atom), K (GPa), and K′.
3. The LDA direct band gap at Γ (eV).
4. The full set of Γ‑point phonon frequencies (cm⁻¹) with irreducible‑representation labels.

Save each class of results to the corresponding JSON output file listed in the workflow steps. The hidden verifier will compare your computed values to reference data and assign a score per stage.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code) or equivalent: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials for Ge and N (or equivalent library): https://www.materialscloud.org/discover/sssp/table
- Phonopy (optional, for phonon finite-displacement post-processing): https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: DFT structural relaxations for E(V) data
- Role: process
- Action: For β-Ge₃N₄ (space group P6₃/m) and γ-Ge₃N₄ (space group Fd-3m), perform plane-wave DFT structural relaxations using the LDA exchange-correlation functional over a series of fixed unit-cell volumes spanning approximately ±5% compression/expansion around the experimental equilibrium volume. At each volume, relax the lattice parameters (consistent with the volume and space-group symmetry) and all internal atomic coordinates. Record total energy, relaxed lattice constants, and final fractional coordinates to an intermediate file (ev_data.json) for subsequent EOS fitting and equilibrium structure selection.
- Evidence: `/app/outputs/ev_data.json`

### Step 2: Report optimized lattice parameters and internal coordinates
- Role: scored
- Action: From the relaxation data, identify the volume corresponding to the minimum total energy (the equilibrium volume). Extract the lattice constants and fractional atomic coordinates of β and γ at that volume, ensuring the reported values are consistent with the paper’s space group conventions. Write the results to optimized_structures.json.
- Output file: `/app/outputs/optimized_structures.json`
- Format: json
- Contract: {"beta": {"space_group": "P6_3/m", "a": float, "c": float, "Ge_6h": [x, y, z], "N_6h": [x, y, z], "N_2c": [x, y, z]}, "gamma": {"space_group": "Fd-3m", "a": float, "GeIV_8a": [0,0,0], "GeVI_16d": [5/8,5/8,5/8], "N_32e": [x, x, x]}}
- Scoring: scored by hidden verifier

### Step 3: Report Birch-Murnaghan EOS parameters
- Role: scored
- Action: Fit the set of (V,E) data for β and γ to the Birch-Murnaghan equation of state to obtain the equilibrium volume per atom V₀ (Å³/atom), bulk modulus K (GPa), and its pressure derivative K′. Write the results to eos_parameters.json.
- Output file: `/app/outputs/eos_parameters.json`
- Format: json
- Contract: {"beta": {"V0": float, "K": float, "Kprime": float}, "gamma": {"V0": float, "K": float, "Kprime": float}}
- Scoring: scored by hidden verifier

### Step 4: Electronic structure calculation at Γ point
- Role: process
- Action: Using the optimized equilibrium structures, perform a self-consistent DFT calculation and compute Kohn-Sham eigenvalues at the Γ point. Determine the direct band gap as the difference between the conduction-band minimum and the valence-band maximum at Γ.
- Evidence: none

### Step 5: Report LDA band gaps
- Role: scored
- Action: Extract the direct band gap at Γ for β and γ and write them to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"beta": {"LDA_band_gap_eV": float}, "gamma": {"LDA_band_gap_eV": float}}
- Scoring: scored by hidden verifier

### Step 6: Γ-point phonon calculation
- Role: process
- Action: For the equilibrium β and γ structures, compute the force-constant matrix using finite atomic displacements (e.g., ±0.01 Å) in DFT. Diagonalize the dynamical matrix at Γ to obtain phonon frequencies, and use point-group symmetry to assign irreducible representations (e.g., A_g, E_2g, B_u, etc.).
- Evidence: none

### Step 7: Report phonon frequencies
- Role: scored (load-bearing)
- Action: Collect all Γ-point phonon frequencies with their symmetry labels for β and γ, and save to phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: {"beta": [{"frequency_cm-1": float, "symmetry": string}, ...], "gamma": [{"frequency_cm-1": float, "symmetry": string}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structures.json`
- `/app/outputs/eos_parameters.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structures.json
- path: `/app/outputs/optimized_structures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice constants and fractional internal coordinates for the equilibrium structures of β- and γ-Ge₃N₄.
- schema:
  - `type`: object
  - `required`:
    - `beta`:
      - `type`: object
      - `required`:
        - `space_group`: string
        - `a`: float
        - `c`: float
        - `Ge_6h`: array of 3 floats
        - `N_6h`: array of 3 floats
        - `N_2c`: array of 3 floats
    - `gamma`:
      - `type`: object
      - `required`:
        - `space_group`: string
        - `a`: float
        - `GeIV_8a`: array of 3 floats
        - `GeVI_16d`: array of 3 floats
        - `N_32e`: array of 3 floats

### eos_parameters.json
- path: `/app/outputs/eos_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Birch-Murnaghan equation-of-state parameters for the two phases.
- schema:
  - `type`: object
  - `required`:
    - `beta`:
      - `type`: object
      - `required`:
        - `V0`: float (Å³/atom)
        - `K`: float (GPa)
        - `Kprime`: float
    - `gamma`:
      - `type`: object
      - `required`:
        - `V0`: float (Å³/atom)
        - `K`: float (GPa)
        - `Kprime`: float

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: LDA direct band gaps at the Γ point.
- schema:
  - `type`: object
  - `required`:
    - `beta`:
      - `type`: object
      - `required`:
        - `LDA_band_gap_eV`: float
    - `gamma`:
      - `type`: object
      - `required`:
        - `LDA_band_gap_eV`: float

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Γ-point phonon frequencies and irreducible representations.
- schema:
  - `type`: object
  - `required`:
    - `beta`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`:
          - `frequency_cm-1`: float
          - `symmetry`: string
    - `gamma`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`:
          - `frequency_cm-1`: float
          - `symmetry`: string

Notes: All outputs are compared to the paper's reported LDA reference values with appropriate tolerances. The symmetry labels for β are A_g, B_g, E_1g, E_2g, A_u, B_u, E_1u, E_2u; for γ: A_1g, E_g, T_1g, T_2g, A_2u, E_u, T_1u, T_2u.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta": {
            "type": "object",
            "required": {
              "space_group": "string",
              "a": "float",
              "c": "float",
              "Ge_6h": "array of 3 floats",
              "N_6h": "array of 3 floats",
              "N_2c": "array of 3 floats"
            }
          },
          "gamma": {
            "type": "object",
            "required": {
              "space_group": "string",
              "a": "float",
              "GeIV_8a": "array of 3 floats",
              "GeVI_16d": "array of 3 floats",
              "N_32e": "array of 3 floats"
            }
          }
        }
      },
      "description": "Lattice constants and fractional internal coordinates for the equilibrium structures of β- and γ-Ge₃N₄."
    },
    {
      "file": "eos_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta": {
            "type": "object",
            "required": {
              "V0": "float (Å³/atom)",
              "K": "float (GPa)",
              "Kprime": "float"
            }
          },
          "gamma": {
            "type": "object",
            "required": {
              "V0": "float (Å³/atom)",
              "K": "float (GPa)",
              "Kprime": "float"
            }
          }
        }
      },
      "description": "Birch-Murnaghan equation-of-state parameters for the two phases."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta": {
            "type": "object",
            "required": {
              "LDA_band_gap_eV": "float"
            }
          },
          "gamma": {
            "type": "object",
            "required": {
              "LDA_band_gap_eV": "float"
            }
          }
        }
      },
      "description": "LDA direct band gaps at the Γ point."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta": {
            "type": "array",
            "items": {
              "type": "object",
              "required": {
                "frequency_cm-1": "float",
                "symmetry": "string"
              }
            }
          },
          "gamma": {
            "type": "array",
            "items": {
              "type": "object",
              "required": {
                "frequency_cm-1": "float",
                "symmetry": "string"
              }
            }
          }
        }
      },
      "description": "Γ-point phonon frequencies and irreducible representations."
    }
  ],
  "notes": "All outputs are compared to the paper's reported LDA reference values with appropriate tolerances. The symmetry labels for β are A_g, B_g, E_1g, E_2g, A_u, B_u, E_1u, E_2u; for γ: A_1g, E_g, T_1g, T_2g, A_2u, E_u, T_1u, T_2u."
}
```

## How you are scored
Each scored output file is checked separately by a hidden verifier. For a given artifact, the verifier reads the values you provided, compares them to established reference values using appropriate tolerances, and computes a partial score. The final overall score is a weighted sum of these stage scores. To receive credit, you must actually execute the computational workflow and write correctly formatted JSON files; merely looking up or guessing the numbers is not sufficient because the verifier expects results derived from the LDA computational protocol outlined in the workflow.
