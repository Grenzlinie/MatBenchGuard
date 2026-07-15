# First-principles thermodynamic and transport properties of LaNi4Sb12 skutterudite

## Problem background
Thermoelectric materials can convert waste heat into electricity, but their performance is limited by the interplay of electrical and thermal transport. Filled skutterudites, such as LaNi4Sb12, are of interest because filler atoms inside the crystal cages scatter phonons and can reduce lattice thermal conductivity while maintaining good electrical properties. This task examines the skutterudite LaNi4Sb12 by computing its thermodynamic properties (heat capacity, thermal expansion, Grüneisen parameter) as functions of temperature and pressure, and its thermoelectric transport coefficients (Seebeck coefficient, electrical conductivity, thermal conductivity, power factor) across a wide temperature range. The results quantify the material's potential for thermoelectric applications.

## Approach
The workflow uses first-principles calculations without relying on experimental data. Starting from the known crystal structure (body-centered cubic, space group Im3, 17 atoms per unit cell), you will perform density functional theory (DFT) calculations with an open-source code to relax the structure and compute an energy–volume (E–V) curve. The E–V data serve as input to the quasi‑harmonic Debye model, which yields the temperature‑ and pressure‑dependent quantities: constant‑volume heat capacity C_V, thermal expansion coefficient α, and Grüneisen parameter γ. This step requires the number of atoms, the molecular mass, and a Poisson ratio (choose a reasonable value). Separately, a dense‑k‑point DFT calculation provides electronic band energies; these are processed with the Boltzmann transport code BoltzTraP2 under the constant relaxation‑time approximation (τ = 5 × 10⁻¹⁵ s) to obtain the Seebeck coefficient, electrical conductivity (per relaxation time), and electronic contribution to the thermal conductivity. The lattice thermal conductivity is estimated via the Slack equation using the Debye temperature and Grüneisen parameter obtained earlier, allowing the total thermal conductivity and the power factor S²σ to be assembled. All required tools (Quantum ESPRESSO or equivalent, Gibbs2, BoltzTraP2) are publicly available.

## Reproduction target
Produce two scored CSV files in `/app/outputs`:

1. `thermodynamic_properties.csv` — columns: `T(K)`, `P(GPa)`, `CV(J/mol·K)`, `alpha(1/K)`, `gamma`. Rows for all combinations of `T = 50, 100, 200, 300, 370` K and `P = 0, 5, 10` GPa.

2. `transport_properties.csv` — columns: `T(K)`, `Seebeck(µV/K)`, `sigma_tau(Ω⁻¹·m⁻¹·s⁻¹)`, `kappa(W/m·K)`, `PF(µW/(cm·K²·s))`. Rows for `T = 50, 100, 200, 300, 400, 600, 800` K.

The files must contain exactly these columns and rows. No external reference to plots or tables is needed; the hidden verifier will check the format and assess whether the numerical values obey expected physical trends and fall within plausible ranges.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Gibbs2 (quasi-harmonic Debye model code): http://gibbs.ujf.cas.cz/
- BoltzTraP2: https://github.com/sousaw/BoltzTraP2
- LaNi4Sb12 crystal structure (Im3, space group 204)

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for LaNi4Sb12 in the Im3 space group using an open-source DFT code (e.g., Quantum ESPRESSO) to obtain the equilibrium lattice constant and relaxed atomic positions.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 2: DFT E-V curve calculation
- Role: process
- Action: Using the relaxed structure, compute total energies for a series of unit cell volumes to generate energy-volume data E(V).
- Evidence: `/app/outputs/ev_curve.dat`

### Step 3: Thermodynamic properties via quasi-harmonic Debye model
- Role: scored (load-bearing)
- Action: Run the quasi-harmonic Debye model (Gibbs2 or equivalent) using the E(V) data from step 2, the number of atoms per unit cell (17), the molecular mass, and a Poisson ratio to compute constant-volume heat capacity C_V, thermal expansion coefficient α, and Grüneisen parameter γ at T = 50, 100, 200, 300, 370 K and P = 0, 5, 10 GPa. Output the results as a structured CSV.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: Columns: T(K), P(GPa), CV(J/mol·K), alpha(1/K), gamma. Rows for each (T,P) combination: T=50,100,200,300,370 K at P=0,5,10 GPa.
- Scoring: scored by hidden verifier

### Step 4: DFT electronic structure for transport
- Role: process
- Action: Perform self-consistent DFT calculation on the relaxed structure with a dense k-point mesh to obtain electronic band energies E(k) required for transport calculations.
- Evidence: `/app/outputs/band_energies.eig`

### Step 5: Transport properties and total thermal conductivity
- Role: scored (load-bearing)
- Action: Compute Boltzmann transport coefficients using BoltzTraP2 with constant relaxation time τ = 5×10⁻¹⁵ s. Extract Seebeck coefficient S, electrical conductivity σ/τ, and electronic thermal conductivity κ_e/τ. Estimate lattice thermal conductivity κ_L using Slack's equation with the Debye temperature and Grüneisen parameter from step 3. Compute total thermal conductivity κ = κ_e + κ_L and power factor PF = S²·σ. Output the results for T = 50, 100, 200, 300, 400, 600, 800 K as a CSV.
- Output file: `/app/outputs/transport_properties.csv`
- Format: csv
- Contract: Columns: T(K), Seebeck(µV/K), sigma_tau(Ω⁻¹·m⁻¹·s⁻¹), kappa(W/m·K), PF(µW/(cm·K²·s)). Rows for T=50,100,200,300,400,600,800 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_properties.csv`
- `/app/outputs/transport_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed constant-volume heat capacity, thermal expansion coefficient, and Grüneisen parameter at specified temperatures and pressures.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `P(GPa)`, `CV(J/mol·K)`, `alpha(1/K)`, `gamma`
  - `units`:
    - `T(K)`: K
    - `P(GPa)`: GPa
    - `CV(J/mol·K)`: J/(mol·K)
    - `alpha(1/K)`: 1/K
    - `gamma`: dimensionless

### transport_properties.csv
- path: `/app/outputs/transport_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed Seebeck coefficient, electrical conductivity (per relaxation time), total thermal conductivity, and power factor at specified temperatures.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `Seebeck(µV/K)`, `sigma_tau(Ω⁻¹·m⁻¹·s⁻¹)`, `kappa(W/m·K)`, `PF(µW/(cm·K²·s))`
  - `units`:
    - `T(K)`: K
    - `Seebeck(µV/K)`: µV/K
    - `sigma_tau(Ω⁻¹·m⁻¹·s⁻¹)`: Ω⁻¹·m⁻¹·s⁻¹
    - `kappa(W/m·K)`: W/(m·K)
    - `PF(µW/(cm·K²·s))`: µW/(cm·K²·s)

Notes: The checker will recompute target metrics from the submitted CSV rows (e.g., C_V at 370 K, α at 300 K, γ at 300 K, Seebeck at 300 K, κ at 300 K, PF at 300 K, and trends) and compare them to hidden paper-derived reference values using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "P(GPa)",
          "CV(J/mol·K)",
          "alpha(1/K)",
          "gamma"
        ],
        "units": {
          "T(K)": "K",
          "P(GPa)": "GPa",
          "CV(J/mol·K)": "J/(mol·K)",
          "alpha(1/K)": "1/K",
          "gamma": "dimensionless"
        }
      },
      "description": "Computed constant-volume heat capacity, thermal expansion coefficient, and Grüneisen parameter at specified temperatures and pressures."
    },
    {
      "file": "transport_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "Seebeck(µV/K)",
          "sigma_tau(Ω⁻¹·m⁻¹·s⁻¹)",
          "kappa(W/m·K)",
          "PF(µW/(cm·K²·s))"
        ],
        "units": {
          "T(K)": "K",
          "Seebeck(µV/K)": "µV/K",
          "sigma_tau(Ω⁻¹·m⁻¹·s⁻¹)": "Ω⁻¹·m⁻¹·s⁻¹",
          "kappa(W/m·K)": "W/(m·K)",
          "PF(µW/(cm·K²·s))": "µW/(cm·K²·s)"
        }
      },
      "description": "Computed Seebeck coefficient, electrical conductivity (per relaxation time), total thermal conductivity, and power factor at specified temperatures."
    }
  ],
  "notes": "The checker will recompute target metrics from the submitted CSV rows (e.g., C_V at 370 K, α at 300 K, γ at 300 K, Seebeck at 300 K, κ at 300 K, PF at 300 K, and trends) and compare them to hidden paper-derived reference values using appropriate tolerances."
}
```

## How you are scored
A hidden scoring script reads your two CSV files. It first confirms that the required columns and rows are present and correctly formatted. It then evaluates the values against a set of physical consistency criteria (e.g., temperature dependencies, convergence to known limits, and qualitative pressure effects) and compares key quantities to independent reference values with appropriate tolerances. Each check contributes a partial reward, and the final score is a weighted sum (range 0–1). Obtaining physically sensible trends and reasonable magnitudes is sufficient; numerical deviations caused by different computational choices are accommodated by the tolerance bands. Simply writing down expected numbers without performing the actual calculations will not pass the validation checks.
