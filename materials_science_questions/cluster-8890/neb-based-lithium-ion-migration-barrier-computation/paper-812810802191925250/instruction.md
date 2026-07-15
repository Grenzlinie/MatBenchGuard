# NEB-based Lithium Ion Migration Barrier Computation

## Problem background
Ti3C2Tx MXenes are candidate anode materials for lithium-ion batteries. Surface terminations (O, F, OH) introduced during synthesis can alter the lithium adsorption strength and diffusion kinetics, which are critical for battery capacity and rate capability. Understanding how these terminations affect Li‑ion adsorption and diffusion energies is essential to optimizing the material.

## Approach
Use plane‑wave density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional, projector‑augmented wave (PAW) pseudopotentials, and a DFT‑D2 van der Waals correction. Construct monolayer supercells of Ti3C2 terminated with O, F, OH (and mixed substitutions) at the hollow sites among three neighbouring carbon atoms above/below the Ti3C2 layer. Perform variable‑cell geometry relaxations for the bare supercells and for lithium‑decorated configurations. Compute the first‑layer Li adsorption energy per Li atom from total energy differences. Then, using climbing‑image nudged elastic band (CI‑NEB) calculations, determine the energy barrier for Li diffusion along the preferred C→Ti→C pathway. The target is to obtain adsorption energies for three fully terminated configurations and diffusion barriers for O‑dominated surfaces with small F/OH substitutions.

## Reproduction target
Compute and report in eV (a) the first‑layer Li adsorption energy per Li atom on Ti3C2O2, Ti3C2F2, and Ti3C2(OH)2 (using 2×2 supercells), and (b) the CI‑NEB diffusion barriers for Li migration along the C→Ti→C path on Ti3C2O2, Ti3C2O1.75F0.25, and Ti3C2O1.75(OH)0.25 (using 3×3 supercells).

## Assets

- Quantum ESPRESSO (QE) – plane-wave DFT code: https://www.quantum-espresso.org/
- SSSP library – PBE pseudopotentials (efficiency version): https://www.materialscloud.org/discover/sssp/table/pbe
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Relax 2×2 supercells for adsorption calculations
- Role: process
- Action: Build 2×2 supercells of Ti3C2O2, Ti3C2F2, and Ti3C2(OH)2 by placing termination atoms at hollow sites among neighboring C atoms above/below the Ti3C2 monolayer. Perform variable-cell relaxation using DFT (PBE, DFT-D2 van der Waals correction).
- Evidence: `/app/outputs/relaxed_adsorption_structures.json`

### Step 2: Compute first-layer Li adsorption energies
- Role: scored (load-bearing)
- Action: For each relaxed 2×2 supercell, place a single Li atom at the preferred adsorption site (hollow site atop the termination atoms), relax the Li-decorated structure, and compute the adsorption energy per Li atom as E_ad = (E(Li-MX) - E(MX) - E(Li))/n with n=1. Write the three values into /app/outputs/adsorption_energies.json.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: JSON object with keys "Ti3C2O2", "Ti3C2F2", "Ti3C2(OH)2"; values are floats (eV).
- Scoring: scored by hidden verifier

### Step 3: Relax 3×3 supercells for diffusion barrier calculations
- Role: process
- Action: Build 3×3 supercells corresponding to Ti3C2O2 (Ti27C18O18), Ti3C2O1.75F0.25 (Ti27C18O17F), and Ti3C2O1.75(OH)0.25 (Ti27C18O17(OH)) by substituting one termination atom with F or OH. Perform variable-cell relaxation with the same DFT settings as used for adsorption supercells.
- Evidence: `/app/outputs/relaxed_diffusion_structures.json`

### Step 4: Compute CI-NEB Li diffusion barriers
- Role: scored (load-bearing)
- Action: For each relaxed 3×3 supercell, set the Li initial and final positions along the C→Ti→C path, run a climbing-image NEB calculation with at least 5 images, and extract the energy barrier. Write the three barriers into /app/outputs/diffusion_barriers.json.
- Output file: `/app/outputs/diffusion_barriers.json`
- Format: json
- Contract: JSON object with keys "Ti3C2O2_barrier", "Ti3C2O1.75F0.25_barrier", "Ti3C2O1.75(OH)0.25_barrier"; values are floats (eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`
- `/app/outputs/diffusion_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: First‑layer Li adsorption energy per Li atom (eV) on three differently terminated Ti3C2 monolayers.
- schema:
  - `type`: object
  - `required`:
    - `Ti3C2O2`: number (eV)
    - `Ti3C2F2`: number (eV)
    - `Ti3C2(OH)2`: number (eV)

### diffusion_barriers.json
- path: `/app/outputs/diffusion_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: CI‑NEB energy barriers (eV) for Li diffusion along the C→Ti→C path on O‑dominated Ti3C2Tx surfaces with and without small F/OH substitutions.
- schema:
  - `type`: object
  - `required`:
    - `Ti3C2O2_barrier`: number (eV)
    - `Ti3C2O1.75F0.25_barrier`: number (eV)
    - `Ti3C2O1.75(OH)0.25_barrier`: number (eV)

Notes: This is a compute‑driven reproduction task. The solving agent must run DFT relaxations and CI‑NEB calculations using Quantum ESPRESSO and the specified pseudopotentials. No experimental data is required; the results are compared to the paper‑reported values within a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Ti3C2O2": "number (eV)",
          "Ti3C2F2": "number (eV)",
          "Ti3C2(OH)2": "number (eV)"
        }
      },
      "description": "First‑layer Li adsorption energy per Li atom (eV) on three differently terminated Ti3C2 monolayers."
    },
    {
      "file": "diffusion_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Ti3C2O2_barrier": "number (eV)",
          "Ti3C2O1.75F0.25_barrier": "number (eV)",
          "Ti3C2O1.75(OH)0.25_barrier": "number (eV)"
        }
      },
      "description": "CI‑NEB energy barriers (eV) for Li diffusion along the C→Ti→C path on O‑dominated Ti3C2Tx surfaces with and without small F/OH substitutions."
    }
  ],
  "notes": "This is a compute‑driven reproduction task. The solving agent must run DFT relaxations and CI‑NEB calculations using Quantum ESPRESSO and the specified pseudopotentials. No experimental data is required; the results are compared to the paper‑reported values within a hidden tolerance."
}
```

## How you are scored
A hidden verifier reads your submitted adsorption_energies.json and diffusion_barriers.json files and compares each value against a reference derived from the original computational study. Your reward is based on how closely your computed adsorption energies and diffusion barriers match the expected values. The verifier weighs each entry and assigns a cumulative score; simply reporting numbers without running the actual DFT workflow will not receive credit. The exact scoring function and tolerances are not disclosed.
