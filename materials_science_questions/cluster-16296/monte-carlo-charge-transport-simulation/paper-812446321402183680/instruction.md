# Microscopic Scattering at a GaAs-AlGaAs (111) Heterojunction

## Problem background
Semiconductor heterojunctions such as GaAs-AlGaAs are the building blocks of quantum well and superlattice devices. The standard effective-mass approximation assumes that electron states on both sides of the junction have simple parabolic bands, but at atomic-scale dimensions this assumption may break down. A key open question is whether evanescent (non-propagating) waves on the alloy side significantly alter the reflection properties of an electron incident on the interface. This task investigates that question using a microscopic scattering calculation.

## Approach
The computational method combines empirical pseudopotentials with the layer method. Bulk band structures for GaAs and AlxGa1-xAs are first generated at zero in-plane wavevector (k_parallel=0) to obtain the full set of propagating Bloch and evanescent states over a range of energies near the band gap. The interface is taken to be the (111) plane with the interatomic spacing set to the GaAs lattice constant. The pseudopotential parameters for GaAs and AlAs are taken from standard solid-state literature. For each alloy composition, each bulk state is expanded in plane waves; wave-function continuity across the interface is enforced, and the resulting linear equations are solved to yield the complex amplitudes of all transmitted, reflected, and evanescent waves. The reflection coefficient for an electron incident from the GaAs side in the Γ1 valley at k_parallel=0 takes the form R = exp(i φ), and the phase shift φ is extracted as a function of energy above the GaAs Γ1 minimum. Additionally, the amplitudes of the Γ1- and L1-derived evanescent states on the alloy side are recorded, and the valence-band discontinuity is obtained from the difference in the bulk valence-band maxima. The effective-mass prediction is computed for comparison using the alloy-composition-dependent effective masses, providing a baseline against which the full empirical-pseudopotential results are assessed.

## Reproduction target
Produce three CSV files under /app/outputs: (1) valence_discontinuity.csv with columns x and discontinuity_eV for x = 0, 0.25, 0.5, 0.75, 1.0. (2) phase_shifts.csv with columns x, energy_above_Gamma1_eV, phi_rad for each alloy composition x in [0.25, 0.5, 0.75, 1.0] and at least the energies 0.0, 0.05, 0.1, 0.15, 0.2 eV. (3) evanescent_amplitudes.csv with columns x, state, energy_above_Gamma1_eV, amplitude for x = 0.5 and x = 1.0, with state being either 'Gamma1' or 'L1', at the same energy points. The goal is to obtain these quantities from first-principles empirical-pseudopotential calculations without relying on effective-mass theory.

## Assets

- GaAs and AlAs empirical pseudopotential form factors
- GaAs lattice constant (5.65325 Å)

## Workflow steps

### Step 1: Bulk Bandstructure Generation
- Role: process
- Action: Compute the bulk bandstructures and the complete set of propagating Bloch and evanescent states for GaAs and AlxGa1-xAs using empirical pseudopotentials and the layer method. Do this for a range of energies around the band gap and for in-plane wavevector k_parallel=0. The interface plane is (111) and the interatomic spacing is set equal to the GaAs lattice constant.
- Evidence: `/app/outputs/bulk_states.json`

### Step 2: Valence Band Discontinuity
- Role: scored
- Action: Extract valence band maxima from the bulk bandstructures and compute the valence band discontinuity as a function of Al mole fraction x. Output the results for x = 0, 0.25, 0.5, 0.75, 1.0.
- Output file: `/app/outputs/valence_discontinuity.csv`
- Format: csv
- Contract: x, discontinuity_eV
- Scoring: scored by hidden verifier

### Step 3: Interface Matching
- Role: process
- Action: For each alloy composition x and a set of electron energies E above the Γ1 minimum, expand each bulk state in plane waves, enforce wavefunction continuity at the interface, and solve the resulting linear equations to obtain complex amplitudes (reflection, transmission, evanescent coefficients). Verify current conservation and wavefunction symmetry constraints.
- Evidence: `/app/outputs/matching_checks.json`

### Step 4: Reflection Phase Shifts
- Role: scored (load-bearing)
- Action: From the solved complex amplitudes, extract the phase shift φ of the reflection coefficient (R = exp(iφ) for k_parallel=0). Write results for each alloy concentration x and a set of energies 0–0.2 eV above the GaAs Γ1 minimum.
- Output file: `/app/outputs/phase_shifts.csv`
- Format: csv
- Contract: x, energy_above_Gamma1_eV, phi_rad
- Scoring: scored by hidden verifier

### Step 5: Evanescent Wave Amplitudes
- Role: scored
- Action: From the solved amplitudes, extract the absolute amplitudes of the Γ1- and L1-derived evanescent waves on the alloy side for x=0.5 and x=1.0. Write results for each energy.
- Output file: `/app/outputs/evanescent_amplitudes.csv`
- Format: csv
- Contract: x, state, energy_above_Gamma1_eV, amplitude
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/valence_discontinuity.csv`
- `/app/outputs/phase_shifts.csv`
- `/app/outputs/evanescent_amplitudes.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### valence_discontinuity.csv
- path: `/app/outputs/valence_discontinuity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Valence band discontinuity as a function of Al mole fraction x, computed from bulk bandstructures.
- schema:
  - `type`: table
  - `required_columns`: `x`, `discontinuity_eV`
  - `units`:
    - `discontinuity_eV`: eV

### phase_shifts.csv
- path: `/app/outputs/phase_shifts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reflection coefficient phase shift φ (rad) for electron incident at k_parallel=0 on the (111) GaAs-AlGaAs heterojunction.
- schema:
  - `type`: table
  - `required_columns`: `x`, `energy_above_Gamma1_eV`, `phi_rad`
  - `units`:
    - `energy_above_Gamma1_eV`: eV
    - `phi_rad`: rad

### evanescent_amplitudes.csv
- path: `/app/outputs/evanescent_amplitudes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Absolute amplitudes of Γ1- and L1-derived evanescent waves on the alloy side for x=0.5 and x=1.0.
- schema:
  - `type`: table
  - `required_columns`: `x`, `state`, `energy_above_Gamma1_eV`, `amplitude`
  - `units`:
    - `energy_above_Gamma1_eV`: eV
    - `amplitude`: 

Notes: All comparison uses the reference_match policy: the hidden checker compares submitted values against paper-digitized curves with tolerances specified in the hidden grading spec. The phase_shifts output is load-bearing; genuine execution of the bulk-state generation and interface matching is required to produce correct phase shifts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "valence_discontinuity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "discontinuity_eV"
        ],
        "units": {
          "discontinuity_eV": "eV"
        }
      },
      "description": "Valence band discontinuity as a function of Al mole fraction x, computed from bulk bandstructures."
    },
    {
      "file": "phase_shifts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "energy_above_Gamma1_eV",
          "phi_rad"
        ],
        "units": {
          "energy_above_Gamma1_eV": "eV",
          "phi_rad": "rad"
        }
      },
      "description": "Reflection coefficient phase shift φ (rad) for electron incident at k_parallel=0 on the (111) GaAs-AlGaAs heterojunction."
    },
    {
      "file": "evanescent_amplitudes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "state",
          "energy_above_Gamma1_eV",
          "amplitude"
        ],
        "units": {
          "energy_above_Gamma1_eV": "eV",
          "amplitude": ""
        }
      },
      "description": "Absolute amplitudes of Γ1- and L1-derived evanescent waves on the alloy side for x=0.5 and x=1.0."
    }
  ],
  "notes": "All comparison uses the reference_match policy: the hidden checker compares submitted values against paper-digitized curves with tolerances specified in the hidden grading spec. The phase_shifts output is load-bearing; genuine execution of the bulk-state generation and interface matching is required to produce correct phase shifts."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored artifacts. The verifier compares your computed values to reference results derived from the original investigation using appropriate tolerances. The phase shifts carry the largest weight (0.5), evanescent amplitudes (0.3), and valence band discontinuity (0.2). Reporting numbers without genuine execution of the layer-method and interface-matching pipeline will not suffice, as the verification requires agreement across multiple alloy concentrations and energies that can only be obtained by faithfully following the described multi-step workflow. The final reward is a single number between 0 and 1, reflecting the weighted sum of the per-artifact scores.
