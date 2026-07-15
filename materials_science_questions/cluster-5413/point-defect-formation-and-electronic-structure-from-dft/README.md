# Point Defect Formation and Electronic Structure from DFT

This workflow family contains computational studies that model point defects in crystalline materials using first-principles density functional theory (DFT). The common goal is to compute defect formation energies, thermodynamic transition levels, and defect-induced electronic states, often linking the results to experimental observables such as electrical conductivity, optical transitions, or catalytic activity.

## Common Computational Pattern

All papers follow a core computational pipeline:

1. **Bulk Structure Optimization**  
   Obtain relaxed lattice parameters and atomic positions of the pristine host crystal using periodic DFT. This step often validates the chosen exchange-correlation functional (e.g., PBE-GGA, PBEsol, HSE06) against experimental lattice constants or bulk moduli.

2. **Supercell Construction**  
   Build a supercell of the host (e.g., 2×2×2, 3×3×3) to accommodate point defects with minimal periodic-image interaction. Neutral and/or charged defects are introduced by removing/adding atoms, with charge compensated either by a jellium background or by explicit counter-defects (e.g., oxygen vacancies as compensation for aliovalent dopants).

3. **Defect Formation Energy Calculation**  
   The formation energy $E_f(D^q)$ of defect $D$ in charge state $q$ is computed as:
   $$E_f(D^q) = E_{\mathrm{tot}}(D^q) - E_{\mathrm{tot}}(\mathrm{host}) - \sum_i n_i \mu_i + q(\epsilon_V + \Delta\epsilon_F) + E_{\mathrm{corr}}$$
   where $\mu_i$ are chemical potentials linked to synthesis conditions (e.g., oxygen partial pressure), $\epsilon_V$ is the valence-band maximum, $\Delta\epsilon_F$ is the Fermi level relative to $\epsilon_V$, and $E_{\mathrm{corr}}$ accounts for finite-size effects. Formation energies are often plotted as a function of $\Delta\epsilon_F$ to construct transition-level diagrams.

4. **Electronic Structure Analysis**  
   - **Density of states (DOS)** – atom-projected and orbital-resolved to identify defect-induced gap states, their character (e.g., O $2p$, metal $d$), and spin polarization.  
   - **Charge density differences** – visualize electron/hole localization around defects (polarons, charge transfer).  
   - **Band structures** – assess whether defect states cause effective doping, pinning, or mid-gap traps.

5. **Migration and Mobility (when applicable)**  
   - **Nudged elastic band (NEB)** or climbing-image NEB for diffusion barriers.  
   - **Temperature-accelerated dynamics (TAD)** and ab initio molecular dynamics (AIMD) for sampling migration paths and estimating hop rates.
   - **Formation energies of vacancy–impurity complexes** to evaluate thermodynamic driving forces for clustering.

## Required Resources

Based on the context provided across papers, typical assets include:

- **Crystal structures** – Experimental lattice parameters from literature (often from ICSD) to initialize DFT models.
- **DFT software** – VASP, CASTEP, Quantum ESPRESSO, or similar plane-wave pseudopotential codes.
- **Pseudopotentials/functionals** – PAW/USPP, PBE, PBEsol, HSE06, sometimes with on-site Hubbard U corrections.
- **Chemical potential references** – Total energies of elemental phases, oxides, or molecular $\mathrm{O}_2/\mathrm{H}_2$ to define growth conditions (O‑rich vs. O‑poor).
- **Experimental validation data** – Reported values of formation enthalpies, activation energies, band gaps, hyperfine couplings, EPR g‑factors, electrical measurements, or STEM image databases for comparison.

## Verification Style

This family uses **numeric** verification. Computed defect formation energies, migration barriers, transition levels, and band gaps are compared directly with experimental measurements (e.g., activation enthalpy from conductivity data, optical band gaps, deep-level transient spectroscopy, or chemical shifts in NMR). Tolerances are typically defined in the specific paper’s `instruction.md`, often requiring agreement within a few tenths of an eV or better. The verification may involve one‑to‑one numeric comparisons or statistical trends across a series of defects/dopants.

## Task Structure

Each paper in the family resides in a directory `paper‑<id>/`. The public entry point is `instruction.md` (not `TASK.md`), which describes the computational objectives and any precise verification thresholds for that paper. Resources required by a given paper are listed in its instruction; the solving agent should obtain them before execution.
