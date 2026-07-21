# Equilibrium Sizes of Aqueous H₂SO₄ Solution Droplets

## Problem background
Atmospheric aerosol droplets containing sulphuric acid grow by water vapour uptake. The equilibrium size of a solution droplet depends on the ambient relative humidity (RH), the amount of dissolved acid, and the curvature effect (Kelvin effect). For a given dry H₂SO₄ particle, the equilibrium radius changes with humidity according to a modified Kelvin relation that accounts for concentration‑dependent surface tension and density. This task requires you to compute equilibrium radii for several dry sizes and relative humidities, reproducing the growth of aqueous H₂SO₄ droplets.

## Governing equation and physical constants
The water vapour equilibrium over a binary H₂SO₄–H₂O droplet is described by the modified Kelvin equation:

\[
\ln\!\left(\frac{S_w}{a_w}\right) =
\frac{2\,M_w\,\sigma}{R\,T\,\rho}\,
\frac{1}{r}
\Bigl[\,1 + \frac{X}{\rho}\frac{\mathrm{d}\rho}{\mathrm{d}X}
      - \frac{3}{2}\,\frac{X}{\sigma}\frac{\mathrm{d}\sigma}{\mathrm{d}X}\Bigr]
\]

where:
- \(S_w = \text{RH}/100\) – water saturation ratio (dimensionless)
- \(a_w\) – water activity in the solution (from the data file)
- \(M_w = 18.015\ \text{g mol}^{-1}\) – molar mass of water
- \(R = 8.314\) – gas constant (use as given; CGS‑compatible numerical value)
- \(T = 298.15\ \text{K}\) – temperature (25 °C)
- \(\sigma\) – surface tension of the solution (\(\text{dyn cm}^{-1}\))
- \(\rho\) – solution density (\(\text{g cm}^{-3}\))
- \(X\) – mass percent of H₂SO₄ in the droplet
- \(r\) – droplet radius (cm)

**Mass conservation**: For a dry particle of radius \(r_0\) (µm), the acid mass is

\[
m_{\text{acid}} = \frac{4}{3}\pi r_{\text{dry}}^3 \,\rho_{\text{pure}},
\qquad r_{\text{dry}} = r_0 \times 10^{-4}\ \text{cm},\;
\rho_{\text{pure}} = 1.84\ \text{g cm}^{-3}.
\]

The total droplet mass when the acid mass fraction is \(X\) % is
\[
m_{\text{total}} = m_{\text{acid}} \times \frac{100}{X}.
\]
The droplet volume is \(V = m_{\text{total}}/\rho\), so the equilibrium radius is
\[
r = \left(\frac{3V}{4\pi}\right)^{1/3}\ \text{cm},
\]
which is then converted to µm (\(1\ \text{cm} = 10^4\ \mu\text{m}\)).

The derivatives \(\mathrm{d}\rho/\mathrm{d}X\) and \(\mathrm{d}\sigma/\mathrm{d}X\) are obtained from the supplied data file; **attention** – the tabulated values are scaled:
- \(\mathrm{d}\rho/\mathrm{d}X\) in the file is multiplied by \(10^3\); divide by \(1000\) to obtain \(\text{g cm}^{-3}\) per mass%.
- \(\mathrm{d}\sigma/\mathrm{d}X\) in the file is multiplied by \(10^2\); divide by \(100\) to obtain \(\text{dyn cm}^{-1}\) per mass%.

## Thermodynamic data
The file **`/app/assets/h2so4_properties.csv`** (bundled with the task) contains the properties of aqueous H₂SO₄ solutions as functions of mass percent \(X\), as provided in the data file:

| Column | Description | Unit |
|--------|-------------|------|
| X      | Mass % H₂SO₄ | – |
| rho    | Density \(\rho\) | g cm⁻³ |
| drho_dx | \(\mathrm{d}\rho/\mathrm{d}X\) (scaled ×10³) | g cm⁻³ per mass% (after division) |
| sigma  | Surface tension \(\sigma\) | dyn cm⁻¹ |
| dsigma_dx | \(\mathrm{d}\sigma/\mathrm{d}X\) (scaled ×10²) | dyn cm⁻¹ per mass% (after division) |
| a_w    | Water activity \(a_w\) | – |
| a_o    | Acid activity \(a_o\) | – |

You **must** read this file and use linear interpolation between the given \(X\) values to obtain properties at arbitrary compositions. The data cover the range \(X \in [0.5,\,85]\).

## Required outputs
For **every** combination of dry radius and relative humidity listed below, compute the equilibrium droplet radius \(r\) (in µm). Write the results to `/app/outputs/growth_curve.csv`.

### Dry radii \(r_0\) (µm)
0.001, 0.005, 0.05, 0.1, 0.5

### Relative humidities (%)
0, 10, 30, 50, 70, 80, 90, 100, 101, 110

**Special case:** when \(\text{RH}=0\), no water condenses; set `eq_radius_um = dry_radius_um` directly.

### Output file format
- Path: `/app/outputs/growth_curve.csv`
- Format: CSV with header
- Columns:
  - `dry_radius_um` (float, µm)
  - `rh_pct` (int, %)
  - `eq_radius_um` (float, µm)
- One row per (dry_radius_um, rh_pct) pair (50 rows total).

## Solution method (summary)
1. For RH = 0, output the dry radius.
2. Otherwise, with \(S_w = \text{RH}/100\), search for the mass fraction \(X \in [0.5,\,85]\) that satisfies the modified Kelvin equation. A robust approach is to scan \(X\) in fine steps (e.g. 0.1 %) and find the value that minimizes the absolute difference between the left‑ and right‑hand sides.
3. At each trial \(X\):
   - Obtain \(a_w\), \(\rho\), \(\sigma\), \(\mathrm{d}\rho/\mathrm{d}X\), \(\mathrm{d}\sigma/\mathrm{d}X\) from the interpolated tabular data.
   - Compute the droplet radius \(r\) from the mass conservation relations.
   - Evaluate the equation residual.
4. When the best \(X\) is found, compute the corresponding equilibrium radius and convert it to µm.

**Note:** The checker will independently solve the same equation using the same data file and identical constants, and compare your `eq_radius_um` values against its own recomputed values with a relative tolerance of 5 %.

## Assets
- `/app/assets/h2so4_properties.csv` – thermodynamic properties of H₂SO₄ solutions.

## Output files
- `/app/outputs/growth_curve.csv`