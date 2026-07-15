# First-principles thermodynamics and phonon stability of high-pressure gold fluorides

## Problem background
Gold (Au) is typically found in the +3 oxidation state in its compounds, but under high pressure it may adopt unusual valence states such as +2, +4, and +6 through reactions with fluorine. Determining the stable crystal structures and pressure-dependent stability of binary Au–F compounds (AuF₂, AuF₃, AuF₄, AuF₆) is fundamental for understanding high-pressure gold chemistry. This task computes the ground-state phases, the pressures at which phase transitions occur, the accompanying volume collapse, and the amount of charge transferred from gold to fluorine (Bader charge). It also checks whether the predicted stable phases are dynamically stable by analyzing their phonon spectra. The goal is to assess whether these exotic valence states and structures are thermodynamically and dynamically viable under compression.

## Approach
The reproduction uses open-source density functional theory (DFT) and lattice dynamics tools. Candidate crystal structures are manually built from the reported space-group symmetries and bonding motifs, then relaxed at a grid of pressures using Quantum ESPRESSO with the PBE exchange-correlation functional. From the relaxed total energies, the enthalpy per formula unit is computed to identify the lowest-energy (ground-state) phase at each pressure and to locate any pressure-induced phase transitions. For the AuF₃ compound, the volume collapse at the transition is quantified. At a fixed pressure of 20 GPa, Bader charge analysis is performed on the charge density to extract the net charge on the gold atom. Finally, phonon dispersion curves are calculated via the finite-displacement method using the PHONOPY package, and inspected for imaginary modes that would indicate dynamical instability.

## Reproduction target
Produce a JSON file (`results.json`) with the following quantities for each stoichiometry:
- AuF₂: ground-state phase, lower and upper transition pressures (GPa), Bader charge on Au (e).
- AuF₃: ground-state phase, transition pressure (GPa), volume collapse at the transition (%), Bader charge on Au (e).
- AuF₄: ground-state phase, lower and upper transition pressures (GPa), Bader charge on Au (e).
- AuF₆: ground-state phase, Bader charge on Au (e).

Additionally, produce a `phonon_stability.json` file that for each claimed stable phase (AuF₂ Pnma, AuF₃ Cmc2₁, AuF₄ C2/c, AuF₆ R-3) reports a boolean `no_imaginary_modes` indicating whether the phonon dispersion contains no imaginary frequencies. The reported numbers must be computed by following the outlined protocol; they should reflect the outcome of a faithfully executed workflow with the specified open-source tools.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Prepare initial structures and DFT input files
- Role: process
- Action: Construct initial crystal structures for the candidate phases (AuF₂ Pnma, AuF₃ P6₁22 and Cmc2₁, AuF₄ C2/c, AuF₆ R-3) from their space-group descriptions and the paper's bonding motifs. Generate Quantum ESPRESSO input files for each structure at a set of target pressures (e.g., 0, 5, 10, 15, 20, 25, 30, 40 GPa). Select appropriate pseudopotentials, k-point grids, and energy cutoffs.
- Evidence: `/app/outputs/prepared_inputs_summary.json`

### Step 2: Run DFT structural optimizations
- Role: process
- Action: For each phase and each pressure, perform full variable-cell relaxation using Quantum ESPRESSO. Ensure convergence of forces and stress. Save final relaxed structures (total energies and geometries).
- Evidence: `/app/outputs/relaxation_summary.json`

### Step 3: Thermodynamic stability and Bader analysis
- Role: scored (load-bearing)
- Action: From the relaxed structures and total energies, compute enthalpy per formula unit at each pressure. Determine the ground-state phase at each pressure and identify transition pressures. Calculate the volume collapse at the AuF₃ P6₁22 → Cmc2₁ transition. For structures relaxed at 20 GPa, perform Bader charge analysis and extract the net charge on Au atoms. Assemble all results into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"AuF2": {"ground_state_phase": "string", "transition_pressure_lower": null or number, "transition_pressure_upper": number, "Bader_charge_au": number}, "AuF3": {"ground_state_phase": "string", "transition_pressure": number, "volume_collapse_percent": number, "Bader_charge_au": number}, "AuF4": {"ground_state_phase": "string", "transition_pressure_lower": null or number, "transition_pressure_upper": number, "Bader_charge_au": number}, "AuF6": {"ground_state_phase": "R-3", "Bader_charge_au": number}}
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion calculations
- Role: process
- Action: For each claimed stable phase at a representative pressure within its stability range (e.g., AuF₃ Cmc2₁ at 10 GPa, AuF₂ Pnma at 20 GPa, AuF₄ C2/c at 20 GPa, AuF₆ R-3 at 20 GPa), construct supercells and compute phonon dispersions using PHONOPY with a finite-displacement approach, obtaining Hellmann–Feynman forces from Quantum ESPRESSO.
- Evidence: `/app/outputs/phonon_calculations_summary.json`

### Step 5: Dynamical stability check
- Role: scored
- Action: Inspect the phonon dispersion curves for each phase. Verify that no imaginary (negative) frequencies exist across the entire Brillouin zone. Report a boolean 'true' if the phase is dynamically stable. Save results to a JSON file.
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: {"AuF2_Pnma": {"no_imaginary_modes": boolean}, "AuF3_Cmc2_1": {"no_imaginary_modes": boolean}, "AuF4_C2c": {"no_imaginary_modes": boolean}, "AuF6_R-3": {"no_imaginary_modes": boolean}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/phonon_stability.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed thermodynamic properties (ground-state phases, transition pressures, volume collapse) and Bader charges for Au-F compounds; compared to paper-reported values within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `AuF2`:
      - `type`: object
      - `required`:
        - `ground_state_phase`: string
        - `transition_pressure_lower`: number or null
        - `transition_pressure_upper`: number
        - `Bader_charge_au`: number
    - `AuF3`:
      - `type`: object
      - `required`:
        - `ground_state_phase`: string
        - `transition_pressure`: number
        - `volume_collapse_percent`: number
        - `Bader_charge_au`: number
    - `AuF4`:
      - `type`: object
      - `required`:
        - `ground_state_phase`: string
        - `transition_pressure_lower`: number or null
        - `transition_pressure_upper`: number
        - `Bader_charge_au`: number
    - `AuF6`:
      - `type`: object
      - `required`:
        - `ground_state_phase`: string
        - `Bader_charge_au`: number
  - `units`:
    - `transition_pressure`: GPa
    - `volume_collapse_percent`: %
    - `Bader_charge_au`: e

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Boolean dynamical stability report for each phase; true means no imaginary phonon modes.
- schema:
  - `type`: object
  - `required`:
    - `AuF2_Pnma`:
      - `no_imaginary_modes`: boolean
    - `AuF3_Cmc2_1`:
      - `no_imaginary_modes`: boolean
    - `AuF4_C2c`:
      - `no_imaginary_modes`: boolean
    - `AuF6_R-3`:
      - `no_imaginary_modes`: boolean

Notes: The original paper used VASP; this reproduction uses Quantum ESPRESSO with PBE pseudopotentials. Code-to-code differences are absorbed by generous tolerances in the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "AuF2": {
            "type": "object",
            "required": {
              "ground_state_phase": "string",
              "transition_pressure_lower": "number or null",
              "transition_pressure_upper": "number",
              "Bader_charge_au": "number"
            }
          },
          "AuF3": {
            "type": "object",
            "required": {
              "ground_state_phase": "string",
              "transition_pressure": "number",
              "volume_collapse_percent": "number",
              "Bader_charge_au": "number"
            }
          },
          "AuF4": {
            "type": "object",
            "required": {
              "ground_state_phase": "string",
              "transition_pressure_lower": "number or null",
              "transition_pressure_upper": "number",
              "Bader_charge_au": "number"
            }
          },
          "AuF6": {
            "type": "object",
            "required": {
              "ground_state_phase": "string",
              "Bader_charge_au": "number"
            }
          }
        },
        "units": {
          "transition_pressure": "GPa",
          "volume_collapse_percent": "%",
          "Bader_charge_au": "e"
        }
      },
      "description": "Computed thermodynamic properties (ground-state phases, transition pressures, volume collapse) and Bader charges for Au-F compounds; compared to paper-reported values within tolerance."
    },
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "AuF2_Pnma": {
            "no_imaginary_modes": "boolean"
          },
          "AuF3_Cmc2_1": {
            "no_imaginary_modes": "boolean"
          },
          "AuF4_C2c": {
            "no_imaginary_modes": "boolean"
          },
          "AuF6_R-3": {
            "no_imaginary_modes": "boolean"
          }
        }
      },
      "description": "Boolean dynamical stability report for each phase; true means no imaginary phonon modes."
    }
  ],
  "notes": "The original paper used VASP; this reproduction uses Quantum ESPRESSO with PBE pseudopotentials. Code-to-code differences are absorbed by generous tolerances in the hidden grading specification."
}
```

## How you are scored
Each scored artifact is evaluated by a hidden verifier that compares your computed results against reference values from the scientific literature. The verifier checks that the reported ground-state phases are correct, that transition pressures and volume collapse fall within an acceptable margin, that Bader charges are physically plausible, and that each phase claimed to be stable has no imaginary phonon modes. A reward is computed as a weighted sum over the individual stages of the workflow. Simply reporting literature values without performing the calculations will not yield a high score, because the verifier expects the quantitative outcome of a genuine re-execution of the protocol. The exact reference values and tolerances are not disclosed.
