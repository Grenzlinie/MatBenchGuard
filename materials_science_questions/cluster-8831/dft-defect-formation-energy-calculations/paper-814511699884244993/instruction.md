# CaZn2N2 Nitride Semiconductor DFT Properties Reproduction

## Problem background
Nitride semiconductors are attractive for electronics and optoelectronics because they can be formed from earth‑abundant elements and possess favourable electronic properties. However, the commercialized nitrides are largely limited to GaN and its alloys. High‑throughput first‑principles screening has been used to identify previously unreported ternary zinc nitride semiconductors with small carrier effective masses and tunable bandgaps. This task reproduces the computational predictions for one of the most promising candidates, CaZn2N2. Using density functional theory (DFT), you must determine its ground‑state crystal structure, verify its stability, and compute its direct bandgap, carrier effective masses, and formation energy.

## Approach
The reproduction follows a multi‑stage computational workflow using publicly available, open‑source tools. First, an evolutionary algorithm (e.g., USPEX or CALYPSO) searches for the lowest‑energy crystal structure of CaZn2N2, evaluating candidate structures with the PBE‑GGA exchange‑correlation functional via Quantum ESPRESSO. The best structure is then fully relaxed (cell parameters and atomic positions) and its phonon density of states is computed with Phonopy to confirm the absence of imaginary vibrational modes, establishing dynamical stability. To assess thermodynamic stability, the formation energy per atom is calculated relative to the convex hull of competing phases (from the Materials Project) using PBE‑GGA. Finally, the electronic structure is refined with the HSE06 screened hybrid functional: the direct bandgap is obtained from the band structure, and the hole and electron effective masses are extracted by quadratic fitting of the band edges near the valence band maximum and conduction band minimum. The entire pipeline runs with Quantum ESPRESSO and PseudoDojo pseudopotentials, ensuring that the computations are fully reproducible with open‑source software.

## Reproduction target
Determine the ground‑state crystal structure of CaZn2N2, verify its dynamical and thermodynamic stability, and compute the following four quantitative properties for that structure:

- direct bandgap (eV)
- hole effective mass (in units of the free‑electron rest mass m₀)
- electron effective mass (in m₀)
- formation energy per atom (meV/atom)

Collect these values into a single JSON file named `step_01_properties.json` with the schema:
```json
{
  "direct_bandgap_eV": number,
  "hole_effective_mass_m0": number,
  "electron_effective_mass_m0": number,
  "formation_energy_meV_per_atom": number
}
```
All quantities must originate from the DFT workflow described above; simply looking up the values is not sufficient.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- USPEX evolutionary crystal structure prediction code: http://uspex-team.org/
- PseudoDojo pseudopotentials: http://www.pseudo-dojo.org/
- Materials Project database: https://materialsproject.org/
- Inorganic Crystal Structure Database (ICSD)

## Workflow steps

### Step 1: Crystal Structure Prediction
- Role: process
- Action: Use an evolutionary algorithm crystal structure prediction code (e.g., USPEX or CALYPSO) to search for the ground-state crystal structure of CaZn2N2. Generate candidate structures with up to 4 formula units per cell, relax them using the PBE-GGA functional via Quantum ESPRESSO, and identify the lowest-energy structure.
- Evidence: `/app/outputs/predicted_structure.json`

### Step 2: Geometry Optimization and Phonon Stability
- Role: process
- Action: Fully relax the predicted CaZn2N2 structure (atomic positions and cell parameters) using PBE-GGA with Quantum ESPRESSO. Compute the phonon density of states using Phonopy to verify the absence of imaginary modes, confirming dynamical stability.
- Evidence: `/app/outputs/phonon_stability.txt`

### Step 3: Formation Energy Calculation
- Role: process
- Action: Calculate the formation energy per atom of the relaxed CaZn2N2 structure relative to the convex hull of competing phases (Ca, Zn, binary and ternary nitrides from the Materials Project) using PBE-GGA. The result will show whether the structure is thermodynamically stable or slightly metastable (within 50 meV/atom above the hull).
- Evidence: `/app/outputs/formation_energy.json`

### Step 4: Electronic Structure (HSE06)
- Role: process
- Action: Perform HSE06 hybrid functional electronic structure calculations on the relaxed CaZn2N2 structure using Quantum ESPRESSO. Compute the direct bandgap and the hole and electron effective masses by quadratic fitting of the band edges near the VBM and CBM with fine k-point sampling.
- Evidence: `/app/outputs/electronic_structure.json`

### Step 5: Assemble Final Properties
- Role: scored (load-bearing)
- Action: Collect the computed direct bandgap (eV), hole effective mass (m₀), electron effective mass (m₀), and formation energy (meV/atom) into a JSON file.
- Output file: `/app/outputs/step_01_properties.json`
- Format: json
- Contract: {"direct_bandgap_eV": number, "hole_effective_mass_m0": number, "electron_effective_mass_m0": number, "formation_energy_meV_per_atom": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_properties.json
- path: `/app/outputs/step_01_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted properties of the ground-state structure of CaZn2N2: direct bandgap, hole effective mass, electron effective mass, and formation energy per atom. Values must be obtained from the DFT workflow steps above.
- schema:
  - `type`: object
  - `required`:
    - `direct_bandgap_eV`: number
    - `hole_effective_mass_m0`: number
    - `electron_effective_mass_m0`: number
    - `formation_energy_meV_per_atom`: number
  - `units`:
    - `direct_bandgap_eV`: eV
    - `hole_effective_mass_m0`: free-electron rest mass (m0)
    - `electron_effective_mass_m0`: free-electron rest mass (m0)
    - `formation_energy_meV_per_atom`: meV per atom

Notes: The agent must execute all process steps to obtain the properties. The checker will compare each reported quantity to hidden gold values with directional tolerances that reward meeting or exceeding the paper's quality (e.g., smaller effective mass, more negative formation energy).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "direct_bandgap_eV": "number",
          "hole_effective_mass_m0": "number",
          "electron_effective_mass_m0": "number",
          "formation_energy_meV_per_atom": "number"
        },
        "units": {
          "direct_bandgap_eV": "eV",
          "hole_effective_mass_m0": "free-electron rest mass (m0)",
          "electron_effective_mass_m0": "free-electron rest mass (m0)",
          "formation_energy_meV_per_atom": "meV per atom"
        }
      },
      "description": "Predicted properties of the ground-state structure of CaZn2N2: direct bandgap, hole effective mass, electron effective mass, and formation energy per atom. Values must be obtained from the DFT workflow steps above."
    }
  ],
  "notes": "The agent must execute all process steps to obtain the properties. The checker will compare each reported quantity to hidden gold values with directional tolerances that reward meeting or exceeding the paper's quality (e.g., smaller effective mass, more negative formation energy)."
}
```

## How you are scored
A hidden verifier independently examines your submitted `step_01_properties.json` and compares each reported quantity against hidden reference values. The comparison is directional: results that meet or exceed the quality expected for a good semiconductor (e.g., smaller effective masses, more stable formation energy) will receive full credit; degradation relative to the reference will reduce the score. Reporting numbers without running the pipeline will not yield a passing score.
