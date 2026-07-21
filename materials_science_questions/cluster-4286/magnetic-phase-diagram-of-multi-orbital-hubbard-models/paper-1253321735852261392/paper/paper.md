# Magnetotransport and Phase competition in three-dimensional Hubbard-Holstein model at half-filling

Sandip Halder$^{1, \ast}$ and Moshe Schechter$^{1, \dagger}$

$^{1}$ Department of Physics, Ben-Gurion University of the Negev, Beer-Sheva 84105, Israel

We investigate the magnetotransport properties of the one-band Hubbard-Holstein model at half-filling in three dimensions (3D) using exact diagonalization based semi-classical Monte Carlo simulations with phonons treated in the adiabatic limit. The low-temperature electronic correlation $U$ vs electron-phonon coupling $V$ phase diagram reveals two insulating phases-antiferromagnetic (AF-I) and charge-ordered (CO-I)-separated by a first-order transition, with no metallic phase observed at their intersection, indicating robustness of these phases in 3D. For $U \sim bandwidth$, the $V$ vs temperature $T$ phase diagram exhibits multiple phases including AF-I, CO-I, Mott-Hubbard insulator, bipolaronic insulator, and two bipolaronic metallic states. Several first-order transitions occur near $V \sim 3.75$. Above the ordering temperature, the density of states shows universal behavior dominated by electronic contribution, while susceptibility and DOS analyses reveal pseudogap features. Magnetic and transport properties along the phase boundary highlight strong proximity effects between competing phases, suggesting routes for tuning correlated materials and emergent electronic states.

## I. INTRODUCTION

The Hubbard interaction ($U$) and electron-phonon coupling ($g$) are two fundamental and competing interactions, which are found widely in nature$^{1-3}$ and govern the electronic, magnetic, and structural properties of strongly correlated materials$^{4-7}$. The onsite Hubbard $U$ is amenable for electronic localization, local moment formation, Mott insulating behavior, and robust magnetic and orbital orders$^{1,2,8}$. The modulation of $U$ through bandwidth control, dimensional confinement, epitaxial strain, chemical substitutions, interfacial engineering is leveraged in a vast range of technological applications$^{6,8}$, such as Mott transistors$^{9,10}$, oxide-based neuromorphic devices$^{11-13}$, and antiferromagnetic spintronics$^{14,15}$. Here, correlation-driven phase transitions (metal-insulator transitions) make possible low-power electronic switching and solid-state sensor devices$^{16}$. Also strong electronic correlation-driven mechanisms, such as history-dependent resistance and multistability, are exploited to create memristive and neuromorphic elements$^{11,17,18}$, which are important for neuromorphic computing$^{17,19-21}$. On the other hand, electron-phonon coupling ($g$) connects the electronic degrees of freedom with lattice distortions, leading to polaron formation$^{22}$, charge density waves (CDW)$^{23,24}$, structural phase transitions$^{25,26}$, and, at strong coupling, bipolaronic states$^{27-29}$. Materials whose properties are dominated by electron-phonon coupling are technologically relevant for optoelectronic devices$^{30,31}$, thermoelectrics$^{30}$, and ultrafast switching applications$^{32}$. Strong electron-phonon coupling helps improve electromechanical responses, which play a key role in sensors$^{33-35}$, actuators$^{33,34}$, and strain-controlled electronic devices$^{36,37}$.

In a large class of correlated materials, such as high $T_C$ cuprates$^{3,38}$, fullerides$^{39}$, nickelates$^{25,40-42}$, manganites$^{43,44}$, vanadates$^{2}$, and organic salts$^{45}$, the Hubbard $U$ and electron-phonon coupling $g$ coexist and, in some cases, compete, giving rise to emergent phases$^{46}$ that are not observed when the individual interactions $U$ or $g$ act alone. For instance, correlation-assisted charge ordering$^{2,47,48}$, lattice-driven metal-insulator transitions$^{2,49,50}$, and coupled magnetic-structural phases$^{26,51}$, are realized due to the subtle interplay of electronic correlation and electron-phonon coupling. From a technological standpoint, this synergy enables multifunctional materials in which electronic, magnetic, and structural properties can be simultaneously tuned by electric field, strain, or temperature$^{52-55}$. Balanced manipulation of the interplay between U and g stands as an important asset toward adaptive electronics$^{46,56}$, ultrafast switching devices$^{57}$, and quantum and oxide technologies$^{46,56-58}$, where phase competition and tunability are not limitations but key functional advantages. Overall, in addition to the individual roles of $U$ and $g$, their cooperation and antagonistic competition are central to many technologically relevant functionalities.

All these practical features urge for a model Hamiltonian that includes both Hubbard $U$ and electron-phonon coupling $g$, comprehensively delineates their interplay, and sheds light on the understanding of these systems. In this context, the Hubbard-Holstein (HH) model is widely investigated, as it explores the interplay among charge order, antiferromagnetism, and superconductivity$^{59-69}$. Most of the studies have been reported on one-dimensional ($1D$) systems, with well-established phase diagrams that include spin-density waves, bond-ordered waves, CDW, metallic phases, and phase separation behavior$^{70-77}$. Density matrix renormalization group (DMRG) studies and quantum Monte Carlo (QMC) simulations on $1D$ also revealed several intriguing general features$^{78-81}$ at finite phonon frequencies, as well as in the adiabatic ($\omega \to 0$) and anti-adiabatic limits ($\omega \to \infty$)$^{80,82}$. Some of them emphasized the stability of pairing correlations when the system is doped or when the electronic band structure is modified, i.e., in the particle-hole symmetry broken scenario$^{78,79}$. A few other reports

were dedicated to establishing an intermediate metallic state between the Peierls insulator and the Mott insu- lator, where the metallic regime depends on the phonon frequency $^{74,75,80,81}$.

Apart from the $1D$ studies, a myriad of striking phases have also been identified in the two-dimensional Hubbard-Holstein model $^{59,65-67,83-86}$. The phases in- clude, naturally, the AF phase, CO phase, supercon- ducting phases, and other phases such as polaronic, bipolaronic, quasiparticles $^{67}$, and pseudogap $^{87,88}$ phases. Moreover, phase separation was reported upon doping the CDW insulator whereas a uniform superconducting ground state was evidenced in case of doping the su- perconducting phase $^{59}$. A recently developed variational non-Gaussian wave function approach within exact di- agonalization predicts two intervening phases between the spin-ordered and charge-ordered phases $^{89}$. One of them may exhibit superconductivity and the other dis- plays large charge fluctuations and dominant binding en- ergy, whereas both the phases reside within the supercon- ducting regime according to the variational Monte Carlo(VMC) studies $^{59,68}$.

In a nutshell, extensive studies of the Hubbard- Holstein model had been performed using a plethora of methods, such as exact diagonalization (ED) in $1D$ and $2D^{89,90}$, density matrix renormalization group(DMRG) studies in $1D^{75,81}$, different variants of quan- tum Monte Carlo (QMC) simulations [such as exact QMC, contineous-time QMC, determinant QMC] in both $1D$ and $2D^{64,75,80,91,92}$, exact diagonalization based semi- classical Monte Carlo (s-MC) technique in $2D^{88}$, dy- namical mean field theory (DMFT) $^{93,94}$ and some times in conjecture with the numerical renormalization group(NRG) in infinite dimension $^{93}$, Hartree-Fock mean-field theory in $2D^{83}$, and perturbative approaches $^{83,84}$. How- ever, there are no reports in real-space three dimensions till now to the best of our knowledge. This lacking might be a result of the enhanced numerical complexities and computational cost.

Specifically, the familiy of nickelates is important in the context of the interplay between electron-phonon cou- pling and strong electronic correlations, which drive var- ious intriguing phenomena $^{25,41,95-100}$. The $RNiO_3$ ($R$ is a rare-earth lanthanide element) compounds exhibit staggered-type phononic modes, i.e., alternate $NiO_6$ oc- tahedra are expanded and compressed in a rocksalt- type distortion $^{25,40,99}$. This contraction (expansion) of the $NiO_6$ octahedra leads to charge disproportionation into $Ni^{3+\delta}O_6$ ($Ni^{3-\delta}O_6$), stabilizing the insulating state via energy gain $^{99}$. The charge segregation ($\delta$) increases with decreasing lanthanide ionic radius $^{101,102}$, accompa- nied by an enhanced disparity in Ni-O bond lengths between electron-rich and electron-depleted Ni sites $^{99}$. An exact diagonalization based Hartree-Fock calculation has shown that rocksalt-type lattice distortions (con- traction/expansion of O octahedra) are energetically fa- vorable in these nickelates ($RNiO_3$), and that a strong electron-phonon coupling drives these rocksalt-like dis- tortions in nickelates $^{100}$.

Considering the absence of theoretical studies in three dimensions and the experimental relevance of systems where both $U$ and $g$ are important, we investigate the magnetotransport properties of the Hubbard-Holstein model in $3D$ using an exact diagonalization based semi- classical Monte Carlo (s-MC) method. To access large system sizes $(8^3)$, we employ the traveling cluster approx- imation (TCA) $^{103}$ with a TCA cluster size of $4^3$. The phonon variables are treated in the adiabatic limit with two modes: expansion and contraction $^{25,40,66,99}$. The low-temperature $U$-$V$ ($V\sim g^2/K$, scaled in terms of energy unit $t$) phase diagram at half-filling reveals two phases: an antiferromagnetic insulator and a charge- ordered insulator, separated by a first-order transition line. In contrast to previous reports $^{88,104}$, no metallic phase is observed at their intersection. For $U=8$, away from both the perturbative and strong correlation limits, the $V$-$T$ phase diagram exhibits several phases, including antiferromagnetic insulator (AF-I), charge-ordered insu- lator (CO-I), Mott-Hubbard insulator (MH-I), bipola- ronic insulator (BP-I), and two bipolaronic metals (BP- M and BP-M*). The distinction between BP-M and BP- M* is identified from the temperature evolution of the bipolaronic order parameter. The transitions AF-I$\rightarrow$CO- I, MH-I$\rightarrow$BP-I, and BP-M*$\rightarrow$BP-M are all first order and occur near $V\sim3.75$ at different temperatures. Near this transition line, the density of states (DOS) shows univer- sal behavior above the ordering temperature, indicating that high-temperature properties are dominated by elec- tronic contributions. Pseudogap features are also cap- tured in our calculations from susceptibility and DOS analyses. Finally, we examine magnetic and transport properties along the transition line of the $U$-$V$ phase di- agram, where proximity to competing phases and exter- nal factors such as frustration, strain, doping, long-range hopping, and dimensional confinement may lead to tun- able material properties and emergent phases.

The paper is organized as follows: In Sec. **II**, we briefly describe our model Hamiltonian and numerical method in order to study the ground state and finite tempera- ture properties of the system. In Sec. **III**, we outline various physical observables which will be used to calcu- late the magnetic, transport, and electronic properties of the system. The details of the ground-state $U$-$V$ phase diagram at half-filling are delineated in Sec. **IV**. The $V$- $T$ phase diagram for a fixed $U=8$ is illustrated in Sec. **V**. Sec. **VI** is devoted to explaining the universality near the transition line and the physics of pseudogap features. In Sec. **VII**, we describe the magnetotransport proper- ties for small $U$ and $V$ combinations. The features along the transition (boundary) line of the $U$-$V$ phase diagram are represented in Sec. **VIII**. Finally, we summarize our results in Sec. **IX**.

## MODEL HAMILTONIAN AND METHOD

We explore the magnetotransport properties of the one band Hubbard-Holstein model in three dimensions, which is represented as follows

$$
\begin{aligned}
H= & -t \sum_{<i, j>, \sigma}\left(c_{i, \sigma}^{\dagger} c_{j, \sigma}+H . c .\right)+U \sum_{i} n_{i, \uparrow} n_{i, \downarrow} \\
& +g \sum_{i} n_{i} \cdot \mathbf{Q}_{i}^{\prime}+\frac{K}{2} \sum_{i} \mathbf{Q}_{i}^{\prime 2}-\mu \sum_{i} n_{i},
\end{aligned}
$$

where $c_{i, \sigma}^{\dagger}$ and $c_{i, \sigma}$ indicate the electron creation and annihilation operator at site $i$ with spin $\sigma$ $(=\uparrow$ or, $\downarrow)$. $<i, j>$ represents the nearest neighbor sites on a $3 D$ cubic lattice and $t$ is the hopping amplitude among these nearest neighbor sites. The strength of onsite Hubbard repulsive interaction is denoted by $U$. $n_{i}=\sum_{\sigma} n_{i, \sigma}=$ $\sum_{\sigma} c_{i, \sigma}^{\dagger} c_{i, \sigma}$, is the charge density operator at site $i$. The average filling (density) of the system is controlled by the chemical potential $\mu$. Here we concentrate on the case of half-filling where $\mu=0$. $g$ is the coupling strength of phonon $\mathbf{Q}_{i}^{\prime}$ with the electronic density $n_{i}$ at arbitrary lattice site $i$. The stiffness constant of the distortion is denoted by $K$. In our investigation, two possible distortions (expansion and contraction modes) are considered and the phonon modes are treated in the adiabatic limit, which are justified in some experiments $^{25,40,99,101}$ and theoretical $^{83,100}$ investigations.

The pure Holstein and Hubbard models are recovered in the limits $U=0$ and $g=0$, respectively. At half-filling in pure classical Holstein model, the single site energy is (for $t=0$)

$$
E=g Q_{i}^{\prime}+\frac{K}{2} Q_{i}^{\prime 2} .
$$

The energy is minimum with respect to the distortion $Q_{min}'=-\frac{g}{K}=\rho$ and the corresponding polaronic minimum energy (polaronic binding energy) is $E_{pol}=-\frac{g^{2}}{2K}$. Thereafter, we rescale the phonon coordinate $Q'$ by $\rho$ such as $Q=Q'/\rho$ and the phonon energies by $|E_{pol}|$ which leads the phononic part of the Hamiltonian in Eq. (1) in terms of a single dimensionless parameter $V$ (scaled in term of energy unit $t$) to be presented as

$$
\begin{aligned}
H= & -t \sum_{<i, j>, \sigma}\left(c_{i, \sigma}^{\dagger} c_{j, \sigma}+H . c .\right)+U \sum_{i} n_{i, \uparrow} n_{i, \downarrow} \\
& +V \sum_{i} n_{i} \cdot \mathbf{Q}_{i}+\frac{V}{2} \sum_{i} \mathbf{Q}_{i}^{2}-\mu \sum_{i} n_{i} \\
= & H_{p}+H_{i n t} .
\end{aligned}
$$

Here, $H_{p}$ contains all other terms except the Hubbard interaction term. Therefore, $H_{p}$ is bilinear (quadratic) in electronic creation and annihilation operators and holds the phononic terms. $H_{int}$ contains the interacting Hubbard term which is quartic in nature. This quartic interaction term is then decomposed into two different quadratic terms in order to solve the Hamiltonian in the following way $^{105,106}$:

$$
U n_{i, \uparrow} n_{i, \downarrow}=U\left[\frac{1}{4} n_{i}^{2}-\left(\mathbf{S}_{i} \cdot \hat{\Omega}_{i}\right)^{2}\right]
$$

with $\mathbf{S}_{i}$ and $\hat{\Omega}_{i}$ are the spin vector and the arbitrary unit vector at the $i$th site, respectively. The spin vector $\mathbf{S}_{i}$ is defined as $\mathbf{S}_{i}=\frac{\hbar}{2} \sum_{\alpha, \beta} c_{i, \alpha}^{\dagger} \sigma_{\alpha, \beta} c_{i, \beta}$ where $\hbar=1$, and $\sigma$ is the Pauli matrices. In Eq. (4), the applied decoupling is rotationally invariant. Next the partition function of the total Hamiltonian in Eq. (3) is written as $Z=Tr e^{-\beta H}$, where $\beta=\frac{1}{T}$ is the inverse temperature and the Boltzmann constant $k_{B}$ is set to 1. The interval $[0, \beta]$ is split into $M$ number of equally spaced slices of width $\Delta \tau$ $(\beta=M \Delta \tau)$. Following this, for very large $M$ (i.e., in the limit $\Delta \tau \rightarrow 0$ ), we express $e^{-\beta(H_{p}+H_{int})}=(e^{-\Delta \tau H_{p}} e^{-\Delta \tau H_{int}})^{M}$ up to first order in $\Delta \tau$ using Suzuki-Trotter transformation. Thereafter, implementing Hubbard-Stratonovich (H-S) transformation, the interacting part of the partition function $e^{-\Delta \tau U \sum_{i}[\frac{1}{4} n_{i}^{2}-(S_{i} \cdot \hat{\Omega}_{i})^{2}]}$ takes a form which is shown to be proportional to

$$
\begin{aligned}
\sim & \int d \phi_{i}(l) d \Delta_{i}(l) d^{2} \Omega_{i}(l) \\
& \times e^{-\Delta \tau\left[\sum_{i}\left\{\frac{\phi_{i}(l)^{2}}{U}+i \phi_{i}(l) n_{i}+\frac{\Delta_{i}(l)^{2}}{U}-i \Delta_{i}(l) \hat{\Omega}_{i}(l) \cdot \mathbf{S}_{i}\right\}\right],}
\end{aligned}
$$

for a generic time slice ' $l$ '. Here, the H-S auxiliary fields $\phi_{i}(l)$ and $\Delta_{i}(l)$ at arbitrary site i, are coupled with the charge density $n_{i}$ and with the spin vector $\mathbf{S}_{\mathbf{i}}$, respectively. Then by introducing a new vector auxiliary field $\mathbf{m}_{i}^{\prime}(l)=\Delta_{i}(l) \cdot \hat{\Omega}_{i}(l)$, the total partition function $^{88,105,106}$ is written as

$$
\begin{aligned}
Z= & \text { const. } \times T r \prod_{l=M}^{1} \int d \phi_{i}(l) d^{3} \mathbf{m}_{i}^{\prime}(l) d Q_{i} \times \\
& e^{-\Delta \tau\left[H_{p}+\sum_{i}\left\{\frac{\phi_{i}(l)^{2}}{U}+i \phi_{i}(l) n_{i}+\frac{\mathbf{m}_{i}^{\prime}(l)^{2}}{U}-2 \mathbf{m}^{\prime}{ }_{i} \cdot \mathbf{S}_{i}\right\}\right],}
\end{aligned}
$$

where the product follows the time order product, i.e., former time appears at the right ( $l$ runs from $M$ to 1 ).

An effective model Hamiltonian is derived from this partition function. At this step, we neglect the $\tau$ dependence of the classical auxiliary fields and retain the spatial fluctuations of the auxiliary fields which capture the physics of inhomogeneities in real space system. Then, using the saddle point value of the auxiliary field $i \phi_{i}(l)=\frac{U}{2}<n_{i}>$ and redefining $\mathbf{m}_{i}=\frac{U}{2} \mathbf{m}_{i}^{\prime}$, we express the effective Hamiltonian $^{88}$ in the following form

$$
\begin{aligned}
H_{e f f}= & -t \sum_{<i, j>, \sigma}\left(c_{i, \sigma}^{\dagger} c_{j, \sigma}+H . c .\right) \\
& +\frac{U}{2} \sum_{i}\left(<n_{i}>n_{i}-\mathbf{m}_{i} \cdot \sigma_{i}\right)+\frac{U}{4} \sum_{i}\left(\mathbf{m}_{i}{ }^{2}-<n_{i}>^{2}\right) \\
& +V \sum_{i} n_{i} \cdot \mathbf{Q}_{i}+\frac{V}{2} \sum_{i} \mathbf{Q}_{i}^{2}-\mu \sum_{i} n_{i}.
\end{aligned}
\tag{7}
$$

We compute this final Hamiltonian in Eq. (7) using semi-classical Monte Carlo technique via the exact diagonalization of fermions in the fixed background of classical fields $\{\mathbf{m}_{i}\}$ and $\{\mathbf{Q}_{i}\}$, and $\{<n_{i}>\}$ configurations. The classical field configurations $(\mathbf{m}_{i}, \mathbf{Q}_{i})$ are annealed using standard Metropolis algorithm $^{107-109}$ by visiting each lattice site sequentially. We estimate $\{<n_{i}>\}$ self-consistently at every $10^{th}$ step of the MC sweeps, which are used in the next 10 MC steps of the MC update. At each temperature, we have employed 2000 MC sweeps, where the first 1000 MC sweeps are used to thermalize the system and the next 1000 MC sweeps are utilized in calculating the physical observables. We also discard 10 MC sweeps between two consecutive measurements to avoid spurious self-correlation in the data. Traveling cluster approximation (TCA) based Monte Carlo scheme $^{103,105,106,108,110}$ is adopted to access large system sizes.

## III. PHYSICAL OBSERVABLES

For exploring the magnetotransport properties and various ground state phases of the one-band Hubbard-Holstein model in three dimensions, we calculate various physical quantities associated with magnetic, transport, electronic, and charge profiles. We first evaluate the structure factor of the quantum spin correlation as follows

$$
S(\boldsymbol{q})=\frac{1}{N^{2}} \sum_{i, j}\left\langle\boldsymbol{S}_{i}.. \boldsymbol{S}_{j}\right\rangle e^{-i \boldsymbol{q} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right)},
$$

with $\mathbf{S}_{\mathbf{i}}$ being the quantum spin vector at site i, determined from the eigenvalues and eigenvectors obtained through the diagonalization of the effective Hamiltonian in Equation (7). Here, $\mathbf{q}$ is the wave vector, and $N$ is the total number of lattice sites in the system. The thermal and quantum mechanical averages of the observables are represented by the angular brackets. The indices $i$ and $j$ run over all lattice sites.

Then, we determine the charge structure factor [CO(q)] in order to measure the charge order (CO) of the system as follows,

$$
C O(\boldsymbol{q})=\frac{1}{N^{2}} \sum_{i, j}\left\langle\left(n_{i}-<n>\right) \cdot\left(n_{j}-<n>\right)\right\rangle e^{-i \boldsymbol{q} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right)},
$$

where $<n>$ is the average density of the system. We basically estimate the charge structure factor at $\mathbf{q}=(\pi, \pi, \pi)$, i.e., $\mathrm{CO}(\pi, \pi, \pi)$, which measures long-range staggered-type (G-type) charge order.

The average local moment $(M)$, which is a measure of the system averaged magnetization squared, is evaluated using the expression $M=\left\langle\left(n_{\uparrow}-n_{\downarrow}\right)^{2}\right\rangle=\langle n\rangle-2\left\langle n_{\uparrow} n_{\downarrow}\right\rangle$, where $\langle n\rangle=\left\langle n_{\uparrow}+n_{\downarrow}\right\rangle$. Subsequently, the distribution of the local moment is represented by $P(M)$, defined as $P(M)=\sum_{i} \delta\left(M-M_{i}\right)$.

Numerically, we calculate the specific heat $C_{v}(U, T)$ of the system by differentiating the total energy with respect to temperature $\left[C_{v}(U, T)=\frac{d E(U, T)}{d T}\right]$ by implementing the central difference formula. We then examine the temperature evolution of this thermodynamic observable.

We compute the electronic properties of the system by calculating the density of state [DOS($\omega$)] at an arbitrary frequency $\omega$, which is defined as $D O S(\omega)=\frac{1}{N} \sum_{\alpha} \delta(\omega-$ $\left.\epsilon_{\alpha}\right)$. Here, $\epsilon_{\alpha}$ represents the single-particle eigenvalues, and $\alpha$ runs over the total number $(=2 \mathrm{~N})$ of eigenvalues of the system. The delta function is calculated using its Lorentzian representation with a broadening $\sim B W / 2 N$ ( $B W$ is the bare bandwidth) to evaluate the DOS.

To analyze the transport properties, we estimate conductivity of the system in the dc limit using the KuboGreenwood formalism $^{111-113}$ in the following way,

$$
\sigma(\omega)=\frac{A}{N} \sum_{\alpha, \beta}\left(n_{\alpha}-n_{\beta}\right) \frac{\left|f_{\alpha \beta}\right|^{2}}{\epsilon_{\beta}-\epsilon_{\alpha}} \delta\left[\omega-\left(\epsilon_{\beta}-\epsilon_{\alpha}\right)\right]
$$

where $A=\pi e^{2} / \hbar a$ ( $a$ is the lattice parameter). $f_{\alpha \beta}$ represents the matrix elements of the paramagnetic current operator $\hat{j}_{\gamma}=i t \sum_{i, \sigma}\left(c_{i, \sigma}^{\dagger} c_{i+\hat{\gamma}, \sigma}-c_{i+\hat{\gamma}, \sigma}^{\dagger} c_{i, \sigma}\right)$ between the eigenstates $\mid \psi_{\alpha}>$ and $\mid \psi_{\beta}>$ with corresponding eigenenergies $\epsilon_{\alpha}$ and $\epsilon_{\beta}$, respectively. $\gamma$ can be $x$, or $y$, or $z$. Here, $n_{\alpha}=\mathcal{F}\left(\mu-\epsilon_{\alpha}\right)$ is the Fermi function for the single-particle energy level $\epsilon_{\alpha}$. Then, we determine the averaged dc-conductivity by averaging over a small low-frequency interval $(\Delta \omega)$ in the following way

$$
\sigma_{a v}(\Delta \omega)=\frac{1}{\Delta \omega} \int_{0}^{\Delta \omega} \sigma(\omega) d \omega,
$$

where $\Delta \omega$ is chosen to be three to five times larger than the mean finite-size gap (average eigenvalue separation) of the system $^{105,106}$, which is actually the ratio of the bare bandwidth to the total number of eigenvalues.

The carriers localization/delocalization is determined by the effective hopping parameter (a measure of the gain in kinetic energy) $)^{106,114-116}$ as follows:

$$
t_{e f f} \equiv\left(\frac{t^{s y s}}{t}\right)_{\gamma}=\frac{\left\langle\sum_{i, \sigma}\left(c_{i, \sigma}^{\dagger} c_{i+\hat{\gamma}, \sigma}+c_{i, \sigma}^{\dagger} c_{i+\hat{\gamma}, \sigma}\right)\right\rangle_{U, V}}{\left\langle\sum_{i, \sigma}\left(c_{i+\hat{\gamma}, \sigma}^{\dagger} c_{i, \sigma}+c_{i, \sigma}^{\dagger} c_{i+\hat{\gamma}, \sigma}\right)\right\rangle_{0}},
$$

where the angular brackets represent the expectation value in the system.

![](./images/1253321735852261392_1.jpg)

FIG. 1: (a) The ground-state $U$-$V$ phase diagram at electron density $n=1$ (half-filling) is shown at low temperature $T=0.005$. The charge-ordered insulating (CO-I) and antiferromagnetic insulating (AF-I) phases are separated by a phase boundary (see main text for details). For a fixed $V=4$, the temperature dependence of $CO(\pi,\pi,\pi)$ and $S(\pi,\pi,\pi)$ with varying $U$ ($U=0$-$16$) is shown in panels (b) and (c), respectively, with identical legends. The results indicate a transition from the CO phase (at $U=8$) to the AF phase (at $U=9$). The precise transition point is determined to be $U=8.4$ from the order parameters at $T=0.005$, as shown in the inset of (c). The inset reveals a discontinuous transition from the charge-ordered (CO) phase to the spin-ordered (SO) phase, confirming its first-order nature. (d) The variation of $T_{CO}$ and $T_N$ with $U$ is shown for fixed $V=4$. While $T_{CO}$ decreases with increasing $U$ and vanishes abruptly above $U\approx8.4$, $T_N$ emerges in the AF phase, further supporting the first-order CO-AF transition. The corresponding $T_{MIT}$ values for $U<8.5$ (open black symbols) and $U\geq8.5$ (open red symbols) are displayed in the inset. Temperature $T$ is measured in units of $t$. The blue (red) line in AF (CO) phase along the phase boundary in (a) is utilized in Sec. VIII.

Additionally, inverse participation ratio is defined as IPR $=\sum_i(\psi_l^i)^4$, where $\psi_l^i$ is the normalized single-particle wave function associated with the $l$th eigenvalue at site $i^{110}$. Here, $\text{IPR}(\epsilon_F)$ characterizes the localized or extended nature of the wave function at the Fermi level $\epsilon_F$. All the physical parameters, such as $U$, $T$, and $\omega$ are measured in units of $t$.

## IV. EXPLORING U-V PHASE DIAGRAM AT HALF-FILLING IN REAL-SPACE THREE DIMENSIONS

To analyze the interplay between $U$ and $V$ in strongly correlated systems, we investigate the magnetotransport properties of the three-dimensional Hubbard-Holstein model. We first construct the ground-state $U$-$V$ phase diagram at half-filling ($n=1$) at a very low temperature $T=0.005$, using Monte Carlo simulations for an $8^3$ lattice [Fig. 1(a)]. To the best of our knowledge, there has not been any study of the ground-state phase diagram in $3D$ system. For small $V$ and any finite $U$, the system stabilizes in an antiferromagnetic insulating (AF-I) phase, whereas for small $U$ and finite $V$, it exhibits a charge-ordered insulating (CO-I) phase due to gap opening at the Fermi level$^{24}$. In the weak-coupling regime, these ordered phases originate from Fermi-surface instabilities (Slater or Peierls)$^{24,117-120}$. Notably, no metallic phase is observed in our calculations, indicating that the observed AF-I and CO-I phases are more robust in three dimensions than in lower dimensions. The transition between AF-I and CO-I occurs abruptly upon increasing $V$ (for fixed $U$) or $U$ (for fixed $V$), indicating a first-order phase transition. Furthermore, the critical $V$ for the AF-CO transition increases with increasing $U$ (as $J\sim1/U$ decreases), consistent with earlier studies of the Holstein $t$-$J$ model$^{121,122}$. This first-order nature is confirmed by the discontinuous change of the order parameters $S(\pi,\pi,\pi)$ and $CO(\pi,\pi,\pi)$ with $U$ at fixed $V=4$ [inset of Fig. 1(c)], where the system abruptly switches from charge order at $U=8.4$ to spin order at $U=8.5$.

We now present the charge structure factor $[CO(\pi,\pi,\pi)]$ and spin structure factor $[S(\pi,\pi,\pi)]$ in Fig. 1(b) and (c), respectively, for a fixed $V=4$ and varying $U$, that were used to prepare the $U$-$V$ phase diagram in Fig. 1(a). The charge ordering temperature ($T_{CO}$) decreases with increasing $U$ up to $U=8.4$, then drops to zero at $U=8.5$ and above [see Fig. 1(b) and (d)]. For larger V, charge carriers form bipolarons that organize in a staggered pattern, establishing a charge-ordered (CO) phase below $T_{CO}$. The electronic correlation $U$ affects bipolaron formation and their effective interactions$^{65,123,124}$, leading to a decrease in $T_{CO}$ with increasing $U$, as the onsite $U$ weakens charge ordering. For $U\geq8.5$, the system converts to an antiferromagnetic phase, confirmed by the antiferromagnetic structure factor $\text{[S}(\pi,\pi,\pi)\text{]}$ in Fig. 1(c) and $T_N$ in Fig. 1(d). In this AF phase, the Neel temperature $T_N$ increases with decreasing $U$ in the larger $U$ range ($U\geq10$) but begins to decrease near the phase boundary for $U<10$ due to the proximity effect of the charge-ordered phase. Moreover, the metal-insulator transition temperature $T_{MIT}$ [estimated from $\rho$ ($\rho\sim\frac{1}{\sigma}$) vs $T$ plot by the temperature with minimum resistivity in Fig. 2(d)] decreases in both CO and AF regimes as one approaches the transition line, as illustrated in the inset of Fig. 1(d).

For characterization of the typical behavior of $T_{CO}$, $T_N$, and $T_{MIT}$ with $U$ in Fig. 1(d), we evaluate the effective hopping ($t_{eff}$), specific heat ($C_v$), resistivity ($\rho$) (see Fig. 2). The dip in $t_{eff}$ marks the ordering temperature (AF or CO), below which $t_{eff}$ increases due to kinetic energy gain for stabilizing the order. The peak in $C_v$ also corresponds to the ordering temperature. In the CO regime ($U<8.5$), the dip in $t_{eff}$ and the peak in $C_v$ both shift to lower temperatures with increasing $U$, indicating a suppression of $T_{CO}$ (see Fig. 2(a) and

![](./images/1253321735852261392_2.jpg)

FIG. 2: (a) Temperature dependence of $t_{eff}$ for fixed $V=4$ and varying $U=0,2,4,6,8$, and 8.4. In this range ($U<8.5$), the ground state remains in the CO phase. The dip in $t_{eff}$, associated with the charge-ordering temperature, shifts to lower $T$ with increasing $U$. Inset: The peak in $C_v$, corresponding to CO formation, also shifts to lower $T$ as $U$ increases. (b) For $U\geq8.5$ and $V=4$, the peak in $C_v$, associated with the antiferromagnetic transition, initially shifts to higher $T$ with increasing $U$ up to $U=10$, and then decreases. (c) The temperature corresponding to the dip in $t_{eff}$ vs $T$ follows the same trend as in (b), increasing with $U$ up to $U=10$ and decreasing thereafter. Panels (a)-(c) collectively support the behavior of $T_{CO}$ and $T_N$ shown in Fig. 1(d). (d) For $U<8.5$ (CO phase), the metal-insulator transition temperature $T_{MIT}$ decreases with increasing $U$, whereas for $U\geq8.5$ (AF phase) $T_{MIT}$ increases with $U$ (inset), consistent with the inset of Fig. 1(d). Temperature $T$ is measured in units of $t$.

Fig. 1(d)). In the AF regime ($U\geq8.5$), the peak position of $C_v$ exhibits nonmonotonic behavior. It shifts to higher temperature as $U$ increases from 8.5 to 10, then moves to lower temperature for larger $U$ (Fig. 2(b)). The dip in $t_{eff}$(Fig. 2(c)) follows the same trend, corroborating the behavior of $T_N$ in Fig. 1(d). The resistivity $\rho$ (Fig. 2(d)) further shows that the metal-insulator transition temperature ($T_{MIT}$) decreases (increases) with increasing $U$ in the CO (AF) regime, consistent with the inset of Fig. 1(d).

Overall, our obtained $U$-$V$ phase diagram is consistent with the phase diagram at half-filling in $2D^{88}$, except for the metallic phase that arises in $2D$ at low values of $U$ and $V$. In quantum Monte Carlo (QMC) study at half-filling in $1D^{104}$, a metallic phase is observed between the CO and AF phases, and the region of this metallic phase contracts as approaches to the adiabatic limit, ultimately leading to a phase diagram similar to Fig. 1(a).

![](./images/1253321735852261392_3.jpg)

FIG. 3: (a) Antiferromagnetic structure factor $S(\pi,\pi,\pi)$ vs $T$ for fixed $U=8$ and varying $V=0$-$6$. Up to $V=3$, the system exhibits an AF transition with the Neel temperature $T_N$ decreasing as $V$ increases. Inset: $CO(\pi,\pi,\pi)$ vs $T$ shows that for $V=4,5,6$ the system is in the CO phase, with the charge-ordering temperature $T_{CO}$ increasing with $V$. Legends in the main panel and inset are identical. (b) $S(\pi,\pi,\pi)$ vs $T$ for $V=3.7$ and 3.8. Inset: $CO(\pi,\pi,\pi)$ vs $T$ for the same $V$ values. The system remains in the AF phase for $V=3.7$ and in the CO phase for $V=3.8$. Temperature $T$ is measured in units of $t$.

## V. PHASE CHARACTERIZATION ACROSS THE BOUNDARY FOR U = 8

In this section, we examine the effect of $V$ on the MH-I and AF-I states and search for distinct phases from low to high temperature regimes. We explore the magnetic, charge, and transport properties for a fixed $U=8$ (away from perturbative and large $U$ limits) and varying $V$ and present the $V$ - $T$ phase diagram. The system remains AF for $V\leq3$ and transitions to a CO phase for $V\geq4$, depicted in Fig. 3(a). An abrupt AF to CO transition between $V=3.7$ and 3.8, indicating a first-order transition, is observed as illustrated in Fig. 3(b).

In Fig. 4(a) we plot the $V$ - $T$ phase diagram for $U=8$. At the pure Hubbard case, $V=0$, we find a successive metal-insulator (Mott) and antiferromagnetic transitions at temperatures $T_{MIT}\sim0.8$ and $T_N=0.21$, respectively, upon decreasing the temperature$^{105,106}$. In the temperature range $T_N<T\leq T_{MIT}$, the system remains in a MH-I state, or in other words, paramagnetic insulating (PM-I) state. When $V$ is turned on, the ground state at low tempertures remains an AF-I state up to $V=3.7$ and then transitions discontinuously to a CO-I state above this point. The transtion is first-order in nature, consistent with previous studies$^{59}$, although those studies were reported in lower dimensions. The MH-I region between $T_{MIT}$ and $T_N$ decreases with increasing $V$ but survives in a finite region even near the transition line at $V=3.7$. To illustrate the reduction of the MH-I region, we plot $S(\pi,\pi,\pi)$ vs $T$ (left panel) and $\rho$ vs $T$ (right panel) at fixed $U=8$ for $V=0,2,3$ in Fig. 4(b). The Neel temperature $T_N$ decreases minutely with increasing $V$, whereas $T_{MIT}$ decreases significantly.

![](./images/1253321735852261392_4.jpg)

FIG. 4: (a) $V$-$T$ phase diagram for fixed $U=8$. At low temperatures, the system undergoes a first-order transition from the AF-I to CO-I phase near $V\approx3.7$. Additional phases such as the Mott-Hubbard insulator (MH-I), bipolaronic insulator (BP-I), and two bipolaronic metallic phases (BP-M and BP-M*) are also observed at high temperatures (see text for details). (b) $S(\pi,\pi,\pi)$ vs $T$ (left) and resistivity $\rho$ vs $T$ (right) for $V=0,2$, and 3 at $U=8$. The Neel temperature $T_N$ decreases slightly with increasing $V$, while the metal-insulator transition temperature $T_{MIT}$ decreases more significantly. Near the phase boundary, $T_{MIT}$ remains larger than $T_N$. (c) Temperature dependence of the local moment $M$ for $V=0,2$, and 3. At high temperatures, $M$ decreases with $V$. (d) Temperature evolution of $CO(\pi,\pi,\pi)$ (left) and resistivity $\rho$ (right). Both the charge-ordering temperature $T_{CO}$ and $T_{MIT}$ decrease as $V$ is reduced from 6 to 4. Near the phase boundary, $T_{MIT}>T_N$, indicating the persistence of the BP-I regime. Temperature $T$ is measured in units of $t$.

Eventually, $T_{MIT}$ remains higher than $T_N$ even near the transition line, indicating the presence of the MH-I region between $T_{MIT}$ and $T_N$. In the pure Hubbard limit ($V=0$), large onsite local moment formation at high temperature ($T\sim1$; see Fig. 4(c)) drives the metal-insulator transition$^{125,126}$. But in Hubbard-Holstein case ($V\neq0$), the electron-phonon coupling ($V$) hinders onsite local moment formation at high temperature. As a result, larger local moments develop only at low temperatures compared to the pure Hubbard case (Fig. 4(c)), leading to a significant decrease in $T_{MIT}$ with increasing $V$. For $V>3.7$, bipolarons form at high temperature and order below $T_{CO}$ (Fig. 4(a)). Both $T_{CO}$ and $T_{MIT}$ increase with $V$ (compare Fig. 4(a) and (d)). The intermediate BP-I region between $T_{MIT}$ and $T_{CO}$ narrows as $V$ decreases but remains finite near the transition line $V\sim3.8$. Notably, just above $T_N$ and $T_{CO}$, the system exhibits a first-order transition between the Mott-Hubbard insulator and the bipolaronic insulator, consistent with earlier DMFT+NRG studies$^{127}$ at strong coupling and zero temperature.

The system, which at low temperatures is in either the AF or CO phases, evolves into bipolaronic metallic phases (BP-M* or BP-M) at higher temperatures. To characterize the BP-M and BP-M* phases, we compute the bipolaronic order parameter $BPO=|<n-1>|=\frac{1}{N}\sum_i|n_i-1|^{127}$, where $N$ is the number of lattice sites. This quantity measures the average charge imbalance relative to half-filling $(<n>=1)$. In the BP-M* phase ($V\leq3.7$), $|<n-1>|$ decreases as the temperature is lowered from $T\sim1$ to $T_{MIT}$ (Fig. 5(a)). In contrast, in the BP-M phase, it increases upon cooling over the same temperature range (Fig. 5(b)). Thus, the bipolaronic order parameter distinguishes BP-M* from BP-M, although both phases are metallic. In the CO regime ($V>3.7$), the system undergoes successive transitions from CO-I to BP-I to BP-M with increasing temperature (Fig. 4(a)). Similarly, in the AF regime ($V\leq3.7$), it transitions from AF-I to MH-I to the distinct bipolaronic metallic phase (BP-M*). Here, the transition between BP-M* and BP-M is first-order, occurring abruptly as $V$ changes from 3.7 to 3.8.

![](./images/1253321735852261392_5.jpg)

FIG. 5: (a) Temperature dependence of the bipolaronic order parameter $BPO=|<n-1>|$ for fixed $U=8$ and varying $V\leq3.7$ (up to the phase boundary in Fig. 4(a)). In this range, the ground state is antiferromagnetic. BPO increases with decreasing $T$, reaches a maximum near $T\approx1$, and decreases at lower temperatures. Its high-temperature magnitude increases with $V$, while in the pure Hubbard limit ($V=0$) BPO vanishes at all temperatures. (b) For $V>3.7$, where the ground state is charge ordered, BPO increases with decreasing $T$ and saturates at low temperature. The low-temperature magnitude of BPO increases monotonically with $V$. Open circles in (a) and (b) indicate the temperatures where the system shows metal-insulator transition for the corresponding $V$.

## VI. UNIVERSALITY AND PSEUDOGAP FEATURES NEAR THE TRANSITION LINE

In the $V$-$T$ phase diagram shown in Fig. 4(a), several phases emerge at different temperature and $V$ scales. To understand the origin of these transitions, we focus on the region near the phase boundary for $U=8$ and $V=3.6$, 3.7, and 3.8. As discussed earlier, the ground state at low temperature is antiferromagnetic (AF) for $V=3.6$ and

![](./images/1253321735852261392_6.jpg)

FIG. 6: Density of states (DOS) for fixed $U=8$ and $V=$ 3.6,3.7, and 3.8 at three temperatures: (a) $T=0.25$ (near $T_{MIT}$), (b) $T=0.15$ (near $T_{N}$ and $T_{CO}$), and (c) $T=0.005$. The DOS for different $V$ values overlap at $T=0.25$ and $T=0.15$. At low temperature ($T=0.005$), the DOS for $V=3.6$ and $3.7$ (AF ground state) separates from that of $V=3.8$ (CO ground state). (d) Temperature dependence of $t_{eff}$ for $V=3.6,3.7$, and 3.8, which overlap down to the ordering temperature and separate below it. Inset: $IPR(\epsilon_{F})$ shows a similar behavior.

3.7, while it becomes charge ordered (CO) for $V=3.8$. The corresponding ordering temperatures, namely the Neel temperature $T_{N}$ and the charge-ordering temperature $T_{CO}$, are nearly identical ($T_{N}\sim T_{CO}\sim 0.15$). To examine the origin of these ordered states, we analyze the density of states (DOS) at three representative temperatures: $T=0.25$ (near the metal-insulator transition temperature $T_{MIT}$), $T=0.15$ (near $T_{N}$ and $T_{CO}$), and a low temperature $T=0.005$, as shown in Fig. 6(a)-(c). At low temperature, the DOS in both AF and CO phases exhibits a clear gap around the Fermi level ($\omega=0$), indicating insulating behavior. The opening of this gap coincides with the onset of long-renge order. Notably, across $V=3.7$, the gap appears at nearly the same temperature for both AF and CO phases, suggesting that the electronic gap drives the transition to the ordered phase, while the values of $U$ and $V$ determine the nature of the ordered state. At higher temperatures, the metal-insulator transition occurs at approximately the same temperature ($T_{MIT}\sim 0.25$) for both AF and CO ground states. The DOS curves collapse onto each other near $T_{MIT}$ (Fig. 6(a)) and also near the ordering temperature (Fig. 6(b)), indicating that the electronic spectra are indistinguishable above the ordering temperatures. To support this observation, we compute the effective hopping parameter $t_{eff}$ (a measure of the average kinetic energy) and the inverse participation ratio $IPR(\epsilon_{F})$ (a measure of electronic localization), shown in Fig. 6(d). The $t_{eff}$ curves overlap down to the ordering temperature and separate below it, consistent with the DOS results. The IPR shows a similar trend (see the inset of Fig. 6(d)). These results indicate a universal electronic behavior above the ordering temperature, suggesting that the electronic DOS plays a dominant role in driving the metal-insulator transition.

![](./images/1253321735852261392_7.jpg)

FIG. 7: (a) Density of states (DOS) for $U=8,V=2$, and temperatures $T=1.6,1,0.6$, and 0.45. In this parameter regime, the ground state is antiferromagnetic (AF) [Fig. 4(a)], and a pseudogap develops below $T\sim 1$. (b) DOS for $U=8$, $V=5$, and $T=2,1.4,1,0.6$, and 0.51. Here the ground state is charge ordered (CO), and a pseudogap appears below $T\sim$ 1.4. Temperature dependence of the DOS at the Fermi level, $DOS(0)$, for (c) $V\leq 3.7$ (AF phase) and (d) $V>3.7$ (CO phase), respectively. The peak in $DOS(0)$, associated with pseudogap formation, shifts to lower (higher) temperatures with increasing $V$ in the AF (CO) regime. The increasing magnitude of $DOS(0)$ for $V\leq 3.7$ reflects enhanced charge fluctuations, consistent with the $\chi_{n}$ results in Fig. 8(b).

Since the spectral properties exhibit a degree of universality near the transition line, it is important to investigate them across the entire $V$-$T$ phase diagram in Fig. 4(a), particularly at higher temperatures. For this purpose, we consider two representative points away from the transition line: $U=8,V=2$ and $U=8,V=5$, corresponding to AF and CO ground states, respectively. Figure 7(a) shows that for $U=8,V=2$, the DOS begins to develop a local minimum around the Fermi level ($\omega=0$) below $T\sim 1$, while the corresponding metal-insulator transition occurs at $T_{MIT}\sim 0.4$. Similarly, for $U=8,V=5$, a local minimum appears below $T\sim 1.4$ (Fig. 7(b)), which is significantly higher than the transition temperature $T_{MIT}\sim 0.51$. These results indicate that insulating behavior emerges when a sufficient gap forms in the DOS at the Fermi level, leading to a metal-insulator transition with $T_{MIT}<T_{PG}$. Here, $T_{PG}$ denotes the pseudogap formation temperature, defined as the highest temperature below which the DOS develops a minimum at the Fermi level, following the conventional definition used in correlated materials$^{128}$. To determine $T_{PG}$, we compute the DOS weight at the Fermi level, $DOS(0)$, for both $V\leq 3.7$ and $V>3.7$, as shown in Fig. 7(c) and (d). In the AF regime ($V\leq 3.7$), the

![](./images/1253321735852261392_8.jpg)

FIG. 8: (a) Temperature dependence of the bipolaronic order parameter BPO (right) and $DOS(0)$ (left) for fixed $U=8$ and $V=1$ and 3. The peaks of BPO and $DOS(0)$ occur at nearly the same temperature, indicating a close connection between pseudogap formation and charge imbalance. Density susceptibility $\chi_n$ for (b) $V \leq 3.7$ (AF ground state) and (c) $V>3.7$ (CO ground state). Arrows mark the pseudogap formation temperature $T_{PG}$, obtained from the peak in $DOS(0)$ [Fig. 7(c) and (d)]. Significant charge fluctuations below $T_{PG}$ lead to pseudogap formation. (d) Spin susceptibility $\chi_s$ for $V \leq 3.7$; the peak corresponds to the antiferromagnetic Neel temperature $T_N$.

peak position of $DOS(0)$, which signals $T_{PG}$, shifts to lower temperatures as $V$ approaches the transition line $V=3.7$, while its magnitude increases. This behavior likely arises from enhanced charge fluctuations (short-range charge correlations) at higher temperatures as the system approaches the boundary. The trend is consistent with the resistivity results in Fig. 4(b) and indicates enhanced metallicity near the transition line. In contrast, for $V>3.7$, the peak position of $DOS(0)$ shifts to higher temperatures with increasing $V$, while its magnitude decreases (Fig. 7(d)). This reduction in $DOS(0)$ is associated with the increasing tendency toward localized bipolaron formation with increasing $V$ (see also Fig. 5(b)).

To examine the correlation between pseudogap formation and charge imbalance at high temperatures for $V \leq 3.7$ (where the ground state is AF), we plot the bipolaronic order parameter (BPO) and $DOS(0)$ for $V=1$ and 3 in Fig. 8(a). The peak positions of $DOS(0)$ coincide with those of the BPO, indicating that pseudogap formation is closely related to charge imbalance. In other words, sufficiently strong charge fluctuations (short-range charge correlations) drive the pseudogap formation. To further support this observation, we calculate the density susceptibility $\chi_n=\frac{1}{N}(<n^2>-<n>^2)^{91,128}$ for different $V$ values in the AF regime, shown in Fig. 8(b). A pronounced enhancement of charge fluctuations is observed below the pseudogap formation temperature $T_{PG}$ (indicated by the solid black arrow), estimated from the peak positions in Fig. 7(c). As $V$ decreases (moving away from the transition line), the charge fluctuations weaken, leading to a reduction in $DOS(0)$, consistent with Fig. 7(c). Similarly, for $V>3.7$, a significant density susceptibility is observed below $T_{PG}$, as shown in Fig. 8(c). In this regime (CO phase), the peak in $\chi_n$ corresponds to the charge ordering transition, and its temperature follows the same $V$-dependence as $T_{CO}$. Furthermore, the magnetic susceptibility $\chi_s$ [$\chi_s=\frac{1}{N}(<(S^z)^2>-<S^z>^2)$, $S^z=\frac{1}{N}\sum_i S_i^z$] also exhibits peaks that coincide with the antiferromagnetic transition for $V \leq 3.7$, as shown in Fig. 8(d). The Neel temperature $T_N$ aligns well with the peak positions of $\chi_s$.

### VII. MAGNETOTRANSPORT PROPERTIES FOR LOW TO INTERMEDIATE U AND V COMBINATIONS ACROSS THE BOUNDARY

In this section, we explore the physics of low to intermediate values of $U$ and $V$ at half-filling, which may be relevant for materials where both electronic correlations and electron-phonon coupling are moderate. We focus on the magnetotransport and electronic spectral properties by evaluating the resistivity $(\rho)$ and density of states (DOS), as shown in Fig. 9. Figure 9(a) presents the resistivity for fixed $V=3$ and varying $U=5,6,7,8$ across the boundary of the $U$-$V$ phase diagram in Fig. 1(a). The system is in the charge-ordered (CO) phase for $U=5$ and 6, while it exhibits an antiferromagnetic (AF) phase for $U=7$ and 8 at low temperatures, as shown in the inset of Fig. 9(a). In both phases, the system undergoes a metal-insulator transition and becomes insulating at low temperatures. In the CO phase, the charge-ordering temperature $T_{CO}$ decreases with increasing $U$, reflecting the suppression of onsite double occupancy by the Hubbard interaction. In this regime, the metal-insulator transition temperature approximately coincides with the charge-ordering temperature $(T_{MIT} \sim T_{CO})$. In contrast, in the AF phase for $U=8$, the metal-insulator transition temperature exceeds the Neel temperature $(T_{MIT}>T_N)$, indicating the presence of a Mott insulating state. To further understand the spectral properties, we analyze two representative points in the phase diagram: $V=3,U=5$ (CO phase) and $V=3,U=8$ (AF phase). The $DOS(\omega)$ for both cases shows a clear gap at low temperature (Fig. 9(b)) around the Fermi level $(\omega=0)$, confirming the insulating behavior observed in the transport results [Fig. 9(a)]. The gap is larger in the AF phase due to the stronger Hubbard interaction. In the CO phase $(U=5)$, the gap decreases with increasing temperature (Fig. 9(c)) and disappears just above the charge-ordering temperature $(T_{CO} \sim 0.22)$, resulting in a metallic state consistent with the resistivity results. In contrast, in the AF phase $(U=8)$, a pseudogap feature appears in the DOS above the Neel temperature $(T_N \sim 0.18)$, as shown in Fig. 9(d). This pseudogap originates from local fluctuations of spin, charge, and phonon degrees of freedom

![](./images/1253321735852261392_9.jpg)

FIG. 9: (a) Resistivity $\rho$ vs $T$ for fixed $V=3$ and varying $U=5,6,7$, and 8 across the phase boundary in Fig. 1(a). The system exhibits a metal-insulator transition (MIT) for all $U$. Inset: structure factors $CO(\pi,\pi,\pi)$ (solid) and $S(\pi,\pi,\pi)$ (dashed). $T_{MIT}$ coincides with $T_{CO}$, while for $U=8$ (AF phase) $T_{MIT}>T_N$. (b) DOS near the Fermi level ($\omega=\epsilon_F=0$) at $T=0.005$, showing a clear gap in both CO ($U=5$) and AF ($U=8$) phases. (c) For $U=5$ (CO phase), the gap weakens with increasing $T$ and closes above $T_{CO}\sim0.22$, yielding a finite DOS at the Fermi level. (d) For $U=8$ (AF phase), the gap softens with increasing $T$ and evolves into a pseudogap above $T_N\sim0.18$, with spectral weight at the Fermi level arising from local spin correlations.

![](./images/1253321735852261392_10.jpg)

FIG. 10: (a) Phonon distribution $P(Q)$ at $T=0.005$ for fixed $V=3$ in the charge-ordered ($U=5$) and antiferromagnetic ($U=8$) phases. $P(Q)$ exhibits a bimodal distribution in the CO phase and a unimodal distribution in the AF phase. (b) Corresponding local moment distributions $P(M)$, showing unimodal behavior in both phases. Inset: In the CO phase, the density $P(n)$ (magenta) and double occupancy $P(d=n_\uparrow n_\downarrow)$ (blue) are bimodal, whereas $P(M)$ (black) remains unimodal. Legends in (a) and (b) are identical. Temperature evolution of sublattice-resolved densities $(n_A,n_B)$, double occupancies $(d_A,d_B)$, and local moments $(M_A,M_B)$ for (c) $U=5,V=3$ (CO phase) and (d) $U=8,V=3$ (AF phase).

above $T_N$, which introduce finite spectral weight inside the gap region. Such fluctuation-driven pseudogap behavior also results in well-known non-Drude features in the optical conductivity$^{88}$.

To further characterize the ground-state phases beyond transport and spectral properties, we examine the phonon distribution function P(Q) and the local moment distribution P(M) at low temperature $T=0.005$, shown in Fig. 10(a) and (b). In the CO phase ($V=3,U=5$), P(Q) exhibits a bimodal distribution$^{88,129}$, indicating a staggered pattern of elongated and contracted phonon modes, consistent with experimental observations$^{25,40,99}$. In contrast, the antiferromagnetic (AF) phase ($V=3,U=8$) shows a unimodal phonon distribution, reflecting uniform lattice distortion and nearly uniform site occupancy. The local moment distribution P(M), however, remains unimodal in both phases (Fig. 10(b)). In the AF phase, the peak occurs at a larger moment due to reduced double occupancy at larger $U$. In the CO phase, the peak appears at a smaller moment. Interestingly, despite the bimodal distributions of density $n$ and double occupancy $d=n_\uparrow n_\downarrow$ in the CO phase (inset of Fig. 10(b)), P(M) remains unimodal. To clarify this behavior, we compute sublattice-resolved quantities $n_{A,B}$, $d_{A,B}$, and $M_{A,B}$ (Fig. 10(c)). Below the charge-ordering temperature $T_{CO}$, the A-sublattice shows an increase in density and double occupancy, while the B-sublattice shows a corresponding decrease. This results in equivalent local moments on both sublattices ($M_A=n_A-2d_A\equiv M_B=n_B-2d_B$), leading to a uniform local moment distribution in the CO phase. The sublattice splitting of double occupancy is consistent with earlier studies$^{93}$. For completeness, the corresponding sublattice-resolved quantities for the AF phase are shown in Fig. 10(d). Here $n_A\sim n_B$ and $d_A\sim d_B$, with very small double occupancy, producing a larger average local moment compared to the CO phase, while still satisfying $M_A\sim M_B$.

Most previous studies of the half-filled Hubbard-Holstein model in lower dimensions ($1D$ and $2D$) report a metallic phase at small $U$ and $V$ near the boundary between the AF and CO phases. In contrast, our $U$-$V$ phase diagram in Fig. 1(a) shows no evidence of a metallic phase in this regime. To substantiate this result, we examine the magnetic, transport, and electronic properties for small $U$ and $V$. We first analyze the magnetotransport properties at $V=2$ by varying $U=3,4,5$, and 6 across the phase boundary in Fig. 1(a). For $U=3,4$ the system is in the CO phase, while for $U=5,6$ it is in the AF phase, as confirmed by $S(\pi,\pi,\pi)$ and $CO(\pi,\pi,\pi)$ calculations (not shown). As shown in Fig. 11(a), the system exhibits a metal-insulator transition for all values of $U$. Specifically, the transitions for $U=3,4$ ($U=5,6$) correspond to charge (spin) ordering. In this weak-coupling regime, CO arises from Peierls instability$^{24,130}$, while AF order originates from Slater instability$^{117}$ driven by

![](./images/1253321735852261392_11.jpg)

FIG. 11: (a) Resistivity $\rho$ vs temperature $T$ for fixed $V=2$ and $U=3$–6 across the phase boundary in Fig. 1(a). MITs for $U=3,4$ correspond to charge ordering (solid) and for $U=5,6$ to spin ordering (dashed). (b) DOS for CO ($V=2,U=3$) and AF ($V=2,U=6$) phases at $T=0.005$ and $0.2$. At low $T$, both phases show a clear gap; at $T=0.2$ (above ordering), the DOS at the Fermi level is finite. $\rho$ vs $T$ for (c) $V=1$, $U=1$–4 and (d) $V=0.5$, $U=0$–3. All cases exhibit MITs, with insulating ground states at low temperatures.

Fermi-surface nesting$^{64,131}$. Consequently, $T_{MIT}$ coincides with the corresponding ordering temperature ($T_{CO}$ or $T_N$). Moreover, $T_{MIT}$ increases away from the phase boundary-decreasing $U$ in the CO phase and increasing $U$ in the AF phase. The DOS at low temperature ($T=0.005$) exhibits a clear gap at the Fermi level for both CO ($U=3$) and AF ($U=6$) phases, confirming insulating ground states (Fig. 11(b)). At higher temperature ($T=0.2$), above the ordering temperatures, a finite DOS at the Fermi level indicates metallic behavior, consistent with the resistivity results. We further compute resistivity for smaller values $V=1,0.5$, and below $0.5$ while varying $U$ across the phase boundary. In all cases, the system undergoes a metal-insulator transition and remains insulating at low temperatures, as shown in Fig. 11(c) and (d). These results collectively support the absence of a metallic phase in the $U$-$V$ phase diagram of Fig. 1(a). Overall, in three dimensions the competition between $U$ and $V$ at small coupling strengths does not overcome Fermi-surface instabilities, and the system retains its insulating character.

## VIII. FEATURES ALONG THE BOUNDARY OF THE PHASE DIAGRAM

In the previous sections, we characterized the phases across the $U$-$V$ phase diagram by varying $U$ at fixed $V$ and vice versa. Here, we investigate the properties along the phase boundary, indicated by the blue (AF) and red (CO) lines in Fig. 1(a). Since phases near the boundary are highly sensitive to perturbations, factors such as doping, strain, frustration, or long-range hopping may drive transitions or stabilize new phases. Therefore, understanding the physics along the boundary is important. To examine this, we consider several $(U,V)$ points along the CO boundary (red line in Fig. 1(a)): $(0.5,0.5)$, $(1,1)$, $(3,2)$, $(5,3)$, $(7,4)$, $(9,5)$, $(11,6)$, $(13,7)$, $(15,8)$, $(17,9)$, $(19,10)$. Similarly, along the AF boundary (blue line in Fig. 1(a)) we consider: $(2,0.5)$, $(4,1)$, $(6,2)$, $(8,3)$, $(10,4)$, $(12,5)$, $(14,6)$, $(16,7)$, $(18,8)$, $(20,10)$, $(22,10)$.

![](./images/1253321735852261392_12.jpg)

FIG. 12: (a) The Neel temperature $T_N$ for the pure Hubbard model ($V=0$) shows a nonmonotonic dependence on $U$, reaching a maximum around $U\sim8$. The inset displays the charge-ordering temperature $T_{CO}$ for the pure Holstein model ($U=0$), which also shows nonmonotonic behavior with an optimum near $V\sim5$. (b) $T_N$ is plotted for a series of $(U,V)$ points along the AF boundary (blue line) in Fig. 1(a): $(2,0.5)$, $(4,1)$, $(6,2)$, $(8,3)$, $(10,4)$, $(12,5)$, $(14,6)$, $(16,7)$, $(18,8)$, $(20,10)$, $(22,10)$ (set-I). For clarity, the plot shows only the variation with $U$. The inset shows $T_{CO}$ along the CO boundary (red line) in Fig. 1(a) for the points $(0.5,0.5)$, $(1,1)$, $(3,2)$, $(5,3)$, $(7,4)$, $(9,5)$, $(11,6)$, $(13,7)$, $(15,8)$, $(17,9)$, $(19,10)$ (set-II), displayed as a function of $V$. Sublattice-resolved densities ($n_A,n_B$), double occupancies ($d_A,d_B$), and local moments ($M_A,M_B$) are shown along the boundary line in the (c) CO phase (set-II) and (d) AF phase (set-I). The inset of (d) presents the variation of $\Delta S_z=|S_z^A-S_z^B|$ along the CO and AF boundaries.

In order to compare our results obtained along the phase boundary in presence of both $U$ and $V$ with pure Hubbard ($U=0$) or Holstein ($V=0$) limits, we first describe the properties in these pure limits and then discuss the case varying both $U$ and $V$ along the boundary. For the pure Hubbard limit ($V=0$), the system remains antiferromagnetic for any finite $U$, and the Neel temperature $T_N$ varies nonmonotonically$^{105,106}$ with $U$ (Fig. 12(a)). In the pure Holstein limit ($U=0$), the charge-ordering temperature $T_{CO}$ also shows a nonmonotonic dependence on $V$, as shown in the inset of Fig. 12(a). Although no direct results exist for the 3D Holstein model, similar behavior has been reported in two dimensions$^{88}$, despite de-

bates about long-range order due to the Mermin-Wagner theorem $^{132,133}$. A DMFT study on a bipartite lattice $^{129}$ also reported nonmonotonic $T_{CO}$ with unimodal and bimodal phonon distributions depending on the electron-phonon coupling. In contrast, our study (in the adiabatic limit) shows only bimodal phonon distributions. Along the AF boundary, the nonmonotonic behavior of $T_N$ persists even with finite $V$ (12(b)), reaching a maximum near $(U,V)=(8,3)$. However, the magnitude of $T_N$ is slightly reduced compared to the pure Hubbard case, indicating that the physics in the AF phase is primarily governed by $U$, with $V$ providing a secondary effect. Similarly, along the CO boundary, $T_{CO}$ retains its nonmonotonic behavior (inset of Fig. 12(b)) and reaches a maximum near $(U,V)=(9,5)$. The magnitude of $T_{CO}$, however, is significantly reduced in the presence of finite $U$ compared to the pure Holstein model.

At low temperature $T=0.005$ in the CO regime, the A-sublattice density $n_A$ increases with $U$, while $n_B$ decreases along the boundary line (Fig. 12(c)). Although both $U$ and $V$ vary, the plot is shown versus $U$ for clarity. The densities saturate at $n_A \sim 2$ and $n_B \sim 0$ for $U \geq 11$ ($V \geq 5$). Thus, densities split along the boundary even for small $(U,V)$, with a similar splitting in double occupancies: $d_A$ increases and $d_B$ decreases, saturating at $d_A \sim 1$ and $d_B \sim 0$. This corresponds to an alternating pattern of doubly occupied and empty sites in the CO phase. Despite this, the local moments remain equal in both sublattices ($M_A=M_B$), decreasing from the paramagnetic limit (0.5) toward the bipolaronic limit (0) with increasing $U$. In the AF regime, the sublattice densities remain equal ($n_A=n_B=1$) along the boundary (Fig. 12(d)). The double occupancies decrease with increasing $U$, leading to larger local moments, with $M_A=M_B$. To further distinguish the phases, we evaluate $\Delta S_z=|S_z^A - S_z^B|$ (inset of Fig. 12(d)). $\Delta S_z$ vanishes in the CO phase but is finite in the AF phase and increases with $U$. These results provide a comprehensive description of the behavior of the AF and CO phases in the presence of both $U$ and $V$ along the phase boundary, and are therefore important for understanding and designing quantum materials that host both AF and CO phases, as well as for studying the proximity effects between them.

## IX. CONCLUSIONS

Motivated by the lack of theoretical studies in three dimensions and the experimental relevance of coexisting electronic correlations and electron-phonon interactions, we investigate the magnetotransport properties of the half-filled one-band Hubbard-Holstein model using an exact diagonalization based semiclassical Monte Carlo (s-MC) approach. We first establish the ground-state $U$-$V$ phase diagram, where the antiferromagnetic (AF) and charge-ordered (CO) phases are separated by a first-order transition line. Throughout the phase diagram, the system remains insulating, as confirmed by resistivity and density-of-states (DOS) calculations. In particular, no metallic phase is found even for small $U$ and $V$, suggesting that the observed AF-I and CO-I phases are more robust in three dimensions than in lower dimensions. For an optimal correlation strength $U=8$, the $V$-$T$ phase diagram reveals a rich set of phases, including AF-I, CO-I, MH-I, BP-I, BP-M*, and BP-M. Robust first-order metal-to-metal and insulator-to-insulator transitions occur near $V \sim 3.75$. The distinction between BP-M and BP-M* is identified from the temperature dependence of the bipolaronic order parameter. Notably, the DOS collapses near the transition line above the ordering temperatures, indicating a universal high-temperature behavior dominated by electronic contributions. Fluctuations arising from short-range correlations, which give rise to pseudogap features, are systematically characterized through calculations of susceptibilities, DOS, and the bipolaronic order parameter.

We also examine magnetic and charge-order profiles along the phase boundaries of the $U$-$V$ diagram, where both $U$ and $V$ vary. Along these boundaries, the nonmonotonic behavior of $T_N$ ($T_{CO}$) with $U$ ($V$) persists in the AF (CO) regimes. However, $T_N$ is slightly reduced by finite $V$, while $T_{CO}$ is strongly suppressed by $U$. Understanding the behavior of physical properties along these boundaries may aid in designing heterostructures combining AF and CO components, where interface effects and the competition or coexistence of these phases could lead to new phenomena. We leave such studies for future work.

## ACKNOWLEDGMENT

S. H. acknowledges Kreitman School of Advanced Graduate Studies at BGU for providing the Kreitman Postdoctoral Fellowship. M. S. acknowledges support by the Israel Science Foundation Grant No. 3679/24.

* Electronic address: halder@post.bgu.ac.il
† Electronic address: smoshe@bgu.ac.il
$^{1}$ Elbio Dagotto. Complexity in strongly correlated electronic systems. *Science*, 309(5732):257-262, 2005.
$^{2}$ Masatoshi Imada, Atsushi Fujimori, and Yoshinori Tokura. Metal-insulator transitions. *Rev. Mod. Phys.*, 70:1039-1263, Oct 1998.
$^{3}$ Andrea Damascelli, Zahid Hussain, and Zhi-Xun Shen. Angle-resolved photoemission studies of the cuprate superconductors. *Rev. Mod. Phys.*, 75:473-541, Apr 2003.

4 Miodrag L. Kulić. Interplay of electron-phonon in- teraction and strong correlations: the possible way to high-temperature superconductivity. Physics Reports,338(1):1-264, 2000.

5 M. Capone, C. Castellani, and M. Grilli. Electron-phonon interaction in strongly correlated systems. Advances in Condensed Matter Physics, 2010(1):920860, 2010.

6 J. Mannhart and D. G. Schlom. Oxide interfaces-an op- portunity for electronics. Science, 327(5973):1607-1611,2010.

7 Elbio Dagotto, Takashi Hotta, and Adriana Moreo. Colos- sal magnetoresistant materials: the key role of phase sep- aration. Physics Reports, 344(1):1-153, 2001.

8 Byoung Ki Choi, Luca Moreschini, Aaron Bostwick, R. Stanley Williams, Young Jun Chang, and Eli Roten- berg. Correlation control of the mott transition in la- tio3/srtio3 heterostructures. Communications Materials,7(1):18, 2025.

9 C. H. Ahn, J.-M. Triscone, and J. Mannhart. Elec- tric field effect in correlated oxide systems. Nature,424(6952):1015-1018, 2003.

10 Philipp Scheiderer, Matthias Schmitt, Judith Gabel, Michael Zapf, Martin Stübinger, Philipp Schütz, Lenart Dudy, Christoph Schlueter, Tien-Lin Lee, Michael Sing,and Ralph Claessen. Tailoring materials for mottronics: Excess oxygen doping of a prototypical mott insulator. Advanced Materials, 30(25):1706708, 2018.

11 You Zhou and Shriram Ramanathan. Mott memory and neuromorphic devices. Proceedings of the IEEE,103(8):1289-1310, 2015.

12 Ting-Chang Chang, Kuan-Chang Chang, Tsung-Ming Tsai, Tian-Jian Chu, and Simon M. Sze. Resistance random access memory. Materials Today, 19(5):254-264,2016.

13 Uday S. Goteti, Ivan A. Zaluzhnyy, Shriram Ramanathan, Robert C. Dynes, and Alex Frano. Low-temperature emergent neuromorphic networks with correlated oxide devices. Proceedings of the National Academy of Sciences,118(35):e2103934118, 2021.

14 P. Wadley, B. Howells, J. Železný, C. Andrews, V. Hills, R. P. Campion, V. Novák, K. Olejník, F. Maccherozzi, S. S. Dhesi, S. Y. Martin, T. Wagner, J. Wunderlich, F. Freimuth, Y. Mokrousov, J. Kuneš, J. S. Chauhan, M. J. Grzybowski, A. W. Rushforth, K. W. Edmonds, B. L. Gallagher, and T. Jungwirth. Electrical switching of an antiferromagnet. Science, 351(6273):587-590, 2016.

15 X. Marti, I. Fina, C. Frontera, Jian Liu, P. Wadley, Q. He, R. J. Paull, J. D. Clarkson, J. KudrnovskÃœ, I. Turek, J. KuneÅ¡, D. Yi, J.-H. Chu, C. T. Nelson, L. You, E. Arenholz, S. Salahuddin, J. Fontcuberta, T. Jungwirth, and R. Ramesh. Room-temperature antiferromagnetic memory resistor. Nature Materials, 13(4):367-374, 2014.

16 Zheng Yang, Changhyun Ko, and Shriram Ramanathan. Oxide electronics utilizing ultrafast metal-insulator tran- sitions. Annual Review of Materials Research, 41(Volume41, 2011):337-367, 2011.

17 Guangdong Zhou, Zhongrui Wang, Bai Sun, Feichi Zhou, Linfeng Sun, Hongbin Zhao, Xiaofang Hu, Xiaoyan Peng, Jia Yan, Huamin Wang, Wenhua Wang, Jie Li, Bingtao Yan, Dalong Kuang, Yuchen Wang, Lidan Wang, and Shukai Duan. Volatile and nonvolatile memristive devices for neuromorphic computing. Advanced Electronic Mate- rials, 8(7):2101127, 2022.

18 Ki Chang Kwon, Ji Hyun Baek, Kootak Hong, Soo Young Kim, and Ho Won Jang. Memristive devices based on two- dimensional transition metal chalcogenides for neuromor- phic computing. Nano-Micro Letters, 14(1):58, 2022.

19 Ying Li. Simulation of memristive synapses and neuro- morphic computing on a quantum computer. Phys. Rev. Res., 3:023146, May 2021.

20 Sieu D. Ha, Jian Shi, Yasmine Meroz, L. Mahadevan, and Shriram Ramanathan. Neuromimetic circuits with synap- tic devices based on strongly correlated electron systems. Phys. Rev. Appl., 2:064003, Dec 2014.

21 Irem Boybat, Manuel Le Gallo, S. R. Nandakumar, Tim- oleon Moraitis, Thomas Parnell, Tomas Tuma, Bipin Ra- jendran, Yusuf Leblebici, Abu Sebastian, and Evange- los Eleftheriou. Neuromorphic computing with multi- memristive synapses. Nature Communications, 9(1):2514,2018.

22 Cesare Franchini, Michele Reticcioli, Martin Setvin, and Ulrike Diebold. Polarons in materials. Nature Reviews Materials, 6(7):560-586, 2021.

23 Y. Y. Peng, A. A. Husain, M. Mitrano, S. X.-L. Sun, T. A. Johnson, A. V. Zakrzewski, G. J. MacDougall, A. Barbour, I. Jarrige, V. Bisogni, and P. Abbamonte. Enhanced electron-phonon coupling for charge-density- wave formation in $la_{1.8-x}eu_{0.2}sr_{x}cuo_{4+\delta}$. Phys. Rev. Lett.,125:097002, Aug 2020.

24 R. E. Peierls, editor. Quantum Theory of Solids. Claren- don Oxford, 1955.

25 J. A. Alonso, J. L. García-Muñoz, M. T. Fernández-Díaz, M. A. G. Aranda, M. J. Martínez-Lope, and M. T. Casais. Charge disproportionation in $Rnio_{3}$ perovskites: Simulta neous metal-insulator and structural transition in $ynio_{3}$. Phys. Rev. Lett., 82:3871-3874, May 1999.

26 Minjae Kim. Signatures of spin-orbital states of $t_{2g}^{2}$ sys tem in optical conductivity: $rvo_{3}$ ($r=$ Y and la). Phys. Rev. B, 97:155141, Apr 2018.

27 Nikolai V. Prokof'ev and Boris V. Svistunov. Polaron problem by diagrammatic quantum monte carlo. Phys. Rev. Lett., 81:2514-2517, Sep 1998.

28 P. E. Kornilovitch. Continuous-time quantum monte carlo algorithm for the lattice polaron. Phys. Rev. Lett.,81:5382-5385, Dec 1998.

29 J. Bonc`a, T. Katrasˇnik, and S. A. Trugman. Mobile bipolaron. Phys. Rev. Lett., 84:3153-3156, Apr 2000.

30 Zhiying Bai, Dawei He, Shaohua Fu, Qing Miao, Shuangyan Liu, Mohan Huang, Kun Zhao, Yongsheng Wang, and Xiaoxian Zhang. Recent progress in elec- tron-phonon interaction of two-dimensional materials. Nano Select, 3(7):1112-1122, 2022.

31 Ronald Ulbricht, Euan Hendry, Jie Shan, Tony F. Heinz, and Mischa Bonn. Carrier dynamics in semiconductors studied with time-resolved terahertz spectroscopy. Rev. Mod. Phys., 83:543-586, Jun 2011.

32 J. K. Chen, W. P. Latham, and J. E. Beraun. The role of electron-phonon coupling in ultrafast laser heating. Jour- nal of Laser Applications, 17(1):63-68, 02 2005.

33 Charles J. Sayers, Armando Genco, Chiara Trovatello, Stefano Dal Conte, Vladislav O. Khaustov, Jorge Cervantes-Villanueva, Davide Sangalli, Alejandro Molina- Sanchez, Camilla Coletti, Christoph Gadermaier, and Giulio Cerullo. Strong coupling of coherent phonons to excitons in semiconducting monolayer mote2. Nano Let- ters, 23(20):9235-9242, Oct 2023.

34 A. Benyamini, A. Hamo, S. Viola Kusminskiy, F. von Oppen, and S. Ilani. Real-space tailoring of the elec-

tronâ??phonon coupling in ultraclean nanotube mechani- cal resonators. *Nature Physics*, 10(2):151–156, 2014.

35 Jun Yan, M.-H. Kim, J. A. Elle, A. B. Sushkov, G. S. Jenkins, H. M. Milchberg, M. S. Fuhrer, and H. D. Drew. Dual-gated bilayer graphene hot-electron bolometer. *Na- ture Nanotechnology*, 7(7):472–478, 2012.

36 Iris Niehues, Robert Schmidt, Matthias DrÃœppel, Philipp Marauhn, Dominik Christiansen, Malte Selig, Gunnar BerghÃœser, Daniel Wigger, Robert Schneider, Lisa Braasch, Rouven Koch, Andres Castellanos-Gomez, Tilmann Kuhn, Andreas Knorr, Ermin Malic, Michael Rohlfing, Steffen Michaelis de Vasconcellos, and Rudolf Bratschitsch. Strain control of excitonâ??phonon cou- pling in atomically thin semiconductors. *Nano Letters*, 18(3):1751–1757, Mar 2018.

37 Dao-Sheng Tang, Guang-Zhao Qin, Ming Hu, and Bing- Yang Cao. Thermal transport properties of gan with bi- axial strain and electron-phonon coupling. *Journal of Ap- plied Physics*, 127(3):035102, 01 2020.

38 A. Lanzara, P. V. Bogdanov, X. J. Zhou, S. A. Kellar, D. L. Feng, E. D. Lu, T. Yoshida, H. Eisaki, A. Fuji- mori, K. Kishio, J.-I. Shimoyama, T. Noda, S. Uchida, Z. Hussain, and Z.-X. Shen. Evidence for ubiquitous strong electronâ??phonon coupling in high-temperature superconductors. *Nature*, 412(6846):510–514, 2001.

39 O. Gunnarsson. Superconductivity in fullerides. *Rev. Mod. Phys.*, 69:575–606, Apr 1997.

40 Kristjan Haule and Gheorghe L. Pascut. Mott transition and magnetism in rare earth nickelates and its fingerprint on the x-ray scattering. *Scientific Reports*, 7(1):10375, 2017.

41 Evgeny A. Stepanov, Matteo Vandelli, Alexander I. Licht- enstein, and Frank Lechermann. Charge density wave or- dering in ndnio2: effects of multiorbital nonlocal correla- tions. *npj Computational Materials*, 10(1):108, 2024.

42 J. M. Tranquada, J. E. Lorenzo, D. J. Buttrey, and V. Sachan. Cooperative ordering of holes and spins in la2nio4.125. *Phys. Rev. B*, 52:3581–3595, Aug 1995.

43 A. J. Millis, P. B. Littlewood, and B. I. Shraiman. Dou- ble exchange alone does not explain the resistivity of $La_{1-x}Sr_xMnO_3$. *Phys. Rev. Lett.*, 74:5144–5147, Jun 1995.

44 A. J. Millis. Lattice effects in magnetoresistive manganese perovskites. *Nature*, 392(6672):147–150, 1998.

45 B J Powell and Ross H McKenzie. Strong electronic cor- relations in superconducting organic charge transfer salts. *Journal of Physics: Condensed Matter*, 18(45):R827, oct 2006.

46 Jun Zhan, Yuhao Gu, Xianxin Wu, and Jiangping Hu. Cooperation between electron-phonon coupling and elec- tronic interaction in bilayer nickelates la3ni2o7. *Phys. Rev. Lett.*, 134:136002, Mar 2025.

47 Runxue Wang, Xipeng Zhang, Hengyang Xie, Yuanhui Xu, Keju Sun, Yanlong Yu, Yongshan Liu, and Xian- feng Hao. Role of electronic correlation effect on charge ordering in $\beta$-v2opo4. *Computational Materials Science*, 173:109433, 2020.

48 Qisi Wang, Karin von Arx, Masafumi Horio, Deepak John Mukkattukavil, Julia Küspert, Yasmine Sassa, Thorsten Schmitt, Abhishek Nag, Sunseng Pyon, Tomohiro Takayama, Hidenori Takagi, Mirian Garcia-Fernandez, Ke-Jin Zhou, and Johan Chang. Charge order lock-in by electron-phonon coupling in la1.675eu0.2sr0.125cuo4. *Sci- ence Advances*, 7(27):eabg7394, 2021.

49 Alexandru B. Georgescu and Andrew J. Millis. Quan- tifying the role of the lattice in metalâ??insulator phase transitions. *Communications Physics*, 5(1):135, 2022.

50 M. Ge, T. F. Qi, O. B. Korneta, D. E. De Long, P. Schlottmann, W. P. Crummett, and G. Cao. Lattice- driven magnetoresistivity and metal-insulator transition in single-layered iridates. *Phys. Rev. B*, 84:100402, Sep 2011.

51 Qingzhuo Duan, Zixuan Jia, Zenghui Fan, Runyu Ma, Jingyao Meng, Bing Huang, and Tianxing Ma. Breathing- driven metal-insulator transition in correlated kagome systems. *Chinese Physics Letters*, 42(9):090712, sep 2025.

52 J.H. Ngai, F.J. Walker, and C.H. Ahn. Correlated ox- ide physics and electronics. *Annual Review of Materials Research*, 44(Volume 44, 2014):1–17, 2014.

53 C. W. Bark, D. A. Felker, Y. Wang, Y. Zhang, H. W. Jang, C. M. Folkman, J. W. Park, S. H. Baek, H. Zhou, D. D. Fong, X. Q. Pan, E. Y. Tsymbal, M. S. Rzchowski, and C. B. Eom. Tailoring a two-dimensional electron gas at the laalo₃/srTiO₃ (001) interface by epitaxial strain. *Proceedings of the National Academy of Sciences*, 108(12):4720–4724, 2011.

54 Yukio Watanabe. Dft $+U$ accurate for strain effect and overall properties of perovskite oxide ferroelectronics and polaron. *Journal of Applied Physics*, 135(22), Jun 2024.

55 Mathieu Mirjolet, Francisco Rivadulla, Premysl Marsik, Vladislav Borisov, Roser Valentí, and Josep Fontcuberta. Electron-phonon coupling and electron-phonon scatter- ing in srvo3. *Advanced Science*, 8(15):2004207, 2021.

56 Zhenwei Ou, Bin Peng, Weibin Chu, Zhe Li, Cheng Wang, Yan Zeng, Hongyi Chen, Qiuyu Wang, Guohua Dong, Yongyi Wu, Ruibin Qiu, Li Ma, Lili Zhang, Xiaoze Liu, Tao Li, Ting Yu, Zhongqiang Hu, Ti Wang, Ming Liu, and Hongxing Xu. Strong electron-phonon coupling mediates carrier transport in bifeo3. *Advanced Science*, 10(22):2301057, 2023.

57 Edoardo Baldini, Michael A. Sentef, Swagata Acharya, Thomas Brumme, Evgeniia Sheveleva, Fryderyk Lyzwa, Ekaterina Pomjakushina, Christian Bernhard, Mark van Schilfgaarde, Fabrizio Carbone, Angel Rubio, and Cédric Weber. Electron-phonon-driven three-dimensional metal- licity in an insulating cuprate. *Proceedings of the National Academy of Sciences*, 117(12):6409–6416, 2020.

58 Nitin Pratap Singh, Kusum Lata, and Linga Reddy Cenkeramaddi. Electron-phonon interactions and helmholtz free energy in confined systems: Advancing low-dimensional superconductors for quantum technolo- gies. *Results in Physics*, 73:108270, 2025.

59 Seher Karakuzu, Luca F. Tocchio, Sandro Sorella, and Federico Becca. Superconductivity, charge-density waves, antiferromagnetism, and phase separation in the hubbard- holstein model. *Phys. Rev. B*, 96:205145, Nov 2017.

60 Zhaoyu Han, Steven A. Kivelson, and Hong Yao. Strong coupling limit of the holstein-hubbard model. *Phys. Rev. Lett.*, 125:167001, Oct 2020.

61 W. Koller, D. Meyer, Y. Ōno, and A. C. Hewson. First- and second-order phase transitions in the holstein- hubbard model. *Europhysics Letters*, 66(4):559, may 2004.

62 W. Koller, D. Meyer, and A. C. Hewson. Dynamic re- sponse functions for the holstein-hubbard model. *Phys. Rev. B*, 70:155103, Oct 2004.

63 W. Koller, A. C. Hewson, and D. M. Edwards. Pola- ronic quasiparticles in a strongly correlated electron band. *Phys. Rev. Lett.*, 95:256401, Dec 2005.

64 Natanael C. Costa, Kazuhiro Seki, Seiji Yunoki, and Sandro Sorella. Phase diagram of the two-dimensional hubbard-holstein model. Communications Physics, 3(1):80, 2020.

65 E. A. Nowadnick, S. Johnston, B. Moritz, R. T. Scalet- tar, and T. P. Devereaux. Competition between antiferro- magnetic and charge-density-wave order in the half-filled hubbard-holstein model. Phys. Rev. Lett., 109:246404, Dec 2012.

66 S. Johnston, E. A. Nowadnick, Y. F. Kung, B. Moritz, R. T. Scalettar, and T. P. Devereaux. Determinant quan- tum monte carlo study of the two-dimensional single-band hubbard-holstein model. Phys. Rev. B, 87:235133, Jun 2013.

67 C. B. Mendl, E. A. Nowadnick, E. W. Huang, S. Johnston, B. Moritz, and T. P. Devereaux. Doping dependence of ordered phases and emergent quasiparticles in the doped hubbard-holstein model. Phys. Rev. B, 96:205141, Nov 2017.

68 Takahiro Ohgoe and Masatoshi Imada. Competition among superconducting, antiferromagnetic, and charge orders with intervention by phase separation in the 2d holstein-hubbard model. Phys. Rev. Lett., 119:197001, Nov 2017.

69 Z. B. Huang, W. Hanke, E. Arrigoni, and D. J. Scalapino. Electron-phonon vertex in the two-dimensional one-band hubbard model. Phys. Rev. B, 68:220507, Dec 2003.

70 A. Nocera, M. Soltanieh-ha, C. A. Perroni, V. Cataudella, and A. E. Feiguin. Interplay of charge, spin, and lat- tice degrees of freedom in the spectral properties of the one-dimensional hubbard-holstein model. Phys. Rev. B, 90:195134, Nov 2014.

71 Shaozhi Li, Yanfei Tang, Thomas A. Maier, and Steven Johnston. Phase competition in a one-dimensional three- orbital hubbard-holstein model. Phys. Rev. B, 97:195116, May 2018.

72 Bo Xiao, F. Hébert, G. Batrouni, and R. T. Scalettar. Competition between phase separation and spin density wave or charge density wave order: Role of long-range interactions. Phys. Rev. B, 99:205145, May 2019.

73 F. Hébert, Bo Xiao, V. G. Rousseau, R. T. Scalettar, and G. G. Batrouni. One-dimensional hubbard-holstein model with finite-range electron-phonon coupling. Phys. Rev. B, 99:075108, Feb 2019.

74 Ch Uma Lavanya, I. V. Sankar, and Ashok Chatterjee. Metallicity in a holstein-hubbard chain at half filling with gaussian anharmonicity. Scientific Reports, 7(1):3774, 2017.

75 Martin Hohenadler and Fakher F. Assaad. Excitation spectra and spin gap of the half-filled holstein-hubbard model. Phys. Rev. B, 87:075149, Feb 2013.

76 H. Matsueda, T. Tohyama, and S. Maekawa. Electron- phonon coupling and spin-charge separation in one- dimensional mott insulators. Phys. Rev. B, 74:241103, Dec 2006.

77 Wen-Qiang Ning, Hui Zhao, Chang-Qin Wu, and Hai- Qing Lin. Phonon effects on spin-charge separation in one dimension. Phys. Rev. Lett., 96:156402, Apr 2006.

78 Masaki Tezuka, Ryotaro Arita, and Hideo Aoki. Density- matrix renormalization group study of pairing when electron-electron and electron-phonon interactions coex- ist: Effect of the electronic band structure. Phys. Rev. Lett., 95:226401, Nov 2005.

79 Masaki Tezuka, Ryotaro Arita, and Hideo Aoki. Phase diagram for the one-dimensional hubbard-holstein model: A density-matrix renormalization group study. Phys. Rev. B, 76:155114, Oct 2007.

80 R. T. Clay and R. P. Hardikar. Intermediate phase of the one dimensional half-filled hubbard-holstein model. Phys. Rev. Lett., 95:096401, Aug 2005.

81 H. Fehske, G. Hager, and E. Jeckelmann. Metallicity in the half-filled holstein-hubbard model. Europhysics Let- ters, 84(5):57001, nov 2008.

82 Eduardo Fradkin and Jorge E. Hirsch. Phase diagram of one-dimensional electron-phonon systems. i. the su- schrieffer-heeger model. Phys. Rev. B, 27:1680-1697, Feb 1983.

83 Sanjeev Kumar and Jeroen van den Brink. Charge or- dering and magnetism in quarter-filled hubbard-holstein model. Phys. Rev. B, 78:155123, Oct 2008.

84 E. Berger, P. Valášek, and W. von der Linden. Two- dimensional hubbard-holstein model. Phys. Rev. B, 52:4806-4814, Aug 1995.

85 Takashi Hotta and Yasutami Takada. Effect of electron correlation on phonons in a strongly coupled electron- phonon system. Phys. Rev. B, 56:13916-13926, Dec 1997.

86 E. A. Nowadnick, S. Johnston, B. Moritz, and T. P. Dev- ereaux. Renormalization of spectra by phase competition in the half-filled hubbard-holstein model. Phys. Rev. B, 91:165127, Apr 2015.

87 N. Dupuis. Spin fluctuations and pseudogap in the two- dimensional half-filled hubbard model at weak coupling. Phys. Rev. B, 65:245118, Jun 2002.

88 Saurabh Pradhan and G. Venketeswara Pai. Holstein- hubbard model at half filling: A static auxiliary field study. Phys. Rev. B, 92:165124, Oct 2015.

89 Yao Wang, Ilya Esterlis, Tao Shi, J. Ignacio Cirac, and Eugene Demler. Zero-temperature phases of the two- dimensional hubbard-holstein model: A non-gaussian ex- act diagonalization study. Phys. Rev. Res., 2:043258, Nov 2020.

90 F. Marsiglio. Pairing in the holstein model in the dilute limit. Physica C: Superconductivity, 244(1):21-34, 1995.

91 Manuel Weber and Martin Hohenadler. Two-dimensional holstein-hubbard model: Critical temperature, ising uni- versality, and bipolaron liquid. Phys. Rev. B, 98:085405, Aug 2018.

92 Yuta Murakami, Philipp Werner, Naoto Tsuji, and Hideo Aoki. Ordered phases in the holstein-hubbard model: In- terplay of strong coulomb interaction and electron-phonon coupling. Phys. Rev. B, 88:125126, Sep 2013.

93 Johannes Bauer and Alex C. Hewson. Competition be- tween antiferromagnetic and charge order in the hubbard- holstein model. Phys. Rev. B, 81:235113, Jun 2010.

94 J. Bauer. Competing interactions and symmetry break- ing in the hubbard-holstein model. Europhysics Letters, 90(2):27002, may 2010.

95 Shohei Hayashida, Vignesh Sundaramurthy, Wenfeng Wu, Pascal Puphal, Thomas Keller, Björn Fåk, Masahiko Isobe, Bernhard Keimer, Karsten Held, Liang Si, and Matthias Hepting. Lattice dynamics of the infinite-layer nickelate lanio₂. Phys. Rev. B, 112:205104, Nov 2025.

96 E.F. Talantsev and V.V. Chistyakov. Debye temperature, electron-phonon coupling constant, and three-dome shape of crystalline strain as a function of pressure in highly compressed la3ni2o7-δ. Letters on Materials, 14(3):262-268, 2024.

97 Zhenfeng Ouyang, Miao Gao, and Zhong-Yi Lu. Absence

of electron-phonon coupling superconductivity in the bi- layer phase of la3ni2o7 under pressure. npj Quantum Ma- terials, 9(1):80, 2024.

98 Yang Zhang, Ling-Fang Lin, Adriana Moreo, Thomas A. Maier, and Elbio Dagotto. Structural phase transition, sâ±-wave pairing, and magnetic stripe order in bilayered superconductor la3ni2o7 under pressure. Nature Commu- nications, 15(1):2470, 2024.

99 J. L. García-Muñoz, M. A. G. Aranda, J. A. Alonso, and M. J. Martínez-Lope. Structure and charge order in the antiferromagnetic band-insulating phase of ndnio3. Phys. Rev. B, 79:134432, Apr 2009.

100 Steve Johnston, Anamitra Mukherjee, Ilya Elfimov, Mona Berciu, and George A. Sawatzky. Charge disproportion- ation without charge transfer in the rare-earth-element nickelates as a possible mechanism for the metal-insulator transition. Phys. Rev. Lett., 112:106404, Mar 2014.

101 J. A. Alonso, M. J. Martínez-Lope, M. T. Casais, J. L. García-Muñoz, and M. T. Fernández-Díaz. Room- temperature monoclinic distortion due to charge dispro- portionation in rnio3 perovskites with small rare-earth cations ($r=$ Ho, y, er, tm, yb, and lu): A neutron diffrac- tion study. Phys. Rev. B, 61:1756-1763, Jan 2000.

102 U. Staub, G. I. Meijer, F. Fauth, R. Allenspach, J. G. Bednorz, J. Karpinski, S. M. Kazakov, L. Paolasini, and F. d'Acapito. Direct observation of charge order in an epitaxial ndnio3 film. Phys. Rev. Lett., 88:126402, Mar 2002.

103 S. Kumar and P. Majumdar. A travelling cluster approx- imation for lattice fermions strongly coupled to classical degrees of freedom. The European Physical Journal B - Condensed Matter and Complex Systems, 50(4):571-579, 2006.

104 R. P. Hardikar and R. T. Clay. Phase diagram of the one- dimensional hubbard-holstein model at half and quarter filling. Phys. Rev. B, 75:245103, Jun 2007.

105 Sandip Halder, Sourav Chakraborty, and Kalpataru Prad- han. Layer-resolved magnetotransport properties in anti- ferromagnetic/paramagnetic superlattices: Proximity ef- fect induced antiferromagnetism in a paramagnetic metal. Phys. Rev. B, 110:195147, Nov 2024.

106 Sandip Halder, Sudip Mandal, and Kalpataru Pradhan. Microscopic study of interlayer magnetic coupling across the interface in antiferromagnetic bilayers. Phys. Rev. B, 111:125149, Mar 2025.

107 Nicholas Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller, and Edward Teller. Equa- tion of state calculations by fast computing machines. The Journal of Chemical Physics, 21(6):1087-1092, 06 1953.

108 Sandip Halder, Subrat K. Das, and Kalpataru Pradhan. Interfacial antiferromagnetic coupling driven magneto- transport properties in ferromagnetic superlattices. Phys. Rev. B, 108:235111, Dec 2023.

109 Soma Chatterjee, Sandip Halder, Kalipada Das, Kalpataru Pradhan, and I. Das. Magnetization reversal in nanocrystalline gd0.5sr0.5mno3. Phys. Rev. B, 110:155138, Oct 2024.

110 Sourav Chakraborty, Sandip Halder, and Kalpataru Prad- han. Itinerant ferromagnetism in a spin-fermion model for diluted spin systems. Phys. Rev. B, 108:165110, Oct 2023.

111 Gerald D. Mahan, editor. Many-Particle Physics. Springer New York, NY, 2012.

112 S. Kumar and P. Majumdar. Anti-localisation to strong localisation: The interplay of magnetic scattering and structural disorder. Europhysics Letters, 65(1):75, jan 2004.

113 Pavlo Bulanchuk. On the delta function broadening in the kubo-greenwood equation. Computer Physics Com- munications, 261:107714, 2021.

114 S. R. White, D. J. Scalapino, R. L. Sugar, E. Y. Loh, J. E. Gubernatis, and R. T. Scalettar. Numerical study of the two-dimensional hubbard model. Phys. Rev. B, 40:506-516, Jul 1989.

115 Rubem Mondaini and Thereza Paiva. Magnetism, trans- port, and thermodynamics in two-dimensional half-filled hubbard superlattices. Phys. Rev. B, 95:075142, Feb 2017.

116 Maykon V. Araújo, José P. de Lima, Sandro Sorella, and Natanael C. Costa. Two-dimensional $t-t'$ holstein model. Phys. Rev. B, 105:165103, Apr 2022.

117 J. C. Slater. Magnetic effects and the hartree-fock equa- tion. Phys. Rev., 82:538-541, May 1951.

118 G. Gruner, editor. Density Waves in Solids. Westview Press, 2000.

119 Eric Jeckelmann, Chunli Zhang, and Steven R. White. Metal-insulator transition in the one-dimensional holstein model at half filling. Phys. Rev. B, 60:7950-7955, Sep 1999.

120 Martin Hohenadler and Holger Fehske. Density waves in strongly correlated quantum chains. The European Phys- ical Journal B, 91(9):204, 2018.

121 Peter Prelovšek, Roland Zeyher, and Peter Horsch. Self- localization of composite spin-lattice polarons. Phys. Rev. Lett., 96:086402, Mar 2006.

122 A. Greco and A. Dobry. Stability of correlated electronic systems under the influence of the electron-phonon inter- action. Solid State Communications, 99(7):473-477, 1996.

123 G. Sangiovanni, M. Capone, C. Castellani, and M. Grilli. Electron-phonon interaction close to a mott transition. Phys. Rev. Lett., 94:026401, Jan 2005.

124 G. Sangiovanni, O. Gunnarsson, E. Koch, C. Castellani, and M. Capone. Electron-phonon interaction and antifer- romagnetic correlations. Phys. Rev. Lett., 97:046404, Jul 2006.

125 K. Borejsza and N. Dupuis. Antiferromagnetism and single-particle properties in the two-dimensional half-filled hubbard model: A nonlinear sigma model approach. Phys. Rev. B, 69:085119, Feb 2004.

126 K. Borejsza and N. Dupuis. Antiferromagnetism and single-particle properties in the two-dimensional half-filled hubbard model: Slater vs. mott-heisenberg. Europhysics Letters, 63(5):722, sep 2003.

127 Gun Sang Jeon, Tae-Ho Park, Jung Hoon Han, Hyun C. Lee, and Han-Yong Choi. Dynamical mean-field theory of the hubbard-holstein model at half filling: Zero temper- ature metal-insulator and insulator-insulator transitions. Phys. Rev. B, 70:125114, Sep 2004.

128 I. Esterlis, S. A. Kivelson, and D. J. Scalapino. Pseudogap crossover in the electron-phonon system. Phys. Rev. B, 99:174516, May 2019.

129 S. Ciuchi and F. de Pasquale. Charge-ordered state from weak to strong coupling. Phys. Rev. B, 59:5431-5440, Feb 1999.

130 Jinwoong Hwang, Wei Ruan, Yi Chen, Shujie Tang, Michael F Crommie, Zhi-Xun Shen, and Sung-Kwan Mo. Charge density waves in two-dimensional transition metal dichalcogenides. Reports on Progress in Physics, 87(4):044502, apr 2024.

$^{131}$ Yung-Ting Lee, Po-Tuan Chen, Zheng-Hong Li, Jyun-Yu Wu, Chia-Nung Kuo, Chin Shan Lue, Chien-Te Wu, Chien-Cheng Kuo, Cheng-Tien Chiang, Taisuke Ozaki, Chun-Liang Lin, Chi-Cheng Lee, Hung-Chung Hsueh, and Ming-Chiang Chung. Revealing the charge density wave caused by peierls instability in two-dimensional nbse2. *ACS Materials Letters*, 6(7):2941-2947, Jul 2024.

$^{132}$ N. D. Mermin and H. Wagner. Absence of ferromagnetism or antiferromagnetism in one- or two-dimensional isotropic heisenberg models. *Phys. Rev. Lett.*, 17:1133-1136, Nov 1966.

$^{133}$ P. C. Hohenberg. Existence of long-range order in one and two dimensions. *Phys. Rev.*, 158:383-386, Jun 1967.