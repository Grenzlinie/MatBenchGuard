# DFT Investigation of Magnetic Ground State, Elastic Constants, and Bader Charges of ThCr2Si2

## Problem background
ThCr2Si2 is the prototype structure of a broad family of 122 ternary phases, including iron-based superconductors. Despite its structural importance, first-principles data on its electronic, magnetic, and elastic properties were lacking. This work provides a first-principles density functional theory investigation of the structural, magnetic, elastic, and bonding properties of ThCr2Si2, which serves as a reference for the large class of 122-like systems.

## Approach
The approach is based on plane-wave density functional theory with the generalized gradient approximation (GGA-PBE). Five collinear magnetic configurations (non-magnetic, ferromagnetic, and three antiferromagnetic orderings: AFM1, AFM2, AFM3) are examined. Total energies and Cr magnetic moments are computed from fully relaxed structures to determine the magnetic ground state. For the predicted ground-state structure, the six independent elastic constants are obtained from stress-strain distortions, and Bader charge analysis is performed to extract effective atomic charges. All calculations can be carried out with an open-source DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials.

## Reproduction target
Compute the total-energy differences (ΔE in eV/f.u.) and Cr magnetic moments (μB) for all five magnetic configurations, using the AFM3 configuration as the energy reference (ΔE = 0). Compute the six independent elastic constants (C11, C12, C13, C33, C44, C66, all in GPa) for the AFM3 structure. Perform a Bader charge analysis on the AFM3 structure to obtain effective atomic charges (in e) for Th, Cr, and Si. All results must be written to the prescribed JSON output files.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for Th, Cr, Si: https://www.quantum-espresso.org/pseudopotentials/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Generate initial magnetic configurations
- Role: process
- Action: Prepare input structures for ThCr2Si2 in the non-magnetic (NM), ferromagnetic (FM), and three collinear antiferromagnetic configurations (AFM1, AFM2, AFM3) as described in the paper. Use the experimental tetragonal cell (space group I4/mmm) with lattice parameters a≈4.04 Å, c≈10.59 Å and atomic positions Th (2a (0,0,0)), Cr (4d (0,0.5,0.25)), Si (4e (0,0,z~0.375)). Set up spin polarizations according to the patterns shown in the paper.
- Evidence: none

### Step 2: DFT structure relaxation and total energies
- Role: process
- Action: Run full geometry optimizations (positions and cell parameters) for all five magnetic configurations using a plane-wave DFT code with GGA-PBE pseudopotentials. Converge forces to ≤2 meV/Å. Obtain relaxed total energies, atomic magnetic moments, and the final relaxed structure for the AFM3 state.
- Evidence: `/app/outputs/relax_output.log`

### Step 3: Magnetic ground state results
- Role: scored
- Action: From the computed total energies, derive the total-energy differences (ΔE in eV/f.u.) with AFM3 as the zero reference, and extract the Cr magnetic moments (MM in μB). Write the results to step_01_magnetic_ground_state.json.
- Output file: `/app/outputs/step_01_magnetic_ground_state.json`
- Format: json
- Contract: {"NM": {"delta_E": <float>, "MM": null}, "FM": {"delta_E": <float>, "MM": <float>}, "AFM1": {"delta_E": <float>, "MM": [<float>, <float>]}, "AFM2": {"delta_E": <float>, "MM": <float>}, "AFM3": {"delta_E": 0.0, "MM": <float>}}
- Scoring: scored by hidden verifier

### Step 4: Elastic constant calculations (stress-strain)
- Role: process
- Action: For the relaxed AFM3 structure, compute the six independent elastic constants (C11, C12, C13, C33, C44, C66) by applying small finite distortions and evaluating the resulting stress tensor using the DFT code.
- Evidence: `/app/outputs/elastic_output.log`

### Step 5: Elastic constant results
- Role: scored (load-bearing)
- Action: Report the computed elastic constants in step_02_elastic_constants.json.
- Output file: `/app/outputs/step_02_elastic_constants.json`
- Format: json
- Contract: {"C11": <float>, "C12": <float>, "C13": <float>, "C33": <float>, "C44": <float>, "C66": <float>}
- Scoring: scored by hidden verifier

### Step 6: Bader charge analysis
- Role: process
- Action: Perform a self-consistent field calculation on the relaxed AFM3 structure to obtain the ground-state charge density. Then use the Bader code to partition the charge density and compute effective atomic charges.
- Evidence: `/app/outputs/bader_output.log`

### Step 7: Bader charge results
- Role: scored (load-bearing)
- Action: Write the effective Bader charges for Th, Cr, and Si to step_03_bader_charges.json.
- Output file: `/app/outputs/step_03_bader_charges.json`
- Format: json
- Contract: {"Th": <float>, "Cr": <float>, "Si": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_magnetic_ground_state.json`
- `/app/outputs/step_02_elastic_constants.json`
- `/app/outputs/step_03_bader_charges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_magnetic_ground_state.json
- path: `/app/outputs/step_01_magnetic_ground_state.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total-energy differences and magnetic moments for all five magnetic configurations.
- schema:
  - `type`: object
  - `required`: `NM`, `FM`, `AFM1`, `AFM2`, `AFM3`
  - `items`: object
  - `units`:
    - `delta_E`: eV/f.u.
    - `MM`: μB

### step_02_elastic_constants.json
- path: `/app/outputs/step_02_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Six independent elastic constants for the AFM3 phase.
- schema:
  - `type`: object
  - `required`: `C11`, `C12`, `C13`, `C33`, `C44`, `C66`
  - `items`: object
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C66`: GPa

### step_03_bader_charges.json
- path: `/app/outputs/step_03_bader_charges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bader effective atomic charges for Th, Cr, and Si in the AFM3 ground state.
- schema:
  - `type`: object
  - `required`: `Th`, `Cr`, `Si`
  - `items`: object
  - `units`:
    - `Th`: e
    - `Cr`: e
    - `Si`: e

Notes: Tolerances and exact reference values are hidden. The agent must produce results by re-running the DFT workflow; copying values from other sources will not pass.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_magnetic_ground_state.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "NM",
          "FM",
          "AFM1",
          "AFM2",
          "AFM3"
        ],
        "items": {},
        "units": {
          "delta_E": "eV/f.u.",
          "MM": "μB"
        }
      },
      "description": "Total-energy differences and magnetic moments for all five magnetic configurations."
    },
    {
      "file": "step_02_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "C11",
          "C12",
          "C13",
          "C33",
          "C44",
          "C66"
        ],
        "items": {},
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C66": "GPa"
        }
      },
      "description": "Six independent elastic constants for the AFM3 phase."
    },
    {
      "file": "step_03_bader_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Th",
          "Cr",
          "Si"
        ],
        "items": {},
        "units": {
          "Th": "e",
          "Cr": "e",
          "Si": "e"
        }
      },
      "description": "Bader effective atomic charges for Th, Cr, and Si in the AFM3 ground state."
    }
  ],
  "notes": "Tolerances and exact reference values are hidden. The agent must produce results by re-running the DFT workflow; copying values from other sources will not pass."
}
```

## How you are scored
A hidden verifier reads each scored output file and compares the reported values against reference values derived from the original paper. Each artifact is scored independently using appropriate tolerances, and the final reward is a weighted combination of the per-step scores. Only values computed by actually executing the described DFT workflow are considered valid; reporting numbers obtained from any other source will not pass the verifier.
