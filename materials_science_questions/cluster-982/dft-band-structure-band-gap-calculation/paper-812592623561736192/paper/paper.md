Physical Chemistry Chemical Physics

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: K. Fan, Y. Ying, X. Luo and H. Huang, Phys. Chem. Chem. Phys., 2020, DOI: 10.1039/D0CP01133A.

![](./images/812592623561736192_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/812592623561736192_2.jpg)

rsc.li/pccp

# Monolayer $\text{PC}_5$/$\text{PC}_6$: Promising Anode Materials for Lithium-Ion Batteries

Ke Fan$^{a}$, Yiran Ying$^{a}$, Xin Luo$^{*b}$, and Haitao Huang$^{*a}$

$^{a}$Department of Applied Physics, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, P.R. China

$^{b}$School of Physics, Sun Yat-sen University, Guangzhou, Guangdong Province, P.R. China, 510275

## AUTHOR INFORMATION

### Corresponding Author

*E-mail: aphhuang@polyu.edu.hk (H.H.); luox77@mail.sysu.edu.cn (X.L.)

ABSTRACT.

Employing two-dimensional (2D) materials as anodes for lithium-ion batteries (LIBs) is believed to be an effective approach to meet the growing demands of high-capacity next-generation LIBs. In this work, the first-principles density functional theory (DFT) calculations are employed to evaluate the potential application of two-dimensional phosphorus carbide (2D $PC_x$, x=2, 5, and 6) monolayers as anode materials for lithium-ion batteries. The 2D $PC_x$ systems are predicted to show outstanding structural stability and electronic properties. From the nudged elastic band calculations, the single Li atom show extreme high diffusivities on the $PC_x$ monolayer with low energy barriers of 0.18 eV for $PC_2$, 0.47 eV for $PC_5$, and 0.44 eV for $PC_6$. We further demonstrate that the theoretical specific capacity of monolayer $PC_5$ and $PC_6$ can reach up to 1251.7 and 1235.9 mAh g⁻¹, respectively, several times that of graphite anode used in commercial LIBs. These results suggest that both $PC_5$ and $PC_6$ monolayer are promising anode materials for LIBs. Our work opens a new avenue to explore novel 2D materials in energy applications, where phosphorus carbides could be used as high-performance anode in LIBs.

### 1. Introduction

In recent years, battery systems have made a big contribution to the rapid development of the electronics market.¹,² Among all types of batteries, lithium-ion batteries (LIBs), as one of the greatest successes of clean energy storage technologies, have attracted widespread attention.³⁻⁶ Searching for suitable materials for LIBs electrodes, especially anodes, is a significant topic in modern battery technology. Conventional anode materials in LIBs have a bulk structure with low capacity and high diffusion barrier.⁷ Since the successful isolation of graphene from graphite,⁸⁻¹⁰ two-dimensional (2D) materials, such as hexagonal boron nitride,¹¹, ¹² phosphorene,¹³⁻¹⁵ transition metal dichalcogenides,¹⁶ and MXenes¹⁷⁻¹⁹ have been widely studied and identified as potential anode materials with enhanced electronic properties for LIBs. Despite these efforts, designing 2D anodes with higher capacity and lower diffusion barrier which can be commercialized is still a challenging job for researchers.

It is well-known that graphene and phosphorene are two important 2D materials that have potential applications in LIBs. Graphene shows excellent conductivity and stability, but six carbon atoms can only adsorb one Li ion to form a $LiC_6$ intercalation.²⁰ As a comparison, one Li atom can be intercalated with two phosphorus atoms in phosphorene, while the disadvantage of phosphorene is the limited stability in air or humid environment.²¹,²² Since both elemental carbon and phosphorus are reported to form stable 2D monolayers and have similar structures including three-fold coordinated atoms and a

hexagonal network, $^{23-25}$ it is reasonable to believe that compound phosphorus carbides can be stable as a monolayer and display properties that might even be superior to both constituents. Until now, several phosphorus carbide monolayers have been theoretically predicted to be stable, among which 2D PC has been fabricated successfully through doping C atoms into phosphorus ones. $^{25-31}$ Tan *et al.* have synthesized metallic black phosphorus carbide ($\beta$-PC) which has been verified to be stable at the DFT level, $^{26}$ and Zhang *et al.* has proposed to use the $\gamma$-PC in the LIBs. $^{28}$ However, the studies of 2D phosphorus carbide as a promising anode material for LIBs are still scarce due to limited 2D candidates and possible structural instability. Recently, Yu *et al.* have performed extensive structural search for $PC_x$ (x=2, 3, 5, and 6) monolayers, and they found that $PC_2$ (metal), $PC_3$ (semiconductor with a band gap of 2.15 eV), $PC_5$ (metal) and $PC_6$ (semiconductor with a band gap of 0.84 eV) are thermodynamically stable. $^{30}$ The predicted $PC_x$ structures except for wide-band-gap semiconductor $PC_3$, may have potential applications in anodes for LIBs, but theoretical or experimental evidence is lacking.

Inspired by the great potential of PC in LIBs discussed above, in this work, we systematically investigate the stability, electronic and Li storage properties of $PC_2$, $PC_5$ and $PC_6$ monolayers by means of density functional theory (DFT) calculations. Our calculations reveal that $PC_x$ (x=2, 5, and 6) systems show not only excellent thermal and dynamic stability but also high electron and ionic conductivities. The relatively high capacity of $PC_5$ (1251.7 mAh g⁻¹) and $PC_6$ (1235.9 mAh g⁻¹) suggesting that both candidates could be promising anode materials for LIBs.

## 2. Computational methods

Our calculations were performed in the framework of DFT calculations by the Vienna ab initio simulation package (VASP).³² The generalized gradient approximation (GGA) with the Perdew-Burke-Ernzerhof (PBE) flavor³³ was chosen as the exchange-correlation functional. Van der Waals interaction was considered by using the semiempirical DFT-D2³⁴ approach. For the calculation of band structures and density of states (DOS), a more accurate Heyd-Scuseria-Ernzerhof 06 (HSE06) hybrid functional³⁵ was applied. A plane-wave cut-off energy of 500 eV was employed, which can lead to sufficiently converged total energy values for 2D PCₓ (Fig. S1). To avoid the interlayer interaction, a vacuum layer of 15Å along the c-axis was added to the slabs. The Brillouin zone was sampled using a Monkhorst-Pack k-point mesh scheme, and the meshes of Γ-centered 13×13×1 and 6×6×1 were used for the unit cell and the 2×2×1 supercell, respectively. K-point mesh size convergence was also tested and confirmed (Fig. S2). During geometric relaxation, the convergence criteria for energy and force were set to be $10^{-5}$ eV and $0.01$ eV Å⁻¹, respectively, while for self-consistent field calculations, energy convergence criteria of $10^{-5}$ eV was also used. Conjugated gradient algorithm was applied for geometric relaxation. Charge differential analysis combined with the Bader charge method³⁶ was used to quantitatively estimate the charge redistribution and transfer. The climbing image nudged elastic band (CI-NEB) method³⁷ was applied to calculate the potential energy diffusion

pathway and the minimum diffusion energy barrier of lithium ions on the $PC_x$ monolayer (2×2×1 supercell).

Phonon dispersion spectra were calculated by Phonopy code³⁸. Density functional perturbation theory method was used to calculate force constants in real space. Local density approximation (LDA) was used as the exchange-correlation functional. During phonon dispersion spectra calculations, displacement of each ion was set as 0.01 Å, and energy convergence criteria was set as $10^{-8}$ eV. *Ab initio* molecular dynamics (AIMD)³⁹ simulations with Nosé-Hoover thermostat for NVT ensemble were performed at 300 K with the time step of 2 fs. The total simulation time for 3×3 supercell of $PC_x$ was set as 12 ps. Nosé mass corresponding to 80 fs (40 time steps) was chosen.

The adsorption energy of Li atoms on the $PC_x$ monolayer can be calculated with the following equation⁴⁰:

$$
E_{ad}=(E_{PC_xLi_n}-E_{PC_x}-n\mu_{Li})/n \tag{1}
$$

Here, $E_{PC_xLi_n}$ and $E_{PC_x}$ are the total energies of $PC_x$ with and without Li atom adsorption, respectively. $\mu_{Li}$ represents the energy per Li atom in body-centered cubic (bcc) structure (i.e. chemical potential), and $n$ corresponds to the number of Li atoms in the adsorption configurations.

The differential charge density as a function of space is obtained as the difference between the valence charge density before and after the bonding¹⁹:

$$
\Delta\rho(\vec{r})=\rho_{PC_xLi_n}(\vec{r})-\rho_{Li}(\vec{r})-\rho_{PC_x}(\vec{r}) \tag{2}
$$

where $\rho_{PC_xLi_n}(\vec{r})$, $\rho_{Li}(\vec{r})$, and $\rho_{PC_x}(\vec{r})$ represent the charge density distributions of Li-

intercalated $PC_x$ systems, Li atom, and bare $PC_x$ monolayer, respectively.

The charge/discharge processes can be described by the following half-cell reactions:³¹

$$PC_x +nLi^+ +ne^- \leftrightarrow PC_xLi_n \tag{3}$$

The open circuit voltage (OCV) at different coverage on the surfaces of the $PC_x$ is calculated as⁴¹⁻⁴³:

$$OCV \approx (E_{PC_x} +n\mu_{Li} - E_{PC_xLi_n})/n \tag{4}$$

The maximum capacity (Cₘ) can be obtained by the following equation⁴²,⁴⁴:

$$C_M \approx zy_{max}F/M_{PC_x} \tag{5}$$

where z, $y_{max}$, F, and $M_{PC_x}$ are the valence number, maximum adatom content (corresponding to chemical formula PCₓLiᵧ), Faraday constant (26.8 Ahmol⁻¹)⁴⁵, and relative molecular mass of $PC_x$, respectively. In the calculation of adsorption process, all the atoms were fully relaxed.

## 3. Results and discussion

### 3.1 Structures and stability

All three DFT-optimized structures of $PC_x$ (shown in Fig. 1 with all optimized lattice constants shown in Table S1) are quasi-planar, with P atoms located away from the basal plane. $PC_2$ with the space group of P-1 is constructed with 5-8-5 rings, similar to the case of popgraphene.⁴⁶ The 5-ring consists one P atom and four C atoms, while the 8-ring is

consisted of four P and four C atoms. Each atom (P and C) is coordinated with two C atoms and one P atom. The other two structures are stabilized into two types of hexagonal structure including $C_6$, $P_2C_4$ rings for $PC_5$ and $C_6$, $PC_5$ rings for $PC_6$ (space group P-3). For $PC_5$, two types of $P_2C_4$ rings (ortho-P and para-P) are aligned in $a$ direction and $C_6$ rings fill up the plane in a zigzag configuration, and each P atom is coordinated with one P atom and two C atoms, similar to the situation of $PC_2$. For $PC_6$, on the other hand, each $C_6$ ring is surrounded by six $PC_5$ rings, and each P is coordinated with three C atoms. The quasi-planar nature of $PC_x$ may provide abundant adsorption sites for practical battery applications.

![](./images/812592623561736192_3.jpg)

Fig. 1 Top and side views of 2D (a) $PC_2$, (b) $PC_5$, and (c) $PC_6$. The unit cells are indicated by black dashed lines.

The structural stability is a very important factor for practical application of 2D materials. Here, we calculate the phonon dispersion to check the phase stability. Taking $PC_5$ as an example, in Fig. 2b, the absence of imaginary phonon modes in the first

Brillouin zone indicates that $PC_5$ monolayer is dynamically stable. Furthermore, AIMD simulations are used to examine its thermal stability. No obvious structural reconstructions can be noticed as the total energy of the system oscillate around the equilibrium values at the room temperature after the equilibrium time (Fig. S3). Similarly, Fig. 2 and S3 shows dynamical and thermal stability of $PC_2$ and $PC_6$. In addition, mechanical stabilities of $PC_x$ are also confirmed because the calculated 2D elastic constants can satisfy the Born criteria (see Table S2 and the discussions below).

![](./images/812592623561736192_4.jpg)

Fig. 2 Phonon dispersion spectra of 2D (a) $PC_2$, (b) $PC_5$, and (c) $PC_6$, and electron localization function (ELF) maps of (d) $PC_2$, (e) $PC_5$, and (f) $PC_6$ along planes containing specified bonding atoms. P and C atoms are represented in orange and blue, respectively.

The calculated electron localization function (ELF)⁴⁷,⁴⁸ clearly describes the bonding behavior. Generally, ELF > 0.5 corresponds to a covalent bond or core electrons, whereas the ionic bond is represented by a smaller ELF value (<0.5). An ELF value of 0.5 is the metallic bond.⁴⁹,⁵⁰ For $PC_5$, as illustrated in Fig. 2e, the bonds between C-C, P-P and P-C atoms are covalent in nature. Each C atom bonds with the three nearest neighbors in a planar configuration implying that the C atoms are sp² hybridized. On the other hand, lone pair electron is shown near P atoms, together with the buckled configuration of $PC_5$, showing a sp³ hybridization of P atoms. This bonding configuration satisfying the chemical octet rule on both C and P sites enhances its structure stability. In $PC_2$ and $PC_6$ system (Fig. 2d and 2f), C-C, P-P and C-P bonds also show covalent bond character, with sp² hybridization of C atoms and sp³ hybridization of P atoms. The detailed information about ELF plane is shown in Fig. S4.

### 3.2 Electronic properties

The electronic structure of anode material strongly correlates with the battery cyclability and rate performance. Since PBE functional usually underestimates the exact band gap values, here, we use more sophisticated hybrid functional HSE06 to perform the electronic structure calculations. Fig. 3 shows the computed density of states (DOS) and electronic band structures. Both PC₂ and PC₅ monolayers show metallic character with a

band-crossing point along the $\Gamma$-Y direction (Fig. 3a and 3b) which reveal its intrinsic metallicity and high density of carriers, indicating good electronic conductivity. The major contribution to the DOS of the crossing bands comes from the C atoms with small contribution from the P atoms. The $PC_6$ monolayer is a direct-gap semiconductor with a band gap of 0.84 eV at the M point (Fig. 3c). Despite its semiconducting nature, $PC_6$ shows high carrier mobility above $10^5$ cm$^2$ V$^{-1}$ s$^{-1}$. $^{30}$ These features render $PC_x$ as promising candidates for LIBs anodes.

![](./images/812592623561736192_5.jpg)

Fig. 3 Electronic band structure (left) and PDOS (right) for 2D (a) $PC_2$, (b) $PC_5$ and (c) $PC_6$ calculated at the HSE06 level. Partial band structure contributed by P and C atoms are represented by orange and blue dots, respectively, and the sizes of the dots are proportional to the weight of the contribution. Fermi levels are set to be zero.

### 3.3 Investigation of 2D $PC_x$ as anode materials for LIBs

Aside from the stability and electronic structure, the diffusion energy barrier, specific capacity, and open-circuit voltage (OCV) are also the key performance parameters of an anode material for LIBs. To systematically study the adsorption properties, a 2×2×1 supercell is used to examine the adsorption sites for an isolated Li atom. Several possible high-symmetry adsorption sites are considered (Fig. S5). In $PC_2$ system, after full structural relaxation, only three inequivalent adsorption sites A1, A2 and A3 are identified. For Li on A1 site, the adsorption energy is -0.94 eV, while for A2 and A3 site, the values are -0.44 eV and -0.87 eV, indicating that A1 is the most favorable adsorption site (Fig. S5). The adsorption energies are -0.84 and -0.83 eV (Fig. S5) for the most favorable A1 sites of $PC_5$ and $PC_6$, respectively. The relatively large adsorption energies of Li atom on $PC_x$ systems ensure the strong adsorption of Li atoms on the anodes.

To visualize the effects of adatom adsorption on the charge distribution, we calculate the differential charge density. Fig. 4 clearly shows the charge transfer from the Li atom to the substrates. Further Bader charge analysis (Table S3) show that each Li transfer 0.89, 0.89, and 0.91 electron to C atoms in $PC_2$, $PC_5$, and $PC_6$, respectively, confirming that

the adsorption can be mainly attributed to the interaction between Li and C atom.

![](./images/812592623561736192_6.jpg)

Fig. 4 The differential charge density distribution (Left: side view, and Right: top view) of Li adsorption on (a) $PC_2$, (b) $PC_5$, and (c) $PC_6$. Pink and yellow colors indicate electron accumulation and depletion, respectively.

The charge-discharge rate, which depends on the mobility of the intercalating ions, is another significant character for assessing the capability of an electrode material for rechargeable batteries. Therefore, we simulate the motion of Li atom on the surface of $PC_x$ and investigate the diffusion barriers using the CI-NEB method. Based on the adsorption energy of Li atom on several high-symmetry sites (Fig. S5) in each system, color-filled contour plots are presented in Fig. 5 and S6. From the calculated contour plot of total energy (including adsorbed single Li atom) as a function of adsorption site position, the

energetically feasible diffusion paths between the nearest-neighboring lowest-energy adsorption sites ($A_1$ and $A_2$) are selected. For $PC_5$, two possible diffusion pathways are shown in Fig. 5. For Path 1 ($A_1$$\rightarrow$$B$$\rightarrow$$A_2$), the diffusion energy barrier is 0.47 eV with diffusion distance of 8.06 Å. For Path 2 ($A_1$$\rightarrow$$C$$\rightarrow$$A_2$), the barrier height is 0.57 eV. For $PC_2$ and $PC_6$, the diffusion energy barrier is 0.18 eV and 0.44 eV with diffusion distances of 4.54 Å and 9.04 Å, respectively (Fig. S6). We note that the diffusion barriers on $PC_x$ are comparable to that on typical 2D materials such as graphene (0.33 eV),$^{51, 52}$ 1T-MoS$_2$ (0.28 eV),$^{53, 54}$ and MoN$_2$ (0.78 eV).$^{42}$ The low barriers ensure that Li ions can migrate easily on the surface of our studied systems. Therefore, 2D $PC_x$ systems can be promising electrode materials with fast charge–discharge rate and good rate capability.

![](./images/812592623561736192_7.jpg)

Fig. 5 (a) Schematic illustration of two possible paths of Li diffusion on the $PC_5$ monolayer based on the color-filled contour plots of adsorption energy of single Li atom on the surface, (b) diffusion of single adatom over $PC_5$ monolayer through the more favorable pathway (Path 1), and (c) the corresponding diffusion barrier diagrams of Li-$PC_5$. Enlarged figures near the maximum energy along Path 1 are also shown. The Li, P, and C atoms are distinguished by green, orange, and blue color, respectively.

For practical applications, the storage capacity of batteries is the key indicator for the performance of the electrode materials and the current focus for improvement. To explore

the maximum storage capacity for Li atoms, we consider the adsorption with an increasing number of adsorbed Li atoms on both sides of the $PC_x$ monolayers in the 2×2 supercell.

To obtain more accurate results, both the atomic positions and lattice constants are fully relaxed for the configurations after the intercalation. The Li atoms are inserted into $PC_x$ systems gradually and randomly until the monolayer reached to its final capacity point. For $PC_2$ monolayer, two Li atoms can be adsorbed in a single cell at most. Otherwise, the structure will collapse (Fig. S7). Thus, the structural deformation may be caused by the intercalation and deintercalation of Li ions in anodes. Therefore, limiting the deformation which is induced by the Li atoms adsorption is necessary. Here, we conduct a series of AIMD simulations to monitor the structural stability of the Li-intercalated $PC_5$ and $PC_6$ nanosheets. Structures with different numbers of adsorbed Li atoms are tested by the simulations to identify the maximum number which does not lead to noticeable deformation of $PC_x$ structures at ambient condition. The AIMD results shown in Fig. 6 present the structures with maximum Li atoms for $PC_5$ and $PC_6$ and all the original bonds are kept completely intact. To be specific, the maximum adatom number is 4.25 per $PC_5$, i.e. $P_8C_{40}Li_{34}$, over which the structure will collapse (Fig. S8). For, $PC_6$, on the other hand, the maximum adatom number is 4.75 (corresponding to chemical formula $P_8C_{48}Li_{38}$), which is judged by the large distance between new adatom and substrate, so that the chemical interactions are too weak to be considered (Fig. S9)$^{19, 55}$. Thus, the intercalation of the Li atoms leads to outstanding capacity of 1251.7 and 1235.9 mAh g⁻¹ for $PC_5$ and $PC_6$, respectively. The remarkable storage capacities of the phosphorus carbides can be

explained by the quasi-planar structures with abundant adsorption sites and relatively small atomic mass of P and C. Compared with carbon-based materials like graphite, introducing P can remarkably increase the theoretical capacity because one Li atom can coordinate with two P atoms, and phosphorus can help form puckered structures.

The calculated OCV as a function of the adatom content y on the $PC_2$, $PC_5$, and $PC_6$ supercell is plotted in Fig. S10. We can see that the curves for all systems show similar overall trend where the OCV decreases as the number of Li atom y increases at low Li coverage, then converges to a saturated value at higher Li coverage. It is noteworthy that OCV of $PC_5$ shows a slight increase when the adatom content y ranges from 1 to 2. This is similar to the case of $Ti_3C_2Li_x$, whose OCV increases when x ranges from 0.46 to $0.92.^{17}$ This phenomenon can be attributed to the fact that the exact OCV values depend on the sequence of adding Li adatoms on adsorption sites with different adsorption energies. Thus, when discussing OCV, we only focus on the overall trend instead of OCV value on specific points.

![](./images/812592623561736192_8.jpg)

Fig. 6 Optimized structures before and after AIMD simulations (2 ps, 300 K) of Li-intercalated PC₅ and PC₆ (2×2 supercell) with maximum numbers of adsorbed Li atoms without deformation, including top and side view of P₈C₄₀Li₃₄ (a) before and (b) after AIMD simulation, and top and side view of P₈C₄₈Li₃₈ (c) before and (d) after AIMD simulation. The Li, P, and C atoms are distinguished by green, orange, and blue color, respectively.

## 4. Conclusion

In summary, we explore the potential applications of 2D $PC_x$ (x=2, 5, 6) monolayers as the anode materials for Li-ion batteries by means of DFT calculations and *ab initio* molecular dynamics simulations. The most energetically favorable diffusion pathways for Li atom in PC₂, PC₅ and PC₆ are identified with considerably low diffusion barriers of 0.18 eV, 0.47 eV and 0.44 eV, respectively, which in turn allows fast charge–discharge rates when they are used as anodes. In addition, PC₅ and PC₆ monolayer also exhibit high

theoretical capacity values of 1251.7 mAh g⁻¹ and 1235.9 mAh g⁻¹, respectively, which are nearly three times that of graphite. These excellent properties suggest that the dynamically stable PC₅ and PC₆ monolayers could be promising anode materials. Our results give insightful prospects for further experimental work to explore carbon rich PCₓ monolayers as promising electrode material for Li ion batteries.

AUTHOR INFORMATION

Notes

The authors declare no competing financial interests.

ACKNOWLEDGMENT

This work was supported by the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No. PolyU152208/18E), the Hong Kong Polytechnic University (Project Nos. RHA3), and Science and Technology Program of Guangdong Province of China (Project No. 2019A050510012). X. L. thanks support from NSFC (No. 11804286) and the fundamental Research Funds for the central Universities.

REFERENCES

1.     H. Chen, T. N. Cong, W. Yang, C. Tan, Y. Li and Y. Ding, *Prog. Nat. Sci.*, 2009, **19**, 291-312.
2.     G. Ren, G. Ma and N. Cong, *Renewable Sustainable Energy Reviews*, 2015, **41**, 225-236.
3.     L. Lu, X. Han, J. Li, J. Hua and M. Ouyang, *J. Power Sources*, 2013, **226**, 272-288.

4.  G. Pistoia, *Lithium-ion batteries*, Newnes, advances and applications, 2013.

5.  Z. Li, J. Huang, B. Y. Liaw, V. Metzler and J. Zhang, *J. Power Sources*, 2014, **254**, 168-182.

6.  N. Nitta, F. Wu, J. T. Lee and G. Yushin, *Materials today*, 2015, **18**, 252-264.

7.  Y. Zhong, M. Yang, X. Zhou and Z. Zhou, *Materials Horizons*, 2015, **2**, 553-566.

8.  A. Kuzmenko, E. Van Heumen, F. Carbone and D. Van Der Marel, *Phys. Rev. Lett.*, 2008, **100**, 117401.

9.  A. Luican, G. Li and E. Y. Andrei, *Solid State Commun.*, 2009, **149**, 1151-1156.

10. A. K. Geim and K. S. Novoselov, in *Nanoscience and Technology: A Collection of Reviews from Nature Journals*, World Scientific, 2010, pp. 11-19.

11. H. Li, R. Y. Tay, S. H. Tsang, W. Liu and E. H. T. Teo, *Electrochim. Acta*, 2015, **166**, 197-205.

12. M. T. F. Rodrigues, K. Kalaga, H. Gullapalli, G. Babu, A. L. M. Reddy and P. M. Ajayan, *Advanced Energy Materials*, 2016, **6**, 1600218.

13. S. Zhao, W. Kang and J. Xue, *J. Mater. Chem. A*, 2014, **2**, 19046-19052.

14. W. Li, Y. Yang, G. Zhang and Y.-W. Zhang, *Nano Lett.*, 2015, **15**, 1691-1697.

15. G.-C. Guo, D. Wang, X.-L. Wei, Q. Zhang, H. Liu, W.-M. Lau and L.-M. Liu, *J. Phys. Chem. Lett.*, 2015, **6**, 5002-5008.

16. Y. Jing, Z. Zhou, C. R. Cabrera and Z. Chen, *J. Phys. Chem. C*, 2013, **117**, 25409-25413.

17. D. Er, J. Li, M. Naguib, Y. Gogotsi and V. B. Shenoy, *ACS Appl. Mater. Interfaces*, 2014, **6**, 11173-11179.

18. J. Hu, B. Xu, C. Ouyang, S. A. Yang and Y. Yao, *J. Phys. Chem. C*, 2014, **118**, 24274-24281.

19. K. Fan, Y. Ying, X. Li, X. Luo and H. Huang, *J. Phys. Chem. C*, 2019, **123**, 18207-18214.

20. V. Zinth, C. von Lüders, M. Hofmann, J. Hattendorff, I. Buchberger, S. Erhard, J. Rebelo-Kornmeier, A. Jossen and R. Gilles, *J. Power Sources*, 2014, **271**, 152-159.

21. B. Sa, Y.-L. Li, J. Qi, R. Ahuja and Z. Sun, *J. Phys. Chem. C*, 2014, **118**, 26560-26568.

22. J. Dai and X. C. Zeng, *J. Phys. Chem. Lett.*, 2014, **5**, 1289-1293.

23. G. Seifert and E. Hernandez, *Chem. Phys. Lett.*, 2000, **318**, 355-360.

24. B. Zhang and D. S. Su, *Small*, 2014, **10**, 222-229.

25. G. Wang, R. Pandey and S. P. Karna, *Nanoscale*, 2016, **8**, 8819-8825.

26. W. C. Tan, Y. Cai, R. J. Ng, L. Huang, X. Feng, G. Zhang, Y.-W. Zhang, C. A. Nijhuis, X. Liu and K.-W. Ang, *Adv. Mater.*, 2017, **29**, 1700503.

27. W. C. Tan, L. Huang, R. J. Ng, L. Wang, D. M. N. Hasan, T. J. Duffin, K. S. Kumar, C. A. Nijhuis, C. Lee and K. W. Ang, *Adv. Mater.*, 2018, **30**, 1700503.

28. W. Zhang, J. Yin, P. Zhang, X. Tang and Y. Ding, *J. Mater. Chem. A*, 2018, **6**, 12029-12037.

29. D. Singh, S. Kansara, S. K. Gupta and Y. Sonvane, *J. Mater. Sci.*, 2018, **53**, 8314-8327.

30. T. Yu, Z. Zhao, Y. Sun, A. Bergara, J. Lin, S. Zhang, H. Xu, L. Zhang, G. Yang and Y. Liu, *J. Am. Chem. Soc.*, 2019, **141**, 1599-1605.

31. K. Dou, Y. Ma, T. Zhang, B. Huang and Y. Dai, *Phys. Chem. Chem. Phys.*, 2019.

32. G. Kresse and J. Furthmüller, *Phys. Rev. B*, 1996, **54**, 11169.

33. J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.* , 1996, **77**, 3865.

34. S. Grimme, *J. Comput. Chem.*, 2006, **27**, 1787-1799.

35. A. V. Krukau, O. A. Vydrov, A. F. Izmaylov and G. E. Scuseria, *J. Chem. Phys.*, 2006, **125**, 224106.

36. W. Tang, E. Sanville and G. Henkelman, *J. Phys.: Condens. Matter*, 2009, **21**, 084204.

37. G. Henkelman, B. P. Uberuaga and H. Jónsson, *J. Chem. Phys.*, 2000, **113**, 9901-9904.

38. A. Togo and I. Tanaka, *Scr. Mater.*, 2015, **108**, 1-5.

39. S. Nosé, *J. Chem. Phys.*, 1984, **81**, 511-519.

40. F. T. Hesselink, *J. Colloid Interf. Sci.*, 1977, **60**, 448-466.

41. E. Yang, H. Ji and Y. Jung, *J. Phys. Chem. C*, 2015, **119**, 26374-26380.

42. X. Zhang, Z. Yu, S.-S. Wang, S. Guan, H. Y. Yang, Y. Yao and S. A. Yang, *J. Mater. Chem. A*, 2016, **4**, 15224-15231.

43. X. Li, Q. Wang and P. Jena, *J. Phys. Chem. Lett.*, 2017, **8**, 3234-3241.

44. X. Zhang, J. Hu, Y. Cheng, H. Y. Yang, Y. Yao and S. A. Yang, *Nanoscale*, 2016, **8**, 15340-15347.

45. Y. Xie, Y. Dall'Agnese, M. Naguib, Y. Gogotsi, M. W. Barsoum, H. L. Zhuang and P. R. C. Kent, *J. Am. Chem. Soc.*, 2014, **8**, 9606-9615.

46. S. Wang, B. Yang, H. Chen and E. Ruckenstein, *J. Mater. Chem. A*, 2018, **6**, 6815-6821.

47. A. Savin, R. Nesper, S. Wengert and T. F. Fässler, *Angewandte Chemie International Edition in English*, 1997, **36**, 1808-1832.

48. S. Noury, X. Krokidis, F. Fuster and B. Silvi, *Computers chemistry*, 1999, **23**, 597-604.

49. J. K. Burdett and T. A. McCormick, *J. Phys. Chem. A*, 1998, **102**, 6366-6372.

50. V. Tsirelson and A. Stash, *Chem. Phys. Lett.*, 2002, **351**, 142-148.

51. E. Lee and K. A. Persson, *Nano Lett.*, 2012, **12**, 4624-4628.

52. Q. Meng, A. Hu, C. Zhi and J. Fan, *Phys. Chem. Chem. Phys.*, 2017, **19**, 29106-29113.

53. T. Yu, Z. Zhao, L. Liu, S. Zhang, H. Xu and G. Yang, *J. Am. Chem. Soc.*, 2018, **140**, 5962-5968.

54. C.-S. Liu, X.-L. Yang, J. Liu and X.-J. Ye, *ACS Applied Energy Materials*, 2018, **1**, 3850-3859.

55. Q. Meng, J. Ma, Y. Zhang, Z. Li, C. Zhi, A. Hu and J. Fan, *Nanoscale*, 2018, **10**, 3385-3392.