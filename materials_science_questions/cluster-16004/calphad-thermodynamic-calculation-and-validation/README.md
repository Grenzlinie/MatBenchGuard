# CALPHAD Thermodynamic Calculation and Validation

This workflow family encompasses computational studies that apply the CALPHAD (CALculation of PHAse Diagrams) method to model and predict phase equilibria, thermochemical properties, diffusion kinetics, and related phenomena in materials systems, with a strong emphasis on validation against experimental data. The papers span 162 tasks, primarily focusing on metallic alloys, intermetallics, and ceramic systems, notably Ni‑based superalloys, Cu‑Ni, Fe‑Ni, Al‑Si, and Ni‑In systems.

## Core Computational Pattern

The common workflow across this family follows a systematic thermodynamic assessment and validation cycle:

1. **Data collection**: Gather experimental phase equilibria data (e.g., solidus/liquidus temperatures, phase boundaries, invariant reactions), thermochemical properties (enthalpies of mixing, activities, heat capacities), diffusion coefficients, and optionally first‑principles (DFT) calculations for phases or compounds.

2. **Model selection**: Choose appropriate thermodynamic models for each phase:
   - Substitutional regular solution (liquid, fcc, etc.) with Redlich‑Kister polynomials for excess Gibbs energy.
   - Sublattice models using the Compound Energy Formalism (CEF) for intermetallic compounds and ordered phases (e.g., B2, L1₂, B8₂).
   - Stoichiometric compounds modeled as line compounds.

3. **Parameter optimization**: Use an optimization procedure (often with software like Thermo‑Calc’s PARROT module, ChemSage, or custom codes) to determine model parameters (enthalpy, entropy, interaction parameters) that best reproduce the selected reference data. The objective is to minimize the deviation between calculated and experimental values, typically using least‑squares.

4. **Phase diagram and property calculation**: With the optimized thermodynamic description, compute:
   - Phase diagrams (binary/ternary isothermal sections, liquidus projections).
   - Phase fractions and compositions as function of temperature.
   - Thermochemical properties (activity, chemical potential, enthalpy of mixing, heat capacity).
   - Diffusion‑controlled properties via coupling with atomic mobility databases (e.g., DICTRA) to simulate concentration profiles and interdiffusion coefficients.
   - Additional properties such as surface tension (via Butler’s equation) and magnetic contributions to Gibbs energy.

5. **Validation**: Compare computed results against experimental data not used in the optimization, using absolute difference, relative error, or visual inspection of phase boundaries. The acceptable tolerance is often defined per task (e.g., within experimental uncertainty). The workflow family’s default verification is **numeric** – the agent compares computed numbers (phase fraction, composition, temperature, energy) with experimental values using appropriate error metrics.

## Typical Resources

Each task directory (`paper-*`) contains an `instruction.md` specifying the exact required resources (experimental datasets, model parameters, computational tools). They commonly draw from:

- **Datasets**: Phase diagram data (from compilations like ASM, Landolt‑Börnstein), thermochemical tables (e.g., Hultgren, SGTE), diffusion couple composition profiles, activity measurements from Knudsen cell mass spectrometry, first‑principles formation enthalpies.
- **Models and Formalisms**: Redlich‑Kister polynomials, sublattice and CEF models, Butler equation for surface tension, magnetic contribution models, Arrhenius diffusion kinetics.
- **Software / Tools**: Thermo‑Calc, DICTRA, ChemSage, ATAT (Alloy Theoretic Automated Toolkit) for cluster expansion and Monte Carlo, custom codes for autonomic phase diagram calculation, and standard Python/Matlab for fitting and plotting.

**Note**: The solving agent is responsible for acquiring these resources as part of the task reproduction. The `instruction.md` only describes the task; it does not bundle the data or software.

## Verification Style

All tasks in this family are **dry‑lab**: they do not require new experimental work. Verification relies on existing experimental data provided with the task. The verification process involves:

- Computing the required output (e.g., a phase diagram line, a set of compositions, a diffusion profile).
- Comparing the computed values to given experimental references using a predefined metric (e.g., absolute error of phase boundary coordinates, relative error of activity values, RMS deviation of concentration profiles).
- Ensuring all model parameters are consistent and the thermodynamic description reproduces the claimed phase equilibria within stated tolerances.

This mirrors the family’s `verify_type: numeric` and the verification note in `tag_meta`.

## Directory Structure

Within the family cluster, each paper is placed in a separate subdirectory named `paper-<paper_id>`. The entry point for reproduction is the `instruction.md` file inside that directory, which details the specific goal, required data/model references, expected outputs, and verification criteria. There is no other public file.
