# DFT and TD-DFT Property Calculation for Donor-Acceptor Monomers

## Problem background
Organic solar cells based on donor–acceptor (D–A) copolymers are a promising photovoltaic technology because their electronic properties can be tuned by choosing appropriate donor and acceptor units. A key challenge is to design low‑band‑gap polymers that absorb a broad portion of the solar spectrum and provide efficient charge separation. This task reproduces a computational study that designed nine D–A monomers with 4‑methoxy‑9‑methyl‑9H‑carbazole (MMCB) as the electron donor and various heterocyclic acceptors. The aim is to predict their geometric, electronic, and optical properties using first‑principles calculations and to determine how these properties change with the acceptor, guiding the selection of candidates for bulk‑heterojunction solar cells.

## Approach
The central idea is to use density functional theory (DFT) and its time‑dependent variant (TD‑DFT) to compute the properties of each monomer from scratch. For each of the nine monomers, two different environments are considered: isolated molecule (gas phase) and chloroform solvent, modeled with an implicit solvation model. The workflow consists of three main stages:
- Geometry optimization with a hybrid functional (B3LYP) and a double‑zeta basis set (6‑31G) to obtain the ground‑state structure.
- Extraction of geometric parameters (dihedral angle between donor and acceptor, linker bond length, dipole moment) and frontier molecular orbital energies (HOMO, LUMO) from the optimized geometry.
- TD‑DFT calculation on the optimized geometry to find the first singlet excited state, from which the optical gap (Eopt) and the absorption wavelength λmax are obtained.
From these, the band gap (Eg = LUMO − HOMO) and the exciton binding energy (EB = Eg − Eopt) are computed. All calculations are performed with an open‑source quantum chemistry package (ORCA, PySCF, or NWChem) and the standard 6‑31G basis set. The final output is a single table that collects the results for every monomer and phase, allowing a systematic comparison of the acceptor influence.

## Reproduction target
For the nine monomers defined in the bundled `monomers.smi` file, run the DFT and TD‑DFT calculations at the B3LYP/6‑31G level both in vacuum and using an implicit solvation model for chloroform. From these calculations, extract the following quantities for each monomer and phase:
- donor–acceptor dihedral angle (φ, in degrees),
- linker bond length (d_BL, in ångström),
- dipole moment (μ, in Debye),
- HOMO and LUMO energies (eV),
- band gap Eg = LUMO − HOMO (eV),
- first singlet excitation energy Eopt (eV) and its corresponding wavelength λmax (nm),
- exciton binding energy EB = Eg − Eopt (eV).
Compile all data into a single CSV file, `monomer_properties.csv`, with one row per monomer/phase (18 rows total) and the columns specified in the output contract. The hidden checker will then verify that your extracted dihedral angles, bond lengths, and band‑gap ordering are internally consistent and match the trends expected from the underlying chemistry, and that the exciton binding energies are physically meaningful.

## Assets

- Monomers SMILES file
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- 6-31G basis set

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: For each of the nine monomers (from monomers.smi), perform DFT geometry optimization using the B3LYP functional with the 6-31G basis set. Run in both gas phase and chloroform solvent (IEF-PCM model). Save the optimized geometries for all 18 monomer/phase combinations.
- Evidence: `/app/outputs/geomopt_outputs`

### Step 2: Extract geometric and electronic properties
- Role: process
- Action: From each optimized geometry, compute: donor–acceptor dihedral angle φ (degrees), link bond length d_BL (Å), dipole moment (Debye), HOMO energy (eV), LUMO energy (eV), and band gap Eg = LUMO − HOMO (eV). Save per-monomer/per-phase values for later compilation.
- Evidence: `/app/outputs/analysis_raw`

### Step 3: TD-DFT excited-state calculation
- Role: process
- Action: For each optimized geometry (monomer/phase), run a TD-DFT calculation at the B3LYP/6-31G level to obtain the first singlet excitation energy Eopt (eV) and its corresponding wavelength λmax (nm). Store the outputs.
- Evidence: `/app/outputs/tddft_outputs`

### Step 4: Compile final property table
- Role: scored (load-bearing)
- Action: Aggregate the computed properties for all nine monomers in both phases. Compute the exciton binding energy EB = Eg − Eopt (eV). Write a single CSV file monomer_properties.csv with one row per monomer/phase (18 rows total).
- Output file: `/app/outputs/monomer_properties.csv`
- Format: csv
- Contract: Table with columns: monomer (string), phase (string, 'gas' or 'sol'), phi_deg (float, degrees), d_BL_A (float, angstrom), dipole_D (float, Debye), HOMO_eV (float, eV), LUMO_eV (float, eV), Eg_eV (float, eV), Eopt_eV (float, eV), EB_eV (float, eV), lambda_max_nm (float, nm). 18 rows (9 monomers × 2 phases).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monomer_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monomer_properties.csv
- path: `/app/outputs/monomer_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Scored file: the checker verifies the Eg ordering trend matches the paper's exact ranking, all phi_deg fall within 130–160°, d_BL for 3,6-MMCB-SDP is near 1.54 Å while others are near 1.48 Å, and all EB are positive and within tolerance of reference values.
- schema:
  - `type`: table
  - `required_columns`: `monomer`, `phase`, `phi_deg`, `d_BL_A`, `dipole_D`, `HOMO_eV`, `LUMO_eV`, `Eg_eV`, `Eopt_eV`, `EB_eV`, `lambda_max_nm`
  - `units`:
    - `phi_deg`: degrees
    - `d_BL_A`: angstrom
    - `dipole_D`: Debye
    - `HOMO_eV`: eV
    - `LUMO_eV`: eV
    - `Eg_eV`: eV
    - `Eopt_eV`: eV
    - `EB_eV`: eV
    - `lambda_max_nm`: nm

Notes: The agent must run the full DFT and TD-DFT pipeline; the CSV is the sole scored artifact. The checker uses structural checks (ordering, range, anomaly) combined with value tolerances against paper-reported E_g and E_B references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monomer_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "monomer",
          "phase",
          "phi_deg",
          "d_BL_A",
          "dipole_D",
          "HOMO_eV",
          "LUMO_eV",
          "Eg_eV",
          "Eopt_eV",
          "EB_eV",
          "lambda_max_nm"
        ],
        "units": {
          "phi_deg": "degrees",
          "d_BL_A": "angstrom",
          "dipole_D": "Debye",
          "HOMO_eV": "eV",
          "LUMO_eV": "eV",
          "Eg_eV": "eV",
          "Eopt_eV": "eV",
          "EB_eV": "eV",
          "lambda_max_nm": "nm"
        }
      },
      "description": "Scored file: the checker verifies the Eg ordering trend matches the paper's exact ranking, all phi_deg fall within 130–160°, d_BL for 3,6-MMCB-SDP is near 1.54 Å while others are near 1.48 Å, and all EB are positive and within tolerance of reference values."
    }
  ],
  "notes": "The agent must run the full DFT and TD-DFT pipeline; the CSV is the sole scored artifact. The checker uses structural checks (ordering, range, anomaly) combined with value tolerances against paper-reported E_g and E_B references."
}
```

## How you are scored
A hidden verifier (checker) will read your `monomer_properties.csv` and evaluate it against several structural and ordering criteria that are derived from the known behavior of these molecules. It does not simply compare your numbers to a single fixed reference. Instead, it checks that:
- the dihedral angles fall within a plausible range for non‑planar D–A monomers,
- the linker bond length for a particular monomer differs systematically from the rest,
- the band gaps obey a specific ordering trend when the monomers are ranked,
- the exciton binding energies are positive and behave consistently across monomers and phases.
Each criterion carries a weight, and the final reward (a float between 0 and 1) is the weighted sum of the scores on these criteria. Because the constraints involve relative ordering and internal consistency, fabricating numbers without running the actual DFT/TD‑DFT pipeline will almost certainly violate them. You must genuinely execute the calculations and produce physically correct results to pass the verifier.
