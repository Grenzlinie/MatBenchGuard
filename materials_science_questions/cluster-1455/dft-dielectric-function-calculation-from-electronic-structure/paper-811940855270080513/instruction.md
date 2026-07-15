# Dielectric function computation from effective Hamiltonian MD

## Problem background
The terahertz dielectric response of ferroelectric BaTiO₃ in its paraelectric phase is important for applications, but the number and nature of the modes that contribute to this response have been heavily debated. Atomistic simulations based on a first-principles effective Hamiltonian can, in principle, predict the full frequency- and temperature-dependent complex dielectric function, yet such a computation has not been performed before. This task aims to fill that gap by computing the complex permittivity ε(ν) from effective-Hamiltonian molecular dynamics and characterizing the spectral features that emerge.

## Approach
We use an effective Hamiltonian that captures the local soft-mode displacement and strain degrees of freedom of BaTiO₃, with parameters taken from the literature. Molecular dynamics (MD) simulations of a 14×14×14 supercell are carried out in the paraelectric phase. After equilibration in the NPT ensemble, the homogeneous strain is frozen and the system is evolved in the NVE ensemble while the total dipole moment M(t) is recorded. From the dipole trajectory we compute the dipole autocorrelation function ⟨M(t)·M(0)⟩ using an overlap technique. The fluctuation–dissipation theorem then yields the complex dielectric function ε(ν)=ε′(ν)+iε″(ν). To quantify the spectral content, ε(ν) is fitted with a sum of classical damped harmonic oscillators, extracting their frequencies, damping, and oscillator strengths.

## Reproduction target
1. Compute the complex dielectric function ε(ν) (real part ε′ and imaginary part ε″) at the two temperatures 440 K and 470 K over the frequency range 1–150 cm⁻¹, and write the spectra to `epsilon_spectra.csv`. 2. Fit the simulated ε(ν) at each temperature with a model consisting of two damped harmonic oscillators. Output the oscillator parameters (ν₁, γ₁, S₁, ν₂, γ₂, S₂) and the peak frequencies ν₁′ and ν₂′ of ε″ to `mode_parameters.csv`. The objective is to obtain a self-consistent description of the dielectric response; the spectra should exhibit plausible multi-mode structure, and the fitted parameters must be consistent with the ε″ peaks computed directly from the spectra.

## Assets

- Effective Hamiltonian parameters for BaTiO3 (force-constant matrix based): 10.1103/PhysRevB.73.144105
- Python numerical libraries (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Load effective Hamiltonian and set up the supercell
- Role: process
- Action: Retrieve the effective Hamiltonian parameters for BaTiO3 from the published paper, construct the effective Hamiltonian model (local soft-mode and strain variables), and define the 14×14×14 supercell system.
- Evidence: `/app/outputs/effective_hamiltonian_summary.txt`

### Step 2: Run MD simulations to generate dipole moment trajectories
- Role: process
- Action: For each target temperature (440 K and 470 K): equilibrate in the NPT ensemble for 20 000 steps (1 fs timestep) using an Evans‑Hoover thermostat and the PV barostat term, then switch to the NVE ensemble with frozen homogeneous strain (5 000 equilibration steps + 2 975 000 production steps). Record the total dipole moment time series M(t) at every 4 fs.
- Evidence: `/app/outputs/dipole_trajectory_440K.npy, dipole_trajectory_470K.npy`

### Step 3: Compute complex dielectric function
- Role: scored (load-bearing)
- Action: From the dipole moment time series, compute the dipole autocorrelation function ⟨M(t)·M(0)⟩ via the overlap approach (10 000 individual functions, time range 0–8.2 ps, step 4 fs). Perform the numerical Fourier transform and apply the fluctuation–dissipation formula to obtain ε'(ν) and ε''(ν) for frequencies 1–150 cm⁻¹ at both temperatures. Write the spectra to epsilon_spectra.csv.
- Output file: `/app/outputs/epsilon_spectra.csv`
- Format: csv
- Contract: Columns: temperature (K), frequency (cm⁻¹), epsilon_real (dimensionless), epsilon_imag (dimensionless). One row per frequency point.
- Scoring: scored by hidden verifier

### Step 4: Fit two damped harmonic oscillators to ε(ν)
- Role: scored
- Action: Fit the simulated ε(ν) (from epsilon_spectra.csv) to the sum of two classical damped harmonic oscillators for both temperatures. Extract the mode frequencies (ν₁, ν₂), damping constants (γ₁, γ₂), oscillator strengths (S₁, S₂), and compute the peak positions ν₁' and ν₂' of the imaginary part. Write all fitted parameters to mode_parameters.csv.
- Output file: `/app/outputs/mode_parameters.csv`
- Format: csv
- Contract: Columns: temperature (K), nu1 (cm⁻¹), gamma1 (cm⁻¹), S1 (dimensionless), nu2 (cm⁻¹), gamma2 (cm⁻¹), S2 (dimensionless), nu1_prime (cm⁻¹), nu2_prime (cm⁻¹). One row per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/epsilon_spectra.csv`
- `/app/outputs/mode_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### epsilon_spectra.csv
- path: `/app/outputs/epsilon_spectra.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Complex dielectric function spectra at 440 K and 470 K. The checker will recompute the peak positions of ε''(ν) and compare them to the paper's reported values.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `frequency`, `epsilon_real`, `epsilon_imag`
  - `units`:
    - `temperature`: K
    - `frequency`: cm⁻¹
    - `epsilon_real`: dimensionless
    - `epsilon_imag`: dimensionless

### mode_parameters.csv
- path: `/app/outputs/mode_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted two‑oscillator parameters and peak frequencies. The checker will compare the submitted ν₁' and ν₂' against the paper's reference values.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `nu1`, `gamma1`, `S1`, `nu2`, `gamma2`, `S2`, `nu1_prime`, `nu2_prime`
  - `units`:
    - `temperature`: K
    - `nu1`: cm⁻¹
    - `gamma1`: cm⁻¹
    - `S1`: dimensionless
    - `nu2`: cm⁻¹
    - `gamma2`: cm⁻¹
    - `S2`: dimensionless
    - `nu1_prime`: cm⁻¹
    - `nu2_prime`: cm⁻¹

Notes: The effective Hamiltonian parameters are from DOI 10.1103/PhysRevB.73.144105. The MD simulation is computationally heavy; the agent should run the full production using adequate compute resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "epsilon_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "frequency",
          "epsilon_real",
          "epsilon_imag"
        ],
        "units": {
          "temperature": "K",
          "frequency": "cm⁻¹",
          "epsilon_real": "dimensionless",
          "epsilon_imag": "dimensionless"
        }
      },
      "description": "Complex dielectric function spectra at 440 K and 470 K. The checker will recompute the peak positions of ε''(ν) and compare them to the paper's reported values."
    },
    {
      "file": "mode_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "nu1",
          "gamma1",
          "S1",
          "nu2",
          "gamma2",
          "S2",
          "nu1_prime",
          "nu2_prime"
        ],
        "units": {
          "temperature": "K",
          "nu1": "cm⁻¹",
          "gamma1": "cm⁻¹",
          "S1": "dimensionless",
          "nu2": "cm⁻¹",
          "gamma2": "cm⁻¹",
          "S2": "dimensionless",
          "nu1_prime": "cm⁻¹",
          "nu2_prime": "cm⁻¹"
        }
      },
      "description": "Fitted two‑oscillator parameters and peak frequencies. The checker will compare the submitted ν₁' and ν₂' against the paper's reference values."
    }
  ],
  "notes": "The effective Hamiltonian parameters are from DOI 10.1103/PhysRevB.73.144105. The MD simulation is computationally heavy; the agent should run the full production using adequate compute resources."
}
```

## How you are scored
A hidden verifier independently assesses each scored artifact and combines the results into a final reward. For `epsilon_spectra.csv`, the verifier checks that ε″(ν) exhibits a well-defined peak structure, that ε′(ν) follows the expected frequency and temperature trends, and that the peak positions are physically sensible. For `mode_parameters.csv`, the verifier validates that the reported peak frequencies ν₁′ and ν₂′ are consistent with the peaks visible in the submitted ε″ spectra and that the oscillator parameters are self-consistent. The check does not require matching a specific published number; instead it rewards spectral features and internal consistency that arise from genuinely running the molecular dynamics pipeline. Simply reporting the paper's claimed values without supporting spectra will receive little or no credit.
