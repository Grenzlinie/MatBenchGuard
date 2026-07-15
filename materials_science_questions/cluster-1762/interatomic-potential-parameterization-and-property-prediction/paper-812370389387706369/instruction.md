# Compute Thermodynamic Properties of Liquid d- and f-Shell Metals via Variational Hard-Sphere Pseudopotential Approach

## Problem background
The thermodynamic properties of liquid d- and f-shell metals (enthalpy, entropy, Helmholtz free energy) can be predicted from first principles using pseudopotential perturbation theory with a hard-sphere reference fluid. The variational approach minimizes the free energy with respect to the hard-sphere diameter, with the ion-ion interaction treated via a Percus–Yevick structure factor. The Baria–Jani model pseudopotential and the Taylor local-field correction for exchange and correlation provide a parameter-free scheme once the effective core radius is fixed by the condition of zero total pressure. This task implements that scheme to compute the enthalpy, entropy, and free energy for 12 liquid metals at their melting temperatures, enabling comparison with experimental measurements.

## Approach
For each metal you are given the atomic volume Ω, valency Z, melting temperature T, and hard-sphere diameter σ. You will implement the following:

1. **Internal energy**: compute the ionic contribution (kinetic energy plus Madelung term), the homogeneous electron gas energy (kinetic, exchange, correlation, and low‑temperature specific heat), and the electron‑ion interaction energy via second‑order pseudopotential perturbation theory. The electron‑ion term uses the Baria–Jani bare‑ion pseudopotential and the Hartree dielectric function modified by the Taylor local‑field correction.

2. **Entropy**: compute the ideal‑gas entropy, the hard‑sphere packing entropy (from the Percus–Yevick expression), and the electronic entropy.

3. **Pseudopotential core radius**: the model potential contains an effective core radius r_c that is not supplied. It must be determined by imposing zero total pressure P = −∂F/∂Ω at the given melting temperature and volume. This involves iteratively adjusting r_c until the pressure calculated from the full Helmholtz free energy (F = E − T S) vanishes.

4. **Free energy**: evaluate the total Helmholtz free energy as F = H − T S, where H is the sum of the internal energy components.

All wave‑vector integrals are carried out to 40 k_F. The procedure yields H, S/k_B, and F for each metal, as well as their component breakdowns.

## Reproduction target
Compute the total enthalpy H (in 10⁻³ a.u.), total entropy S/k_B (dimensionless), and Helmholtz free energy F (in 10⁻³ a.u.) for the 12 liquid metals Cu, Ag, Au, Ni, Pd, Pt, Rh, Ir, La, Yb, Ce, and Th at their experimental melting temperatures. The required input parameters (Ω, Z, T, σ) are provided in the task. Report all contributions and totals in the CSV file `/app/outputs/thermodynamic_results.csv` following the output contract below. The values will be compared to hidden reference values to assess correctness.

## Assets

- Metal input parameters
- Baria–Jani model pseudopotential: 10.1016/S0921-4526(02)01847-7
- Taylor local-field correction: 10.1088/0305-4608/8/8/011
- Percus–Yevick hard-sphere structure factor
- Scientific Python packages: numpy scipy

## Workflow steps

### Step 1: Read input parameters
- Role: process
- Action: Read the provided table of atomic volumes (Ω), valencies (Z), melting temperatures (T), and hard-sphere diameters (σ) for all 12 metals (Cu, Ag, Au, Ni, Pd, Pt, Rh, Ir, La, Yb, Ce, Th). These are used in all subsequent calculations.
- Evidence: `/app/outputs/parameters_used.log`

### Step 2: Determine pseudopotential core radius
- Role: process
- Action: For each metal, determine the effective core radius r_c of the Baria–Jani pseudopotential by imposing the zero-pressure condition. Compute the total pressure from the volume derivative of the Helmholtz free energy expression (F = E – TS) that includes the ionic, electronic, and electron-ion contributions with the hard-sphere structure factor and Taylor local-field correction. Iteratively adjust r_c until pressure equals zero at the given melting temperature and atomic volume. The converged r_c is used in the subsequent energy calculation.
- Evidence: `/app/outputs/core_radius_values.json`

### Step 3: Compute thermodynamic quantities
- Role: scored (load-bearing)
- Action: Using the determined core radius and the input parameters, compute for each metal the total enthalpy H (in 10^{-3} atomic units), total entropy S/k_B, and Helmholtz free energy F (in 10^{-3} a.u.), along with their component contributions: H_elect-ion, H_ion, H_elect; S_gas/k_B, S_η/k_B, S_elect/k_B. All q-space integrals must be carried out up to 40 k_F. Output a CSV file with all component and total values.
- Output file: `/app/outputs/thermodynamic_results.csv`
- Format: csv
- Contract: CSV with columns: metal (string), H_elect_ion (float, 10^{-3} a.u.), H_ion (float), H_elect (float), H_total (float), S_gas_kB (float), S_eta_kB (float), S_elect_kB (float), S_total_kB (float), F_total (float, 10^{-3} a.u.). One row per metal in any order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_results.csv
- path: `/app/outputs/thermodynamic_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with computed enthalpy, entropy and free energy components and totals for the 12 metals.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `H_elect_ion`, `H_ion`, `H_elect`, `H_total`, `S_gas_kB`, `S_eta_kB`, `S_elect_kB`, `S_total_kB`, `F_total`
  - `units`:
    - `H_elect_ion`: 1e-3 a.u.
    - `H_ion`: 1e-3 a.u.
    - `H_elect`: 1e-3 a.u.
    - `H_total`: 1e-3 a.u.
    - `S_gas_kB`: dimensionless
    - `S_eta_kB`: dimensionless
    - `S_elect_kB`: dimensionless
    - `S_total_kB`: dimensionless
    - `F_total`: 1e-3 a.u.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "H_elect_ion",
          "H_ion",
          "H_elect",
          "H_total",
          "S_gas_kB",
          "S_eta_kB",
          "S_elect_kB",
          "S_total_kB",
          "F_total"
        ],
        "units": {
          "H_elect_ion": "1e-3 a.u.",
          "H_ion": "1e-3 a.u.",
          "H_elect": "1e-3 a.u.",
          "H_total": "1e-3 a.u.",
          "S_gas_kB": "dimensionless",
          "S_eta_kB": "dimensionless",
          "S_elect_kB": "dimensionless",
          "S_total_kB": "dimensionless",
          "F_total": "1e-3 a.u."
        }
      },
      "description": "CSV file with computed enthalpy, entropy and free energy components and totals for the 12 metals."
    }
  ],
  "notes": ""
}
```

## How you are scored
After you submit `/app/outputs/thermodynamic_results.csv`, a hidden verifier will evaluate each of the 12 rows. For each metal it compares your reported total enthalpy H_total, total entropy S_total_kB, and Helmholtz free energy F_total to hidden reference values using appropriate tolerances. It also checks internal consistency: H_total must equal H_elect‑ion + H_ion + H_elect; S_total_kB must equal S_gas_kB + S_eta_kB + S_elect_kB; and F_total must equal H_total − T × S_total_kB / k_B (using the T you were given). The score is the fraction of metals for which all comparisons and consistency checks pass. The reference values and exact tolerances are not disclosed.
