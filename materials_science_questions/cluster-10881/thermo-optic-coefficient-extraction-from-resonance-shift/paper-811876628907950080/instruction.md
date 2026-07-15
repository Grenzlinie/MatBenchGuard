# Moiré Deflection Tomography Applicability for Argon Arc Plasma

## Problem background
Moiré deflection tomography is an optical technique that measures refractive-index gradients in transparent phase objects. While it has been widely applied to low-temperature flows such as flames and jets, extending it to diagnose high-temperature arc plasmas presents new challenges. In a plasma, the refractive index depends strongly on temperature because the contributions from neutral atoms, ions, and free electrons vary dramatically as ionization increases. For an argon arc plasma at atmospheric pressure, the combined effect of these species determines the temperature sensitivity of the refractive index, dn/dT. The limited resolution of moiré deflectometry — typically around Δn = 1×10⁻⁵ — restricts the temperature regions where reliable diagnosis is possible. This task investigates the temperature-dependent thermo-optic properties of an argon plasma and deduces the temperature intervals over which moiré deflection tomography can provide accurate measurements for a given error tolerance. The analysis considers two probe wavelengths, 532 nm and 808 nm, and requires computation of the electron density, refractive index, its temperature derivative, and the resulting relative measurement error across a wide temperature range.

## Approach
The approach is based on the Saha ionization model, which describes the equilibrium populations of neutral argon atoms, singly charged ions, doubly charged ions, and electrons. For argon, both first and second ionizations (with ionization energies 15.759 eV and 27.629 eV) are considered because the plasma temperature can reach up to 20,000 K. Partition functions for the three species are incorporated to obtain realistic ionization fractions. The system of Saha equations, combined with quasi-neutrality and the ideal gas equation at 1 atm pressure, yields a cubic equation for the electron density. By solving this equation at temperatures from 5000 K to 20,000 K in steps of about 500 K, one obtains the number densities of all species and their temperature derivatives.

Once the particle densities are known, the total refractive index (n-1) of the plasma is computed as a sum of contributions from neutral atoms, ions, and free electrons, each depending on the probe wavelength. For a given wavelength λ, the atom/ion contribution follows a standard dispersion relation (using known constants A, B, and the Loschmidt number L), while the electron contribution is proportional to -λ². The temperature derivative dn/dT is obtained by differentiating the refractive-index expression with respect to T, which involves the derivatives of the number densities. The relative measurement error e is defined as e = Δn / (|dn/dT| · T), where Δn is the assumed moiré deflectometer resolution of 1×10⁻⁵.

The full computation is performed for two probe wavelengths: 532 nm (green laser) and 808 nm (near-infrared). For each wavelength, the output includes a table of T, N_e, n-1, dn/dT, and e. Finally, for each of the error thresholds 0.10, 0.12, 0.15, and 0.20, the contiguous temperature intervals where e does not exceed the threshold are identified. These intervals represent the applicable ranges for moiré deflection tomography under the corresponding measurement error requirements.

## Reproduction target
The goal is to numerically evaluate the thermo-optic properties of an argon arc plasma at 1 atm over the temperature range 5000–20000 K and to determine the temperature intervals where moiré deflection tomography can operate within specified error limits. Specifically, produce the following four scored CSV files:

1. `thermo_optic_data_532nm.csv` – contains columns T, N_e, n-1, dn/dT, and e for the 532 nm probe wavelength.
2. `error_intervals_532nm.csv` – lists the temperature lower and upper bounds for error thresholds 0.10, 0.12, 0.15, 0.20 at 532 nm.
3. `thermo_optic_data_808nm.csv` – same schema as above but for the 808 nm probe wavelength.
4. `error_intervals_808nm.csv` – temperature intervals for the same four error thresholds at 808 nm.

The target is to compute these quantities from first principles using the Saha ionization model, appropriate partition functions, and the known dispersion constants for argon. The derived temperature intervals represent the main practical range in which the measurement error stays below the given tolerance. Do not attempt to reproduce experimental fringe images or comparisons with flame data; only the numerical analysis portion is required.

## Assets

- NumPy: pip install numpy
- SciPy: pip install scipy

## Workflow steps

### Step 1: Solve Saha equations for argon plasma particle densities
- Role: process
- Action: Implement Saha ionization equations for argon (first and second ionization, E1=15.759 eV, E2=27.629 eV) at pressure 1 atm, using standard partition functions. For temperatures from 5000 K to 20000 K in steps of about 500 K, numerically solve the cubic equation for electron density N_e, then compute N1, N2, N_a, and temperature derivatives dN_e/dT, dN_i/dT, dN_a/dT using the given formulas. Save the resulting arrays to an evidence CSV file.
- Evidence: `/app/outputs/saha_densities.csv`

### Step 2: Compute refractive index and dn/dT for λ=532 nm
- Role: scored (load-bearing)
- Action: Using the densities from the Saha solution, compute the refractive index (n-1) = 1.05959e-23*(N_a+0.67N_i) - 1.2623e-22*N_e, its temperature derivative dn/dT = 1.05959e-23*(dN_a/dT+0.67 dN_i/dT) - 1.2623e-22*dN_e/dT, and the relative measurement error e = 1e-5 / (|dn/dT| * T). Output a CSV with columns: T, N_e, n-1, dn/dT, e.
- Output file: `/app/outputs/thermo_optic_data_532nm.csv`
- Format: csv
- Contract: T: number (K), N_e: number (cm^-3), n-1: number, dn/dT: number (K^-1), e: number
- Scoring: scored by hidden verifier

### Step 3: Determine applicable temperature intervals for λ=532 nm
- Role: scored
- Action: From the computed thermo-optic data for 532 nm, find contiguous temperature intervals where e ≤ threshold for thresholds 0.10, 0.12, 0.15, 0.20. Report the lower and upper temperature bounds of the main interval for each threshold. Output a CSV with columns: error_threshold, T_lower (K), T_upper (K).
- Output file: `/app/outputs/error_intervals_532nm.csv`
- Format: csv
- Contract: error_threshold: number (0.1, 0.12, 0.15, 0.20), T_lower: number (K), T_upper: number (K)
- Scoring: scored by hidden verifier

### Step 4: Compute refractive index and dn/dT for λ=808 nm
- Role: scored (load-bearing)
- Action: Reuse the Saha densities. For λ=808 nm (8080 Å), compute the wavelength-dependent constants f_atom = (1/L)*(A + B/(808e-7 cm)²) and f_e = -4.46e-14*(808e-7 cm)², using the same A, B, L as for 532 nm. Compute n-1 = f_atom*(N_a+0.67N_i) + f_e*N_e, dn/dT = f_atom*(dN_a/dT+0.67 dN_i/dT) + f_e*dN_e/dT, and e = 1e-5/(|dn/dT|*T). Output a CSV with columns: T, N_e, n-1, dn/dT, e.
- Output file: `/app/outputs/thermo_optic_data_808nm.csv`
- Format: csv
- Contract: T: number (K), N_e: number (cm^-3), n-1: number, dn/dT: number (K^-1), e: number
- Scoring: scored by hidden verifier

### Step 5: Determine applicable temperature intervals for λ=808 nm
- Role: scored
- Action: From the computed thermo-optic data for 808 nm, find temperature intervals where e ≤ 0.10, 0.12, 0.15, 0.20. Output a CSV with columns: error_threshold, T_lower (K), T_upper (K).
- Output file: `/app/outputs/error_intervals_808nm.csv`
- Format: csv
- Contract: error_threshold: number (0.1, 0.12, 0.15, 0.20), T_lower: number (K), T_upper: number (K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_optic_data_532nm.csv`
- `/app/outputs/error_intervals_532nm.csv`
- `/app/outputs/thermo_optic_data_808nm.csv`
- `/app/outputs/error_intervals_808nm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_optic_data_532nm.csv
- path: `/app/outputs/thermo_optic_data_532nm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed thermo-optic quantities at 532 nm: temperature T, electron density N_e, refractive index (n-1), temperature derivative dn/dT, and relative measurement error e. Scored via structural consistency checks (peak locations, zero crossings, error formula consistency).
- schema:
  - `type`: table
  - `required_columns`: `T`, `N_e`, `n-1`, `dn/dT`, `e`
  - `units`:
    - `T`: K
    - `N_e`: cm^-3
    - `n-1`: dimensionless
    - `dn/dT`: K^-1
    - `e`: dimensionless

### error_intervals_532nm.csv
- path: `/app/outputs/error_intervals_532nm.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Applicable temperature ranges at 532 nm for error tolerances 0.10, 0.12, 0.15, 0.20.
- schema:
  - `type`: table
  - `required_columns`: `error_threshold`, `T_lower`, `T_upper`
  - `units`:
    - `error_threshold`: dimensionless
    - `T_lower`: K
    - `T_upper`: K

### thermo_optic_data_808nm.csv
- path: `/app/outputs/thermo_optic_data_808nm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed thermo-optic quantities at 808 nm. Scored via structural consistency checks (peak locations, zero crossings, error formula consistency).
- schema:
  - `type`: table
  - `required_columns`: `T`, `N_e`, `n-1`, `dn/dT`, `e`
  - `units`:
    - `T`: K
    - `N_e`: cm^-3
    - `n-1`: dimensionless
    - `dn/dT`: K^-1
    - `e`: dimensionless

### error_intervals_808nm.csv
- path: `/app/outputs/error_intervals_808nm.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Applicable temperature ranges at 808 nm for error tolerances 0.10, 0.12, 0.15, 0.20.
- schema:
  - `type`: table
  - `required_columns`: `error_threshold`, `T_lower`, `T_upper`
  - `units`:
    - `error_threshold`: dimensionless
    - `T_lower`: K
    - `T_upper`: K

Notes: All outputs are CSVs with header row. The thermo‑optic data files are scored by structural audit (consistency checks, peak/zero locations); the interval files are scored against hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_optic_data_532nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "N_e",
          "n-1",
          "dn/dT",
          "e"
        ],
        "units": {
          "T": "K",
          "N_e": "cm^-3",
          "n-1": "dimensionless",
          "dn/dT": "K^-1",
          "e": "dimensionless"
        }
      },
      "description": "Computed thermo-optic quantities at 532 nm: temperature T, electron density N_e, refractive index (n-1), temperature derivative dn/dT, and relative measurement error e. Scored via structural consistency checks (peak locations, zero crossings, error formula consistency)."
    },
    {
      "file": "error_intervals_532nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "error_threshold",
          "T_lower",
          "T_upper"
        ],
        "units": {
          "error_threshold": "dimensionless",
          "T_lower": "K",
          "T_upper": "K"
        }
      },
      "description": "Applicable temperature ranges at 532 nm for error tolerances 0.10, 0.12, 0.15, 0.20."
    },
    {
      "file": "thermo_optic_data_808nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "N_e",
          "n-1",
          "dn/dT",
          "e"
        ],
        "units": {
          "T": "K",
          "N_e": "cm^-3",
          "n-1": "dimensionless",
          "dn/dT": "K^-1",
          "e": "dimensionless"
        }
      },
      "description": "Computed thermo-optic quantities at 808 nm. Scored via structural consistency checks (peak locations, zero crossings, error formula consistency)."
    },
    {
      "file": "error_intervals_808nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "error_threshold",
          "T_lower",
          "T_upper"
        ],
        "units": {
          "error_threshold": "dimensionless",
          "T_lower": "K",
          "T_upper": "K"
        }
      },
      "description": "Applicable temperature ranges at 808 nm for error tolerances 0.10, 0.12, 0.15, 0.20."
    }
  ],
  "notes": "All outputs are CSVs with header row. The thermo‑optic data files are scored by structural audit (consistency checks, peak/zero locations); the interval files are scored against hidden reference values."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. For each scored artifact, the verifier will:

- Read the submitted CSV files and check that they have the required columns and a reasonable number of rows.
- Recompute the measurement error e from the provided dn/dT and T (or directly use the e column) and verify that key structural features appear within expected tolerances: the electron density N_e should peak near a certain temperature, the refractive index (n-1) should cross zero at a particular temperature, and dn/dT should reach a minimum (zero) close to the N_e peak.
- Derive temperature intervals where e does not exceed each of the four thresholds and compare the resulting interval bounds to reference values.

The final reward is a weighted sum of scores from the individual artifacts. Agreement with the reference is judged with tolerances that account for legitimate differences in numerical implementation and partition function estimates. There is no requirement to match specific digits from the literature; instead, the verifier rewards physically correct trends and reasonable quantitative agreement. Simply reporting numbers without a correct underlying computation will not receive credit.
