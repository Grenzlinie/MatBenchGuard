# DFT adsorption energetics on metal surfaces

This workflow family encompasses density functional theory (DFT) computations of adsorption energies, geometries, and electronic properties for atomic and molecular adsorbates on metal and related surfaces. The studies range from simple physisorption to complex catalytic steady-state kinetics, but all share a core DFT-driven analysis of adsorption.

## Common computational pattern

The typical workflow proceeds through the following stages:

1. **System construction** – Build a surface slab model (often using a periodic supercell with vacuum), select high‑symmetry adsorption sites (top, bridge, hollow, etc.), and place the adsorbate in initial configurations.
2. **Parameter selection** – Choose an exchange‑correlation functional (commonly GGA‑PBE), pseudopotentials (PAW or ultrasoft), and convergence parameters (energy cutoff, k‑point mesh, force tolerance).
3. **Geometry optimization** – Relax the atomic positions of the adsorbate and the surface layers (or top layers) to find the minimum‑energy configuration.
4. **Energy calculation** – Compute the binding/adsorption energy using the standard formula  
   `E_bind = E_system – (E_surface + E_adsorbate)`  
   where negative values indicate exothermic (favorable) adsorption.
5. **Analysis** – Extract structural parameters (bond lengths, distances, surface distortions), electronic properties (charge transfer via Bader or Mulliken analysis, density of states, band structure), and in some cases magnetic moments or reaction barriers.

Spin‑polarized calculations are used when magnetic effects are relevant. When the workflow is extended to kinetics, transition‑state theory (TST) converts DFT barriers into rate constants, and kinetic Monte Carlo (kMC) may be employed to simulate steady‑state turnover frequencies.

## Resources

Each task relies on computational tools and input files that are specified in the `instruction.md` file of the corresponding `paper-*` directory. Common resources include:

- **DFT codes** – e.g., VASP, Quantum ESPRESSO, or other plane‑wave/FP‑LAPW implementations.
- **Pseudopotentials** – PAW or ultrasoft pseudopotentials appropriate for the chosen functional.
- **Structural files** – Atomic coordinates of the clean surface and the adsorbate.

The solving agent obtains the exact resource list from the task’s `instruction.md`; no additional bundling is required.

## Verification style

Verification is **numeric**: computed adsorption energies, bond lengths, and other measurable quantities are compared against reference values (literature, experiments, or higher‑level calculations) within predefined tolerances. Typical tolerances are `±0.1 eV` for energies and `±0.02 Å` for bond lengths. This ensures that the reproduction of the original results meets the expected accuracy. For kinetic workflows, detailed‑balance checks or consistency with equilibrium thermodynamics serve as additional verification.

## Task structure

Each `paper-*` subdirectory is a standalone **Harbor task** containing:

- `instruction.md` – The public task description with step‑by‑step instructions, required software, input files, and verification criteria.
- (Other files as needed for the specific reproduction, such as scripts, input templates, or reference data.)

The tasks are independent; a user can run any single task after setting up the specified computational environment.
