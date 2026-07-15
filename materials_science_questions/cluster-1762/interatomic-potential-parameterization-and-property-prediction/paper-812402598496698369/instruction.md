# Lattice-Dynamical Reproduction of Raman Phonon Frequencies in HgBa2CuO4

## Problem background
The vibrational properties of HgBa2CuO4, including the Raman-active phonon frequencies, are important for understanding the role of phonons in high-temperature superconductivity. Measuring or predicting the pressure dependence of these modes provides insight into charge transfer and bond stiffness changes. This task asks you to compute the zone-center Raman-active phonon frequencies of HgBa2CuO4 at ambient pressure and the pressure evolution of the apical-oxygen A1g mode using an unscreened rigid-ion model.

## Approach
Use an unscreened rigid-ion model where the interatomic potential consists of a long-range Coulomb part with effective charges and a short-range Born-Mayer repulsion with element-specific radii. The parameters are fully specified. Obtain the tetragonal crystal structure in space group P4/mmm from a published pressure-dependent diffraction study. Construct the dynamical matrix at the Brillouin-zone Gamma point by summing over all atom pairs, diagonalize it, and assign the Raman-active modes (A1g and Eg) using factor group analysis or eigenvector inspection. For the pressure sweep, use the pressure-dependent lattice constants (linearly extrapolated to 7.5 GPa) and recompute the Gamma-point frequencies, isolating the apical-oxygen A1g mode.

## Reproduction target
Compute the four Raman-active zone-center phonon frequencies of HgBa2CuO4 at ambient pressure (Ba A1g, Ba Eg, O(2) Eg, and O(2) A1g) and write them to `ambient_raman_frequencies.csv`. Then compute the O(2) A1g (apical-oxygen) mode frequency for a series of pressures from 0 to 7.5 GPa, using at least 8 pressure points, and write the results to `pressure_raman_O_A_A1g.csv`. The output files must follow the exact column schemas and units specified in the workflow steps.

## Assets

- Crystal structure of HgBa2CuO4 under pressure (Hunter et al., 1994): 10.1016/0921-4534(94)90776-X

## Workflow steps

### Step 1: Obtain crystal structure data
- Role: process
- Action: Retrieve the crystal structure of HgBa2CuO4 (space group P4/mmm) from Hunter et al., Physica C 221 (1994) 1. Extract atomic positions and lattice constants a and c at ambient pressure and at several pressures up to 0.6 GPa. Create a linear extrapolation of a and c up to 7.5 GPa for use in the pressure-dependent calculation.
- Evidence: `/app/outputs/lattice_params_extrapolation.json`

### Step 2: Compute ambient-pressure Raman-active phonon frequencies
- Role: scored
- Action: Implement the unscreened rigid-ion model with parameters Z(k) and R(k) given in the paper (Hg Z=0.77 R=0.105, Ba Z=1.45 R=0.214, Cu Z=1.70 R=0.139, O Z=-1.325 R=0.173, with a=1822 eV, b=12.364, e2/4piE0=144 eV/nm). Using the ambient-pressure crystal structure, construct the dynamical matrix at the Gamma point, diagonalize, identify the Raman-active modes (A1g and Eg) via group theory or eigenvector analysis, and report frequencies for Ba A1g, Ba Eg, O(2) Eg, and O(2) A1g (apical oxygen).
- Output file: `/app/outputs/ambient_raman_frequencies.csv`
- Format: csv
- Contract: mode (string), frequency_cm1 (float)
- Scoring: scored by hidden verifier

### Step 3: Compute pressure dependence of apical-oxygen A1g Raman mode
- Role: scored (load-bearing)
- Action: Using the same rigid-ion model and the pressure-dependent lattice constants (extrapolated to 7.5 GPa from step 1), compute the O(2) A1g (apical-oxygen) mode frequency for a series of pressures from 0 to 7.5 GPa (at least 8 points). Output a CSV with pressure and frequency.
- Output file: `/app/outputs/pressure_raman_O_A_A1g.csv`
- Format: csv
- Contract: pressure_GPa (float), frequency_cm1 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ambient_raman_frequencies.csv`
- `/app/outputs/pressure_raman_O_A_A1g.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ambient_raman_frequencies.csv
- path: `/app/outputs/ambient_raman_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ambient-pressure Raman-active phonon frequencies. Each row gives a mode label (e.g., 'Ba A1g') and its computed frequency in inverse centimeters.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `frequency_cm1`
  - `units`:
    - `frequency_cm1`: cm^{-1}

### pressure_raman_O_A_A1g.csv
- path: `/app/outputs/pressure_raman_O_A_A1g.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pressure dependence of the O_A A1g Raman mode frequency. Must contain frequency values at a series of pressures from 0 to 7.5 GPa, with strictly increasing frequency as pressure rises. A hidden check also verifies the frequency at a specific pressure.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `frequency_cm1`
  - `units`:
    - `pressure_GPa`: GPa
    - `frequency_cm1`: cm^{-1}

Notes: Ambient frequencies are scored by comparing the computed values to hidden reference values within a tolerance. The pressure file is scored by checking that the frequency increases monotonically with pressure across all reported points, and that a hidden pressure point has the expected frequency (exact_match within tolerance).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ambient_raman_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "frequency_cm1"
        ],
        "units": {
          "frequency_cm1": "cm^{-1}"
        }
      },
      "description": "Ambient-pressure Raman-active phonon frequencies. Each row gives a mode label (e.g., 'Ba A1g') and its computed frequency in inverse centimeters."
    },
    {
      "file": "pressure_raman_O_A_A1g.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "frequency_cm1"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "frequency_cm1": "cm^{-1}"
        }
      },
      "description": "Pressure dependence of the O_A A1g Raman mode frequency. Must contain frequency values at a series of pressures from 0 to 7.5 GPa, with strictly increasing frequency as pressure rises. A hidden check also verifies the frequency at a specific pressure."
    }
  ],
  "notes": "Ambient frequencies are scored by comparing the computed values to hidden reference values within a tolerance. The pressure file is scored by checking that the frequency increases monotonically with pressure across all reported points, and that a hidden pressure point has the expected frequency (exact_match within tolerance)."
}
```

## How you are scored
A hidden verifier will inspect each output artifact independently. For the ambient frequencies, it compares your computed mode frequencies against reference values derived from the rigid-ion model. For the pressure file, it checks that the reported frequencies exhibit a monotonic increase with pressure (structural consistency) and also verifies the frequency at a specific, hidden pressure. The verifier combines these checks into an overall reward score, weighting the ambient frequencies and pressure trend proportionally. To earn full credit, your implementation must faithfully execute the rigid-ion lattice dynamics — simply writing numbers found elsewhere is not sufficient.
