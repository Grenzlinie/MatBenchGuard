# Molecular Mechanics Interaction Energy and QSAR Model for Carbon Nanoparticles with a SARS-CoV-2 RNA Fragment

## Problem background
The COVID-19 pandemic has underscored the need for antiviral strategies, including nanomaterials that may interact with viral components. Carbon nanoparticles (CNPs) such as fullerenes, carbon nanotubes, and graphene are candidate anti-viral agents. This work investigates the molecular interactions between a set of 17 structurally diverse CNPs and a key RNA fragment of SARS-CoV-2 — the frameshift stimulation element (FSE) that is essential for viral replication. The goal is to compute the interaction energies that stabilize these complexes and to develop quantitative structure-activity relationship (QSAR) models that link CNP structural descriptors to the interaction strength. Such models can help screen and design nanomaterials that interact strongly with the viral RNA.

## Approach
The method uses classical molecular mechanics simulations. For each CNP, a complex with the SARS-CoV-2 RNA FSE fragment is built. A simulated annealing protocol with the Universal Force Field (UFF) is applied to sample low‑energy configurations. After annealing and geometry optimization, the total potential energy of the complex, the isolated CNP, and the isolated RNA are recorded. The interaction energy is then obtained as the difference between the complex energy and the sum of the energies of the isolated components. This procedure is repeated for all 17 CNPs. Separately, several constitutional molecular descriptors that capture size, surface, and topology (molecular weight, overall surface area, specific surface area, volume, and sum of degrees) are computed for each CNP. Orthogonal partial least squares (OPLS) regression is used to build QSAR models that quantitatively relate these descriptors to the computed interaction energies. Three models are built: one for fullerenes only, one for carbon nanotubes and graphenes combined, and one for all CNPs together.

## Reproduction target
Reproduce the interaction energy values (total potential energy component) for all 17 CNP‑RNA complexes using the specified simulated annealing protocol, and report them in a CSV file. In addition, compute the five molecular descriptors for each CNP and perform OPLS regression to build the three QSAR models; output the regression equations, coefficients, and standard goodness‑of‑fit statistics (R², RMSE, and cumulative Q²) in a structured JSON file. The models to produce are: (1) fullerenes only, (2) carbon nanotubes and graphenes combined, and (3) all CNPs together.

## Assets

- SARS-CoV-2 RNA frameshift stimulation element (FSE) 3D structure (PDB 6XRZ): https://www.rcsb.org/structure/6XRZ
- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- Open Babel cheminformatics toolkit: http://openbabel.org/
- NumPy: numpy
- scikit-learn: scikit-learn
- RDKit: rdkit

## Workflow steps

### Step 1: Prepare molecular structures
- Role: process
- Action: Obtain the three-dimensional structure of the SARS-CoV-2 RNA frameshift stimulation element (FSE) from the public PDB entry 6XRZ (or equivalent). Construct the 17 carbon nanoparticle (CNP) models: fullerenes (C20, C36, C60, C70, C240, C20@C60, C20@C60@C240), carbon nanotubes (SCNT (10,0), SCNT (6,6), SCNT (28,0), DCNT (10,0), DCNT (6,6), TCNT (10,0), NR (6,6), SCNT (16,0)@C60), and graphenes (MG, BG). Use the geometries and formulas described in the method.
- Evidence: none

### Step 2: Run simulated annealing simulations
- Role: process
- Action: For each CNP, build the complex with the RNA fragment and run a classical simulated annealing simulation using the Universal Force Field (e.g., with LAMMPS) with the protocol: 200 annealing cycles, initial temperature 200 K, mid‑cycle temperature 300 K, 50 heating ramps per cycle, 100 dynamic steps per ramp, NVT ensemble with Nosé–Hoover thermostat, 1 fs timestep, cutoff 18.5 Å. After each cycle minimize the lowest energy configuration. Save the total potential energy, van der Waals energy, and electrostatic energy for the optimized complex, the isolated CNP, and the isolated RNA.
- Evidence: `/app/outputs/simulation_logs.txt`

### Step 3: Compute interaction energies
- Role: scored
- Action: From the simulation output energies, calculate the interaction energy for each CNP–RNA complex as E_int = E_complex – E_CNP – E_RNA, for the total potential, van der Waals, and electrostatic components. Write the results to a CSV file.
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: CSV with columns: CNP_name (string), E_int_total (float, kcal/mol), E_int_vdw (float, optional), E_int_elec (float, optional). 17 rows, one per CNP.
- Scoring: scored by hidden verifier

### Step 4: Compute molecular descriptors
- Role: process
- Action: Compute the five molecular descriptors (molecular weight MW, overall surface area OSA, volume Vol, specific surface area SSA, sum of degrees SDeg) for each CNP using cheminformatics tools (e.g., RDKit, Open Babel) and save the descriptor table as a CSV file.
- Evidence: `/app/outputs/descriptors.csv`

### Step 5: Develop nano‑QSAR models
- Role: scored (load-bearing)
- Action: Using the total potential interaction energies from interaction_energies.csv and the descriptors from descriptors.csv, perform orthogonal partial least squares (OPLS) regression. Build three models: fullerenes only, CNTs+graphenes, and all CNPs. Output each model's regression equation, coefficients, and statistics R², RMSE, cumulative Q² (Q²_CUM) in a structured JSON file.
- Output file: `/app/outputs/qsar_models.json`
- Format: json
- Contract: JSON object with keys 'fullerenes', 'cnt_graphenes', 'all'. Each value is an object containing: 'equation' (string), 'R2' (float), 'RMSE' (float), 'Q2_CUM' (float), 'coefficients' (object with descriptor names as keys and numeric coefficient values).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.csv`
- `/app/outputs/qsar_models.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of interaction energies per CNP, calculated from the annealing simulations. The checker compares E_int_total against paper‑reported reference values (hidden) and verifies the among‑family ordering (fullerenes < graphenes < CNTs).
- schema:
  - `type`: table
  - `required_columns`: `CNP_name`, `E_int_total`
  - `optional_columns`: `E_int_vdw`, `E_int_elec`
  - `units`:
    - `E_int_total`: kcal/mol
    - `E_int_vdw`: kcal/mol
    - `E_int_elec`: kcal/mol

### qsar_models.json
- path: `/app/outputs/qsar_models.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: QSAR model coefficients and statistics. The checker re‑fits the same OPLS regressions from the agent's own interaction_energies.csv and descriptors.csv and confirms that the agent's reported R² and Q²_CUM are within 0.1 of the re‑fit values.
- schema:
  - `type`: object
  - `required`: `fullerenes`, `cnt_graphenes`, `all`
  - `properties`:
    - `fullerenes`:
      - `type`: object
      - `required`: `equation`, `R2`, `RMSE`, `Q2_CUM`, `coefficients`
    - `cnt_graphenes`:
      - `type`: object
      - `required`: `equation`, `R2`, `RMSE`, `Q2_CUM`, `coefficients`
    - `all`:
      - `type`: object
      - `required`: `equation`, `R2`, `RMSE`, `Q2_CUM`, `coefficients`

Notes: The agent must run the full simulated annealing pipeline to produce the component energies. The QSAR step is load‑bearing: its verification uses a recompute from the agent's own numerical outputs, so faking interaction energies without real simulation yields inconsistent QSAR statistics and fails the check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "CNP_name",
          "E_int_total"
        ],
        "optional_columns": [
          "E_int_vdw",
          "E_int_elec"
        ],
        "units": {
          "E_int_total": "kcal/mol",
          "E_int_vdw": "kcal/mol",
          "E_int_elec": "kcal/mol"
        }
      },
      "description": "Table of interaction energies per CNP, calculated from the annealing simulations. The checker compares E_int_total against paper‑reported reference values (hidden) and verifies the among‑family ordering (fullerenes < graphenes < CNTs)."
    },
    {
      "file": "qsar_models.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "fullerenes",
          "cnt_graphenes",
          "all"
        ],
        "properties": {
          "fullerenes": {
            "type": "object",
            "required": [
              "equation",
              "R2",
              "RMSE",
              "Q2_CUM",
              "coefficients"
            ]
          },
          "cnt_graphenes": {
            "type": "object",
            "required": [
              "equation",
              "R2",
              "RMSE",
              "Q2_CUM",
              "coefficients"
            ]
          },
          "all": {
            "type": "object",
            "required": [
              "equation",
              "R2",
              "RMSE",
              "Q2_CUM",
              "coefficients"
            ]
          }
        }
      },
      "description": "QSAR model coefficients and statistics. The checker re‑fits the same OPLS regressions from the agent's own interaction_energies.csv and descriptors.csv and confirms that the agent's reported R² and Q²_CUM are within 0.1 of the re‑fit values."
    }
  ],
  "notes": "The agent must run the full simulated annealing pipeline to produce the component energies. The QSAR step is load‑bearing: its verification uses a recompute from the agent's own numerical outputs, so faking interaction energies without real simulation yields inconsistent QSAR statistics and fails the check."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. For `interaction_energies.csv`, the verifier compares your reported total interaction energies against hidden reference values (derived from the published study) with a generous tolerance, and it checks that the relative ordering of interaction strengths among the three CNP families (fullerenes, carbon nanotubes, graphene) follows the correct trend. For `qsar_models.json`, the verifier re‑performs the same OPLS regressions using your own `interaction_energies.csv` and the descriptors you computed, and verifies that the R² and cumulative Q² you reported are consistent with the re‑fit values (within a predetermined margin). The final reward is a weighted combination of the scores from both stages; simply reporting a number that matches the published result without genuinely running the simulation pipeline will not pass the consistency check.
