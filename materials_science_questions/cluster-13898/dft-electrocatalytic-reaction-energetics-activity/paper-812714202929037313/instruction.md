# Compile N 1s Binding Energies and Shifts for CNx Active Sites

## Problem background
Nitrogen-doped carbon nanostructures (CNx) are promising cost-effective catalysts for the oxygen reduction reaction (ORR) in fuel cells, but the nature of the active sites remains debated. Post‑reaction X‑ray photoelectron spectroscopy (XPS) experiments show that the N‑1s envelope changes with applied potential, suggesting protonation and formation of ORR intermediates on nitrogen sites. Density functional theory (DFT) can predict the N 1s core‑level binding energies of different nitrogen functionalities, providing the energetic reference to interpret the experimental shifts.

This task compiles the DFT‑computed N 1s binding energies reported in the paper's Supporting Information for a set of CNx model sites and computes the corresponding binding‑energy shifts.

## Approach
The paper’s Supporting Information provides absolute N 1s binding energies (in eV) for eight nitrogen‑doped carbon edge sites: zigzag pyridinic, zigzag pyridinium, zigzag oxide, basal quaternary, armchair pyridinic, armchair pyridinium, armchair quaternary, armchair oxide. For each site the table lists the binding energy for the bare site and for several chemically relevant states: protonated, and with adsorbed ORR intermediates OOH*, OH*, O*.

Using these absolute energies you will compute:
- The shift of each state relative to the **bare zigzag pyridinic** reference (taken as 0.0 eV).
- For the protonated state, the **protonation shift** (E_bind(protonated) − E_bind(bare)).
- For the adsorbate states (OOH*, OH*, O*), the **adsorbate shift** (E_bind(adsorbate‑covered) − E_bind(bare)).

All results are to be written in a single JSON file.

## Provided data
The following table gives the DFT N 1s core‑level binding energies (eV) extracted from the paper’s Supporting Information. Use these values **as given** to perform the required computations.

| Site                  | State        | Binding energy (eV) |
|-----------------------|--------------|---------------------|
| zigzag_pyridinic      | bare         | 398.7              |
| zigzag_pyridinic      | protonated   | 400.3              |
| zigzag_pyridinic      | OOH          | 399.1              |
| zigzag_pyridinic      | OH           | 399.1              |
| zigzag_pyridinic      | O            | 398.7              |
| zigzag_pyridinium     | bare         | 400.3              |
| zigzag_pyridinium     | OOH          | 402.3              |
| zigzag_pyridinium     | OH           | 402.3              |
| zigzag_pyridinium     | O            | 400.3              |
| zigzag_oxide          | bare         | 402.7              |
| zigzag_oxide          | OH           | 403.1              |
| zigzag_oxide          | OOH          | 402.7              |
| zigzag_oxide          | O            | 402.7              |
| basal_quaternary      | bare         | 401.5              |
| basal_quaternary      | OOH          | 401.5              |
| basal_quaternary      | OH           | 401.4              |
| basal_quaternary      | O            | 401.9              |
| armchair_pyridinic    | bare         | 398.8              |
| armchair_pyridinic    | protonated   | 400.4              |
| armchair_pyridinic    | OOH          | 399.2              |
| armchair_pyridinic    | OH           | 399.2              |
| armchair_pyridinic    | O            | 398.8              |
| armchair_pyridinium   | bare         | 400.4              |
| armchair_pyridinium   | OOH          | 402.4              |
| armchair_pyridinium   | OH           | 402.4              |
| armchair_pyridinium   | O            | 400.4              |
| armchair_quaternary   | bare         | 401.5              |
| armchair_quaternary   | OH           | 401.1              |
| armchair_quaternary   | OOH          | 401.5              |
| armchair_quaternary   | O            | 401.5              |
| armchair_oxide        | bare         | 402.7              |
| armchair_oxide        | OH           | 403.1              |
| armchair_oxide        | OOH          | 402.7              |
| armchair_oxide        | O            | 402.7              |

## Reproduction target
Using the absolute binding energies from the table above, create a single JSON file (`dft_binding_energies.json`) that contains for every site‑state combination:
- the absolute binding energy (`binding_energy_eV`),
- the shift relative to bare zigzag pyridinic (`shift_vs_zigzag_pyridinic_eV`),
- for the protonated state the protonation shift (`protonation_shift_eV`),
- for OOH*, OH*, O* states the adsorbate shift (`adsorbate_shift_eV`).

## Workflow steps

### Step 1: Compile the binding energies and compute shifts
- Role: scored (load‑bearing)
- Action: Read the binding energy table provided above. For each (site, state) pair that appears in the table, include an entry in the output JSON. Compute the required shifts from the absolute energies:
  1. Shift vs. zigzag pyridinic bare: `binding_energy_eV − 398.7`.
  2. Protonation shift: `binding_energy_eV(protonated) − binding_energy_eV(bare)` (only for the protonated state).
  3. Adsorbate shift: `binding_energy_eV(adsorbate‑covered) − binding_energy_eV(bare)` (only for OOH*, OH*, O* states).
- Output file: `/app/outputs/dft_binding_energies.json`
- Format: json
- Contract: see Output contract section.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_binding_energies.json`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_binding_energies.json
- path: `/app/outputs/dft_binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: A JSON object containing the N 1s binding energies and computed shifts for the eight CNx site models in their bare, protonated, and ORR‑intermediate states. Only the states listed in the provided data table need be included; missing states should not be present.
- schema:
  The top‑level value is an object. Each key is a site name (e.g., `zigzag_pyridinic`, `basal_quaternary`). The corresponding value is an object whose keys are the state names (`bare`, `protonated`, `OOH`, `OH`, `O`). Only the states that appear for that site in the table are required; do not include state keys for which no data were provided.
  For each state key, the value is an object with the following entries:
  - `binding_energy_eV` (number, required) – the absolute binding energy from the table.
  - `shift_vs_zigzag_pyridinic_eV` (number, optional but highly recommended) – shift relative to bare zigzag pyridinic (398.7 eV).
  - `protonation_shift_eV` (number, optional; only present for the `protonated` state) – difference between protonated and bare.
  - `adsorbate_shift_eV` (number, optional; only present for OOH, OH, O states) – difference between adsorbate‑covered and bare.

The checker will recompute shifts from the binding energies you provide and compare them against reference values. The exact keys present must match the states listed in the data table; extra or missing keys may affect scoring.

## Self‑check before finishing (optional, not scored)
A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects are well‑formed, and the expected state keys are present according to the provided data (no missing keys that were in the table, and no extra keys). Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Each key is a site name; the value is an object with state keys (bare, protonated, OOH, OH, O) that were present in the provided data table. Each state value is an object containing at least binding_energy_eV (number). Optional fields: shift_vs_zigzag_pyridinic_eV, protonation_shift_eV (protonated only), adsorbate_shift_eV (OOH/OH/O only)."
      },
      "description": "A JSON object containing DFT‑computed N 1s binding energies and shifts for the eight CNx site models in their bare, protonated, and ORR‑intermediate states."
    }
  ],
  "notes": "The reported binding energies and shifts serve as the raw artifact; the checker will recompute shift values from the binding energies and compare them against hidden reference values from the paper's Supporting Information. Relative ordering and approximate magnitude (within tolerance) are scored."
}
```

## How you are scored
A hidden verifier reads your `dft_binding_energies.json`. It first recomputes the shift values (adsorbate‑induced shifts, protonation shifts, and shifts relative to zigzag pyridinic) from the binding energies you report. These computed shifts are compared against reference shift data. The verifier checks whether all required entries are present, whether the ordering of shifts matches the expected trends (e.g., protonation should increase binding energy, certain intermediates should yield characteristic shifts), and whether shift magnitudes lie within an acceptable tolerance. Scoring weights are distributed across the site/state combinations; missing or unphysical entries receive no credit. The absolute binding energies are used only to derive shifts, so systematic shifts in absolute values do not affect the score as long as relative trends are correct.