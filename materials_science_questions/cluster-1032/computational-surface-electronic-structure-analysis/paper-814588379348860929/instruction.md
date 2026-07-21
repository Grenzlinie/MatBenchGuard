# Bulk properties of antiferromagnetic transition-metal oxides from LDA+U+SOI DFT

## Problem background
Antiferromagnetic late transition-metal oxides MnO, FeO, CoO, and NiO crystallize in the rocksalt structure and are textbook examples of strongly correlated electron systems. Their bulk structural, magnetic, and electronic properties are governed by the localized 3d electrons of the transition-metal ions, by superexchange-driven antiferromagnetic ordering, and by spin-orbit coupling. Accurate first-principles prediction of these properties requires going beyond standard local-density approximations; a widely used approach is DFT+U with spin-orbit coupling and noncollinear spins. The computed bulk lattice constants, magnetic moments, easy magnetization axes, and fundamental Kohn-Sham band gaps serve as essential references for understanding the surfaces of these materials and are the focus of this task.

## Approach
The core method is self-consistent density functional theory (DFT) in the local-density approximation (LDA) augmented by an on-site Hubbard U correction (Dudarev scheme, U=4 eV) and spin-orbit coupling, using a noncollinear spin treatment. The bulk rocksalt crystal structures of MnO, FeO, CoO, and NiO are taken as the initial input. For each material, the cubic lattice constant is relaxed to minimize the total energy. The self-consistent charge and magnetization densities then provide the total magnetic moment (spin plus orbital contributions) integrated inside the PAW spheres. The easy magnetization direction (axis or plane) is determined by comparing total energies for several high-symmetry spin orientations. Finally, the Kohn-Sham band structure is computed along high-symmetry lines, from which the indirect and direct fundamental gaps are extracted. The workflow can be executed with any open-source DFT code that supports LDA+U, spin-orbit coupling, noncollinear spins, and PAW pseudopotentials (e.g., Quantum ESPRESSO, ABINIT, GPAW).

## Computational parameters
To ensure physically meaningful results, use the following convergence parameters (which are consistent with the reference literature):

- **Exchange-correlation functional:** LDA (Perdew–Zunger parametrization) with Hubbard U correction (Dudarev scheme), including spin-orbit coupling and noncollinear spins.
- **Hubbard U:** U = 4 eV for all four materials.
- **Pseudopotentials:** Projector-augmented wave (PAW) method. Use standard LDA PAW pseudopotentials (e.g., from the SSSP library v1.2.0 or later for Quantum ESPRESSO, or LDA PAW potentials recommended for VASP).
- **Plane-wave cutoff:** 750 eV.
- **k‑point mesh:** Γ‑centered Monkhorst–Pack grid of at least 8×8×8 for the cubic conventional cell.
- **Total energy convergence:** Better than 1 meV per formula unit.
- **Lattice relaxation:** Relax the cubic lattice constant by minimizing total energy versus volume (e.g., Murnaghan equation-of-state fit or direct cell relaxation). Stop when stress components are below 0.1 kbar (10 MPa).

## Reproduction target
Compute, for each of the four antiferromagnetic oxides (MnO, FeO, CoO, NiO), the following bulk properties using LDA+U+SOI with U=4 eV:

- Equilibrium cubic lattice constant \(a_0\) (in Å)
- Total magnetic moment \(\mu\) (in \(\mu_\mathrm{B}\))
- Easy spin axis or plane (as a string)
- Indirect Kohn-Sham fundamental gap \(E_\mathrm{g}^\mathrm{ind}\) (in eV)
- Direct fundamental gap \(E_\mathrm{g}^\mathrm{dir}\) (in eV)

### Determining the easy spin axis/plane
1. Perform noncollinear spin-polarized total-energy calculations with the spin magnetization fixed along several high-symmetry directions (at least [001], [111], [110]).
2. Identify the orientation that gives the lowest total energy.
3. If a single direction is the clear minimum, report it in bracket notation `[uvw]` (e.g., `[111]`). If several directions within a plane are nearly degenerate, report the easy plane as `(hkl) plane` (e.g., `(111) plane`). If more than one equivalent set of directions appears, separate them with a comma and a space (e.g., `~[-1-1 1.5], [-110]`).
4. Use plain text characters without LaTeX markup; the tilde `~` or the ≈ symbol may be used to indicate approximate equality.

### Extracting band gaps
- Compute the Kohn–Sham band structure along standard high-symmetry paths for the rocksalt structure (e.g., Γ‑X‑W‑K‑Γ‑L).
- Determine the valence-band maximum (VBM) and conduction-band minimum (CBM) from the eigenvalues.
- The indirect gap is the smallest difference between VBM and CBM at different **k**‑points. The direct gap is the smallest difference at the same **k**‑point.

Assemble the results into a CSV file named `bulk_properties.csv` with one row per material and columns: `material`, `a0_angstrom`, `mu_muB`, `easy_axis`, `E_g_ind_eV`, `E_g_dir_eV`. The values must be the outcome of running the DFT workflow as described; they should reflect the expected physical trends for these materials.

## Assets

- DFT code with LDA+U+SOI capability (e.g., Quantum ESPRESSO, ABINIT, GPAW): https://www.quantum-espresso.org/
- PAW pseudopotentials for Mn, Fe, Co, Ni, O: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Bulk DFT calculations
- Role: process
- Action: Perform self-consistent DFT calculations for bulk MnO, FeO, CoO, and NiO in the rocksalt structure, strictly following the computational parameters specified above. For each material:
  - Relax the cubic lattice constant until the stress condition is met.
  - Compute total magnetic moments from spin-magnetization density integrated inside PAW spheres.
  - Determine the easy axis/plane by comparing total energies for different spin orientations as described.
  - Extract the Kohn-Sham band structure and determine the indirect and direct fundamental gaps.
- Evidence: none (intermediate artifacts can be stored at your discretion, but only the final CSV is scored)

### Step 2: Compile bulk properties table
- Role: scored
- Action: From the completed DFT calculations, extract for each material the quantities listed above and assemble them into a CSV file with one row per material.
- Output file: `/app/outputs/bulk_properties.csv`
- Format: csv
- Contract: material: string; a0_angstrom: float; mu_muB: float; easy_axis: string; E_g_ind_eV: float; E_g_dir_eV: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.csv
- path: `/app/outputs/bulk_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bulk structural, magnetic, and electronic properties of MnO, FeO, CoO, and NiO computed within LDA+U+SOI (U=4 eV) as reported in the paper's Table I. The hidden checker will compare each entry against the paper's reference values within appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `material`, `a0_angstrom`, `mu_muB`, `easy_axis`, `E_g_ind_eV`, `E_g_dir_eV`
  - `units`:
    - `a0_angstrom`: Å
    - `mu_muB`: μB
    - `easy_axis`: string (must follow the notation described above)
    - `E_g_ind_eV`: eV
    - `E_g_dir_eV`: eV

Notes: The task covers only the bulk reference DFT calculations. Surface slab relaxations, surface magnetic moments, electronic surface states, and SP-STM image simulations are excluded. Numerical differences due to different DFT implementations and pseudopotentials are expected and absorbed by the verification tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "a0_angstrom",
          "mu_muB",
          "easy_axis",
          "E_g_ind_eV",
          "E_g_dir_eV"
        ],
        "units": {
          "a0_angstrom": "Å",
          "mu_muB": "μB",
          "easy_axis": "string",
          "E_g_ind_eV": "eV",
          "E_g_dir_eV": "eV"
        }
      },
      "description": "Bulk structural, magnetic, and electronic properties of MnO, FeO, CoO, and NiO computed within LDA+U+SOI (U=4 eV) as reported in the paper's Table I. The hidden checker will compare each entry against the paper's reference values within appropriate tolerances."
    }
  ],
  "notes": "The task covers only the bulk reference DFT calculations. Surface slab relaxations, surface magnetic moments, electronic surface states, and SP-STM image simulations are excluded. Numerical differences due to different DFT implementations and pseudopotentials are expected and absorbed by the verification tolerances."
}
```

## How you are scored
A hidden verifier will read your submitted `bulk_properties.csv` and compare each property (one entry per material) against independently obtained reference values. The comparison uses numerical tolerances designed to absorb legitimate differences between DFT implementations and pseudopotentials while distinguishing physically correct results from guesses. The final reward is the fraction of property entries that fall within tolerance; achieving full credit therefore requires physically correct trends and magnitudes. Reporting numbers without actually performing the DFT calculations is unlikely to meet the verifier's tolerances.