# Band Gap and Binding Energy of PCBM Crystals from DFT-LDA

## Problem background
PCBM (phenyl-C61-butyric-acid-methyl-ester) is a fullerene derivative commonly used in organic photovoltaic devices. The way PCBM molecules pack into a crystal influences important electronic properties, particularly the band gap, which affects solar cell efficiency. This task focuses on calculating the ground-state electronic structure of three cubic PCBM crystal phases using density functional theory (DFT) within the local-density approximation (LDA). The aim is to determine the band gaps, gap types, and cohesive energies of these phases, providing insight into how crystal packing alters the electronic properties of methanofullerene solids.

## Approach
The reproduction uses plane-wave DFT with the LDA exchange-correlation functional and the projector-augmented wave (PAW) method to describe core electrons. Three cubic crystal structures are considered: simple cubic (sc), body-centered cubic (bcc), and face-centered cubic (fcc), each containing one PCBM molecule per primitive cell. The lattice constants are held fixed at the values derived from the structural optimization in the original study (sc: 9.9 Å, bcc: 11.1 Å, fcc: 12.1 Å).

First, the atomic positions (including molecular orientation) are relaxed for each crystal while the lattice constants remain fixed. Separately, the total energy of an isolated PCBM molecule is computed inside a large supercell to avoid spurious periodic interactions; this serves as the reference for binding energies. Using the relaxed crystal structures, the electronic band structure is then calculated along the standard high-symmetry k‑paths for each Bravais lattice.

From the band structure, the following quantities are extracted for each phase:
- Band gap (Eg): the difference between the conduction band minimum (CBM) and the valence band maximum (VBM), in eV.
- Gap type: whether the gap is direct (VBM and CBM at the same k‑point) or indirect (VBM and CBM at different k‑points).
- VBM k‑point label and CBM k‑point label: the high‑symmetry point names where the band edges occur.
- Binding energy (Eb): computed as the total energy of the crystal minus the total energy of the isolated molecule, in eV.

Any DFT code that supports LDA and PAW pseudopotentials (e.g., Quantum ESPRESSO, VASP) may be used. The workflow is organised into three ordered steps: (1) isolated molecule relaxation and energy, (2) position relaxation of the cubic crystals, and (3) band structure analysis and binding energy calculation.

## Reproduction target
For each of the three cubic PCBM crystal phases (sc, bcc, fcc) at the fixed lattice constants listed above, calculate the following quantities using DFT‑LDA with PAW pseudopotentials:
- Band gap Eg (eV)
- Gap type ("direct" or "indirect")
- High‑symmetry k‑point labels of the VBM and CBM
- Binding energy Eb = E_crystal − E_isolated molecule (eV)

Report all results in a single JSON file located at `/app/outputs/cubic_results.json`. The required structure is given in the output contract below. The two preceding process steps (isolated molecule and crystal position relaxation) are essential prerequisites and must be executed; they produce evidence files that the verifier may inspect.

## Assets

- DFT package with PAW (e.g., Quantum ESPRESSO, VASP): https://www.quantum-espresso.org/
- PAW pseudopotentials for C, H, O (LDA): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Isolated PCBM molecule relaxation and energy
- Role: process
- Action: Construct the PCBM molecule and relax its atomic positions using DFT-LDA with PAW pseudopotentials in a large supercell to avoid periodic interactions. Obtain the relaxed total energy.
- Evidence: `/app/outputs/isolated_energy.txt`

### Step 2: Position relaxation of cubic PCBM crystals
- Role: process
- Action: For each cubic lattice (sc, bcc, fcc), set up a primitive cell containing one PCBM molecule with the fixed lattice constants (sc: 9.9 Å, bcc: 11.1 Å, fcc: 12.1 Å). Relax all atomic positions while keeping lattice constants fixed. Record the final total energy and relaxed coordinates.
- Evidence: `/app/outputs/crystal_energies.txt`

### Step 3: Band structure and binding energy calculation
- Role: scored (load-bearing)
- Action: Using the relaxed crystal structures, compute the electronic band structure along high-symmetry k-paths for each cubic phase. Determine the band gap Eg = CBM - VBM, identify whether it is direct or indirect, and record the k-point labels of VBM and CBM. Compute the cohesive energy Eb = E_crystal - E_isolated for each structure. Write all results to cubic_results.json.
- Output file: `/app/outputs/cubic_results.json`
- Format: json
- Contract: Top-level keys: 'sc', 'bcc', 'fcc'. Each value is an object with fields: 'Eb' (float, eV), 'Eg' (float, eV), 'gap_type' (string, 'direct' or 'indirect'), 'vbm_kpoint' (string), 'cbm_kpoint' (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cubic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cubic_results.json
- path: `/app/outputs/cubic_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing Eb, Eg, gap type, and VBM/CBM k-point labels for sc, bcc, and fcc PCBM crystals.
- schema:
  - `type`: object
  - `required`: `sc`, `bcc`, `fcc`
  - `properties`:
    - `sc`:
      - `type`: object
      - `properties`:
        - `Eb`:
          - `type`: number
        - `Eg`:
          - `type`: number
        - `gap_type`:
          - `type`: string
        - `vbm_kpoint`:
          - `type`: string
        - `cbm_kpoint`:
          - `type`: string
      - `required`: `Eb`, `Eg`, `gap_type`, `vbm_kpoint`, `cbm_kpoint`
    - `bcc`:
      - `type`: object
      - `properties`:
        - `Eb`:
          - `type`: number
        - `Eg`:
          - `type`: number
        - `gap_type`:
          - `type`: string
        - `vbm_kpoint`:
          - `type`: string
        - `cbm_kpoint`:
          - `type`: string
      - `required`: `Eb`, `Eg`, `gap_type`, `vbm_kpoint`, `cbm_kpoint`
    - `fcc`:
      - `type`: object
      - `properties`:
        - `Eb`:
          - `type`: number
        - `Eg`:
          - `type`: number
        - `gap_type`:
          - `type`: string
        - `vbm_kpoint`:
          - `type`: string
        - `cbm_kpoint`:
          - `type`: string
      - `required`: `Eb`, `Eg`, `gap_type`, `vbm_kpoint`, `cbm_kpoint`

Notes: The agent must compute the isolated molecule total energy to obtain binding energies. Lattice constants are fixed as given. Any reasonable DFT-LDA + PAW implementation may be used; tolerances will absorb code-to-code variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cubic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "sc",
          "bcc",
          "fcc"
        ],
        "properties": {
          "sc": {
            "type": "object",
            "properties": {
              "Eb": {
                "type": "number"
              },
              "Eg": {
                "type": "number"
              },
              "gap_type": {
                "type": "string"
              },
              "vbm_kpoint": {
                "type": "string"
              },
              "cbm_kpoint": {
                "type": "string"
              }
            },
            "required": [
              "Eb",
              "Eg",
              "gap_type",
              "vbm_kpoint",
              "cbm_kpoint"
            ]
          },
          "bcc": {
            "type": "object",
            "properties": {
              "Eb": {
                "type": "number"
              },
              "Eg": {
                "type": "number"
              },
              "gap_type": {
                "type": "string"
              },
              "vbm_kpoint": {
                "type": "string"
              },
              "cbm_kpoint": {
                "type": "string"
              }
            },
            "required": [
              "Eb",
              "Eg",
              "gap_type",
              "vbm_kpoint",
              "cbm_kpoint"
            ]
          },
          "fcc": {
            "type": "object",
            "properties": {
              "Eb": {
                "type": "number"
              },
              "Eg": {
                "type": "number"
              },
              "gap_type": {
                "type": "string"
              },
              "vbm_kpoint": {
                "type": "string"
              },
              "cbm_kpoint": {
                "type": "string"
              }
            },
            "required": [
              "Eb",
              "Eg",
              "gap_type",
              "vbm_kpoint",
              "cbm_kpoint"
            ]
          }
        }
      },
      "description": "JSON file containing Eb, Eg, gap type, and VBM/CBM k-point labels for sc, bcc, and fcc PCBM crystals."
    }
  ],
  "notes": "The agent must compute the isolated molecule total energy to obtain binding energies. Lattice constants are fixed as given. Any reasonable DFT-LDA + PAW implementation may be used; tolerances will absorb code-to-code variations."
}
```

## How you are scored
A hidden verifier evaluates your submitted artifacts. The main scored artifact is `/app/outputs/cubic_results.json`; the verifier compares the reported band gaps, gap types, k‑point labels, and binding energies for all three structures against a hidden reference derived from the original study. The two process steps (`isolated_energy.txt` and `crystal_energies.txt`) are also audited to confirm that the necessary computations were performed. The final reward is a weighted combination of the correctness of the scored output and the presence of the required evidence. You must genuinely execute the DFT workflow to obtain the correct results; simply guessing or fabricating values will not pass the hidden checks.
