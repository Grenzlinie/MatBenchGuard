# Simulation of Auger Electron Emission and Transmission Through Tip–Sample Electric Field

## Problem background
In a scanning probe electron energy spectrometer (SPEES), an STM tip biased at a negative voltage creates a strong localized electric field between the tip and the sample surface. Auger electrons emitted from the sample can be severely suppressed by this field, and it is unclear which electrons emerge from the field region, from which radial positions on the sample, and at what angles. Understanding these spatial and angular characteristics is essential for optimizing detection efficiency and spatial resolution of the spectrometer. The present task addresses the open quantitative question: what is the spatial distribution of detectable Auger electrons leaving the tip–sample field region, and how are these electrons distributed in elevation angle at the exit of the field?

## Approach
The approach simulates the entire emission and transport chain for Au NOO Auger electrons (69 eV) created by incident field‑emission electrons at 132 eV. The simulation has three parts:

1. **Elastic escape from the solid.** A Monte Carlo simulation of electron elastic transport inside gold, using screened Rutherford elastic scattering and Bethe continuous slowing‑down, computes the probability $P_{\mathrm{el}}(\theta_0)$ that an Auger electron generated beneath the surface reaches the surface elastically, as a function of its emission elevation angle $\theta_0$ (angle with the sample surface).

2. **Transmission through the tip–shield electric field.** An electrostatic model of the tip (a paraboloid apex + cone + parabolic base) inside a grounded cylindrical shield is built. The tip is biased at −132 V and the sample is grounded, with a tip–sample separation of 50 µm. Exact geometric dimensions of the tip, shield, and their arrangement are provided in the workflow steps. The Laplace equation is solved for the electric potential, and then 69 eV electrons are launched from a grid of radial positions $r_0$ (13–50 µm) and all emission angles $(\theta_0, \varphi_0)$. Each trajectory is tracked until the electron either exits the field region (radial position $>310$ µm with upward velocity) or is stopped. The fraction of escaped electrons yields the transmission probability $P_{\mathrm{S}}(r_0,\theta_0)$.

3. **Radial and angular profiles of detectable Auger electrons.** The incident electron beam profile $J_{\mathrm{S}}(r_0)$ is modelled as a Gaussian with full width at half maximum 15.5 µm (this profile is a given input). The relative detectable Auger electron intensity is computed as $J'_\mathrm{A}(r_0,\theta_0) = J_{\mathrm{S}}(r_0)\,P_{\mathrm{el}}(\theta_0)\,P_{\mathrm{S}}(r_0,\theta_0)$. This intensity is integrated over $\theta_0$ (0–90°) to obtain the radial profile $J'_\mathrm{A}(r_0)$. The raw trajectory data at the edge of the electric field are used to compile the angular intensity distribution $I(\theta)$ of outgoing electrons.

## Reproduction target
Carry out the complete simulation pipeline described in the workflow steps and produce two scored output files:

- `radial_profile.csv`: a table with columns `r0_um` (distance from sample centre in µm) and `Jprime_A` (relative detectable Auger intensity in arbitrary units). The radial profile encodes the spatial origin of electrons that escape the electric field.
- `angular_distribution.csv`: a table with columns `theta_deg` (elevation angle of outgoing electrons measured from the sample surface, in degrees, 0–90) and `I_theta` (relative intensity at that angle, arbitrary units). This distribution describes how the outgoing electrons are directed.

The goal is to produce artifacts whose physical shape and characteristics (peak location, width, angular concentration) reflect the true behaviour of the simulated Auger electron transport, as verified by the hidden checker.

## Assets

- Open-source electrostatic solver and particle tracer
- Monte Carlo electron transport code
- Python scientific stack: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Monte Carlo simulation of elastic escape probability P_el(θ0)
- Role: process
- Action: Run a Monte Carlo simulation to compute the probability P_el that an Auger electron generated inside Au reaches the surface elastically, as a function of emission elevation angle θ0. Use standard electron-solid interaction models (screened Rutherford elastic cross section, Bethe continuous slowing-down). The incident electron energy is 132 eV, Auger electron initial energy 69 eV, and the material is gold.
- Evidence: `/app/outputs/pel_distribution.csv`

### Step 2: Electrostatic tracing of Auger electrons through tip–shield electric field to obtain P_S(r0,θ0)
- Role: process
- Action: Build an electrostatic model of the tip (paraboloid apex + cone + parabolic base) inside a grounded cylindrical shield, with the tip biased at −132 V and the sample grounded, separated by 50 µm. The exact tip geometry is: a top paraboloid with focus p=100 nm, a middle cone with half-cone angle α=10°, and a base parabola of revolution with focus p=40 µm; the lengths of these three parts are 10, 213, and 97 µm respectively. The tip diameter is 420 µm, length 320 µm. The tip is shielded by a grounded metal cylinder with inner diameter 620 µm, and the tip extends 50 µm out of the shield. Solve for the electric potential, then launch 69 eV electrons from a grid of radial positions r0 (13–50 µm) and full range of emission angles (θ0, φ0). Track trajectories until they either exit the shield region (radial position >310 µm and upward velocity) or are stopped. Count the fraction that escape to obtain the transmission probability map P_S(r0,θ0).
- Evidence: `/app/outputs/ps_distribution.csv`

### Step 3: Radial profile of detectable Auger intensity J'_A(r0)
- Role: scored (load-bearing)
- Action: Combine the incident beam profile J_S(r0) (a Gaussian with FWHM=15.5 µm), the elastic escape probability P_el(θ0) (treated as constant for θ0>25° and zero below), and the transmission map P_S(r0,θ0) to compute J'_A(r0,θ0)=J_S·P_el·P_S. Integrate J'_A over θ0 (0–90°) to obtain the radial intensity profile J'_A(r0). Save the profile as a CSV with columns 'r0_um' and 'Jprime_A' (arbitrary units).
- Output file: `/app/outputs/radial_profile.csv`
- Format: csv
- Contract: r0_um: float (distance from sample center in µm), Jprime_A: float (relative intensity, arbitrary units)
- Scoring: scored by hidden verifier

### Step 4: Angular distribution of outgoing electrons and collection efficiency
- Role: scored
- Action: From the trajectory data at the edge of the electric field region, compile the elevation angle θ of each outgoing electron to form the angular intensity distribution I(θ). Save a CSV with columns 'theta_deg' (angle in degrees, 0–90) and 'I_theta' (arbitrary units). The checker will compute the collection efficiency ηC (fraction of electrons with θ<2.2°) from this distribution.
- Output file: `/app/outputs/angular_distribution.csv`
- Format: csv
- Contract: theta_deg: float (elevation angle in degrees), I_theta: float (relative intensity, arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/radial_profile.csv`
- `/app/outputs/angular_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### radial_profile.csv
- path: `/app/outputs/radial_profile.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Radial distribution of relative detectable Auger electron intensity J'_A(r0). The checker will locate the peak and compute the FWHM to compare with hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `r0_um`, `Jprime_A`
  - `units`:
    - `r0_um`: µm
    - `Jprime_A`: arbitrary

### angular_distribution.csv
- path: `/app/outputs/angular_distribution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Angular intensity distribution I(θ) of outgoing Auger electrons at the edge of the electric field. The checker will integrate this distribution to compute the collection efficiency ηC and compare with a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `theta_deg`, `I_theta`
  - `units`:
    - `theta_deg`: degrees
    - `I_theta`: arbitrary

Notes: The incident beam profile J_S(r0) is provided as a Gaussian with FWHM=15.5 µm; field emission simulation is not required. The exact geometry and parameters for the tip, shield, and sample are given in the instruction. The scored outputs are the radial profile and angular distribution; ηC is derived by the checker from the angular distribution. All intermediate process outputs must be produced by the agent; they are not provided as resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "radial_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r0_um",
          "Jprime_A"
        ],
        "units": {
          "r0_um": "µm",
          "Jprime_A": "arbitrary"
        }
      },
      "description": "Radial distribution of relative detectable Auger electron intensity J'_A(r0). The checker will locate the peak and compute the FWHM to compare with hidden reference values."
    },
    {
      "file": "angular_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta_deg",
          "I_theta"
        ],
        "units": {
          "theta_deg": "degrees",
          "I_theta": "arbitrary"
        }
      },
      "description": "Angular intensity distribution I(θ) of outgoing Auger electrons at the edge of the electric field. The checker will integrate this distribution to compute the collection efficiency ηC and compare with a hidden reference."
    }
  ],
  "notes": "The incident beam profile J_S(r0) is provided as a Gaussian with FWHM=15.5 µm; field emission simulation is not required. The exact geometry and parameters for the tip, shield, and sample are given in the instruction. The scored outputs are the radial profile and angular distribution; ηC is derived by the checker from the angular distribution. All intermediate process outputs must be produced by the agent; they are not provided as resources."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores each of the two scored artifacts. The verifier reads your output files and performs the following checks:

- For `radial_profile.csv`, the verifier extracts the radial position of the maximum intensity and the full width at half maximum (FWHM) and compares them against hidden expected values that correspond to a physically correct simulation.
- For `angular_distribution.csv`, the verifier computes the collection efficiency $\eta_C$ as $\eta_C = \int_{0}^{2.2^\circ} I(\theta)\,\mathrm{d}\theta \;\big/\; \int_{0}^{90^\circ} I(\theta)\,\mathrm{d}\theta$ and compares the result with a hidden reference. The angular distribution is also examined to ensure it is concentrated at small angles, as dictated by the field suppression.

Both checks are mandatory: each artifact must be present, in the correct CSV format, and contain physically plausible data. The two stages carry prescribed weights that sum to the final reward. Simply inserting a target number from external sources is insufficient — the artifacts must be generated by running the simulation pipeline as described in the workflow steps.
