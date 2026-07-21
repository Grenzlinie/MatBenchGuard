PHYSICAL REVIEW B 89, 214113 (2014)

# Strain-induced control of domain wall morphology in ultrathin $PbTiO_{3}$ films

Zhijun Jiang, $^{1}$ Ruizhi Zhang, $^{1,2}$ Dawei Wang, $^{1,*}$ D. Sichuga, $^{3}$ C.-L. Jia, $^{1,4}$ and L. Bellaiche $^{5}$

$^{1}$ Electronic Materials Research Laboratory, Key Laboratory of the Ministry of Education and International Center for Dielectric Research, Xi'an Jiaotong University, Xi'an 710049, China
$^{2}$ Department of Physics, State Key Laboratory of Photoelectric Technology and Functional Materials (Cultivation Base), Northwest University, Xi'an 710069, China
$^{3}$ Physics Department, Augusta Technical College, Augusta, Georgia 30906, USA
$^{4}$ Peter Grünberg Institute and Ernst Ruska Centre for Microscopy and Spectroscopy with Electrons, Research Center Jülich, D-52425 Jülich, Germany
$^{5}$ Institute for Nanoscience and Engineering and Physics Department, University of Arkansas, Fayetteville, Arkansas 72701, USA

(Received 5 February 2014; revised manuscript received 3 June 2014; published 25 June 2014)

Ab initio effective Hamiltonian simulations reveal a strain-induced control of domain morphology in epitaxial $PbTiO_{3}$ ultrathin films being under open-circuit electrical boundary conditions. More precisely, rather different out-of-plane domain structures are found to be the ground state, depending on the value of the misfit strain. Examples include domain walls lying in different crystallographic planes or even being wandering. Analysis of the computations allows us to reveal the precise interactions responsible for such strain-driven domain reorganization.

DOI: 10.1103/PhysRevB.89.214113
PACS number(s): 77.80.Dj, 77.55.fg, 77.80.bn

## I. INTRODUCTION

Ferroelectric ultrathin films are promising candidates for various miniaturized applications because of their ferroelectric or piezoelectric properties. Dipolar nanodomains have been observed in such films, and have been intensively studied in the last ten years or so [1-16]. More recently, domain walls have attracted attention because they can play a crucial role in devices performance and even lead to novel phenomena. For instance, it has been shown that domain-wall motion contributes to more than $60\%$ of the measured piezoelectric coefficients [17], and room-temperature electronic conduc- tivity was reported at the ferroelectric domain walls in the insulating multiferroic $BiFeO_{3}$ [18]. Ferroelectricity was even discovered in the twin walls made of the nonpolar $CaTiO_{3}$ material [19,20]. Another interesting feature of domain walls is that changing their morphology can significantly affect physi- cal properties. For instance, different configurations of domain walls were systematically investigated in $BaTiO_{3}$ [21,22] and their influence on piezoelectricity was analyzed [23]. Similarly, the electrical conductance was recently reported to be a continuous function of the domain-wall orientation in hexagonal $ErMnO_{3}$ [24].

Given these findings, it is of obvious importance to determine if (i) the normal direction of the domain walls can be systematically controlled, and (ii) the formation of wandering domain walls can be engineered, in ultrathin films to achieve desired physical properties (note that by wandering walls, we mean labyrinthlike structures for which different parts of the walls have different normal directions, as experimentally found in Refs. [25,26]). In particular, one wonders if the widely used method to tune properties of ultrathin films [27], which is the variation of the misfit strain originating from the difference in lattice constants between the substrate and the material forming the film, can lead to the realization of items (i) and (ii).

The aim of this paper is to address the aforementioned items (i) and (ii) in thin films made of $PbTiO_{3}$ (PTO)—which is a prototype ferroelectric material-by taking advantage of a first-principles-derived effective Hamiltonian. Note that PTO systems, along with other well-known ferroelectric materials (e.g., $BaTiO_{3}$ ), have been widely investigated using ab initio methods, but focusing on aspects that are different from items (i) and (ii), to the best of our knowledge. Examplesof such aspects include the structure of the (001) and (011) surfaces [28], effects of external electric fields on structural properties of the (001) surfaces [29], critical thickness for ferroelectricity [30], and atomistic structure of the $180^{\circ}$ and $90^{\circ}$ domain boundaries and closure domains [31-33], as well as the use of a model effective Hamiltonian within molecular dynamics to understand how strain and electrodes can affect ferroelectric domains and diffuse transitions in PTO ultrathin films [34]. Here, we report that varying the magnitude of the misfit strains leads to (i) a change of the energy hierarchy of multidomain configurations having different normal directions to their walls, therefore resulting in a strain-induced control of such normal direction; and (ii) the engineering of the overall morphology (i.e., straight versus wandering) of the domain walls. Analysis of the atomistic simulations also reveals the microscopic interactions responsible for such desired controls.

## II. METHOD

We model (001) epitaxial films made of PTO and being under open-circuit electrical boundary conditions. We use a $12×12×12$ supercell that is periodic along the x and y axes (which are along the pseudocubic [100] and [010] directions, respectively), but finite along the nonperiodic z axis (which is along the [001] pseudocubic direction) with the termination layers being the Pb-O layer, to mimic such a film, which has a thickness of $\sim 4.8$ nm. The total internal energy $E_{tot}$ is provided by a first-principles-derived effective Hamiltonian [6,15,35-37], in which the degrees of freedom are the local soft modes (directly proportional to the electric dipoles and centered on the

*dawei.wang@mail.xjtu.edu.cn

1098-0121/2014/89(21)/214113(6)
214113-1
©2014 American Physical Society

JIANG, ZHANG, WANG, SICHUGA, JIA, AND BELLAICHE
PHYSICAL REVIEW B 89, 214113 (2014)

Ti ions) and oxygen octahedra tiltings at each five-atom cell, as well as the homogeneous and inhomogeneous strains. As consistent with measurements [38], this effective Hamiltonian predicts for PTO bulk (i) a Curie temperature $T_{C} \simeq 750$ K (note that, as consistent with Ref. [39], the on-site harmonic parameter of the effective Hamiltonian was reduced by 28.5% with respect to its local density approximation value to yield such Curie temperature); (ii) a tetragonal $P4mm$ phase for temperatures below $T_{C}$; and (iii) no long-range ordering of the (antiferrodistortive) oxygen octahedra tilting down to the lowest temperatures. In the case of the films, the open-circuit electrical boundary conditions were taken into account by including the inherent depolarization field in the effective Hamiltonian [40]. Epitaxial strains experienced by the films were also modeled by freezing some components of the homo- geneous strain tensors. More precisely, the strain components $\eta_{xy} = \eta_{yx} = 0$ and $\eta_{xx} = \eta_{yy} = (a_{\text{sub}} - a_{\text{PTO}})/a_{\text{PTO}}$, where $a_{\text{sub}}$ and $a_{\text{PTO}}$ are the lattice constants of the substrate and cubic PTO bulk at $T_{C}$, respectively, are fixed in simulations for any selected misfit strain. All the other strain components, the local soft modes, and oxygen octahedral tiltings (including those near the surfaces) are allowed to relax to minimize the free energy. Note that the $\eta_{xx} = \eta_{yy}$ misfit strain will be denoted by $s$ in the following, and will be varied from $-6\%$ to $+4\%$. With this effective Hamiltonian, up to 320 000 Monte Carlo (MC) sweeps are employed and the system is typically cooled down to low temperatures, for each considered $s$.

## III. RESULTS AND DISCUSSION
### A. Different domain morphologies

Figure 1 displays snapshots of predicted out-of-plane domain structures in the middle (001) $TiO_2$ layer of the film (i.e., the sixth layer along the [001] direction) for compressive strains $(s < 0)$, at a temperature $T = 10$ K. The red and blue regions show individual down and up domains, respectively, and arrows represent the out-of-plane dipoles at five-atom cells. Figure 1 clearly reveals that domains can adopt different morphologies, with the normal vector of the walls being along different directions: for small compressive strain (typically less than 1.6% in magnitude), the domain walls are usually found to lie in a (100) plane [cf. Fig. 1(a)], while for larger compressive strain (larger than 2.1% in strength), the (110) plane [see Fig. 1(c)] is typically favored for the formation of domain walls. Even more striking, for intermediate compressive strains, we numerically found that there is a formation of a wandering domain [shown in Fig. 1(b)] that has domain walls in the (100) or (110) plane, depending on the locations inside the ($x$-$y$) plane. These latter results are consistent with the experimental study of Ref. [25] conducted on $Pb(Zr_{0.2}, Ti_{0.8})O_3$ systems experiencing a lattice mismatch of about $-1.5\%$, and for which $180^\circ$ domains with strongly faceted domain walls and wandering walls were reported.

It has to be noted that in addition to out-of-plane domains, the films can also exhibit an ordering between its in-plane electric dipoles. To appreciate such fact, Fig. 2 depicts the

![](./images/814722050491940866_1.jpg)

FIG. 1. (Color online) Snapshots of the three different out-of-plane domain configurations typically found by the simulations, at compressive strains, at $T = 10$ K. Red and blue colors are used to represent domains with negative and positive components of the dipoles along the $z$ axis, which are separated by domain walls colored in green and yellow. Panels (a) and (c) represent the (100)- and (110)-type of domain walls, while panel (b) shows wandering domains.

214113-2

![](./images/814722050491940866_2.jpg)

FIG. 2. (Color online) Temperature-versus-misfit-strain phase diagram of the PTO ultrathin film of 4.8 nm thickness under open-circuit electrical boundary conditions. (i) $p$ indicates the paraelectric phase; (ii) $aa$ indicates a homogeneous phase with an in-plane polarization along the [110] direction; (iii) $c^d$ indicates a state with out-of-plane domains; (iv) the $abc^d$ phase possesses both out-of-plane domains and in-plane polarization having $x$ and $y$ components (the $bc^d$ phase is a special case of the $abc^d$ phase, where there is no polarization along the $x$ axis).

temperature-versus-misfit-strain diagram in the considered PTO film. Several important regions can be seen in this plot: (i) The paraelectric $p$ phase [41] exists at high temperatures for any misfit strain. (ii) For tensile strains $(s>0)$ and for temperatures below the transition temperature, the $aa$ phase [41] exists, for which there is no more out-of-plane domain but rather a homogeneous polarization lying along the in-plane pseudocubic [110] direction. (iii) For compressive strains $(s<0)$, the $c^d$ phase (the superscript $d$ refers to domains) [6] appears below the paraelectric-to-ferroelectric transition temperature. This is a phase solely formed by $180^\circ$ domains having opposite out-of-plane electric dipoles, as experimentally found in Ref. [2]. (iv) For $-2\% < s < 0$, at lower temperatures, there is the $bc^d$ phase that possesses an in-plane polarization along the $y$ axis, in addition to out-of-plane domains. (v) An $abc^d$ phase [6], in which an in-plane polarization having unequal $x$ and $y$ components is superimposed on the $180^\circ$ out-of-plane domains, is further found at even lower temperature, when $-1\% < s < 0$. It is important to realize that the appearance of close-flux domains for compressive strain $(s<0)$ can break the symmetry in the $x$-$y$ plane, which explains why the $P_x$ and $P_y$ components of the polarization can appear at different critical temperatures in this region. For instance, the evolution of $P_x$, $P_y$, and $P_z$ with respect to temperature for $s=-0.5\%$ (cf. Fig. 3) shows a $\sim$200 K difference in the transition temperature between $P_x$ and $P_y$ (note that the overall, macroscopic $P_z$ vanishes at this $s$ misfit strain for temperatures $\lesssim700$ K as a result of the formation of out-of-plane domains, and that it is still zero for higher temperatures because the system is in the paraelectric $p$ state). The next subsection provides additional atomistic information about the breaking in symmetry between $P_x$ and $P_y$, which is also consistent with Ref. [34] showing that $\varepsilon_{xx} \neq \varepsilon_{yy}$.

### B. Microscopic structure

Microscopic structure information (e.g., atomic positions) can be inferred from the Cartesian components of the local modes, $(u_x, u_y, u_z)$, which are directly proportional to local electric dipoles. Here we show how the local modes behave along a [100] line passing through the supercell, at $T=6$ K and for a misfit strain $s=-0.5\%$, in the $12 \times 12 \times 12$ supercell. Figures 4(a) and 4(b) report such information for a middle and the top (001) $TiO_2$ layers, respectively, in the case of the (ground state) (100) domain morphology. One can clearly see that, *inside the sample*, (i) $u_x$ and $u_y$ have similar magnitude at each unit cell [cf. Fig. 4(a)]; and (ii) $u_z$ is positive in the region extending from the third to eighth Ti sites along the [100] line, while it is negative in the remaining sites of this line, reflecting the formation of the out-of-plane up and

![](./images/814722050491940866_3.jpg)

FIG. 3. (Color online) Polarization of the PTO film as a function of temperature, for a misfit strain $s=-0.5\%$. The transition temperatures for $P_x$ and $P_y$ are different by $\sim$200 K. $P_z$ vanishes even below the critical temperature of $\sim$700 K because of the formation of out-of-plane domains. The magnitude of $P_y$ is approximately twice that of $P_x$ at low temperature ($T<100$ K).

![](./images/814722050491940866_4.jpg)

FIG. 4. (Color online) Local modes as a function of the Ti site index along a [100] line, at $T=6$ K and for a misfit strain $s=-0.5\%$, for a $12 \times 12 \times 12$ supercell. Panel (a) shows the result at a middle $TiO_2$ (001) layer (seventh layer along the $z$ axis) while panel (b) reports the same information but for the top, surface layer.

down domains. On the other hand, $u_x$ and $u_y$ significantly differ in behavior *at the surface* [cf. Fig. 4(b)]: all the $u_y$ are negative and similar at the different Ti sites existing along the [100] line, while $u_x$ evolves like a sine function and adopts negative as well as positive values, along that line. The dipole rotation associated with this behavior of $u_x$ near the surface is a known phenomenon [6,42] and occurs in order to close the flux associated with $180^\circ$ out-of-plane domains. On the other hand, since the normal of the domain wall is not along the $y$ axis (it is along the $x$ axis), $u_y$ does not need to significantly rotate within the film, even at the surface. This difference between the $u_x$ and $u_y$ components of the microscopic local modes naturally explains the difference between the macroscopic $P_x$ and $P_y$ components of the polarization depicted in Fig. 3.

### C. Origin of the different domain morphologies

Let us now try to understand the origin(s) for the three different morphologies of the out-of-plane domain walls shown in Fig. 1. To this end, Fig. 5 compares the total internal energy at low temperature (namely, $T=6$ K) of these three domain structures, as a function of $s$ varying between $-3.0\%$ and $-1.0\%$. Note that we numerically found that these three domain structures are stable/metastable for this range of $s$, and that above $0\%$ (i.e., for tensile strains), Fig. 2 indicates that states possessing out-of-plane domains are destabilized in favor of the homogeneous $aa$ phase. For $s>-1.6\%$, the (100)-type domain wall has a lower internal energy, as consistent with the experimental observation in PTO films grown on a $\text{SrTiO}_3$ substrate [2]. On the other hand, for $s<-2.1\%$, the (110) domain becomes energetically favorable. In addition, for $s$ ranging between $-2.1\%$ and $-1.6\%$, the three different configurations have almost degenerate energies. For instance, at $s=-1.8\%$, the (100)-type, the wandering, and the (110)-type domain structure have internal energy (with respect to the paraelectric phase and per five atoms) equal to $-34.32$, $-34.11$, and $-34.36$ meV, respectively. Anisotropy can therefore be considered as being annihilated when $s$ is around $-1.8\%$, which explains the occurrence of wandering domain walls. It is also consistent with the possibility that labyrinths [43,44] exist in that range of $s$, as recently reported for epitaxially strained PTO thin systems [26]. Figure 5 therefore shows that the morphology of the domain walls can be dramatically modified and controlled by varying the misfit strain, which is of obvious fundamental and technological interest.

![](./images/814722050491940866_5.jpg)

FIG. 5. (Color online) Dependence of the total internal energy on misfit strain at $T=6$ K, for the three predicted domain-wall morphologies.

![](./images/814722050491940866_6.jpg)

FIG. 6. (Color online) Decomposition of the total internal energy at $T=6$ K into different parts: (a) short-range dipolar interaction; (b) local mode self-energy and strain-dipole interactions; (c) long-range dipole-dipole interactions; and (d) the three energies shown in (a), (b), and (c) added together. The red curves with circles indicate the results obtained for (100)-type domain, the blue curves with stars correspond to (110)-type domain, while the green curves with squares show data for the wandering domain.

In order to understand the origin of such modification, Fig. 6 reports the decomposition of the total internal energy into several constituent parts [37], at $T=6$ K. These parts are the short-range dipolar interactions [Fig. 6(a)], the sum of the local mode self-energy and the energy resulting from the coupling between strain and local modes [Fig. 6(b)], and the long-range dipolar interactions [Fig. 6(c)]. These three different energies are then added together and displayed in Fig. 6(d). One can see that there is a competition between these energies, as consistent with what is known for the pattern structure formation in a variety of different systems [45], such as Langmuir films and two-dimensional magnetic garnets [46]. In particular, Fig. 6(a) reveals that the short-range interaction favors the (100)-type domain, likely because the (110)-type domain has a larger domain-wall area-per-total volume—therefore containing a larger relative number of opposite dipoles. On the other hand, the other two forms of the energies shown in Figs. 6(b) and 6(c) typically favor the (110)-type domain. At large compressive strain, the gain in the short-range interactions for the (100)-type domain with respect to the (110)-type domain is unable to compensate the preference of the other two energies to favor the (110)-type domain. On the other hand, for compressive strain smaller in magnitude than $\simeq1.5\%$, the difference in short-range interactions between the (100)-type and (110)-type domains is large enough to make the (100)-type domain of lower total internal energy. Such strain-dependent competition explains the strain-driven change in the normal of the most stable domain walls (it is interesting to realize that Ref. [34] found that a change of this normal direction can also occur by playing with the value of parameters associated with strain-phonon coupling). Moreover, Figs. 6(a)–6(c) further show that the domain with wandering walls has energy parts

that are typically in-between those of the (100)-type and (110)-type domains. As a result, for intermediate strains, it can have a total internal energy that is very close to that of these two latter domains, therefore providing an explanation of why domains with wandering walls can be observed for intermediate strains [25,26]. The energies shown in Fig. 6 are found to be the most important in determining the stability of the domain configuration. Note that another contribution to the total energy, namely the elastic energy, has approximately the same value for the different investigated configurations at a given misfit strain. In other words, the elastic energy only weakly depends on the domain morphology for a given epitaxial strain. However, this weak strain dependency (and in particular the strain dependency of the elastic energy associated with the local *inhomogeneous* strain) is enough to shift the energy of the different configurations, and therefore makes the internal energies of the three domains crossing from $\simeq-1.3\%$ in Fig. 6(d) (for which elastic energy is not considered) to $\simeq-1.8\%$ in Fig. 5 (where all interactions are included). Note also that the crossing of the *free* (rather than internal) energies associated with these three types of domains is likely to be temperature dependent, suggesting that the ranges of strains for which these three domains are the most stable configurations may change with temperature as well.

### D. Effects of film's thickness
We finally investigate how a film's thickness may affect the physical properties shown in this paper. Let us first recall that it is well established that the domain width is expected to obey the so-called Kittel law yielding a square-root dependence on film thickness [47]. Such dependency has already been observed in previous effective-Hamiltonian-based simulations on $\text{Pb}(\text{Zr}_{0.4},\text{Ti}_{0.6})\text{O}_3$ films [48]. To determine other effects of the film's thickness, we performed additional simulations on $\text{PbTiO}_3$ (PTO) films having different thicknesses, namely $\simeq1.2$ nm (using a $12\times12\times3$ supercell), 2.4 nm (as mimicked by a $12\times12\times6$ supercell), 3.2 nm (using a $12\times12\times8$ supercell), 4.8 nm (as modeled by a $12\times12\times12$ supercell), and 8 nm (using a $12\times12\times20$ supercell). The considered strain was kept the same and equal to $s=-0.5\%$ in these simulations. We numerically found that increasing the film thickness from 2.4 to 8 nm (i) does not significantly change the critical temperature at which the $x$ component of the polarization, $P_x$, begins to develop; (ii) only rather slightly decreases (from $\sim$550 K to $\sim$500 K) the temperature at which the $y$ component of the polarization, $P_y$, starts to form. These results indicates that these critical temperatures only weakly depend on the thickness of the ultrathin films for thickness ranging between 2.4 and 8 nm. Note that for the thinnest investigated film (that is of 1.2 nm thickness), both $P_x$ and $P_y$ begin to develop at $\simeq450$ K. In that case, and as indicated below, out-of-plane domains do not exist anymore.

Regarding the effect of the film thickness on domain morphologies, we found several interesting features. First of all, the $12\times12\times3$ supercell shows no sign of domain at the lowest available temperature (6 K). The electric dipoles rather all point along the in-plane [110] direction. Such finding is consistent with previous theoretical findings for $\text{Pb}(\text{Zr}_{0.4},\text{Ti}_{0.6})\text{O}_3$ films showing that, below 1.2 nm, the Kittel law does not apply anymore due to the disappearance of $180^\circ$ stripe domains [48]. It is also consistent with an experimental study on PTO films showing that no abrupt ferroelectric/dielectric transition is observed for layers thinner than four unit cells [49]. Moreover, we also discovered that the $12\times12\times6$ supercell adopts domain walls that are of the (110) type in its ground state, which contrasts with the case of the $12\times12\times8$, $12\times12\times12$, and $12\times12\times20$ supercells that all energetically prefer to adopt (100) domain type. As a result, relatively small film thickness can also influence the equilibrium domain morphologies for a given strain.

### IV. CONCLUSION
Our first-principles-based simulations reveal that the morphology of domain walls is controllable by strain in epitaxial (001) ultrathin films made of the prototype ferroelectric $\text{PbTiO}_3$ material. For instance, (100), (110), and even wandering domains are found to be stable at different misfit strains. Microscopic structure information is presented to understand the breaking in symmetry between $P_x$ and $P_y$ at some misfit strains, and further, the decomposition of the total internal energy into different parts allows us to precisely determine the energetic competition responsible for the strain-induced change in morphology of the domain walls. We thus hope that the present study extends the knowledge of ferroelectric and multifunctional materials as well as domain walls, and may be of technological relevance.

### ACKNOWLEDGMENTS
We thank Q. Zhang and P. Evans for discussions related to Ref. [26]. This work was financially supported by the National Natural Science Foundation of China (NSFC) under Grant No. 51390472 and the 111 Project (B14040). R.Z. acknowledges support from NSFC under Grant No. 11104220. L.B. acknowledges the financial support of NSF Grant No. DMR-1066158. We thank Shanghai Supercomputer Center for providing computational capability for some of our simulations.

[1] A. Munkholm, S. K. Streiffer, M. V. Ramana Murty, J. A. Eastman, C. Thompson, O. Auciello, L. Thompson, J. F. Moore, and G. B. Stephenson, *Phys. Rev. Lett.* **88**, 016101 (2001).

[2] S. K. Streiffer, J. A. Eastman, D. D. Fong, C. Thompson, A. Munkholm, M. V. Ramana Murty, O. Auciello, G. R. Bai, and G. B. Stephenson, *Phys. Rev. Lett.* **89**, 067601 (2002).

[3] C. Lichtensteiger, J.-M. Triscone, J. Junquera, and P. Ghosez, *Phys. Rev. Lett.* **94**, 047603 (2005).

[4] B. W. Wessels, *Annu. Rev. Mater. Res.* **37**, 659 (2007).

[5] P. Aguado-Puente and J. Junquera, *Phys. Rev. Lett.* **100**, 177601 (2008).

[6] D. Sichuga and L. Bellaiche, *Phys. Rev. Lett.* **106**, 196102 (2011).

[7] C. T. Nelson, B. Winchester, Y. Zhang, S.-J. Kim, A. Melville, C. Adamo, C. M. Folkman, S.-H. Baek, C.-B. Eom, D. G. Schlom, L.-Q. Chen, and X. Pan, *Nano Lett.* **11**, 828 (2011).

[8] M. D. Rossell, R. Erni, M. P. Prange, J.-C. Idrobo, W. Luo, R. J. Zeches, S. T. Pantelides, and R. Ramesh, *Phys. Rev. Lett.* **108**, 047601 (2012).

[9] D. Wang, E. K. H. Salje, S.-B. Mi, C.-L. Jia, and L. Bellaiche, *Phys. Rev. B* **88**, 134107 (2013).

[10] T. Tybell, P. Paruch, T. Giamarchi, and J.-M. Triscone, *Phys. Rev. Lett.* **89**, 097601 (2002).

[11] A. Grigoriev, D.-H. Do, D. M. Kim, C.-B. Eom, B. Adams, E. Dufresne, and P. G. Evans, *Phys. Rev. Lett.* **96**, 187601 (2006).

[12] M. J. Highland, T. T. Fister, M.-I. Richard, D. D. Fong, P. H. Fuoss, C. Thompson, J. A. Eastman, S. K. Streiffer, and G. B. Stephenson, *Phys. Rev. Lett.* **105**, 167601 (2010).

[13] Q. Zhang, R. Herchig, and I. Ponomareva, *Phys. Rev. Lett.* **107**, 177601 (2011).

[14] B. K. Mani, C.-M. Chang, and I. Ponomareva, *Phys. Rev. B* **88**, 064306 (2013).

[15] D. Sichuga and L. Bellaiche, *Phys. Rev. B* **85**, 214111 (2012).

[16] I. Kornev, H. Fu, and L. Bellaiche, *Phys. Rev. Lett.* **93**, 196104 (2004).

[17] S. B. Seshadri, A. D. Prewitt, A. J. Studer, D. Damjanovic, and J. L. Jones, *Appl. Phys. Lett.* **102**, 042911 (2013).

[18] J. Seidel, L. W. Martin, Q. He, Q. Zhan, Y. H. Chu, A. Rother, M. E. Hawkridge, P. Maksymovych, P. Yu, M. Gajek, N. Balke, S. V. Kalinin, S. Gemming, F. Wang, G. Catalan, J. F. Scott, N. A. Spaldin, J. Orenstein, and R. Ramesh, *Nat. Mater.* **8**, 229 (2009).

[19] L. Goncalves-Ferreira, S. A. T. Redfern, E. Artacho, and E. K. H. Salje, *Phys. Rev. Lett.* **101**, 097602 (2008).

[20] S. Van Aert, S. Turner, R. Delville, D. Schryvers, G. Van Tendeloo, and E. K. H. Salje, *Adv. Mater.* **24**, 523 (2012).

[21] J. Hlinka and P. Marton, *Phys. Rev. B* **74**, 104104 (2006).

[22] P. Marton, I. Rychetsky, and J. Hlinka, *Phys. Rev. B* **81**, 144125 (2010).

[23] P. Ondrejkovic, P. Marton, M. Guennou, N. Setter, and J. Hlinka, *Phys. Rev. B* **88**, 024114 (2013).

[24] D. Meier, J. Seidel, A. Cano, K. Delaney, Y. Kumagai, M. Mostovoy, N. A. Spaldin, R. Ramesh, and M. Fiebig, *Nat. Mater.* **11**, 284 (2012).

[25] C.-L. Jia, S.-B. Mi, K. Urban, I. Vrejoiu, M. Alexe, and D. Hesse, *Nat. Mater.* **7**, 57 (2008).

[26] Q. Zhang, 2014 Fundamental Physics of Ferroelectrics and Related Materials Workshop (unpublished); P. Evans and Q. Zhang (private communication).

[27] D. G. Schlom, L.-Q. Chen, C.-B. Eom, K. M. Rabe, S. K. Streiffer, and J.-M. Triscone, *Annu. Rev. Mater. Res.* **37**, 589 (2007).

[28] R. I. Eglitis and David Vanderbilt, *Phys. Rev. B* **76**, 155439 (2007).

[29] B. Meyer and David Vanderbilt, *Phys. Rev. B* **63**, 205426 (2001).

[30] Y. Umeno, B. Meyer, C. Elsässer, and P. Gumbsch, *Phys. Rev. B* **74**, 060101(R) (2006).

[31] S. Pöykkö and D. J. Chadi, *Appl. Phys. Lett.* **75**, 2830 (1999).

[32] T. Shimada, S. Tomoda, and T. Kitamura, *Phys. Rev. B* **81**, 144116 (2010).

[33] B. Meyer and David Vanderbilt, *Phys. Rev. B* **65**, 104111 (2002).

[34] S. Kouser, T. Nishimatsu, and U. V. Waghmare, *Phys. Rev. B* **88**, 064102 (2013).

[35] D. Sichuga, I. Ponomareva, and L. Bellaiche, *Phys. Rev. B* **80**, 134116 (2009).

[36] W. Zhong, D. Vanderbilt, and K. M. Rabe, *Phys. Rev. Lett.* **73**, 1861 (1994).

[37] W. Zhong and D. Vanderbilt, and K. M. Rabe, *Phys. Rev. B* **52**, 6301 (1995).

[38] S. Venkatesan, A. Vlooswijk, B. J. Kooi, A. Morelli, G. Palasantzas, J. T. M. De Hosson, and B. Noheda, *Phys. Rev. B* **78**, 104112 (2008).

[39] L. Walizer, S. Lisenkov, and L. Bellaiche, *Phys. Rev. B* **73**, 144105 (2006).

[40] I. Ponomareva, I. I. Naumov, I. Kornev, H. Fu, and L. Bellaiche, *Phys. Rev. B* **72**, 140102(R) (2005).

[41] N. A. Pertsev, A. G. Zembilgotov, and A. K. Tagantsev, *Phys. Rev. Lett.* **80**, 1988 (1998).

[42] C.-L. Jia, K. W. Urban, M. Alexe, D. Hesse, and I. Vrejoiu, *Science* **331**, 1420 (2011).

[43] A. N. Morozovska, E. A. Eliseev, J. J. Wang, G. S. Svechnikov, Y. M. Vysochanskii, V. Gopalan, and L-Q. Chen, *Phys. Rev. B* **81**, 195437 (2010).

[44] V. V. Shvartsman, B. Dkhil, and A. L. Kholkin, *Annu. Rev. Mater. Res.* **43**, 423 (2013).

[45] P. Heinig, L. E. Helseth, and Th. M. Fischer, *New J. Phys.* **6**, 189 (2004).

[46] J. R. Iglesias, S. Gonçalves, O. A. Nagel, and M. Kiwi, *Phys. Rev. B* **65**, 064447 (2002).

[47] G. Catalan, J. Seidel, R. Ramesh, and J. F. Scott, *Rev. Mod. Phys.* **84**, 119 (2012).

[48] B. Lai, I. Ponomareva, I. Kornev, L. Bellaiche, and G. Salamo, *App. Phys. Lett.* **91**, 152909 (2007).

[49] R. Meyer, A. Vailionis, and P. McIntyre, arXiv:0704.2441.