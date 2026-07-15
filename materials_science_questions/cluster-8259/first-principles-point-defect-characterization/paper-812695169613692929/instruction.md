# First-principles defect characterization of blue phosphorene

## Problem background
Blue phosphorene (BlueP) is a two‑dimensional semiconductor with a wide indirect band gap and a buckled honeycomb structure. Point defects — single vacancies, double vacancies, and Stone‑Wales rotations — inevitably appear during synthesis and can drastically alter electronic, magnetic, and transport properties, enabling potential applications in nanoelectronics and spintronics. A systematic understanding of how these defects affect formation energies, band gaps, magnetic moments, and current‑voltage characteristics is needed to guide device design.

## Approach
We use density functional theory (DFT) as implemented in the SIESTA package with the GGA‑PBE exchange‑correlation functional and norm‑conserving pseudopotentials to compute total energies, band structures, and magnetic moments. Transport properties are studied with the non‑equilibrium Green’s function (NEGF) method within the TranSIESTA module, which yields the current via the Landauer–Büttiker formula. The workflow begins with a 7×4 rectangular supercell of pristine blue phosphorene (112 P atoms). From this, eight defect structures are built by removing or rotating specific atoms: a single vacancy SV(5|9), four double‑vacancy types (DV), and two Stone‑Wales defects (SW). All geometries are relaxed until forces are small. Static DFT calculations with denser k‑point sampling then provide band gaps and magnetic moments. Formation energies are obtained from total energy differences relative to the pristine supercell. Finally, two‑probe devices are constructed along zigzag and armchair transport directions and the current at 2.6 V bias is computed for every system.

## Reproduction target
Produce two scored JSON files under `/app/outputs`:

1. `properties.json` — an array of objects, one per system (pristine plus the seven defects listed below), each containing:
   - `defect` (string, exactly as written)
   - `formation_energy` (number, eV)
   - `band_gap` (number, eV)
   - `magnetic_moment` (number, μB)
   Defect names: `pristine`, `SV(5|9)`, `DV(5|8|5)-1`, `DV(555|777)`, `DV(5555|6|7777)`, `DV(5|8|5)-2`, `SW(55|77)-1`, `SW(55|77)-2`. For pristine, `formation_energy` is defined as 0.

2. `currents_26V.json` — an array of objects with the same defect names, each containing:
   - `defect` (string)
   - `current_zigzag` (number, μA)
   - `current_armchair` (number, μA)
   All numeric values to three decimal places.

## Assets

- SIESTA DFT package (includes TranSIESTA transport module): https://departments.icmab.es/leem/siesta/
- Norm-conserving pseudopotential for phosphorus (SIESTA format): https://departments.icmab.es/leem/siesta/Databases/Pseudopotentials/

## Workflow steps

### Step 1: Construct supercells
- Role: process
- Action: Generate initial atomic coordinates for a 7×4 rectangular supercell of pristine blue phosphorene (112 atoms) using the known lattice parameters, then introduce the defect structures SV(5|9), DV(5|8|5)-1, DV(555|777), DV(5555|6|7777), DV(5|8|5)-2, SW(55|77)-1, SW(55|77)-2 by removing or rotating atoms as described in the paper's method.
- Evidence: `/app/outputs/initial_geometries.zip`

### Step 2: DFT geometry optimization
- Role: process
- Action: For each supercell (pristine and all defects), run DFT structure relaxation using a GGA-PBE functional with a norm-conserving pseudopotential, DZP basis set, and a suitable plane-wave cutoff, until forces converge. Save the relaxed coordinates and total energies.
- Evidence: `/app/outputs/relaxed_structures.zip`

### Step 3: Static electronic structure calculation
- Role: process
- Action: For each relaxed structure, perform a static DFT calculation with a denser k-point mesh to obtain band gaps and magnetic moments. Record the band gap (eV) and total magnetic moment (μB) for each defect.
- Evidence: `/app/outputs/electronic_properties_raw.json`

### Step 4: Compile formation energies, band gaps, and magnetic moments
- Role: scored (load-bearing)
- Action: Calculate formation energies from the total energies: E_f = E_defect − N × E_p, where E_p is the energy per P atom in pristine BlueP (pristine formation energy is 0). Gather band gaps and magnetic moments from the static calculations. Assemble a JSON array of objects, one per defect (including pristine), with keys: defect (string), formation_energy (eV, number), band_gap (eV, number), magnetic_moment (μB, number).
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: array of objects: { defect (string), formation_energy (number), band_gap (number), magnetic_moment (number) }
- Scoring: scored by hidden verifier

### Step 5: NEGF transport simulation
- Role: scored (load-bearing)
- Action: Using the relaxed geometries, construct two-probe devices for both zigzag and armchair transport directions. For each defect and pristine, run a NEGF calculation at a bias of 2.6 V, employing a suitable k-point sampling along the transport direction. Compute the current from the Landauer-Büttiker formula. Record the current (μA) for zigzag and armchair directions.
- Output file: `/app/outputs/currents_26V.json`
- Format: json
- Contract: array of objects: { defect (string), current_zigzag (number, unit μA), current_armchair (number, unit μA) }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.json`
- `/app/outputs/currents_26V.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed defect formation energies, band gaps, and magnetic moments for pristine and all defective blue phosphorene supercells.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect`, `formation_energy`, `band_gap`, `magnetic_moment`
    - `properties`:
      - `defect`:
        - `type`: string
      - `formation_energy`:
        - `type`: number
        - `units`: eV
      - `band_gap`:
        - `type`: number
        - `units`: eV
      - `magnetic_moment`:
        - `type`: number
        - `units`: μB

### currents_26V.json
- path: `/app/outputs/currents_26V.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: NEGF-calculated current at 2.6 V bias along zigzag and armchair directions for each system.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect`, `current_zigzag`, `current_armchair`
    - `properties`:
      - `defect`:
        - `type`: string
      - `current_zigzag`:
        - `type`: number
        - `units`: μA
      - `current_armchair`:
        - `type`: number
        - `units`: μA

Notes: All numeric values to three decimal places. The defect names must exactly match the list: pristine, SV(5|9), DV(5|8|5)-1, DV(555|777), DV(5555|6|7777), DV(5|8|5)-2, SW(55|77)-1, SW(55|77)-2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect",
            "formation_energy",
            "band_gap",
            "magnetic_moment"
          ],
          "properties": {
            "defect": {
              "type": "string"
            },
            "formation_energy": {
              "type": "number",
              "units": "eV"
            },
            "band_gap": {
              "type": "number",
              "units": "eV"
            },
            "magnetic_moment": {
              "type": "number",
              "units": "μB"
            }
          }
        }
      },
      "description": "Computed defect formation energies, band gaps, and magnetic moments for pristine and all defective blue phosphorene supercells."
    },
    {
      "file": "currents_26V.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect",
            "current_zigzag",
            "current_armchair"
          ],
          "properties": {
            "defect": {
              "type": "string"
            },
            "current_zigzag": {
              "type": "number",
              "units": "μA"
            },
            "current_armchair": {
              "type": "number",
              "units": "μA"
            }
          }
        }
      },
      "description": "NEGF-calculated current at 2.6 V bias along zigzag and armchair directions for each system."
    }
  ],
  "notes": "All numeric values to three decimal places. The defect names must exactly match the list: pristine, SV(5|9), DV(5|8|5)-1, DV(555|777), DV(5555|6|7777), DV(5|8|5)-2, SW(55|77)-1, SW(55|77)-2."
}
```

## How you are scored
A hidden verifier reads your `properties.json` and `currents_26V.json` and compares every numeric entry against a set of reference values using tolerance‑based comparisons. It also checks internal consistency — for example, the formation energies should exhibit a physically reasonable ordering among defect types, and the magnetic moments should be compatible with the nature of each defect (some defects are expected to be non‑magnetic). The final reward is a weighted sum of these comparisons, normalized between 0 and 1. You must execute the full workflow (DFT relaxation, static electronic structure, NEGF transport) to obtain the numbers; simply writing reference values is not sufficient and will not yield a high score.
