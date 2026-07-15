# Core-shell vibration frequencies and oxygen Frenkel pair recombination dynamics in UO2

## Problem background
Uranium dioxide (UO₂) is the standard nuclear fuel, and its high tolerance to radiation damage is believed to be partly due to rapid recombination of Frenkel pairs (a vacancy-interstitial pair). Molecular dynamics (MD) simulations are a key tool for probing these recombination processes at the atomic scale, but conventional rigid-ion interatomic potentials do not explicitly account for ion polarizability. A core-shell model, where each ion is represented by a massive core and a light shell connected by a harmonic spring, provides a way to incorporate polarizability. This task investigates how the use of an adiabatic core-shell model in UO₂ affects the recombination dynamics of oxygen Frenkel pairs compared to what a rigid-ion model would predict.

## Approach
The simulation protocol has four stages:
1. **Adiabaticity check**: Compute the natural vibration frequencies of the oxygen and uranium core-shell units from the spring constants and mass fractions to confirm they are well separated from the ionic vibrational spectrum (<800 cm⁻¹).
2. **System setup**: Build a 5×5×5 supercell of UO₂ fluorite (lattice parameter 5.468 Å). Create oxygen Frenkel pair defects of ranks 3, 4 type‑I, 4 type‑II, and 5 by removing a lattice oxygen and placing it at the corresponding octahedral interstitial position. Equilibrate each configuration at the five target temperatures using NPT and NVT ensembles with the Meis–Chartier core-shell potential.
3. **MD recombination runs**: For each rank and temperature, perform multiple independent MD simulations with the adiabatic core-shell potential using a variable time step (maximum displacement 0.04 Å). Track the distance between the interstitial and the vacancy; the recombination time is the moment when the interstitial returns to the original vacancy site.
4. **Data analysis**: Compute the mean and standard deviation of the recombination times across the simulations for each condition. Fit the temperature-dependent mean lifetimes to an Arrhenius law, τ = τ₀ exp(Eₐ/kB T), to extract the pre‑exponential factor τ₀ and the activation energy Eₐ for each Frenkel pair rank.

## Reproduction target
The goal is to produce three scored artifacts:
1. `core_shell_frequencies.txt`: the natural vibration frequencies of oxygen and uranium core-shell units (in THz and cm⁻¹) calculated from the given spring constants and mass fractions.
2. `oxygen_fp_recombination_times.csv`: for each oxygen Frenkel pair rank (3, 4I, 4II, 5) and each temperature (600, 900, 1200, 1500, 1800 K), the mean recombination lifetime, its standard deviation, and the number of independent runs.
3. `oxygen_fp_arrhenius_params.csv`: the Arrhenius pre‑exponential factor τ₀ (ps) and activation energy Eₐ (eV) obtained by fitting the mean lifetimes from the previous file.
The recombination lifetimes and activation energies should reflect the dynamics of oxygen Frenkel pair recombination under the adiabatic core-shell model.

## Assets

- CP2K program package: https://www.cp2k.org
- Meis-Chartier core-shell potential for UO2: 10.1016/j.jnucmat.2005.01.016

## Workflow steps

### Step 1: Compute core-shell natural frequencies
- Role: scored
- Action: Calculate the natural vibration frequencies of oxygen and uranium core‑shell units using the given spring constants and mass fractions: ν = (1/(2π))√(k/(x(1-x)m)). Output both the frequency in THz and the wavenumber in cm⁻¹.
- Output file: `/app/outputs/core_shell_frequencies.txt`
- Format: txt
- Contract: Two lines: 'O: ν = <value> THz ( <value> cm⁻¹ )' and 'U: ν = <value> THz ( <value> cm⁻¹ )'
- Scoring: scored by hidden verifier

### Step 2: Prepare UO2 supercell and oxygen Frenkel pair defect configurations
- Role: process
- Action: Build a 5×5×5 supercell of UO2 fluorite (lattice parameter a0=5.468 Å). Create defect configurations for oxygen Frenkel pairs of ranks 3, 4 type‑I, 4 type‑II, and 5 by removing an oxygen atom from its lattice site and placing it at the corresponding octahedral interstitial position. Equilibrate each configuration at 600, 900, 1200, 1500, and 1800 K using NPT and NVT ensembles with the core‑shell potential.
- Evidence: `/app/outputs/preparation.log`

### Step 3: Run MD simulations of oxygen Frenkel pair recombination
- Role: scored (load-bearing)
- Action: For each oxygen FP rank (3, 4I, 4II, 5) and each temperature (600, 900, 1200, 1500, 1800 K), run 30 independent MD simulations using the adiabatic core‑shell potential and a variable time step with max displacement 0.04 Å. Record the recombination time (when the interstitial returns to the vacancy site). Report the mean and standard deviation of the recombination time in picoseconds, and the number of runs.
- Output file: `/app/outputs/oxygen_fp_recombination_times.csv`
- Format: csv
- Contract: CSV header: rank,temperature_K,mean_lifetime_ps,std_lifetime_ps,num_runs. One row per combination of rank and temperature.
- Scoring: scored by hidden verifier

### Step 4: Arrhenius analysis of oxygen recombination lifetimes
- Role: scored
- Action: Fit the mean recombination lifetimes from step 3 to the Arrhenius function τ = τ₀ exp(E_a / k_B T). Output the fitted pre‑exponential factor τ₀ (ps) and activation energy E_a (eV) for each rank.
- Output file: `/app/outputs/oxygen_fp_arrhenius_params.csv`
- Format: csv
- Contract: CSV header: rank,tau0_ps,Ea_eV. One row per rank (3,4I,4II,5).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/core_shell_frequencies.txt`
- `/app/outputs/oxygen_fp_recombination_times.csv`
- `/app/outputs/oxygen_fp_arrhenius_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### core_shell_frequencies.txt
- path: `/app/outputs/core_shell_frequencies.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Natural core-shell vibration frequencies for O and U, used to validate adiabatic separation.
- schema:
  - `type`: text
  - `description`: Two lines: 'O: ν = <value> THz ( <value> cm⁻¹ )' and 'U: ν = <value> THz ( <value> cm⁻¹ )'

### oxygen_fp_recombination_times.csv
- path: `/app/outputs/oxygen_fp_recombination_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean and standard deviation of recombination times for oxygen Frenkel pairs of ranks 3, 4I, 4II, 5 at temperatures 600, 900, 1200, 1500, 1800 K.
- schema:
  - `type`: table
  - `required_columns`: `rank`, `temperature_K`, `mean_lifetime_ps`, `std_lifetime_ps`, `num_runs`
  - `units`:
    - `mean_lifetime_ps`: ps
    - `std_lifetime_ps`: ps
    - `temperature_K`: K

### oxygen_fp_arrhenius_params.csv
- path: `/app/outputs/oxygen_fp_arrhenius_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Arrhenius pre‑exponential factor and activation energy fitted from the recombination lifetimes for each oxygen Frenkel pair rank.
- schema:
  - `type`: table
  - `required_columns`: `rank`, `tau0_ps`, `Ea_eV`
  - `units`:
    - `tau0_ps`: ps
    - `Ea_eV`: eV

Notes: The task reproduces the core-shell vibration frequencies and the oxygen Frenkel pair recombination dynamics using the Meis-Chartier potential. Uranium Frenkel pairs, static formation energies, and isolated defect migration energies are excluded per the taskability scope, focusing on the main dynamic claim that polarizability alters oxygen FP recombination times.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "core_shell_frequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Two lines: 'O: ν = <value> THz ( <value> cm⁻¹ )' and 'U: ν = <value> THz ( <value> cm⁻¹ )'"
      },
      "description": "Natural core-shell vibration frequencies for O and U, used to validate adiabatic separation."
    },
    {
      "file": "oxygen_fp_recombination_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rank",
          "temperature_K",
          "mean_lifetime_ps",
          "std_lifetime_ps",
          "num_runs"
        ],
        "units": {
          "mean_lifetime_ps": "ps",
          "std_lifetime_ps": "ps",
          "temperature_K": "K"
        }
      },
      "description": "Mean and standard deviation of recombination times for oxygen Frenkel pairs of ranks 3, 4I, 4II, 5 at temperatures 600, 900, 1200, 1500, 1800 K."
    },
    {
      "file": "oxygen_fp_arrhenius_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rank",
          "tau0_ps",
          "Ea_eV"
        ],
        "units": {
          "tau0_ps": "ps",
          "Ea_eV": "eV"
        }
      },
      "description": "Arrhenius pre‑exponential factor and activation energy fitted from the recombination lifetimes for each oxygen Frenkel pair rank."
    }
  ],
  "notes": "The task reproduces the core-shell vibration frequencies and the oxygen Frenkel pair recombination dynamics using the Meis-Chartier potential. Uranium Frenkel pairs, static formation energies, and isolated defect migration energies are excluded per the taskability scope, focusing on the main dynamic claim that polarizability alters oxygen FP recombination times."
}
```

## How you are scored
Each output file is checked by a hidden verifier. The verifier compares your computed core-shell frequencies against reference values derived from the given potential parameters, allowing a small tolerance. For the recombination times, it compares each mean lifetime to a gold standard; credit is awarded if the difference is within a generous relative margin or if it falls within the reported standard deviation. The Arrhenius activation energies are compared to expected values within a tolerance, and the verifier also checks that the activation energies follow a physically motivated ordering across the ranks. The final score is a weighted sum of the individual stage scores.
