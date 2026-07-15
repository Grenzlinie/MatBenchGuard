# Phonon-based dynamical stability analysis of ternary iron-halide noble-gas compounds

## Problem background
The terrestrial abundance anomalies of helium and xenon suggest the existence of deep-Earth reservoirs of these noble gases. A recent computational study proposed that several ternary iron-halide compounds could sequester He and Xe by being thermodynamically and dynamically stable under moderate pressures (below 60 GPa). This task investigates whether first-principles calculations can confirm the stability of these candidate compounds.

## Approach
We use density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional. Total energies are computed for the five candidate ternary compounds (FeF₂He, FeF₃He, FeF₂Xe, FeF₃Xe, FeCl₃Xe) and for all relevant reference phases of the constituent elements and binaries at their corresponding pressures. Formation energies per formula unit are then derived by subtracting the appropriate reference energies. Phonon calculations are performed via the finite-displacement or density-functional perturbation theory (DFPT) method to obtain the full phonon dispersion; the absence of imaginary modes (allowing for small numerical noise) indicates dynamical stability.

## Reproduction target
Using open-source DFT and phonon tools, compute the formation energies and dynamical stability of the five ternary iron-halide noble-gas compounds at their reported stable pressures. Specifically, produce (1) a JSON file with the DFT total energy and formation energy (eV/f.u.) for each compound, and (2) a JSON file indicating whether each compound is dynamically stable and its minimum phonon frequency. The full P–T phase diagram construction and melting simulations are not required; only the static stability quantities are scored.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- phonopy: https://phonopy.github.io/phonopy/
- PseudoDojo pseudopotentials (standard accuracy): http://www.pseudo-dojo.org/
- Crystal structures of ternary compounds and reference phases: 10.1063/5.0164149

## Workflow steps

### Step 1: Obtain crystal structures
- Role: process
- Action: Download or extract from the public supplementary material (Table S3) the crystal structures of the five ternary compounds (FeF2He, FeF3He, FeF2Xe, FeF3Xe, FeCl3Xe) and the required reference binary and elemental phases (FeF2, FeF3, FeCl3, solid He, Xe, Fe, F, Cl) at the specified pressures (e.g., 60 GPa for Fe-F-Xe compounds, 65 GPa for FeCl3Xe).
- Evidence: `/app/outputs/input_structures.json`

### Step 2: Perform DFT and phonon calculations
- Role: process
- Action: Using Quantum ESPRESSO with PBE functional and PseudoDojo pseudopotentials, relax the structures and compute total energies for all ternary and reference phases. Compute phonon force constants for the five ternary compounds via DFPT or finite displacement. Ensure adequate k-point sampling and energy cutoffs.
- Evidence: `/app/outputs/dft_output.json`

### Step 3: Compute formation energies
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute the formation energy per formula unit for each ternary compound using the appropriate reference phases. Output the total energy and formation energy for each compound.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {
  "FeF2He": { "total_energy_computed": <float>, "formation_energy_eV_per_fu": <float> },
  "FeF3He": { ... },
  "FeF2Xe": { ... },
  "FeF3Xe": { ... },
  "FeCl3Xe": { ... }
}
- Scoring: scored by hidden verifier

### Step 4: Assess dynamical stability
- Role: scored
- Action: Using phonopy, compute the phonon dispersion and density of states for each ternary compound. Determine the minimum phonon frequency across the Brillouin zone. Report whether each compound is dynamically stable (no imaginary modes, allowing for small numerical noise < -5 cm⁻¹).
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: {
  "FeF2He": { "dynamically_stable": <boolean>, "minimum_frequency_cm-1": <float> },
  "FeF3He": { ... },
  "FeF2Xe": { ... },
  "FeF3Xe": { ... },
  "FeCl3Xe": { ... }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/phonon_stability.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent-computed total energies and formation energies per formula unit for the five ternary compounds.
- schema:
  - `type`: object
  - `required`:
    - `FeF2He`: object with total_energy_computed (eV) and formation_energy_eV_per_fu
    - `FeF3He`: object with total_energy_computed (eV) and formation_energy_eV_per_fu
    - `FeF2Xe`: object with total_energy_computed (eV) and formation_energy_eV_per_fu
    - `FeF3Xe`: object with total_energy_computed (eV) and formation_energy_eV_per_fu
    - `FeCl3Xe`: object with total_energy_computed (eV) and formation_energy_eV_per_fu
  - `units`:
    - `total_energy_computed`: eV
    - `formation_energy_eV_per_fu`: eV per formula unit

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Dynamical stability verdict and minimum phonon frequency for each ternary compound.
- schema:
  - `type`: object
  - `required`:
    - `FeF2He`: object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)
    - `FeF3He`: object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)
    - `FeF2Xe`: object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)
    - `FeF3Xe`: object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)
    - `FeCl3Xe`: object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)
  - `units`:
    - `minimum_frequency_cm-1`: cm⁻¹
    - `dynamically_stable`: boolean (true if no imaginary modes, allowing for small numerical noise)

Notes: The formation energies are recomputed by the checker from the agent's total energies using hidden reference total energies and compared to the paper's reported formation energies with a tolerance. Phonon stability is checked by verifying that minimum_frequency_cm-1 > -5 cm⁻¹ and dynamically_stable is true for all compounds.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "FeF2He": "object with total_energy_computed (eV) and formation_energy_eV_per_fu",
          "FeF3He": "object with total_energy_computed (eV) and formation_energy_eV_per_fu",
          "FeF2Xe": "object with total_energy_computed (eV) and formation_energy_eV_per_fu",
          "FeF3Xe": "object with total_energy_computed (eV) and formation_energy_eV_per_fu",
          "FeCl3Xe": "object with total_energy_computed (eV) and formation_energy_eV_per_fu"
        },
        "units": {
          "total_energy_computed": "eV",
          "formation_energy_eV_per_fu": "eV per formula unit"
        }
      },
      "description": "Agent-computed total energies and formation energies per formula unit for the five ternary compounds."
    },
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "FeF2He": "object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)",
          "FeF3He": "object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)",
          "FeF2Xe": "object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)",
          "FeF3Xe": "object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)",
          "FeCl3Xe": "object with dynamically_stable (boolean) and minimum_frequency_cm-1 (float)"
        },
        "units": {
          "minimum_frequency_cm-1": "cm⁻¹",
          "dynamically_stable": "boolean (true if no imaginary modes, allowing for small numerical noise)"
        }
      },
      "description": "Dynamical stability verdict and minimum phonon frequency for each ternary compound."
    }
  ],
  "notes": "The formation energies are recomputed by the checker from the agent's total energies using hidden reference total energies and compared to the paper's reported formation energies with a tolerance. Phonon stability is checked by verifying that minimum_frequency_cm-1 > -5 cm⁻¹ and dynamically_stable is true for all compounds."
}
```

## How you are scored
A hidden verifier independently scores each scored output file. For formation energies, the verifier recomputes the formation energy from your reported total energies using hidden reference total energies and compares the result to a paper-derived target value. For dynamical stability, it checks that the minimum frequency is above a small negative threshold to account for numerical noise and that the stability flag is true for all compounds. The final reward is a weighted sum of these stage scores. You must produce the values yourself; merely reporting the paper's numbers is not sufficient.
