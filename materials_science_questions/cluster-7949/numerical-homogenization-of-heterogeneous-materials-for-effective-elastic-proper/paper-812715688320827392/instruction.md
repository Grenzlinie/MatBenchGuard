# Radial Stress at IL/Al Interface in UMo/Al Dispersion Fuel

## Problem background
UMo/Al dispersion fuel—uranium‑molybdenum alloy particles dispersed in an aluminum matrix—is a candidate for converting research reactors from highly‑enriched to low‑enriched uranium. During irradiation, the fuel meat undergoes complex microstructural changes: interaction layer (IL) growth between the UMo particles and the Al matrix, fission‑induced swelling, and pore formation. Large pores, which can lead to excessive meat swelling (breakaway swelling), are often observed at the IL/Al matrix interface, where the local mechanical state strongly influences pore nucleation and growth. Accurately predicting the radial stress at this interface as a function of fission density is therefore essential for fuel performance assessment and for modeling pore evolution. This task reproduces that local stress prediction using a physics‑based analytical stress model developed for dispersion fuel geometry.

## Model equations and data

### 1. Geometry and hypothetical unit cell
The calculation domain is a three‑layer spherical composite: a UMo fuel particle of radius $r_f$, surrounded by an interaction layer (IL) of outer radius $r_{IL}$, and an outer aluminum matrix shell of outer radius $r_m$. A hypothetical fission gas bubble of radius $r_i$ sits at the centre of the UMo particle.

### 2. Governing equations
For each region, the total strain is the sum of elastic, creep, swelling, thermal expansion and IL‑formation components:
$$
\begin{aligned}
\varepsilon_r &= \frac{1}{E}\bigl[\sigma_r - 2\nu\sigma_\theta\bigr] + \int_0^t A_c \dot f\bigl[\sigma_r - 2\mu\sigma_\theta\bigr]\,d\tau + S_r + \eta_r + \beta_r \tag{1}\\
\varepsilon_\theta &= \frac{1}{E}\bigl[(1-\nu)\sigma_\theta - \nu\sigma_r\bigr] + \int_0^t A_c \dot f\bigl[(1-\mu)\sigma_\theta - \mu\sigma_r\bigr]\,d\tau + S_\theta + \eta_\theta + \beta_\theta \tag{2}
\end{aligned}
$$

Kinematic relations in spherical coordinates:
$$
\varepsilon_r = \frac{\partial u}{\partial r},\qquad \varepsilon_\theta = \frac{u}{r} \tag{3,4}
$$

Mechanical equilibrium:
$$
\frac{\partial\sigma_r}{\partial r} - \frac{2}{r}(\sigma_\theta - \sigma_r) = 0 \tag{5}
$$

### 3. Closed‑form stress solutions
Because the swelling, thermal and IL‑formation strains are isotropic, the difference terms $\Delta S = S_r-S_\theta$, etc., are zero, and the derived function $f(t)$ vanishes. The general solution of (1)–(5) reduces to
$$
\sigma_r(r) = C_1 + \frac{C_2}{r^3},\qquad \sigma_\theta(r) = C_1 - \frac{C_2}{2r^3} \tag{9a,10a}
$$
where $C_1$ and $C_2$ are integration constants determined by boundary and interface conditions.

#### 3.1 Boundary and interface conditions
At the inner bubble surface ($r=r_i$): $\sigma_r^{\rm f}(r_i) = P_i$  (B1)

At the UMo/IL interface ($r=r_f$): $\sigma_r^{\rm f}(r_f) = \Pi_1$, $\sigma_r^{\rm IL}(r_f) = \Pi_1$  (B2-B3)

At the IL/Al interface ($r=r_{IL}$): $\sigma_r^{\rm IL}(r_{IL}) = \Pi_2$, $\sigma_r^{\rm Al}(r_{IL}) = \Pi_2$  (B4-B5)

At the outermost surface ($r=r_m$): $\sigma_r^{\rm Al}(r_m) = \sigma_h$  (B6)

$\Pi_1$ and $\Pi_2$ are the unknown interfacial radial stresses; $P_i$ is the fission gas bubble pressure; $\sigma_h$ is the external hydrostatic stress.

#### 3.2 Explicit coefficients
Applying the conditions yields for each region:

**UMo fuel**
$$
C_1^{\rm f} = -\frac{P_i r_i^3 - \Pi_1 r_f^3}{r_f^3 - r_i^3},\qquad
C_2^{\rm f} = \frac{r_i^3 r_f^3 (P_i - \Pi_1)}{r_f^3 - r_i^3} \tag{B7,B8}
$$

**Interaction layer (IL)**
$$
C_1^{\rm IL} = -\frac{-\Pi_1 r_f^3 + \Pi_2 r_{IL}^3}{r_f^3 - r_{IL}^3},\qquad
C_2^{\rm IL} = -\frac{r_f^3 r_{IL}^3 (\Pi_1 - \Pi_2)}{r_f^3 - r_{IL}^3} \tag{B9,B10}
$$

**Al matrix**
$$
C_1^{\rm Al} = -\frac{\sigma_h r_m^3 - \Pi_2 r_{IL}^3}{r_{IL}^3 - r_m^3},\qquad
C_2^{\rm Al} = -\frac{r_{IL}^3 r_m^3 (\Pi_2 - \sigma_h)}{r_{IL}^3 - r_m^3} \tag{B11,B12}
$$

### 4. Determination of $\Pi_1$ and $\Pi_2$
The interfacial stresses are obtained by enforcing displacement continuity at the two interfaces. The radial displacement follows from (4) and (2):
$$
u(r) = r\,\varepsilon_\theta = r\left\{ \frac{1}{E}\bigl[(1-\nu)\sigma_\theta - \nu\sigma_r\bigr] + \int_0^t A_c\dot f\bigl[(1-\mu)\sigma_\theta - \mu\sigma_r\bigr]d\tau + S_\theta + \eta_\theta + \beta_\theta \right\} \tag{6}
$$
At $r=r_f$ (UMo/IL): $u^{\rm f}(r_f) = u^{\rm IL}(r_f)$.  
At $r=r_{IL}$ (IL/Al): $u^{\rm IL}(r_{IL}) = u^{\rm Al}(r_{IL})$.

Substituting the stress expressions (9a,10a) with the coefficients (B7)-(B12) into (6) gives two equations that are linear in $\Pi_1$ and $\Pi_2$ (after discretising the time integral). These are solved numerically at each time or fission‑density step. The right‑hand side depends on geometry ($r_f,r_{IL},r_m$), material properties, accumulated creep, swelling/thermal/IL strains, $P_i$ and $\sigma_h$.

### 5. Fission gas bubble pressure $P_i$
The bubble radius $r_i$ is obtained from the gaseous swelling component $x_g = (\Delta V/V_0)_g$:
$$
r_i^3 = r_f^3\,\frac{x_g}{x_g+1} \tag{15}
$$
The bubble pressure follows from the ideal gas law:
$$
P_i = \frac{k\,Y_{fg}\,F_d\,T_f}{x_g} \tag{16}
$$
with $k = 1.380649\times10^{-23}$ J/K, $Y_{fg}=0.25$ (fission gas yield per fission), $F_d$ fission density (fissions/cm³), $T_f$ fuel temperature (K). $x_g$ is obtained from the swelling correlations below.

### 6. Irradiation correlations

#### 6.1 UMo total swelling
$(\Delta V/V_0)_s$ in percent, $F_d$ in $10^{21}$ fission/cm³:
- **U‑10Mo** (plate V6022M):
  - if $F_d \le 3.0$: $(\Delta V/V_0)_s = 5.0\,F_d$
  - else: $(\Delta V/V_0)_s = 15 + 6.3\,(F_d-3) + 0.33\,(F_d-3)^2$

- **U‑7Mo** (plate R3R108):
  - if $F_d \le 2.0$: $(\Delta V/V_0)_s = 5.0\,F_d$
  - else: $(\Delta V/V_0)_s = 10 + 6.7\,(F_d-2) + 0.58\,(F_d-2)^2$

#### 6.2 Gaseous swelling (used for $x_g$)
- **U‑10Mo**:
  - $F_d \le 3.0$: $(\Delta V/V_0)_g = 1.0\,F_d$
  - else: $(\Delta V/V_0)_g = 3.0 + 6.3\,(F_d-3) + 0.33\,(F_d-3)^2$

- **U‑7Mo**:
  - $F_d \le 2.0$: $(\Delta V/V_0)_g = 1.0\,F_d$
  - else: $(\Delta V/V_0)_g = 2.0 + 6.7\,(F_d-2) + 0.58\,(F_d-2)^2$

#### 6.3 IL fission‑induced swelling
$(\Delta V/V_0)_{IL} = 6.4\,F_d^{IL}$   (in %), with $F_d^{IL} = \psi F_d$, $\psi = 0.27$.

#### 6.4 Interaction layer growth
IL thickness $Y$ (μm) evolves as $Y^2 = Y_0^2\,f_{Si}\,f_{Mo}$, where  
$Y_0^2 = 2.6\times10^{-8}\,\dot f^{1/2} \exp\!\bigl(-32009/(R T)\bigr)\,t$  (C9)  
with $\dot f$ fission rate (fission/cm³/s), $T$ temperature (K), $t$ time (s), $R = 8.314$ J/mol K.

Si addition factor:
$$
\begin{aligned}
f_{Si} = &\,(1.201 - 6.2\times10^{-4}T)\,\exp\!\bigl[-(10.333 - 2.1\times10^{-2}T)\,W_{Si}\bigr] \\
&+ (6.2\times10^{-4}T - 0.201)\,\exp\!\bigl[-(8.1\times10^{-4}T - 0.302)\,W_{Si}\bigr] \quad (C10)
\end{aligned}
$$
with $W_{Si}$ Si content in wt% (0 for V6022M, 5 for R3R108), $T \le 473$ K.  
Mo content factor: $f_{Mo} = 1.35 - 0.05\,W_{Mo}$  (C11), with $W_{Mo}$ Mo content in wt% (10 for V6022M, 7 for R3R108).

From $Y$ and the uniform‑size FCC particle geometry the IL volume $V_{IL}$ and consumed volumes are obtained; for the stress model we need the volume changes expressed via the strains in §6.6. The intermediate consumed volumes are:
$$
V_f^c = \frac{\rho_{IL}}{\rho_f}\frac{M_f}{M_{IL}}\,V_{IL},\qquad
V_{Al}^c = 0.5\,\frac{\rho_{IL}}{\rho_{Al}}\frac{M_{Al}}{M_{IL}}\,V_{IL} \tag{C12,C13}
$$
with densities and molecular masses from §7.

#### 6.5 Thermal expansion
$\eta = \alpha\,(T - T_{\rm ref})$, $T_{\rm ref}=298$ K. Linear expansion coefficients $\alpha$ are listed in the material table.

#### 6.6 Chemical‑expansion strains (IL growth)
The isotropic strain due to IL volume change is $\beta = \tfrac{1}{3}\ln\!\bigl[1 + (\Delta V/V_0)^c\bigr]$, where

- for IL: $(\Delta V/V_0)^c_{IL} = V_{IL}/V^0_{IL}$   (C15)
- for UMo (consumption): $(\Delta V/V_0)^c_f = -V_f^c/V^0_f$   (C17)
- for Al (consumption): $(\Delta V/V_0)^c_{Al} = -V_{Al}^c/V^0_{Al}$   (C19)

The initial volumes $V^0_f$, $V^0_{IL}$, $V^0_{Al}$ are computed from the initial radii $r_f^0$, $r_f^0$+0.5 μm (initial IL thickness) and $r_m^0$, respectively. $r_m^0$ is determined from the uranium loading (see Table 2).

#### 6.7 Fission‑induced creep
The effective creep strain increment over time step $\Delta t$ is
$$
\Delta\bar\varepsilon^c = A_c\,(\sigma_r - \sigma_\theta)\,\dot f\,\Delta t \quad \text{(from Eq. 22-23)}
$$
The creep contribution to the radial and circumferential strains is taken as one‑third of the effective strain (isotropic creep).

### 7. Material properties (Table 1 of the paper)
Quantities are for each constituent.

**UMo (U‑10Mo for V6022M, U‑7Mo for R3R108):**
- Density: 17.1 g/cm³ (10Mo), 17.3 g/cm³ (7Mo)
- Mean linear thermal expansion $\alpha$ (10⁻⁶ K⁻¹): $7.91 + 1.21\times10^{-2}\,T$ (valid for both, T in K)
- Young’s modulus $E$ (GPa): 67.7 (10Mo), 50.6 (7Mo)
- Poisson’s ratio $\nu$: 0.34; under creep $\mu$: 0.34
- Creep constant $A_c$: $500\times10^{-25}$ cm³/MPa

**IL:**
- Density: 6.10 g/cm³
- $\alpha$: 16.5 K⁻¹
- $E$: 134 GPa
- $\nu$: 0.241, $\mu$: 0.241
- $A_c$: $400\times10^{-25}$ cm³/MPa

**Al matrix:**
- Density: $2.7\,(1 + \bar\alpha\,\Delta T)^{-3}$ g/cm³
- $\alpha$: $18.1 + 2.38\times10^{-2}\,T - 2.94\times10^{-5}\,T^2 + 3.03\times10^{-8}\,T^3$ K⁻¹
- $E$: $70.3\,[1 - 4.8\times10^{-4}\,(T-293)]$ GPa
- $\nu$: 0.33, $\mu$: 0.5
- $A_c$: $50\times10^{-25}$ cm³/MPa

Molecular masses (g/mol): $M_U = 238.0$, $M_{Al}=26.98$, $M_{Mo}=95.94$.  
For U‑10Mo: $M_f \approx 223.8$, for U‑7Mo: $M_f \approx 224.5$.  
For IL (U(Mo)Al₄): $M_{IL} \approx 431.8$.

### 8. Plate fabrication and irradiation data (Table 2)
Input parameters for the two plates. Fission density at end of life (EOL) and temperature are location‑dependent.

| Parameter                  | V6022M        | R3R108        |
|----------------------------|---------------|---------------|
| Fuel meat composition       | U‑10Mo/Al     | U‑7Mo/Al‑5Si  |
| U‑loading (gU/cm³)         | 6             | 8             |
| Irradiation time (EFPD)    | 257           | 98            |
| UMo particle size (µm)     | 50            | 50            |
| Initial IL thickness (µm)  | 0.5           | 0.5           |
| **Location A**                              |
| Fission density (10²¹ f/cm³‑UMo) | 5.91          | 5.30          |
| Temperature (°C)                     | 134           | 274           |
| **Location B**                              |
| Fission density               | 5.68          | 4.78          |
| Temperature                    | 139           | 264           |
| **Location C**                              |
| Fission density               | 5.43          | 4.16          |
| Temperature                    | 139           | 244           |

Fission density values are from the paper, temperature values are calculated in the study. Use life‑averaged fission rate (fission density / irradiation time) for $\dot f$ and the listed average temperature for $T$ in the integrations.

### 9. External hydrostatic stress $\sigma_h$
$\sigma_h$ as a function of fission density for each plate/location is provided as a CSV file (`sigma_h_V6022M_A.csv`, etc.). These data are digitised from Fig. 9 and must be loaded and interpolated at each time step.

### 10. Iterative solution procedure (Section 2.5)
For each case (plate, location), perform the following over a discretised fission‑density range from 0 to $F_d^{\rm EOL}$ (≥50 points):

1. Initialise radii: $r_f^0 = d/2$ (d = 50 µm), $r_{IL}^0 = r_f^0 + Y_0$ (initial IL thickness), $r_m^0$ = outer radius from U‑loading and volume fractions (see note). Set $F_d=0$.
2. At each new $F_d$ step (increment $\Delta F_d$):
   a. Update fission density, compute effective time step $\Delta t = \Delta F_d / \dot f$.
   b. Calculate all swelling, thermal, IL growth strains, and bubble pressure $P_i$ (Eq. 16).
   c. Obtain $\sigma_h$ from the provided CSV.
   d. Iterate to solve for $\Pi_1$, $\Pi_2$:
      - Start with previous time step values or initial guesses.
      - Form the two displacement continuity equations using (6), with stresses expressed via (9a,10a) and coefficients (B7-B12). The integral over time in (6) is evaluated numerically, e.g., by Euler forward with the current and previous stress states.
      - Solve the linear system for $\Pi_1$, $\Pi_2$.
      - Update the interface radii: $r_f^{k+1} = r_f^k + u^f(r_f^k)$, $r_{IL}^{k+1} = r_{IL}^k + u^{IL}(r_{IL}^k)$, $r_m^{k+1} = r_m^k + u^{Al}(r_m^k)$.
      - Check convergence $\max(|\Delta r|/r) < 10^{-4}$. If not converged, repeat with updated radii.
   e. Once converged, record $F_d$ and $\sigma_r^{\rm Al}(r_{IL}) = \Pi_2$.
3. Proceed to next $F_d$ step, using converged radii as initial guess for next step.

The outer matrix radius $r_m$ in the unit cell corresponds to the equivalent matrix volume surrounding one UMo particle. It is determined from the U‑loading $U_{\rm load}$ (gU/cm³) and particle size. Using the relation $U_{\rm load} = \rho_U^{fuel} V_f / V_{\rm cell}$, where $\rho_U^{fuel}$ is the uranium density in the fuel particle (≈ $w_U \rho_f$), the cell volume is $V_{\rm cell} = (4/3)\pi r_m^3$. Thus
$$
r_m = r_f \left(\frac{\rho_U^{fuel}}{U_{\rm load}}\right)^{1/3}
$$
where $\rho_U^{fuel} = w_U \rho_f$, $w_U$ is the mass fraction of uranium in the fuel alloy (≈0.9 for 10Mo, 0.93 for 7Mo). For V6022M ($U_{\rm load}=6$ gU/cm³, $\rho_f$=17.1 g/cm³) and R3R108 ($U_{\rm load}=8$ gU/cm³, $\rho_f$=17.3 g/cm³) compute $r_m$. This sets the initial $r_m^0$.

## Reproduction target
Produce a CSV file, `ilal_stress_vs_fd.csv`, that reports the radial stress (MPa) at the IL/Al matrix interface as a function of fission density (in units of 10^21 fissions per cm³ of UMo) for the six plate‑location combinations: V6022M‑A, V6022M‑B, V6022M‑C, R3R108‑A, R3R108‑B, R3R108‑C. Each series must span from zero fission density up to the end‑of‑life value for that case, with at least 50 data points per series.

## Assets
All material properties, irradiation correlations, plate fabrication data, and hydrostatic stress CSVs are provided in this document or as accompanying bundled data files. No external resources are needed.

## Workflow steps

### Step 1: Load input data and implement correlations
- Role: process
- Action: Read the bundled material properties, irradiation correlations, plate irradiation data, and the hydrostatic stress (σh) CSV files. Implement the given swelling, IL growth, creep, and thermal‑expansion correlations as functions.
- Evidence: `/app/outputs/data_loaded.txt`

### Step 2: Compute radial stress at IL/Al interface and export CSV
- Role: scored (load-bearing)
- Action: Implement the analytical stress model (closed‑form expressions for σr, σθ, bubble pressure, interfacial stress iteration) using the loaded data. For each plate (V6022M, R3R108) and location (A,B,C), integrate over irradiation time/fission density and output the radial stress at the IL/Al interface. Write the result to ilal_stress_vs_fd.csv.
- Output file: `/app/outputs/ilal_stress_vs_fd.csv`
- Format: csv
- Contract: CSV with columns: plate (string), location (string, one of A/B/C), fission_density_1e21 (float), radial_stress_MPa (float). Must contain exactly six series covering the fission density range from 0 to the end-of-life value for each case, with at least 50 points per series.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ilal_stress_vs_fd.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ilal_stress_vs_fd.csv
- path: `/app/outputs/ilal_stress_vs_fd.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Radial stress at the IL/Al interface as a function of fission density for the six plate/location cases. Checker compares end-of-life values and a sign-transition trend to hidden paper gold with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `plate`, `location`, `fission_density_1e21`, `radial_stress_MPa`
  - `units`:
    - `fission_density_1e21`: 10^21 fissions/cm³
    - `radial_stress_MPa`: MPa

Notes: Only the CSV is scored. The process step evidence (data_loaded.txt) is not verified. The checker uses hidden gold end-of-life values and a trend check for V6022M location B stress sign transition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ilal_stress_vs_fd.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "plate",
          "location",
          "fission_density_1e21",
          "radial_stress_MPa"
        ],
        "units": {
          "fission_density_1e21": "10^21 fissions/cm³",
          "radial_stress_MPa": "MPa"
        }
      },
      "description": "Radial stress at the IL/Al interface as a function of fission density for the six plate/location cases. Checker compares end-of-life values and a sign-transition trend to hidden paper gold with tolerance."
    }
  ],
  "notes": "Only the CSV is scored. The process step evidence (data_loaded.txt) is not verified. The checker uses hidden gold end-of-life values and a trend check for V6022M location B stress sign transition."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares the radial stress values in your CSV against reference results (derived from the original study) at the end‑of‑life fission densities for each of the six cases. For one specific case, the verifier also checks a qualitative trend in the stress‑vs‑fission‑density curve. The reward is weighted: the majority of credit comes from accurate stress values, and a smaller portion from the correct trend. The exact tolerances, weights, and reference values are hidden. Only artifacts produced by a correctly executed workflow can earn credit; reporting the target numbers without running the model is detected and will receive no reward.
