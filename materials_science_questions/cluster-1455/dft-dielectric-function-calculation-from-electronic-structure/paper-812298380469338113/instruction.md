# Lattice energy simulation of cobalt monoxide polymorphs

## Problem background
Cobalt monoxide (CoO) can adopt several polymorphic structures—rock salt (Fm3m), zinc blende (F43m), and wurtzite (P63mc)—with distinct morphologies and cation coordinations. Understanding the relative thermodynamic stability, equilibrium lattice parameters, and dielectric response of these polymorphs is important for predicting their formation and properties. This task focuses on the computational component: atomistic lattice simulations that compute total lattice energies, relaxed structural parameters, and dielectric constants for the three experimentally observed polymorphs using a shell model with interatomic potentials. The results must distinguish the most stable polymorph and provide quantitative structural and dielectric properties for each phase.

## Approach
The calculations are based on a Born model of an ionic crystal. Ions are assigned formal charges (O²⁻ and Co²⁺) and interact via long-range Coulombic forces, summed to infinity using the Ewald method, and short-range repulsive and dispersive interactions parameterised as Buckingham potentials. Electronic polarisation is treated with the shell model, where a massless shell attached to each ion core by a harmonic spring can displace relative to the core, providing a realistic description of dielectric response. For the rock salt polymorph, where Co²⁺ occupies octahedral sites, an additional crystal-field stabilisation term—the octahedral site preference energy (OSPE)—must be added to the ionic cohesive energy to obtain the total lattice energy. The unit cell energy is minimised with respect to ion positions and lattice vectors, yielding the relaxed structure, total lattice energy, and static and high-frequency dielectric constants. The agent will set up and run geometry optimisation and property calculations for the three polymorphs using an open-source lattice simulation code (e.g., GULP) with the specified Buckingham potentials, shell parameters, and OSPE value. The relative stability of the polymorphs is assessed by comparing the computed total lattice energies.

## Reproduction target
Using the shell-model potentials and the octahedral site preference energy (0.32 eV), perform lattice energy minimisation and property calculations for CoO in the rock salt (Fm3m), zinc blende (F43m), and wurtzite (P63mc) structures. Compute and report the total lattice energy (in eV) for each polymorph, the relaxed lattice parameters (a for cubic polymorphs; a and c for wurtzite), and the static (ε0) and high-frequency (ε∞) dielectric constants (isotropic values for cubic polymorphs, anisotropic components ε11 and ε33 for wurtzite). The computed quantities must be extracted into three structured JSON artifacts as detailed in the workflow steps. The results will be evaluated for correctness of the energy ordering (more negative total lattice energy corresponds to greater stability) and numerical agreement with reference values.

## Assets

- GULP (General Utility Lattice Program): https://github.com/gulp-xx/gulp
- Interatomic potentials for CoO (Buckingham + shell model) from Catlow et al. 1977: 10.1080/14786437708232964
- Co2+ octahedral site preference energy (0.32 eV) from Dunitz & Orgel 1957: 10.1016/0022-3697(57)90093-8

## Workflow steps

### Step 1: Run GULP lattice energy minimizations
- Role: process
- Action: Using GULP (or an equivalent open-source lattice simulation code), set up and run geometry optimization and property calculations for CoO in rock salt (Fm3m), zinc blende (F43m), and wurtzite (P63mc) structures. Employ the Buckingham potentials and shell model parameters from Catlow et al. (1977). For the rock salt polymorph (octahedrally coordinated), add the octahedral site preference energy (OSPE = 0.32 eV) to the computed ionic cohesive energy to obtain the total lattice energy. Compute the total lattice energy, relaxed lattice parameters (a, and c for wurtzite), and static (ε0) and high-frequency (ε∞) dielectric constants (anisotropic components for wurtzite) for each polymorph. Save all raw output.
- Evidence: `/app/outputs/simulation.log`

### Step 2: Report energy ranking
- Role: scored (load-bearing)
- Action: Extract the total lattice energy for each polymorph from the simulation output. Produce a JSON array of objects with keys 'polymorph' (one of 'rock_salt', 'zinc_blende', 'wurtzite') and 'total_lattice_energy_eV' (float, in eV).
- Output file: `/app/outputs/step_01_energy_ranking.json`
- Format: json
- Contract: [{"polymorph": string, "total_lattice_energy_eV": float}]
- Scoring: scored by hidden verifier

### Step 3: Report lattice parameters
- Role: scored
- Action: Extract the equilibrium lattice constants from the optimization output. For rock salt and zinc blende, report only 'a_nm' (cubic lattice constant). For wurtzite, report both 'a_nm' and 'c_nm'. Produce a JSON array of objects with keys 'polymorph', 'a_nm' (float), and 'c_nm' (float or null).
- Output file: `/app/outputs/step_02_lattice_parameters.json`
- Format: json
- Contract: [{"polymorph": string, "a_nm": float, "c_nm": float or null}]
- Scoring: scored by hidden verifier

### Step 4: Report dielectric constants
- Role: scored
- Action: Extract the static and high-frequency dielectric constants from the simulation output. For the wurtzite polymorph, provide anisotropic components: epsilon_0_11, epsilon_0_33, epsilon_inf_11, epsilon_inf_33. For rock salt and zinc blende, provide isotropic values: epsilon_0 and epsilon_inf. Produce a JSON array of objects with appropriate keys (all floats; null where not applicable).
- Output file: `/app/outputs/step_03_dielectric_constants.json`
- Format: json
- Contract: [{"polymorph": string, "epsilon_0": float or null, "epsilon_inf": float or null, "epsilon_0_11": float or null, "epsilon_0_33": float or null, "epsilon_inf_11": float or null, "epsilon_inf_33": float or null}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_ranking.json`
- `/app/outputs/step_02_lattice_parameters.json`
- `/app/outputs/step_03_dielectric_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_ranking.json
- path: `/app/outputs/step_01_energy_ranking.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total lattice energy (eV) for each CoO polymorph. The array must contain exactly three objects with polymorph values 'rock_salt', 'zinc_blende', 'wurtzite'.
- schema:
  - `type`: array
  - `required`: object
  - `items`:
    - `type`: object
    - `required`: `polymorph`, `total_lattice_energy_eV`
    - `properties`:
      - `polymorph`:
        - `type`: string
      - `total_lattice_energy_eV`:
        - `type`: number
  - `required_columns`:
  - `units`: object

### step_02_lattice_parameters.json
- path: `/app/outputs/step_02_lattice_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice parameters (a in nm, c in nm where applicable) for each CoO polymorph.
- schema:
  - `type`: array
  - `required`: object
  - `items`:
    - `type`: object
    - `required`: `polymorph`, `a_nm`
    - `properties`:
      - `polymorph`:
        - `type`: string
      - `a_nm`:
        - `type`: number
      - `c_nm`:
        - `type`: `number`, `null`
  - `required_columns`:
  - `units`:
    - `a_nm`: nm
    - `c_nm`: nm

### step_03_dielectric_constants.json
- path: `/app/outputs/step_03_dielectric_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Static (ε0) and high-frequency (ε∞) dielectric constants for each CoO polymorph. For rock salt and zinc blende, use epsilon_0, epsilon_inf; for wurtzite, use the 11 and 33 components.
- schema:
  - `type`: array
  - `required`: object
  - `items`:
    - `type`: object
    - `required`: `polymorph`
    - `properties`:
      - `polymorph`:
        - `type`: string
      - `epsilon_0`:
        - `type`: `number`, `null`
      - `epsilon_inf`:
        - `type`: `number`, `null`
      - `epsilon_0_11`:
        - `type`: `number`, `null`
      - `epsilon_0_33`:
        - `type`: `number`, `null`
      - `epsilon_inf_11`:
        - `type`: `number`, `null`
      - `epsilon_inf_33`:
        - `type`: `number`, `null`
  - `required_columns`:
  - `units`: object

Notes: All values are to be obtained from a single lattice simulation run using the specified potentials and OSPE. The checker compares each reported quantity to reference values (from Table I of the original study) with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_ranking.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": {},
        "items": {
          "type": "object",
          "required": [
            "polymorph",
            "total_lattice_energy_eV"
          ],
          "properties": {
            "polymorph": {
              "type": "string"
            },
            "total_lattice_energy_eV": {
              "type": "number"
            }
          }
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Total lattice energy (eV) for each CoO polymorph. The array must contain exactly three objects with polymorph values 'rock_salt', 'zinc_blende', 'wurtzite'."
    },
    {
      "file": "step_02_lattice_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": {},
        "items": {
          "type": "object",
          "required": [
            "polymorph",
            "a_nm"
          ],
          "properties": {
            "polymorph": {
              "type": "string"
            },
            "a_nm": {
              "type": "number"
            },
            "c_nm": {
              "type": [
                "number",
                "null"
              ]
            }
          }
        },
        "required_columns": [],
        "units": {
          "a_nm": "nm",
          "c_nm": "nm"
        }
      },
      "description": "Relaxed lattice parameters (a in nm, c in nm where applicable) for each CoO polymorph."
    },
    {
      "file": "step_03_dielectric_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": {},
        "items": {
          "type": "object",
          "required": [
            "polymorph"
          ],
          "properties": {
            "polymorph": {
              "type": "string"
            },
            "epsilon_0": {
              "type": [
                "number",
                "null"
              ]
            },
            "epsilon_inf": {
              "type": [
                "number",
                "null"
              ]
            },
            "epsilon_0_11": {
              "type": [
                "number",
                "null"
              ]
            },
            "epsilon_0_33": {
              "type": [
                "number",
                "null"
              ]
            },
            "epsilon_inf_11": {
              "type": [
                "number",
                "null"
              ]
            },
            "epsilon_inf_33": {
              "type": [
                "number",
                "null"
              ]
            }
          }
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Static (ε0) and high-frequency (ε∞) dielectric constants for each CoO polymorph. For rock salt and zinc blende, use epsilon_0, epsilon_inf; for wurtzite, use the 11 and 33 components."
    }
  ],
  "notes": "All values are to be obtained from a single lattice simulation run using the specified potentials and OSPE. The checker compares each reported quantity to reference values (from Table I of the original study) with appropriate tolerances."
}
```

## How you are scored
Your output is scored by a hidden verifier that independently evaluates each of the three JSON artifacts. The verifier compares your reported total lattice energies, lattice parameters, and dielectric constants to reference values derived from the original study, using appropriate tolerances that account for implementation differences. For energy ordering, the verifier checks that the computed total lattice energies follow the expected stability sequence (more negative = more stable). Each artifact receives a score reflecting how many of its quantities satisfy the tolerance criteria, and the final reward is a weighted combination of these stage scores. Simply reporting numbers that resemble typical results is not sufficient; the values must be obtained from a genuine simulation run using the specified potentials, shell model, and OSPE addition.
