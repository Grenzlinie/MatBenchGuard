# Calibrating dispersion-corrected atom-centered potentials for phosphorus

## Problem background
Standard density functional theory (DFT) with generalized gradient approximations (GGA) such as BLYP, BP, and PBE poorly describes dispersion (van der Waals) interactions. This limits its accuracy for binding energies and equilibrium geometries of weakly bound molecular systems. Dispersion-corrected atom-centered potentials (DCACPs) are atom-centered additions to the Kohn–Sham Hamiltonian that aim to recover dispersion interactions at low computational cost. This task aims to calibrate DCACPs for phosphorus for these three functionals using high‑level CCSD(T) reference data, and to evaluate how the correction affects computed interaction energies and equilibrium distances of several phosphorus‑containing dimers.

## Approach
The approach consists of three main phases: (i) generation of a high‑level reference interaction curve for the parallel (P₂)₂ dimer at the CCSD(T)/aug‑cc‑pVTZ level with counterpoise correction; (ii) computation of the corresponding uncorrected DFT (BLYP, BP, PBE) interaction curves using plane‑wave pseudopotential calculations; (iii) fitting a DCACP for phosphorus as a single nonlocal f‑channel Gaussian correction for each functional by minimizing a penalty function that measures the deviation of the DFT+DCACP total interaction energy from the CCSD(T) reference. The fitted potentials are then tested on three dimer systems — (P₂)₂, (PH₃)₂, and (PN)₂. For every system, functional, and correction type (uncorrected and DCACP), the interaction potential is scanned as a function of intermolecular distance. The binding energy (depth of the potential minimum) and equilibrium distance are extracted. The workflow requires initial monomer geometry optimizations at the MP2 level, followed by the reference, calibration, fitting, and evaluation steps.

## Reproduction target
Produce a CSV file at `/app/outputs/step_03_test_results.csv` that reports, for every combination of dimer system ((P₂)₂, (PH₃)₂, (PN)₂), functional (BLYP, BP, PBE), and correction type (uncorrected, DCACP), the binding energy (kJ/mol, defined as the depth of the interaction potential minimum; leave the field empty if the curve is purely repulsive) and the equilibrium intermolecular distance (Å). The required columns are: system, functional, correction_type, binding_energy_kJmol, equilibrium_distance_A. The DCACP‑corrected binding energies and equilibrium distances are the primary quantities to be checked.

## Assets

- Plane-wave DFT code (e.g., CPMD, Quantum ESPRESSO): https://www.quantum-espresso.org/
- CCSD(T) code (e.g., ORCA, PySCF): https://orcaforum.kofo.mpg.de/
- aug-cc-pVTZ basis set: https://www.basissetexchange.org/
- Goedecker-type pseudopotential for phosphorus: CPMD library or CP2K pseudopotential database
- Python with numpy, scipy: python3

## Workflow steps

### Step 1: Geometry optimization of monomers
- Role: process
- Action: Optimize the geometries of P2, PH3, and PN molecules at the MP2/aug-cc-pVTZ level using a quantum chemistry code (e.g., ORCA). Record the equilibrium coordinates for use in dimer construction.
- Evidence: `/app/outputs/optimized_geometries.json`

### Step 2: CCSD(T) reference interaction energies for (P2)2
- Role: process
- Action: Construct the (P2)2 dimer in parallel D2h geometry using the optimized P2 monomer. Compute CCSD(T)/aug-cc-pVTZ counterpoise-corrected interaction energies at a series of intermolecular separations. Write the reference curve (distance vs energy) to a file.
- Evidence: `/app/outputs/ccsdt_reference_curve.json`

### Step 3: DFT uncorrected interaction curves for (P2)2
- Role: process
- Action: Using a plane-wave DFT code with the Goedecker pseudopotential for phosphorus, compute DFT interaction energies for the (P2)2 dimer at the same intermolecular separations as the reference. Perform this for each of the three functionals: BLYP, BP, PBE. Save the energy curves.
- Evidence: `/app/outputs/dft_uncorrected_curves.json`

### Step 4: Fit DCACP parameters for phosphorus
- Role: process
- Action: Implement the DCACP formalism as a single nonlocal f-channel Gaussian correction potential. For each functional (BLYP, BP, PBE), define a penalty function that measures the deviation between the DFT total-energy interaction curve (uncorrected + DCACP) and the CCSD(T) reference. Minimize the penalty to obtain optimized DCACP parameters for phosphorus. Output the parameter sets in a Goedecker–Teter–Hutter compatible format.
- Evidence: `/app/outputs/dcacp_parameters.json`

### Step 5: Evaluate DCACPs on dimers and export results
- Role: scored (load-bearing)
- Action: For each dimer system ((P2)2, (PH3)2, (PN)2) and for each functional (BLYP, BP, PBE), perform plane-wave DFT calculations without DCACP and with the fitted DCACP. For each combination, scan the intermolecular distance, determine the interaction potential minimum, and extract the binding energy (kJ/mol) and equilibrium distance (Å). For purely repulsive curves, leave binding_energy_kJmol empty. Write all results to /app/outputs/step_03_test_results.csv with columns: system, functional, correction_type, binding_energy_kJmol, equilibrium_distance_A. Include both uncorrected and DCACP-corrected rows.
- Output file: `/app/outputs/step_03_test_results.csv`
- Format: csv
- Contract: CSV with columns: system (string: one of (P2)2, (PH3)2, (PN)2), functional (string: BLYP, BP, PBE), correction_type (string: uncorrected, DCACP), binding_energy_kJmol (numeric, empty for repulsive curves), equilibrium_distance_A (numeric).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_test_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_test_results.csv
- path: `/app/outputs/step_03_test_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies and equilibrium distances for all dimers, functionals, and correction types. The hidden checker compares DCACP-corrected rows to the paper-reported gold using tolerances.
- schema:
  - `type`: table
  - `required_columns`: `system`, `functional`, `correction_type`, `binding_energy_kJmol`, `equilibrium_distance_A`
  - `units`:
    - `binding_energy_kJmol`: kJ/mol
    - `equilibrium_distance_A`: Å

Notes: The solid-state tests (β-white and black phosphorus) are omitted due to computational cost. Only the dimer results are required to verify the DCACP calibration and transferability claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_test_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "functional",
          "correction_type",
          "binding_energy_kJmol",
          "equilibrium_distance_A"
        ],
        "units": {
          "binding_energy_kJmol": "kJ/mol",
          "equilibrium_distance_A": "Å"
        }
      },
      "description": "Binding energies and equilibrium distances for all dimers, functionals, and correction types. The hidden checker compares DCACP-corrected rows to the paper-reported gold using tolerances."
    }
  ],
  "notes": "The solid-state tests (β-white and black phosphorus) are omitted due to computational cost. Only the dimer results are required to verify the DCACP calibration and transferability claims."
}
```

## How you are scored
A hidden verifier reads your `step_03_test_results.csv` and independently compares the reported DCACP‑corrected binding energies and equilibrium distances against hidden reference values using absolute tolerances. Your overall score is the fraction of DCACP rows that satisfy the tolerance criteria. Uncorrected results are audited for qualitative consistency (e.g., repulsive character where expected). All workflow steps must be executed to produce the final CSV; reporting numbers without completing the calibration process will not pass the audit.
