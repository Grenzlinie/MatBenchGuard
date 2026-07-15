![](./images/811805371084570624_1.jpg)

# Electronic structure, Raman tensors, and resonance phenomena in a simple molecular model

M. Meyer, P. G. Etchegoin, and E. C. Le Ru

Citation: *Am. J. Phys.* **78**, 300 (2010); doi: 10.1119/1.3271796

View online: http://dx.doi.org/10.1119/1.3271796

View Table of Contents: http://ajp.aapt.org/resource/1/AJPIAS/v78/i3

Published by the American Association of Physics Teachers

---

## Related Articles
Measurement of sub-natural linewidth AC Stark shifts in cold atoms: An experiment for an advanced undergraduate laboratory
*Am. J. Phys.* **79**, 1211 (2011)

Resource Letter VWCPF-1: van der Waals and Casimir–Polder forces
*Am. J. Phys.* **79**, 697 (2011)

Five ways to the nonresonant dynamic Stark effect
*Am. J. Phys.* **79**, 477 (2011)

Measuring the molecular polarizability of air
*Am. J. Phys.* **79**, 428 (2011)

Comment on "On the classical analysis of spin-orbit coupling in hydrogenlike atoms," by A. L. Kholmetskii, O. V. Missevitch, and T. Yarman [*Am. J. Phys.* **78** (4), 428–432 (2010)]
*Am. J. Phys.* **78**, 1422 (2010)

---

## Additional information on *Am. J. Phys.*
Journal Homepage: http://ajp.aapt.org/

Journal Information: http://ajp.aapt.org/about/about_the_journal

Top downloads: http://ajp.aapt.org/most_downloaded

Information for Authors: http://ajp.dickinson.edu/Contributors/contGenInfo.html

---

## ADVERTISEMENT

![](./images/811805371084570624_2.jpg)

# Electronic structure, Raman tensors, and resonance phenomena in a simple molecular model

M. Meyer, P. G. Etchegoin, $^{\text{a)}}$ and E. C. Le Ru$^{\text{b)}}$

The MacDiarmid Institute for Advanced Materials and Nanotechnology, School of Chemical and Physical Sciences, Victoria University of Wellington, P.O. Box 600, Wellington, New Zealand

(Received 9 August 2009; accepted 16 November 2009)

Some concepts in modern spectroscopy are very specialized, and explanations based on simple examples are not readily available. An example is the changes in the intrinsic symmetry of Raman tensors in molecules produced by resonance or near-resonance conditions. Many of these effects can be obtained from commercial and open source programs that solve the electronic structure of the molecules with density functional theory and compute the Raman tensors of the vibrations. The origin of these changes is hidden by the complexity of these calculations and by the many intermediate computational steps that are not presented to the user. We discuss a simplified model for the electronic structure of a molecule and correlate what is observed with a calculation using density functional theory for a specific molecule. The model yields insight into resonance phenomena, symmetry-related aspects of Raman tensors, and the microscopic origin of the Raman effect itself. © 2010 American Association of Physics Teachers.

[DOI: 10.1119/1.3271796]

## I. INTRODUCTION

The ever increasing availability of computer power makes relatively complex quantum mechanical calculations acces- sible to physicists and chemists. $^{1}$ Solving the electronic structure of molecules with density functional theory, $^{2}$ for example, involves an inherent degree of complexity and re- quires the use of a number of concepts in quantum mechan- ics such as the variational theorem, Fock operators, electron correlations, Slater determinants, and density functionals. Textbooks often study the simplest of cases (for example, $H_{2}^{+}$) but limit themselves to generalities for more complex molecules because they can only be solved numerically on a computer. The available programs to do these calculations (both commercial and open source) hide the technicalities and difficulties from the user and thus act as a "black box." This use is acceptable in cases where the direct comparison of a specific property of the molecule (the vibrational spec- trum, for example) with experiments is sought. It then might not be necessary or desirable to go into all the details of the calculation in the same way that it might not be necessary to understand all the details of the circuitry of an instrument to carry out an experiment. The results are judged by the sound- ness of their physical meaning and by their overall agree- ment and consistency with experiments.

Quantum chemical calculations deduce a variety of prop- erties for a given molecule from the calculated electronic structure. We will concentrate here on Raman spectroscopy. $^{1,3}$ The output of density functional theory pro grams includes vibrational frequencies and the Raman spec- trum (including Raman tensors for the vibrations $^{1}$) but does not give insight into the microscopic origin of these magni- tudes. Raman tensors, in particular, have specific symmetries that are related to the symmetries of the vibrations by group theory. $^{4}$ These symmetries define a number of readily mea surable properties of molecules, such as the depolarization ratio, $^{3,5,6}$ and are part of the standard protocols used in spec troscopy to understand the vibrational structure of molecules.

In Raman spectroscopy the symmetries of Raman tensors change depending on the (laser) excitation being used. These changes and the associated effects are grouped under what are normally called "resonance effects." These changes in symmetry can be seen experimentally and obtained from density functional theory calculations. The purpose of this paper is to present the simplest possible example of a Raman tensor calculation to show the origin of some of the well- known resonance effects such as symmetry changes. We as- sume familiarity with only basic quantum mechanics (wave functions and operators) and discuss a simplified calculation of molecular orbitals, states, transition dipoles, and polariz- abilities. We avoid the more complex facets of the theory by reducing the problem to a fictitious toy molecule, whose electronic structure becomes analytically tractable.

## II. THE TOY MOLECULE

We consider a molecule with four sites and two types of "atoms," A and B. For the example to be useful, the molecu- lar structure and electronic properties should be easy enough to be solvable analytically. Also, as will become clear, we need a structure that is two-dimensional (that is, not a linear molecule such as $CO_{2}$ ). To this end, we have chosen the model depicted in Fig. 1, which satisfies this minimum set of conditions. We limit ourselves to one valence orbital per site, thus completely ignoring lower lying core-electrons. The single orbital wave functions of the different sites are $|\varphi_{1}\rangle$, $|\varphi_{2}\rangle$, $|\varphi_{3}\rangle$, and $|\varphi_{4}\rangle$. Having one orbital per site does not necessarily mean that each atom donates one electron to the structure-we will assume that atoms of type A donate one electron each and the valence orbitals of atoms B are empty. We fix the site energies for $i=1,3$ to be $\langle\varphi_{i}|\hat{H}| \varphi_{i}\rangle=\epsilon_{a}$ (atoms of type A) and for $i=2,4$ to be $\langle\varphi_{i}|\hat{H}| \varphi_{i}\rangle=\epsilon_{b}$ (atoms of type B). For the cross-terms we assume an overlap integral of $-t$ through the overlap of orbitals of (nearest) neighboring at- oms, for example, $\langle\varphi_{1}|\hat{H}| \varphi_{2}\rangle=-t/2$ and $\langle\varphi_{2}|\hat{H}| \varphi_{1}\rangle=-t/2$. The orbital overlaps of sites 1 and 3, as well as sites 2 and 4, are assumed to be negligible. The electronic structure is there- fore represented by what is known as the tight binding approximation $^{7,8}$ with a linear combination of atomic orbitals approach. $^{2,9}$

![](./images/811805371084570624_3.jpg)

Fig. 1. A schematic representation of the structure of a toy molecule. Two different types of atoms with one orbital per site and site energies $\epsilon_a$ and $\epsilon_b$, respectively, are arranged in a square structure. Each atom interacts with its nearest neighbors (of the opposite type) through an overlap interaction integral. The Hamiltonian of this system in the tight binding approximation is given by Eq. (1) and produces the four eigenvectors given by Eq. (8) and schematically displayed in Fig. 2.

We assume the wave functions to be normalized (that is, $\langle\varphi_i|\varphi_i\rangle=1$) so that we can project the Hamiltonian onto the basis of the atomic orbitals. The Hamiltonian operator $\hat{H}$ for the system in Fig. 1 (in a ket-bra representation) is given by
$$
\begin{aligned}
\hat{H}= & \epsilon_{a}\left(\left|\varphi_{1}\right\rangle\left\langle\varphi_{1}|+| \varphi_{3}\right\rangle\left\langle\varphi_{3}\right|\right)+\epsilon_{b}\left(\left|\varphi_{2}\right\rangle\left\langle\varphi_{2}|+| \varphi_{4}\right\rangle\left\langle\varphi_{4}\right|\right) \\
& -\frac{t}{2}\left(\left|\varphi_{1}\right\rangle\left\langle\varphi_{2}|+| \varphi_{2}\right\rangle\left\langle\varphi_{1}|+| \varphi_{2}\right\rangle\left\langle\varphi_{3}|+| \varphi_{3}\right\rangle\left\langle\varphi_{2}|+| \varphi_{3}\right\rangle\right. \\
& \left.\times\left\langle\varphi_{4}|+| \varphi_{4}\right\rangle\left\langle\varphi_{3}|+| \varphi_{4}\right\rangle\left\langle\varphi_{1}|+| \varphi_{1}\right\rangle\left\langle\varphi_{4}\right|\right).
\end{aligned}
$$

In matrix form in the basis $|\varphi_1\rangle$, $|\varphi_2\rangle$, $|\varphi_3\rangle$, and $|\varphi_4\rangle$ (in that order), the Hamiltonian takes the form
$$
\hat{H}=\left(\begin{array}{cccc}
\epsilon_{a} & -\frac{t}{2} & 0 & -\frac{t}{2} \\
-\frac{t}{2} & \epsilon_{b} & -\frac{t}{2} & 0 \\
0 & -\frac{t}{2} & \epsilon_{a} & -\frac{t}{2} \\
-\frac{t}{2} & 0 & -\frac{t}{2} & \epsilon_{b}
\end{array}\right),
$$
from which we can readily determine the eigenvalues $\hbar \omega_{i}$ and eigenvectors $|\psi^{j}\rangle$.

## III. EIGENSTATES

The eigenvalues and eigenvectors can be concisely expressed using the definitions
$$
\gamma \equiv \frac{\epsilon_{b}-\epsilon_{a}}{2}, \quad \kappa \equiv \sqrt{\gamma^{2}+t^{2}}.
\tag{3}
$$

The eigenvalues can be written as
$$
\hbar \omega_{1}=\epsilon_{a}+\gamma-\kappa,
\tag{4a}
$$
$$
\hbar \omega_{2}=\epsilon_{a},
\tag{4b}
$$
$$
\hbar \omega_{3}=\epsilon_{b},
\tag{4c}
$$
$$
\hbar \omega_{4}=\epsilon_{b}-\gamma+\kappa.
\tag{4d}
$$

The corresponding normalized eigenvectors are
$$
\left|\psi^{1}\right\rangle=\frac{t}{\sqrt{2(\gamma+\kappa)^{2}+2 t^{2}}}\left(\begin{array}{c}
(\gamma+\kappa) / t \\
1 \\
(\gamma+\kappa) / t \\
1
\end{array}\right),
\tag{5}
$$
$$
\left|\psi^{2}\right\rangle=\frac{1}{\sqrt{2}}\left(\begin{array}{c}
-1 \\
0 \\
1 \\
0
\end{array}\right),
\tag{6}
$$
$$
\left|\psi^{3}\right\rangle=\frac{1}{\sqrt{2}}\left(\begin{array}{c}
0 \\
-1 \\
0 \\
1
\end{array}\right),
\tag{7}
$$
$$
\left|\psi^{4}\right\rangle=\frac{t}{\sqrt{2(\gamma-\kappa)^{2}+2 t^{2}}}\left(\begin{array}{c}
(\gamma-\kappa) / t \\
1 \\
(\gamma-\kappa) / t \\
1
\end{array}\right).
\tag{8}
$$

We have ordered the eigenvalues and eigenvectors according to their energy. For any $t>0$ (as assumed here), the lowest and highest energy eigenvalues are always at $\epsilon_{1,4}=\epsilon_{a}$ $+\gamma \mp \sqrt{\gamma^{2}+t^{2}}$ (or equivalently $\epsilon_{1,4}=\epsilon_{b}-\gamma \mp \sqrt{\gamma^{2}+t^{2}}$).

The second and third eigenvalues are the atomic site energies; we assume (without any loss of generality) that $\epsilon_a$ $<\epsilon_b$. These eigenvectors describe "antibonding" (antisymmetric) states formed by a linear combination of orbitals from atoms of type A or B, respectively. They are also odd with respect to the center of the molecule (that is, they change sign upon an inversion). This symmetry is a natural consequence of the parity of these states. $^{4,10}$ The first and last eigenvalues are the average site energy plus or minus the splitting $\kappa$. They describe even states formed by linear combinations of contributions from orbitals of both types of atoms.

Of interest for the calculation of the optical properties is the difference between the second and first, and third and first eigenvalues, respectively (which are the only dipole allowed transitions). We can define these differences as
$$
\hbar \omega_{12} \equiv \hbar\left(\omega_{2}-\omega_{1}\right)=-\gamma+\kappa
\tag{9}
$$
and
$$
\hbar \omega_{13} \equiv \hbar\left(\omega_{3}-\omega_{1}\right)=\gamma+\kappa.
\tag{10}
$$

The eigenvectors $|\psi^{k}\rangle$ are collections of scaling coefficients for the basis set of atomic orbitals $|\varphi\rangle$,
$$
\left|\psi^{k}\right\rangle=\left(\begin{array}{c}
c_{1}^{k} \\
c_{2}^{k} \\
c_{3}^{k} \\
c_{4}^{k}
\end{array}\right).
\tag{11}
$$

![](./images/811805371084570624_4.jpg)

Fig. 2. Schematic representation of the electronic energy levels for the parameters $\epsilon_{a}$=1 eV, $\epsilon_{b}$=1.2 eV, and $t$=0.5 eV. The wave functions of the different levels [see Eq. (3)] are represented as schematic intensity maps (all of them plotted in the same scale). White (dark) means a positive (negative) part of the wave function. The ground state at $\hbar\omega_{1}$ and the highest electronic level (at $\hbar\omega_{4}$) are symmetric with respect to the origin; the two intermediate states $\hbar\omega_{2}$ and $\hbar\omega_{3}$ are antisymmetric along $\hat{y}$ and $\hat{x}$, respectively. Dipole allowed transitions can only occur between states of different parity. The transitions $1\rightarrow2$ and $1\rightarrow3$ are the only dipole allowed transitions from the ground state, and $1\rightarrow4$ is a dipole forbidden (quadrupolar transition).

To visualize the qualitative electronic landscape described by the eigenvectors $|\psi^{i}\rangle$, we assume the wave functions $|\varphi_{i}\rangle$ to be single Gaussian-like atomic orbitals centered at the atomic positions and take characteristic values for the parameters $\epsilon_{a,b}$ and $t$. Then, we can represent these electronic levels in both their energy spectrum and their spatial distribution. We take the site energies for atoms of type $a$ and $b$ to be different but close. For example, for $\epsilon_{a}$=1 eV, $\epsilon_{b}$=1.2 eV, and $t$=0.5 eV, we obtain the energy levels and wave functions shown in Fig. 2.

We now try to understand how these wave functions and levels determine the optical properties of this toy molecule.

## IV. THE LINEAR OPTICAL PROPERTIES OF THE TOY MOLECULE

We shall show the microscopic origin of certain preresonance phenomena in molecules using the simplified model. We shall only be concerned with the linear optical properties and Raman scattering efficiencies below any dipole allowed transition, that is, in what would normally be classified as the *transparency region* of the molecule. In particular, we are interested in the changes that these quantities undergo as the photon energy approaches resonance, that is, becomes closer (approaching the transition from smaller energies) to the first dipole allowed transition $1\rightarrow2$.

The linear optical polarizability arises from the effect of the perturbation introduced by the electric dipole operator (of the light) on the electronic structure of the molecule. If the energy of the photon is smaller than the lowest dipole allowed transition ($1\rightarrow2$ in our case), there is no direct effect produced by the perturbation. In other words, the photon cannot change the electronic structure by producing electronic transitions among levels, which is the reason for transparency in the first place. However, in the quantum mechanical approach, $^{11}$ the first-order correction to the presence of the electric field's perturbation (for which the ground state of the molecule is both the initial and final state) leads to the well-known expression $^{12}$ for the linear optical polarizability given by $^{11,13}$

$$
\begin{aligned}
\alpha_{i j}(\omega)= & \frac{4 \pi}{\varepsilon_{0}} \sum_{k}\left(\frac{\left\langle\psi^{1}\left|p_{i}\right| \psi^{k}\right\rangle\left\langle\psi^{k}\left|p_{j}\right| \psi^{1}\right\rangle}{\hbar\left(\omega_{k}-\omega_{1}\right)-\hbar \omega-i \Gamma}\right. \\
& \left.+\frac{\left\langle\psi^{1}\left|p_{j}\right| \psi^{k}\right\rangle\left\langle\psi^{k}\left|p_{i}\right| \psi^{1}\right\rangle}{\hbar\left(\omega_{k}-\omega_{1}\right)+\hbar \omega-i \Gamma}\right),
\end{aligned}\qquad(12)
$$

where $\alpha_{i j}(\omega)$ is the $ij$-component of the linear optical polarizability tensor at frequency $\omega$ and the parameter $\Gamma$ models the resonant damping/broadening. We shall not discuss the details of polarizability theory, which is extensively treated in the literature. $^{12,14,15}$ Instead, we take Eq. (12) as the starting point for the effects we will study.

Expressions such as $\langle\psi^{1}|p_{i}| \psi^{k}\rangle$ in Eq. (12) represent the matrix elements of the $i$th component ($i$=$x,y$ in two dimensions) of the electric dipole operator $\mathbf{p}=e\mathbf{r}$. The other terms and symbols have their usual meaning. The first term in Eq. (12) represents a virtual transition to an excited state ($1\rightarrow k$) through the $p_{i}$ component of the dipole operator, followed by a return to the ground state through the transition $k\rightarrow1$ induced by the $p_{j}$ component of $\mathbf{p}$. The energy denominators are a distinctive characteristic of second-order perturbation terms in quantum mechanics. $^{11}$ The second term in Eq. (12) differs from the first one only in the sign of $\omega$ (the perturbation frequency) in the denominator. The origin of the second term in Eq. (12) is that the linear optical polarizability needs to satisfy causality (Kramers-Kronig relations). $^{12,15}$ For $\omega\approx(\omega_{k}-\omega_{1})$ (close to resonance) we can ignore the second term and work with the simplified expression

$$
\alpha_{i j}(\omega) \approx \frac{4 \pi}{\varepsilon_{0}} \sum_{k}\left(\frac{\left\langle\psi^{1}\left|p_{i}\right| \psi^{k}\right\rangle\left\langle\psi^{k}\left|p_{j}\right| \psi^{1}\right\rangle}{\hbar\left(\omega_{k}-\omega_{1}\right)-\hbar \omega-i \Gamma}\right).\qquad(13)
$$

Due to the symmetry of the wave functions (see Fig. 2), it is straightforward to show that there are only two dipole allowed transitions in the system in Fig. 2: One for $\omega_{1}\rightarrow\omega_{2}$, which has nonzero matrix elements only for the $y$ component of $\mathbf{p}$ (that is, $p_{y}$) and one nonzero matrix element for $\omega_{1}\rightarrow\omega_{3}$ only for $p_{x}\neq0$. Also the transition $\omega_{1}\rightarrow\omega_{4}$ is not dipole allowed (by parity) and need not be considered for the optical properties from the ground state ($\omega_{1}\rightarrow\omega_{4}$ is a quadrupolar transition). There are no off-diagonal elements in the polarizability tensor in the system of axes depicted in Fig. 1.

Thus the full polarizability tensor in two dimensions of the molecule reads

$$
\hat{\alpha}(\omega)=\left(\begin{array}{cc}
\alpha_{x x}(\omega) & 0 \\
0 & \alpha_{y y}(\omega)
\end{array}\right),\qquad(14)
$$

where $\alpha_{x x}(\omega)$ and $\alpha_{y y}(\omega)$ are given in Eqs. (15) and (16).

The $yy$ component of the polarizability tensor, which is affected only by the lowest dipole allowed transition, is

$$
\alpha_{y y}(\omega)=\frac{4 \pi}{\varepsilon_{0}} \frac{\left|\left\langle\psi^{1}\left|p_{y}\right| \psi^{2}\right\rangle\right|^{2}}{\hbar \omega_{12}-\hbar \omega-i \Gamma},\qquad(15)
$$

where $\omega_{12}\equiv(\omega_{2}-\omega_{1})$. Likewise, we obtain for $\alpha_{x x}(\omega)$ (which is affected only by the $\omega_{1}\rightarrow\omega_{3}$ transition)

$$
\alpha_{x x}(\omega)=\frac{4 \pi}{\varepsilon_{0}} \frac{\left|\left\langle\psi^{1}\left|p_{x}\right| \psi^{3}\right\rangle\right|^{2}}{\hbar \omega_{13}-\hbar \omega-i \Gamma}.\qquad(16)
$$

The energy differences $\hbar \omega_{12}$ and $\hbar \omega_{13}$ can be expressed in terms of the parameters of the electronic structure of the model by means of Eqs. (9) and (10). The matrix elements involved can also be calculated in terms of the basic param- eters of the model. In general, the matrix elements for the $1 \to 2$ and $1 \to 3$ transitions will not be the same because atoms of type A and B are different and the excited state (Fig. 2) involves atoms of either one type or the other. For the approximation that the atomic wave functions $|\varphi_{i}\rangle$ are similar for both atom types, which is sufficient for the sub- sequent discussion, the matrix elements of the two dipoles allowed transitions become identical.

If $\sqrt{2} a$ is the length of one of the four sides of the square in the structure in Fig. 1, the matrix elements are given by
$$
\begin{aligned}
\left\langle\psi^{1}\left|p_{y}\right| \psi^{2}\right\rangle=\frac{-e t}{\sqrt{(\gamma+\kappa)^{2}+t^{2}}}\left(2\left\langle\varphi_{2}|y| \varphi_{1}\right\rangle+\frac{(\gamma+\kappa)}{t} a\right), \\
(17)
\end{aligned}
$$
and
$$
\begin{aligned}
\left\langle\psi^{1}\left|p_{x}\right| \psi^{3}\right\rangle=\frac{-e t}{\sqrt{(\gamma+\kappa)^{2}+t^{2}}}\left(\frac{2(\gamma+\kappa)}{t}\left\langle\varphi_{1}|x| \varphi_{2}\right\rangle+a\right), \\
(18)
\end{aligned}
$$
where we have taken into account that $p_{x}=e x$ and $p_{y}=e y$, If we assume $\langle\varphi_{2}|y| \varphi_{1}\rangle=\langle\varphi_{1}|x| \varphi_{2}\rangle=a / 2$, that is, the orbitals of sites 1 and 2 have (approximately) a symmetric weighting on the $x$ and $y$ coordinates, we obtain
$$
\left\langle\psi^{1}\left|p_{y}\right| \psi^{2}\right\rangle=\left\langle\psi^{1}\left|p_{x}\right| \psi^{3}\right\rangle=\frac{-e a(\gamma+\kappa+t)}{\sqrt{(\gamma+\kappa)^{2}+t^{2}}}.\qquad(19)
$$

Therefore, if we use Eqs. (15), (16), and (19), the linear polarizability tensor can be written as
$$
\begin{aligned}
\hat{\alpha}(\omega)= & \frac{4 \pi a^{2}(\gamma+\kappa+t)^{2}}{\varepsilon_{0}\left((\gamma+\kappa)^{2}+t^{2}\right)} \\
& \times\left(\begin{array}{cc}
\frac{1}{\gamma+\kappa-\hbar \omega-i \Gamma} & 0 \\
0 & \frac{1}{-\gamma+\kappa-\hbar \omega-i \Gamma}
\end{array}\right). \quad(20)
\end{aligned}
$$

The advantage of having the linear optical polarizability expressed in terms of purely microscopic parameters of the electronic structure of the molecule is that we can now un- derstand the effect of a perturbation produced by a vibration. This fact is at the heart of the semiclassical description of the origin of the Raman effect and the derivation of the Raman polarizability tensor. From there, the effect of the approach to resonance on the Raman polarizability can be evaluated explicitly.

Because $\alpha_{x x} \neq \alpha_{y y}$, Eq. (20) represents the tensor of a birefringent molecule, which is in our case due solely to the two different resonant denominators.

![](./images/811805371084570624_5.jpg)

Fig. 3. The vibrational analysis of the molecule is much easier in the system of axes defined by $x^{\prime}-y^{\prime}$ in (a). Bond stretching $k_{\|}$and bond bending $k_{\perp}$ elastic constants can be defined and represented by classical springs con- necting the atoms. For our purposes we set $m_{a}=m_{b}$ to solve the dynamics without any loss of generality. Of all the internal modes of vibrations exist- ing in this molecule, we shall concentrate only on the breathing mode with the eigenvector represented in (b). This mode belongs to the $\Gamma_{1}$ irreducible representation of the $D_{2}$ point group of the molecule and results in the same change $(\delta t)$ in the overlap energy $t$ in all bonds at the same time. In general, we have $\delta t=\varsigma Q$ , where $\varsigma$ is a constant and $Q$ is the scalar eigenvector amplitude (Ref. 1). See the text for details.

## V. THE RAMAN TENSOR OF THE BREATHING MODE

Of all the vibrations possible in the toy molecule, we will consider only one of them, namely, the breathing mode of the molecule depicted in Fig. 3(b). This mode will always existand belongs to the $\Gamma_{1}$ irreducible representation of the $D_{2}$  point group of the molecule. $^{4}$ It is a fully symmetric mode, and the reasons for concentrating our attention on it are as follows.

(1) It is an even mode (with respect to the origin), and therefore it is Raman active. $^{3,6}$

(2) It produces the same effect in all bonds. This is not nec- essarily true even if a mode is even and Raman active, but it allows in this case an easy parameterization of its effect on the electronic structure by a simple scalar change in the overlap interaction energy $t$ .

(3) To a good approximation, we can model the effect of the mode on the electronic structure as a change in the over- lap energy integral $t$ between nearest neighbors, that is, $t \to t+\delta t$ , where $\delta t=\varsigma Q$ , with $\varsigma$ a constant and $Q$ is the scalar amplitude of the vibrational displacement of the nuclei.

(4) We can calculate the Raman tensor of the vibration in a semiclassical approach by expanding the linear optical polarizability [Eq. (20)] in powers of $Q$ (to first order).

This mode produces the same effect in all the bonds, that is, a change in the overlap integral $t$ . According to the phe nomenological theory of Raman scattering, $^{1}$ the Raman po larizability tensor for a given vibration is
$$\hat{\alpha}_{\text {Raman }}(\omega)=\frac{Q}{2} \hat{R}(\omega),\qquad(21)$$
where
$$\hat{R}(\omega)=\left[\frac{\partial \hat{\alpha}(\omega)}{\partial Q}\right]_{Q=0}\qquad(22)$$
is the Raman tensor. Equation (21) for the Raman polariz- ability tensor can be thought of as a Taylor expansion of thelinear optical polarizability $\hat{\alpha}$ in powers of $Q$ when $t \to t$  $+\delta t$ , with $\delta t=\varsigma Q$ . The off-diagonal terms of $\hat{\alpha}_{Raman }(\omega)$ re main zero in the expansion of $\hat{\alpha}(\omega)$ to first order in $Q$ be

cause a change in overlap integrals $t \to t+\delta t$ for all the bonds does not change the symmetry and in particular the parity with respect to the origin of the wave functions. Note that the linear optical polarizability tensor $\hat{\alpha}$ may have a component which is zero, but its derivative with respect to $Q$ might be nonzero. This is not the case here and the Raman tensor $\hat{R}$ remains diagonal.

There are two effects produced by the change $t \to t+\delta t$: An effect coming from the change in the matrix elements and an effect coming from the change in the energies of the levels. It turns out that the change in the matrix elements is dominant in the expansion, and moreover, this often turns out to be the case for more complicated models for the electronic structure the molecules. One advantage of having a simplified version of the electronic structure is that we can establish a link between the effect of a vibration on the structure and its relation to a perturbation of the electronic structure. Otherwise, we could start directly from the classical polarizability and postulate the existence of changes in the parameters in terms of $Q$. These changes appear in this case as purely phenomenological with no real inkling on why they happen. Having a simplified electronic structure provides a much clearer picture of what happens at a microscopic level: A vibration can "modulate" the overlap integrals of the orbitals. This picture provides a microscopic description of what is termed in solid-state theory as the electron-phonon interaction, which is required to explain the Raman effect in quantum mechanical terms.

It is possible to show that the leading terms in the expansion of the linear polarizability as a function of $Q$ have the form

$$
\begin{aligned}
\hat{\alpha}_{\text{Raman}}(\omega) & =\left(\begin{array}{cc}
\alpha_{x x}^{R}(\omega) & 0 \\
0 & \alpha_{y y}^{R}(\omega)
\end{array}\right) \quad(23 \mathrm{a}) \\
& =R_{0}\left(\begin{array}{cc}
\frac{1}{\gamma+\kappa-\hbar \omega-i \Gamma} & 0 \\
0 & \frac{1}{-\gamma+\kappa-\hbar \omega-i \Gamma},
\end{array}\right),
\end{aligned}
$$

where $R_{0}$ is a constant $^{16}$ proportional to the scalar mode amplitude $Q$. We included in the matrix only those terms with the frequency dependences in the denominators, whose influence we will study.

From Eqs. (23) we deduce that ignoring $\Gamma$ for the rest of the argument

$$
\frac{\alpha_{y y}^{R}}{\alpha_{x x}^{R}}=\frac{\omega_{13}-\omega}{\omega_{12}-\omega},
$$

which is the most important result of this derivation and shows how the ratio of the two components of the Raman polarizability tensor behave as a function of $\omega$ and, in particular, what happens when a resonant condition is approached. Specifically, if $\omega \to 0$ and $\omega_{13} \approx \omega_{12}$, that is, far from resonance, we have $\alpha_{y y}^{R} / \alpha_{x x}^{R} \approx \omega_{13} / \omega_{12}$. For the parameters in Fig. 2, both components differ by $\approx 20 \%$. In general, both components may be comparable due to the fact that the small splitting in energy between $\hbar \omega_{12}$ and $\hbar \omega_{13}$ does not play a crucial role when $\hbar \omega$ is much smaller than both of them. Hence, far from resonance, we expect

$$
\hat{\alpha}_{\text{Raman}}(\omega) \propto\left(\begin{array}{cc}
\beta_{1} & 0 \\
0 & \beta_{2}
\end{array}\right),
$$

with $\beta_{1} \approx \beta_{2}$. If the splitting is really small, we can achieve a condition where

$$
\hat{\alpha}_{\text{Raman}}(\omega) \propto\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right).
$$

In this case the Raman polarizability tensor for the breathing mode can be completely isotropic.

In contrast, if $\omega \to \omega_{12}$ and $\omega_{13}>\omega_{12}$, that is, the first dipole allowed transition is approached from below in energy, the effect of the splitting between $\omega_{12}$ and $\omega_{13}$ is increased close to resonance, and there is a complete dominance of the effect of the closest transition to $\omega$. In this case according to Eq. (24) $\alpha_{x x}^{R} \gg \alpha_{y y}^{R}$ and

$$
\hat{\alpha}_{\text{Raman}}(\omega) \propto\left(\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right).
$$

In other words, the Raman tensor is transformed from a fully symmetric almost isotropic in many cases tensor far away from resonance [Eq. (26)] to a highly uniaxial tensor [Eq. (27)] when the first dipole allowed transition is approached. This conclusion is general.

From the point of view of molecular Raman scattering, there is some limited information on the symmetry of the modes in the depolarization ratio $\rho$ of the bare molecules, which is a classic topic in molecular spectroscopy. $^{1,3,5}$ Normal depolarization ratios are in the range $0<\rho<3 / 4$ for different types of vibrations with different symmetries. A few special cases are $\rho=0$, which occurs for totally symmetric tensors such as Eq. (26) but in three dimensions, $\rho=3 / 4$, which occurs for traceless Raman tensors, and $\rho=1 / 3$, which occurs for uniaxial tensors where one of the components is dominant such as Eq. (27) but in three dimensions. Our previous results suggest that modes will usually have a frequency dependent depolarization ratio. For example, the case of the breathing mode we have treated suggests that it will have a depolarization ratio close to zero far from resonance and close to $1 / 3$ when the first dipole allowed transition is approached. This fact is observed experimentally in many cases, and it can be taken as a rough measure of the degree of symmetry breakdown that is present under some experimental conditions involving resonances.

### VI. REAL MOLECULES AND DENSITY FUNCTIONAL THEORY CALCULATIONS

Conventional density functional theory calculations of the electronic structure of molecules $^{1,17}$ share some of the limitations of the examples we have considered. For example, they will not include-in their simplest forms-any vibronic coupling. $^{2,3}$ Still, density functional theory produces a much more realistic electronic wave function constructed from more atomic orbitals per site and a self-consistent electronic field in a geometry-optimized structure. $^{1,2}$ The calculation of Raman depolarization ratios as a function of excitation wavelengths can be performed with available software, and it is possible to show the same effect of the change in symmetry in the Raman polarizabilities approaching a uniaxial tensor near a resonance condition, which is the same effect revealed in our toy molecule. The calculation of this effect can be an exercise where students match what density functional

![](./images/811805371084570624_6.jpg)

Fig. 4. (a) Raman tensor representations of four characteristic modes of benzenethiol for different excitation wavelengths. To represent the tensors we plot the $x$-$y$ projection of $|\mathbf{e} \cdot \hat{R} \cdot \mathbf{e}|^{2}$, where $\mathbf{e}$ is a unit vector with varying orientations (Ref. 1). The $x$-$y$ plane coincides with the molecular plane. This representation of the tensors is well suited to highlight the changes in symmetry introduced by different resonance conditions. (b) Vibrational displacement eigenvectors of the four modes studied here. The coordinate systems for the tensor projections and the vibrational displacement are the same.

theory programs predict for simple molecules with a simpler phenomenology such as the one presented in this paper.

As an example, we briefly discuss the case of benzenethiol ($\mathrm{C}_{6}\mathrm{H}_{5}\mathrm{SH}$). The reasons for choosing this molecule (besides the obvious advantage of it being small) will become clear later. We calculated the Raman frequencies and tensors (which yield Raman activities and depolarization ratios $^{1,5}$) via density functional theory. $^{18-23}$ The conclusions should be taken with care due to the intrinsic limitations of the methods involved in these calculations, but they provide an exemplary case study of symmetry breakdown under resonance conditions.

The calculations were performed for a set of excitation wavelengths from the static case ($\lambda_{\mathrm{exc}} \to \infty$) toward higher energies (shorter wavelengths) approaching resonance. The resonance frequencies were determined via time-dependent density functional theory, with the energetically lowest (dipole allowed) transitions at 262, 261, and 240 nm, respectively, and with (relative) oscillator strengths of 0.0134, 0.0026, and 0.2164. The first transition has an electric dipole moment well-aligned ($\Delta\phi=8^{\circ}$) with the $x$-axis (short axis of the molecule in the molecular plane), the much weaker second transition dipole is parallel to the $z$-axis (out of plane), and the strong transition at 240 nm is aligned with the $y$-axis ($\Delta\phi=0.2^{\circ}$) and thus parallel to the long axis of the molecule (see Fig. 4).

The drastic effect of resonance regarding the change of the intrinsic symmetry of the different modes is summarized in Figs. 4 and 5. When going from off-resonance (static) to near-resonance (280 nm) excitation, the Raman activity (proportional to the cross sections of the modes $^{1,3}$) slowly increases—up to a factor of $\approx 30$ with respect to the static field case [see Fig. 5(a)]—and the symmetry of the modes changes, which is also evident in the slight change in the "shape" of the tensors (see Fig. 4). Upon reaching the first two transitions at $\approx 260$ nm, the Raman activity increases by a factor of $\approx 2 \times 10^{4}$. At 250 nm the Raman activity goes over the first (weak) dipole allowed resonance at $\approx 260$ nm, and a drop in the Raman activities is observed. The depolarization ratios of all modes, however, approach the value of 1/3. The transition at 240 nm is by far the strongest in this region, and accordingly, it completely dominates the tensor symmetry (depolarization ratios$=1/3$ for all modes, and all tensors aligned with the transition dipole, that is, along the long axis of the molecule).

![](./images/811805371084570624_7.jpg)

Fig. 5. Simulated resonance behavior of the selected modes of benzenethiol. Plotted are the relative changes in the (a) Raman activity (Ref. 1) and (b) the depolarization ratio $\rho$ as a function of the excitation wavelength $\lambda$ for four characteristic modes (the vibrational frequencies given on the top-right corner). The relative change in the Raman activity is evaluated with respect to that at the 900 nm excitation, which is almost identical to the static field ($\lambda \to \infty$) results. The dominance of the approach to the resonance at 240 nm becomes apparent in the depolarization ratio, which changes rapidly close to it and modifies all values of the depolarization ratios $\rho$ to be exactly 1/3 at resonance (240 nm). This behavior is produced by the highly uniaxial character of all tensors at resonance irrespective of their intrinsic symmetries. The mode at $1627\ \mathrm{cm}^{-1}$ shows a competition between two resonant behaviors, as explained in the text.

The vibration at $1626\ \mathrm{cm}^{-1}$ shows an interesting behavior, which can be understood in terms of resonance phenomena and deserves an additional comment. It will also justify the choice of benzenethiol for this example. The mode at $1626\ \mathrm{cm}^{-1}$ is dominantly coupled to the transition dipole at $\approx 240$ nm far from resonance. This fact is evidenced, for example, in the shape of the Raman tensor representations in Fig. 4; at 600 and 280 nm (far from resonance), the tensor's main axis is predominantly along the vertical direction ($y$-axis). However, benzenethiol, unlike benzene, is not a perfectly symmetric molecule (because of the asymmetry introduced by the thiol group), and as a result, the symmetry

classification of the modes is not exact, and there is always a small amount of coupling to other transitions. The Raman tensor of the $1626\ \text{cm}^{-1}$ mode is weakly coupled to the transition at $\approx$260 nm. Close to $\approx$260 nm the weaker coupling to that resonance dominates the behavior of the tensor to the extent that its main axis changes to be along the $x$-axis of the molecule (which is the dipole direction for the $\approx$260 nm transition). This competition between the weak coupling to the $\approx$260 nm transition with the stronger coupling to the dominant one at $\approx$240 nm is also responsible for the "bump" in the depolarization ratio observed for the $1626\ \text{cm}^{-1}$ mode in Fig. 5. A similar phenomenon exists for the $\approx$706 $\text{cm}^{-1}$ mode, but in this case the mode is more strongly coupled to the $\approx$260 nm transition when it is far from resonance and only changes its main axis when reaching the (dominant) transition at $\approx$240 nm (Fig. 5).

## VII. CONCLUSIONS

Several general conclusions on resonant Raman phenomena can be obtained from this study. The most important is that resonance phenomena can effectively change the depolarization ratios (and therefore the intrinsic symmetry) of the Raman modes. We showed for the model calculation how a molecule with two dipoles allowed transition results in a Raman tensor for the breathing mode that is almost isotropic far from resonance to one that is mainly uniaxial when the lowest dipole allowed transition is approached. This phenomenology is also observed for depolarization ratios calculated with density functional theory as a function of wavelength, even though the underlying reasons for this behavior are hidden by the complexity of these calculations. Issues related to symmetries of polarizabilities under resonant conditions are important in many areas of modern spectroscopy, most notably in the emerging field of single-molecule Raman spectroscopy. $^{1,24}$ A qualitative microscopic understanding of these phenomena is desirable for understanding the output of more sophisticated numerical methods (such as density functional theory) and, ultimately, the most important objective, which is understanding (at least conceptually) the origin of experimental observations.

$^{\text{a})}$Electronic mail: Pablo.Etchegoin@vuw.ac.nz
$^{\text{b})}$Electronic mail: Eric.LeRu@vuw.ac.nz
$^{1}$E. C. Le Ru and P. G. Etchegoin, *Principles of Surface Enhanced Raman Spectroscopy and Related Plasmonic Effects* (Elsevier, Amsterdam, 2009).
$^{2}$P. W. Atkins and R. S. Friedman, *Molecular Quantum Mechanics*, 4th ed. (Oxford U. P., New York, 2005).
$^{3}$D. A. Long, *The Raman Effect: A Unified Treatment of the Theory of Raman Scattering by Molecules* (Wiley, Chichester, 2002).
$^{4}$M. Tinkham, *Group Theory and Quantum Mechanics* (McGraw-Hill, New York, 1964).
$^{5}$W. Hayes and R. Loudon, *Scattering of Light by Crystals* (Wiley, New York, 1975).
$^{6}$S. P. S. Porto, "Angular dependence and depolarization ratio of the Raman effect," J. Opt. Soc. Am. **56**, 1585–1589 (1966).
$^{7}$N. W. Ashcroft and N. D. Mermin, *Solid State Physics* (Harcourt Brace, New York, 1976).
$^{8}$O. Madelung, *Introduction to Solid-State Theory* (Springer-Verlag, Berlin, 1981).
$^{9}$T. Engel, *Quantum Chemistry and Spectroscopy* (Pearson/Benjamin Cummings, San Francisco, 2005).
$^{10}$Parity is expected to be the natural way of classifying states for molecular structures that possess a center of inversion. Although this point is a general topic of group theory, we shall only use it here in its most basic form and shall not dwell further into symmetry-related issues.
$^{11}$L. D. Landau and E. M. Lifshitz, *Quantum Mechanics* (Elsevier, Amsterdam, 2003).
$^{12}$K. D. Bonin and V. V. Kresin, *Electric-Dipole Polarizabilities of Atoms, Molecules and Clusters* (World Scientific, Singapore, 1997).
$^{13}$L. D. Landau, E. M. Lifshitz, and L. P. Pitaevskiĭ, *Electrodynamics of Continuous Media* (Elsevier, Amsterdam, 2004).
$^{14}$T. G. Spiro and P. Stein, "Resonance effects in vibrational scattering from complex molecules," Annu. Rev. Phys. Chem. **28**, 501–521 (1977).
$^{15}$P. Y. Yu and M. Cardona, *Fundamentals of Semiconductors: Physics and Materials Properties* (Springer, Berlin, 2004).
$^{16}$The exact form of $R_{0}$ in terms of $\gamma$, $\kappa$, and $t$ is lengthy, does not add to the principal point, and is omitted here. It can be easily obtained from the prefactor in Eq. (15) by replacing $t$ by $t+\delta t$ (also in the expression for $\kappa$) and using the command "Taylor" in MATLAB (to expand the expression in powers of $\delta t$).
$^{17}$R. M. Dreizler and E. K. U. Gross, *Density Functional Theory: An Approach to the Quantum Many-Body Problem* (Springer-Verlag, Berlin, 1990).
$^{18}$We used GAUSSIAN03 with the B3LYP method and the basis set 6-311++G(d,p). For the excitation frequency dependence, the coupled-perturbed Hartree–Fock method was used.
$^{19}$M. J. Frisch *et al.*, GAUSSIAN 03 Revision C.02, ⟨www.gaussian.com/⟩.
$^{20}$A. D. Becke, "Density-functional thermochemistry. III. The role of exact exchange," J. Chem. Phys. **98**, 5648–5652 (1993).
$^{21}$C. Lee, W. Yang, and R. G. Parr, "Development of the Colle–Salvetti correlation-energy formula into a functional of the electron density," Phys. Rev. B **37**, 785–789 (1988).
$^{22}$R. Krishnan, J. Stephen Binkley, R. Seeger, and John A. Pople, "Self-consistent molecular orbital methods. XX. A basis set for correlated wave functions," J. Chem. Phys. **72**, 650–654 (1980).
$^{23}$J. Gerratt and I. M. Mills, "Force constants and dipole-moment derivatives of molecules from perturbed Hartree–Fock calculations. I," J. Chem. Phys. **49**, 1719–1729 (1968).
$^{24}$P. G. Etchegoin and E. C. Le Ru, "A perspective on single molecule SERS: current status and future challenges," Phys. Chem. Chem. Phys. **10**, 6079–6089 (2008).