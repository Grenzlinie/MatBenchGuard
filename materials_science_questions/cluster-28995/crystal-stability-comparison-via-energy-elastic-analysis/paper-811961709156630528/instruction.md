# FePt Nanoparticle Stability: Single Crystalline vs Multiply Twinned via Energy Analysis

## Problem background
FePt nanoparticles in the L1₀ ordered phase exhibit high magneto-crystalline anisotropy and are promising for high‑density magnetic recording. Their structural stability governs which morphologies form during synthesis. This work investigates the relative energetic stability of multiply twinned (icosahedral and decahedral) versus single crystalline truncated octahedral FePt nanoparticles using atomistic simulations based on an analytic bond‑order potential (ABOP) for Fe–Pt. The comparison is performed for both chemically disordered (A1) and ordered (L1₀) phases, for particle sizes spanning roughly 500 to 10 000 atoms.

## Approach
The approach centres on implementing the analytic bond‑order potential (ABOP) for Fe–Pt from the provided parameter set and using it to perform molecular statics (conjugate‑gradient relaxation at 0 K) on closed‑shell nanoparticles of three morphologies:

- **Single crystalline truncated octahedra** constructed by a Wulff shape with the surface‑energy ratio predicted by the ABOP.
- **Marks decahedra** with equal indices m = n = p (square {100} facets and re‑entrant {111} facets).
- **Icosahedral multiply twinned particles**.

For each morphology and size, the average potential energy per atom must be obtained in two chemical states:

- **A1 disordered phase** – Fe and Pt atoms are assigned randomly at an equiatomic ratio; at least 20 random configurations are relaxed and the results averaged.
- **L1₀ ordered phase** – The layered L1₀ structure is built, equiatomic composition is enforced by randomly introduced anti‑site defects, and multiple configurations are averaged. For icosahedral particles, which cannot accommodate global L1₀ order without anti‑phase boundaries, a Monte‑Carlo simulated‑annealing procedure (atom displacements and exchanges, cooling from 1200 K to 0 K) is used to find a low‑energy ordered configuration, which is then further relaxed by molecular statics.

The key question to answer is how the per‑atom energy of the three morphologies compares across sizes and phases.

## Reproduction target
Compute the relaxed average potential energy per atom (eV/atom) for FePt nanoparticles in the single crystalline truncated octahedron, Marks decahedron, and icosahedral morphologies. At least five distinct particle sizes in the range 500–10 000 atoms must be examined. Calculations are required for both the A1 disordered phase and the L1₀ ordered phase, enforcing equiatomic composition in the ordered particles. Record the results in the file `/app/outputs/energies.csv` with one row per combination of size, morphology, and phase.

## Assets

- FePt analytic bond-order potential parameter set

## Workflow steps

### Step 1: Generate particle geometries
- Role: process
- Action: Generate closed-shell atomic coordinates for single crystalline truncated octahedra (using Wulff construction with the surface energy ratio derived from the ABOP), Marks decahedra with equal indices m=n=p, and icosahedral MTPs. Produce at least five distinct particle sizes in the range 500-10000 atoms for each morphology. Record the generated sizes and morphologies for the next step.
- Evidence: `/app/outputs/particle_geometries.json`

### Step 2: Compute relaxed potential energies
- Role: scored (load-bearing)
- Action: Using the geometries from Step 1, implement the analytic bond-order potential (ABOP) for Fe-Pt with the provided parameter set. For each morphology and size: (i) for the chemically disordered A1 phase, assign Fe and Pt atoms randomly with 1:1 composition, generate at least 20 random configurations, minimize energy via molecular statics (conjugate-gradient relaxation), and compute the average potential energy per atom; (ii) for the chemically ordered L1₀ phase (single crystalline and decahedral particles), construct the layered L1₀ structure, introduce anti-site defects to enforce equiatomic composition, average over multiple relaxed configurations; (iii) for ordered L1₀ icosahedral particles, use Monte Carlo simulated annealing (atom displacements and exchanges, cooling from 1200 K to 0 K) to find a low-energy ordered arrangement, then relax with molecular statics and record the average energy per atom. Output a CSV file 'energies.csv' with one row per combination of size, morphology, and phase.
- Output file: `/app/outputs/energies.csv`
- Format: csv
- Contract: CSV with columns: atoms (int), morphology (string: one of 'single', 'deca', 'ico'), phase (string: one of 'A1', 'L10'), energy_per_atom (float, eV/atom). One row per combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.csv
- path: `/app/outputs/energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average potential energy per atom for each particle size, morphology, and phase. The checker will verify energetic ordering between morphologies for each size and phase, and a threshold condition for small sizes.
- schema:
  - `type`: table
  - `required_columns`: `atoms`, `morphology`, `phase`, `energy_per_atom`
  - `units`:
    - `energy_per_atom`: eV/atom

Notes: The scoring is a structural audit (ordering and threshold), not a direct metric comparison. The energy values must be negative, but the checker primarily inspects relative order and size-dependent energy differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "atoms",
          "morphology",
          "phase",
          "energy_per_atom"
        ],
        "units": {
          "energy_per_atom": "eV/atom"
        }
      },
      "description": "Average potential energy per atom for each particle size, morphology, and phase. The checker will verify energetic ordering between morphologies for each size and phase, and a threshold condition for small sizes."
    }
  ],
  "notes": "The scoring is a structural audit (ordering and threshold), not a direct metric comparison. The energy values must be negative, but the checker primarily inspects relative order and size-dependent energy differences."
}
```

## How you are scored
A hidden verifier inspects `/app/outputs/energies.csv`. It checks that the data satisfy structural relationships (an energetic ordering between the three morphologies for each phase and size, together with a minimum energy difference for the smallest sizes) that characterise the physically expected behaviour. The check does **not** depend on exact numerical agreement with any previously published plot or table. Score is aggregated across all evaluated size‑phase groups, with the small‑size threshold carrying higher weight. Reporting correct relationships is therefore essential; providing fabricated numbers without performing the required simulations will not succeed.
