# Computation of Zero-Field Splitting and Exchange Coupling Constants from Crystal Structures using DFT/CASSCF

## Problem background
Transition metal complexes can exhibit rich magnetic behaviour arising from zero‑field splitting (ZFS) and exchange interactions between paramagnetic centres. Accurately computing these magnetic parameters from first principles helps to understand magneto‑structural correlations. The goal of this task is to theoretically determine the ZFS parameters (axial D and rhombic E/D ratio) for the two crystallographically distinct Co(II) centres within a trinuclear CoIII₂CoII complex, and the nearest‑neighbour exchange coupling constants (J1 and J2) within a pentanuclear Ni(II) cluster, using the published crystal structures and quantum chemical methods. The results will provide insight into how the coordination environment and bridging ligands influence the magnetic anisotropy and coupling strength.

## Approach
The magnetic parameters are computed directly from the crystal structures without geometry relaxation. For the Co(II) centres, a complete active space self‑consistent field calculation (CASSCF) followed by second‑order N‑electron valence state perturbation theory (NEVPT2) is employed, using an active space that includes seven electrons in the five 3d orbitals (CAS(7,5)). The zero‑field splitting tensor and g‑tensor are obtained from the spin–orbit coupling within the quartet and doublet states, yielding D and the E/D ratio. For the Ni₅ cluster, broken‑symmetry density functional theory (DFT) is applied with the B3LYP hybrid functional and the TZVP basis set. The exchange coupling constants J1 and J2 are extracted by mapping the energies of several broken‑symmetry spin configurations onto a Heisenberg spin Hamiltonian, following a least‑squares fitting procedure. All quantum chemical calculations are carried out with the ORCA program package.

## Reproduction target
Compute the zero‑field splitting parameters (D and E/D) for the two crystallographically independent Co(II) centres (hereafter referred to as Co1 and Co3) in the trinuclear CoIII₂CoII complex, using the crystal structure from CCDC 2046942. Compute the nearest‑neighbour exchange coupling constants J1 and J2 for the pentanuclear Ni(II) cluster from CCDC 2046943. All values must be saved in a single JSON file, `/app/outputs/computed_parameters.json`, following the exact structure defined in the output contract. The calculations must be performed at the CASSCF/NEVPT2 level for the Co centres and at the broken‑symmetry DFT (B3LYP/TZVP) level for the Ni cluster; no geometry optimisation is allowed.

## Assets

- CIF file for complex 1 (CCDC 2046942): https://www.ccdc.cam.ac.uk/structures/
- CIF file for complex 2 (CCDC 2046943): https://www.ccdc.cam.ac.uk/structures/
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/app.php/portal

## Workflow steps

### Step 1: Extract molecular geometries from CIF files
- Role: process
- Action: Download the CIF files for complex 1 (CCDC 2046942) and complex 2 (CCDC 2046943). Extract atomic coordinates to prepare input structures for quantum chemical calculations. Save geometry summary as evidence.
- Evidence: `/app/outputs/geometry_summary.txt`

### Step 2: Compute magnetic parameters via CASSCF/NEVPT2 and broken-symmetry DFT
- Role: scored (load-bearing)
- Action: For complex 1, run CASSCF/NEVPT2 calculations on each crystallographically distinct Co(II) center using ORCA to obtain zero-field splitting parameters D and E/D. For complex 2, run broken-symmetry DFT calculations (B3LYP/TZVP) on the pentanuclear Ni(II) cluster to extract the two nearest-neighbor exchange coupling constants J1 and J2. Compile all computed values into /app/outputs/computed_parameters.json.
- Output file: `/app/outputs/computed_parameters.json`
- Format: json
- Contract: {"Co1": {"D": <float in cm⁻¹>, "E_over_D": <float>}, "Co3": {"D": <float in cm⁻¹>, "E_over_D": <float>}, "Ni": {"J1": <float in cm⁻¹>, "J2": <float in cm⁻¹}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_parameters.json
- path: `/app/outputs/computed_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The computed zero-field splitting parameters (D, E/D) for the two Co(II) centers and exchange coupling constants (J1, J2) for the Ni5 cluster. All values are compared to hidden paper-reported references within respective tolerances.
- schema:
  - `type`: object
  - `required`: `Co1`, `Co3`, `Ni`
  - `properties`:
    - `Co1`:
      - `type`: object
      - `required`: `D`, `E_over_D`
      - `properties`:
        - `D`:
          - `type`: number
          - `units`: cm^{-1}
        - `E_over_D`:
          - `type`: number
    - `Co3`:
      - `type`: object
      - `required`: `D`, `E_over_D`
      - `properties`:
        - `D`:
          - `type`: number
          - `units`: cm^{-1}
        - `E_over_D`:
          - `type`: number
    - `Ni`:
      - `type`: object
      - `required`: `J1`, `J2`
      - `properties`:
        - `J1`:
          - `type`: number
          - `units`: cm^{-1}
        - `J2`:
          - `type`: number
          - `units`: cm^{-1}

Notes: The checker compares each parameter against the paper’s DFT/CASSCF computed reference values using tolerances (±5 cm⁻¹ for D, ±0.05 for E/D, ±2 cm⁻¹ for J). No gold values are exposed in the task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Co1",
          "Co3",
          "Ni"
        ],
        "properties": {
          "Co1": {
            "type": "object",
            "required": [
              "D",
              "E_over_D"
            ],
            "properties": {
              "D": {
                "type": "number",
                "units": "cm^{-1}"
              },
              "E_over_D": {
                "type": "number"
              }
            }
          },
          "Co3": {
            "type": "object",
            "required": [
              "D",
              "E_over_D"
            ],
            "properties": {
              "D": {
                "type": "number",
                "units": "cm^{-1}"
              },
              "E_over_D": {
                "type": "number"
              }
            }
          },
          "Ni": {
            "type": "object",
            "required": [
              "J1",
              "J2"
            ],
            "properties": {
              "J1": {
                "type": "number",
                "units": "cm^{-1}"
              },
              "J2": {
                "type": "number",
                "units": "cm^{-1}"
              }
            }
          }
        }
      },
      "description": "The computed zero-field splitting parameters (D, E/D) for the two Co(II) centers and exchange coupling constants (J1, J2) for the Ni5 cluster. All values are compared to hidden paper-reported references within respective tolerances."
    }
  ],
  "notes": "The checker compares each parameter against the paper’s DFT/CASSCF computed reference values using tolerances (±5 cm⁻¹ for D, ±0.05 for E/D, ±2 cm⁻¹ for J). No gold values are exposed in the task."
}
```

## How you are scored
A hidden verifier reads your `computed_parameters.json` and compares each parameter (D, E/D, J1, J2) against a hidden reference value using tolerances that account for the expected method‑dependent spread of quantum chemical calculations. Your reward is determined by how many of the six quantities agree with the reference within those tolerances. Simply looking up and reporting the literature values is not sufficient; the verification environment expects that the submitted numbers have been derived from the quantum‑chemical workflow described in the steps above. The scoring policy is `reference_match`, as specified in the output contract, and all scored artefacts contribute to the final reward.
