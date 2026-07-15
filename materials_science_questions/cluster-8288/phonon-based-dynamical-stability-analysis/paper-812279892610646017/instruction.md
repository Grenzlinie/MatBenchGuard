# Reproducing pressure-induced isostructural phase transition in a nitride superlattice via density functional theory

## Problem background
Isostructural phase transitions (IPTs) are rare phase transitions that preserve the crystal symmetry, making them challenging to characterize and detect. In nitride superlattices, it has been proposed that hydrostatic pressure can drive a continuous or discontinuous change from a wurtzite-derived structure to an h-derived structure without altering the space group. The 1x1 GaN/ScN superlattice is predicted to exhibit such an IPT, potentially showing a second-order character, and is associated with dramatic changes in structural parameters, a soft A1(TO) phonon mode, and anomalous piezoelectric behavior. Reproducing the key structural, dynamical, and piezoelectric signatures for this system provides a rigorous test of the first-principles prediction.

## Approach
Use first-principles density functional theory (DFT) within the local density approximation (LDA) to perform total-energy calculations and geometry optimizations for the 1x1 GaN/ScN superlattice (space group P3m1) at a series of fixed volumes that span pressures from about 0 to 20 GPa. For each volume, relax all structural degrees of freedom (in-plane lattice constant, axial ratio c/a, internal parameters u for Ga-N and Sc-N bonds) to locate the minimum-energy configuration. From the total energies and volumes, fit a Birch-Murnaghan equation of state to obtain pressure, enthalpy, and volume relations. Analyze the structural data to determine the pressure at which the isostructural phase transition between the wurtzite-derived and h-derived states occurs, and verify the order of the transition by examining the continuity of the volume change. Perform density functional perturbation theory (DFPT) calculations to compute the zone-center A1(TO) phonon frequency at several pressures around the transition, checking for soft-mode behavior. Use the Berry-phase method to compute spontaneous polarization, and apply finite strains with internal coordinate relaxations to obtain the piezoelectric coefficient e33 at ambient pressure.

## Reproduction target
Compute the structural parameters (c/a ratio, internal parameters <u_GaN> and <u_ScN>, volume per 4 atoms) as a function of hydrostatic pressure for the 1x1 GaN/ScN superlattice, covering pressures from 0 to 20 GPa. Provide sufficient resolution near the transition to resolve the continuous change. Determine the pressure at which the isostructural phase transition occurs between the wurtzite-derived and h-derived states, and confirm whether the volume changes continuously (second-order character) or discontinuously. Calculate the zone-center A1(TO) phonon frequency at several pressures around the transition, and compute the e33 piezoelectric coefficient at ambient pressure. Report all quantities in the specified output files (step_01_structural_properties.csv, step_02_transition_pressure.txt, step_03_piezoelectric_e33.txt, step_04_phonon_frequency.csv).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ABINIT: https://www.abinit.org/
- Pseudopotential libraries (SSSP/PseudoDojo/HGH): https://www.materialscloud.org/discover/sssp/
- Python scientific stack (numpy, scipy, matplotlib): numpy, scipy, matplotlib

## Workflow steps

### Step 1: Superlattice model construction
- Role: process
- Action: Build the atomic structure of the 1×1 GaN/ScN superlattice (space group P3m1, stacking along [0001]) using the lattice vectors and atomic positions of the parent compounds. Generate input geometry files suitable for DFT calculations.
- Evidence: none

### Step 2: DFT total-energy and geometry relaxations
- Role: process
- Action: Run LDA-DFT calculations for the 1×1 GaN/ScN superlattice at a series of fixed volumes spanning pressures from approximately 0 to 20 GPa (at least 10 volume points). For each volume, relax all structural degrees of freedom (in-plane lattice constant a, axial ratio c/a, internal coordinates u) to obtain the minimum-energy configuration. Use a plane-wave basis set with standard pseudopotentials and k-point sampling sufficient to converge total energies and forces.
- Evidence: `/app/outputs/dft_energy_volume.dat`

### Step 3: Structural properties vs pressure
- Role: scored (load-bearing)
- Action: From the DFT results, fit a Birch-Murnaghan equation of state to compute pressure as a function of volume. Compile a table of the axial ratio c/a, the layer-averaged internal parameters ⟨u_GaN⟩ and ⟨u_ScN⟩, and the volume per 4 atoms at a grid of pressures covering 0–20 GPa, with sufficient resolution near the transition.
- Output file: `/app/outputs/step_01_structural_properties.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), c_over_a (float), u_ScN (float), u_GaN (float), volume_per4atoms_Bohr3 (float).
- Scoring: scored by hidden verifier

### Step 4: Transition pressure determination
- Role: scored
- Action: Analyze the structural data (e.g., enthalpy crossing or inflection point of c/a vs pressure) to determine the pressure at which the isostructural phase transition occurs between the wurtzite-derived and h-derived states. Verify that the volume changes continuously to confirm the second-order nature.
- Output file: `/app/outputs/step_02_transition_pressure.txt`
- Format: txt
- Contract: A single float value of the transition pressure in GPa.
- Scoring: scored by hidden verifier

### Step 5: DFPT phonon calculations
- Role: process
- Action: Using the relaxed structures at several pressures near the transition (e.g., 8, 10, 11, 12, 14 GPa), perform density functional perturbation theory (DFPT) calculations to obtain the zone-center phonon frequencies, focusing on the A1(TO) mode.
- Evidence: `/app/outputs/phonon_calc.log`

### Step 6: A1(TO) phonon frequency vs pressure
- Role: scored
- Action: Extract the zone-center A1(TO) phonon frequency at each pressure where DFPT was performed. Report the frequencies in a table.
- Output file: `/app/outputs/step_04_phonon_frequency.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), A1_TO_frequency_cm-1 (float).
- Scoring: scored by hidden verifier

### Step 7: Berry-phase polarization and piezoelectric coefficient
- Role: process
- Action: Compute spontaneous polarization using the Berry-phase method for the relaxed structure at ambient pressure (~0 GPa). Apply finite strains and relax internal coordinates to compute the strain derivative of polarization, obtaining the piezoelectric coefficient e33.
- Evidence: `/app/outputs/piezo_calc.out`

### Step 8: Piezoelectric coefficient e33
- Role: scored
- Action: Report the e33 piezoelectric coefficient at ambient pressure in C/m² for the 1×1 GaN/ScN superlattice.
- Output file: `/app/outputs/step_03_piezoelectric_e33.txt`
- Format: txt
- Contract: A single float value in C/m².
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_properties.csv`
- `/app/outputs/step_02_transition_pressure.txt`
- `/app/outputs/step_03_piezoelectric_e33.txt`
- `/app/outputs/step_04_phonon_frequency.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_properties.csv
- path: `/app/outputs/step_01_structural_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Structural parameters (axial ratio, internal u parameters, volume per 4 atoms) of the 1×1 GaN/ScN superlattice as a function of hydrostatic pressure.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `c_over_a`, `u_ScN`, `u_GaN`, `volume_per4atoms_Bohr3`
  - `units`:
    - `pressure_GPa`: GPa
    - `c_over_a`: dimensionless
    - `u_ScN`: dimensionless
    - `u_GaN`: dimensionless
    - `volume_per4atoms_Bohr3`: Bohr^3

### step_02_transition_pressure.txt
- path: `/app/outputs/step_02_transition_pressure.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: The pressure at which the isostructural phase transition occurs in 1×1 GaN/ScN, determined from enthalpy crossing or inflection point analysis.
- schema:
  - `type`: text
  - `description`: A single float value representing the transition pressure in GPa.

### step_03_piezoelectric_e33.txt
- path: `/app/outputs/step_03_piezoelectric_e33.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Piezoelectric coefficient e33 of the 1×1 GaN/ScN superlattice at ambient pressure (~0 GPa).
- schema:
  - `type`: text
  - `description`: A single float value representing the e33 piezoelectric coefficient in C/m².

### step_04_phonon_frequency.csv
- path: `/app/outputs/step_04_phonon_frequency.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zone-center A1(TO) phonon frequency of the 1×1 GaN/ScN superlattice at several pressures near the transition, showing soft-mode behavior.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `A1_TO_frequency_cm-1`
  - `units`:
    - `pressure_GPa`: GPa
    - `A1_TO_frequency_cm-1`: cm^{-1}

Notes: All scored outputs must be derived from the DFT/DFPT calculations. The structural properties table must show a continuous structural transition with axial ratio and internal parameters changing as pressure increases. The transition pressure should be determined from the structural data (e.g., inflection point or equation-of-state analysis). The phonon frequency should soften to a minimum near the transition. The piezoelectric coefficient should be reported at ambient pressure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "c_over_a",
          "u_ScN",
          "u_GaN",
          "volume_per4atoms_Bohr3"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "c_over_a": "dimensionless",
          "u_ScN": "dimensionless",
          "u_GaN": "dimensionless",
          "volume_per4atoms_Bohr3": "Bohr^3"
        }
      },
      "description": "Structural parameters (axial ratio, internal u parameters, volume per 4 atoms) of the 1×1 GaN/ScN superlattice as a function of hydrostatic pressure."
    },
    {
      "file": "step_02_transition_pressure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single float value representing the transition pressure in GPa."
      },
      "description": "The pressure at which the isostructural phase transition occurs in 1×1 GaN/ScN, determined from enthalpy crossing or inflection point analysis."
    },
    {
      "file": "step_03_piezoelectric_e33.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single float value representing the e33 piezoelectric coefficient in C/m²."
      },
      "description": "Piezoelectric coefficient e33 of the 1×1 GaN/ScN superlattice at ambient pressure (~0 GPa)."
    },
    {
      "file": "step_04_phonon_frequency.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "A1_TO_frequency_cm-1"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "A1_TO_frequency_cm-1": "cm^{-1}"
        }
      },
      "description": "Zone-center A1(TO) phonon frequency of the 1×1 GaN/ScN superlattice at several pressures near the transition, showing soft-mode behavior."
    }
  ],
  "notes": "All scored outputs must be derived from the DFT/DFPT calculations. The structural properties table must show a continuous structural transition with axial ratio and internal parameters changing as pressure increases. The transition pressure should be determined from the structural data (e.g., inflection point or equation-of-state analysis). The phonon frequency should soften to a minimum near the transition. The piezoelectric coefficient should be reported at ambient pressure."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. Each scored output file is independently checked against expected results derived from the paper's findings (hidden gold). For the structural properties table, the verifier compares your computed c/a, u parameters, and volume at given pressures to reference data. The transition pressure is extracted from your data (e.g., via equation-of-state fitting or inflection point analysis) and compared to a hidden reference value. The phonon frequencies are checked for the expected softening trend near the transition and compared to reference values at specific pressures. The piezoelectric coefficient e33 is compared to a reference value at ambient pressure. The final score is a weighted combination of these checks. Merely reporting pre-existing values without genuinely executing the calculations is detectable and will result in low scores.
