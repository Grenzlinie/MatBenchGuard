# First-principles Phonons and Thermodynamic Properties of a Ternary Chalcogenide

## Problem background
Cu₂GeSe₃ is a diamond-like ternary chalcogenide that exhibits an unexpectedly low lattice thermal conductivity, making it an interesting candidate for thermoelectric applications. The origin of this low conductivity—whether it stems from unusually strong bonding anharmonicity or from other factors—has been debated. Clarifying the lattice dynamics and thermodynamic properties of this material is essential to understanding its heat transport behavior. This task investigates those properties by computing the phonon spectrum, mode Grüneisen parameters, and the macroscopic Grüneisen parameter and lattice thermal conductivity at room temperature from first-principles.

## Approach
The approach is a computational one. Using density functional theory (DFT) with the generalized gradient approximation (PBE functional), you will relax the orthorhombic crystal structure of Cu₂GeSe₃ (space group Imm2). You will then employ the frozen-phonon finite-displacement method (implemented in the Phonopy package) with a supercell to compute the force constants and the phonon frequencies and eigenvectors at the equilibrium volume. To capture the volume dependence of the vibrational modes, you will repeat the phonon calculations at several strained volumes and derive the mode Grüneisen parameters. From these data you will (a) classify the Γ‑point optical phonons according to the C₂ᵥ point group and match them to approximate experimental Raman peak positions, and (b) compute thermodynamic properties within the quasi-harmonic approximation: the average Grüneisen parameter at 300 K is obtained by a mode-averaging weighted by mode heat capacities, and the lattice thermal conductivity at 300 K is estimated via Slack’s formula, using an experimental Debye temperature of 168 K.

## Reproduction target
Compute the following quantities for the orthorhombic Cu₂GeSe₃ crystal: (1) A list of Γ‑point Raman-active phonon frequencies (in cm⁻¹) paired with their symmetry assignments (A₁, A₂, B₁, or B₂), mapped to the experimental Raman peak positions reported in the literature (Marcano et al. 2008). (2) The average Grüneisen parameter (dimensionless) at 300 K and the lattice thermal conductivity (in W/m·K) at 300 K computed using Slack’s formula with the experimental Debye temperature of 168 K. The two results must be saved in the files `step_01_phonon_frequencies.json` and `step_02_thermodynamic_properties.json` as detailed in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- PBE pseudopotentials for Cu, Ge, Se: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: Relax the orthorhombic Cu₂GeSe₃ crystal structure (space group Imm2) using DFT with the PBE functional and appropriate pseudopotentials. Start from the experimental lattice parameters a=11.889 Å, b=4.052 Å, c=5.596 Å and the following fractional atomic coordinates (Wyckoff positions): Cu at 4c (0.168, 0, 0.262), Ge at 2b (0, 0.5, 0.734), Se₁ at 2a (0, 0, 0.009), Se₂ at 4c (0.329, 0, -0.003). Optimize ionic positions until forces are below a reasonable threshold. Provide the relaxed structure for subsequent phonon calculations.
- Evidence: none

### Step 2: Phonon dispersion at equilibrium volume
- Role: process
- Action: Using the relaxed structure, build a supercell containing 72 atoms and compute force constants via finite displacements with Phonopy. Use DFT (PBE) to calculate phonon frequencies and eigenvectors, sampling the Brillouin zone with a Γ-centred mesh. Extract the Γ‑point phonon frequencies and eigenvectors.
- Evidence: none

### Step 3: Volume‑dependent phonon calculations
- Role: process
- Action: Repeat the finite‑displacement phonon calculations at several volumes around equilibrium (by scaling the lattice constants) to obtain the volume derivatives of the phonon frequencies. Compute the mode Grüneisen parameters γₙ(q) according to γₙ(q) = −(V₀/ωₙ) ∂ωₙ/∂V.
- Evidence: none

### Step 4: Raman mode analysis
- Role: scored
- Action: Analyze the Γ‑point optical phonon frequencies and eigenvectors. Classify each mode according to the C₂ᵥ point group (A₁, A₂, B₁, B₂). Match each Γ‑point optical mode to the nearest experimental Raman peak reported for Cu₂GeSe₃ (Marcano et al. 2008) and assign symmetries. Write the results as an array of objects.
- Output file: `/app/outputs/step_01_phonon_frequencies.json`
- Format: json
- Contract: Array of objects, each with keys: peak_wavenumber (float, approximate experimental wavenumber in cm⁻¹), computed_frequency (float, calculated frequency in cm⁻¹), symmetry_label (string, e.g. A1, A2, B1, B2).
- Scoring: scored by hidden verifier

### Step 5: Thermodynamic property computation
- Role: scored (load-bearing)
- Action: From the equilibrium phonon frequencies and the volume-dependent data, compute: (a) the average Grüneisen parameter γ at 300 K by mode averaging (weighted by mode heat capacities), (b) the lattice thermal conductivity κ_L at 300 K using Slack’s formula with the experimental Debye temperature 168 K. Write the results as a JSON object.
- Output file: `/app/outputs/step_02_thermodynamic_properties.json`
- Format: json
- Contract: Object with required keys: gamma_300K (float, dimensionless), kappa_L_300K (float, W/m·K). Optional key: Cv_300K (float, J/g·K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_frequencies.json`
- `/app/outputs/step_02_thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_frequencies.json
- path: `/app/outputs/step_01_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Assignment of computed Γ‑point phonon frequencies (cm⁻¹) to the approximate experimental Raman peaks, with symmetry labels.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `peak_wavenumber`, `computed_frequency`, `symmetry_label`
    - `properties`:
      - `peak_wavenumber`:
        - `type`: number
        - `unit`: cm⁻¹
      - `computed_frequency`:
        - `type`: number
        - `unit`: cm⁻¹
      - `symmetry_label`:
        - `type`: string

### step_02_thermodynamic_properties.json
- path: `/app/outputs/step_02_thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Average Grüneisen parameter and lattice thermal conductivity of Cu₂GeSe₃ at 300 K, computed from the phonon data and Slack’s formula.
- schema:
  - `type`: object
  - `required`: `gamma_300K`, `kappa_L_300K`
  - `properties`:
    - `gamma_300K`:
      - `type`: number
      - `unit`: dimensionless
    - `kappa_L_300K`:
      - `type`: number
      - `unit`: W/m·K
    - `Cv_300K`:
      - `type`: number
      - `unit`: J/g·K

Notes: The phonon frequencies are compared against hidden experimental reference values with tolerances; symmetry assignments are accepted for all ambiguous peaks. Thermodynamic properties are compared against hidden reference values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "peak_wavenumber",
            "computed_frequency",
            "symmetry_label"
          ],
          "properties": {
            "peak_wavenumber": {
              "type": "number",
              "unit": "cm⁻¹"
            },
            "computed_frequency": {
              "type": "number",
              "unit": "cm⁻¹"
            },
            "symmetry_label": {
              "type": "string"
            }
          }
        }
      },
      "description": "Assignment of computed Γ‑point phonon frequencies (cm⁻¹) to the approximate experimental Raman peaks, with symmetry labels."
    },
    {
      "file": "step_02_thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma_300K",
          "kappa_L_300K"
        ],
        "properties": {
          "gamma_300K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "kappa_L_300K": {
            "type": "number",
            "unit": "W/m·K"
          },
          "Cv_300K": {
            "type": "number",
            "unit": "J/g·K"
          }
        }
      },
      "description": "Average Grüneisen parameter and lattice thermal conductivity of Cu₂GeSe₃ at 300 K, computed from the phonon data and Slack’s formula."
    }
  ],
  "notes": "The phonon frequencies are compared against hidden experimental reference values with tolerances; symmetry assignments are accepted for all ambiguous peaks. Thermodynamic properties are compared against hidden reference values with tolerances."
}
```

## How you are scored
A hidden verifier will independently score each of the two scored artifacts. For the phonon frequencies, the verifier compares each reported computed frequency to a hidden experimental reference Raman frequency; your assignment to the experimental peak is evaluated based on the frequency match. For the thermodynamic properties, the verifier compares your reported average Grüneisen parameter and lattice thermal conductivity to reference values. The final reward is a weighted combination of the per-artifact scores, with the thermodynamic properties carrying a substantial share and the phonon frequencies accounting for the remainder. Simply reporting the paper’s numbers is not sufficient—the verifier expects the results to fall within acceptable tolerances that reflect honest re-computation with a different code base.
