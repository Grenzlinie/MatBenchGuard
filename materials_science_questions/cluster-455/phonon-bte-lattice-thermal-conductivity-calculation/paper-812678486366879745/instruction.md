# Strain-augmented Monte Carlo ray-tracing simulation of thermal conductivity in nanoporous silicon

## Problem background
Silicon phononic crystals (PnCs) with sub‑100 nm periodic arrays of through‑holes exhibit thermal conductivity far below the limit predicted by fully diffuse boundary scattering (the Casimir limit). This anomaly cannot be fully explained by conventional phonon particle scattering from surface roughness or by coherent wave interference effects. The anomalous thermal transport has been linked to local elastic softening of the silicon, which can reduce phonon group velocity and promote additional internal phonon scattering due to non‑uniform elasticity. A quantitative understanding of this mechanism requires determining how strain‑induced changes in elastic modulus and lattice thermal conductivity of silicon translate into the effective thermal transport in nanostructured holey films.

## Approach
The reproduction follows a two‑stage physics‑based workflow. First, first‑principles lattice‑dynamics calculations (density‑functional theory with Quantum ESPRESSO, Phonopy, and the Boltzmann transport equation solver ShengBTE) are performed for single‑crystal silicon under isotropic tensile strain to obtain the strain‑dependent Young's modulus and lattice thermal conductivity at 300 K. This provides the reference relationships needed to map elastic softening to thermal transport changes. Second, a three‑dimensional Monte‑Carlo ray‑tracing (MCRT) simulation is implemented to compute phonon thermal transport in PnC films with periodic through‑hole arrays. The MCRT assumes fully diffuse boundary scattering and uses bulk Si phonon properties. For each pitch, an effective strain is identified from experimentally measured normalized Young's modulus and the first‑principles strain‑modulus relationship. The strain‑dependent sound velocity reduction factor (proportional to the square root of the modulus ratio) is then applied to the low‑frequency phonon group velocities, and the change in scattering rates due to elastic non‑uniformity is incorporated. By comparing the Casimir‑limit thermal conductivity κ_sim (no strain) with the strain‑incorporated κ_strain, one can evaluate how elastic softening affects the thermal conductivity trend across pitches ranging from 34 nm to 2000 nm.

## Reproduction target
The goal is to produce two main results: (1) a table of strain‑dependent elastic modulus and lattice thermal conductivity of silicon at 300 K for strains 0 %, 2 %, 4 %, 6 %, 8 %, and 10 % from first‑principles calculations; (2) a table for six PnC pitches (34 nm, 100 nm, 200 nm, 500 nm, 1000 nm, 2000 nm) containing the Casimir‑limit thermal conductivity κ_sim and the strain‑incorporated thermal conductivity κ_strain. From these, compute the normalized ratio κ_strain/κ_sim and show that it decreases with decreasing pitch, following a trend that is consistent with the strain‑modulus relationship established in part (1).

## Assets

- PnC geometry parameters
- Experimental normalized Young's modulus
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- ShengBTE: https://www.shengbte.org/

## Workflow steps

### Step 1: Strain-dependent first-principles lattice dynamics
- Role: scored (load-bearing)
- Action: Perform DFT calculations with Quantum ESPRESSO for single-crystal silicon at lattice constants corresponding to isotropic tensile strains s = 0%, 2%, 4%, 6%, 8%, 10% (a = 5.4021, 5.5101, 5.6182, 5.7262, 5.8343, 5.9423 Å). Use Phonopy to obtain harmonic force constants and phonon dispersions, and ShengBTE to compute lattice thermal conductivity at 300 K and the phonon group velocities and relaxation times. Compute the Young’s modulus for each strain from the elastic constants. Write the results to step_01_first_principles_results.csv. Additionally, save the full phonon data (dispersion, group velocities, relaxation times, cumulative thermal conductivity vs. MFP) for the 0% strain case to a file phonon_data_0pct.npz (needed for step 02).
- Output file: `/app/outputs/step_01_first_principles_results.csv`
- Format: csv
- Contract: strain_percent (integer), lattice_constant_angstrom (float), elastic_modulus_GPa (float), thermal_conductivity_W_mK (float)
- Scoring: scored by hidden verifier

### Step 2: MCRT simulation with strain-augmented sound velocity
- Role: scored
- Action: 1. Load the PnC geometry from the provided resource (res_pnc_geometry) and the experimental normalized modulus from (res_exp_normalized_modulus). 2. Using the bulk Si phonon properties saved in step_01 (0% strain), implement a 3D Monte Carlo ray-tracing code for phonon thermal conductivity assuming fully diffuse boundary scattering. For each pitch, compute the Casimir-limit thermal conductivity κ_sim. 3. Map each pitch to an effective strain rate s by linearly interpolating between the experimental normalized modulus and the first-principles strain-modulus relationship obtained from step_01. For pitches smaller than the smallest measured modulus, extrapolate linearly. 4. For each pitch, apply the sound-velocity reduction factor (E(s)/E(0))^{1/2} as a scaling factor for the low-frequency group velocities, and also consider the change in phonon scattering rates due to elastic non-uniformity (modelled as a factor on the phonon MFP). Compute the strain-incorporated thermal conductivity κ_strain. 5. Write the final results to step_02_kappa_results.csv.
- Output file: `/app/outputs/step_02_kappa_results.csv`
- Format: csv
- Contract: pitch_nm (integer), kappa_sim (float, W/mK), kappa_strain (float, W/mK)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_first_principles_results.csv`
- `/app/outputs/step_02_kappa_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_first_principles_results.csv
- path: `/app/outputs/step_01_first_principles_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Strain-dependent elastic modulus and lattice thermal conductivity for single-crystal Si at 300 K. The checker compares values to hidden reference within tolerance and verifies monotonic decrease with strain.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `lattice_constant_angstrom`, `elastic_modulus_GPa`, `thermal_conductivity_W_mK`
  - `units`:
    - `elastic_modulus_GPa`: GPa
    - `thermal_conductivity_W_mK`: W/mK

### step_02_kappa_results.csv
- path: `/app/outputs/step_02_kappa_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated thermal conductivity for each pitch: Casimir limit κ_sim and strain-incorporated κ_strain. The checker computes the ratio κ_strain/κ_sim and compares its pitch dependence against a hidden experimental trend (mean absolute error).
- schema:
  - `type`: table
  - `required_columns`: `pitch_nm`, `kappa_sim`, `kappa_strain`
  - `units`:
    - `kappa_sim`: W/mK
    - `kappa_strain`: W/mK

Notes: The full phonon data file phonon_data_0pct.npz is required as an intermediate for step_02 but is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_first_principles_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "lattice_constant_angstrom",
          "elastic_modulus_GPa",
          "thermal_conductivity_W_mK"
        ],
        "units": {
          "elastic_modulus_GPa": "GPa",
          "thermal_conductivity_W_mK": "W/mK"
        }
      },
      "description": "Strain-dependent elastic modulus and lattice thermal conductivity for single-crystal Si at 300 K. The checker compares values to hidden reference within tolerance and verifies monotonic decrease with strain."
    },
    {
      "file": "step_02_kappa_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pitch_nm",
          "kappa_sim",
          "kappa_strain"
        ],
        "units": {
          "kappa_sim": "W/mK",
          "kappa_strain": "W/mK"
        }
      },
      "description": "Simulated thermal conductivity for each pitch: Casimir limit κ_sim and strain-incorporated κ_strain. The checker computes the ratio κ_strain/κ_sim and compares its pitch dependence against a hidden experimental trend (mean absolute error)."
    }
  ],
  "notes": "The full phonon data file phonon_data_0pct.npz is required as an intermediate for step_02 but is not scored."
}
```

## How you are scored
Your deliverables are scored independently by a hidden verifier. Step 1 is scored by comparing your reported elastic modulus and thermal conductivity against a physical reference: the values must be monotonic with strain and agree within a tolerance that accounts for typical variability in first‑principles toolchains. Step 2 is scored by evaluating the trend of the normalized ratio κ_strain/κ_sim versus pitch. The verifier holds an experimental reference trend and measures how well your computed ratio reproduces this trend (e.g., using mean absolute error). Each step carries a portion of the total reward. Simply reporting numbers without performing the actual computations will not satisfy the scoring criteria.
