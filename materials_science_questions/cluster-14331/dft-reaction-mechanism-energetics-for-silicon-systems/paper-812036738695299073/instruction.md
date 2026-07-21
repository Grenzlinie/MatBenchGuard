# DFT Reaction Mechanism Energetics for Silicon Systems

## Problem background
During gas-source molecular beam epitaxy of silicon using precursors like silane or disilane, a key surface reaction is the decomposition of adsorbed silyl (SiH₃) to silylene (SiH₂) and a hydrogen atom. Silylene can adopt different adsorption configurations on the Si(100)-(2×1) surface, primarily intrarow (where it bridges two neighbouring silicon dimers along a dimer row) and on-dimer (where it inserts into a single surface dimer). The relative stability of these configurations is known to change with the local coverage of coadsorbed hydrogen released by the decomposition reaction itself. Understanding the decomposition pathway—which configuration is formed, the activation barriers that govern the rate, and the partitioning of the released energy among the products—is important for controlling film growth at the atomic scale. This task reproduces the density functional theory (DFT) study of these energetics: compute the relative energies of intrarow and on-dimer silylene at three hydrogen coverages, the activation barriers for the two decomposition channels, and the frustrated translational kinetic energy imparted to the hydrogen atom.

## Approach
The method uses periodic slab DFT within the generalized gradient approximation (Perdew–Burke–Ernzerhof functional) and a plane-wave basis set with norm-conserving pseudopotentials. The Si(100)-(2×1) surface is represented by a slab of several atomic layers; the bottom layer is kept fixed at bulk positions, the bottom face is passivated with hydrogen, and a vacuum gap separates periodic images. Silylene adsorbates are placed in both intrarow and on-dimer geometries, each with 0, 1, or 2 coadsorbed hydrogen atoms in the vicinity, and the structures are fully relaxed to obtain total energies. To follow the silyl decomposition, a series of constrained relaxations is performed: the distance between the silyl silicon and the departing hydrogen is held fixed at a sequence of values that span the bond-breaking range, while all other atomic positions are relaxed. The energy maximum along each series defines the transition state, and the activation barrier is the difference between transition-state and reactant energies. Finally, the Cartesian forces on the dissociating hydrogen atom are recorded in the exit valley (transition state to product) and numerically integrated to give the classical work W = ∫ F·dr, which is interpreted as the frustrated translational energy of the hydrogen.

## Reproduction target
For the Si(100)-(2×1) surface modeled with GGA-PBE and norm-conserving pseudopotentials, compute and save the following three quantities as structured JSON files:

1. **Relative silylene stability** – ΔE = E(on-dimer) − E(intrarow) for hydrogen coverages of 0, 1, and 2 coadsorbed H atoms, using the supercell that best minimises lateral interactions for each case.
2. **Activation barriers** – barrier energies (transition-state minus reactant) for the decomposition pathways leading to intrarow silylene and to on-dimer silylene.
3. **Frustrated translational energy of hydrogen** – the work integral along the exit valley of the intrarow channel, obtained from your own force data computed in the constrained scan.

You must perform the DFT calculations yourself and derive these quantities from them. The raw force data is not submitted; only the final numerical results are scored.

## Assets

- Quantum ESPRESSO plane-wave DFT code (or equivalent PBE/norm-conserving capable code): https://www.quantum-espresso.org/
- PBE norm-conserving pseudopotentials for Si and H from SSSP efficiency library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Optimize intrarow and on-dimer SiH₂ configurations with varying H coverage
- Role: process
- Action: Build the Si(100)-(2×1) slab model. Use the bulk Si lattice constant **a = 5.43 Å**. The slab consists of 6 layers of silicon; the bottom layer is fixed at ideal bulk positions, the bottom face is terminated with hydrogen, and a vacuum gap of about 10 Å is used.
  Add a SiH₂ adsorbate in both the **intrarow** and **on-dimer** geometries. For each geometry prepare three hydrogen coverages: **0 coadsorbed H**, **1 coadsorbed H** on a neighbouring dimer, and **2 coadsorbed H** atoms.

  **Initial geometry guidance**
  - Intrarow silylene: the SiH₂ group bridges two adjacent silicon dimers along the same dimer row. The silicon atom of SiH₂ bonds to one Si atom of each of the two dimers, forming a four-membered ring. Without coadsorbed H, the two involved dimers remain buckled. With 1 coadsorbed H, place one H atom on a dangling bond of the adjacent dimer (the dimer that is part of the four-membered ring) as illustrated in the paper (structure B). With 2 coadsorbed H atoms, place two H atoms on the two dangling bonds of that same adjacent dimer, making it symmetric (structure C).
  - On-dimer silylene: the SiH₂ group inserts into a single surface dimer. Its Si atom bonds to both Si atoms of the same dimer, while the dimer σ bond is preserved. Coadsorbed H atoms are placed on a neighbouring dimer: for 0 H no additional atoms; for 1 H, one H on a dangling bond of that neighbouring dimer; for 2 H, two H atoms saturate the two dangling bonds of the neighbouring dimer.

  **Supercell and k‑point sampling**
  Use supercell sizes that minimize lateral interactions:
  - For coverages 0 H and 1 H, use a **4×2** (or equivalently 2×4) supercell.
  - For coverage 2 H, use a **2×2** supercell.
  
  Sample the Brillouin zone with the following k‑point sets (the first direction is along the dimer bond, the second along the dimer row, the third perpendicular to the slab):
  - 2×2 supercell: 4 k‑points at (0, ±1/4, ±1/4).
  - 2×4 supercell: 2 k‑points at (0, 0, ±1/4).
  - 4×2 supercell: 2 k‑points at (0, ±1/4, 0).

  Fully relax each structure with DFT: use the PBE functional, a plane-wave cut-off energy of 20 Ry, and norm-conserving pseudopotentials. Record the final total energy of each configuration in a local file for use in Step 2; this file is **not** part of the final submission.

### Step 2: Compute relative stability of intrarow vs on-dimer silylene
- Role: scored
- Action: From the total energies recorded in Step 1, compute the energy difference ΔE = E(on-dimer) − E(intrarow) for each hydrogen coverage (0H, 1H, 2H). For each coverage use the energy obtained with the supercell prescribed above. Write the three ΔE values to a JSON file.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: {"delta_E_0H_eV": float, "delta_E_1H_eV": float, "delta_E_2H_eV": float}
- Scoring: scored by hidden verifier

### Step 3: Constrained DFT scans for intrarow and on-dimer decomposition
- Role: process
- Action: Starting from the adsorbed silyl (SiH₃) geometry, perform constrained relaxations to map the decomposition pathways.

  **Initial silyl geometry**
  Place the SiH₃ group on a surface dangling bond such that its Si atom binds to one Si atom of a surface dimer. The three H atoms point away from the surface in a near‑tetrahedral arrangement.
  - For the **intrarow pathway**: adsorb the silyl on a Si atom that belongs to a dimer row in a position that allows the departing H to leave and the remaining SiH₂ fragment to relax into the intrarow configuration bridging two adjacent dimers (similar to the initial state in the paper).
  - For the **on-dimer pathway**: adsorb the silyl on a dimer such that the same dimer will host the final on-dimer silylene after H departure.

  Constrained scans:
  - **Intrarow pathway**: Fix the distance d(Si–H) between the silyl silicon and the dissociating hydrogen to values covering the bond-breaking range. Use a scan from **1.4 Å to 3.4 Å** in steps of **0.1 Å** (at least 21 points).
  - **On-dimer pathway**: Fix d(Si–H) from **1.4 Å to 3.9 Å** in steps of **0.1 Å** (at least 26 points).
  At each constrained distance, relax all other ionic degrees of freedom fully. Record the total energy as a function of d(Si–H). Also save the **Cartesian force components** acting on the dissociating hydrogen atom for the **exit‑valley region** (i.e. from the transition state to the product minimum). These force data will be used in Step 5 to compute the work integral. The force file is an intermediate artefact and **is not submitted**.

### Step 4: Compute activation barriers for both decomposition pathways
- Role: scored (load-bearing)
- Action: From the energy curves obtained in Step 3, locate the transition state (energy maximum) and the reactant minimum for each pathway. Compute the activation barrier = E(transition state) − E(reactant). Write the two barrier values to a JSON file.
- Output file: `/app/outputs/activation_barriers.json`
- Format: json
- Contract: {"intrarow_barrier_eV": float, "on_dimer_barrier_eV": float}
- Scoring: scored by hidden verifier

### Step 5: Compute frustrated translational energy of hydrogen via force integration
- Role: scored (load-bearing)
- Action: Using the force data on the dissociating hydrogen atom recorded along the **intrarow exit valley** in Step 3, numerically integrate the force along the displacement from the transition state to the product well: **W = ∫ F·dr**. Interpret the integrated work as the frustrated translational kinetic energy of the H atom (they are identical under the classical, minimum-energy-path, decoupling approximation used in the reference study). Write the work integral and the estimated frustrated translational energy (the same numerical value) to a JSON file.
- Output file: `/app/outputs/frustrated_energy_hydrogen.json`
- Format: json
- Contract: {"H_work_integral_eV": float, "estimated_frustrated_translational_energy_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artefacts under `/app/outputs`. The **only files that will be read by the verifier** are:
- `/app/outputs/relative_energies.json`
- `/app/outputs/activation_barriers.json`
- `/app/outputs/frustrated_energy_hydrogen.json`

Other intermediate files (e.g. optimised structure energies, force scan data) **must not be submitted** and are not checked by the verifier.

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

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys) — it does **NOT** judge scientific correctness, and passing it does not mean your answer is correct.

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
A hidden verifier independently checks your submitted files. For the relative energies and activation barriers, it compares your reported values against hidden reference values that correspond to the published study’s results under the same computational conditions; each comparison uses a tolerance that admits normal variability between different DFT codes and hardware while distinguishing a genuine reproduction from a coarse guess. For the frustrated translational energy, the verifier compares your reported work integral and estimated energy to a hidden reference value derived from the paper (you must compute these yourself by integrating the exit‑valley forces obtained in your constrained scan). The three scored components are combined with predetermined weights to yield a single reward between 0 and 1. Submitting numbers that cannot be traced back to the required DFT scans will not pass the comparison.