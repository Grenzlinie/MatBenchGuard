# Probing anharmonic phonons by quantum correlators: A path integral approach
T. Morresi, $^{1}$ L. Paulatto, $^{1}$ R. Vuilleumier, $^{2}$ and M. Casula $^{1, a)}$

$^{1)}$Institut de Minéralogie, de Physique des Matériaux et de Cosmochimie (IMPMC), Sorbonne Université, CNRS UMR 7590, IRD UMR 206, MNHN, 4 Place Jussieu, 75252 Paris, France
$^{2)}$PASTEUR, Département de chimie, École normale supérieure, PSL University, Sorbonne Université, CNRS, 75005 Paris, France

We devise an efficient scheme to determine vibrational properties from Path Integral Molecular Dynamics (PIMD) simulations. The method is based on zero-time Kubo-transformed correlation functions and captures the anharmonicity of the potential due to both temperature and quantum effects. Using analytical derivations and numerical calculations on toy-model potentials, we show that two different estimators built upon PIMD correlation functions fully characterize the phonon spectra and the anharmonicity strength. The first estimator is associated with force-force quantum correlators and gives access to the fundamental frequencies and thermodynamic properties of the quantum system. The second one is instead connected to displacement-displacement correlators and probes the lowest-energy phonon excitations with high accuracy. We also prove that the use of generalized eigenvalue equations, in place of the standard normal mode equations, leads to a significant speed-up in the PIMD phonon calculations, both in terms of faster convergence rate and smaller time-step bias. Within this framework, using ab initio PIMD simulations, we compute phonon dispersions of diamond and of the high-pressure $I4_1$/amd phase of atomic hydrogen. We find that, in the latter case, the anharmonicity is stronger than previously estimated and yields a sizeable red-shift in the vibrational spectrum of atomic hydrogen.

## I. INTRODUCTION
Atomic vibrations are responsible for many thermodynamic and spectral properties of molecules and solids $^{1,2}$, such as the thermal expansion and specific heat, or Raman and infrared spectra, to mention just a few. Furthermore, since the advent of the Bardeen, Cooper, and Schrieffer (BCS) theory, $^{3}$ it is well established that lattice vibrations are fundamental to determine the superconducting materials properties through their coupling with electrons $^{4}$. In particular, the recent exciting discoveries of high-temperature high-pressure hydrogen-based superconductors, such as $H_3S^5$ and $LaH_{10}^6$, have revealed the key role played by hydrogen, the lightest element of the periodic table, in making these materials superconducting. The distinguishing feature of these systems is the presence of strong proton fluctuations and large electron-phonon coupling, which both drive the system into the superconducting state. However, while the impact of nuclear quantum effects (NQE) on the behaviour of hydrogen-based materials is substantial, from the theoretical and computational sides the inclusion of NQE into phonon dispersion still represents a challenge for strongly anharmonic systems.

The standard framework to get lattice and ionic vibrational properties is the harmonic approximation, where the static Born-Oppenheimer (BO) potential is expanded until the second order around the potential minimum, that is the equilibrium configuration of the system. While this approach is the basis for beyond-harmonic theories, it neglects the eventual anharmonicity due to NQE and temperature. For instance, one cannot explain the thermal expansion of solids $^{7}$ within this framework. In order to go beyond the harmonic approximation and take into account interactions between phonons, one can attempt to use perturbation theory $^{8}$. This is however doomed to failure whenever applied to anharmonic systems such as hydrogen-rich materials, because in these cases large atomic fluctuations go well beyond the range of applicability required by theory. To overcome this difficulty, one can use methods based on Molecular Dynamics (MD) simulations, where anharmonic effects can be taken into account non-perturbatively. MD methods have been applied to molecules $^{9,10}$ to compute normal modes, and to crystal systems $^{11-14}$ to compute phonons in a variety of ways $^{15}$. Nevertheless, classical MD simulations can describe thermal effects, but they do not include the quantum statistical behaviours of nuclei. The quantum thermal bath $^{16,17}$ has been introduced in this regard to mimic NQE in MD simulations. This scheme is based on a modified Langevin dynamics and is exact in the case of systems made of harmonic oscillators. It provides satisfactory results in some anharmonic systems such as ice $^{18,19}$ but, being based on classical MD, it suffers from zero point energy leakage issues $^{20}$, although some recent work tends to correct this problem $^{21}$. Methods not based on MD while including both thermal and quantum effects are the Self Consistent Harmonic Approximation $^{22}$ (SCHA) and its stochastic implementations $^{23,24}$(SSCHA), and the Self-Consistent Ab Initio Lattice Dynamics $^{25}$ (SCAILD), where anharmonicity is sampled through real space stochastic techniques. Also the Self Consistent Phonon (SCPH) theory, developed in Ref. 26 and implemented in Ref. 27, belongs to this class of non-MD schemes.

Despite their recent revival, mainly boosted by the physics of hydrogen-rich materials, all these methods deteriorate in case of strong anharmonicity. Path integral techniques are a way to improve upon previous self-consistent approaches and to go towards sampling the *exact* thermal distribution of quantum nuclei, therefore including anharmonicity at all orders. However, the price to pay is the increase in computational cost and the difficulty of *measuring* the vibrational properties, once the quantum thermal distribution is sampled.

In this work, we propose a scheme to extract accurate phonon dispersions and low-lying excitations from the quantum thermal distribution function exactly sampled by efficient Path Integral Molecular Dynamics (PIMD) simulations. While PIMD

$^{a)}$Electronic mail: michele.casula@sorbonne-universite.fr

is a general framework that covers many types of path integrals combined into MD simulations, such as Centroid Molecular Dynamics, Ring Polymer Molecular Dynamics (RPMD) or its thermostatted version (TRPMD), in the following we will always refer to PIMD in the context of TRPMD. In our approach, the quantum system is thermalized through a Langevin thermostat, implemented within the framework of the fast Path Integral Ornstein-Uhlenbeck Dynamics (PIOUD) algorithm $^{28}$.

By extending the maximum localization criterion to determine normal modes in classical $MD^{10}$, we develop quantum Kubo-transformed correlation functions that give rise to analogous expressions in PIMD. We prove that these quantum correlators are one order of magnitude more efficient than the standard ones, by yielding converged phonon frequencies after a few picoseconds of dynamics and at a larger time steps. We first test the proposed estimators in one- and two-dimensional toy models, which are exactly solvable. Then, we apply our estimators to compute the phonon dispersion of materials from first principles, by using forces from density functional theory (DFT). We show the case of diamond, a benchmark system, and the more difficult atomic $I4_1/amd$ phase of hydrogen, where NQE and anharmonic effects are large.

The paper is organized as follows: In Sec. II we set the formalism of our PIMD framework, and we define the quantum correlators upon which the phonon estimators are based, valid for both isolated and extended systems. Results are shown in Sec. III. In particular, in Sec. III A we focus on one-dimensional (1D) toy models; in Sec. III B we study a strongly anharmonic two-dimensional (2D) system; in Sec. III C we report ab initio results obtained for diamond and in Sec. III D the ones for atomic $I4_1/amd$ hydrogen. Finally, we draw conclusions and perspectives in Sec. IV.

## II. THEORY

We present here the PIMD framework, where we will derive the phonon quantum estimators. To set the formalism, Sec. II A gives a brief overview of the PIMD with Langevin thermostat, i.e. the Path Integral Langevin Dynamics (PILD), whose details can be found in the pioneering work by Ceriotti and coworkers $^{29,30}$. However, in our work the PILD equation of motions (EOMs) are integrated using the PIOUD algorithm, introduced recently in Ref. 28 by some of us. PIOUD is a general scheme, capable of propagating EOMs with both deterministic forces - such as in DFT - and stochastic forces - such as in the Quantum Monte Carlo (QMC) case -, keeping the temperature constant. PIOUD is very efficient, because it is built upon an optimal number of Trotter factorizations of the Liouvillian operator. $^{28}$ In Sec. II B we introduce the general formalism to compute quantum mechanical expectation values in PIMD. The remaining Subsections are devoted to phonon evaluation. In Sec. II C we recall the formula for the phonon computation obtained from a localization criterion for the classical velocity-velocity correlation functions $^{10}$. Then, we develop the PIMD extension of the classical correlators by using the Kubo formalism. In Sec. II D, the quantum force-force phonon estimators are derived, while in Sec. II E we provide the derivation of the phonons calculation based on quantum displacement-displacement correlators. For the sake of clarity, all derivations are first done considering an isolated system, i.e. a molecule, thus neglecting the periodicity of a crystalline system. The generalization to periodic systems is carried out in Sec. II F. Finally, in Sec. II G we discuss the advantages of computing phonons by complying with the localization principle scheme, once compared with Kubo formulas that do not fulfill it.

### A. Path Integral Molecular Dynamics

We consider a system of $N$ distinguishable particles. Using a Trotter factorization of the trace, the quantum mechanical partition function $Z=\text{tr}[e^{-\beta H}]$ can be written as $^{29,31}$

$$
Z = \lim_{P \to \infty} \frac{1}{(2\pi \hbar)^f} \int d^f \mathbf{p} \int d^f \mathbf{x} \, e^{-\beta_P H_P(\mathbf{x},\mathbf{p})}, \tag{1}
$$

with $P$ the number of beads, $f=N \cdot P$, $\beta_P=\beta/P$, $1/\beta=k_b T$, and where $\mathbf{x}$ and $\mathbf{p}$ are the $3NP$-dimensional vectors of positions and momenta respectively. In practice, Eq. (1) is evaluated using a discretization approximation with $P$ finite. However, $P$ is taken large enough to guarantee the convergence of the integral. The PIMD Hamiltonian $H_P(\mathbf{x},\mathbf{p})$ in Eq. (1) is

$$
\begin{aligned}
H_P(\mathbf{x},\mathbf{p}) = \sum_{i=1}^{3N} \sum_{j=1}^{P} \left( \frac{[p_i^{(j)}]^2}{2m_i} + \frac{1}{2} m_i \omega_P^2 [x_i^{(j)} - x_i^{(j-1)}]^2 \right) \\
+ \sum_{j=1}^{P} V(x_1^{(j)},...,x_{3N}^{(j)}),
\end{aligned} \tag{2}
$$

where $\omega_P=1/(\beta_P \hbar)$ and $x_i^0=x_i^P$. Henceforth, we set $\hbar=1$. The Hamiltonian $H_P$ is defined in an extended phase-space that consists of $P$ images (beads) of the physical N-particle system connected each other through harmonic potentials, while the particles within every image interact through the potential $V$. This maps the quantum system onto a classical model of interacting ring polymers $^{31,32}$.

For later purposes, it is convenient to split the extended Hamiltonian as $H_P(\mathbf{x},\mathbf{p})=T_P(\mathbf{p})+V_P(\mathbf{x})$, where

$$
\begin{aligned}
V_P &= \frac{1}{2} \sum_{i=1}^{3N} \sum_{j=1}^{P} m_i \omega_P^2 [x_i^{(j)} - x_i^{(j-1)}]^2 + \sum_{j=1}^{P} V(x_1^{(j)},...,x_{3N}^{(j)}), \\
T_P &= \sum_{i=1}^{3N} \sum_{j=1}^{P} \frac{[p_i^{(j)}]^2}{2m_i}.
\end{aligned} \tag{3}
$$

The choice of $m_i$ equal to the physical masses of the particles $^{33}$ and the EOMs generated by Eq. (2) in the extended phase-space correspond to the RPMD approximation. Therein, we neglect the statistics of quantum particles, which are treated as Boltzmannons. Morever, the RPMD trajectories are only meant to sample the stationary quantum thermal distribution, and do not represent a real time dynamics $^{29}$.

In order to keep the temperature constant during the simulations, we used a Langevin thermostat and the PIOUD algorithm $^{28}$. It is worth noting that different algorithms have

been developed to integrate the nuclear EOMs with built-in Langevin thermostats, such as the path integral Langevin equation²⁹ (PILE) or the generalized Langevin equation²⁹,³⁰,³⁴ (GLE). At variance with PILE, PIOUD integrates exactly the thermal Brownian motion of a quantum particle. In particular, while the PILE Liouvillian operator is split into normal modes evolution of harmonic oscillators and Langevin thermostatting, in PIOUD there is a single Liouvillian propagation step that includes both processes. It corresponds to an Ornstein Uhlenbeck dynamics for the **x** and **p** coordinates, which saves a Trotter breakup. This nice PIOUD feature allows one to use larger integration time steps without reducing the number of beads, that is of paramount importance for saving CPU time. On the other hand, GLE is well designed for faster convergence with the number of beads, but it does not fulfill the fluctuation-dissipation theorem. Therefore, the PIOUD integration scheme is the most suitable for our purposes.

The Born-Oppenheimer potential energy surface and nuclear forces are computed at each time step by using the DFT-based Quantum Espresso³⁵ engine for solving the electronic Schrödinger equation³⁶,³⁷. Thus, our approach is fully ab ini- tio.

### B. Quantum mechanical observables and PIMD correlation functions
In the PIMD framework, the quantum mechanical expectation value $\langle A \rangle = \frac{1}{Z}\text{tr}[e^{-\beta \hat{H}} \hat{A}]$ takes the expression³⁸,³⁹

$$
\langle A \rangle = \int d^f \mathbf{p} \int d^f \mathbf{x} \frac{e^{-\beta_P H_P(\mathbf{x},\mathbf{p})}}{Z} \mathsf{A}(\mathbf{x}) \equiv \langle \langle \mathsf{A} \rangle \rangle, \tag{4}
$$

where $\langle\langle \cdots \rangle\rangle$ indicates the average over the paths that sample the statistical distribution of $H_P(\mathbf{x},\mathbf{p})$, and

$$
\mathsf{A}(\mathbf{x}) = \frac{1}{P} \sum_{j=1}^P A(\mathbf{x}^{(j)}), \tag{5}
$$

is the bead-averaged operator, $\mathbf{x}^{(j)}$ being the 3N-dimensional vector of coordinates of the $j$-th image. In Eq. (4) we have assumed that the operator $\hat{A}$ is purely position-dependent, and we have used the cyclic invariance of the trace. The trajectories generated by the PIMD EOMs, $\{\mathbf{x}^{(j)}(t)\}_{j=1,\dots,P}$, are used to evaluate the integrals $\langle\langle \cdots \rangle\rangle$, such as the one above.

The time-correlation between two observables $A$ and $B$ is defined as:

$$
c_{AB}(t) = \frac{1}{Z}\text{tr}\left[ e^{-\beta \hat{H}} \hat{A} e^{i \hat{H} t} \hat{B} e^{-i \hat{H} t} \right], \tag{6}
$$

while the Kubo-transformed version of Eq. (6) reads:³⁸⁻⁴²

$$
\tilde{c}_{AB}(t) = \frac{1}{\beta Z} \int_0^\beta d\lambda \ \text{tr}\left[ e^{-(\beta-\lambda) \hat{H}} \hat{A} e^{-\lambda \hat{H}} e^{i \hat{H} t} \hat{B} e^{-i \hat{H} t} \right]. \tag{7}
$$

Their Fourier transforms are related each other via the Equation:

$$
C_{AB}(\omega) = \frac{\beta \omega}{1 - e^{-\beta \omega}} \tilde{C}_{AB}(\omega), \tag{8}
$$

where $C_{AB}(\omega)$ ($\tilde{C}_{AB}(\omega)$) is the Fourier transform of $c_{AB}(t)$ ($\tilde{c}_{AB}(t)$). The relation in Eq. (8) shows that the time dependent Kubo-transformed correlation function of Eq. (7) carries the same information as the one in Eq. (6). Nevertheless, one can show³⁸ that $\tilde{c}_{AB}$ is real and even with respect to $t$, a property shared with classical MD correlation functions. This is in contrast to $c_{AB}$ which, in general, is a complex function. The Kubo-transformed correlation function can be derived using linear response theory,³⁹,⁴³ and its time dependence is accessible over a short time-scale through PIMD simulations, due to its parallelism with classical correlation functions. In this work, however, we will just focus on instantaneous correlations. Hereafter, we will refer only to $t=0$ correlation functions and, thus, for the sake of clarity we will drop the time-dependence in our notation, i.e. $\tilde{c}_{AB} \equiv \tilde{c}_{AB}(0)$. Within PIMD, the zero-time $A$-$B$ correlation function and its Kubo transform read³⁸,⁴²,⁴⁴

$$
c_{AB} = \int d^f \mathbf{p} \int d^f \mathbf{x} \frac{e^{-\beta_P H_P(\mathbf{x},\mathbf{p})}}{Z} \frac{1}{P} \sum_{j=1}^P A(\mathbf{x}^{(j)}) B(\mathbf{x}^{(j)}), \tag{9}
$$

$$
\tilde{c}_{AB} = \int d^f \mathbf{p} \int d^f \mathbf{x} \frac{e^{-\beta_P H_P(\mathbf{x},\mathbf{p})}}{Z} \mathsf{A}(\mathbf{x}) \mathsf{B}(\mathbf{x}), \tag{10}
$$

respectively. Note that while $c_{AB}$ is the average over products of equal-image operators, the Kubo-transformed correlator $\tilde{c}_{AB}$ includes all product terms, both diagonal and off-diagonal in the bead index. Analogously to Eq. (4), a shorthand notation for Eq. (10) is $\tilde{c}_{AB} \equiv \langle\langle \mathsf{AB} \rangle\rangle$. The latter will be the building block of our quantum estimators.

### C. Classical Phonon Estimators
We now focus on observables related to the evaluation of phonon frequencies. We start from the N-particle classical Hamiltonian, for which anharmonic vibrational theories have already been extensively developed in previous works⁸,¹⁰⁻¹². This formally corresponds to the $P=1$ limiting case of Eq. (2), although the classical situation is substantially different from the quantum case, as Eq. (2) becomes the physical, albeit classical, Hamiltonian, and its EOMs represent a real time dynamics. In this limit, $T_{P=1}=K$, i.e. the classical kinetic energy, and $V_{P=1}=V$, i.e. the inter-particle potential.

The key quantity to compute phonons and other derived quantities, such as the vibrational entropy and vibrational free energies, is the force constant matrix, defined as the second derivative of the potential energy $V$ with respect to the displacement of atoms from their equilibrium configurations. Using Cartesian coordinates (as we will do in the rest of the paper), the force constant matrix at zero temperature is $\bar{V}_{i_1 i_2} = \left. \frac{\partial^2 V}{\partial x_{i_1} \partial x_{i_2}} \right|_{\bar{\mathbf{x}}}$, where $\bar{\mathbf{x}}$ is the potential energy minimum and $i_1, i_2 = 1, ..., 3N$ are the collective Cartesian indices. More generally, if the temperature is different from zero, the force constant matrix can be defined as

$$
\bar{V}_{i_1 i_2} \equiv \left\langle \frac{\partial^2 V}{\partial x_{i_1} \partial x_{i_2}} \right\rangle, \tag{11}
$$

where the brackets indicate the average over a statistical ensem- ble. The matrix $\bar{V}_{i_{1} i_{2}}$ enters the standard eigenvalue problemto compute phonon frequencies:
$$
\bar{V}_{i_{1} i_{2}} Y_{i_{2} i_{3}}=\omega_{i_{3}}^{2} m_{i_{1}} Y_{i_{1} i_{3}},\qquad(12)
$$
where $\omega_{k}$ is the frequency of the k-th normal mode, and $Y_{i_{2} i_{3}}$  is the matrix containing the phonon pattern for each normal mode.
The usual scheme to get $\bar{V}$ at zero temperature is to com pute the second derivatives numerically around the equilib- rium geometry. This is the main idea behind the most popularapproaches, such as the frozen phonon approximation $^{45,46}$  where the derivatives are computed explicitly -, and density functional perturbation theory (DFPT), $^{47,48}$ which evaluates second derivatives through response functions.
In this work we will deal with canonical ensemble simula- tions. To extract the force constant matrix $\bar{V}$ in this situation, one exploits an exact relation between force fluctuations and $\bar{V}$ , which holds at statistical equilibrium, namely $^{10,49}$ 
$$\begin{aligned}
\left\langle F_{i_{1}} F_{i_{2}}\right\rangle & =\int d^{N} \mathbf{p} e^{-\beta K} \int d^{N} \mathbf{x} \frac{\partial V}{\partial x_{i_{1}}} \frac{\partial V}{\partial x_{i_{2}}} \frac{e^{-\beta V}}{Z} \\
& =\frac{1}{\beta} \bar{V}_{i_{1} i_{2}}
\end{aligned}\qquad(13)$$
 where Z is the classical partition function and $F_{i}$ is the force acting on the i-th degree of freedom. The above relation, de- rived integrating by parts with respect to $x_{i_{2}}$ , is a recipe to obtain the force constant matrix at finite temperature through the evaluation of force-force correlators (i.e. the force co- variance matrix). Therefore, it does not require the explicit minimization of the energy. Furthermore, it is worth noting that Eq. (13) is very general, because it is fulfilled for any physical potential V.
In the context of classical MD simulations, a more generalexpression than the one of Eq. (12) has been derived in Refs. 10 and 50, by using a localization criterion for the Fourier- transformed velocity-velocity correlation functions. This lo- calization principle requires that the power spectrum of the po- sition coordinates is maximally localized in frequency for the effective normal modes. It generalizes the normal mode analy- sis to anharmonic systems, where the phonon modes acquire a sizeable broadening. Following the localization principle, and by making use of the stationarity of correlation functions, it is possible to derive a generalized eigenvalue problem where theauto-correlations are taken in the zero-time limit. It reads $^{10}$ 
$$\left\langle F_{i_{1}} F_{i_{2}}\right\rangle Y_{i_{2} i_{3}}=\omega_{i_{3}}^{2}\left\langle p_{i_{1}} p_{i_{2}}\right\rangle Y_{i_{2} i_{3}},\qquad(14)$$
 where $\omega_{i_{3}}^{2}$ are the squared phonons frequencies. By means of Eq. (13), Eq. (14) looks very similar to Eq. (12), apart from the momentum correlator on its right-hand side. However, one can derive Eq. (12) from the most general Eq. (14) thanks tothe relation:
$$\left\langle p_{i_{1}} p_{i_{2}}\right\rangle=k_{b} T m_{i_{1}} \delta_{i_{1} i_{2}},\qquad(15)$$
 which holds at thermodynamic equilibrium, when the mo- menta of the 3N degrees of freedom are decorrelated and fulfill the equipartition theorem.
Another way to obtain the force constant matrix for a sys- tem at thermal equilibrium is based on the displacement-displacement correlation function:
$$\begin{aligned}
\left\langle\delta x_{i_{1}} \delta x_{i_{2}}\right\rangle & \approx \int d^{N} \mathbf{p} e^{-\beta K} \int d^{N} \mathbf{x} \delta x_{i_{1}} \delta x_{i_{2}} \frac{e^{-\frac{\beta}{2} \delta \mathbf{x}^{T} \cdot \bar{V} \cdot \delta \mathbf{x}}}{Z} \\
& \approx \beta\left[\bar{V}^{-1}\right]_{i_{1} i_{2}},
\end{aligned}\qquad(16)$$
 where $\delta x=x-\overline{x}$ is the nuclear displacement from the equilib rium geometry. At variance with Eq. (13), in Eq. (16) the iden- tity is only approximated, because the relation with $\bar{V}$ relies on the truncation of the Taylor expansion of V at the second or- der in $\delta x$ , namely $V=V_{0}+\frac{1}{2} \frac{\partial^{2} V}{\partial x_{i_{1}} \partial x_{i_{2}}}|_{\tilde{x}} \delta x_{i_{1}} \delta x_{i_{2}}+o(\delta x^{3})$ . The identity in Eq. (16) becomes exact in the small temperature limit, or if the potential V is harmonic. Nonetheless, using Eq. (16) to estimate the force constant matrix and inserting it into Eq. (12) corresponds to the Principal Mode Analysis method $^{51,52}$ . Analogously to the force correlation functions, the localization principle of Ref. 10 leads to another general- ized eigenvalue version of Eq. (12) that can be obtained fromthe zero-time displacement-displacement correlation function:
$$\left[\left\langle\delta \mathbf{x} \delta \mathbf{x}^{T}\right\rangle^{-1}\right]_{i_{1} i_{2}} W_{i_{2} i_{3}}=\omega_{i_{3}}^{2}\left[\left\langle\dot{\mathbf{x}} \dot{\mathbf{x}}^{T}\right\rangle^{-1}\right]_{i_{1} i_{2}} W_{i_{2} i_{3}},\qquad(17)$$
 where W is the matrix containing the patterns of the principalmodes. By exploiting the equipartition theorem for velocities:
$$\left[\left\langle\dot{\mathbf{x}} \dot{\mathbf{x}}^{T}\right\rangle^{-1}\right]_{i_{1} i_{2}}=m_{i_{1}} \beta \delta_{i_{1} i_{2}},\qquad(18)$$
 one can derive the standard eigenvalue Eq. (12) from the gen- eralized eigenvalue Eq. (17). It is important to notice that for harmonic systems, or in the small temperature limit, Eqs.(14) and (17) correspond to the same generalized eigenvalue problem and, thus, yield the same frequencies at thermody- namic equilibrium. At zero temperature both principal mode and normal mode analysis yield the same eigenvalues, which in this limit correspond to the harmonic frequencies.
D. Quantum force-force estimator
To quantize the classical approach we reviewed in Sec. II C, let us take into account the force constant matrix defined in Eq. (11). According to its definition, $\bar{V}_{i_{1} i_{2}}$ can be seen as an instantaneous two-particle correlation function that weights the coordinates of particles $i_{1}$ and $i_{2}$ by the amplitude $\frac{\partial^{2} V}{\partial x_{i_{1}} \partial x_{i_{2}}}$ . Therefore, we can extend its definition within the PIMD frame- work either using Eq. (9), or its Kubo transform in Eq. (10). Since we will show that the most appropriate quantum esti- mators to compute phonons in PIMD simulations are those based on Kubo-transformed correlation functions, we definethe PIMD force constant matrix as:
$$\bar{V}_{i_{1} i_{2}} \equiv\left\langle\left\langle\frac{1}{P^{2}} \sum_{j_{1}, j_{2}=1}^{P} \frac{\partial^{2} \mathrm{~V}}{\partial x_{i_{1}}^{\left(j_{1}\right)} \partial x_{i_{2}}^{\left(j_{2}\right)}}\right\rangle\right\rangle=\left\langle\left\langle\bar{V}_{i_{1} i_{2}}\right\rangle\right\rangle, \quad(19)$$
 where the rightmost expression is a shorthand notation,with $\bar{V}_{i j}$ the Kubo-averaged Hessian of V(x)= $\frac{1}{P} \sum_{j=1}^{P} V(x^{(j)})$ .

By also defining the quantum force fluctuation by means of a Kubo-transformed correlation function, namely $\tilde{c}_{F_{i_{1}} F_{i_{2}}}=\left\langle\left\langle\mathrm{F}_{i_{1}} \mathrm{~F}_{i_{2}}\right\rangle\right\rangle$, we prove that the following relation holds (see App. A for the full derivation):

$$
\left\langle\left\langle\mathrm{F}_{i_{1}} \mathrm{~F}_{i_{2}}\right\rangle\right\rangle=\frac{1}{\beta}\left\langle\left\langle\tilde{\nabla}_{i_{1} i_{2}}\right\rangle\right\rangle . \tag{20}
$$

This is the exact PIMD analogue of Eq. (13), and - like in the classical case - the above relation is general, because it does not depend on the form of the potential $V$. If a similar derivation were carried out by using PIMD correlation functions as per Eq. (9), Eq. (20) would be broken, as shown in App. A as well, and no quantum analogue of the classical relation would be found. This strongly supports the idea that the Kubo-transformed correlation functions are the most suitable extensions of the corresponding classical quantities.

Furthermore, in a quantum system, the zero-time Kubo-transformed autocorrelation for Cartesian momenta fulfills the equipartition theorem, i.e. $\tilde{c}_{p_{i_{1}} p_{i_{2}}}=m_{i_{1}} k_{b} T \delta_{i_{1} i_{2}}$. This relation holds also for the momenta of the effective classical system of ring polymers. Thus, given the classical localization principle of the effective normal modes $^{10}$ in terms of force autocorrelation function, these quantum relations enable us to write down the corresponding PIMD generalized eigenvalue problem for phonons evaluation:

$$
\left\langle\left\langle\mathrm{F}_{i_{1}} \mathrm{~F}_{i_{2}}\right\rangle\right\rangle Y_{i_{2}, i_{3}}=\omega_{F F, i_{3}}^{2}\left\langle\left\langle\mathrm{p}_{i_{1}} \mathrm{p}_{i_{2}}\right\rangle\right\rangle Y_{i_{2}, i_{3}}, \tag{21}
$$

where both F and p observables are averaged over the whole ring polymers, as defined in Eq. (5). Like in the classical case, Eq. (21) is more general than the standard eigenvalue problem, which can be readily derived from the definition of the PIMD force constant matrix in Eq. (19), and reads:

$$
\left\langle\left\langle\tilde{\nabla}_{i_{1} i_{2}}\right\rangle\right\rangle Y_{i_{2}, i_{3}}=\omega_{i_{3}}^{2} m_{i_{1}} Y_{i_{1}, i_{3}}. \tag{22}
$$

The generalized eigenvalue Eq. (21) reduces to the standard eigenvalue Eq. (22) in the thermodynamic equilibrium limit of the extended phase-space with $3 N P$ degrees of freedom. Therefore, the $\omega_{F F, i}$ eigenvalue is the fundamental frequency of the $i$-th normal mode. However, Eq. (21) does not require perfect equipartition, in contrast to Eq. (22). This will turn out to be a great advantage for a much faster convergence and a more precise evaluation of the phonon modes, when the generalized eigenvalue problem is applied to the quantum case.

In Sec. IIG, by using 1D model potentials, we will examine the equilibration time and the time step bias affecting the phonon frequencies convergence during the PIMD EOMs evolution. By comparing the results obtained with both eigenvalue problems Eqs. (21) and (22), we will demonstrate the better performance of Eq. (21), which improves the phonon estimation efficiency by at least one order of magnitude with respect to the standard approach of Eq. (22).

## E. Quantum displacement-displacement estimator

As done for the force-force correlation functions in Sec. IID, we want here to extend the classical displacement-displacement correlators in order to compute phonons in a quantum system within the PIMD framework. As already seen for the force-force estimators, the most appropriate quantum correlation functions, which preserve the relationships found in the classical situation, are the ones based on the Kubo transform. Thus, we proceed by quantizing the classical autocorrelations present in the principal mode analysis and in the classical generalized eigenvalue problem of Eq. (17).

In the PIMD notation, the displacement-displacement and velocity-velocity autocorrelation matrix elements are given by

$$
\begin{aligned}
\left\langle\left\langle\delta x_{i_{1}} \delta x_{i_{2}}\right\rangle\right\rangle & =\left\langle\left\langle\left(\frac{1}{P} \sum_{j_{1}=1}^{P} \delta x_{i_{1}}^{\left(j_{1}\right)}\right)\left(\frac{1}{P} \sum_{j_{2}=1}^{P} \delta x_{i_{2}}^{\left(j_{2}\right)}\right)\right\rangle\right\rangle, \\
\left\langle\left\langle\dot{x}_{i_{1}} \dot{x}_{i_{2}}\right\rangle\right\rangle & =\left\langle\left\langle\left(\frac{1}{P} \sum_{j_{1}=1}^{P} \dot{x}_{i_{1}}^{\left(j_{1}\right)}\right)\left(\frac{1}{P} \sum_{j_{2}=1}^{P} \dot{x}_{i_{2}}^{\left(j_{2}\right)}\right)\right\rangle\right\rangle.
\end{aligned} \tag{23}
$$

Thus, following the same path as the force-force case, by extending Eq. (17) into the PIMD case, one obtains

$$
\left[\left\langle\left\langle\delta \mathbf{x} \delta \mathbf{x}^{T}\right\rangle\right\rangle^{-1}\right]_{i_{1}, i_{2}} W_{i_{2}, i_{3}}=\omega_{\delta x \delta x, i_{3}}^{2}\left[\left\langle\left\langle\dot{\mathbf{x}} \dot{\mathbf{x}}^{T}\right\rangle\right\rangle^{-1}\right]_{i_{1}, i_{2}} W_{i_{2}, i_{3}},
$$

where we adopted the same notation as the classical case, but the classical correlation functions are replaced by the Kubotransformed quantum auto-correlations. Like in the classical case, it is true that $\tilde{c}_{\dot{x}_{i} \dot{x}_{j}}=\delta_{i, j} k_{b} T / m_{i}$. However, at variance with the force-force estimator of Eq. (20), the Kubo displacement-displacement correlator is not exactly related to the Kubo force constant matrix. This is very similar to the classical behavior, where only the classical force auto-correlation can be exactly expressed in terms of $\tilde{\nabla}_{i_{1} i_{2}}$ (Eq. (13)), while the relation between the classical displacement-displacement correlator and $\tilde{\nabla}_{i_{1} i_{2}}$ is approximated (Eq. (16)). However, at variance with the classical framework, the broken relation between the Kubo-transformed displacement correlator and the Kubo-transformed force constant matrix hides a deeper physical meaning for the eigenvalues $\omega_{\delta x \delta x, i}$ in Eq. (24). Indeed, such eigenvalues are no longer an estimation of the fundamental frequencies of the system, but they are more directly related to the first energy excitation of the phonon modes.

To show this property in a simple and transparent situation, let us focus on a 1D system with Hamiltonian $\hat{H}=\frac{\hat{p}^{2}}{2 m}+\hat{V}(x)$. To be more explicit, here we will use the notation of the true quantum Kubo-transformed correlation functions instead of their PIMD versions. With our aim, it is useful to decompose Eq. (7) at zero time in terms of the complete set of quantum eigenstates $\{|n\rangle\}$ of the time-independent Hamiltonian $\hat{H}$:

$$
\begin{aligned}
\tilde{c}_{A B} & =\frac{1}{\beta Z} \int_{0}^{\beta} d \lambda \operatorname{tr}\left[e^{-(\beta-\lambda) \hat{H}} \hat{A} e^{-\lambda \hat{H}} \hat{B}\right] \\
& =\frac{1}{\beta Z} \sum_{n, m} e^{-\beta E_{n}} A_{n m} B_{m n} \frac{1-e^{-\beta \omega_{m, n}}}{\omega_{m, n}} \\
& =\frac{1}{\beta Z} \sum_{n, m} \tilde{c}_{A B}^{(n m)},
\end{aligned} \tag{25}
$$

where $\omega_{m, n}=E_{m}-E_{n}$ is the energy difference between the $m$-th and $n$-th quantum levels, and $A_{m n}=\langle m|\hat{A}| n\rangle$. In the 1D

case, Eq. (24) can be rewritten as:
$$
\omega_{\delta x \delta x}^{2}=\frac{\tilde{c}_{\hat{x} \hat{x}}}{\tilde{c}_{\delta x \delta x}}=\frac{\sum_{l, n} \omega_{l, n}^{2} \cdot \tilde{c}_{\delta x \delta x}^{(l, n)}}{\sum_{l, n} \tilde{c}_{\delta x \delta x}^{(l, n)}}=\sum_{l, n} \omega_{l, n}^{2} \cdot \tilde{d}_{\delta x \delta x}^{(l, n)}, \quad(26)
$$
where we employed the correlation functions decomposition in terms of the Hamiltonian eigenstates, as detailed in Eq. (25), and we used the quantum mechanical equivalence $\langle l|\hat{\dot{x}}_{i}| n\rangle=$  $i \cdot\langle l|\hat{x}_{i}| n\rangle \cdot \omega_{l, n}$ . At the rightmost-hand side of Eq. (24), we defined the coefficients
$$
\tilde{d}_{\delta x \delta x}^{(l, n)}=\frac{\tilde{c}_{\delta x \delta x}^{(l, n)}}{\sum_{l, n} \tilde{c}_{\delta x \delta x}^{(l, n)}},\qquad(27)
$$
which are normalized to 1, once summed over $l$ and $n$ (i.e. $\sum_{l, n} \tilde{d}_{\delta x \delta x}^{(l, n)}=1$ ). From Eq. (25), we observe that the quantum displacement-displacement estimator is a sum of squared- transitions between the eigenstates of the system. In particular the coefficients $\tilde{d}_{\delta x \delta x}^{(l, n)}$ are proportional to $\propto \frac{|\langle l|(\hat{x}-\bar{x})| n\rangle|^{2}}{\omega_{n, l}}$ . Considering the $T \to 0$ limit, where only the ground state ispopulated, the coefficients become (see appendix B):
$$
\tilde{d}_{\delta x \delta x}^{(l, n)} \simeq \tilde{d}_{\delta x \delta x}^{(0, n)} \propto \frac{|\langle 0|(\hat{x}-\bar{x})| n\rangle|^{2}}{\omega_{n, 0}},\qquad(28)
$$
where $n=\{1,..., \infty\}$ runs over the excited-states indices, and|0) represents the ground state. By inspecting Eq. (28), it

![](./images/867770780115533962_1.jpg)

FIG. 1. Semi-log plot of the quantum displacement-displacement estimator weights $\tilde{d}_{\delta x \delta x}^{(0, n)}$ at $20 ~K$ for the Morse potential (top-left panel), quartic (top-right panel) and symmetric double well with dif- ferent parameters (bottom-left and bottom-right panels) with respect to quantum state transitions. The $n \to m$ transition is labelled as $(n, m)$ on the $x$ axis. At low temperature, only transitions from the ground state are significantly different from zero (Eq. (28)). In the case of symmetric double well (S.D.W.) with $c_{0}=0.3$ , the yellow bars correspond to transition from the first excited state, which for high potential barriers is very close to the ground state. A detailed description of the 1D models can be found in Sec. III A.
is straightforward to see that $\tilde{d}_{\delta x \delta x}^{(0, n)}$ is positive definite $\forall n$ .
Therefore, it can be interpreted as a weighting function for the squared transition energies in Eq. (26). Moreover, it is a decreasing function of $n$ . Indeed, in Eq. (28) both numerator and $1 / \omega_{n, 0}$ are decreasing with $n$ . To illustrate and quantify the $n$ -dependence of the weights in Eq. (28), in Fig. 1 we plot their values for 1D toy-model potentials that will be presented in more detail in Sec. III A. In all cases studied, more than99% of the total weight belongs to the first energy transition. Moreover, the decay with $n$ is exponentially fast. Despite the specific examples reported here, we found that this behaviour is common to all systems we have studied in Sec. III, which are representative of a large and diverse set of anharmonic situations. These are therefore universal features, and we can take the displacement-based generalized eigenvalue problem in Eq. (24) as an accurate way to access the first energy exci- tations of the phonon spectrum.
A similar approach for estimating phonon excitation ener- gies has also been proposed in Refs. 53 and 54, where low-lying phonons excitations are computed by the standard eigenvalueproblem that can be derived by plugging $\tilde{c}_{\hat{x}_{i} \hat{x}_{j}}=\delta_{i, j} k_{b} T / m_{i}$  into Eq. (24). Therefore, in that case, the equipartition is im- posed a priori. Instead, in our case, the rigorous quantization of the classical relations allowed us to derive a PIMD general- ized eigenvalue problem analogous to the classical localization principle, which does not require a perfect equipartition. Re- markably, we found that the generalized eigenvalue problem is much more efficient than the standard one in predicting the vibrational frequencies in PIMD, as reported in Sec. II G for the force-force as well as for the displacement-displacement estimators.
Finally, we notice that for a harmonic potential, the quantum displacement-displacement estimator coincides with the force- force one - as in the classical case -, and the two approaches give exactly the same eigenvalues. Indeed, in the harmonic situation the fundamental frequency yielded by the force-force estimator equals the first excitation energy $\omega_{1,0}$ provided with unitary weight by the displacement-displacement estimator. However, we stress once again that, in the general anharmonic case, the physical information carried by the two eigenvalues is different.
## F. PIMD estimators for crystalline systems
While for isolated systems like molecules the correlation functions accumulated over the MD or PIMD trajectories are usually enough to construct good estimators $^{55}$ , for crystals one should exploit the space group properties to build symmetric force constant and correlation matrices. Furthermore, to ac- cess the phonon dispersion in the Brillouin zone away from the $\Gamma$ -point by means of MD or PIMD simulations, one makes use of a supercell with periodic boundary conditions, where the lattice vector $a_{i}$ is repeated $n_{i}$ times, with $i=\{1,2,3\}$ and $n_{i} \geq 1$ . The set of integers $(n_{1}, n_{2}, n_{3})$ , i.e. the size of the supercell, should be chosen in such a way that the correlation matrix elements between the central atoms and those at the supercell border is negligible.
When dealing with periodic boundary conditions, the strat-

egy to compute the phonon dispersion relies on the following
procedure:

- From MD or PIMD trajectories, we build the super-
cell interatomic correlation matrices in real space for
all quantities of interest, i.e. force and momentum
autocorrelations for the force-force estimator, displace-
ment and velocity autocorrelations for the displacement-
displacement estimator. In order to avoid global trans-
lational drifts, at each time step we apply the following
pinning strategy for the matrices that are not gauge in-
variant with respect to translations. The reference frame
is pinned over the i-th atom of the supercell, so that
each atomic position and displacement are computed
with respect to this atom. We loop over the equivalent
atoms of the supercell, $i = \{1,...,M_{\text{eq}}\}$, by repeating the
same procedure for each atom $i$, and averaging the auto-
correlation functions over the different pinning centers.
In this way, the resulting correlation functions - in par-
ticular the displacement correlation matrix - will be fully
symmetric and gauge invariant.

- For each q-point accessible by the supercell size, namely
$\mathbf{q} = \left( \frac{h_1}{n_1}\mathbf{b}_1, \frac{h_2}{n_2}\mathbf{b}_2, \frac{h_3}{n_3}\mathbf{b}_3 \right)$, where $\mathbf{b}_i$ are the reciprocal lat-
tice vectors and $h_i = \{0,...,n_i-1\}$, we perform a Fourier
transform of the different real-space correlation matri-
ces, and we solve the generalized eigenvalue (GEV)
problems (Eqs. (14) and (17) for MD, and Eqs. (21)
and (24) for PIMD). In particular, the dual forms of the
real-space Eqs. (21) and (24) read

$$
\begin{aligned}
& \langle\langle \mathrm{F}_{i_1} \mathrm{~F}_{i_2} \rangle\rangle(\mathbf{q}) Y_{i_2:i_3}(\mathbf{q})= \\
& =\omega_{F F: i_3}^2(\mathbf{q})\langle\langle \mathrm{p}_{i_1} \mathrm{p}_{i_2} \rangle\rangle(\mathbf{q}) Y_{i_2:i_3}(\mathbf{q}),
\end{aligned}
\tag{29}
$$

and

$$
\begin{aligned}
& \left[\langle\langle \delta \mathbf{x} \delta \mathbf{x}^T \rangle\rangle^{-1}(\mathbf{q})\right]_{i_1, i_2} W_{i_2:i_3}(\mathbf{q})= \\
& =\omega_{\delta x \delta x: i_3}^2(\mathbf{q})\left[\langle\langle \dot{\mathbf{x}} \dot{\mathbf{x}}^T \rangle\rangle^{-1}(\mathbf{q})\right]_{i_1, i_2} W_{i_2:i_3}(\mathbf{q}),
\end{aligned}
\tag{30}
$$

respectively, where $i_1, i_2, i_3 = \{1,...,3N\}$ are the indices
of the unit-cell degrees of freedom.

- From the solution of the two GEVs, using the eigenval-
ues $d_i(\mathbf{q})$ and eigenvectors $|d_i(\mathbf{q})\rangle$ of Eq. (29) or Eq. (30),
we reconstruct for both estimators the true dynamical
matrix:

$$
\mathrm{D}_m(\mathbf{q})=\sum_i\left|d_i(\mathbf{q})\right\rangle d_i(\mathbf{q})\left\langle d_i(\mathbf{q})\right|,
\tag{31}
$$

for each q-point. $\mathrm{D}_m$ is otherwise defined as the mass-
weighted Fourier transform of the force constant ma-
trix. Eq. (31), obtained from the solution of Eq. (29) or
Eq. (30), is a generalization of the standard definition.

- We impose the space-group symmetry relations in q-
space by symmetrizing the dynamical matrix elements
for each q-point and by creating all the dynamical ma-
trices belonging to the star of a given q-point $^{56}$. This
procedure allows one to average the equivalent dynami-
cal matrices eventually created in the stars of the q-points
that are sampled independently during the simulation $^{57}$.

- We go back to real space by Fourier transforming the
fully symmetrized $\mathrm{D}_m$ and by building the real-space
force constant matrix, at this stage being fully symmet-
ric.

- As last step, we perform an interpolation of the phonon
dispersion, by computing and diagonalizing the final
dynamical matrix on a finer q-grid.

### G. Generalized eigenvalue vs standard eigenvalue problem

We prove numerically that, for phonon calculations based
on force autocorrelations, the GEV problem in Eq. (21) is
much more efficient than the standard eigenvalue problem in
Eq. (22), where the mass matrix has been replaced by momen-
tum correlations in the former Equation. In the same way, we
compare the displacement-displacement GEV in Eq. (24) with
its standard version as well. In order to do that, we performed
PIMD simulations of a 1D particle bounded by a Morse po-
tential $V(x)=\frac{k}{2 d_m^2} \cdot\left(1-e^{-a_m \cdot x}\right)^2$, with $k=0.4837$ a.u. and
$a_m=1.1$ bohr $^{-1}$. The temperature $T$ is 100 K, the number
of beads $P=80$, while we varied the integration time-step $\Delta t$
from 0.25 fs to 1 fs. The friction parameter $\gamma_0$ of the Langevin
thermostat $^{28}$ is $1.46 \cdot 10^{-3}$ atomic units. This value is the same
as in Ref. 28, where it is found to be optimal for both stochas-
tic and deterministic forces, representing a good compromise
between diffusion and thermalization rates in systems with
strong NQE. The same value for $\gamma_0$ has been used throughout
all calculations presented in this work.

In Fig. 2 we plot the behavior of the estimated phonon eigen-
values as a function of the PIMD time evolution. We observe
that the frequencies computed from GEV rapidly converge to-
wards the exact values, obtained by diagonalizing numerically
the quantum Hamiltonian. The convergence is reached after
a few ps of dynamics, independently of the $\Delta t$ value. On the
other hand, the solutions of Eq. (22), dubbed $\omega_{FF}(standard)$,
and the one relative to the displacement-displacement esti-
mator, labelled $\omega_{\delta x \delta x}(standard)$, show oscillation amplitudes
much larger than the ones from the corresponding GEV solu-
tions, in all reported cases. Even worse, for $\Delta t \geq 0.5$ fs, the
finite time-step bias become sizeable $(>50 \mathrm{~cm}^{-1})$, while it is
still negligible for the GEV frequencies.

In App. C we present the same analysis for other two relevant
cases of anharmonicity: a 1D particle bounded by a quartic
potential and the one in a symmetric double well potential.
The results show the better performance of the GEV estimators
with respect to the standard ones in all anharmonic situations.

We deduce that the improvement given by GEV phonon
equations with respect to their standard versions is twofold:
firstly they allow to work with a larger time-step $\Delta t$, and sec-
ondly their eigenvalues converge on a much shorter time scale.

![](./images/867770780115533962_2.jpg)

FIG. 2. Convergence of the PIMD phonon eigenvalues for a 1D particle bounded by a Morse potential at 100 K obtained with different integration time-steps $\Delta t$. The exact solutions obtained from the numerical Schrödinger equation are given in red for the force-force (fundamental frequency) and orange for the displacement-displacement estimators ($\omega_{1,0}$ excitation energy).

From the toy models analyzed here, we infer that the gain in $\Delta t$ is at least a factor of 2, while the improvement in the convergence time is even more impressive. We go from about 40 ps in the standard eigenvalue equation to about 4 ps in the GEV. The overall gain in efficiency is therefore larger than one order of magnitude. This is of paramount importance to reduce the global cost of the phonon calculations by PIMD, and to make challenging problems feasible.

Our finding about the performance of the phonon quantum GEV problems whose form has been borrowed from a classical localization principle is particularly important. It is clear that the equipartition theorem implied by the standard eigenvalue problem is hard to reach in the extended $3NP$ space of polymers, where several energy scales coexist. Moreover, it is also clear that nuclear vibrations - particularly the low-energy ones - are very sensitive to the quality of the phase-space sampling. Therefore, the use of GEV for PIMD phonon calculations turns out to be key for an efficient and accurate evaluation of vibrational frequencies.

## III. RESULTS

To benchmark the proposed quantum phonon estimators, firstly we studied 1D model potentials, for which we determined the exact vibrational spectrum through the numerical solution of the Schrödinger equation.

Then, we focused also on a more complex 2D model potential, where we could tune the interaction of the two degrees of freedom. Also in that case, we computed the exact spectrum, and compared against the PIMD force and displacement autocorrelation approaches for benchmark.

Finally, as real test cases, we studied the phonon dispersions of diamond and of atomic hydrogen at high pressure in the I4$_1$/amd phase.

### A. One-dimensional models

For the 1D case, we studied the following potentials, listed in an increasing order of anharmonicity and shown in Fig. 3:

- Harmonic potential: $V(x)=\frac{k}{2}\cdot x^2$;
- Morse potential: $V(x)=\frac{k}{2\cdot a_m^2}\cdot(1-e^{-a_m\cdot x})^2$ with $a_m = 0.2, 0.4, 0.6, 0.8$;
- Quartic potential: $V(x)=c_q\cdot k\cdot x^4$ with $c_q = 0.01, 0.1, 1$;
- Symmetric double well potential: $V(x)=k\cdot(x^2-c_0)^2$ with $c_0 = 0.05, 0.1, 0.3$.

![](./images/867770780115533962_3.jpg)

FIG. 3. 1D potentials used to test the behaviour of the quantum estimators. For each potential-type, we plot only the most anharmonic one.

Then, as a realistic 1D case, we evaluate the PIMD phonon estimators also for the hydrogen molecule using the accurate potential taken from Ref. 58.

In the model potentials, the parameter $k$ is always fixed equal to 0.183736 atomic units, while the physical mass is chosen equal to the hydrogen atom mass. These choices correspond to an oscillation frequency for the harmonic case of $\sqrt{k/m} = \omega_{harm}=2194.74\ \mathrm{cm}^{-1}$.

The details of Schrödinger equation solutions can be found in App. D. We have already introduced the notation for the PIMD eigenvalues obtained from the displacement-displacement ($\omega_{\delta x \delta x}$) and force-force ($\omega_{FF}$) autocorrelations; In the following we call $\frac{\omega_0}{2}$ the exact ground state energy and $\omega_{1,0}$ the exact first excitation energy.

It is worth noting that in the harmonic case, all the estimators are equivalent and - as expected - give exactly the value of $\omega_{harm}$ as fundamental frequency independently of the temperature. In such case, the ratio between the PIMD displacement and force estimators, $\gamma_{\text{PIMD}} \equiv \omega_{\delta x \delta x}/\omega_{FF}$, gives exactly one. In the anharmonic situations instead, $\gamma_{\text{PIMD}}$ will deviate from the identity and it will be a quantitative signature of the anharmonic strength in the potential. In the following, we will compare the value of $\gamma_{\text{PIMD}}$ with $\gamma_{exact} \equiv \frac{\omega_{1,0}}{\omega_0}$, i.e. the exact ratio between the first transition energy and twice the ground state energy computed from the Schrödinger equation. For the other anharmonic potentials, in order to test the PIMD estimators, we prefer to use a temperature as low as 20 K, where quantum effects are dominant.

### 1. Morse potential

The anharmonicity of the Morse potential is controlled by the $a_m$ parameter; in the limit of $a_m \to 0$, the potential becomes harmonic, while for increasing $a_m$, the potential's shape becomes more and more anharmonic. From the results in Tab. I, we can observe that the estimator $\omega_{\delta x \delta x}$ reproduces the energy difference between the first excited state and the ground state, as expected from Eq. (28). On the other hand, the force-force estimator closely follows the fundamental frequency value. The ratio between the displacement-displacement and force-force estimators follows the trend of the true $\gamma_{exact}$ and, as expected, by increasing $a_m$ it deviates more and more from 1.

<table>
<caption>TABLE I. Morse potential. $\omega_0$ is the ground state energy, $\omega_{1,0}$ the energy difference between the first excited state and the ground state. All the estimators are computed at 20 K and are given in $\mathrm{cm}^{-1}$. $\gamma_{exact}$ is the ratio between $\omega_{1,0}$ and $\omega_0$.</caption>
<tbody>
<tr>
<th>$a_m$</th>
<td>0.2</td>
<td>0.4</td>
<td>0.6</td>
<td>0.8</td>
</tr>
<tr>
<th>$\omega_{FF}$</th>
<td>2193.55</td>
<td>2189.96</td>
<td>2183.96</td>
<td>2175.55</td>
</tr>
<tr>
<th>$\omega_0$</th>
<td>2193.54</td>
<td>2189.96</td>
<td>2183.98</td>
<td>2175.62</td>
</tr>
<tr>
<th>$\omega_{\delta x \delta x}$</th>
<td>2190.86</td>
<td>2179.22</td>
<td>2159.82</td>
<td>2132.70</td>
</tr>
<tr>
<th>$\omega_{1,0}$</th>
<td>2189.97</td>
<td>2175.63</td>
<td>2151.75</td>
<td>2118.30</td>
</tr>
<tr>
<th>$\gamma_{\text{PIMD}}$</th>
<td>0.9987</td>
<td>0.9950</td>
<td>0.9889</td>
<td>0.9803</td>
</tr>
<tr>
<th>$\gamma_{exact}$</th>
<td>0.9983</td>
<td>0.9934</td>
<td>0.9852</td>
<td>0.9736</td>
</tr>
</tbody>
</table>

### 2. Quartic potential

At variance with Morse, the quartic potential cannot be reduced to the harmonic case by tuning the anharmonicity parameter $c_q$. The displacement-displacement estimator reproduces very well the energy difference between the first excited state and the ground state (Tab. II) for all the three cases analysed.

<table>
<caption>TABLE II. Quartic potential. The notation is the same as in Tab. I.</caption>
<tbody>
<tr>
<th>$c_q$</th>
<td>0.01</td>
<td>0.1</td>
<td>1.0</td>
</tr>
<tr>
<th>$\omega_{FF}$</th>
<td>332.74</td>
<td>716.86</td>
<td>1544.44</td>
</tr>
<tr>
<th>$\omega_0$</th>
<td>239.39</td>
<td>515.76</td>
<td>1111.17</td>
</tr>
<tr>
<th>$\omega_{\delta x \delta x}$</th>
<td>310.85</td>
<td>669.71</td>
<td>1442.85</td>
</tr>
<tr>
<th>$\omega_{1,0}$</th>
<td>309.23</td>
<td>666.20</td>
<td>1435.30</td>
</tr>
<tr>
<th>$\gamma_{\text{PIMD}}$</th>
<td>0.9342</td>
<td>0.9342</td>
<td>0.9342</td>
</tr>
<tr>
<th>$\gamma_{exact}$</th>
<td>1.2917</td>
<td>1.2917</td>
<td>1.2917</td>
</tr>
</tbody>
</table>

However, $\omega_{FF}$ is not able to reproduce exactly the value of $\omega_0$. To investigate the reasons of such a mismatch, we compared $\omega_{FF}$ with the SCHA frequency, defined as the best harmonic approximation to the ground state energy, based on a variational principle for the free energy of the system$^{24}$. We found that the two values are very close each other, while being different from the exact ground state energy. This points to the fact that, for a quartic potential, the functional shape of the true ground state wave function is far from being harmonic, therefore invalidating the definition of the force constant matrix in Eq. (11) as a mean to recover the right fundamental frequency in this highly anharmonic case. Due to the difference between $\omega_{FF}$ and $\omega_0$, we find that $\gamma_{\text{PIMD}}$ is always smaller than 1, while $\gamma_{exact}$ is larger. The quartic potential points out to the fact

that the parameter $\gamma_{\text{PIMD}}$ cannot carry the information about the eventual superharmonic behavior of the potential energy (i.e. the case in which $\omega_{1,0} > \omega_0$). Nevertheless, its departure from 1, as reported in Tab. II, still signals an anharmonic behavior, and denotes correctly a larger deviation from harmonicity, if compared with the Morse potential.

### 3. Symmetric double well potential

The symmetric double well potential is physically relevant in situations where a hydrogen atom is shared by other two atoms to form a symmetric H-bond configuration. This occurs in many ferroelectrics or antiferroelectrics, where the hydrogen atom is shared by two oxygen or other electronegative atoms$^{59}$. This also happens in the $H_50_2^+$ zundel cation$^{28,60,61}$. By varying the $c_0$ parameter of the symmetric double well potential, we can range from the scenario where the barrier is smaller than the ground state energy ($c_0 = 0.05$ in Tab. III) until the situation in which the barrier is much higher than the ground state ($c_0 = 0.3$ in Tab. III). By analysing the results of Tab. III, we observe again that $\omega_{\delta x \delta x}$ closely follows the $\omega_{1,0}$ value also in the extreme case in which the first excited state is close to the ground state ($c_0 = 0.3$). We deduce that the eigenvalue returned by the displacement-displacement estimator is reliable for evaluating the excitation energy spectrum over a wide range of anharmonic strengths. The force-force frequency, instead, overestimates $\omega_0$ for $c_0 \leq 0.1$, while underestimates it when the barrier is higher. This can be rationalized with the fact

<table>
<caption>TABLE III. Symmetric double well potential. The notation is the same as in Tab. I.</caption>
<thead>
  <tr>
    <th>$c_0$</th>
    <th>0.05</th>
    <th>0.1</th>
    <th>0.3</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\omega_{FF}$</td>
    <td>1384.79</td>
    <td>1321.63</td>
    <td>2946.93</td>
  </tr>
  <tr>
    <td>$\omega_0$</td>
    <td>947.88</td>
    <td>1100.10</td>
    <td>3102.14</td>
  </tr>
  <tr>
    <td>$\omega_{\delta x \delta x}$</td>
    <td>1190.52</td>
    <td>925.44</td>
    <td>124.85</td>
  </tr>
  <tr>
    <td>$\omega_{1,0}$</td>
    <td>1178.02</td>
    <td>904.02</td>
    <td>59.99</td>
  </tr>
  <tr>
    <td>$\gamma_{\text{PIMD}}$</td>
    <td>0.8597</td>
    <td>0.7002</td>
    <td>0.0423</td>
  </tr>
  <tr>
    <td>$\gamma_{exact}$</td>
    <td>1.2427</td>
    <td>0.8217</td>
    <td>0.0193</td>
  </tr>
</tbody>
</table>

that when $c_0$ is small, the behaviour of the symmetric double well is similar to the quartic potential case seen previously. On the other hand, when $c_0$ is higher, $\omega_{FF}$ tends to describe the curvature of one of the two wells.

The extreme case of anharmonicity due to double well potentials with high barriers is nicely detected by the ratio between the two quantum estimators $\gamma_{\text{PIMD}}$, which shows a dramatic deviation from 1, in a very good agreement with $\gamma_{exact}$.

### 4. Hydrogen molecule

As final test for 1D potentials, we consider the realistic case of hydrogen molecule in the relative radial coordinate. We employed the effective potential from Ref. 58 that reproduces very well (with an error of $\pm 1$ cm$^{-1}$) the experimental Q$_{1}(0)$ Raman lines$^{62,63}$. As the hydrogen molecule potential in the

<table>
<caption>TABLE IV. Hydrogen molecule (here the potential minimum is set to zero). The notation is the same as Tab. I.</caption>
<tbody>
  <tr>
    <td>$\omega_{FF}$</td>
    <td>4392.99</td>
  </tr>
  <tr>
    <td>$\omega_0$</td>
    <td>4359.44</td>
  </tr>
  <tr>
    <td>$\omega_{\delta x \delta x}$</td>
    <td>4218.38</td>
  </tr>
  <tr>
    <td>$\omega_{1,0}$</td>
    <td>4162.08</td>
  </tr>
  <tr>
    <td>$\gamma_{\text{PIMD}}$</td>
    <td>0.9602</td>
  </tr>
  <tr>
    <td>$\gamma_{exact}$</td>
    <td>0.9547</td>
  </tr>
</tbody>
</table>

radial coordinate looks like a Morse potential (with $a_m \sim 1.1$ using our notation), it is not surprising that we find the same behaviour of the estimators as in the Morse case. The same numerical value for $\omega_{\delta x \delta x}$ has been found and reported in Ref. 54.

### B. Two-dimensional model

For the two-degree of freedom case, the Hamiltonian is given by
$$
H = \frac{p_1^2}{2m} + \frac{p_2^2}{2m} + V(x_1,x_2). \tag{32}
$$

To check the validity of the scheme to compute the 2D numerical Schrödinger equation, we analyse firstly two harmonic oscillators, i.e. $V(x_1,x_2) = k \cdot (x_1^2 + x_2^2)$, coupled by a $\zeta \cdot x_1 \cdot x_2$ potential that can be solved analytically also in the context of PIMD$^{34}$ or by perturbation theory for $\zeta \ll 1$. Results of this case are reported in appendix D. Of course, in the 2D case, for

![](./images/867770780115533962_4.jpg)

FIG. 4. Symmetric double well potentials $(x_1)$ plus quartic potential $(x_2)$ coupled by a potential term of $x_1 \cdot x_2^2$ type.

each estimator we get two eigenvalues. Therefore, for clarity here we adopt the following notation: $\omega_{\delta x \delta x}$ and $\omega_{FF}$ acquire

an index and become $\omega_{\delta x \delta x, i}$ and $\omega_{F F, i}$, where $i=1,2$. Moreover, the ground state energy, that we call $Z P E_{\text {exact }}$, is the sum of the zero point energies of the two modes. Thus, we estimate $Z P E_{\text {exact }}$ with $Z P E_{\text {PIMD }}=\left(\omega_{F F, 1}+\omega_{F F, 2}\right) / 2$.

A less trivial case is a double well coupled with a quartic potential by a $\zeta \cdot x_{1} \cdot x_{2}^{2}$ term:

$$
V\left(x_{1}, x_{2}\right)=k \cdot\left(x_{1}^{2}-c_{0}\right)^{2}+4 k \cdot x_{2}^{4}+\zeta \cdot x_{1} \cdot x_{2}^{2}. \quad(33)
$$

As in the 1D case, we choose $k=0.183736$ a.u.; then, we set $c_{0}=0.1$, and we varied $\zeta$ to switch from a non-interacting case $(\zeta=0)$ to a strong interacting case $(\zeta=0.2)$. In Fig. 4 we show the potential shape in the case of $\zeta=0.2$. In Tab. V we report the results. The situation in which $\zeta=0$ is the non-interacting case and the 2D problem reduces to two 1D problems. In the latter case, for the symmetric double well degree of freedom we get the same results as the 1D problem studied previously with $c_{0}=1$. By switching on the interaction, we observe that results agree with the findings in the 1D case. Indeed, despite the large anharmonicity, one could expect only in some physical extreme conditions, $\omega_{\delta x \delta x, 1}$ and $\omega_{\delta x \delta x, 2}$ are always very close to the first transition energies $(\omega_{1,0}$ and $\omega_{2,0}$ respectively) and represent an upper bound of them. On the other hand, the two frequencies given by the force-force estimator are harder to compare with the exact results because the $Z P E_{\text {exact }}$ value hides the contribution carried by the two modes. However, from the comparison between $Z P E_{\text {PIMD }}$ and $Z P E_{\text {exact }}$ we can conclude that, as previously found, the fundamental frequency estimates become less accurate by increasing the interaction parameter $\zeta$. The 2D models evidence that the

<table>
<caption>Table V. Symmetric double well potential $(x_1)$ coupled with a quartic potential $(x_2)$ through a $\zeta \cdot x_1 \cdot x_2^2$ interaction. We named the two modes for each estimator with (i=1) and (i=2), $ZPE_{\text{PIMD}}$ is the PIMD zero point energy computed as $(\omega_{F F,1} + \omega_{F F,2})/2$ while $ZPE_{\text{exact}}$ is the ground state energy.</caption>
<thead>
  <tr>
    <th>$\boldsymbol \zeta$</th>
    <th>0.0</th>
    <th>0.1</th>
    <th>0.2</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\omega_{FF,i}$</td>
    <td>(i=1) 1321.66<br>(i=2) 2449.55</td>
    <td>(i=1) 1400.28<br>(i=2) 2410.38</td>
    <td>(i=1) 1615.27<br>(i=2) 2314.16</td>
  </tr>
  <tr>
    <td>$ZPE_{\text{PIMD}}$</td>
    <td>1885.60</td>
    <td>1905.33</td>
    <td>1964.71</td>
  </tr>
  <tr>
    <td>$ZPE_{\text{exact}}$</td>
    <td>1785.52</td>
    <td>1756.87</td>
    <td>1665.86</td>
  </tr>
  <tr>
    <td>$\omega_{\delta x \delta x,i}$</td>
    <td>(i=1) 925.14<br>(i=2) 2289.19</td>
    <td>(i=1) 959.07<br>(i=2) 2199.82</td>
    <td>(i=1) 1063.03<br>(i=2) 1941.19</td>
  </tr>
  <tr>
    <td>$\omega_{1,0}$</td>
    <td>903.72</td>
    <td>927.48</td>
    <td>999.57</td>
  </tr>
  <tr>
    <td>$\omega_{2,0}$</td>
    <td>2277.20</td>
    <td>2162.48</td>
    <td>1867.59</td>
  </tr>
  <tr>
    <td>$\gamma_{\text{PIMD}}^{(i=1)}$</td>
    <td>0.699</td>
    <td>0.6849</td>
    <td>0.6581</td>
  </tr>
  <tr>
    <td>$\gamma_{\text{PIMD}}^{(i=2)}$</td>
    <td>0.9345</td>
    <td>0.9126</td>
    <td>0.8388</td>
  </tr>
</tbody>
</table>

overall performance of the estimators is still quantitative valid in the presence of interaction between anharmonic degrees of freedom. Therefore, we expect their reliability also in the truly many-body situation of real solids, as we will show in the diamond benchmark system.

### C. Diamond

The first crystalline system that we analyse is diamond, for which a vast literature of both experimental and theoretical results exists $^{64-67}$. We performed a classical MD simulation and a PIMD one to compare the results and study the impact of quantum effects. In both cases, we kept the temperature constant at 300 K and in PIMD we employed 12 beads that were enough to converge the kinetic energy estimators. For both MD and PIMD simulations, the supercell is made by $2 \times 2 \times 2$ conventional cells of diamond (each containing 8 atoms). The convergence with respect to the supercell size and the other DFT parameters was checked using DFPT simulations as implemented within Quantum Espresso $^{35}$ (QE). All the estimators in MD and PIMD were computed using a PBE exchange-correlation functional and ultrasoft pseudopotential that we took from the QE webpage. The classical MD simulation was run using the algorithm implemented as in Ref. 29 for the integration of EOMs. For this case, the time-step integrator was set to 0.5 fs, while DFT energy cut-off was set equal to 60 Ry for wavefunctions (480 Ry for charge density). The k-mesh to integrate over the Brillouin zone was equal to $2 \times 2 \times 2$ and the MD simulation lasted for 31 ps. Results are reported in Fig. 5(a).

Diamond is an interesting system to test our estimators because at $\Gamma$ there is a weak but sizeable renormalization of the Raman frequency due to anharmonic effects, which is estimated to be $15\ \text{cm}^{-1}$ in Ref. 68 and $17.4\ \text{cm}^{-1}$ in Ref. 69. Raman frequencies are associated to transitions between vibrational (and rotational if present) states; therefore we expect to retrieve this effect through the quantum displacement-displacement estimator.

The relative shift of the classical displacement-displacement with respect to the DFPT harmonic calculation at $\Gamma$ is $7\pm2$ $\text{cm}^{-1}$ at 300 K. We exclude that the Raman shift is due to anharmonic temperature effects the classical phonon simulations could capture. Indeed, it is known that the impact of temperature in diamond is marginal in the [0-300] K range. Experimentally, the Raman mode shift is less than $1\ \text{cm}^{-1}$ in this temperature interval $^{64}$. Thus, we deduce that this energy difference is due to anharmonic quantum effects that classical MD cannot fully capture. In order to recover a renormalization similar to the predicted one, one should take into account quantum effects. In Fig. 5(c), we plot the phonon dispersions from PIMD simulations. The latter lasted 34 ps, with a time-step integrator of 0.75 fs. The DFT parameters for the calculation of the BO surface during the dynamics are the same as in the MD case. While the overall shape looks very similar to the classical MD case and to the DFPT calculation, in this case the displacement-displacement estimator gives us a renormalization of $13.7\pm2\ \text{cm}^{-1}$ at $\Gamma$, in accordance with the theoretical prediction in Ref. 68.

Although we can reproduce the anharmonic shift at $\Gamma$ and the theoretical calculations at DFT-PBE level reported in Ref. 68, we notice that the absolute value of the optical mode at $\Gamma$ does not agree with the experimental one $^{64,65}$. For instance, while the experimental first-order Raman mode is $\sim$1332.8 $\text{cm}^{-1}$, our displacement-displacement estimator gives 1276.9

![](./images/867770780115533962_5.jpg)

FIG. 5. Diamond: (a) Phonon dispersion and DOS obtained from classical MD simulations at 300 K compared with DFPT calculation; (b) classical MD: zoom around the optical region; (c) Phonon dispersion and DOS obtained from PIMD simulations at 300 K with 12 beads compared with DFPT calculation; (d) PIMD: zoom around the optical region.

$\text{cm}^{-1}$. This is due to the failure of the PBE functional that does not describe correctly the electronic correlation $^{68}$. To overcome this issue a full Quantum Monte Carlo calculation of the phonon dispersion for diamond was performed in Ref. 70. In particular, the $\langle \delta x \delta x \rangle$ curve in Fig. 5(c), is the same reported in Ref. 70 where it was used to renormalize the Quantum Monte Carlo phonon dispersion by anharmonic contributions. Using the Variational Monte Carlo as electronic solver, the estimated Raman frequency is $1336.9\ \text{cm}^{-1}$.

## D. I4$_1$/amd high-pressure phase of hydrogen

The determination of the phase diagram of solid hydrogen at high pressures is one of the major challenges in condensed matter physics. Indeed, as hydrogen is the lightest element, it is characterized by large NQE and show strong anharmonicity. Therefore, a good application for the PIMD estimators is the I4$_1$/amd phase of atomic hydrogen at 500 Gpa, which is predicted to be the first atomic metallic phase above $490\ \text{Gpa}^{71,73}$. We thus performed MD and PIMD simulations at both 20 K and 120 K, to compare the relative impact of quantum and thermal effects.

The unit cell of tetragonal I4$_1$/amd atomic hydrogen is made of two atoms. We set $a = 2.286$ bohr and $c = 5.820$ bohr as lattice parameters, taken from Ref. 71. These values correspond to a pressure of 500 GPa, as estimated by DFT calculations with the PBE exchange-correlation functional. In order to sample the phonon dispersion, we used a $3 \times 3 \times 3$ supercell, made of 54 atoms. As this phase is metallic, a fine k-mesh in reciprocal space is required for the electronic integration over the Brillouin zone (BZ). At DFPT level, convergence on the phonon dispersion is reached using a $30 \times 30 \times 30$ k-space grid in the unit cell. This corresponds to a $10 \times 10 \times 10$ k-mesh for the supercell. In our calculations, the plane-wave (density) energy cutoff is set equal to 50 Ry (330 Ry), and the Gaussian smearing is 0.03 Ry. For both temperatures, the classical MD time-step $\Delta t$ is 0.5 fs , while in PIMD simulations $\Delta t = 0.9$ fs. In the latter case, the number of beads is $P = 120$ ($P = 50$) for the simulations at 20 K (120 K). $P$ is chosen by studying the convergence of the virial and primitive kinetic energy estimators $^{28,29}$ (see appendix E). The simulation length is 10 ps for classical MD, while it is 6 ps for PIMD. Remarkably, we find that such total simulation times are enough to achieve an error bar of less than $10\ \text{cm}^{-1}$ on the phonon eigenvalues in almost all cases. This is thanks to the generalized eigenvalue problems, as formulated in Eqs. (21) and (24). The hardest case is the PIMD simulation at 20 K, which requires a larger number of beads, $P = 120$. Even in this situation, the error bar does not exceed $50\ \text{cm}^{-1}$. In App. E, we plot the convergence of phonon frequencies at $\Gamma$ and M points as a function of the simulation time. The frequencies are very stable after a short equilibration time of $\approx 1.5$ ps, with no drift and very small statistical fluctuations afterwards.

As a last technical remark, it is worth noting that the size of the $3 \times 3 \times 3$ q-point grid sampled by the MD/PIMD supercell is not enough to interpolate the phonon dispersion on a dense q-mesh. Indeed, from DFPT calculations, it turns out that a finer $6 \times 6 \times 6$ mesh is needed for interpolation. Therefore, assuming that the anharmonic corrections are shorter-ranged, we interpolate the difference between the harmonic and anharmonic force constant matrices on the $3 \times 3 \times 3$ grid. We then add this anharmonic correction to the force constant matrix obtained on a finer $6 \times 6 \times 6$ mesh from DFPT calculations. This scheme has previously been employed in SSCHA calculations of analogous systems $^{23,71}$.

In Figs. 6(a) and 6(b), we plot the phonon dispersions at 20 K from classical and PIMD estimators, respectively; Figs. 6(c) and 6(d) show classical and quantum dispersions at 120 K. At 20 K, the classical MD estimators both agree very well with harmonic DFPT calculations, as one would expect at such a low temperature. In the quantum case, the dispersion of the phonon frequencies computed through the force-force estimator follows well the SSCHA dispersion $^{71}$, computed as q-dependent set of eigenvalues, diagonalizing the best auxiliary harmonic potential that minimizes the vibrational free energy. The force-

![](./images/867770780115533962_6.jpg)

FIG. 6. $I4_1/amd$ atomic phase of hydrogen at 500 GPa: (a) Phonon dispersion obtained from MD simulations at 20 K compared with DFPT calculation (red) and SSCHA$^{71}$ (yellow). The red curve is perfectly covered by the force-force phonon estimator (blue); (b) Phonon dispersion obtained from PIMD simulations at 20 K compared with DFPT calculation (red) and SSCHA (yellow); (c) same as (a), but at 120 K; (d) same as (b) but at 120 K. In panel (d), for the quantum displacement-displacement estimator, we plot the energies only at the q-points sampled by the simulations, because the dynamical matrix is harder to interpolate in this case. The data in Ref. 71 were digitalized using WebPlotDigitizer$^{72}$.

![](./images/867770780115533962_7.jpg)

FIG. 7. $I4_1/amd$ atomic phase of hydrogen at 500 GPa: (a) Total phonon DOS obtained from classical MD simulations at 20 K compared with DFPT calculation (red); (b) Total phonon DOS obtained from PIMD simulations at 20 K compared with DFPT calculation (red).

force estimator is quite close to the harmonic DFPT phonons as well. However, the displacement-displacement PIMD estima- tor strongly renormalizes the harmonic curve. In particular, the quantum displacement-displacement optical branches are soft- ened by $200$-$300\ \mathrm{cm}^{-1}$ on average. Therefore, the simulations at 20 K reveal the presence of strong NQE and anharmonicity. While we can quantify the anharmonic strength by compar- ing the quantum force-force and displacement-displacement curves, in this case the temperature dependence of the classical simulations also suggests a large deviation from the harmonic behavior. Indeed, at variance with the low temperature case, at120 K the classical displacement-displacement estimator gives results that are significanlty different than DFPT (Fig. 6(c)). Anharmonicity makes the classical phonon frequencies de- pend on temperature. On the other hand, the PIMD curves seem to be less affected by temperature effects, as NQE pre- vail (Fig. 6(d)).

The shape of phonon dispersions is reflected in the phonon density of states (DOS), that we plot for classical MD and PIMD simulations at 20 K in Figs. (7(a)) and (7(b)), respec- tively. In particular, the quantum displacement-displacement DOS can be directly compared with vibrational spectroscopies, as it is the density distribution of the lowest-energy phonon excitations (green line in Fig. (7(b))). Instead, the force-force and harmonic DOS are ground state approximations of the spectrum. Fig. (7(b)) shows that quantum effects lead to a siz-able red-shift, due to anharmonicity, which amounts to $\approx 250$ cm-1, if one compares lowest-energy excitations with fun- damental frequencies. A similar shift has been predicted in Ref. 74 for high-pressure molecular hydrogen, by means of a time-dependent SSCHA formulation.

From these results, we infer that the form of the poten- tial felt by phonons in the atomic phase of hydrogen is far from being harmonic, as previously supposed $^{71}$ based on the estimate of the fundamental frequencies only. Rather, the comparison between fundamental and excited-states quanti- ties obtained from the two quantum estimators allows one to capture a non-negligible anharmonic behavior. Thus, the consistent evaluation of both quantum estimators within the same PIMD framework is a valuable strategy to characterize the shape of the many-body interaction potential felt by the phonon quasiparticles.

## IV. CONCLUSION

This work lays down the formalism to extend in a trans- parent way phonon dispersion calculations from classical to path integral molecular dynamics simulations. The proposed phonon quantum estimators are built upon zero-time Kubo- transformed quantum correlation functions, and are tested over toy-model potentials where exact results can be compared with from the numerical solution of the Schrödinger equation.

We derived two classes of PIMD phonon estimators, based on the displacement auto-correlation and force auto- correlation functions, respectively. In particular, we have shown that while the force-force quantum correlators give ac- cess to the fundamental frequencies and thermodynamic prop- erties of the quantum system, the displacement-displacement correlators probe the lowest-energy phonon excitations, and so the low-energy phonon spectroscopy with high accuracy. We have also shown that the simultaneous evaluation of quantum force-force and displacement-displacement phonon estimators gives a precious insight into the anharmonicity strength of the system, within the same framework.

Furthermore, the rigorous quantization of classical equa- tions performed in this work allowed us to write down a gen- eralized eigenvalue problem for the effective normal modes determination, borrowed from the classical localization prin- ciple of the velocity power spectrum. We prove that the use of generalized eigenvalue equations in place of standard normal mode equations leads to a remarkable speed-up in the PIMD phonon calculations, both in terms of faster convergence rate and smaller time-step bias. The approach we propose gives converged eigenvalues at a lower computational cost and with a much smaller error bar. Overall, a one-order-of-magnitude gain is expected when PIMD phonons are computed through a generalized eigenvalues problem, either based on force or on displacement autocorrelation functions.

Our method relies on the PIOUD algorithm to integrate the path integral equation of motions in a Langevin framework. This algorithm allows one to run very efficient PIMD simula- tions. Our approach is fully ab initio, the BO interaction po- tential for nuclei being computed at the DFT level. We applied this to the calculation of phonon properties of diamond and atomic hydrogen using PBE-DFT as solver for the electronic part. Nevertheless, concerning the BO surface, PIOUD can also deal with stochastic approaches such as Quantum Monte Carlo (QMC). Therefore, the PIMD formalism developed here for phonons calculations in quantum systems is already QMC- compliant $^{28,75}$ . This feature can open interesting avenues in the future, and it represents a strong appeal for using our method when facing with strongly correlated materials.

Finally, we believe that this framework is particularly suit- able for a better understanding of the recent experimental discovery of high-temperature high-pressure superconductors, such as $H_3S$ and $LaH_{10}$, where the fundamental role played by hydrogen in making these materials superconducting is al- ready known $^{76,77}$ . Indeed, our approach takes into account NQE, phonon anharmonicity and temperature effects together, in a non-perturbative way, without relying on any harmonic or self-consistent theory. In this sense, it goes beyond current approximations limiting state-of-the-art methods.

## ACKNOWLEDGMENTS

T.M. and M.C. are grateful to the French grand équipement national de calcul intensif (GENCI) for the computational time provided under Project No. 0906493. T.M. and M.C. acknowl- edge that this work was supported by French state funds man- aged by the ANR within the Investissements d'Avenir pro- gramme under reference ANR-11-IDEX-0004-02, and more specifically within the framework of the Cluster of Excellence MATISSE led by Sorbonne University. All the authors thank Lorenzo Monacelli for useful discussions.

This work is partially supported by the European Centre of Excellence in Exascale Computing TREX - Targeting Real Chemical Accuracy at the Exascale. This project has received funding from the European Union's Horizon 2020 - Research and Innovation program - under grant agreement no. 952165.

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

### Appendix A: Relation between Kubo-transformed force constant matrix and PIMD force-force correlation functions

In this appendix we review some properties of the PIMD force-force correlation functions.

The Kubo-transformed force constant matrix can be derived exactly from the force-force correlation matrix in the following way:
$$
\begin{aligned}
&\left\langle\left\langle\frac{1}{P^{2}} \sum_{j_{1}, j_{2}=1}^{P} \frac{\partial^{2} \mathcal{V}}{\partial x_{i_{1}}^{\left(j_{1}\right)} \partial x_{i_{2}}^{\left(j_{2}\right)}}\right\rangle\right\rangle= \\
&=\int d^{f} \mathbf{p} e^{-\beta_{P} T_{P}} \int d^{f} \mathbf{x} \frac{1}{P^{2}} \sum_{j_{1}, j_{2}=1}^{P} \frac{\partial^{2} \mathcal{V}}{\partial x_{i_{1}}^{\left(j_{1}\right)} \partial x_{i_{2}}^{\left(j_{2}\right)}} \frac{e^{-\beta_{P} V_{P}}}{Z} \\
&=\beta_{P} \int d^{f} \mathbf{p} e^{-\beta_{P} T_{P}} \int d^{f} \mathbf{x} \frac{1}{P^{2}}\left(\sum_{j_{1}=1}^{P} \frac{\partial \mathcal{V}}{\partial x_{i_{1}}^{\left(j_{1}\right)}}\right)\left(\sum_{j_{2}=1}^{P} \frac{\partial V_{P}}{\partial x_{i_{2}}^{\left(j_{2}\right)}}\right) \frac{e^{-\beta_{P} V_{P}}}{Z} \\
&=\beta \int d^{f} \mathbf{p} e^{-\beta_{P} T_{P}} \int d^{f} \mathbf{x} \frac{1}{P^{2}}\left(\sum_{j_{1}=1}^{P} \frac{\partial \mathcal{V}}{\partial x_{i_{1}}^{\left(j_{1}\right)}}\right)\left(\sum_{j_{2}=1}^{P} \frac{\partial \mathcal{V}}{\partial x_{i_{2}}^{\left(j_{2}\right)}}\right. \\
&\left.\quad+\frac{1}{P} \sum_{j_{2}=1}^{P} m_{i_{2}} \omega_{P}^{2}\left(2 x_{i_{2}}^{\left(j_{2}\right)}-x_{i_{2}}^{\left(j_{2}+1\right)}-x_{i_{2}}^{\left(j_{2}-1\right)}\right)\right) \frac{e^{-\beta_{P} V_{P}}}{Z} \\
&=\beta \int d^{f} \mathbf{p} e^{-\beta_{P} T_{P}} \int d^{f} \mathbf{x} \frac{1}{P^{2}}\left(\sum_{j_{1}=1}^{P} \frac{\partial \mathcal{V}}{\partial x_{i_{1}}^{\left(j_{1}\right)}}\right)\left(\sum_{j_{2}=1}^{P} \frac{\partial \mathcal{V}}{\partial x_{i_{2}}^{\left(j_{2}\right)}}\right) \frac{e^{-\beta_{P} V_{P}}}{Z} \\
&=\beta \int d^{f} \mathbf{p} e^{-\beta_{P} T_{P}} \int d^{f} \mathbf{x} \mathrm{F}_{i_{1}} \mathrm{~F}_{i_{2}} \frac{e^{-\beta_{P} V_{P}}}{Z}=\beta\left\langle\left\langle\mathrm{F}_{i_{1}} \mathrm{~F}_{i_{2}}\right\rangle\right\rangle, \quad \text { (A1) }
\end{aligned}
$$
where we integrated by parts with respect to $x_{i_{2}}^{(j_{2})}$ between the second and the third row and where we used the fact that $\sum_{j_{2}=1}^{P}(2 x_{i_{2}}^{(j_{2})}-x_{i_{2}}^{(j_{2}+1)}-x_{i_{2}}^{(j_{2}-1)})=0$. This relation extends the classical one in Eq. (14) in a transparent way. On the other hand, if one considers the equal-time correlation functions in Eq. (9) and tries to obtain the force constant matrix using them instead of the Kubo ones, he would end up with:
$$
\begin{aligned}
&\left\langle\left\langle\frac{1}{P} \sum_{j=1}^{P} \frac{\partial^{2} \mathcal{V}}{\partial x_{i_{1}}^{(j)} \partial x_{i_{2}}^{(j)}}\right\rangle\right\rangle= \\
&=\int d^{f} \mathbf{p} e^{-\beta_{P} T_{P}} \int d^{f} \mathbf{x} \frac{1}{P} \sum_{j=1}^{P} \frac{\partial^{2} \mathcal{V}}{\partial x_{i_{1}}^{(j)} \partial x_{i_{2}}^{(j)}} \frac{e^{-\beta_{P} V_{P}}}{Z} \\
&=\beta_{P} \int d^{f} \mathbf{p} e^{-\beta_{P} T_{P}} \int d^{f} \mathbf{x} \frac{1}{P}\left(\sum_{j=1}^{P} \frac{\partial \mathcal{V}}{\partial x_{i_{1}}^{(j)}} \frac{\partial V_{P}}{\partial x_{i_{2}}^{(j)}}\right) \frac{e^{-\beta_{P} V_{P}}}{Z}(\mathrm{~A} 2)
\end{aligned}
$$
where the term inside the parenthesis is
$$
\begin{aligned}
& \sum_{j=1}^{P} \frac{\partial \mathcal{V}}{\partial x_{i_{1}}^{(j)}} \frac{\partial V_{P}}{\partial x_{i_{2}}^{(j)}}= \\
& =\sum_{j=1}^{P} F_{i_{1}}^{(j)}\left[F_{i_{2}}^{(j)}+m_{i_{2}} \omega_{P}^{2}\left(2 x_{i_{2}}^{(j)}-x_{i_{2}}^{(j+1)}-x_{i_{2}}^{(j-1)}\right)\right].(\mathrm{A} 3)
\end{aligned}
$$

Last expression clearly shows that the equal-time force corre- lation contains the fictitious interbead coupling terms which make it different from the physical force constant matrix. For our purposes, this result supports the use of Kubo-transformed correlation functions in place of the equal-time ones.

### Appendix B: Low temperature limit of quantum correlation functions

In the limit of low temperature $T \rightarrow 0$ ($\beta \rightarrow \infty$ and $Z \approx$ $\sum_{i=1}^{N_{deg}} e^{-\beta E_{i}}$ where $N_{deg}$ is the number of states close to the ground state, as in the double well potentials with high barri- ers), the true quantum thermal zero-time correlation function, decomposed like the Kubo-transformed one in Eq. (25) be- comes:
$$
\begin{gathered}
\lim _{\beta \rightarrow \infty} c_{A B}=\frac{1}{Z} \sum_{n=1}^{N_{d e g}} e^{-\beta E_{n}}\left[A_{n n} B_{n n}+\sum_{m \neq n} A_{n m} B_{m n}\right] \\
\text { if } N_{d e g}=1 \quad c_{A B} \sim A_{00} B_{00}+\sum_{m>0} A_{0 m} B_{m 0}. \quad \text { (B1) }
\end{gathered}
$$

It is worth noting that if $N_{deg}$=1, at $t=0$ the true quantum correlation functions can be written as an expectation value over the ground state.
$$
\lim _{\beta \rightarrow \infty} c_{A B} \sim\left\langle 0\left|A B^{+}\right| 0\right\rangle. \quad \text { (B2) }
$$

On the other hand for the Kubo-transformed correlation func- tion one can find:
$$
\begin{gathered}
\lim _{\beta \rightarrow \infty} \tilde{c}_{A B}=\frac{1}{Z} \sum_{n=1}^{N_{d e g}} e^{-\beta E_{n}}\left[A_{n n} B_{n n}+2 \sum_{m>n} A_{n m} B_{m n} \cdot \frac{1-e^{-\beta \hbar \omega_{m, n}}}{\beta \cdot \hbar \omega_{m, n}}\right] \\
\text { if } N_{d e g}=1 \quad \tilde{c}_{A B} \sim A_{00} B_{00}+2 \sum_{m>0} \frac{A_{0 m} B_{m 0}}{\beta \cdot \omega_{m, 0}}. \quad \text { (B3) }
\end{gathered}
$$

Differently from the true quantum case, it is worth noting that the zero-time Kubo correlator cannot be reduced into an expectation value over the ground state as Eq. (B2).

### Appendix C: Convergence of the phonon frequencies from the generalized eigenvalue equation versus the standard eigenvalue equation

Here we investigate the behaviour of the GEV and standard estimators already presented in the main text in II G for a Morse potential. We extend this analysis by including the

![](./images/867770780115533962_8.jpg)

FIG. 8. Convergence of the PIMD estimators for a 1D degree of freedom bounded by a quartic potential at 100 K obtained with different time-step $\Delta t$. The exact solutions that we obtain from the numerical Schrödinger equation are given in red for the force-force and orange for the displacement-displacement.

![](./images/867770780115533962_9.jpg)

FIG. 9. Convergence of the PIMD estimators for a 1D degree of freedom bounded by a symmetric double well potential at 100 K obtained with different time-step $\Delta t$. The exact solutions that we obtain from the numerical Schrödinger equation are given in red for the force-force and orange for the displacement-displacement.

case of a quartic potential (Fig. (8)), that we choose equal to $V(x)=k \cdot x^{4}$ and a symmetric double well potential (SDW in Fig. (9)), $V(x)=k \cdot(x^{2}-0.19)^{2}$ , where $k=0.483736$ a.u. like in the Morse case. The temperature is always equal to 100 K and the number of beads is equal to 120 for the quartic and 160 for the symmetric double well. We observe that GEV solutions converge always faster and with less oscillations to the exact value (computed from the Schrödinger equation). However, at variance with the Morse potential reported in the main text, we denote a small error of the GEV solutions for a time-step integrator of 1 fs.

## Appendix D: Schemes for the solution of the numerical Schrödinger equations

In the 1D case, the Schrödinger equation is discretized using finite differences on a fine mesh $(2 \cdot 10^{5}$ points). The discretized Hamiltonian is tridiagonal, thus easily diagonalizable using Lapack package $^{78}$ . Indeed, the potentials that we consider are bounded for $x \to \pm \infty$ except for the Morse that for $x \to+\infty$ tends to a finite value. However, in the region where $\frac{d V}{d x}=0$ , we are able to reproduce analytical results for the harmonic and Morse potential eigenvalues with an error $<0.01 ~cm^{-1}$ until the tenth bound state, that is enough to build our correlation functions at 20 K. For the 2D case, we still use finite differences for discretizing the Schrödinger equation in a real space square grid, but then the Laplace operator is not tridiagonal. Our real space grid is made of $1.5 \cdot 10^{3} \times 1.5 \cdot 10^{3}$ points, resulting in a $2.25 \cdot 10^{6} \times 2.25 \cdot 10^{6}$ Hamiltonian matrix. Instead of diagonalizing exactly the huge discretized Hamil-

![](./images/867770780115533962_10.jpg)

FIG. 10. Two harmonic potentials coupled by a term of the type $\zeta \cdot x_{1} \cdot x_{2}$.

<table><caption>TABLE VI. Two harmonic oscillators $(c_{11}=c_{12}=0.147$ a.u. in Eq. (D1)) with coupling potential $\zeta \cdot x_{1} \cdot x_{2}$ . The energies are given in $cm^{-1}$ .</caption>
<tbody>
<tr>
<td>$\zeta / c_{11}$</td>
<td>0.0</td>
<td>0.1</td>
<td>0.5</td>
</tr>
<tr>
<td>$\omega_{F F, i}$</td>
<td>(i=1) 1963.29</td>
<td>(i=1) 1862.54</td>
<td>(i=1) 1388.25</td>
</tr>
<tr>
<td></td>
<td>(i=2) 1963.29</td>
<td>(i=2) 2059.12</td>
<td>(i=2) 2404.53</td>
</tr>
<tr>
<td>$ZPE_{PIMD}$</td>
<td>1963.29</td>
<td>1960.83</td>
<td>1896.39</td>
</tr>
<tr>
<td>$ZPE_{exact}$</td>
<td>1962.91</td>
<td>1960.45</td>
<td>1896.03</td>
</tr>
<tr>
<td>$\omega_{\delta x \delta x, i}$</td>
<td>(i=1) 1962.78</td>
<td>(i=1) 1862.05</td>
<td>(i=1) 1387.90</td>
</tr>
<tr>
<td></td>
<td>(i=2) 1962.78</td>
<td>(i=2) 2058.58</td>
<td>(i=2) 2403.91</td>
</tr>
<tr>
<td>$\omega_{1,0}$</td>
<td>1962.78</td>
<td>1862.05</td>
<td>1387.90</td>
</tr>
<tr>
<td>$\omega_{2,0}$</td>
<td>1962.78</td>
<td>2058.58</td>
<td>2403.91</td>
</tr>
<tr>
<td>$\gamma_{PIMD}^{(i=1)}$</td>
<td>0.9997</td>
<td>0.9997</td>
<td>0.9997</td>
</tr>
<tr>
<td>$\gamma_{PIMD}^{(i=2)}$</td>
<td>0.9997</td>
<td>0.9997</td>
<td>0.9997</td>
</tr>
</tbody>
</table>

tonian, we employ the Arnoldi package $^{79}$ to compute only the

first twenty eigenvalues and eigenvectors, that are enough to evaluate the estimators. The wider mesh grid gives an error of the order $<2\ \text{cm}^{-1}$ on the eigenvalues that we check comparing them with 2D harmonic oscillators analytical solutions. In picture (10) we show an example of 2D harmonic oscillators coupled by an $\zeta \cdot x_1 \cdot x_2$ term:

$$V(x_1,x_2)=c_{11}\cdot x_1^2+c_{12}\cdot x_2^2+\zeta \cdot x_1 \cdot x_2. \tag{D1}$$

While we know that in the harmonic case, both the displacement-displacement and force-force estimators give the same correct result, in Tab. VI we can observe a difference always smaller than $1\ \text{cm}^{-1}$ between displacement-displacement and force-force which is due to numerical errors.

## Appendix E: Convergence of phonon frequencies for I4₁/amd hydrogen

We present in Fig. 11 the convergence of the kinetic energy estimators (virial and primitive$^{28}$) for I4₁/amd hydrogen with respect the number of beads at 20 K. Although using 120

![](./images/867770780115533962_11.jpg)

FIG. 11. Convergence of the virial (blue) and primitive (red) kinetic energy estimators at 20 K for the I4₁/amd atomic hydrogen.

beads the kinetic energy is not fully converged, we choose this value for our simulations for computational reasons. Indeed, a larger value would have implied a lower time-step value and, of course, a longer simulation with additional CPU-time. The cost of this simulation was already around $2.5\cdot 10^5$ total CPU-hours.

Furthermore, we show that the length of $\sim 6$ ps is enough for the PIMD simulations of I4₁/amd hydrogen in order to get well converged phonon frequencies. As examples, in Fig. 12 we report the results at $\Gamma$, while in Fig. 13 the results at the M point. After 5 ps, we do not observe any significant change in the frequencies at the q-point sampled with the simulations and also in the phonon dispersions obtained from the successive interpolations.

$^1$M. Born and K. Huang, *Dynamical Theory of Crystal Lattices* (Oxford University Press, 1954).

![](./images/867770780115533962_12.jpg)

FIG. 12. Convergence of the optical phonon frequencies at $\Gamma$ point for the $\langle FF \rangle$ estimator.

![](./images/867770780115533962_13.jpg)

FIG. 13. Convergence of phonon frequencies at the M point of the Brillouin zone for the $\langle FF \rangle$ estimator.

$^2$E. B. Wilson, J. C. Decius, and P. C. Cross, *Molecular vibrations : the theory of infrared and Raman vibrational spectra*, corrected republication ed. (New York : Dover Publications, 1980) reprint of the 1955 ed. published by McGraw-Hill, New York.

$^3$J. Bardeen, L. N. Cooper, and J. R. Schrieffer, "Theory of superconductivity," Phys. Rev. **108**, 1175–1204 (1957).

$^4$G. R. Stewart, "Unconventional superconductivity," *Advances in Physics* **66**, 75–196 (2017), https://doi.org/10.1080/00018732.2017.1331615.

$^5$A. P. Drozdov, M. I. Eremets, I. A. Troyan, V. Ksenofontov, and S. I. Shylin, "Conventional superconductivity at 203 kelvin at high pressures in the sulfur hydride system," *Nature* **525**, 73–76 (2015).

$^6$A. P. Drozdov, P. P. Kong, V. S. Minkov, S. P. Besedin, M. A. Kuzovnikov, S. Mozaffari, L. Balicas, F. F. Balakirev, D. E. Graf, V. B. Prakapenka, E. Greenberg, D. A. Knyazev, M. Tkacz, and M. I. Eremets, "Superconductivity at 250 k in lanthanum hydride under high pressures," *Nature* **569**, 528 – 531 (2019).

$^7$B. Fultz, "Vibrational thermodynamics of materials," *Progress in Materials Science* **55**, 247 – 352 (2010).

$^8$L. Paulatto, F. Mauri, and M. Lazzeri, "Anharmonic properties from a generalized third-order ab initio approach: Theory and applications to graphite and graphene," Phys. Rev. B **87**, 214303 (2013).

$^{9}$M. Schmitz and P. Tavan, "Vibrational spectra from atomic fluctua- tions in dynamics simulations. i. theory, limitations, and a sample ap- plication," The Journal of Chemical Physics 121, 12233-12246 (2004), https://aip.scitation.org/doi/pdf/10.1063/1.1822914.

$^{10}$M. Martinez, M.-P. Gaigeot, D. Borgis, and R. Vuilleumier, "Ex- tracting effective normal modes from equilibrium dynamics at finite temperature," The Journal of Chemical Physics 125, 144106 (2006), https://doi.org/10.1063/1.2346678.

$^{11}$O. Hellman, I. A. Abrikosov, and S. I. Simak, "Lattice dynamics of anhar- monic solids from first principles," Phys. Rev. B 84, 180301 (2011).

$^{12}$O. Hellman, P. Steneteg, I. A. Abrikosov, and S. I. Simak, "Temperature dependent effective potential method for accurate free energy calculations of solids," Phys. Rev. B 87, 104111 (2013).

$^{13}$E. Noukaras, G. Kalosakas, C. Galiotis, and K. Papagelis, "Phonon prop- erties of graphene derived from molecular dynamics simulations," Scientific Reports 5 (2015), 10.1038/srep12923.

$^{14}$L. T. Kong, "Phonon dispersion measured directly from molecular dynamics simulations," Computer Physics Communications 182, 2201 - 2207 (2011).

$^{15}$Throughout this work we refer to phonons for both molecules and crystal systems.

$^{16}$H. Dammak, Y. Chalopin, M. Laroche, M. Hayoun, and J.-J. Greffet, "Quantum thermal bath for molecular dynamics simulation," Phys. Rev. Lett. 103, 190601 (2009).

$^{17}$H. Dammak, E. Antoshchenkova, M. Hayoun, and F. Finocchi, "Isotope effects in lithium hydride and lithium deuteride crystals by molecular dy- namics simulations," Journal of Physics: Condensed Matter 24, 435402 (2012).

$^{18}$Y. Bronstein, P. Depondt, F. Finocchi, and A. M. Saitta, "Quantum-driven phase transition in ice described via an efficient langevin approach," Phys. Rev. B 89, 214101 (2014).

$^{19}$Y. Bronstein, P. Depondt, L. Bove, R. Gaál, A. Saitta, and F. Finocchi, "Quantum versus classical protons in pure and salty ice under pressure," Physical Review B 93, 024104 (2016).

$^{20}$M. Ben-Nun and R. D. Levine, "On the zero point energy in classical trajectory computations," The Journal of Chemical Physics 105, 8136-8141 (1996), https://doi.org/10.1063/1.472668.

$^{21}$E. Mangaud, S. Huppert, T. Plé, P. Depondt, S. Bonella, and F. Finocchi, "The fluctuation-dissipation theorem as a diagnosis and cure for zero-point energy leakage in quantum thermal bath simulations," J. Chem. Theory Comput. 15, 2863 - 2880 (2019).

$^{22}$D. Hooton, "Li. a new treatment of anharmonicity in lattice ther- modynamics: I," The London, Edinburgh, and Dublin Philo- sophical Magazine and Journal of Science 46, 422-432 (1955), https://doi.org/10.1080/14786440408520575.

$^{23}$I. Errea, M. Calandra, and F. Mauri, "Anharmonic free energies and phonon dispersions from the stochastic self-consistent harmonic approxi- mation: Application to platinum and palladium hydrides," Phys. Rev. B 89, 064302 (2014).

$^{24}$R. Bianco, I. Errea, L. Paulatto, M. Calandra, and F. Mauri, "Second- order structural phase transitions, free energy curvature, and temperature- dependent anharmonic phonons in the self-consistent harmonic approxi- mation: Theory and stochastic implementation," Phys. Rev. B 96, 014111 (2017).

$^{25}$P. Souvatzis, O. Eriksson, M. I. Katsnelson, and S. P. Rudin, "Entropy driven stabilization of energetically unstable crystal structures explained from first principles theory," Phys. Rev. Lett. 100, 095901 (2008).

$^{26}$N. R. Werthamer, "Self-consistent phonon formulation of anharmonic lattice dynamics," Phys. Rev. B 1, 572-581 (1970).

$^{27}$T. Tadano and S. Tsuneyuki, "Self-consistent phonon calculations of lattice dynamical properties in cubic srtio₃ with first-principles anharmonic force constants," Phys. Rev. B 92, 054301 (2015).

$^{28}$F. Mouhat, S. Sorella, R. Vuilleumier, A. M. Saitta, and M. Casula, "Fully quantum description of the zundel ion: Combining variational quantum monte carlo with path integral langevin dynamics," Journal of Chemi- cal Theory and Computation 13, 2400-2417 (2017), pMID: 28441484, https://doi.org/10.1021/acs.jctc.7b00017.

$^{29}$M. Ceriotti, M. Parrinello, T. Markland, and D. Manolopoulos, "Efficient stochastic thermostatting of path integral molecular dynamics," The Journal of chemical physics 133, 124104 (2010).

$^{30}$M. Ceriotti, D. E. Manolopoulos, and M. Parrinello, "Accelerat- ing the convergence of path integral dynamics with a generalized langevin equation," The Journal of Chemical Physics 134, 084104 (2011), https://doi.org/10.1063/1.3556661.

$^{31}$R. P. Feynman and A. R. Hibbs, Quantum Mechanics and Path Integrals (McGraw-Hill, New York, 1965).

$^{32}$D. M. Ceperley, "Path integrals in the theory of condensed helium," Rev. Mod. Phys. 67, 279-355 (1995).

$^{33}$M. Parrinello and A. Rahman, "Study of an f center in molten kcl," The Journal of Chemical Physics 80, 860-867 (1984), https://doi.org/10.1063/1.446740.

$^{34}$M. Rossi, V. Kapil, and M. Ceriotti, "Fine tuning classical and quantum molecular dynamics using a generalized langevin equation," The Journal of Chemical Physics 148, 102301 (2018), https://doi.org/10.1063/1.4990536.

$^{35}$P. G. et al., "Quantum espresso: a modular and open-source software project for quantum simulations of materials," Journal of Physics: Condensed Mat- ter 21, 395502 (2009).

$^{36}$P. Hohenberg and W. Kohn, "Inhomogeneous electron gas," Phys. Rev. 136, B864-B871 (1964).

$^{37}$W. Kohn and L. J. Sham, "Self-consistent equations including exchange and correlation effects," Phys. Rev. 140, A1133-A1138 (1965).

$^{38}$I. R. Craig and D. E. Manolopoulos, "Quantum statistics and classical mechanics: Real time correlation functions from ring polymer molecu- lar dynamics," The Journal of Chemical Physics 121, 3368-3373 (2004), https://doi.org/10.1063/1.1777575.

$^{39}$T. J. H. Hele, "Thermal quantum time-correlation functions from classical-like dynamics," Molecular Physics 115, 1435-1462 (2017), https://doi.org/10.1080/00268976.2017.1303548.

$^{40}$R. Kubo, "Statistical-mechanical theory of irreversible processes. i. gen- eral theory and simple applications to magnetic and conduction prob- lems," Journal of the Physical Society of Japan 12, 570-586 (1957), https://doi.org/10.1143/JPSJ.12.570.

$^{41}$A. Witt, S. D. Ivanov, M. Shiga, H. Forbert, and D. Marx, "On the appli- cability of centroid and ring polymer path integral molecular dynamics for vibrational spectroscopy," The Journal of Chemical Physics 130, 194510 (2009), https://doi.org/10.1063/1.3125009.

$^{42}$T. J. H. Hele, "On the relation between thermostatting ring-polymer molecu- lar dynamics and exact quantum dynamics," Molecular Physics 114, 1461-1471 (2016), https://doi.org/10.1080/00268976.2015.1136003.

$^{43}$T. Yamamoto, "Quantum statistical mechanical theory of the rate of ex- change chemical reactions in the gas phase," The Journal of Chemical Physics 33, 281-289 (1960), https://doi.org/10.1063/1.1731099.

$^{44}$S. Habershon, D. E. Manolopoulos, T. E. Markland, and T. F. Miller, "Ring-polymer molecular dynamics: Quantum effects in chemical dy- namics from classical trajectories in an extended phase space," Annual Review of Physical Chemistry 64, 387-413 (2013), pMID: 23298242, https://doi.org/10.1146/annurev-physchem-040412-110122.

$^{45}$K. Parlinski, Z. Q. Li, and Y. Kawazoe, "First-principles determination of the soft mode in cubic zro₂," Phys. Rev. Lett. 78, 4063-4066 (1997).

$^{46}$A. Togo and I. Tanaka, "First principles phonon calculations in materials science," Scr. Mater. 108, 1-5 (2015).

$^{47}$X. Gonze and C. Lee, "Dynamical matrices, born effective charges, di- electric permittivity tensors, and interatomic force constants from density- functional perturbation theory," Phys. Rev. B 55, 10355-10368 (1997).

$^{48}$S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, "Phonons and related crystal properties from density-functional perturbation theory," Rev. Mod. Phys. 73, 515-562 (2001).

$^{49}$A. Pereverzev and T. D. Sewell, "Obtaining the hessian from the force covariance matrix: Application to crystalline explosives petn and rdx," The Journal of Chemical Physics 142, 134110 (2015), https://doi.org/10.1063/1.4916614.

$^{50}$M.-P. Gaigeot, M. Martinez, and R. Vuilleumier, "Infrared spectroscopy in the gas and liquid phase from first principle molecular dynamics simulations: application to small peptides," Molecular Physics 105, 2857-2878 (2007), https://doi.org/10.1080/00268970701724974.

$^{51}$B. R. Brooks, D. Janežič, and M. Karplus, "Harmonic analysis of large sys- tems. i. methodology," Journal of Computational Chemistry 16, 1522-1542 (1995), https://onlinelibrary.wiley.com/doi/pdf/10.1002/jcc.540161209.

$^{52}$R. A. Wheeler, H. Dong, and S. E. Boesch, "Quasiharmonic vibrations of water, water dimer, and liquid water from principal component analysis

of quantum or qm/mm trajectories," ChemPhysChem 4, 382-384 (2003), https://onlinelibrary.wiley.com/doi/pdf/10.1002/cphc.200390066.
53R. Ramírez and T. López-Ciudad, "The schrödinger formulation of the feynman path centroid density," The Journal of Chemical Physics 111, 3339-3348 (1999), https://doi.org/10.1063/1.479666.
54R. Ramírez and T. López-Ciudad, "Low lying vibrational excitation ener- gies from equilibrium path integral simulations," The Journal of Chemical Physics 115, 103-114 (2001), https://doi.org/10.1063/1.1378318.
55 However, in molecular calculations one has to define a proper frame for appropriate internal coordinates.
56*Space groups in reciprocal space and representations," in Group Theory(Springer Berlin Heidelberg, Berlin, Heidelberg, 2008) pp. 209-237.
57To do that we exploit the Quantum Espresso tool q2qstar.x.
 $^{58}$ W. Kolos and L. Wolniewicz, "Potential energy curves for the $x^{1} \sigma_{g}^{+}, b^{3} \sigma_{u}^{+}$ , and $c^{1} \pi_{u}$ states of the hydrogen molecule," The Journal of Chemical Physics43, 2429-2441 (1965), https://doi.org/10.1063/1.1697142.
59E. Matsushita and T. Matsubara, "Note on Isotope Effect in Hydro- gen Bonded Crystals," Progress of Theoretical Physics 67, 1-19 (1982), https://academic.oup.com/ptp/article-pdf/67/1/1/5438755/67-1-1.pdf.
60Q. Yu and J. M. Bowman, "How the zundel (h5o2+) potential can be used to predict the proton stretch and bend frequencies of larger protonated water clusters," The Journal of Physical Chemistry Letters 7, 5259-5265 (2016), pMID: 27973907, https://doi.org/10.1021/acs.jpclett.6b02561.
61F. Agostini, R. Vuilleumier, and G. Ciccotti, "Infrared spectroscopy and effective modes analysis of the protonated water dimer h+(h2o)2 at room temperature under h/d substitution," The Journal of Chemical Physics 134,084303 (2011), https://doi.org/10.1063/1.3521273.
62L. Wolniewicz, "Nonadiabatic energies of the ground state of the hydro- gen molecule," The Journal of Chemical Physics 103, 1792-1799 (1995), https://doi.org/10.1063/1.469753.
63E. Allin, A. McKague, V. Soots, and H. Welsh, "The raman spectrum of solid hydrogen," J. Phys. France 26, 615-620 (1965).
64M. S. Liu, L. A. Bursill, S. Prawer, and R. Beserman, "Temperature depen- dence of the first-order raman phonon line of diamond," Phys. Rev. B 61,3391-3395(2000).
65J. Kulda, H. Kainzmaier, D. Strauch, B. Dorner, M. Lorenzen, and M. Krisch, "Overbending of the longitudinal optical phonon branch in dia- mond as evidenced by inelastic neutron and x-ray scattering," Phys. Rev. B66,241202(2002).
66M. Schwoerer-BOhning, A. T. Macrander, and D. A. Arms, "Phonon dis- persion of diamond measured by inelastic x-ray scattering," Phys. Rev. Lett.80,5572-5575(1998).
67P. Pavone, K. Karch, O. Schütt, D. Strauch, W. Windl, P. Giannozzi, and S. Baroni, "Ab initio lattice dynamics of diamond," Phys. Rev. B 48, 3156-3163(1993).
68R. Maezono, A. Ma, M. D. Towler, and R. J. Needs, "Equation of state and raman frequency of diamond from quantum monte carlo simulations," Phys. Rev. Lett. 98, 025701 (2007).
69D. Vanderbilt, S. G. Louie, and M. L. Cohen, "Calculation of phonon- phonon interactions and the absence of two-phonon bound states in dia- mond," Phys. Rev. Lett. 53, 1477-1480 (1984).
70K. Nakano, T. Morresi, M. Casula, R. Maezono, and S. Sorella, "Atomic forces by quantum monte carlo: application to phonon dispersion calcula- tion,"(2020), arXiv:2012.01264 [cond-mat.mtrl-sci].
71M. Borinaga, I. Errea, M. Calandra, F. Mauri, and A. Bergara, "Anhar- monic effects in atomic hydrogen: Superconductivity and lattice dynamical stability," Phys. Rev. B 93, 174308 (2016).
72A. Rohatgi, "Webplotdigitizer: Version 4.3," (2020).
73C. J. Pickard and R. J. Needs, "Structure of phase iii of solid hydrogen," Nature Physics 3 (2007), 10.1038/nphys625.
74L. Monacelli and F. Mauri, "Time-dependent self consistent harmonic ap- proximation: Anharmonic nuclear quantum dynamics and time correlation functions,"(2020), arXiv:2011.14986 [cond-mat.stat-mech].
75G. Rillo, M. A. Morales, D. M. Ceperley, and C. Pierleoni, "Coupled electron-ion monte carlo simulation of hydrogen molecu- lar crystals," The Journal of Chemical Physics 148, 102314 (2018), https://doi.org/10.1063/1.5001387.
761. Errea, M. Calandra, C. J. Pickard, J. R. Nelson, R. J. Needs, Y. Li, H. Liu, Y. Zhang, Y. Ma, and F. Mauri, "Quantum hydrogen-bond symmetrization in the superconducting hydrogen sulfide system," Nature 532, 81-84 (2016).
771. Errea, F. Belli, L. Monacelli, A. Sanna, T. Koretsune, T. Tadano, R. Bianco, M. Calandra, R. Arita, F. Mauri, and J. A. Flores-Livas, "Quantum crystal structure in the 250-kelvin superconducting lanthanum hydride," Nature578,66-69(2020).
78E. Anderson, Z. Bai, C. Bischof, S. Blackford, J. Demmel, J. Dongarra, J. Du Croz, A. Greenbaum, S. Hammarling, A. McKenney, and D. Sorensen, LAPACK Users' Guide, 3rd ed. (Society for Industrial and Applied Mathe- matics, Philadelphia, PA, 1999).
79R. B. Lehoucq, D. C. Sorensen, and C. Yang, "Arpack users guide: Solution of large scale eigenvalue problems by implicitly restarted arnoldi methods."(1997).