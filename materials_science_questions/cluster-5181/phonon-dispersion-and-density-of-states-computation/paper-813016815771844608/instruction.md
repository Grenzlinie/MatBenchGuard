# Pressure-dependent effective bond orders and phonon frequencies of RDX

## Problem background
Understanding how mechanical compression affects electron distribution within energetic molecules is crucial for predicting the initiation and safety of high explosives like RDX. Vibrational frequency shifts (Raman blue shifts) observed under shock loading are thought to arise from intramolecular electron redistribution (IER) — electrons moving from some bonds to others. First-principles density functional theory (DFT) can probe this by computing pressure-dependent effective bond orders and phonon frequencies, providing a window into which bonds donate or accept electrons. This task reproduces the DFT analysis that identifies electron donor and acceptor bonds in α‑RDX under hydrostatic pressure using open‑source tools.

## Approach
The reproduction uses plane‑wave density functional theory with the PBE exchange‑correlation functional and Grimme D3 dispersion correction. Starting from the known α‑RDX crystal structure (space group Pbca), the crystal is fully relaxed at hydrostatic pressures of 0, 0.5, and 1.0 GPa. For each relaxed geometry, effective bond orders are computed from the charge density using the DDEC6 method, focusing on representative C–H, C–N, N–N, and N–O bonds. In parallel, finite‑displacement calculations are performed to obtain zone‑centre phonon frequencies. The resulting pressure‑dependent bond orders and phonon frequencies capture the competition between bond compression and charge redistribution. The comparison of trends across bond types reveals which bonds act as electron donors or acceptors under pressure, and whether the lattice stiffens uniformly. The workflow is fully automatable using open‑source codes (Quantum ESPRESSO, PHONOPY, DDEC6/Chargemol) and a public crystal structure.

## Reproduction target
Produce two CSV tables documenting the pressure‑dependent effective bond orders and zone‑centre phonon frequencies of α‑RDX at hydrostatic pressures of 0, 0.5, and 1.0 GPa. The first table must list for each pressure the effective bond order of several representative bonds (C–H, C–N, equatorial/axial N–N and N–O). The second table must list all zone‑centre phonon mode frequencies (in cm⁻¹) at each pressure. The target is to compute these quantities and the trends they exhibit with increasing pressure, specifically: whether each bond order increases or decreases, and whether all phonon frequencies shift upwards. The output files must follow the prescribed schema.

## Assets

- α‑RDX crystal structure (space group Pbca): https://www.ccdc.cam.ac.uk/structures/search?access=public&id=CHXZIR
- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- PHONOPY: https://phonopy.github.io/phonopy/
- DDEC6 / Chargemol: https://sourceforge.net/projects/ddec/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Obtain α‑RDX crystal structure
- Role: process
- Action: Fetch the α‑RDX crystal structure (space group Pbca) from a public crystallographic database (CSD entry CHXZIR or COD ID 1011103) and prepare the atomic coordinates and unit cell parameters.
- Evidence: `/app/outputs/crystal_structure.cif`

### Step 2: DFT structural relaxation under hydrostatic pressure
- Role: process
- Action: Using an open‑source DFT code (e.g., Quantum ESPRESSO) with the PBE functional, dispersion correction (Grimme D3), and standard pseudopotentials, relax the α‑RDX crystal at hydrostatic pressures of 0, 0.5, and 1.0 GPa. Output relaxed structures and charge density files.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 3: Compute pressure-dependent effective bond orders
- Role: scored (load-bearing)
- Action: Use DDEC6 (Chargemol) on the charge density outputs from the relaxed structures at 0, 0.5, and 1.0 GPa to compute effective bond orders. Tabulate the bond orders for representative C–H, C–N, N–N, and N–O bonds. Write the table to effective_bond_orders.csv.
- Output file: `/app/outputs/effective_bond_orders.csv`
- Format: csv
- Contract: Columns: pressure_GPa (float), bond_label (str), effective_bond_order (float). Must contain rows for pressures 0, 0.5, and 1.0 for each representative bond.
- Scoring: scored by hidden verifier

### Step 4: Compute zone‑centre phonon frequencies
- Role: scored
- Action: Perform finite‑displacement calculations on the relaxed structures at 0, 0.5, and 1.0 GPa (e.g., with PHONOPY) to obtain zone‑centre phonon frequencies. Write all frequencies to phonon_frequencies.csv.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: pressure_GPa (float), mode_index (int), frequency_cm1 (float). Must include all zone‑centre modes for pressures 0, 0.5, and 1.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_bond_orders.csv`
- `/app/outputs/phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_bond_orders.csv
- path: `/app/outputs/effective_bond_orders.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of effective bond orders for selected C–H, C–N, N–N, and N–O bonds at three hydrostatic pressures. Monotonic trends will be scored.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `bond_label`, `effective_bond_order`
  - `units`:
    - `pressure_GPa`: GPa
    - `effective_bond_order`: dimensionless

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of zone‑centre phonon frequencies at three hydrostatic pressures. The blue‑shift trend will be scored.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `mode_index`, `frequency_cm1`
  - `units`:
    - `pressure_GPa`: GPa
    - `frequency_cm1`: cm^-1

Notes: The scored quantities are monotonic trends, not exact absolute values. The hidden checker compares the sign of changes (slope) against the paper's reported trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_bond_orders.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "bond_label",
          "effective_bond_order"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "effective_bond_order": "dimensionless"
        }
      },
      "description": "Table of effective bond orders for selected C–H, C–N, N–N, and N–O bonds at three hydrostatic pressures. Monotonic trends will be scored."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "mode_index",
          "frequency_cm1"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "frequency_cm1": "cm^-1"
        }
      },
      "description": "Table of zone‑centre phonon frequencies at three hydrostatic pressures. The blue‑shift trend will be scored."
    }
  ],
  "notes": "The scored quantities are monotonic trends, not exact absolute values. The hidden checker compares the sign of changes (slope) against the paper's reported trends."
}
```

## How you are scored
The hidden verifier inspects each output CSV independently. For effective bond orders, it verifies that the changes between 0 and 1.0 GPa are monotonic and that the sign of the change (increase/decrease) is consistent for each bond type, comparing against a reference derived from the underlying physics. For phonon frequencies, it checks that every mode’s frequency at 1.0 GPa is higher than at 0 GPa (a blue shift). The verifier does not require exact numerical agreement with any specific published values but scores based on the correctness of the trends. Each artifact carries a weight that contributes to the final score. The verifier’s criteria and tolerances are hidden; your job is to perform the computations faithfully and report the physically correct results.
