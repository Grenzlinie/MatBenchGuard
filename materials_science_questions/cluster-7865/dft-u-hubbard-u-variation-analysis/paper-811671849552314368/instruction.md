# DFT+U Hubbard U Variation and Exchange Parameter Analysis for Double-Perovskites

## Problem background
The ordered double-perovskites Sr2CuOsO6 and Sr2NiOsO6 each contain alternating 3d (Cu/Ni) and 5d (Os) transition-metal ions in corner-sharing octahedra. Experiments show they are magnetic insulators with distinct dominant magnetic interactions (antiferromagnetic for the Cu compound, ferromagnetic for the Ni compound), but standard density functional theory without Hubbard corrections tends to predict metallic behavior. This task addresses the discrepancy by systematically exploring the on-site Coulomb repulsion U applied to the 3d and 5d ions to find the conditions that reproduce insulating states, and to extract the effective spin exchange constants that govern their magnetic interactions.

## Approach
Use an open-source DFT code implementing the Dudarev DFT+U formalism (e.g., Quantum ESPRESSO) with GGA-PBE and standard pseudopotentials. For Sr2CuOsO6, compute total energies and band-gap presence for the spin configurations AF1, AF2, AF3 while scanning U_Cu = 3, 4, 5, 6 eV and U_Os = 2, 3, 4 eV. For Sr2NiOsO6, fix U_Os = 4 eV and vary U_Ni = 3, 4, 5, 6 eV for the FM, G-type, A-type, and C-type spin arrangements. Record raw total energies and gap indicators. Then, at U_M = 6 eV and U_Os = 4 eV, calculate the total energies of eight ordered spin states (FM, AF1–AF7) for both compounds. From these eight-state energies, apply an energy-mapping method based on the spin Hamiltonian for mixed-spin dimers to extract the seven effective nearest-neighbour exchange constants J1–J7.

## Reproduction target
Produce two scored artifacts. First, a band gap summary table (band_gap_summary.csv) that reports the raw total energy and whether a band gap is present for every (U_M, U_Os) combination and spin state computed in the parameter scans for both Sr2CuOsO6 and Sr2NiOsO6. Second, extract the effective spin exchange constants J1–J7 for each compound from the eight-state total energies and record them in spin_exchange_constants.csv.

## Assets

- Sr2CuOsO6 experimental crystal structure: https://doi.org/10.1016/j.jssc.2007.11.001
- Sr2NiOsO6 experimental crystal structure: https://doi.org/10.1021/ic048726f
- Open-source DFT code (Quantum ESPRESSO): https://www.quantum-espresso.org/
- Standard pseudopotentials (SSSP or PSLibrary): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT+U parameter scan for Sr2CuOsO6
- Role: process
- Action: Perform DFT+U calculations for the experimental Sr2CuOsO6 structure using U_Cu = 3,4,5,6 eV and U_Os = 2,3,4 eV for the spin states AF1, AF2, AF3. For each combination, save total energy and band gap indicator.
- Evidence: `/app/outputs/CuOsO6_raw_energies.json`

### Step 2: DFT+U calculations for Sr2NiOsO6
- Role: process
- Action: Perform DFT+U calculations for the experimental Sr2NiOsO6 structure with U_Os = 4 eV, U_Ni = 3,4,5,6 eV for the spin states FM, G-type, A-type, C-type. Save total energies and gap indicators.
- Evidence: `/app/outputs/NiOsO6_raw_energies.json`

### Step 3: Compile band gap summary
- Role: scored (load-bearing)
- Action: Aggregate the total energies and band-gap indications from the two parameter scans into a single summary table. For each calculation, report the raw total energy and whether a band gap is present.
- Output file: `/app/outputs/band_gap_summary.csv`
- Format: csv
- Contract: compound (string), U_M (float, eV), U_Os (float, eV), spin_state (string), total_energy_eV (float, eV), has_gap (string, yes/no)
- Scoring: scored by hidden verifier

### Step 4: Eight-spin-state total energies
- Role: process
- Action: Run DFT+U calculations for both Sr2CuOsO6 and Sr2NiOsO6 using U_M = 6 eV, U_Os = 4 eV for the eight ordered spin states (FM, AF1, AF2, AF3, AF4, AF5, AF6, AF7). Save the total energy of each state.
- Evidence: `/app/outputs/eight_state_energies.csv`

### Step 5: Extract spin exchange constants
- Role: scored (load-bearing)
- Action: From the eight-state total energies, compute the effective spin exchange constants J1-J7 for each compound using the spin Hamiltonian energy expressions and the energy mapping method.
- Output file: `/app/outputs/spin_exchange_constants.csv`
- Format: csv
- Contract: compound (string), exchange_path (string), J_eff (float, meV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_summary.csv`
- `/app/outputs/spin_exchange_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_summary.csv
- path: `/app/outputs/band_gap_summary.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Summarized DFT+U results: total energies and band-gap presence for Sr2CuOsO6 and Sr2NiOsO6 across the surveyed Hubbard U values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `U_M`, `U_Os`, `spin_state`, `total_energy_eV`, `has_gap`
  - `units`:
    - `U_M`: eV
    - `U_Os`: eV
    - `total_energy_eV`: eV

### spin_exchange_constants.csv
- path: `/app/outputs/spin_exchange_constants.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Effective spin exchange constants (J1-J7) extracted from DFT+U total energies of eight ordered spin states.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `exchange_path`, `J_eff`
  - `units`:
    - `J_eff`: meV

Notes: The raw DFT outputs (CuOsO6_raw_energies.json, NiOsO6_raw_energies.json, eight_state_energies.csv) are required intermediate evidence but are not directly scored. The checker verifies structural patterns (gap presence and ground-state ordering for the band gap summary, sign consistency for exchange constants) against hidden reference criteria.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "U_M",
          "U_Os",
          "spin_state",
          "total_energy_eV",
          "has_gap"
        ],
        "units": {
          "U_M": "eV",
          "U_Os": "eV",
          "total_energy_eV": "eV"
        }
      },
      "description": "Summarized DFT+U results: total energies and band-gap presence for Sr2CuOsO6 and Sr2NiOsO6 across the surveyed Hubbard U values."
    },
    {
      "file": "spin_exchange_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "exchange_path",
          "J_eff"
        ],
        "units": {
          "J_eff": "meV"
        }
      },
      "description": "Effective spin exchange constants (J1-J7) extracted from DFT+U total energies of eight ordered spin states."
    }
  ],
  "notes": "The raw DFT outputs (CuOsO6_raw_energies.json, NiOsO6_raw_energies.json, eight_state_energies.csv) are required intermediate evidence but are not directly scored. The checker verifies structural patterns (gap presence and ground-state ordering for the band gap summary, sign consistency for exchange constants) against hidden reference criteria."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output artifact. It recomputes relative energies and band-gap assignments from your submitted raw data, solves the exchange constant equations from your eight‑state energies, and compares the resulting patterns and numerical values against hidden reference criteria. The final reward is a weighted sum over the scored stages; simply reporting expected numbers without executing the required computations will not yield a high score.
