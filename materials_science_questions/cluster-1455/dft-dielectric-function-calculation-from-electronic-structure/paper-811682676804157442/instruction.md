# Strain-dependent dielectric constant of hexagonal La2O3 from density functional theory

## Problem background
Rare-earth oxides (e.g., La2O3) are candidate high-κ dielectrics for CMOS applications. Strain engineering is a promising route to tune their physical properties. This task addresses the effect of hydrostatic strain on the static dielectric constant of hexagonal La2O3, a key parameter for gate dielectrics. The goal is to quantify the out-of-plane dielectric response as the lattice constant is varied.

## Approach
Density functional perturbation theory (DFPT) within the local density approximation (LDA) is used to compute the static dielectric tensor of hexagonal La2O3 at several lattice constants, simulating hydrostatic strain. The abinit code with Hartwigsen–Goedecker–Hutter (HGH) pseudopotentials for La and O will be employed. For each strain point, a self-consistent electronic structure calculation is performed followed by a response-function calculation to extract the dielectric tensor. The focus is on the component ε33, the c-axis dielectric constant.

## Reproduction target
Produce a JSON file, epsilon_vs_lattice.json, that maps lattice constant (in Å) to the computed ε33 (dimensionless) for at least five distinct hydrostatic strain values covering a range from below to above the equilibrium lattice constant. The resulting dataset must capture the strain dependence of ε33.

## Assets

- abinit DFT code: https://www.abinit.org/download
- HGH pseudopotentials for La and O
- Hexagonal La2O3 crystal structure data: 10.1006/jssc.1999.XXXX

## Workflow steps

### Step 1: Compute dielectric constant as a function of lattice constant
- Role: scored (load-bearing)
- Action: Set up abinit input files for hexagonal La2O3 at a series of lattice constants (representing hydrostatic strain from below to above the equilibrium value). Run abinit with LDA and HGH pseudopotentials, using response function theory to compute the static dielectric tensor. Parse the output files to extract ε33 (the c-axis component) for each lattice constant. Write a JSON file containing an array of objects with keys 'lattice_constant' (in Angstrom) and 'epsilon_33' (dimensionless).
- Output file: `/app/outputs/epsilon_vs_lattice.json`
- Format: json
- Contract: JSON array of objects. Each object must contain: 'lattice_constant' (float, unit: Angstrom) and 'epsilon_33' (float, dimensionless). Array must have at least 5 entries covering a monotonic series of lattice constants.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/epsilon_vs_lattice.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### epsilon_vs_lattice.json
- path: `/app/outputs/epsilon_vs_lattice.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Dynamic dielectric constant component ε33 along c-axis of hexagonal La2O3 as a function of lattice constant under hydrostatic strain. The checker verifies that epsilon_33 is non-decreasing as lattice_constant increases and performs a few result-level comparisons within tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `lattice_constant`, `epsilon_33`
    - `properties`:
      - `lattice_constant`:
        - `type`: number
        - `unit`: Angstrom
      - `epsilon_33`:
        - `type`: number
        - `unit`: dimensionless

Notes: The absolute values depend on numerical parameters (k‑point grid, cutoff), so monotonicity is the primary scoring criterion. The agent must write the required JSON schema.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "epsilon_vs_lattice.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "lattice_constant",
            "epsilon_33"
          ],
          "properties": {
            "lattice_constant": {
              "type": "number",
              "unit": "Angstrom"
            },
            "epsilon_33": {
              "type": "number",
              "unit": "dimensionless"
            }
          }
        }
      },
      "description": "Dynamic dielectric constant component ε33 along c-axis of hexagonal La2O3 as a function of lattice constant under hydrostatic strain. The checker verifies that epsilon_33 is non-decreasing as lattice_constant increases and performs a few result-level comparisons within tolerance."
    }
  ],
  "notes": "The absolute values depend on numerical parameters (k‑point grid, cutoff), so monotonicity is the primary scoring criterion. The agent must write the required JSON schema."
}
```

## How you are scored
A hidden verifier will validate the JSON structure and may compare the computed ε33 values against a reference dataset. It will also check the internal consistency of the strain evolution. The overall score, between 0 and 1, will reflect how well the submitted results match expected physical trends and reference values. You are not required to reproduce specific published numbers exactly; a correct computation of the strain dependence is what matters.
