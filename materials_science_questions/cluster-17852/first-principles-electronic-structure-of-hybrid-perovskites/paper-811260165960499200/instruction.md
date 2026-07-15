# DFT Dielectric and Polaron Properties of MAPbI3 with Oriented MA+ Rotors

## Problem background
Hybrid organic–inorganic lead iodide perovskites such as MAPbI3 feature methylammonium (MA+) cations that rotate rapidly within the inorganic PbI3− cages. Understanding how these rotational dynamics interact with photoexcited carriers is central to explaining carrier lifetimes and ultimately designing better photovoltaic materials. This interaction has been hypothesized to involve carrier-rotor coupling mediated by polaron formation, where the orientation of the MA+ cation alters dielectric screening and trapping energies. Reproducing the first-principles predictions for these orientation-dependent electronic properties will test whether such an electron–rotor interaction is quantitatively plausible.

## Approach
Use density functional theory (DFT) with a generalized gradient approximation (GGA) functional and a van der Waals correction (e.g. Grimme D2). Compute dielectric constant tensors via density functional perturbation theory (linear response) on a MAPbI3 unit cell with the MA+ C−N axis aligned along the [100], [110], and [111] crystallographic directions. Then, on a 3×3×3 supercell for each orientation, calculate polaron trapping energies as the energy difference between a delocalized electronic state and a fully relaxed localized (trapped) state when one electron is added (electron polaron) or removed (hole polaron). Separately, apply the rigid free-rotor model to estimate rotational frequency ratios of the four MA+ isotopologues (CH3NH3+, CH3ND3+, CD3NH3+, CD3ND3+) by computing moments of inertia and using the relation ν ∝ 1/√I, assuming identical molecular geometry and standard atomic masses.

## Reproduction target
Produce three JSON artifacts:
1. dielectric_constants.json – the full 3×3 dielectric tensor and its averaged diagonal value for each of the three MA+ orientations.
2. polaron_trapping_energies.json – electron and hole polaron trapping energies (in meV) for each orientation.
3. rotational_frequencies.json – the rotational frequency ratio of each isotopologue relative to CH3NH3+.
These quantities must be computed from the DFT and analytical models, not looked up.

## Assets

- MAPbI3 crystal structure: https://doi.org/10.1039/C3TA10564A
- Quantum ESPRESSO or equivalent DFT code: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/
- Python packages: numpy

## Workflow steps

### Step 1: Build oriented MAPbI3 structural models
- Role: process
- Action: Construct the unit cell and a 3×3×3 supercell of tetragonal MAPbI3 (a=8.8310 Å, c=12.6855 Å). For each crystallographic orientation [100], [110], [111], orient the C-N axis of the MA+ cation accordingly while keeping the inorganic PbI3− framework fixed. Generate three unit cells and three supercells, one per orientation.
- Evidence: `/app/outputs/orientations_setup.log`

### Step 2: Compute dielectric constant tensors
- Role: scored
- Action: For each orientation ([100], [110], [111]), perform a DFT calculation on the unit cell using density functional perturbation theory (linear response) to obtain the full dielectric constant tensor (3×3 matrix in row-major order). Compute the averaged diagonal value as (ε_xx+ε_yy+ε_zz)/3. Use a GGA functional with van der Waals correction. Write a JSON file with the tensor and averaged diagonal for each orientation.
- Output file: `/app/outputs/dielectric_constants.json`
- Format: json
- Contract: Top-level object with keys "100", "110", "111". Each value is an object with "tensor" (list of 9 floats) and "avg_diagonal" (float).
- Scoring: scored by hidden verifier

### Step 3: Compute polaron trapping energies
- Role: scored (load-bearing)
- Action: For each orientation, use the 3×3×3 supercell. Compute the energy of the delocalized (bulk-like) state via a standard SCF calculation. Then introduce a localized electron (or hole) by adding/removing one electron and fully relax the structure to obtain the trapped polaron state. The polaron trapping energy is the difference between the two energies. Sample the Brillouin zone at the gamma point. Report electron and hole trapping energies in meV.
- Output file: `/app/outputs/polaron_trapping_energies.json`
- Format: json
- Contract: Top-level object with keys "100", "110", "111". Each value is an object with "electron" (float) and "hole" (float) in meV.
- Scoring: scored by hidden verifier

### Step 4: Compute rotational frequency ratios
- Role: scored
- Action: Using the rigid free-rotor model, compute the rotational frequency of each MA+ isotopologue (CH3NH3+, CH3ND3+, CD3NH3+, CD3ND3+) about the C-N axis. Frequency is inversely proportional to the square root of the moment of inertia. Calculate the ratio relative to CH3NH3+. Input atomic masses from standard sources; assume identical molecular geometry.
- Output file: `/app/outputs/rotational_frequencies.json`
- Format: json
- Contract: Object with keys "CH3NH3", "CH3ND3", "CD3NH3", "CD3ND3", each a float ratio (CH3NH3 = 1.0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dielectric_constants.json`
- `/app/outputs/polaron_trapping_energies.json`
- `/app/outputs/rotational_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dielectric_constants.json
- path: `/app/outputs/dielectric_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dielectric constant tensors and average diagonal values for MAPbI3 with MA+ oriented along [100], [110], [111].
- schema:
  - `type`: object
  - `required`:
    - `100`:
      - `type`: object
      - `required`:
        - `tensor`: list of 9 floats
        - `avg_diagonal`: float
    - `110`:
      - `type`: object
      - `required`:
        - `tensor`: list of 9 floats
        - `avg_diagonal`: float
    - `111`:
      - `type`: object
      - `required`:
        - `tensor`: list of 9 floats
        - `avg_diagonal`: float

### polaron_trapping_energies.json
- path: `/app/outputs/polaron_trapping_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electron and hole polaron trapping energies in meV for each MA+ orientation.
- schema:
  - `type`: object
  - `required`:
    - `100`:
      - `type`: object
      - `required`:
        - `electron`: float (meV)
        - `hole`: float (meV)
    - `110`:
      - `type`: object
      - `required`:
        - `electron`: float (meV)
        - `hole`: float (meV)
    - `111`:
      - `type`: object
      - `required`:
        - `electron`: float (meV)
        - `hole`: float (meV)

### rotational_frequencies.json
- path: `/app/outputs/rotational_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Rotational frequency ratios of the four MA+ isotopologues relative to CH3NH3+ (CH3NH3 = 1.0).
- schema:
  - `type`: object
  - `required`:
    - `CH3NH3`: float
    - `CH3ND3`: float
    - `CD3NH3`: float
    - `CD3ND3`: float

Notes: All tolerances are hidden. The checker compares the reported dielectric constants, polaron trapping energies, and rotational frequency ratios to the paper's published values. It also verifies the ordering of polaron trapping energies: [110] > [111] > [100] for both carriers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dielectric_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "100": {
            "type": "object",
            "required": {
              "tensor": "list of 9 floats",
              "avg_diagonal": "float"
            }
          },
          "110": {
            "type": "object",
            "required": {
              "tensor": "list of 9 floats",
              "avg_diagonal": "float"
            }
          },
          "111": {
            "type": "object",
            "required": {
              "tensor": "list of 9 floats",
              "avg_diagonal": "float"
            }
          }
        }
      },
      "description": "Dielectric constant tensors and average diagonal values for MAPbI3 with MA+ oriented along [100], [110], [111]."
    },
    {
      "file": "polaron_trapping_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "100": {
            "type": "object",
            "required": {
              "electron": "float (meV)",
              "hole": "float (meV)"
            }
          },
          "110": {
            "type": "object",
            "required": {
              "electron": "float (meV)",
              "hole": "float (meV)"
            }
          },
          "111": {
            "type": "object",
            "required": {
              "electron": "float (meV)",
              "hole": "float (meV)"
            }
          }
        }
      },
      "description": "Electron and hole polaron trapping energies in meV for each MA+ orientation."
    },
    {
      "file": "rotational_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "CH3NH3": "float",
          "CH3ND3": "float",
          "CD3NH3": "float",
          "CD3ND3": "float"
        }
      },
      "description": "Rotational frequency ratios of the four MA+ isotopologues relative to CH3NH3+ (CH3NH3 = 1.0)."
    }
  ],
  "notes": "All tolerances are hidden. The checker compares the reported dielectric constants, polaron trapping energies, and rotational frequency ratios to the paper's published values. It also verifies the ordering of polaron trapping energies: [110] > [111] > [100] for both carriers."
}
```

## How you are scored
A hidden verifier reads the three output JSON files and compares your computed values to independently known reference values. Each scored artifact (dielectric constants, polaron trapping energies, rotational frequency ratios) is evaluated separately using tolerances that account for methodological differences; the verifier also checks that the ordering of polaron trapping energies across orientations follows a physically expected trend. The final reward is a weighted combination of these per‐artifact scores. Reporting the paper's numbers without performing the computations will not earn credit.
