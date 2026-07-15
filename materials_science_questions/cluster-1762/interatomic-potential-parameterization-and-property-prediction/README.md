# Interatomic Potential Parameterization and Property Prediction

## Common Computational Pattern

This workflow family encompasses a recurring sequence of computational steps found across a wide range of solid-state physics and materials science papers. The core pattern is:

1. **Select an interatomic potential functional form** – Choose an explicit analytic expression that represents the total energy or pair interactions of a material. Common choices include Born–Mayer / Buckingham pair potentials, shell models for ionic polarizability, Tersoff or Stillinger–Weber many‑body potentials, tight‑binding second‑moment approximation (TB‑SMA), embedded‑atom method (EAM), Fisher–Sinclair (FSM), bond‑order potentials (e.g., Tersoff‑like with environmental angular dependence), and local pseudopotentials (Ashcroft empty‑core, Heine–Abarenkov, model pseudopotentials). Some papers incorporate Coulomb, van der Waals ($r^{-6}$, $r^{-8}$), three‑body bond‑bending terms, or exchange‑charge corrections (Lundqvist).

2. **Determine potential parameters by fitting** – The free parameters in the chosen functional form are adjusted to reproduce a set of target data. Targets most frequently include experimental or first‑principles values of equilibrium lattice constants, cohesive energies (or atomization energies), elastic moduli (bulk modulus, $C_{11}, C_{12}, C_{44}$), and vibrational frequencies (phonon frequencies, Raman modes). In pseudopotential‑based studies the parameter (often an empty‑core radius) is fixed by the zero‑pressure equilibrium condition. When binary or mixed systems are involved, cross‑interaction parameters are obtained from geometric mixing rules (e.g., arithmetic/geometric means) or by fitting to compound properties.

3. **Compute material properties with the calibrated potential** – Once the potential is fully parameterized, it is used to calculate a range of material properties that were not part of the fitting set. Typical outputs include: second‑order elastic constants (with pressure or temperature dependence), lattice dynamics (phonon dispersion curves, vibrational density of states, Raman/infrared mode assignments), cohesive energies of different structures (polymorphs, phases under pressure), defect formation and migration energies (vacancies, interstitials, antisites) and relating to diffusion coefficients or ionic conductivity, thermodynamic quantities (free energy, enthalpy, entropy) via variational methods or equations of state, and mechanical stability criteria (Cauchy discrepancy, elastic instability).

4. **Verify against experiment** – The computed results are compared with available experimental reference data. For elastic constants, phonon frequencies, and cohesive energies, tables of calculated vs. experimental values are often presented, with average percentage deviations reported. For phase transitions, the crossing of Gibbs free energy curves or the softening of phonon modes is checked against measured transition pressures. The verification type is predominantly **numeric**; the primary metric is the quantitative match between calculated and measured numbers (relative error, absolute deviation, or qualitative agreement in trends).

## Typical Model Types and Fitting Targets

From the papers included in this family, the following categories appear repeatedly:

- **Ionic interactions**: Buckingham pair potential ($A\exp(-r/\rho)-C/r^6$) with formal or partial charges, often combined with a shell model for oxygen polarizability (O²⁻ shell, cation shells). Targets: lattice constants, dielectric constants, elastic moduli.
- **Many‑body metal potentials**: TB‑SMA, EAM, Finnis–Sinclair, bond‑order potentials. Targets: cohesive energy, lattice parameter, elastic constants (including Cauchy discrepancy), vacancy formation energy, and in some cases metastable phase energies.
- **Pseudopotentials**: Ashcroft empty‑core, local Heine‑Abarenkov‑type, model pseudopotentials with adjustable core radii. Targets: lattice spacing (via zero‑pressure condition), and sometimes elastic moduli or phonon frequencies; often used in perturbation theory to compute total binding energies, bulk moduli, or alloy thermodynamics.
- **Three‑body angular terms**: Stillinger–Weber, Tersoff‑like bond‑order, or explicit $\cos\theta$‑dependent terms to enforce tetrahedral or directional bonding. Targets: bond lengths, bond angles, elastic constants, and relative stabilities of different coordination environments.

## Verification Style

The papers uniformly apply **numeric** verification: after fitting the potential, the model's predictions for one or more quantitative properties (elastic constants, phonon frequencies, cohesive energy, activation energies, etc.) are compared with experimental measurements. The comparison is typically presented in tables giving calculated vs. experimental values and the percentage deviation or absolute error. Agreement within a few percent is often accepted as validation. In few cases, the Cauchy discrepancy or the ratio of activation energies is used as an internal consistency check. This workflow family therefore does not rely on qualitative visual comparison alone but on rigorous numeric benchmarking against reference data.

## Per‑Paper Tasks

Each `paper‑*` subdirectory in this family is a standalone Harbor task. The public interface is a single `instruction.md` file. The solving agent is expected to reproduce the computational workflow described in that instruction using the given model parameters, compute the required properties, and present results in the specified format – for instance, a table of elastic constants or a list of formation energies – exactly as instructed. The resources (potential parameters, crystal structures, experimental targets) are provided within the task, and no external inventing is required.
