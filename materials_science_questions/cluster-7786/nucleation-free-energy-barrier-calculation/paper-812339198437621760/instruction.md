# Calcite-Stearate Interfacial Energies via Molecular Dynamics

## Problem background
Calcite crystals nucleate on the polar (01.2) face on a variety of ionized organic substrates. Polar surfaces possess a macroscopic dipole moment that must be quenched for stable growth. This task investigates how the dipole moment can be quenched for an organic substrate with arbitrary charge density by modifying the density of Ca^{2+} ions in the terminating crystal plane via cation vacancies. Classical molecular dynamics simulations are used to compute interfacial energies for calcite (01.2) and (00.1) surfaces against stearic acid monolayers across a range of monolayer densities.

## Approach
The method uses classical molecular dynamics to simulate interfaces between calcite crystal slabs and stearate monolayers. For each surface (01.2) and (00.1), three monolayer densities are considered: the maximum density matching a full cation plane (ρmax), 4/5 ρmax, and 2/3 ρmax. To cancel the macroscopic dipole, the density of Ca^{2+} ions in the outermost crystal plane is adjusted according to the dipole quenching condition (sum of charge densities of the modified outer planes equals -σ_next/2). Four simulation blocks are constructed for each interface: a pure crystal slab, a pure water slab, a monolayer on a half‑water slab, and a monolayer on a half‑crystal slab. Molecular dynamics is run in the NVT ensemble at 300 K using the Pavese calcite potential, CHARMM22 for stearate headgroups, and TIP3P for water. From the average potential energies of each block (E_c, E_w, E_mw, E_mc) and the simulation cell surface area A, the interfacial energy γ_mc is computed as γ_mc = (E_mc – 0.5 E_c – (E_mw – 0.5 E_w)) / A.

## Reproduction target
Run the MD simulations and compute the interfacial energies for the six interfaces (two surfaces × three densities). Write the results to a CSV file with one row per interface, containing the surface label, the monolayer density fraction, the Ca^{2+} density fraction used, the monolayer unit cell b parameter (in Å), and the computed interfacial energy (in mJ/m²). The CSV must contain at least three rows for the (01.2) surface and three rows for the (00.1) surface.

## Assets

- DL_POLY (or LAMMPS): https://www.scd.stfc.ac.uk/Pages/DL_POLY.aspx
- Pavese et al. calcite interatomic potential: 10.1007/BF00207812
- CHARMM22 force field for stearate headgroups: 10.1021/jp960059d
- TIP3P water model: 10.1063/1.445869
- Calcite crystal structure (rhombohedral, R-3c)

## Workflow steps

### Step 1: System setup and MD simulations
- Role: process
- Action: Set up atomic configurations for (01.2) and (00.1) calcite surfaces with stearate monolayers at three monolayer densities: ρmax, 4/5 ρmax, and 2/3 ρmax. Apply the dipole quenching condition (sum of charge densities of the modified outer planes equals -σ_{next}/2) to determine the required Ca²⁺ ionic density in the outer crystal planes. For each interface (two surfaces × three densities), construct the four simulation blocks: pure crystal slab, pure water slab, monolayer on half water slab, and monolayer on half crystal slab. Run NVT MD simulations at 300 K using DL_POLY (or LAMMPS) with the Pavese calcite potential, CHARMM22 for stearate headgroups, and TIP3P for water. Obtain average potential energies (E_c, E_w, E_mw, E_mc) and the simulation cell surface area A for each block, to be used in the next step.
- Evidence: none

### Step 2: Compute interfacial energies and report
- Role: scored
- Action: From the MD average energies obtained in step 1, compute the interfacial energy for each interface using the relation γ_mc = (E_mc – 0.5 E_c – (E_mw – 0.5 E_w)) / A. Write a CSV file with one row per interface (six rows total) containing the surface label, monolayer density fraction, Ca²⁺ density fraction, monolayer b lattice parameter in Å, and the computed interfacial energy in mJ/m².
- Output file: `/app/outputs/interfacial_energies.csv`
- Format: csv
- Contract: CSV with header row; columns: surface (string, values '(01.2)' or '(00.1)'), monolayer_density_fraction (float, fraction of ρmax, values 1.0, 0.8, ~0.667), ca_density_fraction (float, required Ca²⁺ density fraction from dipole quenching), b_param_Angstrom (float, monolayer unit cell b dimension in Å), interfacial_energy_mJm2 (float, computed interfacial energy in mJ/m²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interfacial_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interfacial_energies.csv
- path: `/app/outputs/interfacial_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing the computed interfacial energies.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `monolayer_density_fraction`, `ca_density_fraction`, `b_param_Angstrom`, `interfacial_energy_mJm2`
  - `units`:
    - `b_param_Angstrom`: Å
    - `interfacial_energy_mJm2`: mJ/m²
  - `notes`: Six rows: three monolayer densities for each of the two surfaces.

Notes: The task outputs a single CSV file with the computed interfacial energies. Scoring is based on structural trends (T3) rather than exact numerical match to the paper's values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interfacial_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "monolayer_density_fraction",
          "ca_density_fraction",
          "b_param_Angstrom",
          "interfacial_energy_mJm2"
        ],
        "units": {
          "b_param_Angstrom": "Å",
          "interfacial_energy_mJm2": "mJ/m²"
        },
        "notes": "Six rows: three monolayer densities for each of the two surfaces."
      },
      "description": "CSV file containing the computed interfacial energies."
    }
  ],
  "notes": "The task outputs a single CSV file with the computed interfacial energies. Scoring is based on structural trends (T3) rather than exact numerical match to the paper's values."
}
```

## How you are scored
A hidden verifier will read your submitted CSV file and check that it contains the required columns and the expected number of rows. The verifier then evaluates whether the computed interfacial energies satisfy certain structural relationships that are expected from the physical model. The verifier does NOT compare your numbers against the specific values reported in the literature; instead, it checks for internal consistency and physically meaningful ordering of the results. The final score is a weighted combination of these structural checks. Simply reporting numbers without running the full MD workflow will not meet the structural criteria.
