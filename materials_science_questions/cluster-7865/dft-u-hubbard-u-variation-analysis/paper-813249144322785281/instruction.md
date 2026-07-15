# Magnetic Ground State and Mott Gap Opening in a Frustrated Spinel via DFT+U

## Problem background
MgV₂O₄ is a frustrated vanadium spinel that undergoes a structural transition from cubic to tetragonal at low temperature, followed by magnetic ordering. Standard local spin density approximation (LSDA) calculations predict a metallic ground state, yet experimentally MgV₂O₄ is a Mott insulator. Understanding how electronic correlations and magnetic ordering together open the insulating gap is essential to understanding the physics of this class of materials.

## Approach
Use density functional theory (DFT) as implemented in the open-source plane‑wave code Quantum ESPRESSO. Build supercells corresponding to three magnetic configurations: ferromagnetic (FM), antiferromagnetic (AFM), and an alternative antiferromagnetic (AFMA). Perform self‑consistent LSDA total‑energy calculations on each supercell to identify the magnetic ground state. Then, for the lowest‑energy magnetic ordering, compute the electronic band structure at four levels of theory: LSDA, LSDA+U with Hubbard U−J = 2 eV, LSDA+U with U−J = 4 eV, and LSDA+U with spin‑orbit coupling (SO) included. Extract the fundamental band gap at the Fermi level for each case and examine how the gap evolves with correlations and spin‑orbit coupling.

## Reproduction target
1. Determine the magnetic ground state by computing and comparing the total energies of the FM, AFM, and AFMA supercells.  2. For the ground‑state magnetic configuration, compute the fundamental electronic band gap (at the Fermi level) using LSDA, LSDA+U (U−J = 2 eV), LSDA+U (U−J = 4 eV), and LSDA+U+SO. Verify that including on‑site Coulomb correlations opens a gap and that the gap increases with the Hubbard U value and with the addition of spin‑orbit coupling.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (or equivalent open-source library): https://www.materialscloud.org/discover/sssp/table
- Crystal structure data for MgV2O4 (experimental): 10.1103/PhysRevB.82.140406

## Workflow steps

### Step 1: Build supercell models for magnetic configurations
- Role: process
- Action: Construct supercells for the ferromagnetic (FM), antiferromagnetic (AFM), and alternative antiferromagnetic (AFMA) magnetic configurations of MgV₂O₄ using the experimental low-temperature tetragonal crystal structure. Use the published lattice constants a=5.920 Å, c=8.323 Å and atomic positions from Wheeler et al., Phys. Rev. B 82, 140406 (2010). The supercell should contain 8 nonequivalent V ions. Export the structures in a format suitable for Quantum ESPRESSO.
- Evidence: `/app/outputs/supercell_structures.zip`

### Step 2: Compute total energies for magnetic configurations
- Role: scored (load-bearing)
- Action: Perform self-consistent LSDA calculations for the FM, AFM, and AFMA supercells using Quantum ESPRESSO. Use appropriate k-point sampling and convergence criteria. Extract the total energy for each configuration and write to total_energies.json.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: {"FM": <float>, "AFM": <float>, "AFMA": <float>}
- Scoring: scored by hidden verifier

### Step 3: Compute band gaps for AFM ground state
- Role: scored
- Action: For the AFM supercell (lowest-energy configuration), perform band structure calculations using Quantum ESPRESSO with four levels of theory: (i) LSDA, (ii) LSDA+U with U-J=2 eV, (iii) LSDA+U with U-J=4 eV, and (iv) LSDA+U+SO (U-J=2 eV, spin-orbit coupling). Extract the fundamental band gap at the Fermi level for each method and write the results to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: [{"method": "string", "band_gap_eV": <float>}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Total energies of FM, AFM, and AFMA magnetic configurations. The checker verifies that AFM energy is the lowest (by a margin) to confirm the magnetic ground state.
- schema:
  - `type`: object
  - `required`:
    - `FM`: number (energy)
    - `AFM`: number (energy)
    - `AFMA`: number (energy)
  - `items`: object
  - `units`:
    - `FM`: Ry or eV
    - `AFM`: Ry or eV
    - `AFMA`: Ry or eV

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Band gaps for LSDA, LSDA+U (U-J=2 eV), LSDA+U (U-J=4 eV), and LSDA+U+SO. The checker verifies that the gap opens and increases with correlations and spin-orbit coupling, and that the LSDA gap is metallic.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `method`: string
      - `band_gap_eV`: number
  - `required_columns`: `method`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

Notes: All energies may be reported in Ry or eV; the checker normalises. The agent is free to use any open-source pseudopotential library and choose appropriate computational parameters.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "FM": "number (energy)",
          "AFM": "number (energy)",
          "AFMA": "number (energy)"
        },
        "items": {},
        "units": {
          "FM": "Ry or eV",
          "AFM": "Ry or eV",
          "AFMA": "Ry or eV"
        }
      },
      "description": "Total energies of FM, AFM, and AFMA magnetic configurations. The checker verifies that AFM energy is the lowest (by a margin) to confirm the magnetic ground state."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "method": "string",
            "band_gap_eV": "number"
          }
        },
        "required_columns": [
          "method",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Band gaps for LSDA, LSDA+U (U-J=2 eV), LSDA+U (U-J=4 eV), and LSDA+U+SO. The checker verifies that the gap opens and increases with correlations and spin-orbit coupling, and that the LSDA gap is metallic."
    }
  ],
  "notes": "All energies may be reported in Ry or eV; the checker normalises. The agent is free to use any open-source pseudopotential library and choose appropriate computational parameters."
}
```

## How you are scored
A hidden verifier independently evaluates each scored workflow step. For the magnetic ground state, it validates that the AFM total energy is the lowest among the three configurations (with a required margin). For the band gaps, it checks that the LSDA gap is metallic (near zero), that the LSDA+U gaps are positive and increase with increasing U, and that the LSDA+U+SO gap is no smaller than the LSDA+U (U−J = 2 eV) gap. The final reward is a weighted combination of the scores from the two stages. Simply reporting a number is not enough; the verifier assesses the computed artifacts.
