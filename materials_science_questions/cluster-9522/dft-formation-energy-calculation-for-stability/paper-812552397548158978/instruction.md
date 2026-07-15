# DFT Formation Energy Calculation for CsSnI3 Polymorph Stability

## Problem background
CsSnI3 exhibits two polymorphs near ambient temperature: a black orthorhombic perovskite (B‑γ) phase suitable for optoelectronics, and a yellow one‑dimensional double‑chain (Y) phase that is optically inactive. The B‑γ phase is metastable and readily transforms into the Y phase, especially in the presence of moisture, followed by irreversible oxidation to Cs2SnI6. It has been reported that doping with small amounts of SbI3 or BiI3 (≈3 mol%) significantly suppresses this phase transition, possibly by reversing the thermodynamic stability of the two phases. The underlying hypothesis is that doping modifies the electronic structure, thereby lowering the heat of formation of the B‑γ phase below that of the Y phase. The primary computational task is therefore to compute the heats of formation (ΔHF, in eV per formula unit) for pristine and MI3‑doped (M = Sb, Bi) B‑γ and Y CsSnI3 and determine the relative stability ordering.

## Approach
The calculation proceeds by density functional theory (DFT) using the PBEsol exchange‑correlation functional, which has been shown to describe the energetics of these halide perovskites reasonably well. From the publicly available crystal structures of the B‑γ (ICSD 262926) and Y (ICSD 262927) phases, 2×2×2 supercells (32 formula units) are built. For pristine systems these correspond to Cs32Sn32I96. For doped systems, one Sn atom is replaced by the dopant (Sb or Bi) and an additional interstitial I atom is introduced to preserve charge neutrality, giving Cs32Sn31M1I97. The total energies of all supercells (pristine B‑γ, pristine Y, Sb‑doped B‑γ, Sb‑doped Y, Bi‑doped B‑γ, Bi‑doped Y) are obtained after full geometry optimization. In addition, the energies per atom (μi) of the elemental references (Cs, Sn, I, Sb, Bi) in their standard crystalline phases are computed under the same DFT conditions. The heat of formation for each supercell is then ΔHF = Etotal(supercell) – Σi ni μi, normalized by 32 to obtain eV per formula unit. Comparing the resulting ΔHF values across phases and doping conditions reveals whether the relative stability ordering is altered.

## Reproduction target
Produce a CSV file `formation_energies.csv` with columns `phase` (one of 'B‑gamma' or 'Y'), `doping` (one of 'pristine', 'Sb', 'Bi'), and `delta_HF` (eV per formula unit) for all six systems. Compute the formation energies following the DFT protocol described in the Approach section. The hidden verifier will evaluate the submitted energies based on the thermodynamic stability relationships they imply.

## Assets

- B-gamma CsSnI3 crystal structure: ICSD 262926
- Y CsSnI3 crystal structure: ICSD 262927
- Elemental reference crystal structures
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBEsol pseudopotentials: SSSP library via qe-pseudo-download

## Workflow steps

### Step 1: Supercell Construction
- Role: process
- Action: Build 2x2x2 supercells for B-gamma and Y CsSnI3: pristine (Cs32Sn32I96), and 3 mol% SbI3- and BiI3-doped compositions (Cs32Sn31M1I97, M = Sb or Bi). For doping, substitute one Sn with M and add an interstitial I atom. Use the crystal structures from ICSD 262926 (B-gamma) and 262927 (Y).
- Evidence: `/app/outputs/supercells.pkl`

### Step 2: DFT Total Energy Calculations
- Role: process
- Action: Perform DFT geometry optimization and total energy calculation for all six supercells (pristine B-gamma, pristine Y, Sb-doped B-gamma, Sb-doped Y, Bi-doped B-gamma, Bi-doped Y) and for the elemental reference phases (Cs, Sn, I, Sb, Bi) using Quantum ESPRESSO with the PBEsol functional. Use a plane-wave cutoff of 350 eV and appropriate k-point sampling. Extract the total energy (E_total) for each system.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Heat of Formation Calculation
- Role: scored (load-bearing)
- Action: Compute the heat of formation ΔH_F = E_total(supercell) – Σ_i n_i μ_i, where μ_i are the per-atom DFT energies of the elemental references. Normalize by the number of formula units (32) to obtain ΔH_F in eV per formula unit. Output a CSV table with phase (B-gamma or Y), doping (pristine, Sb, Bi), and delta_HF (eV/f.u.) for all six conditions.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: phase (string, one of 'B-gamma' or 'Y'), doping (string, one of 'pristine','Sb','Bi'), delta_HF (float, eV/f.u.)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed heats of formation for pristine and doped CsSnI3 in the B-gamma and Y phases. The scoring verifies the relative ordering of formation energies across phases and doping conditions.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `doping`, `delta_HF`
  - `columns`:
    - `phase`: string (one of 'B-gamma' or 'Y')
    - `doping`: string (one of 'pristine', 'Sb', 'Bi')
    - `delta_HF`: float (eV per formula unit)

Notes: Scoring is based on structural ordering: for pristine, ΔH_F(Y) must be lower than ΔH_F(B-gamma); for Sb- and Bi-doped, ΔH_F(B-gamma) must be lower than ΔH_F(Y). Absolute values contribute only to a minor consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "doping",
          "delta_HF"
        ],
        "columns": {
          "phase": "string (one of 'B-gamma' or 'Y')",
          "doping": "string (one of 'pristine', 'Sb', 'Bi')",
          "delta_HF": "float (eV per formula unit)"
        }
      },
      "description": "Computed heats of formation for pristine and doped CsSnI3 in the B-gamma and Y phases. The scoring verifies the relative ordering of formation energies across phases and doping conditions."
    }
  ],
  "notes": "Scoring is based on structural ordering: for pristine, ΔH_F(Y) must be lower than ΔH_F(B-gamma); for Sb- and Bi-doped, ΔH_F(B-gamma) must be lower than ΔH_F(Y). Absolute values contribute only to a minor consistency check."
}
```

## How you are scored
A hidden verifier reads the submitted `formation_energies.csv` and assigns a score based on a comparison of the relative formation energies across the six conditions. The verifier independently evaluates the submitted artifact; no manually reported aggregate number is accepted in lieu of the required CSV file.
