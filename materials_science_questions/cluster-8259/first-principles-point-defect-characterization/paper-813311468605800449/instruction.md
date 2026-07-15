# Adiabatic core-shell model validation and Frenkel pair recombination in UO2

## Problem background
Uranium dioxide (UO2) is the standard nuclear fuel, and understanding the recombination behavior of radiation-induced Frenkel pairs is crucial for predicting radiation tolerance. A key open question is how the explicit description of ionic polarizability, via a core-shell model, affects the recombination times of oxygen and uranium Frenkel pairs compared to a simpler rigid-ion model. This task implements the adiabatic core-shell model and compares its predictions for Frenkel pair recombination lifetimes with those of a rigid-ion model, testing the influence of polarizability.

## Approach
Two interatomic potential models for UO2 are compared: an adiabatic core-shell model (Meis and Chartier) that includes ion polarizability, and a rigid-ion model (Morelon et al.) that treats ions as point charges. Both are implemented in the CP2K molecular dynamics package. The workflow first validates the core-shell model by computing the analytic natural vibration frequencies of the core-shell units and verifying adiabatic separation via a velocity autocorrelation function (VACF) spectrum at 500 K. The main simulation creates a specific oxygen Frenkel pair defect (rank 5, vacancy-interstitial distance of √35/4 times the lattice parameter) in a 5×5×5 supercell at 600 K. Multiple independent NVT trajectories are run for each potential, and the mean recombination time is extracted. The comparison between the two potentials quantifies the role of polarizability.

## Reproduction target
Compute the mean recombination lifetime τ (in picoseconds) for an oxygen Frenkel pair of rank 5 at 600 K, using both the adiabatic core-shell potential and the rigid-ion potential. Additionally, calculate the analytic core-shell vibration frequencies for oxygen and uranium, and determine the highest ionic vibrational frequency from the VACF of the pristine system at 500 K to confirm adiabatic separation (the frequency must be below 800 cm⁻¹).

## Assets

- CP2K molecular dynamics package: https://www.cp2k.org/
- Meis and Chartier core-shell potential parameters for UO2: 10.1016/j.jnucmat.2005.04.028
- Morelon et al. rigid-ion potential parameters for UO2: 10.1080/14786430310001600441
- UO2 fluorite crystal structure: https://legacy.materialsproject.org/materials/mp-2501/

## Workflow steps

### Step 1: Prepare interatomic potential inputs
- Role: process
- Action: Assemble the full interatomic potential parameters for the rigid-ion model (Morelon et al.) and the adiabatic core-shell model (Meis and Chartier), including Buckingham parameters, spring constants (k_O=70.824 eV/Å², k_U=171.556 eV/Å²) and shell mass fractions (x_O=0.1, x_U=0.01). Create CP2K input files for both potentials.
- Evidence: `/app/outputs/potential_files_exist.log`

### Step 2: Compute core-shell natural frequencies
- Role: scored
- Action: Calculate the natural core-shell vibration frequencies for oxygen and uranium using the formula ν = 1/(2π) sqrt(k/(x(1-x)m)) with the given parameters and atomic masses. Output the frequencies in THz and wavenumbers.
- Output file: `/app/outputs/step_00_core_shell_frequencies.json`
- Format: json
- Contract: JSON object with keys: nu_O_core_shell_THz, nutilde_O_core_shell_cm-1, nu_U_core_shell_THz, nutilde_U_core_shell_cm-1 (all numeric).
- Scoring: scored by hidden verifier

### Step 3: Equilibrate UO2 supercell via NPT MD
- Role: process
- Action: Build a 5×5×5 supercell of UO2 in the fluorite structure. For each interatomic potential (rigid-ion and core-shell), run an NPT equilibration at 600 K and 0 GPa for 20 ps, saving the final structure and velocities.
- Evidence: `/app/outputs/equilibration.log`

### Step 4: Create oxygen Frenkel pair defect
- Role: process
- Action: From the equilibrated structure, displace an oxygen atom to the octahedral interstitial site to form a rank-5 oxygen Frenkel pair (vacancy-interstitial distance √35/4 a0). Prepare CP2K input files for NVT recombination simulations at 600 K.
- Evidence: `/app/outputs/defect_created.log`

### Step 5: Run MD for velocity autocorrelation function
- Role: process
- Action: Perform a short NVT molecular dynamics simulation at 500 K using the core-shell potential (time step ≤0.77 fs) on the pristine supercell to collect atomic velocities for VACF analysis. Save a trajectory file for at least 10 ps.
- Evidence: `/app/outputs/vacf_trajectory.xyz`

### Step 6: Compute vibrational spectrum and highest frequency
- Role: scored
- Action: From the saved 500 K trajectory, compute the velocity autocorrelation function and its Fourier transform to obtain the vibrational density of states. Determine the highest ionic frequency peak and report its wavenumber; it must lie below 800 cm⁻¹.
- Output file: `/app/outputs/step_01_vacf_highest_frequency.json`
- Format: json
- Contract: JSON object with key highest_ionic_frequency_cm-1 (numeric).
- Scoring: scored by hidden verifier

### Step 7: Run recombination MD simulations
- Role: process
- Action: For each potential (core-shell and rigid-ion), run 30 independent NVT simulations at 600 K for the oxygen rank-5 Frenkel pair (3 initial configurations × 10 random initial velocities), each up to 2 ns or until recombination. Record the recombination event time for each run.
- Evidence: none

### Step 8: Analyze recombination lifetimes
- Role: scored (load-bearing)
- Action: From the collected recombination times, compute the mean lifetime τ (in ps) for the oxygen rank-5 Frenkel pair at 600 K for both the core-shell and rigid-ion models.
- Output file: `/app/outputs/step_02_frenkel_lifetimes.json`
- Format: json
- Contract: JSON object with keys oxygen_rank5_tau_core_shell (ps) and oxygen_rank5_tau_rigid_ion (ps), both numeric.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_00_core_shell_frequencies.json`
- `/app/outputs/step_01_vacf_highest_frequency.json`
- `/app/outputs/step_02_frenkel_lifetimes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_00_core_shell_frequencies.json
- path: `/app/outputs/step_00_core_shell_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Analytically computed natural core-shell vibration frequencies.
- schema:
  - `type`: object
  - `required`:
    - `nu_O_core_shell_THz`: number
    - `nutilde_O_core_shell_cm-1`: number
    - `nu_U_core_shell_THz`: number
    - `nutilde_U_core_shell_cm-1`: number

### step_01_vacf_highest_frequency.json
- path: `/app/outputs/step_01_vacf_highest_frequency.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Highest ionic vibrational frequency from VACF at 500 K; must be < 800 cm⁻¹.
- schema:
  - `type`: object
  - `required`:
    - `highest_ionic_frequency_cm-1`: number

### step_02_frenkel_lifetimes.json
- path: `/app/outputs/step_02_frenkel_lifetimes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Mean recombination lifetime (ps) for oxygen rank-5 FP at 600 K for both potentials.
- schema:
  - `type`: object
  - `required`:
    - `oxygen_rank5_tau_core_shell`: number
    - `oxygen_rank5_tau_rigid_ion`: number

Notes: All scored artifacts are re-derivable: the analytic frequencies follow a known formula, the highest ionic frequency comes from a VACF spectrum, and the recombination times are aggregated from independent MD runs. The checker compares against paper-reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_00_core_shell_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "nu_O_core_shell_THz": "number",
          "nutilde_O_core_shell_cm-1": "number",
          "nu_U_core_shell_THz": "number",
          "nutilde_U_core_shell_cm-1": "number"
        }
      },
      "description": "Analytically computed natural core-shell vibration frequencies."
    },
    {
      "file": "step_01_vacf_highest_frequency.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "highest_ionic_frequency_cm-1": "number"
        }
      },
      "description": "Highest ionic vibrational frequency from VACF at 500 K; must be < 800 cm⁻¹."
    },
    {
      "file": "step_02_frenkel_lifetimes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "oxygen_rank5_tau_core_shell": "number",
          "oxygen_rank5_tau_rigid_ion": "number"
        }
      },
      "description": "Mean recombination lifetime (ps) for oxygen rank-5 FP at 600 K for both potentials."
    }
  ],
  "notes": "All scored artifacts are re-derivable: the analytic frequencies follow a known formula, the highest ionic frequency comes from a VACF spectrum, and the recombination times are aggregated from independent MD runs. The checker compares against paper-reported values with appropriate tolerances."
}
```

## How you are scored
Each scored output file – frequencies, VACF highest frequency, and recombination lifetimes – will be checked by a hidden verifier. The verifier compares your computed values against independently determined reference criteria: the analytic frequencies against the correct formula-derived values, the VACF peak against a threshold, and the recombination lifetimes against expected bounds with appropriate tolerances. You must produce these quantities by running the simulations and analysis; simply copying expected numbers is not sufficient. Each scored artifact contributes a share of the final reward.
