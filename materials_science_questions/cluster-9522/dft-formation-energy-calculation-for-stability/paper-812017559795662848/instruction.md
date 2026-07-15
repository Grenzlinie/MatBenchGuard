# CEF Site Fraction Modelling of Partially Ordered Solid Solution

## Problem background
The compound of interest crystallizes in the Sm5Ge4-type structure (space group Pnma) with three distinct metal sites. When a fraction of the primary metal atoms is replaced by a second metal, the substitution exhibits a strong site preference: the second metal does not distribute randomly but favors specific sites over others. Understanding this preference is important for predicting structural and thermodynamic properties of the solid solution. This task focuses on modelling the equilibrium distribution of the substituting element across the three sites as a function of overall composition, using a thermodynamic model built on ab initio total-energy calculations.

## Approach
The Compound Energy Formalism (CEF) provides a framework for the Gibbs energy of phases with multiple sublattices. Here a three-sublattice model for the metal sites (I, II, III) is used, together with a stoichiometric fourth sublattice (Ge). The Gibbs energy per formula unit is written as a sum over the eight end-member energies (each representing a specific arrangement of the two metal species on the three sublattices) weighted by products of site fractions, plus the ideal configurational entropy; no excess energy of mixing is included. Two sets of end-member substitution energies (derived from ab initio DFT) are provided as fixed input parameters. At a fixed temperature and for a given overall composition, the equilibrium site fractions are obtained by minimizing the Gibbs energy with respect to the site fractions, subject to normalization of each sublattice and the mass-balance constraint linking composition to site fractions. The task is to perform this minimization at T = 1673 K for a series of composition index values x (0 ≤ x ≤ 3.8) using each energy set, and to tabulate the resulting site fractions for sublattices I, II, and III.

## Reproduction target
Compute the equilibrium site fractions of the substituting element on sublattices I, II, and III as a function of the composition index x (0 ≤ x ≤ 3.8) at T = 1673 K, using the two end-member energy sets (Set A and Set B) described in the workflow steps. For each set, produce a CSV file containing columns: x, y_Nb_I, y_Nb_II, y_Nb_III. Evaluate at 10–20 evenly spaced x values covering the full range. The two output files are the primary deliverables that will be evaluated.

## Assets

- pycalphad: pycalphad
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: CEF site fractions – Set A
- Role: scored (load-bearing)
- Action: Using the Compound Energy Formalism (CEF) sublattice model (Hf,Nb)1(Hf,Nb)2(Hf,Nb)2Ge4 and the end-member substitution energies of Set A given below, compute the equilibrium Nb site fractions for the three sublattices (I=Hf1, II=Hf2, III=Hf3) as a function of composition index x at T=1673 K. The Gibbs energy expression is the sum over the eight end-member energies weighted by site-fraction products plus the configurational entropy term (no excess Gibbs energy). The site fractions must be obtained by minimising the Gibbs energy subject to the normalisation and mass-balance constraints. End-member energies (Set A, kJ/mol, relative to Hf5Ge4): (Hf:Hf:Hf:Ge)=0.00, (Nb:Hf:Hf:Ge)=0.14, (Hf:Nb:Hf:Ge)=5.22, (Hf:Hf:Nb:Ge)=18.18, (Nb:Nb:Hf:Ge)=8.00, (Nb:Hf:Nb:Ge)=19.58, (Hf:Nb:Nb:Ge)=27.08, (Nb:Nb:Nb:Ge)=30.54. Evaluate at 10–20 evenly spaced x values between 0 and 3.8 (inclusive). Output the results to /app/outputs/site_fractions_setA.csv.
- Output file: `/app/outputs/site_fractions_setA.csv`
- Format: csv
- Contract: CSV file with columns: x (float, composition index), y_Nb_I (float), y_Nb_II (float), y_Nb_III (float). One row per x point.
- Scoring: scored by hidden verifier

### Step 2: CEF site fractions – Set B
- Role: scored (load-bearing)
- Action: Repeat the CEF calculation using the simplified end-member energy Set B (kJ/mol): (Hf:Hf:Hf:Ge)=0.00, (Nb:Hf:Hf:Ge)=0.41, (Hf:Nb:Hf:Ge)=6.70, (Hf:Hf:Nb:Ge)=18.18, (Nb:Nb:Hf:Ge)=7.11, (Nb:Hf:Nb:Ge)=18.59, (Hf:Nb:Nb:Ge)=24.88, (Nb:Nb:Nb:Ge)=25.29. All other parameters (sublattice model, temperature, composition range) are identical to Set A. Output the results to /app/outputs/site_fractions_setB.csv.
- Output file: `/app/outputs/site_fractions_setB.csv`
- Format: csv
- Contract: CSV file with columns: x (float), y_Nb_I (float), y_Nb_II (float), y_Nb_III (float). One row per x point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/site_fractions_setA.csv`
- `/app/outputs/site_fractions_setB.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### site_fractions_setA.csv
- path: `/app/outputs/site_fractions_setA.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium Nb site fractions on sublattices I, II, III computed using end-member energy Set A at T=1673 K.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y_Nb_I`, `y_Nb_II`, `y_Nb_III`
  - `units`:
    - `x`: dimensionless composition index
    - `y_Nb_I`: site fraction
    - `y_Nb_II`: site fraction
    - `y_Nb_III`: site fraction

### site_fractions_setB.csv
- path: `/app/outputs/site_fractions_setB.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium Nb site fractions on sublattices I, II, III computed using end-member energy Set B at T=1673 K.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y_Nb_I`, `y_Nb_II`, `y_Nb_III`
  - `units`:
    - `x`: dimensionless composition index
    - `y_Nb_I`: site fraction
    - `y_Nb_II`: site fraction
    - `y_Nb_III`: site fraction

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "site_fractions_setA.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y_Nb_I",
          "y_Nb_II",
          "y_Nb_III"
        ],
        "units": {
          "x": "dimensionless composition index",
          "y_Nb_I": "site fraction",
          "y_Nb_II": "site fraction",
          "y_Nb_III": "site fraction"
        }
      },
      "description": "Equilibrium Nb site fractions on sublattices I, II, III computed using end-member energy Set A at T=1673 K."
    },
    {
      "file": "site_fractions_setB.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y_Nb_I",
          "y_Nb_II",
          "y_Nb_III"
        ],
        "units": {
          "x": "dimensionless composition index",
          "y_Nb_I": "site fraction",
          "y_Nb_II": "site fraction",
          "y_Nb_III": "site fraction"
        }
      },
      "description": "Equilibrium Nb site fractions on sublattices I, II, III computed using end-member energy Set B at T=1673 K."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently implements the same CEF model with the same end-member energies and temperature. For each output file (Set A and Set B), the verifier recomputes the equilibrium site fractions and compares them to your reported values. The overall score reflects how well your site fractions agree with those obtained from a correct implementation of the model. Simply providing a set of numbers without performing the CEF minimization will not succeed, because the verifier's reference values are generated from the model equations and the given input parameters, not from a static lookup table.
