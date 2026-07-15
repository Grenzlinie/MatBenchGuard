# DFT Electronic Structure of BaTiO3, SrTiO3, and BST Heterostructure

## Problem background
BaₓSr₁₋ₓTiO₃ (BST) solid solutions are promising candidates for memory cell capacitors in highly integrated dynamic random access memory. Understanding their electronic structure is essential to explain their dielectric and ferroelectric properties. Hybrid density functional theory (DFT) calculations can accurately reproduce experimental lattice constants and band gaps of the parent perovskites BaTiO₃ and SrTiO₃, and can predict the electronic properties of layered BST heterostructures, including band gap changes and the orbital character of valence and conduction bands.

## Approach
You will perform first-principles electronic structure calculations using a hybrid exchange-correlation functional (B3PW, with 20% non-local Fock exchange). You must use small-core effective core potentials (Hay-Wadt) for Ti, Sr, and Ba, and all-electron Gaussian basis sets for O. The calculations will be carried out on cubic primitive unit cells of BaTiO₃ and SrTiO₃, and on a 2×2×2 supercell of Ba₀.₅Sr₀.₅TiO₃ with alternating Ba/Sr layers. For each system, you will optimize the lattice constant at fixed ideal perovskite atomic positions, then compute the electronic band gap as the energy difference between the valence band maximum and conduction band minimum. For the BST supercell, you will additionally compute the projected density of states (PDOS) decomposed into O 2p, Ti 3d, Ba, and Sr contributions. Use an open‑source periodic DFT code (e.g., CP2K) that supports hybrid functionals and the required pseudopotentials/basis sets.

## Reproduction target
Your goal is to reproduce the procedure and output the following quantities: (1) optimized lattice constants of cubic BaTiO₃ and SrTiO₃; (2) optical band gaps of BaTiO₃, SrTiO₃, and the BST heterostructure; (3) the projected density of states of the BST supercell. You must write these results to the specified output files in the required formats. Do NOT aim for a specific numeric value; instead, follow the defined method exactly using public resources, and report the computed results as they come out of your calculations.

## Assets

- CP2K open-source DFT code: https://www.cp2k.org/
- Hay-Wadt small-core ECPs for Ti, Sr, Ba; all-electron for O: CP2K POTENTIAL library
- Gaussian basis sets for O, Ti, Sr, Ba (quality comparable to O-8-411(1d)G, Ti-411(311d)G, Sr/Ba-311(1d)G): CP2K BASIS set library

## Workflow steps

### Step 1: Optimize BaTiO3 and SrTiO3 lattice constants
- Role: scored
- Action: Perform DFT geometry optimization on cubic primitive unit cells of BaTiO3 and SrTiO3 using the B3PW hybrid functional (20% non-local Fock exact exchange), Hay-Wadt small-core effective core potentials for Ti, Sr/Ba, appropriate Gaussian basis sets, and conjugate-gradient optimization. Extract the optimized lattice constants in Å and write them to the output file.
- Output file: `/app/outputs/lattice_constants.json`
- Format: json
- Contract: {"BaTiO3": <float>, "SrTiO3": <float>}
- Scoring: scored by hidden verifier

### Step 2: Construct and optimize BST layered supercell
- Role: process
- Action: Build a 2×2×2 supercell of Ba0.5Sr0.5TiO3 with alternating Ba/Sr layers (as shown in the paper). Optimize the lattice constant using DFT with the same functional, ECPs, basis sets, and conjugate-gradient optimizer, keeping atomic positions at ideal perovskite sites. Save the optimized supercell structure as an XYZ file for downstream steps.
- Evidence: `/app/outputs/bst_supercell_optimized.xyz`

### Step 3: Compute band gaps for BaTiO3, SrTiO3, and BST
- Role: scored (load-bearing)
- Action: For the optimized structures from steps 1 and 2, compute the electronic band structure (or density of states) and determine the optical band gap as the energy difference between the valence band maximum and conduction band minimum. Write the three gaps (in eV) to the output file.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"BaTiO3": <float>, "SrTiO3": <float>, "BST": <float>}
- Scoring: scored by hidden verifier

### Step 4: Calculate BST projected density of states
- Role: scored
- Action: Using the optimized BST supercell from step 2, compute the projected density of states (PDOS) projected onto O 2p, Ti 3d, Ba, and Sr atomic orbitals. Produce a CSV file with columns: energy (eV, relative to the valence band maximum), total DOS, Ti_d, O_p, Ba_p, and Sr_p contributions. DOS values are in arbitrary units.
- Output file: `/app/outputs/partial_dos_BST.csv`
- Format: csv
- Contract: columns: energy (float, eV), total (float), Ti_d (float), O_p (float), Ba_p (float), Sr_p (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/partial_dos_BST.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.json
- path: `/app/outputs/lattice_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constants of cubic BaTiO3 and SrTiO3 from DFT geometry optimization.
- schema:
  - `type`: object
  - `required`:
    - `BaTiO3`: number
    - `SrTiO3`: number
  - `units`:
    - `BaTiO3`: Å
    - `SrTiO3`: Å

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optical band gaps (VBM–CBM) for BaTiO3, SrTiO3, and the BST heterostructure.
- schema:
  - `type`: object
  - `required`:
    - `BaTiO3`: number
    - `SrTiO3`: number
    - `BST`: number
  - `units`:
    - `BaTiO3`: eV
    - `SrTiO3`: eV
    - `BST`: eV

### partial_dos_BST.csv
- path: `/app/outputs/partial_dos_BST.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Projected density of states of the BST supercell. Used to verify orbital character of valence and conduction band edges.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total`, `Ti_d`, `O_p`, `Ba_p`, `Sr_p`
  - `units`:
    - `energy`: eV (relative to VBM)
    - `total`: arbitrary
    - `Ti_d`: arbitrary
    - `O_p`: arbitrary
    - `Ba_p`: arbitrary
    - `Sr_p`: arbitrary

Notes: Electron density difference maps are omitted as qualitative and not numerically checkable. The agent must re‑run the DFT workflow using an open‑source code (CP2K) with the B3PW hybrid functional and Hay-Wadt small‑core ECPs; all inputs are public. Scoring compares computed lattice constants and band gaps to paper‑reported values (hidden gold) with appropriate tolerances, and checks orbital dominance trends in the PDOS.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BaTiO3": "number",
          "SrTiO3": "number"
        },
        "units": {
          "BaTiO3": "Å",
          "SrTiO3": "Å"
        }
      },
      "description": "Optimized lattice constants of cubic BaTiO3 and SrTiO3 from DFT geometry optimization."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BaTiO3": "number",
          "SrTiO3": "number",
          "BST": "number"
        },
        "units": {
          "BaTiO3": "eV",
          "SrTiO3": "eV",
          "BST": "eV"
        }
      },
      "description": "Optical band gaps (VBM–CBM) for BaTiO3, SrTiO3, and the BST heterostructure."
    },
    {
      "file": "partial_dos_BST.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total",
          "Ti_d",
          "O_p",
          "Ba_p",
          "Sr_p"
        ],
        "units": {
          "energy": "eV (relative to VBM)",
          "total": "arbitrary",
          "Ti_d": "arbitrary",
          "O_p": "arbitrary",
          "Ba_p": "arbitrary",
          "Sr_p": "arbitrary"
        }
      },
      "description": "Projected density of states of the BST supercell. Used to verify orbital character of valence and conduction band edges."
    }
  ],
  "notes": "Electron density difference maps are omitted as qualitative and not numerically checkable. The agent must re‑run the DFT workflow using an open‑source code (CP2K) with the B3PW hybrid functional and Hay-Wadt small‑core ECPs; all inputs are public. Scoring compares computed lattice constants and band gaps to paper‑reported values (hidden gold) with appropriate tolerances, and checks orbital dominance trends in the PDOS."
}
```

## How you are scored
A hidden verifier will independently check each of the three output files. It will compare your computed lattice constants, band gaps, and PDOS characteristics against objective reference expectations derived from the original study. The verifier combines the scores of the individual artifacts by weight to produce a final reward between 0 and 1. Reporting a number close to a known reference is not sufficient; you must execute the outlined workflow faithfully and produce the required artifacts as specified. The verifier's criteria are hidden, so treat every step with care.
