# Thermodynamic Modeling of Ordered Intermetallic Phases Workflow Family

## Overview
This workflow family contains reproduction tasks for 84 papers that compute phase diagrams, thermodynamic properties, and order–disorder transitions of ordered intermetallic phases. The common goal is to model configurational free energy as a function of order parameters, parametrize interatomic interactions, and solve equilibrium conditions to determine phase boundaries, long‑range order, and defect thermodynamics. All work is computational (dry‑lab) and validated numerically.

## Common Computational Pattern
The papers follow a shared methodological pipeline:
1. **Define a configurational model** – Express the free energy (or internal energy plus entropy) of the lattice system in terms of site occupation variables, order parameters, or cluster probabilities. Examples include the Bragg‑Williams‑Gorsky approximation, Ising‑model pair energies, Fermionic site occupancies, and cluster variation method (CVM) formulations (e.g., tetrahedron approximation for fcc lattices).
2. **Parametrize interatomic interactions** – Obtain the energetic parameters that enter the free energy. Sources are:
   - First‑principles electronic structure calculations (tight‑binding TB‑LMTO, EMTO‑CPA, screened generalized perturbation method SGPM) to extract effective pair and multisite interactions.
   - Empirical pair potentials, canonical Slater‑Koster d‑band models, or experimental thermochemical data (enthalpies of formation).
3. **Solve equilibrium conditions** – Minimize the free energy (or grand potential) with respect to the order parameters/cluster variables. Numerical methods include:
   - Direct minimization with constraints (e.g., Lagrange multipliers).
   - Natural iteration method (NIM) for CVM cluster probabilities.
   - Algebraic solution of closed‑form equilibrium relations (Fermi‑Dirac occupations, analytic tangent constructions).
4. **Extract phase‑equilibrium information** – From the minimized free energy surfaces, determine phase stability, transition temperatures, composition‑dependent order parameters, phase boundaries, and tie lines.

## Typical Resources/Data
- **Electronic structure inputs**: tight‑binding parameters (canonical ddσ, ddπ), density‑functional supercell energies used in Connolly‑Williams inversions.
- **Interaction models**: pair‑interaction parameters (W, V), multi‑atom parameters (α, β), chemical interchange energies.
- **Statistical mechanics approximations**: CVM tetrahedron/quadruplet formulae, Bragg‑Williams‑Gorsky entropy expressions, Fermi‑Dirac statistics.
- **Thermochemical data**: standard enthalpies of formation, lattice stability parameters, activity coefficients when fitting to experiment.
- **Numerical solvers**: NIM iterators for CVM, linear equation solvers for rate‑constant inversions, phase‑field 1D boundary‑value integrators.

## Verification Style
All tasks in this family are verified **numerically**. Computed phase boundaries, order‑parameter curves, transition temperatures, and thermodynamic potentials are compared with reference calculations or experimental data. A successful reproduction requires **residuals below 1×10⁻⁴** (or equivalent tolerance) for key quantities such as free energies, equilibrium compositions, or phase‑transformation temperatures.

## Task Structure
Each paper is stored in a separate `paper-*` subdirectory. Inside each subdirectory, the public entry point for the Harbor task is **`instruction.md`**. This file describes the specific reproduction target, input parameters, and any required resources. No other files (such as TASK.md) need to be created; the solving agent will obtain additional assets from the provided metadata.
