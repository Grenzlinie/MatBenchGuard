# Defect migration energy barrier calculation

## Problem background
Vacancy-mediated diffusion is central to many kinetic processes in alloys, including radiation damage evolution and high-temperature stability. The mobility of vacancies is governed by the migration energy barrier that an atom must overcome to jump into a neighboring vacant site. Understanding how different alloying elements affect this barrier is key to designing materials with tailored diffusion behavior. In this task, we investigate the effect of manganese (Mn) addition on vacancy migration barriers in Ni-based concentrated solid-solution alloys and across several pure metals. The required computation will quantify how the presence of Mn changes the average energy barrier relative to reference systems where Mn is absent.

## Approach
We use first-principles density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and projector-augmented wave (PAW) pseudopotentials. The vacancy migration path and its energy barrier are obtained with the climbing-image nudged elastic band (CI-NEB) method, which identifies the minimum-energy path between an initial state (atom at its lattice site with a neighboring vacancy) and a final state (atom moved into that vacancy).

For the Ni–Co–X alloys (X = Co, Fe, Mn) we construct large supercells (120 atoms) that approximate a random solid solution, using either the Similar Atomic Environment (SAE) method or Special Quasirandom Structures (SQS). For each alloy we introduce a vacancy and compute the migration barrier for several nearest-neighbor Ni and Co atoms exchanging with that vacancy.

To test the generality of the Mn effect, we select at least three pure metals from a set that includes Cu, Fe, V, Ti, Cr, Zn, Al, Ta, and W, and build supercells for both the pure metal and the binary alloy with 20 at.% Mn (e.g., pure Cu and Cu₀.₈Mn₀.₂). For Fe-based systems, strong electron correlations are accounted for by using DFT+U with an effective Hubbard Ueff = 2 eV. For each system we compute migration barriers for at least two host-atom diffusion paths.

The comparison of the computed average barriers between Mn-containing and non-Mn systems constitutes the main reproduction target.

## Reproduction target
Compute the vacancy migration barriers for nearest-neighbor atoms in Ni₀.₆Co₀.₂X₀.₂ (X = Co, Fe, Mn) alloys and for at least three pure-metal vs. 80/20 metal–Mn binary alloy systems. The verifier will evaluate the results using a predefined structural criterion.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials (PSLibrary / SSSP): https://www.quantum-espresso.org/pseudopotentials
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Generate supercell structures
- Role: process
- Action: For each alloy composition Ni0.6Co0.2X0.2 (X=Co, Fe, Mn), generate a 120-atom FCC supercell that approximates the atomic distribution of a random solid solution (use SAE or SQS). For the universality test, generate supercells for at least three pure metals (select from Cu, Fe, V, Ti, Cr, Zn, Al, Ta, W) and for the corresponding binary alloys with 20 at.% Mn, employing the appropriate Bravais lattice (FCC/BCC/HCP) and supercell sizes (typically 64–120 atoms).
- Evidence: `/app/outputs/supercell_structures.json`

### Step 2: Create vacancy end-point configurations
- Role: process
- Action: For each supercell, remove an atom to introduce a vacancy. Identify the nearest-neighbor (1nn) atoms. For each chosen diffusing atom (for NiCoX systems: at least two 1nn Ni and two 1nn Co paths; for universality systems: at least two paths of the host metal type), construct the initial (atom in original site, vacancy present) and final (atom moved into vacancy) images as end-points for CI-NEB.
- Evidence: `/app/outputs/endpoint_configurations.json`

### Step 3: Compute migration barriers for NiCoX alloys
- Role: scored (load-bearing)
- Action: Using DFT (Quantum ESPRESSO with PAW-PBE pseudopotentials) and the climbing-image nudged elastic band (CI-NEB) method with three intermediate images, calculate the minimum-energy path and migration barrier (Ed = E_saddle − E_initial) for each diffusion path in the Ni0.6Co0.2X0.2 (X=Co, Fe, Mn) alloys. Output results in a CSV file with one row per path.
- Output file: `/app/outputs/migration_barriers_NiCoX.csv`
- Format: csv
- Contract: CSV with header: alloy,atom_type,migration_barrier_eV. alloy: string (e.g., 'Ni0.6Co0.2Mn0.2'); atom_type: string, 'Ni' or 'Co'; migration_barrier_eV: float. One row per path.
- Scoring: scored by hidden verifier

### Step 4: Compute migration barriers for universality set
- Role: scored (load-bearing)
- Action: Perform CI-NEB calculations for the chosen pure metals and their Mn-containing binary alloys (20 at.% Mn). For each system, compute Ed for at least two migration paths involving the host metal atom. For the Fe-based system, apply DFT+U with an effective Hubbard Ueff = 2 eV. Output results in a CSV file.
- Output file: `/app/outputs/migration_barriers_universality.csv`
- Format: csv
- Contract: CSV with header: system,atom_type,migration_barrier_eV. system: string (e.g., 'pure Cu', 'Cu0.8Mn0.2'); atom_type: string (e.g., 'Cu'); migration_barrier_eV: float. One row per path.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barriers_NiCoX.csv`
- `/app/outputs/migration_barriers_universality.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barriers_NiCoX.csv
- path: `/app/outputs/migration_barriers_NiCoX.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed migration barriers for Ni and Co atoms in Ni0.6Co0.2X0.2 (X=Co,Fe,Mn) alloys. The checker will compute per-alloy average barriers and evaluate structural trends.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `atom_type`, `migration_barrier_eV`
  - `units`:
    - `migration_barrier_eV`: eV

### migration_barriers_universality.csv
- path: `/app/outputs/migration_barriers_universality.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed migration barriers for pure metals and their 80/20 metal-Mn binary alloys. The checker will compute per-system average barriers and evaluate structural trends.
- schema:
  - `type`: table
  - `required_columns`: `system`, `atom_type`, `migration_barrier_eV`
  - `units`:
    - `migration_barrier_eV`: eV

Notes: The scoring is structural (T3): it evaluates relative ordering and magnitude differences of computed average barriers without requiring exact numeric agreement. The exact criteria are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barriers_NiCoX.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "atom_type",
          "migration_barrier_eV"
        ],
        "units": {
          "migration_barrier_eV": "eV"
        }
      },
      "description": "Computed migration barriers for Ni and Co atoms in Ni0.6Co0.2X0.2 (X=Co,Fe,Mn) alloys. The checker will compute per-alloy average barriers and evaluate structural trends."
    },
    {
      "file": "migration_barriers_universality.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "atom_type",
          "migration_barrier_eV"
        ],
        "units": {
          "migration_barrier_eV": "eV"
        }
      },
      "description": "Computed migration barriers for pure metals and their 80/20 metal-Mn binary alloys. The checker will compute per-system average barriers and evaluate structural trends."
    }
  ],
  "notes": "The scoring is structural (T3): it evaluates relative ordering and magnitude differences of computed average barriers without requiring exact numeric agreement. The exact criteria are not disclosed."
}
```

## How you are scored
A hidden verifier will read your output CSV files and assess the results against a predefined structural criterion that evaluates relative ordering and magnitude differences among the computed average barriers. The exact criteria (magnitude thresholds, direction) are not disclosed to prevent leakage. The verifier does not require exact numeric agreement with a reference dataset. Reporting literature values without executing the required DFT+CI-NEB workflow will not satisfy the scoring criteria.
