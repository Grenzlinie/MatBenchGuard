# Point defect formation and electronic structure from DFT

## Problem background
Monolayer MoS2 is a two-dimensional semiconductor with potential for nanoelectronics. Its electronic properties are strongly influenced by the surrounding dielectric environment. This task investigates, via density functional theory (DFT), how oxygen vacancies in the high-k dielectric HfO2 affect the electronic structure of a MoS2–HfO2 interface. The key question is whether such vacancies introduce defect states within the band gap of MoS2 and shift the Fermi level, leading to doping-like behavior. By computing the atom-projected density of states for the defective system, the presence and nature of any defect states can be determined.

## Approach
The workflow uses plane-wave DFT with the LDA exchange-correlation functional and the Grimme DFT-D2 van der Waals correction, as implemented in Quantum ESPRESSO. Standard pseudopotentials from the SSSP efficiency library are employed. First, the equilibrium in‑plane lattice constant of an isolated monolayer MoS2 is determined. Then a periodic supercell is built consisting of the MoS2 monolayer on an oxygen‑terminated, hydrogen‑passivated monoclinic HfO2 slab of about 2 nm thickness, with in‑plane dimensions chosen to limit strain. The ideal (defect‑free) interface is relaxed, allowing the MoS2 layer and the upper half of the oxide slab to move until forces converge. Subsequently, a single oxygen atom is removed from the topmost oxygen layer of the slab, creating a periodic oxygen vacancy with a density of approximately 1.97 × 10^14 cm⁻². This defective structure is relaxed again under the same settings. Finally, a self‑consistent calculation is performed, and the total and atom‑projected density of states (per element: total, Mo, S, Hf, O) is computed with the energy axis referenced to the Fermi level. The resulting DOS is saved in a CSV file for analysis.

## Reproduction target
Compute the atom-projected density of states for the relaxed MoS2–HfO2 heterostructure containing an oxygen vacancy in the topmost oxide layer. The output must be a CSV file with energy (eV relative to the Fermi level) and per‑element DOS columns (total, Mo, S, Hf, O) on a fine energy grid covering the region of the MoS2 band gap. This file is the sole scored artifact. From it, the checker will identify whether occupied defect states appear within the MoS2 gap and assess the alignment of the Fermi level with respect to the MoS2 band edges, thereby evaluating the doping character of the defective interface.

## Assets

- Quantum ESPRESSO (DFT code, LDA functional, DFT-D2 vdW correction): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of bulk MoS2: Crystallography Open Database COD ID 1000014 or ICSD 42542
- Crystal structure of bulk monoclinic HfO2: ICSD 63861 or equivalent monoclinic HfO2 structure (P2_1/c)
- Standard DFT parameters (cutoff, k-mesh, force convergence)

## Workflow steps

### Step 1: MoS2 lattice constant relaxation
- Role: process
- Action: Perform volume relaxation of an isolated monolayer MoS2 unit cell using LDA-DFT to obtain the equilibrium in-plane lattice constant. This value will be used to construct the heterostructure supercell.
- Evidence: `/app/outputs/mos2_lattice.txt`

### Step 2: Construction of MoS2-HfO2 heterostructure supercell
- Role: process
- Action: Build a periodic supercell consisting of an approximately 2 nm thick HfO2 slab terminated with oxygen (top O layer passivated by hydrogen) and a monolayer MoS2 layer, using the relaxed MoS2 lattice constant. Use the rectangular in-plane dimensions a=9.366 Å, b=5.407 Å. The lower half of the oxide atoms should be fixed during later relaxations.
- Evidence: `/app/outputs/supercell_structure.xyz`

### Step 3: DFT relaxation of the ideal (defect-free) interface
- Role: process
- Action: Relax the ideal MoS2-HfO2 heterostructure (no defects) using LDA exchange-correlation with DFT-D2 van der Waals correction. Allow all MoS2 atoms and the top half of the oxide layers to move until forces are below 0.02 eV/Å. This provides a relaxed reference geometry and starting point for the vacancy calculation.
- Evidence: `/app/outputs/ideal_relaxed.xyz`

### Step 4: Introduce O vacancy and relax defective system
- Role: process
- Action: Starting from the relaxed ideal interface, remove a single oxygen atom from the topmost (MoS2-adjacent) O layer of the HfO2 slab, creating a periodic O vacancy with density ~1.97×10^14 cm^-2. Relax the defective system again using the same LDA+vdW settings and convergence criteria.
- Evidence: `/app/outputs/defective_relaxed.xyz`

### Step 5: Compute density of states for the defective system
- Role: scored (load-bearing)
- Action: Using the relaxed defective structure, perform a self-consistent DFT calculation and then compute the total and atom-projected density of states (per element: total, Mo, S, Hf, O). Output the DOS as a CSV file with energy relative to the Fermi level (EF=0 eV). The energy grid should be dense enough to resolve defect states (step ≤ 0.01 eV) and cover the MoS2 band gap and defect region (e.g., -4 to +4 eV).
- Output file: `/app/outputs/density_of_states.csv`
- Format: csv
- Contract: CSV with columns: energy (eV, float, relative to EF=0), total_DOS (float, states/eV), Mo_DOS (float), S_DOS (float), Hf_DOS (float), O_DOS (float). Energy grid step ≤ 0.01 eV, covering at least -4 to +4 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/density_of_states.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### density_of_states.csv
- path: `/app/outputs/density_of_states.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Atom-projected density of states for the defective MoS2-HfO2 system with an O vacancy. The checker will locate the MoS2 band gap from total_DOS, verify the presence of an occupied Hf-derived state within the gap, and confirm that the Fermi level (0 eV) is at or above the conduction band minimum (n-type pinning).
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_DOS`, `Mo_DOS`, `S_DOS`, `Hf_DOS`, `O_DOS`
  - `units`:
    - `energy`: eV relative to EF

Notes: The checker will recompute the VBM and CBM from the total_DOS, then check for a peak in Hf_DOS (and total_DOS) at energy <0 eV within the gap, and assess Fermi level alignment. Structural features are scored with tolerance ±0.2 eV for the defect peak position to allow for method differences. No absolute energy values are required to match the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "density_of_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_DOS",
          "Mo_DOS",
          "S_DOS",
          "Hf_DOS",
          "O_DOS"
        ],
        "units": {
          "energy": "eV relative to EF"
        }
      },
      "description": "Atom-projected density of states for the defective MoS2-HfO2 system with an O vacancy. The checker will locate the MoS2 band gap from total_DOS, verify the presence of an occupied Hf-derived state within the gap, and confirm that the Fermi level (0 eV) is at or above the conduction band minimum (n-type pinning)."
    }
  ],
  "notes": "The checker will recompute the VBM and CBM from the total_DOS, then check for a peak in Hf_DOS (and total_DOS) at energy <0 eV within the gap, and assess Fermi level alignment. Structural features are scored with tolerance ±0.2 eV for the defect peak position to allow for method differences. No absolute energy values are required to match the paper."
}
```

## How you are scored
A hidden verifier inspects only the artifacts you write under /app/outputs. It does not re‑run your calculations. Each scored workflow step is evaluated independently from the corresponding output file, and the final reward is a weighted sum of the per‑step rewards (values between 0 and 1). For this task, the sole scored artifact is the density_of_states.csv. The verifier checks the CSV format and then examines the density of states for structural features related to the Fermi‑level position and the occupation of any defect states inside the MoS2 band gap. Because different DFT implementations or pseudopotentials can shift absolute energies, the verifier uses tolerances and looks for qualitative signatures rather than exact numerical agreement with a reference. As long as the key structural signatures are present, your solution can earn full credit even if the precise numerical values differ from those reported in the original study. You do not need to attempt to match any specific number; faithfully execute the workflow steps and output the required CSV file.
