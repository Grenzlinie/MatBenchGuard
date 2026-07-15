# DFT Calculation of Frenkel-Pair Formation Energies and Stability Trends in Silicon

## Problem background
Radiation-induced displacement damage in silicon creates Frenkel pairs (vacancy‑interstitial pairs), especially for low‑energy primary knock‑on recoils. The stability of these Frenkel pairs — whether they recombine, remain as bound pairs, or contribute to long‑lived defects — is believed to depend on the local Fermi level (doping type) and on the vacancy‑interstitial separation. Understanding these stabilities is crucial because they directly influence the post‑irradiation defect population and may underlie observed differences in damage rates between n‑type and p‑type silicon. This task computes the formation and binding energies of nine distinct Frenkel‑pair configurations in silicon for three charge states (+2, 0, −2) and determines their mechanical stability after structural relaxation, providing a quantitative picture of how charge state and separation distance affect FP energetics.

## Approach
The approach uses first‑principles DFT in the local density approximation (LDA) to perform total‑energy calculations and structural relaxations. A 3×3×3 simple‑cubic supercell of silicon (216 atoms, bulk lattice constant 5.39 Å) is employed. Reference systems — perfect bulk, an isolated vacancy, and an isolated tetrahedral interstitial — are relaxed first to obtain baseline total energies. Then nine symmetrically distinct initial Frenkel‑pair configurations are constructed, spanning vacancy‑interstitial separations from roughly 4 Å to 9 Å. For each configuration, three charge states are modeled by adjusting the net electron count (+2, 0, −2). The resulting total energies from the relaxed structures are used to compute formation energies (energy of the defected supercell relative to perfect bulk) and binding energies (the difference between the FP formation energy and the sum of the isolated vacancy and interstitial formation energies). The final relaxed geometries also yield a stability classification: each run is flagged as stable (FP remains intact), unstable (recombined to perfect crystal), or partially recombined (a non‑FP defect structure). All calculations are carried out with a plane‑wave DFT code and an available Vanderbilt ultrasoft pseudopotential for silicon.

## Reproduction target
Compute and report the formation energies and binding energies for all nine Frenkel‑pair configurations in the charge states +2, 0, and −2. Produce two scored comma‑separated value (CSV) files. The first file, `reference_energies.csv`, must contain the total energies and formation energies of the perfect bulk, isolated vacancy, and isolated interstitial. The second file, `FP_results_table.csv`, must list each FP configuration (configuration identifier, vacancy‑interstitial separation in Å, charge state, stability flag, total energy, formation energy, and binding energy). The stability values must reflect the outcome of the DFT relaxations. The goal is to obtain a complete data table that allows verification of how formation and binding energies vary with charge state and separation distance.

## Assets

- Silicon crystal structure (diamond, a=5.39 Å)
- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, ABINIT)
- Vanderbilt ultrasoft pseudopotential for Si (LDA)

## Workflow steps

### Step 1: Build silicon supercells
- Role: process
- Action: Construct a 3×3×3 simple cubic supercell of Si with 216 atoms and lattice constant 5.39 Å. Build structures for: perfect bulk, isolated vacancy, isolated tetrahedral interstitial, and nine symmetrically distinct Frenkel-pair configurations with vacancy-interstitial separations ranging from ~4 Å to ~9 Å. Generate input files for charge states +2, 0, and -2 by adjusting the net electron count.
- Evidence: `/app/outputs/supercell_coordinates.json`

### Step 2: DFT reference calculations for pristine and point-defect systems
- Role: process
- Action: Run DFT-LDA structural relaxations and total-energy calculations for perfect bulk Si, isolated vacancy, and isolated tetrahedral interstitial. Use a plane-wave code with an ultrasoft pseudopotential, converged kinetic energy cutoff, and appropriate k-point sampling.
- Evidence: `/app/outputs/ref_relax.log`

### Step 3: DFT calculations for Frenkel-pair configurations
- Role: process
- Action: For each of the nine initial FP configurations in charge states +2, 0, and -2, run DFT-LDA relaxations. Determine which configurations remain mechanically stable (do not spontaneously recombine). Classify each as stable, unstable (recombined to bulk), or partially recombined (non-FP defect).
- Evidence: `/app/outputs/fp_relax.log`

### Step 4: Compute reference defect formation energies
- Role: scored
- Action: From the DFT total energies of perfect bulk, isolated vacancy, and isolated interstitial, compute the formation energies: E_form(V) = E_tot(V) – E_tot(bulk) and E_form(I) = E_tot(I) – E_tot(bulk). Write results to reference_energies.csv.
- Output file: `/app/outputs/reference_energies.csv`
- Format: csv
- Contract: Columns: system (str: perfect_bulk/V/I), charge_state (int, 0 for all), total_energy_eV (float), formation_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Compute FP formation and binding energies and stability
- Role: scored (load-bearing)
- Action: For each FP configuration and charge state, compute formation energy E_form = E_tot(FP) – E_tot(bulk), and binding energy E_bind = E_form(V) + E_form(I) – E_form(FP). Compile the stability classification (stable/unstable/partially_recombined) from the DFT relaxation outcomes. Write all results to FP_results_table.csv.
- Output file: `/app/outputs/FP_results_table.csv`
- Format: csv
- Contract: Columns: config_id (str), separation_A (float), charge_state (int: +2, 0, -2), stability (str: stable/unstable/partially_recombined), total_energy_eV (float), formation_energy_eV (float), binding_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reference_energies.csv`
- `/app/outputs/FP_results_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reference_energies.csv
- path: `/app/outputs/reference_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Reference formation energies for the perfect bulk, isolated vacancy, and isolated tetrahedral interstitial computed from the DFT total energies. The formation energy for perfect_bulk is defined as 0 eV.
- schema:
  - `type`: table
  - `required_columns`: `system`, `charge_state`, `total_energy_eV`, `formation_energy_eV`
  - `units`:
    - `total_energy_eV`: eV
    - `formation_energy_eV`: eV

### FP_results_table.csv
- path: `/app/outputs/FP_results_table.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Formation energies, binding energies, and stability classifications for each of the nine Frenkel-pair configurations in three charge states (+2, 0, -2). The stability flags indicate whether the FP remained mechanically stable after DFT relaxation or spontaneously recombined.
- schema:
  - `type`: table
  - `required_columns`: `config_id`, `separation_A`, `charge_state`, `stability`, `total_energy_eV`, `formation_energy_eV`, `binding_energy_eV`
  - `units`:
    - `separation_A`: angstrom
    - `total_energy_eV`: eV
    - `formation_energy_eV`: eV
    - `binding_energy_eV`: eV

Notes: The checker will recompute formation and binding energies from the agent's submitted total energies and perfect_bulk reference. It will verify that formation energies of the isolated vacancy/interstitial are within a tolerance of expected values, that FP formation energies fall in a reasonable range, and that the submitted data follow physically expected patterns for Frenkel pairs in Si. The stability flags are also checked for consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reference_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "charge_state",
          "total_energy_eV",
          "formation_energy_eV"
        ],
        "units": {
          "total_energy_eV": "eV",
          "formation_energy_eV": "eV"
        }
      },
      "description": "Reference formation energies for the perfect bulk, isolated vacancy, and isolated tetrahedral interstitial computed from the DFT total energies. The formation energy for perfect_bulk is defined as 0 eV."
    },
    {
      "file": "FP_results_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "config_id",
          "separation_A",
          "charge_state",
          "stability",
          "total_energy_eV",
          "formation_energy_eV",
          "binding_energy_eV"
        ],
        "units": {
          "separation_A": "angstrom",
          "total_energy_eV": "eV",
          "formation_energy_eV": "eV",
          "binding_energy_eV": "eV"
        }
      },
      "description": "Formation energies, binding energies, and stability classifications for each of the nine Frenkel-pair configurations in three charge states (+2, 0, -2). The stability flags indicate whether the FP remained mechanically stable after DFT relaxation or spontaneously recombined."
    }
  ],
  "notes": "The checker will recompute formation and binding energies from the agent's submitted total energies and perfect_bulk reference. It will verify that formation energies of the isolated vacancy/interstitial are within a tolerance of expected values, that FP formation energies fall in a reasonable range, and that the submitted data follow physically expected patterns for Frenkel pairs in Si. The stability flags are also checked for consistency."
}
```

## How you are scored
Your work is scored by a hidden verifier that inspects the two CSV files under `/app/outputs`. The verifier recomputes formation and binding energies from the total energies you provide and checks that they are internally consistent. It then compares the values against expected numerical ranges and required trends (e.g., the relative stability of different charge states and the dependence of binding energy on separation). The stability flags are also checked for consistency with the submitted energies. Each of the scored stages (`reference_energies.csv` and `FP_results_table.csv`) is awarded a partial score, and the final reward is a weighted combination of those scores. Merely reporting numbers that are plausible or that match known literature values is not sufficient; the verifier evaluates whether your computed numbers follow the physically expected patterns and fall within acceptable ranges for a DFT‑LDA calculation of this type.
