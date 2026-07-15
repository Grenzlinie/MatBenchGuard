# DFT Formation Energy and Migration Barrier Calculations for Interstitial Dumbbells in Ni, NiCo, and NiFe

## Problem background
Single-phase concentrated solid-solution alloys (SP-CSAs) such as NiCo and NiFe exhibit enhanced radiation tolerance compared to pure metals. A microscopic understanding of how chemical complexity alters the formation and migration of interstitial defects is essential for interpreting irradiation-induced segregation and the observed changes in interstitial diffusion modes. This work investigates interstitial dumbbell defects in pure Ni and two model alloys using first-principles calculations. The objective is to compute formation energies of dumbbells in different orientations and compositions, and migration barriers for key diffusion paths, thereby revealing the atomistic origins of the distinct radiation response.

## Approach
The computational approach employs spin-polarized density functional theory (DFT) with a plane-wave basis and standard GGA-PBE pseudopotentials, executed with an open-source DFT code such as Quantum ESPRESSO. The alloys are modelled as ordered L1₂ structures, and 3×3×3 supercells are used. For each system, a perfect supercell is first relaxed to obtain a reference total energy. Interstitial dumbbell defects are introduced with three high-symmetry orientations (<100>, <110>, <111>) and different atomic species combinations. The defect supercells are relaxed, and their total energies are recorded. Formation energies are then derived from these energies using the standard defect formation energy definition that compares defect and perfect supercell energies, corrected by chemical potentials of the constituent elements obtained from elemental bulk calculations. Migration barriers for representative one-dimensional translation and three-dimensional rotation/translation paths are calculated using the nudged elastic band (NEB) method. The results are analysed to identify the relative stability of different dumbbell types and the energy barriers governing interstitial diffusion.

## Reproduction target
Produce two CSV output files under /app/outputs:

- `dumbbell_formation_energies.csv`: containing the formation energy (eV per dumbbell) for each system (Ni, NiCo, NiFe), dumbbell type (<100>, <110>, <111>), and atomic composition (e.g., Ni-Ni, Ni-Fe, etc.).
- `migration_barriers.csv`: containing the migration barrier (eV) for each system and a short description of the diffusion process (e.g., '1D translation <110> NiCo').

The target is to reproduce the correct relative ordering of formation energies across the different compositions and orientations, and the trend of migration barriers that distinguishes fast one-dimensional motion in pure Ni from mixed or sluggish three-dimensional motion in the alloys. The exact numerical values depend on the computational settings; what matters is the self-consistent set of results that capture these physical trends.

## Assets

- Atomic Simulation Environment (ASE): ase
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV or SSSP pseudopotentials: https://www.quantum-espresso.org/pseudopotentials
- NumPy: numpy

## Workflow steps

### Step 1: Lattice parameter optimization and supercell construction
- Role: process
- Action: Optimize the lattice parameters of fcc Ni, ordered L1₂ Ni₃Co, and ordered L1₂ Ni₃Fe using spin-polarized DFT. Construct 3×3×3 supercells (108 atoms) for each system.
- Evidence: `/app/outputs/lattice_parameters.json`

### Step 2: DFT relaxation of perfect supercells
- Role: process
- Action: Perform full ionic relaxation of defect-free 3×3×3 supercells of Ni, NiCo, and NiFe until all forces are below a chosen convergence threshold. Save the total energies.
- Evidence: `/app/outputs/perfect_supercell_energies.json`

### Step 3: DFT relaxation of interstitial dumbbell defect supercells
- Role: process
- Action: For each system, construct supercells containing a single interstitial dumbbell with orientations <100>, <110>, <111> and all relevant atomic compositions (Ni–Ni, Ni–Fe, Fe–Ni, Fe–Fe for NiFe; Ni–Co, Co–Co, Co–Ni, Ni–Ni for NiCo; Ni–Ni in pure Ni). Relax each defect supercell until forces converge. Save total energies and relaxed structures.
- Evidence: `/app/outputs/defect_supercell_energies.json`

### Step 4: Compute dumbbell formation energies
- Role: scored (load-bearing)
- Action: Calculate interstitial formation energies using the definition from the paper's methodology: E_f = E_defect - N_host*E_coh(bulk) - Σ n_i*μ_i, where chemical potentials μ_i are taken from cohesive energies of elemental bulk phases (Ni, Co, Fe) computed under the same code settings. Output results as a CSV.
- Output file: `/app/outputs/dumbbell_formation_energies.csv`
- Format: csv
- Contract: system (Ni/NiCo/NiFe), dumbbell_type (<100>/<110>/<111>), composition (e.g. Ni-Ni, Ni-Fe), formation_energy (float, eV per dumbbell)
- Scoring: scored by hidden verifier

### Step 5: NEB migration barrier calculations
- Role: scored
- Action: Using the relaxed defect endpoints from previous steps, perform nudged elastic band (NEB) calculations to compute migration energy barriers for: (a) 1D translation of <110> dumbbells in pure Ni and in NiCo; (b) 3D rotation/translation for selected paths (<111> to <110> in all three systems; <100> to <110> in Ni and NiFe). Ensure force convergence on NEB images. Save the barrier heights as a CSV.
- Output file: `/app/outputs/migration_barriers.csv`
- Format: csv
- Contract: system (Ni/NiCo/NiFe), process_description (string e.g. '1D translation <110> NiCo', '3D rotation <100>-><110> Ni'), barrier_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dumbbell_formation_energies.csv`
- `/app/outputs/migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dumbbell_formation_energies.csv
- path: `/app/outputs/dumbbell_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of interstitial dumbbells in Ni, NiCo, and NiFe. Scoring verifies the relative ordering and energy gaps match paper-reported trends.
- schema:
  - `type`: table
  - `required_columns`: `system`, `dumbbell_type`, `composition`, `formation_energy`
  - `units`:
    - `formation_energy`: eV per dumbbell

### migration_barriers.csv
- path: `/app/outputs/migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Migration energy barriers for selected 1D and 3D interstitial diffusion paths. Scoring verifies that 1D barriers in Ni are very low, 1D in NiCo is higher, and 1D in NiFe is essentially suppressed, while 3D barriers show a consistent trend.
- schema:
  - `type`: table
  - `required_columns`: `system`, `process_description`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

Notes: The agent must use Quantum ESPRESSO with GGA-PBE pseudopotentials. Ordered L1₂ supercells (Ni₃Co, Ni₃Fe) are used as models for NiCo and NiFe alloys. The scoring tolerates differences due to code and pseudopotential choices but requires the correct relative ordering and approximate energy gaps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dumbbell_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "dumbbell_type",
          "composition",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "eV per dumbbell"
        }
      },
      "description": "Formation energies of interstitial dumbbells in Ni, NiCo, and NiFe. Scoring verifies the relative ordering and energy gaps match paper-reported trends."
    },
    {
      "file": "migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "process_description",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Migration energy barriers for selected 1D and 3D interstitial diffusion paths. Scoring verifies that 1D barriers in Ni are very low, 1D in NiCo is higher, and 1D in NiFe is essentially suppressed, while 3D barriers show a consistent trend."
    }
  ],
  "notes": "The agent must use Quantum ESPRESSO with GGA-PBE pseudopotentials. Ordered L1₂ supercells (Ni₃Co, Ni₃Fe) are used as models for NiCo and NiFe alloys. The scoring tolerates differences due to code and pseudopotential choices but requires the correct relative ordering and approximate energy gaps."
}
```

## How you are scored
A hidden verifier independently assesses each scored artifact. For the formation energies, the checker verifies that the relative ordering of the computed formation energies for the various dumbbell compositions matches the published findings, and that the energy gaps between certain key configurations fall within hidden tolerance windows. For the migration barriers, the checker confirms that the one-dimensional barrier in pure Ni is extremely low, that the barrier in NiCo is higher, and that the one-dimensional path in NiFe is effectively blocked, while the three-dimensional barriers across the systems are of consistent magnitude. The tolerances account for legitimate differences due to DFT code, pseudopotentials, and convergence settings, but are sufficiently tight to reject arbitrary or guessed values. Each artifact contributes a weighted fraction to the final score; reporting numbers without performing the actual DFT calculations will not meet the verification criteria.
