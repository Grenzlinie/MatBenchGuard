# Superconductivity in a Two-Orbital Hubbard Model
with Electron and Hole Fermi Pockets:
Application in Iron Oxypnictide Superconductors

Kazuhiro SANO* and Yoshiaki ŌNO¹,²

Department of Physics Engineering, Mie University, Tsu 514-8507
¹Department of Physics, Niigata University, Niigata 950-2181
²Center for Transdisciplinary Research, Niigata University, Niigata 950-2181

(Received June 26, 2009; accepted October 1, 2009; published December 10, 2009)

We investigate the electronic states of a one-dimensional two-orbital Hubbard model with band splitting by the exact diagonalization method. The Luttinger liquid parameter $K_{\rho}$ is calculated to obtain superconducting (SC) phase diagram as a function of on-site interactions: the intra- and inter-orbital Coulomb $U$ and $U'$, the Hund coupling $J$, and the pair transfer $J'$. In this model, electron and hole Fermi pockets are produced when the Fermi level crosses both the upper and lower orbital bands. We find that the system shows two types of SC phases, the SC I for $U > U'$ and the SC II for $U < U'$, in the wide parameter region including both weak and strong correlation regimes. Pairing correlation functions indicate that the most dominant pairing for the SC I (SC II) is the intersite (on-site) intraorbital spin-singlet with (without) sign reversal of the order parameters between two Fermi pockets. The result of the SC I is consistent with the sign-reversing $s$-wave pairing that has recently been proposed for iron oxypnictide superconductors.

KEYWORDS: iron oxypnictide superconductors, two-orbital Hubbard model, pairing symmetry, exact diagonalization

DOI: 10.1143/JPSJ.78.124706

## 1. Introduction
The recent discovery of iron oxypnictide superconductors¹⁻⁵ with transition temperatures of up to $T_{\mathrm{c}} \sim 55\,K$ has stimulated much interest in the relationship between the mechanism of the superconductivity and the orbital degrees of freedom. First-principles calculations have predicted the band structure with hole Fermi pockets around the $\Gamma$ point and electron Fermi pockets around the $M$ point.⁶⁻⁸ By using the weak-coupling approaches based on multiorbital models, the spin-singlet $s$-wave pairing is predicted, where the order parameter of this pairing changes its sign between hole and electron Fermi pockets (sign-reversing $s$-wave pairing).⁹⁻¹³ This unconventional $s$-wave pairing is expected to emerge owing to the effect of antiferromagnetic spin fluctuations. Since the strong correlation between electrons is considered to play an important role in the superconductivity of iron oxypnictides as well as in that of high-$T_{\mathrm{c}}$ cuprates, nonperturbative and reliable approaches are required.

As a nonperturbative approach, the exact diagonalization (ED) method has been extensively applied in the Hubbard, $d$-$p$, and $t$-$J$ models.¹⁴,¹⁵ Although these models are much simplified and mostly limited to one dimension, it has elucidated some important effects of a strong correlation on superconductivity. Using the ED method, we have studied the one-dimensional (1D) two-orbital Hubbard model in the presence of the band splitting $\Delta$. It is found that the superconducting (SC) phase appears in the vicinity of the partially polarized ferromagnetism when the exchange (Hund's rule) coupling $J$ is larger than its critical value on the order of $\Delta$.¹⁶ The result suggests that spin triplet pairing emerges owing to the effect of ferromagnetic spin fluctuation. In the case of $\Delta = 0$, spin triplet superconductivity has also been discussed on the basis of bosonization¹⁷⁻¹⁹ and numerical²⁰⁻²² approaches. Previous works, however, were restricted to the case of a single Fermi surface, and the effects of electron and hole Fermi pockets on superconductivity have not been discussed therein.

In this study, we investigate the 1D two-orbital Hubbard model with electron and hole Fermi pockets, where the Fermi level crosses both the upper and lower bands in the presence of a finite band splitting $\Delta$. Using the ED method, the Luttinger liquid parameter $K_{\rho}$ is calculated to obtain the SC phase diagram as a function of on-site Coulomb interactions in a wide parameter region including both weak- and strong-correlation regimes. It would clarify the effects of a strong correlation on superconductivity in iron oxypnictides. We also calculate various pairing correlation functions and discuss a possible pairing symmetry. Although our model is much simplified and limited to one dimension, we expect that the essence of the superconducting mechanism of iron oxypnictides can be discussed.

## 2. Model and Formulation
We consider the one-dimensional two-orbital Hubbard model given by the following Hamiltonian:

$$
\begin{aligned}
H =& t \sum_{i,m,\sigma} (c_{i,m,\sigma}^{\dagger} c_{i+1,m,\sigma} + \mathrm{h.c.}) \\
&+ \frac{\Delta}{2} \sum_{i,\sigma} (n_{i,u,\sigma} - n_{i,l,\sigma}) + U \sum_{i,m} n_{i,m,\uparrow} n_{i,m,\downarrow} \\
&+ U' \sum_{i,\sigma} n_{i,u,\sigma} n_{i,l,-\sigma} + (U' - J) \sum_{i,\sigma} n_{i,u,\sigma} n_{i,l,\sigma} \\
&- J \sum_{i} (c_{i,u,\uparrow}^{\dagger} c_{i,u,\downarrow}^{\dagger} c_{i,l,\downarrow} c_{i,l,\uparrow} + \mathrm{h.c.}) \\
&- J' \sum_{i} (c_{i,u,\uparrow}^{\dagger} c_{i,u,\downarrow}^{\dagger} c_{i,l,\uparrow} c_{i,l,\downarrow} + \mathrm{h.c.}),
\end{aligned} \tag{1}
$$

*E-mail: sano@phen.mie-u.ac.jp

124706-1

![](./images/811817429234614274_1.jpg)

Fig. 1. Schematic diagrams of (a) the model Hamiltonian, (b) the band structure in the noninteracting case, and (c) a corresponding two- dimensional Fermi surface related to our 1D model.

where $c_{i,m,\sigma}^{\dagger}$ stands for the creation operator of an electron with a spin $\sigma$ ($= \uparrow, \downarrow$) and an orbital $m$ ($= u, l$) at site $i$ and $n_{i,m,\sigma}=c_{i,m,\sigma}^{\dagger}c_{i,m,\sigma}$. Here, $t$ represents the hopping integral between the same orbitals and we set $t = 1$ in this study. The interaction parameters $U, U', J$, and $J'$ stand for the intra- and inter-orbital direct Coulomb interactions, exchange (Hund's rule) coupling, and pair-transfer, respectively. $\Delta$ denotes the energy difference between the two atomic orbitals. For simplicity, we impose the relation $J = J'$.

The model in eq. (1) is schematically shown in Fig. 1(a). In a noninteracting case ($U = U' = J = 0$), the Hamiltonian eq. (1) yields dispersion relations representing the upper and lower band energies: $\epsilon^{u}(k)=2t\cos k+(\Delta/2)$ and $\epsilon^{l}(k)=2t\cos k-(\Delta/2)$, where $k$ is the wave vector. This band structure is schematically shown in Fig. 1(b). When the Fermi level $E_{k_{\mathrm{F}}}$ crosses both the upper and lower bands, the system is metallic with electron and hole Fermi pockets corresponding to a characteristic band structure of the FeAs plane in iron oxypnictides, as shown in Fig. 1(c).

We numerically diagonalize the model Hamiltonian up to 6 sites (12 orbitals) and estimate the Luttinger liquid parameter $K_{\rho}$ from the ground-state energy of finite-size systems using the standard Lanczos algorithm. $^{14)}$ To reduce the finite size effect, we impose the boundary condition (periodic or antiperiodic) on upper and lower orbitals independently and chose both boundary conditions to minimize $|K_{\rho}^{0}-1|$, where $K_{\rho}^{0}$ represents the $K_{\rho}$ of the finite-size system in a noninteracting case. The typical deviation of $K_{\rho}$ from unity becomes about $\sim 0.1$ for a six-site system. For simplicity, we will redefine $K_{\rho}$ as a renormalize value calculated using $K_{\rho}/K_{\rho}^{0}$, hereafter.

On the basis of the Tomonaga-Luttinger liquid theo- ry, $^{23-27)}$ various types of correlation functions are determined by the single parameter $K_{\rho}$ in the model which is isotropic in spin space. For a single-band model with two Fermi points, $\pm k_{\mathrm{F}}$, the SC correlation function decays as $\sim r^{-[1+(1/K_{\rho})]}$, while the CDW and SDW correlation functions decay as $\sim \cos(2k_{\mathrm{F}}r)r^{-(1+K_{\rho})}$. Thus, the SC correlation is dominant for $K_{\rho}>1$, while the CDW or SDW correlation is dominant for $K_{\rho}<1$. On the other hand, for a two-band model with four Fermi points, i.e., $\pm k_{\mathrm{F}_{1}}$ and $\pm k_{\mathrm{F}_{2}}$, low-energy excitations are given by a single gapless charge mode with a gapped spin mode. $^{26-28)}$ In this case, the SC and CDW correlations decay as $\sim r^{-1/2K_{\rho}}$ and $\sim \cos[2(k_{\mathrm{F}_{2}}-k_{\mathrm{F}_{1}})r]r^{-2K_{\rho}}$, respectively, while the SDW correlation decays exponentially. Hence, the SC correlation is dominant for $K_{\rho}>0.5$, while the CDW correlation is dominant for $K_{\rho}<0.5$. In either case, the SC correlation increases with the exponent $K_{\rho}$, and then $K_{\rho}$ is regarded as a good indicator of superconductivity. $^{29)}$ As the noninteracting $K_{\rho}$ is always unity, we assume that the condition of $K_{\rho}>1$ for our model corresponds to the superconducting state realized in oxy- pnictide superconductors.

## 3. Phase Diagram

Figure 2 shows $K_{\rho}$ as a function of $U'$ for several values of $\Delta$ at an electron density $n = 5/3$ (10 electrons/6 sites), where we set $J = U'/4$ with $U = U' + 2J$. When $U'$ increases, $K_{\rho}$ decreases for a small $U'$, while it increases for a large $U'$ in the case of $\Delta \geq 1.9$, and then becomes larger than unity for $U'>2.3$ in the case of $\Delta=1.9$. When $J$ ($= U'/4$) is larger than a certain critical value, the ground state changes into the partially polarized ferromagnetic state with a total spin $S = 1$ from the singlet state with $S = 0$. We find that superconductivity is most enhanced in the vicinity of the partially polarized ferromagnetic state. To confirm superconductivity, we calculate the energy difference of the ground state, $E_{0}(\phi)-E_{0}(0)$, as a function of the external flux $\phi$. As shown in the inset of Fig. 2, anomalous flux quantization is clearly observed for $\Delta=1.9$ while not for $\Delta=0.8$.

In Fig. 3, we show the phase diagram of the ground state on the $U'-J$ parameter plane under the condition of $U = U'+2J$ for $n = 5/3$ (10 electrons/6 sites) at $\Delta=1.9$. It contains the singlet state with $S = 0$ together with partially polarized ferromagnetic states with $S = 1$ and $S = 2$. The

![](./images/811817429234614274_2.jpg)

Fig. 2. $K_{\rho}$ as a function of $U'(=4J)$ for $n = 5/3$ (10 electrons/6 sites) at $\Delta=0.8,1.6,1.9,2.3$, and 2.8. The singlet ground state changes into a partially polarized ferromagnetic ($S = 1$) state at $U'\simeq 2.5,3.2$, and 4.1 for $\Delta=1.9,2.3$, and 2.8, respectively. The inset shows the energy difference $E_{0}(\phi)-E_{0}(0)$ as a function of the external flux $\phi$ for $n = 2/3$ (6 electrons/9 sites) at $\Delta=1.2$.

124706-2

![](./images/811817429234614274_3.jpg)

Fig. 3. Phase diagram of the ground state with $K_{\rho}$ on the $U'-J$ parameter plane with $U = U'+2J$ for $n = 5/3$ (10 electrons/6 sites) at $\Delta = 1.9$.

![](./images/811817429234614274_4.jpg)

Fig. 4. Phase diagram of the ground state with $K_{\rho}$ on the $U-U'$ parameter plane with $J = U'/4$ for $n = 5/3$ (10 electrons/6 sites) at $\Delta = 1.9$.

singlet state with $K_{\rho} > 1$, where we call it the SC phase, appears near the partially polarized ferromagnetic region at $J \gtrsim U'$. It extends from the attractive region ($U' < 0$) to the realistic parameter region with $J \sim U'/4 > 0$, which is expected to correspond to that in the case of iron oxypnictides.⁸) We have confirmed that similar phase diagrams are also obtained for $\Delta = 2.3$ and 2.6.

Figure 4 shows the phase diagram of the ground state on the $U-U'$ plane under the condition of $J = U'/4$ for $n = 5/3$ (10 electrons/6 sites) at $\Delta = 1.9$. We observe two types of SC phases with $K_{\rho} > 1$, the SC I for $U > U'$ and the SC II for $U < U'$, in the wide parameter region including both weak- and strong-correlation regimes. Note that the SC I corresponds to the SC phase shown in Fig. 3 and belongs to the realistic parameter region mentioned before.

## 4. Pairing Correlation

To examine the nature of these SC phases, we calculate SC pairing correlation functions for the various types of pairing symmetries schematically shown in Fig. 5. Explicit forms of the SC pairing correlation functions $C(r)$ are given by

$$
S_{\mathrm{on}}^{\mathrm{l}}(r)=\frac{1}{N} \sum_{i}\left\langle c_{i, l, \uparrow}^{\dagger} c_{i, l, \downarrow}^{\dagger} c_{i+r, l, \downarrow} c_{i+r, l, \uparrow}\right\rangle,
$$

$$
S_{\mathrm{on}}^{\mathrm{u}}(r)=\frac{1}{N} \sum_{i}\left\langle c_{i, u, \uparrow}^{\dagger} c_{i, u, \downarrow}^{\dagger} c_{i+r, u, \downarrow} c_{i+r, u, \uparrow}\right\rangle,
$$

![](./images/811817429234614274_5.jpg)

Fig. 5. Schematic diagrams of various types of superconducting pairing symmetries, $S_{\mathrm{on}}^{\mathrm{l}}, S_{\mathrm{on}}^{\mathrm{u}}, S_{\mathrm{nn}}^{\mathrm{l}}, S_{\mathrm{nn}}^{\mathrm{u}}$, and $S_{\mathrm{on}}^{\mathrm{lu}}$ with spin singlet pairings and $T_{\mathrm{nn}}^{\mathrm{l}}$, $T_{\mathrm{nn}}^{\mathrm{u}}$, and $T_{\mathrm{on}}^{\mathrm{lu}}$ with spin triplet pairings.

$$
\begin{aligned}
S_{\mathrm{nn}}^{\mathrm{l}}(r)= & \frac{1}{2 N} \sum_{i}\left\langle\left(c_{i, l, \uparrow}^{\dagger} c_{i+1, l, \downarrow}^{\dagger}-c_{i, l, \downarrow}^{\dagger} c_{i+1, l, \uparrow}^{\dagger}\right)\right. \\
& \left.\times\left(c_{i+r+1 \downarrow} c_{i+r, l, \uparrow}-c_{i+r+1, l, \uparrow} c_{i+r, l, \downarrow}\right)\right\rangle,
\end{aligned}
$$

$$
\begin{aligned}
S_{\mathrm{nn}}^{\mathrm{u}}(r)= & \frac{1}{2 N} \sum_{i}\left\langle\left(c_{i, u, \uparrow}^{\dagger} c_{i+1, u, \downarrow}^{\dagger}-c_{i, u, \downarrow}^{\dagger} c_{i+1, u, \uparrow}^{\dagger}\right)\right. \\
& \left.\times\left(c_{i+r+1, u, \downarrow} c_{i+r, u, \uparrow}-c_{i+r+1, u, \uparrow} c_{i+r, u, \downarrow}\right)\right\rangle,
\end{aligned}
$$

$$
\begin{aligned}
S_{\mathrm{on}}^{\mathrm{lu}}(r)= & \frac{1}{2 N_{u}} \sum_{i}\left\langle\left(c_{i, l, \uparrow}^{\dagger} c_{i, u, \downarrow}^{\dagger}-c_{i, l, \downarrow}^{\dagger} c_{i, u, \uparrow}^{\dagger}\right)\right. \\
& \left.\times\left(c_{i+r, u, \downarrow} c_{i+r, l, \uparrow}-c_{i+r, u, \uparrow} c_{i+r, l, \downarrow}\right)\right\rangle,
\end{aligned}
$$

$$
\begin{aligned}
T_{\mathrm{nn}}^{\mathrm{l}}(r)= & \frac{1}{2 N_{u}} \sum_{i}\left\langle\left(c_{i, l, \uparrow}^{\dagger} c_{i+1, l, \downarrow}^{\dagger}+c_{i, l, \downarrow}^{\dagger} c_{i+1, l, \uparrow}^{\dagger}\right)\right. \\
& \left.\times\left(c_{i+r+1 \downarrow} c_{i+r, l, \uparrow}+c_{i+r+1, l, \uparrow} c_{i+r, l, \downarrow}\right)\right\rangle,
\end{aligned}
$$

$$
\begin{aligned}
T_{\mathrm{nn}}^{\mathrm{u}}(r)= & \frac{1}{2 N_{u}} \sum_{i}\left\langle\left(c_{i, u, \uparrow}^{\dagger} c_{i+1, u, \downarrow}^{\dagger}+c_{i, u, \downarrow}^{\dagger} c_{i+1, u, \uparrow}^{\dagger}\right)\right. \\
& \left.\times\left(c_{i+r+1, u, \downarrow} c_{i+r, u, \uparrow}+c_{i+r+1, u, \uparrow} c_{i+r, u, \downarrow}\right)\right\rangle,
\end{aligned}
$$

$$
\begin{aligned}
T_{\mathrm{on}}^{\mathrm{lu}}(r)= & \frac{1}{2 N_{u}} \sum_{i}\left\langle\left(c_{i, l, \uparrow}^{\dagger} c_{i, u, \downarrow}^{\dagger}+c_{i, l, \downarrow}^{\dagger} c_{i, u, \uparrow}^{\dagger}\right)\right. \\
& \left.\times\left(c_{i+r, u, \downarrow} c_{i+r, l, \uparrow}+c_{i+r, u, \uparrow} c_{i+r, l, \downarrow}\right)\right\rangle,
\end{aligned}
$$

where $S_{\mathrm{on}}^{\mathrm{l}}(r)$, $S_{\mathrm{on}}^{\mathrm{u}}(r)$, $S_{\mathrm{nn}}^{\mathrm{l}}(r)$, $S_{\mathrm{nn}}^{\mathrm{u}}(r)$, and $S_{\mathrm{on}}^{\mathrm{lu}}(r)$ denote the singlet pairing correlation functions on the same site in the lower orbital, on the same site in the upper orbital, between nearest-neighbor sites in the lower orbital, between nearest-neighbor sites in the upper orbital, and between the lower and upper orbitals on the same site, respectively. Furthermore, $T_{\mathrm{nn}}^{\mathrm{l}}(r)$, $T_{\mathrm{nn}}^{\mathrm{u}}(r)$, and $T_{\mathrm{on}}^{\mathrm{lu}}(r)$ are the triplet pairing correlation functions between nearest-neighbor sites in the lower orbital, between nearest-neighbor sites in the upper orbital, and between the lower and upper orbitals on the same site, respectively.

In Fig. 6, we show the absolute values of various types of SC pairing correlation functions $|C(r)|$ for $n = 5/3$ (10 electrons/6 sites) at $\Delta = 1.9$, $U' = 4$, $J = 1.0$, and $U = -0.4$. Here, the electronic state of the system belongs to the SC II phase, although the phase diagram for $U < 0$ is not explicitly shown in Fig. 4. Note that $|T_{\mathrm{nn}}^{\mathrm{u}}(r)| < 10^{-4}$ and $S_{\mathrm{on}}^{\mathrm{lu}}(r = 3)=T_{\mathrm{on}}^{\mathrm{lu}}(r = 3)=0$, which are not shown in Fig. 6. We find that $S_{\mathrm{on}}^{\mathrm{u}}(r)$ and $S_{\mathrm{nn}}^{\mathrm{u}}(r)$ decay very slowly as functions

124706-3

![](./images/811817429234614274_6.jpg)

Fig. 6. Absolute values of various types of SC pairing correlation functions $|C(r)|$ as functions of $r$ for $n=5/3$ (10 electrons/6 sites) at $\Delta=1.9$, $U'(=4J)=1.0$, and $U=-0.4$, corresponding to the SC II phase.

![](./images/811817429234614274_7.jpg)

Fig. 7. Absolute values of various types of SC pairing correlation functions $|C(r)|$ as functions of $r$ for $n=5/3$ (10 electrons/6 sites) at $\Delta=1.9$, $U'(=4J)=1.0$, and $U=2.4$, corresponding to the SC I phase.

of $r$, and $|S_{\text{on}}^{\text{u}}(r=3)|$ is the largest among the various $|C(r=3)|$ values. Therefore, a relevant pairing symmetry for the SC II phase seems to be the spin singlet pairing in the upper orbital band, mainly consist of "on-site" pairing. It is considered that such a pairing in attractive region with $U<0$ is due to the intra-orbital attraction $U$. On the other hand, in repulsive region with $U'>U>0$, the pairing may be due to charge fluctuation, which is enhanced by a large inter-orbital repulsion $U'$ similarly to that in the case of the $d$-$p$ model in the presence of the inter-orbital repulsion $U_{pd}.^{30)}$

Next, we discuss the superconductivity in the SC I phase including the realistic parameter region mentioned before. Figure 7 shows the absolute values of various types of SC pairing correlation functions $|C(r)|$ for $n=5/3$ (10 electrons/6 sites) at $\Delta=1.9$, $U'=4J=1.0$, and $U=2.4$, where the system belongs to the SC I phase, as shown in Fig. 4. Here, $|T_{\text{nn}}^{\text{u}}(r)|$, $|S_{\text{on}}^{\text{lu}}(r=3)|$, and $|T_{\text{on}}^{\text{lu}}(r=3)|$ are not shown, because these correlation functions are very small or zero. We find that $|S_{\text{on}}^{\text{l}}(r)|$ is considerably suppressed compared with $|S_{\text{nn}}^{\text{u}}(r)|$ in contrast to that in the case of the SC II phase. Furthermore, $|S_{\text{nn}}^{\text{l}}(r)|$ increases with increasing $r$ except at $r=2$. Therefore, the relevant pairing symmetry for the SC I phase seems to be an extended spin singlet pairing, and mainly consist of nearest-neighbor site pairing.

![](./images/811817429234614274_8.jpg)

Fig. 8. Pairing correlation functions $S_{\text{nn}}^{\text{l-u}}(r)$ and $T_{\text{nn}}^{\text{l-u}}(r)$. Here, we show the absolute value of the correlation functions at $U=2.4$, $\Delta=1.9$, and $U'(=4J)=1.0$ for $n=5/3$ (10 electrons/6 sites). The inset shows a schematic diagram of the pairing symmetries, $S_{\text{nn}}^{\text{l-u}}(r)$ and $T_{\text{nn}}^{\text{l-u}}(r)$.

Recently, weak-coupling approaches such as RPA and perturbation expansions have shown that the sign-reversing $s$-wave ($s_{\pm}$-wave) pairing is realized in iron oxypnictide superconductors. $^{9-13)}$ The order parameter of such a pairing is considered to change its sign between hole and the electron Fermi pockets. To compare our result with the result obtained by weak-coupling approaches, we examine the SC pairing correlation function between the lower and upper orbitals, such as

$$
S_{\text{nn}}^{\text{l-u}}(r)=\frac{1}{2N}\sum_{i}\langle\Delta_{\text{nn}}^{l}(i)^{\dagger}\Delta_{\text{nn}}^{u}(i+r)\rangle
$$

with

$$
\Delta_{\text{nn}}^{m}(i)^{\dagger}=c_{i,m,\uparrow}^{\dagger}c_{i+1,m,\downarrow}^{\dagger}-c_{i,m,\downarrow}^{\dagger}c_{i+1,m,\uparrow}^{\dagger}\ (m=l,u).
$$

We also define $T_{\text{nn}}^{\text{l-u}}(r)$ as well as $S_{\text{nn}}^{\text{l-u}}(r)$ in the above equation.

When the $s_{\pm}$-wave pairing is dominant, the values of the interorbital SC pairing correlation function are expected to be negative, since the Fermi surface of the lower (upper) orbital band in our model corresponds to a hole (electron) Fermi pocket, as shown in Fig. 1(b). In Fig. 8, we show the interorbital pairing correlation functions $S_{\text{nn}}^{\text{l-u}}(r)$ and $T_{\text{nn}}^{\text{l-u}}(r)$ (see also inset) for the same parameters in Fig. 4 corre- sponding to the SC I phase. We see that the values of $T_{\text{nn}}^{\text{l-u}}(r)$ are positive and very small, while those of $S_{\text{nn}}^{\text{l-u}}(r)$ are negative except at $r=3$ and not so small. This result suggests that the relevant pairing symmetry of the SC I phase is the spin-singlet $s_{\pm}$-wave pairing, which agrees with the result of the weak coupling approaches. Therefore, we expect that the $s_{\pm}$-wave pairing proposed on the basis of the result of weak-coupling approaches is realized in the wide parameter region including both weak- and strong-correla- tion regimes.

Finally, we discuss the mechanism of superconductivity in the SC I phase. The $s_{\pm}$-wave pairing is considered to be mediated by the antiferromagnetic fluctuation due to the nesting effect between electron and hole pockets. $^{9-13)}$ At first glance, the SC I phase is located adjacent to the partial ferromagnetic phase $(S=1)$, and then, the ferromagnetic fluctuation seems to be related to superconductivity. To examine the relationship between spin fluctuation and

124706-4

superconductivity, we also calculate the spin correlation function for finite-size systems, where a short-range spin correlation is considered to be crucial for the superconduc- tivity. We obtain the ferromagnetic and antiferromagnetic components of the spin correlation as a function of $U'$ $(=4J)$ for a fixed $U=1.5$ (see also Fig. 4) and find that antiferromagnetic (ferromagnetic) correlation increases(decreases) with decreasing $U'$ together with increasing $K_{\rho}$ (not shown). Therefore, we conclude that the antiferromag- netic spin fluctuation is responsible for the $s_{\pm}$-wave pairing in the SC I phase.

## 5. Summary and Discussion
We have investigated the superconductivity of the one- dimensional two-orbital Hubbard model in the case of electron and hole Fermi pockets corresponding to a characteristic band structure of iron oxypnictide super- conductors. To obtain reliable results including those in the strong-correlation regime, we used the exact diagonal- ization method and calculated the critical exponent $K_{\rho}$ on the basis of the Luttinger liquid theory. It has been found that the system shows two types of SC phases, the SC I for $U>U'$ and the SC II for $U<U'$ , in the wide param eter region including both weak- and strong-correlation regimes.

We have also calculated various types of SC pairing correlation functions in the realistic parameter region of the iron oxypnictides. The result indicates that the most dominant pairing for the SC I phase is the intersite intra- orbital spin-singlet with sign reversal of the order parameters between two Fermi pockets. The result is consistent with the sign-reversing $s_{\pm}$-wave pairing that has recently been proposed on the basis of the result obtained by weak- coupling approaches for iron oxypnictide superconductors. This indicates that the $s_{\pm}$-wave pairing is realized not only in a weak-correlation regime but also in a strong- correlation regime. We have also calculated the spin correlation function and found that antiferromagnetic spin fluctuation is responsible for the $s_{\pm}$-wave pairing in the SC I phase.

As for the SC II phase, the most dominant pairing is found to be the on-site intraorbital spin-singlet pairing, which is consistent with the ordinary $s$-wave pairing of BCS super conductors. However, the superconducting mechanism of this phase is due to the charge fluctuation enhanced by the interorbital Coulomb interaction and is different from the conventional BCS superconductivity due to the electron- phonon interaction. Although the SC II phase seems to be realized only for the unrealistic parameter region in our model, it might be realized for a realistic parameter region in the $d-p$ model, which is closer to iron oxypnictides. $^{13,30)}$ We will address such a problem by applying the present method in the $d-p$ model in the future.

1) Y. Kamihara, T. Watanabe, M. Hirano, and H. Hosono: J. Am. Chem. Soc. 130 (2008) 3296.
2) Z.-A. Ren, W. Lu, J. Yang, W. Yi, X.-L. Shen, Z.-C. Li, G.-C. Che,X.-L. Dong, L.-L. Sun, F. Zhou, and X.-X. Zhao: Chin. Phys. Lett. 25(2008)2215.
3) X. H. Chen, T. Wu, G. Wu, R. H. Liu, H. Chen, and D. F. Fang: Nature453 (2008) 761.
4) G. F. Chen, Z. Li, D. Wu, G. Li, W. Z. Hu, J. Dong, P. Zheng, J. L. Luo, and N. L. Wang: Phys. Rev. Lett. 100 (2008) 247002.
5) H. Kito, H. Eisaki, and A. Iyo: J. Phys. Soc. Jpn. 77 (2008) 063707.
6) D. J. Singh and M. H. Du: Phys. Rev. Lett. 100 (2008) 237003.
7) S. Ishibashi, K. Terakura, and H. Hosono: J. Phys. Soc. Jpn. 77 (2008)053709
8) K. Nakamura, R. Arita, and M. Imada: J. Phys. Soc. Jpn. 77 (2008)093711.
9) K. Kuroki, S. Onari, R. Arita, H. Usui, Y. Tanaka, H. Kontani, and H. Aoki: Phys. Rev. Lett. 101 (2008) 087004.
10) I. I. Mazin, D. J. Singh, M. D. Johannes, and M. H. Du: Phys. Rev. Lett. 101 (2008) 057003.
11) F. Wang, H. Zhai, Y. Ran, A. Vishwanath, and D.-H. Lee: Phys. Rev. Lett. 102 (2009) 047005.
12) T. Nomura: J. Phys. Soc. Jpn. 78 (2009) 034716; T. Nomura: Proc. IntSymp. Fe-Pnictide Superconductors, J. Phys. Soc. Jpn. 77 (2008) Suppl. C, p. 123.
13) Y. Yanagi, Y. Yamakawa, and Y. Ono: J. Phys. Soc. Jpn. 77 (2008)123701; Y. Yanagi, Y. Yamakawa, and Y. Ono: Proc. Int. Symp. Fe-Pnictide Superconductors, J. Phys. Jpn. 77 (2008) Suppl. C, p.149.
14) H. J. Schulz: Phys. Rev. Lett. 64 (1990) 2831; A. Sudb, C. M. Varma,T. Giamarchi, E. B. Stechel, and T. Scalettar: Phys. Rev. Lett. 70(1993) 978; M. Ogata, M. U. Luchini, S. Sorella, and F. F. Assaad: Phys. Rev. Lett. 66 (1991) 2388.
15) C. A. Hayward, D. Poilblanc, R. M. Noack, D. J. Scalapino, and W. Hanke: Phys. Rev. Lett. 75 (1995) 926; D. Poilblanc, D. J. Scalapino, and W. Hanke: Phys. Rev. B 52 (1995) 6796; K. Sano: J. Phys. Soc. Jpn. 65 (1996) 1146.
16) K. Sano and Y. Ono: J. Phys. Soc. Jpn. 72 (2003) 1847; K. Sano and Y. Ono: J. Phys.: Condens. Matter 19 (2007) 145284.
17) D. G. Shelton and A. M. Tsvelik: Phys. Rev. B 53 (1996) 14036.
18) S. Q. Shen: Phys. Rev. B 57 (1998) 6474.
19) H. C. Lee, P. Azaria, and E. Boulat: Phys. Rev. B 69 (2004) 155109.
20) H. Sakamoto, T. Momoi, and K. Kubo: Phys. Rev. B 65 (2002)224403.
21) T. Shirakawa, Y. Ohta, and S. Nishimoto: J. Magn. Magn. Mater. 310(2007)663.
22) K. Sano and Y. Ono: J. Magn. Magn. Mater. 310 (2007) e319.
23) J. Solyom: Adv. Phys. 28 (1979) 201.
24) J. Voit: Rep. Prog. Phys. 58 (1995) 977.
25) V. J. Emery: in Highly Conducting One-Dimensional Solids, ed. J. T. Devreese, R. Evrand, and V. van Doren (Plenum, New York, 1979) p.327.
26) L. Balentz and M. P. A. Fisher: Phys. Rev. B 53 (1996) 12133.
27) M. Fabrizio: Phys. Rev. B 54 (1996) 10054.
28) V. J. Emery, S. A. Kivelson, and O. Zachar: Phys. Rev. B 59 (1999)15641.
29) The noninteracting band structure for the present model is almost equivalent to that for the ladder model, which has electron and hole Fermi pockets during moderate band splitting and filling. Results obtained using numerical methods such as the ED and DMRG indicate that the electronic state of the ladder model can be analyzed well usingthe weak-coupling theory except in a strong-coupling limit. $^{15)}$
30) K. Sano and Y. Ono: Physica C 205 (1993) 170; K. Sano and Y. Ono:Phys. Rev. B 51 (1995) 1175; K. Sano and Y. Ono: Physica C 242(1995)113.

---
124706-5