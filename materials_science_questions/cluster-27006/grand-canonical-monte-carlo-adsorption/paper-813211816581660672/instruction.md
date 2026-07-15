# Grand Canonical Monte Carlo Adsorption in Na‑ZSM‑5

## Problem background
Zeolites such as ZSM‑5 are crystalline aluminosilicates used for gas separations. In ZSM‑5, some silicon atoms can be replaced by aluminium, creating a charge deficit that is balanced by extra‑framework cations such as Na⁺. The resulting Na‑ZSM‑5 can exhibit enhanced adsorption of polar/quadrupolar molecules like CO₂ and N₂ compared to the all‑silica analogue (silicalite‑1).

This task investigates, via Grand Canonical Monte Carlo (GCMC) simulations, how the Si/Al ratio (and thus the Na⁺ and Al content) affects the adsorption of pure CO₂ and N₂ in Na‑ZSM‑5 at 308 K. Furthermore, for the lowest Si/Al ratio (13) the influence of the effective partial charge of the Na⁺ cation is studied by comparing simulation results with experimental adsorption data. The quantities to be computed are adsorption isotherms (loading vs. pressure) and isosteric heats of adsorption.

## Approach
Atomistic models of Na‑ZSM‑5 are built using the orthorhombic MFI framework coordinates. Al substitutions are introduced at the specified Si/Al ratios, and each is charge‑compensated by a Na⁺ cation placed at an intersection site. The zeolite framework and cations are treated as rigid; the cations remain frozen at their assigned locations.

Interatomic interactions are described by pair‑wise Lennard‑Jones potentials and Coulombic interactions with the force field parameters given in the table below (Table 1 of the source literature). Short‑range LJ interactions are truncated at 13 Å, and long‑range electrostatics between guest molecules are evaluated via Ewald summation with a real‑space cut‑off of 20 Å.

**Force field parameters**

| Species | ε/kB (K) | ε (kJ/mol) | σ (Å) | Partial charge q (e) |
|---------|----------|------------|-------|----------------------|
| **Zeolite** | | | | |
| Si | 0 | 0 | 0 | +2 (no Al) / +2.05 (Al present) |
| O_z | 89.6 | 0.745 | 2.806 | −1 (no Al) / −1.025 (Al present) |
| Al | 0 | 0 | 0 | +1.75 |
| O_Al | 89.6 | 0.745 | 2.806 | −1.2 |
| **CO₂** | | | | |
| C | 27.0 | 0.22 | 2.80 | +0.7 |
| O_g | 79.0 | 0.65 | 3.05 | −0.35 |
| **N₂** | | | | |
| N | 36.0 | 0.30 | 3.31 | −0.404 |
| m_Z | 0 | 0 | 0 | +0.81 |
| **Cation** | | | | |
| Na | 0 | 0 | 0 | +1 (default, adjustable) |
| Na–C (cross) | 20.44 | 0.17 | 2.72 | N/A |
| Na–O_g (cross) | 34.88 | 0.29 | 2.83 | N/A |
| Na–N (cross) | 105.8 | 0.88 | 2.82 | N/A |

Notes: The LJ parameters for cross interactions (Na–C, Na–O_g, Na–N) are provided; for other cross interactions, use Lorentz–Berthelot mixing rules. The Si and O_z charges depend on whether Al substitutions are present; for silicalite‑1 (no Al) use the first value, for Al‑containing structures use the second value (the framework charge neutrality must be maintained). The Na⁺ charge is set to 1e in the base simulations, and reduced to 0.7e or 0.4e in the charge‑variation step. To accelerate the simulations, the electrostatic potential from the rigid framework (including cations) is pre‑tabulated on a fine grid (0.2 Å spacing) once for each structure.

Grand Canonical Monte Carlo simulations are performed in the μVT ensemble for pure CO₂ and pure N₂ at 308 K over a wide pressure range. Equilibrium loadings are recorded at each pressure. Isosteric heats of adsorption are computed from the same trajectories using the fluctuation theorem, relating fluctuations in potential energy and particle number to the heat of adsorption.

For Si/Al = 13, simulations are repeated with Na⁺ partial charges of 1.0e, 0.7e, and 0.4e, and the resulting isotherms and heats are compared to experimental measurements (provided as hidden gold) to assess the effective charge carried by the cation.

## Reproduction target
Produce the following scored artifacts:

- Adsorption isotherms for pure CO₂ and N₂ in Na‑ZSM‑5 (T = 308 K) for six Si/Al ratios — ∞ (silicalite‑1), 95, 47, 31, 23, and 13 — with the Na⁺ charge set to 1e. The data must be written to `step_04_isotherms.csv` with columns: gas (CO2 or N2), SiAl, pressure_bar (bar), loading_molecules_per_uc (molecules per unit cell).

- Isosteric heats of adsorption for CO₂ and N₂ for the same six Si/Al ratios, computed as a function of loading. Output as `step_05_isosteric_heats.csv` with columns: gas, SiAl, loading_molecules_per_uc, Qst_kJ_per_mol (kJ/mol).

- For Si/Al = 13 only: adsorption isotherms and isosteric heats for CO₂ and N₂ obtained with three different Na⁺ partial charges (1.0e, 0.7e, 0.4e). The results must be combined into `step_07_charge_comparison.csv` with columns: gas, Na_charge_e, pressure_bar, loading_molecules_per_uc, Qst_kJ_per_mol.

The hidden checker will compare the simulated data against experimentally measured isotherms and heats (for Si/Al = 13) and against the expected trends among Si/Al ratios.

## Assets

- MFI zeolite framework coordinates (van Koningsveld et al., 1987): https://www.iza-structure.org/databases/
- Force field parameters (Lennard‑Jones and partial charges)
- RASPA molecular simulation package (open‑source GCMC code): https://github.com/raplep/raspa
- Python packages (numpy, pandas, scipy) for post‑processing: pypi

## Workflow steps

### Step 1: Build zeolite models and pre‑computed electrostatic potential grids
- Role: process
- Action: Construct atomistic models of Na‑ZSM‑5 for Si/Al ratios ∞, 95, 47, 31, 23, 13 using the MFI framework coordinates. Place Al substitutions and Na⁺ cations at intersection sites. Assign Lennard‑Jones parameters and partial charges from the force field table. Pre‑tabulate the electrostatic potential from the rigid framework (including cations) on a fine grid (0.2 Å spacing) for use in GCMC.
- Evidence: `/app/outputs/models_and_grids.tar.gz`

### Step 2: Molecular dynamics validation of frozen Na⁺ cation assumption
- Role: process
- Action: Perform short molecular dynamics simulations on the Na‑ZSM‑5 models to verify that Na⁺ cations remain near their initial Al‑adjacent sites and do not diffuse, justifying the frozen‑cation approximation used in GCMC.
- Evidence: `/app/outputs/md_validation.log`

### Step 3: GCMC simulations of CO₂ and N₂ adsorption at T=308 K (all Si/Al)
- Role: scored (load-bearing)
- Action: Run Grand Canonical Monte Carlo simulations in the μVT ensemble for pure CO₂ and pure N₂ using the models and potential grids from Step 01. Temperature = 308 K. Pressure ranges: CO₂ from 10⁻⁹ to 20 bar (extended to 300 bar for N₂). For each Si/Al ratio (∞, 95, 47, 31, 23, 13) with Na⁺ charge = 1e, collect equilibrium loadings (molecules/unit cell) at each simulated pressure. Output a CSV containing the adsorption isotherm data.
- Output file: `/app/outputs/step_04_isotherms.csv`
- Format: csv
- Contract: columns: gas (string: 'CO2' or 'N2'), SiAl (string: 'inf', '95', '47', '31', '23', '13'), pressure_bar (float), loading_molecules_per_uc (float)
- Scoring: scored by hidden verifier

### Step 4: Isosteric heats of adsorption for CO₂ and N₂ (all Si/Al)
- Role: scored
- Action: From the same GCMC trajectories used in Step 03, compute the isosteric heat of adsorption as a function of loading using the fluctuation theorem. Output a CSV containing the isosteric heat values.
- Output file: `/app/outputs/step_05_isosteric_heats.csv`
- Format: csv
- Contract: columns: gas (string: 'CO2' or 'N2'), SiAl (string), loading_molecules_per_uc (float), Qst_kJ_per_mol (float)
- Scoring: scored by hidden verifier

### Step 5: GCMC simulations with varied Na⁺ partial charges at Si/Al=13
- Role: scored
- Action: For Si/Al=13, repeat the GCMC simulations of Step 03 for CO₂ and N₂ with Na⁺ partial charges set to 0.7e and 0.4e (the 1e case is already in Step 03). Compute the corresponding adsorption isotherms and isosteric heats. Output a CSV containing the combined results for all three charges.
- Output file: `/app/outputs/step_07_charge_comparison.csv`
- Format: csv
- Contract: columns: gas (string: 'CO2' or 'N2'), Na_charge_e (float: 1.0, 0.7, 0.4), pressure_bar (float), loading_molecules_per_uc (float), Qst_kJ_per_mol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_isotherms.csv`
- `/app/outputs/step_05_isosteric_heats.csv`
- `/app/outputs/step_07_charge_comparison.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_isotherms.csv
- path: `/app/outputs/step_04_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Adsorption isotherms (loading vs pressure) for CO₂ and N₂ in Na‑ZSM‑5 at 308 K for Si/Al ratios ∞, 95, 47, 31, 23, 13.
- schema:
  - `type`: table
  - `required_columns`: `gas`, `SiAl`, `pressure_bar`, `loading_molecules_per_uc`
  - `units`:
    - `pressure_bar`: bar
    - `loading_molecules_per_uc`: molecules per unit cell

### step_05_isosteric_heats.csv
- path: `/app/outputs/step_05_isosteric_heats.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Isosteric heat of adsorption as a function of loading for CO₂ and N₂ in Na‑ZSM‑5 at 308 K.
- schema:
  - `type`: table
  - `required_columns`: `gas`, `SiAl`, `loading_molecules_per_uc`, `Qst_kJ_per_mol`
  - `units`:
    - `loading_molecules_per_uc`: molecules per unit cell
    - `Qst_kJ_per_mol`: kJ/mol

### step_07_charge_comparison.csv
- path: `/app/outputs/step_07_charge_comparison.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Adsorption isotherms and isosteric heats for Si/Al=13 with Na⁺ partial charges of 1.0e, 0.7e, and 0.4e.
- schema:
  - `type`: table
  - `required_columns`: `gas`, `Na_charge_e`, `pressure_bar`, `loading_molecules_per_uc`, `Qst_kJ_per_mol`
  - `units`:
    - `pressure_bar`: bar
    - `loading_molecules_per_uc`: molecules per unit cell
    - `Qst_kJ_per_mol`: kJ/mol

Notes: All outputs are produced by the GCMC workflow. The checker will recompute metrics (e.g., loading at specific pressures, relative tolerance, low‑pressure ordering, high‑pressure convergence, isosteric heat comparison) from these CSV files.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas",
          "SiAl",
          "pressure_bar",
          "loading_molecules_per_uc"
        ],
        "units": {
          "pressure_bar": "bar",
          "loading_molecules_per_uc": "molecules per unit cell"
        }
      },
      "description": "Adsorption isotherms (loading vs pressure) for CO₂ and N₂ in Na‑ZSM‑5 at 308 K for Si/Al ratios ∞, 95, 47, 31, 23, 13."
    },
    {
      "file": "step_05_isosteric_heats.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas",
          "SiAl",
          "loading_molecules_per_uc",
          "Qst_kJ_per_mol"
        ],
        "units": {
          "loading_molecules_per_uc": "molecules per unit cell",
          "Qst_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Isosteric heat of adsorption as a function of loading for CO₂ and N₂ in Na‑ZSM‑5 at 308 K."
    },
    {
      "file": "step_07_charge_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas",
          "Na_charge_e",
          "pressure_bar",
          "loading_molecules_per_uc",
          "Qst_kJ_per_mol"
        ],
        "units": {
          "pressure_bar": "bar",
          "loading_molecules_per_uc": "molecules per unit cell",
          "Qst_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Adsorption isotherms and isosteric heats for Si/Al=13 with Na⁺ partial charges of 1.0e, 0.7e, and 0.4e."
    }
  ],
  "notes": "All outputs are produced by the GCMC workflow. The checker will recompute metrics (e.g., loading at specific pressures, relative tolerance, low‑pressure ordering, high‑pressure convergence, isosteric heat comparison) from these CSV files."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden verifier that reads your CSV artifacts and compares selected data points to hidden gold values (paper‑reported simulation results and experimental measurements). For the isotherm file, the checker examines loading at specific pressures, verifies that low‑pressure loading increases with decreasing Si/Al ratio, and checks that high‑pressure loadings converge toward the silicalite‑1 saturation value. For the isosteric heat file, the checker compares the heat of adsorption at low and high loadings. For the charge‑comparison file, the checker computes the agreement between each charge‑variant simulation and the experimental isotherms (mean absolute percentage error) and identifies which charge yields the best match.

Scoring is monotonic in quality: meeting or beating the reference performance earns full credit for that artifact. If your results deviate from the hidden gold, the reward decreases proportionally to the deviation. Each scored artifact carries a weight; the final reward is a weighted sum of the per‑artifact scores.
