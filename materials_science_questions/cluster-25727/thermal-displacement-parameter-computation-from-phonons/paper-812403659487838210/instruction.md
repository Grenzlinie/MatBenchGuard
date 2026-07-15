# Discrete-level electronic model for temperature-dependent lattice constant in Au nanoparticles

## Problem background
In ultra-small metallic nanoparticles, the electronic energy levels become discrete due to quantum confinement. This finite-size effect can modify the equilibrium lattice spacing beyond the usual thermal expansion driven by lattice anharmonicity. Valence electrons occupying discrete levels contribute a temperature-dependent potential energy that depends on the lattice constant. For sufficiently small particles this electronic contribution can change sign with temperature, causing a crossover in the thermal expansion behavior. The task is to compute the electronic correction to the lattice parameter and the resulting temperature-dependent corrected cell parameter for 4 nm Au nanoparticles.

## Approach
Model the valence electrons in a 4 nm Au nanoparticle as a discrete, ten-level system with equal energy spacing Δ. At each temperature the levels are populated according to Fermi-Dirac statistics, giving a total electronic potential energy U_v that varies with the lattice spacing R because the level spacing scales as Δ(R) $\propto$ 1/$R^3$. The temperature-dependent derivative dU_v/dR is computed and, through an elastic restoring force parameterized by the bulk modulus of gold, yields a shift δa(T) in the equilibrium lattice constant. Separately, the effect of ordinary lattice thermal expansion is accounted for by using the bulk linear expansion coefficient of Au to back-calculate the zero-temperature cell parameter a0 from the known room-temperature value. The corrected cell parameter at each temperature is a*(T) = a0 + δa(T). The computation is performed numerically over the temperature range of interest.

## Reproduction target
Using the discrete electronic level model with level spacing Δ = 3.5 meV and ten equally spaced levels, compute the temperature-dependent corrected cell parameter a*(T) and its reciprocal 1/a*(T) for a 4 nm Au nanoparticle. Correct for lattice thermal expansion by employing the bulk Au linear expansion coefficient α = 1.4×10⁻⁵ K⁻¹ and the room-temperature cell parameter a = 4.0682 Å. Produce a CSV file `/app/outputs/corrected_cell_parameter.csv` with columns `temperature_K`, `a_star_Angstrom`, and `1_over_a_star_Angstrom-1` for every temperature from 0 K to 390 K in steps of 5 K (79 rows, including both endpoints).

## Assets

- Python scientific computing environment: python3; numpy; scipy; matplotlib

## Workflow steps

### Step 1: Compute electronic correction from discrete level model
- Role: process
- Action: Implement the discrete electronic energy level model for 4 nm Au nanoparticles using ten equally spaced levels with spacing Δ = 3.5 meV. Compute the temperature-dependent derivative dU_v/dR of the valence electron potential energy, and from it derive the shift δa(T) in the equilibrium lattice constant. The proportionality between strain and -dU_v/dR should be estimated using known physical constants (e.g., bulk modulus of Au) to ensure physical consistency. Produce evidence plot electronic_correction_plot.png.
- Evidence: `/app/outputs/electronic_correction_plot.png`

### Step 2: Generate corrected cell parameter CSV
- Role: scored (load-bearing)
- Action: Combine the electronic shift δa(T) with lattice thermal expansion correction. Compute a0, the T=0 K cell parameter, by reversing the room-temperature value a=4.0682 Å using the bulk Au linear expansion coefficient α = 1.4×10⁻⁵ K⁻¹. Then compute the corrected cell parameter a*(T) = a0 + δa(T) and its reciprocal 1/a*(T) for temperatures from 0 K to 390 K in 5 K steps. Output the results to corrected_cell_parameter.csv.
- Output file: `/app/outputs/corrected_cell_parameter.csv`
- Format: csv
- Contract: temperature_K (float), a_star_Angstrom (float), 1_over_a_star_Angstrom-1 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/corrected_cell_parameter.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### corrected_cell_parameter.csv
- path: `/app/outputs/corrected_cell_parameter.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file with three columns: temperature_K (float), a_star_Angstrom (float), 1_over_a_star_Angstrom-1 (float). The hidden checker will recompute the expected theoretical curve using the same model and compare relative errors and structural features (minimum location, trend signs).
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `a_star_Angstrom`, `1_over_a_star_Angstrom-1`
  - `units`:
    - `temperature_K`: K
    - `a_star_Angstrom`: Å
    - `1_over_a_star_Angstrom-1`: Å⁻¹

Notes: The electronic correction step requires determining the proportionality between δa and dU_v/dR. The agent should use a physically motivated estimate (e.g., derived from the bulk modulus of Au) to obtain a reasonable a*(T) curve.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "corrected_cell_parameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "a_star_Angstrom",
          "1_over_a_star_Angstrom-1"
        ],
        "units": {
          "temperature_K": "K",
          "a_star_Angstrom": "Å",
          "1_over_a_star_Angstrom-1": "Å⁻¹"
        }
      },
      "description": "CSV file with three columns: temperature_K (float), a_star_Angstrom (float), 1_over_a_star_Angstrom-1 (float). The hidden checker will recompute the expected theoretical curve using the same model and compare relative errors and structural features (minimum location, trend signs)."
    }
  ],
  "notes": "The electronic correction step requires determining the proportionality between δa and dU_v/dR. The agent should use a physically motivated estimate (e.g., derived from the bulk modulus of Au) to obtain a reasonable a*(T) curve."
}
```

## How you are scored
A hidden verifier independently implements the same discrete-level model and computes the reference a*(T) and 1/a*(T) curve. It compares your submitted CSV against this reference. The scoring checks that the predicted values fall within a generous relative tolerance, that the inverse lattice constant curve exhibits a minimum at a specific temperature, and that the low-temperature and high-temperature trends have the correct sign (expansion versus contraction). The reward is a weighted combination across the evaluated properties, with the main scored artifact carrying the largest weight. Reporting numbers without correctly implementing the physical model will not match the reference and will score low.
