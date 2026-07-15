# Monte Carlo Simulation of Hot-Electron Intraband Light Emission in InSb

## Problem background
In n-InSb, the application of a strong electric field drives electrons into nonequilibrium “hot” states. The far-infrared intraband light emission from these hot electrons depends on the electron distribution in momentum space. When the distribution becomes anisotropic (streaming along the field), the luminescence can become anisotropic and partially polarized. A second-order perturbation treatment yields emission probability formulas that account for the different scattering mechanisms: acoustic phonons, polar optical phonons, and ionized impurities. The goal of this reproduction is to implement a theoretical model that calculates the temperature-dependent photon emission intensities along the transverse and longitudinal directions relative to the electric field, and from them quantify the emission anisotropy and the degree of polarization.

## Approach
We use a one-particle Monte Carlo technique to simulate electron transport in n-InSb under a constant electric field of 100 V/cm. The simulation includes scattering by acoustic phonons (elastic), polar optical phonons (absorption and emission), and ionized impurities. For each scattering event the electron’s kinetic energy ε and the angle θ between the wave vector and the field direction are recorded. This ensemble of (ε,θ) samples the nonequilibrium electron distribution function.  
For each recorded event we compute the photon emission probability for the four scattering processes using the paper’s derived formulas, which depend on ε, θ, the photon energy Ω, and the observation geometry. The calculation covers the transverse direction (averaged over polarization) and the longitudinal direction (averaged over polarization), within the photon energy range corresponding to wavelengths 80–110 µm. The per-event probabilities are accumulated to obtain the energy-resolved transition rates R_s(Ω) for each mechanism.  
Multiplying by the photon spectral density and integrating over the photon energy yields the total photon number emitted per unit time for the transverse (I⟂) and longitudinal (I∥) directions. The procedure is repeated for a set of lattice temperatures spanning 10–140 K. Finally, the emission anisotropy K = I⟂/I∥ and the degree of polarization of the transverse emission D = (I⟂−I∥)/(I⟂+I∥) are calculated from the directional intensities.

## Reproduction target
Produce, for n-InSb under an electric field of 100 V/cm in the spectral range 80–110 µm, the following quantities as functions of lattice temperature T at the precise grid 10, 20, 30, …, 140 K:
- The total photon number (in arbitrary units) emitted in the transverse direction (P_transverse) and in the longitudinal direction (P_longitudinal).
- The anisotropy factor K = P_transverse / P_longitudinal.
- The degree of polarization D = (P_transverse − P_longitudinal)/(P_transverse + P_longitudinal).
Write the results to the two CSV files described below, following the exact column schemas.

## Assets

- n-InSb material parameters
- Python 3 with NumPy, SciPy, matplotlib
- Monte Carlo technique reference (Jacoboni and Reggiani)

## Workflow steps

### Step 1: Monte Carlo simulation of hot-electron transport
- Role: process
- Action: Run a one-particle Monte Carlo simulation of electron motion in n-InSb under an electric field of E = 100 V/cm, including scattering by acoustic phonons, polar optical phonons (absorption and emission), and ionized impurities. For each scattering event, record the electron kinetic energy ε and the angle θ between the wave vector and the field direction. Perform the simulation for the lattice temperatures 10, 20, 30, ..., 140 K. Accumulate at least 1e6 scattering events per temperature to obtain good statistics.
- Evidence: `/app/outputs/mc_log.txt`

### Step 2: Compute photon emission transition rates
- Role: process
- Action: For each recorded (ε, θ) from the simulation, compute the photon emission probability for the four scattering mechanisms (acoustic phonon, ionized impurity, optical phonon absorption, optical phonon emission) using the emission probability formulas in the paper. Perform the calculation for the required emission directions (transverse emission averaged over polarization, transverse emission for polarization parallel and perpendicular to the field, and longitudinal emission averaged). Accumulate the transition rate R_s(Ω) as a function of photon energy Ω, discretizing over the range corresponding to wavelengths 80–110 μm.
- Evidence: none

### Step 3: Integrate transition rates to obtain total photon numbers
- Role: process
- Action: Multiply each R_s(Ω) by the photon spectral density (e.g., blackbody distribution) and integrate over the photon energy range 11.3–15.5 meV. Sum contributions from all scattering mechanisms to obtain the total photon number emitted per unit time for the transverse direction (I⟂) and the longitudinal direction (I∥) at each temperature.
- Evidence: none

### Step 4: Save photon intensity temperature dependence
- Role: scored
- Action: Write the computed total photon numbers for the transverse and longitudinal directions as functions of lattice temperature to a CSV file.
- Output file: `/app/outputs/temperature_dependence.csv`
- Format: csv
- Contract: Columns: T (lattice temperature in K, numeric), P_transverse (photon number, numeric), P_longitudinal (photon number, numeric). Rows must be present for temperatures 10, 20, 30, ..., 140 K in ascending order.
- Scoring: scored by hidden verifier

### Step 5: Save anisotropy and polarization degree vs temperature
- Role: scored
- Action: From P_transverse and P_longitudinal, compute the anisotropy factor K = P_transverse / P_longitudinal and the degree of polarization D = (P_transverse - P_longitudinal) / (P_transverse + P_longitudinal) for each temperature. Write to CSV.
- Output file: `/app/outputs/anisotropy_and_polarization.csv`
- Format: csv
- Contract: Columns: T (lattice temperature in K, numeric), K (anisotropy factor, numeric), D (degree of polarization, numeric, between -1 and 1). Rows must be present for temperatures 10, 20, 30, ..., 140 K in ascending order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_dependence.csv`
- `/app/outputs/anisotropy_and_polarization.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_dependence.csv
- path: `/app/outputs/temperature_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Photon emission intensities (arbitrary units) for the transverse and longitudinal directions as a function of lattice temperature, obtained from the Monte Carlo simulation. Must contain one row for each T = 10, 20, 30, ..., 140 K in ascending order.
- schema:
  - `type`: table
  - `columns`:
    - `name`: T
    - `unit`: K
    - `name`: P_transverse
    - `unit`: arbitrary
    - `name`: P_longitudinal
    - `unit`: arbitrary

### anisotropy_and_polarization.csv
- path: `/app/outputs/anisotropy_and_polarization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Emission anisotropy K and degree of polarization D of the transverse emission as functions of lattice temperature, derived from the directional intensities. Must contain one row for each T = 10, 20, 30, ..., 140 K in ascending order.
- schema:
  - `type`: table
  - `columns`:
    - `name`: T
    - `unit`: K
    - `name`: K
    - `unit`: dimensionless
    - `name`: D
    - `unit`: dimensionless

Notes: The hidden checker compares the simulated intensity curves and the anisotropy/polarization values to reference data digitized from the paper's figures, using tolerances appropriate for independent Monte Carlo reproductions. The temperature grid is fixed at 10,20,…,140 K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "T",
            "unit": "K"
          },
          {
            "name": "P_transverse",
            "unit": "arbitrary"
          },
          {
            "name": "P_longitudinal",
            "unit": "arbitrary"
          }
        ]
      },
      "description": "Photon emission intensities (arbitrary units) for the transverse and longitudinal directions as a function of lattice temperature, obtained from the Monte Carlo simulation. Must contain one row for each T = 10, 20, 30, ..., 140 K in ascending order."
    },
    {
      "file": "anisotropy_and_polarization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "T",
            "unit": "K"
          },
          {
            "name": "K",
            "unit": "dimensionless"
          },
          {
            "name": "D",
            "unit": "dimensionless"
          }
        ]
      },
      "description": "Emission anisotropy K and degree of polarization D of the transverse emission as functions of lattice temperature, derived from the directional intensities. Must contain one row for each T = 10, 20, 30, ..., 140 K in ascending order."
    }
  ],
  "notes": "The hidden checker compares the simulated intensity curves and the anisotropy/polarization values to reference data digitized from the paper's figures, using tolerances appropriate for independent Monte Carlo reproductions. The temperature grid is fixed at 10,20,…,140 K."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares your CSV files against reference values obtained from an independent, accurate implementation of the Monte Carlo simulation. The verifier checks the reported P_transverse, P_longitudinal, K, and D at each temperature against the reference data, using tolerance margins that account for the inherent Monte Carlo noise and implementation variations. The per‑point scores are combined into a final reward that reflects the overall quality of your reproduction. Because the tolerances are set such that a simulation with genuine physics will pass while random or fabricated data will not, you must faithfully implement the scattering rates, emission probability formulas, and integration steps described in the workflow.
