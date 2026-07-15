# Spin State Determination of Transition Metal Ions

## Overview

This workflow family addresses the determination of spin states (low‑spin, high‑spin, intermediate‑spin) of transition metal ions—with a particular emphasis on cobalt (Co)—embedded in crystalline solids. The approach integrates orbital‑resolved electronic structure calculations or crystal‑field analyses with experimental spectroscopic or magnetometric data to assign and validate the spin state. The family covers dry‑lab computations that produce testable magnetic or spectroscopic predictions, which are then compared with experimental results (SQUID magnetometry, X‑ray absorption spectroscopy, X‑ray magnetic circular dichroism, neutron scattering, etc.) to confirm the spin‑state assignment.

## Common Computational Pattern

The general workflow across the included papers can be described as follows:

1. **Obtain a geometric model** of the transition metal ion’s local environment, either from crystal‑structure databases, literature, or by relaxing the structure with density functional theory (DFT).
2. **Compute the single‑ion electronic structure** using one of two primary paradigms:
   - **First‑principles electronic structure** (e.g., DFT with hybrid functionals such as PBEh45, LDA/GGA, or Green’s‑function approaches) to obtain orbital‑level energies, projected densities of states, and magnetic moments. Spin‑orbit coupling is included either self‑consistently or perturbatively.
   - **Crystal‑field / ligand‑field models** that parametrize the splitting of the metal 3d levels (e.g., exchange charge model – ECM, ligand field multiplet – LFM). These models often serve as input for simulating X‑ray or optical spectra.
3. **Determine the spin state** by evaluating the relative energies of possible d‑electron configurations (low‑spin, high‑spin, intermediate‑spin) under the influence of crystal‑field splitting, electron–electron (Coulomb/Hund) interactions, and spin‑orbit coupling. For cobalt(II) (d⁷), this typically involves comparing the occupation schemes of the t₂g and e_g manifolds (or their symmetry‑adapted counterparts).
4. **Calculate additional physical properties** that depend on the spin state: magnetic moments, exchange coupling constants, X‑ray absorption pre‑edge intensities, circular dichroism spectra, or spin‑Hamiltonian parameters.
5. **Validate the assignment** by comparing computed observables (e.g., magnetic moment vs. SQUID data, computed XAS/XMCD line shapes vs. experimental spectra, or fitted spin‑Hamiltonian parameters vs. susceptibility data). The verification ensures that the predicted spin state reproduces the experimental behaviour.

## Typical Methods and Tools

Based on the papers in this family, the following resources are commonly employed:

- **DFT codes**: CRYSTAL (LCAO approach), augmented spherical wave (ASW) method, Green’s‑function LMTO (GF‑LMTO), VASP, etc.
- **Hybrid functional parametrizations**: PBEh45 (α=0.45), UTPSSh, HSE06, B3PW.
- **Crystal‑field parameter extraction**: Exchange charge model (ECM) yielding Bₚᵏ parameters for the crystal‑field Hamiltonian H_CF = Σ Bₚᵏ Oₚᵏ.
- **Ligand field multiplet codes**: Quanty (used for simulating XAS pre‑edge including p–d hybridization and spin‑orbit coupling).
- **Multi‑reference / configuration‑interaction methods**: CASSCF, CASPT2, MRCI (with active spaces including metal d and ligand p orbitals) for highly correlated spin‑state energetics.
- **Spin‑Hamiltonian fitting**: Numerical diagonalization of Heisenberg‑type Hamiltonians (e.g., ∑ –2J_ij Ŝ_i·Ŝ_j) to reproduce magnetic susceptibility (χT) and magnetisation data.
- **Spectroscopic analysis**: XMCD sum rules, Buckingham–Dunn uniaxial rotational strength formulae, and cluster models for interpreting X‑ray absorption features.

No specific dataset is required beyond crystallographic information; all necessary resources are task‑dependent and provided in each `paper‑*` subdirectory.

## Verification Style

Verification is fundamentally experimental. The computed spin‑state assignments are compared against low‑temperature magnetisation, magnetic susceptibility (χT vs. T), specific‑heat jumps, or spectroscopic fingerprints (XAS pre‑edge shapes, XMCD intensity ratios, vibrational spectra). When available, published experimental Curie–Weiss temperatures, g‑factors, or exchange constants serve as benchmarks. Agreement between calculation and measurement is taken as confirmation of the spin‑state assignment.

## Task Organization

Each `paper‑*` subdirectory corresponds to a standalone Harbor task. The task’s public file is `instruction.md`, which defines the specific computational or analytical procedure needed to reproduce or extend the corresponding paper’s results. The solving agent should consult the `instruction.md` of the relevant task for details about the required computations, input files, and expected outputs.

---

*This README applies to the entire workflow family; individual task instructions are contained within each subdirectory.*
