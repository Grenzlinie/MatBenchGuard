# First-principles point defect characterization

## Overview
This workflow family covers density functional theory (DFT) studies of point defects in crystalline solids. It includes vacancies, interstitials, antisites, impurity substitutions, and complexes. The primary goal is to quantify thermodynamic stability (formation energies), electronic properties (charge-state transition levels, defect-induced gap states), and spectroscopic signatures (optical transitions, hyperfine interactions, vibrational modes) using supercell models.

## Common computational pattern
The standard workflow proceeds through these stages:

1. **Host bulk modeling** – Compute equilibrium lattice parameters, band structure, and density of states (DOS) of the pristine crystal using a suitable exchange-correlation functional (often hybrid functionals such as HSE06, PBE0, or setups tuned to reproduce experimental band gaps). Spin‑orbit coupling and magnetic spin polarization are included when needed.

2. **Supercell construction** – Build a large supercell (typically 64–576 atoms) to isolate the defect and minimize periodic image interactions. Supercell size and shape are chosen to accommodate defect relaxation and lattice distortions (e.g., octahedral tilts, Jahn‑Teller distortions).

3. **Defect introduction and relaxation** – Insert the defect (vacancy, substitution, interstitial, antisite, or complex) and relax atomic coordinates. Multiple charge states ( q = 0, ±1, ±2, …) are relaxed separately. Symmetry‑breaking reconstructions, off‑center relaxations, and polaronic localization are explicitly explored.

4. **Total‑energy calculations** – Compute the total energy of each defect‑containing supercell, usually with the same functional and convergence criteria as the host. For charged defects, charge‑correction schemes (jellium background, potential alignment, band‑edge charge‑density corrections) are applied to account for finite‑size errors.

5. **Formation energy analysis** – Evaluate defect formation energies as a function of the Fermi level and atomic chemical potentials:
   ```
   Ef[X^q] = Etot[X^q] – Etot[host] – Σ n_i μ_i + q (EF + EVBM) + E_corr
   ```
   Thermodynamic charge‑state transition levels ε(q/q′) are obtained from the Fermi‑level positions where formation energies of different charge states cross.

6. **Electronic structure characterization** – Calculate band structures, total and projected densities of states (PDOS), and real‑space charge densities. Identify localized defect states, their orbital character, and their magnetic moments. Deep, shallow, and resonant levels are classified.

7. **Derived properties** (if required by the specific task) – Compute optical transition energies (zero‑phonon lines, Stokes shifts), vibrational signatures, migration barriers (NEB), carrier capture cross‑sections, and Debye–Waller factors using DFT‑based methods such as time‑dependent DFT, constrained DFT, or the nudged‑elastic‑band method.

## Typical verification
- **Numeric verification** – Reported defect formation energies, transition levels, or band gaps are compared to experimental measurements (e.g., deep‑level transient spectroscopy, photoluminescence, Hall effect). Agreement is judged using a typical energy tolerance of **≤ 0.1 eV**.
- **Structural verification** – Computed bond lengths, coordination numbers, and vibration frequencies are checked against experimental values (XRD, EXAFS, Raman, IR) when available.
- **Spectroscopic verification** – Calculated zero‑phonon lines, hyperfine constants, and optical absorption/emission energies are matched against experimental photoluminescence, ODMR, EPR, or UPS/XPS data.

## Tools and resources referenced in the family
- **DFT codes**: VASP, CASTEP, CP2K, QSTEM (for STEM simulations), LAMMPS (for MD with empirical potentials).
- **Functionals**: PBE, PBEsol, HSE06, PBE0, BB1K; often with tuned Hartree–Fock exchange fractions.
- **Post‑processing**: Formation‑energy plotters, NEB path samplers, Wigner–Seitz defect analysis, Gaussian‑fitting of diffusion profiles.
- **Model size**: Supercells from ~100 to ~2000 atoms; embedded‑cluster QM/MM models up to ~20 000 atoms.

## Family scope
- **Number of papers**: 138
- **Total size**: 203 tasks
- **Domains**: Condensed‑matter physics, materials science, computational chemistry
- **Lab type**: Dry (fully computational)
