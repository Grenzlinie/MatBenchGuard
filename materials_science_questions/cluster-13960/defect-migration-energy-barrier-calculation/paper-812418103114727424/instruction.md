# Reproduce activation energies and diffusion event statistics for a Ni vacancy in B2 NiAl using EAM potential

## Problem background
Diffusion in ordered B2 compounds such as NiAl is controlled by vacancy-mediated jumps that must restore the perfect order of the lattice.  Unlike pure metals, simple nearest-neighbor jumps create disorder, so mass transport relies on complex cyclic mechanisms whose energetics and relative frequencies are not fully established.  This task uses an embedded-atom interatomic potential to quantify, for a Ni vacancy, three static activation energies (vacancy formation energy, next-nearest-neighbor migration energy, and the peak barrier of the {110} six-jump cycle) and to determine the statistical distribution of dynamic diffusion events at 1200 K through direct molecular dynamics observation.

## Approach
The reproduction follows a two‑stage protocol.  First, molecular statics minimizations are performed on periodic B2 NiAl supercells with and without a Ni vacancy.  Energy differences yield the vacancy formation energy, a constrained drag of the vacancy along a next‑nearest‑neighbor path gives the NNN migration barrier, and a step‑by‑step drag through the {110} six‑jump cycle produces the energy‑displacement curve from which the highest barrier is extracted.  Second, molecular dynamics (constant temperature, NVT ensemble) is run at 1200 K on a smaller periodic cell containing a single Ni vacancy.  Atomic trajectories are recorded throughout the simulation, and all diffusion events are identified and classified into the categories used in the original experimental analysis: six‑jump cycles (uninterrupted, interrupted, and their {110} fraction), ten‑jump cycles (uninterrupted and interrupted), fourteen‑jump cycles, failed attempts returning to the original configuration (involving one, two, or more than two atoms), and any other unclassified events.  The raw counts are converted to percentages that sum to 100 %.

## Reproduction target
Produce two scored artifacts:

- `/app/outputs/static_energies.json`:  a JSON object containing the Ni vacancy formation energy (eV), the NNN migration energy (eV), and the peak barrier of the {110} six‑jump cycle (eV).
- `/app/outputs/md_statistics.json`: a JSON object reporting the percentage breakdown of all diffusion events observed during at least 1.5 ns of MD at 1200 K, using the categories `six_jump_cycles_total_percent`, `six_jump_cycles_uninterrupted_percent`, `six_jump_cycles_interrupted_percent`, `six_jump_110_of_six_jump_percent`, `ten_jump_cycles_percent`, `ten_jump_cycles_uninterrupted_percent`, `fourteen_jump_cycles_percent`, `failed_attempts_1atom_percent`, `failed_attempts_2atom_percent`, `failed_attempts_more2_percent`, and `other_percent`.  The percentages must sum to 100 %.

The exact numerical values are not prescribed; they emerge from the computations with the specified potential and protocol.

## Assets

- EAM potential for NiAl (Farkas et al. 1995): https://www.ctcms.nist.gov/potentials/
- LAMMPS molecular dynamics simulator: https://lammps.org

## Workflow steps

### Step 1: Compute static activation energies
- Role: scored
- Action: Set up a 9x9x9 unit cell B2 NiAl block with periodic boundary conditions using the EAM potential. Perform molecular statics (energy minimization) to compute the Ni vacancy formation energy (energy difference between relaxed perfect crystal and relaxed crystal with one Ni vacancy), the NNN migration energy (highest barrier along the NNN jump path), and the energy-displacement curve for the {110} six-jump cycle, reporting the highest barrier (third jump in the cycle).
- Output file: `/app/outputs/static_energies.json`
- Format: json
- Contract: { "ni_vacancy_formation_energy_eV": float, "ni_vacancy_nnn_migration_energy_eV": float, "six_jump_cycle_peak_barrier_eV": float }
- Scoring: scored by hidden verifier

### Step 2: Run molecular dynamics of Ni vacancy at 1200 K
- Role: process
- Action: Set up a 5x5x5 unit cell B2 NiAl block (125 unit cells, 249 atoms) with one Ni vacancy and periodic boundary conditions, using the equilibrium lattice parameter at 1200 K. Run constant-temperature MD (NVT) with a 2 fs time step for at least 750,000 steps (1.5 ns). Track atomic trajectories frequently enough (every 50-100 steps during cycles) to identify diffusion events. Save the trajectory as a log or trajectory file for later analysis.
- Evidence: `/app/outputs/md_trajectory.log`

### Step 3: Classify diffusion events and compute statistics
- Role: scored (load-bearing)
- Action: Analyze the MD trajectory to detect and classify all diffusion events (six-jump, ten-jump, fourteen-jump cycles, failed attempts, other), count their occurrences, and compute the percentage breakdown of event types for a Ni vacancy at 1200 K. Use the event definitions and categories as described in the paper's Table 2. Report results in JSON, ensuring the percentages sum to 100%.
- Output file: `/app/outputs/md_statistics.json`
- Format: json
- Contract: { "six_jump_cycles_total_percent": float, "six_jump_cycles_uninterrupted_percent": float, "six_jump_cycles_interrupted_percent": float, "six_jump_110_of_six_jump_percent": float, "ten_jump_cycles_percent": float, "ten_jump_cycles_uninterrupted_percent": float, "fourteen_jump_cycles_percent": float, "failed_attempts_1atom_percent": float, "failed_attempts_2atom_percent": float, "failed_attempts_more2_percent": float, "other_percent": float }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_energies.json`
- `/app/outputs/md_statistics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_energies.json
- path: `/app/outputs/static_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed Ni vacancy formation energy, NNN migration energy, and peak barrier of the {110} six-jump cycle, all in eV.
- schema:
  - `type`: object
  - `required`:
    - `ni_vacancy_formation_energy_eV`: float
    - `ni_vacancy_nnn_migration_energy_eV`: float
    - `six_jump_cycle_peak_barrier_eV`: float

### md_statistics.json
- path: `/app/outputs/md_statistics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Percentage breakdown of diffusion event types for a Ni vacancy at 1200 K; percentages must sum to 100.
- schema:
  - `type`: object
  - `required`:
    - `six_jump_cycles_total_percent`: float
    - `six_jump_cycles_uninterrupted_percent`: float
    - `six_jump_cycles_interrupted_percent`: float
    - `six_jump_110_of_six_jump_percent`: float
    - `ten_jump_cycles_percent`: float
    - `ten_jump_cycles_uninterrupted_percent`: float
    - `fourteen_jump_cycles_percent`: float
    - `failed_attempts_1atom_percent`: float
    - `failed_attempts_2atom_percent`: float
    - `failed_attempts_more2_percent`: float
    - `other_percent`: float

Notes: All static energies must be computed using the provided EAM potential and molecular statics. MD percentages must be computed from a trajectory of at least 1.5 ns at 1200 K. The breakdown categories follow the paper's classification (Table 2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ni_vacancy_formation_energy_eV": "float",
          "ni_vacancy_nnn_migration_energy_eV": "float",
          "six_jump_cycle_peak_barrier_eV": "float"
        }
      },
      "description": "Computed Ni vacancy formation energy, NNN migration energy, and peak barrier of the {110} six-jump cycle, all in eV."
    },
    {
      "file": "md_statistics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "six_jump_cycles_total_percent": "float",
          "six_jump_cycles_uninterrupted_percent": "float",
          "six_jump_cycles_interrupted_percent": "float",
          "six_jump_110_of_six_jump_percent": "float",
          "ten_jump_cycles_percent": "float",
          "ten_jump_cycles_uninterrupted_percent": "float",
          "fourteen_jump_cycles_percent": "float",
          "failed_attempts_1atom_percent": "float",
          "failed_attempts_2atom_percent": "float",
          "failed_attempts_more2_percent": "float",
          "other_percent": "float"
        }
      },
      "description": "Percentage breakdown of diffusion event types for a Ni vacancy at 1200 K; percentages must sum to 100."
    }
  ],
  "notes": "All static energies must be computed using the provided EAM potential and molecular statics. MD percentages must be computed from a trajectory of at least 1.5 ns at 1200 K. The breakdown categories follow the paper's classification (Table 2)."
}
```

## How you are scored
A hidden verifier independently evaluates the two scored artifacts.  For each artifact, the verifier compares the reported numbers to reference values that represent the expected outcome of the computational protocol.  The comparison tolerates small deviations due to implementation details (e.g., minimization algorithm, thermostat settings) and stochastic run‑to‑run variation in the MD simulations.  Each artifact receives a score that is then combined with the other (the main activation energies and the primary event categories carry higher weight) to produce an overall reward between 0 and 1.  Simply returning plausible numbers without executing the actual statics and dynamics computations is unlikely to yield a high reward because the verifier expects values consistent with a genuine re‑run of the specified steps.
