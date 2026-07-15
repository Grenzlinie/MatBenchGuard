# DFT Geometry Optimization and Bond Dissociation Energy Calculation of a Silicon Cluster Model

## Problem background
The deposition of aluminum on hydrogen-terminated Si(100) surfaces is critical for VLSI interconnect technology. Understanding the initial surface chemistry requires knowledge of the Si–H bond dissociation energy on the clean H-terminated surface. This task focuses on computing the bond dissociation energies for two distinct Si–H bond sites on a Si9H16 cluster model of the Si(100) 1×1:H surface using density functional theory.

## Approach
The surface is modeled by a Si9H16 cluster. Atomic positions are constrained to mimic the bulk-terminated surface: deeper silicon atoms are frozen in their bulk-like positions, while second-layer and surface atoms are partially relaxed. The lateral and internal Si–H bond cleavage sites are examined. The energy prediction follows a two‑stage protocol: (1) geometry optimization within the local spin density approximation (LSD) using the Dirac exchange and Vosko-Wilk-Nusair (VWN) correlation functional, and (2) a single‑point energy calculation on the optimized geometry adding nonlocal gradient corrections (Becke exchange and Perdew correlation, denoted NLSD). The dissociation energy for each site is computed as the difference between the total NLSD energies of the Si9H16 reactant and the products Si9H15 + H.

## Reproduction target
Compute the NLSD dissociation energies for the lateral (l) and internal (i) Si–H bond cleavage on the Si9H16 cluster, defined as ΔE = E(Si9H15) + E(H) – E(Si9H16) for each site. Report both values, in kcal/mol, in a JSON file.

## Assets

- Open-source DFT code supporting LSD (VWN) and NLSD (Becke-Perdew) with all-electron Gaussian basis sets (e.g., NWChem, CP2K, Quantum ESPRESSO, PySCF): https://nwchemgit.github.io/ (or https://www.cp2k.org/, https://www.quantum-espresso.org/, https://pyscf.org/)
- Double-zeta split-valence plus polarization (DZVP) Gaussian basis set for Si and H: Available in standard basis set libraries of most DFT codes (e.g., from Godbout et al., Can. J. Chem. 70, 560 (1992))

## Workflow steps

### Step 1: Construct Si9H16 and Si9H15 cluster models
- Role: process
- Action: Build the atomic coordinates for the Si9H16 cluster (reactant) and the Si9H15 cluster (product with one H removed) with the geometric constraints: Si atoms in layers 3 and 4 fully frozen in bulk-like positions; all terminating H atoms fixed; second-layer Si atoms allowed to move in x and z directions; surface Si atoms fixed at 3.84 Å; H atoms on the surface fully optimized (except for the removal site in Si9H15). Identify the lateral (l) and internal (i) Si-H bond sites.
- Evidence: `/app/outputs/cluster_geometries.xyz`

### Step 2: LSD geometry optimization
- Role: process
- Action: Perform geometry optimizations of Si9H16 and Si9H15 using the local spin density approximation (LSD) with the Dirac exchange functional and Vosko-Wilk-Nusair (VWN) correlation functional, and the DZVP basis set. Apply the same bond-length/coordinate constraints as in step 1. Obtain LSD total energies for both clusters.
- Evidence: `/app/outputs/lsd_optimization.log`

### Step 3: NLSD single-point energy calculations
- Role: process
- Action: On the LSD-optimized geometries, compute single-point energies with nonlocal gradient corrections (Becke exchange, Perdew correlation) to obtain NLSD total energies for Si9H16, Si9H15, and an isolated H atom (same functional/basis).
- Evidence: `/app/outputs/nlsd_energies.txt`

### Step 4: Compute and report Si-H dissociation energies
- Role: scored (load-bearing)
- Action: Using the NLSD total energies from step 3, compute the dissociation energies for the lateral (l) and internal (i) Si-H bonds: ΔE = E(Si9H15) + E(H) - E(Si9H16) for each site. Output both values, in kcal/mol, as a JSON file.
- Output file: `/app/outputs/si_h_dissociation_energies.json`
- Format: json
- Contract: {"lateral_nlsd": float (kcal/mol), "internal_nlsd": float (kcal/mol)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/si_h_dissociation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### si_h_dissociation_energies.json
- path: `/app/outputs/si_h_dissociation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: NLSD dissociation energies for lateral and internal Si-H bond cleavage on the Si9H16 cluster. Values are compared to fixed reference energies with a tolerance.
- schema:
  - `type`: object
  - `required`: `lateral_nlsd`, `internal_nlsd`
  - `properties`:
    - `lateral_nlsd`:
      - `type`: number
    - `internal_nlsd`:
      - `type`: number
  - `units`:
    - `lateral_nlsd`: kcal/mol
    - `internal_nlsd`: kcal/mol

Notes: Scoring uses exact_match against hidden reference values (the paper's reported NLSD energies). The tolerance absorbs implementation differences between DFT codes and basis sets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "si_h_dissociation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lateral_nlsd",
          "internal_nlsd"
        ],
        "properties": {
          "lateral_nlsd": {
            "type": "number"
          },
          "internal_nlsd": {
            "type": "number"
          }
        },
        "units": {
          "lateral_nlsd": "kcal/mol",
          "internal_nlsd": "kcal/mol"
        }
      },
      "description": "NLSD dissociation energies for lateral and internal Si-H bond cleavage on the Si9H16 cluster. Values are compared to fixed reference energies with a tolerance."
    }
  ],
  "notes": "Scoring uses exact_match against hidden reference values (the paper's reported NLSD energies). The tolerance absorbs implementation differences between DFT codes and basis sets."
}
```

## How you are scored
A hidden verifier reads your output JSON file and compares the two reported dissociation energies to hidden reference values. The verifier also checks the mean of the two energies. Your reward is based on how closely your computed values agree with the hidden reference, within tolerances that accommodate typical differences between DFT codes and basis sets. You do not need to match a specific number from any external report; focus on faithfully implementing the DFT protocol and geometric constraints described in the workflow steps.
