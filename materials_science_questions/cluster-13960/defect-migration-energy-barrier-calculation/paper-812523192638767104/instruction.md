# Proton migration barrier calculation in VO2 and oxygen-deficient VO2

## Problem background
Proton (H+) insertion into correlated oxides such as VO2 enables reconfigurable synaptic transistors where the protonic diffusion barrier determines switching speed. Oxygen vacancies are intrinsic defects that may influence proton migration, but their quantitative effect on the energy barriers remains an open question. In this task, you will use first-principles density functional theory (DFT+U) to compute proton migration energy barriers in stoichiometric VO2 and in oxygen-deficient VO2-δ, and determine whether oxygen vacancies increase or decrease these barriers.

## Approach
The workflow is an ab‑initio simulation pipeline. Starting from the rutile VO2 crystal structure, you will construct supercells for stoichiometric VO2 and for VO2-δ containing one oxygen vacancy. After identifying stable proton insertion sites, you will define three distinct proton diffusion tunnels along the [001] crystallographic direction. All structures are relaxed using spin‑polarized GGA-PBE with a Hubbard U correction on vanadium 3d states. Finally, the climbing‑image nudged elastic band (CI‑NEB) method is used to obtain the minimum‑energy paths for proton hopping along each tunnel, and the energy barrier (saddle point minus initial minimum) is extracted. The result is a comparison of barrier heights between stoichiometric and oxygen‑deficient VO2.

## Reproduction target
You must produce a CSV file, `migration_barriers.csv`, containing at least four rows: one barrier for stoichiometric VO2 and one barrier for each of three tunnels (tunnel1, tunnel2, tunnel3) in oxygen‑deficient VO2‑δ. Each row has the columns `system` ("stoichiometric" or "oxygen‑deficient"), `tunnel` (empty string for stoichiometric, "tunnel1", "tunnel2", or "tunnel3" for oxygen‑deficient), and `barrier_eV` (float, unit eV). The hidden verifier will compare your computed barriers to reference values from the literature and will assess whether the barriers in VO2-δ are higher or lower than the stoichiometric barrier. The task is to faithfully compute these barriers using the prescribed DFT+U workflow; reporting numbers without performing the actual calculations will not satisfy the scoring criteria.

## Assets

- Rutile VO2 crystal structure (mp-19032): https://materialsproject.org/materials/mp-19032/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV pseudopotentials (or equivalent PAW/USPP): http://www.physics.rutgers.edu/gbrv/

## Workflow steps

### Step 1: Construct supercells and define diffusion tunnels
- Role: process
- Action: Using a rutile VO2 crystal structure, build supercells for stoichiometric VO2 and oxygen-deficient VO2-δ with one oxygen vacancy. Identify stable proton insertion sites and define the three diffusion tunnels (tunnel 1: H3→H2, tunnel 2: H7→H6, tunnel 3: H9→H12) along the [001] direction. Save the prepared initial atomic configurations.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: DFT+U structural relaxation
- Role: process
- Action: Relax the lattice parameters and atomic coordinates of all supercells using DFT+U (GGA-PBE, U=3.25 eV on V 3d states) with a suitable plane‑wave energy cutoff and k‑point sampling, converging Hellmann–Feynman forces below 0.01 eV/Å.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 3: Compute proton migration barriers
- Role: scored (load-bearing)
- Action: Using the relaxed structures, compute the proton migration energy barrier for stoichiometric VO2 and for oxygen-deficient VO2-δ along the three pre‑defined tunnels (tunnel 1: H3→H2, tunnel 2: H7→H6, tunnel 3: H9→H12). Employ NEB or CI‑NEB at the same DFT+U level to obtain the minimum‑energy path and extract each barrier height (energy difference between saddle point and initial minimum). Collect all barriers into a single CSV file.
- Output file: `/app/outputs/migration_barriers.csv`
- Format: csv
- Contract: Columns: system (string: 'stoichiometric' or 'oxygen-deficient'), tunnel (string: empty string for stoichiometric, 'tunnel1','tunnel2','tunnel3' for oxygen-deficient), barrier_eV (float, unit eV). At least 4 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barriers.csv
- path: `/app/outputs/migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Proton migration barriers. The checker compares each barrier to the paper‑reported value using a tolerance and additionally verifies the trend that all oxygen‑deficient barriers are strictly lower than the stoichiometric barrier.
- schema:
  - `type`: table
  - `required_columns`: `system`, `tunnel`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

Notes: The instruction does not reveal the expected barrier values or the tolerance; the checker uses the paper’s hidden gold numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "tunnel",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Proton migration barriers. The checker compares each barrier to the paper‑reported value using a tolerance and additionally verifies the trend that all oxygen‑deficient barriers are strictly lower than the stoichiometric barrier."
    }
  ],
  "notes": "The instruction does not reveal the expected barrier values or the tolerance; the checker uses the paper’s hidden gold numbers."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `migration_barriers.csv`. The verifier compares each reported barrier value to a hidden reference value using a tolerance, awarding partial credit for each barrier that meets the tolerance. It also performs a trend check: it verifies whether the three oxygen‑deficient barriers are consistently higher or consistently lower than the stoichiometric barrier (the exact direction is unknown to you; you must compute it). The combination of value accuracy and the trend verification yields a final reward between 0 and 1. The absolute values and tolerance are hidden; simply reporting numbers that match the paper without running the DFT workflow is not sufficient to pass all checks.
