# Quantum Monte Carlo calculation of Compton profiles of solid lithium

Claudia Filippi
Department of Physics, University of Illinois at Urbana-Champaign, Urbana, Illinois 61801

David M. Ceperley
Department of Physics and National Center for Supercomputing Applications, University of Illinois at Urbana-Champaign, Urbana, Illinois 61801

(Received 31 July 1998)

Recent high-resolution Compton scattering experiments in lithium have shown significant discrepancies with conventional band theoretical results. We present a pseudopotential quantum Monte Carlo study of electron-electron and electron-ion correlation effects on the momentum distribution of lithium. We compute the correlation correction to the valence Compton profiles obtained within Kohn-Sham density functional theory in the local density approximation and determine that electronic correlation does not account for the discrepancy with the experimental results. Our calculations lead to different conclusions than recent $GW$ studies and indicate that other effects (thermal disorder, core-valence separation, etc.) must be invoked to explain the discrepancy with experiments. [S0163-1829(99)08011-X]

## I. INTRODUCTION

Inelastic x-ray scattering is called Compton scattering when the energy and the momentum transferred are large compared to the characteristic energy and reciprocal interelectronic distance of the scattering system. Compton scattering probes the electronic structure of materials through the electronic momentum distribution and, if the scattering system is metallic, gives direct information on various characteristics of the Fermi surface, such as position and size of the Fermi breaks and their renormalization due to electron-electron correlation. Fermi momenta are of the order of 1 a.u. so that high resolution in momentum is necessary in order to resolve features related to the Fermi surface. In the last few years, the advent of high-intensity, high-energy, and well-polarized synchrotron sources has made it possible to obtain resolutions of the order of 0.1 a.u. and high statistics. Record resolutions of the order of 0.02 a.u. have been recently achieved for solid beryllium $^{1}$ and lithium. $^{2}$

In the range of energy and momentum transferred where the recoil electron can be considered free, i.e., within the impulse approximation, $^{3}$ the experimental double-differential Compton cross section is related to the momentum distribution $n(\mathbf{p})$ of the electronic system as (in atomic units $\hbar=e=m=1$)

$$
\frac{d^{2} \sigma}{d \Omega d \omega_{2}}=\left(\frac{d \sigma}{d \Omega}\right)_{\mathrm{Th}} \int \frac{d \mathbf{p}}{(2 \pi)^{3}} n(\mathbf{p}) \delta\left(q^{2} / 2+\mathbf{p} \cdot \mathbf{q}-\omega\right), \quad(1)
$$

where $\omega$ and $\mathbf{q}$ are the energy and momentum transferred, $\omega_{2}$ is the energy of the scattered photon, and $(d \sigma / d \Omega)_{\mathrm{Th}}$ is the Thomson differential cross section. The outcome of a Compton scattering experiment is therefore given by what is called a Compton profile in a given direction $\mathbf{q}$ and defined as

$$
J(\tilde{p})=\int d \mathbf{p} n(\mathbf{p}) \delta(\mathbf{p} \cdot \hat{\mathbf{q}}-\tilde{p}). \quad(2)
$$

The Compton profile at $\tilde{p}$ is the integral of the momentum distribution on a plane perpendicular to the unit vector $\hat{\mathbf{q}}$ at a distance $\tilde{p}$ from the origin. The momentum distribution is expressed in terms of the wave function of the electronic system as

$$
\begin{aligned}
n(\mathbf{p})= & \frac{N}{V} \int d \mathbf{r}_{1} \cdots d \mathbf{r}_{N} \int d \mathbf{r}^{\prime} e^{i \mathbf{p} \cdot \mathbf{r}^{\prime}} \\
& × \Psi^{*}\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{N}\right) \Psi\left(\mathbf{r}_{1}+\mathbf{r}^{\prime}, \ldots, \mathbf{r}_{N}\right), \quad(3)
\end{aligned}
$$

where $N$ is the number of electrons and $V$ the volume of the system.

Since Compton experiments can only access the momentum distribution in an indirect way and there are difficulties in handling background or subtracting the core contribution (the impulse approximation may not hold for the core electrons $^{4,5}$), it is important to establish the performance of the technique for a system for which high-resolution experimental data are available and correlated calculations can be performed. Being a low- $Z$ material, lithium has been the subject of Compton studies since the early days of x-ray Compton scattering. $^{6}$ Recent high-resolution experiments have been conducted on lithium and Fermi-surface signatures have been investigated either by analyzing first and second derivatives of the Compton profiles $^{7}$ or attempting a reconstruction of the momentum distribution. $^{8}$

Despite overall shape similarities, there is a clear discrepancy between the measured Compton profiles of lithium and the theoretical profiles computed within Kohn-Sham density functional theory in the local density approximation (LDA) even when the Lam-Platzman correlation corrections $^{9}$ are included. These discrepancies were attributed to inadequate treatment of correlation in the Kohn-Sham single-particle picture $^{7}$ and it was proposed that plasmaron (a bound hole-plasmon state) losses could explain the observed difference. $^{8}$ Two recent theoretical studies have tried to explain this discrepancy but reached opposite conclusions. Kubo calculated

the Compton profiles using the occupation numbers obtained from a $GW$ calculation and recovered good agreement with experimental results. $^{10}$ Dungdale and Jarlborg simulated the effect of thermal disorder on the Kohn-Sham Compton profiles, found that disorder leads to a delocalization of the momentum distribution and concluded that this effect, combined with the Lam-Platzman correlation corrections, accounts for the discrepancy with the experimental Compton profiles. $^{11}$

In order to determine the correction to the LDA Compton profiles due to electron-electron correlation, we perform a fully correlated calculation of the momentum distribution of solid lithium within pseudopotential quantum Monte Carlo (QMC). The QMC Compton profiles differ from the room-temperature experimental data by Sakurai *et al.* $^{7}$ and indicate that Lam-Platzman corrections give a satisfactory description of electronic correlation in this system even though they are isotropic and cannot reproduce the observed directional dependence of the QMC corrections to the LDA Compton profiles. Therefore, the QMC results for bcc lithium differ from the $GW$ calculations $^{10}$ and suggest that the discrepancy between conventional band theory and experiments originates from other sources: temperature effects $^{11}$ or problems in the interpretation of the experimental data $^{4,5}$ are possible explanations.

Recently, QMC calculations of Compton profiles have also been performed for a rather different system, silicon. $^{12}$ Due to the absence of a Fermi surface, the momentum distribution of silicon is a smooth function and finite-size errors in QMC are easier to correct than in a metal. These studies concluded that, also in silicon, correlation effects are well described by the Lam-Platzman corrections and do not fully account for the discrepancy between the theoretical Kohn-Sham LDA profiles and the experimental results.

In Sec. II, the characteristics of our density functional theory calculations are outlined. In Sec. III, the functional form of the QMC wave function is described. In Sec. IV, we compare the Kohn-Sham Compton profiles obtained from pseudopotential and full-core LDA calculations. We then discuss the role of electron-ion and electron-electron correlation on the momentum distribution in QMC. We finally present the QMC correlation corrections to the valence Kohn-Sham Compton profiles and compare them with the experimental results. In Appendix A, the linear tetrahedron method to obtain the Kohn-Sham Compton profiles is briefly outlined. In Appendix B, convergence of valence properties of lithium from full-core plane-wave calculations is discussed. Variance minimization, variational Monte Carlo (VMC) and diffusion Monte Carlo (DMC) methods are briefly presented in Appendix C.

## II. LDA CALCULATIONS

We study bcc lithium at the experimental lattice constant of 6.60 a.u. We carry out pseudopotential and full-core calculations within LDA density functional theory in a planewave basis. The pseudopotential calculations provide the single-particle orbitals that enter in the QMC wave function and the reference momentum distribution for the correlation corrections determined within QMC. The full-core calculations of the valence contribution to the Compton profiles are carried out to account properly for core-valence orthogonality. In Appendix A, we describe how to evaluate the Kohn-Sham momentum distribution and construct the Compton profiles using the linear tetrahedron method.

In the pseudopotential calculations, we use the Troullier-Martins pseudopotentials whose $s$ and $p$ components are generated with a cutoff radius of 2.4 a.u. (Ref. 13). The planewave cutoff is set to 16 Ry and 44 special $k$ points $^{14}$ in the irreducible wedge of the zone are used for zone sampling during iteration to self-consistency. The Compton profiles are generated from 16 206 $k$ points in the irreducible zone unfolded in a sphere of 2 a.u. radius (the mesh spacing is 0.0136 a.u.). The profiles are converged with respect to mesh spacing and sphere radius but appear to be very sensitive to the value of the Fermi energy that must be carefully determined as described in Appendix A.

The valence Compton profiles from a plane-wave fullcore calculation are obtained with a plane-wave cutoff of 400 Ry and 3311 $k$ points in the irreducible zone, unfolded into a sphere of 4 a.u. radius (the mesh spacing is 0.0238 a.u.). The Compton profiles are in good agreement with the profiles computed with the linearized augmented plane-wave method. $^{15}$ In Appendix B, we discuss convergence issues for valence properties computed from a full-core calculation in a plane-wave basis.

The LDA Compton profiles are normalized to the number of valence electrons per unit cell, in this case one electron per unit cell. The error in the normalization of the original LDA Compton profiles is very small. For instance, in the [111] direction, the error is about 0.1% for the pseudopotential and 0.8% for the full-core calculation.

## III. QUANTUM MONTE CARLO CALCULATIONS

In the quantum Monte Carlo simulations of bcc lithium, we treat lithium as a pseudo-ion of charge one plus one valence electron. We test the use of both a local and a nonlocal pseudopotential. $^{16}$ To simulate an infinite solid, we model the system as a collection of ions and electrons in a simulation cell periodically repeated. An effective computation of the Ewald sums over the images of the potential is obtained by optimizing the separation between the long- and shortrange components of the electron-electron, electron-ion, and ion-ion interactions. $^{17}$ We will consider cubic simulations cells containing 54, 250, and 686 lithium atoms.

The wave function used in these calculations is a determinant of single-particle orbitals multiplied by a Jastrow factor describing electron-electron and electron-ion correlations:

$$
\Psi=D^{\uparrow} \times D^{\downarrow} \exp \left[-\sum_{i>j}^{N} u\left(r_{i j}\right)+\sum_{i=1}^{N} \chi\left(\mathbf{r}_{i}\right)\right]. \tag{4}
$$

$D^{\uparrow}$ and $D^{\downarrow}$ are the Slater determinants of single-particle orbitals for the up and down electrons, respectively, $u$ correlates pairs of electrons and $\chi$ is a single-body term.

We consider two forms of single-particle orbitals. (1) We test the very simple choice

$$
\phi_{0}(\mathbf{r})=e^{i \mathbf{k} \cdot \mathbf{r}}. \tag{5}
$$

(2) We compute the single-particle orbitals from a LDA density functional theory calculation within a plane-wave basis:
$$
\phi_{\mathrm{LDA}}(\mathbf{r})=\sum_{\mathbf{G}} c_{\mathbf{k}+\mathbf{G}} e^{i(\mathbf{k}+\mathbf{G}) \cdot \mathbf{r}},\qquad(6)
$$
where $\mathbf{G}$ are the reciprocal lattice vector of the underlying bcc lattice. We discuss the occupation of the orbitals below.

The electron-electron term in the Jastrow factor is periodic over the cell and contains no free parameters. It is derived within the random-phase approximation (RPA) and has been extensively used for the homogeneous electron gas $^{18}$ and solid hydrogen calculations. $^{19}$ It describes both the exact short range (cusp condition) and large distance (plasmon) behavior. We only impose the antiparallel cusp conditions,
$$
u^{\uparrow \downarrow}\left(r_{i j}\right)=u^{\uparrow \uparrow}\left(r_{i j}\right)=u^{\downarrow \downarrow}\left(r_{i j}\right)=u_{\mathrm{RPA}}\left(r_{i j}\right).\qquad(7)
$$

The single-body term in the Jastrow factor has the periodicity of the underlying lattice, is expanded in Fourier components and rewritten as the sum over stars of reciprocal lattice vectors
$$
\chi(\mathbf{r})=\sum_{s} \chi_{s} \sum_{\mathbf{G} \in s} \Phi_{\mathbf{G}} e^{i \mathbf{G} \cdot \mathbf{r}}.\qquad(8)
$$

Since the point group of bcc lithium is symmorphic, the phases $\Phi_{\mathbf{G}}$ can be set to unity. We include up to twelve stars but convergence is obtained already with an expansion over seven stars. The coefficients of the stars, $\chi_{s}$, are optimized using the variance minimization method. $^{20,21}$

A brief description of variance minimization, VMC and DMC methods is given in Appendix C.

### A. $k$-point sampling
We require that the wave function satisfies boundary conditions that can be either periodic or arbitrary:
$$
\begin{aligned}
& \Psi\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{i}+\mathbf{R}_{s}, \ldots, \mathbf{r}_{N}\right) \\
& \quad=e^{i \mathbf{k}_{s} \cdot \mathbf{R}_{s}} \Psi\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{i}, \ldots, \mathbf{r}_{N}\right),
\end{aligned}\qquad(9)
$$
where one electron has been displaced by a translational vector of the simulation cell $\mathbf{R}_{s}$. The Jastrow component is periodic over the cell and does not affect the phase of the wave function. The determinant satisfies the above equation if the single-particle orbitals $\phi$ obey similar equations, $\phi(\mathbf{r}+\mathbf{R}_{s})$ $=\exp \{i \mathbf{k}_{s} \cdot \mathbf{R}_{s}\} \phi(\mathbf{r})$, that is if the orbitals correspond to a single $k$-point sampling of the simulation cell given by $\mathbf{k}_{s}$. If we impose periodic boundary conditions on our cubic cell of side $L$, the orbitals are Bloch states with wave vectors defined on a cubic grid centered on the origin with spacing $2 \pi / L$. For arbitrary boundary conditions, the grid of wave vectors is shifted by $\mathbf{k}_{s}$.

The idea of $k$-point sampling in QMC was introduced to achieve faster convergence in the total energy versus system size, possibly faster than in a periodic calculation. $^{22}$ For bcc lithium, since the valence band is an $s$ band, a calculation not at the $\Gamma$ point yields a higher energy and corresponds to an excited state of our finite simulation cell. On the other hand, the allowed momenta coincide with the wave vectors compatible with the condition of periodicity on the simulation cell, so we can obtain a higher resolution in momentum space by performing calculations with different boundary conditions. $^{12}$

We only consider $k$ samplings that yield a grid of $k$ points with inversion symmetry so that we can construct a real wave function by occupying linear combinations of pairs of orbitals:
$$
\phi_{\mathbf{k}}^{+}=\frac{1}{2}\left(\phi_{\mathbf{k}}+\phi_{-\mathbf{k}}\right), \quad \phi_{\mathbf{k}}^{-}=\frac{1}{2 i}\left(\phi_{\mathbf{k}}-\phi_{-\mathbf{k}}\right).\qquad(10)
$$

By restricting ourselves to real wave functions, we can perform both VMC and DMC calculations and avoid the complications of dealing with complex wave functions in DMC. $^{23}$ For a cubic simulation cell, there are only four vectors $\mathbf{k}_{s}$ that preserve inversion symmetry corresponding to $\Gamma$, $X, M$, and $R$ sampling of the cubic simulation cell. The $\Gamma$ point calculation yields a cubic grid of $k$ vectors centered on the origin with spacing $2 \pi / L$ and the additional calculations provide three grids shifted by $(2 \pi / L) / 2$ in the [100], [110], and [111] directions, respectively.

To construct the determinantal part of the wave function, we compute the orbitals on the grid of $k$ vectors compatible with the boundary conditions and occupy the orbitals $\phi_{0}$ or $\phi_{\mathrm{LDA}}$ within the first Brillouin zone with the lowest free-electron $(\phi_{0})$ or LDA $(\phi_{\mathrm{LDA}})$ energy. In general, the highest occupied level is degenerate and only partially occupied, so we should employ a linear combination of determinants in order to construct a wave function with the proper symmetry. We instead always use a single determinant and symmetrize the momentum distribution on the grid of allowed wave vectors by averaging it over symmetry related $k$ vectors on the grid. This procedure is done separately for the four $k$-point samplings. Finally, by combining the results of the four calculations and applying the symmetry rotations of the cubic group, we obtain a momentum distribution defined on a mesh with spacing $(2 \pi / L) / 2$.

We consider cubic cells with 54, 250, and 686 atoms. For the 54-atom cell, we only carry out a $\Gamma$-point calculation. The wave function is constructed from the orbitals corresponding to the lowest four complete shells of $k$ vectors, so it is real, has the full symmetry of the lattice and is a spin singlet. For the 250- and 686-atom cell, we compute the momentum distribution for four wave functions corresponding to $\Gamma, X, M$, and $R$ sampling of the cubic cell. The grid in momentum space has spacing 0.095 and 0.068 a.u. for the 250- and the 686-atom cell, respectively.

### B. Momentum distribution and Compton profiles
The momentum distribution of the correlated wave function is computed as the expectation value over the distribution given either by $\Psi^{2}$ (VMC) or by the product of the trial wave function and the fixed-node solution (DMC):
$$
n(\mathbf{p})=\sum_{i} \frac{1}{V}\left\langle\int d \mathbf{r}^{\prime} e^{i \mathbf{p} \cdot \mathbf{r}^{\prime}} \frac{\Psi\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{i}+\mathbf{r}^{\prime}, \ldots, \mathbf{r}_{N}\right)}{\Psi\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{N}\right)}\right\rangle.
$$

At a given Monte Carlo step, we uniformly sample $M$ random positions $\mathbf{r}^{\prime}$ within the simulation cell and, for each position and particle, compute in turn the above ratio. $^{24}$ The

value of $M$ depends on the size of the system and is determined to optimize the efficiency in sampling the momentum distribution. The allowed values of momentum coincide with the sets of vectors compatible with the condition of periodicity imposed on the simulation cell [Eq. (9)].

To obtain the Compton profiles, we have to integrate the momentum distribution over planes perpendicular to a given direction. It is possible to compute the Compton profiles directly within QMC. For instance, to evaluate the profile in the [100] direction, we could estimate the following expectation value:

$$
J(\tilde{p}_{x})=\sum_{i} \frac{(2 \pi)^{2}}{V}\left\langle\int d x e^{i \tilde{p}_{x} x} \frac{\Psi\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{i}+x, \ldots, \mathbf{r}_{N}\right)}{\Psi\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{N}\right)}\right\rangle.
\tag{12}
$$

This procedure is equivalent to evaluating the integral of the momentum distribution as the histogram over the momenta compatible with the boundary conditions:

$$
J(\tilde{p}_{x}) \approx(2 \pi / L)^{2} \sum_{\mathbf{p}: p_{x}=\tilde{p}_{x}} n(\mathbf{p}),
\tag{13}
$$

and is clearly a poor representation of the integral of a function with several discontinuities, especially if the grid of $k$ vectors is coarse. The Compton profiles computed in this way show indeed a strong dependence on the size of the simulation cell.

To obtain Compton profiles with reduced finite size errors, we want to integrate a smoother function than the QMC momentum distribution, $n_{\mathrm{QMC}}(\mathbf{p})$. We have to select a reference distribution $n_{\mathrm{MODEL}}(\mathbf{p})$ whose Compton profiles $J_{\mathrm{MODEL}}(p)$ can be computed with high accuracy and such that the difference $\Delta n(\mathbf{p})=n_{\mathrm{QMC}}(\mathbf{p})-n_{\mathrm{MODEL}}(\mathbf{p})$ is a smoother function than the original $n_{\mathrm{QMC}}(\mathbf{p})$. The Compton profiles are then obtained as

$$
J_{\mathrm{QMC}}(p)=J_{\mathrm{MODEL}}(p)+\Delta J(p),
\tag{14}
$$

where the corrections $\Delta J(p)$ are computed by integrating $\Delta n(\mathbf{p})$ on the grid defined by the four $k$-point samplings using the linear tetrahedron method. The only difference in computing $\Delta J(p)$ from the method described in Appendix A is that there is no Kohn-Sham energy defined on the grid and no Fermi energy but all grid points are considered for integration. In Sec. IV, we will show our choice for the reference momentum distribution.

## IV. RESULTS AND DISCUSSION

We present calculations of the momentum distribution and Compton profiles within LDA Kohn-Sham density functional theory. We perform both pseudopotential and full-core calculations. We then compute the momentum distribution within pseudopotential QMC and determine the correlation contribution to the directional Compton profiles.

### A. Kohn-Sham LDA Compton profiles

In Fig. 1, we show the LDA momentum distribution along the [110] and [111] directions for a local ($s$ component) and a nonlocal ($s$ and $p$ components) pseudopotential. The effect of the lattice on the momentum distribution is more pronounced when using a nonlocal pseudopotential, yielding a bigger reduction below the Fermi break and a more significant contribution from the secondary Fermi surfaces (unklapp processes). For both the local and nonlocal pseudopotentials, the momentum distribution is strongly anisotropic and goes to zero after the first Fermi break since the Fermi surface of lithium is completely contained within the first Brillouin zone.

![](./images/811823003326218241_1.jpg)

FIG. 1. LDA momentum distribution in the [110] and [111] directions using a local and a nonlocal pseudopotential.

We find that the momentum distribution obtained with the nonlocal pseudopotential is in better qualitative agreement with our full-core calculations. Therefore, for a more realistic description of bcc lithium, we have to use a nonlocal pseudopotential even though this is computationally more demanding in QMC and introduces the additional locality approximation in DMC. $^{16}$

The agreement of the valence momentum distributions from a nonlocal pseudopotential and a full-core calculation is only qualitative because of the pseudopotential approximation (lack of correct orthogonalization between core and valence). When computing the momentum distribution within a pseudopotential scheme, we are underestimating the momentum distribution at high momenta and, consequently, overestimating it at low momenta. This effect is also evident in the Compton profiles.

In Fig. 2, the pseudopotential Compton profiles are compared with the valence profiles obtained with the full-core potential in the [100], [110], and [111] directions. As mentioned in Sec. II, we normalize the LDA Compton profiles to the number of valence electrons per unit cell, in this case one electron per unit cell. As expected, the Compton profiles constructed from valence orbitals correctly orthogonalized to the core orbitals show a higher tail at high momenta than the pseudopotential profiles and, since they must integrate to the same value, a significantly lower value at low momenta. The Compton profile of a free-particle system at the same density of lithium ($r_{s}=3.25$ a.u.) is an up-side down parabola terminating at $p_{\mathrm{F}}=0.5905$ a.u. Due to electron-ion correlation, the Kohn-Sham profiles develop a tail beyond $p_{\mathrm{F}}$ but the sharp features of the presence of a Fermi surface are clearly visible in any direction at about 0.6 a.u. The location of the Fermi break varies however for the different directions as a result of the already observed anisotropy (see Fig. 1). The

![](./images/811823003326218241_2.jpg)

FIG. 2. Valence Compton profiles of Li in the [100], [110], and [111] directions. The LDA Compton profiles constructed using the Troullier-Martins pseudopotential are compared with the LDA profiles obtained with the full-core $-3/r$ potential.

effect of secondary Fermi surfaces (unklapp processes) ap- pears both in the pseudopotential and full-core potential valence profiles. The effect is more pronounced in the [110] direction at about 0.8 a.u. and all profiles show an additional bump in the far tail (above 1.6 a.u.).

Within pseudopotential quantum Monte Carlo, we will compute a correction to the Compton profiles due to electronic correlations. This correction will be summed to the valence Compton profile from a full-core calculation to account properly for core-valence orthogonality.

### B. Quantum Monte Carlo Compton profiles

In order to calculate the correlation corrections to the Kohn-Sham Compton profiles of Fig. 2, we first determine the potential and wave function needed to correctly describe the momentum distribution of solid lithium within QMC. We start modeling bcc lithium with the simplest potential and wave function and improve upon that with a more sophisticated wave function and Hamiltonian.

The tests are conducted on a small simulation cell of 54 electrons and 54 lithium ions on a bcc lattice and with periodic boundary conditions. We carry out QMC calculations using the Troullier-Martins pseudopotential and test the use of a local ($s$ component) and a nonlocal ($s$ and $p$ components) pseudopotential as we have done within LDA density functional theory. For either potential, we employ both the free-electron orbitals $\phi_0$ [Eq. (5)] and LDA orbitals [Eq. (6)] determined with a plane-wave cutoff of 16 Ry. The Jastrow factor is separately optimized in each case using 2000 configurations within variance minimization. The VMC and DMC energies obtained with the nonlocal pseudopotential and the LDA orbitals are given by $E_{\text{VMC}}=-0.2524(1)$ Hartree and $E_{\text{DMC}}=-0.2591(1)$ Hartree.

![](./images/811823003326218241_3.jpg)

FIG. 3. VMC and DMC spherical momentum distribution for bcc lithium with a local (upper plot) and nonlocal (lower plot) pseudopotential and a simulation cell of 54 atoms with periodic boundary conditions. Either simple plane-wave ($\phi_0$) or LDA orbitals ($\phi_{\text{LDA}}$) are employed in the determinantal part of the wave function. The VMC momentum distribution for the electron gas is also shown. The statistical errors are smaller than the size of the symbols. The vertical dashed line indicates the position of $p_{\text{F}}$.

In Fig. 3, we show the spherical average of the momentum distribution in the case of local and nonlocal pseudopotentials. The VMC and DMC spherical momentum distribution for bcc lithium are compared with the VMC momentum distribution of the homogeneous electron gas at the same density ($r_s$=3.25 a.u.). The wave function for the electron gas is given by the product of a determinant of simple plane waves, $\phi_0$, and a Jastrow factor only containing the electron-electron term described in Sec. III. The momentum distribution of the electron gas shows a discontinuity at $p_{\text{F}}$. It is reduced below $p_{\text{F}}$ and develops a tail at high momenta with respect to the noninteracting step function. The persistence of a Fermi break and its location are consistent with the

Fermi-liquid behavior of the system. In the presence of an electron-ion pseudopotential, we have a further reduction of the size of the Fermi break due to electron-ion correlation. In all cases, the VMC and DMC momentum distribution are almost indistinguishable indicating that for this system the variational wave function is quite close to the fixed-node solution in describing this property.

For both local and nonlocal pseudopotentials, we test the use of free-electron orbitals, $\phi_0$, versus LDA orbitals. The use of orbitals given by a single plane wave is justified if the dependence of the periodic component of the Bloch states is not strongly varying with $\mathbf{k}$. This dependence can then be simply included in the Jastrow part as an electron-ion term, $\chi$ [Eq. (4)]. As shown in Fig. 3, this argument holds in the case of a local potential: the momentum distribution is not signifi- cantly different when using the orbitals $\phi_0$ or the LDA or bitals. On the other hand, free-electron orbitals in the deter- minant plus an electron-ion term in the Jastrow component give a poor description of electron-ion correlation when us- ing a nonlocal pseudopotential. LDA orbitals yield a larger reduction below the Fermi wave vector and the appearance of additional structure in the tail of the momentum distribu- tion as contribution from secondary Fermi surfaces. This ef- fect is smeared out because of spherical averaging and is more evident when plotting the momentum distribution along different directions.

Having identified the necessary features to describe bcc lithium (a nonlocal pseudopotential and LDA orbitals in the determinantal part of the wave function), we perform QMC calculations for larger systems and different boundary con- ditions to obtain higher resolution in momentum space. We consider two systems with 250 and 686 atoms and compute the VMC momentum distribution for four wave functions corresponding to $\Gamma$, $X$, $M$, and $R$ sampling of the cubic cell. For the system with 250 atoms, we also determine the mo- mentum distribution within DMC. The parameters used in the electron-ion Jastrow component of the four wave func- tions for both system sizes are the ones optimized for the 54-atom simulation cell.

As already explained, each $k$-point sampling defines a grid of allowed wave vectors and the QMC wave function is constructed from the orbitals with the lowest LDA energy. This procedure yields a different LDA Fermi energy $\epsilon_{\mathrm{F}}^{\mathbf{k}_{s}}$ and set of occupation numbers $f_{\mathbf{p}}^{\mathbf{k}_{s}}$ for each $k$-point sampling. The occupation $f_{\mathbf{p}}^{\mathbf{k}_{s}}$ is equal to two below $\epsilon_{\mathrm{F}}^{\mathbf{k}_{s}}$ and in general frac tional at the Fermi level. In the following, when comparing the LDA and QMC momentum distribution on the grid, we are referring to

$$
n_{\mathrm{LDA}}(\mathbf{p})=\left|c_{\mathbf{p}}\right|^{2} f_{\mathbf{p}}^{\mathbf{k}_{s}} \theta\left(\epsilon(\mathbf{p})-\epsilon_{\mathrm{F}}^{\mathbf{k}_{s}}\right), \quad(15)
$$

where $c_{\mathbf{p}}$ is the Fourier component of an LDA orbital and the momentum $\mathbf{p}$ is on the grid corresponding to $\mathbf{k}_{s}$ sampling. This ensures that both the LDA and the QMC momentum distribution satisfy the sum rule $\sum_{i} n(\mathbf{p}_{i})=N$ for each $k$-point sampling.

In Fig. 4, we plot the VMC and DMC momentum distri- butions in the [100], [110], and [111] directions for the 250- atom cell. The LDA distribution evaluated on the same $k$ vectors is also shown for comparison. The VMC and DMC results are quite close to each other with the DMC momen- tum distribution being slightly higher at low momenta and lower at high momenta than the VMC one. In the QMC distribution, we observe a reduction of the LDA momentum distribution below the Fermi wave vector, the persistence of the discontinuity and an enhancement at high momenta due to electron-electron correlation. The momentum distribution for lithium both in LDA and in QMC is strongly anisotropic.

![](./images/811823003326218241_4.jpg)

FIG. 4. VMC and DMC momentum distribution of bcc lithium in the [100], [110], and [111] directions. The statistical error is smaller than the size of the symbols. The momentum distribution is computed for a 250-atom cell and four different $k$-point samplings. The LDA momentum distribution evaluated at the same vectors is shown for comparison.

As explained in Sec. III, we want to define a reference momentum distribution such that its difference with the QMC distribution is a smoother function to integrate and Compton profiles with reduced finite size errors can be ob- tained. In Fig. 5, we show the difference of the QMC and LDA momentum distributions along the [110] direction for the 250-atom cell. This difference has smaller discontinuity than the original VMC or DMC data and its integral is less sensitive to finite-size errors. However, a yet better choice is to compute the following difference

$$
\Delta n^{\alpha}(\mathbf{p})=n_{\mathrm{QMC}}(\mathbf{p})-\alpha n_{\mathrm{LDA}}(\mathbf{p}), \quad(16)
$$

where the parameter $\alpha$ is chosen to reduce the size of the discontinuity in the function $\Delta n^{\alpha}$. To determine $\alpha$, we mini- mize the cost function

$$
\sum_{\mathbf{p}} \sum_{i=1}^{3}\left[\Delta n^{\alpha}(\mathbf{p})-\Delta n^{\alpha}\left(\mathbf{p}+d p_{i}\right)\right]^{2} n_{\mathrm{QMC}}(\mathbf{p})^{2}, \quad(17)
$$

where $d p_{i}$ is one grid spacing in the $x$, $y$, and $z$ directions.

For both the 250- and the 686-atom simulation cell, we find the optimal value of $\alpha=0.8$. In Fig. 5, $\Delta n^{\alpha}(\mathbf{p})$ is plot- ted in the [110] direction for the 250-atom system. $\Delta n^{\alpha}(\mathbf{p})$ is a more regular function to integrate with no significant

![](./images/811823003326218241_5.jpg)

FIG. 5. Difference $n_{\mathrm{VMC}}-n_{\mathrm{LDA}}$ and $n_{\mathrm{VMC}}-\alpha\ n_{\mathrm{LDA}}$ of the VMC and LDA momentum distribution. The momentum distribution is computed for a 250-atom cell and four different $k$-point samplings. The parameter $\alpha$ is equal to 0.8.

discontinuity and a similar behavior is observed in the [100] and [111] directions. We show below that this procedure of defining a reference momentum distribution is successful since it yields Compton profiles that lie on the same curve for the various system sizes (see Figs. 6 and 7).

To obtain the Compton profiles, we compute $\Delta J^{\alpha}(p)$ by integrating $\Delta n^{\alpha}(\mathbf{p})$ with the linear tetrahedron method. The momentum space is divided in cubes, the cubes in tetrahedra and a contribution to the integral from each tetrahedron is computed as in Appendix A. $\Delta J^{\alpha}(p)$ represents the correlation contribution to the Compton profile that is finally obtained as

![](./images/811823003326218241_6.jpg)

FIG. 6. Valence Compton profiles for lithium in the [100], [110], and [111] directions. The VMC results for the cell with 250 and 686 atoms and four $k$-point sampling are compared with the LDA valence profiles from a full-core calculation and the experimental results (Ref. 7).

![](./images/811823003326218241_7.jpg)

FIG. 7. Difference of the QMC and LDA valence Compton profiles for lithium in the [100], [110], and [111] directions. We show the VMC and DMC results for the cell with 250 atoms and the VMC results for the cell with 686 atom.

$$
J_{\mathrm{QMC}}(p)=\alpha J_{\mathrm{LDA}}(p)+\Delta J^{\alpha}(p), \tag{18}
$$

where $J_{\mathrm{LDA}}(p)$ is the LDA Compton profile. To take into account core-valence orthogonality properly, we add the correlation contribution $\Delta J^{\alpha}(p)$ to the LDA valence Compton profile obtained from a full-core calculation (see Fig. 2). $\Delta J^{\alpha}(p)$ is computed using a pseudopotential but, since it is the difference of results from two pseudopotential calculations (LDA and QMC), there is some degree of cancellation in the pseudopotential error. Even though we do not impose that $\Delta J^{\alpha}(p)$ is normalized to $(1-\alpha)$, as it would be for perfect sampling in momentum space, we find that the deviation in the normalization of $J_{\mathrm{QMC}}(p)$ from unity is very small. For instance, in the [111] direction, the error in normalization is only 0.08% and 0.16% for the 250- and 686-atom cell, respectively.

In Fig. 6, the VMC Compton profiles in the [100], [110], and [111] directions for the 250- and 686-atom cell are compared with the LDA valence profiles from the full-core calculation and the room-temperature experimental results by Sakurai *et al.*.⁷ The agreement between the simulations with 250 and 686 electrons implies that the differences between the QMC profiles and either the LDA or the experimental curves are beyond finite-size errors. Due to electron-electron interaction, the QMC profiles are lower at low momenta and higher at intermediate and high momenta than the LDA profiles. The experimental data, on the other hand, show opposite trends. They are lower than the QMC profiles below the Fermi wave vector and significantly higher in the intermediate and far tail. We do not convolute our results with the experimental resolution since the momentum resolution for the 250-atom simulation is only marginally better than the experimental resolution of 0.12 a.u. The continuum line for the QMC profiles is a result of the linear tetrahedron construction on $\Delta n^{\alpha}(\mathbf{p})$.

In Fig. 7, we show the difference of the QMC and LDA valence Compton profiles, $J_{\rm QMC}-J_{\rm LDA}$, in the [100], [110], and [111] directions, so details in the correlation corrections can be better appreciated. We plot the VMC and DMC results for the 250-atom cell and the VMC results for the 686-atom cell. The agreement between the results of the simulations with the two system sizes is quite good with the exception of the [100] direction at low momenta as a result of finite-size errors for the 250-atom cell. As already observed for the momentum distribution, the DMC results are only slightly higher at low momenta and lower at high momenta than the VMC ones. The difference of the LDA and QMC profiles is anisotropic. In the [100] and [111] directions, the QMC profiles do not show the sharp features of the LDA profiles at the Fermi break but are more rounded off and, consequently, their difference is peaked at the Fermi break.

If we assume a constant valence density corresponding to $r_s$=3.25 a.u. and employ the QMC momentum distribution we computed for the electron gas, the resulting Lam-Platzman corrections are in qualitative agreement with the QMC correlation corrections of Fig. 7. Consequently, given the large difference between the experimental results by Sakurai *et al.* and the QMC profiles, the Lam-Platzman corrections offer a satisfactory description of electronic correlation in QMC even though they are isotropic and cannot resolve the directional differences observed within QMC.

In disagreement with the $GW$ calculations, $^{10}$ the QMC results indicate that electronic correlation in lithium only accounts for about 30% of the discrepancy between experimental data and conventional band theoretical results. A similar conclusion has been obtained recently in a comparison of QMC and experimental Compton profiles for bulk silicon. $^{12}$ Other effects such as temperature $^{11}$ or the interpretation of experimental results (in particular, the validity of the impulse approximation $^{4,5}$) may explain the difference between experiments and QMC calculations. Our calculations also show that QMC cannot only offer a qualitative description of correlation effects in Compton profiles but, if finite-size errors are properly taken care of, also resolve directional differences in the correlation corrections to the LDA results and provide useful comparisons for new Compton scattering experiments. $^{2}$

## ACKNOWLEDGMENTS
This work was supported by NSF Grant No. DMR 9422496. We are grateful to Dr. Y. Sakurai for sending us the experimental results and to Professor Jose Luis Martins for giving us his plane-wave code. We thank Bernardo Barbiellini and P. Platzman for suggesting this project and for many useful discussions. C.F. also benefited from several discussions with Erik Koch, Keijo Hämäläinen, Aleksi Soininen, and Laurent Bellaiche. The calculations were performed at the National Center for Supercomputing Applications of the University of Illinois at Urbana-Champaign.

## APPENDIX A: LINEAR TETRAHEDRON METHOD
To determine the momentum distribution within Kohn-Sham density functional theory, the Kohn-Sham valence wave functions and eigenvalues are evaluated on a very fine grid of $k$ points within the irreducible wedge of the Brillouin zone. The Fourier coefficients of the orbitals with the corresponding eigenvalues are unfolded from the irreducible zone to full space and the momentum distribution is obtained by simply squaring the Fourier components. This procedure yields a square mesh with the momentum distribution and single-particle energy defined at each point.

To obtain the Compton profiles in a given direction, we integrate the momentum distribution using the linear tetrahedron method as described by Lehmann and Taut. $^{25}$ The expression for the Compton profile [Eq. (2)] is rewritten as
$$
J(\tilde{p})=\int d \mathbf{p} n(\mathbf{p}) \delta(\hat{\mathbf{q}} \cdot \mathbf{p}-\tilde{p}) \theta(\epsilon(\mathbf{p})-\epsilon_{\mathrm{F}}), \quad \text{(A1)}
$$
where $n(\mathbf{p})$ and $\epsilon(\mathbf{p})$ are the Kohn-Sham single-particle momentum distribution and energy and $\epsilon_{\mathrm{F}}$ the Fermi energy. The $\theta$ function is introduced to ensure that only states below the Fermi energy are included. If $n(\mathbf{p})$ and $\epsilon(\mathbf{p})$ have been computed on a square grid in momentum space, the mesh naturally divides space in cubes whose corners are defined by the grid points. Each cube is then divided in six tetrahedra and each tetrahedron is considered in turn. Within each tetrahedron, $n(\mathbf{p})$ and $\epsilon(\mathbf{p})$ are linearly interpolated. The step function $\theta(\epsilon(\mathbf{p})-\epsilon_{\mathrm{F}})$ may restrict the integration to only part of the tetrahedron: the primary tetrahedron is divided in secondary ones delimited by the boundaries $\epsilon(\mathbf{p})=\epsilon_{\mathrm{F}}$. For a given value of $\tilde{p}$, the surface of constant projection, $\hat{\mathbf{q}} \cdot \mathbf{p}$=$\tilde{p}$, is determined within each of the secondary tetrahedra and the contribution to $J(\tilde{p})$ is computed as the integral over this surface of the linear interpolation of the momentum distribution.

Before computing the Compton profiles, the Fermi energy $\epsilon_{\mathrm{F}}$ must be estimated. For a given value of the Fermi energy, we apply the linear tetrahedron construction to determine the volume delimited by the Fermi surface and iteratively change $\epsilon_{\mathrm{F}}$ so that
$$
\int d \mathbf{p} \theta(\epsilon(\mathbf{p})-\epsilon_{\mathrm{F}})=\frac{4 \pi}{3} p_{\mathrm{F}}^{3}, \quad \text{(A2)}
$$
where $p_{\mathrm{F}}$ is the Fermi momentum.

## APPENDIX B: FULL-CORE PLANE-WAVE LDA CALCULATIONS
As mentioned in Sec. IV, due to the lack of correct orthogonalization between core and valence, the pseudopotential momentum distribution is too low at high momenta and, consequently, too high at low momenta. To account for the correct oscillatory behavior of the valence wave functions, the valence orbitals are usually computed within traditional all-electron schemes (linearized augmented plane wave or linear muffin-tin orbital methods) or, alternatively, the true valence-wave functions are reconstructed from the pseudized orbitals. $^{26,27}$ On the other hand, several calculations in the literature have shown the feasibility of plane-wave calculations using the unscreened Coulomb potential for first-row elements. $^{19,28,29}$ We therefore decided to follow this more

<table>
<caption>TABLE I. Total energy of full-core bcc lithium versus the energy cutoff employed in the plane-wave calculation. The energy of full-core atomic lithium is $E_{\text{atom}}=-14.6682$ Ry. All energies are in Rydberg.</caption>
<thead>
  <tr>
    <th>$E_{\text{cutoff}}$</th>
    <th>$E_{\text{total}}$</th>
    <th>$\epsilon_{1s}$</th>
    <th>$\epsilon_{2s}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>300</td>
    <td>$-14.6277$</td>
    <td>$-2.7442$</td>
    <td>$-0.3102$</td>
  </tr>
  <tr>
    <td>400</td>
    <td>$-14.6886$</td>
    <td>$-2.7619$</td>
    <td>$-0.3086$</td>
  </tr>
  <tr>
    <td>1500</td>
    <td>$-14.7985$</td>
    <td>$-2.7948$</td>
    <td>$-0.3058$</td>
  </tr>
  <tr>
    <td>1800</td>
    <td>$-14.8032$</td>
    <td>$-2.7962$</td>
    <td>$-0.3057$</td>
  </tr>
</tbody>
</table>

straightforward route and adopt a plane-wave basis also with the $-3/r$ potential of lithium.

In Table I, we show the convergence in the total energy and the $1s$ and $2s$ eigenvalues at the $\Gamma$ point for full-core solid lithium as a function of plane-wave cutoff. For zone sampling to self-consistency, we used 14 special $k$ points. To obtain an accuracy of a few mRy on either the total energy or the $1s$ eigenvalue, plane-wave cutoffs higher than 1800 Ry are required. On the other hand, the convergence in valence properties such as the $2s$ level is achieved at significantly lower cutoffs.

Bellaiche and Kunc$^{28}$ obtained convergence in the structural properties of solid LiH with a plane-wave cutoff of the order of 200 Ry and the valence Compton profiles were in good agreement with the ones reconstructed by simply orthogonalizing the valence wave functions to a core atomic orbital. Similarly, we find that the valence orbitals of lithium are well converged at about 300 Ry and increasing the plane-wave cutoff to 400 Ry has a negligible effect on the valence Compton profiles.

## APPENDIX C: QUANTUM MONTE CARLO METHODS

The variance minimization method$^{20,21}$ consists of the minimization of the variance of the local energy over a set of $N_c$ configurations $\{R_i\}$ sampled from the square of the best wave function available before we start the optimization, $\Psi_0$:

$$
\sigma_{\mathrm{opt}}^{2}[\Psi]=\sum_{i}^{N_{c}}\left[\frac{\mathcal{H} \Psi\left(R_{i}\right)}{\Psi\left(R_{i}\right)}-E_{\text {guess }}\right]^{2} w\left(R_{i}\right) \bigg/ \sum_{i}^{N_{c}} w\left(R_{i}\right).
\tag{C1}
$$

$E_{\text{guess}}$ is a guess for the energy of the state we are interested in and $w(R_i)=|\Psi(R_i)/\Psi_0(R_i)|^2$. We do not allow the ratio of the weights to the average weight to exceed a maximum value.

We compute the expectation value of various operators both in variational and diffusion Monte Carlo. In VMC, configurations are sampled from $\Psi^2$ using Metropolis Monte Carlo method and the expectation value of a given operator $\mathcal{O}$ is obtained from

$$
\mathrm{O}_{\mathrm{VMC}}=\frac{1}{N} \sum_{i}^{N} \frac{\mathcal{O} \Psi\left(R_{i}\right)}{\Psi\left(R_{i}\right)}.
\tag{C2}
$$

The transition matrix consists of a drift-diffusion step with a time step optimized to minimize the autocorrelation time. In DMC, the imaginary time-evolution operator $\exp(-\mathcal{H}\tau)$ is used to project out the ground state from the trial wave function within the fixed-node and the short-time approximations.$^{30}$ The time-step error coming from the short-time approximation is negligible but the fixed-node error limits the accuracy of the results we obtain.

$^{1}$K. Hämäläinen, S. Manninen, C.-C Kao, W. Caliebe, J. B. Hastings, A. Bansil, S. Kaprzyk, and P. M. Platzman, Phys. Rev. B $\textbf{54}$, 5453 (1996).

$^{2}$K. Hämäläinen (private communication).

$^{3}$P. Eisenberger and P. M. Platzman, Phys. Rev. A $\textbf{2}$, 415 (1970).

$^{4}$P. Holm and R. Ribberfors, Phys. Rev. A $\textbf{40}$, 6251 (1989).

$^{5}$A. Issolah, B. Levy, A. Beswick, and G. Loupias, Phys. Rev. A $\textbf{38}$, 4509 (1988); A. Issolah, Y. Garreau, B. Levy, and G. Loupias, Phys. Rev. B $\textbf{44}$, 11 029 (1991); Solid State Commun. $\textbf{84}$, 1099 (1992).

$^{6}$P. Eisenberger, L. Lam, P. M. Platzman, and P. Schmidt, Phys. Rev. B $\textbf{6}$, 3671 (1972).

$^{7}$Y. Sakurai, Y. Tanaka, A. Bansil, S. Kaprzyk, A. T. Stewart, Y. Nagashima, T. Hyodo, S. Nanao, H. Kawata, and N. Shiotani, Phys. Rev. Lett. $\textbf{74}$, 2252 (1995).

$^{8}$W. Schülke, G. Stutz, F. Wohlert, and A. Kaprolat, Phys. Rev. B $\textbf{54}$, 14 381 (1996).

$^{9}$L. Lam and P. M. Platzman, Phys. Rev. B $\textbf{12}$, 5122 (1974).

$^{10}$Y. Kubo, J. Phys. Soc. Jpn. $\textbf{65}$, 16 (1996); $\textbf{66}$, 2236 (1997).

$^{11}$S. B. Dugdale and T. Jarlborg, Solid State Commun. $\textbf{105}$, 283 (1998).

$^{12}$B. Králik, P. Delaney, and S. G. Louie, Phys. Rev. Lett. $\textbf{80}$, 4253 (1998).

$^{13}$N. Troullier and J. L. Martins, Phys. Rev. B $\textbf{43}$, 1993 (1991).

$^{14}$H. J. Monkhorst and J. D. Pack, Phys. Rev. B $\textbf{13}$, 5188 (1976); $\textbf{16}$, 1748 (1977).

$^{15}$C. Blaas (unpublished).

$^{16}$S. Fahy, X. W. Wang, and S. G. Louie, Phys. Rev. Lett. $\textbf{61}$, 1631 (1988); M. M. Hurley and P. A. Christiansen, J. Chem. Phys. $\textbf{86}$, 1069 (1987); B. L. Hammond, P. J. Reynolds, and W. A. Lester, Jr., ibid. $\textbf{87}$, 1130 (1987); L. Mitáš, E. L. Schirley, and D. M. Ceperley, ibid. $\textbf{95}$, 3467 (1991); L. Mitáš, Phys. Rev. A $\textbf{49}$, 4411 (1994); J. C. Grossman and L. Mitáš, Phys. Rev. Lett. $\textbf{74}$, 1323 (1995).

$^{17}$V. Natoli and D. M. Ceperley, J. Comput. Phys. $\textbf{117}$, 171 (1995).

$^{18}$D. M. Ceperley, Phys. Rev. B $\textbf{18}$, 3126 (1978).

$^{19}$V. Natoli, R. M. Martin, and D. M. Ceperley, Phys. Rev. Lett. $\textbf{70}$, 1952 (1993); $\textbf{74}$, 1601 (1995).

$^{20}$C. J. Umrigar, K. G. Wilson, and J. W. Wilkins, Phys. Rev. Lett. $\textbf{60}$, 1719 (1988); in *Computer Simulation Studies in Condensed Matter Physics: Recent Developments*, edited by D. P. Landau and H. B. Schüttler (Springer-Verlag, Berlin, 1988).

$^{21}$R. L. Coldwell, Int. J. Quantum Chem., Symp. $\textbf{11}$, 215 (1977).

$^{22}$G. Rajagopal, R. J. Needs, S. D. Kenny, W. M. C. Foulkes, and A. James, Phys. Rev. Lett. $\textbf{73}$, 1959 (1994); Phys. Rev. B $\textbf{51}$, 10 591 (1995).

$^{23}$G. Ortiz, D. M. Ceperley, and R. M. Martin, Phys. Rev. Lett. $\textbf{71}$, 2777 (1993).

$^{24}$W. L. McMillan, Phys. Rev. **138**, A442 (1965).

$^{25}$G. Lehmann and M. Taut, Phys. Status Solidi B **54**, 469 (1972).

$^{26}$B. Meyer, K. Hummler, C. Elsässer, and M. Fähnle, J. Phys.:
Condens. Matter **7**, 9201 (1995).

$^{27}$P. Delaney, B. Králik, and S. G. Louie, Phys. Rev. B **58**, 4320
(1998).

$^{28}$L. Bellaiche and K. Kunc, Phys. Rev. B **55**, 5006 (1997); Int. J.
Quantum Chem. **61**, 647 (1997).

$^{29}$M. Teter, Phys. Rev. B **48**, 5031 (1993).

$^{30}$J. B. Anderson, J. Chem. Phys. **63**, 1499 (1975); **65**, 4121 (1976);
P. J. Reynolds, D. M. Ceperley, B. J. Alder, and W. A. Lester,
ibid. **77**, 5593 (1982); J. W. Moskowitz, K. E. Schmidt, M. A.
Lee, and M. H. Kalos, ibid. **77**, 349 (1982).