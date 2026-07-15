# DFT spin-state and electronic structure analysis of iron dimer and trimer

## Problem background
Small transition-metal clusters exhibit magnetic ordering that can strongly influence their electronic structure. This reproduction task addresses the iron dimer (Fe2) and trimer (Fe3), where allowing ferromagnetic spin polarization is predicted to alter bonding and ionization energetics. The central question is to what extent spin‑restricted versus spin‑unrestricted density functional theory (DFT) calculations predict different optimized geometries and first adiabatic ionization potentials, and how those predictions compare with independent experimental benchmarks.

## Approach
The calculations follow a first‑principles DFT protocol. For Fe2 we compare two levels of theory: a spin‑restricted calculation and a spin‑unrestricted calculation that permits spin polarization. For Fe3 we perform only the spin‑unrestricted calculation because the trimer’s ground state is expected to be magnetic. In each case we: (i) optimize the geometry of the neutral cluster, (ii) compute the total energy of the neutral, (iii) optimize the geometry of the singly charged cation, (iv) compute its total energy, and (v) derive the adiabatic ionization potential (IP) as the difference between cation and neutral total energies. The computations use a generalized gradient approximation (GGA) exchange‑correlation functional together with a triple‑zeta quality basis set; the agent may select an open‑source implementation (e.g., ORCA). No external input files are required – the atomic positions are defined from the cluster stoichiometry. The final output contains bond lengths, total energies, and IPs for each spin mode and cluster.

## Reproduction target
Produce two JSON artifact files under `/app/outputs`: `step_01_fe2_results.json` containing the optimized bond length, neutral and cation total energies, and the adiabatic ionization potential for both spin‑restricted and spin‑unrestricted Fe2; and `step_02_fe3_results.json` containing the same quantities for spin‑unrestricted Fe3 (average bond length). All energies must be reported in electron‑volts and bond lengths in angstroms. The hidden verifier will examine these values for physical reasonableness and consistency with reference data, but the task objective is to complete the full computational workflow and report the resulting numbers.

## Assets

- ORCA quantum chemistry package: https://www.faccts.de/orca/

## Workflow steps

### Step 1: Fe2 structure and ionization potential
- Role: scored (load-bearing)
- Action: Perform DFT geometry optimization and ΔSCF ionization potential calculations for the iron dimer (Fe2) in spin-restricted and spin-unrestricted modes, using a GGA functional and triple-zeta basis set. Compute the neutral and cationic total energies at the optimized geometries, derive the adiabatic ionization potentials, and report the bond lengths. Write all results to step_01_fe2_results.json.
- Output file: `/app/outputs/step_01_fe2_results.json`
- Format: json
- Contract: JSON object with keys: Fe2_spin_restricted_bond_length (float, angstrom), Fe2_spin_unrestricted_bond_length (float), Fe2_spin_restricted_neutral_total_energy (float, eV), Fe2_spin_restricted_cation_total_energy (float, eV), Fe2_spin_unrestricted_neutral_total_energy (float, eV), Fe2_spin_unrestricted_cation_total_energy (float, eV), Fe2_spin_restricted_IP (float, eV), Fe2_spin_unrestricted_IP (float, eV).
- Scoring: scored by hidden verifier

### Step 2: Fe3 structure and ionization potential
- Role: scored
- Action: Perform DFT geometry optimization and ΔSCF ionization potential calculation for the iron trimer (Fe3) in spin-unrestricted mode, using a GGA functional and triple-zeta basis set. Compute neutral and cationic total energies at the optimized geometry, derive the adiabatic ionization potential, and report the average bond length. Write all results to step_02_fe3_results.json.
- Output file: `/app/outputs/step_02_fe3_results.json`
- Format: json
- Contract: JSON object with keys: Fe3_spin_unrestricted_bond_length (float, angstrom), Fe3_spin_unrestricted_neutral_total_energy (float, eV), Fe3_spin_unrestricted_cation_total_energy (float, eV), Fe3_spin_unrestricted_IP (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_fe2_results.json`
- `/app/outputs/step_02_fe3_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_fe2_results.json
- path: `/app/outputs/step_01_fe2_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Contains Fe2 optimized bond lengths, total energies, and computed adiabatic ionization potentials for both spin-restricted and spin-unrestricted DFT calculations. The checker verifies that spin-unrestricted IP is lower than restricted IP by a significant margin, that restricted and unrestricted IPs fall within allowed windows, and that bond lengths are physically reasonable.
- schema:
  - `type`: object
  - `required`:
    - `Fe2_spin_restricted_bond_length`: float (angstrom)
    - `Fe2_spin_unrestricted_bond_length`: float (angstrom)
    - `Fe2_spin_restricted_neutral_total_energy`: float (eV)
    - `Fe2_spin_restricted_cation_total_energy`: float (eV)
    - `Fe2_spin_unrestricted_neutral_total_energy`: float (eV)
    - `Fe2_spin_unrestricted_cation_total_energy`: float (eV)
    - `Fe2_spin_restricted_IP`: float (eV)
    - `Fe2_spin_unrestricted_IP`: float (eV)
  - `units`:
    - `bond_length`: angstrom
    - `total_energy`: eV
    - `IP`: eV

### step_02_fe3_results.json
- path: `/app/outputs/step_02_fe3_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Contains Fe3 optimized (average) bond length, total energies, and computed adiabatic ionization potential from spin-unrestricted DFT. The checker verifies that the IP falls within an allowed window and the bond length is physically reasonable.
- schema:
  - `type`: object
  - `required`:
    - `Fe3_spin_unrestricted_bond_length`: float (angstrom)
    - `Fe3_spin_unrestricted_neutral_total_energy`: float (eV)
    - `Fe3_spin_unrestricted_cation_total_energy`: float (eV)
    - `Fe3_spin_unrestricted_IP`: float (eV)
  - `units`:
    - `bond_length`: angstrom
    - `total_energy`: eV
    - `IP`: eV

Notes: The original paper used SCF-Xα-SW; this reproduction uses open-source DFT (e.g., ORCA with PBE/def2-TZVP). Tolerances are set to accommodate expected shifts due to functional and basis set differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_fe2_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Fe2_spin_restricted_bond_length": "float (angstrom)",
          "Fe2_spin_unrestricted_bond_length": "float (angstrom)",
          "Fe2_spin_restricted_neutral_total_energy": "float (eV)",
          "Fe2_spin_restricted_cation_total_energy": "float (eV)",
          "Fe2_spin_unrestricted_neutral_total_energy": "float (eV)",
          "Fe2_spin_unrestricted_cation_total_energy": "float (eV)",
          "Fe2_spin_restricted_IP": "float (eV)",
          "Fe2_spin_unrestricted_IP": "float (eV)"
        },
        "units": {
          "bond_length": "angstrom",
          "total_energy": "eV",
          "IP": "eV"
        }
      },
      "description": "Contains Fe2 optimized bond lengths, total energies, and computed adiabatic ionization potentials for both spin-restricted and spin-unrestricted DFT calculations. The checker verifies that spin-unrestricted IP is lower than restricted IP by a significant margin, that restricted and unrestricted IPs fall within allowed windows, and that bond lengths are physically reasonable."
    },
    {
      "file": "step_02_fe3_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Fe3_spin_unrestricted_bond_length": "float (angstrom)",
          "Fe3_spin_unrestricted_neutral_total_energy": "float (eV)",
          "Fe3_spin_unrestricted_cation_total_energy": "float (eV)",
          "Fe3_spin_unrestricted_IP": "float (eV)"
        },
        "units": {
          "bond_length": "angstrom",
          "total_energy": "eV",
          "IP": "eV"
        }
      },
      "description": "Contains Fe3 optimized (average) bond length, total energies, and computed adiabatic ionization potential from spin-unrestricted DFT. The checker verifies that the IP falls within an allowed window and the bond length is physically reasonable."
    }
  ],
  "notes": "The original paper used SCF-Xα-SW; this reproduction uses open-source DFT (e.g., ORCA with PBE/def2-TZVP). Tolerances are set to accommodate expected shifts due to functional and basis set differences."
}
```

## How you are scored
A hidden verifier reads your two JSON files and compares each reported quantity to reference criteria. The checks include that bond lengths lie within physically plausible bounds, that total energies are self‑consistent, and that the ionization potentials for different spin treatments display the expected structural relationship. The verifier combines the results of all checks into a final reward score between 0 and 1. To obtain full credit you must execute the DFT calculations and report derived values that satisfy the hidden criteria; reporting arbitrary or hand‑entered numbers will not pass.
