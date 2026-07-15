# Numerical electron mobility calculation for n-type silicon with RPA screening and phase shifts

## Problem background
Carrier mobility in doped semiconductors, especially n‑type silicon, is limited by scattering from ionized impurities and phonons. Conventional perturbative models (Born approximation) often fail at high doping levels and at low temperatures, where non‑degenerate or semi‑degenerate electron statistics demand a more exact treatment. The problem is to compute the electron mobility from first principles by combining a finite‑temperature random‑phase approximation (RPA) for dielectric screening, an exact phase‑shift treatment of impurity scattering, and an iterative solution of the linearized Boltzmann transport equation that includes elastic (acoustic) and inelastic (optical) phonon scattering. The result serves as a benchmark for how screening, multiple valleys, and non‑perturbative scattering jointly govern the transport properties of majority‑carrier electrons in n‑type silicon.

## Approach
The approach is a numerical pipeline that proceeds from fundamental material constants to the final mobility. Silicon is modelled with isotropic effective‑mass bands and degenerate conduction‑band valleys. For each doping density and temperature, the chemical potential is determined self‑consistently so that the electron density matches the doping. The RPA dielectric function of the free‑carrier gas is computed as a function of wave‑vector, and the resulting screened impurity potential is obtained by a Fourier‑transform integration. Partial‑wave phase shifts are then calculated by solving the radial Schrödinger equation with this screened potential for several angular momenta. Impurity scattering rates are built from the phase shifts, while phonon scattering rates are computed from deformation‑potential theory, treating acoustic phonon scattering as elastic and optical phonon scattering as inelastic. The linearized Boltzmann equation is solved iteratively using Rode's method, yielding the perturbed distribution function. Finally, the electron mobility is obtained from the conductivity integral evaluated with the converged distribution function and the carrier density. All numerical work can be done with standard open‑source libraries (NumPy, SciPy) and requires only the publicly known material parameters of silicon.

## Reproduction target
Compute the electron mobility (in cm²/V·s) of n‑type silicon for the following doping concentrations: 1×10¹⁸, 5×10¹⁸, 1×10¹⁹, 5×10¹⁹, and 1×10²⁰ cm⁻³, at two temperatures: 300 K and 77 K. The workflow must deliver a CSV file (`step_01_mobility.csv`) with columns `temperature_K`, `doping_concentration_cm3`, and `mobility_cm2_Vs`, containing exactly ten rows (five doping levels × two temperatures). The file will be scored by the hidden verifier against independently determined reference values.

## Assets

- NumPy: numpy
- SciPy: scipy
- Silicon material parameters

## Workflow steps

### Step 1: Specify silicon material parameters
- Role: process
- Action: Define and record the required silicon material parameters from standard references: electron effective mass, high-frequency dielectric constant, valley degeneracy, acoustic and optical deformation potentials, optical phonon energy, sound velocity, and mass density.
- Evidence: none

### Step 2: Determine chemical potential and equilibrium distribution
- Role: process
- Action: For each doping concentration (1E18,5E18,1E19,5E19,1E20 cm^-3) and temperature (300 K and 77 K), solve numerically for the chemical potential μ such that the carrier density equals the doping concentration, assuming isotropic effective-mass bands with the specified valley degeneracy. Compute the equilibrium Fermi-Dirac distribution f(k).
- Evidence: none

### Step 3: Compute finite‑temperature RPA dielectric function
- Role: process
- Action: Numerically integrate the RPA expression to obtain the electron-gas dielectric function ε_RPA(q) as a function of wavevector q for each doping concentration and temperature, using the chemical potential and equilibrium distribution from step 2.
- Evidence: none

### Step 4: Compute screened impurity potential V(r)
- Role: process
- Action: Perform the Fourier-transform integral of v_q / ε_RPA(q) to obtain the real-space screened potential V(r) for a unit-charge impurity, for each doping concentration and temperature.
- Evidence: none

### Step 5: Compute impurity scattering phase shifts
- Role: process
- Action: Numerically solve the radial Schrödinger scattering problem with V(r) to obtain partial-wave phase shifts δ_l(k) for a sufficient number of angular momenta and a grid of wavevector magnitudes relevant to the occupation.
- Evidence: none

### Step 6: Compute impurity and phonon scattering rates
- Role: process
- Action: Convert the phase shifts into the impurity scattering kernel S_imp(k,k') using standard partial-wave expressions. Compute phonon scattering rates S_ph(k,k') using deformation-potential theory: treat acoustic phonon scattering as elastic and optical phonon scattering as inelastic, using the material parameters from step 1.
- Evidence: none

### Step 7: Solve linearized Boltzmann equation via Rode's method
- Role: process
- Action: Implement Rode's iterative procedure to solve the linearized Boltzmann transport equation for the perturbed distribution g(k), using the total scattering rates (impurity + phonon) and the equilibrium distribution. Iterate until self-consistency.
- Evidence: none

### Step 8: Compute and save electron mobility
- Role: scored (load-bearing)
- Action: Calculate the electron mobility from the converged g(k) by evaluating the conductivity integral and dividing by the carrier density. Write the resulting mobility values for the five doping concentrations at both 300 K and 77 K to step_01_mobility.csv.
- Output file: `/app/outputs/step_01_mobility.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float), doping_concentration_cm3 (float), mobility_cm2_Vs (float). Exactly 10 rows (5 concentrations × 2 temperatures).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mobility.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mobility.csv
- path: `/app/outputs/step_01_mobility.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electron mobility in n-type silicon computed from the full first-principles numerical pipeline: RPA dielectric screening, exact phase-shift impurity scattering, deformation-potential phonon scattering, and Rode's iterative Boltzmann solution. The checker compares each mobility value against hidden reference values (extracted from the paper's figures) with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `doping_concentration_cm3`, `mobility_cm2_Vs`
  - `units`:
    - `temperature_K`: K
    - `doping_concentration_cm3`: cm^-3
    - `mobility_cm2_Vs`: cm^2/Vs

Notes: Only the majority‑carrier electron mobility for n‑type silicon is required; minority‑carrier, hole, and local‑field‑correction calculations are explicitly out of scope. The hidden gold consists of mobility values read from the published figures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mobility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "doping_concentration_cm3",
          "mobility_cm2_Vs"
        ],
        "units": {
          "temperature_K": "K",
          "doping_concentration_cm3": "cm^-3",
          "mobility_cm2_Vs": "cm^2/Vs"
        }
      },
      "description": "Electron mobility in n-type silicon computed from the full first-principles numerical pipeline: RPA dielectric screening, exact phase-shift impurity scattering, deformation-potential phonon scattering, and Rode's iterative Boltzmann solution. The checker compares each mobility value against hidden reference values (extracted from the paper's figures) with a relative tolerance."
    }
  ],
  "notes": "Only the majority‑carrier electron mobility for n‑type silicon is required; minority‑carrier, hole, and local‑field‑correction calculations are explicitly out of scope. The hidden gold consists of mobility values read from the published figures."
}
```

## How you are scored
Your scored output (`step_01_mobility.csv`) is evaluated by a hidden verifier that independently compares each mobility value you report to reference benchmarks using a relative tolerance. Full credit is earned if every entry lies within the tolerance; otherwise the reward is proportional to the number of entries that pass. The verifier only reads your artifacts and does not re‑execute your code. Simply copying or guessing the paper’s numbers will not guarantee a passing score — the tolerance is chosen to reward honest reproduction while accounting for numerical spread across different implementations.
