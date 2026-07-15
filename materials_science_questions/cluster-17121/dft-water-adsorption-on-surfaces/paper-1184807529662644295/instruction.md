# Shape Memory in 2D Covalent Organic Frameworks

## Problem background
Two-dimensional covalent organic frameworks (2D COFs) are layered crystalline materials built from covalently bonded molecular building blocks. Their layers are held together by weak van der Waals interactions, which makes it possible to change the interlayer stacking and, consequently, the pore size of the one-dimensional nanochannels. Understanding which stacking arrangement is thermodynamically stable in the presence of adsorbed guest molecules is a key step toward controlling the pore structure. Molecular dynamics simulations provide a route to compute the enthalpy of the COF and COF–adsorbate systems under different interlayer stacking angles and adsorbate loadings, offering insight into the driving forces that favor one stacking phase over another.

## Approach
The approach is to perform classical molecular dynamics simulations using the LAMMPS package and the ReaxFF-lg reactive force field, which captures van der Waals interactions, Coulomb forces, and London dispersion. The system under study is the TAPT‑TFPA COF constructed as a 2×2 supercell containing 5 layers. Interlayer stacking is varied by changing the incline angle between the layer normal and the stacking axis (70°, 80°, 85°, 90°). Simulations are carried out under the NPT ensemble (300 K, 1 atm) for 5 × 10⁶ steps with a 0.1 fs time step. Three types of systems are simulated: (i) pure COF at each incline angle, (ii) COF with inserted THF molecules at four loadings (0, 30, 60, 112 THF per supercell), and (iii) COF with inserted H₂O molecules at three loadings (628, 780, 917 H₂O per supercell). For each equilibrium trajectory, the average enthalpy of the simulation cell is computed. For COF + THF systems, the operational enthalpy H(n) is obtained by adding the contribution of the missing liquid THF molecules, using a reference liquid‑phase THF enthalpy per molecule. The average van der Waals interaction energy between THF and the COF is also extracted. For COF + H₂O systems, the operational enthalpy is computed analogously using a liquid‑water reference enthalpy, and the oxygen‑oxygen radial distribution function g_OO(r) is calculated to characterize water ordering. All results are saved as CSV files for later verification.

## Reproduction target
Determine and report, from the molecular dynamics simulations described in the workflow steps, the following quantitative results: (1) For pure COF, the average enthalpy as a function of the incline angle, identifying which angle gives the lowest enthalpy. (2) For COF + THF, the operational enthalpy H(n) at each incline angle and THF loading, and the average THF–COF interaction energy, to reveal how adsorbate loading modifies the relative stability of different stacking angles. (3) For COF + H₂O, the operational enthalpy at each incline angle and water loading, to observe how the energetically preferred stacking angle shifts as more water is added, and the position and height of the first peak of the O–O radial distribution function, to assess any structural ordering of the confined water. All outputs must be written as the CSV files listed in the Workflow steps with the specified column schemas.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- ReaxFF-lg force field parameters: 10.1021/jp201599t
- TAPT-TFPA COF crystal structure: 10.1016/j.xcrp.2023.101273
- Reference enthalpy of liquid THF per molecule
- Reference enthalpy of liquid H2O per molecule

## Workflow steps

### Step 1: Build COF and COF+adsorbate initial configurations
- Role: process
- Action: Construct initial atomic configurations for TAPT-TFPA COF in a 2×2 unit cell with 5 layers at incline angles 70°, 80°, 85°, 90°. Also generate configurations with inserted THF molecules at loadings 0, 30, 60, 112 and with H2O molecules at loadings 628, 780, 917. Output LAMMPS data files and input scripts.
- Evidence: `/app/outputs/model_build.log`

### Step 2: Run pure COF MD simulations
- Role: process
- Action: Using LAMMPS with ReaxFF-lg force field, run NPT simulations (300 K, 1 atm) for pure COF at each incline angle for 5×10⁶ steps (0.1 fs time step). Store trajectory and log files.
- Evidence: `/app/outputs/pure_cof_simulation.log`

### Step 3: Extract pure COF enthalpy vs incline angle
- Role: scored (load-bearing)
- Action: From the pure COF simulation logs, compute the average enthalpy per simulation cell after equilibration and write pure_cof_enthalpy.csv.
- Output file: `/app/outputs/pure_cof_enthalpy.csv`
- Format: csv
- Contract: columns: incline_angle (degrees), enthalpy (kcal/mol). One row per angle.
- Scoring: scored by hidden verifier

### Step 4: Run COF+THF MD simulations
- Role: process
- Action: For each incline angle and each THF loading (n=0,30,60,112), run NPT simulations using the same settings as pure COF. Store log files.
- Evidence: `/app/outputs/cof_thf_simulation.log`

### Step 5: Compute COF+THF operational enthalpy
- Role: scored (load-bearing)
- Action: From the COF+THF simulation logs, compute H₀(n) (enthalpy of COF with n THF). Then compute operational enthalpy H(n) = H₀(n) + (112-n) * h_THF, where h_THF is the enthalpy per liquid THF molecule. Write cof_thf_enthalpy.csv.
- Output file: `/app/outputs/cof_thf_enthalpy.csv`
- Format: csv
- Contract: columns: incline_angle (degrees), n_THF (integer), enthalpy (kcal/mol). One row per angle and loading combination.
- Scoring: scored by hidden verifier

### Step 6: Analyze THF–COF interaction energy
- Role: scored (load-bearing)
- Action: From the same THF simulation trajectories, compute the average van der Waals interaction energy between THF molecules and the COF. Write cof_thf_interaction_energy.csv.
- Output file: `/app/outputs/cof_thf_interaction_energy.csv`
- Format: csv
- Contract: columns: incline_angle (degrees), n_THF (integer), interaction_energy (kcal/mol). One row per angle and loading combination.
- Scoring: scored by hidden verifier

### Step 7: Run COF+H2O MD simulations
- Role: process
- Action: For each incline angle and each H2O loading (n=628,780,917), run NPT simulations using the same settings. Store log files.
- Evidence: `/app/outputs/cof_h2o_simulation.log`

### Step 8: Compute COF+H2O operational enthalpy
- Role: scored (load-bearing)
- Action: From H2O simulation logs, compute H₀(n) and then operational enthalpy H(n) with water reference enthalpy h_H2O. Write cof_h2o_enthalpy.csv.
- Output file: `/app/outputs/cof_h2o_enthalpy.csv`
- Format: csv
- Contract: columns: incline_angle (degrees), n_H2O (integer), enthalpy (kcal/mol). One row per angle and loading combination.
- Scoring: scored by hidden verifier

### Step 9: Compute water O–O radial distribution function peaks
- Role: scored (load-bearing)
- Action: From equilibrated H2O simulation trajectories, compute the O–O radial distribution function g_OO(r) for each loading and incline angle. Extract the position and height of the first peak. Write cof_h2o_rdf_peak.csv.
- Output file: `/app/outputs/cof_h2o_rdf_peak.csv`
- Format: csv
- Contract: columns: n_H2O (integer), incline_angle (degrees), first_peak_position (Angstrom), first_peak_height (arbitrary units). One row per condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_cof_enthalpy.csv`
- `/app/outputs/cof_thf_enthalpy.csv`
- `/app/outputs/cof_thf_interaction_energy.csv`
- `/app/outputs/cof_h2o_enthalpy.csv`
- `/app/outputs/cof_h2o_rdf_peak.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_cof_enthalpy.csv
- path: `/app/outputs/pure_cof_enthalpy.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Enthalpy of pure COF as a function of incline angle. Lower enthalpy is better; the reference value favors a slipped-AA minimum near 85°.
- schema:
  - `type`: table
  - `required_columns`: `incline_angle`, `enthalpy`
  - `units`:
    - `incline_angle`: degrees
    - `enthalpy`: kcal/mol

### cof_thf_enthalpy.csv
- path: `/app/outputs/cof_thf_enthalpy.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Operational enthalpy H(n) of COF+THF system. The agent must compute the enthalpy minimum near 70° incline; lower is better.
- schema:
  - `type`: table
  - `required_columns`: `incline_angle`, `n_THF`, `enthalpy`
  - `units`:
    - `incline_angle`: degrees
    - `n_THF`: integer
    - `enthalpy`: kcal/mol

### cof_thf_interaction_energy.csv
- path: `/app/outputs/cof_thf_interaction_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average vdW interaction energy between THF and COF. The checker verifies the trend (stronger interaction at 70°).
- schema:
  - `type`: table
  - `required_columns`: `incline_angle`, `n_THF`, `interaction_energy`
  - `units`:
    - `incline_angle`: degrees
    - `n_THF`: integer
    - `interaction_energy`: kcal/mol

### cof_h2o_enthalpy.csv
- path: `/app/outputs/cof_h2o_enthalpy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Operational enthalpy of COF+H2O system. The checker verifies the stability inversion trend: the minimum shifts from 70° to 85° with increasing water loading.
- schema:
  - `type`: table
  - `required_columns`: `incline_angle`, `n_H2O`, `enthalpy`
  - `units`:
    - `incline_angle`: degrees
    - `n_H2O`: integer
    - `enthalpy`: kcal/mol

### cof_h2o_rdf_peak.csv
- path: `/app/outputs/cof_h2o_rdf_peak.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: First peak of O–O radial distribution function, indicating water ordering. The checker compares the peak position and height to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `n_H2O`, `incline_angle`, `first_peak_position`, `first_peak_height`
  - `units`:
    - `n_H2O`: integer
    - `incline_angle`: degrees
    - `first_peak_position`: Angstrom
    - `first_peak_height`: arbitrary units

Notes: All scored artifacts are derived from MD simulations; the agent must re-run the full pipeline. No pre-computed data is provided. The reference liquid enthalpies h_THF and h_H2O are obtained from public thermodynamic data or simple reference MD runs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_cof_enthalpy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "incline_angle",
          "enthalpy"
        ],
        "units": {
          "incline_angle": "degrees",
          "enthalpy": "kcal/mol"
        }
      },
      "description": "Enthalpy of pure COF as a function of incline angle. Lower enthalpy is better; the reference value favors a slipped-AA minimum near 85°."
    },
    {
      "file": "cof_thf_enthalpy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "incline_angle",
          "n_THF",
          "enthalpy"
        ],
        "units": {
          "incline_angle": "degrees",
          "n_THF": "integer",
          "enthalpy": "kcal/mol"
        }
      },
      "description": "Operational enthalpy H(n) of COF+THF system. The agent must compute the enthalpy minimum near 70° incline; lower is better."
    },
    {
      "file": "cof_thf_interaction_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "incline_angle",
          "n_THF",
          "interaction_energy"
        ],
        "units": {
          "incline_angle": "degrees",
          "n_THF": "integer",
          "interaction_energy": "kcal/mol"
        }
      },
      "description": "Average vdW interaction energy between THF and COF. The checker verifies the trend (stronger interaction at 70°)."
    },
    {
      "file": "cof_h2o_enthalpy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "incline_angle",
          "n_H2O",
          "enthalpy"
        ],
        "units": {
          "incline_angle": "degrees",
          "n_H2O": "integer",
          "enthalpy": "kcal/mol"
        }
      },
      "description": "Operational enthalpy of COF+H2O system. The checker verifies the stability inversion trend: the minimum shifts from 70° to 85° with increasing water loading."
    },
    {
      "file": "cof_h2o_rdf_peak.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_H2O",
          "incline_angle",
          "first_peak_position",
          "first_peak_height"
        ],
        "units": {
          "n_H2O": "integer",
          "incline_angle": "degrees",
          "first_peak_position": "Angstrom",
          "first_peak_height": "arbitrary units"
        }
      },
      "description": "First peak of O–O radial distribution function, indicating water ordering. The checker compares the peak position and height to hidden gold values."
    }
  ],
  "notes": "All scored artifacts are derived from MD simulations; the agent must re-run the full pipeline. No pre-computed data is provided. The reference liquid enthalpies h_THF and h_H2O are obtained from public thermodynamic data or simple reference MD runs."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently reads each of the scored CSV artifacts. For every artifact, the verifier compares the reported values to a hidden reference derived from the paper's reported computational results. The comparison considers whether the computed quantities follow the expected trends, relative ordering, and structural features. Each artifact receives a partial score, and the weighted sum of these scores gives the final reward. The highest reward is earned by executing the full simulation and analysis pipeline honestly; simply reporting numbers without performing the underlying process steps will not produce artifacts that pass all of the hidden consistency checks.
