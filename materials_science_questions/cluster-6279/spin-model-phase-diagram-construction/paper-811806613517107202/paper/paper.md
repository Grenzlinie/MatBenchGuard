# Monte Carlo Study of Relaxor Systems:
## A Minimum Model of $\boldsymbol{Pb(In_{1/2}Nb_{1/2})O_3}$

Yusuke TOMITA*, Takeo KATO, and Kazuma HIROTA¹

Institute for Solid State Physics, University of Tokyo, Kashiwa, Chiba 277-8581, Japan
¹Department of Earth and Space Science, Faculty of Science, Osaka University, Toyonaka, Osaka 560-0043, Japan

(Received November 3, 2009; accepted December 15, 2009; published February 10, 2010)

We examine a simple model of $Pb(In_{1/2}Nb_{1/2})O_3$ (PIN), which includes both long-range dipole–dipole interaction and random local anisotropy. An improved algorithm optimized for long-range interaction has been applied to efficient large-scale Monte Carlo simulation. We demonstrate that the phase diagram of PIN is qualitatively reproduced by this minimum model. Some characteristic features of relaxors such as nanoscale domain formation, slow dynamics, and dispersive dielectric responses are also examined.

**KEYWORDS:** relaxors, ferroelectric phase transition, antiferroelectric phase transition, Monte Carlo algorithm, domain formation, slow dynamics, dispersive dielectric responses, $Pb(In_{1/2}Nb_{1/2})O_3$

DOI: 10.1143/JPSJ.79.023001

Relaxors, whose first discovery dates back to over half a century ago,¹⁾ have newly attracted much interest over the past few decades owing to their colossal dielectric and piezoelectric responses that are appealing for industrial applications. Despite intensive research, however, the physical origin of the unusual properties of relaxors is not fully understood yet.²⁾ This is because nanoscale intrinsic randomness in relaxor systems has to be addressed appropriately.

As a simple example to understand the physics of relaxors, let us choose the lead-based relaxor Pb-$(In_{1/2}Nb_{1/2})O_3$ (PIN), which is the target of the present theoretical work. The intrinsic inhomogeneities of relaxor systems originate from the random configuration of $In^{3+}$ and $Nb^{5+}$ at the B-site in the perovskite structure, while the dielectric property of such systems is governed mainly by the replacement of Pb and O ions. This system has the advantage that the strength of randomness can be controlled by adjusting annealing temperature.³⁾ For the lowest annealing temperature, an alternate order of In and Nb atoms stabilizes the fourfold antiferroelectric (AFE) phase. For the higher annealing temperature, an increase in B-site randomness decreases AFE transition temperature. Under sufficiently strong randomness in the B-site, the ferroelectric phase accompanies relaxor properties. This behavior of PIN suggests that the potential FE instability exists behind the AFE phase, and that its emergence by the selective suppression of the AFE phase due to B-site randomness is relevant to FE relaxors. Recent experimental progress in the X-ray diffraction analysis facilitated by strong-intensity photon sources has also enabled us to detect the potential competition between the FE and AFE phases of PIN from the viewpoint of lattice dynamics.⁴⁾⁵⁾

There are several theoretical methods for elucidating the emergence of relaxor properties. They utilize the existing effective theory dealing with a strong randomness such as the extension of the Ginzburg–Landau–Devonshire theory,⁶⁾⁷⁾ the spherical random-bond–random-field model,⁸⁾ and the dynamical-related model.⁹⁾¹⁰⁾ Although these approaches have provided useful description of relaxor properties, it is unclear how their model parameters should be derived microscopically. At present, first-principles calculation is playing a crucial role in the microscopic description of ferroelectrics and ferroelectric relaxors. In the pioneering work by Cohen and coworker,¹¹⁾¹²⁾ the electron-structure calculation of $BaTiO_3$ and $PbTiO_3$ indicated the importance of the covalent nature among composite atoms through Ti-O hybridization. After the success of their work, microscopic first-principles approaches have been adopted in a number of issues. Further theoretical progress has been achieved by a hybrid method combining the microscopic derivation of the effective Hamiltonian and its numerical simulation. Zhong *et al.* have derived the effective Hamiltonian of $BaTiO_3$ by extracting the adiabatic potential of important phonon modes from first-principles calculation.¹³⁾¹⁴⁾ Monte Carlo simulation for this effective Hamiltonian has enabled the successful reproduction of the sequential finite-temperature phase transitions of $BaTiO_3$ in good agreement with experimental results. Recently, the hybrid method has also been applied to the study of relaxor systems.¹⁵⁾¹⁶⁾

Thus, the utilization of first-principles calculation is a promising method for understanding relaxors. However, there still remain several difficulties to overcome for the actual application of this method to the study of relaxors. One major difficulty is in the use of the numerical solver of the effective Hamiltonian for phonons. Even though the effective Hamiltonian derived for relaxors is in a simple form, its numerical simulation may become extremely difficult because it is inevitable to encounter slow dynamics inherent to random systems. The Monte Carlo simulation of the effective Hamiltonian needs a large number of Monte Carlo steps owing to its long correlation time. Therefore, the development of appropriate numerical solvers for relaxor systems seems indispensable. This situation may remind us of Monte Carlo studies of spin-glass systems. Although the Hamiltonian of spin-glass systems has a simple form, much effort has to be exerted for sufficient Monte Carlo sampling to understand their peculiar slow dynamics. In the research field of relaxors, however, the importance of developing a numerical solver has not been addressed so far.

In this paper, we propose a simple model of ferroelectric relaxors to explain the phase diagram of PIN. Our model

*E-mail: ytomita@issp.u-tokyo.ac.jp

includes both long-range dipole-dipole interaction and local randomness. We apply the new effective algorithm optimized for long-range interaction proposed by Fukui and Todo.¹⁷ This new algorithm enables us to simulate long-range interaction systems with the cost of O(N) with respect to the system size N, while the conventional simulation for the same system takes the cost of O(N²). In addition to the substantial reduction in computational time by employing this algorithm, we adopt the exchange Monte Carlo method to attenuate the slow dynamics of random systems.¹⁸ We show that our simple model may qualitatively reproduce the phase diagram of PIN. Moreover, we demonstrate that some characteristic features of relaxors such as domain formation and dispersive dielectric response are reproduced reasonably. Our results indicate the power of the sophisticated Monte Carlo method as well as the possibility that relaxor systems may be represented by a simple model.

We consider the model Hamiltonian for PIN on a 2D square lattice as

$$
\begin{aligned}
\mathcal{H}= & \sum_{i<j}\left[\frac{\boldsymbol{S}_{i} \cdot \boldsymbol{S}_{j}}{r_{i j}^{3}}-3 \frac{\left(\boldsymbol{r}_{i j} \cdot \boldsymbol{S}_{i}\right)\left(\boldsymbol{r}_{i j} \cdot \boldsymbol{S}_{j}\right)}{r_{i j}^{5}}\right] \\
& -\sum_{i}\left(\boldsymbol{D}_{i} \cdot \boldsymbol{S}_{i}\right)^{2},
\end{aligned}
\tag{1}
$$

where $\boldsymbol{S}_{i}$ is a unit vector in the xy-plane representing the dipole moment on the ith unit cell induced by the off-center replacement of the Pb atom. The first term of the Hamiltonian is the dipole-dipole interaction dependent on the relative position $\boldsymbol{r}_{i j}=\boldsymbol{r}_{j}-\boldsymbol{r}_{i}$ between the sites i and j, while the second term describes local anisotropy whose direction and strength are denoted as $\boldsymbol{D}_{i}$. In order to reproduce the phase diagram of PIN, we design our model such that the FE phase is stabilized by dipole-dipole interaction, while the AFE phase is stabilized in the presence of an alternative change in $\boldsymbol{D}_{i}$. Supposing that B-site randomness affects only the local energy change through the anisotropy parameter $\boldsymbol{D}_{i}$, we can expect that all the features of PIN, i.e., the AFE transition in the ordered PIN, its suppression by B-site randomness, and the appearance of the FE domain in the sufficiently disordered PIN are reproduced.

The detailed setting of our model is given as follows. In a naive 2D square lattice, the dipole-dipole interaction does not lead to ferroelectric instability because the columnar antiferroelectric state is more favored in orthogonal lattices.¹⁹ Therefore, we modify our model slightly: We divide the unit cells into two bipartite sublattices named P and Q, and shift only the Q-sites in the z-direction by a unit length. This rearrangement of unit cells ensures ferroelectric instability in the absence of local anisotropy. The antiferroelectric instability is driven by an alternative arrangement of two types of anisotropy, namely, $\boldsymbol{D}_{1}$ and $\boldsymbol{D}_{2}$ in the P- and Q-sites, where $\boldsymbol{D}_{1}=(D/\sqrt{2},-D/\sqrt{2})$ and $\boldsymbol{D}_{2}=(D/\sqrt{2},D/\sqrt{2})$. The randomness of $\boldsymbol{D}$ is controlled by the probability p, where $\boldsymbol{D}_{1}$ ($\boldsymbol{D}_{2}$) is attached to the P-(Q-)site with a probability $(1-p)^2$, oppositely to $p^2$, and is turned off ($\boldsymbol{D}=\boldsymbol{0}$) with $2p(1-p)$. The two limiting values $p=0$ and $1/2$ correspond to the ordered and completely disordered PINs, respectively.

The model Hamiltonian is examined by Monte Carlo simulations under a periodic boundary condition to minimize the strong surface effect due to long-range interaction. Long-range interactions are summed up by the Ewald summation technique.²⁰ We employ the O(N) method based on Walker's algorithm for efficient update¹⁷,²¹ as well as the temperature-exchange algorithm.¹⁸ One exchange trial between replicas was made for each of the 10 MC steps. The system size is taken up to $N=32\times32$, for which $3\times10^6$ MC steps for thermalization and $2\times10^5$ MC steps for measurement were needed in the severest case of $p=1/2$. The sample average is taken over 10 different random configurations of $\boldsymbol{D}_{i}$ for each p. Throughout this paper, the strength of the anisotropy is fixed as $|\boldsymbol{D}_{i}|=1$.

![](./images/811806613517107202_1.jpg)

Fig. 1. (Color online) (a) A plot of four-fold antiferroelectric (AFE) order parameters in the absence of randomness ($p=0$) and (b) a plot of ferroelectric (FE) order parameters at $p=0.5$ are shown for different system sizes $N=L\times L$. (c) Phase diagram obtained by the minimum model. Phase boundaries in the figure are visual guides.

Figure 1(a) shows the temperature dependence of the average squared four-fold staggered polarization $m_{\text{AF}}$ for the ordered PIN ($p=0$). The pattern of the AFE ordering, which is shown in Fig. 1(c), agrees with experimental observations. As the system size $N=L\times L$ increases, a sharp increase in the order parameter appears below a critical temperature, indicating the phase transition. The transition point is determined by the crossing point of the Binder parameters, $\langle m_{\text{AF}}^4\rangle/\langle m_{\text{AF}}^2\rangle^2$, of $L=16$ and 32. By a similar analysis of nonzero values of p, the phase boundary of AFE in the $p$-$T$ plane is determined, as shown by full circles in Fig. 1(c). For small values of p, the transition temperature of AFE is suppressed by the B-site randomness. For sufficiently large values of p, the FE domain develops at low temperatures instead of the AFE phase. Figure 1(b) shows the average squared uniform polarization as a function of temperature in the completely disordered case ($p=1/2$). An abrupt increase in squared polarization below a threshold temperature for the $N=32\times32$ system indicates a rapid development of the FE domain. In our simulation, however, no long-range FE ordering could be

![](./images/811806613517107202_2.jpg)

Fig. 2. (Color online) Log-log plot of the normalized time autocorrelation functions. While the autocorrelation functions decay smoothly for the no-anisotropy system at $T=0.2$ and the random system at $T=0.3$, the autocorrelation function shows a slow decay for the random system at $T=0.2$.

detected by finite-size scaling because of the very slow relaxation of the Monte Carlo sampling and the complex size dependence in the presence of strong randomness. Here, we roughly estimate the threshold temperature at which the local FE instability rises up by Binder-parameter analysis between $L=16$ and 32, and plot it using the empty circle in Fig. 1(c). At approximately $p=0.4$, the competition between AFE and FE makes the Monte Carlo calculation severe, and the phase boundary could not be determined. Rough interpolations for AFE and FE are shown by the solid curves in Fig. 1(c) only as visual guides. The obtained phase diagram is in good agreement with experimental results of PIN.

For large values of $p$, some characteristic features of relaxor systems appear below a crossover temperature, which locates higher than the threshold temperature for FE domain formation, as indicated roughly by the dashed line in Fig. 1(c). The emergence of relaxor properties is indicated significantly by the slow convergence of the Monte Carlo average. Figure 2 shows the normalized autocorrelation of the energy $E$ for $N=32 \times 32$ defined by

$$
\phi(t)=\frac{\langle E(0) E(t)\rangle-\langle E\rangle^{2}}{\left\langle E^{2}\right\rangle-\langle E\rangle^{2}} \tag{2}
$$

as a function of the Monte Carlo step $t$ in the completely random case $(p=1 / 2)$. Here, for the purpose of examining the dynamics of the system, we turned off the exchange process between replicas. We find that the decay of the autocorrelation function is extremely slow at $T=0.2$ in clear contrast with that at a higher temperature $T=0.3$. This slow energy relaxation indicates a glasslike behavior for relaxors at low temperatures. In order to confirm that this slow relaxation comes from randomness of the B-site, we also calculated the autocorrelation at $T=0.2$ in the absence of local anisotropy $(|D_{i}|=0)$, for which normal FE ordering is expected. As seen in Fig. 2, the autocorrelation function follows a simple decay with no anomalous slow relaxation. Thus, the present model is expected to exhibit relaxor properties under sufficiently strong randomness below a crossover temperature.

In order to visualize the glassy state realized in the relaxor phase, we show in Fig. 3 the spatial pattern of dipole directions by taking snapshots as a function of the MC steps for $p=0.5$ and $N=32 \times 32$. We can see that mosaic-like FE domains are formed after a finite relaxation time. The boundaries (domain-wall regions) between the neighboring FE domains are rather clear. One may consider that the FE domain structure is determined by a partially ordered configuration of anisotropy, the so-called chemical nano-region (CNR). The present FE domain is, however, irrelevant to CNR, because partial ordering is absent for a complete random choice of anisotropy at each site in our model.

![](./images/811806613517107202_3.jpg)

Fig. 3. (Color online) Snapshots of dipole configuration for $p=0.5$ and $T=0.1$. Each color denotes the angle of dipole moment. Reference color bars are shown on the right. The bottom color denotes $-\pi$, and the top color denotes $\pi$. The last graph shows the result for the same parameters but for a model with a dipole interaction interrupted up to the next-nearest sites.

As has already been mentioned, the present system possesses FE instability in the absence of local anisotropy $(D=0)$. The random configuration of anisotropy similarly causes a local FE instability due to effective cancellation of anisotropy, but at the same time prevents the growth of an FE domain into a uniform FE order, as seen in Fig. 3. A small but finite change of the snapshot in the long-time region of the Monte Carlo simulation indicates that a very slow fluctuation of the FE domain governs the relaxor properties in the present model. Here, we should note that the evolution of the dipole configuration along the Monte Carlo step is not directly related to actual real-time dynamics. The snapshots, however, provide intuitive and fruitful insights for understanding physical processes in relaxor systems. In our model, the long-range nature of the dipole interaction is essential for the formation of the FE domain structure. To see this, we show a snapshot of Monte Carlo simulation for a model with dipole interaction interrupted up to the next-nearest site in the last graph of Fig. 3. We find that the domain structure disappears in this modified model.

The existence of nanoscale frustrated FE domains indicates the high degeneracy of glassy states. This degeneracy is expected to be responsible for large dielectric responses since a significant change in the polarization of such FE domains is possible by a small external electric field. To see this, we measure the Monte Carlo evolution of the total polarization under a small "ac" electric field, which varies periodically along the Monte Carlo step. We then calculate the "ac" dielectric constant in the linear response regime. We should note again that the "ac" dielectric constant thus

023001-3

![](./images/811806613517107202_4.jpg)

Fig. 4. (Color online) Dielectric constants evaluated as functions of temperature under the ac electric field for several frequencies in the (a) ordered case ($p=0$) and (b) completely disordered case ($p=1/2$).

obtained is not equal to the real-time ac dielectric constant. Furthermore, we should keep in mind that this is a nonequilibrium response since the relaxation to equilibrium states is never realized in the glassy phase in the present simulation. Nevertheless, the "ac" dielectric response calculated here is expected to mimic the actual ac response in a qualitative level. In Fig. 4, we show the "ac" dielectric constant as a function of temperature for three frequencies in the ordered ($p=0.0$) and completely disordered ($p=1/2$) cases. In both cases, dielectric constant shows a peak at approximately the transition (crossover) temperature. The marked difference is found in the low-temperature phase. In the ordered case, dielectric constant sharply drops in the low-temperature AFE phase, and becomes almost independ- ent of frequency. On the other hand, in the disordered case, it decreases gradually as temperature decreases, and a strong frequency dependence remains. This strong dispersion of dielectric constant at low temperatures can be explained as follows. Under a high-frequency electric field, each dipole inside FE domains may respond to an external field. Under a low-frequency electric field, however, those with frustration that construct large domains start to respond. Therefore, in a minimum model, a dipolar glass with ferroelectric ordering is realized. This ordering causes a broadened dielectric constant and a strong dependence on frequency in the relaxor phase.

In summary, we examined a simple theoretical model of PIN composed of dipolar interaction and local random anisotropy. We demonstrated that efficient Monte Carlo simulations equipped with an improved algorithm optimized for long-range interaction may access several characteristic features of relaxors. The phase diagram of PIN was qualitatively reproduced by appropriate inclusion of the intrinsic competition between the AFE and FE phases. By the examination of the Monte Carlo evolution of the dipole configuration, we demonstrated some of the glassy behaviors inherent to relaxor systems such as the FE domain formation, extremely slow dynamics, and strong frequency dependence of dielectric responses.

We end this paper by mentioning the future outlook of theoretical approaches to studying relaxors. The model we treated here includes a few artificial assumptions. They, however, will be removed by replacing our model with the effective Hamiltonian derived by first-principles calculation. We stress that the smart Monte Carlo algorithm is applicable not only to the rotator model but also to the continuous- variable model. The hybridization of the first-principles calculation and statistical approach based on the Monte Carlo simulation will be an effective means of elucidating the microscopic origin of relaxors.

### Acknowledgments

The computation in the present work is executed on computers at the Supercomputer Center, Institute for Solid State Physics, University of Tokyo. The present work is financially supported by Grants-in-Aid for Scientific Re- search B (19340109), and for Scientific Research on Priority Areas "Novel States of Matter Induced by Frustration" (19052002) from the Ministry of Education, Culture, Sports, Science and Technology (MEXT), and by the Next Generation Supercomputing Project, Nanoscience Program, MEXT, Japan.

1) G. A. Smolenskii and A. I. Agronovskaya: Sov. Phys. Tech. Phys. A 3 (1958) 1380.
2) For recent reviews, A. A. Bokov and Z.-G. Ye: J. Mater. Sci. 41 (2006) 31.
3) A. A. Bokov, I. P. Raevskii, O. I. Prokopalo, E. G. Fesenko, and V. G. Smotrakov: Ferroelectrics 54 (1984) 241.
4) K. Ohwada, K. Hirota, H. Terauchi, T. Fukuda, S. Tsutui, A. Q. R. Baron, J. Mizuki, H. Ohwa, and N. Yasuda: Phys. Rev. B 77 (2008) 094136.
5) K. Ohwada and Y. Tomita: J. Phys. Soc. Jpn. 79 (2010) 011012.
6) A. F. Devonshire: Adv. Phys. 3 (1954) 85.
7) J.-M. Liu, S. T. Lau, H. L. W. Chan, and C. L. Choy: J. Mater. Sci. 41 (2006) 163.
8) R. Blinc, J. Dolinšek, A. Gregorovič, B. Zalar, C. Filipič, Z. Kutnjak, A. Levstik, and R. Pirc: Phys. Rev. Lett. 83 (1999) 424.
9) A. J. Bell: J. Phys.: Condens. Matter 5 (1993) 8773.
10) B. E. Vugmeister and H. Rabitz: Phys. Rev. B 57 (1998) 7581.
11) R. E. Cohen: Nature 358 (1992) 136.
12) R. E. Cohen and H. Krakauer: Ferroelectrics 136 (1992) 65.
13) W. Zhong, D. Vanderbilt, and K. M. Rabe: Phys. Rev. Lett. 73 (1994) 1861.
14) W. Zhong, D. Vanderbilt, and K. M. Rabe: Phys. Rev. B 52 (1995) 6301.
15) S. Tinte, B. P. Burton, E. Cockayne, and U. V. Waghmare: Phys. Rev. Lett. 97 (2006) 137601.
16) B. P. Burton, E. Cockayne, S. Tinte, and U. V. Waghmare: Phys. Rev. B 77 (2008) 144114.
17) K. Fukui and S. Todo: J. Comput. Phys. 228 (2009) 2629.
18) K. Hukushima and K. Nemoto: J. Phys. Soc. Jpn. 65 (1996) 1604.
19) Y. Tomita: J. Phys. Soc. Jpn. 78 (2009) 114004.
20) J.-J. Weis: J. Phys.: Condens. Matter 15 (2003) S1471.
21) A. J. Walker: ACM Trans. Math. Software 3 (1977) 253.

023001-4