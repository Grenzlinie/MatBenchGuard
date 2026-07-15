# Classical Nucleation Theory Critical Size Calculation

This workflow family computes the critical nucleus (or bubble) size, the number of molecules involved, and the Gibbs free energy barrier for nucleation using the classical nucleation theory (capillarity approximation). Given thermodynamic parameters – temperature, supersaturation, surface tension, molar volume – the workflow yields the critical radius, the activation energy barrier, and often the nucleation rate or equilibrium size. It applies to both condensation from the vapor/liquid phase and bubble formation in supersaturated solid solutions, across multiple domains including materials science, physical chemistry, and astrophysics.

## Common Computational Pattern

All workflows in this family share a core numerical procedure:

1. **Input parameters**: Gather material-specific constants and state variables – surface energy \(\sigma\), molar volume \(V_m\), temperature \(T\), supersaturation \(\Delta\mu\) (or equivalent concentration/pressure difference), and, where needed, the gas/solute concentration and possible mechanical constraints (e.g., ambient pressure).

2. **Critical size calculation**: Apply classical nucleation theory formulas to compute:
   - Critical radius \(r^* = \frac{2\sigma V_m}{\Delta\mu}\) (or modified forms for bubble nucleation where the Laplace pressure modifies the chemical potential).
   - Critical Gibbs free energy barrier \(\Delta G^* = \frac{16\pi}{3} \frac{\sigma^3}{(\Delta g_v)^2}\), with \(\Delta g_v\) the bulk driving force per volume.
   - Critical number of molecules \(n^* = \frac{32\pi}{3} \frac{\sigma^3 V_m^2}{(\Delta\mu)^3}\) (for spherical nuclei).

3. **Nucleation rate and growth**: The steady‑state nucleation rate \(J = J_0 \exp(-\Delta G^*/k_BT)\) is sometimes calculated. Some implementations proceed further to compute equilibrium size distributions or temporal evolution (e.g., growth of bubbles after exceeding a threshold radius).

4. **Validation**: The computed critical or equilibrium sizes are compared against experimental measurements (e.g., bubble radii in aluminum from literature, dust condensation temperatures in stellar winds) using a tolerance‑based numeric check. The verification is strictly numerical: predicted radii must agree within a specified tolerance with observed values.

## Workflow Variants

Two distinct implementations are part of this family:

- **Bubble nucleation in solids** (paper `320829950636589056`): Models the formation of hydrogen bubbles in aluminum. Requires material constants (surface energy inside a grain, solution energy of hydrogen, saturation concentration), the global hydrogen content, and the bubble density. Computes a threshold radius \(r_b^*\) and equilibrium radius for bubbles; validates against experimental values from Talbot (1975).

- **SiO nucleation for silicate dust in stellar outflows** (paper `867758850516713839`): Re‑calibrates SiO vapour pressure data and determines nucleation rates under circumstellar conditions. Uses the new vapour‑pressure relation to compute critical cluster sizes and condensation temperatures for AGB star winds; validates against infrared‑derived dust condensation temperatures.

## Required Resources

No fixed external datasets or pre‑trained models are supplied in advance. The solving agent must obtain the necessary input parameters from the literature cited in each workflow (e.g., Table 1 in the first paper, experimentally measured vapour pressures in the second). Scientific computing tools (Python, Fortran, or any numerical environment capable of solving transcendental equations and evaluating exponential functions) suffice to implement the formulas.

## Verification

Verification is numeric: the computed critical radius, critical molecule count, or condensation temperature is compared against a reference value (from experiments or observations) with a predefined relative or absolute tolerance. If the discrepancy is within tolerance, the workflow is considered correct. The check is performed by the solving agent as part of the Harbor task.

## Subdirectory Structure

Each workflow variant resides in its own `paper‑<paper_id>` subdirectory. The public interface for a task is the file `instruction.md`, which contains the precise computational steps, required parameters, expected outputs, and verification criteria. For example:

- `paper‑320829950636589056/instruction.md` – Classical nucleation theory for hydrogen bubbles in aluminum.
- `paper‑867758850516713839/instruction.md` – Re‑calibrated SiO nucleation for dust condensation.

No other files are required to be shared between tasks; each is self‑contained.
