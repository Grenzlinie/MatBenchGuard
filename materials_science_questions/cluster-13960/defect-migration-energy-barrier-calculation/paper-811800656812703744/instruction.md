# Au Migration Barriers on Graphene Vacancies and Zigzag Edges via DFT NEB

## Problem background
Metal atoms on graphene surfaces can be trapped at vacancies and migrate together with the vacancy. Understanding the migration barriers and the role of edges is crucial for defect-mediated engineering of graphene's atomic and electronic structures. This task studies the properties and diffusion mechanisms of gold atoms at single vacancies in infinite graphene and near zigzag edges using density-functional theory (DFT). The key open questions are: what are the stable configurations and formation energies of a gold atom at a single vacancy, and what are the energy barriers for the Au atom to move through the vacancy, for the Au-vacancy pair to migrate laterally, and for the Au atom to diffuse along a hydrogen-passivated zigzag edge? Computing these quantities will provide insight into the dynamics of metal atoms on substitutional sites in graphene.

## Approach
The calculations are carried out with the plane-wave DFT code Quantum ESPRESSO (PWscf and NEB modules). The exchange-correlation functional is the generalized gradient approximation (GGA) of Perdew-Wang (PW91), and ultrasoft pseudopotentials describe the core electrons. The approach consists of two parts: (1) Static relaxations to find the minimum-energy configurations of an Au atom at a single vacancy in a graphene supercell. Both the off-plane stable structure and the constrained in-plane (flat) saddle-point structure are relaxed, and the formation energy of each is computed as E_f = E_system - E_system_with_vacancy - E_Au. The difference between these formation energies gives the energy barrier for the Au atom to pass through the vacancy. (2) Climbing-image nudged elastic band (CI-NEB) calculations to find minimum-energy paths and activation energies for two migration processes: the lateral migration of an Au-vacancy pair in an infinite graphene sheet, and the migration of an Au atom along the apex sites of a hydrogen-passivated zigzag graphene ribbon. The ribbon is modeled with a width of about 16 A and periodic boundary conditions. All supercells include sufficient vacuum to avoid spurious interactions between periodic images.

## Reproduction target
Perform the DFT calculations described above and report the following five energy quantities (in eV) in a JSON file `/app/outputs/results.json`:

- `off_plane_formation_energy_eV`: formation energy of the off-plane Au-vacancy configuration
- `in_plane_formation_energy_eV`: formation energy of the constrained in-plane (flat) Au configuration
- `through_vacancy_barrier_eV`: energy difference between the in-plane and off-plane configurations
- `lateral_migration_barrier_eV`: activation barrier for lateral migration of the Au-vacancy pair in infinite graphene
- `edge_migration_barrier_eV`: activation barrier for Au migration between apex sites of the hydrogen-passivated zigzag edge

The JSON file must follow the exact schema shown in step 4.

## Assets

- Quantum ESPRESSO (PWscf and NEB modules): https://www.quantum-espresso.org/
- Ultrasoft pseudopotential for carbon
- Ultrasoft pseudopotential for gold

## Workflow steps

### Step 1: Relax Au at single vacancy and compute formation energies
- Role: process
- Action: Construct a graphene supercell (79 C atoms, single vacancy, 12 Å vacuum along c-axis). Place an Au atom near the vacancy. Relax the off-plane minimum-energy configuration and compute the total energy. Then compute the constrained in-plane flat configuration (saddle point) and its total energy. Calculate the formation energy for each configuration using E_f = E_system − E_system_with_vacancy − E_Au. Also compute the reference energies E_system_with_vacancy and E_Au at the same level of theory. The difference in formation energies gives the through-vacancy barrier.
- Evidence: `/app/outputs/au_vacancy_relax.log`

### Step 2: NEB for Au-vacancy pair lateral migration in infinite graphene
- Role: process
- Action: Using the off-plane relaxed structures from step_01, prepare initial and final images of the Au-vacancy pair displaced by one lattice vector. Run a climbing-image NEB calculation (neb.x) to find the minimum energy pathway and extract the activation barrier for lateral migration.
- Evidence: `/app/outputs/neb_lateral.out`

### Step 3: NEB for Au edge migration on zigzag ribbon
- Role: process
- Action: Construct a hydrogen-passivated zigzag graphene ribbon of width ~16 Å. Place the Au atom at an apex site of the zigzag edge and relax the structure. Set up a NEB calculation where the Au atom jumps to a neighboring apex site. Run the climbing-image NEB and extract the activation energy for edge migration.
- Evidence: `/app/outputs/neb_edge.out`

### Step 4: Write final reproduction results
- Role: scored (load-bearing)
- Action: Collect the five computed quantities: off-plane formation energy (eV), in-plane formation energy (eV), through-vacancy barrier (eV), lateral migration barrier (eV), and edge migration barrier (eV). Write them into a JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"off_plane_formation_energy_eV": float, "in_plane_formation_energy_eV": float, "through_vacancy_barrier_eV": float, "lateral_migration_barrier_eV": float, "edge_migration_barrier_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The five energy values (in eV) that constitute the main reproduction targets. The checker compares each to the paper's reported numbers using hidden tolerances (±0.15 eV for formation energies and through-vacancy barrier, ±0.2 eV for migration barriers).
- schema:
  - `type`: object
  - `required`: `off_plane_formation_energy_eV`, `in_plane_formation_energy_eV`, `through_vacancy_barrier_eV`, `lateral_migration_barrier_eV`, `edge_migration_barrier_eV`
  - `properties`:
    - `off_plane_formation_energy_eV`:
      - `type`: number
    - `in_plane_formation_energy_eV`:
      - `type`: number
    - `through_vacancy_barrier_eV`:
      - `type`: number
    - `lateral_migration_barrier_eV`:
      - `type`: number
    - `edge_migration_barrier_eV`:
      - `type`: number

Notes: The agent must produce exactly this JSON structure. All values are in eV. Tolerances are hidden and account for pseudopotential and numerical differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "off_plane_formation_energy_eV",
          "in_plane_formation_energy_eV",
          "through_vacancy_barrier_eV",
          "lateral_migration_barrier_eV",
          "edge_migration_barrier_eV"
        ],
        "properties": {
          "off_plane_formation_energy_eV": {
            "type": "number"
          },
          "in_plane_formation_energy_eV": {
            "type": "number"
          },
          "through_vacancy_barrier_eV": {
            "type": "number"
          },
          "lateral_migration_barrier_eV": {
            "type": "number"
          },
          "edge_migration_barrier_eV": {
            "type": "number"
          }
        }
      },
      "description": "The five energy values (in eV) that constitute the main reproduction targets. The checker compares each to the paper's reported numbers using hidden tolerances (±0.15 eV for formation energies and through-vacancy barrier, ±0.2 eV for migration barriers)."
    }
  ],
  "notes": "The agent must produce exactly this JSON structure. All values are in eV. Tolerances are hidden and account for pseudopotential and numerical differences."
}
```

## How you are scored
A hidden verifier evaluates your submission in two parts. First, it checks that all required intermediate evidence files (`au_vacancy_relax.log`, `neb_lateral.out`, `neb_edge.out`) are present, indicating that the DFT and NEB workflow was genuinely executed. Second, it reads your final result file `/app/outputs/results.json` and compares each of the five reported values against reference values derived from the original study. The comparison uses hidden tolerances that account for expected variations due to different pseudopotential choices, implementation details, and numerical settings. Your overall score is a weighted combination of these checks; producing the required artifacts through actual computation (rather than guessing or hardcoding values) is essential to earn credit. The exact tolerances and weights are not disclosed, but the scoring is designed to reward physically reasonable results that are consistent with the described methodology.
