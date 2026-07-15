# Grand Canonical Monte Carlo Hydrogen Adsorption Simulation in Co-MIL-88A

## Problem background
Hydrogen storage in metal-organic frameworks (MOFs) is a promising route for clean energy carriers, but achieving high gravimetric capacity at ambient temperature remains challenging. MIL-88A is a flexible MOF with unsaturated metal sites that can enhance gas adsorption. When the metal is cobalt (Co-MIL-88A), the coordinatively unsaturated Co sites may provide strong binding for H2 molecules. The central open question is: what are the favorable H2 adsorption sites in Co-MIL-88A, what binding energies does H2 exhibit at these sites, and what gravimetric hydrogen uptake can be achieved under cryogenic (77 K) and ambient (298 K) conditions up to 100 bar?

## Approach
This reproduction uses a combined density functional theory (DFT) and grand canonical Monte Carlo (GCMC) approach. The Co-MIL-88A structure is constructed by replacing Fe with Co in the known Fe-MIL-88A crystal structure. DFT geometry optimization is performed with the revPBE+vdW-DF dispersion-corrected functional to obtain the equilibrium unit cell. H2 molecules are then placed at four candidate adsorption sites — hollow, ligand, metal side-on, and metal end-on — and the adsorption energy for each site is computed via DFT relaxations of H2 while the framework is kept fixed. DDEC atomic point charges are derived from the DFT electron density of the optimized framework. Using these charges and generic MOF Lennard-Jones parameters, GCMC simulations are run with RASPA to compute hydrogen adsorption isotherms at 77 K and 298 K for pressures up to 100 bar. The electrostatic contribution is isolated by repeating the 77 K simulation without Coulomb interactions, enabling separation of the dispersion and electrostatic parts of the absolute uptake.

## Reproduction target
The task is to reproduce the following quantities for Co-MIL-88A: (1) DFT-computed adsorption energies for the four distinct H2 binding sites (hollow, ligand, metal side-on, metal end-on), stored in binding_energies.csv; (2) GCMC-computed excess and absolute gravimetric H2 loadings (wt%) at 77 K for pressures up to 100 bar, stored in isotherms_77K.csv; (3) the same at 298 K, stored in isotherms_298K.csv; (4) the decomposition of the absolute 77 K loading into Lennard-Jones and Coulomb contributions and the resulting electrostatic percentage, stored in electrostatic_contrib_77K.csv. The required columns and formatting are defined in the workflow steps.

## Assets

- Open-source DFT code: https://www.quantum-espresso.org
- DDEC charge analysis software: https://sourceforge.net/projects/ddec/
- Fe-MIL-88A crystal structure: 10.1039/b516776d
- RASPA molecular simulation package: https://github.com/piemmel/RASPA2

## Workflow steps

### Step 1: Geometry optimization of Co-MIL-88A
- Role: process
- Action: Construct the Co-MIL-88A unit cell by replacing Fe with Co in the Fe-MIL-88A crystal structure obtained from the public resource. Perform DFT geometry optimization (variable-cell relaxation) using the revPBE+vdW-DF functional to determine the optimized lattice parameters and atomic positions.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 2: H2 adsorption energies
- Role: scored
- Action: Place H2 molecule at the four sites (hollow, ligand, metal side-on, metal end-on) on the optimized Co-MIL-88A structure; perform DFT geometry relaxations (H2 coordinates relaxed, framework fixed) using revPBE+vdW-DF. Compute the adsorption energy for each site using E_ads = E(MOF+H2) – (E(MOF) + E(H2)). Save the binding energies (E_ads) as negative values to the output file.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: columns: site (string), E_ads_kJmol (float)
- Scoring: scored by hidden verifier

### Step 3: DDEC charge calculation
- Role: process
- Action: Using the DFT electron density of the optimized Co-MIL-88A framework, compute DDEC net atomic charges for all atom types. Save the charge assignments to a file for GCMC input.
- Evidence: `/app/outputs/ddec_charges.csv`

### Step 4: H2 adsorption isotherm at 77 K
- Role: scored (load-bearing)
- Action: Run GCMC simulations using RASPA for Co-MIL-88A at 77 K with the full Lennard-Jones plus Coulomb potential (using the DDEC charges and LJ parameters from the generic MOF force field). Compute absolute and excess gravimetric H2 loadings (wt%) for pressures up to 100 bar and save the isotherm data.
- Output file: `/app/outputs/isotherms_77K.csv`
- Format: csv
- Contract: columns: pressure_bar (float), exc_wt (float), abs_wt (float)
- Scoring: scored by hidden verifier

### Step 5: H2 adsorption isotherm at 298 K
- Role: scored
- Action: Run GCMC simulations using RASPA for Co-MIL-88A at 298 K with the full potential and save absolute and excess H2 loadings.
- Output file: `/app/outputs/isotherms_298K.csv`
- Format: csv
- Contract: columns: pressure_bar (float), exc_wt (float), abs_wt (float)
- Scoring: scored by hidden verifier

### Step 6: Electrostatic contribution at 77 K
- Role: scored
- Action: Run GCMC simulations using RASPA for Co-MIL-88A at 77 K without electrostatic interactions (LJ only). Using the absolute loadings from the LJ-only run and from the full-potential 77 K run, compute the electrostatic contribution (difference) and its percentage for each pressure. Save the table.
- Output file: `/app/outputs/electrostatic_contrib_77K.csv`
- Format: csv
- Contract: columns: pressure_bar (float), abs_wt_LJplusCoulomb (float), abs_wt_LJonly (float), coulomb_wt (float), electrostatic_pct (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/isotherms_77K.csv`
- `/app/outputs/isotherms_298K.csv`
- `/app/outputs/electrostatic_contrib_77K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: DFT-calculated H2 adsorption energies for the four sites: hollow, ligand, metal side-on, metal end-on. Used to verify site ordering and energy values.
- schema:
  - `type`: table
  - `required_columns`: `site`, `E_ads_kJmol`

### isotherms_77K.csv
- path: `/app/outputs/isotherms_77K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: GCMC-computed H2 excess and absolute gravimetric loadings at 77 K for pressures up to 100 bar.
- schema:
  - `type`: table
  - `required_columns`: `pressure_bar`, `exc_wt`, `abs_wt`

### isotherms_298K.csv
- path: `/app/outputs/isotherms_298K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: GCMC-computed H2 excess and absolute gravimetric loadings at 298 K for pressures up to 100 bar.
- schema:
  - `type`: table
  - `required_columns`: `pressure_bar`, `exc_wt`, `abs_wt`

### electrostatic_contrib_77K.csv
- path: `/app/outputs/electrostatic_contrib_77K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electrostatic contribution to absolute H2 uptake at 77 K, separated by comparing full-potential and LJ-only GCMC simulations.
- schema:
  - `type`: table
  - `required_columns`: `pressure_bar`, `abs_wt_LJplusCoulomb`, `abs_wt_LJonly`, `coulomb_wt`, `electrostatic_pct`

Notes: All outputs are tabular CSV files. The checker compares numerical values against reference data with tolerances and validates the ordering of binding energies. Target policy is reference_match for each file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "E_ads_kJmol"
        ]
      },
      "description": "DFT-calculated H2 adsorption energies for the four sites: hollow, ligand, metal side-on, metal end-on. Used to verify site ordering and energy values."
    },
    {
      "file": "isotherms_77K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_bar",
          "exc_wt",
          "abs_wt"
        ]
      },
      "description": "GCMC-computed H2 excess and absolute gravimetric loadings at 77 K for pressures up to 100 bar."
    },
    {
      "file": "isotherms_298K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_bar",
          "exc_wt",
          "abs_wt"
        ]
      },
      "description": "GCMC-computed H2 excess and absolute gravimetric loadings at 298 K for pressures up to 100 bar."
    },
    {
      "file": "electrostatic_contrib_77K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_bar",
          "abs_wt_LJplusCoulomb",
          "abs_wt_LJonly",
          "coulomb_wt",
          "electrostatic_pct"
        ]
      },
      "description": "Electrostatic contribution to absolute H2 uptake at 77 K, separated by comparing full-potential and LJ-only GCMC simulations."
    }
  ],
  "notes": "All outputs are tabular CSV files. The checker compares numerical values against reference data with tolerances and validates the ordering of binding energies. Target policy is reference_match for each file."
}
```

## How you are scored
Your submission will be evaluated by a hidden automatic verifier. The verifier independently scores each scored artifact (binding_energies.csv, isotherms_77K.csv, isotherms_298K.csv, electrostatic_contrib_77K.csv) by comparing your computed numerical results against a hidden reference with appropriate tolerances, and may also check structural consistency (e.g., the ordering of site binding energies and the pressure dependence of the electrostatic contribution). Each artifact is assigned a weight, and the verifier combines the individual scores into a final reward between 0 and 1. Reporting values that match the hidden reference yields high reward; arbitrary or incorrect results score low.
