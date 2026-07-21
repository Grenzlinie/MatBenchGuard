# Compute Exchange Coupling Constants via Broken-Symmetry DFT for a Heterometallic Ni–V Anderson Wheel

## Problem background
This task addresses the quantitative description of magnetic exchange interactions in a heterometallic Anderson wheel containing Ni(II) and V(IV) ions. Understanding the pairwise exchange coupling constants that govern the magnetic behavior of such polynuclear clusters is essential for rationalizing their experimental magnetic properties and for designing new molecule-based magnetic materials. In the original work, broken-symmetry density functional theory (DFT) calculations were performed on the crystal structure of the Ni–V wheel to extract the four distinct isotropic exchange constants J1–J4. Your goal is to recompute these constants from first principles using the same theoretical protocol, thereby reproducing the DFT-derived exchange parameters that the original study used to interpret the magnetic data.

## Approach
The workflow uses the broken-symmetry DFT approach to evaluate magnetic exchange. Starting from the publicly deposited crystal structure (CCDC 1847956), spin-polarised DFT calculations are carried out with the B3LYP hybrid functional and a triple-ζ valence (TZV) all-electron basis set. Total energies are computed for the high-spin (ferromagnetic) reference state and for four broken-symmetry solutions that correspond to the distinct exchange pathways J1–J4 defined by the topology of the metal–ligand bridge network. The isotropic exchange constants are then obtained by applying the broken-symmetry energy-difference formula, which maps the computed state energies onto the pairwise coupling parameters of the Heisenberg spin Hamiltonian. All calculations must be performed on the full crystal-structure geometry without truncation, and the energies must be sufficiently converged to yield stable exchange constants.

## Reproduction target
Compute the four isotropic exchange constants J1, J2, J3, J4 (in cm⁻¹) for the Ni–V Anderson wheel using broken-symmetry B3LYP/TZV DFT calculations on the crystal structure. Save the results in `/app/outputs/j_values.json` as a JSON object with keys `"J1"`, `"J2"`, `"J3"`, `"J4"`, each mapping to a floating-point number in reciprocal centimetres. The target values represent the DFT-predicted coupling strengths for the four distinct pairwise exchange pathways present in the cluster.

## Assets

- Crystal structure of complex 1 (CCDC 1847956): https://www.ccdc.cam.ac.uk/structures/
- Open-source DFT code supporting B3LYP/TZV (e.g., ORCA): https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Obtain crystal structure
- Role: process
- Action: Download the crystal structure file (CIF format) of the target Ni–V wheel complex from CCDC accession 1847956.
- Evidence: `/app/outputs/complex1.cif`

### Step 2: Run broken-symmetry DFT calculations
- Role: process
- Action: Perform spin-polarized DFT calculations using the B3LYP functional and TZV basis set on the crystal structure. Compute total energies for the high-spin (HS) state and the four broken-symmetry (BS) states corresponding to the distinct exchange pathways J1–J4. Save the converged energies.
- Evidence: `/app/outputs/dft_energies.txt`

### Step 3: Extract exchange constants J1–J4
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute the four isotropic exchange constants J1, J2, J3, J4 (in cm⁻¹) using the broken-symmetry formula. Write the values to a JSON file.
- Output file: `/app/outputs/j_values.json`
- Format: json
- Contract: object {J1: float cm⁻¹, J2: float cm⁻¹, J3: float cm⁻¹, J4: float cm⁻¹}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/j_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### j_values.json
- path: `/app/outputs/j_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Exchange coupling constants J1–J4 for the target heterometallic wheel obtained from broken-symmetry DFT, in cm⁻¹. Compared to hidden reference values from the published DFT calculations.
- schema:
  - `type`: object
  - `required`: `J1`, `J2`, `J3`, `J4`
  - `properties`:
    - `J1`:
      - `type`: number
      - `description`: Exchange coupling constant J1 in cm⁻¹
    - `J2`:
      - `type`: number
      - `description`: Exchange coupling constant J2 in cm⁻¹
    - `J3`:
      - `type`: number
      - `description`: Exchange coupling constant J3 in cm⁻¹
    - `J4`:
      - `type`: number
      - `description`: Exchange coupling constant J4 in cm⁻¹

Notes: The hidden reference corresponds to the DFT-computed values for the Ni-containing wheel reported in the original study. Units are cm⁻¹ and the sign convention follows −2∑J_ij S_i·S_j.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "j_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "J1",
          "J2",
          "J3",
          "J4"
        ],
        "properties": {
          "J1": {
            "type": "number",
            "description": "Exchange coupling constant J1 in cm⁻¹"
          },
          "J2": {
            "type": "number",
            "description": "Exchange coupling constant J2 in cm⁻¹"
          },
          "J3": {
            "type": "number",
            "description": "Exchange coupling constant J3 in cm⁻¹"
          },
          "J4": {
            "type": "number",
            "description": "Exchange coupling constant J4 in cm⁻¹"
          }
        }
      },
      "description": "Exchange coupling constants J1–J4 for the target heterometallic wheel obtained from broken-symmetry DFT, in cm⁻¹. Compared to hidden reference values from the published DFT calculations."
    }
  ],
  "notes": "The hidden reference corresponds to the DFT-computed values for the Ni-containing wheel reported in the original study. Units are cm⁻¹ and the sign convention follows −2∑J_ij S_i·S_j."
}
```

## How you are scored
A hidden verifier independently checks the `j_values.json` file you submit. It compares each reported exchange constant (J1–J4) to reference DFT values that correspond to the same computational protocol applied to the same crystal structure. The comparison checks both the sign and the magnitude of each constant. A reported constant must agree with the reference within a hidden tolerance to earn credit. Partial credit is awarded: each of the four constants contributes 25% of the total reward. The verifier does not inspect intermediate files; only the final JSON artifact is scored. Submitting the correct numbers is necessary, but the task requires that you obtain them through genuine execution of the DFT workflow; the scoring premise is that you followed the prescribed method.
