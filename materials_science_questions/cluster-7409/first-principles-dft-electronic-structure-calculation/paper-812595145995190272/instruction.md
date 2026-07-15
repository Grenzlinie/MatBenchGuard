# First-principles calculation of phonon-derived crossover temperature decrease in Sc-substituted λ-Ti₃O₅

## Problem background
Renewable heat storage using phase-change ceramics can recover low-temperature waste heat. This task focuses on scandium-substituted lambda-Ti3O5 (λ-Ti3O5) as a potential heat-storage material. First-principles DFT+phonon Gibbs free energy calculations are employed to study the λ–β solid-phase transition. The objective is to quantify the change in the λ–β crossover temperature (the temperature at which the Gibbs free energies of the two phases are equal) when a small amount of Sc (≈3 at%) is substituted into Ti3O5, relative to pure Ti3O5.

## Approach
The crossover temperature is approached by computing the Gibbs free energy difference ΔG(T) = G_λ − G_β as a function of temperature for both pure Ti3O5 and Sc-substituted Ti3O5 (≈3 at% Sc, achieved by replacing 1 Ti atom by Sc in a 1×3×1 supercell containing 36 Ti atoms). Density-functional theory (DFT) with an open-source plane-wave code (Quantum ESPRESSO) is used for geometry optimization and force calculations. Vibrational free energies are then obtained via the Phonopy package, which evaluates the phonon density of states and integrates to yield G_λ and G_β at a range of temperatures. The crossover temperature T_p is determined from the condition ΔG(T_p) = 0, and the relative change between the two compositions is computed as (Tp_pure − Tp_substituted) / Tp_pure × 100%.

## Reproduction target
Produce the following artifacts by executing the full DFT+phonon workflow:

1. `delta_G_data.csv` – a CSV file with columns `composition`, `temperature_K`, and `delta_G_eV` containing ΔG(T) curves for both pure and Sc-substituted systems over a temperature range that covers the expected crossover.

2. `crossover_temperatures.json` – a JSON object with the computed crossover temperatures (`Tp_pure_K`, `Tp_Sc_substituted_K`) and the `relative_decrease_percent`.

The result must be derived from the complete first-principles pipeline; merely reporting a number without the intermediate data is not sufficient.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- Pseudopotentials (Ti, O, Sc): https://www.materialscloud.org/discover/sssp/
- Crystal structures of λ-Ti₃O₅ and β-Ti₃O₅

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct (1×3×1) supercells for λ-Ti₃O₅, β-Ti₃O₅, and Sc-substituted λ and β phases (replace one Ti atom by Sc per 36 Ti) using published experimental structures.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: Relax atomic positions and lattice parameters of the four supercells using DFT (e.g., Quantum ESPRESSO).
- Evidence: `/app/outputs/relaxed_energies.txt`

### Step 3: Phonon free energy curves
- Role: scored
- Action: Perform phonon calculations with Phonopy on each relaxed supercell to obtain vibrational free energies. Compute ΔG(T) = G_λ − G_β for pure and Sc-substituted systems and write the data as a CSV file.
- Output file: `/app/outputs/delta_G_data.csv`
- Format: csv
- Contract: composition: str, temperature_K: float, delta_G_eV: float
- Scoring: scored by hidden verifier

### Step 4: Crossover temperature and decrease
- Role: scored (load-bearing)
- Action: From the ΔG(T) data, find the temperature where ΔG=0 for each composition, compute the relative decrease, and write the results to crossover_temperatures.json.
- Output file: `/app/outputs/crossover_temperatures.json`
- Format: json
- Contract: {"Tp_pure_K": float, "Tp_Sc_substituted_K": float, "relative_decrease_percent": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_G_data.csv`
- `/app/outputs/crossover_temperatures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_G_data.csv
- path: `/app/outputs/delta_G_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: ΔG(T) data for pure and Sc-substituted Ti₃O₅; must show sign change near the crossover temperatures.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `temperature_K`, `delta_G_eV`
  - `column_types`:
    - `composition`: str
    - `temperature_K`: float
    - `delta_G_eV`: float
  - `units`:
    - `temperature_K`: Kelvin
    - `delta_G_eV`: electronvolts

### crossover_temperatures.json
- path: `/app/outputs/crossover_temperatures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed crossover temperatures for pure and Sc-substituted Ti₃O₅, and the relative decrease.
- schema:
  - `type`: object
  - `required`:
    - `Tp_pure_K`: float
    - `Tp_Sc_substituted_K`: float
    - `relative_decrease_percent`: float
  - `units`:
    - `Tp_pure_K`: Kelvin
    - `Tp_Sc_substituted_K`: Kelvin
    - `relative_decrease_percent`: percent

Notes: The main reward is carried by crossover_temperatures.json; delta_G_data.csv provides supporting structural evidence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_G_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "temperature_K",
          "delta_G_eV"
        ],
        "column_types": {
          "composition": "str",
          "temperature_K": "float",
          "delta_G_eV": "float"
        },
        "units": {
          "temperature_K": "Kelvin",
          "delta_G_eV": "electronvolts"
        }
      },
      "description": "ΔG(T) data for pure and Sc-substituted Ti₃O₅; must show sign change near the crossover temperatures."
    },
    {
      "file": "crossover_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Tp_pure_K": "float",
          "Tp_Sc_substituted_K": "float",
          "relative_decrease_percent": "float"
        },
        "units": {
          "Tp_pure_K": "Kelvin",
          "Tp_Sc_substituted_K": "Kelvin",
          "relative_decrease_percent": "percent"
        }
      },
      "description": "Computed crossover temperatures for pure and Sc-substituted Ti₃O₅, and the relative decrease."
    }
  ],
  "notes": "The main reward is carried by crossover_temperatures.json; delta_G_data.csv provides supporting structural evidence."
}
```

## How you are scored
A hidden verifier checks your submitted artifacts and combines the evidence into a final reward between 0 and 1.

**Primary reward** (crossover_temperatures.json): the checker compares your `relative_decrease_percent` to a hidden reference value using a tolerance that accounts for systematic differences between DFT codes (choice of pseudopotentials, exchange‑correlation functional, phonon convergence parameters). A result that meets or exceeds the expected accuracy earns full credit; the score degrades only as the deviation from the reference grows beyond an acceptable window.

**Secondary consistency check** (delta_G_data.csv, lower weight): the verifier confirms that the ΔG(T) curves exhibit a sign change (crossing zero) near the crossover temperatures you report, demonstrating a coherent thermodynamic calculation.

**Important:** simply copying a known literature value without producing the required raw computation artifacts will be detected and will not earn the full reward; the checker evaluates both the reported numbers and their consistency with the intermediate data you provide.
