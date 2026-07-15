PHYSICAL REVIEW B 103, 104503 (2021)

Two-dimensional topological superconductivity candidate in a van der Waals layered material

Jing-Yang You, $^{1}$ Bo Gu, $^{2}$ Gang Su, $^{2}$ and Yuan Ping Feng $^{1,3,*}$

$^{1}$ Department of Physics, National University of Singapore, 2 Science Drive 3, Singapore 117551
$^{2}$ Kavli Institute for Theoretical Sciences, and CAS Center for Excellence in Topological Quantum Computation, University of Chinese Academy of Sciences, Beijng 100190, China
$^{3}$ Centre for Advanced 2D Materials, National University of Singapore, 6 Science Drive 2, Singapore 117546

![](./images/817398224263315457_1.jpg)
(Received 7 January 2021; revised 19 February 2021; accepted 22 February 2021; published 2 March 2021)

Two-dimensional (2D) topological superconductors are highly desired because they not only offer opportunities for exploring novel exotic quantum physics but also possess potential applications in quantum computation. However, there are few reports about 2D superconductors, let alone topological superconductors. Here, we find a 2D monolayer $W_2N_3$, which can be exfoliated from its real van der Waals bulk material with much lower exfoliation energy than $MoS_2$, to be a topological metal with exotic topological states at different energy levels. Owing to the Van Hove singularities, the density of states near the Fermi level are high, making the monolayer a compensate metal. Moreover, the monolayer $W_2N_3$ is unveiled to be a superconductor with the superconducting transition temperature $T_C \sim 22$ K and a superconducting gap of about 5 meV based on the anisotropic Migdal-Eliashberg formalism, arising from the strong electron-phonon coupling around the $\Gamma$ point, and the 2D superconductor is phonon mediated and fits the BCS mechanism with an Ising-type pairing. Because of the strong electron and lattice coupling, the monolayer displays a non-Fermi liquid behavior in its normal states at temperatures lower than 80 K, where the specific heat exhibits $T^3$ behavior and the Wiedemann-Franz law is dramatically violated. Our findings not only provide a platform to study the emergent phenomena in 2D topological superconductors, but also open a door to discover more 2D high-temperature topological superconductors in van der Waals materials.

DOI: 10.1103/PhysRevB.103.104503

### I. INTRODUCTION

Two-dimensional (2D) materials have been extensively studied due to their intriguing properties, such as magnetism [1–4], topological states [5–7], superconductivity [8–10], and so on. Since the successful exfoliation of graphene in 2004 [11], several 2D materials including $MoS_2$ [12,13], $CrI_3$ [1], $CrGeTe_3$ [2], etc., have been synthesized in experiments. Among these 2D materials, single atomic layer materials are particularly fascinating because they can be easily exfoliated from their van der Waals bulk materials and can be constructed into multifarious heterostructures to realize composite and extraordinary physical phenomena [14–19].

2D superconductors exfoliated from van der Waals bulk materials represent a unique class of 2D superconductivity because of the easy fabrication and the absence of the substrate [20–27]. While there are exotic properties related to them, the discovery of these exfoliated 2D superconductors has been rarely reported. The monolayer transition-metal dichalcogenides $NbSe_2$, $TaS_2$, and $TiSe_2$ display coexisting superconductivity and charge density waves driven by electron-phonon coupling (EPC) [10,22,27–33]. Recently, the monolayer $NiTe_2$ was reported to be a two-gap superconductor with $T_C \sim 5.7$ K, and the $T_C$ can be enhanced to 11.3 K by inserting one lithium atomic layer into bilayer $NiTe_2$ [34]. These 2D superconductors provide great opportunities for exploring fascinating quantum physics. The discovery of 2D topological materials, such as quantum spin Hall [5,6], quantum anomalous Hall insulators [7], and topological (semi) metals [35–37] sheds insightful light on the study of emerging physical phenomena because of the interplay of superconductivity and nontrivial topology. The emergent topological superconductors with Majorana fermions are thought to be useful for fault-tolerant quantum computation [38–40]. Topological superconductivity was proposed to be induced in topological boundary states of heterostructures composed of topological materials and superconductors by proximity effects [38–40]. However, the interface conditions dramatically influence the observation of topological superconductivity. Therefore, discovering 2D materials with simultaneously superconductivity and nontrivial topology will be of great value to achieve topological superconductivity. Although several 2D superconductors have been obtained, very few of them can exhibit topological states [41–46]. Thus, a crucial issue is to fabricate novel 2D materials with simultaneously superconductivity and nontrivial topology, where van der Waals materials may play an important role.

In this paper, we report a detailed investigation of the superconductivity and nontrivial electronic topology in 2D monolayer $W_2N_3$ [47]. The monolayer $W_2N_3$ exhibits a topological metal with three nodal lines traversing the whole

*phyfyp@nus.edu.sg

2469-9950/2021/103(10)/104503(6)
104503-1
©2021 American Physical Society

Brillouin zone (BZ), which are protected by the symmetries. Topological surface states with respect to these nontrivial band topology are also investigated. Moreover, the monolayer $\text{W}_2\text{N}_3$ is found to be a superconductor with the superconducting transition temperature of about 22 K and the superconducting gap up to 5 meV based on the anisotropic Midgal-Eliashberg formalism. This 2D superconductor is phonon mediated and fits the BCS mechanism with Ising-type pairing. The high $T_C$ and large superconducting gap are revealed to result from the enhanced EPC near the Fermi level at the $\Gamma$ point. The strong EPC comes from the high density of states near the Fermi level brought about by the Van Hove singularities near the Fermi level, leading to more electrons susceptible to pairing mediated by phonons. In addition, owing to the strong EPC, the normal states of monolayer $\text{W}_2\text{N}_3$ perform as a non-Fermi liquid at temperatures lower than 80 K, where the electrical specific heat shows a cubic dependence of temperature and the Wiedemann-Franz law is obviously violated. The coexistence of superconductivity and nontrivial band topology in this layered material makes it an inevitable platform to study topological superconductivity.

## II. CALCULATION METHOD

Our first-principles calculations were based on the density functional theory as implemented in the QUANTUM ESPRESSO package [48], using the full relativistic pseudopotential. The vacuum layer was set to $15$ $\mathring{\text{A}}$. To warrant an energy convergence of less than 1 meV per atom, the planewave kinetic-energy cutoff was set as 100 Ry and the energy cutoff for charge density was set as 1250 Ry. The structural optimization was performed until the forces on atoms were less than 1 meV. An unshifted BZ $\mathbf{k}$ point mesh of $20\times20\times1$ was utilized for electronic charge density calculations. The phonon modes are computed within density-functional perturbation theory [16] on a $10\times10\times1$ $\mathbf{q}$ mesh. The EPW code [49–51] was employed for the calculation of superconducting gap with both fine $\mathbf{k}$ and $\mathbf{q}$ meshes of $100\times100\times1$ in the BZ. The surface spectrum was calculated by using the Wannier functions and the iterative Green's function method [52–55]. The electronic and phonon transport properties were calculated with the packages BOLTZTRAP [56] and SHENGBTE [57], respectively.

## III. CRYSTAL STRUCTURE

The bulk $\text{W}_2\text{N}_3$ has a van der Waals layered crystal structure with the space group of $P6_3/mmc$ (No. 194) [58]. It is composed of inversion symmetric N-W-N-W-N layers with two 1T N-W-N layers sharing one layer of N atoms as shown in Fig. 1(a), and shows AB stacking along the (0001) direction. The monolayer $\text{W}_2\text{N}_3$ with the space group of $P\bar{6}m2$ (No. 187) can be easily exfoliated from its bulk material due to the low exfoliation energy of 46.6 meV/atom [47,59], which is much lower than that for monolayer $\text{MoS}_2$ with 76.3 meV/atom [60]. The in-plane lattice constant of monolayer $\text{W}_2\text{N}_3$ is optimized to be $a=2.864$ $\mathring{\text{A}}$, which is reasonable compared with the in-plane lattice constant of its bulk [58].

![](./images/817398224263315457_2.jpg)

FIG. 1. (a) Top and side views of the crystalline structure of monolayer $\text{W}_2\text{N}_3$. (b) Electronic band structures of monolayer $\text{W}_2\text{N}_3$ without (dash blue lines) and with (solid red lines) SOC and the corresponding partial density of states (DOS) with SOC. The Brillouin zone (BZ) with high symmetry paths is inserted.

## IV. TOPOLOGICAL STATES

The electronic structure of monolayer $\text{W}_2\text{N}_3$ without and with spin-orbital coupling (SOC) as well as the partial DOS with SOC are plotted in Fig. 1(b). By comparing the electronic band structures of monolayer $\text{W}_2\text{N}_3$ without and with SOC, one may observe that the SOC removes some degenerate points and significantly changes the band structure because of the heavy W atoms possessing relative large SOC. Thus, all results discussed in the following were calculated with SOC included. For monolayer $\text{W}_2\text{N}_3$, there are four bands crossing the Fermi level, making the monolayer a compensated metal as shown in Fig. 1(b). There are three flower-shaped hole pockets (labeled as $S_{\Gamma_{1,2,3}}$, from the inside out) and one electron pocket ($S_{\Gamma_4}$) at the $\Gamma$ point. At the centers of the boundary of BZ, M, are elliptical hole ($S_{\text{M}_1}$) and electron ($S_{\text{M}_2}$) pockets [Fig. 2(a)]. The W and N atoms contribute almost equally to the low energy band structure and DOS near Fermi level because of the large $p$-$d$ hybridization. The band structures present many interesting features: the SOC lifts the degenerate points at 0.5 eV above the Fermi level, leading to the nontrivial band topology characterized by the topological invariant $Z_2=1$; both without and with SOC the Weyl points at about 1.5 eV below Fermi level at K (K') points are stable, which are protected by the symmetries at K (K') points; it is interesting to note that the twofold band degeneracy along the high symmetry lines $\Gamma$-M exists both without and with SOC; there are several Van Hove singularities in the band structure leading to sharp peaks of DOS, in particular, the Van Hove singularities at about 0.1 eV below the Fermi level bringing about high DOS near the Fermi level. The twofold degeneracy along $\Gamma$-M high symmetry lines is protected by the symmetries because, when SOC is included, any point on $\Gamma$-M lines belongs to the group $G_8^5$ with the reality of

![](./images/817398224263315457_3.jpg)

FIG. 2. (a) Fermi surfaces (red lines) for monolayer W₂N₃. The surface states of monolayer W₂N₃ projected on (b) (111), (c) (100), and (d) (010) planes, respectively. Warmer colors represent higher local density of states and blue regions indicate the bulk band gap.

$a$, which only possesses 2D irreducible representation [61], constraining the twofold degeneracy along $\Gamma$-M at all energy scales. These nontrivial topological states are fully reflected in their surface states as shown in Figs. 2(b)-2(d), where abundant topological surface states can be seen.

### V. SUPERCONDUCTIVITY

The metallic property with high DOS near the Fermi level motivated us to investigate the possible superconductivity. The phonon spectra, the phonon density of states (PhDOS), the Eliashberg electron-phonon spectral function $\alpha^2 F(\omega)$, and the cumulative frequency dependent EPC $\lambda(\omega)$ are shown in Fig. 3(a). The absence of imaginary frequency modes indicates the dynamical stability of monolayer W₂N₃ as shown in Fig. 3(a). From the projected PhDOS, we find that W atoms vibrate in the low-frequency region, while N atoms vibrate in the relative higher frequency region because their distinct atomic masses, and the phonon vibrational modes of W and N atoms are separated by a phonon spectral energy gap of about 6 meV. $\alpha^2 F(\omega)$ displays a dominant peak centered around 10 meV at the low-frequency region, while $\alpha^2 F(\omega)$ is more spread at the high-frequency region. The cumulative frequency-dependent EPC $\lambda(\omega)$ can be calculated by integrating $\alpha^2 F(\omega)$. From the calculated $\lambda(\omega)$, we find that the low-frequency phonons [below the phonon spectral gap (35 meV)] account for 74% of the total EPC $[\lambda = \lambda(\infty) = 1.47]$. Thus, W atoms make the main contribution to the EPC. Utilizing our calculated $\alpha^2 F(\omega)$ and $\lambda(\omega)$ together with a typical value of the effective screened Coulomb repulsion constant $\mu^* = 0.1$, the superconducting transition temperature $T_C$ is calculated to be 21 K with the McMillan-Allen-Dynes approach [62-64], which is the highest reported for 2D superconductors exfoliated from van der Waals bulk materials.

![](./images/817398224263315457_4.jpg)

FIG. 3. (a) The phonon spectrum and phonon density of states (PhDOS) (multiply 5), Eliashberg spectral function $\alpha^2 F(\omega)$, and the cumulative frequency-dependent of EPC $\lambda(\omega)$ of monolayer W₂N₃ at ambient pressure. (b) Quasiparticle DOS in the superconducting state for two representative temperatures of 6 K (red dashed line) and 18 K (blue dash-dotted line). The black dashed line indicates the DOS of normal state, which is normalized to 1 at the Fermi level. The superconducting DOS $N_S(\omega)$ becomes 1 beyond the highest phonon energy. (c) Anisotropic superconducting gap of monolayer W₂N₃ on the Fermi surface as a function of temperature. Red dashed curve is BCS fit of the superconducting gap. (d) Momentum-resolved superconducting gap $\Delta_k$ on the Fermi surface (blue dashed lines) at 10 K, where warmer color (red) indicates bigger $\Delta_k$. (e) Momentum-resolved electron-coupling strength $\lambda_k$ within 0.2 eV on the Fermi surface (blue dashed curves). Warmer colors (dark red) indicates larger $\lambda_k$.

Figure 3(b) shows the quasiparticle DOS in the superconducting state at two representative temperatures of 6 and 18 K, relative to the DOS in the normal state as a function of frequency $\omega$ (meV) based on the anisotropic Migdal-Eliashberg theory [49-51]. We can observe that the superconducting gaps at 6 and 18 K are about 5 and 4 meV, respectively. The $k$-resolved superconducting gaps on the Fermi surface, $\Delta_k(T)$, for several temperatures below 20 K with $\omega = 0$, as well as the BCS fit for the superconducting gap are displayed in Fig. 3(c). It is seen that the superconducting gap vanishes around 21.7 K, which is a little higher than the $T_C$ (21 K)

![](./images/817398224263315457_5.jpg)

FIG. 4. (a) Temperature dependence of electronic specific heat
C of monolayer $W_2N_3$. The upper and lower insets are the enlarged
parts of the specific heat at temperatures below $T_C$ ($T < 20$ K), and
above $T_C$ ($20 < T < 80$ K), respectively. The black dashed lines
are fitting curves at different temperature regions. (b) Temperature-
dependent electrical ($\sigma$) and thermal ($\kappa_e$) conductivities, and Lorenz
number $L$ [$L = \kappa_e/(\sigma T)$]. (c) The mode-resolved lattice thermal
conductivity $\kappa_p$ as a function of temperature. (d) The mode-resolved
phonon lifetime as a function of frequency at 300 K.

obtained with the McMillan-Allen-Dynes approach, and the
zero-temperature superconducting gap is about 5 meV.

Figure 3(d) shows the momentum-resolved superconduct-
ing gap on the Fermi surface. On the whole Fermi surface,
there are finite superconducting gaps, indicating the Fermi
surface is fully gapped below$T_C$. The superconducting gap
on the $S_{\Gamma_1}$ line exhibits larger gap distribution around the
lowland on $\Gamma$-K paths, while the largest superconducting gaps
on the $S_{\Gamma_3}$ and $S_{\Gamma_4}$ lines distribute on $\Gamma$-M paths, and the
superconducting gap on the $S_{\Gamma_2}$ line is smaller than that on
the above three Fermi surface lines. The superconducting gaps
on the $S_{M_1}$ and $S_{M_2}$ lines is about 2 meV smaller than that on
the $S_\Gamma$ lines. It is noted that the superconducting gaps both on
the $S_\Gamma$ and $S_M$ lines are highly anisotropic. The regions of the
Fermi surface with the largest superconducting gap coincide
with the EPC strength $\lambda_k$ as shown in Fig. 3(e). Thus, the
high $T_C$ and large $\Delta_k$ in monolayer $W_2N_3$ are mainly from
the strong EPC of the Fermi surface at the $\Gamma$ point.

## VI. TRANSPORT PROPERTIES

It is worth mentioning that due to the exceedingly strong
coupling between the electrons and phonons, the normal
state of monolayer $W_2N_3$ may be a non-Fermi liquid. The
temperature-dependent electronic specific heat of monolayer
$W_2N_3$ is calculated as shown in Fig. 4(a). It is noted that the
specific heat $C(T)$ displays distinct features: at low tempera-
ture (below $T_C$), $C(T) \sim T^{-3/2} \cdot \exp(-a/T)$, i.e., the specific
heat accords with the low-temperature specific heat of BCS
superconductors (upper inset); at $20 < T < 80$ K, $C(T) \sim
T^3$ (lower inset); and at high temperature region ($T > 80$ K),
$C(T) \sim T$. It is clear that below 80 K, the normal stat shows
a non-Fermi liquid behavior [65].

To further verify this observation, the temperature-
dependent Lorenz number $L [=\kappa_e/(\sigma T)]$ is also studied, as
presented in Fig. 4(b). We can observe that the Lorenz number
$L$ is not a constant at temperatures below 80 K, which dramat-
ically violates the Wiedemann-Franz law [66], while at high
temperatures it shows almost a constant, indicating a Fermi
liquid behavior.

The lattice thermal conductivity is given in Fig. 4(c). It
can be observed at temperatures lower than 200 K, the lat-
tice thermal conductivity dominates, while at temperatures
above 200 K, the electrical thermal conductivity dominates.
It is noted that at low temperatures, the three acoustic modes
(modes 1–3) make the main contribution to lattice thermal
conductivity, while with the increase of temperature the con-
tribution of three optical branches from the vibration of N
atoms (modes 4–6) begins to match or even surpass that of the
acoustic branches. The optical branches from the vibration of
N atoms (modes 7–15) make little contribution to the thermal
conductivity at the whole temperature range.

To gain more insight into phonon transport of mono-
layer $W_2N_3$, the mode-resolved phonon lifetime is plotted
in Fig. 4(d). It is found that most phonon lifetimes of three
acoustic branches are comparable with three optical branches
from W atom vibration, showing a comparable contribution to
the lattice thermal conductivity, while the phonon lifetime of
the optical branches above 40 meV is shorter because of the
larger scatting rate. Thus, the N atoms contribute little to the
thermal conductivity, leading to the low thermal conductivity
of monolayer $W_2N_3$.

![](./images/817398224263315457_6.jpg)

FIG. 5. Spin texture of electronic bands that cross the Fermi
level, where the up (blue) and down (green) arrows represent the
opposite out-of-plane spin polarization directions. In this figure, we
only plot the spin texture of partial Fermi surface and the spin texture
in other parts of the Fermi surface can be obtained by symmetries.

## VII. DISCUSSION

To unveil the pairing mechanism and possible relation be-
tween the nontrivial band topology and superconductivity, the
spin texture of the Fermi surface is calculated as plotted in
Fig. 5. From Fig. 5(a), it is noted that each Fermi line is fully
out-of-plane spin polarized, indicating an Ising-type pairing
in monolayer $W_2N_3$. This result is similar to the superconduc-
tivity in ion-gated $MoS_2$ [8]. However, the magnitude of spin

moments is different at different $\mathbf{k}$ points on the Fermi surface for monolayer $\mathrm{W}_{2} \mathrm{~N}_{3}$. The spin-polarization direction between the outer and inner Fermi surface is inverted at the degenerate points on $\Gamma-M$ paths, at which the spin up and spin down are canceled. Comparing Figs. 3(d) and 5, it is interesting to note that the strength of EPC is related to the magnitude of spin moment, that is, where the magnitude of the spin moment is large, the EPC is also enhanced. Since the superconductivity is related to the degeneracy point, which determines the topological metal state of monolayer $\mathrm{W}_{2} \mathrm{~N}_{3}$, there may be some correlation between the topology and superconductivity in our system, which needs further deep-going study.

## VIII. SUMMARY

In this paper, we report that a 2D monolayer $\mathrm{W}_{2} \mathrm{~N}_{3}$ hosts simultaneously topological states and superconductivity. The monolayer is found to exhibit different topological states at different energy levels, including topological $Z_{2}$ insulators, Weyl semimetals, and topological nodal line metals. The exotic topological surface states are also investigated.

Furthermore, based on anisotropic Migdal-Eliashberg theory, the monolayer $\mathrm{W}_{2} \mathrm{~N}_{3}$ is predicted to be a phonon-mediated BCS superconductor with the superconducting transition temperature $T_{C} \sim 22 \mathrm{~K}$ and the superconducting gap $\Delta_{k} \sim 5 \mathrm{meV}$. The high $T_{C}$ and large $\Delta_{k}$ are unveiled to be from the enhanced electron and lattice coupling near the Fermi level at the $\Gamma$ point. Due to the large EPC, the normal state of monolayer $\mathrm{W}_{2} \mathrm{~N}_{3}$ performs as a non-Fermi liquid at temperatures below $80 \mathrm{~K}$, where the electrical specific heat displays a $T^{3}$ behavior and the Wiedemann-Franz law is dramatically violated. Our results will spur the observation of 2D high-temperature topological superconductivity.

## ACKNOWLEDGMENTS

This research/project is supported by the Ministry of Education, Singapore, under its MOE AcRF Tier 3 Award No. MOE2018-T3-1-002. B.G. and G.S. are supported in part by the National Key R&D Program of China (Grant No. 2018YFA0305800), the Strategic Priority Research Program of the Chinese Academy of Sciences (Grant No. XDB28000000), and NSFC (Grant No. 11834014).

[1] B. Huang, G. Clark, E. Navarro-Moratalla, D. R. Klein, R. Cheng, K. L. Seyler, D. Zhong, E. Schmidgall, M. A. McGuire, D. H. Cobden, W. Yao, D. Xiao, P. Jarillo-Herrero, and X. Xu, Nature 546, 270 (2017).

[2] C. Gong, L. Li, Z. Li, H. Ji, A. Stern, Y. Xia, T. Cao, W. Bao, C. Wang, Y. Wang, Z. Q. Qiu, R. J. Cava, S. G. Louie, J. Xia, and X. Zhang, Nature 546, 265 (2017).

[3] Y. Deng, Y. Yu, Y. Song, J. Zhang, N. Z. Wang, Z. Sun, Y. Yi, Y. Z. Wu, S. Wu, J. Zhu, J. Wang, X. H. Chen, and Y. Zhang, Nature 563, 94 (2018).

[4] D. J. O'Hara, T. Zhu, A. H. Trout, A. S. Ahmed, Y. K. Luo, C. H. Lee, M. R. Brenner, S. Rajan, J. A. Gupta, D. W. McComb, and R. K. Kawakami, Nano Lett. 18, 3125 (2018).

[5] B. A. Bernevig, T. L. Hughes, and S.-C. Zhang, Science 314, 1757 (2006).

[6] M. Konig, S. Wiedmann, C. Brune, A. Roth, H. Buhmann, L. W. Molenkamp, X.-L. Qi, and S.-C. Zhang, Science 318, 766 (2007).

[7] C.-Z. Chang, J. Zhang, X. Feng, J. Shen, Z. Zhang, M. Guo, K. Li, Y. Ou, P. Wei, L.-L. Wang, Z.-Q. Ji, Y. Feng, S. Ji, X. Chen, J. Jia, X. Dai, Z. Fang, S.-C. Zhang, K. He, Y. Wang, L. Lu, X.-C. Ma, and Q.-K. Xue, Science 340, 167 (2013).

[8] Y. Saito, Y. Nakamura, M. S. Bahramy, Y. Kohama, J. Ye, Y. Kasahara, Y. Nakagawa, M. Onga, M. Tokunaga, T. Nojima, Y. Yanase, and Y. Iwasa, Nat. Phys. 12, 144 (2015).

[9] J. M. Lu, O. Zheliuk, I. Leermakers, N. F. Q. Yuan, U. Zeitler, K. T. Law, and J. T. Ye, Science 350, 1353 (2015).

[10] X. Xi, Z. Wang, W. Zhao, J.-H. Park, K. T. Law, H. Berger, L. Forró, J. Shan, and K. F. Mak, Nat. Phys. 12, 139 (2015).

[11] K. S. Novoselov, Science 306, 666 (2004).

[12] A. Splendiani, L. Sun, Y. Zhang, T. Li, J. Kim, C.-Y. Chim, G. Galli, and F. Wang, Nano Lett. 10, 1271 (2010).

[13] Y. Li, H. Wang, L. Xie, Y. Liang, G. Hong, and H. Dai, J. Am. Chem. Soc. 133, 7296 (2011).

[14] A. K. Geim and I. V. Grigorieva, Nature 499, 419 (2013).

[15] K. S. Novoselov, A. Mishchenko, A. Carvalho, and A. H. C. Neto, Science 353, aac9439 (2016).

[16] S. Baroni, S. de Gironcoli, A. D. Corso, and P. Giannozzi, Rev. Mod. Phys. 73, 515 (2001).

[17] M.-Y. Li, C.-H. Chen, Y. Shi, and L.-J. Li, Mater. Today 19, 322 (2016).

[18] J. Zhang, L. Du, S. Feng, R.-W. Zhang, B. Cao, C. Zou, Y. Chen, M. Liao, B. Zhang, S. A. Yang, G. Zhang, and T. Yu, Nat. Commun. 10, 4226 (2019).

[19] C. Gong, E. M. Kim, Y. Wang, G. Lee, and X. Zhang, Nat. Commun. 10, 2657 (2019).

[20] Y. Saito, T. Nojima, and Y. Iwasa, Nat. Rev. Mater. 2, 16094 (2016).

[21] I. Guillamón, H. Suderow, S. Vieira, L. Cario, P. Diener, and P. Rodière, Phys. Rev. Lett. 101, 166407 (2008).

[22] M. M. Ugeda, A. J. Bradley, Y. Zhang, S. Onishi, Y. Chen, W. Ruan, C. Ojeda-Aristizabal, H. Ryu, M. T. Edmonds, H.-Z. Tsai, A. Riss, S.-K. Mo, D. Lee, A. Zettl, Z. Hussain, Z.-X. Shen, and M. F. Crommie, Nat. Phys. 12, 92 (2015).

[23] Y. Cao, V. Fatemi, S. Fang, K. Watanabe, T. Taniguchi, E. Kaxiras, and P. Jarillo-Herrero, Nature 556, 43 (2018).

[24] D. Jiang, T. Hu, L. You, Q. Li, A. Li, H. Wang, G. Mu, Z. Chen, H. Zhang, G. Yu, J. Zhu, Q. Sun, C. Lin, H. Xiao, X. Xie, and M. Jiang, Nat. Commun. 5, 5708 (2014).

[25] Y. Yu, L. Ma, P. Cai, R. Zhong, C. Ye, J. Shen, G. D. Gu, X. H. Chen, and Y. Zhang, Nature 575, 156 (2019).

[26] X. Xi, L. Zhao, Z. Wang, H. Berger, L. Forró, J. Shan, and K. F. Mak, Nat. Nanotechnol. 10, 765 (2015).

[27] E. Navarro-Moratalla, J. O. Island, S. Mañas-Valero, E. Pinilla-Cienfuegos, A. Castellanos-Gomez, J. Quereda, G. Rubio-Bollinger, L. Chirolli, J. A. Silva-Guillén, N. Agraït, G. A. Steele, F. Guinea, H. S. J. van der Zant, and E. Coronado, Nat. Commun. 7, 11043 (2016).

[28] T. Valla, A. V. Fedorov, P. D. Johnson, P.-A. Glans, C. McGuinness, K. E. Smith, E. Y. Andrei, and H. Berger, *Phys. Rev. Lett.* **92**, 086401 (2004).

[29] F. Zheng, Z. Zhou, X. Liu, and J. Feng, *Phys. Rev. B* **97**, 081101(R) (2018).

[30] F. Zheng and J. Feng, *Phys. Rev. B* **99**, 161119(R) (2019).

[31] B. Sipos, A. F. Kusmartseva, A. Akrap, H. Berger, L. Forró, and E. Tutiš, *Nat. Mater.* **7**, 960 (2008).

[32] R. A. Klemm, *Physica C: Superconductivity and its Applications* **514**, 86 (2015).

[33] M. Calandra and F. Mauri, *Phys. Rev. Lett.* **106**, 196406 (2011).

[34] F. Zheng, X.-B. Li, P. Tan, Y. Lin, L. Xiong, X. Chen, and J. Feng, *Phys. Rev. B* **101**, 100505(R) (2020).

[35] A. A. Burkov, *Nat. Mater.* **15**, 1145 (2016).

[36] C.-K. Chiu, J. C.Y. Teo, A. P. Schnyder, and S. Ryu, *Rev. Mod. Phys.* **88**, 035005 (2016).

[37] A. Bansil, H. Lin, and T. Das, *Rev. Mod. Phys.* **88**, 021004 (2016).

[38] L. Fu and C. L. Kane, *Phys. Rev. Lett.* **100**, 096407 (2008).

[39] M. Z. Hasan and C. L. Kane, *Rev. Mod. Phys.* **82**, 3045 (2010).

[40] X.-L. Qi and S.-C. Zhang, *Rev. Mod. Phys.* **83**, 1057 (2011).

[41] Y.-F. Lv, W.-L. Wang, Y.-M. Zhang, H. Ding, W. Li, L. Wang, K. He, C.-L. Song, X.-C. Ma, and Q.-K. Xue, *Science Bull.* **62**, 852 (2017).

[42] M. Liao, Y. Zang, Z. Guan, H. Li, Y. Gong, K. Zhu, X.-P. Hu, D. Zhang, Y. Xu, Y.-Y. Wang, K. He, X.-C. Ma, S.-C. Zhang, and Q.-K. Xue, *Nat. Phys.* **14**, 344 (2018).

[43] G. C. Ménard, S. Guissart, C. Brun, R. T. Leriche, M. Trif, F. Debontridder, D. Demaille, D. Roditchev, P. Simon, and T. Cren, *Nat. Commun.* **8**, 2040 (2017).

[44] F. Fei, X. Bo, R. Wang, B. Wu, J. Jiang, D. Fu, M. Gao, H. Zheng, Y. Chen, X. Wang, H. Bu, F. Song, X. Wan, B. Wang, and G. Wang, *Phys. Rev. B* **96**, 041201(R) (2017).

[45] H. Leng, C. Paulsen, Y. K. Huang, and A. de Visser, *Phys. Rev. B* **96**, 220506(R) (2017).

[46] C. Liu, C.-S. Lian, M.-H. Liao, Y. Wang, Y. Zhong, C. Ding, W. Li, C.-L. Song, K. He, X.-C. Ma, W. Duan, D. Zhang, Y. Xu, L. Wang, and Q.-K. Xue, *Phys. Rev. Materials* **2**, 094001 (2018).

[47] H. Yu, X. Yang, X. Xiao, M. Chen, Q. Zhang, L. Huang, J. Wu, T. Li, S. Chen, L. Song, L. Gu, B. Y. Xia, G. Feng, J. Li, and J. Zhou, *Adv. Mater.* **30**, 1805655 (2018).

[48] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, *J. Phys.: Condens. Matter* **21**, 395502 (2009).

[49] F. Giustino, M. L. Cohen, and S. G. Louie, *Phys. Rev. B* **76**, 165108 (2007).

[50] E. R. Margine and F. Giustino, *Phys. Rev. B* **87**, 024505 (2013).

[51] S. Poncé, E. Margine, C. Verdi, and F. Giustino, *Comput. Phys. Commun.* **209**, 116 (2016).

[52] N. Marzari and D. Vanderbilt, *Phys. Rev. B* **56**, 12847 (1997).

[53] I. Souza, N. Marzari, and D. Vanderbilt, *Phys. Rev. B* **65**, 035109 (2001).

[54] Q. Wu, S. Zhang, H.-F. Song, M. Troyer, and A. A. Soluyanov, *Comput. Phys. Commun.* **224**, 405 (2018).

[55] M. P. L. Sancho, J. M. L. Sancho, J. M. L. Sancho, and J. Rubio, *J. Phys. F: Met. Phys.* **15**, 851 (1985).

[56] G. K. Madsen and D. J. Singh, *Comput. Phys. Commun.* **175**, 67 (2006).

[57] W. Li, J. Carrete, N. A. Katcho, and N. Mingo, *Comput. Phys. Commun.* **185**, 1747 (2014).

[58] S. Wang, X. Yu, Z. Lin, R. Zhang, D. He, J. Qin, J. Zhu, J. Han, L. Wang, H. kwang Mao, J. Zhang, and Y. Zhao, *Chem. Mater.* **24**, 3023 (2012).

[59] N. Mounet, M. Gibertini, P. Schwaller, D. Campi, A. Merkys, A. Marrazzo, T. Sohier, I. E. Castelli, A. Cepellotti, G. Pizzi, and N. Marzari, *Nat. Nanotechnol.* **13**, 246 (2018).

[60] J. Zhou, L. Shen, M. D. Costa, K. A. Persson, S. P. Ong, P. Huck, Y. Lu, X. Ma, Y. Chen, H. Tang, and Y. P. Feng, *Sci. Data* **6**, 86 (2019).

[61] H. Wondratschek, *Acta Crystallogr. Sect. A* **29**, 581 (1973).

[62] W. L. McMillan, *Phys. Rev.* **167**, 331 (1968).

[63] P. B. Allen and R. C. Dynes, *Phys. Rev. B* **12**, 905 (1975).

[64] F. Giustino, *Rev. Mod. Phys.* **89**, 015003 (2017).

[65] A. J. Schofield, *Contemp. Phys.* **40**, 95 (1999).

[66] R. Franz and G. Wiedemann, *Ann. Phys. (Berlin)* **165**, 497 (1853).