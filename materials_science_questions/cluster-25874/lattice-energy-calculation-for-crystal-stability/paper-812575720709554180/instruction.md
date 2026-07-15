# Reproduce periodic DFT relative stability of crystal polymorphs with and without dispersion correction

## Problem background
Hexaphenyl carbodiphosphorane (CDP^Ph) crystallizes in different solid-state forms: a bent P–C–P geometry is observed from most solvents, while crystallization from benzene gives a linear P–C–P arrangement with co-crystallized benzene. When the benzene is removed, the resulting desolvated linear phase (C') can be compared to the bent solvent-free phase (structure A). The relative energetic stability of the bent and desolvated linear polymorphs is expected to depend on a balance of intramolecular electronic interactions and intermolecular dispersion forces. By performing periodic density functional theory (DFT) optimizations with and without a dispersion correction, one can examine which functional correctly captures the energetic preference and how the predicted P–C–P bond angles compare to experimentally characterized geometries.

## Approach
Periodic DFT will be used to optimize the crystal structures of the bent polymorph (structure A, orthorhombic, P2₁2₁2₁) and the desolvated linear polymorph (C', trigonal, R-3 after removal of benzene). Two functionals are employed: the standard PBE functional (no dispersion) and PBE augmented with the D3(BJ) dispersion correction (PBE-D3). For each functional, both polymorphs are optimized to allow a direct comparison. After optimization, the total energy per CDP^Ph molecule and the P–C–P bond angle are extracted for each combination. The relative stability is assessed by computing the energy difference per molecule relative to the more stable structure at each functional level, expressed in kcal/mol. This setup probes whether the inclusion of dispersion interactions reverses the predicted stability ordering between the bent and linear forms.

## Reproduction target
Produce a CSV file (`step_01_optimization_results.csv`) that contains, for the bent (A) and desolvated linear (C') polymorphs, the following quantities obtained from periodic DFT optimizations at both the PBE and PBE-D3 levels:
- Final P–C–P bond angle (degrees)
- Total energy per CDP^Ph molecule (eV)
- Relative energy per CDP^Ph molecule (kcal/mol), with the zero of energy set to the more stable structure at each functional level.
The file must have exactly four rows (A_bent+PBE, A_bent+PBE-D3, Cprime_linear+PBE, Cprime_linear+PBE-D3) and the columns: `structure`, `functional`, `final_PCP_angle_deg`, `total_energy_per_CDP_eV`, `relative_energy_per_CDP_kcal_mol`. The purpose is to determine which functional predicts the bent or linear phase to be more stable and to compare the computed bond angles with physically plausible ranges.

## Assets

- CDPPh crystal structures: bent (A, orthorhombic P2₁2₁2₁) and linear (C, trigonal R-3 with co-crystallized benzene): CCDC 1980395 (structure A) and CCDC 1982550 (structure C)
- Periodic DFT code (CP2K, Quantum ESPRESSO, or VASP): https://www.cp2k.org
- Pseudopotentials/PAW datasets for C, H, P (e.g., GTH pseudopotentials for CP2K, SSSP for Quantum ESPRESSO): bundled with DFT code or from code-specific repositories
- Python with pandas (optional): pandas

## Workflow steps

### Step 1: Prepare input structures
- Role: process
- Action: Obtain the crystal structure CIF files for bent CDPPh (structure A, orthorhombic, P2₁2₁2₁; CCDC 1980395) and linear CDPPh with co-crystallized benzene (structure C, trigonal, R-3; CCDC 1982550) from the Cambridge Structural Database. Remove all benzene molecules from structure C to create the desolvated linear C' unit cell. Save the prepared structures in a format suitable for periodic DFT input.
- Evidence: `/app/outputs/prepared_structures.zip`

### Step 2: PBE optimization of bent structure A
- Role: process
- Action: Run a periodic DFT geometry optimization (atomic positions and cell parameters) on structure A using the PBE functional without dispersion correction. Use appropriate k‑point sampling, an energy cutoff consistent with the pseudopotentials, and standard convergence criteria. Save the final optimized geometry and total energy output log.
- Evidence: `/app/outputs/PBE_opt_A.log`

### Step 3: PBE optimization of desolvated linear structure C'
- Role: process
- Action: Run a periodic DFT geometry optimization on the desolvated linear structure C' using the PBE functional, with the same settings as step_02. Save the final geometry and total energy output log.
- Evidence: `/app/outputs/PBE_opt_Cprime.log`

### Step 4: PBE-D3 optimization of bent structure A
- Role: process
- Action: Run a periodic DFT geometry optimization on structure A using the PBE functional with the D3(BJ) dispersion correction. Use the same computational settings as the PBE runs. Save the final geometry and total energy output log.
- Evidence: `/app/outputs/PBE-D3_opt_A.log`

### Step 5: PBE-D3 optimization of desolvated linear structure C'
- Role: process
- Action: Run a periodic DFT geometry optimization on structure C' using the PBE-D3(BJ) functional, identical settings. Save the final geometry and total energy output log.
- Evidence: `/app/outputs/PBE-D3_opt_Cprime.log`

### Step 6: Collect results and write scored CSV
- Role: scored (load-bearing)
- Action: From the optimized structures of steps 02‑05, extract for each structure‑functional combination: the P–C–P bond angle (degrees), the total energy per CDPPh molecule (eV), and the relative energy per CDPPh molecule (kcal/mol) taking the more stable structure at each functional level as the energy zero. Write a CSV file with columns: structure, functional, final_PCP_angle_deg, total_energy_per_CDP_eV, relative_energy_per_CDP_kcal_mol. The file must contain exactly four rows: A_bent+PBE, A_bent+PBE-D3, Cprime_linear+PBE, Cprime_linear+PBE-D3.
- Output file: `/app/outputs/step_01_optimization_results.csv`
- Format: csv
- Contract: CSV with columns: structure (string: 'A_bent' or 'Cprime_linear'), functional (string: 'PBE' or 'PBE-D3'), final_PCP_angle_deg (float, degrees), total_energy_per_CDP_eV (float, eV), relative_energy_per_CDP_kcal_mol (float, kcal/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_optimization_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_optimization_results.csv
- path: `/app/outputs/step_01_optimization_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed results from periodic DFT optimizations, including energy ordering between bent and linear polymorphs with and without dispersion correction.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `functional`, `final_PCP_angle_deg`, `total_energy_per_CDP_eV`, `relative_energy_per_CDP_kcal_mol`
  - `units`:
    - `final_PCP_angle_deg`: degrees
    - `total_energy_per_CDP_eV`: eV
    - `relative_energy_per_CDP_kcal_mol`: kcal/mol

Notes: The ordering of relative energies (which structure is more stable) and the numerical ranges of the P-C-P angles are the scored quantities. The checker will verify that the reported values follow the physically meaningful trend and lie within acceptable tolerances derived from the paper's reference data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_optimization_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "functional",
          "final_PCP_angle_deg",
          "total_energy_per_CDP_eV",
          "relative_energy_per_CDP_kcal_mol"
        ],
        "units": {
          "final_PCP_angle_deg": "degrees",
          "total_energy_per_CDP_eV": "eV",
          "relative_energy_per_CDP_kcal_mol": "kcal/mol"
        }
      },
      "description": "Computed results from periodic DFT optimizations, including energy ordering between bent and linear polymorphs with and without dispersion correction."
    }
  ],
  "notes": "The ordering of relative energies (which structure is more stable) and the numerical ranges of the P-C-P angles are the scored quantities. The checker will verify that the reported values follow the physically meaningful trend and lie within acceptable tolerances derived from the paper's reference data."
}
```

## How you are scored
A hidden verifier inspects the scored CSV artifact (`step_01_optimization_results.csv`). It checks that the reported relative energy ordering between the two polymorphs is physically reasonable at each functional level and that the P–C–P bond angles fall within acceptable boundaries derived from known structural data. The verifier compares your reported values against hidden reference criteria (tolerances and ordering constraints) but does not require exact numerical agreement with any published table. Simply reporting literature numbers without genuinely performing the DFT optimizations will not pass; the checks are designed to validate that the underlying computations were executed. The final score is a float between 0.0 and 1.0 that reflects how well your submitted results satisfy the required physical trends and structural ranges.
