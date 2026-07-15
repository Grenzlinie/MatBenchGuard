# Group-theoretical phonon symmetry decomposition of GaSe polytypes

## Problem background
Layered GaSe crystals are built from identical Se-Ga-Ga-Se layers that stack in different arrangements, forming several polytypes (γ, ε, β). The symmetry of vibrational modes in each polytype is determined by group theory and depends on both the layer symmetry and the stacking order. Decomposing the Γ-point phonons into irreducible representations, separated by acoustic, optical, interlayer, and intralayer character, enables identification of polytypes from Raman spectra and reveals how interlayer interactions modify the vibrational spectrum. This task requires you to perform the group-theoretical decomposition for the three main polytypes and for the isolated monolayer.

## Approach
We adopt a layer-based approach: first model the single GaSe layer (layer group p‑6m2) and compute its mechanical (vibrational) representation at the Γ‑point using the LSITESYM program (or an equivalent group-theoretical tool). This yields the irreducible representation content of the layer's acoustic and optical modes. Then, for each polytype (γ with space group R3m, ε with P6m2, β with P63/mmc), use the SITESYM program (or equivalent) to map the layer Wyckoff positions into the bulk space group and obtain the bulk phonon representations at Γ. These bulk modes are further partitioned into interlayer modes (derived from the layer's acoustic modes) and intralayer modes (derived from the layer's optical modes). The results are the integer counts of each irreducible representation for each category.

## Reproduction target
Produce a single JSON file, `decomposition.json`, that contains the irreducible representation counts for each system:
- A single GaSe layer: acoustic and optical modes.
- γ (R3m), ε (P6m2), β (P63/mmc) polytypes: acoustic, optical, interlayer, and intralayer modes.
Each count is an integer; the irreducible representation labels must follow the conventions used in the literature for the corresponding point groups (e.g., A1′, E′, etc.). The JSON structure is detailed in the Output contract section.

## Assets

- Bilbao Crystallographic Server: https://www.cryst.ehu.es/
- GaSe crystallographic data

## Workflow steps

### Step 1: Define GaSe layer structural model
- Role: process
- Action: Prepare the crystallographic input for a single GaSe layer: layer group p-6m2, Ga at Wyckoff 2e, Se at 2d. Create a suitable input file (e.g., CIF or Bilbao server input) for subsequent symmetry analysis.
- Evidence: none

### Step 2: Compute layer phonon representation with LSITESYM
- Role: process
- Action: Run LSITESYM (or equivalent group-theoretical tool) on the Bilbao Crystallographic Server or using a local implementation to compute the mechanical (vibrational) representation at the Γ-point for the single GaSe layer. Obtain the irreducible representation decomposition of acoustic and optical modes.
- Evidence: none

### Step 3: Compute bulk phonon representations for polytypes with SITESYM
- Role: process
- Action: For each GaSe polytype (γ, ε, β), use SITESYM (or an equivalent tool) to map the layer Wyckoff positions into the bulk space group (R3m, P6m2, P63/mmc) and determine the bulk phonon mode symmetries at the Γ-point. Classify the resulting modes into interlayer and intralayer components.
- Evidence: none

### Step 4: Compile final decomposition JSON
- Role: scored (load-bearing)
- Action: Parse the outputs from LSITESYM/SITESYM (or compute the irreducible representation counts directly using group theory) and write the results to decomposition.json. The JSON must contain the exact irreducible representation labels and counts for the single GaSe layer and for the γ, ε, β polytypes, following the schema described in the output contract.
- Output file: `/app/outputs/decomposition.json`
- Format: json
- Contract: JSON object with keys 'layer', 'gamma', 'epsilon', 'beta'. Each value is an object with keys 'acoustic', 'optical' (and for polytypes also 'interlayer', 'intralayer'). Each such key maps to an object whose keys are irreducible representation label strings (e.g., 'A1''', 'E''', 'Gamma1', etc.) and values are integer counts. For the layer, omit 'interlayer' and 'intralayer'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/decomposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### decomposition.json
- path: `/app/outputs/decomposition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Group-theoretical irreducible representation counts for vibrational modes in GaSe layer and polytypes (γ, ε, β). The counts must match the paper's Table 1.
- schema:
  - `type`: object
  - `required`:
    - `layer`: object
    - `gamma`: object
    - `epsilon`: object
    - `beta`: object
  - `items`:
    - `acoustic`:
      - `type`: object
      - `description`: irrep label string -> integer count
    - `optical`:
      - `type`: object
      - `description`: irrep label string -> integer count
    - `interlayer`:
      - `type`: object
      - `description`: irrep label string -> integer count
    - `intralayer`:
      - `type`: object
      - `description`: irrep label string -> integer count
  - `required_columns`:
  - `units`: object

Notes: The checker compares the agent's integer counts for each irreducible representation in each system against hidden gold values derived from the paper's Table 1. Only exact integer agreement is required; no tolerance for numerical noise.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "decomposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "layer": "object",
          "gamma": "object",
          "epsilon": "object",
          "beta": "object"
        },
        "items": {
          "acoustic": {
            "type": "object",
            "description": "irrep label string -> integer count"
          },
          "optical": {
            "type": "object",
            "description": "irrep label string -> integer count"
          },
          "interlayer": {
            "type": "object",
            "description": "irrep label string -> integer count"
          },
          "intralayer": {
            "type": "object",
            "description": "irrep label string -> integer count"
          }
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Group-theoretical irreducible representation counts for vibrational modes in GaSe layer and polytypes (γ, ε, β). The counts must match the paper's Table 1."
    }
  ],
  "notes": "The checker compares the agent's integer counts for each irreducible representation in each system against hidden gold values derived from the paper's Table 1. Only exact integer agreement is required; no tolerance for numerical noise."
}
```

## How you are scored
After you submit your `decomposition.json`, a hidden verifier will extract every irreducible representation count from your file and compare it to the correct group-theoretical result. An exact integer match is required for each count — no tolerance is applied because the counts are deterministic integers. The verifier computes the fraction of entries that match exactly and returns a single reward between 0.0 (no matches) and 1.0 (all counts correct). There is no partial credit for close but incorrect counts. The JSON schema and key names must be completely correct or the file will be rejected before scoring.
