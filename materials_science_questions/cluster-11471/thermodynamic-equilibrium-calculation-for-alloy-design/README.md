# Thermodynamic equilibrium calculation for alloy design

## Overview
This workflow family covers the use of **CALPHAD software** (e.g., Thermo‑Calc) to compute equilibrium phase diagrams, phase fractions, and phase compositions as functions of temperature for multicomponent alloys. The results support alloy composition design, interpretation of experimental transformation temperatures, and explanation of microstructural features such as phase partitioning and stability.

**Domain(s):** 材料科学, 热力学, 合金设计, 计算相图  
**Workflow scale:** 183 total, 124 papers  
**Lab type:** dry (no new experiments required — only computational work)  
**Verification:** numeric (results compared against existing experimental measurements within tolerance)

## Common computational pattern
The core computational approach across the family is **thermodynamic equilibrium calculation** using the CALPHAD (CALculation of PHAse Diagrams) methodology. Typical steps include:
1. **Model input:** Define alloy composition (mass percent or mole fraction of all elements) and temperature range.
2. **Phase diagram & equilibrium computation:** Use Gibbs free energy models from critically assessed databases (e.g., TCFE3, TCFE8) to calculate:
   - Equilibrium phase assemblages at each temperature.
   - Phase fractions, compositions, and transformation temperatures (e.g., liquidus, solidus, solvus).
   - Driving forces for phase transformations and chemical potentials.
3. **Non‑equilibrium extensions:** In many papers, the basic equilibrium calculation is extended via **Scheil–Gulliver solidification** (no solid diffusion) or **Lever‑Rule** (full equilibrium) simulations, or by solving constrained carbon equilibria (CCE) for quenching and partitioning processes.
4. **Post‑processing:** Derived numerical quantities (phase fractions, transition temperatures, carbon potentials, etc.) are compared against experimental data from literature or from the paper’s own measurements to validate the thermodynamic description and guide alloy design.

Papers in the family may also incorporate:
- **Gibbs–Thomson effect** corrections for curved interfaces.
- **Segregation energy** and **solute drag** models within moving interfaces.
- **Composite models** linking phase fractions and Hollomon‑type flow laws to predict mechanical properties.

The common thread is that **accurate phase‑equilibrium information, computed with commercial or custom CALPHAD‑based programs, forms the foundation for all subsequent analysis.**

## Data / Model / Tool categories
Based on the provided papers, the following resources are typically used; the exact combination depends on the specific task.

**Software / Computational tools:**
- Thermo‑Calc (including the Thermo‑Calc Matlab Toolbox)
- MatLab (for custom scripting and coupling)
- DICTRA (for diffusion‑controlled moving‑boundary simulations)

**Databases:**
- TCFE3 (Fe‑base alloys)
- TCFE8 (updated Fe‑base alloys)
- CALPHAD databases for specific subsystems (e.g., Fe‑Cr‑V‑C, Fe‑Cr‑Ni‑Mo, etc.)

**Model parameters:**
- Gibbs‑energy expressions from sublattice models.
- Redlich–Kister interaction parameters.
- Diffusion coefficients (carbon, substitutional elements).
- Interfacial energies, molar volumes, magnetic contributions.

**Note:** The concrete set of resources needed for reproducing a paper’s results is listed in each `paper‑*` subdirectory’s `instruction.md`. The solving agent is expected to obtain the required software/databases; no extra bundling is required.

## Verification style
This family is verified **numerically**: calculated outputs—such as phase fractions, transformation temperatures, eutectic compositions, carbon potentials, or predicted PAR‑equilibrium compositions—are compared against existing experimental measurements (from published literature or the same study). The agreement is judged by whether the numerical difference falls within an acceptable tolerance. The verify note states: “通过计算输出的相分数、转变温度等数值与已有实验测量值进行容差比对来判定是否成功” (success is determined by comparing computed phase fractions, transformation temperatures, etc. with existing experimental data within a tolerance).

## Task structure
Each paper in the family is represented as a standalone **Harbor task** in a directory `paper‑{paper_id}`. The public interface is **`instruction.md`**, which contains the task description, required inputs, and expected outputs. The solving agent reads that file and produces the deliverable, typically a set of computed phase diagrams or numerical results.
