Catalysis
Science &
Technology

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: Z. Zhao and Q.
Liu, Catal. Sci. Technol., 2018, DOI: 10.1039/C7CY02252B.

![](./images/813056351692390401_1.jpg)

This is an Accepted Manuscript, which has been through the
Royal Society of Chemistry peer review process and has been
accepted for publication.

Accepted Manuscripts are published online shortly after
acceptance, before technical editing, formatting and proof reading.
Using this free service, authors can make their results available
to the community, in citable form, before we publish the edited
article. We will replace this Accepted Manuscript with the edited
and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the
author guidelines.

Please note that technical editing may introduce minor changes
to the text and/or graphics, which may alter content. The journal's
standard Terms & Conditions and the ethical guidelines, outlined
in our author and reviewer resource centre, still apply. In no
event shall the Royal Society of Chemistry be held responsible
for any errors or omissions in this Accepted Manuscript or any
consequences arising from the use of any information it contains.

![](./images/813056351692390401_2.jpg)

rsc.li/catalysis

# Layer-dependent properties of $MoS_2$ nanosheets with different crystal structures study by DFT calculations

Zong-Yan Zhao$^*$, Qing-Lu Liu

Faculty of Materials Science and Engineering, Kunming University of Science and Technology,
Kunming 650093, P. R. China

## Abstract

As a typical representative of layered transition metal dichalcogenides, $MoS_2$ nanosheets have been widely studied in both experimental and theoretical works, and have a wide range of applications in the fields of nanotechnology and microelectronics. Based on hybrid functional within density functional theory calculations, the microstructure, electronic structures, and optical properties of $MoS_2$ nanosheets with different crystal phases are investigated. Based on the analyzing of phonon dispersion, it can be determined that 2H-$MoS_2$ monylayer is thermodynamically stable. In the case of 2H-$MoS_2$ nanosheets, the band gap is monotonically decreases from 2.219 to 1.441 eV by the exponential form, as the layer number increases from 1 to infinite. Moreover, 2H-$MoS_2$ monolayer is a direct band gap semiconductor. On the other hand, 3R-$MoS_2$ monolayer still exhibits metallic characteristics, while 1T'-$MoS_2$ monolayer has a very narrow band gap. The main features of electronic structure of $MoS_2$ nanosheets are contributed by the intra-layer interaction, and the inter-layer interaction only induces slight perturbation. But the latter has an important influence on the electronic structure of $MoS_2$ ultrathin nanosheets, especially monolayer. Furthermore, some fitting equations about optical properties are also provided, which not only better understand the variation of electronic structure with respect the layer number changing, but also provide convenient method to determine the layer number of $MoS_2$ nanosheets in practices. These results indicate $MoS_2$ nanosheets may serve as the promising candidates for photo-electrics applications.

## Keywords

2D materials; $MoS_2$; Electronic structure; Optical properties; DFT calculations

### 1. Introduction

A standard of classification for crystal structure is based on the dimensions (i.e. 0D, 1D, 2D, and 3D). Among these types of materials, 2D nanomaterial exhibit extremely high surface conductivity, especially when they are exfoliated to few layers or monolayer. The common morphology of 2D nanomaterial is the ultrathin nanosheet. Owing to the excellent flexibility, 2D nanosheet can be easily spread onto variety of substrates, and also can be used as substrate to load 0D or 1D nanomaterials. These characteristics not only enhance the performance of 2D nanosheet, but also broaden its applications. Thus, due to these unique properties and versatile applications, 2D nanosheets have attracted extensive interests. The most typically successful example of 2D nanomaterial is the exploration and development of graphene.¹ With the research progress of graphene, the graphene-like 2D nanomaterials have been attracted more and more concern. Transition metal sulfides with graphene-like layered structure have become the research focus in recent years.² Among them, MoS₂ has been widely studied as their representative, because it overcomes the drawbacks (for instance: zero band gap) of graphene. At the same time, it still has many advantages of graphene, becoming promising material in assisting or even replacing graphene. Nowadays, tt has potential applications in catalysis, field effect transistors, optoelectronic devices, and spintronic devices, becoming a hotspot in many fields (such as: physics, chemistry, materials, electronics, and so on).

As a typical representative of layered transition metal dichalcogenides (TMDCs), MoS₂ nanosheet has been widely studied in both experimental and theoretical works, and has a wide range of applications in the fields of nanotechnology and microelectronics. In 2005, Novoselov et al. successfully exfoliated MoS₂ monolayer from bulk MoS₂ using a micromechanical cleavage method, that is stable under ambient conditions and exhibit high crystal quality.³,⁴ From then on, researchers have successfully prepared MoS₂ monolayer samples by different methods, implying the existence and attainability of these 2D nanomaterials are reasonable and feasible.⁵⁻¹¹ Zeng et al. found the viability of optical valley control and suggested the possibility of valley-based electronic and optoelectronic applications in MoS₂ monolayers.¹² Mak et al. demonstrated that optical pumping with circularly polarized light can achieve complete dynamic valley polarization in monolayer MoS₂, in which the polarization is retained for longer than 1 ns.¹³ Because monolayer MoS₂ has a direct band gap, it can be used to construct interband tunnel FETs, which offer lower

power consumption than classical transistors.¹⁴ Radisavljevic et al. reported on the first integrated circuit based on a MoS₂ monolayer, and their integrated circuits are capable of operating as inverters, converting logical "1" into logical "0", with room-temperature voltage gain higher than 1, making them suitable for incorporation into digital circuits.¹⁵ On the other hand, the flexible transistor array of MoS₂ monolayer can be used as a highly sensitive gas sensor with excellent reproducibility, which exhibits much higher sensitivity.¹⁶ MoS₂ bulk is an indirect band gap (~1.29 eV at room temperature) semiconductor with negligible photoluminescence, while research shows that the band gap value continues to increase with the decrease of layer numbers. Especially, the MoS₂ monolayer is a direct band gap (~1.8 eV) semiconductor with strong photoluminescence.¹⁷

In the field of photocatalysis, MoS₂ nanosheets also exhibit excellent performances.¹⁸ Xiang et al. studied the synergetic effect of MoS₂ nanosheet and graphene as cocatalysts for enhanced photocatalytic H₂ production activity of TiO₂ nano particles, which reaches a high H₂ production rate of 165.3 μmol h⁻¹.¹⁹ They considered the unusual photocatalytic activity arises from the positive synergetic effect between the MoS₂ nanosheet and graphene components in the hybrid cocatalyst, which serve as an electron collector and a source of active adsorption sites, respectively. Gao et al. reported MoS₂ quantum dots can significantly improve the photocatalysis properties of TiO₂, which is caused by the increased charge separation, visible-light absorbance, specific surface area and reaction sites upon the introduction of MoS₂ quantum dots.²⁰ Zong et al. loaded MoS₂ as cocatalyst on CdS, and found the photocatalytic H₂ evolution can be increased by 36 times under visible light, which is even higher than Pt loading under the same reaction condition.²¹ Joshi et al. generated hydrogen via photoelectrochemical water splitting using films of chemically exfoliated 2D MoS₂ layers.²² They believed 2D MoS₂ is one of the promising candidates as a photocatalyst for light-induced hydrogen generation, and the efficient photoelectrocatalytic property of the 2D MoS₂ is possibly due to availability of catalytically active edge sites together with minimal stacking that favors the electron transfer. Chang et al. observed that 1T'-MoS₂ exhibit higher eletrocatalytic hydrogen activity than that of 2H-MoS₂. But, if the photoharvester semiconductors with a higher conduction band position (such as CdS), 2H-MoS₂ monolayer could act as cocatalyst in photocatalysis, which would be beneficial for photo-excited electron transport into the 2H-MoS₂ monolayer, thus facilitating the hydrogen reduction reaction.²³

Although lots of studies have been involved on different 2D nanosheetss to date, it is also imperative and interesting to look into other layered materials candidates for the low-cost 2D

semiconductor materials. In this work, we will draw attention to $MoS_2$ as low-cost and layered semiconductor material, which are attracting much attention due to its suitable. In the research of new materials, researchers often adjust the properties of existing materials according to the need to expand application range and to optimize device functionality. Density functional theory (DFT) calculations can better help researcher to predict the structure and properties of new materials, but also to provide theoretical explanation for the successful experiments, becoming the strong supporter for experimental and industrial development. For instance, Komsa et al. presented an extensive first-principles study of a large set of native defects in $MoS_2$ in order to find out the types and concentration of the most important defects; $^{24}$ Gao et al. found the band gap values of silicone-$MoS_2$ heterobilayers could be effectively modulated under an external electric field by using DFT calculations, implying silicone-$MoS_2$ heterobilayers to be candidate materials for logic circuits and photonic devices. $^{25}$ Especially, Yun et al. $^{26}$ and Padilha et al. $^{27}$ have traced the evolution of the band structure as a function of the layer number. They found the valence band maximum increase rapidly with the layer number, while the conduction band minimum remains almost constant. Their findings resolve some disagreements (such as the band gap value), which is key to applications of $MoS_2$ in optoelectronics. However, the layer number in their models is less than 3, and they only considered the 2H-$MoS_2$ phase. As far as we know, as varying of the layer number, the physical mechanism to control the electronic structure of $MoS_2$ nanosheets with different crystal phases is still unclear, which is getting closer and closer attention in the field of catalysis (especially photocatalysis). On the other hand, some other relevant polytypes of $MoS_2$ have been shown to be catalytic active, even outperforms their 2H phase counterpart. $^{23, 28-31}$ Therefore, it is necessary to systematically study the tendency and corresponding properties in the evolution process from bulk to monolayer through constructing reasonable structure model of $MoS_2$ nanosheets with different crystal phases, as well as the effects of layer number on the crystal micro-structure, electrical and optical properties.

## 2. Computational methods and models

The DFT calculations were carried out with the CASTEP (Cambridge Serial Total Energy Package) codes. $^{32-35}$ The core electrons were treated with the norm-conserving pseudopotential. In order to obtain accurate properties, the hybrid functional (HSE06) was utilized as the

exchange-correlation functional. $^{36}$ In addition, for the characteristic layer-type lattice, the van der Waals interaction by adding a semi-empirical dispersion potential (D) to the conventional Kohn-Sham DFT energy, through a pair-wise force field following Grimme's DFT-D method, $^{37}$ is incorporated to better describe the non-bonding interaction between the layers. The wave functions of the valence electrons were expanded using a plane-wave basis set within a specified energy cutoff that was chosen as 880 eV. The convergent standards were set as $5 \times 10^{-7}$ eV atom $^{-1}$ for self-consistent field (SCF) tolerance, $0.01$ eV/Å for maximum force, $5 \times 10^{-4}$ Å for maximum displacement tolerances, 0.02 GPa for maximum stress and $5 \times 10^{-6}$ eV atom $^{-1}$ for total energy change in the geometry optimization. Other settings are as follows: The Monkhorst-Pack scheme k-points grid sampling was set as $9 \times 9 \times 1$ for the structural optimization and $16 \times 16 \times 1$ for the properties calculations; an $80 \times 80 \times 200$ mesh was used for fast Fourier transformation.

In order to model the structure of $MoS_{2}$ nanosheet, the primitive cell of 2D layer was directly cut from the optimized 3D $MoS_{2}$ bulk structure along the (001) crystal plane. The reason is that the direction of the van der Waals interaction is along the $c$ vector in the bulk cases. The optimized plane structural parameters of the nanosheets are also similar to bulk cases. When the (001) slab of $MoS_{2}$ was cleaved from the bulk phase, it was separated by a vacuum space of 20-Å-thickness from its periodic image along the normal direction. In the slab models, a finite layer numbers of $MoS_{2}$ in a three-dimensional periodic supercell were utilized to simulate two-dimensional films. Using above mentioned method, the atomic positions in the supercells were optimized to achieve the stable states with minimum total energy. Based on the optimized supercell models, the electronic structure and optical properties were further calculated and analyzed.

## 3. Results and discussions

To check the applicability and accuracy of the computational methods used in the present work, the optimized lattice constants and electronic structures of bulk $MoS_{2}$ with different crystal phases are preparatively investigated by calculating the total energies, electronic structures. The calculation lattice constants of $MoS_{2}$ are listed as following (the values in bracket are the corresponding experimental measuring values $^{38-40}$): (1)1T'-$MoS_{2}$: a = 5.815 Å (5.489 Å), b = 3.244 Å (3.169 Å), c = 5.407 Å (6.162 Å), $\alpha = 90^{\circ}$ ($90^{\circ}$), $\beta = 89.94^{\circ}$ ($90^{\circ}$), $\gamma = 90^{\circ}$ ($90^{\circ}$); (2) 2H-$MoS_{2}$: a = b = 3.185 Å (3.169 Å), c = 12.389 Å (12.324 Å), $\alpha = \beta = 90^{\circ}$ ($90^{\circ}$), $\gamma = 120^{\circ}$ ($120^{\circ}$); (3) 3R-$MoS_{2}$: a = b = 3.192

Å (3.163 Å), c = 18.281 Å (18.370 Å), $\alpha = \beta = 90^\circ$ (90°), $\gamma = 120^\circ$ (120°). In the present work, we chose 1T'-MoS₂ as subject because: 1) it is more stable than 1H and 1T phases (its binding energy is larger by ~8 eV/atom); 2) it present more excellent functional performance, especially non-zero band gap at monolayer in previous literatures.⁴¹,⁴² The detailed structural parameters are listed in Table S1 in Supporting Information. In the present work, 2R-MoS₂ bulk is an indirect band gap semiconductor with band gap of 1.441 eV; while 1T'-MoS₂ bulk and 3R-MoS₂ bulk present zero band gaps as conductor. These results agree with the related experiment and theoretical studies. Thus, according to the results of the above calculations, we can conclude the selected calculation methods should be reliable for the studies of electronic states and optical properties of MoS₂ nanosheets from bulk to monolayer.

### 3.1 Microstructure and Stability

The crystal structure of MoS₂ has three kinds: 1T'-MoS₂, 2H-MoS₂ and 3R-MoS₂, as shown in Figure 1. Among them, the 1T'-MoS₂ and 3R-MoS₂ are the metastable structure, and 2H-MoS₂ is usually the stable structure. 1T'-MoS₂ has tetragonal symmetry with one layer per repeat unit. 2H-MoS₂ has hexagonal symmetry with two layers per repeat unit. 3R-MoS₂ has rhombohedral symmetry with three layers per repeat unit. Moreover, 1T'-MoS₂ and 3R-MoS₂ present the conductive characteristic, and 2H-MoS₂ is a semiconductor. As typical layered structure, the basic structure of MoS₂ is the sandwich layered S-Mo-S structure layer, in which the quasi 2D layer is composed of three layers of atoms: the middle layer is a molybdenum atom layer, upper and lower two layers are sulfur atoms, as shown in Figure 1. Covalent bonds between molybdenum atoms and sulfur atoms form 2D atomic crystals. The multilayer or block of MoS₂ is made up of these sandwiches through a weak van der Waals bond. This results in strong interaction between layers, and the interaction between layers is very weak. Three molybdenum atoms and three sulfur atoms form hexatomic ring, which is the basic unit for the quasi 2D layer. In the cases of 2H and 3R structure, the hexatomic ring is regular hexagon; while in the case of 1T' structure, the hexatomic ring is distorted hexagon. 1T'-MoS₂ and 3R-MoS₂ have octahedral coordination, while 2H-MoS₂ has trigonal prismatic coordination, as shown in Figure 2. At the same time, 2H-MoS₂ and 3R-MoS₂ are centrosymmetric with identical Mo-S bond lengths, while 1T'-MoS₂ lacks inversion symmetry with different Mo-S bond lengths. In addition to the above differences, the dominant difference

between the three crystal structures is the stacking mode of $[MoS_6]$ polyhedron along the $c$-axis. In the case of $1T'-MoS_2$ that contains one layer per lattice cell, each repeating unit is consisted by two distinct $[MoS_6]$ polyhedral, in which S atoms don't overlap along the $c$-axis. The crystal structure of $1T'-MoS_2$ is reconstructed from $1×1×2$ cell of $1T-MoS_2$. More than that, $1T'-MoS_2$ is more stable and exhibits higher activity towards the hydrogen evolution reaction than that of 1T- and $1H-MoS_2$.$^{28}$ In the case of $2H-MoS_2$ that contains two layers per lattice cell, each repeating unit is consisted by a $[MoS_6]$ polyhedron, in which S atoms overlap along the $c$-axis. This stacking mode allows $2H-MoS_2$ to have the maximum interlayer spacing (3.087 Å), which is the most stable of the three structures. In the case of $3R-MoS_2$ that contains three layers per lattice cell, each repeating unit is consisted by a $[MoS_6]$ polyhedron, in which S atoms don't overlap along the $c$-axis. In other words, $3R-MoS_2$ possesses the structural features of $1T'$- and $2H-MoS_2$. The above calculated commendably results reproduced the experimental observations and measurements, $^{43,44}$ and laid a solid foundation for the credibility of the below prediction.

Owing to the weak interaction of van der Waals between layers, the variation of microstructure of $MoS_2$ nanosheet is very inconspicuous, in the evolution process from bulk to monolayer. The first evidence is the variation of bond length distribution, as shown in Table S2 in Supporting Information. In the case of $1T'-MoS_2$, the bond length is slightly increased at the out-side surface (i.e. the 20 layers model), and then almost does not change again until in the bilayer and monolayer models. Finally, it is slightly decreased in the bilayer model, while it is slightly increased again in the monolayer model, except the shorter Mo-S2 bond. In the case of $2H-MoS_2$, the bond length at the out-side surface is firstly decreased, and then slightly increased again; while in the case of $3R-MoS_2$, it is gradually increased. Although there are different variation trends, the variation amplitude of bond length in these three $MoS_2$ systems is quite small (i.e. smaller than ~0.045 Å). The insignificant variation of bond length distribution implies $MoS_2$ nanosheets could keep the main excellent properties of $MoS_2$ bulk that are attributed to the interaction between Mo and S atoms. In other words, the preparation process of $MoS_2$ nanosheets has little impact on the key properties and performance of $MoS_2$, which is very important for the functional applications of $MoS_2$ nanosheets and monolayer.

The second evidence is the variation of layer thickness and layer spacing with respect the layer numbers, as shown in Table S3 and S4 in Supporting Information. In the cases of $1T'-MoS_2$ and $2H-MoS_2$, they are firstly increased, and then slightly decreased in the bilayer model, and finally

slightly increased again in the monolayer. While, in the case of $3R-MoS_2$, they are gradually increased, with the decrease of layer numbers. The variation amplitudes of layer thickness and layer spacing of $2H-MoS_2$ are the largest in the three $MoS_2$ nanosheets, 0.030 and $0.120\ \mathring{A}$, respectively. While, the variation amplitude of layer thickness of $3R-MoS_2$ is the smallest, $0.007\ \mathring{A}$; and the layer spacing of $1T'-MoS_2$ is the smallest, $0.010\ \mathring{A}$. As shown in Figure 3, the variation trends of $2H-MoS_2$ are very particular: when the layer number is larger than 12, the differences of layer thickness or layer spacing are obviously large with respect those of bulk phase; when the layer number is smaller than 7, the differences of layer thickness or layer spacing are almost ignored with respect those of bulk phase. Furthermore, the layer thickness variation of $2H-MoS_2$ is mutated, while the layer spacing variation is gradual, between above trends. Another phenomenon to notice is that the differences of layer thickness and layer spacing between nanosheet and bulk of $1T'-MoS_2$ is relatively large, as similar as the thicker $2H-MoS_2$ nanosheets (layer number is layer than 12); while the differences of layer thickness and layer spacing between nanosheet and bulk of $3R-MoS_2$ is relatively small, as similar as the thinner $2H-MoS_2$ nanosheets (layer number is smaller than 7).

The third evidence is the different energy variation tendency with respect layer number, as shown in Figure 4. The surface energy is calculated by the following formula:
$$E_{surf}=\left[E_{surf-tot}-nE_{bulk-tot}\right]/2S$$
where E<sub>surf-tot</sub> and E<sub>bulk-tot</sub> is the total energy of nanosheet and bulk model, n is the corresponding stoichiometric ratio between surface and bulk models, and S is the surface area. The surface energy of three $MoS_2$ nanosheet is relatively low, less than $0.24\ J/m^2$, indicating the van der Waals interaction between layers. In the cases of $2H-$ and $3R-MoS_2$ nanosheets, the surface energy is exponentially increasing as increasing of layer numbers, and finally converged to 0.183 and $0.233\ J/m^2$, respectively. On the contrary, the surface energy of $1T'-MoS_2$ nanosheets is exponentially decreasing as the increase of layer numbers, and finally converged to $0.005\ J/m^2$. Furthermore, the variation range of surface energy is more obvious in the case of $1T'-MoS_2$ nanosheets. Particularly, in compared to bilayer model, $2H-$ and $3R-MoS_2$ monolayer exhibits obviously decreasing surface energy, while $1T'-MoS_2$ monolayer almost has equal surface energy. To further investigate the formation of $MoS_2$ nanosheets, the cleaving energy is calculated by the following formula:
$$E_{cleav}=\left[E_{N-1}+E_1-E_N\right]/S$$
where N-1, 1, and N is the layer numbers. The cleaving energy can be understood as the energy required cleaving $MoS_2$ monolayer from $MoS_2$ nanosheets with N layers. It can be found that the cleaving energy of three $MoS_2$

nanosheets is exponentially increasing as the increase of layer numbers, and finally converged to 0.288, 0.304, and $0.351\ \text{J/m}^2$, respectively. This calculated result suggests it is relatively easy to prepare $\text{MoS}_2$ monolayer from $\text{MoS}_2$ nanosheets. Moreover, it is easier to get the $\text{MoS}_2$ monolayer from the thinner $\text{MoS}_2$ nanosheets. The binding energy is calculated by the following formula:

$E_{bind} = [\text{nE}_{\text{Mo}} + 2\text{nE}_{\text{S}} - \text{E}_{\text{tot}}]/3\text{n}$ , where n is the atom number of Mo. Similarly, the binding energy is also exponentially increasing as the increase of layer numbers, and finally converged to the corresponding values of bulk phase, 22.28, 22.04, and 22.86 eV/molecule, respectively. Owing to lack of the interaction between layers, the binding energy of $\text{MoS}_2$ monolayer is obviously less than those of other $\text{MoS}_2$ nanosheets. Based on these calculated results, another conclusion could be draw: 2H phase is more energetically stable than the 1T' or 3R phases, because its binding energy are larger than those in 1T' or 3R phase by ~0.58 or ~0.82 eV per unit cell. Finally, the van der Waals energy also calculated. It is found the van der Waals energy is obviously exponentially increasing as the increase of layer numbers, and finally converged to 0.47, 0.36, and $0.37\ \text{J/m}^2$, respectively. These calculated results imply that the interaction between layers of $\text{MoS}_2$ is very weak, result in the possibility to obtain $\text{MoS}_2$ nanosheet and monolayer by mechanical or chemical exfoliation.

The structural stability cannot be ensured, even though the structure can be optimized by minimizing the total energy. To further confirm the structural stability of $\text{MoS}_2$ monolayers, the phonon dispersions of the energetically stable $\text{MoS}_2$ monolayers were calculated, which is an important indication of structural stability. As shown in Figure 5, in the cases of 1T'- and 3R-$\text{MoS}_2$ monolayer, the photon modes at some $k$-points in the Brillouin zone present imaginary frequencies, indicating they are dynamically unstable. On the contrary, in the case of 2H-$\text{MoS}_2$ monolayer, there are no significant imaginary vibrational frequencies in the calculated phonon dispersion curves, indicating that it is dynamically stable. The calculated phonon dispersions of 2H-$\text{MoS}_2$ monolayer is well consistent with previous reported results. $^{45}$ Thus, the $\text{MoS}_2$ monolayer (i.e. 2D $\text{MoS}_2$) with 2H phase is more energetically and dynamically stable, in comparison with 1T' and 3R phases. Moreover, 2H-$\text{MoS}_2$ monolayer has an obvious band gap between acoustic branch and optical branch. The corresponding gap is about 1.10 THz. In the case of 1T'-$\text{MoS}_2$ monolayer, there are obvious overlapping between acoustic branch and optical branch, resulting in non-band gap vibration. In addition, 3R-$\text{MoS}_2$ monolayer has small band gap (~0.15 THz) between acoustic

branch and optical branch. As shown in Figure 2, the symmetry of $[MoS_6]$ polyhedron is belong to the point group of $C_s$ (for $1T'-MoS_2$), $D_{3h}$ (for $2H-MoS_2$), and $D_{3d}$ (for $3R-MoS_2$). From the symmetry point of view, $2H-MoS_2$ has the higher symmetry, thus the atomic vibrational modes present higher degeneracy; while $1T'-MoS_2$ has unequal S lattice sites (as labeled as S1 and S2 as shown in Figure 1) and lower symmetry, thus the atomic vibrational modes present more obvious dispersivity. Based on the results of phonon dispersion, one can further understand the bonding forms between Mo and S atoms in the $1T'-MoS_2$ is relatively complicated, and the versatility of $2H-MoS_2$ monolayer.

### 3.2 Electronic structure

For the applications of $MoS_2$ nanosheets, electronic structure is the key determinant. As shown in Figure 6, the band structures of $MoS_2$ bulk, bilayer, and monolayer with different crystal phases are provided and compared. In the cases of bulk $1T'$- and $3R-MoS_2$, the energy levels are overlapping and crossing the Fermi energy level ($E_F$), indicating the conducting characteristics. On the contrary, bulk $2H-MoS_2$ presents semiconducting characteristics. Its valence band maximum is located at the $\Gamma$ point, while the conduction band minimum is located at the middle of $\Gamma$-K line. The distance between valence band maximum and conduction band minimum is 1.441 eV. So, bulk $2H-MoS_2$ is belongs to the indirect band gap semiconductor. The band gap value of bulk $2H-MoS_2$ is consistent with reported experimental measurements. $^{46}$ The band gap is determined by the crystal potential field. The latter is further determined by the interaction between atomic cores and valence electrons, which is closely related to the crystal structure. In the crystal structure of $2H-MoS_2$, the S atoms overlap along the $c$-axis, which means there is relative strong repulsive force. Thus, the overlapping of wave function is relative weaker, resulting in the existence band gap. In the crystal structures of $1T'$- and $3R-MoS_2$, the S atoms don't overlap along the $c$-axis, which means there is relative strong attractive force. Thus, the overlapping of wave function is relative stronger, resulting in the inexistence band gap. As similar as discussion above, bulk $2H-MoS_2$ presents higher degeneracy; while $1T'-MoS_2$ presents more obvious dispersivity, due to the different symmetry. From bulk to bilayer, and then to monolayer, the features of band structure and E-$k$ dispersion maintain certain similarity. The subtle variations are mainly in the energy level shifting, the change of energy levels near the Fermi level, and the energy level degenerating. This implies once again that it is

possible to retain the excellent photoelectric properties of $MoS_2$, when it is prepared $MoS_2$ nanosheets.

As the layer number decreasing of $2H-MoS_2$ nanosheets from bulk to monolayer, the conduction band minimum is down-shifting from the middle of $\Gamma$-K line towards K point. At the same time, the valence band energy at the K point also up-shifting, and becomes the valence band maximum as same as the $\Gamma$ point. The distance between valence band maximum and conduction band minimum is 2.219 eV. Thus, $2H-MoS_2$ monolayer is belongs to a direct band gap semiconductor with wider band gap of 2.219 eV. This transition has been observed experimentally and theoretically. $^{17,47}$ At the same time, the lowest conduction band becomes doubly degenerate at the K point in bulk $MoS_2$, which is well agreement with previous finding. $^{22}$ However, there has been a lot of controversy about the value of band gap of $2H-MoS_2$, whether it is bulk or monolayer. $^{48}$ In order to clear provide the variation of band gap value of $2H-MoS_2$ nanosheets, the layer dependent curve is illustrated in Figure 7. As the layer number increases from 1 to infinite (i.e. bulk), the band gap is monotonically decreases from 2.219 to 1.441 eV, which is similar with reported observations. $^{49}$ Furthermore, the variation tendency is well represented by an exponential change, and the fitting curve is also plotted in Figure 7. When the layer number is reached to 8 ML, the band gap is almost equal to that of bulk $2H-MoS_2$. On the other hand, one can find that the variation range of band gap is relatively small (~0.27 eV), if the layer number is larger than 1 ML. However, the band gap of $2H-MoS_2$ monolayer is larger than that of $2H-MoS_2$ bilayer by 0.512 eV. This seems to suggest that the band gap variations are mainly caused by interlayer van der Waals interactions. As shown in Figure 4, different energy forms are obviously changed from bilayer to monolayer. In the published literatures, Li et al. found the inter-layer interaction vanishes, when the inter-sheet separation is greater than 4.5 Å, result that the band gap of bilayer is equal to that of monolayer. $^{49}$

The situations of $1T'-MoS_2$ and $3R-MoS_2$ are slightly different with that of $2H-MoS_2$. In compared with $2H-MoS_2$, the conduction band shifting is almost ignored. The most obvious different is the energy levels shifting near the Fermi energy level in the case of $1T'-MoS_2$: (1) In the B-D line, the valence band is down-shifting, while the conduction band is up-shifting, as the decreasing of layer numbers. Finally, they are completely separated to form a band gap about 0.683 eV in this region. On the contrary, in the bulk phase, they are overall overlapping together; while in the bilayer, they are just contact together. In other words, in the B-D line, $1T'-MoS_2$ nanosheets

exhibit metallic conductivity when the layer number is larger than 2; 1T'-MoS₂ bilayer exhibits semi-metallic conductivity; while 1T'-MoS₂ monolayer exhibits semiconducting conductivity. (2) In the $\Gamma$-Y line, the valence band top and conduction band bottom are separated each other with a band gap about 0.226 eV. As the decreasing of layer number, the valence band top is up-shifting, while the conduction band bottom is down-shifting. Thus, they are partially overlapping in this wave vector region, in the case of 1T'-MoS₂ bilayer. Interestingly, in the case of 1T'-MoS₂ monolayer, the valence band top and conduction band bottom are separated again, with a band gap about 0.076 eV, which is consistent with previous results.⁴² According to the inset in Figure 6, one can find the reason is the energy degeneracy at the valence band top in this region. For the existence of latter band gap of 0.076 eV, the minimum band gap of 1T'-MoS₂ monolayer is very small. In the case of 3R-MoS₂, the main variations are mainly exhibited by the energy levels degeneracy and the energy level shifting near the Fermi energy level at the $\Gamma$ point. As shown in Figure 4, the surface energy and cleaving energy of 3R-MoS₂ are the largest, while the binding energy and van der Waals energy of 3R-MoS₂ are the smallest, among these three crystal phases. These calculated results suggest that the main features of electronic structure of MoS₂ nanosheets are contributed by the intra-layer interaction, and the inter-layer interaction only induces slight perturbation. On the other hand, these calculated results could further explain some reported experimental phenomenon. For example, the metallic property or narrow band gap makes 1T'-MoS₂ monolayer can easily capture photo-excited electrons, facilitating the catalytic HER activities; if the CB edge of photocatalyst is higher than that of 2H-MoS₂ monolayer, it can not only capture photo-excited electrons which serve as an electron collector and a source of active adsorption sites, but also absorb more visible light.¹⁹,²³ On the other hand, 1T'-MoS₂ monolayer is the most HER active polytype, because there are HER active sites both on the basal plane and at the edges of the layered grains. In comparison, the basal planes of 1H- and 1T- MoS₂ monolayers are HER inactive and their edge-sites are still not as active as those of the 1T0 polytype.²⁸

Combination above analysis, one can draw that the main characteristics of electronic structure of MoS₂ nanosheets are contributed by the intra-layer interaction. Thus, they can be kept as the decreasing of layer number, in the process from MoS₂ bulk to MoS₂ monolayer. However, owing to the different inter-layer interaction among these three crystal phases, it exhibits different impacts in the process from MoS₂ bulk to MoS₂ monolayer. The significant variations take place the valence band top and conduction band bottom, because these electronic states originate from a linear

combination of $p_{z}$ orbitals on S atoms and $d_{z^{2}}$ orbitals on Mo atoms, which are rather delocalized and have an antibonding nature. $^{50}$ When the inter-layer interaction is decreased or vanished, they will up-shifting. On the other hand, in the energy range of -13~-16 eV, there is an isolated energy band that mainly composed by the S-3s states that is semi-core energy levels, as shown in Figure S1 in Supporting Information. So, compared these semi-core energy levels, one can find the energy band shifting of $MoS_{2}$ nanosheets from bulk to monolayer. Based on this criterion, the energy band shifting of $2H-MoS_{2}$ nanosheets is very obvious, while that of $3R-MoS_{2}$ is least obvious. In summary, the band gap varies when the layer number of $MoS_{2}$ nanosheets is decrease. The reasons can be understood as following: (1) the valence band top is down-shifting, while the conduction band bottom is up-shifting; (2) the splitting of the bands that delimit the band gap becomes less pronounced; (3) the inter-layer interaction is reduced when the layer number is decreased. The less interaction between the orbital leads to smaller band dispersion and larger band gap. These variations in character present an interesting opportunity for engineering the electronic properties of $MoS_{2}$ nanosheets as a function of interlayer separation and/or number of layers. For example, the freestanding $MoS_{2}$ monolayer exhibits an increase in luminescence quantum efficiency by more than a factor of $10^{4}$ compared with the bulk material. $^{51}$

### 3.3 Optical properties

As an important application of photoelectric functional materials of $MoS_{2}$ nanosheets, the calculation of optical properties not only can provide relevant direct evidence and information, but also can further explain the variation about electronic structure. At the same time, the calculation of the optical properties depended on layer numbers can also provide the related measurement basis for $MoS_{2}$ nanosheets, because optical measuring is relatively easy to carry out.

As shown in Figure 8, the static dielectric constant ($\varepsilon_{1}(0)$) and static refractive index (n(0)) present the same tendency as function of layer number: they are monotonically increasing by the exponential forms with the increase of the layer number, and eventually converged to a certain value. Moreover, the converged values are much closed to the corresponding value of $MoS_{2}$ bulk, as indicated the dot dash lines in Figure 8, except $1T'-MoS_{2}$. For the monolayers, the $\varepsilon_{1}(0)$ and n(0) values are almost equal in these three crystal phases. When the layer number is larger than 2, the values of $\varepsilon_{1}(0)$ and n(0) of $2H-MoS_{2}$ nanoseets are obviously smaller than those of other nanosheets.

The fitting formulas are listed as following:

1T'-MoS₂: $\varepsilon_1(0)=15.967-17.158\exp(-n/4.25);\ n(0)=3.991-3.338\exp(-n/3.278)$ (eqn. 1)

2H-MoS₂: $\varepsilon_1(0)=5.580-5.512\exp(-n/2.44);\ n(0)=2.330-1.392\exp(-n/2.401)$ (eqn. 2)

3R-MoS₂: $\varepsilon_1(0)=12.565-15.117\exp(-n/2.758);\ n(0)=3.588-3.176\exp(-n/2.416)$ (eqn. 3)

The high frequency dielectric constant ($\varepsilon_1 (\infty)$) and refractive index (n($\infty$)) are also illustrated in Figure 8. They present different variation tendency: (1) they are monotonically decreasing by the exponential forms with the increase of the layer number; (2) their decay coefficients are relatively large, so they present almost linearly decay; (3) the differences between these three crystal phases are relatively small; (4) the differences between coverage values and the corresponding values of bulk are relatively large. The values and variation tendency of 2H-MoS₂ is almost as same as those of 1T'-MoS₂, while the values of 3R-MoS₂ are relatively large. The fitting formulas are listed as following:

1T'-MoS₂: $\varepsilon_1(\infty)=0.552+0.363\exp(-n/25.419);\ n(\infty)=0.729+0.228\exp(-n/29.029)$ (eqn. 4)

2H-MoS₂: $\varepsilon_1(\infty)=0.552+0.362\exp(-n/27.178);\ n(\infty)=0.735+0.221\exp(-n/30.181)$ (eqn. 5)

3R-MoS₂: $\varepsilon_1(\infty)=0.640+0.272\exp(-n/21.539);\ n(\infty)=0.791+0.164\exp(-n/24.048)$ (eqn. 6)

For the applications of nanosheets or ultrathin films, the other facile parameters of optical properties are the absorption and reflectivity spectra. As shown in Figure S2 and S3 in Supporting Information, the absorption and reflectivity spectra in ultraviolet to visible light region (100-700 nm) of MoS₂ nanosheets are plotted, in which the corresponding spectra of MoS₂ as the reference are also presented. For 2H-MoS₂ nanosheet, the optical absorption properties are consistent with previous reported results: the 600-700 nm absorption originates from the interband excitonic transitions, and the 400-450 nm absorption arises from the transitions between the higher density of state regions.⁵² As the layer number is decreasing, the absorption coefficient and reflectivity is decreasing. In the cases of 1T'- and 2H-MoS₂ nanosheets, there is an obvious band centered at ~180 nm, while there is an obvious band centered at ~220 nm in the case of 3R-MoS₂. Other important phenomenon is that this band edge is gradually blue-shifting, as the decreasing of the layer number. As discussed the variation of electronic structure above, the band position will be shifted when the layer number is decreased: the valence band or the energy band below the Fermi energy level will be down-shifted, while the conduction band or the energy band above the Fermi energy level will be

up-shifted. Thus, the required energy for the electronic transition is increased, so that the corresponding absorption peak or reflection peak will be produced blue-shifting. These calculated results suggest that the variations of electronic structure or energy band shifting of $MoS_2$ nanosheets can be visually displayed and conveniently characterized by the movement of absorption peak or reflected peak.

To further explore the optical properties those are depended to the layer number of $MoS_2$ nanosheets, the values at the band center of absorption and reflectivity spectra are extracted and illustrated in Figure 9. Similarly, the calculated results are also present monotonically increasing by the exponential forms, as the increasing of layer number. From bulk to monolayer, the values of absorption coefficient and reflectivity are about halfway down. Among these three crystal phases, $2H-MoS_2$ nanosheets have the largest absorption coefficient and reflectivity, while $3R-MoS_2$ nanosheets have the smallest absorption coefficient and reflectivity. The fitting formulas are listed as following:

1T'-MoS₂: $\alpha(\sim 185 nm)=2.360-1.558\exp(-n/3.60);\ f(\sim 185 nm)=0.440+0.320\exp(-n/2.952)$

(eqn. 7)

2H-MoS₂: $\alpha(\sim 185 nm)=2.725-1.656\exp(-n/3.973);\ f(\sim 185 nm)=0.492+0.312\exp(-n/3.30)$

(eqn. 8)

3R-MoS₂: $\alpha(\sim 220 nm)=1.797-1.262\exp(-n/3.220);\ f(\sim 220 nm)=0.392+0.306\exp(-n/2.866)$

(eqn. 9)

The equations 1~9 not only explains the variation tendency of optical properties of $MoS_2$ nanosheets, but also better understand the variation of electronic structure. At the same time, it is convenient to determine the layers number of $MoS_2$ nanosheets in experiments by using these equations.

## 4. Conclusions

In order to explore the intrinsic properties depended on layer number, the microstructure, electronic structure, and optical properties of $1T'-/2H-/3R-MoS_2$ nanosheets with different layer numbers were calculated by hybrid functional within density functional theory. Owing to the weak interaction of van der Waals, the variation of microstructure of $MoS_2$ nanosheet is very

inconspicuous in the evolution process from bulk to monolayer: the variation of bond length distribution, layer thickness, and layer spacing with respect the layer numbers could be ignored; the variation of different energy forms (surface energy, cleaving energy, binding energy, and van der Waals energy) with respect layer number are very slight. Based on the phonon dispersion, the $MoS_2$ monolayer with 2H phase (i.e. 2D $MoS_2$) is more energetically and dynamically stable. From bulk to bilayer, and then to monolayer, the features of band structure and E-$k$ dispersion maintain certain similarity. The subtle variations are mainly in the energy level shifting, the change of energy levels near the Fermi level, and the energy level degenerating. In the case of 2H-$MoS_2$, the band gap is monotonically decreases from 2.219 to 1.441 eV as the layer number increases from 1 to infinite. Moreover, 2H-$MoS_2$ monolayer is a direct band gap semiconductor. 1T'-$MoS_2$ nanosheets exhibit metallic conductivity when the layer number is larger than 2; 1T'-$MoS_2$ bilayer exhibits semi-metallic conductivity; while 1T'-$MoS_2$ monolayer exhibits semiconducting conductivity with a narrow band gap of 0.076 eV. The main features of electronic structure of $MoS_2$ nanosheets are contributed by the intra-layer interaction, and the inter-layer interaction only induces slight perturbation. But the latter has an important influence on the electronic structure of $MoS_2$ ultrathin nanosheets, especially monolayer. These variations in character present an interesting opportunity for the modulation of electronic properties of $MoS_2$ nanosheets as a function of interlayer separation and/or number of layers. The calculated optical properties not only explain the variation tendency of optical properties of $MoS_2$ nanosheets, but also better understand the variation of electronic structure. At the same time, it is convenient to determine the layers number of $MoS_2$ nanosheets in experiments by using the fitting equations in the present work.

## Author Information

### Corresponding Author
*E-mail: zzy@kmust.edu.cn. . Tel: +86-871-65109952, Fax: +86-871-65107922.

## Notes
The authors declare no competing financial interest.

## Acknowledgements

The authors would like to acknowledge financial support from the National Natural Science Foundation of China (Grant No. 21473082), and the 18th Yunnan Province Young Academic and Technical Leaders Reserve Talent Project (Grant No. 2015HB015).

## References

1.  K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva and A. A. Firsov, *Science*, 2004, **306**, 666.

2.  R. Ganatra and Q. Zhang, *ACS Nano*, 2014, **8**, 4074-4099.

3.  K. S. Novoselov, D. Jiang, F. Schedin, T. J. Booth, V. V. Khotkevich, S. V. Morozov and A. K. Geim, *P. Natl. Acad. Sci. Usa.*, 2005, **102**, 10451-10453.

4.  K. S. Novoselov, A. Mishchenko, A. Carvalho and A. H. Castro Neto, *Science*, 2016, **353**.

5.  J. N. KavathekarColeman, M. Lotya, A. O'Neill, S. D. Bergin, P. J. King, U. Khan, K. Young, A. Gaucher, S. De, R. J. Smith, I. V. Shvets, S. K. Arora, G. Stanton, H.-Y. Kim, K. Lee, G. T. Kim, G. S. Duesberg, T. Hallam, J. J. Boland, J. J. Wang, J. F. Donegan, J. C. Grunlan, G. Moriarty, A. Shmeliov, R. J. Nicholls, J. M. Perkins, E. M. Grieveson, K. Theuwissen, D. W. McComb, P. D. Nellist and V. Nicolosi, *Science*, 2011, **331**, 568-571.

6.  R. J. Smith, P. J. King, M. Lotya, C. Wirtz, U. Khan, S. De, A. O'Neill, G. S. Duesberg, J. C. Grunlan, G. Moriarty, J. Chen, J. Wang, A. I. Minett, V. Nicolosi and J. N. Coleman, *Adv. Mater.*, 2011, **23**, 3944-3948.

7.  K.-G. Zhou, N.-N. Mao, H.-X. Wang, Y. Peng and H.-L. Zhang, *Angew. Chem. Int. Ed.*, 2011, **50**, 10839-10842.

8.  Y.-H. Lee, X.-Q. Zhang, W. Zhang, M.-T. Chang, C.-T. Lin, K.-D. Chang, Y.-C. Yu, J. T.-W. Wang, C.-S. Chang, L.-J. Li and T.-W. Lin, *Adv. Mater.*, 2012, **24**, 2320-2325.

9.  A. Castellanos-Gomez, M. Barkelid, A. M. Goossens, V. E. Calado, H. S. J. van der Zant and G. A. Steele, *Nano Lett.*, 2012, **12**, 3187-3192.

10. J. J. Scragg, J. T. Wätjen, M. Edoff, T. Ericson, T. Kubart and C. Platzer-Björkman, *J. Am. Chem. Soc.*, 2012, **134**, 19330-19333.

11. X. Wang, H. Feng, Y. Wu and L. Jiao, *J. Am. Chem. Soc.*, 2013, **135**, 5304-5307.

12. H. Zeng, J. Dai, W. Yao, D. Xiao and X. Cui, *Nat Nano*, 2012, **7**, 490-493.

13. K. F. Mak, K. He, J. Shan and T. F. Heinz, *Nat Nano*, 2012, **7**, 494-498.

14. RadisavljevicB, RadenovicA, Briviol, GiacomettiV and KisA, *Nat Nano*, 2011, **6**, 147-150.

15. B. Radisavljevic, M. B. Whitwick and A. Kis, *ACS Nano*, 2011, **5**, 9934-9938.

16. Q. He, Z. Zeng, Z. Yin, H. Li, S. Wu, X. Huang and H. Zhang, *Small*, 2012, **8**, 2994-2999.

17. A. Splendiani, L. Sun, Y. Zhang, T. Li, J. Kim, C.-Y. Chim, G. Galli and F. Wang, *Nano Lett.*, 2010, **10**, 1271-1275.

18. Y. Li, Y.-L. Li, C. M. Araujo, W. Luo and R. Ahuja, *Catalysis Science & Technology*, 2013, **3**, 2214-2220.

19. Q. Xiang, J. Yu and M. Jaroniec, *J. Am. Chem. Soc.*, 2012, **134**, 6575-6578.

20. W. Gao, M. Wang, C. Ran and L. Li, *Chem. Commun.*, 2015, **51**, 1709-1712.

21. X. Zong, H. Yan, G. Wu, G. Ma, F. Wen, L. Wang and C. Li, *J. Am. Chem. Soc.*, 2008, **130**, 7176-7177.

22. R. K. Joshi, S. Shukla, S. Saxena, G.-H. Lee, V. Sahajwalla and S. Alwarappan, *AIP Advances*, 2016, **6**, 015315.

23. K. Chang, X. Hai, H. Pang, H. Zhang, L. Shi, G. Liu, H. Liu, G. Zhao, M. Li and J. Ye, *Adv. Mater.*, 2016, **28**, 10033-10041.

24. H.-P. Komsa and A. V. Krasheninnikov, *Phys. Rev. B*, 2015, **91**, 125304.

25. N. Gao, J. C. Li and Q. Jiang, *Phys. Chem. Chem. Phys.*, 2014, **16**, 11673-11678.

26. W. S. Yun, S. W. Han, S. C. Hong, I. G. Kim and J. D. Lee, *Phys. Rev. B*, 2012, **85**, 033305.

27. J. E. Padilha, H. Peelaers, A. Janotti and C. G. Van de Walle, *Phys. Rev. B*, 2014, **90**, 205420.

28. X.-L. Fan, Y. Yang, P. Xiao and W.-M. Lau, *Journal of Materials Chemistry A*, 2014, **2**, 20545-20551.

29. C. Dajin, L. Song, L. Huanhuan, L. Can, L. Lei, G. Yinyan, N. Lengyuan, L. Xinjuan and W. Tao, *Materials Research Express*, 2017, **4**, 035908.

30. R. J. Toh, Z. Sofer, J. Luxa, D. Sedmidubsky and M. Pumera, *Chem. Commun.*, 2017, **53**, 3054-3057.

31. D. Voiry, M. Salehi, R. Silva, T. Fujita, M. Chen, T. Asefa, V. B. Shenoy, G. Eda and M. Chhowalla, *Nano Lett.*, 2013, **13**, 6222-6227.

32. D. Vanderbilt, *Phys. Rev. B*, 1990, **41**, 7892.

33. J. A. Rodriguez, G. Liu, T. Jirsak, J. Hrbek, Z. Chang, J. Dvorak and A. Maiti, *J. Am. Chem. Soc.*, 2002, **124**, 5242-5250.

34. K. Okazaki, Y. Morikawa, S. Tanaka, K. Tanaka and M. Kohyama, *Phys. Rev. B*, 2004, **69**, 235404.

35. N. Lopez and J. K. Nørskov, *J. Am. Chem. Soc.*, 2002, **124**, 11262-11263.

36. A. V. Krukau, O. A. Vydrov, A. F. Izmaylov and G. E. Scuseria, *J. Chem. Phys.*, 2006, **125**, 224106-224105.

37. S. Grimme, *J. Comput. Chem.*, 2006, **27**, 1787-1799.

38. V. Petkov, S. J. L. Billinge, P. Larson, S. D. Mahanti, T. Vogt, K. K. Rangan and M. G. Kanatzidis, *Phys. Rev. B*, 2002, **65**, 092105.

39. J. Heising and M. G. Kanatzidis, *J. Am. Chem. Soc.*, 1999, **121**, 11720-11732.

40. B. Schönfeld, J. J. Huang and S. C. Moss, *Acta Crystallogr. Sec. B*, 1983, **39**, 404-407.

41. X. Qian, J. Liu, L. Fu and J. Li, *Science*, 2014, **346**, 1344-1347.

42. T. Olsen, *Phys. Rev. B*, 2016, **94**, 235106.

43. E. Benavente, M. A. Santa Ana, F. Mendizábal and G. González, *Coordin. Chem. Rev.*, 2002, **224**, 87-109.

44. Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman and M. S. Strano, *Nat Nano*, 2012, **7**, 699-712.

45. C. Ataca, M. Topsakal, E. Aktürk and S. Ciraci, *J. Phys. Chem. C*, 2011, **115**, 16354-16361.

46. R. Coehoorn, C. Haas and R. A. de Groot, *Phys. Rev. B*, 1987, **35**, 6203-6206.

47. K. Dolui, I. Rungger, C. Das Pemmaraju and S. Sanvito, *Phys. Rev. B*, 2013, **88**, 075420.

48. J. A. Miwa, S. Ulstrup, S. G. Sørensen, M. Dendzik, A. G. Čabo, M. Bianchi, J. V. Lauritsen and P. Hofmann, *Phys. Rev. Lett.*, 2015, **114**, 046802.

49. T. Li and G. Galli, *J. Phys. Chem. C*, 2007, **111**, 16192-16196.

50. L. F. Mattheiss, *Phys. Rev. B*, 1973, **8**, 3719-3740.

51. K. F. Mak, C. Lee, J. Hone, J. Shan and T. F. Heinz, *Phys. Rev. Lett.*, 2010, **105**, 136805.

52. K. Wang, J. Wang, J. Fan, M. Lotya, A. O'Neill, D. Fox, Y. Feng, X. Zhang, B. Jiang, Q. Zhao, H. Zhang, J. N. Coleman, L. Zhang and W. J. Blau, *ACS Nano*, 2013, **7**, 9260-9267.

# Captions of Figures

Figure 1. The bulk crystal structure of $MoS_2$ with different phases.

Figure 2. The constructing unit and the corresponding polyhedron of $MoS_2$ in different crystal phases

Figure 3. The layer thickness and layer spacing of $MoS_2$ nanosheets with respect of layer numbers

Figure 4. Different energy forms of $MoS_2$ nanosheets with respect of layer numbers

Figure 5. The calculated phonon dispersion of $MoS_2$ nanosheets with different crystal phases

Figure 6. The calculated band structure of $MoS_2$ nanosheets: bulk, bilayer, and monolayer, with different crystal phases

Figure 7. The band gap of 2H-$MoS_2$ nanosheets with respect of layer numbers, the dot dashed line repents the corresponding value of bulk

Figure 8. The dielectric function and refractive index of $MoS_2$ nanosheets with respect of layer numbers, the dot dashed line repents the corresponding value of bulk

Figure 9. The absorption coefficient and reflectivity of $MoS_2$ nanosheets with respect of layer numbers, the dot dashed line repents the corresponding value of bulk

![](./images/813056351692390401_3.jpg)

Figure 1. The bulk crystal structure of $MoS_2$ with different phases.

![](./images/813056351692390401_4.jpg)

Figure 2. The constructing unit and the corresponding polyhedron of $MoS_2$ in different crystal phases

![](./images/813056351692390401_5.jpg)

Figure 3. The layer thickness and layer spacing of $MoS_2$ nanosheets with respect of layer numbers

![](./images/813056351692390401_6.jpg)

Figure 4. Different energy forms of $\text{MoS}_2$ nanosheets with respect of layer numbers

![](./images/813056351692390401_7.jpg)

Figure 5. The calculated phonon dispersion of MoS₂ nanosheets with different crystal phases

![](./images/813056351692390401_8.jpg)

Figure 6. The calculated band structure of $MoS_2$ nanosheets: bulk, bilayer, and monolayer, with different crystal phases

![](./images/813056351692390401_9.jpg)

Figure 7. The band gap of 2H-MoS₂ nanosheets with respect of layer numbers, the dot dashed line
repents the corresponding value of bulk

![](./images/813056351692390401_10.jpg)

Figure 8. The dielectric function and refractive index of $MoS_2$ nanosheets with respect of layer numbers, the dot dashed line repents the corresponding value of bulk

![](./images/813056351692390401_11.jpg)

Figure 9. The absorption coefficient and reflectivity of $MoS_2$ nanosheets with respect of layer numbers, the dot dashed line repents the corresponding value of bulk

For Table of Contents Only

![](./images/813056351692390401_12.jpg)

Synopsis: The main features of electronic structure of $MoS_2$ nanosheets are contributed by the intra-layer interaction, and the inter-layer interaction only induces slight perturbation. But the latter has an important influence on the electronic structure of $MoS_2$ ultrathin nanosheets, especially monolayer.