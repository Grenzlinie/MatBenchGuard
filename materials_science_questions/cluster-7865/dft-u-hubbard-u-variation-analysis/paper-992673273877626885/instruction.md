# LSDA+U+J and cDFT Investigation of Ferrimagnetic YBaCo4O7 (Y114)

## Problem background
YBaCo₄O₇ (Y114) is a transition-metal oxide exhibiting charge disproportionation, where three Co ions adopt the +2 oxidation state and one adopts +3. This leads to slightly different tetrahedral oxygen environments for the two cobalt types and a ferrimagnetic magnetic structure at low temperature. Standard DFT treatments with Hubbard‑model corrections (DFT+U+J) are commonly used to study such systems, but accurately modeling the magnetic moments remains challenging. Constrained DFT (cDFT) with potential‑based self‑consistency enforces charge and magnetic‑moment constraints directly, offering an alternative way to describe the local electronic structure and magnetism of strongly correlated materials. The work compares these two approaches for Y114, focusing on the structural and magnetic properties that emerge from each method.

## Approach
The LSDA+U+J method with empirically fitted Hubbard parameters (U=8 eV for Co²⁺, U=6 eV for Co³⁺, Hund's J=0.1 eV) is used to optimize the geometry of ferrimagnetic Y114. The resulting structure reveals two distinct tetrahedral oxygen coordinations for the two cobalt sites. The bond lengths and bond angles around each Co ion are extracted. Next, a constrained DFT (cDFT) calculation is performed on the relaxed structure, where the total charge on each Co site is fixed to the formal oxidation state (+2 or +3) and the magnetic moments of all non‑magnetic atoms (Y, Ba, O) are constrained to zero. The self‑consistent cDFT solution yields magnetic moments for the Co ions that reflect the effects of charge localisation and inter‑site interactions.

## Reproduction target
Start from the primitive cell of Y114 obtained from the Materials Project (mp‑19151). Perform a spin‑polarized LSDA+U+J structural relaxation using Quantum ESPRESSO with the specified Hubbard parameters, plane‑wave cutoff, and k‑point mesh, and save the relaxed atomic positions. From the relaxed structure, compute the eight Co–O bond distances and twelve O–Co–O bond angles and write them to a CSV file. Then, using ABINIT, set up a cDFT calculation on the same relaxed structure, applying charge constraints on Co and zero‑moment constraints on Y, Ba, and O. Extract the magnetic moments of the two distinct Co sites and write them to a second CSV file. The target quantities are the bond geometry (lengths and angles) from LSDA+U+J and the Co magnetic moments from cDFT.

## Assets

- YBaCo₄O₇ (mp-19151): https://materialsproject.org/materials/mp-19151
- PseudoDojo ONCV pseudopotentials: http://www.pseudo-dojo.org/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ABINIT: https://www.abinit.org/

## Workflow steps

### Step 1: LSDA+U+J structural relaxation
- Role: process
- Action: Perform a spin‑polarized LSDA+U+J structural relaxation of ferrimagnetic YBaCo₄O₇ (Y114) using Quantum ESPRESSO, starting from the Materials Project mp‑19151 primitive cell. Set Hubbard parameters: U=8 eV for the Co²⁺ site, U=6 eV for the Co³⁺ site, and Hund's J=0.1 eV for all Co atoms. Enforce ferrimagnetic order with opposite initial spin orientations for Co²⁺ and Co³⁺ ions. Use LSDA functional, a plane‑wave kinetic energy cutoff of 50 Ha, a 6×6×3 Γ‑centered k‑point mesh, and force convergence of 5×10⁻⁵ Ha/Bohr. Save the relaxed atomic positions and lattice vectors to a JSON file (relaxed_structure.json).
- Evidence: `/app/outputs/relaxed_structure.json`

### Step 2: Extract Co–O bond geometry
- Role: scored
- Action: Read relaxed_structure.json, identify the Co³⁺ (Co1) and Co²⁺ (Co2) sites, and compute all eight Co–O bond distances (Å) and twelve O–Co–O bond angles (degrees). Output a CSV with one row per bond or angle, labeled as described in the output schema.
- Output file: `/app/outputs/step_01_bond_geometry.csv`
- Format: csv
- Contract: type (str, 'bond' or 'angle'), label (str, e.g. 'Co1-O1' or 'O1-Co1-O2'), value (float, Å for bonds, degrees for angles)
- Scoring: scored by hidden verifier

### Step 3: Constrained DFT calculation
- Role: process
- Action: Using ABINIT, set up a spin‑polarized cDFT calculation on the relaxed structure from relaxed_structure.json. Employ LSDA functional, plane‑wave cutoff 50 Ha, and 6×6×3 Γ‑centered k‑point grid. Apply charge constraints: Co²⁺ sites to +2, Co³⁺ site to +3. Constrain the magnetic moments of Y, Ba, and O atoms to zero. Use a weight‑function radius of 2 Bohr around each atom. Save the self‑consistent magnetic moments of all atoms to a JSON file (cdft_all_moments.json).
- Evidence: `/app/outputs/cdft_all_moments.json`

### Step 4: Extract Co magnetic moments
- Role: scored (load-bearing)
- Action: Read cdft_all_moments.json and extract the magnetic moment (μ_B) for the Co²⁺ (Co2) and Co³⁺ (Co1) sites. Write a CSV with one row per unique cobalt site, identifying the site and its moment.
- Output file: `/app/outputs/step_02_cdft_magnetic_moments.csv`
- Format: csv
- Contract: site (str, 'Co1' or 'Co2'), mu_B (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bond_geometry.csv`
- `/app/outputs/step_02_cdft_magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bond_geometry.csv
- path: `/app/outputs/step_01_bond_geometry.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: LSDA+U+J Co–O bond lengths and O–Co–O bond angles. The checker compares each bond length and angle to the paper’s reported values within a hidden tolerance.
- schema:
  - `required_columns`: `type`, `label`, `value`
  - `units`:
    - `value`: Å for bond lengths, degrees for angles

### step_02_cdft_magnetic_moments.csv
- path: `/app/outputs/step_02_cdft_magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Cobalt magnetic moments from cDFT. The checker compares the two site moments to the paper’s reported cDFT values within a hidden tolerance.
- schema:
  - `required_columns`: `site`, `mu_B`
  - `units`:
    - `mu_B`: Bohr magnetons

Notes: Both artifacts are re‑derivable from the raw QE/ABINIT outputs; the scored CSV files contain the values directly, and the checker will compare them to the paper’s gold values. No interpolation or transformation beyond extraction is expected.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bond_geometry.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "type",
          "label",
          "value"
        ],
        "units": {
          "value": "Å for bond lengths, degrees for angles"
        }
      },
      "description": "LSDA+U+J Co–O bond lengths and O–Co–O bond angles. The checker compares each bond length and angle to the paper’s reported values within a hidden tolerance."
    },
    {
      "file": "step_02_cdft_magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "site",
          "mu_B"
        ],
        "units": {
          "mu_B": "Bohr magnetons"
        }
      },
      "description": "Cobalt magnetic moments from cDFT. The checker compares the two site moments to the paper’s reported cDFT values within a hidden tolerance."
    }
  ],
  "notes": "Both artifacts are re‑derivable from the raw QE/ABINIT outputs; the scored CSV files contain the values directly, and the checker will compare them to the paper’s gold values. No interpolation or transformation beyond extraction is expected."
}
```

## How you are scored
The hidden verifier compares the bond lengths and angles in step_01_bond_geometry.csv to a set of hidden reference values within a tolerance. For each bond and angle, full credit is given if the deviation is within tolerance. Similarly, the magnetic moments in step_02_cdft_magnetic_moments.csv are compared to hidden reference moments. The overall reward is the average of the two stage scores. Producing values within tolerance earns full credit; larger deviations reduce the score proportionally.
