## Problem background

Photocatalytic water splitting is a promising route for sustainable hydrogen production using solar energy. Two‑dimensional graphitic carbon nitrides, in particular monolayer C₂N, have emerged as potential metal‑free photocatalysts. For a semiconductor to drive overall water splitting, its conduction band minimum (CBM) must lie above the water reduction potential and its valence band maximum (VBM) must lie below the water oxidation potential. This task computes the electronic band structure and absolute band edge positions of pristine C₂N and its boron‑ and phosphorus‑doped variants, assessing their thermodynamic feasibility for overall water splitting.

## Approach

Use first‑principles density functional theory (DFT) with a hybrid functional to obtain accurate band gaps and absolute band edge energies. Build the monolayer C₂N crystal structure from its known hexagonal unit cell (12 C and 6 N atoms, lattice parameter ~8.33 Å). Relax the geometry using a PBE functional, then construct substitutionally doped cells: one nitrogen atom replaced by boron (B‑doped) and one nitrogen replaced by phosphorus (P‑doped). Relax each doped cell. For each relaxed system, perform a static calculation with the HSE06 hybrid functional, determine the band gap and the absolute CBM/VBM energies relative to the vacuum level by aligning the planar‑averaged electrostatic potential. Compare the band edges to the standard water redox potentials (at pH 0) to verify whether the criterion for overall water splitting is satisfied.

## Reproduction target

Compute the HSE06‑level band gap (eV), absolute conduction band minimum CBM (eV, vacuum referenced), and absolute valence band maximum VBM (eV, vacuum referenced) for:

1. Pristine monolayer C₂N
2. B‑doped C₂N (B substituting N)
3. P‑doped C₂N (P substituting N)

The numeric results for each system will be written to separate JSON files. The viability for water splitting is assessed by checking whether CBM > −4.44 eV and VBM < −5.67 eV.

## Assets

- **Quantum ESPRESSO** – open‑source DFT code. Access: https://www.quantum‑espresso.org/
- **Standard solid‑state pseudopotentials (SSSP library)** – PBE pseudopotentials suitable for HSE06 calculations. Access: https://www.materialscloud.org/discover/sssp/table/efficiency
- **C₂N crystal structure** – monolayer C₂N hexagonal unit cell with 12 C and 6 N atoms, lattice parameter ≈ 8.33 Å. The structure is described in the literature (Mahmood et al., Nat. Commun. 6, 6486, 2015); the agent builds the input geometry from these known parameters.

## Workflow steps

### Step 1: Relax pristine C₂N geometry
- Role: process
- Action: Perform geometry relaxation of monolayer C₂N using Quantum ESPRESSO with the PBE functional. Relax atomic positions and cell until forces are converged.
- Evidence: `/app/outputs/pristine_relax.out`

### Step 2: Relax B‑doped C₂N geometry
- Role: process
- Action: Construct a cell with one nitrogen atom substituted by boron. Relax the geometry using the same functional and convergence criteria as for pristine C₂N.
- Evidence: `/app/outputs/B_doped_relax.out`

### Step 3: Relax P‑doped C₂N geometry
- Role: process
- Action: Construct a cell with one nitrogen atom substituted by phosphorus. Relax the geometry as before.
- Evidence: `/app/outputs/P_doped_relax.out`

### Step 4: Compute band edges of pristine C₂N
- Role: scored (load-bearing)
- Action: Using the relaxed pristine structure, run an HSE06 static calculation. Extract the band gap, absolute CBM (vacuum) and VBM (vacuum) via vacuum‑alignment. Write the results to the output file.
- Output file: `/app/outputs/pristine_results.json`
- Format: json
- Contract: A JSON object with keys "band_gap" (number, eV), "CBM_vacuum" (number, eV), "VBM_vacuum" (number, eV).
- Scoring: scored by hidden verifier

### Step 5: Compute band edges of B‑doped C₂N
- Role: scored
- Action: From the relaxed B‑doped geometry, run HSE06 static calculation. Determine band gap, CBM_vacuum, VBM_vacuum using the same vacuum‑alignment procedure. Write to output file.
- Output file: `/app/outputs/B_doped_results.json`
- Format: json
- Contract: Same JSON schema as above.
- Scoring: scored by hidden verifier

### Step 6: Compute band edges of P‑doped C₂N
- Role: scored
- Action: From the relaxed P‑doped geometry, run HSE06 static calculation and extract the three quantities. Write to output file.
- Output file: `/app/outputs/P_doped_results.json`
- Format: json
- Contract: Same JSON schema.
- Scoring: scored by hidden verifier

## Output files

- `/app/outputs/pristine_results.json`
- `/app/outputs/B_doped_results.json`
- `/app/outputs/P_doped_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_results.json
- path: `/app/outputs/pristine_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: HSE06 band gap and absolute band edge energies (vacuum level) for pristine monolayer C₂N. Values are checked against hidden reference with tolerances; also checked for water‑splitting feasibility (CBM > −4.44 eV, VBM < −5.67 eV).
- schema:
  - `type`: object
  - `required`: `band_gap`, `CBM_vacuum`, `VBM_vacuum`
  - `properties`:
    - `band_gap`:
      - `type`: number
      - `units`: eV
    - `CBM_vacuum`:
      - `type`: number
      - `units`: eV
    - `VBM_vacuum`:
      - `type`: number
      - `units`: eV

### B_doped_results.json
- path: `/app/outputs/B_doped_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: HSE06 band properties for B‑doped C₂N (B substituting N). Same vacuum alignment and water‑splitting checks apply.
- schema:
  - `type`: object
  - `required`: `band_gap`, `CBM_vacuum`, `VBM_vacuum`
  - `properties`:
    - `band_gap`:
      - `type`: number
      - `units`: eV
    - `CBM_vacuum`:
      - `type`: number
      - `units`: eV
    - `VBM_vacuum`:
      - `type`: number
      - `units`: eV

### P_doped_results.json
- path: `/app/outputs/P_doped_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: HSE06 band properties for P‑doped C₂N (P substituting N). Same vacuum alignment and water‑splitting checks apply.
- schema:
  - `type`: object
  - `required`: `band_gap`, `CBM_vacuum`, `VBM_vacuum`
  - `properties`:
    - `band_gap`:
      - `type`: number
      - `units`: eV
    - `CBM_vacuum`:
      - `type`: number
      - `units`: eV
    - `VBM_vacuum`:
      - `type`: number
      - `units`: eV

Notes: Each JSON must contain the three numeric keys. The hidden verifier compares the reported values to paper‑derived references with tolerances and also applies the water‑redox feasibility check (CBM > −4.44 eV, VBM < −5.67 eV).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap",
          "CBM_vacuum",
          "VBM_vacuum"
        ],
        "properties": {
          "band_gap": {
            "type": "number",
            "units": "eV"
          },
          "CBM_vacuum": {
            "type": "number",
            "units": "eV"
          },
          "VBM_vacuum": {
            "type": "number",
            "units": "eV"
          }
        }
      },
      "description": "HSE06 band gap and absolute band edge energies (vacuum level) for pristine monolayer C₂N. Values are checked against hidden reference with tolerances; also checked for water‑splitting feasibility (CBM > −4.44 eV, VBM < −5.67 eV)."
    },
    {
      "file": "B_doped_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap",
          "CBM_vacuum",
          "VBM_vacuum"
        ],
        "properties": {
          "band_gap": {
            "type": "number",
            "units": "eV"
          },
          "CBM_vacuum": {
            "type": "number",
            "units": "eV"
          },
          "VBM_vacuum": {
            "type": "number",
            "units": "eV"
          }
        }
      },
      "description": "HSE06 band properties for B‑doped C₂N (B substituting N). Same vacuum alignment and water‑splitting checks apply."
    },
    {
      "file": "P_doped_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap",
          "CBM_vacuum",
          "VBM_vacuum"
        ],
        "properties": {
          "band_gap": {
            "type": "number",
            "units": "eV"
          },
          "CBM_vacuum": {
            "type": "number",
            "units": "eV"
          },
          "VBM_vacuum": {
            "type": "number",
            "units": "eV"
          }
        }
      },
      "description": "HSE06 band properties for P‑doped C₂N (P substituting N). Same vacuum alignment and water‑splitting checks apply."
    }
  ],
  "notes": "Each JSON must contain the three numeric keys. The hidden verifier compares the reported values to paper‑derived references with tolerances and also applies the water‑redox feasibility check (CBM > −4.44 eV, VBM < −5.67 eV)."
}
```

## How you are scored

A hidden verifier reads each JSON file and compares the reported `band_gap`, `CBM_vacuum`, and `VBM_vacuum` against the paper’s hidden reference values, with appropriate tolerances that account for different DFT implementations. Additionally, the verifier checks that for each system CBM > −4.44 eV and VBM < −5.67 eV (water redox potentials at pH 0). Each scored step carries a weight; the final reward is the weighted average of per‑step scores. Reporting paper numbers without genuinely running the calculations will not earn credit.
