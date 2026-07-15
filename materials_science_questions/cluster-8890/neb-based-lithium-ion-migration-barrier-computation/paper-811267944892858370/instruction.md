# Li, Na, Mg intercalation and diffusion barriers in 2H-MoS2 with controlled interlayer spacing

## Problem background
Layered molybdenum disulfide (MoS₂) is a promising cathode material for rechargeable batteries beyond Li-ion, including Na and Mg. Its open van der Waals gap can host guest ions, but the slow diffusion of larger or multivalent ions limits practical performance. This work investigates how varying the interlayer spacing (by changing the lattice constant c) affects the thermodynamics and kinetics of Li, Na, and Mg intercalation in the 2H phase of MoS₂. The target is to compute the binding energies at intercalation sites and the migration barriers as a function of c, providing insight into whether layer expansion can unlock fast multivalent-ion mobility.

## Approach
Use first-principles density functional theory (DFT) with a van der Waals-corrected functional to model a 3×3×1 supercell of bulk 2H-MoS₂. The interlayer spacing is controlled by varying the lattice constant c in the range 12–24 Å, fixing one Mo atom per layer to maintain the chosen spacing while relaxing other atoms. For each c, a single M atom (M = Li, Na, Mg) is placed at the octahedral (Oh) or tetrahedral (Th) site and the binding energy is calculated as the difference in total energy between the intercalated system, the empty host at the same c, and the isolated M atom. Migration barriers are computed along the Oh–Th–Oh diffusion path using the climbing-image nudged elastic band (CI-NEB) method with at least five intermediate images. All calculations use an open-source DFT code with pseudopotentials and a plane-wave basis; the essential physics is captured by the choice of a vdW functional.

## Reproduction target
Produce two CSV files containing intercalation binding energies and diffusion barriers for Li, Na, and Mg in 2H-MoS₂ across a range of lattice constants c. For binding energies, evaluate the Oh site for all ions at c = 12, 13, 14, 15, 16, 18, 20, 24 Å, and additionally the Th site for Li when c > 15 Å. For diffusion barriers, use CI-NEB to obtain the barrier height (relative to the more stable site) along Oh–Th–Oh for each ion at c = 13, 14, 15, 16, 17, 18 Å. The output columns must match the schema specified in the workflow steps.

## Assets

- 2H-MoS2 crystal structure: https://materialsproject.org/materials/mp-2815/
- Open-source DFT code with NEB capability: quantum-espresso
- Pseudopotentials for Mo, S, Li, Na, Mg: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build and relax pristine MoS2 supercell
- Role: process
- Action: Construct a 3×3×1 supercell of hexagonal 2H-MoS2 using the experimental lattice constants (a=3.15 Å, c=12.60 Å). Perform DFT structure relaxation with a van der Waals corrected functional to obtain equilibrium lattice parameters and atomic positions. The relaxed cell is used for all subsequent intercalation calculations.
- Evidence: none

### Step 2: Compute intercalation binding energies
- Role: scored
- Action: For each ion (Li, Na, Mg) and each lattice constant c in [12, 13, 14, 15, 16, 18, 20, 24] Å, intercalate a single M atom at the Oh site (and additionally at the Th site for Li when c > 15 Å). In all calculations, fix the z-coordinate of one Mo atom in each MoS₂ layer to constrain the interlayer spacing. Perform DFT total energy calculations for M/MoS₂, isolated M atom, and empty MoS₂ at each c. Compute binding energy E_b = E(M/MoS₂) - E(MoS₂) - E(atom). Write the results to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: CSV with columns: ion (Li|Na|Mg), c_A (float), site (Oh|Th), binding_energy_eV (float). One row per (ion, c, site) combination.
- Scoring: scored by hidden verifier

### Step 3: Compute CI-NEB diffusion barriers
- Role: scored (load-bearing)
- Action: For each ion (Li, Na, Mg) and each lattice constant c in [13, 14, 15, 16, 17, 18] Å, compute the minimum energy path for diffusion along alternating Oh and Th sites (Oh→Th→Oh) using the climbing-image nudged elastic band (CI-NEB) method. Use at least five intermediate images and a force convergence criterion of 0.1 eV/Å. Determine the diffusion barrier as the maximum energy difference along the path relative to the more stable site. Write the barrier values to diffusion_barriers.csv.
- Output file: `/app/outputs/diffusion_barriers.csv`
- Format: csv
- Contract: CSV with columns: ion (Li|Na|Mg), c_A (float), barrier_eV (float), start_site (Oh|Th), end_site (Oh|Th), reference_site (Oh|Th). One row per ion and c value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/diffusion_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies of Li, Na, Mg intercalated in 2H-MoS2 at octahedral and tetrahedral sites for various interlayer spacings (lattice constant c).
- schema:
  - `type`: table
  - `required_columns`: `ion`, `c_A`, `site`, `binding_energy_eV`

### diffusion_barriers.csv
- path: `/app/outputs/diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Diffusion energy barriers for Li, Na, Mg migration between Oh and Th sites in 2H-MoS2 at selected interlayer spacings.
- schema:
  - `type`: table
  - `required_columns`: `ion`, `c_A`, `barrier_eV`, `start_site`, `end_site`, `reference_site`

Notes: The checker compares computed binding energies and diffusion barriers to hidden reference values with appropriate tolerances and verifies structural trends (monotonic decrease with c, minimum barrier for Li, similarity of Na/Mg barriers, etc.).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ion",
          "c_A",
          "site",
          "binding_energy_eV"
        ]
      },
      "description": "Binding energies of Li, Na, Mg intercalated in 2H-MoS2 at octahedral and tetrahedral sites for various interlayer spacings (lattice constant c)."
    },
    {
      "file": "diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ion",
          "c_A",
          "barrier_eV",
          "start_site",
          "end_site",
          "reference_site"
        ]
      },
      "description": "Diffusion energy barriers for Li, Na, Mg migration between Oh and Th sites in 2H-MoS2 at selected interlayer spacings."
    }
  ],
  "notes": "The checker compares computed binding energies and diffusion barriers to hidden reference values with appropriate tolerances and verifies structural trends (monotonic decrease with c, minimum barrier for Li, similarity of Na/Mg barriers, etc.)."
}
```

## How you are scored
A hidden verifier reads the submitted binding_energies.csv and diffusion_barriers.csv, compares your computed energies and barriers to reference criteria, and checks basic structural consistency (e.g., monotonicity of barriers with c). The reward is a weighted combination of the binding energy and diffusion barrier scores; the barrier stage carries the majority weight. The verifier does not re-run your DFT calculations and does not penalize legitimate differences due to choice of DFT code or pseudopotential, provided the physics is correct. You are scored on the correctness of the computed trends and the accuracy relative to the hidden gold.
