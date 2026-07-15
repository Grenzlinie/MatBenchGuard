# MD Simulation of Specific Heat in Metallic Liquids and Glasses

## Problem background
The specific heat of supercooled metallic liquids near the glass transition temperature is extremely difficult to measure experimentally because these liquids crystallize rapidly. Molecular dynamics (MD) simulations provide a way to compute the constant-volume specific heat C_Ω(T) from energy fluctuations and to examine its temperature dependence in systems that form metallic glasses versus those that do not. This task re-implements such a computational study for a representative glass-forming binary alloy and a pure non-glass-forming metal, calculating C_Ω and related thermodynamic quantities across the supercooled liquid range.

## Approach
The approach uses classical molecular dynamics with periodic boundary conditions and interatomic potentials that include both two-body interactions and volume-dependent energies. For the Ca0.7Mg0.3 alloy, the potentials and temperature-dependent atomic volumes are taken from the published description by Li et al. (J. Chem. Phys. 88, 2700, 1988). For pure Na, the interatomic potentials are taken from Li et al. (J. Phys. F 16, 309, 1986). The simulation protocol consists of a temperature-quench procedure: first equilibrate the liquid at a temperature well above the melting point, then reduce the temperature in steps down towards the glass transition. At each temperature, at least 18,000 time steps are run; the first 6,000 are discarded to allow equilibration. The constant-volume specific heat C_Ω (in units of k_B per atom) is then computed from the variance of the total energy over the second and third 6,000-step blocks. For the alloy, the atomic volume Ω(T) is taken directly from the literature reference; for pure Na, Ω(T) must be determined self-consistently by minimizing the Helmholtz free energy F with respect to volume (∂F/∂Ω=0) at each temperature. The thermal expansion coefficient α_p is derived from the temperature derivative of Ω.

## Reproduction target
Produce two CSV files:  
- For Ca0.7Mg0.3: at several temperatures between approximately 780 K and 900 K, report the computed values of C_Ω (k_B⁻¹), atomic volume Ω (Å³), and α_p (K⁻¹).  
- For pure Na: at several temperatures between approximately 140 K and 312 K, report the same quantities.  
Each file must contain at least 5 rows covering the respective temperature range and must follow the specified column format. The reported values should be obtained by faithfully following the described MD protocol and potential models.

## Assets

- Ca-Mg interatomic potentials and temperature-dependent atomic volumes from Li et al. J. Chem. Phys. 88, 2700 (1988): https://doi.org/10.1063/1.454847
- Na interatomic potentials from Li et al. J. Phys. F 16, 309 (1986): https://doi.org/10.1088/0305-4608/16/3/009

## Workflow steps

### Step 1: MD Simulation for Ca0.7Mg0.3 Alloy
- Role: scored (load-bearing)
- Action: Simulate Ca0.7Mg0.3 alloy (700 Ca, 300 Mg) in a cubic box with periodic boundary conditions using the interatomic potentials and temperature-dependent atomic volumes from Li et al. (1988). Perform a temperature-quench MD simulation: equilibrate at a temperature well above melting, then cool stepwise to approximately 780 K. At each temperature run at least 18000 time steps; discard the first 6000, compute the constant-volume specific heat C_Omega (in units of kB per atom) from energy fluctuations of the second and third 6000-step blocks. Derive the thermal expansion coefficient alpha_p from the supplied Omega(T) values. Report results at multiple temperatures covering the range from near Tm to near Tg.
- Output file: `/app/outputs/ca_mg_results.csv`
- Format: csv
- Contract: Columns: temperature_K (float), C_Omega_kB (float, units of kB per atom), atomic_volume_A3 (float, cubic Angstroms), alpha_p_K-1 (float, inverse Kelvin)
- Scoring: scored by hidden verifier

### Step 2: MD Simulation for Pure Na Metal
- Role: scored (load-bearing)
- Action: Simulate pure Na (1000 atoms) in a cubic box with periodic boundary conditions using the interatomic potentials from Li et al. (1986). Perform a temperature-quench MD simulation: equilibrate above melting, cool stepwise to approximately 140 K. Self-consistently determine the atomic volume Omega(T) at each temperature via the Helmholtz free-energy condition ∂F/∂Ω=0 as described in the paper. At each temperature, run at least 18000 time steps; discard the first 6000, compute C_Omega (kB per atom) from energy fluctuations of the second and third 6000-step blocks, and derive alpha_p from the computed Omega(T). Report results at multiple temperatures.
- Output file: `/app/outputs/na_results.csv`
- Format: csv
- Contract: Columns: temperature_K (float), C_Omega_kB (float, units of kB per atom), atomic_volume_A3 (float, cubic Angstroms), alpha_p_K-1 (float, inverse Kelvin)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ca_mg_results.csv`
- `/app/outputs/na_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ca_mg_results.csv
- path: `/app/outputs/ca_mg_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic quantities for the Ca0.7Mg0.3 alloy: temperature in K, constant-volume specific heat C_Omega in kB per atom, atomic volume in Å^3, and thermal expansion coefficient α_p in K^{-1}. The checker will compare reported values to digitized reference data.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `C_Omega_kB`, `atomic_volume_A3`, `alpha_p_K-1`
  - `units`:
    - `temperature_K`: K
    - `C_Omega_kB`: kB per atom
    - `atomic_volume_A3`: A^3
    - `alpha_p_K-1`: K^{-1}

### na_results.csv
- path: `/app/outputs/na_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic quantities for pure Na metal: temperature in K, constant-volume specific heat C_Omega in kB per atom, atomic volume in Å^3, and thermal expansion coefficient α_p in K^{-1}. The checker will compare reported values to digitized reference data.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `C_Omega_kB`, `atomic_volume_A3`, `alpha_p_K-1`
  - `units`:
    - `temperature_K`: K
    - `C_Omega_kB`: kB per atom
    - `atomic_volume_A3`: A^3
    - `alpha_p_K-1`: K^{-1}

Notes: The scoring is a weighted combination of numeric closeness to reference digitized data and structural trend satisfaction. The hidden checker uses the paper's original figures as gold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ca_mg_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "C_Omega_kB",
          "atomic_volume_A3",
          "alpha_p_K-1"
        ],
        "units": {
          "temperature_K": "K",
          "C_Omega_kB": "kB per atom",
          "atomic_volume_A3": "A^3",
          "alpha_p_K-1": "K^{-1}"
        }
      },
      "description": "Thermodynamic quantities for the Ca0.7Mg0.3 alloy: temperature in K, constant-volume specific heat C_Omega in kB per atom, atomic volume in Å^3, and thermal expansion coefficient α_p in K^{-1}. The checker will compare reported values to digitized reference data."
    },
    {
      "file": "na_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "C_Omega_kB",
          "atomic_volume_A3",
          "alpha_p_K-1"
        ],
        "units": {
          "temperature_K": "K",
          "C_Omega_kB": "kB per atom",
          "atomic_volume_A3": "A^3",
          "alpha_p_K-1": "K^{-1}"
        }
      },
      "description": "Thermodynamic quantities for pure Na metal: temperature in K, constant-volume specific heat C_Omega in kB per atom, atomic volume in Å^3, and thermal expansion coefficient α_p in K^{-1}. The checker will compare reported values to digitized reference data."
    }
  ],
  "notes": "The scoring is a weighted combination of numeric closeness to reference digitized data and structural trend satisfaction. The hidden checker uses the paper's original figures as gold."
}
```

## How you are scored
Your output CSV files will be evaluated by a hidden verifier. The verifier compares your reported C_Ω, Ω, and α_p values against a set of reference values obtained from the original computational study. It also performs consistency checks on the temperature sequences. The final reward is a weighted sum of the scores for the two stages. Accurate reproduction of the MD protocol's results is required.
