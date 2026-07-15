# DFT Reaction Mechanism Energetics for Silicon Systems

## Problem background
During gas-source molecular beam epitaxy of silicon using precursors like silane or disilane, a key surface reaction is the decomposition of adsorbed silyl (SiH₃) to silylene (SiH₂) and a hydrogen atom. Silylene can adopt different adsorption configurations on the Si(100)-(2×1) surface, primarily intrarow (where it bridges two neighbouring silicon dimers along a dimer row) and on-dimer (where it inserts into a single surface dimer). The relative stability of these configurations is known to change with the local coverage of coadsorbed hydrogen released by the decomposition reaction itself. Understanding the decomposition pathway—which configuration is formed, the activation barriers that govern the rate, and the partitioning of the released energy among the products—is important for controlling film growth at the atomic scale. This task reproduces the density functional theory (DFT) study of these energetics: compute the relative energies of intrarow and on-dimer silylene at three hydrogen coverages, the activation barriers for the two decomposition channels, and the frustrated translational kinetic energy imparted to the hydrogen atom.

## Approach
The method uses periodic slab DFT within the generalized gradient approximation (Perdew–Burke–Ernzerhof functional) and a plane-wave basis set with norm-conserving pseudopotentials. The Si(100)-(2×1) surface is represented by a slab of several atomic layers; the bottom layer is kept fixed at bulk positions, the bottom face is passivated with hydrogen, and a vacuum gap separates periodic images. Silylene adsorbates are placed in both intrarow and on-dimer geometries, each with 0, 1, or 2 coadsorbed hydrogen atoms in the vicinity, and the structures are fully relaxed to obtain total energies ΔE = E(on-dimer) − E(intrarow) for each coverage. To follow the silyl decomposition, a series of constrained relaxations is performed: the distance between the silyl silicon and the departing hydrogen is held fixed at a sequence of values that span the bond-breaking range, while all other atomic positions are relaxed. The energy maximum along each series defines the transition state, and the activation barrier is the difference between transition-state and reactant energies. Finally, the Cartesian forces on the dissociated hydrogen atom are recorded in the exit valley (transition state to product) and numerically integrated to give the classical work W = ∫ F·dr, which is interpreted as the frustrated translational energy of the hydrogen.

## Reproduction target
For the Si(100)-(2×1) surface modeled with GGA-PBE and norm-conserving pseudopotentials, compute and save the following three quantities as structured JSON files:

1. **Relative silylene stability** – ΔE = E(on-dimer) − E(intrarow) for hydrogen coverages of 0, 1, and 2 coadsorbed H atoms, using the supercell that best minimises lateral interactions for each case.
2. **Activation barriers** – barrier energies (transition-state minus reactant) for the decomposition pathways leading to intrarow silylene and to on-dimer silylene.
3. **Frustrated translational energy of hydrogen** – the work integral along the exit valley of the intrarow channel, obtained from the force data saved in the evidence file.

The raw force data from the constrained scan (forces_H_exit_valley.csv) must be provided as supporting evidence for the integration.

## Assets

- Quantum ESPRESSO plane-wave DFT code (or equivalent PBE/norm-conserving capable code): https://www.quantum-espresso.org/
- PBE norm-conserving pseudopotentials for Si and H from SSSP efficiency library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Optimize intrarow and on-dimer SiH2 configurations with varying H coverage
- Role: process
- Action: Build the Si(100)-(2×1) slab model (6 layers, bottom fixed, H-terminated, ~10 Å vacuum) using the known Si lattice parameter. Add SiH2 adsorbate in intrarow and on-dimer geometries for three hydrogen coverages (0, 1, and 2 coadsorbed H atoms). Perform full geometry optimization for each configuration using DFT (PBE functional, plane-wave cutoff 20 Ry, norm-conserving pseudopotentials) with appropriately chosen supercell sizes (2×2, 2×4, 4×2) to minimize lateral interactions. Record the optimized total energy for each structure in an evidence CSV file.
- Evidence: `/app/outputs/energies_silylene_geometries.csv`

### Step 2: Compute relative stability of intrarow vs on-dimer silylene
- Role: scored
- Action: From the total energies recorded in step01, compute the energy difference ΔE = E(on-dimer) − E(intrarow) for each hydrogen coverage (0H, 1H, 2H), using energies from the supercell that gives the most converged lateral interaction (e.g., 2×2 for 2H, 4×2 or 2×4 for 0H and 1H). Write the three ΔE values to a JSON file.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: {"delta_E_0H_eV": float, "delta_E_1H_eV": float, "delta_E_2H_eV": float}
- Scoring: scored by hidden verifier

### Step 3: Constrained DFT scans for intrarow and on-dimer decomposition
- Role: process
- Action: Starting from the adsorbed silyl (SiH₃) geometry, perform a series of constrained relaxations. Hold the distance dSi-H between the silyl silicon and the dissociating hydrogen fixed at a set of values covering the bond-breaking range (at least 21 points for intrarow, 26 for on-dimer). At each fixed distance, fully relax all other ionic degrees of freedom. Record the total energy as a function of distance, and save the Cartesian forces acting on the dissociating H atom along the exit valley (from transition state to product) in a dedicated CSV evidence file. Identify the transition state as the energy maximum along each path.
- Evidence: `/app/outputs/forces_H_exit_valley.csv`

### Step 4: Compute activation barriers for both decomposition pathways
- Role: scored (load-bearing)
- Action: From the energy curves obtained in step03, locate the transition state (maximum energy) and the reactant minimum for each decomposition pathway. Compute the activation barrier as the difference in total energy between transition state and reactant. Write the two barrier values to a JSON file.
- Output file: `/app/outputs/activation_barriers.json`
- Format: json
- Contract: {"intrarow_barrier_eV": float, "on_dimer_barrier_eV": float}
- Scoring: scored by hidden verifier

### Step 5: Compute frustrated translational energy of hydrogen via force integration
- Role: scored (load-bearing)
- Action: Using the forces on the dissociated hydrogen atom along the intrarow exit valley (from the step03 evidence file forces_H_exit_valley.csv), numerically integrate the force along the displacement from the transition state to the product well: W = ∫ F·dr. Interpret the integrated work as the frustrated translational kinetic energy of the H atom. Write the work integral and the estimated excess energy above thermal (which are identical under the paper's approximation) to a JSON file.
- Output file: `/app/outputs/frustrated_energy_hydrogen.json`
- Format: json
- Contract: {"H_work_integral_eV": float, "estimated_frustrated_translational_energy_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.json`
- `/app/outputs/activation_barriers.json`
- `/app/outputs/frustrated_energy_hydrogen.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.json
- path: `/app/outputs/relative_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy difference ΔE = E(on-dimer) - E(intrarow) for 0, 1, and 2 coadsorbed H atoms.
- schema:
  - `type`: object
  - `required`:
    - `delta_E_0H_eV`: float (eV)
    - `delta_E_1H_eV`: float (eV)
    - `delta_E_2H_eV`: float (eV)

### activation_barriers.json
- path: `/app/outputs/activation_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT activation barriers for intrarow and on-dimer decomposition pathways.
- schema:
  - `type`: object
  - `required`:
    - `intrarow_barrier_eV`: float (eV)
    - `on_dimer_barrier_eV`: float (eV)

### frustrated_energy_hydrogen.json
- path: `/app/outputs/frustrated_energy_hydrogen.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Work integral and frustrated translational energy of the H atom; the checker compares your reported values to a hidden reference.
- schema:
  - `type`: object
  - `required`:
    - `H_work_integral_eV`: float (eV)
    - `estimated_frustrated_translational_energy_eV`: float (eV)

Notes: Both values in frustrated_energy_hydrogen.json should be identical under the classical, minimum-energy-path, decoupling approximation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_E_0H_eV": "float (eV)",
          "delta_E_1H_eV": "float (eV)",
          "delta_E_2H_eV": "float (eV)"
        }
      },
      "description": "Energy difference ΔE = E(on-dimer) - E(intrarow) for 0, 1, and 2 coadsorbed H atoms."
    },
    {
      "file": "activation_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "intrarow_barrier_eV": "float (eV)",
          "on_dimer_barrier_eV": "float (eV)"
        }
      },
      "description": "DFT activation barriers for intrarow and on-dimer decomposition pathways."
    },
    {
      "file": "frustrated_energy_hydrogen.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "H_work_integral_eV": "float (eV)",
          "estimated_frustrated_translational_energy_eV": "float (eV)"
        }
      },
      "description": "Work integral and frustrated translational energy of the H atom; the checker compares your reported values to a hidden reference."
    }
  ],
  "notes": "Both values in frustrated_energy_hydrogen.json should be identical under the classical, minimum-energy-path, decoupling approximation."
}
```

## How you are scored
A hidden verifier independently checks your submitted files. For the relative energies and activation barriers, it compares your reported values against a hidden reference that corresponds to the original study’s results under the same or equivalent computational conditions; each comparison uses a tolerance that admits normal variability between different DFT codes and hardware while distinguishing a genuine reproduction from a coarse guess. For the frustrated translational energy, the verifier reads the force evidence file you provide and recomputes the integral W = ∫ F·dr; the result is compared to the hidden reference. The three scored components are combined with predetermined weights to yield a single reward between 0 and 1. Submitting a number that cannot be traced back to the required DFT scans will not pass the recomputation check.
