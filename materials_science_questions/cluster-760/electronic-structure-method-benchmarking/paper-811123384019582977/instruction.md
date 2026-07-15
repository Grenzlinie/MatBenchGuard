# Semi-empirical CNDO/2 prediction of spin–orbit splittings in linear molecules

## Problem background
Semi-empirical molecular orbital methods offer a practical route to estimate spin–orbit splittings in degenerate electronic states, aiding the assignment of photoelectron spectra. This task investigates a method that uses CNDO/2 wavefunctions together with effective atomic coupling constants to predict splittings for linear polyatomic molecules. Two calculation procedures are considered: one based on an open‑shell CNDO/2 calculation of the degenerate state, and one based on a simpler closed‑shell calculation followed by a correction for the missing electron. The quality of these predictions is of interest for interpreting experimental spectra, especially for molecules containing first- and second-row elements and halogens.

## Approach
The method relies on standard CNDO/2 semi‑empirical calculations. For each molecule, experimental equilibrium bond lengths (obtained from the CCCBDB database) are used to run both a restricted closed‑shell calculation and, where applicable, an unrestricted open‑shell calculation on the ²Π state. From these calculations, the molecular orbital coefficients and charge‑density matrices are extracted, and net atomic charges are computed.

The spin–orbit splitting is then obtained from a one‑center effective orbital coupling formula. For a given molecular orbital, the effective coupling constant \zeta is expressed as a sum over atoms, where each atom’s contribution is the product of the orbital’s population on that atom and an interpolated coupling constant that depends on the atom’s net charge and two atomic parameters: the effective coupling constants for the neutral atom (\xi_A) and for the singly charged cation (\xi_A^+). The atomic coupling constants for the relevant elements are provided as part of the task.

Procedure I (open‑shell): the net atomic charges and the coefficients of the singly occupied \alpha‑spin orbital from the unrestricted open‑shell calculation are substituted directly into the formula.

Procedure II (closed‑shell): the net charges obtained from the closed‑shell calculation are first adjusted by subtracting the orbital population of the electron being removed, and then the same formula is applied.

For the interhalogen species BrCl⁺, ICl⁺, and IBr⁺, the wavefunction and density of ClF are employed in place of a direct calculation, using the heavy‑atom coupling constants for Br/I as appropriate.

The task requires executing the full pipeline: retrieving geometries, running CNDO/2 calculations with pyscf, extracting the needed quantities, and applying the formulas. Neither the bond lengths nor the coupling constants need to be computed from scratch; they are either retrieved from public sources or provided.

## Reproduction target
Produce a CSV file `/app/outputs/spin_orbit_splittings.csv` containing the computed spin–orbit splittings (in cm⁻¹) for every molecule listed in Step 1, using both Procedure I and Procedure II wherever applicable. The columns must include: `molecule` (string), `state` (string), `procedure_I_splitting` (float or 'N/A'), `procedure_II_splitting` (float or 'N/A'), and optionally `experimental_splitting` (float). For molecules where a procedure is not applicable (e.g., BeH does not have an open‑shell entry), enter 'N/A' in the corresponding field.

## Assets

- pyscf: pyscf
- CCCBDB: https://cccbdb.nist.gov/
- Effective atomic coupling constants

## Workflow steps

### Step 1: Collect molecular geometries
- Role: process
- Action: For every molecule listed in the study (diatomics and polyatomics from the paper’s Table 2), retrieve its experimental equilibrium bond length from the CCCBDB database (or an equivalent public source). For the interhalogen molecules BrCl⁺, ICl⁺, IBr⁺, use the bond length of ClF (1.628 Å) and treat the molecule with the appropriate heavy‑atom coupling constants as described in the original work. Store the geometries in a structured file for use in the CNDO/2 calculations.
- Evidence: `/app/outputs/geometries.json`

### Step 2: Run closed‑shell CNDO/2 calculations
- Role: process
- Action: For each molecule, perform a restricted closed‑shell CNDO/2 calculation using the experimental bond length. Save the molecular orbital coefficients and the charge‑density matrix (P_μν). These results are required for Procedure II of the spin‑orbit formula.
- Evidence: `/app/outputs/closed_shell_results.json`

### Step 3: Run open‑shell CNDO/2 calculations
- Role: process
- Action: For each molecule that requires Procedure I (as indicated by the presence of open‑shell entries in the paper’s Table 2), perform an unrestricted open‑shell CNDO/2 calculation on the degenerate ²Π state. Extract the α‑spin orbital coefficients and the charge‑density matrix. For molecules that do not have an open‑shell entry (e.g., BeH), this step may be skipped or produce a note.
- Evidence: `/app/outputs/open_shell_results.json`

### Step 4: Compute spin–orbit splittings
- Role: scored (load-bearing)
- Action: Using the CNDO/2 outputs and the effective atomic coupling constants, compute the spin‑orbit splitting (in cm⁻¹) for each molecule with both procedures: (a) Procedure I: substitute open‑shell net atomic charges and the singly‑occupied α‑orbital coefficients into the one‑center effective orbital coupling formula; (b) Procedure II: correct the closed‑shell charges by subtracting the orbital population of the missing electron, then apply the same formula. For molecules where one procedure is not applicable, fill the corresponding field with 'N/A'. Write the results to /app/outputs/spin_orbit_splittings.csv.
- Output file: `/app/outputs/spin_orbit_splittings.csv`
- Format: csv
- Contract: Columns: molecule (string), state (string), procedure_I_splitting (float, cm⁻¹, or 'N/A'), procedure_II_splitting (float, cm⁻¹, or 'N/A'), experimental_splitting (float, cm⁻¹, optional).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_orbit_splittings.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_orbit_splittings.csv
- path: `/app/outputs/spin_orbit_splittings.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Agent‑reported spin‑orbit splittings for all molecules. The verifier will recompute per‑molecule errors against a hidden reference and assess whether the average accuracy meets the expected level for both procedures.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `state`, `procedure_I_splitting`, `procedure_II_splitting`
  - `optional_columns`: `experimental_splitting`
  - `units`:
    - `procedure_I_splitting`: cm⁻¹
    - `procedure_II_splitting`: cm⁻¹
    - `experimental_splitting`: cm⁻¹

Notes: The CSV must contain every molecule from the study for which the paper reported a calculated splitting. The procedure_I_splitting and procedure_II_splitting columns accept either a numeric value (cm⁻¹) or the string 'N/A' when a procedure is not applicable. The experimental_splitting column is optional.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_orbit_splittings.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "state",
          "procedure_I_splitting",
          "procedure_II_splitting"
        ],
        "optional_columns": [
          "experimental_splitting"
        ],
        "units": {
          "procedure_I_splitting": "cm⁻¹",
          "procedure_II_splitting": "cm⁻¹",
          "experimental_splitting": "cm⁻¹"
        }
      },
      "description": "Agent‑reported spin‑orbit splittings for all molecules. The verifier will recompute per‑molecule errors against a hidden reference and assess whether the average accuracy meets the expected level for both procedures."
    }
  ],
  "notes": "The CSV must contain every molecule from the study for which the paper reported a calculated splitting. The procedure_I_splitting and procedure_II_splitting columns accept either a numeric value (cm⁻¹) or the string 'N/A' when a procedure is not applicable. The experimental_splitting column is optional."
}
```

## How you are scored
A hidden verifier will read your CSV file and compare each numeric splitting value against a reference (derived from the original study). For each molecule and procedure, it will compute the absolute percent error; then it will calculate the average percent error per procedure. The final reward is based on how well your computed averages agree with the expected accuracy level. Merely reporting the paper's published numbers is not sufficient—you must carry out the calculations described in the workflow steps to achieve a high score.
