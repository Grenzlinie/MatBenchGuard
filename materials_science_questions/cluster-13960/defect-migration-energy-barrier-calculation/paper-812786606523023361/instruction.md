# Harmonic TST prefactor for Li interstitial diffusion in Si via local effective Hessian

## Problem background
Predicting the rate of atomic diffusion in crystalline solids is central to understanding kinetic processes such as defect migration and phase transformations. In harmonic transition state theory (TST) the jump frequency is expressed as a product of a migration energy barrier and an effective frequency prefactor ν*. While the energy barrier can be obtained from static calculations, the prefactor depends on the full vibrational spectrum of the system—the ratio of the product of normal-mode frequencies at the initial basin to that at the saddle point. Computing this ratio conventionally requires diagonalizing the full Hessian of the entire simulation cell, a task that scales cubically with the number of atoms and quickly becomes intractable for large systems. The local effective Hessian method overcomes this limitation by limiting the force‑constant calculation to a small ’active region’ around the migrating atom while incorporating the mechanical response of the surrounding ’environment’ through a relaxation correction, thereby dramatically reducing computational cost while retaining accuracy. This task applies the relaxed‑environment variant of that method to compute the harmonic TST prefactor for lithium interstitial diffusion in diamond cubic silicon—a representative validation system—and evaluates the convergence of the prefactor with the size of the active region.

## Approach
The core idea is to partition the system into an active region (atoms near the diffusion path) and an environment (the rest). By exploiting block‑matrix identities, the standard TST prefactor can be rewritten in terms of *local effective Hessians*—Hessians of the active region that are corrected for the static relaxation of the environment. Concretely, after locating the saddle point (the transition state) between two stable interstitial sites, one computes the mass‑weighted Hessian for the active region in both the basin and the activated configurations, but allowing the environment atoms to relax to zero force during the force‑constant calculation. The correction term has the form −X^T E^{−1} X where E is the environment Hessian block and X couples active and environment regions. The prefactor ν* is then obtained from the imaginary‑mode frequency at the saddle, (ν₁ᴬ)², and the ratio of determinants of the two effective Hessians. In this task, a Nudged Elastic Band (NEB) simulation is first run with LAMMPS and a ReaxFF potential for Li in Si to identify the basin and saddle configurations. The saddle configuration is then used to center a spherical active region; for each radius (4, 6, 8 Å) the local effective Hessian calculation is performed using the `local_hessian` LAMMPS module, which implements the relaxed‑environment approach. The output is the converged ν* value for each radius.

## Reproduction target
Compute the harmonic TST prefactor ν* (in THz) for lithium interstitial diffusion in diamond cubic silicon using the relaxed‑environment local effective Hessian method at active region radii of 4 Å, 6 Å, and 8 Å. The three values must be written as a JSON array `[ν_4, ν_6, ν_8]` to `/app/outputs/prefactor.json`.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- LAMMPS-local_hessian module: https://go.uic.edu/lammps_local_hessian
- ReaxFF parameter file for Li-Si system: 10.1088/0965-0393/21/7/074002

## Workflow steps

### Step 1: NEB simulation for Li interstitial diffusion
- Role: process
- Action: Set up a 6x6x6 supercell of diamond cubic Si (lattice constant 5.46 Å) with a Li atom at a tetrahedral interstitial site as the initial state and an adjacent tetrahedral site as the final state. Run a nudged elastic band (NEB) simulation in LAMMPS using the provided ReaxFF potential to locate the minimum energy path, obtain the basin and saddle configurations, and verify the energy barrier (expected ~0.63 eV). Extract the saddle configuration (highest energy replica).
- Evidence: `/app/outputs/saddle_configuration.data`

### Step 2: Local effective Hessian prefactor calculation
- Role: scored (load-bearing)
- Action: For each active region radius r in {4, 6, 8} Å, centered at the migrating Li atom's position in the saddle configuration, compute the harmonic TST prefactor v* using the LAMMPS-local_hessian module with the relaxed-environment approach. This involves computing the effective Hessians via environment relaxation and evaluating v* = sqrt( (v1_A)^2 * det(B_eff)/det(A_eff) ). Produce the three values (in THz) in the same order [v_4, v_6, v_8] and write them as a JSON array to /app/outputs/prefactor.json.
- Output file: `/app/outputs/prefactor.json`
- Format: json
- Contract: A JSON array of three floating-point numbers, e.g. [5.2, 8.7, 9.8]. Order: radius 4 Å, 6 Å, 8 Å.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/prefactor.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### prefactor.json
- path: `/app/outputs/prefactor.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Harmonic TST prefactor v* for Li interstitial diffusion in Si at active region radii 4, 6, 8 Å, as a JSON array.
- schema:
  - `type`: array
  - `items`:
    - `type`: number
    - `description`: prefactor in THz

Notes: The scored output is a JSON array of three floats. The hidden reference values are the paper-reported prefactors for these radii, and the checker will apply relative and absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "prefactor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "number",
          "description": "prefactor in THz"
        }
      },
      "description": "Harmonic TST prefactor v* for Li interstitial diffusion in Si at active region radii 4, 6, 8 Å, as a JSON array."
    }
  ],
  "notes": "The scored output is a JSON array of three floats. The hidden reference values are the paper-reported prefactors for these radii, and the checker will apply relative and absolute tolerances."
}
```

## How you are scored
A hidden verifier reads the file `/app/outputs/prefactor.json` and checks that it is a valid JSON array of three numbers. Each of the three prefactor values is compared to a hidden reference value (not provided to you) using generous tolerances that account for the variability inherent in different numerical implementations, force‑field versions, and convergence choices. The reward is a weighted average of the per‑radius accuracies (the result for the 4 Å active region carries the highest weight). A correct calculation earns full credit; results that deviate significantly receive a proportionally lower score. The preliminary NEB simulation and all necessary numerical settings are part of your workflow but are not directly scored—only the final prefactor array in `prefactor.json` contributes to the reward.
