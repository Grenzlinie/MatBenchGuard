# Phonon Dispersion and Ferroelectric Hysteresis of BaTiO3 Using Effective Atomic Potentials

## Problem background
BaTiO₃ is a prototypical ferroelectric perovskite. Second-principles effective atomic potentials allow large-scale simulations of such materials, but the impact of long-range dipolar interactions is not fully understood. This task investigates whether an effective atomic potential constructed from dynamical matrices on a 2×2×2 q-point mesh, and without the analytic infinite-range dipole–dipole correction, can faithfully capture the global phonon dispersion, the transverse-optical (TO) ferroelectric instability, and the finite-temperature hysteresis behavior when compared to a reference potential built on an 8×8×8 mesh with the full analytic dipole–dipole term. The central question is to what extent the truncated-range model reproduces the properties of the reference model; this determines whether such simplified potentials are sufficient for the description of polar materials.

## Approach
The workflow uses the MULTIBINIT code and a publicly available second-principles model for BaTiO₃ that provides harmonic force constants and anharmonic coefficients. Two effective atomic potentials are constructed: (i) a reference model, M8+Dip, built with an 8×8×8 q‑point mesh and the analytic infinite‑range dipole–dipole correction activated; (ii) a truncated‑range model, M2, built with a 2×2×2 q‑point mesh and the analytic dipole–dipole correction deactivated. For both potentials, phonon dispersion curves are computed along the high‑symmetry path Γ–X–M–Γ, and the frequencies at the Γ and X points are extracted. From these dispersions, the soft TO mode at Γ is identified, and its frequency and eigendisplacement character are recorded. Additionally, hybrid Monte Carlo (HMC) simulations are performed at 50 K on a 12×12×12 supercell for both models, following a BFGS structural relaxation, to obtain the polarization versus electric‑field hysteresis loop; the coercive field and remanent polarization are then extracted. The key comparison is between the M2 results and those of the M8+Dip reference.

## Reproduction target
The objective is to execute the described workflow and produce three scored artifacts: (1) a CSV (`phonon_frequencies.csv`) listing the phonon frequencies (in cm⁻¹) at the Γ and X points for all modes of the M2 and M8+Dip models; (2) a text file (`unstable_TO_mode.txt`) reporting the frequency and character of the unstable TO mode at Γ for each model; (3) a CSV (`hysteresis_summary.csv`) reporting the coercive field (kV/cm) and remanent polarization (μC/cm²) from the 50 K hysteresis loop for both models. The hidden verifier will compare your reported quantities against the expected values derived from the original study, using predefined tolerances to account for implementation‑ and hardware‑related variations.

## Assets

- MULTIBINIT: https://github.com/multibinit/MULTIBINIT
- Second-Principles Model of BaTiO3 (revised)

## Workflow steps

### Step 1: Build M8+Dip potential
- Role: process
- Action: Using MULTIBINIT and the provided BaTiO3 model, construct the effective atomic potential with an 8x8x8 q-point mesh and the analytic infinite-range dipole-dipole correction activated. Save the model definition.
- Evidence: `/app/outputs/M8Dip_model.log`

### Step 2: Build M2 potential
- Role: process
- Action: Using MULTIBINIT and the provided BaTiO3 model, construct the effective atomic potential with a 2x2x2 q-point mesh and the analytic long-range dipole-dipole correction deactivated. Save the model definition.
- Evidence: `/app/outputs/M2_model.log`

### Step 3: Compute phonon dispersion frequencies
- Role: scored (load-bearing)
- Action: For both M8+Dip and M2 models, compute phonon dispersion curves along the high-symmetry path Gamma-X-M-Gamma. Extract frequencies (in cm^-1) at the Gamma and X points for all phonon modes. Write a CSV with columns: q_point (string, e.g., 'Gamma', 'X'), mode_index (integer, 0-based), frequency_M2 (float), frequency_M8+Dip (float).
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: q_point,mode_index,frequency_M2,frequency_M8+Dip
- Scoring: scored by hidden verifier

### Step 4: Report unstable TO mode
- Role: scored
- Action: From the computed phonon dispersion, identify the soft transverse-optical (TO) mode at the Gamma point for each model. For M2 and M8+Dip, report the frequency (negative for imaginary/unstable) and its character (e.g., chain-like eigendisplacement). Write two lines to a text file: one for M2, one for M8+Dip, in the format 'M2: frequency=value (cm^-1), character=<description>' and similarly for M8+Dip.
- Output file: `/app/outputs/unstable_TO_mode.txt`
- Format: txt
- Contract: Two lines, each: 'Model: frequency=value (cm^-1), character=description'
- Scoring: scored by hidden verifier

### Step 5: Simulate hysteresis loop at 50 K
- Role: scored (load-bearing)
- Action: For both M2 and M8+Dip models, perform a hybrid Monte Carlo (HMC) simulation at 50 K on a 12x12x12 supercell, preceded by BFGS structural relaxation. Compute the polarization vs. electric-field hysteresis loop. Extract the coercive field (kV/cm) and remanent polarization (muC/cm^2). Write a CSV with columns: model (string, 'M2' or 'M8+Dip'), coercive_field (float), remanent_polarization (float).
- Output file: `/app/outputs/hysteresis_summary.csv`
- Format: csv
- Contract: model,coercive_field,remanent_polarization
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/unstable_TO_mode.txt`
- `/app/outputs/hysteresis_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies at Gamma and X points for M2 and M8+Dip models, compared against paper-derived reference values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `q_point`, `mode_index`, `frequency_M2`, `frequency_M8+Dip`
  - `units`:
    - `frequency_M2`: cm^-1
    - `frequency_M8+Dip`: cm^-1

### unstable_TO_mode.txt
- path: `/app/outputs/unstable_TO_mode.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Reported frequency and character of the unstable TO ferroelectric mode for both models, checked for agreement with paper values.
- schema:
  - `type`: text
  - `description`: Two lines: 'M2: frequency=<value> (cm^-1), character=<description>' and 'M8+Dip: frequency=<value> (cm^-1), character=<description>'; imaginary frequency as negative.

### hysteresis_summary.csv
- path: `/app/outputs/hysteresis_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Coercive field and remanent polarization from HMC hysteresis loops at 50 K for M2 and M8+Dip, compared to paper reference.
- schema:
  - `type`: table
  - `required_columns`: `model`, `coercive_field`, `remanent_polarization`
  - `units`:
    - `coercive_field`: kV/cm
    - `remanent_polarization`: muC/cm^2

Notes: All quantitative comparisons are performed by the hidden checker against paper-reported reference values with predefined tolerances. The checker validates schema correctness and value agreement.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_point",
          "mode_index",
          "frequency_M2",
          "frequency_M8+Dip"
        ],
        "units": {
          "frequency_M2": "cm^-1",
          "frequency_M8+Dip": "cm^-1"
        }
      },
      "description": "Phonon frequencies at Gamma and X points for M2 and M8+Dip models, compared against paper-derived reference values with tolerances."
    },
    {
      "file": "unstable_TO_mode.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Two lines: 'M2: frequency=<value> (cm^-1), character=<description>' and 'M8+Dip: frequency=<value> (cm^-1), character=<description>'; imaginary frequency as negative."
      },
      "description": "Reported frequency and character of the unstable TO ferroelectric mode for both models, checked for agreement with paper values."
    },
    {
      "file": "hysteresis_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "coercive_field",
          "remanent_polarization"
        ],
        "units": {
          "coercive_field": "kV/cm",
          "remanent_polarization": "muC/cm^2"
        }
      },
      "description": "Coercive field and remanent polarization from HMC hysteresis loops at 50 K for M2 and M8+Dip, compared to paper reference."
    }
  ],
  "notes": "All quantitative comparisons are performed by the hidden checker against paper-reported reference values with predefined tolerances. The checker validates schema correctness and value agreement."
}
```

## How you are scored
An automated hidden verifier evaluates your submission. First, it checks that all required output files exist and conform to the declared formats and schemas. Then, for each scored artifact, the verifier compares your reported values (phonon frequencies, TO mode frequency, and hysteresis parameters) against hidden reference values that are based on the paper's published results for the same physical conditions. The comparison is performed with predefined tolerance margins. Your final reward is a weighted combination of the per‑artifact scores, with the phonon frequencies and hysteresis parameters carrying the largest weight. Reporting values without genuinely executing the simulation is insufficient, because the verifier also performs internal consistency checks and will detect artifacts that are not physically self‑consistent.
