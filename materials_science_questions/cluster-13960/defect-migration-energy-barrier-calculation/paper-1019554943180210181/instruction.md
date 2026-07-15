# CI-NEB Migration Barrier of C_i-V_C Frenkel Pair in 4H-SiC with and without Al Substitution

## Problem background
Aluminum ion implantation is the primary method for p-type doping in 4H-SiC, which is essential for high-voltage power devices. However, the implantation process introduces point defects (such as carbon vacancies, carbon interstitials, and antisites) that can couple with the implanted Al atoms, degrading electrical activation and channel transport. Understanding the energetic interactions between Al dopants and native defects is critical for improving device performance. This work investigates the migration energetics of a carbon interstitial–carbon vacancy (C_i–V_C) Frenkel pair in 4H-SiC, which is a key defect complex. The target quantity to reproduce is the minimum energy path (MEP) for the formation of this pair, both in a pristine supercell and in one where Al occupies a Si site (Al_Si). Computing the MEP for both cases reveals how the presence of Al alters the energy landscape, providing insight into defect–dopant coupling.

## Approach
Density functional theory (DFT) calculations are used within the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation. The software is Quantum ESPRESSO (pw.x for relaxations, neb.x for nudged elastic band). Pseudopotentials are taken from the SSSP library: ultrasoft for Si, PAW for C and Al. A 240-atom 4H-SiC supercell (3×5×1 repeat of a 16-atom rectangular unit cell) is constructed for all calculations. Two supercell configurations are prepared: a pristine cell and one where a single Si site is replaced by Al. Both are fully relaxed. Next, for each supercell, end points for the CI-NEB are created: the initial state is the perfect lattice; the final state contains a C_i–V_C Frenkel pair formed by moving one carbon atom from a lattice site to a tetrahedral interstitial site along the <0001> direction. A climbing-image nudged elastic band (CI-NEB) calculation with 7 images (including endpoints) is run for each case to find the minimum energy path. The total energy of each image relative to the initial state is recorded in electronvolts. The comparison between the pure and Al-doped MEPs quantifies the effect of Al on the barrier.

## Reproduction target
Compute the minimum energy path (MEP) for the formation of a C_i–V_C Frenkel pair in a 240-atom 4H-SiC supercell using CI-NEB with 7 images. Perform this calculation twice: once for the pure 4H-SiC supercell, and once for a supercell in which one Si site is substituted by Al. For each case, write the total energy (in eV) of each image relative to the initial state into a JSON array of exactly seven numbers. The two output files are: `mep_no_al.json` (pure supercell) and `mep_with_al.json` (Al-doped supercell). The hidden verifier will compare the two paths to evaluate the barrier difference.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Si ultrasoft pseudopotential: https://pseudopotentials.quantum-espresso.org/upf_files/Si.pbe-nd-rrkjus_psl.1.0.0.UPF
- C PAW pseudopotential: https://pseudopotentials.quantum-espresso.org/upf_files/C.pbe-n-kjpaw_psl.1.0.0.UPF
- Al PAW pseudopotential: https://pseudopotentials.quantum-espresso.org/upf_files/Al.pbe-n-kjpaw_psl.1.0.0.UPF
- 4H-SiC lattice constants

## Workflow steps

### Step 1: Supercell construction and geometry relaxation
- Role: process
- Action: Construct a 240-atom 4H-SiC supercell (3×5×1 repeat of the 16-atom rectangular unit cell) and create two configurations: (a) pristine supercell, (b) supercell with one Al atom substituting a Si site. Perform full geometry optimization for both using Quantum ESPRESSO (pw.x) with PBE functional, the specified pseudopotentials, and force convergence <1e-3 Ry/bohr. Save the final relaxed atomic coordinates for the next step.
- Evidence: `/app/outputs/relaxed_pure.xyz, relaxed_al.xyz`

### Step 2: Define initial and final states for CI-NEB
- Role: process
- Action: For each relaxed supercell (pure and Al_Si), create the initial state (perfect lattice) and the final state containing a C_i-V_C Frenkel pair by moving one carbon atom from a lattice site to a tetrahedral interstitial site along the <0001> direction. Save the atomic coordinate files for the initial and final configurations.
- Evidence: `/app/outputs/initial_pure.xyz, final_pure.xyz, initial_al.xyz, final_al.xyz`

### Step 3: CI-NEB for pure 4H-SiC
- Role: scored (load-bearing)
- Action: Run a climbing-image nudged elastic band (CI-NEB) calculation with 7 images (including initial and final) for the pure 4H-SiC supercell using Quantum ESPRESSO (neb.x). Use the same functional/pseudopotentials and total energy convergence 1e-6 Ry, force convergence 1e-4 Ry/bohr. Record the total energy of each image (in eV, relative to the initial state) and write to mep_no_al.json.
- Output file: `/app/outputs/mep_no_al.json`
- Format: json
- Contract: JSON array of exactly 7 numbers, each representing the total energy (in eV) of one image relative to the initial state.
- Scoring: scored by hidden verifier

### Step 4: CI-NEB for Al_Si-doped 4H-SiC
- Role: scored (load-bearing)
- Action: Run a CI-NEB calculation with the same settings (7 images, convergence criteria) for the supercell containing an Al_Si substitution. Record the total energy of each image (in eV, relative to the initial state) and write to mep_with_al.json.
- Output file: `/app/outputs/mep_with_al.json`
- Format: json
- Contract: JSON array of exactly 7 numbers, each representing the total energy (in eV) of one image relative to the initial state.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mep_no_al.json`
- `/app/outputs/mep_with_al.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mep_no_al.json
- path: `/app/outputs/mep_no_al.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Minimum energy path (MEP) energies for the C_i-V_C Frenkel pair formation in pure 4H-SiC, obtained from a CI-NEB calculation with 7 images.
- schema:
  - `type`: array
  - `items`:
    - `type`: number
    - `unit`: eV
  - `description`: Array of 7 relative total energies (in eV) for the CI-NEB images of C_i-V_C formation in pure 4H-SiC. The first and last energies correspond to the initial and final states.

### mep_with_al.json
- path: `/app/outputs/mep_with_al.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Minimum energy path (MEP) energies for the C_i-V_C Frenkel pair formation in the presence of an Al_Si substitution, from a CI-NEB calculation with 7 images.
- schema:
  - `type`: array
  - `items`:
    - `type`: number
    - `unit`: eV
  - `description`: Array of 7 relative total energies (in eV) for the CI-NEB images of C_i-V_C formation in the Al_Si-doped 4H-SiC supercell.

Notes: The checker recomputes the energy barrier (maximum minus minimum) from each MEP array and evaluates the reduction caused by Al doping using a threshold_or_better policy. The agent must provide exactly 7 energies per file in correct order.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mep_no_al.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "number",
          "unit": "eV"
        },
        "description": "Array of 7 relative total energies (in eV) for the CI-NEB images of C_i-V_C formation in pure 4H-SiC. The first and last energies correspond to the initial and final states."
      },
      "description": "Minimum energy path (MEP) energies for the C_i-V_C Frenkel pair formation in pure 4H-SiC, obtained from a CI-NEB calculation with 7 images."
    },
    {
      "file": "mep_with_al.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "number",
          "unit": "eV"
        },
        "description": "Array of 7 relative total energies (in eV) for the CI-NEB images of C_i-V_C formation in the Al_Si-doped 4H-SiC supercell."
      },
      "description": "Minimum energy path (MEP) energies for the C_i-V_C Frenkel pair formation in the presence of an Al_Si substitution, from a CI-NEB calculation with 7 images."
    }
  ],
  "notes": "The checker recomputes the energy barrier (maximum minus minimum) from each MEP array and evaluates the reduction caused by Al doping using a threshold_or_better policy. The agent must provide exactly 7 energies per file in correct order."
}
```

## How you are scored
A hidden automated verifier inspects the two output files. It checks that each file contains exactly seven numeric energies (relative to the initial state) in a JSON array. For each path, the verifier recomputes the energy barrier (difference between the maximum and minimum energy values along the path). The primary scoring criterion is the difference in barrier height between the pure and Al-doped cases. The verifier uses a hidden threshold derived from the paper’s reported results and awards credit based on a threshold-or-better monotonic policy: a larger barrier reduction (more lowering) earns full credit, and diminishing credit is given as the reduction falls below the threshold. Additional minor checks may audit the smoothness of the path (single maximum) and the exact number of images, but the main weight is on the barrier reduction computed from the arrays.
