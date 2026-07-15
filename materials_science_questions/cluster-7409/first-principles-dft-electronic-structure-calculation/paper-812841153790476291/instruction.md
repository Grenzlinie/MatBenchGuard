# Multilevel DFT optimization of an edge dislocation core in rutile TiO2

## Problem background
Dislocations in rutile TiO₂ are known to influence mechanical strength, electrical conductivity, and photocatalytic activity. Understanding their atomic-scale structure and electronic behaviour is essential for engineering oxide-based devices, but the complexity of the material — variable stoichiometry, mixed ionic-covalent bonding, and large configuration space — makes experimental determination and theoretical modelling particularly challenging. A multilevel computational strategy, combining a second-moment tight-binding potential (SMTBQ) global optimization with density functional theory (DFT) screening and DFT+U refinement, has been proposed to tackle this problem. The present reproduction task targets the b=c[001] edge dislocation. It aims to identify the most stable atomic configurations of this dislocation as a function of oxygen chemical potential and to characterize their electronic properties, specifically the presence or absence of localized electronic states within the band gap that could act as charge traps.

## Approach
The core of the experiment is a hierarchical computational pipeline. First, a slab supercell containing a single edge dislocation is built using lattice parameters from the SMTBQ model. Global optimization is then performed using the EON software together with the SMTBQ potential to generate candidate dislocation core structures for two compositions: stoichiometric (Ti₂₃₀O₄₆₀) and oxygen-deficient (Ti₂₃₁O₄₆₁). The most promising configurations from this classical-potential stage are further relaxed and screened with spin-polarized density functional theory (PBE functional, minimal k‑point sampling). The lowest‑energy candidate from each composition is then refined with DFT+U to obtain the final defect geometry. From these refined structures, the dislocation formation energy is computed as a function of oxygen chemical potential, and the electronic density of states projected onto different spatial regions (bulk‑like vs. dislocation core) is analysed. This multilevel approach balances the need to sample a vast configuration space with the accuracy required to capture electron localisation effects near the defect.

## Reproduction target
The aim is to produce three concrete artifacts from the full computational workflow. The first artifact is a file containing the DFT+U-optimized atomic coordinates for both the stoichiometric (Ti₂₃₀O₄₆₀) and oxygen‑deficient (Ti₂₃₁O₄₆₁) dislocation cores. The second artifact is a table of dislocation formation energies per unit length for both compositions at six values of the oxygen chemical potential (μ_O − 0.5·E(O₂) = 0.0, −1.0, −2.0, −3.0, −4.0, −5.0 eV). From this table one should observe whether the stoichiometric core is more stable when oxygen is abundant and whether the oxygen‑deficient core becomes preferred under reducing conditions. The third artifact is a projected density of states (PDOS) separated into bulk‑like regions and the dislocation core region; the PDOS allows one to determine if the oxygen‑deficient core introduces occupied electronic states in the band gap close to the valence band maximum. Completing the full pipeline, not merely reporting numbers, is required.

## Assets

- EON software for atomic scale simulations: https://theory.cm.utexas.edu/eon/
- SMTBQ potential parameters for rutile TiO2: 10.1021/acs.jpcc.5b01631
- Open-source DFT code with PBE+U (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org

## Workflow steps

### Step 1: Bulk reference DFT+U calculations
- Role: process
- Action: Perform spin-polarized DFT+U calculations for bulk rutile TiO2 and an isolated oxygen molecule to obtain equilibrium lattice constants and total energies per formula unit E(TiO2) and E(O2). These reference values are used later to scale supercells and compute formation energies.
- Evidence: `/app/outputs/bulk_reference_energies.json`

### Step 2: Supercell construction with edge dislocation
- Role: process
- Action: Construct a slab supercell (~689-694 atoms) of rutile TiO2 containing an isolated edge dislocation with Burgers vector b=c[001]. The slab is periodic in y=[1-10] and z=[001] and has free surfaces in x=[110]. Use the SMTBQ lattice constants for the initial geometry. Arrange 11 and 12 unit-cell layers on either side of the dislocation core to produce balanced strain. Save the initial atomic structure as evidence.
- Evidence: `/app/outputs/initial_supercell.xyz`

### Step 3: SMTBQ global optimization and screening
- Role: process
- Action: Run global optimization using the SMTBQ potential implemented in EON. For two compositions — Ti230O460 (stoichiometric) and Ti231O461 (oxygen-deficient) — perform at least 100 saddle-point searches per composition. Starting from a suitable initial configuration, displace atoms near the core randomly, use minimum-mode following to find saddle points, relax into new minima, and collect distinct configurations. For each composition, select configurations within 5 eV of the lowest energy, relax them with charge equilibration, then retain those within 1 eV of the lowest relaxed energy. Write the retained configurations with their SMTBQ energies to step_01_smtbq_configurations.csv.
- Evidence: `/app/outputs/step_01_smtbq_configurations.csv`

### Step 4: DFT-1 pre-screening
- Role: process
- Action: For every configuration retained from the SMTBQ stage, carry out spin-polarized DFT calculations using the PBE functional, a plane-wave cutoff of 300 eV, and Gamma-point only. Relax atomic positions until forces are below 0.1 eV/Å while keeping cell dimensions fixed. Record the total energy for each configuration and write the results (composition, configuration ID, DFT-1 total energy) to step_02_dft1_energies.csv. Select the lowest-energy structure for each composition for DFT-2 refinement.
- Evidence: `/app/outputs/step_02_dft1_energies.csv`

### Step 5: DFT-2 refinement and final structure
- Role: scored (load-bearing)
- Action: For the lowest-energy structure of each composition from DFT-1, perform DFT+U refinement with U_Ti=4.2 eV, a plane-wave cutoff of 350 eV, and k-point mesh 1×1×3. Scale the supercell dimensions to the bulk DFT+U lattice constants before relaxation. Optimize all atomic positions until forces are <0.1 eV/Å. Write the final relaxed atomic coordinates for both structures into an XYZ file, with each structure as a separate frame containing the lattice vectors in the comment line.
- Output file: `/app/outputs/step_03_dft2_structure.xyz`
- Format: other
- Contract: XYZ format; comment line (line 2) contains lattice vectors, e.g. 'Lattice="Ax Ay Az; Bx By Bz; Cx Cz"'. Atomic lines: element x y z (in Angstrom). Two frames, one per composition.
- Scoring: scored by hidden verifier

### Step 6: Formation energy analysis
- Role: scored
- Action: Using the DFT+U total energies from the final structures and the bulk reference energies (E(TiO2) and E(O2)), compute the dislocation formation energy per unit length for both compositions as a function of oxygen chemical potential following the method of expression (1) in the paper. Evaluate at oxygen chemical potentials relative to 0.5*E(O2): -5.0, -4.0, -3.0, -2.0, -1.0, 0.0 eV. Write the results to step_03_formation_energy.csv.
- Output file: `/app/outputs/step_03_formation_energy.csv`
- Format: csv
- Contract: CSV with columns: composition (string, e.g. 'Ti230O460'), oxygen_chemical_potential(eV) (numeric, relative to 0.5*E(O2)), formation_energy(eV/Ang) (numeric). Six rows per composition.
- Scoring: scored by hidden verifier

### Step 7: Projected density of states
- Role: scored
- Action: From the DFT+U calculation for both dislocation structures, compute the projected electronic density of states (PDOS) using Gaussian smearing. Separate atoms into bulk-like regions B1, B2 and the dislocation core region D as defined in the published procedure. Output a DAT file with four columns: energy (eV relative to Fermi), total_DOS, PDOS_B1, PDOS_B2, PDOS_D. Include both structures in the same file, separated by comment lines indicating the composition.
- Output file: `/app/outputs/step_03_dft2_dos.dat`
- Format: txt
- Contract: Four columns: energy(eV) relative to Fermi, total_DOS (states/eV/cell), PDOS_B1, PDOS_B2, PDOS_D. Sections for each composition are separated by a comment line '#' with the composition label.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_dft2_structure.xyz`
- `/app/outputs/step_03_formation_energy.csv`
- `/app/outputs/step_03_dft2_dos.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_dft2_structure.xyz
- path: `/app/outputs/step_03_dft2_structure.xyz`
- format: other
- purpose: scored
- target_policy: reference_match
- description: Final optimized atomic structures of the stoichiometric and oxygen-deficient dislocation cores; the checker compares core-atom RMSD against hidden references.
- schema:
  - `type`: other
  - `description`: XYZ file with two frames containing the DFT+U optimized atomic coordinates. Each frame's second line is a comment with the lattice vectors in the format 'Lattice="Ax Ay Az; Bx By Bz; Cx Cz"'.

### step_03_formation_energy.csv
- path: `/app/outputs/step_03_formation_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dislocation formation energy per unit length for both compositions at six oxygen chemical potentials; the checker validates ordering and numerical agreement with hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `oxygen_chemical_potential`, `formation_energy`
  - `units`:
    - `oxygen_chemical_potential`: eV
    - `formation_energy`: eV/Å

### step_03_dft2_dos.dat
- path: `/app/outputs/step_03_dft2_dos.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Projected density of states for bulk-like and dislocation core regions; the checker verifies the presence of occupied Ti3+ gap states near the valence band maximum for the oxygen-deficient core.
- schema:
  - `type`: text
  - `columns`: `energy`, `total_DOS`, `PDOS_B1`, `PDOS_B2`, `PDOS_D`
  - `units`:
    - `energy`: eV
    - `DOS`: states/eV/cell

Notes: The XYZ structure file is load-bearing to prevent bypass of the SMTBQ/DFT workflow. All values in formation_energy.csv and dos.dat must be self-consistently derived from the same underlying DFT+U calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_dft2_structure.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "other",
        "description": "XYZ file with two frames containing the DFT+U optimized atomic coordinates. Each frame's second line is a comment with the lattice vectors in the format 'Lattice=\"Ax Ay Az; Bx By Bz; Cx Cz\"'."
      },
      "description": "Final optimized atomic structures of the stoichiometric and oxygen-deficient dislocation cores; the checker compares core-atom RMSD against hidden references."
    },
    {
      "file": "step_03_formation_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "oxygen_chemical_potential",
          "formation_energy"
        ],
        "units": {
          "oxygen_chemical_potential": "eV",
          "formation_energy": "eV/Å"
        }
      },
      "description": "Dislocation formation energy per unit length for both compositions at six oxygen chemical potentials; the checker validates ordering and numerical agreement with hidden reference values."
    },
    {
      "file": "step_03_dft2_dos.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "columns": [
          "energy",
          "total_DOS",
          "PDOS_B1",
          "PDOS_B2",
          "PDOS_D"
        ],
        "units": {
          "energy": "eV",
          "DOS": "states/eV/cell"
        }
      },
      "description": "Projected density of states for bulk-like and dislocation core regions; the checker verifies the presence of occupied Ti3+ gap states near the valence band maximum for the oxygen-deficient core."
    }
  ],
  "notes": "The XYZ structure file is load-bearing to prevent bypass of the SMTBQ/DFT workflow. All values in formation_energy.csv and dos.dat must be self-consistently derived from the same underlying DFT+U calculations."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier that inspects each of the three scored output files. For the atomic structure, the verifier compares the core‑atom positions against a reference structure (RMSD threshold) to assess the geometric accuracy. For the formation energy, it checks that the relative ordering of the two compositions is correct at the extremes of the oxygen chemical potential and compares your reported formation energy values against hidden reference figures within allowed tolerances. For the density of states, the verifier analyses the PDOS data to confirm that the oxygen‑deficient core exhibits the expected qualitative feature (occupied states in the gap near the valence band maximum). The three individual scores are combined into a single reward value between 0.0 and 1.0, with the structure and formation energy receiving the greatest weight. A reproduction that merely quotes the target values without running the workflow will not meet the tolerances and will score poorly.
