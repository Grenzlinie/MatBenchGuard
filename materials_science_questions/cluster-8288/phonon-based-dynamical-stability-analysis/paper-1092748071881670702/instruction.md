# MXene Phase Stability from Bulk Coordination: TiC and MoC Reproduction

## Problem background
Two-dimensional transition metal carbides and nitrides, known as MXenes, exhibit a wide variety of structural phases whose stability is critical for their application in energy storage, catalysis, and electronics. The paper proposes that the phase stability of MXenes can be predicted from the coordination environments of their parent bulk phases: four bulk polymorphs (B1, HX1a, HX1b, HX2) characterized by distinct octahedral and prismatic coordination sequences may determine the relative stability of the derived MXene structures. This reproduction task investigates this hypothesis for two benchmark systems, TiC and MoC, by computing total energies of the bulk phases and their corresponding F-terminated M₂CT₂ MXenes, and evaluating the dynamical stability of the most stable MXene.

## Approach
Following the paper’s coordination-rule classification, the four bulk polymorphs (B1, HX1a, HX1b, HX2) and the four F-terminated M₂CT₂ MXene configurations (T-1, T-2, H-1, H-2) are considered for each of TiC and MoC. Total energies are computed using density functional theory (DFT) with the PBE-D2 functional and SSSP pseudopotentials, employing the open-source Quantum ESPRESSO package. The relative energetic stability ordering of the bulk phases is compared with that of the MXene structures to test whether the bulk ordering is preserved. For the most stable MXene per system (identified by the lowest total energy per atom), lattice-dynamical stability is assessed via density functional perturbation theory (DFPT) phonon calculations using Phonopy with a 3×3×1 supercell; imaginary phonon modes indicate dynamic instability.

## Reproduction target
Compute and rank the total energy per atom for the four bulk TiC and MoC polymorphs (B1, HX1a, HX1b, HX2) and for the four F-terminated M₂CT₂ MXene structures (T-1, T-2, H-1, H-2). Output the energy ordering as CSV files. For the most stable MXene of each system (lowest total energy per atom), perform a DFPT phonon calculation and report whether any imaginary phonon modes are present, yielding a dynamical stability verdict in a text file.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- SSSP Pseudopotentials (PBE PAW): https://www.materialscloud.org/discover/sssp/table/precision
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Generate crystal structures and QE inputs
- Role: process
- Action: Generate atomic coordinates for the four bulk TiC and MoC phases (B1, HX1a, HX1b, HX2) and the four F-terminated M2CT2 MXene structures (T-1, T-2, H-1, H-2) for TiC and MoC, following the coordination rules (octahedral vs prismatic) described in the approach. Write Quantum ESPRESSO input files for relaxation.
- Evidence: none

### Step 2: DFT relaxations of bulk phases
- Role: process
- Action: Using Quantum ESPRESSO pw.x with PBE-D2 functional and SSSP pseudopotentials, relax atomic positions and cell parameters of the four TiC and four MoC bulk phases. Ensure convergence in energy and forces.
- Evidence: none

### Step 3: Extract bulk energies
- Role: scored
- Action: From the relaxed bulk output, extract the total energy per atom for each phase and write a CSV.
- Output file: `/app/outputs/bulk_energies.csv`
- Format: csv
- Contract: Columns: system (str, 'TiC' or 'MoC'), phase (str, one of B1, HX1a, HX1b, HX2), total_energy_per_atom (float, eV/atom).
- Scoring: scored by hidden verifier

### Step 4: DFT relaxations of MXene phases
- Role: process
- Action: Using the same settings, relax the four Ti2CF2 and four Mo2CF2 MXene structures in a supercell with a vacuum region of at least 20 Å between periodic images.
- Evidence: none

### Step 5: Extract MXene energies
- Role: scored
- Action: From the relaxed MXene output, compute the total energy per atom for each structure and write a CSV.
- Output file: `/app/outputs/mxene_energies.csv`
- Format: csv
- Contract: Columns: system (str), mxene_label (str, one of T-1, T-2, H-1, H-2), total_energy_per_atom (float, eV/atom).
- Scoring: scored by hidden verifier

### Step 6: Phonon calculation on most stable MXene
- Role: process
- Action: For the most stable MXene per system (determined by the lowest total energy per atom from the previous step), perform a DFPT phonon calculation using Quantum ESPRESSO ph.x and Phonopy with a 3×3×1 supercell. Collect the phonon dispersion and vibrational DOS.
- Evidence: none

### Step 7: Check dynamical stability
- Role: scored (load-bearing)
- Action: Analyze the computed phonon dispersion: if any mode has a negative squared frequency (imaginary) beyond a small tolerance, flag as 'Yes' for imaginary frequency; otherwise 'No'. Write the conclusion for each system.
- Output file: `/app/outputs/phonon_results.txt`
- Format: txt
- Contract: Two lines, each formatted as '{system} {mxene_label}: {Yes/No}, {conclusion}', e.g., 'TiC T-1: No, dynamically stable'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_energies.csv`
- `/app/outputs/mxene_energies.csv`
- `/app/outputs/phonon_results.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_energies.csv
- path: `/app/outputs/bulk_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed total energy per atom for each TiC and MoC bulk polymorph.
- schema:
  - `type`: table
  - `required_columns`: `system`, `phase`, `total_energy_per_atom`
  - `units`:
    - `total_energy_per_atom`: eV/atom

### mxene_energies.csv
- path: `/app/outputs/mxene_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed total energy per atom for each F-terminated M2CT2 MXene.
- schema:
  - `type`: table
  - `required_columns`: `system`, `mxene_label`, `total_energy_per_atom`
  - `units`:
    - `total_energy_per_atom`: eV/atom

### phonon_results.txt
- path: `/app/outputs/phonon_results.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Dynamical stability verdict: for each system, the most stable MXene label and whether imaginary phonon modes were found.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object

Notes: The structural audit will check that the energy ordering of bulk phases and MXene phases matches the paper's reported stability order, and that the phonon analysis finds no imaginary modes for the most stable MXene. No absolute energy values or tolerances are given in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "phase",
          "total_energy_per_atom"
        ],
        "units": {
          "total_energy_per_atom": "eV/atom"
        }
      },
      "description": "Computed total energy per atom for each TiC and MoC bulk polymorph."
    },
    {
      "file": "mxene_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "mxene_label",
          "total_energy_per_atom"
        ],
        "units": {
          "total_energy_per_atom": "eV/atom"
        }
      },
      "description": "Computed total energy per atom for each F-terminated M2CT2 MXene."
    },
    {
      "file": "phonon_results.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {},
        "items": {}
      },
      "description": "Dynamical stability verdict: for each system, the most stable MXene label and whether imaginary phonon modes were found."
    }
  ],
  "notes": "The structural audit will check that the energy ordering of bulk phases and MXene phases matches the paper's reported stability order, and that the phonon analysis finds no imaginary modes for the most stable MXene. No absolute energy values or tolerances are given in the public contract."
}
```

## How you are scored
A hidden verifier inspects each scored artifact. For the bulk and MXene energy CSV files, it checks whether the total-energy-per-atom ordering across the structures matches the expected stability trend derived from the parent bulk coordination rules. For the phonon results text file, it verifies that the most stable MXene for each system is correctly identified and that the dynamical stability flag (imaginary frequencies present or not) is consistent with the computed phonon dispersion. The final reward is a weighted combination of the correctness of these structural trends; exact numerical agreement with a single paper-reported value is not required.
