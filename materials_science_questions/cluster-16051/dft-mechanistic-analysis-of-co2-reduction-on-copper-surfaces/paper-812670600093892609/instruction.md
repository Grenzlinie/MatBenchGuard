# DFT Electronic Properties of Cu/Zn Alloys for CO2 Electroreduction

## Problem background
Copper-based catalysts are among the few materials capable of deep electroreduction of CO2 to multi-carbon products. However, pure Cu surfaces suffer from low selectivity and competing hydrogen evolution. Alloying copper with zinc has been explored as a strategy to tune the electronic structure and improve catalytic performance. First-principles calculations can reveal how Zn incorporation alters key quantities such as the surface work function, the d-band center of Cu atoms, and the energetics of hydrogen adsorption, all of which are thought to influence catalytic activity and selectivity. Computing these electronic properties from density functional theory provides insight into the synergistic role of Zn in Cu/Zn bimetallic catalysts.

## Approach
Perform spin-polarized DFT calculations using a plane-wave code and a suitable exchange-correlation functional (e.g., PBE) along with standard pseudopotentials. Construct symmetric surface slab models for the four metallic systems: pure Cu in its fcc phase, and the alloys Cu3Zn (fcc L12), CuZn (bcc B2), and Cu5Zn8 (complex cubic). For each slab, compute the work function as the difference between the vacuum level and the Fermi energy, and extract the projected d-band center of surface Cu atoms from the density of states. Determine the hydrogen adsorption free energy ΔG_H* by calculating the total energy difference between a slab with an adsorbed hydrogen atom and the clean slab, corrected by half the energy of a gas-phase H2 molecule and vibrational zero-point contributions. Then build co-adsorbed configurations of *CO and *CH2 on each surface and, after relaxation, record the C–C distance in the most stable geometry. The four quantities form a consistent set of descriptors that can be compared across the four alloy compositions.

## Reproduction target
Compute, via the DFT workflow described below, four electronic properties for each of the four systems: pure Cu, Cu3Zn, CuZn, and Cu5Zn8:

- work function (in eV)
- d-band center of surface Cu atoms (in eV, referenced to the Fermi level)
- hydrogen adsorption free energy ΔG_H* (in eV)
- C–C distance in the most stable co-adsorbed structure of *CO and *CH2 (in Å)

All values must be collected into a single JSON file, /app/outputs/dft_properties.json, following the exact schema given in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (SSSP/PseudoDojo): https://www.materialscloud.org/sssp/
- Crystal structures of Cu, Cu3Zn, CuZn, Cu5Zn8: https://materialsproject.org/
- ASE (Atomic Simulation Environment): https://wiki.fysik.dtu.dk/ase/
- Standard DFT workflows for adsorption energies

## Workflow steps

### Step 1: Build surface slab models
- Role: process
- Action: Construct symmetric surface slab models for Cu(111), Cu3Zn(111), CuZn(110), and Cu5Zn8(100) using ASE or similar tools. Start from bulk crystal structures (obtained from public materials databases or standard references). Generate Quantum ESPRESSO input files for each slab; ensure sufficient vacuum layer and slab thickness to model the surface.
- Evidence: `/app/outputs/slab_models.log`

### Step 2: DFT property calculation and output
- Role: scored (load-bearing)
- Action: For each slab model, run DFT calculations using Quantum ESPRESSO to compute: (a) work function as the difference between vacuum level and Fermi energy, (b) projected d-band center of surface Cu atoms, (c) hydrogen adsorption free energy ΔG_H* = E(slab+H) − E(slab) − ½E(H2) + zero-point energy corrections, and (d) the C-C distance in the most stable co-adsorbed configuration of *CO and *CH2. Collect all results into a single JSON file.
- Output file: `/app/outputs/dft_properties.json`
- Format: json
- Contract: JSON object with top-level keys 'Cu', 'Cu3Zn', 'CuZn', 'Cu5Zn8'. Each value is an object with keys 'work_function_eV' (float), 'd_band_center_eV' (float), 'delta_G_H_star_eV' (float), 'C_C_distance_A' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_properties.json
- path: `/app/outputs/dft_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the computed work function, d-band center, hydrogen adsorption free energy, and co-adsorbed C-C distance for pure Cu, Cu3Zn, CuZn, and Cu5Zn8 surfaces. The hidden checker compares these values against reference values obtained from a published source with tolerance, and additionally verifies that the relationships among the four alloy compositions satisfy appropriate structural consistency checks.
- schema:
  - `type`: object
  - `required`: `Cu`, `Cu3Zn`, `CuZn`, `Cu5Zn8`
  - `properties`:
    - `Cu`:
      - `type`: object
      - `properties`:
        - `work_function_eV`:
          - `type`: number
        - `d_band_center_eV`:
          - `type`: number
        - `delta_G_H_star_eV`:
          - `type`: number
        - `C_C_distance_A`:
          - `type`: number
    - `Cu3Zn`:
      - `type`: object
      - `properties`:
        - `work_function_eV`:
          - `type`: number
        - `d_band_center_eV`:
          - `type`: number
        - `delta_G_H_star_eV`:
          - `type`: number
        - `C_C_distance_A`:
          - `type`: number
    - `CuZn`:
      - `type`: object
      - `properties`:
        - `work_function_eV`:
          - `type`: number
        - `d_band_center_eV`:
          - `type`: number
        - `delta_G_H_star_eV`:
          - `type`: number
        - `C_C_distance_A`:
          - `type`: number
    - `Cu5Zn8`:
      - `type`: object
      - `properties`:
        - `work_function_eV`:
          - `type`: number
        - `d_band_center_eV`:
          - `type`: number
        - `delta_G_H_star_eV`:
          - `type`: number
        - `C_C_distance_A`:
          - `type`: number

Notes: The checker will perform a reference match against hidden gold values (±0.5 eV for energies, ±0.5 Å for distance) and will additionally audit the internal consistency of the results across the four alloy compositions. The agent must use a consistent pseudopotential library and exchange-correlation functional; systematic toolchain shifts are absorbed by the tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Cu",
          "Cu3Zn",
          "CuZn",
          "Cu5Zn8"
        ],
        "properties": {
          "Cu": {
            "type": "object",
            "properties": {
              "work_function_eV": {
                "type": "number"
              },
              "d_band_center_eV": {
                "type": "number"
              },
              "delta_G_H_star_eV": {
                "type": "number"
              },
              "C_C_distance_A": {
                "type": "number"
              }
            }
          },
          "Cu3Zn": {
            "type": "object",
            "properties": {
              "work_function_eV": {
                "type": "number"
              },
              "d_band_center_eV": {
                "type": "number"
              },
              "delta_G_H_star_eV": {
                "type": "number"
              },
              "C_C_distance_A": {
                "type": "number"
              }
            }
          },
          "CuZn": {
            "type": "object",
            "properties": {
              "work_function_eV": {
                "type": "number"
              },
              "d_band_center_eV": {
                "type": "number"
              },
              "delta_G_H_star_eV": {
                "type": "number"
              },
              "C_C_distance_A": {
                "type": "number"
              }
            }
          },
          "Cu5Zn8": {
            "type": "object",
            "properties": {
              "work_function_eV": {
                "type": "number"
              },
              "d_band_center_eV": {
                "type": "number"
              },
              "delta_G_H_star_eV": {
                "type": "number"
              },
              "C_C_distance_A": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Contains the computed work function, d-band center, hydrogen adsorption free energy, and co-adsorbed C-C distance for pure Cu, Cu3Zn, CuZn, and Cu5Zn8 surfaces. The hidden checker compares these values against reference values obtained from a published source with tolerance, and additionally verifies that the relationships among the four alloy compositions satisfy appropriate structural consistency checks."
    }
  ],
  "notes": "The checker will perform a reference match against hidden gold values (±0.5 eV for energies, ±0.5 Å for distance) and will additionally audit the internal consistency of the results across the four alloy compositions. The agent must use a consistent pseudopotential library and exchange-correlation functional; systematic toolchain shifts are absorbed by the tolerance."
}
```

## How you are scored
A hidden verifier scores your outputs. Each property in dft_properties.json is compared against a hidden reference (derived from established data) within appropriate tolerances. In addition, the verifier checks that the relationships among the four alloy compositions satisfy expected structural trends. The verifier combines these checks into a single reward. Because the scoring relies on a genuine DFT workflow, simply reporting known literature numbers is unlikely to satisfy the structural consistency checks.
