PAPER • OPEN ACCESS

# Finite-size effects in cylindrical topological insulators

To cite this article: Michele Governale et al 2020 New J. Phys. 22 063042

View the [article online] for updates and enhancements.

This content was downloaded from IP address 2.57.76.76 on 25/06/2020 at 04:03

# New Journal of Physics
The open access journal at the forefront of physics
![](./images/812640031339446274_1.jpg)

## PAPER

# Finite-size effects in cylindrical topological insulators

Michele Governale¹,⁵, Bibek Bhandari², Fabio Taddei³, Ken-Ichiro Imura⁴ and Ulrich Zülicke¹

¹ School of Chemical and Physical Sciences and MacDiarmid Institute for Advanced Materials and Nanotechnology, Victoria University of Wellington, PO Box 600, Wellington 6140, New Zealand
² Scuola Normale Superiore and NEST, Istituto Nanoscienze-CNR, I-56126 Pisa, Italy
³ NEST, Istituto Nanoscienze-CNR and Scuola Normale Superiore, I-56126 Pisa, Italy
⁴ Department of Quantum Matter, AdSM, Hiroshima University, Higashi-Hiroshima 739-8530, Japan
⁵ Author to whom any correspondence should be addressed.

E-mail: michele.governale@vuw.ac.nz

Keywords: topological insulators, nanowires, optical transitions

## Abstract
We present a theoretical study of a nanowire made of a three-dimensional topological insulator. The bulk topological insulator is described by a continuum-model Hamiltonian, and the cylindrical-nanowire geometry is modelled by a hard-wall boundary condition. We provide the secular equation for the eigenergies of the systems (both for bulk and surface states) and the analytical form of the energy eigenfunctions. We describe how the surface states of the cylinder are modified by finite-size effects. In particular, we provide a $1/R$ expansion for the energy of the surface states up to second order. The knowledge of the analytical form for the wavefunctions enables the computation of matrix elements of any single-particle operators. In particular, we compute the matrix elements of the optical dipole operator, which describe optical absorption and emission, treating intra- and inter-band transition on the same footing. Selection rules for optical transitions require conservation of linear momentum parallel to the nanowire axis, and a change of 0 or $\pm 1$ in the total-angular-momentum projection parallel to the nanowire axis. The magnitude of the optical-transition matrix elements is strongly affected by the finite radius of the nanowire.

## 1. Introduction
Three-dimensional (3D) topological insulators (TIs) were predicted in 2007 [1] as electronic systems characterized by an insulating bulk and gapless conducting surface states (for a review, see references [2–5]). The states at the interface between the system and the vacuum are topologically protected against time-reversal invariant perturbations and consist, at low energy, of two-dimensional Dirac fermions [6–8]. Recent advances in nanofabrication techniques have enabled the realization of 3D-TI samples of reduced dimensionality, for example in the form of nanowires [9–26]. 3D-TI nanowires proximised with an s-wave superconductor have been proposed as a possible platform for the realization of Majorana bound states [27, 28]. The availability of nanometer-scale samples is interesting also because it offers the opportunity to investigate the competition between the inverted bulk gap and the size-quantisation energy as well as the extent of the localization of surface states [29–38]. In reference [29], an approximate analytic model supplemented by a numerical scheme based on exact diagonalisation was introduced to study the quantum interference effects on the low-energy spectrum of $Bi_2Se_3$ nanowires.

In this paper we explore the properties of a finite-radius 3D-TI cylinder, using the envelope-function description of the TI bulk band structure developed in references [39, 40]. Our goal is to determine the dependence of its energy spectrum and eigenfunctions on the radius $R$. The central point of our analysis is the analytical expression of the eigenfunctions, which allow us to express cylindrical hard-wall boundary conditions in terms of secular equations that can be approximated in the limit of large radii: we obtain

© 2020 The Author(s). Published by IOP Publishing Ltd on behalf of the Institute of Physics and Deutsche Physikalische Gesellschaft

<table>
<caption>Table 1. Values for parameters in the effective continuum-model Hamiltonian describing bulk-electronic states of currently available topological-insulator materials, from reference [41].</caption>
<thead>
<tr>
<th>
</th>
<th>
Bi₂Se₃
</th>
<th>
Bi₂Te₃
</th>
<th>
Sb₂Te₃
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$m_0$ (eV)
</td>
<td>
$-0.169$
</td>
<td>
$-0.296$
</td>
<td>
$-0.182$
</td>
</tr>
<tr>
<td>
$m_1$ (eV Å²)
</td>
<td>
$3.353$
</td>
<td>
$9.258$
</td>
<td>
$22.136$
</td>
</tr>
<tr>
<td>
$m_2$ (eV Å²)
</td>
<td>
$29.375$
</td>
<td>
$177.355$
</td>
<td>
$51.320$
</td>
</tr>
<tr>
<td>
$B$ (eV Å)
</td>
<td>
$1.836$
</td>
<td>
$0.900$
</td>
<td>
$1.174$
</td>
</tr>
<tr>
<td>
$A$ (eV Å)
</td>
<td>
$2.513$
</td>
<td>
$4.003$
</td>
<td>
$3.694$
</td>
</tr>
</tbody>
</table>

approximate expressions for the eigenenergies up to second order in $1/R$. The analytical functional form of the eigenfunctions, which is valid irrespective of the radius of the wire, enables the calculation of the matrix elements of any observable. As an example, we consider the dipole matrix elements for optical transitions. In particular, we find that the selection rules for absorption and emission are not modified by a finite radius, in contrast to the case of a spherical nanoparticle [36]. Numerical results are presented for three different materials, namely Bi₂Se₃, Bi₂Te₃, and Sb₂Te₃, which show qualitatively different behaviours. We compute eigenenergies as functions of the radius $R$ and longitudinal momentum and compare them with approximate large-radius expressions. The eigenenergies are found to be oscillating for small values of $R$, especially in the case of Bi₂Te₃. Moreover, we characterize the behaviour of eigenfunctions by plotting the average radial coordinate and the corresponding variance as a function of the radius $R$. As expected, the average coordinate moves towards the centre of the nanowire for small values of $R$, more rapidly for Bi₂Te₃ than for Bi₂Se₃, while the variance increases in an oscillating fashion for increasing radii, reaching the asymptotic value more rapidly in the case of Bi₂Se₃ with respect to Bi₂Te₃. Finally, we calculate numerically the dependence of the optical dipole matrix elements on the radius finding quantitative important changes with respect to the bulk situation.

The paper is organized as follows. In section 2, we present an analytic treatment for a cylindrical 3D-TI nanowire with hard-wall confinement. We conclude section 2 with a complete analytic expression for the eigenfunction of the finite-radius 3D-TI. In section 3, we study the finite size effects on the topological properties of a cylindrical 3D-TI for two different materials. Specifically, we study the eigenenergies and characterise the eigenfunctions of the system as a function of the radius of the cylinder. Finally, in section 3.3, we calculate the optical dipole matrix elements of a cylindrical TI and study their dependence on the the radius of the cylinder.

## 2. Model

We consider an infinitely long cylinder of TI of radius $R$, whose axis is in the $z$-direction. The bulk TI is described by the Hamiltonian [39, 40]

$$
H_{0}=\left(\begin{array}{cccc}
m(\mathbf{p}) & B p_{z} & 0 & A p_{-} \\
B p_{z} & -m(\mathbf{p}) & A p_{-} & 0 \\
0 & A p_{+} & m(\mathbf{p}) & -B p_{z} \\
A p_{+} & 0 & -B p_{z} & -m(\mathbf{p})
\end{array}\right),
\tag{1}
$$

where $\mathbf{p}=(p_{x}, p_{y}, p_{z})$ is the momentum operator, $m(\mathbf{p})=m_{0}+m_{1} p_{z}^{2}+m_{2}(p_{x}^{2}+p_{y}^{2})$ is the mass term and $p_{\pm}=p_{x} \pm i p_{y}$. The effective Hamiltonian equation (1) is written in the basis of the four states closest to the Fermi energy at the $\Gamma$ point, $\{|P1_{z}^{+}\uparrow\rangle,|P2_{z}^{-}\uparrow\rangle,|P1_{z}^{+}\downarrow\rangle,|P2_{z}^{-}\downarrow\rangle\}$, where the label $P1(2)_{z}$ indicates that they stem from atomic $p_{z}$ orbitals of the two different atoms in the material and the superscript $\pm$ refers to their parity [39, 40]. When the sign of $m_{0}/m_{2}$ is negative, the material is in the topological insulating phase, causing isolated boundaries to host surfaces states represented by gapless Dirac cones. The coefficients $m_{0}$, $m_{1}$ and $m_{2}$, as well as the coefficients $A$ and $B$ of the linear-momentum terms depend on the material [41]. The values of the parameters for the most common TIs are reported in table 1. As the system has cylindrical symmetry, it is convenient to express $H_{0}$ in cylindrical coordinates. Following Imura et al [42], we write the Hamiltonian as a sum of two terms

$$
H_{0}=H_{\perp}+H_{\parallel},
\tag{2}
$$

where

$$
H_{\perp}=\left(\begin{array}{cccc}
m_{\perp} & 0 & 0 & -i A \mathrm{e}^{-\mathrm{i} \varphi} \partial_{\rho} \\
0 & -m_{\perp} & -i A \mathrm{e}^{-\mathrm{i} \varphi} \partial_{\rho} & 0 \\
0 & -i A \mathrm{e}^{\mathrm{i} \varphi} \partial_{\rho} & m_{\perp} & 0 \\
-i A \mathrm{e}^{\mathrm{i} \varphi} \partial_{\rho} & 0 & 0 & -m_{\perp}
\end{array}\right)
\tag{3a}
$$

$$
H_{\|}=\left(\begin{array}{cccc}
m_{\|} & B p_{z} & 0 & -\frac{A}{\rho} \mathrm{e}^{-\mathrm{i} \varphi} \partial_{\varphi} \\
B p_{z} & -m_{\|} & -\frac{A}{\rho} \mathrm{e}^{-\mathrm{i} \varphi} \partial_{\varphi} & 0 \\
0 & \frac{A}{\rho} \mathrm{e}^{\mathrm{i} \varphi} \partial_{\varphi} & m_{\|} & -B p_{z} \\
\frac{A}{\rho} \mathrm{e}^{\mathrm{i} \varphi} \partial_{\varphi} & 0 & -B p_{z} & -m_{\|}
\end{array}\right)
\tag{3b}
$$

and with the mass terms given by the expressions

$$
m_{\perp}=m_{0}+m_{2}\left(-\partial_{\rho}^{2}-\frac{1}{\rho} \partial_{\rho}\right)
\tag{4}
$$

$$
m_{\|}=-m_{2} \frac{1}{\rho^{2}} \partial_{\varphi}^{2}+m_{1} p_{z}^{2}.
\tag{5}
$$

The Hamiltonian $H_{0}$ commutes both with $p_{z}$ and with the $z$-component of the total angular momentum $(L_{z}+\frac{\hbar}{2} \sigma_{z}) \otimes \tau_{0}$, where $\tau_{0}$ is the identity matrix in the orbital pseudo-spin subspace. In the following, to avoid cluttering the notation, we set $\hbar=1$. The commutation relations of $H_{0}$ discussed above suggest the following Ansatz for the wave function:

$$
\Psi(\rho, \varphi, z)=\frac{\mathrm{e}^{\mathrm{i} k_{z} z}}{\sqrt{2 \pi}}\left(\begin{array}{c}
\Phi_{1}(\rho) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
\Phi_{2}(\rho) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
\Phi_{3}(\rho) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi} \\
\Phi_{4}(\rho) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi}
\end{array}\right),
\tag{6}
$$

where $k_{z}$ is the eigenvalue of $p_{z}$ and $j$ (half integer) the eigenvalue of the $z$ component of the total angular momentum. Solving the eigensystem requires applying the Hamiltonian equation (1) to the wavefunciton in equation (6). The calculation is detailed in appendix A. In order to solve the radial part of the eigensystem, we make further Ansatze for the $\Phi_{i}(\rho)$ and rewrite equation (6) as

$$
\Psi(\rho, \varphi, z)=\frac{\mathrm{e}^{\mathrm{i} k_{z} z}}{\sqrt{2 \pi}}\left(\begin{array}{c}
c_{1} J_{j-\frac{1}{2}}(\kappa \rho) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
c_{2} J_{j-\frac{1}{2}}(\kappa \rho) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
c_{3} J_{j+\frac{1}{2}}(\kappa \rho) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi} \\
c_{4} J_{j+\frac{1}{2}}(\kappa \rho) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi}
\end{array}\right),
\tag{7}
$$

where $J_{n}(z)$ is a Bessel function of the first kind and $\kappa$ and the coefficients $c_{1}, \ldots, c_{4}$ need to be determined. In order for the Ansatz of equation (7) to be an eigenfunction of $H_{0}$ with energy $E$, the parameter $\kappa$ needs to take one of the following two values

$$
\kappa_{ \pm}=\left[-\left(\frac{m_{0}}{m_{2}}+\frac{A^{2}}{2 m_{2}^{2}}+\frac{m_{1}}{m_{2}} k_{z}^{2}\right) \pm \sqrt{\frac{A^{4}}{4 m_{2}^{4}}+\frac{E^{2}}{m_{2}^{2}}+\frac{A^{2} m_{0}}{m_{2}^{3}}+\left(\frac{A^{2}}{m_{2}^{2}} \frac{m_{1}}{m_{2}}-\frac{B^{2}}{m_{2}^{2}}\right) k_{z}^{2}}\right]^{1 / 2}.
\tag{8}
$$

For the coefficients $\left(c_{1}, c_{2}, c_{3}, c_{4}\right)^{T}$ there are four independent solutions (two for $\kappa_{+}$and two for $\kappa_{-}$) given by

$$
\left(\frac{i A \kappa_{ \pm}}{\Delta_{ \pm}}, 0, \frac{B k_{z}}{\Delta_{ \pm}}, 1\right)^{\mathrm{T}}, \quad\left(-\frac{B k_{z}}{\Delta_{ \pm}}, 1,-\frac{i A \kappa_{ \pm}}{\Delta_{ \pm}}, 0\right)^{\mathrm{T}},
\tag{9}
$$

where $\Delta_{ \pm}=m_{2} \kappa_{ \pm}^{2}+m_{1} k_{z}^{2}+m_{0}-E$. The general solution for the wavefunction with quantum numbers $k_{z}, j$ and $E$ is a linear combination of the four independent solutions obtained above:


$$
\Psi(\rho, \varphi, z)=\frac{\mathrm{e}^{\mathrm{i} k_{z} z}}{\sqrt{2 \pi}} \sum_{\eta= \pm}\left\{\alpha_{\eta}\left(\begin{array}{c}
\frac{i A \kappa_{\eta}}{\Delta_{\eta}} J_{j-\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
0 \\
\frac{B k_{z}}{\Delta_{\eta}} J_{j+\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi} \\
J_{j+\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi}
\end{array}\right)+\beta_{\eta}\left(\begin{array}{c}
-\frac{B k_{z}}{\Delta_{\eta}} J_{j-\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
J_{j-\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
-\frac{i A \kappa_{\eta}}{\Delta_{\eta}} J_{j+\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi} \\
0
\end{array}\right)\right\}.
$$

We can now solve the confinement problem by assuming a hard-wall cylindrical confinement potential of radius $R$. We need to impose the boundary condition $\Psi(R, \varphi, z)=0$. This leads to as system of equations for the coefficients $\alpha_{\eta}$ and $\beta_{\eta}$ which has non-trivial solutions for energies obeying the secular equation

$$
\frac{T_{j}\left(\kappa_{+} R\right)}{T_{j}\left(\kappa_{-} R\right)}+\frac{T_{j}\left(\kappa_{-} R\right)}{T_{j}\left(\kappa_{+} R\right)}=\frac{\kappa_{+} \Delta_{-}}{\kappa_{-} \Delta_{+}}+\frac{\kappa_{-} \Delta_{+}}{\kappa_{+} \Delta_{-}}+\frac{B^{2}}{A^{2}} k_{z}^{2} \frac{\left(\Delta_{+}-\Delta_{-}\right)^{2}}{\kappa_{+} \kappa_{-} \Delta_{+} \Delta_{-}},
$$

where we have defined the function $T_{j}(z)=\frac{J_{j+1 / 2}(z)}{J_{j-1 / 2}(z)}$. A detailed derivation of the secular equation is provided in appendix A. In the case $k_{z}=0$, the problem decouples in two $2 \times 2$ problems and we have two independent secular equations

$$
\frac{\kappa_{+} \Delta_{-}}{\kappa_{-} \Delta_{+}}=\frac{T_{j}\left(\kappa_{+} R\right)}{T_{j}\left(\kappa_{-} R\right)},
$$

$$
\frac{\kappa_{+} \Delta_{-}}{\kappa_{-} \Delta_{+}}=\frac{T_{j}\left(\kappa_{-} R\right)}{T_{j}\left(\kappa_{+} R\right)},
$$

which are analogous to equation (28) of reference [36]. The $k_{z}=0$ energy eigenstates associated with solutions of equation (12a) have $\beta_{\eta}=0$ and therefore their only nonvanishing spinor components are the first and the fourth. Conversely, the eigenstates corresponding to solutions of equation (12b) have $\alpha_{\eta}=0$ and therefore their only nonvanishing spinor components are the second and the third. Taking into account the transformation properties of the basis states under spatial inversion, it is straightforward to show that eigenstates associated with energy eigenvalues arising from the secular equation (12a) [(12b)] are also parity eigenstates with eigenvalue $(-1)^{j-\frac{1}{2}}\left[(-1)^{j+\frac{1}{2}}\right]$. Even for finite $k_{z}$, the spinors multiplied by $\alpha_{\eta}$ $\left[\beta_{\eta}\right]$ in the Ansatz (10) remain parity eigenstates with eigenvalue $(-1)^{j-\frac{1}{2}}\left[(-1)^{j+\frac{1}{2}}\right]$. However, as the energy eigenstates for nonzero $k_{z}$ are superpositions of these opposite-parity spinors, they are not eigenstates of parity.

Once we fix the quantum number $j$ and $k_{z}$ and solve the secular equation (11) we obtain a series of solutions both with positive and negative energies. Of these, we will only consider the two, one positive and one negative, with the smallest absolute value of the energy. We will indicate the positive(negative)-energy solution with $s=+(-) .{ }^{6}$ Furthermore, we will restrict our analysis to energies that lie within the bulk gap. The quantum numbers that we will use to label the states are $s= \pm, j, k_{z}$. The secular problem yields the full knowledge of the eigenfunctions. In order to simplify the notation, in the following we rewrite the eigenfunction equation (10) as

$$
\Psi_{s, j, k_{z}}(\rho, \varphi, z)=\frac{\mathrm{e}^{\mathrm{i} k_{z} z}}{2 \pi}\left(\begin{array}{c}
\Phi_{1, s, j, k_{z}}(\rho) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
\Phi_{2, s, j, k_{z}}(\rho) \mathrm{e}^{\mathrm{i}\left(j-\frac{1}{2}\right) \varphi} \\
\Phi_{3, s, j, k_{z}}(\rho) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi} \\
\Phi_{4, s, j, k_{z}}(\rho) \mathrm{e}^{\mathrm{i}\left(j+\frac{1}{2}\right) \varphi}
\end{array}\right),
$$

where the wavefunction obeys the normalisation condition $\sum_{i=1}^{4} \int_{0}^{R} \mathrm{~d} \rho \rho\left|\Phi_{i, s, j, k_{z}}(\rho)\right|^{2}=1$.

### 3. Results

In order to understand the effect of a finite radius of the cylinder and how it affects the topologically protected surface states, we start from the large-radius limit.

${ }^{6}$ In principle, we could introduce another integer quantum number to label the different solutions as in the case of a particle in a box.

### 3.1. Large-radius expansion
A natural length scale in this context is the effective Compton length $R_0 = \left| \frac{A}{m_0} \right|$. In the following we perform an expansion in $R_0/R$ and find corrections to the asymptotic (large $R$) results obtained by Imura *et al* [42]. To this aim, we make use of Hankel's asymptotic expansion for the Bessel function [43]

$$
J_{n}(z) \approx \sqrt{\frac{2}{\pi z}}\left[P(n, z) \cos \left(z-\frac{1}{2} n \pi-\frac{1}{4} \pi\right)-Q(n, z) \sin \left(z-\frac{1}{2} n \pi-\frac{1}{4} \pi\right)\right]. \tag{14}
$$

The functions $P(n,z)$ and $Q(n,z)$ are power series of $1/z$.

#### 3.1.1. Zero axial momentum
We start by considering the case of zero axial momentum $(k_z = 0)$, with the goal to understand the $j$-dependence of the surface states. We will consider only one of the two secular equations, namely equation (12a) which can be recast as

$$
\kappa_{+} \Delta_{-} J_{j-\frac{1}{2}}\left(\kappa_{+} R\right) J_{j+\frac{1}{2}}\left(\kappa_{-} R\right)-\kappa_{-} \Delta_{+} J_{j+\frac{1}{2}}\left(\kappa_{+} R\right) J_{j-\frac{1}{2}}\left(\kappa_{-} R\right)=0. \tag{15}
$$

For realistic materials, see table 1, and small values of energies $E \ll |m_0|$, $\kappa_{\pm} = k \pm iq$ with $q > 0$. In the large-radius limit $qR \gg 1$, we keep only the terms proportional to $\exp(qR)$ in equation (14). The secular equation reduces to

$$
\begin{aligned}
& \kappa_{+} \Delta_{-}\left[P\left(j-\frac{1}{2}, \kappa_{+} R\right)-i Q\left(j-\frac{1}{2}, \kappa_{+} R\right)\right]\left[P\left(j+\frac{1}{2}, \kappa_{-} R\right)+i Q\left(j+\frac{1}{2}, \kappa_{-} R\right)\right]= \\
& -\kappa_{-} \Delta_{+}\left[P\left(j-\frac{1}{2}, \kappa_{-} R\right)+i Q\left(j-\frac{1}{2}, \kappa_{-} R\right)\right]\left[P\left(j+\frac{1}{2}, \kappa_{+} R\right)-i Q\left(j+\frac{1}{2}, \kappa_{+} R\right)\right].
\end{aligned} \tag{16}
$$

Taking the zeroth order of the Hankel's expansion (i.e. $P(n,z)=1$ and $Q(n,z)=0$), the secular equation becomes

$$
\kappa_{+} \Delta_{-}+\kappa_{-} \Delta_{+}=0. \tag{17}
$$

This equation has a zero-energy solution if $m_0/m_2 < 0$, i.e. when the system is in the topological phase.

Next, we consider the next two terms in the Hankel's expansion, that is $P(n,z) = 1 - (4n^2 - 1)(4n^2 - 9)/(128z^2)$ and $Q(n,z) = (4n^2 - 1)/(8z)$, and insert them into equation (16). After some tedious but otherwise standard algebra, we obtain the eigenenergies up to second-order in $R_0/R$

$$
E=A \frac{j}{R}-\frac{A^{2}}{2 m_{0}} \frac{j}{R^{2}}. \tag{18}
$$

The first term is in agreement with reference [42], the second term gives the first correction to the asymptotic result. The other solution, with the opposite sign, $E = -Aj/R + \frac{A^2}{2m_0}\frac{j}{R^2}$ arises from solving equation (12b). The values of $\kappa_{\pm}$ corresponding to the energies in equation (18) can be found by inserting equation (18) in equation (8) and setting $k_z = 0$.

#### 3.1.2. Finite axial momentum
In this section we assume that $k_z R \gg 1$. Proceeding in the same way as for case $k_z = 0$, in zeroth-order in $R_0/R$ the secular equation for the case of non-zero axial momentum reduces to

$$
\left(\kappa_{+} \Delta_{-}+\kappa_{-} \Delta_{+}\right)^{2}+\frac{B^{2}}{A^{2}} k_{z}^{2}\left(\Delta_{+}-\Delta_{-}\right)^{2}=0. \tag{19}
$$

This equation has the solutions

![](./images/812640031339446274_2.jpg)

$$
E = \pm Bk_{z}, \tag{20}
$$

which represents the linear dispersion of the surface modes.

Considering the Hankel's expansion up to terms in $1/z^{2}$, that is $P(n,z)=1-(4n^{2}-1)(4n^{2}-9)/(128z^{2})$ and $Q(n,z)=(4n^{2}-1)/(8z)$, we obtain the eigenenergies up to second order in $R_{0}/R$

$$
E = \pm \left( Bk_{z} + \frac{1}{2} \frac{A^{2}j^{2}}{Bk_{z}R^{2}} \right), \tag{21}
$$

which corresponds to the Taylor expansion in second order in $1/(k_{z}R)$ of the result by Imura *et al* [42], $E=\pm\sqrt{B^{2}k_{z}^{2}+A^{2}j^{2}/R^{2}}$. Notice that we are not allowed to take the $k_{z}\to0$ limit, as this result has been derived assuming $k_{z}\gg1/R$. The values of $\kappa_{\pm}$ corresponding to the energies in equation (21) can be found by inserting equation (21) in equation (8).

### 3.2. Numerical results
In this section we present numerical results for three different materials, namely $\text{Bi}_{2}\text{Se}_{3}$, $\text{Bi}_{2}\text{Te}_{3}$, and $\text{Sb}_{2}\text{Te}_{3}$, using the parameters of table 1. We use the following units for length and momentum, respectively,

$$
R_{0} = \left| \frac{A}{m_{0}} \right| \quad \text{and} \quad k_{0} = \left| \frac{m_{0}}{B} \right|,
$$

where $R_{0}=1.49$ nm for $\text{Bi}_{2}\text{Se}_{3}$, $1.35$ nm for $\text{Bi}_{2}\text{Te}_{3}$, and $2.03$ nm for $\text{Sb}_{2}\text{TE}_{3}$.

Figure 1 shows how the eigenenergies in units of $E_{R}=A/R$ depend on the radius of the cylinder for the three materials and for three different values of $j$. Here we show only the positive energies, that is $s=+$. Solid curves refer to the exact result obtained by solving equation (12), while the dashed curves refer to the large-radius analytic expression equation (18). We observe that the latter solutions approximate well the numerical results when $R\gtrsim6R_{0}$ for $\text{Bi}_{2}\text{Se}_{3}$ and $\text{Sb}_{2}\text{Te}_{3}$, and when $R\gtrsim20R_{0}$ for $\text{Bi}_{2}\text{Te}_{3}$, respectively. For $\text{Bi}_{2}\text{Se}_{3}$ and $\text{Sb}_{2}\text{Te}_{3}$ it is worthwhile noticing that at $R=6R_{0}$, especially for $j=3/2$ and $5/2$, the normalized eigenenergies have not yet reached the asymptotic ($R\gg R_{0}$) value (represented by the thin solid lines, see equation (18)). On the other hand, when the radius of the cylinder is small, figure 1 shows an oscillatory behaviour, especially in the case of $\text{Bi}_{2}\text{Te}_{3}$, that is more pronounced for smaller values of $j$, similarly to a spherical nanoparticle [36]. For $\text{Bi}_{2}\text{Te}_{3}$, the effect of these oscillations are so large that, for some values of the radius, the surface-state energy goes to zero. For these values of the radius the two states $s=\pm$ become degenerate, the degeneracy is preserved by the fact that they have opposite parity. This oscillatory behaviour is a consequence of the fact that the wavefunction is no longer localized on

![](./images/812640031339446274_3.jpg)

![](./images/812640031339446274_4.jpg)

the surface of the cylinder. We conclude that $Bi_2Te_3$ is the ideal candidate material to observe finite size effects in TI nanowires. The oscillations are consistent with the results of reference [29] (see also appendix B). The similarity between the results presented here and the corresponding results for a spherical nanoparticle is not surprizing, as for $k_z=0$ the system is equivalent to a disk, i.e., the twodimensional sphere, and the basic structure of the secular equation mirrors that for a sphere in three dimensions. In particular, energy eigenstates are also parity eigenstates as for the spherical nanoparticle. This ceases to be the case for $k_z\neq0$.

In figure 2 we show the positive eigenenergies, divided by the asymptotic value $E_{R,j,k_z}=\sqrt{B^2k_z^2+A^2j^2/R^2}$, as a function of wavevector $k_z$. Finite-size effects appear in this plot as deviations from unity of the normalized eigenenergies and are more pronounced form small values of $k_z$.

Since we have the full knowledge of the eigenfunctions, we can calculate the expectation values of any single-particle operator. The average of the radial coordinate in the state $\Psi_{s,j,k_z}$ is simply given by

$$
\langle\rho\rangle_{s,j,k_z}=\sum_{i=1}^{4}\int_{0}^{R}\mathrm{d}\rho\,\rho^{2}\left|\Phi_{i,s,j,k_z}(\rho)\right|^{2},
\tag{22}
$$

and its variance by

$$
\mathcal{D}\rho_{s,j,k_z}=\sqrt{\langle\rho^{2}\rangle_{s,j,k_z}-\langle\rho\rangle_{s,j,k_z}^{2}}.
\tag{23}
$$

Figure 3 (top panels) shows that the average of the radial coordinate, $\langle\rho\rangle_{s,j,k_z}$, approaches $R$ for large values of the radius as expected for topologically-protected surface states. The average of the radial position for both materials increases monotonically with the radius of the cylinder, showing weak oscillations only for the case of $Bi_2Te_3$. As shown in figure 3 (bottom panels), the variance in itself approaches, in an

oscillatory fashion, a constant value of the order of $R_0$ for large values of radius (the variance varies very little for $R \gtrsim 8R_0$ for ${\rm Bi_2Se_3}$ and $R \gtrsim 24R_0$ for ${\rm Bi_2Te_3}$). Since the value of $R_0$ is similar for the two materials ($R_0 = 1.5$ nm for ${\rm Bi_2Se_3}$ and $R_0 = 1.35$ nm for ${\rm Bi_2Te_3}$), we can conclude that in ${\rm Bi_2Se_3}$ the asymptotic form of the surface states is reached for smaller values of the radius compared to ${\rm Bi_2Te_3}$.

### 3.3. Optical transitions in cylindrical topological insulators
In typical semiconductor nanostructures, optical transitions between size-quantized levels can be neatly categorized as being either intra-band or inter-band transitions [44]. In the narrow-gap materials of interest for our present work, however, these two types of transitions are not well-separated in energy and need to be treated on the same footing. A versatile formalism for calculating all optical-transition matrix elements in such systems using the envelope part of the confined-charge-carrier wave functions was developed in reference [36]. Here we recall the basic features of this approach before applying it to the case of cylindrical TI nanowires.

Optical transitions are mediated by matrix elements of the electric-dipole operator $\mathbf{d}$, which can be written as the sum of intra- and inter-band contributions [36, 44]

$$
\mathbf{d} = \mathbf{d}^{(\text{intra})} + \mathbf{d}^{(\text{inter})} \quad . \tag{24}
$$

The intra-band part $\mathbf{d}^{(\text{intra})} \equiv e\mathbf{r} \mathbb{1}$ pertains to transitions between size-quantized states within the same band, i.e., envelope wave functions multiplying the same basis state in $\mathbf{k} \cdot \mathbf{p}$ space. In contrast, the inter-band part $\mathbf{d}^{(\text{inter})}$ accounts for optical transitions between different bands, i.e., different $\mathbf{k} \cdot \mathbf{p}$ basis states, whose magnitude is renormalized by the overlap of associated envelope wave-function components. Calculation of $\mathbf{d}^{(\text{inter})}$ within the envelope-function formalism is aided by a fundamental relationship of the electric-dipole matrix elements between $\mathbf{k} \cdot \mathbf{p}$ basis states with coefficients of the linear-in-$\mathbf{k}$ terms appearing in the multi-band envelope-function Hamiltonian $H_0$. More specifically, writing $H_0$ from equation (1) as

$$
H_0 = \left[ m_0 + m_1 k_z^2 + m_2(k_x^2 + k_y^2) \right] \tau_z \otimes \sigma_0 + Bk_z \tau_x \otimes \sigma_z + A k_x \tau_x \otimes \sigma_x + A k_y \tau_x \otimes \sigma_y, \tag{25}
$$

where $\sigma_i$ and $\tau_i$ are Pauli matrices in spin and orbital-pseudo-spin space, respectively, we have [44]

$$
\langle \tau' \sigma' | e\mathbf{r} | \tau \sigma \rangle = \tau \frac{ie}{2m_0} \langle \tau' \sigma' | \left( \partial H_0/\partial \mathbf{k} \right)_{\mathbf{k}=0} | \tau \sigma \rangle \quad . \tag{26}
$$

Here $|\tau \sigma\rangle$ represents the basis functions in the orbital and spin space of the Hamiltonian $H_0$ defined in equation (1), and $\tau$ is the eigenvalue of $\tau_z$ associated with the eigenstate $|\tau \sigma\rangle$. Taking the derivative $\partial H_0/\partial \mathbf{k}$ of $H_0$ in equation (25) and setting $\mathbf{k}=0$, we find

$$
\mathbf{d}^{(\text{inter})} = \frac{eB}{2m_0} \tau_y \otimes \sigma_z \hat{z} + \frac{eA}{2m_0} \tau_y \otimes \sigma_y \hat{y} + \frac{eA}{2m_0} \tau_y \otimes \sigma_x \hat{x} \quad . \tag{27}
$$

Using the general formalism discussed in the previous paragraph, the optical-dipole matrix elements between confined TI-nanowire states is obtained as

$$
\mathbf{d}_{s,j,k_z}^{s',j',k_z'} = \int \mathrm{d}z \int_0^R \rho \mathrm{d}\rho \int_0^{2\pi} \mathrm{d}\varphi \Psi_{s',j',k_z'}^\dagger(\rho, \varphi, z) \mathbf{d}(\rho, \varphi, z) \Psi_{s,j,k_z}(\rho, \varphi, z) . \tag{28}
$$

Here $\mathbf{d}(\rho, \varphi, z) \equiv e(\rho \cos\varphi \hat{x} + \rho \sin\varphi \hat{y} + z \hat{z}) \mathbb{1} + \mathbf{d}^{(\text{inter})}$, with $\mathbf{d}^{(\text{inter})}$ given in equation (27). Using equation (10) and performing the integrals over $\varphi$ and $z$, we obtain

$$
(d_x + id_y)_{s,j,k_z}^{s',j',k_z'} = \delta_{k_z,k_z'} \delta_{j,j'+1} \left[ e \sum_{i=1}^4 (\mathcal{R}_{ii})_{s,j,k_z}^{s',j+1,k_z} - \frac{ieA}{m_0} \left( (\mathcal{S}_{14})_{s,j,k_z}^{s',j+1,k_z} - (\mathcal{S}_{23})_{s,j,k_z}^{s',j+1,k_z} \right) \right], \tag{29}
$$

![](./images/812640031339446274_5.jpg)

and
$$
\left(d_{x}-i d_{y}\right)_{s, j, k_{z}}^{s^{\prime}, j^{\prime}, k_{z}^{\prime}}=\delta_{k_{z}, k_{z}^{\prime}} \delta_{j^{\prime}, j-1}\left[e \sum_{i=1}^{4}\left(\mathcal{R}_{i i}\right)_{s, j, k_{z}}^{s^{\prime}, j-1, k_{z}}-\frac{i e A}{m_{0}}\left(\left(\mathcal{S}_{32}\right)_{s, j, k_{z}}^{s^{\prime}, j-1, k_{z}}-\left(\mathcal{S}_{41}\right)_{s, j, k_{z}}^{s^{\prime}, j-1, k_{z}}\right)\right],\qquad(30)
$$
where we have defined the overlap integrals
$$
\left(\mathcal{S}_{m n}\right)_{s, j, k_{z}}^{s^{\prime}, j^{\prime}, k_{z}^{\prime}}=\int_{0}^{R} \mathrm{d} \rho \rho \Phi_{m, s^{\prime}, j^{\prime}, k_{z}^{\prime}}^{*}(\rho) \Phi_{n, s, j, k_{z}}(\rho)\qquad(31)
$$
and the matrix elements of radial position
$$
\left(\mathcal{R}_{m n}\right)_{s, j, k_{z}}^{s^{\prime}, j^{\prime}, k_{z}^{\prime}}=\int_{0}^{R} \mathrm{d} \rho \rho^{2} \Phi_{m, s^{\prime}, j^{\prime}, k_{z}^{\prime}}^{*}(\rho) \Phi_{n, s, j, k_{z}}(\rho).\qquad(32)
$$

For circular polarization in the plane perpendicular to the nanowire axis, we find the conventional selection rule $j'=j\pm1$, which is mandated by the conservation of total-angular-momentum projection (including the photon's) parallel to the nanowire axis. In addition, linear momentum $k_z$ parallel to the nanowire axis is conserved in any optical transition. The energy threshold for absorption is associated with transitions between $(s'=+,j=\pm1/2,k'_z=0)$ and $(s=-,j\mp1/2,k_z=0)$. At the subband edge $(k_z=0$ and $k'_z=0)$ for $d_x+id_y$ only the overlap integral $(\mathcal{S}_{14})_{-,-1/2,0}^{+,+1/2,0}$ is non-vanishing for absorption, while for emission the only non-vanishing overlap integral is $(\mathcal{S}_{23})_{+,-1/2,0}^{+,-1/2,0}$. For the opposite polarization, namely $d_x-id_y$, the non-vanishing overlap integrals at the band edge are: $(\mathcal{S}_{32})_{-,1/2,0}^{+,-1/2,0}$ for absorption and $(\mathcal{S}_{41})_{+,1/2,0}^{-,-1/2,0}$ for emission, respectively. The overlap integrals relevant for the absorption threshold are shown in figure 4 as a function of the radius of the wire. It needs to be noticed that also the matrix elements of the radial position $(\mathcal{R}_{mn})_{s,j,k_z}^{s',j',k_z'}$ contribute both to absorption and emission. The sum of these matrix elements for the case of absorption is shown in figure 5 as a function of the radius of the wire. The finite radius of the nanowire does not affect the selection rules but leads to significant quantitative changes of the dipole matrix elements.

Matrix elements of the optical-dipole component parallel to the nanowire axis are given by
$$
\begin{aligned}
\left(d_{z}\right)_{s, j, k_{z}}^{s^{\prime}, j^{\prime}, k_{z}^{\prime}}= & \left\{e \sum_{i=1}^{4}\left(\mathcal{S}_{i i}\right)_{s, j, k_{z}}^{s^{\prime}, j, k_{z}^{\prime}} \int \mathrm{d} z \frac{\mathrm{e}^{i\left(k_{z}-k_{z}^{\prime}\right) z}}{2 \pi}+\delta_{k_{z}, k_{z}^{\prime}} \frac{i e B}{2 m_{0}}\right. \\
& \left.\times\left[\left(\mathcal{S}_{21}\right)_{s, j, k_{z}}^{s^{\prime}, j, k_{z}^{\prime}}-\left(\mathcal{S}_{12}\right)_{s, j, k_{z}}^{s^{\prime}, j, k_{z}^{\prime}}+\left(\mathcal{S}_{34}\right)_{s, j, k_{z}}^{s^{\prime}, j, k_{z}^{\prime}}-\left(\mathcal{S}_{43}\right)_{s, j, k_{z}}^{s^{\prime}, j, k_{z}^{\prime}}\right]\right\} \delta_{j^{\prime}, j}.
\end{aligned}\qquad(33)
$$


![](./images/812640031339446274_6.jpg)

**Figure 5.** Dependence of $\sum_{i=1}^{4} \mathcal{R}_{ii}$ on the radius of the cylinder of (a) $\text{Bi}_2\text{Se}_3$ and (b) $\text{Bi}_2\text{Te}_3$ for $k_z = k_z' = 0$.

![](./images/812640031339446274_7.jpg)

**Figure 6.** Overlap integrals entering the dipole matrix element relevant for absorption for linearly-polarised (longitudinal) light as a function of the radius of the cylinder of (a) $\text{Bi}_2\text{Se}_3$ and (b) $\text{Bi}_2\text{Te}_3$ for $k_z = k_z' = 0$.

The first term on the r.h.s. of equation (33) is ill-defined because the envelope functions are not localized in their dependence on the $z$ coordinate and, hence, the dipole approximation is not valid. However, the remaining basis-function-mediated contributions describe valid optical transitions. For these, both linear momentum $k_z$ and the total-angular-momentum projection $j$ parallel to the nanowire axis are the same for initial and final states involved in optical transitions. For states at the energy threshold of absorption, we find that the only non vanishing overlap integrals are $(\mathcal{S}_{12})_{-,\pm1/2,0}^{+,\pm1/2,0}$ and $(\mathcal{S}_{43})_{-,\pm1/2,0}^{+,\pm1/2,0}$, while for emission the non vanishing overlap integrals are $(\mathcal{S}_{21})_{+,\pm1/2,0}^{-,\pm1/2,0}$ and $(\mathcal{S}_{34})_{+,\pm1/2,0}^{-,\pm1/2,0}$. The overlap integrals relevant for absorption are shown in figure 6. Again, the selection rules for optical transitions are consistent with the basic symmetries associated with a cylindrical-nanowire geometry, and finite-size effects are manifested as significant quantitative changes in the magnitude of dipole matrix elements.

## 4. Conclusions
In this paper we have studied a nanowire made of TI. In particular, we have provided the analytical form of the energy eigenfuctions, which is central to the derivation of an analytical secular equation for the eigenenergies. This secular equation, on one hand, enables an analytical expansion for large radii and, on the other hand, is amenable to straightforward numerical solution. We study the dependence of the eigenenergies on the radius of the wire and we find oscillations as a function of the radius, which are very pronounced for $\text{Bi}_2\text{Te}_3$. The analytical form of the energy eigenfuctions enables the computation of the matrix elements of any single-particle operator. We have considered the optical dipole matrix elements. While we find the usual selection rules for absorption/emission, the value of the matrix elements is strongly dependent on the radius of the cylinder.

Our work can inform further detailed exploration of physical properties exhibited by TI nanowires. For example, the implications of cylindrical symmetry on the topological magnetoelectric effect have previously

been studied within the framework of macroscopic continuum-electromagnetic theory [45]. To gain insight about the materials-size dependence of unconventional electromagnetic responses, the formalism of reference [45] could be generalized to treat the magnetoelectric effect in TI nanowires by adopting appropriate boundary conditions that reflect the surface-electromagnetic response [46]. Calculation of the relevant parameters entering amended boundary conditions for the electromagnetic fields could be facilitated by the explicit form of surface- and bound-state wave functions provided in our present work. Recent studies [47, 48] have revealed interesting topological-electromagnetic responses of spherical nanoparticles, and we expect a future investigation of the TI-nanowire electromagnetic response to be equally fruitful.

## Appendix A. Secular equation for confined states

In this appendix we provide the detailed derivation of the secular equation for the state of the TI cylinder. Acting with the Hamiltonian (2) on the wave function equation (6) and looking for eigenfunctions with energy $E$, we obtain

$$
\left(\begin{array}{cccc}
m_{\perp}+m_{-}\left(j, k_{z}\right)-E & B k_{z} & 0 & -i A\left[\partial_{\rho}+\frac{1}{\rho}\left(j+\frac{1}{2}\right)\right] \\
B k_{z} & -\left[m_{\perp}+m_{-}\left(j, k_{z}\right)+E\right] & -i A\left[\partial_{\rho}+\frac{1}{\rho}\left(j+\frac{1}{2}\right)\right] & 0 \\
0 & -i A\left[\partial_{\rho}-\frac{1}{\rho}\left(j-\frac{1}{2}\right)\right] & m_{\perp}+m_{+}\left(j, k_{z}\right)-E & -B k_{z} \\
-i A\left[\partial_{\rho}-\frac{1}{\rho}\left(j-\frac{1}{2}\right)\right] & 0 & -B k_{z} & -\left[m_{\perp}+m_{+}\left(j, k_{z}\right)+E\right]
\end{array}\right)\left(\begin{array}{c}
\Phi_{1}(\rho) \\
\Phi_{2}(\rho) \\
\Phi_{3}(\rho) \\
\Phi_{4}(\rho)
\end{array}\right)=0,
$$

where we have defined $m_{ \pm}\left(j, k_{z}\right)=m_{2} \frac{1}{\rho^{2}}\left(j \pm \frac{1}{2}\right)^{2}+m_{1} k_{z}^{2}$. To solve the eigensystem equation (A.1) we make the *Ansatz*

$$
\left(\begin{array}{l}
\Phi_{1}(\rho) \\
\Phi_{2}(\rho) \\
\Phi_{3}(\rho) \\
\Phi_{4}(\rho)
\end{array}\right)=\left(\begin{array}{l}
c_{1} J_{j-\frac{1}{2}}(\kappa \rho) \\
c_{2} J_{j-\frac{1}{2}}(\kappa \rho) \\
c_{3} J_{j+\frac{1}{2}}(\kappa \rho) \\
c_{4} J_{j+\frac{1}{2}}(\kappa \rho)
\end{array}\right), \tag{A.2}
$$

where $J_{n}(z)$ is a Bessel function of the first kind and $\kappa$ and the coefficients $c_{1}, \ldots, c_{4}$ need to be determined. Substituting the *Ansatz* equation (A.2) in (A.1), we obtain the following equation for the coefficients

$$
\left(\begin{array}{cccc}
-\left(\kappa^{2}+\frac{m_{1}}{m_{2}} k_{z}^{2}+\frac{m_{0}-E}{m_{2}}\right) & -\frac{B k_{z}}{m_{2}} & 0 & i \frac{A \kappa}{m_{2}} \\
\frac{B k_{z}}{m_{2}} & -\left(\kappa^{2}+\frac{m_{1}}{m_{2}} k_{z}^{2}+\frac{m_{0}+E}{m_{2}}\right) & -i \frac{A \kappa}{m_{2}} & 0 \\
0 & -i \frac{A \kappa}{m_{2}} & -\left(\kappa^{2}+\frac{m_{1}}{m_{2}} k_{z}^{2}+\frac{m_{0}-E}{m_{2}}\right) & \frac{B k_{z}}{m_{2}} \\
i \frac{A \kappa}{m_{2}} & 0 & -\frac{B k_{z}}{m_{2}} & -\left(\kappa^{2}+\frac{m_{1}}{m_{2}} k_{z}^{2}+\frac{m_{0}+E}{m_{2}}\right)
\end{array}\right)\left(\begin{array}{l}
c_{1} \\
c_{2} \\
c_{3} \\
c_{4}
\end{array}\right)=0. \tag{A.3}
$$

Equation (A.3) has non-trivial solutions for

$$
\left(\kappa^{2}+\frac{m_{1}}{m_{2}} k_{z}^{2}+\frac{m_{0}}{m_{2}}\right)^{2}+\frac{A^{2}}{m_{2}^{2}} \kappa^{2}+\frac{B^{2}}{m_{2}^{2}} k_{z}^{2}-\frac{E^{2}}{m_{2}^{2}}=0 \tag{A.4}
$$

which yields⁷

$$
\kappa=\kappa_{ \pm}=\sqrt{-\left(\frac{m_{0}}{m_{2}}+\frac{A^{2}}{2 m_{2}^{2}}+\frac{m_{1}}{m_{2}} k_{z}^{2}\right) \pm \sqrt{\frac{A^{4}}{4 m_{2}^{4}}+\frac{E^{2}}{m_{2}^{2}}+\frac{A^{2} m_{0}}{m_{2}^{3}}+\left(\frac{A^{2}}{m_{2}^{2}} \frac{m_{1}}{m_{2}}-\frac{B^{2}}{m_{2}^{2}}\right) k_{z}^{2}}}. \tag{A.5}
$$

There are four independent solutions for $(c_{1}, c_{2}, c_{3}, c_{4})^{\mathrm{T}}$ and are given by

⁷ The negative sign for the outer square root does not give a different solution and therefore should not be considered due to the property of the Bessel's functions: $J_{n}(z)=(-1)^{n} J_{n}(-z)$ for integer $n$.

![](./images/812640031339446274_8.jpg)

$$
\left(\frac{i A \kappa_{ \pm}}{\Delta_{ \pm}}, 0, \frac{B k_{z}}{\Delta_{ \pm}}, 1\right)^{\mathrm{T}}, \tag{A.6}
$$

$$
\left(-\frac{B k_{z}}{\Delta_{ \pm}}, 1,-\frac{i A \kappa_{ \pm}}{\Delta_{ \pm}}, 0\right)^{\mathrm{T}}, \tag{A.7}
$$

where we have introduced the following abbreviation $\Delta_{\pm}=m_{2} \kappa_{\pm}^{2}+m_{1} k_{z}^{2}+m_{0}-E$. The general solution with quantum numbers $k_z$, $j$ and $E$ can therefore be written as

$$
\Psi(\rho, \varphi, z)=\frac{\mathrm{e}^{i k_{z} z}}{\sqrt{2 \pi}} \sum_{\eta= \pm}\left\{\alpha_{\eta}\left(\begin{array}{c}
\frac{i A \kappa_{\eta}}{\Delta_{\eta}} J_{j-\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{i\left(j-\frac{1}{2}\right) \varphi} \\
0 \\
\frac{B k_{z}}{\Delta_{\eta}} J_{j+\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{i\left(j+\frac{1}{2}\right) \varphi} \\
J_{j+\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{i\left(j+\frac{1}{2}\right) \varphi}
\end{array}\right)+\beta_{\eta}\left(\begin{array}{c}
-\frac{B k_{z}}{\Delta_{\eta}} J_{j-\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{i\left(j-\frac{1}{2}\right) \varphi} \\
J_{j-\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{i\left(j-\frac{1}{2}\right) \varphi} \\
-\frac{i A \kappa_{\eta}}{\Delta_{\eta}} J_{j+\frac{1}{2}}\left(\kappa_{\eta} \rho\right) \mathrm{e}^{i\left(j+\frac{1}{2}\right) \varphi} \\
0
\end{array}\right)\right\}. \tag{A.8}
$$

Assuming a hard-wall cylindrical confinement potential of radius $R$, we need to impose the boundary condition $\Psi(R, \varphi, z)=0$ which leads to the following system of equations:

$$
\left(\begin{array}{cccc}
\frac{i A \kappa_{+}}{\Delta_{+}} J_{j-\frac{1}{2}}\left(\kappa_{+} R\right) & -\frac{B k_{z}}{\Delta_{+}} J_{j-\frac{1}{2}}\left(\kappa_{+} R\right) & \frac{i A \kappa_{-}}{\Delta_{-}} J_{j-\frac{1}{2}}\left(\kappa_{-} R\right) & -\frac{B k_{z}}{\Delta_{-}} J_{j-\frac{1}{2}}\left(\kappa_{-} R\right) \\
0 & J_{j-\frac{1}{2}}\left(\kappa_{+} R\right) & 0 & J_{j-\frac{1}{2}}\left(\kappa_{-} R\right) \\
\frac{B k_{z}}{\Delta_{+}} J_{j+\frac{1}{2}}\left(\kappa_{+} R\right) & -\frac{i A \kappa_{+}}{\Delta_{+}} J_{j+\frac{1}{2}}\left(\kappa_{+} R\right) & \frac{B k_{z}}{\Delta_{-}} J_{j+\frac{1}{2}}\left(\kappa_{-} R\right) & -\frac{i A \kappa_{-}}{\Delta_{-}} J_{j+\frac{1}{2}}\left(\kappa_{-} R\right) \\
J_{j+\frac{1}{2}}\left(\kappa_{+} R\right) & 0 & J_{j+\frac{1}{2}}\left(\kappa_{-} R\right) & 0
\end{array}\right)\left(\begin{array}{c}
\alpha_{+} \\
\beta_{+} \\
\alpha_{-} \\
\beta_{-}
\end{array}\right)=0. \tag{A.9}
$$

We then obtain the secular equation

$$
\begin{aligned}
& {\left[\kappa_{+} \Delta_{-} J_{j-\frac{1}{2}}\left(\kappa_{-} R\right) J_{j+\frac{1}{2}}\left(\kappa_{+} R\right)-\kappa_{-} \Delta_{+} J_{j-\frac{1}{2}}\left(\kappa_{+} R\right) J_{j+\frac{1}{2}}\left(\kappa_{-} R\right)\right]} \\
& \quad \times\left[\kappa_{+} \Delta_{-} J_{j-\frac{1}{2}}\left(\kappa_{+} R\right) J_{j+\frac{1}{2}}\left(\kappa_{-} R\right)-\kappa_{-} \Delta_{+} J_{j-\frac{1}{2}}\left(\kappa_{-} R\right) J_{j+\frac{1}{2}}\left(\kappa_{+} R\right)\right] \\
& \quad+\frac{B^{2}}{A^{2}} k_{z}^{2}\left(\Delta_{+}-\Delta_{-}\right)^{2} J_{j-\frac{1}{2}}\left(\kappa_{-} R\right) J_{j-\frac{1}{2}}\left(\kappa_{+} R\right) J_{j+\frac{1}{2}}\left(\kappa_{-} R\right) J_{j+\frac{1}{2}}\left(\kappa_{+} R\right)=0. \tag{A.10}
\end{aligned}
$$

Notice that the term in the third line of equation (A.10) vanishes for $k_z=0$. By simple algebraic manipulations, equation (A.10) can be cast in the form of equation (11).

## Appendix B. Small-radius limit

In section 3.2 we found interesting finite-size effects for small values of the radius $R$, such as the oscillatory behaviour of the eigenenergies. In order to understand the origin of the oscillations in figure 1, here we use

the Hankel's asymptotic expansion (equation (14)), but without approximating the trigonometric functions, and solve the secular equation at each given order. The plot of the eigenenergy as a function of $R$, obtained by taking into account only the first order in $1/z$ [$P(n,z)=1$ and $Q(n,z)=(4n^2-1)/(8z)$], is shown in figure B1 as a dashed black curve: it is found to agree remarkably well with the full numerical results (solid red curve). The expansion up to second order in $1/z$ (not shown)
[$P(n,z)=1-(4n^2-1)(4n^2-9)/(128z^2)$ and $Q(n,z)=(4n^2-1)/(8z)$] is practically indistinguishable from the full numerical results.

## ORCID iDs

Michele Governale 🔗 https://orcid.org/0000-0001-7947-2155
Fabio Taddei 🔗 https://orcid.org/0000-0002-2482-6750
Ken-Ichiro Imura 🔗 https://orcid.org/0000-0002-8834-0493
Ulrich Zülicke 🔗 https://orcid.org/0000-0001-5055-3330

## References

[1] Fu L, Kane C L and Mele E J 2007 Topological insulators in three dimensions *Phys. Rev. Lett.* **98** 106803
[2] Hasan M Z and Kane C L 2010 Colloquium: topological insulators *Rev. Mod. Phys.* **82** 3045
[3] Qi X L and Zhang S C 2011 Topological insulators and superconductors *Rev. Mod. Phys.* **83** 1057
[4] Hasan M Z and Moore J E 2011 Three-dimensional topological insulators *Annu. Rev. Condens. Matter Phys.* **2** 55
[5] Ando Y 2013 Topological insulator materials *J. Phys. Soc. Japan* **82** 102001
[6] Lee D H 2009 Surface states of topological insulators: the Dirac fermion in curved two-dimensional spaces *Phys. Rev. Lett.* **103** 196804
[7] Parente V, Lucignano P, Vitale P, Tagliacozzo A and Guinea F 2011 Spin connection and boundary states in a topological insulator *Phys. Rev. B* **83** 075424
[8] Imura K I, Yoshimura Y, Takane Y and Fukui T 2012 Spherical topological insulator *Phys. Rev. B* **86** 235119
[9] Cho S, Dellabetta B, Zhong R, Schneeloch J, Liu T, Gu G, Gilbert M J and Mason N 2015 Aharonov-Bohm oscillations in a quasi-ballistic three-dimensional topological insulator nanowire *Nat. Commun.* **6** 7634
[10] Kim M, Kim J, Hou Y, Yu D, Doh Y J, Kim B, Kim K W and Suh J 2019 Nanomechanical characterization of quantum interference in a topological insulator nanowire *Nat. Commun.* **10** 4522
[11] Münning F, Breunig O, Legg H F, Roitsch S, Fan D, Rößler M, Rosch A and Ando Y 2019 Quantum confinement of the Dirac surface states in topological-insulator nanowires (arXiv:1910.07863)
[12] Tian M *et al* 2013 Dual evidence of surface dirac states in thin cylindrical topological insulator $Bi_2Te_3$ nanowires *Sci. Rep.* **3** 1212
[13] Hamdou B, Gooth J, Dorn A, Pippel E and Nielsch K 2013 Surface state dominated transport in topological insulator $Bi_2Te_3$ nanowires *Appl. Phys. Lett.* **103** 193107
[14] Safdar M *et al* 2013 Topological surface transport properties of single-crystalline SnTe nanowire *Nano Lett.* **13** 5344
[15] Bäßler S *et al* 2015 One-dimensional edge transport on the surface of cylindrical $Bi_xTe3-ySe_y$ nanowires in transverse magnetic fields *Appl. Phys. Lett.* **107** 181602
[16] Arango Y C *et al* 2016 Quantum transport and nano angle-resolved photoemission spectroscopy on the topological surface states of single $Sb_2Te_5$ nanowires *Sci. Rep.* **6** 29493
[17] Ziegler J *et al* 2018 Probing spin helical surface states in topological HgTe nanowires *Phys. Rev. B* **97** 035157
[18] Bhattacharyya B, Sharma A, Awana V P S, Senguttuvan T D and Husale S 2017 FIB synthesis of $Bi_2Se_3$ 1D nanowires demonstrating the co-existence of Shubnikov-de Haas oscillations and linear magnetoresistance *J. Phys.: Condens. Matter* **29** 07LT01
[19] Peng H *et al* 2009 AharonovBohm interference in topological insulator nanoribbons *Nat. Mater.* **9** 225
[20] Xiu F *et al* 2011 Manipulating surface states in topological insulator nanoribbons *Nat. Nanotechnol.* **6** 216
[21] Hong S S, Cha J J, Kong D and Cui Y 2012 Ultra-low carrier concentration and surface-dominant transport in antimony-doped $Bi_2Se_3$ topological insulator nanoribbons *Nat. Commun.* **3** 757
[22] Wang Z, Qiu R L J, Lee C H, Zhang Z and Gao X P A 2013 Ambipolar surface conduction in ternary topological insulator $Bi_2(Te_{1-x}Se_x)_3$ nanoribbons *ACS Nano* **7** 2126
[23] Jauregui L A, Pettes M T, Rokhinson L P, Shi L and Chen Y P 2015 Gate tunable relativistic mass and Berry/s phase in topological insulator nanoribbon field effect devices *Sci. Rep.* **5** 8452
[24] Dufouleur J *et al* 2017 Weakly-coupled quasi-1d helical modes in disordered 3d topological insulator quantum wires *Sci. Rep.* **7** 45276
[25] Kunakova G *et al* 2018 Bulk-free topological insulator Bi2Se3 nanoribbons with magnetotransport signatures of Dirac surface states *Nanoscale* **10** 19595
[26] Hong S S, Zhang Y, Cha J J, Qi X L and Cui Y 2014 One-dimensional helical transport in topological insulator nanowire interferometers *Nano Lett.* **14** 2815
[27] de Juan F, Ilan R and Bardarson J H 2014 Robust transport signatures of topological superconductivity in topological insulator nanowires *Phys. Rev. Lett.* **113** 107003
[28] Cook A and Franz M 2011 Majorana fermions in a topological-insulator nanowire proximity-coupled to an $s$-wave superconductor *Phys. Rev. B* **84** 201105
[29] Iorio P, Perroni C A and Cataudella V 2016 Quantum interference effects in $Bi_2Se_3$ topological insulator nanowires with variable cross-section lengths *Eur. Phys. J. B* **89** 97
[30] Hong S S, Kong D and Cui Y 2014 Topological insulator nano-structures *MRS Bull.* **39** 873
[31] Zhou B, Lu H Z, Chu R L, Shen S Q and Niu Q 2008 Finite size effects on helical edge states in a quantum spin-Hall system *Phys. Rev. Lett.* **101** 246807

[32] Linder J, Yokoyama T and Sudbø A 2009 Anomalous finite size effects on surface states in the topological insulator $Bi_2Se_3$ Phys. Rev. B 80 205401

[33] Liu C X, Zhang H, Yan B, Qi X L, Frauenheim T, Dai X, Fang Z and Zhang S C 2010 Oscillatory crossover from two-dimensional to three-dimensional topological insulators Phys. Rev. B 81 041307

[34] Imura K I, Okamoto M, Yoshimura Y, Takane Y and Ohtsuki T 2012 Finite-size energy gap in weak and strong topological insulators Phys. Rev. B 86 245436

[35] Kotulla M and Zülicke U 2017 Manipulating topological-insulator properties using quantum confinement New J. Phys. 19 073025

[36] Gioia L, Christie M G, Zülicke U, Governale M and Sneyd A J 2019 Spherical topological insulator nanoparticles: quantum size effects and optical transitions Phys. Rev. B 100 205417

[37] Zhang Y and Vishwanath A 2010 Anomalous aharonov-bohm conductance oscillations from topological insulator surface states Phys. Rev. Lett. 105 206601

[38] Bardarson J H, Brouwer P W and Moore J E 2010 Aharonov-bohm oscillations in disordered topological insulator nanowires Phys. Rev. Lett. 105 156803

[39] Zhang H, Liu C X, Qi X L, Dai X, Fang Z and Zhang S C 2009 Topological insulators in $Bi_2Se_3$, $Bi_2Te_3$ and $Sb_2Te_3$ with a single Dirac cone on the surface Nat. Phys. 82 438

[40] Liu C X, Qi X L, Zhang H, Dai X, Fang Z and Zhang S C 2010 Model Hamiltonian for topological insulators Phys. Rev. B 82 045122

[41] Nechaev I A and Krasovskii E E 2016 Relativistic $\boldsymbol{k \cdot p}$ Hamiltonians for centrosymmetric topological insulators from ab initio wave functions Phys. Rev. B 94 201410

[42] Imura K I, Takane Y and Tanaka A 2011 Spin Berry phase in anisotropic topological insulators Phys. Rev. B 84 195406

[43] Abramowitz M and Stegun I A 1964 Handbook of Mathematical Functions (New York: Dover)

[44] Haug H and Koch S W 2009 Quantum Theory of the Optical and Electronic Properties of Semiconductors 5th edn (Singapore: World Scientific)

[45] Martín-Ruiz A 2019 Magnetoelectric effect in cylindrical topological insulators Phys. Rev. D 98 056012

[46] Yang Y et al 2019 A general theoretical and experimental framework for nanoscale electromagnetism Nature 576 248

[47] Siroki G, Lee D K K, Haynes P D and Giannini V 2016 Single-electron induced surface plasmons on a topological nanoparticle Nat. Commun. 7 12375

[48] Zirnstein H-G and Rosenow B 2017 Time-reversal-symmetric topological magnetoelectric effect in three-dimensional topological insulators Phys. Rev. B 96 201112(R)