# Classical Electrostatic Calculation of K+ Complex Binding Energies

## Problem background
The binding energies of potassium ion complexes with small molecules are of interest for understanding gas-phase ion chemistry. One approach to investigate the nature of the bonding is to perform classical electrostatic calculations and compare the results with experimental measurements. This task reproduces a classical electrostatic calculation used to analyze the binding of K+ to a series of nitrogen and oxygen bases: H2O, NH3, CH3NH2, (CH3)2NH, and (CH3)3N. The goal is to compute the total stabilization energy and its components from the electrostatic model and report the equilibrium ion–molecule distances.

## Approach
The total stabilization energy E_t of a K+·M complex at a given ion–molecule distance R is computed as the sum of four contributions: permanent dipole attraction (E_dip), induced dipole attraction (E_ind), London dispersion (E_dis), and Born-Mayer repulsion (E_rep).

E_dip is evaluated by summing the Coulomb potentials between the K+ ion and net atomic charges Q_i on the atoms i of molecule M. The net atomic charges are taken from published Mulliken population analyses and scaled to match experimental dipole moments.

E_ind is computed from a sum over atom contributions using atomic polarizabilities.

E_dis is obtained from a modified London formula that depends on the molecular polarizabilities of M and K+ and their ionization potentials (multiplied by 2.5).

E_rep is a sum of Born-Mayer repulsive terms with parameters derived from scattering data.

All parameter values (atomic coordinates, charges, polarizabilities, ionization potentials, repulsive C and a constants) are obtained from openly published literature. The equilibrium binding energy is found by minimizing E_t with respect to the K+–O (for H2O) or K+–N distance R.

## Reproduction target
Compute the equilibrium ion–molecule distance R (Å) and the four energy components E_dip, E_ind, E_dis, E_rep, and the total stabilization energy E_t (all in kcal/mol) for the five K+·M complexes: M = H2O, NH3, CH3NH2, (CH3)2NH, (CH3)3N. Save the results in the CSV file step_01_electrostatic_results.csv as specified in the workflow steps.

## Assets

- Hehre and Pople (1970) Mulliken populations for H2O, NH3, CH3NH2, (CH3)2NH, (CH3)3N: https://doi.org/10.1021/ja00710a005
- Almenningen and Bastiansen (1955) molecular geometries for methylamines: https://doi.org/10.3891/acta.chem.scand.09-0815
- Nishikawa et al. (1955) molecular geometries for H2O, NH3: https://doi.org/10.1063/1.1741968
- Amdur et al. (1973) repulsive potential parameters for K+–atom interactions: https://doi.org/10.1063/1.1680603
- Le Fevre and Russel (1967) molecular polarizabilities for methylamines: https://doi.org/10.1039/tf9676300374
- Experimental dipole moments of H2O, NH3, methylamines
- Python scientific stack (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Assemble and scale input parameters
- Role: process
- Action: Obtain net atomic charges Q_i from the Mulliken populations of Hehre and Pople (1970) for H2O, NH3, and the three methylamines; scale them by the factor required to match the experimental dipole moments of each molecule (a factor of 1.6 is suggested). Gather molecular geometries (bond lengths, angles) from Almenningen & Bastiansen and Nishikawa et al. Collect atomic polarizabilities (α_N=0.98, α_C=1, α_H=0.44 Å³), molecular polarizabilities, ionization potentials (I_M, I_K+), and the repulsive parameters C_K+-i and a_K+-i from Amdur (1973) following Eliezer & Krindel. Multiply ionization potentials by 2.5.
- Evidence: none

### Step 2: Classical electrostatic energy minimization and results
- Role: scored (load-bearing)
- Action: For each molecule M (H2O, NH3, CH3NH2, (CH3)2NH, (CH3)3N), compute the total stabilization energy as E_t = E_dip + E_ind + E_dis + E_rep using the electrostatic formulas (permanent dipole, induced dipole, London dispersion, Born-Mayer repulsion). Minimize E_t with respect to the K+–O (for H2O) or K+–N distance R. Report the equilibrium distance R (Å) and the four energy components and total energy (all in kcal/mol).
- Output file: `/app/outputs/step_01_electrostatic_results.csv`
- Format: csv
- Contract: Columns: molecule (str), R_ion_N (float, Å), E_dip (float, kcal/mol), E_ind (float, kcal/mol), E_dis (float, kcal/mol), E_rep (float, kcal/mol), E_t (float, kcal/mol). One row per molecule (H2O, NH3, CH3NH2, (CH3)2NH, (CH3)3N).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_electrostatic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_electrostatic_results.csv
- path: `/app/outputs/step_01_electrostatic_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium ion–molecule distances and energy components (permanent dipole, induced dipole, London dispersion, repulsion) and total stabilization energy for the five K+·M complexes (M = H2O, NH3, CH3NH2, (CH3)2NH, (CH3)3N).
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `R_ion_N`, `E_dip`, `E_ind`, `E_dis`, `E_rep`, `E_t`
  - `units`:
    - `R_ion_N`: angstrom
    - `E_dip`: kcal/mol
    - `E_ind`: kcal/mol
    - `E_dis`: kcal/mol
    - `E_rep`: kcal/mol
    - `E_t`: kcal/mol

Notes: The checker will verify that the reported E_t values match the hidden gold values within the required tolerance and that E_dip+E_ind+E_dis+E_rep equals E_t for each row (internal consistency).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_electrostatic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "R_ion_N",
          "E_dip",
          "E_ind",
          "E_dis",
          "E_rep",
          "E_t"
        ],
        "units": {
          "R_ion_N": "angstrom",
          "E_dip": "kcal/mol",
          "E_ind": "kcal/mol",
          "E_dis": "kcal/mol",
          "E_rep": "kcal/mol",
          "E_t": "kcal/mol"
        }
      },
      "description": "Computed equilibrium ion–molecule distances and energy components (permanent dipole, induced dipole, London dispersion, repulsion) and total stabilization energy for the five K+·M complexes (M = H2O, NH3, CH3NH2, (CH3)2NH, (CH3)3N)."
    }
  ],
  "notes": "The checker will verify that the reported E_t values match the hidden gold values within the required tolerance and that E_dip+E_ind+E_dis+E_rep equals E_t for each row (internal consistency)."
}
```

## How you are scored
Your CSV output is evaluated by a hidden verifier. The verifier compares your reported total stabilization energies for each molecule to the expected reference values. It also checks that the sum of the four component energies (E_dip + E_ind + E_dis + E_rep) equals the total energy E_t for each row within a tight tolerance (internal consistency). The verifier may also compare the equilibrium distances against expected values. Full credit requires accurate computation of the energies; reporting literature values without performing the actual electrostatic minimization will not be rewarded.
