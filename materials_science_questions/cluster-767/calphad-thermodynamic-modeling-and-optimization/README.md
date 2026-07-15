# CALPHAD Thermodynamic Modeling and Optimization

This workflow family centers on the **CALPHAD (CALculation of PHAse Diagrams) method**: the construction, optimization, and validation of thermodynamic models for phases in multicomponent systems to predict phase equilibria and thermodynamic properties. The tasks are entirely computational (dry lab), requiring no additional wet‑lab experiments; all necessary data can be sourced from publicly available literature or existing databases. Verification is strictly **numeric**, typically comparing computed phase boundaries, invariant temperatures, enthalpies, or activities against experimental measurements using tolerance‑aligned metrics (e.g., RMSD, deviation within experimental uncertainty).

## Family Overview
- **Domains**: Materials Science, Thermodynamics, Phase Diagrams, Computational Materials Science  
- **Lab Type**: Dry (all work is computational or based on existing experimental data)  
- **Verification Type**: Numeric (quantitative comparison of computed values with experimental references)  
- **Verification Note**: “通过比较计算与实验的相边界温度、热力学性质等数值指标（如RMSD）进行容差对齐验证。”  
- **Lab‑Type Reason**: The workflow relies on already published experimental phase diagram data and thermochemical measurements; model parameter optimization and phase equilibrium calculations can be reproduced without any new experimental work.

## Common Computational Pattern
Every task within this family follows the same core CALPHAD workflow:

1. **Model Construction**  
   Select appropriate thermodynamic descriptions for each phase (liquid, solid solutions, stoichiometric compounds). Typical choices include:
   - Substitutional regular or subregular solution models (Redlich–Kister polynomials)
   - Sublattice models (Compound Energy Formalism, two‑sublattice models)
   - Modified Quasichemical Model (MQM) for oxide/short‑range ordering systems
   - Ordering models (Bragg–Williams) and magnetic contributions (Inden–Hillert formalism)
   Define the Gibbs energy of each phase as a function of composition, temperature, and pressure.

2. **Parameter Assessment / Optimization**  
   Use experimental data (phase diagram invariant points, liquidus/solidus lines, calorimetric enthalpies of mixing, activities, solubility limits) to calibrate the model parameters. This is performed via **least‑squares optimization** (e.g., Thermo‑Calc/PARROT) or through custom iterative fitting procedures. The objective is to minimize the deviation between calculated and measured values.

3. **Phase Equilibrium Calculation**  
   Compute stable phase assemblages and phase boundaries by **Gibbs energy minimization** or by solving the conditions of equal chemical potentials. Tools used include Thermo‑Calc, Selektor‑A (GEM), and custom codes like TEREQUIL. The output includes phase diagrams, tie‑lines, invariant equilibria, and thermodynamic property curves.

4. **Validation**  
   The computed results are compared against held‑out or literature experimental data. Agreement is judged by numerical tolerances (e.g., temperature differences < a few K, enthalpies within a few kJ/mol) or by visual overlay of calculated and experimental phase boundaries.

## Key Resources
Based on the papers in this family, the following categories of resources appear:

### Experimental Datasets (input for assessment)
- Phase diagram data: liquidus/solidus temperatures, invariant reactions, measured by DTA, thermal analysis, quenching methods, EPMA, XRD.
- Thermochemical data: enthalpy of mixing (calorimetric), partial enthalpies, vapor pressure activity measurements.
- Crystallographic data: lattice constants, site occupancies (to define sublattice models).
- Ab initio data: total‑energy differences for unstable end‑members (e.g., sigma‑phase lattice stabilities).
- Solubility data: liquid solubility of compounds in solvents for LPE process design.

### Thermodynamic Models
- Substitutional solution: Redlich–Kister polynomials ($L$‑parameters)
- Sublattice models: two‑sublattice (e.g., $(A)_a (B,B^{\prime})_b$), Compound Energy Formalism
- Modified Quasichemical Model (MQM) for short‑range ordering in liquids/oxides
- Bragg–Williams ordering model with magnetic and ordering excess contributions
- Ideal solid solutions / ideal mixing assumptions
- Isotropic interaction potentials (Ashcroft pseudopotential, Double Yukawa) for liquid metals (non‑CALPHAD but related)

### Software & Tools
- **Thermo‑Calc / PARROT**: least‑squares parameter optimization and phase diagram calculation
- **Selektor‑A (GEM)**: Gibbs energy minimization for solid‑aqueous‑gas equilibria
- **TEREQUIL**: derivative‑free algorithm for calculating coexisting compositions in ternary systems
- **Custom codes**: self‑consistent variational parameter determination for pure metal melts, lattice stability calculations, perturbation theory for fluid mixtures
- **General programming**: C, Fortran for thermodynamic equation‑of‑state evaluation and custom solvers

## Verification Style
All tasks in this family verify their outputs **numerically**. The computed phase diagrams, invariant temperatures, enthalpies, and activities are compared against **experimental reference data** using quantitative metrics. Common examples:
- The mean absolute difference between calculated and measured liquidus/eutectic temperatures (K)
- RMSD for enthalpy of mixing curves
- Relative deviation in solute solubility limits
- Agreement of computed phase boundaries within reported experimental uncertainties (e.g., ±2 °C, ±0.001 at.%)
- Visual checks supported by numerical tolerance (e.g., “two successive iterations must not differ by more than 0.1%”)

The verification is thus purely **numeric** and does not rely on synthetic benchmarks or qualitative evaluation.

## Repository Structure
Each subdirectory named `paper-*` corresponds to an independent Harbor task. The only public entry point is `instruction.md` within that subdirectory. There is no bundling of multiple tasks; each paper is reproduced and verified as a standalone unit.
