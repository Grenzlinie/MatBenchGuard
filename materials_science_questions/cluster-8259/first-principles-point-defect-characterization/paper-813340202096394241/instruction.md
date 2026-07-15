# First-principles defect formation energies in hybrid C/BN nanostructures

## Problem background
Hybrid carbon / boron nitride (C/BN) nanostructures—including nanotubes and planar superlattices with zigzag-edged domain boundaries—can exhibit half-metallic electronic properties that are attractive for spintronic applications. Point defects such as substitutional atoms and vacancies at the C-BN interface may alter local electronic structure and magnetic behaviour, making it important to understand where these defects are most likely to form and how their stability compares. This task addresses the neutral defect formation energetics in such hybrids using first-principles density functional theory (DFT). The computed formation energies will be used to assess whether defects preferentially locate at C-BN interfaces rather than deep inside pure C or BN domains, and whether substitutional defects are more stable than vacancies.

## Approach
The method uses spin-polarised DFT within the generalised-gradient approximation (GGA-PBE) as implemented in the open-source SIESTA code. Troullier–Martin pseudopotentials and a double-ζ-plus-polarisation localised basis set describe the valence electrons. Two model systems are considered: a (5,5) armchair C-BN nanotube with 160 atoms and a planar (5,7) C-BN superlattice. For each system, supercells with at least 30 Å vacuum separation are constructed, and seven neutral point defects (C_B, C_N, B_C, N_C, V_C, V_B, V_N) are placed at two interfaces (C-B and C-N) of the hybrid as well as at interior positions inside pure CNT and pure BNNT of the same chirality. Atomic positions are relaxed until forces are sufficiently small, and the Brillouin zone is sampled with dense k-point grids along the periodic direction. From the total energies of the pristine and defective supercells, and using the formation energies of the pure reference systems (pure CNT, pure BNNT, and the pristine hybrid), chemical potential bounds for nitrogen are established: a nitrogen-rich limit (precipitation into N₂) and a nitrogen-poor limit (the poorest nitrogen atmosphere that still permits h-BN growth). The carbon chemical potential is fixed at the C-rich limit (clean CNT), and the boron chemical potential is determined from the thermodynamic stability constraint of the hybrid. The neutral defect formation energy is then evaluated as E_f = E_tot(defect) - Σ n_i μ_i for every defect at each location, with μ_N varied across the allowed range. The outcome is a table of formation energies for all combinations of defect, location, and nitrogen chemical potential, which captures the relative stability trends.

## Reproduction target
Produce a comma-separated value (CSV) file at `/app/outputs/formation_energies.csv` that contains the neutral defect formation energies (in eV) for the hybrid C-BN nanostructures and the pure reference domains. The file must have one row per defect–location–μ_N combination and include the columns: `system` (values: `pure_CNT`, `pure_BNNT`, `hybrid`), `defect` (values: `C_B`, `C_N`, `B_C`, `N_C`, `V_C`, `V_B`, `V_N`), `location` (values: `interface_B`, `interface_N`, `interior_C`, `interior_BN`), `mu_N` (the nitrogen chemical potential in eV, at least three values spanning from the N-rich to the N-poor limit), and `E_f` (the formation energy in eV). The energies must be computed from spin-polarised DFT calculations performed with SIESTA, using the same pseudopotentials and basis set, and with chemical potentials derived from the reference systems as described in the workflow steps. The resulting CSV enables an independent check of whether interfacial formation energies are lower than those in the interior and whether substitutional formation energies are lower than those of the corresponding vacancies.

## Assets

- SIESTA DFT package: https://departments.icmab.es/leem/siesta/
- Troullier-Martin pseudopotentials for C, B, N: SIESTA pseudopotential library

## Workflow steps

### Step 1: Construct supercell models
- Role: process
- Action: Build atomic coordinates for pristine and defective supercells of (5,5) armchair C-BN nanotubes (160 atoms) and (5,7) planar C-BN superlattices, with >30 Å vacuum separation. Insert each neutral point defect (C_B, C_N, B_C, N_C, V_C, V_B, V_N) at the C-B and C-N interfaces of the hybrid systems and at interior positions within pure CNT and pure BNNT of the same chirality.
- Evidence: `/app/outputs/structures_metadata.json`

### Step 2: Perform DFT relaxations and total energy calculations
- Role: process
- Action: Run spin-polarized DFT calculations using SIESTA with Troullier-Martin pseudopotentials and double-ζ-plus-polarization basis for all pristine and defective supercells. Relax atomic positions until forces <0.02 eV/Å. Use at least 1×1×100 k-point sampling. Record final total energies and relaxed geometries.
- Evidence: `/app/outputs/dft_summary.json`

### Step 3: Determine chemical potential bounds
- Role: process
- Action: From the total energies of pure CNT, pure BNNT, and the pristine hybrid supercell, compute the formation energies of the reference systems and use them to establish chemical potential bounds for μ_N (N-rich limit from N2 precipitation; N-poor limit from h-BN growth). Fix μ_C to the C-rich limit (clean CNT) and express μ_B via μ_C+μ_B+μ_N = ΔE_f(CBN).
- Evidence: `/app/outputs/reference_energies.json`

### Step 4: Compute defect formation energies
- Role: scored (load-bearing)
- Action: Using the relaxed total energies and chemical potentials, compute the neutral defect formation energy E_f = E_tot(defect) - Σ n_i μ_i for every defect at each location. Use μ_C fixed to the CNT reference, μ_N spanning at least three values from N-rich to N-poor (derived from reference_energies), and μ_B determined from the stability constraint. Output one row per defect–location–μ_N combination.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: system (pure_CNT, pure_BNNT, hybrid), defect (C_B, C_N, B_C, N_C, V_C, V_B, V_N), location (interface_B, interface_N, interior_C, interior_BN), mu_N (float, eV), E_f (float, eV). One row per combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing computed neutral defect formation energies for all defect types, locations, and nitrogen chemical potential values. Used to verify the relative stability trends (interfacial vs interior preference, substitutional vs vacancy) via structural checks.
- schema:
  - `type`: table
  - `required_columns`: `system`, `defect`, `location`, `mu_N`, `E_f`
  - `units`:
    - `mu_N`: eV
    - `E_f`: eV

Notes: Charged defect calculations and electronic structure analysis (DOS, half-metallicity) are excluded per the reproduction scope. The scored target is limited to neutral defect formation energies and relative trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "defect",
          "location",
          "mu_N",
          "E_f"
        ],
        "units": {
          "mu_N": "eV",
          "E_f": "eV"
        }
      },
      "description": "CSV file containing computed neutral defect formation energies for all defect types, locations, and nitrogen chemical potential values. Used to verify the relative stability trends (interfacial vs interior preference, substitutional vs vacancy) via structural checks."
    }
  ],
  "notes": "Charged defect calculations and electronic structure analysis (DOS, half-metallicity) are excluded per the reproduction scope. The scored target is limited to neutral defect formation energies and relative trends."
}
```

## How you are scored
A hidden verifier reads your `formation_energies.csv` and checks the reported formation energies against expected structural trends. Specifically, for every defect type, the verifier compares the formation energy at the interface with the formation energy in the interior of the corresponding pure domain, and checks whether the interfacial value is lower. It also compares each substitutional defect with its associated vacancy (e.g., C_B vs V_C) at the same location and μ_N, and verifies that the substitutional is lower. The reward is based on the proportion of correct comparisons across all defect types and conditions. Simply reporting arbitrary numbers will not satisfy these checks; your computed energies must reflect the physical magnitudes obtained from the described DFT workflow.
