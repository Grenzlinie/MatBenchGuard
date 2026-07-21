# Moiré Deflection Tomography Applicability for Argon Arc Plasma

## Problem background
Moiré deflection tomography is an optical technique that measures refractive-index gradients in transparent phase objects. While it has been widely applied to low-temperature flows such as flames and jets, extending it to diagnose high-temperature arc plasmas presents new challenges. In a plasma, the refractive index depends strongly on temperature because the contributions from neutral atoms, ions, and free electrons vary dramatically as ionization increases. For an argon arc plasma at atmospheric pressure, the combined effect of these species determines the temperature sensitivity of the refractive index, dn/dT. The limited resolution of moiré deflectometry — typically around Δn = 1×10⁻⁵ — restricts the temperature regions where reliable diagnosis is possible. This task investigates the temperature-dependent thermo-optic properties of an argon plasma and deduces the temperature intervals over which moiré deflection tomography can provide accurate measurements for a given error tolerance. The analysis considers two probe wavelengths, 532 nm and 808 nm, and requires computation of the electron density, refractive index, its temperature derivative, and the resulting relative measurement error across a wide temperature range.

## Approach
The approach is based on the Saha ionization model, which describes the equilibrium populations of neutral argon atoms, singly charged ions, doubly charged ions, and electrons. Both first and second ionizations (with ionization energies 15.759 eV and 27.629 eV) are considered because the plasma temperature can reach up to 20,000 K. The partition functions are taken as **constant values**:  
- neutral atom: Z₀ = 1  
- singly charged ion: Z₁ = 2.5  
- doubly charged ion: Z₂ = 1  

The system of Saha equations, combined with quasi‑neutrality (Nₑ = N₁⁺ + 2 N₂⁺) and the ideal gas law at 1 atm pressure, leads to a cubic equation for the electron density Nₑ. The Saha relations are:

\[
\frac{N_e N_1}{N_a} = K_1, \qquad 
\frac{N_e N_2}{N_1} = K_2
\]

where

\[
K_j = 2\,\frac{Z_{\text{upper}}}{Z_{\text{lower}}}\,
\left(\frac{2\pi m_e k_B T}{h^2}\right)^{\!3/2}
\exp\!\left(-\frac{E_{\text{ion}}}{k_B T}\right)
\]

with \(E_1 = 15.759\ \text{eV}\), \(E_2 = 27.629\ \text{eV}\), \(k_B = 8.617333\!\times\!10^{-5}\ \mathrm{eV\,K^{-1}}\) (used in the exponential). For the prefactor, use the following physical constants:
- Planck constant: \(h = 6.62607015 \times 10^{-34}\) J·s
- Electron mass: \(m_e = 9.10938356 \times 10^{-31}\) kg
- Boltzmann constant in SI units: \(k_B = 1.380649 \times 10^{-23}\) J·K⁻¹

The total heavy‑particle number density is given by the ideal gas law (using the SI value of \(k_B\)):

\[
N_t = \frac{P}{k_B T},\qquad P = 1\ \text{atm} = 101\,325\ \mathrm{Pa}.
\]

From the conservation equation \(N_a + N_1 + N_2 + N_e = N_t\) and the two Saha relations, the following cubic equation for \(N_e\) is obtained:

\[
N_e^3 + 2K_1 N_e^2 + (3K_1 K_2 - K_1 N_t) N_e - 2K_1 K_2 N_t = 0.
\]

After solving for \(N_e\), the other densities follow from:

\[
N_1 = \frac{N_e^2}{N_e + 2K_2},\qquad
N_2 = \frac{K_2 N_1}{N_e},\qquad
N_a = \frac{N_1 N_e}{K_1}
\]

and the total ion density is \(N_i = N_1 + N_2\).

The temperature derivatives of the number densities (needed for \(dn/dT\)) can be obtained either by analytical differentiation of the Saha equations or by central finite differences on a fine temperature grid.

Once the particle densities are known, the total refractive index \(n-1\) of the plasma is computed as a sum of contributions from neutral atoms, ions, and free electrons. For a given probe wavelength \(\lambda\) (in cm), the atom/ion contribution follows the dispersion formula

\[
n_{\text{atom}} - 1 = \frac{1}{L}\!\left(A + \frac{B}{\lambda^2}\right)N_a,
\]

where \(L = 2.687\times10^{19}\ \mathrm{cm^{-3}}\) is the Loschmidt number. The constants for argon are:

\[
A = 2.79\times10^{-4},\qquad B = 1.64\times10^{-14}\ \mathrm{cm^2}.
\]

The contribution of an ion is taken as 67% of that of an atom, i.e. factor 0.67.  
The electron contribution is negative:

\[
n_{\text{electron}} - 1 = -4.46\times10^{-14}\,\lambda^2\,N_e
\]

(\(\lambda\) in cm and \(N_e\) in cm⁻³).

Thus the total refractive index is

\[
n-1 = \frac{1}{L}\!\left(A + \frac{B}{\lambda^2}\right)\bigl(N_a + 0.67\,N_i\bigr) - 4.46\times10^{-14}\,\lambda^2\,N_e.
\]

The temperature derivative \(dn/dT\) is obtained by differentiating the above expression with respect to \(T\), which involves the derivatives \(dN_a/dT\), \(dN_i/dT\), and \(dN_e/dT\).

The relative measurement error \(e\) is defined as

\[
e = \frac{\Delta n}{\bigl| \frac{dn}{dT} \bigr| \, T},
\]

with the assumed moiré deflectometer resolution \(\Delta n = 1\times10^{-5}\).

The full computation is performed for two probe wavelengths:  
- 532 nm: \(\lambda = 5.32\times10^{-5}\ \mathrm{cm}\)  
- 808 nm: \(\lambda = 8.08\times10^{-5}\ \mathrm{cm}\)  

For each wavelength, you must substitute \(\lambda\) into the above formulas to obtain the actual numerical coefficients for \(n-1\) and \(dn/dT\) (i.e. compute the factors \(\frac{1}{L}(A + B/\lambda^2)\) and \(-4.46\times10^{-14}\lambda^2\)). The output includes a table of \(T\), \(N_e\), \(n-1\), \(dn/dT\), and \(e\). Finally, for each of the error thresholds 0.10, 0.12, 0.15, and 0.20, the contiguous temperature intervals where \(e\) does not exceed the threshold are identified. These intervals represent the applicable ranges for moiré deflection tomography under the corresponding measurement error requirements.

## Reproduction target
The goal is to numerically evaluate the thermo‑optic properties of an argon arc plasma at 1 atm over the temperature range 5000–20000 K and to determine the temperature intervals where moiré deflection tomography can operate within specified error limits. Specifically, produce the following four scored CSV files:

1. `thermo_optic_data_532nm.csv` – contains columns T, N_e, n-1, dn/dT, and e for the 532 nm probe wavelength.
2. `error_intervals_532nm.csv` – lists the temperature lower and upper bounds for error thresholds 0.10, 0.12, 0.15, 0.20 at 532 nm.
3. `thermo_optic_data_808nm.csv` – same schema as above but for the 808 nm probe wavelength.
4. `error_intervals_808nm.csv` – temperature intervals for the same four error thresholds at 808 nm.

The target is to compute these quantities from first principles using the Saha ionization model, the partition functions (\(Z_0=1\), \(Z_1=2.5\), \(Z_2=1\)), and the argon dispersion constants (\(A=2.79\times10^{-4}\), \(B=1.64\times10^{-14}\ \mathrm{cm^2}\)). The derived temperature intervals represent the main practical range in which the measurement error stays below the given tolerance. Do not attempt to reproduce experimental fringe images or comparisons with flame data; only the numerical analysis portion is required.

## Assets

- NumPy: pip install numpy
- SciPy: pip install scipy

## Workflow steps

### Step 1: Solve Saha equations for argon plasma particle densities
- Role: process
- Action: Implement the Saha ionization equations given above with the specified constants (\(E_1=15.759\ \mathrm{eV}\), \(E_2=27.629\ \mathrm{eV}\), partition functions \(Z_0=1\), \(Z_1=2.5\), \(Z_2=1\)). For temperatures from 5000 K to 20000 K in steps of about 500 K, numerically solve the cubic equation for electron density \(N_e\), then compute \(N_1\), \(N_2\), \(N_a\), and the temperature derivatives \(dN_e/dT\), \(dN_i/dT\), \(dN_a/dT\) (central finite differences are acceptable). Keep all number densities in cm⁻³.

### Step 2: Compute refractive index and dn/dT for λ=532 nm
- Role: scored (load-bearing)
- Action: Using the densities from the Saha solution, compute the refractive index by substituting \(\lambda = 5.32\times10^{-5}\ \mathrm{cm}\) into the total refractive index formula:

  \[
  n-1 = \frac{1}{L}\!\left(A + \frac{B}{\lambda^2}\right)\bigl(N_a + 0.67\,N_i\bigr) - 4.46\times10^{-14}\,\lambda^2\,N_e,
  \]
  with \(A=2.79\times10^{-4}\), \(B=1.64\times10^{-14}\ \mathrm{cm^2}\), \(L=2.687\times10^{19}\ \mathrm{cm^{-3}}\).

  Compute the temperature derivative \(dn/dT\) by differentiating this expression:
  \[
  \frac{dn}{dT} = \frac{1}{L}\!\left(A + \frac{B}{\lambda^2}\right)\!\left(\frac{dN_a}{dT} + 0.67\,\frac{dN_i}{dT}\right) - 4.46\times10^{-14}\,\lambda^2\,\frac{dN_e}{dT}.
  \]

  Calculate the relative measurement error:
  \[
  e = \frac{1\times10^{-5}}{|dn/dT| \cdot T}.
  \]
  Output a CSV with columns: T, N_e, n-1, dn/dT, e.
- Output file: `/app/outputs/thermo_optic_data_532nm.csv`
- Format: csv
- Contract: T: number (K), N_e: number (cm⁻³), n-1: number, dn/dT: number (K⁻¹), e: number
- Scoring: scored by hidden verifier

### Step 3: Determine applicable temperature intervals for λ=532 nm
- Role: scored
- Action: From the computed thermo‑optic data for 532 nm, find contiguous temperature intervals where \(e \le \text{threshold}\) for thresholds 0.10, 0.12, 0.15, 0.20. Report the lower and upper temperature bounds of the widest contiguous interval for each threshold. Output a CSV with columns: error_threshold, T_lower (K), T_upper (K).
- Output file: `/app/outputs/error_intervals_532nm.csv`
- Format: csv
- Contract: error_threshold: number (0.1, 0.12, 0.15, 0.20), T_lower: number (K), T_upper: number (K)
- Scoring: scored by hidden verifier

### Step 4: Compute refractive index and dn/dT for λ=808 nm
- Role: scored (load-bearing)
- Action: Reuse the Saha densities. For λ=808 nm (\(\lambda = 8.08\times10^{-5}\ \mathrm{cm}\)), compute the wavelength‑dependent factors exactly as in Step 2, using the same constants \(A\), \(B\), \(L\). That is, first compute

  \[
  f_{\text{atom}} = \frac{1}{L}\!\left(A + \frac{B}{\lambda^2}\right),\qquad f_e = -4.46\times10^{-14}\,\lambda^2.
  \]

  Then evaluate

  \[
  n-1 = f_{\text{atom}}\,(N_a + 0.67 N_i) + f_e\,N_e,
  \]
  \[
  \frac{dn}{dT} = f_{\text{atom}}\!\left(\frac{dN_a}{dT} + 0.67\frac{dN_i}{dT}\right) + f_e\,\frac{dN_e}{dT},
  \]
  and
  \[
  e = \frac{1\times10^{-5}}{|dn/dT| \cdot T}.
  \]

  Output a CSV with columns: T, N_e, n-1, dn/dT, e.
- Output file: `/app/outputs/thermo_optic_data_808nm.csv`
- Format: csv
- Contract: T: number (K), N_e: number (cm⁻³), n-1: number, dn/dT: number (K⁻¹), e: number
- Scoring: scored by hidden verifier

### Step 5: Determine applicable temperature intervals for λ=808 nm
- Role: scored
- Action: From the computed thermo‑optic data for 808 nm, find temperature intervals where \(e \le 0.10, 0.12, 0.15, 0.20\). Output a CSV with columns: error_threshold, T_lower (K), T_upper (K).
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
- description: Computed thermo‑optic quantities at 532 nm: temperature T, electron density N_e, refractive index (n-1), temperature derivative dn/dT, and relative measurement error e. Scored via structural consistency checks (peak locations, zero crossings, error formula consistency).
- schema:
  - `type`: table
  - `required_columns`: `T`, `N_e`, `n-1`, `dn/dT`, `e`
  - `units`:
    - `T`: K
    - `N_e`: cm⁻³
    - `n-1`: dimensionless
    - `dn/dT`: K⁻¹
    - `e`: dimensionless

### error_intervals_532nm.csv
- path: `/app/outputs/error_intervals_532nm.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Applicable temperature ranges at 532 nm for error tolerances 0.10, 0.12, 0.15, 0.20.
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
- description: Computed thermo‑optic quantities at 808 nm. Scored via structural consistency checks (peak locations, zero crossings, error formula consistency).
- schema:
  - `type`: table
  - `required_columns`: `T`, `N_e`, `n-1`, `dn/dT`, `e`
  - `units`:
    - `T`: K
    - `N_e`: cm⁻³
    - `n-1`: dimensionless
    - `dn/dT`: K⁻¹
    - `e`: dimensionless

### error_intervals_808nm.csv
- path: `/app/outputs/error_intervals_808nm.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Applicable temperature ranges at 808 nm for error tolerances 0.10, 0.12, 0.15, 0.20.
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
          "N_e": "cm⁻³",
          "n-1": "dimensionless",
          "dn/dT": "K⁻¹",
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
          "N_e": "cm⁻³",
          "n-1": "dimensionless",
          "dn/dT": "K⁻¹",
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