# Classical MD and Tight-binding Transport Simulation for Chirality-dependent Conductance in Carbon Nanotubes

## Problem background
Carbon nanotubes (CNTs) have outstanding electromechanical properties. Experiments have shown that a metallic CNT suspended over a trench can lose conductivity by orders of magnitude when deformed by an atomic force microscope (AFM) tip. The mechanism remains debated — it could stem from sp³ bond reconstruction at the nanoscale, or from strain‑induced band‑gap opening without any sp³ formation. This task investigates whether a chirality‑dependent electronic response exists: armchair and zigzag nanotubes of comparable size may respond very differently to the same mechanical deformation. The goal is to compute the conductance of an armchair (6,6) and a zigzag (12,0) carbon nanotube under two types of deformation — bending and tip indentation — and to determine whether and how strongly each chirality loses conductance.

## Approach
The approach follows a two‑stage simulation workflow.

**Structural relaxation:** Build (6,6) armchair and (12,0) zigzag nanotubes (2400 atoms each). Apply two deformation modes:
- Bending: rotate the two halves of the tube in opposite directions around a central axis until a total bend angle of 40° is reached.
- Tip deformation: use a 15‑atom Li needle tip pushed into the tube from below, reaching a deformation angle of 25°.
For every configuration (undeformed, bent, tip‑deformed) relax the atomic coordinates with a classical force field — the Universal Force Field (UFF) — keeping the end contact regions fixed. This mimics semi‑infinite leads and captures the strain state.

**Electronic transport:** From the relaxed geometries, construct a nearest‑neighbour sp³ tight‑binding Hamiltonian in a non‑orthogonal basis. The Hamiltonian and overlap matrix elements are bond‑length‑dependent, following the published parametrization of Papaconstantopoulos (the agent is expected to implement the parametrization scheme using the reference DOI provided). Treat the two ends as semi‑infinite perfect nanotube leads by computing the retarded self‑energies. Solve for the retarded Green’s function of the central device region, obtain the transmission T(E) via the Landauer‑Büttiker formalism, and compute the conductance at 300 K from T(E) convolved with the derivative of the Fermi–Dirac distribution. This yields the conductance in units of the conductance quantum 2e²/h.

The key comparison is between the armchair (6,6) and the zigzag (12,0) tubes under the same deformation states, revealing any chirality‑dependent conductance suppression.

## Reproduction target
Produce six conductance values (in units of 2e²/h) for the two chiralities under three conditions:
- armchair (6,6): undeformed, 40° bending, 25° tip deformation
- zigzag (12,0): undeformed, 40° bending, 25° tip deformation

Store these six numbers in the JSON file `/app/outputs/conductance_ratios.json` with the keys `armchair_undeformed`, `armchair_bending_40`, `armchair_tip_25`, `zigzag_undeformed`, `zigzag_bending_40`, `zigzag_tip_25`. The output must adhere to the schema described in the output contract.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/
- Papaconstantopoulos tight-binding parametrization: 10.1557/PROC-491-221

## Workflow steps

### Step 1: System construction and classical UFF relaxation
- Role: process
- Action: Build (6,6) and (12,0) carbon nanotubes with 2400 atoms each. Generate three configurations per chirality: undeformed, bent by 40°, and tip-deformed by 25° (using a 15-atom Li needle model). Relax all structures using the Universal Force Field (UFF) in LAMMPS, fixing the end contact regions to mimic semi-infinite leads. Produce relaxed atomic coordinate files for each configuration.
- Evidence: none

### Step 2: Conductance computation via tight-binding transport
- Role: scored (load-bearing)
- Action: Using the relaxed coordinates from step 1, construct strain-dependent nearest-neighbour sp³ tight-binding Hamiltonians and overlap matrices following the Papaconstantopoulos parametrization. For each configuration, treat the ends as semi-infinite perfect nanotube leads, compute the retarded Green's function of the device region recursively, obtain the transmission T(E), and calculate conductance at 300 K via the Landauer-Büttiker formula. Report the six conductance values (in units of 2e²/h) for: (6,6) undeformed, bent 40°, tip 25°; (12,0) undeformed, bent 40°, tip 25°.
- Output file: `/app/outputs/conductance_ratios.json`
- Format: json
- Contract: {"armchair_undeformed": float, "armchair_bending_40": float, "armchair_tip_25": float, "zigzag_undeformed": float, "zigzag_bending_40": float, "zigzag_tip_25": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/conductance_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### conductance_ratios.json
- path: `/app/outputs/conductance_ratios.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Six conductance values (in units of 2e²/h) that enable the checker to verify the chirality‑dependent conductance drop.
- schema:
  - `type`: object
  - `required`: `armchair_undeformed`, `armchair_bending_40`, `armchair_tip_25`, `zigzag_undeformed`, `zigzag_bending_40`, `zigzag_tip_25`
  - `properties`:
    - `armchair_undeformed`:
      - `type`: number
      - `description`: Conductance of undeformed (6,6) armchair tube (2e²/h)
    - `armchair_bending_40`:
      - `type`: number
      - `description`: Conductance of (6,6) armchair tube under 40° bending
    - `armchair_tip_25`:
      - `type`: number
      - `description`: Conductance of (6,6) armchair tube under 25° tip deformation
    - `zigzag_undeformed`:
      - `type`: number
      - `description`: Conductance of undeformed (12,0) zigzag tube (2e²/h)
    - `zigzag_bending_40`:
      - `type`: number
      - `description`: Conductance of (12,0) zigzag tube under 40° bending
    - `zigzag_tip_25`:
      - `type`: number
      - `description`: Conductance of (12,0) zigzag tube under 25° tip deformation

Notes: The hidden checker recomputes reduction factors (undeformed / deformed) for each case and applies threshold_or_better criteria consistent with the paper's reported trend. The output only provides raw conductance values; tolerances are defined hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "conductance_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "armchair_undeformed",
          "armchair_bending_40",
          "armchair_tip_25",
          "zigzag_undeformed",
          "zigzag_bending_40",
          "zigzag_tip_25"
        ],
        "properties": {
          "armchair_undeformed": {
            "type": "number",
            "description": "Conductance of undeformed (6,6) armchair tube (2e²/h)"
          },
          "armchair_bending_40": {
            "type": "number",
            "description": "Conductance of (6,6) armchair tube under 40° bending"
          },
          "armchair_tip_25": {
            "type": "number",
            "description": "Conductance of (6,6) armchair tube under 25° tip deformation"
          },
          "zigzag_undeformed": {
            "type": "number",
            "description": "Conductance of undeformed (12,0) zigzag tube (2e²/h)"
          },
          "zigzag_bending_40": {
            "type": "number",
            "description": "Conductance of (12,0) zigzag tube under 40° bending"
          },
          "zigzag_tip_25": {
            "type": "number",
            "description": "Conductance of (12,0) zigzag tube under 25° tip deformation"
          }
        }
      },
      "description": "Six conductance values (in units of 2e²/h) that enable the checker to verify the chirality‑dependent conductance drop."
    }
  ],
  "notes": "The hidden checker recomputes reduction factors (undeformed / deformed) for each case and applies threshold_or_better criteria consistent with the paper's reported trend. The output only provides raw conductance values; tolerances are defined hidden."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/conductance_ratios.json`, recomputes reduction factors (undeformed conductance divided by deformed conductance) for each chirality and deformation type, and checks whether the reduction factors fall within hidden tolerance windows that reflect the true physical response of the nanotube under deformation. The checker uses hidden thresholds; meeting or exceeding the required behaviour earns full credit, and progressive partial credit is given as the values deviate from the expected response. The agent is not required to match specific paper‑reported numbers — only to produce conductance values that are physically consistent with the applied strain and the electronic structure of each chirality.
