# Charge-state dependence of Frenkel pair stability in silicon

## Problem background
Silicon-based devices exposed to radiation suffer displacement damage, and experiments show that p‑type Si often exhibits a lower apparent damage rate than n‑type Si. This dopant‑type dependence correlates with the fraction of damage caused by low‑energy primary knock‑on atom (PKA) recoils, whose primary products are isolated vacancy‑interstitial pairs, or Frenkel pairs (FPs). To understand the atomic‑scale origin of this effect, first‑principles density functional theory (DFT) calculations are used to study how the stability of Frenkel pairs depends on local charge state (a proxy for effective doping) and on vacancy‑interstitial separation distance. In this task you will compute, for a set of FP configurations under different charge states, which ones remain stable versus recombining, and determine their formation energies and binding energies.

## Approach
The calculations employ DFT within the local density approximation (LDA) and Vanderbilt ultrasoft pseudopotentials. You will construct a 3×3×3 simple‑cubic Si supercell containing 216 atoms (lattice constant 5.39 Å) and generate nine symmetrically distinct initial configurations of a vacancy and a tetrahedral interstitial with different vacancy–interstitial separations. For each configuration, perform geometry relaxations for charge states +2, 0, and –2 using an open‑source plane‑wave DFT code (e.g. Quantum ESPRESSO, ABINIT, or GPAW). In addition, compute the total energy of an isolated vacancy and an isolated tetrahedral interstitial in the same supercell. After relaxation, a configuration is classified as stable if it retains a distinct vacancy‑interstitial pair; if it relaxes back to perfect bulk Si it is unstable. From the total energies of stable FPs and isolated defects, the formation energy is computed as E(FP) – E(bulk) and the binding energy as E(vac) + E(int) – E(FP). The results are collected in two scored CSV files as described in the workflow steps.

## Reproduction target
Classify the stability of nine Frenkel pair configurations for charge states +2, 0, and –2 and compute the formation energy and binding energy of every stable configuration. Report the stability classification in stability_table.csv (one row per configuration per charge state, with configuration ID, charge state, separation distance, and a boolean stability flag) and the energies in energies_summary.csv (one row for the isolated vacancy, one for the isolated interstitial, and one row per stable FP configuration with its charge state, giving total energy, formation energy, and binding energy). The hidden verifier will compare your stability pattern and the ranges of formation and binding energies to a reference that represents the expected physical result.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Silicon LDA ultrasoft pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct Frenkel Pair configurations
- Role: process
- Action: Construct a 3×3×3 simple-cubic Si supercell (216 atoms, lattice constant 5.39 Å). Generate nine symmetrically distinct initial configurations of a vacancy and a tetrahedral interstitial with different vacancy–interstitial separation distances, covering the range of sizes studied in the paper. Save the atomic positions for each configuration.
- Evidence: `/app/outputs/fp_geometries_info.txt`

### Step 2: DFT relaxations and total energy calculations
- Role: process
- Action: For each FP configuration and for isolated vacancy and interstitial, perform DFT geometry relaxations using an LDA functional and ultrasoft pseudopotentials, with an open-source code (e.g., Quantum ESPRESSO). For FP configurations, relax for charge states +2, 0, -2. Record total energies and whether the FP remained stable or recombined. Save a log file documenting the calculations.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 3: Report stability table
- Role: scored
- Action: From the DFT results, generate a CSV file listing for each of the nine configurations and each charge state whether the FP is stable (true) or has recombined (false). Include config ID, charge state, separation distance, and stability.
- Output file: `/app/outputs/stability_table.csv`
- Format: csv
- Contract: config_id (int), charge_state (int, +2/0/-2), separation_A (float), stable (bool)
- Scoring: scored by hidden verifier

### Step 4: Report energies summary
- Role: scored (load-bearing)
- Action: From the DFT total energies of stable FPs and isolated defects, compute formation energies (E_FP - E_bulk) and binding energies (E_vac + E_int - E_FP). Generate a CSV file with columns: type (vacancy, interstitial, FP), config_id, charge_state, total_energy_eV, formation_energy_eV, binding_energy_eV. Include one row for isolated vacancy and one for isolated interstitial, and one row for each stable FP configuration with its charge state.
- Output file: `/app/outputs/energies_summary.csv`
- Format: csv
- Contract: type (str, one of 'vacancy','interstitial','FP'), config_id (int, nullable), charge_state (int, nullable), total_energy_eV (float), formation_energy_eV (float, nullable), binding_energy_eV (float, nullable)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stability_table.csv`
- `/app/outputs/energies_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stability_table.csv
- path: `/app/outputs/stability_table.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Per-configuration stability classification across charge states. Checker verifies structural trend: all 9 configurations stable at +2, progressively fewer at 0 (only the three largest remain stable), only the largest (~8.1 Å) stable at -2.
- schema:
  - `type`: table
  - `required_columns`: `config_id`, `charge_state`, `separation_A`, `stable`
  - `units`:
    - `separation_A`: angstrom
    - `stable`: boolean

### energies_summary.csv
- path: `/app/outputs/energies_summary.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation and binding energies for stable Frenkel pairs (one row per stable configuration per charge state) and for isolated vacancy and interstitial. Checker extracts min/max formation energy range and min/max binding energy range and checks they fall within the paper's reported ranges with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `type`, `config_id`, `charge_state`, `total_energy_eV`, `formation_energy_eV`, `binding_energy_eV`
  - `notes`: config_id and charge_state are nullable for isolated defects; formation_energy_eV and binding_energy_eV are nullable for isolated defects.

Notes: The stability table reports the classification from the geometry relaxations. The energies summary reports the computed formation and binding energies. Both files are required; the checker verifies the stability trend and energy ranges against the paper's reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stability_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "config_id",
          "charge_state",
          "separation_A",
          "stable"
        ],
        "units": {
          "separation_A": "angstrom",
          "stable": "boolean"
        }
      },
      "description": "Per-configuration stability classification across charge states. Checker verifies structural trend: all 9 configurations stable at +2, progressively fewer at 0 (only the three largest remain stable), only the largest (~8.1 Å) stable at -2."
    },
    {
      "file": "energies_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "type",
          "config_id",
          "charge_state",
          "total_energy_eV",
          "formation_energy_eV",
          "binding_energy_eV"
        ],
        "notes": "config_id and charge_state are nullable for isolated defects; formation_energy_eV and binding_energy_eV are nullable for isolated defects."
      },
      "description": "Formation and binding energies for stable Frenkel pairs (one row per stable configuration per charge state) and for isolated vacancy and interstitial. Checker extracts min/max formation energy range and min/max binding energy range and checks they fall within the paper's reported ranges with tolerances."
    }
  ],
  "notes": "The stability table reports the classification from the geometry relaxations. The energies summary reports the computed formation and binding energies. Both files are required; the checker verifies the stability trend and energy ranges against the paper's reported values."
}
```

## How you are scored
A hidden verifier inspects your output files. For stability_table.csv it checks that your stability pattern (which configurations are stable at each charge state) matches a reference qualitative trend. For energies_summary.csv the verifier computes the minimum and maximum formation energy among your stable FP entries and verifies that this range falls within a hidden tolerance interval; it does the same for the binding energy range. Both the stability pattern and the energy ranges must be satisfied to receive full credit. The verifier does not read the source paper; it compares your computed results against a hidden reference. You must obtain your results by executing the described DFT workflow rather than by embedding known numbers.
