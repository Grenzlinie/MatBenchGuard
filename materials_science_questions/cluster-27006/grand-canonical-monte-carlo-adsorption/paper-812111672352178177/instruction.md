# GCMC and MD of Benzene/CO₂ Mixture on Silicalite

## Problem background
Supercritical CO₂ is an environmentally benign solvent widely used for adsorption separation and adsorbent regeneration. Understanding the adsorption and diffusion of aromatic/CO₂ mixtures in zeolites is essential for designing such processes. This work uses molecular simulations to compute adsorption isotherms, heats, and diffusion coefficients for pure CO₂ and a benzene/CO₂ mixture in silicalite, providing quantitative insight into the competitive adsorption and transport processes.

## Approach
Grand Canonical Monte Carlo (GCMC) simulations are used to compute absolute and excess adsorption isotherms and isosteric heats of adsorption. Molecular Dynamics (MD) simulations yield self‑diffusion coefficients of CO₂ in the mixture. Bulk‑phase properties (chemical potentials, densities, enthalpy departures) are obtained from the Peng–Robinson equation of state, with the benzene/CO₂ binary interaction parameter fitted to vapor‑liquid equilibrium data. The simulations are performed on the silicalite ORTHO crystal structure with a specified force field for CO₂, benzene, and the framework. The workflow computes: (1) pure CO₂ absolute and excess adsorption isotherms at three temperatures; (2) isosteric heat of CO₂ adsorption vs. loading; (3) mixture adsorption isotherms for CO₂ and benzene at two temperatures; and (4) CO₂ self‑diffusion coefficients in the mixture as a function of pressure.

## Reproduction target
Produce the pure CO₂ absolute and excess adsorption isotherms at 308.2 K, 318.2 K, and 328.2 K over a pressure range up to 20 MPa, together with the isosteric heat of adsorption as a function of loading. For the mixture, produce the adsorption isotherms of benzene and CO₂ (benzene bulk mole fraction 0.001) at 318.2 K and 328.2 K over 1–15 MPa. Finally, compute the CO₂ self‑diffusion coefficient in the mixture at 328.2 K for at least five pressures; the reported values should show that the diffusion coefficient increases with pressure and is at least an order of magnitude lower than a typical pure‑CO₂ diffusion value in silicalite.

## Assets

- Silicalite MFI ORTHO crystal structure: http://www.iza-structure.org/databases/
- Force field parameters for CO₂, benzene, and silicalite
- RASPA2 molecular simulation code: https://github.com/nimafazel/RASPA2
- Benzene–CO₂ VLE data for binary interaction parameter fitting: 10.1021/je00055a019

## Workflow steps

### Step 1: Fit binary interaction parameter for benzene/CO₂ P-R EOS
- Role: process
- Action: Using published VLE data for the benzene/CO₂ system, fit the binary interaction parameter kij in the Peng–Robinson equation of state. The resulting kij will be used to compute bulk‑phase chemical potentials for the mixture.
- Evidence: `/app/outputs/fitted_kij.json`

### Step 2: Compute bulk fluid properties from P-R EOS
- Role: process
- Action: For all required temperature and pressure conditions (pure CO₂ at 308.2, 318.2, 328.2 K over low‑20 MPa; mixture at 318.2, 328.2 K, benzene mole fraction 0.001, pressures 1–15 MPa), use the Peng–Robinson EOS to calculate bulk‑phase chemical potentials, bulk fluid densities, and partial‑molar enthalpy departures. For the mixture, use the fitted kij from s0.
- Evidence: `/app/outputs/bulk_thermo.csv`

### Step 3: Run GCMC simulations for pure CO₂ on silicalite
- Role: process
- Action: Perform Grand Canonical Monte Carlo simulations of pure CO₂ on the silicalite ORTHO structure using the force field parameters and the bulk chemical potentials from s1. Use a 2×2×2 unit cell simulation box, periodic boundary conditions, and energy/cavity biasing. Run approximately 6×10⁶ MC steps per state point, discarding the first half for equilibration. Record absolute adsorption loading and average internal energy of the adsorbed phase for every state point.
- Evidence: `/app/outputs/pure_co2_simulation.log`

### Step 4: Compute pure CO₂ adsorption isotherms
- Role: scored
- Action: From the GCMC output of s2, extract the absolute adsorption loading n_abs (mmol g⁻¹) for each state point. Calculate the excess adsorption n_ex using n_ex = n_abs − Vg·ρg, where Vg=175 cm³ kg⁻¹ and ρg is the bulk molar density from s1. Write a CSV file containing T, P, n_abs, n_ex for all simulated (T, P) pairs.
- Output file: `/app/outputs/step_01_pure_co2_isotherms.csv`
- Format: csv
- Contract: T (K), P (MPa), n_abs (mmol g−1), n_ex (mmol g−1)
- Scoring: scored by hidden verifier

### Step 5: Compute pure CO₂ isosteric heat of adsorption
- Role: scored
- Action: From the GCMC internal energies of s2 and the bulk enthalpy departure from s1, compute the isosteric heat of adsorption Q_st as a function of absolute loading n_abs. Write a CSV with columns n_abs, Q_st spanning the loading range.
- Output file: `/app/outputs/step_02_pure_co2_qst.csv`
- Format: csv
- Contract: n_abs (mmol g−1), Qst (kJ mol−1)
- Scoring: scored by hidden verifier

### Step 6: Run GCMC simulations for benzene/CO₂ mixture
- Role: process
- Action: Perform GCMC simulations for the benzene/CO₂ mixture on the same silicalite structure, using the mixture chemical potentials from s1 (with fitted kij). Set the bulk benzene mole fraction to 0.001 and run at 318.2 K and 328.2 K for pressures from 1 to 15 MPa. Use ≈1×10⁷ MC steps with the same equilibration protocol. Record individual adsorption loadings of benzene and CO₂ for each state point.
- Evidence: `/app/outputs/mixture_simulation.log`

### Step 7: Compute mixture adsorption isotherms
- Role: scored (load-bearing)
- Action: From the output of s5, extract the adsorption amounts of benzene (n_benzene in mmol g⁻¹) and CO₂ (n_CO₂ in mmol g⁻¹) at each simulated (T, P) point. Write a CSV file with columns T, P, n_benzene, n_CO₂ for all state points.
- Output file: `/app/outputs/step_03_mixture_isotherms.csv`
- Format: csv
- Contract: T (K), P (MPa), n_benzene (mmol g−1), n_CO2 (mmol g−1)
- Scoring: scored by hidden verifier

### Step 8: Run MD simulations for benzene/CO₂ mixture
- Role: process
- Action: Using the final configurations from the mixture GCMC runs (s5) for five pressures (e.g. 3, 5, 9, 12, 15 MPa) at 328.2 K, perform NVT Molecular Dynamics simulations with the same force field and simulation box. Run equilibration (≥100 ps) followed by a production run (≥200 ps) to compute mean‑squared displacements. Record centre‑of‑mass trajectories.
- Evidence: `/app/outputs/md_trajectories.log`

### Step 9: Compute CO₂ self‑diffusion coefficients from MD
- Role: scored
- Action: From the MD trajectories of s7, compute the mean‑squared displacement (MSD) of CO₂ molecules and obtain the self‑diffusion coefficient D_CO₂ (m² s⁻¹) via the Einstein relation. Write a CSV file with columns P, D_CO₂ for the five mixture pressures.
- Output file: `/app/outputs/step_04_md_diffusion.csv`
- Format: csv
- Contract: P (MPa), D_CO2 (m2 s−1)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_pure_co2_isotherms.csv`
- `/app/outputs/step_02_pure_co2_qst.csv`
- `/app/outputs/step_03_mixture_isotherms.csv`
- `/app/outputs/step_04_md_diffusion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_pure_co2_isotherms.csv
- path: `/app/outputs/step_01_pure_co2_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pure CO₂ absolute and excess adsorption isotherms. One row per simulated (T,P) point (3 temperatures × ~10 pressures).
- schema:
  - `type`: table
  - `required_columns`: `T`, `P`, `n_abs`, `n_ex`
  - `units`:
    - `T`: K
    - `P`: MPa
    - `n_abs`: mmol g−1
    - `n_ex`: mmol g−1

### step_02_pure_co2_qst.csv
- path: `/app/outputs/step_02_pure_co2_qst.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Isosteric heat of adsorption as a function of CO₂ absolute loading. At least 10 rows spanning the loading range.
- schema:
  - `type`: table
  - `required_columns`: `n_abs`, `Qst`
  - `units`:
    - `n_abs`: mmol g−1
    - `Qst`: kJ mol−1

### step_03_mixture_isotherms.csv
- path: `/app/outputs/step_03_mixture_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Benzene/CO₂ mixture adsorption isotherms at bulk benzene mole fraction 0.001. One row per simulated (T,P) point (2 temperatures × ≥5 pressures).
- schema:
  - `type`: table
  - `required_columns`: `T`, `P`, `n_benzene`, `n_CO2`
  - `units`:
    - `T`: K
    - `P`: MPa
    - `n_benzene`: mmol g−1
    - `n_CO2`: mmol g−1

### step_04_md_diffusion.csv
- path: `/app/outputs/step_04_md_diffusion.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CO₂ self‑diffusion coefficients in the benzene/CO₂ mixture at 328.2 K. One row for each of the five simulated pressures (e.g. 3, 5, 9, 12, 15 MPa).
- schema:
  - `type`: table
  - `required_columns`: `P`, `D_CO2`
  - `units`:
    - `P`: MPa
    - `D_CO2`: m2 s−1

Notes: All scored files are compared to hidden gold values or structural checks. The binary interaction parameter fitting and P-R EOS calculations are included as process steps; their correctness is enforced through the load‑bearing mixture isotherm check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_pure_co2_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P",
          "n_abs",
          "n_ex"
        ],
        "units": {
          "T": "K",
          "P": "MPa",
          "n_abs": "mmol g−1",
          "n_ex": "mmol g−1"
        }
      },
      "description": "Pure CO₂ absolute and excess adsorption isotherms. One row per simulated (T,P) point (3 temperatures × ~10 pressures)."
    },
    {
      "file": "step_02_pure_co2_qst.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_abs",
          "Qst"
        ],
        "units": {
          "n_abs": "mmol g−1",
          "Qst": "kJ mol−1"
        }
      },
      "description": "Isosteric heat of adsorption as a function of CO₂ absolute loading. At least 10 rows spanning the loading range."
    },
    {
      "file": "step_03_mixture_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P",
          "n_benzene",
          "n_CO2"
        ],
        "units": {
          "T": "K",
          "P": "MPa",
          "n_benzene": "mmol g−1",
          "n_CO2": "mmol g−1"
        }
      },
      "description": "Benzene/CO₂ mixture adsorption isotherms at bulk benzene mole fraction 0.001. One row per simulated (T,P) point (2 temperatures × ≥5 pressures)."
    },
    {
      "file": "step_04_md_diffusion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "P",
          "D_CO2"
        ],
        "units": {
          "P": "MPa",
          "D_CO2": "m2 s−1"
        }
      },
      "description": "CO₂ self‑diffusion coefficients in the benzene/CO₂ mixture at 328.2 K. One row for each of the five simulated pressures (e.g. 3, 5, 9, 12, 15 MPa)."
    }
  ],
  "notes": "All scored files are compared to hidden gold values or structural checks. The binary interaction parameter fitting and P-R EOS calculations are included as process steps; their correctness is enforced through the load‑bearing mixture isotherm check."
}
```

## How you are scored
Each scored artifact (CSV file) is evaluated independently by a hidden verifier that compares your submitted values against reference data or structural criteria. The verifier checks column structure and data integrity, then scores each artifact according to accuracy thresholds and trend consistency. Partial credit is awarded per artifact, and the final reward is the weighted sum of these scores. Simply reporting the paper's numerical results without executing the required simulations will be detected by consistency checks and result in a low score.
