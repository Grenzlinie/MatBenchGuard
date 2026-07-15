# DFT Band Gap Calculation of a Hybrid Graphene Nanoribbon–ZnO Composite

## Problem background
Graphene nanoribbons (GNRs) can exhibit semiconducting band gaps that depend on their width and edge termination, making them attractive for electronic applications. Hybridizing a GNR with zinc oxide (ZnO) nanostructures has been suggested as a way to modify the ribbon's electronic structure. This task investigates a pristine armchair GNR (C74H20, width ~1.3 nm, hydrogen-passivated edges) and the same ribbon functionalized with a (Zn3O3)3 ring cluster. The open question is the value of the electronic band gap of each system.

## Approach
Use plane-wave density functional theory (DFT) within the generalized gradient approximation (GGA) with the PBE exchange-correlation functional. Construct a supercell for each system that is periodic along the ribbon length and includes sufficient vacuum in the perpendicular directions. First, build the pristine GNR model and relax its geometry. Then, attach the ZnO cluster to six carbon atoms of the relaxed GNR to form the hybrid composite, and relax the hybrid structure as well. For each relaxed geometry, compute the electronic band structure along a high-symmetry path of the Brillouin zone and extract the band gap (the energy difference between the valence band maximum and the conduction band minimum). An open-source DFT code such as Quantum ESPRESSO with standard pseudopotentials is used to perform all calculations.

## Reproduction target
Perform DFT calculations to obtain two numbers: the band gap (in eV) of the pristine armchair graphene nanoribbon (C74H20) and the band gap (in eV) of the hybrid GNR-ZnO composite. Report each as a single floating-point value in its respective output file.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP PBE pseudopotentials (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build pristine GNR atomic structure
- Role: process
- Action: Construct the atomic coordinates for a pristine armchair graphene nanoribbon supercell (C74H20) with width ~1.3 nm, hydrogen passivation on both edges, periodic along the ribbon length, and a vacuum layer of at least 20 Å in the non-periodic directions. Generate the initial input geometry file for DFT.
- Evidence: `/app/outputs/gnr_initial.cif`

### Step 2: DFT geometry optimization of pristine GNR
- Role: process
- Action: Perform geometry optimization of the pristine GNR supercell using Quantum ESPRESSO with the PBE exchange-correlation functional, a plane-wave kinetic energy cutoff of 340 eV (or equivalent Ry), a 4×1×1 Monkhorst-Pack k-point grid, and SSSP PBE efficiency pseudopotentials. Relax atomic positions until forces are below a reasonable threshold.
- Evidence: `/app/outputs/gnr_optimized.xyz`

### Step 3: Build hybrid GNR-ZnO atomic structure
- Role: process
- Action: Starting from the optimized pristine GNR, attach a (Zn3O3)3 ring cluster to six carbon atoms as described in the paper, forming the hybrid GNR-ZnO composite. Generate the initial atomic coordinates for the hybrid structure.
- Evidence: `/app/outputs/hybrid_initial.cif`

### Step 4: DFT geometry optimization of hybrid GNR-ZnO
- Role: process
- Action: Perform geometry optimization of the hybrid GNR-ZnO supercell using the same DFT parameters and pseudopotentials as in the previous optimization step (adding Zn and O pseudopotentials). Relax the structure to a local energy minimum.
- Evidence: `/app/outputs/hybrid_optimized.xyz`

### Step 5: Compute band gap of pristine GNR
- Role: scored (load-bearing)
- Action: Perform a DFT band structure calculation on the optimized pristine GNR (from step 02) along the Brillouin zone high-symmetry path. Determine the band gap (energy difference between valence band maximum and conduction band minimum) in eV and write the value to the output file.
- Output file: `/app/outputs/intrinsic_bandgap.txt`
- Format: txt
- Contract: A single floating-point number in eV, e.g., 1.234
- Scoring: scored by hidden verifier

### Step 6: Compute band gap of hybrid GNR-ZnO
- Role: scored (load-bearing)
- Action: Perform a DFT band structure calculation on the optimized hybrid GNR-ZnO (from step 04). Extract the band gap in eV and write it to the output file.
- Output file: `/app/outputs/hybrid_bandgap.txt`
- Format: txt
- Contract: A single floating-point number in eV, e.g., 0.567
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/intrinsic_bandgap.txt`
- `/app/outputs/hybrid_bandgap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### intrinsic_bandgap.txt
- path: `/app/outputs/intrinsic_bandgap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed band gap of the pristine armchair graphene nanoribbon (C74H20).
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the band gap of the pristine GNR in eV.

### hybrid_bandgap.txt
- path: `/app/outputs/hybrid_bandgap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed band gap of the hybrid GNR-ZnO composite.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the band gap of the hybrid GNR-ZnO composite in eV.

Notes: Both band gaps are compared to the paper's reported values with tolerances. Additionally, the hybrid gap must be smaller than the intrinsic gap by a required margin. Full reward requires both values within tolerance and the ordering condition satisfied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "intrinsic_bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the band gap of the pristine GNR in eV."
      },
      "description": "Computed band gap of the pristine armchair graphene nanoribbon (C74H20)."
    },
    {
      "file": "hybrid_bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the band gap of the hybrid GNR-ZnO composite in eV."
      },
      "description": "Computed band gap of the hybrid GNR-ZnO composite."
    }
  ],
  "notes": "Both band gaps are compared to the paper's reported values with tolerances. Additionally, the hybrid gap must be smaller than the intrinsic gap by a required margin. Full reward requires both values within tolerance and the ordering condition satisfied."
}
```

## How you are scored
Two artifacts are scored: `intrinsic_bandgap.txt` (the pristine GNR band gap) and `hybrid_bandgap.txt` (the hybrid composite band gap). A hidden verifier reads each file and compares the numeric value to a reference standard using a hidden tolerance. The verifier also inspects structural relationships between the two values. The final reward is a weighted combination of the scores for these two artifacts; full credit requires successfully executing the DFT workflow as described, not simply reporting any particular number.
