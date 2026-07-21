# Adiabatic resonant tunneling: stochastic simulation of electron exchange in STM

## Problem background
When an electroactive species is adsorbed on a metal electrode and an STM tip is positioned above it, electrons can tunnel from the electrode to the tip via the adsorbate orbital. The electron transfer is coupled to solvent reorganization, so the occupation of the adsorbate level and the tunneling rate depend strongly on the nuclear configuration. The goal is to compute the adiabatic occupation of the adsorbate level, the coordinate-dependent electron transfer rate, and the resulting average tunneling current under various bias voltages and overpotentials.

## Approach
The system is described by an Anderson-type Hamiltonian where the adsorbate interacts with continua representing the electrode and the tip. In the adiabatic limit, for a given solvent coordinate q (0 ≤ q ≤ 1, q=0 oxidized state, q=1 reduced state), the adsorbate reaches a steady-state occupation ⟨n_a(q)⟩ that is given by integrating the broadened density of states below the Fermi levels of the two metals. Simultaneously, electrons flow from the electrode to the tip at a rate k(q) that depends on the overlap of the two Fermi windows. These formulas define the adiabatic potential-energy surface E(q) on which the nuclear motion occurs.

The solvent coordinate is propagated using a collision-model stochastic dynamics: the system moves on E(q) while colliding with heat bath particles at each time step, corresponding to low friction. During the simulation, the instantaneous rate k(q) is accumulated, and the time-averaged electron current is recorded after many barrier crossings. Simulations are run for several reorganization energies, bias voltages, and overpotentials as specified in the workflow steps.

## Model details (must be implemented)

**Notation**
- `Δ1`, `Δ2` : broadenings due to coupling to electrode and tip, respectively; `Δ = Δ1 + Δ2`.
- `λ` : reorganization energy (eV).
- `V_b` : tunneling bias (V), defined as `V_b = E_F^el - E_F^tip`.
- `η` : overpotential with respect to the electrode (V).
- `ε_a` : energy of the adsorbate orbital (eV). We set the Fermi level of the electrode as zero, `E_F^el = 0`, and the Fermi level of the tip as `E_F^tip = -V_b`. The adsorbate level is related to the overpotential by
  ```
  ε_a = λ - η          (Eq. 5 of the paper, with e₀=1 in eV units and E_F^el=0)
  ```
- `\tilde{ε}(q) = ε_a - 2λ q` : solvent-shifted electronic energy of the adsorbate level.

**Adiabatic occupation** (Eq. (3))
```
⟨n_a(q)⟩ = (Δ1/Δ) * (1/π) * [π/2 + arctan((E_F^el - \tilde{ε})/Δ)]
         + (Δ2/Δ) * (1/π) * [π/2 + arctan((E_F^tip - \tilde{ε})/Δ)]
```
With our choice `E_F^el = 0` and `E_F^tip = -V_b` this becomes
```
⟨n_a(q)⟩ = (Δ1/Δ) * (1/π) * [π/2 + arctan(-\tilde{ε}/Δ)]
         + (Δ2/Δ) * (1/π) * [π/2 + arctan((-V_b - \tilde{ε})/Δ)]
```

**Adiabatic electron transfer rate** (Eq. (4))
```
k(q) = (Δ1 Δ2 / (π ℏ Δ)) [arctan((E_F^el - \tilde{ε})/Δ) - arctan((E_F^tip - \tilde{ε})/Δ)]
```
In all calculations we set ℏ = 1 (arbitrary units). For the output file `adiabatic_quantities.csv` **an overall factor of 0.05 is applied** so that the numerical values match the expected scale:
```
k(q) = 0.05 * (Δ1 Δ2 / (π Δ)) [arctan(-\tilde{ε}/Δ) - arctan((-V_b - \tilde{ε})/Δ)]
```
This scaling is used only in Step 1; for Step 2 the absolute magnitude is unimportant because results are normalised.

**Potential-energy surface**
```
E(q) = λ q² + n_a(q) (ε_a - 2λ q)
```
where `n_a(q)` is the adiabatic occupation computed above. The first term is the solvent harmonic free energy; the second is the contribution from the electronic energy.

**Temperature and thermal averaging**
The bath temperature is `kT = 0.05 eV`. Under Boltzmann statistics the equilibrium average of any function `A(q)` is
```
⟨A⟩ = ∫₀¹ A(q) exp(-E(q)/kT) dq / ∫₀¹ exp(-E(q)/kT) dq
```
The average current is obtained from `⟨k(q)⟩` using this formula (or, equivalently, from a long stochastic MD trajectory).

**Collision-model stochastic dynamics (optional)**
The paper implements the stochastic dynamics of Kast et al. The following parameters are used when performing MD simulations:
- System mass m₁ = 1 (in internal units).
- Bath particle mass m₂ = 0.01 → mass ratio m = m₂/m₁ = 0.01.
- Time step δt = 0.01 (internal units, harmonic period T = 2π, i.e. ω = 1).
- Friction coefficient: γ = 2m / ((1+m) δt) ≈ 1.98.
The algorithm is the generalized Verlet collision method described in the original Kast paper; at each step the system collides with a bath particle whose velocity is drawn from the Maxwell-Boltzmann distribution at temperature kT.
Because the low-friction limit ensures Boltzmann statistics, the time-averaged current from a sufficiently long MD run converges to the thermal average. **You may either run the stochastic MD or compute the thermal average analytically via the Boltzmann integral; both approaches are accepted.**

## Reproduction target
Produce two scored artifacts:
1) `adiabatic_quantities.csv` : the solvent-coordinate-dependent occupation ⟨n_a(q)⟩ and electron transfer rate k(q) for the parameter set Δ1=Δ2=0.01 eV, λ=0.6 eV, V_b=0.2 V, η=0, evaluated on a q grid from 0 to 1 step 0.01.
2) `current_results.csv` : time-averaged normalised current for the following sets of conditions (corresponding to Figs. 4, 6 and 7 of the paper):

   **Fig 4 – current vs bias**
   - Δ1 = Δ2 = 0.01 eV, η = 0.01 V
   - λ = 0.2, 0.4, 0.6 eV (each in its own scenario)
   - Bias values: 0.0, 0.05, 0.10, …, 0.50 V (step 0.05 V)
   - Scenario name: `fig4_lambda_<λ>` (e.g. `fig4_lambda_0.2`)

   **Fig 6 – current vs overpotential (Δ1=Δ2=0.01 eV)**
   - Δ1 = Δ2 = 0.01 eV, V_b = 0.1 V
   - λ = 0.2, 0.4, 0.6 eV
   - Overpotential values: -0.30, -0.25, …, +0.30 V (step 0.05 V)
   - Scenario name: `fig6_lambda_<λ>`

   **Fig 7 – current vs overpotential (asymmetric couplings)**
   - Δ1 = 0.01 eV, Δ2 = 0.001 eV, V_b = 0.05 V
   - λ = 0.2, 0.4, 0.6 eV
   - Overpotential values: -0.30, -0.25, …, +0.30 V (step 0.05 V)
   - Scenario name: `fig7_lambda_<λ>`

   For each scenario the current curve is **normalised to a maximum of 1** (divide all currents of that scenario by the maximum current within the scenario).

   The rows in `current_results.csv` must contain exactly one row per (scenario, bias/η value). Columns:

   - `scenario` : as above.
   - `independent_variable` : string such as `V_b=0.05` or `eta=-0.30` (use the exact format with two decimal places).
   - `independent_value` : numeric value of the bias or overpotential in V.
   - `current` : normalised average current (float, ≤ 1).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute adiabatic occupation and tunneling rate
- Role: scored
- Action: Using the formulas given in "Model details", compute ⟨n_a(q)⟩ and k(q) for the parameter set Δ1 = Δ2 = 0.01 eV, λ = 0.6 eV, V_b = 0.2 V, η = 0. Evaluate at q from 0 to 1 in steps of 0.01. Remember to multiply the rate by the factor 0.05. Save the results to `adiabatic_quantities.csv`.
- Output file: `/app/outputs/adiabatic_quantities.csv`
- Format: csv
- Contract: Columns: q (float, dimensionless solvent coordinate from 0 to 1), occupation (float, dimensionless), rate (float, arbitrary units as defined above).
- Scoring: scored by hidden verifier (pointwise comparison with analytic recomputation, tolerance 5% rel.)

### Step 2: Compute average current (time-averaged or Boltzmann-averaged)
- Role: scored (load-bearing)
- Action: For every scenario listed in "Reproduction target", compute the average current either by **analytical Boltzmann integration** (using the integral formula in "Model details" with `kT = 0.05 eV`) or by **stochastic molecular dynamics** with the collision-model parameters described above (δt=0.01, m=0.01, harmonic period T=2π). If you choose MD, run long enough to average over several thousand barrier crossings. Normalise each scenario’s current values so that the maximum within the scenario is 1. Save all results to `current_results.csv` following the exact naming and format conventions.
- Output file: `/app/outputs/current_results.csv`
- Format: csv
- Contract: Columns: scenario (string), independent_variable (string), independent_value (float, V), current (float, ≤1 normalised).
- Scoring: scored by hidden verifier (comparison to expected Boltzmann average with an absolute tolerance of 0.2, plus checks that current increases with bias and peaks near η=0).

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adiabatic_quantities.csv`
- `/app/outputs/current_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adiabatic_quantities.csv
- path: `/app/outputs/adiabatic_quantities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adiabatic occupation probability ⟨n_a(q)⟩ and electron transfer rate k(q) for the parameter set Δ1=Δ2=0.01 eV, λ=0.6 eV, V_b=0.2 V, η=0, computed on a dense q grid.
- schema:
  - `type`: table
  - `required_columns`: `q`, `occupation`, `rate`
  - `units`:
    - `q`: dimensionless (0 to 1)
    - `occupation`: dimensionless
    - `rate`: arbitrary units (rate formula multiplied by 0.05)

### current_results.csv
- path: `/app/outputs/current_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time-averaged (or Boltzmann-averaged) electron tunneling current, normalised, for current vs. bias and current vs. overpotential curves across multiple system parameters.
- schema:
  - `type`: table
  - `required_columns`: `scenario`, `independent_variable`, `independent_value`, `current`
  - `units`:
    - `independent_value`: V
    - `current`: dimensionless (normalised to 1)

Notes: The hidden checker recomputes reference values from the public formulas and parameters; it does not rely on digitised gold curves. For `adiabatic_quantities.csv` it compares the reported occupation and rate curves pointwise with a relative tolerance and verifies the occupation is monotonic. For `current_results.csv` it compares reported currents against expected Boltzmann averages with an absolute tolerance and checks qualitative trends (current increases with bias, current peaks near η=0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adiabatic_quantities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q",
          "occupation",
          "rate"
        ],
        "units": {
          "q": "dimensionless (0 to 1)",
          "occupation": "dimensionless",
          "rate": "arbitrary units (rate formula multiplied by 0.05)"
        }
      },
      "description": "Adiabatic occupation probability ⟨n_a(q)⟩ and electron transfer rate k(q) for the parameter set Δ1=Δ2=0.01 eV, λ=0.6 eV, V_b=0.2 V, η=0, computed on a dense q grid."
    },
    {
      "file": "current_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "scenario",
          "independent_variable",
          "independent_value",
          "current"
        ],
        "units": {
          "independent_value": "V",
          "current": "dimensionless (normalised to 1)"
        }
      },
      "description": "Time-averaged (or Boltzmann-averaged) electron tunneling current, normalised, for current vs. bias and current vs. overpotential curves across multiple system parameters."
    }
  ],
  "notes": "The hidden checker recomputes reference values from the public formulas and parameters; it does not rely on digitised gold curves. For adiabatic_quantities.csv it compares the reported occupation and rate curves pointwise with a relative tolerance and verifies the occupation is monotonic. For current_results.csv it compares reported currents against expected Boltzmann averages with an absolute tolerance and checks qualitative trends (current increases with bias, current peaks near η=0)."
}
```

## How you are scored
A hidden verifier independently checks each output file. For `adiabatic_quantities.csv`, it recomputes the reference occupation and rate values from the given formulas and compares your results pointwise within a 5% relative tolerance; it also checks that the occupation is monotonic. For `current_results.csv`, it recomputes the expected Boltzmann-averaged current for each scenario using the public parameters and compares your reported (normalised) values with an absolute tolerance of 0.2; it additionally verifies qualitative trends (current monotonically increases with bias, and the current vs. overpotential curve peaks near η=0). Both scores are combined by weight. Reporting a number without executing the required calculation will not receive credit.