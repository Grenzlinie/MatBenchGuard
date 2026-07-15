# Helmholtz Fermi-surface harmonics for anisotropic Eliashberg superconducting gap and critical temperature

## Problem background
Superconductivity mediated by the electron‑phonon interaction can be described by the anisotropic Eliashberg equations, but directly solving them in momentum space requires an exceedingly fine sampling of the Fermi surface and becomes computationally prohibitive. The central idea of this work is to reformulate the Eliashberg equations in a basis of Helmholtz Fermi‑surface harmonics (HFSH) — an orthonormal set of functions obtained by solving the Helmholtz equation on each Fermi surface sheet. This transformation replaces continuous k‑space integrals with discrete sums over a small number of HFSH coefficients, dramatically reducing the dimensionality while preserving full anisotropy. The method is benchmarked on the gap anisotropy of MgB₂, a prototypical multi‑band superconductor, and applied to the high‑pressure hydride YH₆ to predict its critical temperature. This reproduction task requires re‑implementing the HFSH‑based workflow and computing the corresponding superconducting properties from first principles.

## Approach
The approach consists of three stages: (i) first‑principles electronic structure and electron‑phonon coupling calculations, (ii) generation of the HFSH basis and projection of the coupling, and (iii) solution of the Eliashberg equations in the HFSH representation.

First, density functional theory (DFT) and density functional perturbation theory (DFPT) calculations are performed using Quantum ESPRESSO, combined with the EPW code for Wannier interpolation, to obtain the Fermi surface mesh, the anisotropic electron‑phonon coupling matrix λ_{k,k'}(iω), the density of states at the Fermi level N_F, and the Fermi velocities v_k. Separate calculations are carried out for hexagonal MgB₂ (P6/mmm) at ambient pressure and for body‑centered cubic YH₆ (Im‑3m) at 300 GPa.

Second, for each material the Fermi surface is triangulated into a mesh of vertices, and the fully symmetric HFSH basis functions Φ_{L̃}(k) are constructed on each Fermi surface sheet by solving the Helmholtz equation and applying the crystal point‑group symmetry. The full anisotropic λ_{k,k'} is then projected onto these basis functions via Fermi surface integrals to obtain the compact coefficient matrix λ_{L̃,L̃'}(iω). Only the symmetric HFSH subset contributes to the s‑wave superconducting state, so the size of the problem is drastically reduced.

Third, for MgB₂ the nonlinear anisotropic Eliashberg equations are solved self‑consistently at T = 10 K in the HFSH subspace with a Matsubara frequency cutoff of 10 times the maximum phonon energy, using the Coulomb pseudopotential μ* = 0.16 and n_{L̃} = 16 symmetric HFSHs per sheet. The resulting mass renormalization Z_{L̃} and pairing field φ_{L̃} coefficients are used to reconstruct the superconducting gap Δ_k = φ_k / Z_k on the Fermi surface, from which the minimum and maximum gap on the σ sheets and on the π sheets are extracted. For YH₆, the linearized Eliashberg eigenvalue problem is set up in the HFSH representation with μ* = 0.11 and n_{L̃} = 48 symmetric HFSHs. The temperature is swept until the largest eigenvalue reaches unity; that temperature is identified as the critical temperature T_c. All codes and input structures are publicly available, and the entire workflow is re‑executable.

## Reproduction target
Two superconducting properties must be computed from scratch using the above workflow:

1. **MgB₂ gap boundaries at 10 K**: Solve the nonlinear HFSH Eliashberg equations with μ* = 0.16 and n_{L̃} = 16 symmetric HFSHs per sheet, then determine the minimum and maximum values of the superconducting gap on the σ Fermi surface sheets and on the π sheets separately. Report these four numbers (in meV) in the file `mgb2_gap.json`.

2. **YH₆ critical temperature at 300 GPa**: Solve the linearized HFSH Eliashberg eigenvalue problem with μ* = 0.11 and n_{L̃} = 48 symmetric HFSHs, sweeping temperature until the maximum eigenvalue equals 1. Report this temperature (in K) in the file `yh6_tc.json`.

All intermediate steps (DFT/DFPT, HFSH generation, λ projection) must be executed; the final JSON files contain the computed quantities, not manually inserted values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- EPW (Electron-Phonon Wannier) code: https://epw-code.org/
- Wannier90: https://www.wannier90.org/
- MgB2 crystal structure: https://materialsproject.org/materials/mp-1560
- YH6 crystal structure at 300 GPa: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.99.220502
- SSSP pseudopotential library (v1.3): https://www.materialscloud.org/discover/sssp/table/efficiency
- scipy / numpy: scipy numpy

## Workflow steps

### Step 1: MgB2 first-principles electron-phonon coupling
- Role: process
- Action: Perform DFT and DFPT calculations for MgB2 using Quantum ESPRESSO and EPW to obtain the Fermi surface mesh, the anisotropic λ_{k,k'}(iω) matrix, the density of states N_F, and the Fermi velocities v_k.
- Evidence: `/app/outputs/mgb2_epw_output.log`

### Step 2: MgB2 HFSH basis generation
- Role: process
- Action: Construct the fully symmetric Helmholtz Fermi-surface harmonics basis set Φ_{L̃}(k) on the Fermi surface mesh of MgB2, respecting the crystal symmetry.
- Evidence: `/app/outputs/mgb2_hfsh_info.txt`

### Step 3: MgB2 λ projection to HFSH coefficients
- Role: process
- Action: Project the anisotropic λ_{k,k'} onto the HFSH basis to obtain the reduced matrix λ_{L,L'}(iω) for MgB2, using the Fermi surface integrals.
- Evidence: `/app/outputs/mgb2_lambda_hfsh.npy`

### Step 4: MgB2 superconducting gap at 10 K
- Role: scored (load-bearing)
- Action: Solve the nonlinear anisotropic Eliashberg equations in the HFSH representation at T=10 K, using μ*=0.16 and n_{L̃}=16 fully symmetric HFSHs per Fermi surface sheet, to obtain Z_L and φ_L. Compute the superconducting gap Δ_k = φ_k/Z_k on the Fermi surface and determine the minimum and maximum values on the σ sheets and on the π sheets separately. Write the four values (in meV) to mgb2_gap.json.
- Output file: `/app/outputs/mgb2_gap.json`
- Format: json
- Contract: {"sigma_gap_min_meV": <float>, "sigma_gap_max_meV": <float>, "pi_gap_min_meV": <float>, "pi_gap_max_meV": <float>}
- Scoring: scored by hidden verifier

### Step 5: YH6 first-principles electron-phonon coupling
- Role: process
- Action: Perform DFT and DFPT calculations for YH6 in the bcc structure at 300 GPa using Quantum ESPRESSO and EPW to obtain the Fermi surface mesh and the anisotropic λ_{k,k'}(iω) matrix.
- Evidence: `/app/outputs/yh6_epw_output.log`

### Step 6: YH6 HFSH basis generation
- Role: process
- Action: Construct the fully symmetric HFSH basis set Φ_{L̃}(k) on the Fermi surface mesh of YH6, respecting the bcc symmetry.
- Evidence: `/app/outputs/yh6_hfsh_info.txt`

### Step 7: YH6 λ projection to HFSH coefficients
- Role: process
- Action: Project the anisotropic λ_{k,k'} onto the HFSH basis to obtain λ_{L,L'}(iω) for YH6, using the Fermi surface integrals.
- Evidence: `/app/outputs/yh6_lambda_hfsh.npy`

### Step 8: YH6 critical temperature from linearized Eliashberg equation
- Role: scored (load-bearing)
- Action: Solve the linearized anisotropic Eliashberg eigenvalue problem in the HFSH representation using n_{L̃}=48 fully symmetric HFSHs and μ*=0.11. Sweep temperature until the maximum eigenvalue equals 1; that temperature is T_c. Write the result (in K) to yh6_tc.json.
- Output file: `/app/outputs/yh6_tc.json`
- Format: json
- Contract: {"Tc_K": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mgb2_gap.json`
- `/app/outputs/yh6_tc.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mgb2_gap.json
- path: `/app/outputs/mgb2_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Minimum and maximum superconducting gap on the σ and π Fermi surface sheets of MgB2 at 10 K (meV).
- schema:
  - `type`: object
  - `required`:
    - `sigma_gap_min_meV`: number
    - `sigma_gap_max_meV`: number
    - `pi_gap_min_meV`: number
    - `pi_gap_max_meV`: number

### yh6_tc.json
- path: `/app/outputs/yh6_tc.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical temperature of YH6 at 300 GPa (K).
- schema:
  - `type`: object
  - `required`:
    - `Tc_K`: number

Notes: Checker compares each reported value to the paper's reference values within a hidden tolerance; values are exact_match because they are physical quantities with no directional 'better' (closeness indicates correct reproduction).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mgb2_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "sigma_gap_min_meV": "number",
          "sigma_gap_max_meV": "number",
          "pi_gap_min_meV": "number",
          "pi_gap_max_meV": "number"
        }
      },
      "description": "Minimum and maximum superconducting gap on the σ and π Fermi surface sheets of MgB2 at 10 K (meV)."
    },
    {
      "file": "yh6_tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc_K": "number"
        }
      },
      "description": "Critical temperature of YH6 at 300 GPa (K)."
    }
  ],
  "notes": "Checker compares each reported value to the paper's reference values within a hidden tolerance; values are exact_match because they are physical quantities with no directional 'better' (closeness indicates correct reproduction)."
}
```

## How you are scored
A hidden verifier reads the two JSON files you write to `/app/outputs`. For each file, the verifier extracts your reported numbers and compares them to expected reference values using predetermined tolerances. The comparisons are performed independently, and a weighted average yields the final reward in the range [0, 1]. A higher score indicates better agreement with the reference; merely reporting numbers that match published literature without correctly executing the workflow is insufficient, as the verifier checks the integrity of the pipeline through your submitted artifacts.
