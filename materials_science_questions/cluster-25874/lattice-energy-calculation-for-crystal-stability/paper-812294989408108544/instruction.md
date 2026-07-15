# Packing Potential Energy Calculation for Crystal Structures

## Problem background
The paper studies the homo- and heteromolecular crystals of the hexaruthenium carbido carbonyl clusters Ru6C(CO)14(η6-xylene) and Ru6C(CO)11(η6-xylene)2. Homomolecular crystals of each (denoted A and B) are known, and a heteromolecular cocrystal (C) containing both molecules has been obtained. The central question is whether the cocrystal is energetically competitive with the separate homomolecular crystals, i.e., whether the packing efficiency and cohesive energies of the three crystals are comparable. This task computes the relevant quantities: packing coefficients and packing potential energies.

## Approach
The approach uses the Gavezzotti integration method to compute van der Waals molecular volumes from atomic coordinates, using standard van der Waals radii (C 1.75 Å, O 1.50 Å, H 1.17 Å, Ru 2.35 Å). The packing coefficient is then calculated as pc = V_mol * Z / V_cell. Packing potential energies are estimated by the atom-atom pairwise potential method, summing exp-6 interactions over all atoms with a 15 Å cutoff. Two sets of potential parameters are used: Mirsky (MRK) and Gavezzotti–Filippini (GVF), with ruthenium atoms treated as argon. The computation is performed for each of the three crystals A, B, and C. For crystals with multiple independent molecules in the asymmetric unit, average values are taken where appropriate.

## Reproduction target
Compute, for each crystal (A, B, C), the packing coefficient and the packing potential energy using both the MRK and GVF parameter sets. For crystal C, report the mean packing potential energy over the two independent molecules. The final results must be written to `/app/outputs/results_table.json` as a JSON object with the structure: `{"crystal_A": {"packing_coefficient": <number>, "ppe_MRK": <number>, "ppe_GVF": <number>}, "crystal_B": {...}, "crystal_C": {"packing_coefficient": <number>, "ppe_MRK_mean": <number>, "ppe_GVF_mean": <number>}}`. Use the crystal structures provided as supplementary material (public deposits) and the potential parameter sets (also provided).

## Assets

- Crystal structure of Ru6C(CO)14(xylene) (crystal A)
- Crystal structure of Ru6C(CO)11(xylene)2 (crystal B)
- Crystal structure of the cocrystal C (1 and 2)
- Atom-atom potential parameters (MRK and GVF)

## Workflow steps

### Step 1: Compute molecular volumes
- Role: process
- Action: Using the atomic coordinates from the crystal structures of A, B, C and literature van der Waals radii (C 1.75 Å, O 1.50 Å, H 1.17 Å, Ru 2.35 Å), compute the van der Waals molecular volumes for every independent molecule via the integration method proposed by Gavezzotti. Write the volumes to molecular_volumes.json.
- Evidence: `/app/outputs/molecular_volumes.json`

### Step 2: Compute packing coefficients and packing potential energies
- Role: scored (load-bearing)
- Action: Using the computed molecular volumes and the crystal unit cell parameters (V_cell, Z), compute packing coefficients (pc = V_mol * Z / V_cell) for crystals A, B, C. Then, using the atom-atom pairwise potential method with the MRK and GVF parameter sets (cutoff 15 Å, Ru treated as Ar), compute the packing potential energy (ppe) for each molecule, averaging over independent molecules where applicable. Output all results to results_table.json.
- Output file: `/app/outputs/results_table.json`
- Format: json
- Contract: {"crystal_A": {"packing_coefficient": <number>, "ppe_MRK": <number>, "ppe_GVF": <number>}, "crystal_B": {"packing_coefficient": <number>, "ppe_MRK": <number>, "ppe_GVF": <number>}, "crystal_C": {"packing_coefficient": <number>, "ppe_MRK_mean": <number>, "ppe_GVF_mean": <number>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_table.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_table.json
- path: `/app/outputs/results_table.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Packing coefficient and packing potential energy values for the three crystals A, B, C computed using the given atom-atom potential parameters. The checker compares these to the paper's reference values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `crystal_A`:
      - `packing_coefficient`: number
      - `ppe_MRK`: number (kcal mol⁻¹)
      - `ppe_GVF`: number (kcal mol⁻¹)
    - `crystal_B`:
      - `packing_coefficient`: number
      - `ppe_MRK`: number (kcal mol⁻¹)
      - `ppe_GVF`: number (kcal mol⁻¹)
    - `crystal_C`:
      - `packing_coefficient`: number
      - `ppe_MRK_mean`: number (kcal mol⁻¹)
      - `ppe_GVF_mean`: number (kcal mol⁻¹)

Notes: All needed crystal coordinates and potential parameter files are public. The agent must perform the volume integration and atom–atom summations from scratch. Tolerances are set to accept typical numerical variation from different implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_table.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "crystal_A": {
            "packing_coefficient": "number",
            "ppe_MRK": "number (kcal mol⁻¹)",
            "ppe_GVF": "number (kcal mol⁻¹)"
          },
          "crystal_B": {
            "packing_coefficient": "number",
            "ppe_MRK": "number (kcal mol⁻¹)",
            "ppe_GVF": "number (kcal mol⁻¹)"
          },
          "crystal_C": {
            "packing_coefficient": "number",
            "ppe_MRK_mean": "number (kcal mol⁻¹)",
            "ppe_GVF_mean": "number (kcal mol⁻¹)"
          }
        }
      },
      "description": "Packing coefficient and packing potential energy values for the three crystals A, B, C computed using the given atom-atom potential parameters. The checker compares these to the paper's reference values with appropriate tolerances."
    }
  ],
  "notes": "All needed crystal coordinates and potential parameter files are public. The agent must perform the volume integration and atom–atom summations from scratch. Tolerances are set to accept typical numerical variation from different implementations."
}
```

## How you are scored
A hidden verifier will read your `results_table.json` and compare the reported values to a hidden reference. The comparison uses tolerances large enough to accommodate normal differences between independent implementations, but not so large that a random guess would succeed. You must genuinely run the molecular volume and packing energy computation pipeline; simply copying values from an external source without performing the calculations will not pass. The verifier may also check the ordering of energies among crystals if relevant, but the primary scoring is based on the numerical agreement of the quantities you report.
