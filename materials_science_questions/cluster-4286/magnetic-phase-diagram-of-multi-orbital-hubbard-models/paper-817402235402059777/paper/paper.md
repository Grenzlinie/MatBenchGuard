PHYSICAL REVIEW B 99, 205133 (2019)

# Metal-insulator transition in the two-dimensional Hubbard model:
Dual fermion approach with Lanczos exact diagonalization

Arata Tanaka
Department of Quantum Matter, ADSM, Hiroshima University, Higashi-hiroshima 739-8530, Japan

![](./images/817402235402059777_1.jpg)
(Received 11 December 2018; revised manuscript received 6 May 2019; published 20 May 2019)

In this study, the metal-insulator transition in the square-lattice Hubbard model at half-filling is revisited in relation to the DOS and spectral functions by means of the ladder dual fermion approximation (LDFA). For this purpose, a new expression of the two-body Green's function in the form of resolvents is proposed, which provides tractable and efficient means to calculate the local vertex function with the Lanczos exact diagonalization (ED) method. This makes it possible to use the Lanczos ED method as a solver of the effective impurity Anderson model for LDFA, opening up the way to access low temperatures for these perturbative extensions of the dynamical mean-field theory and to obtain accurate DOS and spectral functions on the real frequency axis by a new variant of the maximum entropy method. It is found that for $U \leqslant 3.5t$, as temperature decreases, the pseudogap formation due to antiferromagnetic correlations in the quasiparticle peak of the spectral function occurs at the $X$ point $[\boldsymbol{k}=(\pi, 0)]$, spreads through the Fermi surface and ends at the $M_{2}$ point $[\boldsymbol{k}=(\pi/2, \pi/2)]$. The almost simultaneous creation of the pseudogap and the loss of the Fermi liquid feature is consistent with that expected in the Slater regime. Although the pseudogap still appears in the quasi-particle-like single peak for $U \geqslant 4.0t$, the Fermi-liquid feature is partially lost on the Fermi surface already at higher temperatures as expected in the Mott-Heisenberg regime, in which local spins are preformed at high temperatures. A sharp crossover from a pseudogap phase to a Mott insulator at finite $U^{*} \approx 4.7t$ is found to occur below the temperature of the pseudogap formation similar to a previous study with the nonlinear $\sigma$ model approach.

DOI: 10.1103/PhysRevB.99.205133

## I. INTRODUCTION

Nowadays the dynamical mean-field theory (DMFT) [1] is one of the most powerful methods to describe electronic properties in strongly correlated electron systems. Although DMFT is exact in infinite dimension [2], spatial correlation effects, which are absence in DMFT similar to the ordinary mean-field theory, play crucial roles in finite dimensions in some fascinating cases, such as criticality due to thermal or quantum fluctuations, unconventional superconductors, and metal-insulator transitions (MIT) in low dimensions. In recent years, to include spatial correlations, numerous extensions of DMFT have been developed. In DMFT, the problem of electrons on the lattice is mapped to the effective impurity Anderson model (IAM), where the interaction is explicitly considered on one of the sites (the impurity site) and rest of the sites are replaced by an effective medium. In the cluster extensions of DMFT such as the cellular DMFT (CDMFT) or the dynamical cluster approximation (DCA) [3], the impurity site is replaced by a cluster and spatial correlations within the cluster are considered.

Other attempts to include spatial correlations are perturbative extensions of DMFT [4] and among of them, there is a class of methods in which the local vertex functions instead of the bare interaction are used as the diagrammatic elements of the perturbation. Those in this category are, for example, the pioneering work of Kusunose [5], the dynamical vertex approximation (D$\Gamma$A) [6], the dual fermion approximation (DFA) [7,8], the dual boson approximation (DBA) [9], the one-particle irreducible approach (1PI) [10], the DMFT to functional renormalization group approach (DMFT$^2$RG) [11], and the triply irreducible local expansion (TRILEX) [12].

To solve the effective IAM for DMFT, various numerical methods have been developed. In the perturbative extensions of DMFT mentioned above, the two-body Green's function of the effective IAM is further required to obtain the local four-point vertex function. Efficient schemes to calculate the two-body Green's function have already been developed and applied to DFA and D$\Gamma$A with the continuous-time quantum Monte Carlo (QMC) [13-16] and the ordinary exact diagonalization (ED) [6,17-20] methods. The QMC methods have difficulty in accuracy particularly in low temperatures because of the statical errors. On the other hand, for the ordinary ED technique, the method so far proposed is that with the Lehmann representation and as will be discussed later, it has problem in efficiency and the limitation of the number of the many-body basis functions.

One of the purposes of this paper is to present a new formula for the two-body Green's function. This renders efficient and accurate means to calculate the local vertex function and makes it possible to use the Lanczos ED technique [1,21] as a solver of the effective IAM required for DFA and similar perturbative extensions of DMFT.

The MIT in the two-dimensional (2D) Hubbard model at half filling still remains to be a subject of debate even after decades of extensive studies [22-31]. Although it is well established that the ground state of the half-filled 2D Hubbard

2469-9950/2019/99(20)/205133(22)
205133-1
©2019 American Physical Society

model on a square lattice has long-range antiferromagnetic (AFM) order [32,33], the difficulty mainly arises from the fact that long-range AFM order cannot be stable at finite temperatures in two dimension because of the Mermin-Wagner theorem [34]. The MIT has been discussed in relation to the Slater and Mott-Heisenberg mechanisms. In the Slater regime, the gap formation is essentially that of one-body picture, i.e., the Brillouin zone folding caused by the AFM ordering. Hence, the spin and charge degrees of freedom are entwined and both the spin and charge excitations have the same energy scale. In contrast, in the Mott-Heisenberg regime, localized spins preformed at high temperatures and AFM ordering occurs through the exchange coupling between these local spins. Since this picture is essentially based on many-body theories, the energy scale of the charge excitation $\approx U$ and the spin excitation $\approx 4t^{2}/U$ are generally different. In a study with the nonlinear $\sigma$ model approach [30,31], the pseudogap is formed at low temperatures. While a clear insulating gap opens in the Mott-Heisenberg regime, the DOS at the Fermi level remains finite for $T>0$ in the Slater regime and thus the MIT point $U_{\mathrm{c}}\approx4.2t$ is expected to be positioned at the boundary between these two regimes. On the other hand, Anderson has proposed that whole low-temperature physics of the 2D Hubbard model is mapped onto the 2D Heisenberg model and a Mott gap opens for all $U>0$ [26].

DMFT predicts the first-order Mott MIT at finite temperatures with a second-order critical endpoint $U_{\mathrm{c}}\approx10t$ at $T=0$ when the paramagnetic (PM) state is assumed [1], which is essentially the same to the MIT in infinite dimension. CDMFT [35,36], the variational cluster approximation (VCA) [37] and the second-order DFA [18,38], which are only capable for short-range spatial correlations within the cluster, also find the first-order MIT at finite temperatures similar to DMFT but with substantially smaller critical values $U_{\mathrm{c}}\approx6t$. In these theories, however, the AFM insulating state have finite Néel temperatures and the region where the first-order MIT line presence in the $U$-$T$ phase diagram is replaced by the AFM insulating phase when the solutions are not constrained to the PM state [36].

In the studies by means of D$\Gamma$A and extrapolated lattice QMC [37,39], the ladder dual fermion approximation (LDFA) [4], and the two-particle self-consistent approximation (TPSC) [24,25], which incorporate the effects of long-range correlations and fulfill the Mermin-Wagner theorem, the MIT occurs at much smaller $U$ compared to the CDMFT results. In the QMC calculations of finite-size clusters [40] has also found the pseudogap at least $U\geqslant2.0t$. Schëfer *et al.* suggest in their combined study of D$\Gamma$A and lattice QMC [37] that $U_{\mathrm{c}}=0$ for $T\rightarrow0$ and thus no MIT occurs at any $U>0$ similar to the 1D Hubbard model [41].

However, the formation of the pseudogap does not necessarily indicate insulating behavior in low temperatures and examination of subtle changes in states inside the gap as a function of temperature is required to verify whether $U_{\mathrm{c}}$ stays finite or $U_{\mathrm{c}}=0$ [31]. For this reason, it is essential to obtain precise information of the DOS and spectral function in the vicinity of the Fermi level to understand the MIT in the 2D Hubbard model. Although there are already several LDFA works [42–45] and that with the diagrammatic Mote Carlo approach [46,47] on the 2D Hubbard model at half filling, detailed investigation on the DOS and spectral function with LDFA at low temperatures is still lacking.

In addition to a new formula for the two-body Green’s function, the other purpose of this paper is to investigate the DOS and spectral function of the square-lattice Hubbard model at half filling by means of LDFA to elucidate the behavior and origin of the MIT. In particular, utilizing the newly developed Lanczos ED scheme to calculate the two-body Green’s function as the solver of the effective IAM for LDFA, it is possible to access large $U$ and low-temperature region of the $U$-$T$ phase diagram where previous studies still have not reached and obtain results with unprecedented accuracy. It is found that a sharp crossover from a pseudogap phase to a Mott insulator around $U^{*}\approx4.7t$ occurs below the temperature of the pseudogap formation.

The rest of this paper is structured as follows. In Sec. II, a short explanation on the $U$-$T$ phase diagram of the 2D Hubbard model obtained in this study is given. In Sec. III, the new formula of two-body Green’s function is presented. Section IV describes how to calculate the two-body Green’s function approximately with the Lanczos algorithm with the new formula. In Sec. V, a brief overview of LDFA is given and some technical points specific to the Lanczos ED method are presented. In Sec. VI, a detailed description of the maximum entropy method used in this study is given. In Sec. VII, results of LDFA calculations of the 2D Hubbard model are presented. The paper is closed with a discussion in Sec. VIII and a brief summary in Sec. IX. Derivations of the new formula in Sec. III and the update formula of the hybridization function in Sec. VII are deferred to Appendices A and B. The convergence of the vertex function of IAM with the Lanczos ED method is discussed in Appendix C and the DOS of the 2D Hubbard model inferred by the present and standard maximum entropy methods are compared in Appendix D.

## II. $U$-$T$ PHASE DIAGRAM OF THE 2D HUBBARD MODEL

Before embarking on rather lengthy explanation of the present computational scheme, here, we give a succinct account on the $U$-$T$ phase diagram of the 2D Hubbard model obtained in this study. Figure 1 shows $U$-$T$ phase diagram for the half-filled Hubbard model on a square lattice obtained with LDFA. As will be discussed in Sec. VII E, a metallic to pseudogap phase crossover is found to occur with decreasing temperature: the pseudogap is first formed in the quasiparticle peak of the spectral function at the $X$ point $\boldsymbol{k}=(\pi,0)$ (shown by the closed tip-up triangles) and the formation spreads through the Fermi surface and ends at the $M_{2}$ point $\boldsymbol{k}=(\pi/2,\pi/2)$ (closed tip-down triangles). The results are consistent with the previous D$\Gamma$A and lattice QMC study [37] (also indicated in Fig. 1).

However, the characteristic of the pseudogap formation changes depending on the size of $U$. For $U\leqslant3.5t$, the pseudogap formation and the loss of the Fermi-liquid feature occur simultaneously and below the temperature of the pseudogap formation at the $M_{2}$ point, the Fermi surface is totally lost and the system enters the pseudogap phase. These results for $U\leqslant3.5t$ are consistent with those expected in the Slater regime.

![](./images/817402235402059777_2.jpg)

FIG. 1. $U$-$T$ phase diagram for the half-filled Hubbard model on a square lattice obtained with LDFA. Temperatures where the double occupancy $D$ has the local maximum (closed diamonds), the pseudogap formation occur at the $X$ (closed tip-up triangles) and $M_2$ (closed tip-down triangles) points in the spectral function $A_k(\omega)$ and the DOS at the Fermi level is $\rho(\omega=0)=10^{-7}$ for $U\geqslant4.8t$ (closed circles) are shown. The vertical line at $U=4.7t$ is the crossover line from the pseudogap phase to the Mott insulator. For references, the DMFT Néel temperature $T_{\text{N}}^{\text{DMFT}}$ (crosses) in Ref. [44] and the pseudogap formation temperatures at the $X$ (open tip-up triangles) and $M_2$ (open tip-down triangles) points in the combined study of D$\Gamma$A and lattice QMC [39] are also presented.

On the other hand, for larger $U$, although the formation of the pseudogap still occurs in the quasi-particle-like single peak at the Fermi level accompanied by prominent shoulder structures at $\omega\approx\pm U/2$, the Fermi-liquid feature is partially lost around the $X$ point already at higher temperatures above the DMFT Néel temperature $T_{\text{N}}^{\text{DMFT}}$ for $U=4.0t$ and totally lost for $U\geqslant5.5t$. These results for $U\geqslant4.0t$ is consistent with those expected in the Mott-Heisenberg regime, in which local spins are preformed above the temperature where AFM correlations start to develop.

As will be discussed in Sec. VII D, a sharp crossover from the pseudogap phase to the Mott insulator around $U^*\approx4.7t$ is found to occur below the temperature of the pseudogap formation. For $U<U^*$, the DOS at the Fermi level is reduced with decreasing temperature but persists even at low temperatures. In contrast, for $U>U^*$, the reduction is much rapid and clear gap opening occurs at certain temperature. The value of $U^*\approx4.7t$ coincides with the boundary between the Slater and Mott-Heisenberg regimes defined by the inflection point of the double occupancy $D$ curve as a function of $U$ as will be discussed in Sec. VII B. These low-energy behavior of DOS in the vicinity of the Fermi level is consistent with the previous study with the nonlinear $\sigma$ model approach [31].

### III. EXPRESSION OF TWO-BODY GREEN'S FUNCTION IN THE FORM OF RESOLVENTS

As an expression for two-body Green's function, the Lehmann representation has been used for the ordinary ED technique [6,17,18]. However, the structure of the formula is not suitable for the Lanczos exact diagonalization method. The expression has terms like

$$
\sum_{lmnk} \frac{(e^{-\beta E_l}/Z)\langle k|c_2|l\rangle\langle l|c_1|m\rangle\langle m|c_3^\dagger|n\rangle\langle n|c_4^\dagger|k\rangle}{(E_k-E_l+i\omega_1)(E_l-E_m+i\omega_2)(E_m-E_n-i\omega_3)}, \quad (1)
$$

where $|l\rangle$ and $E_l$ are the $l$th lowest eigenvalue and corresponding eigenvector of the Hamiltonian; $c_i^\dagger$ and $c_i$ represent creation and annihilation operators of an electron on the impurity site, respectively and index $i\,(i=1,2,3)$ of these operators and also those of $g_{12}$ and $\chi_{1234}$ later appeared in this section are shorthand notation of combined index for the spin $\sigma_i$ and orbital $o_i$ degree of freedom, e.g., $c_1\equiv c_{\sigma_1,o_1}$; $\omega_i$ denote the fermionic Matsubara frequency: $\omega_i=\pi(2n_i+1)/\beta$. Since these terms contain the factors in the denominator with the difference of two eigenvalues, e.g., $E_m-E_n$, terms with nearly degenerated two high-energy eigenvectors $E_m$ and $E_n$ can have large contribution [18]. Therefore the precise eigenvalues of whole energy range are necessary. Since the Lanczos ED is accurate only for low-energy eigenvectors, an alternative expression for the two-body Green's function is desired.

On the other hands, for the Fourier transform of the one-body Green's function $g_{12}(\tau)\equiv-\langle\mathcal{T}[c_1(\tau)c_2^\dagger(0)]\rangle$ the expression with resolvents

$$
\begin{aligned}
g_{12}(i\omega) &= \frac{1}{Z}\sum_{l,m} e^{-\beta E_l} \Bigg\{ \frac{\langle l|c_1|m\rangle\langle m|c_2^\dagger|l\rangle}{i\omega+E_l-E_m} \\
&\quad + \frac{\langle l|c_2^\dagger|m\rangle\langle m|c_1|l\rangle}{i\omega+E_m-E_l} \Bigg\} \tag{2} \\
&= \frac{1}{Z}\sum_{l} e^{-\beta E_l} \Bigg\{ \langle l|c_1\frac{1}{i\omega+E_l-\mathcal{H}}c_2^\dagger|l\rangle \\
&\quad - \langle l|c_2^\dagger\frac{1}{-i\omega+E_l-\mathcal{H}}c_1|l\rangle \Bigg\} \tag{3}
\end{aligned}
$$

is applicable to the Lanczos ED technique and has already adopted in the DMFT studies [1,48]. Since eigenvector $|l\rangle$ only within the energy range of the thermal excitation contribute due to the presence of the Boltzmann factor $e^{-\beta E_l}$, $|l\rangle$ and $E_l$ can be accurately calculated at low temperatures with the Lanczos ED technique. The resolvents in Eq. (3) can be transformed into continued fractions using the Lanczos algorithm and this continued fraction can be terminated typically several hundreds floors to obtain accurate results even for systems with $\sim10^7$ basis functions. This technique is called the recursion method [49]. The procedure is also equivalent to replacing $E_m$ and $|m\rangle$ in Eq. (2) by those approximately obtained within a subspace spanned by the Lanczos vectors, i.e., the Krylov subspace [21].

The expression of the Fourier transform of the two-body Green's function

$$
\chi_{1234}(\tau_1,\tau_2;\tau_3,\tau_4)\equiv\langle\mathcal{T}[c_1(\tau_1)c_2(\tau_2)c_3^\dagger(\tau_3)c_4^\dagger(\tau_4)]\rangle, \quad (4)
$$

presented here consists of terms each of which has three or two resolvents in the form $1/(i\omega+E_l-\mathcal{H})$ and the factor $e^{-\beta E_l}$ sharing the same eigenvalue $E_l$. Because of this feature, only terms with $E_l$ within the energy range of the thermal

excitation contribute similar to Eq. (3) of the one-body Green's function. Therefore, unlike the Lehmann representation, the denominators of these terms are always large with the high-energy eigenvectors of $\mathcal{H}$ and thus no significant contribution of high-energy eigenvectors is expected. This makes it possible to approximate the eigenvectors of $\mathcal{H}$ by those calculated within the Krylov subspace constructed by the Lanczos algorithm, which is less accurate in high-energy eigenvectors.

The detailed derivation of the expression is in Appendix A. The expression can be separated into three components in terms of the similarity to the three scattering channels: those of the horizontal $\chi^{\text{ph}}$ and vertical $\chi^{\underline{\text{ph}}}$ particle-hole, and the particle-particle $\chi^{\text{pp}}$ types:

$$
\chi_{1234}=\chi_{1234}^{\text{ph}}+\chi_{1234}^{\underline{\text{ph}}}+\chi_{1234}^{\text{pp}}. \tag{5}
$$

Each of the components can be given as

$$
\begin{aligned}
& \chi_{1234}^{\mathrm{ph}}\left(i \omega_{1}, i \omega_{2} ; i \omega_{3}, i \omega_{4}\right) \\
& \quad=-\frac{1}{Z} \sum_{l} e^{-\beta E_{l}}\left\langle l\left|\left(\left(c_{1} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{4}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{4}} \|\left(c_{2} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{3}}-\left(c_{3}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{2}}\right)_{E_{l}-i\left(\omega_{2}-\omega_{3}\right)}\right| l\right\rangle \\
& \quad-\frac{1}{Z} \sum_{l} e^{-\beta E_{l}}\left\langle l\left|\left(\left(c_{2} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{3}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{3}} \|\left(c_{1} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{4}}-\left(c_{4}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{1}}\right)_{E_{l}+i\left(\omega_{2}-\omega_{3}\right)}\right| l\right\rangle \\
& \quad+\frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{4}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{4}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{2} \Delta c_{3}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{3}^{\dagger} \Delta c_{2}\right)_{E_{l}-i \omega_{3}}\right]\right| l\right\rangle \\
& \quad+\frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \Delta c_{4}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{4}^{\dagger} \Delta c_{1}\right)_{E_{l}-i \omega_{4}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{2} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{3}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{3}}\right]\right| l\right\rangle \\
& \quad+\beta \delta_{\omega_{1}, \omega_{4}} \frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{4}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{1}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{2} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{3}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{2}}\right]\right| l\right\rangle,
\end{aligned} \tag{6}
$$

$$
\begin{aligned}
& \chi_{1234}^{\mathrm{ph}}\left(i \omega_{1}, i \omega_{2} ; i \omega_{3}, i \omega_{4}\right) \\
& \quad=+\frac{1}{Z} \sum_{l} e^{-\beta E_{l}}\left\langle l\left|\left(\left(c_{1} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{3}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{3}} \|\left(c_{2} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{4}}-\left(c_{4}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{2}}\right)_{E_{l}+i\left(\omega_{1}-\omega_{3}\right)}\right| l\right\rangle \\
& \quad+\frac{1}{Z} \sum_{l} e^{-\beta E_{l}}\left\langle l\left|\left(\left(c_{2} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{4}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{4}} \|\left(c_{1} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{3}}-\left(c_{3}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{1}}\right)_{E_{l}-i\left(\omega_{1}-\omega_{3}\right)}\right| l\right\rangle \\
& \quad-\frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{3}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{3}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{2} \Delta c_{4}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{4}^{\dagger} \Delta c_{2}\right)_{E_{l}-i \omega_{4}}\right]\right| l\right\rangle \\
& \quad-\frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \Delta c_{3}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{3}^{\dagger} \Delta c_{1}\right)_{E_{l}-i \omega_{3}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{2} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{4}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{4}}\right]\right| l\right\rangle \\
& \quad-\beta \delta_{\omega_{1}, \omega_{3}} \frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{1}}-\left(c_{3}^{\dagger} \| c_{1}\right)_{E_{l}-i \omega_{1}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{2} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{2}}-\left(c_{4}^{\dagger} \| c_{2}\right)_{E_{l}-i \omega_{2}}\right]\right| l\right\rangle,
\end{aligned} \tag{7}
$$

$$
\begin{aligned}
& \chi_{1234}^{\mathrm{pp}}\left(i \omega_{1}, i \omega_{2} ; i \omega_{3}, i \omega_{4}\right) \\
& \quad=-\frac{1}{Z} \sum_{l} e^{-\beta E_{l}}\left\langle l\left|\left(\left(c_{1} \| c_{2}\right)_{E_{l}+i \omega_{1}}-\left(c_{2} \| c_{1}\right)_{E_{l}+i \omega_{2}} \|\left(c_{3}^{\dagger} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{4}}-\left(c_{4}^{\dagger} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{3}}\right)_{E_{l}+i\left(\omega_{1}+\omega_{2}\right)}\right| l\right\rangle \\
& \quad-\frac{1}{Z} \sum_{l} e^{-\beta E_{l}}\left\langle l\left|\left(\left(c_{3}^{\dagger} \| c_{4}^{\dagger}\right)_{E_{l}-i \omega_{3}}-\left(c_{4}^{\dagger} \| c_{3}^{\dagger}\right)_{E_{l}-i \omega_{4}} \|\left(c_{1} \| c_{2}\right)_{E_{l}-i \omega_{2}}-\left(c_{2} \| c_{1}\right)_{E_{l}-i \omega_{1}}\right)_{E_{l}-i\left(\omega_{1}+\omega_{2}\right)}\right| l\right\rangle \\
& \quad+\frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \| c_{2}\right)_{E_{l}+i \omega_{1}}-\left(c_{2} \| c_{1}\right)_{E_{l}+i \omega_{2}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{3}^{\dagger} \Delta c_{4}^{\dagger}\right)_{E_{l}-i \omega_{3}}-\left(c_{4}^{\dagger} \Delta c_{3}^{\dagger}\right)_{E_{l}-i \omega_{4}}\right]\right| l\right\rangle \\
& \quad+\frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \Delta c_{2}\right)_{E_{l}+i \omega_{1}}-\left(c_{2} \Delta c_{1}\right)_{E_{l}+i \omega_{2}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{3}^{\dagger} \| c_{4}^{\dagger}\right)_{E_{l}-i \omega_{3}}-\left(c_{4}^{\dagger} \| c_{3}^{\dagger}\right)_{E_{l}-i \omega_{4}}\right]\right| l\right\rangle \\
& \quad+\beta \delta_{\omega_{1},-\omega_{2}} \frac{1}{Z} \sum_{l, m} \delta_{E_{l}, E_{m}} e^{-\beta E_{l}}\left\langle l\left|\left[\left(c_{1} \| c_{2}\right)_{E_{l}+i \omega_{1}}-\left(c_{2} \| c_{1}\right)_{E_{l}-i \omega_{1}}\right]\right| m\right\rangle\left\langle m\left|\left[\left(c_{3}^{\dagger} \| c_{4}^{\dagger}\right)_{E_{l}-i \omega_{3}}-\left(c_{4}^{\dagger} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{3}}\right]\right| l\right\rangle,
\end{aligned} \tag{8}
$$


where the operators in the form of $(\mathcal{A} \| \mathcal{B})_{z}$ and $(\mathcal{A} \triangle \mathcal{B})_{\substack{z \\ z'}}$ are the abbreviations of those contain one and two resolvents, respectively, and are defined as

$$
(\mathcal{A} \| \mathcal{B})_{z} \equiv \mathcal{A} \frac{1}{z-\mathcal{H}^{\prime}} \mathcal{B},
\tag{9}
$$

$$
(\mathcal{A} \triangle \mathcal{B})_{\substack{z \\ z'}} \equiv \mathcal{A} \frac{1}{z-\mathcal{H}} \frac{1}{z'-\mathcal{H}} \mathcal{B}.
\tag{10}
$$

The resolvent with the Hamiltonian $\mathcal{H}'$ in the denominator of Eq. (9) is the same to that of $\mathcal{H}$ except that all the eigenvectors $|l\rangle$ whose eigenvalue $E_{l}$ are equal to the real part of $z$ are projected out as

$$
(\mathcal{A} \| \mathcal{B})_{z}=\sum_{l, E_{l} \neq \operatorname{Re} z} \mathcal{A}|l\rangle \frac{1}{z-E_{l}}\langle l| \mathcal{B}.
\tag{11}
$$

The first two lines of the right-hand side of each of Eqs. (6)-(8) contain eight terms with three resolvents such as

$$
\begin{aligned}
& -\sum_{l} \frac{e^{-\beta E_{l}}}{Z}\left\langle l\left|\left(\left(c_{1} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{1}} \|\left(c_{2} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{3}}\right)_{E_{l}-i\left(\omega_{2}-\omega_{3}\right)}\right| l\right\rangle \\
& \quad=-\sum_{l} \frac{e^{-\beta E_{l}}}{Z}\langle l| c_{1} \frac{1}{i \omega_{1}+E_{l}-\mathcal{H}^{\prime}} c_{4}^{\dagger} \frac{1}{i\left(\omega_{3}-\omega_{2}\right)+E_{l}-\mathcal{H}^{\prime}} c_{2} \frac{1}{i \omega_{3}+E_{l}-\mathcal{H}} c_{3}^{\dagger}|l\rangle.
\end{aligned}
\tag{12}
$$

In total 4! (=24) of terms of this kind exist and we call them the major terms. Each term contains a resolvent with a bosonic Matsubara frequency, e.g., that with $i(\omega_{3}-\omega_{2})$ in Eq. (12), and for this resolvent, eigenvectors with eigenvalue $E_{l}$ are projected out to avoid divergence at zero frequency. The proper treatment of these special cases further requires 36 counter terms (for details, see Appendix A) and there are two kinds of them: one is those consist of products of two factors containing one and two resolvents as

$$
\begin{aligned}
& \sum_{\substack{l, m \\
E_{l}=E_{m}}} \frac{e^{-\beta E_{l}}}{Z}\left\langle l\left|\left(c_{1} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{1}}\right| m\right\rangle\left\langle m\left|\left(c_{2} \triangle c_{3}^{\dagger}\right)_{\substack{E_{l}+i \omega_{2} \\
E_{l}+i \omega_{3}}}\right| l\right\rangle \\
& \quad=\sum_{\substack{l, m \\
E_{l}=E_{m}}} \frac{e^{-\beta E_{l}}}{Z}\langle l| c_{1} \frac{1}{i \omega_{1}+E_{l}-\mathcal{H}} c_{4}^{\dagger}|m\rangle\langle m| c_{2} \frac{1}{i \omega_{2}+E_{l}-\mathcal{H}} \frac{1}{i \omega_{3}+E_{l}-\mathcal{H}} c_{3}^{\dagger}|l\rangle,
\end{aligned}
\tag{13}
$$

and the other kind of the counter terms have the form

$$
\begin{aligned}
& \beta \delta_{\omega_{1}, \omega_{4}} \sum_{\substack{l, m \\
E_{l}=E_{m}}} \frac{e^{-\beta E_{l}}}{Z}\left\langle l\left|\left(c_{1} \| c_{4}^{\dagger}\right)_{E_{l}+i \omega_{1}}\right| m\right\rangle\left\langle m\left|\left(c_{2} \| c_{3}^{\dagger}\right)_{E_{l}+i \omega_{2}}\right| l\right\rangle \\
& \quad=\beta \delta_{\omega_{1}, \omega_{4}} \sum_{\substack{l, m \\
E_{l}=E_{m}}} \frac{e^{-\beta E_{l}}}{Z}\langle l| c_{1} \frac{1}{i \omega_{1}+E_{l}-\mathcal{H}} c_{4}^{\dagger}|m\rangle\langle m| c_{2} \frac{1}{i \omega_{2}+E_{l}-\mathcal{H}} c_{3}^{\dagger}|l\rangle.
\end{aligned}
\tag{14}
$$

Note that if the eigenenergies of wave functions with different electron numbers are degenerated, the counter terms in Eq. (8) can have nonzero values even without finite superconducting order parameter. This can happen if the system possesses the electron-hole symmetry, e.g., half-filled square-lattice Hubbard model with the nearest-neighbor hopping in this study.

## IV. APPROXIMATION OF TWO-BODY GREEN'S FUNCTION WITH LANCZOS ALGORITHM

Having the new expression in hand, in this section, we discuss how to calculate the two-body Green's function approximately with the Lanczos algorithm [21]. The Lanczos algorithm is a unitary transformation, which converts a symmetric or Hermitian matrix $\mathcal{H}$ into a tridiagonal form:

$$
T^{(n)}=\left(\begin{array}{ccccc}
a_{1} & b_{1} & 0 & \cdots & 0 \\
b_{1} & a_{2} & b_{2} & \ddots & \vdots \\
0 & b_{2} & a_{3} & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & b_{n-1} \\
0 & \cdots & 0 & b_{n-1} & a_{n}
\end{array}\right).
\tag{15}
$$

Starting from a properly chosen initial vector $|v_{1}\rangle$, it creates one of the orthonormal basis vector $|v_{n}\rangle$ in every iteration step, and at $n$th step these basis vectors span the Krylov subspace $\mathcal{K}^{n}(|v_{1}\rangle, \mathcal{H})=\operatorname{span}\{|v_{1}\rangle, \mathcal{H}|v_{1}\rangle, \mathcal{H}^{2}|v_{1}\rangle, \ldots, \mathcal{H}^{n-1}|v_{1}\rangle\}$. In practice, because of round off error, the orthogonality of the

vectors $|v_n\rangle$ breaks midway through the iteration. This occurs as soon as the lowest eigenvector converges and one may set the criterion to terminate the iteration when this convergence is reached:

$$
\left|b_{n-1} s_{1, n}\right|<\varepsilon_{\text {lan }},\qquad(16)
$$

where $s_{i, j}$ is the $j$th component of the eigenvector of $T^{(n)}$ with the $i$th lowest eigenvalue $\theta_i$, i.e., $T^{(n)}\left|s_i\right\rangle=\theta_i\left|s_i\right\rangle$. In this study, the threshold $\varepsilon_{\text {lan }}=\alpha_{\text {lan }} \sqrt{N_{\text {sys }}} \varepsilon$ is assumed, where $N_{\text {sys }}$ is the order of matrix $\mathcal{H}$, $\varepsilon$ denotes the machine accuracy $\varepsilon=10^{-15}$ and $\alpha_{\text {lan }}=10$. The $i$th lowest eigenvalue $E_i$ and corresponding eigenvector $|i\rangle$ of $\mathcal{H}$ can be approximated as

$$
|i\rangle \approx \sum_{j=1}^{n} s_{i, j}\left|v_{j}\right\rangle, \quad E_{i} \approx \theta_{i}.
$$

High accuracy (typically more than 10 digits) can be expected for the eigenvector $|1\rangle$ of the lowest eigenvalue $E_1$ and the rest of them are less accurate.

Now, let us consider the major term with the form

$$
\begin{aligned}
& \sum_{l} \frac{e^{-\beta E_{l}}}{Z}\langle l| \mathcal{O}_{1} \frac{1}{i \omega+E_{l}-\mathcal{H}} \mathcal{O}_{2} \\
& \quad \times \frac{1}{i v+E_{l}-\mathcal{H}^{\prime}} \mathcal{O}_{3} \frac{1}{i \omega^{\prime}+E_{l}-\mathcal{H}} \mathcal{O}_{4}|l\rangle,\qquad(17)
\end{aligned}
$$

where each $\mathcal{O}_{i}(i=1,2,3,4)$ is one of $c_{1}, c_{2}, c_{3}^{\dagger}$, or $c_{4}^{\dagger}$ and $v$ is the bosonic and $\omega$, and $\omega^{\prime}$ are the fermionic Matsubara frequencies. The eigenvectors $|l\rangle$ need to be included in the calculations are limited to those of low energies by the Boltzmann factor $e^{-\beta E_{l}}$. Note that high accuracy is particularly needed for $E_l$ and $|l\rangle$ since it affects later calculations. Therefore, instead of calculating all the $E_l$ and $|l\rangle$ required at a time by the Lanczos algorithm describe above, it is preferable to use the so called restart Lanczos method [21], where only one lowest eigenvector is calculated at a time and repeat the same Lanczos procedure except in each step $|v_n\rangle$ is orthogonalized to all the previously obtained eigenvectors. In this way, all the required $E_l$ and $|l\rangle$ can be calculated with high precision.

One of the three resolvents in Eq. (17) on the left can be obtained approximately using $N_{\mathrm{L}}$ eigenvalues $E_{m}^{\mathrm{L}}$ and eigenvectors $\left|m^{\mathrm{L}}\right\rangle$ generated by combined use of the restart Lanczos method for low lying eigenvectors within the reach of the thermal excitation and the ordinary Lanczos method with the initial vector $\mathcal{O}_{1}^{\dagger}|l\rangle$ for rest of high-energy eigenvectors as

$$
\frac{1}{i \omega+E_{l}-\mathcal{H}} \approx \sum_{m=1}^{N_{\mathrm{L}}}\left|m^{\mathrm{L}}\right\rangle \frac{1}{i \omega+E_{l}-E_{m}^{\mathrm{L}}}\left\langle m^{\mathrm{L}}\right|.\qquad(18)
$$

The same can be done for the resolvent on the right using $N_{\mathrm{R}}$ eigenvalues $E_{m}^{\mathrm{R}}$ and eigenvectors $\left|m^{\mathrm{R}}\right\rangle$ generated by these Lanczos methods with the initial vector $\mathcal{O}_{4}|l\rangle$. Although the high-energy eigenvectors obtained with the ordinary Lanczos method are less accurate compared to the low-energy eigenvectors calculated with the restart Lanczos method, the resultant left and right resolvents have proper asymptotic behavior. For instance,

$$
\frac{1}{z-\mathcal{H}} \mathcal{O}_{4}|l\rangle=\sum_{n=0}^{\infty} \frac{1}{z^{n+1}} \mathcal{H}^{n} \mathcal{O}_{4}|l\rangle\qquad(19)
$$

for the right resolvent. Obviously the expansion is correct up to the $N_{\mathrm{R}}$ th order, since their coefficients belong to the Krylov space $\mathcal{K}^{N_{\mathrm{R}}}\left(\mathcal{O}_{4}|l\rangle, \mathcal{H}\right)$.

For the resolvent in the center, excitations through the left and right resolvents with different energy scales are required to be considered. To do so, vectors which represent excitation at the left $\left|v_{\alpha}^{L}\right\rangle$ and right $\left|v_{\alpha}^{R}\right\rangle$ resolvents with the energy $\Omega_{\alpha}$ and an artificial lifetime width $\gamma_{\alpha}$ are introduced as

$$
\begin{aligned}
\left|v_{\alpha}^{\mathrm{L}}\right\rangle & =\sum_{m=1}^{N_{\mathrm{L}}} \mathcal{O}_{2}^{\dagger}\left|m^{\mathrm{L}}\right\rangle \frac{\left\langle m^{\mathrm{L}}\left|\mathcal{O}_{1}^{\dagger}\right| l\right\rangle}{\left(\Omega_{\alpha}+E_{l}-E_{m}^{\mathrm{L}}\right)^{2}+\gamma_{\alpha}^{2}}, \\
\left|v_{\alpha}^{\mathrm{R}}\right\rangle & =\sum_{m=1}^{N_{\mathrm{R}}} \mathcal{O}_{3}\left|m^{\mathrm{R}}\right\rangle \frac{\left\langle m^{\mathrm{R}}\left|\mathcal{O}_{4}\right| l\right\rangle}{\left(\Omega_{\alpha}+E_{l}-E_{m}^{\mathrm{R}}\right)^{2}+\gamma_{\alpha}^{2}}.
\end{aligned}\qquad(20)
$$

We use these vectors with a finite number of reference energy points $\Omega_{\alpha}\left(\alpha=1,2, \ldots, N_{\alpha}\right)$ as the initial vectors of the band Lanczos method [21], which is an extension of the Lanczos method with multiple initial vectors, to generate the basis set to construct approximated resolvent. The Lanczos vectors need to be orthogonalized to the eigenvector $|l\rangle$ and, if exist, all the degenerated eigenvectors with the eigenvalue $E_l$ [see Eq. (11)]. It is, however, recommendable to calculate the low-energy eigenvectors within the reach of the thermal excitation by the restart Lanczos method and use the band Lanczos method to generate high-energy eigenvectors by orthogonalizing its initial and Lanczos vectors to the former. It is essential to choose one of $\Omega_{\alpha}$ to be $\Omega_{\alpha} \gg E_{\max }-E_{l}$ to make $\chi_{1234}$ have proper asymptotic behavior, where $E_{\max }$ is the maximum eigenvalue of $\mathcal{H}$.

As demonstrated in Appendix C, the resultant $\chi_{1234}$ (or the vertex function) converges rapidly as the number of the reference energy points $\Omega_{\alpha}$ increases. In the calculations of the 2D Hubbard model in this study, we adopted four reference energy points $\Omega_{1}=0, \Omega_{2}=0.02 W, \Omega_{3}=0.04 W$, and $\Omega_{4}=4 W$ with all $\gamma_{\alpha}=0.1 W$, where the effective band width $W$ is defined as

$$
W \equiv \sqrt{U^{2}+64 t^{2}}.\qquad(21)
$$

To further reduce the burden of the computational tasks, the initial vectors $\left|v_{\alpha}^{L}\right\rangle$ and $\left|v_{\alpha}^{R}\right\rangle$ of the four major terms in each of the first two lines on the right side of Eqs. (6)-(8) can be combined (they are not necessarily linearly independent and the number of required initial vectors is smaller than it appears) and the basis set generated by the band Lanczos method with the combined initial vectors can be shared in the calculation of these four major terms.

Once $N_{\mathrm{C}}$ eigenvalues $E_{n}^{\mathrm{C}}$ and eigenvectors $\left|n^{\mathrm{C}}\right\rangle$ are obtained with the band Lanczos method, we can approximate the major term in the form of Eq. (17) as

$$
\begin{aligned}
& \frac{1}{Z} \sum_{l=1}^{N_{l}} \sum_{m=1}^{N_{\mathrm{L}}} \sum_{n=1}^{N_{\mathrm{C}}} \sum_{m^{\prime}=1}^{N_{\mathrm{R}}} e^{-\beta E_{l}} \\
& \quad \times \frac{\left\langle l\left|\mathcal{O}_{1}\right| m^{\mathrm{L}}\right\rangle\left\langle m^{\mathrm{L}}\left|\mathcal{O}_{2}\right| n^{\mathrm{C}}\right\rangle\left\langle n^{\mathrm{C}}\left|\mathcal{O}_{3}\right| m^{\prime \mathrm{R}}\right\rangle\left\langle m^{\prime \mathrm{R}}\left|\mathcal{O}_{4}\right| l\right\rangle}{\left(i \omega+E_{l}-E_{m}^{\mathrm{L}}\right)\left(i v+E_{l}-E_{n}^{\mathrm{C}}\right)\left(i \omega^{\prime}+E_{l}-E_{m^{\prime}}^{\mathrm{R}}\right)},(22)
\end{aligned}
$$

which bears a resemblance to Eq. (1) but all the three factors in the denominator and $e^{-\beta E_{l}}$ shares the same $E_{l}$. This makes terms with all the eigenvalues $E_{l}, E_{m}^{\mathrm{L}}, E_{n}^{\mathrm{C}}$, and $E_{m^{\prime}}^{\mathrm{R}}$

being within the energy range of thermal excitation mostly contribute and for these terms, one can use the restart Lanczos method to obtain accurate eigenvectors and eigenvalues. For the rest of terms with high-energy excitations, the combined use of the ordinary and band Lanczos methods as described ensures accurate asymptotic behavior. Since the typical number of the Lanczos vectors, $N_{\rm L}$, $N_{\rm C}$, and $N_{\rm R}$, is several hundreds even for $10^6$ actual basis functions, the method proposed here renders drastic reduction of computational workload over ordinary ED method.

The counter terms, such as Eqs. (13) and (14) can be calculated in the similar way. For instance, the second factor with two resolvents in Eq. (13) can be approximated using $N_{\rm R}$ eigenvalues $E_n^{\rm R}$ and eigenvectors $|n^{\rm R}\rangle$ generated from the band Lanczos algorithm with the initial vectors $c_3^\dagger|l\rangle$ and $c_2^\dagger|m\rangle$ for all the degenerated eigenvectors $|l\rangle$ and $|m\rangle$ ($E_l = E_m$) as

$$
\sum_{n=1}^{N_{\rm R}} \frac{\langle m|c_2|n^{\rm R}\rangle\langle n^{\rm R}|c_3^\dagger|l\rangle}{\left(i\omega_2 + E_l - E_n^{\rm R}\right)\left(i\omega_3 + E_l - E_n^{\rm R}\right)}. \tag{23}
$$

### V. LADDER DUAL FERMION APPROXIMATION

In this section, a brief overview of LDFA [7,8,42] and some technical points specific to the present calculation scheme are provided. The action for the 2D Hubbard model on the square lattice with the nearest-neighbor hopping integral $t$ and the on-site Coulomb interaction $U$ is

$$
\begin{aligned}
S[\bar{c}, c] =& -\sum_{k\omega\sigma} \bar{c}_{k\omega\sigma}(i\omega + \mu - \varepsilon_k)c_{k\omega\sigma} \\
& + U \sum_i \int_0^\beta d\tau \bar{c}_{i\tau\uparrow}c_{i\tau\uparrow}\bar{c}_{i\tau\downarrow}c_{i\tau\downarrow}, \tag{24}
\end{aligned}
$$

where $\bar{c}_{k\omega\sigma}$ ($c_{k\omega\sigma}$) and $\bar{c}_{i\tau\sigma}$ ($c_{i\tau\sigma}$) are the fermionic Grassmann fields corresponding to the creation (annihilation) operators $c_{k\sigma}^\dagger$ ($c_{k\sigma}$) and $c_{i\sigma}^\dagger$ ($c_{i\sigma}$), respectively; $\omega$ represents the fermionic Matsubara frequency, $\mu$ denotes the chemical potential, and $\varepsilon_k = -2t(\cos k_x + \cos k_y)$.

The IAM at site $i$ can be written as

$$
\begin{aligned}
S_{\rm imp}[\bar{c}_i, c_i] =& -\sum_{\omega\sigma} \bar{c}_{i\omega\sigma}(i\omega + \mu - \Delta_\omega)c_{i\omega\sigma} \\
& + U \int_0^\beta d\tau \bar{c}_{i\tau\uparrow}c_{i\tau\uparrow}\bar{c}_{i\tau\downarrow}c_{i\tau\downarrow}, \tag{25}
\end{aligned}
$$

where $\Delta_\omega$ denotes the hybridization function, which is arbitrary at this point. The lattice action in Eq. (24) can be represented by the action of the IAM for each site $i$ plus a correction term:

$$
S[\bar{c}, c] = \sum_i S_{\rm imp}[\bar{c}_i, c_i] + \sum_{k\omega\sigma} \bar{c}_{k\omega\sigma}(\varepsilon_k - \Delta_\omega)c_{k\omega\sigma}. \tag{26}
$$

Instead of directly performing the perturbative calculations with Eq. (26), a new fermionic auxiliary field, which is called the dual fermion, $f_{k\omega\sigma}$ is introduced using a Hubbard-Stratonovich transformation [7,8]. The original action can be mapped onto that of the dual fermion by integrating out the real electron field $c_{k\omega\sigma}$. In this way, one can separate the problem of solving the IAM to obtain the local approximation and the perturbative corrections for the spatial correlations, avoiding the double counting of local contributions. The action of $f_{k\omega\sigma}$ within the fourth order is

$$
\begin{aligned}
S_d[\bar{f}, f] =& -\sum_{k\omega\sigma} \bar{f}_{k\omega\sigma}\left[G_{k\omega}^{d,0}\right]^{-1} f_{k\omega\sigma} \\
& - \frac{1}{4} \sum_{\substack{1234 \\ i}} \gamma_{1234}^{(4)} \bar{f}_{i1} \bar{f}_{i2} f_{i3} f_{i4}, \tag{27}
\end{aligned}
$$

where shorthand notations such as $1 \equiv (\omega_1, \sigma_1)$ are used for the indices; $G_{k\omega}^{d,0}$ denotes noninteracting dual-fermion one-body Green's function, and $\gamma_{1234}^{(4)}$ represents the reducible four-point vertex function of the impurity site for original electrons and they are defined using the local one-body $g_\omega$ and two-body $\chi_{1234}$ Green's functions of the impurity site for original electrons as

$$
G_{k\omega}^{d,0} = -g_\omega + \left[g_\omega^{-1} + \Delta_\omega - \varepsilon_k\right]^{-1}, \tag{28}
$$

$$
\gamma_{1234}^{(4)} = g_1^{-1} g_2^{-1}\left[\chi_{1234} - \beta(\delta_{14}\delta_{23} - \delta_{13}\delta_{24})g_1g_2\right]g_3^{-1} g_4^{-1}. \tag{29}
$$

Note that diagrams containing the six-point vertex function give a negligible contribution [42]. For the sake of convenience, we use notation

$$
\gamma_{\omega\omega';\Omega}^{\sigma_1\sigma_2\sigma_3\sigma_4} \equiv \gamma_{(\omega,\sigma_1),(\omega'+\Omega,\sigma_2),(\omega',\sigma_3),(\omega+\Omega,\sigma_4)}^{(4)}. \tag{30}
$$

Since we are dealing with the PM state, the system has spin rotational symmetry and the vertex function can be diagonalized with respect to the spin indices and separated into the charge ($S=0$) and spin ($S=1$) components:

$$
\gamma_{\omega\omega';\Omega}^{(\rm ch)} = \gamma_{\omega\omega';\Omega}^{\uparrow\uparrow\uparrow\uparrow} + \gamma_{\omega\omega';\Omega}^{\downarrow\downarrow\downarrow\downarrow}, \tag{31}
$$

$$
\gamma_{\omega\omega';\Omega}^{(\rm sp)} = \gamma_{\omega\omega';\Omega}^{\uparrow\uparrow\uparrow\uparrow} - \gamma_{\omega\omega';\Omega}^{\downarrow\downarrow\downarrow\downarrow} = \gamma_{\omega\omega';\Omega}^{\uparrow\downarrow\uparrow\downarrow} = \gamma_{\omega\omega';\Omega}^{\downarrow\uparrow\downarrow\uparrow}. \tag{32}
$$

To include effects of long-range spin fluctuations, the ladder diagram of the particle-hole channel is taken into account, which is considered to be the dominant correction to DMFT for the spatial fluctuations in low temperatures at half filling. The Bethe-Salpeter equation of the dual fermion for the charge ($\alpha = {\rm ch}$) and spin ($\alpha = {\rm sp}$) components are

$$
\Gamma_{\omega\omega';q\Omega}^{(\alpha)} = \gamma_{\omega\omega';\Omega}^{(\alpha)} + \frac{1}{\beta} \sum_{\omega''} \gamma_{\omega\omega'';\Omega}^{(\alpha)} \chi_{q\omega''\Omega}^{d,0} \Gamma_{\omega''\omega';q\Omega}^{(\alpha)}, \tag{33}
$$

where

$$
\chi_{q\omega\Omega}^{d,0} = -\frac{1}{N} \sum_k G_{k\omega}^d G_{k+q,\omega+\Omega}^d. \tag{34}
$$

We define the effective interaction of each component $\alpha$ as

$$
\mathcal{V}_{\omega;q\Omega}^{(\alpha)} = \frac{1}{2\beta} \sum_{\omega'} \gamma_{\omega\omega';\Omega}^{(\alpha)} \chi_{q\omega'\Omega}^{d,0} \left(\Gamma_{\omega'\omega;q\Omega}^{(\alpha)} - \frac{1}{2}\gamma_{\omega'\omega;\Omega}^{(\alpha)}\right) \tag{35}
$$

and the self-energy for the dual fermion can be written as

$$
\begin{aligned}
\Sigma_{k\omega}^d =& \frac{-1}{\beta N} \sum_{q\omega'} \gamma_{\omega\omega';0}^{(\rm ch)} G_{q\omega'}^d \\
& + \frac{1}{\beta N} \sum_{q\Omega} \left(\mathcal{V}_{\omega;q\Omega}^{(\rm ch)} + 3\mathcal{V}_{\omega;q\Omega}^{(\rm sp)}\right) G_{k+q,\omega+\Omega}^d. \tag{36}
\end{aligned}
$$

The Green's function of the dual fermion is obtained from Dyson's equation

$$
\left[G_{k \omega}^{d}\right]^{-1}=\left[G_{k \omega}^{d, 0}\right]^{-1}-\Sigma_{k \omega}^{d}. \tag{37}
$$

The electron Green's function can be obtained from its dual counterpart as

$$
\begin{aligned}
G_{k \omega}= & {\left[\varepsilon_{k}-\Delta_{\omega}\right]^{-1} g_{\omega}^{-1} G_{k \omega}^{d} g_{\omega}^{-1}\left[\varepsilon_{k}-\Delta_{\omega}\right]^{-1} } \\
& -\left[\varepsilon_{k}-\Delta_{\omega}\right]^{-1}. \tag{38}
\end{aligned}
$$

There is also similar one-to-one correspondence between electrons and their dual counterparts for the higher-order correlation functions [8,50].

The local corrections can be efficiently included in the impurity problem with a proper choice of $\Delta_{\omega}$. For the purpose, the condition $\left\langle G_{k \omega}^{d}\right\rangle_{k}=0$, with which diagrams containing a local loop vanish, is commonly used, where $\langle\cdots\rangle_{k}=(1 / N) \sum_{k} \cdots$. This condition is reduced to the self-consistent condition of DMFT for the noninteracting dual fermions and therefore DMFT can be regarded as the lowest order in DFA [8]. The nonlocal corrections can be included in $\Sigma_{k \omega}^{d}$ by higher orders of dual fermion perturbation theory as already discussed.

In the calculations of the dual fermionic quantities in Eqs. (33)-(37), the frequency cutoff $-N_{\omega}+1 \leqslant n \leqslant N_{\omega}$ is set for the variables with the fermionic Matsubara frequency $\omega_{n}=(2 n-1) \pi / \beta$ and $|m| \leqslant 2 N_{\omega}-1$ for those with the bosonic Matsubara frequency $\Omega_{m}=2 m \pi / \beta$. Choosing $N_{\omega} \approx W \beta / \pi$ is found to be sufficient to obtain accurate results, where $W$ is the effective band width in Eq. (21).

In the ED method, the conduction band of the effective IAM is replaced by discretized $N_{\mathrm{b}}$ energy levels (or bath sites) $l$ with energy $\varepsilon_{l}^{\mathrm{b}}$ and hybridization strength $V_{l}$ to the impurity orbital. The Hamiltonian can be written as

$$
\mathcal{H}_{\mathrm{imp}}=\sum_{l \sigma}\left\{\varepsilon_{l}^{\mathrm{b}} a_{l \sigma}^{\dagger} a_{l \sigma}+V_{l}\left(a_{l \sigma}^{\dagger} c_{\sigma}+\text { H.c. }\right)\right\}+U n_{\uparrow} n_{\downarrow}, \quad(39)
$$

where $c_{\sigma}^{\dagger}\left(c_{\sigma}\right)$ and $a_{l \sigma}^{\dagger}\left(a_{l \sigma}\right)$ are the creation (annihilation) operators of an electron on the impurity site and bath site $l$, respectively, and $n_{\sigma} \equiv c_{\sigma}^{\dagger} c_{\sigma}$. All the effects of the lattice and interaction except for the impurity site are encoded in the parameter set $\left\{\varepsilon_{l}^{\mathrm{b}}, V_{l}\right\}$ or the hybridization function

$$
\Delta\left(z ;\left\{\varepsilon_{l}^{\mathrm{b}}, V_{l}\right\}\right)=\sum_{l=1}^{N_{\mathrm{b}}} \frac{\left|V_{l}\right|^{2}}{z-\varepsilon_{l}^{\mathrm{b}}}. \tag{40}
$$

The outline of the computational procedure of LDFA is as follows. The one-body Green's function $g_{\omega}$ at the impurity site can be obtained by the Lanczos ED method utilizing Eq. (3). The two-body Green's function $\chi_{1234}$ at the impurity site can be calculated using Eqs. (4)-(8) and the prescription in Sec. IV. Once $g_{\omega}$ and $\chi_{1234}$ are obtained, the self-energy $\Sigma_{k \omega}^{d}$ and Green's function $G_{k \omega}^{d}$ of the dual fermion are calculated within the ladder approximation in the particle-hole channel using Eqs. (28)-(37). $\Sigma_{k \omega}^{d}$ and $G_{k \omega}^{d}$ must be calculated iteratively until self-consistency is reached in the same manner to the fluctuation exchange approximation [51] (the inner loop in Fig. 2). More technical details can be found in Refs. [18,44]. The modified Broyden's method is applied to accelerate the convergence of the self-consistency loop of $\Sigma_{k \omega}^{d}$ [52].

![](./images/817402235402059777_3.jpg)

FIG. 2. Illustration of the computational procedure of LDFA.

We further require the parameter set $\left\{\varepsilon_{l}^{\mathrm{b}}, V_{l}\right\}$ of the effective IAM to fulfill the condition $\left\langle G_{k \omega}^{d}\right\rangle_{k}=0$. To this end, we first choose the initial guess of the parameter set $\left\{\varepsilon_{l}^{\mathrm{b}}, V_{l}\right\}$, e.g., that of DMFT, and calculate $G_{k \omega}^{d}$. We update the parameter set,calculate $G_{k \omega}^{d}$ again and repeat this procedure until $\left\langle G_{k \omega}^{d}\right\rangle_{k}=0$ is fulfilled (the outer loop in Fig. 2).

For the update of the hybridization function, we use

$$
\Delta_{\omega}^{\text {new }}=\left\langle G_{k \omega}^{d}\left[G_{k \omega}^{d, 0}\right]^{-1} g_{k \omega}\right\rangle_{k}^{-1}\left\langle G_{k \omega}^{d}\left[G_{k \omega}^{d, 0}\right]^{-1} g_{k \omega} \varepsilon_{k}\right\rangle_{k}. \tag{41}
$$

The detailed derivation of Eq. (41) can be found in Ap-pendix B. Once the new hybridization function is obtained, the parameter set $\left\{\varepsilon_{l}^{\mathrm{b}}, V_{l}\right\}$ for the next iteration is determined by minimizing the distant function defined as

$$
d=\sum_{p=1}^{2 N_{\omega}} \frac{1}{\left|z_{p}\right|}\left|\Delta^{\mathrm{new}}\left(z_{p}\right)-\Delta\left(z_{p} ;\left\{\varepsilon_{l}^{\mathrm{b}}, V_{l}\right\}\right)\right|^{2}, \tag{42}
$$

where the set of $2 N_{\omega}$ points $\left\{z_{p}\right\}$ on the complex plane with $\operatorname{Im} z_{p}>0$ consists of $N_{\omega}$ points on the imaginary axis at the fermionic Matsubara frequencies and $N_{\omega}$ equally spaced points on a circle with the radius $R=\pi\left(2 N_{\omega}+5\right) / \beta$. This choice of data points alleviates the problems in the accuracy of the results and the stability of the convergence encountered in the above mentioned iteration process. The similar technique is also used in the analytic continuation with MEM in Sec. VI. To find the optimal solution of the parameter set $\left\{\varepsilon_{l}^{\mathrm{b}}, V_{l}\right\}$ is not a straightforward task because of the presence of numerous solutions with nearly the same distance. A genetic algorithm is applied in combination with the conjugate gradient method to improve the slow convergence of the solution.

## VI. MAXIMUM ENTROPY METHOD

Since the perturbative calculations are performed with the Matsubara frequency in the present formalism for LDFA, the analytic continuation is required to convert the results as functions of the real frequency. For the spectral function $A(\omega) \equiv-(1 / \pi) \operatorname{Im} G(\omega)$, the relation to the Green's function at an arbitrary complex number $z$

$$
G(z)=\int_{-\infty}^{\infty} \frac{1}{z-\omega} A(\omega) d \omega \tag{43}
$$

can be utilized. If a set of $N_{G}$ data of the Green's function $\boldsymbol{G} \equiv\left(G\left(z_{1}\right), G\left(z_{2}\right), \cdots\right)$ is given as input, one may obtain approximately a set of $N_{A}$ discretized data of spectral function

$\boldsymbol{A} \equiv (A(\omega_1)\Delta\omega, A(\omega_2)\Delta\omega, \cdots)$ by solving the linear equation
$$\boldsymbol{G} = K\boldsymbol{A}, \tag{44}$$
where $K$ denotes the $N_G \times N_A$ matrix with $K_{ij} \equiv 1/(z_i - \omega_j)$.
Solving Eq. (44) is known to be severely ill-posed problem
and the effective number of constraints imposed to $\boldsymbol{A}$ by the
equation is far less than $N_G$ within the practical numerical
precision. To extract the limited information about $\boldsymbol{A}$ properly,
the maximum entropy method based on Bayesian inference is
employed [53], where the entropic prior as a means of the
regularization is introduced to circumvent the problem of the
overfitting.

The joint probability of $\boldsymbol{A}$ and hyperparameters $\alpha_\chi$ and $\alpha_S$
for given $\boldsymbol{G}$ is described by using Bayes's theorem as
$$
P(\boldsymbol{A}, \alpha_\chi, \alpha_S|\boldsymbol{G}) = P(\boldsymbol{G}|\boldsymbol{A}, \alpha_\chi)P(\boldsymbol{A}|\alpha_S)P(\alpha_\chi)P(\alpha_S)/P(\boldsymbol{G}). \tag{45}
$$

The distribution of the sum of squared relative errors
$$
\chi^2 \equiv \sum_{i=1}^{N_G} \frac{\left|G_i - \sum_j K_{ij}A_j\right|^2}{|G_i|^2} \tag{46}
$$
is assumed to be represented as a Gaussian function
$$
P(\boldsymbol{G}|\boldsymbol{A}, \alpha_\chi) = \frac{\alpha_\chi^{N_G/2}}{(2\pi)^{N_G/2} \prod_l |G_l|} \mathrm{exp}(-\alpha_\chi \chi^2/2). \tag{47}
$$

Here, $\alpha_\chi$ is also optimized as a hyperparameter, since the stan-
dard deviation $\sigma = 1/\sqrt{\alpha_\chi}$ for the spectral function $A_k(\omega)$
inferred by MEM from the LDFA Green's function of the 2D
Hubbard model has strong momentum $\boldsymbol{k}$ dependence: while
the values of $\sigma$ at $\boldsymbol{k}$ points on the Fermi surface, i.e., the $X-M_2$
line in Fig. 9(d), range from $\sigma = 5 \times 10^{-7}$ to $2 \times 10^{-6}$,
those at $\boldsymbol{k} = (0,0)$ are from $\sigma = 3 \times 10^{-5}$ to $4 \times 10^{-4}$. The
entropic prior is given as
$$
P(\boldsymbol{A}|\alpha_S) \approx \frac{\alpha_S^{N_A/2}}{(2\pi)^{N_A/2} \prod_i m_i^{1/2}} \mathrm{exp}(\alpha_S S), \tag{48}
$$
where $S$ is the relative entropy between $\boldsymbol{A}$ and the default
model $\boldsymbol{m} \equiv (m_1, m_2, \dots)$, and is defined as
$$
S = \sum_{i=1}^{N_A} [A_i - m_i - A_i \ln(A_i/m_i)]. \tag{49}
$$

The uniform distribution is adopted for the default model:
$m_i = 1/N_A$. The prior probabilities for hyperparameters $P(\alpha_\chi)$
and $P(\alpha_S)$ are assumed to be constants and $P(\boldsymbol{G})$ is the
normalization factor.

The joint probability of the hyperparameters $\alpha_\chi$ and $\alpha_S$
can be obtained inserting Eqs. (46)-(49) into Eq. (45) and
integrated it over $\boldsymbol{A}$ within the Gaussian approximation:
$$
\begin{aligned}
\ln P(\alpha_\chi, \alpha_S|\boldsymbol{G}) \approx & \mathrm{const.} + \frac{N_G}{2} \ln \alpha_\chi + \frac{1}{2} \sum_{i=1}^{N_A} \ln \frac{\alpha_S A_i^{\mathrm{max}}}{\alpha_\chi \lambda_i + \alpha_S} \\
& - \frac{\alpha_\chi}{2} \chi^2(\boldsymbol{A}^{\mathrm{max}}) + \alpha_S S(\boldsymbol{A}^{\mathrm{max}}), \tag{50}
\end{aligned}
$$
where $\boldsymbol{A}^{\mathrm{max}}$ denotes $\boldsymbol{A}$ at which $P(\boldsymbol{A}, \alpha_\chi, \alpha_S|\boldsymbol{G})$ is the max-
imum with given values of $\alpha_\chi$ and $\alpha_S$. $\lambda_i$ represents $i$th
eigenvalue of the matrix $\Lambda$:
$$
\Lambda_{ij} = \sum_{l=1}^{N_G} \left(A_i^{\mathrm{max}}\right)^{1/2} K_{li}^* K_{lj} \left(A_j^{\mathrm{max}}\right)^{1/2}/|G_l|^2. \tag{51}
$$

![](./images/817402235402059777_4.jpg)

FIG. 3. Schematic representation of the data points on the com-
plex plane used for MEM. In addition to the data at the fermionic
Matsubara frequencies $z_n = i(2n-1)\pi/\beta$ $(n=1,2,\dots,N_\omega)$ de-
picted as the crosses on the imaginary axis, the equally spaced points
represented as the dots on the curve consisting of two quarter circle
arcs with the radius $R$ connected by the straight line with the length
$W$ in Eq. (21) are included in this study.

Our problem of the analytic continuation is now reduced
to find the set of $\boldsymbol{A}$, $\alpha_\chi$ and $\alpha_S$ which is at the maximum
of $P(\boldsymbol{A}, \alpha_\chi, \alpha_S|\boldsymbol{G})$. To do so, we first set guess values of $\alpha_\chi$
and $\alpha_S$ and maximize $P(\boldsymbol{A}, \alpha_\chi, \alpha_S|\boldsymbol{G})$ with respect to $\boldsymbol{A}$. This
is equivalent to minimizing $Q(\boldsymbol{A}) \equiv \alpha_\chi \chi^2(\boldsymbol{A})/2 - \alpha_S S(\boldsymbol{A})$,
which can be achieved using the Newton-Raphson method.
The calculations are repeated with different values of $\alpha_S$ to
find the maximum of $P(\alpha_\chi, \alpha_S|\boldsymbol{G})$ in Eq. (50) with respect to
$\alpha_S$ with fixed value of $\alpha_\chi$. The golden section search method
is applied for this optimization of $\alpha_S$. To find the maximum of
$P(\alpha_\chi, \alpha_S|\boldsymbol{G})$ in Eq. (50) with respect to $\alpha_\chi$,
$$
\frac{\partial}{\partial \alpha_\chi} P(\alpha_\chi, \alpha_S|\boldsymbol{G}) = 0 \tag{52}
$$
is calculated assuming the $\alpha_\chi$ dependence of $\boldsymbol{A}^{\mathrm{max}}$ is negligi-
ble. The resultant equation for the optimal $\alpha_\chi$ is
$$
\alpha_\chi = \frac{1}{\chi^2(\boldsymbol{A}^{\mathrm{max}})} \left(N_G - \sum_{i=1}^{N_A} \frac{\lambda_i}{\lambda_i + \alpha_S/\alpha_\chi}\right). \tag{53}
$$

This can be solved iteratively by inserting previously obtained
value of $\alpha_\chi$ repeatedly on the right-hand side of the equation.
After solving Eq. (53), the optimization of $\boldsymbol{A}$ and $\alpha_S$ follows
with this new value of $\alpha_\chi$ and again solving Eq. (53). This
process is repeated until convergence is reached.

In the LDFA calculations, the $N_\omega$ data of $G(z_n)$ at the
fermionic Matsubara frequencies, i.e., $z_n = i(2n-1)\pi/\beta$
$(n=1,2,\dots,N_\omega)$ on the imaginary axis are adopted. For
the rest of the data, instead of taking them on the Matsubara
frequencies, a set of data points placed at the same distance
$R$ from the nearest pole of $G(z)$ on the real axis is chosen:
equally spaced points on the curve consisting of two quarter
circle arcs with the radius $R$ connected by a straight line with
the length $W$ in Eq. (21) as shown in Fig. 3. This choice of
data points ameliorates the difficulty of solving Eq. (44) and

the accuracy of $A(\omega)$ obtained is improved, particularly in structures away from the Fermi level. The value of $R$ adopted in this study is $R=2.7W$ except for $U=3.0$, for which $R=1.8W$ is used and the number of these additional points is $N_{\mathrm{R}} \approx R\beta$.

Note that altering the default model other than the uniform distribution scarcely affects the results. What is even more important is the model for $\chi^{2}$ in Eq. (46), where the square sum of the relative errors is assumed instead of the absolute errors as in the previous studies and the data points are chosen as in Fig. 3. This is probably due to the different quality of the data we obtained here, where the main source of errors comes from arithmetic operations and statistical errors are absence unlike previous studies with QMC [53]. The DOS of the 2D Hubbard model inferred by the present and standard maximum entropy methods are compared in Appendix D.

### VII. 2D HUBBARD MODEL

#### A. Accuracy of the results and bench mark

Before discussing the LDFA results of the 2D Hubbard model obtained with the new Lanczos ED method in detail, here, we evaluate the accuracy of the results and make comparisons with results of other methods. We first check the accuracy of the four-point vertex function in Eq. (29). Since we are dealing with the PM state, the spin rotational symmetry can be verified. To do this, the difference between the horizontal-spin $\gamma^{\uparrow \uparrow \uparrow \uparrow}-\gamma^{\downarrow \downarrow \downarrow \uparrow}$ and vertical-spin $\gamma^{\uparrow \downarrow \uparrow \downarrow}$ components, which should be zero for the exact calculations, are examined with respect to $\Omega$ as

$$
\varepsilon(\Omega)=\frac{\sum_{\omega, \omega^{\prime}}\left|\gamma_{\omega \omega^{\prime} ; \Omega}^{\uparrow \uparrow \uparrow \uparrow}-\gamma_{\omega \omega^{\prime} ; \Omega}^{\uparrow \downarrow \downarrow \uparrow}-\gamma_{\omega \omega^{\prime} ; \Omega}^{\uparrow \downarrow \uparrow \downarrow}\right|}{\sum_{\omega, \omega^{\prime}}\left\{\left|\gamma_{\omega \omega^{\prime} ; \Omega}^{\uparrow \uparrow \uparrow \uparrow}\right|+\left|\gamma_{\omega \omega^{\prime} ; \Omega}^{\uparrow \downarrow \downarrow \uparrow}\right|+\left|\gamma_{\omega \omega^{\prime} ; \Omega}^{\uparrow \downarrow \uparrow \downarrow}\right|\right\}}.
\tag{54}
$$

It is found that $\varepsilon(\Omega) \sim 10^{-5}$ for the lowest $\Omega \sim 0$ and the highest $\Omega=4N_{\omega} \sim 4W$ frequencies and less accurate $\varepsilon(\Omega) \sim 10^{-4}$ for intermediate frequencies $\Omega \sim 2W$. This is expected from the approximation made in the Lanczos ED method, which is accurate in low-energy excitations and asymptotic behavior as mentioned in Sec. IV.

Similarly, the accuracy of the LDFA results can be assessed by calculating the same quantity with different directions of spin for the PM state. The accuracy is typically about six digits for values such as the double occupancy $D \equiv \langle n_{i\uparrow}n_{i\downarrow}\rangle$ calculated using the Migdal-Galitskii formula [58]. At low temperatures, however, because of the divergent property of the spin susceptibility $\chi_{\mathrm{sp}} \sim e^{\Delta/T}$ as $T \to 0$ [59,60], the Bethe-Salpeter equation in Eq. (33) is unstable when $\chi_{\mathrm{sp}}^{-1} \propto 1-\lambda_{\mathrm{sp}} \approx e^{-\Delta/T}$ is too small $1-\lambda_{\mathrm{sp}} \lesssim 10^{-3}$, where $\lambda_{\mathrm{sp}}$ is the maximum eigenvalue of a $2N_{\omega} \times 2N_{\omega}$ matrix

$$
M_{\omega, \omega^{\prime}} \equiv \frac{1}{\beta} \gamma_{\omega, \omega^{\prime} ; 0}^{(\mathrm{sp})} \chi_{(\pi, \pi), \omega^{\prime}, 0}^{d, 0}.
\tag{55}
$$

Although the problem can be partly avoided by using technique in Ref. [44], obtained results are less accurate.

As mention before, in the ED method the conduction band is replaced by a finite number of the bath energy levels in the effective IAM. While the accuracy of the results is expected to increase as the number of the bath levels $N_{\mathrm{b}}$ increases, numerical errors introduce by the Lanczos algorithm, where high-energy excitations are omitted, would increase as the number of basis function increases. To check the convergence of the results as a function of $N_{\mathrm{b}}$, the values of $D$ obtained with $N_{\mathrm{b}}=3,5$, and 7 have been compared. Note that one of the bath level is required to be placed at the Fermi level to describe a metallic state and thus $N_{\mathrm{b}}$ needs to be an odd number for the half-filled square-lattice Hubbard model because of the electron-hole symmetry [18]. Whereas considerable difference $|D_{N_{\mathrm{b}}=3}-D_{N_{\mathrm{b}}=5}|/D_{N_{\mathrm{b}}=5} \sim 10^{-3}$ between those obtained with $N_{\mathrm{b}}=3$ and 5 is found for $U=4.0$ at low temperatures, the discrepancy between those obtained with $N_{\mathrm{b}}=5$ and 7 is already within $2 \times 10^{-5}$.

The deviations from the hybridization sum rule [61], which relates the hybridization strength of the effective IAM and the lattice hopping integrals, have also been examined. The sum rule for the square-lattice Hubbard model with the nearest-neighbor hopping is

$$
\sum_{l=1}^{N_{\mathrm{b}}} V_{l}^{2}=4t^{2}.
\tag{56}
$$

The deviation is rapidly reduced with increasing $N_{\mathrm{b}}$: the relative errors $\varepsilon=|(\sum_{l} V_{l}^{2})^{1/2}-2t|/2t$ are utmost $\varepsilon=0.15,6 \times 10^{-3}$, and $6 \times 10^{-5}$ for $N_{\mathrm{b}}=3,5$, and 7, respectively. These findings indicate that well converged values can be obtained with $N_{\mathrm{b}}=7$. Hence, all results presented in the rest of the paper were calculated with $N_{\mathrm{b}}=7$. The number of discretized momentum points in the Brillouin zone of the square lattice used in the calculations is $64 \times 64$. For simplicity, we set the value of the hopping integral $t=1$.

In Fig. 4, the imaginary part of the self-energy $\mathrm{Im} \Sigma_{\boldsymbol{k}}(i\omega_{n})$ on the imaginary axis at momenta $\boldsymbol{k}=(\pi/2,\pi/2)$ and $\boldsymbol{k}=(\pi,0)$ for $U=8.0$ and $\beta=2.0$ obtained with various methods are compared. The differences are mainly found at the lowest Matsubara frequency, i.e., $\omega_{1} \equiv \pi/\beta$. The LDFA values of $\mathrm{Im} \Sigma_{\boldsymbol{k}}(i\omega_{n})$ are substantially reduced from that of DMFT at $\omega_{1}$ and are in good agreements with the DCA result for $\boldsymbol{k}=(\pi,0)$ in Ref. [62]. Our LDFA results are also in good agreement with the previous LDFA results with the diagrammatic QMC method in Ref. [39]. On the other hand, the D$\Gamma$A values are placed between those of DMFT and LDFA. The D$\Gamma$A values at $\omega_{1}$ considerably deviate from that of DCA.

#### B. Energetics

It has been a long-standing debate over where and how the crossover or transition from the Slater to Mott-Heisenberg regime occurs as $U$ increases in the $2D$ Hubbard model [26,30,36,37,43,54–57]. In the Slater regime electrons are delocalized at high temperatures. In the weak coupling limit, the potential energy decreases in the presence of AFM correlations and therefore the stabilization of AFM order is expected to be mainly driven by the potential energy in the Slater regime. On the other hand, in the Mott-Heisenberg regime the localization of electrons already occurs at high temperatures and local spins are formed. In the strong coupling limit, the AFM coupling between the localized spins can be regarded as a virtual process through the electron hopping and the stabilization of AFM order is, therefore, expected to be mainly driven by the kinetic energy in the Mott-Heisenberg regime.

![](./images/817402235402059777_5.jpg)

FIG. 4. Comparison of the imaginary part of the self-energies $\operatorname{Im}\Sigma_{\boldsymbol{k}}(i\omega_{n})$ on the imaginary axis at momenta $\boldsymbol{k}=(\pi/2,\pi/2)$ (upper panel) and $\boldsymbol{k}=(\pi,0)$ (lower panel) for $U=8.0$ and $\beta=2.0$ obtained with various methods. Those of LDFA (open circles) and DMFT (open squares) are the results of this study. The DCA data (closed diamonds) are reproduced from Ref. [62] and the D$\Gamma$A data (closed triangles) from Ref. [39]. The LDFA with the diagrammatic QMC results (crosses) are taken from Ref. [47] (only data with the Matsubara frequency of $\omega_{1}=\pi/\beta$ are available).

In this section, we discuss the temperature and $U$ dependence of the double occupancy and the kinetic energy obtained with LDFA.

Figure 5 shows temperature dependence of the double occupancy $D\equiv\langle n_{i\uparrow}n_{i\downarrow}\rangle$ for various values of $U$ calculated using the Migdal-Galitskii formula [58]. For $U\leqslant5.0$ at high temperature, $D$ increases with decreasing temperature, reaches its local maximum, and then decreases. The local maximum is positioned just above the DMFT Néel temperature $T_{\text{N}}^{\text{DMFT}}$ indicated by the vertical arrows. Although no long-range AFM order is presence in LDFA in finite temperatures, which abides by the Mermin-Wagner theorem, the connection between the local maximum of $D$ found at temperature near $T_{\text{N}}^{\text{DMFT}}$ for $U\leqslant5.0$ and AFM correlations is apparent. The presence of the local maximum is also found in DCA study for $U=4.0$ in Ref. [62] as indicated by the diamonds in Fig. 5(c). The temperature dependence of $D$ for $U\leqslant5.0$ is consistent with what expected in the Slater regime; in high-temperature metallic state, because of the Fermi degeneracy, $D$ increases with decreasing temperature and $D$ decreases as AFM correlations develop below $T_{\text{N}}^{\text{DMFT}}$, where electrons efficiently avoid in each other. These findings are also consistent with the previous LDFA study, where the reduction of the potential energy due to nonlocal AFM correlations found in a range $1.0\leqslant U\leqslant4.0$ [43].

To elucidate the relation between the AFM correlation and the temperature dependence of $D$ more in detail, in Fig. 6, the imaginary part of the self-energy $\operatorname{Im}\Sigma_{\boldsymbol{k}}(i\omega_{n})$ for $U=4.0$ at momenta on the Fermi surface $\boldsymbol{k}=(\pi,0)$ (the $X$ point) and $\boldsymbol{k}=(\pi/2,\pi/2)$ (the $M_{2}$ point) are shown for various values of $\beta$ in panels (a) and (b), respectively. For a noncorrelated metal, $\operatorname{Im}\Sigma_{\boldsymbol{k}}(i\omega_{n})$ at the lowest Matsubara frequency $\omega_{1}=\pi/\beta$ is expected to increase as temperature is lowered, because of the reduction of thermal fluctuations. Hence, the reduction of $\operatorname{Im}\Sigma_{\boldsymbol{k}}(i\pi/\beta)$ found in Fig. 6 indicates

![](./images/817402235402059777_6.jpg)

FIG. 5. Temperature dependence of the double occupancy $D$ for $U=2.0$ (a), 3.0 (b), 4.0 (c), 5.0 (d), and 6.0 (e). The local maxima are shown by the triangles in (a)-(d). In each panel, the arrow indicates $T_{\text{N}}^{\text{DMFT}}$ taken from Fig. 1 in Ref. [44]. For comparison, the values of $D$ calculated with DCA in Ref. [62] are also represented by the diamonds in (a), (c), and (e).

![](./images/817402235402059777_7.jpg)

FIG. 6. The imaginary part of the self-energy $\operatorname{Im}\Sigma_{\boldsymbol{k}}(i\omega_{n})$ for $U=4.0$ with various values of $\beta$ at momenta on the Fermi surface (a) $\boldsymbol{k}=(\pi,0)$ (the $X$ point) and (b) $\boldsymbol{k}=(\pi/2,\pi/2)$ (the $M_{2}$ point).

![](./images/817402235402059777_8.jpg)

FIG. 7. (a) Comparison between the $U$ dependence of the double occupancy $D$ at $\beta=5.0$ (open tip-up triangles) and $\beta=8.0$ (closed tip-down triangles); The inset shows the values of $D$ at $\beta=5.0$ subtracted from that of $\beta=8.0$ $D_{\beta=8.0}-D_{\beta=5.0}$ in a range from $U=4.0$ to 5.6. (b) $\partial^2 D/\partial U^2$ as a function of $U$ for various values of $\beta$.

the increase of AFM fluctuations and the temperature where $\operatorname{Im}\Sigma_k(i\pi/\beta)$ takes the local maximum would be regarded as the onset temperature of AFM correlations. Indeed, the local maximum $\operatorname{Im}\Sigma_k(i\pi/\beta)$ temperature of the $M_2$ point coincides with $T_{\text{N}}^{\text{DMFT}}$ within the deviation of 0.01 in the range of $U=2.0$ to 6.0. It is also found in the previous LDFA study that the maximum of the uniform spin susceptibility for $U=$ 2.0, 3.0, and 4.0 is located at temperatures close to $T_{\text{N}}^{\text{DMFT}}$ [43]. On the other hand, the local maximum temperature of $\operatorname{Im}\Sigma_k(i\pi/\beta)$ of the $X$ point is placed higher than $T_{\text{N}}^{\text{DMFT}}$ and roughly follows the local maximum temperature of $D$.

In contrast, for $U=6.0$, no local maximum can be found in $D$ below $T=0.5$ in Fig. 5(e): $D$ monotonically decreases around $T_{\text{N}}^{\text{DMFT}}$ with decreasing temperature and increases at much lower temperature ($T<0.17$). As can be seen Figs. 5(d) and 5(e), the increase of $D$ with decreasing temperature occurs much lower temperature than $T_{\text{N}}^{\text{DMFT}}$ for $U\geqslant5.0$ and the relation between the onset of the short-range AFM order and the temperature dependence of $D$ is less clear for $U\geqslant$ 5.0. The lack of local maximum of $D$ for $U\geqslant5.5$ below $T=0.5$ coincides with the absence of the local maximum $\operatorname{Im}\Sigma_k(i\pi/\beta)$ of the $X$ point and indicates non-Fermi-liquid or "bad metallic" behavior at high temperatures. The fact is consistent with the Mott-Heisenberg regime, where local spins are expected to be preformed above the onset temperature of AFM correlations, i.e., $T_{\text{N}}^{\text{DMFT}}$.

To clarify where the crossover from the Slater to Mott- Heisenberg regime occurs, in Fig. 7(a), $D$ as a function of $U$ are plotted for $\beta=5.0$ and 8.0. As can be seen in the $D$ curve of $\beta=5.0$, $D$ decreases linearly with increasing $U$ at high temperatures. However, at low temperatures, the decrease of $D$ does not evenly happen as can be observed in the $D$ curve of $\beta=8.0$: the faster (slower) reduction of $D$ for $U<4.7$ ($U>$ 4.7) causes the formation of the concave (convex) in the $D$ curve. This variation of $D$ at low temperatures is in accordance with the crossover from the Slater to Mott-Heisenberg regime with increasing $U$ and thus one can regard the inflection point of the $D$ curve as a boundary between the two regimes. To examine the inflection point of $D$ curve more in detail, in Fig. 7(b), $\partial^2 D/\partial U^2$ as a function of $U$ is shown for various values of $\beta$. For $\beta=4.0$, there is no inflection point in the $D$ curve in a range from $U=4.1$ to 5.5. As temperature decreases, however, $\partial^2 D/\partial U^2$ as a function of $U$ rapidly converges into a curve, which intersects the $\partial^2 D/\partial U^2{=}0$ line at $U\approx4.7$, and changes its sign from positive to negative at $U\approx4.7$. These results indicates that the crossover from the Slater to Mott-Heisenberg regime occurs around $U^{*}\approx4.7$. Similar crossover from the Slater to Mott-Heisenberg regime has been also found in the AFM phase in the CDMFT [36] and variational QMC [57] studies.

![](./images/817402235402059777_9.jpg)

FIG. 8. Kinetic energy $E_{\text{K}}$ as functions of temperature $T$ for various values of $U$. The arrows indicate $T_{\text{N}}^{\text{DMFT}}$ taken from Fig. 1 in Ref. [44]. The inset shows $\Delta E_{\text{K}}$ for various $U$.

Figure 8 shows temperature dependence of the kinetic energy $E_{\text{K}}$ for various values of $U$. For small $U$, the inclination of $E_{\text{K}}$ is reduced with decreasing temperature and no clear change of this tendency at $T_{\text{N}}^{\text{DMFT}}$ is found. In contrast, for $U>4.5$, the inclination of $E_{\text{K}}$ increases with decreasing temperature particularly for $T<T_{\text{N}}^{\text{DMFT}}$ resulting in steep precipitation of $E_{\text{K}}$ below $T_{\text{N}}^{\text{DMFT}}$. This tendency becomes more clear as $U$ increases. To make a rough estimation of the lowering of $E_{\text{K}}$ caused by the AFM correlation, we assume $E_{\text{K}}$ without the AFM correlation can be approximated by a linear function of $T$ below $T_{\text{N}}^{\text{DMFT}}$ and subtract this approximated value from $E_{\text{K}}$ at the lowest temperature $T_{\text{L}}$ available as

$$
\begin{aligned}
\Delta E_{\text{K}} \equiv & E_{\text{K}}(T_{\text{L}})-E_{\text{K}}(T_{\text{N}}^{\text{DMFT}}) \\
& -\left.\frac{\partial E_{\text{K}}}{\partial T}\right|_{T=T_{\text{N}}^{\text{DMFT}}}(T_{\text{L}}-T_{\text{N}}^{\text{DMFT}}).
\end{aligned}\tag{57}
$$

The result is presented in the inset of Fig. 8. Whereas $\Delta E_{\text{K}}$ remains small $|\Delta E_{\text{K}}|<10^{-2}$ for $U\leqslant4.5$, $\Delta E_{\text{K}}$ rapidly decreases with increasing $U$ for $U>5.0$. This fact is consistent with the crossover behavior of $D$ from the Slater to Mott- Heisenberg regime around $U^{*}\approx4.7$, since in the latter the

205133-12

![](./images/817402235402059777_10.jpg)

FIG. 9. DOS $\rho(\omega)$ (top) and the spectral functions $A_{\boldsymbol{k}}(\omega)$ with momenta $\boldsymbol{k}$ along the symmetry lines $\Gamma$-$X$, $X$-$M$, and $M$-$\Gamma$ (bottom) for $U = 4.0$ calculated by means of LDFA with $\beta = 8.0$ (a), LDFA with $\beta = 5.0$ (b) and CPT with a $4 \times 4$ cluster (c). In (d), the Brillouin zone of the square lattice and the symmetry lines and points are depicted; the dashed line represents the Fermi surface at half filling for $U = 0$.

stabilization of the short-range AFM order is expected to be driven by the kinetic energy.

### C. Structures of DOS and the spectral function

Figure 9 shows LDFA results of DOSs and the spectral functions $A_{\boldsymbol{k}}(\omega)$ with momenta $\boldsymbol{k}$ along the symmetry lines $\Gamma$-$X$, $X$-$M$, and $M$-$\Gamma$ for $U = 4.0$ with $\beta = 8.0$ in panel (a) and with $\beta = 5.0$ in panel (b). For comparison those obtained with the cluster perturbation theory (CPT) [63,64] with a $4 \times 4$ cluster are also presented in panel (c). Although the pseudogap already exists in DOS with $\beta = 5.0$, which is also found in the previous LDFA studies [18,43], one can see the prominent development of the pseudogap DOS for $\beta = 8.0$. Such drastic development in the pseudogap with decreasing temperature is consistent with exponential growth of the AFM correlation length with decreasing temperature discussed in the D$\Gamma$A [37] and LDFA [45] studies. The formation of the pseudogap in DOS is found to start at the temperature close to $T_{\text{N}}^{\text{DMFT}}$.

The formation of the pseudogap is also found in the quasiparticle peaks at the Fermi level in $A_{\boldsymbol{k}}(\omega)$ with $\boldsymbol{k} = (\pi, 0)$ (the $X$ point) and $\boldsymbol{k} = (\pi/2, \pi/2)$ (the $M_2$ point) for $\beta = 8.0$. The pseudogap opening along the $\Gamma$-$X$ and $X$-$M$ lines in the vicinity of the $X$ point is also seen along with the peaks corresponding to the shadow band (indicated by the arrows), which is the reminiscence of the Brillouin zone folding caused by the long-range AFM order. On the other hand, for $\beta = 5.0$, although the incipience of pseudogap formation, e.g., the flattening of the quasiparticle peak top, can be observed at the $X$ point, still no such indication found in the peak at the $M_2$ point. The formation of the pseudogap occurs first at the $X$ point, spreads through the Fermi surface and ends at the $M_2$ point with decreasing temperature. The same trends in the temperature and momentum dependence in the pseudogap formation is found in the previous works with TPSC [27], D$\Gamma$A [65], and the QMC calculations of finite-size clusters [40]. More details of the momentum dependence of the pseudogap formation will be discussed in Sec. VII E. Although the structures of the LDFA spectral functions of the momenta near the $\Gamma$ point are blurred because of inaccuracy of the data and the size of the pseudogap in the vicinity of the Fermi level is substantially smaller compared to those of CPT, reasonable agreements can be found between those obtained with LDFA in panel (a) and CPT in panel (c).

### D. Gap formation in DOS

Although the investigation on spin susceptibility and spin correlation length in the previous works with D$\Gamma$A [37,65] and LDFA [44,45] have already revealed that the low-temperature behavior of the spin fluctuations of the half-filled Hubbard model on a square lattice is consistent with the nonlinear $\sigma$ model, the connection between the spin fluctuation and the pseudogap formation is still not well understood. In the previous study with the nonlinear $\sigma$ model approach [31], it is argued that there is a finite critical value of $U$ ($U_{\text{c}} \approx 4.25$) which separates a pseudogap phase and a Mott insulating phase. In the pseudogap phase, finite $\rho(\omega = 0)$ lingers at finite temperature, whereas clear gap opening occurs in the Mott insulating phase. The purpose of this section is to verify whether such abrupt change in the temperature dependence of $\rho(\omega = 0)$ occurs at a finite $U$ or not.

To see the temperature dependence of DOS, in Fig. 10 those with various values of $\beta$ for $U = 4.5$ and $5.0$ are depicted in panels (a) and (b), respectively. Each of these DOSs

![](./images/817402235402059777_11.jpg)

FIG. 10. $\rho(\omega)$ for $U=4.5$ (a) and 5.0 (b) with various values of $\beta$.

consists of a peak at the Fermi level flanked by the shoulder structures corresponding to the lower- and upper-Hubbard bands at high temperatures. The pseudogap appears at a temperature close to $T_{\text{N}}^{\text{DMFT}}$ and further develops as temperature decreases. While finite DOS in the vicinity of the Fermi level persists for $U=4.5$ even at the lowest temperature indicated in the figure, clear opening of the gap can be seen at $\beta=9.0$ for $U=5.0$. From these results it is expected that a pseudogap phase to Mott-Hubbard insulator transition or crossover exists in between $U=4.5$ and 5.0.

To examine how the temperature dependence of $\rho(\omega=0)$ varies as $U$ changes, in Fig. 11, the logarithmic plots of $\rho(\omega=0)$ as a function of $\beta$ for various values of $U$ are presented. The value of $\rho(\omega=0)$ is reduce as temperature decreases and the reduction becomes steeper as $U$ increases particularly at low temperatures; whereas the value of $\rho(\omega=0)$ for $U=4.9$ is rapidly reduced with decreasing temperature and the value is less than $10^{-10}$ at $\beta=10.0$, the reduction is moderate for $U=4.3$ and the value is only reduced to about $47\%$ from $\beta=3.0$ to 10.0.

In the nonlinear $\sigma$ model approach [31], the temperature dependence of $\rho(\omega=0)$ for the weak coupling limit at low temperatures can be approximated by

$$
\rho(\omega=0) \propto \exp \left(-\beta \Delta_{0}\right), \tag{58}
$$

where $\Delta_{0}$ is half the size of the gap of the AFM state at $T=0$. To verify whether the low-temperature behavior of our results are consistent with the pseudogap phase in the nonlinear $\sigma$ model approach for small $U$, the linear least squares fit is made for $\log_{10} \rho(\omega=0)$ as a function of $\beta$ to determine $\Delta_{0}$. For example, the results of the linear least squares fit for $U=4.5$ is shown in Fig. 12. The fitting is made within a range from $\beta=6.2$ to 8.2. A reasonably good agreement can be obtained within the range. However, the substantial deviation from the linear approximation are found for $\beta \geqslant 9.0$ and the values of $\rho(\omega=0)$ are larger than those expected from Eq. (58). This is probably caused by inaccuracy due to small $1-\lambda_{\text{SP}} \lesssim 5 \times 10^{-4}$ for $\beta>8.5$ as mentioned in Sec. VII A. The similar tendency is found for $U \leqslant 4.7$ at low temperatures. The estimated $\Delta_{0}$'s for various values of $U$ are depicted in the inset. The obtained $2\Delta_{0}$ is, indeed, about the peak to peak distance of the pseudogap structure of DOS for $U \leqslant 4.3$. However, $\Delta_{0}$ rapidly deviates from the actual size of the pseudogap of DOS for $U>4.3$ and the possible range of $\beta$ for the linear fitting is reduced as $U$ increases, indicating rapid disappearance of states inside the gap. No reasonable fitting is available for $U \geqslant 4.8$.

![](./images/817402235402059777_12.jpg)

FIG. 11. Logarithmic plots of $\rho(\omega=0)$ as functions of $\beta$ for various values of $U$: $U=3.0$, 3.5, 4.0, 6.0, and 0.1 interval from 4.3 to 5.5.

![](./images/817402235402059777_13.jpg)

FIG. 12. Logarithmic plot of $\rho(\omega=0)$ as a function of $\beta$ for $U=4.5$ (closed circles) and its linear least squares fit within a range from $\beta=6.2$ to 8.2 (open circles). The inset shows $\Delta_{0}$ evaluated from the least squares analysis for various values of $U$.

These results show that a sharp crossover from the pseudogap phase to the Mott insulator takes place at $U^* \approx 4.7$. Indeed, the value of $U^*$ coincides with the boundary between the Slater and Mott-Heisenberg regimes defined by the inflection point of $D$ curve as a function of $U$, i.e., $(\partial^2 D/\partial U^2)_T = 0$, discussed in Sec. VII B.

The robustness of the results obtained here has been checked by altering the part of the procedure of MEM described in Sec. VI in several different ways, e.g., by taking data points only on the imaginary axis instead of those in Fig. 3 or replacing the definition of $\chi^2$ in Eq. (46) by that with absolute errors. Although the accuracy of the data is reduced and discernible fluctuations of the data can be observed when the same $\log_{10} \rho(\omega = 0)$ plots as in Fig. 11 are made, the variation of the estimated values of $U^*$ is within 0.1.

### E. Pseudogap in the spectral function

In the previous study with D$\Gamma$A [37,66], the MIT in the half-filled Hubbard model on a square lattice has been discussed, where the transition temperature is related to the variation in the $\omega_n$ dependence of $\text{Im } \Sigma_k(i\omega_n)$. If the system is a Fermi liquid or at least a Fermi liquid like, it is expected that $|\text{Im } \Sigma_k(\omega)|$ should decrease as $\omega$ decreases. However, the loss of the Fermi-liquid feature is not necessarily indicating insulating behavior of the system. The purpose of this subsection is to clarify the relation between the pseudogap formation in the spectral function $A_k(\omega)$ and the change in $\text{Im } \Sigma_k(i\omega_n)$.

As discussed in Sec. VII C, the pseudogap formation in $A_k(\omega)$ has $k$ dependence; it initiates at the $X$ point and spread through the Fermi surface and terminates at the $M_2$ point as temperature decreases. Figure 13 shows $A_k(\omega)$ in the vicinity of the Fermi level for $U = 3.0$ at temperatures across the pseudogap formation at the $X$ and $M_2$ points together with the corresponding $\text{Im } \Sigma_k(i\omega_n)$. It is clearly seen in panels (b) and (d) that the $\omega_n$ dependence of $\text{Im } \Sigma_k(i\omega_n)$ changes upturn to downturn in $\text{Im } \Sigma_k(i\omega_n)$ with decreasing temperature around the pseudogap formation temperature. These results are in good agreement with those of D$\Gamma$A calculations for $U = 3.0$ in Ref. [66]. This indicates that for small $U$ the Fermi-liquid feature is gradually lost accompanied by the pseudogap formation in $A_k(\omega)$ at the Fermi level. It is also found in panels (b) and (d) that the variation mainly occurs in the lowest Matsubara frequency $\omega_1 = \pi/\beta$, where $|\text{Im } \Sigma_k(i\pi/\beta)|$ is increases with decreasing temperature. This predominant increase in $|\text{Im } \Sigma_k(i\pi/\beta)|$, as was already pointed out in Ref. [24], is the main cause of the double peak structure in $A_k(\omega)$, i.e., the formation of the pseudogap. Since the low-temperature magnetic excitation of the half-filled Hubbard model on a square lattice is considered to be described by the two-dimensional nonlinear $\sigma$ model in the renormalized classical regime [59], the magnetic scattering at the lowest Matsubara frequency is expected to be the dominant process, which is consistent with our results.

![](./images/817402235402059777_14.jpg)

FIG. 13. Relationship between the pseudogap formation at the Fermi level of $A_k(\omega)$ for $U = 3.0$ and corresponding $\text{Im } \Sigma_k(i\omega_n)$. $A_k(\omega)$ at the $X$ point $[k = (\pi, 0)]$ in the vicinity of the Fermi level with temperatures across the pseudogap formation $\beta = 7.0, 7.5, 8.0, 8.5$, and $9.0$ are shown in (a) and corresponding $\text{Im } \Sigma_k(i\omega_n)$ on the imaginary axis are depicted in (b). Those in (c) and (d) are the same as in (a) and (b) but for the $M_2$ point $[k = (\pi/2, \pi/2)]$ with $\beta = 9.0, 9.5, 10.0, 10.5$, and $11.0$.

The relation, however, becomes less clear as $U$ increases, although the pseudogap formation still occurs below $T_{\text{N}}^{\text{DMFT}}$. As shown in Fig. 14, for $U = 5.0$, $|\text{Im } \Sigma_k(i\omega_n)|$ at the $X$ point monotonically increases with decreasing $\omega_n$ already at high temperatures above $T_{\text{N}}^{\text{DMFT}}$ and therefore no upturn to downturn change occurs in $\text{Im } \Sigma_k(i\omega_n)$ at $\beta = 4.75$ where the pseudogap appears. This non-Fermi-liquid feature in $\text{Im } \Sigma_k(i\omega_n)$ above $T_{\text{N}}^{\text{DMFT}}$ spreads through the Fermi surface from the $X$ to the $M_2$ point as $U$ increases from $U = 4.0$ and at $U = 5.5$ the whole Fermi surface is lost already above the temperature where the pseudogap appears, resulting in no upturn to downturn change in $\text{Im } \Sigma_k(i\omega_n)$ at all.

Furthermore, one can see the enhancement of the intensity of shoulder structures around $\omega \approx \pm 2.5$ in $A_k(\omega)$ and the increase of $|\text{Im } \Sigma_k(i\omega_n)|$ up to $\omega_n \sim 5$ with decreasing temperature. The appearance of the high-energy structure $\omega \approx \pm U/2$ is hallmark of the Mott physics and cannot be explained by the magnetic scattering within the energy scale of $T_{\text{N}}^{\text{DMFT}} \sim 0.3$. These facts can be contrasted with $A_k(\omega)$ and $\text{Im } \Sigma_k(i\omega_n)$ for $U = 3.0$ in Fig. 13, where their temperature effects are mainly found within the energy scale of $T_{\text{N}}^{\text{DMFT}} \sim 0.2$ around the Fermi level and are in accordance with the Slater mechanism of gap formation due to the short-range AFM ordering. Nevertheless, a quasi-particle-like broad single peak still exists at the Fermi level at high temperatures in $A_k(\omega)$ for $U = 5.0$ in Fig. 14 and predominant increase in $|\text{Im } \Sigma_k(i\pi/\beta)|$ owing to the magnetic scattering leads to the pseudogap formation.

![](./images/817402235402059777_15.jpg)

FIG. 14. The same as Fig. 13 but for $U=5.0$.

### F. $U$-$T$ phase diagram

To conclude this section, here we consider how the electronic state changes on the $U$-$T$ parameter space. In Fig. 1, characteristic temperatures so far discussed are summarized. The $D$ local maximum temperature is the onset temperature of AFM correlation in the high-temperature metallic state, which is signaled by increase in $|\mathrm{Im}\,\Sigma_{\boldsymbol{k}}(i\pi/\beta)|$ with decreasing temperature around the $X$ point for $U<5.0$. For $U\geqslant5.5$, on the other hand, strong correlations already develop at high temperatures and no $D$ local maximum temperature found below $T<0.5$. The AFM correlations further develop with decreasing temperature and at $T_{\mathrm{N}}^{\mathrm{DMFT}}$, $|\mathrm{Im}\,\Sigma_{\boldsymbol{k}}(i\pi/\beta)|$ with momenta $\boldsymbol{k}$ on whole Fermi surface start to increase with decreasing temperature.

For $U\leqslant3.5$, the Fermi-liquid behavior is gradually lost below $T_{\mathrm{N}}^{\mathrm{DMFT}}$ line as the AFM correlations develops with decreasing temperature. This starts at the $X$ point of the Fermi surface and ends at the $M_{2}$ point with concomitant formation of the pseudogap in the corresponding quasiparticle peak at the Fermi level. The Fermi surface is totally lost and the formation of the pseudogap at the Fermi level is complete at the $M_{2}$ pseudogap line. The difference between the pseudogap temperatures at the $X$ and $M_{2}$ points rapidly decreases as $U$ is reduced and is only about $2\times10^{-3}$ at $U=2.0$.

The same gradual pseudogap formation in the peak at the Fermi level occurs for $U\geqslant4.0$ below the $T_{\mathrm{N}}^{\mathrm{DMFT}}$ line. In this case, however, $|\mathrm{Im}\,\Sigma_{\boldsymbol{k}}(i\pi/\beta)|$ around the $X$ point is large even at high temperatures and the system is already non-Fermi-liquid like above the pseudogap formation temperature. This tendency is strengthen as $U$ increases and for $U\geqslant5.5$, the whole Fermi surface is already non-Fermi-liquid like above the pseudogap formation temperature, where $A_{\boldsymbol{k}}(\omega)$ has a structure with a broad single peak at the Fermi level accompanied by prominent shoulder structures at $\omega\approx\pm U/2$. In this regards, the formation of the pseudogap at low temperatures only heralds the development of AFM correlations for $U\geqslant5.5$ and local spins are considered to be preformed at higher temperatures as expected in the Mott-Heisenberg regime. This is contrasted with the simultaneous formation of the pseudogap and loss of the Fermi-liquid feature found for $U\leqslant3.5$, which is expected in the Slater regime. Note that the $D$ local maximum and the $X$ and $M_{2}$ pseudogap lines are only those of crossover and no anomaly which indicates a true transition is found in $D$, DOS or the spectral functions.

Further lowering the temperature, the development of the pseudogap is distinctly different depending on whether $U$ is larger or smaller than $U^{*}\approx4.7$. For $U<U^{*}$, $\rho(\omega=0)$ is reduced with decreasing temperature but persists even at low temperatures. In contrast, for $U>U^{*}$, the reduction is much rapid and clear gap opening occurs at certain temperature. The value of $U^{*}\approx4.7$ coincides with the boundary between the Slater and Mott-Heisenberg regimes defined by the inflection point of $D$ curve as a function of $U$.

### VIII. DISCUSSIONS

The MIT in the half-filled Hubbard model on the square lattice has been discussed using D$\Gamma$A and lattice QMC [37]. Although the difference between the pseudogap formation temperatures at the $X$ and $M_{2}$ points is substantially larger compared to the present study, the behavior of the formation found in this D$\Gamma$A study for $U\leqslant4.0$ is essentially the same to the present study (see Fig. 1): the pseudogap formation starts at the $X$ point and ends at the $M_{2}$ point with decreasing temperature. From this results it is suggested that $U_{\mathrm{c}}=0$ for $T\rightarrow0$ and thus no MIT occurs at any $U>0$ similar to the one-dimensional Hubbard model in this D$\Gamma$A study. Although we found a sharp crossover from the pseudogap phase to Mott insulator around $U^{*}\approx4.7$, we did not find any anomaly, e.g., a discontinuity or kink, in $D$ up to the second derivative with respect to $U$ at $U^{*}$. Hence, it is unlikely that $U^{*}\approx4.7$ is the true MIT point. For this reason, in the strict sense, the true MIT point is considered to be presence at $U_{\mathrm{c}}=0$. This weakness of the variation from the metallic to insulating phase at $U^{*}$ as compared to that in infinite dimension is not surprising. Since the pseudogap owing to the AFM correlation already exists at higher temperatures, the crossover we have discussed here amounts to a subtle change in the states in the gap. This is contrasted with the MIT in the Hubbard model in infinite dimension, where the abrupt destruction of the coherent peak at the Fermi level causes the first-order MIT in finite temperature.

In the D$\Gamma$A study, there is no detailed investigation on DOS at the Fermi level below the pseudogap formation temperature in particular for $U>4.0$. For this reason, there is a possibility that a similar sharp crossover from the Slater to Mott-Heisenberg regime is found at finite $U$ in D$\Gamma$A and it would be interesting to investigate DOS at the Fermi level below the pseudogap formation temperature with D$\Gamma$A to clarify this point.

205133-16

## IX. CONCLUSIONS
A new formula for the two-body Green's function combined with the Lanczos ED technique proposed in this paper provides efficient and accurate means to calculate the local vertex function of the effective impurity Anderson model required for DFA and similar perturbative extensions of DMFT. The formula is applicable to not only the impurity Anderson model but cluster models including those with multiple orbitals. Utilizing this new scheme, the double occupancy, kinetic energy, spectral function and DOS of the Hubbard model on the square lattice at the half-filling are calculated by means of LDFA with an unprecedented accuracy at low temperatures and $U$'s ranging from $U=2.0$ to 6.0 to discuss the metal-insulator transition.

It is found that the pseudogap is first formed in the quasi-particle peak of the spectral function at the $X$ point as temperature decreases. The formation spreads through the Fermi surface and ends at the $M_{2}$ point $\boldsymbol{k}=(\pi/2,\pi/2)$ similar to the previous D$\Gamma$A and lattice QMC study [37]. For $U\leqslant3.5$, the pseudogap formation and the loss of the Fermi-liquid feature occur simultaneously and below the temperature of the pseudogap formation at the $M_{2}$ point, the Fermi surface is totally lost and the system enters the pseudogap phase. These results for $U\leqslant3.5$ are consistent with those expected in the Slater regime.

However, for larger $U$, although the formation of the pseudogap still occurs in the quasi-particle-like single peak at the Fermi level accompanied by prominent shoulder structures at $\omega\approx\pm U/2$, the Fermi-liquid feature is partially lost around the $X$ point already at higher temperatures above $T_{\text{N}}^{\text{DMFT}}$ for $U=4.0$ and totally lost for $U\geqslant5.5$. These results for $U\geqslant$ 4.0 is consistent with those expected in the Mott-Heisenberg regime, in which local spins are preformed above the temperature where AFM correlations start to develop.

A sharp crossover from the pseudogap phase to the Mott insulator around $U^{*}\approx4.7$ is found to occur below the temperature of the pseudogap formation. For $U<U^{*}$, $\rho(\omega=0)$ is reduced with decreasing temperature but persists even at low temperatures. In contrast, for $U>U^{*}$, the reduction is much rapid and clear gap opening occurs at certain temperature. These low-energy behavior of DOS in the vicinity of the Fermi level is consistent with the previous study with the nonlinear $\sigma$ model approach [31].

## ACKNOWLEDGMENTS
This work was supported by JSPS KAKENHI Grants No. 25400377, No. 18K03541, and No. 18H03683. The author also would like to thank A. Lichtenstein for fruitful discussions.

## APPENDIX A: DERIVATION OF THE NEW EXPRESSION FOR TWO-BODY GREEN'S FUNCTION
The purpose of this section is to provide detailed description of a derivation of the expression for the two-body Green's function given in Eqs. (5)-(8).

$$
\begin{aligned}
& \chi_{1234}(i \omega_{1}, i \omega_{2} ; i \omega_{3}, i \omega_{1}+i \omega_{2}-i \omega_{3}) \\
& \quad=\int_{0}^{\beta} d \tau_{1} \int_{0}^{\beta} d \tau_{2} \int_{0}^{\beta} d \tau_{3}\langle\mathcal{T}\left[c_{1}\left(\tau_{1}\right) c_{2}\left(\tau_{2}\right) c_{3}^{\dagger}\left(\tau_{3}\right) c_{4}^{\dagger}(0)\right]\rangle e^{i\left(\omega_{1} \tau_{1}+\omega_{2} \tau_{2}-\omega_{3} \tau_{3}\right)} \\
& \quad=\frac{1}{Z} \sum_{l m n k}\langle k|c_{1}| l\rangle\langle l|c_{2}| m\rangle\langle m|c_{3}^{\dagger}| n\rangle\langle n|c_{4}^{\dagger}| k\rangle \phi_{l m n k}\left(\omega_{1}, \omega_{2},-\omega_{3}\right)+\frac{1}{Z} \sum_{l m n k}\langle k|c_{3}^{\dagger}| l\rangle\langle l|c_{1}| m\rangle\langle m|c_{2}| n\rangle\langle n|c_{4}^{\dagger}| k\rangle \phi_{l m n k}\left(-\omega_{3}, \omega_{1}, \omega_{2}\right) \\
& \quad \quad+\frac{1}{Z} \sum_{l m n k}\langle k|c_{2}| l\rangle\langle l|c_{3}^{\dagger}| m\rangle\langle m|c_{1}| n\rangle\langle n|c_{4}^{\dagger}| k\rangle \phi_{l m n k}\left(\omega_{2},-\omega_{3}, \omega_{1}\right)-\frac{1}{Z} \sum_{l m n k}\langle k|c_{3}^{\dagger}| l\rangle\langle l|c_{2}| m\rangle\langle m|c_{1}| n\rangle\langle n|c_{4}^{\dagger}| k\rangle \phi_{l m n k}\left(-\omega_{3}, \omega_{2}, \omega_{1}\right) \\
& \quad \quad-\frac{1}{Z} \sum_{l m n k}\langle k|c_{1}| l\rangle\langle l|c_{3}^{\dagger}| m\rangle\langle m|c_{2}| n\rangle\langle n|c_{4}^{\dagger}| k\rangle \phi_{l m n k}\left(\omega_{1},-\omega_{3}, \omega_{2}\right)-\frac{1}{Z} \sum_{l m n k}\langle k|c_{2}| l\rangle\langle l|c_{1}| m\rangle\langle m|c_{3}^{\dagger}| n\rangle\langle n|c_{4}^{\dagger}| k\rangle \phi_{l m n k}\left(\omega_{2}, \omega_{1},-\omega_{3}\right),
\end{aligned}
\tag{A1}
$$

where

$$
\phi_{l m n k}\left(\omega_{1}, \omega_{2}, \omega_{3}\right)=e^{-\beta E_{k}} \int_{0}^{\beta} d \tau_{1} \int_{0}^{\tau_{1}} d \tau_{2} \int_{0}^{\tau_{2}} d \tau_{3} e^{\left(E_{k}-E_{l}+i \omega_{1}\right) \tau_{1}} e^{\left(E_{l}-E_{m}+i \omega_{2}\right) \tau_{2}} e^{\left(E_{m}-E_{n}+i \omega_{3}\right) \tau_{3}}.
\tag{A2}
$$

If both the condition $E_{k} \neq E_{m}$ or $\omega_{1}+\omega_{2} \neq 0$ and the condition $E_{l} \neq E_{n}$ or $\omega_{2}+\omega_{3} \neq 0$ are satisfied, we obtain

$$
\begin{aligned}
\phi_{l m n k}\left(\omega_{1}, \omega_{2}, \omega_{3}\right)= & -\frac{e^{-\beta E_{n}}-e^{-\beta E_{k}}}{\left(E_{m}-E_{n}+i \omega_{3}\right)\left(E_{l}-E_{n}+i\left(\omega_{2}+\omega_{3}\right)\right)\left(E_{k}-E_{n}+i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\right)} \\
& +\frac{e^{-\beta E_{l}}-e^{-\beta E_{k}}}{\left(E_{m}-E_{n}+i \omega_{3}\right)\left(E_{l}-E_{n}+i\left(\omega_{2}+\omega_{3}\right)\right)\left(E_{k}-E_{l}+i \omega_{1}\right)} \\
& -\frac{e^{-\beta E_{m}}-e^{-\beta E_{k}}}{\left(E_{m}-E_{n}+i \omega_{3}\right)\left(E_{l}-E_{m}+i \omega_{2}\right)\left(E_{k}-E_{m}+i\left(\omega_{1}+\omega_{2}\right)\right)} \\
& -\frac{e^{-\beta E_{l}}-e^{-\beta E_{k}}}{\left(E_{m}-E_{n}+i \omega_{3}\right)\left(E_{l}-E_{m}+i \omega_{2}\right)\left(E_{k}-E_{l}+i \omega_{1}\right)}.
\end{aligned}
\tag{A3}
$$

Now we rewrite the right-hand side of Eq. (A3) in such a way that the three factors in denominator and the argument of the exponential function of each term contain the same eigenvalue of $\mathcal{H}$. To do this, we use the identity

$$
\frac{1}{z_{1} z_{2}}=\frac{1}{z_{2} \pm z_{1}}\left(\frac{1}{z_{1}} \pm \frac{1}{z_{2}}\right). \tag{A4}
$$

For instance, the term with the factor $e^{-\beta E_{l}}$ on the second line of Eq. (A3) can be transformed into

$$
e^{-\beta E_{l}}\left(\frac{1}{E_{m}-E_{n}+i \omega_{3}}-\frac{1}{E_{l}-E_{n}+i\left(\omega_{2}+\omega_{3}\right)}\right) \frac{1}{\left(E_{l}-E_{m}+i \omega_{2}\right)\left(E_{k}-E_{l}+i \omega_{1}\right)}. \tag{A5}
$$

Together with the term with the factor $e^{-\beta E_{l}}$ on the fourth line of Eq. (A3), we get

$$
-e^{-\beta E_{l}} \frac{1}{\left(E_{l}-E_{n}+i\left(\omega_{2}+\omega_{3}\right)\right)\left(E_{l}-E_{m}+i \omega_{2}\right)\left(E_{k}-E_{l}+i \omega_{1}\right)}, \tag{A6}
$$

where all the factors in the denominator and $e^{-\beta E_{l}}$ contain the same eigenvalue $E_{l}$. We can cast all the terms of Eq. (A3) in this form by further repeated use of Eq. (A4) to the terms with $e^{-\beta E_{k}}$:

$$
\begin{aligned}
\phi_{l m n k}\left(\omega_{1}, \omega_{2}, \omega_{3}\right) &=-e^{-\beta E_{k}} \frac{1}{\left(E_{k}-E_{l}+i \omega_{1}\right)\left(E_{k}-E_{m}+i\left(\omega_{1}+\omega_{2}\right)\right)\left(E_{k}-E_{n}+i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\right)} \\
&-e^{-\beta E_{m}} \frac{1}{\left(E_{m}-E_{n}+i \omega_{3}\right)\left(E_{m}-E_{k}-i\left(\omega_{1}+\omega_{2}\right)\right)\left(E_{m}-E_{l}-i \omega_{2}\right)} \\
&+e^{-\beta E_{l}} \frac{1}{\left(E_{l}-E_{m}+i \omega_{2}\right)\left(E_{l}-E_{n}+i\left(\omega_{2}+\omega_{3}\right)\right)\left(E_{l}-E_{k}-i \omega_{1}\right)} \\
&+e^{-\beta E_{n}} \frac{1}{\left(E_{n}-E_{k}-i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\right)\left(E_{n}-E_{l}-i\left(\omega_{2}+\omega_{3}\right)\right)\left(E_{n}-E_{m}-i \omega_{3}\right)}.
\end{aligned} \tag{A7}
$$

These terms correspond to the major terms discussed in Sec. III such as Eq. (12).

We now deal with the situations with $E_{k}=E_{m}$ or $E_{l}=E_{n}$, where some of denominators in Eq. (A7) are zero if $\omega_{1}+\omega_{2}=0$ or $\omega_{2}+\omega_{3}=0$ is satisfied. When $E_{k}=E_{m}$ and $\omega_{1}+\omega_{2} \neq 0$, using Eq. (A4) the first two lines on the right-hand side of Eq. (A7) can be written as

$$
\begin{aligned}
&-e^{-\beta E_{k}}\left\{\frac{1}{\left(E_{k}-E_{l}+i \omega_{1}\right) i\left(\omega_{1}+\omega_{2}\right)\left(E_{k}-E_{n}+i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\right)}-\frac{1}{\left(E_{k}-E_{n}+i \omega_{3}\right) i\left(\omega_{1}+\omega_{2}\right)\left(E_{k}-E_{l}-i \omega_{2}\right)}\right\} \\
&=-e^{-\beta E_{k}}\left[\frac{1}{E_{k}-E_{l}+i \omega_{1}} \frac{1}{E_{k}-E_{n}+i \omega_{3}}\left\{\frac{1}{i\left(\omega_{1}+\omega_{2}\right)}-\frac{1}{E_{k}-E_{n}+i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)}\right\}\right. \\
&\left.\quad-\frac{1}{E_{k}-E_{n}+i \omega_{3}} \frac{1}{E_{k}-E_{l}+i \omega_{1}}\left\{\frac{1}{i\left(\omega_{1}+\omega_{2}\right)}+\frac{1}{E_{k}-E_{l}-i \omega_{2}}\right\}\right] \\
&=e^{-\beta E_{k}} \frac{1}{\left(E_{k}-E_{l}+i \omega_{1}\right)\left(E_{k}-E_{n}+i \omega_{3}\right)}\left\{\frac{1}{E_{k}-E_{n}+i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)}+\frac{1}{E_{k}-E_{l}-i \omega_{2}}\right\}.
\end{aligned} \tag{A8}
$$

Similarly, when $E_{l}=E_{n}$ and $\omega_{2}+\omega_{3} \neq 0$, the last two lines on the right-hand side of Eq. (A7) can be written as

$$
\begin{aligned}
&e^{-\beta E_{l}}\left\{\frac{1}{\left(E_{l}-E_{m}+i \omega_{2}\right) i\left(\omega_{2}+\omega_{3}\right)\left(E_{l}-E_{k}-i \omega_{1}\right)}-\frac{1}{\left(E_{l}-E_{k}-i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\right) i\left(\omega_{2}+\omega_{3}\right)\left(E_{l}-E_{m}-i \omega_{3}\right)}\right\} \\
&=-e^{-\beta E_{l}} \frac{1}{\left(E_{l}-E_{k}-i\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\right)\left(E_{l}-E_{m}+i \omega_{2}\right)}\left\{\frac{1}{E_{l}-E_{k}-i \omega_{1}}+\frac{1}{E_{l}-E_{m}-i \omega_{3}}\right\}.
\end{aligned} \tag{A9}
$$

To complete the calculation of $\phi$, we further need to know special cases of the integration of Eq. (A2). If $E_{k}=E_{m}$ and $\omega_{1}+\omega_{2}=$ 0 , we obtain

$$
\begin{aligned}
\phi_{l m n k}\left(\omega_{1}, \omega_{2}, \omega_{3}\right)=&+e^{-\beta E_{k}} \frac{1}{\left(E_{k}-E_{l}+i \omega_{1}\right)\left(E_{k}-E_{n}+i \omega_{3}\right)}\left\{\frac{1}{E_{k}-E_{n}+i \omega_{3}}+\frac{1}{E_{k}-E_{l}+i \omega_{1}}\right\} \\
&+e^{-\beta E_{l}} \frac{1}{\left(E_{l}-E_{k}-i \omega_{1}\right)^{2}\left(E_{l}-E_{n}+i\left(\omega_{2}+\omega_{3}\right)\right)}+e^{-\beta E_{n}} \frac{1}{\left(E_{n}-E_{k}-i \omega_{3}\right)^{2}\left(E_{n}-E_{l}-i\left(\omega_{2}+\omega_{3}\right)\right)} \\
&+\beta e^{-\beta E_{k}} \frac{1}{\left(E_{k}-E_{n}+i \omega_{3}\right)\left(E_{k}-E_{l}-i \omega_{2}\right)}.
\end{aligned} \tag{A10}
$$

The terms on the first line of Eq. (A10) are identical to Eq. (A8) with $E_{k}=E_{m}$ and $\omega_{1}+\omega_{2}=0$ and the same holds for the terms on the second and third lines of Eq. (A10), which correspond to the terms on the last two lines of Eq. (A7). However the

term on the last line of Eq. (A10) is newly appeared. Similarly, if $E_l = E_n$ and $\omega_2 + \omega_3 = 0$, we obtain

$$
\begin{aligned}
\phi_{lmnk}(\omega_1, \omega_2, \omega_3) =& -e^{-\beta E_k} \frac{1}{(E_k - E_l + i\omega_1)^2(E_k - E_m + i(\omega_1 + \omega_2))} - e^{-\beta E_m} \frac{1}{(E_m - E_l - i\omega_2)^2(E_m - E_k - i(\omega_1 + \omega_2))} \\
& - e^{-\beta E_l} \frac{1}{(E_l - E_k - i\omega_1)(E_l - E_m + i\omega_2)} \left\{ \frac{1}{E_l - E_k - i\omega_1} + \frac{1}{E_l - E_m + i\omega_2} \right\} \\
& - \beta e^{-\beta E_l} \frac{1}{(E_l - E_k - i\omega_1)(E_l - E_m + i\omega_2)}.
\end{aligned} \tag{A11}
$$

We find the terms on the third line of Eq. (A11) are identical to Eq. (A9) with $E_l = E_n$ and $\omega_2 + \omega_3 = 0$ and the terms on the first two lines of Eq. (A11) correspond to those on the first two lines of Eq. (A7). Again, we see the additional term on the last line of Eq. (A11). From Eqs. (A7)-(A11), we obtain

$$
\begin{aligned}
\phi_{lmnk}(\omega_1, \omega_2, \omega_3) =& - (1 - \delta_{E_k,E_m}) e^{-\beta E_k} \frac{1}{(E_k - E_l + i\omega_1)(E_k - E_m + i(\omega_1 + \omega_2))(E_k - E_n + i(\omega_1 + \omega_2 + \omega_3))} \\
& - (1 - \delta_{E_k,E_m}) e^{-\beta E_m} \frac{1}{(E_m - E_n - i\omega_3)(E_m - E_k - i(\omega_1 + \omega_2))(E_m - E_l - i\omega_2)} \\
& + (1 - \delta_{E_l,E_n}) e^{-\beta E_l} \frac{1}{(E_l - E_m + i\omega_2)(E_l - E_n + i(\omega_2 + \omega_3))(E_l - E_k - i\omega_1)} \\
& + (1 - \delta_{E_l,E_n}) e^{-\beta E_n} \frac{1}{(E_n - E_k - i(\omega_1 + \omega_2 + \omega_3))(E_n - E_l - i(\omega_2 + \omega_3))(E_n - E_m - i\omega_3)} \\
& + \delta_{E_k,E_m} e^{-\beta E_k} \frac{1}{(E_k - E_l + i\omega_1)(E_k - E_n + i\omega_3)} \left\{ \frac{1}{E_k - E_n + i(\omega_1 + \omega_2 + \omega_3)} + \frac{1}{E_k - E_l - i\omega_2} \right\} \\
& - \delta_{E_l,E_n} e^{-\beta E_l} \frac{1}{(E_l - E_k - i(\omega_1 + \omega_2 + \omega_3))(E_l - E_m + i\omega_2)} \left\{ \frac{1}{E_l - E_k - i\omega_1} + \frac{1}{E_l - E_m - i\omega_3} \right\} \\
& + \delta_{E_k,E_m} \delta_{\omega_1,-\omega_2} \beta e^{-\beta E_k} \frac{1}{(E_k - E_n + i\omega_3)(E_k - E_l - i\omega_2)} \\
& - \delta_{E_l,E_n} \delta_{\omega_2,-\omega_3} \beta e^{-\beta E_l} \frac{1}{(E_l - E_k - i\omega_1)(E_l - E_m + i\omega_2)}.
\end{aligned} \tag{A12}
$$

Finally, inserting Eq. (A12) into Eq. (A1), we obtain the expression for the two-body Green's function in Eqs. (5)-(8).

## APPENDIX B: DERIVATION OF UPDATE FORMULA OF HYBRIDIZATION FUNCTION

Here, we show the derivation of the update formula of $\Delta_\omega$ for DFA in Eq. (41). For the DMFT calculation, one can choose new $\Delta_\omega$ and $g_\omega$ for next iteration

$$
g_\omega^\text{new} = \langle g_{k\omega} \rangle_k, \tag{B1}
$$

$$
\Delta_\omega^\text{new} = g_\omega^{-1} - \left[ g_\omega^\text{new} \right]^{-1} + \Delta_\omega, \tag{B2}
$$

where $g_{k\omega} \equiv \left[ g_\omega^{-1} + \Delta_\omega - \varepsilon_k \right]^{-1}$ is the DMFT lattice Green's function. These update formulas render robust and rapid convergence of $\Delta_\omega$ for DMFT. A formula similar to Eq. (B1) can be derived for DFA. The condition of the convergence of $\Delta_\omega$ adopted in this study is $\langle G_{k\omega}^d \rangle_k = 0$. We rewrite this equation as

$$
\begin{aligned}
\langle G_{k\omega}^d \rangle_k &= \langle G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1} G_{k\omega}^{d,0} \rangle_k \\
&= \langle G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1} \left( -g_\omega + g_{k\omega} \right) \rangle_k \\
&= -\langle G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1} \rangle_k g_\omega + \langle G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1} g_{k\omega} \rangle_k = 0.
\end{aligned} \tag{B3}
$$

From this one may employ

$$
g_\omega^\text{new} = \langle G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1} \rangle_k^{-1} \langle G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1} g_{k\omega} \rangle_k \tag{B4}
$$

as an update for $g_\omega$ of DFA. Indeed, if $\Sigma_\omega^d = 0$, this equation is reduced to Eq. (B1). With combined use of Eq. (B2), one can obtain new hybridization function for DFA. Finally, substitution of Eq. (B4) into Eq. (B2) and use of the relation $g_{k\omega}^{-1} = g_\omega^{-1} + \Delta_\omega - \varepsilon_k$ results in Eq. (41). Similar formula can be obtained for DMFT: $\Delta_\omega^\text{new} = g_\omega^{-1} \langle g_{k\omega} \varepsilon_k \rangle_k$. Note that instead of directly calculating $G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1}$ in Eq. (41), it is preferable to use

$$
G_{k\omega}^d \left[ G_{k\omega}^{d,0} \right]^{-1} = \left[ 1 - \Sigma_{k\omega}^d G_{k\omega}^{d,0} \right]^{-1} \tag{B5}
$$

to avoid loss of significant digits with small interaction.

## APPENDIX C: CONVERGENCE OF THE VERTEX FUNCTION OF IAM WITH THE LANCZOS ED METHOD

As described in Sec. IV, for the left and right resolvents of the major terms, it is clear that both the low-energy properties and asymptotic behavior can be accurately captured within the Lanczos scheme. For the resolvent in the center, however, excitations through the left and right resolvents must be

![](./images/817402235402059777_16.jpg)

FIG. 15. Comparison of the real part of the local four-point vertex function of the IAM obtained with various values of $N_{\alpha}$. In lower panel, Re $\gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}$ as a function of the Matsubara frequency $\omega_{n}$ is shown for $\omega^{\prime}=\pi / \beta$ and $v=4 \pi / \beta$. In upper panel, logarithmic plots of the relative difference between Re $\gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}$ obtained with $N_{\alpha}(=2,4,6$, and 8$)$ and that of $N_{\alpha}=10$ are presented [see Eq. (C2)]. The dashed line is the same as $N_{\alpha}=6$ but $\Omega_{6}$ is omitted in the calculation.

considered and in the present method those at the finite number of the reference energy points $\Omega_{\alpha}(\alpha=1,2, \ldots, N_{\alpha})$ are taken into account as the initial vectors of the band Lanczos method to generate the basis set to construct approximated resolvent [see Eq. (20)]. It is, therefore, important to know how many energy points are required to obtain well converged results within the present Lanczos algorithm. In this section, the convergence of the local four-point vertex function of the IAM with respect to the number of the energy points $N_{\alpha}$ is discussed as an example.

In the calculation, the IAM with $N_{\mathrm{b}}=7$ discretized conduction band levels in Eq. (39) is assumed. For the parameters of the IAM, $U=4, \beta=5$, and $\mu=2$ are adopted and the energies $\varepsilon_{i}^{\mathrm{b}}$ and hybridization strength $V_{i}$ of the discretized levels are $\varepsilon_{1,7}^{\mathrm{b}}= \pm 6$ with $V_{1,7}=0.55, \varepsilon_{2,6}^{\mathrm{b}}= \pm 3$ with $V_{2,6}=$ $0.9, \varepsilon_{3,5}^{\mathrm{b}}= \pm 1$ with $V_{3,5}=0.85$ and $\varepsilon_{4}^{\mathrm{b}}=0$ with $V_{4}=0.6$. These are about the values of the effective IAM of the DFA calculation of the 2D Hubbard model at half-filling with $U=$ $4, \beta=5$. The reference energy points chosen are $\Omega_{1}=0$, $\Omega_{N \alpha}=5.12 W$, and

$$
\Omega_{\alpha}=0.02 \times 2^{(\alpha-2)} W \quad\left(\alpha=2,3, \ldots, N_{\alpha}-1\right), \quad \text { (C1) }
$$

where $W=8.94 . \gamma_{\alpha}=0.1 W$ for all $\alpha$.

In lower panel of Fig. 15, the real part of $\gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}$ [refer Eqs. (29) and (30) for the definition] as a function of the Matsubara frequency $\omega_{n}$ is depicted for $\omega^{\prime}=\pi / \beta$ and $v=$ $4 \pi / \beta$. The convergence is very rapid and already Re $\gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}$ obtained with $N_{\alpha}=2$ is hardly distinguishable from the others with larger $N_{\alpha}$. To examine the accuracy of the results more closely, the relative differences between Re $\gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}$ obtained with $N_{\alpha}(=2,4,6$, and 8$)$ and that of $N_{\alpha}=10$ defined as

$$
\delta \gamma_{N_{a}}(\omega)=\frac{\left|\left(\operatorname{Re} \gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}\right)_{N \alpha}-\left(\operatorname{Re} \gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}\right)_{N \alpha=10}\right|}{\left|\left(\operatorname{Re} \gamma_{\omega \omega^{\prime} ; v}^{\uparrow \downarrow \uparrow \downarrow}\right)_{N \alpha=10}\right|} \quad(\mathrm{C} 2)
$$

are indicated as logarithmic plots in upper panel. About three digits accuracy can be found for the result with $N_{\alpha}=2$. The accuracy is improved to five digits for $N_{\alpha}=4$ and six digits or more for $N_{\alpha} \geqslant 6$. As mentioned in Sec. IV, it is essential to include one large energy point $\Omega_{\alpha} \gg E_{\max }-E_{l}$, i.e., $\Omega_{N_{a}}=$ $5.12 W$ in our example. Indeed, as shown by the dashed line in upper panel, the accuracy of the result drastically deteriorates from its counterpart, i.e., from six digits to less than three digits, when $\Omega_{6}$ is omitted in the calculation with the $N_{\alpha}=6$ reference points.

## APPENDIX D: COMPARISON OF DOS INFERRED BY THE PRESENT AND STANDARD MEMS

In the present study, the MEM adopted for the analytic continuation of the DOS and spectral functions is different from the standard method used in the majority of the previous studies [53]. As mentioned in Sec. VI, the differences can be boiled down to the three points: (i) not only the data of the Green's function on the imaginary axis but those on the complex plane indicated in Fig. 3 are used, (ii) the sum of squared relative errors in Eq. (46) is adopted for $\chi^{2}$ instead of the sum of squared absolute errors, and (iii) the standard deviation $\sigma=\alpha_{\chi}{ }^{-1 / 2}$ of the Gaussian function in Eq. (47) is not given as a parameter but inferred from the data as a hyperparameter $\alpha_{\chi}$.

The purpose of this section is to clarify to what extent these differences affect the results. The quality of the results can be assessed by comparing the DOS $\rho(\omega)$ directly inferred from the local Green's function $G_{\mathrm{loc}}\left(z_{n}\right)$ data by MEM to the DOS obtained from the summation of the spectral function $A_{k}(\omega)$ inferred from corresponding $G_{k}\left(z_{n}\right)$ data by MEM: $\rho(\omega)=$ $(1 / N) \sum_{k} A_{k}(\omega) . \rho(\omega)$ and $A_{k}(\omega)$ are treated as $N_{A}=512$ discretized data within the range of $-1.5 W<\omega<1.5 W$.

The LDFA results of DOS of the 2D Hubbard model with $U=4.0$ and various values of $\beta$ are shown in Fig. 16. The DOSs obtained with the present MEM are indicated in panel (a) and the results obtained with the points (i), (ii), and (iii) mentioned above being altered to those of the standard method are shown in panels (b), (c), and (d), respectively. The solid lines are the DOSs directly inferred from the $G_{\mathrm{loc}}\left(z_{n}\right)$ data by MEM and the dashed lines are those obtained from the summation of $A_{k}(\omega)$ inferred from corresponding $G_{k}\left(z_{n}\right)$ data by MEM.

The DOSs obtained directly from the $G_{\mathrm{loc}}\left(z_{n}\right)$ data by the present MEM are in good agreement with those obtained from the summation of $A_{k}(\omega)$ throughout the whole energy and temperature ranges as can be seen in panel (a). On the other hand, the deviations are apparent in the high-energy structures $(|\omega|>1)$ of the results in panel (b) and also those at the low temperatures in panel (c). The deviations are much larger in panel (d) and this is because the quasi-particle-like peaks appeared at the high-energy region in the spectral function,

205133-20

![](./images/817402235402059777_17.jpg)

FIG. 16. DOS $\rho(\omega)$ of the 2D Hubbard model for $U=4.0$ by means of LDFA with various value of $\beta$ obtained using the analytic continuation with the present MEM (a) and with partly modified versions of the present MEM (b)-(d). In (b), only the data of the Green's function on the imaginary axis (the number of the data is $N_{G}=256$) are used instead of those indicated in Fig. 3. In (c), the sum of squared absolute errors is assumed for $\chi^{2}$ instead of relative errors in Eq. (46). In (d), the standard deviation in Eq. (47) is fixed to $\sigma=\alpha_{\chi}^{-1 / 2}=5 \times 10^{-5}$ instead of optimizing hyperparameter $\alpha_{\chi}$ from the data. The solid lines are the DOSs directly inferred from $G_{\mathrm{loc}}(z_{n})$ data by MEM and the dashed lines are those obtained from the summation of $A_{k}(\omega)$ inferred from corresponding $G_{k}(z_{n})$ data set by MEM.

e.g., those placed near the $\Gamma$ point in Fig. 9, get too sharp with fixed $\sigma=5 \times 10^{-5}$ (estimated $\sigma$ at the $\Gamma$ point is one order larger in the case of the present MEM).

As discussed in Sec. IV and also demonstrated in Appendix C, the Lanczos ED method used in this study is the method which is accurate not only in the low-energy properties but also in the asymptotic behavior. Because of this feature, it is expected that one can infer more accurate DOS or spectral functions by exploiting high-energy information of the data: by using relative errors instead of absolute errors in Eq. (46) to give more weight to the data points on the high-energy side or by placing the data points not too far from the poles on the real axis as in Fig. 3 to avoid the loss of information. This explains why the present MEM can extract more accurate information of the DOS and spectral functions than the standard MEM.

[1] A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg, Rev. Mod. Phys. 68, 13 (1996).

[2] W. Metzner and D. Vollhardt, Phys. Rev. Lett. 62, 324 (1989).

[3] T. A. Maier, M. Jarrell, T. Prushke, and M. Hettler, Rev. Mod. Phys. 77, 1027 (2005).

[4] G. Rohringer, H. Hafermann, A. Toschi, A. A. Katanin, A. E. Antipov, M. I. Katsnelson, A. I. Lichtenstein, A. N. Rubtsov, and K. Held, Rev. Mod. Phys. 90, 025003 (2018).

[5] H. Kusunose, J. Phys. Soc. Jpn. 75, 054713 (2006).

[6] A. Toschi, A. A. Katanin, and K. Held, Phys. Rev. B 75, 045118 (2007).

[7] A. N. Rubtsov, M. I. Katsnelson, and A. I. Lichtenstein, Phys. Rev. B 77, 033101 (2008).

[8] A. N. Rubtsov, M. I. Katsnelson, A. I. Lichtenstein, and A. Georges, Phys. Rev. B 79, 045133 (2009).

[9] A. N. Rubtsov, M. I. Katsnelson, and A. I. Lichtenstein, Ann. Phys. 327, 1320 (2012).

[10] G. Rohringer, A. Toschi, H. Hafermann, K. Held, V. I. Anisimov, and A. A. Katanin, Phys. Rev. B 88, 115112 (2013).

[11] C. Taranto, S. Andergassen, J. Bauer, K. Held, A. Katanin, W. Metzner, G. Rohringer, and A. Toschi, Phys. Rev. Lett. 112, 196402 (2014).

[12] T. Ayral and O. Parcollet, Phys. Rev. B 92, 115109 (2015).

[13] G. Li, H. Lee, and H. Monien, Phys. Rev. B 78, 195105 (2008).

[14] H. Hafermann, K. R. Patton, and P. Werner, Phys. Rev. B 85, 205106 (2012).

[15] H. Hafermann, Phys. Rev. B 89, 235128 (2014).

[16] H. Shinaoka, J. Otsuki, K. Haule, M. Wallerberger, E. Gull, K. Yoshimi, and M. Ohzeki, Phys. Rev. B 97, 205111 (2018).

[17] H. Hafermann, C. Jung, S. Brener, M. I. Katsnelson, A. N. Rubtsov, and A. I. Lichtenstein, Europhys. Lett. 85, 27007 (2009).

[18] H. Hafermann, Numerical Approaches to Spatial Correlations in Strongly Interacting Fermion Systems (Cuvillier Verlag, Göttingen, 2010).

[19] G. Rohringer, A. Valli, and A. Toschi, Phys. Rev. B 86, 125114 (2012).

[20] A. Valli, T. Schäfer, P. Thunström, G. Rohringer, S. Andergassen, G. Sangiovanni, K. Held, and A. Toschi, Phys. Rev. B 91, 115115 (2015).
205133-21

[21] *Templates for the Solution of Algebraic Eigenvalue Problems: A Practical Guide*, edited by Z. Bai, J. Demmel, J. Dongarra, A. Ruhe, and H. van der Vorst (SIAM, Philadelphia, 2000).

[22] J. R. Schrieffer, X. G. Wen, and S. C. Zhang, *Phys. Rev. B* **39**, 11663 (1989).

[23] M. Vekić and S. R. White, *Phys. Rev. B* **47**, 1160 (1993).

[24] Y. M. Vilk and A.-M. S. Tremblay, *Europhys. Lett.* **33**, 159 (1996).

[25] Y. M. Vilk and A.-M. S. Tremblay, *J. Phys.* **17**, 1309 (1997).

[26] P. W. Anderson, *The Theory of Superconductivity in the High-*$T_c$ *Cuplates*, Princeton Series in Physics (Princeton University Press, NJ, 1997).

[27] S. Moukouri, S. Allen, F. Lemay, B. Kyung, D. Poulin, Y. M. Vilk, and A.-M. S. Tremblay, *Phys. Rev. B* **61**, 7887 (2000).

[28] F. Mancini, *Europhys. Lett.* **50**, 229 (2000).

[29] A. Avella, F. Mancini, and R. Münzner, *Phys. Rev. B* **63**, 245117 (2001).

[30] K. Borejsza and N. Dupuis, *Europhys. Lett.* **63**, 722 (2003).

[31] K. Borejsza and N. Dupuis, *Phys. Rev. B* **69**, 085119 (2004).

[32] J. E. Hirsch, *Phys. Rev. B* **31**, 4403 (1985).

[33] S. R. White, D. J. Scalapino, R. L. Sugar, E. Y. Loh, J. E. Gubernatis, and R. T. Scalettar, *Phys. Rev. B* **40**, 506 (1989).

[34] N. D. Mermin and H. Wagner, *Phys. Rev. Lett.* **17**, 1133 (1966).

[35] H. Park, K. Haule, and G. Kotliar, *Phys. Rev. Lett.* **101**, 186403 (2008).

[36] L. Fratino, P. Sémon, M. Charlebois, G. Sordi, and A.-M. S. Tremblay, *Phys. Rev. B* **95**, 235109 (2017).

[37] T. Schäfer, F. Geles, D. Rost, G. Rohringer, E. Arrigoni, K. Held, N. Blümer, M. Aichhorn, and A. Toschi, *Phys. Rev. B* **91**, 125109 (2015).

[38] E. G. C. P. van Loon, M. I. Katsnelson, and H. Hafermann, *Phys. Rev. B* **98**, 155117 (2018).

[39] T. Schäfer, A. Toschi, and K. Held, *J. Magn. Magn. Mater.* **400**, 107 (2016).

[40] D. Rost, E. V. Gorelik, F. Assaad, and N. Blümer, *Phys. Rev. B* **86**, 155109 (2012).

[41] E. H. Lieb and F. Y. Wu, *Phys. Rev. Lett.* **20**, 1445 (1968).

[42] H. Hafermann, G. Li, A. N. Rubtsov, M. I. Katsnelson, A. I. Lichtenstein, and H. Monien, *Phys. Rev. Lett.* **102**, 206401 (2009).

[43] E. G. C. P. van Loon, H. Hafermann, and M. I. Katsnelson, *Phys. Rev. B* **97**, 085125 (2018).

[44] J. Otsuki, H. Hafermann, and A. I. Lichtenstein, *Phys. Rev. B* **90**, 235132 (2014).

[45] T. Ribic, P. Gunacker, and K. Held, *Phys. Rev. B* **98**, 125106 (2018).

[46] S. Iskakov, A. E. Antipov, and E. Gull, *Phys. Rev. B* **94**, 035102 (2016).

[47] J. Gukelberger, E. Kozik, and H. Hafermann, *Phys. Rev. B* **96**, 035152 (2017).

[48] M. Capone, L. de' Medici, and A. Georges, *Phys. Rev. B* **76**, 245116 (2007).

[49] V. Heine in *Solid State Physics*, edited by H. Ehrenreich, F. Seitz, and D. Turnbull (Academic Press, New York, 1980), Vol. 35, p. 87.

[50] S. Brener, H. Hafermann, A. N. Rubtsov, M. I. Katsnelson, and A. I. Lichtenstein, *Phys. Rev. B* **77**, 195105 (2008).

[51] N. E. Bickers and S. R. White, *Phys. Rev. B* **43**, 8044 (1991).

[52] R. Žitko, *Phys. Rev. B* **80**, 125125 (2009).

[53] M. Jarrell and J. E. Gubernatis, *Phys. Rep.* **269**, 133 (1996).

[54] S. Moukouri and M. Jarrell, *Phys. Rev. Lett.* **87**, 167010 (2001).

[55] B. Kyung, J. S. Landry, D. Poulin, and A.-M. S. Tremblay, *Phys. Rev. Lett.* **90**, 099702 (2003).

[56] E. Gull, P. Werner, X. Wang, M. Troyer, and A. J. Millis, *Europhys. Lett.* **84**, 37009 (2008).

[57] L. F. Tocchio, F. Becca, and S. Sorella, *Phys. Rev. B* **94**, 195126 (2016).

[58] V. M. Galitskii and A. B. Migdal, *Zh. Eksp. Teor. Fiz.* **34**, 139 (1958) [JETP **7**, 96 (1958)].

[59] S. Chakravarty, B. I. Halperin, and D. R. Nelson, *Phys. Rev. Lett.* **60**, 1057 (1988).

[60] P. Hasenfratz and F. Niedermayer, *Phys. Lett. B* **268**, 231 (1991).

[61] E. Koch, G. Sangiovanni, and O. Gunnarsson, *Phys. Rev. B* **78**, 115102 (2008).

[62] J. P. F. LeBlanc, A. E. Antipov, F. Becca, I. W. Bulik, G. Kin- Lic Chan, C.-M. Chung, Y. Deng, M. Ferrero, T. M. Henderson, C. A. Jiménez-Hoyos, E. Kozik, X.-W. Liu, A. J. Millis, N. V. Prokof'ev, M. Qin, G. E. Scuseria, H. Shi, B. V. Svistunov, L. F. Tocchio, I. S. Tupitsyn, S. R. White, S. Zhang, B.-X. Zheng, Z. Zhu, and E. Gull, (Simons Collaboration on the Many-Electron Problem) *Phys. Rev. X* **5**, 041041 (2015).

[63] D. Sénéchal, D. Perez, and M. Pioro-Ladrière, *Phys. Rev. Lett.* **84**, 522 (2000).

[64] D. Sénéchal, D. Perez, and D. Plouffe, *Phys. Rev. B* **66**, 075129 (2002).

[65] A. A. Katanin, A. Toschi, and K. Held, *Phys. Rev. B* **80**, 075104 (2009).

[66] G. Rohringer and A. Toschi, *Phys. Rev. B* **94**, 125144 (2016).