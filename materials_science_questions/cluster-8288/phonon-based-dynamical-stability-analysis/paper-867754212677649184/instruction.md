# First-principles electronic structure and phonon stability analysis of a Heusler superconductor

## Problem background
The Heusler compound ZrNi2Ga has been proposed as a candidate for superconductivity. First-principles electronic structure calculations suggest that a van Hove singularity in the band structure near the L-point can strongly enhance the density of states at the Fermi level, potentially raising the superconducting transition temperature. This task reproduces those calculations to verify the existence and energy position of the van Hove singularity, and to compute the phonon dispersion to assess whether the crystal structure is dynamically stable.

## Approach
Use first-principles density functional theory (DFT) with the GGA-PBE exchange-correlation functional and an open-source plane-wave code (Quantum ESPRESSO). The crystal adopts the cubic L2₁ Heusler structure (space group Fm-3m). Start from the experimental lattice constant, then perform a variable-cell relaxation to obtain the equilibrium geometry. From the relaxed structure, run a self-consistent field calculation to get the ground-state charge density and wavefunctions. Post-process the results to compute the electronic band structure along high-symmetry directions, paying special attention to the L-point, and generate the total density of states. Identify the van Hove singularity and extract its energy offset relative to the Fermi level and the DOS at the Fermi level. For the phonon calculation, use either density-functional perturbation theory or the finite-displacement method (Phonopy) to compute the full phonon dispersion and determine the minimum frequency; flag the presence of any imaginary modes that would indicate lattice instability.

## Reproduction target
Perform the full first-principles workflow for ZrNi2Ga and produce two JSON output files under /app/outputs:

1) dos_and_band_analysis.json – containing the energy offset of the van Hove singularity at the L-point from the Fermi level (in meV), the electronic density of states at the Fermi level (in states per eV per formula unit), and a boolean indicating whether the singularity is present at the L-point.

2) phonon_frequencies.json – containing the minimum phonon frequency across the Brillouin zone (in cm⁻¹) and a boolean indicating whether any imaginary phonon modes exist.

The target is to compute these values from the DFT simulations, not to retrieve them from the literature.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP efficiency PBE pseudopotentials (Zr, Ni, Ga): https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of ZrNi2Ga

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT variable-cell relaxation of the ZrNi2Ga cubic L2₁ structure using a GGA-PBE functional to obtain the equilibrium lattice parameter and atomic positions. Save the relaxed structure for subsequent steps.
- Evidence: `/app/outputs/step1_optimization.log`

### Step 2: SCF calculation
- Role: process
- Action: Perform a self-consistent field DFT calculation on the relaxed structure to obtain ground-state charge density, wavefunctions, and forces. Save the output for later use.
- Evidence: `/app/outputs/step2_scf.log`

### Step 3: Electronic structure analysis
- Role: scored
- Action: Using the SCF charge density, compute the band structure along a high-symmetry path (including the L-point) and the total density of states. Identify the van Hove singularity at the L-point and extract its energy relative to the Fermi level (in meV) and the DOS at the Fermi level (states/eV per formula unit). Write the results to dos_and_band_analysis.json.
- Output file: `/app/outputs/dos_and_band_analysis.json`
- Format: json
- Contract: {"vhs_energy_relative_to_fermi_meV": number, "dos_at_fermi_states_per_eV_formula_unit": number, "vhs_present_at_L_point": boolean}
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion and stability
- Role: scored (load-bearing)
- Action: Using the forces from the SCF calculation, compute the phonon dispersion via density functional perturbation theory (or finite-displacement method) within the harmonic approximation. Determine the minimum phonon frequency (in cm⁻¹) across the Brillouin zone and whether any imaginary modes exist. Output the results to phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: {"minimum_phonon_frequency_cm-1": number, "imaginary_modes_present": boolean}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_and_band_analysis.json`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_and_band_analysis.json
- path: `/app/outputs/dos_and_band_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic structure analysis results: energy offset of the van Hove singularity at the L-point relative to the Fermi level (meV), electronic density of states at the Fermi level (states/eV per formula unit), and a boolean indicating whether the singularity is present at the L-point.
- schema:
  - `type`: object
  - `required`:
    - `vhs_energy_relative_to_fermi_meV`: number
    - `dos_at_fermi_states_per_eV_formula_unit`: number
    - `vhs_present_at_L_point`: boolean

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon dispersion results: the minimum phonon frequency (cm⁻¹) across the Brillouin zone, and a boolean indicating whether any imaginary (negative) phonon modes exist.
- schema:
  - `type`: object
  - `required`:
    - `minimum_phonon_frequency_cm-1`: number
    - `imaginary_modes_present`: boolean

Notes: The checker extracts the reported VHS energy offset and compares it to the paper's reference value with a hidden tolerance; it verifies that the minimum phonon frequency is positive (dynamical stability).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_and_band_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "vhs_energy_relative_to_fermi_meV": "number",
          "dos_at_fermi_states_per_eV_formula_unit": "number",
          "vhs_present_at_L_point": "boolean"
        }
      },
      "description": "Electronic structure analysis results: energy offset of the van Hove singularity at the L-point relative to the Fermi level (meV), electronic density of states at the Fermi level (states/eV per formula unit), and a boolean indicating whether the singularity is present at the L-point."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "minimum_phonon_frequency_cm-1": "number",
          "imaginary_modes_present": "boolean"
        }
      },
      "description": "Phonon dispersion results: the minimum phonon frequency (cm⁻¹) across the Brillouin zone, and a boolean indicating whether any imaginary (negative) phonon modes exist."
    }
  ],
  "notes": "The checker extracts the reported VHS energy offset and compares it to the paper's reference value with a hidden tolerance; it verifies that the minimum phonon frequency is positive (dynamical stability)."
}
```

## How you are scored
A hidden verifier inspects each workflow stage's output artifact independently. It checks that the submitted JSON files contain the required fields and that the reported numeric values and boolean flags fall within expected tolerances (details are hidden). The final reward is a weighted combination of the scores from the electronic structure stage and the phonon stage. Submitting pre-recorded numbers without executing the actual DFT and phonon calculations will not pass the verification, because the checker's criteria are based on re-computed quantities and structural checks.
