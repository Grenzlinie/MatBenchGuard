# Electronic Structure Bonding Analysis

Characterize chemical bonding (covalent, ionic, metallic contributions) in crystalline solids using first‑principles electronic structure calculations and post‑processing analyses such as density of states, population analysis, and charge density maps.

## Common computational pattern

1. **Obtain a structural model** (from experiment or prior optimization) and prepare input files.
2. **Perform a first‑principles electronic‑structure calculation** – typically density‑functional theory (GGA, LDA, or hybrid functionals) with plane‑wave/pseudopotential (CASTEP, VASP), full‑potential LAPW (WIEN2k), or LMTO codes.
3. **Extract electronic descriptors**:
   - total and partial (orbital‑resolved) density of states (DOS/PDOS)
   - band structures along high‑symmetry paths
   - real‑space charge density / charge‑density differences
   - population analyses (Mulliken, Bader, bond orders)
   - crystal‑orbital Hamilton populations (COHP) where available
4. **Interpret bonding character** using the above descriptors to classify bonds as covalent, ionic, metallic, or mixed. Often quantitative numbers (e.g., bond orders, charge transfer, ICOHP values) are reported and compared across materials or dopants.

## Typical tools and resources

- **DFT packages:** VASP, CASTEP, WIEN2k, Quantum ESPRESSO, LMTO codes.
- **Analysis tools:** COHP/LOBSTER for bond‑resolved energy contributions, Bader analysis for charge partitioning, Mulliken population analysis, and standard post‑processing scripts.
- **Structural databases / reference data:** ICSD, experimental lattice parameters, bulk moduli, band gaps.

## Verification style

This family uses **numeric** verification: computed quantities such as equilibrium lattice constants, bond lengths, bulk moduli, band gaps, formation energies, magnetic moments, and work functions are compared against experimental values or established reference calculations. Typical tolerances are a few percent for structural parameters and 0.1–0.2 eV for energy differences.

## Output organization

Each `paper-*` subdirectory is a standalone **Harbor task**. The public entry point is `instruction.md` (not `TASK.md`). It contains the full problem statement, required input files (crystal structure, computation settings), and the expected numeric outputs for verification.
