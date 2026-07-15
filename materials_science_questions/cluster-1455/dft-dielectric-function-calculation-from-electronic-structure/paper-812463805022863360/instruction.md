# Shell-model potentials for cubic KNbO3: bulk and defect properties

## Problem background
KNbO₃ (potassium niobate) is a ferroelectric perovskite widely used in nonlinear optics, including frequency-doubling laser applications. In its cubic high-temperature phase (above the paraelectric-to-ferroelectric transition temperature), the material exhibits complex ionic interactions that determine its dielectric, elastic, and defect properties. Understanding and predicting these properties is essential for optimizing device performance and for interpreting experimental data on ionic transport, which is often governed by point defects such as oxygen vacancies. The present work aims to derive classical shell-model potentials for the cubic phase and to use them to compute a comprehensive set of bulk and defect properties. By comparing the computed results with experimental measurements and with independent quantum-chemical (INDO) calculations, one can assess the reliability of the shell model. Your task is to implement the given potentials and calculate these properties, so you can directly evaluate how well a simple classical model can capture the physics of this perovskite.

## Approach
The calculations employ the classical shell model, which describes ions as massive cores coupled by harmonic springs to massless shells that represent electronic polarization. The interionic interaction is given by a Buckingham potential of the form D exp(−R/ρ) − C/R⁶, with parameters (D, ρ, C) specified for K–O, Nb–O, and O–O pairs. The shell model also assigns a core charge and shell charge to each polarizable ion, along with a spring constant. Two sets of parameters are given: potential I treats K⁺ as unpolarizable (no shell, fixed charge), while potential II includes a polarizable shell on K⁺. All calculations are performed for cubic KNbO₃ at 710 K, using the experimental lattice constant a = 4.022 Å.

The workflow is:
1. Build input files for a shell-model code (such as GULP) that define the crystal structure, the pair potentials, and the core/shell parameters.
2. Calculate perfect-crystal properties: lattice energy (cohesive energy, in eV per formula unit), elastic constants (c₁₁, c₁₂, c₄₄) by finite strain methods, the static dielectric constant εₛ and high-frequency dielectric constant ε∞ from the lattice dynamics, and the frequencies of the zone-centre (Γ) phonon modes, in particular the lowest-frequency transverse optic soft mode ω_TO₁.
3. Calculate defect properties: the formation energies of oxygen, potassium, and niobium vacancies (in eV), the relaxed atomic displacements around the oxygen vacancy and around the saddle-point configuration for oxygen-ion migration (expressed as fractions of the lattice constant multiplied by 100), and the oxygen-vacancy migration energy (eV). The defect calculations employ the standard methodology provided by the code (e.g., the Mott–Littleton two-region method) as appropriate for isolated point defects.
4. Repeat the entire calculation using potential II and compare the results.

The procedure isolates the ability of the shell model to reproduce experimental trends without relying on adjustable parameters: the potentials are fixed and must be used as given.

## Reproduction target
Produce two JSON files, `potential_I_results.json` and `potential_II_results.json`, containing the following quantities computed from the shell-model calculation with the respective potential:

- cohesive energy (eV)
- elastic constants c₁₁, c₁₂, c₄₄ (GPa)
- static permittivity εₛ (dimensionless)
- high-frequency permittivity ε∞ (dimensionless)
- frequency of the soft transverse optic mode ω_TO₁ (cm⁻¹)
- vacancy formation energies for oxygen (V_O), potassium (V_K), and niobium (V_Nb) in eV
- for the oxygen vacancy:
  - displacements of neighboring Nb, O, and K ions (fraction of lattice constant × 100)
  - displacements at the migration saddle point for the mobile O_i ion and the surrounding Nb₁, Nb₂, Nb₃, O₁, and K ions (same units)
  - migration energy (eV)

The results must be written exactly according to the schema described in the workflow steps.

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/gulp/

## Workflow steps

### Step 1: Prepare potential I input files
- Role: process
- Action: Create input file(s) for a shell-model code (e.g., GULP) defining the cubic KNbO3 structure (lattice constant 4.022 Å) with the Buckingham pair potentials and core–shell parameters of potential I as given for unpolarizable K⁺. The input must enable subsequent calculation of perfect-crystal properties (cohesive energy, elastic constants, permittivities, soft-mode phonon frequency at Γ) and defect properties (O, K, Nb vacancies and O-vacancy migration saddle point).
- Evidence: `/app/outputs/potential_I_input.gin`

### Step 2: Compute and output potential I results
- Role: scored (load-bearing)
- Action: Run the shell-model calculation with potential I. From the output extract: cohesive energy (eV), elastic constants c₁₁, c₁₂, c₄₄ (GPa), static permittivity εₛ, high-frequency permittivity ε∞, soft-mode frequency ω_TO1 (cm⁻¹), vacancy formation energies for V_O, V_K, V_Nb (eV), atomic displacements around the O vacancy and its saddle point (as fractions of the lattice constant × 100), and O-vacancy migration energy (eV). Write all quantities to potential_I_results.json following the prescribed schema.
- Output file: `/app/outputs/potential_I_results.json`
- Format: json
- Contract: {"cohesive_energy": float (eV), "elastic_constants": {"c11": float (GPa), "c12": float (GPa), "c44": float (GPa)}, "permittivities": {"epsilon_s": float, "epsilon_inf": float}, "soft_mode_frequency": float (cm⁻¹), "vacancy_formation_energies": {"V_O": float (eV), "V_K": float (eV), "V_Nb": float (eV)}, "O_vacancy": {"displacements": {"Nb": float (fraction×100), "O": float (fraction×100), "K": float (fraction×100)}, "saddle_point_displacements": {"O_i": float (fraction×100), "Nb1": float (fraction×100), "Nb2": float (fraction×100), "Nb3": float (fraction×100), "O1": float (fraction×100), "K": float (fraction×100)}, "migration_energy": float (eV)}}
- Scoring: scored by hidden verifier

### Step 3: Prepare potential II input files
- Role: process
- Action: Modify the input file(s) to use potential II parameters (the only differences are A₁₃ = 640.0 eV, Y₁ = −2.76 e, K₁ = 80.0 eV Å⁻²), keeping the same structure and calculation settings.
- Evidence: `/app/outputs/potential_II_input.gin`

### Step 4: Compute and output potential II results
- Role: scored (load-bearing)
- Action: Run the shell-model calculation with potential II and extract the same set of properties as for potential I. Write the results to potential_II_results.json using the identical schema.
- Output file: `/app/outputs/potential_II_results.json`
- Format: json
- Contract: Same as potential_I_results.json: {"cohesive_energy": float (eV), ...}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/potential_I_results.json`
- `/app/outputs/potential_II_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### potential_I_results.json
- path: `/app/outputs/potential_I_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All perfect‑crystal and defect properties computed from shell‑model potential I for cubic KNbO₃ at 710 K, compared to hidden reference values.
- schema:
  - `type`: object
  - `required`: `cohesive_energy`, `elastic_constants`, `permittivities`, `soft_mode_frequency`, `vacancy_formation_energies`, `O_vacancy`
  - `properties`:
    - `cohesive_energy`: number (unit: eV)
    - `elastic_constants`:
      - `type`: object
      - `properties`:
        - `c11`: number (unit: GPa)
        - `c12`: number (unit: GPa)
        - `c44`: number (unit: GPa)
    - `permittivities`:
      - `type`: object
      - `properties`:
        - `epsilon_s`: number (dimensionless)
        - `epsilon_inf`: number (dimensionless)
    - `soft_mode_frequency`: number (unit: cm⁻¹)
    - `vacancy_formation_energies`:
      - `type`: object
      - `properties`:
        - `V_O`: number (unit: eV)
        - `V_K`: number (unit: eV)
        - `V_Nb`: number (unit: eV)
    - `O_vacancy`:
      - `type`: object
      - `properties`:
        - `displacements`:
          - `type`: object
          - `properties`:
            - `Nb`: number (fraction of lattice constant × 100)
            - `O`: number (fraction of lattice constant × 100)
            - `K`: number (fraction of lattice constant × 100)
        - `saddle_point_displacements`:
          - `type`: object
          - `properties`:
            - `O_i`: number (fraction of lattice constant × 100)
            - `Nb1`: number (fraction of lattice constant × 100)
            - `Nb2`: number (fraction of lattice constant × 100)
            - `Nb3`: number (fraction of lattice constant × 100)
            - `O1`: number (fraction of lattice constant × 100)
            - `K`: number (fraction of lattice constant × 100)
        - `migration_energy`: number (unit: eV)

### potential_II_results.json
- path: `/app/outputs/potential_II_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All perfect‑crystal and defect properties computed from shell‑model potential II for cubic KNbO₃ at 710 K, compared to hidden reference values.
- schema:
  - `type`: object
  - `description`: Same structured schema as potential_I_results.json: cohesive_energy (eV), elastic_constants {c11,c12,c44} (GPa), permittivities {epsilon_s, epsilon_inf}, soft_mode_frequency (cm⁻¹), vacancy_formation_energies {V_O, V_K, V_Nb} (eV), O_vacancy {displacements {Nb,O,K} (fraction×100), saddle_point_displacements {O_i, Nb1, Nb2, Nb3, O1, K} (fraction×100), migration_energy (eV)}

Notes: The solver must install an open‑source shell‑model code (e.g., GULP) and construct input files from the potentials specified in the paper's Table 3. No fitting or training is required; the potentials are provided as fixed parameters. All numerical outputs must follow the defined units and schema exactly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "potential_I_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "cohesive_energy",
          "elastic_constants",
          "permittivities",
          "soft_mode_frequency",
          "vacancy_formation_energies",
          "O_vacancy"
        ],
        "properties": {
          "cohesive_energy": "number (unit: eV)",
          "elastic_constants": {
            "type": "object",
            "properties": {
              "c11": "number (unit: GPa)",
              "c12": "number (unit: GPa)",
              "c44": "number (unit: GPa)"
            }
          },
          "permittivities": {
            "type": "object",
            "properties": {
              "epsilon_s": "number (dimensionless)",
              "epsilon_inf": "number (dimensionless)"
            }
          },
          "soft_mode_frequency": "number (unit: cm⁻¹)",
          "vacancy_formation_energies": {
            "type": "object",
            "properties": {
              "V_O": "number (unit: eV)",
              "V_K": "number (unit: eV)",
              "V_Nb": "number (unit: eV)"
            }
          },
          "O_vacancy": {
            "type": "object",
            "properties": {
              "displacements": {
                "type": "object",
                "properties": {
                  "Nb": "number (fraction of lattice constant × 100)",
                  "O": "number (fraction of lattice constant × 100)",
                  "K": "number (fraction of lattice constant × 100)"
                }
              },
              "saddle_point_displacements": {
                "type": "object",
                "properties": {
                  "O_i": "number (fraction of lattice constant × 100)",
                  "Nb1": "number (fraction of lattice constant × 100)",
                  "Nb2": "number (fraction of lattice constant × 100)",
                  "Nb3": "number (fraction of lattice constant × 100)",
                  "O1": "number (fraction of lattice constant × 100)",
                  "K": "number (fraction of lattice constant × 100)"
                }
              },
              "migration_energy": "number (unit: eV)"
            }
          }
        }
      },
      "description": "All perfect‑crystal and defect properties computed from shell‑model potential I for cubic KNbO₃ at 710 K, compared to hidden reference values."
    },
    {
      "file": "potential_II_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Same structured schema as potential_I_results.json: cohesive_energy (eV), elastic_constants {c11,c12,c44} (GPa), permittivities {epsilon_s, epsilon_inf}, soft_mode_frequency (cm⁻¹), vacancy_formation_energies {V_O, V_K, V_Nb} (eV), O_vacancy {displacements {Nb,O,K} (fraction×100), saddle_point_displacements {O_i, Nb1, Nb2, Nb3, O1, K} (fraction×100), migration_energy (eV)}"
      },
      "description": "All perfect‑crystal and defect properties computed from shell‑model potential II for cubic KNbO₃ at 710 K, compared to hidden reference values."
    }
  ],
  "notes": "The solver must install an open‑source shell‑model code (e.g., GULP) and construct input files from the potentials specified in the paper's Table 3. No fitting or training is required; the potentials are provided as fixed parameters. All numerical outputs must follow the defined units and schema exactly."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier. For each of the two output files, the verifier extracts every numerical quantity (cohesive energy, elastic constants, permittivities, soft-mode frequency, vacancy formation energies, migration energy, and atomic displacements) and compares them to a hidden reference. Each quantity is scored individually, with the most weight given to the key bulk and defect properties. The scores from both potentials are then combined into a final reward between 0 and 1, where 1 indicates full reproduction quality. The verifier does not depend on the paper’s original data files; it uses an independently prepared reference. Simply copying reported numbers without actually running the shell-model calculation will not achieve a high score because the verifier checks that the set of values is internally consistent with the physical calculation.
