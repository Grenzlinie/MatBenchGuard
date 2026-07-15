# Vacancy Migration Barriers in Si using ART nouveau and SIESTA

## Problem background
Self-diffusion in crystalline silicon is mediated by native point defects, particularly the neutral monovacancy. Understanding diffusion, damage annealing, and defect evolution requires accurate knowledge of the formation energy and the energy barriers for vacancy hopping and competing activated mechanisms such as reorientation of the Jahn–Teller distorted configuration. This task requires you to compute these quantities for a single neutral vacancy in Si using a first-principles approach that combines saddle-point sampling with density-functional theory.

## Approach
The SIEST-A-RT method couples the activation-relaxation technique (ART nouveau) with the SIESTA density-functional theory (DFT) code. ART nouveau is an open-ended saddle-point search algorithm: starting from a local minimum it applies a random displacement, then follows the lowest negative curvature eigendirection while minimizing forces perpendicular to it to converge to a transition state; after crossing the saddle, the system relaxes to a new minimum. SIESTA provides forces and total energies within the local-density approximation (LDA) using norm-conserving Troullier-Martins pseudopotentials, an optimized single-ζ polarized atomic orbital basis set, a real-space mesh cutoff of 50 Ry, and Γ-point Brillouin zone sampling.

You will construct a 216-atom pristine supercell of Si at the LDA lattice constant (5.39 Å) and relax it with SIESTA. After removing one atom to create a neutral monovacancy in a 215-atom cell, you will relax the defective supercell to obtain the Jahn–Teller distorted D₂d minimum. From the total energies of the perfect and defective cells you will compute the vacancy formation energy using the expression E_form = E_{N-1} − (N−1)/N × E_N with N = 216.

Starting from the relaxed vacancy minimum, you will perform multiple ART nouveau saddle‑point searches, restricting initial random displacements to atoms surrounding the vacancy. From the resulting set of saddle points and minima you will extract the lowest barrier for a nearest‑neighbour vacancy hop (simple diffusion) and the barrier for a reorientation event that switches the pairing of the dangling bonds between equivalent D₂d states. The barrier is the difference between the saddle-point energy and the minimum energy. All ART and relaxation steps use the same SIESTA settings.

## Reproduction target
Produce the following three output files under `/app/outputs`:

- `step_01_formation_energy.txt` – the vacancy formation energy computed from your relaxed total energies, formatted as `E_form = <value> eV`.
- `step_02_migration_barrier.txt` – the lowest energy barrier for a nearest‑neighbour vacancy hop obtained from the ART saddle‑point searches, formatted as `E_barrier_hop = <value> eV`.
- `step_03_reorientation_barrier.txt` – the energy barrier for reorientation between equivalent D₂d orientations obtained from the ART searches, formatted as `E_barrier_reorient = <value> eV`.

Each file must contain exactly one line with the numeric value in eV units. The values must be derived from your own SIESTA calculations and ART sampling; do not substitute literature values.

## Assets

- SIESTA DFT code: https://departments.icmab.es/leem/siesta/
- Troullier‑Martins pseudopotentials for Si: https://www.quantum-simulation.org/potentials/sg15_oncv/upf/

## Workflow steps

### Step 1: Relax pristine Si supercell
- Role: process
- Action: Build a 216‑atom diamond‑cubic Si supercell using the LDA lattice constant (5.39 Å) and relax atomic positions with SIESTA (LDA functional, Troullier‑Martins pseudopotentials, SZ‑optimized PAO basis, real‑space mesh cutoff 50 Ry, Γ‑point sampling) until forces fall below 0.002 eV/Å via conjugate‑gradient minimization.
- Evidence: `/app/outputs/perfect_relax.log`

### Step 2: Relax vacancy supercell
- Role: process
- Action: Remove one atom to create a neutral monovacancy in a 215‑atom cell and relax using the same SIESTA settings as the perfect supercell, until forces < 0.002 eV/Å, to obtain the Jahn–Teller D₂d minimum.
- Evidence: `/app/outputs/vacancy_relax.log`

### Step 3: Compute vacancy formation energy
- Role: scored
- Action: Using the total energies from the relaxed pristine and defective supercells (N=216), compute the formation energy E_form = E_{N-1} - (N-1)/N * E_N and output the result as a single line: E_form = <value> eV.
- Output file: `/app/outputs/step_01_formation_energy.txt`
- Format: txt
- Contract: Single line: E_form = <value> eV
- Scoring: scored by hidden verifier

### Step 4: ART nouveau saddle‑point sampling
- Role: process
- Action: Starting from the relaxed vacancy D₂d minimum, perform ART nouveau saddle‑point searches. For each event: apply random initial displacements restricted to atoms surrounding the vacancy; use the Lanczos algorithm to follow the lowest negative curvature eigendirection while minimizing perpendicular directions until total force < 0.1 eV/Å. After reaching the saddle, relax to the new minimum. Use SIESTA with the same DFT parameters. Generate enough events to reliably identify the lowest‑energy nearest‑neighbour vacancy hop and a reorientation event.
- Evidence: `/app/outputs/art_events.log`

### Step 5: Extract migration barrier
- Role: scored (load-bearing)
- Action: From the ART‑generated events, identify the transition state corresponding to a nearest‑neighbour vacancy hop (simple diffusion) and compute the barrier as E_saddle − E_minimum. Output the lowest such barrier as a single line: E_barrier_hop = <value> eV.
- Output file: `/app/outputs/step_02_migration_barrier.txt`
- Format: txt
- Contract: Single line: E_barrier_hop = <value> eV
- Scoring: scored by hidden verifier

### Step 6: Extract reorientation barrier
- Role: scored
- Action: From the ART events, identify the transition state for reorientation between equivalent D₂d orientations (change of pairing) and compute its barrier. Output the barrier as a single line: E_barrier_reorient = <value> eV.
- Output file: `/app/outputs/step_03_reorientation_barrier.txt`
- Format: txt
- Contract: Single line: E_barrier_reorient = <value> eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energy.txt`
- `/app/outputs/step_02_migration_barrier.txt`
- `/app/outputs/step_03_reorientation_barrier.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energy.txt
- path: `/app/outputs/step_01_formation_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Vacancy formation energy computed from DFT total energies.
- schema:
  - `description`: Single line: E_form = <value> eV. The value is a real number (eV units).

### step_02_migration_barrier.txt
- path: `/app/outputs/step_02_migration_barrier.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Lowest migration energy barrier for nearest‑neighbour vacancy hopping.
- schema:
  - `description`: Single line: E_barrier_hop = <value> eV. The value is a real number (eV units).

### step_03_reorientation_barrier.txt
- path: `/app/outputs/step_03_reorientation_barrier.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Energy barrier for reorientation between equivalent D₂d states.
- schema:
  - `description`: Single line: E_barrier_reorient = <value> eV. The value is a real number (eV units).

Notes: These three numbers are the main reproducible quantities of the study. The hidden checker compares each to the paper‑reported value within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "description": "Single line: E_form = <value> eV. The value is a real number (eV units)."
      },
      "description": "Vacancy formation energy computed from DFT total energies."
    },
    {
      "file": "step_02_migration_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "description": "Single line: E_barrier_hop = <value> eV. The value is a real number (eV units)."
      },
      "description": "Lowest migration energy barrier for nearest‑neighbour vacancy hopping."
    },
    {
      "file": "step_03_reorientation_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "description": "Single line: E_barrier_reorient = <value> eV. The value is a real number (eV units)."
      },
      "description": "Energy barrier for reorientation between equivalent D₂d states."
    }
  ],
  "notes": "These three numbers are the main reproducible quantities of the study. The hidden checker compares each to the paper‑reported value within a tolerance."
}
```

## How you are scored
A hidden verifier reads each of your three output files, extracts the numeric energy value, and compares it against a hidden reference using a fixed tolerance. Your final reward is a weighted sum of the scores for the three individual checks. Reporting values that are not consistent with your own computational workflow will yield low or zero reward, because the hidden reference reflects the expected outcome of a correct execution of the described protocol. You must perform the complete computational pipeline; looking up results from the literature is not sufficient.
