Physical Chemistry Chemical Physics

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: G. Liu, X. Feng, L. Wang, S. A. T. Redfern, Y. Xue, G. Gao and H. Liu, *Phys. Chem. Chem. Phys.*, 2019, DOI:
10.1039/C9CP02409C.

![](./images/812753700865966081_1.jpg)

This is an Accepted Manuscript, which has been through the
Royal Society of Chemistry peer review process and has been
accepted for publication.

Accepted Manuscripts are published online shortly after acceptance,
before technical editing, formatting and proof reading. Using this free
service, authors can make their results available to the community, in
citable form, before we publish the edited article. We will replace this
Accepted Manuscript with the edited and formatted Advance Article as
soon as it is available.

You can find more information about Accepted Manuscripts in the
Information for Authors.

Please note that technical editing may introduce minor changes to the
text and/or graphics, which may alter content. The journal's standard
Terms          com          
`在� **RainSamese**                                          � arrangem
Terms & Conditions and the Ethical guidelines still apply. In no event
shall the Royal Society of Chemistry be held responsible for any errors
or omissions in this Accepted Manuscript or any consequences arising
from the use of any information it contains.

![](./images/812753700865966081_2.jpg)

rsc.cc/pccp

# Theoretical investigation of the valence states in Au via the Au-F compounds under high pressure
View Article Online
DOI: 10.1039/C9CP02409C

Guangtao Liu¹,*, Xiaolei Feng²,³, Linyan Wang⁴, Simon A. T. Redfern²,³, Xue Yong⁵, Guoying Gao⁴, and Hanyu Liu¹,*

¹ Innovation Center for Computational Physics Methods and Software & State Key Laboratory of Superhard Materials, College of Physics, Jilin University, Changchun 130012, China

² Department of Earth Sciences, University of Cambridge, Cambridge, CB2 3EQ, UK
³ Center for High Pressure Science and Technology Advanced Research, Shanghai 201203, China

⁴ Center for High Pressure Science, State Key Laboratory of Metastable Materials Science and Technology, Yanshan University, Qinhuangdao 066004, China

⁵ Department of Physics and Engineering Physics, University of Saskatchewan, Saskatoon, S7N 5B2, Canada

In addition to known Au³⁺ and Au⁵⁺, it has recently been shown that Au is likely to possess unusual valence states in the compressed Au-F compounds. However, our simulations reveal that polymeric ground-state AuF₄ shows unexpected 6-fold coordinated rather than 4-fold, indicating more complete comprehending on the anomalous Au⁴⁺ is highly required. To fully understand the nature and origin of anomalous valence states in Au, we have extensively investigated the ground-state structures of Au-F compounds at high pressures using quantum mechanical computational methods. As a consequence, we identify several previously unreported (stable) AuF₂, AuF₃ and AuF₄ structures. Our results extend the known polymorphism of AuFₙ compounds and offer a fundamental understanding of the origin of unusual valence states in Au that prevail at high pressure.

Key words: gold fluoride, high pressure, first principles, ground state, valence state.

Corresponding authors:  liuguangtao@jlu.edu.cn (Guangtao Liu) and hanyuliu@jlu.edu.cn (Hanyu Liu)


### 1. Introduction

Gold (Au) is well known for its inert noble metallic character, remaining pristine and untarnished even when exposed to air.¹ As a result of the relativistic effect, Au is unique and apparently different from other elements (Ag and Cu) of the same group²⁻³, forming stable compounds, typically oxidized to $Au^{3+}$, under certain conditions. Of all compounds that may occur, fluorine (F), having the strongest electronegativity of all elements, is expected to be among the most effective at capturing electrons, oxidizing a metal to its highest valence state. The reaction of Au and F has indeed been reported, with new valence states occurring upon their combination, in particular in organic compounds.⁴ Most stable $AuF_3$ crystallizes in the space group $P6_122$ with Au atoms lying at the centers of elongated octahedra containing two Au-F₁ bonds ($d = 2.04$ Å), two Au-F₂ bonds ($d = 1.91$ Å) and weak cross-linking with $Au\cdots F$ (2.69 Å)⁵,⁶ (Fig. 1a). The square-planar $AuF_4$ units are joined by symmetrical fluoro bridges to form chains. The search for the other unconventional Au-F compounds with diverse Au valence states has attracted considerable attention, as evidenced by several theoretical and experimental reports that have been published in recent years⁷⁻¹². To date, $Au^{n+}$ ($n≠3$) have been reported in metastable phases, as molecular gas¹³⁻¹⁵ or in complex compounds with ligands¹⁶,¹⁷, with elusive $Au^{+}$, $Au^{2+}$, and $Au^{5+}$ occurring in certain of these aurides¹². The stable solid binary Au-F compounds with unusual oxidation states, by contrast, are relatively unexplored. In particular, the existence of crystalline $AuF_n$ with new oxidation states remains an open question under, especially, non-ambient condition such as high pressure.

Compression has been widely recognized as being highly effective in modifying the properties of materials, driving increased density via changes in inter-atomic distances, changes in bonding and in polyhedral arrangements and stacking. It may also induce charge transfer, and thus drive structural phase transition and stabilize new structures, especially involving the formation of unconventional stoichiometries representing new valence states that are generally inaccessible at ambient conditions. Of particular interest, in the context of Au-F system, are several theoretical investigations that suggest that Cs¹⁸, Ir¹⁹, Hg²⁰, I²¹, and Xe²² may show unexpected valence states at extreme pressures, even to the extent that negative oxidation states for Au were reported in the Li-Au compounds under high pressure²³. It seems, therefore that, compression provides a potential route to obtain new and

unconventional compounds with unusual valence states, for example (in this case) via the reaction of Au and F. Very recently, a study using density functional theory (DFT) reported that new valence states of Au exist via new stoichiometric compounds $AuF_4$ and $AuF_6$ under compression, indicating the existence of $Au^{4+}$ and $Au^{6+.24}$ It is noteworthy that, the stabilities of these compounds are highly sensitive to the ground states of phases across the Au-F system, where formation energies are finely balanced. Moreover, knowing their precise crystal structures adopted is key, as coordination number plays a fundamental role in controlling the physicochemical properties (especially the valence state) of these materials. With these points in mind, a further in-depth search of the ground states in this system is paramount in understanding the $AuF_n$ compounds in particular, and anomalous valence states of Au more generally.

Here, the possible Au-F structures across a range of chemical compositions ($AuF_n$, n=1-7) have been explored extensively at zero temperature and high pressure using crystal structure prediction methods with first principles total energy calculations. Different from earlier findings²⁴, we find that $AuF_3$ transforms from the ambient-pressure hexagonal structure ($P6_122$) to a new layered orthorhombic structure ($Cmc2_1$) at around 6 GPa. In addition, an orthorhombic $AuF_2$ phase ($Pnma$) and a 6-fold coordinated monoclinic $AuF_4$ phase ($C2/c$) are found to be energetically stable above about 15 and 6 GPa, respectively. Our results define the ground states in the $AuF_n$ system and confirm that Au can indeed adopt unconventional valence states under high pressures.

## 2. Computational details

The ground states of $AuF_n$ (n=1-7) were probed systematically using the Crystal structure Analysis by Particle Swarm Optimization (CALYPSO) code²⁵,²⁶, which is based on a search of the global minimum in the free energy surfaces calculated by DFT total energy calculations. CALYPSO provides structural predictions from the knowledge of only the chemical composition and given intensive thermodynamic variables, such as pressure. This method is found to be a powerful tool in discovering unreported crystal structures and resolving experimental uncertainties²⁷⁻³⁰. Our simulation cell comprised 1-6 formula units (f.u.) (2-24 atoms) of $AuF_n$(n=1-7) at 1, 10, and 20 GPa. The population size of each search

generation was 50. The best 20 structures from the previous generation and 30 new ones generated by the algorithm composed each subsequent generation. Generally, each search was steered by energy and terminated after the generation of 2000-2500 structures.

DFT calculations, including structural optimizations, calculations of enthalpies, electronic structures and phonons, were performed using the Vienna *Ab initio* Simulation Package (VASP)³¹ code with the Perdew-Burke-Ernzerhof³² exchange-correlation functional. The $5d^{10}6s^{1}$ and $2s^{2}2p^{5}$ electrons were treated as valence electrons for Au and F, respectively. To ensure that all enthalpy calculations were well converged to about 1 meV/atom, a Monkhorst-Pack grid was selected with sufficient density $(2\pi\times0.03$ Å⁻¹ for AuF and $2\pi\times0.08$ Å⁻¹ for $\text{AuF}_{n>1}$) in reciprocal space, as well as appropriate energy cutoff (700 eV). The electronic properties were calculated over a k-point grid of $2\pi\times0.04$ Å⁻¹ and 700 eV energy cutoff. The electron localization function (ELF)³³,³⁴ was also calculated using the VASP code. The Crystal Orbital Hamiltonian Population (COHP) formalism was used for bond analysis, as implemented in the LOBSTER package³⁵⁻³⁷. The phonon calculations were carried out using a finite displacement approach³⁸ through the PHONOPY code³⁹, which uses the Hellmann-Feynman forces calculated from the optimized supercells through the VASP code. In our calculations of phonon spectra, we selected $2\pi\times0.05$ Å⁻¹ and 900 eV as the parameters and extended the unit cells to supercell volumes larger than about $1000$ Å³. It has been proven that these computational schemes are suitable for the theoretical studies of aurides and can describe their properties well at high pressures.²³,⁴⁰

## 3. Results and discussion

### A. The ground states of $AuF_{n}$ under high pressure

First, the crystal structure evolution of $\text{AuF}_{3}$ was studied from 0 to 40 GPa. The lattice parameters and atomic positions for all candidate structures were allowed to fully relax until the target pressure was achieved during local geometry structure optimization. The ground-state hexagonal phase $(P6_{1}22)$ and the high-pressure $P$-$1$ phase proposed previously²⁴ were successfully reproduced, confirming the reliability of the computational scheme adopted in this work. Additionally, we found a previously unreported energetically stable structure with orthorhombic symmetry $(Cmc2_{1})$ at high pressure. The enthalpy curves as a function of

pressure for $AuF_3$ (Fig. S1a) demonstrate that our $Cmc2_1$ structure is stable between 6 and 25 GPa, then transforms to the $P$-$1$ phase. This 4-fold coordinated $Cmc2_1$ structure still contains square-planar $AuF_4$ units with distinct Au-F bonds (1.919, 1.923, 1.994 and 2.019 Å at 10 GPa). The square-planar units are connected through connecting F atoms and are co-planar, forming a layered structure (Fig. 1b). As would be anticipated, the high-pressure phase is denser than the ambient-pressure phase (Fig. S1b) with a volume collapse of 6.3% occurring at the pressure-induced first order phase transition from the $P6_122$ structure to the $Cmc2_1$ one.

In $AuF_2$, the enthalpies of candidates are shown in Fig. S2a. The low-pressure $P2_1/c$ phase is a layered structure, with square-planar $AuF_4$ units connected by four connecting F atoms (Fig. 1c). The high-pressure $Pnma$ phase is stable below 30 GPa and similar with their reported $Cmcm$ structure$^{24}$. This $Pnma$ structure is composed of isolated $AuF_2$ molecules, connecting to each other through weak Van der Waals interactions (Fig. 1d). Its coordination number is two and Au bonds with nonequivalent F atoms, with bond lengths of 1.950 and 1.964 Å at 20 GPa, a little shorter than those of $AuF_3$. The $AuF_2$ comprises a quasi-linear molecular structure with a near-linear F-Au-F angle of $177.3^\circ$. In AuF, our structure search reveals the enthalpies of the structures are much lower than those of the previous AuF structures$^{41}$ (Fig. S2b). The predicted structures in this work are both composed of zig-zag chains with an alternating sequence of atoms $\cdots$F-Au-F-Au-F$\cdots$ (Figs. 1e and 1f) with bond lengths ranging from 2.154 to 2.158 Å.

We turn now to the fluorine-rich part of the Au-F binary, which shows peroxidation states of Au. Unlike previous report of the isolated molecular $AuF_4$ unit$^{24}$, here $AuF_4$ adopts a structure with monoclinic symmetry ($C2/c$), which is composed of two nonequivalent 3-dimensional $AuF_6$ units (octahedra) connected through two fluoride bridges (Fig. 1g). $AuF_4$ exhibits typical polymerization characteristics, which may lower the enthalpy of this compound. The Au-F bond lengths range from 1.906 to 2.160 Å at 20 GPa. Au with four F atoms located in one plane, but with a small angle with the adjacent $\{AuF_4\}$ planes of other units. The known $AuF_5$ structure is composed of $Au_2F_{10}$ molecular units, with each pair of $AuF_6$ units sharing two F atoms (Fig. 1h). It was reported that the isolated $AuF_6$ molecules have six Au-F bonds of length 1.893 Å$^{24}$ (Fig. 1i). The shortest F-F distances are 2.35 and 2.57 Å in the $AuF_4$ and $AuF_6$ structures, respectively, which suggests that molecular $F_2$ does

not exist in these structures (the typical F-F bond length is $1.41$ $\AA$ in molecular $F_2$). $AuF_8$ is composed of the isolated $AuF_6$ molecules with additional F atoms (Fig. 1j). Intuitively, this phase is expected to be unstable and tends to decompose into a mixture of $AuF_6$ and $F_2$ due to the lack of an expected stable crystalline configuration.

### B. The stability of $AuF_n$ in the Au-F system

Our results on the ground-state enthalpies of $AuF_2$, $AuF_3$, and $AuF_4$ result in small adjustments to the convex hull of the Au-F system, which means that the relative stabilities of $AuF_n$ phases may be changed. Our calculated convex hulls, as a function of pressure, are shown in Figs. 2a-c. Our exploration of structures in the $AuF_n$ system shows that the well-known $AuF_3$ stoichiometry still has the lowest enthalpy across the entire Au-F binary system. The formation enthalpies of two stoichiometric compounds, $AuF_2$ and $AuF_4$, with Au adopting a variety of valence states, are negative with respect to end member mixtures at ~15 and ~6 GPa, respectively (Fig. 2d). Moreover, it has been shown in the previous work that the $R$-3 phase of $AuF_6$ is stable above $5$ $GPa^{24}$. It is very clear that, high pressure can lower the formation enthalpies of these new stoichiometries. The molar volumes of these products are lower than the sum of reactants, indicating that $AuF_2$, $AuF_4$, and $AuF_6$ are denser compared with $AuF_3$ and Au/F (Figs. S3). In fact, their synthesis pressures are likely to be higher than our theoretical values and additionally high temperature may be necessary, since the kinetic energy barrier of reaction must be overcome in the nucleation and growth of new phase.

A synthesizable solid-state compound needs also exhibit dynamic stability. In addition to considering their thermodynamic stabilities, we further confirmed the phonon dispersion curves of these new structures over the range of pressures corresponding to their enthalpic stabilities (Fig. S4). No imaginary phonon frequencies were found in across the entire Brillouin zone, confirming the dynamical stabilities of our new structures at these corresponding conditions. Even though some of the ground states of the $AuF_n$ compounds and the ranges of stable pressure are different from previous investigation$^{24}$, the stabilities of $AuF_2$, $AuF_3$, $AuF_4$, and $AuF_6$ under compression are validated here.

With increasing pressure, the potential energy surface of the Au-F system is changed markedly and become more complicated. Therefore, more local minima appear under

compression, corresponding to new (and rather diverse) stoichiometries. With increasing F concentration, the coordination number of Au by F increases from four (in $AuF_3$) to six (in $AuF_4$ or $AuF_6$) and the square-planar configuration transforms to octahedral. Crystal field theory has been used to successfully describe the break down of degeneracy of $d$ electron orbital states⁴². The electrons in the Au $5d$ orbitals and those in the F atoms repel each other due to repulsion between like charges. Therefore, the Au $5d$ electrons closer to the F atoms have a higher energy than the others further away, which results in splitting of the energies of the Au $5d$ orbitals. In the square-planar $AuF_3$ structure, this results in four different energy levels (Fig. S5). On the other hand, every six F atoms that form an octahedron around an Au ion in the $AuF_4$ and $AuF_6$ structures, the most common type, split its $5d$ orbitals into $d_{xy}$, $d_{xz}$, $d_{yz}$, (lower energy) $d_{z^2}$, and $d_{x^2-y^2}$ (higher energy). Normally, the increase of oxidation state is helpful in amplifying the magnitude of the splitting energy difference between the high and low energy levels. The lengths of Au-F bonds in $AuF_6$ are a little smaller than those in the $AuF_3$ structure; therefore their electrons are closer and more repelled, usually resulting in larger difference of splitting energy levels. The total energy of the system may decrease through crystal field stabilization as well as from the enhanced crystal field splitting of $5d$ orbitals under pressure. As a result, the splitting of Au $5d$ orbitals may explain why 6-fold coordinated $AuF_4$ and $AuF_6$ can exist to some extent.

### C. Electronic properties and valence states of $AuF_n$

To probe the nature of the electronic properties and the chemical bonds in the meliorative $AuF_n$ structures, we calculated their projected density of state (DOS), ELF, and charge population. As is evident by the sizeable bandgaps, $AuF_3$ and $AuF_4$ are semiconducting, whereas $AuF_2$ is metallic judged from the large DOS at the Fermi level (Fig. 3a). This is consistent with the band structure of the $AuF_2$ phase, where three bands clearly cross and overlap at the Fermi level (Fig. S6). Although obtaining the precise bandgaps of these semiconductors is not the main focus in this study, we note that the computed bandgaps are likely to be underestimated since normal DFT calculations are adopted here. For example, the bandgap of the $Cmc2_1$ phase ($AuF_3$) is calculated to be larger when the screened hybrid functional of Heyd, Scuseria, and Ernzerhof (HSE06)⁴³ is employed (Fig. S7).

The states below or close to the Fermi level are principally associated with Au $5d$ and F $2p$ electrons, while the contributions from Au $6s$ and F $2s$ are quite small or even close to zero. This may indicate significant charge transfer from Au $6s$ and F $2s$ to Au $5d$ and F $2p$ orbitals. With increasing of F content, the F $2p$ contribution below the Fermi level increases remarkably, attributed to an increase in charge transfer from Au $5d$ into F $2p$ states with the increase of F concentration.

Our selected ELF of $\text{AuF}_3$ (Fig. 3b) can map the probability of finding electron pairs in different regions of the crystal structure. The largest ELF values are observed near the F atoms, corresponding to their core $2s$ electrons, but some electrons localize around the Au atoms. The ELF values between the Au and F atoms are significantly different, indicating its typical ionic characteristics.

Electrons tend to transfer from Au to F and thus Au naturally shows positive oxidation states in this system. In both $\text{AuF}_3$ and $\text{AuF}_2$, Au-F bonds show dominantly ionic bond character. The contrasting electronic properties of metallic $\text{AuF}_2$ can be understood intuitively in terms of the decreased concentration of nonmetallic F in these phases, which can enable redundant valence electrons at Au to become free. The charge transfer between Au and F atoms supports this assumption, which can be more clearly illustrated using a Bader population analysis$^{44}$. This method is calculated by partitioning the space into Bader basins around each atom based on the stationary points of charge density. The integration of charges in each basin can give the total charge of each atom. For easy comparison, we computed the Bader charge of each structure at 20 GPa. Even though $\text{AuF}$ and $\text{AuF}_5$ are thermodynamically unstable, we consider them here for comparison. The calculated Au Bader charges for $\text{AuF}_n$ (n=1-6) are $0.565e$, $1.066e$, $1.485e$, $1.741e$, $1.939e$ and $2.076e$, respectively, increasing monotonically from $\text{AuF}$ to $\text{AuF}_6$ (Fig. 3c). Usually, the calculated Bader charges are significantly smaller than the numbers of formal oxidation states even in the typical ionic compounds$^{18,45}$. For example, every F atom accepts 0.5-0.8$e$ from Cs in the Cs-F system. In contrast to the mixed-valence character found for $\text{AuO}$ ($\text{Au}^+\text{Au}^{3+}\text{O}_2$) (here, $\text{Au}^+$ and $\text{Au}^{3+}$ provide $0.47e$ and $1.12e$, respectively)$^{46}$, the Bader charges from the nonequivalent Au atoms in all our $\text{AuF}_n$ phases are very similar, which clearly indicates that Au shows a single valence state in each structure. Here, each F atom accepts ~0.35-0.57$e$ from Au and the number of

electrons which each Au atom donates to F decreases from a maximum in AuF₆ through
AuF₅.₂ to AuF, where the Au ions should adopt +6, +5, +4, +3, +2, and +1 valence states,
respectively.

Because the bonding between Au and F atoms in AuFₙ compounds is significant, we
have also examined these interactions by calculating the crystal orbital Hamilton populations
and the respective integrated crystal orbital Hamilton populations (ICOHPs). The ICOHP
counts the energy weighted population of wave functions between two atomic orbitals for a
pair of selected atoms; therefore, this value tends to scale with bond strength in compounds.
The value of the ICOHP between the Au–F pairs is quite large for AuF and become larger
with increasing F content, indicating that the Au–F bonds become stronger. The ICOHPs of
Au–Au and F–F shows rather low values (close to zero) in AuF₆. (Fig. S8)

## 4. Conclusions

In summary, we have carried out a systematic exploration of the ground state energies of
compounds in the binary Au-F system at elevated pressure. A pressure-induced phase
transition to a new layered structure is found for AuF₃ while compressed AuF₄ contains two
nonequivalent 3-dimensional AuF₆ units. We find that the compressed Au ions are 2- (AuF₂),
4- (AuF₃) and 6-fold coordinated (AuF₄ and AuF₆) by F for different concentrations of F. Our
studies significantly modify the reported ground-state structures of the Au-F system and
confirm the existence of new stable stoichiometries in this system at high pressure,
highlighting the existence of additional valence states (+4 and +6) for Au.

## Acknowledgments

The authors acknowledge funding support from the National Natural Science Foundation
of China under Grants No. 11604314 and 11604290, Funding Program for Recruited Oversea
Scholars of Hebei Province (CL201729) and PhD foundation by Yanshan University (Grant
B970). S.A.T.R is grateful for support from NERC (NE/P012167/1). X. F. acknowledges
China Scholarship Council (CSC) funding.

Figures and captions:

![](./images/812753700865966081_3.jpg)

Fig. 1: The crystal structures of ${\rm AuF_n}$: (a) the $P6_122$ phase (${\rm AuF_3}$) at 0 GPa, (b) the $Cmc2_1$ phase (${\rm AuF_3}$) at 10 GPa, (c) the $P2_1/c$ phase (${\rm AuF_2}$) at 0 GPa, (d) the $Pnma$ phase (${\rm AuF_2}$) at 20 GPa, (e) the $P2_1/m$ phase (AuF) at 10 GPa, (f) the $P2_1/c$ phase (AuF) at 10 GPa, (g) the $C2/c$ phase (${\rm AuF_4}$) at 20 GPa, (h) the $Pnma$ phase (${\rm AuF_5}$) at 0 GPa, (i) the $R$-$3$ phase (${\rm AuF_6}$) at 20 GPa, and (j) the $C2/c$ phase (${\rm AuF_7}$) at 20 GPa. The large gold and small blue spheres represent Au and F atoms, respectively. The lengths of Au-F bonds are indicated, in $\mathring{\text{A}}$.

![](./images/812753700865966081_4.jpg)

Fig. 2: Ground-state and static enthalpy of formation per atom of the ${\rm AuF}_n$ structures with respect to their end-member counterparts; the fluorine molar content (x = 0 corresponds to pure Au; x = 1 to pure F) for the ground state and $P=$ (a) 0, (b) 20 and (c) 40 GPa. The symbols on the solid lines indicate those compounds are stable at the corresponding pressures, while those on the dashed lines represent those unstable with respect to their decomposition into elements and other stable compounds. (d) The stable range of pressure for ${\rm AuF}_n$.

![](./images/812753700865966081_5.jpg)
![](./images/812753700865966081_6.jpg)

Fig. 3: (a) The projected DOS of the Pnma phase (AuF₂), the Cmc2₁ phase (AuF₃), the C2/c phase (AuF₄) and the P2₁/c phase (AuF₆) at 20 GPa. The Fermi level has been set to 0 eV. (b) The electron localized function of the Cmc2₁ phase (AuF₃) at (0 1 0) cutoff plane at 20 GPa. As implemented in VASP, ELF ranges from 0 (free electron gas) to 1 (localized electrons). (c) Calculated Bader charge of Au in AuFₙ at 20 GPa.

### References

1  G. J. Hutchings, M. Brust and H. Schmidbaur, Gold - an introductory perspective, *Chem. Soc. Rev.*, 2008, **37**, 1759.

2  P. Pyykko, Relativistic effects in structural chemistry, *Chem. Rev.*, 1988, **88**, 563–594.

3  H. Häkkinen, M. Moseler and U. Landman1, Bonding in Cu, Ag, and Au clusters: relativistic effects, trends, and surprises, *Phys. Rev. Lett.*, 2002, **89**, 033401.

4  J. Miro and C. Pozo, Fluorine and gold: a fruitful partnership, *Chem. Rev*, 2016, **116**, 11924–11966.

5  B. Žemva, K. Lutar, A. Jesih, W. J. Casteel, A. P. Wilkinson, D. E. Cox, R. B. Von Dreele, H. Borrmann and N. Bartlett, Silver trifluoride: preparation, crystal structure, some properties, and comparison with $AuF_3$, *J. Am. Chem. Soc*, 1991, **113**, 4192–4198.

6  B. F. W. B. Einstein, R. Rao, J. Trotter, N. Bartlett and B. Columbia, The crystal structure of gold trifluoride, *J. Chem. Soc. A Inorganic, Phys. Theor.*, 1967, 478–482.

7  A. Schulz and M. Hargittai, Structural variations and bonding in gold halides: a quantum chemical study of monomeric and dimeric gold monohalide and gold trihalide molecules, $AuX$, $Au_2X_2$, $AuX_3$, and $Au_2X_6$ (X = F, Cl, Br, I), *Chem. Eur. J.*, 2001, **7**, 3657–3670.

8  P. Schwerdtfeger, P. D. W. Boyd, S. Brienne and A. K. Burrell, Relativistic effects in gold chemistry. 4. gold (III) and gold (V) compounds, *Inorg. Chem.*, 1992, **31**, 3411.

9  S. Riedel and M. Kaupp, Has $AuF_7$ been made?, *Inorg. Chem.*, 2006, **45**, 1228–1234.

10 I. C. Hwang and K. Seppelt, Gold pentafluoride: structure and fluoride ion affinity, *Angew. Chemie - Int. Ed.*, 2001, **40**, 3690–3693.

11 J. Brunvoll, A. A. Ischenko, A. A. Ivanov, G. V. Romanov, V. B. Soklov, V. P. Spiridonov and T. G. Ssrand, Composition and molecular structure of gaseous gold pentafluoride by electron diffraction, *Acta Chem. Scand. A*, 1982, **36**, 705–709.

12 F. Mohr, The chemistry of gold-fluoro compounds: a continuing challenge for gold chemists, *Gold Bull.*, 2004, **37**, 164–169.

13 C. J. Evans and M. C. L. Gerry, Confirmation of the existence of gold (I) fluoride,

AuF: microwave spectrum and structure, *J. Am. Chem. Soc.*, 2000, **122**, 1560-1561.

14 X. Wang, L. Andrews, K. Willmann, F. Brosi and S. Riedel, Investigation of gold fluorides and noble gas complexes by matrix-isolation spectroscopy and quantum-chemical calculations, *Angew. Chemie - Int. Ed.*, 2012, **51**, 10628-10632.

15 X. Wang, L. Andrews, F. Brosi and S. Riedel, Matrix infrared spectroscopy and quantum-chemical calculations for the coinage-metal fluorides: comparisons of Ar-AuF, Ne-AuF, and molecules $MF_2$ and $MF_3$, *Chem. Eur. J.*, 2013, **19**, 1397-1409.

16 I. Hwang and K. Seppelt, The reduction of $AuF_3$ in super acidic solution, *Z. Anorg. Allg. Chem.*, 2002, **628**, 765-769.

17 S. H. Elder, G. M. Lucier, F. J. Hollander and N. Bartlett, Synthesis of Au (II) fluoro complexes and their structural and magnetic properties, *J. Am. Chem. Soc.*, 1997, **119**, 1020-1026.

18 M. Miao, Caesium in high oxidation states and as a p-block element, *Nat. Chem.*, 2013, **5**, 846-852.

19 J. Lin, Z. Zhao, C. Liu, J. Zhang, X. Du, G. Yang and Y. Ma, $IrF_8$ molecular crystal under high pressure, *J. Am. Chem. Soc.*, 2019, **141**, 5409-5414.

20 J. Botana, X. Wang, C. Hou, D. Yan, H. Lin, Y. Ma and M. S. Miao, Mercury under pressure acts as a transition metal: calculated from first principles, *Angew. Chemie - Int. Ed.*, 2015, **54**, 9280-9283.

21 D. Luo, J. Lv, F. Peng, Y. Wang, G. Yang, M. Rahm and Y. Ma, A hypervalent and cubically coordinated molecular phase of $IF_8$ predicted at high pressure, *Chem. Sci.*, 2019, **10**, 2543-2550.

22 Q. Zhu, D. Y. Jung, A. R. Oganov, C. W. Glass, C. Gatti and A. O. Lyakhov, Stability of xenon oxides at high pressures, *Nat. Chem.*, 2013, **5**, 61-5.

23 G. Yang, Y. Wang, F. Peng, A. Bergara and Y. Ma, Gold as a 6p-element in dense lithium aurides, *J. Am. Chem. Soc.*, 2016, **138**, 4046-4052.

24 J. Lin, S. Zhang, W. Guan, G. Yang and Y. Ma, Gold with +4 and +6 oxidation states in $AuF_4$ and $AuF_6$, *J. Am. Chem. Soc.*, 2018, **140**, 9545-9550.

25 Y. Wang, J. Lv, L. Zhu and Y. Ma, Crystal structure prediction via particle-swarm optimization, *Phys. Rev. B*, 2010, **82**, 094116.

26 Y. Wang, J. Lv, L. Zhu and Y. Ma, CALYPSO: a method for crystal structure prediction, *Comput. Phys. Commun.*, 2012, **183**, 2063-2070.

27 J. Lv, Y. Wang, L. Zhu and Y. Ma, Predicted novel high-pressure phases of lithium, *Phys. Rev. Lett.*, 2011, **106**, 015503.

28 G. Liu, S. Besedin, A. Irodova, H. Liu, G. Gao, M. Eremets, X. Wang and Y. Ma, Nb-H system at high pressures and temperatures, *Phys. Rev. B*, 2017, **95**, 104110.

29 M. Zhang, H. Liu, Q. Li, B. Gao, Y. Wang, H. Li, C. Chen and Y. Ma, Superhard BC₃ in cubic diamond structure, *Phys. Rev. Lett.*, 2015, **114**, 015502.

30 Y. Li, J. Hao, H. Liu, S. Lu and J. S. Tse, High-energy density and superhard nitrogen-rich B-N compounds, *Phys. Rev. Lett.*, 2015, **115**, 105502.

31 G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, *Phys. Rev. B*, 1996, **54**, 11169-11186.

32 J. P. Perdew, K. Burke and M. Ernzerhof, Generalized gradient approximation made simple, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

33 K. Peters, S. Wartanessian, A. F. Sax, K. E. Edgecombe, A. D. Becke, J. Flad, R. Nesper, H. Preuss, H. J. Werner, P. J. Knowles, H. Stoll, H. Preuss, J. A. Pople, S. Gordon, D. J. De Frees, J. A. Pople and F. X. Fraschio, Electron localization in solid-state structures of elements - diamond structure, *Angew. Chem. Int. Ed.*, 1992, **31**, 187-188.

34 A. D. Becke and K. E. Edgecombe, A simple measure of electron localization in atomic and molecular-systems, *J. Chem. Phys.*, 1990, **92**, 5397.

35 R. Dronskowski and P. E. Blöchl, Crystal orbital hamilton populations (COHP) - energy-resolved visualization of chemical bonding in solids based on density-functional calculations, *J. Phys. Chem.*, 1993, **97**, 8617-8624.

36 V. L. Deringer, A. L. Tchougréeff and R. Dronskowski, Crystal orbital Hamilton population (COHP) analysis as projected from plane-wave basis sets, *J. Phys. Chem. A*, 2011, **115**, 5461-5466.

37 S. Maintz, V. L. Deringer, A. L. Tchougréeff and R. Dronskowski, LOBSTER: a tool to extract chemical bonding from plane-wave based DFT, *J. Comput. Chem.*, 2016, **37**, 1030-1035.

38 K. Parlinski, Z. Q. Li and Y. Kawazoe, First-principles determination of the soft mode in cubic $ZrO_2$, *Phys. Rev. Lett.*, 1997, **78**, 4063–4066.

39 A. Togo, F. Oba and I. Tanaka, First-principles calculations of the ferroelastic transition between rutile-type and $CaCl_2$-type $SiO_2$ at high pressures, *Phys. Rev. B*, 2008, **78**, 134106.

40 M. Rahm, R. Hoffmann and N. W. Ashcroft, Ternary Gold hydrides: routes to stable and potentially superconducting compounds, *J. Am. Chem. Soc.*, 2017, **139**, 8740–8751.

41 D. Kurzydłowski and W. Grochala, Elusive AuF in the solid state as accessed via high pressure comproportionation, *Chem. Commun.*, 2008, **9**, 1073–10755.

42 J. H. Van Vleck, Theory of the variations in paramagnetic anisotropy among different salts of the iron group, *Phys. Rev.*, 1932, **41**, 208–215.

43 J. Heyd, G. E. Scuseria and M. Ernzerhof, Hybrid functionals based on a screened coulomb potential, *J. Chem. Phys.*, 2003, **118**, 8207–8215.

44 W. Tang, E. Sanville and G. Henkelman, A grid-based Bader analysis algorithm without lattice bias, *J. Phys. Condens. Matter*, 2009, **21**, 084204.

45 J. Botana and M. S. Miao, Pressure-stabilized lithium caesides with caesium anions beyond the -1 state, *Nat. Commun.*, 2014, **5**, 4861.

46 A. Hermann, M. Derzsi, W. Grochala and R. Ho, AuO: evolving from dis- to comproportionation and back again, *Inorg. Chem.*, 2016, **55**, 1278–1286.