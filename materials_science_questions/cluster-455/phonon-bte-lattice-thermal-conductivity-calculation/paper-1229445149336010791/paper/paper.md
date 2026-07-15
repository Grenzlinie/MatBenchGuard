# Physical origin of enhanced electrical conduction in aluminum-graphene composites

K. Nepal, $^{1,a)}$ C. Ugwumadu, $^{1}$ K.N. Subedi, $^{2}$ K. Kappagantula, $^{3}$ and D. A. Drabold $^{1,b)}$

$^{1)}$Department of Physics and Astronomy, Nanoscale and Quantum Phenomena Institute (NQPI), Ohio University, Athens, Ohio 45701, USA
$^{2)}$Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA
$^{3)}$Pacific Northwest National Laboratory, Richland, Washington, 99352, USA

(Dated: 5 January 2024)

The electronic and transport properties of aluminum-graphene composite materials were investigated using *ab initio* plane wave density functional theory. The interfacial structure is reported for several configurations. In some cases, the face-centered aluminum (111) surface relaxes in a nearly ideal registry with graphene, resulting in a remarkably continuous interface structure. The Kubo-Greenwood formula and space-projected conductivity were employed to study electronic conduction in aluminum single- and double-layer graphene-aluminum composite models. The electronic density of states at the Fermi level is enhanced by the graphene for certain aluminum-graphene interfaces, thus, improving electronic conductivity. In double-layer graphene composites, conductivity varies non-monotonically with temperature, showing an increase between 300-400 K at short aluminum-graphene distances, unlike the consistent decrease in single-layer composites.

Recent experimental research has shown that composites formed by the inclusion of single layer or multiple layers of graphene into aluminum (Al) and copper (Cu) improve the electronic conduction properties of bulk metal. The interfacial structure of the metal-graphene composites is generally believed to form a high-energy configuration under suitable compression for specific experimental designs, such as hot-extrusion$^{1,2}$ or friction-extrusion$^{3}$ methods. This discovery holds promise for long-distance power transmission, and other applications$^{4-6}$.

Several works have provided insight into the mechanisms of enhanced conduction in Al-graphene (Al-G) and Cu-graphene (Cu-G) composites$^{7-13}$. For example, Cao and co-workers showed that the electron concentration in both Al and carbon (C) atoms is contingent upon the orientation of the Al-G interface$^{14}$. Wang and co-workers demonstrated that the incorporation of graphene additives induces a shift in the Fermi level of copper from *ab initio* calculations$^{15}$. These studies suggest that the presence of graphene in aluminum and copper results in the alignment of metal grains in specific orientations and/or facilitates direct carrier transfer between graphene and metals. However, the precise mechanism by which this transport occurs and the impact of graphene on the global conductivity of these composites is still not well understood.

In a previous Letter in this journal$^{16}$, we discussed electronic transport in copper-graphene composites by considering a single graphene layer sandwiched between two Cu (111) surfaces. We noted the enhancement of the electronic density of states near the Fermi level at short copper-graphene distances - suggesting improved electronic conductivity for the composites. This complementary study extends the analysis to aluminum-graphene composites formed with single and double-layer graphene. We offer atomistic insights into structural relaxation at the aluminum-graphene interface and explore the temperature-dependent conductivity with the number of graphene layers in the composites. In what follows, models of Aluminum - single-layer graphene - Aluminum composites are referred to as SL, and Aluminum - double-layer graphene - Aluminum composite is referred to as DL. We focus the discussion on the DL models except where the contrast to SL is informative.

To create the Al-G composite models, we started with an orthorhombic cell of face-centered Al (111) that includes a stacking fault, as shown in Figure 1 (a). Al (111) terminations are known for their low surface energy and high electronic conductivity$^{17,18}$. Single and double ("AB" stacking) graphene sheets were positioned above the aluminum fault layer to form an interface. The side view of the arrangement of the atoms in the SL and DL models is shown in Figures 1 (b) and 1 (c), respectively. To represent the thermophysical phenomena typically observed in solid-phase processed Al-G composites, we simulated the "compression" of the composites by reducing the Al-G distance. A similar method was employed in earlier work to study the pressure dependence of conductivity on mono-crystal Copper, as well as Copper - single-layer Graphene - Copper composite$^{16,19}$. Next, employing the conjugate gradient algorithm within the Vienna *ab initio* simulation package (VASP)$^{20}$, an energy-optimized interface structure of the composite was attained for several constant volume simulations. The compression and relaxation procedures employed in this paper hope to mimic conditions commonly observed in aluminum composites that exhibit improved electrical conductivity through solid-phase processing methods. Details regarding the VASP simulation protocol and the method to create the compressed composite models are provided in Sections S1 and S2 of the supplementary material.

Visual inspection of the composite models before any compression and structural optimization, as shown in Figure 1 (d), shows the misalignment between Al and C atoms as a honey-

$^{a)}$Electronic mail: kn478619@ohio.edu
$^{b)}$Electronic mail: drabold@ohio.edu

![](./images/1229445149336010791_1.jpg)

FIG. 1. (a) ABCABC... planar stacking in the Al (111) face-centered structure with a fault layer, shown by blue atoms. Representative structure of interface models with (b) single-layer and (c) double-layer graphene, where $d_{Al-G}$ is the distance between the aluminum surface and the graphene layer. (d) Top view of the arrangement of carbon atoms in the graphene layer with Al (111) for a weakly interacting Al-graphene system with the interfacial distance of 3.48 Å (before relaxation). (e) Interface structure in composite models after the relaxation of DL composites with [i] $d_{Al-G}=3.41$ and [ii] 2.97 Å. For $d_{Al-G}=2.97$ Å, the optimized interface structure forms a strain-free registry between Al and C. All cyan (brown) spheres represent Al (C) atoms.

<table>
<caption>Table 1: Fermi level as a function of Al-G composites for varying aluminum-graphene interfacial distance. The first and second row corresponds to DL and SL composites respectvely.</caption>
<tbody>
<tr>
<td>$d_{Al-G}$ [Å]</td>
<td>3.41</td>
<td>3.35</td>
<td>3.31</td>
<td>3.24</td>
<td>3.19</td>
<td>3.11</td>
<td>3.07</td>
<td>2.97</td>
<td>2.94</td>
</tr>
<tr>
<td>$E_{f}$ [eV]</td>
<td>6.70</td>
<td>6.79</td>
<td>6.93</td>
<td>7.05</td>
<td>7.20</td>
<td>7.29</td>
<td>7.36</td>
<td>7.52</td>
<td>7.63</td>
</tr>
<tr>
<td>$d_{Al-G}$ [Å]</td>
<td>3.40</td>
<td>3.35</td>
<td>3.31</td>
<td>3.25</td>
<td>3.13</td>
<td>3.01</td>
<td>2.90</td>
<td>2.71</td>
<td>
</td>
</tr>
<tr>
<td>$E_{f}$ [eV]</td>
<td>6.78</td>
<td>7.07</td>
<td>7.34</td>
<td>7.62</td>
<td>7.87</td>
<td>8.18</td>
<td>8.43</td>
<td>8.67</td>
<td>
</td>
</tr>
</tbody>
</table>

comb lattice of graphene (lattice constant of 2.46 Å) has a lattice mismatch of $\approx 5\%$ with the face-centered Al (111) surface nearest-neighbor distance of 2.34 Å. However, after compression of the models followed by structural optimization (via energy minimization), there appears to be an alignment between the Al and C atoms. Figure 1 (e) ([i] and [ii]), corresponding to models with $d_{Al-G}=3.41$ Å and 2.97 Å respectively, shows that the extent of atomic alignments between C and Al is dependent on the extent of the compression. The self-organized interface configuration for the compressed model ($d_{Al-G}=2.97$ Å in this work) is one of the low energy Al-G interface structure, so-called strain-free registry$^{21-23}$.

We computed the atom-projected electronic density of states (PDoS) for varying interfacial distance models. The PDoS for the SL and DL composite models are shown in Figure 2 (a) and 2 (b), respectively. The focus is on the region near the Fermi energy ($\varepsilon_{f}$), indicated by the gray dashed lines and shifted to zero. As the distance between aluminum and graphene (Al-G distance) decreased, we observed an enhancement of the electronic density of states near the Fermi level from both carbon (TOP) and aluminum (BOTTOM) atoms. With a random phase approximation$^{25-28}$, Mott and Davis showed that the electronic conductivity is proportional to $N^{2}(\varepsilon_{f})^{29}$, $N(\varepsilon_{f})$ being the density of states at the Fermi energy ($\varepsilon_{f}$). To explore this further, we plotted the behavior of $N^{2}(\varepsilon_{f})$ for the compressed composite models (brown curve in Figure 3 (a)). Indeed, $N^{2}(\varepsilon_{f})$ roughly tracks the electronic conductivity ($\sigma$) calculated using the Kubo-Greenwood formula (KGF)$^{30-32}$, shown by gray curve in Figure 3 (a). As the Al-G distance decreases, both $N^{2}(\varepsilon_{f})$ and electronic con-

![](./images/1229445149336010791_2.jpg)

FIG. 2. Projected electron density of states (PDoS) on carbon and aluminum atoms for (a) SL and (b) DL composites. The Fermi level is shifted to zero and is shown by the gray vertical dashed line in each subplot.

![](./images/1229445149336010791_3.jpg)

FIG. 3. (a) Conductivity for the DL model for various Al-G distances ($d_{Al-G}$) in the x-axis). The average conductivity ($\sigma$) is represented by the gray curve, with $\sigma_0$ denoting the conductivity of the Al-matrix shown in Figure 1 (a) calculated at 300K. The squared density of states at the Fermi level is shown in brown. In the inset, a Bader analysis$^{24}$ illustrates the average charge gain and loss for C (blue) and Al (green) atoms. (b) Estimated energy ($\Phi$) required to remove an electron from pure Al surface and with graphene layer placed on it at different interfacial distances. Dotted lines are included in all plots as visual aids.

ductivity increase, consistent with the elementary notion that metallicity/conduction are associated with a large $N(\varepsilon_f)$. The most compressed DL composite ($d_{Al-G}=2.97$ Å) exhibits approximately 40% higher conductivity relative to the aluminum matrix at 300 K. Analogous results for the SL models can be found in Figure S1 in the supplementary material.

The Fermi level shifts towards higher energies with decreasing Al-G distance, allowing more electronic states to participate in conduction (see details in Table I). This behavior has been reported for graphene on copper$^{15,16}$. We further predicted the work function of the composites for varying Al-G distances which is shown in Figure 3 (b). The plot shows that the work function decreases with decreasing Al-G distance, and hints at increasing charge transfer between interfacial graphene and aluminum atoms. These effects are quantified by estimating the average charge transfer from interfacial Al to C atoms, shown in the inset of Figure 3 (a). At the shortest interfacial distance ($d_{Al-G}=2.97$ Å), the average transfer of electronic charge to graphene reached 0.075 electrons per atom.

Next, we computed the conduction path in real space and its Al-G distance dependence. To achieve this, we employed the space-projected conductivity (SPC) method to project the electronic conductivity onto real-space grids$^{33-35}$. The upper panel of Figure 4 shows the isosurface plots of the transverse SPC values for DL composite models with interfacial distances of 3.41 Å and 2.97 Å, represented by (a) and (b) in Figure 4, respectively. The color bar on the right indicates the magnitude of SPC values, with red (blue) indicating low (high) values. At short Al-G distances, both aluminum and graphene contribute to conduction, particularly at the Al-G interface. The SPC at short Al-G distances reveals that graphene actively participates in conduction and forms a bridge between Al atoms on opposite layers. Notably, Figure 4 (upper panel) illustrates the formation of a continuous network of graphene sheets within the aluminum matrix, establishing a pathway for electron transport.

![](./images/1229445149336010791_4.jpg)

FIG. 4. [TOP] Projected 2D transverse SPC [in Siemens/cm/Å$^3$] iso-surface plot. [BOTTOM] Band decomposed charge density [in $e^-$/Å$^3$] corresponds to 15 bands below and above the Fermi level. The charge density values were scaled by a factor of 100. The data presented is for DL models with $d_{Al-G}=$ (a) 3.41 Å, (b) 2.97 Å. The pink (brown) spheres represent the Al (C) atoms in the models.

To further delineate the enhanced electron transport through the Al-G interface, we computed the electronic charge density near the Fermi level (see implementation examples in References³⁶⁻³⁹). By decomposing 15 bands above and below the Fermi level from the total electron charge density, we generated isosurface plots, shown in the lower panel of Figure 4. The same models used for the SPC calculation were employed. In the model with $d_{Al-G}=2.97$ Å, a higher degree of interaction between graphene and interfacial aluminum atoms was observed, indicated by the presence of black and red regions in the isosurface plot.

Next, we investigated the temperature dependence of conductivity in the composite models. This was done by estimating the average electrical conductivity from KGF for models held at different temperatures. The procedure to calculate the temperature-dependent conductivity is discussed in Section S3 of the supplementary material. Figure 5 presents the average electronic conductivity, obtained from 10 uncorrelated snapshots, as a function of temperature, ranging from 100 K to 600 K. Figure 5 (a) shows the conductivity behavior for the DL models corresponding to two interfacial distances. The model with $d_{Al-G}=3.41$ Å exhibits a nearly linear relationship, shown by blue plots. However, the model with short Al-G distance, $d_{Al-G}=2.97$ Å (shown by red plots), displays local extrema at around 300 K (minima) and 400 K (maxima). This non-monotonic behavior is in accord with experimental observations of conductivity enhancement in solid-phase processed metal-graphene composites¹,³, suggesting that this work captures, to some extent, the physics of the real material. In contrast, the extrema are not observed in the SL composite models, as shown in Figure 5 (b) and 5 (c) which correspond to Al-G distances $d_{Al-G}=3.01$ Å and 3.40 Å respectively. The non-monotonic temperature dependence observed exclusively in the compressed DL composites can be attributed to two factors: (1) The active involvement of graphene layers in charge transfer at shorter Al-G distances and (2) thermally driven hopping across the inter-layer galleries between the compressed graphene double-layer⁴⁰⁻⁴³.

![](./images/1229445149336010791_5.jpg)

FIG. 5. (a) Average electronic conductivity plotted versus annealing temperature for DL composite models with Al-G distances of 2.97 Å (red) and 3.41 Å (blue). (b) and (c) Similar plots for SL composite models, with Al-G distances of 3.01 Å and 3.40 Å, respectively. Vertical bars represent the standard deviation from the mean conductivity, averaged from the last 10 snapshots taken at 50 fs intervals over 3 ps annealing. Horizontal bars represent temperature fluctuations during constant temperature annealing.

We show that graphene and graphene stacks enhance the electronic conductivity of Al and while a key addition to the area, it is not the full story. The graphene structures are dispersed in an unknown way throughout the metal microstructures in the experimentally synthesized bulk composites and conspire to create a globally enhanced conductivity and globally modified temperature dependence. These effects could be due to (1) reduced scattering at grain boundaries from the graphene or (2) forming a network of isolated or weakly interacting Al-G structures. Our work complements both of these imaginings. The registry between the $sp^2$ carbon network (see Figure 1e [ii]) and the Al (111) surface suggests that mechanism (1) may be a key player in conductivity enhancement, as we demonstrate that a self-organized grain boundary buffer may form at Al (111) surfaces.

In conclusion, this study provides a comprehensive atomic-level understanding of the role of graphene as an additive in aluminum grains, focusing on single- and double-graphene stack(s) in the aluminum matrix. We have demonstrated that the increased electrical conductivity observed in Al-graphene composites arises from the enhanced electronic dynamics at the Fermi level. The interaction between carbon and interfacial aluminum atoms highlights the active role of graphene in facilitating electronic conduction. Furthermore, our study depicts the experimentally observed enhanced electrical conductivity within the temperature range of 300 K to 400 K.

## ACKNOWLEDGMENTS

The authors gratefully acknowledge the support received from the National Science Foundation (NSF) for computational resources through XSEDE (Grant No. ACI-1548562; allocation no. DMR-190008P) and ACCESS (Grant No. 2138259, 2138286, and 2138296; allocation no. phy230007p). The authors also acknowledge the support received from the Department of Energy (DOE) Vehicles Technology Office Powertrain Materials Core Program. Pacific Northwest National Laboratory is operated by the Battelle Memorial Institute for the U.S. Department of Energy under contract No. DE-AC06-76LO1830.

¹A. Nittala, J. Smith, B. Gwalani, J. Silverstein, F. Kraft, and K. Kappagantula, “Simultaneously improved electrical and mechanical performance of hot-extruded bulk scale aluminum-graphene wires,” *Materials Science and Engineering: B* 293, 116452 (2023).

$^{2}$K. S. Kappagantula, J. A. Smith, A. K. Nittala, and F. F. Kraft, "Macro copper-graphene composites with enhanced electrical conductivity," Jour- nal of Alloys and Compounds 894, 162477 (2022).

$^{3}$B. Gwalani, X. Li, A. Nittala, W. Choi, M. Reza-E-Rabby, J. Atehortua, A. Bhattacharjee, M. Pole, J. Silverstein, M. Song, and K. Kappagan- tula, "Unprecedented electrical performance of friction-extruded copper- graphene composites," Materials and Design 237, 112555 (2023).

$^{4}$A. K. Sharma, R. Bhandari, and C. Pinca-Bretotean, "A systematic overview on fabrication aspects and methods of aluminum metal matrix composites," Materials Today: Proceedings 45, 4133-4138 (2021), 8th In- ternational Conference on Advanced Materials and Structures - AMS 2020.

$^{5}$K. Jiju, S. Gurusamy, and S. Prakash, "Study on preparation of al - sic metal matrix composites using powder metallurgy technique and its me- chanical properties," Materials Today: Proceedings 27, 1843-1847 (2020).

$^{6}$X. Sauvage, E. V. Bobruk, M. Y. Murashkin, Y. Nasedkina, N. A. Enikeev, and R. Z. Valiev, "Optimization of electrical conductivity and strength com- bination by structure design at the nanoscale in al-mg-si alloys," Acta Mater. 98, 355 (2015).

$^{7}$J. Tokutomi, T. Uemura, S. Sugiyama, J. Shiomi, and J. Yanagimoto, "Hot extrusion to manufacture the metal matrix composite of carbon nanotube and aluminum with excellent electrical conductivities and mechanical prop- erties," CIRP Annals - Manufacturing Technology 64, 257-260 (2015).

$^{8}$F. A. Chyada, A. R. Jabur, and H. A. Alwan, "Effect addition of graphene on electrical conductivity and tensile strength for recycled electric power transmission wires," Energy Procedia 119, 121-130 (2017).

$^{9}$L. Brown, P. Joyce, D. Forrest, and L. Salamanca-Riba, "Physical and me- chanical characterization of a nanocarbon infused aluminum-matrix com- posite," Materials Performance and Characterization 3, 65-80 (2014).

$^{10}$A. M. Ali, M. Z. Omar, H. Hashim, M. S. Salleh, and I. F. Mohamed, "Recent development in graphene-reinforced aluminium matrix composite: A review," Reviews on Advanced Materials Science 60, 801-817 (2021).

$^{11}$X. Zhang and S. Wang, "Interfacial strengthening of graphene/aluminum composites through point defects: A first-principles study." Nanomaterials (Basel) 11, 3 (2021).

$^{12}$D.-Y. Kim and H.-J. Choi, "Recent developments towards commercializa- tion of metal matrix composites," Materials 13, 2828 (2020).

$^{13}$M. S. Ayar, P. M. George, and R. R. Patel, "Advanced research progresses in aluminium metal matrix composites: An overview," AIP Conference Pro- ceedings 2317, 020026 (2021).

$^{14}$M. Cao, Y. Luo, Y. Xie, Z. Tan, G. Fan, Q. Guo, Y. Su, Z. Li, and D.-B. Xiong, "The influence of interface structure on the electrical conductivity of graphene embedded in aluminum matrix," Advanced Materials Interfaces 6, 1900468 (2019).

$^{15}$W. Wang, Y. Liu, T. Wang, K. Sheng, and B. Yu, "Graphene/cu (111) in- terface study: The density functional theory calculations," in 2011 Interna- tional Conference on Electronics, Communications and Control (ICECC) (IEEE, 2011) pp. 265-268.

$^{16}$K. N. Subedi, K. Nepal, C. Ugwumadu, K. Kappagantula, and D. A. Drabold, "Electronic transport in copper-graphene composites," Applied Physics Letters 122, 031903 (2023).

$^{17}$J.-M. Zhang, F. Ma, and K.-W. Xu, "Calculation of the surface energy of fcc metals with modified embedded-atom method," Applied Surface Sci- ence 229, 34-42 (2004).

$^{18}$Y. Wang, M. Li, P. Peng, H. Gao, J. Wang, and B. Sun, "Preferred ori- entation at the al/graphene interface: First-principles calculations and ex- perimental observation," Journal of Alloys and Compounds 900, 163304 (2022).

$^{19}$N. A. Lanzillo, J. B. Thomas, B. Watson, M. Washington, and S. K. Nayak, "Pressure-enabled phonon engineering in metals," Proceedings of the Na- tional Academy of Sciences 111, 8712-8716 (2014).

$^{20}$G. Kresse and J. Hafner, "Ab initio molecular dynamics for liquid metals," Phys. Rev. B 47, 558-561 (1993).

$^{21}$Y. Qi, L. G. Hector, N. Ooi, and J. B. Adams, "A first principles study of adhesion and adhesive transfer at al(111)/graphite(0001)," Surface Science 581, 155-168 (2005).

$^{22}$W. Lee, S. Jang, M. J. Kim, and J. M. Myoung, "Interfacial interactions and dispersion relations in carbon-aluminium nanocomposite systems," Nan- otechnology 19, 285701 (2008).

$^{23}$Y. Qi and L. G. Hector, "Adhesion and adhesive transfer at alu- minum/diamond interfaces: A first-principles study," Phys. Rev. B 69, 235401 (2004).

$^{24}$W. Tang, E. Sanville, and G. Henkelman, "A grid-based bader analysis algorithm without lattice bias," Journal of Physics: Condensed Matter 21, 084204 (2009).

$^{25}$N. K. Hindley, "Random phase model of amorphous semiconductors i. transport and optical properties," Journal of Non-Crystalline Solids 5, 17-30 (1970).

$^{26}$N. K. Hindley, "Random phase model of amorphous semiconductors ii. hot electrons," Journal of Non-Crystalline Solids 5, 31-40 (1970).

$^{27}$L. Friedman and N. F. Mott, "The hall effect near the metal-insulator tran- sition," in Sir Nevill Mott - 65 Years in Physics, pp. 529-534.

$^{28}$L. Friedman, "Hall conductivity of amorphous semiconductors in the ran- dom phase model," Journal of Non-Crystalline Solids 6, 329-341 (1971).

$^{29}$N. F. Mott and E. A. Davis, "Electronic processes in non-crystalline mate- rials," (Clarendon/Oxford University Press, Oxford, New York, 1979) 2nd ed., Chap. 2, pp. 6-58.

$^{30}$R. Kubo, "Statistical-mechanical theory of irreversible processes. i. gen- eral theory and simple applications to magnetic and conduction problems," J.Phys.Soc.Jpn 12, 570-586 (1957).

$^{31}$D. A. Greenwood, "The boltzmann equation in the theory of electrical con- duction in metals," Proc.Phys.Soc. 71, 585-596 (1958).

$^{32}$L. L. Moseley and T. Lukes, "A simplified derivation of the Kubo- Greenwood formula," American Journal of Physics 46, 676-677 (1978).

$^{33}$K. N. Subedi, K. Kappagantula, F. Kraft, A. Nittala, and D. A. Drabold, "Electrical conduction processes in aluminum: Defects and phonons," Phys. Rev. B 105, 104114 (2022).

$^{34}$K. N. Subedi, K. Prasai, M. N. Kozicki, and D. A. Drabold, "Structural ori- gins of electronic conduction in amorphous copper-doped alumina," Phys. Rev. Materials 3, 065605 (2019).

$^{35}$K. N. Subedi, K. Prasai, and D. A. Drabold, "Space-projected conductivity and spectral properties of the conduction matrix," Phys. Status Solidi B 258, 2000438 (2020).

$^{36}$C. Ugwumadu, K. Nepal, R. Thapa, Y. Lee, Y. Al Majali, J. Trembly, and D. Drabold, "Simulation of multi-shell fullerenes using machine-learning gaussian approximation potential," Carbon Trends 10, 100239 (2023).

$^{37}$C. Ugwumadu, R. Thapa, Y. Al-Majali, J. Trembly, and D. A. Drabold, "Formation of amorphous carbon multi-walled nanotubes from random ini- tial configurations," physica status solidi (b) 260, 2200527 (2023).

$^{38}$C. Ugwumadu, R. Thapa, K. Nepal, and D. A. Drabold, "Atomistic nature of amorphous graphite," European Journal of Glass Science and Technol- ogy Part B 64, 16-22 (2023).

$^{39}$R. Thapa, C. Ugwumadu, K. Nepal, J. Trembly, and D. A. Drabold, "Ab initio simulation of amorphous graphite," Phys. Rev. Lett. 128, 236402 (2022).

$^{40}$S. Ono, "C-axis resistivity of graphite in connection with stacking faults," Journal of the Physical Society of Japan 40, 498-504 (1976).

$^{41}$N. Iwashita, H. Imagawa, and W. Nishiumi, "Variation of temperature de- pendence of electrical resistivity with crystal structure of artificial graphite products," carbon 61, 602-608 (2013).

$^{42}$S. Bapat, "Thermal conductivity and electrical resistivity of two types of ATJ-S graphite to $3500^{\circ}$ k," carbon 11, 511-514 (1973).

$^{43}$K. Matsubara, K. Sugihara, and T. Tsuzuku, "Electrical resistance in the c direction of graphite," Phys. Rev. B 41, 969-974 (1990).

Supplementary Material
Physical origin of enhanced electrical conduction in aluminum-graphene composites

K. Nepal,¹, * C. Ugwumadu,¹ K.N. Subedi,² K. Kappagantula,³ and D. A. Drabold¹, †

¹ Department of Physics and Astronomy, Nanoscale and Quantum
Phenomena Institute (NQPI) Ohio University, Athens, Ohio 45701, USA
² Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA
³ Pacific Northwest National Laboratory, Richland, Washington, 99352, USA
(Dated: January 5, 2024)

The electronic and transport properties of aluminum-graphene composite materials were investi-
gated using ab initio plane wave density functional theory. The interfacial structure is reported for
several configurations. In some cases, the face-centered aluminum (111) surface relaxes in a nearly
ideal registry with graphene, resulting in a remarkably continuous interface structure. The Kubo-
Greenwood formula and space-projected conductivity were employed to study electronic conduction
in aluminum single- and double-layer graphene-aluminum composite models. The electronic density
of states at the Fermi level is enhanced by the graphene for certain aluminum-graphene interfaces,
thus, improving electronic conductivity. In double-layer graphene composites, conductivity varies
non-monotonically with temperature, showing an increase between 300-400 K at short aluminum-
graphene distances, unlike the consistent decrease in single-layer composites.

**Sect. S1. SIMULATION PROTOCOL UTILIZED IN VASP FOR CALCULATIONS IN THIS WORK**

All the calculations in this work were performed using the plane wave density functional theory code, VASP (Vienna
ab initio simulation package) [? ]. For geometry optimization using conjugate gradient in VASP (maximum residual
force is less than 0.01 eV/Å), we used a kinetic energy cutoff of 420 eV. For single-point calculations, we used an
energy cutoff of 480 eV. Projected augmented wave (PAW) potentials were implemented for ion-election interactions,
and the generalized gradient approximation (GGA) of Perdew–Burke–Ernzerhof (PBE) as the exchange-correlation
functional [? ? ]. The Brillouin zone was sampled using the Monkhorst-Pack [? ] scheme with $2 \times 2 \times 1$ k-point
meshes as implemented in VASP.

**Sect. S2. PRESSURE-RELAXED AL-G COMPOSITE MODELS**

To impose compression onto the system, the vertical dimension of the composite model was reduced followed by
a structural relaxation. For each compression followed by relaxation, the initial and final interfacial distances were
noted and are listed in Table S1, along with the external pressure on relaxed models computed within VASP. Table
S1 left and right correspond to SL and DL composites. The graphene layer formed on either side was at similar
configurations with the interfacial Al layers after relaxation.

**Sect. S3. SIMULATION PROTOCOL FOR TEMPERATURE-DEPENDENT CONDUCTIVITY CALCULATIONS**

To perform the temperature-dependent conductivity calculations, we followed the simulation protocol outlined in
reference [? ]. Selected models were equilibrated in a canonical ensemble for a temperature range between 100 K
to 600 K, in steps of 50 K. The temperature was maintained using the Nosé-Hoover thermostat. The simulations
were conducted for 3 ps with a timestep of 1.5 fs. For the subsequent conductivity calculations, we selected the last
10 configurations separated by intervals of 50 fs for each temperature considered. At temperatures below the Debye
temperature, classical MD is not justified, as lattice quantization should be considered; however, while the dynamics
are unrealistic it appears that the naive classical sampling yields sensible results when employed with KGF, as we
demonstrated and discussed in detail earlier and discussed in detail [? ].

* kn478619@ohio.edu
† drabold@ohio.edu

TABLE S1. Summary of variation in the interfacial distance for different Al-G models after atomic structure relaxation and corresponding external pressure. The left and right correspond to SL and DL graphene aluminum composites respectively.

<table>
  <thead>
    <tr>
      <th colspan="3">Single</th>
      <th colspan="3">Double</th>
    </tr>
    <tr>
      <td>$\mathrm{^a} \, d_{Al-G}$<br>[$\mathring{A}$]</td>
      <td>$\mathrm{^b} \, d_{Al-G}$<br>[$\mathring{A}$]</td>
      <td>$\mathrm{^c} \, \mathrm{P}$<br>[kB]</td>
      <td>$\mathrm{^a} \, d_{Al-G}$<br>[$\mathring{A}$]</td>
      <td>$\mathrm{^b} \, d_{Al-G}$<br>[$\mathring{A}$]</td>
      <td>$\mathrm{^c} \, \mathrm{P}$<br>[kB]</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3.48</td>
      <td>3.40</td>
      <td>0.27</td>
      <td>3.48</td>
      <td>3.41</td>
      <td>1.15</td>
    </tr>
    <tr>
      <td>3.42</td>
      <td>3.35</td>
      <td>3.42</td>
      <td>3.42</td>
      <td>3.35</td>
      <td>2.77</td>
    </tr>
    <tr>
      <td>3.36</td>
      <td>3.31</td>
      <td>8.41</td>
      <td>3.36</td>
      <td>3.31</td>
      <td>6.25</td>
    </tr>
    <tr>
      <td>3.31</td>
      <td>3.25</td>
      <td>16.82</td>
      <td>3.30</td>
      <td>3.24</td>
      <td>9.72</td>
    </tr>
    <tr>
      <td>3.28</td>
      <td>3.13</td>
      <td>20.09</td>
      <td>3.24</td>
      <td>3.19</td>
      <td>14.35</td>
    </tr>
    <tr>
      <td>3.21</td>
      <td>3.01</td>
      <td>27.29</td>
      <td>3.18</td>
      <td>3.11</td>
      <td>17.50</td>
    </tr>
    <tr>
      <td>3.16</td>
      <td>2.90</td>
      <td>36.68</td>
      <td>3.12</td>
      <td>3.07</td>
      <td>22.66</td>
    </tr>
    <tr>
      <td>3.09</td>
      <td>2.71</td>
      <td>69.76</td>
      <td>3.06</td>
      <td>3.01</td>
      <td>27.64</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>3.00</td>
      <td>2.97</td>
      <td>31.88</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>2.96</td>
      <td>2.94</td>
      <td>34.69</td>
    </tr>
  </tbody>
</table>

$\mathrm{^a}$ Reduced Al-G interfacial distance before conjugate gradient relaxation in VASP
$\mathrm{^b}$ Obtained Al-G interfacial distance after conjugate gradient relaxation was completed
$\mathrm{^c}$ External pressure computed for the compressed models within VASP.

![](./images/1229445149336010791_6.jpg)

FIG. S1. All plot corresponds to the SL model for the different Al-G distances ($d_{Al-G}$) in the x-axis. The conductivity of the relaxed SL models is represented by the gray curve, with $\sigma_0$ denoting the conductivity of the Al-matrix calculated at 300K. The squared density of states at the Fermi level is shown in brown. In the inset, Bader analysis illustrates the average charge gain and loss for C (blue) and Al (green) atoms. Dotted lines are included in all plots as visual aids.