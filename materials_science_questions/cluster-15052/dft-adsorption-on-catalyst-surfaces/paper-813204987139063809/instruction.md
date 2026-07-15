# CO Adsorption on Atomically Thin SnO2: DFT Adsorption Energy and Density of States

## Problem background
Atomically thin tin dioxide (SnO2) sheets are promising catalysts for CO oxidation. Their activity is thought to be governed by the large fraction of undercoordinated surface atoms and by electronic structure modifications that accompany the reduced thickness. Density functional theory (DFT) can be used to investigate how CO binds to Sn sites of different coordination and how the density of states (DOS) changes when going from bulk SnO2 to an ultrathin sheet.

## Approach
Construct models of the tetragonal (rutile) SnO2 (001) surface and of bulk SnO2 from the public crystal structure. Perform plane-wave DFT calculations with the GGA-PBE functional to relax the geometries and to compute total energies. Determine CO adsorption energies on a four-coordinate surface Sn atom and on a six-coordinate interior Sn atom as
E_ads = E(slab+CO) – E(slab) – E(CO).
Then compute the total DOS for a five-layer (0.66 nm) slab and for bulk, aligning the energy scales to the Fermi level. Compare the computed values for the two Sn sites and examine the DOS near the valence band edge.

## Reproduction target
- Compute the adsorption energy of CO on a four-coordinate surface Sn atom of a SnO2 (001) slab and on a six-coordinate interior Sn atom. Report both energies in eV.
- Compute the total density of states for the five-layer SnO2 slab and for bulk SnO2, outputting the spectra with energy relative to the Fermi level.
- Save the adsorption energies to `/app/outputs/co_adsorption_energies.csv` and the DOS data to `/app/outputs/dos_data.csv`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP, GBRV): https://www.materialscloud.org/discover/sssp/tablette
- Rutile SnO2 crystal structure: https://materialsproject.org/materials/mp-856/

## Workflow steps

### Step 1: CO adsorption energy calculation
- Role: scored (load-bearing)
- Action: Perform DFT calculations to compute the adsorption energy of CO on a four-coordinate Sn atom at the SnO2 (001) surface and on a six-coordinate Sn atom in the interior. Build appropriate slab and bulk models from the rutile SnO2 structure, relax geometries, and calculate adsorption energies as E_ads = E(slab+CO) - E(slab) - E(CO). Report both energies in eV.
- Output file: `/app/outputs/co_adsorption_energies.csv`
- Format: csv
- Contract: Columns: site (string, values 'surface_Sn_CN4' or 'interior_Sn_CN6'), adsorption_energy (float, eV).
- Scoring: scored by hidden verifier

### Step 2: Density of states calculation
- Role: scored
- Action: Perform DFT calculations for a five-layer (0.66 nm) SnO2 slab and for bulk SnO2 to obtain the total density of states (DOS). Align energy scales to the Fermi level and output the DOS curves as energy (eV) and DOS values for both slab and bulk.
- Output file: `/app/outputs/dos_data.csv`
- Format: csv
- Contract: Columns: energy (float, eV relative to Fermi level), dos_slab (float, arbitrary units), dos_bulk (float, arbitrary units).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/co_adsorption_energies.csv`
- `/app/outputs/dos_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### co_adsorption_energies.csv
- path: `/app/outputs/co_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CO adsorption energies in eV for surface Sn (CN=4) and interior Sn (CN=6).
- schema:
  - `type`: table
  - `required_columns`: `site`, `adsorption_energy`
  - `units`:
    - `adsorption_energy`: eV

### dos_data.csv
- path: `/app/outputs/dos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total density of states for the 0.66 nm SnO2 slab and bulk SnO2; energy aligned to the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `dos_slab`, `dos_bulk`
  - `units`:
    - `energy`: eV relative to Fermi level
    - `dos_slab`: arbitrary units
    - `dos_bulk`: arbitrary units

Notes: The ethylenediamine adsorption calculation is omitted as it is not a headline result. The scoring for DOS verifies that the slab DOS exceeds bulk DOS near the valence band edge.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "co_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "adsorption_energy"
        ],
        "units": {
          "adsorption_energy": "eV"
        }
      },
      "description": "CO adsorption energies in eV for surface Sn (CN=4) and interior Sn (CN=6)."
    },
    {
      "file": "dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "dos_slab",
          "dos_bulk"
        ],
        "units": {
          "energy": "eV relative to Fermi level",
          "dos_slab": "arbitrary units",
          "dos_bulk": "arbitrary units"
        }
      },
      "description": "Total density of states for the 0.66 nm SnO2 slab and bulk SnO2; energy aligned to the Fermi level."
    }
  ],
  "notes": "The ethylenediamine adsorption calculation is omitted as it is not a headline result. The scoring for DOS verifies that the slab DOS exceeds bulk DOS near the valence band edge."
}
```

## How you are scored
A hidden verifier will read your `co_adsorption_energies.csv` and `dos_data.csv`. It will check that the adsorption energies are reported in eV and that the relationship between the two Sn sites satisfies a required structural trend. For the DOS data, it will verify that the slab DOS near the valence band edge exhibits a specific enhancement relative to bulk. Each artifact is scored independently and the scores are combined into a final reward. Simply reporting numbers from the literature is not sufficient; you must perform the computations and produce the requested CSV files.
