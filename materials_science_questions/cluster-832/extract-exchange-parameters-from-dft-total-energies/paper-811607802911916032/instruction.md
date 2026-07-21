# Compute biquadratic coupling from a fluctuation-enhanced loose spin model

## Problem background
Interlayer exchange coupling in magnetic multilayers can be mediated by dilute magnetic impurities, leading to biquadratic (BQ) coupling. In CuMn/Co multilayers, the random spatial distribution of Mn impurity atoms is known to influence the coupling, but previous loose spin coupling models required unphysically large exchange fields. A theory that properly accounts for the three‑dimensional random Mn positions introduces an additional lateral‑fluctuation contribution to the biquadratic coupling, which together with the standard RKKY and loose spin terms can reproduce the observed temperature‑dependent canting of the Co layer magnetizations. This task asks you to implement that full model and compute the resulting interlayer coupling angles and exchange energies.

## Approach
Implement the loose spin coupling model including the lateral fluctuation contribution according to the equations below. The core idea is to compute RKKY exchange fields acting on Mn impurities placed in the Cu spacer, sum over impurity positions on the (111) planes to obtain bilinear (J1_LSC) and biquadratic (J2_LSC) loose spin couplings, and then perform a 2D convolution of the laterally varying J1_LSC with a random 6 % Mn occupancy to capture the fluctuation‑driven biquadratic term (J2_fluct). Combine these with a direct RKKY bilinear term between the Co layers to obtain total J1 and J2. From these, minimize the magnetic free energy (which includes the external Zeeman energy) to find the equilibrium interlayer coupling angle φ as a function of temperature at a fixed applied field of 7 mT. Fit the four RKKY exchange parameters (B_eff, T0, T0i, J_Co/J_Mn) by minimizing the mismatch between the computed φ(T) and a set of provided experimental coupling angles (see Step 2). Once the best‑fit parameters are found, compute the coupling angle and the total exchange energies J1 and J2 across a dense temperature grid.

### Physical constants and parameters
Use the following numerical values (SI units):
- Co layer thickness: d_Co = 21 Å = 2.1e-9 m
- CuMn spacer thickness: t = 19 Å = 1.9e-9 m
- Cu(111) interplanar spacing: d_Cu = 2.087 Å = 2.087e-10 m
- Extremal spanning vector for RKKY oscillation: q_z = 2π / d_Cu (q_z ≈ 3.010e10 m^{-1})
- RKKY phase: Φ = 0.2 rad (estimated from Co/Cu(111) literature)
- Co volume magnetization: M = 1.44e6 A/m (corresponding to 1.46 µ_B/atom)
- Mn magnetic moment: m_Mn = 4.4 µ_B = 4.4 * 9.274e-24 J/T ≈ 4.08e-23 J/T
- Exchange stiffness of Co: A = 1.2e-8 J/m
- Boltzmann constant: k_B = 1.380649e-23 J/K
- Bohr magneton: µ_B = 9.274009994e-24 J/T
- Applied external field: H = 7 mT = 0.007 T

### RKKY exchange fields on Mn impurities
For a paramagnetic Mn spin located at distance z from the left Co layer (0 ≤ z ≤ t), the exchange fields from the left (A) and right (B) Co layers are:

U_A(z) = B_eff * (d_Cu^2 / z^2) * sin(q_z z + Φ) * f_T(z)
U_B(z) = B_eff * (d_Cu^2 / (t-z)^2) * sin(q_z (t-z) + Φ) * f_T(t-z)

where the temperature‑damping factor is:

f_T(ζ) = (ζ T/T_0 + T/T_0^i) / sinh(ζ T/T_0 + T/T_0^i)

Here B_eff, T_0, T_0^i are fitting parameters; the scaling factor J_Co/J_Mn is introduced later to account for different hybridization: the effective field felt by the Mn spin is U_eff(z) = (J_Co/J_Mn) * |U_A(z) + U_B(z)|, where the vector sum must respect the relative angle φ between the Co layer magnetizations. Because U_A is parallel to the left Co magnetization and U_B parallel to the right Co magnetization, the magnitude of the total exchange field is

U(z, φ) = sqrt( U_A(z)^2 + U_B(z)^2 + 2 U_A(z) U_B(z) cos φ )

### Free energy of a single loose spin
Treat the Mn impurity as a classical magnetic moment. Its free energy in the exchange field U is

F(U) = -k_B T * ln[ sinh( m_Mn * U / (k_B T) ) / ( m_Mn * U / (k_B T) ) ]

### Loose spin coupling contributions
The bilinear and biquadratic contributions from the Mn impurities are obtained by summing over all Mn positions on the (111) planes of the Cu spacer. (Assume one Mn site per (111) lattice plane with 6% occupancy; the exact site density cancels in the final expressions because J1 and J2 are normalised per unit area). The planes are located at z_i = n * d_Cu for n = 0, 1, …, floor(t / d_Cu). For each plane, compute F for three Co-magnetization configurations: parallel (φ=0), antiparallel (φ=π), and orthogonal (φ=π/2). Then

J1_LSC =  1/2 Σ_i [ F( U(z_i, π) ) - F( U(z_i, 0) ) ]
J2_LSC = Σ_i [ 1/2 ( F( U(z_i, π) ) + F( U(z_i, 0) ) ) - F( U(z_i, π/2) ) ]

(These integral/summation expressions give the coupling energies per unit area; the factor of plane density is absorbed in the fitting parameters, so no additional normalisation is needed beyond the sum.)

### Fluctuation biquadratic term (J2_fluct)
The random lateral positions of Mn impurities cause local variations in J1_LSC. To obtain the fluctuation term:

1. For a given set of parameters, compute the 2D lateral map J1_LSC(x,y) on a fine grid in the plane of the layers (size of a few hundred nm) by summing the contributions from each (111) plane, with a random 6% occupancy of Mn sites at those planes. Each Mn position is treated as a δ‑function source of the J1_LSC interaction (the spatial dependence arises from the RKKY distance s(x,y) in the plane).
2. Decompose this J1_LSC(x,y) into dominant Fourier components. A practical approximation is to model the fluctuation field as J_F(x,y) = a sin(π x / l) sin(π y / l), where the amplitude a and length scale l are chosen to reproduce the typical amplitude and wavelength of the fluctuations observed in the computed map.
3. The resulting additional biquadratic coupling is

J2_fluct = (1 / (4 * sqrt(2) * π * A)) * Σ_i a_i l_i coth( sqrt(2) * π * d_Co / l_i ),

summing over all dominant Fourier components i.

### Direct RKKY bilinear coupling between Co layers
The direct RKKY coupling between the Co layers (without Mn impurities) is expressed as

J1_RKKY(T) = J_RKKY0 * sin( q_z t + Φ ) * ( T / T0 ) / sinh( T / T0 )

where J_RKKY0 is taken from the literature for Co/Cu(111) multilayers. Use the value J_RKKY0 = -2.0e-5 J/m².

### Total coupling energies
J1_total(T) = J1_RKKY(T) + J1_LSC(T)
J2_total(T) = J2_LSC(T) + J2_fluct(T)

### Equilibrium coupling angle
The magnetic energy of the two Co layers, assuming negligible in‑plane anisotropy, is

E(φ,T) = - M d_Co H cos(φ/2) - J1_total(T) cos φ + J2_total(T) cos² φ

For each temperature T, find the equilibrium angle φ(T) that minimises E(φ,T) for φ ∈ [0°, 180°]. This is the computed interlayer coupling angle.

### Fitting procedure
Fit the four parameters B_eff, T0, T0i, and J_Co/J_Mn to minimise the sum of squared differences between the computed φ(T) at the target temperatures listed in Step 2 and the corresponding experimental angles. Use a global optimizer (e.g., differential evolution, then refinement with L‑BFGS‑B) to cope with potential multiple minima.

Once the best‑fit parameters are found, compute φ(T) over a dense temperature grid from 10 K to 150 K (step ≤ 1 K) and calculate J1_total and J2_total on the same grid.

## Reproduction target
Use the described model and fitting procedure to produce three outputs:
1. The best‑fit RKKY exchange parameters as a JSON file.
2. A temperature‑dependent curve of the interlayer coupling angle φ (degrees) at H = 7 mT over a temperature range of at least 10–150 K (dense grid), saved as CSV.
3. A temperature‑dependent curve of the total bilinear J1 and biquadratic J2 exchange energies (J / m²) for the same temperature grid, saved as CSV.

These outputs constitute a complete computational reproduction of the model’s predictions for the CuMn/Co system.

## Assets

- python3
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement forward LSC model
- Role: process
- Action: Implement the loose spin coupling model: compute RKKY exchange fields from the paper's formula, sum over Mn positions on (111) planes of the Cu spacer to obtain J1_LSC and J2_LSC via Slonczewski's free-energy formulas, perform a 2D convolution of J1_LSC with random 6% Mn occupancy to compute J2_fluct, and implement energy minimization to find equilibrium coupling angle φ for given parameters and temperature at a fixed field of 7 mT.
- Evidence: `/app/outputs/model_module.py`

### Step 2: Fit model parameters to target data
- Role: process
- Action: Using the implemented forward model, fit the four RKKY exchange parameters (B_eff, T0, T0i, J_Co/J_Mn) to minimize the squared error between computed φ(T) and the following experimental coupling angles at H=7 mT: (Temperature=30 K, Coupling angle=60°), (50 K, 45°), (70 K, 30°), (90 K, 18°), (110 K, 8°), (130 K, 2°). Use an optimizer of your choice.
- Evidence: `/app/outputs/fitting_log.txt`

### Step 3: Output fitted parameters
- Role: scored
- Action: Write the best-fit RKKY exchange parameters to a JSON file.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: Keys: B_eff (float, T), T0 (float, K), T0i (float, K), J_Co_J_Mn (float, unitless).
- Scoring: scored by hidden verifier

### Step 4: Compute coupling angle vs temperature
- Role: scored (load-bearing)
- Action: Using the best-fit parameters, compute the interlayer coupling angle φ at H=7 mT for a dense temperature grid and write to a CSV file.
- Output file: `/app/outputs/coupling_angle_vs_temperature.csv`
- Format: csv
- Contract: Columns: Temperature (float, K), Coupling_angle (float, degrees).
- Scoring: scored by hidden verifier

### Step 5: Compute exchange energies vs temperature
- Role: scored
- Action: Using the best-fit parameters, compute the total bilinear J1 and biquadratic J2 exchange energies for the same temperature grid and write to a CSV file.
- Output file: `/app/outputs/exchange_energies_vs_temperature.csv`
- Format: csv
- Contract: Columns: Temperature (float, K), J1 (float, J/m^2), J2 (float, J/m^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/coupling_angle_vs_temperature.csv`
- `/app/outputs/exchange_energies_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Best-fit RKKY exchange parameters.
- schema:
  - `type`: object
  - `required`:
    - `B_eff`: float (T)
    - `T0`: float (K)
    - `T0i`: float (K)
    - `J_Co_J_Mn`: float (unitless)

### coupling_angle_vs_temperature.csv
- path: `/app/outputs/coupling_angle_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed interlayer coupling angle φ at H=7 mT as function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Coupling_angle`
  - `units`:
    - `Temperature`: K
    - `Coupling_angle`: degrees

### exchange_energies_vs_temperature.csv
- path: `/app/outputs/exchange_energies_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed total bilinear J1 and biquadratic J2 exchange energies as function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `J1`, `J2`
  - `units`:
    - `Temperature`: K
    - `J1`: J/m^2
    - `J2`: J/m^2

Notes: The checker performs structural audits: monotonicity, sign, and plausible magnitude ranges for the coupling angle and exchange energies; reference match for the fitted parameters. Hidden gold values are the paper‑reported best‑fit parameters; no digitised experimental points are embedded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B_eff": "float (T)",
          "T0": "float (K)",
          "T0i": "float (K)",
          "J_Co_J_Mn": "float (unitless)"
        }
      },
      "description": "Best-fit RKKY exchange parameters."
    },
    {
      "file": "coupling_angle_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Coupling_angle"
        ],
        "units": {
          "Temperature": "K",
          "Coupling_angle": "degrees"
        }
      },
      "description": "Computed interlayer coupling angle φ at H=7 mT as function of temperature."
    },
    {
      "file": "exchange_energies_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "J1",
          "J2"
        ],
        "units": {
          "Temperature": "K",
          "J1": "J/m^2",
          "J2": "J/m^2"
        }
      },
      "description": "Computed total bilinear J1 and biquadratic J2 exchange energies as function of temperature."
    }
  ],
  "notes": "The checker performs structural audits: monotonicity, sign, and plausible magnitude ranges for the coupling angle and exchange energies; reference match for the fitted parameters. Hidden gold values are the paper‑reported best‑fit parameters; no digitised experimental points are embedded."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three scored artifacts (fitted parameters, coupling‑angle CSV, exchange‑energy CSV) and combine the results into a single reward in the range [0, 1]. The verifier compares your computed coupling angles and exchange energies at a set of validation temperatures against reference values derived from the original experimental study, and checks that your fitted parameters are consistent with the expected solution. It also examines whether the temperature‑dependent trends of the coupling angle and exchange energies follow the physically required behaviour (e.g., a monotonic increase of φ with decreasing temperature). Merely reporting numbers without correctly implementing the model and fitting pipeline will not yield a passing score; the verifier expects the artifacts to follow from the computational steps you executed.
