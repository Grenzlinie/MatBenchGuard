# Layer‑dependent band gap, work function, and dielectric constant of few‑layer GeSe from first‑principles

## Problem background
Few-layer germanium selenide (GeSe) is a puckered two-dimensional semiconductor that has recently attracted attention for optoelectronic and photovoltaic applications. The electronic and optical properties of few-layer GeSe—including the band gap, work function, and dielectric function—are expected to change with the number of layers, making it possible to tune device behavior by layer thickness. Density functional theory (DFT) calculations are used to compute these layer-dependent properties and explore how they evolve from monolayer to bulk.

## Approach
The approach uses first-principles plane-wave DFT with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation functional and Grimme D2 van der Waals correction to account for interlayer interactions. For each system (bulk GeSe and few-layer slabs with 1 to 6 layers), the workflow begins with full geometry relaxation, followed by a self-consistent field (SCF) calculation to obtain the ground-state charge density and Fermi level. The band structure is then computed along high-symmetry k-points (Γ–X–Y–Γ) to determine the band gap energy and whether the gap is direct or indirect. The work function is extracted from the planar-averaged electrostatic potential by comparing the vacuum level to the Fermi energy. The frequency-dependent dielectric function is calculated for odd numbers of layers (1, 3, 5) via momentum matrix elements and the Kramers–Kronig transformation, and the static dielectric constant is taken as the real part at zero photon energy. The outputs are tabulated as structured CSV files for each measured property.

## Reproduction target
Using the DFT protocol described above, produce three CSV files containing: (1) the band gap energy (in eV) and direct/indirect classification for bulk GeSe and for 1-layer through 6-layer GeSe; (2) the work function (in eV) for each layer from 1 to 6; and (3) the static dielectric constant (real part at 0 eV) for 1, 3, and 5 layers. The computed values, which arise from the computational workflow, will be evaluated against independent hidden reference data. The goal is to successfully reproduce the layer-dependent trends in these properties.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry relaxation
- Role: process
- Action: Perform DFT geometry relaxation for bulk GeSe and 1-6 layer GeSe using PBE functional with Grimme D2 van der Waals correction. Use initial lattice parameters: monolayer a=4.27 Å, b=3.98 Å; 2-6 layers a≈4.58 Å, b≈3.96 Å, with 30 Å vacuum. Relax until forces are sufficiently small. Output relaxed structures for subsequent steps.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Self-consistent field (SCF) calculation
- Role: process
- Action: For each relaxed structure, perform a self-consistent field (SCF) calculation using the PBE functional, a dense k‑point mesh, and an appropriate plane‑wave cutoff to obtain the ground‑state charge density, wavefunctions, and Fermi energy.
- Evidence: `/app/outputs/scf.log`

### Step 3: Band structure calculation
- Role: scored (load-bearing)
- Action: Compute band energies along the high‑symmetry k‑path Γ‑X‑Y‑Γ for each system (bulk and 1‑6 layer GeSe) using the SCF charge density. Determine the band gap (VBM‑CBM difference) and whether the gap is direct (both extrema at X) or indirect. Write results to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: columns: layer (string), band_gap_eV (float), direct_indirect (string: 'direct' or 'indirect')
- Scoring: scored by hidden verifier

### Step 4: Work function calculation
- Role: scored
- Action: From the SCF electrostatic potential and Fermi energy, compute the work function as the energy difference between the vacuum level and the Fermi level for each layer 1‑6. Store the layer‑indexed values in work_functions.csv.
- Output file: `/app/outputs/work_functions.csv`
- Format: csv
- Contract: columns: layer (string), work_function_eV (float)
- Scoring: scored by hidden verifier

### Step 5: Static dielectric constant calculation
- Role: scored
- Action: Compute the frequency‑dependent complex dielectric function for odd layers (1L, 3L, 5L) using momentum matrix elements and the Kramers‑Kronig transformation. Extract the real part at zero photon energy as the static dielectric constant. Write the result to static_dielectric_constants.csv.
- Output file: `/app/outputs/static_dielectric_constants.csv`
- Format: csv
- Contract: columns: layer (string, only '1L','3L','5L'), epsilon_static_real (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/work_functions.csv`
- `/app/outputs/static_dielectric_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap energies and direct/indirect classification for bulk and few‑layer GeSe. The checker compares each row against paper‑reported values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `band_gap_eV`, `direct_indirect`
  - `columns`:
    - `layer`: string (e.g. 'bulk','1L','2L',...'6L')
    - `band_gap_eV`: float (eV)
    - `direct_indirect`: string, one of 'direct' or 'indirect'

### work_functions.csv
- path: `/app/outputs/work_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Work function for each layer 1‑6 GeSe. The checker compares each value against paper‑reported work functions with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `work_function_eV`
  - `columns`:
    - `layer`: string (e.g. '1L','2L',...'6L')
    - `work_function_eV`: float (eV)

### static_dielectric_constants.csv
- path: `/app/outputs/static_dielectric_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static dielectric constant (real part at 0 eV) for odd‑layer GeSe. Checker compares to paper‑reported values with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `epsilon_static_real`
  - `columns`:
    - `layer`: string ('1L', '3L', '5L')
    - `epsilon_static_real`: float (dimensionless)

Notes: All quantities must be computed with the PBE functional and Grimme D2 van der Waals correction as used in the target study. The agent must run all process steps to obtain the SCF density and wavefunctions; no pre‑made intermediate data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "band_gap_eV",
          "direct_indirect"
        ],
        "columns": {
          "layer": "string (e.g. 'bulk','1L','2L',...'6L')",
          "band_gap_eV": "float (eV)",
          "direct_indirect": "string, one of 'direct' or 'indirect'"
        }
      },
      "description": "Band gap energies and direct/indirect classification for bulk and few‑layer GeSe. The checker compares each row against paper‑reported values with appropriate tolerances."
    },
    {
      "file": "work_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "work_function_eV"
        ],
        "columns": {
          "layer": "string (e.g. '1L','2L',...'6L')",
          "work_function_eV": "float (eV)"
        }
      },
      "description": "Work function for each layer 1‑6 GeSe. The checker compares each value against paper‑reported work functions with a tolerance."
    },
    {
      "file": "static_dielectric_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "epsilon_static_real"
        ],
        "columns": {
          "layer": "string ('1L', '3L', '5L')",
          "epsilon_static_real": "float (dimensionless)"
        }
      },
      "description": "Static dielectric constant (real part at 0 eV) for odd‑layer GeSe. Checker compares to paper‑reported values with a tolerance."
    }
  ],
  "notes": "All quantities must be computed with the PBE functional and Grimme D2 van der Waals correction as used in the target study. The agent must run all process steps to obtain the SCF density and wavefunctions; no pre‑made intermediate data is provided."
}
```

## How you are scored
A hidden verifier processes your output files independently. For each artifact—band_gaps.csv, work_functions.csv, and static_dielectric_constants.csv—the verifier compares your reported values against hidden reference values using per-quantity tolerances. A directionality-appropriate comparison ensures that a result meeting or exceeding the hidden threshold earns full credit; performance degrades gradually as the result deviates beyond the tolerance. The verified scores from the three artifacts are combined by weight to produce a final reward between 0 and 1. The verification process does not inspect intermediate logs or evidence files; only the content of the three CSV files matters. Reporting the correct values without performing the required DFT workflow will not satisfy the verifier's tolerance requirements.
