# Steady‑state thermoelectric module performance evaluation

## Overview
This workflow family models thermoelectric (TE) modules – both generators (TEGs) and coolers (TECs) – under steady‑state conditions. It accounts for temperature‑dependent material properties (Seebeck coefficient, electrical resistivity, thermal conductivity), thermal contact resistances, and external heat exchanger interactions. By solving the coupled, nonlinear heat‑balance and electrical‑circuit equations, the workflow evaluates performance metrics (output power, efficiency, coefficient of performance) and supports parametric sweeps over geometric and operating variables for design and optimization.

## Core computational pattern
1. **Setup** – define module geometry (leg length, cross‑section, number of couples, segment lengths for multi‑stage/segmented designs) and obtain temperature‑dependent thermoelectric properties (e.g., from datasheet polynomial fits, two‑parabolic‑band models, or literature data).
2. **Balance equations** – For each junction (hot side, cold side, segment interfaces) write the energy balance:
   - Peltier heat: \( \alpha I T \)
   - Joule heating (half attributed to each adjacent control volume): \( \tfrac12 I^2 R \)
   - Fourier conduction: \( K \Delta T \) or more complex thermal resistance networks when external heat exchangers, air gaps, or fin convection are included.
   - Additional effects: Thomson heat (when temperature‑dependent properties are integrated), thermal radiation between surfaces, and convective coupling to fluids.
   - The electrical circuit is closed with \( I = \frac{\alpha_{\text{eff}} (T_{\text{hot}} - T_{\text{cold}})}{R_{\text{int}} + R_L} \) (matched load optional).
3. **Iterative solution** – Because material parameters depend on temperature and the heat flows depend on current, the system is nonlinear. Solvers employed across papers include fixed‑point iteration, Newton‑Raphson, MATLAB/Excel‑Solver, COMSOL coupled field solvers (fluid‑thermal‑electric), and ANSYS FLUENT with customized UDFs. The iteration continues until junction temperatures, current, and sometimes fluid fields converge within a prescribed tolerance (e.g., \(10^{-6}\) relative change, or energy balance error < 1%).
4. **Performance output** – Once converged, calculate:
   - Output power \( P_{\text{out}} = I^2 R_L \)
   - Heat flows \( Q_h, Q_c \)
   - Efficiency \( \eta = P_{\text{out}} / Q_h \) (TEG) or COP \( = Q_c / P_{\text{in}} \) (TEC)
   - Effective figure of merit \( ZT_{\text{eff}} \) or average \( ZT \) over the operating temperature range.
5. **Parametric sweeps / optimization** – The workflow family typically loops over design variables such as leg height, fill factor, number of leg pairs, segment lengths, load resistance, current, heat flux, or heat transfer coefficients to map performance landscapes. Some papers embed direct‑search optimization (Powell method) or genetic algorithms; others use dimensional analysis (Buckingham Pi) to create compact design correlations.

## Key inputs and resources
- **Material properties** – Temperature‑dependent Seebeck coefficient, electrical conductivity, thermal conductivity. Obtained from:
  - Manufacturer datasheets (e.g., Bi₂Te₃, PbTe, skutterudite)
  - Physical models (two‑parabolic‑band model for Bi₂Te₃, or parametrized fits based on experimental data)
  - Literature data (e.g., PbTe–SrTe with 2% or 4% SrTe, CsSnI₃ for energy filtering layers).
- **Geometry** – Leg dimensions (cross‑section, height, fill factor), number of p‑n couples, segment lengths for segmented or two‑stage designs, area ratios for asymmetrical legs, and external heat exchanger geometries (fin dimensions, microchannel sizes).
- **Thermal interfaces** – Heat transfer coefficients at hot and cold sides, radiation emissivities, thermal paste/contact resistances, air‑gap conduction/convection treatments (Rayleigh number regimes).
- **Tools** – Simulation platforms include MATLAB (custom scripts), COMSOL Multiphysics (coupled multiphysics solver), ANSYS Fluent (finite‑volume TE module), Microsoft Excel with Solver add‑in, and Aspen Plus for fluid mixture properties in cryogenic applications.

## Verification style
Verification is **numerical** and relies on the following checks:
- **Energy balance closure** – The sum of computed heat flows should match the input/removed powers within a tight tolerance (e.g., ~1% error).
- **Solution convergence** – Iterative temperature and current updates are monitored until the relative change drops below a threshold (e.g., \(10^{-6}\)).
- **Comparison to ideal/analytical benchmarks** – For special cases (constant properties, simple geometries) the model output is compared with known formulas (e.g., ideal TEG efficiency, Dunkle’s relation for evaporation) or with published numerical/experimental data (e.g., Chen et al. 2005, manufacturer’s recommended operating points).
- **Sensitivity & parameter studies** – Systematic sweeps over design variables check that trends match physical expectations (e.g., efficiency increases with \( ZT \), output power peaks at matched load).

## Example applications in the family
- **Segmented TEG optimization** – Using Improved Powell algorithm with a discrete numerical model to find optimal leg‑segment ratios and cross‑sectional areas for maximum specific power or efficiency.
- **Hybrid solar–thermoelectric systems** – Coupling PV panels or solar absorbers with TEGs or TECs; solving the coupled energy balances and electrical matching to obtain global efficiency.
- **Waste‑heat recovery** – Integrating TEGs into exhaust streams (ICE, SOFC) with finned or microchannel heat exchangers; full 3‑D fluid‑thermal‑electric coupling to capture parasitic heating.
- **Cooling with TECs** – Selecting commercial TECs from multiple manufacturers, predicting their steady‑state I‑V and COP using parameterized resistance models, and validating against vendor curves.
- **Nanostructured micro‑TEGs** – FEM simulation of PbTe–SrTe elements with temperature‑dependent properties, evaluating efficiency inflections due to Thomson effect and load resistance.
- **Critical concentration ratio for solar TEGs** – Dimensional analysis of the CCR and nonlinear regression over Latin‑hypercube sampled data to build a compact prediction equation.

## Directory structure conventions
Each implemented task resides in a `paper-*` subdirectory with a public `instruction.md` file defining specific inputs, outputs, solver settings, and validation targets for that particular paper’s model or experiment.
