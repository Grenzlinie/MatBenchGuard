# First-principles formation energies and migration barriers of interstitial dumbbells in Ni-based alloys

## Problem background
Single-phase concentrated solid-solution alloys (SP-CSAs) have attracted interest for their enhanced radiation tolerance. Irradiation experiments show that these alloys exhibit segregation at interstitial loops (enrichment of Co/Ni and depletion of Fe/Cr), as well as a transition in interstitial migration behaviour. The underlying defect properties that drive these observations—formation energies and migration kinetics of interstitial dumbbell defects—are not yet fully understood from first principles. This task investigates the formation energetics and migration kinetics of <100>, <110>, and <111> dumbbell interstitials in pure fcc Ni and in two model Ni‑based concentrated alloys with compositions Ni₃Fe (Ni₀.₇₅Fe₀.₂₅) and Ni₃Co (Ni₀.₇₅Co₀.₂₅). The goal is to compute the formation energies and the barriers for several key migration paths, providing insight into the experimentally observed segregation and the interstitial migration mode shift.

## Approach
The calculation is a first-principles DFT workflow. Use spin-polarised density functional theory with the PBE exchange-correlation functional. Construct 3×3×3 supercells (108 atoms) for pure fcc Ni and for the ordered L1₂ structures of Ni₃Fe and Ni₃Co. Create supercells containing interstitial dumbbells in the <100>, <110>, and <111> orientations with the relevant atomic compositions (e.g., Ni–Ni, Ni–Fe, Fe–Fe in NiFe; Ni–Co, Co–Co, Co–Ni in NiCo). Relax each structure and extract total energies to compute formation energies relative to the defect-free bulk references. For selected migration paths, use the climbing‑image nudged elastic band (CI‑NEB) method to obtain minimum‑energy paths and energy barriers. The paths to study are:
(1) one-dimensional (1D) translation of a <110> dumbbell in Ni₃Co (Ni–Co → Co–Co → Ni–Co);
(2) three‑dimensional (3D) rotation between <111> and <110> dumbbells in all three systems;
(3) a 3D translation/rotation path from <100> X–Ni to <110> Ni–Ni via a <001> Ni–Ni intermediate, in all three systems.
The workflow uses an open‑source DFT code (Quantum ESPRESSO) with PAW pseudopotentials from the SSSP library; the original paper used a proprietary code, but the methodology and the physics are unchanged.

## Reproduction target
Produce two scored JSON files under `/app/outputs`:
- `formation_energies.json`: formation energies (in eV) of the investigated dumbbell interstitials in pure Ni, Ni₃Fe, and Ni₃Co. For each system, list the energy for every stable dumbbell composition and orientation specified in the workflow.
- `migration_barriers.json`: energy barriers (in eV) for the three families of CI‑NEB migration paths described above, labelled by system and path.

The hidden verifier will check these artifacts against a reference by evaluating:
- the relative ordering of the formation energies (i.e., which dumbbell compositions are more or less stable) and the energy differences between key species in each alloy;
- the magnitude of the migration barriers, applying threshold conditions that reflect the expected transport regime (fast 1D, mixed 1D+3D, or sluggish 3D).
The task is considered successfully reproduced if the computed trends and barrier values fall within the expected ranges defined by the verifier.

## Assets

- Quantum ESPRESSO: quantum-espresso
- SSSP pseudopotentials (PBE, PAW): https://www.materialscloud.org/discover/sssp/table
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Lattice parameter validation and supercell construction
- Role: process
- Action: Perform DFT geometry optimization of bulk fcc Ni to obtain the equilibrium lattice constant. Using this lattice constant, construct 3×3×3 supercells (108 atoms) of pure Ni, ordered Ni₃Fe (L1₂) and Ni₃Co (L1₂) with the described atomic arrangements. Optimize the atomic positions of the bulk supercells.
- Evidence: `/app/outputs/lattice_opt.log`

### Step 2: Compute interstitial formation energies
- Role: scored (load-bearing)
- Action: For each system (Ni, Ni₃Fe, Ni₃Co), create defect supercells containing ⟨100⟩, ⟨110⟩, and ⟨111⟩ dumbbell interstitials with the specified compositions (e.g., Ni–Ni, Ni–Fe, Fe–Ni, Fe–Fe in NiFe; Ni–Co, Co–Co, Co–Ni in NiCo). Perform spin-polarized DFT relaxations (force convergence 0.01 eV/Å) and extract total energies. Compute formation energies of each dumbbell using the standard reference scheme (defect energy minus appropriate bulk reference).
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: Top-level keys: "Ni", "Ni3Fe", "Ni3Co". Each value is an object with orientation keys ("<100>", "<110>", "<111>"), each containing composition keys (e.g., "Ni-Ni", "Ni-Fe", "Fe-Ni", "Fe-Fe", "Ni-Co", "Co-Co", "Co-Ni") with numeric formation energy in eV.
- Scoring: scored by hidden verifier

### Step 3: Compute migration barriers via CI-NEB
- Role: scored
- Action: For the selected interstitial migration paths, prepare initial and final structures from relaxed endpoint calculations. Use the climbing-image nudged elastic band (CI-NEB) method with force convergence of 0.02 eV/Å to find the minimum energy path. Required paths: (1) 1D translation of ⟨110⟩ Ni–Co → Co–Co → Ni–Co in Ni₃Co; (2) 3D rotation from ⟨111⟩ to ⟨110⟩ dumbbells in Ni, Ni₃Fe, Ni₃Co; (3) 3D translation/rotation from ⟨100⟩ X–Ni to ⟨110⟩ Ni–Ni via ⟨001⟩ Ni–Ni intermediate in all three systems. Report the barrier energy for each path.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: Top-level keys: "Ni", "Ni3Co", "Ni3Fe". Each value is an object with path_description keys (e.g., "1D_<110>_translation", "3D_<111>_to_<110>", "3D_<100>_trans_rot") and numeric barrier energy in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of interstitial dumbbells in Ni and alloys. Verifier checks relative stability ordering and key energy differences.
- schema:
  - `type`: object
  - `required`: object
  - `units`:
    - `energy`: eV
  - `description`: Top-level keys: "Ni", "Ni3Fe", "Ni3Co". Each value is an object with orientation keys ("<100>", "<110>", "<111>"), each containing composition keys (e.g., "Ni-Ni", "Ni-Fe", "Fe-Ni", "Fe-Fe", "Ni-Co", "Co-Co", "Co-Ni") with numeric formation energy in eV.

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Migration barrier energies for key interstitial migration paths. Verifier checks threshold conditions (e.g., barrier ≤0.01 eV in Ni, ~0.07 eV in NiCo, and ≥0.10 eV in NiFe).
- schema:
  - `type`: object
  - `required`: object
  - `units`:
    - `barrier`: eV
  - `description`: Top-level keys: "Ni", "Ni3Co", "Ni3Fe". Each value is an object with path_description keys (e.g., "1D_<110>_translation", "3D_<111>_to_<110>", "3D_<100>_trans_rot") and numeric barrier energy in eV.

Notes: The verifier recomputes ordering and energy differences from formation_energies.json and applies threshold checks on barriers. Tolerances absorb legitimate toolchain spread from using Quantum ESPRESSO instead of VASP.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {},
        "units": {
          "energy": "eV"
        },
        "description": "Top-level keys: \"Ni\", \"Ni3Fe\", \"Ni3Co\". Each value is an object with orientation keys (\"<100>\", \"<110>\", \"<111>\"), each containing composition keys (e.g., \"Ni-Ni\", \"Ni-Fe\", \"Fe-Ni\", \"Fe-Fe\", \"Ni-Co\", \"Co-Co\", \"Co-Ni\") with numeric formation energy in eV."
      },
      "description": "Formation energies of interstitial dumbbells in Ni and alloys. Verifier checks relative stability ordering and key energy differences."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {},
        "units": {
          "barrier": "eV"
        },
        "description": "Top-level keys: \"Ni\", \"Ni3Co\", \"Ni3Fe\". Each value is an object with path_description keys (e.g., \"1D_<110>_translation\", \"3D_<111>_to_<110>\", \"3D_<100>_trans_rot\") and numeric barrier energy in eV."
      },
      "description": "Migration barrier energies for key interstitial migration paths. Verifier checks threshold conditions (e.g., barrier ≤0.01 eV in Ni, ~0.07 eV in NiCo, and ≥0.10 eV in NiFe)."
    }
  ],
  "notes": "The verifier recomputes ordering and energy differences from formation_energies.json and applies threshold checks on barriers. Tolerances absorb legitimate toolchain spread from using Quantum ESPRESSO instead of VASP."
}
```

## How you are scored
After you write the two output files, a hidden verifier (not visible to you) will independently load your JSON artifacts and evaluate each stage separately.

- For `formation_energies.json`, the verifier inspects the stability ordering and checks that selected energy differences satisfy predefined constraints. This stage carries the largest weight because it is load‑bearing.
- For `migration_barriers.json`, the verifier checks that the reported barriers meet threshold conditions consistent with the paper’s physical interpretation; this stage carries a moderate weight.

The stage scores are combined into a final reward between 0 and 1. Merely reporting numbers that happen to match the reference without genuinely executing the DFT and NEB calculations is not sufficient—the verifier’s checks are designed to confirm that the computational workflow has been carried out. You will not be shown the reference values or the tolerances; your job is to produce the best‑possible DFT results using the protocol described in the workflow steps.
