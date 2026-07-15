# First-principles DFT electronic structure of Mg2Al4Si5O18

## Problem background
Mg2Al4Si5O18 (cordierite) is an orthorhombic silicate host with potential for rare-earth activated luminescence. Its intrinsic electronic structure — in particular the band gap at the Γ point and the orbital character of the valence band maximum and conduction band minimum — governs optical absorption and the host’s ability to accommodate activator energy levels. A first-principles calculation of these properties for the pristine compound provides a foundation for understanding the luminescence of doped variants.

## Approach
Use plane-wave density functional theory (DFT) within the generalized gradient approximation (GGA) in the PBE parametrization. Set up the crystal unit cell from the known orthorhombic structure (space group Cccm). Perform a self-consistent field (SCF) calculation to obtain converged ground-state charge density and Kohn-Sham eigenvalues. From the SCF results, extract the direct band gap at the Γ point and compute the projected density of states (PDOS) to assign the dominant atomic-orbital contributions to the valence band maximum (HOMO) and conduction band minimum (LUMO). The calculation is carried out with the open-source Quantum ESPRESSO code and standard SSSP efficiency pseudopotentials.

## Reproduction target
Produce two scored artefacts: (1) a JSON file reporting the direct band gap in electronvolts at the Γ point, together with metadata identifying the method, code and plane-wave cutoff used; (2) a JSON file stating the dominant orbital types for the HOMO and the LUMO, as derived from the PDOS (output as strings, e.g., 'O p' or 'Si s,p'). The calculation must be performed on the pristine Mg2Al4Si5O18 host without dopants.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of Mg2Al4Si5O18 (cordierite): https://materialsproject.org/materials/mp-2984/

## Workflow steps

### Step 1: Structure preparation
- Role: process
- Action: Obtain the CIF file for orthorhombic Mg2Al4Si5O18 (space group Cccm) and convert it into a Quantum ESPRESSO input file containing the crystal unit cell (lattice vectors, atomic positions and species).
- Evidence: `/app/outputs/structure_setup.log`

### Step 2: SCF calculation
- Role: process
- Action: Run a self-consistent field (SCF) calculation for the pristine MASO crystal using Quantum ESPRESSO with GGA-PBE exchange-correlation, a suitable plane-wave cutoff and k-point mesh, producing a converged charge density and Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/scf_output.log`

### Step 3: Extract direct band gap
- Role: scored (load-bearing)
- Action: Post-process the SCF results to determine the direct band gap at the Γ point. Write the extracted gap value in eV along with method metadata.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"direct_gap": <float>, "method": "GGA-PBE", "code": "Quantum ESPRESSO", "cutoff_ry": <float>}
- Scoring: scored by hidden verifier

### Step 4: Determine HOMO/LUMO orbital character
- Role: scored
- Action: Compute the projected density of states (PDOS) and identify the dominant atomic-orbital contributions to the valence band maximum (HOMO) and conduction band minimum (LUMO). Write the orbital strings.
- Output file: `/app/outputs/dos_analysis.json`
- Format: json
- Contract: {"homo_dominant_orbital": "<string>", "lumo_dominant_orbital": "<string>"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/dos_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted direct band gap at the Γ point and the DFT settings used.
- schema:
  - `type`: object
  - `required`: `direct_gap`, `method`, `code`, `cutoff_ry`
  - `properties`:
    - `direct_gap`:
      - `type`: number
      - `description`: Direct band gap in eV
    - `method`:
      - `type`: string
    - `code`:
      - `type`: string
    - `cutoff_ry`:
      - `type`: number

### dos_analysis.json
- path: `/app/outputs/dos_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dominant atomic-orbital character of the HOMO and LUMO.
- schema:
  - `type`: object
  - `required`: `homo_dominant_orbital`, `lumo_dominant_orbital`
  - `properties`:
    - `homo_dominant_orbital`:
      - `type`: string
    - `lumo_dominant_orbital`:
      - `type`: string

Notes: Only results for the pristine MASO host are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "direct_gap",
          "method",
          "code",
          "cutoff_ry"
        ],
        "properties": {
          "direct_gap": {
            "type": "number",
            "description": "Direct band gap in eV"
          },
          "method": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "cutoff_ry": {
            "type": "number"
          }
        }
      },
      "description": "Extracted direct band gap at the Γ point and the DFT settings used."
    },
    {
      "file": "dos_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "homo_dominant_orbital",
          "lumo_dominant_orbital"
        ],
        "properties": {
          "homo_dominant_orbital": {
            "type": "string"
          },
          "lumo_dominant_orbital": {
            "type": "string"
          }
        }
      },
      "description": "Dominant atomic-orbital character of the HOMO and LUMO."
    }
  ],
  "notes": "Only results for the pristine MASO host are scored."
}
```

## How you are scored
A hidden verifier inspects the two output files you write — band_gap.json and dos_analysis.json — and checks that they conform to the declared schema. For each scored artefact, the verifier compares the value(s) you report against a hidden reference result using a predetermined tolerance or string match (as appropriate). The two artefacts are weighted; the final reward is the sum of the weighted scores, capped at 1.0. Simply printing a plausible number without actually executing the DFT SCF will not satisfy the checker, because the required output must be produced by a genuine workflow.
