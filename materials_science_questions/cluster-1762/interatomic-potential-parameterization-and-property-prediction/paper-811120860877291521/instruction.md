# Compute Madelung Potentials for Orthophosphates

## Problem background
X-ray photoelectron spectroscopy (XPS) binding energies of core electrons in solids are influenced by the electrostatic potential from the surrounding ions (the Madelung potential) as well as by final-state relaxation. For phosphorus in orthophosphates, the near-neighbor environment is a PO₄ tetrahedron, and the primary chemical variation comes from the identity and arrangement of the counter-cations. Understanding how the Madelung potential at the phosphorus site depends on the structural parameters and bond ionicities of these compounds is important for interpreting core-level shifts. This task computes the ionicity-corrected Madelung potential at the phosphorus atom for a series of orthophosphate compounds using a semi-empirical model.

## Approach
The ionicity-corrected Madelung potential V_M(P) (in eV) for each compound is computed using the following procedure.

**Constants**
- Vacuum permittivity factor: e²/(4πε₀) = 14.4 eV·Å (when distances are given in Å; 1 Å = 0.1 nm)
- P–O bond distance r_PO = 1.54 Å (0.154 nm)
- Charge transferred from phosphorus to oxygen per bond: q_O = 1.28 (electron units)

**Formula**
V_M(P) = – (14.4 / r_PO) × (1.28 + 3 I)  +  (14.4 × l × (1.89 – 1/N_A) × z / r_AP) × I

where:
- I is the A–PO₄ bond ionicity (provided below for each compound),
- l is the number of A cations in the formula unit,
- z is the largest common factor of the formal charges of cation A and the phosphate group (e.g., for Na⁺ and PO₄³⁻, z = 1; for In³⁺ and PO₄³⁻, z = 3),
- N_A is the effective coordination number of the cation,
- r_AP is the average A–P distance (in Å).

All parameters for each compound are given in the section "Provided Parameters".

## Reproduction target
For the orthophosphate compounds Na₃PO₄, Ca₃(PO₄)₂, Mn₃(PO₄)₂, Ni₃(PO₄)₂, InPO₄, FePO₄, GaPO₄, and BPO₄, compute the ionicity‑corrected Madelung potential V_M(P) (in eV) using the structural parameters provided. The output must be a JSON file containing an array of objects, each with the compound name and its computed V_M. The goal is to obtain a consistent set of potentials that reflect the structural and bonding differences across the series.

## Assets

- Python with numpy: Installable via pip: python3 -m pip install numpy

## Provided Parameters
The following table gives the necessary input data for each orthophosphate compound.

| Compound      | l | z | r_AP (Å) | N_A  | I     |
|---------------|---|---|----------|------|-------|
| Na3PO4       | 3 | 1 | 3.29     | 4.0  | 0.71  |
| Ca3(PO4)2    | 3 | 1 | 3.40     | 5.0  | 0.68  |
| Mn3(PO4)2    | 3 | 1 | 3.24     | 5.0  | 0.47  |
| Ni3(PO4)2    | 3 | 1 | 3.06     | 4.66 | 0.31  |
| InPO4        | 1 | 3 | 3.32     | 6    | 0.37  |
| FePO4        | 1 | 3 | 3.16     | 4    | 0.29  |
| GaPO4        | 1 | 3 | 3.09     | 4    | 0.36  |
| BPO4         | 1 | 3 | 2.73     | 4    | 0.26  |

All parameters are taken from the structural analysis of the phosphates. Use the provided values directly in the V_M formula.

## Workflow steps

### Step 1: Compute Madelung Potentials for Orthophosphates
- Role: scored (load-bearing)
- Action: For each compound listed in "Provided Parameters", use the corresponding values of l, z, r_AP, N_A, and the bond ionicity I. Plug these into the V_M formula given in the Approach section to compute the ionicity-corrected Madelung potential V_M. Write the results to a JSON file.
- Output file: `/app/outputs/madelung_potentials.json`
- Format: json
- Contract: A JSON array of objects, each with 'compound' (string) and 'V_M' (float, electronvolts). Example: [{"compound": "Na3PO4", "V_M": -16.75}, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/madelung_potentials.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### madelung_potentials.json
- path: `/app/outputs/madelung_potentials.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed ionicity-corrected Madelung potentials for eight orthophosphate compounds. The verifier compares each compound's V_M against a hidden reference value and assesses the relative ordering across compounds.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `V_M`
    - `properties`:
      - `compound`:
        - `type`: string
      - `V_M`:
        - `type`: number
        - `unit`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "madelung_potentials.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "V_M"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "V_M": {
              "type": "number",
              "unit": "eV"
            }
          }
        }
      },
      "description": "Computed ionicity-corrected Madelung potentials for eight orthophosphate compounds. The verifier compares each compound's V_M against a hidden reference value and assesses the relative ordering across compounds."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your output file and evaluate two aspects: (i) per‑compound agreement: each computed V_M is compared to a hidden reference value within a tolerance; (ii) trend consistency: the relative ordering of V_M values across compounds is compared to a reference ordering. The final score is a weighted combination of the fraction of compounds meeting the tolerance and the fraction of correctly ordered pairs. Do not attempt to match pre‑known numbers; the evaluation rewards physically meaningful potentials that reflect the provided structural parameters.
