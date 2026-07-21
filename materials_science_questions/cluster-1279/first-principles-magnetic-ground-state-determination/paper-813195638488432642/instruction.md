# First-principles magnetic ground state determination of Cr2GeC

## Problem background
The layered ternary carbide Cr2GeC belongs to the MAX phase family of compounds (M_{n+1}AX_n), which are of interest for both fundamental science and applied technology due to their unusual combination of metallic and ceramic properties. Understanding the magnetic ordering in Cr2GeC is important because magnetic MAX phases could enable spintronics applications. Density functional theory (DFT) calculations, including a Hubbard U correction to treat Cr 3d electrons, have been used to compare different magnetic configurations and identify the ground state, but the precise ordering and the resulting magnetic moments are sensitive to the treatment of electron correlation. This task asks you to compute the relative stability of the nonmagnetic, ferromagnetic, and ferrimagnetic configurations and to characterize the magnetic properties of the most stable phase.

## Approach
First‑principles DFT calculations are carried out in the generalized gradient approximation (GGA‑PBE) with an on‑site Coulomb repulsion correction (GGA+U) on the Cr 3d states, using the Hubbard U and exchange J parameters specified below. The crystal structure is fixed to the hexagonal P63/mmc unit cell with the lattice constants a=2.925 Å, c=12.024 Å and the atomic positions listed under **Structure**. Three spin configurations are considered: nonmagnetic (NM), ferromagnetic (FM), and a ferrimagnetic (FIM) arrangement in which Cr spins within the Cr–C–Cr trilayer couple ferromagnetically while the coupling between trilayers across the Ge layer is antiferromagnetic. For each configuration, a self‑consistent total‑energy calculation is performed, and the total energies are compared to identify the magnetic ground state. From the charge density of the ferrimagnetic configuration, site‑resolved spin magnetic moments are obtained by integrating the spin density inside atomic spheres, and the spin‑resolved total density of states is computed to confirm the magnitude and nature of the spin splitting.

## Structure
Cr2GeC crystallises in the hexagonal space group P6₃/mmc (No. 194). Use the following atomic positions in the conventional cell:

| Atom | Wyckoff | x | y | z |
|------|---------|---|---|---|
| C    | 2a | 0.0 | 0.0 | 0.0 |
| Ge   | 2d | 2/3 | 1/3 | 1/4 |
| Cr   | 4f | 1/3 | 2/3 | 0.0833 |
| Cr   | 4f | 2/3 | 1/3 | 0.5833 |

These coordinates give the correct Cr–C–Cr trilayer stacking and Cr–Ge–Cr separation. For the conventional cell the total number of atoms is 8 (four Cr, two Ge, two C), corresponding to two formula units.

## Computational parameters
Use the following convergence and U‑correction parameters, which match the conditions described in the reference study:

- Plane‑wave energy cutoff: 450 eV
- k‑point mesh: 10×10×2 (Monkhorst–Pack)
- Smearing: Methfessel‑Paxton or equivalent, width 0.02 Ry (≈0.27 eV)
- Hubbard parameters for Cr 3d: U = 1.95 eV, J = 0.95 eV (effective U_eff = U – J = 1.0 eV)
- Pseudopotentials: ultrasoft or projector‑augmented wave PBE pseudopotentials (e.g., SSSP‑efficiency or GBRV)

## Magnetic configuration setup
In all spin‑polarised calculations, initial magnetic moments must be set to guide the self‑consistent field (SCF) cycle towards the desired configuration.

- **FM**: Place a positive initial moment of ~2 μB on every Cr atom; no moment on Ge and C.
- **FIM**: The ferrimagnetic order has two distinct Cr layers: Cr atoms at z ≈ 0.0833 (Cr_I) and Cr atoms at z ≈ 0.5833 (Cr_II) couple antiferromagnetically across the Ge slab, while the moments within each trilayer are parallel. Assign initial moments of +2 μB to Cr_I (two atoms at z ≈ 0.0833 and its symmetric equivalent) and −2 μB to Cr_II (two atoms at z ≈ 0.5833 and its symmetric equivalent). Ge and C start with zero moment.
- **NM**: Perform a non‑spin‑polarised calculation.

## Reproduction target
Use an open‑source GGA+U‑capable DFT code (e.g., Quantum ESPRESSO) to: (1) calculate the total energy of Cr2GeC in the NM, FM, and FIM configurations and report the relative energies; (2) from the FIM self‑consistent charge density, compute site‑resolved spin magnetic moments and the total net magnetic moment; (3) compute the spin‑polarized total density of states and verify that it shows a spin asymmetry indicative of a net moment. The target is not a single number but an energy ordering and a set of magnetic observables that must be internally consistent.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare input structure
- Role: process
- Action: Construct the crystal structure input file for Cr2GeC using the lattice constants, space group and atomic positions listed in the **Structure** section. The conventional cell contains two formula units.

### Step 2: Total energy calculations for magnetic configurations
- Role: scored
- Action: Perform self-consistent DFT calculations using the computational parameters and initial magnetic moments described above. Run three SCF calculations: nonmagnetic (NM), ferromagnetic (FM), and ferrimagnetic (FIM). Record the total energy for each configuration.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: magnetic_configuration (string), total_energy (eV), relative_energy (eV), relative_energy_per_atom (eV/atom)
- Scoring: scored by hidden verifier

### Step 3: Site-resolved magnetic moment calculation
- Role: scored (load-bearing)
- Action: From the self-consistent charge density of the FIM configuration, compute the spin magnetic moment inside each atomic sphere (using the DFT code's post-processing tool such as projwfc.x in QE). Sum the site-resolved moments to obtain the total net magnetic moment.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: atom_label (string), spin_moment (μB)
- Scoring: scored by hidden verifier

### Step 4: Total density of states (TDOS)
- Role: scored
- Action: Using the self-consistent charge density of the FIM configuration, compute the spin-resolved total density of states (e.g., via dos.x in QE). Output the energy grid and the corresponding spin-up and spin-down DOS.
- Output file: `/app/outputs/total_dos.dat`
- Format: txt
- Contract: energy (eV), spin_up_dos (states/eV/f.u.), spin_down_dos (states/eV/f.u.)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.csv`
- `/app/outputs/magnetic_moments.csv`
- `/app/outputs/total_dos.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total energies for NM, FM, FIM configurations; ordering and relative differences compared to the ground-state ordering.
- schema:
  - `required_columns`: `magnetic_configuration`, `total_energy`, `relative_energy`, `relative_energy_per_atom`
  - `units`:
    - `total_energy`: eV
    - `relative_energy`: eV
    - `relative_energy_per_atom`: eV/atom

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Site-resolved spin magnetic moments for the FIM state; total and individual values compared within hidden tolerances to the paper-reported values.
- schema:
  - `required_columns`: `atom_label`, `spin_moment`
  - `units`:
    - `spin_moment`: μB

### total_dos.dat
- path: `/app/outputs/total_dos.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Spin-polarized total density of states for the FIM phase; integrated spin difference checked for net moment and asymmetry consistent with ferrimagnetic ordering.
- schema:
  - `required_columns`: `energy`, `spin_up_dos`, `spin_down_dos`
  - `units`:
    - `energy`: eV
    - `spin_up_dos`: states/eV/f.u.
    - `spin_down_dos`: states/eV/f.u.

Notes: Only the ferrimagnetic (FIM) state magnetic moments and TDOS are scored; the nonmagnetic and ferromagnetic configurations are used only to verify the ground-state ordering via total energies. The structural optimization is omitted; use the given lattice constants. The partial DOS and charge density difference are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "magnetic_configuration",
          "total_energy",
          "relative_energy",
          "relative_energy_per_atom"
        ],
        "units": {
          "total_energy": "eV",
          "relative_energy": "eV",
          "relative_energy_per_atom": "eV/atom"
        }
      },
      "description": "Total energies for NM, FM, FIM configurations; ordering and relative differences compared to the ground-state ordering."
    },
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "atom_label",
          "spin_moment"
        ],
        "units": {
          "spin_moment": "μB"
        }
      },
      "description": "Site-resolved spin magnetic moments for the FIM state; total and individual values compared within hidden tolerances to the paper-reported values."
    },
    {
      "file": "total_dos.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "energy",
          "spin_up_dos",
          "spin_down_dos"
        ],
        "units": {
          "energy": "eV",
          "spin_up_dos": "states/eV/f.u.",
          "spin_down_dos": "states/eV/f.u."
        }
      },
      "description": "Spin-polarized total density of states for the FIM phase; integrated spin difference checked for net moment and asymmetry consistent with ferrimagnetic ordering."
    }
  ],
  "notes": "Only the ferrimagnetic (FIM) state magnetic moments and TDOS are scored; the nonmagnetic and ferromagnetic configurations are used only to verify the ground-state ordering via total energies. The structural optimization is omitted; use the given lattice constants. The partial DOS and charge density difference are not required."
}
```

## How you are scored
Each of the scored artifacts (total_energies.csv, magnetic_moments.csv, total_dos.dat) will be read by a hidden verifier that compares your computed results to reference expectations. For total_energies.csv, the verifier checks the relative ordering of the configurations and the magnitude of the energy differences. For magnetic_moments.csv, it compares the site‑resolved and total magnetic moments to known values within hidden tolerances. For total_dos.dat, it integrates the spin‑up and spin‑down DOS to estimate the net moment and checks for asymmetry consistent with a ferrimagnetic state. The verifier does not merely accept a reported number; it recomputes or cross‑validates where possible. The final reward is a weighted combination of scores from all three stages. You must generate the artifacts by genuine DFT calculations; fabricating numbers that simply match a reported result will not satisfy the consistency checks.