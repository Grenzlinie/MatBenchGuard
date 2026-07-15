# Thermodynamic Constitutive Modeling from Dissipation Inequality

## Workflow Overview

This workflow family comprises tasks that **derive thermodynamically consistent constitutive models** for materials by:
1.  Postulating a free energy function dependent on state variables (strain, temperature, internal variables).
2.  Applying the first and second laws of thermodynamics (typically the Clausius‑Duhem inequality) to obtain stress, entropy, and evolution equations.
3.  Ensuring that the resulting model satisfies the dissipation inequality, i.e., the total dissipation is non‑negative.

The derived constitutive relations are then implemented numerically and verified against **numeric indicators** (e.g., residual dissipation rate, frame indifference, energy stability, mesh‑size independence).

## Common Computational Pattern

- **State Variables:** Elastic strain, temperature, and a set of internal (microstructural) variables (e.g., damage parameters, plastic strain, phase fractions, back‑stress).
- **Free Energy Formulation:** A Helmholtz free energy function is split into mechanical, chemical, thermal, and, if needed, gradient or interface energy contributions.
- **Thermodynamic Constraints:** The Clausius‑Duhem inequality is used to derive:
  - Reversible constitutive equations for stress and entropy.
  - Residual dissipation inequality that must be satisfied by the evolution laws.
- **Evolution Laws:** Based on the dissipation inequality, associative or non‑associative flow rules, hardening/softening laws, and thermal coupling terms are formulated. Internal variables evolve via rate equations that guarantee non‑negative dissipation.
- **Numerical Implementation:** The derived model is discretized within a finite‑element or finite‑volume framework (e.g., ABAQUS, custom FEM, acoustic Riemann solvers) and solved for boundary‑value problems.
- **Verification:** Numerical simulations check:
  - Non‑negativity of the residual dissipation rate.
  - Material frame indifference (objectivity) of the stress response.
  - Incremental energy stability (e.g., a priori stability estimates, time‑step bounds).
  - Mesh‑size independence for softening models (via crack‑band or gradient regularization).

## Typical Verification Style

The family is verified **numerically** (dry lab). No actual experiments are required. Verification includes:
- Computing and checking the sign of the dissipation rate.
- Comparing numerical predictions (stress‑strain curves, force histories, yield surfaces) with analytical solutions or published benchmarks.
- For fracture/damage models: ensuring that global energy dissipation is mesh‑independent.
- For coupled thermo‑mechanical models: verifying that the total entropy production is non‑negative and that the staggered algorithm inherits the continuum a priori energy estimate.

## Resources and Tools

These are the categories of resources that appear in the provided papers:
- **Constitutive Models:** Continuum damage, viscoelasticity, plasticity (isotropic, kinematic, distortional hardening), gradient plasticity, shape memory alloys, TRIP steels, magneto‑rheological elastomers.
- **Numerical Solvers:** Finite element solvers (e.g., ABAQUS), in‑house finite element codes, finite volume solvers with Riemann problem‑based contact dynamics.
- **Benchmarks:** Analytical solutions (e.g., uniaxial extension of a two‑beam composite, thick‑walled tube inflation), closed‑form thermodynamic relations, and small‑strain linearizations for validation.

*Note:* Each `paper-*` subdirectory is a standalone Harbor task. The task description and required inputs are given in `instruction.md` within that subdirectory. This README only describes the common pattern shared across the family.
