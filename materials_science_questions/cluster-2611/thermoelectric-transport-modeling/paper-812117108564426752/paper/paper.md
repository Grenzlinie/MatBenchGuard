PHYSICAL REVIEW B 73, 035120 (2006)

# Electronic structure calculations of strongly correlated electron systems by the dynamical mean-field method

V. S. Oudovenko
Bogoliubov Laboratory for Theoretical Physics, Joint Institute for Nuclear Research, 141980 Dubna, Russia
and Center for Materials Theory, Department of Physics and Astronomy, Rutgers University, Piscataway, New Jersey 08854, USA

G. Pálsson, K. Haule, and G. Kotliar
Center for Materials Theory, Department of Physics and Astronomy, Rutgers University, Piscataway, New Jersey 08854, USA

S. Y. Savrasov
Department of Physics, University of California, Davis, One Shields Avenue, Davis, California 95616, USA

(Received 13 October 2005; published 18 January 2006)

We review some aspects of the realistic implementation of the dynamical mean-field theory. We extend some dynamical mean-field techniques to include the calculations of transport coefficients. The approach is illustrated on $La_{1-x}Sr_xTiO_3$ material undergoing a density-driven Mott transition.

DOI: 10.1103/PhysRevB.73.035120
PACS number(s): 71.10.—w, 71.27.+a, 75.20.Hr

## I. INTRODUCTION

In recent years understanding of the physics of strongly correlated materials has undergone tremendous increase. This is in part due to the advances in the theoretical treatments of correlations, such as the development of dynamical mean-field theory (DMFT).$^1$ This approach offers a minimal description of the electronic structure of correlated materials, treating both the Hubbard and the quasiparticle bands on the same footing. It becomes exact in the limit of infinite lattice coordination introduced in the pioneering work of Metzner and Vollhardt.$^2$ The great allure of DMFT is the flexibility of the method and its adaptability to different systems as well as the simple conceptual picture it allows us to form of the dynamics of the system. The mean-field nature of the method and the fact that the solution maps onto an impurity model, many of which have been thoroughly studied in the past, means that a great body of previous work can be brought to bear on the solution of models of correlated lattice electrons. This is exemplified by the great many numerical methods that can be employed to solve the DMFT equations.

DMFT has been very successful in understanding the mechanism of the Mott transition in model Hamiltonians. We now understand that the various concentration-induced phase transitions can be viewed as bifurcation of a single functional of the Weiss field. The phase diagram of the one-band Hubbard model, demonstrating that there is a first-order Mott transition at finite temperatures, is fully established.$^1$ Furthermore Landau-like analysis demonstrates that all the qualitative features are quite generic at high temperatures.$^3$ However, the low-temperature ordered phases and the quantitative aspects of the spectra of specific materials clearly require realistic treatment.

This triggered realistic development of DMFT in the last decade which has now reached the stage that we can start tackling real materials from an almost $ab$ $initio$ approach,$^{4,5}$ something which in the past has been exclusively in the domain of density functional theories. We are now starting to see the merger of DMFT and such $ab$ $initio$ techniques and consequently the opportunities for doing real electronic structure calculations for strongly correlated materials which so far were not within the reach of traditional density functional theories.

Density functional theory$^6$ (DFT) is the canonical example of the $ab$ $initio$ approach, very successful in predicting ground-state properties of many systems which are less correlated, for example the elemental metals and semiconductors. However, it fails in more correlated materials. It is unable to predict that any system is a Mott insulator in the absence of magnetic order. It is also not able to describe correctly a strongly correlated metallic state. As a matter of principle DFT is a theory of the ground state. Its Kohn-Sham spectra cannot be rigorously identified with the excitation spectra of the system. In weakly correlated substances the Kohn-Sham spectra is a good approximation to start a perturbative treatment of the one-electron spectra using the $GW$ method.$^7$ However, this approach breaks down in strongly correlated situations, because it is unable to produce Hubbard bands. In orbitally ordered situations the local density approximation (LDA)+$U$ method$^8$ produces the Hubbard bands; however, this method fails to produce quasiparticle bands and hence it is unable to describe strongly correlated metals. Furthermore, once long-range order is lost the LDA+$U$ method reduces to the LDA and hence it becomes inappropriate even for Mott insulators.

Dynamical mean-field theory is the simplest theory that is able to describe on the same footing total energies and the spectra of correlated electrons even when it contains both quasiparticle and Hubbard bands. Combined with the LDA, one then has a theory that reduces to a successful method (LDA) in the weak-correlation limit. In the static limit, one can show$^9$ that LDA+$U$ can be viewed as a static limit of the LDA+DMFT used in conjunction with the Hartree-Fock approximation. Therefore the LDA+$U$ is equivalent to the LDA+DMFT+further approximations which are only justified in static ordered situations. Up to now, the realistic LDA

1098-0121/2006/73(3)/035120(21)/$23.00
035120-1
©2006 The American Physical Society

band structure was considered with DMFT for the purpose of computing one-electron (photoemission) spectra and total energies.

Following Refs. 1, 4, and 5 in this paper we extend this approach to computation of transport properties. Many transport studies within DMFT applied to model Hamiltonians have been carried out, and the strengths (nonperturbative character) and limitations (absence of vertex corrections) are well understood. However, applications to real materials require realistic computations of current matrix elements.

There are two ways in which the DMFT can be used to understand the physics of real materials. The simplest approach, outlined in Refs. 1 and 4, is closely tied to the idea of model Hamiltonians. This requires (i) methodology for deriving the hopping parameters and the interaction constants, (ii) a technique for solving the dynamical mean-field equations, and (iii) an algorithm for evaluating the transport function which enters in the equations of transport coefficients. The second direction is more ambitious and focus on an integration of (i) and (ii) using functional formulations. $^{10}$

In this paper we follow the first approach. The emphasis here is in illustration of different aspects of the modeling which affect the final answer. This is necessary to obtain a balanced approach toward material calculations. There are now many impurity solvers; they differ in their accuracy and computational cost. In the present paper we use two impurity solvers, the Hirsch-Fye quantum Monte Carlo (QMC) method$^{11}$ and the symmetrized finite-$U$ non-crossing approximation$^{12}$ (SUNCA) method comparing them in the context of simplified models without the additional complications of real materials. To calculate the transport properties we use the SUNCA method as an impurity solver and $La_{1-x}Sr_{x}TiO_{3}$ as an example material.$^{13}$ For other reviews of realistic implementations of DMFT and electronic structure see Ref. 14.

In the next section we briefly review basic dynamical mean-field theory concepts and their application to realistic structure calculations. The theory of the transport calculations is given in Sec. III. The test system used for transport calculations, which is doped $LaTiO_{3}$ ceramics, and the DMFT results are described in Sec. IV. The results of dc transport calculations are presented in Sec. V. And finally we come to conclusions in Sec. VI.

## II. DYNAMICAL MEAN-FIELD THEORY
### A. Realistic DMFT formalism

A central concept in electronic structure theory is the $f$-model Hamiltonian. Conceptually, one starts from the full many-body problem containing all electrons and then proceeds to eliminate some high-energy degrees of freedom. The result is a Hamiltonian containing only a few bands. The determination of the model Hamiltonian is a difficult problem in itself, which has received significant attention.$^{15-21}$ The Kohn-Sham Hamiltonian is a good starting point for the kinetic part of the Hamiltonian and can be conveniently expressed in a basis of linear muffin-tin orbitals (LMTO's),$^{22}$ which need not be orthogonal (see Appendix A), as

$$
H_{L D A}=\sum_{i m, j m^{\prime}, \sigma}\left(\varepsilon_{i m} \delta_{i m, j m^{\prime}}+t_{i m, j m^{\prime}}\right) c_{i m \sigma}^{\dagger} c_{j m^{\prime} \sigma}, \quad(1)
$$

where $i,j$ are atomic site indices, $m$ is the orbital one, and $\sigma$ denotes spin.

It is well known that the LDA severely underestimates strong electron interactions between localized $d$ and $f$ electrons because the exchange interaction is taken into account only approximately via the functional of electron density. To correct this situation, the LDA Hamiltonian can be supplemented with a Coulomb interaction term between electrons in the localized orbitals (here we will call them a heavy set of orbitals). The largest contribution comes from the Coulomb repulsion between electrons on the same lattice site which we will approximate by the interaction matrix $U^{i}$ of the heavy shell $(h)$ of atom $i$ as

$$
H_{i n t}=\frac{1}{2} \sum_{i \alpha \alpha^{\prime}} U_{\alpha \alpha^{\prime}}^{i} n_{i \alpha} n_{i \alpha^{\prime}},
$$

where the index $\alpha=(m,\sigma)$ combines the orbital and spin indices.

The LDA Hamiltonian already contains a part of the local interaction which has to be subtracted to avoid double counting. The full Hamiltonian is thus approximated by

$$
H=H_{L D A}-H_{d c}+H_{i n t}=H^{0}+H_{i n t}, \quad(2)
$$

where $H^{0}$ is the one-particle part of the Hamiltonian, which will play the role of the kinetic term within a DMFT approach. The double-counting correction cannot be rigorously derived within the LDA+DMFT. Instead, it is commonly assumed to have a simple static Hartree-Fock form, just shifting the energies of the heavy set,

$$
H_{d c \tau m, \tau^{\prime} m^{\prime}}(k)=\delta_{\tau m, \tau^{\prime} m^{\prime}} \delta_{\tau \tau_{h}} E_{d c}. \quad(3)
$$

Here, $\tau$ is the atomic index in the elementary unit cell; $\tau_{h}$ runs over atoms with correlated orbitals. The simplest approximation commonly used for $E_{d c}$ is$^{4,8}$

$$
E_{d c}=U\left(n_{h}-\frac{1}{2}\right), \quad(4)
$$

where $n_{h}=\sum_{m \sigma} n_{m \sigma}$ is the total number of electrons in the heavy shell (see Appendix A).

The main postulate of the DMFT formalism is that the self-energy is local, i.e., it does not depend on momentum, $\Sigma(k,\omega)=\Sigma(\omega)$. This postulate can be shown to be exact in the limit of infinite dimensions provided that the hopping parameters between different sites are scaled appropriately. Within this approach, the original lattice problem can be mapped onto an Anderson impurity model where the local Green's function and the self-energy, $G_{loc}$ and $\Sigma$, are identified with the corresponding functions for the impurity model, i.e.,

$$
\Sigma_{i m p}(\omega)=\Sigma(\omega) \quad \text { and } \quad G_{i m p}(\omega)=G_{l o c}(\omega). \quad(5)
$$

Equations (5) along with the trivial identity

$$G_{l o c}(\omega)=\sum_{k} G(k, \omega)\qquad(6)$$

constitute a closed set of self-consistent equations (here and everywhere in the text the normalization over the number of lattice points is assumed). The only thing that remains is to solve the Anderson impurity model.

Notice that the statement that the self-energy is local is a basis-dependent statement and if $\Sigma(i \omega_{n})$ is momentum independent in one basis and $U_{k}$ is a unitary transformation from one basis to another, and the LMTO Hamiltonian, $H_{L D A}$ in the new basis is given by $U_{k} H_{L D A} U_{k}^{\dagger}$ , then the self-energy in the new basis $\Sigma'=U_{k} \Sigma(i \omega_{n}) U_{k}^{\dagger}$ is momentum dependent. Therefore DMFT approximation, if valid at all, is valid in one basis. $^{23}$ Hence, we will work in a very localized basis where the DMFT approximation is most justified.

So we assume that the self-energy is local and nonzero only in the block of heavy orbitals. Therefore it is convenient to partition the Hamiltonian and the Green's function into the light and heavy sets (denoted by $l$ and $h$ , respectively) as
$$\begin{aligned}
G(k, \omega)= & {\left[(\omega+\mu)\left(\begin{array}{ll}
O_{h h} & O_{h l} \\
O_{l h} & O_{l l}
\end{array}\right)_{k}-\left(\begin{array}{ll}
H_{h h}^{0} & H_{h l}^{0} \\
H_{l h}^{0} & H_{l l}^{0}
\end{array}\right)_{k}\right.} \\
& \left.-\left(\begin{array}{cc}
\Sigma_{h h}(\omega) & 0 \\
0 & 0
\end{array}\right)\right]^{-1},
\end{aligned}\qquad(7)$$
where $[\cdots]^{-1}$ means matrix inversion, $\mu$ is the chemical potential, and $O$ is the overlap matrix (see Appendix B).

In DMFT we construct the self-energy $\Sigma$ as a solution of the Anderson impurity model with a noninteracting propagator (Weiss function) $G_{0}$ ,
$$\begin{aligned}
S_{i m p}= & \sum_{\alpha \alpha^{\prime}, \tau \tau^{\prime}} c_{\alpha}^{\dagger}(\tau) \mathcal{G}_{0_{\alpha \alpha^{\prime}}}^{-1}\left(\tau, \tau^{\prime}\right) c_{\alpha^{\prime}}\left(\tau^{\prime}\right) \\
& +\sum_{\alpha \alpha^{\prime} \in h} \frac{U_{\alpha \alpha^{\prime}}}{2} n_{\alpha}(\tau) n_{\alpha^{\prime}}(\tau),
\end{aligned}\qquad(8)$$
where $\alpha$ and $\alpha'$ are running over indices $m \sigma$ . The Weiss function can be linked to the lattice quantities since the local Green's function and self-energy are related to each other by the Dyson equation
$$G_{l o c}\left(i \omega_{n}\right)^{-1}=\mathcal{G}_{0}\left(i \omega_{n}\right)^{-1}-\Sigma\left(i \omega_{n}\right).\qquad(9)$$

Combining Eqs. (6), (7), and (9) we finally obtain
$$\mathcal{G}_{0}^{-1}\left(i \omega_{n}\right)=\left(\sum_{k} \frac{1}{\left(i \omega_{n}+\mu\right) O_{k}-H_{k}^{0}-\Sigma\left(i \omega_{n}\right)}\right)^{-1}+\Sigma\left(i \omega_{n}\right).$$

One can solve the very general impurity model defined by the action (8) and Weiss field (10). But it is much cheaper to eliminate the light (weakly interacting) bands and define an effective action in the subspace of heavy bands only. In this way, the local problem can be substantially simplified. The procedures of light band elimination and restoration are called downfolding and upfolding, respectively. Their detailed description can be found elsewhere. $^{24}$

To solve the set of DMFT equations, a method to solve the local problem is required. In the following, we will focus our attention on two impurity solvers: QMC, $^{1,25}$ andSUNCA. $^{12}$

Below, we summarize the basic steps in the DMFT self- consistent scheme that delivers the local self-energy-a cru- cial quantity to calculate the transport and optical properties of a solid.

Usually one starts the iteration by a guess for the Weiss field $G_{0}^{-1}$ from which the local Green's function $G_{l o c}$ is cal culated by one of the impurity solvers. The self-energy is then obtained by the use of the Dyson equation
$$G_{h h}^{-1}=\mathcal{G}_{0}^{-1}-\Sigma.\qquad(11)$$

Momentum summation over the Brillouin zone, also called the DMFT self-consistency condition,
$$G_{h h}=\sum_{k}\left[(\omega+\mu) O_{e f f}(k)-H_{e f f}(k)-\Sigma\right]^{-1},\qquad(12)$$
delivers a new guess for the local Green's function andthrough the Dyson equation also for the Weiss field $G_{0}^{-1}$ :
$$\mathcal{G}_{0 h h}=[(\omega+\mu)-\Delta]^{-1},\qquad(13)$$
where the hybridization function $\Delta$ behaves regularly at in finity.

The iteration is continued until convergence is found to the desired level. The scheme can be illustrated by the following flowchart:
$$\mathcal{G}_{0}^{-1} \stackrel{\text { Imp solver }}{\rightarrow} G \stackrel{D E}{\rightarrow} \Sigma \stackrel{D M F T S C C}{\rightarrow} \mathcal{G}_{0}^{-1},$$
where DE stands for the Dyson equation and DMFT SCC means the DMFT self-consistent condition.

The QMC impurity solver is defined in imaginary time $\tau$ ; therefore the following additional Fourier transformations between imaginary time and Matsubara frequency points arenecessary:
$$\mathcal{G}_{0}(i \omega) \stackrel{I F T}{\rightarrow} \mathcal{G}_{0}(\tau) \stackrel{Q M C}{\rightarrow} G(\tau) \stackrel{F T}{\rightarrow} G(i \omega).$$

Here FT and IFT are the direct Fourier and inverse Fourier transformations, respectively. Since the QMC method produces results in complex time $[G(\tau_{m})$ with $\tau_{m}=m \Delta \tau$ , m=1,..., L] and the DMFT self-consistency equations make use of the frequency-dependent Green's functions and self- energies, we must have an accurate method to compute Fou- rier transforms from the time to the frequency domain. This is done by representing the functions in the time domain by cubic splined functions which should go through the original points with the condition of continuous second derivatives imposed. Once we know the cubic spline coefficients we can compute the Fourier transformation of the splined functions analytically (see Appendixes C and D). After the self- consistency is reached, the analytic continuation is required to obtain the real-frequency self-energy. This issue is ad- dressed in Sec. II B. Let us notice here that for simplicity in our QMC calculations we used the orthogonal basis. The nonorthogonal implementation can be found in Ref. 26.

![](./images/812117108564426752_1.jpg)

FIG. 1. (Color online) Spectral function for semicircular DOS, inverse temperature $\beta$=16 and density $n$=0.8. Dot-dashed, full, and double-dot-dashed curves correspond to the sum (17) with $M$ chosen to be 6, 9, and 12, respectively. In the legend, we also print the lowest singular value taken into account ($S_M$). For comparison we show the maximum entropy spectrum (dashed curve) and SUNCA spectrum (dotted line). The inset shows the same spectra in a broader window.

function obtained by the maximum entropy method and the SUNCA solution for the same parameters. The difference between the various curves gives as a rough estimate for the accuracy of the technique. As we see, the quasiparticle resonance is obtained by reasonably high accuracy, while the Hubbard band is determined with less accuracy. In the inset of Fig. 1 we plot the same curves in a broader window. As we see, the singular value decomposition does not guarantee the spectra to be positive at higher frequencies. This, however, does not prevent us from accurately determining most of the physical quantities.

Within DMFT, the real-frequency self-energy can be obtained from the local Green's function by the inversion of the Hilbert transform. Although the implementation is very straightforward, we will briefly mention the algorithm we used. In the high-frequency regime, we can expand the Hilbert transform in terms of moments of the density of states (DOS) as

$$
w(z)=\int \frac{D(\varepsilon) d \epsilon}{z-\varepsilon}=\sum_{n} \frac{\left\langle\varepsilon^{n}\right\rangle}{z^{n+1}}. \tag{18}
$$

The series can be inverted and solved for $z$:

$$
\begin{aligned}
z(w)= & \frac{1}{w}+\langle\varepsilon\rangle+\left(\left\langle\varepsilon^{2}\right\rangle-\langle\varepsilon\rangle^{2}\right) w+\left(\left\langle\varepsilon^{3}\right\rangle-3\left\langle\varepsilon^{2}\right\rangle\langle\varepsilon\rangle+2\langle\varepsilon\rangle^{3}\right) w^{2} \\
& +\cdots. \tag{19}
\end{aligned}
$$

For most of the frequency points, the expansion up to some higher power ($\sim w^{8}$) gives already an accurate estimation for the inverse function. However, when $w$ gets large, we need to use one of the standard root-finding methods to accurately determine the solution. This is, however, much easier than general root finding in the complex plane since we always have a good starting guess for the solution. We start evaluating the inverse function at high frequency where the absolute value of $G$ is small and we can use the expansion in Eq. (19). Then we use the fact that the Green's function is a continuous function of a real frequency and we can follow the solution from frequency point to frequency point by improving it with a few steps of a secant (or Newton) method. Special attention, however, must be paid not to cross the branch cut and get lost in the nonphysical complex plane. Therefore, each secant or Newton step has to be shortened if necessary. The self-energy is finally expressed by the inverse of Hilbert transform $w^{-1}$ as

$$
\Sigma=\omega+\mu-w^{-1}(G). \tag{20}
$$

![](./images/812117108564426752_2.jpg)

FIG. 2. (Color online) Imaginary part of the self-energy obtained from the Green's function by the inverse of the Hilbert transform. Full line was obtained by the singular value decomposition, the dashed by the maximum entropy method, and the dot dashed by SUNCA. Parameters used are the same as in Fig. 1.

Figure 2 shows the imaginary part of the self-energy obtained by both analytic-continuation methods. As a reference and comparison we also show the results obtained by the SUNCA method, which is defined and evaluated on the realfrequency axes and hence does not require analytic continuation. The low-frequency part of the self-energy is again very reliably determined and does not differ by more than 3%.

## III. TRANSPORT COMPUTATION

### A. Transport theory

The transport parameters of the system are expressed in terms of so-called kinetic coefficients, denoted here by $A_{m}$. The equation for the electrical resistivity $\rho$ is given by

$$
\rho=\frac{k_{B} T}{e^{2}} \frac{1}{A_{0}}. \tag{21}
$$

The thermopower $S$ and the thermal conductivity $\kappa$ are expressed through

$$
S=-\frac{k_{B}}{|e|} \frac{A_{1}}{A_{0}}, \quad \kappa=k_{B}\left(A_{2}-\frac{A_{1}^{2}}{A_{0}}\right). \tag{22}
$$

Within the Kubo formalism$^{28}$ the kinetic coefficients are given in terms of equilibrium state current-current correlation functions of the particle and the heat currents in the system; namely we have

$$
A_{m}=\beta^{m} \lim _{\omega \rightarrow 0} Z_{m}(i v \rightarrow \omega+i 0),\qquad(23)
$$

where

$$
Z_{0}(i v)=\frac{i \hbar}{i v \beta} \int_{0}^{\beta} d \tau e^{i v \tau}\left\langle T_{\tau} j^{x}(\tau) j^{x}(0)\right\rangle,\qquad(24)
$$

$$
Z_{1}(i v)=\frac{i \hbar}{i v \beta} \int_{0}^{\beta} d \tau e^{i v \tau}\left\langle T_{\tau} j^{x}(\tau) Q^{x}(0)\right\rangle,\qquad(25)
$$

$$
Z_{2}(i v)=\frac{i \hbar}{i v \beta} \int_{0}^{\beta} d \tau e^{i v \tau}\left\langle T_{\tau} Q^{x}(\tau) Q^{x}(0)\right\rangle.\qquad(26)
$$

To evaluate these correlation functions, expressions for the electric and heat currents $j^{x}$ and $Q^{x}$ are needed. Once those currents are evaluated calculation of the transport properties within the DMFT is reduced to the evaluation of the transport function

$$
\phi^{x x}(\epsilon)=\frac{1}{V} \sum_{k} \operatorname{Tr}\left\{v_{k}^{x}(\epsilon) \rho_{k}(\epsilon) v_{k}^{x}(\epsilon) \rho_{k}(\epsilon)\right\},\qquad(27)
$$

and the transport coefficients

$$
A_{m}=N_{s p i n} \pi \hbar \int_{-\infty}^{\infty} d \epsilon \phi^{x x}(\epsilon) f(\epsilon) f(-\epsilon)(\beta \epsilon)^{m}.\qquad(28)
$$

The momentum integral in Eq. (27) extends over the Brillouin zone and $V$ is the volume of the unit cell. The simplest form of the velocity is $\langle k \beta|(1 / m) \nabla_{x}| k \alpha\rangle=v_{k}^{\alpha \beta}$ and it requires evaluation of matrix elements of $\nabla_{x}$. However, an alternative form of the current and the transport function can be derived via the Peirls substitution generally in the nonorthogonal basis and is described in Appendix E. These two procedures generally give different answers. $^{23,29,30}$

Next we define the energy-dependent velocity as

$$
\vec{v}_{k}(\epsilon)=\vec{v}_{k}-\epsilon \vec{u}_{k}.\qquad(29)
$$

The second term is due to the nonorthogonality of the basis or more specifically due to overlap between orbitals at different sites; local nonorthogonality does not contribute to the velocity. The spectral density matrix $\rho_{k}(\epsilon)$ is the multiorbital generalization of the regular single orbital density of states and is given in terms of the retarded Green's function $G$ of the system by the equation

$$
\rho_{k}(\epsilon)=-\frac{1}{2 \pi i}\left\{G_{k}(\epsilon)-\left[G_{k}(\epsilon)\right]^{\dagger}\right\}.\qquad(30)
$$

Finally the Green's function (GF) is given by

$$
G_{k}(z)=\left[(z+\mu) O_{k}-H_{k}^{0}-\Sigma(z)\right]^{-1}.\qquad(31)
$$

Note here that in accordance with the DMFT the self-energy matrix is assumed to be momentum independent. Now given an effective Hamiltonian for the system, an overlap matrix, and the self-energy, the equations above give a complete prescription for computing the transport parameters. For computation of Eq. (27) we have developed two methods; one method generalizes the analytical tetrahedron method $^{31}$ (ATM) and the other one uses the one-particle GF method in DMFT, $^{4}$ used to compute spectral densities in band structure calculations. First the total Hamiltonian $H_{k}(\epsilon)=H_{k}^{0}+\Sigma(\epsilon)$ is diagonalized and written in the form

$$
H_{k}(\epsilon)=O_{k} A_{k}^{R}(\epsilon) E_{k}(\epsilon) A_{k}^{L}(\epsilon) O_{k},\qquad(32)
$$

where $E_{k}$ is the diagonal matrix of complex eigenvalues and $A_{k}^{R}$ and $A_{k}^{L}$ are the right and the left eigenvector matrices, respectively. Then the Green's function can be written as

$$
G_{k}(\epsilon)=A_{k}^{R}(\epsilon)\left[(\epsilon+\mu) I-E_{k}(\epsilon)\right]^{-1} A_{k}^{L}(\epsilon),\qquad(33)
$$

with $I$ being the identity matrix. The transport function can now be expressed as

$$
\begin{aligned}
\phi^{x x}(\epsilon)= & -\frac{1}{2 \pi^{2} V} \operatorname{Re} \sum_{k, p q}\left[r_{k, q p}^{x} r_{k, p q}^{x} D_{k, p} D_{k, q}\right. \\
& \left.-\frac{1}{2}\left(s_{k, q p}^{x} t_{k, p q}^{x}+s_{k, p q}^{x} t_{k, q p}^{x}\right) D_{k, p}\left(D_{k, q}\right)^{*}\right], \quad(34)
\end{aligned}
$$

where the matrices $r^{x}, s^{x}$, and $t^{x}$ are

$$
\begin{aligned}
& r_{k}^{x}=r_{k}^{x}(\epsilon) \equiv A_{k}^{L}(\epsilon) v_{k}^{x}(\epsilon) A_{k}^{R}(\epsilon), \\
& s_{k}^{x}=s_{k}^{x}(\epsilon) \equiv A_{k}^{L}(\epsilon) v_{k}^{x}(\epsilon)\left[A_{k}^{L}(\epsilon)\right]^{\dagger}, \\
& t_{k}^{x}=t_{k}^{x}(\epsilon) \equiv\left[A_{k}^{R}(\epsilon)\right]^{\dagger} v_{k}^{x}(\epsilon) A_{k}^{R}(\epsilon),
\end{aligned}\qquad(35)
$$

and $D_{k}$ is a diagonal matrix defined by

$$
D_{k}=D_{k}(\epsilon) \equiv\left[(\epsilon+\mu) I-E_{k}(\epsilon)\right]^{-1}.\qquad(36)
$$

When the computation of the transport function is carried out one is faced with computing integrals of the form

$$
\begin{gathered}
\sum_{k} \frac{r_{k, p q}^{x} r_{k, q p}^{x}}{\left(\epsilon+\mu-E_{k, p}\right)\left(\epsilon+\mu-E_{k, q}\right)}, \\
\sum_{k} \frac{s_{k, p q}^{x} t_{k, q p}^{x}}{\left(\epsilon+\mu-E_{k, p}\right)\left(\epsilon+\mu-E_{k, q}^{*}\right)}.
\end{gathered}\qquad(37)
$$

The strategy that is used to compute these integrals is similar in spirit to the analytical tetrahedron method. The Brillouin zone is split up into a collection of equal-sized tetrahedra and the integral over each tetrahedron is taken using linear interpolation between the four corners of the tetrahedron. In the analytical tetrahedron method the numerator and the energy eigenvalues in the denominator are linearized independently and the resulting integral is then done analytically. In our case we would want to follow the same rule which results in two linear functions in the denominator. Unfortunately we have not been able to evaluate that integral in the most general case, i.e., when none of the tetrahedron corners are degenerate, although solutions can be found for degenerate cases when at least two of the four corners of the tetrahedron are identical. Hence we have to pursue further approximations which we outline below.

The two main integrals that we need to compute are of the form

$$
T_{S S}^{p q}=\sum_{k \in \Delta} \frac{F(k)}{\left(z-E_{k, p}\right)\left(z-E_{k, q}\right)},
$$

$$
T_{O S}^{p q}=\sum_{k \in \Delta} \frac{F(k)}{\left(z-E_{k, p}\right)\left(z-E_{k, q}\right)^{*}} . \qquad (38)
$$

Here $\Delta$ denotes the tetrahedron and $SS$ indicates that the imaginary parts of both denominators have the same sign and $OS$ indicates that they have the opposite sign. This is ensured by the fact that the self-energy is retarded and $z$ is real. For the diagonal case $(p=q)$ the $T_{SS}$ integral can be computed exactly by linearizing the eigenvalues in the denominator; one simply needs to differentiate the ATM formulas by Lambin and Vigneron. $^{31}$ For the diagonal $T_{OS}$, however, we note that the numerator is real and therefore we can write the integral in the following form:

$$
T_{O S}^{p p}=\operatorname{Im} \sum_{k \in \Delta}\left(\frac{F(k)}{\gamma_{k, p}}\right) \frac{1}{z-E_{k, p}}, \qquad (39)
$$

where $\gamma_{k,p} = \operatorname{Im} E_{k,p}$. We note that $\gamma_{k,p}$ is solely due to the self-energy, which is momentum independent, and thus it is reasonable to expect that $\gamma_{k,p}$ changes little with momentum. Hence the term in the parentheses will be approximated linearly within the tetrahedron and the resulting integral can be computed with the ATM.

The off-diagonal case $(p \neq q)$ for both $T_{SS}$ and $T_{OS}$ is treated the same way so we will just look at $T_{SS}$. Both factors in the denominator are inspected and we determine which one has larger modulus (on average if necessary). Then we write the integral in the form

$$
\left.T_{S S}^{p q}\right|_{p \neq q}=\sum_{k \in \Delta}\left(\frac{F(k)}{\left(z-E_{k}\right)_{L}}\right) \frac{1}{\left(z-E_{k}\right)_{S}}, \qquad (40)
$$

where $L$ indicates the denominator with the larger modulus and $S$ indicates the one with the smaller modulus. The term in the parentheses is now approximated linearly within the tetrahedron and the resulting integral can be computed with the ATM.

The approach described here to compute the transport function has been tested numerically against models where other methods can be used to evaluate the transport function. For cubic systems with nearest-neighbor hopping one can, for instance, evaluate both the density of states and the transport function quite efficiently using fast Fourier transforms. $^{1}$ In general the results are quite accurate.

### B. Small-scattering limit

In order to make connections with previous approaches to the computation of transport properties it is interesting to consider the small-scattering limit. So we take the self-energy of the form

$$
\Sigma(\epsilon)=\Sigma^{\prime}(\epsilon)+\gamma \Sigma^{\prime \prime}(\epsilon), \qquad (41)
$$

where $\Sigma'(\epsilon)$ is the real part of the self-energy matrix, $\gamma\Sigma''(\epsilon)$ is the imaginary part, and $\gamma$ is a small parameter.

It is clear that the transport function will diverge as $1/\gamma$ and thus we can approximate the numerator matrix elements to zeroth order in $\gamma$. Within this approximation the transport function can be written as

$$
\phi^{x x}(\epsilon)=\frac{1}{V} \sum_{k, p}\left(v_{k, p}^{x}\right)^{2} \tau_{k, p}(\epsilon) \delta\left(\epsilon+\mu-E_{k, p}^{\prime}\right), \qquad (42)
$$

where $E_{k,p}'$ are the eigenvalues of $H_{0}^{0}+\Sigma'(\epsilon)$ and $v_{k,p}^{x}$ denotes the corresponding band velocity. The lifetime $\tau_{k,p}(\epsilon)$ is formally given by

$$
\tau_{k, p}(\epsilon)=\frac{1}{2 \pi\left|\operatorname{Im} E_{k, p}\right|} ; \qquad (43)
$$

here $E_{k,p}$ are the eigenvalues of the full Hamiltonian. The imaginary part of these eigenvalues is due to the scattering term and is therefore to first approximation linear in $\gamma$. The lifetime therefore diverges as $1/\gamma$ but for a finite value of $\gamma$ we regard Eq. (42) as an approximation to the transport function and we will refer to this approach as the small-scattering approximation.

In spite of the limited validity of the small-scattering approximation it is useful in the sense that it is computationally much simpler to evaluate the transport function in the small-scattering approximation than in the general case. Therefore it can be used in order to obtain a rough idea of the behavior of the transport parameters.

The equations of the small-scattering approximation are very similar to the formulas that have been used by other groups to compute the transport parameters of real materials. $^{32-34}$ In particular the assumption of constant lifetime is quite often used in practice, especially when the thermopower is being calculated. In this case we obtain

$$
\phi^{x x}(\epsilon)=\tau \Phi^{x x}(\epsilon), \qquad (44)
$$

where the so-called transport density $\Phi$ is defined as

$$
\Phi^{x x}(\epsilon)=\frac{1}{V} \sum_{k, p}\left(v_{k, p}^{x}\right)^{2} \delta\left(\epsilon+\mu-E_{k, p}^{\prime}\right). \qquad (45)
$$

Numerical tests have shown that while the small-scattering approximation can be quite good for broadbands it does not work well in narrowbands such as the dynamically generated quasiparticle bands of strongly correlated systems due to constant time approximation used.

In the case of the thermopower we obtain

$$
\begin{gathered}
S=-\frac{k_{B}}{|e|}\left(\frac{\int_{-\infty}^{\infty} \Phi^{x x}(\epsilon) f(\epsilon) f(-\epsilon)(\beta \epsilon)}{\int_{-\infty}^{\infty} \Phi^{x x}(\epsilon) f(\epsilon) f(-\epsilon}\right), \\
\stackrel{T \rightarrow 0}{=}-\left.\frac{k_{B}}{|e|} \frac{\pi^{2} k_{B} T}{3} \frac{d}{d \epsilon} \ln \Phi^{x x}(\epsilon)\right|_{0}.
\end{gathered}\qquad(46)
$$

This is the classical Mott relation for the thermopower. In the literature this equation is often quoted with the transport density replaced by the spectral density and much emphasis placed on the fact that in case the Fermi level coincides with a Van Hove singularity the thermopower diverges. This conclusion is not supported when the correct form for the ther-


mopower is used since no Van Hove singularities are present in the transport density.

For free electrons the transport density is given by
$$
\Phi^{x x}(\epsilon)=\frac{1}{12 \pi^{2}}\left(\frac{2 m_{e}}{\hbar^{2}}\right)^{3 / 2} \epsilon^{3 / 2}, \quad(47)
$$
and therefore we get
$$
S=-\frac{k_{B}}{|e|} \frac{\pi^{2} k_{B} T}{2} \frac{1}{\epsilon_{F}}=-n^{-2 / 3} T \times 0.281 \frac{n V}{K}, \quad(48)
$$
where the density $n$ is measured in electrons per cubic Bohr radius and the temperature $T$ is measured in kelvin. In case the effective mass of the electrons is enhanced the ther- mopower will simply increase by the enhancement factor.

The enhancement of the thermopower can also be de- duced from the Mott equation in case the only effect of the real part of the self-energy is to change the effective mass of the bands that cross the Fermi surface. If we assume that the change in effective mass is the same for all the bands that participate in the transport the low-temperature thermopower becomes
$$
S \simeq-\left.\frac{k_{B}}{|e|} \frac{\pi^{2} k_{B} T}{3 Z} \frac{d}{d \epsilon} \ln \Phi^{0, x x}(\epsilon)\right|_{0}, \quad(49)
$$
where the noninteracting transport density $\Phi^{0, x x}(\epsilon)$ is defined by
$$
\Phi^{0, x x}(\epsilon)=\frac{1}{V} \sum_{k, p}\left(v_{k, p}^{0, x}\right)^{2} \delta\left(\epsilon+\mu-E_{k, p}^{0}\right). \quad(50)
$$

Here $Z$ denotes the quasiparticle residue of the bands in volved. Hence we see indeed that the low-temperature ther- mopower is enhanced by a factor of $1 / Z$ compared to the noninteracting thermopower.

## IV. TEST SYSTEM AND DMFT RESULTS

### A. Test system

To test the obtained transport equations on a realistic sys- tem we have chosen a doped $LaTiO_{3}$ compound. The $La_{1-x} Sr_{x} TiO_{3}$ series has been studied very extensively in the past $^{35-40}$ and can be regarded as being one of the prime ex amples exhibiting the Mott-Hubbard metal-insulator transi- tion. The end compound $LaTiO_{3}$ when prepared well is a Mott-Hubbard insulator although in the literature it is often characterized as a correlated or a poor metal. At high tem- perature this material is paramagnetic. The other end com- pound $SrTiO_{3}$ is an uncorrelated band insulator with a direct gap of $3.3 eV$ . The electronic structure properties of the $La_{1-x} Sr_{x} TiO_{3}$ series is governed by the triple degenerated cu bic $t_{2 g}$ bands of the $3 d$ orbitals ( $d^{1}$ ionic configuration). $^{41}$ In the distorted structure of $LaTiO_{3}$ the degeneracy of the band has been lifted and the single electron occupies a very nar- row, nondegenerate $d_{x y}$ band. $^{42}$ Studies of the magnetic sus ceptibility do indeed indicate that the electronic structure of thePbnm phase is that of a narrow $d_{x y}$ band, which then with doping changes into a broad $t_{2 g}$ band (calculated bandwidth is $W=2.7 eV$ ) with degenerate $d_{x y}, d_{x z}$ , and $d_{y z}$ orbitals in the
<table><caption>TABLE I. The linear coefficient of specific heat $\gamma$ for $La_{1-x} Sr_{x} TiO_{3}$ measured in units of $mJ / mol K^{2}$ . The experimental data are taken from Ref. 45. LDA data for the linear coefficient of specific heat are computed from the $LaTiO_{3}$ LDA DOS.</caption>
<tbody><tr><th></th><td colspan="9">Doping (%)</td></tr><tr><th></th><td>5</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td><td>70</td><td>80</td></tr><tr><th>Experiment</th><td>16.52</td><td>11.51</td><td>8.57</td><td>7.70</td><td>6.21</td><td>5.38</td><td>4.55</td><td>4.35</td><td>3.52</td></tr><tr><th>LDA</th><td>3.23</td><td>3.16</td><td>3.00</td><td>2.82</td><td>2.67</td><td>2.52</td><td>2.38</td><td>2.19</td><td>2.10</td></tr></tbody></table>
$Ibmm$ and $Pm 3 m$ phases. As a function of doping the mate rial behaves as a canonical doped Mott insulator. The specific heat and the susceptibility are enhanced, the Hall number is unrenormalized, while the photoemission spectral function has a resonance with a weight that decreases as one ap- proaches half filling. Very near half filling, (for dopings less than $8 \%$ ) the physics is fairly complicated. At small dopingan antiferromagnetic metallic phase is observed. $^{39,43,44}$ 

To obtain the LDA band structure of $LaTiO_{3}$ we used the linear muffin-tin orbitals method in its atomic sphere ap- proximation (ASA) with the basis $Ti(4 s, 4 p, 3 d), O(2 s, 2 p)$ , and $La(6 s, 5 p, 5 d)$ assuming for simplicity instead a real orthorhombic structure with a small distortions a cubic one with the same volume and the lattice constant $a_{0}=7.40$ a.u. This approximation brings a slight overestimation of the ef- fective bandwidth and underestimation of the band gap be- tween valence and conduction bands. In photoemission stud- ies of $LaTiO_{3},^{13}$ a similar basis has been used.

Using the LDA band structure one can compute and com- pare with experiment the linear coefficient of specific heat which is simply given in terms of the density of states at the Fermi level by
$$
\gamma=2.357\left(\frac{\mathrm{mJ}}{\mathrm{mol} \mathrm{K}^{2}}\right) \frac{\rho_{t o t}\left(E_{f}\right)[\text { states } /(\mathrm{eV} \text { unit cell })]}{Z},
$$
where $Z$ is the quasiparticle residue or the inverse of the mass renormalization. In LDA calculations the value of $Z$ is equal to 1. Doping dependence of the linear coefficient of specific heat in LDA calculations was computed within the rigid band model. Our results along with the experimental data are presented in Table I.

In general, we see that the LDA data for $\gamma$ are lower than the experimental values, indicating a strong mass renormal- ization. We note also that as we get closer to the Mott- Hubbard transition the effective mass grows significantly. This is consistent with DMFT modeling of the Mott-Hubbard transition which shows that indeed the effective mass di- verges at the transition. We should note, however, that this is not a necessary signature for the Mott-Hubbard transition: in V2O3 the pressure-driven metal-insulator transition is accom- panied by the divergence of the effective mass whereas the doping-driven transition in the same system does not showthat divergence. $^{46}$ 

The physical picture of the studied material is quite trans- parent, very near half filling (dopings less than $8 \%$ ) the

Fermi energy becomes very small and now is comparable with the exchange interactions and structural distortion energies. A treatment beyond single-site DMFT then becomes important to treat the spin degrees of freedom. On the other hand for moderate and large doping, the Kondo energy is the dominant energy and the DMFT is expected to be accurate. This was substantiated by a series of papers which compared DMFT calculations in single-band or multiband Hubbard models using a simplified density of states with the physical properties of real materials. Reference 47 addressed the enhancement of the magnetic susceptibility and the specific heat as half filling is approached. The optical conductivity and the suppression of the charge degrees of freedom as the Mott insulator is approached was described in Refs. 48 and 49, the observation that the Hall coefficient is not renormalized was found in Refs. 50 and 51. Finally the thermoelectric power on the model level using iterative perturbation theory (IPT) as impurity solver was investigated by Pálsson and Kotliar. $^{52}$

Given the fact that only very simple tight-binding parametrizations were used in those works, and the fact that a large number of experiments were fitted with the same value of parameters one should regard the qualitative agreement with experiment as very satisfactory. The photoemission spectroscopy of this compound as well as in other transition metal compounds is not completely consistent with the bulk data, and it has been argued that disorder, and modeling of the specific surface environment is required to improve the agreement with experiment. $^{53}$ In this situation, it is clear that this is the simplest system for study, and it was in fact the first system studied by LDA+DMFT. $^{4}$

The important questions to be addressed are the degree of quantitative accuracy of DMFT. Furthermore, given the simplicity of this system, and the existence of well-controlled experiments, it is an ideal system for testing the effects of different approximations within the LDA+DMFT scheme.

### B. The model

As we pointed out in Sec. II for a correct description of a system with strong electron correlations one needs to bring the self-energy into the heavy orbitals. To this end a model which correctly describes the physics of interacting orbitals is needed. In this paper we consider a three-band Hubbard model whose underlying noninteracting dispersion relation is that of the degenerate cubic $t_{2g}$ band of the transition metal $3d$ orbitals. For simplicity the Hubbard interaction term is taken to be SU(6) invariant, i.e., there is equal interaction between two electrons of opposite spin in the same orbital as there is between two electrons in different orbitals on the same site. The more general case will be reconsidered in future publications.

The value of the interaction strength in our model is chosen large enough to exhibit metal-insulator behavior in the studied compound. In units of half bandwidth $D$, the interaction strength is taken to be $U$=5. The interaction strength should be regarded as an input parameter whose value has to be adjusted to the experimental situation. Saying this, we mean the chosen interaction strengths should be good enough to reproduce as many physical properties as possible with maximum proximity to experiment. To investigate the dependence of the calculated physical properties on the interaction strength we calculate all quantities studied in this paper for the values of Coulomb repulsion $U$=3, 4, and 5. On the model level $U$=4 is the value very close to the minimum interaction to get metal-insulator transition (MIT) for integer filling $n$=1 even in the threefold-degenerate Hubbard model using the DMFT as an instrument which takes care of the interaction in the system. Hence our choice of the interaction should guarantee exploration of two physically different behaviors of the system with and without the MIT. In the literature the absolute value of Coulomb interaction is the magnitude under discussion mainly because there is no direct and reliable method to extract it either experimentally or theoretically. The uncertainty between different theoretical methods $^{13,54}$ attempting to estimate the value of $U$ is quite substantial, the interaction strength ranging from 3.2 to 6 eV.

It should be noticed that although this choice of parameters is consistent with insulating behavior of this system it might have limited validity in the real system at low doping. Since $La_{1-x}Sr_{x}TiO_{3}$ is known to undergo several structural transformations upon doping and in particular the structure of $LaTiO_{3}$ is distorted away from the cubic perovskite structure and in fact the distortion lifts the degeneracy of the $t_{2g}$ orbitals and the ground-state orbital is a narrow nondegenerate $d_{xy}$ orbital. Hence one might expect that the Mott-Hubbard transition in this system would be better described in a one-band model ($x$$<$0.08). At larger dopings ($x$$>$0.08) it is, however, clear that the system is degenerate and thus our model can be expected to give a reasonably good description in the larger doping range. In the present paper we do not consider the effect of lifting the degeneracy due to Jahn-Teller distortion; rather we explore the threefold-degenerate Hubbard model in the whole region of doping interval including $n$=1 point.

The kinetic part of the model Hamiltonian has been obtained from tight-binding LMTO ASA calculations. The band structure of the compound around the Fermi level consists of the threefold-degenerate Ti $3d$ $t_{2g}$ band, hosting one electron, which is well separated from an empty Ti $3d$ $e_{g}$ band located above the $t_{2g}$ band. A rather broad gap below $t_{2g}$ separates Ti $3d$ and completely filled $2p$ oxygen band. Hence it is quite straightforward to make the tight-binding fit of the $t_{2g}$ band to be used in the impurity solvers. To achieve asymmetry in the tight-binding DOS one needs to take into account the next-nearest-neighbor, so-called, $t'$ term on Ti sublattice. The dispersion that we obtained from the fit is the following: $\epsilon_{\mathbf{k}}$=$2t$(cos$k_{x}$+cos$k_{y}$)+$2t'$cos($k_{x}$+$k_{y}$)+$2t_{\perp}$cos$k_{z}$, where $t$=-0.3297, $t'$=-0.0816, $t_{\perp}$=-0.0205 in eV. The $t_{2g}$ part of the $LaTiO_{3}$ DOS (dotted line) and its fit (solid line) are presented in Fig. 3. We also added one more curve in Fig. 3 corresponding to a semicircular DOS which we will use for a different kind of benchmarking of our approach.

The results for a few chosen doping values computed at temperature equal to 300 K are displayed in Table IIwhere we have also displayed the experimental results from Ref. 40.

It is quite noteworthy that for the two lowest doping values in the table the LDA and the experiment are in a good


![](./images/812117108564426752_3.jpg)

FIG. 3. (Color online) LDA DOS of LaTiO₃ (dotted line with star symbols), its tight-binding fit (solid line) and semicircular DOS (dot-dashed line). Arrows indicate Fermi-level position for filling n=0.8 (the first one is for the semicircular DOS, and the second one is for the tight-binding fit).

agreement. For higher values of doping, however, the experimental values are about twice as large as the LDA values. The good agreement at low doping should be regarded as mostly accidental since the experimental data for doping values less than 5% show the holelike thermopower, which the LDA, of course, will not be able to reproduce.

### C. Summary of DMFT results
In the previous section we described how to obtain the Hubbard-like Hamiltonian with the kinetic part coming from downfolded bands and the interaction part defined by renormalized Coulomb repulsion. In this section we study the influence of interactions on physical properties of the system. The method used to solve the Hamiltonian is the dynamical mean-field theory which was described in Sec. II.

So, the main effect expected from electron interactions is to reproduce the Mott transition when the system approaches an integer filling. One can see indications of the MIT in filling $n$, dependencies of the chemical potential $\mu$, and quasiparticle residue $Z$. The MIT is clearly seen by a jump of the $\mu$ versus $n$ dependence (the chemical potential changes while the filling remains the same) plotted in Fig. 4 and also by the vanishing energy scale seen in the $Z$ versus $n$ dependence in Fig. 5 while approaching the Mott transition.

In Fig. 4 we plot the chemical potential against filling around filling $n=1$ for three values of Coulomb interaction $U=3$, 4, and 5 in units of the half bandwidth $D$, and for two shapes of the DOS (semicircular and tight binding). We notice here that both semicircular and realistic DOSs are renormalized in such a way that they run in the interval $[-D,D]$ with the norm equal to 1. The first two upper curves presented in Fig. 4 correspond to $U=3$. The upper curve is obtained using the tight-binding DOS and the lower one comes from the semicircular DOS. The first curve is nearly a straight line crossing $n=1$ point while the line corresponding to the semicircular DOS is about to make a jump which is clearly presented in the behavior of $U=4$ line. The jump becomes even more pronounced for $U=5$ and both semicircular and tight-binding DOS. Let us notice that the absolute value of the jump for the tight-binding DOS is smaller than for the semicircular DOS. From this figure one can easily conclude that the critical interaction when insulating behavior appears in the system should be somewhere between $U=3$ and 4 and closer to the second value (the final conclusion about the insulating behavior one can make from the energy dependence of the DOS on the real axis).

<table>
<caption>TABLE II. The thermopower $S$ of La₁₋ₓSrₓTiO₃ at 300 K measured in units of $\mu$V/K is computed using the LDA band structure. The experimental data are taken from Ref. 40.</caption>
<thead>
  <tr>
    <th rowspan="2"></th>
    <th colspan="5">Doping (%)</th>
  </tr>
  <tr>
    <th>5</th>
    <th>25</th>
    <th>50</th>
    <th>75</th>
    <th>80</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Experiment</td>
    <td>−5.2</td>
    <td>−9.3</td>
    <td>−18.3</td>
    <td>−29.4</td>
    <td>−41.2</td>
  </tr>
  <tr>
    <td>LDA data</td>
    <td>−5.6</td>
    <td>−7.8</td>
    <td>−9.3</td>
    <td>−18.2</td>
    <td>−22.8</td>
  </tr>
</tbody>
</table>

![](./images/812117108564426752_4.jpg)

FIG. 4. (Color online) The chemical potential $\mu$ versus filling $n$ for semicircular (sc) and tight-binding (tb) DOS and various values of interaction $U$ at temperature $\beta=16$.

In Fig. 5 we see five curves for the same values of interaction and shapes of the DOS as in the previous graph. As we expected for $U=3$ (both DOS, semicircular and tight binding) at $n=1$ we have a finite value of $Z$. Notice that again (as in the previous plot) the tight-binding DOS shows

![](./images/812117108564426752_5.jpg)

FIG. 5. (Color online) Filling dependence of the quasiparticle residue, $Z$, for semicircular (sc) and tight-binding (tb) DOS and various values of interaction, $U$, at temperature $\beta=16$.


![](./images/812117108564426752_6.jpg)

FIG. 6. (Color online) DOS at the Fermi level, $\rho(E_F)$ [states/(eV unitcell)], vs filling, $n$, for semicircular (sc) and tight-binding (tb) DOS and various values of interaction, $U$. All of the data was computed for $\beta=16$.

more metallic behavior (larger value of $Z$ and a straighter line than in the case of the semicircular DOS). All other values of the interaction clearly show insulating behavior of the system.

So now one can see how electron correlations change the physical properties of the system. Here we recall that the main input to the DMFT QMC or DMFT SUNCA procedure consists of the shape of the DOS (semicircle or tight binding) and the value of the interaction $U$. We will analyze both shapes of DOS for values of $U$ mentioned above.

Using our results presented in Fig. 5 and the behavior of $\rho(E_F)$ presented in Fig. 6 we can calculate the linear coefficient of specific heat $\gamma$. As we saw above, the LDA results differ a lot from experimental values of $\gamma$. Now we want to know whether we can get any improvements by applying DMFT, which changes the quasiparticle residue $Z$ and renormalizes the DOS.

In Fig. 7 we plot the linear coefficient of specific heat against filling for different values of Coulomb repulsion using semicircular and tight-binding DOSs. We notice that for the same repulsion strength the linear coefficient of specific heat for the semicircular DOS is larger than for the tight-binding one, which is a consequence of the larger pinning value in the semicircular DOS. Comparing $U$ dependencies for the semicircular DOS we see that the linear coefficient of specific heat for $U$=3 is a nearly linear function until filling $n$=1, which one can explain by the almost linear dependence of the quasiparticle residue observed in Fig. 5. For $U$=4 and 5 the doping dependence of the linear coefficient of specific heat reproduces the experimental behavior and the only question left is how close theoretical and experimental results are. From the plot we see that in general the results for the semicircular DOS are positioned far from the experimental values while for the tight-binding DOS the experimental curve is just in between the $U$=3 and 5 lines. Hence we can claim a rather good agreement (contrary to the LDA situation) between the DMFT and experimental curves for the whole range of dopings. The divergence of the linear coefficient of specific heat shows a strong $d$-electron effective mass enhancement at the Fermi level while approaching the MIT. $^{43}$ In the case of $U$=5 a small overestimation of the linear coefficient of specific heat for large doping can be explained by 10-15 % inaccuracy in the procedure of the quasiparticle extraction (we define it from the self-energy on Matsubara axis). We could also slightly tune the interaction strength, which probably should be smaller, down to 4. In general the agreement between DMFT QMC results and the experimental ones is quite good.

So we can summarize the linear coefficient of specific heat results by saying that changes in the spectral weight $Z$ are the main source of the improvement of our results for the linear coefficient of the specific heat. Those changes are most remarkable for $U$=5 where $Z$ tends to zero when density approaches the integer filling $n$=1. The diverging behavior of the linear coefficient of specific heat for small doping in the real material can be explained by one of the structural transitions happening in $LaTiO_3$, at doping less than 5% the threefold degeneracy is lifted and we effectively have only a one-band model for which $U$=3 could be large enough to get the MIT transition at integer filling.

### D. Comparison QMC and SUNCA methods

In this section we analyze and compare two impurity solvers, i.e., QMC and SUNCA, as candidates to compute transport properties. Earlier comparisons $^{55}$ of QMC and NCA pointed out that the NCA underestimates the Kondo temperature of the problem. To improve the situation, i.e., put more weight on the quasiparticle peak, we used the SUNCA method. Similar to the case of LDA calculation, in the impurity problem treatment, we also need to make a reasonable compromise between speed and accuracy. It is well known that the QMC impurity solver is very expensive but exact (the only approximation used in the QMC is the Trotter breakup) while the SUNCA is a computationally cheap method but it is based on more approximations. The QMC method works in imaginary-time and Matsubara-frequency domains while the SUNCA works on the real-frequency axis. To compute transport properties one needs the self-energy on the real axis. In the case of QMC calculations it is necessary to make the analytical continuation using the maximum entropy or singular decomposition method to get the self-energy on the real axis as was described in Sec. II B. This is

![](./images/812117108564426752_7.jpg)

FIG. 7. (Color online) The linear coefficient of specific heat $\gamma$ (mJ/mol K$^2$) vs the density for different interaction strengths and DOSs at temperature $\beta=16$.

035120-11

![](./images/812117108564426752_8.jpg)

FIG. 8. (Color online) Filling dependence of the quasiparticle residue $Z$ and the linear coefficient of specific heat $\gamma$ obtained from two impurity solvers: QMC (solid line with stars) and SUNCA (dashed line with circle symbols) for $U$=5, temperature $\beta$=16. Experimental points are given by cross symbols and dot-dashed line is used as a guide for the eye. The tight-binding density of states was used in the self-consistency loop of the DMFT procedure. For comparison we also provide the $Z$ vs $n$ curve obtained with the IPT method for the same parameters as the ones used in the QMC and SUNCA calculations.

the weakest point in the DMFT QMC procedure. DMFT SUNCA working on the real axis has the self-energy right after self-consistency is reached.

As we noticed in the previous subsection the main task of the interaction (read the impurity solver) is to produce the MIT at integer fillings. And one of the criteria of insulating behavior in the system is vanishing quasiparticle weight. In Fig. 8 we compare the quasiparticle residue $Z$ obtained from DMFT QMC and DMFT SUNCA methods as a function of doping for $U$=5 and a realistic DOS. We see that both methods are in a good agreement with each other. We also provide a $Z$ versus $n$ curve calculated using iterative perturbative theory$^{56}$ to see that all three impurity solvers produce the same trend at least qualitatively.

Now we can go further and compare the electron GF on the Matsubara axis. The imaginary axis is a natural space of work for QMC and to compare results with SUNCA we used the Lehmann representation connecting the spectral function on the real axis with the GF on the imaginary axis. The representation is analytical and exact; hence the comparison can be made without any assumptions and approximations or uncertainties which could arise in the case of the analytical continuation provided we wanted to compare results on the real axis.

In Fig. 9 we plot the GF and imaginary parts of the self-energy for temperature $\beta$=16 (the temperature which is mostly used in our calculations) and for 10% and 20% of dopings (they are our usual dopings used in calculations). From Fig. 9 we can conclude that there is quite good agreement between the two methods and therefore we used the SUNCA in our transport calculations where the behavior of the self-energy on the real axis around the Fermi level is very crucial for the transport properties, which are extremely sensitive to the shape, slope, and value of the self-energy at the

![](./images/812117108564426752_9.jpg)

FIG. 9. (Color online) In the two upper panels we compare the energy dependencies of imaginary and real parts of the GF on the Matsubara axis for dopings $n$=0.8 and 0.9 computed using QMC (circles) and SUNCA (solid line) methods. In the lower panels we plot the imaginary parts of the self-energies for the same parameters as in the upper panels. We used the semicircular DOS in the DMFT self-consistency procedure and $U$=5 at temperature $\beta$=16.

Fermi level. The SUNCA plays the role of a "good analytical continuation." Transport properties become more and more sensitive to all the details of the transport function at the Fermi energy with lowering temperature. Taking into account all the comparisons made and calculations done we conclude that the SUNCA is a fast and accurate enough method to compute the transport properties of the compound.

## V. RESULTS OF TRANSPORT CALCULATIONS

### A. Spectral and transport functions in real system

Before doing transport computations it is worth studying the spectral and transport function dependencies on doping and temperature. As we discussed in the previous Sec. IV D we will use the SUNCA as the main method to compute transport properties (one can avoid the analytical continuation procedure in this case). But, at any rate, we also did calculations with the QMC impurity solver and compared the results obtained from the two impurity solvers and described

![](./images/812117108564426752_10.jpg)

FIG. 10. (Color online) Temperature dependence of DMFT density of states for $n$=0.8 and $U$=5. A larger frequency interval is plotted in the inset. Energy is in units of half bandwidth $D$.

![](./images/812117108564426752_11.jpg)

FIG. 11. (Color online) Doping dependence of DMFT density of states for $T$=0.05 and $U$=5. A larger frequency interval is plotted in the inset. Energy is in units of half bandwidth $D$.

differences between them when they were the most noticeable.

In Fig. 10 we plotted the density of states per spin (the lower Hubbard band and quasiparticle peak are shown in the main panel and the inset shows the whole energy range) at filling $n$=0.8 for various values of temperature. Here temperature is measured in units of the half bandwidth $D$=1.35 eV and thus the actual temperature range is quite large with the smallest temperature, corresponding to $T$=0.05, being around 780 K. The highest temperature plotted is equal to 1 but it is still not large enough to make incoherent motion in the system dominant. As we can see temperature changes are quite substantial (the lower Hubbard band nearly disappeared and the quasiparticle peak is shifted toward the upper Hubbard band, indicating the tendency to join the upper Hubbard band and form an incoherent broad bump) but they are still not close enough to reach the incoherent motion state (the upper Hubbard band is changed but still it is very well separated from the quasiparticle (QP) peak—lower Hubbard band creation). This situation is to be expected as we know the QP picture disappears for temperatures higher than the Coulomb repulsion $U$, which is 5 in our case. Hence, for $T\geqslant 5$ one will see only incoherent motion in the system. Let us notice here the difference between SUNCA and QMC where in the last method the spectral density is just a single hump corresponding to purely incoherent carrier dynamics observed already for temperature $\beta$=1. If we start from an incoherent picture and lower temperature, then the incoherent hump splits up and the Hubbard bands start to form. For even lower temperature the lower Hubbard band moves completely below the Fermi surface and the coherent quasiparticle peak appears at the Fermi level. The lower Hubbard band starts to form at $\beta$=4, the QP peak is formed for $\beta\geqslant 10$. For temperature lower than $\beta$=16 the weight of the QP peak nearly does not change. We observe similar behavior of the DOS in the SUNCA where the shape of the QP and the lower Hubbard band change only slightly for temperatures lower than $T$=0.1. The described discrepancies on the real axis between the two methods are entirely in the domain of the analytical continuation (maximum entropy method) which reliably reproduces only the low-energy part. We should notice one more interesting thing in Fig. 10, namely, the temperature dependence of the DOS value at the Fermi level. When this value reaches that of the noninteracting DOS we say that the pinning condition is obeyed. The temperature when the pinning condition is reached is called the pinning temperature and it strongly depends on doping. For filling $n$=0.8 as we can conclude from Fig. 10 the pinning temperature is about 0.1.

![](./images/812117108564426752_12.jpg)

FIG. 12. (Color online) Temperature dependence of imaginary part of the self-energy for $n$=0.8. In the inset the real part of the self-energy is shown for the same temperatures. Energy is in units of half bandwidth $D$.

In Fig. 11 we plotted the density of states per spin for $T$=0.05 and different values of doping. The choice of temperature was dictated by the consideration that it should be lower than the pinning temperature for the largest filling presented. With increased doping the quasiparticle peak broadens and its spectral weight increases a lot while the weight of the lower Hubbard band changes a little (doping changes are 10–20%). All the weight that the QP peak gained came from the upper Hubbard band (see inset in Fig. 11 where a larger energy interval is presented). With increased doping the system becomes less and less correlated and in the limit of 100% doping the Hubbard bands vanish and the quasiparticle peak transforms into a free and an empty tight-binding band. With decreasing doping the QP peak vanishes and the system becomes insulating for the repulsion $U$=5.

![](./images/812117108564426752_13.jpg)

FIG. 13. (Color online) Doping dependence of imaginary part of the self-energy for $T$=0.1. In the inset the real part of the self-energy is shown for the same dopings. Energy is in units of half bandwidth $D$.

![](./images/812117108564426752_14.jpg)

FIG. 14. (Color online) Temperature dependence of the transport function for $n=0.8$. In the inset a larger frequency interval is used. Energy is in units of half bandwidth $D$.

In Figs. 12 and 13 we presented the dependence of the imaginary part (main panels) and real part (inset) of the self-energy on temperature and doping for the same temperatures as in Fig. 10, and the same dopings as in Fig. 11. In Fig. 12 we see nice quadratic behavior of the self-energy for low temperatures with the minimum at around the chemical potential (zero in our case) which then rises and shifts with the temperature to the right-hand side. The real part of the self-energy reflects the quasiparticle residue $Z$, and with lowering the temperature the QP residue increases and approaches the pinning value. The doping dependence of the imaginary part of the self-energy shows that the self-energy at the chemical potential decreases with increased doping. This is exactly what one should expect for a system close to the free-electron state where a more quadratic and smaller imaginary part of the self-energy is anticipated. The real part of the self-energy shows the same tendency with increasing doping as in the case of the temperature dependence: the curve that crosses the Fermi level becomes more flat. At zero doping it should have a zero derivative at the chemical potential signaling about $Z=1$. The self-energy is an extremely important characteristic of the system as it is the only quantity that enters into transport calculations. Using the self-energy one computes the transport functions, the main ingredient of all transport equations.

![](./images/812117108564426752_15.jpg)

FIG. 15. (Color online) Doping dependence of the transport function for temperature $T=0.1$. In the inset a larger frequency interval is shown. Energy is in units of half bandwidth $D$.

![](./images/812117108564426752_16.jpg)

FIG. 16. (Color online) The temperature behavior of thermopower at different dopings.

In Figs. 14 and 15 we plot the temperature and density dependencies of the transport function for the same set of parameters as we used for Figs. 10 and 11, respectively. One can reveal similar features as in the density of states: in the transport function behavior one clearly identifies contributions coming from the upper Hubbard band and the lower one plus the QP peak. But the most important contribution to transport properties at low temperatures comes from the energy region around the Fermi level. As can be seen from Eq. (28) the transport coefficients are entirely defined by the transport function integral in an energy window that depends on temperature. These equations allow one at least qualitatively to define the sign of the thermopower for small temperatures. If the slope of the transport function is increasing then the thermopower should be negative and for the other slope it should be positive. For a large energy window the sign of the thermopower will strongly depend on the shape of the transport function and its position relative to the chemical potential.

### B. Transport parameters

In Figs. 16-19 we plotted the transport parameters of the studied system for different densities against temperature.

![](./images/812117108564426752_17.jpg)

FIG. 17. (Color online) The temperature of the resistivity at three different dopings.

![](./images/812117108564426752_18.jpg)

FIG. 18. (Color online) The Lorentz ratio vs temperature for three different dopings.

The transport parameters under consideration are the following: $\rho$ denotes the electrical resistivity, $\kappa$ is the thermal conductivity, $S$ is the thermopower, and $L$ is the Lorentz ratio. The resistivity behavior, as it was found experimentally$^{45}$ and theoretically, is a quadratic function in a relatively low-temperature interval becoming linear at higher temperatures. The quadratic temperature dependence of the electrical resistivity is reminiscent of the strong electron-electron scattering which predominates in the electron-phonon scattering process. The thermal conductivity behaves like $T^{-2}$ till temperatures of the order $10^{3}-10^{4}$, which are relatively large temperatures.$^{52}$ The Lorentz number tends to a constant value around $16-17$ nW $\Omega/\text{K}^{2}$, indicating that the character of the low-temperature scattering is Fermi liquid. The thermopower behavior is a little bit more complicated. At low temperature the thermopower linearly tends to zero. It is very hard for us to distinguish the doping dependence for relatively small temperatures as all changes lie between the error bars which are in our case larger than the difference between the lower and higher thermopower curves presented in the figure. The reason for large errors lies in a very small value of the imaginary part of the self-energy which we have to deal with on lowering the temperature and this situation is very challenging for the used impurity solvers. For higher temperatures (higher than 1000 K) we are certain of the thermopower behavior as there are no problems with the self-energy determination in this temperature range. With increasing temperature we observe a local maximum in the temperature interval $(5\times 10^{3})-(2\times 10^{4})$. We associate it with increasing temperature cutoff [see Eq. (28)], which is large enough to take into account the right-hand side slope of the central part in the transport function. Or in other words the local maximum in the thermopower in some way mimics the behavior of the transport function (the hump around the chemical potential). At any particular temperature the thermopower has a bit more complicated behavior. But generally it is growing with vanishing doping and for lower than 10% doping one could even get a positive thermopower which first becomes positive at temperatures around 5000 K (see the $n=0.9$ thermopower curve) and then the positiveness will propagate to smaller temperatures.

In Fig. 16 along with theoretical curves we plot the experimental data (taken from Fig. 8 in Ref. 57) for filling $n=0.5$ in a rather large temperature interval (200-1000 K). We should notice here that the majority of experimental results$^{40,57}$ for doped LaTiO$_{3}$ are published for temperatures less than 300 K which is a rather hard task to deal with numerically for the reason we pointed out above. The largest temperature interval used experimentally we found in Ref. 57. To our satisfaction the results obtained are very close to the experimental ones. Moreover, we capture correctly the general trend with temperature, which is a linear dependence for temperatures as high as 800-1000 K and then we see an experimental tendency to change the curvature of the slope to one similar to the $n=0.7$ case plotted in Fig. 16. The theoretical thermopower results are quite encouraging. For temperatures higher than 1000 K the curves obtained could be considered as our predictions for the future experiments.

From the results presented we see that the thermopower behavior (which we also treated as electronic) is accurate within 30% in absolute value. One would expect that the thermopower could become positive with decreasing doping in the way it is experimentally observed. We also could obtain it provided we do a much more delicate and hard job taking into account the structural transition happening at doping $x<0.05$ as in this case we effectively should have a one-band model instead of a threefold-degenerate one. But this is beyond the scope of the present work. Close to the MIT we have a strongly asymmetric DOS and transport functions which in the case of integer filling $n=1$ will produce a positive sign of the thermopower. The reason for this is the position of the negative slope (right-hand side) of the lower Hubbard band, which is closer to the Fermi energy than the upper one and hence has a dominant contribution to the transport properties of the system.

![](./images/812117108564426752_19.jpg)

FIG. 19. (Color online) The temperature behavior of the thermal conductivity for different dopings.

Analyzing Figs. 16-19 as functions of doping for a fixed temperature we can see that all curves behave in the way one would expect. The resistivity is growing with decreasing doping as the system approaches the MIT while the thermal conductivity and the Lorentz number are decreasing.

The biggest discrepancy between theory and experiment is in predicting the resistivity at low temperatures. We believe that the main source of the disagreement is due to the SU($N$) approximation neglecting the Hund's coupling $J$ and crystal field splitting between $t_{2g}$ bands. Partial lifting of the degeneracy of the atomic ground state by including the

035120-15

OUDOVENKO *et al.*
PHYSICAL REVIEW B **73**, 035120 (2006)

Hund’s $J$ results in increase of $T_k$ and consequently in increase of resistivity bringing it closer to the experimental data. The second reason for disagreement might be due to limitations of the impurity solvers to access experimental temperatures.

So it would be fair to say that in our calculations we can catch at least semiqualitative behavior of the transport parameters. The electrical resistivity would require an additional treatment to get quantitatively better agreement while the thermopower calculations deserve quantitative comparison with experiment and can be accurate enough providing 20–30 % agreement with experiment.

## VI. CONCLUSION

In the paper we proposed and implemented a method for calculation of thermoelectrical properties in real materials. Dynamical mean-field theory was used to take into account strong electron interactions and thereby bring the self-energy into first-principles calculations. Taking a rather generic density of states for many strongly correlated materials, we obtained temperature and doping dependencies for such thermoelectric properties as electrical resistivity, thermal conductivity, thermopower, and the Lorentz ratio.

We believe that this method will be a powerful tool for the analysis of existing experimental data and for guiding us to a proper physical understanding of thermoelectrical phenomena. This is especially important not only for correlated materials such as Mott-Hubbard insulators and high-temperature superconductors but also for simple materials like the noble metals which display thermoelectric behavior that still lacks a proper description. In addition we hope this method will aid in the search for new materials with better thermoelectrical performance by allowing for *ab initio* predictions of thermoelectric properties.

## ACKNOWLEDGMENTS

We greatly acknowledge usage of the Cray T3E-900 computer at NERSC, Berkeley, as well as Rutgers Beowulf computational cluster which allowed us to make the present computations feasible.

## APPENDIX A: LDA HAMILTONIAN IN NONORTHOGONAL BASE

In LDA one has to solve the well-known Kohn-Sham equation
$$
\left(-\nabla^{2}+V\right) \Psi_{\mathbf{k} j}=\epsilon_{\mathbf{k} j} \Psi_{\mathbf{k} j}. \tag{A1}
$$

The eigenfunctions $\Psi_{\mathbf{k} j}$ are expanded in a basis set for example the LMTO basis $\chi_{\mathbf{k}}^{\alpha}(\mathbf{r})$ which is not necessarily orthogonal as
$$
\Psi_{\mathbf{k} j}=\sum_{\alpha} A_{\mathbf{k} j}^{\alpha} \chi_{\alpha \mathbf{k}}. \tag{A2}
$$

Substituting Eq. (A2) in Eq. (A1) we obtain
$$
H_{L D A}^{\alpha \beta}(\mathbf{k}) A_{\mathbf{k} j}^{\beta}=\epsilon_{\mathbf{k} j} O_{\mathbf{k}}^{\alpha \beta} A_{\mathbf{k} j}^{\beta}.
$$

## APPENDIX B: MANY-BODY THEORY IN A NONORTHOGONAL BASIS

Our starting point here is a representation of the kinetic term of the Hamiltonian in an orthogonal basis $\{|i\rangle\}$ and we assume that this basis is related to the nonorthogonal basis $\{|\alpha\rangle\}$ by the transformation matrix
$$
|i\rangle=\sum_{\alpha}|\alpha\rangle S_{\alpha i} \quad \text { and } \quad\langle i|=\sum_{\alpha}\langle\alpha| S_{\alpha i}^{*}=\sum_{\alpha} S_{i \alpha}^{+}\langle\alpha|. \quad(\mathrm{B} 1)
$$

The Hamiltonian is now written as
$$
\begin{aligned}
H=\sum_{i j}\langle i|H| j\rangle c_{i}^{\dagger} c_{j}=\sum_{i j \alpha \beta} S_{i \alpha}^{+}\langle\alpha|H| \beta\rangle S_{\beta j} c_{i}^{\dagger} c_{j}=\sum_{\alpha \beta} H_{\alpha \beta} c_{\alpha}^{\dagger} c_{\beta}. \\
(\mathrm{B} 2)
\end{aligned}
$$

The last term in the equation above is a requirement that we place on the creation and destruction operators in the nonorthogonal basis and thus we find that
$$
c_{\alpha}^{\dagger}=\sum_{i} c_{i}^{\dagger} S_{i \alpha}^{\dagger} \quad \text { and } \quad c_{\alpha}=\sum_{j} S_{\alpha j} c_{j}. \quad \text { (B3) }
$$

The nonorthogonality of the basis is encoded in the overlap matrix $O_{\alpha \beta}=\langle\alpha \mid \beta\rangle$ and this matrix can be related to the transformation matrix $S$ in the following manner:
$$
\delta_{i j}=\langle i \mid j\rangle=\sum_{\alpha \beta} S_{i \alpha}^{\dagger}\langle\alpha \mid \beta\rangle S_{\beta j}=\sum_{\alpha \beta} S_{i \alpha}^{\dagger} O_{\alpha \beta} S_{\beta j}. \quad(\mathrm{B} 4)
$$

Therefore we see that the overlap matrix is defined by
$$
O=\left(S S^{\dagger}\right)^{-1}. \quad \text { (B5) }
$$

We should note here that the creation operator $c_{\alpha}^{\dagger}$ does not create a particle in the state $|\alpha\rangle$ when acting on the vacuum, since as we see
$$
\begin{aligned}
c_{\alpha}^{\dagger}|0\rangle=\sum_{i} c_{i}^{\dagger} S_{i \alpha}^{\dagger}|0\rangle=\sum_{i}|i\rangle S_{i \alpha}^{\dagger}=\sum_{i \beta}|\beta\rangle S_{\beta i} S_{i \alpha}^{\dagger}=\sum_{\beta}|\beta\rangle O_{\beta \alpha}^{-1}. \\
(\mathrm{B} 6)
\end{aligned}
$$

It is, however, worth noting that this state has unit overlap with the state $|\alpha\rangle$ and zero overlap with all of the other basis states. The commutation relationships of these operators are the same as for regular Fermi operators except that we get
$$
\left\{c_{\alpha}^{\dagger}, c_{\beta}\right\}=\sum_{i j} S_{\beta j}\left\{c_{i}^{\dagger}, c_{j}\right\} S_{i \alpha}^{\dagger}=S_{\beta i} S_{i \alpha}^{\dagger}=O_{\beta \alpha}^{-1}. \quad(\mathrm{B} 7)
$$

Let us finally obtain the expression for the Green's function in the nonorthogonal basis,
$$
G_{\alpha \beta}(\tau)=-\left\langle c_{\alpha}(\tau) c_{\beta}^{\dagger}(0)\right\rangle. \quad \text { (B8) }
$$

The easiest way to calculate this Green’s function is by looking at the Lagrangian for the system in the orthogonal basis and then simply transform it into the nonorthogonal one. We have (summation over repeated indices implied)

035120-16

$$
\begin{aligned}
\mathcal{L} & =c_{i}^{\dagger} \frac{\partial}{\partial \tau} c_{i}-c_{i}^{\dagger} H_{i j} c_{j}=S_{i \beta}^{-1} c_{\alpha}^{\dagger} \frac{\partial}{\partial \tau} c_{\beta}\left(S^{\dagger}\right)_{\alpha i}^{-1}-c_{\alpha}^{\dagger} H_{\alpha \beta} c_{\beta} \\
& =c_{\alpha}^{\dagger} O_{\alpha \beta} \frac{\partial}{\partial \tau} c_{\beta}-c_{\alpha}^{\dagger} H_{\alpha \beta} c_{\beta}.
\end{aligned}
\qquad (B9)
$$

The free Matsubara Green's function can now be obtained using Fourier transformation of the operators in the Lagrangian and then the inverse of the Green's function $G_{\alpha \beta}^{0}(i \omega)$ is simply the term multiplying $c_{\alpha}^{\dagger} c_{\beta}$. Thus we obtain
$$G_{\alpha \beta}^{0}(\omega)=[i \omega O-H]_{\alpha \beta}^{-1}. \qquad (B10)$$

The renormalized Green's function one gets as in the orthogonal case by adding the self-energy to the Hamiltonian and thus
$$G(i \omega)=[i \omega O-H-\Sigma]^{-1}. \qquad (B11)$$

We should remark here that these Green's functions do not share the same properties as their cousins in the orthogonal bases do and in particular the total density is not given by trace of $G(\tau=0^{-})$. To see that we go back to the orthogonal basis where we know how things work and write the density operator as
$$\rho=\sum_{i} c_{i}^{\dagger} c_{i}=\sum_{i \alpha \beta} S_{i \beta}^{-1} c_{\alpha}^{\dagger} c_{\beta}\left(S^{\dagger}\right)_{\alpha i}^{-1}=\sum_{\alpha \beta} O_{\alpha \beta} c_{\alpha}^{\dagger} c_{\beta}. \quad \text { (B12) }$$

Thus the total density of electrons in the system is
$$\begin{aligned}
n_{t o t}=\langle\rho\rangle=\sum_{\alpha \beta} O_{\alpha \beta}\left\langle c_{\alpha}^{\dagger} c_{\beta}\right\rangle=\sum_{\alpha \beta} G_{\beta \alpha}\left(\tau=0^{-}\right) O_{\alpha \beta}. & \\
& \text { (B13) }
\end{aligned}$$

We should note in particular that this means that there seems to be no good way of assigning a density to a particular orbital in the nonorthogonal case.

## APPENDIX C: SPLINES AND FOURIER TRANSFORMATIONS

### 1. Direct Fourier transformation

As we know in the QMC program we need to do direct and inverse Fourier transformations. The direct Fourier transformation is done exactly, i.e., first we obtain coefficients of the cubic spline exploiting physical properties of the GF and then make an analytical Fourier integration knowing the form of the splined curve. The cubic spline interpolation formula reads
$$G(\tau)=a_{i}+b_{i}\left(\tau-\tau_{i}\right)+c_{i}\left(\tau-\tau_{i}\right)^{2}+d_{i}\left(\tau-\tau_{i}\right)^{3}, \quad \tau \in\left[\tau_{i}, \tau_{i+1}\right],$$
where the coefficients $a_{i}, b_{i}, c_{i}, d_{i}$ are equal to the values of the function, its first, second, and third derivatives at knot $i$, i.e., $a_{i}=G(\tau_{i}), b_{i}=G^{\prime}(\tau_{i}), c_{i}=G^{\prime \prime}(\tau_{i}), d_{i}=G^{\prime \prime \prime}(\tau_{i})$.

Or in terms of the GF values, $G_{i}=G(\tau_{i})$, and its second derivative, $M_{i}=G^{\prime \prime}(\tau_{i})$, only
$$a_{i}=G_{i},$$

$$b_{i}=\frac{G_{i+1}-G_{i}}{h}-\frac{2 M_{i}+M_{i+1}}{6} h,$$

$$c_{i}=\frac{M_{i}}{2},$$

$$d_{i}=\frac{M_{i+1}-M_{i}}{6 h}. \qquad (C1)$$

From the equations above we see that one needs to know the second derivatives $M_{i}$, using tabulated values of the GF $G_{i}$, in order to get the cubic spline interpolation. To obtain the $M_{i}$ coefficients we use the conditions of smoothness of the first derivative and continuity of the second one. As a result we have $L+1$ equations for $L+3$ unknowns,
$$\left[\begin{array}{ccccc}
2 & \lambda_{0} & & & 0 \\
\mu_{1} & 2 & \lambda_{1} & & & \\
& \mu_{2} & \cdot & \cdot & & \\
& & \cdot & \cdot & \cdot & \\
& & & \cdot & \cdot & 2 & \mu_{n-1} \\
0 & & & & & \mu_{n} & 2
\end{array}\right]\left[\begin{array}{c}
M_{0} \\
M_{1} \\
\cdots \\
\cdots \\
M_{n}
\end{array}\right]=\left[\begin{array}{c}
d_{0} \\
d_{1} \\
\cdot \\
\cdot \\
\cdot \\
d_{n}
\end{array}\right],$$
where $L$ is the number of time slices. In addition to $L+1$ $M_{0},..., M_{n}, n=0,..., L$, unknowns $d_{0}$ and $d_{n}$ also should be provided. The last two unknowns entirely depend on the boundary conditions which we have to specify in order to have a unique solution of Eq. (C2). If one knows the first derivatives at the end points then $d_{0}$ and $d_{n}$ are defined through
$$\lambda_{0}=1, \quad d_{0}=\frac{6}{h}\left(\frac{G_{1}-G_{0}}{h}-G_{0}^{\prime}\right),$$

$$\mu_{0}=1, \quad d_{n}=\frac{6}{h}\left(G_{n}^{\prime}-\frac{G_{n}-G_{n-1}}{h}\right),$$
and $d_{i}=(3 / h)[(G_{i+1}-G_{i}) / h-(G_{i}-G_{i-1}) / h], \ \lambda_{i}=\mu_{i}=\frac{1}{2}, \ $ for $i \in[1, n-1]$. More detailed derivations of the above formulas can be found in Ref. 58.

We can reduce numbers of unknowns just putting $M_{0}$ and $M_{n}$ to zero (the so-called natural spline boundary conditions). In this case
$$\lambda_{0}=0, \quad d_{0}=0, \quad \mu_{n}=0, \quad d_{n}=0,$$
and we have the number of unknowns matching the number of equations, $L+1$.

This boundary condition is good enough to compute the FT of the GF in the system at or close to half filling since the second derivative of the Green's function is small in absolute value in this regime. And using the natural spline boundary condition we do not impose a noticeable error. However, away from half filling when the asymmetry of the system grows, along with the amplitude, of one out of the two second derivatives, usage of the natural spline eventually leads to pathological behavior of the self-energy. The signature of this pathology is in the "overshooting" effect $^{59}$ when the self energy at some finite Matsubara frequency, i.e., the imaginary part of the self-energy, becomes positive in some frequency region on the positive Matsubara half axis while it

should be always negative. This, of course, amounts to having negative spectral weight for the self-energy which is something that does not occur for fermionic response functions. The "overshooting" can get especially severe in the limiting cases of small temperatures, small particle densities, or large interaction strength.

So, to avoid the problem with the self-energy and, hence, with the whole procedure of the self-consistency in the DMFT QMC program we need to use the proper boundary conditions. And in this case we have two possibilities to get a unique solution for the system of Eq. (C2) exploiting physical properties of the studied GF: (a) we can provide the first derivatives at both ends separately (in the next section we show how to calculate those derivatives) or (b) we can provide the sum of the first and the sum of the second derivatives at the end points, so called the first and the second moments of the GF.

With the second choice of the boundary conditions (b) the system of equations becomes a three-diagonal one with two off-diagonal elements in the opposite corners of the matrix ($-M_{n-1}$ and $-\frac{1}{2}M_0$):

$$
\begin{align*}
4M_0\ +\ M_1& & -M_{n-1} &=d_0, \\
\frac{1}{2}M_0\ +2M_1\ +\frac{1}{2}M_2& & &=d_1, \\
\frac{1}{2}M_1\ +2M_2\ +\frac{1}{2}M_3& & &=d_2, \\
\frac{1}{2}M_2\ +2M_3\ +\frac{1}{2}M_4& & &=d_3, \\
\ddot{\quad} & \ddot{\quad} & \ddot{\quad} & \vdots \\
& \frac{1}{2}M_{n-3}\ +2M_{n-2}\ \frac{1}{2}M_{n-1} &=d_{n-2}, \\
-\frac{1}{2}M_0& & +\frac{1}{2}M_{n-2}\ +2M_{n-1} &=d_{n-1}, \\
& & &\text{(C3)}
\end{align*}
$$

where $d_0=(6/h)[(G_1-G_0)/h+(G_n-G_{n-1})/h-M^{(1)}]+2M^{(2)}$, $d_{n-1}=(6/h)[(G_n+G_{n-2}-2G_{n-1})/h]-\frac{1}{2}B$, $G_0'+G_n'=M^{(1)}$, $M_0+M_n=M^{(2)}$.

Solving the above system of equations we obtain the spline coefficients $a_i,b_i,c_i,d_i$ and can take the Fourier integral analytically,

$$
\begin{align*}
G_m(\omega_n)=&\int_{\tau_{m-1}}^{\tau_m} d\tau[a+b(\tau-\tau_m) \\
&+c(\tau-\tau_m)^2-d(\tau-\tau_m)^3]e^{(i\tau\omega_n)} \\
=&\frac{e^{i\tau_m\omega_n}(-6d+2ic\omega_n+b\omega_n^2-ia\omega_n^3)}{\omega_n^4} \\
&-\frac{1}{\omega_n^4}[e^{i\tau_{m-1}\omega_n}(-6d+2ic\omega_n-6i\Delta\tau d\omega_n+b\omega_n^2 \\
&-2c\Delta\tau\omega_n^2+3(\Delta\tau)^2d\omega_n^2-ia\omega_n^3+ib\Delta\tau\omega_n^3 \\
&-ic(\Delta\tau)^2\omega_n^3+i(\Delta\tau)^3d\omega_n^3)]. \tag{C4}
\end{align*}
$$

The sum $G_m(\omega_n)$ over $m$ $G(\omega_n)=\sum_{m=1}^L G_m(\omega_n)$, will give us the Fourier integral in frequency space.

### 2. Inverse Fourier transformation

As is well known the Green's function $G(\omega)$ falls off as $1/\omega$ when $\omega\rightarrow\infty$. In the program we deal with a finite number of frequency points and cutting off the $1/\omega$ tail one would make a rather crude approximation as the discontinuity of GF $G(\tau)$ (imaginary-time domain) has been removed. In this situation, the high-frequency tail has to be extracted from the GF $G(\omega)$ and Fourier transformed analytically using the following Fourier relation:

$$
\frac{1}{i\omega_n-\epsilon} \leftrightarrow-[\Theta(\tau)+\zeta n(\epsilon)]e^{-\epsilon\tau}, \tag{C5}
$$

where $n(\epsilon)\equiv1/[\exp\{\beta\epsilon\}-\zeta]$ and $\zeta=\pm1$ depending on whether $\omega_n$ is bosonic or fermionic.

The inverse Fourier transformation for the GF without the tail is made by straightforward summation over Matsubara frequencies. Once it has been done we add the information about the tail using Eq. (C5).

---

## APPENDIX D: MOMENTS

The moments $M^{(k)}$ are nothing else than the expansion of the GF in the frequency domain,

$$
G(\omega)=\sum_{k=0}^N \frac{M^{(k)}}{\omega^{k+1}}. \tag{D1}
$$

Another definition of the $k$-degree moment is the following:

$$
M^{(k)}=\int_{-\infty}^{+\infty} d\omega\ \omega^k\rho(\omega), \tag{D2}
$$

where $\rho(\omega)$ is the density of states.

The moments $M^{(k)}$ can be bound to a sum of GFs and the sum of its derivatives in imaginary-time space as

$$
(-1)^{k+1}[G^{(k)}(0^+)+G^{(k)}(\beta^-)]=M^{(k)}, \tag{D3}
$$

where $k=0,\dots,N$.

To show this one needs to take the Fourier integral in parts

$$
\begin{align*}
G(i\omega_n)=&\int_0^\beta e^{i\omega_n\tau}G(\tau)d\tau \\
=&\sum_{k=0}^N \frac{(-1)^{k+1}[G^{(k)}(0^+)+G^{(k)}(\beta^-)]}{(i\omega_n)^{k+1}} \\
&+\frac{(-1)^{N+1}}{(i\omega_n)^{N+1}}\int_0^\beta e^{i\omega_n\tau}\frac{\partial^{N+1}G(\tau)}{\partial\tau^{N+1}}d\tau. \tag{D4}
\end{align*}
$$

So, to solve the system of Eq. (C3) we need to adhere to the proper boundary conditions which are expressed through the various moments of the Green's function. What we need finally is to provide the first three moments $M^{(0)},M^{(1)},M^{(2)}$. The first moment for the Green's function is equal to 1, the second moment proportional to the chemical potential in the system and the third one is a little bit more complicated and contains a density-density correlator. To show that we start with the single-impurity Anderson model which reads

$$
\begin{aligned}
H_{S I A M}= & \sum_{k \alpha} \varepsilon_{k \alpha} c_{k \alpha}^{\dagger} c_{k \alpha}+\sum_{\alpha}\left(\varepsilon_{\alpha}+\frac{1}{2} \sum_{\alpha^{\prime} \neq \alpha} U_{\alpha^{\prime} \alpha}\right) f_{\alpha}^{\dagger} f_{\alpha} \\
& +\sum_{k \alpha} V_{k \alpha}\left(f_{\alpha}^{\dagger} c_{k \alpha}+c_{k \alpha}^{\dagger} f_{\alpha}\right) \\
& +\sum_{\alpha<} \sum_{\alpha^{\prime}} U_{\alpha \alpha^{\prime}}\left(n_{\alpha} n_{\alpha^{\prime}}-\frac{1}{2}\left(n_{\alpha}+n_{\alpha^{\prime}}\right)\right),
\end{aligned}
$$

where $\tilde{\varepsilon}_{\alpha}=\varepsilon_{\alpha}+\frac{1}{2} \sum_{\alpha \neq \alpha^{\prime}} U_{\alpha^{\prime} \alpha}$. The first three moments are obtained from the following commutators:
$$
M^{(k)}=\left\langle\left\{\mathcal{L}^{k} f_{\alpha} ; f_{\alpha}^{\dagger}\right\}_{+}\right\rangle,
$$

where $\mathcal{L O}=[\mathcal{O}, \mathcal{H}]$ denotes the commutator of operator $\mathcal{O}$ with the Hamiltonian, and $\{\cdots\}_{+}$is the anticommutator. After some algebra one finds the following expressions for the moments:
$$
M^{(0)}=\left\langle\left\{f_{\alpha}, f_{\alpha}^{\dagger}\right\}\right\rangle=1,
$$

$$
M^{(1)}=\left\langle\left\{\left[f_{\alpha}, H\right], f_{\alpha}^{\dagger}\right\}\right\rangle=\tilde{\varepsilon}_{\alpha}+\sum_{\alpha^{\prime} \neq \alpha} U_{\alpha \alpha^{\prime}}\left(n_{\alpha^{\prime}}-\frac{1}{2}\right),
$$

$$
\begin{aligned}
M^{(2)}= & \left\langle\left\{\left[\left[f_{\alpha}, H\right], H\right], f_{\alpha}^{\dagger}\right\}\right\rangle \\
= & \left\langle\left\{\left[f_{\alpha}, H\right],\left[H, f_{\alpha}^{\dagger}\right]\right\}\right\rangle \\
= & \left\langle\tilde{\varepsilon}_{\alpha}^{2}+2 \tilde{\varepsilon}_{\alpha} \sum_{\alpha^{\prime} \neq \alpha} U_{\alpha \alpha^{\prime}}\left(n_{\alpha^{\prime}}-\frac{1}{2}\right)\right. \\
& \left.+\sum_{\alpha^{\prime}, \alpha^{\prime \prime} \neq \alpha} \sum U_{\alpha \alpha^{\prime}} U_{\alpha \alpha^{\prime \prime}}\left(n_{\alpha^{\prime}}-\frac{1}{2}\right)\left(n_{\alpha^{\prime \prime}}-\frac{1}{2}\right)+\sum_{k} V_{k \alpha}^{2}\right\rangle,
\end{aligned}
$$

where $\sum_{k} V_{k \alpha}^{2}=M_{0}^{2}-\left(M_{0}^{1}\right)^{2}$, and the moments $M_{0}^{i}$ are defined by Eq. (D2) with $\rho(\omega)=D(\omega)$, where $D(\omega)$ is the noninteracting DOS.

Summing up similar terms in the $\mathrm{SU}(N)$ approximation we get
$$
M^{(1)}=\varepsilon_{\alpha}+(2 N-1) U n, \quad \text { (D7) }
$$

$$
M^{(2)}=\varepsilon_{\alpha}^{2}+2 \varepsilon_{\alpha}(2 N-1) U n+U^{2}[(2 N-1) n+\langle n n\rangle]+\sum_{k} V_{k \alpha}^{2},
$$

where $n$ is the filling per band and per spin, $n=(1 / 2 N) \Sigma_{\alpha} n_{\alpha}$, and the double occupancy is defined as $\langle n n\rangle=\sum_{\alpha \neq \alpha^{\prime}}\left\langle n_{\alpha} n_{\alpha^{\prime}}\right\rangle$.

The second way to make the correct cubic spline as we mentioned before in Appendix C 1 is to provide the first derivatives at both ends of the imaginary-time interval (the boundary conditions). To find the first derivatives at the ends one can use the following definition of the first derivatives of finite-temperature GF:
$$
-\frac{\partial}{\partial \tau}\left\langle T_{\tau} f_{\alpha}(\tau) f_{\alpha}^{\dagger}(0)\right\rangle=-\left\langle T\left[H, f_{\alpha}\right] f_{\alpha}^{\dagger}\right\rangle=G_{\alpha}^{\prime}\left(0^{+}\right).
$$

Using as the Hamiltonian $H=H_{S I A M}$ we can easily obtain the derivatives at the ends:
$$
\begin{aligned}
G_{\alpha}^{\prime}\left(0^{+}\right)= & \varepsilon_{\alpha}\left(1-n_{\alpha}\right)+\left\langle\sum_{k} V_{k \alpha} c_{k \alpha} f_{\alpha}^{\dagger}\right\rangle \\
& +\sum_{\alpha^{\prime} \neq \alpha} U_{\alpha \alpha^{\prime}}\left(n_{\alpha^{\prime}}-\left\langle n_{\alpha^{\prime}} n_{\alpha}\right\rangle\right),
\end{aligned}
$$

$$
\begin{aligned}
G_{\alpha}^{\prime}\left(\beta^{-}\right)=\varepsilon_{\alpha} n_{\alpha}+\left\langle\sum_{k} V_{k \alpha} f_{\alpha}^{\dagger} c_{k \alpha}\right\rangle+\sum_{\alpha^{\prime} \neq \alpha} U_{\alpha \alpha^{\prime}}\left\langle n_{\alpha^{\prime}} n_{\alpha}\right\rangle, & \text { (D9) }
\end{aligned}
$$

where averages, e.g., $\left\langle\sum_{k} V_{k \alpha} c_{k \alpha} f_{\alpha}^{\dagger}\right\rangle$ can be calculated from the following expression:
$$
\left\langle\sum_{k} V_{k \alpha} c_{k \alpha} f_{\alpha}^{\dagger}\right\rangle=-T \sum_{n} \Delta_{\alpha}\left(i \omega_{n}\right) G_{\alpha}\left(i \omega_{n}\right). \quad \text { (D10) }
$$

In the obtained formulas [Eqs. (D6)-(D10)] we should know the filling $n_{\alpha}$ for each band and spin as well as the density-density correlator $\left\langle n_{\alpha} n_{\alpha^{\prime}}\right\rangle$. The filling we can extract from the GF itself. The calculation of the correlator in the QMC highlights one of the advantages of the method, i.e., the correlator is provided by the QMC itself and one does not need to rely on any additional approximations to obtain it as, e.g., in the case of the multiband IPT method $^{60}$ where the coherent potential approximation is used to get the correlator. At each time slice the density-density correlator is also computed from the GF but in the imaginary-time domain where it is simply a product of two Green's functions in $(\tau, \tau^{\prime})$ space. We should note here that we compute the correlator along with other parameters in the system at each iteration step and once self-consistency is reached we have correctly obtained all the components and parameters in the system. And finally, with a small enough imaginary time step $\Delta \tau$ one can completely avoid the "overshooting" problem, keeping in mind the main limitation of the QMC procedure $U \Delta \tau / 2$ $<1$. In the present computations we choose $\Delta \tau=1 / 4$ which is good enough for the range of parameters we use in the current paper.

## APPENDIX E: TRANSPORT CALCULATIONS: CURRENT DERIVATION

Below we derive the expressions for the currents in a general basis. This is done by extending the gauge-theoretic method developed in Ref. 61. In the nonorthogonal basis the action for the system can be expressed as follows:
$$
S=\int d \tau \sum_{k} c_{k \alpha}^{\dagger}\left(O_{k \alpha \beta} \overleftrightarrow{\partial}_{\tau}+H_{k \alpha \beta}\right) c_{k \beta}. \quad \text { (E1) }
$$

Here $\overleftrightarrow{\partial}_{\tau}=1 / 2\left(\vec{\partial}_{\tau}-\overleftarrow{\partial}_{\tau}\right)$ denotes the antisymmetrized time derivative. The particle and heat currents can now be obtained by considering the invariance of the action under local phase transformation and local translations in time, respectively. In

the orthogonal case one is led to the following expression for
the currents:
$$
\vec{j}=-\left.\frac{\partial H\left[\vec{A}_{p}\right]}{\partial \vec{A}_{p}}\right|_{\vec{A}_{p}=0} \quad \text { and } \quad \vec{Q}=-\left.\frac{\partial H\left[\vec{A}_{h}\right]}{\partial \vec{A}_{p}}\right|_{\vec{A}_{h}=0},
\tag{E2}
$$
where $\vec{A}_{p}$ and $\vec{A}_{h}$ are gauge fields conjugate to the currents
and $H[\vec{A}_{p}]$ and $H[\vec{A}_{h}]$ denote the gauged Hamiltonian, i.e.,
the Hamiltonian with the replacements $\vec{k} \to \vec{k}-\vec{A}_{p}$ and
$\vec{k} \to \vec{k}+\vec{A}_{h} \vec{\partial}_{\tau}$, respectively. This replacement is performed in
both the kinetic and the interaction terms but not in the field
operators. In our case, however, the overlap matrix appearing
in the action depends also on momentum and therefore the
proper generalization of the currents to nonorthogonal basis
will also take the overlap matrix into account. Thus we ob-
tain
$$
\vec{j}=-\left.\frac{\partial\left(O\left[\vec{A}_{p}\right] \vec{\partial}_{\tau}+H\left[\vec{A}_{p}\right]\right)}{\partial \vec{A}_{p}}\right|_{\vec{A}_{p}=0},
\tag{E3}
$$

$$
\vec{Q}=-\left.\frac{\partial\left(O\left[\vec{A}_{h}\right] \vec{\partial}_{\tau}+H\left[\vec{A}_{h}\right]\right)}{\partial \vec{A}_{h}}\right|_{\vec{A}_{h}=0}.
\tag{E4}
$$

Performing these operations leads to the following expres-
sions:
$$
\vec{j}=\sum_{k \alpha \beta}\left(\vec{v}_{k, \alpha \beta} B_{k, \alpha \beta}^{(0)}-\vec{u}_{k, \alpha \beta} B_{k, \alpha \beta}^{(1)}\right),
\tag{E5}
$$

$$
\vec{Q}=\sum_{k \alpha \beta}\left(\vec{v}_{k, \alpha \beta} B_{k, \alpha \beta}^{(1)}-\vec{u}_{k, \alpha \beta} B_{k, \alpha \beta}^{(2)}\right),
\tag{E6}
$$
where we have defined
$$
B_{k, \alpha \beta}^{(n)}=(-1)^{n} c_{k, \alpha}^{\dagger}\left(\vec{\partial}_{\tau}\right)^{n} c_{k, \beta},
\tag{E7}
$$
and
$$
\vec{v}_{k, \alpha \beta}=\frac{1}{\hbar} \vec{\nabla}_{k} H_{k, \alpha \beta}^{0} \quad \text { and } \quad \vec{u}_{k, \alpha \beta}=\frac{1}{\hbar} \vec{\nabla}_{k} O_{k, \alpha \beta},
\tag{E8}
$$
where $H_{k, \alpha \beta}^{0}$ is the tight-binding LMTO Hamiltonian of the
system and $O_{k, \alpha \beta}$ is the overlap matrix that captures the non-
orthogonality of the basis that we are using. The validity of
the expressions above is not restricted to DMFT and they are
in fact true for all density-density interactions such as the
Hubbard interaction. This is because the interaction terms are
gauge invariant and therefore they do not contribute to the
expressions for the currents.

$^{1}$ A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg, Rev.
Mod. Phys. 68, 13 (1996).
$^{2}$ W. Metzner and D. Vollhardt, Phys. Rev. Lett. 62, 324 (1989).
$^{3}$ G. Kotliar, Eur. Phys. J. B 11, 27 (1999).
$^{4}$ V. I. Anisimov et al., J. Phys.: Condens. Matter 9, 7359 (1997).
$^{5}$ A. I. Lichtenstein and M. I. Katsnelson, Phys. Rev. B 57, 6884
(1998).
$^{6}$ Theory of the Inhomogeneous Electron Gas, edited by S. Lun-
dqvist and S. H. March (Plenum, New York, 1983).
$^{7}$ F. Aryasetiawan and O. Gunnarsson, Rep. Prog. Phys. 61, 237
(1998).
$^{8}$ V. I. Anisimov, J. Zaanen, and O. K. Andersen, Phys. Rev. B 44,
943 (1991).
$^{9}$ I. Yang, S. Y. Savrasov, and G. Kotliar, cond-mat/0107063 (un-
published).
$^{10}$ G. Kotliar and S. Savrasov, in New Theoretical Approaches to
Strongly Correlated Systems, edited by A. M. Tsvelik (Kluwer
Academic Publishers, Dordrecht, The Netherlands, 2001).
$^{11}$ J. E. Hirsch and R. M. Fye, Phys. Rev. Lett. 56, 2521 (1986).
$^{12}$ K. Haule, S. Kirchner, J. Kroha, and P. Wölfle, Phys. Rev. B 64,
155111 (2001).
$^{13}$ I. A. Nekrasov et al., Eur. Phys. J. B 18, 133 (2000).
$^{14}$ K. Held et al., Int. J. Mod. Phys. B 15, 2611 (2001).
$^{15}$ D. van der Marel and G. A. Sawatzky, Phys. Rev. B 37, 10674
(1988).
$^{16}$ A. K. McMahan, R. M. Martin, and S. Satpathy, Phys. Rev. B 38,
6650 (1988).
$^{17}$ M. S. Hybertsen, M. Schlüter, and N. E. Christensen, Phys. Rev.
B 39, 9028 (1989).
$^{18}$ J. F. Annett, R. M. Martin, A. K. McMahan, and S. Satpathy,
Phys. Rev. B 40, 2620 (1989).
$^{19}$ O. Gunnarsson, Phys. Rev. B 41, 514 (1990).
$^{20}$ J. Zaanen and G. A. Sawatzky, J. Solid State Chem. 88, 8 (1990).
$^{21}$ V. I. Anisimov and O. Gunnarsson, Phys. Rev. B 43, 7570
(1991).
$^{22}$ O. K. Andersen, Phys. Rev. B 12, 3060 (1975).
$^{23}$ I. Paul and G. Kotliar, cond-mat/0211538 (unpublished).
$^{24}$ V. S. Oudovenko, G. Palsson, S. Y. Savrasov, K. Haule, and G.
Kotliar, Phys. Rev. B 70, 125112 (2004).
$^{25}$ K. Takegahara, J. Phys. Soc. Jpn. 62, 1736 (1992).
$^{26}$ G. Kotliar et al., Rev. Mod. Phys. (to be published).
$^{27}$ M. Jarrell and J. E. Gubernatis, Phys. Rep. 269, 133 (1996).
$^{28}$ G. D. Mahan, Many-Particle Physics, 2nd ed. (Plenum, New
York, 1993).
$^{29}$ E. I. Blount, Solid State Phys. 13, 305 (1962).
$^{30}$ A. J. Millis, J. Electron Spectrosc. Relat. Phenom. 114-116, 669
(2001).
$^{31}$ P. Lambin and J. P. Vigneron, Phys. Rev. B 29, 3430 (1984).
$^{32}$ D. J. Singh and I. I. Mazin, Phys. Rev. B 56, R1650 (1997).
$^{33}$ S. G. Kim, I. I. Mazin, and D. J. Singh, Phys. Rev. B 57, 6199
(1998).
$^{34}$ M. Fornari and D. J. Singh, cond-mat/9904307 (unpublished).
$^{35}$ J. E. Sunstrom IV, S. M. Kauzlarich, and P. Klavins, Chem.
Mater. 4, 346 (1992).
$^{36}$ Y. Maeno, S. Awajo, H. Matsumoto, and T. Fujita, Physica B
165-166, 1185 (1990).

$^{37}$D. A. Crandles, T. Timusk, J. D. Garrett, and J. E. Greedan, Physica C **201**, 407 (1992).

$^{38}$M. Onoda and M. Yasumoto, J. Phys.: Condens. Matter **9**, 3861 (1997).

$^{39}$M. Onoda and M. Kohno, J. Phys.: Condens. Matter **10**, 1003 (1998).

$^{40}$C. C. Hays, J. S. Zhou, J. T. Markert, and J. B. Goodenough, Phys. Rev. B **60**, 10367 (1999).

$^{41}$E. Pavarini *et al.*, cond-mat/0309102 (unpublished).

$^{42}$J. B. Goodenough, Prog. Solid State Chem. **5**, 145 (1971).

$^{43}$K. Kumagai *et al.*, Phys. Rev. B **48**, 7636 (1993).

$^{44}$Y. Okada, T. Arima, Y. Tokura, C. Murayama, and N. Mori, Phys. Rev. B **48**, 9677 (1993).

$^{45}$Y. Tokura *et al.*, Phys. Rev. Lett. **70**, 2126 (1993).

$^{46}$S. A. Carter, T. F. Rosenbaum, P. Metcalf, J. M. Honig, and J. Spalek, Phys. Rev. B **48**, 16841 (1993).

$^{47}$M. J. Rozenberg, G. Kotliar, and X. Y. Zhang, Phys. Rev. B **49**, 10181 (1994).

$^{48}$M. Rozenberg *et al.*, Phys. Rev. Lett. **75**, 105 (1995).

$^{49}$G. Kotliar and H. Kajueter, Phys. Rev. B **54**, R14221 (1996).

$^{50}$H. Kajueter, G. Kotliar, and G. Moeller, Phys. Rev. B **53**, 16214 (1996).

$^{51}$H. Kajueter and G. Kotliar, Int. J. Mod. Phys. B **11**, 729 (1997).

$^{52}$G. Pálsson and G. Kotliar, Phys. Rev. Lett. **80**, 4775 (1998).

$^{53}$D. D. Sarma, S. R. Barman, H. Kajueter, and G. Kotliar, Euro- phys. Lett. **36**, 307 (1996).

$^{54}$I. Solovyev, N. Hamada, and K. Terakura, Phys. Rev. B **53**, 7158 (1996).

$^{55}$M. B. Zolfl *et al.*, Phys. Rev. B **61**, 12810 (2000).

$^{56}$H. Kajueter and G. Kotliar, Phys. Rev. Lett. **77**, 131 (1996).

$^{57}$R. Moos, A. Gnudi, and K. H. Härdtl, J. Appl. Phys. **78**, 5042 (1995).

$^{58}$J. Stoer and R. Bulirsch, *Introduction to Numerical Analysis* (Springer-Verlag, New York, 1980).

$^{59}$V. S. Oudovenko and G. Kotliar, Phys. Rev. B **65**, 075102 (2002).

$^{60}$H. Kajueter, Ph.D. thesis, Rutgers University, Graduate School, New Brunswick, NJ, 1996.

$^{61}$J. Moreno and P. Coleman, cond-mat/9603079 (unpublished).