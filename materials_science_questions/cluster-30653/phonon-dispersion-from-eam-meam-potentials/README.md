# Phonon dispersion from EAM/MEAM potentials

This family of computational workflows calculates phonon dispersion curves for
metals and alloys using the Embedded Atom Method (EAM) or Modified Embedded Atom
Method (MEAM) for the interatomic interactions. The primary goal is to predict
and validate vibrational spectra against experimental neutron/scattering
data.

## Core computational pattern

The common procedure across the papers in this family consists of:

1. **Define the EAM/MEAM total‑energy functional**  
   The potential energy of a system of atoms with positions
   \(\mathbf{R}_i\) is given by
   \[
   E_{\text{tot}} = \sum_i F_i(\rho_i) + \frac12 \sum_{i\neq j} \phi_{ij}(R_{ij}),
   \]
   where \(\rho_i = \sum_{j\neq i} \rho_j^a(R_{ij})\) is the host electron density at atom \(i\),
   \(F_i\) is the embedding energy function, \(\phi_{ij}\) is the short‑range pair potential,
   and \(\rho_j^a\) is the atomic electron density contribution from atom \(j\).
   For MEAM, angular terms are added to the density.

2. **Fit the potential parameters to bulk properties**  
   The functions \(F\), \(\phi\), and \(\rho^a\) are parameterised to reproduce
   experimental or first‑principles data such as:
   - equilibrium lattice constants
   - cohesive energy
   - elastic constants (\(C_{11}, C_{12}, C_{44}\))
   - vacancy formation energy
   - (optionally) equation‑of‑state of Rose et al.

3. **Compute interatomic force‑constant tensors**  
   The force‑constant tensor between atoms \(i\) and \(j\) is obtained from the
   second derivatives of the total energy:
   \[
   K_{ij}^{\alpha\beta} = \frac{\partial^2 E_{\text{tot}}}{\partial R_i^{\alpha} \partial R_j^{\beta}}.
   \]
   For EAM this leads to an expression involving the derivatives of \(F\), \(\phi\),
   and \(\rho^a\) (see, e.g., Nelson et al., Phys. Rev. B 40, 1465 (1989)).

4. **Construct the dynamical matrix**  
   For a given wave‑vector \(\mathbf{q}\) the dynamical matrix is built from the
   force‑constant tensors:
   \[
   D_{\alpha\beta}(\mathbf{q}) = \frac{1}{\sqrt{M_\alpha M_\beta}} \sum_{l} K_{0l}^{\alpha\beta} e^{i\mathbf{q}\cdot(\mathbf{R}_l - \mathbf{R}_0)},
   \]
   where the sum runs over lattice translations.

5. **Diagonalise the dynamical matrix**  
   The eigenvalues \(\omega_\lambda(\mathbf{q})\) give the phonon frequencies.
   This step is often implemented using standard linear algebra routines or
   dedicated codes like `phonopy`.

6. **Compare with experimental phonon dispersion data**  
   The calculated \(\omega(\mathbf{q})\) curves are plotted against experimental
   points from inelastic neutron scattering (INS) or other measurements.
   The agreement is quantified by metrics such as:
   - average relative error
   - r.m.s. deviation
   - maximum deviation at Brillouin‑zone boundaries

   A typical acceptable deviation is of order ~0.3 THz at zone boundaries
   (see Nelson et al., 1989).

## Common resources (tool‑ and dataset‑categories)

*Interatomic‑potential fitting*  
`atomicrex`, the `pyiron`/`PotentialFit` interface, or custom codes implementing
EAM/MEAM analytical forms.

*Phonon calculations*  
`phonopy`; the dynamical‑matrix construction and diagonalisation can also be
performed within the same code used for MD (e.g., LAMMPS with the `phonon`
package).

*Molecular dynamics / static relaxations*  
`LAMMPS` is frequently employed to relax structures and compute forces.

*DFT reference data generation*  
`VASP` (via the `pyiron` wrapper) is used when the potential is trained from
first‑principles databases.

*Workflow automation*  
`pyiron` provides integrated job management and wrappers around the above tools,
enabling reproducible end‑to‑end pipelines.

*Experimental phonon data*  
Measured phonon dispersion curves for f.c.c. transition metals (e.g., Cu, Ag, Ni,
Pd) and for some b.c.c. metals are taken from the literature (INS experiments).

## Verification style

The verification is **numeric**: the computed phonon frequencies are compared with
experimental data using quantitative accuracy measures (average relative error,
r.m.s. deviation, zone‑boundary deviations). The workflow is purely computational
and does not generate new laboratory data; instead, it benchmarks against already
published experimental curves.

## Repository structure

Each `paper-*` directory is a standalone **Harbor task**.  The public
entry‑point file is `instruction.md`, which details the specific objective
and evaluation criteria for that paper.
