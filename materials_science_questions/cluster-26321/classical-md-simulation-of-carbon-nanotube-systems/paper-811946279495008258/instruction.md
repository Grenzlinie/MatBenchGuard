# Molecular mechanics quantification of CNT-β-CD interaction

## Problem background
Understanding how cyclodextrin molecules interact with carbon nanotubes is essential for designing stable, functional nanocomposites. In particular, the binding of β-cyclodextrin (β‑CD) onto multiwall carbon nanotubes (MWCNTs) depends on the nanotube surface perfection and on the orientation (head or tail) of the β‑CD molecule. Molecular mechanics simulations can quantify these interactions by computing binding energies and decomposing them into van der Waals, electrostatic, and hydrogen-bond contributions. This task asks you to determine, through systematic simulations, how these factors influence the binding strength and to what extent different non‑covalent forces contribute.

## Approach
Use classical molecular mechanics (MM) with a suitable open‑source engine to model isolated (40,0) carbon nanotubes – both perfect and containing a Stone–Wales defect – and a β‑cyclodextrin molecule. After optimizing the isolated building blocks to their minimum‑energy geometries, assemble four composite systems: head‑contact and tail‑contact β‑CD on the perfect CNT, and the same two orientations on the defective CNT. Optimize each composite using a classical force field and consistent convergence criteria. The binding energy is obtained as the difference between the total potential energy of the composite and the sum of the energies of the optimized isolated CNT and β‑CD. By parsing the force‑field energy output, decompose the nonbond part into van der Waals, electrostatic, and hydrogen‑bond components to reveal the interaction makeup.

## Reproduction target
Produce a CSV file `/app/outputs/binding_energies.csv` with one row per scenario (head_pCNT, tail_pCNT, head_dCNT, tail_dCNT) and columns: scenario, binding_energy, nonbond_energy, vdw_energy, electrostatic_energy, hbond_energy (all in kcal/mol). The hidden verifier will read this file and assess whether your computed energies and decompositions satisfy internal structural consistency checks that reflect the physical nature of CNT–β‑CD interactions. You must execute the full simulation pipeline described in the workflow steps; a fabricated answer that does not originate from actual simulations will not pass the verification.

## Assets

- Molecular mechanics engine (e.g., LAMMPS, OpenMM): https://lammps.sandia.gov
- CNT structure generator (TubeGen or similar): http://turin.nss.udel.edu/research/tubegenonline.html
- β-CD structure: https://pubchem.ncbi.nlm.nih.gov/compound/444041
- Force field parameters (OPLS-AA, CHARMM, or equivalent)

## Workflow steps

### Step 1: Build initial structures
- Role: process
- Action: Generate initial atomic coordinates for a perfect (40,0) CNT of length 38 Å with hydrogen termination, a (40,0) CNT containing a Stone–Wales defect, and a β-cyclodextrin molecule (with head secondary-OH and tail primary-OH rims).
- Evidence: none

### Step 2: Optimize isolated components
- Role: process
- Action: Perform geometry optimization on the isolated perfect CNT, defective CNT, and β-CD using a classical force field. Converge to force < 0.001 kcal/mol/Å and energy change < 5e-6 kcal/mol.
- Evidence: none

### Step 3: Assemble composite initial configurations
- Role: process
- Action: Place the head (secondary-OH side) or tail (primary-OH side) of the optimized β-CD near the surface of the perfect or defective CNT to create four starting structures: p-CNT+head, p-CNT+tail, d-CNT+head, d-CNT+tail.
- Evidence: none

### Step 4: Optimize composite systems
- Role: process
- Action: Minimize each composite system with the same force field and convergence criteria as for the isolated components, obtaining minimum-energy geometries and total potential energies.
- Evidence: none

### Step 5: Calculate binding energies and energy decomposition
- Role: scored (load-bearing)
- Action: Compute binding energy for each composite as E_complex − E_CNT − E_β-CD. Decompose the total potential energy into nonbond components (van der Waals, electrostatic, hydrogen bond). Write results to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: Columns: scenario (string: head_pCNT, tail_pCNT, head_dCNT, tail_dCNT), binding_energy (float, kcal/mol), nonbond_energy (float, kcal/mol), vdw_energy (float, kcal/mol), electrostatic_energy (float, kcal/mol), hbond_energy (float, kcal/mol). One row per scenario.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Binding energies and energy decomposition for head/tail attachment of β-CD on perfect and Stone–Wales defective (40,0) CNTs. The checker verifies relative trends: head vs tail preference on perfect CNT, defect effect, and van der Waals dominance.
- schema:
  - `type`: table
  - `required_columns`: `scenario`, `binding_energy`, `nonbond_energy`, `vdw_energy`, `electrostatic_energy`, `hbond_energy`
  - `units`:
    - `binding_energy`: kcal/mol
    - `nonbond_energy`: kcal/mol
    - `vdw_energy`: kcal/mol
    - `electrostatic_energy`: kcal/mol
    - `hbond_energy`: kcal/mol

Notes: Absolute binding energies are not required to match the paper; only relative trends and van der Waals dominance are scored. The agent must use an open-source MM code and a classical force field.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "scenario",
          "binding_energy",
          "nonbond_energy",
          "vdw_energy",
          "electrostatic_energy",
          "hbond_energy"
        ],
        "units": {
          "binding_energy": "kcal/mol",
          "nonbond_energy": "kcal/mol",
          "vdw_energy": "kcal/mol",
          "electrostatic_energy": "kcal/mol",
          "hbond_energy": "kcal/mol"
        }
      },
      "description": "Binding energies and energy decomposition for head/tail attachment of β-CD on perfect and Stone–Wales defective (40,0) CNTs. The checker verifies relative trends: head vs tail preference on perfect CNT, defect effect, and van der Waals dominance."
    }
  ],
  "notes": "Absolute binding energies are not required to match the paper; only relative trends and van der Waals dominance are scored. The agent must use an open-source MM code and a classical force field."
}
```

## How you are scored
A hidden verifier reads your `binding_energies.csv` and compares your computed values against hidden structural expectations derived from the physical behaviour of the system. The reward is a weighted combination of checks on the four scenarios. Your computed energies and decomposition must reflect the correct relative trends and physical roles of the different interaction components. Exact numerical agreement with any particular reference is not required – only the physically correct behaviour matters. The verification is fully automated and runs without any external network access.
