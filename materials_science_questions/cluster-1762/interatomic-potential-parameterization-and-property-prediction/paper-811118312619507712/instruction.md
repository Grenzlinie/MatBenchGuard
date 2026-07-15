# Interatomic Potential Parameterization and Property Prediction

## Problem background
Silver iodide (AgI) is a canonical superionic conductor with a rich phase diagram. At low pressure, it crystallizes in the zinc blende (γ-AgI) structure, which does not exhibit fast-ion diffusion. Under high pressure, AgI transforms to a rocksalt-structured phase, where increased ionic conductivity has been reported at elevated temperatures. Understanding the structural properties of the stoichiometric phases and the cation diffusion behavior in rocksalt AgI is critical for applications in solid-state electrochemistry and high-pressure ionic conductors. This task uses atomistic molecular dynamics (MD) simulations driven by an empirical three-body potential (the Tersoff model) to compute the equilibrium structural parameters of zinc blende AgI and to evaluate the silver-ion diffusion coefficients in rocksalt AgI under conditions of high pressure and high temperature. The central question is whether the potential, with a fixed published parameter set, can simultaneously reproduce the zinc blende phase properties and predict superionic-like diffusion in the rocksalt phase.

## Approach
The Tersoff potential is a bond-order potential that captures the angular dependence of covalent bonding through a local coordination-dependent term, making it suitable for tetrahedrally coordinated solids. For this task, the potential parameters for AgI have been fitted separately and are provided as fixed constants. The approach consists of two main computational experiments:

1. **Zinc blende structural properties**: Implement the Tersoff potential and initialize a periodic simulation cell of γ-AgI. Perform equilibrium MD runs under varying volumes to obtain the energy–volume curve. Fit the Murnaghan equation of state to extract the equilibrium lattice constant, bulk modulus, and its pressure derivative; the minimum of the fitted curve yields the cohesive energy per atom. Elastic constants are computed from small strains applied to the equilibrium cell.
2. **Rocksalt diffusion**: Use the same potential to construct a rocksalt AgI simulation cell. Maintain the system at fixed pressures (20, 30, 40 kbar) and a range of temperatures (900–1600 K) using a thermostat. For each (pressure, temperature) condition, after equilibration, compute the mean squared displacement (MSD) of the silver cations over a long time interval. The diffusion coefficient is extracted from the linear long-time slope of the MSD via the Einstein relation.

The simulation engine can be any open‑source MD code (e.g., LAMMPS) or a custom Python implementation; the essential requirement is that the specified potential and protocol are followed.

## Reproduction target
Produce two JSON artifact files:

- **`zincblende_properties.json`**: Contains the equilibrium lattice constant (Å), bulk modulus (Mbar), bulk modulus derivative, cohesive energy per atom (eV/atom), and the elastic moduli (C₁₁−C₁₂)/2 and C₄₄ (both Mbar) for zinc blende AgI at zero pressure and low temperature.
- **`rocksalt_diffusion.json`**: Contains an array of diffusion coefficient records for rocksalt AgI. Each record lists the applied pressure (kbar), the temperature (K), and the computed diffusion coefficient (cm²/s). The dataset must span at least three pressures (20, 30, 40 kbar) and for each pressure at least five distinct temperatures covering the interval 900–1600 K. The diffusion coefficients must be positive and must increase monotonically with temperature at every fixed pressure.

The goal is to independently compute these quantities by running the described MD simulations; no external experimental data should be downloaded.

## Assets

- Tersoff potential functional form: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.37.6991
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Python packages numpy, scipy: numpy scipy

## Workflow steps

### Step 1: Zinc blende structural properties
- Role: scored (load-bearing)
- Action: Implement the Tersoff potential for AgI with the parameters A=207.500 eV, B=36.160 eV, λ=1.8095 Å⁻¹, μ=0.9428 Å⁻¹, n=0.78734, h=-0.57058, β=1.0999e-6, c=1.0039e5, d=16.218, R=3.43 Å, D=0.20 Å, λ₃=0, α=0. Set up a 216-atom cubic simulation cell with periodic boundaries for the zinc blende structure. Equilibrate and collect energy–volume data; fit the Murnaghan equation of state to obtain lattice constant a₀, bulk modulus B, and bulk modulus derivative B′. Extract cohesive energy per atom from the minimum of the fitted curve. Compute elastic constants using a standard method to obtain (C₁₁−C₁₂)/2 and C₄₄. Write all quantities to /app/outputs/zincblende_properties.json.
- Output file: `/app/outputs/zincblende_properties.json`
- Format: json
- Contract: {
  "lattice_constant_angstrom": float,
  "bulk_modulus_Mbar": float,
  "bulk_modulus_derivative": float,
  "cohesive_energy_eV_per_atom": float,
  "elastic_C11_minus_C12_over_2_Mbar": float,
  "elastic_C44_Mbar": float
}
- Scoring: scored by hidden verifier

### Step 2: Rocksalt phase diffusion coefficients
- Role: scored
- Action: Using the same Tersoff potential, set up a 216-atom rocksalt AgI simulation cell. Run MD simulations under temperature control at pressures 20, 30, 40 kbar and a range of temperatures covering 900–1600 K (at least five distinct temperatures per pressure). For each (p,T) condition, equilibrate and then calculate the mean squared displacement (MSD) of Ag⁺ cations over a sufficiently long trajectory; extract the diffusion coefficient D from the Einstein relation (long-time slope of MSD). Collect all (pressure_kbar, temperature_K, diffusion_coefficient_cm2_per_s) tuples and write them to /app/outputs/rocksalt_diffusion.json.
- Output file: `/app/outputs/rocksalt_diffusion.json`
- Format: json
- Contract: {
  "diffusion_coefficients": [
    {
      "pressure_kbar": float,
      "temperature_K": float,
      "diffusion_coefficient_cm2_per_s": float
    }
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zincblende_properties.json`
- `/app/outputs/rocksalt_diffusion.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zincblende_properties.json
- path: `/app/outputs/zincblende_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the computed structural and elastic properties of zinc blende AgI and the equilibrium structural properties of rocksalt AgI, all computed with the Tersoff potential. Each field is compared to the paper's reported value with an appropriate hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_angstrom`: float (Å)
    - `bulk_modulus_Mbar`: float (Mbar)
    - `bulk_modulus_derivative`: float (dimensionless)
    - `cohesive_energy_eV_per_atom`: float (eV/atom)
    - `elastic_C11_minus_C12_over_2_Mbar`: float (Mbar)
    - `elastic_C44_Mbar`: float (Mbar)
    - `rocksalt_lattice_constant_angstrom`: float (Å)
    - `rocksalt_bulk_modulus_Mbar`: float (Mbar)
    - `rocksalt_bulk_modulus_derivative`: float (dimensionless)

### rocksalt_diffusion.json
- path: `/app/outputs/rocksalt_diffusion.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Scored artifact containing Ag⁺ diffusion coefficients in rocksalt AgI. The checker verifies that all coefficients are positive and of order 10⁻⁵ cm²/s, and that for each pressure D increases monotonically with temperature.
- schema:
  - `type`: object
  - `required`:
    - `diffusion_coefficients`: array of objects
  - `items`:
    - `pressure_kbar`: float
    - `temperature_K`: float
    - `diffusion_coefficient_cm2_per_s`: float

Notes: The potential parameters are provided as public constants; re-fitting is not required. The agent may use any open-source MD code (LAMMPS, custom Python, etc.). No external dataset download is necessary. Rocksalt structural properties are scored alongside zincblende properties in the same artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zincblende_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_angstrom": "float (Å)",
          "bulk_modulus_Mbar": "float (Mbar)",
          "bulk_modulus_derivative": "float (dimensionless)",
          "cohesive_energy_eV_per_atom": "float (eV/atom)",
          "elastic_C11_minus_C12_over_2_Mbar": "float (Mbar)",
          "elastic_C44_Mbar": "float (Mbar)",
          "rocksalt_lattice_constant_angstrom": "float (Å)",
          "rocksalt_bulk_modulus_Mbar": "float (Mbar)",
          "rocksalt_bulk_modulus_derivative": "float (dimensionless)"
        }
      },
      "description": "Scored artifact containing the computed structural and elastic properties of zinc blende AgI and the equilibrium structural properties of rocksalt AgI, all computed with the Tersoff potential. Each field is compared to the paper's reported value with an appropriate hidden tolerance."
    },
    {
      "file": "rocksalt_diffusion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "diffusion_coefficients": "array of objects"
        },
        "items": {
          "pressure_kbar": "float",
          "temperature_K": "float",
          "diffusion_coefficient_cm2_per_s": "float"
        }
      },
      "description": "Scored artifact containing Ag⁺ diffusion coefficients in rocksalt AgI. The checker verifies that all coefficients are positive and of order 10⁻⁵ cm²/s, and that for each pressure D increases monotonically with temperature."
    }
  ],
  "notes": "The potential parameters are provided as public constants; re-fitting is not required. The agent may use any open-source MD code (LAMMPS, custom Python, etc.). No external dataset download is necessary. Rocksalt structural properties are scored alongside zincblende properties in the same artifact."
}
```

## How you are scored
A hidden verifier will read your submitted JSON artifacts and evaluate them against reference criteria derived from the literature. The verifier does **not** simply compare your reported numbers to a single static answer; instead:
- For `zincblende_properties.json`, every field is compared to a hidden reference value with an appropriate tolerance that accounts for legitimate numerical spread from different MD implementations.
- For `rocksalt_diffusion.json`, the checker enforces structural consistency: all coefficients must be positive, physically plausible in magnitude, and, for each pressure, must increase monotonically with temperature. Additionally, individual data points are compared against expected reference values within a generous factor.

The scores from the two stages are weighted and combined into a final reward between 0 and 1. A submission that merely hard‑codes the expected numbers without running the actual MD workflow will fail the structural monotonicity and tolerance checks; the reward is designed to reward a faithful reproduction of the computational protocol.
