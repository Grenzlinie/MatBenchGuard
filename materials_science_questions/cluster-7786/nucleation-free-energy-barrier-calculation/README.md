# Nucleation Free-Energy Barrier Calculation

## Overview

This workflow family focuses on computing the free-energy barrier for crystal nucleation. The core task is to **calculate the critical free energy (ΔG\*) or nucleation rate as a function of system conditions**—such as temperature, supersaturation, composition, or undercooling—using classical nucleation theory (CNT) or its extensions, given thermodynamic and kinetic parameters of the system.

The family is **dry‑lab** (numerical) and the verification style is **numeric**, evaluating the accuracy of computed barriers/rates against experimental or simulation data via metrics like relative error or R².

## Main Computational Pattern

Across the family, the common computational pattern consists of these steps:

1. **Define the free energy of nucleus formation**, typically as a function of size (radius or number of monomers) and sometimes shape or composition:
   ```
   ΔG(n) = –n·Δμ + γ·A(n)   [CNT form]
   ```
   where:
   - `Δμ` is the chemical potential difference per growth unit (driving force), expressed via temperature, supersaturation, or composition.
   - `γ` is the interfacial free energy density (possibly temperature- or orientation-dependent) and `A(n)` the surface area.

2. **Extend or modify** the basic expression to account for additional physics:
   - Elastic self‑energy of the embryo (e.g., for martensitic transformations)
   - Effect of parent‑phase free‑energy change (modified CNT)
   - Enthalpy‑saving terms for glass transition or ultra‑stable glass formation
   - Composition fluctuations, multicomponent effects, or composition‑dependent surface tension
   - Contact‑angle corrections for heterogeneous nucleation (spherical‑cap geometry)

3. **Find the critical nucleus size** `n*` (or `r*`) by setting `d(ΔG)/dn = 0` and compute the critical barrier `ΔG* = ΔG(n*)`.

4. **Connect barrier to observables** via kinetic relations:
   - Steady‑state nucleation rate: `J = K·exp(–ΔG*/k_B T)` with a pre‑exponential factor `K` that often involves a diffusion activation energy (viscosity‑ or diffusion‑controlled attachment rate).
   - Metastable lifetime or onset temperature via Poisson statistics and time‑scale crossing.

5. **Numerically evaluate** the barrier or derived quantity and **compare with reference data** (experimental nucleation rates, undercoolings, temperatures of first nucleation) using quantitative metrics (R², relative error, etc.).

## Typical Inputs and Resources

The specific parameters and models used in a task come from the literature resources bundled with each paper. Common categories of required inputs include:

- **Thermodynamic quantities:**
  - Melting enthalpy / entropy, bulk free‑energy difference models (e.g., Hoffmann model, Turnbull approximation)
  - Chemical potentials, activity coefficients, solubility, supersaturation ratio
- **Interfacial properties:**
  - Surface energy density (solid‑liquid, solid‑vapour, etc.) and its temperature dependence
  - Wetting angles, broken‑bond parameters, structural ratios for interfacial coarse‑graining
- **Kinetic coefficients:**
  - Diffusion coefficients, viscosity models (Vogel‑Fulcher, power‑law, Arrhenius forms)
  - Monomer attachment attempt frequencies
- **Geometric and lattice information:**
  - Molar volume, atomic spacing, lattice type, crystallographic orientation, nucleus shape assumptions

When applying a modified theory, the paper’s instruction.md will specify the required model equations and their parameter values (taken from the paper or its supplementary data).

## Verification

Verification is **numeric**. The computed nucleation barrier, critical size, or derived temperature is compared against experimentally measured or simulation‑determined values. Typical metrics include:
- Relative error between predicted and observed critical undercooling or nucleation rate.
- Coefficient of determination (R²) when fitting a series of data points.
- Linear regression slopes on transformed variables (`ln(J)` vs. `1/ΔT²`, etc.) to extract interfacial energies.

The provided reasoning chains often show how these comparisons are performed and what level of agreement is considered acceptable.

## Task Structure

Each `paper-*` subdirectory is a standalone **Harbor** task. The public entry point is `instruction.md` (not `TASK.md`), which details:
- The specific model equations and parameters used for that paper.
- The computational recipe (steps) to obtain the predicted barrier or rate.
- The reference data and the expected verification procedure.

The README you are reading describes the common family; individual paper instructions provide the concrete instantiation.

## Notes

- This workflow family does not require wet‑lab experimentation; all computations are based on pre‑existing thermodynamic and kinetic data.
- The solver should **not** invent resources; rely on the provided paper metadata, reasoning chains, and the instruction.md in each paper subdirectory.
- Many tasks involve extensions to classical theory (parent‑phase free energy change, elastic energy, 2D ribbon nuclei, etc.) — always defer to the specific instructions for the exact formulation to use.
