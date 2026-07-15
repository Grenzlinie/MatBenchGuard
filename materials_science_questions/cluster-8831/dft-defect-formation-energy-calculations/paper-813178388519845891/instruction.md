# DFT Formation Energies and Elastic Constants of Defective OsN₂

## Problem background
Synthesized marcasite OsN₂ under high pressure and temperature displays a bulk modulus that is significantly lower than predictions from generalized gradient approximation (GGA) density functional theory. Typically, experimental elastic properties lie between GGA and local-density approximation (LDA) estimates, so the observed deviation raises questions about the real structure of the synthesized material. One hypothesis is that nitrogen vacancies or oxygen substitution impurities, commonly incorporated during high-pressure synthesis, may alter both the thermodynamic stability and the mechanical properties. A computational investigation of these defect structures is needed to clarify how such substitutions change formation energies and elastic constants, and to understand whether they can explain the discrepancy with experiment.

## Approach
The study is a first-principles DFT investigation. Three models of a marcasite OsN₂ 2×2×2 supercell are constructed: the pristine stoichiometric cell, a cell containing one nitrogen vacancy, and a cell in which one nitrogen atom is replaced by an oxygen atom (corresponding to approximately 3.1% defect concentration). The generalized gradient approximation in the Perdew–Burke–Ernzerhof form (GGA-PBE) is used throughout, together with the projector-augmented wave method for core electrons. For each model, the atomic positions are relaxed until forces and total energy changes are converged. Reference energies for bulk osmium (hexagonal close-packed), molecular N₂, and molecular O₂ are obtained in separate calculations. Using these, the formation energy per formula unit is computed for each supercell. The nine independent elastic constants are then calculated for each relaxed structure using the finite-strain stress method. Polycrystalline bulk modulus, shear modulus, Poisson's ratio, and the G/B ratio are derived from the elastic constants via the Voigt–Reuss–Hill averaging scheme. The quantities are compared across the three models to assess the effect of defects on stability and elasticity.

## Reproduction target
Produce two JSON files containing the GGA-PBE results for the three 2×2×2 supercell models:

1. `formation_energies.json` – formation energies (eV per formula unit) for the pristine cell, the N-vacancy cell, and the O-substitution cell.
2. `elastic_properties.json` – elastic constants C11 through C66 (in GPa) and the derived moduli (bulk modulus B, shear modulus G, Poisson's ratio ν, and the ratio G/B) for each of the same three models.

The agent must run the full DFT workflow (supercell construction, reference energies, geometry optimization, elastic-constant evaluation) and write the final aggregates to these files. No pre-existing DFT outputs are provided; all quantities must be recomputed.

## Assets

- Marcasite OsN₂ unit cell atomic positions and lattice parameters
- PAW pseudopotentials for Os, N, O: https://www.materialscloud.org/discover/sssp/table/precision
- Open-source DFT software (Quantum ESPRESSO): https://www.quantum-espresso.org/
- Reference structures for bulk Os (P6₃/mmc), N₂ and O₂ molecules
- Python packages numpy, scipy: numpy scipy

## Workflow steps

### Step 1: Construct supercell models
- Role: process
- Action: Build a 2×2×2 supercell from the orthorhombic marcasite OsN₂ unit cell. Create three variants: pristine c-OsN₂, N-vacancy (remove one N atom), and O-substitution (replace one N atom with O).
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Compute reference elemental energies
- Role: process
- Action: Using DFT (GGA-PBE, PAW pseudopotentials), compute total energies for bulk Os (P6₃/mmc), the N₂ molecule, and the O₂ molecule. Record the total energy per atom for Os and per molecule for N₂ and O₂.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: DFT geometry optimization of supercells
- Role: process
- Action: Relax the atomic positions of all three supercell models using DFT (GGA-PBE, PAW pseudopotentials) with convergence criteria on forces and energy. Obtain the final total DFT energy for each relaxed supercell.
- Evidence: `/app/outputs/relaxation_outputs.json`

### Step 4: Calculate formation energies
- Role: scored (load-bearing)
- Action: Compute the formation energy per formula unit for each relaxed supercell using E_form = (E_total - m·E_Os - (n/2)·E_N2 - (l/2)·E_O2) / (m+n+l), where m, n, l are the numbers of Os, N, O atoms. Write the three GGA values to formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {"c-OsN2_GGA": number, "N-vacancy_GGA": number, "O-substitution_GGA": number}
- Scoring: scored by hidden verifier

### Step 5: Calculate elastic constants and derived properties
- Role: scored
- Action: Apply the finite-strain method to each relaxed supercell to compute stress responses and extract the nine independent elastic constants C11, C12, C13, C22, C33, C44, C55, C66 using DFT (GGA-PBE). Derive polycrystalline bulk modulus B, shear modulus G, Poisson's ratio ν, and the ratio G/B via Voigt-Reuss-Hill averaging. Write the complete set for all three models to elastic_properties.json.
- Output file: `/app/outputs/elastic_properties.json`
- Format: json
- Contract: {"c-OsN2_GGA": {"C11": number, "C12": number, "C13": number, "C22": number, "C33": number, "C44": number, "C55": number, "C66": number, "B": number, "G": number, "v": number, "G_B": number}, "N-vacancy_GGA": {...}, "O-substitution_GGA": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/elastic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: GGA-PBE formation energies (eV per formula unit) for the three 2×2×2 supercell models: c-OsN₂, N-vacancy (3.1% concentration), and O-substitution (3.1% concentration).
- schema:
  - `type`: object
  - `required`:
    - `c-OsN2_GGA`: number
    - `N-vacancy_GGA`: number
    - `O-substitution_GGA`: number
  - `items`: object
  - `required_columns`:
  - `units`: object

### elastic_properties.json
- path: `/app/outputs/elastic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: GGA-PBE elastic constants (Cij in GPa), bulk modulus B, shear modulus G, Poisson's ratio ν, and G/B for the three 2×2×2 supercell models.
- schema:
  - `type`: object
  - `required`:
    - `c-OsN2_GGA`: object
    - `N-vacancy_GGA`: object
    - `O-substitution_GGA`: object
  - `items`:
    - `C11`: number
    - `C12`: number
    - `C13`: number
    - `C22`: number
    - `C33`: number
    - `C44`: number
    - `C55`: number
    - `C66`: number
    - `B`: number
    - `G`: number
    - `v`: number
    - `G_B`: number
  - `required_columns`:
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C22`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C55`: GPa
    - `C66`: GPa
    - `B`: GPa
    - `G`: GPa
    - `v`: dimensionless
    - `G_B`: dimensionless

Notes: Scoring is hidden reference_match against paper-reported GGA values for 2×2×2 supercells (Table 1 formation energies, Table 2 elastic constants). The agent must compute and report the quantities; the checker compares with appropriate tolerances. LDA values and higher concentrations are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c-OsN2_GGA": "number",
          "N-vacancy_GGA": "number",
          "O-substitution_GGA": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "GGA-PBE formation energies (eV per formula unit) for the three 2×2×2 supercell models: c-OsN₂, N-vacancy (3.1% concentration), and O-substitution (3.1% concentration)."
    },
    {
      "file": "elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c-OsN2_GGA": "object",
          "N-vacancy_GGA": "object",
          "O-substitution_GGA": "object"
        },
        "items": {
          "C11": "number",
          "C12": "number",
          "C13": "number",
          "C22": "number",
          "C33": "number",
          "C44": "number",
          "C55": "number",
          "C66": "number",
          "B": "number",
          "G": "number",
          "v": "number",
          "G_B": "number"
        },
        "required_columns": [],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C22": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C55": "GPa",
          "C66": "GPa",
          "B": "GPa",
          "G": "GPa",
          "v": "dimensionless",
          "G_B": "dimensionless"
        }
      },
      "description": "GGA-PBE elastic constants (Cij in GPa), bulk modulus B, shear modulus G, Poisson's ratio ν, and G/B for the three 2×2×2 supercell models."
    }
  ],
  "notes": "Scoring is hidden reference_match against paper-reported GGA values for 2×2×2 supercells (Table 1 formation energies, Table 2 elastic constants). The agent must compute and report the quantities; the checker compares with appropriate tolerances. LDA values and higher concentrations are excluded."
}
```

## How you are scored
A hidden verifier, provided with a copy of the paper’s own GGA values, reads your submitted `formation_energies.json` and `elastic_properties.json`. It first checks that the files are valid JSON and contain all required fields. Then, for each numerical quantity, it compares your reported value to a hidden reference value using appropriate tolerances. A score is computed based on how closely each quantity matches the reference, with penalties increasing for larger deviations. In addition, the verifier checks that the relative ordering of the formation energies among the three models obeys a required trend (derived from physical expectations). The final reward is a weighted combination of the formation-energy and elastic-property checks. Submitting arbitrary numbers without actually executing the DFT computations will not achieve a competitive score.
