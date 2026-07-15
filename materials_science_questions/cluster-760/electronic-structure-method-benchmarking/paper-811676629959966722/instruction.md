# Compute Si–H dissociation and H₂ desorption energies for Si₉Hₓ cluster models using nonlocal DFT

## Problem background
The reconstructed Si(100)2x1 surface consists of rows of surface dimers, where each surface Si atom possesses a dangling bond, making the surface highly reactive. Understanding the strengths of surface Si–H bonds and the energetics of H₂ desorption is important for explaining reaction mechanisms on this technologically relevant surface. Finite cluster models can capture the local bonding environment of the dimer. This task aims to compute the reaction energies for Si–H bond dissociation and H₂ desorption from such cluster models using density functional theory with nonlocal corrections, providing a quantitative test of the computational approach.

## Approach
The Si(100) surface dimer is modeled by three hydrogen-terminated clusters: Si₉H₁₂ (clean surface), Si₉H₁₃ (one surface H), and Si₉H₁₄ (two surface H atoms). The approach is entirely computational and consists of the following conceptual stages. First, the three clusters are built with bulk-like Si–Si distances and tetrahedral angles, while applying constraints that mimic the embedding in a larger surface: deeper Si atoms (layers 3 and 4) and all terminating H atoms are kept fixed; second-layer Si atoms are allowed to move only in the x and z directions; surface Si atoms and any surface H atoms are fully relaxed. Next, geometry optimizations are carried out at the local density approximation (LDA) level using Dirac exchange and VWN correlation with a double-zeta plus polarization (DZVP) basis set, respecting the defined constraints. On the LDA-optimized structures, single-point nonlocal DFT calculations are then performed with the VWN+BP functional (VWN local reference plus Becke exchange and Perdew correlation added perturbatively) using a larger triple-zeta plus polarization (TZVPP) basis set; total energies are obtained for Si₉H₁₂, Si₉H₁₃, Si₉H₁₄, the H atom, and the H₂ molecule. Finally, three reaction energies (in kcal/mol) are obtained by energy differences: (1) Si₉H₁₄ → Si₉H₁₃ + H, (2) Si₉H₁₃ → Si₉H₁₂ + H, and (3) Si₉H₁₄ → Si₉H₁₂ + H₂.

## Reproduction target
Reconstruct the three cluster models (Si₉H₁₂, Si₉H₁₃, Si₉H₁₄) according to the constraint scheme described in the workflow steps. Optimize their geometries at the LDA/DZVP level, then compute VWN+BP/TZVPP single-point energies for the optimized clusters, the H atom, and the H₂ molecule. From these total energies, calculate the three VWN+BP/TZVPP reaction energies (kcal/mol) and report them in the file `reaction_energies.json` as an object with the keys `Si9H14_to_Si9H13_H`, `Si9H13_to_Si9H12_H`, and `Si9H14_to_Si9H12_H2`. The numerical values will be compared against independent reference results.

## Assets

- Open‑source DFT code (e.g., NWChem, CP2K, ORCA): https://github.com/nwchemgit/nwchem
- DZVP basis set for Si and H: https://www.basissetexchange.org
- TZVPP basis set for Si and H: https://www.basissetexchange.org

## Workflow steps

### Step 1: Build Si₉H₁₂, Si₉H₁₃, Si₉H₁₄ cluster models
- Role: process
- Action: Construct Si9H12, Si9H13, and Si9H14 cluster models of the Si(100) surface dimer. Fix all Si atoms in layers 3 and 4 and all terminating H atoms; allow second‑layer Si atoms to move only in x and z directions; fully relax surface Si atoms and surface H atoms. Use bulk‑like Si‑Si distances and tetrahedral angles for the starting structure as described in the paper's reference 1c.
- Evidence: `/app/outputs/cluster_models.xyz`

### Step 2: LDA geometry optimization
- Role: process
- Action: Optimize the geometries of the three clusters at the local density approximation (LDA) level using Dirac exchange and VWN correlation with the DZVP basis set, respecting the constraints defined in step_01.
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 3: VWN+BP/TZVPP single‑point nonlocal DFT energies
- Role: process
- Action: Perform single‑point nonlocal DFT calculations on the LDA‑optimized geometries of Si9H12, Si9H13, Si9H14, the H atom, and the H2 molecule using the VWN+BP functional (VWN local reference plus Becke exchange and Perdew correlation added perturbatively) with the TZVPP basis set. Record the total electronic energies.
- Evidence: `/app/outputs/total_energies.json`

### Step 4: Compute reaction energies
- Role: scored (load-bearing)
- Action: Calculate the three reaction energies from the total energies obtained in step_03 and report them in kcal/mol: (1) Si9H14 → Si9H13 + H, (2) Si9H13 → Si9H12 + H, (3) Si9H14 → Si9H12 + H2.
- Output file: `/app/outputs/reaction_energies.json`
- Format: json
- Contract: { "Si9H14_to_Si9H13_H": <float>, "Si9H13_to_Si9H12_H": <float>, "Si9H14_to_Si9H12_H2": <float> }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reaction_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_energies.json
- path: `/app/outputs/reaction_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: VWN+BP/TZVPP nonlocal DFT reaction energies for Si–H dissociation and H₂ desorption from Si₉Hₓ cluster models of the Si(100) surface.
- schema:
  - `type`: object
  - `required`:
    - `Si9H14_to_Si9H13_H`: number (kcal/mol)
    - `Si9H13_to_Si9H12_H`: number (kcal/mol)
    - `Si9H14_to_Si9H12_H2`: number (kcal/mol)
  - `units`:
    - `Si9H14_to_Si9H13_H`: kcal/mol
    - `Si9H13_to_Si9H12_H`: kcal/mol
    - `Si9H14_to_Si9H12_H2`: kcal/mol

Notes: The hidden gold is the paper‑reported VWN+BP/TZVPP values; scoring uses a tolerance to absorb legitimate toolchain spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Si9H14_to_Si9H13_H": "number (kcal/mol)",
          "Si9H13_to_Si9H12_H": "number (kcal/mol)",
          "Si9H14_to_Si9H12_H2": "number (kcal/mol)"
        },
        "units": {
          "Si9H14_to_Si9H13_H": "kcal/mol",
          "Si9H13_to_Si9H12_H": "kcal/mol",
          "Si9H14_to_Si9H12_H2": "kcal/mol"
        }
      },
      "description": "VWN+BP/TZVPP nonlocal DFT reaction energies for Si–H dissociation and H₂ desorption from Si₉Hₓ cluster models of the Si(100) surface."
    }
  ],
  "notes": "The hidden gold is the paper‑reported VWN+BP/TZVPP values; scoring uses a tolerance to absorb legitimate toolchain spread."
}
```

## How you are scored
A hidden verifier reads your `reaction_energies.json` file and compares each of the three reported reaction energies to a hidden reference value (the reference was computed independently using the same functional and basis set). A small tolerance is allowed to absorb legitimate numerical differences from different DFT implementations and geometry guesses. The reward is the fraction of the three energies that fall within tolerance; the full reward is awarded only when all three are within the allowed margin. The workflow steps that produce intermediate artifacts are required to reach the final scored output, but only the final reaction energies contribute directly to the reward.
