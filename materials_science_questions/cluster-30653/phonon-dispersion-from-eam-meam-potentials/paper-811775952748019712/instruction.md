# EAM Potential for Uranium: Reproducing Thermophysical Properties via MD Simulations

## Problem background
Uranium is a heavy actinide with strongly temperature- and density-dependent thermophysical behaviour. Reliable predictions of its liquid properties, shock compression response, and melting curve require accurate interatomic potentials that can be used in molecular-dynamics simulations. In this task you will implement an embedded-atom model (EAM) potential tailored for uranium and perform large-scale MD simulations to compute a comprehensive set of thermophysical properties across a wide range of conditions — from near‑melting liquid at ambient pressure up to 5000 K, along the shock Hugoniot to pressures of several hundred GPa, and the melting line at high compression. The computed quantities include density, pressure, internal energy, bulk modulus, self‑diffusion coefficient, dynamic viscosity, and melting temperature.

## Approach
The interatomic interaction is described by an EAM potential whose total energy is the sum of a pair potential and an embedding function. The pair term is a Morse function φ(r) = ε[exp(-2α(r/d-1)) - 2 exp(-α(r/d-1))] with parameters ε, d, and α. The embedding function Φ(ρ) is a piecewise polynomial defined over a set of knot densities; it depends on an effective electron density ρ_i = Σ_j ψ(r_ij) where the density kernel ψ(r) decays exponentially. All potential parameters are listed in the implementation step. The MD simulations will be run with the LAMMPS package. Liquid uranium is modelled in the NVT or NPT ensemble at several temperatures and the experimental densities that keep the pressure near zero. From the trajectories you will extract the time‑averaged potential energy, pressure, isothermal bulk modulus (via pressure‑volume perturbations), self‑diffusion coefficient (from mean‑square displacement), and dynamic viscosity (via the Stokes–Einstein relation with a fixed ion radius). Solid bcc uranium is equilibrated at 298 K. Shock‑compressed states are simulated at constant volume with given compression ratios and temperatures. The melting curve is determined by the reheating method: a defective bcc lattice is heated incrementally and the melting point is identified from the maximum structure factor S(K).

## Reproduction target
Produce four CSV files in /app/outputs, each with the specified columns and rows:

1. `liquid_properties.csv` – nine rows for liquid uranium at temperatures 1406, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000 K, each at its corresponding experimental density given in the step. Columns: `T(K)`, `density(g/cm3)`, `pressure(GPa)`, `U_EAM(kJ/mol)`, `K_T(GPa)`, `diffusion(cm2/s)`, `viscosity(cP)`.
2. `crystal_properties.csv` – a single row for bcc uranium at 298 K. Columns: `state`, `density(g/cm3)`, `U_EAM(kJ/mol)`, `pressure(GPa)`. The state must be the string `bcc`.
3. `shock_hugoniot.csv` – twelve rows at compression ratios Z (V/V₀) = 0.900, 0.800, 0.768, 0.750, 0.718, 0.700, 0.693, 0.668, 0.653, 0.6423, 0.628, 0.5834, each with its own model temperature as listed in the step. Columns: `Z`, `pressure(GPa)`, `energy(kJ/mol)`. The energy is the total internal energy (potential plus kinetic) and does not include any electronic excitation contribution.
4. `melting_temperatures.csv` – six rows for compressions Z = 0.90, 0.80, 0.70, 0.65, 0.60, 0.55. Columns: `Z`, `pressure(GPa)`, `Tmelt(K)`. Determine the melting temperature by the reheating method described in the approach; also record the average pressure during the transition.

All fields are floating‑point numbers except the state column. The checker expects exactly these columns and exactly the listed rows in the given order.

## Assets

- LAMMPS: https://lammps.sandia.gov/download.html

## Workflow steps

### Step 1: EAM potential implementation and LAMMPS input preparation
- Role: process
- Action: Implement the EAM potential for uranium using the functional forms and parameters specified in the paper. Produce a LAMMPS input script (or implement a custom pair style) that computes the total potential energy as sum_i Φ(ρ_i) + sum_{i<j} φ(r_ij), with ρ_i = sum_j ψ(r_ij). Use the Morse pair potential φ(r) = ε[exp(-2α(r/d-1)) - 2 exp(-α(r/d-1))] with ε=0.209 eV, d=3.3318 Å, α=4.100; the density kernel ψ(r) = p1 exp(-p2 r) with p1=5.5619, p2=1.3850; and the piecewise embedding function Φ(ρ) given by Eqs. (4)-(8) with knot densities ρ1=0.900, ρ2=0.800, ρ3=0.700, ρ4=0.600, ρ5=0.500, ρ6=0.400, ρ7=0.100, ρ8=1.20, ρ9=2.00, coefficients a1=-3.5659, c1=0.2753, c2=-0.100, c3=-0.200, c4=3.65, c5=-1.850, c6=0.500, c7=10.60, c8=0.050, c9=1.62, c10=2.24, and exponents m=1.80, n=1.71. Set cut-off radius to 12.20 Å.
- Evidence: `/app/outputs/eam_lammps_input.lammps`

### Step 2: Liquid uranium properties at low pressure
- Role: scored (load-bearing)
- Action: Run MD simulations for liquid uranium at the following temperatures and experimental densities: (1406 K, 17.226 g/cm³), (1500 K, 17.06 g/cm³), (2000 K, 16.18 g/cm³), (2500 K, 15.33 g/cm³), (3000 K, 14.53 g/cm³), (3500 K, 13.76 g/cm³), (4000 K, 13.03 g/cm³), (4500 K, 12.3 g/cm³), (5000 K, 11.7 g/cm³). Use NPT or NVT dynamics to maintain ~zero pressure. Extract from the trajectory: (a) potential energy U_EAM (kJ/mol) – the average EAM potential energy plus kinetic energy (3/2 RT), (b) pressure (GPa), (c) isothermal bulk modulus K_T (GPa) from the pressure–volume derivative, (d) self-diffusion coefficient D (cm²/s) from the slope of mean-square displacement vs time, (e) dynamic viscosity η (cP) computed via Stokes–Einstein η = k_B T / (6 π r_a D) with ion radius r_a = 0.792 Å. Output these values to liquid_properties.csv.
- Output file: `/app/outputs/liquid_properties.csv`
- Format: csv
- Contract: CSV header: T(K),density(g/cm3),pressure(GPa),U_EAM(kJ/mol),K_T(GPa),diffusion(cm2/s),viscosity(cP). Nine data rows for the listed temperatures. All fields are floating-point numbers.
- Scoring: scored by hidden verifier

### Step 3: Bcc crystal properties at 298 K
- Role: scored
- Action: Set up a bcc uranium crystal of about 1024 atoms at 298 K with zero external pressure. Perform an MD run and measure the equilibrium density, potential energy U_EAM (kJ/mol), and pressure (GPa). Write a single-row CSV file crystal_properties.csv.
- Output file: `/app/outputs/crystal_properties.csv`
- Format: csv
- Contract: CSV header: state,density(g/cm3),U_EAM(kJ/mol),pressure(GPa). One row with state='bcc'.
- Scoring: scored by hidden verifier

### Step 4: Shock Hugoniot states
- Role: scored
- Action: For the following compressed states (Z = V/V₀) and the corresponding model temperatures: (0.900, 420 K), (0.800, 810 K), (0.768, 1075 K), (0.750, 1170 K), (0.718, 1910 K), (0.700, 2540 K), (0.693, 2830 K), (0.668, 4010 K), (0.653, 4825 K), (0.6423, 5515 K), (0.628, 5810 K), (0.5834, 9045 K), run NVT simulations at constant volume. For each state compute the pressure and the total internal energy (U_EAM = potential energy + kinetic energy, in kJ/mol) – do not include the electron excitation contribution U_el. Output the results to shock_hugoniot.csv.
- Output file: `/app/outputs/shock_hugoniot.csv`
- Format: csv
- Contract: CSV header: Z,pressure(GPa),energy(kJ/mol). Twelve rows in the order listed. All fields are floating-point numbers.
- Scoring: scored by hidden verifier

### Step 5: Melting temperatures at high compression
- Role: scored
- Action: For each compression ratio Z = 0.90, 0.80, 0.70, 0.65, 0.60, 0.55, determine the melting temperature using the reheating method: prepare a defective bcc lattice, run isothermal MD at several temperatures, monitor the maximum structure factor S(K) as a function of temperature, and identify the melting temperature. Also record the average pressure during the melting transition. Output the six (Z, pressure, Tmelt) rows to melting_temperatures.csv.
- Output file: `/app/outputs/melting_temperatures.csv`
- Format: csv
- Contract: CSV header: Z,pressure(GPa),Tmelt(K). Six rows for the listed Z values. All fields are floating-point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/liquid_properties.csv`
- `/app/outputs/crystal_properties.csv`
- `/app/outputs/shock_hugoniot.csv`
- `/app/outputs/melting_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### liquid_properties.csv
- path: `/app/outputs/liquid_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed liquid uranium properties at nine temperatures along the p≈0 isobar.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `density(g/cm3)`, `pressure(GPa)`, `U_EAM(kJ/mol)`, `K_T(GPa)`, `diffusion(cm2/s)`, `viscosity(cP)`

### crystal_properties.csv
- path: `/app/outputs/crystal_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Properties of bcc crystalline uranium at 298 K.
- schema:
  - `type`: table
  - `required_columns`: `state`, `density(g/cm3)`, `U_EAM(kJ/mol)`, `pressure(GPa)`

### shock_hugoniot.csv
- path: `/app/outputs/shock_hugoniot.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pressure and energy along the shock Hugoniot at twelve compression ratios.
- schema:
  - `type`: table
  - `required_columns`: `Z`, `pressure(GPa)`, `energy(kJ/mol)`

### melting_temperatures.csv
- path: `/app/outputs/melting_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Melting temperatures at seven high-pressure states including the ambient-pressure point, determined by the reheating method.
- schema:
  - `type`: table
  - `required_columns`: `Z`, `pressure(GPa)`, `Tmelt(K)`

Notes: All outputs are compared to the paper-reported values within tolerances suitable for MD run-to-run variability. The electron excitation contribution U_el is not part of the scored energy outputs; the agent must report only the EAM potential energy plus kinetic energy (U_EAM).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "liquid_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "density(g/cm3)",
          "pressure(GPa)",
          "U_EAM(kJ/mol)",
          "K_T(GPa)",
          "diffusion(cm2/s)",
          "viscosity(cP)"
        ]
      },
      "description": "Computed liquid uranium properties at nine temperatures along the p≈0 isobar."
    },
    {
      "file": "crystal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "state",
          "density(g/cm3)",
          "U_EAM(kJ/mol)",
          "pressure(GPa)"
        ]
      },
      "description": "Properties of bcc crystalline uranium at 298 K."
    },
    {
      "file": "shock_hugoniot.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Z",
          "pressure(GPa)",
          "energy(kJ/mol)"
        ]
      },
      "description": "Pressure and energy along the shock Hugoniot at twelve compression ratios."
    },
    {
      "file": "melting_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Z",
          "pressure(GPa)",
          "Tmelt(K)"
        ]
      },
      "description": "Melting temperatures at seven high-pressure states including the ambient-pressure point, determined by the reheating method."
    }
  ],
  "notes": "All outputs are compared to the paper-reported values within tolerances suitable for MD run-to-run variability. The electron excitation contribution U_el is not part of the scored energy outputs; the agent must report only the EAM potential energy plus kinetic energy (U_EAM)."
}
```

## How you are scored
The hidden verifier will read your output CSV files and compare each numerical entry against a hidden gold reference. The total reward is a weighted average of the fraction of property values that fall within an acceptable tolerance band. The tolerances reflect the run‑to‑run variability inherent in classical MD simulations with different implementations and are not disclosed. The stage weights are:

- liquid_properties.csv: 0.40
- shock_hugoniot.csv: 0.30
- melting_temperatures.csv: 0.20
- crystal_properties.csv: 0.10

The reward is a single float between 0 and 1. You must respect the exact CSV format (columns, row order, no extra data) for the checker to parse your files. Submitting pre‑known numbers is not sufficient — the checker tests the results of your actual simulations.
