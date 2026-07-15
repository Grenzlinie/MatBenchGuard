# Zeolite Stability from Lattice Energy Minimization

## Problem background
Zeolites are microporous aluminosilicate minerals widely used in catalysis, gas separation, and ion exchange. Understanding their thermodynamic stability is crucial for guiding synthesis and predicting performance. For a given framework composition (e.g., pure silica), the most stable structure is the one with the lowest lattice energy. Lattice energy minimization is a computational method that finds the minimum of the potential energy surface by relaxing both atomic positions and unit‑cell parameters, using a specified interatomic potential. This task asks you to compute and compare the lattice energies per SiO₂ unit for five important siliceous zeolites, thereby determining their relative stabilities.

## Approach
The calculations employ a formal‑charge ionic potential model that includes: (i) a Coulomb term between all ion pairs, (ii) a Buckingham short‑range repulsion plus van der Waals attraction (`A exp(-r/ρ) - C/r⁶`), and (iii) a harmonic bond‑bending term for O‑Si‑O angles (equilibrium angle 109.47°). Two variants are considered:
- **Rigid ion**: each ion carries a fixed formal charge, and there is no polarizability.
- **Shell model**: oxygen ions are split into a core and a shell, connected by a harmonic spring; this accounts for ionic polarizability.

The interatomic parameters (A, ρ, C, charges, spring constant, bond‑bending force constant) were originally derived by fitting to the structure and properties of α‑quartz; they are available in a published reference (Jackson & Catlow, 1988). The agent must obtain these parameters and set up both potential models.

A constant‑pressure energy minimization (Newton‑Raphson) is then performed for each of five pure‑silica frameworks: faujasite, zeolite A, mordenite, silicalite (the MFI framework), and α‑quartz. The lattice energy per SiO₂ unit is extracted from each relaxed structure. By comparing the energies, the relative stability of the zeolites can be ranked; α‑quartz serves as a dense‑phase reference.

## Reproduction target
Your task is to produce a single JSON file, `lattice_energies.json`, containing exactly ten entries—one for each of the five zeolites under both the rigid‑ion and shell‑model potentials. Each entry must report the minimum lattice energy per SiO₂ unit in eV, using the following zeolite identifiers: `faujasite`, `zeolite_A`, `mordenite`, `silicalite`, and `alpha_quartz`. The model field must be either `rigid_ion` or `shell_model`.

The absolute energy values will be compared against a hidden reference, and the relative ordering of the shell‑model energies among the zeolites (i.e., excluding α‑quartz) will be audited to ensure it follows the expected stability trend. No further outputs are scored.

## Assets

- GULP (General Utility Lattice Program): https://github.com/artsyfartsy/gulp
- IZA Zeolite Structure Database: http://www.iza-structure.org/databases/
- Jackson & Catlow (1988) – Si-O potential parameters: 10.1080/08927028708080923

## Workflow steps

### Step 1: Acquire crystal structures and interatomic potential parameters
- Role: process
- Action: Download the pure-silica crystallographic data (.cif files) for faujasite, zeolite A, mordenite, silicalite (MFI framework), and alpha-quartz from the IZA database. Obtain the Si-O interatomic potential parameters (Buckingham A, rho, C; formal charges; core-shell spring constant; O-Si-O bond-bending force constant k with equilibrium angle 109.47°) from Jackson & Catlow (1988). Prepare input files for both rigid-ion (no shell) and shell-model descriptions.
- Evidence: `/app/outputs/structures_and_parameters.log`

### Step 2: Compute lattice energies and report results
- Role: scored (load-bearing)
- Action: Using GULP, perform constant-pressure lattice energy minimization (Newton-Raphson) for each of the five zeolites under both rigid-ion and shell-model potentials. Extract the final minimum lattice energy per SiO2 unit (in eV) for each run. Collect the ten values into a single JSON file.
- Output file: `/app/outputs/lattice_energies.json`
- Format: json
- Contract: A JSON array of objects, each with keys: 'zeolite' (string, one of: faujasite, zeolite_A, mordenite, silicalite, alpha_quartz), 'model' (string: 'rigid_ion' or 'shell_model'), 'energy_per_SiO2' (float, in eV). The array must contain exactly 10 entries, covering all five zeolites under both models.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energies.json
- path: `/app/outputs/lattice_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Minimum lattice energies per SiO2 unit for the five zeolites under both rigid-ion and shell-model potentials. Absolute energy values will be compared against the paper's reported numbers with a hidden tolerance; ordering of shell-model energies will be checked for correct ranking (silicalite most stable, then mordenite, zeolite_A, faujasite).
- schema:
  - `type`: array
  - `minItems`: 10
  - `maxItems`: 10
  - `items`:
    - `type`: object
    - `required`: `zeolite`, `model`, `energy_per_SiO2`
    - `properties`:
      - `zeolite`:
        - `type`: string
        - `enum`: `faujasite`, `zeolite_A`, `mordenite`, `silicalite`, `alpha_quartz`
      - `model`:
        - `type`: string
        - `enum`: `rigid_ion`, `shell_model`
      - `energy_per_SiO2`:
        - `type`: number
        - `units`: eV

Notes: Scoring for lattice_energies.json uses exact_match with an absolute tolerance for each energy plus a structural ordering check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "minItems": 10,
        "maxItems": 10,
        "items": {
          "type": "object",
          "required": [
            "zeolite",
            "model",
            "energy_per_SiO2"
          ],
          "properties": {
            "zeolite": {
              "type": "string",
              "enum": [
                "faujasite",
                "zeolite_A",
                "mordenite",
                "silicalite",
                "alpha_quartz"
              ]
            },
            "model": {
              "type": "string",
              "enum": [
                "rigid_ion",
                "shell_model"
              ]
            },
            "energy_per_SiO2": {
              "type": "number",
              "units": "eV"
            }
          }
        }
      },
      "description": "Minimum lattice energies per SiO2 unit for the five zeolites under both rigid-ion and shell-model potentials. Absolute energy values will be compared against the paper's reported numbers with a hidden tolerance; ordering of shell-model energies will be checked for correct ranking (silicalite most stable, then mordenite, zeolite_A, faujasite)."
    }
  ],
  "notes": "Scoring for lattice_energies.json uses exact_match with an absolute tolerance for each energy plus a structural ordering check."
}
```

## How you are scored
A hidden verifier will read your submitted `lattice_energies.json`. It will:
- check that the file is a valid JSON array with exactly 10 items and correct keys;
- compare each energy value to a reference value within a hidden tolerance (the comparison rewards values that are close to the expected numbers);
- verify that the shell‑model energies for the zeolites (faujasite, zeolite_A, mordenite, silicalite) show the correct relative stability ordering.

The final reward is a weighted combination of these checks, with the energy‑accuracy check carrying the most weight. Simply reporting numbers without actually performing the minimization will not satisfy the verifier; the output must be generated by your computational pipeline following the steps above. No tolerance or reference value is disclosed here.
