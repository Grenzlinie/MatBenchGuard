# Ensemble QM/MM Calculation of P450 Compound I: Electronic Structure and Fe–O Bond Enthalpy

## Problem background
Cytochrome P450 (CYP) enzymes are central to drug metabolism. The key oxidising species in their catalytic cycle is Compound I (Cpd I), a high‑valent iron‑oxo porphyrin π‑cation radical. A major open question is whether the electronic structure and the strength of the Fe–O bond of Cpd I vary between different CYP isoforms or change when a substrate is present in the active site. Answering this question is critical for building quantitative models that predict CYP reactivity and selectivity. This task focuses on the bacterial isoform P450cam (PDB 1DZ9) and aims to determine, through a full multi‑scale computational protocol, how the structural, electronic, and energetic properties of Cpd I differ between the substrate‑free (apo) enzyme and the enzyme bound to a small substrate molecule (propene).

## Approach
The protocol combines stochastic‑boundary molecular dynamics (MD) sampling with hybrid quantum mechanics/molecular mechanics (QM/MM) geometry optimisation. For each of the two systems (P450cam‑apo and P450cam‑propene), an MD simulation using the CHARMM27 force field generates an ensemble of protein conformations. From each MD trajectory, several snapshots are extracted and first minimised with the MM force field to relieve steric strain. Then each snapshot is refined at the QM/MM level, treating the porphine ring plus the cysteinate ligand (–SCH₃) as the quantum region, with the rest of the protein described by CHARMM27. In the propene‑bound system the entire substrate molecule is included in the QM region. The QM calculations use density functional theory (B3LYP) with effective core potentials (LACVP) and 6‑31G* basis sets, and the Cpd I quartet spin state is modelled with a restricted open‑shell approach. Link atoms handle the QM/MM boundary, and fixed MM charges polarise the QM wavefunction. From each optimised geometry, key structural and electronic properties (bond lengths, Mulliken spin densities) are extracted, and the Fe–O bond enthalpy ΔE₂ is estimated via a thermodynamic cycle that involves the QM/MM energies of the full Cpd I and the de‑oxygenated fragment, together with reference energies from a small‑model DFT calculation. All per‑snapshot quantities are collected in a single CSV file, from which ensemble averages are computed.

## Reproduction target
For the bacterial P450cam isoform (PDB ID 1DZ9) in both the substrate‑free (P450cam_apo) and propene‑bound (P450cam_prop) forms, execute the complete MD → MM minimisation → QM/MM optimisation pipeline. Produce a single CSV file `per_snapshot_properties.csv` that contains, for at least 5 snapshots per system, the following per‑snapshot quantities:

- system identifier ("P450cam_apo" or "P450cam_prop")
- snapshot id
- Fe–S bond length (Å)
- Fe–O bond length (Å)
- Mulliken spin densities on Fe, S, O, and the porphyrin
- Fe–O bond enthalpy ΔE₂ (kcal mol⁻¹)

From this file, ensemble averages for each system can be computed to evaluate whether the electronic structure and the Fe–O bond enthalpy differ between the substrate‑free and substrate‑bound states.

## Assets

- P450cam crystal structure (PDB 1DZ9): https://www.rcsb.org/structure/1DZ9
- Propene molecule: https://pubchem.ncbi.nlm.nih.gov/compound/8252
- CHARMM27 forcefield parameters: CHARMM27
- Open-source MD engine with CHARMM27 support: https://openmm.org
- Open-source QM/MM software supporting B3LYP/LACVP,6-31G*: https://www.cp2k.org

## Workflow steps

### Step 1: Prepare initial protein structures
- Role: process
- Action: Obtain the P450cam crystal structure (PDB 1DZ9). Reverse any non-wild-type mutations to restore the wild-type enzyme. Prepare two systems: (i) substrate-free (P450cam_apo) and (ii) with a propene molecule docked into the active site (P450cam_prop). Generate CHARMM27 topologies and coordinates for both systems.
- Evidence: `/app/outputs/prepared_structures.txt`

### Step 2: Stochastic-boundary molecular dynamics sampling
- Role: process
- Action: For each system, run a 5 ns production MD simulation using the CHARMM27 force field under stochastic-boundary conditions. Save coordinates at 200 ps intervals to obtain at least 5 snapshots per system.
- Evidence: `/app/outputs/md_snapshots.log`

### Step 3: MM energy minimization of snapshots
- Role: process
- Action: For every saved MD snapshot, perform MM energy minimization with CHARMM27 using steepest descent followed by adapted-basis Newton–Raphson minimization to relieve steric strain before QM/MM treatment.
- Evidence: `/app/outputs/mm_minimized_energies.txt`

### Step 4: QM/MM geometry optimization
- Role: process
- Action: For each MM-minimized snapshot, perform QM/MM geometry optimization at the B3LYP/LACVP,6-31G* level of theory. The QM region must contain the porphine ring (without substituents) and the cysteinate ligand modeled as methyl mercaptide (⁻SCH₃). In the propene system, include the entire propene molecule in the QM region. Model the quartet spin state of Compound I using a restricted open-shell approach. The MM region (CHARMM27) is optimized at each QM step, and fixed MM charges are included in the QM Hamiltonian. Use link atoms at QM/MM boundaries and zero out charges on link atoms and neighboring atoms to preserve total charge.
- Evidence: `/app/outputs/qm_optimized_geometries`

### Step 5: Small-model DFT reference calculations
- Role: process
- Action: Using the same DFT level (B3LYP/LACVP,6-31G*), compute the triplet oxygen atom energy E_QM(O) and the energies of a small heme model (porphine + ⁻SH) for the relaxed low-spin doublet Fe(III) fragment (E_QM(Fe)) and the unrelaxed Fe(III) fragment (E_QM(Fe*)). The relaxation correction ΔE_relax = E_QM(Fe) − E_QM(Fe*) is used later in the ΔE₂ estimator and is computed once for all snapshots.
- Evidence: `/app/outputs/small_model_energies.txt`

### Step 6: Compile per-snapshot properties and Fe–O bond enthalpy
- Role: scored (load-bearing)
- Action: For every QM/MM-optimized snapshot, extract the Fe–S and Fe–O bond lengths and Mulliken spin densities on Fe, S, O, and the porphyrin. Estimate the Fe–O bond enthalpy ΔE₂ using the thermodynamic decomposition: ΔE₂ = E_QM(O) + (E_QM(Fe) − E_QM(Fe*)) + E_QM/MM(Fe*) − E_QM/MM(FeO), where E_QM/MM(FeO) is the QM/MM energy of the optimized Cpd I structure and E_QM/MM(Fe*) is the QM/MM energy obtained by deleting the ferryl oxygen from that structure and performing a single-point calculation with the Fe(III) fragment treated as a low-spin doublet. Write a CSV file `per_snapshot_properties.csv` containing all per-snapshot quantities for both P450cam_apo and P450cam_prop (at least 5 snapshots per system).
- Output file: `/app/outputs/per_snapshot_properties.csv`
- Format: csv
- Contract: Columns: system (string), snapshot_id (integer), Fe_S_bond_length_A (float), Fe_O_bond_length_A (float), spin_density_S (float), spin_density_O (float), spin_density_Fe (float), spin_density_porph (float), DeltaE2_kcal_per_mol (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/per_snapshot_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### per_snapshot_properties.csv
- path: `/app/outputs/per_snapshot_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-snapshot properties and Fe–O bond enthalpy for both P450cam_apo and P450cam_prop systems, enabling the checker to compute ensemble averages and verify the substrate effect.
- schema:
  - `type`: table
  - `required_columns`: `system`, `snapshot_id`, `Fe_S_bond_length_A`, `Fe_O_bond_length_A`, `spin_density_S`, `spin_density_O`, `spin_density_Fe`, `spin_density_porph`, `DeltaE2_kcal_per_mol`
  - `units`:
    - `Fe_S_bond_length_A`: Å
    - `Fe_O_bond_length_A`: Å
    - `spin_density_S`: Mulliken spin density (e)
    - `spin_density_O`: Mulliken spin density (e)
    - `spin_density_Fe`: Mulliken spin density (e)
    - `spin_density_porph`: Mulliken spin density (e)
    - `DeltaE2_kcal_per_mol`: kcal mol⁻¹

Notes: The agent must run the full MD → MM minimization → QM/MM optimization pipeline; the scored CSV is only produced after all prior stages. At least 5 snapshots per system are required. The checker will compute per-system averages from this CSV and compare them to hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "per_snapshot_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "snapshot_id",
          "Fe_S_bond_length_A",
          "Fe_O_bond_length_A",
          "spin_density_S",
          "spin_density_O",
          "spin_density_Fe",
          "spin_density_porph",
          "DeltaE2_kcal_per_mol"
        ],
        "units": {
          "Fe_S_bond_length_A": "Å",
          "Fe_O_bond_length_A": "Å",
          "spin_density_S": "Mulliken spin density (e)",
          "spin_density_O": "Mulliken spin density (e)",
          "spin_density_Fe": "Mulliken spin density (e)",
          "spin_density_porph": "Mulliken spin density (e)",
          "DeltaE2_kcal_per_mol": "kcal mol⁻¹"
        }
      },
      "description": "Per-snapshot properties and Fe–O bond enthalpy for both P450cam_apo and P450cam_prop systems, enabling the checker to compute ensemble averages and verify the substrate effect."
    }
  ],
  "notes": "The agent must run the full MD → MM minimization → QM/MM optimization pipeline; the scored CSV is only produced after all prior stages. At least 5 snapshots per system are required. The checker will compute per-system averages from this CSV and compare them to hidden reference values."
}
```

## How you are scored
After you finish, a hidden verifier will read your `per_snapshot_properties.csv` file. It will compute the per‑system ensemble averages of the structural, electronic, and energetic properties and compare them to hidden reference values that correspond to a correct execution of the protocol. The verifier checks for agreement within reasonable tolerances and also tests whether the Fe–O bond enthalpy exhibits the expected physical trend between the substrate‑free and substrate‑bound forms. Your final reward is a weighted combination of the scores from each scored stage, with this load‑bearing CSV carrying the largest weight. Simply reporting published numbers without running the computational protocol is not sufficient; the verifier requires data that are produced by your own pipeline.
