# DFT Reaction Energetics of SiH3 Insertion on Si(001)-(2x1):H Surface

## Problem background
In plasma-enhanced chemical vapor deposition of hydrogenated amorphous silicon (a-Si:H), the silyl radical (SiH3) is believed to be the dominant film‑forming precursor. A critical question is how SiH3 adsorbs on the hydrogen‑terminated, dimerized Si(001) surface. A proposed mechanism is dissociative insertion into the surface Si–Si dimer bond, which would generate two surface dihydride species. Establishing the energetics of this pathway — the relative stability of key intermediates and the activation barriers — is essential for understanding the kinetics of film growth. Your task is to compute the reaction energy profile of SiH3 insertion on a model of the Si(001)-(2×1):H surface.

## Approach
Use density functional theory (DFT) with the B3LYP functional, CEP‑31G(d) basis set plus an effective core potential on Si, and the 6‑31G basis set on H. Model the surface with a Si9H12 cluster: two Si atoms in the top layer (allowed to relax), four in the second layer, two in the third, and one in the fourth; dangling bonds to the bulk are capped with H at 1.50 Å. Direct the SiH3 radical at the centre of the surface Si–Si dimer in a Si‑down orientation. Optimise geometries and locate transition states along the reaction coordinate that comprise: (A) the transition state for radical insertion between the dimer atoms, breaking the Si–Si bond; (B) the intermediate immediately after insertion where the radical couples weakly to both dimer atoms; (C) the configuration after the radical bonds fully to one surface Si; (D) the transition state for hydrogen transfer from the radical to the other dimer Si; and (E) the final product with two surface SiH2 groups. The reference state (RS) is the optimised cluster plus a free SiH3 radical placed far from the surface. Compute total energies and report the energies of A–E relative to RS.

## Reproduction target
Produce a CSV file, energies.csv, containing the relative energies (in eV) of configurations A, B, C, D, E with the reference state (RS) set to zero. From these energies, the barrier for dimer‑breaking insertion is given directly by the relative energy of A, and the barrier for hydrogen transfer is the difference between the energies of D and C. The verifier will check that the reported energies lead to meaningful activation barriers and that the overall energy profile is physically consistent.

## Assets

- Open-source DFT code (e.g., PySCF, NWChem, ORCA): https://pyscf.org
- Basis sets CEP-31G(d) for Si and 6-31G for H: https://www.basissetexchange.org

## Workflow steps

### Step 1: Construct Si9H12 cluster model and initial geometries
- Role: process
- Action: Construct a Si9H12 cluster model of the Si(001)-(2x1):H surface: top layer (2 Si), second layer (4 Si), third layer (2 Si), fourth layer (1 Si). Replace Si-Si bonds to bulk with Si-H bonds at 1.50 Å and optimize only the top two Si atoms to allow dimer reconstruction. Prepare initial guess geometries for the reference state (free SiH3 radical) and stationary points A–E (SiH3 radical directed at dimer center, Si-down orientation).
- Evidence: `/app/outputs/cluster_geometries.xyz`

### Step 2: DFT reaction path energetics
- Role: scored (load-bearing)
- Action: Using an open-source DFT code with the B3LYP functional, CEP-31G(d) basis set on Si, 6-31G basis set on H, and an effective core potential on Si, perform geometry optimizations and transition state searches for the reference state (RS) and configurations A, B, C, D, E as described. Compute total energies and report them relative to the RS energy in a CSV file.
- Output file: `/app/outputs/energies.csv`
- Format: csv
- Contract: CSV with columns: configuration (string, one of A,B,C,D,E) and relative_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.csv
- path: `/app/outputs/energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed relative DFT energies of the five stationary points A-E along the dissociative insertion pathway. The reference state (RS) energy is taken as zero by convention and is not listed.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `relative_energy_eV`
  - `units`:
    - `relative_energy_eV`: eV

Notes: The checker will validate the CSV format, derive activation barriers (insertion barrier = E(A) - E(RS), H-transfer barrier = E(D) - E(C)), compare the five relative energies and two barriers to the hidden reference values within absolute tolerances, and verify structural ordering constraints. No MD simulation is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "relative_energy_eV"
        ],
        "units": {
          "relative_energy_eV": "eV"
        }
      },
      "description": "Computed relative DFT energies of the five stationary points A-E along the dissociative insertion pathway. The reference state (RS) energy is taken as zero by convention and is not listed."
    }
  ],
  "notes": "The checker will validate the CSV format, derive activation barriers (insertion barrier = E(A) - E(RS), H-transfer barrier = E(D) - E(C)), compare the five relative energies and two barriers to the hidden reference values within absolute tolerances, and verify structural ordering constraints. No MD simulation is required."
}
```

## How you are scored
A hidden verifier reads your energies.csv, validates its format, and independently derives the two activation barriers (insertion barrier = energy(A), H‑transfer barrier = energy(D) − energy(C)). It then compares each of the five relative energies and the two barriers against reference values that correspond to accurate DFT results, using predetermined tolerances. Additionally, it checks that the energy profile along the reaction path satisfies expected qualitative structural constraints (e.g., the insertion barrier is positive, and the energies of the minima and transition states follow a consistent order). The final score is a weighted sum of these checks, with the quantitative energy comparisons carrying the most weight.
