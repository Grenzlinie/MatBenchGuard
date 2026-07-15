This article was downloaded by: [Moskow State Univ Bibliote]
On: 09 February 2014, At: 09:24
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/811835190153314305_1.jpg)

Molecular Physics: An International Journal at the Interface Between Chemistry and Physics

Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/tmph20

The calculation of molecular geometrical properties in the Hellmann–Feynman approximation

VebjØSRN Bakken $^{a}$ , Trygve Helgaker $^{a}$ , Wim Klopper $^{a}$ & Kenneth Ruud $^{a}$

$^{a}$ Department of Chemistry, University of Oslo, Oslo, Norway
Published online: 04 Mar 2011.

To cite this article: VebjØSRN Bakken, Trygve Helgaker, Wim Klopper & Kenneth Ruud (1999) The calculation of molecular geometrical properties in the Hellmann–Feynman approximation, Molecular Physics: An International Journal at the Interface Between Chemistry and Physics, 96:4, 653-671, DOI: 10.1080/00268979909483002

To link to this article: http://dx.doi.org/10.1080/00268979909483002

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

**MOLECULAR PHYSICS, 1999, VOL. 96, NO. 4, 653-671**

# The calculation of molecular geometrical properties in the Hellmann-Feynman approximation

VEBJØRN BAKKEN, TRYGVE HELGAKER, WIM KLOPPER and KENNETH RUUD

Department of Chemistry, University of Oslo, PO Box 1033 Blindern, N-0315 Oslo, Norway

(Received 28 May 1998; revised version accepted 6 July 1998)

The ab initio calculation of molecular geometrical properties in the Hellmann-Feynman approximation is discussed in which the atomic orbitals are fixed at the positions of the nuclei at the reference geometry, thereby avoiding the calculation of derivatives of the molecular integrals with respect to the positions of the atomic orbitals. For the molecular gradient, the molecular Hessian, and the molecular dipole gradient, the convergence of the calculated properties is studied for a large number of basis sets at the Hartree-Fock level and at the CCSD(T)-R12 level. In the Hellmann-Feynman approximation, it is found to be necessary to impose explicitly rotational and translational invariance. Although small basis sets perform poorly in the Hellmann-Feynman approximation (compared with the standard approach where the atomic orbitals are moving with the displaced nuclei), satisfactory convergence is obtained for geometries and harmonic frequencies (to within 1% of the standard approximation) with the larger of the correlation-consistent core-valence cc-pCVXZ basis sets. For the infrared intensities, the agreement with the standard approach is still poor (only within 15% for the largest correlation-consistent basis). The best results are obtained with an R12 basis previously developed for the calculation of energies in the explicitly correlated R12 approximation. In this basis, the geometrical parameters and harmonic frequencies are within 0.5% of the standard approach and the infrared intensities within 5%, suggesting that the Hellmann-Feynman approximation may be useful for applications at the highly accurate MP2-R12, CCSD-R12, and CCSD(T)-R12 levels of theory.

## 1. Introduction
According to the Hellmann-Feynman theorem [1,2], we may calculate the force acting on a nucleus in a molecular system as the expectation value of the field at the nucleus multiplied by the nuclear charge. Since the operator for the field is a simple one-electron operator, the Hellmann-Feynman theorem opens up the possibility for an efficient calculation of molecular forces.

Unfortunately, the conditions that must be satisfied for the Hellmann-Feynman theorem to be applied are rather strict. Each parameter entering the wavefunction must be either variationally determined or else unaffected by the nuclear distortion. Indeed, these conditions are not satisfied for the calculation of geometrical derivatives by the standard wavefunctions of quantum chemistry, where the molecular orbitals are expanded in a finite set of atomic orbitals (AOs) fixed on the atomic nuclei. As the molecule distorts, the AOs move with the nuclei and thus their positions are neither variationally determined nor fixed in space. Consequently, the Hellmann-Feynman theorem cannot be applied. Instead, the nuclear forces must be evaluated by a more elaborate scheme, which takes into account the displacement of the AOs as the molecule distorts [3]. In practice, the calculation of molecular forces (molecular gradients) for such wavefunctions becomes rather time-consuming, requiring the evaluation of the derivatives of all molecular integrals with respect to the nuclear positions. A further complication arises since, upon displacement of the nuclei, the molecular orbitals (which are expanded in the AOs) do not remain orthonormal. Orthonormality constraints must therefore be applied, introducing terms that involve derivatives of the overlap matrix [3].

Nowadays, programs have been developed that calculate molecular forces efficiently for all the standard wavefunctions of quantum chemistry, using analytical rather than numerical techniques [4,5]. Moreover, for many approximations, also the force constants (molecular Hessian) may be calculated efficiently by analytical techniques [6,7], although the higher complexity of the Hessian evaluation means that often Hessians are obtained by numerical differentiation of analytically calculated gradients. For the evaluation of anharmonicities

0026-8976/99 $12.00 © 1999 Taylor & Francis Ltd.

(i.e., derivatives higher than second), very few programs have been developed, and then only at the Hartree-Fock level [8, 9]. Thus, although the difficulties introduced by fixing the AOs on the nuclei can be solved quite effi- ciently at the gradient level, to higher orders, the com- plexity of the calculations becomes so great that no attempts have been made at calculating these properties analytically. Moreover, for certain highly complex wavefunctions, the explicitly correlated wavefunctions, for example, no implementation exists even at the gra- dient level, and the evaluation of geometrical derivatives must be carried out numerically.

Clearly, it would be advantageous if it were possible to calculate the molecular gradients from the simple Hellmann-Feynman expression and the higher deriva- tives from the corresponding expressions of higher order perturbation theory. Not only would we then be able to calculate molecular gradients more easily from complex wavefunctions, but also we would be able to calculate routinely a large number of higher order properties that involve mixed perturbation operators, some of which are nuclear displacements. Since the geometrical distor- tion operators are simple multiplicative one-electron operators, the evaluation of for example anharmonicity corrections to harmonic frequencies and double-har- monic infrared intensities or vibrational corrections to electric polarizabilities would be a relatively straightfor- ward matter, incorporated readily into a general scheme for the evaluation of one-electron molecular properties [10, 11].

In the present paper, we shall consider the evaluation of geometrical molecular properties by the application of the Hellmann-Feynman theorem. For the standard models of ab initio theory, the application of the Hell- mann-Feynman theorem is tantamount to assuming that the AOs do not follow the nuclei as these distort upon perturbation, but instead remain fixed at their original positions in the undistorted system. In the limit of a complete basis, the position of the AOs does not matter and the application of the Hellmann- Feynman theorem then yields the same forces as a numerical differentiation of the molecular electronic energy. For finite basis sets, however, the results obtained by application of the Hellmann-Feynman the- orem and by differentiation will differ. An important aspect of the present investigation is therefore to inves- tigate what basis sets are needed for the Hellmann- Feynman forces to be equivalent to the energy gradient.

Comparisons of Hellmann-Feynman forces and energy gradients have appeared in the literature before. In particular, we draw attention to the papers by Nakatsuji and coworkers [12-14], who explored the use of the Hellmann-Feynman approximation for the calculation of molecular gradients. These authors intro- duced special 'family' basis sets so as to satisfy as closely as possible the conditions of the Hellmann-Feynman theorem. These family basis sets were obtained by including the derivatives of the AOs of the original 'parent' basis and were shown to give a significant improvement in the description of the Hellmann- Feynman forces [12]. However, these investigations are now rather old. Modern calculations usually are carried out using larger basis sets than fifteen years ago. It is therefore of interest to compare the Hellmann-Feynman forces and energy gradients again, in order to see how modern, larger basis sets perform for the Hellmann- Feynman forces. Of particular interest are the new hier- archical basis sets such as the atomic natural orbitals (ANOs) of Almlöf and Taylor [15] and the correlation- consistent basis sets of Dunning and coworkers [16-19]. These basis sets allow for a systematic improvement in the description of the electronic structure towards the limit of an infinite basis set, at least for the correlation energy. Experience has shown that a similar systematic improvement in the description is observed for a variety of molecular properties as well [18, 23-25], in particular for the correlation-consistent sets, for which special modifications exist to improve the descriptions of the outer-valence [18], inner-valence [17], and core regions [20].

This paper differs from the work of Nakatsuji and coworkers in the following respects. First, we consider the evaluation of both first- and second-order properties in the Hellmann-Feynman approximation: the molecu- lar gradient, the molecular Hessian, and the molecular dipole gradient. Second, we do not consider the use of special 'family' basis sets as generated by differentiation, but rather the calculation of these properties using the standard basis sets of quantum chemistry. Finally, we consider the calculation of Hellmann-Feynman proper- ties for highly accurate, explicitly correlated wavefunc- tions.

## 2. Theory
We begin this section by discussing the Hellmann- Feynman theorem and the Hellmann-Feynman approx- imation. Next, we consider the evaluation of molecular gradients, molecular Hessians, and dipole gradients in the Hellmann-Feynman approximation, discussing the operators needed for their evaluation and the expected basis-set convergence of these properties in the Hell- mann-Feynman approximation. A naïve treatment in a Cartesian frame is not translationally and rotationally invariant. This lack of invariance is a feature of the Hellmann-Feynman approximation that deserves atten- tion, and such a non-invariant theory can be only pre- liminary. Therefore, we conclude this section with a

discussion on how to impose translational and rota- tional symmetry in the calculated properties.

### 2.1. The Hellmann-Feynman theorem
Let us assume that, in a given approximation of *ab initio* theory, the molecular electronic energy is calculated as the expectation value of the electronic Hamiltonian

$$
E = \langle 0|\hat{H}|0\rangle. \tag{1}
$$

According to the Hellmann-Feynman theorem [1, 2], we may calculate the total derivatives of the electronic energy as the expectation values of the corresponding derivatives of the Hamiltonian

$$
\frac{\mathrm{d}E}{\mathrm{d}x} = \left\langle 0\left|\frac{\mathrm{d}\hat{H}}{\mathrm{d}x}\right|0\right\rangle, \tag{2}
$$

provided that the parameters that determine the wave- function are either variationally optimized for each value of $x$ or else independent of $x$. This result follows by expanding the total derivatives of the energy in par- tial derivatives

$$
\frac{\mathrm{d}E}{\mathrm{d}x} = \frac{\partial E}{\partial x} + \sum_{i} \frac{\partial E}{\partial \lambda_{i}} \frac{\partial \lambda_{i}}{\partial x}, \tag{3}
$$

where $\lambda_{i}$ are the wavefunction parameters. Clearly, the contribution from the $i$th wavefunction parameter $\lambda_{i}$ vanishes either if the energy is optimized with respect to this parameter,

$$
\frac{\partial E}{\partial \lambda_{i}} = 0, \tag{4}
$$

or if the parameter itself is unaffected by the distortion,

$$
\frac{\partial \lambda_{i}}{\partial x} = 0. \tag{5}
$$

Unless these Hellmann-Feynman conditions are satis- fied for all $\lambda_{i}$, we cannot evaluate the derivative from the Hellmann-Feynman expression (2) [21].

Obviously, the Hellmann-Feynman conditions are satisfied for the exact wavefunction. These conditions are satisfied also by many approximate wavefunctions, for example the numerical Hartree-Fock wavefunction [22]. However, for wavefunctions expanded in a finite set of analytical AOs fixed on the nuclear centres, the Hellmann-Feynman conditions are not satisfied for geo- metrical derivatives. Instead, we must take into account in our calculations the contributions from the deriva- tives of the AOs to the molecular gradient, complicating our calculation of molecular forces considerably.

### 2.2. The Hellmann-Feynman approximation
In view of the simplicity of the Hellmann-Feynman expression (2), it appears worthwhile to explore wave- function models for which the Hellmann-Feynman con- ditions are satisfied for nuclear displacements. Indeed, it is simple to set up a model for which the Hellmann- Feynman conditions are satisfied rigorously for molecu- lar forces.

Let us assume that the molecular properties are cal- culated at some reference geometry where the Cartesian nuclear coordinates are given by $\mathbf{R}_{I}$. In the Hellmann- Feynman approximation, we assume that, as the mol- ecule distorts, the AOs are not allowed to follow the nuclei but are instead kept fixed at the positions of the reference geometry $\mathbf{R}_{I}$. Since the AOs are fixed in space, the Hellmann-Feynman conditions are rigorously satis- fied and we may calculate forces according to equation (2). Obviously, the numbers obtained in the Hellmann- Feynman approximation will be different from those obtained by analytical differentiation of the electronic energy (with the AOs moving with the displaced nuclei). In particular, whereas the description of the electronic system in the Hellmann-Feynman approxi- mation is biased towards the unperturbed system, no such bias is present in the standard approach, where the AOs are fixed on the nuclei rather than at the refer- ence geometry. Therefore, as we increase the AO basis, we expect the properties calculated in the Hellmann- Feynman approximation to converge slower to the basis set limit than the properties calculated in the stan- dard approach. However, for a sufficiently large basis, the two approaches become equivalent as the orbital space spanned by the AOs becomes more and more saturated.

### 2.3. Derivatives of the electronic Hamiltonian
In atomic units, the non-relativistic spin-free elec- tronic Hamiltonian operator for a molecular electronic system in the presence of an external electric field $\mathbf{F}$ is given as

$$
\begin{aligned}
\hat{H}(\boldsymbol{\alpha}_{I}, \mathbf{F}) =& -\frac{1}{2} \sum_{i} \nabla_{i}^{2} - \sum_{i,I} \frac{Z_{I}}{\left|\mathbf{r}_{i} - \left(\mathbf{R}_{I} + \boldsymbol{\alpha}_{I}\right)\right|} \\
&+ \sum_{i>j} \frac{1}{\left|\mathbf{r}_{i} - \mathbf{r}_{j}\right|} + \sum_{I>J} \frac{Z_{I}Z_{J}}{\left|\left(\mathbf{R}_{I} + \boldsymbol{\alpha}_{I}\right) - \left(\mathbf{R}_{J} + \boldsymbol{\alpha}_{J}\right)\right|} \\
&+ \mathbf{F} \cdot \sum_{i} \mathbf{r}_{i} - \mathbf{F} \cdot \sum_{I} Z_{I}(\mathbf{R}_{I} + \boldsymbol{\alpha}_{I}) \tag{6}
\end{aligned}
$$

where $\mathbf{r}_{i}$ are the electronic coordinates, $\mathbf{R}_{I}$ the nuclear coordinates of the reference geometry, $\boldsymbol{\alpha}_{I}$ the nuclear displacement coordinates, and $Z_{I}$ the nuclear charges. In the notation

$$
\mathbf{r}_{i I}=\mathbf{r}_{i}-\mathbf{R}_{I}, \tag{7}
$$

$$
\mathbf{R}_{I J}=\mathbf{R}_{I}-\mathbf{R}_{J}, \tag{8}
$$

the first derivatives of the Hamiltonian are given by

$$
\left.\frac{\mathrm{d} \hat{H}}{\mathrm{d} \boldsymbol{\alpha}_{I}}\right|_{\mathbf{0}}=-Z_{I} \sum_{i} \frac{\mathbf{r}_{i I}}{r_{i I}^{3}}-Z_{I} \sum_{K \neq I} \frac{Z_{K} \mathbf{R}_{I K}}{R_{I K}^{3}} \tag{9}
$$

$$
\left.\frac{\mathrm{d} \hat{H}}{\mathrm{d} \mathbf{F}}\right|_{\mathbf{0}}=\sum_{i} \mathbf{r}_{i}-\sum_{I} Z_{I} \mathbf{R}_{I} \tag{10}
$$

where the differentiations have been carried out for the reference geometry and at zero electric field. The operator in equation (9) is the operator for the electric field at the position of the $I$th nucleus, with contributions from all the electrons and from the remaining nuclei. The operator in equation (10) is the dipole moment operator, with contributions from all the electrons and all the nuclei. For the reference geometry and at zero field, the nonzero second derivatives of the Hamiltonian are

$$
\begin{aligned}
\left.\frac{\mathrm{d}^{2} \hat{H}}{\mathrm{d} \boldsymbol{\alpha}_{I}^{2}}\right|_{\mathbf{0}} & =\frac{4 \pi}{3} Z_{I} \mathbf{I}_{3} \sum_{i} \delta\left(r_{i I}\right)-Z_{I} \sum_{i} \frac{3 \mathbf{r}_{i I} \mathbf{r}_{i I}^{T}-r_{i I}^{2} \mathbf{I}_{3}}{r_{i I}^{5}} \\
& +Z_{I} \sum_{K \neq I} Z_{K} \frac{3 \mathbf{R}_{I K} \mathbf{R}_{I K}^{T}-R_{I K}^{2} \mathbf{I}_{3}}{R_{I K}^{5}}, \tag{11}
\end{aligned}
$$

$$
\left.\frac{\mathrm{d}^{2} \hat{H}}{\mathrm{d} \boldsymbol{\alpha}_{I} \mathrm{~d} \boldsymbol{\alpha}_{J}}\right|_{\mathbf{0}}=-Z_{I} Z_{J} \frac{3 \mathbf{R}_{I J} \mathbf{R}_{I J}^{T}-R_{I J}^{2} \mathbf{I}_{3}}{R_{I J}^{5}}, \tag{12}
$$

$$
\left.\frac{\mathrm{d}^{2} \hat{H}}{\mathrm{d} \boldsymbol{\alpha}_{I} \mathrm{~d} \mathbf{F}}\right|_{\mathbf{0}}=Z_{I} \mathbf{I}_{3}, \tag{13}
$$

where $\mathbf{I}_{3}$ is the $3 \times 3$ unit matrix. The second derivative with respect to the coordinates of the $I$th nucleus (equation (11)) is a rather complicated operator, containing a Coulomb contact term and a field gradient term (with contributions from the electrons and the remaining nuclei). By contrast, the second derivative with respect to the simultaneous displacements of two different nuclei and with respect to the displacement of one nucleus and the field are simple operators, with no contributions from the electrons. It should be noted further that the arguments given here for the use of the Hellmann-Feynman approximation are valid also for $a b$ initio models in which the energies are not given as expectation values but instead obtained from some other energy functional, e.g., for coupled-cluster energies.

### 2.4. Molecular properties in the Hellmann-Feynman approximation

The electronic energy of the unperturbed system is given as

$$
\begin{aligned}
E(\mathbf{0}, \mathbf{0})= & \frac{1}{2}\left\langle 0\left|\sum_{i} \nabla_{i}^{2}\right| 0\right\rangle-\left\langle 0\left|\sum_{i, I} \frac{Z_{I}}{r_{i I}}\right| 0\right\rangle \\
& +\left\langle 0\left|\sum_{i>j} \frac{1}{\left|\mathbf{r}_{i}-\mathbf{r}_{j}\right|}\right| 0\right\rangle+\sum_{I>J} \frac{Z_{I} Z_{J}}{R_{I J}}. \quad(14)
\end{aligned}
$$

According to the Hellmann-Feynman theorem equation (2), we may calculate the molecular gradient as a simple one-electron expectation value of the electric field operator (equation (9)):

$$
\left.\frac{\mathrm{d} E}{\mathrm{~d} \boldsymbol{\alpha}_{I}}\right|_{\mathbf{0}}=-Z_{I}\left\langle 0\left|\sum_{i} \frac{\mathbf{r}_{i I}}{r_{i I}^{3}}\right| 0\right\rangle-Z_{I} \sum_{K \neq I} \frac{Z_{K} \mathbf{R}_{I K}}{R_{I K}^{3}}, \quad(15)
$$

in accordance with standard first-order perturbation theory. This expression should be contrasted with the much more complicated expression that arises when we allow the AOs to be displaced with the nuclei [3]. From second-order perturbation theory we obtain the following expressions for the diagonal and non-diagonal elements of the molecular Hessian:

$$
\begin{aligned}
\left.\frac{\mathrm{d}^{2} E}{\mathrm{~d} \boldsymbol{\alpha}_{I}^{2}}\right|_{\mathbf{0}}= & \frac{4 \pi}{3} Z_{I} \mathbf{I}_{3}\left\langle 0\left|\sum_{i} \delta\left(r_{i I}\right)\right| 0\right\rangle \\
& -Z_{I}\left\langle 0\left|\sum_{i} \frac{3 \mathbf{r}_{i I} \mathbf{r}_{i I}^{T}-r_{i I}^{2} \mathbf{I}_{3}}{r_{i I}^{5}}\right| 0\right\rangle \\
& +Z_{I} \sum_{K \neq I} Z_{K} \frac{3 \mathbf{R}_{I K} \mathbf{R}_{I K}^{T}-R_{I K}^{2} \mathbf{I}_{3}}{R_{I K}^{5}} \\
& -2 Z_{I}^{2} \sum_{n} \frac{\left\langle 0\left|\sum_{i} \frac{\mathbf{r}_{i I}}{r_{i I}^{3}}\right| n\right\rangle\left\langle n\left|\sum_{i} \frac{\mathbf{r}_{i I}^{T}}{r_{i I}^{3}}\right| 0\right\rangle}{E_{n}-E_{0}}, \quad(16)
\end{aligned}
$$

$$
\begin{aligned}
\left.\frac{\mathrm{d}^{2} E}{\mathrm{~d} \boldsymbol{\alpha}_{I} \mathrm{~d} \boldsymbol{\alpha}_{J}}\right|_{\mathbf{0}}= & -Z_{I} Z_{J} \frac{3 \mathbf{R}_{I J} \mathbf{R}_{I J}^{T}-R_{I J}^{2} \mathbf{I}_{3}}{R_{I J}^{5}} \\
& -2 Z_{I} Z_{J} \sum_{n} \frac{\left\langle 0\left|\sum_{i} \frac{\mathbf{r}_{i I}}{r_{i I}^{3}}\right| n\right\rangle\left\langle n\left|\sum_{i} \frac{\mathbf{r}_{i J}^{T}}{r_{i J}^{3}}\right| 0\right\rangle}{E_{n}-E_{0}} .
\end{aligned}
$$

Finally, for the dipole gradient, we obtain in the Hellmann-Feynman approximation:

$$
\left.\frac{\mathrm{d}^{2} E}{\mathrm{~d} \boldsymbol{\alpha}_{I} \mathrm{~d} \mathbf{F}}\right|_{\mathbf{0}}=Z_{I} \mathbf{I}_{3}-2 Z_{I} \sum_{n} \frac{\left\langle 0\left|\sum_{i} \frac{\mathbf{r}_{i I}}{r_{i I}^{3}}\right| n\right\rangle\left\langle n\left|\sum_{i} \mathbf{r}_{i}^{T}\right| 0\right\rangle}{E_{n}-E_{0}} .
$$

In practice, the second-order properties are not calculated by carrying out a summation over excited states as implied by perturbation theory expressions (16)-(18). Instead, the derivatives are obtained using methods that do not require the explicit calculation of excited states [7]. Still, we have here given only the Rayleigh-Schrödinger expressions, since they indicate clearly the structure of the equations.

### 2.5. Basis set convergence of the Hellmann-Feynman properties

From the expressions above given for the different properties we may draw some conclusions regarding the expected basis set requirements for the calculation of geometrical derivatives in the Hellmann-Feynman approximation. Thus, whereas the calculation of the energy depends on the potential at the nuclei (which scales as $r_{il}^{-1}$), the calculation of the forces depends on the field at the nuclei (which scales as $r_{il}^{-2}$). Clearly, in the evaluation of molecular forces in the Hellmann-Feynman approximation, we sample a different region of the electronic distribution than in the calculation of the energy itself. In particular, we would expect the convergence of the Hellmann-Feynman forces to be more sensitive to the description of the inner regions of the electronic distribution than the calculation of the energy. Since most basis sets have been developed for the calculation of molecular electronic energies (rather than the calculation of the electric field), we expect the convergence of the Hellmann-Feynman forces with respect to the standard basis sets to be slower than the convergence of the electronic energy itself.

Considering the calculation of the Hessian matrix, we note that the diagonal elements of equation (16) depend on the electric field gradient at the nucleus (scaling as $r_{il}^{-3}$) and on the electron density at the nuclei (because of the presence of the Coulomb contact term). In general, the basis set convergence of properties that depend on the electronic wavefunction at a particular point in space is notoriously slow [26]. We would therefore expect the calculation of the diagonal elements of the Hessian to converge slowly. On the other hand, the non-diagonal elements of Hessian (17) have no contact contribution at all. Indeed, from the presence of the electric field operators in the sum-over-states contribution to the Hessian we would expect the non-diagonal elements of the Hessian matrix in the Hellmann-Feynman approximation to converge not significantly slower than the molecular forces in the same approximation.

As a consequence of the different rates of convergence, the translational and rotational invariance of the Hessian in a Cartesian frame is violated. However, we impose translational invariance explicitly by computing the diagonal elements of the Hessian from the expression

$$
\frac{\mathrm{d}^{2} E}{\mathrm{~d} \alpha_{I}^{2}}=-\sum_{K \neq I} \frac{\mathrm{d}^{2} E}{\mathrm{~d} \alpha_{I} \mathrm{~d} \alpha_{K}}. \tag{19}
$$

The difficulties associated with the convergence of the Coulomb-contact term and the electronic contributions to the field gradient are then avoided completely, making the convergence of the Hessian and the vibrational frequencies not significantly slower than for the molecular forces. A general treatment of both translational and rotational invariance for all properties follows in the next subsection.

To illustrate the slow convergence of the Coulomb contact terms, consider the harmonic frequencies in the water molecule. In the cc-pCVQZ basis, the three normal frequencies are $158638 \mathrm{~cm}^{-1}$, $153900 \mathrm{~cm}^{-1}$, and $2783 i \mathrm{~cm}^{-1}$ when calculated from equation (16) in the Hellmann-Feynman approximation. When calculated from equation (19) (still in the Hellmann-Feynman approximation), the frequencies become $4184 \mathrm{~cm}^{-1}$, $4087 \mathrm{~cm}^{-1}$, and $1739 \mathrm{~cm}^{-1}$, only about $1 \%$ away from the Hartree-Fock limit. Clearly, without the use of equation (19) the accurate calculation of molecular Hessians in the Hellmann-Feynman approximation would not be possible.

The problems disussed here do not arise if the molecular Hessian is calculated by differentiation (numerical or analytical) of the Hellmann-Feynman gradient. This mixed approach was used by Nakatsuji *et al.* [14] and is used here also for the CCSD(T)-R12 wavefunction. For the other calculations in this paper (i.e., for all Hartree-Fock calculations), the strict Hellmann-Feynman scheme was used.

### 2.6. Translational and rotational invariance in the Hellmann-Feynman approximation

In the Hellmann-Feynman approximation, there is a strong bias in the description of the electronic system towards the unperturbed system (i.e., the molecule in the reference geometry). Because of this bias, the description is not translationally and rotationally invariant. Thus, if the nuclear displacement represents a simple translation or rotation of the molecule (rather than a true distortion), the calculated energy will not remain constant but change as the AOs become displaced off the nuclei. We shall now see how we may impose the correct translational and rotational symmetries on the molecular gradient, the molecular Hessian, and the dipole gradient.

Let us consider the translational and rotational symmetries of the molecular gradient, the molecular Hessian, and the dipole gradient of a molecular system

containing $N$ atoms. In the following, we shall assume that the molecule has six translational and rotational degrees of freedom. However, the procedure may be modified readily to linear systems, containing only five such degrees of freedom.

In Cartesian coordinates, the molecular gradient is represented by a column vector $\mathbf{g}$ which may be partitioned into $N$ blocks $\mathbf{g}_K$, each of which contains the three Cartesian gradient elements of the $K$th nucleus:

$$
\mathbf{g} = \begin{bmatrix}
\mathbf{g}_1 \\
\vdots \\
\mathbf{g}_N
\end{bmatrix}. \tag{20}
$$

The molecular Hessian is represented by the symmetric $3N \times 3N$ matrix $\mathbf{G}$, which is partitioned in the same manner into $3 \times 3$ matrices $\mathbf{G}_{KL}$, containing the derivatives with respect to nucleus $K$ and nucleus $L$:

$$
\mathbf{G} = \begin{bmatrix}
\mathbf{G}_{11} & \dots & \mathbf{G}_{1N} \\
\vdots & & \vdots \\
\mathbf{G}_{N1} & \dots & \mathbf{G}_{NN}
\end{bmatrix}. \tag{21}
$$

Finally, we represent the molecular dipole gradient by a $3N \times 3$ rectangular matrix $\mathbf{A}$, which may be partitioned as

$$
\mathbf{A} = \begin{bmatrix}
\mathbf{A}_1 \\
\vdots \\
\mathbf{A}_N
\end{bmatrix}, \tag{22}
$$

where $\mathbf{A}_K$ is a $3 \times 3$ square matrix containing the derivatives of the molecular dipole moment $\mathbf{d}$ with respect to the Cartesian coordinates of nucleus $K$. The matrix $\mathbf{A}_K$ is known as the atomic polar tensor (APT) of the $K$th nucleus.

To display the translational and rotational symmetries of these property matrices in a compact form, we introduce the $6 \times 3N$ rectangular matrix

$$
\mathbf{T} = \begin{bmatrix}
\mathbf{T}_1 & \dots & \mathbf{T}_N
\end{bmatrix} \tag{23}
$$

where $K$th block $\mathbf{T}_K$ is a rectangular $6 \times 3$ matrix containing the partial derivatives of the three Cartesian coordinates of the $K$th nucleus with respect to the six translational and rotational coordinates of the molecule. In the notation

$$
\mathbf{v} \times = \begin{bmatrix}
0 & -v_z & v_y \\
v_z & 0 & -v_x \\
-v_y & v_x & 0
\end{bmatrix} \tag{24}
$$

the blocks of the $\mathbf{T}$ matrix may be written as

$$
\mathbf{T}_K = \begin{bmatrix}
\mathbf{I}_3 \\
\mathbf{R}_{K} \times
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
0 & -Z_K & Y_K \\
Z_K & 0 & -X_K \\
-Y_K & X_K & 0
\end{bmatrix}. \tag{25}
$$

The translational and rotational symmetries of the gradient, Hessian, and dipole gradient may now be written compactly as

$$
\mathbf{Tg} = \mathbf{0}, \tag{26}
$$

$$
\mathbf{TG} = \mathbf{M}, \tag{27}
$$

$$
\mathbf{TA} = \mathbf{N}, \tag{28}
$$

where we have introduced the matrices

$$
\mathbf{M} = \begin{bmatrix}
\mathbf{0}_3 & \dots & \mathbf{0}_3 \\
\mathbf{g}_1 \times & \dots & \mathbf{g}_N \times
\end{bmatrix}, \tag{29}
$$

$$
\mathbf{N} = \begin{bmatrix}
q\mathbf{I}_3 \\
\mathbf{d} \times
\end{bmatrix}, \tag{30}
$$

with $q$ the total charge of the system. We note here that relations (26)-(28) follow by expanding the total derivatives of the molecular properties (in this case the energy, the molecular gradient, and the molecular dipole moment, respectively) with respect to the six translational and rotational coordinates (the RHS of the equations) in the partial derivatives with respect to the $3N$ Cartesian coordinates of the system (the LHS of the equations). For more details on the translational and rotational symmetries of these matrices, please refer to Helgaker [27].

When $\mathbf{g}$, $\mathbf{G}$, or $\mathbf{A}$ is calculated by explicit differentiation, relations (26)-(28) are satisfied automatically. In such cases, we may utilize these relations to compute six of the Cartesian derivatives in terms of the remaining $3N - 6$ derivatives [28]. On the other hand, when the property matrices have been calculated in the Hellmann-Feynman approximation rather than by differentiation, relations (26)-(28) are not satisfied. We may then use the translational and rotational symmetries of equations (26)-(28) to impose the correct translational and rotational symmetries on the molecular properties calculated in this approximation.

Since $\mathbf{T}$ is a $6 \times 3N$ matrix containing six independent rows, we conclude that $\mathbf{TT}^T$ is a nonsingular $6 \times 6$ matrix. We now introduce the pseudo-inverse of $\mathbf{T}$ as the $3N \times 6$ matrix:

$$
\mathbf{T}^{+}=\mathbf{T}^{T}\left(\mathbf{T} \mathbf{T}^{T}\right)^{-1}.
\tag{31}
$$

It is easily verified that, when multiplied by $\mathbf{T}$ from the left, $\mathbf{T}^{+}$works like a usual inverse:
$$
\mathbf{T} \mathbf{T}^{+}=\mathbf{I}_{6}
\tag{32}
$$

However, when multiplied by $\mathbf{T}$ from the right, $\mathbf{T}^{+}$does not give the $3N \times 3N$ unit matrix but instead a projection matrix
$$
\left(\mathbf{T}^{+} \mathbf{T}\right)\left(\mathbf{T}^{+} \mathbf{T}\right)=\mathbf{T}^{+} \mathbf{T}
\tag{33}
$$
with six translational and rotational eigenvalues equal to one and the remaining $3N-6$ eigenvalues equal to zero. Applied to any matrix, the matrix $\mathbf{T}^{+} \mathbf{T}$ projects away the components orthogonal to the translational and rotational degrees of freedom.

Let $\mathbf{g}_{\mathrm{HFA}}, \mathbf{G}_{\mathrm{HFA}}$, and $\mathbf{A}_{\mathrm{HFA}}$ be the molecular gradient, Hessian, and dipole gradient calculated in the Hellmann-Feynman approximation. To arrive at a set of matrices that display the correct translational and rotational symmetries, we first project away the translational and rotational components and then add a term to make sure that the correct symmetries of equations (26)-(28) are satisfied. We obtain
$$
\mathbf{g}=\left(\mathbf{I}_{3 N}-\mathbf{T}^{+} \mathbf{T}\right) \mathbf{g}_{\mathrm{HFA}},
\tag{34}
$$
$$
\mathbf{G}=\left(\mathbf{I}_{3 N}-\mathbf{T}^{+} \mathbf{T}\right) \mathbf{G}_{\mathrm{HFA}}\left(\mathbf{I}_{3 N}-\mathbf{T}^{+} \mathbf{T}\right)^{T},
\tag{35}
$$
$$
\mathbf{A}=\left(\mathbf{I}_{3 N}-\mathbf{T}^{+} \mathbf{T}\right) \mathbf{A}_{\mathrm{HFA}}+\mathbf{T}^{+} \mathbf{N},
\tag{36}
$$
where, in the transformation of the Hessian, we have assumed that the gradient $\mathbf{g}$ vanishes. It is readily verified that these matrices satisfy symmetry conditions (26)-(28).

### 3. Computational details

The results presented in this paper for the molecular properties calculated in the Hellmann-Feynman approximation have all been obtained using the geometry for which the (translationally and rotationally) projected Hellmann-Feynman force vanishes. Although this geometry does not represent the potential energy minimum of the molecules, it is used since the calculated results then correspond to a consistent, independent study in the Hellmann-Feynman approximation.

The basis sets employed in these calculations are listed in, e.g., table 2. Most of these are either the standard correlation-consistent basis sets (cc-pVXZ, aug-pVXZ, cc-pCXZ, and aug-cc-pVXZ) or their fully decontracted counterparts (prim-cc-pVXZ and prim-cc-pCVXZ) [16–19]. In addition, we have used the ANOs of Widmark *et al.* [29] in decontracted form, and the ANO+ basis, obtained from the standard ANO basis by adding tight and diffuse functions as described below. Finally, we have used the R12 basis sets (*vide infra*) and the R12+ basis, obtained from the R12 basis in the same manner as we obtained and ANO+ basis from the ANO basis.

The Hartree-Fock geometry optimizations and the calculations of the different molecular properties, analytically and in the Hellmann-Feynman approximation, were done using a local version of the Dalton program [30]. The geometry optimizations were terminated when the norm of the projected Hellmann-Feynman gradient was smaller than $10^{-5} E_{\mathrm{h}} / a_{0}$ and when in addition either the change in the energy from the previous geometry was less than $10^{-6} E_{\mathrm{h}}$ or the norm of the calculated step was less than $10^{-5} a_{0}$.

The R12 computations were performed with the DIRCCR12 program [31], employing spherical harmonic Gaussian basis sets of the type 7s5p4d for H and 13s8p6d5f for C, N, and O. These sets are typical of basis sets used in CCSD(T)-R12 calculations [32–34] and therefore in this paper are referred to as the R12 basis sets. The approximate computation of many-electron integrals by means of the approximate resolution of the identity requires, for atoms with occupied p-shells, that the one-electron basis set is (nearly) saturated up to the level of f-type atomic functions. Thus, large spdf basis sets are used, but there is no need for g-type and higher angular momentum functions. The 7s5p4d basis set for H has been constructed as follows [35]. The 5s primitive functions of the VTZ basis set of Schäfer and coworkers [36] have been augmented with tight and diffuse s-type functions (table 1). The resulting 7s basis set has then been combined with the 5p4d component of the aug-cc-pV5Z basis set [16–19]. Analogously, the 13s8p6dd5f basis sets for C, N, and O have been obtained by combining the corresponding 11s6p primitive functions of the TZV basis sets of Schäfer and coworkers [37] with the 5d4f component of the aug-cc-pV5Z basis sets, augmented with tight and diffuse functions (table 1). The final basis sets for $\mathrm{N}_{2}$ (or $\mathrm{CO}$) and for $\mathrm{H}_{2} \mathrm{O}$ contain 204 and 186 functions, respectively.

**Table 1. Exponents of augmented functions.**

<table>
<thead>
<tr>
<th></th>
<th>C</th>
<th>N</th>
<th>O</th>
<th>H</th>
</tr>
<tr>
<th colspan="5">Tight functions</th>
</tr>
</thead>
<tbody>
<tr>
<td>s</td>
<td>140 000.0</td>
<td>210 000.0</td>
<td>270 000.0</td>
<td>230.0</td>
</tr>
<tr>
<td>p</td>
<td>200.0</td>
<td>280.0</td>
<td>360.0</td>
<td></td>
</tr>
<tr>
<td>d</td>
<td>8.0</td>
<td>12.0</td>
<td>15.0</td>
<td></td>
</tr>
<tr>
<td>f</td>
<td>4.8</td>
<td>7.2</td>
<td>10.4</td>
<td></td>
</tr>
<tr>
<th colspan="5">Diffuse functions</th>
</tr>
<tr>
<td>s</td>
<td>0.040</td>
<td>0.055</td>
<td>0.074</td>
<td>0.032</td>
</tr>
<tr>
<td>p</td>
<td>0.035</td>
<td>0.050</td>
<td>0.058</td>
<td></td>
</tr>
</tbody>
</table>

Table 2. Geometrical results for the $\mathrm{H}_{2} \mathrm{O}$ molecule. $|\mathbf{g}|$ is the norm of the analytical gradient vector, whereas $\left|\mathbf{g}_{\mathrm{HFA}}\right|$ is the norm of the unprojected (non-invariant) Hellmann-Feynman gradient vector. In each basis, the molecule was optimized using the analytical gradient. The basis sets with the plus signs were constructed by adding additional tight and diffuse s and p functions.

<table>
<thead>
<tr>
<th>Basis</th>
<th>$\frac{E}{E_{\mathrm{h}}}$</th>
<th>$\frac{|\mathbf{g}|}{E_{\mathrm{h}} a_{0}^{-1}}$</th>
<th>$\frac{\left|\mathbf{g}_{\mathrm{HFA}}\right|}{E_{\mathrm{h}} a_{0}^{-1}}$</th>
<th>$\frac{r_{\mathrm{OH}}}{\mathrm{pm}}$</th>
<th>$\frac{\angle_{\mathrm{HOH}}}{\mathrm{deg}}$</th>
<th>$\frac{q_{\mathrm{O}}}{e}$</th>
<th>$\frac{q_{\mathrm{H}}}{e}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>cc-pVDZ</td>
<td>$-76.027054$</td>
<td>$0.00000$</td>
<td>$0.80890$</td>
<td>$94.63$</td>
<td>$104.61$</td>
<td>$-0.562$</td>
<td>$0.281$</td>
</tr>
<tr>
<td>cc-pVTZ</td>
<td>$-76.057770$</td>
<td>$0.00000$</td>
<td>$0.38122$</td>
<td>$94.06$</td>
<td>$106.00$</td>
<td>$-0.569$</td>
<td>$0.284$</td>
</tr>
<tr>
<td>cc-pVQZ</td>
<td>$-76.065519$</td>
<td>$0.00000$</td>
<td>$0.12648$</td>
<td>$93.96$</td>
<td>$106.22$</td>
<td>$-0.575$</td>
<td>$0.287$</td>
</tr>
<tr>
<td>cc-pV5Z</td>
<td>$-76.067783$</td>
<td>$0.00000$</td>
<td>$0.02071$</td>
<td>$93.96$</td>
<td>$106.33$</td>
<td>$-0.579$</td>
<td>$0.289$</td>
</tr>
<tr>
<td>aug-cc-pVDZ</td>
<td>$-76.041844$</td>
<td>$0.00000$</td>
<td>$0.72309$</td>
<td>$94.36$</td>
<td>$105.93$</td>
<td>$-0.573$</td>
<td>$0.287$</td>
</tr>
<tr>
<td>aug-cc-pVTZ</td>
<td>$-76.061203$</td>
<td>$0.00000$</td>
<td>$0.36936$</td>
<td>$94.10$</td>
<td>$106.32$</td>
<td>$-0.576$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>aug-cc-pVQZ</td>
<td>$-76.066676$</td>
<td>$0.00000$</td>
<td>$0.12016$</td>
<td>$93.98$</td>
<td>$106.33$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>aug-cc-pV5Z</td>
<td>$-76.068009$</td>
<td>$0.00000$</td>
<td>$0.01758$</td>
<td>$93.96$</td>
<td>$106.34$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>cc-pCVDZ</td>
<td>$-76.027469$</td>
<td>$0.00000$</td>
<td>$0.37131$</td>
<td>$94.61$</td>
<td>$104.64$</td>
<td>$-0.564$</td>
<td>$0.282$</td>
</tr>
<tr>
<td>cc-pCVTZ</td>
<td>$-76.057966$</td>
<td>$0.00000$</td>
<td>$0.09533$</td>
<td>$94.05$</td>
<td>$106.00$</td>
<td>$-0.569$</td>
<td>$0.285$</td>
</tr>
<tr>
<td>cc-pCVQZ</td>
<td>$-76.065631$</td>
<td>$0.00000$</td>
<td>$0.02656$</td>
<td>$93.96$</td>
<td>$106.22$</td>
<td>$-0.575$</td>
<td>$0.287$</td>
</tr>
<tr>
<td>cc-pCV5Z</td>
<td>$-76.067799$</td>
<td>$0.00000$</td>
<td>$0.00930$</td>
<td>$93.96$</td>
<td>$106.33$</td>
<td>$-0.579$</td>
<td>$0.289$</td>
</tr>
<tr>
<td>aug-cc-pCVDZ</td>
<td>$-76.042150$</td>
<td>$0.00000$</td>
<td>$0.32475$</td>
<td>$94.35$</td>
<td>$105.94$</td>
<td>$-0.573$</td>
<td>$0.287$</td>
</tr>
<tr>
<td>aug-cc-pCVTZ</td>
<td>$-76.061436$</td>
<td>$0.00000$</td>
<td>$0.08827$</td>
<td>$94.09$</td>
<td>$106.30$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>aug-cc-pCVQZ</td>
<td>$-76.066771$</td>
<td>$0.00000$</td>
<td>$0.02510$</td>
<td>$93.98$</td>
<td>$106.33$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>aug-cc-pCV5Z</td>
<td>$-76.068007$</td>
<td>$0.00000$</td>
<td>$0.00827$</td>
<td>$93.96$</td>
<td>$106.34$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>prim-cc-pVDZ</td>
<td>$-76.030937$</td>
<td>$0.00000$</td>
<td>$0.35999$</td>
<td>$94.17$</td>
<td>$105.22$</td>
<td>$-0.561$</td>
<td>$0.280$</td>
</tr>
<tr>
<td>prim-cc-pVTZ</td>
<td>$-76.057878$</td>
<td>$0.00000$</td>
<td>$0.12965$</td>
<td>$94.05$</td>
<td>$106.00$</td>
<td>$-0.569$</td>
<td>$0.285$</td>
</tr>
<tr>
<td>prim-cc-pVQZ</td>
<td>$-76.065564$</td>
<td>$0.00000$</td>
<td>$0.05787$</td>
<td>$93.96$</td>
<td>$106.22$</td>
<td>$-0.575$</td>
<td>$0.287$</td>
</tr>
<tr>
<td>prim-cc-pV5Z</td>
<td>$-76.067795$</td>
<td>$0.00000$</td>
<td>$0.01830$</td>
<td>$93.96$</td>
<td>$106.33$</td>
<td>$-0.579$</td>
<td>$0.289$</td>
</tr>
<tr>
<td>prim-cc-pCVDZ</td>
<td>$-76.031843$</td>
<td>$0.00000$</td>
<td>$0.37717$</td>
<td>$94.18$</td>
<td>$105.19$</td>
<td>$-0.561$</td>
<td>$0.280$</td>
</tr>
<tr>
<td>prim-cc-pCVTZ</td>
<td>$-76.058861$</td>
<td>$0.00000$</td>
<td>$0.06966$</td>
<td>$94.03$</td>
<td>$106.01$</td>
<td>$-0.570$</td>
<td>$0.285$</td>
</tr>
<tr>
<td>prim-cc-pCVQZ</td>
<td>$-76.066160$</td>
<td>$0.00000$</td>
<td>$0.01588$</td>
<td>$93.96$</td>
<td>$106.22$</td>
<td>$-0.575$</td>
<td>$0.287$</td>
</tr>
<tr>
<td>prim-cc-pCV5Z</td>
<td>$-76.067836$</td>
<td>$0.00000$</td>
<td>$0.00657$</td>
<td>$93.96$</td>
<td>$106.33$</td>
<td>$-0.579$</td>
<td>$0.289$</td>
</tr>
<tr>
<td>ANO</td>
<td>$-76.067775$</td>
<td>$0.00000$</td>
<td>$0.02682$</td>
<td>$93.97$</td>
<td>$106.33$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>ANO +</td>
<td>$-76.067847$</td>
<td>$0.00000$</td>
<td>$0.02034$</td>
<td>$93.97$</td>
<td>$106.33$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>R12 basis</td>
<td>$-76.066649$</td>
<td>$0.00000$</td>
<td>$0.00487$</td>
<td>$93.97$</td>
<td>$106.34$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
<tr>
<td>R12 basis +</td>
<td>$-76.066675$</td>
<td>$0.00000$</td>
<td>$0.00351$</td>
<td>$93.97$</td>
<td>$106.34$</td>
<td>$-0.577$</td>
<td>$0.288$</td>
</tr>
</tbody>
</table>

## 4. Results and discussion

### 4.1. Geometry optimizations

In the Hellmann-Feynman approximation, the Hartree-Fock optimization of the geometry proceeds in the normal manner using a standard first-order optimization technique [38] (employing redundant internal coordinates [39] and updated Hessians), and at each point the Hellmann-Feynman gradient is calculated. However, since the Hellmann-Feynman gradient does not represent a true gradient of the energy (except in the limit of an infinite basis), some problems were encountered that are not present in standard minimizations.

First, it is essential to carry out the optimization using the projected rather than the full Hellmann-Feynman force. If the translational and rotational components are not projected out, the optimization does not converge, the molecule being translated and rotated rigidly. Since our optimizations were carried out in internal rather than Cartesian coordinates, the projection was carried out effectively when the forces were transformed to the internal coordinates.

Next, for small basis sets, the usual Hessian update schemes do not work as well as in standard optimizations. As a result, the optimization worked in most cases better when the off-diagonal elements of the updated Hessian were set equal to zero in each iteration. Nevertheless, for the larger basis sets (and in particular for the R12 basis), no such problems were encountered and the optimizations were as efficient as for true gradients. We also note that, in the Hellmann-Feynman optimizations, all tests that involve a comparison of calculated energies at different points can no longer be applied rigorously (since strictly speaking we do not seek an energy minimum but rather a zero Hellmann-Feynman force). As an example, one may find that the calculated energy increases as the projected Hellmann-Feynman force goes to zero. In practice, these problems are solved by applying rather loose criteria for step control and rejection.

### Table 3. Geometrical results for the $\text{H}_2\text{O}$ molecule. In each basis, the molecule was optimized using the Hellmann-Feynman gradient. The basis sets with the plus signs were constructed by adding additional tight and diffuse s and p functions.

<table>
  <thead>
    <tr>
      <th>Basis</th>
      <th>$\frac{E}{E_\text{h}}$</th>
      <th>$\frac{|\mathbf{g}|}{E_\text{h}\,a_0^{-1}}$</th>
      <th>$\frac{|\mathbf{g}_\text{HFA}|}{E_\text{h}\,a_0^{-1}}$</th>
      <th>$\frac{r_\text{OH}}{\text{pm}}$</th>
      <th>$\frac{\angle_\text{HOH}}{\text{deg}}$</th>
      <th>$\frac{q_\text{O}}{e}$</th>
      <th>$\frac{q_\text{H}}{e}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cc-pVDZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>cc-pVTZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>cc-pVQZ</td>
      <td>$-76.053\,287$</td>
      <td>$0.113\,80$</td>
      <td>$0.076\,63$</td>
      <td>$98.49$</td>
      <td>$87.60$</td>
      <td>$-0.332$</td>
      <td>$0.166$</td>
    </tr>
    <tr>
      <td>cc-pV5Z</td>
      <td>$-76.067\,486$</td>
      <td>$0.017\,97$</td>
      <td>$0.011\,04$</td>
      <td>$94.58$</td>
      <td>$103.27$</td>
      <td>$-0.515$</td>
      <td>$0.258$</td>
    </tr>
    <tr>
      <td>aug-cc-pVDZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>aug-cc-pVTZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$-76.055\,929$</td>
      <td>$0.106\,89$</td>
      <td>$0.071\,17$</td>
      <td>$98.17$</td>
      <td>$88.79$</td>
      <td>$-0.360$</td>
      <td>$0.180$</td>
    </tr>
    <tr>
      <td>aug-cc-pV5Z</td>
      <td>$-76.067\,795$</td>
      <td>$0.015\,41$</td>
      <td>$0.009\,15$</td>
      <td>$94.50$</td>
      <td>$103.75$</td>
      <td>$-0.543$</td>
      <td>$0.272$</td>
    </tr>
    <tr>
      <td>cc-pCVDZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>cc-pCVTZ</td>
      <td>$-76.051\,908$</td>
      <td>$0.084\,35$</td>
      <td>$0.051\,96$</td>
      <td>$97.39$</td>
      <td>$93.12$</td>
      <td>$-0.339$</td>
      <td>$0.169$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$-76.065\,186$</td>
      <td>$0.023\,78$</td>
      <td>$0.012\,86$</td>
      <td>$94.85$</td>
      <td>$102.69$</td>
      <td>$-0.498$</td>
      <td>$0.249$</td>
    </tr>
    <tr>
      <td>cc-pCV5Z</td>
      <td>$-76.067\,747$</td>
      <td>$0.008\,35$</td>
      <td>$0.004\,21$</td>
      <td>$94.27$</td>
      <td>$105.15$</td>
      <td>$-0.547$</td>
      <td>$0.273$</td>
    </tr>
    <tr>
      <td>aug-cc-pCVDZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>aug-cc-pCVTZ</td>
      <td>$-76.055\,972$</td>
      <td>$0.080\,04$</td>
      <td>$0.047\,17$</td>
      <td>$97.23$</td>
      <td>$93.99$</td>
      <td>$-0.410$</td>
      <td>$0.205$</td>
    </tr>
    <tr>
      <td>aug-cc-pCVQZ</td>
      <td>$-76.066\,373$</td>
      <td>$0.022\,87$</td>
      <td>$0.011\,55$</td>
      <td>$94.85$</td>
      <td>$103.05$</td>
      <td>$-0.526$</td>
      <td>$0.263$</td>
    </tr>
    <tr>
      <td>aug-cc-pCV5Z</td>
      <td>$-76.067\,966$</td>
      <td>$0.007\,54$</td>
      <td>$0.003\,54$</td>
      <td>$94.25$</td>
      <td>$105.31$</td>
      <td>$-0.560$</td>
      <td>$0.280$</td>
    </tr>
    <tr>
      <td>prim-cc-pVDZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>prim-cc-pVTZ</td>
      <td>$-76.046\,062$</td>
      <td>$0.115\,14$</td>
      <td>$0.074\,05$</td>
      <td>$98.80$</td>
      <td>$88.13$</td>
      <td>$-0.288$</td>
      <td>$0.144$</td>
    </tr>
    <tr>
      <td>prim-cc-pVQZ</td>
      <td>$-76.063\,149$</td>
      <td>$0.051\,41$</td>
      <td>$0.032\,47$</td>
      <td>$95.81$</td>
      <td>$97.69$</td>
      <td>$-0.451$</td>
      <td>$0.225$</td>
    </tr>
    <tr>
      <td>prim-cc-pV52</td>
      <td>$-76.067\,569$</td>
      <td>$0.015\,92$</td>
      <td>$0.009\,50$</td>
      <td>$94.51$</td>
      <td>$103.69$</td>
      <td>$-0.523$</td>
      <td>$0.262$</td>
    </tr>
    <tr>
      <td>prim-cc-pCVDZ</td>
      <td></td>
      <td></td>
      <td colspan="5">No convergence</td>
    </tr>
    <tr>
      <td>prim-cc-pCVTZ</td>
      <td>$-76.055\,810$</td>
      <td>$0.061\,85$</td>
      <td>$0.035\,73$</td>
      <td>$96.46$</td>
      <td>$96.97$</td>
      <td>$-0.380$</td>
      <td>$0.190$</td>
    </tr>
    <tr>
      <td>prim-cc-pCVQZ</td>
      <td>$-76.066\,023$</td>
      <td>$0.014\,72$</td>
      <td>$0.006\,23$</td>
      <td>$94.56$</td>
      <td>$104.51$</td>
      <td>$-0.521$</td>
      <td>$0.261$</td>
    </tr>
    <tr>
      <td>prim-cc-pCV5Z</td>
      <td>$-76.067\,813$</td>
      <td>$0.006\,52$</td>
      <td>$0.002\,47$</td>
      <td>$94.20$</td>
      <td>$105.64$</td>
      <td>$-0.553$</td>
      <td>$0.276$</td>
    </tr>
    <tr>
      <td>ANO</td>
      <td>$-76.067\,314$</td>
      <td>$0.024\,22$</td>
      <td>$0.012\,79$</td>
      <td>$94.88$</td>
      <td>$102.75$</td>
      <td>$-0.530$</td>
      <td>$0.265$</td>
    </tr>
    <tr>
      <td>ANO +</td>
      <td>$-76.067\,598$</td>
      <td>$0.018\,58$</td>
      <td>$0.008\,94$</td>
      <td>$94.69$</td>
      <td>$103.80$</td>
      <td>$-0.544$</td>
      <td>$0.272$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$-76.066\,638$</td>
      <td>$0.004\,83$</td>
      <td>$0.000\,59$</td>
      <td>$94.19$</td>
      <td>$106.13$</td>
      <td>$-0.570$</td>
      <td>$0.285$</td>
    </tr>
    <tr>
      <td>R12 basis +</td>
      <td>$-76.066\,668$</td>
      <td>$0.003\,43$</td>
      <td>$0.000\,72$</td>
      <td>$94.14$</td>
      <td>$106.51$</td>
      <td>$-0.575$</td>
      <td>$0.288$</td>
    </tr>
  </tbody>
</table>

### 4.2. Hartree-Fock calculations

For a careful study of the basis set convergence, the water molecule was chosen. For each basis set, two independent sets of optimizations and property calculations were carried out: one in the standard approach (using the true Cartesian derivatives), the other in the Hell-mann-Feynman approximation. At each optimized geometry, the molecular Hessian and the dipole gradient were calculated. From these matrices, the harmonic frequencies, double-harmonic infrared intensities, and the Cioslowski atomic charges [40] were calculated in the usual manner. In addition, for the geometry optimized using the true gradient, the Hellmann-Feynman gradient was computed for comparison; equivalently, for the Hellmann-Feynman geometry the true gradient was determined.

The results for the water molecule are contained in tables 2-5. As seen from tables 3 and 5, no results are available for some of the smaller basis sets in the Hellmann-Feynman approximation. The reason for their absence is that the optimization failed to converge for these basis sets. As the bond angle decreased in the course of the optimization, the bond distance increased, leading to a fragmentation of the molecule. Clearly, for these small basis sets, the Hellmann-Feynman approximation breaks down completely. This breakdown occurs for all the double-zeta basis sets and also for the cc-pVTZ and aug-cc-pVTZ sets.

In figure 1 we have plotted the norm of the full (unprojected) Hellmann-Feynman gradient at the true energy minimum of each basis set (see also table 2). For each sequence of correlation-consistent basis sets, the norm of the Hellmann-Feynman gradient is large at the double-zeta level but decreases rapidly as the cardinal number increases from $X=2$ to $X=5$. Thus, in the simple cc-pVXZ sequence, the norm decreases from $0.81\ E_\text{h}\,a_0^{-1}$ for the cc-pVDZ basis to $0.02\ E_\text{h}\,a_0^{-1}$ for the cc-pV5Z basis. Only a minor improvement is observed at the aug-cc-pVXZ level. In the cc-pCVXZ sequence, the norm decreases from $0.37\ E_\text{h}\,a_0^{-1}$ at the cc-pCVDZ level to $0.009\ E_\text{h}\,a_0^{-1}$ at the cc-pCV5Z level. Clearly, what is needed for

Table 4. Harmonic vibrational frequencies and intensities for the $H_2O$ molecule. In each basis, the molecule was optimized using the analytical gradient. The basis sets with the plus signs were constructed by adding additional tight and diffuse s and p functions.

<table>
<thead>
<tr>
<th>Basis</th>
<th>$\omega_1$<br>cm$^{-1}$</th>
<th>$\omega_2$<br>cm$^{-1}$</th>
<th>$\omega_3$<br>cm$^{-1}$</th>
<th>$I_1$<br>km mol$^{-1}$</th>
<th>$I_2$<br>km mol$^{-1}$</th>
<th>$I_3$<br>km mol$^{-1}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>cc-pVDZ</td>
<td>4212.09</td>
<td>4113.77</td>
<td>1775.82</td>
<td>60.478</td>
<td>21.177</td>
<td>80.697</td>
</tr>
<tr>
<td>cc-pVTZ</td>
<td>4226.96</td>
<td>4127.05</td>
<td>1753.01</td>
<td>75.246</td>
<td>14.567</td>
<td>90.304</td>
</tr>
<tr>
<td>cc-pVQZ</td>
<td>4229.47</td>
<td>4130.15</td>
<td>1750.58</td>
<td>85.547</td>
<td>15.058</td>
<td>93.684</td>
</tr>
<tr>
<td>cc-pV5Z</td>
<td>4230.96</td>
<td>4130.55</td>
<td>1748.31</td>
<td>90.751</td>
<td>15.711</td>
<td>95.144</td>
</tr>
<tr>
<td>aug-cc-pVDZ</td>
<td>4237.63</td>
<td>4130.24</td>
<td>1744.30</td>
<td>87.884</td>
<td>14.395</td>
<td>93.154</td>
</tr>
<tr>
<td>aug-cc-pVTZ</td>
<td>4222.46</td>
<td>4120.16</td>
<td>1745.18</td>
<td>92.290</td>
<td>15.103</td>
<td>96.383</td>
</tr>
<tr>
<td>aug-cc-pVQZ</td>
<td>4228.82</td>
<td>4128.33</td>
<td>1747.65</td>
<td>92.817</td>
<td>15.152</td>
<td>96.432</td>
</tr>
<tr>
<td>aug-cc-pV5Z</td>
<td>4230.60</td>
<td>4129.92</td>
<td>1748.05</td>
<td>92.738</td>
<td>15.120</td>
<td>96.531</td>
</tr>
<tr>
<td>cc-pCVDZ</td>
<td>4212.90</td>
<td>4113.67</td>
<td>1775.41</td>
<td>61.234</td>
<td>21.310</td>
<td>81.088</td>
</tr>
<tr>
<td>cc-pCVTZ</td>
<td>4219.00</td>
<td>4122.69</td>
<td>1753.05</td>
<td>76.068</td>
<td>14.798</td>
<td>90.268</td>
</tr>
<tr>
<td>cc-pCVQZ</td>
<td>4230.31</td>
<td>4130.92</td>
<td>1750.66</td>
<td>85.490</td>
<td>15.038</td>
<td>93.685</td>
</tr>
<tr>
<td>cc-pCV5Z</td>
<td>4231.03</td>
<td>4130.64</td>
<td>1748.39</td>
<td>90.783</td>
<td>15.726</td>
<td>95.137</td>
</tr>
<tr>
<td>aug-cc-pCVDZ</td>
<td>4237.93</td>
<td>4130.00</td>
<td>1744.47</td>
<td>88.069</td>
<td>14.359</td>
<td>93.298</td>
</tr>
<tr>
<td>aug-cc-pCVTZ</td>
<td>4216.12</td>
<td>4117.69</td>
<td>1745.40</td>
<td>92.791</td>
<td>15.259</td>
<td>96.354</td>
</tr>
<tr>
<td>aug-cc-pCVQZ</td>
<td>4229.42</td>
<td>4128.90</td>
<td>1747.72</td>
<td>92.811</td>
<td>15.154</td>
<td>96.429</td>
</tr>
<tr>
<td>aug-cc-pCV5Z</td>
<td>4230.65</td>
<td>4129.99</td>
<td>1748.07</td>
<td>92.736</td>
<td>15.125</td>
<td>96.522</td>
</tr>
<tr>
<td>prim-cc-pVDZ</td>
<td>4220.77</td>
<td>4124.03</td>
<td>1766.25</td>
<td>49.762</td>
<td>15.415</td>
<td>83.257</td>
</tr>
<tr>
<td>prim-cc-pVTZ</td>
<td>4219.87</td>
<td>4123.41</td>
<td>1752.77</td>
<td>76.129</td>
<td>14.852</td>
<td>90.131</td>
</tr>
<tr>
<td>prim-cc-pVQZ</td>
<td>4229.99</td>
<td>4130.59</td>
<td>1750.54</td>
<td>85.417</td>
<td>15.011</td>
<td>93.693</td>
</tr>
<tr>
<td>prim-cc-pV5Z</td>
<td>4230.98</td>
<td>4130.58</td>
<td>1748.36</td>
<td>90.800</td>
<td>15.726</td>
<td>95.109</td>
</tr>
<tr>
<td>prim-cc-pCVDZ</td>
<td>4219.89</td>
<td>4123.19</td>
<td>1765.85</td>
<td>50.005</td>
<td>15.585</td>
<td>82.781</td>
</tr>
<tr>
<td>prim-cc-pCVTZ</td>
<td>4221.66</td>
<td>4125.10</td>
<td>1753.51</td>
<td>76.722</td>
<td>15.118</td>
<td>90.218</td>
</tr>
<tr>
<td>prim-cc-pCVQZ</td>
<td>4230.48</td>
<td>4131.07</td>
<td>1750.55</td>
<td>85.463</td>
<td>15.028</td>
<td>93.771</td>
</tr>
<tr>
<td>prim-cc-pCV5Z</td>
<td>4231.08</td>
<td>4130.71</td>
<td>1748.40</td>
<td>90.822</td>
<td>15.739</td>
<td>95.103</td>
</tr>
<tr>
<td>ANO</td>
<td>4230.78</td>
<td>4130.32</td>
<td>1747.67</td>
<td>92.767</td>
<td>15.151</td>
<td>96.325</td>
</tr>
<tr>
<td>ANO +</td>
<td>4230.91</td>
<td>4130.45</td>
<td>1747.72</td>
<td>92.739</td>
<td>15.144</td>
<td>96.314</td>
</tr>
<tr>
<td>R12 basis</td>
<td>4231.45</td>
<td>4130.94</td>
<td>1747.81</td>
<td>92.949</td>
<td>15.176</td>
<td>96.569</td>
</tr>
<tr>
<td>R12 basis +</td>
<td>4231.46</td>
<td>4130.95</td>
<td>1747.84</td>
<td>92.936</td>
<td>15.177</td>
<td>96.564</td>
</tr>
</tbody>
</table>

improved convergence is the addition of tight rather than diffuse functions. Decontraction gives some further improvement. In general, basis sets of quin-tuple-zeta quality or at least quadruple-zeta quality are needed for reasonable agreement with the true gradient. The ANO basis sets appear to perform worse than the corresponding correlation-consistent basis sets. The best performance is obtained with the R12 basis sets, which give Hellmann-Feynman norms less than $0.005 E_{\mathrm{h}} a_{0}^{-1}$. In contrast to the other basis sets, the R12 sets have been developed to satisfy certain com-pleteness relations required in the explicitly correlated R12 method. Apparently, the special functions needed for the R12 calculations improve also the description of molecular properties in the Hellmann-Feynman approximation.

Our numbers for the norm of the Hellmann-Feynman gradient may be compared with the differences found by Nakatsuji et al. between the analytical and Hellmann-Feynman gradients at the experimental minima [12]. In their family basis sets, the differences are about $0.05 E_{\mathrm{h}} a_{0}^{-1}$, and thus fall between the results obtained with the standard cc-pCVTZ or cc-pCVQZ basis sets. Using the R12 basis, the errors are an order of magni-tude smaller.

Having discussed the norm of the Hellmann-Feynman gradient at the true minima, we now proceed to consider the geometries optimized using the Hellman-Feynman gradients and the properties calculated in the Hellmann-Feynman approximation at these geometries. In figures 2 and 3 we have plotted the relative errors of the Hellmann-Feynman properties relative to the properties calculated in the standard manner, using the R12 basis and various correlation-consistent quintuple-zeta basis sets. The 'geometrical' properties (i.e., the bond distance, the bond angle, and the harmonic frequencies) behave in much the same manner as the norm of the Hellmann-Feynman

Table 5. Harmonic vibrational frequencies and intensities for the $\mathrm{H}_{2} \mathrm{O}$ molecule. In each basis, the molecule was optimized using the Hellmann-Feynman gradient. The basis sets with the plus signs were constructed by adding additional tight and diffuse s and p functions.

<table>
  <thead>
    <tr>
      <th>Basis</th>
      <th>$\frac{\omega_{1}}{\mathrm{~cm}^{-1}}$</th>
      <th>$\frac{\omega_{2}}{\mathrm{~cm}^{-1}}$</th>
      <th>$\frac{\omega_{3}}{\mathrm{~cm}^{-1}}$</th>
      <th>$\frac{I_{1}}{\mathrm{~km} \mathrm{~mol}^{-1}}$</th>
      <th>$\frac{I_{2}}{\mathrm{~km} \mathrm{~mol}^{-1}}$</th>
      <th>$\frac{I_{3}}{\mathrm{~km} \mathrm{~mol}^{-1}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cc-pVDZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>cc-pVTZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>cc-pVQZ</td>
      <td>3474.26</td>
      <td>3437.64</td>
      <td>1655.89</td>
      <td>1.051</td>
      <td>5.222</td>
      <td>8.273</td>
    </tr>
    <tr>
      <td>cc-pV5Z</td>
      <td>4172.38</td>
      <td>4072.73</td>
      <td>1721.62</td>
      <td>50.341</td>
      <td>6.442</td>
      <td>60.511</td>
    </tr>
    <tr>
      <td>aug-cc-pVDZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>aug-cc-pVTZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>3492.49</td>
      <td>3456.79</td>
      <td>1618.18</td>
      <td>0.083</td>
      <td>0.289</td>
      <td>12.634</td>
    </tr>
    <tr>
      <td>aug-cc-pV5Z</td>
      <td>4189.75</td>
      <td>4091.90</td>
      <td>1696.81</td>
      <td>67.841</td>
      <td>10.886</td>
      <td>77.763</td>
    </tr>
    <tr>
      <td>cc-pCVDZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>cc-pCVTZ</td>
      <td>3852.60</td>
      <td>3816.60</td>
      <td>1720.58</td>
      <td>2.900</td>
      <td>1.167</td>
      <td>10.541</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>4079.37</td>
      <td>3996.61</td>
      <td>1750.24</td>
      <td>37.128</td>
      <td>4.871</td>
      <td>55.450</td>
    </tr>
    <tr>
      <td>cc-pCV5Z</td>
      <td>4183.56</td>
      <td>4087.20</td>
      <td>1740.62</td>
      <td>69.051</td>
      <td>10.256</td>
      <td>77.309</td>
    </tr>
    <tr>
      <td>aug-cc-pCVDZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>aug-cc-pCVTZ</td>
      <td>3901.38</td>
      <td>3856.95</td>
      <td>1758.73</td>
      <td>5.177</td>
      <td>0.658</td>
      <td>23.860</td>
    </tr>
    <tr>
      <td>aug-cc-pCVQZ</td>
      <td>4085.97</td>
      <td>4001.63</td>
      <td>1746.38</td>
      <td>56.697</td>
      <td>8.844</td>
      <td>68.732</td>
    </tr>
    <tr>
      <td>aug-cc-pCV5Z</td>
      <td>4188.13</td>
      <td>4091.66</td>
      <td>1738.81</td>
      <td>80.269</td>
      <td>13.020</td>
      <td>86.858</td>
    </tr>
    <tr>
      <td>prim-cc-pVDZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>prim-cc-pVTZ</td>
      <td>3715.88</td>
      <td>3710.87</td>
      <td>1717.77</td>
      <td>4.153</td>
      <td>24.691</td>
      <td>5.007</td>
    </tr>
    <tr>
      <td>prim-cc-pVQZ</td>
      <td>3898.83</td>
      <td>3852.34</td>
      <td>1719.56</td>
      <td>14.389</td>
      <td>2.175</td>
      <td>37.829</td>
    </tr>
    <tr>
      <td>prim-cc-pV5Z</td>
      <td>4195.76</td>
      <td>4105.02</td>
      <td>1759.71</td>
      <td>53.841</td>
      <td>7.666</td>
      <td>65.059</td>
    </tr>
    <tr>
      <td>prim-cc-pCVDZ</td>
      <td colspan="7">No convergence</td>
    </tr>
    <tr>
      <td>prim-cc-pCVTZ</td>
      <td>3977.83</td>
      <td>3918.21</td>
      <td>1728.57</td>
      <td>0.218</td>
      <td>0.102</td>
      <td>18.990</td>
    </tr>
    <tr>
      <td>prim-cc-pCVQZ</td>
      <td>4128.69</td>
      <td>4037.97</td>
      <td>1742.58</td>
      <td>51.134</td>
      <td>6.711</td>
      <td>66.210</td>
    </tr>
    <tr>
      <td>prim-cc-pCV5Z</td>
      <td>4199.88</td>
      <td>4101.63</td>
      <td>1746.42</td>
      <td>73.754</td>
      <td>10.891</td>
      <td>80.801</td>
    </tr>
    <tr>
      <td>ANO</td>
      <td>4104.32</td>
      <td>4023.61</td>
      <td>1725.99</td>
      <td>58.298</td>
      <td>9.845</td>
      <td>70.817</td>
    </tr>
    <tr>
      <td>ANO +</td>
      <td>4134.04</td>
      <td>4047.02</td>
      <td>1726.85</td>
      <td>67.756</td>
      <td>11.438</td>
      <td>78.168</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>4209.19</td>
      <td>4108.37</td>
      <td>1737.26</td>
      <td>87.737</td>
      <td>14.027</td>
      <td>92.433</td>
    </tr>
    <tr>
      <td>R12 basis +</td>
      <td>4218.96</td>
      <td>4116.54</td>
      <td>1736.00</td>
      <td>92.059</td>
      <td>14.693</td>
      <td>95.722</td>
    </tr>
  </tbody>
</table>

![](./images/811835190153314305_2.jpg)

Figure 1. Norm of the unprojected Hellmann-Feynman gradient (atomic units). For each basis set the geometry has been optimized using the analytical gradient.

![](./images/811835190153314305_3.jpg)

Figure 2. Absolute value of the relative error in the Hellmann-Feynman results compared with the analytical result. Geometrical parameters and frequencies for the quintuple basis sets and the R12 basis are shown.

![](./images/811835190153314305_4.jpg)

Figure 3. Absolute value of the relative error in the Hellmann-Feynman results compared with the analytical result. Charges and intensities for the quintuple basis sets and the R12 basis are shown. Note that the scale is much larger than in figure 2.

gradient discussed above. Of the correlation-consistent basis sets, the prim-cc-pCV5Z basis performs best, but the best overall performance is again that of the R12 basis.

The performance of the Hellmann-Feynman approximation for the molecular properties involving the dipole gradient (the charges and in particular the infrared intensities) is rather different, see figure 3. Noting the difference in scale from figure 2, we find that the infrared intensities calculated in the Hell-mann-Feynman approximation differ from the analytical ones by as much as 60% at the cc-pV5Z level.

![](./images/811835190153314305_5.jpg)

Figure 4. Bond length of the $\text{H}_2\text{O}$ molecule (in pm) optimized using analytical and Hellmann-Feynman gradients.

![](./images/811835190153314305_6.jpg)

Figure 5. Bond angle of the $\text{H}_2\text{O}$ molecule (in deg) optimized using analytical and Hellmann-Feynman gradients. The two analytical curves are almost indistinguishable. Some of the smaller basis sets failed to converge when the Hellmann- Feynman gradient was used.

For the R12 basis, however, the difference is only about 5%, a considerable improvement on the cc-pV5Z basis. For these properties, diffuse functions are essential, as we may see from the improvements in the performance of the correlation-consistent basis sets when diffuse functions are added at the aug-cc-pV5Z and aug-cc- pCV5Z levels. Nevertheless, the aug-cc-pCV5Z basis still performs poorer than the R12 basis.

The basis set convergence of the different molecular properties is illustrated in figures 4–7. In these figures we have plotted the molecular properties (the OH bond distance, the HOH bond angle, the highest harmonic

![](./images/811835190153314305_7.jpg)

Figure 6. Highest frequency of the $\text{H}_2\text{O}$ molecule (in $\text{cm}^{-1}$) optimized using analytical and Hellmann-Feynman gradients.

![](./images/811835190153314305_8.jpg)

Figure 7. Intensity (in $\text{km mol}^{-1}$) corresponding to the highest frequency of the $\text{H}_2\text{O}$ molecule. In each basis, the molecule was optimized using analytical and Hellmann-Feynman gradients.

frequency, and the corresponding intensity) as functions
of the cardinal number, calculated both as derivatives
and in the Hellmann-Feynman approximation. For
comparison, we have added the Hartree-Fock basis set
limit (as calculated analytically at the aug-cc-pCV5Z
level) as a straight line, and the Hellmann-Feynman
result obtained in the R12 basis as a cross. The much
slower convergence of the Hellmann-Feynman

Molecular geometry in the Hellmann-Feynman approximation

Table 6. Geometrical and vibrational results for the CO molecule. In each basis, the molecule was optimized using the analytical gradient (top half) and the Hellmann-Feynman gradient (bottom half).

<table>
  <thead>
    <tr>
      <th>Basis</th>
      <th>$\frac{E}{E_\text{h}}$</th>
      <th>$\frac{|\mathbf{g}|}{E_\text{h}\,a_0^{-1}}$</th>
      <th>$\frac{\mathbf{g}_\text{HFA}}{E_\text{h}\,a_0^{-1}}$</th>
      <th>$\frac{r_\text{CO}}{\text{pm}}$</th>
      <th>$\frac{q_\text{C}}{e}$</th>
      <th>$\frac{q_\text{O}}{e}$</th>
      <th>$\frac{\omega_1}{\text{cm}^{-1}}$</th>
      <th>$\frac{I_1}{\text{km mol}^{-1}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cc-pVQZ</td>
      <td>$-112.790\,626$</td>
      <td>$0.000\,00$</td>
      <td>$0.107\,51$</td>
      <td>$110.20$</td>
      <td>$0.351$</td>
      <td>$-0.351$</td>
      <td>$2427.31$</td>
      <td>$142.315$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$-112.790\,812$</td>
      <td>$0.000\,00$</td>
      <td>$0.105\,65$</td>
      <td>$110.20$</td>
      <td>$0.353$</td>
      <td>$-0.353$</td>
      <td>$2426.10$</td>
      <td>$144.636$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$-112.790\,888$</td>
      <td>$0.000\,00$</td>
      <td>$0.021\,92$</td>
      <td>$110.19$</td>
      <td>$0.351$</td>
      <td>$-0.351$</td>
      <td>$2427.53$</td>
      <td>$142.330$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$-112.790\,682$</td>
      <td>$0.000\,00$</td>
      <td>$0.005\,97$</td>
      <td>$110.18$</td>
      <td>$0.353$</td>
      <td>$-0.353$</td>
      <td>$2427.02$</td>
      <td>$144.510$</td>
    </tr>
    <tr>
      <td>cc-pVQZ</td>
      <td>$-112.788\,632$</td>
      <td>$0.103\,73$</td>
      <td>$0.040\,17$</td>
      <td>$112.99$</td>
      <td>$0.349$</td>
      <td>$-0.349$</td>
      <td>$2146.58$</td>
      <td>$127.181$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$-112.788\,891$</td>
      <td>$0.101\,88$</td>
      <td>$0.040\,15$</td>
      <td>$112.94$</td>
      <td>$0.350$</td>
      <td>$-0.350$</td>
      <td>$2085.25$</td>
      <td>$128.059$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$-112.790\,815$</td>
      <td>$0.020\,88$</td>
      <td>$0.007\,70$</td>
      <td>$110.71$</td>
      <td>$0.347$</td>
      <td>$-0.347$</td>
      <td>$2356.07$</td>
      <td>$136.315$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$-112.790\,677$</td>
      <td>$0.005\,88$</td>
      <td>$0.001\,05$</td>
      <td>$110.32$</td>
      <td>$0.353$</td>
      <td>$-0.353$</td>
      <td>$2419.25$</td>
      <td>$143.692$</td>
    </tr>
  </tbody>
</table>

Table 7. Geometrical and vibrational results for the $\text{N}_2$ molecule. In each basis, the molecule was optimized using the analytical gradient (top half) and the Hellmann-Feynman gradient (bottom half).

<table>
  <thead>
    <tr>
      <th>Basis</th>
      <th>$\frac{E}{E_\text{h}}$</th>
      <th>$\frac{|\mathbf{g}|}{E_\text{h}\,a_0^{-1}}$</th>
      <th>$\frac{|\mathbf{g}_\text{HFA}|}{E_\text{h}\,a_0^{-1}}$</th>
      <th>$\frac{r_\text{NN}}{\text{pm}}$</th>
      <th>$\frac{q_\text{N}}{e}$</th>
      <th>$\frac{\omega_1}{\text{cm}^{-1}}$</th>
      <th>$\frac{I_1}{\text{km mol}^{-1}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cc-pVQZ</td>
      <td>$-108.994\,470$</td>
      <td>$0.000\,00$</td>
      <td>$0.081\,30$</td>
      <td>$106.56$</td>
      <td>$0.000$</td>
      <td>$2729.74$</td>
      <td>$0.000$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$-108.994\,933$</td>
      <td>$0.000\,00$</td>
      <td>$0.082\,03$</td>
      <td>$106.56$</td>
      <td>$0.000$</td>
      <td>$2728.95$</td>
      <td>$0.000$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$-108.994\,710$</td>
      <td>$0.000\,00$</td>
      <td>$0.018\,49$</td>
      <td>$106.55$</td>
      <td>$0.000$</td>
      <td>$2730.07$</td>
      <td>$0.000$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$-108.994\,720$</td>
      <td>$0.000\,00$</td>
      <td>$0.004\,15$</td>
      <td>$106.55$</td>
      <td>$0.000$</td>
      <td>$2730.60$</td>
      <td>$0.000$</td>
    </tr>
    <tr>
      <td>cc-pVQZ</td>
      <td>$-108.993\,498$</td>
      <td>$0.084\,39$</td>
      <td>$0.000\,00$</td>
      <td>$108.25$</td>
      <td>$0.000$</td>
      <td>$2640.03$</td>
      <td>$0.000$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$-108.993\,940$</td>
      <td>$0.085\,22$</td>
      <td>$0.000\,00$</td>
      <td>$108.27$</td>
      <td>$0.000$</td>
      <td>$2584.87$</td>
      <td>$0.000$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$-108.994\,665$</td>
      <td>$0.018\,71$</td>
      <td>$0.000\,00$</td>
      <td>$106.91$</td>
      <td>$0.000$</td>
      <td>$2668.55$</td>
      <td>$0.000$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$-108.994\,718$</td>
      <td>$0.004\,15$</td>
      <td>$0.000\,00$</td>
      <td>$106.63$</td>
      <td>$0.000$</td>
      <td>$2726.30$</td>
      <td>$0.000$</td>
    </tr>
  </tbody>
</table>

approximation is illustrated well. The only property for which the standard approach converges slowly is the infrared intensity.

### 4.3. Hartree-Fock calculations on $CO$, $N_2$, and $NH_3$
To confirm that the results obtained for the water molecule are representative, calculations were performed on a few other small molecules (CO, $\text{N}_2$, and $\text{NH}_3$) as well. As for water, the geometries were optimized using both the true gradient and the Hellmann-Feynman gradient, and the various properties were calculated for the converged structures. Only a subset of the basis sets used for water were employed: the R12 basis and the three correlation-consistent quadruple-zeta sets cc-pVQZ, aug-cc-pVQZ, and cc-pCVQZ.

#### 4.3.1. $CO$
All results for the CO molecule can be found in table 6. Compared with the $\text{H}_2\text{O}$ molecule, the properties of CO calculated in the Hellmann-Feynman approximation come closer to the analytical results, probably because of the rigid structure of the molecule. Of the correlation-consistent sets, the cc-pCVQZ set gives the better results, just a few per cent off the analytical result. However, it cannot compete with the slightly larger R12 basis, where all properties are within $1\%$ of the analytical values. Clearly the performance of the two other sets is inferior and, in this molecule, it is not clear that augmentation improves the charges and intensities, probably because of the poor geometry obtained with the aug-cc-pVQZ basis. However, it is noteworthy that all sets produce reasonable atomic charges. This may be related to the way the dipole gradient has been made translationally and rotationally invariant (using information about the dipole moment).

#### 4.3.2. $N_2$
Owing to its high symmetry, the $\text{N}_2$ molecule provides less information than do the other molecules. The two nitrogen atoms are equivalent and there is zero atomic charge. Furthermore, the infrared intensity of the single vibrational frequency is zero since the molecule possesses a centre of inversion. As can be seen from table 7, the R12 basis still outperforms the other basis sets, producing results with a relative error less than $0.2\%$.

Table 8. Geometrical results for the $NH_3$ molecule. In each basis, the molecule was optimized using the analytical gradient (top half) and the Hellmann-Feynman gradient (bottom half).

<table>
  <thead>
    <tr>
      <th>Basis</th>
      <th>$\frac{E}{E_{\mathrm{h}}}$</th>
      <th>$\frac{|\mathbf{g}|}{E_{\mathrm{h}} a_{0}^{-1}}$</th>
      <th>$\frac{\mathbf{g}_{\mathrm{HFA}}}{E_{\mathrm{h}} a_{0}^{-1}}$</th>
      <th>$\frac{r_{\mathrm{NH}}}{\mathrm{pm}}$</th>
      <th>$\frac{\angle_{\mathrm{HNH}}}{\mathrm{deg}}$</th>
      <th>$\frac{q_{\mathrm{N}}}{e}$</th>
      <th>$\frac{q_{\mathrm{N}}}{e}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cc-pVQZ</td>
      <td>$-56.223\;596$</td>
      <td>$0.000\;00$</td>
      <td>$0.070\;33$</td>
      <td>$99.80$</td>
      <td>$107.91$</td>
      <td>$-0.470$</td>
      <td>$0.157$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$-56.224\;504$</td>
      <td>$0.000\;00$</td>
      <td>$0.065\;15$</td>
      <td>$99.79$</td>
      <td>$108.15$</td>
      <td>$-0.469$</td>
      <td>$0.156$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$-56.223\;693$</td>
      <td>$0.000\;00$</td>
      <td>$0.014\;94$</td>
      <td>$99.80$</td>
      <td>$107.91$</td>
      <td>$-0.470$</td>
      <td>$0.157$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$-56.224\;369$</td>
      <td>$0.000\;00$</td>
      <td>$0.003\;73$</td>
      <td>$99.79$</td>
      <td>$108.16$</td>
      <td>$-0.469$</td>
      <td>$0.156$</td>
    </tr>
    <tr>
      <td>cc-pVQZ</td>
      <td>$-56.214\;485$</td>
      <td>$0.077\;82$</td>
      <td>$0.041\;36$</td>
      <td>$102.74$</td>
      <td>$96.05$</td>
      <td>$-0.092$</td>
      <td>$0.031$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$-56.216\;768$</td>
      <td>$0.070\;22$</td>
      <td>$0.037\;26$</td>
      <td>$102.48$</td>
      <td>$97.12$</td>
      <td>$-0.137$</td>
      <td>$0.046$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$-56.223\;373$</td>
      <td>$0.014\;87$</td>
      <td>$0.005\;65$</td>
      <td>$100.51$</td>
      <td>$105.80$</td>
      <td>$-0.341$</td>
      <td>$0.114$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$-56.224\;359$</td>
      <td>$0.003\;72$</td>
      <td>$0.000\;01$</td>
      <td>$99.99$</td>
      <td>$108.11$</td>
      <td>$-0.460$</td>
      <td>$0.153$</td>
    </tr>
  </tbody>
</table>

Table 9. Harmonic vibrational frequencies and intensities for the $NH_3$ molecule. In each basis, the molecule was optimized using the analytical gradient (top half) and the Hellmann-Feynman gradient (bottom half).

<table>
  <thead>
    <tr>
      <th>Basis</th>
      <th>$\frac{\omega_1, \omega_2}{\mathrm{cm}^{-1}}$</th>
      <th>$\frac{\omega_3}{\mathrm{cm}^{-1}}$</th>
      <th>$\frac{\omega_4, \omega_5}{\mathrm{cm}^{-1}}$</th>
      <th>$\frac{\omega_6}{\mathrm{cm}^{-1}}$</th>
      <th>$\frac{I_1, I_2}{\mathrm{km\ mol}^{-1}}$</th>
      <th>$\frac{I_3}{\mathrm{km\ mol}^{-1}}$</th>
      <th>$\frac{I_4, I_5}{\mathrm{km\ mol}^{-1}}$</th>
      <th>$\frac{I_6}{\mathrm{km\ mol}^{-1}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cc-pVQZ</td>
      <td>$3811.19$</td>
      <td>$3688.58$</td>
      <td>$1789.96$</td>
      <td>$1112.42$</td>
      <td>$4.683$</td>
      <td>$0.776$</td>
      <td>$19.684$</td>
      <td>$189.159$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$3814.89$</td>
      <td>$3689.84$</td>
      <td>$1786.57$</td>
      <td>$1094.98$</td>
      <td>$6.576$</td>
      <td>$1.168$</td>
      <td>$18.848$</td>
      <td>$179.932$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$3811.84$</td>
      <td>$3689.05$</td>
      <td>$1789.85$</td>
      <td>$1112.43$</td>
      <td>$4.669$</td>
      <td>$0.771$</td>
      <td>$19.663$</td>
      <td>$188.862$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$3816.78$</td>
      <td>$3692.07$</td>
      <td>$1786.97$</td>
      <td>$1093.84$</td>
      <td>$6.613$</td>
      <td>$1.151$</td>
      <td>$18.911$</td>
      <td>$180.269$</td>
    </tr>
    <tr>
      <td>cc-pVQZ</td>
      <td>$3280.68$</td>
      <td>$3267.01$</td>
      <td>$1669.44$</td>
      <td>$1315.83$</td>
      <td>$28.996$</td>
      <td>$29.440$</td>
      <td>$0.029$</td>
      <td>$7.240$</td>
    </tr>
    <tr>
      <td>aug-cc-pVQZ</td>
      <td>$3296.03$</td>
      <td>$3279.07$</td>
      <td>$1637.41$</td>
      <td>$1267.65$</td>
      <td>$19.086$</td>
      <td>$19.350$</td>
      <td>$0.328$</td>
      <td>$14.566$</td>
    </tr>
    <tr>
      <td>cc-pCVQZ</td>
      <td>$3698.50$</td>
      <td>$3591.80$</td>
      <td>$1765.62$</td>
      <td>$1140.74$</td>
      <td>$0.001$</td>
      <td>$4.686$</td>
      <td>$9.998$</td>
      <td>$100.421$</td>
    </tr>
    <tr>
      <td>R12 basis</td>
      <td>$3795.73$</td>
      <td>$3671.65$</td>
      <td>$1778.12$</td>
      <td>$1086.42$</td>
      <td>$5.883$</td>
      <td>$1.341$</td>
      <td>$18.100$</td>
      <td>$174.581$</td>
    </tr>
  </tbody>
</table>

### 4.3.3. $NH_3$

The last molecule to be examined is ammonia. Tables 8 and 9 show that this compound seems to pose a greater challenge within the Hellmann-Feynman approximations than the other molecules, at least for the smaller basis sets. The optimized geometries show that the structures obtained with these basis sets behave much like that found for water: the bond angles are too small and the bond distances too long. The poor geometries probably affect the calculation of frequencies, and in particular intensities, of the various vibrational modes of $NH_3$. The molecule has a total of six modes of vibration, with two pairs being degenerate, and this more complex structure may increase the sensitivity of the results to errors in the Hessian and the dipole gradient. Indeed, it is observed that the two basis sets that give the worst results, cc-pVQZ and aug-cc-pVQZ, yield intensities with a completely wrong internal structure, i.e., the intensities that should have been the higher ones are very low and vice versa. The cc-pCVQZ basis, on the other hand, gets this structure more or less right although the numbers are not very impressive with the two highest intensities being only about 50% of what they should have been. In the R12 basis, these errors are reduced to less than 5%, and both geometrical and vibrational results are satisfactory.

### 4.4. CCSD(T)-R12 calculations

To investigate how electron correlation affects the performance of the Hellmann-Feynman approximation, we have used the Hellmann-Feynman forces at the level of explicitly correlated CCSD(T)-R12 theory [32-34, 41-44] to compute the bond length and harmonic vibrational wavenumber of $N_2$, the harmonic vibrational wavenumber and dipole gradient of CO, and the electronic barrier to linearity of $H_2O$.

For the CCSD(T)-R12 calculations, we have exploited finite perturbation theory. Thus, the first-order properties are obtained as

$$
E^{\alpha}=\frac{\partial E}{\partial \alpha}=\lim _{\lambda \rightarrow 0} \frac{1}{2 \lambda}\left[E\left(\hat{H}+\lambda \hat{H}^{\alpha}\right)-E\left(\hat{H}-\lambda \hat{H}^{\alpha}\right)\right], \quad(37)
$$

where $E(\hat{V})$ is the CCSD(T)-R12 energy calculated using the Hamiltonian $\hat{V}$ and $\hat{H}^{\alpha}=\partial \hat{H} / \partial \alpha$. By an extension of this scheme, the second-order properties such as force

Molecular geometry in the Hellmann-Feynman approximation

Table 10. Valence-only CCSD(T)-R12 results for the $N_2$ molecule; $\mathrm{d}E/\mathrm{d}R$ is the Hellmann-Feynman gradient.

<table>
  <thead>
    <tr>
      <th>$\frac{R}{a_0}$</th>
      <th>$\frac{\text{Energy}}{E_\text{h}}$</th>
      <th>$\frac{\mathrm{d}E/\mathrm{d}R}{E_\text{h}\,a_0^{-1}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2.050</td>
      <td>$-109.417\,599$</td>
      <td>$-0.041\,058$</td>
    </tr>
    <tr>
      <td>2.060</td>
      <td>$-109.417\,931$</td>
      <td>$-0.024\,947$</td>
    </tr>
    <tr>
      <td>2.070</td>
      <td>$-109.418\,105$</td>
      <td>$-0.009\,455$</td>
    </tr>
    <tr>
      <td>2.075</td>
      <td>$-109.418\,135$</td>
      <td>$-0.001\,925$</td>
    </tr>
    <tr>
      <td>2.080</td>
      <td>$-109.418\,127$</td>
      <td>$0.005\,410$</td>
    </tr>
    <tr>
      <td>2.085</td>
      <td>$-109.418\,083$</td>
      <td>$0.012\,643$</td>
    </tr>
    <tr>
      <td>2.090</td>
      <td>$-109.418\,003$</td>
      <td>$0.019\,736$</td>
    </tr>
    <tr>
      <td>2.100</td>
      <td>$-109.417\,738$</td>
      <td>$0.033\,617$</td>
    </tr>
    <tr>
      <td></td>
      <td>Exact</td>
      <td>HFA</td>
    </tr>
    <tr>
      <td>$r_e/\text{pm}$</td>
      <td>$109.88$</td>
      <td>$109.87$</td>
    </tr>
    <tr>
      <td>$\omega_e/\text{cm}^{-1}$</td>
      <td>$2367.2$</td>
      <td>$2362.4$</td>
    </tr>
    <tr>
      <td>$|\mathbf{g}_\text{exact}|/E_\text{h}\,a_0^{-1}$</td>
      <td>$0.0$</td>
      <td>$0.000\,34$</td>
    </tr>
    <tr>
      <td>$|\mathbf{g}_\text{HFA}|/E_\text{h}\,a_0^{-1}$</td>
      <td>$0.000\,33$</td>
      <td>$0.0$</td>
    </tr>
    <tr>
      <td>$E_\text{min}/E_\text{h}$</td>
      <td>$-109.418\,137$</td>
      <td>$-109.418\,137$</td>
    </tr>
  </tbody>
</table>

constants and dipole gradients are obtained using double finite perturbation theory

$$
\begin{aligned}
E^{\alpha \beta} &=\frac{\partial^{2} E}{\partial \alpha \partial \beta} \\
&=\lim _{\lambda \rightarrow 0} \lim _{\mu \rightarrow 0} \frac{1}{2 \lambda \mu}[ E(\hat{H}+\lambda \mu \hat{H}^{\alpha \beta})-E(\hat{H}-\lambda \mu \hat{H}^{\alpha \beta}) \\
&+2 E(\hat{H})+E(\hat{H}+\lambda \hat{H}^{\alpha}+\mu \hat{H}^{\beta}) \\
&+E(\hat{H}-\lambda \hat{H}^{\alpha}-\mu \hat{H}^{\beta}) \\
&-E(\hat{H}+\lambda \hat{H}^{\alpha})-E(\hat{H}-\lambda \hat{H}^{\alpha})-E(\hat{H}+\mu \hat{H}^{\beta}) \\
&-E(\hat{H}-\mu \hat{H}^{\beta})],
\end{aligned}
\tag{38}
$$

where $\hat{H}^{\alpha \beta}=\partial^{2} \hat{H} / \partial \alpha \partial \beta$.

Table 10 shows, for the $N_2$ molecule, the results of valence-only CCSD(T)-R12 calculations of the energy and Hellmann-Feynman gradient as a function of the interatomic distance. From the energy calculations, we find the minimum of the potential energy curve at $r_\text{e}=109.88\,\text{pm}$, whereas the Hellmann-Feynman gradient is zero at $r_\text{e}=109.87\,\text{pm}$. When we compute the force constant by numerical differentiation of the Hell-mann-Feynman gradient, we obtain a harmonic vibra-tional wavenumber of $\omega_\text{e}=2362.4\,\text{cm}^{-1}$, only $0.2\%$ below the exact wavenumber of the CCSD(T)-R12 cal-culations. The norm of the exact gradient at the Hell-mann-Feynman minimum is $0.000\,34\,E_\text{h}\,a_0^{-1}$, whereas the Hellmann-Feynman gradient at the exact minimum is $0.000\,33\,E_\text{h}\,a_0^{-1}$. With the present R12 basis, we obtain roughly the same accuracy at the CCSD(T)-R12 level as we did for the Hartree-Fock calculations. Thus, the correlation component of the calculation, which is

Table 11. Valence-only CCSD(T)-R12 results for the CO molecule; $\mathrm{d}E/\mathrm{d}R=\frac{1}{2}(\mathrm{d}E/\mathrm{d}z_\text{C}-\mathrm{d}E/\mathrm{d}z_\text{O})$ is the Hellmann-Feynman gradient; $d_\text{e}$ is the dipole moment; and $d_\text{e}'=\mathrm{d}d_\text{e}/\mathrm{d}R$.

<table>
  <thead>
    <tr>
      <th>$\frac{R}{a_0}$</th>
      <th>$\frac{\text{Energy}}{E_\text{h}}$</th>
      <th>$\frac{\mathrm{d}E/\mathrm{d}R}{E_\text{h}\,a_0^{-1}}$</th>
      <th>$\frac{\text{Dipole}}{e a_0}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2.110</td>
      <td>$-113.201\,504$</td>
      <td>$-0.033\,428$</td>
      <td>$0.059\,026$</td>
    </tr>
    <tr>
      <td>2.120</td>
      <td>$-113.201\,763$</td>
      <td>$-0.020\,252$</td>
      <td>$0.052\,232$</td>
    </tr>
    <tr>
      <td>2.130</td>
      <td>$-113.201\,892$</td>
      <td>$-0.007\,559$</td>
      <td>$0.045\,439$</td>
    </tr>
    <tr>
      <td>2.135</td>
      <td>$-113.201\,910$</td>
      <td>$-0.001\,390$</td>
      <td>$0.042\,043$</td>
    </tr>
    <tr>
      <td>2.140</td>
      <td>$-113.201\,897$</td>
      <td>$0.004\,665$</td>
      <td>$0.038\,649$</td>
    </tr>
    <tr>
      <td>2.150</td>
      <td>$-113.201\,782$</td>
      <td>$0.016\,434$</td>
      <td>$0.031\,861$</td>
    </tr>
    <tr>
      <td>2.160</td>
      <td>$-113.201\,551$</td>
      <td>$0.027\,763$</td>
      <td>$0.025\,078$</td>
    </tr>
    <tr>
      <td></td>
      <td>Exact</td>
      <td colspan="2">HFA</td>
    </tr>
    <tr>
      <td>$r_e/\text{pm}$</td>
      <td>$113.00$</td>
      <td colspan="2">$113.04$</td>
    </tr>
    <tr>
      <td>$\omega_e/\text{cm}^{-1}$</td>
      <td>$2169.1$</td>
      <td colspan="2">$2165.8$</td>
    </tr>
    <tr>
      <td>$d_e/e a_0$</td>
      <td>$0.041\,8$</td>
      <td colspan="2">$0.041\,3$</td>
    </tr>
    <tr>
      <td>$d_e'/e$</td>
      <td>$0.679$</td>
      <td colspan="2">$0.682$</td>
    </tr>
    <tr>
      <td>$|\mathbf{g}_\text{exact}|/E_\text{h}\,a_0^{-1}$</td>
      <td>$0.0$</td>
      <td colspan="2">$0.000\,93$</td>
    </tr>
    <tr>
      <td>$|\mathbf{g}_\text{HFA}|/E_\text{h}\,a_0^{-1}$</td>
      <td>$0.002\,98$</td>
      <td colspan="2">$0.002\,27$</td>
    </tr>
    <tr>
      <td>$E_\text{min}/E_\text{h}$</td>
      <td>$-113.201\,910$</td>
      <td colspan="2">$-113.201\,910$</td>
    </tr>
  </tbody>
</table>

described effectively by the $r_{12}$-dependent functions, does not introduce any noticeable new errors in the Hellmann-Feynman approximation. Thus, in our opi-nion, the Hellmann-Feynman approximation may indeed be an important tool for R12 calculations, once basis-set deficiencies at the Hartree-Fock level are elim-inated.

Similar results are obtained for the CO molecule, see table 11. For this molecule, we have investigated also the dipole moment and dipole gradient. For the Hellmann-Feynman optimized structure, the norm of the residual Hellmann-Feynman force (because of lack of transla-tional and rotational invariance) is $0.002\,27\,E_\text{h}\,a_0^{-1}$. From numerical differentiation of the Hellmann-Feynman gradient, we obtain a harmonic vibrational wavenumber of $\omega_\text{e}=2165.8\,\text{cm}^{-1}$, only $0.2\%$ below the exact wavenumber of the CCSD(T)-R12 calcula-tions. The exact dipole gradient has been obtained at the exact minimum by numerical differentiation of the dipole moments computed for different internuclear dis-tances (table 11), whereas the dipole gradient within the Hellmann-Feynman minimum framework has been obtained through application of double finite perturba-tion theory at the Hellmann-Feynman minimum. The error of the latter is only $0.4\%$.

Valence-only CCSD(T)-R12 results for $\mathrm{H_2O}$ are col-lected in tables 12 and 13. There has recently been an interest in the electronic barrier to linearity in the water molecule [45, 46], and therefore we have optimized the geometries of the $C_{2\text{v}}$ minimum energy structure and the linear saddle-point structure of $\mathrm{H_2O}$ at the valence-only

Table 12. Valence-only CCSD(T)-R12 results for the $\mathrm{H}_{2} \mathrm{O}$ molecule ($\mathrm{C}_{2 v}$ geometry); the $\mathrm{H}$ atoms lie on the $x$ axis; the $\mathrm{O}$ atom lies on the $z$ axis; and $\mathrm{d} E / \mathrm{d} z_{\text {internal }}=\mathrm{d} E / \mathrm{d} z_{\mathrm{O}}-2 \mathrm{~d} E / \mathrm{d} z_{\mathrm{H}}$.

<table>
  <thead>
    <tr>
      <th>
        $\frac{x_{\mathrm{H}}}{a_{0}}$
      </th>
      <th>
        $\frac{z_{\mathrm{O}}}{a_{0}}$
      </th>
      <th>
        Energy
      </th>
      <th>
        $\frac{\mathrm{d} E / \mathrm{d} x_{\mathrm{H}}}{E_{\mathrm{h}} a_{0}^{-1}}$
      </th>
      <th>
        $\frac{\mathrm{d} E / \mathrm{d} z_{\mathrm{H}}}{E_{\mathrm{h}} a_{0}^{-1}}$
      </th>
      <th>
        $\frac{\mathrm{d} E / \mathrm{d} z_{\mathrm{O}}}{E_{\mathrm{h}} a_{0}^{-1}}$
      </th>
      <th>
        $\frac{\sum_{i} \mathrm{~d} E / \mathrm{d} z_{i}}{E_{\mathrm{h}} a_{0}^{-1}}$
      </th>
      <th>
        $\frac{\mathrm{d} E / \mathrm{d} z_{\text {internal }}}{E_{\mathrm{h}} a_{0}^{-1}}$
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
      </td>
      <td>
      </td>
      <td>
        $E_{\mathrm{h}}$
      </td>
      <td>
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
        $1.420$
      </td>
      <td>
        $1.100$
      </td>
      <td>
        $- 76.371\,723$
      </td>
      <td>
        $- 0.008\,787$
      </td>
      <td>
        $0.006\,170$
      </td>
      <td>
        $- 0.010\,590$
      </td>
      <td>
        $0.001\,751$
      </td>
      <td>
        $- 0.022\,930$
      </td>
    </tr>
    <tr>
      <td>
        $1.420$
      </td>
      <td>
        $1.110$
      </td>
      <td>
        $- 76.371\,790$
      </td>
      <td>
        $- 0.006\,594$
      </td>
      <td>
        $0.003\,792$
      </td>
      <td>
        $- 0.005\,858$
      </td>
      <td>
        $0.001\,726$
      </td>
      <td>
        $- 0.013\,442$
      </td>
    </tr>
    <tr>
      <td>
        $1.420$
      </td>
      <td>
        $1.120$
      </td>
      <td>
        $- 76.371\,808$
      </td>
      <td>
        $- 0.004\,462$
      </td>
      <td>
        $0.001\,434$
      </td>
      <td>
        $- 0.001\,168$
      </td>
      <td>
        $0.001\,700$
      </td>
      <td>
        $- 0.004\,036$
      </td>
    </tr>
    <tr>
      <td>
        $1.420$
      </td>
      <td>
        $1.130$
      </td>
      <td>
        $- 76.371\,780$
      </td>
      <td>
        $- 0.002\,389$
      </td>
      <td>
        $- 0.000\,903$
      </td>
      <td>
        $0.003\,479$
      </td>
      <td>
        $0.001\,673$
      </td>
      <td>
        $0.005\,285$
      </td>
    </tr>
    <tr>
      <td>
        $1.430$
      </td>
      <td>
        $1.100$
      </td>
      <td>
        $- 76.371\,812$
      </td>
      <td>
        $- 0.004\,565$
      </td>
      <td>
        $0.003\,992$
      </td>
      <td>
        $- 0.006\,298$
      </td>
      <td>
        $0.001\,686$
      </td>
      <td>
        $- 0.014\,282$
      </td>
    </tr>
    <tr>
      <td>
        $1.430$
      </td>
      <td>
        $1.110$
      </td>
      <td>
        $- 76.371\,836$
      </td>
      <td>
        $- 0.002\,458$
      </td>
      <td>
        $0.001\,674$
      </td>
      <td>
        $- 0.001\,686$
      </td>
      <td>
        $0.001\,662$
      </td>
      <td>
        $- 0.005\,034$
      </td>
    </tr>
    <tr>
      <td>
        $1.430$
      </td>
      <td>
        $1.120$
      </td>
      <td>
        $- 76.371\,813$
      </td>
      <td>
        $- 0.000\,410$
      </td>
      <td>
        $- 0.000\,624$
      </td>
      <td>
        $0.002\,886$
      </td>
      <td>
        $0.001\,638$
      </td>
      <td>
        $0.004\,135$
      </td>
    </tr>
    <tr>
      <td>
        $1.430$
      </td>
      <td>
        $1.130$
      </td>
      <td>
        $- 76.371\,745$
      </td>
      <td>
        $0.001\,580$
      </td>
      <td>
        $- 0.002\,902$
      </td>
      <td>
        $0.007\,416$
      </td>
      <td>
        $0.001\,612$
      </td>
      <td>
        $0.013\,220$
      </td>
    </tr>
    <tr>
      <td>
        $1.440$
      </td>
      <td>
        $1.100$
      </td>
      <td>
        $- 76.371\,818$
      </td>
      <td>
        $- 0.000\,442$
      </td>
      <td>
        $0.001\,900$
      </td>
      <td>
        $- 0.002\,178$
      </td>
      <td>
        $0.001\,622$
      </td>
      <td>
        $- 0.005\,978$
      </td>
    </tr>
    <tr>
      <td>
        $1.440$
      </td>
      <td>
        $1.110$
      </td>
      <td>
        $- 76.371\,801$
      </td>
      <td>
        $0.001\,581$
      </td>
      <td>
        $- 0.000\,360$
      </td>
      <td>
        $0.002\,319$
      </td>
      <td>
        $0.001\,599$
      </td>
      <td>
        $0.003\,039$
      </td>
    </tr>
    <tr>
      <td>
        $1.440$
      </td>
      <td>
        $1.120$
      </td>
      <td>
        $- 76.371\,739$
      </td>
      <td>
        $0.003\,547$
      </td>
      <td>
        $- 0.002\,601$
      </td>
      <td>
        $0.006\,777$
      </td>
      <td>
        $0.001\,575$
      </td>
      <td>
        $0.011\,979$
      </td>
    </tr>
    <tr>
      <td>
        $1.440$
      </td>
      <td>
        $1.130$
      </td>
      <td>
        $- 76.371\,632$
      </td>
      <td>
        $0.005\,457$
      </td>
      <td>
        $- 0.004\,822$
      </td>
      <td>
        $0.011\,194$
      </td>
      <td>
        $0.001\,550$
      </td>
      <td>
        $0.020\,838$
      </td>
    </tr>
    <tr>
      <td>
      </td>
      <td>
      </td>
      <td>
      </td>
      <td>
        Exact
      </td>
      <td>
        HFA
      </td>
      <td>
      </td>
      <td>
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        $r_{e}/\mathrm{pm}$
      </td>
      <td>
      </td>
      <td>
        $95.81$
      </td>
      <td>
        $96.05$
      </td>
      <td>
      </td>
      <td>
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        ${\angle}_{\mathrm{HOH}}/\mathrm{deg}$
      </td>
      <td>
        $104.45$
      </td>
      <td>
        $104.58$
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
      <td colspan="2">
        ${|{\mathbf{g}}_{\text{exact}}|}/{E_{\mathrm{h}} a_{0}^{- 1}}$
      </td>
      <td>
      </td>
      <td>
        $0.0$
      </td>
      <td>
        $0.004\,31$
      </td>
      <td>
      </td>
      <td>
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        ${|{\mathbf{g}}_{\text{HFA}}|}/{E_{\mathrm{h}} a_{0}^{- 1}}$
      </td>
      <td>
      </td>
      <td>
        $0.004\,19$
      </td>
      <td>
        $0.000\,99$
      </td>
      <td>
      </td>
      <td>
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        $E_{\text{min}}/E_{\mathrm{h}}$
      </td>
      <td>
      </td>
      <td>
        $- 76.371\,836$
      </td>
      <td>
        $- 76.371\,824$
      </td>
      <td>
      </td>
      <td>
      </td>
      <td>
      </td>
    </tr>
  </tbody>
</table>

Table 13. Valence-only CCSD(T)-R12 results for the $\mathrm{H}_{2} \mathrm{O}$ molecule ($\mathrm{D}_{\infty \text{h}}$ geometry); the atoms lie on the $x$ axis; and $\Delta E$ is the electronic barrier to linearity.

<table>
  <thead>
    <tr>
      <th>
        $\frac{R}{\mathrm{pm}}$
      </th>
      <th>
        Energy
      </th>
      <th>
        $\frac{\mathrm{d} E / \mathrm{d} x_{\mathrm{H}}}{E_{\mathrm{h}} a_{0}^{-1}}$
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
      </td>
      <td>
        $E_{\mathrm{h}}$
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        $91.0$
      </td>
      <td>
        $- 76.319\,482$
      </td>
      <td>
        $- 0.033\,600$
      </td>
    </tr>
    <tr>
      <td>
        $92.0$
      </td>
      <td>
        $- 76.320\,394$
      </td>
      <td>
        $- 0.019\,980$
      </td>
    </tr>
    <tr>
      <td>
        $93.0$
      </td>
      <td>
        $- 76.320\,812$
      </td>
      <td>
        $- 0.007\,271$
      </td>
    </tr>
    <tr>
      <td>
        $93.5$
      </td>
      <td>
        $- 76.320\,845$
      </td>
      <td>
        $- 0.001\,241$
      </td>
    </tr>
    <tr>
      <td>
        $94.0$
      </td>
      <td>
        $- 76.320\,768$
      </td>
      <td>
        $0.004\,582$
      </td>
    </tr>
    <tr>
      <td>
        $94.5$
      </td>
      <td>
        $- 76.320\,583$
      </td>
      <td>
        $0.010\,204$
      </td>
    </tr>
    <tr>
      <td>
        $95.0$
      </td>
      <td>
        $- 76.320\,294$
      </td>
      <td>
        $0.015\,631$
      </td>
    </tr>
    <tr>
      <td>
        $96.0$
      </td>
      <td>
        $- 76.319\,420$
      </td>
      <td>
        $0.025\,923$
      </td>
    </tr>
    <tr>
      <td>
      </td>
      <td>
        Exact
      </td>
      <td>
        HFA
      </td>
    </tr>
    <tr>
      <td>
        $r_{e}/\mathrm{pm}$
      </td>
      <td>
        $93.40$
      </td>
      <td>
        $93.61$
      </td>
    </tr>
    <tr>
      <td>
        ${|{\mathbf{g}}_{\text{exact}}|}/{E_{\mathrm{h}} a_{0}^{- 1}}$
      </td>
      <td>
        $0.0$
      </td>
      <td>
        $0.003\,41$
      </td>
    </tr>
    <tr>
      <td>
        ${|{\mathbf{g}}_{\text{HFA}}|}/{E_{\mathrm{h}} a_{0}^{- 1}}$
      </td>
      <td>
        $0.003\,45$
      </td>
      <td>
        $0.0$
      </td>
    </tr>
    <tr>
      <td>
        $E_{\text{min}}/E_{\mathrm{h}}$
      </td>
      <td>
        $- 76.320\,848$
      </td>
      <td>
        $- 76.320\,838$
      </td>
    </tr>
    <tr>
      <td>
        $\Delta E/\mathrm{cm}^{- 1}$
      </td>
      <td>
        $11\,190.6$
      </td>
      <td>
        $11\,190.1$
      </td>
    </tr>
  </tbody>
</table>

CCSD(T)-R12 level. Using Hellmann–Feynman gradients, we find that the OH bond length is overestimated by about $0.2$ pm both for the $\mathrm{C}_{2 v}$ and linear structure ($0.2\%$ error). For both structures, the energy at the Hellmann–Feynman minimum is found about $0.01$ m$E_{\mathrm{h}}$ above the true minimum. Thus, an almost perfect cancellation of errors occurs with respect to the electronic barrier to linearity. The error in this quantity is negligible.

From the above results, we conclude that the use of the Hellmann–Feynman forces in CCSD(T)-R12 calculations with appropriate basis sets is a very promising approach. In our calculations, we find errors smaller than $0.5\%$. Furthermore, it is remarkable that the R12 basis sets, which have been developed explicitly for the CCSD(T)-R12 calculations, are such good basis sets for the computation of Hellmann–Feynman forces.

### 5. Conclusion

We have investigated the Hellmann–Feynman approximation for the calculation of molecular geometrical properties at the Hartree–Fock and CCSD(T)-R12 levels. With the larger modern basis sets, it appears that the differences between the properties calculated in the Hellmann–Feynman approximation and by (analytical or numerical) differentiation appear to be small. However, it is important to use basis sets that give a good description of the inner valence regions, such as the larger cc-pCVXZ basis sets and in particular the R12 basis sets.

The Hellmann–Feynman properties do not exhibit the usual translational and rotational symmetries that arise from differentiation of the electronic energy. However, these symmetries may be imposed as discussed in the present paper, improving the quality of the results. In particular, for the molecular Hessian it is essential that the diagonal Cartesian elements are determined by invoking translational invariance. In this manner, we avoid the slow convergence of the Coulomb contact

term, thereby obtaining a convergence of the frequencies which is as rapid as the molecular forces.

This work has received support through grants of computer time from the Research Council of Norway (Grants Nos NN1118K and NN2694K).

### References

[1] HELLMANN, H., 1937, *Einführung in die Quantenchemie* (Leipzig: Deuticke).

[2] FEYNMAN, R. P., 1939, *Phys. Rev.*, **56**, 340.

[3] PULAY, P., 1995, *Modern Electronic Structure Theory*, edited by D. R. Yarkony (Singapore: World Scientific).

[4] PULAY, P., 1970, *Molec. Phys.*, **18**, 473.

[5] GODDARD, J. D., HANDY, N. C., and SCHAEFER III, H. F., 1979, *J. chem. Phys.*, **71**, 1525.

[6] POPLE, J. A., KRISHNAN, R., SCHLEGEL, H. B., and BINKLEY, J. S., 1979, *Int. J. Quantum Chem. Quantum Chem. Symp.*, **13**, 225.

[7] HELGAKER, T. U., ALMLÖF, J., JENSEN, H. J. AA., and JØRGENSEN, P., 1986, *J. chem. Phys.*, **84**, 6266.

[8] GAW, J. F., YAMAGUCHI, Y., and SCHAEFFER III, H. F., 1984, *J. chem. Phys.*, **81**, 6395.

[9] GAW, J. F., and HANDY, N. C., 1987, *Proc. Semin. Comput. Methods Quantum Chem.* 7th, University of York.

[10] OLSEN, J., and JØRGENSEN, P., 1995, *Modern ElectronicStructure Theory*, edited by D. R. Yarkony (Singapore: World Scientific).

[11] AUGSPURGER, J. D., and DYKSTRA, C. E., 1991, *J. phys. Chem.*, **95**, 9230.

[12] NAKATSUJI, H., KANDA, K., HADA, M., and YONEZAWA, T., 1982, *J. chem. Phys.*, **77**, 3109.

[13] NAKATSUJI, H., KANDA, K., HADA, M., and YONEZAWA, T., 1983, *J. chem. Phys.*, **79**, 2493.

[14] NAKATSUJI, H., KANDA, K., and YONEZAWA, T., 1982, *J. chem. Phys.*, **77**, 1961.

[15] ALMLÖF, J., and TAYLOR, P. R., 1987, *J. chem. Phys.*, **86**, 4070.

[16] DUNNING JR., T. H., 1989, *J. chem. Phys.*, **90**, 1007.

[17] KENDALL, R. A., DUNNING JR., T. H., and HARRISON, R. J., 1992, *J. chem. Phys.*, **96**, 6796.

[18] WOON, D. E., and DUNNING JR., T. H., 1994, *J. chem. Phys.*, **100**, 2975.

[19] DUNNING JR., T. H., WOON, D. E., and PETERSON, K. A., unpublished.

[20] WOON, D. E., and DUNNING JR., T. H., 1995, *J. chem. Phys.*, **103**, 4572.

[21] MEYER, W., and PULAY, P., 1972, *J. chem. Phys.*, **56**, 2109.

[22] LAAKSONEN, L., PYYKKÖ, P., and SUNDHOLM, D., 1983, *Chem. Phys. Lett.*, **96**, 1.

[23] HALKIER, A., KOCH, H., CHRISTIANSEN, O., JØRGENSEN, P., and HELGAKER, T., 1997, *J. chem. Phys.*, **107**, 849.

[24] HELGAKER, T., GAUSS, J., JØRGENSEN, P., and OLSEN, J., 1997, *J. chem. Phys.*, **106**, 6430.

[25] RUUD, K., and HELGAKER, T., 1997, *Chem. Phys. Lett.*, **264**, 17.

[26] HELGAKER, T., and TAYLOR, P. R., 1995, *Modern Electronic Structure Theory*, edited by D. R. Yarkony (Singapore: World Scientific).

[27] HELGAKER, T., 1988, *Acta Chem. Scand. A*, **42**, 515.

[28] KOMORNICKI, A., ISHIDA, K., MOROKUMA, K., DITCHFIELD, R., and CONRAD, M., 1977, *Chem. Phys. Lett.*, **45**, 595.

[29] WIDMARK, P.-O., MALMQVIST, P.-Å., and ROOS, B. O., 1990, *Theoret. Chim. Acta*, **77**, 291.

[30] HELGAKER, T., JENSEN, H. J. AA., JØRGENSEN, P., OLSEN, J., RUUD, K., ÅGREN, H., ANDERSEN, T., BAK, K. L., BAKKEN, V., CHRISTIANSEN, O., DAHLE, P., DALSKOV, E. K., ENEVOLDSEN, T., HEIBERG, H., HETTEMA, H., JONSSON, D., KIRPEKAR, S., KOBAYASHI, R., KOCH, H., MIKKELSEN, K. V., NORMAN, P., PACKER, M. J., SAUE, T., TAYLOR, P. R., and VAHTRAS, O., 1997, *Dalton, an ab initio* electronic structure program: see http://www. kjemi.uio.no/software/dalton/dalton.html.

[31] NOGA, J., and KLOPPER, W., 1995, DIRCCR12 program.

[32] NOGA, J., KLOPPER, W., and KUTZELNIGG, W., 1997, *Recent Advances in Coupled-Cluster Theory*, edited by R. J. Bartlett (Singapore: World Scientific).

[33] MÜLLER, H., KUTZELNIGG, W., and NOGA, J., 1997, *Molec. Phys.*, **92**, 535.

[34] KLOPPER, W., 1998, *The Encyclopedia of Computational Chemistry*, edited by P. v. R. Schleyer, N. L. Allinger, T. Clark, J. Gasteiger, P. A. Kollman, H. F. Schaefer III and P. R. Schreiner (Chichester: Wiley).

[35] The aug-cc-pCVXZ (X = D, T, Q, 5, 6), VTZ, and TZV basis sets were obtained from the Extensible Computational Chemistry Environment Basis Set Database, Version 1.0, as developed and distributed by the Molecular Science Computing Facility, Environmental and Molecular Sciences Laboratory which is part of the Pacific Northwest Laboratory, PO Box 999, Richmond, WA 99352, USA, and funded by the US Department of Energy. The Pacific Northwest Laboratory is a multi-program laboratory operated by Battelle Memorial Institute for the US Department of Energy under Contract DE-AC06-76RLO 1830.

[36] SCHÄFER, A., HORN, H., and AHLRICHS, R., 1992, *J. chem. Phys.*, **97**, 2571.

[37] SCHÄFER, A., HUBER, C., and AHLRICHS, R., 1994, *J. chem. Phys.*, **100**, 5829.

[38] BAKKEN, V., and HELGAKER, T., unpublished.

[39] PENG, C., AYALA, P. Y., SCHLEGEL, H. B., and FRISCH, M. J., 1996, *J. comput. Chem.*, **17**, 49.

[40] CIOSLOWSKI, J., 1989, *J. Amer. chem. Soc.*, **111**, 8333.

[41] NOGA, J., KUTZELNIGG, W., and KLOPPER, W., 1992, *Chem. Phys. Lett.*, **199**, 497.

[42] NOGA, J., and KUTZELNIGG, W., 1994, *J. chem. Phys.*, **101**, 7738.

[43] KLOPPER, W., and NOGA, J., 1995, *J. chem. Phys.*, **103**, 6127.

[44] HELGAKER, T., KLOPPER, W., KOCH, H., and NOGA, J., 1997, *J. chem. Phys.*, **106**, 9639.

[45] CSÁSZÁR, A. G., ALLEN, W. D., and SCHAEFER III, H. F., 1998, *J. chem. Phys.*, **108**, 9751.

[46] TARCZAY, G., CSÁSZÁR, A. G., KLOPPER, W., SZALAY, V., ALLEN, W. D., and SCHAEFER III, H. F., unpublished.