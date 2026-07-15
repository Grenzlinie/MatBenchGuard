# Screw dislocation-solute interaction energies and core reconstruction in bcc Fe from DFT

## Problem background
In body‑centred cubic (bcc) iron, the 1/2⟨111⟩ screw dislocation normally adopts a symmetric easy core. Previous work has shown that carbon interstitials can stabilise a hard core configuration, forming regular trigonal prisms of iron atoms around the solutes. This study investigates whether the same reconstruction occurs for the neighbouring interstitial solutes boron, nitrogen, and oxygen, and quantifies the resulting dislocation–solute interactions.

## Approach
The method uses spin‑polarised DFT with the PAW formalism and the PBE GGA functional. Dislocations are modelled with periodic quadrupolar dipole arrays in supercells of 135 and 270 iron atoms, allowing solute separations of 1b and 2b along the ⟨111⟩ dislocation line. Reference energies for pure Fe bulk, isolated solutes (B, C, N, O) in their preferred interstitial sites, and pure dislocation cores (easy and hard) are computed first. Then dislocations with solutes placed in first‑neighbour octahedral‑like positions (the E₁ configuration) are relaxed. For each solute and separation, the final total energy and the final core configuration (easy or hard) are recorded. From these energies one can derive the solute–dislocation interaction energy and the solute–solute interaction along the line.

## Reproduction target
Compute and submit (i) a JSON file with raw DFT total energies for all reference and solute‑decorated dislocation systems, from which the hidden verifier recomputes the solute–dislocation interaction energy (E_int) and the solute–solute interaction energy (V_XX) along the dislocation line, and (ii) a JSON file of boolean flags indicating whether each relaxation from the initial easy‑core plus E₁ solute configuration resulted in the hard core.

The target quantities are defined as:
E_int = ½ E_disloc+X + E_bulk – ½ E_disloc – E_X,
V_XX = ½ (E_disloc+X(1b) + E_hard(1b) – E_disloc+X(2b)),
where E_disloc+X is the total energy of the dislocation dipole with two solutes, E_disloc is the energy of the easy‑core dislocation dipole of the same length, E_bulk is the energy of a perfect bcc Fe supercell, E_X is the energy of a perfect cell with one solute in its stable octahedral site, and E_hard(1b) is the energy of the hard‑core dislocation dipole of length 1b.

## Assets

- Quantum ESPRESSO or GPAW (open-source DFT with PAW, GGA-PBE): https://www.quantum-espresso.org/
- PAW pseudopotentials for Fe, B, C, N, O (PBE, without semicore for Fe, 2s2p for solutes): https://pseudodojo.org/
- Atomic Simulation Environment (ASE): pip install ase

## Workflow steps

### Step 1: Bulk reference DFT calculations
- Role: process
- Action: Perform spin-polarised DFT (PAW, PBE GGA) for a perfect bcc Fe supercell (250-atom or similar) to obtain E_bulk. For each solute X = B, C, N, O, place a single solute in an octahedral interstitial site and relax the supercell to obtain E_X. Record the total energies in a temporary file for later use.
- Evidence: `/app/outputs/bulk_ref_energies.json`

### Step 2: Pure dislocation reference DFT calculations
- Role: process
- Action: Construct a quadrupolar array of 1/2⟨111⟩ screw dislocation dipoles in bcc Fe using cells containing 135 Fe atoms (1b length) and 270 Fe atoms (2b length). Relax the easy-core dipole in both cells to obtain E_easy_1b and E_easy_2b. Constrain the three central ⟨111⟩ Fe columns to the same altitude to relax the hard-core dipole (1b cell) and obtain E_hard_1b. Store the energies in a temporary file.
- Evidence: `/app/outputs/dislocation_ref_energies.json`

### Step 3: Dislocation–solute relaxation simulations
- Role: process
- Action: For each solute X ∈ {B, C, N, O} and each solute separation distance d ∈ {1b, 2b} along ⟨111⟩, prepare a dislocation dipole cell with two solute atoms placed in the E₁ octahedral-like first-neighbour positions near each core. Relax atomic positions until forces fall below 10⁻² eV/Å. Additionally, for Fe(N) with d = 1b, perform a separate relaxation starting with the N atom at the centre of the hard-core prismatic site. For every case, record the final total energy E_disloc_X_d and note the final core configuration (easy or hard). Save all raw results in a temporary file.
- Evidence: `/app/outputs/relaxation_results.json`

### Step 4: Compile total energy table
- Role: scored (load-bearing)
- Action: From the data collected in the previous steps, produce a scored file total_energies.json containing all raw total energies: E_bulk (float), E_X_B, E_X_C, E_X_N, E_X_O (floats), E_easy_1b, E_easy_2b, E_hard_1b (floats), and for each solute and distance (1b, 2b) the final energy E_disloc_X_1b, E_disloc_X_2b (floats). For Fe(N) 1b use the lower energy from the hard-core relaxation.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: Keys: E_bulk (float), E_X_B (float), E_X_C (float), E_X_N (float), E_X_O (float), E_easy_1b (float), E_easy_2b (float), E_hard_1b (float), E_disloc_B_1b (float), E_disloc_B_2b (float), E_disloc_C_1b (float), E_disloc_C_2b (float), E_disloc_N_1b (float), E_disloc_N_2b (float), E_disloc_O_1b (float), E_disloc_O_2b (float). All energies in eV.
- Scoring: scored by hidden verifier

### Step 5: Reconstruction outcomes
- Role: scored
- Action: Produce a second scored file summarizing whether each relaxation from the E₁ configuration led to the hard core.
- Output file: `/app/outputs/reconstruction_outcomes.json`
- Format: json
- Contract: Keys: B_1b, B_2b, C_1b, C_2b, N_1b, N_2b, O_1b, O_2b (each boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`
- `/app/outputs/reconstruction_outcomes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw DFT total energies from which the checker recomputes solute-dislocation interaction energies E_int and solute-solute interaction energies V_XX, comparing to hidden paper-reported values within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `E_bulk`: float
    - `E_X_B`: float
    - `E_X_C`: float
    - `E_X_N`: float
    - `E_X_O`: float
    - `E_easy_1b`: float
    - `E_easy_2b`: float
    - `E_hard_1b`: float
    - `E_disloc_B_1b`: float
    - `E_disloc_B_2b`: float
    - `E_disloc_C_1b`: float
    - `E_disloc_C_2b`: float
    - `E_disloc_N_1b`: float
    - `E_disloc_N_2b`: float
    - `E_disloc_O_1b`: float
    - `E_disloc_O_2b`: float
  - `units`: eV

### reconstruction_outcomes.json
- path: `/app/outputs/reconstruction_outcomes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Boolean flags indicating whether the relaxation from E₁ configuration resulted in the hard core; compared to expected pattern (all true except N_1b=false).
- schema:
  - `type`: object
  - `required`:
    - `B_1b`: boolean
    - `B_2b`: boolean
    - `C_1b`: boolean
    - `C_2b`: boolean
    - `N_1b`: boolean
    - `N_2b`: boolean
    - `O_1b`: boolean
    - `O_2b`: boolean

Notes: All energies in eV. The checker recomputes E_int and V_XX from total_energies.json using the formulas described in the instruction; the reconstruction_outcomes.json is compared to the paper's reported spontaneity pattern.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "E_bulk": "float",
          "E_X_B": "float",
          "E_X_C": "float",
          "E_X_N": "float",
          "E_X_O": "float",
          "E_easy_1b": "float",
          "E_easy_2b": "float",
          "E_hard_1b": "float",
          "E_disloc_B_1b": "float",
          "E_disloc_B_2b": "float",
          "E_disloc_C_1b": "float",
          "E_disloc_C_2b": "float",
          "E_disloc_N_1b": "float",
          "E_disloc_N_2b": "float",
          "E_disloc_O_1b": "float",
          "E_disloc_O_2b": "float"
        },
        "units": "eV"
      },
      "description": "Raw DFT total energies from which the checker recomputes solute-dislocation interaction energies E_int and solute-solute interaction energies V_XX, comparing to hidden paper-reported values within tolerance."
    },
    {
      "file": "reconstruction_outcomes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B_1b": "boolean",
          "B_2b": "boolean",
          "C_1b": "boolean",
          "C_2b": "boolean",
          "N_1b": "boolean",
          "N_2b": "boolean",
          "O_1b": "boolean",
          "O_2b": "boolean"
        }
      },
      "description": "Boolean flags indicating whether the relaxation from E₁ configuration resulted in the hard core; compared to expected pattern (all true except N_1b=false)."
    }
  ],
  "notes": "All energies in eV. The checker recomputes E_int and V_XX from total_energies.json using the formulas described in the instruction; the reconstruction_outcomes.json is compared to the paper's reported spontaneity pattern."
}
```

## How you are scored
A hidden verifier independently scores each output file. For `total_energies.json`, the verifier recomputes E_int and V_XX from the submitted energies and compares them to expected reference values (with an allowance for differences between DFT codes). For `reconstruction_outcomes.json`, the verifier compares each boolean flag to the expected pattern. The final reward is a weighted average of the scores, with `total_energies.json` carrying the largest weight. Reporting numbers that match the paper is not sufficient; the verifier reconstructs the quantities of interest from your raw energies and configuration records.
