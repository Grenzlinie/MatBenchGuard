# Continuum Raman Excitation Profiles of HI via Coupled-Channel Wavepacket Propagation

## Problem background
Resonance Raman scattering involves photoexcitation from a ground vibrational eigenstate to an electronically excited manifold, followed by radiative decay back to vibrationally excited levels of the ground electronic state. In diatomic molecules, when several dissociative excited electronic states lie close in energy and are coupled, the wavepackets evolving on different potential surfaces can interfere, modifying the Raman intensities and potentially producing resonance de‑enhancement – a dip in the Raman excitation profile (REP) as a function of incident wavelength. This task computes the continuum Raman spectrum of hydrogen iodide (HI), a system for which four coupled excited electronic states contribute, to examine whether such interference effects manifest in the overall REPs for fundamental and overtone vibrational transitions.

## Approach
The calculation follows a time‑dependent quantum mechanical wavepacket framework. First, the potential energy curves of the ground and four excited electronic states, together with the corresponding transition dipole moments, are obtained. The ground‑state vibrational eigenfunctions and eigenenergies for v = 0–5 are solved. For each excited electronic channel, an initial wavepacket is formed by multiplying the v = 0 eigenfunction by the channel‑specific transition dipole; similarly, promoted states for v ≥ 1 are prepared by taking the product of the transition dipole with the respective excited vibrational eigenfunction. These initial wavepackets are propagated on the coupled excited‑state surfaces using a grid‑based method that evaluates the kinetic energy operator via fast Fourier transform and advances time with a second‑order difference scheme. At each time step, the autocorrelation of the initial wavepacket and the cross‑correlations with the promoted states are recorded for every channel. Channel‑resolved Raman amplitudes are obtained by Fourier transforming these time‑domain correlation functions. The total Raman amplitude for each final vibrational level is the sum over channels, and the overall REP intensity is computed from the squared magnitude of the total amplitude, scaled by the appropriate frequency factors. The final result is a set of overall REP curves – one for the fundamental and one for each overtone – showing the intensity as a function of incident wavelength.

## Reproduction target
Produce a CSV file containing the overall Raman excitation profiles (REPs) for the HI fundamental transition (v = 0 → 1) and the first four overtone transitions (v = 0 → 2, 3, 4, 5). The file must have columns: wavelength_nm (incident wavelength in nanometres) and intensity_fundamental, intensity_overtone_2, intensity_overtone_3, intensity_overtone_4, intensity_overtone_5 (intensities in arbitrary but consistent units). The intensity in each column is the total Raman intensity summed over all four excited electronic channels. The curves should reflect the genuine outcome of the coupled‑channel wavepacket simulation, without any post‑processing that alters the relative shape or dip structure of the profiles.

## Assets

- Levy-Shapiro HI potential energy curves and transition dipole moments: 10.1063/1.455069
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare potential energy curves and transition dipoles
- Role: process
- Action: Obtain the Levy-Shapiro potential energy curves and transition dipole moments for the ground and four excited electronic states of HI from the published dataset and prepare them as functions of internuclear distance r. This provides the input potentials, nonadiabatic couplings, and transition dipoles for all subsequent steps.
- Evidence: none

### Step 2: Compute ground vibrational eigenstates
- Role: process
- Action: Solve the time-independent Schrödinger equation for nuclear motion on the ground electronic state potential to obtain the vibrational eigenfunctions χ_v(r) and eigenenergies for vibrational levels v=0 through at least v=5, using the ground potential from step 01.
- Evidence: none

### Step 3: Prepare initial wavepackets and promoted states
- Role: process
- Action: For each excited-state channel l=1..4, construct the initial promoted-state wavepacket |φ^l(0)⟩ = μ^l(r) |χ_0(r)⟩, where χ_0 is the v=0 eigenfunction from step 02 and μ^l is the transition dipole from step 01. Also build the promoted states φ_v^l = μ^l χ_v for v=1..5, required for cross-correlation functions in step 04.
- Evidence: none

### Step 4: Propagate wavepackets and compute time correlation functions
- Role: process
- Action: Propagate the four-channel wavepacket on the coupled excited-state potential energy surface using a grid-based method. Evaluate the kinetic energy operator with the fast Fourier transform (FFT) and use a second-order difference scheme for time propagation. At every timestep, compute the channel autocorrelation C_{00}^l(t) = ⟨φ^l(0)|φ^l(t)⟩ and the cross-correlations C_{v0}^l(t) = ⟨φ_v^l|φ^l(t)⟩ for v=1..5 up to the final time. The inputs (potentials, couplings, initial wavepackets, promoted states) come from steps 01 and 03.
- Evidence: none

### Step 5: Compute Raman excitation profiles (overall REPs)
- Role: scored (load-bearing)
- Action: Fourier transform the time-domain correlation functions from step 04 to obtain channel-specific Raman amplitudes α_{v0}^l(ω). Sum over channels l to get total Raman amplitudes α_{v0}(ω) for v=1..5. Compute the overall Raman excitation profile intensities I_{v0}(ω) = ω ω_s^3 |α_{v0}(ω)|^2 as a function of incident wavelength. Output the overall REP curves for the fundamental (v=1) and overtones (v=2,3,4,5) as a CSV.
- Output file: `/app/outputs/overall_rep.csv`
- Format: csv
- Contract: wavelength_nm (float), intensity_fundamental (float), intensity_overtone_2 (float), intensity_overtone_3 (float), intensity_overtone_4 (float), intensity_overtone_5 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/overall_rep.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### overall_rep.csv
- path: `/app/outputs/overall_rep.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Overall Raman excitation profiles (REPs) for HI, containing the incident wavelength and the total intensity for the fundamental v=0→1 and overtone v=0→2,3,4,5 transitions. The intensities must be in consistent arbitrary units. The file is scored by comparing the shape, dip position, and overtone trend to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `intensity_fundamental`, `intensity_overtone_2`, `intensity_overtone_3`, `intensity_overtone_4`, `intensity_overtone_5`
  - `units`:
    - `wavelength_nm`: nm
    - `intensity_fundamental`: arbitrary units
    - `intensity_overtone_2`: arbitrary units
    - `intensity_overtone_3`: arbitrary units
    - `intensity_overtone_4`: arbitrary units
    - `intensity_overtone_5`: arbitrary units

Notes: Only the overall (summed over channels) REP curves are required; channel-specific REPs and photodissociation cross sections are not part of the scored output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "overall_rep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "intensity_fundamental",
          "intensity_overtone_2",
          "intensity_overtone_3",
          "intensity_overtone_4",
          "intensity_overtone_5"
        ],
        "units": {
          "wavelength_nm": "nm",
          "intensity_fundamental": "arbitrary units",
          "intensity_overtone_2": "arbitrary units",
          "intensity_overtone_3": "arbitrary units",
          "intensity_overtone_4": "arbitrary units",
          "intensity_overtone_5": "arbitrary units"
        }
      },
      "description": "Overall Raman excitation profiles (REPs) for HI, containing the incident wavelength and the total intensity for the fundamental v=0→1 and overtone v=0→2,3,4,5 transitions. The intensities must be in consistent arbitrary units. The file is scored by comparing the shape, dip position, and overtone trend to a hidden reference."
    }
  ],
  "notes": "Only the overall (summed over channels) REP curves are required; channel-specific REPs and photodissociation cross sections are not part of the scored output."
}
```

## How you are scored
A hidden verifier examines each required output artifact. For the REP file (overall_rep.csv), the verifier checks the following structural and quantitative properties: (i) the fundamental REP shows two maxima separated by a discernible dip; (ii) the dip centre wavelength is compared against an expected value within a hidden tolerance; (iii) the overtone REPs display increasingly deeper dips relative to the fundamental profile; and (iv) the overall intensity trends across the full wavelength range are consistent with a physically reasonable coupled‑channel calculation. The individual checks are combined with predetermined weights to yield the final reward. Merely reporting numbers copied from the literature is not sufficient; the generated curves must arise from a correctly executed simulation pipeline.
