# Shell-Model Parametrization and Property Prediction for Cubic KNbO3

## Problem background
Perovskite oxides like KNbO₃ are important functional materials for optical and electronic applications, and their properties are strongly influenced by atomic-scale defects. Understanding defect formation and migration requires accurate interatomic potential models. The cubic (high-temperature) phase of KNbO₃ serves as the reference structure for modeling. A semi-empirical shell model can capture both ionic and covalent bonding contributions, enabling the calculation of structural, elastic, dielectric, and defect properties. This task involves deriving a shell-model parametrization for cubic KNbO₃ and using it to predict a comprehensive set of material properties.

## Approach
The interatomic interactions are described by Buckingham pair potentials (exponential repulsion plus an attractive dispersion term) and a core-shell model to account for ionic polarizability. Each ion is represented by a core and a massless shell connected by a harmonic spring; the shell charge and spring constant are adjustable parameters. The parametrization is performed by fitting the potential parameters to reproduce the experimental soft-mode transverse optic phonon frequency ω_TO1 = 96 cm⁻¹ at the Γ point for cubic KNbO₃ at 710 K, with a fixed lattice constant of 4.022 Å. Starting from a previously published set of parameters, the fitting procedure refines the repulsive and van der Waals parameters and the core-shell charges/spring constants to achieve this target. Once the potential is obtained, it is used in lattice dynamics and defect calculations: elastic constants (c₁₁, c₁₂, c₄₄) are computed via second derivatives of the energy; static and high-frequency dielectric permittivities are extracted from the phonon response; Γ‑point phonon frequencies are calculated from the dynamical matrix; isolated vacancy formation energies are obtained by comparing the energy of a supercell containing a vacancy to that of a perfect crystal; and the oxygen vacancy migration barrier is determined by locating the saddle-point configuration along the interstitialcy migration path.

## Reproduction target
Develop a Buckingham + core-shell potential for cubic KNbO₃ that reproduces the experimental soft-mode frequency ω_TO1 = 96 cm⁻¹ at 710 K (lattice constant 4.022 Å). Using the fitted potential, compute the following quantities for the same cubic phase at 710 K:

- Elastic constants c₁₁, c₁₂, c₄₄ (in GPa).
- Static permittivity ε_s and high-frequency permittivity ε_∞ (dimensionless).
- Frequencies (in cm⁻¹) of the transverse and longitudinal optic modes TO1, LO1, TO2, LO2, TO3, LO3 at the Γ point.
- Formation energies (in eV) of isolated oxygen (V_O), potassium (V_K), and niobium (V_Nb) vacancies.
- Oxygen vacancy migration energy (in eV) along the interstitialcy mechanism.

Write the results to the specified JSON files. The parameter set itself is not scored numerically, but it must be saved as potential_parameters.json to document the fitting process.

## Assets

- Donnerberg–Exner shell-model potentials for KNbO3: 10.1103/PhysRevB.49.3746
- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/

## Workflow steps

### Step 1: Fit shell-model potential
- Role: process
- Action: Starting from the Donnerberg–Exner Buckingham potentials, refine the D_ij, ρ_ij, C_ij parameters for pairs K–O, Nb–O, O–O, and the core-shell charges Y_i and spring constants K_i for K, Nb, O, to match the experimental soft-mode frequency ω_TO1 = 96 cm⁻¹ at the Γ point for cubic KNbO3 at 710 K (lattice constant a=4.022 Å). Use the GULP code.
- Evidence: `/app/outputs/potential_parameters.json`

### Step 2: Compute elastic and dielectric properties
- Role: scored (load-bearing)
- Action: Using the fitted potential, compute the elastic constants c11, c12, c44, the static and high-frequency permittivities ε_s and ε_∞, and the phonon frequencies (TO1, LO1, TO2, LO2, TO3, LO3) at the Γ point for cubic KNbO3 at 710 K.
- Output file: `/app/outputs/elastic_dielectric_properties.json`
- Format: json
- Contract: {"type":"object","properties":{"c11":{"type":"number"},"c12":{"type":"number"},"c44":{"type":"number"},"eps_s":{"type":"number"},"eps_inf":{"type":"number"},"phonon_frequencies":{"type":"array","items":{"type":"object","properties":{"mode":{"type":"string"},"frequency":{"type":"number"}},"required":["mode","frequency"]}}},"required":["c11","c12","c44","eps_s","eps_inf","phonon_frequencies"]}
- Scoring: scored by hidden verifier

### Step 3: Compute vacancy formation energies
- Role: scored (load-bearing)
- Action: Using the fitted potential, compute the formation energies of isolated oxygen, potassium and niobium vacancies in cubic KNbO3 at 710 K.
- Output file: `/app/outputs/vacancy_formation_energies.json`
- Format: json
- Contract: {"type":"object","properties":{"V_O":{"type":"number"},"V_K":{"type":"number"},"V_Nb":{"type":"number"}},"required":["V_O","V_K","V_Nb"]}
- Scoring: scored by hidden verifier

### Step 4: Compute oxygen vacancy migration energy
- Role: scored (load-bearing)
- Action: Using the fitted potential, determine the saddle-point configuration for an oxygen vacancy migrating via the interstitialcy mechanism and compute the migration barrier as the energy difference between the saddle point and the stable vacancy configuration.
- Output file: `/app/outputs/o_migration_energy.json`
- Format: json
- Contract: {"type":"object","properties":{"energy":{"type":"number"}},"required":["energy"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_dielectric_properties.json`
- `/app/outputs/vacancy_formation_energies.json`
- `/app/outputs/o_migration_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_dielectric_properties.json
- path: `/app/outputs/elastic_dielectric_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic constants, static and high-frequency permittivities, and Γ-point TO/LO phonon frequencies computed with the fitted shell-model potential.
- schema:
  - `type`: object
  - `required`:
    - `c11`: number (GPa)
    - `c12`: number (GPa)
    - `c44`: number (GPa)
    - `eps_s`: number (dimensionless)
    - `eps_inf`: number (dimensionless)
    - `phonon_frequencies`: array of objects with mode (string) and frequency (number, cm⁻¹)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `c11`: GPa
    - `c12`: GPa
    - `c44`: GPa
    - `eps_s`: dimensionless
    - `eps_inf`: dimensionless
    - `phonon_frequencies[].frequency`: cm⁻¹

### vacancy_formation_energies.json
- path: `/app/outputs/vacancy_formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of isolated O, K, and Nb vacancies.
- schema:
  - `type`: object
  - `required`:
    - `V_O`: number (eV)
    - `V_K`: number (eV)
    - `V_Nb`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `V_O`: eV
    - `V_K`: eV
    - `V_Nb`: eV

### o_migration_energy.json
- path: `/app/outputs/o_migration_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Oxygen vacancy migration energy computed via the interstitialcy mechanism.
- schema:
  - `type`: object
  - `required`:
    - `energy`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `energy`: eV

Notes: Only the standard (unpolarizable K⁺) potential I is required for the scored quantities; the polarizable variant (potential II) is optional. INDO calculations are entirely excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_dielectric_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c11": "number (GPa)",
          "c12": "number (GPa)",
          "c44": "number (GPa)",
          "eps_s": "number (dimensionless)",
          "eps_inf": "number (dimensionless)",
          "phonon_frequencies": "array of objects with mode (string) and frequency (number, cm⁻¹)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "c11": "GPa",
          "c12": "GPa",
          "c44": "GPa",
          "eps_s": "dimensionless",
          "eps_inf": "dimensionless",
          "phonon_frequencies[].frequency": "cm⁻¹"
        }
      },
      "description": "Elastic constants, static and high-frequency permittivities, and Γ-point TO/LO phonon frequencies computed with the fitted shell-model potential."
    },
    {
      "file": "vacancy_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V_O": "number (eV)",
          "V_K": "number (eV)",
          "V_Nb": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "V_O": "eV",
          "V_K": "eV",
          "V_Nb": "eV"
        }
      },
      "description": "Formation energies of isolated O, K, and Nb vacancies."
    },
    {
      "file": "o_migration_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "energy": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Oxygen vacancy migration energy computed via the interstitialcy mechanism."
    }
  ],
  "notes": "Only the standard (unpolarizable K⁺) potential I is required for the scored quantities; the polarizable variant (potential II) is optional. INDO calculations are entirely excluded."
}
```

## How you are scored
A hidden verifier evaluates your submitted artifacts. The potential_parameters.json file is checked only for structural correctness (required keys and types). The three property files (elastic_dielectric_properties.json, vacancy_formation_energies.json, o_migration_energy.json) are scored by comparing your reported values against hidden reference values using domain-appropriate tolerances. Each scored file contributes to an overall reward between 0 and 1. Simply reporting numbers is not sufficient; the workflow must produce the fitted potential and use it to generate the properties. The verifier operates independently and cannot be influenced by any text in your solution.
