# DFT Geometry Optimization and Mulliken Population Analysis of [Si(S2O7)3]2-

## Problem background
Tetravalent silicon in octahedral coordination by oxygen is unusual, and examples with purely inorganic, chelating ligands are exceedingly rare. The synthesis of the hexacoordinate [Si(S2O7)3]2- anion, in which three bidentate disulfate groups surround the central silicon, provides the first structurally characterized member of this class. To understand the electronic structure and bonding in this unique silicate, density functional theory (DFT) calculations were carried out on the isolated anion. Reproducing the quantum-chemical characterization of the [Si(S2O7)3]2- anion yields the optimized molecular geometry and the effective atomic charges from a Mulliken population analysis—quantities that reflect the nature of the Si–O bonds.

## Approach
The electronic structure of the isolated [Si(S2O7)3]2- anion is described by Kohn-Sham density functional theory using the global hybrid PBE0 exchange-correlation functional and the correlation-consistent cc-pVDZ basis set. An initial three-dimensional geometry is constructed from standard disulfate structural parameters, and a full geometry optimization is performed to locate the equilibrium structure. From the converged wavefunction, Mulliken population analysis provides effective atomic charges, and the final Cartesian coordinates give the Si–O bond distances. The calculation is executed with an open-source quantum chemistry package; no experimental data are used as input.

## Reproduction target
Perform a full geometry optimization of the [Si(S2O7)3]2- anion at the PBE0/cc-pVDZ level and extract the following quantities into the structured JSON file `reproduction_outputs.json`:

- the effective Mulliken charge on silicon (float, dimensionless),
- the effective Mulliken charges on the six oxygen atoms that are directly bonded to silicon (list of six floats, dimensionless),
- the six Si–O bond distances in picometres from the optimized geometry (list of six floats).

The target is to compute these values from first principles; the exact numerical reference is unknown to you and will be checked by a hidden verifier.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- cc-pVDZ basis set: ORCA basis set library
- Open Babel: openbabel

## Workflow steps

### Step 1: DFT Geometry Optimization
- Role: process
- Action: Build an initial 3D structure of the [Si(S2O7)3]2- anion from standard disulfate geometry, then run an open-source quantum chemistry package (e.g., ORCA) with the PBE0 functional and cc-pVDZ basis set to perform a full geometry optimization. Save the output (including energies, convergence, final coordinates, and Mulliken charges) to `orca_output.log`.
- Evidence: `/app/outputs/orca_output.log`

### Step 2: Extract Mulliken Charges and Si-O Distances
- Role: scored (load-bearing)
- Action: Parse the ORCA output file (`orca_output.log`) to extract the Mulliken atomic charge on Si and the six coordinating oxygen atoms, and the six Si–O bond distances from the optimized geometry. Write these values to `reproduction_outputs.json`.
- Output file: `/app/outputs/reproduction_outputs.json`
- Format: json
- Contract: JSON object with keys: "Si_charge" (float, dimensionless), "O_charges" (list of 6 floats, dimensionless), "Si_O_distances" (list of 6 floats, unit: pm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_outputs.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_outputs.json
- path: `/app/outputs/reproduction_outputs.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the effective Mulliken charge on silicon, charges on the six coordinating oxygen atoms, and the six Si-O bond distances from the DFT-optimized anion.
- schema:
  - `type`: object
  - `required`:
    - `Si_charge`: number
    - `O_charges`: array
    - `Si_O_distances`: array
  - `items`:
    - `O_charges`:
      - `type`: number
    - `Si_O_distances`:
      - `type`: number
  - `units`:
    - `Si_O_distances`: pm

Notes: The checker compares each value to hidden paper-reported gold values using absolute tolerances. The ORCA output log is retained as evidence but not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_outputs.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Si_charge": "number",
          "O_charges": "array",
          "Si_O_distances": "array"
        },
        "items": {
          "O_charges": {
            "type": "number"
          },
          "Si_O_distances": {
            "type": "number"
          }
        },
        "units": {
          "Si_O_distances": "pm"
        }
      },
      "description": "Contains the effective Mulliken charge on silicon, charges on the six coordinating oxygen atoms, and the six Si-O bond distances from the DFT-optimized anion."
    }
  ],
  "notes": "The checker compares each value to hidden paper-reported gold values using absolute tolerances. The ORCA output log is retained as evidence but not scored."
}
```

## How you are scored
An automated verifier reads your `reproduction_outputs.json` and compares each numerical entry to hidden reference values that have been extracted from the published study. Each reported charge and each bond distance is checked for agreement within a tolerance. The reward is the proportion of those values that lie within the allowed tolerance range. The verifier does not inspect intermediate files; only the final JSON output is scored. Reporting a number without performing the DFT calculation is not sufficient, because the required values depend on the specific functional, basis set, and optimization protocol used.
