# Magnetic Anisotropy Energy Computation

## Overview
This workflow family contains 62 computational tasks that compute **magnetic anisotropy energy (MAE)** and **easy-axis orientation** for a wide variety of magnetic systems including bulk materials, thin films, multilayers, monolayers, clusters, and surface adatoms. The core approach is to evaluate total energy differences for different magnetization directions using spin‑orbit coupling (SOC)‑inclusive electronic structure calculations. The MAE is the primary numeric output, often complemented by orbital moments and electronic structure analysis.

## Common Computational Pattern
Across all papers in this family, the workflow follows these steps:
1. **Structural Definition** – The atomic structure (bulk, slab, monolayer, cluster) is set up, often using relaxed or experimental lattice parameters. Internal coordinates may be optimized in a scalar‑relativistic DFT run.
2. **Scalar‑Relativistic DFT** – Spin‑polarized density functional theory (DFT) is performed without SOC to obtain a self‑consistent charge density and wavefunctions. Common choices are GGA (PBE), GGA+U, or LDA, implemented in plane‑wave (VASP) or full‑potential (FLAPW/WIEN2k) codes.
3. **SOC Treatment** – Spin‑orbit coupling is introduced either self‑consistently or via a second‑variation/force‑theorem step. Typical methods include second‑variation FLAPW, perturbative SOC, or fully relativistic Dirac‑based approaches.
4. **Energy for Different Magnetization Directions** – Total energies are computed for at least two orientation directions (e.g., in‑plane vs. out‑of‑plane). The MAE is taken as the difference, e.g., `MAE = E[100] – E[001]` for tetragonal systems, or using appropriate directional pairs.
5. **Post‑processing** – The easy axis is identified from the lowest energy direction. Additional analyses include k‑resolved MAE, orbital moment decomposition, perturbation theory rationalisation, and projection of density of states. This step often traces the origin of the anisotropy back to specific orbital hybridisations or SOC matrix elements.
6. **Verification** – Numerical convergence with respect to k‑point density, basis size, and SOC parameters is always checked. The computed MAE is compared against experimental data (magnetometry, MOKE, FMR) or previous theoretical values. Sensitivity to exchange‑correlation functionals (e.g., GGA vs LDA, HSE06) and effective U parameters is tested to ensure qualitative robustness.

## Key Data and Resources
- **Structures** – Experimental lattice constants (from XRD), relaxed geometries, crystallographic data.
- **DFT Software** – VASP, WIEN2k, FLAPW, OOMMF (for micromagnetic simulations using DFT‑derived parameters).
- **Exchange‑Correlation** – PBE‑GGA, GGA+U (Dudarev formulation), LDA, HSE06.
- **Pseudopotentials/Basis** – PAW potentials, LAPW basis, plane‑wave cutoffs.
- **SOC Implementations** – Second‑variational FLAPW, magnetic force theorem (sum of occupied band eigenvalues), full Dirac relativistic equation.

## Verification Style
All tasks are **numeric verification**: MAE magnitudes are compared with experimental or literature values within a tolerance. Convergence tests ensure that MAE changes by less than a threshold upon increasing k‑points, basis quality, or SOC treatment. Multiple functionals are often benchmarked to confirm the identified easy axis. The verification note for the family states: *“通过计算得到的MAE数值与文献或实验值进行容差对齐，同时进行收敛性测试和泛函比较。”* (MAE values are tolerance‑aligned with literature/experiment, with convergence tests and functional comparisons.)

## Family Structure
Each paper is a self‑contained Harbor task located in `paper‑<paper_id>/`. The public instruction file is `instruction.md`, which specifies the MAE computation objectives for that particular material or system. Tasks can be executed independently, and together they form a comprehensive benchmark of MAE prediction methods.
