# Fully-kinetic Monte Carlo electron transport in lower ionosphere under lightning EMP

## Problem background
Rapidly varying electromagnetic pulses (EMPs) produced by lightning discharges interact with the lower ionosphere, heating ambient electrons, causing ionization, and generating optical emissions. The electron distribution function can be highly anisotropic during the first few microseconds of the interaction before evolving toward a more isotropic state. Understanding how optical emission patterns depend on the EMP waveform—in particular the rise time and pulse width—requires a time-dependent kinetic treatment that resolves this transient anisotropy. This task implements such a simulation to compute the evolution of the electron velocity distribution and the altitude-integrated optical emission rates for realistic and idealized EMP waveforms.

## Approach
Build a 1D fully-kinetic time-dependent Monte Carlo particle simulation coupled to a Lax-Wendroff Maxwell field solver for electron dynamics in the lower ionosphere. The simulation uses publicly available electron–air collision cross-section data (total scattering cross section and energy loss function), a neutral atmospheric density profile from a standard thermospheric model (70–100 km), and published excitation, transition, and quenching rates for the N₂ first positive band. Electron trajectories are advanced with an electric field acceleration step, collision probabilities are sampled from the cross sections, and inelastic energy losses are treated with an effective inelastic cross section. Observable quantities—normalized Legendre moments of the velocity distribution and optical emission rates—are accumulated from the particle ensemble. A constant-electric-field case at a single altitude is used to study isotropization of the distribution. Then the full coupled Maxwell-Monte Carlo simulation is run for families of EMP waveforms (realistic three-parameter pulses and cosh-shaped pulses) with varying rise times and pulse widths, under both equal-total-energy and equal-peak-amplitude normalizations. For each simulation, the altitude-integrated optical emission rate in the N₂ first positive band is recorded as a function of time.

## Reproduction target
Produce three scored CSV artifacts by running the simulations:
1. `distribution_moments.csv` – normalized Legendre moments f0–f3 at a single altitude (90 km) under a constant electric field, at specified times after the field is turned on, to demonstrate the evolution toward isotropy.
2. `emission_rates_realistic.csv` – altitude-integrated optical emission rate in the N₂ first positive band for realistic EMP waveforms with four different rise times (T₂ = 2, 5, 10, 25 µs), all carrying equal total pulse energy, computed over the altitude range 70–100 km and up to 150 µs.
3. `emission_rates_cosh.csv` – altitude-integrated optical emission rate for cosh-shaped EMPs with pulse widths T₂ = 5, 7, 10, 20 µs, under two normalization conditions: (a) equal total pulse energy, and (b) equal peak amplitude. The altitude range and time window are the same as for the realistic case.
The target is to reproduce the structural patterns evident in these outputs: isotropization of the electron distribution, double-peaked versus single-peaked temporal profiles of the emission, and the relative ordering of peak emission rates across different waveform parameters. Exact numeric agreement with any published figure is not required.

## Assets

- Electron-air collision cross section data: https://www.lxcat.net/
- Neutral atmospheric density profile: https://ccmc.gsfc.nasa.gov/models/NRLMSIS~00/
- N2 excitation, transition and quenching rates: 10.1029/93GL01989

## Workflow steps

### Step 1: Compile input data
- Role: process
- Action: Obtain neutral density profile N(z) for 70–100 km from NRLMSISE‑00 and tabulate the energy‑dependent total scattering cross section σ_tot(ε) and energy loss function F(ε) from LXCat or published literature. Also extract the excitation, transition, and quenching rates for the 1st positive N₂ band from Taranenko (1993). Store these in a format usable by the simulation code.
- Evidence: `/app/outputs/data_assembly.log`

### Step 2: Electron distribution moments
- Role: scored (load-bearing)
- Action: Run the Monte Carlo simulation for a single cell at 90 km altitude with a constant electric field E=50 V/m turned on at t=0. Initialize 10⁴ particles with Maxwellian initial velocities. Evolve using the algorithm: (i) update v_parallel by -eEδt/m_e, (ii) compute collision probability P_i = N σ_tot(ε_i) v_i δt, (iii) for colliding particles set new speed v_i√(1-σ_in/σ_tot) and random scattering angle θ, (iv) record normalized Legendre moments f0–f3 of the velocity distribution at times 0.5, 1.0, 1.5 µs. Write distribution_moments.csv.
- Output file: `/app/outputs/distribution_moments.csv`
- Format: csv
- Contract: Columns: time_us (float), f0 (float), f1 (float), f2 (float), f3 (float). One row per time point.
- Scoring: scored by hidden verifier

### Step 3: Altitude-integrated emission rates for realistic EMPs
- Role: scored (load-bearing)
- Action: For each realistic EMP waveform defined with T₁=100 µs, T₃=50 µs and T₂ ∈ {2,5,10,25} µs, where each pulse is scaled to equal total energy (E_max adjusted accordingly), run the full coupled simulation (Maxwell + MC particles) over altitude 70–100 km with 300 m cells and 10⁴ particles per cell. At each time step compute the 1st positive N₂ band optical emission rate using the excitation/transition/quenching rates, integrate over altitude, and record the total emission rate as a function of time up to 150 µs. Output emission_rates_realistic.csv.
- Output file: `/app/outputs/emission_rates_realistic.csv`
- Format: csv
- Contract: Columns: time_us (float), case (string, e.g., 'T2_2'), emission_rate (float, arbitrary units). Time series covering 0–150 µs.
- Scoring: scored by hidden verifier

### Step 4: Altitude-integrated emission rates for cosh EMPs
- Role: scored (load-bearing)
- Action: For cosh‑shaped EMPs with E(t) ∝ cosh⁻¹(t/T₂)² and T₂ ∈ {5,7,10,20} µs, under two normalization conditions: (a) equal total pulse energy, and (b) equal peak amplitude. For each condition and T₂, run the simulation as in the previous step and compute altitude-integrated emission rate up to 150 µs. Output emission_rates_cosh.csv.
- Output file: `/app/outputs/emission_rates_cosh.csv`
- Format: csv
- Contract: Columns: time_us (float), case (string, e.g., 'equal_energy_T2_5'), emission_rate (float, arbitrary units). Time series covering 0–150 µs.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/distribution_moments.csv`
- `/app/outputs/emission_rates_realistic.csv`
- `/app/outputs/emission_rates_cosh.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### distribution_moments.csv
- path: `/app/outputs/distribution_moments.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The normalized Legendre moments of electron velocity distribution at 90 km altitude under constant electric field 50 V/m at specified times (0.5, 1.0, 1.5 µs). Verifies isotropization.
- schema:
  - `type`: table
  - `required_columns`: `time_us`, `f0`, `f1`, `f2`, `f3`

### emission_rates_realistic.csv
- path: `/app/outputs/emission_rates_realistic.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Altitude-integrated optical emission rate in 1st positive N₂ band for realistic EMP waveforms. Verifies double-peaked temporal profiles and relative ordering of peak emission rates.
- schema:
  - `type`: table
  - `required_columns`: `time_us`, `case`, `emission_rate`

### emission_rates_cosh.csv
- path: `/app/outputs/emission_rates_cosh.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Altitude-integrated optical emission rate for cosh EMPs under equal-energy and equal-amplitude normalizations. Verifies monotonic dependence on pulse width and single-peaked profiles for shorter pulses.
- schema:
  - `type`: table
  - `required_columns`: `time_us`, `case`, `emission_rate`

Notes: Verification uses structural patterns (isotropization, double-peaked vs single-peaked, relative ordering within factor 2) rather than exact numeric match. No gold values are revealed here; the checker inspects shape and trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "distribution_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_us",
          "f0",
          "f1",
          "f2",
          "f3"
        ]
      },
      "description": "The normalized Legendre moments of electron velocity distribution at 90 km altitude under constant electric field 50 V/m at specified times (0.5, 1.0, 1.5 µs). Verifies isotropization."
    },
    {
      "file": "emission_rates_realistic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_us",
          "case",
          "emission_rate"
        ]
      },
      "description": "Altitude-integrated optical emission rate in 1st positive N₂ band for realistic EMP waveforms. Verifies double-peaked temporal profiles and relative ordering of peak emission rates."
    },
    {
      "file": "emission_rates_cosh.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_us",
          "case",
          "emission_rate"
        ]
      },
      "description": "Altitude-integrated optical emission rate for cosh EMPs under equal-energy and equal-amplitude normalizations. Verifies monotonic dependence on pulse width and single-peaked profiles for shorter pulses."
    }
  ],
  "notes": "Verification uses structural patterns (isotropization, double-peaked vs single-peaked, relative ordering within factor 2) rather than exact numeric match. No gold values are revealed here; the checker inspects shape and trends."
}
```

## How you are scored
A hidden verifier will independently examine each output file. It checks for structural patterns consistent with the underlying physics: for the distribution moments, whether the isotropic component dominates after sufficient time; for the realistic EMP emission rates, whether the temporal profiles show two distinct peaks (interference pattern) and whether the peak rates follow a plausible ordering with changing rise time; for the cosh EMP emission rates, whether the dependence on pulse width under the two normalizations matches expected trends (e.g., monotonic change) and whether shorter pulses produce single-peaked profiles. Comparisons use tolerances suitable for independent re-implementations that may differ in numerical details, discretisation, and random seeds. Each stage carries a weight, and the final score is a weighted combination. Simply reporting the paper's numbers without running the simulation will not produce the rich structural patterns required by the verifier.
