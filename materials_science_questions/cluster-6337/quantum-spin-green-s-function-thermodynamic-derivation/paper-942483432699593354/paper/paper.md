
# Accessing Excitation Spectrum of Many-body Systems via Single-Mode Approximation within Quantum Monte Carlo Simulations

Yan Liu, \( ^{1} \)  Kemeng Wu, \( ^{1} \), Yan-Cheng Wang, \( ^{2,3} \)  Jie Lou, \( ^{1,4,*} \)  Zheng Yan, \( ^{5,6,7,†} \)  and Yan Chen \( ^{1,4,‡} \) 

 \( ^{1} \) Department of Physics and State Key Laboratory of Surface Physics, Fudan University, Shanghai 200438, China

 \( ^{2} \) Collaborative Center for Physics and Chemistry,

Institute of International Innovation, Beihang University, Hangzhou 311115, China

 \( ^{3} \) Tianmushan Laboratory, Hangzhou 311115, China

 \( ^{4} \) Collaborative Innovation Center of Advanced Microstructures, Nanjing 210093, China

 \( ^{5} \) Department of Physics, School of Science, Westlake University, Hangzhou 310030, China

 \( ^{6} \) Institute of Natural Sciences, Westlake Institute for Advanced Study, Hangzhou 310024, China

 \( ^{7} \) Lanzhou Center for Theoretical Physics & Key Laboratory of Theoretical Physics of Gansu Province, Lanzhou University, Lanzhou, Gansu 730000, China

We extend the Single Mode Approximation (SMA) into quantum Monte Carlo (QMC) simulations to provide an efficient and fast method to obtain the dynamical dispersion of quantum many-body systems. Based on Stochastic Series Expansion (SSE) and its projector algorithms, the SMA + SSE method can simply extract the dispersion of the dynamical spectrum in the long wave-length limit and the upper bound of the dispersion elsewhere, without external calculations and high technique barriers. Meanwhile, numerical analytic continuation methods require the fine data of imaginary time correlations and complex programming. Therefore, our method can approach the excitation dispersion of large systems, e.g., we take the two-dimensional Heisenberg model on a  \( 512 \times 512 \)  square lattice. We demonstrate the effectiveness and efficiency of our method with high precision via additional examples. We also demonstrate that SMA combined with SSE goes beyond spin-wave theory with numerical results.

## I. INTRODUCTION

Strongly correlated systems emerge with many novel phenomena and thus attract much attention. Usually, exotic quantum states with peculiar behaviors do not thoroughly exhibit themselves in small systems due to finite-size effects. The exponentially increasing degree of freedom of the Hilbert space hinders further understanding of quantum many-body systems. This stimulates people to derive new approaches to more extensive system sizes. Quantum Monte Carlo (QMC) is a powerful numerical tool for dealing with complex systems, especially with a high degree of freedom [1, 2].

Generally, there are two main branches of QMC methods. The first branch uses stochastic processes to simulate the finite temperature partition function of quantum many-body systems. This branch includes algorithms like Stochastic Series Expansion (SSE) [2–8] and path integral [9–12]. The other one performs the ground state wave function at zero temperature, such as diffusion Monte Carlo [13–17] and Green’s function Monte Carlo [18–21].

Although knowledge of the ground state is always what people seek in the first place, excited states and energy spectrum, which carry information on the energy gap and dynamical exponent z, also play a crucial role in our understanding of the system. Experiments like neutron scattering have been performed to explore the excitations in antiferromagnetic materials [22, 23]. Obtaining the excitation information of many-body systems is one of the most challenging tasks in QMC simulations. Some numerical analytical continuation (NAC) methods like maximum entropy method and Stochastic Analytic Continuation (SAC) [24–30] have been developed during the past decades, aiming at solving this problem [31–37]. Unfortunately, massive computing resources are required to get excitation spectrum. Moreover, these algorithms need to fit each spectrum case by case, with modifications that may lead to ambiguous results, not to mention the fitting process itself could be time-consuming. As a result, the computation complexity of numerical, analytical continuation methods limits these algorithms' power to reach larger lattice sizes, explore vast choices of parameters, or test various candidate materials. Is introducing a faster approach with less cost to extract energy-momentum dispersion from quantum Monte Carlo simulations feasible? In this paper, we show a possible access to large-scale calculation of the energy dispersion: the single mode approximation (SMA) that has been widely used in the field of Bose-condensed systems, quantum information, quantum spin systems and condensed matter theory [38–45].

As far as we know, SMA has yet to be used in the QMC simulations. In this paper, we develop an efficient scheme extending the SMA into QMC algorithms to extract the dispersion information straightforwardly with extremely cheap computational cost and low barrier of technique. This new approach can reach large spin systems with up to  \( 10^{6} \)  spins.

This paper is organized as follows: We begin in Sec. II by introducing the Single-Mode Approximation. In Sec.
 

III, we describe how the SSE algorithm cooperates with SMA. In Sec. IV, we discuss how SMA works with the projector QMC method on a valence-bond (VB) basis. We show the results of several calculations in Sec. V and conclude with a summary in Sec. VI.

## II. SINGLE-MODE APPROXIMATION

Single-mode approximation was first introduced by Richard Feynman in 1954 to investigate excited states in liquid helium. He estimated the lowest collective excitation energy of superfluid  \( {}^{4}He \)  by using the variational principle [38]. This method has been widely applied to various systems including not only liquid helium, but also for cold atom systems, BCS-BEC crossover, phonons in crystals, metals, and quantum spin systems. [39–44, 46–48]. In this paper, we mainly talk about how this method can be applied to spin lattice models.

The key point of SMA is the assumption that by acting some momentum-dependent operators on the ground state, a single excitation can be created. An appropriate trial operator produces a well-estimated upper bound of the low-energy excitation [38] in the long wave-length limit.

Naturally, in our lattice spin system, we choose the  \( S^{z} \)  operator in momentum space as the form of excitation:

 \[ \hat{S}^{z}(\boldsymbol{q})=\frac{1}{\sqrt{N}}\sum_{i}e^{-i\boldsymbol{q}\cdot\boldsymbol{r}_{i}}\hat{S}_{i}^{z}, \quad (1) \] 

where q is a given momentum.  \( \hat{S}_{i}^{z} \)  denotes the z component of the spin at site i. The variational wavefunction to describe a lowest excited state is

 \[ |\psi_{\boldsymbol{q}}\rangle=\hat{S}^{z}(\boldsymbol{q})|\mathrm{G S}\rangle. \quad (2) \] 

If this state is orthogonal to the ground state, the corresponding norm of this wavefunction is

 \[ S_{z}^{2}(\boldsymbol{q})=\langle\psi_{\boldsymbol{q}}|\psi_{\boldsymbol{q}}\rangle=\langle\mathrm{G S}|\hat{S}^{z\dagger}(\boldsymbol{q})\hat{S}^{z}(\boldsymbol{q})|\mathrm{G S}\rangle. \quad (3) \] 

By using these notations, the single-mode approximation spectrum can be expressed as

 \[ \omega_{\mathrm{S M A}}=\frac{\langle\psi_{\boldsymbol{q}}|(\hat{H}-E_{0})|\psi_{\boldsymbol{q}}\rangle}{\langle\psi_{\boldsymbol{q}}|\psi_{\boldsymbol{q}})} \quad (4) \] 

where  \( \omega_{SMA} \)  is an upper bound of energy gap at wavevector q and  \( E_{0} \)  is the exact ground state energy [38]. Using Eq.(2) and (3), we can rewrite Eq.(4) as

 \[ \begin{align*}\omega_{\mathrm{SMA}}&=\frac{1}{S_{z}^{2}(\boldsymbol{q})}\langle\psi_{\boldsymbol{q}}|(\hat{H}-E_{0})|\psi_{\boldsymbol{q}}\rangle\\&=\frac{1}{S_{z}^{2}(\boldsymbol{q})}\langle\mathrm{GS}|\hat{S}^{z}(-\boldsymbol{q})[\hat{H},\hat{S}^{z}(\boldsymbol{q})]|\mathrm{GS}\rangle\\&=\frac{1}{S_{z}^{2}(\boldsymbol{q})}\langle\mathrm{GS}|[\hat{S}^{z}(\boldsymbol{q}),\hat{H}]\hat{S}^{z}(-\boldsymbol{q})|\mathrm{GS}\rangle\\&=\frac{1}{2}\frac{\langle\mathrm{GS}|[\hat{S}^{z}(-\boldsymbol{q}),[\hat{H},\hat{S}^{z}(\boldsymbol{q})]]|\mathrm{GS}\rangle}{S_{z}^{2}(\boldsymbol{q})},\end{align*} \quad (5) \] 

which completes our derivation of excitation spectrum of SMA.

In cases when state  \( |\Psi_{q}\rangle \)  is not orthogonal to the ground state  \( |GS\rangle \) , namely

 \[ \langle\mathrm{G S}|\psi_{\boldsymbol{q}}\rangle=\langle\mathrm{G S}|\hat{S}^{z}(\boldsymbol{q})|\mathrm{G S}\rangle=c_{1}\neq0, \quad (6) \] 

we can express our variational wavefunction as

 \[ |\psi_{\boldsymbol{q}}\rangle=c_{1}|\mathrm{G S}\rangle+c_{2}|\mathrm{E S}\rangle \quad (7) \] 

where  \( |ES\rangle \)  represents an excited state orthogonal to the ground state

 \[ \langle\mathrm{G S}|\mathrm{E S}\rangle=0. \quad (8) \] 

To get the correct estimate of dispersion in such cases, one has to modify the variational equation (4) to

 \[ \omega_{\mathrm{S M A}}=\frac{\langle\mathrm{E S}|(\hat{H}-E_{0})|\mathrm{E S}\rangle}{\langle\mathrm{E S}|\mathrm{E S}\rangle}. \quad (9) \] 

After making use of the relation

 \[ c_{2}^{*}c_{2}\langle\mathrm{E S}|(\hat{H}-E_{0})|\mathrm{E S}\rangle=\langle\psi_{\boldsymbol{q}}|(\hat{H}-E_{0})|\psi_{\boldsymbol{q}}\rangle \quad (10) \] 

and the Gram-Schmidt process

 \[ c_{2}|\mathrm{E S}\rangle=|\psi_{\boldsymbol{q}}\rangle-\frac{\langle\mathrm{G S}|\psi_{\boldsymbol{q}}\}}{\langle\mathrm{G S}|\mathrm{G S}\rangle}|\mathrm{G S}\mathrm{\rangle}, \quad (11) \] 

we express the final Single-Mode Approximation expression as

 \[ \begin{align*}\omega_{\mathrm{SMA}}=&\frac{\langle\mathrm{GS}|(\hat{H}-E_{0})|\mathrm{GS}\rangle}{(\langle\psi_{\boldsymbol{q}}|-\langle\mathrm{GS}|\frac{\langle\mathrm{GS}|\psi_{\boldsymbol{q}}\rangle}{\langle\mathrm{GS}|\mathrm{GS}\rangle})|(\psi_{\boldsymbol{q}})-\frac{\langle\mathrm{GS}|\psi_{\boldsymbol{q}}\rangle}{\langle\mathrm{GS}|\mathrm{GS}\rangle}|\mathrm{GS}\mathrm{\rangle)}\\=&\frac{1}{2}\frac{\langle\mathrm{GS}|[\hat{S}^{z}(-\boldsymbol{q}),[\hat{H},\hat{S}^{z}(\boldsymbol{q})]]|\mathrm{GS}\rangle}{S_{z}^{2}(\boldsymbol{q})-\frac{|\langle\mathrm{GS}|\psi_{\boldsymbol{q}}\rangle|^{2}}{\langle\mathrm{GS}|\mathrm{GS}\rangle}}.\end{align*} \quad (12) \] 

In summary, the spirit of SMA is to construct a low-energy-excitation state, e.g., a spin-wave perturbated wavefunction as Eq.(2), which is orthogonal to the ground state to estimate the upper bound of the first excited gap, thus  \( \omega_{SMA} \geq \omega \) . The “=” holds only if the excited mode is single, then we have  \( \omega_{SMA} = \omega \) .

## III. SMA COMBINED WITH SSE

In this section we introduce how to perform SMA calculations with SSE and explain how the measurements are performed.

The stochastic series expansion [2–5, 8] approach constitutes a method to simulate sign-problem-free spin systems using quantum Monte Carlo techniques. Here, we briefly summarize the important part of this algorithm. Its starting point is the partition function of the system:

 \[ Z=\mathrm{T r}(e^{-\beta\hat{H}}). \quad (13) \]
 
![](./images/942483432699593354_1.jpg)

Figure 1. Sketch of SMA excitation spectrum measurement of a six-spin system with Stochastic Series Expansion. The imaginary time dimension is depicted horizontally. Filled and open circles represent  \( \uparrow \)  and  \( \downarrow \)  spins, respectively. Black bonds, which change the spin configuration, denote off-diagonal operators. White bonds that keep the spins unchanged denote diagonal operators. The identity operator is omitted in this figure. The bond highlighted by the red box represents the randomly chosen non-identity operator. “Configuration 1” and “Configuration 2” denote the spin configurations in light orange and blue boxes, respectively. Here, “Configuration 1” is  \( |\uparrow\downarrow\uparrow\downarrow\rangle \)  and “Configuration 2” is  \( |\uparrow\downarrow\downarrow\uparrow\uparrow\rangle \) .

Its Taylor expansion replaces the exponential operator in the partition function, and the trace is rewritten as a summation over a complete basis of the system,

 \[ Z=\sum_{\alpha}\sum_{n=0}^{\infty}\frac{\beta^{n}}{n!}\langle\alpha|(-\hat{H})^{n}|\alpha\rangle \quad (14) \] 

The Hamiltonian is written as the sum of several terms

 \[ \hat{H}=\sum_{i}\hat{H}_{i} \quad (15) \] 

where i is a label for enumerating different terms. The Taylor series is truncated at M. M should be sufficiently large so that the truncation error is small enough and negligible. After all these steps, the partition function is

 \[ Z=\sum_{\alpha}\sum_{\{H_{\alpha}\}}\frac{\beta^{n}(M-n)!}{M!}\langle\alpha|\prod_{i}\hat{H}_{\alpha_{i}}|\alpha\rangle \quad (16) \] 

All possible operator strings with lengths between 0 and M are summed over.  \( \alpha \)  and  \( H_{\alpha} \)  are sampled during a Monte Carlo procedure according to each term's weight.

Since the SSE is usually performed in the spin  \( S_{Z} \)  basis, the equal-time correlation function of the spin z component in Eq.(3), i.e., the denominator part of Eq.(5), can be directly measured. The double commutator, i.e., the numerator part of Eq.(5), can be measured as follows. It contains four terms,

 \[ \frac{1}{2}\langle\hat{S}_{q}^{z\dagger}\hat{H}\hat{S}_{q}^{z}-\hat{S}_{q}^{zz\dagger}\hat{S}_{q}^{z}\hat{H}-\hat{H}\hat{S}_{q}z\hat{S}_{q}^{z\dagger}+\hat{S}_{q}^{z}\hat{H}\hat{S}_{q}^{zz\dagger}\rangle. \quad (17) \] 

We now briefly describe how to measure these quantities from SMA. After the system has reached equilibrium (ground state in this case), randomly choose a non-identity operator from imaginary time. For convenience, we assume the imaginary time dimension is horizontal, as shown in Fig.1. “Configuration 1/2” (notated as “C1/C2”) denotes the state (or spin configuration) on the left/right side of the chosen operator, respectively. Notice that  \( \hat{S}_{q}^{z} \)  is diagonal (although not Hermitian in most cases) in the  \( S_{z} \)  basis, so these  \( \hat{S}_{q}^{z} \)  and  \( \hat{S}_{\uparrow}^{z\dagger} \)  operators applied on “C1” or “C2” result in complex numbers  \( S_{q}^{z*}(C1) \)  and  \( S_{q}^{\uparrow}(C2) \) :

 \[ \begin{align*}\langle\hat{S}_{q}^{z\dagger}\hat{H}\hat{S}_{q}^{z}\rangle&=\langle S_{q}^{z*}(C1)S_{q}^{z}(C2)\hat{H}\rangle\\&=\langle S_{q}^{z*}(C1)S_{q}^{z}(C2)\frac{\hat{n}}{\beta}\rangle\end{align*} \quad (18) \] 

Notice that we use a “hat” notation to distinguish quantum operators from numbers. In the second line,  \( \hat{H} \)  is replaced by  \( \hat{n}/\beta \) , which is the energy estimator in the SSE algorithm [2, 4]. Making use of the relation Eq.(18), the double commutator estimator can be expressed as

 \[ \begin{align*}f(\boldsymbol{q})=\frac{1}{2}\langle(S_{q}^{z*}(\mathrm{C}1)S_{q}^{z}(\mathrm{C}2)-S_{q}^{z*}(\mathrm{C}1)S_{q}^{z}(\mathrm{C}1)\\-S_{q}^{z}(\mathbb{C}2)S_{q}^{z*}(\mathrm{C}2)+S_{q}^{z}(\mathrm{C}1)S_{q}^{z*}(\mathrm{C}2))\times\frac{\hat{n}}{\beta}\rangle,\end{align*} \quad (19) \] 

which is the final expression of the SMA spectrum. This expression is independent of forms of Hamiltonians, enabling us to use SMA in systems with complicated Hamiltonians.

## IV. SMA COMBINED WITH PROJECTOR QMC

In cases where the spin system only involves Heisenberg interaction that preserve SU(2) spin symmetry, we can combine SMA with projector QMC. Resulted method can be easily parallelized, making it faster and more efficient. The Projector QMC method was initially introduced by Sandvik [49, 50] to access ground states of quantum spin systems efficiently. This algorithm is formulated in a combined space of spin  \( S_{z} \)  and valence-bond bases. Since one can directly obtain information
 
![](./images/942483432699593354_2.jpg)

Figure 2. Illustration of a valence-bond transposition graph on a  \( 4 \times 4 \)  square lattice. This valence bond basis is used in projector QMC approach. Solid circles represent sites on sublattice A, and open circles represent sites on sublattices B. Red and blue bond configuration represent the bra  \( \langle\psi_{l}| \)  and the ket  \( |\psi_{R}\rangle \)  respectively. This figure is a transposition graph of the inner product  \( \langle\psi_{L}|\psi_{R}\rangle \) . Spins on site i and j belong to the same loop, so  \( \langle\psi_{L}|\hat{\mathbf{S}}_{i} \cdot \hat{\mathbf{S}}_{j}|\psi_{R}\rangle/\langle\psi_{L}|\psi_{R}\rvert = -3/4 \) . Spins on-site i and k are not correlated since they are in different loops.

on valence bonds, it is naturally suited for studying spin rotationally-invariant Hamiltonians, such as the Heisenberg model and its extension versions with long-range interactions. The properties of valence-bond basis and projector QMC methods have been demonstrated in detail in the literature [49–51].

In this section, we describe our algorithm with the Heisenberg model

 \[ \hat{H}=\sum_{i,j}J_{i j}\hat{\pmb{S}}_{i}\cdot\hat{\pmb{S}}_{j}. \quad (20) \] 

Based on the definition of SMA spectrum, we define

 \[ f(\boldsymbol{q})=\frac{1}{2}\langle\mathbf{G S}|[\hat{\boldsymbol{S}}(-\boldsymbol{q}),[\hat{H},\hat{\boldsymbol{S}}(\boldsymbol{q})]]|\mathbf{G S}\rangle, \quad (21) \] 

where  \( \boldsymbol{S}(q) \)  denotes the Fourier transform of spin operator

 \[ \hat{\pmb{S}}(\pmb{q})=\frac{1}{\sqrt{N}}\sum_{i}e^{-i\pmb{q}\cdot\pmb{r}_{i}}\hat{\pmb{S}}_{i}. \quad (22) \] 

After we expanding Eq.(21) with Eq.(22) and Hamiltonian Eq.(20),  \( f(\mathbf{q}) \)  is written as

 \[ \begin{align*}f(\boldsymbol{q})=\frac{1}{2N}\sum_{i,j}J_{ij}\sum_{l,l^{\prime}}e^{-i\boldsymbol{q}\cdot(\boldsymbol{r}_{l}-\boldsymbol{r}_{l^{\prime}})}\\ \langle\mathbf{GS}|[\hat{\boldsymbol{S}}_{l^{\prime}},[\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j},\hat{\boldsymbol{S}}_{l}]]|\mathbf{GS}\rangle.\end{align*} \quad (23) \] 

We note that all multiplications in the commutation relation are dot products of vectors. Only terms of which both subscripts l and  \( l' \)  take values i or j are non-zero since operators on different sites commute with each other. Commutation relations [52]

 \[ [\hat{\pmb{S}}_{i},[\hat{\pmb{S}}_{\dot{\imath}}\cdot\hat{\pmb{S}}_{j},\hat{\pmb{S}}_{i}]]=2\hat{\pmb{S}}_{\dot{\imath}}\cdot\hat{\pmb{S}}_{j}, \quad (24) \] 

 \[ [\hat{\pmb{S}}_{i},[\hat{\pmb{S}}_{\dot{\imath}}\cdot\hat{\pmb{S}}_{j},\hat{\pmb{S}}_{J}]]=-2\hat{\pmb{S}}_{\dot{\imath}}\cdot\hat{\pmb{S}}_{j} \quad (25) \] 

can be obtained after some simple SU(2) algebra calculations. Taking all of these relations into account, we finally get

 \[ f(\boldsymbol{q})=-\frac{4}{N}\sum_{i,j}J_{i j}\sin^{2}(\frac{1}{2}\boldsymbol{q}\cdot(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}))\langle\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j}\rangle_{\mathrm{G S}}. \quad (26) \] 

Here we have replaced  \( \langle GS|\hat{S}_{i}\cdot\hat{S}_{j}|GS\rangle \)  by its abbreviation  \( \langle\hat{S}_{i}\cdot\hat{S}_{j}\rangle_{GS} \) . Spin-spin correlation in the ground state can be easily estimated in the VB basis [51]:

 \[ \langle\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j}\rangle_{\mathrm{G S}}=\frac{3}{4}\epsilon_{i j}\delta^{i j}. \quad (27) \] 

Here  \( \epsilon_{ij} \)  is -1 if site i and j are on the same sub-lattice of underlying bipartite lattice, and is one otherwise.  \( \delta^{ij} \)  equals one if site i and j belong to the same loop formed in the transposition graph. If they belong to different loops, then  \( \delta^{ij} \)  takes the value of 0. See Fig.2 as an example.

To obtain the SMA spectrum of the Heisenberg model, only spin-spin correlations in the ground state are necessary. Projector QMC and VB basis offer quick and convenient access to these correlation functions. Non-trivial parallel programming can be applied to this algorithm, remarkably enhancing power and efficiency. These advantages enable us to obtain a spectrum of systems with  \( 10^{4} \) , even  \( 10^{5} \)  spins.

Although the spectrum of some simple Hamiltonians, like the Heisenberg model, can be simulated and obtained easily, the method discussed in this section could be more suitable for systems with complicated Hamiltonians. Trying to simplify the double commutator may eventually obtain observables that are hard to estimate in practice. For example, Q term interaction  \( (\hat{\mathbf{S}}_{i} \cdot \hat{\mathbf{S}}_{j})(\hat{\mathbf{S}}_{k} \cdot \hat{\mathbf{S}}_{l}) \)  in J-Q model [53–55] produce terms including

 \[ [\hat{S}_{i}^{z},[(\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j})(\hat{\boldsymbol{S}}_{k}\cdot\hat{\boldsymbol{S}}_{l}),\hat{S}_{k}^{z}]]=-\frac{1}{3}(\hat{\boldsymbol{S}}_{i}\times\hat{\boldsymbol{S}}_{j})\cdot(\hat{\boldsymbol{S}}_{k}\times\hat{\boldsymbol{S}}_{l}). \quad (28) \] 

Cross-product terms can be estimated using QMC. However, the procedure would be cumbersome since cross-product terms contain several off-diagonal operators. Thus, projector QMC with SMA does not fit when J-Q model is of interest.

We conclude that the principle is, if the double commutator can be simplified into an easily-calculated estimator in valence-bond basis or  \( S_{z} \)  basis, projector QMC with SMA is able to solve this problem very efficiently, since projector QMC can be performed with non-trivial programming. If ideal simplification cannot be achieved,
 
![](./images/942483432699593354_3.jpg)

Figure 3. a) SMA spectrum of 2D AFM Heisenberg model on a square lattice of system size L = 512. Periodic boundary condition is applied. This spectrum is obtained from projector QMC combined with SMA. Two gapless excitation modes exist at M and  \( \Gamma \)  points, respectively. b) Energy excitation gap at M point of different system sizes. With the increase in system size, the gap at M converges to zero. Errors of data are smaller than the symbol sizes.

then SSE with SMA should be applied, since SSE + SMA is more general.

The following section will show several examples calculated using the methods mentioned above.

## V. RESULTS

## A. 2D AFM Heisenberg Model

The first case is the two-dimensional antiferromagnetic (AFM) Heisenberg model with only nearest neighbor interactions on a square lattice

 \[ \hat{H}=J\sum_{\langle i,j\rangle}\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j} \quad (29) \] 

where  \( \langle i,j\rangle \)  denotes nearest neighbor sites, and coupling J > 0.

This Hamiltonian is simple, so we calculate using projector QMC with non-trivial parallel programming. In the simulation, we set the imaginary time length  \( m = 0.8L^{3} \) , length of measurement 100,000 times  \( \times \)  40 bins. Systems with  \( 512 \times 512 \)  spins are simulated, and the SMA spectrum obtained is shown in Fig.3 (a). Two gapless modes exist, one at M point of momentum space and the other at  \( \Gamma \)  point. Both gapless modes have linear dispersion in the low-energy part. This result is consistent with the spectrum given by spin-wave theory [22, 56].

It is worth noting here that indicated by the original SMA expression Eq. \( (5) \) , either the double commutator vanishes or the equal-time correlation function diverges as a function of system size would induce the absence of an energy gap.

At  \( \Gamma \)  point, the operator acted on the system commutes with the total Hamiltonian,

 \[ [\hat{S}_{z}(\boldsymbol{q}=0),J\sum_{\langle i,j\rangle}\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j}]=0. \quad (30) \] 

As a result, the numerator in Eq. \( (5) \)  is always zero, regardless of the system size.

At the M point, the equal-time correlation function on the denominator increases with system size and finally diverges in the thermal-dynamic limit. This fact indicates that there must be a gapless mode at M. As shown in Fig.3 (b), the energy gap becomes smaller and converges to zero with the increase of lattice size.

We mention here that the key point of numerical analytic continuation is fitting the spectrum according to the imaginary time correlation data. However, to get accurate information of low energy part of the dispersion using NAC method, one has to measure correlations of very long imaginary time distances with high precision, and fit the correlation data several times according to the value of the entropy or other standards. In fact, it needs high-technical barrier to write an extra code for the numerical analytic continuation in speciality. That's the motivation why we want to develop a method obtaining the dispersion quickly with low barrier.

The SAC method successfully obtained the spectrum function of 2D square lattice AFM Heisenberg model [29] which is also calculated here. The SAC can perform the continuum spectrum while SMA can only get a single dispersion. But the dispersion catches the main mode with the largest weight in the spectrum. Due to the low cost of SMA method, we can simulate much larger system size. Data of the dispersion of  \( 512 \times 512 \)  two-dimensional AFM model are provided, of which the size is far beyond the SAC method's reach (about  \( 10^{3} \)  spin systems [30]).

## B. 2D long-range FM Heisenberg Model

The next example is the two-dimensional ferromagnetic (FM) Heisenberg model with long-range interactions. The Hamiltonian is

 \[ \hat{H}=\sum_{i,j}J_{i j}\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j} \quad (31) \] 

with  \( J_{ij} < 0 \) . Here, the term “long-range” means that the coupling strength decays as a power law form:

 \[ \hat{H}=\sum_{i,j}\frac{1}{|r_{ij}|^{\alpha}}|\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{j}. \quad (32) \]
 
![](./images/942483432699593354_4.jpg)

![](./images/942483432699593354_5.jpg)

Figure 4. The upper panel is the SMA spectrum obtained by SSE simulation and spin-wave theory spectrum of the 2D ferromagnetic Heisenberg model on a square lattice. Lattice size L = 48. Periodic boundary condition is applied. Only interactions between nearest neighbors are included when power exponent  \( \alpha \)  approaches infinity. The  \( \alpha \rightarrow \infty \)  SMA results fit well with the spin wave theory. Different  \( \alpha \)  leads to different dispersion relation near  \( \Gamma \) . The lower panel is the dispersion relations near the  \( \Gamma \)  point. Power law fitting results are labeled on the panel. The dispersion power exponent decreases with decreasing  \( \alpha \) . Error bars are smaller than the size of the symbol.

The power exponent  \( \alpha \)  controls the effective range of coupling. As  \( \alpha \) , approaches infinity, the model returns to the Heisenberg model with only nearest-neighbor interactions. Strong long-distance couplings come in with small  \( \alpha \) . Spectrums of ferromagnetic Heisenberg models can be well estimated by spin wave theory [56, 58, 59]. According to spin-wave theory, the dispersion of a magnon is

 \[ \omega_{\mathrm{F M}}(\pmb{q})=|J_{0}-J_{\pmb{q}}| \quad (33) \] 

where  \( J_{q} \)  is the Fourier transform of  \( J_{ij} \) 

 \[ J_{\boldsymbol{q}}=\sum_{\boldsymbol{r}}e^{-i\boldsymbol{q}\cdot\boldsymbol{r}}J_{\boldsymbol{r}} \quad (34) \] 

Here, we compare our SSE with SMA results with the dispersion of magnon. We set  \( \beta = L \)  here. Results are exhibited in Fig.4. Fig.4 (a) shows the spectrum of the Heisenberg model with different decay exponent  \( \alpha \) .

![](./images/942483432699593354_6.jpg)

![](./images/942483432699593354_7.jpg)

Figure 5. a) The black line shows the SMA spectrum from SSE simulations of the anti-ferromagnetic Heisenberg chain. The lower and upper bounds of spinon excitation are shown with red and purple lines, respectively. The lower bound of spinon excitation is  \( \omega = \frac{1}{2}\pi|J\sin k| \) , indicated by the red line. The upper bound of spinon excitation is  \( \omega = \pi|J|\sin\frac{1}{2}k \) , which is shown by the purple line [57]. The blue line indicates the result of the spin-wave theory (which is wrong). The length of the chain is L = 2048. b) Energy gap near momentum  \( \pi \)  of different chain length. Maximum chain length L = 2048 is reached. In both figures, error bars are smaller than the symbols.

When  \( \alpha \)  approaches infinity, only nearest-neighbor interactions are considered. In this case, our result is consistent with the spectrum given by spin-wave theory. The corresponding dispersion near the  \( \Gamma \)  point is quadratic. As is shown in Fig.4, as  \( \alpha \)  decreases to 2.5, this gapless mode still retains. However, the dispersion relations [56]

 \[ \omega\sim k^{s} \quad (35) \] 

varies with  \( \alpha \) . In the nearest neighbor version, dispersion power exponent s = 2. As  \( \alpha \)  decreases, s also decreases. This mode has a linear dispersion when  \( \alpha = 3.0 \) . Corresponding s has been tagged on the lower panel of Fig.4. All results are well compatible with magnon dispersion given by spin-wave theory for long-range interactions [56, 59].
 

## C. AFM Heisenberg Chain

If the SMA algorithm always gives the same spectrum as spin-wave theory, undoubtedly, it makes this method less appealing. Fortunately, this is not the case.

The last case shown in this paper is an anti-ferromagnetic Heisenberg chain with periodic boundary conditions. The Hamiltonian is

 \[ \hat{H}=J\sum_{i=1}^{N}\hat{\boldsymbol{S}}_{i}\cdot\hat{\boldsymbol{S}}_{i+1} \quad (36) \] 

where  \( \hat{S}_{N+1} = \hat{S}_{1} \)  and J > 0.

As is known, spin wave theory breaks down here and gives a wrong dispersion velocity [57]

 \[ v_{\mathrm{S W}}=|J| \quad (37) \] 

which is shown in Fig.5 with the blue line. This velocity is smaller than the correct result obtained from spinon theory [57]

 \[ v_{\mathrm{s p i n o n}}=\frac{\pi}{2}|J|. \quad (38) \] 

In the simulation, we fix the temperature  \( \beta = 100 \) . As shown in Fig.5, we can obtain the correct velocity near momentum 0 and  \( 2\pi \)  from SSE with SMA calculations. In this case, SMA still works while spin-wave theory breaks down, indicating SMA calculation's better feasibility.

At momentum  \( \pi \) , according to spinon excitation, there exists a strongly continuous spectrum [57]. In such cases, SMA’s upper bound energy gap estimation is unreliable. With the increase of the system size, the gap given by SMA becomes smaller (Fig.5 b)). With the chain length increase, this gap converges to zero as the system approaches the thermodynamic limit. However, SMA does not tell the correct velocity of dispersion near momentum  \( \pi \)  because of the continuous spectrum.

## VI. CONCLUSIONS

We introduce an algorithm to perform single-mode approximation calculations via quantum Monte Carlo. In

[1] J. Gubernatis, N. Kawashima, and P. Werner, Quantum Monte Carlo Methods (Cambridge University Press, 2016).

[2] A. W. Sandvik, Stochastic series expansion methods (2019), arXiv:1909.10591 [cond-mat.str-el].

[3] A. W. Sandvik and J. Kurkijärvi, Quantum monte carlo simulation method for spin systems, Phys. Rev. B 43, 5950 (1991).

particular, two versions of the combination of single-mode approximation with quantum Monte Carlo are employed. Projector QMC with non-trivial parallel programming can be applied when directly simplifying the double commutator. In this case, large systems with  \( 10^{6} \)  spins are accessible. For a system with a complicated Hamiltonian, we develop another general method with which forms of the Hamiltonians become irrelevant. Both algorithms can perform large-scale simulations outside of the reach of conventional spectrum-estimating algorithms. They may play an important role when large system sizes are crucial in exhibiting exotic excitations, and many systems should be selected according to their excitations. Several cases are calculated as examples. In the two-dimensional Heisenberg model, either ferromagnetic or anti-ferromagnetic, SMA calculations give the correct excitation dispersions consistent with spin-wave theory. In the 1D anti-ferromagnetic chain, SMA goes beyond the spin-wave theory. Although the approximation near continuous spectrum could be more accurate, the correct velocity of dispersion near momentum 0 and  \( 2\pi \)  can be obtained. With the advent of this state-of-the-art algorithm, scanning through parameters and performing statistical works of the spectrum have become possible.

## VII. ACKNOWLEDGEMENTS

This work is supported by the National Key Research and Development Program of China Grant No. 2022YFA1404204, and the National Natural Science Foundation of China Grant No. 12274086. ZY thanks the inspirational discussions with Zi Yang Meng, Amos Chan, and David Huse in another related project and the support from the start-up funding of Westlake University and the open fund of Lanzhou Center for Theoretical Physics (12247101). Y.C.W. acknowledges the support from Zhejiang Provincial Natural Science Foundation of China (Grant No. LZ23A040003), and the support from the High-performance Computing Centre of Zhongfa Aviation Institute of Beihang University. The authors acknowledge the Beijing PARATERA Tech Co., Ltd. for providing HPC resources that have contributed to the research results reported within this paper.

[4] A. W. Sandvik, Stochastic series expansion method with operator-loop update, Phys. Rev. B 59, R14157 (1999).

[5] O. F. Syljuåsen and A. W. Sandvik, Quantum monte carlo with directed loops, Phys. Rev. E 66, 046701 (2002).

[6] Z. Yan, Y. Wu, C. Liu, O. F. Syljuåsen, J. Lou, and Y. Chen, Sweeping cluster algorithm for quantum spin systems with strong geometric restrictions, Phys. Rev. B 99, 165135 (2019).
 

[7] Z. Yan, Global scheme of sweeping cluster algorithm to sample among topological sectors, Phys. Rev. B 105, 184432 (2022).

[8] N. Desai and S. Pujari, Resummation-based quantum monte carlo for quantum paramagnetic phases, Phys. Rev. B 104, L060406 (2021).

[9] N. Prokof'ev, B. Svistunov, and I. Tupitsyn, "worm" algorithm in quantum monte carlo simulations, Phys. Lett. A 238, 253 (1998).

[10] M. Boninsegni, N. V. Prokof'ev, and B. V. Svistunov, Worm algorithm and diagrammatic monte carlo: A new approach to continuous-space path integral monte carlo simulations, Phys. Rev. E 74, 036701 (2006).

[11] M. Boninsegni, N. Prokof'ev, and B. Svistunov, Worm algorithm for continuous-space path integral monte carlo simulations, Phys. Rev. Lett. 96, 070601 (2006).

[12] F. Krzakala, A. Rosso, G. Semerjian, and F. Zamponi, Path-integral representation for quantum spin models: Application to the quantum cavity method and monte carlo simulations, Phys. Rev. B 78, 134428 (2008).

[13] I. Kosztin, B. Faber, and K. Schulten, Introduction to the diffusion Monte Carlo method, American Journal of Physics 64, 633 (1996).

[14] O. F. Syljuåsen, Diffusion monte carlo in continuous time, Journal of low temperature physics 140, 281 (2005).

[15] O. F. Syljuåsen, Random walks near rokhsar–kivelson points, International Journal of Modern Physics B 19, 1973 (2005).

[16] O. F. Syljuåsen, Continuous-time diffusion monte carlo method applied to the quantum dimer model, Phys. Rev. B 71, 020401(R) (2005).

[17] O. F. Syljuåsen, Plaquette phase of the square-lattice quantum dimer model: Quantum monte carlo calculations, Phys. Rev. B 73, 245105 (2006).

[18] N. Trivedi and D. M. Ceperley, Ground-state correlations of quantum antiferromagnets: A green-function monte carlo study, Phys. Rev. B 41, 4552 (1990).

[19] N. Trivedi and D. M. Ceperley, Green-function monte carlo study of quantum antiferromagnets, Phys. Rev. B 40, 2737 (1989).

[20] D. M. Arnow, M. H. Kalos, M. A. Lee, and K. E. Schmidt, Green’s function monte carlo for few fermion problems, The Journal of Chemical Physics 77, 5562 (1982).

[21] M. A. Lee and K. E. Schmidt, Green’s function monte carlo, Computer in Physics 6, 192 (1992).

[22] B. Dalla Piazza, M. Mourigal, N. B. Christensen, G. Nilsen, P. Tregenna-Piggott, T. Perring, M. Enderle, D. F. McMorrow, D. Ivanov, and H. M. Rønnow, Fractional excitations in the square-lattice quantum antiferromagnet, Nature physics 11, 62 (2015).

[23] G. Sala, M. B. Stone, B. K. Rai, A. F. May, P. Laurell, V. O. Garlea, N. P. Butch, M. D. Lumsden, G. Ehlers, G. Pokharel, et al., Van hove singularity in the magnon spectrum of the antiferromagnetic quantum honeycomb lattice, Nature communications 12, 171 (2021).

[24] S. Gull and J. Skilling, Maximum entropy method in image processing, IEE Proceedings F (Communications, Radar and Signal Processing) 131, 646 (1984).

[25] A. W. Sandvik, Stochastic method for analytic continuation of quantum monte carlo data, Phys. Rev. B 57, 10287 (1998).

[26] K. S. D. Beach, Identifying the maximum entropy method as a special limit of stochastic analytic continuation (2004), arXiv:cond-mat/0403055 [cond-mat.str-el].

[27] O. F. Syljuåsen, Using the average spectrum method to extract dynamics from quantum monte carlo simulations, Phys. Rev. B 78, 174429 (2008).

[28] A. W. Sandvik, Constrained sampling method for analytic continuation, Phys. Rev. E 94, 063308 (2016).

[29] H. Shao, Y. Q. Qin, S. Capponi, S. Chesi, Z. Y. Meng, and A. W. Sandvik, Nearly deconfined spinon excitations in the square-lattice spin-1/2 heisenberg antiferromagnet, Physical Review X 7, 041072 (2017).

[30] H. Shao and A. W. Sandvik, Progress on stochastic analytic continuation of quantum monte carlo data, Physics Reports 1003, 1 (2023).

[31] Z. Yan, R. Samajdar, Y.-C. Wang, S. Sachdev, and Z. Y. Meng, Triangular lattice quantum dimer model with variable dimer density, Nature Communications 13, 5799 (2022).

[32] Z. Zhou, C. Liu, Z. Yan, Y. Chen, and X.-F. Zhang, Quantum dynamics of topological strings in a frustrated ising antiferromagnet, npj Quantum Materials 7, 60 (2022).

[33] Z. Yan, Y.-C. Wang, N. Ma, Y. Qi, and Z. Y. Meng, Topological phase transition and single/multi anyon dynamics of z 2 spin liquid, npj Quantum Materials 6, 39 (2021).

[34] Z. Zhou, X.-F. Zhang, et al., Quantum tricriticality of incommensurate phase induced by quantum strings in frustrated ising magnetism, SciPost Physics 14, 037 (2023).

[35] Z. Yan and Z. Y. Meng, Unlocking the general relationship between energy and entanglement spectra via the wormhole effect, Nature Communications 14, 2360 (2023).

[36] C. Zhou, Z. Yan, H.-Q. Wu, K. Sun, O. A. Starykh, and Z. Y. Meng, Amplitude mode in quantum magnets via dimensional crossover, Physical Review Letters 126, 227201 (2021).

[37] Z. Liu, J. Li, R.-Z. Huang, Z. Yan, and D.-X. Yao, Bulk and edge dynamics of a two-dimensional affleck-kennedy-lieb-tasaki model, Physical Review B 105, 014418 (2022).

[38] R. P. Feynman, Atomic theory of the two-fluid model of liquid helium, Physical Review 94, 262 (1954).

[39] A. Griffin, T. Nikuni, and E. Zaremba, Bose-condensed gases at finite temperatures (Cambridge University Press, 2009).

[40] J. P. Toennies and A. F. Vilesov, Superfluid helium droplets: A uniquely cold nanomatrix for molecules and molecular complexes, Angewandte Chemie International Edition 43, 2622 (2004).

[41] J. Haegeman, S. Michalakis, B. Nachtergaele, T. J. Osborne, N. Schuch, and F. Verstraete, Elementary excitations in gapped quantum spin systems, Physical review letters 111, 080401 (2013).

[42] S. Yi, Ö. E. Müstecaplıoğlu, C.-P. Sun, and L. You, Single-mode approximation in a spinor-1 atomic condensate, Physical Review A 66, 011601(R) (2002).

[43] D. E. Bruschi, J. Louko, E. Martín-Martínez, A. Dragan, and I. Fuentes, Unruh effect in quantum information beyond the single-mode approximation, Physical Review A 82, 042332 (2010).

[44] A. M. Läuchli, S. Capponi, and F. F. Assaad, Dynamical dimer correlations at bipartite and non-bipartite rokhsar–kivelson points, Journal of Statistical Mechanics: Theory and Experiment 2008, P01010 (2008).
 

[45] Z. Yan, Z. Y. Meng, D. A. Huse, and A. Chan, Height-conserving quantum dimer models, Physical Review B 106, L041115 (2022).

[46] E. Manousakis, The spin-1/2 heisenberg antiferromagnet on a square lattice and its application to the cuprous oxides, Reviews of Modern Physics 63, 1 (1991).

[47] Q. Chen, J. Stajic, S. Tan, and K. Levin, Bcs–bcc crossover: From high temperature superconductors to ultracold superfluids, Physics Reports 412, 1 (2005).

[48] S. Takeno and M. Goda, A theory of phonon-like excitations in non-crystalline solids and liquids, Progress of Theoretical Physics 47, 790 (1972).

[49] A. W. Sandvik, Ground state projection of quantum spin systems in the valence-bond basis, Phys. Rev. Lett. 95, 207203 (2005).

[50] A. W. Sandvik and H. G. Evertz, Loop updates for variational and projector quantum monte carlo simulations in the valence-bond basis, Phys. Rev. B 82, 024407 (2010).

[51] K. Beach and A. W. Sandvik, Some formal results for the valence bond basis, Nucl. Phys. B 750, 142 (2006).

[52] D. Vörös and K. Penc, Dynamical structure factor of the  \( \mathrm{su}(3) \)  heisenberg chain: Variational monte carlo approach, Phys. Rev. B 104, 184426 (2021).

[53] A. W. Sandvik, Evidence for deconfined quantum criticality in a two-dimensional heisenberg model with four-

spin interactions, Phys. Rev. Lett. 98, 227202 (2007).

[54] A. W. Sandvik, Continuous quantum phase transition between an antiferromagnet and a valence-bond solid in two dimensions: Evidence for logarithmic corrections to scaling, Phys. Rev. Lett. 104, 177201 (2010).

[55] S. Pujari, K. Damle, and F. Alet, Néel-state to valence-bond-solid transition on the honeycomb lattice: Evidence for deconfined criticality, Phys. Rev. Lett. 111, 087203 (2013).

[56] M. Song, J. Zhao, C. Zhou, and Z. Y. Meng, Dynamical properties of quantum many-body systems with long-range interactions, Phys. Rev. Res. 5, 033046 (2023).

[57] M. Takahashi, Thermodynamics of one-dimensional solvable models (Cambridge university press Cambridge, 1999).

[58] N. Defenu, T. Donner, T. Macri, G. Pagano, S. Ruffo, and A. Trombettoni, Long-range interacting quantum systems, Rev. Mod. Phys. 95, 035002 (2023).

[59] O. K. Diessel, S. Diehl, N. Defenu, A. Rosch, and A. Chiocchetta, Generalized higgs mechanism in long-range-interacting quantum systems, Phys. Rev. Res. 5, 033038 (2023).
 
