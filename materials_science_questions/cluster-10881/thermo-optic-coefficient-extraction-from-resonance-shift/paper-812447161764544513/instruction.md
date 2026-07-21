# Temperature Dependence of Phase-Matching Angle from SHG Intensity Data

## Problem background
NYAB (Nd:YAl₃(BO₃)₄) is a self-frequency-doubling crystal used in compact diode-pumped green lasers. 
The temperature dependence of the phase‑matching angle affects laser alignment and efficiency. 
Measuring the rate of change of the phase‑matching angle with temperature (dθₘ/dT) and the 
corresponding acceptance widths is essential for thermal management and cavity design.

## Approach
The second‑harmonic generation (SHG) intensity follows a sinc² function of the wave‑vector mismatch:

$$
P_{\text{SHG}} \propto \text{sinc}^2(\Delta k \, L / 2)
$$

where *L* is the crystal length, and *Δk* is the wave‑vector mismatch.  
Near the phase‑matching condition, *Δk* is approximately linear in both the propagation angle *θ* 
and the temperature *T*:

$$
\Delta k \approx \beta_\theta (\theta - \theta_{\text{m0}}) + \beta_T (T - T_0)
$$

Here *β_θ* is the angular sensitivity parameter and *β_T* the temperature sensitivity parameter.

By recording the SHG intensity versus angle at several fixed temperatures, each trace can be fitted 
to a sinc² model:

$$
y = A + B\,\text{sinc}^2\bigl[C\,(x - D)\bigr]
$$

For an angle scan, *x* is the propagation angle, *D* gives the phase‑matching angle *θₘ* at that 
temperature, and *C* is related to the angular sensitivity *β_θ* by *C = β_θ L/2*.  
A linear regression of the extracted *θₘ* values against *T* yields d*θₘ*/d*T*.

Independently, the ratio of the angular acceptance width to the temperature acceptance width, 
Δ*θ*/Δ*T*, can be obtained from the fitted sensitivity parameters. For the sinc² function the 
full‑width at half‑maximum (FWHM) condition leads to:

$$
\Delta\theta\,L = \frac{2.783\,L}{|C_{\text{avg}}|}, \qquad
\Delta T\,L = \frac{2.783\,L}{|C_T|}
$$

where *C_avg* is the average |*C*| from the angle scans and *C_T* is |*C*| from the temperature 
scan. The crystal length is *L* = 0.4 cm.  
The two independently determined quantities — the directly regressed d*θₘ*/d*T* and the 
acceptance‑width ratio Δ*θ*/Δ*T* — should agree according to the theoretical relation 

$$
|\mathrm{d}\theta_m/\mathrm{d}T| = \Delta\theta / \Delta T .
$$

## Reproduction target
Given the digitized SHG intensity vs. angle data at five temperatures (bundled as a CSV file) 
and SHG intensity vs. temperature data at a fixed propagation angle (bundled as a separate CSV 
file), your goal is to:

1. Extract the phase‑matching angles at each temperature by fitting a sinc² function.
2. Perform linear regression of the phase‑matching angle against temperature to obtain the 
   slope d*θₘ*/d*T* and its uncertainty.
3. Fit the temperature scan to a sinc² function to obtain the temperature sensitivity parameter.
4. Compute the angular and temperature acceptance width–length products (Δ*θ*·L and Δ*T*·L) 
   and their ratio Δ*θ*/Δ*T*.
5. Compare the independently determined d*θₘ*/d*T* and Δ*θ*/Δ*T* to assess the agreement 
   predicted by the theoretical relation between them.

## Assets
- `angle_scan_data.csv` – digitized SHG intensity vs. angle at five temperatures
- `temperature_scan_data.csv` – digitized SHG intensity vs. temperature at a fixed angle
- `scipy` – Python package for curve fitting and scientific computing
- `numpy` – numerical Python package

## Workflow steps

### Step 1: Fit sinc² to angle scans
- **Role:** process
- **Action:** Load `angle_scan_data.csv`, separate the five temperature scans, and fit each to 
  the model *y = A + B·sinc²[C·(x − D)]* using least‑squares curve fitting. Extract the fitted 
  parameters *D* (phase‑matching angle, in rad) and *C* for each temperature.
- **Evidence:** none

### Step 2: Output fitted angles
- **Role:** scored
- **Action:** Write the extracted phase‑matching angles (*D*) and the corresponding temperatures 
  to `fitted_angles.json`.
- **Output file:** `/app/outputs/fitted_angles.json`
- **Format:** json
- **Contract:** `{"T_C": [float], "D_rad": [float]}`
- **Scoring:** scored by hidden verifier

### Step 3: Linear regression of θₘ vs T
- **Role:** scored (load‑bearing)
- **Action:** Perform linear least‑squares regression on the (T, D) pairs from the angle fits. 
  Output the slope (d*θₘ*/d*T*), intercept, and rms residual.
- **Output file:** `/app/outputs/linear_regression_slope.json`
- **Format:** json
- **Contract:** `{"slope_rad_per_C": float, "intercept_rad": float, "rms_residual_rad": float}`
- **Scoring:** scored by hidden verifier

### Step 4: Fit sinc² to temperature scan
- **Role:** process
- **Action:** Load `temperature_scan_data.csv` and fit to 
  *y = A + B·sinc²[C_T·(T − T₀)]* using least‑squares curve fitting to obtain *C_T* and *T₀*.
- **Evidence:** none

### Step 5: Compute acceptance widths and ratio
- **Role:** process
- **Action:** Using the average |*C*| from the five angle fits (|*C_avg*|) and |*C_T*| from the 
  temperature fit, compute the acceptance width–length products in the required units:
  - Δ*θ*·L = 2.783 × 0.4 cm / |*C_avg*| → convert to mrad·cm (1 rad = 10³ mrad)
  - Δ*T*·L = 2.783 × 0.4 cm / |*C_T*| → in °C·cm
  Then compute the ratio Δ*θ*/Δ*T* = (Δ*θ*·L) / (Δ*T*·L) → expressed in rad/°C.
- **Evidence:** none

### Step 6: Output acceptance ratio
- **Role:** scored (load‑bearing)
- **Action:** Write Δ*θ*·L (in mrad·cm), Δ*T*·L (in °C·cm), and the ratio (in rad/°C) to 
  `acceptance_ratio.json`.
- **Output file:** `/app/outputs/acceptance_ratio.json`
- **Format:** json
- **Contract:** 
  `{"Delta_theta_L_mrad_cm": float, "Delta_T_L_C_cm": float, "ratio_rad_per_C": float}`
- **Scoring:** scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:

- `/app/outputs/fitted_angles.json`  
  Object with keys `T_C` (array of five temperatures in °C) and `D_rad` (array of five 
  phase‑matching angles in rad), in the same order as the scans.

- `/app/outputs/linear_regression_slope.json`  
  Object with keys `slope_rad_per_C` (d*θₘ*/d*T* in rad/°C), `intercept_rad` (intercept in rad), 
  and `rms_residual_rad` (rms residual of the linear fit in rad).

- `/app/outputs/acceptance_ratio.json`  
  Object with keys `Delta_theta_L_mrad_cm` (angular acceptance width–length product in mrad·cm), 
  `Delta_T_L_C_cm` (temperature acceptance width–length product in °C·cm), and 
  `ratio_rad_per_C` (Δ*θ*/Δ*T* expressed in rad/°C).

## Self-check before finishing (optional, not scored)
Before you finish, verify that:
- `fitted_angles.json` exists and contains the two required keys with five numeric values each.
- `linear_regression_slope.json` exists and contains the three required numeric keys.
- `acceptance_ratio.json` exists and contains the three required numeric keys.
- All JSON files are valid and the values are physically plausible (e.g., angles on the order of 
  milliradians, slope on the order of 10⁻⁵ rad/°C, acceptance widths consistent with the data).

This checks **shape only** — it does not verify scientific correctness, and passing it does not 
mean your answer is correct.