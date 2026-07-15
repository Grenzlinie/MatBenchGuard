# Space- and Time-Dependent Monte Carlo for High-Frequency Conductivity in GaN

## Problem background
In compensation-doped polar semiconductors like GaN at low temperatures, electrons can exhibit cyclic motion under high electric fields: an electron is accelerated ballistically, emits an optical phonon, loses nearly all its kinetic energy, and the cycle repeats. This leads to spatial and temporal modulation of electron velocity and concentration, giving rise to transit-time resonances. When such a drifting electron gas is subjected to a small space- and time-dependent electric field, the high-frequency conductivity can become negative in certain frequency-wavevector windows, enabling amplification of THz waves. This task reproduces the calculation of the complex high-frequency conductivity σ_{ω,q} of a compensated electron gas in bulk GaN under a combined DC and AC field using a single-particle Monte Carlo method.

## Approach
Implement a single-particle Monte Carlo simulation for electrons in the Γ valley of GaN with parabolic band (effective mass 0.2 m0). Scattering mechanisms include ionized impurities (mixed Brooks-Herring/Conwell-Weisskopf model for compensated samples), quasielastic acoustic phonons, and polar optical phonons. The electron is subjected to a uniform stationary field F0 plus a small spatially and temporally varying field F_{ω,q} cos(qz−ωt). The simulation records electron appearances and momentum projections in discretized {t,z,P_z} phase-space meshes over many temporal periods. From the accumulated counts, the steady-state current density and the first Fourier harmonic of the alternating current are extracted. The specific complex conductivity (Re[σ]/e n_e and Im[σ]/e n_e, in cm^2/(V·s)) is derived from the harmonic and field amplitude. This procedure is performed at three target frequencies for a fixed wavevector, under the physical conditions specified in the workflow steps.

## Reproduction target
Compute the specific complex conductivity per electron (Re[σ]/(e n_e) and Im[σ]/(e n_e), in cm^2/(V·s)) at three frequencies: ω/2π = 0.2, 0.5, 1.0 THz. The physical parameters are: DC field F0=3 kV/cm, AC field amplitude F_{ω,q}=0.1×F0, wavevector q=10^5 cm^{-1}, lattice temperature T0=30 K, ionized impurity concentration N_i=10^16 cm^{-3}, and electron concentration n_e=10^15 cm^{-3}. Write the resulting values to the CSV file conductivity_values.csv with columns freq_THz, Re_sigma_per_e, Im_sigma_per_e. The simulation must first produce the intermediate phase_counts.npz file containing the phase-resolved counts, which is required for the subsequent conductivity extraction.

## Assets

- Python 3.8+
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Monte Carlo simulation and phase-space data collection
- Role: process
- Action: Implement the single-particle Monte Carlo algorithm for electrons in bulk GaN with Γ-valley parabolic band (m*=0.2 m0). Include ionized-impurity scattering (mixed Brooks-Herring/Conwell-Weisskopf model for compensated samples), quasielastic acoustic-phonon scattering, and polar optical-phonon scattering. For each target frequency (0.2, 0.5, 1.0 THz), simulate electron dynamics under the total field F0 + F_{ω,q} cos(qz-ωt) with F0=3 kV/cm, F_{ω,q}=0.1×F0, q=10^5 cm^{-1}, T0=30 K, N_i=1e16 cm^{-3}, n_e=1e15 cm^{-3}. Discretize the {t,z,P_z} phase space into cells of temporal period T=2π/ω and spatial period Λ=2π/q, further subdivided into fine meshes for phase-resolved collection. Run the simulation for a large number of periods to achieve sufficient statistical accuracy. Record the accumulated electron appearance counts and momentum projections in each mesh. Save the aggregated phase-space data for all three frequencies in a single NumPy archive file 'phase_counts.npz'.
- Evidence: `/app/outputs/phase_counts.npz`

### Step 2: Complex conductivity calculation
- Role: scored (load-bearing)
- Action: From the phase-space data in phase_counts.npz, compute the steady-state current density J_{z,0} by averaging over the phase-space meshes. Extract the first-order Fourier harmonic of the alternating current, Re[j_{ω,q}] and Im[j_{ω,q}], using the phase-space formulas for current density and Fourier component. Then derive the specific complex conductivity per electron, Re[σ]/(e n_e) and Im[σ]/(e n_e), in units of cm^2/(V·s), for each of the three frequencies. Save the results to 'conductivity_values.csv'.
- Output file: `/app/outputs/conductivity_values.csv`
- Format: csv
- Contract: Table with columns: freq_THz (float, frequency in THz), Re_sigma_per_e (float, specific real part of conductivity in cm^2/(V·s)), Im_sigma_per_e (float, specific imaginary part in cm^2/(V·s)). Three rows for frequencies 0.2, 0.5, 1.0 THz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/conductivity_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### conductivity_values.csv
- path: `/app/outputs/conductivity_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Specific high-frequency complex conductivity per electron for the three target frequencies (0.2, 0.5, 1.0 THz) at wavevector q=1e5 cm^{-1}.
- schema:
  - `type`: table
  - `required_columns`: `freq_THz`, `Re_sigma_per_e`, `Im_sigma_per_e`
  - `units`:
    - `freq_THz`: THz
    - `Re_sigma_per_e`: cm^2/(V·s)
    - `Im_sigma_per_e`: cm^2/(V·s)

Notes: The soler must produce the intermediate phase_counts.npz evidence to document that the Monte Carlo simulation was run. The scored CSV is derived from that data and compared to hidden gold values. The simulation is computationally intensive; the solver may use high-performance computing resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "conductivity_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "freq_THz",
          "Re_sigma_per_e",
          "Im_sigma_per_e"
        ],
        "units": {
          "freq_THz": "THz",
          "Re_sigma_per_e": "cm^2/(V·s)",
          "Im_sigma_per_e": "cm^2/(V·s)"
        }
      },
      "description": "Specific high-frequency complex conductivity per electron for the three target frequencies (0.2, 0.5, 1.0 THz) at wavevector q=1e5 cm^{-1}."
    }
  ],
  "notes": "The soler must produce the intermediate phase_counts.npz evidence to document that the Monte Carlo simulation was run. The scored CSV is derived from that data and compared to hidden gold values. The simulation is computationally intensive; the solver may use high-performance computing resources."
}
```

## How you are scored
A hidden verifier will examine your submitted artifacts. For the scored step (conductivity_values.csv), the verifier will check that the file is present, correctly formatted, and contains values that match reference expected results within a tolerance that accounts for statistical noise and implementation differences. The verifier may also recompute the conductivity from the raw phase-space data in phase_counts.npz to verify internal consistency. The final reward is a weighted combination of these checks. Providing only the final conductivity values without the correct underlying simulation data will not receive full credit.
