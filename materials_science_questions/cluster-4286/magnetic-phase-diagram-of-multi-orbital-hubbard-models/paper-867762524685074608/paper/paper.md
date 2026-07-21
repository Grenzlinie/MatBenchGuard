# Phase diagram of orbital-selective Mott transitions at finite temperatures

Kensuke INABA, Akihisa KOGA, Sei-ichiro SUGA and Norio KAWAKAMI

Department of Applied Physics, Osaka University, Suita, Osaka 565-0871
(Received August 30, 2018)

Mott transitions in the two-orbital Hubbard model with different bandwidths are investigated at finite temperatures. By means of the self-energy functional approach, we discuss the stability of the intermediate phase with one orbital localized and the other itinerant, which is caused by the orbital-selective Mott transition (OSMT). It is shown that the OSMT realizes two different coexistence regions at finite temperatures in accordance with the recent results of Liebsch. We further find that the particularly interesting behavior emerges around the special condition $U = U'$ and $J = 0$, which includes a new type of the coexistence region with three distinct states. By systematically changing the Hund coupling, we establish the global phase diagram to elucidate the key role played by the Hund coupling on the Mott transitions.

KEYWORDS: Orbital-selective Mott transition, Self-energy functional approach

Strongly correlated electron systems with some orbitals have been investigated extensively. $^{1,2}$ In particular, substantial progress in theoretical understanding of Mott transitions of multi-orbital systems has been made by dynamical mean-field theory (DMFT) $^{3,4}$ calculations. $^{5-29}$ Among them, the orbital-selective Mott transition (OSMT) $^{30}$ in the multi-orbital system with different bandwidths has been one of the most active topics in this context. Typical materials are $Ca_{2-x}Sr_{x}RuO_{4}^{31}$ and $La_{n+1}Ni_{n}O_{3n+1},^{32,33}$ where the OSMT is suggested to be realized by the chemical substitution and the change in the temperature. These experimental findings have stimulated theoretical investigations on this issue. $^{21-30,34,35}$ It has been clarified by extensive works that in the two-orbital system with different bandwidths at zero temperature, the OSMT occurs in general and merges to a single Mott transition in a certain restricted parameter region. $^{22,24,25}$ Also, it has been realized that the Hund coupling is an important key parameter to understand the correct nature of the OSMT. $^{28,36}$

In contrast to the detailed analysis at zero temperature, systematic discussions at finite temperatures $^{21,23,27,28}$ are lacking. In particular, the stability of the intermediate metallic phase may be important to discuss the possibility of the OSMT in real materials. It is thus desirable to investigate the OSMT in the multi-orbital model at finite temperatures. Quite recently, Liebsch have studied finite-temperature properties of the OSMT by DMFT combined with the exact diagonalization method, $^{28}$ where the OSMT occurs even at finite temperatures.

In this paper, we give the detailed investigation of the OSMT in the two-orbital Hubbard model at zero and finite temperatures. We make use of the self-energy functional approach (SFA) proposed by Potthoff, $^{37}$ which is efficient to study finite-temperature properties, to determine the detailed phase diagram. The present study provides the results complementary to Liebsch's in a certain parameter regime, $^{28}$ and moreover establishes rich phase diagrams, which include a new type of the coexistence region with three distinct states. We further clarify how the magnitude of the Hund coupling controls the nature of phase diagrams at finite temperatures.

We consider the two-orbital Hubbard model with different bandwidths, which is given by the Hamiltonian, $\mathcal{H} = \mathcal{H}_0 + \sum_i \mathcal{H}_i'$ with

$$
\mathcal{H}_0 = \sum_{<i,j>,\alpha,\sigma} \left(t_\alpha - \mu \delta_{ij}\right) c_{i\alpha\sigma}^\dagger c_{j\alpha\sigma}, \tag{1}
$$

$$
\begin{aligned}
\mathcal{H}_i' =& U \sum_\alpha n_{i\alpha\uparrow}n_{i\alpha\downarrow} + \sum_{\sigma\sigma'} (U' - \delta_{\sigma\sigma'} J) n_{i1\sigma} n_{i2\sigma'} \\
&- J(c_{i1\uparrow}^\dagger c_{i1\downarrow} c_{i2\downarrow}^\dagger c_{i2\uparrow} + c_{i1\uparrow}^\dagger c_{i1\downarrow} c_{i2\uparrow} c_{i2\downarrow} + H.c.),(2)
\end{aligned}
$$

where $c_{i\alpha\sigma}^\dagger (c_{i\alpha\sigma})$ is the creation (annihilation) operator of an electron at the $i$th site with spin $\sigma(=\uparrow,\downarrow)$ and orbital $\alpha(=1,2)$, and $n_{i\alpha\sigma} = c_{i\alpha\sigma}^\dagger c_{i\alpha\sigma}$. Here, $t_\alpha$ denotes the hopping integral for orbital $\alpha$, $\mu$ the chemical potential, $U(U')$ the intra-orbital (inter-orbital) Coulomb interaction, and $J$ the Hund coupling including the spin-flip and pair-hopping terms. In the following, we impose the condition $U = U' + 2J$, which results from rotational symmetry of degenerate orbitals.

In order to discuss the Mott transitions at zero and finite temperatures, we use here the self-energy functional approach SFA, $^{37}$ which is based on the Luttinger-Ward variational method. $^{38}$ This approach allows us to deal with finite-temperature properties of the multi-orbital system efficiently, $^{39}$ where standard DMFT with numerical techniques may encounter some difficulties in a practical computation when the number of orbitals increases.

In SFA, one makes use of the fact that the Luttinger-Ward functional does not depend on the detail of the Hamiltonian $\mathcal{H}_0$ as far as the interaction term $\mathcal{H}'$ is unchanged. $^{37}$ This enables us to introduce a proper reference system with the same interaction term. One of the simplest models for the reference system is explicitly given by the following Hamiltonian, $\mathcal{H}_\text{ref} = \sum_i \mathcal{H}_\text{ref}^{(i)}$,

$$
\mathcal{H}_\text{ref}^{(i)} = \sum_{\alpha\sigma} \left[\epsilon_{0\alpha}^{(i)} c_{i\alpha\sigma}^\dagger c_{i\alpha\sigma} + \epsilon_\alpha^{(i)} a_{\alpha\sigma}^{(i)\dagger} a_{\alpha\sigma}^{(i)}\right]
$$

$$
+\sum_{\alpha \sigma} V_{\alpha}^{(i)}\left(c_{i \alpha \sigma}^{\dagger} a_{\alpha \sigma}^{(i)}+H . c .\right)+H_{i}^{\prime}, \quad (3)
$$

where $a_{\alpha \sigma}^{(i) \dagger}(a_{\alpha \sigma}^{(i)})$ creates (annihilates) an electron with $\sigma$ spin and $\alpha$ orbital, which is connected to the $i$ th site in the original lattice. This approximation is regarded as a finite-temperature extension of the two-site DMFT $^{40}$ in some respects. In this paper, we fix the parameters $\epsilon_{0 \alpha}=0, \epsilon_{\alpha}=\mu$ and $\mu=U / 2+U^{\prime}-J / 2$ to discuss the zero and finite temperature properties at half filling. By choosing the parameters $V_{\alpha}$ to minimize the grand potential, $\partial \Omega / \partial V_{\alpha}=0(\alpha=1,2)$, we can find a proper reference Hamiltonian, which approximately describes the original correlated system.

We note that the hybridization $V_{\alpha}$ between a given site on the original lattice and a site in the reference system may be regarded as the renormalized bandwidth of the $\alpha$-orbital band. For example, for small $V_{\alpha}$, heavy quasiparticles are formed in the $\alpha$ band, and at $V_{\alpha}=0$ the system is driven to the Mott insulating state. By calculating hybridizations $V_{1}$ and $V_{2}$, we thus discuss the stability of the metallic state in our two-orbital Hubbard model. In the following, we focus on the system with $W_{1}=2.0$ and $W_{2}=4.0$ to discuss Mott transitions, where $W_{\alpha}$ is the bandwidth of $\alpha$-orbital for the semi-circular density of states (DOS), $\rho_{\alpha}(x)=4 / \pi W_{\alpha} \sqrt{1-\left(2 x / W_{\alpha}\right)^{2}}$.

We begin our discussions with the Mott transitions at zero temperature for a typical choice of the ratio of the parameters, $U^{\prime}=0.5 U$ and $J=0.25 U$. Figure 1 shows the contour plots of the grand potential and the corresponding entropy per site $S / L$ at the stationary point, where $L$ is the number of sites. When the Coulomb interaction is small $(U=2.3)$, the stationary point, where the grand potential is minimized, is located around $(V_{1}, V_{2}) \sim(0.14,0.55)$. This implies that the effective bandwidth for each orbital state is finite, stabilizing the metallic (M) phase. Increasing the interaction, the stationary point of the system touches the $V_{2}$-axis as shown in the inset (b): the effective bandwidth for the narrower band $V_{1}$ vanishes while $V_{2}$ still remains finite. Therefore, the OSMT occurs, where one band is insulating and the other is still metallic. We refer to this phase as the OSM phase in the following. It is seen that the residual entropy in the OSM phase is $S / L=\log 2$, implying the formation of free localized $s=1 / 2$ spins. Further increase of the interaction induces the Mott transition in the other band to the Mott insulating (MI) phase, where $V_{1}=V_{2}=0$ as shown in the inset (c). In this case, the localized spins for two bands form the triplet state due to the Hund coupling, so that the residual entropy $S / L=\log 3$ in the region $U>3.4$. Note that the residual entropy at zero temperature is an artifact of our simplified SFA approach. This pathological behavior can be somehow improved, e.g. by taking into account spin fluctuations more accurately. At zero temperature, we can find no other local minima in the grand potential when the interaction is varied. Therefore, we clearly observe double second-order Mott transitions in the multi-orbital system, which indeed confirms the claim of Koga et $a l .^{22}$ for the OSM transition obtained by means of DMFT combined with the exact diagonalization.

![](./images/867762524685074608_1.jpg)

Fig. 1. The entropy per site $S / L$ as a function of $U$ with fixed ratios $U^{\prime}=0.5 U$ and $J=0.25 U$ at $T=0$. Inset shows the contour plot of the grand potential for (a)$U=2.3$, (b) 2.8 and (c) 3.6, where crosses denote the minima of the grand potential.

We now move to the phase diagram at finite temperatures. Since each transition at zero temperature is similar to that for the single-orbital Hubbard model, $^{3}$ the first-order transition may occur at finite temperatures around each critical point, as shown in ref. 28. In fact, we find that when the system belongs to the metallic phase close to the critical point, two stationary points representing the M and OSM states appear simultaneously once the system is at finite temperatures $(T=0.002)$, as shown in Fig. 2. The double-well structure causes the first-order Mott transition with hysteresis at finite temperatures (Fig. 2 (b)). At $T=0.002$, as $U$ increases, the stationary point for the metallic state disappears around $U_{c 2} \sim 2.36$, where the Mott transition occurs to the OSM phase. On the other hand, as $U$ decreases, the OSM phase realized is stable down to $U_{c 1} \sim 2.24$. The first-order transition point $U_{c} \sim 2.33$ for $T=0.002$ is determined by the crossing point of the two minima in the grand potential. The obtained phase diagram is shown in Fig. 3. It is found that the two distinct coexistence regions appear around $U \sim 2.4$ and $U \sim 3.3$. The phase

![](./images/867762524685074608_2.jpg)

Fig. 2. (a) The contour plot of the grand potential $\Omega(V_{1}, V_{2})$ at $T=0.002, U=2.3$ and $J=0.25 U$. Two minima coexist, which correspond to the M and OSM states. (b) The entropy vs the interaction $U$ at $T=0.002, J=0.25 U$.


![](./images/867762524685074608_3.jpg)

Fig. 3. $U-T$ phase diagram at $J=0.25U$. There are two coexistence phases, which are featured by the triangular-shaped regions: (left)the metallic phase and orbital-selective Mott phase coexist and (right) orbital-selective Mott phase and insulating phase coexist.

![](./images/867762524685074608_4.jpg)

Fig. 4. (a) Entropy $S/L$ and (b) Specific heat $C/L$ as a function of $U$ in the crossover region, $J=0.25U$.

boundaries $U_{c 1}, U_{c 2}$ and $U_{c}$ merge at the critical temperature $T_{c}$ for each transition. Similar phase diagram was recently obtained by Liebsch by means of DMFT with the exact diagonalization method, who gave better estimates of the critical temperatures. $^{28}$ Nevertheless, our SFA treatment elucidates further interesting properties such as the crossover behavior among the competing M, OSM and MI phases. To make this point more explicit, we calculate thermodynamic quantities such as the entropy and the specific heat, which are displayed in Fig. 4. We can see a double-step structure similar to that found at zero temperature in the curve of the entropy. Such anomalies are more clearly seen in the specific heat. It is quite impressive that the crossover behavior among three phases are clearly seen even at higher temperatures. We can thus say that the OSM phase is rather well defined even at higher temperatures above the critical tempera- tures.

We have so far discussed the OSMT for the system with rather large Hund couplings. According to the zero- temperature analysis, $^{22,24,25}$ it is known that around the special condition $U=U^{\prime}$ and $J=0$ at $W_{1}/W_{2}=0.5$, a non-trivial single Mott transition occurs, whose origin is attributed to enhanced orbital fluctuations. $^{23}$ Therefore, it is interesting to observe what happens at finite temperatures, when the system approaches the condition $U=U^{\prime}$ and $J=0$. By performing similar calculations, we end up with the phase diagram for the system with $U^{\prime}=0.94U,J=0.03U$ (Fig. 5). Since the Hund coupling is very small in this case, two critical points for the OSMT at zero temperature are close to each other. One of the most remarkable findings here is that three competing states (M, OSM and MI states) coexist in a certain region at finite temperatures, where three distinct local minima appear in the grand potential, as shown in the inset. In these parameters, the coexistence regions are quite sensitive to how large the Hund coupling is.

![](./images/867762524685074608_5.jpg)

Fig. 5. $U-T$ phase diagram at $J=0.03U$: we have used the same symbols as in Fig. 3. Note that the two coexistence regions are not separated here in contrast to Fig. 3. Three distinct states (M,OSM,and MI states) coexist in the region which is surrounded by filled and open circles. Inset shows the contour plot of the ground potential in the coexistence region for $U=4.45,T=0.004$, where there are three local minima.

To observe how the Hund coupling controls finite- temperature properties, we show the global phase dia- grams in Fig. 6 by systematically changing $J$. As the Hund coupling decreases, both the critical points $U_{c2}^{(1)}$ and $U_{c2}^{(2)}$ increase monotonically, stabilizing the metallic state up to fairly large Coulomb interactions, as already mentioned for the zero-temperature case. $^{22}$ A remarkable feature in Fig. 6 is that the completely different behavior emerges in the critical temperatures $T_{c}^{(1)}$ and $T_{c}^{(2)}$. It is seen that $T_{c}^{(1)}$ is almost unchanged, whereas $T_{c}^{(2)}$ strongly depends on the Hund coupling. This may be explained as follows. Around the first boundary between the M and OSM phases, the nature of the transition is essentially the same as the single-orbital case, as discussed above. Therefore, the Hund coupling little affects the critical temperature $T_{c}^{(1)}$. On the other

![](./images/867762524685074608_6.jpg)

Fig. 6. Overall picture for the coexistence regions with systematic change of $J$: two types of the regions are shown for $J = 0.25U$, $J = 0.1U$, $J = 0.03U$ and $J = 0$ from left to right. At $J = 0$, the transition from the metal to OSM disappears.

hand, around the second phase transition between the OSM and MI phases, orbital fluctuations should play a vital role. The presence of the Hund coupling somewhat suppresses orbital fluctuations due to the formation of the triplet state. $^{15}$ Therefore, as $J$ decreases, enhanced orbital fluctuations raise the critical temperature $T_{c}^{(2)}$, as seen in Fig. 6. Note that for very small Hund couplings ($J \lesssim 0.03U$) the OSM phase disappears, $^{25}$ and thus the finite as well as zero-temperature properties can be approximately described by the multi-orbital model ($U \neq U'$) with the same bandwidths. $^{15,17,19,39}$

In summary, we have investigated Mott transitions in the two-orbital Hubbard model with different bandwidths at finite temperatures. By means of the self-energy functional approach, we have confirmed that two distinct coexistence regions appear in the phase diagram in accordance with the recent results obtained by DMFT. A notable new finding is that the OSM phase is rather well defined even at temperatures higher than the two critical temperatures. Further remarkable features have been elucidated in the phase diagram around special conditions with small Hund couplings $J \simeq 0$ ($U \simeq U'$), where the coexistence region with three competing phases emerges. Orbital fluctuations are enhanced there, and therefore the system gets very sensitive to small perturbations, giving rise to the rich phase diagram at low temperatures. We have also clarified the role of the Hund coupling on global features in the phase diagram: the Hund coupling has little (sizable) effect on the transition between the M and OSM (OSM and MI) phases, which is again attributed to the role played by enhanced orbital fluctuations.

In this paper we have exploited the simplified version of SFA to elucidate fundamental properties at finite temperatures. Since instabilities to possible ordered phases have not been considered here, SFA is to be generalized to incorporate such ordered phases, which should be done in the future work.

We would like to thank M. Sigrist, T. M. Rice and A. Liebsch for valuable discussions. Numerical computations were carried out at the Supercomputer Center, the Institute for Solid State Physics, University of Tokyo.

This work was supported by a Grant-in-Aid for Scientific Research from the Ministry of Education, Culture, Sports, Science, and Technology, Japan.

1) M. Imada, A. Fujimori and Y. Tokura: Rev. Mod. Phys. **70** (1998) 1039.
2) Y. Tokura and N. Nagaosa: Science **288** (2000) 462.
3) A. Georges, G. Kotliar, W. Krauth and M. J. Rozenberg: Rev. Mod. Phys. **68** (1996) 13.
4) G. Kotliar and D. Vollhardt: Phys. Today **57** (2004) 53.
5) C.-I. Kim, Y. Kuramoto and T. Kasuya: J. Phys. Soc. Jpn. **59** (1990) 2414.
6) G. Kotliar and H. Kajueter: Phys. Rev. B **54** (1996) 14221.
7) M. J. Rozenberg: Phys. Rev. B **55** (1997) R4855.
8) J. Bünemann and W. Weber, Phys. Rev. B **55**, 4011 (1997); J. Bünemann and W. Weber and F. Gebhard, ibid **57**, 6896 (1998).
9) H. Hasegawa: J. Phys. Soc. Jpn. **56** (1997) 1196.
10) K. Held and D. Vollhardt: Eur. Phys. J. B **5** (1998) 473.
11) J. E. Han, M. Jarrel and D. L. Cox: Phys. Rev. B **58** (1998) R4199.
12) T. Momoi and K. Kubo: Phys. Rev. B **58** (1998) R567.
13) A. Klejnberg and J. Spalek: Phys. Rev. B **57** (1998) 12401.
14) Y. Imai and N. Kawakami: J. Phys. Soc. Jpn **70** (2001) 2365.
15) A. Koga and Y. Imai and N. Kawakami: Phys. Rev. B **66** (2002) 165107; J. Phys. Soc. Jpn. **72** (2003) 1306.
16) V. S. Oudovenko and G. Kotliar: Phys. Rev. B **65** (2002) 075102.
17) Y. Ono, M. Potthoff and R. Bulla: Phys. Rev. B **67** (2003) 035119.
18) Y. Tomio and T. Ogawa: ond-mat/0407314.
19) T. Pruschke and R. Bulla: Eur. Phys. J. B **44** (2005) 217.
20) S. Sakai, R. Arita and H. Aoki: cond-mat/0405503.
21) A. Liebsch, Phys. Rev. Lett. **91**, 226401 (2003); Europhys. Lett. **63**, 97 (2003); Phys. Rev. B **70**, 249904 (2004).
22) A. Koga, N. Kawakami, T. M. Rice and M. Sigrist: Phys. Rev. Lett. **92** (2004) 216402.
23) A. Koga, N. Kawakami, T. M. Rice and M. Sigrist: cond-mat/0503651.
24) M. Ferrero, F. Becca, M. Fabrizio and M. Capone: cond-mat/0503759.
25) L. de' Medici, A. Georges and S. Biermann: cond-mat/0503764.
26) R. Arita and K. Held: cond-mat/0504040.
27) C. Knecht, N. Blümer and P. G. J. van Dongen: cond-mat/0505106.
28) After the completion of the present work, we became aware of the recent preprint; A. Liebsch: cond-mat/0505393.
29) S. Biermann, L. de' Medici and A. Georges: cond-mat/0505737.
30) V. I. Anisimov, I. A. Nekrasov, D. E. Kondakov, T. M. Rice and M. Sigrist: Eur. Phys. J. B **25** (2002) 191.
31) S. Nakatsuji et al.: Phys. Rev. Lett. **90** (2003) 137202; S. Nakatsuji and Y. Maeno: Phys. Rev. Lett. **84** (2000) 2666.
32) K. Sreedhar: et al., J. Solid State Comm. **110** (1994) 208; Z. Zhang, et al.: J. Solid State Comm. **108** (1994) 402; **117** (1995) 236.
33) Y. Kobayashi, S. Taniguchi, M. Kasai, M. Sato, T. Nishioka and M. Kontani: J. Phys. Soc. Jpn **65** (1996) 3978.
34) M. Sigrist and M. Troyer: Eur. Phys. J. B **39** (2004) 207.
35) Z. Fang, N. Nagaosa and K. Terakura: Phys. Rev. B **69** (2004) 45116.
36) A. Koga, N. Kawakami, T. M. Rice and M. Sigrist: cond-mat/0406457.
37) M. Potthoff: Eur. Phys. J. B **32** (2003) 429; M. Potthoff: ibid **36** (2003) 335; K. Pozgajčić: cond-mat/0407172.
38) J. M. Luttinger: Phys. Rev. **118** (1960) 1417.
39) K. Inaba, A. Koga, S. Suga and N. Kawakami: cond-mat/0506150.
40) M. Potthoff: Phys. Rev. B **64** (2001) 165114.