# Intramolecular Hydrogen Bond Energy from Internal Rotation Barriers for β-Diketones

## Problem background
Intramolecular hydrogen bonds stabilize certain molecular conformations, but their energy ($E_{\mathrm{HB}}$) is not directly measurable and must be estimated. The classic estimate compares the energy of the chelate (hydrogen-bonded) form with that of an open, hydrogen‑bond‑free conformation. This can be unreliable when the open form suffers from extraneous interactions that contaminate the energy difference. An alternative approach uses internal rotation barriers: the barrier for rotating the donor group (e.g., O–H) is expected to be higher in the chelate form due to the stabilising hydrogen bond. By comparing this barrier to that of a properly chosen hydrogen‑bond‑free reference molecule, one may obtain a more robust estimate of the hydrogen bond energy. This method has been proposed and tested on simple β‑diketones, where the hydrogen bond is O–H···O.

## Approach
The rotation barrier method (RBM) estimates the hydrogen bond energy as the difference between the donor rotation barrier in the chelate form ($\mathrm{RB}_{\mathrm{D}}^{\mathrm{chelate}}$) and the analogous barrier in a hydrogen‑bond‑free reference compound ($\mathrm{RB}_{\mathrm{D}}^{\mathrm{reference}}$): $E_{\mathrm{HB1}} = \mathrm{RB}_{\mathrm{D}}^{\mathrm{chelate}} - \mathrm{RB}_{\mathrm{D}}^{\mathrm{reference}}$. For the O–H donor group, the reference molecule is obtained by replacing the adjacent carbonyl group (R–C=O) with a hydrogen atom. The classic estimate is $E_{\mathrm{HB}} = E_{\mathrm{open}} - E_{\mathrm{chelate}}$, where $E_{\mathrm{open}}$ is the energy of the donor rotated by 180°. The two methods should yield consistent values when extraneous interactions are minimal. This task applies both methods to malondialdehyde (MDA) and acetylacetone (ACAC) at the B3LYP/6‑31G** level using an open‑source quantum chemistry package. Full geometry optimizations are performed for the chelate minima, the open form (donor rotated), and the reference minima. Potential energy scans of the O–H torsion angle (5° increments) provide the rotation barriers.

## Reproduction target
Using an open‑source quantum chemistry code (e.g., Psi4 or PySCF), perform B3LYP/6‑31G** calculations for MDA and ACAC. For each molecule, compute: (i) the total energies of the chelate and open minima, (ii) the O–H rotation barrier in the chelate form, and (iii) the O–H rotation barrier in the hydrogen‑bond‑free reference molecule. From these, derive the classic hydrogen bond energy ($E_{\mathrm{HB}}$) and the RBM estimate ($E_{\mathrm{HB1}}$). Record all intermediate and final energies in a structured JSON file as specified in the workflow steps. The reproduced energies should demonstrate internal consistency: for each molecule, $E_{\mathrm{HB1}}$ should lie within a reasonable range of $E_{\mathrm{HB}}$, as expected if the rotation barrier method is a valid approximation.

## Assets

- Open-source quantum chemistry program (e.g., Psi4 or PySCF): https://psicode.org/ or https://pyscf.org/

## Workflow steps

### Step 1: Generate molecular structures
- Role: process
- Action: Define initial molecular geometries (Cartesian coordinates or Z-matrix) for malondialdehyde (MDA) and acetylacetone (ACAC) in the chelate (hydrogen-bonded) conformation, the open conformation (donor group rotated 180°), and the hydrogen-bond-free reference molecules (obtained by replacing the carbonyl group with H as described in the paper). Provide these as input files for the quantum chemistry code.
- Evidence: none

### Step 2: Run DFT calculations: optimizations and torsion scans
- Role: process
- Action: Using the selected open-source quantum chemistry program, perform the following calculations at the B3LYP/6-31G** level for each molecule/conformation: (i) full geometry optimization to obtain stable minima (E_chelate, E_open, and reference minima); (ii) for the O–H torsion scans, perform constrained optimizations at 5° increments from 0° to 180° (or until the maximum energy point) to obtain energy profiles. The maximum energy along each scan gives the rotation barrier (RB_D_chelate) and the reference barrier (RB_D_reference).
- Evidence: none

### Step 3: Extract energies and compute hydrogen bond energies
- Role: scored (load-bearing)
- Action: Parse the output from the DFT calculations to extract: E_chelate (total energy of the chelate minimum), E_open (total energy of the open minimum), RB_D_chelate (max energy from donor O–H torsion scan in chelate), RB_D_reference (max energy from donor O–H torsion scan in the reference molecule). Compute classic E_HB = E_open – E_chelate and rotation barrier E_HB1 = RB_D_chelate – RB_D_reference. Convert all energies to kJ/mol (1 Hartree = 2625.5 kJ/mol) and write the results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of objects. Each object keys: molecule (string), level (string), E_chelate (float, Hartree), E_open (float, Hartree), E_HB (float, kJ/mol), RB_D_chelate (float, kJ/mol), RB_D_reference (float, kJ/mol), E_HB1 (float, kJ/mol).
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
- description: Computed hydrogen bond energies and related quantities for MDA and ACAC at B3LYP/6-31G** level. The checker will compare the reported values to hidden reference values from the original paper.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `molecule`, `level`, `E_chelate`, `E_open`, `E_HB`, `RB_D_chelate`, `RB_D_reference`, `E_HB1`
    - `properties`:
      - `molecule`:
        - `type`: string
      - `level`:
        - `type`: string
      - `E_chelate`:
        - `type`: number
        - `units`: Hartree
      - `E_open`:
        - `type`: number
        - `units`: Hartree
      - `E_HB`:
        - `type`: number
        - `units`: kJ/mol
      - `RB_D_chelate`:
        - `type`: number
        - `units`: kJ/mol
      - `RB_D_reference`:
        - `type`: number
        - `units`: kJ/mol
      - `E_HB1`:
        - `type`: number
        - `units`: kJ/mol

Notes: Only B3LYP/6-31G** calculations for MDA and ACAC are required. MP2 results and additional systems are omitted. The rotation barrier method is validated by comparing E_HB1 with classic E_HB.

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
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "molecule",
            "level",
            "E_chelate",
            "E_open",
            "E_HB",
            "RB_D_chelate",
            "RB_D_reference",
            "E_HB1"
          ],
          "properties": {
            "molecule": {
              "type": "string"
            },
            "level": {
              "type": "string"
            },
            "E_chelate": {
              "type": "number",
              "units": "Hartree"
            },
            "E_open": {
              "type": "number",
              "units": "Hartree"
            },
            "E_HB": {
              "type": "number",
              "units": "kJ/mol"
            },
            "RB_D_chelate": {
              "type": "number",
              "units": "kJ/mol"
            },
            "RB_D_reference": {
              "type": "number",
              "units": "kJ/mol"
            },
            "E_HB1": {
              "type": "number",
              "units": "kJ/mol"
            }
          }
        }
      },
      "description": "Computed hydrogen bond energies and related quantities for MDA and ACAC at B3LYP/6-31G** level. The checker will compare the reported values to hidden reference values from the original paper."
    }
  ],
  "notes": "Only B3LYP/6-31G** calculations for MDA and ACAC are required. MP2 results and additional systems are omitted. The rotation barrier method is validated by comparing E_HB1 with classic E_HB."
}
```

## How you are scored
Each workspace step's output is evaluated independently by a hidden verifier. The main scored artifact is `results.json`. The verifier checks that the file contains all required fields for both molecules, that the reported values are physically reasonable (positive barriers and energy differences), and that the numerical results agree with hidden reference values within an appropriate margin. The final reward is a weighted sum over all scoring stages. Reporting the paper’s numeric results is not sufficient; the computed energies must follow the protocol described in the workflow and be written to `/app/outputs/results.json`.
