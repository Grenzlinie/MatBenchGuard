# Electronic Structure Tuning of Carboxylates on Cu(110) by DFT

## Problem background
In molecular electronics, a key challenge is to control the alignment of molecular orbitals with respect to the metal Fermi level, because this dictates the barrier for charge injection and the transport properties of the molecule–metal junction. This work explores whether the electronic structure of π‑conjugated carboxylic acids anchored on Cu(110) can be systematically tuned by chemical functionalization. The specific focus is on the effect of replacing a CH group by a nitrogen atom in the aromatic ring: for two chemisorbed carboxylates—benzoate (BCA) and ortho‑pyridine‑carboxylate (ortho‑PyCA)—the central question is whether and how this substitution changes the orbital character (σ versus π) of the experimentally relevant highest occupied molecular orbital (HOMO) and alters the HOMO–LUMO energy gap.

## Approach
The approach is grounded in density functional theory (DFT) using the generalized gradient approximation (GGA‑PBE) together with projector‑augmented‑wave (PAW) pseudopotentials. Each molecule is modelled on a periodic five‑layer Cu(110) slab with a 4×5 in‑plane supercell. Geometry optimizations are performed, after which the local density of states (LDOS) at the molecular site is computed and decomposed into σ (in‑plane atomic contributions) and π (perpendicular) components. The key quantity is the HOMOexp–LUMOexp gap, defined as the energy difference between the first prominent occupied and unoccupied LDOS peaks that have significant electron density toward the vacuum side, deliberately excluding the strongly interface‑localised σ1 and σ1* states. By comparing the LDOS and the resulting peak assignment for BCA and ortho‑PyCA, one can quantify how the CH→N substitution modifies the character of the HOMOexp and the size of the gap.

## Reproduction target
For two chemisorbed systems—benzoate (BCA) on Cu(110) and ortho‑pyridine‑carboxylate (ortho‑PyCA) on Cu(110)—perform a complete DFT slab‑model workflow: construct the initial geometries, run geometry optimizations and LDOS calculations with σ/π decomposition, identify the HOMOexp and LUMOexp peaks (excluding the interface‑localised σ1 and σ1* states), determine whether the HOMOexp has σ or π character, and compute the HOMOexp–LUMOexp gap (in eV). For ortho‑PyCA also note the presence of the σ2 orbital. Record the results in a JSON file according to the output contract. The goal is to quantify how the CH→N substitution changes the gap and the nature of the frontier orbital.

## Assets

- Quantum ESPRESSO (or equivalent DFT code supporting GGA-PBE and PAW): https://www.quantum-espresso.org/
- PBE pseudopotentials for Cu, O, C, H, N (PAW method): https://www.quantum-espresso.org/pseudopotentials
- Copper crystal structure (fcc, a=3.64 Å)
- Molecular geometries for benzoate (C7H5O2) and ortho-pyridine-carboxylate (C6H4NO2)

## Workflow steps

### Step 1: Initial geometry preparation
- Role: process
- Action: Construct periodic slab supercells for benzoate (BCA) and ortho-pyridine-carboxylate (ortho-PyCA) chemisorbed on Cu(110) using the experimental Cu lattice constant a=3.64 Å, a 4×5 in-plane supercell, five Cu layers, and deprotonated molecular geometries. Create DFT input files with GGA-PBE functional, PAW pseudopotentials, Γ-point sampling, plane-wave cutoff 500 eV, and dipole correction.
- Evidence: `/app/outputs/geometry_preparation.log`

### Step 2: DFT geometry optimization and LDOS calculation
- Role: process
- Action: Run geometry optimizations for both BCA/Cu(110) and ortho-PyCA/Cu(110) systems. Then compute the local density of states (LDOS) at the molecular site and its decomposition into σ and π contributions. Save the relaxed atomic coordinates and raw LDOS data.
- Evidence: `/app/outputs/ldos_data.tar.gz`

### Step 3: Frontier orbital analysis and gap determination
- Role: scored (load-bearing)
- Action: From the computed LDOS, identify HOMOexp and LUMOexp peaks (the first prominent peaks with significant electron density toward vacuum, excluding the interface-localized σ1 and σ1* states). Determine the orbital character (σ or π) of HOMOexp for each molecule. Compute the HOMOexp-LUMOexp gap (in eV). For ortho-PyCA, note the presence of the σ2 orbital. Write the results to molecule_results.json.
- Output file: `/app/outputs/molecule_results.json`
- Format: json
- Contract: A JSON array of two objects. Each object must contain keys: molecule (string, 'BCA' or 'ortho-PyCA'), HOMOexp_character (string, 'σ' or 'π'), gap_HOMO_exp_LUMO_exp (float, eV), sigma2_present (boolean). For ortho-PyCA, sigma2_present should be true; for BCA, false.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/molecule_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### molecule_results.json
- path: `/app/outputs/molecule_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed electronic structure quantities for BCA and ortho-PyCA. Used to verify that CH→N substitution changes the HOMOexp orbital character from π to σ and yields a gap consistent with the paper's reference (hidden).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `molecule`, `HOMOexp_character`, `gap_HOMO_exp_LUMO_exp`, `sigma2_present`
    - `extra`: False
    - `properties`:
      - `molecule`:
        - `type`: string
      - `HOMOexp_character`:
        - `type`: string
      - `gap_HOMO_exp_LUMO_exp`:
        - `type`: number
        - `unit`: eV
      - `sigma2_present`:
        - `type`: boolean

Notes: The checker compares the agent's reported gap and orbital character against hidden paper-reference values within a tolerance. No raw LDOS recomputation is performed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "molecule_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "molecule",
            "HOMOexp_character",
            "gap_HOMO_exp_LUMO_exp",
            "sigma2_present"
          ],
          "extra": false,
          "properties": {
            "molecule": {
              "type": "string"
            },
            "HOMOexp_character": {
              "type": "string"
            },
            "gap_HOMO_exp_LUMO_exp": {
              "type": "number",
              "unit": "eV"
            },
            "sigma2_present": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Computed electronic structure quantities for BCA and ortho-PyCA. Used to verify that CH→N substitution changes the HOMOexp orbital character from π to σ and yields a gap consistent with the paper's reference (hidden)."
    }
  ],
  "notes": "The checker compares the agent's reported gap and orbital character against hidden paper-reference values within a tolerance. No raw LDOS recomputation is performed."
}
```

## How you are scored
A hidden verifier will read your molecule_results.json. It checks that the JSON has the required structure, then compares your reported HOMOexp character and gap value for each molecule against hidden reference values known to the checker. It also verifies the sigma2_present field. The reward is based on how closely these quantities agree with the reference. Simply reporting numbers without genuinely performing the DFT workflow is not sufficient; the scoring weights are distributed across the stages so that the main computational result carries the largest share.
