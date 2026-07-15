# DFT Electronic Structure of Orthorhombic CH3NH3PbI3 with Three Functionals

## Problem background
The organic-inorganic hybrid perovskite CH3NH3PbI3 is a promising light-absorbing material that can dramatically improve the efficiency of dye-sensitized solar cells. To guide materials design, it is essential to accurately determine its structural and electronic properties from first principles. Standard density-functional approximations, however, may not reliably capture the weak van der Waals interactions that are important in such hybrid systems. This task investigates how three exchange-correlation functionals — a local (LDA), a semi-local (GGA), and a non-local van der Waals functional — predict the lattice constants, band gap, density of states, and bonding character of the orthorhombic phase of CH3NH3PbI3.

## Approach
The conceptual approach is to perform first-principles DFT calculations for orthorhombic CH3NH3PbI3 using an open-source plane-wave code with PAW pseudopotentials. Starting from the experimentally determined crystal structure, full structural optimization (cell shape and atomic positions) is carried out with three functionals: PZ81 (LDA), PBE (GGA), and optB86b+vdWDF (a non-local van der Waals functional). The resulting lattice constants are compared to available experimental data to assess which functional gives the most faithful structure. Using the relaxed cells, static electronic structure calculations are performed to obtain the Kohn-Sham band gap, total and partial density of states, and the band structure along high-symmetry lines. Bader charge analysis is then applied to the pseudo-valence charge density to examine ionic and covalent bonding character. The comparison reveals the role of van der Waals interactions and the chemical inequivalence of the two crystallographically distinct iodine sites.

## Reproduction target
Produce the following six artifacts for the orthorhombic CH3NH3PbI3 crystal starting from the experimental structure (Baikie et al., 2013):

1. **Optimized lattice constants and volumes** – after full cell-and-atom relaxation with PZ81, PBE, and optB86b+vdWDF.
2. **Band gap energies** – the Kohn-Sham gap (in eV) for each functional.
3. **Total density of states (TDOS)** – for the optB86b+vdWDF functional, as a two-column (energy, TDOS) text file.
4. **Partial density of states (PDOS)** – atom- and orbital-resolved (Pb, I1, I2, C, N, H; s and p contributions) for the optB86b+vdWDF functional.
5. **Band structure** – eigenvalues along the standard high-symmetry path of the orthorhombic Brillouin zone for the optB86b+vdWDF functional.
6. **Bader atomic charges** – for Pb, I1, I2, N, C, and the fragment charges for PbI3, CH3, and NH3, for all three functionals.

Write each artifact to the exact file and format specified in the workflow steps. The hidden checker will verify structural trends among the functionals, recompute the band gap from the TDOS, audit the band structure for a direct gap at the Γ point, and compare Bader charges against reference data.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- libvdwxc library (needed for optB86b+vdWDF): https://github.com/libvdwxc/libvdwxc
- PAW pseudopotentials (PSlibrary or equivalent): https://www.quantum-espresso.org/pseudopotentials
- Experimental orthorhombic CH3NH3PbI3 crystal structure (CIF): 10.1039/C3TA10518A
- Bader charge analysis code (Henkelman group): https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Structural optimization and lattice constants
- Role: scored
- Action: Starting from the experimental CIF of orthorhombic CH3NH3PbI3 (Baikie et al. 2013), perform DFT structural cell‑and‑atom relaxation using PZ81 (LDA), PBE (GGA), and optB86b+vdWDF functionals. For each functional, extract the fully relaxed lattice constants a, b, c (Å) and unit cell volume (Å³). Write the results to step_01_optimized_lattice.csv.
- Output file: `/app/outputs/step_01_optimized_lattice.csv`
- Format: csv
- Contract: functional(string), a_A(float), b_A(float), c_A(float), volume_A3(float)
- Scoring: scored by hidden verifier

### Step 2: Band gap calculation
- Role: scored
- Action: Using the relaxed structures from step_01, perform static electronic‑structure calculations (with a dense k‑point mesh) for each of the three functionals. Determine the Kohn‑Sham band gap (eV) for each functional. Write the values to step_02_band_gap.csv.
- Output file: `/app/outputs/step_02_band_gap.csv`
- Format: csv
- Contract: functional(string), band_gap_eV(float)
- Scoring: scored by hidden verifier

### Step 3: Total density of states (TDOS) for optB86b+vdWDF
- Role: scored
- Action: For the structure relaxed with optB86b+vdWDF, compute the total density of states (TDOS) on a fine energy grid. Write a two‑column whitespace‑separated text file with energy (eV) in the first column and total DOS in the second. The checker will recompute the band gap from this data.
- Output file: `/app/outputs/step_03_total_dos_optB86b.dat`
- Format: txt
- Contract: Two-column whitespace-separated: energy_eV(float)  total_dos(float)
- Scoring: scored by hidden verifier

### Step 4: Partial density of states (PDOS) for optB86b+vdWDF
- Role: scored
- Action: For the optB86b+vdWDF relaxed structure, compute atom‑ and orbital‑projected density of states (PDOS) for Pb, I1, I2, C, N, and H atoms, resolving s and p contributions. Write a CSV with columns atom, orbital, energy (eV), and PDOS.
- Output file: `/app/outputs/step_04_partial_dos_optB86b.csv`
- Format: csv
- Contract: atom(string), orbital(string), energy_eV(float), pdos(float)
- Scoring: scored by hidden verifier

### Step 5: Band structure for optB86b+vdWDF
- Role: scored (load-bearing)
- Action: For the optB86b+vdWDF relaxed structure, calculate the electronic band structure along the standard high‑symmetry path of the orthorhombic Brillouin zone. Output a CSV where the first four columns are k‑point index and fractional coordinates (kx, ky, kz), followed by eigenenergy columns (one per band).
- Output file: `/app/outputs/step_05_band_structure_optB86b.csv`
- Format: csv
- Contract: kpoint_index(int), kx(float), ky(float), kz(float), band_1_eV(float), band_2_eV(float), ... (one column per band)
- Scoring: scored by hidden verifier

### Step 6: Bader charge analysis
- Role: scored
- Action: For each of the three relaxed structures (PZ81, PBE, optB86b+vdWDF), run Bader charge analysis on the pseudo‑valence charge density. Compute atomic charges for Pb, I1, I2, N, C and the fragment charges for PbI3, CH3, and NH3. Write a CSV with columns functional, atom_type, and charge (e).
- Output file: `/app/outputs/step_06_bader_charges.csv`
- Format: csv
- Contract: functional(string), atom_type(string), charge_e(float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_optimized_lattice.csv`
- `/app/outputs/step_02_band_gap.csv`
- `/app/outputs/step_03_total_dos_optB86b.dat`
- `/app/outputs/step_04_partial_dos_optB86b.csv`
- `/app/outputs/step_05_band_structure_optB86b.csv`
- `/app/outputs/step_06_bader_charges.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_optimized_lattice.csv
- path: `/app/outputs/step_01_optimized_lattice.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constants and volume for each functional, compared to the paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `a_A`, `b_A`, `c_A`, `volume_A3`
  - `units`:
    - `a_A`: Å
    - `b_A`: Å
    - `c_A`: Å
    - `volume_A3`: Å³

### step_02_band_gap.csv
- path: `/app/outputs/step_02_band_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Theoretical band gap energies for three functionals, compared to the paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

### step_03_total_dos_optB86b.dat
- path: `/app/outputs/step_03_total_dos_optB86b.dat`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Total DOS; the checker recomputes the band gap by finding the HOMO‑LUMO separation and scores a directional band‑gap error.
- schema:
  - `type`: text
  - `required`:
    - `column_1`: energy_eV (float)
    - `column_2`: total_dos (float)

### step_04_partial_dos_optB86b.csv
- path: `/app/outputs/step_04_partial_dos_optB86b.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Partial DOS; structural audit confirms distinct I1 and I2 PDOS curves and that I2 peaks lie closer to the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `orbital`, `energy_eV`, `pdos`
  - `units`:
    - `energy_eV`: eV
    - `pdos`: arb. units

### step_05_band_structure_optB86b.csv
- path: `/app/outputs/step_05_band_structure_optB86b.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band structure; the checker verifies a direct band gap at the Γ point by examining eigenenergy differences.
- schema:
  - `type`: table
  - `required_columns`: `kpoint_index`, `kx`, `ky`, `kz`
  - `items`:
    - `band_*_eV`: float

### step_06_bader_charges.csv
- path: `/app/outputs/step_06_bader_charges.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bader atomic charges; compared to the paper‑reported values for each functional and atom/fragment.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `atom_type`, `charge_e`
  - `units`:
    - `charge_e`: elementary charge

Notes: The checker recomputes the band gap from step_03 and verifies the structural properties of PDOS and band structure. Lattice constants, volumes, band gaps, and Bader charges are compared to the paper‑reported values with hidden tolerances. The load‑bearing step_05 forces the agent to actually run the DFT pipeline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_optimized_lattice.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "a_A",
          "b_A",
          "c_A",
          "volume_A3"
        ],
        "units": {
          "a_A": "Å",
          "b_A": "Å",
          "c_A": "Å",
          "volume_A3": "Å³"
        }
      },
      "description": "Optimized lattice constants and volume for each functional, compared to the paper‑reported values."
    },
    {
      "file": "step_02_band_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Theoretical band gap energies for three functionals, compared to the paper‑reported values."
    },
    {
      "file": "step_03_total_dos_optB86b.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "required": {
          "column_1": "energy_eV (float)",
          "column_2": "total_dos (float)"
        }
      },
      "description": "Total DOS; the checker recomputes the band gap by finding the HOMO‑LUMO separation and scores a directional band‑gap error."
    },
    {
      "file": "step_04_partial_dos_optB86b.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom",
          "orbital",
          "energy_eV",
          "pdos"
        ],
        "units": {
          "energy_eV": "eV",
          "pdos": "arb. units"
        }
      },
      "description": "Partial DOS; structural audit confirms distinct I1 and I2 PDOS curves and that I2 peaks lie closer to the Fermi level."
    },
    {
      "file": "step_05_band_structure_optB86b.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kpoint_index",
          "kx",
          "ky",
          "kz"
        ],
        "items": {
          "band_*_eV": "float"
        }
      },
      "description": "Band structure; the checker verifies a direct band gap at the Γ point by examining eigenenergy differences."
    },
    {
      "file": "step_06_bader_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "atom_type",
          "charge_e"
        ],
        "units": {
          "charge_e": "elementary charge"
        }
      },
      "description": "Bader atomic charges; compared to the paper‑reported values for each functional and atom/fragment."
    }
  ],
  "notes": "The checker recomputes the band gap from step_03 and verifies the structural properties of PDOS and band structure. Lattice constants, volumes, band gaps, and Bader charges are compared to the paper‑reported values with hidden tolerances. The load‑bearing step_05 forces the agent to actually run the DFT pipeline."
}
```

## How you are scored
Each of the six output files is evaluated by an automated, hidden verifier. The verifier independently recomputes quantities where possible (e.g., the band gap from the total density of states) and compares your reported results against reference criteria. For structural artifacts, it checks expected relationships such as the ordering of lattice constants across functionals and the character of the electronic states. Your total reward is a weighted sum of the per-step scores; the largest weights go to the steps that capture the main findings of the study. The checker uses internal thresholds that reflect the expected variation between different DFT implementations; you are not required to guess them. Run the DFT pipeline faithfully using the described functionals and pseudopotentials, and report the outcomes as instructed. Honest, well-executed calculations that capture the physical trends will score highly.
