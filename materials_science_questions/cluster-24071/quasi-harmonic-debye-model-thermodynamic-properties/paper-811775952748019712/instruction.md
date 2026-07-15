# EAM potential and thermophysical properties of liquid uranium

## Problem background
Liquid uranium exhibits an anomalously high heat capacity at elevated temperatures, attributed to electronic excitations. Reliable thermophysical data for liquid uranium across a wide range of temperatures and pressures are essential for nuclear and high‑pressure applications, yet experimental measurements remain scarce. Molecular dynamics (MD) simulations with classical interatomic potentials can efficiently sample configurational space and provide these properties. This task reproduces an embedded‑atom model (EAM) potential for uranium and uses MD to compute key thermophysical quantities of liquid uranium, including potential energy, bulk modulus, self‑diffusion, dynamic viscosity, melting temperature, and shock Hugoniot states.

## Approach
The EAM potential is built from three contributions: a Morse pairwise interaction, an exponential density‑kernel function that defines an effective electron density at each ion position, and a piecewise‑polynomial embedding function that depends on that density. The potential parameters are fitted to reproduce the experimental density and isothermal bulk modulus of liquid uranium at melting temperature, and to match shock Hugoniot data at high compressions.

Once the potential is assembled, LAMMPS is used to perform a series of NVT molecular dynamics simulations. For liquid uranium at zero pressure, simulations are run at the experimentally known densities at eight temperatures (1406–4500 K). From the MD trajectories the potential energy, isothermal bulk modulus, self‑diffusion coefficient, and dynamic viscosity (via the Stokes–Einstein relation) are computed.

Shock Hugoniot states are determined by varying the temperature for each compression ratio until the simulated internal energy satisfies the Hugoniot jump relation with respect to a reference state (bcc uranium at 298 K and density 19.05 g/cm³). Finally, the ambient‑pressure melting temperature of the EAM model is estimated by the reheating method: a defective bcc lattice is progressively heated and the solid–liquid transition is detected by monitoring the structure factor.

## Reproduction target
Your goal is to produce the following four artifacts:

1. A JSON file containing the full set of EAM potential parameters (Morse depth, minimum distance, curvature; density‑kernel coefficients; embedding‑function knot densities, polynomial coefficients, and exponents; and the cutoff radius).
2. A CSV file with thermophysical properties of liquid uranium at zero pressure for eight temperatures (1406, 1500, 2000, 2500, 3000, 3500, 4000, 4500 K). For each temperature, report the simulation density, potential energy, isothermal bulk modulus, self‑diffusion coefficient, and dynamic viscosity.
3. A CSV file with shock Hugoniot states for six compression ratios (V/V₀ = 0.90, 0.80, 0.70, 0.65, 0.60, 0.55). For each compression, report the temperature that satisfies the Hugoniot relation, the pressure, and the total internal energy.
4. A plain text file containing the estimated ambient‑pressure melting temperature (in Kelvin) of the EAM uranium model.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- Python scientific stack: pip install numpy scipy pandas

## Workflow steps

### Step 1: EAM potential parameter assembly
- Role: scored
- Action: Implement the analytical forms and numerical values for the EAM potential exactly as described: Morse pair interaction with ε=0.209 eV, d=3.3318 Å, α=4.100; exponential density kernel ψ(r)=p₁ exp(-p₂ r) with p₁=5.5619, p₂=1.3850; embedding function Φ(ρ) built from the piecewise formulas (quadratic, power‑law) with the knot densities ρ₁…ρ₉ and coefficients a₁, c₁…c₁₀, m=1.80, n=1.71; cut‑off radius 12.20 Å. Save the full parameter set to a JSON file.
- Output file: `/app/outputs/step_01_eam_potential_parameters.json`
- Format: json
- Contract: JSON object with keys: p1, p2, rho1..rho9, a1, c1..c10, m, n, eps (Morse depth in eV), d (Morse minimum distance in Å), alpha (Morse curvature), cutoff (cut-off radius in Å).
- Scoring: scored by hidden verifier

### Step 2: MD simulation of liquid uranium at zero pressure
- Role: scored (load-bearing)
- Action: Run NVT MD simulations of liquid uranium (1968 atoms) at the experimental densities: T=1406 K → 17.226 g/cm³, 1500 K → 17.06 g/cm³, 2000 K → 16.18 g/cm³, 2500 K → 15.33 g/cm³, 3000 K → 14.53 g/cm³, 3500 K → 13.76 g/cm³, 4000 K → 13.03 g/cm³, 4500 K → 12.3 g/cm³. Compute and report potential energy U_pot, isothermal bulk modulus K_T, self‑diffusion coefficient D, and viscosity η using the Stokes–Einstein relation with ion radius r_a = 0.792 Å.
- Output file: `/app/outputs/step_02_liquid_properties_zero_p.csv`
- Format: csv
- Contract: CSV with columns: T_K (temperature in Kelvin), density_gcm3 (simulation density in g/cm³), U_pot_kJmol (potential energy in kJ/mol), K_T_GPa (isothermal bulk modulus in GPa), D_cm2s (self‑diffusion coefficient in 10⁻⁵ cm²/s), viscosity_cP (dynamic viscosity in centipoise).
- Scoring: scored by hidden verifier

### Step 3: Shock Hugoniot state determination
- Role: scored (load-bearing)
- Action: For each compression ratio Z = V/V₀ = 0.90, 0.80, 0.70, 0.65, 0.60, 0.55, determine the temperature T such that the NVT MD simulation satisfies the Hugoniot energy relation with respect to an initial reference state: bcc crystal at T₀ = 298 K and V₀ = molar volume corresponding to density 19.05 g/cm³ (V₀ = 12.49 cm³/mol). Use small NVT ensembles (2000 atoms) and adjust T until the Hugoniot equation holds. Report the final P and total internal energy U (potential + kinetic) at the Hugoniot state.
- Output file: `/app/outputs/step_03_shock_hugoniot.csv`
- Format: csv
- Contract: CSV with columns: Z (V/V₀), T_model_K (temperature in Kelvin), P_GPa (pressure in GPa), U_kJmol (total internal energy in kJ/mol).
- Scoring: scored by hidden verifier

### Step 4: Melting temperature estimation
- Role: scored
- Action: Estimate the melting temperature of the EAM uranium model at ambient pressure using the reheating method: start from a defective bcc lattice, heat progressively, and monitor the structure factor to detect the solid–liquid transition.
- Output file: `/app/outputs/step_04_melting_temperature.txt`
- Format: txt
- Contract: Single floating‑point number representing the melting temperature in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_eam_potential_parameters.json`
- `/app/outputs/step_02_liquid_properties_zero_p.csv`
- `/app/outputs/step_03_shock_hugoniot.csv`
- `/app/outputs/step_04_melting_temperature.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_eam_potential_parameters.json
- path: `/app/outputs/step_01_eam_potential_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The complete set of EAM potential parameters, exactly as given in the paper. All numeric values must be present; the hidden checker verifies every key and compares values with a small relative tolerance.
- schema:
  - `type`: object
  - `required`: `p1`, `p2`, `rho1`, `rho2`, `rho3`, `rho4`, `rho5`, `rho6`, `rho7`, `rho8`, `rho9`, `a1`, `c1`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `m`, `n`, `eps`, `d`, `alpha`, `cutoff`

### step_02_liquid_properties_zero_p.csv
- path: `/app/outputs/step_02_liquid_properties_zero_p.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermophysical properties of liquid uranium at zero pressure for eight temperatures (1406–4500 K). Quantities are compared to paper-reported gold values using tolerance‑based checks.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `density_gcm3`, `U_pot_kJmol`, `K_T_GPa`, `D_cm2s`, `viscosity_cP`
  - `units`:
    - `T_K`: K
    - `density_gcm3`: g/cm³
    - `U_pot_kJmol`: kJ/mol
    - `K_T_GPa`: GPa
    - `D_cm2s`: 10⁻⁵ cm²/s
    - `viscosity_cP`: cP

### step_03_shock_hugoniot.csv
- path: `/app/outputs/step_03_shock_hugoniot.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Shock Hugoniot states for six compression ratios (Z=0.90 to 0.55) obtained by solving the Hugoniot equation with MD. Compared to paper-reported Hugoniot temperatures, pressures, and energies with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `Z`, `T_model_K`, `P_GPa`, `U_kJmol`
  - `units`:
    - `Z`: V/V₀ (dimensionless)
    - `T_model_K`: K
    - `P_GPa`: GPa
    - `U_kJmol`: kJ/mol

### step_04_melting_temperature.txt
- path: `/app/outputs/step_04_melting_temperature.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Estimated ambient‑pressure melting temperature of the EAM uranium model. Checked against the paper‑reported value with a tolerance.
- schema:
  - `type`: text
  - `description`: A single floating‑point number (in Kelvin).

Notes: All scored artifacts are compared against paper‑derived reference values with appropriate tolerances. Step 01 is an exact match of the published parameter set; steps 02‑04 use reference match because they result from stochastic MD runs and small toolchain differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_eam_potential_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "p1",
          "p2",
          "rho1",
          "rho2",
          "rho3",
          "rho4",
          "rho5",
          "rho6",
          "rho7",
          "rho8",
          "rho9",
          "a1",
          "c1",
          "c2",
          "c3",
          "c4",
          "c5",
          "c6",
          "c7",
          "c8",
          "c9",
          "c10",
          "m",
          "n",
          "eps",
          "d",
          "alpha",
          "cutoff"
        ]
      },
      "description": "The complete set of EAM potential parameters, exactly as given in the paper. All numeric values must be present; the hidden checker verifies every key and compares values with a small relative tolerance."
    },
    {
      "file": "step_02_liquid_properties_zero_p.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "density_gcm3",
          "U_pot_kJmol",
          "K_T_GPa",
          "D_cm2s",
          "viscosity_cP"
        ],
        "units": {
          "T_K": "K",
          "density_gcm3": "g/cm³",
          "U_pot_kJmol": "kJ/mol",
          "K_T_GPa": "GPa",
          "D_cm2s": "10⁻⁵ cm²/s",
          "viscosity_cP": "cP"
        }
      },
      "description": "Thermophysical properties of liquid uranium at zero pressure for eight temperatures (1406–4500 K). Quantities are compared to paper-reported gold values using tolerance‑based checks."
    },
    {
      "file": "step_03_shock_hugoniot.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Z",
          "T_model_K",
          "P_GPa",
          "U_kJmol"
        ],
        "units": {
          "Z": "V/V₀ (dimensionless)",
          "T_model_K": "K",
          "P_GPa": "GPa",
          "U_kJmol": "kJ/mol"
        }
      },
      "description": "Shock Hugoniot states for six compression ratios (Z=0.90 to 0.55) obtained by solving the Hugoniot equation with MD. Compared to paper-reported Hugoniot temperatures, pressures, and energies with tolerances."
    },
    {
      "file": "step_04_melting_temperature.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating‑point number (in Kelvin)."
      },
      "description": "Estimated ambient‑pressure melting temperature of the EAM uranium model. Checked against the paper‑reported value with a tolerance."
    }
  ],
  "notes": "All scored artifacts are compared against paper‑derived reference values with appropriate tolerances. Step 01 is an exact match of the published parameter set; steps 02‑04 use reference match because they result from stochastic MD runs and small toolchain differences."
}
```

## How you are scored
Your submission will be evaluated by a hidden checker program. For the EAM parameter file, the checker verifies that all required keys are present and that each numeric parameter matches the expected reference values. For the liquid‑property and Hugoniot CSV files, and for the melting‑temperature file, the checker compares your computed numbers against hidden reference values for each property (e.g., potential energy at each temperature, pressure at each compression ratio, melting point). The agreement improves your score. The final reward is a weighted combination across all scored artifacts; producing results that are consistent with the correctly implemented EAM potential and MD protocol yields a higher reward.
