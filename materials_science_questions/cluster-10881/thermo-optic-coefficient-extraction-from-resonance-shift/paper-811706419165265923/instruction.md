# Steady-State Temperature Field in an End-Pumped Cylindrical Laser Crystal with Convective End-Face Conditions

## Problem background
Diode-pumped solid-state lasers suffer from thermal effects because a fraction of the absorbed pump energy is converted to heat, causing a non-uniform temperature rise inside the laser crystal. Accurately modeling the steady-state temperature field is critical for predicting thermal lensing, distortion, and laser stability. This work addresses the case of an end-pumped cylindrical Nd:YAG crystal where, in addition to side-face cooling, the crystal ends exchange heat with the ambient air through convection. The task is to compute the temperature field for several heat-transfer strengths and to quantify how the temperature and the resulting thermal distortion at the pumped face depend on the end-face cooling condition.

## Mathematical model

The crystal is a cylinder of radius \(R = 3\ \mathrm{mm}\) and length \(L = 2\ \mathrm{mm}\). The side face is held at a constant temperature (relative temperature zero), while the two end faces satisfy convective (mixed) boundary conditions with a heat-transfer parameter \(\sigma\).

The pump light has a Gaussian radial profile with waist \(\omega = 0.32\ \mathrm{mm}\) and power \(P = 20\ \mathrm{W}\). The absorption coefficient is \(\beta = 20.7\ \mathrm{cm}^{-1} = 2.07\ \mathrm{mm}^{-1}\). The fraction of absorbed power converted to heat is  
\[
\eta = 1 - \frac{\lambda_\mathrm{p}}{\lambda_\mathrm{L}} = 1 - \frac{808}{1064} \approx 0.2406 .
\]

The volumetric heat source is  
\[
q_v(r,z) = \eta\beta I(r,z) = \eta\beta I_0 \,\mathrm{e}^{-2r^2/\omega^2}\,\mathrm{e}^{-\beta z},
\qquad
I_0 = \frac{2P}{\pi\omega^2} .
\]

The steady-state temperature field \(u(r,z)\) (relative to the side-face temperature) satisfies Poisson’s equation  
\[
\frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{\partial^2 u}{\partial z^2} = -\frac{q_v}{\lambda},
\]
with boundary conditions  
\[
u|_{r=R}=0,\qquad u|_{r=0} < \infty,
\]  
\[
\left(-\frac{\partial u}{\partial z} + \sigma u\right)\!\Big|_{z=0} = \sigma T,
\qquad
\left(\frac{\partial u}{\partial z} + \sigma u\right)\!\Big|_{z=L} = \sigma T,
\]
where the relative ambient air temperature is \(T = 5\,^\circ\mathrm{C}\) and the thermal conductivity is \(\lambda = 13\ \mathrm{W\,m^{-1}\,K^{-1}}\) (when using mm as the length unit, convert to \(\lambda = 0.013\ \mathrm{W\,mm^{-1}\,K^{-1}}\)).

## Analytical series solution

The solution is expressed as a Fourier‑Bessel series involving the zeroth‑order Bessel function \(J_0\). Let \(\alpha_n\) (\(n=1,2,\dots\)) be the positive zeros of \(J_0\), i.e. \(J_0(\alpha_n)=0\). The derivatives at the zeros are \(J_0'(\alpha_n) = -J_1(\alpha_n)\), where \(J_1\) is the first‑order Bessel function.

The temperature field is  
\[
\begin{aligned}
u(r,z) = \sum_{n=1}^{\infty}
\Bigl[ & A_n \cosh\!\Bigl(\frac{\alpha_n z}{R}\Bigr)
      + B_n \sinh\!\Bigl(\frac{\alpha_n z}{R}\Bigr)
      + \phi_n(z) \Bigr] J_0\!\Bigl(\frac{\alpha_n r}{R}\Bigr),
\tag{9}
\end{aligned}
\]
where the functions \(\phi_n(z)\) and \(f_n(z)\) are defined below, and the coefficients \(A_n, B_n\) are determined by the end‑face boundary conditions.

**Radial‑modal forcing function \(f_n(z)\)**  

The heat source is expanded in the Bessel basis. For the Gaussian pump,  
\[
f_n(z) = C_n\,\mathrm{e}^{-\beta z},
\qquad
C_n = \frac{2\,\eta\beta I_0}{\lambda R^2\,\bigl[J_0'(\alpha_n)\bigr]^2}\,
      \int_0^R r\,J_0\!\Bigl(\frac{\alpha_n r}{R}\Bigr)\,\mathrm{e}^{-2r^2/\omega^2}\,\mathrm{d}r .
\tag{13}
\]

**Axial particular solution \(\phi_n(z)\)**  

\[
\phi_n(z) = \frac{R}{\alpha_n}
           \int_0^z \sinh\!\Bigl(\frac{\alpha_n z}{R} - \frac{\alpha_n \tau}{R}\Bigr)\, f_n(\tau)\,\mathrm{d}\tau .
\tag{12}
\]

For the exponential form of \(f_n\) the integral can be evaluated analytically, but numerical integration using quadrature is also acceptable. The derivative \(\phi'_n(z)\) appears in the boundary conditions and can be obtained directly by differentiating (12):
\[
\phi'_n(z) = \int_0^z \cosh\!\Bigl(\frac{\alpha_n z}{R} - \frac{\alpha_n \tau}{R}\Bigr)\, f_n(\tau)\,\mathrm{d}\tau .
\]

**Coefficients \(A_n\) and \(B_n\)**  

With the auxiliary quantities  
\[
\begin{aligned}
P_n &= \sigma\,\phi'_n(L)
      - \frac{2\sigma\alpha_n T}{R\,\alpha_n\,J_0'(\alpha_n)}\,
        \sinh\!\Bigl(\frac{\alpha_n L}{R}\Bigr)
      - \frac{2\sigma^2 T}{\alpha_n\,J_0'(\alpha_n)}\,
        \cosh\!\Bigl(\frac{\alpha_n L}{R}\Bigr)
      + \frac{2\sigma^2 T}{\alpha_n\,J_0'(\alpha_n)} ,
\tag{14}
\end{aligned}
\]

\[
\begin{aligned}
Q_n &= \frac{2\sigma^2 T}{\alpha_n\,J_0'(\alpha_n)}\,
      \sinh\!\Bigl(\frac{\alpha_n L}{R}\Bigr)
      + \frac{2\sigma\alpha_n T}{R\,\alpha_n\,J_0'(\alpha_n)}\,
        \cosh\!\Bigl(\frac{\alpha_n L}{R}\Bigr)
      + \frac{2\sigma\alpha_n T}{R\,\alpha_n\,J_0'(\alpha_n)} ,
\tag{15}
\end{aligned}
\]

the constants are given by  
\[
A_n = \frac{
        -\sigma\phi'_n(0)\,\sinh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        -\frac{\alpha_n}{R}\phi'_n(0)\,\cosh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        +\frac{\alpha_n}{R}\phi'_n(L) + P_n
      }{
        \sigma^2\sinh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        + \bigl(\frac{\alpha_n}{R}\bigr)^2\sinh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        + 2\sigma\frac{\alpha_n}{R}\cosh\!\bigl(\frac{\alpha_n L}{R}\bigr)
      },
\tag{10}
\]

\[
B_n = \frac{
        \frac{\alpha_n}{R}\phi'_n(0)\,\sinh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        + \sigma\phi'_n(0)\,\cosh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        + \sigma^2\phi_n(L) + Q_n
      }{
        \sigma^2\sinh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        + \bigl(\frac{\alpha_n}{R}\bigr)^2\sinh\!\bigl(\frac{\alpha_n L}{R}\bigr)
        + 2\sigma\frac{\alpha_n}{R}\cosh\!\bigl(\frac{\alpha_n L}{R}\bigr)
      } .
\tag{11}
\]

All quantities are evaluated using the chosen length unit (mm is convenient, with \(\lambda\) converted to \(0.013\ \mathrm{W\,mm^{-1}\,K^{-1}}\)).

**Series truncation**  
Truncate the sum after the first 25–50 terms (zeros of \(J_0\) easily obtained from `scipy.special.jn_zeros`). The exact number may be increased until the maximum temperature changes by less than 0.1 °C.

## Reproduction target
Compute the steady-state temperature field \(u(r,z)\) inside the Nd:YAG crystal for three end‑face heat‑transfer conditions:  
\(\sigma = 0\) (adiabatic ends),  
\(\sigma = 0.6\) (finite convective cooling),  
and a large \(\sigma\) (e.g. 100) that approximates the limit \(\sigma\to\infty\) (isothermal ends at the ambient temperature).

Evaluate the field on a regular Cartesian grid covering \(r \in [0, 3]~\mathrm{mm}\) and \(z \in [0, 2]~\mathrm{mm}\) using at least \(100\times100\) points for each \(\sigma\) value. Write the grid points to `temperature_field.csv` with columns `sigma`, `r_mm`, `z_mm`, `u_degC`.

From this output the hidden verifier will extract the maximum temperature and will compute the maximum thermal distortion at the pumped end, checking how both quantities change with \(\sigma\).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute temperature field on a grid
- Role: scored (load-bearing)
- Action: Implement the analytical eigenfunction expansion described above to compute the steady temperature field \(u(r,z)\) inside the cylindrical laser crystal for the three values of \(\sigma\) (0, 0.6, and a large value ≈ 100) on a regular Cartesian grid covering \(r\) in \([0,3]\) mm and \(z\) in \([0,2]\) mm (minimum \(100\times100\) points per \(\sigma\)).  Use the crystal and pump parameters given in the mathematical model.  Write the computed grid points to `temperature_field.csv`.
- Output file: `/app/outputs/temperature_field.csv`
- Format: csv
- Contract: CSV with header: `sigma` (dimensionless), `r_mm` (float, radial position 0–3 mm), `z_mm` (float, axial position 0–2 mm), `u_degC` (float, computed relative temperature). One row per grid point for each sigma value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_field.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_field.csv
- path: `/app/outputs/temperature_field.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Gridded temperature field \(u(r,z)\) for three heat‑transfer conditions. The checker will extract the maximum temperature and compute the thermal distortion \(l_z(r) = \alpha \int_0^L u(r,z)\,\mathrm{d}z\) (with thermal expansion coefficient \(\alpha = 8.2\times10^{-5}\,\mathrm{K}^{-1}\), length \(L=2\,\mathrm{mm}\)), compare the maxima to hidden gold values, and verify the trend that both maxima decrease as \(\sigma\) increases.
- schema:
  - `type`: table
  - `required_columns`: `sigma`, `r_mm`, `z_mm`, `u_degC`
  - `units`:
    - `r_mm`: mm
    - `z_mm`: mm
    - `u_degC`: °C

Notes: The checker recomputes derived quantities from the raw temperature field; no separate thermal distortion output is required from the agent. The hidden gold values are the paper’s reported maximum temperatures and thermal distortions for each \(\sigma\) value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma",
          "r_mm",
          "z_mm",
          "u_degC"
        ],
        "units": {
          "r_mm": "mm",
          "z_mm": "mm",
          "u_degC": "°C"
        }
      },
      "description": "Gridded temperature field u(r,z) for three heat-transfer conditions. The checker will extract the maximum temperature and compute thermal distortion l_z(r) = alpha * integral_0^L u(r,z) dz, compare the maxima to hidden gold, and verify the trend that both maxima decrease as sigma increases."
    }
  ],
  "notes": "The checker recomputes derived quantities from the raw temperature field; no separate thermal distortion output is required from the agent. The hidden gold values are the paper's reported maximum temperatures and thermal distortions for each sigma value."
}
```

## How you are scored
A hidden verifier reads your `temperature_field.csv` and groups the data by \(\sigma\). For each \(\sigma\), it locates the maximum temperature, and numerically integrates the temperature field along \(z\) for every radial point to obtain the thermal distortion profile \(l_z(r) = \alpha \int_0^L u(r,z)\,\mathrm{d}z\), from which the maximum distortion at the pumped end (\(z=0\)) is taken. These derived quantities are compared against hidden reference values using tolerances that account for numerical discretization and series truncation. The verifier also confirms that both the maximum temperature and the maximum thermal distortion decrease as \(\sigma\) increases. The stage score is the primary component of the final reward; a solution that implements the correct physics and yields results consistent with the reference within the allowed tolerances receives full credit, and a better-than-reference result is never penalized.