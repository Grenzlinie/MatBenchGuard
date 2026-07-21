# DFT Study of Band Gap and Adsorption Energy in Transition-Metal-Doped CNT(6,0)

## Problem background
Carbon nanotubes (CNTs) have electronic properties that can be tuned by doping with transition metals. In this task, you will investigate how single Cu, Ag, and Au atoms adsorbed at three distinct sites — inside the tube cavity, at the hydrogen-passivated edge, and on the outer sidewall — of a finite CNT(6,0) model affect its band gap energy and adsorption energy. Understanding these site- and metal-dependent changes is important for the design of CNT-based electronic devices and catalysts.

## Approach
Use density functional theory (DFT) with the B3PW91 functional and the LANL2DZ basis set, which provides effective core potentials for the transition metals. Construct a finite, hydrogen-passivated CNT(6,0) model containing 48 carbon atoms and 12 hydrogen atoms. Build the pristine nanotube and nine doped structures where a single Cu, Ag, or Au atom is placed at one of three adsorption sites: inside (I), edge (E), or outside (O). Perform full geometry optimizations for all CNT-containing systems and single-point energy calculations for isolated metal atoms. From the DFT outputs, extract the HOMO and LUMO eigenvalues; the band gap energy is defined as the difference between the LUMO and HOMO energies. The adsorption energy is computed as the total energy of the metal+nanotube complex minus the sum of the pristine tube energy and the isolated metal atom energy. As an additional analysis required by the original method, run Natural Bond Orbital (NBO) population analysis on the optimized doped structures; the atomic charges are recorded but not numerically scored.

## Reproduction target
Compute, from your DFT results, the band gap energy (in eV) for the pristine CNT(6,0) and for each of the nine doped systems (Cu, Ag, Au at I, E, O). Also compute the adsorption energy (in eV) for each doped system. Write the band gap results to `/app/outputs/band_gaps.csv` with columns `system` (one of `pristine`, `Cu-I`, `Cu-E`, `Cu-O`, `Ag-I`, `Ag-E`, `Ag-O`, `Au-I`, `Au-E`, `Au-O`) and `Eg` (float, eV). Write the adsorption energies to `/app/outputs/adsorption_energies.csv` with columns `system` (same codes minus `pristine`) and `Eads` (float, eV). The band gaps and adsorption energies are defined by the equations in the approach; you must compute them from the raw DFT outputs, not from previously reported numbers. Both CSV files are scored.

## Assets

- Open-source DFT code supporting B3PW91/LANL2DZ (e.g., ORCA, NWChem): https://orcaforum.kofo.mpg.de
- LANL2DZ basis set and effective core potential: https://www.basissetexchange.org

## Workflow steps

### Step 1: Build initial atomic geometries
- Role: process
- Action: Construct a finite, hydrogen-passivated CNT(6,0) model (48 C atoms, 12 H atoms). Generate initial Cartesian coordinates for the pristine tube and for each of the nine doped systems (Cu, Ag, Au at Inside, Edge, Outside sites). Also prepare an isolated atom structure for each metal. Save coordinates in a format readable by the chosen DFT code.
- Evidence: `/app/outputs/geometries.zip`

### Step 2: Run DFT geometry optimizations and energy calculations
- Role: process
- Action: For every structure (pristine CNT, nine doped CNTs, three isolated metal atoms), perform a full DFT geometry optimization (for the CNT structures) and single-point energy calculation (for the isolated atoms) using the B3PW91 functional and LANL2DZ basis set. Record total energies, HOMO and LUMO eigenvalues, and the optimized final coordinates.
- Evidence: `/app/outputs/dft_outputs.zip`

### Step 3: Compute and report band gap energies
- Role: scored (load-bearing)
- Action: Extract the HOMO and LUMO eigenvalues from the DFT output for the pristine and each doped system. Compute the band gap Eg = ε_LUMO − ε_HOMO (in eV) and write the results to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with columns: system (string, one of 'pristine','Cu-I','Cu-E','Cu-O','Ag-I','Ag-E','Ag-O','Au-I','Au-E','Au-O'), Eg (float, in eV).
- Scoring: scored by hidden verifier

### Step 4: Compute and report adsorption energies
- Role: scored (load-bearing)
- Action: Using the total energies from step 2 for the doped CNT systems, the pristine CNT, and the isolated metal atoms, compute Eads = E(CNT+metal) − E(pristine) − E(isolated metal atom). Convert to eV and write the results to adsorption_energies.csv.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: CSV with columns: system (string, e.g., 'Cu-I','Cu-E','Cu-O','Ag-I','Ag-E','Ag-O','Au-I','Au-E','Au-O'), Eads (float, in eV).
- Scoring: scored by hidden verifier

### Step 5: Perform NBO charge analysis
- Role: process
- Action: Run Natural Bond Orbital (NBO) population analysis on the optimized wavefunctions of all doped CNT structures. Record the atomic charges.
- Evidence: `/app/outputs/nbo_charges.log`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/adsorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap energies for the pristine and all nine doped CNT(6,0) variants. The hidden checker compares the submitted values to the paper's reported band gaps (reference) within a tolerance and enforces structural trends.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Eg`
  - `units`:
    - `Eg`: eV

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies of Cu, Ag, Au on CNT(6,0) at the three sites. The hidden checker compares the submitted values to the paper's reported adsorption energies (reference) within a tolerance and enforces site/metal ordering.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Eads`
  - `units`:
    - `Eads`: eV

Notes: NBO analysis (step 5) is required as a process step but is not scored because the paper shows only qualitative color-mapped charges without explicit numeric targets. The scored outputs are band_gaps.csv and adsorption_energies.csv; both must be present and match the declared schema.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Eg"
        ],
        "units": {
          "Eg": "eV"
        }
      },
      "description": "Band gap energies for the pristine and all nine doped CNT(6,0) variants. The hidden checker compares the submitted values to the paper's reported band gaps (reference) within a tolerance and enforces structural trends."
    },
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Eads"
        ],
        "units": {
          "Eads": "eV"
        }
      },
      "description": "Adsorption energies of Cu, Ag, Au on CNT(6,0) at the three sites. The hidden checker compares the submitted values to the paper's reported adsorption energies (reference) within a tolerance and enforces site/metal ordering."
    }
  ],
  "notes": "NBO analysis (step 5) is required as a process step but is not scored because the paper shows only qualitative color-mapped charges without explicit numeric targets. The scored outputs are band_gaps.csv and adsorption_energies.csv; both must be present and match the declared schema."
}
```

## How you are scored
A hidden verifier reads your `band_gaps.csv` and `adsorption_energies.csv` and scores them in multiple dimensions: structural consistency checks (e.g., relative ordering of band gaps or adsorption energies between different metals and adsorption sites) and quantitative comparison to a hidden reference derived from the original study. The reward is a weighted combination of these checks. You must compute all values by running the DFT workflow; reporting the expected numbers without genuine computation will not pass the checks. The verifier does not inspect the intermediate DFT output files or the NBO log; only the two CSV files are evaluated.
