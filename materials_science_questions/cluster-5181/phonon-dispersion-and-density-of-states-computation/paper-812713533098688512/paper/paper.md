![](./images/812713533098688512_1.jpg)

Phenomenological manybody potentials from the interstitial electron model. I.
Dynamic properties of metals

Mo Li and William A. Goddard III

Citation: *The Journal of Chemical Physics* **98**, 7995 (1993); doi: 10.1063/1.464553
View online: http://dx.doi.org/10.1063/1.464553
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/98/10?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
Visualizing many-body dynamics
Phys. Today **67**, 68 (2014); 10.1063/PT.3.2428

On the problem of fitting many-body potentials. I. The minimal maximum error scheme and the paradigm of
metal systems
J. Chem. Phys. **110**, 8899 (1999); 10.1063/1.478809

Modeling calcium and strontium clusters with many-body potentials
J. Chem. Phys. **107**, 4674 (1997); 10.1063/1.474829

A manybody confinement potential model for multihadron systems
AIP Conf. Proc. **110**, 100 (1984); 10.1063/1.34343

The electronic structure of molecules by a manybody approach. I. Ionization potentials and oneelectron
properties of benzene
J. Chem. Phys. **65**, 1378 (1976); 10.1063/1.433244

![](./images/812713533098688512_2.jpg)

# Phenomenological many-body potentials from the interstitial electron model. I. Dynamic properties of metals

Mo Li${}^{\text{a)}}$ and William A. Goddard III${}^{\text{b),c)}}$

California Institute of Technology, Pasadena, California 91125 ${}^{\text{d)}}$

(Received 6 November 1992; accepted 28 January 1993)

Inspired by the *ab initio* generalized-valence-bond calculations of small metal clusters, we propose a phenomenological many-body interaction model, the interstitial electron model (IEM), for interactions of ions and electrons in metals. In this model, the valence electrons are treated as classical particles situated at the crystal lattice interstitial positions. Simple pair potentials are used for ions and interstitial electrons, allowing the inhomogeneity and anisotropy of electron density distributions to be taken into account phenomenologically. To test the efficacy and applicability of this approach, the IEM is applied to lattice dynamics in fcc metals: Cu, Ni, Ag, Au, Pd, Pt, Al, Ca, Sr, and $\gamma$-Fe. The phonon dispersion relations, densities of states, and Debye temperature are calculated and found to be in good agreement with experiments. Extension of the IEM to the construction of a new many-body potential in metals and alloys is discussed.

## I. INTRODUCTION

Although pairwise interatomic interactions are still widely used in theories and simulations of condensed matter, much attention has been paid to incorporating many-body electron effects into an empirical interatomic potential.${}^{1}$ More specifically, the handling of the inhomogeneity and anisotropy in the electron density distribution is the center of interest. The simplest approach is to add to the pair potential${}^{2,3}$ a crystal volume dependent energy term which arises mainly from the density dependent electron kinetic energy. However, the introduction of such a volume dependent energy, or homogeneous electron density dependent energy, usually leads to the so called compressibility paradox: the compressibility derived from the long wave limit is not the same as that derived from homogeneous deformation. Moreover, the volume dependent pair potential is not, in general, suited for the study of problems that do not involve volume change (such as shear deformation, internal distortions, or cracking, etc.). The embedded atom method (EAM)${}^{4}$ has overcome this difficulty by including in the interatomic potential an inhomogeneous electron density dependent embedding energy deduced from density functional theory.${}^{5}$ However, the assumption in the EAM that the electron density is spherically symmetric or isotropic has been found to lead to a contradiction${}^{6}$ in hcp metals where the derived Cauchy discrepancy, $C_{12}-C_{66}$, has a sign opposite to that of the Cauchy discrepancy obtained from experiments. This happens in hcp metals that have the largest deviations from the ideal $c/a$ ratio (1.633), including Cd (1.886), Zn (1.856), and Be (1.568). It is very likely that the contradiction arises from neglecting the anisotropy of electron density distributions in these metals. For instance, it has been observed both theoretically and experimentally that the electron density of hcp Be is not homogeneous and accumulates at the tetrahedral interstices along the $c$ axis.${}^{7,8}$ Thus, an angular dependent embedding energy function is needed in the EAM to take into account the anisotropic electron density distributions in the hcp metals.

Inspired by the results from *ab initio* generalized-valence-bond (GVB) calculations of small metal clusters,${}^{9}$ we recently proposed a phenomenological interstitial electron model (IEM) to take into account the electron degrees of freedom in lattice dynamics.${}^{10}$ GVB calculations on clusters have shown that the electrons concentrate primarily at tetrahedral interstitial positions. Figure 1 shows the GVB orbitals of an fcc $\text{Li}_{13}^{+}$ cluster. The contour plots of the GVB orbitals or electron densities at different cross sections in the fcc structure show that the electrons accumulate primarily at the tetrahedral interstitial positions. In this GVB description, half the tetrahedra have two electrons and half have one (for a total of 12 electrons). These tetrahedra alternate so that the neighbors to a site with two electrons only have one electron. The full wave function is then a resonance of the configuration in Fig. 1 with one where the occupations are all interchanged.

Such an inhomogeneous and anisotropic charge distribution at the interstices in metals has been found in $\text{Li},{}^{11}$ $\text{Be},{}^{7}$ Rh, and $\text{Pd}^{12}$ in electronic band structure calculations and subsequently observed experimentally in bulk Be.${}^{8}$ The localization of the electrons at the lattice interstices suggests that the electron degrees of freedom can be treated explicitly, and thus an empirical many-body interaction potential can be constructed to handle the inhomogeneity and anisotropy of the valence electron density distributions in metals and alloys. In the IEM${}^{10}$ the electron density distribution at each interstice is replaced by a classical particle with a finite size and finite or zero mass sitting at

${}^{\text{a)}}$W. M. Keck Laboratory (138-78).
${}^{\text{b)}}$Materials and Molecular Simulation Center, Beckman Institute (139-74).
${}^{\text{c)}}$Author to whom correspondence should be addressed.
${}^{\text{d)}}$Contribution No. 8750 from Chemistry and Chemical Engineering.

J. Chem. Phys. 98 (10), 15 May 1993
© 1993 American Institute of Physics

![](./images/812713533098688512_3.jpg)

FIG. 1. GVB orbitals for two types of bond pairs on the fcc Li+3 cluster.
(a) The two spin-paired orbitals located in the doubly occupied 111
tetrahedron and (b) the orbital localized in the singly occupied 111 tet-
rahedron (and spin paired with the orbital of the 111 tetrahedron). Here,
cross sectional amplitudes of each of the orbitals are given at different
evenly spaced (001) planes. Planes B, D, and F pass through atoms,
marked by filled circles. Planes C and E pass through the centers of the
tetrahedral hollows, marked by asterisks. Planes A and G pass through
virtual tetrahedral centers [from Ref. 9(b)].

the center of the lattice interstice (its equilibrium posi-
tion); simple pairwise interaction potentials are used for
the interstitial electrons as well as the ions. Aside from its
simplicity, other features make the IEM a more attractive
model than the conventional interatomic or atom-centered
many-body potentials. First, pair potentials for many-body
electron-electron and electron-ion interactions greatly fa-
cilitate computations. In contrast, the angular dependent
atom-centered many-body potentials are usually awkward
to use. Second, the electron degrees of freedom are explic-
itly included and the electrons can respond to the external
perturbations independently. This allows the use of IEM to
study transport properties (electrical and thermogal-
vanic), work functions, plasma frequencies (if a finite mass
is assigned to the electrons), and so on. Finally, lattice
dynamics results¹⁰ indicate that the interactions between
ions are short ranged if the many-body effects are appro-
priately handled (the screened Coulomb potential is an-
other example).

This paper is the first of a series to construct a new
many-body potential in metals and alloys using the IEM.
The preliminary account of the work appeared in Ref. 10.
The reasons for applying the IEM first to lattice dynamics
are as follows. First, since lattice dynamics provides a di-
rect and sensitive probe of the interatomic interactions in
condensed matters (for a recent review, see Brüesch¹³),
comparison of the predicted lattice dynamic results with
those measured from experiments could provide a neces-
sary test for the efficacy and applicability of the IEM. Sec-
ond, only a minimum amount of work is needed to apply
the IEM to lattice dynamics in order to check its perfor-
mance because the exact forms of the interaction potentials
are not required: it is the various derivatives of the poten-
tials that are actually used in the lattice dynamics studies.

In order to facilitate the testing of the IEM, further
simplifications were made to minimize the number of free
parameters. First, nearest-neighbor interactions are used
and the longer ranged interactions, including Coulomb in-
teractions, are neglected. Since pair potentials are used, the
IEM reduces to a central force constant model (for the
ions and electrons). Any increase in the interaction range
increases the number of free parameters drastically (this
becomes clear in the next section). Second, fcc metals
rather than bcc or hcp metals, are considered, because the
fcc structure has the least number of tetrahedral interstices
and thus, the least number of interstitial electrons per unit
cell. Furthermore, the superposition of the sublattice of
interstitial electrons on the fcc structure adds only a tetra-
hedral point group to the overall symmetry. Therefore, the
symmetry group of the composite system has a greatly
reduced number of independent free parameters. In con-
trast, the bcc and hcp composite structures have larger
numbers of lattice particles and lower bond symmetry
groups, making it very complicated and almost impossible
to get analytical results. Finally, the electron mass is as-
sumed to be zero, which is equivalent to a Born-
Oppenheimer approximation. All these approximations
can be relaxed straightforwardly for numerical calculations
(as will be shown in future publications). In this paper, the

simplified model is studied analytically in order to demonstrate the applicability and efficacy of the IEM.

In the following section, we describe the IEM in detail. We present elastic properties derived from the IEM in Sec. III, the fitting procedure for the IEM model in Sec. IV, and the calculated phonon dispersion curves, densities of states, and the Debye temperature in Sec. V. Finally, the validity and universality in the IEM is briefly discussed.

## II. THE INTERSTITIAL ELECTRON MODEL

The Hamiltonian for the composite system with ions and interstitial electrons is written as
$$
H=T_{\mathrm{e}}+T_{\mathrm{i}}+V_{\mathrm{ii}}(R)+V_{\mathrm{ie}}(r, R)+V_{\mathrm{ee}}(r), \tag{1}
$$
where the subscripts i and e refer to the ions and electrons; $R$ denotes the ion positions, and $r$ denotes the positions of the interstitial electrons centered at the interstitial tetrahedra; $T_{\mathrm{i}}$ and $T_{\mathrm{e}}$ are the kinetic energies of the ions and electrons in the system and $V_{\mathrm{ii}}(R)$, $V_{\mathrm{ie}}(r, R)$, and $V_{\mathrm{ee}}(r)$ are the potential energies from the ion-ion, ion-electron, and electron-electron interactions. In the IEM, the potential energies are expressed as the summations of the phenomenological pairwise interactions,
$$
V_{\mathrm{ii}}(R)=\frac{1}{2} \sum_{\substack{l l^{\prime} \\\left(k k^{\prime}\right)}} \phi_{\mathrm{ii}}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right), \tag{2}
$$

$$
V_{\mathrm{ie}}(r, R)=\frac{1}{2} \sum_{\substack{l l^{\prime} \\\left(k k^{\prime}\right)}} \phi_{i e}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right), \tag{3}
$$
and
$$
V_{\mathrm{ee}}(R)=\frac{1}{2} \sum_{\substack{l l^{\prime} \\\left(k k^{\prime}\right)}} \phi_{\mathrm{ee}}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right), \tag{4}
$$
where $r\left(\begin{array}{l}l \\ k\end{array}\right)$ or $\left(\begin{array}{l}l \\ k\end{array}\right)$ specifies the position of the $k$ th particle situated in the $l$ th cell. The separation of two particles at $\left(\begin{array}{l}l \\ k\end{array}\right)$ and $\left(\begin{array}{l}l^{\prime} \\ k^{\prime}\end{array}\right)$ is expressed as $r\left(\begin{array}{c}l l^{\prime} \\ k k^{\prime}\end{array}\right)$ or $\left(\begin{array}{c}l l^{\prime} \\ k k^{\prime}\end{array}\right)$. $\phi_{\mathrm{ii}}, \phi_{\mathrm{ie}}$, and $\phi_{\mathrm{ee}}$ are the pairwise ion-ion, ion-electron, and electron-electron interactions. In this work, the summation extends to the nearest neighbors only.

The interstitial electrons in the IEM sit at the centers of the tetrahedral interstitial sites. For an fcc structure, there are a total of eight tetrahedra (12 in both bcc and hcp structures) per unit cell located at positions such as $\left[\frac{1}{4} \frac{1}{4} \frac{1}{4}\right]$, etc. They form a simple cubic sublattice in the composite system. However, the nearest neighbor ion-electron bond has a tetrahedral symmetry. The unit cell of this composite structure has one ion at [000] and two interstitial electrons at $\left[\frac{1}{4} \frac{1}{4} \frac{1}{4}\right]$ and $\left[\frac{3}{4} \frac{3}{4} \frac{3}{4}\right]$, the fluorite structure. Each such interstitial electron represents half the number of delocalized valence electrons from each atom. Thus for $\mathrm{Cu}(3 d)^{10}(4 s)^{1}$ atoms each interstitial electron represents half an electron. A GVB calculation of Cu metal would lead to full electrons at each tetrahedron site and those would go at alternate sites (as in zinc blend or GaAs). The full wave function would be a resonance of these two zinc blend configurations. The classical IEM description then uses half an electron at each site. In addition to the fluorite structure we also considered an alternative configuration which has the interstitial electrons sit at alternate tetrahedral interstitial positions. This leads to a unit cell with one ion at [000] and one interstitial electron at $\left[\frac{1}{4} \frac{1}{4} \frac{1}{4}\right]$, the zinc blend structure.

In the IEM, metals and alloys have the ions and interstitial electrons as the basic constituents. The latter is superimposed on the ion structures, or the atom structures as in the conventional atom-centered schemes. Such a composite system is equivalent to a "compound" composed of two different kinds of particles occupying two different sublattices. For convenience, in the following sections we will use the terms fluorite (three particles per unit cell) and zinc blend (two particles per unit cell) in referring to the two interstitial electron configurations.

The equations of motion for the lattice particles in the composite system can be easily derived within the harmonic approximation from Eq. (1),
$$
M_{k} \ddot{u}_{\alpha}\left(\begin{array}{l}
l \\
k
\end{array}\right)=-\sum_{l^{\prime}, k^{\prime}, \beta} \Phi_{\alpha \beta}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right) u_{\beta}\left(\begin{array}{l}
l^{\prime} \\
k^{\prime}
\end{array}\right), \tag{5}
$$
where $u_{\beta}\left(\begin{array}{l}l \\ k\end{array}\right)$ and $\ddot{u}_{\alpha}\left(\begin{array}{l}l \\ k\end{array}\right)$ are the Cartesian components of the displacements of the $k$ th particle and its second derivative with respect to time. $\Phi_{\alpha \beta}\left(\begin{array}{c}l l^{\prime} \\ k k^{\prime}\end{array}\right)$ is used as a collective symbol for the force constant matrix with components $\Phi_{\alpha \beta}^{\mathrm{ii}}, \Phi_{\alpha \beta}^{\mathrm{ie}}$, and $\Phi_{\alpha \beta}^{\mathrm{ee}}$. Here
$$
\Phi_{\alpha \beta}^{\mathrm{ii}}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)=\frac{\partial^{2} V_{\mathrm{ii}}}{\partial x_{\alpha}\left(\begin{array}{l}
l \\
k
\end{array}\right) \partial x_{\beta}\left(\begin{array}{l}
l^{\prime} \\
k^{\prime}
\end{array}\right)}, \tag{6}
$$
etc. and $x_{\alpha}\left(\begin{array}{l}l \\ k\end{array}\right)$ is the Cartesian component of the particle position $\left(\begin{array}{l}l \\ k\end{array}\right)$ at equilibrium. For pair interactions, Eq. (6) becomes
$$
\begin{aligned}
\Phi_{\alpha \beta}^{\mathrm{ii}}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)= & \phi_{\mathrm{ii}}^{\prime}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)\left[\frac{x_{\alpha}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right) x_{\beta}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)}{r^{3}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)}-\frac{\delta_{\alpha \beta}}{r\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)}\right] \\
& -\phi_{\mathrm{ii}}^{\prime \prime}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right) \frac{x_{\alpha}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right) x_{\beta}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)}{r^{2}\left(\begin{array}{c}
l l^{\prime} \\
k k^{\prime}
\end{array}\right)}. \tag{7}
\end{aligned}
$$

Equation (7) suggests that the derivatives $\phi^{\prime}\left(\begin{array}{c}l l^{\prime} \\ k k^{\prime}\end{array}\right)$ and $\phi^{\prime \prime}\left(\begin{array}{c}l l^{\prime} \\ k k^{\prime}\end{array}\right)$ can be used as free parameters for lattice dynamics. The number of such parameters increases with increasing number of neighbors included in the interaction. Since there are three types of potentials, there are a total of six free parameters for the nearest-neighbor interactions. For convenience, force constants are used rather than the potential derivatives. The symmetry group of the composite structure greatly reduces the number of components of the force constant matrices. It can be shown (see Ref. 10 for details) that the number of nonzero components of the force constant matrices $\Phi_{\alpha \beta}\left(\begin{array}{c}l l^{\prime} \\ k k^{\prime}\end{array}\right)$ for the nearest-neighbor pairwise potentials exactly matches the number of the potential derivatives. These independent force constants are listed as follows:

$$
\alpha=\Phi_{11}^{\mathrm{ii}}\left({ }_{00}^{0 l^{\prime}}\right)=-\frac{1}{a \sqrt{2}} \phi_{\mathrm{ii}}^{\prime}-\frac{1}{2} \phi_{\mathrm{ii}}^{\prime \prime}, \tag{8a}
$$

$$
\gamma=\Phi_{12}^{\mathrm{ii}}\left({ }_{00}^{0 l^{\prime}}\right)=\frac{1}{a \sqrt{2}} \phi_{\mathrm{ii}}^{\prime}-\frac{1}{2} \phi_{\mathrm{ii}}^{\prime \prime}, \tag{8b}
$$

$$
\mu=\Phi_{11}^{\mathrm{ie}}\left({ }_{01}^{0 l^{\prime}}\right)=-\frac{8}{a 3 \sqrt{3}} \phi_{\mathrm{ie}}^{\prime}-\frac{1}{3} \phi_{\mathrm{ie}}^{\prime \prime}, \tag{8c}
$$

$$
\lambda=\Phi_{12}^{\mathrm{ie}}\left({ }_{01}^{0 l^{\prime}}\right)=-\frac{4}{a 3 \sqrt{3}} \phi_{\mathrm{ie}}^{\prime}-\frac{1}{3} \phi_{\mathrm{ie}}^{\prime \prime}, \tag{8d}
$$

$$
\delta=
\begin{cases}
\Phi_{11}^{\mathrm{ee}}\left({ }_{12}^{0 l^{\prime}}\right)=-\phi_{\mathrm{ee}}^{\prime}, & \text{(fluorite)} \\
\Phi_{11}^{\mathrm{ee}}\left({ }_{12}^{0 l^{\prime}}\right)=-\frac{1}{a \sqrt{2}} \phi_{\mathrm{ee}}^{\prime}-\frac{1}{2} \phi_{\mathrm{ee}}^{\prime \prime}, & \text{(zinc blend)}
\end{cases}, \tag{8e}
$$

$$
\rho=
\begin{cases}
\Phi_{22}^{\mathrm{ee}}\left({ }_{12}^{0 l^{\prime}}\right)=-\frac{2}{a} \phi_{\mathrm{ee}}^{\prime}, & \text{(fluorite)} \\
\Phi_{12}^{\mathrm{ee}}\left({ }_{12}^{0 l^{\prime}}\right)=\frac{1}{a \sqrt{2}} \phi_{\mathrm{ee}}^{\prime}-\frac{1}{2} \phi_{\mathrm{ee}}^{\prime \prime}, & \text{(zinc blend)}
\end{cases}, \tag{8f}
$$

where $\alpha, \gamma, \mu, \lambda, \delta$, and $\rho$ are the independent components of the force constants. $a$ is the lattice parameter. $k=0,1$, and 2 refer to the ion and interstitial electrons in the unit cell, respectively. For the zinc blend structure, there are two lattice particles, so $k=0,1$. The fluorite structure has three lattice particles, $k=0,1,2$.

Fourier transformation of Eq. (5) gives the equations of motion for ions and interstitial electrons in the unit cell

$$
M_{k} \omega^{2}(\mathbf{q}) u_{\alpha}(\mathbf{q} k)=\sum_{k^{\prime} \beta} D_{\alpha \beta}\left({ }_{k k^{\prime}}^{\mathbf{q}}\right) u_{\beta}\left(\mathbf{q} k^{\prime}\right), \tag{9}
$$

where $\mathbf{q}$ is the wave vector, $\omega(\mathbf{q})$ is the vibration frequency, and $M_{k}$ is the mass of the lattice particle $k$ in the unit cell. $D_{\alpha \beta}$ are the corresponding dynamic matrices. For the fluorite structure, Eq. (9) can be written explicitly as

$$
\begin{aligned}
M_{0} \omega^{2}(\mathbf{q}) u_{\alpha}(\mathbf{q} 0)= & D_{\alpha \beta}^{\mathrm{ii}}\left({ }_{00}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 0)+D_{\alpha \beta}^{\mathrm{ie}}\left({ }_{01}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 1) \\
& +D_{\alpha \beta}^{\mathrm{ie}}\left({ }_{02}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 2), \tag{10a}
\end{aligned}
$$

$$
\begin{aligned}
M_{1} \omega^{2}(\mathbf{q}) u_{\alpha}(\mathbf{q} 1)= & D_{\alpha \beta}^{\mathrm{ei}}\left({ }_{10}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 0)+D_{\alpha \beta}^{\mathrm{ee}}\left({ }_{11}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 1) \\
& +D_{\alpha \beta}^{\mathrm{ee}}\left({ }_{12}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 2), \tag{10b}
\end{aligned}
$$

$$
\begin{aligned}
M_{2} \omega^{2}(\mathbf{q}) u_{\alpha}(\mathbf{q} 2)= & D_{\alpha \beta}^{\mathrm{ei}}\left({ }_{20}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 0)+D_{\alpha \beta}^{\mathrm{ee}}\left({ }_{21}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 1) \\
& +D_{\alpha \beta}^{\mathrm{ee}}\left({ }_{22}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 2). \tag{10c}
\end{aligned}
$$

The left hand sides of Eqs. (10b) and (10c) are zero ($M_1=M_2=0$, in the Born-Oppenheimer approximation), so the electron coordinates $\mathbf{u}(\mathbf{q} 1)$ and $\mathbf{u}(\mathbf{q} 2)$ can be expressed in terms of the ion coordinates $\mathbf{u}(\mathbf{q} 0)$ from the last two equations. Substituting the electron coordinates into Eq. (10a), leads to the equation of motion for the ion. Thus,

$$
M_{0} \omega^{2}(\mathbf{q}) u_{\alpha}(\mathbf{q} 0)=\sum_{k^{\prime}, \beta} D_{\alpha \beta}^{\text {total }}\left({ }_{00}^{\mathbf{q}}\right) u_{\beta}(\mathbf{q} 0), \tag{11}
$$

where $D_{\alpha \beta}^{\text {total }}$ is the dynamic matrix for ions with the electron-electron and electron-ion interactions taken into account. Its general form can be written as

$$
D_{\alpha \beta}^{\text {total }}\left({ }_{k k^{\prime}}^{\mathbf{q}}\right)=D_{\alpha \gamma}^{\mathrm{ie}}\left({ }_{k s}^{\mathbf{q}}\right) D_{\gamma \lambda}^{\mathrm{ee}}\left({ }_{s s^{\prime}}^{\mathbf{q}}\right)^{-1} D_{\lambda \beta}^{\mathrm{ei}}\left({ }_{s^{\prime} k^{\prime}}^{\mathbf{q}}\right). \tag{12}
$$

The summation convention is used here for the repeated indices, $\alpha, \beta, \gamma$, etc. $k$ denotes the ions and $s$ denotes electrons. The $D^{\text {ee }}$ is a $3 \times 3$ matrix for the zinc blend structure and $6 \times 6$ matrix for the fluorite structure. For bcc metals, there are a total of 12 tetrahedral interstices, or 6 interstitial electrons per unit cell. So the corresponding $D^{\text {ee }}$ is an $18 \times 18$ matrix, too tedious to solve analytically.

Phonon dispersions $\omega(\mathbf{q})$ are obtained by solving the secular equation,

$$
\left|D_{\alpha \beta}^{\text {total }}\left({ }_{00}^{\mathbf{q}}\right)-\delta_{\alpha \beta} M_{0} \omega^{2}(\mathbf{q})\right|=0. \tag{13}
$$

### III. ELASTIC PROPERTIES

In the long wavelength limit, the elastic properties can be derived from the lattice dynamics equation (11). The three elastic constants $\mathrm{C}_{11}, \mathrm{C}_{12}$, and $\mathrm{C}_{44}$ for fcc metals are expressed through the force constants,

$$
\begin{aligned}
& \mathrm{C}_{11}=-\frac{a^{2}}{2 V_{a}}(2 \alpha+\mu+\delta), \\
& \mathrm{C}_{12}=-\frac{a^{2}}{2 V_{a}}(-2 \alpha+3 \gamma-\mu+2 \lambda-\rho), \\
& \mathrm{C}_{44}=-\frac{a^{2}}{4 V_{a}}\left(2 \alpha-\gamma+\mu+\rho-\frac{\lambda^{2}}{\mu+\delta+2 \rho}\right),
\end{aligned} \tag{14}
$$

for the fluorite structure, and

$$
\begin{aligned}
& \mathrm{C}_{11}=-\frac{a^{2}}{4 V_{a}}(4 \alpha+\mu+4 \delta), \\
& \mathrm{C}_{12}=-\frac{a^{2}}{4 V_{a}}(-4 \alpha+6 \gamma-\mu+2 \lambda-4 \delta+6 \rho), \\
& \mathrm{C}_{44}=-\frac{a^{2}}{4 V_{a}}\left(4 \alpha-2 \gamma+\mu+4 \delta-2 \rho-\frac{\lambda^{2}}{\mu}\right),
\end{aligned} \tag{15}
$$

for the zinc blend structure. $V_{a}=\frac{1}{4} a^{3}$ is the volume per atom.

Mechanical equilibrium requires the stress $\sigma_{11}\left(=\sigma_{22}=\sigma_{33}\right)$ to be zero, that is,

$$
\frac{a^{2}}{2 V_{a}}(-2 \alpha+2 \gamma-\mu+\lambda-\rho)=0, \tag{16}
$$

for the fluorite structure and

$$
\frac{a^{2}}{4 V_{a}}(-4 \alpha+4 \gamma-\mu+\lambda-4 \delta+4 \rho)=0, \tag{17}
$$

for the zinc blend structure.

The above results directly lead to a relation between $\mathrm{C}_{12}$ and $\mathrm{C}_{44}$ at equilibrium,

<table>
<caption>TABLE I. Experimental data used for fitting IEM parameters. The lattice parameters, elastic constants, phonon spectra, and mass are in units of $\mathring{A}$, $10^{11}$ dyn/cm², THz, and amu, respectively.</caption>
<thead>
<tr>
<th>
</th>
<th>
Cu
</th>
<th>
Al
</th>
<th>
Ca
</th>
<th>
Sr
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$a$
</td>
<td>
3.6150
</td>
<td>
4.0496
</td>
<td>
5.5820
</td>
<td>
6.0849
</td>
</tr>
<tr>
<td>
$C_{11}$
</td>
<td>
16.840
</td>
<td>
11.394
</td>
<td>
2.780
</td>
<td>
1.700
</td>
</tr>
<tr>
<td>
$C_{12}$
</td>
<td>
12.140
</td>
<td>
6.663
</td>
<td>
1.823
</td>
<td>
1.200
</td>
</tr>
<tr>
<td>
$C_{44}$
</td>
<td>
7.540
</td>
<td>
2.783
</td>
<td>
1.630
</td>
<td>
0.990
</td>
</tr>
<tr>
<td>
$\omega_{X}^{L}$
</td>
<td>
7.190
</td>
<td>
9.796
</td>
<td>
4.520
</td>
<td>
3.200
</td>
</tr>
<tr>
<td>
$\omega_{X}^{T}$
</td>
<td>
5.080
</td>
<td>
5.867
</td>
<td>
3.630
</td>
<td>
2.325
</td>
</tr>
<tr>
<td>
Mass
</td>
<td>
63.540
</td>
<td>
26.980
</td>
<td>
40.08
</td>
<td>
87.73
</td>
</tr>
</tbody>
</table>

$$
\mathrm{C}_{12}-\mathrm{C}_{44}=\begin{cases}
-\frac{a^{2}}{2 V_{a}} \frac{\lambda^{2}}{\mu+\delta+2 \rho}, & \text { (fluorite) } \\
-\frac{a^{2}}{4 V_{a}} \frac{\lambda^{2}}{\mu}, & \text { (zinc blend) }
\end{cases}. \qquad (18)
$$

If the particle interactions are pairwise and every particle is at the center of inversion, then $\mathrm{C}_{12}-\mathrm{C}_{44}=0$, which is the Cauchy relation. $^{14}$ Except for a few crystals with the sodium chloride structure, the Cauchy relations are seldom obeyed. This discrepancy shows the necessity of nonpairwise interatomic interactions arising from the inhomogeneous and anisotropic electron density distributions. Equation (18) shows that the Cauchy discrepancy is related to ion-electron interactions in the zinc blend structure and to the ion-electron and electron-electron interactions in the fluorite structure. We should point out that in the IEM, the anisotropy of the electron density distribution is expressed by the arrangement of the interstitial electrons in the anisotropic tetrahedral interstices. The nonpairwise interactions between ions or atoms are mediated from the electron-ion and electron-electron interactions.

### IV. PARAMETERS FOR IEM

The IEM is a phenomenological model which uses the first and second derivatives of nearest-neighbor pair interparticle interactions as the free parameters. In order to calculate other static and dynamic properties, these free parameters have to be determined. The six parameters are related to the force constants $\alpha$, $\gamma$, $\mu$, $\lambda$, $\delta$, and $\rho$, which are directly related to the experimentally measured quantities. The force constants can be determined using the measured elastic constants, lattice constants, and two vibration frequencies at the zone boundary $X$, which are given by

$$
M_{0} \omega_{L}^{2}\left(\mathbf{q}_{X}\right)=-16 \alpha-8 \mu, \qquad (19)
$$

$$
M_{0} \omega_{T}^{2}\left(\mathbf{q}_{X}\right)=-16 \alpha+8 \gamma-8 \mu+\frac{8 \lambda^{2}}{\mu+\delta+\rho}, \qquad (20)
$$

for the fluorite structure and

$$
M_{0} \omega_{L}^{2}\left(\mathbf{q}_{X}\right)=-16 \alpha-4 \mu, \qquad (21)
$$

$$
M_{0} \omega_{T}^{2}\left(\mathbf{q}_{X}\right)=-16 \alpha+8 \gamma-4 \mu+\frac{4 \lambda^{2}}{\mu+4 \delta-2 \rho}, \qquad (22)
$$

for the zinc blend structure. The six experimental input data used in determining the six free parameters are listed in Table I. $^{15-26}$

<table>
<caption>TABLE II. (a) The force constants for the fluorite structure (dyn/cm). (b) The force constants for the zinc blend structure (dyn/cm).</caption>
<thead>
<tr>
<th>
(a)
</th>
<th>
Cu
</th>
<th>
Al
</th>
<th>
Ca
</th>
<th>
Sr
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$\alpha$
</td>
<td>
1 676.728
</td>
<td>
$-$7 684.250
</td>
<td>
5 734.482
</td>
<td>
$-$1 970.997
</td>
</tr>
<tr>
<td>
$\gamma$
</td>
<td>
$-$5 093.518
</td>
<td>
$-$6 783.201
</td>
<td>
$-$1 832.328
</td>
<td>
$-$3 218.063
</td>
</tr>
<tr>
<td>
$\mu$
</td>
<td>
30 212.914
</td>
<td>
$-$5 802.030
</td>
<td>
$-$18 164.677
</td>
<td>
$-$3 395.454
</td>
</tr>
<tr>
<td>
$\lambda$
</td>
<td>
$-$16 849.532
</td>
<td>
$-$6 708.041
</td>
<td>
$-$3 255.665
</td>
<td>
$-$432.877
</td>
</tr>
<tr>
<td>
$\delta$
</td>
<td>
$-$3 578.843
</td>
<td>
$-$1 717.809
</td>
<td>
$-$1 063.267
</td>
<td>
2 165.283
</td>
</tr>
<tr>
<td>
$\rho$
</td>
<td>
$-$177.11
</td>
<td>
896.087
</td>
<td>
$-$224.608
</td>
<td>
468.445
</td>
</tr>
<tr>
<td>
(b)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\alpha$
</td>
<td>
$-$2 554.551
</td>
<td>
$-$8 989.286
</td>
<td>
2 074.753
</td>
<td>
$-$119.199
</td>
</tr>
<tr>
<td>
$\gamma$
</td>
<td>
$-$5 269.800
</td>
<td>
$-$10 047.416
</td>
<td>
$-$1 850.334
</td>
<td>
$-$2 725.060
</td>
</tr>
<tr>
<td>
$\mu$
</td>
<td>
$-$43 500.710
</td>
<td>
$-$4 267.197
</td>
<td>
$-$21 690.437
</td>
<td>
$-$14 189.100
</td>
</tr>
<tr>
<td>
$\lambda$
</td>
<td>
$-$26 895.600
</td>
<td>
$-$8 188.291
</td>
<td>
$-$4 834.012
</td>
<td>
$-$4 259.430
</td>
</tr>
<tr>
<td>
$\delta$
</td>
<td>
$-$1 789.421
</td>
<td>
$-$1 388.083
</td>
<td>
$-$531.634
</td>
<td>
1 082.641
</td>
</tr>
<tr>
<td>
$\rho$
</td>
<td>
$-$3 225.450
</td>
<td>
650.320
</td>
<td>
$-$820.653
</td>
<td>
1 203.835
</td>
</tr>
</tbody>
</table>

Because of the simplifications discussed above, Eqs. (14)-(17) and (19)-(22) can be solved analytically to obtain the six force constants for the two interstitial electron configurations. For the fluorite structure, a cubic equation in $\rho$ is solved and three sets of real solutions are obtained. But only one set of the force constants is acceptable, the other two give imaginary phonon dispersions.

For the zinc blend structure, a quadratic equation in $\rho$ needs to be solved to get solutions for other force constants. Two solutions were obtained for Cu, Ni, and Al. The phonon dispersions calculated using these two sets of parameters are almost identical. For Ca, Sr, and $\gamma$-Fe, there is only one solution which gives real phonon dispersions. For Au, Ag, Pd, and Pt, there is no solution. However, for the metals with the zinc blend structure which have solutions, the longitudinal and $T_{2}$ transverse branches of the phonon dispersions along the [110] direction show no crossing and their polarization vectors show a dependence on the wave vectors. The reason for these incorrect results is the nonsymmetric assignment of the interstitial electrons. There is only one interstitial electron per unit cell in the zinc blend structure, so the second term of the $D^{\text{tot}}$ has a nonzero imaginary part resulting from the electron vibrations. In the fluorite structure, the imaginary part is canceled because the two interstitial electrons contribute the same imaginary parts, but with opposite signs (they vibrate with the same magnitude and opposite phases). So, the zinc blend structure is not a desirable configuration for lattice dynamics.

In Table II [(a) and (b)], the force constants are listed for Cu, Al, Ca, and Sr with the fluorite and zinc blend structures, respectively. Since the two sets of force constants of Cu, Ni, and Al with the zinc blend structure give identical phonon dispersions, only one set is listed in Table II (b). The rest of the parameters, calculated phonon dispersions (along the symmetry and off-symmetry directions), and density of states for Ni, Pd, Ag, Pt, Au, and $\gamma$-Fe are deposited with the Physics Auxiliary Publication

![](./images/812713533098688512_4.jpg)

FIG. 2. Phonon dispersion curves for Cu. Dots represent experimental data. Solid lines are for the fluorite structure.

Service of AIP. $^{27}$ Interested readers can obtain these results from there.

## V. LATTICE DYNAMICS

In the traditional Born-von Kármán method, the second derivatives of the potential energy with respect to the atom displacements are used as empirical parameters in the study of lattice dynamics. A satisfactory fit of experimental phonon dispersions by this method usually needs many such parameters, making the interaction range of the interatomic potentials extremely long. It is not desirable to have long range interatomic interactions. The physical meaning of an interatomic potential having five to ten nearest neighbors becomes questionable. Microscopic theories, on the other hand, are able to provide detailed understanding of lattice vibrations by explicitly including the electrons, but their complicated formalisms usually make it very difficult to calculate the phonon dispersions and thermophysical properties. For instance, the recently developed frozen-phonon method $^{28}$ could handle transition metals, but complications in computing the total energies make the calculated phonon dispersions available only at the wave vectors commensurate with the ion displacements. It would, therefore, be desirable to have lattice dynamics models which, on one hand, have a simple formalism for the numerical calculations and, on the other hand, still retain the important many-body effects. There are a growing number of such lattice dynamics models, for example, the shell model $^{29}$ for ionic solids and the adiabatic bond charge model $^{30}$ for covalent bond solids, the third-order perturbation method $^{31}$ for transition metals, and so on. The IEM bears the same key feature as these models: the valence electrons are treated as fictitious classical particles and the interatomic or interior interactions are modulated by the presence of these electrons. The vibration spectra, densities of states, and Debye temperature are calculated using IEM and presented as follows.

![](./images/812713533098688512_5.jpg)

FIG. 3. Phonon dispersion curves for Al.

The phonon dispersion curves were calculated for fcc metals Cu, Ni, Ag, Au, Pd, Pt, Al, Ca, Sr, and $\gamma$-Fe using the parameters for the fluorite structure. Figures 2-5 show only the phonon dispersions of Cu, Al, Ca, and Sr. The dots are the corresponding phonon dispersions from neutron scattering experiments. $^{16-26}$ Along the three high symmetry directions the phonon dispersions agree with experiments almost within experimental error, except for the transverse branch in the [111] direction for Pd, Pt, and Au, and the longitudinal branch for $\gamma$-Fe, which has an obvious softening at zone boundary $L$ at high temperature. For Ca and Sr, the phonon dispersion curves are in good agreement with experiment except for the [111] longitudinal branch in Ca. The best fit is for transition metals. In general, the IEM gives good predictions of the phonon dispersion relations for all ten fcc metals (alkaline earth metals, simple metal, and transition metals). A similar quality fit

![](./images/812713533098688512_6.jpg)

FIG. 4. Phonon dispersion curves for Ca.

![](./images/812713533098688512_7.jpg)

FIG. 5. Phonon dispersion curves for Sr.

using the traditional force constant model in the atom-centered scheme, would need at least eight sets of nearest neighbors. $^{32}$

The off-symmetry phonon dispersions of Cu are calculated and can be obtained from the Physics Auxiliary Publication Service. It was found $^{33}$ that using atom-centered pair potential models with force constants obtained by fitting experimental phonon dispersion curves along the high symmetry directions, the lattice dynamics do not necessarily predict the vibration frequencies in off-symmetry directions. Using the IEM, we find that the calculated phonon frequencies in the off-symmetry directions agree with the measured ones very well.

To calculate other thermophysical properties, one needs to know the phonon densities of states. The densities of states were computed for all fcc metals and displayed in Figs. 6-9 for Cu, Al, Ca, and Sr. Figure 10 shows the calculated Debye temperature for Cu, using the calculated density of states in Fig. 6. One can see that it agrees quite well with the experiments. $^{33,34}$

![](./images/812713533098688512_8.jpg)

FIG. 6. Phonon density of states for Cu.

![](./images/812713533098688512_9.jpg)

FIG. 7. Phonon density of states for Al.

Despite these good results with IEM, it remains to be shown that the IEM is capable of treating the many-body effects (phonon dispersions in fcc metals are quite simple). A more stringent test was conducted recently by Schultz and Messmer. $^{12}$ Using the IEM, they successfully fit the phonon dispersions in the intermetallic compound $Ni_3Al$ with as few as 12 parameters. Their results demonstrate that the IEM is able to predict dynamic properties of complicated systems. Further tests still need to be done to check effects on dynamic properties of not only different structures such as bcc and hcp, but also long range interactions ignored in the present simple model.

## VI. CONCLUSIONS

We have proposed and tested the interstitial electron model for lattice dynamics in metals. This model is inspired by results from calculations of small metal clusters using the *ab initio* generalized-valence-bond method. We calculated the phonon dispersions, densities of states, and Debye temperature for most fcc metals in the periodic table. The results are quite encouraging. However, since the specific form of the IEM used here is oversimplified (only

![](./images/812713533098688512_10.jpg)

FIG. 8. Phonon density of states for Ca.

J. Chem. Phys., Vol. 98, No. 10, 15 May 1993

![](./images/812713533098688512_11.jpg)

FIG. 9. Phonon density of states for Sr.

nearest-neighbor terms), these results merely demonstrate the applicability of IEM. Extending this model to use long range interactions is straightforward.

Because the key assumption that the electrons are lo- calized at the lattice interstitial sites is based on results from small cluster calculations, it remains uncertain whether the IEM is able to predict bulk properties and whether it can be generalized to other metals and alloys. To judge its validity and universality would require $ab$ initio calculations using correlated wave functions on very large, bulklike systems. Nevertheless, other theoretical or experimental approaches have provided some interesting results that support the assumption of localization of va- lence electrons in lattice interstices. For instance, band structure calculations $^{7,9,12}$ and x-ray measurements $^{8}$ indi cate that the electron accumulation at the tetrahedral in- terstices is not an artifact arising from the small cluster size effect or resulting from a particular technique used, but a natural consequence of electron many-body interactions. Unfortunately, real space distributions of the electron den- sity are often not available from experiment. We hope that the importance of the anisotropic and inhomogeneous elec- tron distribution to the interatomic interaction, as demon- strated by the IEM, will motivate further investigations along this direction.

In order to determine whether the IEM can predict other bulk properties, further tests are necessary. Like any other empirical interatomic interaction, the IEM is a phe- nomenological model. Its merits are based on simplicity and the ability to predict a variety of physical properties. It will be useful to apply it to realistic problems such as the above mentioned Cauchy discrepancy in hcp metals, sur- face structures, transport properties, structures of defects, and so on. This work is in progress.

## ACKNOWLEDGMENTS

This work was initiated with support from a grant from the National Science Foundation-Materials Research Groups (Grant No. DMR-8811795) and finished with support from NSF-CHE-91-100284. The facilities of the MSC/BI are supported also by grants from DOE-AICD, Allied Signal, ASAHI Chemical, ASAHI Glass, BP Amer- ica, Chevron, Xerox Corp., and Beckman Institute.

![](./images/812713533098688512_12.jpg)

FIG. 10. Calculated Debye temperature for Cu. Experimental data are from Ref. 32 (dots) and 33 (triangles).

$^{1}$Many-Atom Interactions in Solids, edited by R. M. Nieminen, M. J. Puska, and M. J. Manninen (Springer-Verlag, Berlin, 1990); Atomistic Simulation of Materials beyond Pair Potentials, edited by V. Vitek and D. J. Srolovitz (Plenum, New York, 1991); Interatomic Potentials and Crystalline Defects, edited by J. K. Lee (AIME, Warrendale, PA,1981).
$^{2}$K. Fuchs, Proc. R. Soc., London Ser. B 153, 622 (1936); R. A. Johnson, Phys. Rev. B 6, 2094 (1972).
$^{3}$W. A. Harrison, Electronic Structure and the Properties of Solids (Free- man, San Francisco, 1980).
$^{4}$M. S. Daw and M. I. Baskes, Phys. Rev. B 29, 6443 (1984).
$^{5}$P. Hohenberg and W. Kohn, Phys. Rev. B 136, 864 (1964).
$^{6}$M. Li and W. A. Goddard III (unpublished results).
$^{7}$S. T. Inoue and J. Y. Yamashita, J. Phys. Soc. Jpn. 35, 677 (1973); R. Dovesi et al., Phys. Rev. B 25, 3731 (1982) and M. Y. Chou, P. K. Lam, and M. L. Cohen, ibid. 28, 4179 (1983).
$^{8}$F. K. Larsen and N. K. Hansen, Acta Crystallogr. B 40, 169 (1984); L. Massa et al., Phys. Rev. Lett. 55, 622 (1985).
$^{9}$(a) M. H. McAdon and W. A. Goddard, Phys. Rev. Lett. 55, 2563(1985); (b) J. Phys. Chem. 91, 2607 (1987).
$^{10}$M. Li and W. A. Goddard, Phys. Rev. B 40, 12155 (1989).
$^{11}$R. Dovesi et al., Z. Phys. B 51, 195 (1983).
$^{12}$P. A. Schultz and R. P. Messmer, Phys. Rev. B 45, 7467 (1992).
$^{13}$P. Bruësch, Phonons: Theory and Experiments, Springer Series in Solid- State Science 34 (Springer-Verlag, Berlin, Heidelberg, 1982); A. A. Maradudin, E. W. Montroll, G. H. Weiss, and I. P. Ipatova, Theory of Lattice Dynamics in the Harmonic Approximation, 2nd ed. (Academic, New York, 1971).
$^{14}$M. Born and K. Huang, Dynamical Theory of Crystal Lattice (Oxford University, London, New York, 1954), p. 136.
$^{15}$W. B. Pearson, Handbook of Lattice Spacings and Structures of Metals and Alloys (Pergamon, Oxford, 1967); R. O. Simmons and H. Wang, Single Crystal Elastic Constants and Calculated Aggregate Properties: A Handbook (MIT, Cambridge, 1971).
$^{16}$U. Buchenau, M. Heiroth, H. R. Schober et al., Phys. Rev. B 30, 3502(1984).
$^{17}$R. Stedman, L. Almqvist, and G. Nilsson, Phys. Rev. 162, 549 (1967).
$^{18}$R. J. Birgeneau, J. Cordes, G. Dolling, and A. D. B. Woods, Phys. Rev. A 13, 1359 (1964).
$^{19}$E. C. Svensson, B. Brockhouse, and J. M. Rowe, Phys. 155, 619(1967).
$^{20}$A. P. Miller and B. N. Brockhouse, Can. J. Phys. 4, 704 (1971).
$^{21}$W. A. Kamitakahara and B. N. Brockhouse, Phys. Lett. 2A, 639(1969).
$^{22}$R. Ohrlich and W. Drexel, 4th IAEA Symp. Inelastic Scattering of Neutrons, Vol. 1 (IAEA, Vienna, 1968), p. 203.

$^{23}$J. W. Lynn, H. G. Smith, and R. M. Nicklow, Phys. Rev. B 8, 3493 (1973).

$^{24}$J. Zarestky and C. Stassis, Phys. Rev. B 35, 4500 (1987).

$^{25}$R. Stedman and G. Nilsson, Phys. Rev. 145, 492 (1966).

$^{26}$C. Stassis, J. Zaretsky, D. K. Misemer, H. L. Skriver, and B. N. Harmon, Phys. Rev. B 27, 3303 (1983).

$^{27}$See AIP document no. PAPS JCPSA-98-7995-19 for 19 pages of tables and figures. Order by PAPS number and journal reference from American Institute of Physics, Physics Auxiliary Publication Service, 335 East 45th Street, New York, NY 10017. The price is $1.50 for each microfiche (60 pages) or $5.00 for photocopies of up to 30 pages, and $0.15 for each additional page over 30 pages. Airmail additional. Make checks payable to the American Institute of Physics.

$^{28}$K.-M. Ho, C. L. Fu, and B. N. Harmon, Phys. Rev. B 2, 1575 (1984).

$^{29}$W. Cochran, Phys. Rev. Lett. 2, 495 (1959).

$^{30}$W. Weber, Phys. Rev. Lett. 33, 371 (1974).

$^{31}$D. Prakash and J. C. Upadhyaya, J. Phys. Chem. Solids 49, 91 (1988).

$^{32}$G. Gilat and R. M. Nicklow, Phys. Rev. 143, 487, (1966).

$^{33}$D. L. Martin, Can. J. Phys. 38, 17 (1960).

$^{34}$T. C. Cetas, C. R. Tilford, and C. A. Swenson, Phys. Rev. 174, 835 (1968).
<br>
J. Chem. Phys., Vol. 98, No. 10, 15 May 1993