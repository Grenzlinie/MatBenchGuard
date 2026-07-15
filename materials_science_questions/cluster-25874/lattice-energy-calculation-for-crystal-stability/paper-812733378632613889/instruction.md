# Atom–Atom Buckingham Potential Energy Calculations for Mn₂(CO)₁₀

## Problem background
Transition metal carbonyl clusters, such as Mn₂(CO)₁₀, exhibit specific molecular conformations and crystal packing motifs. Understanding why a particular geometry is adopted in the solid state requires disentangling three contributions: the strong metal–ligand and metal–metal bonds, the non-bonded interactions between ligands within the same molecule, and the intermolecular packing forces that organise molecules in the crystal. A simple atom–atom potential model can quantify these ligand–ligand and ligand–environment interactions and thus help assess whether intramolecular attraction/repulsion or crystal packing dominates the observed structure.

## Approach
Non-bonded interactions are captured by a pairwise Buckingham potential of the form A exp(−B r) − C r⁻⁶, where r is the interatomic distance and the parameters A, B, C depend on the atom types (O–O, O–C, C–C, and noble-gas–O with the metal approximated by the corresponding noble gas). The calculation is performed on the experimental room-temperature crystal structure of Mn₂(CO)₁₀. For the intramolecular non-bonded energy (IAM), all atom pairs within a single reference molecule are considered, excluding nearest-neighbour 1–3 contacts. The total is partitioned into O–O, O–C, C–C repulsive, C–C attractive, and metal–O contributions. For the intermolecular packing energy (IEM), crystal symmetry is used to generate surrounding molecules, and the interaction energy between the reference molecule and every molecule whose atoms fall within a 10 Å cutoff is summed. The goal is to implement this protocol, compute the partitioned IAM and the total IEM, and output the results as plain CSV files.

## Reproduction target
Given the room-temperature crystal structure of Mn₂(CO)₁₀ (CSD refcode MNCO10), implement the Buckingham potential using the atom-pair parameters specified in the assets below. Compute: (1) the intramolecular non-bonded energy components O–O, O–C, C–C repulsive, C–C attractive, and M–O (in kcal/mol); and (2) the total intermolecular packing energy (in kcal/mol). Write these results to the designated CSV files. The target is to produce these quantities by re‑running the computational procedure; do not simply transcribe literature values.

## Assets

- Cambridge Structural Database (CSD) – Mn₂(CO)₁₀ room temperature structure (refcode MNCO10): MNCO10

## Workflow steps

### Step 1: Obtain crystal structure of Mn₂(CO)₁₀ (room temperature)
- Role: process
- Action: Retrieve the atomic coordinates, unit cell parameters, and space group for room-temperature Mn₂(CO)₁₀ from the Cambridge Structural Database (CSD) using refcode MNCO10. Save the structure as a CIF file for later steps.
- Evidence: `/app/outputs/mn2co10_rt.cif`

### Step 2: Compute intramolecular non-bonded energies (IAM)
- Role: scored (load-bearing)
- Action: Using the room-temperature structure from Step 1, implement the Buckingham pair potential sum over atom pairs: A*exp(-B*r) - C*r^{-6} with the atom-pair parameters for O-O, O-C, C-C, and Kr-Kr/Kr-O as reported in the paper (A in kcal/mol, B in Å^{-1}, C in kcal/mol). Compute all intra-reference-molecule non-bonded atom–atom pairs, excluding nearest-neighbour 1–3 contacts. Partition the total into O–O, O–C, C–C repulsive, C–C attractive, and M–O contributions (using Kr as proxy for Mn) and output these five values in kcal/mol to a CSV file.
- Output file: `/app/outputs/iam_breakdown.csv`
- Format: csv
- Contract: Columns: OO, OC, CC_rep, CC_attr, MO (all floats, kcal/mol)
- Scoring: scored by hidden verifier

### Step 3: Compute intermolecular packing energy (IEM)
- Role: scored (load-bearing)
- Action: Using the same Buckingham potential and the crystal structure, generate all symmetry-equivalent molecules in the unit cell. Sum the intermolecular atom–atom interactions between a chosen reference molecule and all surrounding molecules whose atoms lie within a 10 Å cutoff of the reference molecule. Output the total intermolecular energy in kcal/mol as a single value in a CSV file.
- Output file: `/app/outputs/iem_total.csv`
- Format: csv
- Contract: Column: IEM_total (float, kcal/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/iam_breakdown.csv`
- `/app/outputs/iem_total.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### iam_breakdown.csv
- path: `/app/outputs/iam_breakdown.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Partitioned intramolecular non-bonded energies for Mn₂(CO)₁₀ and Fe₃(CO)₁₂ room-temperature structures.
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `OO`, `OC`, `CC_rep`, `CC_attr`, `MO`
  - `units`:
    - `OO`: kcal/mol
    - `OC`: kcal/mol
    - `CC_rep`: kcal/mol
    - `CC_attr`: kcal/mol
    - `MO`: kcal/mol

### iem_total.csv
- path: `/app/outputs/iem_total.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total intermolecular packing energy for Mn₂(CO)₁₀ and Fe₃(CO)₁₂ room-temperature structures.
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `IEM_total`
  - `units`:
    - `IEM_total`: kcal/mol

Notes: The checker compares submitted values to hidden reference values (paper-reported energies) with tolerances. The agent must reimplement the Buckingham potential and crystal symmetry handling; the OPEC program is not required. Additional clusters (Fe₂(CO)₉, Co₂(CO)₈, Ru₃(CO)₁₂, Ir₆(CO)₁₆) are excluded because their IAM breakdowns are not directly comparable (missing repulsive C–C components) or require more complex structural handling (bridging ligands, isomer separation) that would add disproportionate complexity without changing the core reproduction method; Mn₂(CO)₁₀ and Fe₃(CO)₁₂ are representative.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "iam_breakdown.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "OO",
          "OC",
          "CC_rep",
          "CC_attr",
          "MO"
        ],
        "units": {
          "OO": "kcal/mol",
          "OC": "kcal/mol",
          "CC_rep": "kcal/mol",
          "CC_attr": "kcal/mol",
          "MO": "kcal/mol"
        }
      },
      "description": "Partitioned intramolecular non-bonded energies for Mn₂(CO)₁₀ and Fe₃(CO)₁₂ room-temperature structures."
    },
    {
      "file": "iem_total.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "IEM_total"
        ],
        "units": {
          "IEM_total": "kcal/mol"
        }
      },
      "description": "Total intermolecular packing energy for Mn₂(CO)₁₀ and Fe₃(CO)₁₂ room-temperature structures."
    }
  ],
  "notes": "The checker compares submitted values to hidden reference values (paper-reported energies) with tolerances. The agent must reimplement the Buckingham potential and crystal symmetry handling; the OPEC program is not required. Additional clusters (Fe₂(CO)₉, Co₂(CO)₈, Ru₃(CO)₁₂, Ir₆(CO)₁₆) are excluded because their IAM breakdowns are not directly comparable (missing repulsive C–C components) or require more complex structural handling (bridging ligands, isomer separation) that would add disproportionate complexity without changing the core reproduction method; Mn₂(CO)₁₀ and Fe₃(CO)₁₂ are representative."
}
```

## How you are scored
A hidden verifier independently checks each of your two output files. For the IAM breakdown, every component is compared against a hidden reference derived from the original work. For the IEM total, the single number is similarly compared. Comparisons use a tolerance that accounts for minor numerical differences between independent implementations; values within tolerance receive full credit for that part. The overall reward is a weighted sum: the IAM components contribute 60% of the final score, and the IEM total contributes 40%. Simply submitting the benchmark numbers without authentic computation will not pass the verifier’s checks.
