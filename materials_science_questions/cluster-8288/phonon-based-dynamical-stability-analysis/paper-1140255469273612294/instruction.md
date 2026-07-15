# DFT phonon and ferroaxial switching simulation in RbFe(MoO4)2

## Problem background
Ferroaxial materials possess bistable orientational domains that are free from depolarizing or stray fields, making them promising for non-volatile data storage. However, switching ferroaxial order is challenging because conventional conjugate fields are difficult to engineer. This work proposes using circularly polarized terahertz (THz) pulses to resonantly drive a doubly degenerate phonon mode, creating an effective axial field via the cross product of the phonon displacement and the electric field. The computational study predicts that such excitation can deterministically switch ferroaxial domains in RbFe(MoO4)2 below its transition temperature, with a fluence threshold, and can transiently polarize the para-axial state above the transition. This task reproduces those computational predictions: first-principles phonon calculations and numerical integration of the coupled equations of motion to test whether the switching and polarization dynamics can be obtained from open-source tools.

## Approach
The reproduction relies on two computational stages. First, density functional theory (DFT) calculations are performed on the high-symmetry P-3m1 crystal structure of RbFe(MoO4)2 to obtain the phonon frequencies at the Gamma point, the double‑well potential along the ferroaxial soft mode, and the trilinear coupling constant α that couples the driven Eu phonon to the axial order parameter. These calculations use the LDA+U functional and are carried out with open‑source codes (Quantum ESPRESSO and Phonopy). Second, the computed parameters are inserted into a system of coupled ordinary differential equations that describe the dynamics of the driven phonon mode and the axial order parameter under a circularly polarized Gaussian THz pulse. The equations are integrated numerically for two distinct regimes: below the critical temperature Tc (180 K), where the potential is a double‑well, and above Tc (200 K), where the potential is a single‑well. The simulation explores a range of fluences to identify the switching threshold below Tc and records the transient axial polarization for both pulse helicities above Tc. The temperature dependence of the soft‑mode frequency is taken from published experimental data.

## Reproduction target
Produce the following six artifacts:
1. A CSV file listing the computed phonon mode labels and frequencies at the Gamma point, including the degenerate Eu mode and the unstable A2g soft mode.
2. A CSV file recording the energy vs. displacement along the A2g eigenvector, showing the double‑well potential profile.
3. A text file containing the single value of the trilinear coupling constant α in units of elementary charge per unit cell length (q_e/uÅ).
4. A CSV file with time series of the axial order parameter Q_A for multiple fluences (including 12.5, 14, and 20 mJ/cm²) when starting from an A+ domain at 180 K, using a right‑circular Gaussian pulse centered at 24 THz with 600 fs FWHM.
5. A text file reporting the lowest fluence (in mJ/cm²) at which the sign of Q_A inverts and remains in the opposite well after the pulse, extracted from the above simulation.
6. A CSV file with time traces of Q_A for both left‑circular and right‑circular polarization pulses at a fixed fluence of 6 mJ/cm² and a temperature of 200 K.

## Assets

- RbFe(MoO4)2 crystal structure (P-3m1)
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: DFT phonon frequencies
- Role: scored
- Action: Perform DFT structural relaxation of the high-temperature P-3m1 phase of RbFe(MoO4)2 using LDA+U and compute phonon frequencies at the Gamma point with Phonopy. Save mode labels and frequencies (at least Eu mode and A2g soft mode).
- Output file: `/app/outputs/step_01_phonon_frequencies.csv`
- Format: csv
- Contract: mode (string), frequency_THz (float)
- Scoring: scored by hidden verifier

### Step 2: Double-well potential
- Role: scored
- Action: Displace atomic positions along the unstable A2g eigenvector for a series of amplitudes, compute total energies, and record the double-well potential profile.
- Output file: `/app/outputs/step_02_double_well_potential.csv`
- Format: csv
- Contract: displacement_Angstrom (float), energy_eV (float)
- Scoring: scored by hidden verifier

### Step 3: Trilinear coupling constant
- Role: scored
- Action: Compute the off-diagonal mode effective charge tensor to obtain the trilinear coupling coefficient α between the Eu phonon and the A2g soft mode. Output the value in units of q_e/uÅ.
- Output file: `/app/outputs/step_03_coupling_constant.txt`
- Format: txt
- Contract: Single number: alpha (float)
- Scoring: scored by hidden verifier

### Step 4: Switching simulation below Tc
- Role: scored (load-bearing)
- Action: Using the computed Eu frequency, coupling constant α, and temperature-dependent soft mode frequency from literature, integrate the coupled ODEs for a circularly polarized Gaussian pulse (24 THz, 600 fs FWHM, various fluences including 12.5, 14, 20 mJ/cm²). Start from A+ domain at 180 K. Record time evolution of the axial order parameter Q_A for each fluence.
- Output file: `/app/outputs/step_04_switching_below_Tc.csv`
- Format: csv
- Contract: fluence_mJcm2 (float), time_ps (float), Q_A (float, arbitrary units)
- Scoring: scored by hidden verifier

### Step 5: Switching threshold fluence
- Role: scored
- Action: From the previous simulation, determine the lowest fluence at which the sign of Q_A inverts and remains in the opposite well after the pulse. Output the threshold in mJ/cm².
- Output file: `/app/outputs/step_05_threshold_fluence.txt`
- Format: txt
- Contract: Single number: threshold fluence in mJ/cm² (float)
- Scoring: scored by hidden verifier

### Step 6: Transient simulation above Tc
- Role: scored
- Action: Repeat ODE integration for para-axial state at 200 K with a fixed fluence of 6 mJ/cm². Simulate for left-circularly and right-circularly polarized pulses. Record time traces of Q_A for each helicity.
- Output file: `/app/outputs/step_06_transient_above_Tc.csv`
- Format: csv
- Contract: helicity (string: 'left' or 'right'), time_ps (float), Q_A (float, arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_frequencies.csv`
- `/app/outputs/step_02_double_well_potential.csv`
- `/app/outputs/step_03_coupling_constant.txt`
- `/app/outputs/step_04_switching_below_Tc.csv`
- `/app/outputs/step_05_threshold_fluence.txt`
- `/app/outputs/step_06_transient_above_Tc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_frequencies.csv
- path: `/app/outputs/step_01_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon mode labels and frequencies at Gamma point. Checker compares the Eu mode frequency to the paper's reference within tolerance.
- schema:
  - `required_columns`: `mode`, `frequency_THz`

### step_02_double_well_potential.csv
- path: `/app/outputs/step_02_double_well_potential.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy vs. displacement along the A2g soft mode. Checker verifies a double-well shape with two symmetric minima.
- schema:
  - `required_columns`: `displacement_Angstrom`, `energy_eV`

### step_03_coupling_constant.txt
- path: `/app/outputs/step_03_coupling_constant.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Single value for the trilinear coupling constant α. Checker compares to the paper's value within tolerance.
- schema:
  - `type`: text
  - `units`: q_e/uÅ

### step_04_switching_below_Tc.csv
- path: `/app/outputs/step_04_switching_below_Tc.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of Q_A for each fluence below Tc. Checker verifies sign reversal above a threshold fluence.
- schema:
  - `required_columns`: `fluence_mJcm2`, `time_ps`, `Q_A`

### step_05_threshold_fluence.txt
- path: `/app/outputs/step_05_threshold_fluence.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Switching threshold fluence extracted from the simulation. Checker compares to the paper's threshold within tolerance.
- schema:
  - `type`: text
  - `units`: mJ/cm²

### step_06_transient_above_Tc.csv
- path: `/app/outputs/step_06_transient_above_Tc.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time traces of Q_A for left and right circular polarization above Tc. Checker verifies opposite signs for opposite helicities.
- schema:
  - `required_columns`: `helicity`, `time_ps`, `Q_A`

Notes: The hidden checker compares the reported Eu phonon frequency and coupling constant to the paper's computed reference values with tolerances. The double-well potential and time traces are checked for correct structural features (two minima of symmetric depth, sign reversal above threshold, opposite signs for opposite helicities). All gold values are derived from the paper's reported computational results and are not disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "required_columns": [
          "mode",
          "frequency_THz"
        ]
      },
      "description": "Phonon mode labels and frequencies at Gamma point. Checker compares the Eu mode frequency to the paper's reference within tolerance."
    },
    {
      "file": "step_02_double_well_potential.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "displacement_Angstrom",
          "energy_eV"
        ]
      },
      "description": "Energy vs. displacement along the A2g soft mode. Checker verifies a double-well shape with two symmetric minima."
    },
    {
      "file": "step_03_coupling_constant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "units": "q_e/uÅ"
      },
      "description": "Single value for the trilinear coupling constant α. Checker compares to the paper's value within tolerance."
    },
    {
      "file": "step_04_switching_below_Tc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "fluence_mJcm2",
          "time_ps",
          "Q_A"
        ]
      },
      "description": "Time series of Q_A for each fluence below Tc. Checker verifies sign reversal above a threshold fluence."
    },
    {
      "file": "step_05_threshold_fluence.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "units": "mJ/cm²"
      },
      "description": "Switching threshold fluence extracted from the simulation. Checker compares to the paper's threshold within tolerance."
    },
    {
      "file": "step_06_transient_above_Tc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "helicity",
          "time_ps",
          "Q_A"
        ]
      },
      "description": "Time traces of Q_A for left and right circular polarization above Tc. Checker verifies opposite signs for opposite helicities."
    }
  ],
  "notes": "The hidden checker compares the reported Eu phonon frequency and coupling constant to the paper's computed reference values with tolerances. The double-well potential and time traces are checked for correct structural features (two minima of symmetric depth, sign reversal above threshold, opposite signs for opposite helicities). All gold values are derived from the paper's reported computational results and are not disclosed here."
}
```

## How you are scored
A hidden verifier will independently score each of the six workflow artifacts against reference criteria derived from the paper's original computational study. The verifier checks the structural features and numerical values of your submitted files—for example, whether the double‑well potential has two symmetrically deep minima, whether the time traces show sign reversal above a certain fluence, and whether the transient signs are opposite for opposite helicities. Numerical comparisons are made within appropriate tolerances that account for the use of different software implementations. Each artifact contributes a weighted share to the final reward (a value between 0 and 1). Simply quoting a paper's reported number is insufficient; you must execute the workflow to generate the required artifacts from the public inputs and tools.
