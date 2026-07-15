![](./images/811634985940287488_1.jpg)

Second-order nonadiabatic couplings from time-dependent density
functional theory: Evaluation in the immediate vicinity of Jahn-
Teller/Renner-Teller intersections

Chunping Hu, Osamu Sugino, and Kazuyuki Watanabe

Citation: J. Chem. Phys. 135, 074101 (2011); doi: 10.1063/1.3624565
View online: http://dx.doi.org/10.1063/1.3624565
View Table of Contents: http://jcp.aip.org/resource/1/JCPSA6/v135/i7
Published by the American Institute of Physics.

---

Additional information on J. Chem. Phys.
Journal Homepage: http://jcp.aip.org/
Journal Information: http://jcp.aip.org/about/about_the_journal
Top downloads: http://jcp.aip.org/features/most_downloaded
Information for Authors: http://jcp.aip.org/authors

ADVERTISEMENT

![](./images/811634985940287488_2.jpg)

# Second-order nonadiabatic couplings from time-dependent density functional theory: Evaluation in the immediate vicinity of Jahn-Teller/Renner-Teller intersections

Chunping Hu, $^{1,a)}$ Osamu Sugino, $^{2}$ and Kazuyuki Watanabe $^{1}$

$^{1}$ Department of Physics, Tokyo University of Science, 1-3 Kagurazaka, Shinjuku, Tokyo 162-8601, Japan
$^{2}$ Institute for Solid State Physics, University of Tokyo, Kashiwa, Chiba 277-8581, Japan

(Received 31 May 2011; accepted 13 July 2011; published online 15 August 2011)

For a rigorous quantum simulation of nonadiabatic dynamics of electrons and nuclei, knowledge of not only the first-order but also the second-order nonadiabatic couplings (NACs) is required. Here, we propose a method to efficiently calculate the second-order NAC from time-dependent density functional theory (TDDFT), on the basis of the Casida ansatz adapted for the computation of first-order NAC, which has been justified in our previous work and can be shown to be valid for calculating second-order NAC between ground state and singly excited states within the Tamm-Dancoff approximation. Test calculations of the second-order NAC in the immediate vicinity of Jahn-Teller and Renner-Teller intersections show that calculation results from TDDFT, combined with modified linear response theory, agree well with the prediction from the Jahn-Teller/Renner-Teller models. Contrary to the diverging behavior of the first-order NAC near all types of intersection points, the Cartesian components of the second-order NAC are shown to be negligibly small near Renner-Teller glancing intersections, while they are significantly large near the Jahn-Teller conical intersections. Nevertheless, the components of the second-order NAC can cancel each other to a large extent in Jahn-Teller systems, indicating the background of neglecting the second-order NAC in practical dynamics simulations. On the other hand, it is shown that such a cancellation becomes less effective in an elliptic Jahn-Teller system and thus the role of second-order NAC needs to be evaluated in the rigorous framework. Our study shows that TDDFT is promising to provide accurate data of NAC for full quantum mechanical simulation of nonadiabatic processes. © 2011 *American Institute of Physics*. [doi:10.1063/1.3624565]

## I. INTRODUCTION

Nonadiabatic transitions, i.e., transitions between adiabatic states, are ubiquitous in physical, chemical, and biological systems. $^{1–3}$ In recent years, there has been growing interest in quantum mechanical study of nonadiabatic transitions, $^{4–9}$ which has been regarded as a challenging field for theorists: Although most *ab initio* theories are built upon the Born-Oppenheimer approximation to separate the nuclear and electronic degrees of freedom, this approximation will break down in the region where nonadiabatic transitions occur. In order to describe nonadiabatic processes, it is necessary to go beyond the Born-Oppenheimer approximation and take account of nonadiabatic couplings (NACs), which is the driving force for nonadiabatic transition to different potential energy surfaces. $^{3}$ Since NACs (preferentially called as first and second derivative couplings in quantum chemistry) are defined as matrix elements of the first and second derivatives with respect to nuclear coordinates between adiabatic states (many-body wavefunctions), nonadiabatic dynamics simulation has long been relying on wavefunction-based methods to provide the NAC data. For more efficient calculation of NAC, density functional methods, $^{10}$ especially those based on time-dependent density functional theory (TDDFT), have been developed in the last decade. The study was initiated by Chernyak and Mukamel $^{11}$ who proposed to perturb the ground state using the nuclear derivative of Hamiltonian and to compute NAC from the density response. This scheme was first implemented by Baer $^{12}$ to study $H_3$ using a real-time approach and by $Hu$ *et al.* $^{13,14}$ to systematically study small molecules using the frequency-space formalism of Casida *et al.* $^{15,16}$ To avoid the pseudopotential problem in the calculation of NAC, all-electron TDDFT schemes have been independently developed by $Hu$ *et al.* $^{17}$ and Send and Furche. $^{18}$ Alternatively, formulations of NAC from TDDFT have also been achieved by Tavernelli *et al.* $^{19–21}$ using the Casida ansatz, which is promising to correctly give NACs between excited states within the Tamm-Dancoff approximation (TDA). A recent study by $Hu$ *et al.* $^{22}$ further clarified relationships between different DFT/TDDFT formulations of NAC. $^{10,19,23,24}$ These NAC schemes have been applied to nonadiabatic dynamics simulations and have shown that TDDFT is promising for balanced cost and performance on the computation of polyatomic systems. $^{19,25–27}$

So far most studies on the computation and application of NAC are focused on the first-order, without much discussion on the second-order. Although second-order NAC can be in principle expressed by the first-order, the numerical evaluation cannot be easily carried out. This is because not only the differentiation of first-order NAC is needed, but also a

$^{a)}$Electronic mail: hu@rs.kagu.tus.ac.jp.

complete expansion in eigenstates makes the product of first-order NAC involving these states rather complicated. In the wavefunction-based framework, although several methods for evaluating second-order NAC have been presented, $^{28-30}$ there are very few literatures on the direct evaluation of second-order NAC in molecular systems. Correspondingly, the practical study by nonadiabatic simulation seldom takes second-order NAC into consideration. A simplified procedure is to replace the full quantum description as the quantum-classical simulation, since the time evolution of the nuclear degrees of freedom is described by a Poisson bracket that introduces only the first-order derivatives. $^{31}$ On the other hand, even the full nonadiabatic operators, both first- and second-order NACs, are taken into consideration in the formulation, such as *ab initio* multiple spawning, the second-order NAC are just ignored in the practice. $^{7,32,33}$ It is noted that the second-order NACs are often found to be small by experience; $^{7}$ however, they are not the second-order item in the Taylor expansion but originated from the presence of the scalar Laplacian. Therefore, in contrast to the vector form of first-order NACs, the second-order NACs are scalars. In order to verify the validity of neglecting second-order NAC in nonadiabatic simulations, it is crucial to examine the behavior of second-order NAC when the intersection points are approached. If the similar diverging behavior as first-order NAC is observed, the neglect of second-order NAC needs to be critically reconsidered.

The aim of the present study is to develop an efficient TDDFT method for the calculation of second-order NAC, which is desired to have the same level computational cost as the first-order, and then to examine the behavior of second-order NAC near intersection points. For the efficiency, the explicit expansion into first-order NAC should be avoided. We will show that this can be achieved by using the Casida ansatz adapted for the first-order NAC, $^{22}$ while there is no need to explicitly construct auxiliary excited-state wavefunctions. $^{23}$ Justification of our procedure can be shown within the TDA. To check if the second-order NAC diverge at intersection points, we carry out TDDFT calculations within modified linear response theory $^{34,35}$ in the immediate vicinity of Jahn-Teller, $^{36,37}$ Renner-Teller, $^{38,39}$ and elliptic Jahn-Teller intersections, $^{40}$ and compare results with the model analysis. It is verified that our TDDFT results are in good agreement with the predictions from the models. In the vicinity of different types of intersections, different behaviors of second-order NAC are revealed, either in the Cartesian components ($x$, $y$, and $z$) or as a whole scalar: The components are shown to be negligibly small near Renner-Teller glancing intersections, while they are significantly large near the Jahn-Teller conical intersections. Nevertheless, the components of second-order NAC can cancel each other to a large extent in Jahn-Teller systems, indicating the background of neglecting second-order NAC in practical dynamics simulations. On the other hand, it is also shown that such a cancellation becomes less effective in an elliptic Jahn-Teller system and thus the role of second-order NAC needs to be evaluated in the rigorous framework.

The present paper is organized as follows. In Sec. II, we present the formulation of second-order NAC from TDDFT and its extension within modified linear response theory. In Sec. III, implementation in the planewave pseudopotential framework and computational details are given. In Sec. IV, practical calculations on various molecular systems possessing Jahn-Teller, Renner-Teller, or elliptic Jahn-Teller intersections are performed, and compared with ideal values predicted by Jahn-Teller/Renner-Teller models. In Sec. V, we conclude our work.

## II. FORMULATION

### A. Second-order NAC from the adapted Casida ansatz

In the previous work of Hu *et al.*, rigorous TDDFT formulations of the first-order NAC have been achieved, using the Kohn-Sham (KS) matrix elements of either $h$-operator $^{13,14,17}$ or $d$-operator, $^{22}$ i.e.,

$$
\hat{h}_{\mu} \equiv \frac{\partial \hat{H}}{\partial R_{\mu}}, \quad \hat{d}_{\mu} \equiv \frac{\partial}{\partial R_{\mu}}, \tag{1}
$$

where $H$ is the many-body Hamiltonian and $R_{\mu}$ is the nuclear coordinate with $\mu$ representing $x$, $y$, and $z$ components and atom index.

The $h$-matrix formulation gives first-order NAC as

$$
\left\langle \Psi_0 \right| \frac{\partial}{\partial R_{\mu}} \left| \Psi_I \right\rangle = \omega_I^{-1} \left\langle \Psi_0 \right| \frac{\partial \hat{H}}{\partial R_{\mu}} \left| \Psi_I \right\rangle = \omega_I^{-3/2} \mathbf{h}_{\mu}^{\dagger} \mathbf{S}^{-1/2} \mathbf{F}_I, \tag{2}
$$

where $\Psi_0$ ($\Psi_I$) is the many-body electronic wavefunction of the ground ($I$th excited) state, and $\omega_I$ is the excitation energy. Matrix elements of $\mathbf{S}$ and $\mathbf{h}_{\mu}$ are given by

$$
S_{ij\sigma,kl\tau} = \frac{\delta_{\sigma,\tau} \delta_{i,k} \delta_{j,l}}{(f_{k\tau} - f_{l\tau})(\varepsilon_{l\tau} - \varepsilon_{k\tau})}, \tag{3}
$$

$$
h_{ij\sigma,\mu} = \left\langle \psi_{i\sigma} \right| \frac{\partial \hat{H}}{\partial R_{\mu}} \left| \psi_{j\sigma} \right\rangle, \tag{4}
$$

where $\psi_{i\sigma}$, $\varepsilon_{i\sigma}$, $f_{i\sigma}$ are, respectively, the orbital, eigenvalue, and occupation number for the $i$th KS state with spin $\sigma$. $\mathbf{F}_I$ is the eigenvector of the Casida equation $^{15}$

$$
\Omega \mathbf{F}_I = \omega_I^2 \mathbf{F}_I, \tag{5}
$$

where

$$
\begin{aligned}
\Omega_{ij\sigma,kl\tau} &= \delta_{\sigma,\tau} \delta_{i,k} \delta_{j,l} (\varepsilon_{l\tau} - \varepsilon_{k\tau})^2 + 2\sqrt{(f_{i\sigma} - f_{j\sigma})(\varepsilon_{j\sigma} - \varepsilon_{i\sigma})} \\
&\quad \times K_{ij\sigma,kl\tau} \sqrt{(f_{k\tau} - f_{l\tau})(\varepsilon_{l\tau} - \varepsilon_{k\tau})},
\end{aligned} \tag{6}
$$

with $\mathbf{K}$ being the KS matrix of the Hartree and exchange-correlation (xc) kernel ($\Lambda^{\text{hxc}}$),

$$
K_{ij\sigma,kl\tau} = \iint d\mathbf{r} d\mathbf{r}' \psi_{i\sigma} (\mathbf{r}) \psi_{j\sigma} (\mathbf{r}) \Lambda^{\text{hxc}}(\mathbf{r}, \mathbf{r}') \psi_{k\tau}(\mathbf{r}') \psi_{l\tau}(\mathbf{r}'). \tag{7}
$$

The KS orbitals have been assumed to be real for simplicity.

On the other hand, the $d$-matrix formulation gives first-order NAC as

$$
\left\langle \Psi_0 \right| \frac{\partial}{\partial R_{\mu}} \left| \Psi_I \right\rangle = \omega_I^{1/2} \mathbf{d}_{\mu}^{\dagger} \mathbf{S}^{1/2} \mathbf{F}_I, \tag{8}
$$

where

$$
d_{ij\sigma,\mu} = \left\langle \psi_{i\sigma} \right| \hat{d}_{\mu} \left| \psi_{j\sigma} \right\rangle = \left\langle \psi_{i\sigma} \right| \frac{\partial}{\partial R_{\mu}} \left| \psi_{j\sigma} \right\rangle. \tag{9}
$$

The $d$-matrix formulation is derived from the original $h$-matrix formulation, using the relationship between the nuclear derivatives of many-body Hamiltonian and Kohn-Sham Hamiltonian. It can avoid the problem of the pseudopotential approximation in reproducing the inelastic terms corresponding to the off-diagonal $h$-matrix elements.

It is interesting to note that the two TDDFT formulations of first-order NAC, Eqs. (2) and (8), give similar but subtly different expressions for the connection between TDDFT quantities and many-body theory, i.e.,
$$
\mathbf{h}_{\mu}^{\dagger} \mathbf{S}^{-1 / 2} \mathbf{F}_{I}=\omega_{I}^{1 / 2}\left\langle\Psi_{0}\left|\hat{h}_{\mu}\right| \Psi_{I}\right\rangle,
\tag{10}
$$

$$
\mathbf{d}_{\mu}^{\dagger} \mathbf{S}^{1 / 2} \mathbf{F}_{I}=\omega_{I}^{-1 / 2}\left\langle\Psi_{0}\left|\hat{d}_{\mu}\right| \Psi_{I}\right\rangle,
\tag{11}
$$
which can be further compared with the one for the dipole operator $\hat{r}_{\mu}$,
$$
\mathbf{r}_{\mu}^{\dagger} \mathbf{S}^{-1 / 2} \mathbf{F}_{I}=\omega_{I}^{1 / 2}\left\langle\Psi_{0}\left|\hat{r}_{\mu}\right| \Psi_{I}\right\rangle,
\tag{12}
$$
as derived by Casida for the calculation of oscillator strength. $^{15}$ The expression of the $\hat{d}_{\mu}$ operator, Eq. (11), shows a distinct feature as it gives different powers in $\mathbf{S}$ and $\omega_{I}$. It is reminded that Eq. (12) is the basis of the Casida ansatz, in which the auxiliary many-body excited-state wavefunction is constructed as
$$
\bar{\Psi}_{I}=\sum_{i j \sigma}^{f_{i \sigma}>f_{j \sigma}} \sqrt{\frac{\varepsilon_{j \sigma}-\varepsilon_{i \sigma}}{\omega_{I}}} F_{i j \sigma, I} \hat{a}_{j \sigma}^{\dagger} \hat{a}_{i \sigma} \bar{\Psi}_{0},
\tag{13}
$$
so that
$$
\left\langle\Psi_{0}\left|\hat{O}_{\mu}\right| \Psi_{I}\right\rangle=\left\langle\bar{\Psi}_{0}\left|\hat{O}_{\mu}\right| \bar{\Psi}_{I}\right\rangle.
\tag{14}
$$

Herein $\hat{a}_{j \sigma}^{\dagger}$ and $\hat{a}_{i \sigma}$ are, respectively, the creation and annihilation operators, and $\bar{\Psi}_{0}$ is a Slater determinant of occupied KS orbitals. Details regarding the Casida ansatz and the mapping between TDDFT quantities and many-body theory can be found in Ref. 23. Nevertheless, in order to validate Eq. (14) also for $\hat{O}_{\mu}=\hat{d}_{\mu}$, the Casida ansatz need to be adapted according to Eq. (11) in the following way:
$$
\tilde{\Psi}_{I}=\sum_{i j \sigma}^{f_{i \sigma}>f_{j \sigma}} \sqrt{\frac{\omega_{I}}{\varepsilon_{j \sigma}-\varepsilon_{i \sigma}}} F_{i j \sigma, I} \hat{a}_{j \sigma}^{\dagger} \hat{a}_{i \sigma} \tilde{\Psi}_{0},
\tag{15}
$$
where $\tilde{\Psi}_{0}=\bar{\Psi}_{0}$.

With the adapted Casida ansatz in hand, we can now readily derive the second-order NAC, assuming the similarity between first- and second-derivative operators. Defining
$$
\hat{b}_{\mu} \equiv \frac{\partial^{2}}{\partial R_{\mu}^{2}},
\tag{16}
$$
we can get
$$
\left\langle\Psi_{0}\left|\hat{b}_{\mu}\right| \Psi_{I}\right\rangle=\left\langle\tilde{\Psi}_{0}\left|\hat{b}_{\mu}\right| \tilde{\Psi}_{I}\right\rangle
\tag{17}
$$
from the adapted Casida ansatz. Since Eq. (15) is equivalent to
$$
\tilde{\Psi}_{I}=\sum_{i j \sigma}^{f_{i \sigma}>f_{j \sigma}} \omega_{I}^{1 / 2}\left(\mathbf{S}^{1 / 2} \mathbf{F}_{I}\right)_{i j \sigma} \hat{a}_{j \sigma}^{\dagger} \hat{a}_{i \sigma} \tilde{\Psi}_{0},
\tag{18}
$$
further using the connection from the Casida ansatz to the mapping between TDDFT and many-body theory, $^{23}$ we can get
$$
\mathbf{b}_{\mu}^{\dagger} \mathbf{S}^{1 / 2} \mathbf{F}_{I}=\omega_{I}^{-1 / 2}\left\langle\Psi_{0}\left|\hat{b}_{\mu}\right| \Psi_{I}\right\rangle,
\tag{19}
$$
i.e.,
$$
\left\langle\Psi_{0}\left|\frac{\partial^{2}}{\partial R_{\mu}^{2}}\right| \Psi_{I}\right\rangle=\omega_{I}^{1 / 2} \mathbf{b}_{\mu}^{\dagger} \mathbf{S}^{1 / 2} \mathbf{F}_{I}.
\tag{20}
$$

This expression shows that we can calculate second-order NAC without explicitly constructing (auxiliary) excited wavefunctions. Moreover, it is appealing that the computational cost of second-order NAC by this expression is at the same level as that of the first-order. On the other hand, it is noted that although the derivation of Eq. (11) is rigorous, derivation of Eq. (19) is not yet. The validity of the adapted Casida ansatz for the second-order NAC needs to be further justified. Next, we show that this can be achieved within the TDA, where the adapted Casida ansatz becomes equivalent to the original one.

### B. Second-order NAC within the TDA

The justification of the second-order NAC formulation can be attempted by using the expansion of first-order NAC to show the validity of Eq. (17). It has been shown $^{21,22}$ that for those between ground state and singly excited states, it generally holds that
$$
\left\langle\Psi_{0}\left|\hat{d}_{\mu}\right| \Psi_{I}\right\rangle=\left\langle\tilde{\Psi}_{0}\left|\hat{d}_{\mu}\right| \tilde{\Psi}_{I}\right\rangle,
\tag{21}
$$
and for those between singly excited states, the validity of the expression
$$
\left\langle\Psi_{I}\left|\hat{h}_{\mu}\right| \Psi_{J}\right\rangle=\left\langle\bar{\Psi}_{I}\left|\hat{h}_{\mu}\right| \bar{\Psi}_{J}\right\rangle
\tag{22}
$$
can be justified using the TDA, where $\omega_{I}^{1 / 2} \mathbf{S}^{1 / 2}=1$, and the two forms of auxiliary wavefunctions become the same, i.e., $\bar{\Psi}_{I}=\tilde{\Psi}_{I}$. The second-order NAC can be expanded by the first-order as
$$
\begin{aligned}
\left\langle\Psi_{0}\left|\hat{b}_{\mu}\right| \Psi_{I}\right\rangle= & -\left\langle\frac{\partial}{\partial R_{\mu}} \Psi_{0}\left|\frac{\partial}{\partial R_{\mu}} \Psi_{I}\right\rangle+\frac{\partial}{\partial R_{\mu}}\left\langle\Psi_{0}\right| \frac{\partial}{\partial R_{\mu}} \mid \Psi_{I}\right\rangle \\
= & -\sum_{m}\left\langle\frac{\partial}{\partial R_{\mu}} \Psi_{0}\left|\Psi_{m}\right\rangle\left\langle\Psi_{m}\right| \frac{\partial}{\partial R_{\mu}} \Psi_{I}\right\rangle \\
& +\frac{\partial}{\partial R_{\mu}}\left\langle\Psi_{0}\left|\frac{\partial}{\partial R_{\mu}}\right| \Psi_{I}\right\rangle \\
= & \sum_{m}\left\langle\Psi_{0}\left|\hat{d}_{\mu}\right| \Psi_{m}\right\rangle \frac{\left\langle\Psi_{m}\left|\hat{h}_{\mu}\right| \Psi_{I}\right\rangle}{E_{I}-E_{m}} \\
& +\frac{\partial}{\partial R_{\mu}}\left\langle\Psi_{0}\left|\hat{d}_{\mu}\right| \Psi_{I}\right\rangle,
\end{aligned}
\tag{23}
$$
which rigorously holds since $\left\langle\Psi_{m} | \Psi_{n}\right\rangle=\delta_{m n}$. Similarly, if we can show this orthonormalized condition for the auxiliary

wavefunction, i.e., $\langle \tilde{\Psi}_m | \tilde{\Psi}_n \rangle = \delta_{mn}$, we can get

$$
\begin{aligned}
\langle \tilde{\Psi}_0 | \hat{b}_\mu | \tilde{\Psi}_I \rangle =& -\left\langle \frac{\partial}{\partial R_\mu} \tilde{\Psi}_0 \bigg| \frac{\partial}{\partial R_\mu} \tilde{\Psi}_I \right\rangle + \frac{\partial}{\partial R_\mu} \langle \tilde{\Psi}_0 | \frac{\partial}{\partial R_\mu} | \tilde{\Psi}_I \rangle \\
=& -\sum_m \left\langle \frac{\partial}{\partial R_\mu} \tilde{\Psi}_0 \bigg| \tilde{\Psi}_m \right\rangle \left\langle \tilde{\Psi}_m \bigg| \frac{\partial}{\partial R_\mu} \tilde{\Psi}_I \right\rangle \\
& + \frac{\partial}{\partial R_\mu} \langle \tilde{\Psi}_0 | \frac{\partial}{\partial R_\mu} | \tilde{\Psi}_I \rangle \\
=& \sum_m \langle \tilde{\Psi}_0 | \hat{d}_\mu | \tilde{\Psi}_m \rangle \frac{\langle \tilde{\Psi}_m | \hat{h}_\mu | \tilde{\Psi}_I \rangle}{E_I - E_m} \\
& + \frac{\partial}{\partial R_\mu} \langle \tilde{\Psi}_0 | \hat{d}_\mu | \tilde{\Psi}_I \rangle.
\end{aligned}
\tag{24}
$$

From Eqs. (21) and (22), the identity of Eqs. (23) and (24) can be justified provided that $\tilde{\Psi}_I = \tilde{\Psi}_I$, since we have to reconstruct the auxiliary wavefunction from $\tilde{\Psi}_m$ to $\tilde{\Psi}_m$ when the operator is changed from $\hat{d}_\mu$ to $\hat{h}_\mu$. This is satisfied when the TDA is valid. In the meanwhile, the orthonormalized condition that

$$
\begin{aligned}
\delta_{IJ} =& \langle \tilde{\Psi}_I | \tilde{\Psi}_J \rangle = \sqrt{\omega_I \omega_J} \sum_{ij\sigma} \sum_{kl\tau} (\mathbf{S}^{1/2} \mathbf{F}_I)_{ij\sigma}^\dagger (\mathbf{S}^{1/2} \mathbf{F}_J)_{kl\tau} \\
& \times \langle \tilde{\Psi}_0 | \hat{a}_{i\sigma}^\dagger \hat{a}_{j\sigma} \hat{a}_{l\tau}^\dagger \hat{a}_{k\tau} | \tilde{\Psi}_0 \rangle \\
=& \sqrt{\omega_I \omega_J} \sum_{ij\sigma} \sum_{kl\tau} (\mathbf{S}^{1/2} \mathbf{F}_I)_{ij\sigma}^\dagger (\mathbf{S}^{1/2} \mathbf{F}_J)_{kl\tau} \\
& \times \delta_{ik} \delta_{jl} \delta_{\sigma \tau} = \sqrt{\omega_I \omega_J} \mathbf{F}_I^\dagger \mathbf{S} \mathbf{F}_J,
\end{aligned}
\tag{25}
$$

also holds within the TDA since $\mathbf{F}_I^\dagger \mathbf{F}_J = \delta_{IJ}$. Therefore, Eqs. (23) and (24) become identical, i.e., the validity of Eq. (17) is justified within the TDA.

Further remark is on the complete expansion in Eq. (24). As long as we only consider a singly excited state, this does not pose a problem since $\tilde{\Psi}_0$ is a single Slater determinant and only the contributions from other singly excited states enter the expansion.

### C. Extension within TDDFT modified linear response theory: Justification of the Slater transition state method

In the calculation of first-order NAC, a particular example is the case of the Slater transition state method for doublet systems. Billeter and Curioni$^{10}$ have used the following expression:

$$
\langle \Psi_0 | \frac{\partial}{\partial R_\mu} | \Psi_I \rangle = \langle \psi_{i\sigma}^m | \frac{\partial}{\partial R_\mu} | \psi_{j\sigma}^m \rangle,
\tag{26}
$$

where the $(i,j)$ pair is the particle-hole orbitals responsible for the $I$th transition, and $m$ denotes the mid-excited state (Slater transition state) in which the particle-hole orbitals are each filled with a half electron. They have found that this expression can give accurate results of first-order NAC between doublet states of molecules at equilibrium geometries, and their approach is further validated by our TDDFT modified linear response theory$^{34,35}$ and also by our calculations near intersection points.$^{22}$ Next, we will show that the extension of TDDFT formulation of second-order NAC, within modified linear response theory, is also equivalent to the Slater transition state method for doublet systems.

Within modified linear response, the excitation energy is calculated from the response of the mid-excited state, while other terms in the NAC formula are calculated from that of the pure-state configuration.$^{35}$ Corresponding to the mid-excited state of a doublet system, the adapted Casida equation,

$$
\Omega^m \mathbf{F}_I^m = \omega_I^m \mathbf{F}_I^m,
\tag{27}
$$

with the matrix element,

$$
\begin{aligned}
\Omega_{ij\sigma, kl\tau}^m =& \delta_{i,k} \delta_{j,l} \delta_{\sigma, \tau} \left( \epsilon_{j\sigma}^m - \epsilon_{i\sigma}^m \right)^2 + 2 \left( f_{i\sigma}^m - f_{j\sigma}^m \right) \left( \epsilon_{j\sigma}^m - \epsilon_{i\sigma}^m \right) \\
& \times K_{ij\sigma, kl\tau}^m,
\end{aligned}
\tag{28}
$$

gives

$$
\omega_I^m = \epsilon_{j\sigma}^m - \epsilon_{i\sigma}^m,
\tag{29}
$$

since $f_{i\sigma}^m = f_{j\sigma}^m = 0.5$ in the mid-excited state of a doublet system, which renders the corresponding off-diagonal elements of $\Omega$ to be zero. On the other hand, the pure state configuration in the mid-excited state, which uses the occupation number of the ground state while keeping other quantities of the mid-excited state, gives

$$
\mathbf{b}_{\mu,p}^\dagger \mathbf{S}_p^{1/2} \mathbf{F}_I^p = b_{ij\sigma}^m \left( \epsilon_{j\sigma}^m - \epsilon_{i\sigma}^m \right)^{-1/2},
\tag{30}
$$

due to the fact that $F_{ij\sigma,I}^p$ is practically equivalent to 1 and other components of $\mathbf{F}_I$ are zero. Therefore,

$$
\langle \Psi_0 | \hat{b}_\mu | \Psi_I \rangle = \left( \omega_I^m \right)^{1/2} \mathbf{b}_{\mu,p}^\dagger \mathbf{S}_p^{1/2} \mathbf{F}_I^p = b_{ij\sigma}^m \!=\! \langle \psi_{i\sigma}^m | \frac{\partial^2}{\partial R_\mu^2} | \psi_{j\sigma}^m \rangle,
\tag{31}
$$

which is just the second-derivative coupling matrix element between the particle-hole orbitals. As a result, the TDDFT formulation of second-order NAC in doublet systems is just reduced to the Slater transition state method.

## III. IMPLEMENTATION AND COMPUTATIONAL DETAILS

The implementation of the present TDDFT method for second-order NAC is based on the ABINIT code,$^{41}$ which is a planewave pseudopotential approach. All calculations are performed within adiabatic local spin density approximation (LSDA) using the Teter Pade parametrization.$^{42}$ The Troullier-Martins pseudopotentials$^{43}$ with nonlinear core correction,$^{44}$ generated by Khein and Allan, are used for various atomic species. Only the $\Gamma$ point $(k=0)$ is taken into consideration in the $\mathbf{k}$ point sampling, which corresponds to the use of real wavefunctions. Convergence parameters, such as the supercell size, number of unoccupied orbitals, and kinetic energy cutoff, are examined to ensure reasonably accurate results. On the basis of the previous implementation of modified linear response theory in ABINIT,$^{35}$ its extension for calculating second-order NAC requires almost no additional labor, since it is only necessary to construct the pure-state configuration from the mid-excited state, and to apply the same calculation procedures as ordinary linear response theory. To check the performance of our method, it is desired to compare

TDDFT results for general atomic geometries with those from wavefunction-based methods; however, there are too few lit- eratures on this aspect and the direct comparison is difficult. Therefore, we concentrate on evaluating second-order NAC in the immediate vicinity of Jahn-Teller, Renner-Teller, and elliptic Jahn-Teller intersections, where we can directly com- pare our results with predictions from corresponding models.

$$
\left\langle\psi_{i \sigma}\left|\hat{b}_{\mu}\right| \psi_{j \sigma}\right\rangle=\frac{\left\langle\psi_{i \sigma}(\mathbf{R}) \mid \psi_{j \sigma}\left(\mathbf{R}+\Delta R \cdot \mathbf{e}_{\mu}\right) \operatorname{sgn}\left(\xi_{+}\right)-2 \psi_{j \sigma}(\mathbf{R})+\psi_{j \sigma}\left(\mathbf{R}-\Delta R \cdot \mathbf{e}_{\mu}\right) \operatorname{sgn}\left(\xi_{-}\right)\right\rangle}{\Delta R},
\tag{32}
$$

where $\mathbf{e}_{\mu}$ is the unit vector along the $\mu$ axis, $\operatorname{sgn}(\xi)$ is the sign function, i.e.,

$$
\operatorname{sgn}(\xi)=
\begin{cases}
-1 & \text{if } \xi < 0 \\
1 & \text{if } \xi > 0
\end{cases},
\tag{33}
$$

$$
\xi_{+}=\left\langle\psi_{j \sigma}(\mathbf{R}) \mid \psi_{j \sigma}\left(\mathbf{R}+\Delta R \cdot \mathbf{e}_{\mu}\right)\right\rangle,
\tag{34}
$$

$$
\xi_{-}=\left\langle\psi_{j \sigma}(\mathbf{R}) \mid \psi_{j \sigma}\left(\mathbf{R}-\Delta R \cdot \mathbf{e}_{\mu}\right)\right\rangle.
\tag{35}
$$

The accuracy of the above numerical differentiation scheme is checked by using different $\Delta R$. In practice, we choose $\Delta R$ $= 0.002 - 0.004$ bohr.

## IV. RESULTS AND DISCUSSIONS

In this section, we present calculation results on vari- ous molecular systems possessing Jahn-Teller, Renner-Teller, or elliptic Jahn-Teller intersections, where the ground state and the first excited state of these molecular systems are degenerate.

TABLE I. The calculated $x$, $y$, and $z$ components of second-order NAC (in bohr $^{-2}$) on three atoms of $H_3$ and $Li_3$, which are located in the geometry of Fig. 1. The contour radius $q$ is 0.02 bohr and angle $\theta$ is 0. The ideal val- ues from the Jahn-Teller model, as derived in Appendix A and summarized in Table V, are also listed for comparison. It is noted that the $z$ components of second-order NAC in the Jahn-Teller model are dependent on atomic dis- tances and have been derived within two sets of parameters: the values inside the parenthesis are derived by $r_{Li-Li}=5.0$ bohrs, while the others outside are derived by $r_{H-H}=1.9729$ bohrs.

|         |         | $x$       | $y$        | $z$          |
|---------|---------|-----------|------------|--------------|
| $H_3$   | Atom 1  | 1085.88   | $-1074.36$ | 12.75        |
|         | Atom 2  | 0.30      | 0.00       | 0.00         |
|         | Atom 3  | $-1085.30$| 1073.36    | $-12.68$     |
| $Li_3$  | Atom 1  | 1102.08   | $-1090.50$ | 4.37         |
|         | Atom 2  | 1.44      | 0.00       | 0.00         |
|         | Atom 3  | $-1099.12$| 1086.05    | $-4.71$      |
| Model   | Atom 1  | 1082.53   | $-1082.53$ | $12.67\ (5.0)$|
|         | Atom 2  | 0.00      | 0.00       | $0.0\ (0.0)$ |
|         | Atom 3  | $-1082.53$| 1082.53    | $-12.67\ (-5.0)$ |

## A. Finite difference method of calculating b-matrix elements

The calculation of $b$-matrix elements is implemented in a straightforward finite-difference scheme, with the consid- eration of aligning the phases of KS orbitals, $^{10}$ as shown by

## A. Jahn-Teller systems

In Table I, we list the $x$, $y$, and $z$ components of second- order NAC in two typical Jahn-Teller systems: The proto- type $H_3$ molecule $^{45-47}$ and an alkali-metal trimer $Li_3$. $^{48,49}$ The three atoms are located in the geometry of Fig. 1 in which one atom is moved on the circular contour around the intersection point. The contour radius $q$ is chosen as 0.02 bohr, which is sufficiently small so as to be comparable to the condition of the Jahn-Teller model. It is clearly seen that at such a small $q$, the $x$ and $y$ components of second-order NAC in $H_3$ and $Li_3$ are significantly large: The nonzero values are in the order of 1000 bohr $^{-2}$, which are much larger than those of the first- order NAC (which are in the order of $1/q$). In the meanwhile, both the magnitude and relative signs of TDDFT results are in good agreement with the Jahn-Teller model. (The ideal values of second-order NAC from the Jahn-Teller model can be de- rived from the derivatives of the first-order NAC, as shown by Appendix A.) On the other hand, it is noted that the $z$ com- ponents of second-order NAC are quite small but nonzero, either in $H_3$ or $Li_3$. This is different from the zero values of $z$ components of the first-order NAC in $X_3$ systems near inter- section points. The Jahn-Teller model predicts that the $x$ and $y$ components of second-order NAC only depend on contour radius $q$ and angle $\theta$, while there is an additional dependence

![](./images/811634985940287488_3.jpg)

FIG. 1. The geometry of the $X_3$ system as one X atom (numbered as 2) is moved on the contour around the intersection point (located at $O$). The nuclear configuration at the intersection point is an equilateral triangle with $D_{3h}$ symmetry, corresponding to the degeneracy of the ground state and the first excited state.

![](./images/811634985940287488_4.jpg)

FIG. 2. The z components of second-order NAC on the three atoms of $H_3$. The labels 1z, 2z, and 3z denote the z components on atoms 1, 2, and 3, while 1z_JT, 2z_JT, and 3z_JT denote those from the Jahn-Teller model, respectively.

of z component on the internuclear distance $r$. In our calculations, we set $r_{\text{H--H}} = 1.9729$ bohrs and $r_{\text{Li--Li}} = 5.0$ bohrs, respectively; therefore, TDDFT calculations are expected to give different z components for $H_3$ and $Li_3$, and the results seem to give such a difference: Both the magnitude and sign agree with the ideal values corresponding to the above internuclear distances. However, since the z components are quite small we need to make sure whether they are intrinsically nonzero. For this purpose, we have made a detailed examination of the z components of second-order NAC on the three atoms of $H_3$ as a function of the contour angle $\theta$, as shown by Fig. 2. As $\theta$ is varied from $0^\circ$ to $180^\circ$, the z components on all atoms, although small, show clear dependencies on $\theta$ and agree well with the Jahn-Teller model. This means that the small z components of second-order NAC are intrinsically nonzero and have been accurately reproduced by TDDFT.

Another noteworthy point in Table I is the sum of x, y, and z components. In contrary to the vector form of first-order NACs, second-order NACs are scalars due to the presence of the scalar Laplacian; therefore, only the sum of x, y, and z components are meaningful in the nonadiabatic dynamics simulation. Table I shows the sum of the components in both $H_3$ and $Li_3$ are small, as predicted by the Jahn-Teller model. This can provide the background for the neglect of second-order NAC in practical simulations. $^{7,32,33}$

### B. Renner-Teller systems

In Table II, we list the x, y, and z components of second-order NAC in several typical Renner-Teller systems: The $BH_2$, $CH_2^+$, $NH_2$, and $H_2O^+$ molecules, $^{50,51}$ which are located in the geometry of Fig. 3 with the contour angle $\theta = 0$. The contour radius $q$ is chosen as 0.1 bohr, which is known to be sufficiently small and can be comparable to the condition of the Renner-Teller model. The internuclear distances are set as $r_{\text{H--B}} = 2.0$ bohrs, $r_{\text{H--C}} = 2.0$ bohrs, $r_{\text{H--N}} = 1.95$ bohrs, and $r_{\text{H--O}} = 1.85$ bohrs. It is interesting to see that all components of second-order NAC on three atoms of all molecules are negligibly small (reminding that the first-order NAC in Renner-Teller systems are in the order of $1/q$) and agree with the Renner-Teller model. (The ideal values of second-order NAC from the Renner-Teller model can be derived from the derivatives of the first-order NAC, as shown by Appendix B.) As a matter of fact, NAC of Renner-Teller system are not dependent on the contour angle $\theta$, and thus the negligibly small values of second-order NAC in demonstrated systems are not accidental results for a specified geometry, but indicate that they are intrinsically zero. In connection with the nonadiabatic dynamics simulation, it is thus verified that the sum of x, y, and z components can be regarded as zero in Renner-Teller systems. This also provides a background for the neglect of second-order NAC in practical dynamics simulations. $^{7,32,33}$

<table>
<caption>TABLE II. The calculated x, y, and z components of second-order NAC (in bohr$^{-2}$) on three atoms of $BH_2$, $CH_2^+$, $NH_2$, and $H_2O^+$, which are located in the geometry of Fig. 3. The contour radius $q$ is 0.1 bohr and the angle $\theta$ is 0. The ideal values from the Renner-Teller model, as derived in Appendix B, are also listed for comparison.</caption>
<thead>
  <tr>
    <th></th>
    <th></th>
    <th>x</th>
    <th>y</th>
    <th>z</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$BH_2$</td>
    <td>Atom $H_{(1)}$</td>
    <td>0.015</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom B</td>
    <td>0.016</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom $H_{(2)}$</td>
    <td>0.015</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>$CH_2^+$</td>
    <td>Atom $H_{(1)}$</td>
    <td>$-0.012$</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom C</td>
    <td>0.013</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom $H_{(2)}$</td>
    <td>$-0.012$</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>$NH_2$</td>
    <td>Atom $H_{(1)}$</td>
    <td>0.018</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom N</td>
    <td>0.018</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom $H_{(2)}$</td>
    <td>0.018</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>$H_2O^+$</td>
    <td>Atom $H_{(1)}$</td>
    <td>$-0.0035$</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom O</td>
    <td>0.021</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom $H_{(2)}$</td>
    <td>0.0014</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>Model</td>
    <td>Atom 1</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom 2</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td></td>
    <td>Atom 3</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
</tbody>
</table>

### C. Elliptic Jahn-Teller system

In Table III, we list TDDFT calculation results of the x, y, and z components of the second-order NAC on the three atoms of $NaH_2$, which is known as an elliptic Jahn-Teller system. $^{40,52}$ The three atoms are located in the geometry of Fig. 4 with the contour angle $\theta = 60^\circ$. Other parameters regarding the geometry are $r = 2.18$ bohrs and $R = 3.6127$ bohrs, according to the intersection point determined in our previous work. $^{14}$ For an elliptic Jahn-Teller

![](./images/811634985940287488_5.jpg)

FIG. 3. Geometry of the $XH_2$ or $XH_2^+$ system when the X atom is moved on the contour around the Renner-Teller intersection point (indicated by the open square) on the collinear axis. The contour, with radius $q$ and angle $\theta$, is fixed in the $xy$ plane, which is perpendicular to the HH axis. The two hydrogen atoms are set to be symmetric to the plane.

<table>
<caption>TABLE III. Calculated values of $x$, $y$, and $z$ components of second-order NAC (in bohr$^{-2}$) on the three atoms of NaH$_2$, which are located in the geometry shown by Fig. 4 with the contour radius $q = 0.1$ bohr and angle $\theta = 60^\circ$.</caption>
<thead>
<tr>
<th>
</th>
<th>
$x$
</th>
<th>
$y$
</th>
<th>
$z$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
Atom Na
</td>
<td>
20.54
</td>
<td>
$-$110.13
</td>
<td>
1.23
</td>
</tr>
<tr>
<td>
Atom H$_{(1)}$
</td>
<td>
$-$542.53
</td>
<td>
$-$10.94
</td>
<td>
$-$2.89
</td>
</tr>
<tr>
<td>
Atom H$_{(2)}$
</td>
<td>
$-$618.23
</td>
<td>
51.59
</td>
<td>
$-$5.42
</td>
</tr>
</tbody>
</table>

systems, the angular NAC, $A_\theta$, is not just in a quantized value of 0.5, but shows a strong dependence on the contour angle $\theta$. Using the similar procedures in Appendix A but setting $A_\theta$ as a variable rather than a constant of 0.5, we can easily get the conclusion that second-order NAC would depend on $\partial A_\theta/\partial\theta$, i.e., the slope of angular NAC with respect to $\theta$. Therefore, we set $\theta$ as $60^\circ$ at which $\partial A_\theta/\partial\theta$ is relatively large, as revealed by our previous work.$^{14}$ It is clearly seen that under such a condition the magnitudes of $x$ and $y$ components become unbalanced in comparison with the Jahn-Teller systems. Meanwhile, the $z$ components are still relatively small. Therefore, the sum of $x$, $y$, and $z$ components of second-order NAC cannot be negligibly small. Regarding the role of NAC in the nonadiabatic dynamics simulation, it is thus suggested to include second-order NAC in the rigorous simulation of general molecular systems, which might possess accidental conical intersections without any symmetry requirements as in Jahn-Teller systems.

## V. CONCLUSION

We have proposed an efficient TDDFT method for calculating second-order NAC between ground state and singly excited states, which is based on the Casida ansatz adapted for first-order NAC, while the calculation procedure can be done without the need of explicitly constructing auxiliary excited-state wavefunctions. Our formulation can be justified when the TDA is valid. Within the modified linear response theory, the TDDFT formulation is reduced to the Slater transition method in doublet systems. Test calculations are carried out in the immediate vicinity of various types of intersection points. The results are in good agreement with the ideal values derived from Jahn-Teller or Renner-Teller models. Contrary to the diverging behavior of first-order NAC near intersections, the Cartesian components of second-order NAC are shown to be negligibly small near Renner-Teller intersections, while they are significantly large near Jahn-Teller intersections. Nevertheless, the Cartesian components of second-order NAC can cancel each other to a large extent in Jahn-Teller systems, showing the background of neglecting second-order NAC in nonadiabatic dynamics simulations. On the other hand, it is revealed that such a cancellation becomes less effective in an elliptic Jahn-Teller system and thus the role of second-order NAC needs to be evaluated in the rigorous framework. Finally, it is noted that the performance of TDDFT on the computation of second-order NAC needs to be further validated, particularly for a general atomic geometry, which requires reference data and remains future work.

![](./images/811634985940287488_6.jpg)

FIG. 4. The geometry of the NaH$_2$ system as the Na atom is moved on the contour around the conical intersection point (indicated by the open square). The nuclear configuration at the conical intersection point is an isosceles triangle with C$_{2v}$ symmetry.

## ACKNOWLEDGMENTS

The authors thank Dr. Yoshitaka Tateyama, Mr. Jun Haruyama, and Mr. Yohei Iwami for fruitful discussions. This work was supported in part by the Project of Materials Design through Computics: Complex Correlation and Non-Equilibrium Dynamics, a Grant in Aid for Scientific Research on Innovative Areas, and the Next Generation Super Computing Project, Nanoscience Program, MEXT, Japan. C.H. thanks the support by State Key Laboratory of New Ceramic and Fine Processing, Tsinghua University. K.W. acknowledges partial financial support from MEXT through a Grant-in-Aid (Grant Nos. 19540411 and 22104007). Testing of our program has been performed on the supercomputers of Institute for Solid State Physics, University of Tokyo.

## APPENDIX A: SECOND-ORDER NAC FROM THE JAHN-TELLER MODEL

The Jahn-Teller model describes a class of systems in which a set of nuclear coordinates are coupled to a two-level system consisting of the ground state and the first excited state of appropriate symmetry.$^{53}$ Figure 5 shows an arbitrary configuration of a Jahn-Teller trimer. When the contour radius $q$ is sufficiently small, the angular NAC has a quantized value of 1/2 according to the Jahn-Teller model.$^{53}$ All components of first-order NAC on the three atoms can thus be uniquely determined, as shown by Table IV.

To derive the $x$ component of second-order NAC on atom 2, we move atom 2 in the $x$ direction with a small displacement $\Delta$, as shown by Fig. 6. Since the Jahn-Teller model is a two-level system, we can get

$$
\langle \Psi_0 | \frac{\partial^2}{\partial x_2^2} | \Psi_1 \rangle = \frac{\partial}{\partial x_2} \langle \Psi_0 | \frac{\partial}{\partial x_2} | \Psi_1 \rangle = \frac{A_{x_2}^\text{disp} - A_{x_2}}{\Delta}, \tag{A1}
$$

where $A_{x_2}$ is the $x$ component of first-order NAC before the displacement, as listed in Table IV. The new $x$ component of first-order NAC on atom 2 after the displacement, $A_{x_2}^\text{disp}$, can be determined from the new geometry as

$$
A_{x_2}^\text{disp} = \frac{0.5}{q'} \cos \theta', \tag{A2}
$$

![](./images/811634985940287488_7.jpg)

FIG. 5. Configuration of a Jahn-Teller trimer in the xy plane, in which atom 2 is regarded on a contour with radius q and angle $\theta$ around the intersection point (vertex D of the equilateral triangle). Arrows represent NAC vectors on the three atoms.

where
$$
q' = \sqrt{q^2 \cos^2 \theta + (q \sin \theta - \Delta)^2}, \tag{A3}
$$

$$
\theta' = \arccos \left( \frac{q \cos \theta}{q'} \right). \tag{A4}
$$

By taking $\Delta \to 0$ in Eq. (A1), we can get
$$
\begin{aligned}
\langle \Psi_0 | \frac{\partial^2}{\partial x_2^2} | \Psi_1 \rangle &= \lim_{\Delta \to 0} \frac{1}{\Delta} \left( \frac{0.5}{q'} \cos \theta' - \frac{0.5}{q} \cos \theta \right) \\
&= \frac{0.5}{q^2} \sin 2\theta. \tag{A5}
\end{aligned}
$$

The derivation of the $y$ component of second-order NAC on atom 2 is similar to that of the $x$ component in the above; thus, the detail is not shown here. Next, to derive the $z$ component, we move atom 2 in the $z$ direction as shown by Fig. 7, and then we can get
$$
\langle \Psi_0 | \frac{\partial^2}{\partial z_2^2} | \Psi_1 \rangle = \frac{\partial}{\partial z_2} \langle \Psi_0 | \frac{\partial}{\partial z_2} | \Psi_1 \rangle = \frac{A_{z_2}^{\text{disp}}}{\Delta}, \tag{A6}
$$
which uses the fact that the $z$ component of first-order NAC on atom 2 before the displacement is zero. The new geometry after the displacement gives
$$
A_{z_2}^{\text{disp}} = \frac{0.5}{q'} \cos \alpha = \frac{0.5}{q'} \cos \alpha_1 \cos \alpha_2, \tag{A7}
$$
where $q'$ is the new contour radius around the vertex of the equilateral triangle in the new atomic plane. $\alpha$ is the angle between the new NAC vector and the $z$ axis, $\alpha_1$ is the angle between the new atomic plane and the $z$ axis, and $\alpha_2$ is the angle between the new NAC vector and the projection of the $z$ axis in the new atomic plane. Using the geometric relationships shown by Fig. 7, we can get
$$
q' = \sqrt{r_3^2 + r^2 - 2r_3 r \cos \left[ \arccos \left( \frac{r_3^2 + r^2 - r_4^2}{2r_3 r} \right) - 60^\circ \right]}, \tag{A8}
$$

$$
\alpha_1 = \arcsin \left( \frac{h_1}{h_2} \right), \tag{A9}
$$

$$
\alpha_2 = 90^\circ - \arccos \left( \frac{q'^2 + r_4^2 - r^2}{2q' r_4} \right) - \arccos \left( \frac{h_2}{r_4} \right). \tag{A10}
$$

The auxiliary quantities in the above equations are calculated as
$$
r_3 = \sqrt{r_1^2 + \Delta^2}, r_4 = \sqrt{r_2^2 + \Delta^2},
$$

$$
h_1 = \frac{\sqrt{3}}{2} r + q \cos \theta, h_2 = \sqrt{h_1^2 + \Delta^2},
$$

$$
r_1 = \sqrt{r^2 + q^2 - 2qr \cos(150^\circ - \theta)},
$$

$$
r_2 = \sqrt{r^2 + q^2 - 2qr \cos(210^\circ - \theta)}.
$$

By taking $\Delta \to 0$, we can get $r_3 \to r_1$, $r_4 \to r_2$, $h_2 \to h_1$, $q' \to q$, and $\alpha_2 \to 90^\circ - \theta$. Then, Eq. (A6) is reduced to
$$
\begin{aligned}
\langle \Psi_0 | \frac{\partial^2}{\partial z_2^2} | \Psi_1 \rangle &= \lim_{\Delta \to 0} \frac{1}{\Delta} \frac{0.5}{q} \cos \left[ \arcsin \left( \frac{h_1}{h_2} \right) \right] \cos(90^\circ - \theta) \\
&= \frac{0.5}{q} \frac{1}{\sqrt{3}r/2} \sin \theta, \tag{A11}
\end{aligned}
$$
where we have used the fact that $r \gg q$.

To derive components of second-order NAC on atoms 1 and 3, we need not make displacements but can merely use

![](./images/811634985940287488_8.jpg)

FIG. 6. Schematic view of the derivation process of the $x$ component of second-order NAC on atom 2. A small displacement $\Delta$ is made in the $x$ direction for atom 2. After displacement, the contour radius is changed from $q$ to $q'$, and the contour angle is changed from $\theta$ to $\theta'$. The arrow denotes the new NAC vector on atom 2.

<table>
<caption>TABLE IV. The $x$, $y$, and $z$ components of first-order NAC on the three atoms of a Jahn-Teller trimer, which are located in the geometry shown by Fig. 5. $q$ is the contour radius and $\theta$ is the contour angle.</caption>
<thead>
<tr>
<th></th>
<th>$x$</th>
<th>$y$</th>
<th>$z$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Atom 1</td>
<td>$\frac{0.5}{q} \cos(120^\circ - \theta)$</td>
<td>$-\frac{0.5}{q} \sin(120^\circ - \theta)$</td>
<td>0</td>
</tr>
<tr>
<td>Atom 2</td>
<td>$\frac{0.5}{q} \cos \theta$</td>
<td>$\frac{0.5}{q} \sin \theta$</td>
<td>0</td>
</tr>
<tr>
<td>Atom 3</td>
<td>$-\frac{0.5}{q} \cos(60^\circ - \theta)$</td>
<td>$\frac{0.5}{q} \sin(60^\circ - \theta)$</td>
<td>0</td>
</tr>
</tbody>
</table>

![](./images/811634985940287488_9.jpg)

FIG. 7. Schematic view of the derivation process of the $z$ component of second-order NAC on atom 2. After a small displacement $\Delta$ is made in the $z$ direction for atom 2, the contour radius is changed from $q$ to $q'$, and the NAC vector (denoted by the arrow ending on atom 2) is located in the new atomic plane.

the fact that the three atoms are equivalent, i.e., not only atom 2 can be regarded as rotating in a contour around the intersection point, other two atoms can also be taken into such a view. In Fig. 8, where atomic geometry is the same as in Fig. 5, atom 1 is regarded as rotating around the intersection point A with contour radius $q$ and angle $\theta_0$. Here, A is the vertex of a new equilateral triangle with side length $r_0$. The geometric analysis gives

$$
r_0 = \sqrt{q^2 + r^2 - 2qr \cos(210^\circ - \theta)}, \tag{A12}
$$

$$
\begin{aligned}
\theta_0 &= 150^\circ + \arccos\left( \frac{q^2 + r_0^2 - r^2}{2qr_0} \right) \\
&= 150^\circ + \arccos\left[ \frac{q - r \cos(210^\circ - \theta)}{r} \right]. \tag{A13}
\end{aligned}
$$

Using the fact that $r \gg q$, we can easily get $r_0 = r$ and $\theta_0 = 120^\circ + \theta$. Replacing $r$ and $\theta$ in the expression of second-order NAC components on atom 2 with $r_0$ and $\theta_0$, we can immediately get the results for atom 1.

![](./images/811634985940287488_10.jpg)

FIG. 8. Schematic view of the derivation process of second-order NAC components on atom 1, which is regarded as rotating around vertex A of a new equilateral triangle with side length $r_0$. The corresponding contour radius and angle is $q$ and $\theta_0$, respectively.

<table>
<caption>TABLE V. The $x$, $y$, and $z$ components of second-order NAC on the three atoms of a Jahn-Teller trimer, which are located in the geometry shown by Fig. 5. $q$ is the contour radius and $\theta$ is the contour angle.</caption>
<thead>
<tr>
<th></th>
<th>$x$</th>
<th>$y$</th>
<th>$z$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Atom 1</td>
<td>$\frac{0.5}{q^2} \cos(30^\circ + 2\theta)$</td>
<td>$-\frac{0.5}{q^2} \cos(30^\circ + 2\theta)$</td>
<td>$\frac{0.5}{q} \frac{1}{\sqrt{3}r/2} \sin(\theta + 120^\circ)$</td>
</tr>
<tr>
<td>Atom 2</td>
<td>$\frac{0.5}{q^2} \sin 2\theta$</td>
<td>$-\frac{0.5}{q^2} \sin 2\theta$</td>
<td>$\frac{0.5}{q} \frac{1}{\sqrt{3}r/2} \sin \theta$</td>
</tr>
<tr>
<td>Atom 3</td>
<td>$-\frac{0.5}{q^2} \sin(120^\circ - 2\theta)$</td>
<td>$\frac{0.5}{q^2} \sin(120^\circ - 2\theta)$</td>
<td>$\frac{0.5}{q} \frac{1}{\sqrt{3}r/2} \sin(\theta - 120^\circ)$</td>
</tr>
</tbody>
</table>

The results for atom 3 can be derived in a way similar to that for atom 1. The final results of second-order NAC components on all atoms are listed in Table V.

## APPENDIX B: SECOND-ORDER NAC FROM THE RENNER-TELLER MODEL

Figure 9 shows an arbitrary configuration of an $\text{XY}_2$ Renner-Teller system, where the X atom is moved with a sufficiently small displacement $q$ from the $z$ axis, which is the seam of Renner-Teller intersections. According to the Renner-Teller model, $^{53}$ the angular NAC has a quantized value of 1.0 and all components of first-order NAC on three atoms can be determined, as shown by Table VI. Note that all $y$ and $z$ components are equal to zero, meaning that the NAC vectors are parallel to the $x$ axis.

Because the first-order NAC vectors are perpendicular to the $yz$ plane, small movement of atoms in the $yz$ plane will not alter the direction of NAC vectors and the $y$ and $z$ components of first-order NAC are kept to be zero after the displacement. Therefore, we can immediately conclude that $y$ and $z$ components of second-order NAC on all atoms are zero.

To derive the $x$ component of second-order NAC on atom 2, we move atom 2 in the $x$ direction, as shown by Fig. 10(a). Since the Renner-Teller model is a two-level system, we can get

$$
\langle \Psi_0 | \frac{\partial^2}{\partial x_2^2} | \Psi_1 \rangle = \frac{\partial}{\partial x_2} \langle \Psi_0 | \frac{\partial}{\partial x_2} | \Psi_1 \rangle = \frac{A_{x_2}^{\text{disp}} - A_{x_2}}{\Delta}, \tag{B1}
$$

where

$$
A_{x_2} = \frac{1}{q}. \tag{B2}
$$

The new geometry after the displacement gives

$$
A_{x_2}^{\text{disp}} = \frac{1}{q'} \cos \theta, \tag{B3}
$$

![](./images/811634985940287488_11.jpg)

FIG. 9. Configuration of an $\text{XY}_2$ Renner-Teller system in the $yz$ plane. The three atoms are located in a geometry slightly distorted from the linear geometry, and atom 2 is regarded on a contour around the $z$ axis with contour radius $q$.

TABLE VI. The $x$, $y$, and $z$ components of first-order NAC on the three atoms of an $XY_2$ Renner-Teller system, which is located in the geometry shown by Fig. 9. $q$ is the contour radius, while $r_1$ ($r_2$) is the distance of atom 1 (atom 3) from the intersection point.

<table>
  <thead>
    <tr>
      <th></th>
      <th>$x$</th>
      <th>$y$</th>
      <th>$z$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Atom 1</td>
      <td>$-\frac{1}{q}\frac{r_2}{r_1+r_2}$</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Atom 2</td>
      <td>$\frac{1}{q}$</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Atom 3</td>
      <td>$-\frac{1}{q}\frac{r_1}{r_1+r_2}$</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

where $q' = \sqrt{q^2 + \Delta^2}$ and $\theta = \arccos(q/q')$. By taking $\Delta \to$ 0 in Eq. (B1), we can get

$$
\langle \Psi_0 | \frac{\partial^2}{\partial x_2^2} | \Psi_1 \rangle = \lim_{\Delta \to 0} \frac{1}{\Delta} \left[ \frac{-\Delta^2}{(q^2 + \Delta^2)q} \right] = 0. \tag{B4}
$$

In a similar way, the $x$ component of second-order NAC on atom 1 can be derived by displacing atom 1 in the $x$ direction, shown by Fig. 10(b), as

$$
\langle \Psi_0 | \frac{\partial^2}{\partial x_1^2} | \Psi_1 \rangle = \frac{\partial}{\partial x_1} \langle \Psi_0 | \frac{\partial}{\partial x_1} | \Psi_1 \rangle = \frac{A_{x_1}^{\mathrm{disp}} - A_{x_1}}{\Delta}, \tag{B5}
$$

where

$$
A_{x_1} = -\frac{1}{q} \frac{r_2}{r_1 + r_2}, \tag{B6}
$$

$$
A_{x_1}^{\mathrm{disp}} = -\frac{1}{q'} \frac{r_2'}{r_1' + r_2'} \cos \theta, \tag{B7}
$$

$$
q' = \sqrt{q^2 + (r_2 - r_2')^2}, \tag{B8}
$$

$$
\theta = \arccos(q/q'), \tag{B9}
$$

$$
r_2' = r_2 \cdot \frac{r_1 + r_2}{r_1' + r_2'} = r_2 \cdot \frac{r_1 + r_2}{\sqrt{(r_1 + r_2)^2 + \Delta^2}}. \tag{B10}
$$

![](./images/811634985940287488_12.jpg)

FIG. 10. Schematic view of the derivation process of the $x$ component of second-order NAC on (a) atom 2 and (b) atom 1. A small displacement $\Delta$ is made in the $x$ direction for atom 2 in (a) and atom 1 in (b). After displacement the contour radius is changed from $q$ to $q'$. Note that in (b) the intersection point is changed from O to $O'$.

Taking $\Delta \to 0$ in Eq. (B5), we can get

$$
\begin{aligned}
\langle \Psi_0 | \frac{\partial^2}{\partial x_1^2} | \Psi_1 \rangle &= \lim_{\Delta \to 0} \frac{1}{\Delta} \\
&\times \frac{q^2 r_2 \Delta^2 + r_2^3 \Delta^2}{\left[ q^2 \Delta^2 + q^2(r_1 + r_2)^2 + r_2^2 \Delta^2 \right] q(r_1 + r_2)} = 0.
\tag{B11}
\end{aligned}
$$

Finally, since the derivation of $x$ component of second-order NAC on atom 3 is essentially equivalent to that of atom 1, the result for atom 3 is also 0.

In one word, all components of second-order NAC on the three atoms of the Renner-Teller system are equal to zero.

$^1$D. R. Yarkony, Rev. Mod. Phys. 68, 985 (1996).
$^2$H. Nakamura, Nonadiabatic Transitions: Concepts, Basic Theories, and Applications (World Scientific, Singapore, 2002).
$^3$M. Baer, Beyond Born-Oppenheimer: Electronic Nonadiabatic Coupling Terms and Conical Intersections (Wiley, Hoboken, NJ, 2006).
$^4$N. L. Doltsinis and D. Marx, Phys. Rev. Lett. 88, 166402 (2002).
$^5$X. Li, J. C. Tully, H. B. Schlegel, and M. J. Frisch, J. Chem. Phys. 123, 084106 (2005).
$^6$C. M. Isborn, X. Li, and J. C. Tully, J. Chem. Phys. 126, 134307 (2007).
$^7$T. D. Martínez, Chem. Phys. Lett. 272, 139 (1997).
$^8$T. Yonehara and K. Takatsuka, J. Chem. Phys. 128, 154104 (2008).
$^9$T. Yonehara and K. Takatsuka, J. Chem. Phys. 129, 134109 (2008).
$^{10}$S. R. Billeter and A. Curioni, J. Chem. Phys. 122, 034105 (2005).
$^{11}$V. Chernyak and S. Mukamel, J. Chem. Phys. 112, 3572 (2000).
$^{12}$R. Baer, Chem. Phys. Lett. 364, 75 (2002).
$^{13}$C. Hu, H. Hirai, and O. Sugino, J. Chem. Phys. 127, 064103 (2007).
$^{14}$C. Hu, H. Hirai, and O. Sugino, J. Chem. Phys. 128, 154111 (2008).
$^{15}$M. E. Casida, in Recent Advances in Density Functional Methods, Part I, edited by D. P. Chong (World Scientific, Singapore, 1995), p. 155.
$^{16}$C. Jamorski, M. E. Casida, and D. R. Salahub, J. Chem. Phys. 104, 5134 (1996).
$^{17}$C. Hu, O. Sugino, and Y. Tateyama, J. Chem. Phys. 131, 114101 (2009).
$^{18}$R. Send and F. Furche, J. Chem. Phys. 132, 044107 (2010).
$^{19}$E. Tapavicza, I. Tavernelli, and U. Rothlisberger, Phys. Rev. Lett. 98, 023001 (2007).
$^{20}$I. Tavernelli, E. Tapavicza, and U. Rothlisberger, J. Chem. Phys. 130, 124107 (2009).
$^{21}$I. Tavernelli, B. F. E. Curchod, A. Laktionov, and U. Rothlisberger, J. Chem. Phys. 133, 194104 (2010).
$^{22}$C. Hu, O. Sugino, H. Hirai, and Y. Tateyama, Phys. Rev. A 82, 062508 (2010).
$^{23}$I. Tavernelli, B. F. E. Curchod, and U. Rothlisberger, J. Chem. Phys. 131, 196101 (2009).
$^{24}$I. Tavernelli, B. F. E. Curchod, and U. Rothlisberger, Phys. Rev. A 81, 052508 (2010).
$^{25}$E. Tapavicza, I. Tavernelli, U. Rothlisberger, C. Filippi, and M. E. Casida, J. Chem. Phys. 129, 124108 (2008).
$^{26}$U. Werner, R. Mitrić, T. Suzuki, and V. Bonačić-Koutecký, Chem. Phys. 349, 319 (2008).
$^{27}$H. Hirai and O. Sugino, Phys. Chem. Chem. Phys. 11, 4570 (2009).
$^{28}$L. T. Redmon, Phys. Rev. A 25, 2453 (1982).
$^{29}$B. H. LengsfieldIII and D. R. Yarkony, J. Chem. Phys. 84, 348 (1986).
$^{30}$H. Ågren, A. Flores-Riveros, and H. J. A. Jensen, Phys. Rev. A 34, 4606 (1986).
$^{31}$M. Santer, U. Manthe, and G. Stock, J. Chem. Phys. 114, 2001 (2001).
$^{32}$T. J. Martínez, M. Ben-Nun, and R. D. Levine, J. Phys. Chem. A 101, 6389 (1997).
$^{33}$M. Ben-Nun and T. J. Martínez, Chem. Phys. Lett. 298, 57 (1998).
$^{34}$C. Hu, O. Sugino, and Y. Miyamoto, Phys. Rev. A 74, 032508 (2006).
$^{35}$C. Hu and O. Sugino, J. Chem. Phys. 126, 074112 (2007).
$^{36}$I. B. Bersuker, Chem. Rev. 101, 1067 (2001).
$^{37}$I. B. Bersuker, The Jahn-Teller Effect (Cambridge University Press, Cambridge, England, 2006).
$^{38}$C. Jungen and A. J. Merer, Mol. Phys. 40, 1 (1980).

$^{39}$I. A. Mikhailov, V. Kokoouline, Å. Larson, S. Tonzani, and C. H. Greene, Phys. Rev. A **74**, 032707 (2006).

$^{40}$Á. Vibók, G. J. Halász, T. Vèrteši, S. Suhai, M. Baer, and J. P. Toennies, J. Chem. Phys. **119**, 6588 (2003).

$^{41}$X. Gonze, J.-M. Beuken, R. Caracas, F. Detraux, M. Fuchs, G.-M. Rig- nanese, L. Sindic, M. Verstraete, G. Zerah, F. Jollet, M. Torrent, A. Roy, M. Mikami, Ph. Ghosez, J.-Y. Raty, and D. C. Allan, Com- put. Mater. Sci. **25**, 478 (2002). The ABINIT code is a common project of the Université Catholique de Louvain, Corning Incorporated, the Université de Liège, Mitsubishi Chemical Corp., and other contributors; see http://www.abinit.org.

$^{42}$S. Goedecker, M. Teter, and J. Hutter, Phys. Rev. B **54**, 1703 (1996).

$^{43}$N. Troullier and J. L. Martins, Phys. Rev. B **43**, 1993 (1991).

$^{44}$S. G. Louie, S. Froyen, and M. L. Cohen, Phys. Rev. B **26**, 1738 (1982).

$^{45}$R. Abrol, A. Shaw, and A. Kuppermann, J. Chem. Phys. **115**, 4640 (2001).

$^{46}$G. Halász, Á. Vibók, A. M. Mebel, and M. Baer, Chem. Phys. Lett. **358**, 163 (2002).

$^{47}$G. Halaász, Á. Vibók, A. M. Mebel, and M. Baer, J. Chem. Phys. **118**, 3052 (2003).

$^{48}$J. L. Martins, R. Car, and J. Buttet, J. Chem. Phys. **78**, 5646 (1983).

$^{49}$W. H. Gerber and E. Schumacher, J. Chem. Phys. **69**, 1692 (1978).

$^{50}$Y. Liu, I. B. Bersuker, W. Zou, and J. E. Boggs, Chem. Phys. **376**, 30 (2010).

$^{51}$G. J. Halász, Á. Vibók, R. Baer, and M. Baer, J. Chem. Phys. **124**, 081106 (2006).

$^{52}$D. R. Yarkony, J. Chem. Phys. **84**, 3206 (1986).

$^{53}$M. Desouter-Lecomte, D. Dehareng, B. Leyh-Nihant, M. Th. Praet, A. J. Lorquet, and J. C. Lorquet, J. Phys. Chem. **89**, 214 (1985).