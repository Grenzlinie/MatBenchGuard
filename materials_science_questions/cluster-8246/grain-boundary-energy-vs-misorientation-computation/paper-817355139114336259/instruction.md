# Structural Vacancy Model for Tilt Grain Boundaries in Aluminum

## Problem background
Grain boundaries in polycrystalline metals control many material properties, yet predicting their stable atomic structure and grain‑boundary energy remains a long‑standing challenge. The coincidence site lattice (CSL) model provides an initial geometric framework but typically yields unrealistically high energies and no excess volume because some atoms near the boundary plane are under compression (interatomic distance smaller than equilibrium) while others are in loose regions (distance larger than equilibrium). An alternative approach introduces structural vacancies and additional atoms into the boundary region, followed by atomic relaxation, to obtain stable structures with significantly lower energy. This task applies such a structural vacancy model to the special Σ5(013)[100] tilt grain boundary in aluminum, which serves as a well‑characterized test case.

## Approach
The structural vacancy model proceeds in three stages.

1. **CSL bicrystal construction**: a bicrystal for the Σ5(013)[100] tilt boundary is built with the appropriate misorientation and cell dimensions.
2. **Vacancy relaxation**: additional atoms are introduced into regions where the interatomic distance exceeds 1.4 times the nearest‑neighbour distance (r₁) by extending atomic planes from one grain into the other. Then, for every pair of atoms whose distance is less than 0.7 r₁, one atom is removed from the core and the remaining atom is placed symmetrically in the grain boundary plane, forming a distributed vacancy. This step relieves compression and fills loose regions, producing a vacancy‑relaxed configuration.
3. **Atomic relaxation via molecular statics**: a gradient‑descent energy minimization is performed using an interatomic potential to obtain the final stable grain boundary structure. The task may use either the Morse pair potential with parameters for aluminum taken from Tsaregorodtsev et al. (1984), or the Cleri–Rosato many‑body potential with parameters from Cleri and Rosato (1993).

After each stage, the grain‑boundary energy (J m⁻²) is computed. The final energy after atomic relaxation is the primary quantity of interest.

## Reproduction target
Implement the full structural vacancy model for the Σ5(013)[100] tilt grain boundary in aluminum. Construct the initial CSL bicrystal, apply the vacancy‑relaxation protocol with the specified distance thresholds, and perform atomic relaxation using gradient descent with either the Morse or Cleri–Rosato potential. After each of the three stages (initial CSL, vacancy relaxation, atomic relaxation), compute the grain‑boundary energy in J m⁻². Save the results in a JSON file (`gb_energy_summary.json`) that records which potential was used and the three energies. The objective is the final relaxed energy; the intermediate energies document the relaxation history.

## Assets

- Aluminum fcc crystal structure and lattice parameter
- Morse pair potential parameters for aluminum from Tsaregorodtsev et al. (1984)
- Cleri-Rosato many-body potential parameters for aluminum: 10.1103/PhysRevB.48.22

## Workflow steps

### Step 1: Construct CSL bicrystal
- Role: process
- Action: Construct the initial bicrystal for the Σ5(013)[100] tilt grain boundary in fcc aluminum using the CSL model. Use rotation axis [100], misorientation angle 36.87°, crystal dimensions 80a × 20a × 40a (a = 4.05 Å), fixed boundaries in xOy and yOz, periodic in xOz. Save the atomic coordinates.
- Evidence: `/app/outputs/cs_bicrystal.xyz`

### Step 2: Vacancy relaxation
- Role: process
- Action: Apply the vacancy relaxation protocol: introduce additional atoms in regions where interatomic distance exceeds 1.4 r₁ (r₁ = nearest-neighbor distance) by extending atomic planes from one grain into the other; then, for every pair of atoms with distance less than 0.7 r₁, remove one atom from the core and place the remaining atom symmetrically in the grain boundary plane to form a distributed vacancy. Save the relaxed atomic coordinates.
- Evidence: `/app/outputs/vacancy_relaxed.xyz`

### Step 3: Atomic relaxation via molecular statics
- Role: process
- Action: Perform atomic relaxation using molecular statics (gradient descent) to minimize the grain‑boundary energy. Use either the Morse pair potential or the Cleri–Rosato many‑body potential. Shift atoms until convergence. Save the final relaxed atomic coordinates.
- Evidence: `/app/outputs/final_relaxed.xyz`

### Step 4: Record GB energies
- Role: scored (load-bearing)
- Action: After each of the three stages (initial CSL, vacancy relaxation, atomic relaxation), compute the grain‑boundary energy in J/m². Save the results in a JSON file indicating the potential used.
- Output file: `/app/outputs/gb_energy_summary.json`
- Format: json
- Contract: JSON object with keys: potential_type (string, either 'Morse' or 'Cleri_Rosato'), initial_CSL_energy_Jm2 (float), vacancy_relaxed_energy_Jm2 (float), final_energy_Jm2 (float). All energies in J/m².
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gb_energy_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gb_energy_summary.json
- path: `/app/outputs/gb_energy_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Summary of grain‑boundary energies after each construction stage. The checker will verify that final_energy_Jm2 ≤ hidden upper threshold (lower is better), that vacancy_relaxed_energy_Jm2 > final_energy_Jm2, and initial_CSL_energy_Jm2 > vacancy_relaxed_energy_Jm2.
- schema:
  - `type`: object
  - `required`:
    - `potential_type`: string
    - `initial_CSL_energy_Jm2`: float
    - `vacancy_relaxed_energy_Jm2`: float
    - `final_energy_Jm2`: float
  - `items`: object
  - `units`:
    - `initial_CSL_energy_Jm2`: J/m²
    - `vacancy_relaxed_energy_Jm2`: J/m²
    - `final_energy_Jm2`: J/m²

Notes: The checker enforces both absolute energy thresholds (monotonic with lower being better) and structural ordering (energy steadily decreases through the pipeline). The chosen potential must be stated, and the corresponding hidden thresholds are applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gb_energy_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "potential_type": "string",
          "initial_CSL_energy_Jm2": "float",
          "vacancy_relaxed_energy_Jm2": "float",
          "final_energy_Jm2": "float"
        },
        "items": {},
        "units": {
          "initial_CSL_energy_Jm2": "J/m²",
          "vacancy_relaxed_energy_Jm2": "J/m²",
          "final_energy_Jm2": "J/m²"
        }
      },
      "description": "Summary of grain‑boundary energies after each construction stage. The checker will verify that final_energy_Jm2 ≤ hidden upper threshold (lower is better), that vacancy_relaxed_energy_Jm2 > final_energy_Jm2, and initial_CSL_energy_Jm2 > vacancy_relaxed_energy_Jm2."
    }
  ],
  "notes": "The checker enforces both absolute energy thresholds (monotonic with lower being better) and structural ordering (energy steadily decreases through the pipeline). The chosen potential must be stated, and the corresponding hidden thresholds are applied."
}
```

## How you are scored
Your output is evaluated by a hidden verifier. The verifier reads `gb_energy_summary.json` and checks that the reported energies obey the expected hierarchy: initial CSL energy > vacancy‑relaxed energy > final energy. It then compares the energy values against a hidden reference that is based on the published results for the potential you chose. Meeting or exceeding the reference (i.e., final energy at or below the reference, with energy decreases that are at least as large as expected) earns full credit; larger deviations reduce the score. The verifier combines these checks into a final reward between 0.0 and 1.0. Note that simply reporting the correct reference numbers without executing the pipeline is insufficient—the verifier also performs structural sanity checks that require a genuine simulation output.
