# DFT Elastic Constants and Ductility Trends in ZrN-based Ternary Nitrides

## Problem background
Transition metal nitride coatings are widely used for their high hardness and wear resistance. Alloying ZrN with other elements can modify its mechanical properties, particularly ductility. Understanding how different solutes (Ti, Al) affect the elastic constants and the key ductility indicator (the Pugh ratio G/B) is essential for designing better coating materials. This work uses density functional theory (DFT) to compute these trends computationally.

## Approach
We employ first-principles DFT calculations with the generalized gradient approximation (GGA-PBE) to determine the elastic properties of cubic B1 (NaCl) structured ZrN, TiN, AlN, and the ternary alloys Zr0.50Ti0.50N and Zr0.50Al0.50N. The crystal structures are fully relaxed, and the single-crystal elastic tensor components C11, C12, C44 are obtained by applying small homogeneous strains to the relaxed unit cells and fitting the total energy as a function of strain. From these constants, we derive the polycrystalline bulk modulus B, shear modulus G using the Voigt-Reuss-Hill average, Young's modulus E, Poisson's ratio ν, and the Pugh ratio G/B. Comparing the G/B ratios between the ternary alloys and their parent binary compounds provides a measure of relative ductility.

## Reproduction target
Compute the single-crystal elastic constants C11, C12, C44 and the derived polycrystalline moduli B, G, E, ν, and G/B for five compounds: ZrN, TiN, AlN, Zr0.50Ti0.50N, and Zr0.50Al0.50N. Output all results in a single CSV file (`elastic_moduli.csv`) with the columns specified in the output contract. Your computed G/B values will be checked against ordering constraints among the five materials. You do not need to match any specific numerical literature values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT Geometry Optimization
- Role: process
- Action: Optimize the crystal structures of ZrN, TiN, AlN, Zr0.50Ti0.50N, and Zr0.50Al0.50N in the cubic B1 (NaCl) structure using DFT with the GGA-PBE functional. For ternary alloys, construct a 2x2x2 supercell (64 atoms) with the clustered configuration (C#3). Perform full relaxation of lattice parameters and atomic positions until forces and stresses are well converged.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Elastic Constants and Polycrystalline Moduli
- Role: scored (load-bearing)
- Action: From the relaxed structures, compute the elastic tensor components C11, C12, C44 by applying small homogeneous strains and fitting the total energy vs. strain relation. Derive the polycrystalline bulk modulus B, shear modulus G (Voigt-Reuss-Hill average), Young's modulus E, Poisson's ratio nu, and the Pugh ratio G/B. Output all quantities for all five compounds in a single CSV file.
- Output file: `/app/outputs/elastic_moduli.csv`
- Format: csv
- Contract: Columns: compound (string), C11 (GPa, float), C12 (GPa, float), C44 (GPa, float), B (GPa, float), G (GPa, float), E (GPa, float), nu (float), G_over_B (float). Rows: ZrN, TiN, AlN, Zr0.50Ti0.50N, Zr0.50Al0.50N.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli.csv
- path: `/app/outputs/elastic_moduli.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed elastic constants and polycrystalline moduli for ZrN, TiN, AlN, Zr0.50Ti0.50N, Zr0.50Al0.50N. Used to verify ductility trends via structural inequalities on G_over_B.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `C11`, `C12`, `C44`, `B`, `G`, `E`, `nu`, `G_over_B`
  - `column_types`:
    - `compound`: string
    - `C11`: number
    - `C12`: number
    - `C44`: number
    - `B`: number
    - `G`: number
    - `E`: number
    - `nu`: number
    - `G_over_B`: number
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `B`: GPa
    - `G`: GPa
    - `E`: GPa
    - `G_over_B`: dimensionless

Notes: The checker verifies the following inequalities: G_over_B(Zr0.50Ti0.50N) < G_over_B(ZrN) and < G_over_B(TiN); G_over_B(Zr0.50Al0.50N) < G_over_B(ZrN) and < G_over_B(AlN). No tolerance on absolute values; only the relative ordering is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "C11",
          "C12",
          "C44",
          "B",
          "G",
          "E",
          "nu",
          "G_over_B"
        ],
        "column_types": {
          "compound": "string",
          "C11": "number",
          "C12": "number",
          "C44": "number",
          "B": "number",
          "G": "number",
          "E": "number",
          "nu": "number",
          "G_over_B": "number"
        },
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "B": "GPa",
          "G": "GPa",
          "E": "GPa",
          "G_over_B": "dimensionless"
        }
      },
      "description": "Computed elastic constants and polycrystalline moduli for ZrN, TiN, AlN, Zr0.50Ti0.50N, Zr0.50Al0.50N. Used to verify ductility trends via structural inequalities on G_over_B."
    }
  ],
  "notes": "The checker verifies the following inequalities: G_over_B(Zr0.50Ti0.50N) < G_over_B(ZrN) and < G_over_B(TiN); G_over_B(Zr0.50Al0.50N) < G_over_B(ZrN) and < G_over_B(AlN). No tolerance on absolute values; only the relative ordering is required."
}
```

## How you are scored
A hidden verifier reads your `elastic_moduli.csv` and checks that the G_over_B values satisfy a set of ordering relationships among the five compounds. The verifier also validates that the output file conforms to the required format and columns. Scoring is based on the proportion of the structural ordering checks that hold; no comparison to absolute target values is performed. You are not required to reproduce any specific numerical results from prior work.
