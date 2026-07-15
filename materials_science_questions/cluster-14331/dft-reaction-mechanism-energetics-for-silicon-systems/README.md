# DFT Reaction Mechanism Energetics for Silicon Systems

This workflow family contains **170 computational papers** (93 unique sources) that use density functional theory (DFT) and *ab initio* methods to study reaction mechanisms, activation energies, and thermochemistry for silicon‑containing systems. The family spans gas‑phase reactions, surface chemistry (e.g., silica, silicon surfaces), organosilicon catalysis, and materials processes such as CVD and H/D exchange.

## Core Computational Pattern

Across the papers, the **main computational workflow** follows these steps:

1. **Model definition** – A molecular cluster, periodic slab, or finite molecule is chosen to represent the silicon system (e.g., surface dimer cluster, organosilane, catalytic intermediate).
2. **Geometry optimization** – Stationary points (reactants, products, intermediates) are optimized using a density functional (commonly B3LYP, BP86, or PBE) or a correlated *ab initio* method (MP2, CCSD(T)), with appropriate basis sets.
3. **Transition state location** – Saddle points are identified (often via relaxed scan, Berny algorithm, or LST/QST) and verified by a single imaginary frequency and intrinsic reaction coordinate (IRC) calculations.
4. **Energy refinement** – Single‑point energies are computed at a higher level (e.g., CCSD(T)//MP2, G3MP2, or with nonlocal corrections) and combined with zero‑point vibrational corrections to obtain thermochemical data.
5. **Reaction analysis** – Activation energies, reaction enthalpies, free‑energy barriers, and product distributions are derived; kinetic interpretations (Arrhenius fits, LFER, isotope effects, RRKM) often accompany the mechanisms.

### Commonly Encountered Resources

**Computational methods:** B3LYP, BP86, PBE, MP2, CCSD(T), G3MP2, CAS‑SCF, and semi‑empirical (AM1).

**Basis sets:** 6‑311+G(d,p), 6‑31G**, TZVP/TZVPP, DZP, LANL2DZ with effective core potentials.

**Software tools:** Gaussian 03/98, DGauss, deMon, KiSThelP, DMol^3 (implicit from paper mentions).

## Typical Verification Style

The family employs **numeric verification**: the success of a reproduced calculation is judged by comparing the computed activation energies and reaction energies against experimental kinetic data or high‑accuracy benchmark calculations (e.g., CCSD(T) or multireference methods) within a specified tolerance (e.g., a few kcal·mol⁻¹). Many papers explicitly validate their level of theory by benchmarking bond dissociation energies or vibrational frequencies against known experimental values.

## Harbor Task Structure

Each `paper‑*` subdirectory is a standalone Harbor task containing a public `instruction.md` file that describes the required computation. The solving agent must replicate the reported energetic quantities (barriers, reaction energies, etc.) and optionally provide mechanistic interpretation using the described computational protocol. No additional bundled resources (e.g., pre‑computed geometries) are guaranteed; the agent must obtain the necessary basis sets, functionals, and input geometries as specified in the instruction.

---
*Workflow family definition: “DFT‑based computational study of reaction mechanisms involving silicon compounds, including geometry optimization, transition state search, and calculation of activation energies and reaction thermochemistry.”*
