# Phonon instability of K8Si46 clathrate at high pressure

## Problem background
The structural stability of type-I K8Si46 clathrate under high pressure has been investigated experimentally, revealing an isostructural phase transition and pressure-induced amorphization. Ab initio phonon band structure calculations have been used to explore the microscopic mechanism behind these observations. In this reproduction task, you will compute the phonon dispersion and Hellmann-Feynman forces for K8Si46 at 16 GPa to determine the stability of the guest K atoms in the large cages.

## Approach
The computational method is based on density functional theory (DFT) using the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation (GGA) and a plane-wave pseudopotential approach. The crystal structure of K8Si46 is the type-I clathrate (space group Pm-3n, lattice constant 10.275 Å) with atomic positions taken from published crystallographic data. First, a variable-cell geometry optimization is performed at a fixed external pressure of 16 GPa to obtain the relaxed structure. Then, the phonon dispersion is computed via density functional perturbation theory (DFPT) at the same pressure, and the lowest phonon frequency across the Brillouin zone is extracted. In a separate calculation, the Hellmann-Feynman force acting on a K atom at its high-symmetry site (1/4, 1/2, 0) in the large cage is computed along the b crystallographic axis. The workflow is implemented with an open-source DFT code and standard pseudopotentials.

## Reproduction target
Using an open-source DFT code (e.g., Quantum ESPRESSO), set up the K8Si46 structure from public data and perform geometry optimization at 16 GPa. Compute the phonon dispersion via DFPT and determine the minimum phonon frequency (in cm⁻¹) across the entire Brillouin zone. Save this value as a JSON object with key 'minimum_frequency' in the file `phonon_frequencies_16GPa.json`. Additionally, from the optimized structure, compute the Hellmann-Feynman force (in eV/Å) on the K atom at (1/4, 1/2, 0) along the b direction and save it as a JSON object with key 'force' in `force_on_K_16GPa.json`. The reported numbers must be the result of your own calculations; do not copy values from any external source.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE GGA pseudopotentials for K and Si: https://www.quantum-espresso.org/pseudopotentials
- K8Si46 crystal structure

## Workflow steps

### Step 1: Geometry optimization at 16 GPa
- Role: process
- Action: Set up the K8Si46 structure (space group Pm-3n, lattice constant 10.275 Å, atomic positions from public sources). Perform a DFT variable-cell geometry optimization at a fixed pressure of 16 GPa to obtain the relaxed structure for subsequent steps.
- Evidence: `/app/outputs/step_01_optimization.log`

### Step 2: Phonon dispersion and minimum frequency
- Role: scored (load-bearing)
- Action: Using the relaxed structure from step 1, perform a phonon dispersion calculation with density functional perturbation theory (DFPT) at 16 GPa. Determine the lowest phonon frequency across the Brillouin zone and write it to the output file. A negative value indicates an imaginary mode (dynamical instability).
- Output file: `/app/outputs/phonon_frequencies_16GPa.json`
- Format: json
- Contract: {"minimum_frequency": <float>}
- Scoring: scored by hidden verifier

### Step 3: Hellmann-Feynman force on K atom
- Role: scored
- Action: Using the relaxed structure from step 1, perform a single-point DFT calculation with the K atom at its high-symmetry site (1/4, 1/2, 0) in the large cage. Compute the Hellmann-Feynman force acting on that K atom along the b crystallographic axis and write it to the output file.
- Output file: `/app/outputs/force_on_K_16GPa.json`
- Format: json
- Contract: {"force": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies_16GPa.json`
- `/app/outputs/force_on_K_16GPa.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies_16GPa.json
- path: `/app/outputs/phonon_frequencies_16GPa.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reproduce the phonon instability: minimum phonon frequency of K8Si46 at 16 GPa. A negative value indicates imaginary modes.
- schema:
  - `type`: object
  - `required`: `minimum_frequency`
  - `properties`:
    - `minimum_frequency`:
      - `type`: number
      - `description`: Lowest phonon frequency across the Brillouin zone, in cm⁻¹

### force_on_K_16GPa.json
- path: `/app/outputs/force_on_K_16GPa.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Verify the off-center stabilization: force on the K atom at its symmetry site (1/4, 1/2, 0) along the b direction.
- schema:
  - `type`: object
  - `required`: `force`
  - `properties`:
    - `force`:
      - `type`: number
      - `description`: Hellmann-Feynman force on the K atom along the b axis, in eV/Å

Notes: The task reproduces the computational evidence for a phonon-driven isostructural transition. The scored quantities are the minimum phonon frequency and the on-site force, both at 16 GPa. Tolerances will be applied to account for code/pseudopotential differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies_16GPa.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "minimum_frequency"
        ],
        "properties": {
          "minimum_frequency": {
            "type": "number",
            "description": "Lowest phonon frequency across the Brillouin zone, in cm⁻¹"
          }
        }
      },
      "description": "Reproduce the phonon instability: minimum phonon frequency of K8Si46 at 16 GPa. A negative value indicates imaginary modes."
    },
    {
      "file": "force_on_K_16GPa.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "force"
        ],
        "properties": {
          "force": {
            "type": "number",
            "description": "Hellmann-Feynman force on the K atom along the b axis, in eV/Å"
          }
        }
      },
      "description": "Verify the off-center stabilization: force on the K atom at its symmetry site (1/4, 1/2, 0) along the b direction."
    }
  ],
  "notes": "The task reproduces the computational evidence for a phonon-driven isostructural transition. The scored quantities are the minimum phonon frequency and the on-site force, both at 16 GPa. Tolerances will be applied to account for code/pseudopotential differences."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the two output artifacts and compares your reported numbers to a hidden reference derived from published results. Each artifact is assessed by matching the numeric value within an appropriate tolerance; the final reward is a weighted combination of the two scores. The verifier does not re-run your calculations: it only inspects the final reported numbers. Therefore, you must execute the full computational workflow and report the values you obtain.
